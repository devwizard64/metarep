#include <sm64.h>

static void pljump_80269F40(
	PLAYER *pl, SHORT frame1, SHORT frame2, SHORT frame3
)
{
	int frame = pl->obj->s.skel.frame;
	if (frame1 == frame || frame2 == frame || frame3 == frame)
	{
		Na_ObjSePlay(NA_SE0_37, pl->obj);
	}
}

static void pljump_80269FC0(PLAYER *pl)
{
	u32 state = pl->state;
	if (!(state & PF_DMGE) && state != PS_JUMP_24 && state != PS_JUMP_19)
	{
		if (!(pl->flag & PL_00040000))
		{
			if (pl->peak-pl->pos[1] > 1150)
			{
				Na_ObjSePlay(NA_SE2_10, pl->obj);
				pl->flag |= PL_00040000;
			}
		}
	}
}

#if REVISION >= 199609
static void pljump_8026A090(PLAYER *pl)
{
	if (pl->code == 0 && (pl->speed <= -28 || 28 <= pl->speed))
	{
		PL_TrigSound(pl, NA_SE2_30, PL_VOICE);
	}
	else
	{
		PL_TrigSound(pl, NA_SE2_05, PL_VOICE);
	}
}
#else
#define pljump_8026A090(pl) PL_TrigSound(pl, NA_SE2_05, PL_VOICE)
#endif

static int pljump_8026A12C(PLAYER *pl)
{
	pl->ang[1] = ATAN2(pl->wall->nz, pl->wall->nx);
	if (pl->speed < 24) pl->speed = 24;
	if (!(pl->flag & PL_METALCAP)) PL_Damage(pl, 3);
	Na_ObjSePlay(NA_SE2_14, pl->obj);
	player_802521A0(pl);
	return PL_SetStateDrop(pl, PS_JUMP_37, 1);
}

static int pljump_8026A224(PLAYER *pl, u32 state)
{
	float height = pl->peak - pl->pos[1];
#ifdef sgi
	float sp28 = pl->phase == PS_JUMP_29 ? 600.0F : 1150.0F;
#else
	float sp28 = 1150;
#endif
	if (pl->state != PS_JUMP_24 && pl->ground->code != BG_1)
	{
		if (pl->vel[1] < -55)
		{
			if (height > 3000)
			{
				PL_Damage(pl, 4);
#ifdef MOTOR
				motor_8024C834(5, 80);
#endif
				camera_8027F590(9);
				Na_ObjSePlay(NA_SE2_0A, pl->obj);
				return PL_SetStateDrop(pl, state, 4);
			}
			else if (height > sp28 && !PL_IsSlipMin(pl))
			{
				PL_Damage(pl, 2);
				pl->press = 30;
#ifdef MOTOR
				motor_8024C834(5, 80);
#endif
				camera_8027F590(9);
				Na_ObjSePlay(NA_SE2_0A, pl->obj);
			}
		}
	}
	return FALSE;
}

static int pljump_8026A400(PLAYER *pl)
{
	if (pl->status & PA_ATCKREQ)
	{
		return PL_SetState(pl, pl->speed > 28 ? PS_JUMP_0A : PS_JUMP_2C, 0);
	}
	return FALSE;
}

static int pljump_8026A494(PLAYER *pl)
{
	int env = pl->scene->env & ENV_MASK;
	BGFACE *ground = pl->ground;
	int flag = ground->flag;
	int code = ground->code;
	if (
		ground && (env == ENV_SNOW || env == ENV_SAND) &&
		!(code == BG_1 || code == BG_48 || (code >= BG_53 && code <= BG_55)) &&
		!(flag & BG_MOVE) && pl->peak-pl->pos[1] > 1000 && ground->ny >= COS_30
	) return TRUE;
	return FALSE;
}

static int pljump_8026A598(PLAYER *pl, u32 state)
{
	if (pljump_8026A494(pl))
	{
		Na_ObjSePlay(NA_SE2_0B_D0, pl->obj);
		pl->effect |= PE_00010000;
		PL_SetStateDrop(pl, PS_DEMO_3C, 0);
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		return TRUE;
	}
	return pljump_8026A224(pl, state);
}

static int pljump_8026A62C(PLAYER *pl)
{
	BGFACE *ground = pl->ground;
	if (ground->code == BG_44)
	{
		float speed;
		short angy = ground->attr << 8;
		pl->slide_x += 1.2F * SIN(angy);
		pl->slide_z += 1.2F * COS(angy);
		speed = DIST2(pl->slide_x, pl->slide_z);
		if (speed > 48)
		{
			pl->slide_x = pl->slide_x * 48/speed;
			pl->slide_z = pl->slide_z * 48/speed;
			speed = 32;
		}
		else if (speed > 32)
		{
			speed = 32;
		}
		pl->vel[0] = pl->slide_x;
		pl->vel[2] = pl->slide_z;
		pl->slide_ang = ATAN2(pl->slide_z, pl->slide_x);
		pl->speed = speed * COS(pl->ang[1]-pl->slide_ang);
#if REVISION < 199609
		Na_ObjSePlay(NA_SE4_10, pl->obj);
#endif
		return TRUE;
	}
	return FALSE;
}

static void pljump_8026A818(PLAYER *pl)
{
	if (!pljump_8026A62C(pl))
	{
		float limit = pl->state == PS_JUMP_08 ? 48.0F : 32.0F;
		pl->speed = ConvergeF(pl->speed, 0, 0.35F, 0.35F);
		if (pl->status & PA_WALKREQ)
		{
			SHORT dang = pl->stick_ang - pl->ang[1];
			float accel = pl->stick_dist / 32.0F;
			pl->speed += 1.5F * COS(dang) * accel;
			pl->ang[1] += 0x200 * SIN(dang) * accel;
		}
		if (pl->speed > limit) pl->speed -= 1;
		if (pl->speed < -16) pl->speed += 2;
		pl->vel[0] = pl->slide_x = pl->speed * SIN(pl->ang[1]);
		pl->vel[2] = pl->slide_z = pl->speed * COS(pl->ang[1]);
	}
}

static void pljump_8026AA48(PLAYER *pl)
{
	float side = 0;
	if (!pljump_8026A62C(pl))
	{
		float limit = pl->state == PS_JUMP_08 ? 48.0F : 32.0F;
		pl->speed = ConvergeF(pl->speed, 0, 0.35F, 0.35F);
		if (pl->status & PA_WALKREQ)
		{
			SHORT dang = pl->stick_ang - pl->ang[1];
			float accel = pl->stick_dist / 32.0F;
			pl->speed += accel * COS(dang) * 1.5F;
			side = accel * SIN(dang) * 10;
		}
		if (pl->speed > limit) pl->speed -= 1;
		if (pl->speed < -16) pl->speed += 2;
		pl->slide_x = pl->speed * SIN(pl->ang[1]);
		pl->slide_z = pl->speed * COS(pl->ang[1]);
		pl->slide_x += side * SIN(pl->ang[1]+0x4000);
		pl->slide_z += side * COS(pl->ang[1]+0x4000);
		pl->vel[0] = pl->slide_x;
		pl->vel[2] = pl->slide_z;
	}
}

static void pljump_8026ACD8(PLAYER *pl)
{
	if (pl->status & PA_WALKREQ)
	{
		SHORT dang = pl->stick_ang - pl->ang[1];
		float accel = pl->stick_dist / 32.0F;
		pl->speed += COS(dang) * accel;
		pl->ang[1] += SIN(dang) * accel * 0x400;
		if (pl->speed < 0)
		{
			pl->ang[1] += 0x8000;
			pl->speed *= -1;
		}
		if (pl->speed > 32) pl->speed -= 2;
	}
	pl->vel[0] = pl->slide_x = pl->speed * SIN(pl->ang[1]);
	pl->vel[2] = pl->slide_z = pl->speed * COS(pl->ang[1]);
}

static void pljump_8026AE5C(PLAYER *pl)
{
	short rot = -(SHORT)(pl->cont->x * (pl->speed/4.0F));
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
	pl->ang[2] = 20 * -pl->rot[1];
}

static void pljump_8026B004(PLAYER *pl)
{
	short rot = -(SHORT)(pl->cont->y * (pl->speed/5.0F));
	if (rot > 0)
	{
		if (pl->rot[0] < 0)
		{
			pl->rot[0] += 0x40;
			if (pl->rot[0] > 0x20) pl->rot[0] = 0x20;
		}
		else
		{
			pl->rot[0] = ConvergeI(pl->rot[0], rot, 0x20, 0x40);
		}
	}
	else if (rot < 0)
	{
		if (pl->rot[0] > 0)
		{
			pl->rot[0] -= 0x40;
			if (pl->rot[0] < -0x20) pl->rot[0] = -0x20;
		}
		else
		{
			pl->rot[0] = ConvergeI(pl->rot[0], rot, 0x40, 0x20);
		}
	}
	else
	{
		pl->rot[0] = ConvergeI(pl->rot[0], 0, 0x40, 0x40);
	}
}

static void pljump_8026B17C(PLAYER *pl)
{
	UNUSED int i;
	pljump_8026B004(pl);
	pljump_8026AE5C(pl);
	pl->speed -= 2.0F * ((float)pl->ang[0]/0x4000) + 0.1F;
	pl->speed -= 0.5F * (1-COS(pl->rot[1]));
	if (pl->speed < 0) pl->speed = 0;
	if      (pl->speed > 16)    pl->ang[0] += (pl->speed-32)*6;
	else if (pl->speed >  4)    pl->ang[0] += (pl->speed-32)*10;
	else                        pl->ang[0] -= 0x400;
	pl->ang[0] += pl->rot[0];
	if (pl->ang[0] > DEG( 60)) pl->ang[0] = DEG( 60);
	if (pl->ang[0] < DEG(-60)) pl->ang[0] = DEG(-60);
	pl->vel[0] = pl->speed * COS(pl->ang[0]) * SIN(pl->ang[1]);
	pl->vel[1] = pl->speed * SIN(pl->ang[0]);
	pl->vel[2] = pl->speed * COS(pl->ang[0]) * COS(pl->ang[1]);
	pl->slide_x = pl->vel[0];
	pl->slide_z = pl->vel[2];
}

static int pljump_8026B444(PLAYER *pl, u32 state, int anime, int flag)
{
	int result;
	pljump_8026AA48(pl);
	result = PL_ProcJump(pl, flag);
	switch (result)
	{
	case JUMP_STAY:
		PL_SetAnime(pl, anime);
		break;
	case JUMP_LAND:
		if (!pljump_8026A598(pl, PS_WALK_20)) PL_SetState(pl, state, 0);
		break;
	case JUMP_WALL:
		PL_SetAnime(pl, anime);
		if (pl->speed > 16)
		{
#ifdef MOTOR
			motor_8024C834(5, 40);
#endif
			PL_Reflect(pl, FALSE);
			pl->ang[1] += 0x8000;
			if (pl->wall)
			{
				PL_SetState(pl, PS_JUMP_27, 0);
			}
			else
			{
				if (pl->vel[1] > 0) pl->vel[1] = 0;
				if (pl->speed >= 38)
				{
					pl->effect |= PE_00000002;
					PL_SetState(pl, PS_JUMP_30, 0);
				}
				else
				{
					if (pl->speed > 8) PL_SetSpeed(pl, -8);
					return PL_SetState(pl, PS_JUMP_36, 0);
				}
			}
		}
		else
		{
			PL_SetSpeed(pl, 0);
		}
		break;
	case JUMP_LEDGE:
		PL_SetAnime(pl, ANIME_51);
		PL_SetStateDrop(pl, PS_SPEC_0B, 0);
		break;
	case JUMP_HANG:
		PL_SetState(pl, PS_SPEC_08, 0);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	return result;
}

static int PL_ExecJump00(PLAYER *pl)
{
	if (pljump_8026A400(pl)) return TRUE;
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_JUMP_29, 0);
	PL_TrigJumpEffect(pl, NA_SE0_00, PL_JUMPVOICE);
	pljump_8026B444(pl, PS_WALK_30, ANIME_77, 3);
	return FALSE;
}

static int PL_ExecJump01(PLAYER *pl)
{
	int anime = pl->vel[1] >= 0 ? ANIME_80 : ANIME_76;
	if (pljump_8026A400(pl)) return TRUE;
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_JUMP_29, 0);
	PL_TrigJumpEffect(pl, NA_SE0_00, NA_SE2_03);
	pljump_8026B444(pl, PS_WALK_32, anime, 3);
	return FALSE;
}

static int PL_ExecJump02(PLAYER *pl)
{
	if (bu_jump) return PL_SetState(pl, PS_JUMP_2F, 0);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_JUMP_0A, 0);
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_JUMP_29, 0);
#if REVISION >= 199609
	PL_TrigJumpEffect(pl, NA_SE0_00, PL_JUMPVOICE);
#else
	PL_TrigJumpEffect(pl, NA_SE0_00, NA_SE2_04);
#endif
	pljump_8026B444(pl, PS_WALK_38, ANIME_193, 0);
#ifdef MOTOR
	if (pl->state == PS_WALK_38) motor_8024C834(5, 40);
#endif
	pljump_80269F40(pl, 2, 8, 20);
	return FALSE;
}

static int PL_ExecJump03(PLAYER *pl)
{
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_JUMP_29, 0);
	PL_TrigJumpEffect(pl, NA_SE0_00, NA_SE2_00);
	pljump_8026B444(pl, PS_WALK_3A, ANIME_4, 0);
#ifdef MOTOR
	if (pl->state == PS_WALK_3A) motor_8024C834(5, 40);
#endif
	pljump_80269F40(pl, 2, 3, 17);
	return FALSE;
}

static int PL_ExecJump0C(PLAYER *pl)
{
	int anime;
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_JUMP_0A, 0);
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_JUMP_29, 0);
	switch (pl->code)
	{
	case 0: anime = ANIME_86; break;
	case 1: anime = ANIME_144; break;
	case 2: anime = ANIME_83; break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
	pljump_8026B444(pl, PS_WALK_31, anime, 1);
	return FALSE;
}

static int PL_ExecJump20(PLAYER *pl)
{
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_JUMP_0C, 0);
	}
	if (pl->status & PA_ATCKREQ && !(pl->take->o_hit_flag & HF_0010))
	{
		return PL_SetState(pl, PS_JUMP_2B, 0);
	}
	if (pl->status & PA_TRIGREQ) return PL_SetStateDrop(pl, PS_JUMP_29, 0);
	PL_TrigJumpEffect(pl, NA_SE0_00, PL_JUMPVOICE);
	pljump_8026B444(pl, PS_WALK_34, ANIME_65, 1);
	return FALSE;
}

static int PL_ExecJump21(PLAYER *pl)
{
	int anime = pl->code == 0 ? ANIME_67 : ANIME_68;
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_JUMP_0C, 0);
	}
	if (pl->status & PA_ATCKREQ && !(pl->take->o_hit_flag & HF_0010))
	{
		return PL_SetState(pl, PS_JUMP_2B, 0);
	}
	if (pl->status & PA_TRIGREQ) return PL_SetStateDrop(pl, PS_JUMP_29, 0);
	pljump_8026B444(pl, PS_WALK_35, anime, 1);
	return FALSE;
}

static int PL_ExecJump07(PLAYER *pl)
{
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_JUMP_0A, 0);
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_JUMP_29, 0);
	PL_TrigJumpEffect(pl, NA_SE0_00, PL_JUMPVOICE);
	if (pljump_8026B444(pl, PS_WALK_33, ANIME_191, 1) != JUMP_LEDGE)
	{
		pl->obj->s.ang[1] += 0x8000;
	}
	if (pl->obj->s.skel.frame == 6) Na_ObjSePlay(NA_SE0_5A, pl->obj);
	return FALSE;
}

static int PL_ExecJump06(PLAYER *pl)
{
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_JUMP_0A, 0);
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_JUMP_29, 0);
	PL_TrigJumpVoice(pl);
	pljump_8026B444(pl, PS_WALK_30, ANIME_203, 1);
	return FALSE;
}

static int PL_ExecJump08(PLAYER *pl)
{
	int anime = pl->obj->o_v7 == 0 ? ANIME_19 : ANIME_20;
	PL_TrigJumpEffect(pl, NA_SE0_00, NA_SE2_04);
	if (pl->ground->code == BG_56 && pl->phase == 0)
	{
		Na_ObjSePlay(NA_SE2_0C, pl->obj);
		pl->phase = 1;
	}
	pljump_8026B444(pl, PS_WALK_39, anime, 1);
#ifdef MOTOR
	if (pl->state == PS_WALK_39) motor_8024C834(5, 40);
#endif
	return FALSE;
}

static int PL_ExecJump1A_1B(PLAYER *pl)
{
	PL_TrigJumpEffect(pl, NA_SE0_00, PL_JUMPVOICE);
	PL_SetAnime(pl, ANIME_74);
	pljump_8026AA48(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		PL_SetState(pl, PS_WALK_06, 1);
		break;
	case JUMP_WALL:
		PL_SetSpeed(pl, 0);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	pl->obj->s.pos[1] += 42;
	return FALSE;
}

static int PL_ExecJump24(PLAYER *pl)
{
	SHORT spin_ang = pl->spin_ang;
	SHORT rot = pl->status & PA_JUMPSTA ? 0x2000 : 0x1800;
	pl->rot[1] = ConvergeI(pl->rot[1], rot, 0x200, 0x200);
	pl->spin_ang += pl->rot[1];
	PL_SetAnime(pl, pl->code == 0 ? ANIME_149 : ANIME_148);
	if (PL_IsAnimeLast2F(pl)) pl->code = 1;
	if (spin_ang > pl->spin_ang) Na_ObjSePlay(NA_SE0_38, pl->obj);
	pljump_8026ACD8(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		PL_SetState(pl, PS_WAIT_38, 0);
		break;
	case JUMP_WALL:
		PL_Reflect(pl, FALSE);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	pl->obj->s.ang[1] += pl->spin_ang;
#ifdef MOTOR
	motor_8024C924();
#endif
	return FALSE;
}

static int PL_ExecJump0A(PLAYER *pl)
{
	if (pl->code == 0)  PL_TrigJumpEffect(pl, NA_SE0_35, NA_SE2_03);
	else                PL_TrigJumpEffect(pl, NA_SE0_00, PL_JUMPVOICE);
	PL_SetAnime(pl, ANIME_136);
	if (PL_CheckTaking(pl))
	{
		PL_TakeObject(pl);
		pl->ctrl->take = 1;
		if (pl->state != PS_JUMP_0A) return TRUE;
	}
	pljump_8026AA48(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_STAY:
		if (pl->vel[1] < 0 && pl->ang[0] > DEG(-60))
		{
			pl->ang[0] -= 0x200;
			if (pl->ang[0] < DEG(-60)) pl->ang[0] = DEG(-60);
		}
		pl->obj->s.ang[0] = -pl->ang[0];
		break;
	case JUMP_LAND:
		if (pljump_8026A494(pl) && pl->ang[0] == DEG(-60))
		{
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
			Na_ObjSePlay(NA_SE2_0B_D0, pl->obj);
			pl->effect |= PE_00010000;
			PL_SetStateDrop(pl, PS_DEMO_3A, 0);
		}
		else if (!pljump_8026A224(pl, PS_WALK_21))
		{
			if (!pl->take)  PL_SetState(pl, PS_WALK_16, 0);
			else            PL_SetState(pl, PS_ATCK_05, 0);
		}
		pl->ang[0] = 0;
		break;
	case JUMP_WALL:
		PL_Reflect(pl, TRUE);
		pl->ang[0] = 0;
		if (pl->vel[1] > 0) pl->vel[1] = 0;
		pl->effect |= PE_00000002;
		PL_SetStateDrop(pl, PS_JUMP_30, 0);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	return FALSE;
}

static int PL_ExecJump2B(PLAYER *pl)
{
	if (++pl->timer == 4) PL_ThrowObject(pl);
	PL_TrigSound(pl, NA_SE2_07, PL_VOICE);
	PL_SetAnime(pl, ANIME_82);
	pljump_8026AA48(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		if (!pljump_8026A598(pl, PS_WALK_20)) pl->state = PS_WAIT_36;
		break;
	case JUMP_WALL:
		PL_SetSpeed(pl, 0);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	return FALSE;
}

static int PL_ExecJump09(PLAYER *pl)
{
	if (pl->speed < 15) PL_SetSpeed(pl, 15);
	PL_TrigJumpEffect(pl, NA_SE0_32, PL_JUMPVOICE);
	PL_SetAnime(pl, ANIME_77);
	switch (PL_ProcJump(pl, 1))
	{
	case JUMP_LAND:
		PL_SetState(pl, PS_WALK_30, 0);
		camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1);
		break;
	case JUMP_WALL:
		PL_SetSpeed(pl, 15);
		break;
	case JUMP_LEDGE:
#if REVISION >= 199609
		PL_SetAnime(pl, ANIME_51);
#endif
		PL_SetState(pl, PS_SPEC_0B, 0);
		camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	return FALSE;
}

static int PL_ExecJump23(PLAYER *pl)
{
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_JUMP_0C, 0);
	}
	if (pl->speed < 15) PL_SetSpeed(pl, 15);
	PL_TrigJumpEffect(pl, NA_SE0_32, PL_JUMPVOICE);
	PL_SetAnime(pl, ANIME_65);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		PL_SetState(pl, PS_WALK_34, 0);
		camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1);
		break;
	case JUMP_WALL:
		PL_SetSpeed(pl, 15);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	return FALSE;
}

static int PL_ExecJump05(PLAYER *pl)
{
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_JUMP_0A, 0);
	PL_TrigJumpEffect(pl, NA_SE0_00, PL_JUMPVOICE);
	PL_SetSpeed(pl, 0.98F*pl->speed);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		if (!pljump_8026A598(pl, PS_WALK_20))
		{
			pl->ang[0] = 0;
			PL_SetState(pl, pl->speed < 0 ? PS_WALK_10 : PS_WALK_30, 0);
		}
		break;
	case JUMP_WALL:
		PL_SetSpeed(pl, 0);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	PL_SetAnime(pl, ANIME_77);
	pl->obj->s.ang[1] = pl->obj->o_v7;
	return FALSE;
}

static int PL_ExecJump29(PLAYER *pl)
{
	int result;
	PL_TrigSound(pl, NA_SE0_35, PL_SOUND);
	if (pl->phase == 0)
	{
		if (pl->timer < 10)
		{
			float sp28 = 20 - 2*pl->timer;
			if (pl->pos[1]+sp28+160 < pl->roof_y)
			{
				pl->pos[1] += sp28;
				pl->peak = pl->pos[1];
				FVecCpy(pl->obj->s.pos, pl->pos);
			}
		}
		pl->vel[1] = -50;
		PL_SetSpeed(pl, 0);
		PL_SetAnime(pl, pl->code == 0 ? ANIME_60 : ANIME_59);
		if (pl->timer == 0) Na_ObjSePlay(NA_SE0_37, pl->obj);
		if (++pl->timer >= pl->obj->s.skel.anime->frame+4)
		{
			Na_ObjSePlay(NA_SE2_22, pl->obj);
			pl->phase = 1;
		}
	}
	else
	{
		PL_SetAnime(pl, ANIME_61);
		result = PL_ProcJump(pl, 0);
		if (result == JUMP_LAND)
		{
			if (pljump_8026A494(pl))
			{
#ifdef MOTOR
				motor_8024C834(5, 80);
#endif
				Na_ObjSePlay(NA_SE2_0B_D0, pl->obj);
				pl->effect |= PE_00010000;
				PL_SetState(pl, PS_DEMO_3B, 0);
			}
			else
			{
				PL_PlayFallEffect(pl, NA_SE0_60);
				if (!pljump_8026A224(pl, PS_WALK_20))
				{
					pl->effect |= PE_00000010|PE_00010000;
					PL_SetState(pl, PS_WAIT_3C, 0);
				}
			}
			camera_8027F590(2);
		}
		else if (result == JUMP_WALL)
		{
			PL_SetSpeed(pl, -16);
			if (pl->vel[1] > 0) pl->vel[1] = 0;
			pl->effect |= PE_00000002;
			PL_SetState(pl, PS_JUMP_30, 0);
		}
	}
	return FALSE;
}

static int PL_ExecJump34(PLAYER *pl)
{
	PL_TrigJumpEffect(
		pl, NA_SE0_00, pl->code == 0 ? PL_JUMPVOICE : PL_NULLVOICE
	);
	PL_SetSpeed(pl, pl->speed);
	if (PL_ProcJump(pl, 0) == JUMP_LAND)
	{
		PL_PlayLandEffect(pl, NA_SE0_08);
		PL_SetState(pl, PS_WALK_09, 0);
	}
	PL_SetAnime(pl, pl->code == 0 ? ANIME_77 : ANIME_41);
	pl->effect |= PE_00000800;
	Na_ObjSePlay(NA_SE1_10, pl->obj);
	pl->obj->o_v7 += 3;
	pl->power -= 10;
	if (pl->power < 0x100) pl->power = 0xFF;
#ifdef MOTOR
	motor_8024C924();
#endif
	return FALSE;
}

static int PL_ExecJump35(PLAYER *pl)
{
	PL_SetSpeed(pl, pl->speed);
	if (PL_ProcJump(pl, 0) == JUMP_LAND)
	{
		PL_PlayLandEffect(pl, NA_SE0_08);
		PL_SetState(pl, PS_WALK_09, 0);
	}
	PL_SetAnime(pl, ANIME_86);
	pl->effect |= PE_00000800;
	pl->obj->o_v7 += 3;
	pl->power -= 10;
	if (pl->power < 0x100) pl->power = 0xFF;
#ifdef MOTOR
	motor_8024C924();
#endif
	return FALSE;
}

static int PL_ExecJump2E(PLAYER *pl)
{
	if (pl->timer == 0)
	{
		float speed;
		switch (pl->code)
		{
		case 0: pl->vel[1] =  45; speed = 32; break;
		case 1: pl->vel[1] =  60; speed = 36; break;
		case 2: pl->vel[1] = 100; speed = 48; break;
#ifdef __GNUC__
		default: __builtin_unreachable();
#endif
		}
		Na_ObjSePlay(speed < 40 ? NA_SE3_6C : NA_SE3_6D_40, pl->obj);
		if (pl->speed < speed) PL_SetSpeed(pl, speed);
		pl->timer = 1;
	}
	PL_TrigJumpEffect(pl, NA_SE0_00, PL_JUMPVOICE);
	PL_SetAnime(pl, ANIME_136);
	pljump_8026AA48(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		if (pl->code < 2)
		{
			PL_SetState(pl, PS_JUMP_2E, pl->code+1);
		}
		else
		{
			pl->take->o_hit_result = HR_400000;
			pl->take = NULL;
			PL_SetState(pl, PS_WALK_13, 0);
		}
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		pl->effect |= PE_00010000;
		break;
	case JUMP_WALL:
		PL_Reflect(pl, FALSE);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	pl->obj->s.ang[0] = ATAN2(pl->speed, -pl->vel[1]);
	return FALSE;
}

static int pljump_8026D1B0(
	PLAYER *pl, u32 state1, u32 state2, int anime, float speed
)
{
	int result;
	PL_SetSpeed(pl, speed);
	result = PL_ProcJump(pl, 0);
	switch (result)
	{
	case JUMP_STAY:
		PL_SetAnime(pl, anime);
		break;
	case JUMP_LAND:
#ifdef MOTOR
		if (pl->state != PS_JUMP_36) motor_8024C834(5, 40);
#endif
		if (!pljump_8026A598(pl, state2))
		{
#if REVISION >= 199609
			if (pl->state == PS_JUMP_3D || pl->state == PS_JUMP_3E)
			{
				PL_SetState(pl, state1, pl->damage);
			}
			else
			{
				PL_SetState(pl, state1, pl->code);
			}
#else
			PL_SetState(pl, state1, pl->code);
#endif
		}
		break;
	case JUMP_WALL:
		PL_SetAnime(pl, ANIME_2);
		PL_Reflect(pl, FALSE);
		if (pl->vel[1] > 0) pl->vel[1] = 0;
		PL_SetSpeed(pl, -speed);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	return result;
}

static int pljump_8026D33C(PLAYER *pl)
{
	if (
		pl->status & PA_JUMPREQ && pl->wall_timer != 0 &&
		pl->prevstate == PS_JUMP_27
	)
	{
		pl->ang[1] += 0x8000;
		return PL_SetState(pl, PS_JUMP_06, 0);
	}
	return FALSE;
}

static int PL_ExecJump30(PLAYER *pl)
{
	if (pljump_8026D33C(pl)) return TRUE;
	pljump_8026A090(pl);
	pljump_8026D1B0(pl, PS_WALK_22, PS_WALK_20, ANIME_2, -16);
	return FALSE;
}

static int PL_ExecJump31(PLAYER *pl)
{
	if (pljump_8026D33C(pl)) return TRUE;
	pljump_8026A090(pl);
	pljump_8026D1B0(pl, PS_WALK_23, PS_WALK_21, ANIME_45, 16);
	return FALSE;
}

static int PL_ExecJump33(PLAYER *pl)
{
	pljump_8026A090(pl);
	pljump_8026D1B0(pl, PS_WALK_20, PS_WALK_20, ANIME_2, -16);
	return FALSE;
}

static int PL_ExecJump32(PLAYER *pl)
{
	pljump_8026A090(pl);
	pljump_8026D1B0(pl, PS_WALK_21, PS_WALK_21, ANIME_45, 16);
	return FALSE;
}

static int PL_ExecJump3E(PLAYER *pl)
{
	u32 state = pl->code ? PS_WALK_20 : PS_WALK_22;
	PL_TrigSound(pl, NA_SE2_10, PL_VOICE);
	pljump_8026D1B0(pl, state, PS_WALK_20, ANIME_2, pl->speed);
	pl->speed *= 0.98F;
	return FALSE;
}

static int PL_ExecJump3D(PLAYER *pl)
{
	SHORT angx;
	u32 state = pl->code ? PS_WALK_21 : PS_WALK_23;
	PL_TrigSound(pl, NA_SE2_10, PL_VOICE);
	if (!pljump_8026D1B0(pl, state, PS_WALK_21, ANIME_45, pl->speed))
	{
		angx = ATAN2(pl->speed, -pl->vel[1]);
		if (angx > 0x1800) angx = 0x1800;
		pl->obj->s.ang[0] = angx + 0x1800;
	}
	pl->speed *= 0.98F;
	return FALSE;
}

static int PL_ExecJump36(PLAYER *pl)
{
	if (pljump_8026D33C(pl)) return TRUE;
	pljump_8026A090(pl);
	pljump_8026D1B0(pl, PS_WALK_31, PS_WALK_20, ANIME_86, pl->speed);
	return FALSE;
}

static int PL_ExecJump38(PLAYER *pl)
{
	if (pl->phase == 0)
	{
		if (pl->speed > -60)    pl->speed -= 6;
		else                    pl->phase = 1;
	}
	else
	{
		if (pl->speed < -16) pl->speed += 0.8F;
		if (pl->vel[1] < 0 && pl->gravity < 4) pl->gravity += 0.05F;
	}
	if (++pl->timer == 20) PL_BlowCap(pl, 50);
	PL_SetSpeed(pl, pl->speed);
#if REVISION < 199609
	PL_TrigSound(pl, NA_SE2_05, PL_VOICE);
#endif
	PL_SetAnime(pl, ANIME_2);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		PL_SetState(pl, PS_JUMP_33, 0);
		break;
	case JUMP_WALL:
		PL_SetAnime(pl, ANIME_45);
		PL_Reflect(pl, FALSE);
		if (pl->vel[1] > 0) pl->vel[1] = 0;
		PL_SetSpeed(pl, -pl->speed);
		break;
	}
	return FALSE;
}

static int PL_ExecJump27(PLAYER *pl)
{
	if (pl->take) PL_DropObject(pl);
	if (++pl->timer < 3)
	{
		if (pl->status & PA_JUMPREQ)
		{
			pl->vel[1] = 52;
			pl->ang[1] += 0x8000;
			return PL_SetState(pl, PS_JUMP_06, 0);
		}
	}
	else
	{
		if (pl->speed >= 38)
		{
			pl->wall_timer = 5;
			if (pl->vel[1] > 0) pl->vel[1] = 0;
			pl->effect |= PE_00000002;
			return PL_SetState(pl, PS_JUMP_30, 0);
		}
		else
		{
			pl->wall_timer = 5;
			if (pl->vel[1] > 0) pl->vel[1] = 0;
			if (pl->speed > 8) PL_SetSpeed(pl, -8);
			return PL_SetState(pl, PS_JUMP_36, 0);
		}
	}
#ifdef sgi
	PL_SetAnime(pl, ANIME_204);
#else
	return PL_SetAnime(pl, ANIME_204);
#endif
}

static int PL_ExecJump26(PLAYER *pl)
{
	if (pl->phase == 0)
	{
		pl->vel[1] = 30;
		pl->phase = 1;
	}
	PL_TrigJumpEffect(pl, NA_SE0_00, PL_JUMPVOICE);
	pljump_8026AA48(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_STAY:
		if (pl->phase == 1)
		{
			if (PL_SetAnime(pl, ANIME_111) == 4)
			{
				Na_ObjSePlay(NA_SE0_37, pl->obj);
			}
		}
		else
		{
			PL_SetAnime(pl, ANIME_86);
		}
		break;
	case JUMP_LAND:
		PL_SetState(pl, PS_WAIT_32, 0);
		PL_PlayLandEffect(pl, NA_SE0_08);
		break;
	case JUMP_WALL:
		PL_SetSpeed(pl, 0);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	if (pl->phase == 1 && PL_IsAnimeLast2F(pl)) pl->phase = 2;
	return FALSE;
}

static int PL_ExecJump2D(PLAYER *pl)
{
	if (pl->phase == 0)
	{
		pl->vel[1] = 30;
		pl->phase = 1;
	}
	PL_TrigJumpEffect(pl, NA_SE0_00, PL_JUMPVOICE);
	pljump_8026AA48(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_STAY:
		if (pl->phase == 1)
		{
			if (PL_SetAnime(pl, ANIME_112) == 4)
			{
				Na_ObjSePlay(NA_SE0_37, pl->obj);
			}
		}
		else
		{
			PL_SetAnime(pl, ANIME_86);
		}
		break;
	case JUMP_LAND:
		PL_SetState(pl, PS_WAIT_32, 0);
		PL_PlayLandEffect(pl, NA_SE0_08);
		break;
	case JUMP_WALL:
		PL_SetSpeed(pl, 0);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	if (pl->phase == 1 && pl->obj->s.skel.frame == 2) pl->phase = 2;
	return FALSE;
}

static int PL_ExecJump0E(PLAYER *pl)
{
	if (++pl->timer > 30 && pl->pos[1]-pl->ground_y > 500)
	{
		return PL_SetState(pl, PS_JUMP_0C, 1);
	}
	pljump_8026A818(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		if (pl->phase == 0 && pl->vel[1] < 0 && pl->ground->ny >= COS_10)
		{
			pl->vel[1] = -pl->vel[1] / 2.0F;
			pl->phase = 1;
		}
		else
		{
			PL_SetState(pl, PS_WALK_12, 0);
		}
		PL_PlayLandEffect(pl, NA_SE0_08);
		break;
	case JUMP_WALL:
		if (pl->vel[1] > 0) pl->vel[1] = 0;
		pl->effect |= PE_00000002;
		PL_SetState(pl, PS_JUMP_30, 0);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	PL_SetAnime(pl, ANIME_145);
	return FALSE;
}

static int PL_ExecJump22(PLAYER *pl)
{
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_JUMP_21, 1);
	}
	if (++pl->timer > 30 && pl->pos[1]-pl->ground_y > 500)
	{
		return PL_SetState(pl, PS_JUMP_21, 1);
	}
	pljump_8026A818(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		if (pl->phase == 0 && pl->vel[1] < 0 && pl->ground->ny >= COS_10)
		{
			pl->vel[1] = -pl->vel[1] / 2.0F;
			pl->phase = 1;
		}
		else
		{
			PL_SetState(pl, PS_WALK_14, 0);
		}
		PL_PlayLandEffect(pl, NA_SE0_08);
		break;
	case JUMP_WALL:
		if (pl->vel[1] > 0) pl->vel[1] = 0;
		PL_DropObject(pl);
		pl->effect |= PE_00000002;
		PL_SetState(pl, PS_JUMP_30, 0);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	PL_SetAnime(pl, ANIME_69);
	return FALSE;
}

static int PL_ExecJump37(PLAYER *pl)
{
#ifdef MOTOR
	if (!(pl->flag & PL_VOICE))
	{
		PL_TrigSound(pl, NA_SE2_14, PL_VOICE);
		motor_8024C834(5, 80);
	}
#else
	PL_TrigSound(pl, NA_SE2_14, PL_VOICE);
#endif
	if (!(pl->status & PA_WALKREQ))
	{
		pl->speed = ConvergeF(pl->speed, 0, 0.35F, 0.35F);
	}
	pljump_8026ACD8(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		if (pl->ground->code == BG_1)
		{
			pl->phase = 0;
			if (!(pl->flag & PL_METALCAP)) PL_Damage(pl, 3);
			pl->vel[1] = 84;
			Na_ObjSePlay(NA_SE2_14, pl->obj);
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
		}
		else
		{
			PL_PlayFallEffect(pl, NA_SE0_18);
			if (pl->phase < 2 && pl->vel[1] < 0)
			{
				pl->vel[1] = -pl->vel[1] * 0.4F;
				PL_SetSpeed(pl, 0.5F*pl->speed);
				pl->phase++;
			}
			else
			{
				PL_SetState(pl, PS_WAIT_39, 0);
			}
		}
		break;
	case JUMP_WALL:
		PL_Reflect(pl, FALSE);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	PL_SetAnime(pl, ANIME_41);
	if (
		(pl->scene->env & ENV_MASK) != ENV_SNOW && !(pl->flag & PL_METALCAP) &&
		pl->vel[1] > 0
	)
	{
		pl->effect |= PE_00000800;
		if (pl->phase == 0) Na_ObjSePlay(NA_SE1_10, pl->obj);
	}
	if (pl->power < 0x100) PL_Fade(pl, FADE_DIE);
	pl->ctrl->eyes = 8;
#ifdef MOTOR
	motor_8024C924();
#endif
	return FALSE;
}

static int PL_ExecJump2A(PLAYER *pl)
{
	if (pl->phase == 0 && pl->timer == 0)
	{
		PL_TrigJumpEffect(pl, NA_SE0_00, NA_SE2_03);
		PL_SetAnime(pl, ANIME_140);
	}
	if (++pl->timer > 30 && pl->pos[1]-pl->ground_y > 500)
	{
		return PL_SetState(pl, PS_JUMP_0C, 2);
	}
	pljump_8026AA48(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_STAY:
		if (pl->phase == 0)
		{
			pl->obj->s.ang[0] = ATAN2(pl->speed, -pl->vel[1]);
			if (pl->obj->s.ang[0] > 0x1800) pl->obj->s.ang[0] = 0x1800;
		}
		break;
	case JUMP_LAND:
		if (pl->phase == 0 && pl->vel[1] < 0)
		{
			pl->vel[1] = -pl->vel[1] / 2.0F;
			pl->phase = 1;
			pl->timer = 0;
		}
		else
		{
			PL_SetState(pl, PS_WALK_1A, 0);
		}
		PL_PlayLandEffect(pl, NA_SE0_08);
		break;
	case JUMP_WALL:
		if (pl->vel[1] > 0) pl->vel[1] = 0;
		pl->effect |= PE_00000002;
		PL_SetState(pl, PS_JUMP_30, 0);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	return FALSE;
}

static int PL_ExecJump2C(PLAYER *pl)
{
	int frame;
	if (pl->phase == 0)
	{
		PL_TrigSound(pl, NA_SE2_1F, PL_SOUND);
		pl->obj->s.skel.index = -1;
		PL_SetAnime(pl, ANIME_79);
		pl->phase = 1;
	}
	frame = pl->obj->s.skel.frame;
	if (frame == 0) pl->ctrl->punch = 0x86;
	if (frame >= 0 && frame < 8) pl->flag |= PL_KICK;
	pljump_8026AA48(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		if (!pljump_8026A598(pl, PS_WALK_20)) PL_SetState(pl, PS_WALK_31, 0);
		break;
	case JUMP_WALL:
		PL_SetSpeed(pl, 0);
		break;
	}
	return FALSE;
}

static int PL_ExecJump18(PLAYER *pl)
{
	if (pl->scene->cam->mode != 3) pl->camera->demo = 2;
	PL_SetSpeed(pl, pl->speed);
	PL_TrigSound(pl, NA_SE2_04, PL_VOICE);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_STAY:
		PL_SetAnime(pl, ANIME_21);
		pl->ang[0] = ATAN2(pl->speed, pl->vel[1]);
		pl->obj->s.ang[0] = -pl->ang[0];
		break;
	case JUMP_LAND:
		PL_SetState(pl, PS_WALK_16, 0);
		pl->ang[0] = 0;
		camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1);
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		break;
	case JUMP_WALL:
		PL_SetSpeed(pl, -16);
		pl->ang[0] = 0;
		if (pl->vel[1] > 0) pl->vel[1] = 0;
		pl->effect |= PE_00000002;
		PL_SetState(pl, PS_JUMP_30, 0);
		camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	if (pl->flag & PL_WINGCAP && pl->vel[1] < 0) PL_SetState(pl, PS_JUMP_19, 0);
	if ((pl->speed -= 0.05) < 10) PL_SetSpeed(pl, 10);
	if (pl->vel[1] > 0) pl->effect |= PE_00000001;
#ifdef MOTOR
	motor_8024C924();
#endif
	return FALSE;
}

static int PL_ExecJump19(PLAYER *pl)
{
	SHORT angx = pl->ang[0];
	if (pl->status & PA_TRIGREQ)
	{
		if (pl->scene->cam->mode == 3)
		{
			camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1);
		}
		return PL_SetState(pl, PS_JUMP_29, 1);
	}
	if (!(pl->flag & PL_WINGCAP))
	{
		if (pl->scene->cam->mode == 3)
		{
			camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1);
		}
		return PL_SetState(pl, PS_JUMP_0C, 0);
	}
	if (pl->scene->cam->mode != 3) camera_80286188(pl->scene->cam, 3, 1);
	if (pl->phase == 0)
	{
		if (pl->code == 0)
		{
			PL_SetAnime(pl, ANIME_91);
		}
		else
		{
			PL_SetAnime(pl, ANIME_207);
			if (pl->obj->s.skel.frame == 1) Na_ObjSePlay(NA_SE0_37, pl->obj);
		}
		if (PL_IsAnimeLast1F(pl))
		{
			if (pl->code == 2)
			{
				GmInitMessage(0);
				pl->code = 1;
			}
			PL_SetAnime(pl, ANIME_42);
			pl->phase = 1;
		}
	}
	pljump_8026B17C(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_STAY:
		pl->obj->s.ang[0] = -pl->ang[0];
		pl->obj->s.ang[2] = pl->ang[2];
		pl->timer = 0;
		break;
	case JUMP_LAND:
		PL_SetState(pl, PS_WALK_16, 0);
		PL_SetAnime(pl, ANIME_136);
		PL_SetAnimeFrame(pl, 7);
		pl->ang[0] = 0;
		camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1);
#ifdef MOTOR
		motor_8024C834(5, 60);
#endif
		break;
	case JUMP_WALL:
		if (pl->wall)
		{
			PL_SetSpeed(pl, -16);
			pl->ang[0] = 0;
			if (pl->vel[1] > 0) pl->vel[1] = 0;
			Na_ObjSePlay(
				pl->flag & PL_METALCAP ? NA_SE0_42 : NA_SE0_45, pl->obj
			);
			pl->effect |= PE_00000002;
			PL_SetState(pl, PS_JUMP_30, 0);
			camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1);
		}
		else
		{
			if (pl->timer++ == 0) Na_ObjSePlay(NA_SE0_44_C0, pl->obj);
			if (pl->timer == 30) pl->timer = 0;
			pl->ang[0] -= 0x200;
			if (pl->ang[0] < DEG(-60)) pl->ang[0] = DEG(-60);
			pl->obj->s.ang[0] = -pl->ang[0];
			pl->obj->s.ang[2] = pl->ang[2];
		}
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	if (pl->ang[0] > 0x800 && pl->speed >= 48) pl->effect |= PE_00000001;
	if (angx <= 0 && pl->ang[0] > 0 && pl->speed >= 48)
	{
		Na_ObjSePlay(NA_SE0_56, pl->obj);
#if REVISION >= 199609
		Na_ObjSePlay(Na_Se2_2B(), pl->obj);
#endif
#ifdef MOTOR
		motor_8024C834(50, 40);
#endif
	}
	Na_ObjSePlay(NA_SE1_17, pl->obj);
	PL_SetSpeedEffect(pl);
	return FALSE;
}

static int PL_ExecJump28(PLAYER *pl)
{
	if (!(pl->status & PA_JUMPSTA) || pl->obj->o_hit_result & HR_000080)
	{
		pl->attach->o_hit_result = 0;
		pl->attach->o_v7 = gfx_frame;
		PL_TrigSound(pl, NA_SE2_05, PL_VOICE);
#ifdef MOTOR
		motor_8024C834(4, 40);
#endif
		return PL_SetState(pl, PS_JUMP_0C, 0);
	}
	pl->pos[0] = pl->attach->o_posx;
	pl->pos[1] = pl->attach->o_posy - 92.5F;
	pl->pos[2] = pl->attach->o_posz;
	pl->ang[1] = 0x4000 - pl->attach->o_angy;
	if (pl->phase == 0)
	{
		PL_SetAnime(pl, ANIME_53);
		if (PL_IsAnimeLast1F(pl))
		{
			PL_SetAnime(pl, ANIME_43);
			pl->phase = 1;
		}
	}
	FVecSet(pl->vel, 0, 0, 0);
	FVecSet(pl->obj->s.pos, pl->pos[0], pl->pos[1], pl->pos[2]);
	SVecSet(pl->obj->s.ang, 0, 0x4000-pl->ang[1], 0);
	return FALSE;
}

static int PL_ExecJump14(PLAYER *pl)
{
#if REVISION >= 199609
	if (pl->status & (PA_ATCKREQ|PA_TRIGREQ))
	{
		if (pl->scene->cam->mode == 3)
		{
			camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1);
		}
		if (pl->status & PA_ATCKREQ)    return PL_SetState(pl, PS_JUMP_0A, 0);
		else                            return PL_SetState(pl, PS_JUMP_29, 0);
	}
#else
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_JUMP_0A, 0);
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_JUMP_29, 0);
#endif
	PL_TrigJumpEffect(pl, NA_SE0_00, NA_SE2_04);
	if (pl->phase == 0)
	{
		PL_SetAnime(pl, ANIME_208);
		if (pl->obj->s.skel.frame == 7) Na_ObjSePlay(NA_SE0_37, pl->obj);
		if (PL_IsAnimeLast2F(pl))
		{
			PL_SetAnime(pl, ANIME_111);
#ifdef MOTOR
			motor_8024C834(8, 80);
#endif
			pl->phase = 1;
		}
	}
	if (pl->phase == 1 && pl->obj->s.skel.frame == 1)
	{
		Na_ObjSePlay(NA_SE0_37, pl->obj);
	}
	if (pl->vel[1] < 4)
	{
		if (pl->scene->cam->mode != 3) camera_80286188(pl->scene->cam, 3, 1);
		if (pl->speed < 32) PL_SetSpeed(pl, 32);
		PL_SetState(pl, PS_JUMP_19, 1);
	}
	if (pl->timer++ == 10)
	{
		if (pl->scene->cam->mode != 3) camera_80286188(pl->scene->cam, 3, 1);
	}
	pljump_8026AA48(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		if (!pljump_8026A598(pl, PS_WALK_20)) PL_SetState(pl, PS_WALK_32, 0);
		break;
	case JUMP_WALL:
		PL_Reflect(pl, FALSE);
		break;
	case JUMP_BURN:
		pljump_8026A12C(pl);
		break;
	}
	return FALSE;
}

static int PL_ExecJump0D(PLAYER *pl)
{
	PL_TrigJumpVoice(pl);
	pljump_8026B444(pl, PS_WALK_31, ANIME_10, 1);
	return FALSE;
}

static int PL_ExecJump1C(PLAYER *pl)
{
	SHORT dang = pl->stick_ang - pl->ang[1];
	float dist = pl->stick_dist / 32.0F;
	PL_TrigSound(pl, NA_SE2_0C, PL_VOICE);
	if (pl->phase == 0)
	{
		PL_SetAnime(pl, ANIME_207);
		if (pl->obj->s.skel.frame == 1)
		{
			Na_ObjSePlay(NA_SE0_37, pl->obj);
#ifdef MOTOR
			motor_8024C834(8, 80);
#endif
		}
		if (PL_IsAnimeLast2F(pl)) pl->phase = 1;
	}
	else
	{
		PL_SetAnime(pl, ANIME_21);
	}
	pljump_8026AA48(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		PL_SetState(pl, PS_WALK_16, 0);
		break;
	case JUMP_WALL:
		PL_SetSpeed(pl, -16);
		break;
	}
	pl->obj->s.ang[0] =  0x1800 * dist * COS(dang);
	pl->obj->s.ang[2] = -0x1000 * dist * SIN(dang);
	return FALSE;
}

static int PL_ExecJump2F(PLAYER *pl)
{
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_JUMP_0A, 0);
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_JUMP_29, 0);
	PL_TrigJumpEffect(pl, NA_SE0_00, NA_SE2_04);
	pljump_8026AA48(pl);
	switch (PL_ProcJump(pl, 0))
	{
	case JUMP_LAND:
		if (pl->phase++ == 0)   pl->vel[1] = 42;
		else                    PL_SetState(pl, PS_WAIT_32, 0);
		PL_PlayLandEffect(pl, NA_SE0_08);
		break;
	case JUMP_WALL:
		PL_Reflect(pl, TRUE);
		break;
	}
	if (pl->phase == 0 || pl->vel[1] > 0)
	{
		if (PL_SetAnime(pl, ANIME_111) == 0) Na_ObjSePlay(NA_SE0_37, pl->obj);
	}
	else
	{
		PL_SetAnime(pl, ANIME_86);
	}
	pl->effect |= PE_00000008;
	return FALSE;
}

static int pljump_8026FA18(PLAYER *pl)
{
	if (pl->pos[1] < pl->water-100) return PL_EnterWater(pl);
	if (pl->status & PA_PRESREQ) return PL_SetStateDrop(pl, PS_DEMO_39, 0);
	if (pl->ground->code == BG_56 && pl->state & PF_WIND)
	{
		return PL_SetStateDrop(pl, PS_JUMP_1C, 0);
	}
	pl->sink = 0;
	return FALSE;
}

int PL_ExecJump(PLAYER *pl)
{
	int result;
	if (pljump_8026FA18(pl)) return TRUE;
	pljump_80269FC0(pl);
	switch (pl->state)
	{
	case PS_JUMP_00: result = PL_ExecJump00(pl); break;
	case PS_JUMP_01: result = PL_ExecJump01(pl); break;
	case PS_JUMP_0C: result = PL_ExecJump0C(pl); break;
	case PS_JUMP_20: result = PL_ExecJump20(pl); break;
	case PS_JUMP_21: result = PL_ExecJump21(pl); break;
	case PS_JUMP_07: result = PL_ExecJump07(pl); break;
	case PS_JUMP_06: result = PL_ExecJump06(pl); break;
	case PS_JUMP_24: result = PL_ExecJump24(pl); break;
	case PS_JUMP_09: result = PL_ExecJump09(pl); break;
	case PS_JUMP_23: result = PL_ExecJump23(pl); break;
	case PS_JUMP_05: result = PL_ExecJump05(pl); break;
	case PS_JUMP_34: result = PL_ExecJump34(pl); break;
	case PS_JUMP_35: result = PL_ExecJump35(pl); break;
	case PS_JUMP_02: result = PL_ExecJump02(pl); break;
	case PS_JUMP_03: result = PL_ExecJump03(pl); break;
	case PS_JUMP_08: result = PL_ExecJump08(pl); break;
	case PS_JUMP_1A:
	case PS_JUMP_1B: result = PL_ExecJump1A_1B(pl); break;
	case PS_JUMP_0A: result = PL_ExecJump0A(pl); break;
	case PS_JUMP_2B: result = PL_ExecJump2B(pl); break;
	case PS_JUMP_30: result = PL_ExecJump30(pl); break;
	case PS_JUMP_31: result = PL_ExecJump31(pl); break;
	case PS_JUMP_32: result = PL_ExecJump32(pl); break;
	case PS_JUMP_33: result = PL_ExecJump33(pl); break;
	case PS_JUMP_36: result = PL_ExecJump36(pl); break;
	case PS_JUMP_27: result = PL_ExecJump27(pl); break;
	case PS_JUMP_26: result = PL_ExecJump26(pl); break;
	case PS_JUMP_18: result = PL_ExecJump18(pl); break;
	case PS_JUMP_0E: result = PL_ExecJump0E(pl); break;
	case PS_JUMP_22: result = PL_ExecJump22(pl); break;
	case PS_JUMP_37: result = PL_ExecJump37(pl); break;
	case PS_JUMP_38: result = PL_ExecJump38(pl); break;
	case PS_JUMP_2D: result = PL_ExecJump2D(pl); break;
	case PS_JUMP_2E: result = PL_ExecJump2E(pl); break;
	case PS_JUMP_2F: result = PL_ExecJump2F(pl); break;
	case PS_JUMP_29: result = PL_ExecJump29(pl); break;
	case PS_JUMP_3D: result = PL_ExecJump3D(pl); break;
	case PS_JUMP_3E: result = PL_ExecJump3E(pl); break;
	case PS_JUMP_14: result = PL_ExecJump14(pl); break;
	case PS_JUMP_2A: result = PL_ExecJump2A(pl); break;
	case PS_JUMP_2C: result = PL_ExecJump2C(pl); break;
	case PS_JUMP_19: result = PL_ExecJump19(pl); break;
	case PS_JUMP_28: result = PL_ExecJump28(pl); break;
	case PS_JUMP_0D: result = PL_ExecJump0D(pl); break;
	case PS_JUMP_1C: result = PL_ExecJump1C(pl); break;
	}
	return result;
}
