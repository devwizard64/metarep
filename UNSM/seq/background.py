import main
import ultra

import UNSM.c
from . import d_texture_n

background_a = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[ultra.c.f_data, "E0.BackgroundA", 0x0A000000, 0x0A020000, [
		d_texture_n("rgba16", 32, 32, 64, "a/%02o"),
	]],
	[UNSM.c.f_background, "E0.BackgroundA", 0x0A020000],
]

seq_background_a = [
	[main.s_file, "data/background/a.c", background_a],
]

background_b = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[ultra.c.f_data, "E0.BackgroundB", 0x0A000000, 0x0A020000, [
		d_texture_n("rgba16", 32, 32, 64, "b/%02o"),
	]],
	[UNSM.c.f_background, "E0.BackgroundB", 0x0A020000],
]

seq_background_b = [
	[main.s_file, "data/background/b.c", background_b],
]

background_c = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[ultra.c.f_data, "E0.BackgroundC", 0x0A000000, 0x0A014800, [
		d_texture_n("rgba16", 32, 32, 41, "c/%02o"),
	]],
	[UNSM.c.f_background, "E0.BackgroundC", 0x0A014800],
]

seq_background_c = [
	[main.s_file, "data/background/c.c", background_c],
]

background_d = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[ultra.c.f_data, "E0.BackgroundD", 0x0A000000, 0x0A018800, [
		d_texture_n("rgba16", 32, 32, 49, "d/%02o"),
	]],
	[UNSM.c.f_background, "E0.BackgroundD", 0x0A018800],
]

seq_background_d = [
	[main.s_file, "data/background/d.c", background_d],
]

background_e = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[ultra.c.f_data, "E0.BackgroundE", 0x0A000000, 0x0A020000, [
		d_texture_n("rgba16", 32, 32, 64, "e/%02o"),
	]],
	[UNSM.c.f_background, "E0.BackgroundE", 0x0A020000],
]

seq_background_e = [
	[main.s_file, "data/background/e.c", background_e],
]

background_f = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[ultra.c.f_data, "E0.BackgroundF", 0x0A000000, 0x0A020000, [
		d_texture_n("rgba16", 32, 32, 64, "f/%02o"),
	]],
	[UNSM.c.f_background, "E0.BackgroundF", 0x0A020000],
]

seq_background_f = [
	[main.s_file, "data/background/f.c", background_f],
]

background_g = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[ultra.c.f_data, "E0.BackgroundG", 0x0A000000, 0x0A020000, [
		d_texture_n("rgba16", 32, 32, 64, "g/%02o"),
	]],
	[UNSM.c.f_background, "E0.BackgroundG", 0x0A020000],
]

seq_background_g = [
	[main.s_file, "data/background/g.c", background_g],
]

background_h = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[ultra.c.f_data, "E0.BackgroundH", 0x0A000000, 0x0A014800, [
		d_texture_n("rgba16", 32, 32, 41, "h/%02o"),
	]],
	[UNSM.c.f_background, "E0.BackgroundH", 0x0A014800],
]

seq_background_h = [
	[main.s_file, "data/background/h.c", background_h],
]

background_i = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[ultra.c.f_data, "E0.BackgroundI", 0x0A000000, 0x0A020000, [
		d_texture_n("rgba16", 32, 32, 64, "i/%02o"),
	]],
	[UNSM.c.f_background, "E0.BackgroundI", 0x0A020000],
]

seq_background_i = [
	[main.s_file, "data/background/i.c", background_i],
]

background_j = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[ultra.c.f_data, "E0.BackgroundJ", 0x0A000000, 0x0A020000, [
		d_texture_n("rgba16", 32, 32, 64, "j/%02o"),
	]],
	[UNSM.c.f_background, "E0.BackgroundJ", 0x0A020000],
]

seq_background_j = [
	[main.s_file, "data/background/j.c", background_j],
]
