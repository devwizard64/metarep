#include <sm64.h>

#ifdef JAPANESE
#include "fileselect.ja_jp.h"
#endif
#ifdef ENGLISH
#include "fileselect.en_us.h"
#endif

#define F_SELECT        -1

#define F_MIN           0
#define F_FILE          0
#define F_FILE_A        0
#define F_FILE_B        1
#define F_FILE_C        2
#define F_FILE_D        3
#define F_SCORE         4
#define F_COPY          5
#define F_ERASE         6
#define F_MAX           7

#define FS_MIN          7
#define FS_FILE         7
#define FS_FILE_A       7
#define FS_FILE_B       8
#define FS_FILE_C       9
#define FS_FILE_D       10
#define FS_SELECT       11
#define FS_COPY         12
#define FS_ERASE        13
#define FS_MAX          14

#define FC_MIN          14
#define FC_FILE         14
#define FC_FILE_A       14
#define FC_FILE_B       15
#define FC_FILE_C       16
#define FC_FILE_D       17
#define FC_SELECT       18
#define FC_SCORE        19
#define FC_ERASE        20
#define FC_MAX          21

#define FE_MIN          21
#define FE_FILE         21
#define FE_FILE_A       21
#define FE_FILE_B       22
#define FE_FILE_C       23
#define FE_FILE_D       24
#define FE_SELECT       25
#define FE_SCORE        26
#define FE_COPY         27
#define FE_MAX          28

#define F_OPTION        28
#define FO_MIN          29
#define FO_SOUND        29
#define FO_STEREO       29
#define FO_MONO         30
#define FO_PHONE        31
#define FO_MAX          32

#define TILE_CLOSED     0
#define TILE_OPEN       1
#define TILE_OPENED     2
#define TILE_CLOSE      3
#define TILE_CLICK      4
#define TILE_SELECT     5
#define TILE_DESELECT   6

extern Gfx gfx_print_1cyc_begin[];
extern Gfx gfx_print_1cyc_end[];
extern Gfx gfx_lgfont_begin[];
extern Gfx gfx_lgfont_end[];
extern unsigned char *coursename[];

extern Gfx gfx_smfont_begin[];
extern Gfx gfx_smfont_end[];
extern Gfx gfx_select_cursor_0[];
extern Gfx gfx_select_cursor_1[];

static OBJECT *fs_obj[32];
static s8 fs_state = F_SELECT;
static char fs_mode = 1;
static u8 fs_alpha = 0;
static float cursor_pos[2] = {0, 0};
static short cursor_flag = 0;
static short click_pos[2] = {-10000, -10000};
static s8 click_file = -1;
static char click_flag = FALSE;
static char click_msg = 0;
static u8 click_alpha = 0;
static short click_timer = 0;
static s8 sound_flag = 0;
static u8 blink[2];
static char erase_flag = 0;
static char fs_full = FALSE;
static char fs_result = 0;
static char score_flag = 0;

void FileBack_Init(void)
{
	object->o_shapeangy = 0x8000;
	object->o_f5 = 9;
}

void FileBack_Proc(void)
{
	ObjectSetScale(9);
}

static int FileIsClick(SHORT x, SHORT y, float z)
{
	float scale = (float)52.4213;
	float ortho_x = SCREEN_WD/2.0 * (float)x / (scale     * z);
	float ortho_y = SCREEN_HT/2.0 * (float)y / (scale*3/4 * z);
	SHORT xh = ortho_x + 25;
	SHORT xl = ortho_x - 25;
	SHORT yh = ortho_y + 21;
	SHORT yl = ortho_y - 21;
	if (
		click_pos[0] < xh && click_pos[0] > xl &&
		click_pos[1] < yh && click_pos[1] > yl
	) return TRUE;
	return FALSE;
}

static void FileTile_Open1(OBJECT *obj)
{
	if (                  obj->o_v1 < 16) obj->o_shapeangy += 0x800;
	if (obj->o_v1 <  8                  ) obj->o_shapeangx += 0x800;
	if (obj->o_v1 >= 8 && obj->o_v1 < 16) obj->o_shapeangx -= 0x800;
	obj->o_relx -= obj->o_f2 / 16.0;
	obj->o_rely -= obj->o_f3 / 16.0;
	if (obj->o_posz < obj->o_f4+17800.0) obj->o_relz += 17800.0 / 16.0;
	obj->o_v1++;
	if (obj->o_v1 == 16)
	{
		obj->o_relx = 0;
		obj->o_rely = 0;
		obj->o_v0 = TILE_OPENED;
		obj->o_v1 = 0;
	}
}

static void FileTile_Close1(OBJECT *obj)
{
	if (                  obj->o_v1 < 16) obj->o_shapeangy -= 0x800;
	if (obj->o_v1 <  8                  ) obj->o_shapeangx -= 0x800;
	if (obj->o_v1 >= 8 && obj->o_v1 < 16) obj->o_shapeangx += 0x800;
	obj->o_relx += obj->o_f2 / 16.0;
	obj->o_rely += obj->o_f3 / 16.0;
	if (obj->o_posz > obj->o_f4) obj->o_relz -= 17800.0 / 16.0;
	obj->o_v1++;
	if (obj->o_v1 == 16)
	{
		obj->o_relx = obj->o_f2;
		obj->o_rely = obj->o_f3;
		obj->o_v0 = TILE_CLOSED;
		obj->o_v1 = 0;
	}
}

static void FileTile_Open2(OBJECT *obj)
{
	if (                  obj->o_v1 < 16) obj->o_shapeangy += 0x800;
	if (obj->o_v1 <  8                  ) obj->o_shapeangx += 0x800;
	if (obj->o_v1 >= 8 && obj->o_v1 < 16) obj->o_shapeangx -= 0x800;
	obj->o_relx -= obj->o_f2 / 16.0;
	obj->o_rely -= obj->o_f3 / 16.0;
	obj->o_relz -= 1860.0 / 16.0;
	obj->o_v1++;
	if (obj->o_v1 == 16)
	{
		obj->o_relx = 0;
		obj->o_rely = 0;
		obj->o_v0 = TILE_OPENED;
		obj->o_v1 = 0;
	}
}

static void FileTile_Close2(OBJECT *obj)
{
	if (                  obj->o_v1 < 16) obj->o_shapeangy -= 0x800;
	if (obj->o_v1 <  8                  ) obj->o_shapeangx -= 0x800;
	if (obj->o_v1 >= 8 && obj->o_v1 < 16) obj->o_shapeangx += 0x800;
	obj->o_relx += obj->o_f2 / 16.0;
	obj->o_rely += obj->o_f3 / 16.0;
	if (obj->o_posz > obj->o_f4) obj->o_relz += 1860.0 / 16.0;
	obj->o_v1++;
	if (obj->o_v1 == 16)
	{
		obj->o_relx = obj->o_f2;
		obj->o_rely = obj->o_f3;
		obj->o_v0 = TILE_CLOSED;
		obj->o_v1 = 0;
	}
}

static void FileTile_Click(OBJECT *obj)
{
	if (fs_mode == 1)
	{
		if (obj->o_v1 <  4) obj->o_relz -= 20;
		if (obj->o_v1 >= 4) obj->o_relz += 20;
	}
	else
	{
		if (obj->o_v1 <  4) obj->o_relz += 20;
		if (obj->o_v1 >= 4) obj->o_relz -= 20;
	}
	obj->o_v1++;
	if (obj->o_v1 == 8)
	{
		obj->o_v0 = TILE_CLOSED;
		obj->o_v1 = 0;
	}
}

static void FileTile_Select(OBJECT *obj)
{
	obj->o_f5 += 0.0022;
	obj->o_v1++;
	if (obj->o_v1 == 10)
	{
		obj->o_v0 = TILE_CLOSED;
		obj->o_v1 = 0;
	}
}

static void FileTile_Deselect(OBJECT *obj)
{
	obj->o_f5 -= 0.0022;
	obj->o_v1++;
	if (obj->o_v1 == 10)
	{
		obj->o_v0 = TILE_CLOSED;
		obj->o_v1 = 0;
	}
}

void FileTile_Init(void)
{
	object->o_f2 = object->o_relx;
	object->o_f3 = object->o_rely;
}

void FileTile_Proc(void)
{
	switch (object->o_v0)
	{
	case 0:
		object->o_f4 = object->o_posz;
		break;
	case 1:
		if (fs_mode == 1) FileTile_Open1(object);
		if (fs_mode == 2) FileTile_Open2(object);
		fs_alpha = 0;
		cursor_flag = 4;
		break;
	case 2:
		break;
	case 3:
		if (fs_mode == 1) FileTile_Close1(object);
		if (fs_mode == 2) FileTile_Close2(object);
		fs_alpha = 0;
		cursor_flag = 4;
		break;
	case 4:
		FileTile_Click(object);
		cursor_flag = 4;
		break;
	case 5:
		FileTile_Select(object);
		cursor_flag = 4;
		break;
	case 6:
		FileTile_Deselect(object);
		cursor_flag = 4;
		break;
	}
	ObjectSetScale(object->o_f5);
}

extern OBJLANG obj_filetile[];

#define FileMenu_MakeTile(obj, shape, scale, posx, posy, posz, angy) \
	ObjMakeRel( \
		obj, shape, obj_filetile, (posx)/scale, (posy)/scale, posz, 0, angy, 0 \
	)
#define FileMenu_InitTileSel(tile, shape, x, y) \
{ \
	fs_obj[tile] = FileMenu_MakeTile(object, shape, 1, x, y, 0, 0); \
	fs_obj[tile]->o_f5 = (float)1/1; \
}
#define FileMenu_InitTileSub(obj, tile, shape, x, y) \
{ \
	fs_obj[tile] = FileMenu_MakeTile(obj, shape, 9, x, y, -100, -0x8000); \
	fs_obj[tile]->o_f5 = (float)1/9; \
}
#define FileMenu_InitFileSel(i) \
{ \
	if (ISTRUE(BuFileIsActive(i))) \
	{ \
		fs_obj[F_FILE+i] = FileMenu_MakeTile( \
			object, S_FILE_MARIO_S, 1, \
			i & 1 ? +1500 : -6400, \
			i & 2 ?     0 : +2800, \
			0, 0 \
		); \
	} \
	else \
	{ \
		fs_obj[F_FILE+i] = FileMenu_MakeTile( \
			object, S_FILE_NEW_S, 1, \
			i & 1 ? +1500 : -6400, \
			i & 2 ?     0 : +2800, \
			0, 0 \
		); \
	} \
	fs_obj[F_FILE+i]->o_f5 = (float)1/1; \
}
#define FileMenu_InitFileSub(obj, tile, i) \
{ \
	if (ISTRUE(BuFileIsActive(i))) \
	{ \
		fs_obj[tile+i] = FileMenu_MakeTile( \
			obj, S_FILE_MARIO, 9, \
			i & 1 ? -1500 : +6400, \
			i & 2 ?     0 : +2800, \
			-100, -0x8000 \
		); \
	} \
	else \
	{ \
		fs_obj[tile+i] = FileMenu_MakeTile( \
			obj, S_FILE_NEW, 9, \
			i & 1 ? -1500 : +6400, \
			i & 2 ?     0 : +2800, \
			-100, -0x8000 \
		); \
	} \
	fs_obj[tile+i]->o_f5 = (float)1/9; \
}

static void FileMenu_ScoreFile(OBJECT *obj, CHAR back)
{
	if (obj->o_v0 == TILE_OPENED)
	{
		if (cursor_flag == 2)
		{
			Na_FixSePlay(NA_SE7_07);
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
			obj->o_v0 = TILE_CLOSE;
		}
	}
	if (obj->o_v0 == TILE_CLOSED)
	{
		fs_state = back;
		if (fs_mode == 2) fs_mode = 1;
	}
}

static void FileMenu_ScoreInit(OBJECT *obj)
{
	FileMenu_InitFileSub(obj, FS_FILE, 0);
	FileMenu_InitFileSub(obj, FS_FILE, 1);
	FileMenu_InitFileSub(obj, FS_FILE, 2);
	FileMenu_InitFileSub(obj, FS_FILE, 3);
	FileMenu_InitTileSub(obj, FS_SELECT, S_TILE_YELLOW, +6400, -3500);
	FileMenu_InitTileSub(obj, FS_COPY,   S_TILE_BLUE,       0, -3500);
	FileMenu_InitTileSub(obj, FS_ERASE,  S_TILE_RED,    -6400, -3500);
}

static void FileMenu_ScoreProc(OBJECT *obj)
{
	int i;
	if (obj->o_v0 == TILE_OPENED)
	{
		for (i = FS_MIN; i < FS_MAX; i++)
		{
			SHORT x = fs_obj[i]->o_posx;
			SHORT y = fs_obj[i]->o_posy;
			if (ISTRUE(FileIsClick(x, y, 22)) && click_timer > 30)
			{
				if (i == FS_SELECT || i == FS_COPY || i == FS_ERASE)
				{
					Na_FixSePlay(NA_SE7_11);
#ifdef MOTOR
					motor_8024C834(5, 80);
#endif
					fs_obj[i]->o_v0 = TILE_CLICK;
					fs_state = i;
				}
				else if (click_timer > 30)
				{
					if (ISTRUE(BuFileIsActive(i-FS_FILE)))
					{
						Na_FixSePlay(NA_SE7_06);
#ifdef MOTOR
						motor_8024C834(5, 80);
#endif
						fs_obj[i]->o_v0 = TILE_OPEN;
						fs_state = i;
					}
					else
					{
						Na_FixSePlay(NA_SE7_0E);
#ifdef MOTOR
						motor_8024C834(5, 80);
#endif
						fs_obj[i]->o_v0 = TILE_CLICK;
						if (click_timer > 30)
						{
							click_flag = TRUE;
							click_timer = 0;
						}
					}
				}
				fs_mode = 2;
				break;
			}
		}
	}
}

static void FileMenu_CopyInit(OBJECT *obj)
{
	FileMenu_InitFileSub(obj, FC_FILE, 0);
	FileMenu_InitFileSub(obj, FC_FILE, 1);
	FileMenu_InitFileSub(obj, FC_FILE, 2);
	FileMenu_InitFileSub(obj, FC_FILE, 3);
	FileMenu_InitTileSub(obj, FC_SELECT, S_TILE_YELLOW, +6400, -3500);
	FileMenu_InitTileSub(obj, FC_SCORE,  S_TILE_GREEN,      0, -3500);
	FileMenu_InitTileSub(obj, FC_ERASE,  S_TILE_RED,    -6400, -3500);
}

static void FileMenu_CopyFile(OBJECT *obj, int tile)
{
	switch (obj->o_v6)
	{
	case 0:
		if (ISTRUE(fs_full)) return;
		if (ISTRUE(BuFileIsActive(tile-FC_FILE)))
		{
			Na_FixSePlay(NA_SE7_11);
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
			fs_obj[tile]->o_v0 = TILE_SELECT;
			click_file = tile-FC_FILE;
			obj->o_v6 = 1;
			click_flag = TRUE;
			click_timer = 0;
		}
		else
		{
			Na_FixSePlay(NA_SE7_0E);
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
			fs_obj[tile]->o_v0 = TILE_CLICK;
			if (click_timer > 20)
			{
				click_flag = TRUE;
				click_timer = 0;
			}
		}
		break;
	case 1:
		fs_obj[tile]->o_v0 = TILE_CLICK;
		if (ISFALSE(BuFileIsActive(tile-FC_FILE)))
		{
			Na_FixSePlay(NA_SE7_1E);
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
			obj->o_v6 = 2;
			click_flag = TRUE;
			click_timer = 0;
			BuFileCopy(click_file, tile-FC_FILE);
			fs_obj[tile]->s.shape = shape_table[S_FILE_MARIO_S];
			fs_obj[F_FILE+tile-FC_FILE]->s.shape = shape_table[S_FILE_MARIO_S];
		}
		else
		{
			if (tile == FC_FILE+click_file)
			{
				Na_FixSePlay(NA_SE7_0E);
#ifdef MOTOR
				motor_8024C834(5, 80);
#endif
				fs_obj[FC_FILE+click_file]->o_v0 = TILE_DESELECT;
				obj->o_v6 = 0;
				click_flag = TRUE;
				return;
			}
			if (click_timer > 20)
			{
				click_flag = TRUE;
				click_timer = 0;
			}
		}
		break;
	}
}

static void FileMenu_CopyProc(OBJECT *obj)
{
	int i;
	if (obj->o_v0 == TILE_OPENED)
	{
		for (i = FC_MIN; i < FC_MAX; i++)
		{
			SHORT x = fs_obj[i]->o_posx;
			SHORT y = fs_obj[i]->o_posy;
			if (ISTRUE(FileIsClick(x, y, 22)))
			{
				if (i == FC_SELECT || i == FC_SCORE || i == FC_ERASE)
				{
					if (obj->o_v6 == 0)
					{
						Na_FixSePlay(NA_SE7_11);
#ifdef MOTOR
						motor_8024C834(5, 80);
#endif
						fs_obj[i]->o_v0 = TILE_CLICK;
						fs_state = i;
					}
				}
				else
				{
					if (fs_obj[i]->o_v0 == TILE_CLOSED && click_timer > 30)
					{
						FileMenu_CopyFile(obj, i);
					}
				}
				fs_mode = 2;
				break;
			}
		}
		if (obj->o_v6 == 2 && click_timer > 30)
		{
			obj->o_v6 = 0;
			fs_obj[FC_FILE+click_file]->o_v0 = TILE_DESELECT;
		}
	}
}

static void FileMenu_EraseInit(OBJECT *obj)
{
	FileMenu_InitFileSub(obj, FE_FILE, 0);
	FileMenu_InitFileSub(obj, FE_FILE, 1);
	FileMenu_InitFileSub(obj, FE_FILE, 2);
	FileMenu_InitFileSub(obj, FE_FILE, 3);
	FileMenu_InitTileSub(obj, FE_SELECT, S_TILE_YELLOW, +6400, -3500);
	FileMenu_InitTileSub(obj, FE_SCORE,  S_TILE_GREEN,      0, -3500);
	FileMenu_InitTileSub(obj, FE_COPY,   S_TILE_BLUE,   -6400, -3500);
}

static void FileMenu_EraseFile(OBJECT *obj, int tile)
{
	switch (obj->o_v6)
	{
	case 0:
		if (ISTRUE(BuFileIsActive(tile-FE_FILE)))
		{
			Na_FixSePlay(NA_SE7_11);
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
			fs_obj[tile]->o_v0 = TILE_SELECT;
			click_file = tile-FE_FILE;
			obj->o_v6 = 1;
			click_flag = TRUE;
			click_timer = 0;
		}
		else
		{
			Na_FixSePlay(NA_SE7_0E);
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
			fs_obj[tile]->o_v0 = TILE_CLICK;
			if (click_timer > 20)
			{
				click_flag = TRUE;
				click_timer = 0;
			}
		}
		break;
	case 1:
		if (tile == FE_FILE+click_file)
		{
			Na_FixSePlay(NA_SE7_11);
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
			fs_obj[FE_FILE+click_file]->o_v0 = TILE_DESELECT;
			obj->o_v6 = 0;
			click_flag = TRUE;
		}
		break;
	}
}

static void FileMenu_EraseProc(OBJECT *obj)
{
	int i;
	if (obj->o_v0 == TILE_OPENED)
	{
		for (i = FE_MIN; i < FE_MAX; i++)
		{
			SHORT x = fs_obj[i]->o_posx;
			SHORT y = fs_obj[i]->o_posy;
			if (ISTRUE(FileIsClick(x, y, 22)))
			{
				if (i == FE_SELECT || i == FE_SCORE || i == FE_COPY)
				{
					if (obj->o_v6 == 0)
					{
						Na_FixSePlay(NA_SE7_11);
#ifdef MOTOR
						motor_8024C834(5, 80);
#endif
						fs_obj[i]->o_v0 = TILE_CLICK;
						fs_state = i;
					}
				}
				else
				{
					if (click_timer > 30) FileMenu_EraseFile(obj, i);
				}
				fs_mode = 2;
				break;
			}
		}
		if (obj->o_v6 == 2 && click_timer > 30)
		{
			obj->o_v6 = 0;
			fs_obj[FE_FILE+click_file]->o_v0 = TILE_DESELECT;
		}
	}
}

static void FileMenu_OptionInit(OBJECT *obj)
{
	FileMenu_InitTileSub(obj, FO_STEREO, S_TILE_BUTTON, +4800, 0);
	FileMenu_InitTileSub(obj, FO_MONO,   S_TILE_BUTTON,     0, 0);
	FileMenu_InitTileSub(obj, FO_PHONE,  S_TILE_BUTTON, -4800, 0);
	fs_obj[FO_SOUND+sound_flag]->o_v0 = TILE_SELECT;
}

static void FileMenu_OptionProc(OBJECT *obj)
{
	int i;
	if (obj->o_v0 == TILE_OPENED)
	{
		for (i = FO_MIN; i < FO_MAX; i++)
		{
			SHORT x = fs_obj[i]->o_posx;
			SHORT y = fs_obj[i]->o_posy;
			if (ISTRUE(FileIsClick(x, y, 22)))
			{
				if (i == FO_STEREO || i == FO_MONO || i == FO_PHONE)
				{
					if (obj->o_v6 == 0)
					{
						Na_FixSePlay(NA_SE7_11);
#ifdef MOTOR
						motor_8024C834(5, 80);
#endif
						fs_obj[i]->o_v0 = TILE_CLICK;
						fs_state = i;
						sound_flag = i-FO_SOUND;
						BuSetSound(sound_flag);
					}
				}
				fs_mode = 2;
				break;
			}
		}
	}
}

static void FileMenu_OpenFile(OBJECT *obj, int file)
{
	if (obj->o_v0 == TILE_OPENED) fs_result = file;
}

static void FileMenu_OpenSelect(SHORT tile, OBJECT *obj)
{
	int i;
	if (obj->o_v0 == TILE_CLOSED && fs_obj[tile]->o_v0 == TILE_OPENED)
	{
		Na_FixSePlay(NA_SE7_07);
		fs_obj[tile]->o_v0 = TILE_CLOSE;
		fs_mode = 1;
	}
	if (fs_obj[tile]->o_v0 == TILE_CLOSED)
	{
		fs_state = -1;
		if (tile == F_SCORE)
		{
			for (i = FS_MIN; i < FS_MAX; i++) ObjDestroy(fs_obj[i]);
		}
		if (tile == F_COPY)
		{
			for (i = FC_MIN; i < FC_MAX; i++) ObjDestroy(fs_obj[i]);
		}
		if (tile == F_ERASE)
		{
			for (i = FE_MIN; i < FE_MAX; i++) ObjDestroy(fs_obj[i]);
		}
		if (tile == F_OPTION)
		{
			for (i = FO_MIN; i < FO_MAX; i++) ObjDestroy(fs_obj[i]);
		}
	}
}

static void FileMenu_OpenScore(SHORT tile, OBJECT *obj)
{
	int i;
	if (obj->o_v0 == TILE_CLOSED && fs_obj[tile]->o_v0 == TILE_OPENED)
	{
		Na_FixSePlay(NA_SE7_07);
		fs_obj[tile]->o_v0 = TILE_CLOSE;
		fs_mode = 1;
	}
	if (fs_obj[tile]->o_v0 == TILE_CLOSED)
	{
		if (tile == F_SCORE)
		{
			for (i = FS_MIN; i < FS_MAX; i++) ObjDestroy(fs_obj[i]);
		}
		if (tile == F_COPY)
		{
			for (i = FC_MIN; i < FC_MAX; i++) ObjDestroy(fs_obj[i]);
		}
		if (tile == F_ERASE)
		{
			for (i = FE_MIN; i < FE_MAX; i++) ObjDestroy(fs_obj[i]);
		}
		fs_state = F_SCORE;
		Na_FixSePlay(NA_SE7_06);
		fs_obj[F_SCORE]->o_v0 = TILE_OPEN;
		FileMenu_ScoreInit(fs_obj[F_SCORE]);
	}
}

static void FileMenu_OpenCopy(SHORT tile, OBJECT *obj)
{
	int i;
	if (obj->o_v0 == TILE_CLOSED && fs_obj[tile]->o_v0 == TILE_OPENED)
	{
		Na_FixSePlay(NA_SE7_07);
		fs_obj[tile]->o_v0 = TILE_CLOSE;
		fs_mode = 1;
	}
	if (fs_obj[tile]->o_v0 == TILE_CLOSED)
	{
		if (tile == F_SCORE)
		{
			for (i = FS_MIN; i < FS_MAX; i++) ObjDestroy(fs_obj[i]);
		}
		if (tile == F_COPY)
		{
			for (i = FC_MIN; i < FC_MAX; i++) ObjDestroy(fs_obj[i]);
		}
		if (tile == F_ERASE)
		{
			for (i = FE_MIN; i < FE_MAX; i++) ObjDestroy(fs_obj[i]);
		}
		fs_state = F_COPY;
		Na_FixSePlay(NA_SE7_06);
		fs_obj[F_COPY]->o_v0 = TILE_OPEN;
		FileMenu_CopyInit(fs_obj[F_COPY]);
	}
}

static void FileMenu_OpenErase(SHORT tile, OBJECT *obj)
{
	int i;
	if (obj->o_v0 == TILE_CLOSED && fs_obj[tile]->o_v0 == TILE_OPENED)
	{
		Na_FixSePlay(NA_SE7_07);
		fs_obj[tile]->o_v0 = TILE_CLOSE;
		fs_mode = 1;
	}
	if (fs_obj[tile]->o_v0 == TILE_CLOSED)
	{
		if (tile == F_SCORE)
		{
			for (i = FS_MIN; i < FS_MAX; i++) ObjDestroy(fs_obj[i]);
		}
		if (tile == F_COPY)
		{
			for (i = FC_MIN; i < FC_MAX; i++) ObjDestroy(fs_obj[i]);
		}
		if (tile == F_ERASE)
		{
			for (i = FE_MIN; i < FE_MAX; i++) ObjDestroy(fs_obj[i]);
		}
		fs_state = F_ERASE;
		Na_FixSePlay(NA_SE7_06);
		fs_obj[F_ERASE]->o_v0 = TILE_OPEN;
		FileMenu_EraseInit(fs_obj[F_ERASE]);
	}
}

void FileMenu_Init(void)
{
	FileMenu_InitFileSel(0);
	FileMenu_InitFileSel(1);
	FileMenu_InitFileSel(2);
	FileMenu_InitFileSel(3);
	FileMenu_InitTileSel(F_SCORE,  S_TILE_GREEN,  -6400, -3500);
	FileMenu_InitTileSel(F_COPY,   S_TILE_BLUE,   -2134, -3500);
	FileMenu_InitTileSel(F_ERASE,  S_TILE_RED,    +2134, -3500);
	FileMenu_InitTileSel(F_OPTION, S_TILE_PURPLE, +6400, -3500);
	fs_alpha = 0;
}

static void FileMenu_Select(void)
{
	CHAR i;
	if (ISTRUE(FileIsClick(
		fs_obj[F_OPTION]->o_posx, fs_obj[F_OPTION]->o_posy, 200
	)))
	{
		fs_obj[F_OPTION]->o_v0 = TILE_OPEN;
		fs_state = F_OPTION;
	}
	else
	{
		for (i = F_FILE; i < F_FILE+7; i++)
		{
			SHORT x = fs_obj[i]->o_posx;
			SHORT y = fs_obj[i]->o_posy;
			if (ISTRUE(FileIsClick(x, y, 200)))
			{
				fs_obj[i]->o_v0 = TILE_OPEN;
				fs_state = i;
				break;
			}
		}
	}
	switch (fs_state)
	{
	case F_FILE_A:
#if REVISION >= 199609
		Na_FixSePlay(NA_SE7_23);
#else
		Na_FixSePlay(NA_SE7_1E);
#endif
#ifdef MOTOR
		motor_8024C834(60, 70);
		motor_8024C89C(1);
#endif
		break;
	case F_FILE_B:
#if REVISION >= 199609
		Na_FixSePlay(NA_SE7_23);
#else
		Na_FixSePlay(NA_SE7_1E);
#endif
#ifdef MOTOR
		motor_8024C834(60, 70);
		motor_8024C89C(1);
#endif
		break;
	case F_FILE_C:
#if REVISION >= 199609
		Na_FixSePlay(NA_SE7_23);
#else
		Na_FixSePlay(NA_SE7_1E);
#endif
#ifdef MOTOR
		motor_8024C834(60, 70);
		motor_8024C89C(1);
#endif
		break;
	case F_FILE_D:
#if REVISION >= 199609
		Na_FixSePlay(NA_SE7_23);
#else
		Na_FixSePlay(NA_SE7_1E);
#endif
#ifdef MOTOR
		motor_8024C834(60, 70);
		motor_8024C89C(1);
#endif
		break;
	case F_SCORE:
		Na_FixSePlay(NA_SE7_06);
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		FileMenu_ScoreInit(fs_obj[F_SCORE]);
		break;
	case F_COPY:
		Na_FixSePlay(NA_SE7_06);
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		FileMenu_CopyInit(fs_obj[F_COPY]);
		break;
	case F_ERASE:
		Na_FixSePlay(NA_SE7_06);
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		FileMenu_EraseInit(fs_obj[F_ERASE]);
		break;
	case F_OPTION:
		Na_FixSePlay(NA_SE7_06);
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
		FileMenu_OptionInit(fs_obj[F_OPTION]);
		break;
	}
}

void FileMenu_Proc(void)
{
	switch (fs_state)
	{
	case F_SELECT:  FileMenu_Select(); break;
	case F_FILE_A:  FileMenu_OpenFile(fs_obj[F_FILE_A], 1); break;
	case F_FILE_B:  FileMenu_OpenFile(fs_obj[F_FILE_B], 2); break;
	case F_FILE_C:  FileMenu_OpenFile(fs_obj[F_FILE_C], 3); break;
	case F_FILE_D:  FileMenu_OpenFile(fs_obj[F_FILE_D], 4); break;
	case F_SCORE:   FileMenu_ScoreProc(fs_obj[F_SCORE]); break;
	case F_COPY:    FileMenu_CopyProc (fs_obj[F_COPY]);  break;
	case F_ERASE:   FileMenu_EraseProc(fs_obj[F_ERASE]); break;
	case FS_FILE_A: FileMenu_ScoreFile(fs_obj[FS_FILE_A], F_SCORE); break;
	case FS_FILE_B: FileMenu_ScoreFile(fs_obj[FS_FILE_B], F_SCORE); break;
	case FS_FILE_C: FileMenu_ScoreFile(fs_obj[FS_FILE_C], F_SCORE); break;
	case FS_FILE_D: FileMenu_ScoreFile(fs_obj[FS_FILE_D], F_SCORE); break;
	case FS_SELECT: FileMenu_OpenSelect(F_SCORE, fs_obj[FS_SELECT]); break;
	case FS_COPY:   FileMenu_OpenCopy  (F_SCORE, fs_obj[FS_COPY]);   break;
	case FS_ERASE:  FileMenu_OpenErase (F_SCORE, fs_obj[FS_ERASE]);  break;
	case FC_FILE_A: break;
	case FC_FILE_B: break;
	case FC_FILE_C: break;
	case FC_FILE_D: break;
	case FC_SELECT: FileMenu_OpenSelect(F_COPY, fs_obj[FC_SELECT]); break;
	case FC_SCORE:  FileMenu_OpenScore (F_COPY, fs_obj[FC_SCORE]);  break;
	case FC_ERASE:  FileMenu_OpenErase (F_COPY, fs_obj[FC_ERASE]);  break;
	case FE_FILE_A: break;
	case FE_FILE_B: break;
	case FE_FILE_C: break;
	case FE_FILE_D: break;
	case FE_SELECT: FileMenu_OpenSelect(F_ERASE, fs_obj[FE_SELECT]); break;
	case FE_SCORE:  FileMenu_OpenScore (F_ERASE, fs_obj[FE_SCORE]);  break;
	case FE_COPY:   FileMenu_OpenCopy  (F_ERASE, fs_obj[FE_COPY]);   break;
	case F_OPTION:  FileMenu_OptionProc(fs_obj[F_OPTION]); break;
	case FO_STEREO: FileMenu_OpenSelect(F_OPTION, fs_obj[FO_STEREO]); break;
	case FO_MONO:   FileMenu_OpenSelect(F_OPTION, fs_obj[FO_MONO]);   break;
	case FO_PHONE:  FileMenu_OpenSelect(F_OPTION, fs_obj[FO_PHONE]);  break;
	}
	click_pos[0] = -10000;
	click_pos[1] = -10000;
}

static unsigned char str_return[] = {STR_RETURN};
static unsigned char str_view_score[] = {STR_VIEW_SCORE};
static unsigned char str_file_copy[] = {STR_FILE_COPY};
static unsigned char str_file_erase[] = {STR_FILE_ERASE};
static unsigned char str_sound[][8] =
{
	{STR_STEREO},
	{STR_MONO},
	{STR_PHONE},
};
static unsigned char str_mario_a[] = {STR_MARIO_A};
static unsigned char str_mario_b[] = {STR_MARIO_B};
static unsigned char str_mario_c[] = {STR_MARIO_C};
static unsigned char str_mario_d[] = {STR_MARIO_D};
static unsigned char str_new[] = {STR_NEW};

static void FsProcClick(void)
{
	if (
		fs_state == FS_FILE_A ||
		fs_state == FS_FILE_B ||
		fs_state == FS_FILE_C ||
		fs_state == FS_FILE_D
	) 
	{
		if (contp->down & (B_BUTTON|START_BUTTON))
		{
			click_pos[0] = cursor_pos[0];
			click_pos[1] = cursor_pos[1];
			cursor_flag = 1;
		}
		else if (contp->down & A_BUTTON)
		{
			score_flag = 1 - score_flag;
			Na_FixSePlay(NA_SE7_11);
		}
	}
	else
	{
		if (contp->down & (A_BUTTON|B_BUTTON|START_BUTTON))
		{
			click_pos[0] = cursor_pos[0];
			click_pos[1] = cursor_pos[1];
			cursor_flag = 1;
		}
	}
}

static void FsProcCursor(void)
{
	SHORT x = contp->stick_x;
	SHORT y = contp->stick_y;
	if (y > -2 && y < +2) y = 0;
	if (x > -2 && x < +2) x = 0;
	cursor_pos[0] += x/8;
	cursor_pos[1] += y/8;
	if (cursor_pos[0] > +132) cursor_pos[0] = +132;
	if (cursor_pos[0] < -132) cursor_pos[0] = -132;
	if (cursor_pos[1] >  +90) cursor_pos[1] =  +90;
	if (cursor_pos[1] <  -90) cursor_pos[1] =  -90;
	if (!cursor_flag) FsProcClick();
}

static void FsDrawCursor(void)
{
	FsProcCursor();
#ifdef sgi
	GfxTranslate(GFX_PUSH, cursor_pos[0]+160-5.0, cursor_pos[1]+120-25.0, 0);
#else
	GfxTranslate(GFX_PUSH, cursor_pos[0]+160-5, cursor_pos[1]+120-25, 0);
#endif
	if (!cursor_flag) gSPDisplayList(glistp++, gfx_select_cursor_0);
	if ( cursor_flag) gSPDisplayList(glistp++, gfx_select_cursor_1);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	if (cursor_flag)
	{
		cursor_flag++;
		if (cursor_flag == 5) cursor_flag = 0;
	}
}

static void FsPrint16(CHAR font, SHORT x, SHORT y, const unsigned char *str)
{
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha-click_alpha);
	Print16(font, x, y, str);
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
}

static void FsPrintLg(SHORT x, SHORT y, const unsigned char *str)
{
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha-click_alpha);
	PrintLg(x, y, str);
	gSPDisplayList(glistp++, gfx_lgfont_end);
}

static int ClickFade(void)
{
	if (ISTRUE(click_flag))
	{
		click_alpha += 50;
		if (click_alpha == 250)
		{
			click_flag = FALSE;
			return TRUE;
		}
	}
	else
	{
		if (click_alpha > 0) click_alpha -= 50;
	}
	return FALSE;
}

static void FsDrawSelectFile(CHAR file, SHORT x, SHORT y)
{
	static unsigned char str_star[] = {CH16_STAR,CH_NUL};
	static unsigned char str_cross[] = {CH16_CROSS,CH_NUL};
	unsigned char buf[4];
	CHAR offset = 0;
	if (ISTRUE(BuFileIsActive(file)))
	{
		SHORT total = BuFileStarTotal(file);
		Print16(FONT_GLB, x, y, str_star);
		if (total < 100)
		{
			Print16(FONT_GLB, x+16, y, str_cross);
			offset = 16;
		}
		IntToStr(total, buf);
		Print16(FONT_GLB, x+16+offset, y, buf);
	}
	else
	{
		Print16(FONT_GLB, x, y, str_new);
	}
}

static void FsDrawSelect(void)
{
	static unsigned char str_banner_select[] = {STR_BANNER_SELECT};
	static unsigned char str_score[] = {STR_SCORE};
	static unsigned char str_copy[] = {STR_COPY};
	static unsigned char str_erase[] = {STR_ERASE};
#if REVISION >= 199609
#ifdef sgi
	static short sound_x;
#else
	SHORT sound_x;
#endif
#endif
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
#ifdef JAPANESE
	Print16(FONT_SEL, 96, 35, str_banner_select);
#endif
#ifdef ENGLISH
	Print16(FONT_GLB, 93, 35, str_banner_select);
#endif
	FsDrawSelectFile(0,  92,  78);
	FsDrawSelectFile(1, 209,  78);
	FsDrawSelectFile(2,  92, 118);
	FsDrawSelectFile(3, 209, 118);
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
#ifdef JAPANESE
	PrintLg( 50, 39, str_score);
	PrintLg(115, 39, str_copy);
	PrintLg(180, 39, str_erase);
#endif
#ifdef ENGLISH
	PrintLg( 52, 39, str_score);
	PrintLg(117, 39, str_copy);
	PrintLg(177, 39, str_erase);
#endif
#if REVISION >= 199609
	sound_x = StrCenterX(254, str_sound[sound_flag], 10);
	PrintLg(sound_x, 39, str_sound[sound_flag]);
#else
#ifdef JAPANESE
	PrintLg(235, 39, str_sound[sound_flag]);
#endif
#endif
	gSPDisplayList(glistp++, gfx_lgfont_end);
	gSPDisplayList(glistp++, gfx_smfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
	PrintSm( 92,  65, str_mario_a);
	PrintSm(207,  65, str_mario_b);
	PrintSm( 92, 105, str_mario_c);
	PrintSm(207, 105, str_mario_d);
	gSPDisplayList(glistp++, gfx_smfont_end);
}

static void FsDrawScoreMsg(CHAR msg)
{
	static unsigned char str_banner_score[] = {STR_BANNER_SCORE};
	static unsigned char str_no_data[] = {STR_NO_DATA};
	switch (msg)
	{
#ifdef JAPANESE
	case 0: FsPrint16(FONT_SEL, 90, 35, str_banner_score); break;
	case 1: FsPrintLg(90, 190, str_no_data); break;
#endif
#ifdef ENGLISH
	case 0: FsPrint16(FONT_GLB, 95, 35, str_banner_score); break;
	case 1: FsPrintLg(99, 190, str_no_data); break;
#endif
	}
}

static void FsDrawScore(void)
{
	if (click_timer == 20) click_flag = TRUE;
	if (ISTRUE(ClickFade()))
	{
		if (click_msg == 0) click_msg = 1;
		else                click_msg = 0;
	}
	FsDrawScoreMsg(click_msg);
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
	FsDrawSelectFile(0,  90,  76);
	FsDrawSelectFile(1, 211,  76);
	FsDrawSelectFile(2,  90, 119);
	FsDrawSelectFile(3, 211, 119);
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
#ifdef JAPANESE
	PrintLg( 45, 35, str_return);
	PrintLg(128, 35, str_file_copy);
	PrintLg(228, 35, str_file_erase);
#endif
#ifdef ENGLISH
	PrintLg( 44, 35, str_return);
	PrintLg(135, 35, str_file_copy);
	PrintLg(231, 35, str_file_erase);
#endif
	gSPDisplayList(glistp++, gfx_lgfont_end);
	gSPDisplayList(glistp++, gfx_smfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
	PrintSm( 89,  62, str_mario_a);
	PrintSm(211,  62, str_mario_b);
	PrintSm( 89, 105, str_mario_c);
	PrintSm(211, 105, str_mario_d);
	gSPDisplayList(glistp++, gfx_smfont_end);
}

static void FsDrawCopyMsg(CHAR msg)
{
	static unsigned char str_banner_copy[] = {STR_BANNER_COPY};
	static unsigned char str_copy_where[] = {STR_COPY_WHERE};
	static unsigned char str_no_data[] = {STR_NO_DATA};
	static unsigned char str_copy_finish[] = {STR_COPY_FINISH};
	static unsigned char str_data_exist[] = {STR_DATA_EXIST};
	static unsigned char str_no_empty[] = {STR_NO_EMPTY};
	switch (msg)
	{
	case 0:
#ifdef JAPANESE
		if (ISTRUE(fs_full))    FsPrintLg(90, 190, str_no_empty);
		else                    FsPrint16(FONT_SEL, 90, 35, str_banner_copy);
		break;
	case 1: FsPrintLg(90, 190, str_copy_where);    break;
	case 2: FsPrintLg(90, 190, str_no_data);       break;
	case 3: FsPrintLg(90, 190, str_copy_finish);   break;
	case 4: FsPrintLg(90, 190, str_data_exist);    break;
#endif
#ifdef ENGLISH
		if (ISTRUE(fs_full))    FsPrintLg(119, 190, str_no_empty);
		else                    FsPrint16(FONT_GLB, 104, 35, str_banner_copy);
		break;
	case 1: FsPrintLg(109, 190, str_copy_where);    break;
	case 2: FsPrintLg(101, 190, str_no_data);       break;
	case 3: FsPrintLg(110, 190, str_copy_finish);   break;
	case 4: FsPrintLg(110, 190, str_data_exist);    break;
#endif
	}
}

static void FsProcCopy(void)
{
	switch (fs_obj[F_COPY]->o_v6)
	{
	case 0:
		if (click_timer == 20) click_flag = TRUE;
		if (ISTRUE(ClickFade()))
		{
			if (click_msg == 0) click_msg = 2;
			else                click_msg = 0;
		}
		break;
	case 1:
		if (click_timer == 20 && click_msg == 4) click_flag = TRUE;
		if (ISTRUE(ClickFade()))
		{
			if (click_msg != 1) click_msg = 1;
			else                click_msg = 4;
		}
		break;
	case 2:
		if (click_timer == 20) click_flag = TRUE;
		if (ISTRUE(ClickFade()))
		{
			if (click_msg != 3) click_msg = 3;
			else                click_msg = 0;
		}
		break;
	}
}

static void FsDrawCopy(void)
{
	FsProcCopy();
	FsDrawCopyMsg(click_msg);
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
	FsDrawSelectFile(0,  90,  76);
	FsDrawSelectFile(1, 211,  76);
	FsDrawSelectFile(2,  90, 119);
	FsDrawSelectFile(3, 211, 119);
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
#ifdef JAPANESE
	PrintLg( 45, 35, str_return);
	PrintLg(133, 35, str_view_score);
#endif
#ifdef ENGLISH
	PrintLg( 44, 35, str_return);
	PrintLg(128, 35, str_view_score);
#endif
#if REVISION >= 199609
	PrintLg(230, 35, str_file_erase);
#else
	PrintLg(220, 35, str_file_erase);
#endif
	gSPDisplayList(glistp++, gfx_lgfont_end);
	gSPDisplayList(glistp++, gfx_smfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
	PrintSm( 89,  62, str_mario_a);
	PrintSm(211,  62, str_mario_b);
	PrintSm( 89, 105, str_mario_c);
	PrintSm(211, 105, str_mario_d);
	gSPDisplayList(glistp++, gfx_smfont_end);
}

static void FsDrawErasePrompt(SHORT x, SHORT y)
{
	static unsigned char str_yes[] = {STR_YES};
	static unsigned char str_no[] = {STR_NO};
	SHORT theta = 0x1000*gfx_frame;
#if REVISION >= 199609
	SHORT posx = cursor_pos[0] + (x+70);
	SHORT posy = cursor_pos[1] + 120;
#else
	SHORT posx = cursor_pos[0] + 160;
	SHORT posy = cursor_pos[1] + 120;
#endif
#ifdef JAPANESE
	if (posx < 164 && posx > 144 && posy < 210 && posy > 190)
#endif
#ifdef ENGLISH
	if (posx < 169 && posx > 139 && posy < 210 && posy > 190)
#endif
	{
		blink[0] = 0xFF-50 + 50*SIN(theta);
		blink[1] = 150;
		erase_flag = 1;
	}
#if REVISION >= 199707
	else if (posx < 213 && posx > 193 && posy < 210 && posy > 190)
#else
	else if (posx < 218 && posx > 188 && posy < 210 && posy > 190)
#endif
	{
		blink[0] = 150;
		blink[1] = 0xFF-50 + 50*SIN(theta);
		erase_flag = 2;
	}
	else
	{
		blink[0] = 150;
		blink[1] = 150;
		erase_flag = 0;
	}
	if (cursor_flag == 2)
	{
		if (erase_flag == 1)
		{
			Na_FixSePlay(NA_SE2_10);
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
			fs_obj[F_ERASE]->o_v6 = 2;
			click_flag = TRUE;
			click_timer = 0;
			BuFileErase(click_file);
			fs_obj[FE_FILE+click_file]->s.shape = shape_table[S_FILE_NEW_S];
			fs_obj[F_FILE+click_file]->s.shape = shape_table[S_FILE_NEW_S];
			erase_flag = 0;
		}
		else if (erase_flag == 2)
		{
			Na_FixSePlay(NA_SE7_11);
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
			fs_obj[FE_FILE+click_file]->o_v0 = TILE_DESELECT;
			fs_obj[F_ERASE]->o_v6 = 0;
			click_flag = TRUE;
			click_timer = 0;
			erase_flag = 0;
		}
	}
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, blink[0], blink[0], blink[0], fs_alpha);
	PrintLg(x+56, y, str_yes);
	gDPSetEnvColor(glistp++, blink[1], blink[1], blink[1], fs_alpha);
	PrintLg(x+98, y, str_no);
	gSPDisplayList(glistp++, gfx_lgfont_end);
}

static void FsDrawEraseMsg(CHAR msg)
{
	STATIC unsigned char str_banner_erase[] = {STR_BANNER_ERASE};
	STATIC unsigned char str_really[] = {STR_REALLY};
	STATIC unsigned char str_no_data[] = {STR_NO_DATA};
	STATIC unsigned char str_erased[] = {STR_ERASED};
	STATIC unsigned char str_data_exist[] = {STR_DATA_EXIST};
	switch (msg)
	{
#ifdef JAPANESE
	case 0:
#if REVISION >= 199707
		FsPrint16(FONT_SEL, 111, 35, str_banner_erase);
#else
		FsPrint16(FONT_SEL, 96, 35, str_banner_erase);
#endif
		break;
	case 1:
		FsPrintLg(90, 190, str_really);
		FsDrawErasePrompt(90, 190);
		break;
	case 2:
		FsPrintLg(90, 190, str_no_data);
		break;
	case 3:
		str_erased[3] = CH_A + click_file;
		FsPrintLg(90, 190, str_erased);
		break;
	case 4:
		FsPrintLg(90, 190, str_data_exist);
		break;
#endif
#ifdef ENGLISH
	case 0:
		FsPrint16(FONT_GLB, 98, 35, str_banner_erase);
		break;
	case 1:
		FsPrintLg(90, 190, str_really);
		FsDrawErasePrompt(90, 190);
		break;
	case 2:
		FsPrintLg(100, 190, str_no_data);
		break;
	case 3:
		str_erased[6] = CH_A + click_file;
		FsPrintLg(100, 190, str_erased);
		break;
	case 4:
		FsPrintLg(100, 190, str_data_exist);
		break;
#endif
	}
}

static void FsProcErase(void)
{
	switch (fs_obj[F_ERASE]->o_v6)
	{
	case 0:
		if (click_timer == 20 && click_msg == 2) click_flag = TRUE;
		if (ISTRUE(ClickFade()))
		{
			if (click_msg == 0) click_msg = 2;
			else                click_msg = 0;
		}
		break;
	case 1:
		if (ISTRUE(ClickFade()))
		{
			if (click_msg != 1) click_msg = 1;
			cursor_pos[0] = 43;
			cursor_pos[1] = 80;
		}
		break;
	case 2:
		if (click_timer == 20) click_flag = TRUE;
		if (ISTRUE(ClickFade()))
		{
			if (click_msg != 3) click_msg = 3;
			else                click_msg = 0;
		}
		break;
	}
}

static void FsDrawErase(void)
{
	FsProcErase();
	FsDrawEraseMsg(click_msg);
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
	FsDrawSelectFile(0,  90,  76);
	FsDrawSelectFile(1, 211,  76);
	FsDrawSelectFile(2,  90, 119);
	FsDrawSelectFile(3, 211, 119);
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
#ifdef JAPANESE
	PrintLg( 45, 35, str_return);
	PrintLg(133, 35, str_view_score);
	PrintLg(223, 35, str_file_copy);
#endif
#ifdef ENGLISH
	PrintLg( 44, 35, str_return);
	PrintLg(127, 35, str_view_score);
	PrintLg(233, 35, str_file_copy);
#endif
	gSPDisplayList(glistp++, gfx_lgfont_end);
	gSPDisplayList(glistp++, gfx_smfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
	PrintSm( 89,  62, str_mario_a);
	PrintSm(211,  62, str_mario_b);
	PrintSm( 89, 105, str_mario_c);
	PrintSm(211, 105, str_mario_d);
	gSPDisplayList(glistp++, gfx_smfont_end);
}

static void FsDrawOption(void)
{
	int i;
#if REVISION >= 199609
	SHORT x;
#endif
	UNUSED u8 alpha;
	STATIC unsigned char str_banner_option[] = {STR_BANNER_OPTION};
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
#ifdef JAPANESE
	Print16(FONT_SEL, 96, 35, str_banner_option);
#endif
#ifdef ENGLISH
	Print16(FONT_GLB, 88, 35, str_banner_option);
#endif
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	for (i = 0; i < 3; i++)
	{
		if (i == sound_flag)
		{
			gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
		}
		else
		{
			gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, fs_alpha);
		}
#if REVISION >= 199609
		x = StrCenterX(87 + 74*i, str_sound[i], 10);
		PrintLg(x, 87, str_sound[i]);
#else
		PrintLg(67 + 74*i, 87, str_sound[i]);
#endif
	}
	gSPDisplayList(glistp++, gfx_lgfont_end);
}

static void FsDrawExtraStar(CHAR file, SHORT x, SHORT y)
{
	unsigned char buf[20];
	static unsigned char str_star_x[] = {CH_STAR,CH_CROSS,CH_NUL};
	PrintSm(x, y, str_star_x);
	IntToStr(BuFileStarExtra(file), buf);
	PrintSm(x+16, y, buf);
}

static void FsDrawCourseScore(CHAR file, SHORT course, SHORT x, SHORT y)
{
	unsigned char buf[20];
	UCHAR star = BuFileGetStar(file, course);
	STATIC unsigned char str_coin_x[] = {CH_COIN,CH_CROSS,CH_NUL};
	STATIC unsigned char str_star[] = {CH_STAR,CH_NUL};
#ifdef JAPANESE
	STATIC unsigned char str_file[][5] =
	{
		{CH_HYPHEN,CH_HYPHEN,CH_HYPHEN,CH_HYPHEN,CH_NUL},
		{CH_K_MA,CH_K_RI,CH_K_O,CH_A,CH_NUL},
		{CH_K_MA,CH_K_RI,CH_K_O,CH_B,CH_NUL},
		{CH_K_MA,CH_K_RI,CH_K_O,CH_C,CH_NUL},
		{CH_K_MA,CH_K_RI,CH_K_O,CH_D,CH_NUL},
	};
#endif
#ifdef ENGLISH
	STATIC unsigned char str_file[][8] =
	{
		{CH_HYPHEN,CH_HYPHEN,CH_HYPHEN,CH_HYPHEN,CH_NUL},
		{SM_MARIOL,SM_MARIOR,CH_A,CH_NUL},
		{SM_MARIOL,SM_MARIOR,CH_B,CH_NUL},
		{SM_MARIOL,SM_MARIOR,CH_C,CH_NUL},
		{SM_MARIOL,SM_MARIOR,CH_D,CH_NUL},
	};
#endif
	if (score_flag == 0)
	{
		PrintSm(x+25, y, str_coin_x);
		IntToStr(BuFileGetCoin(file, course), buf);
		PrintSm(x+41, y, buf);
		if (star & 0100) PrintSm(x+70, y, str_star);
	}
	else
	{
#ifdef JAPANESE
		PrintSm(x, y, str_coin_x);
		IntToStr(BuGetHiScoreCoin(course), buf);
		PrintSm(x+16, y, buf);
		PrintSm(x+45, y, str_file[BuGetHiScoreFile(course)]);
#endif
#ifdef ENGLISH
		PrintSm(x+18, y, str_coin_x);
		IntToStr(BuGetHiScoreCoin(course), buf);
		PrintSm(x+34, y, buf);
		PrintSm(x+60, y, str_file[BuGetHiScoreFile(course)]);
#endif
	}
}

static void FsDrawCourseStar(CHAR file, SHORT course, SHORT x, SHORT y)
{
	SHORT i = 0;
	unsigned char buf[20];
	UCHAR star = BuFileGetStar(file, course);
	CHAR count = BuFileStarCount(file, course);
	if (star & 0100) count--;
	for (i = 0; i < count; i++) buf[i] = CH_STAR;
	buf[i] = CH_NUL;
	PrintSm(x, y, buf);
}

#ifdef JAPANESE
#if REVISION >= 199707
#define FsPrintCourse(crstab, i) \
{ \
	PrintSm(23+5*(i<9), 35+12*i, SegmentToVirtual(crstab[i])); \
	FsDrawCourseStar(file, i, 152, 35+12*i); \
	FsDrawCourseScore(file, i, 213, 35+12*i); \
}
#else
#define FsPrintCourse(crstab, i) \
{ \
	PrintSm(23, 35+12*i, SegmentToVirtual(crstab[i])); \
	FsDrawCourseStar(file, i, 152, 35+12*i); \
	FsDrawCourseScore(file, i, 213, 35+12*i); \
}
#endif
#endif
#ifdef ENGLISH
#define FsPrintCourse(crstab, i) \
{ \
	PrintSm(23+3*(i<9), 35+12*i, SegmentToVirtual(crstab[i])); \
	FsDrawCourseStar(file, i, 171, 35+12*i); \
	FsDrawCourseScore(file, i, 213, 35+12*i); \
}
#endif

static void FsDrawScoreFile(CHAR file)
{
	STATIC unsigned char str_banner_mario[] = {STR_BANNER_MARIO};
#if REVISION >= 199609
	STATIC unsigned char str_hi_score[] = {STR_HI_SCORE};
	STATIC unsigned char str_my_score[] = {STR_MY_SCORE};
#endif
	unsigned char str_number[] = {0,CH_NUL};
	unsigned char **crstab = SegmentToVirtual(coursename);
#if REVISION < 199609
	STATIC unsigned char str_hi_score[] = {STR_HI_SCORE};
	STATIC unsigned char str_my_score[] = {STR_MY_SCORE};
#endif
	str_number[0] = CH_A + file;
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
#ifdef JAPANESE
	Print16(FONT_SEL, 28, 15, str_banner_mario);
	Print16(FONT_GLB, 86, 15, str_number);
#endif
#ifdef ENGLISH
	Print16(FONT_GLB, 25, 15, str_banner_mario);
	Print16(FONT_GLB, 95, 15, str_number);
#endif
	FsDrawSelectFile(file, 124, 15);
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
	gSPDisplayList(glistp++, gfx_smfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, fs_alpha);
	FsPrintCourse(crstab, 0);
	FsPrintCourse(crstab, 1);
	FsPrintCourse(crstab, 2);
	FsPrintCourse(crstab, 3);
	FsPrintCourse(crstab, 4);
	FsPrintCourse(crstab, 5);
	FsPrintCourse(crstab, 6);
	FsPrintCourse(crstab, 7);
	FsPrintCourse(crstab, 8);
	FsPrintCourse(crstab, 9);
	FsPrintCourse(crstab, 10);
	FsPrintCourse(crstab, 11);
	FsPrintCourse(crstab, 12);
	FsPrintCourse(crstab, 13);
	FsPrintCourse(crstab, 14);
#ifdef JAPANESE
#if REVISION >= 199707
	PrintSm(33, 215, SegmentToVirtual(crstab[25]));
#else
	PrintSm(23, 215, SegmentToVirtual(crstab[25]));
#endif
	FsDrawExtraStar(file, 152, 215);
	if (score_flag == 0)    PrintSm(237, 24, str_my_score);
	else                    PrintSm(237, 24, str_hi_score);
#endif
#ifdef ENGLISH
	PrintSm(29, 215, SegmentToVirtual(crstab[25]));
	FsDrawExtraStar(file, 171, 215);
	if (score_flag == 0)    PrintSm(238, 24, str_my_score);
	else                    PrintSm(231, 24, str_hi_score);
#endif
	gSPDisplayList(glistp++, gfx_smfont_end);
}

static void FsDraw(void)
{
	UNUSED int i;
	GfxScreenProj();
	switch (fs_state)
	{
	case F_SELECT:  FsDrawSelect(); break;
	case F_SCORE:   FsDrawScore(); score_flag = 0; break;
	case F_COPY:    FsDrawCopy();   break;
	case F_ERASE:   FsDrawErase();  break;
	case FS_FILE_A: FsDrawScoreFile(0);  break;
	case FS_FILE_B: FsDrawScoreFile(1);  break;
	case FS_FILE_C: FsDrawScoreFile(2);  break;
	case FS_FILE_D: FsDrawScoreFile(3);  break;
	case F_OPTION:  FsDrawOption(); break;
	}
	if (
		ISTRUE(BuFileIsActive(0)) &&
		ISTRUE(BuFileIsActive(1)) &&
		ISTRUE(BuFileIsActive(2)) &&
		ISTRUE(BuFileIsActive(3))
	) fs_full = TRUE;
	else fs_full = FALSE;
	if (fs_alpha < 250) fs_alpha += 10;
	if (click_timer < 1000) click_timer++;
}

void *FileSelectDraw(int code, UNUSED SHAPE *shape, UNUSED void *data)
{
	if (code == SC_DRAW)
	{
		FsDraw();
		FsDrawCursor();
	}
	return NULL;
}

long FileSelectInit(UNUSED SHORT code, UNUSED long status)
{
	fs_state = -1;
	fs_mode = 1;
	fs_alpha = 0;
	switch (file_index)
	{
	case 1: cursor_pos[0] = -94; cursor_pos[1] =  46; break;
	case 2: cursor_pos[0] =  24; cursor_pos[1] =  46; break;
	case 3: cursor_pos[0] = -94; cursor_pos[1] =   5; break;
	case 4: cursor_pos[0] =  24; cursor_pos[1] =   5; break;
	}
	click_pos[0] = -10000;
	click_pos[1] = -10000;
	cursor_flag = 0;
	fs_result = 0;
	click_file = -1;
	click_flag = FALSE;
	click_msg = 0;
	click_alpha = 0;
	click_timer = 0;
	erase_flag = 0;
	sound_flag = BuGetSound();
#ifndef sgi
	return 1;
#endif
}

long FileSelectProc(UNUSED SHORT code, UNUSED long status)
{
	SceneProc();
	return fs_result;
}
