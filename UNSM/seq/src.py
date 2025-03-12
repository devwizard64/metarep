import main
import ultra

import UNSM.c
from . import f_code, f_data, d_texture_n

staff = [
	[main.s_if, {"J0.code.data", "J3.code.data"}, [
		[main.f_str, "#ifdef JAPANESE\n"],
		[main.f_str, "#if REVISION >= 199609\n"],
		[main.s_if, "J3.code.data", [
			[ultra.c.f_data, "J3.code.data", 0x8030CE10, 0x8030CEF8, [
				[0, 20, 1, UNSM.c.d_staff_str],
			]],
		]],
		[main.f_str, "#else\n"],
		[main.s_if, "J0.code.data", [
			[ultra.c.f_data, "J0.code.data", 0x8032C790, 0x8032C868, [
				[0, 20, 1, UNSM.c.d_staff_str],
			]],
		]],
		[main.f_str, "#endif\n"],
		[main.f_str, "#endif\n\n"],
	]],
	[main.s_if, "E0.code.data", [
		[main.f_str, "#ifdef ENGLISH\n"],
		[ultra.c.f_data, "E0.code.data", 0x8032D6D0, 0x8032D7CC, [
			[0, 20, 1, UNSM.c.d_staff_str],
		]],
		[main.f_str, "#endif\n\n"],
	]],
	[main.s_if, "P0.code.data", [
		[main.f_str, "#ifdef MULTILANG\n"],
		[ultra.c.f_data, "P0.code.data", 0x802F9880, 0x802F999C, [
			[0, 20, 1, UNSM.c.d_staff_str],
		]],
		[main.f_str, "#endif\n\n"],
	]],
	[main.s_if, "C3.code.data", [
		# [main.f_str, "#ifdef CHINESE\n"],
		# [ultra.c.f_data, "C3.code.data", 0x8030F370, 0x8030F460, [
		# 	[0, 20, 1, UNSM.c.d_staff_str],
		# ]],
		# [main.f_str, "#endif\n"],
	]],
]

tagobj = [
	[main.f_str, "#define TAGOBJ_NULL {obj_coin, S_COIN, 0}\n\n"],
	[ultra.c.f_data, "E0.code.data", 0x803317E0, 0x80332350, [
		[0, -366, 1, UNSM.c.d_tagobj, 0x803317E0],
	]],
]

mapobj = [
	[ultra.c.f_data, "E0.code.data", 0x80332350, 0x803325E8, [
		[0,  -83, 1, UNSM.c.d_mapobj],
	]],
]

mathtbl = [
	[main.f_str, ".data\n\n"],
	[ultra.asm.f_data, "E0.ulib.data", 0x80386000, 0x8038B802, 0, [
		[0x1400, 1, ultra.asm.d_float],
		[  0x80, 8, ultra.asm.d_uhalf, "0x%04X"],
		[     1, 1, ultra.asm.d_uhalf, "0x%04X"],
	]],
]

audio_work = [
	[main.f_str, "#include \"Na_internal.h\"\n\n"],
	[ultra.c.f_bss, "E0.code.data", 0x80220DA0, 0x80226CD0],
]

seq = [
	[main.s_file, "src/staff.c", staff],
	[main.s_file, "src/tagobj.c", tagobj],
	[main.s_file, "src/mapobj.c", mapobj],
	[main.s_file, "src/mathtbl.s", mathtbl],
	[main.s_file, "src/audio/work.c", audio_work],
]

struct_enemyc = [
	[0x0E, "struct", "enemyc0", None, [
		(0x00, main.sym_var("msg_start", "s16")),
		(0x02, main.sym_var("msg_win", "s16")),
		(0x04, main.sym_var("path", "PATH *")),
		(0x08, main.sym_var("star", "SVEC")),
	]],
	[0x0B, "struct", "enemyc1", None, [
		(0x00, main.sym_var("scale", "float")),
		(0x04, main.sym_var("se", "Na_Se")),
		(0x08, main.sym_var("dist", "short")),
		(0x0A, main.sym_var("damage", "s8")),
	]],
	[0x0A, "struct", "enemyc2", None, [
		(0x00, main.sym_var("map", "MAP *")),
		(0x04, main.sym_var("p_map", "MAP *")),
		(0x08, main.sym_var("p_shape", "s16")),
	]],
	[0x06, "struct", "enemyc3", None, [
		(0x00, main.sym_var("map", "MAP *")),
		(0x04, main.sym_var("shape", "s16")),
	]],
	[0x0C, "struct", "enemyc4", None, [
		(0x00, main.sym_var("msg", "s16")),
		(0x04, main.sym_var("radius", "float")),
		(0x08, main.sym_var("height", "float")),
	]],
	[0x0C, "struct", "enemyc5", None, [
		(0x00, main.sym_var("shape", "int")),
		(0x04, main.sym_var("script", "OBJLANG *")),
		(0x08, main.sym_var("scale", "float")),
	]],
]

seq_tmp = [
	f_code("E0.code.text", 0x8027F590, 0x8029C764, "src/E0/camera.s"),
	f_data("E0.code.data", 0x8032DF20, 0x8032FEB4, 0x803370F0, 0x80337794, 0x8033C520, 0x8033CBD4, "src/E0/camera.data.c", """#include <sm64.h>

#define CAM_WINDEMO(x1, x2, x3, x4, x5, x6, x7) \\
{ \\
	((x1) & 15) | ((x2) & 15) << 4, \\
	((x3) & 15) | ((x4) & 15) << 4, \\
	((x5) & 15) | ((x6) & 15) << 4, \\
	((x7) & 15), \\
}

#define CAM_PAUSE(a1, a2, a3, a4, b1, b2, b3, b4) \\
( \\
	((a1) & 1) << 0 | ((a2) & 1) << 1 | \\
	((a3) & 1) << 2 | ((a4) & 1) << 3 | \\
	((b1) & 1) << 4 | ((b2) & 1) << 5 | \\
	((b3) & 1) << 6 | ((b4) & 1) << 7 \\
)
""", [
		[0,    1, 1, ultra.c.d_s32],
		[0,    1, 1, ultra.c.d_addr, 0],
		[0,    2, 1, ultra.c.d_s32],
		[0,    1, 1, ultra.c.d_addr, 0],
		[0,    1, 1, ultra.c.d_s16, "0x%04X"], [0, 1, 2, None],
		[0,    2, 1, ultra.c.d_s32],
		[0,    4, 1, ultra.c.d_f32],
		[0,    4, ultra.c.d_align_u8],
		[0,    2, 1, ultra.c.d_addr, ultra.A_ADDR|ultra.A_ARRAY, 0x8033C520, 0x24],
		[0,    1, 1, ultra.c.d_s32],
		[1,    5, 3, ultra.c.d_f32],
		[0,  -18, 1, ultra.c.d_addr, 0],
		[1,    2, 3, ultra.c.d_f32],
		[1,    1, 7, ultra.c.d_u16], [0, 1, 2, None],
		[1,    1, 5, ultra.c.d_u8], [0, 1, 3, None],
		[0,   -4, 1, UNSM.c.d_campos],
		[0, -130, 1, UNSM.c.d_camctl],
		[0,  -40, 1, ultra.c.d_addr, 0],
		[0, -148, 1, UNSM.c.d_campath],
		[1,    3, 3, ultra.c.d_f32],
		[0,  -88, 1, UNSM.c.d_campath],
		[0, -102, 1, UNSM.c.d_camdemo],
		[0, -27, 1, UNSM.c.d_camera_windemo],
		[0, -19, 1, UNSM.c.d_camera_pause],
		[0, 1, 1, None],
		[0, -198, 1, UNSM.c.d_campath],
	], [
		[0,  -10, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    2, 1, ultra.c.d_f32],
		[0,  -10, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   52, 1, ultra.c.d_f32],
		[0,  -17, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    4, 1, ultra.c.d_f32],
		[0,  -29, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    9, 1, ultra.c.d_f32],
		[0,   -6, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    8, 1, ultra.c.d_f32],
		[0,  -11, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   54, 1, ultra.c.d_f32],
		[0, -129, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    9, 1, ultra.c.d_f32],
		[0,  -65, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    5, 1, ultra.c.d_f32],
		[0,   -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),

	f_code("E0.code.text", 0x802E3E50, 0x802F972C, "src/E0/enemyb.s", ".set fp=32\n"),
	[main.s_file, "src/E0/enemyb.data.c", [
		[main.f_str, "#include <sm64.h>\n\n"],
		[ultra.c.f_data, "E0.code.data", 0x803383D0, 0x803389A4, [
			[0,  21, 1, ultra.c.d_f64],
			[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
			[0,   2, 1, ultra.c.d_f64],
			[0,   1, 1, ultra.c.d_f32],
			[0, -10, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,  18, 1, ultra.c.d_f32], [0, 1, 4, None],
			[0,   2, 1, ultra.c.d_f64],
			[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN], [0, 1, 4, None],
			[0,   1, 1, ultra.c.d_f64],
			[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
			[0,   6, 1, ultra.c.d_f64],
			[0,  11, 1, ultra.c.d_f32],
			[0,  -6, 1, ultra.c.d_addr, ultra.A_EXTERN], [0, 1, 4, None],
			[0,   5, 1, ultra.c.d_f64],
			[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
			[0,   3, 1, ultra.c.d_f64],
			[0,  15, 1, ultra.c.d_f32],
			[0, -16, 1, ultra.c.d_addr, ultra.A_EXTERN], [0, 1, 4, None],
			[0,   1, 1, ultra.c.d_f64],
			[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,  10, 1, ultra.c.d_f32], [0, 1, 4, None],
			[0,   3, 1, ultra.c.d_f64],
			[0,   4, 1, ultra.c.d_f32],
			[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   6, 1, ultra.c.d_f32],
			[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   4, 1, ultra.c.d_f32],
			[0,   1, 1, ultra.c.d_f64],
			[0, -36, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   3, 1, ultra.c.d_f32], [0, 1, 4, None],
			[0,   2, 1, ultra.c.d_f64],
			[0,  11, 1, ultra.c.d_f32], [0, 1, 4, None],
			[0,   3, 1, ultra.c.d_f64],
			[0,  -7, 1, ultra.c.d_addr, ultra.A_EXTERN], [0, 1, 4, None],
			[0,  20, 1, ultra.c.d_f64],
			[0,   3, 1, ultra.c.d_f32], [0, 1, 4, None],
			[0,   2, 1, ultra.c.d_f64],
			[0,   8, 1, ultra.c.d_f32],
			[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   3, 1, ultra.c.d_f32],
			[0,   1, 1, ultra.c.d_f64],
			[0,   4, 1, ultra.c.d_f32],
			[0, -11, 1, ultra.c.d_addr, ultra.A_EXTERN],
		]],
		[main.f_str, "\n"],
		[ultra.c.f_bss, "E0.code.data", 0x80361450, 0x80361454],
		[main.f_str, "\n"],
		[ultra.c.f_data, "E0.code.data", 0x80332610, 0x8033283C, [
			[0, 1, ultra.c.d_align_s8],
			[0, 1, ultra.c.d_align_s16],
			[0, 3, ultra.c.d_align_s8],
			[0, 10, 1, UNSM.c.d_hitinfo],
			[0, 2, 1, UNSM.c.d_path_data],
			[0, 4, 1, UNSM.c.d_hitinfo],
			[0, 1, ultra.c.d_align_s8],
			[0, 1, 1, UNSM.c.d_hitinfo],
			[0, 1, 1, UNSM.c.d_path_data],
			[0, 3, 1, UNSM.c.d_hitinfo],
			[1, -4, 2, ultra.c.d_s16],
		]],
	]],

	f_code("E0.code.text", 0x802F9730, 0x80314A2C, "src/E0/enemyc.s"),
	[main.s_file, "src/E0/enemyc.data.c", [
		[main.f_str, "#include <sm64.h>\n\n"],
		[ultra.c.f_data, "E0.code.data", 0x803389B0, 0x80338D94, [
			[0,   2, 1, ultra.c.d_f32],
			[0,  -9, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,  21, 1, ultra.c.d_f32],
			[0,  -7, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,  22, 1, ultra.c.d_f32],
			[0,  -6, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   4, 1, ultra.c.d_f32],
			[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,  23, 1, ultra.c.d_f32],
			[0,  -8, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   4, 1, ultra.c.d_f32],
			[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,  18, 1, ultra.c.d_f32],
			[0,  -8, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   8, 1, ultra.c.d_f32],
			[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   7, 1, ultra.c.d_f32],
			[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,  12, 1, ultra.c.d_f32],
			[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   4, 1, ultra.c.d_f32],
			[0, -15, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   6, 1, ultra.c.d_f32],
			[0,  -8, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   8, 1, ultra.c.d_f32],
			[0,  -6, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,  18, 1, ultra.c.d_f32],
		]],
		[main.f_str, "\n"],
		[ultra.c.f_struct, struct_enemyc],
		[main.f_str, "\n"],
		[ultra.c.f_bss, "E0.code.data", 0x80361460, 0x8036148C],
		[main.f_str, "\n"],
		[ultra.c.f_data, "E0.code.data", 0x80332840, 0x80332E4C, [
			[0,   1, 1, UNSM.c.d_hitinfo],
			[1,   1, 6, ultra.c.d_u8], [0, 1, 2, None], # template
			[1,   1, 6, ultra.c.d_u8], [0, 1, 2, None], # template
			[0,  -2, 1, UNSM.c.d_enemyc0],
			[0,   1, 1, UNSM.c.d_hitinfo],
			[1,   1, 6, ultra.c.d_u8], [0, 1, 2, None], # template
			[0,   2, 1, UNSM.c.d_hitinfo],
			[1,   1, 3, ultra.c.d_s16], [0, 1, 2, None],
			[0,   1, 1, UNSM.c.d_hitinfo],
			[0,  -3, 1, UNSM.c.d_enemyc1],
			[1,  -2, 6, ultra.c.d_u8], # template
			[0,   3, 1, UNSM.c.d_hitinfo],
			[1,   1, 6, ultra.c.d_u8], [0, 1, 2, None], # template
			[1,   1, 4, ultra.c.d_f32],
			[1,   1, 3, ultra.c.d_s32, UNSM.fmt.fmt_msg],
			[0,   1, 1, UNSM.c.d_hitinfo],
			[1,   1, 6, ultra.c.d_u8], [0, 1, 2, None], # template
			[0,   1, 1, UNSM.c.d_hitinfo],
			[1,   1, 6, ultra.c.d_s8], [0, 1, 2, None],
			[0,   1, 1, UNSM.c.d_particle],
			[0,   2, 1, UNSM.c.d_hitinfo],
			[0,   1, 1, UNSM.c.d_particle],
			[0, -21, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,  -2, 1, UNSM.c.d_enemyc2],
			[0,   1, 1, UNSM.c.d_hitinfo],
			[0,   2, 1, UNSM.c.d_particle],
			[0,  -2, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[1,   1, 4, ultra.c.d_u8],
			[1,   1, 4, ultra.c.d_f32],
			[0,  -2, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[1,   2, 4, ultra.c.d_s16],
			[1,   1, 4, ultra.c.d_s8],
			[0,  -2, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[1,   1, 2, ultra.c.d_s8], [0, 1, 2, None],
			[1,   1, 2, ultra.c.d_s16],
			[0,  -2, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[1,  -4, 2, UNSM.c.d_80332AC0],
			[1,   1, 4, ultra.c.d_s8],
			[1,   1, 2, ultra.c.d_s16],
			[1,  -2, 4, ultra.c.d_s16],
			[1,   1, 4, ultra.c.d_s16],
			[0,   1, 1, UNSM.c.d_hitinfo],
			[0,   1, 1, UNSM.c.d_particle],
			[0,   1, 1, UNSM.c.d_hitinfo],
			[0, -10, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[1,   1, 4, ultra.c.d_s16],
			[1,  -3, [
				[0, -5, 1, UNSM.c.d_enemyc3],
			]],
			[1,   1, 3, ultra.c.d_s16], [0, 1, 2, None],
			[0,  -3, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   5, 1, UNSM.c.d_hitinfo],
			[1,  -3, 2, ultra.c.d_s16],
			[0,   2, 1, UNSM.c.d_hitinfo],
			[1,   1, 2, ultra.c.d_f32, "%g"],
			[0,   4, 1, UNSM.c.d_hitinfo],
			[1,   1, 6, ultra.c.d_s8], [0, 1, 2, None],
			[0,   1, 1, UNSM.c.d_hitinfo],
			[1,  -3, 3, ultra.c.d_f32],
			[1,   1, 6, ultra.c.d_u8], [0, 1, 2, None], # template
			[0,  -2, 1, UNSM.c.d_enemyc4],
			[1,  -6, 2, ultra.c.d_s16],
			[0,   2, 1, UNSM.c.d_hitinfo],
			[1,  -4, 2, ultra.c.d_s16],
			[1, -31, 3, ultra.c.d_s16], [0, 1, 2, None],
			[0,   1, 1, UNSM.c.d_hitinfo],
			[0,  -2, 1, UNSM.c.d_enemyc5],
			[0,   1, 1, UNSM.c.d_hitinfo],
		]],
	]],
]

seq_audio_tmp = [
	f_code("E0.code.text", 0x80314A30, 0x80316E78, "src/audio/101/driver.s"),
	f_data("E0.code.data", 0x80332E50, 0x80332E50, 0x80338DA0, 0x80338DB4, 0, 0, "src/audio/101/driver.data.c", "#include \"../Na_internal.h\"\n", [], [
		[0, 5, 1, ultra.c.d_f32],
	]),
	f_code("E0.code.text", 0x80316E80, 0x80318034, "src/audio/101/memory.s"),
	f_data("E0.code.data", 0x80332E50, 0x80332E50, 0x80338DC0, 0x80338E08, 0, 0, "src/audio/101/memory.data.c", "#include \"../Na_internal.h\"\n", [], [
		[0, -16, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   2, 1, ultra.c.d_f32],
	]),
	f_code("E0.code.text", 0x80318040, 0x80319914, "src/audio/101/system.s"),
	f_code("E0.code.text", 0x80319920, 0x8031AEDC, "src/audio/101/voice.s"),
	f_data("E0.code.data", 0x80332E50, 0x80332E50, 0x80338E10, 0x80338E28, 0, 0, "src/audio/101/voice.data.c", "#include \"../Na_internal.h\"\n", [], [
		[0, 6, 1, ultra.c.d_f32],
	]),
	f_code("E0.code.text", 0x8031AEE0, 0x8031B82C, "src/audio/101/effect.s"),
	f_data("E0.code.data", 0x80332E50, 0x80332E50, 0x80338E30, 0x80338E54, 0, 0, "src/audio/101/effect.data.c", "#include \"../Na_internal.h\"\n", [], [
		[0, -9, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	f_code("E0.code.text", 0x8031B830, 0x8031E4E4, "src/audio/101/sequence.s"),
	f_data("E0.code.data", 0x80332E50, 0x80332E50, 0x80338E60, 0x803394E4, 0, 0, "src/audio/101/sequence.data.c", "#include \"../Na_internal.h\"\n", [], [
		[0, -417, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	f_code("E0.code.text", 0x8031E4F0, 0x80322364, "src/audio/101/game.s", ".set fp=32\n"),
	f_data("E0.code.data", 0x80332E50, 0x803332A0, 0x803394F0, 0x803397AC, 0x80361490, 0x80364BA0, "src/audio/101/game.data.c", """
#include "../Na_internal.h"

#define BGMCTL_GE_X     0
#define BGMCTL_GE_Y     1
#define BGMCTL_GE_Z     2
#define BGMCTL_LT_X     3
#define BGMCTL_LT_Y     4
#define BGMCTL_LT_Z     5
#define BGMCTL_SCENE    6
#define BGMCTL_AREA     7

#define BGMCTL(x)       (0x8000 >> BGMCTL_##x)
""", [ # wrong bss end
		[0, 2, 1, ultra.c.d_s32],
		[0, -17, 10, ultra.c.d_s8, "%2d"],
		[0, 1, 2, None],
		[0, -11, 1, ultra.c.d_u32, UNSM.fmt.fmt_na_se],
		[0, 1, 4*4, None],
		[0, 2, ultra.c.d_align_u8],
		[0, 1, 1, UNSM.c.d_Na_bgmctl, 6],
		[0, 1, 1, UNSM.c.d_Na_bgmctl, 12],
		[0, 1, 1, UNSM.c.d_Na_bgmctl, 12],
		[0, 1, 1, UNSM.c.d_Na_bgmctl, 2],
		[0, 1, 1, UNSM.c.d_Na_bgmctl, 7],
		[0, 1, 1, UNSM.c.d_Na_bgmctl, 8],
		[0, 1, 1, UNSM.c.d_Na_bgmctl, 7],
		[0, 1, 1, UNSM.c.d_Na_bgmctl, 2],
		[0, 2, ultra.c.d_align_s8],
		[0, -39, 1, ultra.c.d_addr, 0],
		[0, -8, 1, UNSM.c.d_Na_bgmctl_data],
		[1, -39, 3, ultra.c.d_u8, "0x%02X"],
		[0, 1, 3, None],
		[0, -39, 1, ultra.c.d_u16], # ? - doesnt seem like d
		[0, 1, 2, None],
		[0, -34, 1, ultra.c.d_u8],
		[0, 1, 2, None],
		[0, 2, ultra.c.d_align_s8],
		[0, 4, [
			[1, 1, 10, ultra.c.d_u8],
			[0, 1, 2, None],
		]],
		[1, 1, 10, ultra.c.d_u8, "0x%02X"],
		[0, 1, 2, None],
		[1, 2, 3, ultra.c.d_f32],
		[1, 1, 10, ultra.c.d_u8],
		[0, 1, 2, None],
		[0, 3, ultra.c.d_align_u8],
		[0, 1, ultra.c.d_align_u16],
		[0, 1, ultra.c.d_align_u8],
		[0, 1, ultra.c.d_align_u16],
		[0, 5, ultra.c.d_align_u8],
		[0, -4, 4, ultra.c.d_u32, "0x%08X"],
		[1, 2, 16, ultra.c.d_s8],
	], [
		[0, 34, 4, "asciz"],
		[0, 1,  4, None],
		[0,   2, 1, ultra.c.d_f64],
		[0,   7, 1, ultra.c.d_f32],
		[0, -28, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	f_data("E0.code.data", 0x803332A0, 0x8033500C, 0x803397B0, 0x803397B0, 0, 0, "src/audio/101/data.c", "#include \"../Na_internal.h\"\n", [
		[0, -18, 1, UNSM.c.d_Na_cfg],
		[0, -128//8, 8, ultra.c.d_u16, "0x%04X"],
		[0, -252//4, 4, ultra.c.d_f32, "%f"],
		[0,      -1, 3, ultra.c.d_f32, "%f"],
		[0, -128//4, 4, ultra.c.d_f32, "%f"],
		[1,  1, 16, ultra.c.d_u8],
		[1,  1, 16, ultra.c.d_u8],
		[1,  1, 16, ultra.c.d_s8],
		[1,  1, 6, ultra.c.d_s16],
		[0, -4*64//8, 8, ultra.c.d_s16, "%6d"],
		[0, -4, 1, ultra.c.d_addr, 0],
		[1,  1, 10, ultra.c.d_u16],
		[0, -3*128//4, 4, ultra.c.d_f32, "%f"],
		[0, 3, [
			[0, -128//4, 4, ultra.c.d_f32, "%.3f"],
			[0, -128//4, 4, ultra.c.d_f32, "%f"],
		]],
		[0,  1, ultra.c.d_align_s16],
		[0,  1, ultra.c.d_align_s8],
		[0,  2, 1, ultra.c.d_u32, "0x%X"],
		[0,  1, 1, ultra.c.d_s32],
		[0,  1, ultra.c.d_align_s8],
	], []),
]

seq_face_tmp = [
	f_code("E0.menu.text", 0x80178280, 0x8017BDE4, "src/face/draw.text.s", ".set fp=32\n"),
	f_data("E0.menu.data", 0x801A8200, 0x801A833C, 0x801B5610, 0x801B5914, 0x801B9CC0, 0x801B9F24, "src/face/draw.data.c", "#include \"face.h\"\n", [
		[1, 10, 3, ultra.c.d_f32],
		[1, -1, 3, ultra.c.d_f32],
		[0, 1, 1, ultra.c.d_addr, ultra.A_ADDR],
		[0, 2, 1, ultra.c.d_addr, 0],
		[0, 1, 1, ultra.c.d_s32],
		[0, -7, 1, ultra.c.d_addr, ultra.A_ADDR],
		[1, -8, 4, ultra.c.d_f32],
		[0, 3, 1, ultra.c.d_s32],
	], [
		[0, 40, 4, "asciz"],
		[0,   2, 1, ultra.c.d_f64],
		[0, -12, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   4, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32],
	]),
	f_code("E0.menu.text", 0x8017BDF0, 0x80181718, "src/face/object.text.s", ".set fp=32\n"),
	f_data("E0.menu.data", 0x801A8340, 0x801A8358, 0x801B5920, 0x801B5ED8, 0x801B9F30, 0x801BA024, "src/face/object.data.c", "#include \"face.h\"\n", [
		[1, 1, 1, ultra.c.d_s32],
		[0, 3, 4, None],
		[0, 2, 1, ultra.c.d_f32],
	], [
		[0, 82, 4, "asciz"],
		[0,   6, 1, ultra.c.d_f32],
		[0, -64, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   2, 1, ultra.c.d_f32],
		[0,   1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32],
		[0, -32, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 4, None],
		[0,   5, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32],
		[0, -11, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   2, 1, ultra.c.d_f64],
	]),
	f_code("E0.menu.text", 0x80181720, 0x80181D38, "src/face/skin.text.s", ".set fp=32\n"),
	f_data("E0.menu.data", 0x801A8360, 0x801A8360, 0x801B5EE0, 0x801B5F38, 0x801BA030, 0x801BA07C, "src/face/skin.data.c", "#include \"face.h\"\n", [], [
		[0, 2, 4, "asciz"],
	]),
	f_code("E0.menu.text", 0x80181D40, 0x80183A48, "src/face/particle.text.s", ".set fp=32\n"),
	f_data("E0.menu.data", 0x801A8360, 0x801A83DC, 0x801B5F40, 0x801B5FD8, 0x801BA080, 0x801BA084, "src/face/particle.data.c", "#include \"face.h\"\n", [
		[0, 1, 1, ultra.c.d_s32],
		[0, -6, 4, ultra.c.d_s32],
		[0, -1, 1, ultra.c.d_s32],
		[0, -1, 4, ultra.c.d_s32],
		[0, -1, 1, ultra.c.d_s32],
	], [
		[0, 6, 4, "asciz"],
		[0, 4, 1, ultra.c.d_f64],
		[0, 1, 1, ultra.c.d_f32],
		[0, 1, 4, None],
		[0, 4, 1, ultra.c.d_f64],
	]),
	f_code("E0.menu.text", 0x80183A50, 0x8018B830, "src/face/dynlist.text.s", ".set fp=32\n"),
	f_data("E0.menu.data", 0x801A83E0, 0x801A8404, 0x801B5FE0, 0x801B812C, 0x801BA090, 0x801BA1F8, "src/face/dynlist.data.c", "#include \"face.h\"\n", [
		[0, 2, 1, ultra.c.d_addr, 0],
		[1, 1, 6, ultra.c.d_f32],
		[0, 1, 1, ultra.c.d_s32],
	], [
		[0, 241, 4, "asciz"],
		[0, -75, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 1, ultra.c.d_f32],
		[0, -73, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	f_code("E0.menu.text", 0x8018B830, 0x8018C2F0, "src/face/gadget.text.s", ".set fp=32\n"),
	f_data("E0.menu.data", 0x801A8410, 0x801A8410, 0x801B8130, 0x801B82F0, 0x801BA200, 0x801BA320, "src/face/gadget.data.c", "#include \"face.h\"\n", [], [
		[0, 13, 4, "asciz"],
		[0, 1, 4, None],
		[0, 2, 1, ultra.c.d_f64],
	]),
	f_code("E0.menu.text", 0x8018C2F0, 0x8018E660, "src/face/stdio.text.s", ".set fp=32\n"),
	f_data("E0.menu.data", 0x801A8410, 0x801A8454, 0x801B82F0, 0x801B85B0, 0x801BA320, 0x801BAAF0, "src/face/stdio.data.c", "#include \"face.h\"\n", [
		[0, 1, 1, ultra.c.d_s32],
		[0, -7, 1, ultra.c.d_s32],
		[0, 1, 1, ultra.c.d_s32],
		[0, 2, 1, ultra.c.d_u32, "0x%08X"],
		[0, 1, 4, "asciz"],
		[0, 1, 1, ultra.c.d_s32],
	], [
		[0, 34, 4, "asciz"],
		[0, -22, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
	]),
	f_code("E0.menu.text", 0x8018E660, 0x80192050, "src/face/joint.text.s", ".set fp=32\n"),
	f_data("E0.menu.data", 0x801A8460, 0x801A8468, 0x801B85B0, 0x801B8730, 0x801BAAF0, 0x801BAC7C, "src/face/joint.data.c", "#include \"face.h\"\n", [
		[0, 1, 1, ultra.c.d_s32],
		[0, 1, 1, ultra.c.d_addr, 0],
	], [
		[0, 15, 4, "asciz"],
		[0, 1, 4, None],
		[0, 6, 1, ultra.c.d_f64],
		[0, 2, 1, ultra.c.d_f32],
		[0, 8, 1, ultra.c.d_f64],
	]),
	f_code("E0.menu.text", 0x80192050, 0x80193C70, "src/face/net.text.s", ".set fp=32\n"),
	f_data("E0.menu.data", 0x801A8470, 0x801A8470, 0x801B8730, 0x801B8964, 0x801BAC80, 0x801BAC8C, "src/face/net.data.c", "#include \"face.h\"\n", [], [
		[0, 38, 4, "asciz"],
		[0,  3, 1, ultra.c.d_f64],
		[0, -7, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	f_code("E0.menu.text", 0x80193C70, 0x801973C0, "src/face/math.text.s", ".set fp=32\n"),
	f_data("E0.menu.data", 0x801A8470, 0x801A8470, 0x801B8970, 0x801B8A60, 0, 0, "src/face/math.data.c", "#include \"face.h\"\n", [], [
		[0, 12, 4, "asciz"],
		[0, 5, 1, ultra.c.d_f32],
		[0, 4, 1, ultra.c.d_f64],
	]),
	f_code("E0.menu.text", 0x801973C0, 0x8019B060, "src/face/shape.text.s", ".set fp=32\n"),
	f_data("E0.menu.data", 0x801A8470, 0x801A8800, 0x801B8A60, 0x801B8E28, 0x801BAC90, 0x801BAFF0, "src/face/shape.data.c", "#include \"face.h\"\n", [
		[0, 7, 1, ultra.c.d_addr, 0],
		[0, -1, 1, UNSM.c.d_face_srt],
		[0, 1, 1, UNSM.c.d_face_dyndata],
		[0, -1, 1, UNSM.c.d_face_srt],
		[0, 1, 1, UNSM.c.d_face_dyndata],
		[0, -1, 1, UNSM.c.d_face_srt],
		[0, 1, 1, UNSM.c.d_face_dyndata],
		[0, 38, 1, ultra.c.d_addr, 0],
		[0, -24, 1, UNSM.c.d_face_dynlist, 0],
		[0, 1, 4, None],
		[0, 1, 1, ultra.c.d_f64],
	], [
		[0, 61, 4, "asciz"],
		[0, -8, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  5, 1, ultra.c.d_f32],
	]),
	f_code("E0.menu.text", 0x8019B060, 0x801A7830, "src/face/gfx.text.s", ".set fp=32\n"),
	f_data("E0.menu.data", 0x801A8800, 0x801B54B8, 0x801B8E30, 0x801B99E0, 0x801BAFF0, 0x801BEBB8, "src/face/gfx.data.c", "#include \"face.h\"\n", [
		[0, 5, 1, ultra.c.d_s32],
		[0, 5, 1, ultra.c.d_f32],
		[0, 1, 1, ultra.c.d_u32],
		[0, 2, 1, ultra.c.d_s32],
		[0, 3, 1, ultra.c.d_addr, 0],
		[0, 2, 1, ultra.c.d_s32],
		[0, 1, 1, ultra.c.d_addr, 0],
		[0, 4, 1, ultra.c.d_s32],
		[1, 1, 3, ultra.c.d_f32],
		[0, 5, 1, ultra.c.d_addr, 0],
		[0, 1, 1, ultra.c.d_u32],
		[0, 2, 1, ultra.c.d_s32],
		[0, 2, 1, ultra.c.d_addr, 0],
		[0, 1, 1, ultra.c.d_u32],
		[0, -4, 1, UNSM.c.d_face_bank],
		[0, 1, 4, None],
		[0, 1, 1, ultra.c.d_Gfx_cmd],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "hand.0"],
		[0, 1, 1, ultra.c.d_Gfx_cmd],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "hand.1"],
		d_texture_n("rgba16", 32, 32, 8, "red_star.%d"),
		d_texture_n("rgba16", 32, 32, 8, "silver_star.%d"),
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, UNSM.c.d_Mtx],
		[0, 1, 1, ultra.c.d_Gfx, 0x801B1B48],
		[0, -32, 1, ultra.c.d_addr, 0],
		d_texture_n("rgba16", 32, 32, 6, "spark.%d"),
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, ultra.c.d_Gfx, 0x801B4E28],
		[0, -24, 1, ultra.c.d_addr, 0],
		[0, 1, 1, ultra.c.d_Gfx_cmd],
		[0, 1, 1, UNSM.c.d_texture, "ia8", 32, 32, "phong"],
		[0, 1, 1, ultra.c.d_Gfx, 0x801B5398],
		[0, 1, 1, ultra.c.d_s32],
		[0, 1, 1, ultra.c.d_f32],
		[0, 1, 1, ultra.c.d_s32],
		[0, 1, 4, None],
		[0, 1, 1, ultra.c.d_Gfx, 0x801B53B8],
		[0, -6, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, ultra.c.d_Gfx, 0x801B54B8],
	], [
		[0, 168, 4, "asciz"],
		[0,   1, 1, ultra.c.d_f64],
		[0, -34, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  16, 1, ultra.c.d_f64],
		[0, -19, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
	]),
]
