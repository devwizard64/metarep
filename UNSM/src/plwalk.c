#include <sm64.h>

static short plwalk_80263E60(PLAYER *pl)
{
	SHORT angx = PL_GetGroundAngX(pl, 0);
	angx = angx * pl->speed/40;
	return -angx;
}

void plwalk_80263EE4(PLAYER *pl, SHORT lframe, SHORT rframe)
{
	if (PL_IsAnimeAtFrame(pl, lframe) || PL_IsAnimeAtFrame(pl, rframe))
	{
		if (pl->flag & PL_METALCAP)
		{
			if (pl->obj->s.skel.index == ANIME_146)
			{
				PL_PlayEffect(pl, NA_SE0_2F, 0);
			}
			else
			{
				PL_PlayEffect(pl, NA_SE0_2A, 0);
			}
		}
		else if (pl->sink > 50)
		{
			Na_ObjSePlay(NA_SE0_2E, pl->obj);
		}
		else
		{
			if (pl->obj->s.skel.index == ANIME_146)
			{
				PL_PlayEffect(pl, NA_SE0_20, 0);
			}
			else
			{
				PL_PlayEffect(pl, NA_SE0_10, 0);
			}
		}
	}
}

static void plwalk_80264024(PLAYER *pl)
{
	static FMTX plwalk_8033B2C0[2];
	pl->pos[1] = pl->ground_y;
	FMtxGround(plwalk_8033B2C0[pl->index], pl->pos, pl->ang[1], 40);
	pl->obj->s.m = &plwalk_8033B2C0[pl->index];
}

static int plwalk_8026409C(PLAYER *pl, float speed, u32 state, u32 code)
{
	pl->ang[1] = pl->stick_ang;
	PL_SetSpeed(pl, speed);
	return PL_SetState(pl, state, code);
}

static void plwalk_802640FC(PLAYER *pl)
{
	if (pl->speed < 10)
	{
		WALLCHECK check;
		check.x = pl->pos[0];
		check.y = pl->pos[1];
		check.z = pl->pos[2];
		check.radius = 10;
		check.offset = -10;
		if (BGCheckWall(&check))
		{
			BGFACE *ground;
			float ground_y = BGCheckGround(check.x, check.y, check.z, &ground);
			if (ground && check.y-ground_y > 160)
			{
				BGFACE *wall = check.wall[check.count-1];
				SHORT wall_ang = ATAN2(wall->nz, wall->nx);
				short dang = wall_ang - pl->ang[1];
				if (-0x4000 < dang && dang < 0x4000)
				{
					pl->pos[0] = check.x - 20*wall->nx;
					pl->pos[2] = check.z - 20*wall->nz;
					pl->ang[0] = 0;
					pl->ang[1] = wall_ang + 0x8000;
					PL_SetState(pl, PS_SPEC_0E, 0);
					PL_SetAnime(pl, ANIME_28);
				}
			}
		}
	}
}

static void plwalk_802642B4(PLAYER *pl, u32 state1, u32 state2)
{
	if (pl->speed > 16)
	{
		PL_Reflect(pl, TRUE);
		PL_SetStateDrop(pl, state1, 0);
	}
	else
	{
		PL_SetSpeed(pl, 0);
		PL_SetState(pl, state2, 0);
	}
}

static int plwalk_80264340(PLAYER *pl, UNUSED u32 state, UNUSED u32 code)
{
	if (pl->flag & PL_WINGCAP)  return PL_SetState(pl, PS_JUMP_14, 0);
	else if (pl->speed > 20)    return PL_SetState(pl, PS_JUMP_02, 0);
	else                        return PL_SetState(pl, PS_JUMP_00, 0);
	return FALSE;
}

static void plwalk_8026440C(PLAYER *pl, float a1, float a2)
{
	int ang;
	short dang;
	BGFACE *ground = pl->ground;
	SHORT ground_ang = ATAN2(ground->nz, ground->nx);
	float slope = DIST2(ground->nx, ground->nz);
	UNUSED float ny = ground->ny;
	pl->slide_x += a1 * slope * SIN(ground_ang);
	pl->slide_z += a1 * slope * COS(ground_ang);
	pl->slide_x *= a2;
	pl->slide_z *= a2;
	pl->slide_ang = ATAN2(pl->slide_z, pl->slide_x);
	dang = pl->ang[1] - pl->slide_ang;
	ang = dang;
	if (ang > 0x0000 && ang <= 0x4000)
	{
		if ((ang -= 0x200) < 0x0000) ang = 0x0000;
	}
	else if (ang > -0x4000 && ang < 0x0000)
	{
		if ((ang += 0x200) > 0x0000) ang = 0x0000;
	}
	else if (ang > 0x4000 && ang < 0x8000)
	{
		if ((ang += 0x200) > 0x8000) ang = 0x8000;
	}
	else if (ang > -0x8000 && ang < -0x4000)
	{
		if ((ang -= 0x200) < -0x8000) ang = -0x8000;
	}
	pl->ang[1] = pl->slide_ang + ang;
	pl->vel[0] = pl->slide_x;
	pl->vel[1] = 0;
	pl->vel[2] = pl->slide_z;
	PL_ProcQuicksand(pl);
	PL_ProcWind(pl);
	pl->speed = DIST2(pl->slide_x, pl->slide_z);
	if (pl->speed > 100)
	{
		pl->slide_x = pl->slide_x * 100/pl->speed;
		pl->slide_z = pl->slide_z * 100/pl->speed;
	}
	if (ang < -0x4000 || 0x4000 < ang) pl->speed *= -1;
}

static int plwalk_80264740(PLAYER *pl, float a1)
{
	float sp44, sp40, sp3C, sp38;
	int result = FALSE;
	SHORT sp32 = pl->stick_ang - pl->slide_ang;
	float sp2C = COS(sp32);
	float sp28 = SIN(sp32);
	if (sp2C < 0 && pl->speed >= 0) sp2C *= 0.5F + 0.5F*pl->speed/100;
	switch (PL_GetSlip(pl))
	{
	case 19: sp40 = 10; sp44 = (pl->stick_dist/32.0F)*sp2C*0.02F + 0.98F; break;
	case 20: sp40 =  8; sp44 = (pl->stick_dist/32.0F)*sp2C*0.02F + 0.96F; break;
	default: sp40 =  7; sp44 = (pl->stick_dist/32.0F)*sp2C*0.02F + 0.92F; break;
	case 21: sp40 =  5; sp44 = (pl->stick_dist/32.0F)*sp2C*0.02F + 0.92F; break;
	}
	sp3C = DIST2(pl->slide_x, pl->slide_z);
	pl->slide_x += pl->slide_z * (pl->stick_dist/32.0F)*sp28*0.05F;
	pl->slide_z -= pl->slide_x * (pl->stick_dist/32.0F)*sp28*0.05F;
	sp38 = DIST2(pl->slide_x, pl->slide_z);
	if (sp3C > 0 && sp38 > 0)
	{
		pl->slide_x = pl->slide_x * sp3C/sp38;
		pl->slide_z = pl->slide_z * sp3C/sp38;
	}
	plwalk_8026440C(pl, sp40, sp44);
	if (!PL_IsSlipMax(pl) && SQUARE(pl->speed) < SQUARE(a1))
	{
		PL_SetSpeed(pl, 0);
		result = TRUE;
	}
	return result;
}

static void plwalk_80264B54(PLAYER *pl)
{
	float accel;
	BGFACE *ground = pl->ground;
	float slope = DIST2(ground->nx, ground->nz);
	UNUSED float ny = ground->ny;
	short dang = pl->ground_ang - pl->ang[1];
	if (PL_IsSlipMax(pl))
	{
		SHORT slip = 0;
		if (pl->state != PS_WALK_24 && pl->state != PS_WALK_25)
		{
			slip = PL_GetSlip(pl);
		}
		switch (slip)
		{
		case 19: accel = 5.3F; break;
		case 20: accel = 2.7F; break;
		default: accel = 1.7F; break;
		case 21: accel = 0; break;
		}
		if (-0x4000 < dang && dang < 0x4000)    pl->speed += accel*slope;
		else                                    pl->speed -= accel*slope;
	}
	pl->slide_ang = pl->ang[1];
	pl->slide_x = pl->speed * SIN(pl->ang[1]);
	pl->slide_z = pl->speed * COS(pl->ang[1]);
	pl->vel[0] = pl->slide_x;
	pl->vel[1] = 0;
	pl->vel[2] = pl->slide_z;
	PL_ProcQuicksand(pl);
	PL_ProcWind(pl);
}

static int plwalk_80264D80(PLAYER *pl, float a1)
{
	int result = FALSE;
	plwalk_80264B54(pl);
	if (!PL_IsSlipMax(pl))
	{
		pl->speed *= a1;
		if (SQUARE(pl->speed) < 1)
		{
			PL_SetSpeed(pl, 0);
			result = TRUE;
		}
	}
	return result;
}

static void plwalk_80264E18(PLAYER *pl)
{
	float sp1C, sp18;
	if (pl->ground_y < pl->water)
	{
		pl->ground_y = pl->water;
		pl->ground = &water_ground;
		pl->ground->nw = pl->water;
	}
	sp1C = pl->ground && pl->ground->code == BG_9 ? 48.0F : 64.0F;
	sp18 = 2.0F * pl->stick_dist;
	if (sp18 > sp1C) sp18 = sp1C;
	if (sp18 < 24) sp18 = 24;
	if      (pl->speed <= 0)            pl->speed += 1.1F;
	else if (pl->speed <= sp18)         pl->speed += 1.1F - pl->speed/58;
	else if (pl->ground->ny >= 0.95F)   pl->speed -= 1;
	if (pl->speed > 64.0F) pl->speed = 64.0F;
	pl->ang[1] = TURN(pl->ang[1], pl->stick_ang, 0x800);
	plwalk_80264B54(pl);
}

static int plwalk_80265080(PLAYER *pl, float a1)
{
	float sp34;
	int result = FALSE;
	switch (PL_GetSlip(pl))
	{
	case 19: sp34 = a1*0.2F; break;
	case 20: sp34 = a1*0.7F; break;
	default: sp34 = a1*2.0F; break;
	case 21: sp34 = a1*3.0F; break;
	}
	if ((pl->speed = ConvergeF(pl->speed, 0, sp34, sp34)) == 0) result = TRUE;
	plwalk_80264B54(pl);
	return result;
}

static int plwalk_802651B0(PLAYER *pl)
{
	int result = FALSE;
	if ((pl->speed = ConvergeF(pl->speed, 0, 1, 1)) == 0) result = TRUE;
	PL_SetSpeed(pl, pl->speed);
	PL_ProcQuicksand(pl);
	PL_ProcWind(pl);
	return result;
}

static void plwalk_80265244(PLAYER *pl)
{

	float sp1C = pl->ground && pl->ground->code == BG_9 ? 24.0F : 32.0F;
	float sp18 = MIN(pl->stick_dist, sp1C);
	if (pl->sink > 10) sp18 *= 6.25/pl->sink;
	if      (pl->speed <= 0)            pl->speed += 1.1F;
	else if (pl->speed <= sp18)         pl->speed += 1.1F - pl->speed/43;
	else if (pl->ground->ny >= 0.95F)   pl->speed -= 1;
	if (pl->speed > 48) pl->speed = 48;
	pl->ang[1] = TURN(pl->ang[1], pl->stick_ang, 0x800);
	plwalk_80264B54(pl);
}

static int plwalk_80265458(PLAYER *pl)
{
	if (pl->status & PA_SLIPREQ)
	{
		int sp1C = (pl->scene->env & ENV_MASK) == ENV_SLIDER;
		int sp18 = pl->speed <= -1;
		if (sp1C || sp18 || PL_IsFaceDownSlope(pl, 0)) return TRUE;
	}
	return FALSE;
}

static int plwalk_80265514(PLAYER *pl)
{
	short dang = pl->stick_ang - pl->ang[1];
	return dang < -DEG(100) || DEG(100) < dang;
}

static int plwalk_80265558(PLAYER *pl)
{
	UNUSED int i;
	if (pl->status & PA_ATCKREQ)
	{
		if (pl->speed >= 29 && pl->cont->dist > 48)
		{
			pl->vel[1] = 20;
			return PL_SetState(pl, PS_JUMP_0A, 1);
		}
		return PL_SetState(pl, PS_WALK_17, 0);
	}
	return FALSE;
}

static int plwalk_80265620(PLAYER *pl)
{
	PL_DropObject(pl);
	if (pl->phase == 1)
	{
		pl->ang[1] = pl->code;
		return PL_SetState(pl, PS_WAIT_09, 0);
	}
	if (pl->speed >= 16 && pl->ground->ny >= COS_80)
	{
		return PL_SetState(pl, PS_WALK_05, 0);
	}
	return PL_SetState(pl, PS_WALK_0A, 0);
}

static void plwalk_80265700(PLAYER *pl)
{
	int vspeed;
	OBJECT *obj = pl->obj;
	int flag = TRUE;
	SHORT angx = 0;
	float speed = MAX(pl->stick_dist, pl->speed);
	if (speed < 4) speed = 4;
	if (pl->sink > 50)
	{
		vspeed = VSPEED(speed/4.0F);
		PL_SetAnimeV(pl, ANIME_120, vspeed);
		plwalk_80263EE4(pl, 19, 93);
		pl->timer = 0;
	}
	else
	{
		while (flag)
		{
			switch (pl->timer)
			{
			case 0:
				if (speed > 8) pl->timer = 2;
				else
				{
					if ((vspeed = VSPEED(speed/4.0F)) < VSPEED(1/16.0F))
					{
						vspeed = VSPEED(1/16.0F);
					}
					PL_SetAnimeV(pl, ANIME_202, vspeed);
					plwalk_80263EE4(pl, 7, 22);
					if (PL_IsAnimeAtFrame(pl, 23)) pl->timer = 2;
					flag = FALSE;
				}
				break;
			case 1:
				if (speed > 8) pl->timer = 2;
				else
				{
					if ((vspeed = VSPEED(speed)) < VSPEED(1/16.0F))
					{
						vspeed = VSPEED(1/16.0F);
					}
					PL_SetAnimeV(pl, ANIME_146, vspeed);
					plwalk_80263EE4(pl, 14, 72);
					flag = FALSE;
				}
				break;
			case 2:
				if      (speed <  5) pl->timer = 1;
				else if (speed > 22) pl->timer = 3;
				else
				{
					vspeed = VSPEED(speed/4.0F);
					PL_SetAnimeV(pl, ANIME_72, vspeed);
					plwalk_80263EE4(pl, 10, 49);
					flag = FALSE;
				}
				break;
			case 3:
				if (speed < 18) pl->timer = 2;
				else
				{
					vspeed = VSPEED(speed/4.0F);
					PL_SetAnimeV(pl, ANIME_114, vspeed);
					plwalk_80263EE4(pl, 9, 45);
					angx = plwalk_80263E60(pl);
					flag = FALSE;
				}
				break;
			}
		}
	}
	obj->o_v7 = (short)ConvergeI(obj->o_v7, angx, 0x800, 0x800);
	obj->s.ang[0] = obj->o_v7;
}

static void plwalk_80265B1C(PLAYER *pl)
{
	int vspeed;
	int flag = TRUE;
	float speed = MAX(pl->stick_dist, pl->speed);
	if (speed < 2) speed = 2;
	while (flag)
	{
		switch (pl->timer)
		{
		case 0:
			if (speed > 6) pl->timer = 1;
			else
			{
				vspeed = VSPEED(speed);
				PL_SetAnimeV(pl, ANIME_24, vspeed);
				plwalk_80263EE4(pl, 12, 62);
				flag = FALSE;
			}
			break;
		case 1:
			if      (speed <  3) pl->timer = 0;
			else if (speed > 11) pl->timer = 2;
			else
			{
				vspeed = VSPEED(speed);
				PL_SetAnimeV(pl, ANIME_22, vspeed);
				plwalk_80263EE4(pl, 12, 62);
				flag = FALSE;
			}
			break;
		case 2:
			if (speed < 8) pl->timer = 1;
			else
			{
				vspeed = VSPEED(speed/2.0F);
				PL_SetAnimeV(pl, ANIME_23, vspeed);
				plwalk_80263EE4(pl, 10, 49);
				flag = FALSE;
			}
			break;
		}
	}
}

static void plwalk_80265D90(PLAYER *pl)
{
	int vspeed = VSPEED(pl->stick_dist);
	PL_SetAnimeV(pl, ANIME_187, vspeed);
	plwalk_80263EE4(pl, 26, 79);
}

static void plwalk_80265DF8(PLAYER *pl, FVEC a1)
{
	SHORT wall_ang;
	short dang;
	float dx = pl->pos[0] - a1[0];
	float dz = pl->pos[2] - a1[2];
	float dist = DIST2(dx, dz);
	int vspeed = VSPEED(dist*2.0F);
	if (pl->speed > 6) PL_SetSpeed(pl, 6);
	if (pl->wall)
	{
		wall_ang = ATAN2(pl->wall->nz, pl->wall->nx);
		dang = wall_ang - pl->ang[1];
	}
	if (!pl->wall || dang < DEG(-160) || DEG(160) < dang)
	{
		pl->flag |= PL_80000000;
		PL_SetAnime(pl, ANIME_108);
		plwalk_80263EE4(pl, 6, 18);
	}
	else
	{
		if (dang < 0)   PL_SetAnimeV(pl, ANIME_128, vspeed);
		else            PL_SetAnimeV(pl, ANIME_127, vspeed);
		if (pl->obj->s.skel.frame < 20)
		{
			Na_ObjSePlay(NA_SE1_00+pl->surface, pl->obj);
			pl->effect |= PE_00000001;
		}
		pl->phase = 1;
		pl->code = wall_ang + 0x8000;
		pl->obj->s.ang[1] = wall_ang + 0x8000;
		pl->obj->s.ang[2] = PL_GetGroundAngX(pl, 0x4000);
	}
}

static void plwalk_80266038(PLAYER *pl, SHORT a1)
{
	PL_CTRL *ctrl = pl->ctrl;
	UNUSED OBJECT *obj = pl->obj;
	SHORT anime = pl->obj->s.skel.index;
	if (anime == ANIME_72 || anime == ANIME_114)
	{
		short dang = pl->ang[1] - a1;
		short angz = -(SHORT)(dang * pl->speed/12.0F);
		short angx = 0xAA*pl->speed;
		if (angz > DEG( 30)) angz = DEG( 30);
		if (angz < DEG(-30)) angz = DEG(-30);
		if (angx > DEG( 30)) angx = DEG( 30);
		if (angx < DEG(  0)) angx = DEG(  0);
		ctrl->torso_ang[2] = ConvergeI(ctrl->torso_ang[2], angz, 0x400, 0x400);
		ctrl->torso_ang[0] = ConvergeI(ctrl->torso_ang[0], angx, 0x400, 0x400);
	}
	else
	{
		ctrl->torso_ang[2] = 0;
		ctrl->torso_ang[0] = 0;
	}
}

static void plwalk_802661CC(PLAYER *pl, SHORT a1)
{
	PL_CTRL *ctrl = pl->ctrl;
	OBJECT *obj = pl->obj;
	short dang = pl->ang[1] - a1;
	short angz = -(SHORT)(dang * pl->speed/12.0F);
	short angx = 0xAA*pl->speed;
	if (angz >  0x1800) angz =  0x1800;
	if (angz < -0x1800) angz = -0x1800;
	if (angx >  0x1000) angx =  0x1000;
	if (angx <  0x0000) angx =  0x0000;
	ctrl->torso_ang[2] = ConvergeI(ctrl->torso_ang[2], angz, 0x200, 0x200);
	ctrl->torso_ang[0] = ConvergeI(ctrl->torso_ang[0], angx, 0x200, 0x200);
	ctrl->neck_ang[2] = -ctrl->torso_ang[2];
	obj->s.ang[2] = ctrl->torso_ang[2];
	obj->s.pos[1] += 45;
}

static int PL_ExecWalk00(PLAYER *pl)
{
	FVEC pos;
	short angy = pl->ang[1];
	PL_DropObject(pl);
	if (plwalk_80265458(pl)) return PL_SetState(pl, PS_WALK_10, 0);
	if (pl->status & PA_VIEWREQ) return plwalk_80265620(pl);
	if (pl->status & PA_JUMPREQ) return PL_SetTripJump(pl);
	if (plwalk_80265558(pl)) return TRUE;
	if (pl->status & PA_WAITREQ) return plwalk_80265620(pl);
	if (plwalk_80265514(pl) && pl->speed >= 16)
	{
		return PL_SetState(pl, PS_WALK_03, 0);
	}
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_WALK_19, 0);
	pl->phase = 0;
	FVecCpy(pos, pl->pos);
	plwalk_80265244(pl);
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, PS_JUMP_0C, 0);
		PL_SetAnime(pl, ANIME_86);
		break;
	case WALK_STAY:
		plwalk_80265700(pl);
		if (pl->stick_dist-pl->speed > 16) pl->effect |= PE_00000001;
		break;
	case WALK_STOP:
		plwalk_80265DF8(pl, pos);
		pl->timer = 0;
		break;
	}
	plwalk_802640FC(pl);
	plwalk_80266038(pl, angy);
	return FALSE;
}

static int PL_ExecWalk17(PLAYER *pl)
{
	if (plwalk_80265458(pl)) return PL_SetState(pl, PS_WALK_10, 0);
	if (pl->phase == 0 && pl->status & PA_JUMPSTA)
	{
		return PL_SetState(pl, PS_JUMP_2C, 0);
	}
	pl->phase = 1;
	platck_80274F10(pl);
	if (pl->speed >= 0)
	{
		plwalk_80265080(pl, 0.5F);
	}
	else
	{
		if ((pl->speed += 8) >= 0) pl->speed = 0;
		plwalk_80264B54(pl);
	}
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, PS_JUMP_0C, 0);
		break;
	case WALK_STAY:
		pl->effect |= PE_00000001;
		break;
	}
	return FALSE;
}

extern OBJLANG obj_13001650[];

static int PL_ExecWalk02(PLAYER *pl)
{
	if (pl->take->script == SegmentToVirtual(obj_13001650))
	{
		return PL_SetState(pl, PS_JUMP_2E, 0);
	}
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_WALK_00, 0);
	}
	if (plwalk_80265458(pl)) return PL_SetState(pl, PS_WALK_11, 0);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_08, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetStateJump(pl, PS_JUMP_20, 0);
	if (pl->status & PA_WAITREQ) return PL_SetState(pl, PS_WALK_0B, 0);
	if (pl->status & PA_TRIGREQ) return PL_SetStateDrop(pl, PS_WALK_19, 0);
	pl->stick_dist *= 0.4F;
	plwalk_80265244(pl);
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, PS_JUMP_21, 0);
		break;
	case WALK_STOP:
		if (pl->speed > 16) PL_SetSpeed(pl, 16);
		break;
	}
	plwalk_80265B1C(pl);
	if (0.4F*pl->stick_dist-pl->speed > 10) pl->effect |= PE_00000001;
	return FALSE;
}

static int PL_ExecWalk07(PLAYER *pl)
{
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_09, 0);
	if (plwalk_80265458(pl)) return PL_SetStateDrop(pl, PS_WALK_10, 0);
	if (pl->status & PA_WAITREQ) return PL_SetState(pl, PS_WAIT_08, 0);
	pl->stick_dist *= 0.1F;
	plwalk_80265244(pl);
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetStateDrop(pl, PS_JUMP_0C, 0);
		break;
	case WALK_STOP:
		if (pl->speed > 10) PL_SetSpeed(pl, 10);
		break;
	}
	plwalk_80265D90(pl);
	return FALSE;
}

static int PL_ExecWalk03(PLAYER *pl)
{
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetStateJump(pl, PS_JUMP_07, 0);
	if (pl->status & PA_WAITREQ) return PL_SetState(pl, PS_WALK_05, 0);
	if (!plwalk_80265514(pl)) return PL_SetState(pl, PS_WALK_00, 0);
	if (plwalk_80265080(pl, 2)) return plwalk_8026409C(pl, 8, PS_WALK_04, 0);
	Na_ObjSePlay(NA_SE1_00+pl->surface, pl->obj);
	PL_SetSpeedEffect(pl);
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, PS_JUMP_0C, 0);
		break;
	case WALK_STAY:
		pl->effect |= PE_00000001;
		break;
	}
	if (pl->speed >= 18)
	{
		PL_SetAnime(pl, ANIME_188);
	}
	else
	{
		PL_SetAnime(pl, ANIME_189);
		if (PL_IsAnimeLast1F(pl))
		{
			if (pl->speed > 0)  plwalk_8026409C(pl, -pl->speed, PS_WALK_00, 0);
			else                plwalk_8026409C(pl, 8, PS_WALK_00, 0);
		}
	}
	return FALSE;
}

static int PL_ExecWalk04(PLAYER *pl)
{
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetStateJump(pl, PS_JUMP_07, 0);
	plwalk_80265244(pl);
	PL_SetAnime(pl, ANIME_189);
	if (PL_ProcWalk(pl) == WALK_FALL) PL_SetState(pl, PS_JUMP_0C, 0);
	if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, PS_WALK_00, 0);
	pl->obj->s.ang[1] += 0x8000;
	return FALSE;
}

static int PL_ExecWalk05(PLAYER *pl)
{
	if (!(pl->status & PA_VIEWREQ) && pl->status & PA_MOTION)
	{
		return PL_CheckMotion(pl);
	}
	if (plwalk_80265080(pl, 2)) return PL_SetState(pl, PS_WAIT_3D, 0);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_WALK_17, 0);
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, PS_JUMP_0C, 0);
		break;
	case WALK_STAY:
		pl->effect |= PE_00000001;
		break;
	case WALK_STOP:
		plwalk_802642B4(pl, PS_WALK_22, PS_WAIT_3D);
		break;
	}
	Na_ObjSePlay(NA_SE1_00+pl->surface, pl->obj);
	PL_SetSpeedEffect(pl);
	PL_SetAnime(pl, ANIME_15);
	return FALSE;
}

static int PL_ExecWalk0A(PLAYER *pl)
{
	int vspeed;
	SHORT slip = PL_GetSlip(pl);
	if (!(pl->status & PA_VIEWREQ))
	{
		if (plwalk_80265458(pl)) return PL_SetState(pl, PS_WALK_10, 0);
		if (pl->status & PA_JUMPREQ) return PL_SetTripJump(pl);
		if (plwalk_80265558(pl)) return TRUE;
		if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_WALK_00, 0);
		if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_WALK_19, 0);
	}
	if (plwalk_802651B0(pl)) return PL_SetState(pl, PS_WAIT_01, 0);
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, PS_JUMP_0C, 0);
		break;
	case WALK_STOP:
		if (slip == 19) PL_Reflect(pl, TRUE);
		else PL_SetSpeed(pl, 0);
		break;
	}
	if (slip == 19)
	{
		PL_SetAnime(pl, ANIME_195);
		Na_ObjSePlay(NA_SE1_00+pl->surface, pl->obj);
		PL_SetSpeedEffect(pl);
		pl->effect |= PE_00000001;
	}
	else
	{
		if ((vspeed = VSPEED(pl->speed/4.0F)) < VSPEED(1/16.0F))
		{
			vspeed = VSPEED(1/16.0F);
		}
		PL_SetAnimeV(pl, ANIME_72, vspeed);
		plwalk_80263EE4(pl, 10, 49);
	}
	return FALSE;
}

static int PL_ExecWalk0B(PLAYER *pl)
{
	int vspeed;
	SHORT slip = PL_GetSlip(pl);
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_WALK_00, 0);
	}
	if (plwalk_80265458(pl)) return PL_SetState(pl, PS_WALK_11, 0);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_08, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetStateJump(pl, PS_JUMP_20, 0);
	if (pl->status & PA_TRIGREQ) return PL_SetStateDrop(pl, PS_WALK_19, 0);
	if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_WALK_02, 0);
	if (plwalk_802651B0(pl)) return PL_SetState(pl, PS_WAIT_07, 0);
	pl->stick_dist *= 0.4F;
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, PS_JUMP_21, 0);
		break;
	case WALK_STOP:
		if (slip == 19) PL_Reflect(pl, TRUE);
		else PL_SetSpeed(pl, 0);
		break;
	}
	if (slip == 19)
	{
		PL_SetAnime(pl, ANIME_63);
		Na_ObjSePlay(NA_SE1_00+pl->surface, pl->obj);
		PL_SetSpeedEffect(pl);
		pl->effect |= PE_00000001;
	}
	else
	{
		if ((vspeed = VSPEED(pl->speed)) < VSPEED(1/16.0F))
		{
			vspeed = VSPEED(1/16.0F);
		}
		PL_SetAnimeV(pl, ANIME_22, vspeed);
		plwalk_80263EE4(pl, 12, 62);
	}
	return FALSE;
}

static int PL_ExecWalk06(PLAYER *pl)
{
	SHORT angy = pl->ang[1];
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_JUMP_1A, 0);
	if (pl->status & PA_TRIGREQ)
	{
		PL_StopRide(pl);
		if (pl->speed < 24) PL_SetSpeed(pl, 24);
		return PL_SetState(pl, PS_WALK_19, 0);
	}
	plwalk_80264E18(pl);
	PL_SetAnime(pl, pl->code == 0 ? ANIME_109 : ANIME_71);
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, PS_JUMP_1B, 0);
		break;
	case WALK_STOP:
		PL_StopRide(pl);
		Na_ObjSePlay(pl->flag & PL_METALCAP ? NA_SE0_42 : NA_SE0_45, pl->obj);
		pl->effect |= PE_00000002;
		PL_SetState(pl, PS_WALK_22, 0);
		break;
	}
	plwalk_802661CC(pl, angy);
	if (pl->ground->code == BG_1) Na_ObjSePlay(NA_SE1_28, pl->obj);
	else Na_ObjSePlay(NA_SE1_20+pl->surface, pl->obj);
	PL_SetSpeedEffect(pl);
#ifdef MOTOR
	motor_8024C924();
#endif
	return FALSE;
}

static int PL_ExecWalk08(PLAYER *pl)
{
	int vspeed;
	if (plwalk_80265458(pl)) return PL_SetState(pl, PS_WALK_10, 0);
	if (pl->status & PA_VIEWREQ) return PL_SetState(pl, PS_WAIT_24, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetStateJump(pl, PS_JUMP_00, 0);
	if (plwalk_80265558(pl)) return TRUE;
	if (pl->status & PA_WAITREQ) return PL_SetState(pl, PS_WAIT_24, 0);
	if (!(pl->status & PA_TRIGSTA)) return PL_SetState(pl, PS_WAIT_24, 0);
	pl->stick_dist *= 0.1F;
	plwalk_80265244(pl);
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, PS_JUMP_0C, 0);
		break;
	case WALK_STOP:
		if (pl->speed > 10) PL_SetSpeed(pl, 10);
		FALLTHROUGH;
	case WALK_STAY:
		plwalk_80264024(pl);
		break;
	}
	vspeed = VSPEED(2.0F*pl->stick_dist);
	PL_SetAnimeV(pl, ANIME_153, vspeed);
	plwalk_80263EE4(pl, 26, 79);
	return FALSE;
}

static int PL_ExecWalk09(PLAYER *pl)
{
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_JUMP_34, 0);
	if ((pl->obj->o_v7 += 2) > 160) return PL_SetState(pl, PS_WALK_00, 0);
	if (pl->water-pl->ground_y > 50)
	{
		Na_ObjSePlay(NA_SE3_03, pl->obj);
		return PL_SetState(pl, PS_WALK_00, 0);
	}
	if (pl->speed < 8) pl->speed = 8;
	if (pl->speed > 48) pl->speed = 48;
	pl->speed = ConvergeF(pl->speed, 32, 4, 1);
	if (pl->status & PA_WALKREQ)
	{
		pl->ang[1] = TURN(pl->ang[1], pl->stick_ang, 0x600);
	}
	plwalk_80264B54(pl);
	if (PL_ProcWalk(pl) == WALK_FALL) PL_SetState(pl, PS_JUMP_35, 0);
	PL_SetAnimeV(pl, ANIME_114, VSPEED(pl->speed/2.0F));
	plwalk_80263EE4(pl, 9, 45);
	pl->effect |= PE_00000800;
	Na_ObjSePlay(NA_SE1_10, pl->obj);
	if ((pl->power -= 10) < 0x100) PL_SetState(pl, PS_DEMO_11, 0);
	pl->ctrl->eyes = 8;
#ifdef MOTOR
	motor_8024C924();
#endif
	return FALSE;
}

static void plwalk_80267C24(PLAYER *pl)
{
	SHORT dang = pl->stick_ang - pl->ang[1];
	pl->ctrl->torso_ang[0] =  (5461.3335F*pl->stick_dist/32.0F * COS(dang));
	pl->ctrl->torso_ang[2] = -(5461.3335F*pl->stick_dist/32.0F * SIN(dang));
}

static VOID plwalk_80267CE4(PLAYER *pl, u32 state1, u32 state2, int anime)
{
	FVEC pos;
	FVecCpy(pos, pl->pos);
	Na_ObjSePlay(NA_SE1_00+pl->surface, pl->obj);
#ifdef MOTOR
	motor_8024C924();
#endif
	PL_SetSpeedEffect(pl);
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, state2, 0);
		if (pl->speed < -50 || 50 < pl->speed) Na_ObjSePlay(NA_SE2_03, pl->obj);
		break;
	case WALK_STAY:
		PL_SetAnime(pl, anime);
		plwalk_80264024(pl);
		pl->effect |= PE_00000001;
		break;
	case WALK_STOP:
		if (!PL_IsSlipMin(pl))
		{
#if REVISION >= 199609
			if (pl->speed > 16) pl->effect |= PE_00000002;
#else
			pl->effect |= PE_00000002;
#endif
			plwalk_802642B4(pl, PS_WALK_26, state1);
		}
		else if (pl->wall)
		{
			SHORT sp3A = ATAN2(pl->wall->nz, pl->wall->nx);
			float sp34 = DIST2(pl->slide_x, pl->slide_z);
			if ((sp34 *= 0.9) < 4) sp34 = 4;
			pl->slide_ang = sp3A - (short)(pl->slide_ang-sp3A) + 0x8000;
			pl->vel[0] = pl->slide_x = sp34 * SIN(pl->slide_ang);
			pl->vel[2] = pl->slide_z = sp34 * COS(pl->slide_ang);
		}
		plwalk_80264024(pl);
		break;
	}
}

static int plwalk_80267FA4(
	PLAYER *pl, u32 state1, u32 state2, u32 state3, int anime
)
{
	if (pl->timer == 5)
	{
		if (pl->status & PA_JUMPREQ) return PL_SetStateJump(pl, state2, 0);
	}
	else
	{
		pl->timer++;
	}
	if (plwalk_80264740(pl, 4)) return PL_SetState(pl, state1, 0);
	plwalk_80267CE4(pl, state1, state3, anime);
	return FALSE;
}

static int PL_ExecWalk12(PLAYER *pl)
{
	int result =
		plwalk_80267FA4(pl, PS_WAIT_3E, PS_JUMP_00, PS_JUMP_0E, ANIME_145);
	plwalk_80267C24(pl);
	return result;
}

static int PL_ExecWalk14(PLAYER *pl)
{
	int result;
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_WALK_12, 0);
	}
	result = plwalk_80267FA4(pl, PS_WAIT_3F, PS_JUMP_20, PS_JUMP_22, ANIME_69);
	plwalk_80267C24(pl);
	return result;
}

static int PL_ExecWalk19(PLAYER *pl)
{
	int result;
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_12, 0);
	if (pl->timer < 30)
	{
		pl->timer++;
		if (pl->status & PA_JUMPREQ)
		{
			if (pl->speed > 10) return PL_SetStateJump(pl, PS_JUMP_08, 0);
		}
	}
	if (pl->status & PA_ATCKREQ)
	{
		if (pl->speed >= 10) return PL_SetState(pl, PS_JUMP_2A, 0);
		else return PL_SetState(pl, PS_WALK_17, 9);
	}
	if (pl->status & PA_JUMPREQ) return PL_SetStateJump(pl, PS_JUMP_00, 0);
	if (pl->status & PA_VIEWREQ) return PL_SetState(pl, PS_WALK_05, 0);
	result = plwalk_80267FA4(pl, PS_WAIT_20, PS_JUMP_00, PS_JUMP_0C, ANIME_151);
	return result;
}

static int PL_ExecWalk1A(PLAYER *pl)
{
	if (pl->status & PA_JUMPREQ)
	{
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		return PL_SetStateJump(pl, PS_JUMP_26, 0);
	}
	PL_SetAnime(pl, ANIME_140);
	if (PL_IsAnimeLast1F(pl) && pl->speed < 1)
	{
		return PL_SetState(pl, PS_WAIT_25, 0);
	}
	plwalk_80264740(pl, 1);
	switch (PL_ProcWalk(pl))
	{
	case WALK_FALL:
		PL_SetState(pl, PS_JUMP_0C, 2);
		break;
	case WALK_STOP:
		PL_Reflect(pl, TRUE);
		pl->effect |= PE_00000002;
		PL_SetState(pl, PS_WALK_22, 0);
		break;
	}
	Na_ObjSePlay(NA_SE1_00+pl->surface, pl->obj);
	pl->effect |= PE_00000001;
	return FALSE;
}

static int plwalk_802684AC(PLAYER *pl, u32 state1, u32 state2, int anime)
{
	if (pl->timer == 5)
	{
		if (!(pl->status & PA_SLIPREQ) && pl->status & (PA_JUMPREQ|PA_ATCKREQ))
		{
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
			return PL_SetStateDrop(
				pl, pl->speed >= 0 ? PS_JUMP_26 : PS_JUMP_2D, 0
			);
		}
	}
	else
	{
		pl->timer++;
	}
	if (plwalk_80264740(pl, 4)) return PL_SetState(pl, state1, 0);
	plwalk_80267CE4(pl, state1, state2, anime);
	return FALSE;
}

static int PL_ExecWalk13(PLAYER *pl)
{
	int result = plwalk_802684AC(pl, PS_ATCK_06, PS_JUMP_0C, ANIME_137);
	return result;
}

static int PL_ExecWalk15(PLAYER *pl)
{
	int result;
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_WALK_13, 0);
	}
	result = plwalk_802684AC(pl, PS_ATCK_05, PS_JUMP_21, ANIME_137);
	return result;
}

static int PL_ExecWalk16(PLAYER *pl)
{
	if (!(pl->status & PA_SLIPREQ) && pl->status & (PA_JUMPREQ|PA_ATCKREQ))
	{
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		return PL_SetState(pl, pl->speed > 0 ? PS_JUMP_26 : PS_JUMP_2D, 0);
	}
	PL_TrigLandEffect(pl, NA_SE0_18);
	if (plwalk_80264740(pl, 8) && PL_IsAnimeLast1F(pl))
	{
		PL_SetSpeed(pl, 0);
		PL_SetState(pl, PS_ATCK_06, 0);
	}
	if (PL_CheckTaking(pl))
	{
		PL_TakeObject(pl);
		pl->ctrl->take = 1;
		return TRUE;
	}
	plwalk_80267CE4(pl, PS_ATCK_06, PS_JUMP_0C, ANIME_136);
	return FALSE;
}

static int plwalk_802687B8(PLAYER *pl, int anime, int a2, int flag, int code)
{
	int frame;
	if (flag) PL_TrigFallEffect(pl, NA_SE0_18);
	if (code > 0)   PL_TrigSound(pl, NA_SE2_0A, PL_VOICE);
	else            PL_TrigSound(pl, NA_SE2_0B_D0, PL_VOICE);
	if (pl->speed >  32) pl->speed =  32;
	if (pl->speed < -32) pl->speed = -32;
	frame = PL_SetAnime(pl, anime);
	if (frame < a2)             plwalk_80264D80(pl, 0.9F);
	else if (pl->speed >= 0)    PL_SetSpeed(pl, 0.1F);
	else                        PL_SetSpeed(pl, -0.1F);
	if (PL_ProcWalk(pl) == WALK_FALL)
	{
		if (pl->speed >= 0) PL_SetState(pl, PS_JUMP_31, code);
		else                PL_SetState(pl, PS_JUMP_30, code);
	}
	else if (PL_IsAnimeLast1F(pl))
	{
		if (pl->power < 0x100)
		{
			PL_SetState(pl, PS_DEMO_11, 0);
		}
		else
		{
			if (code > 0) pl->invincible = 30;
			PL_SetState(pl, PS_WAIT_01, 0);
		}
	}
	return frame;
}

static int PL_ExecWalk20(PLAYER *pl)
{
	int frame = plwalk_802687B8(pl, ANIME_1, 43, TRUE, pl->code);
	if (frame == 43 && pl->power < 0x100) PL_SetState(pl, PS_DEMO_16, 0);
#if REVISION >= 199609
	if (frame == 54 && pl->prevstate == PS_DEMO_2C)
	{
		Na_ObjSePlay(NA_SE2_20, pl->obj);
	}
#endif
	if (frame == 69) PL_TrigLandEffect(pl, NA_SE0_08);
	return FALSE;
}

static int PL_ExecWalk21(PLAYER *pl)
{
	int frame = plwalk_802687B8(pl, ANIME_44, 21, TRUE, pl->code);
	if (frame == 23 && pl->power < 0x100) PL_SetState(pl, PS_DEMO_15, 0);
	return FALSE;
}

static int PL_ExecWalk22(PLAYER *pl)
{
	plwalk_802687B8(pl, ANIME_123, 22, TRUE, pl->code);
	return FALSE;
}

static int PL_ExecWalk23(PLAYER *pl)
{
	plwalk_802687B8(pl, ANIME_124, 20, TRUE, pl->code);
	return FALSE;
}

static int PL_ExecWalk24(PLAYER *pl)
{
	plwalk_802687B8(pl, ANIME_116, 100, FALSE, pl->code);
	return FALSE;
}

static int PL_ExecWalk25(PLAYER *pl)
{
	plwalk_802687B8(pl, ANIME_117, 100, FALSE, pl->code);
	return FALSE;
}

static int PL_ExecWalk26(PLAYER *pl)
{
	int frame = plwalk_802687B8(pl, ANIME_138, 32, TRUE, pl->code);
	if (frame == 32) PL_PlayLandEffect(pl, NA_SE0_08);
	return FALSE;
}

static int PL_ExecWalk27(PLAYER *pl)
{
	int frame;
	plwalk_80264D80(pl, 0.9F);
	PL_TrigFallEffect(pl, NA_SE0_18);
	frame = PL_SetAnime(pl, ANIME_1);
	if (frame == 54) Na_ObjSePlay(NA_SE2_20, pl->obj);
	if (frame == 68) PL_PlayLandEffect(pl, NA_SE0_08);
	if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, PS_WAIT_01, 0);
	return FALSE;
}

static int plwalk_80268DCC(PLAYER *pl, SHORT anime, u32 state)
{
	int result;
	if (pl->status & PA_WALKREQ)    plwalk_80264D80(pl, 0.98F);
	else if (pl->speed >= 16)       plwalk_80265080(pl, 2);
	else                            pl->vel[1] = 0;
	result = PL_ProcWalk(pl);
	switch (result)
	{
	case WALK_FALL:
		PL_SetState(pl, state, 0);
		break;
	case WALK_STOP:
		PL_SetAnime(pl, ANIME_108);
		break;
	}
	if (pl->speed > 16) pl->effect |= PE_00000001;
	PL_SetAnime(pl, anime);
	PL_TrigLandEffect(pl, NA_SE0_08);
	if (pl->ground->code >= BG_33 && pl->ground->code <= BG_39)
	{
		pl->sink += (4-pl->timer)*3.5F - 0.5F;
	}
	return result;
}

typedef struct plwalk
{
	short time, jump_timer;
	u32 slip, next, jump, land, slide;
}
PLWALK;

static int plwalk_80268F78(
	PLAYER *pl, PLWALK *walk, int (*setstate)(PLAYER *, u32, u32)
)
{
	if (pl->ground->ny < COS_73) return PL_SteepFall(pl, walk->slip, 0);
	pl->jump_timer = walk->jump_timer;
	if (plwalk_80265458(pl)) return PL_SetState(pl, walk->slide, 0);
	if (pl->status & PA_VIEWREQ) return PL_SetState(pl, walk->next, 0);
	if (++pl->timer >= walk->time) return PL_SetState(pl, walk->next, 0);
	if (pl->status & PA_JUMPREQ)
	{
		return setstate(pl, walk->jump, 0);
	}
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, walk->land, 0);
	return FALSE;
}

static int PL_ExecWalk30(PLAYER *pl)
{
	static PLWALK plwalk_8032DC50 =
		{4, 5, PS_JUMP_0C, PS_WAIT_30, PS_JUMP_01, PS_JUMP_0C, PS_WALK_10};
	if (plwalk_80268F78(pl, &plwalk_8032DC50, PL_SetStateJump)) return TRUE;
	plwalk_80268DCC(pl, ANIME_78, PS_JUMP_0C);
	return FALSE;
}

static int PL_ExecWalk31(PLAYER *pl)
{
	static PLWALK plwalk_8032DC68 =
		{4, 5, PS_JUMP_0C, PS_WAIT_32, PS_JUMP_01, PS_JUMP_0C, PS_WALK_10};
	if (plwalk_80268F78(pl, &plwalk_8032DC68, PL_SetStateJump)) return TRUE;
	plwalk_80268DCC(pl, ANIME_87, PS_JUMP_0C);
	return FALSE;
}

static int PL_ExecWalk33(PLAYER *pl)
{
	static PLWALK plwalk_8032DC80 =
		{4, 5, PS_JUMP_0C, PS_WAIT_33, PS_JUMP_01, PS_JUMP_0C, PS_WALK_10};
	if (plwalk_80268F78(pl, &plwalk_8032DC80, PL_SetStateJump)) return TRUE;
	if (plwalk_80268DCC(pl, ANIME_190, PS_JUMP_0C) != WALK_STOP)
	{
		pl->obj->s.ang[1] += 0x8000;
	}
	return FALSE;
}

static int PL_ExecWalk34(PLAYER *pl)
{
	static PLWALK plwalk_8032DC98 =
		{4, 5, PS_JUMP_21, PS_WAIT_34, PS_JUMP_20, PS_JUMP_21, PS_WALK_11};
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_WAIT_30, 0);
	}
	if (plwalk_80268F78(pl, &plwalk_8032DC98, PL_SetStateJump)) return TRUE;
	plwalk_80268DCC(pl, ANIME_64, PS_JUMP_21);
	return FALSE;
}

static int PL_ExecWalk35(PLAYER *pl)
{
	static PLWALK plwalk_8032DCB0 =
		{4, 5, PS_JUMP_21, PS_WAIT_35, PS_JUMP_20, PS_JUMP_21, PS_WALK_11};
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_WAIT_32, 0);
	}
	if (plwalk_80268F78(pl, &plwalk_8032DCB0, PL_SetStateJump)) return TRUE;
	plwalk_80268DCC(pl, ANIME_66, PS_JUMP_21);
	return FALSE;
}

static int PL_ExecWalk39(PLAYER *pl)
{
	static PLWALK plwalk_8032DCC8 =
		{6, 5, PS_JUMP_0C, PS_WAIT_3B, PS_JUMP_08, PS_JUMP_0C, PS_WALK_10};
#if REVISION >= 199707
	if (pl->speed < 0) pl->speed = 0;
#endif
	if (!(pl->status & PA_TRIGSTA)) pl->status &= ~PA_JUMPREQ;
	if (plwalk_80268F78(pl, &plwalk_8032DCC8, PL_SetStateJump)) return TRUE;
	if (!(pl->status & PA_WALKREQ)) PL_TrigSound(pl, NA_SE2_13_80, PL_VOICE);
	plwalk_80268DCC(pl, pl->obj->o_v7 == 0 ? ANIME_17 : ANIME_18, PS_JUMP_0C);
	return FALSE;
}

static int PL_ExecWalk32(PLAYER *pl)
{
	static PLWALK plwalk_8032DCE0 =
		{4, 5, PS_JUMP_0C, PS_WAIT_31, PS_JUMP_00, PS_JUMP_0C, PS_WALK_10};
	if (plwalk_80268F78(pl, &plwalk_8032DCE0, &plwalk_80264340)) return TRUE;
	plwalk_80268DCC(pl, ANIME_75, PS_JUMP_0C);
	return FALSE;
}

static int PL_ExecWalk38(PLAYER *pl)
{
	static PLWALK plwalk_8032DCF8 =
		{4, 0, PS_JUMP_0C, PS_WAIT_3A, PS_NULL, PS_JUMP_0C, PS_WALK_10};
	pl->status &= ~PA_JUMPREQ;
	if (plwalk_80268F78(pl, &plwalk_8032DCF8, PL_SetStateJump)) return TRUE;
	if (!(pl->status & PA_WALKREQ)) PL_TrigSound(pl, NA_SE2_11_80, PL_VOICE);
	plwalk_80268DCC(pl, ANIME_192, PS_JUMP_0C);
	return FALSE;
}

static int PL_ExecWalk3A(PLAYER *pl)
{
	static PLWALK plwalk_8032DD10 =
		{4, 0, PS_JUMP_0C, PS_WAIT_2F, PS_JUMP_03, PS_JUMP_0C, PS_WALK_10};
	if (!(pl->status & PA_TRIGSTA)) pl->status &= ~PA_JUMPREQ;
	if (plwalk_80268F78(pl, &plwalk_8032DD10, PL_SetStateJump)) return TRUE;
	if (!(pl->status & PA_WALKREQ)) PL_TrigSound(pl, NA_SE2_11_80, PL_VOICE);
	plwalk_80268DCC(pl, ANIME_192, PS_JUMP_0C);
	return FALSE;
}

static int plwalk_80269640(
	PLAYER *pl, int anime1, int anime2, u32 state3, u32 state4
)
{
	if (pl->timer++ < 6)
	{
		pl->sink -= (7-pl->timer) * 0.8F;
		if (pl->sink < 1) pl->sink = 1.1F;
		PL_TrigJumpVoice(pl);
		PL_SetAnime(pl, anime1);
	}
	else
	{
		if (pl->timer >= 13) return PL_SetState(pl, state3, 0);
		PL_SetAnime(pl, anime2);
	}
	plwalk_80264D80(pl, 0.95F);
	if (PL_ProcWalk(pl) == WALK_FALL) PL_SetState(pl, state4, 0);
	return FALSE;
}

static int PL_ExecWalk36(PLAYER *pl)
{
	int result =
		plwalk_80269640(pl, ANIME_77, ANIME_78, PS_WAIT_30, PS_JUMP_0C);
	return result;
}

static int PL_ExecWalk37(PLAYER *pl)
{
	int result =
		plwalk_80269640(pl, ANIME_65, ANIME_64, PS_WAIT_34, PS_JUMP_21);
	return result;
}

static int plwalk_80269830(PLAYER *pl)
{
	if (pl->pos[1] < pl->water-100) return PL_EnterWater(pl);
	if (!(pl->state & PF_DMGE) && pl->status & PA_HIT)
	{
		return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	}
	if (pl->status & PA_PRESREQ) return PL_SetStateDrop(pl, PS_DEMO_39, 0);
	if (!(pl->state & PF_DMGE))
	{
		if (pl->power < 0x100) return PL_SetStateDrop(pl, PS_DEMO_11, 0);
	}
	return FALSE;
}

int PL_ExecWalk(PLAYER *pl)
{
	int result;
	if (plwalk_80269830(pl)) return TRUE;
	if (PL_ProcSink(pl, 0.25F)) return TRUE;
	switch (pl->state)
	{
	case PS_WALK_00: result = PL_ExecWalk00(pl); break;
	case PS_WALK_02: result = PL_ExecWalk02(pl); break;
	case PS_WALK_07: result = PL_ExecWalk07(pl); break;
	case PS_WALK_03: result = PL_ExecWalk03(pl); break;
	case PS_WALK_04: result = PL_ExecWalk04(pl); break;
	case PS_WALK_05: result = PL_ExecWalk05(pl); break;
	case PS_WALK_06: result = PL_ExecWalk06(pl); break;
	case PS_WALK_08: result = PL_ExecWalk08(pl); break;
	case PS_WALK_09: result = PL_ExecWalk09(pl); break;
	case PS_WALK_0A: result = PL_ExecWalk0A(pl); break;
	case PS_WALK_0B: result = PL_ExecWalk0B(pl); break;
	case PS_WALK_12: result = PL_ExecWalk12(pl); break;
	case PS_WALK_13: result = PL_ExecWalk13(pl); break;
	case PS_WALK_14: result = PL_ExecWalk14(pl); break;
	case PS_WALK_15: result = PL_ExecWalk15(pl); break;
	case PS_WALK_16: result = PL_ExecWalk16(pl); break;
	case PS_WALK_17: result = PL_ExecWalk17(pl); break;
	case PS_WALK_19: result = PL_ExecWalk19(pl); break;
	case PS_WALK_1A: result = PL_ExecWalk1A(pl); break;
	case PS_WALK_20: result = PL_ExecWalk20(pl); break;
	case PS_WALK_21: result = PL_ExecWalk21(pl); break;
	case PS_WALK_22: result = PL_ExecWalk22(pl); break;
	case PS_WALK_23: result = PL_ExecWalk23(pl); break;
	case PS_WALK_24: result = PL_ExecWalk24(pl); break;
	case PS_WALK_25: result = PL_ExecWalk25(pl); break;
	case PS_WALK_26: result = PL_ExecWalk26(pl); break;
	case PS_WALK_27: result = PL_ExecWalk27(pl); break;
	case PS_WALK_30: result = PL_ExecWalk30(pl); break;
	case PS_WALK_31: result = PL_ExecWalk31(pl); break;
	case PS_WALK_32: result = PL_ExecWalk32(pl); break;
	case PS_WALK_33: result = PL_ExecWalk33(pl); break;
	case PS_WALK_34: result = PL_ExecWalk34(pl); break;
	case PS_WALK_35: result = PL_ExecWalk35(pl); break;
	case PS_WALK_38: result = PL_ExecWalk38(pl); break;
	case PS_WALK_3A: result = PL_ExecWalk3A(pl); break;
	case PS_WALK_36: result = PL_ExecWalk36(pl); break;
	case PS_WALK_37: result = PL_ExecWalk37(pl); break;
	case PS_WALK_39: result = PL_ExecWalk39(pl); break;
	}
	if (!result)
	{
		if (pl->status & PA_WADING)
		{
			pl->effect |= PE_00000400;
			pl->effect &= ~PE_00000001;
		}
	}
	return result;
}
