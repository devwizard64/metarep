import main
import ultra

import UNSM.c
from . import d_texture_n

flower_texture = [
	[ultra.c.f_data, "E0.Weather", 0x0B000008, 0x0B002020, [
		d_texture_n("rgba16", 32, 32, 4),
		[0, -6, 1, ultra.c.d_addr, 0],
	]],
]

lava_texture = [
	[ultra.c.f_data, "E0.Weather", 0x0B002020, 0x0B006048, [
		d_texture_n("rgba16", 32, 32, 8),
		[0, -10, 1, ultra.c.d_addr, 0],
	]],
]

bubble_texture = [
	[ultra.c.f_data, "E0.Weather", 0x0B006048, 0x0B00684C, [
		d_texture_n("rgba16", 32, 32, 1),
		[0, -1, 1, ultra.c.d_addr, 0],
	]],
]

snow_gfx = [
	[ultra.c.f_data, "E0.Weather", 0x0B00684C, 0x0B006D98, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, "a"],
		[0, 1, 4, None],
		[0, 1, 1, ultra.c.d_Gfx, 0x0B006AD8],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, "b"],
		[0, 1, 1, ultra.c.d_Gfx, 0x0B006D98],
	]],
]

seq = [
	[main.s_file, "data/weather/flower/texture.c", flower_texture],
	[main.s_file, "data/weather/lava/texture.c", lava_texture],
	[main.s_file, "data/weather/bubble/texture.c", bubble_texture],
	[main.s_file, "data/weather/snow/gfx.c", snow_gfx],
]
