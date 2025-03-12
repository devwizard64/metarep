#include <sm64.h>

static short quicksand_speed[] = {12, 8, 4};

UNUSED static int physics_8033B290;

BGFACE water_ground =
	{BG_19, 0, 0, 0, 0, 0, {0, 0, 0}, {0, 0, 0}, {0, 0, 0}, 0, 1, 0, 0, NULL};

float PL_GetTrampolinePower(void)
{
	return 0;
}

void PL_CheckTrampoline(UNUSED PLAYER *pl)
{
}

void TrampolineProc(void)
{
}

void BumpCollision(BUMP *a, BUMP *b)
{
	float dx = b->posx - a->posx;
	float dz = b->posz - a->posz;
	float sa = ( dx*a->velx + dz*a->velz) / (dx*dx + dz*dz);
	float sb = (-dx*b->velx - dz*b->velz) / (dx*dx + dz*dz);
	b->velx += b->power*sa*dx - sb*-dx;
	b->velz += b->power*sa*dz - sb*-dz;
	a->velx += -sa*dx + a->power*sb*-dx;
	a->velz += -sa*dz + a->power*sb*-dz;
}

VOID BumpInit(
	BUMP *bump, float posx, float posz, float speed, SHORT angy, float power,
	float radius
)
{
	if (speed < 0)
	{
		speed *= -1;
		angy += 0x8000;
	}
	bump->radius = radius;
	bump->power = power;
	bump->posx = posx;
	bump->posz = posz;
	bump->velx = speed*SIN(angy);
	bump->velz = speed*COS(angy);
}

void PL_Reflect(PLAYER *pl, int flag)
{
	if (pl->wall)
	{
		SHORT angy = ATAN2(pl->wall->nz, pl->wall->nx);
		pl->ang[1] = angy - (short)(pl->ang[1] - angy);
		Na_ObjSePlay(pl->flag & PL_METALCAP ? NA_SE0_42 : NA_SE0_45, pl->obj);
	}
	else
	{
		Na_ObjSePlay(NA_SE0_44_C0, pl->obj);
	}
	if (flag)   PL_SetSpeed(pl, -pl->speed);
	else        pl->ang[1] += 0x8000;
}

int PL_ProcSink(PLAYER *pl, float sink)
{
	if (pl->state & PF_RIDE)
	{
		pl->sink = 0;
	}
	else
	{
		if (pl->sink < 1.1F) pl->sink = 1.1F;
		switch (pl->ground->code)
		{
		case BG_33:
			if ((pl->sink += sink) >= 10) pl->sink = 10;
			break;
		case BG_37:
			if ((pl->sink += sink) >= 25) pl->sink = 25;
			break;
		case BG_38:
		case BG_39:
			if ((pl->sink += sink) >= 60) pl->sink = 60;
			break;
		case BG_34:
		case BG_36:
			if ((pl->sink += sink) >= 160)
			{
				player_802521A0(pl);
				return PL_SetStateDrop(pl, PS_DEMO_12, 0);
			}
			break;
		case BG_35:
		case BG_45:
			player_802521A0(pl);
			return PL_SetStateDrop(pl, PS_DEMO_12, 0);
			break;
		default:
			pl->sink = 0;
			break;
		}
	}
	return FALSE;
}

int PL_SteepFall(PLAYER *pl, u32 state, u32 code)
{
	short dang = pl->ground_ang - pl->ang[1];
	if (-0x4000 < dang && dang < 0x4000)
	{
		pl->speed = 16;
		pl->ang[1] = pl->ground_ang;
	}
	else
	{
		pl->speed = -16;
		pl->ang[1] = pl->ground_ang + 0x8000;
	}
	return PL_SetState(pl, state, code);
}

int PL_ProcQuicksand(PLAYER *pl)
{
	BGFACE *ground = pl->ground;
	int code = ground->code;
	if (code == BG_36 || code == BG_37 || code == BG_39 || code == BG_45)
	{
		SHORT ang = ground->attr << 8;
		float speed = quicksand_speed[ground->attr >> 8];
		pl->vel[0] += speed*SIN(ang);
		pl->vel[2] += speed*COS(ang);
		return TRUE;
	}
	return FALSE;
}

int PL_ProcWind(PLAYER *pl)
{
	BGFACE *ground = pl->ground;
	if (ground->code == BG_44)
	{
		float acc;
		short angy = ground->attr << 8;
		if (pl->state & PF_WALK)
		{
			short dang = pl->ang[1] - angy;
			acc = pl->speed > 0 ? -pl->speed*0.5F : -8;
			if (-0x4000 < dang && dang < 0x4000) acc *= -1;
			acc *= COS(dang);
		}
		else
		{
			acc = 3.2F + (gfx_frame & 3);
		}
		pl->vel[0] += acc * SIN(angy);
		pl->vel[2] += acc * COS(angy);
#if REVISION < 199609
		Na_ObjSePlay(NA_SE4_10, pl->obj);
#endif
		return TRUE;
	}
	return FALSE;
}

void PL_Stop(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	PL_SetSpeed(pl, 0);
	pl->vel[1] = 0;
	pl->pos[1] = pl->ground_y;
	FVecCpy(obj->s.pos, pl->pos);
	SVecSet(obj->s.ang, 0, pl->ang[1], 0);
}

int PL_ProcWait(PLAYER *pl)
{
	int flag;
	OBJECT *obj = pl->obj;
	int result = TRUE;
	PL_SetSpeed(pl, 0);
	flag  = PL_ProcQuicksand(pl);
	flag |= PL_ProcWind(pl);
	if (flag)
	{
		result = PL_ProcWalk(pl);
	}
	else
	{
		pl->pos[1] = pl->ground_y;
		FVecCpy(obj->s.pos, pl->pos);
		SVecSet(obj->s.ang, 0, pl->ang[1], 0);
	}
	return result;
}

static int PL_CheckWalk(PLAYER *pl, FVEC pos)
{
	UNUSED BGFACE *near;
	BGFACE *wall, *roof, *ground;
	float roof_y, ground_y, water_y;
	near = PL_CheckWall(pos, 30, 24);
	wall = PL_CheckWall(pos, 60, 50);
	ground_y = BGCheckGround(pos[0], pos[1], pos[2], &ground);
	roof_y = PL_CheckRoof(pos, ground_y, &roof);
	water_y = BGCheckWater(pos[0], pos[2]);
	pl->wall = wall;
	if (!ground) return WALK_STOP;
	if (pl->state & PF_RIDE)
	{
		if (ground_y < water_y)
		{
			ground_y = water_y;
			ground = &water_ground;
			ground->nw = ground_y;
		}
	}
	if (pos[1] > ground_y+100)
	{
		if (pos[1]+160 >= roof_y) return WALK_STOP;
		FVecCpy(pl->pos, pos);
		pl->ground = ground;
		pl->ground_y = ground_y;
		return WALK_FALL;
	}
	if (ground_y+160 >= roof_y) return WALK_STOP;
	FVecSet(pl->pos, pos[0], ground_y, pos[2]);
	pl->ground = ground;
	pl->ground_y = ground_y;
	if (wall)
	{
		short dang = ATAN2(wall->nz, wall->nx) - pl->ang[1];
		if (DEG( 60) <= dang && dang <= DEG( 120)) return WALK_STAY;
		if (DEG(-60) >= dang && dang >= DEG(-120)) return WALK_STAY;
		return WALK_WALL;
	}
	return WALK_STAY;
}

int PL_ProcWalk(PLAYER *pl)
{
	int i, result;
	FVEC pos;
	for (i = 0; i < 4; i++)
	{
		pos[0] = pl->pos[0] + pl->vel[0]/4.0F * pl->ground->ny;
		pos[2] = pl->pos[2] + pl->vel[2]/4.0F * pl->ground->ny;
		pos[1] = pl->pos[1];
		result = PL_CheckWalk(pl, pos);
		if (result == WALK_FALL || result == WALK_STOP) break;
	}
	pl->surface = PL_GetSurface(pl);
	FVecCpy(pl->obj->s.pos, pl->pos);
	SVecSet(pl->obj->s.ang, 0, pl->ang[1], 0);
	if (result == WALK_WALL) result = WALK_STOP;
	return result;
}

static int PL_CheckLedge(PLAYER *pl, BGFACE *wall, FVEC oldpos, FVEC newpos)
{
	BGFACE *ground;
	FVEC pos;
	float dx, dz;
	if (pl->vel[1] > 0) return FALSE;
	dx = newpos[0] - oldpos[0];
	dz = newpos[2] - oldpos[2];
	if (dx*pl->vel[0] + dz*pl->vel[2] > 0.0F) return FALSE;
	pos[0] = newpos[0] - wall->nx*60;
	pos[2] = newpos[2] - wall->nz*60;
	pos[1] = BGCheckGround(pos[0], newpos[1]+160, pos[2], &ground);
	if (pos[1]-newpos[1] <= 100) return FALSE;
	FVecCpy(pl->pos, pos);
	pl->ground = ground;
	pl->ground_y = pos[1];
	pl->ground_ang = ATAN2(ground->nz, ground->nx);
	pl->ang[0] = 0;
	pl->ang[1] = ATAN2(wall->nz, wall->nx) + 0x8000;
	return TRUE;
}

static int PL_CheckJump(PLAYER *pl, FVEC pos, int flag)
{
	short dang;
	FVEC newpos;
	BGFACE *hwall, *lwall, *roof, *ground;
	float roof_y, ground_y, water_y;
	FVecCpy(newpos, pos);
	hwall = PL_CheckWall(newpos, 150, 50);
	lwall = PL_CheckWall(newpos, 30, 50);
	ground_y = BGCheckGround(newpos[0], newpos[1], newpos[2], &ground);
	roof_y = PL_CheckRoof(newpos, ground_y, &roof);
	water_y = BGCheckWater(newpos[0], newpos[2]);
	pl->wall = NULL;
	if (!ground)
	{
		if (newpos[1] <= pl->ground_y)
		{
			pl->pos[1] = pl->ground_y;
			return JUMP_LAND;
		}
		pl->pos[1] = newpos[1];
		return JUMP_WALL;
	}
	if (pl->state & PF_RIDE)
	{
		if (ground_y < water_y)
		{
			ground_y = water_y;
			ground = &water_ground;
			ground->nw = ground_y;
		}
	}
	if (newpos[1] <= ground_y)
	{
		if (roof_y-ground_y > 160)
		{
			pl->pos[0] = newpos[0];
			pl->pos[2] = newpos[2];
			pl->ground = ground;
			pl->ground_y = ground_y;
		}
		pl->pos[1] = ground_y;
		return JUMP_LAND;
	}
	if (newpos[1]+160 > roof_y)
	{
		if (pl->vel[1] >= 0)
		{
			pl->vel[1] = 0;
			if (flag & 2 && pl->roof && pl->roof->code == BG_5)
			{
				return JUMP_HANG;
			}
			return JUMP_STAY;
		}
		if (newpos[1] <= pl->ground_y)
		{
			pl->pos[1] = pl->ground_y;
			return JUMP_LAND;
		}
		pl->pos[1] = newpos[1];
		return JUMP_WALL;
	}
	if (flag & 1 && !hwall && lwall)
	{
		if (PL_CheckLedge(pl, lwall, pos, newpos)) return JUMP_LEDGE;
		FVecCpy(pl->pos, newpos);
		pl->ground = ground;
		pl->ground_y = ground_y;
		return JUMP_STAY;
	}
	FVecCpy(pl->pos, newpos);
	pl->ground = ground;
	pl->ground_y = ground_y;
	if (hwall || lwall)
	{
		pl->wall = hwall ? hwall : lwall;
		dang = ATAN2(pl->wall->nz, pl->wall->nx) - pl->ang[1];
		if (pl->wall->code == BG_1) return JUMP_BURN;
		if (dang < -0x6000 || dang > 0x6000)
		{
			pl->flag |= PL_40000000;
			return JUMP_WALL;
		}
	}
	return JUMP_STAY;
}

static void PL_ProcSpinGravity(PLAYER *pl)
{
	float min, scale = 1;
	if (pl->rot[1] > 0x400) scale = (float)0x400 / pl->rot[1];
	min = -75*scale;
	pl->vel[1] -= 4*scale;
	if (pl->vel[1] < min) pl->vel[1] = min;
}

static int PL_IsJumpCancel(PLAYER *pl)
{
	if (!(pl->flag & PL_00000100)) return FALSE;
	if (pl->state & (PF_DEMO|PF_DMGE)) return FALSE;
	if (!(pl->status & PA_JUMPSTA) && pl->vel[1] > 20)
	{
		return (pl->state & PF_JPCN) != 0;
	}
	return FALSE;
}

static void PL_ProcGravity(PLAYER *pl)
{
	if (pl->state == PS_JUMP_24 && pl->vel[1] < 0)
	{
		PL_ProcSpinGravity(pl);
	}
	else if (pl->state == PS_JUMP_18)
	{
		pl->vel[1] -= 1;
		if (pl->vel[1] < -75) pl->vel[1] = -75;
	}
	else if (
		pl->state == PS_JUMP_08 ||
		pl->state == PS_JUMP_2A ||
		pl->state == PS_DEMO_35
	)
	{
		pl->vel[1] -= 2;
		if (pl->vel[1] < -75) pl->vel[1] = -75;
	}
	else if (pl->state == PS_JUMP_37 || pl->state == PS_DEMO_04)
	{
		pl->vel[1] -= 3.2F;
		if (pl->vel[1] < -65) pl->vel[1] = -65;
	}
	else if (pl->state == PS_JUMP_38)
	{
		pl->vel[1] -= pl->gravity;
		if (pl->vel[1] < -75) pl->vel[1] = -75;
	}
	else if (PL_IsJumpCancel(pl))
	{
		pl->vel[1] /= 4.0F;
	}
	else if (pl->state & PF_SINK)
	{
		pl->vel[1] -= 1.6F;
		if (pl->vel[1] < -16) pl->vel[1] = -16;
	}
	else if (pl->flag & PL_WINGCAP && pl->vel[1] < 0 && pl->status & PA_JUMPSTA)
	{
		pl->ctrl->wing = 1;
		pl->vel[1] -= 2;
		if (pl->vel[1] < -37.5F)
		{
			if ((pl->vel[1] += 4) > -37.5F) pl->vel[1] = -37.5F;
		}
	}
	else
	{
		pl->vel[1] -= 4;
		if (pl->vel[1] < -75) pl->vel[1] = -75;
	}
}

static void PL_ProcUpWind(PLAYER *pl)
{
	if (pl->state != PS_JUMP_29)
	{
		float vely, level = pl->pos[1] - -1500;
		if (pl->ground->code == BG_56 && -3000 < level && level < 2000)
		{
			if (level >= 0) vely = 10000 / (level+200);
			else            vely = 50;
			if (pl->vel[1] < vely)
			{
				if ((pl->vel[1] += vely/8.0F) > vely) pl->vel[1] = vely;
			}
#if REVISION < 199609
			Na_ObjSePlay(NA_SE4_10, pl->obj);
#endif
		}
	}
}

int PL_ProcJump(PLAYER *pl, int flag)
{
	FVEC pos;
	int i, code, result = 0;
	pl->wall = NULL;
	for (i = 0; i < 4; i++)
	{
		pos[0] = pl->pos[0] + pl->vel[0]/4.0F;
		pos[1] = pl->pos[1] + pl->vel[1]/4.0F;
		pos[2] = pl->pos[2] + pl->vel[2]/4.0F;
		code = PL_CheckJump(pl, pos, flag);
		if (code) result = code;
		if (
			code == JUMP_LAND || code == JUMP_LEDGE ||
			code == JUMP_HANG || code == JUMP_BURN
		) break;
	}
	if (pl->vel[1] >= 0) pl->peak = pl->pos[1];
	pl->surface = PL_GetSurface(pl);
	if (pl->state != PS_JUMP_19) PL_ProcGravity(pl);
	PL_ProcUpWind(pl);
	FVecCpy(pl->obj->s.pos, pl->pos);
	SVecSet(pl->obj->s.ang, 0, pl->ang[1], 0);
	return result;
}

void PL_SetSpeed3D(PLAYER *pl)
{
	pl->vel[0] = pl->speed * COS(pl->ang[0]) * SIN(pl->ang[1]);
	pl->vel[1] = pl->speed * SIN(pl->ang[0]);
	pl->vel[2] = pl->speed * COS(pl->ang[0]) * COS(pl->ang[1]);
}

void PL_SetSpeed2D(PLAYER *pl)
{
	pl->vel[0] = pl->slide_x = pl->speed * SIN(pl->ang[1]);
	pl->vel[1] = 0;
	pl->vel[2] = pl->slide_z = pl->speed * COS(pl->ang[1]);
}
