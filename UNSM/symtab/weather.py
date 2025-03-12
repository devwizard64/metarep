import main

sym_Weather = {
	0x0B000000: main.sym_var("align_0", "UNUSED static long long"),
	0x0B000008: main.sym_var("txt_weather_flower_0", "static u16", "[]"),
	0x0B000808: main.sym_var("txt_weather_flower_1", "static u16", "[]"),
	0x0B001008: main.sym_var("txt_weather_flower_2", "static u16", "[]"),
	0x0B001808: main.sym_var("txt_weather_flower_3", "static u16", "[]"),
	0x0B002008: main.sym_var("txt_weather_flower", "u16 *", "[]"),
	0x0B002020: main.sym_var("txt_lava_0", "static u16", "[]"),
	0x0B002820: main.sym_var("txt_lava_1", "static u16", "[]"),
	0x0B003020: main.sym_var("txt_lava_2", "static u16", "[]"),
	0x0B003820: main.sym_var("txt_lava_3", "static u16", "[]"),
	0x0B004020: main.sym_var("txt_lava_4", "static u16", "[]"),
	0x0B004820: main.sym_var("txt_lava_5", "static u16", "[]"),
	0x0B005020: main.sym_var("txt_lava_6", "static u16", "[]"),
	0x0B005820: main.sym_var("txt_lava_7", "static u16", "[]"),
	0x0B006020: main.sym_var("txt_weather_lava", "u16 *", "[]"),
	0x0B006048: main.sym_var("txt_weather_bubble_0", "static u16", "[]"),
	0x0B006848: main.sym_var("txt_weather_bubble", "u16 *", "[]"),
	0x0B00684C: main.sym_var("txt_snow_a", "static u16", "[]"),
	0x0B006A50: main.sym_var("gfx_snow_a", "Gfx", "[]", flag={"GLOBL"}),
	0x0B006AB0: main.sym_var("gfx_weather_end", "Gfx", "[]", flag={"GLOBL"}),
	0x0B006AD8: main.sym_var("txt_snow_b", "static u16", "[]"),
	0x0B006CD8: main.sym_var("gfx_snow_b", "Gfx", "[]", flag={"GLOBL"}),
	0x0B006D38: main.sym_var("gfx_lava_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x0B006D68: main.sym_var("gfx_lava_txt", "Gfx", "[]", flag={"GLOBL"}),
}

sym_J0_Weather = sym_Weather
sym_E0_Weather = sym_Weather
