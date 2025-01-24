#include <sm64.h>

#define CHANGE_NULL             0
#define CHANGE_STAGE            1
#define CHANGE_SCENE            2
#define CHANGE_PORT             3

#define GM_NORMAL               0
#define GM_PAUSE                2
#define GM_FREEZE               3
#define GM_EXIT                 4
#define GM_FRAMEADV             5

#include "staff.c"

static STAFF staff_table[] =
{
	{STAGE_GROUNDS, 1, 1,               -0x80,     0,  8000,     0, NULL},
	{STAGE_BOB,     1, 1|STAFF_TL|0x00,  0x75,   713,  3918, -3889, staff_01},
	{STAGE_WF,      1, 2|STAFF_BR|0x00,  0x2E,   347,  5376,   326, staff_02},
	{STAGE_JRB,     1, 2|STAFF_TR|0x00,  0x16,  3800, -4840,  2727, staff_03},
	{STAGE_CCM,     2, 2|STAFF_BL|0x00,  0x19, -5464,  6656, -6575, staff_04},
	{STAGE_BBH,     1, 1|STAFF_TL|0x00,  0x3C,   257,  1922,  2580, staff_05},
	{STAGE_HMC,     1, 1|STAFF_BR|0xC0,  0x7B, -6469,  1616, -6054, staff_06},
	{STAGE_THI,     3, 1|STAFF_TR|0x00, -0x20,   508,  1024,  1942, staff_07},
	{STAGE_LLL,     2, 1|STAFF_BL|0x00,  0x7C,   -73,    82, -1467, staff_08},
	{STAGE_SSL,     1, 1|STAFF_TL|0x40,  0x62, -5906,  1024, -2576, staff_09},
	{STAGE_DDD,     1, 2|STAFF_BR|0x00,  0x2F, -4884, -4607,  -272, staff_10},
	{STAGE_SL,      1, 1|STAFF_TR|0x00, -0x22,  1925,  3328,   563, staff_11},
	{STAGE_WDW,     1, 1|STAFF_BL|0x00,  0x69,  -537,  1850,  1818, staff_12},
	{STAGE_TTM,     1, 2|STAFF_TL|0x00, -0x21,  2613,   313,  1074, staff_13},
	{STAGE_THI,     1, 3|STAFF_BR|0x00,  0x36, -2609,   512,   856, staff_14},
	{STAGE_TTC,     1, 1|STAFF_TR|0x00, -0x48, -1304,   -71,  -967, staff_15},
	{STAGE_RR,      1, 1|STAFF_BL|0x00,  0x40,  1565,  1024,  -148, staff_16},
	{STAGE_SA,      1, 1|STAFF_TL|0x00,  0x18, -1050, -1330, -1559, staff_17},
	{STAGE_COTMC,   1, 1|STAFF_BR|0x00, -0x10,  -254,   415, -6045, staff_18},
	{STAGE_DDD,     2, 1|STAFF_TR|0x80, -0x40,  3948,  1185,  -104, staff_19},
	{STAGE_CCM,     1, 1|STAFF_BL|0x00,  0x1F,  3169, -4607,  5240, staff_20},
	{STAGE_GROUNDS, 1, 1,               -0x80,     0,   906, -1200, NULL},
	{STAGE_NULL,    0, 1,                0x00,     0,     0,     0, NULL},
};

HUD hud;
PLAYER player_data[1];
PLAYER *mario = &player_data[0];

static s16 game_state;
static s16 game_timer;

static short freeze_timer;
static FREEZECALL *freeze_callback;

static PL_ENTRY mario_entry;
static s16 game_result;

static s16 fade_mode;
static s16 fade_timer;
static s16 fade_port;
static u32 fade_code;

UNUSED static s16 game_8032D940 = 0;
UNUSED static s16 game_8033B25C;
static char time_flag;
static char mid_flag = FALSE;

char first_msg;

static void GmSceneProc(short *);

int GmTimeCtrl(int code)
{
	switch (code)
	{
	case 0:
		hud.flag |= HUD_TIME;
		time_flag = FALSE;
		hud.time = 0;
		break;
	case 1:
		time_flag = TRUE;
		break;
	case 2:
		time_flag = FALSE;
		break;
	case 3:
		hud.flag &= ~HUD_TIME;
		time_flag = FALSE;
		hud.time = 0;
		break;
	}
	return hud.time;
}

static int GmCheckPause(void)
{
	int msgopen = MsgGet() >= 0;
	int demo = (mario->state & PF_DEMO) != 0;
	if (!(demo || msgopen || wipe.active || fade_mode != FADE_NULL))
	{
		if (cont1->down & START_BUTTON) return TRUE;
	}
	return FALSE;
}

static void GmSetState(SHORT state)
{
	game_state = state;
	game_timer = 0;
}

static void GmExit(int code)
{
	game_state = GM_EXIT;
	game_timer = 0;
	game_result = code;
}

void GmFadeout(int code, int color)
{
	if (color) color = 0xFF;
	AudFadeout(NA_TIME(16*3/2));
	SnWipe(WIPE_FADE_OUT, 16, color, color, color);
	GmFreeze(30, NULL);
	GmExit(code);
}

UNUSED
static void game_8024982C(void)
{
}

void GmInitMessage(int index)
{
	int flag;
	int msg = scenep->msg[index];
	switch (msg)
	{
	case 129: flag = BuGetFlag() & BU_BLUESW;   break;
	case 130: flag = BuGetFlag() & BU_GREENSW;  break;
	case 131: flag = BuGetFlag() & BU_REDSW;    break;
	case 255: flag = TRUE;                      break;
	default:  flag = BuGetStar(course_index-1); break;
	}
	if (!flag)
	{
		GmFreeze(-1, NULL);
		MsgOpen(msg);
	}
}

static void PL_InitDoor(ACTOR *actor, u32 code)
{
	if (code & 2) actor->ang[1] += 0x8000;
#ifdef sgi
	actor->pos[0] += 300 * SIN(actor->ang[1]);
	actor->pos[2] += 300 * COS(actor->ang[1]);
#else
	actor->pos[0] += (int)(300 * SIN(actor->ang[1]));
	actor->pos[2] += (int)(300 * COS(actor->ang[1]));
#endif
}

static void PL_InitCap(PLAYER *pl)
{
	int index = course_index - COURSE_CAPSW;
	switch (index)
	{
	case COURSE_COTMC - COURSE_CAPSW:
		pl->flag |= PL_HEADCAP|PL_METALCAP;
		pl->cap_timer = 30*20;
		break;
	case COURSE_TOTWC - COURSE_CAPSW:
		pl->flag |= PL_HEADCAP|PL_WINGCAP;
		pl->cap_timer = 30*40;
		break;
	case COURSE_VCUTM - COURSE_CAPSW:
		pl->flag |= PL_HEADCAP|PL_VANISHCAP;
		pl->cap_timer = 30*20;
		break;
	}
}

static void PL_InitState(PLAYER *pl, int type, u32 code)
{
	switch (type)
	{
	case ENTER_DOOR:    PL_SetState(pl, PS_DEMO_22, code); break;
	case ENTER_02:      PL_SetState(pl, PS_WAIT_01, 0); break;
	case ENTER_03:      PL_SetState(pl, PS_DEMO_23, 0); break;
	case ENTER_04:      PL_SetState(pl, PS_DEMO_37, 0); break;
	case ENTER_10:      PL_SetState(pl, PS_WAIT_01, 0); break;
	case ENTER_12:      PL_SetState(pl, PS_DEMO_32, 0); break;
	case ENTER_13:      PL_SetState(pl, PS_JUMP_33, 0); break;
	case ENTER_14:      PL_SetState(pl, PS_DEMO_24, 0); break;
	case ENTER_15:      PL_SetState(pl, PS_DEMO_2A, 0); break;
	case ENTER_16:      PL_SetState(pl, PS_DEMO_24, 0); break;
	case ENTER_17:      PL_SetState(pl, PS_JUMP_19, 2); break;
	case ENTER_11:      PL_SetState(pl, PS_SWIM_00, 1); break;
	case ENTER_20:      PL_SetState(pl, PS_DEMO_26, 0); break;
	case ENTER_21:      PL_SetState(pl, PS_DEMO_28, 0); break;
	case ENTER_22:      PL_SetState(pl, PS_DEMO_2D, 0); break;
	case ENTER_23:      PL_SetState(pl, PS_DEMO_29, 0); break;
	case ENTER_24:      PL_SetState(pl, PS_DEMO_2B, 0); break;
	case ENTER_25:      PL_SetState(pl, PS_DEMO_2C, 0); break;
	}
	PL_InitCap(pl);
}

static void GmInitPort(void)
{
	PORT *port = SnGetPort(mario_entry.port);
	int type = SnGetPortType(port->obj);
	if (mario->state != PS_NULL)
	{
		player_actor[0].pos[0] = port->obj->o_posx;
		player_actor[0].pos[1] = port->obj->o_posy;
		player_actor[0].pos[2] = port->obj->o_posz;
		player_actor[0].ang[0] = 0;
		player_actor[0].ang[1] = port->obj->o_angy;
		player_actor[0].ang[2] = 0;
		if (type == ENTER_DOOR)
		{
			PL_InitDoor(&player_actor[0], mario_entry.code);
		}
		if (
			mario_entry.type == CHANGE_STAGE ||
			mario_entry.type == CHANGE_SCENE
		)
		{
			player_actor[0].scene = mario_entry.scene;
			SnOpenPlayer();
		}
		MarioEnter();
		PL_InitState(mario, type, mario_entry.code);
		mario->collide = port->obj;
		mario->attach = port->obj;
	}
	camera_80286F68(scenep->cam);
	mario_entry.type = CHANGE_NULL;
	fade_mode = FADE_NULL;
	switch (type)
	{
	case ENTER_03:      SnWipe(WIPE_STAR_IN,   16, 0x00, 0x00, 0x00); break;
	case ENTER_DOOR:    SnWipe(WIPE_CIRCLE_IN, 16, 0x00, 0x00, 0x00); break;
	case ENTER_04:      SnWipe(WIPE_FADE_IN,   20, 0xFF, 0xFF, 0xFF); break;
	case ENTER_16:      SnWipe(WIPE_FADE_IN,   26, 0xFF, 0xFF, 0xFF); break;
	case ENTER_14:      SnWipe(WIPE_CIRCLE_IN, 16, 0x00, 0x00, 0x00); break;
	case ENTER_27:      SnWipe(WIPE_FADE_IN,   16, 0x00, 0x00, 0x00); break;
	default:            SnWipe(WIPE_STAR_IN,   16, 0x00, 0x00, 0x00); break;
	}
	if (!demop)
	{
		AudPlayBGM(scenep->bgm_mode, scenep->bgm, 0);
		if (mario->flag & PL_METALCAP) AudPlaySpecialBGM(NA_BGM_METAL);
		if (mario->flag & (PL_WINGCAP|PL_VANISHCAP))
		{
			AudPlaySpecialBGM(NA_BGM_SPECIAL);
		}
#if REVISION > 199606
		if (stage_index == STAGE_BOB)
		{
			if (Na_BgmGet() != NA_BGM_RACE && time_flag)
			{
				Na_BgmPlay(0, NA_BGM_RACE, 0);
			}
		}
#endif
		if (mario_entry.stage == STAGE_INSIDE && mario_entry.scene == 1 &&
#if REVISION > 199606
			(mario_entry.port == 31 || mario_entry.port == 32)
#else
			mario_entry.port == 31
#endif
		) Na_FixSePlay(NA_SE7_1D);
#if REVISION > 199606
		if (mario_entry.stage == STAGE_GROUNDS && mario_entry.scene == 1)
		{
			if (
				mario_entry.port == 7 ||
				mario_entry.port == 10 ||
				mario_entry.port == 20 ||
				mario_entry.port == 30
			) Na_FixSePlay(NA_SE7_1D);
		}
#endif
	}
}

static void GmProcEntry(void)
{
	if (mario_entry.type != CHANGE_NULL)
	{
		if (mario_entry.type == CHANGE_SCENE)
		{
			GmTimeHide();
			SnClosePlayer();
			SceneOpen(mario_entry.scene);
		}
		GmInitPort();
	}
}

static void GmInitStage(void)
{
	stage_index = mario_entry.stage;
	GmTimeHide();
	SceneOpen(mario_entry.scene);
	GmInitPort();
}

static void GmInitStaff(void)
{
	u32 state;
	switch (mario_entry.port)
	{
	case PORT_FINAL:    state = PS_DEMO_18; break;
	case PORT_STAFF:    state = PS_DEMO_19; break;
	case PORT_STAFFEND: state = PS_DEMO_1A; break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
	stage_index = mario_entry.stage;
	SceneOpen(mario_entry.scene);
	SVecSet(player_actor[0].pos, staffp->posx, staffp->posy, staffp->posz);
	SVecSet(player_actor[0].ang, 0, staffp->angy << 8, 0);
	player_actor[0].scene = mario_entry.scene;
	SnOpenPlayer();
	MarioEnter();
	PL_SetState(mario, state, 0);
	camera_80286F68(scenep->cam);
	mario_entry.type = CHANGE_NULL;
	fade_mode = FADE_NULL;
	SnWipe(WIPE_FADE_IN, 20, 0x00, 0x00, 0x00);
	if (!staffp || staffp == staff_table)
	{
		AudPlayBGM(scenep->bgm_mode, scenep->bgm, 0);
	}
}

static void GmProcConnect(void)
{
	short _02;
	BGFACE *ground;
	if (stage_index == STAGE_INSIDE && BuStarTotal() >= 70) return;
	if ((ground = mario->ground))
	{
		int index = ground->code - BG_CONNECT;
		if (index >= 0 && index < CONNECT_MAX && scenep->connect)
		{
			CONNECT *connect = &scenep->connect[index];
			if (connect->flag)
			{
				mario->pos[0] += connect->offset[0];
				mario->pos[1] += connect->offset[1];
				mario->pos[2] += connect->offset[2];
				mario->obj->o_posx = mario->pos[0];
				mario->obj->o_posy = mario->pos[1];
				mario->obj->o_posz = mario->pos[2];
				_02 = mario->scene->cam->_02;
				SceneSet(connect->scene);
				mario->scene = scenep;
				camera_8028C7A0(
					connect->offset[0], connect->offset[1], connect->offset[2]
				);
				mario->scene->cam->_02 = _02;
			}
		}
	}
}

static int GmIsSameBGM(SHORT port)
{
	PORT *portp = SnGetPort(port);
	SHORT stage = portp->p.stage & 0x7F;
#if REVISION > 199606
	SHORT scene = portp->p.scene;
	SHORT result = TRUE;
	if (stage == STAGE_BOB && stage == stage_index && scene == scene_index)
	{
		SHORT bgm = Na_BgmGet();
		if (bgm == NA_BGM_SHELL || bgm == NA_BGM_SPECIAL) result = FALSE;
	}
	else
	{
		USHORT mode = scene_table[scene].bgm_mode;
		USHORT bgm  = scene_table[scene].bgm;
		result =
			stage == stage_index &&
			mode == scenep->bgm_mode && bgm == scenep->bgm;
		if (Na_BgmGet() != bgm) result = FALSE;
	}
#else
	USHORT mode = scene_table[portp->p.scene].bgm_mode;
	USHORT bgm  = scene_table[portp->p.scene].bgm;
	SHORT result =
		stage == stage_index && mode == scenep->bgm_mode && bgm == scenep->bgm;
	if (Na_BgmGet() != bgm) result = FALSE;
#endif
	return result;
}

static void GmSetEntry(SHORT stage, SHORT scene, SHORT port, u32 code)
{
	if      (port >= PORT_FINAL)        mario_entry.type = CHANGE_STAGE;
	else if (stage != stage_index)      mario_entry.type = CHANGE_STAGE;
	else if (scene != scenep->index)    mario_entry.type = CHANGE_SCENE;
	else                                mario_entry.type = CHANGE_PORT;
	mario_entry.stage = stage;
	mario_entry.scene = scene;
	mario_entry.port = port;
	mario_entry.code = code;
}

static BGPORT *GmGetBGPort(void)
{
	BGPORT *bgport = NULL;
	int index = mario->ground->code - BG_PORT;
	if (index >= 0 && index < BGPORT_MAX)
	{
		if (index < 3*14 || mario->pos[1]-mario->ground_y < 80)
		{
			bgport = &scenep->bgport[index];
		}
	}
	return bgport;
}

static void GmProcBGPort(void)
{
	BGPORT bgport, *bgportp;
	if (scenep->bgport && mario->ground)
	{
		if ((bgportp = GmGetBGPort()) != NULL)
		{
			if (mario->state & PF_DEMO)
			{
				AudProcWaveSound();
			}
			else if (bgportp->p.attr)
			{
				bgport = *bgportp;
				if (!(bgport.p.stage & 0x80)) mid_flag = BuGetMid(&bgport.p);
				GmSetEntry(
					bgport.p.stage & 0x7F, bgport.p.scene, bgport.p.port, 0
				);
				BuSetMid(&bgport.p);
				SnWipeDelay(WIPE_FADE_OUT, 30, 0xFF, 0xFF, 0xFF, 45);
				GmFreeze(45+30-1, GmSceneProc);
				PL_SetState(mario, PS_DEMO_00, 0);
				mario->obj->s.s.flag &= ~SHP_ACTIVE;
				Na_FixSePlay(NA_SE7_1E);
				AudFadeout(NA_TIME(50));
			}
		}
	}
}

int PL_Fade(PLAYER *pl, int mode)
{
	int fadeout = TRUE;
	if (fade_mode == FADE_NULL)
	{
		pl->invincible = -1;
		fade_code = 0;
		fade_mode = mode;
		switch (mode)
		{
		case FADE_LOGO:
		case FADE_FACE:
			fade_timer = 20;
			fade_port = PORT_WIN;
			prev_course = 0;
			fadeout = FALSE;
			SnWipe(WIPE_STAR_OUT, 20, 0x00, 0x00, 0x00);
			break;
		case FADE_ENDING:
			fade_timer = 60;
			fade_port = PORT_WIN;
			fadeout = FALSE;
			prev_course = 0;
			SnWipe(WIPE_FADE_OUT, 60, 0x00, 0x00, 0x00);
			break;
		case FADE_WIN:
			fade_timer = 32;
			fade_port = PORT_WIN;
			prev_course = 0;
			SnWipe(WIPE_MARIO_OUT, 32, 0x00, 0x00, 0x00);
			break;
		case FADE_DIE:
			if (pl->life == 0) fade_mode = FADE_GAMEOVER;
			fade_timer = 48;
			fade_port = PORT_DIE;
			SnWipe(WIPE_BOWSER_OUT, 48, 0x00, 0x00, 0x00);
			Na_FixSePlay(NA_SE7_18);
			break;
		case FADE_FALL:
			fade_port = PORT_FALL;
			if (!SnGetPort(fade_port))
			{
				if (pl->life == 0)  fade_mode = FADE_GAMEOVER;
				else                fade_port = PORT_DIE;
			}
			fade_timer = 20;
			SnWipe(WIPE_CIRCLE_OUT, 20, 0x00, 0x00, 0x00);
			break;
		case FADE_ROOF:
			fade_timer = 30;
			fade_port = PORT_ROOF;
			SnWipe(WIPE_FADE_OUT, 30, 0xFF, 0xFF, 0xFF);
#if REVISION > 199606
			Na_FixSePlay(NA_SE7_1E);
#endif
			break;
		case FADE_2:
			fade_timer = 30;
			fade_port = ObjGetCode(pl->attach);
			SnWipe(WIPE_FADE_OUT, 30, 0xFF, 0xFF, 0xFF);
			break;
		case FADE_5:
			fade_timer = 20;
			fade_port = ObjGetCode(pl->attach);
			fadeout = !GmIsSameBGM(fade_port);
			SnWipe(WIPE_FADE_OUT, 20, 0xFF, 0xFF, 0xFF);
			break;
		case FADE_DOOR:
			fade_timer = 20;
			fade_code = pl->code;
			fade_port = ObjGetCode(pl->attach);
			fadeout = !GmIsSameBGM(fade_port);
			SnWipe(WIPE_CIRCLE_OUT, 20, 0x00, 0x00, 0x00);
			break;
		case FADE_PIPE:
			fade_timer = 20;
			fade_port = ObjGetCode(pl->attach);
			fadeout = !GmIsSameBGM(fade_port);
			SnWipe(WIPE_STAR_OUT, 20, 0x00, 0x00, 0x00);
			break;
		case FADE_FINAL:
			fade_timer = 30;
			SnWipe(WIPE_FADE_OUT, 30, 0x00, 0x00, 0x00);
			break;
		case FADE_STAFF:
			if (staffp == staff_table)
			{
				fade_timer = 60;
				SnWipe(WIPE_FADE_OUT, 60, 0x00, 0x00, 0x00);
			}
			else
			{
				fade_timer = 20;
				SnWipe(WIPE_FADE_OUT, 20, 0x00, 0x00, 0x00);
			}
			fadeout = FALSE;
			break;
		}
		if (fadeout && !demop) AudFadeout(NA_TIME(fade_timer*3/2));
	}
	return fade_timer;
}

static void GmProcFade(void)
{
	PORT *portp;
	int port;
	if (fade_mode != FADE_NULL && --fade_timer == 0)
	{
		MsgClose();
		if (debug_stage && (fade_mode & FADE_EXIT))
		{
			GmExit(EXIT_DEBUG);
		}
		else if (demop)
		{
			if (fade_mode == FADE_LOGO) GmExit(EXIT_LOGO);
			else                        GmExit(EXIT_FACE);
		}
		else
		{
			switch (fade_mode)
			{
			case FADE_GAMEOVER:
				BuReset();
				GmExit(EXIT_GAMEOVER);
				break;
			case FADE_ENDING:
				GmExit(EXIT_ENDING);
				Na_EndingUnlockSe();
				break;
			case FADE_FACE:
				GmExit(EXIT_FACE);
				break;
			case FADE_FINAL:
				staffp = staff_table;
				GmSetEntry(staffp->stage, staffp->scene, PORT_FINAL, 0);
				break;
			case FADE_STAFF:
				Na_StaffLockSe();
				staffp++;
				level_index = staffp->flag & 7;
				port = (staffp+1)->stage == STAGE_NULL ?
					PORT_STAFFEND : PORT_STAFF;
				GmSetEntry(staffp->stage, staffp->scene, port, 0);
				break;
			default:
				portp = SnGetPort(fade_port);
				GmSetEntry(
					portp->p.stage & 0x7F, portp->p.scene, portp->p.port,
					fade_code
				);
				BuSetMid(&portp->p);
				if (mario_entry.type != CHANGE_STAGE)
				{
					GmFreeze(2, NULL);
				}
				break;
			}
		}
	}
}

static void GmProcHUD(void)
{
	if (!staffp)
	{
		SHORT power = mario->power > 0 ? mario->power >> 8 : 0;
		if (course_index > 0)   hud.flag |= HUD_COIN;
		else                    hud.flag &= ~HUD_COIN;
		if (hud.coin < mario->coin && (gfx_frame & 1))
		{
			Na_Se se = (mario->state & (PF_SWIM|PF_SINK)) ?
				NA_SE3_12 : NA_SE3_11;
			hud.coin++;
			Na_ObjSePlay(se, mario->obj);
		}
		if (mario->life > 100) mario->life = 100;
#if REVISION > 199606
		if (mario->coin > 999) mario->coin = 999;
		if (hud.coin    > 999) hud.coin    = 999;
#else
		if (mario->coin > 999) mario->life = (s8)999;
#endif
		hud.star = mario->star;
		hud.life = mario->life;
		hud.key  = mario->key;
		if (power > hud.power) Na_FixSePlay(NA_SE7_0D);
		hud.power = power;
		if (mario->damage > 0)  hud.flag |= HUD_ALERT;
		else                    hud.flag &= ~HUD_ALERT;
	}
}

static void GmSceneProc(UNUSED short *timer)
{
	SceneProc();
	GmProcHUD();
	if (scenep) camera_802868F8(scenep->cam);
}

static int GmProcNormal(void)
{
	if (demop)
	{
		SceneDemo();
		if (cont1->down & CONT_EXIT)
		{
			PL_Fade(mario, stage_index == STAGE_PSS ? FADE_LOGO : FADE_FACE);
		}
		else if (
			!wipe.active && fade_mode == FADE_NULL &&
			(cont1->down & START_BUTTON)
		)
		{
			PL_Fade(mario, FADE_FACE);
		}
	}
	GmProcEntry();
	GmProcConnect();
	if (time_flag && hud.time < 30*60*10-1) hud.time++;
	SceneProc();
	GmProcHUD();
	if (scenep) camera_802868F8(scenep->cam);
	GmProcBGPort();
	GmProcFade();
	if (game_state == GM_NORMAL)
	{
		if (mario_entry.type == CHANGE_STAGE)
		{
			GmSetState(GM_EXIT);
		}
		else if (freeze_timer != 0)
		{
			GmSetState(GM_FREEZE);
		}
		else if (GmCheckPause())
		{
			AudSetMute(AUD_PAUSE);
			camera_8033C848 |= 0x8000;
			GmSetState(GM_PAUSE);
		}
	}
	return 0;
}

static int GmProcPause(void)
{
	if (msg_status == 0)
	{
		MenuOpen(1);
	}
	else if (msg_status == 1)
	{
		AudClrMute(AUD_PAUSE);
		camera_8033C848 &= ~0x8000;
		GmSetState(GM_NORMAL);
	}
	else
	{
		if (debug_stage)
		{
			GmFadeout(EXIT_DEBUG, 1);
		}
		else
		{
			GmSetEntry(STAGE_INSIDE, 1, 31, 0);
			GmFadeout(0, 0);
			prev_course = 0;
		}
		camera_8033C848 &= ~0x8000;
	}
	return 0;
}

static int GmProcFrameAdv(void)
{
	if (cont1->down & D_JPAD)
	{
		camera_8033C848 &= ~0x8000;
		GmProcNormal();
	}
	else if (cont1->down & START_BUTTON)
	{
		camera_8033C848 &= ~0x8000;
		AudClrMute(AUD_PAUSE);
		GmSetState(GM_NORMAL);
	}
	else
	{
		camera_8033C848 |= 0x8000;
	}
	return 0;
}

void GmFreeze(SHORT timer, FREEZECALL *callback)
{
	freeze_timer = timer;
	freeze_callback = callback;
}

static int GmProcFreeze(void)
{
	if (freeze_callback == (FREEZECALL *)-1) camera_802868F8(scenep->cam);
	else if (freeze_callback) freeze_callback(&freeze_timer);
	if (freeze_timer > 0) freeze_timer--;
	if (freeze_timer == 0)
	{
		freeze_callback = NULL;
		GmSetState(GM_NORMAL);
	}
	return 0;
}

static int GmProcExit(void)
{
	if (freeze_callback) freeze_callback(&freeze_timer);
	if (--freeze_timer == -1)
	{
		hud.flag = 0;
		freeze_timer = 0;
		freeze_callback = NULL;
		if (mario_entry.type != CHANGE_NULL) return mario_entry.stage;
		else return game_result;
	}
	return 0;
}

UNUSED
static int GmProcExitOLD(void)
{
	if (--freeze_timer == -1)
	{
		hud.flag = 0;
		if (mario_entry.type != CHANGE_NULL) return mario_entry.stage;
		else return game_result;
	}
	return 0;
}

static int GmProc(void)
{
	int result;
	switch (game_state)
	{
	case GM_NORMAL:     result = GmProcNormal();    break;
	case GM_PAUSE:      result = GmProcPause();     break;
	case GM_FREEZE:     result = GmProcFreeze();    break;
	case GM_EXIT:       result = GmProcExit();      break;
	case GM_FRAMEADV:   result = GmProcFrameAdv();  break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
	if (result)
	{
		AudResetMute();
		AudUnlock();
	}
	return result;
}

static int GmInit(void)
{
	int opening = FALSE;
	GmSetState(GM_NORMAL);
	fade_mode = FADE_NULL;
	freeze_timer = 0;
	game_result = 0;
	hud.flag = !staffp ? (HUD_ALL & ~HUD_TIME) : 0;
	time_flag = FALSE;
	if (mario_entry.type != CHANGE_NULL)
	{
		if (mario_entry.port >= PORT_FINAL) GmInitStaff();
		else                                GmInitStage();
	}
	else
	{
		if (player_actor[0].scene >= 0)
		{
			SnOpenPlayer();
			MarioEnter();
		}
		if (scenep)
		{
			camera_80286F68(scenep->cam);
			if (demop)
			{
				PL_SetState(mario, PS_WAIT_01, 0);
			}
			else if (!debug_stage && mario->state != PS_NULL)
			{
				if (BuIsActive())
				{
					PL_SetState(mario, PS_WAIT_01, 0);
				}
				else
				{
					PL_SetState(mario, PS_DEMO_01, 0);
					opening = TRUE;
				}
			}
		}
		if (opening)    SnWipe(WIPE_FADE_IN, 90, 0xFF, 0xFF, 0xFF);
		else            SnWipe(WIPE_STAR_IN, 16, 0xFF, 0xFF, 0xFF);
		if (!demop) AudPlayBGM(scenep->bgm_mode, scenep->bgm, 0);
	}
	if (mario->state == PS_DEMO_01) Na_OpeningLockSe();
	return 1;
}

long GameProc(SHORT code, UNUSED long status)
{
	int result = 0;
	switch (code)
	{
	case 0: result = GmInit(); break;
	case 1: result = GmProc(); break;
	}
	return result;
}

long GameInit(UNUSED SHORT code, long status)
{
	mario_entry.type = CHANGE_NULL;
	fade_mode = FADE_NULL;
	first_msg = !BuIsActive();
	stage_index = status;
	course_index = COURSE_NULL;
	prev_course = COURSE_NULL;
	staffp = NULL;
	bu_jump = FALSE;
	MarioInit();
	BuClrMid();
	BuInitCap();
	camera_80287BC4();
	object_b_802E3E50();
	return status;
}

long GameCheckSelect(UNUSED SHORT code, long status)
{
	int mid = mid_flag;
	mid_flag = FALSE;
	stage_index = status;
	course_index = StageToCourse(status);
	if (demop || staffp || course_index == COURSE_NULL) return FALSE;
	if (!(
		stage_index == STAGE_BITDWA ||
		stage_index == STAGE_BITFSA ||
		stage_index == STAGE_BITSA
	))
	{
		mario->coin = 0;
		hud.coin = 0;
		bu_star = BuGetStar(course_index-1);
	}
	if (prev_course != course_index)
	{
		prev_course = course_index;
		CourseInit();
		BuClrMid();
	}
	if (course_index >= COURSE_EXT || mid) return FALSE;
	if (debug_stage && !debug_time) return FALSE;
	return TRUE;
}

long EndingSound(UNUSED SHORT code, UNUSED long status)
{
	Na_FixSePlay(NA_SE7_1F);
	return 1;
}
