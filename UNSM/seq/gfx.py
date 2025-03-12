import main
import ultra

import UNSM.c
import UNSM.fmt

glbfont_texture = [
	[ultra.c.f_data, "E0.Gfx", 0x02000000, 0x02004A00, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, name]
		for name in list("0123456789abcdefghiklmnoprstuwy") + [
			"squote",
			"dquote",
			"cross",
			"coin",
			"mario",
			"star",
		]
	]],
]

staff_texture = [
	[ultra.c.f_data, "E0.Gfx", 0x02004A00, 0x02005900, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 8, 8, name]
		for name in list("346abcdefghijklmnopqrstuvwxyz") + ["period"]
	]],
]

lgfont_texture = [
	[ultra.c.f_data, "E0.Gfx", 0x02005900, 0x02007000, [
		[0, 1, 1, UNSM.c.d_texture, "ia4", 16, 8, name]
		for name in list("0123456789") + [
			"upper_"+x for x in "abcdefghijklmnopqrstuvwxyz"
		] + [
			"lower_"+x for x in "abcdefghijklmnopqrstuvwxyz"
		] + [
			"arrow",
			"bang",
			"coin",
			"cross",
			"lparen",
			"rlparen",
			"rparen",
			"tilde",
			"period",
			"percent",
			"bullet",
			"comma",
			"apostrophe",
			"question",
			"star",
			"nostar",
			"lquote",
			"rquote",
			"colon",
			"hyphen",
			"ampersand",
			"ba",
			"bb",
			"bc",
			"bz",
			"br",
			"cu",
			"cd",
			"cl",
			"cr",
		]
	]],
]

camera_texture = [
	[ultra.c.f_data, "E0.Gfx", 0x02007000, 0x02007700, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, "camera"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, "lakitu"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, "cross"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16",  8,  8, "up"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16",  8,  8, "down"],
	]],
]

glbfont_table = [
	[ultra.c.f_data, "E0.Gfx", 0x02007700, 0x020077E8, [
		[0, -58, 1, ultra.c.d_addr, 0],
	]],
]

lgfont_table = [
	[ultra.c.f_data, "E0.Gfx", 0x020077E8, 0x02007BE8, [
		[0, -0x100, 1, ultra.c.d_addr, 0],
	]],
]

staff_table = [
	[ultra.c.f_data, "E0.Gfx", 0x02007BE8, 0x02007C7C, [
		[0, -37, 1, ultra.c.d_addr, 0],
	]],
]

camera_table = [
	[ultra.c.f_data, "E0.Gfx", 0x02007C7C, 0x02007C94, [
		[0, -6, 1, ultra.c.d_addr, 0],
	]],
]

font = [
	[ultra.c.f_data, "E0.Gfx", 0x02011AB8, 0x02011E10, [
		[0, 1, 1, ultra.c.d_s64],
		[0, 1, 1, ultra.c.d_Gfx, 0x02011C08],
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0,  1, 1, ultra.c.d_Gfx, 0x02011C88],
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0,  1, 1, ultra.c.d_Gfx, 0x02011D90],
		[0, -3, 1, ultra.c.d_Vtx, False],
		[0,  1, 1, ultra.c.d_Gfx, 0x02011E10],
	]],
]

number = [
	[ultra.c.f_data, "E0.Gfx", 0x02011E10, 0x020120B8, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0,  1, 1, ultra.c.d_Gfx, 0x020120B8],
	]],
]

shadow_texture = [
	[ultra.c.f_data, "E0.Gfx", 0x020120B8, 0x020122B8, [
		[0, 1, 1, UNSM.c.d_texture, "ia8", 16, 16, "circle"],
		[0, 1, 1, UNSM.c.d_texture, "ia8", 16, 16, "square"],
	]],
]

wipe_texture = [
	[ultra.c.f_data, "E0.Gfx", 0x020122B8, 0x02014AB8, [
		[0, 1, 1, UNSM.c.d_texture, "ia8", 32, 64, "star"],
		[0, 1, 1, UNSM.c.d_texture, "ia8", 32, 64, "circle"],
		[0, 1, 1, UNSM.c.d_texture, "ia8", 64, 64, "mario"],
		[0, 1, 1, UNSM.c.d_texture, "ia8", 32, 64, "bowser"],
	]],
]

water_texture = [
	[ultra.c.f_data, "E0.Gfx", 0x02014AB8, 0x020172B8, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "0"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "1"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "2"],
		[0, 1, 1, UNSM.c.d_texture, "ia16",   32, 32, "mist"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "lava"],
	]],
]

common = [
	[ultra.c.f_data, "E0.Gfx", 0x020172B8, 0x02017380, [
		[0, 1, 1, ultra.c.d_Lights1],
		[0, 2, 1, UNSM.c.d_Mtx],
		[0, 1, 1, ultra.c.d_Gfx, 0x02017380],
	]],
]

shadow_gfx = [
	[ultra.c.f_data, "E0.Gfx", 0x02017380, 0x020174C0, [
		[0, 1, 1, ultra.c.d_Gfx, 0x020174C0],
	]],
]

wipe_gfx = [
	[ultra.c.f_data, "E0.Gfx", 0x020174C0, 0x02017568, [
		[0, 1, 1, ultra.c.d_Gfx, 0x02017568],
	]],
]

background = [
	[ultra.c.f_data, "E0.Gfx", 0x02017568, 0x020175F0, [
		[0, 1, 1, ultra.c.d_Gfx, 0x020175F0],
	]],
]

water_gfx = [
	[ultra.c.f_data, "E0.Gfx", 0x020175F0, 0x02017698, [
		[0, 1, 1, ultra.c.d_Gfx, 0x02017698],
	]],
]

minimap_gfx = [
	[ultra.c.f_data, "E0.Gfx", 0x02017698, 0x020177B8, [
		[0, 1, 1, UNSM.c.d_texture, "ia8", 8, 8, "arrow"],
		[0, 1, 1, ultra.c.d_Gfx, 0x020177B8],
	]],
]

wave = [
	[ultra.c.f_data, "E0.Gfx", 0x020177B8, 0x02018A0E, [
		[0, 1, 1, ultra.c.d_Lights1],
		[0, 1, 1, ultra.c.d_Gfx, 0x020178C0],
		[0, 2, 1, UNSM.c.d_wave_shape],
		[0, 1, 2, None],
		[0, 1, 1, UNSM.c.d_wave_shade, 0x02018A0E],
	]],
]

seq = [
	[main.s_file, "data/gfx/glbfont/texture.c", glbfont_texture],
	[main.s_file, "data/gfx/staff/texture.c", staff_texture],
	[main.s_file, "data/gfx/lgfont/texture.c", lgfont_texture],
	[main.s_file, "data/gfx/camera/texture.c", camera_texture],
	[main.s_file, "data/gfx/glbfont/table.c", glbfont_table],
	[main.s_file, "data/gfx/lgfont/table.c", lgfont_table],
	[main.s_file, "data/gfx/staff/table.c", staff_table],
	[main.s_file, "data/gfx/camera/table.c", camera_table],
	[UNSM.c.s_message, "data/gfx/select.ja_jp.txt",  "E0.Gfx", 0x02007D28, 0x02007D34, "message", "ja", "selecttab",  "%d"],
	[UNSM.c.s_message, "data/gfx/message.ja_jp.txt", "J0.Gfx", 0x0200DFE8, 0x0200E294, "message", "ja", "messagetab", "%d"],
	[UNSM.c.s_message, "data/gfx/course.ja_jp.txt",  "J0.Gfx", 0x0200E454, 0x0200E4C0, "table",   "ja", "coursename", UNSM.fmt.fmt_coursename],
	[UNSM.c.s_message, "data/gfx/level.ja_jp.txt",   "J0.Gfx", 0x0200EAD0, 0x0200EC58, "table",   "ja", "levelname",  UNSM.fmt.fmt_levelname],
	[UNSM.c.s_message, "data/gfx/message.en_us.txt", "E0.Gfx", 0x02010A68, 0x02010D14, "message", "en", "messagetab", "%d"],
	[UNSM.c.s_message, "data/gfx/course.en_us.txt",  "E0.Gfx", 0x02010F68, 0x02010FD4, "table",   "en", "coursename", UNSM.fmt.fmt_coursename],
	[UNSM.c.s_message, "data/gfx/level.en_us.txt",   "E0.Gfx", 0x0201192C, 0x02011AB4, "table",   "en", "levelname",  UNSM.fmt.fmt_levelname],
	[main.s_file, "data/gfx/font.c", font],
	[main.s_file, "data/gfx/number.c", number],
	[main.s_file, "data/gfx/shadow/texture.c", shadow_texture],
	[main.s_file, "data/gfx/wipe/texture.c", wipe_texture],
	[main.s_file, "data/gfx/water/texture.c", water_texture],
	[main.s_file, "data/gfx/common.c", common],
	[main.s_file, "data/gfx/shadow/gfx.c", shadow_gfx],
	[main.s_file, "data/gfx/wipe/gfx.c", wipe_gfx],
	[main.s_file, "data/gfx/background.c", background],
	[main.s_file, "data/gfx/water/gfx.c", water_gfx],
	[main.s_file, "data/gfx/minimap/gfx.c", minimap_gfx],
	[main.s_file, "data/gfx/wave.c", wave],
]
