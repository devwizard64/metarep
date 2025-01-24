#include <sm64.h>

typedef struct dbprint
{
	short flag;
	short x;
	short y;
	short min_y;
	short max_y;
	short height;
}
DBPRINT;

static const char *db_edit_effectinfo[] =
{
	"  a0 %d",
	"  a1 %d",
	"  a2 %d",
	"  a3 %d",
	"  a4 %d",
	"  a5 %d",
	"  a6 %d",
	"  a7 %d",
	"A",
};

static const char *db_edit_enemyinfo[] =
{
	"  b0 %d",
	"  b1 %d",
	"  b2 %d",
	"  b3 %d",
	"  b4 %d",
	"  b5 %d",
	"  b6 %d",
	"  b7 %d",
	"B",
};

static int db_button = 0;
static int db_repeat = 0;
static char db_init_flag = 0;
static s8 db_page = 0;
static char db_hideinfo = FALSE;
static char db_edit_flag = 0;
static s8 db_line = 0;

static DBPRINT db_out;
static DBPRINT db_err;

UNUSED static
void _802CA370(void)
{
}

UNUSED static
void _802CA380(void)
{
}

UNUSED static
void _802CA390(void)
{
}

UNUSED static
void _802CA3A0(void)
{
}

OSTime DbTimeStart(void)
{
	OSTime t = 0;
	return t;
}

OSTime DbTimeCount(UNUSED OSTime start)
{
	OSTime t = 0;
	return t;
}

static void DbPrintInit(
	DBPRINT *dp, SHORT x, SHORT y, SHORT min_y, SHORT max_y, SHORT height
)
{
	dp->flag = 0;
	dp->x = x;
	dp->y = y;
	dp->min_y = min_y;
	dp->max_y = max_y;
	dp->height = height;
}

static void DbPrintEntry(DBPRINT *dp, const char *fmt, int value)
{
	if (!dp->flag)
	{
		if (dp->y < dp->min_y || dp->max_y < dp->y)
		{
			dprint(dp->x, dp->y, "DPRINT OVER");
			dp->flag++;
		}
		else
		{
			dprintf(dp->x, dp->y, fmt, value);
			dp->y += dp->height;
		}
	}
}

void DbPrintOffset(int off_x, int off_ln)
{
	DBPRINT *dp = &db_out;
	dp->x += off_x;
	dp->y += off_ln * dp->height;
}

void DbPrintErr(const char *fmt, int value)
{
	if (debug_flag & DEBUG_SHOW) DbPrintEntry(&db_err, fmt, value);
}

void DbPrint(const char *fmt, int value)
{
	if (debug_flag & DEBUG_SHOW)
	{
		if (db_page == 0) DbPrintEntry(&db_out, fmt, value);
	}
}

void DbPrintInfo(const char *fmt, int value)
{
	if (db_hideinfo) return;
	if (debug_flag & DEBUG_SHOW) DbPrintEntry(&db_out, fmt, value);
}

void DbPrintTitle(const char *fmt, int value)
{
	if (debug_flag & DEBUG_SHOW) DbPrintEntry(&db_out, fmt, value);
}

static void DbPlayerMapInfo(void)
{
	BGFACE *ground;
	float ground_y, water_y;
	int area, angy = object->o_angy / 182.044;
	area =
		(((int)object->o_posx+MAP_HALF)/BGAREA_SIZE) +
		(((int)object->o_posz+MAP_HALF)/BGAREA_SIZE)*BGAREA_N;
	ground_y = BGCheckGround(
		object->o_posx, object->o_posy, object->o_posz, &ground
	);
	water_y = BGCheckWater(object->o_posx, object->o_posz);
	DbPrintTitle("mapinfo", 0);
	DbPrintInfo("area %x", area);
	DbPrintInfo("wx   %d", object->o_posx);
	DbPrintInfo("wy	  %d", object->o_posy);
	DbPrintInfo("wz   %d", object->o_posz);
	DbPrintInfo("bgY  %d", ground_y);
	DbPrintInfo("angY %d", angy);
	if (ground)
	{
		DbPrintInfo("bgcode   %d", ground->code);
		DbPrintInfo("bgstatus %d", ground->flag);
		DbPrintInfo("bgarea   %d", ground->area);
	}
	if (object->o_posy < water_y) DbPrintInfo("water %d", water_y);
}

static void DbPlayerCheckInfo(void)
{
	DbPrintTitle("checkinfo", 0);
}

static void DbResultCheckInfo(void)
{
	BGCheckDebug(mario_obj->o_posx, mario_obj->o_posz);
}

static void DbPlayerStageInfo(void)
{
	DbPrintTitle("stageinfo", 0);
	DbPrintTitle("stage param %d", object_80361258);
}

static void DbPrintEdit(const char *fmt[])
{
	int i;
	if (!db_edit_flag)
	{
		db_edit_flag++;
		for (i = 0; i < 8; i++) DbPrintInfo(fmt[i], db_work[db_page][i]);
		DbPrintOffset(0, -(8-db_line));
		DbPrintInfo(fmt[8], 0);
		DbPrintOffset(0, +(8-db_line)-1);
	}
}

static void DbResultEffectInfo(void)
{
	DbPrintTitle("effectinfo", 0);
	DbPrintEdit(db_edit_effectinfo);
}

static void DbResultEnemyInfo(void)
{
	DbPrintTitle("enemyinfo", 0);
	DbPrintEdit(db_edit_enemyinfo);
}

static void DbProcButton(void)
{
	int held = cont1->held & (U_JPAD|D_JPAD|L_JPAD|R_JPAD);
	if (!held)
	{
		db_repeat = 0;
		db_button = 0;
	}
	else
	{
		if      (db_repeat == 0)    db_button = held;
		else if (db_repeat == 6)    db_button = held;
		else                        db_button = 0;
		db_repeat++;
		if (db_repeat > 7) db_repeat = 6;
	}
}

void DebugInit(void)
{
	if (!db_init_flag)
	{
		db_init_flag++;
		if (!debug_stage)   debug_flag = 0;
		else                debug_flag = DEBUG_2;
		bgdebug.ground = 0;
		bgdebug.roof = 0;
		bgdebug.wall = 0;
	}
}

void DebugClear(void)
{
	nullbg_count = 0;
	wall_count = 0;
	obj_count = 0;
	db_edit_flag = 0;
	object_80361252 = 0;
	object_80361254 = 0;
	DbPrintInit(&db_out, 20, 185, 40, 200, -15);
	DbPrintInit(&db_err, 180, 30, 0, 150, 15);
	DbProcButton();
}

UNUSED static
void DebugProcSeq(void)
{
	static s8 index = 0;
	static s16 seqdata[] = {U_CBUTTONS, L_CBUTTONS, D_CBUTTONS, R_CBUTTONS, -1};
	s16 *seq = seqdata;
	SHORT x;
	if (!(cont1->held & L_TRIG))
	{
		index = 0;
	}
	else if ((x = cont1->down & (U_CBUTTONS|D_CBUTTONS|L_CBUTTONS|R_CBUTTONS)))
	{
		if (seq[index] == x)
		{
			index++;
			if (seq[index] == -1)
			{
				if (debug_flag == DEBUG_ALL)    debug_flag = DEBUG_2;
				else                            debug_flag = DEBUG_ALL;
			}
		}
		else
		{
			index = 0;
		}
	}
}

UNUSED static
void DebugProcPage(void)
{
	if (debug_flag & DEBUG_SHOW)
	{
		if ((cont1->down & L_JPAD) && (cont1->held & (L_TRIG|R_TRIG)))
		{
			db_page++;
		}
		if ((cont1->down & R_JPAD) && (cont1->held & (L_TRIG|R_TRIG)))
		{
			db_page--;
		}
		if (db_page > 5) db_page = 0;
		if (db_page < 0) db_page = 5;
	}
}

UNUSED static
void DebugProcEdit(void)
{
	if (cont1->down & Z_TRIG) db_hideinfo ^= TRUE;
	if (!(cont1->held & (L_TRIG|R_TRIG)) && !db_hideinfo)
	{
		int step = 1;
		if (cont1->held & B_BUTTON) step = 100;
		if (db_button & U_JPAD)
		{
			db_line--;
			if (db_line < 0) db_line = 0;
		}
		if (db_button & D_JPAD)
		{
			db_line++;
			if (db_line > 7) db_line = 7;
		}
		if (db_button & L_JPAD)
		{
			if (cont1->held & A_BUTTON)
			{
				db_work[db_page][db_line] = db_save[db_page][db_line];
			}
			else
			{
				db_work[db_page][db_line] -= step;
			}
		}
		if (db_button & R_JPAD)
		{
			db_work[db_page][db_line] += step;
		}
	}
}

void DebugExec(void)
{
}

void DebugResult(void)
{
	if (mario_obj)
	{
		switch (db_page)
		{
		case 1: DbResultCheckInfo(); break;
		case 4: DbResultEffectInfo(); break;
		case 5: DbResultEnemyInfo(); break;
		default: break;
		}
	}
	DbPrintInfo("obj  %d", obj_count);
	if (nullbg_count)   DbPrintErr("NULLBG %d", nullbg_count);
	if (wall_count)     DbPrintErr("WALL   %d", wall_count);
}

void DebugPlayer(void)
{
	switch (db_page)
	{
	case 0: break;
	case 1: DbPlayerCheckInfo(); break;
	case 2: DbPlayerMapInfo(); break;
	case 3: DbPlayerStageInfo(); break;
	default: break;
	}
}

extern OBJLANG o_13000708[];
extern OBJLANG o_13001650[];
extern OBJLANG o_13001F3C[];

void DebugProc(void)
{
	UNUSED int i;
	if (db_page == 3 && db_work[5][7] == 1)
	{
		if (cont1->down & R_JPAD)
		{
			ObjMakeOff(0, 0, 100, 200, object, S_SHELL, o_13001F3C);
		}
		if (cont1->down & L_JPAD)
		{
			ObjMakeOff(0, 0, 100, 200, object, S_CRATE, o_13001650);
		}
		if (cont1->down & D_JPAD)
		{
			ObjMakeOff(0, 0, 100, 200, object, S_SHELL, o_13000708);
		}
	}
}

UNUSED static
void DebugPrintMoveStatus(void)
{
	if (object->o_move & OM_BOUND)      DbPrint("BOUND   %x", object->o_move);
	if (object->o_move & OM_TOUCH)      DbPrint("TOUCH   %x", object->o_move);
	if (object->o_move & OM_TAKEOFF)    DbPrint("TAKEOFF %x", object->o_move);
	if (object->o_move & OM_DIVE)       DbPrint("DIVE    %x", object->o_move);
	if (object->o_move & OM_S_WATER)    DbPrint("S WATER %x", object->o_move);
	if (object->o_move & OM_U_WATER)    DbPrint("U WATER %x", object->o_move);
	if (object->o_move & OM_B_WATER)    DbPrint("B WATER %x", object->o_move);
	if (object->o_move & OM_SKY)        DbPrint("SKY     %x", object->o_move);
	if (object->o_move & OM_OUT_SCOPE)  DbPrint("OUT SCOPE %x", object->o_move);
}

UNUSED static
void DebugSetHit(HITINFO *hit)
{
	hit->hit_r = db_work[5][1];
	hit->hit_h = db_work[5][2];
	hit->dmg_r = db_work[5][3];
	hit->dmg_h = db_work[5][4];
}
