#include <sm64.h>

#if REVISION == 199605
extern void Na_game_8048FFE8(void);
#endif

static char stagename[64][16] =
{
	"",
	"",
	"",
	"TERESA OBAKE",
	"YYAMA1 % YSLD1",
	"SELECT ROOM",
	"HORROR DUNGEON",
	"SABAKU % PYRMD",
	"BATTLE FIELD",
	"YUKIYAMA2",
	"POOL KAI",
	"WTDG % TINBOTU",
	"BIG WORLD",
	"CLOCK TOWER",
	"RAINBOW CRUISE",
	"MAIN MAP",
	"EXT1 YOKO SCRL",
	"EXT7 HORI MINI",
	"EXT2 TIKA LAVA",
	"EXT9 SUISOU",
	"EXT3 HEAVEN",
	"FIREB1 % INVLC",
	"WATER LAND",
	"MOUNTAIN",
	"ENDING",
	"URANIWA",
	"EXT4 MINI SLID",
	"IN THE FALL",
	"EXT6 MARIO FLY",
	"KUPPA1",
	"EXT8 BLUE SKY",
	"",
	"KUPPA2",
	"KUPPA3",
	"",
	"DONKEY % SLID2",
	"",
	"",
};

static u16 demo_wait = 0;

static int TitleDemo(int result)
{
	demop = NULL;
	if (!result)
	{
		if (!cont1->held && !cont1->dist)
		{
			if (++demo_wait == 800)
			{
				BankLoad(&demo_bank, demo_index);
				if (++demo_index == demo_bank.info->len) demo_index = 0;
				demop = (DEMO *)((char *)demo_bank.buf+4);
				result = ((char *)demo_bank.buf)[0];
				file_index = 1;
				level_index = 1;
			}
		}
		else
		{
			demo_wait = 0;
		}
	}
	return result;
}

static int TitleDebug(void)
{
	int flag = FALSE;
	if (cont1->down & A_BUTTON) stage_index +=  1, flag = TRUE;
	if (cont1->down & B_BUTTON) stage_index -=  1, flag = TRUE;
	if (cont1->down & U_JPAD)   stage_index -=  1, flag = TRUE;
	if (cont1->down & D_JPAD)   stage_index +=  1, flag = TRUE;
	if (cont1->down & L_JPAD)   stage_index -= 10, flag = TRUE;
	if (cont1->down & R_JPAD)   stage_index += 10, flag = TRUE;
	if (flag) Na_FixSePlay(NA_SE3_2B);
	if (stage_index > 38) stage_index =  1;
	if (stage_index <  1) stage_index = 38;
	file_index = 4;
	level_index = 6;
	dprintc(SCREEN_WD/2, 80, "SELECT STAGE");
	dprintc(SCREEN_WD/2, 30, "PRESS START BUTTON");
	dprintf(40, 60, "%2d", stage_index);
	dprint(80, 60, stagename[stage_index-1]);
	if (cont1->down & START_BUTTON)
	{
		if (cont1->held == (Z_TRIG|START_BUTTON|L_CBUTTONS|R_CBUTTONS))
		{
			debug_stage = FALSE;
			return -1;
		}
		Na_FixSePlay(NA_SE7_1E);
		return stage_index;
	}
	return 0;
}

static int TitleFace(void)
{
	int result = 0;
#if REVISION >= 199609
	static short flag = TRUE;
	if (ISTRUE(flag))
	{
		if (gfx_frame <= 128)   Na_FixSePlay(NA_SE2_32);
		else                    Na_FixSePlay(NA_SE2_33);
		flag = FALSE;
	}
#endif
	SceneDemo();
#if REVISION == 199605
	dprintc(SCREEN_WD/2, 90, "DISK VERSION");
#endif
	if (cont1->down & START_BUTTON)
	{
		Na_FixSePlay(NA_SE7_1E);
#ifdef MOTOR
		motor_8024C834(60, 70);
		motor_8024C89C(1);
#endif
		result = 100 + debug_stage;
#if REVISION >= 199609
		flag = TRUE;
#endif
	}
	return TitleDemo(result);
}

static int TitleGameOver(void)
{
	int result = 0;
#if REVISION >= 199609
	static short flag = TRUE;
	if (ISTRUE(flag))
	{
		Na_FixSePlay(NA_SE2_31);
		flag = FALSE;
	}
#endif
	SceneDemo();
#if REVISION == 199605
	dprintc(SCREEN_WD/2, 90, "DISK VERSION");
#endif
	if (cont1->down & START_BUTTON)
	{
		Na_FixSePlay(NA_SE7_1E);
#ifdef MOTOR
		motor_8024C834(60, 70);
		motor_8024C89C(1);
#endif
		result = 100 + debug_stage;
#if REVISION >= 199609
		flag = TRUE;
#endif
	}
	return TitleDemo(result);
}

static int TitleLogo(void)
{
#if REVISION == 199605
	Na_game_8048FFE8();
#else
	AudPlayBGM(NA_MODE_DEFAULT, NA_BGM_NULL, 0);
	Na_FixSePlay(NA_SE7_14);
#endif
	return 1;
}

#if REVISION < 199606
static int TitleProc4(void)
{
	return 1;
}
#endif

long TitleProc(SHORT code, UNUSED long status)
{
	long result;
	switch (code)
	{
	case 0: result = TitleLogo();      break;
	case 1: result = TitleFace();      break;
	case 2: result = TitleGameOver();  break;
	case 3: result = TitleDebug();     break;
#if REVISION < 199606
	case 4: result = TitleProc4();     break;
#endif
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
	return result;
}
