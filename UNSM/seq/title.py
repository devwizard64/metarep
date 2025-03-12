import main
import ultra

import UNSM.asm
import UNSM.c
from . import d_texture_n

title_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x14000000, 0x1400007C],
	[main.f_str, "#if REVISION != 199605\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x1400007C, 0x14000094],
	[main.f_str, "#endif\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x14000094, 0x140000AC],
	[main.f_str, "#if REVISION == 199605\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x140001AC, 0x140001C8],
	[main.f_str, "#endif\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x140000AC, 0x140000C0],
	[main.f_str, "#if REVISION != 199605\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x140000C0, 0x140000C8],
	[main.f_str, "#endif\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x140000C8, 0x14000108],
	[main.f_str, "#if REVISION != 199605\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x14000108, 0x14000120],
	[main.f_str, "#endif\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x14000120, 0x14000138],
	[main.f_str, "#if REVISION == 199605\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x140001AC, 0x140001C8],
	[main.f_str, "#endif\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x14000138, 0x1400014C],
	[main.f_str, "#if REVISION != 199605\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x1400014C, 0x14000154],
	[main.f_str, "#endif\n"],
	[UNSM.asm.f_seqlang, "E0.Title", 0x14000154, 0x140002D0],
]

title_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802764B0, 0x8027657C],
	[ultra.c.f_extern, "E0.menu.text", 0x8016F670, 0x80170280],
	[ultra.c.f_extern, "E0.Title.Logo", 0x07000000, 0x0700C940],
	[ultra.c.f_data, "E0.Title", 0x140002D0, 0x14000414, [
		[0, 1, 1, UNSM.c.d_shplang, 0x14000414],
	]],
	[ultra.c.f_extern, "E0.Title.Debug", 0x07000000, 0x070065A8],
	[ultra.c.f_data, "E0.Title", 0x14000414, 0x140004FC, [
		[0, 1, 1, UNSM.c.d_shplang, 0x140004FC],
	]],
]

title_logo = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[UNSM.c.f_gltf, "logo", [
		("wood", None, ("wood.rgba16.png", 32, 32)),
		("marble", None, ("marble.rgba16.png", 32, 32)),
		("shade", None),
		("copyright", None, ("copyright.rgba16.png", 128, 16)),
		("trademark", None, ("trademark.rgba16.png", 16, 16)),
	]],
	[UNSM.c.f_gltf_mesh, "logo", [
		(False, "marble"),
		(False, "wood"),
		(False, "shade"),
	]],
	[ultra.c.f_data, "E0.Title.Logo", 0x07007EA0, 0x0700B420, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "wood"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "marble"],
		[0, 1, 1, UNSM.c.d_gfx, 0x0700B420, "logo", 0, 1, 2],
	]],
	[UNSM.c.f_gltf_mesh, "symbol", [
		(False, "copyright"),
		(False, "trademark"),
	]],
	[ultra.c.f_data, "E0.Title.Logo", 0x0700B4A0, 0x0700C790, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 128, 16, "copyright"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16",  16, 16, "trademark"],
		[0, 1, 1, UNSM.c.d_gfx, 0x0700C790, "symbol", 0, 1],
	]],
	[UNSM.c.f_gltf_write],
	[ultra.c.f_data, "E0.Title.Logo", 0x0700C790, 0x0700C940, [
		[0, -(20+16), 3, ultra.c.d_f32, "%.4f"],
	]],
]

title_debug = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[UNSM.c.f_gltf, "debug", [
		("super_s", (0.5, 0xFF, 0x00, 0x00)),
		("super_u", (0.5, 0x00, 0x00, 0xFF)),
		("super_p", (0.5, 0x00, 0xAD, 0x00)),
		("super_e", (0.5, 0xFF, 0x00, 0x00)),
		("super_r", (0.5, 0x00, 0x00, 0xFF)),
		("mario_m", (0.5, 0xFF, 0x00, 0x00)),
		("mario_a", (0.5, 0x00, 0x00, 0xFF)),
		("mario_r", (0.5, 0x00, 0xB2, 0x00)),
		("mario_i", (0.5, 0xFF, 0x00, 0x00)),
		("mario_o", (0.5, 0x00, 0x00, 0xFF)),
	]],
	[ultra.c.f_data, "E0.Title.Debug", 0x07000000, 0x07000018, [
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[UNSM.c.f_gltf_mesh, "super_s", [
		(True, "super_s"),
	]],
	[ultra.c.f_data, "E0.Title.Debug", 0x07000858, 0x07000A40, [
		[0, 1, 1, UNSM.c.d_gfx, 0x07000A28, "super_s", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[UNSM.c.f_gltf_mesh, "super_u", [
		(True, "super_u"),
	]],
	[ultra.c.f_data, "E0.Title.Debug", 0x07001100, 0x070012A0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x07001288, "super_u", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[UNSM.c.f_gltf_mesh, "super_p", [
		(True, "super_p"),
	]],
	[ultra.c.f_data, "E0.Title.Debug", 0x07001BA0, 0x07001DB0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x07001D98, "super_p", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[UNSM.c.f_gltf_mesh, "super_e", [
		(True, "super_e"),
	]],
	[ultra.c.f_data, "E0.Title.Debug", 0x070025F0, 0x070027D8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x070027C0, "super_e", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[UNSM.c.f_gltf_mesh, "super_r", [
		(True, "super_r"),
	]],
	[ultra.c.f_data, "E0.Title.Debug", 0x07003258, 0x070034B8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x070034A0, "super_r", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[UNSM.c.f_gltf_mesh, "mario_m", [
		(True, "mario_m"),
	]],
	[ultra.c.f_data, "E0.Title.Debug", 0x07003DB8, 0x07003FC8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x07003FB0, "mario_m", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[UNSM.c.f_gltf_mesh, "mario_a", [
		(True, "mario_a"),
	]],
	[ultra.c.f_data, "E0.Title.Debug", 0x070048C8, 0x07004AD8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x07004AC0, "mario_a", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[UNSM.c.f_gltf_mesh, "mario_r", [
		(True, "mario_r"),
	]],
	[ultra.c.f_data, "E0.Title.Debug", 0x07005558, 0x070057B8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x070057A0, "mario_r", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[UNSM.c.f_gltf_mesh, "mario_i", [
		(True, "mario_i"),
	]],
	[ultra.c.f_data, "E0.Title.Debug", 0x070059F8, 0x07005AB0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x07005A98, "mario_i", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[UNSM.c.f_gltf_mesh, "mario_o", [
		(True, "mario_o"),
	]],
	[ultra.c.f_data, "E0.Title.Debug", 0x070063B0, 0x070065A8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x070065A8, "mario_o", 0],
	]],
	[UNSM.c.f_gltf_write],
]

title_back = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[ultra.c.f_data, "E0.Title.Back", 0x0A000000, 0x0A0065E8, [
		[0, -16, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, ultra.c.d_Gfx, 0x0A0001C0],
		d_texture_n("rgba16", 80, 20, 4, "title/mario.%d"),
		d_texture_n("rgba16", 80, 20, 4, "title/gameover.%d"),
		[0, -8, 1, ultra.c.d_addr, 0],
		[0, 1, 1, ultra.c.d_s64],
	]],
]

seq = [
	[main.s_file, "stage/title/seq.sx", title_seq],
	[main.s_file, "stage/title/shp.c", title_shp],
	[main.s_file, "stage/title/logo.c", title_logo],
	[main.s_file, "stage/title/debug.c", title_debug],
	[main.s_file, "data/background/title.c", title_back],
]
