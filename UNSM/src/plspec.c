#include <sm64.h>

extern OBJLANG obj_tree[];

static void plspec_8025DD70(PLAYER *pl)
{
	if (pl->attach->script == SegmentToVirtual(obj_tree))
	{
		float height = stage_index == STAGE_SSL ? 250.0F : 100.0F;
		if (pl->pos[1]-pl->ground_y > height) pl->effect |= PE_00002000;
	}
}

static void plspec_8025DE1C(PLAYER *pl, int code)
{
	int istree = pl->attach->script == SegmentToVirtual(obj_tree);
	if (code == 1)
	{
		if (PL_IsAnimeAtFrame(pl, 1))
		{
			Na_ObjSePlay(istree ? NA_SE0_3A : NA_SE0_41, pl->obj);
		}
	}
	else
	{
		Na_ObjSePlay(istree ? NA_SE1_12 : NA_SE1_11, pl->obj);
	}
}

static int plspec_8025DF04(PLAYER *pl, float offset)
{
	UNUSED FVEC pos;
	BGFACE *ground, *roof;
	float ground_y, roof_y;
	int wall, result = 0;
	float top = pl->attach->hit_h - 100;
	OBJECT *obj = pl->obj;
	if (obj->o_f7 > top) obj->o_f7 = top;
	pl->pos[0] = pl->attach->o_posx;
	pl->pos[2] = pl->attach->o_posz;
	pl->pos[1] = pl->attach->o_posy + obj->o_f7 + offset;
	wall  = BGHitWall(&pl->pos[0], &pl->pos[1], &pl->pos[2], 60, 50);
	wall |= BGHitWall(&pl->pos[0], &pl->pos[1], &pl->pos[2], 30, 24);
	roof_y = PL_CheckRoof(pl->pos, pl->pos[1], &roof);
	if (pl->pos[1] > roof_y-160)
	{
		pl->pos[1] = roof_y-160;
		obj->o_f7 = pl->pos[1] - pl->attach->o_posy;
	}
	ground_y = BGCheckGround(pl->pos[0], pl->pos[1], pl->pos[2], &ground);
	if (pl->pos[1] < ground_y)
	{
		pl->pos[1] = ground_y;
		PL_SetState(pl, PS_WAIT_01, 0);
		result = 1;
	}
	else if (obj->o_f7 < -pl->attach->hit_offset)
	{
		pl->pos[1] = pl->attach->o_posy - pl->attach->hit_offset;
		PL_SetState(pl, PS_JUMP_0C, 0);
		result = 2;
	}
	else if (wall)
	{
		if (pl->pos[1] > ground_y+20)
		{
			pl->speed = -2;
			PL_SetState(pl, PS_JUMP_36, 0);
			result = 2;
		}
		else
		{
			PL_SetState(pl, PS_WAIT_01, 0);
			result = 1;
		}
	}
	FVecCpy(pl->obj->s.pos, pl->pos);
	SVecSet(pl->obj->s.ang, pl->attach->o_angx, pl->ang[1], pl->attach->o_angz);
	return result;
}

extern OBJLANG obj_13000118[];

static int PL_ExecSpec00(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	float height;
	OBJLANG *script;
#if REVISION >= 199609
	if (pl->status & PA_TRIGREQ || pl->power < 0x100)
	{
		plspec_8025DD70(pl);
		pl->speed = -2;
		return PL_SetState(pl, PS_JUMP_36, 0);
	}
	if (pl->status & PA_JUMPREQ)
	{
		plspec_8025DD70(pl);
		pl->ang[1] += 0x8000;
		return PL_SetState(pl, PS_JUMP_06, 0);
	}
#else
	if (pl->status & PA_JUMPREQ)
	{
		plspec_8025DD70(pl);
		pl->ang[1] += 0x8000;
		return PL_SetState(pl, PS_JUMP_06, 0);
	}
	if (pl->status & PA_TRIGREQ)
	{
		plspec_8025DD70(pl);
		pl->speed = -2;
		return PL_SetState(pl, PS_JUMP_36, 0);
	}
#endif
	if (pl->cont->y > 16)
	{
		height = pl->attach->hit_h - 100;
		script = VirtualToSegment(SEG_OBJECT, pl->attach->script);
		if (obj->o_f7 < height-0.4F)
		{
			return PL_SetState(pl, PS_SPEC_03, 0);
		}
		if (script != obj_13000118 && pl->cont->y > 50)
		{
			return PL_SetState(pl, PS_SPEC_04, 0);
		}
	}
	if (pl->cont->y < -16)
	{
		obj->o_v6 -= pl->cont->y*2;
		if (obj->o_v6 > 0x1000) obj->o_v6 = 0x1000;
		pl->ang[1] += obj->o_v6;
		obj->o_f7 -= obj->o_v6/0x100;
		if (pl->attach->script == SegmentToVirtual(obj_tree))
		{
			if (pl->pos[1]-pl->ground_y > 100) pl->effect |= PE_00002000;
		}
		plspec_8025DE1C(pl, 2);
#ifdef MOTOR
		motor_8024C924();
#endif
		Na_game_803218D8(1, 2*(obj->o_v6/0x100));
	}
	else
	{
		obj->o_v6 = 0;
		pl->ang[1] -= pl->cont->x*16;
	}
	if (!plspec_8025DF04(pl, 0)) PL_SetAnime(pl, ANIME_13);
	return FALSE;
}

static int PL_ExecSpec03(PLAYER *pl)
{
	int vspeed;
	OBJECT *obj = pl->obj;
	SHORT _02 = pl->scene->cam->_02;
#if REVISION >= 199609
	if (pl->power < 0x100)
	{
		plspec_8025DD70(pl);
		pl->speed = -2;
		return PL_SetState(pl, PS_JUMP_36, 0);
	}
#endif
	if (pl->status & PA_JUMPREQ)
	{
		plspec_8025DD70(pl);
		pl->ang[1] += 0x8000;
		return PL_SetState(pl, PS_JUMP_06, 0);
	}
	if (pl->cont->y < 8) return PL_SetState(pl, PS_SPEC_00, 0);
	obj->o_f7 += pl->cont->y/8.0F;
	obj->o_v6 = 0;
	pl->ang[1] = TURN(pl->ang[1], _02, 0x400);
	if (!plspec_8025DF04(pl, 0))
	{
		vspeed = VSPEED(pl->cont->y/4.0F);
		PL_SetAnimeV(pl, ANIME_5, vspeed);
		plspec_8025DD70(pl);
		plspec_8025DE1C(pl, 1);
	}
	return FALSE;
}

static int PL_ExecSpec01(PLAYER *pl)
{
	PL_TrigSound(pl, NA_SE2_08, PL_VOICE);
	if (!plspec_8025DF04(pl, 0))
	{
		PL_SetAnime(pl, ANIME_6);
		if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, PS_SPEC_00, 0);
		plspec_8025DD70(pl);
	}
	return FALSE;
}

static int PL_ExecSpec02(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	PL_TrigSound(pl, NA_SE2_08, PL_VOICE);
	pl->ang[1] += obj->o_v6;
	obj->o_v6 = obj->o_v6 * 8/10;
	if (!plspec_8025DF04(pl, 0))
	{
		if (obj->o_v6 > 0x800)
		{
			PL_SetAnime(pl, ANIME_7);
		}
		else
		{
			PL_SetAnime(pl, ANIME_8);
			if (PL_IsAnimeLast1F(pl))
			{
				obj->o_v6 = 0;
				PL_SetState(pl, PS_SPEC_00, 0);
			}
		}
		plspec_8025DD70(pl);
	}
	return FALSE;
}

static int PL_ExecSpec04(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	obj->o_v6 = 0;
	if (pl->code == 0)
	{
		PL_SetAnime(pl, ANIME_11);
		if (PL_IsAnimeLast1F(pl)) return PL_SetState(pl, PS_SPEC_05, 0);
	}
	else
	{
		PL_SetAnime(pl, ANIME_12);
		if (pl->obj->s.skel.frame == 0) return PL_SetState(pl, PS_SPEC_00, 0);
	}
	plspec_8025DF04(pl, PL_GetAnimeY(pl));
	return FALSE;
}

static int PL_ExecSpec05(PLAYER *pl)
{
	UNUSED OBJECT *obj = pl->obj;
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_JUMP_0D, 0);
	if (pl->cont->y < -16) return PL_SetState(pl, PS_SPEC_04, 1);
	pl->ang[1] -= pl->cont->x*16;
	PL_SetAnime(pl, ANIME_9);
	plspec_8025DF04(pl, PL_GetAnimeY(pl));
	return FALSE;
}

static int plspec_8025EB50(PLAYER *pl, FVEC pos)
{
	UNUSED int i;
	BGFACE *roof, *ground;
	float roof_y, ground_y, gap;
	pl->wall = PL_CheckWall(pos, 50, 50);
	ground_y = BGCheckGround(pos[0], pos[1], pos[2], &ground);
	roof_y = PL_CheckRoof(pos, ground_y, &roof);
	if (!ground) return 1;
	if (!roof) return 2;
	if (roof_y-ground_y <= 160) return 1;
	if (roof->code != BG_5) return 2;
	gap = roof_y - (pos[1]+160);
	if (gap < -30) return 1;
	if (gap > +30) return 2;
	pos[1] = pl->roof_y - 160;
	FVecCpy(pl->pos, pos);
	pl->ground = ground;
	pl->ground_y = ground_y;
	pl->roof = roof;
	pl->roof_y = roof_y;
	return 0;
}

static int plspec_8025ECFC(PLAYER *pl)
{
	int result;
	FVEC pos;
	float limit = 4;
	pl->speed += 1;
	if (pl->speed > limit) pl->speed = limit;
	pl->ang[1] = TURN(pl->ang[1], pl->stick_ang, 0x800);
	pl->slide_ang = pl->ang[1];
	pl->slide_x = pl->speed * SIN(pl->ang[1]);
	pl->slide_z = pl->speed * COS(pl->ang[1]);
	pl->vel[0] = pl->slide_x;
	pl->vel[1] = 0;
	pl->vel[2] = pl->slide_z;
	pos[0] = pl->pos[0] - pl->vel[0]*pl->roof->ny;
	pos[2] = pl->pos[2] - pl->vel[2]*pl->roof->ny;
	pos[1] = pl->pos[1];
	result = plspec_8025EB50(pl, pos);
	FVecCpy(pl->obj->s.pos, pl->pos);
	SVecSet(pl->obj->s.ang, 0, pl->ang[1], 0);
	return result;
}

static void plspec_8025EED0(PLAYER *pl)
{
	pl->speed = 0;
	pl->slide_x = 0;
	pl->slide_z = 0;
	pl->pos[1] = pl->roof_y - 160;
	FVecCpy(pl->vel, fvec_0);
	FVecCpy(pl->obj->s.pos, pl->pos);
}

static int PL_ExecSpec08(PLAYER *pl)
{
#ifdef MOTOR
	if (pl->timer++ == 0) motor_8024C834(5, 80);
#else
	pl->timer++;
#endif
	if (pl->status & PA_WALKREQ && pl->timer > 30)
	{
		return PL_SetState(pl, PS_SPEC_09, 0);
	}
	if (!(pl->status & PA_JUMPSTA)) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_JUMP_29, 0);
	if (pl->roof->code != BG_5) return PL_SetState(pl, PS_JUMP_0C, 0);
	PL_SetAnime(pl, ANIME_53);
	PL_TrigSound(pl, NA_SE0_2D, PL_SOUND);
	plspec_8025EED0(pl);
	if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, PS_SPEC_09, 0);
	return FALSE;
}

static int PL_ExecSpec09(PLAYER *pl)
{
	if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_SPEC_0A, pl->code);
	if (!(pl->status & PA_JUMPSTA)) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_JUMP_29, 0);
	if (pl->roof->code != BG_5) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->code & 1)   PL_SetAnime(pl, ANIME_198);
	else                PL_SetAnime(pl, ANIME_199);
	plspec_8025EED0(pl);
	return FALSE;
}

static int PL_ExecSpec0A(PLAYER *pl)
{
	if (!(pl->status & PA_JUMPSTA)) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_TRIGREQ) return PL_SetState(pl, PS_JUMP_29, 0);
	if (pl->roof->code != BG_5) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->code & 1)   PL_SetAnime(pl, ANIME_92);
	else                PL_SetAnime(pl, ANIME_93);
	if (pl->obj->s.skel.frame == 12)
	{
		Na_ObjSePlay(NA_SE0_2D, pl->obj);
#ifdef MOTOR
		motor_8024C834(1, 30);
#endif
	}
	if (PL_IsAnimeLast2F(pl))
	{
		pl->code ^= 1;
		if (pl->status & PA_WAITREQ)
		{
			return PL_SetState(pl, PS_SPEC_09, pl->code);
		}
	}
	if (plspec_8025ECFC(pl) == 2) PL_SetState(pl, PS_JUMP_0C, 0);
	return FALSE;
}

static int plspec_8025F384(PLAYER *pl)
{
	float ground_y;
	BGFACE *ground;
	pl->vel[1] = 0;
	pl->speed = -8;
	pl->pos[0] -= 60 * SIN(pl->ang[1]);
	pl->pos[2] -= 60 * COS(pl->ang[1]);
	ground_y = BGCheckGround(pl->pos[0], pl->pos[1], pl->pos[2], &ground);
	if (ground_y < pl->pos[1]-100) pl->pos[1] -= 100;
	else pl->pos[1] = ground_y;
	return PL_SetState(pl, PS_JUMP_36, 0);
}

static void plspec_8025F4B4(PLAYER *pl)
{
	PL_SetAnime(pl, ANIME_195);
	pl->pos[0] += 14 * SIN(pl->ang[1]);
	pl->pos[2] += 14 * COS(pl->ang[1]);
	FVecCpy(pl->obj->s.pos, pl->pos);
}

static void plspec_8025F560(PLAYER *pl)
{
	float dist = pl->timer < 14 ? pl->timer : 14.0F;
	pl->camera->pos[0] = pl->pos[0] + dist*SIN(pl->ang[1]);
	pl->camera->pos[2] = pl->pos[2] + dist*COS(pl->ang[1]);
	pl->camera->pos[1] = pl->pos[1];
	pl->timer++;
	pl->flag |= PL_02000000;
}

static void plspec_8025F644(PLAYER *pl, int anime, u32 state)
{
	PL_Stop(pl);
	PL_SetAnime(pl, anime);
	if (PL_IsAnimeLast1F(pl))
	{
		PL_SetState(pl, state, 0);
		if (state == PS_WAIT_01) plspec_8025F4B4(pl);
	}
}

static int PL_ExecSpec0B(PLAYER *pl)
{
	float height;
	short dang = pl->stick_ang - pl->ang[1];
	int flag = pl->roof_y - pl->ground_y >= 160;
	if (pl->timer < 10) pl->timer++;
	if (pl->ground->ny < COS_25) return plspec_8025F384(pl);
	if (pl->status & (PA_LANDREQ|PA_TRIGREQ)) return plspec_8025F384(pl);
	if (pl->status & PA_JUMPREQ)
	{
		if (flag) return PL_SetState(pl, PS_SPEC_0F, 0);
	}
	if (pl->status & PA_HIT)
	{
		if (pl->obj->o_hit_result & HR_000002) PL_Damage(pl, 3);
		return plspec_8025F384(pl);
	}
#if REVISION == 199703
	if (
		pl->timer == 10 && pl->status & PA_WALKREQ && !(pl->status & PA_JUMPSTA)
	)
#else
	if (pl->timer == 10 && pl->status & PA_WALKREQ)
#endif
	{
		if (-0x4000 <= dang && dang <= 0x4000)
		{
			if (flag) return PL_SetState(pl, PS_SPEC_0C, 0);
		}
		else
		{
			return plspec_8025F384(pl);
		}
	}
	height = pl->pos[1] - PL_CheckGroundYNear(pl, -0x8000, 30);
	if (flag && height < 100) return PL_SetState(pl, PS_SPEC_0F, 0);
	if (pl->code == 0) PL_TrigSound(pl, NA_SE2_08, PL_VOICE);
	PL_Stop(pl);
	PL_SetAnime(pl, ANIME_51);
	return FALSE;
}

static int PL_ExecSpec0C_0D(PLAYER *pl)
{
	if (pl->status & PA_LANDREQ) return plspec_8025F384(pl);
	if (pl->timer >= 28 && pl->status & PA_MOTION)
	{
		plspec_8025F4B4(pl);
		return PL_CheckMotion(pl);
	}
	if (pl->timer == 10) PL_TrigSound(pl, NA_SE2_09, PL_VOICE);
	plspec_8025F644(pl, ANIME_0, PS_WAIT_01);
	plspec_8025F560(pl);
	if (pl->obj->s.skel.frame == 17) pl->state = PS_SPEC_0D;
	return FALSE;
}

static int PL_ExecSpec0E(PLAYER *pl)
{
	if (pl->status & PA_LANDREQ) return plspec_8025F384(pl);
	PL_TrigSound(pl, NA_SE2_08, PL_VOICE);
	plspec_8025F644(pl, ANIME_28, PS_SPEC_0B);
	pl->code = 1;
	return FALSE;
}

static int PL_ExecSpec0F(PLAYER *pl)
{
	if (pl->status & PA_LANDREQ) return plspec_8025F384(pl);
	PL_TrigSound(pl, NA_SE2_13_D0, PL_VOICE);
	plspec_8025F644(pl, ANIME_52, PS_WAIT_01);
	if (pl->obj->s.skel.frame == 8) PL_PlayLandEffect(pl, NA_SE0_08);
	plspec_8025F560(pl);
	return FALSE;
}

static int PL_ExecSpec30(PLAYER *pl)
{
	if (pl->obj->o_hit_result & HR_000004)
	{
		u32 code = (pl->obj->o_hit_result & HR_000040) == 0;
		pl->ang[1] = pl->attach->o_angy;
		FVecCpy(pl->pos, pl->obj->s.pos);
#ifdef MOTOR
		motor_8024C834(5, 60);
#endif
		return PL_SetState(pl, pl->speed >= 0 ? PS_JUMP_3D : PS_JUMP_3E, code);
	}
	PL_SetAnime(pl, ANIME_88);
	return FALSE;
}

static int PL_ExecSpec31(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	short angx = pl->ang[0];
	short angy = pl->ang[1];
	switch (pl->phase)
	{
	case 0:
		pl->obj->s.s.flag &= ~SHP_ACTIVE;
		pl->attach->o_hit_result = HR_008000;
		pl->camera->demo = 1;
		pl->camera->obj = pl->attach;
		FVecSet(pl->vel, 0, 0, 0);
		pl->pos[0] = pl->attach->o_posx;
		pl->pos[1] = pl->attach->o_posy + 350;
		pl->pos[2] = pl->attach->o_posz;
		pl->speed = 0;
		pl->phase = 1;
		break;
	case 1:
		if (pl->attach->o_mode == 1)
		{
			pl->ang[0] = pl->attach->o_angx;
			pl->ang[1] = pl->attach->o_angy;
			obj->o_v6 = pl->attach->o_angy;
			obj->o_v7 = 0;
			pl->phase = 2;
		}
		break;
	case 2:
		pl->ang[0] -= (SHORT)(pl->cont->y*10);
		obj->o_v7  -= (SHORT)(pl->cont->x*10);
		if (pl->ang[0] > DEG(80)) pl->ang[0] = DEG(80);
		if (pl->ang[0] < DEG(0)) pl->ang[0] = DEG(0);
		if (obj->o_v7 > DEG( 90)) obj->o_v7 = DEG( 90);
		if (obj->o_v7 < DEG(-90)) obj->o_v7 = DEG(-90);
		pl->ang[1] = obj->o_v6 + obj->o_v7;
		if (pl->status & PA_JUMPREQ)
		{
			pl->speed   = 100 * COS(pl->ang[0]);
			pl->vel[1]  = 100 * SIN(pl->ang[0]);
			pl->pos[0] += 120 * COS(pl->ang[0]) * SIN(pl->ang[1]);
			pl->pos[1] += 120 * SIN(pl->ang[0]);
			pl->pos[2] += 120 * COS(pl->ang[0]) * COS(pl->ang[1]);
			Na_ObjSePlay(NA_SE0_56, pl->obj);
			Na_ObjSePlay(NA_SE5_1A, pl->obj);
			pl->obj->s.s.flag |= SHP_ACTIVE;
			PL_SetState(pl, PS_JUMP_18, 0);
#ifdef MOTOR
			motor_8024C834(60, 70);
#endif
			pl->attach->o_mode = 2;
			return FALSE;
			break;
		}
		if (pl->ang[0] != angx || pl->ang[1] != angy)
		{
			Na_ObjSePlay(NA_SE1_19, pl->obj);
#ifdef MOTOR
			motor_8024C974(0);
#endif
		}
	}
	FVecCpy(pl->obj->s.pos, pl->pos);
	SVecSet(pl->obj->s.ang, 0, pl->ang[1], 0);
	PL_SetAnime(pl, ANIME_136);
	return FALSE;
}

static int PL_ExecSpec32(PLAYER *pl)
{
	BGFACE *ground;
	FVEC pos;
	float s, c, ground_y;
	OBJECT *obj = pl->obj;
	OBJECT *attach = pl->attach;
	short ang = pl->spin_ang;
	float dx = 0.95F * (pl->pos[0]-attach->o_posx);
	float dz = 0.95F * (pl->pos[2]-attach->o_posz);
	if (pl->vel[1] < 60) pl->vel[1] += 1;
	if ((obj->o_f7 += pl->vel[1]) < 0) obj->o_f7 = 0;
	if (obj->o_f7 > attach->hit_h)
	{
		if (pl->vel[1] < 20) pl->vel[1] = 20;
		return PL_SetState(pl, PS_JUMP_24, 1);
	}
	if (pl->rot[1] < 0x3000) pl->rot[1] += 0x100;
	if (obj->o_v6 < 0x1000) obj->o_v6 += 0x100;
	pl->spin_ang += pl->rot[1];
	s = SIN(obj->o_v6);
	c = COS(obj->o_v6);
	pos[0] = attach->o_posx + dx*c + dz*s;
	pos[2] = attach->o_posz - dx*s + dz*c;
	pos[1] = attach->o_posy + obj->o_f7;
	BGHitWall(&pos[0], &pos[1], &pos[2], 60, 50);
	ground_y = BGCheckGround(pos[0], pos[1], pos[2], &ground);
	if (ground)
	{
		pl->ground = ground;
		pl->ground_y = ground_y;
		FVecCpy(pl->pos, pos);
	}
	else
	{
		if (pos[1] >= pl->ground_y) pl->pos[1] = pos[1];
		else                        pl->pos[1] = pl->ground_y;
	}
	pl->timer++;
	PL_SetAnime(pl, pl->code == 0 ? ANIME_149 : ANIME_148);
	if (PL_IsAnimeLast2F(pl)) pl->code = 1;
	if (ang > pl->spin_ang) Na_ObjSePlay(NA_SE0_38, pl->obj);
	FVecCpy(pl->obj->s.pos, pl->pos);
	SVecSet(pl->obj->s.ang, 0, pl->ang[1]+pl->spin_ang, 0);
#ifdef MOTOR
	motor_8024C924();
#endif
	return FALSE;
}

static int plspec_80260568(PLAYER *pl)
{
	if (pl->pos[1] < pl->water-100) return PL_EnterWater(pl);
	return FALSE;
}

int PL_ExecSpec(PLAYER *pl)
{
	int result;
	if (plspec_80260568(pl)) return TRUE;
	pl->sink = 0;
	switch (pl->state)
	{
	case PS_SPEC_00: result = PL_ExecSpec00(pl); break;
	case PS_SPEC_01: result = PL_ExecSpec01(pl); break;
	case PS_SPEC_02: result = PL_ExecSpec02(pl); break;
	case PS_SPEC_03: result = PL_ExecSpec03(pl); break;
	case PS_SPEC_04: result = PL_ExecSpec04(pl); break;
	case PS_SPEC_05: result = PL_ExecSpec05(pl); break;
	case PS_SPEC_08: result = PL_ExecSpec08(pl); break;
	case PS_SPEC_09: result = PL_ExecSpec09(pl); break;
	case PS_SPEC_0A: result = PL_ExecSpec0A(pl); break;
	case PS_SPEC_0B: result = PL_ExecSpec0B(pl); break;
	case PS_SPEC_0C: result = PL_ExecSpec0C_0D(pl); break;
	case PS_SPEC_0D: result = PL_ExecSpec0C_0D(pl); break;
	case PS_SPEC_0E: result = PL_ExecSpec0E(pl); break;
	case PS_SPEC_0F: result = PL_ExecSpec0F(pl); break;
	case PS_SPEC_30: result = PL_ExecSpec30(pl); break;
	case PS_SPEC_31: result = PL_ExecSpec31(pl); break;
	case PS_SPEC_32: result = PL_ExecSpec32(pl); break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
	return result;
}
