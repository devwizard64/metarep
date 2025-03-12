import main
import ultra

import UNSM.c

from . import d_texture_n

texture_a = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.TextureA", 0x09000000, 0x0900C000, [
		d_texture_n("rgba16", 32, 32, 24, "a%d"),
	]],
]

seq_texture_a = [
	[main.s_file, "data/texture/a.c", texture_a],
]

texture_b = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.TextureB", 0x09000000, 0x0900C800, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "b0"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "b1"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "b2"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "b3"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "b4"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "b5"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "b6"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "b7"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "b8"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "b9"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "b10"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "b11"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "b12"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "b13"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "b14"],
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "b15_g17"], # light spot
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "b16"], # light edge 1
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 64, "b17"], # light torch
	]],
]

seq_texture_b = [
	[main.s_file, "data/texture/b.c", texture_b],
]

texture_c = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.TextureC", 0x09000000, 0x0900B800, [
		d_texture_n("rgba16", 32, 32, 12, "c%d", 0),
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "c12"],
		d_texture_n("rgba16", 32, 32, 21, "c%d", 13),
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "c21_j22_k22"], # shadow circle
	]],
]

seq_texture_c = [
	[main.s_file, "data/texture/c.c", texture_c],
]

texture_d = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.TextureD", 0x09000000, 0x0900C800, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "d0"],
		d_texture_n("rgba16", 64, 32, 6, "d%d", 1),
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "d6"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "d7"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "d8"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "d9"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "d10"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "d11"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "d12"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "d13"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "d14"],
	]],
]

seq_texture_d = [
	[main.s_file, "data/texture/d.c", texture_d],
]

texture_e = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.TextureE", 0x09000000, 0x09008800, [
		d_texture_n("rgba16", 32, 32, 4, "e%d"),
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "e4"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "e5"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "e6"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "e7"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "e8_j12"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "e9"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "e10_i17"],
		d_texture_n("rgba16", 32, 32, 15, "e%d", 11),
	]],
]

seq_texture_e = [
	[main.s_file, "data/texture/e.c", texture_e],
]

texture_f = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.TextureF", 0x09000000, 0x0900A000, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "f0"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "f1"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "f2"],
		d_texture_n("rgba16", 32, 32, 13, "f%d", 3),
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "f13"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "f14"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "f15"],
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "f16"], # ice?
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "f17"], # shadow snowtree
	]],
]

seq_texture_f = [
	[main.s_file, "data/texture/f.c", texture_f],
]

texture_g = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.TextureG", 0x09000000, 0x0900C800, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "g0"],
		d_texture_n("rgba16", 32, 32, 6, "g%d", 1),
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "g6"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "g7"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "g8"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "g9"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "g10"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "g11"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "g12"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "g13"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "g14"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "g15"],
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "g16"], # light edge 2
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "b15_g17"],
	]],
]

seq_texture_g = [
	[main.s_file, "data/texture/g.c", texture_g],
]

texture_h = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.TextureH", 0x09000000, 0x09008C00, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "h0"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "h1_l6"],
		d_texture_n("rgba16", 32, 32, 8, "h%d", 2),
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "h8"],
		d_texture_n("rgba16", 32, 32, 14, "h%d", 9),
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 64, "h14"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 8, "h15"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "h16"],
	]],
]

seq_texture_h = [
	[main.s_file, "data/texture/h.c", texture_h],
]

texture_i = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.TextureI", 0x09000000, 0x0900C800, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "i0"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "i1"],
		d_texture_n("rgba16", 32, 32, 10, "i%d", 2),
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "i10"],
		d_texture_n("rgba16", 32, 32, 15, "i%d", 11),
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "i15"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "i16"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "e10_i17"],
		d_texture_n("rgba16", 32, 32, 22, "i%d", 18),
	]],
]

seq_texture_i = [
	[main.s_file, "data/texture/i.c", texture_i],
]

texture_j = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.TextureJ", 0x09000000, 0x0900C000, [
		d_texture_n("rgba16", 32, 32, 12, "j%d"),
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "e8_j12"],
		d_texture_n("rgba16", 32, 32, 22, "j%d", 13),
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "c21_j22_k22"],
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "j23"], # cloud?
	]],
]

seq_texture_j = [
	[main.s_file, "data/texture/j.c", texture_j],
]

texture_k = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.TextureK", 0x09000000, 0x0900C400, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "k0"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "k1"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "k2"],
		d_texture_n("rgba16", 32, 32, 12, "k%d", 3),
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "k12"],
		d_texture_n("rgba16", 32, 32, 20, "k%d", 13),
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 32, "k20"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "k21"],
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "c21_j22_k22"],
	]],
]

seq_texture_k = [
	[main.s_file, "data/texture/k.c", texture_k],
]

texture_l = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.TextureL", 0x09000000, 0x0900C800, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "l0"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "l1"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "l2"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "l3"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "l4"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "l5"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "h1_l6"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "l7"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "l8"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "l9"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "l10"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "l11"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "l12"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "l13"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "l14"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "l15"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "l16"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "l17"],
	]],
]

seq_texture_l = [
	[main.s_file, "data/texture/l.c", texture_l],
]
