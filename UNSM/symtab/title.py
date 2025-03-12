import main

sym_E0_Title = {
	0x14000000: main.sym("seq_logo", flag={"GLOBL"}),
	0x14000078: main.sym("seq_face", flag={"GLOBL"}),
	0x14000104: main.sym("seq_gameover", flag={"GLOBL"}),
	0x14000190: main.sym("seq_debug", flag={"GLOBL"}),
	0x1400020C: main.sym("goto_fileselect"),
	0x14000238: main.sym("goto_debug"),
	0x1400025C: main.sym("goto_game"),
	0x14000284: main.sym("goto_demo"),
	0x140002A8: main.sym("goto_logo"),
	0x140002D0: main.sym_var("shp_logo", "SHPLANG", "[]", flag={"GLOBL"}),
	0x1400035C: main.sym_var("shp_face", "SHPLANG", "[]", flag={"GLOBL"}),
	0x140003B8: main.sym_var("shp_gameover", "SHPLANG", "[]", flag={"GLOBL"}),
	0x14000414: main.sym_var("shp_debug", "SHPLANG", "[]", flag={"GLOBL"}),
}

seg_E0_Title = {
	0x140004A0: "E0.Title.Debug",
}

sym_E0_TitleLogo = {
	0x07007EA0: main.sym_var("txt_logo_wood", "static u16", "[]"),
	0x070086A0: main.sym_var("txt_logo_marble", "static u16", "[]"),
	0x07008EA0: main.sym_var("gfx_logo_marble", "static Gfx", "[]"),
	0x07009E38: main.sym_var("gfx_logo_wood", "static Gfx", "[]"),
	0x0700ADC0: main.sym_var("gfx_logo_shade", "static Gfx", "[]"),
	0x0700B3A0: main.sym_var("gfx_logo", "Gfx", "[]", flag={"GLOBL"}),
	0x0700B4A0: main.sym_var("txt_logo_copyright", "static u16", "[]"),
	0x0700C4A0: main.sym_var("txt_logo_trademark", "static u16", "[]"),
	0x0700C6A0: main.sym_var("gfx_symbol", "Gfx", "[]", flag={"GLOBL"}),
	0x0700C790: main.sym_var("logo_scale_a", "float", "[]"),
	0x0700C880: main.sym_var("logo_scale_b", "float", "[]"),
}

sym_E0_TitleDebug = {
	0x07000000: main.sym_var("light_debug_super_s", "static Lights1"),
	0x07000858: main.sym_var("gfx_debug_super_s", "Gfx", "[]", flag={"GLOBL"}),
	0x07000A28: main.sym_var("light_debug_super_u", "static Lights1"),
	0x07001100: main.sym_var("gfx_debug_super_u", "Gfx", "[]", flag={"GLOBL"}),
	0x07001288: main.sym_var("light_debug_super_p", "static Lights1"),
	0x07001BA0: main.sym_var("gfx_debug_super_p", "Gfx", "[]", flag={"GLOBL"}),
	0x07001D98: main.sym_var("light_debug_super_e", "static Lights1"),
	0x070025F0: main.sym_var("gfx_debug_super_e", "Gfx", "[]", flag={"GLOBL"}),
	0x070027C0: main.sym_var("light_debug_super_r", "static Lights1"),
	0x07003258: main.sym_var("gfx_debug_super_r", "Gfx", "[]", flag={"GLOBL"}),
	0x070034A0: main.sym_var("light_debug_mario_m", "static Lights1"),
	0x07003DB8: main.sym_var("gfx_debug_mario_m", "Gfx", "[]", flag={"GLOBL"}),
	0x07003FB0: main.sym_var("light_debug_mario_a", "static Lights1"),
	0x070048C8: main.sym_var("gfx_debug_mario_a", "Gfx", "[]", flag={"GLOBL"}),
	0x07004AC0: main.sym_var("light_debug_mario_r", "static Lights1"),
	0x07005558: main.sym_var("gfx_debug_mario_r", "Gfx", "[]", flag={"GLOBL"}),
	0x070057A0: main.sym_var("light_debug_mario_i", "static Lights1"),
	0x070059F8: main.sym_var("gfx_debug_mario_i", "Gfx", "[]", flag={"GLOBL"}),
	0x07005A98: main.sym_var("light_debug_mario_o", "static Lights1"),
	0x070063B0: main.sym_var("gfx_debug_mario_o", "Gfx", "[]", flag={"GLOBL"}),
}

imm_E0_TitleDebug = {
	0x07000878: 0x07000018,
	0x070008A8: 0x07000018,
	0x070008D8: 0x07000018,
	0x07000908: 0x07000018,
	0x07000938: 0x07000018,
	0x07000968: 0x07000018,
	0x07000998: 0x07000018,
	0x070009C8: 0x07000018,
	0x070009F8: 0x07000018,
	0x07001120: 0x07000A40,
	0x07001150: 0x07000A40,
	0x07001180: 0x07000A40,
	0x070011B0: 0x07000A40,
	0x070011E0: 0x07000A40,
	0x07001210: 0x07000A40,
	0x07001240: 0x07000A40,
	0x07001270: 0x07000A40,
	0x07001BC0: 0x070012A0,
	0x07001BF0: 0x070012A0,
	0x07001C20: 0x070012A0,
	0x07001C50: 0x070012A0,
	0x07001C80: 0x070012A0,
	0x07001CB0: 0x070012A0,
	0x07001CE0: 0x070012A0,
	0x07001D10: 0x070012A0,
	0x07001D40: 0x070012A0,
	0x07001D70: 0x070012A0,
	0x07002610: 0x07001DB0,
	0x07002640: 0x07001DB0,
	0x07002670: 0x07001DB0,
	0x070026A0: 0x07001DB0,
	0x070026D0: 0x07001DB0,
	0x07002700: 0x07001DB0,
	0x07002730: 0x07001DB0,
	0x07002760: 0x07001DB0,
	0x07002790: 0x07001DB0,
	0x07003278: 0x070027D8,
	0x070032A8: 0x070027D8,
	0x070032D8: 0x070027D8,
	0x07003308: 0x070027D8,
	0x07003338: 0x070027D8,
	0x07003368: 0x070027D8,
	0x07003398: 0x070027D8,
	0x070033C8: 0x070027D8,
	0x070033F8: 0x070027D8,
	0x07003428: 0x070027D8,
	0x07003458: 0x070027D8,
	0x07003488: 0x070027D8,
	0x07003DD8: 0x070034B8,
	0x07003E08: 0x070034B8,
	0x07003E38: 0x070034B8,
	0x07003E68: 0x070034B8,
	0x07003E98: 0x070034B8,
	0x07003EC8: 0x070034B8,
	0x07003EF8: 0x070034B8,
	0x07003F28: 0x070034B8,
	0x07003F58: 0x070034B8,
	0x07003F88: 0x070034B8,
	0x070048E8: 0x07003FC8,
	0x07004918: 0x07003FC8,
	0x07004948: 0x07003FC8,
	0x07004978: 0x07003FC8,
	0x070049A8: 0x07003FC8,
	0x070049D8: 0x07003FC8,
	0x07004A08: 0x07003FC8,
	0x07004A38: 0x07003FC8,
	0x07004A68: 0x07003FC8,
	0x07004A98: 0x07003FC8,
	0x07005578: 0x07004AD8,
	0x070055A8: 0x07004AD8,
	0x070055D8: 0x07004AD8,
	0x07005608: 0x07004AD8,
	0x07005638: 0x07004AD8,
	0x07005668: 0x07004AD8,
	0x07005698: 0x07004AD8,
	0x070056C8: 0x07004AD8,
	0x070056F8: 0x07004AD8,
	0x07005728: 0x07004AD8,
	0x07005758: 0x07004AD8,
	0x07005788: 0x07004AD8,
	0x07005A18: 0x070057B8,
	0x07005A48: 0x070057B8,
	0x07005A78: 0x070057B8,
	0x070063D0: 0x07005AB0,
	0x07006400: 0x07005AB0,
	0x07006430: 0x07005AB0,
	0x07006460: 0x07005AB0,
	0x07006490: 0x07005AB0,
	0x070064C0: 0x07005AB0,
	0x070064F0: 0x07005AB0,
	0x07006520: 0x07005AB0,
	0x07006550: 0x07005AB0,
	0x07006580: 0x07005AB0,
}

sym_E0_TitleBack = {
	0x0A000000: main.sym_var("vtx_titlebg", "static Vtx", "[]"),
	0x0A000100: main.sym_var("gfx_titlebg_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x0A000118: main.sym_var("gfx_titlebg_vtx", "Gfx", "[]", flag={"GLOBL"}),
	0x0A000130: main.sym_var("gfx_titlebg_0", "Gfx", "[]", flag={"GLOBL"}),
	0x0A000148: main.sym_var("gfx_titlebg_1", "Gfx", "[]", flag={"GLOBL"}),
	0x0A000160: main.sym_var("gfx_titlebg_2", "Gfx", "[]", flag={"GLOBL"}),
	0x0A000178: main.sym_var("gfx_titlebg_3", "Gfx", "[]", flag={"GLOBL"}),
	0x0A000190: main.sym_var("gfx_titlebg_end", "Gfx", "[]", flag={"GLOBL"}),
	0x0A0001C0: main.sym_var("txt_titlebg_mario_0", "static u16", "[]"),
	0x0A000E40: main.sym_var("txt_titlebg_mario_1", "static u16", "[]"),
	0x0A001AC0: main.sym_var("txt_titlebg_mario_2", "static u16", "[]"),
	0x0A002740: main.sym_var("txt_titlebg_mario_3", "static u16", "[]"),
	0x0A0033C0: main.sym_var("txt_titlebg_gameover_0", "static u16", "[]"),
	0x0A004040: main.sym_var("txt_titlebg_gameover_1", "static u16", "[]"),
	0x0A004CC0: main.sym_var("txt_titlebg_gameover_2", "static u16", "[]"),
	0x0A005940: main.sym_var("txt_titlebg_gameover_3", "static u16", "[]"),
	0x0A0065C0: main.sym_var("txt_titlebg_mario", "u16 *", "[]"),
	0x0A0065D0: main.sym_var("txt_titlebg_gameover", "u16 *", "[]"),
	0x0A0065E0: main.sym_var("align_0", "UNUSED static long long"),
}
