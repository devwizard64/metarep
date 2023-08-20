import table

str_main = """
#define SCREEN_WD               320
#define SCREEN_HT               240
#define BORDER_HT               8
"""

str_graphics = """
#define GFX_LEN                 6400
#define FIFO_SIZE               0x1F000
#define FIFO_LEN                (FIFO_SIZE/8)

#define CONTROLLER_LEN          2
"""

str_memory = """
#define MEM_ALLOC_L 0
#define MEM_ALLOC_R 1

#define malloc(size)            heap_alloc(mem_heap, size)
#define free(ptr)               heap_free(mem_heap, ptr)
"""

str_save = """
#define stage_to_course(stage)  course_table[(stage)-1]

#define save_file_star_total(file)  save_file_star_range(file, 0, 24)

#define save_write()                save_file_write(save_index-1)
#define save_erase()                save_file_erase(save_index-1)
#define save_isactive()             save_file_isactive(save_index-1)
#define save_star_count(course)     save_file_star_count(save_index-1, course)
#define save_star_range(min, max)   save_file_star_range(save_index-1, min, max)
#define save_star_total()           save_file_star_total(save_index-1)
#define save_star_get(course)       save_file_star_get(save_index-1, course)
#define save_star_set(course, flag) \\
	save_file_star_set(save_index-1, course, flag)
#define save_coin_get(course)       save_file_coin_get(save_index-1, course)
"""

str_scene = """
#define SCENE_LEN               8
#define SHAPE_LEN               0x100

#define SCENE_FLAG_01           0x01
"""

str_time = """
#define TIME_GFXCPU_START       0
#define TIME_GFXCPU_ENDUPD      1
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

str_object = """
#define obj_code_get(obj)               (((obj)->o_arg & 0x00FF0000) >> 16)
"""

str_obj_data = """
#define P_OBJ_START             31
#define P_OBJ_END               (P_OBJ_START+(-1))

#define M_EXT_NULL      0
#define M_EXT_AY        1
#define M_EXT_AY_ARG    2
#define M_EXT_XYZ       3
#define M_EXT_AY_CODE   4

#define P_OBJ(obj, ay, px, py, pz, arg) \\
	(OBJ_DATA)((P_OBJ_START+P_OBJ_##obj) | (ay) << 9), px, py, pz, arg
"""

str_math = """
#define sin(x)  math_sin[(u16)(x) >> 4]
#define cos(x)  math_cos[(u16)(x) >> 4]
"""

str_shape = """
#define S_TYPE_SCENE            (1)
#define S_TYPE_ORTHO            (2)
#define S_TYPE_PERSP            (3 | 0x100)
#define S_TYPE_LAYER            (4)

#define S_TYPE_EMPTY            (10)
#define S_TYPE_LOD              (11)
#define S_TYPE_SELECT           (12 | 0x100)

#define S_TYPE_CAMERA           (20 | 0x100)
#define S_TYPE_POSANG           (21)
#define S_TYPE_POS              (22)
#define S_TYPE_ANG              (23)
#define S_TYPE_OBJECT           (24)
#define S_TYPE_JOINT            (25)
#define S_TYPE_BILLBOARD        (26)
#define S_TYPE_GFX              (27)
#define S_TYPE_SCALE            (28)

#define S_TYPE_SHADOW           (40)
#define S_TYPE_LIST             (41)
#define S_TYPE_CALLBACK         (42 | 0x100)
#define S_TYPE_BACK             (44 | 0x100)
#define S_TYPE_HAND             (46 | 0x100)
#define S_TYPE_CULL             (47)

#define S_FLAG_ACTIVE           0x0001
#define S_FLAG_HIDE             0x0002
#define S_FLAG_BILLBOARD        0x0004
#define S_FLAG_ZBUFFER          0x0008
#define S_FLAG_OBJHIDE          0x0010
#define S_FLAG_ANIME            0x0020

#define S_CODE_INIT             0
#define S_CODE_DRAW             1
#define S_CODE_CLOSE            2
#define S_CODE_OPEN             3
#define S_CODE_EXIT             4
#define S_CODE_MTX              5

#define shape_layer_get(shp)  (((SHAPE *)(shp))->flag >> 8)
#define shape_layer_set(shp, layer) \\
	(((SHAPE *)(shp))->flag = (layer) << 8 | (((SHAPE *)(shp))->flag & 0xFF))
"""

str_Na = """
#define Na_SE_fixed(se)         Na_SE_play(se, Na_0)
#define Na_SE_obj(se, obj)      Na_SE_play(se, (obj)->list.s.view)

#define Na_SE_lock()            Na_IO_lock(2, 0x037A)
#define Na_SE_unlock()          Na_IO_unlock(2, 0x037A)

typedef u32 NA_SE;
"""

struct_main = [
	[0x4C, "struct", "sc_task", [
		(0x00, table.sym_var("task",    "OSTask")),
		(0x40, table.sym_var("mq",      "OSMesgQueue *")),
		(0x44, table.sym_var("msg",     "OSMesg")),
		(0x48, table.sym_var("state",   "s32")),
	]],
	[0x08, "struct", "sc_client", [
		(0x00, table.sym_var("mq",  "OSMesgQueue *")),
		(0x04, table.sym_var("msg", "OSMesg")),
	]],
]

struct_graphics = [
	[0xC84C, "struct", "frame", [
		(0x0000, table.sym_var("gfx",       "Gfx", "[GFX_LEN]")),
		(0xC800, table.sym_var("task",      "SC_TASK")),
	]],
	[0x1C, "struct", "controller", [
		(0x00, table.sym_var("stick_x",     "s16")),
		(0x02, table.sym_var("stick_y",     "s16")),
		(0x04, table.sym_var("x",           "float")),
		(0x08, table.sym_var("y",           "float")),
		(0x0C, table.sym_var("d",           "float")),
		(0x10, table.sym_var("held",        "u16")),
		(0x12, table.sym_var("down",        "u16")),
		(0x14, table.sym_var("status",      "OSContStatus *")),
		(0x18, table.sym_var("pad",         "OSContPad *")),
	]],
	[0x04, "struct", "demo", [
		(0x00, table.sym_var("count",   "u8")),
		(0x01, table.sym_var("stick_x", "s8")),
		(0x02, table.sym_var("stick_y", "s8")),
		(0x03, table.sym_var("button",  "u8")),
	]],
]

struct_game = [
	[0x10, "struct", "staff", [
		(0x00, table.sym_var("stage",   "u8")),
		(0x01, table.sym_var("scene",   "u8")),
		(0x02, table.sym_var("flag",    "u8")),
		(0x03, table.sym_var("ang",     "u8")),
		(0x04, table.sym_var("pos",     "VECS")),
		(0x0C, table.sym_var("str",     "const char **")),
	]],
	[0x08, "struct", "struct_8033B248", [
		(0x00, table.sym_var("type",    "u8")),
		(0x01, table.sym_var("stage",   "u8")),
		(0x02, table.sym_var("scene",   "u8")),
		(0x03, table.sym_var("port",    "u8")),
		(0x04, table.sym_var("arg",     "u32")),
	]],
]

struct_collision = [
	[0x08, "struct", "collision", [
		(0x00, table.sym_var("type", "u32")),
		(0x04, table.sym_var_fnc("callback", val="int", arg=(
			"struct player *pl",
			"u32 flag",
			"struct object *obj",
		))),
	]],
]

struct_player = [
	[0x28, "struct", "pl_shape", [
		(0x00, table.sym_var("state",   "u32")),
		(0x04, table.sym_var("head",    "s8")),
		(0x05, table.sym_var("eyes",    "s8")),
		(0x06, table.sym_var("glove",   "s8")),
		(0x07, table.sym_var("wing",    "s8")),
		(0x08, table.sym_var("cap",     "s16")),
		(0x0A, table.sym_var("hold",    "s8")),
		(0x0B, table.sym_var("punch",   "u8")),
		(0x0C, table.sym_var("torso",   "VECS")),
		(0x12, table.sym_var("neck",    "VECS")),
		(0x18, table.sym_var("hand",    "VECF")),
		(0x24, table.sym_var("obj",     "struct object *")),
	]],
	[0xC8, "struct", "player", [
		(0x00, table.sym_var("index",       "u16")),
		(0x02, table.sym_var("event",       "u16")),
		(0x04, table.sym_var("flag",        "u32")),
		(0x08, table.sym_var("particle",    "u32")),
		(0x0C, table.sym_var("state",       "u32")),
		(0x10, table.sym_var("state_prev",  "u32")),
		(0x14, table.sym_var("ground_se",   "u32")),
		(0x18, table.sym_var("mode",        "u16")),
		(0x1A, table.sym_var("timer",       "u16")),
		(0x1C, table.sym_var("arg",         "u32")),
		(0x20, table.sym_var("stick_dist",  "float")),
		(0x24, table.sym_var("stick_ang",   "short")),
		(0x26, table.sym_var("invincible",  "s16")),
		(0x28, table.sym_var("timer_a",         "u8")),
		(0x29, table.sym_var("timer_b",         "u8")),
		(0x2A, table.sym_var("timer_wall",      "u8")),
		(0x2B, table.sym_var("timer_ground",    "u8")),
		(0x2C, table.sym_var("ang",         "VECS")),
		(0x32, table.sym_var("ang_vel",     "VECS")),
		(0x38, table.sym_var("slide_ang",   "short")),
		(0x3A, table.sym_var("twirl_ang",   "short")),
		(0x3C, table.sym_var("pos",         "VECF")),
		(0x48, table.sym_var("vel",         "VECF")),
		(0x54, table.sym_var("vel_f",       "float")),
		(0x58, table.sym_var("vel_h",       "float", "[2]")),
		(0x60, table.sym_var("wall",        "struct map_plane *")),
		(0x64, table.sym_var("roof",        "struct map_plane *")),
		(0x68, table.sym_var("ground",      "struct map_plane *")),
		(0x6C, table.sym_var("roof_y",      "float")),
		(0x70, table.sym_var("ground_y",    "float")),
		(0x74, table.sym_var("ground_ang",  "short")),
		(0x76, table.sym_var("water",       "short")),
		(0x78, table.sym_var("obj_col",     "struct object *")),
		(0x7C, table.sym_var("obj_hold",    "struct object *")),
		(0x80, table.sym_var("obj_use",     "struct object *")),
		(0x84, table.sym_var("obj_ride",    "struct object *")),
		(0x88, table.sym_var("obj",         "struct object *")),
		(0x8C, table.sym_var("spawn",       "struct spawn *")),
		(0x90, table.sym_var("scene",       "struct scene *")),
		(0x94, table.sym_var("camera",      "struct pl_camera *")),
		(0x98, table.sym_var("shape",       "PL_SHAPE *")),
		(0x9C, table.sym_var("cont",        "struct controller *")),
		(0xA0, table.sym_var("anime",       "struct bank *")),
		(0xA4, table.sym_var("collision",   "u32")),
		(0xA8, table.sym_var("coin",        "s16")),
		(0xAA, table.sym_var("star",        "s16")),
		(0xAC, table.sym_var("key",         "s8")),
		(0xAD, table.sym_var("life",        "s8")),
		(0xAE, table.sym_var("power",       "s16")),
		(0xB0, table.sym_var("waist",       "short")),
		(0xB2, table.sym_var("hurt",        "u8")),
		(0xB3, table.sym_var("heal",        "u8")),
		(0xB4, table.sym_var("squish",      "u8")),
		(0xB5, table.sym_var("alpha",       "u8")),
		(0xB6, table.sym_var("timer_cap",   "u16")),
		(0xB8, table.sym_var("star_prev",   "s16")),
		(0xBC, table.sym_var("peak",        "float")),
		(0xC0, table.sym_var("sink",        "float")),
		(0xC4, table.sym_var("gravity",     "float")),
	]],
	[0x18, "struct", "pl_walk", [
		(0x00, table.sym_var("time",            "s16")),
		(0x02, table.sym_var("timer_ground",    "s16")),
		(0x04, table.sym_var("state_slip",      "u32")),
		(0x08, table.sym_var("state_next",      "u32")),
		(0x0C, table.sym_var("state_jump",      "u32")),
		(0x10, table.sym_var("state_fall",      "u32")),
		(0x14, table.sym_var("state_slide",     "u32")),
	]],
]

struct_memory = [
	[0x10, "struct", "mem_block", [
		(0x00, table.sym_var("prev",    "struct mem_block *")),
		(0x04, table.sym_var("next",    "struct mem_block *")),
		(0x08, table.sym_var("pad",     "u64")),
	]],
	[0x10, "struct", "mem_frame", [
		(0x00, table.sym_var("size",    "size_t")),
		(0x04, table.sym_var("blockl",  "MEM_BLOCK *")),
		(0x08, table.sym_var("blockr",  "MEM_BLOCK *")),
		(0x0C, table.sym_var("frame",   "struct mem_frame *")),
	]],
	[0x10, "struct", "arena", [
		(0x00, table.sym_var("size",    "long")),
		(0x04, table.sym_var("used",    "long")),
		(0x08, table.sym_var("start",   "char *")),
		(0x0C, table.sym_var("free",    "char *")),
	]],
	[0x08, "struct", "heap_block", [
		(0x00, table.sym_var("next",    "struct heap_block *")),
		(0x04, table.sym_var("size",    "size_t")),
	]],
	[0x10, "struct", "heap", [
		(0x00, table.sym_var("size",    "size_t")),
		(0x04, table.sym_var("block",   "HEAP_BLOCK *")),
		(0x08, table.sym_var("free",    "HEAP_BLOCK *")),
		(0x0C, table.sym_var("pad",     "u32")),
	]],
	[0x08, "struct", "bank_table", [
		(0x00, table.sym_var("len", "unsigned int")),
		(0x04, table.sym_var("src", "const char *")),
		[0x08, "struct", "table", [
			(0x00, table.sym_var("start",   "unsigned long")),
			(0x04, table.sym_var("size",    "unsigned long")),
		], "[1]"],
	]],
	[0x0C, "struct", "bank", [
		(0x00, table.sym_var("table",   "BANK_TABLE *")),
		(0x04, table.sym_var("src",     "const char *")),
		(0x08, table.sym_var("buf",     "char *")),
	]],
]

struct_save = [
	[0x04, "struct", "save_check", [
		(0x00, table.sym_var("key", "u16")),
		(0x02, table.sym_var("sum", "u16")),
	]],
	[0x20, "struct", "save_data", [
		(0x00, table.sym_var("time",    "u32",  "[4]")),
		(0x10, table.sym_var("output",  "u16")),
		(0x12, table.sym_var("pad",     "char", "[10]")),
		(0x1C, table.sym_var("check",   "SAVE_CHECK")),
	]],
	[0x38, "struct", "save_file", [
		(0x00, table.sym_var("stage",   "u8")),
		(0x01, table.sym_var("scene",   "u8")),
		(0x02, table.sym_var("pos",     "VECS")),
		(0x08, table.sym_var("flag",    "u32")),
		(0x0C, table.sym_var("star",    "u8",   "[25]")),
		(0x25, table.sym_var("coin",    "u8",   "[15]")),
		(0x34, table.sym_var("check",   "SAVE_CHECK")),
	]],
	[0x200, "struct", "save", [
		(0x000, table.sym_var("file",   "SAVE_FILE",    "[4][2]")),
		(0x1C0, table.sym_var("data",   "SAVE_DATA",    "[2]")),
	]],
]

struct_scene = [
	[0x20, "struct", "spawn", [
		(0x00, table.sym_var("pos",     "VECS")),
		(0x06, table.sym_var("ang",     "VECS")),
		(0x0C, table.sym_var("scene",   "s8")),
		(0x0D, table.sym_var("group",   "s8")),
		(0x10, table.sym_var("arg",     "u32")),
		(0x14, table.sym_var("script",  "O_SCRIPT *")),
		(0x18, table.sym_var("shape",   "struct shape *")),
		(0x1C, table.sym_var("next",    "struct spawn *")),
	]],
	[0x0C, "struct", "port", [
		(0x00, table.sym_var("index",   "u8")),
		(0x01, table.sym_var("stage",   "u8")),
		(0x02, table.sym_var("scene",   "u8")),
		(0x03, table.sym_var("port",    "u8")),
		(0x04, table.sym_var("obj",     "struct object *")),
		(0x08, table.sym_var("next",    "struct port *")),
	]],
	[0x3A, "struct", "scene", [
		(0x00, table.sym_var("index",       "s8")),
		(0x01, table.sym_var("flag",        "s8")),
		(0x02, table.sym_var("env",         "u16")),
		(0x04, table.sym_var("s",           "SHAPE_SCENE *")),
		(0x08, table.sym_var("map",         "MAP_DATA *")),
		(0x0C, table.sym_var("area",        "AREA_DATA *")),
		(0x10, table.sym_var("obj",         "OBJ_DATA *")),
		(0x14, table.sym_var("port",        "struct port *")),
		(0x18, table.sym_var("bgport",      "void *")),
		(0x1C, table.sym_var("connect",     "void *")),
		(0x20, table.sym_var("spawn",       "struct spawn *")),
		(0x24, table.sym_var("cam",         "struct camera *")),
		(0x28, table.sym_var("wind",        "void *")),
		(0x2C, table.sym_var("jet",         "void *", "[2]")),
		(0x34, table.sym_var("msg",         "u8", "[2]")),
		(0x36, table.sym_var("bgm_mode",    "u16")),
		(0x38, table.sym_var("bgm",         "u16")),
	]],
]

struct_time = [
	[0xC8, "struct", "time", [
		(0x00, table.sym_var("audcpu_i", "s16")),
		(0x02, table.sym_var("audrcp_i", "s16")),
		(0x08, table.sym_var("gfxcpu", "OSTime", "[TIME_GFXCPU_MAX]")),
		(0x30, table.sym_var("gfxrcp", "OSTime", "[TIME_GFXRCP_MAX]")),
		(0x48, table.sym_var("audcpu", "OSTime", "[TIME_AUDCPU_MAX]")),
		(0x88, table.sym_var("audrcp", "OSTime", "[TIME_AUDRCP_MAX]")),
	]],
]

struct_camera = [
	[0x01, "struct", "camera", [
		(0x00, table.sym_var("mode",    "u8")),
		# ...
	]],
	[0x18, "struct", "campos", [
		(0x00, table.sym_var("code",    "s16")),
		(0x04, table.sym_var("pos",     "VECF")),
		(0x10, table.sym_var("_10",     "f32")),
		(0x14, table.sym_var("dist",    "float")),
	]],
	[0x16, "struct", "camctl", [
		(0x00, table.sym_var("scene",   "s8")),
		(0x04, table.sym_var_fnc("callback", arg=(
			"struct camera *cam",
		))),
		(0x08, table.sym_var("pos",     "VECS")),
		(0x0E, table.sym_var("size",    "VECS")),
		(0x14, table.sym_var("ang",     "short")),
	]],
	[0x08, "struct", "campath", [
		(0x00, table.sym_var("code",    "s8")),
		(0x01, table.sym_var("time",    "u8")),
		(0x02, table.sym_var("pos",     "VECS")),
	]],
	[0x06, "struct", "camdemo", [
		(0x00, table.sym_var_fnc("callback", arg=(
			"struct camera *cam",
		))),
		(0x04, table.sym_var("time",    "s16")),
	]],
]

struct_object = [
	[0x68, "struct", "obj_list", [
		(0x000, table.sym_var("s",      "SHAPE_OBJECT")),
		(0x060, table.sym_var("next",   "struct obj_list *")),
		(0x064, table.sym_var("prev",   "struct obj_list *")),
	]],
	[0x260, "struct", "object", [
		(0x000, table.sym_var("list",   "OBJ_LIST")),
		(0x068, table.sym_var("parent", "struct object *")),
		(0x06C, table.sym_var("child",  "struct object *")),
		(0x070, table.sym_var("collision",  "u32")),
		(0x074, table.sym_var("flag",       "s16")),
		(0x076, table.sym_var("col_len",    "s16")),
		(0x078, table.sym_var("obj_col",    "struct object *", "[4]")),
		[0x088, "union", "mem", [
			(None, table.sym_var("s8",  "s8", "[4]")),
			(None, table.sym_var("u8",  "u8", "[4]")),
			(None, table.sym_var("s16", "s16", "[2]")),
			(None, table.sym_var("u16", "u16", "[2]")),
			(None, table.sym_var("s32", "s32")),
			(None, table.sym_var("u32", "u32")),
			(None, table.sym_var("f32", "f32")),
			(None, table.sym_var("ptr", "void *")),
		], "[80]"],
		(0x1C8, table.sym_var("_1C8",       "void *")),
		(0x1CC, table.sym_var("pc",         "O_SCRIPT *")),
		(0x1D0, table.sym_var("sp",         "unsigned int")),
		(0x1D4, table.sym_var("stack",      "void *", "[8]")),
		(0x1F4, table.sym_var("_1F4",       "s16")),
		(0x1F6, table.sym_var("_1F6",       "s16")),
		(0x1F8, table.sym_var("col_hit_r",  "float")),
		(0x1FC, table.sym_var("col_hit_h",  "float")),
		(0x200, table.sym_var("col_dmg_r",  "float")),
		(0x204, table.sym_var("col_dmg_h",  "float")),
		(0x208, table.sym_var("col_offset", "float")),
		(0x20C, table.sym_var("script",     "O_SCRIPT *")),
		(0x210, table.sym_var("_210",       "struct object *")),
		(0x214, table.sym_var("obj_ground", "struct object *")),
		(0x218, table.sym_var("map",        "MAP_DATA *")),
		(0x21C, table.sym_var("mf",         "MTXF")),
		(0x25C, table.sym_var("_25C",       "void *")),
	]],
	[0x10, "struct", "pl_pcl", [
		(0x00, table.sym_var("code",    "u32")),
		(0x04, table.sym_var("flag",    "u32")),
		(0x08, table.sym_var("shape",   "u8")),
		(0x0C, table.sym_var("script",  "O_SCRIPT *")),
	]],
	[0x06, "struct", "struct_8033D274", [
		(0x00, table.sym_var("ground",  "s16")),
		(0x02, table.sym_var("roof",    "s16")),
		(0x04, table.sym_var("wall",    "s16")),
	]],
	[0x24, "struct", "obj_splash", [
		(0x00, table.sym_var("flag",    "s16")),
		(0x02, table.sym_var("shape",   "s16")),
		(0x04, table.sym_var("script",  "O_SCRIPT *")),
		(0x08, table.sym_var("ay_mul",  "short")),
		(0x0A, table.sym_var("p_mul",   "short")),
		(0x0C, table.sym_var("vf_add",  "float")),
		(0x10, table.sym_var("vf_mul",  "float")),
		(0x14, table.sym_var("vy_add",  "float")),
		(0x18, table.sym_var("vy_mul",  "float")),
		(0x1C, table.sym_var("s_add",   "float")),
		(0x20, table.sym_var("s_mul",   "float")),
	]],
	[0x14, "struct", "obj_pcl", [
		(0x00, table.sym_var("arg",     "s8")),
		(0x01, table.sym_var("count",   "s8")),
		(0x02, table.sym_var("shape",   "u8")),
		(0x03, table.sym_var("offset",  "s8")),
		(0x04, table.sym_var("vf_add",  "s8")),
		(0x05, table.sym_var("vf_mul",  "s8")),
		(0x06, table.sym_var("vy_add",  "s8")),
		(0x07, table.sym_var("vy_mul",  "s8")),
		(0x08, table.sym_var("gravity", "s8")),
		(0x09, table.sym_var("drag",    "s8")),
		(0x0C, table.sym_var("s_add",   "float")),
		(0x10, table.sym_var("s_mul",   "float")),
	]],
	[0x10, "struct", "obj_col", [
		(0x00, table.sym_var("type",    "u32")),
		(0x04, table.sym_var("offset",  "u8")),
		(0x05, table.sym_var("ap",      "s8")),
		(0x06, table.sym_var("hp",      "s8")),
		(0x07, table.sym_var("coin",    "s8")),
		(0x08, table.sym_var("hit_r",   "short")),
		(0x0A, table.sym_var("hit_h",   "short")),
		(0x0C, table.sym_var("dmg_r",   "short")),
		(0x0E, table.sym_var("dmg_h",   "short")),
	]],
	[0x08, "struct", "obj_sfx", [
		(0x00, table.sym_var("flag",    "s16")),
		(0x02, table.sym_var("l",       "s8")),
		(0x03, table.sym_var("r",       "s8")),
		(0x04, table.sym_var("se",      "NA_SE")),
	]],
	[0x0C, "struct", "obj_debug", [
		(0x00, table.sym_var("flag",    "s16")),
		(0x02, table.sym_var("x",       "s16")),
		(0x04, table.sym_var("y",       "s16")),
		(0x06, table.sym_var("min",     "s16")),
		(0x08, table.sym_var("max",     "s16")),
		(0x0A, table.sym_var("height",  "s16")),
	]],
]

struct_object_a = [
	[0x0C, "struct", "object_a_0", [
		(0x00, table.sym_var("_00", "s16")),
		(0x04, table.sym_var("_04", "f32")),
		(0x08, table.sym_var("_08", "f32")),
	]],
	[0x0A, "struct", "object_a_1", [
		(0x00, table.sym_var("flag",    "s16")),
		(0x02, table.sym_var("scale",   "short")),
		(0x04, table.sym_var("map",     "MAP_DATA *")),
		(0x08, table.sym_var("dist",    "short")),
	]],
	[0x0C, "struct", "object_a_2", [
		(0x00, table.sym_var("count",   "s16")),
		(0x02, table.sym_var("add",     "short")),
		(0x04, table.sym_var("mul",     "short")),
		(0x06, table.sym_var("shape",   "s16")),
		(0x08, table.sym_var("map",     "MAP_DATA *")),
	]],
	[0x0A, "struct", "object_a_3", [
		(0x00, table.sym_var("map", "MAP_DATA *")),
		(0x04, table.sym_var("px",  "short")),
		(0x06, table.sym_var("pz",  "short")),
		(0x08, table.sym_var("ay",  "short")),
	]],
	[0x14, "struct", "object_a_4", [
		(0x00, table.sym_var("offset",  "s32")),
		(0x04, table.sym_var("scale",   "VECF")),
		(0x10, table.sym_var("vel",     "float")),
	]],
	[0x08, "struct", "object_a_5", [
		(0x00, table.sym_var("shape",   "u8")),
		(0x01, table.sym_var("px",      "s8")),
		(0x02, table.sym_var("pz",      "s8")),
		(0x03, table.sym_var("state",   "s8")),
		(0x04, table.sym_var("data",    "s8 *")),
	]],
	[0x08, "struct", "object_a_6", [
		(0x00, table.sym_var("index",   "u8")),
		(0x01, table.sym_var("flag",    "u8")),
		(0x02, table.sym_var("arg",     "u8")),
		(0x03, table.sym_var("shape",   "u8")),
		(0x04, table.sym_var("script",  "O_SCRIPT *")),
	]],
	[0x08, "struct", "object_a_7", [
		(0x00, table.sym_var("offset",  "short")),
		(0x02, table.sym_var("shape",   "s16")),
		(0x04, table.sym_var("map",     "MAP_DATA *")),
	]],
	[0x10, "struct", "object_a_8", [
		(0x00, table.sym_var("time",        "s32")),
		(0x04, table.sym_var("anime",       "s32")),
		(0x08, table.sym_var("vel",         "float")),
		(0x0C, table.sym_var("anime_vel",   "float")),
	]],
]

struct_wipe = [
	[0x03, "struct", "wipe_arg_fade", [
		(0x00, table.sym_var("r",       "u8")),
		(0x01, table.sym_var("g",       "u8")),
		(0x02, table.sym_var("b",       "u8")),
	]],
	[0x12, "struct", "wipe_arg_window", [
		(0x00, table.sym_var("r",       "u8")),
		(0x01, table.sym_var("g",       "u8")),
		(0x02, table.sym_var("b",       "u8")),
		(0x04, table.sym_var("s_size",  "s16")),
		(0x06, table.sym_var("e_size",  "s16")),
		(0x08, table.sym_var("s_x",     "s16")),
		(0x0A, table.sym_var("s_y",     "s16")),
		(0x0C, table.sym_var("e_x",     "s16")),
		(0x0E, table.sym_var("e_y",     "s16")),
		(0x10, table.sym_var("ang_vel", "short")),
	]],
	[0x04, "union", "wipe_arg", [
		(0x00, table.sym_var("fade",    "WIPE_ARG_FADE")),
		(0x00, table.sym_var("window",  "WIPE_ARG_WINDOW")),
	]],
	[0x16, "struct", "wipe", [
		(0x00, table.sym_var("active",  "u8")),
		(0x01, table.sym_var("type",    "u8")),
		(0x02, table.sym_var("frame",   "u8")),
		(0x03, table.sym_var("blank",   "u8")),
		(0x04, table.sym_var("arg",     "WIPE_ARG")),
	]],
]

struct_shadow = [
	[0x09, "struct", "shadow_rect", [
		(0x00, table.sym_var("sx",      "float")),
		(0x04, table.sym_var("sz",      "float")),
		(0x08, table.sym_var("y_scale", "s8")),
	]],
]

struct_back = [
	[0x10, "struct", "struct_803612C0", [
		(0x00, table.sym_var("_00", "u16")),
		(0x02, table.sym_var("_02", "s16")),
		(0x04, table.sym_var("_04", "s32")),
		(0x08, table.sym_var("_08", "s32")),
		(0x0C, table.sym_var("_0C", "s32")),
	]],
]

struct_scroll = [
	[0x24, "struct", "scroll", [
		(0x00, table.sym_var("index",   "int")),
		(0x04, table.sym_var("texture", "int")),
		(0x08, table.sym_var("len",     "int")),
		(0x0C, table.sym_var("data",    "s16 *")),
		(0x10, table.sym_var("start",   "Gfx *")),
		(0x14, table.sym_var("end",     "Gfx *")),
		(0x18, table.sym_var("draw",    "Gfx *")),
		(0x1C, table.sym_var("r",       "u8")),
		(0x1D, table.sym_var("g",       "u8")),
		(0x1E, table.sym_var("b",       "u8")),
		(0x1F, table.sym_var("a",       "u8")),
		(0x20, table.sym_var("layer",   "int")),
	]],
]

struct_wave = [
	[0x78, "struct", "wave", [
		(0x00, table.sym_var("_00", "s16")),
		(0x02, table.sym_var("_02", "s8")),
		(0x03, table.sym_var("_03", "s8")),
		(0x04, table.sym_var("_04", "s8")),
		(0x05, table.sym_var("_05", "s8")),
		(0x06, table.sym_var("_06", "s8")),
		(0x07, table.sym_var("_07", "s8")),
		# ...
	]],
]

struct_dprint = [
	[0x3C, "struct", "dprint", [
		(0x00, table.sym_var("x",   "s32")),
		(0x04, table.sym_var("y",   "s32")),
		(0x08, table.sym_var("len", "s16")),
		(0x0A, table.sym_var("str", "char", "[50]")),
	]],
]

struct_message = [
	[0x10, "struct", "message", [
		(0x00, table.sym_var("arg",     "s32")),
		(0x04, table.sym_var("line",    "s8")),
		(0x06, table.sym_var("x",       "s16")),
		(0x08, table.sym_var("y",       "s16")),
		(0x0C, table.sym_var("str",     "u8 *")),
	]],
]

struct_weather = [
]

struct_obj_data = [
	[0x08, "struct", "prg_obj", [
		(0x00, table.sym_var("script",  "O_SCRIPT *")),
		(0x04, table.sym_var("shape",   "s16")),
		(0x06, table.sym_var("arg",     "s16")),
	]],
	[0x08, "struct", "map_obj", [
		(0x00, table.sym_var("index",   "u8")),
		(0x01, table.sym_var("ext",     "u8")),
		(0x02, table.sym_var("code",    "u8")),
		(0x03, table.sym_var("shape",   "u8")),
		(0x04, table.sym_var("script",  "O_SCRIPT *")),
	]],
]

struct_hud = [
	[0x0E, "struct", "hud", [
		(0x00, table.sym_var("life",    "s16")),
		(0x02, table.sym_var("coin",    "s16")),
		(0x04, table.sym_var("star",    "s16")),
		(0x06, table.sym_var("power",   "s16")),
		(0x08, table.sym_var("key",     "s16")),
		(0x0A, table.sym_var("flag",    "s16")),
		(0x0C, table.sym_var("timer",   "u16")),
	]],
	[0x0C, "struct", "meter", [
		(0x00, table.sym_var("mode",    "s8")),
		(0x02, table.sym_var("x",       "s16")),
		(0x04, table.sym_var("y",       "s16")),
		(0x08, table.sym_var("scale",   "f32")),
	]],
]

struct_object_b = [
]

struct_object_c = [
	[0x0E, "struct", "object_c_0", [
		(0x00, table.sym_var("msg_start",   "s16")),
		(0x02, table.sym_var("msg_win",     "s16")),
		(0x04, table.sym_var("path",        "PATH_DATA *")),
		(0x08, table.sym_var("star",        "VECS")),
	]],
	[0x0B, "struct", "object_c_1", [
		(0x00, table.sym_var("scale",   "float")),
		(0x04, table.sym_var("se",      "NA_SE")),
		(0x08, table.sym_var("dist",    "short")),
		(0x0A, table.sym_var("damage",  "s8")),
	]],
	[0x0A, "struct", "object_c_2", [
		(0x00, table.sym_var("map",     "MAP_DATA *")),
		(0x04, table.sym_var("p_map",   "MAP_DATA *")),
		(0x08, table.sym_var("p_shape", "s16")),
	]],
	[0x06, "struct", "object_c_3", [
		(0x00, table.sym_var("map",     "MAP_DATA *")),
		(0x04, table.sym_var("shape",   "s16")),
	]],
	[0x0C, "struct", "object_c_4", [
		(0x00, table.sym_var("msg",     "s16")),
		(0x04, table.sym_var("radius",  "float")),
		(0x08, table.sym_var("height",  "float")),
	]],
	[0x0C, "struct", "object_c_5", [
		(0x00, table.sym_var("shape",   "int")),
		(0x04, table.sym_var("script",  "O_SCRIPT *")),
		(0x08, table.sym_var("scale",   "float")),
	]],
]

struct_math = [
	[0x08, "struct", "bspline", [
		(0x00, table.sym_var("time",    "s16")),
		(0x02, table.sym_var("pos",     "VECS")),
	]],
]

struct_shape = [
	[0x18, "struct", "anime", [
		(0x00, table.sym_var("flag",    "s16")),
		(0x02, table.sym_var("waist",   "short")),
		(0x04, table.sym_var("start",   "s16")),
		(0x06, table.sym_var("end",     "s16")),
		(0x08, table.sym_var("frame",   "s16")),
		(0x0A, table.sym_var("joint",   "s16")),
		(0x0C, table.sym_var("val",     "s16 *")),
		(0x10, table.sym_var("tbl",     "u16 *")),
		(0x14, table.sym_var("size",    "size_t")),
	]],
	[0x14, "struct", "skeleton", [
		(0x00, table.sym_var("index",       "s16")),
		(0x02, table.sym_var("waist",       "short")),
		(0x04, table.sym_var("anime",       "ANIME *")),
		(0x08, table.sym_var("frame",       "s16")),
		(0x0A, table.sym_var("timer",       "u16")),
		(0x0C, table.sym_var("frame_amt",   "s32")),
		(0x10, table.sym_var("frame_vel",   "s32")),
	]],
	[0x0C, "struct", "layer_list", [
		(0x00, table.sym_var("mtx",     "Mtx *")),
		(0x04, table.sym_var("gfx",     "Gfx *")),
		(0x08, table.sym_var("next",    "struct layer_list *")),
	]],
	[0x14, "struct", "shape", [
		(0x00, table.sym_var("type",    "s16")),
		(0x02, table.sym_var("flag",    "s16")),
		(0x04, table.sym_var("prev",    "struct shape *")),
		(0x08, table.sym_var("next",    "struct shape *")),
		(0x0C, table.sym_var("parent",  "struct shape *")),
		(0x10, table.sym_var("child",   "struct shape *")),
	]],
	[0x1C, "struct", "shape_callback", [
		(0x00, table.sym_var("s",   "SHAPE")),
		(0x14, table.sym_var_fnc("callback", val="void *", arg=(
			"int code",
			"SHAPE *shape",
			"void *data",
		))),
		(0x18, table.sym_var("arg", "int")),
	]],
	[0x18, "struct", "shape_gfx", [
		(0x00, table.sym_var("s",   "SHAPE")),
		(0x14, table.sym_var("gfx", "Gfx *")),
	]],
	[0x24, "struct", "shape_scene", [
		(0x00, table.sym_var("s",       "SHAPE")),
		(0x14, table.sym_var("index",   "u8")),
		(0x15, table.sym_var("_15",     "u8")),
		(0x16, table.sym_var("x",       "s16")),
		(0x18, table.sym_var("y",       "s16")),
		(0x1A, table.sym_var("w",       "s16")),
		(0x1C, table.sym_var("h",       "s16")),
		(0x1E, table.sym_var("len",     "u16")),
		(0x20, table.sym_var("table",   "SHAPE *")),
	]],
	[0x18, "struct", "shape_ortho", [
		(0x00, table.sym_var("s",       "SHAPE")),
		(0x14, table.sym_var("scale",   "float")),
	]],
	[0x24, "struct", "shape_persp", [
		(0x00, table.sym_var("s",       "SHAPE_CALLBACK")),
		(0x1C, table.sym_var("fovy",    "float")),
		(0x20, table.sym_var("near",    "short")),
		(0x22, table.sym_var("far",     "short")),
	]],
	[0x54, "struct", "shape_layer", [
		(0x00, table.sym_var("s",       "SHAPE")),
		(0x14, table.sym_var("list",    "LAYER_LIST *", "[LAYER_MAX]")),
		(0x34, table.sym_var("next",    "LAYER_LIST *", "[LAYER_MAX]")),
	]],
	[0x3C, "struct", "shape_camera", [
		(0x00, table.sym_var("s",       "SHAPE_CALLBACK")),
		(0x1C, table.sym_var("eye",     "VECF")),
		(0x28, table.sym_var("look",    "VECF")),
		(0x34, table.sym_var("mf",      "MTXF *")),
		(0x38, table.sym_var("rz_m",    "short")),
		(0x3A, table.sym_var("rz_p",    "short")),
	]],
	[0x18, "struct", "shape_lod", [
		(0x00, table.sym_var("s",   "SHAPE")),
		(0x14, table.sym_var("min", "short")),
		(0x16, table.sym_var("max", "short")),
	]],
	[0x20, "struct", "shape_select", [
		(0x00, table.sym_var("s",       "SHAPE_CALLBACK")),
		(0x1C, table.sym_var("arg",     "s16")),
		(0x1E, table.sym_var("index",   "s16")),
	]],
	[0x24, "struct", "shape_posang", [
		(0x00, table.sym_var("s",   "SHAPE_GFX")),
		(0x18, table.sym_var("pos", "VECS")),
		(0x1E, table.sym_var("ang", "VECS")),
	]],
	[0x1E, "struct", "shape_pos", [
		(0x00, table.sym_var("s",   "SHAPE_GFX")),
		(0x18, table.sym_var("pos", "VECS")),
	]],
	[0x1E, "struct", "shape_ang", [
		(0x00, table.sym_var("s",   "SHAPE_GFX")),
		(0x18, table.sym_var("ang", "VECS")),
	]],
	[0x1C, "struct", "shape_scale", [
		(0x00, table.sym_var("s",       "SHAPE_GFX")),
		(0x18, table.sym_var("scale",   "float")),
	]],
	[0x1E, "struct", "shape_billboard", [
		(0x00, table.sym_var("s",   "SHAPE_GFX")),
		(0x18, table.sym_var("pos", "VECS")),
	]],
	[0x1E, "struct", "shape_joint", [
		(0x00, table.sym_var("s",   "SHAPE_GFX")),
		(0x18, table.sym_var("pos", "VECS")),
	]],
	[0x18, "struct", "shape_shadow", [
		(0x00, table.sym_var("s",       "SHAPE")),
		(0x14, table.sym_var("size",    "short")),
		(0x16, table.sym_var("alpha",   "u8")),
		(0x17, table.sym_var("type",    "u8")),
	]],
	[0x20, "struct", "shape_back", [
		(0x00, table.sym_var("s",       "SHAPE_CALLBACK")),
		(0x1C, table.sym_var("arg",     "u32")),
	]],
	[0x60, "struct", "shape_object", [
		(0x00, table.sym_var("s",           "SHAPE")),
		(0x14, table.sym_var("shape",       "SHAPE *")),
		(0x18, table.sym_var("scene",       "s8")),
		(0x19, table.sym_var("group",       "s8")),
		(0x1A, table.sym_var("ang",         "VECS")),
		(0x20, table.sym_var("pos",         "VECF")),
		(0x2C, table.sym_var("scale",       "VECF")),
		(0x38, table.sym_var("skeleton",    "SKELETON")),
		(0x4C, table.sym_var("spawn",       "struct spawn *")),
		(0x50, table.sym_var("mf",          "MTXF *")),
		(0x54, table.sym_var("view",        "VECF")),
	]],
	[0x18, "struct", "shape_list", [
		(0x00, table.sym_var("s",       "SHAPE")),
		(0x14, table.sym_var("shape",   "SHAPE *")),
	]],
	[0x26, "struct", "shape_hand", [
		(0x00, table.sym_var("s",       "SHAPE_CALLBACK")),
		(0x1C, table.sym_var("object",  "SHAPE_OBJECT *")),
		(0x20, table.sym_var("pos",     "VECS")),
	]],
	[0x16, "struct", "shape_cull", [
		(0x00, table.sym_var("s",       "SHAPE")),
		(0x14, table.sym_var("dist",    "short")),
	]],
]

struct_map = [
	[0x30, "struct", "map_plane", [
		(0x00, table.sym_var("type",    "s16")),
		(0x02, table.sym_var("arg",     "s16")),
		(0x04, table.sym_var("flag",    "s8")),
		(0x05, table.sym_var("area",    "s8")),
		(0x06, table.sym_var("y_min",   "short")),
		(0x08, table.sym_var("y_max",   "short")),
		(0x0A, table.sym_var("v0",      "VECS")),
		(0x10, table.sym_var("v1",      "VECS")),
		(0x16, table.sym_var("v2",      "VECS")),
		(0x1C, table.sym_var("nx",      "float")),
		(0x20, table.sym_var("ny",      "float")),
		(0x24, table.sym_var("nz",      "float")),
		(0x28, table.sym_var("nw",      "float")),
		(0x2C, table.sym_var("obj",     "struct object *")),
	]],
	[0x08, "struct", "map_list", [
		(0x00, table.sym_var("next",    "struct map_list *")),
		(0x04, table.sym_var("plane",   "MAP_PLANE *")),
	]],
]

struct_file_select = [
]

struct_star_select = [
]

struct_Na = [
	[0x0C, "struct", "Na_bgmctl", [
		(0x00, table.sym_var("a_voice", "s16")),
		(0x02, table.sym_var("a_vol",   "s16")),
		(0x04, table.sym_var("a_time",  "s16")),
		(0x06, table.sym_var("b_voice", "s16")),
		(0x08, table.sym_var("b_vol",   "s16")),
		(0x0A, table.sym_var("b_time",  "s16")),
	]],
	[0x1C, "struct", "Na_cfg", [
		(0x00, table.sym_var("freq",    "u32")),
		(0x04, table.sym_var("voice",   "u8")),
		(0x05, table.sym_var("e_filt",  "u8")),
		(0x06, table.sym_var("e_size",  "u16")),
		(0x08, table.sym_var("e_vol",   "u16")),
		(0x0A, table.sym_var("vol",     "u16")),
		(0x0C, table.sym_var("_0C",     "size_t")),
		(0x10, table.sym_var("_10",     "size_t")),
		(0x14, table.sym_var("_14",     "size_t")),
		(0x18, table.sym_var("_18",     "size_t")),
	]],
]

struct_face = [
]
