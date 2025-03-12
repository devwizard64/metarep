#include <sm64.h>

static void platck_80274EB0(PLAYER *pl, int anime, u32 state)
{
	PL_ProcWait(pl);
	PL_SetAnime(pl, anime);
	if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, state, 0);
}

int platck_80274F10(PLAYER *pl)
{
	u32 sp24, sp20;
	int frame;
	if (pl->state & PF_WALK)    sp24 = PS_WALK_00, sp20 = PS_WALK_19;
	else                        sp24 = PS_WAIT_01, sp20 = PS_WAIT_20;
	switch (pl->code)
	{
	case 0:
		Na_ObjSePlay(NA_SE2_1E, pl->obj);
		FALLTHROUGH;
	case 1:
		PL_SetAnime(pl, ANIME_103);
		if (PL_IsAnimeLast2F(pl))   pl->code = 2;
		else                        pl->code = 1;
		if (pl->obj->s.skel.frame > 1)
		{
			if (PL_CheckTaking(pl)) return TRUE;
			pl->flag |= PL_PUNCH;
		}
		if (pl->code == 2) pl->ctrl->punch = 0x04;
		break;
	case 2:
		PL_SetAnime(pl, ANIME_105);
		if (pl->obj->s.skel.frame <= 0) pl->flag |= PL_PUNCH;
		if (pl->status & PA_ATCKREQ) pl->code = 3;
		if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, sp24, 0);
		break;
	case 3:
		Na_ObjSePlay(NA_SE2_24, pl->obj);
		FALLTHROUGH;
	case 4:
		PL_SetAnime(pl, ANIME_104);
		if (PL_IsAnimeLast2F(pl))   pl->code = 5;
		else                        pl->code = 4;
		if (pl->obj->s.skel.frame > 0) pl->flag |= PL_PUNCH;
		if (pl->code == 5) pl->ctrl->punch = 0x44;
		break;
	case 5:
		PL_SetAnime(pl, ANIME_106);
		if (pl->obj->s.skel.frame <= 0) pl->flag |= PL_PUNCH;
		if (pl->status & PA_ATCKREQ) pl->code = 6;
		if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, sp24, 0);
		break;
	case 6:
		PL_TrigEffect(pl, NA_SE2_1F, 1);
		frame = PL_SetAnime(pl, ANIME_102);
		if (frame == 0) pl->ctrl->punch = 0x86;
		if (frame >= 0 && frame < 8) pl->flag |= PL_KICK;
		if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, sp24, 0);
		break;
	case 9:
		PL_TrigEffect(pl, NA_SE2_1F, 1);
		PL_SetAnime(pl, ANIME_113);
		frame = pl->obj->s.skel.frame;
		if (frame >= 2 && frame < 8) pl->flag |= PL_SWEEPKICK;
		if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, sp20, 0);
		break;
	}
	return FALSE;
}

static int PL_ExecAtck00(PLAYER *pl)
{
	static char speedtab[] = {0, 1, 1, 2, 3, 5, 7, 10};
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_MOTION) return PL_CheckMotion(pl);
	if (pl->phase == 0 && pl->status & PA_JUMPSTA)
	{
		return PL_SetState(pl, PS_JUMP_2C, 0);
	}
	pl->phase = 1;
	if (pl->code == 0) pl->timer = 7;
	PL_SetSpeed(pl, speedtab[pl->timer]);
	if (pl->timer > 0) pl->timer--;
	platck_80274F10(pl);
	PL_ProcWalk(pl);
	return FALSE;
}

static int PL_ExecAtck03(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetStateDrop(pl, PS_JUMP_0C, 0);
	if (pl->phase == 0 && PL_IsAnimeLast1F(pl))
	{
		PL_TakeObject(pl);
		PL_TrigSound(pl, NA_SE2_06, PL_VOICE);
		pl->phase = 1;
	}
	if (pl->phase == 1)
	{
		if (pl->take->o_hit_flag & HF_0004)
		{
			pl->ctrl->take = 2;
			PL_SetAnime(pl, ANIME_89);
			if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, PS_WAIT_08, 0);
		}
		else
		{
			pl->ctrl->take = 1;
			PL_SetAnime(pl, ANIME_107);
			if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, PS_WAIT_07, 0);
		}
	}
	PL_ProcWait(pl);
	return FALSE;
}

static int PL_ExecAtck05(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	platck_80274EB0(pl, ANIME_139, PS_WAIT_07);
	return FALSE;
}

static int PL_ExecAtck07(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetStateDrop(pl, PS_JUMP_0C, 0);
	if (++pl->timer == 8) PL_DropObject(pl);
	platck_80274EB0(pl, ANIME_110, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecAtck08(PLAYER *pl)
{
	if (pl->take && pl->take->o_hit_flag & HF_0010)
	{
		return PL_SetState(pl, PS_ATCK_07, 0);
	}
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetStateDrop(pl, PS_JUMP_0C, 0);
	if (++pl->timer == 7)
	{
		PL_ThrowObject(pl);
		PL_TrigSound(pl, NA_SE2_07, PL_VOICE);
		PL_TrigSound(pl, NA_SE0_35, PL_SOUND);
#ifdef MOTOR
		motor_8024C834(3, 50);
#endif
	}
	platck_80274EB0(pl, ANIME_101, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecAtck09(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetStateDrop(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetStateDrop(pl, PS_JUMP_0C, 0);
	if (++pl->timer == 13)
	{
		PL_DropObject(pl);
		PL_TrigSound(pl, NA_SE2_07, PL_VOICE);
		PL_TrigSound(pl, NA_SE0_35, PL_SOUND);
#ifdef MOTOR
		motor_8024C834(3, 50);
#endif
	}
	platck_80274EB0(pl, ANIME_185, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecAtck06(PLAYER *pl)
{
	if (pl->status & PA_HIT) return PL_SetState(pl, PS_WAIT_26, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	platck_80274EB0(pl, ANIME_90, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecAtck10(PLAYER *pl)
{
	if (pl->phase == 0)
	{
		pl->phase = 1;
		pl->rot[1] = 0;
		pl->ctrl->take = 3;
		PL_TakeObject(pl);
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		Na_ObjSePlay(NA_SE2_06, pl->obj);
	}
	PL_SetAnime(pl, ANIME_181);
	if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, PS_ATCK_11, 0);
	PL_ProcWait(pl);
	return FALSE;
}

static int PL_ExecAtck11(PLAYER *pl)
{
	SHORT ang;
	if (pl->status & PA_ATCKREQ)
	{
#if REVISION >= 199609
		if (-0xE00 >= pl->rot[1] || pl->rot[1] >= 0xE00)
		{
			Na_ObjSePlay(NA_SE2_36, pl->obj);
		}
		else
		{
			Na_ObjSePlay(NA_SE2_0C, pl->obj);
		}
#else
		Na_ObjSePlay(NA_SE2_0C, pl->obj);
#endif
		return PL_SetState(pl, PS_ATCK_12, 0);
	}
	if (pl->rot[1] == 0)
	{
		if (pl->timer++ > 120) return PL_SetState(pl, PS_ATCK_12, 1);
		PL_SetAnime(pl, ANIME_184);
	}
	else
	{
		pl->timer = 0;
		PL_SetAnime(pl, ANIME_182);
	}
	if (pl->stick_dist > 20)
	{
		if (pl->code == 0)
		{
			pl->code = 1;
			pl->spin_ang = pl->stick_ang;
		}
		else
		{
			ang = (short)(pl->stick_ang-pl->spin_ang) / 0x80;
			if (ang < -0x80) ang = -0x80;
			if (ang > +0x80) ang = +0x80;
			pl->spin_ang = pl->stick_ang;
			pl->rot[1] += ang;
			if (pl->rot[1] > +0x1000) pl->rot[1] = +0x1000;
			if (pl->rot[1] < -0x1000) pl->rot[1] = -0x1000;
		}
	}
	else
	{
		pl->code = 0;
		pl->rot[1] = ConvergeI(pl->rot[1], 0, 0x40, 0x40);
	}
	ang = pl->ang[1];
	pl->ang[1] += pl->rot[1];
	if (pl->rot[1] <= -0x100 && ang < pl->ang[1])
	{
#ifdef MOTOR
		motor_8024C834(4, 20);
#endif
		Na_ObjSePlay(NA_SE5_07, pl->obj);
	}
	if (pl->rot[1] >= +0x100 && ang > pl->ang[1])
	{
#ifdef MOTOR
		motor_8024C834(4, 20);
#endif
		Na_ObjSePlay(NA_SE5_07, pl->obj);
	}
	PL_ProcWait(pl);
	if (pl->rot[1] >= 0)    pl->obj->s.ang[0] = -pl->rot[1];
	else                    pl->obj->s.ang[0] = +pl->rot[1];
	return FALSE;
}

static int PL_ExecAtck12(PLAYER *pl)
{
	if (++pl->timer == 1)
	{
		if (pl->code == 0)
		{
#ifdef MOTOR
			motor_8024C834(5, 50);
#endif
			PL_ThrowObject(pl);
		}
		else
		{
#ifdef MOTOR
			motor_8024C834(4, 50);
#endif
			PL_DropObject(pl);
		}
	}
	pl->rot[1] = 0;
	platck_80274EB0(pl, ANIME_183, PS_WAIT_01);
	return FALSE;
}

static int platck_80275F0C(PLAYER *pl)
{
	float level = pl->water - 100;
	if (pl->pos[1] < level) return PL_EnterWater(pl);
	if (pl->status & PA_PRESREQ) return PL_SetStateDrop(pl, PS_DEMO_39, 0);
	if (pl->power < 0x100) return PL_SetStateDrop(pl, PS_DEMO_11, 0);
	return FALSE;
}

int PL_ExecAtck(PLAYER *pl)
{
	int result;
	if (platck_80275F0C(pl)) return TRUE;
	if (PL_ProcSink(pl, 0.5F)) return TRUE;
	switch (pl->state)
	{
	case PS_ATCK_00: result = PL_ExecAtck00(pl); break;
	case PS_ATCK_03: result = PL_ExecAtck03(pl); break;
	case PS_ATCK_05: result = PL_ExecAtck05(pl); break;
	case PS_ATCK_06: result = PL_ExecAtck06(pl); break;
	case PS_ATCK_07: result = PL_ExecAtck07(pl); break;
	case PS_ATCK_08: result = PL_ExecAtck08(pl); break;
	case PS_ATCK_09: result = PL_ExecAtck09(pl); break;
	case PS_ATCK_10: result = PL_ExecAtck10(pl); break;
	case PS_ATCK_11: result = PL_ExecAtck11(pl); break;
	case PS_ATCK_12: result = PL_ExecAtck12(pl); break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
	if (!result)
	{
		if (pl->status & PA_WADING) pl->effect |= PE_00000080;
	}
	return result;
}
