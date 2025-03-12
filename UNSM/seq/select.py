import main
import ultra

import UNSM.asm
import UNSM.c

file_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "file", [
		("edge", (0.25, 0xFF, 0xFF, 0xFF), ("light.rgba16.png", 32, 32)),
		("face", (0.25, 0xFF, 0xFF, 0xFF), ("new.rgba16.png", 64, 32)),
	]],
	[ultra.c.f_data, "E0.Select.Gfx", 0x07000000, 0x07003018, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "light"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "shade"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "mario"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "new"],
	]],
	[UNSM.c.f_gltf_mesh, "file", [
		(True, "edge"),
		(True, "face"),
	]],
	[ultra.c.f_data, "E0.Select.Gfx", 0x07003158, 0x07003450, [
		[0, 1, 1, UNSM.c.d_gfx, 0x07003258, "file", 0, 1],
		[0, -4, 1, ultra.c.d_Vtx, True],
		[0, 1, 1, ultra.c.d_Gfx, 0x07003450],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Select.Gfx", 0x07000000, 0x07003450],
	[ultra.c.f_data, "E0.Select", 0x140001D0, 0x14000290, [
		[0, 1, 1, UNSM.c.d_shplang, 0x14000290],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

tile_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "tile", [
		("tile", (0.25, 0xFF, 0xFF, 0xFF), ("main.rgba16.png", 32, 32)),
	]],
	[ultra.c.f_data, "E0.Select.Gfx", 0x07003450, 0x07005C68, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "erase"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "copy"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "main"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "score"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "sound"],
	]],
	[UNSM.c.f_gltf_mesh, "tile", [
		(True, "tile"),
	]],
	[ultra.c.f_data, "E0.Select.Gfx", 0x07006038, 0x070062E8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x070062E8, "tile", 0],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Select.Gfx", 0x07003450, 0x070062E8],
	[ultra.c.f_data, "E0.Select", 0x14000290, 0x14000380, [
		[0, 1, 1, UNSM.c.d_shplang, 0x14000380],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

cursor_gfx = [
	[ultra.c.f_data, "E0.Select.Gfx", 0x070062E8, 0x070073D0, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "0"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "1"],
		[0, 1, 1, ultra.c.d_Gfx, 0x070073D0],
	]],
]

selfont_gfx = [
	[ultra.c.f_data, "E0.Select.Gfx", 0x070073D0, 0x0700ABD0, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, name]
		for name in [
			"k_hu",
			"k_xa",
			"k_i",
			"k_ru",
			"k_se",
			"k_re",
			"k_ku",
			"k_to",
			"h_wo",
			"k_ko",
			"k_pi",
			"chouonpu",
			"h_su",
			"h_ru",
			"h_ke",
			"k_ma",
			"k_ri",
			"k_o",
			"k_su",
			"k_a",
			"h_mi",
			"h_do",
			"h_no",
			"question",
			"k_sa",
			"k_u",
			"k_n",
			"k_do",
		]
	]],
	[ultra.c.f_data, "E0.Select.Gfx", 0x0700ABD0, 0x0700AC40, [
		[0, -28, 1, ultra.c.d_addr, 0],
	]],
]

smfont_gfx = [
	[ultra.c.f_data, "E0.Select.Gfx", 0x0700AC40, 0x0700B840, [
		[0, 1, 1, UNSM.c.d_texture, "ia8", 8, 8, name]
		for name in list("0123456789") + [
			"upper_"+x for x in "abcdefghijklmnopqrstuvwxyz"
		] + [
			"coin",
			"cross",
			"star",
			"hyphen",
			"comma",
			"apostrophe",
			"bang",
			"question",
			"marioL",
			"marioR",
			"period",
			"ampersand",
		]
	]],
	[ultra.c.f_data, "E0.Select.Gfx", 0x0700B840, 0x0700BCD8, [
		[0, -256, 1, ultra.c.d_addr, 0],
		[0, 1, 1, ultra.c.d_Gfx, 0x0700BCD8],
	]],
]

course_gfx = [
	[ultra.c.f_data, "E0.Select.Gfx", 0x0700BCE0, 0x0700DE30, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "h"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "l"],
		[0, -8, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, ultra.c.d_Gfx, 0x0700DE30],
	]],
]

select_gfx = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[main.f_str, "#include \"file/shape.c\"\n"],
	[main.f_str, "#include \"tile/shape.c\"\n"],
	[main.f_str, "#include \"cursor/gfx.c\"\n"],
	[main.f_str, "#include \"selfont/gfx.c\"\n"],
	[main.f_str, "#include \"smfont/gfx.c\"\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.Select.Gfx", 0x0700BCD8, 0x0700BCE0, [
		[0, 1, 1, ultra.c.d_s64],
	]],
	[main.f_str, "#include \"course/gfx.c\"\n"],
	[UNSM.c.f_obj, "select"],
	[ultra.c.f_data, "E0.Select.Gfx", 0x0700DE30, 0x0700DE60, [
		[0, 1, 1, UNSM.c.d_map, "map"],
	]],
	[UNSM.c.f_obj_write],
]

select_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.Select", 0x14000000, 0x140001C4],
]

select_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "#include \"file/shape.c\"\n"],
	[main.f_str, "#include \"tile/shape.c\"\n"],
	[ultra.c.f_extern, "E0.menu.text", 0x80176688, 0x801766DC],
	[ultra.c.f_extern, "E0.menu.text", 0x80177518, 0x80177560],
	[ultra.c.f_data, "E0.Select", 0x14000380, 0x14000490, [
		[0, 1, 1, UNSM.c.d_shplang, 0x14000490],
	]],
]

seq = [
	[main.s_file, "stage/select/file/shape.c", file_shape],
	[main.s_file, "stage/select/tile/shape.c", tile_shape],
	[main.s_file, "stage/select/cursor/gfx.c", cursor_gfx],
	[main.s_file, "stage/select/selfont/gfx.c", selfont_gfx],
	[main.s_file, "stage/select/smfont/gfx.c", smfont_gfx],
	[main.s_file, "stage/select/course/gfx.c", course_gfx],
	[main.s_file, "stage/select/gfx.c", select_gfx],
	[main.s_file, "stage/select/seq.sx", select_seq],
	[main.s_file, "stage/select/shp.c", select_shp],
]
