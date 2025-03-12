import main
import ultra

str_math = """
#ifdef __GNUC__
#define sqrtf(x) __builtin_sqrtf(x)
#endif

#define SIN(x)                  sintable[(u16)(x) >> 4]
#define COS(x)                  costable[(u16)(x) >> 4]

#define DIST2(x, y)     sqrtf((x)*(x) + (y)*(y))
#define DIST3(x, y, z)  sqrtf((x)*(x) + (y)*(y) + (z)*(z))

#define MDOT3(m, i, x, y, z) ((m)[0][i]*(x) + (m)[1][i]*(y) + (m)[2][i]*(z))
#define IDOT3(m, i, x, y, z) ((m)[i][0]*(x) + (m)[i][1]*(y) + (m)[i][2]*(z))
#define MDOT4(m, i, x, y, z) (MDOT3(m, i, x, y, z) + (m)[3][i])

#define TURN(x, target, speed) \\
	((target)-ConvergeI((short)((target)-(x)), 0, speed, speed))
"""

struct_math = [
	[0x08, "struct", "bspline", "BSPLINE", [
		(0x00, main.sym_var("time", "short")),
		(0x02, main.sym_var("pos", "SVEC")),
	]],
]

include_math = [
	[main.f_str, str_math],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_math],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.data", 0x80386000, 0x8038B802], # mathtbl
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.data", 0x8038BC90, 0x8038BC9C], # math
	[ultra.c.f_extern, "E0.ulib.data", 0x80385F90, 0x80385FF8], # math
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.text", 0x80378800, 0x8037B21C], # math
]

str_memory = """
#define MEM_ALLOC_L 0
#define MEM_ALLOC_R 1

#define ArenaCreateFull() ArenaCreate(MemGetFree()-sizeof(ARENA), MEM_ALLOC_L)
#define ArenaShrink(arena) ArenaResize(arena, (arena)->used);

#define malloc(size)            HeapAlloc(mem_heap, size)
#define free(ptr)               HeapFree(mem_heap, ptr)
"""

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

include_memory = [
	[main.f_str, str_memory],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_memory],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x801C1000, 0x801CE000], # timg
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x8033B400, 0x8033B498], # memory
	[ultra.c.f_extern, "E0.code.data", 0x8032DD70, 0x8032DD74], # memory
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x80277EE0, 0x80279158], # memory
	[main.f_str, "#ifdef DISK\n"],
	[ultra.c.f_extern, "DD.code.text", [0x80406BAC, 0x80406BF0]],
	[main.f_str, "#endif\n"],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x8027F4E0, 0x8027F584], # slidec
]

include_disk = [
	[main.f_str, "#ifdef DISK\n"],
	[ultra.c.f_extern, "DD.code.text", 0x8040B980, 0x8040BAEC], # disk
	[main.f_str, "#endif\n"],
]

str_main = """
#define SCREEN_WD               320
#define SCREEN_HT               240
#ifdef NTSC
#define BORDER_HT               8
#define FPS                     30
#define NTSCPAL(ntsc, pal)      ntsc
#endif
#ifdef PAL
#define BORDER_HT               1
#define FPS                     25
#define NTSCPAL(ntsc, pal)      pal
#endif

#define SC_AUDCLIENT            1
#define SC_GFXCLIENT            2
"""

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

include_main = [
	[main.f_str, str_main],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_main],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x8033A580, 0x8033AF90], # main
	[ultra.c.f_extern, "E0.code.data", 0x8032D560, 0x8032D58C], # main
	[main.f_str, "#ifdef GATEWAY\n"],
	[ultra.c.f_extern, "G0.code.data", [0x8030186C]], # main
	[main.f_str, "#endif\n"],
	[ultra.c.f_extern, "E0.code.data", 0x8032D58C, 0x8032D5C4], # main
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x80246050, 0x80246DF8], # main
]

str_graphics = """
#define GFX_LEN                 6400
#define FIFO_SIZE               0x1F000
#define FIFO_LEN                (FIFO_SIZE/8)

#define CONTROLLER_MAX          2

#define CONT_EXIT               0x0080
"""

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
		"#ifdef MOTOR",
		(0x1C, main.sym_var("port", "int")),
		"#endif",
	]],
	[0x04, "struct", "demo", "DEMO", [
		(0x00, main.sym_var("count", "u8")),
		(0x01, main.sym_var("stick_x", "s8")),
		(0x02, main.sym_var("stick_y", "s8")),
		(0x03, main.sym_var("button", "u8")),
	]],
]

include_graphics = [
	[main.f_str, str_graphics],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_graphics],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", [
		0x8038F800, # cimg
		0x803B5000,
		0x803DA800,
		0x80000400, # zimg
		0x80227000, # fifo
	]],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x8033AF90, 0x8033B09C], # graphics
	[ultra.c.f_extern, "E0.code.data", 0x8032D5D0, 0x8032D5FC], # graphics
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x80246E70, 0x80248C3C], # graphics
]

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

#define Na_Se2_00()             (NA_SE2_00 + (Na_Random % 3 << 16))
#define Na_Se2_18()             (NA_SE2_18 + (Na_Random % 3 << 16))
#define Na_Se2_2B()             (NA_SE2_2B + (Na_Random % 5 << 16))

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

include_Na = [
	[main.f_str, str_Na],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", [
		0x80226CB8,
		0x803331F0,
		0x803331FC,
	]],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", [
		0x8031950C,
		0x8031E7B8,
		0x8031EB00,
		0x8031FD84,
		0x80320678,
		0x803206BC,
		0x80320E3C,
		0x80320EC4,
		0x803210D4,
		0x8032112C,
		0x80321474,
		0x80321584,
		0x8032171C,
		0x8032174C,
		0x8032180C,
		0x803218D8,
		0x803218F4,
		0x803219AC,
		0x80321BAC,
		0x80321CE4,
		0x80321D38,
		0x80321D5C,
		0x80321E48,
		0x80321F48,
		0x80321F9C,
		0x80322078,
		0x803220B4,
		0x803220F0,
		0x8032212C,
		0x80322168,
		0x803221B8,
		0x803221F4,
		0x80322230,
		0x8032231C,
	]],
]

str_audio = """
#define AUD_PAUSE               1
#define AUD_QUIET               2
"""

include_audio = [
	[main.f_str, str_audio],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x8033B0A0, 0x8033B170], # audio
	[ultra.c.f_extern, "E0.code.data", 0x8032D600, 0x8032D6C1], # audio
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x80248C40, 0x802495DC], # audio
]

include_motor = [
	[main.f_str, "#ifdef MOTOR\n"],
	[ultra.c.f_extern, "J3.code.data", 0x8030CE00, 0x8030CE10], # motor
	[main.f_str, "\n"],
	[ultra.c.f_extern, "J3.code.text", 0x8024C4A0, 0x8024CCB8], # motor
	[main.f_str, "#endif\n"],
]

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

struct_time = [
	# [0xC8, "struct", "time", "TIME", [
	# 	(0x00, main.sym_var("audcpu_i", "short")),
	# 	(0x02, main.sym_var("audrcp_i", "short")),
	# 	(0x08, main.sym_var("gfxcpu", "OSTime", "[TIME_GFXCPU_MAX]")),
	# 	(0x30, main.sym_var("gfxrcp", "OSTime", "[TIME_GFXRCP_MAX]")),
	# 	(0x48, main.sym_var("audcpu", "OSTime", "[TIME_AUDCPU_MAX]")),
	# 	(0x88, main.sym_var("audrcp", "OSTime", "[TIME_AUDRCP_MAX]")),
	# ]],
]

include_time = [
	[main.f_str, str_time],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x8033C390, 0x8033C520],
	[ultra.c.f_extern, "E0.code.data", 0x8032DF10, 0x8032DF1C],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x8027E3E0, 0x8027F4D4],
]

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

#define VSPEED(speed)           ((int)((speed)*0x10000))

#define ShpGetLayer(shp)  ((shp)->flag >> 8)
#define ShpSetLayer(shp, layer) \\
	((shp)->flag = (layer) << 8 | ((shp)->flag & 0xFF))
"""

struct_shape = [
	[0x18, "struct", "anime", "ANIME", [
		(0x00, main.sym_var("flag", "short")),
		(0x02, main.sym_var("waist", "short")),
		(0x04, main.sym_var("start", "short")),
		(0x06, main.sym_var("loop", "short")),
		(0x08, main.sym_var("frame", "short")),
		(0x0A, main.sym_var("joint", "short")),
		(0x0C, main.sym_var("val", "short *")),
		(0x10, main.sym_var("tbl", "u16 *")),
		(0x14, main.sym_var("size", "size_t")),
	]],
	[0x14, "struct", "skeleton", "SKELETON", [
		(0x00, main.sym_var("index", "short")),
		(0x02, main.sym_var("waist", "short")),
		(0x04, main.sym_var("anime", "ANIME *")),
		(0x08, main.sym_var("frame", "short")),
		(0x0A, main.sym_var("stamp", "u16")),
		(0x0C, main.sym_var("vframe", "int")),
		(0x10, main.sym_var("vspeed", "int")),
	]],
	[0x14, "struct", "shape", "SHAPE", [
		(0x00, main.sym_var("type", "short")),
		(0x02, main.sym_var("flag", "short")),
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
		(0x1C, main.sym_var("code", "short")),
		(0x1E, main.sym_var("index", "short")),
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
		(0x0C, main.sym_var("scene", "char")),
		(0x0D, main.sym_var("group", "char")),
		(0x10, main.sym_var("info", "u32")),
		(0x14, main.sym_var("script", "OBJLANG *")),
		(0x18, main.sym_var("shape", "SHAPE *")),
		(0x1C, main.sym_var("next", "struct actor *")),
	]],
	[0x60, "struct", "sobject", "SOBJECT", [
		(0x00, main.sym_var("s", "SHAPE")),
		(0x14, main.sym_var("shape", "SHAPE *")),
		(0x18, main.sym_var("scene", "char")),
		(0x19, main.sym_var("group", "char")),
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

include_shape = [
	[main.f_str, str_shape],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_shape],
	[main.f_str, "\n"],
	[main.f_str, "typedef void *SHPCALL(int code, SHAPE *shape, void *data);\n"],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_shp],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.data", 0x8038B810, 0x8038B810], # shape
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.text", 0x8037B220, 0x8037CB60], # shape
]

include_draw = [
	[ultra.c.f_extern, "E0.code.data", 0x8033BAE0, 0x8033C38C],
	[ultra.c.f_extern, "E0.code.data", 0x8032DE70, 0x8032DF0C],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x8027B6C0, 0x8027E3DC],
]

include_script = [
	[ultra.c.f_extern, "E0.ulib.data", 0x8038BCA0, 0x8038BD9C], # shplang
	[ultra.c.f_extern, "E0.ulib.data", 0x8038B810, 0x8038B894], # shplang
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.data", 0x8038BDA0, 0x8038BE2C], # seqlang
	[ultra.c.f_extern, "E0.ulib.data", 0x8038B8A0, 0x8038B9AC], # seqlang
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.data", 0x8038EEE0, 0x8038EEE2], # objlang
	[ultra.c.f_extern, "E0.ulib.data", 0x8038B9B0, 0x8038BA90], # objlang
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.text", 0x8037CB60, 0x8037E19C], # shplang
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.text", 0x8037E1A0, 0x80380684], # seqlang
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.text", 0x80383B70, 0x80385F88], # seqlang
]

str_object = """
#define OBJECT_MAX              240

#define OBJ_HIT_MAX             4
#define OBJ_WORK_MAX            80

#define ObjGetArg(obj)          ((obj)->o_actorinfo >> 24)
#define ObjSetArg(obj, arg)     ((obj)->o_actorinfo = (arg) << 24)
#define ObjGetCode(obj)         (((obj)->o_actorinfo & 0x00FF0000) >> 16)
#define ObjSetCode(obj, code)   ((obj)->o_actorinfo = ((code) & 0xFF) << 16)
"""

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
		(0x074, main.sym_var("flag", "short")),
		(0x076, main.sym_var("hit_count", "short")),
		(0x078, main.sym_var("hit", "struct object *", "[OBJ_HIT_MAX]")),
		[0x088, "union", "work", [
			(None, main.sym_var("s", "short", "[2]")),
			(None, main.sym_var("i", "int")),
			(None, main.sym_var("f", "float")),
			(None, main.sym_var("p", "void *")),
		], "[OBJ_WORK_MAX]"],
		(0x1C8, main.sym_var("_1C8", "void *")),
		(0x1CC, main.sym_var("pc", "OBJLANG *")),
		(0x1D0, main.sym_var("sp", "unsigned int")),
		(0x1D4, main.sym_var("stack", "unsigned long", "[8]")),
		(0x1F4, main.sym_var("sleep", "short")),
		(0x1F6, main.sym_var("actor_type", "short")),
		(0x1F8, main.sym_var("hit_r", "float")),
		(0x1FC, main.sym_var("hit_h", "float")),
		(0x200, main.sym_var("dmg_r", "float")),
		(0x204, main.sym_var("dmg_h", "float")),
		(0x208, main.sym_var("hit_offset", "float")),
		(0x20C, main.sym_var("script", "OBJLANG *")),
		(0x210, main.sym_var("_210", "struct object *")),
		(0x214, main.sym_var("movebg", "struct object *")),
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
		(0x00, main.sym_var("ground", "short")),
		(0x02, main.sym_var("roof", "short")),
		(0x04, main.sym_var("wall", "short")),
	]],
]

include_object = [
	[main.f_str, str_object],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_object],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x8033CBE0, 0x80361266], # object
	[ultra.c.f_extern, "E0.code.data", 0x8032FEC0, 0x8032FFFC], # object
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x8029C780, 0x8029D884], # object
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802C97D0, 0x802CA03C], # objlist
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802C8F40, 0x802C97C8], # hitcheck
]

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
		(0x14, main.sym_var("flag", "short")),
		(0x16, main.sym_var("count", "short")),
		(0x18, main.sym_var("wall", "BGFACE *", "[4]")),
	]],
]

include_map = [
	[main.f_str, str_map],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_map],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.data", 0x8038BE30, 0x8038BE90], # bgcheck
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.data", 0x8038BE90, 0x8038EED4], # bgload
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.text", 0x80380690, 0x8038248C], # bgcheck
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.ulib.text", 0x80382490, 0x80383B6C], # bgload
]

struct_objectlib = [
	[0x24, "struct", "splash", "SPLASH", [
		(0x00, main.sym_var("flag", "short")),
		(0x02, main.sym_var("shape", "short")),
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
		(0x00, main.sym_var("code", "char")),
		(0x01, main.sym_var("count", "char")),
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
		(0x00, main.sym_var("flag", "short")),
		(0x02, main.sym_var("l", "char")),
		(0x03, main.sym_var("r", "char")),
		(0x04, main.sym_var("se", "Na_Se")),
	]],
]

include_objectlib = [
	[ultra.c.f_struct, struct_objectlib],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x80361270, 0x80361274], # objectlib
	[ultra.c.f_extern, "E0.code.data", 0x80330000, 0x80330018], # objectlib
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x8029DCD4, 0x802A45E4], # objectlib
	[ultra.c.f_extern, "E0.code.text", 0x802A46CC, 0x802A5618], # objectlib
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802CA040, 0x802CA370], # objsound
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x80330E20, 0x80330E38], # movebg
	[ultra.c.f_extern, "E0.code.text", 0x802C89F0, 0x802C8F28], # movebg
	[main.f_str, "#if REVISION >= 199609\n"],
	[ultra.c.f_extern, "E0.code.text", [0x802C8F28]], # movebg
	[main.f_str, "#endif\n"],
]

str_debug = """
#define DEBUG_SHOW              1
#define DEBUG_2                 2
#define DEBUG_ALL               0xFF
"""

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

include_debug = [
	[main.f_str, str_debug],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_debug],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x80361290, 0x803612AC], # debug
	[ultra.c.f_extern, "E0.code.data", 0x80330E40, 0x80330EB2], # debug
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802CA370, 0x802CB5B4], # debug
]

str_wipe = """
#define WIPE_ISIN(type)         (!((type) & 1))
#define WIPE_ISOUT(type)        ((type) & 1)
"""

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

include_wipe = [
	[main.f_str, str_wipe],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_wipe],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x80330EC0, 0x80330ED8],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802CB5C0, 0x802CD1E8],
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

include_shadow = [
	[ultra.c.f_struct, struct_shadow],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x803612B0, 0x803612B6],
	[ultra.c.f_extern, "E0.code.data", 0x80330EE0, 0x80330EF8],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802CD280, 0x802CF5A4],
]

str_background = """
#define BACK_TW                 10
#define BACK_TH                 8
"""

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

include_background = [
	[main.f_str, str_background],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_background],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x803612C0, 0x803612E0],
	[ultra.c.f_extern, "E0.code.data", 0x80330F00, 0x80330F2E],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802CF5B0, 0x802D007C],
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
	# 	(0x10, main.sym_var("begin", "Gfx *")),
	# 	(0x14, main.sym_var("end", "Gfx *")),
	# 	(0x18, main.sym_var("draw", "Gfx *")),
	# 	(0x1C, main.sym_var("r", "u8")),
	# 	(0x1D, main.sym_var("g", "u8")),
	# 	(0x1E, main.sym_var("b", "u8")),
	# 	(0x1F, main.sym_var("alpha", "u8")),
	# 	(0x20, main.sym_var("layer", "int")),
	# ]],
]

include_water = [
	[ultra.c.f_struct, struct_water],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x803612E0, 0x803612E2], # water
	[ultra.c.f_extern, "E0.code.data", 0x80330F30, 0x803312F0], # water
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802D0254, 0x802D104C], # water
	[ultra.c.f_extern, "E0.code.text", 0x802D1330, 0x802D1B70], # water
]

include_objshape = [
	[ultra.c.f_extern, "E0.code.data", 0x803612F0, 0x803612F1],
	[ultra.c.f_extern, "E0.code.data", 0x803312F0, 0x803312FC],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802D2210, 0x802D2360],
]

struct_wave = [
	[0x78, "struct", "wave", "WAVE", [
		(0x00, main.sym_var("code", "short")),
		(0x02, main.sym_var("nmesh", "char")),
		(0x03, main.sym_var("type", "char")),
		(0x04, main.sym_var("stepprev", "char")),
		(0x05, main.sym_var("stepstat", "char")),
		(0x06, main.sym_var("steptrig", "char")),
		(0x07, main.sym_var("state", "char")),
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
		(0x6C, main.sym_var("mode", "char")),
		(0x6D, main.sym_var("alpha", "u8")),
		(0x6E, main.sym_var("diveprev", "char")),
		(0x6F, main.sym_var("divestat", "char")),
		(0x70, main.sym_var("divetrig", "char")),
		(0x74, main.sym_var("size", "float")),
	]],
]

include_wave = [
	[ultra.c.f_struct, struct_wave],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x80361300, 0x8036131D],
	[ultra.c.f_extern, "E0.code.data", 0x80331300, 0x80331360],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802D29C0, 0x802D5B98],
]

struct_dprint = [
	# [0x3C, "struct", "dprint", "DPRINT", [
	# 	(0x00, main.sym_var("x", "int")),
	# 	(0x04, main.sym_var("y", "int")),
	# 	(0x08, main.sym_var("len", "short")),
	# 	(0x0A, main.sym_var("str", "char", "[50]")),
	# ]],
]

include_dprint = [
	[ultra.c.f_extern, "E0.code.data", 0x80361320, 0x803613F0],
	[ultra.c.f_extern, "E0.code.data", 0x80331360, 0x80331364],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802D5E00, 0x802D6F18],
]

str_message = """
#define GFX_PUSH                1
#define GFX_NOPUSH              2

#define FONT_SEL                1
#define FONT_GLB                2

#define CURSOR_V                1
#define CURSOR_H                2

#define MsgIsOpen()             (MsgGet() >= 0)
"""

struct_message = [
	[0x10, "struct", "message", "MESSAGE", [
		(0x00, main.sym_var("code", "int")),
		(0x04, main.sym_var("line", "char")),
		(0x06, main.sym_var("x", "short")),
		(0x08, main.sym_var("y", "short")),
		(0x0C, main.sym_var("str", "unsigned char *")),
	]],
]

include_message = [
	[main.f_str, str_message],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_message],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x803613F0, 0x803613FF],
	[ultra.c.f_extern, "E0.code.data", 0x80331370, 0x8033174C],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802D6F20, 0x802DDDEC],
]

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

struct_tag = [
	# [0x08, "struct", "tagobj", "TAGOBJ", [
	# 	(0x00, main.sym_var("script", "OBJLANG *")),
	# 	(0x04, main.sym_var("shape", "short")),
	# 	(0x06, main.sym_var("code", "short")),
	# ]],
	# [0x08, "struct", "mapobj", "MAPOBJ", [
	# 	(0x00, main.sym_var("index", "u8")),
	# 	(0x01, main.sym_var("ext", "u8")),
	# 	(0x02, main.sym_var("arg", "u8")),
	# 	(0x03, main.sym_var("shape", "u8")),
	# 	(0x04, main.sym_var("script", "OBJLANG *")),
	# ]],
]

include_tag = [
	[main.f_str, str_tag],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_tag],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x803317E0, 0x803325E8],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802E20A0, 0x802E2CF0],
]

str_hud = """
#define HUD_LIFE                0x0001
#define HUD_COIN                0x0002
#define HUD_STAR                0x0004
#define HUD_METER               0x0008
#define HUD_KEY                 0x0010
#define HUD_TIME                0x0040
#define HUD_ALERT               0x8000

#define HUD_ALL                 0x003F
"""

struct_hud = [
	[0x0E, "struct", "hud", "HUD", [
		(0x00, main.sym_var("life", "short")),
		(0x02, main.sym_var("coin", "short")),
		(0x04, main.sym_var("star", "short")),
		(0x06, main.sym_var("power", "short")),
		(0x08, main.sym_var("key", "short")),
		(0x0A, main.sym_var("flag", "short")),
		(0x0C, main.sym_var("time", "u16")),
	]],
	# [0x0C, "struct", "meter", "METER", [
	# 	(0x00, main.sym_var("state", "char")),
	# 	(0x02, main.sym_var("x", "short")),
	# 	(0x04, main.sym_var("y", "short")),
	# 	(0x08, main.sym_var("scale", "float")),
	# ]],
]

include_hud = [
	[main.f_str, str_hud],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_hud],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x80361440, 0x80361442],
	[ultra.c.f_extern, "E0.code.data", 0x803325F0, 0x8033260C],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802E2CF0, 0x802E3E50],
]

struct_camera = [
	[0x24, "struct", "pl_camera", "PL_CAMERA", [
		(0x00, main.sym_var("state", "u32")),
		(0x04, main.sym_var("pos", "FVEC")),
		(0x10, main.sym_var("ang", "SVEC")),
		(0x16, main.sym_var("neck_angx", "short")),
		(0x18, main.sym_var("neck_angy", "short")),
		(0x1A, main.sym_var("eyes", "short")),
		(0x1C, main.sym_var("hand", "short")),
		(0x1E, main.sym_var("demo", "short")),
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
		(0x00, main.sym_var("scene", "char")),
		(0x04, main.sym_var_fnc("callback", arg=(
			"CAMERA *cam",
		))),
		(0x08, main.sym_var("pos", "SVEC")),
		(0x0E, main.sym_var("size", "SVEC")),
		(0x14, main.sym_var("ang", "short")),
	]],
	[0x08, "struct", "campath", "CAMPATH", [
		(0x00, main.sym_var("code", "char")),
		(0x01, main.sym_var("time", "u8")),
		(0x02, main.sym_var("pos", "SVEC")),
	]],
	[0x06, "struct", "camdemo", "CAMDEMO", [
		(0x00, main.sym_var_fnc("callback", arg=(
			"CAMERA *cam",
		))),
		(0x04, main.sym_var("time", "short")),
	]],
]

include_camera = [
	[ultra.c.f_struct, struct_camera],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x8033C520, 0x8033CBE0], # camera / end is wrong
	[ultra.c.f_extern, "E0.code.data", 0x8032DF20, 0x8032FEB4], # camera
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x8027F590, 0x80287D30], # camera
	[ultra.c.f_extern, "E0.code.text", 0x80287DC0, 0x8029AA3C], # camera
	[ultra.c.f_extern, "E0.code.text", 0x8029AB94, 0x8029C764], # camera
]

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
		(0x00, main.sym_var("index", "char")),
		(0x01, main.sym_var("flag", "char")),
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

include_scene = [
	[main.f_str, str_scene],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_scene],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x8033B4B0, 0x8033BAE0],
	[ultra.c.f_extern, "E0.code.data", 0x8032DDC0, 0x8032DE70],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x8027A7D0, 0x8027B6C0],
]

str_player = """
#define PL_JUMPVOICE            0
#define PL_NULLVOICE            ((Na_Se)-1)

#define SLIP_DEFAULT            0
#define SLIP_19                 19
#define SLIP_20                 20
#define SLIP_21                 21

#define PL_Damage(pl, n) \\
	((pl)->damage += (pl)->flag & PL_HEADCAP ? 4*(n) : 6*(n))
"""

struct_player = [
	[0x18, "struct", "bump", "BUMP", [
		(0x00, main.sym_var("power", "float")),
		(0x04, main.sym_var("radius", "float")),
		(0x08, main.sym_var("posx", "float")),
		(0x0C, main.sym_var("posz", "float")),
		(0x10, main.sym_var("velx", "float")),
		(0x14, main.sym_var("velz", "float")),
	]],
	[0x28, "struct", "pl_ctrl", "PL_CTRL", [
		(0x00, main.sym_var("state", "u32")),
		(0x04, main.sym_var("head", "char")),
		(0x05, main.sym_var("eyes", "char")),
		(0x06, main.sym_var("hand", "char")),
		(0x07, main.sym_var("wing", "char")),
		(0x08, main.sym_var("cap", "short")),
		(0x0A, main.sym_var("take", "char")),
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
		(0x26, main.sym_var("invincible", "short")),
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
		(0x98, main.sym_var("ctrl", "PL_CTRL *")),
		(0x9C, main.sym_var("cont", "CONTROLLER *")),
		(0xA0, main.sym_var("anime", "BANK *")),
		(0xA4, main.sym_var("hit_status", "u32")),
		(0xA8, main.sym_var("coin", "short")),
		(0xAA, main.sym_var("star", "short")),
		(0xAC, main.sym_var("key", "s8")),
		(0xAD, main.sym_var("life", "s8")),
		(0xAE, main.sym_var("power", "short")),
		(0xB0, main.sym_var("waist", "short")),
		(0xB2, main.sym_var("damage", "u8")),
		(0xB3, main.sym_var("recover", "u8")),
		(0xB4, main.sym_var("press", "u8")),
		(0xB5, main.sym_var("alpha", "u8")),
		(0xB6, main.sym_var("cap_timer", "u16")),
		(0xB8, main.sym_var("prevstar", "short")),
		(0xBC, main.sym_var("peak", "float")),
		(0xC0, main.sym_var("sink", "float")),
		(0xC4, main.sym_var("gravity", "float")),
	]],
	# [0x18, "struct", "plwalk", "PLWALK", [
	# 	(0x00, main.sym_var("time", "short")),
	# 	(0x02, main.sym_var("jump_timer", "short")),
	# 	(0x04, main.sym_var("slip", "u32")),
	# 	(0x08, main.sym_var("next", "u32")),
	# 	(0x0C, main.sym_var("jump", "u32")),
	# 	(0x10, main.sym_var("land", "u32")),
	# 	(0x14, main.sym_var("slide", "u32")),
	# ]],
	# [0x08, "struct", "collision", "COLLISION", [
	# 	(0x00, main.sym_var("type", "u32")),
	# 	(0x04, main.sym_var_fnc("callback", val="int", arg=(
	# 		"PLAYER *pl",
	# 		"u32 flag",
	# 		"OBJECT *obj",
	# 	))),
	# ]],
]

include_player = [
	[main.f_str, str_player],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_player],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", [
		0x8032DAF8,
		0x8033B3B0,
	]],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x8024BFF0, 0x8025093C], # collision
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x80250940, 0x8025507C], # player
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x80255080, 0x80256DFC], # physics
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", [
		0x80256E88,
		0x802575A8,
		0x80257640,
		0x80263EE4,
		0x80274F10,
	]],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", [
		0x8025D798,
		0x802605D0,
		0x80263898,
		0x80269954,
		0x8026FB04,
		0x8027499C,
		0x80275FE0,
	]],
]

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

struct_game = [
	[0x08, "struct", "pl_entry", "PL_ENTRY", [
		(0x00, main.sym_var("type", "u8")),
		(0x01, main.sym_var("stage", "u8")),
		(0x02, main.sym_var("scene", "u8")),
		(0x03, main.sym_var("port", "u8")),
		(0x04, main.sym_var("code", "u32")),
	]],
]

include_game = [
	[main.f_str, str_game],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_game],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x8033B170, 0x8033B26F], # game
	[ultra.c.f_extern, "E0.code.data", 0x8032D6D0, 0x8032D948], # game
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802495E0, 0x8024BFE4], # game
]

include_course = [
	[ultra.c.f_extern, "E0.code.text", 0x8029C770, 0x8029C780], # course
]

str_backup = """
#define StageToCourse(stage)  ((int)coursetab[(stage)-1])

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

struct_backup = [
	[0x04, "struct", "bucheck", "BUCHECK", [
		(0x00, main.sym_var("key", "u16")),
		(0x02, main.sym_var("sum", "u16")),
	]],
	[0x20, "struct", "backupinfo", "BACKUPINFO", [
		(0x00, main.sym_var("time", "u32", "[4]")),
		(0x10, main.sym_var("sound", "u16")),
		"#ifdef MULTILANG",
		(0x12, main.sym_var("lang", "u16")),
		(0x14, main.sym_var("pad", "char", "[8]")),
		"#else",
		(0x12, main.sym_var("pad", "char", "[10]")),
		"#endif",
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

include_backup = [
	[main.f_str, str_backup],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_backup],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x8033B4A0, 0x8033B4A7], # backup
	[ultra.c.f_extern, "E0.code.data", 0x8032DD80, 0x8032DDBE], # backup
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x80279160, 0x8027A698], # backup
	[main.f_str, "#ifdef MULTILANG\n"],
	[ultra.c.f_extern, "P0.code.text", [0x8026B028, 0x8026B05C]], # backup
	[main.f_str, "#endif\n"],
	[ultra.c.f_extern, "E0.code.text", 0x8027A698, 0x8027A7C4], # backup
]

include_buffer = [
	[ultra.c.f_extern, "E0.code.data", 0x80200200, 0x80220DA0], # buffer
]

include_enemya = [
	[ultra.c.f_extern, "E0.code.text", [
		0x802AAE8C,
		0x802AB558,
		0x802AE0CC,
		0x802AE4C0,
		0x802BED7C,
		0x802C81B4,
	]],
]

include_enemyb = [
	[ultra.c.f_extern, "E0.code.text", [
		0x802E3E50,
		0x802F2B88,
	]],
]

include_enemyc = [
	[ultra.c.f_extern, "E0.code.text", [
		0x8030CD30,
	]],
]

struct_weather = [
	[0x38, "struct", "weather", "WEATHER", [
		(0x00, main.sym_var("flag", "char")),
		(0x02, main.sym_var("frame", "short")),
		(0x04, main.sym_var("x", "int")),
		(0x08, main.sym_var("y", "int")),
		(0x0C, main.sym_var("z", "int")),
		(0x10, main.sym_var("work", "int", "[10]")),
	]],
]

include_weather = [
	[ultra.c.f_struct, struct_weather],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x80361400, 0x80361440],
	[ultra.c.f_extern, "E0.code.data", 0x80331750, 0x803317D8],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802DDDF0, 0x802E2094],
]

include_face = [
	[ultra.c.f_extern, "E0.menu.text", [
		0x8019C418,
		0x8019C450,
		0x8019C4EC,
		0x8019C684,
		0x8019C874,
		0x8019C930,
		0x8019C9C8,
		0x8019C9F8,
	]],
]

str_Na_internal = """
#ifndef __GNUC__
#define __attribute__(x)
#endif

#define DALIGN                  __attribute__((aligned(4)))
#define BALIGN                  __attribute__((aligned(8)))
#define UNUSED                  __attribute__((unused))
#define FALLTHROUGH             __attribute__((fallthrough))

typedef unsigned int size_t;
"""

struct_Na_internal = [
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

src_audio_Na_internal = [
	[main.f_str, "#ifndef __NA_INTERNAL_H__\n#define __NA_INTERNAL_H__\n\n"],
	[main.f_str, "#include <ultra64.h>\n"],
	[main.f_str, "#include <string.h>\n"],
	[main.f_str, "#include <sm64/defaudio.h>\n"],
	[main.f_str, "#include <sm64/main.h>\n"],
	[main.f_str, "#include <sm64/Na.h>\n\n"],
	[main.f_str, str_Na_internal],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_Na_internal],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x801CE000, 0x80200200], # buffer
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x80220DA0, 0x80226CD0], # audio/work
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.data", 0x80361490, 0x80364BA0], # audio/game
	[ultra.c.f_extern, "E0.code.data", 0x80332E50, 0x80335010], # audio/driver..audio/game
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.code.text", 0x80314A30, 0x80322364], # audio/driver..audio/game
	[main.f_str, "\n#endif /* __NA_INTERNAL_H__ */\n"],
]

str_face = """
#ifndef __GNUC__
#define __attribute__(x)
#endif

#define DALIGN                  __attribute__((aligned(4)))
#define BALIGN                  __attribute__((aligned(8)))
#define UNUSED                  __attribute__((unused))
#define FALLTHROUGH             __attribute__((fallthrough))

typedef unsigned int size_t;

""" + "".join(["extern char __dummy%d[];\n" % i for i in range(100)]) + """
#define MEM_FREE 1
#define MEM_USED 2
"""

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
	[0x14, "struct", "memblock", "MEMBLOCK", [
		(0x00, main.sym_var("addr", "char *")),
		(0x04, main.sym_var("size", "size_t")),
		(0x08, main.sym_var("type", "unsigned char")),
		(0x09, main.sym_var("flag", "unsigned char")),
		(0x0C, main.sym_var("next", "struct memblock *")),
		(0x10, main.sym_var("prev", "struct memblock *")),
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

src_face_face = [
	[main.f_str, "#ifndef __FACE_H__\n#define __FACE_H__\n\n"],
	[main.f_str, "#include <ultra64.h>\n"],
	[main.f_str, "#include <sm64/gbiext.h>\n"],
	[main.f_str, "#include \"dynlist.h\"\n\n"],
	[main.f_str, str_face],
	[main.f_str, "\n"],
	[ultra.c.f_struct, struct_face],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.menu.face", 0x04000000, 0x040326E0],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.menu.data", 0, 0],
	[ultra.c.f_extern, "E0.menu.data", 0x801A81E0, 0x801B54C0],
	[main.f_str, "\n"],
	[ultra.c.f_extern, "E0.menu.text", 0x80177710, 0x801A7830],
	[main.f_str, "\n#endif /* __FACE_H__ */\n"],
]

def f_header(name, seq):
	x = "__SM64_%s_H__" % name.upper()
	return [main.s_file, "include/sm64/%s.h" % name, [
		[main.f_str, "#ifndef %s\n#define %s\n\n" % (x, x)],
	] + seq + [
		[main.f_str, "\n#endif /* %s */\n" % x],
	]]

seq = [
	f_header("math", include_math),
	f_header("memory", include_memory),
	f_header("disk", include_disk),

	f_header("main", include_main),
	f_header("graphics", include_graphics),
	f_header("Na", include_Na),
	f_header("audio", include_audio),
	f_header("motor", include_motor),
	f_header("time", include_time),

	f_header("shape", include_shape),
	f_header("draw", include_draw),
	f_header("script", include_script),
	f_header("object", include_object),
	f_header("map", include_map),

	f_header("objectlib", include_objectlib),
	f_header("debug", include_debug),
	f_header("wipe", include_wipe),
	f_header("shadow", include_shadow),
	f_header("background", include_background),
	f_header("water", include_water),
	f_header("objshape", include_objshape),
	f_header("wave", include_wave),
	f_header("dprint", include_dprint),
	f_header("message", include_message),
	f_header("tag", include_tag),
	f_header("hud", include_hud),

	f_header("camera", include_camera),
	f_header("scene", include_scene),
	f_header("player", include_player),
	f_header("game", include_game),
	f_header("course", include_course),
	f_header("backup", include_backup),

	f_header("buffer", include_buffer),

	f_header("enemya", include_enemya),
	f_header("enemyb", include_enemyb),
	f_header("enemyc", include_enemyc),

	f_header("weather", include_weather),

	f_header("face", include_face),

	[main.s_file, "src/audio/Na_internal.h", src_audio_Na_internal],
	[main.s_file, "src/face/face.h", src_face_face],
]
