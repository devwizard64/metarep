import main

str_math = """
#ifdef __GNUC__
#define sqrtf(x) __builtin_sqrtf(x)
#endif

#define SIN(x)                  sintable[(u16)(x) >> 4]
#define COS(x)                  costable[(u16)(x) >> 4]

#define ABS(x)                  ((x) > 0 ? (x) : -(x))
#define SQUARE(x)               ((x)*(x))

#define CROSS3(x0, y0, x1, y1, x2, y2) \\
	(((y1)-(y0))*((x2)-(x1)) - ((x1)-(x0))*((y2)-(y1)))

#define DIST2(x, y)     sqrtf((x)*(x) + (y)*(y))
#define DIST3(x, y, z)  sqrtf((x)*(x) + (y)*(y) + (z)*(z))

#define MDOT3(m, i, x, y, z) ((m)[0][i]*(x) + (m)[1][i]*(y) + (m)[2][i]*(z))
#define IDOT3(m, i, x, y, z) ((m)[i][0]*(x) + (m)[i][1]*(y) + (m)[i][2]*(z))
"""

str_memory = """
#define MEM_ALLOC_L 0
#define MEM_ALLOC_R 1

#define malloc(size)            HeapAlloc(mem_heap, size)
#define free(ptr)               HeapFree(mem_heap, ptr)
"""

str_main = """
#define SCREEN_WD               320
#define SCREEN_HT               240
#define BORDER_HT               8

#define SC_AUDCLIENT            1
#define SC_GFXCLIENT            2
"""

str_Na = """
#define NA_OUTPUT_WIDE          0
#define NA_OUTPUT_PHONE         1
#define NA_OUTPUT_STEREO        2
#define NA_OUTPUT_MONO          3

#define NA_HANDLE_BGM           0
#define NA_HANDLE_FGM           1
#define NA_HANDLE_SE            2

#define Na_FixSePlay(se)        Na_SePlay(se, Na_0)
#define Na_ObjSePlay(se, obj)   Na_SePlay(se, (obj)->s.view)
#define Na_ObjSeStop(se, obj)   Na_SeStop(se, (obj)->s.view)
#define Na_ObjSeKill(obj)       Na_SeKill((obj)->s.view)

#define Na_Se2_00()             (NA_SE2_00 + ((Na_Random % 3) << 16))
#define Na_Se2_2B()             (NA_SE2_2B + ((Na_Random % 5) << 16))

#define Na_LockSe()             Na_PortLock(NA_HANDLE_SE, 0x037A)
#define Na_UnlockSe()           Na_PortUnlock(NA_HANDLE_SE, 0x037A)
#define Na_StaffLockSe()        Na_PortLock(NA_HANDLE_SE, 0x03FF)
#define Na_StaffUnlockSe()      Na_PortUnlock(NA_HANDLE_SE, 0x03FF)
#define Na_EndingLockSe()       Na_PortLock(NA_HANDLE_SE, 0x03F0)
#define Na_EndingUnlockSe()     Na_PortUnlock(NA_HANDLE_SE, 0x03F0)
#define Na_OpeningLockSe()      Na_PortLock(NA_HANDLE_SE, 0x0330)
#define Na_OpeningUnlockSe()    Na_PortUnlock(NA_HANDLE_SE, 0x0330)

typedef u32 Na_Se;
"""

str_graphics = """
#define GFX_LEN                 6400
#define FIFO_SIZE               0x1F000
#define FIFO_LEN                (FIFO_SIZE/8)

#define CONTROLLER_MAX          2

#define CONT_EXIT               0x0080
"""

str_audio = """
#define AUD_PAUSE               1
#define AUD_QUIET               2
"""

str_time = """
#define TIME_GFXCPU_START       0
#define TIME_GFXCPU_ENDPRC      1
#define TIME_GFXCPU_ENDFRM      2
#define TIME_GFXCPU_ENDRDP      3
#define TIME_GFXCPU_END         4
#define TIME_GFXCPU_MAX         5

#define TIME_GFXRCP_START       0
#define TIME_GFXRCP_ENDRSP      1
#define TIME_GFXRCP_ENDRDP      2
#define TIME_GFXRCP_MAX         3

#define TIME_AUDCPU_MAX         8

#define TIME_AUDRCP_MAX         8
"""

str_shape = """
#define SF_CALLBACK             0x100

#define ST_SCENE                (1)
#define ST_ORTHO                (2)
#define ST_PERSP                (3 | SF_CALLBACK)
#define ST_LAYER                (4)

#define ST_EMPTY                (10)
#define ST_LOD                  (11)
#define ST_SELECT               (12 | SF_CALLBACK)

#define ST_CAMERA               (20 | SF_CALLBACK)
#define ST_COORD                (21)
#define ST_POS                  (22)
#define ST_ANG                  (23)
#define ST_OBJECT               (24)
#define ST_JOINT                (25)
#define ST_BILLBOARD            (26)
#define ST_GFX                  (27)
#define ST_SCALE                (28)

#define ST_SHADOW               (40)
#define ST_BRANCH               (41)
#define ST_CALLBACK             (42 | SF_CALLBACK)
#define ST_BACK                 (44 | SF_CALLBACK)
#define ST_HAND                 (46 | SF_CALLBACK)
#define ST_CULL                 (47)

#define SHP_ACTIVE              0x0001
#define SHP_HIDE                0x0002
#define SHP_BILLBOARD           0x0004
#define SHP_ZBUFFER             0x0008
#define SHP_OBJHIDE             0x0010
#define SHP_ANIME               0x0020

#define SC_INIT                 0
#define SC_DRAW                 1
#define SC_CLOSE                2
#define SC_OPEN                 3
#define SC_EXIT                 4
#define SC_MTX                  5

#define ShpGetLayer(shp)  ((shp)->flag >> 8)
#define ShpSetLayer(shp, layer) \\
	((shp)->flag = (layer) << 8 | ((shp)->flag & 0xFF))
"""

str_object = """
#define OBJECT_MAX              240

#define OBJ_HIT_MAX             4
#define OBJ_MEM_MAX             80

#define ObjGetArg(obj)          ((obj)->o_actorinfo >> 24)
#define ObjSetArg(obj, arg)     ((obj)->o_actorinfo = (arg) << 24)
#define ObjGetCode(obj)         (((obj)->o_actorinfo & 0x00FF0000) >> 16)
#define ObjSetCode(obj, code)   ((obj)->o_actorinfo = ((code) & 0xFF) << 16)
"""

str_map = """
#define BG_GROUND               0
#define BG_ROOF                 1
#define BG_WALL                 2

#define BG_MOVE                 1
#define BG_0002                 2
#define BG_WALL_Z               8

#define BGAREA_SIZE             1024
#define BGAREA_N                16
#define BGAREA_MASK             15

#define MAP_SIZE                (BGAREA_SIZE*BGAREA_N)
#define MAP_HALF                (MAP_SIZE/2)

#define BGAREA_FUZZ             50
"""

str_debug = """
#define DEBUG_SHOW              1
#define DEBUG_2                 2
#define DEBUG_ALL               0xFF
"""

str_wipe = """
#define WIPE_ISIN(type)         (!((type) & 1))
#define WIPE_ISOUT(type)        ((type) & 1)
"""

str_background = """
#define BACK_TW                 10
#define BACK_TH                 8
"""

str_message = """
#define GFX_PUSH                1
#define GFX_NOPUSH              2

#define FONT_SEL                1
#define FONT_GLB                2

#define CURSOR_V                1
#define CURSOR_H                2
"""

str_tag = """
#define TAG_START               31
#define TAG_END                 (TAG_START+(-1))

#define MAP_EXT_NULL            0
#define MAP_EXT_ANG             1
#define MAP_EXT_ANG_CODE        2
#define MAP_EXT_XYZ             3
#define MAP_EXT_ANG_ARG         4

#define TAG(tag, angy, posx, posy, posz, code) \\
	(TAG)((TAG_START+TAG_##tag) | (angy) << 9), posx, posy, posz, (u8)(code)
"""

str_hud = """
#define HUD_LIFE                0x0001
#define HUD_COIN                0x0002
#define HUD_STAR                0x0004
#define HUD_METER               0x0008
#define HUD_KEY                 0x0010
#define HUD_TIME                0x0040
#define HUD_ALERT               0x8000

#define HUD_ALL                 0x007F
"""

str_scene = """
#define SCENE_MAX               8
#define SHAPE_MAX               256

#define CONNECT_MAX             4

#define SN_ACTIVE               1

#define STAFF_L                 0x00
#define STAFF_R                 0x10
#define STAFF_T                 0x00
#define STAFF_B                 0x20
#define STAFF_TL                (STAFF_T|STAFF_L)
#define STAFF_TR                (STAFF_T|STAFF_R)
#define STAFF_BL                (STAFF_B|STAFF_L)
#define STAFF_BR                (STAFF_B|STAFF_R)
"""

str_player = """
#define PL_JUMPVOICE            0
#define PL_NULLVOICE            ((Na_Se)-1)

#define SLIP_DEFAULT            0
#define SLIP_19                 19
#define SLIP_20                 20
#define SLIP_21                 21
"""

str_game = """
#define ENTER_DOOR              0x01
#define ENTER_02                0x02
#define ENTER_03                0x03
#define ENTER_04                0x04
#define ENTER_10                0x10
#define ENTER_11                0x11
#define ENTER_12                0x12
#define ENTER_13                0x13
#define ENTER_14                0x14
#define ENTER_15                0x15
#define ENTER_16                0x16
#define ENTER_17                0x17
#define ENTER_20                0x20
#define ENTER_21                0x21
#define ENTER_22                0x22
#define ENTER_23                0x23
#define ENTER_24                0x24
#define ENTER_25                0x25
#define ENTER_27                0x27

#define FADE_EXIT               0x10

#define FADE_NULL               0
#define FADE_ROOF               1
#define FADE_2                  2 /* BBH entry? */
#define FADE_DOOR               3
#define FADE_PIPE               4
#define FADE_5                  5 /* teleport */
#define FADE_WIN                (FADE_EXIT|1)
#define FADE_DIE                (FADE_EXIT|2)
#define FADE_FALL               (FADE_EXIT|3)
#define FADE_GAMEOVER           (FADE_EXIT|4)
#define FADE_ENDING             (FADE_EXIT|5)
#define FADE_FACE               (FADE_EXIT|6)
#define FADE_FINAL              (FADE_EXIT|7)
#define FADE_STAFF              (FADE_EXIT|8)
#define FADE_LOGO               (FADE_EXIT|9)

#define GmTimeShow()            GmTimeCtrl(0)
#define GmTimeStart()           GmTimeCtrl(1)
#define GmTimeStop()            GmTimeCtrl(2)
#define GmTimeHide()            GmTimeCtrl(3)
#define GmTimeGet()             GmTimeCtrl(4)

typedef void FREEZECALL(short *);
"""

str_backup = """
#define StageToCourse(stage)  coursetab[(stage)-1]

#define BuGetHiScoreCoin(course)    ((u16)(BuGetHiScore(course) & 0xFFFF))
#define BuGetHiScoreFile(course)    ((u16)(BuGetHiScore(course) >> 16))

#define BuFileStarTotal(file) BuFileStarRange(file, COURSE_MIN-1, COURSE_MAX-1)
#define BuFileStarExtra(file) BuFileStarRange(file, COURSE_EXT-1, COURSE_MAX-1)

#define BuWrite()                   BuFileWrite(file_index-1)
#define BuErase()                   BuFileErase(file_index-1)
#define BuIsActive()                BuFileIsActive(file_index-1)
#define BuStarCount(course)         BuFileStarCount(file_index-1, course)
#define BuStarRange(min, max)       BuFileStarRange(file_index-1, min, max)
#define BuStarExtra()               BuFileStarExtra(file_index-1)
#define BuStarTotal()               BuFileStarTotal(file_index-1)
#define BuGetStar(course)           BuFileGetStar(file_index-1, course)
#define BuSetStar(course, flag)     BuFileSetStar(file_index-1, course, flag)
#define BuGetCoin(course)           BuFileGetCoin(file_index-1, course)
"""

str_face = """
#ifndef __GNUC__
#define __attribute__(x)
#endif

#define DALIGN                  __attribute__((aligned(4)))
#define BALIGN                  __attribute__((aligned(8)))
#define UNUSED                  __attribute__((unused))
#define FALLTHROUGH             __attribute__((fallthrough))

typedef unsigned int size_t;

extern char __dummy0[];
extern char __dummy1[];
extern char __dummy2[];
extern char __dummy3[];
extern char __dummy4[];
extern char __dummy5[];
extern char __dummy6[];
extern char __dummy7[];
extern char __dummy8[];
extern char __dummy9[];
extern char __dummy10[];
extern char __dummy11[];
extern char __dummy12[];
extern char __dummy13[];
extern char __dummy14[];
extern char __dummy15[];
extern char __dummy16[];
extern char __dummy17[];
extern char __dummy18[];
extern char __dummy19[];
extern char __dummy20[];
extern char __dummy21[];
extern char __dummy22[];
extern char __dummy23[];
extern char __dummy24[];
extern char __dummy25[];
extern char __dummy26[];
extern char __dummy27[];
extern char __dummy28[];
extern char __dummy29[];
extern char __dummy30[];
extern char __dummy31[];
extern char __dummy32[];
extern char __dummy33[];
extern char __dummy34[];
extern char __dummy35[];
extern char __dummy36[];
extern char __dummy37[];
extern char __dummy38[];
extern char __dummy39[];
extern char __dummy40[];
extern char __dummy41[];
extern char __dummy42[];
extern char __dummy43[];
extern char __dummy44[];
extern char __dummy45[];
extern char __dummy46[];
extern char __dummy47[];
extern char __dummy48[];
extern char __dummy49[];
extern char __dummy50[];
extern char __dummy51[];
extern char __dummy52[];
extern char __dummy53[];
extern char __dummy54[];
extern char __dummy55[];
extern char __dummy56[];
extern char __dummy57[];
extern char __dummy58[];
extern char __dummy59[];
extern char __dummy60[];
extern char __dummy61[];
extern char __dummy62[];
extern char __dummy63[];
extern char __dummy64[];
extern char __dummy65[];
extern char __dummy66[];
extern char __dummy67[];
extern char __dummy68[];
extern char __dummy69[];
extern char __dummy70[];
extern char __dummy71[];
extern char __dummy72[];
extern char __dummy73[];
extern char __dummy74[];
extern char __dummy75[];
extern char __dummy76[];
extern char __dummy77[];
extern char __dummy78[];
extern char __dummy79[];
extern char __dummy80[];
extern char __dummy81[];
extern char __dummy82[];
extern char __dummy83[];
extern char __dummy84[];
extern char __dummy85[];
extern char __dummy86[];
extern char __dummy87[];
extern char __dummy88[];
extern char __dummy89[];
extern char __dummy90[];
extern char __dummy91[];
extern char __dummy92[];
extern char __dummy93[];
extern char __dummy94[];
extern char __dummy95[];
extern char __dummy96[];
extern char __dummy97[];
extern char __dummy98[];
extern char __dummy99[];
"""

struct_math = [
	[0x08, "struct", "bspline", "BSPLINE", [
		(0x00, main.sym_var("time", "short")),
		(0x02, main.sym_var("pos", "SVEC")),
	]],
]

struct_memory = [
	[0x10, "struct", "mem_block", "MEM_BLOCK", [
		(0x00, main.sym_var("prev", "struct mem_block *")),
		(0x04, main.sym_var("next", "struct mem_block *")),
		(0x08, main.sym_var("pad", "long long")),
	]],
	[0x10, "struct", "mem_frame", "MEM_FRAME", [
		(0x00, main.sym_var("size", "size_t")),
		(0x04, main.sym_var("blockl", "MEM_BLOCK *")),
		(0x08, main.sym_var("blockr", "MEM_BLOCK *")),
		(0x0C, main.sym_var("frame", "struct mem_frame *")),
	]],
	[0x10, "struct", "arena", "ARENA", [
		(0x00, main.sym_var("size", "long")),
		(0x04, main.sym_var("used", "long")),
		(0x08, main.sym_var("start", "char *")),
		(0x0C, main.sym_var("free", "char *")),
	]],
	[0x08, "struct", "heap_block", "HEAP_BLOCK", [
		(0x00, main.sym_var("next", "struct heap_block *")),
		(0x04, main.sym_var("size", "size_t")),
	]],
	[0x10, "struct", "heap", "HEAP", [
		(0x00, main.sym_var("size", "size_t")),
		(0x04, main.sym_var("block", "HEAP_BLOCK *")),
		(0x08, main.sym_var("free", "HEAP_BLOCK *")),
		(0x0C, main.sym_var("pad", "long")),
	]],
	[0x08, "struct", "bankinfo", "BANKINFO", [
		(0x00, main.sym_var("len", "unsigned int")),
		(0x04, main.sym_var("src", "const char *")),
		[0x08, "struct", "table", [
			(0x00, main.sym_var("start", "unsigned long")),
			(0x04, main.sym_var("size", "unsigned long")),
		], "[1]"],
	]],
	[0x0C, "struct", "bank", "BANK", [
		(0x00, main.sym_var("info", "BANKINFO *")),
		(0x04, main.sym_var("src", "const char *")),
		(0x08, main.sym_var("buf", "void *")),
	]],
]

struct_main = [
	[0x50, "struct", "sctask", "SCTASK", [
		(0x00, main.sym_var("task", "OSTask")),
		(0x40, main.sym_var("mq", "OSMesgQueue *")),
		(0x44, main.sym_var("msg", "OSMesg")),
		(0x48, main.sym_var("status", "int")),
	]],
	[0x08, "struct", "scclient", "SCCLIENT", [
		(0x00, main.sym_var("mq", "OSMesgQueue *")),
		(0x04, main.sym_var("msg", "OSMesg")),
	]],
]

struct_Na = [
	[0x0C, "struct", "Na_BgmCtl", "Na_BgmCtl", [
		(0x00, main.sym_var("a_voice", "s16")),
		(0x02, main.sym_var("a_vol", "s16")),
		(0x04, main.sym_var("a_time", "s16")),
		(0x06, main.sym_var("b_voice", "s16")),
		(0x08, main.sym_var("b_vol", "s16")),
		(0x0A, main.sym_var("b_time", "s16")),
	]],
	[0x1C, "struct", "Na_Cfg", "Na_Cfg", [
		(0x00, main.sym_var("freq", "u32")),
		(0x04, main.sym_var("voice", "u8")),
		(0x05, main.sym_var("e_filt", "u8")),
		(0x06, main.sym_var("e_size", "u16")),
		(0x08, main.sym_var("e_vol", "u16")),
		(0x0A, main.sym_var("vol", "u16")),
		(0x0C, main.sym_var("_0C", "size_t")),
		(0x10, main.sym_var("_10", "size_t")),
		(0x14, main.sym_var("_14", "size_t")),
		(0x18, main.sym_var("_18", "size_t")),
	]],
]

struct_graphics = [
	[0xC850, "struct", "frame", "FRAME", [
		(0x0000, main.sym_var("gfx", "Gfx", "[GFX_LEN]")),
		(0xC800, main.sym_var("task", "SCTASK")),
	]],
	[0x1C, "struct", "controller", "CONTROLLER", [
		(0x00, main.sym_var("stick_x", "short")),
		(0x02, main.sym_var("stick_y", "short")),
		(0x04, main.sym_var("x", "float")),
		(0x08, main.sym_var("y", "float")),
		(0x0C, main.sym_var("dist", "float")),
		(0x10, main.sym_var("held", "u16")),
		(0x12, main.sym_var("down", "u16")),
		(0x14, main.sym_var("status", "OSContStatus *")),
		(0x18, main.sym_var("pad", "OSContPad *")),
	]],
	[0x04, "struct", "demo", "DEMO", [
		(0x00, main.sym_var("count", "u8")),
		(0x01, main.sym_var("stick_x", "s8")),
		(0x02, main.sym_var("stick_y", "s8")),
		(0x03, main.sym_var("button", "u8")),
	]],
]

struct_time = [
	[0xC8, "struct", "time", "TIME", [
		(0x00, main.sym_var("audcpu_i", "s16")),
		(0x02, main.sym_var("audrcp_i", "s16")),
		(0x08, main.sym_var("gfxcpu", "OSTime", "[TIME_GFXCPU_MAX]")),
		(0x30, main.sym_var("gfxrcp", "OSTime", "[TIME_GFXRCP_MAX]")),
		(0x48, main.sym_var("audcpu", "OSTime", "[TIME_AUDCPU_MAX]")),
		(0x88, main.sym_var("audrcp", "OSTime", "[TIME_AUDRCP_MAX]")),
	]],
]

struct_shape = [
	[0x18, "struct", "anime", "ANIME", [
		(0x00, main.sym_var("flag", "s16")),
		(0x02, main.sym_var("waist", "short")),
		(0x04, main.sym_var("start", "s16")),
		(0x06, main.sym_var("loop", "s16")),
		(0x08, main.sym_var("frame", "s16")),
		(0x0A, main.sym_var("joint", "s16")),
		(0x0C, main.sym_var("val", "short *")),
		(0x10, main.sym_var("tbl", "u16 *")),
		(0x14, main.sym_var("size", "size_t")),
	]],
	[0x14, "struct", "skeleton", "SKELETON", [
		(0x00, main.sym_var("index", "s16")),
		(0x02, main.sym_var("waist", "short")),
		(0x04, main.sym_var("anime", "ANIME *")),
		(0x08, main.sym_var("frame", "s16")),
		(0x0A, main.sym_var("stamp", "u16")),
		(0x0C, main.sym_var("vframe", "s32")),
		(0x10, main.sym_var("vspeed", "s32")),
	]],
	[0x14, "struct", "shape", "SHAPE", [
		(0x00, main.sym_var("type", "s16")),
		(0x02, main.sym_var("flag", "s16")),
		(0x04, main.sym_var("prev", "struct shape *")),
		(0x08, main.sym_var("next", "struct shape *")),
		(0x0C, main.sym_var("parent", "struct shape *")),
		(0x10, main.sym_var("child", "struct shape *")),
	]],
]

struct_shp = [
	[0x1C, "struct", "scallback", "SCALLBACK", [
		(0x00, main.sym_var("s", "SHAPE")),
		(0x14, main.sym_var("callback", "SHPCALL *")),
		(0x18, main.sym_var("arg", "unsigned long")),
	]],
	[0x18, "struct", "sgfx", "SGFX", [
		(0x00, main.sym_var("s", "SHAPE")),
		(0x14, main.sym_var("gfx", "Gfx *")),
	]],
	[0x24, "struct", "sscene", "SSCENE", [
		(0x00, main.sym_var("s", "SHAPE")),
		(0x14, main.sym_var("index", "u8")),
		(0x15, main.sym_var("screen", "u8")),
		(0x16, main.sym_var("x", "short")),
		(0x18, main.sym_var("y", "short")),
		(0x1A, main.sym_var("w", "short")),
		(0x1C, main.sym_var("h", "short")),
		(0x1E, main.sym_var("reflen", "u16")),
		(0x20, main.sym_var("reftab", "SHAPE **")),
	]],
	[0x18, "struct", "sortho", "SORTHO", [
		(0x00, main.sym_var("s", "SHAPE")),
		(0x14, main.sym_var("scale", "float")),
	]],
	[0x24, "struct", "spersp", "SPERSP", [
		(0x00, main.sym_var("s", "SCALLBACK")),
		(0x1C, main.sym_var("fovy", "float")),
		(0x20, main.sym_var("near", "short")),
		(0x22, main.sym_var("far", "short")),
	]],
	[0x0C, "struct", "layerlist", "LAYERLIST", [
		(0x00, main.sym_var("mtx", "Mtx *")),
		(0x04, main.sym_var("gfx", "Gfx *")),
		(0x08, main.sym_var("next", "struct layerlist *")),
	]],
	[0x54, "struct", "slayer", "SLAYER", [
		(0x00, main.sym_var("s", "SHAPE")),
		(0x14, main.sym_var("list", "LAYERLIST *", "[LAYER_MAX]")),
		(0x34, main.sym_var("next", "LAYERLIST *", "[LAYER_MAX]")),
	]],
	[0x18, "struct", "slod", "SLOD", [
		(0x00, main.sym_var("s", "SHAPE")),
		(0x14, main.sym_var("min", "short")),
		(0x16, main.sym_var("max", "short")),
	]],
	[0x20, "struct", "sselect", "SSELECT", [
		(0x00, main.sym_var("s", "SCALLBACK")),
		(0x1C, main.sym_var("code", "s16")),
		(0x1E, main.sym_var("index", "s16")),
	]],
	[0x3C, "struct", "scamera", "SCAMERA", [
		(0x00, main.sym_var("s", "SCALLBACK")),
		(0x1C, main.sym_var("eye", "FVEC")),
		(0x28, main.sym_var("look", "FVEC")),
		(0x34, main.sym_var("m", "FMTX *")),
		(0x38, main.sym_var("angz_m", "short")),
		(0x3A, main.sym_var("angz_p", "short")),
	]],
	[0x24, "struct", "scoord", "SCOORD", [
		(0x00, main.sym_var("s", "SGFX")),
		(0x18, main.sym_var("pos", "SVEC")),
		(0x1E, main.sym_var("ang", "SVEC")),
	]],
	[0x1E, "struct", "spos", "SPOS", [
		(0x00, main.sym_var("s", "SGFX")),
		(0x18, main.sym_var("pos", "SVEC")),
	]],
	[0x1E, "struct", "sang", "SANG", [
		(0x00, main.sym_var("s", "SGFX")),
		(0x18, main.sym_var("ang", "SVEC")),
	]],
	[0x1C, "struct", "sscale", "SSCALE", [
		(0x00, main.sym_var("s", "SGFX")),
		(0x18, main.sym_var("scale", "float")),
	]],
	[0x20, "struct", "actor", "ACTOR", [
		(0x00, main.sym_var("pos", "SVEC")),
		(0x06, main.sym_var("ang", "SVEC")),
		(0x0C, main.sym_var("scene", "s8")),
		(0x0D, main.sym_var("group", "s8")),
		(0x10, main.sym_var("info", "u32")),
		(0x14, main.sym_var("script", "OBJLANG *")),
		(0x18, main.sym_var("shape", "SHAPE *")),
		(0x1C, main.sym_var("next", "struct actor *")),
	]],
	[0x60, "struct", "sobject", "SOBJECT", [
		(0x00, main.sym_var("s", "SHAPE")),
		(0x14, main.sym_var("shape", "SHAPE *")),
		(0x18, main.sym_var("scene", "s8")),
		(0x19, main.sym_var("group", "s8")),
		(0x1A, main.sym_var("ang", "SVEC")),
		(0x20, main.sym_var("pos", "FVEC")),
		(0x2C, main.sym_var("scale", "FVEC")),
		(0x38, main.sym_var("skel", "SKELETON")),
		(0x4C, main.sym_var("actor", "ACTOR *")),
		(0x50, main.sym_var("m", "FMTX *")),
		(0x54, main.sym_var("view", "FVEC")),
	]],
	[0x16, "struct", "scull", "SCULL", [
		(0x00, main.sym_var("s", "SHAPE")),
		(0x14, main.sym_var("dist", "short")),
	]],
	[0x1E, "struct", "sjoint", "SJOINT", [
		(0x00, main.sym_var("s", "SGFX")),
		(0x18, main.sym_var("pos", "SVEC")),
	]],
	[0x1E, "struct", "sbillboard", "SBILLBOARD", [
		(0x00, main.sym_var("s", "SGFX")),
		(0x18, main.sym_var("pos", "SVEC")),
	]],
	[0x18, "struct", "sshadow", "SSHADOW", [
		(0x00, main.sym_var("s", "SHAPE")),
		(0x14, main.sym_var("size", "short")),
		(0x16, main.sym_var("alpha", "u8")),
		(0x17, main.sym_var("type", "u8")),
	]],
	[0x18, "struct", "sbranch", "SBRANCH", [
		(0x00, main.sym_var("s", "SHAPE")),
		(0x14, main.sym_var("shape", "SHAPE *")),
	]],
	[0x20, "struct", "sback", "SBACK", [
		(0x00, main.sym_var("s", "SCALLBACK")),
		(0x1C, main.sym_var("code", "u32")),
	]],
	[0x26, "struct", "shand", "SHAND", [
		(0x00, main.sym_var("s", "SCALLBACK")),
		(0x1C, main.sym_var("obj", "SOBJECT *")),
		(0x20, main.sym_var("pos", "SVEC")),
	]],
]

struct_object = [
	[0x68, "struct", "list", "LIST", [
		(0x00, main.sym_var("next", "struct list *")),
		(0x04, main.sym_var("prev", "struct list *")),
	]],
	[0x68, "struct", "objlist", "OBJLIST", [
		(0x000, main.sym_var("s", "SOBJECT")),
		(0x060, main.sym_var("next", "struct object *")),
		(0x064, main.sym_var("prev", "struct object *")),
	]],
	[0x260, "struct", "object", "OBJECT", [
		(0x000, main.sym_var("s", "SOBJECT")),
		(0x060, main.sym_var("next", "struct object *")),
		(0x064, main.sym_var("prev", "struct object *")),
		(0x068, main.sym_var("parent", "struct object *")),
		(0x06C, main.sym_var("child", "struct object *")),
		(0x070, main.sym_var("hit_status", "u32")),
		(0x074, main.sym_var("flag", "s16")),
		(0x076, main.sym_var("hit_count", "s16")),
		(0x078, main.sym_var("hit", "struct object *", "[OBJ_HIT_MAX]")),
		[0x088, "union", "mem", [
			(None, main.sym_var("s", "short", "[2]")),
			(None, main.sym_var("i", "int")),
			(None, main.sym_var("f", "float")),
			(None, main.sym_var("p", "void *")),
		], "[OBJ_MEM_MAX]"],
		(0x1C8, main.sym_var("_1C8", "void *")),
		(0x1CC, main.sym_var("pc", "OBJLANG *")),
		(0x1D0, main.sym_var("sp", "unsigned int")),
		(0x1D4, main.sym_var("stack", "unsigned long", "[8]")),
		(0x1F4, main.sym_var("sleep", "s16")),
		(0x1F6, main.sym_var("actor_type", "s16")),
		(0x1F8, main.sym_var("hit_r", "float")),
		(0x1FC, main.sym_var("hit_h", "float")),
		(0x200, main.sym_var("dmg_r", "float")),
		(0x204, main.sym_var("dmg_h", "float")),
		(0x208, main.sym_var("hit_offset", "float")),
		(0x20C, main.sym_var("script", "OBJLANG *")),
		(0x210, main.sym_var("_210", "struct object *")),
		(0x214, main.sym_var("ride", "struct object *")),
		(0x218, main.sym_var("map", "MAP *")),
		(0x21C, main.sym_var("mtx", "FMTX")),
		(0x25C, main.sym_var("actor_flag", "void *")),
	]],
	# [0x10, "struct", "pl_effect", "PL_EFFECT", [
	# 	(0x00, main.sym_var("code", "u32")),
	# 	(0x04, main.sym_var("flag", "u32")),
	# 	(0x08, main.sym_var("shape", "u8")),
	# 	(0x0C, main.sym_var("script", "OBJLANG *")),
	# ]],
	[0x06, "struct", "bgdebug", "BGDEBUG", [
		(0x00, main.sym_var("ground", "s16")),
		(0x02, main.sym_var("roof", "s16")),
		(0x04, main.sym_var("wall", "s16")),
	]],
]

struct_objectlib = [
	[0x24, "struct", "splash", "SPLASH", [
		(0x00, main.sym_var("flag", "s16")),
		(0x02, main.sym_var("shape", "s16")),
		(0x04, main.sym_var("script", "OBJLANG *")),
		(0x08, main.sym_var("ang_range", "short")),
		(0x0A, main.sym_var("pos_range", "short")),
		(0x0C, main.sym_var("velf_start", "float")),
		(0x10, main.sym_var("velf_range", "float")),
		(0x14, main.sym_var("vely_start", "float")),
		(0x18, main.sym_var("vely_range", "float")),
		(0x1C, main.sym_var("scale_start", "float")),
		(0x20, main.sym_var("scale_range", "float")),
	]],
	[0x14, "struct", "chain", "CHAIN", [
		(0x00, main.sym_var("posx", "float")),
		(0x04, main.sym_var("posy", "float")),
		(0x08, main.sym_var("posz", "float")),
		(0x0C, main.sym_var("angx", "short")),
		(0x0E, main.sym_var("angy", "short")),
		(0x10, main.sym_var("angz", "short")),
	]],
	[0x14, "struct", "particle", "PARTICLE", [
		(0x00, main.sym_var("code", "s8")),
		(0x01, main.sym_var("count", "s8")),
		(0x02, main.sym_var("shape", "u8")),
		(0x03, main.sym_var("offset", "s8")),
		(0x04, main.sym_var("velf_start", "s8")),
		(0x05, main.sym_var("velf_range", "s8")),
		(0x06, main.sym_var("vely_start", "s8")),
		(0x07, main.sym_var("vely_range", "s8")),
		(0x08, main.sym_var("gravity", "s8")),
		(0x09, main.sym_var("drag", "s8")),
		(0x0C, main.sym_var("scale_start", "float")),
		(0x10, main.sym_var("scale_range", "float")),
	]],
	[0x10, "struct", "hitinfo", "HITINFO", [
		(0x00, main.sym_var("type", "u32")),
		(0x04, main.sym_var("offset", "u8")),
		(0x05, main.sym_var("ap", "s8")),
		(0x06, main.sym_var("hp", "s8")),
		(0x07, main.sym_var("ncoin", "s8")),
		(0x08, main.sym_var("hit_r", "short")),
		(0x0A, main.sym_var("hit_h", "short")),
		(0x0C, main.sym_var("dmg_r", "short")),
		(0x0E, main.sym_var("dmg_h", "short")),
	]],
	[0x08, "struct", "stepsound", "STEPSOUND", [
		(0x00, main.sym_var("flag", "s16")),
		(0x02, main.sym_var("l", "s8")),
		(0x03, main.sym_var("r", "s8")),
		(0x04, main.sym_var("se", "Na_Se")),
	]],
]

struct_map = [
	[0x28, "struct", "plane", "PLANE", [
		(0x00, main.sym_var("_00", "short")),
		(0x02, main.sym_var("_02", "short")),
		(0x04, main.sym_var("_04", "short")),
		(0x06, main.sym_var("_06", "short")),
		(0x08, main.sym_var("_08", "short")),
		(0x0A, main.sym_var("_0A", "short")),
		(0x0C, main.sym_var("_0C", "short")),
		(0x0E, main.sym_var("_0E", "short")),
		(0x10, main.sym_var("nx", "float")),
		(0x14, main.sym_var("ny", "float")),
		(0x18, main.sym_var("nz", "float")),
		(0x1C, main.sym_var("nw", "float")),
		(0x20, main.sym_var("_20", "short")),
		(0x22, main.sym_var("_22", "short")),
		(0x24, main.sym_var("_24", "short")),
		(0x26, main.sym_var("_26", "short")),
	]],
	[0x30, "struct", "bgface", "BGFACE", [
		(0x00, main.sym_var("code", "short")),
		(0x02, main.sym_var("attr", "short")),
		(0x04, main.sym_var("flag", "char")),
		(0x05, main.sym_var("area", "AREA")),
		(0x06, main.sym_var("yl", "short")),
		(0x08, main.sym_var("yh", "short")),
		(0x0A, main.sym_var("v0", "SVEC")),
		(0x10, main.sym_var("v1", "SVEC")),
		(0x16, main.sym_var("v2", "SVEC")),
		(0x1C, main.sym_var("nx", "float")),
		(0x20, main.sym_var("ny", "float")),
		(0x24, main.sym_var("nz", "float")),
		(0x28, main.sym_var("nw", "float")),
		(0x2C, main.sym_var("obj", "OBJECT *")),
	]],
	[0x08, "struct", "bglist", "BGLIST", [
		(0x00, main.sym_var("next", "struct bglist *")),
		(0x04, main.sym_var("face", "BGFACE *")),
	]],
	[0x18, "struct", "bgroot", "BGROOT", [
		(0x00, main.sym_var("list", "BGLIST", "[3]")),
	]],
	[0x28, "struct", "wallcheck", "WALLCHECK", [
		(0x00, main.sym_var("x", "float")),
		(0x04, main.sym_var("y", "float")),
		(0x08, main.sym_var("z", "float")),
		(0x0C, main.sym_var("offset", "float")),
		(0x10, main.sym_var("radius", "float")),
		(0x14, main.sym_var("flag", "s16")),
		(0x16, main.sym_var("count", "s16")),
		(0x18, main.sym_var("wall", "BGFACE *", "[4]")),
	]],
]

struct_camera = [
	[0x24, "struct", "pl_camera", "PL_CAMERA", [
		(0x00, main.sym_var("state", "u32")),
		(0x04, main.sym_var("pos", "FVEC")),
		(0x10, main.sym_var("ang", "SVEC")),
		(0x16, main.sym_var("neck_angx", "short")),
		(0x18, main.sym_var("neck_angy", "short")),
		(0x1A, main.sym_var("eyes", "s16")),
		(0x1C, main.sym_var("hand", "s16")),
		(0x1E, main.sym_var("demo", "s16")),
		(0x20, main.sym_var("obj", "OBJECT *")),
	]],
	[0xC0, "struct", "camdata", "CAMDATA", [
		(0x00, main.sym_var("_00", "FVEC")),
		(0x0C, main.sym_var("_0C", "FVEC")),
		(0x18, main.sym_var("_18", "FVEC")),
		(0x24, main.sym_var("_24", "FVEC")),
		(0x30, main.sym_var("_30", "FVEC")),
		(0x3C, main.sym_var("_3C", "u8")),
		(0x3D, main.sym_var("_3D", "u8")),
		(0x40, main.sym_var("_40", "f32")),
		(0x44, main.sym_var("_44", "f32")),
		(0x48, main.sym_var("_48", "f32")),
		(0x4C, main.sym_var("_4C", "SVEC")),
		(0x52, main.sym_var("_52", "SVEC")),
		(0x58, main.sym_var("_58", "s16")),
		(0x5A, main.sym_var("_5A", "s16")),
		(0x5C, main.sym_var("_5C", "s16")),
		(0x60, main.sym_var("_60", "FVEC")),
		(0x6C, main.sym_var("_6C", "SVEC")),
		(0x72, main.sym_var("_72", "s16")),
		(0x74, main.sym_var("_74", "s16")),
		(0x76, main.sym_var("_76", "s16")),
		(0x78, main.sym_var("_78", "s16")),
		(0x7A, main.sym_var("_7A", "s16")),
		(0x7C, main.sym_var("_7C", "s16")),
		(0x7E, main.sym_var("_7E", "s16")),
		(0x80, main.sym_var("look", "FVEC")),
		(0x8C, main.sym_var("eye", "FVEC")),
		(0x98, main.sym_var("_98", "s16")),
		(0x9A, main.sym_var("_9A", "s16")),
		(0x9C, main.sym_var("_9C", "s16")),
		(0x9E, main.sym_var("_9E", "s16")),
		(0xA0, main.sym_var("_A0", "s16")),
		(0xA2, main.sym_var("_A2", "s16")),
		(0xA4, main.sym_var("_A4", "f32")),
		(0xA8, main.sym_var("_A8", "f32")),
		(0xAC, main.sym_var("_AC", "f32")),
		(0xB0, main.sym_var("_B0", "f32")),
		(0xB4, main.sym_var("_B4", "s16")),
		(0xB8, main.sym_var("_B8", "u32")),
		(0xBC, main.sym_var("_BC", "s16")),
	]],
	[0x6C, "struct", "camera", "CAMERA", [
		(0x00, main.sym_var("mode", "u8")),
		(0x01, main.sym_var("_01", "u8")),
		(0x02, main.sym_var("_02", "short")),
		(0x04, main.sym_var("look", "FVEC")),
		(0x10, main.sym_var("pos", "FVEC")),
		(0x1C, main.sym_var("_1C", "char", "[12]")),
		(0x28, main.sym_var("center_x", "float")),
		(0x2C, main.sym_var("center_z", "float")),
		(0x30, main.sym_var("demo", "u8")),
		(0x31, main.sym_var("_31", "char", "[9]")),
		(0x3A, main.sym_var("_3A", "short")),
		(0x3C, main.sym_var("_3C", "char", "[40]")),
		(0x64, main.sym_var("_64", "u8")),
		(0x68, main.sym_var("center_y", "float")),
	]],
	[0x18, "struct", "campos", "CAMPOS", [
		(0x00, main.sym_var("code", "s16")),
		(0x04, main.sym_var("pos", "FVEC")),
		(0x10, main.sym_var("_10", "f32")),
		(0x14, main.sym_var("dist", "float")),
	]],
	[0x16, "struct", "camctl", "CAMCTL", [
		(0x00, main.sym_var("scene", "s8")),
		(0x04, main.sym_var_fnc("callback", arg=(
			"CAMERA *cam",
		))),
		(0x08, main.sym_var("pos", "SVEC")),
		(0x0E, main.sym_var("size", "SVEC")),
		(0x14, main.sym_var("ang", "short")),
	]],
	[0x08, "struct", "campath", "CAMPATH", [
		(0x00, main.sym_var("code", "s8")),
		(0x01, main.sym_var("time", "u8")),
		(0x02, main.sym_var("pos", "SVEC")),
	]],
	[0x06, "struct", "camdemo", "CAMDEMO", [
		(0x00, main.sym_var_fnc("callback", arg=(
			"CAMERA *cam",
		))),
		(0x04, main.sym_var("time", "s16")),
	]],
]

struct_debug = [
	# [0x0C, "struct", "dbprint", "DBPRINT", [
	# 	(0x00, main.sym_var("flag", "short")),
	# 	(0x02, main.sym_var("x", "short")),
	# 	(0x04, main.sym_var("y", "short")),
	# 	(0x06, main.sym_var("min_y", "short")),
	# 	(0x08, main.sym_var("max_y", "short")),
	# 	(0x0A, main.sym_var("height", "short")),
	# ]],
]

struct_wipe = [
	[0x03, "struct", "wipe_fade", "WIPE_FADE", [
		(0x00, main.sym_var("r", "u8")),
		(0x01, main.sym_var("g", "u8")),
		(0x02, main.sym_var("b", "u8")),
	]],
	[0x12, "struct", "wipe_window", "WIPE_WINDOW", [
		(0x00, main.sym_var("r", "u8")),
		(0x01, main.sym_var("g", "u8")),
		(0x02, main.sym_var("b", "u8")),
		(0x04, main.sym_var("ssize", "short")),
		(0x06, main.sym_var("esize", "short")),
		(0x08, main.sym_var("sx", "short")),
		(0x0A, main.sym_var("sy", "short")),
		(0x0C, main.sym_var("ex", "short")),
		(0x0E, main.sym_var("ey", "short")),
		(0x10, main.sym_var("rot", "short")),
	]],
	[0x12, "union", "wipe_data", "WIPE_DATA", [
		(None, main.sym_var("fade", "WIPE_FADE")),
		(None, main.sym_var("window", "WIPE_WINDOW")),
	]],
	[0x16, "struct", "wipe", "WIPE", [
		(0x00, main.sym_var("active", "u8")),
		(0x01, main.sym_var("type", "u8")),
		(0x02, main.sym_var("frame", "u8")),
		(0x03, main.sym_var("blank", "u8")),
		(0x04, main.sym_var("data", "WIPE_DATA")),
	]],
]

struct_shadow = [
	# [0x2D, "struct", "shadow", "SHADOW", [
	# 	(0x00, main.sym_var("x", "float")),
	# 	(0x04, main.sym_var("y", "float")),
	# 	(0x08, main.sym_var("z", "float")),
	# 	(0x0C, main.sym_var("level", "float")),
	# 	(0x10, main.sym_var("scale", "float")),
	# 	(0x14, main.sym_var("nx", "float")),
	# 	(0x18, main.sym_var("ny", "float")),
	# 	(0x1C, main.sym_var("nz", "float")),
	# 	(0x20, main.sym_var("nw", "float")),
	# 	(0x24, main.sym_var("angy", "float")),
	# 	(0x28, main.sym_var("angx", "float")),
	# 	(0x2C, main.sym_var("alpha", "u8")),
	# ]],
	# [0x09, "struct", "shadow_rect", "SHADOW_RECT", [
	# 	(0x00, main.sym_var("sizex", "float")),
	# 	(0x04, main.sym_var("sizez", "float")),
	# 	(0x08, main.sym_var("flag", "char")),
	# ]],
]

struct_background = [
	[0x00, "struct", "background", "BACKGROUND", [
		(0x00, main.sym_var("txt", "u16 *", "[BACK_TW*BACK_TH]")),
	]],
	# [0x10, "struct", "backdata", "BACKDATA", [
	# 	(0x00, main.sym_var("angy", "unsigned short")),
	# 	(0x02, main.sym_var("angx", "short")),
	# 	(0x04, main.sym_var("posx", "int")),
	# 	(0x08, main.sym_var("posy", "int")),
	# 	(0x0C, main.sym_var("index", "int")),
	# ]],
]

struct_water = [
	[0x08, "struct", "waterinfo", "WATERINFO", [
		(0x00, main.sym_var("code", "short")),
		(0x04, main.sym_var("data", "short *")),
	]],
	# [0x24, "struct", "fluidinfo", "FLUIDINFO", [
	# 	(0x00, main.sym_var("code", "unsigned long")),
	# 	(0x04, main.sym_var("txt", "int")),
	# 	(0x08, main.sym_var("n", "int")),
	# 	(0x0C, main.sym_var("data", "short *")),
	# 	(0x10, main.sym_var("start", "Gfx *")),
	# 	(0x14, main.sym_var("end", "Gfx *")),
	# 	(0x18, main.sym_var("draw", "Gfx *")),
	# 	(0x1C, main.sym_var("r", "u8")),
	# 	(0x1D, main.sym_var("g", "u8")),
	# 	(0x1E, main.sym_var("b", "u8")),
	# 	(0x1F, main.sym_var("alpha", "u8")),
	# 	(0x20, main.sym_var("layer", "int")),
	# ]],
]

struct_wave = [
	[0x78, "struct", "wave", "WAVE", [
		(0x00, main.sym_var("code", "s16")),
		(0x02, main.sym_var("nmesh", "s8")),
		(0x03, main.sym_var("type", "s8")),
		(0x04, main.sym_var("stepprev", "s8")),
		(0x05, main.sym_var("stepstat", "s8")),
		(0x06, main.sym_var("steptrig", "s8")),
		(0x07, main.sym_var("state", "s8")),
		(0x08, main.sym_var("angx", "float")),
		(0x0C, main.sym_var("angy", "float")),
		(0x10, main.sym_var("posx", "float")),
		(0x14, main.sym_var("posy", "float")),
		(0x18, main.sym_var("posz", "float")),
		(0x1C, main.sym_var("depth", "float")),
		(0x20, main.sym_var("touchdepth", "float")),
		(0x24, main.sym_var("enterdepth", "float")),
		(0x28, main.sym_var("decay", "float")),
		(0x2C, main.sym_var("touchdecay", "float")),
		(0x30, main.sym_var("enterdecay", "float")),
		(0x34, main.sym_var("speed", "float")),
		(0x38, main.sym_var("touchspeed", "float")),
		(0x3C, main.sym_var("enterspeed", "float")),
		(0x40, main.sym_var("scale", "float")),
		(0x44, main.sym_var("touchscale", "float")),
		(0x48, main.sym_var("enterscale", "float")),
		(0x4C, main.sym_var("timer", "float")),
		(0x50, main.sym_var("centerx", "float")),
		(0x54, main.sym_var("centery", "float")),
		(0x58, main.sym_var("statgfx", "Gfx *")),
		(0x5C, main.sym_var("meshlist", "short **")),
		(0x60, main.sym_var("txtlist", "u16 **")),
		(0x64, main.sym_var("wd", "short")),
		(0x66, main.sym_var("ht", "short")),
		(0x68, main.sym_var("movegfx", "Gfx *")),
		(0x6C, main.sym_var("mode", "s8")),
		(0x6D, main.sym_var("alpha", "u8")),
		(0x6E, main.sym_var("diveprev", "char")),
		(0x6F, main.sym_var("divestat", "char")),
		(0x70, main.sym_var("divetrig", "char")),
		(0x74, main.sym_var("size", "float")),
	]],
]

struct_dprint = [
	# [0x3C, "struct", "dprint", "DPRINT", [
	# 	(0x00, main.sym_var("x", "int")),
	# 	(0x04, main.sym_var("y", "int")),
	# 	(0x08, main.sym_var("len", "s16")),
	# 	(0x0A, main.sym_var("str", "char", "[50]")),
	# ]],
]

struct_message = [
	[0x10, "struct", "message", "MESSAGE", [
		(0x00, main.sym_var("code", "int")),
		(0x04, main.sym_var("line", "char")),
		(0x06, main.sym_var("x", "short")),
		(0x08, main.sym_var("y", "short")),
		(0x0C, main.sym_var("str", "unsigned char *")),
	]],
]

struct_weather = [
	[0x38, "struct", "weather", "WEATHER", [
		(0x00, main.sym_var("flag", "char")),
		(0x02, main.sym_var("frame", "s16")),
		(0x04, main.sym_var("x", "int")),
		(0x08, main.sym_var("y", "int")),
		(0x0C, main.sym_var("z", "int")),
		(0x10, main.sym_var("work", "int", "[10]")),
	]],
]

struct_tag = [
	[0x08, "struct", "tagobj", "TAGOBJ", [
		(0x00, main.sym_var("script", "OBJLANG *")),
		(0x04, main.sym_var("shape", "s16")),
		(0x06, main.sym_var("code", "s16")),
	]],
	[0x08, "struct", "mapobj", "MAPOBJ", [
		(0x00, main.sym_var("index", "u8")),
		(0x01, main.sym_var("ext", "u8")),
		(0x02, main.sym_var("arg", "u8")),
		(0x03, main.sym_var("shape", "u8")),
		(0x04, main.sym_var("script", "OBJLANG *")),
	]],
]

struct_hud = [
	[0x0E, "struct", "hud", "HUD", [
		(0x00, main.sym_var("life", "s16")),
		(0x02, main.sym_var("coin", "s16")),
		(0x04, main.sym_var("star", "s16")),
		(0x06, main.sym_var("power", "s16")),
		(0x08, main.sym_var("key", "s16")),
		(0x0A, main.sym_var("flag", "s16")),
		(0x0C, main.sym_var("time", "u16")),
	]],
	# [0x0C, "struct", "meter", "METER", [
	# 	(0x00, main.sym_var("state", "s8")),
	# 	(0x02, main.sym_var("x", "short")),
	# 	(0x04, main.sym_var("y", "short")),
	# 	(0x08, main.sym_var("scale", "float")),
	# ]],
]

struct_scene = [
	[0x10, "struct", "staff", "STAFF", [
		(0x00, main.sym_var("stage", "u8")),
		(0x01, main.sym_var("scene", "u8")),
		(0x02, main.sym_var("flag", "u8")),
		(0x03, main.sym_var("angy", "s8")),
		(0x04, main.sym_var("posx", "short")),
		(0x06, main.sym_var("posy", "short")),
		(0x08, main.sym_var("posz", "short")),
		(0x0C, main.sym_var("str", "const char **")),
	]],
	[0x04, "struct", "portinfo", "PORTINFO", [
		(0x00, main.sym_var("attr", "u8")),
		(0x01, main.sym_var("stage", "u8")),
		(0x02, main.sym_var("scene", "u8")),
		(0x03, main.sym_var("port", "u8")),
	]],
	[0x0C, "struct", "port", "PORT", [
		(0x00, main.sym_var("p", "PORTINFO")),
		(0x04, main.sym_var("obj", "OBJECT *")),
		(0x08, main.sym_var("next", "struct port *")),
	]],
	[0x04, "struct", "bgport", "BGPORT", [
		(0x00, main.sym_var("p", "PORTINFO")),
	]],
	[0x08, "struct", "connect", "CONNECT", [
		(0x00, main.sym_var("flag", "u8")),
		(0x01, main.sym_var("scene", "u8")),
		(0x02, main.sym_var("offset", "SVEC")),
	]],
	[0x0A, "struct", "scene28", "SCENE28", [
		(0x00, main.sym_var("_00", "short")),
		(0x02, main.sym_var("_02", "short")),
		(0x04, main.sym_var("_04", "short")),
		(0x06, main.sym_var("_06", "short")),
		(0x08, main.sym_var("_08", "short")),
	]],
	[0x08, "struct", "jet", "JET", [
		(0x00, main.sym_var("pos", "SVEC")),
		(0x06, main.sym_var("attr", "short")),
	]],
	[0x3A, "struct", "scene", "SCENE", [
		(0x00, main.sym_var("index", "s8")),
		(0x01, main.sym_var("flag", "s8")),
		(0x02, main.sym_var("env", "u16")),
		(0x04, main.sym_var("shp", "SSCENE *")),
		(0x08, main.sym_var("map", "MAP *")),
		(0x0C, main.sym_var("area", "AREA *")),
		(0x10, main.sym_var("tag", "TAG *")),
		(0x14, main.sym_var("port", "PORT *")),
		(0x18, main.sym_var("bgport", "BGPORT *")),
		(0x1C, main.sym_var("connect", "CONNECT *")),
		(0x20, main.sym_var("actor", "ACTOR *")),
		(0x24, main.sym_var("cam", "CAMERA *")),
		(0x28, main.sym_var("_28", "SCENE28 *")),
		(0x2C, main.sym_var("jet", "JET *", "[2]")),
		(0x34, main.sym_var("msg", "u8", "[2]")),
		(0x36, main.sym_var("bgm_mode", "u16")),
		(0x38, main.sym_var("bgm", "u16")),
	]],
]

struct_player = [
	[0x18, "struct", "bump", "BUMP", [
		(0x00, main.sym_var("power", "float")),
		(0x04, main.sym_var("radius", "float")),
		(0x08, main.sym_var("posx", "float")),
		(0x0C, main.sym_var("posz", "float")),
		(0x10, main.sym_var("velx", "float")),
		(0x14, main.sym_var("velz", "float")),
	]],
	[0x28, "struct", "pl_shape", "PL_SHAPE", [
		(0x00, main.sym_var("state", "u32")),
		(0x04, main.sym_var("head", "s8")),
		(0x05, main.sym_var("eyes", "s8")),
		(0x06, main.sym_var("hand", "s8")),
		(0x07, main.sym_var("wing", "s8")),
		(0x08, main.sym_var("cap", "s16")),
		(0x0A, main.sym_var("take", "s8")),
		(0x0B, main.sym_var("punch", "u8")),
		(0x0C, main.sym_var("torso_ang", "SVEC")),
		(0x12, main.sym_var("neck_ang", "SVEC")),
		(0x18, main.sym_var("hand_pos", "FVEC")),
		(0x24, main.sym_var("obj", "OBJECT *")),
	]],
	[0xC8, "struct", "player", "PLAYER", [
		(0x00, main.sym_var("index", "u16")),
		(0x02, main.sym_var("status", "u16")),
		(0x04, main.sym_var("flag", "u32")),
		(0x08, main.sym_var("effect", "u32")),
		(0x0C, main.sym_var("state", "u32")),
		(0x10, main.sym_var("prevstate", "u32")),
		(0x14, main.sym_var("surface", "u32")),
		(0x18, main.sym_var("phase", "u16")),
		(0x1A, main.sym_var("timer", "u16")),
		(0x1C, main.sym_var("code", "u32")),
		(0x20, main.sym_var("stick_dist", "float")),
		(0x24, main.sym_var("stick_ang", "short")),
		(0x26, main.sym_var("invincible", "s16")),
		(0x28, main.sym_var("a_timer", "u8")),
		(0x29, main.sym_var("b_timer", "u8")),
		(0x2A, main.sym_var("wall_timer", "u8")),
		(0x2B, main.sym_var("jump_timer", "u8")),
		(0x2C, main.sym_var("ang", "SVEC")),
		(0x32, main.sym_var("rot", "SVEC")),
		(0x38, main.sym_var("slide_ang", "short")),
		(0x3A, main.sym_var("spin_ang", "short")),
		(0x3C, main.sym_var("pos", "FVEC")),
		(0x48, main.sym_var("vel", "FVEC")),
		(0x54, main.sym_var("speed", "float")),
		(0x58, main.sym_var("slide_x", "float")),
		(0x5C, main.sym_var("slide_z", "float")),
		(0x60, main.sym_var("wall", "BGFACE *")),
		(0x64, main.sym_var("roof", "BGFACE *")),
		(0x68, main.sym_var("ground", "BGFACE *")),
		(0x6C, main.sym_var("roof_y", "float")),
		(0x70, main.sym_var("ground_y", "float")),
		(0x74, main.sym_var("ground_ang", "short")),
		(0x76, main.sym_var("water", "short")),
		(0x78, main.sym_var("collide", "OBJECT *")),
		(0x7C, main.sym_var("take", "OBJECT *")),
		(0x80, main.sym_var("attach", "OBJECT *")),
		(0x84, main.sym_var("ride", "OBJECT *")),
		(0x88, main.sym_var("obj", "OBJECT *")),
		(0x8C, main.sym_var("actor", "ACTOR *")),
		(0x90, main.sym_var("scene", "SCENE *")),
		(0x94, main.sym_var("camera", "PL_CAMERA *")),
		(0x98, main.sym_var("shape", "PL_SHAPE *")),
		(0x9C, main.sym_var("cont", "CONTROLLER *")),
		(0xA0, main.sym_var("anime", "BANK *")),
		(0xA4, main.sym_var("hit_status", "u32")),
		(0xA8, main.sym_var("coin", "s16")),
		(0xAA, main.sym_var("star", "s16")),
		(0xAC, main.sym_var("key", "s8")),
		(0xAD, main.sym_var("life", "s8")),
		(0xAE, main.sym_var("power", "s16")),
		(0xB0, main.sym_var("waist", "short")),
		(0xB2, main.sym_var("damage", "u8")),
		(0xB3, main.sym_var("recover", "u8")),
		(0xB4, main.sym_var("press", "u8")),
		(0xB5, main.sym_var("alpha", "u8")),
		(0xB6, main.sym_var("cap_timer", "u16")),
		(0xB8, main.sym_var("prevstar", "s16")),
		(0xBC, main.sym_var("peak", "float")),
		(0xC0, main.sym_var("sink", "float")),
		(0xC4, main.sym_var("gravity", "float")),
	]],
	[0x18, "struct", "pl_move", "PL_MOVE", [
		(0x00, main.sym_var("time", "s16")),
		(0x02, main.sym_var("timer_ground", "s16")),
		(0x04, main.sym_var("state_slip", "u32")),
		(0x08, main.sym_var("state_next", "u32")),
		(0x0C, main.sym_var("state_jump", "u32")),
		(0x10, main.sym_var("state_fall", "u32")),
		(0x14, main.sym_var("state_slide", "u32")),
	]],
	# [0x08, "struct", "collision", "COLLISION", [
	# 	(0x00, main.sym_var("type", "u32")),
	# 	(0x04, main.sym_var_fnc("callback", val="int", arg=(
	# 		"PLAYER *pl",
	# 		"u32 flag",
	# 		"OBJECT *obj",
	# 	))),
	# ]],
]

struct_game = [
	[0x08, "struct", "pl_entry", "PL_ENTRY", [
		(0x00, main.sym_var("type", "u8")),
		(0x01, main.sym_var("stage", "u8")),
		(0x02, main.sym_var("scene", "u8")),
		(0x03, main.sym_var("port", "u8")),
		(0x04, main.sym_var("code", "u32")),
	]],
]

struct_backup = [
	[0x04, "struct", "bucheck", "BUCHECK", [
		(0x00, main.sym_var("key", "u16")),
		(0x02, main.sym_var("sum", "u16")),
	]],
	[0x20, "struct", "backupinfo", "BACKUPINFO", [
		(0x00, main.sym_var("time", "u32", "[4]")),
		(0x10, main.sym_var("sound", "u16")),
		(0x12, main.sym_var("pad", "char", "[10]")),
		(0x1C, main.sym_var("check", "BUCHECK")),
	]],
	[0x38, "struct", "backupfile", "BACKUPFILE", [
		(0x00, main.sym_var("stage", "u8")),
		(0x01, main.sym_var("scene", "u8")),
		(0x02, main.sym_var("pos", "SVEC")),
		(0x08, main.sym_var("flag", "u32")),
		(0x0C, main.sym_var("star", "u8", "[25]")),
		(0x25, main.sym_var("coin", "u8", "[15]")),
		(0x34, main.sym_var("check", "BUCHECK")),
	]],
	[0x200, "struct", "backup", "BACKUP", [
		(0x000, main.sym_var("file", "BACKUPFILE", "[4][2]")),
		(0x1C0, main.sym_var("info", "BACKUPINFO", "[2]")),
	]],
]

struct_object_a = [
	[0x0C, "struct", "object_a_0", None, [
		(0x00, main.sym_var("_00", "s16")),
		(0x04, main.sym_var("_04", "f32")),
		(0x08, main.sym_var("_08", "f32")),
	]],
	[0x0A, "struct", "object_a_1", None, [
		(0x00, main.sym_var("flag", "s16")),
		(0x02, main.sym_var("scale", "short")),
		(0x04, main.sym_var("map", "MAP *")),
		(0x08, main.sym_var("dist", "short")),
	]],
	[0x0C, "struct", "object_a_2", None, [
		(0x00, main.sym_var("count", "s16")),
		(0x02, main.sym_var("add", "short")),
		(0x04, main.sym_var("mul", "short")),
		(0x06, main.sym_var("shape", "s16")),
		(0x08, main.sym_var("map", "MAP *")),
	]],
	[0x0A, "struct", "object_a_3", None, [
		(0x00, main.sym_var("map", "MAP *")),
		(0x04, main.sym_var("posx", "short")),
		(0x06, main.sym_var("posz", "short")),
		(0x08, main.sym_var("angy", "short")),
	]],
	[0x14, "struct", "object_a_4", None, [
		(0x00, main.sym_var("offset", "s32")),
		(0x04, main.sym_var("scale", "FVEC")),
		(0x10, main.sym_var("vel", "float")),
	]],
	[0x08, "struct", "object_a_5", None, [
		(0x00, main.sym_var("shape", "u8")),
		(0x01, main.sym_var("posx", "s8")),
		(0x02, main.sym_var("posz", "s8")),
		(0x03, main.sym_var("state", "s8")),
		(0x04, main.sym_var("data", "s8 *")),
	]],
	[0x08, "struct", "object_a_6", None, [
		(0x00, main.sym_var("index", "u8")),
		(0x01, main.sym_var("flag", "u8")),
		(0x02, main.sym_var("code", "u8")),
		(0x03, main.sym_var("shape", "u8")),
		(0x04, main.sym_var("script", "OBJLANG *")),
	]],
	[0x08, "struct", "object_a_7", None, [
		(0x00, main.sym_var("offset", "short")),
		(0x02, main.sym_var("shape", "s16")),
		(0x04, main.sym_var("map", "MAP *")),
	]],
	[0x10, "struct", "object_a_8", None, [
		(0x00, main.sym_var("time", "s32")),
		(0x04, main.sym_var("anime", "s32")),
		(0x08, main.sym_var("vel", "float")),
		(0x0C, main.sym_var("anime_vel", "float")),
	]],
]

struct_object_b = [
]

struct_object_c = [
	[0x0E, "struct", "object_c_0", None, [
		(0x00, main.sym_var("msg_start", "s16")),
		(0x02, main.sym_var("msg_win", "s16")),
		(0x04, main.sym_var("path", "PATH *")),
		(0x08, main.sym_var("star", "SVEC")),
	]],
	[0x0B, "struct", "object_c_1", None, [
		(0x00, main.sym_var("scale", "float")),
		(0x04, main.sym_var("se", "Na_Se")),
		(0x08, main.sym_var("dist", "short")),
		(0x0A, main.sym_var("damage", "s8")),
	]],
	[0x0A, "struct", "object_c_2", None, [
		(0x00, main.sym_var("map", "MAP *")),
		(0x04, main.sym_var("p_map", "MAP *")),
		(0x08, main.sym_var("p_shape", "s16")),
	]],
	[0x06, "struct", "object_c_3", None, [
		(0x00, main.sym_var("map", "MAP *")),
		(0x04, main.sym_var("shape", "s16")),
	]],
	[0x0C, "struct", "object_c_4", None, [
		(0x00, main.sym_var("msg", "s16")),
		(0x04, main.sym_var("radius", "float")),
		(0x08, main.sym_var("height", "float")),
	]],
	[0x0C, "struct", "object_c_5", None, [
		(0x00, main.sym_var("shape", "int")),
		(0x04, main.sym_var("script", "OBJLANG *")),
		(0x08, main.sym_var("scale", "float")),
	]],
]

struct_face = [
	[0xF4, "struct", "control", "CONTROL", [
		(0x00, main.sym_var("_00", "int")),
		(0x04, main.sym_var("_04", "char", "[80]")),
		(0x54, main.sym_var("_54", "int")),
		(0x58, main.sym_var("_58", "char", "[48]")),
		(0x88, main.sym_var("_88", "float")),
		(0x8C, main.sym_var("_8C", "char", "[20]")),
		(0xA0, main.sym_var("_A0", "float")),
		(0xA4, main.sym_var("_A4", "char", "[8]")),
		(0xAC, main.sym_var("_AC", "float")),
		(0xB0, main.sym_var("_B0", "char", "[64]")),
		(0xF0, main.sym_var("prev", "struct control *")),
	]],
	[0x0C, "struct", "vector", "VECTOR", [
		(0x00, main.sym_var("x", "float")),
		(0x04, main.sym_var("y", "float")),
		(0x08, main.sym_var("z", "float")),
	]],
	[0x0C, "struct", "colour", "COLOUR", [
		(0x00, main.sym_var("r", "float")),
		(0x04, main.sym_var("g", "float")),
		(0x08, main.sym_var("b", "float")),
	]],
	[0x18, "struct", "box", "BOX", [
		(0x00, main.sym_var("min_x", "float")),
		(0x04, main.sym_var("min_y", "float")),
		(0x08, main.sym_var("min_z", "float")),
		(0x0C, main.sym_var("max_x", "float")),
		(0x10, main.sym_var("max_y", "float")),
		(0x14, main.sym_var("max_z", "float")),
	]],
	[0x24, "struct", "srt", "SRT", [
		(0x00, main.sym_var("s", "VECTOR")),
		(0x0C, main.sym_var("r", "VECTOR")),
		(0x18, main.sym_var("t", "VECTOR")),
	]],
	[0x0C, "struct", "dyndata", "DYNDATA", [
		(0x00, main.sym_var("count", "int")),
		(0x04, main.sym_var("type", "int")),
		(0x08, main.sym_var("data", "void *")),
	]],
	[0x18, "struct", "dynlist", "DYNLIST", [
		(0x00, main.sym_var("c", "int")),
		(0x04, main.sym_var("p", "const void *")),
		(0x08, main.sym_var("i", "int")),
		(0x0C, main.sym_var("v", "VECTOR")),
	]],
	[0x08, "struct", "bank", "BANK", [
		(0x00, main.sym_var("index", "int")),
		(0x04, main.sym_var("dynlist", "DYNLIST *")),
	]],
]
