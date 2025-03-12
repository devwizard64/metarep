import main

sym_J0_Gfx = {
	0x02008250: main.sym_var("txt_glbfont", "u16 *", "[]"),
	0x02008338: main.sym_var("txt_lgfont", "u8 *", "[]"),
	0x02008738: main.sym_var("txt_staff", "u16 *", "[]"),
	0x020087CC: main.sym_var("txt_camera", "u16 *", "[]"),
	#0x02007D28: main.sym_var("selecttab", "MESSAGE *", "[]"),
	0x0200DFE8: main.sym_var("messagetab", "MESSAGE *", "[]"),
	0x0200E454: main.sym_var("coursename", "unsigned char *", "[]"),
	0x0200EAD0: main.sym_var("levelname", "unsigned char *", "[]"),
	0x0200EC60: main.sym_var("gfx_print_copy_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x0200EC98: main.sym_var("gfx_print_copy_char", "Gfx", "[]", flag={"GLOBL"}),
	0x0200ECC8: main.sym_var("gfx_print_copy_end", "Gfx", "[]", flag={"GLOBL"}),
	0x0200ED00: main.sym_var("gfx_print_1cyc_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x0200ED38: main.sym_var("gfx_print_1cyc_char", "Gfx", "[]", flag={"GLOBL"}),
	0x0200ED68: main.sym_var("gfx_print_1cyc_end", "Gfx", "[]", flag={"GLOBL"}),
	0x0200EDE8: main.sym_var("gfx_message_box", "Gfx", "[]", flag={"GLOBL"}),
	0x0200EE68: main.sym_var("gfx_lgfont_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x0200EEA8: main.sym_var("gfx_lgfont_char", "Gfx", "[]", flag={"GLOBL"}),
	0x0200EEF0: main.sym_var("gfx_lgfont_end", "Gfx", "[]", flag={"GLOBL"}),
	0x0200EF60: main.sym_var("gfx_message_cursor", "Gfx", "[]", flag={"GLOBL"}),
	#0x02011ED8: main.sym_var("gfx_number_0", "Gfx", "[]", flag={"GLOBL"}),
	#0x02011F08: main.sym_var("gfx_number_1", "Gfx", "[]", flag={"GLOBL"}),
	#0x02011F38: main.sym_var("gfx_number_2", "Gfx", "[]", flag={"GLOBL"}),
	#0x02011F68: main.sym_var("gfx_number_3", "Gfx", "[]", flag={"GLOBL"}),
	#0x02011F98: main.sym_var("gfx_number_4", "Gfx", "[]", flag={"GLOBL"}),
	#0x02011FC8: main.sym_var("gfx_number_5", "Gfx", "[]", flag={"GLOBL"}),
	#0x02011FF8: main.sym_var("gfx_number_6", "Gfx", "[]", flag={"GLOBL"}),
	#0x02012028: main.sym_var("gfx_number_7", "Gfx", "[]", flag={"GLOBL"}),
	#0x02012058: main.sym_var("gfx_number_8", "Gfx", "[]", flag={"GLOBL"}),
	#0x02012088: main.sym_var("gfx_number_9", "Gfx", "[]", flag={"GLOBL"}),
	#0x020122B8: main.sym_var("txt_wipe_star", "u8", "[]"),
	#0x02012AB8: main.sym_var("txt_wipe_circle", "u8", "[]"),
	#0x020132B8: main.sym_var("txt_wipe_mario", "u8", "[]"),
	#0x020142B8: main.sym_var("txt_wipe_bowser", "u8", "[]"),
	#0x02014AB8: main.sym_var("txt_water_0", "u16", "[]"),
	#0x020152B8: main.sym_var("txt_water_1", "u16", "[]"),
	#0x02015AB8: main.sym_var("txt_water_2", "u16", "[]"),
	#0x020162B8: main.sym_var("txt_mist", "u16", "[]"),
	#0x02016AB8: main.sym_var("txt_lava", "u16", "[]"),
	0x020144F0: main.sym_var("gfx_quad0", "Gfx", "[]", flag={"GLOBL"}),
	0x02014548: main.sym_var("gfx_shadow_circle", "Gfx", "[]", flag={"GLOBL"}),
	0x02014590: main.sym_var("gfx_shadow_square", "Gfx", "[]", flag={"GLOBL"}),
	0x020145D8: main.sym_var("gfx_shadow_9", "Gfx", "[]", flag={"GLOBL"}),
	0x02014620: main.sym_var("gfx_shadow_4", "Gfx", "[]", flag={"GLOBL"}),
	0x02014638: main.sym_var("gfx_shadow_end", "Gfx", "[]", flag={"GLOBL"}),
	0x02014660: main.sym_var("gfx_wipe_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x02014698: main.sym_var("gfx_wipe_end", "Gfx", "[]", flag={"GLOBL"}),
	0x020146C0: main.sym_var("gfx_wipe_draw", "Gfx", "[]", flag={"GLOBL"}),
	0x02014708: main.sym_var("gfx_background_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x02014738: main.sym_var("gfx_background_tile", "Gfx", "[]", flag={"GLOBL"}),
	0x02014768: main.sym_var("gfx_background_end", "Gfx", "[]", flag={"GLOBL"}),
	0x02014790: main.sym_var("gfx_water_rgba", "Gfx", "[]", flag={"GLOBL"}),
	0x020147D0: main.sym_var("gfx_water_ia", "Gfx", "[]", flag={"GLOBL"}),
	0x02014810: main.sym_var("gfx_water_end", "Gfx", "[]", flag={"GLOBL"}),
	0x02014970: main.sym_var("gfx_wave_s_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x020149A8: main.sym_var("gfx_wave_s_end", "Gfx", "[]", flag={"GLOBL"}),
	0x020149C8: main.sym_var("gfx_wave_e_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x02014A00: main.sym_var("gfx_wave_e_end", "Gfx", "[]", flag={"GLOBL"}),
	0x02014A30: main.sym_var("gfx_wave_draw", "Gfx", "[]", flag={"GLOBL"}),
	0x02014A60: main.sym_var("wave_meshdata", "short", "[]", flag={"GLOBL"}),
	0x02015444: main.sym_var("wave_normdata", "short", "[]", flag={"GLOBL"}),
}

sym_E0_Gfx = {
	0x02000000: main.sym_var("txt_glbfont_0", "static u16", "[]"),
	0x02000200: main.sym_var("txt_glbfont_1", "static u16", "[]"),
	0x02000400: main.sym_var("txt_glbfont_2", "static u16", "[]"),
	0x02000600: main.sym_var("txt_glbfont_3", "static u16", "[]"),
	0x02000800: main.sym_var("txt_glbfont_4", "static u16", "[]"),
	0x02000A00: main.sym_var("txt_glbfont_5", "static u16", "[]"),
	0x02000C00: main.sym_var("txt_glbfont_6", "static u16", "[]"),
	0x02000E00: main.sym_var("txt_glbfont_7", "static u16", "[]"),
	0x02001000: main.sym_var("txt_glbfont_8", "static u16", "[]"),
	0x02001200: main.sym_var("txt_glbfont_9", "static u16", "[]"),
	0x02001400: main.sym_var("txt_glbfont_a", "static u16", "[]"),
	0x02001600: main.sym_var("txt_glbfont_b", "static u16", "[]"),
	0x02001800: main.sym_var("txt_glbfont_c", "static u16", "[]"),
	0x02001A00: main.sym_var("txt_glbfont_d", "static u16", "[]"),
	0x02001C00: main.sym_var("txt_glbfont_e", "static u16", "[]"),
	0x02001E00: main.sym_var("txt_glbfont_f", "static u16", "[]"),
	0x02002000: main.sym_var("txt_glbfont_g", "static u16", "[]"),
	0x02002200: main.sym_var("txt_glbfont_h", "static u16", "[]"),
	0x02002400: main.sym_var("txt_glbfont_i", "static u16", "[]"),
	0x02002600: main.sym_var("txt_glbfont_k", "static u16", "[]"),
	0x02002800: main.sym_var("txt_glbfont_l", "static u16", "[]"),
	0x02002A00: main.sym_var("txt_glbfont_m", "static u16", "[]"),
	0x02002C00: main.sym_var("txt_glbfont_n", "static u16", "[]"),
	0x02002E00: main.sym_var("txt_glbfont_o", "static u16", "[]"),
	0x02003000: main.sym_var("txt_glbfont_p", "static u16", "[]"),
	0x02003200: main.sym_var("txt_glbfont_r", "static u16", "[]"),
	0x02003400: main.sym_var("txt_glbfont_s", "static u16", "[]"),
	0x02003600: main.sym_var("txt_glbfont_t", "static u16", "[]"),
	0x02003800: main.sym_var("txt_glbfont_u", "static u16", "[]"),
	0x02003A00: main.sym_var("txt_glbfont_w", "static u16", "[]"),
	0x02003C00: main.sym_var("txt_glbfont_y", "static u16", "[]"),
	0x02003E00: main.sym_var("txt_glbfont_squote", "static u16", "[]"),
	0x02004000: main.sym_var("txt_glbfont_dquote", "static u16", "[]"),
	0x02004200: main.sym_var("txt_glbfont_cross", "static u16", "[]"),
	0x02004400: main.sym_var("txt_glbfont_coin", "static u16", "[]"),
	0x02004600: main.sym_var("txt_glbfont_mario", "static u16", "[]"),
	0x02004800: main.sym_var("txt_glbfont_star", "static u16", "[]"),
	0x02004A00: main.sym_var("txt_staff_3", "static u16", "[]"),
	0x02004A80: main.sym_var("txt_staff_4", "static u16", "[]"),
	0x02004B00: main.sym_var("txt_staff_6", "static u16", "[]"),
	0x02004B80: main.sym_var("txt_staff_a", "static u16", "[]"),
	0x02004C00: main.sym_var("txt_staff_b", "static u16", "[]"),
	0x02004C80: main.sym_var("txt_staff_c", "static u16", "[]"),
	0x02004D00: main.sym_var("txt_staff_d", "static u16", "[]"),
	0x02004D80: main.sym_var("txt_staff_e", "static u16", "[]"),
	0x02004E00: main.sym_var("txt_staff_f", "static u16", "[]"),
	0x02004E80: main.sym_var("txt_staff_g", "static u16", "[]"),
	0x02004F00: main.sym_var("txt_staff_h", "static u16", "[]"),
	0x02004F80: main.sym_var("txt_staff_i", "static u16", "[]"),
	0x02005000: main.sym_var("txt_staff_j", "static u16", "[]"),
	0x02005080: main.sym_var("txt_staff_k", "static u16", "[]"),
	0x02005100: main.sym_var("txt_staff_l", "static u16", "[]"),
	0x02005180: main.sym_var("txt_staff_m", "static u16", "[]"),
	0x02005200: main.sym_var("txt_staff_n", "static u16", "[]"),
	0x02005280: main.sym_var("txt_staff_o", "static u16", "[]"),
	0x02005300: main.sym_var("txt_staff_p", "static u16", "[]"),
	0x02005380: main.sym_var("txt_staff_q", "static u16", "[]"),
	0x02005400: main.sym_var("txt_staff_r", "static u16", "[]"),
	0x02005480: main.sym_var("txt_staff_s", "static u16", "[]"),
	0x02005500: main.sym_var("txt_staff_t", "static u16", "[]"),
	0x02005580: main.sym_var("txt_staff_u", "static u16", "[]"),
	0x02005600: main.sym_var("txt_staff_v", "static u16", "[]"),
	0x02005680: main.sym_var("txt_staff_w", "static u16", "[]"),
	0x02005700: main.sym_var("txt_staff_x", "static u16", "[]"),
	0x02005780: main.sym_var("txt_staff_y", "static u16", "[]"),
	0x02005800: main.sym_var("txt_staff_z", "static u16", "[]"),
	0x02005880: main.sym_var("txt_staff_period", "static u16", "[]"),
	0x02005900: main.sym_var("txt_lgfont_0", "static u8", "[]"),
	0x02005940: main.sym_var("txt_lgfont_1", "static u8", "[]"),
	0x02005980: main.sym_var("txt_lgfont_2", "static u8", "[]"),
	0x020059C0: main.sym_var("txt_lgfont_3", "static u8", "[]"),
	0x02005A00: main.sym_var("txt_lgfont_4", "static u8", "[]"),
	0x02005A40: main.sym_var("txt_lgfont_5", "static u8", "[]"),
	0x02005A80: main.sym_var("txt_lgfont_6", "static u8", "[]"),
	0x02005AC0: main.sym_var("txt_lgfont_7", "static u8", "[]"),
	0x02005B00: main.sym_var("txt_lgfont_8", "static u8", "[]"),
	0x02005B40: main.sym_var("txt_lgfont_9", "static u8", "[]"),
	0x02005B80: main.sym_var("txt_lgfont_upper_a", "static u8", "[]"),
	0x02005BC0: main.sym_var("txt_lgfont_upper_b", "static u8", "[]"),
	0x02005C00: main.sym_var("txt_lgfont_upper_c", "static u8", "[]"),
	0x02005C40: main.sym_var("txt_lgfont_upper_d", "static u8", "[]"),
	0x02005C80: main.sym_var("txt_lgfont_upper_e", "static u8", "[]"),
	0x02005CC0: main.sym_var("txt_lgfont_upper_f", "static u8", "[]"),
	0x02005D00: main.sym_var("txt_lgfont_upper_g", "static u8", "[]"),
	0x02005D40: main.sym_var("txt_lgfont_upper_h", "static u8", "[]"),
	0x02005D80: main.sym_var("txt_lgfont_upper_i", "static u8", "[]"),
	0x02005DC0: main.sym_var("txt_lgfont_upper_j", "static u8", "[]"),
	0x02005E00: main.sym_var("txt_lgfont_upper_k", "static u8", "[]"),
	0x02005E40: main.sym_var("txt_lgfont_upper_l", "static u8", "[]"),
	0x02005E80: main.sym_var("txt_lgfont_upper_m", "static u8", "[]"),
	0x02005EC0: main.sym_var("txt_lgfont_upper_n", "static u8", "[]"),
	0x02005F00: main.sym_var("txt_lgfont_upper_o", "static u8", "[]"),
	0x02005F40: main.sym_var("txt_lgfont_upper_p", "static u8", "[]"),
	0x02005F80: main.sym_var("txt_lgfont_upper_q", "static u8", "[]"),
	0x02005FC0: main.sym_var("txt_lgfont_upper_r", "static u8", "[]"),
	0x02006000: main.sym_var("txt_lgfont_upper_s", "static u8", "[]"),
	0x02006040: main.sym_var("txt_lgfont_upper_t", "static u8", "[]"),
	0x02006080: main.sym_var("txt_lgfont_upper_u", "static u8", "[]"),
	0x020060C0: main.sym_var("txt_lgfont_upper_v", "static u8", "[]"),
	0x02006100: main.sym_var("txt_lgfont_upper_w", "static u8", "[]"),
	0x02006140: main.sym_var("txt_lgfont_upper_x", "static u8", "[]"),
	0x02006180: main.sym_var("txt_lgfont_upper_y", "static u8", "[]"),
	0x020061C0: main.sym_var("txt_lgfont_upper_z", "static u8", "[]"),
	0x02006200: main.sym_var("txt_lgfont_lower_a", "static u8", "[]"),
	0x02006240: main.sym_var("txt_lgfont_lower_b", "static u8", "[]"),
	0x02006280: main.sym_var("txt_lgfont_lower_c", "static u8", "[]"),
	0x020062C0: main.sym_var("txt_lgfont_lower_d", "static u8", "[]"),
	0x02006300: main.sym_var("txt_lgfont_lower_e", "static u8", "[]"),
	0x02006340: main.sym_var("txt_lgfont_lower_f", "static u8", "[]"),
	0x02006380: main.sym_var("txt_lgfont_lower_g", "static u8", "[]"),
	0x020063C0: main.sym_var("txt_lgfont_lower_h", "static u8", "[]"),
	0x02006400: main.sym_var("txt_lgfont_lower_i", "static u8", "[]"),
	0x02006440: main.sym_var("txt_lgfont_lower_j", "static u8", "[]"),
	0x02006480: main.sym_var("txt_lgfont_lower_k", "static u8", "[]"),
	0x020064C0: main.sym_var("txt_lgfont_lower_l", "static u8", "[]"),
	0x02006500: main.sym_var("txt_lgfont_lower_m", "static u8", "[]"),
	0x02006540: main.sym_var("txt_lgfont_lower_n", "static u8", "[]"),
	0x02006580: main.sym_var("txt_lgfont_lower_o", "static u8", "[]"),
	0x020065C0: main.sym_var("txt_lgfont_lower_p", "static u8", "[]"),
	0x02006600: main.sym_var("txt_lgfont_lower_q", "static u8", "[]"),
	0x02006640: main.sym_var("txt_lgfont_lower_r", "static u8", "[]"),
	0x02006680: main.sym_var("txt_lgfont_lower_s", "static u8", "[]"),
	0x020066C0: main.sym_var("txt_lgfont_lower_t", "static u8", "[]"),
	0x02006700: main.sym_var("txt_lgfont_lower_u", "static u8", "[]"),
	0x02006740: main.sym_var("txt_lgfont_lower_v", "static u8", "[]"),
	0x02006780: main.sym_var("txt_lgfont_lower_w", "static u8", "[]"),
	0x020067C0: main.sym_var("txt_lgfont_lower_x", "static u8", "[]"),
	0x02006800: main.sym_var("txt_lgfont_lower_y", "static u8", "[]"),
	0x02006840: main.sym_var("txt_lgfont_lower_z", "static u8", "[]"),
	0x02006880: main.sym_var("txt_lgfont_arrow", "static u8", "[]"),
	0x020068C0: main.sym_var("txt_lgfont_bang", "static u8", "[]"),
	0x02006900: main.sym_var("txt_lgfont_coin", "static u8", "[]"),
	0x02006940: main.sym_var("txt_lgfont_cross", "static u8", "[]"),
	0x02006980: main.sym_var("txt_lgfont_lparen", "static u8", "[]"),
	0x020069C0: main.sym_var("txt_lgfont_rlparen", "static u8", "[]"),
	0x02006A00: main.sym_var("txt_lgfont_rparen", "static u8", "[]"),
	0x02006A40: main.sym_var("txt_lgfont_tilde", "static u8", "[]"),
	0x02006A80: main.sym_var("txt_lgfont_period", "static u8", "[]"),
	0x02006AC0: main.sym_var("txt_lgfont_percent", "static u8", "[]"),
	0x02006B00: main.sym_var("txt_lgfont_bullet", "static u8", "[]"),
	0x02006B40: main.sym_var("txt_lgfont_comma", "static u8", "[]"),
	0x02006B80: main.sym_var("txt_lgfont_apostrophe", "static u8", "[]"),
	0x02006BC0: main.sym_var("txt_lgfont_question", "static u8", "[]"),
	0x02006C00: main.sym_var("txt_lgfont_star", "static u8", "[]"),
	0x02006C40: main.sym_var("txt_lgfont_nostar", "static u8", "[]"),
	0x02006C80: main.sym_var("txt_lgfont_lquote", "static u8", "[]"),
	0x02006CC0: main.sym_var("txt_lgfont_rquote", "static u8", "[]"),
	0x02006D00: main.sym_var("txt_lgfont_colon", "static u8", "[]"),
	0x02006D40: main.sym_var("txt_lgfont_hyphen", "static u8", "[]"),
	0x02006D80: main.sym_var("txt_lgfont_ampersand", "static u8", "[]"),
	0x02006DC0: main.sym_var("txt_lgfont_ba", "static u8", "[]"),
	0x02006E00: main.sym_var("txt_lgfont_bb", "static u8", "[]"),
	0x02006E40: main.sym_var("txt_lgfont_bc", "static u8", "[]"),
	0x02006E80: main.sym_var("txt_lgfont_bz", "static u8", "[]"),
	0x02006EC0: main.sym_var("txt_lgfont_br", "static u8", "[]"),
	0x02006F00: main.sym_var("txt_lgfont_cu", "static u8", "[]"),
	0x02006F40: main.sym_var("txt_lgfont_cd", "static u8", "[]"),
	0x02006F80: main.sym_var("txt_lgfont_cl", "static u8", "[]"),
	0x02006FC0: main.sym_var("txt_lgfont_cr", "static u8", "[]"),
	0x02007000: main.sym_var("txt_camera_camera", "static u16", "[]"),
	0x02007200: main.sym_var("txt_camera_lakitu", "static u16", "[]"),
	0x02007400: main.sym_var("txt_camera_cross", "static u16", "[]"),
	0x02007600: main.sym_var("txt_camera_up", "static u16", "[]"),
	0x02007680: main.sym_var("txt_camera_down", "static u16", "[]"),
	0x02007700: main.sym_var("txt_glbfont", "u16 *", "[]"),
	0x020077E8: main.sym_var("txt_lgfont", "u8 *", "[]"),
	0x02007BE8: main.sym_var("txt_staff", "u16 *", "[]"),
	0x02007C7C: main.sym_var("txt_camera", "u16 *", "[]"),
	0x02007D28: main.sym_var("selecttab", "MESSAGE *", "[]"),
	0x02010A68: main.sym_var("messagetab", "MESSAGE *", "[]"),
	0x02010F68: main.sym_var("coursename", "unsigned char *", "[]"),
	0x0201192C: main.sym_var("levelname", "unsigned char *", "[]"),
	0x02011AB8: main.sym_var("align_font", "UNUSED static long long"),
	0x02011AC0: main.sym_var("gfx_print_copy_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x02011AF8: main.sym_var("gfx_print_copy_char", "Gfx", "[]", flag={"GLOBL"}),
	0x02011B28: main.sym_var("gfx_print_copy_end", "Gfx", "[]", flag={"GLOBL"}),
	0x02011B60: main.sym_var("gfx_print_1cyc_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x02011B98: main.sym_var("gfx_print_1cyc_char", "Gfx", "[]", flag={"GLOBL"}),
	0x02011BC8: main.sym_var("gfx_print_1cyc_end", "Gfx", "[]", flag={"GLOBL"}),
	0x02011C08: main.sym_var("vtx_message_box", "static Vtx", "[]"),
	0x02011C48: main.sym_var("gfx_message_box", "Gfx", "[]", flag={"GLOBL"}),
	0x02011C88: main.sym_var("vtx_lgfont_char", "static Vtx", "[]"),
	0x02011CC8: main.sym_var("gfx_lgfont_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x02011D08: main.sym_var("gfx_lgfont_char", "Gfx", "[]", flag={"GLOBL"}),
	0x02011D50: main.sym_var("gfx_lgfont_end", "Gfx", "[]", flag={"GLOBL"}),
	0x02011D90: main.sym_var("vtx_message_cursor", "static Vtx", "[]"),
	0x02011DC0: main.sym_var("gfx_message_cursor", "Gfx", "[]", flag={"GLOBL"}),
	0x02011E10: main.sym_var("vtx_number", "static Vtx", "[]"),
	0x02011E50: main.sym_var("gfx_number_begin", "static Gfx", "[]"),
	0x02011E98: main.sym_var("gfx_number_end", "static Gfx", "[]"),
	0x02011ED8: main.sym_var("gfx_number_0", "Gfx", "[]", flag={"GLOBL"}),
	0x02011F08: main.sym_var("gfx_number_1", "Gfx", "[]", flag={"GLOBL"}),
	0x02011F38: main.sym_var("gfx_number_2", "Gfx", "[]", flag={"GLOBL"}),
	0x02011F68: main.sym_var("gfx_number_3", "Gfx", "[]", flag={"GLOBL"}),
	0x02011F98: main.sym_var("gfx_number_4", "Gfx", "[]", flag={"GLOBL"}),
	0x02011FC8: main.sym_var("gfx_number_5", "Gfx", "[]", flag={"GLOBL"}),
	0x02011FF8: main.sym_var("gfx_number_6", "Gfx", "[]", flag={"GLOBL"}),
	0x02012028: main.sym_var("gfx_number_7", "Gfx", "[]", flag={"GLOBL"}),
	0x02012058: main.sym_var("gfx_number_8", "Gfx", "[]", flag={"GLOBL"}),
	0x02012088: main.sym_var("gfx_number_9", "Gfx", "[]", flag={"GLOBL"}),
	0x020120B8: main.sym_var("txt_shadow_circle", "static u8", "[]"),
	0x020121B8: main.sym_var("txt_shadow_square", "static u8", "[]"),
	0x020122B8: main.sym_var("txt_wipe_star", "u8", "[]"),
	0x02012AB8: main.sym_var("txt_wipe_circle", "u8", "[]"),
	0x020132B8: main.sym_var("txt_wipe_mario", "u8", "[]"),
	0x020142B8: main.sym_var("txt_wipe_bowser", "u8", "[]"),
	0x02014AB8: main.sym_var("txt_water_0", "u16", "[]"),
	0x020152B8: main.sym_var("txt_water_1", "u16", "[]"),
	0x02015AB8: main.sym_var("txt_water_2", "u16", "[]"),
	0x020162B8: main.sym_var("txt_mist", "u16", "[]"),
	0x02016AB8: main.sym_var("txt_lava", "u16", "[]"),
	0x020172B8: main.sym_var("light_unused", "UNUSED static Lights1"), # unused
	0x020172D0: main.sym_var("mtx_identity", "static Mtx"),
	0x02017310: main.sym_var("mtx_ortho", "static Mtx"),
	0x02017350: main.sym_var("gfx_quad0", "Gfx", "[]", flag={"GLOBL"}),
	0x02017368: main.sym_var("gfx_quad1", "Gfx", "[]", flag={"GLOBL"}), # unused
	0x02017380: main.sym_var("gfx_shadow_begin", "static Gfx", "[]"),
	0x020173A8: main.sym_var("gfx_shadow_circle", "Gfx", "[]", flag={"GLOBL"}),
	0x020173F0: main.sym_var("gfx_shadow_square", "Gfx", "[]", flag={"GLOBL"}),
	0x02017438: main.sym_var("gfx_shadow_9", "Gfx", "[]", flag={"GLOBL"}),
	0x02017480: main.sym_var("gfx_shadow_4", "Gfx", "[]", flag={"GLOBL"}),
	0x02017498: main.sym_var("gfx_shadow_end", "Gfx", "[]", flag={"GLOBL"}),
	0x020174C0: main.sym_var("gfx_wipe_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x020174F8: main.sym_var("gfx_wipe_end", "Gfx", "[]", flag={"GLOBL"}),
	0x02017520: main.sym_var("gfx_wipe_draw", "Gfx", "[]", flag={"GLOBL"}),
	0x02017568: main.sym_var("gfx_background_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x02017598: main.sym_var("gfx_background_tile", "Gfx", "[]", flag={"GLOBL"}),
	0x020175C8: main.sym_var("gfx_background_end", "Gfx", "[]", flag={"GLOBL"}),
	0x020175F0: main.sym_var("gfx_water_rgba", "Gfx", "[]", flag={"GLOBL"}),
	0x02017630: main.sym_var("gfx_water_ia", "Gfx", "[]", flag={"GLOBL"}),
	0x02017670: main.sym_var("gfx_water_end", "Gfx", "[]", flag={"GLOBL"}),
	0x02017698: main.sym_var("txt_minimap_arrow", "static u8", "[]"),
	0x020176D8: main.sym_var("gfx_minimap_begin", "Gfx", "[]"), # unused
	0x02017710: main.sym_var("gfx_minimap_tile", "Gfx", "[]"), # unused
	0x02017740: main.sym_var("gfx_minimap_arrow", "Gfx", "[]"), # unused
	0x02017798: main.sym_var("gfx_minimap_end", "Gfx", "[]"), # unused
	0x020177B8: main.sym_var("light_wave", "static Lights1"),
	0x020177D0: main.sym_var("gfx_wave_s_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x02017808: main.sym_var("gfx_wave_s_end", "Gfx", "[]", flag={"GLOBL"}),
	0x02017828: main.sym_var("gfx_wave_e_begin", "Gfx", "[]", flag={"GLOBL"}),
	0x02017860: main.sym_var("gfx_wave_e_end", "Gfx", "[]", flag={"GLOBL"}),
	0x02017890: main.sym_var("gfx_wave_draw", "Gfx", "[]", flag={"GLOBL"}),
	0x020178C0: main.sym_var("wave_meshdata", "short", "[]", flag={"GLOBL"}),
	0x020182A4: main.sym_var("wave_normdata", "short", "[]", flag={"GLOBL"}),
}
