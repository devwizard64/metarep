#include <sm64.h>

static short plswim_8032DD30 = FALSE;
static short plswim_8033B340;
static short plswim_8033B342;
static float plswim_8033B344;
static short plswim_8032DD34 = 160;
static short plswim_8032DD38[] = {28, 12, 8, 4};

static void plswim_80270110(PLAYER *pl, u32 effect)
{
	SHORT flag = pl->pos[1] >= pl->water-130;
	if (flag)
	{
		pl->effect |= effect;
		if (flag^plswim_8032DD30) Na_ObjSePlay(NA_SE0_31, pl->obj);
	}
	plswim_8032DD30 = flag;
}

static int plswim_802701CC(PLAYER *pl)
{
	if (pl->flag & PL_METALCAP) return FALSE;
	return pl->water-80 - pl->pos[1] < 400;
}

static float plswim_80270234(PLAYER *pl)
{
	float vely = 0;
	if (pl->flag & PL_METALCAP) vely = pl->state & PF_DMGE ? -2.0F : -18.0F;
	else if (plswim_802701CC(pl)) vely = 1.25F;
	else if (!(pl->state & PF_WALK)) vely = -2;
	return vely;
}

static int plswim_80270304(PLAYER *pl, FVEC pos)
{
	BGFACE *wall, *roof, *ground;
	float roof_y, ground_y;
	wall = PL_CheckWall(pos, 10, 110);
	ground_y = BGCheckGround(pos[0], pos[1], pos[2], &ground);
	roof_y = PL_CheckRoof(pos, ground_y, &roof);
	if (!ground) return 3;
	if (pos[1] >= ground_y)
	{
		if (roof_y-pos[1] >= 160)
		{
			FVecCpy(pl->pos, pos);
			pl->ground = ground;
			pl->ground_y = ground_y;
			if (wall)   return 4;
			else        return 0;
		}
		if (roof_y-ground_y < 160) return 3;
		FVecSet(pl->pos, pos[0], roof_y-160, pos[2]);
		pl->ground = ground;
		pl->ground_y = ground_y;
		return 2;
	}
	else
	{
		if (roof_y-ground_y < 160) return 3;
		FVecSet(pl->pos, pos[0], ground_y, pos[2]);
		pl->ground = ground;
		pl->ground_y = ground_y;
		return 1;
	}
}

static void plswim_80270500(PLAYER *pl, FVEC vel)
{
	int i;
	float radius = 2000;
	if (pl->ground->code == BG_14)
	{
		short angy = pl->ground->attr << 8;
		float accel = plswim_8032DD38[pl->ground->attr >> 8];
		vel[0] += accel * SIN(angy);
		vel[2] += accel * COS(angy);
	}
	for (i = 0; i < 2; i++)
	{
		JET *jet = scenep->jet[i];
		if (jet)
		{
			float accel = 0;
			float dx = jet->pos[0] - pl->pos[0];
			float dy = jet->pos[1] - pl->pos[1];
			float dz = jet->pos[2] - pl->pos[2];
			float dh = DIST2(dx, dz);
			float d = DIST2(dh, dy);
			SHORT angx = ATAN2(dh, dy);
			SHORT angy = ATAN2(dz, dx);
			angy -= (SHORT)(1000*0x2000 / (d+1000));
			if (jet->attr >= 0)
			{
				if (stage_index == STAGE_DDD && scene_index == 2) radius = 4000;
				if (d >= 26 && d < radius) accel = jet->attr * (1-d/radius);
			}
			else
			{
				if (d < 2000) accel = jet->attr * (1-d/2000);
			}
			vel[0] += accel * COS(angx) * SIN(angy);
			vel[1] += accel * SIN(angx);
			vel[2] += accel * COS(angx) * COS(angy);
		}
	}
}

static int plswim_80270918(PLAYER *pl)
{
	UNUSED int i;
	int result;
	FVEC pos, vel;
	OBJECT *obj = pl->obj;
	FVecCpy(vel, pl->vel);
	if (pl->state & PF_SWIM) plswim_80270500(pl, vel);
	pos[0] = pl->pos[0] + vel[0];
	pos[1] = pl->pos[1] + vel[1];
	pos[2] = pl->pos[2] + vel[2];
	if (pos[1] > pl->water-80)
	{
		pos[1] = pl->water-80;
		pl->vel[1] = 0;
	}
	result = plswim_80270304(pl, pos);
	FVecCpy(obj->s.pos, pl->pos);
	SVecSet(obj->s.ang, -pl->ang[0], pl->ang[1], pl->ang[2]);
	return result;
}

static VOID plswim_80270A74(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	if (obj->s.ang[0] > 0)
	{
		obj->s.pos[1] += 60 * SIN(obj->s.ang[0]) * SIN(obj->s.ang[0]);
	}
	if (obj->s.ang[0] < 0) obj->s.ang[0] = obj->s.ang[0] * 6/10;
	if (obj->s.ang[0] > 0) obj->s.ang[0] = obj->s.ang[0] * 10/8;
}

static void plswim_80270B4C(PLAYER *pl)
{
	float vely = plswim_80270234(pl);
	pl->rot[0] = 0;
	pl->rot[1] = 0;
	pl->speed = ConvergeF(pl->speed, 0, 1, 1);
	pl->vel[1] = ConvergeF(pl->vel[1], vely, 2, 1);
	pl->ang[0] = ConvergeI(pl->ang[0], 0, 0x200, 0x200);
	pl->ang[2] = ConvergeI(pl->ang[2], 0, 0x100, 0x100);
	pl->vel[0] = pl->speed * COS(pl->ang[0]) * SIN(pl->ang[1]);
	pl->vel[2] = pl->speed * COS(pl->ang[0]) * COS(pl->ang[1]);
}

static void plswim_80270C94(PLAYER *pl, float a1)
{
	float vely = plswim_80270234(pl);
	float limit = 28;
	if (pl->state & PF_WAIT) pl->speed -= 2;
	if (pl->speed < 0) pl->speed = 0;
	if (pl->speed > limit) pl->speed = limit;
	if (pl->speed > a1) pl->speed -= 0.5F;
	pl->vel[0] = pl->speed * COS(pl->ang[0]) * SIN(pl->ang[1]);
	pl->vel[1] = pl->speed * SIN(pl->ang[0]) + vely;
	pl->vel[2] = pl->speed * COS(pl->ang[0]) * COS(pl->ang[1]);
}

static void plswim_80270E40(PLAYER *pl)
{
	SHORT rot = -(SHORT)(10*pl->cont->x);
	if (rot > 0)
	{
		if (pl->rot[1] < 0)
		{
			pl->rot[1] += 0x40;
			if (pl->rot[1] > 0x10) pl->rot[1] = 0x10;
		}
		else
		{
			pl->rot[1] = ConvergeI(pl->rot[1], rot, 0x10, 0x20);
		}
	}
	else if (rot < 0)
	{
		if (pl->rot[1] > 0)
		{
			pl->rot[1] -= 0x40;
			if (pl->rot[1] < -0x10) pl->rot[1] = -0x10;
		}
		else
		{
			pl->rot[1] = ConvergeI(pl->rot[1], rot, 0x20, 0x10);
		}
	}
	else
	{
		pl->rot[1] = ConvergeI(pl->rot[1], 0, 0x40, 0x40);
	}
	pl->ang[1] += pl->rot[1];
	pl->ang[2] = -pl->rot[1]*8;
}

static void plswim_80270FD8(PLAYER *pl)
{
	SHORT target = -(SHORT)(252*pl->cont->y);
	SHORT speed;
	if (pl->ang[0] < 0) speed = 0x100;
	else                speed = 0x200;
	if (pl->ang[0] < target)
	{
		if ((pl->ang[0] += speed) > target) pl->ang[0] = target;
	}
	else if (pl->ang[0] > target)
	{
		if ((pl->ang[0] -= speed) < target) pl->ang[0] = target;
	}
}

static void plswim_802710C4(PLAYER *pl, int anime, int vspeed)
{
	short *neck = pl->ctrl->neck_ang;
	plswim_80270E40(pl);
	plswim_80270FD8(pl);
	plswim_80270C94(pl, 16);
	plswim_80270918(pl);
	plswim_80270A74(pl);
	if (pl->ang[0] > 0) neck[0] = ConvergeI(neck[0], pl->ang[0]/2, 0x80, 0x200);
	else                neck[0] = ConvergeI(neck[0], 0, 0x200, 0x200);
	if (vspeed == 0)    PL_SetAnime(pl, anime);
	else                PL_SetAnimeV(pl, anime, vspeed);
	plswim_80270110(pl, PE_00000080);
}

static int PL_ExecSwim00(PLAYER *pl)
{
	int speed = 1 << 16;
	if (pl->flag & PL_METALCAP) return PL_SetState(pl, PS_SWIM_34, 1);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_SWIM_21, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_SWIM_10, 0);
	if (pl->ang[0] < -0x1000) speed = 3 << 16;
	plswim_802710C4(pl, ANIME_178, speed);
	return FALSE;
}

static int PL_ExecSwim01(PLAYER *pl)
{
	if (pl->flag & PL_METALCAP) return PL_SetState(pl, PS_SWIM_35, 0);
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_SWIM_00, 0);
	}
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_SWIM_20, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_SWIM_13, 0);
	plswim_802710C4(pl, ANIME_164, 0);
	return FALSE;
}

static int PL_ExecSwim02(PLAYER *pl)
{
	if (pl->flag & PL_METALCAP) return PL_SetState(pl, PS_SWIM_34, 1);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_SWIM_21, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_SWIM_10, 0);
	plswim_802710C4(pl, ANIME_173, 0);
	if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, PS_SWIM_00, 0);
	return FALSE;
}

static int PL_ExecSwim03(PLAYER *pl)
{
	if (pl->flag & PL_METALCAP) return PL_SetState(pl, PS_SWIM_35, 0);
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_SWIM_00, 0);
	}
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_SWIM_20, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_SWIM_13, 0);
	plswim_802710C4(pl, pl->code == 0 ? ANIME_162 : ANIME_163, 0);
	if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, PS_SWIM_01, 0);
	return FALSE;
}

static void plswim_802715EC(PLAYER *pl)
{
	plswim_8033B340 = 0;
	plswim_8033B342 = 0x800;
	plswim_8033B344 = 20 + pl->ang[0]/256.0F;
}

static void plswim_8027163C(PLAYER *pl)
{
	if (plswim_8033B342 != 0)
	{
		if (pl->pos[1] > pl->water-85 && pl->ang[0] >= 0)
		{
			if ((plswim_8033B340 += plswim_8033B342) >= 0)
			{
				pl->obj->s.pos[1] += plswim_8033B344 * SIN(plswim_8033B340);
				return;
			}
		}
	}
	plswim_8033B342 = 0;
}

static void plswim_80271704(PLAYER *pl, SHORT a1)
{
	SHORT sp2E;
	UNUSED OBJECT *obj = pl->obj;
	plswim_80270E40(pl);
	plswim_80270FD8(pl);
	plswim_80270C94(pl, (float)a1/10);
	switch (plswim_80270918(pl))
	{
	case 1:
		sp2E = -PL_GetGroundAngX(pl, -0x8000);
		if (pl->ang[0] < sp2E) pl->ang[0] = sp2E;
		break;
	case 2:
		if (pl->ang[0] > -0x3000) pl->ang[0] -= 0x100;
		break;
	case 4:
		if (pl->cont->y == 0)
		{
			if ((float)pl->ang[0] > 0)
			{
				pl->ang[0] += 0x200;
				if (pl->ang[0] > +0x3F00) pl->ang[0] = +0x3F00;
			}
			else
			{
				pl->ang[0] -= 0x200;
				if (pl->ang[0] < -0x3F00) pl->ang[0] = -0x3F00;
			}
		}
		break;
	}
	plswim_80270A74(pl);
	pl->ctrl->neck_ang[0] = ConvergeI(pl->ctrl->neck_ang[0], 0, 0x200, 0x200);
	plswim_8027163C(pl);
	plswim_80270110(pl, PE_00000400);
}

static void plswim_80271918(PLAYER *pl)
{
	SHORT frame = pl->obj->s.skel.frame;
	if (frame == 0 || frame == 12) Na_ObjSePlay(NA_SE0_34, pl->obj);
}

static int plswim_8027197C(PLAYER *pl)
{
	int posy = pl->pos[1] + 1.5F;
	if (pl->status & PA_JUMPREQ)
	{
		if (posy >= pl->water-80 && pl->ang[0] >= 0 && pl->cont->y < -60)
		{
			SVecSet(pl->rot, 0, 0, 0);
			pl->vel[1] = 62;
			if (!pl->take)  return PL_SetState(pl, PS_JUMP_09, 0);
			else            return PL_SetState(pl, PS_JUMP_23, 0);
		}
	}
	return FALSE;
}

static int PL_ExecSwim10(PLAYER *pl)
{
	if (pl->code == 0) plswim_8032DD34 = 160;
	if (pl->flag & PL_METALCAP) return PL_SetState(pl, PS_SWIM_34, 1);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_SWIM_21, 0);
	if (++pl->timer == 14) return PL_SetState(pl, PS_SWIM_12, 0);
	if (plswim_8027197C(pl)) return TRUE;
	if (pl->timer <  6) pl->speed += 0.5F;
	if (pl->timer >= 9) pl->speed += 1.5F;
	if (pl->timer > 1)
	{
		if (pl->timer < 6 && pl->status & PA_JUMPREQ) pl->phase = 1;
		if (pl->timer == 9 && pl->phase == 1)
		{
			PL_SetAnimeFrame(pl, 0);
			pl->phase = 0;
			pl->timer = 1;
			plswim_8032DD34 = 160;
		}
	}
	if (pl->timer == 1)
	{
		Na_ObjSePlay(plswim_8032DD34 == 160 ? NA_SE0_33 : NA_SE0_47, pl->obj);
		plswim_802715EC(pl);
	}
#ifdef MOTOR
	if (pl->timer < 6) motor_8024CA04();
#endif
	PL_SetAnime(pl, ANIME_170);
	plswim_80271704(pl, plswim_8032DD34);
	return FALSE;
}

static int PL_ExecSwim11(PLAYER *pl)
{
	if (pl->flag & PL_METALCAP) return PL_SetState(pl, PS_SWIM_34, 1);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_SWIM_21, 0);
	if (pl->timer >= 15) return PL_SetState(pl, PS_SWIM_02, 0);
	if (plswim_8027197C(pl)) return TRUE;
	if (pl->status & PA_JUMPSTA && pl->timer >= 7)
	{
		if (pl->timer == 7 && plswim_8032DD34 < 280) plswim_8032DD34 += 10;
		return PL_SetState(pl, PS_SWIM_10, 1);
	}
	if (pl->timer >= 7) plswim_8032DD34 = 160;
	pl->timer++;
	pl->speed -= 0.25F;
	PL_SetAnime(pl, ANIME_171);
	plswim_80271704(pl, plswim_8032DD34);
	return FALSE;
}

static int PL_ExecSwim12(PLAYER *pl)
{
	if (pl->flag & PL_METALCAP) return PL_SetState(pl, PS_SWIM_34, 1);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_SWIM_21, 0);
	if (!(pl->status & PA_JUMPSTA))
	{
		if (pl->timer == 0 && plswim_8032DD34 < 280) plswim_8032DD34 += 10;
		return PL_SetState(pl, PS_SWIM_11, 0);
	}
	pl->speed = ConvergeF(pl->speed, 12, 0.1F, 0.15F);
	pl->timer = 1;
	plswim_8032DD34 = 160;
	if (pl->speed < 14)
	{
		plswim_80271918(pl);
		PL_SetAnime(pl, ANIME_172);
	}
	plswim_80271704(pl, plswim_8032DD34);
	return FALSE;
}

static int PL_ExecSwim13(PLAYER *pl)
{
	if (pl->flag & PL_METALCAP) return PL_SetState(pl, PS_SWIM_35, 0);
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_SWIM_00, 0);
	}
	if (++pl->timer == 17) return PL_SetState(pl, PS_SWIM_15, 0);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_SWIM_20, 0);
	if (plswim_8027197C(pl)) return TRUE;
	if (pl->timer <  6) pl->speed += 0.5F;
	if (pl->timer >= 9) pl->speed += 1.5F;
	if (pl->timer > 1)
	{
		if (pl->timer < 6 && pl->status & PA_JUMPREQ) pl->phase = 1;
		if (pl->timer == 9 && pl->phase == 1)
		{
			PL_SetAnimeFrame(pl, 0);
			pl->phase = 0;
			pl->timer = 1;
		}
	}
	if (pl->timer == 1)
	{
		Na_ObjSePlay(NA_SE0_33, pl->obj);
		plswim_802715EC(pl);
	}
	PL_SetAnime(pl, ANIME_159);
	plswim_80271704(pl, 160);
	return FALSE;
}

static int PL_ExecSwim14(PLAYER *pl)
{
	if (pl->flag & PL_METALCAP) return PL_SetState(pl, PS_SWIM_35, 0);
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_SWIM_00, 0);
	}
	if (pl->timer >= 15) return PL_SetState(pl, PS_SWIM_03, 0);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_SWIM_20, 0);
	if (plswim_8027197C(pl)) return TRUE;
	if (pl->status & PA_JUMPSTA && pl->timer >= 7)
	{
		return PL_SetState(pl, PS_SWIM_13, 0);
	}
	pl->timer++;
	pl->speed -= 0.25F;
	PL_SetAnime(pl, ANIME_160);
	plswim_80271704(pl, 160);
	return FALSE;
}

static int PL_ExecSwim15(PLAYER *pl)
{
	if (pl->flag & PL_METALCAP) return PL_SetState(pl, PS_SWIM_35, 0);
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_SWIM_00, 0);
	}
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_SWIM_20, 0);
	if (!(pl->status & PA_JUMPSTA)) return PL_SetState(pl, PS_SWIM_14, 0);
	pl->speed = ConvergeF(pl->speed, 12, 0.1F, 0.15F);
	if (pl->speed < 14)
	{
		plswim_80271918(pl);
		PL_SetAnime(pl, ANIME_161);
	}
	plswim_80271704(pl, 160);
	return FALSE;
}

static int PL_ExecSwim16(PLAYER *pl)
{
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_SWIM_00, 0);
	}
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_SWIM_20, 0);
	if (pl->timer++ == 240)
	{
		pl->take->o_hit_result = HR_400000;
		pl->take = NULL;
		AudStopShellBGM();
		PL_SetState(pl, PS_SWIM_12, 0);
	}
	pl->speed = ConvergeF(pl->speed, 30, 2, 1);
	plswim_80271918(pl);
	PL_SetAnime(pl, ANIME_161);
	plswim_80271704(pl, 300);
	return FALSE;
}

static int plswim_8027267C(PLAYER *pl)
{
	if (pl->obj->hit_status & HIT_TAKE)
	{
		OBJECT *obj = PL_GetHitObj(pl, HIT_TAKE);
		float dx = obj->o_posx - pl->pos[0];
		float dz = obj->o_posz - pl->pos[2];
		short dang = (SHORT)ATAN2(dz, dx) - pl->ang[1];
		if (DEG(-60) <= dang && dang <= DEG(60))
		{
			pl->attach = obj;
			PL_TakeObject(pl);
			pl->ctrl->take = 1;
			return 1;
		}
	}
	return 0;
}

static int PL_ExecSwim20(PLAYER *pl)
{
	plswim_80270E40(pl);
	plswim_80270FD8(pl);
	plswim_80270C94(pl, 16);
	plswim_80270918(pl);
	plswim_80270A74(pl);
	PL_SetAnime(pl, ANIME_177);
	PL_TrigSound(pl, NA_SE0_33, PL_SOUND);
	pl->ctrl->neck_ang[0] = ConvergeI(pl->ctrl->neck_ang[0], 0, 0x200, 0x200);
	if (pl->timer++ == 5)
	{
		PL_ThrowObject(pl);
#ifdef MOTOR
		motor_8024C834(3, 50);
#endif
	}
	if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, PS_SWIM_00, 0);
	return FALSE;
}

extern OBJLANG obj_13000708[];

static int PL_ExecSwim21(PLAYER *pl)
{
	if (pl->speed < 7) pl->speed += 1;
	plswim_80270E40(pl);
	plswim_80270FD8(pl);
	plswim_80270C94(pl, 16);
	plswim_80270918(pl);
	plswim_80270A74(pl);
	pl->ctrl->neck_ang[0] = ConvergeI(pl->ctrl->neck_ang[0], 0, 0x200, 0x200);
	PL_TrigSound(pl, NA_SE0_33, PL_SOUND);
	switch (pl->phase)
	{
	case 0:
		PL_SetAnime(pl, ANIME_176);
		if (PL_IsAnimeLast1F(pl)) pl->phase = 1 + plswim_8027267C(pl);
		break;
	case 1:
		PL_SetAnime(pl, ANIME_175);
		if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, PS_SWIM_02, 0);
		break;
	case 2:
		PL_SetAnime(pl, ANIME_174);
		if (PL_IsAnimeLast1F(pl))
		{
			if (pl->take->script == SegmentToVirtual(obj_13000708))
			{
				AudPlayShellBGM();
				PL_SetState(pl, PS_SWIM_16, 0);
			}
			else
			{
				PL_SetState(pl, PS_SWIM_03, 1);
			}
		}
		break;
	}
	return FALSE;
}

static void plswim_80272A60(PLAYER *pl, int anime, u32 state, int code)
{
	plswim_80270B4C(pl);
	plswim_80270918(pl);
	PL_SetAnime(pl, anime);
	pl->ctrl->neck_ang[0] = 0;
	if (PL_IsAnimeLast1F(pl))
	{
		if (code > 0) pl->invincible = 30;
		PL_SetState(pl, pl->power >= 0x100 ? state : PS_SWIM_07, 0);
	}
}

static int PL_ExecSwim05(PLAYER *pl)
{
	plswim_80272A60(pl, ANIME_158, PS_SWIM_00, pl->code);
	return FALSE;
}

static int PL_ExecSwim06(PLAYER *pl)
{
	plswim_80272A60(pl, ANIME_168, PS_SWIM_00, pl->code);
	return FALSE;
}

static int PL_ExecSwim08(PLAYER *pl)
{
	PL_TrigSound(pl, NA_SE2_10, PL_SOUND);
	Na_ObjSePlay(NA_SE1_16, pl->obj);
	camera_8027F590(10);
	if (PL_SetAnime(pl, ANIME_122) == 0)
	{
		pl->timer++;
		pl->flag |= 0x0040;
	}
	if (pl->timer >= 6)
	{
		pl->invincible = 30;
		PL_SetState(pl, pl->power < 0x100 ? PS_SWIM_07 : PS_SWIM_00, 0);
	}
	plswim_80270B4C(pl);
	plswim_80270918(pl);
	pl->ctrl->neck_ang[0] = 0;
	return FALSE;
}

static int PL_ExecSwim04(PLAYER *pl)
{
	switch (pl->phase)
	{
	case 0:
		PL_SetAnime(pl, ANIME_165);
		pl->ctrl->eyes = 2;
		if (PL_IsAnimeLast1F(pl)) pl->phase = 1;
		break;
	case 1:
		PL_SetAnime(pl, ANIME_166);
		pl->ctrl->eyes = 8;
		if (pl->obj->s.skel.frame == 30) PL_Fade(pl, FADE_DIE);
		break;
	}
	PL_TrigSound(pl, NA_SE2_23, PL_SOUND);
	plswim_80270B4C(pl);
	plswim_80270918(pl);
	return FALSE;
}

static int PL_ExecSwim07(PLAYER *pl)
{
	plswim_80270B4C(pl);
	plswim_80270918(pl);
	pl->ctrl->eyes = 8;
	PL_SetAnime(pl, ANIME_167);
	if (PL_SetAnime(pl, ANIME_167) == 35) PL_Fade(pl, FADE_DIE);
	return FALSE;
}

static int PL_ExecSwim22(PLAYER *pl)
{
	int sp24, sp20 = pl->take != NULL;
	float sp1C = plswim_802701CC(pl) ? 0.0F : -5.0F;
	if (pl->flag & PL_METALCAP) sp20 |= 4;
	else if (pl->prevstate & PF_DIVE || pl->status & PA_JUMPSTA) sp20 |= 2;
	pl->timer++;
	plswim_80270B4C(pl);
	sp24 = plswim_80270918(pl);
	if (pl->phase == 0)
	{
		Na_ObjSePlay(NA_SE0_30, pl->obj);
		if (pl->peak-pl->pos[1] > 1150) Na_ObjSePlay(NA_SE2_11_F0, pl->obj);
		pl->effect |= PE_00000040;
		pl->phase = 1;
#ifdef MOTOR
		if (pl->prevstate & PF_JUMP) motor_8024C834(5, 80);
#endif
	}
	if (sp24 == 1 || pl->vel[1] >= sp1C || pl->timer > 20)
	{
		switch (sp20)
		{
		case 0|0: PL_SetState(pl, PS_SWIM_02, 0); break;
		case 0|1: PL_SetState(pl, PS_SWIM_03, 0); break;
		case 2|0: PL_SetState(pl, PS_SWIM_12, 0); break;
		case 2|1: PL_SetState(pl, PS_SWIM_15, 0); break;
		case 4|0: PL_SetState(pl, PS_SWIM_34, 0); break;
		case 4|1: PL_SetState(pl, PS_SWIM_35, 0); break;
		}
		plswim_8033B342 = 0;
	}
	switch (sp20)
	{
	case 0|0: PL_SetAnime(pl, ANIME_173); break;
	case 0|1: PL_SetAnime(pl, ANIME_162); break;
	case 2|0: PL_SetAnime(pl, ANIME_172); break;
	case 2|1: PL_SetAnime(pl, ANIME_161); break;
	case 4|0: PL_SetAnime(pl, ANIME_86); break;
	case 4|1: PL_SetAnime(pl, ANIME_67); break;
	}
	pl->effect |= PE_00000200;
	return FALSE;
}

static int PL_ExecSwim23(PLAYER *pl)
{
	float s, c, dist;
	SHORT angy;
	OBJECT *obj = pl->obj;
	OBJECT *attach = pl->attach;
	float dx = pl->pos[0] - attach->o_posx;
	float dz = pl->pos[2] - attach->o_posz;
	float d = DIST2(dx, dz);
	if ((obj->o_f7 += pl->vel[1]) < 0)
	{
		obj->o_f7 = 0;
		if (d < 16.1F && pl->timer++ == 16) PL_Fade(pl, FADE_DIE);
	}
	if (d <= 28)
	{
		dist = 16;
		angy = 0x1800;
	}
	else if (d < 256.0F)
	{
		dist = d - (12 - d/32.0F);
		angy = 0x1C00 - d*20;
	}
	else
	{
		dist = d-4;
		angy = 0x800;
	}
	pl->vel[1] = -640 / (dist+16);
	s = SIN(angy);
	c = COS(angy);
	if (d < 1)
	{
		dx = dist * SIN(pl->ang[1]);
		dz = dist * COS(pl->ang[1]);
	}
	else
	{
		dx *= dist / d;
		dz *= dist / d;
	}
	pl->pos[0] = attach->o_posx + dx*c + dz*s;
	pl->pos[2] = attach->o_posz - dx*s + dz*c;
	pl->pos[1] = attach->o_posy + obj->o_f7;
	pl->ang[1] = ATAN2(dz, dx) + 0x8000;
	PL_SetAnime(pl, ANIME_86);
	FVecCpy(pl->obj->s.pos, pl->pos);
	SVecSet(pl->obj->s.ang, 0, pl->ang[1], 0);
#ifdef MOTOR
	motor_8024C924();
#endif
	return FALSE;
}

static void plswim_80273518(PLAYER *pl, int a1)
{
	if (!(pl->flag & PL_SOUND)) pl->effect |= PE_00010000;
	PL_TrigSound(pl, a1 ? NA_SE0_51 : NA_SE0_50, PL_SOUND);
}

static void plswim_802735A4(PLAYER *pl)
{
	if (PL_IsAnimeAtFrame(pl, 10) || PL_IsAnimeAtFrame(pl, 49))
	{
		Na_ObjSePlay(NA_SE0_52, pl->obj);
		pl->effect |= PE_00000001;
	}
}

static void plswim_80273618(PLAYER *pl)
{
	float speed = pl->stick_dist / 1.5F;
	if      (pl->speed <=     0) pl->speed += 1.1F;
	else if (pl->speed <= speed) pl->speed += 1.1F - pl->speed/43;
	else if (pl->ground->ny >= 0.95F) pl->speed -= 1;
	if (pl->speed > 32) pl->speed = 32;
	pl->ang[1] = TURN(pl->ang[1], pl->stick_ang, 0x800);
	pl->slide_x = pl->speed * SIN(pl->ang[1]);
	pl->slide_z = pl->speed * COS(pl->ang[1]);
	pl->vel[0] = pl->slide_x;
	pl->vel[1] = 0;
	pl->vel[2] = pl->slide_z;
}

static int plswim_802737F4(PLAYER *pl)
{
	UNUSED float posy = pl->pos[1] + pl->vel[1];
	float water = pl->water - 100;
	if (pl->vel[1] > 0 && pl->pos[1] > water) return TRUE;
	if (pl->status & PA_WALKREQ)
	{
		SHORT dang = pl->stick_ang - pl->ang[1];
		pl->speed += 0.8F * COS(dang);
		pl->ang[1] += 512 * SIN(dang);
	}
	else
	{
		pl->speed = ConvergeF(pl->speed, 0, 0.25F, 0.25F);
	}
	if (pl->speed > 16) pl->speed -= 1;
	if (pl->speed <  0) pl->speed += 2;
	pl->vel[0] = pl->slide_x = pl->speed * SIN(pl->ang[1]);
	pl->vel[2] = pl->slide_z = pl->speed * COS(pl->ang[1]);
	return FALSE;
}

static int PL_ExecSwim30(PLAYER *pl)
{
	if (!(pl->flag & PL_METALCAP)) return PL_SetState(pl, PS_SWIM_00, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_SWIM_38, 0);
	if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_SWIM_32, 0);
	switch (pl->phase)
	{
	case 0: PL_SetAnime(pl, ANIME_195); break;
	case 1: PL_SetAnime(pl, ANIME_196); break;
	case 2: PL_SetAnime(pl, ANIME_197); break;
	}
	if (PL_IsAnimeLast1F(pl) && ++pl->phase == 3) pl->phase = 0;
	PL_Stop(pl);
	if (pl->pos[1] >= pl->water-150) pl->effect |= PE_00000080;
	return FALSE;
}

static int PL_ExecSwim31(PLAYER *pl)
{
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_SWIM_30, 0);
	}
	if (!(pl->flag & PL_METALCAP)) return PL_SetState(pl, PS_SWIM_01, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_SWIM_39, 0);
	if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_SWIM_33, 0);
	PL_Stop(pl);
	PL_SetAnime(pl, ANIME_63);
	return FALSE;
}

static int PL_ExecSwim32(PLAYER *pl)
{
	int vspeed;
	if (!(pl->flag & PL_METALCAP)) return PL_SetState(pl, PS_SWIM_00, 0);
	if (pl->status & PA_VIEWREQ) return PL_SetState(pl, PS_SWIM_30, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_SWIM_38, 0);
	if (pl->status & PA_WAITREQ) return PL_SetState(pl, PS_SWIM_30, 0);
	if ((vspeed = VSPEED(pl->speed/4.0F)) < VSPEED(1/16.0F))
	{
		vspeed = VSPEED(1/16.0F);
	}
	PL_SetAnimeV(pl, ANIME_72, vspeed);
	plswim_802735A4(pl);
	plswim_80273618(pl);
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, PS_SWIM_34, 1);
		break;
	case WALK_STOP:
		pl->speed = 0;
		break;
	}
	return FALSE;
}

static int PL_ExecSwim33(PLAYER *pl)
{
	int vspeed;
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_SWIM_32, 0);
	}
	if (!(pl->flag & PL_METALCAP)) return PL_SetState(pl, PS_SWIM_01, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_SWIM_39, 0);
	if (pl->status & PA_WAITREQ) return PL_SetState(pl, PS_SWIM_31, 0);
	pl->stick_dist *= 0.4F;
	if ((vspeed = VSPEED(pl->speed/2.0F)) < VSPEED(1/16.0F))
	{
		vspeed = VSPEED(1/16.0F);
	}
	PL_SetAnimeV(pl, ANIME_23, vspeed);
	plswim_802735A4(pl);
	plswim_80273618(pl);
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, PS_SWIM_35, 1);
		break;
	case WALK_STOP:
		pl->speed = 0;
		break;
	}
	return FALSE;
}

static int PL_ExecSwim38(PLAYER *pl)
{
	if (!(pl->flag & PL_METALCAP)) return PL_SetState(pl, PS_SWIM_00, 0);
	if (plswim_802737F4(pl)) return PL_SetState(pl, PS_JUMP_09, 1);
	plswim_80273518(pl, FALSE);
	PL_SetAnime(pl, ANIME_77);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		PL_SetState(pl, PS_SWIM_3A, 0);
		break;
	case JUMP_WALL:
		pl->speed = 0;
		break;
	}
	return FALSE;
}

static int PL_ExecSwim39(PLAYER *pl)
{
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_SWIM_34, 0);
	}
	if (!(pl->flag & PL_METALCAP)) return PL_SetState(pl, PS_SWIM_01, 0);
	if (plswim_802737F4(pl)) return PL_SetState(pl, PS_JUMP_23, 1);
	plswim_80273518(pl, FALSE);
	PL_SetAnime(pl, ANIME_65);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		PL_SetState(pl, PS_SWIM_3B, 0);
		break;
	case JUMP_WALL:
		pl->speed = 0;
		break;
	}
	return FALSE;
}

static int PL_ExecSwim34(PLAYER *pl)
{
	if (!(pl->flag & PL_METALCAP)) return PL_SetState(pl, PS_SWIM_00, 0);
	if (pl->status & PA_WALKREQ)
	{
		pl->ang[1] += 0x400 * SIN(pl->stick_ang-pl->ang[1]);
	}
	PL_SetAnime(pl, pl->code == 0 ? ANIME_86 : ANIME_169);
	plswim_80270B4C(pl);
	if (plswim_80270918(pl) & 1) PL_SetState(pl, PS_SWIM_36, 0);
	return FALSE;
}

static int PL_ExecSwim35(PLAYER *pl)
{
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_SWIM_34, 0);
	}
	if (!(pl->flag & PL_METALCAP)) return PL_SetState(pl, PS_SWIM_01, 0);
	if (pl->status & PA_WALKREQ)
	{
		pl->ang[1] += 0x400 * SIN(pl->stick_ang-pl->ang[1]);
	}
	PL_SetAnime(pl, ANIME_67);
	plswim_80270B4C(pl);
	if (plswim_80270918(pl) & 1) PL_SetState(pl, PS_SWIM_37, 0);
	return FALSE;
}

static int PL_ExecSwim3A(PLAYER *pl)
{
	plswim_80273518(pl, TRUE);
	if (!(pl->flag & PL_METALCAP)) return PL_SetState(pl, PS_SWIM_00, 0);
	if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_SWIM_32, 0);
	PL_Stop(pl);
	PL_SetAnime(pl, ANIME_78);
	if (PL_IsAnimeLast1F(pl)) return PL_SetState(pl, PS_SWIM_30, 0);
	return FALSE;
}

static int PL_ExecSwim3B(PLAYER *pl)
{
	plswim_80273518(pl, TRUE);
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_SWIM_30, 0);
	}
	if (!(pl->flag & PL_METALCAP)) return PL_SetState(pl, PS_SWIM_01, 0);
	if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_SWIM_33, 0);
	PL_Stop(pl);
	PL_SetAnime(pl, ANIME_64);
	if (PL_IsAnimeLast1F(pl)) return PL_SetState(pl, PS_SWIM_31, 0);
	return FALSE;
}

static int PL_ExecSwim36(PLAYER *pl)
{
	plswim_80273518(pl, TRUE);
	if (!(pl->flag & PL_METALCAP)) return PL_SetState(pl, PS_SWIM_00, 0);
	if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_SWIM_32, 0);
	PL_Stop(pl);
	PL_SetAnime(pl, ANIME_87);
	if (PL_IsAnimeLast1F(pl)) return PL_SetState(pl, PS_SWIM_30, 0);
	return FALSE;
}

static int PL_ExecSwim37(PLAYER *pl)
{
	plswim_80273518(pl, TRUE);
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_SWIM_30, 0);
	}
	if (!(pl->flag & PL_METALCAP)) return PL_SetState(pl, PS_SWIM_01, 0);
	if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_SWIM_33, 0);
	PL_Stop(pl);
	PL_SetAnime(pl, ANIME_66);
	if (PL_IsAnimeLast1F(pl)) return PL_SetState(pl, PS_SWIM_31, 0);
	return FALSE;
}

static int plswim_80274864(PLAYER *pl)
{
	if (pl->pos[1] > pl->water-80)
	{
		if (pl->water-80 > pl->ground_y)
		{
			pl->pos[1] = pl->water-80;
		}
		else
		{
			if (pl->state == PS_SWIM_16 && pl->take)
			{
				pl->take->o_hit_result = HR_400000;
				pl->take = NULL;
				AudStopShellBGM();
			}
			return PL_EnterField(pl);
		}
	}
	if (pl->power < 0x100 && !(pl->state & (PF_DEMO|PF_DMGE)))
	{
		PL_SetState(pl, PS_SWIM_04, 0);
	}
	return FALSE;
}

int PL_ExecSwim(PLAYER *pl)
{
	int result;
	if (plswim_80274864(pl)) return TRUE;
	pl->sink = 0;
	pl->ctrl->neck_ang[1] = 0;
	pl->ctrl->neck_ang[2] = 0;
	switch (pl->state)
	{
	case PS_SWIM_00: result = PL_ExecSwim00(pl); break;
	case PS_SWIM_01: result = PL_ExecSwim01(pl); break;
	case PS_SWIM_02: result = PL_ExecSwim02(pl); break;
	case PS_SWIM_03: result = PL_ExecSwim03(pl); break;
	case PS_SWIM_04: result = PL_ExecSwim04(pl); break;
	case PS_SWIM_05: result = PL_ExecSwim05(pl); break;
	case PS_SWIM_06: result = PL_ExecSwim06(pl); break;
	case PS_SWIM_07: result = PL_ExecSwim07(pl); break;
	case PS_SWIM_08: result = PL_ExecSwim08(pl); break;
	case PS_SWIM_10: result = PL_ExecSwim10(pl); break;
	case PS_SWIM_11: result = PL_ExecSwim11(pl); break;
	case PS_SWIM_12: result = PL_ExecSwim12(pl); break;
	case PS_SWIM_13: result = PL_ExecSwim13(pl); break;
	case PS_SWIM_14: result = PL_ExecSwim14(pl); break;
	case PS_SWIM_15: result = PL_ExecSwim15(pl); break;
	case PS_SWIM_16: result = PL_ExecSwim16(pl); break;
	case PS_SWIM_20: result = PL_ExecSwim20(pl); break;
	case PS_SWIM_21: result = PL_ExecSwim21(pl); break;
	case PS_SWIM_22: result = PL_ExecSwim22(pl); break;
	case PS_SWIM_23: result = PL_ExecSwim23(pl); break;
	case PS_SWIM_30: result = PL_ExecSwim30(pl); break;
	case PS_SWIM_32: result = PL_ExecSwim32(pl); break;
	case PS_SWIM_34: result = PL_ExecSwim34(pl); break;
	case PS_SWIM_36: result = PL_ExecSwim36(pl); break;
	case PS_SWIM_38: result = PL_ExecSwim38(pl); break;
	case PS_SWIM_3A: result = PL_ExecSwim3A(pl); break;
	case PS_SWIM_31: result = PL_ExecSwim31(pl); break;
	case PS_SWIM_33: result = PL_ExecSwim33(pl); break;
	case PS_SWIM_35: result = PL_ExecSwim35(pl); break;
	case PS_SWIM_37: result = PL_ExecSwim37(pl); break;
	case PS_SWIM_39: result = PL_ExecSwim39(pl); break;
	case PS_SWIM_3B: result = PL_ExecSwim3B(pl); break;
	}
	return result;
}
