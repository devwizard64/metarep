#include <sm64.h>

extern OBJLANG obj_13000E88[];
extern OBJLANG obj_13000EAC[];
extern OBJLANG obj_13001BB4[];
extern OBJLANG obj_13001BD4[];
extern OBJLANG obj_13002A48[];
extern OBJLANG obj_13002AF0[];
extern OBJLANG obj_13002F40[];
extern OBJLANG obj_13003868[];

static Vp demo_vp =
{{
	{4*(SCREEN_WD/2), 4*(SCREEN_HT/2), G_MAXZ/2, 0},
	{4*(SCREEN_WD/2), 4*(SCREEN_HT/2), G_MAXZ/2, 0},
}};
static OBJECT *demo_pipe;
static OBJECT *demo_peach;
static OBJECT *demo_toadA;
static OBJECT *demo_toadB;
static OBJECT *demo_star;
UNUSED static OBJECT *pldemo_8033B2B4;
static STAFF *staffdrawp = NULL;
static char peach_eyes = 0;
static char pldemo_8032DB48 = 0;
static short peach_anime;
static short toad_anime[2];

static int StaffStrWd(const char *str)
{
	int c, width = 0;
	while ((c = *str++) != '\0') width += c == ' ' ? 4 : 7;
	return width;
}

void StaffDraw(void)
{
	if (staffdrawp)
	{
		const char **strtab = staffdrawp->str;
		const char *str = *strtab++;
		SHORT n = *str++ - '0';
		SHORT y =
			(staffdrawp->flag & STAFF_B ? 28 : SCREEN_HT-68) + 16*(n == 1);
#if REVISION >= 199609
		SHORT ht = 16;
#else
#define ht 16
#endif
		StaffBegin();
		StaffPrint(28, y, str);
#if REVISION >= 199609
		switch (n)
		{
		case 4:
			StaffPrint(28, y+24, *strtab++);
			n = 2;
			ht = 24;
			break;
		case 5:
			StaffPrint(28, y+16, *strtab++);
			n = 3;
			break;
#ifdef MULTILANG
		case 6:
			StaffPrint(28, y+32, *strtab++);
			n = 3;
			break;
		case 7:
			StaffPrint(28, y+16, *strtab++);
			StaffPrint(28, y+32, *strtab++);
			n = 3;
			break;
#endif
		}
#endif
		while (n-- > 0)
		{
			StaffPrint(SCREEN_WD-28-StaffStrWd(*strtab), y, *strtab);
			y += ht;
			strtab++;
		}
		StaffEnd();
		staffdrawp = NULL;
#undef ht
	}
}

void pldemo_80257060(void)
{
	ObjectSetAnime(peach_anime);
	if (objectlib_8029FF04())
	{
		if (peach_anime < 3 || peach_anime == 6 || peach_anime == 7)
		{
			peach_anime++;
		}
	}
}

void pldemo_802570DC(void)
{
	int i = object->o_posx >= 0;
	ObjectSetAnime(toad_anime[i]);
	if (objectlib_8029FF04())
	{
		if (toad_anime[i] == 0 || toad_anime[i] == 2) toad_anime[i]++;
	}
}

void *Ctrl_pldemo_80257198(int code, SHAPE *shape, UNUSED void *data)
{
	static char eyestab[] = {2, 3, 2, 1, 2, 3, 2};
	SSELECT *shp = (SSELECT *)shape;
	if (code == SC_DRAW)
	{
		if (peach_eyes == 0)
		{
			SHORT i = (draw_timer+32) >> 1 & 31;
			if (i < 7)  shp->index = 4*pldemo_8032DB48 + eyestab[i];
			else        shp->index = 4*pldemo_8032DB48 + 1;
		}
		else
		{
			shp->index = 4*pldemo_8032DB48 + peach_eyes-1;
		}
	}
	return NULL;
}

UNUSED
static void pldemo_80257270(short *timer)
{
	if (MsgGet() == MSG_NULL) *timer = 0;
}

static int pldemo_802572B0(PLAYER *pl)
{
	static u8 startab[] = {1, 3, 8, 30, 50, 70};
	int i, result = 0;
	for (i = 0; i < 6; i++)
	{
		int n = startab[i];
		if (pl->prevstar < n && pl->star >= n)
		{
			result = MSG_141+i;
			break;
		}
	}
	pl->prevstar = pl->star;
	return result;
}

static void pldemo_8025733C(PLAYER *pl)
{
	int msg;
	if (PL_IsAnimeLast2F(pl) && msg_result)
	{
		if (msg_result == 1 || msg_result == 2)
		{
			BuWrite();
			if (msg_result == 2) GmFadeout(EXIT_FACE, 0);
		}
		if (msg_result != 2)
		{
			objectlib_802A4728();
			pl->ang[1] += 0x8000;
			if ((msg = pldemo_802572B0(pl)))
			{
				Na_PeachMessage();
				PL_SetState(pl, PS_DEMO_05, msg);
			}
			else
			{
				PL_SetState(pl, PS_WAIT_01, 0);
			}
		}
	}
}

static OBJECT *pldemo_80257450(
	PLAYER *pl, int shape, OBJLANG *script, SHORT ang
)
{
	OBJECT *o = ObjMakeHere(pl->obj, shape, script);
	o->o_shapeangy = pl->ang[1] + ang;
	o->o_posx = pl->pos[0];
	o->o_posy = pl->pos[1];
	o->o_posz = pl->pos[2];
	return o;
}

static void pldemo_802574E8(PLAYER *pl)
{
	pl->flag &= ~PL_HEADCAP;
	pl->flag |= PL_HANDCAP;
	Na_ObjSePlay(NA_SE0_3D, pl->obj);
}

static void pldemo_80257548(PLAYER *pl)
{
	pl->flag &= ~PL_HANDCAP;
	pl->flag |= PL_HEADCAP;
	Na_ObjSePlay(NA_SE0_3E, pl->obj);
}

int pldemo_802575A8(void)
{
	int class = mario->state & PC_MASK;
	int result = FALSE;
	if (mario->state == PS_DEMO_0A || class == PC_WAIT || class == PC_WALK)
	{
		if (!(mario->state & (PF_RIDE|PF_DMGE)) && mario->state != PS_WAIT_27)
		{
			result = TRUE;
		}
	}
	return result;
}

int pldemo_80257640(int code)
{
	int result = 0;
	if (mario->state == PS_DEMO_06)
	{
		if (mario->phase < 8)
		{
			result = 1;
		}
		if (mario->phase == 8)
		{
			if (code == 0)  mario->phase++;
			else            result = 2;
		}
	}
	else
	{
		if (code != 0 && pldemo_802575A8())
		{
			mario->attach = object;
			PL_SetState(mario, PS_DEMO_06, code);
			result = 1;
		}
	}
	return result;
}

static int PL_ExecDemo06(PLAYER *pl)
{
	int rot = 0;
	if (pl->code == 2) rot = -0x400;
	if (pl->code == 3) rot = 0x180;
	if (pl->phase < 8)
	{
		SHORT angy = PL_GetAngToObj(pl, pl->attach);
		pl->ang[1] = TURN(pl->ang[1], angy, 0x800);
		pl->timer += rot;
		PL_SetAnime(pl, !pl->take ? ANIME_194 : ANIME_63);
	}
	else if (pl->phase >= 9 && pl->phase < 9+8)
	{
		pl->timer -= rot;
	}
	else if (pl->phase == 23)
	{
		if (pl->flag & PL_HANDCAP) PL_SetState(pl, PS_DEMO_3D, 0);
		else PL_SetState(pl, !pl->take ? PS_WAIT_01 : PS_WAIT_07, 0);
	}
	FVecCpy(pl->obj->s.pos, pl->pos);
	SVecSet(pl->obj->s.ang, 0, pl->ang[1], 0);
	SVecSet(pl->ctrl->neck_ang, pl->timer, 0, 0);
	if (pl->phase != 8) pl->phase++;
	return FALSE;
}

static int PL_ExecDemo0A(PLAYER *pl)
{
	PL_SetAnime(pl, !pl->take ? ANIME_194 : ANIME_63);
	FVecCpy(pl->obj->s.pos, pl->pos);
	SVecSet(pl->obj->s.ang, 0, pl->ang[1], 0);
	return FALSE;
}

static int PL_ExecDemo00(PLAYER *pl)
{
	PL_SetAnime(pl, ANIME_14);
	PL_Stop(pl);
	pl->obj->s.s.flag &= ~SHP_ACTIVE;
	if (pl->code)
	{
		pl->code--;
		if (!(pl->code & 0xFFFF)) PL_Fade(pl, pl->code >> 16);
	}
	return FALSE;
}

#ifdef sgi
#define HIHALF(x)   (((u16 *)&(x))[0])
#define LOHALF(x)   (((u16 *)&(x))[1])
#else
#define HIHALF(x)   ((u16)((x) >> 16))
#define LOHALF(x)   ((u16)((x) >>  0))
#endif

static int PL_ExecDemo05(PLAYER *pl)
{
	pl->phase++;
	if (pl->phase == 2) objectlib_802A4704();
	if (pl->phase < 9)
	{
		PL_SetAnime(pl, pl->prevstate == PS_DEMO_03 ? ANIME_178 : ANIME_194);
		pl->timer -= 0x400;
	}
	else if (pl->phase == 9)
	{
		u32 code = pl->code;
		if (!HIHALF(code))  MsgOpen(LOHALF(code));
		else                MsgOpenInt(HIHALF(code), LOHALF(code));
	}
	else if (pl->phase == 10)
	{
		if (MsgIsOpen()) pl->phase--;
	}
	else if (pl->phase < 19)
	{
		pl->timer += 0x400;
	}
	else if (pl->phase == 25)
	{
		objectlib_802A4728();
		if (first_msg)
		{
			first_msg = FALSE;
			AudPlayStageBGM(NA_BGM_CASTLE);
		}
		if (pl->prevstate == PS_DEMO_03) PL_SetState(pl, PS_SWIM_00, 0);
		else PL_SetState(
			pl, pl->prevstate == PS_DEMO_2F ? PS_WALK_00 : PS_WAIT_01, 0
		);
	}
	SVecSet(pl->ctrl->neck_ang, pl->timer, 0, 0);
	return FALSE;
}

static int PL_ExecDemo08(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	PL_TrigSound(pl, NA_SE0_5B, PL_SOUND);
	switch (pl->phase)
	{
	case 0:
		camera_8028BD34(1);
		objectlib_802A4704();
		PL_SetAnime(pl, ANIME_194);
		pl->phase = 1;
		FALLTHROUGH;
	case 1:
		pl->ang[1] += obj->o_v5 / 11;
		pl->pos[0] += obj->o_f6 / 11;
		pl->pos[2] += obj->o_f7 / 11;
		if (pl->timer++ == 10)
		{
			MsgOpenSignpost(pl->attach->o_code);
			pl->phase = 2;
		}
		break;
	case 2:
		if (!camerap->demo)
		{
			objectlib_802A4728();
			PL_SetState(pl, PS_WAIT_01, 0);
		}
		break;
	}
	FVecCpy(obj->s.pos, pl->pos);
	SVecSet(obj->s.ang, 0, pl->ang[1], 0);
	return FALSE;
}

static int PL_ExecDemo0F(PLAYER *pl)
{
	BGFACE *ground;
	float ground_y;
	FVEC pos;
	float speed = cont1->held & B_BUTTON ? 4 : 1;
	if (cont1->held & L_TRIG) speed = 0.01F;
	PL_SetAnime(pl, ANIME_14);
	FVecCpy(pos, pl->pos);
	if (cont1->held & U_JPAD) pos[1] += 16*speed;
	if (cont1->held & D_JPAD) pos[1] -= 16*speed;
	if (pl->stick_dist > 0)
	{
		pos[0] += 32*speed * SIN(pl->stick_ang);
		pos[2] += 32*speed * COS(pl->stick_ang);
	}
	PL_CheckWall(pos, 60, 50);
	ground_y = BGCheckGround(pos[0], pos[1], pos[2], &ground);
	if (ground)
	{
		if (pos[1] < ground_y) pos[1] = ground_y;
		FVecCpy(pl->pos, pos);
	}
	pl->ang[1] = pl->stick_ang;
	FVecCpy(pl->obj->s.pos, pl->pos);
	SVecSet(pl->obj->s.ang, 0, pl->ang[1], 0);
	if (cont1->down == A_BUTTON)
	{
		u32 state;
		if (pl->pos[1] <= pl->water-100)    state = PS_SWIM_00;
		else                                state = PS_WAIT_01;
		PL_SetState(pl, state, 0);
	}
	return FALSE;
}

static void pldemo_80258184(PLAYER *pl, int inwater)
{
	if (pl->phase == 0)
	{
		switch (++pl->timer)
		{
		case 1:
			ObjMakeHere(pl->obj, S_POWERSTAR, obj_13003868);
			AudLock();
			if (pl->code & 1)
			{
				Na_StarCatch();
			}
			else if (stage_index == STAGE_BITDWA || stage_index == STAGE_BITFSA)
			{
				Na_BgmPlay(NA_HANDLE_FGM, NA_BGM_ARENACLEAR, 0);
			}
			else
			{
				Na_BgmPlay(NA_HANDLE_FGM, NA_BGM_STARCATCH, 0);
			}
			break;
		case 42:
			Na_ObjSePlay(NA_SE2_0C, pl->obj);
			break;
		case 80:
			if (!(pl->code & 1))
			{
				PL_Fade(pl, FADE_WIN);
			}
			else
			{
				objectlib_802A4704();
				MsgOpenPrompt(bu_level == 7 ? MSG_13 : MSG_14);
				pl->phase = 1;
			}
			break;
		}
	}
	else if (pl->phase == 1 && msg_answer)
	{
		if (msg_answer == 1) BuWrite();
		pl->phase = 2;
	}
	else if (pl->phase == 2 && PL_IsAnimeLast1F(pl))
	{
		int msg;
		objectlib_802A4728();
		AudUnlock();
		msg = pldemo_802572B0(pl);
		if (msg) PL_SetState(pl, PS_DEMO_05, msg);
		else PL_SetState(pl, inwater ? PS_SWIM_00 : PS_WAIT_01, 0);
	}
}

static int PL_ExecDemo02_07(PLAYER *pl)
{
	pl->ang[1] = pl->scene->cam->_02;
	PL_SetAnime(pl, pl->phase == 2 ? ANIME_206 : ANIME_205);
	pldemo_80258184(pl, FALSE);
	if (pl->phase != 2 && pl->timer >= 40) pl->ctrl->hand = 2;
	PL_Stop(pl);
	return FALSE;
}

static int PL_ExecDemo03(PLAYER *pl)
{
	pl->ang[1] = pl->scene->cam->_02;
	PL_SetAnime(pl, pl->phase == 2 ? ANIME_180 : ANIME_179);
	FVecCpy(pl->obj->s.pos, pl->pos);
	SVecSet(pl->obj->s.ang, 0, pl->ang[1], 0);
	pldemo_80258184(pl, TRUE);
	if (pl->phase != 2 && pl->timer >= 62) pl->ctrl->hand = 2;
	return FALSE;
}

static int PL_ExecDemo04(PLAYER *pl)
{
	if (pl->pos[1] < pl->water-130)
	{
		Na_ObjSePlay(NA_SE0_30, pl->obj);
		pl->effect |= PE_00000040;
		return PL_SetState(pl, PS_DEMO_03, pl->code);
	}
	if (PL_ProcJump(pl, 1) == JUMP_LAND)
	{
		PL_PlayLandEffect(pl, NA_SE0_08);
		PL_SetState(pl, pl->code & 1 ? PS_DEMO_07 : PS_DEMO_02, pl->code);
	}
	PL_SetAnime(pl, ANIME_86);
	return FALSE;
}

static int pldemo_802586CC(PLAYER *pl, int anime, int frame)
{
	int f = PL_SetAnime(pl, anime);
	if (f == frame) PL_Fade(pl, FADE_DIE);
	pl->ctrl->eyes = 8;
	PL_Stop(pl);
	return f;
}

static int PL_ExecDemo11(PLAYER *pl)
{
	if (pl->status & PA_GAS) return PL_SetState(pl, PS_DEMO_14, 0);
	PL_TrigSound(pl, NA_SE2_15, PL_SOUND);
	pldemo_802586CC(pl, ANIME_50, 80);
	if (pl->obj->s.skel.frame == 77) PL_PlayLandEffect(pl, NA_SE0_18);
	return FALSE;
}

static int PL_ExecDemo13(PLAYER *pl)
{
	PL_TrigSound(pl, NA_SE2_15, PL_SOUND);
	pldemo_802586CC(pl, ANIME_121, 43);
	return FALSE;
}

static int PL_ExecDemo14(PLAYER *pl)
{
	PL_TrigSound(pl, NA_SE2_15, PL_SOUND);
	pldemo_802586CC(pl, ANIME_47, 86);
	return FALSE;
}

static int PL_ExecDemo16(PLAYER *pl)
{
	PL_TrigSound(pl, NA_SE2_15, PL_SOUND);
	if (pldemo_802586CC(pl, ANIME_3, 54) == 40)
	{
		PL_PlayFallEffect(pl, NA_SE0_18);
	}
	return FALSE;
}

static int PL_ExecDemo15(PLAYER *pl)
{
	PL_TrigSound(pl, NA_SE2_15, PL_SOUND);
	if (pldemo_802586CC(pl, ANIME_46, 37) == 37)
	{
		PL_PlayFallEffect(pl, NA_SE0_18);
	}
	return FALSE;
}

static int PL_ExecDemo12(PLAYER *pl)
{
	if (pl->phase == 0)
	{
		PL_SetAnime(pl, ANIME_118);
		PL_SetAnimeFrame(pl, 60);
		pl->phase = 1;
	}
	if (pl->phase == 1)
	{
		if (pl->sink >= 100) PL_TrigSound(pl, NA_SE2_10, PL_SOUND);
		if ((pl->sink += 5) >= 180)
		{
			PL_Fade(pl, FADE_DIE);
			pl->phase = 2;
		}
	}
	PL_ProcWait(pl);
	Na_ObjSePlay(NA_SE1_14, pl->obj);
	return FALSE;
}

static int PL_ExecDemo17(PLAYER *pl)
{
	PL_TrigSound(pl, NA_SE2_15, PL_SOUND);
	PL_SetAnime(pl, ANIME_14);
	pl->obj->s.s.flag &= ~SHP_ACTIVE;
	pl->power = 0xFF;
	if (pl->timer++ == 60) PL_Fade(pl, FADE_DIE);
	return FALSE;
}

static int pldemo_80258B24(PLAYER *pl, u32 state, int anime, float speed)
{
	int result;
	PL_SetSpeed(pl, speed);
	PL_SetAnime(pl, anime);
	result = PL_ProcJump(pl, 0) == JUMP_LAND;
	if (result) PL_SetState(pl, state, 0);
	return result;
}

static int PL_ExecDemo2E(PLAYER *pl)
{
	pl->ang[1] = pl->attach->o_angy;
	pl->pos[0] = pl->attach->o_posx + 75*COS(pl->ang[1]);
	pl->pos[2] = pl->attach->o_posz + 75*SIN(pl->ang[1]);
	if (pl->code & 2) pl->ang[1] += 0x8000;
	if (pl->timer == 0)
	{
		pldemo_80257450(pl, S_DOORKEY, obj_13001BB4, 0);
		PL_SetAnime(pl, ANIME_97);
	}
	switch (pl->obj->s.skel.frame)
	{
	case  79: Na_ObjSePlay(NA_SE3_42, pl->obj); break;
	case 111: Na_ObjSePlay(NA_SE3_3B, pl->obj); break;
	}
	PL_UseAnimePos(pl);
	PL_Stop(pl);
	if (PL_IsAnimeLast1F(pl))
	{
		if (ObjGetArg(pl->attach) == 1)
		{
			BuSetFlag(BU_KEYDOOR2);
			BuClrFlag(BU_KEY2);
		}
		else
		{
			BuSetFlag(BU_KEYDOOR1);
			BuClrFlag(BU_KEY1);
		}
		PL_SetState(pl, PS_WALK_00, 0);
	}
	pl->timer++;
	return FALSE;
}

static int PL_ExecDemo2F(PLAYER *pl)
{
	switch (pl->phase)
	{
	case 0:
		pl->ang[1] = pl->attach->o_angy;
		if (pl->code & 2) pl->ang[1] += 0x8000;
		pl->obj->o_f6 = pl->pos[0];
		pl->obj->o_f7 = pl->pos[2];
		PL_SetAnime(pl, ANIME_156);
		pl->phase++;
		break;
	case 1:
		if (PL_IsAnimeLast1F(pl))
		{
			ObjMakeHere(pl->obj, S_POWERSTAR, obj_13002F40);
			pl->phase++;
		}
		break;
	case 2:
		if (pl->timer++ == 70)
		{
			PL_SetAnime(pl, ANIME_157);
			pl->phase++;
		}
		break;
	case 3:
		if (PL_IsAnimeLast1F(pl))
		{
			BuSetFlag(PL_GetStarDoorFlag(pl->attach));
			PL_SetState(pl, PS_DEMO_05, MSG_38);
		}
		break;
	}
	pl->pos[0] = pl->obj->o_f6;
	pl->pos[2] = pl->obj->o_f7;
	PL_UseAnimePos(pl);
	PL_Stop(pl);
	return FALSE;
}

static int PL_ExecDemo31(PLAYER *pl)
{
	if (pl->timer++ == 0)
	{
		float dx, dz;
		SHORT angy;
		pl->collide->o_hit_result = HR_010000;
		angy = pl->attach->o_angy + DEG(30);
		if (pl->code & 2) angy += 0x8000 - DEG(60);
		dx = pl->attach->o_posx + 150*SIN(angy) - pl->pos[0];
		dz = pl->attach->o_posz + 150*COS(angy) - pl->pos[2];
		pl->obj->o_f6 = dx/20;
		pl->obj->o_f7 = dz/20;
		pl->ang[1] = ATAN2(dz, dx);
	}
	if (pl->timer < 15)
	{
		PL_SetAnime(pl, ANIME_194);
	}
	else if (pl->timer < 35)
	{
		pl->pos[0] += pl->obj->o_f6;
		pl->pos[2] += pl->obj->o_f7;
		PL_SetAnimeV(pl, ANIME_72, VSPEED(2.5F));
	}
	else
	{
		pl->ang[1] = pl->attach->o_angy;
		if (pl->code & 2) pl->ang[1] += 0x8000;
		pl->pos[0] += 12 * SIN(pl->ang[1]);
		pl->pos[2] += 12 * COS(pl->ang[1]);
		PL_SetAnimeV(pl, ANIME_72, VSPEED(2.5F));
	}
	PL_Stop(pl);
	if (pl->timer == 48) PL_SetState(pl, PS_WAIT_01, 0);
	return FALSE;
}

static int PL_ExecDemo20_21(PLAYER *pl)
{
	if (pl->timer == 0)
	{
		if (pl->code & 1)
		{
			pl->collide->o_hit_result = HR_010000;
			PL_SetAnime(pl, ANIME_95);
		}
		else
		{
			pl->collide->o_hit_result = HR_020000;
			PL_SetAnime(pl, ANIME_96);
		}
	}
	pl->ang[1] = pl->attach->o_angy;
	pl->pos[0] = pl->attach->o_posx;
	pl->pos[2] = pl->attach->o_posz;
	PL_UseAnimePos(pl);
	PL_Stop(pl);
	if (pl->code & 4)
	{
		if (pl->timer == 16) PL_Fade(pl, FADE_DOOR);
	}
	else if (PL_IsAnimeLast1F(pl))
	{
		if (pl->code & 2) pl->ang[1] += 0x8000;
		PL_SetState(pl, PS_WAIT_01, 0);
	}
	pl->timer++;
	return FALSE;
}

static int PL_ExecDemo22(PLAYER *pl)
{
	if (pl->phase == 0)
	{
		pl->phase = 1;
		if (pl->code & 1)   pl->attach->o_hit_result = HR_040000;
		else                pl->attach->o_hit_result = HR_080000;
	}
	else if (pl->attach->o_mode == 0)
	{
		if (ISTRUE(first_msg) && stage_index == STAGE_INSIDE)
		{
			PL_SetState(pl, PS_DEMO_05, MSG_21);
		}
		else
		{
			PL_SetState(pl, PS_WAIT_01, 0);
		}
	}
	PL_SetAnime(pl, ANIME_194);
	PL_Stop(pl);
	return FALSE;
}

static int PL_ExecDemo23(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	if (pl->timer++ < 11)
	{
		obj->s.s.flag &= ~SHP_ACTIVE;
		return FALSE;
	}
	obj->s.s.flag |= SHP_ACTIVE;
	PL_TrigSound(pl, NA_SE2_04, PL_VOICE);
	if (stage_index == STAGE_THI)
	{
		if (scene_index == 2)   PL_TrigSound(pl, NA_SE7_17, PL_SOUND);
		else                    PL_TrigSound(pl, NA_SE7_16, PL_SOUND);
	}
	if (pldemo_80258B24(pl, PS_WAIT_30, ANIME_77, 8))
	{
		PL_SetSpeed(pl, 0);
		PL_PlayLandEffect(pl, NA_SE0_08);
	}
	return FALSE;
}

static int PL_ExecDemo24(PLAYER *pl)
{
	if (pl->pos[1] < pl->water-100)
	{
		GmInitMessage(0);
		return PL_EnterWater(pl);
	}
	PL_SetSpeed(pl, pl->speed);
	if (PL_ProcJump(pl, 0) == JUMP_LAND)
	{
		PL_PlayLandEffect(pl, NA_SE0_08);
		PL_SetState(pl, PS_DEMO_25, 0);
	}
	if (pl->phase == 0 && pl->pos[1]-pl->ground_y > 300)
	{
		if (PL_SetAnime(pl, ANIME_111) == 0) Na_ObjSePlay(NA_SE0_37, pl->obj);
	}
	else
	{
		pl->phase = 1;
		PL_SetAnime(pl, ANIME_86);
	}
	return FALSE;
}

static int PL_ExecDemo25(PLAYER *pl)
{
	PL_Stop(pl);
	PL_SetAnime(pl, ANIME_87);
	if (PL_IsAnimeLast1F(pl))
	{
		GmInitMessage(0);
		PL_SetState(pl, PS_WAIT_01, 0);
	}
	return FALSE;
}

static int PL_ExecDemo26(PLAYER *pl)
{
	if (pl->timer++ > 15 && pldemo_80258B24(pl, PS_DEMO_27, ANIME_86, -32))
	{
		pl->recover = 4*7+3;
	}
	pl->obj->s.ang[1] += 0x8000;
	pl->effect |= PE_00000008;
	return FALSE;
}

static int PL_ExecDemo2D(PLAYER *pl)
{
	if (pldemo_80258B24(pl, PS_DEMO_27, ANIME_86, 0)) pl->recover = 4*7+3;
	pl->obj->s.ang[1] += 0x8000;
	pl->effect |= PE_00000008;
	return FALSE;
}

static int PL_ExecDemo27(PLAYER *pl)
{
	int frame;
	PL_ProcWait(pl);
	PL_TrigLandEffect(pl, NA_SE0_08);
	switch (pl->phase)
	{
	case 0:
		PL_SetAnime(pl, pl->code == 0 ? ANIME_87 : ANIME_78);
		if (PL_IsAnimeLast2F(pl))
		{
			if (!(bu_course == COURSE_BITDW || bu_course == COURSE_BITFS))
			{
				objectlib_802A4704();
			}
			MenuOpen(MENU_SAVE);
			msg_result = 0;
			pl->phase = 3;
			if (!(pl->flag & PL_HEADCAP)) pl->phase = 2;
			if (bu_course == COURSE_BITDW || bu_course == COURSE_BITFS)
			{
				pl->phase = 1;
			}
		}
		break;
	case 1:
		frame = PL_SetAnime(pl, ANIME_49);
		switch (frame)
		{
		case -1:
			pldemo_80257450(pl, S_DOORKEY, obj_13001BD4, -0x8000);
			FALLTHROUGH;
		case  67: Na_ObjSePlay(NA_SE0_36, pl->obj); FALLTHROUGH;
		case  83: Na_ObjSePlay(NA_SE0_3F, pl->obj); FALLTHROUGH;
		case 111: Na_ObjSePlay(NA_SE0_5C, pl->obj);
		}
		pldemo_8025733C(pl);
		break;
	case 2:
		frame = PL_SetAnime(pl, ANIME_94);
		if ((frame >= 18 && frame < 55) || (frame >= 112 && frame < 134))
		{
			pl->ctrl->hand = 1;
		}
		if (frame >= 109 && frame < 154) pl->ctrl->eyes = 2;
		pldemo_8025733C(pl);
		break;
	case 3:
		frame = PL_SetAnime(pl, ANIME_55);
		switch (frame)
		{
		case 12: pldemo_802574E8(pl); break;
		case 37:
		case 53: Na_ObjSePlay(NA_SE0_40, pl->obj); break;
		case 82: pldemo_80257548(pl); break;
		}
		pldemo_8025733C(pl);
		break;
	}
	pl->obj->s.ang[1] += 0x8000;
	return FALSE;
}

static int PL_ExecDemo28(PLAYER *pl)
{
	if (pl->timer++ > 15 && pldemo_80258B24(pl, PS_WALK_27, ANIME_86, -32))
	{
		Na_ObjSePlay(NA_SE2_0B_D0, pl->obj);
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		pl->life--;
		pl->recover = 4*7+3;
	}
	pl->power = 0x100;
	return FALSE;
}

static int PL_ExecDemo29(PLAYER *pl)
{
	if (pldemo_80258B24(pl, PS_WAIT_32, ANIME_86, 0))
	{
		Na_ObjSePlay(NA_SE2_0B_D0, pl->obj);
		pl->life--;
		pl->recover = 4*7+3;
	}
	pl->power = 0x100;
	return FALSE;
}

static int PL_ExecDemo2A(PLAYER *pl)
{
	if (pldemo_80258B24(pl, PS_WALK_27, ANIME_86, 0))
	{
		Na_ObjSePlay(NA_SE2_0B_D0, pl->obj);
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		pl->life--;
		pl->recover = 4*7+3;
	}
	pl->power = 0x100;
	return FALSE;
}

static int PL_ExecDemo2B(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	PL_TrigSound(pl, NA_SE2_04, PL_VOICE);
	if (pl->timer++ < 11)
	{
		obj->s.s.flag &= ~SHP_ACTIVE;
		return FALSE;
	}
	if (pldemo_80258B24(pl, PS_DEMO_27, ANIME_77, -24))
	{
		pl->recover = 4*7+3;
		pl->code = 1;
	}
	pl->effect |= PE_00000008;
	obj->s.ang[1] += 0x8000;
	obj->s.s.flag |= SHP_ACTIVE;
	return FALSE;
}

static int PL_ExecDemo2C(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	if (pl->timer++ < 11)
	{
		obj->s.s.flag &= ~SHP_ACTIVE;
		return FALSE;
	}
	if (pldemo_80258B24(pl, PS_WALK_20, ANIME_2, -24))
	{
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		pl->life--;
		pl->recover = 4*7+3;
	}
	obj->s.s.flag |= SHP_ACTIVE;
	pl->power = 0x100;
	return FALSE;
}

static int PL_ExecDemo32(PLAYER *pl)
{
	pldemo_80258B24(pl, PS_DEMO_33, ANIME_86, 0);
	if (pl->pos[1] < pl->water-100) PL_EnterWater(pl);
	return FALSE;
}

static int PL_ExecDemo33(PLAYER *pl)
{
	PL_TrigLandEffect(pl, NA_SE0_08);
	PL_SetAnime(pl, ANIME_87);
	PL_Stop(pl);
	if (PL_IsAnimeLast1F(pl))
	{
		GmInitMessage(0);
		PL_SetState(pl, PS_WAIT_01, 0);
	}
	return FALSE;
}

static int PL_ExecDemo35(PLAYER *pl)
{
	float height, scale, dx, dz, dist, speed;
	dx = pl->attach->o_posx - pl->pos[0];
	dz = pl->attach->o_posz - pl->pos[2];
	dist = DIST2(dx, dz);
	speed = dist > 20 ? 20/2.0F : dist/2.0F;
	if (speed < 0.5F) speed = 0;
	switch (pl->phase)
	{
	case 0:
		height = 512 - (pl->pos[1]-pl->ground_y);
		pl->vel[1] = height > 0 ? sqrtf(4*height+1)-1 : 2;
		pl->phase = 1;
		pl->timer = 100;
		FALLTHROUGH;
	case 1:
		pl->ang[1] = ATAN2(dz, dx);
		PL_SetSpeed(pl, speed);
		if (PL_SetAnime(pl, ANIME_111) == 0) Na_ObjSePlay(NA_SE0_37, pl->obj);
		pl->flag &= ~PL_00000100;
		PL_ProcJump(pl, 0);
		if (pl->vel[1] <= 0) pl->phase = 2;
		break;
	case 2:
	case 3:
		pl->ang[1] = ATAN2(dz, dx);
		PL_SetSpeed(pl, speed);
		pl->flag &= ~PL_00000100;
		if (PL_ProcJump(pl, 0) == JUMP_LAND)
		{
			PL_Fade(pl, FADE_2);
#ifdef MOTOR
			motor_8024C834(15, 80);
#endif
			pl->phase = 4;
		}
		if (pl->phase == 2)
		{
			if (pl->obj->s.skel.frame == 0) pl->phase = 3;
		}
		else
		{
			PL_TrigSound(pl, NA_SE0_46, PL_SOUND);
			PL_SetAnime(pl, ANIME_136);
			pl->obj->s.ang[0] = ATAN2(pl->speed, -pl->vel[1]);
		}
		pl->press = -1;
		if (pl->timer > 10)
		{
			pl->timer -= 6;
			scale = (float)pl->timer / 100;
			FVecSet(pl->obj->s.scale, scale, scale, scale);
		}
		break;
	case 4:
		PL_Stop(pl);
		pl->obj->s.s.flag |= SHP_OBJHIDE;
		break;
	}
	return FALSE;
}

static int PL_ExecDemo34(PLAYER *pl)
{
	PL_TrigEffect(pl, pl->flag & PL_METALCAP ? NA_SE0_28 : NA_SE0_00, TRUE);
	PL_TrigJumpVoice(pl);
	if (pl->phase == 0)
	{
		float dx = pl->attach->o_posx - pl->pos[0];
		float dz = pl->attach->o_posz - pl->pos[2];
		float dist = DIST2(dx, dz);
		pl->vel[1] = 60;
		pl->ang[1] = ATAN2(dz, dx);
		PL_SetSpeed(pl, dist / 20);
		pl->flag &= ~PL_00000100;
		pl->phase = 1;
	}
	PL_SetAnime(pl, ANIME_80);
	PL_ProcJump(pl, 0);
	if (pl->vel[1] <= 0) PL_SetState(pl, PS_DEMO_35, 0);
	return FALSE;
}

static int PL_ExecDemo36(PLAYER *pl)
{
	PL_TrigSound(pl, NA_SE0_57, PL_SOUND);
	PL_SetAnime(pl, pl->prevstate == PS_WAIT_20 ? ANIME_152 : ANIME_194);
#ifdef MOTOR
	if (pl->timer == 0)
	{
		motor_8024C834(30, 70);
		motor_8024C89C(2);
	}
#endif
	pl->flag |= PL_00000080;
	if (pl->timer < 32) pl->alpha = 8*(31-pl->timer);
	if (pl->timer++ == 20) PL_Fade(pl, FADE_5);
	PL_Stop(pl);
	return FALSE;
}

static int PL_ExecDemo37(PLAYER *pl)
{
	PL_TrigSound(pl, NA_SE0_57, PL_SOUND);
	PL_SetAnime(pl, ANIME_194);
#ifdef MOTOR
	if (pl->timer == 0)
	{
		motor_8024C834(30, 70);
		motor_8024C89C(2);
	}
#endif
	if (pl->timer < 32)
	{
		pl->flag |= PL_00000080;
		pl->alpha = 8*pl->timer;
	}
	else
	{
		pl->flag &= ~PL_00000080;
	}
	if (pl->timer++ == 32)
	{
		if (pl->pos[1] < pl->water-100)
		{
			if (pl->scene->cam->mode != 8)
			{
				camera_80286188(pl->scene->cam, 8, 1);
			}
			PL_SetState(pl, PS_SWIM_00, 0);
		}
		else
		{
			PL_SetState(pl, PS_WAIT_01, 0);
		}
	}
	PL_Stop(pl);
	return FALSE;
}

static int PL_ExecDemo38(PLAYER *pl)
{
	PL_TrigSound(pl, NA_SE2_10, PL_SOUND);
	Na_ObjSePlay(NA_SE1_16, pl->obj);
	camera_8027F590(10);
	if (PL_SetAnime(pl, ANIME_122) == 0)
	{
		pl->timer++;
		pl->flag |= PL_00000040;
	}
	if (pl->code == 0)
	{
		PL_SetSpeed(pl, 0);
		if (PL_ProcJump(pl, 1) == JUMP_LAND)
		{
			PL_PlayLandEffect(pl, NA_SE0_08);
			pl->code = 1;
		}
	}
	else
	{
		if (pl->timer > 5)
		{
			pl->invincible = 30;
			PL_SetState(pl, pl->power < 0x100 ? PS_DEMO_13 : PS_WAIT_01, 0);
		}
		PL_Stop(pl);
	}
	return FALSE;
}

static int PL_ExecDemo39(PLAYER *pl)
{
	UNUSED int i;
	float scale, gap;
	SHORT angy;
	int eject = FALSE;
	if ((gap = pl->roof_y-pl->ground_y) < 0) gap = 0;
	switch (pl->phase)
	{
	case 0:
		if (gap > 160)
		{
			pl->press = 0;
			return PL_SetState(pl, PS_WAIT_01, 0);
		}
		pl->press = -1;
		if (gap >= 10.1F)
		{
			scale = gap/160;
			FVecSet(pl->obj->s.scale, 2-scale, scale, 2-scale);
		}
		else
		{
			if (!(pl->flag & PL_METALCAP) && !pl->invincible)
			{
				PL_Damage(pl, 3);
				PL_TrigSound(pl, NA_SE2_0A, PL_VOICE);
			}
			FVecSet(pl->obj->s.scale, 1.8, 0.05, 1.8F);
#ifdef MOTOR
			motor_8024C834(10, 80);
#endif
			pl->phase = 1;
		}
		break;
	case 1:
		if (gap >= 30) pl->phase = 2;
		break;
	case 2:
		if (++pl->timer >= 15)
		{
			if (pl->power < 0x100)
			{
				PL_Fade(pl, FADE_DIE);
				PL_SetState(pl, PS_DEMO_00, 0);
			}
			else if (!pl->damage)
			{
				pl->press = 30;
				PL_SetState(pl, PS_WAIT_01, 0);
			}
		}
		break;
	}
	if (pl->ground && pl->ground->ny < 0.5F)
	{
		angy = ATAN2(pl->ground->nz, pl->ground->nx);
		eject = TRUE;
	}
	if (pl->roof && -0.5F < pl->roof->ny)
	{
		angy = ATAN2(pl->roof->nz, pl->roof->nx);
		eject = TRUE;
	}
	if (eject)
	{
		pl->vel[0] = 10 * SIN(angy);
		pl->vel[2] = 10 * COS(angy);
		pl->vel[1] = 0;
		if (PL_ProcWalk(pl) == WALK_FALL)
		{
			pl->press = 0;
			PL_SetState(pl, PS_WAIT_01, 0);
			return FALSE;
		}
	}
	if (pl->code++ > 300)
	{
		pl->power = 0xFF;
		pl->damage = 0;
		PL_Fade(pl, FADE_DIE);
		PL_SetState(pl, PS_DEMO_00, 0);
	}
	PL_Stop(pl);
	PL_SetAnime(pl, ANIME_14);
	return FALSE;
}

static int PL_ExecDemo3D(PLAYER *pl)
{
	int frame = PL_SetAnime(pl, ANIME_54);
	if (frame == 0) objectlib_802A4704();
	if (frame == 28) pldemo_80257548(pl);
	if (PL_IsAnimeLast1F(pl))
	{
		PL_SetState(pl, PS_WAIT_01, 0);
		objectlib_802A4728();
	}
	PL_ProcWait(pl);
	return FALSE;
}

static void pldemo_8025AEA8(
	PLAYER *pl, int anime, int frame2, int frame3, int frame4, u32 state
)
{
	int frame = PL_SetAnime(pl, anime);
	if (pl->status & PA_JUMPREQ)
	{
		pl->timer++;
		if (pl->timer >= 5)
		{
			if (frame < frame2-1)
			{
				frame = frame2-1;
				PL_SetAnimeFrame(pl, frame);
			}
		}
	}
	PL_Stop(pl);
	if (frame == -1)
	{
		PL_PlayEffect(pl, NA_SE0_48, TRUE);
	}
	else if (frame == frame2)
	{
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		PL_PlayEffect(pl, NA_SE0_43, TRUE);
	}
	else if (frame == frame3 || frame == frame4)
	{
		PL_PlayLandEffect(pl, NA_SE0_08);
	}
	if (PL_IsAnimeLast1F(pl)) PL_SetState(pl, state, 0);
}

static int PL_ExecDemo3A(PLAYER *pl)
{
	pldemo_8025AEA8(pl, ANIME_57, 96, 105, 135, PS_WAIT_01);
	return FALSE;
}

static int PL_ExecDemo3B(PLAYER *pl)
{
	pldemo_8025AEA8(pl, ANIME_62, 127, 136, -2, PS_WAIT_3C);
	return FALSE;
}

static int PL_ExecDemo3C(PLAYER *pl)
{
	pldemo_8025AEA8(pl, ANIME_85, 116, 129, -2, PS_WAIT_01);
	return FALSE;
}

static void pldemo_8025B0F8(PLAYER *pl)
{
	pl->phase = 0;
	pl->timer = 0;
	pl->code++;
}

static void PL_Demo01_0(PLAYER *pl)
{
	hud.flag = 0;
	pl->camera->demo = 9;
	pl->obj->s.s.flag &= ~SHP_ACTIVE;
	pldemo_8025B0F8(pl);
}

static void PL_Demo01_1(PLAYER *pl)
{
	if (pl->camera->demo != 9)
	{
		if (pl->timer++ == NTSCPAL(37, 47))
		{
			demo_pipe = ObjMakeAt(
				object, 0, S_PIPE, obj_13002A48, -1328, 60, 4664, 0, 180, 0
			);
			pldemo_8025B0F8(pl);
		}
	}
}

static void PL_Demo01_2(PLAYER *pl)
{
	demo_pipe->o_posy = camera_80289B0C(demo_pipe->o_posy, 260, 10);
	if (pl->timer == 0) Na_ObjSePlay(NA_SE7_17, demo_pipe);
	if (pl->timer++ == NTSCPAL(38, 28))
	{
		pl->vel[1] = 60;
		pldemo_8025B0F8(pl);
	}
}

static void PL_Demo01_3(PLAYER *pl)
{
	if (pl->timer == 25) hud.flag = HUD_ALL;
	if (pl->timer++ >= 118)
	{
		pl->obj->s.s.flag |= SHP_ACTIVE;
#if REVISION == 199703
		PL_TrigSound(pl, NA_SE0_44_A0, PL_SOUND);
		PL_TrigSound(pl, NA_SE2_04, PL_VOICE);
#else
		PL_TrigSound(pl, NA_SE2_04, PL_VOICE);
#if REVISION >= 199609
		PL_TrigSound(pl, NA_SE0_44_A0, PL_SOUND);
#endif
#endif
		PL_SetAnime(pl, ANIME_77);
		PL_SetSpeed(pl, 10);
		if (PL_ProcJump(pl, 0) == JUMP_LAND)
		{
			Na_OpeningUnlockSe();
			PL_PlayLandEffect(pl, NA_SE0_08);
#if REVISION >= 199609
			Na_ObjSePlay(NA_SE2_11_80, pl->obj);
#endif
			pldemo_8025B0F8(pl);
		}
	}
}

static void PL_Demo01_4(PLAYER *pl)
{
	PL_SetAnime(pl, ANIME_78);
	if (PL_IsAnimeLast1F(pl)) pldemo_8025B0F8(pl);
	PL_Stop(pl);
}

static void PL_Demo01_5(PLAYER *pl)
{
	if (pl->timer++ == 0)
	{
		Na_ObjSePlay(NA_SE7_16, demo_pipe);
		PL_SetAnime(pl, ANIME_194);
	}
	demo_pipe->o_posy -= 5;
	if (demo_pipe->o_posy <= 50)
	{
		ObjKill(demo_pipe);
		pldemo_8025B0F8(pl);
	}
	PL_Stop(pl);
}

static void PL_Demo01_6(PLAYER *pl)
{
	if (!camerap->demo)
	{
		camera_8033C848 &= ~0x2000;
		PL_SetState(pl, PS_WAIT_01, 0);
	}
	PL_Stop(pl);
}

static int PL_ExecDemo01(PLAYER *pl)
{
	switch (pl->code)
	{
	case 0: PL_Demo01_0(pl); break;
	case 1: PL_Demo01_1(pl); break;
	case 2: PL_Demo01_2(pl); break;
	case 3: PL_Demo01_3(pl); break;
	case 4: PL_Demo01_4(pl); break;
	case 5: PL_Demo01_5(pl); break;
	case 6: PL_Demo01_6(pl); break;
	}
	return FALSE;
}

static void PL_Demo09_0(PLAYER *pl)
{
	if (pl->phase == 0)
	{
		pl->status |= PA_JUMPSTA;
		pl->flag |= PL_WINGCAP|PL_HEADCAP;
		pl->ang[1] = -0x8000;
		pl->pos[0] = 0;
		pl->pos[2] = 0;
		PL_SetSpeed(pl, 0);
		PL_SetAnime(pl, ANIME_86);
		if (PL_ProcJump(pl, 1) == JUMP_LAND)
		{
			AudPlayStageBGM(NA_BGM_FINALCLEAR);
			PL_PlayLandEffect(pl, NA_SE0_08);
			pl->phase++;
		}
	}
	else
	{
		PL_SetAnime(pl, ANIME_87);
		if (PL_IsAnimeLast1F(pl))
		{
			pl->camera->demo = 10;
			pldemo_8025B0F8(pl);
		}
	}
}

static int PL_Demo09_1(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	if (pl->phase == 0)
	{
		PL_SetAnime(pl, ANIME_37);
		obj->o_f7 = 0;
		if (PL_IsAnimeLast2F(pl))
		{
			PL_PlayLandEffect(pl, NA_SE0_08);
			pl->phase++;
		}
	}
	else
	{
		int frame = PL_SetAnime(pl, ANIME_38);
		if (frame == 3 || frame == 28 || frame == 60)
		{
			PL_PlayEffect(pl, NA_SE0_00, TRUE);
		}
		if (frame >= 3) obj->o_f7 -= 32;
		switch (frame)
		{
		case  3: Na_ObjSePlay(Na_Se2_00(), pl->obj); break;
		case 28: Na_ObjSePlay(NA_SE2_03, pl->obj); break;
		case 60: Na_ObjSePlay(NA_SE2_04, pl->obj); break;
		}
		pl->effect |= PE_00000008;
		if (PL_IsAnimeLast2F(pl)) pldemo_8025B0F8(pl);
	}
	FVecSet(pl->pos, 0, 307, obj->o_f7);
	PL_UseAnimePos(pl);
	FVecCpy(obj->s.pos, pl->pos);
	SVecSet(obj->s.ang, 0, pl->ang[1], 0);
	return FALSE;
}

static BSPLINE pldemo_8032DB5C[] =
{
	{20, {    0,  678, -2916}},
	{30, {    0,  680, -3500}},
	{40, { 1000,  700, -4000}},
	{50, { 2500,  750, -3500}},
	{50, { 3500,  800, -2000}},
	{50, { 4000,  850,     0}},
	{50, { 3500,  900,  2000}},
	{50, { 2000,  950,  3500}},
	{50, {    0, 1000,  4000}},
	{50, {-2000, 1050,  3500}},
	{50, {-3500, 1100,  2000}},
	{50, {-4000, 1150,     0}},
	{50, {-3500, 1200, -2000}},
	{50, {-2000, 1250, -3500}},
	{50, {    0, 1300, -4000}},
	{50, { 2000, 1350, -3500}},
	{50, { 3500, 1400, -2000}},
	{50, { 4000, 1450,     0}},
	{50, { 3500, 1500,  2000}},
	{50, { 2000, 1600,  3500}},
	{50, {    0, 1700,  4000}},
	{50, {-2000, 1800,  3500}},
	{50, {-3500, 1900,  2000}},
	{30, {-4000, 2000,     0}},
	{ 0, {-3500, 2100, -2000}},
	{ 0, {-2000, 2200, -3500}},
	{ 0, {    0, 2300, -4000}},
};

static int PL_Demo09_2(PLAYER *pl)
{
	FVEC pos;
	UNUSED OBJECT *obj = pl->obj;
	switch (pl->phase)
	{
	case 0:
		PL_SetAnime(pl, ANIME_42);
		BSplineInit(pldemo_8032DB5C);
		pl->phase++;
		FALLTHROUGH;
	case 1:
		if (BSplineProc(pos))
		{
			PL_SetState(pl, PS_JUMP_0C, 0);
			pl->phase++;
		}
		else
		{
			float dx = pos[0] - pl->pos[0];
			float dy = pos[1] - pl->pos[1];
			float dz = pos[2] - pl->pos[2];
			float dist = DIST2(dx, dz);
			SHORT angy = ATAN2(dz, dx);
			FVecCpy(pl->pos, pos);
			pl->obj->s.ang[0] = -ATAN2(dist, dy);
			pl->obj->s.ang[1] = angy;
			pl->obj->s.ang[2] = 20 * (short)(pl->ang[1]-angy);
			pl->ang[1] = angy;
		}
		break;
	case 2:
		PL_SetState(pl, PS_JUMP_0C, 0);
		break;
	}
	pl->ctrl->hand = 5;
	FVecCpy(pl->obj->s.pos, pl->pos);
	pl->effect |= PE_00000008;
	if (pl->timer++ == 500) PL_Fade(pl, FADE_FINAL);
	return FALSE;
}

static int PL_ExecDemo09(PLAYER *pl)
{
	switch (pl->code)
	{
	case 0: PL_Demo09_0(pl); break;
	case 1: PL_Demo09_1(pl); break;
	case 2: PL_Demo09_2(pl); break;
	}
	return FALSE;
}

static void pldemo_8025BC80(SHORT posx, SHORT posy, SHORT posz, float dist)
{
	static int angx = 0;
	static int angy = 0;
	SHORT dx = dist * COS(angx)*SIN(angy);
	SHORT dy = dist * SIN(angx);
	SHORT dz = dist * COS(angx)*COS(angy);
	ObjMakeAt(object, 0, 0, obj_13002AF0, posx+dx, posy+dy, posz+dz, 0, 0, 0);
	dx = dx * 4/3;
	dx = dy * 4/3;
	dx = dz * 4/3;
	ObjMakeAt(object, 0, 0, obj_13002AF0, posx-dx, posy-dy, posz-dz, 0, 0, 0);
	angx += 0x3800;
	angy += 0x6000;
}

static float pldemo_8025BEB8(OBJECT *obj)
{
	BGFACE *ground;
	SVEC pos;
	float posx, posy, posz;
	ObjGetAnimePos(obj, obj->s.ang[1], pos);
	posx = obj->s.pos[0] + pos[0];
	posy = obj->s.pos[1] + 10;
	posz = obj->s.pos[2] + pos[2];
	return BGCheckGround(posx, posy, posz, &ground);
}

static void PL_Demo18_0(PLAYER *pl)
{
	if (pl->timer == 1) pl->camera->demo = 11;
	pl->status |= PA_JUMPSTA;
	pl->flag |= PL_WINGCAP|PL_HEADCAP;
	PL_SetAnime(pl, ANIME_86);
	PL_SetSpeed(pl, 0);
	if (PL_ProcJump(pl, 0) == JUMP_LAND)
	{
		PL_PlayLandEffect(pl, NA_SE0_08);
		pldemo_8025B0F8(pl);
	}
}

static void PL_Demo18_1(PLAYER *pl)
{
	PL_SetAnime(pl, ANIME_87);
	PL_Stop(pl);
	if (PL_IsAnimeLast1F(pl))
	{
		pl->cap_timer = 60;
		demo_star = ObjMakeAt(
			object, 0, S_POWERSTAR, obj_13002A48, 0, 2528, -1800, 0, 0, 0
		);
		ObjSetScale(demo_star, 3);
		pldemo_8025B0F8(pl);
	}
}

static void PL_Demo18_2(PLAYER *pl)
{
	PL_SetAnime(pl, pl->phase == 0 ? ANIME_32 : ANIME_33);
	if (pl->phase == 0 && PL_IsAnimeLast2F(pl)) pl->phase++;
	if (pl->timer == 90) AudPlayStageBGM(NA_BGM_ENDING);
	if (pl->timer == 255) pldemo_8025B0F8(pl);
	demo_star->o_shapeangy += 0x400;
	pldemo_8025BC80(0, 2528, -1800, 250);
	Na_ObjSePlay(NA_SE6_0B, demo_star);
}

#if REVISION >= 199707
#define EXTEND 1
#else
#define EXTEND 0
#endif

static void PL_Demo18_3(PLAYER *pl)
{
	if (pl->timer == 1) SnWipe(WIPE_FADE_OUT, 14, 0xFF, 0xFF, 0xFF);
	if (pl->timer == 2) Na_FixSePlay(NA_SE7_1E);
	if (pl->timer == 44) SnWipe(WIPE_FADE_IN, 192, 0xFF, 0xFF, 0xFF);
	if (pl->timer == 40)
	{
		ObjKill(demo_star);
		demo_peach = ObjMakeAt(
			object, 0, 222, obj_13000EAC, 0, 2428, -1300, 0, 0, 0
		);
		camera_8032DF24 = demo_peach;
		demo_toadA = ObjMakeAt(
			object, 0, 221, obj_13000E88, +200, 906, -1290, 0, 0, 0
		);
		demo_toadB = ObjMakeAt(
			object, 0, 221, obj_13000E88, -200, 906, -1290, 0, 0, 0
		);
		demo_peach->o_alpha = 0x7F;
		demo_toadA->o_alpha = 0xFF;
		demo_toadB->o_alpha = 0xFF;
		peach_eyes = 4;
		peach_anime = 4;
		toad_anime[0] = 4;
		toad_anime[1] = 5;
	}
	if (pl->timer > NTSCPAL(275, 200)) demo_peach->o_alpha =
		camera_80289B0C(demo_peach->o_alpha, 0xFF, 2);
	if (pl->timer >= 40) pldemo_8025BC80(0, 2628, -1300, 150);
	if (pl->timer == NTSCPAL(355+45*EXTEND, 280)) pldemo_8025B0F8(pl);
	if (pl->timer >= 40) Na_ObjSePlay(NA_SE6_0B, demo_peach);
}

static void PL_Demo18_4(PLAYER *pl)
{
	pldemo_8025BC80(0, demo_peach->o_posy, -1300, 150);
	if (demo_peach->o_posy >= 1300)
	{
		if (pl->phase < 60) pl->phase += 5;
	}
	else
	{
		if (pl->phase > 26) pl->phase -= 2;
		PL_SetAnime(pl, ANIME_31);
	}
	if ((demo_peach->o_posy -= pl->phase/10) <= 907)
	{
		demo_peach->o_posy = 906;
	}
	Na_ObjSePlay(NA_SE6_0B, demo_peach);
	if (pl->timer > NTSCPAL(583, 530)) pldemo_8025B0F8(pl);
}

static void PL_Demo18_5(PLAYER *pl)
{
	BGFACE *ground;
	if (pl->timer == 22) peach_anime = 5;
	if ((pl->pos[2] -= 20) <= -1181)
	{
		pl->pos[2] = -1180;
		pldemo_8025B0F8(pl);
	}
	pl->pos[1] = BGCheckGround(pl->pos[0], pl->pos[1], pl->pos[2], &ground);
	PL_SetAnimeV(pl, ANIME_114, VSPEED(8));
	plwalk_80263EE4(pl, 9, 45);
	FVecCpy(pl->obj->s.pos, pl->pos);
	pl->effect |= PE_00000001;
}

#define CAPTION_X (SCREEN_WD/2)
#define CAPTION_Y (SCREEN_HT-13)

static void PL_Demo18_6(PLAYER *pl)
{
	int frame = PL_SetAnime(pl, pl->phase == 0 ? ANIME_34 : ANIME_30);
	if (pl->phase == 0)
	{
		if (frame == 8) pldemo_802574E8(pl);
		if (PL_IsAnimeLast1F(pl)) pl->phase++;
	}
	switch (pl->timer)
	{
	case 80+30*EXTEND:
		peach_anime = 6;
		break;
	case 81+30*EXTEND:
		peach_eyes = 3;
		break;
	case 145+30*EXTEND:
		peach_eyes = 2;
		break;
	case 228+30*EXTEND:
		peach_eyes = 1;
		pldemo_8032DB48 = 1;
		break;
	case 230+30*EXTEND:
		CaptionOpen(CAPTION_X, CAPTION_Y, 0, 30);
#if REVISION >= 199609
		Na_SeqMute(NA_HANDLE_BGM, 60, 40);
		Na_ObjSePlay(NA_SE2_38, demo_peach);
#endif
		break;
	case 275+30*EXTEND:
		peach_eyes = 0;
		pldemo_8032DB48 = 0;
		break;
	case 290+30*EXTEND:
		CaptionOpen(CAPTION_X, CAPTION_Y, 1, 60);
#if REVISION >= 199609
		Na_ObjSePlay(NA_SE2_39, demo_peach);
#endif
		break;
	case 480+30*EXTEND:
		pldemo_8025B0F8(pl);
		break;
	}
}

static void PL_Demo18_7(PLAYER *pl)
{
	peach_anime = 9;
	switch (pl->timer)
	{
	case 29+10*EXTEND:
		CaptionOpen(CAPTION_X, CAPTION_Y, 2, 30);
#if REVISION >= 199609
		Na_ObjSePlay(NA_SE2_3A, demo_peach);
#endif
		break;
	case 45+20*EXTEND:
		pldemo_8032DB48 = 1;
		break;
	case 75+30*EXTEND:
		CaptionOpen(CAPTION_X, CAPTION_Y, 3, 30);
#if REVISION >= 199609
		Na_ObjSePlay(NA_SE2_3B, demo_peach);
#endif
		break;
	case NTSCPAL(130+40*EXTEND, 150):
		CaptionOpen(CAPTION_X, CAPTION_Y, 4, 40);
#if REVISION >= 199609
		Na_ObjSePlay(NA_SE2_3C, demo_peach);
#endif
		break;
	case NTSCPAL(200+50*EXTEND, 260):
		pldemo_8025B0F8(pl);
		break;
	}
}

static void PL_Demo18_8(PLAYER *pl)
{
	static u8 eyestab[] = {2,2,3,3,2,2,1,1,2,2,3,3,2,2,1,1,2,2,3,3};
	peach_anime = 10;
	if (pl->timer >= 90)
	{
		pl->ctrl->eyes = pl->timer < 90+20 ? eyestab[pl->timer-90] : 2;
	}
	switch (pl->timer)
	{
	case   8: pldemo_8032DB48 = 0; break;
	case  10: peach_eyes = 3; break;
	case  50: peach_eyes = 4; break;
	case  75: pl->ctrl->eyes = 2; break;
	case  76: pl->ctrl->eyes = 3; break;
	case 100: peach_eyes = 3; break;
	case 136: peach_eyes = 0; break;
	case 140: pldemo_8025B0F8(pl); break;
	}
}

static void PL_Demo18_9(PLAYER *pl)
{
	int frame = PL_SetAnime(pl, ANIME_39);
	if (frame == 77) pldemo_80257548(pl);
	if (frame == 88) Na_ObjSePlay(NA_SE2_0C, pl->obj);
	if (frame >= 98) pl->ctrl->hand = 2;
	if (pl->timer < 52) pl->ctrl->eyes = 2;
	switch (pl->timer)
	{
	case  70: peach_eyes = 1; break;
	case  86: peach_eyes = 2; break;
	case  90: peach_eyes = 3; break;
	case 120: peach_eyes = 0; break;
	case 140:
#if REVISION >= 199609
		Na_SeqUnmute(NA_HANDLE_BGM, 60);
#endif
		AudPlayStageBGM(NA_BGM_STAFF);
		break;
	case 142:
		pldemo_8025B0F8(pl);
		break;
	}
}

static void PL_Demo18_10(PLAYER *pl)
{
	PL_SetAnime(pl, ANIME_194);
	demo_peach->o_posy = pldemo_8025BEB8(demo_peach);
	demo_toadA->o_posy = pldemo_8025BEB8(demo_toadA);
	demo_toadB->o_posy = pldemo_8025BEB8(demo_toadB);
	switch (pl->timer)
	{
	case 1:
		peach_anime = 0;
		toad_anime[0] = 0;
		toad_anime[1] = 2;
		pldemo_8032DB48 = 1;
		CaptionOpen(CAPTION_X, CAPTION_Y, 5, 30);
#if REVISION >= 199609
		Na_ObjSePlay(NA_SE2_3D, demo_peach);
#endif
		break;
	case 55:
		CaptionOpen(CAPTION_X, CAPTION_Y, 6, 40);
		break;
	case 130:
		CaptionOpen(CAPTION_X, CAPTION_Y, 7, 50);
#if REVISION >= 199609
		Na_ObjSePlay(NA_SE2_3E, demo_peach);
#endif
		break;
	}
	if (pl->timer == 350) pldemo_8025B0F8(pl);
}

static void PL_Demo18_11(PLAYER *pl)
{
	PL_SetAnime(pl, pl->phase == 0 ? ANIME_35 : ANIME_36);
	pl->obj->s.pos[1] = pldemo_8025BEB8(pl->obj);
	if (pl->phase == 0 && PL_IsAnimeLast2F(pl)) pl->phase = 1;
	if (pl->timer == 95)
	{
		CaptionOpen(CAPTION_X, CAPTION_Y, 0, 40);
#if REVISION >= 199609
		Na_ObjSePlay(NA_SE2_3F, demo_peach);
#endif
	}
	if (pl->timer == 389) pldemo_8025B0F8(pl);
}

static void PL_Demo18_12(PLAYER *pl)
{
	if (pl->phase == 0)
	{
		PL_Fade(pl, FADE_STAFF);
		pool_entry = 1500;
		pl->phase = 1;
	}
}

static int PL_ExecDemo18(PLAYER *pl)
{
	switch (pl->code)
	{
	case  0: PL_Demo18_0(pl); break;
	case  1: PL_Demo18_1(pl); break;
	case  2: PL_Demo18_2(pl); break;
	case  3: PL_Demo18_3(pl); break;
	case  4: PL_Demo18_4(pl); break;
	case  5: PL_Demo18_5(pl); break;
	case  6: PL_Demo18_6(pl); break;
	case  7: PL_Demo18_7(pl); break;
	case  8: PL_Demo18_8(pl); break;
	case  9: PL_Demo18_9(pl); break;
	case 10: PL_Demo18_10(pl); break;
	case 11: PL_Demo18_11(pl); break;
	case 12: PL_Demo18_12(pl); break;
	}
	pl->timer++;
	demo_vp.vp.vscale[0] = 4*(SCREEN_WD/2);
	demo_vp.vp.vscale[1] = 4*(SCREEN_HT/2*3/4);
	demo_vp.vp.vtrans[0] = 4*(SCREEN_WD/2);
	demo_vp.vp.vtrans[1] = 4*(SCREEN_HT/2);
	SnSetVp(NULL, &demo_vp, 0x00, 0x00, 0x00);
	return FALSE;
}

static int PL_ExecDemo19(PLAYER *pl)
{
	pl->camera->demo = 13;
	if (pl->pos[1] < pl->water-100)
	{
		if (pl->scene->cam->mode != 3) camera_80286188(pl->scene->cam, 3, 1);
		PL_SetAnime(pl, ANIME_178);
		FVecCpy(pl->obj->s.pos, pl->pos);
		SVecCpy(pl->obj->s.ang, pl->ang);
		pl->effect |= PE_00000020;
	}
	else
	{
		PL_SetAnime(pl, ANIME_194);
		if (pl->timer > 0) PL_Stop(pl);
	}
	if (pl->timer > NTSCPAL(60, 50))
	{
		int x, y;
		if (pl->phase < 40) pl->phase += 2;
		x = 4*(SCREEN_WD/2) * pl->phase/100;
		y = 4*(SCREEN_HT/2) * pl->phase/100;
		demo_vp.vp.vscale[0] = 4*(SCREEN_WD/2) - x;
		demo_vp.vp.vscale[1] = 4*(SCREEN_HT/2) - y;
		demo_vp.vp.vtrans[0] =
			4*(SCREEN_WD/2) + (staffp->flag & STAFF_R ? x : -x) * 56/100;
		demo_vp.vp.vtrans[1] =
			4*(SCREEN_HT/2) + (staffp->flag & STAFF_B ? y : -y) * 66/100;
		SnSetVp(&demo_vp, NULL, 0x00, 0x00, 0x00);
	}
	if (pl->timer == NTSCPAL(90, 80)) StaffClear();
	if (pl->timer >= NTSCPAL(90, 80)) staffdrawp = staffp;
	if (pl->timer++ == NTSCPAL(200+4*EXTEND, 160)) PL_Fade(pl, FADE_STAFF);
	pl->obj->s.ang[1] += (staffp->flag & 0xC0) << 8;
	return FALSE;
}

static int PL_ExecDemo1A(PLAYER *pl)
{
	if (pl->phase == 0)
	{
		pl->camera->demo = 12;
		demo_peach =
			ObjMakeAt(object, 0, 222, obj_13000EAC,   60, 906, -1180, 0, 0, 0);
		demo_toadA =
			ObjMakeAt(object, 0, 221, obj_13000E88, +180, 906, -1170, 0, 0, 0);
		demo_toadB =
			ObjMakeAt(object, 0, 221, obj_13000E88, -180, 906, -1170, 0, 0, 0);
		demo_peach->o_alpha = 0xFF;
		demo_toadA->o_alpha = 0xFF;
		demo_toadB->o_alpha = 0xFF;
		peach_anime = 11;
		toad_anime[0] = 6;
		toad_anime[1] = 7;
		pl->phase = 1;
	}
	PL_SetAnime(pl, ANIME_29);
	PL_Stop(pl);
	pl->obj->s.ang[1] += 0x8000;
	pl->obj->s.pos[0] -= 60;
	pl->ctrl->hand = 5;
	if (pl->timer++ == 300) PL_Fade(pl, FADE_ENDING);
	return FALSE;
}

static int pldemo_8025D70C(PLAYER *pl)
{
	if (
		pl->ground->code == BG_35 &&
		pl->state & PF_DMGE && pl->state != PS_DEMO_12
	)
	{
		player_802521A0(pl);
		return PL_SetStateDrop(pl, PS_DEMO_12, 0);
	}
	return FALSE;
}

int PL_ExecDemo(PLAYER *pl)
{
	int result;
	if (pldemo_8025D70C(pl)) return TRUE;
	switch (pl->state)
	{
	case PS_DEMO_00: result = PL_ExecDemo00(pl); break;
	case PS_DEMO_01: result = PL_ExecDemo01(pl); break;
	case PS_DEMO_02: result = PL_ExecDemo02_07(pl); break;
	case PS_DEMO_07: result = PL_ExecDemo02_07(pl); break;
	case PS_DEMO_03: result = PL_ExecDemo03(pl); break;
	case PS_DEMO_04: result = PL_ExecDemo04(pl); break;
	case PS_DEMO_05: result = PL_ExecDemo05(pl); break;
	case PS_DEMO_06: result = PL_ExecDemo06(pl); break;
	case PS_DEMO_0F: result = PL_ExecDemo0F(pl); break;
	case PS_DEMO_08: result = PL_ExecDemo08(pl); break;
	case PS_DEMO_09: result = PL_ExecDemo09(pl); break;
	case PS_DEMO_0A: result = PL_ExecDemo0A(pl); break;
	case PS_DEMO_11: result = PL_ExecDemo11(pl); break;
	case PS_DEMO_12: result = PL_ExecDemo12(pl); break;
	case PS_DEMO_13: result = PL_ExecDemo13(pl); break;
	case PS_DEMO_14: result = PL_ExecDemo14(pl); break;
	case PS_DEMO_15: result = PL_ExecDemo15(pl); break;
	case PS_DEMO_16: result = PL_ExecDemo16(pl); break;
	case PS_DEMO_17: result = PL_ExecDemo17(pl); break;
	case PS_DEMO_18: result = PL_ExecDemo18(pl); break;
	case PS_DEMO_19: result = PL_ExecDemo19(pl); break;
	case PS_DEMO_1A: result = PL_ExecDemo1A(pl); break;
	case PS_DEMO_20:
	case PS_DEMO_21: result = PL_ExecDemo20_21(pl); break;
	case PS_DEMO_22: result = PL_ExecDemo22(pl); break;
	case PS_DEMO_23: result = PL_ExecDemo23(pl); break;
	case PS_DEMO_24: result = PL_ExecDemo24(pl); break;
	case PS_DEMO_25: result = PL_ExecDemo25(pl); break;
	case PS_DEMO_26: result = PL_ExecDemo26(pl); break;
	case PS_DEMO_27: result = PL_ExecDemo27(pl); break;
	case PS_DEMO_28: result = PL_ExecDemo28(pl); break;
	case PS_DEMO_29: result = PL_ExecDemo29(pl); break;
	case PS_DEMO_2A: result = PL_ExecDemo2A(pl); break;
	case PS_DEMO_2B: result = PL_ExecDemo2B(pl); break;
	case PS_DEMO_2C: result = PL_ExecDemo2C(pl); break;
	case PS_DEMO_2D: result = PL_ExecDemo2D(pl); break;
	case PS_DEMO_2E: result = PL_ExecDemo2E(pl); break;
	case PS_DEMO_2F: result = PL_ExecDemo2F(pl); break;
	case PS_DEMO_31: result = PL_ExecDemo31(pl); break;
	case PS_DEMO_32: result = PL_ExecDemo32(pl); break;
	case PS_DEMO_33: result = PL_ExecDemo33(pl); break;
	case PS_DEMO_34: result = PL_ExecDemo34(pl); break;
	case PS_DEMO_35: result = PL_ExecDemo35(pl); break;
	case PS_DEMO_36: result = PL_ExecDemo36(pl); break;
	case PS_DEMO_37: result = PL_ExecDemo37(pl); break;
	case PS_DEMO_38: result = PL_ExecDemo38(pl); break;
	case PS_DEMO_39: result = PL_ExecDemo39(pl); break;
	case PS_DEMO_3A: result = PL_ExecDemo3A(pl); break;
	case PS_DEMO_3B: result = PL_ExecDemo3B(pl); break;
	case PS_DEMO_3C: result = PL_ExecDemo3C(pl); break;
	case PS_DEMO_3D: result = PL_ExecDemo3D(pl); break;
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
