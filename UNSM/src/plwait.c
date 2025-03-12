#include <sm64.h>

static int plwait_802608B0(PLAYER *pl)
{
	PL_DropObject(pl);
	if (pl->ground->ny < COS_73) return PL_SteepFall(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetStateJump(pl, PS_JUMP_00, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	if (pl->status & PA_VIEWREQ) return PL_SetState(pl, PS_WAIT_27, 0);
	if (pl->status & PA_WALKREQ)
	{
		pl->ang[1] = pl->stick_ang;
		return PL_SetState(pl, PS_WALK_00, 0);
	}
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_00, 0);
	if (pl->status & PA_TRIGSTA) return PL_SetState(pl, PS_WAIT_21, 0);
	return FALSE;
}

static int plwait_80260AAC(PLAYER *pl)
{
	if (pl->ground->ny < COS_73) return PL_SteepFall(pl, PS_JUMP_21, 0);
	if (pl->take->o_hit_flag & HF_0040)
	{
		pl->take->o_hit_flag &= ~HF_0040;
		return PL_SetState(pl, PS_ATCK_07, 0);
	}
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetStateJump(pl, PS_JUMP_20, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_21, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_11, 0);
	if (pl->status & PA_WALKREQ)
	{
		pl->ang[1] = pl->stick_ang;
		return PL_SetState(pl, PS_WALK_02, 0);
	}
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_08, 0);
	if (pl->status & PA_TRIGSTA) return PL_SetStateDrop(pl, PS_WAIT_21, 0);
	return FALSE;
}

static int PL_ExecWait01(PLAYER *pl)
{
	if (pl->sink > 30) return PL_SetState(pl, PS_WAIT_0D, 0);
	if (pl->status & PA_GAS) return PL_SetState(pl, PS_WAIT_0A, 0);
	if (!(pl->code & 1) && pl->power < 0x300)
	{
		return PL_SetState(pl, PS_WAIT_05, 0);
	}
	if (plwait_802608B0(pl)) return TRUE;
	if (pl->phase == 3)
	{
		if ((pl->scene->env & ENV_MASK) == ENV_SNOW)
		{
			return PL_SetState(pl, PS_WAIT_0B, 0);
		}
		else
		{
			return PL_SetState(pl, PS_WAIT_02, 0);
		}
	}
	if (pl->code & 1)
	{
		PL_SetAnime(pl, ANIME_126);
	}
	else
	{
		switch (pl->phase)
		{
		case 0: PL_SetAnime(pl, ANIME_195); break;
		case 1: PL_SetAnime(pl, ANIME_196); break;
		case 2: PL_SetAnime(pl, ANIME_197); break;
		}
		if (PL_IsAnimeLast1F(pl) && ++pl->phase == 3)
		{
			float height = pl->pos[1] - PL_CheckGroundYNear(pl, -0x8000, 60);
			if (height < -24 || 24 < height || pl->ground->flag & 1)
			{
				pl->phase = 0;
			}
			else
			{
				if (++pl->timer < 10) pl->phase = 0;
			}
		}
	}
	PL_ProcWait(pl);
	return FALSE;
}

static void plwait_80260F94(PLAYER *pl, int phase, int frame, Na_Se se)
{
	if (pl->phase == phase && pl->obj->s.skel.frame == frame)
	{
		Na_ObjSePlay(se, pl->obj);
	}
}

static int PL_ExecWait02(PLAYER *pl)
{
#if REVISION >= 199609
	int frame;
#endif
	if (plwait_802608B0(pl)) return TRUE;
	if (pl->sink > 30) return PL_SetState(pl, PS_WAIT_0D, 0);
	if (pl->phase == 4) return PL_SetState(pl, PS_WAIT_03, 0);
	switch (pl->phase)
	{
#if REVISION >= 199609
	case 0: frame = PL_SetAnime(pl, ANIME_129); break;
	case 1: frame = PL_SetAnime(pl, ANIME_130); break;
	case 2: frame = PL_SetAnime(pl, ANIME_131); pl->ctrl->eyes = 2; break;
	case 3: frame = PL_SetAnime(pl, ANIME_132); pl->ctrl->eyes = 2; break;
#else
	case 0: PL_SetAnime(pl, ANIME_129); break;
	case 1: PL_SetAnime(pl, ANIME_130); break;
	case 2: PL_SetAnime(pl, ANIME_131); pl->ctrl->eyes = 2; break;
	case 3: PL_SetAnime(pl, ANIME_132); pl->ctrl->eyes = 2; break;
#endif
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
	plwait_80260F94(pl, 1, 41, NA_SE0_3F);
	plwait_80260F94(pl, 1, 49, NA_SE0_3F);
	plwait_80260F94(pl, 3, 15, NA_SE0_18 + pl->surface);
	if (PL_IsAnimeLast1F(pl)) pl->phase++;
#if REVISION >= 199609
	if (pl->phase == 2 && frame == -1) Na_ObjSePlay(NA_SE2_0D, pl->obj);
	if (pl->phase == 1 && frame == -1) Na_ObjSePlay(NA_SE2_37, pl->obj);
#else
	if (pl->phase == 2) PL_TrigSound(pl, NA_SE2_0D, PL_VOICE);
#endif
	PL_ProcWait(pl);
	return FALSE;
}

static int PL_ExecWait03(PLAYER *pl)
{
	int frame;
	if (pl->status & PA_ACTION)
	{
		return PL_SetState(pl, PS_WAIT_04, pl->phase);
	}
	if (pl->sink > 30) return PL_SetState(pl, PS_WAIT_04, pl->phase);
	if (pl->pos[1]-PL_CheckGroundYNear(pl, -0x8000, 60) > 24)
	{
		return PL_SetState(pl, PS_WAIT_04, pl->phase);
	}
	pl->ctrl->eyes = 3;
	PL_ProcWait(pl);
	switch (pl->phase)
	{
	case 0:
		frame = PL_SetAnime(pl, ANIME_133);
		if (frame == -1 && pl->timer == 0) AudSetMute(AUD_QUIET);
		if (frame == 2) Na_ObjSePlay(NA_SE2_0E, pl->obj);
		if (frame == 20) Na_ObjSePlay(NA_SE2_0F, pl->obj);
		if (PL_IsAnimeLast1F(pl) && ++pl->timer > 45) pl->phase++;
		break;
	case 1:
		if (PL_SetAnime(pl, ANIME_134) == 18) PL_PlayFallEffect(pl, NA_SE0_18);
		if (PL_IsAnimeLast1F(pl)) pl->phase++;
		break;
	case 2:
		frame = PL_SetAnime(pl, ANIME_135);
#if REVISION >= 199609
		PL_TrigSound(pl, NA_SE2_35, PL_SOUND);
#else
		if (frame == 2) Na_ObjSePlay(NA_SE2_0F, pl->obj);
		if (frame == 25) Na_ObjSePlay(NA_SE2_0E, pl->obj);
#endif
		break;
	}
	return FALSE;
}

static int PL_ExecWait04(PLAYER *pl)
{
	if (pl->timer == 0)
	{
		Na_SeStop(NA_SE2_0E, pl->obj->s.view);
		Na_SeStop(NA_SE2_0F, pl->obj->s.view);
#if REVISION >= 199609
		Na_SeStop(NA_SE2_35, pl->obj->s.view);
#endif
		AudClrMute(AUD_QUIET);
	}
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	pl->timer++;
	if (pl->timer > 20) return PL_SetState(pl, PS_WAIT_01, 0);
	PL_ProcWait(pl);
	PL_SetAnime(pl, pl->code == 0 ? ANIME_200 : ANIME_201);
	return FALSE;
}

static int PL_ExecWait0B(PLAYER *pl)
{
	int frame;
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	if (pl->status & PA_ACTION) pl->phase = 2;
	PL_ProcWait(pl);
	switch (pl->phase)
	{
	case 0:
		frame = PL_SetAnime(pl, ANIME_25);
		if (frame == 49)
		{
			pl->effect |= PE_00020000;
			Na_ObjSePlay(NA_SE2_16, pl->obj);
		}
		if (frame == 7 || frame == 81) Na_ObjSePlay(NA_SE0_2C, pl->obj);
		if (PL_IsAnimeLast2F(pl)) pl->phase = 1;
		break;
	case 1:
		frame = PL_SetAnime(pl, ANIME_27);
		if (frame == 9 || frame == 25 || frame == 44)
		{
			Na_ObjSePlay(NA_SE0_2C, pl->obj);
		}
		break;
	case 2:
		PL_SetAnime(pl, ANIME_26);
		if (PL_IsAnimeLast2F(pl)) PL_SetState(pl, PS_WAIT_01, 0);
		break;
	}
	return FALSE;
}

static int PL_ExecWait0A(PLAYER *pl)
{
	int frame;
	if (plwait_802608B0(pl)) return TRUE;
	PL_ProcWait(pl);
	frame = PL_SetAnime(pl, ANIME_48);
	if (frame == 25 || frame == 35) Na_ObjSePlay(NA_SE2_1D, pl->obj);
	if (frame == 50 || frame == 58) Na_ObjSePlay(NA_SE2_1C, pl->obj);
	if (frame == 71 || frame == 80) Na_ObjSePlay(NA_SE2_1B, pl->obj);
	return FALSE;
}

extern OBJLANG obj_13001650[];

static int PL_ExecWait07(PLAYER *pl)
{
	if (pl->take->script == SegmentToVirtual(obj_13001650))
	{
		return PL_SetState(pl, PS_JUMP_2E, 0);
	}
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_WAIT_01, 0);
	}
	if (pl->sink > 30) return PL_SetStateDrop(pl, PS_WAIT_0D, 0);
	if (plwait_80260AAC(pl)) return TRUE;
	PL_ProcWait(pl);
	PL_SetAnime(pl, ANIME_63);
	return FALSE;
}

static int PL_ExecWait08(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetStateDrop(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetStateDrop(pl, PS_WALK_10, 0);
	if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_WALK_07, 0);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_09, 0);
	PL_ProcWait(pl);
	PL_SetAnime(pl, ANIME_125);
	return FALSE;
}

static int PL_ExecWait09(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_MOTION) return PL_CheckMotion(pl);
	if (pl->status & PA_VIEWREQ) return PL_SetState(pl, PS_WAIT_27, 0);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_00, 0);
	PL_SetAnime(pl, ANIME_126);
	PL_ProcWait(pl);
	return FALSE;
}

static int PL_ExecWait0D(PLAYER *pl)
{
	if (pl->sink < 30) return PL_SetState(pl, PS_WAIT_01, 0);
	if (plwait_802608B0(pl)) return TRUE;
	if (pl->sink > 70)  PL_SetAnime(pl, ANIME_118);
	else                PL_SetAnime(pl, ANIME_119);
	PL_ProcWait(pl);
	return FALSE;
}

static int PL_ExecWait20(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetStateJump(pl, PS_JUMP_03, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	if (pl->status & PA_VIEWREQ) return PL_SetState(pl, PS_WAIT_22, 0);
	if (!(pl->status & PA_TRIGSTA)) return PL_SetState(pl, PS_WAIT_22, 0);
	if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_WAIT_23, 0);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_00, 9);
	PL_ProcWait(pl);
	PL_SetAnime(pl, ANIME_152);
	return FALSE;
}

static int PL_ExecWait05(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->power >= 0x500) return PL_SetState(pl, PS_WAIT_01, 0);
	if (plwait_802608B0(pl)) return TRUE;
	if (PL_SetAnime(pl, ANIME_186) == 1) Na_ObjSePlay(Na_Se2_18(), pl->obj);
	PL_ProcWait(pl);
	pl->ctrl->eyes = 2;
	return FALSE;
}

static int PL_ExecWait06(PLAYER *pl)
{
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_WAIT_05, 0);
	}
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->power >= 0x500) return PL_SetState(pl, PS_WAIT_07, 0);
	if (plwait_80260AAC(pl)) return TRUE;
	PL_SetAnime(pl, ANIME_186);
	PL_ProcWait(pl);
	pl->ctrl->eyes = 2;
	return FALSE;
}

static void plwait_8026217C(PLAYER *pl, int anime, u32 state)
{
	PL_ProcWait(pl);
	PL_SetAnime(pl, anime);
	if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, state, 0);
}

static int PL_ExecWait3D(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_00, 0);
	if (!(pl->status & PA_VIEWREQ) && pl->status & PA_MOTION)
	{
		return PL_CheckMotion(pl);
	}
	plwait_8026217C(pl, ANIME_16, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecWait3E(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_MOTION) return PL_CheckMotion(pl);
	plwait_8026217C(pl, ANIME_143, PS_WAIT_01);
	if (pl->obj->s.skel.frame == 6) PL_PlayLandEffect(pl, NA_SE0_08);
	return FALSE;
}

static int PL_ExecWait3F(PLAYER *pl)
{
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_WAIT_01, 0);
	}
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_MOTION) return PL_CheckMotionTake(pl);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_08, 0);
	plwait_8026217C(pl, ANIME_70, PS_WAIT_07);
	return FALSE;
}

static int PL_ExecWait25(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetStateDrop(pl, PS_JUMP_0C, 0);
	plwait_8026217C(pl, ANIME_141, PS_WAIT_20);
	return FALSE;
}

static int PL_ExecWait21(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetStateJump(pl, PS_JUMP_03, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	PL_ProcWait(pl);
	PL_SetAnime(pl, ANIME_151);
	if (PL_IsAnimeLast2F(pl)) PL_SetState(pl, PS_WAIT_20, 0);
	return FALSE;
}

static int PL_ExecWait22(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_JUMPREQ) return PL_SetStateJump(pl, PS_JUMP_03, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	PL_ProcWait(pl);
	PL_SetAnime(pl, ANIME_150);
	if (PL_IsAnimeLast2F(pl)) PL_SetState(pl, PS_WAIT_01, 0);
	return FALSE;
}

static int PL_ExecWait23(PLAYER *pl)
{
	if (pl->status & PA_VIEWREQ) return PL_SetState(pl, PS_WAIT_22, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	PL_ProcWait(pl);
	PL_SetAnime(pl, ANIME_155);
	if (PL_IsAnimeLast2F(pl)) PL_SetState(pl, PS_WALK_08, 0);
	return FALSE;
}

static int PL_ExecWait24(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	PL_ProcWait(pl);
	PL_SetAnime(pl, ANIME_154);
	if (PL_IsAnimeLast2F(pl)) PL_SetState(pl, PS_WAIT_20, 0);
	return FALSE;
}

static int PL_ExecWait26(PLAYER *pl)
{
	SHORT theta;
	float dist;
	if (pl->obj->o_hit_result & HR_000010)
	{
#ifdef MOTOR
		motor_8024C834(70, 40);
#endif
		return PL_SetStateDamage(pl, PS_DEMO_38, 0, 4);
	}
	if (pl->timer == 0)
	{
#ifdef MOTOR
		motor_8024C834(70, 40);
#endif
		if (pl->obj->o_hit_result & HR_000002)
		{
			return PL_SetStateDamage(pl, PS_WALK_22, 0, 12);
		}
	}
	if (++pl->timer == 48) return PL_SetState(pl, PS_WAIT_01, 0);
	theta = 0x1000*(pl->timer % 16);
	dist = 4 + (float)8*(6 - pl->timer/8);
	PL_SetSpeed(pl, 0);
	FVecSet(pl->vel, 0, 0, 0);
	if (SIN(theta) >= 0)    pl->pos[1] = pl->ground_y + dist*SIN(theta);
	else                    pl->pos[1] = pl->ground_y - dist*SIN(theta);
	FVecCpy(pl->obj->s.pos, pl->pos);
	SVecSet(pl->obj->s.ang, 0, pl->ang[1], 0);
	PL_SetAnime(pl, ANIME_14);
	return FALSE;
}

static int plwait_80262BC4(PLAYER *pl, int anime, u32 state)
{
	PL_ProcWait(pl);
	PL_SetAnime(pl, anime);
	if (PL_IsAnimeLast1F(pl)) return PL_SetState(pl, state, 0);
	return FALSE;
}

static int plwait_80262C34(PLAYER *pl, u32 state)
{
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_VIEWREQ) return PL_SetState(pl, PS_WAIT_01, 0);
	if (pl->status & PA_JUMPREQ)
	{
		if (!state) return PL_SetTripJump(pl);
		else        return PL_SetStateJump(pl, state, 0);
	}
	if (pl->status & PA_MOTION) return PL_CheckMotion(pl);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_00, 0);
	return FALSE;
}

static int PL_ExecWait30(PLAYER *pl)
{
	if (plwait_80262C34(pl, PS_NULL)) return TRUE;
	plwait_80262BC4(pl, ANIME_78, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecWait31(PLAYER *pl)
{
	if (plwait_80262C34(pl, PS_NULL)) return TRUE;
	plwait_80262BC4(pl, ANIME_75, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecWait33(PLAYER *pl)
{
	if (plwait_80262C34(pl, PS_NULL)) return TRUE;
	plwait_80262BC4(pl, ANIME_190, PS_WAIT_01);
	pl->obj->s.ang[1] += 0x8000;
	return FALSE;
}

static int PL_ExecWait32(PLAYER *pl)
{
	if (plwait_80262C34(pl, PS_NULL)) return TRUE;
	plwait_80262BC4(pl, ANIME_87, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecWait3A(PLAYER *pl)
{
	if (plwait_80262C34(pl, PS_JUMP_00)) return TRUE;
	plwait_80262BC4(pl, ANIME_192, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecWait2F(PLAYER *pl)
{
	if (!(pl->status & PA_TRIGSTA) || pl->obj->s.skel.frame > 5)
	{
		pl->status &= ~PA_JUMPREQ;
	}
	if (plwait_80262C34(pl, PS_JUMP_03)) return TRUE;
	plwait_80262BC4(pl, ANIME_192, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecWait39(PLAYER *pl)
{
	pl->status &= ~(PA_VIEWREQ|PA_ATCKREQ);
	if (plwait_80262C34(pl, PS_NULL)) return TRUE;
	plwait_80262BC4(pl, ANIME_40, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecWait3B(PLAYER *pl)
{
	pl->status &= ~PA_ATCKREQ;
	if (plwait_80262C34(pl, PS_JUMP_00)) return TRUE;
	plwait_80262BC4(pl, pl->obj->o_v7 == 0 ? ANIME_17 : ANIME_18, PS_WAIT_20);
	return FALSE;
}

static int PL_ExecWait34(PLAYER *pl)
{
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_WAIT_01, 0);
	}
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_MOTION) return PL_CheckMotionTake(pl);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_08, 0);
	plwait_80262BC4(pl, ANIME_64, PS_WAIT_07);
	return FALSE;
}

static int PL_ExecWait35(PLAYER *pl)
{
	if (pl->obj->o_hit_result & HR_000008)
	{
		return PL_SetStateDrop(pl, PS_WAIT_01, 0);
	}
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_MOTION) return PL_CheckMotionTake(pl);
	if (pl->status & PA_ATCKREQ) return PL_SetState(pl, PS_ATCK_08, 0);
	plwait_80262BC4(pl, ANIME_66, PS_WAIT_07);
	return FALSE;
}

static int PL_ExecWait36(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (++pl->timer == 4) PL_ThrowObject(pl);
	plwait_80262BC4(pl, ANIME_82, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecWait38(PLAYER *pl)
{
	pl->phase = 1;
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	PL_ProcWait(pl);
	PL_SetAnime(pl, ANIME_147);
	if (pl->rot[1] > 0)
	{
		pl->rot[1] -= 0x400;
		if (pl->rot[1] < 0) pl->rot[1] = 0;
		pl->spin_ang += pl->rot[1];
	}
	pl->obj->s.ang[1] += pl->spin_ang;
	if (PL_IsAnimeLast1F(pl))
	{
		if (pl->rot[1] == 0)
		{
			pl->ang[1] += pl->spin_ang;
			PL_SetState(pl, PS_WAIT_01, 0);
		}
	}
	return FALSE;
}

static int PL_ExecWait3C(PLAYER *pl)
{
	pl->phase = 1;
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_12, 0);
	plwait_80262BC4(pl, ANIME_58, PS_WAIT_3E);
	return FALSE;
}

static int PL_ExecWait27(PLAYER *pl)
{
	int action = (pl->status & (PA_LANDREQ|PA_SLIPREQ|PA_HIT)) != 0;
	if (pl->phase == 0)
	{
		AudSetMute(AUD_QUIET);
		camera_80286188(pl->scene->cam, 6, 16);
		pl->phase = 1;
	}
	else
	{
		if (!(pl->status & PA_VIEWREQ) || action)
		{
			AudClrMute(AUD_QUIET);
			camera_80286188(pl->scene->cam, -1, 1);
			return PL_SetState(pl, PS_WAIT_01, 0);
		}
	}
	if (pl->ground->code == BG_47 && BuStarTotal() >= 10)
	{
		SHORT angx = pl->camera->neck_angx;
		short angy = pl->ang[1] + pl->camera->neck_angy*4/3;
		if (angx == -0x1800 && (angy <= -0x7000 || 0x7000 <= angy))
		{
			PL_Fade(pl, FADE_ROOF);
		}
	}
	PL_ProcWait(pl);
	PL_SetAnime(pl, ANIME_194);
	return FALSE;
}

static int plwait_80263784(PLAYER *pl)
{
	if (pl->pos[1] < pl->water-100)
	{
		if (pl->state == PS_DEMO_25) GmInitMessage(0);
		player_802521A0(pl);
		return PL_EnterWater(pl);
	}
	if (pl->status & PA_PRESREQ)
	{
		player_802521A0(pl);
		return PL_SetStateDrop(pl, PS_DEMO_39, 0);
	}
	if (pl->state != PS_WAIT_0E)
	{
		if (pl->power < 0x100)
		{
			player_802521A0(pl);
			return PL_SetStateDrop(pl, PS_DEMO_11, 0);
		}
	}
	return FALSE;
}

int PL_ExecWait(PLAYER *pl)
{
	int result;
	if (plwait_80263784(pl)) return TRUE;
	if (PL_ProcSink(pl, 0.5F)) return TRUE;
	switch (pl->state)
	{
	case PS_WAIT_01: result = PL_ExecWait01(pl); break;
	case PS_WAIT_02: result = PL_ExecWait02(pl); break;
	case PS_WAIT_03: result = PL_ExecWait03(pl); break;
	case PS_WAIT_04: result = PL_ExecWait04(pl); break;
	case PS_WAIT_05: result = PL_ExecWait05(pl); break;
	case PS_WAIT_06: result = PL_ExecWait06(pl); break;
	case PS_WAIT_07: result = PL_ExecWait07(pl); break;
	case PS_WAIT_08: result = PL_ExecWait08(pl); break;
	case PS_WAIT_0D: result = PL_ExecWait0D(pl); break;
	case PS_WAIT_09: result = PL_ExecWait09(pl); break;
	case PS_WAIT_0A: result = PL_ExecWait0A(pl); break;
	case PS_WAIT_0B: result = PL_ExecWait0B(pl); break;
	/* case PS_WAIT_0E: break; */
	case PS_WAIT_20: result = PL_ExecWait20(pl); break;
	case PS_WAIT_21: result = PL_ExecWait21(pl); break;
	case PS_WAIT_22: result = PL_ExecWait22(pl); break;
	case PS_WAIT_23: result = PL_ExecWait23(pl); break;
	case PS_WAIT_24: result = PL_ExecWait24(pl); break;
	case PS_WAIT_25: result = PL_ExecWait25(pl); break;
	case PS_WAIT_26: result = PL_ExecWait26(pl); break;
	case PS_WAIT_27: result = PL_ExecWait27(pl); break;
	case PS_WAIT_30: result = PL_ExecWait30(pl); break;
	case PS_WAIT_31: result = PL_ExecWait31(pl); break;
	case PS_WAIT_32: result = PL_ExecWait32(pl); break;
	case PS_WAIT_33: result = PL_ExecWait33(pl); break;
	case PS_WAIT_34: result = PL_ExecWait34(pl); break;
	case PS_WAIT_35: result = PL_ExecWait35(pl); break;
	case PS_WAIT_36: result = PL_ExecWait36(pl); break;
	case PS_WAIT_39: result = PL_ExecWait39(pl); break;
	case PS_WAIT_38: result = PL_ExecWait38(pl); break;
	case PS_WAIT_3A: result = PL_ExecWait3A(pl); break;
	case PS_WAIT_2F: result = PL_ExecWait2F(pl); break;
	case PS_WAIT_3B: result = PL_ExecWait3B(pl); break;
	case PS_WAIT_3C: result = PL_ExecWait3C(pl); break;
	case PS_WAIT_3D: result = PL_ExecWait3D(pl); break;
	case PS_WAIT_3E: result = PL_ExecWait3E(pl); break;
	case PS_WAIT_3F: result = PL_ExecWait3F(pl); break;
	}
	if (!result)
	{
		if (pl->status & PA_WADING) pl->effect |= PE_00000080;
	}
	return result;
}
