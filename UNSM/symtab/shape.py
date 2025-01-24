import main

sym_E0_Player = {
	0x00114750: main.sym("_PlayerGfxSegmentRomStart"),
	0x001279B0: main.sym("_PlayerShpSegmentRomStart"),

	# mario
	0x04000000: main.sym_var("light_mario", "static Lights1", "[]"),
	0x04000090: main.sym_var("txt_mario_metal", "static u16", "[]"),
	0x04001090: main.sym_var("txt_mario_button", "static u16", "[]"),
	0x04001890: main.sym_var("txt_mario_logo", "static u16", "[]"),
	0x04002090: main.sym_var("txt_mario_sideburn", "static u16", "[]"),
	0x04002890: main.sym_var("txt_mario_moustache", "static u16", "[]"),
	0x04003090: main.sym_var("txt_mario_eyes_open", "static u16", "[]"),
	0x04003890: main.sym_var("txt_mario_eyes_half", "static u16", "[]"),
	0x04004090: main.sym_var("txt_mario_eyes_closed", "static u16", "[]"),
	0x04005890: main.sym_var("txt_mario_eyes_left", "static u16", "[]"),
	0x04006090: main.sym_var("txt_mario_eyes_right", "static u16", "[]"),
	0x04006890: main.sym_var("txt_mario_eyes_up", "static u16", "[]"),
	0x04007090: main.sym_var("txt_mario_eyes_down", "static u16", "[]"),
	0x04007890: main.sym_var("txt_mario_eyes_dead", "static u16", "[]"),
	0x04008090: main.sym_var("txt_mario_wing_l", "static u16", "[]"),
	0x04009090: main.sym_var("txt_mario_wing_r", "static u16", "[]"),
	0x0400A090: main.sym_var("txt_mario_metal_wing_l", "static u16", "[]"),
	0x0400B090: main.sym_var("txt_mario_metal_wing_r", "static u16", "[]"),
	0x0400CA00: main.sym_var("gfx_mario_h_waist", "static Gfx", "[]"),
	0x0400CC98: main.sym_var("gfx_mario_h_waist_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0400CCC8: main.sym_var("gfx_mario_h_waist_e", "Gfx", "[]", flag={"GLOBL"}),
	0x0400D090: main.sym_var("gfx_mario_h_uarmL", "Gfx", "[]", flag={"GLOBL"}),
	0x0400D1D8: main.sym_var("gfx_mario_h_uarmL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0400D2F8: main.sym_var("gfx_mario_h_larmL", "Gfx", "[]", flag={"GLOBL"}),
	0x0400D758: main.sym_var("gfx_mario_h_fistL", "Gfx", "[]", flag={"GLOBL"}),
	0x0400D8F0: main.sym_var("gfx_mario_h_fistL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0400DCA0: main.sym_var("gfx_mario_h_uarmR", "Gfx", "[]", flag={"GLOBL"}),
	0x0400DDE8: main.sym_var("gfx_mario_h_uarmR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0400DF08: main.sym_var("gfx_mario_h_larmR", "Gfx", "[]", flag={"GLOBL"}),
	0x0400E2C8: main.sym_var("gfx_mario_h_fistR", "static Gfx", "[]"),
	0x0400E458: main.sym_var("gfx_mario_h_fistR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0400E478: main.sym_var("gfx_mario_h_fistR_e", "Gfx", "[]", flag={"GLOBL"}),
	0x0400E6A8: main.sym_var("gfx_mario_h_thighL", "static Gfx", "[]"),
	0x0400E7B0: main.sym_var("gfx_mario_h_thighL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0400E7E0: main.sym_var("gfx_mario_h_thighL_e", "Gfx", "[]", flag={"GLOBL"}),
	0x0400E918: main.sym_var("gfx_mario_h_shinL", "Gfx", "[]", flag={"GLOBL"}),
	0x0400EBB8: main.sym_var("gfx_mario_h_shoeL", "Gfx", "[]", flag={"GLOBL"}),
	0x0400ECA0: main.sym_var("gfx_mario_h_shoeL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0400EEB0: main.sym_var("gfx_mario_h_thighR", "Gfx", "[]", flag={"GLOBL"}),
	0x0400EFB8: main.sym_var("gfx_mario_h_thighR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0400F1D8: main.sym_var("gfx_mario_h_shinR", "Gfx", "[]", flag={"GLOBL"}),
	0x0400F400: main.sym_var("gfx_mario_h_shoeR", "static Gfx", "[]"),
	0x0400F4E8: main.sym_var("gfx_mario_h_shoeR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0400F528: main.sym_var("gfx_mario_h_shoeR_e", "Gfx", "[]", flag={"GLOBL"}),
	0x0400FF28: main.sym_var("gfx_mario_h_torso_button", "static Gfx", "[]"),
	0x0400FF88: main.sym_var("gfx_mario_h_torso_blue", "static Gfx", "[]"),
	0x04010260: main.sym_var("gfx_mario_h_torso_red", "static Gfx", "[]"),
	0x04010348: main.sym_var("gfx_mario_h_torso_shade", "static Gfx", "[]"),
	0x04010370: main.sym_var("gfx_mario_h_torso_s", "Gfx", "[]", flag={"GLOBL"}),
	0x040103F0: main.sym_var("gfx_mario_h_torso", "Gfx", "[]", flag={"GLOBL"}),
	0x040112B0: main.sym_var("gfx_mario_h_cap_logo", "static Gfx", "[]"),
	0x040112E8: main.sym_var("gfx_mario_h_cap_eyes", "static Gfx", "[]"),
	0x04011350: main.sym_var("gfx_mario_h_cap_sideburn", "static Gfx", "[]"),
	0x040113A0: main.sym_var("gfx_mario_h_cap_moustache", "static Gfx", "[]"),
	0x04011438: main.sym_var("gfx_mario_h_cap_skin", "static Gfx", "[]"),
	0x040116F8: main.sym_var("gfx_mario_h_cap_red", "static Gfx", "[]"),
	0x04011870: main.sym_var("gfx_mario_h_cap_hair", "static Gfx", "[]"),
	0x04011960: main.sym_var("gfx_mario_h_cap_shade", "static Gfx", "[]"),
	0x040119A0: main.sym_var("gfx_mario_h_cap_open", "Gfx", "[]", flag={"GLOBL"}),
	0x04011A90: main.sym_var("gfx_mario_h_cap_half", "Gfx", "[]", flag={"GLOBL"}),
	0x04011B80: main.sym_var("gfx_mario_h_cap_closed", "Gfx", "[]", flag={"GLOBL"}),
	0x04011C70: main.sym_var("gfx_mario_h_cap_left", "Gfx", "[]", flag={"GLOBL"}),
	0x04011D60: main.sym_var("gfx_mario_h_cap_right", "Gfx", "[]", flag={"GLOBL"}),
	0x04011E50: main.sym_var("gfx_mario_h_cap_up", "Gfx", "[]", flag={"GLOBL"}),
	0x04011F40: main.sym_var("gfx_mario_h_cap_down", "Gfx", "[]", flag={"GLOBL"}),
	0x04012030: main.sym_var("gfx_mario_h_cap_dead", "Gfx", "[]", flag={"GLOBL"}),
	0x04012120: main.sym_var("gfx_mario_h_cap", "Gfx", "[]", flag={"GLOBL"}),
	0x04012160: main.sym_var("light_mario_old", "UNUSED static Lights1", "[]"),
	0x040132B0: main.sym_var("gfx_mario_h_hair_eyes", "static Gfx", "[]"),
	0x04013318: main.sym_var("gfx_mario_h_hair_moustache", "static Gfx", "[]"),
	0x040133A8: main.sym_var("gfx_mario_h_hair_sideburn", "static Gfx", "[]"),
	0x040133F8: main.sym_var("gfx_mario_h_hair_skin", "static Gfx", "[]"),
	0x040136D0: main.sym_var("gfx_mario_h_hair_hair", "static Gfx", "[]"),
	0x040139C0: main.sym_var("gfx_mario_h_hair_shade", "static Gfx", "[]"),
	0x040139E8: main.sym_var("gfx_mario_h_hair_open", "Gfx", "[]", flag={"GLOBL"}),
	0x04013AB8: main.sym_var("gfx_mario_h_hair_half", "Gfx", "[]", flag={"GLOBL"}),
	0x04013B88: main.sym_var("gfx_mario_h_hair_closed", "Gfx", "[]", flag={"GLOBL"}),
	0x04013C58: main.sym_var("gfx_mario_h_hair_left", "Gfx", "[]", flag={"GLOBL"}),
	0x04013D28: main.sym_var("gfx_mario_h_hair_right", "Gfx", "[]", flag={"GLOBL"}),
	0x04013DF8: main.sym_var("gfx_mario_h_hair_up", "Gfx", "[]", flag={"GLOBL"}),
	0x04013EC8: main.sym_var("gfx_mario_h_hair_down", "Gfx", "[]", flag={"GLOBL"}),
	0x04013F98: main.sym_var("gfx_mario_h_hair_dead", "Gfx", "[]", flag={"GLOBL"}),
	0x04014068: main.sym_var("gfx_mario_h_hair", "Gfx", "[]", flag={"GLOBL"}),
	0x040144D8: main.sym_var("gfx_mario_m_waist", "static Gfx", "[]"),
	0x04014638: main.sym_var("gfx_mario_m_waist_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04014668: main.sym_var("gfx_mario_m_waist_e", "Gfx", "[]", flag={"GLOBL"}),
	0x040147D0: main.sym_var("gfx_mario_m_uarmL", "Gfx", "[]", flag={"GLOBL"}),
	0x04014840: main.sym_var("gfx_mario_m_uarmL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04014950: main.sym_var("gfx_mario_m_larmL", "Gfx", "[]", flag={"GLOBL"}),
	0x04014C90: main.sym_var("gfx_mario_m_fistL", "Gfx", "[]", flag={"GLOBL"}),
	0x04014DC0: main.sym_var("gfx_mario_m_fistL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04014ED0: main.sym_var("gfx_mario_m_uarmR", "Gfx", "[]", flag={"GLOBL"}),
	0x04014F40: main.sym_var("gfx_mario_m_uarmR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04015050: main.sym_var("gfx_mario_m_larmR", "Gfx", "[]", flag={"GLOBL"}),
	0x040153B0: main.sym_var("gfx_mario_m_fistR", "Gfx", "[]", flag={"GLOBL"}),
	0x040154E0: main.sym_var("gfx_mario_m_fistR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04015500: main.sym_var("gfx_mario_m_fistR_e", "Gfx", "[]", flag={"GLOBL"}),
	0x04015620: main.sym_var("gfx_mario_m_thighL", "static Gfx", "[]"),
	0x040156B0: main.sym_var("gfx_mario_m_thighL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x040156E0: main.sym_var("gfx_mario_m_thighL_e", "Gfx", "[]", flag={"GLOBL"}),
	0x04015848: main.sym_var("gfx_mario_m_shinL", "Gfx", "[]", flag={"GLOBL"}),
	0x04015A98: main.sym_var("gfx_mario_m_shoeL", "Gfx", "[]", flag={"GLOBL"}),
	0x04015B60: main.sym_var("gfx_mario_m_shoeL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04015C70: main.sym_var("gfx_mario_m_thighR", "Gfx", "[]", flag={"GLOBL"}),
	0x04015D00: main.sym_var("gfx_mario_m_thighR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04015E10: main.sym_var("gfx_mario_m_shinR", "Gfx", "[]", flag={"GLOBL"}),
	0x04016000: main.sym_var("gfx_mario_m_shoeR", "static Gfx", "[]"),
	0x040160C8: main.sym_var("gfx_mario_m_shoeR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04016108: main.sym_var("gfx_mario_m_shoeR_e", "Gfx", "[]", flag={"GLOBL"}),
	0x04016668: main.sym_var("gfx_mario_m_torso_button", "static Gfx", "[]"),
	0x040166B8: main.sym_var("gfx_mario_m_torso_blue", "static Gfx", "[]"),
	0x04016800: main.sym_var("gfx_mario_m_torso_red", "static Gfx", "[]"),
	0x040168A0: main.sym_var("gfx_mario_m_torso_shade", "static Gfx", "[]"),
	0x040168C8: main.sym_var("gfx_mario_m_torso_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04016948: main.sym_var("gfx_mario_m_torso_e", "Gfx", "[]", flag={"GLOBL"}),
	0x04016A18: main.sym_var("gfx_mario_l_waist", "static Gfx", "[]"),
	0x04016AB8: main.sym_var("gfx_mario_l_waist_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04016AE8: main.sym_var("gfx_mario_l_waist_e", "Gfx", "[]", flag={"GLOBL"}),
	0x04016C20: main.sym_var("gfx_mario_l_uarmL", "Gfx", "[]", flag={"GLOBL"}),
	0x04016C70: main.sym_var("gfx_mario_l_uarmL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04016D50: main.sym_var("gfx_mario_l_larmL", "Gfx", "[]", flag={"GLOBL"}),
	0x04016E20: main.sym_var("gfx_mario_l_fistL", "Gfx", "[]", flag={"GLOBL"}),
	0x04016E80: main.sym_var("gfx_mario_l_fistL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04016F60: main.sym_var("gfx_mario_l_uarmR", "Gfx", "[]", flag={"GLOBL"}),
	0x04016FB0: main.sym_var("gfx_mario_l_uarmR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04017090: main.sym_var("gfx_mario_l_larmR", "Gfx", "[]", flag={"GLOBL"}),
	0x04017160: main.sym_var("gfx_mario_l_fistR", "static Gfx", "[]"),
	0x040171C0: main.sym_var("gfx_mario_l_fistR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x040171E0: main.sym_var("gfx_mario_l_fistR_e", "Gfx", "[]", flag={"GLOBL"}),
	0x040172F0: main.sym_var("gfx_mario_l_thighL", "static Gfx", "[]"),
	0x04017360: main.sym_var("gfx_mario_l_thighL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04017390: main.sym_var("gfx_mario_l_thighL_e", "Gfx", "[]", flag={"GLOBL"}),
	0x040174E8: main.sym_var("gfx_mario_l_shinL", "Gfx", "[]", flag={"GLOBL"}),
	0x04017638: main.sym_var("gfx_mario_l_shoeL", "Gfx", "[]", flag={"GLOBL"}),
	0x040176A8: main.sym_var("gfx_mario_l_shoeL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x040177A8: main.sym_var("gfx_mario_l_thighR", "Gfx", "[]", flag={"GLOBL"}),
	0x04017818: main.sym_var("gfx_mario_l_thighR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04017918: main.sym_var("gfx_mario_l_shinR", "Gfx", "[]", flag={"GLOBL"}),
	0x04017A68: main.sym_var("gfx_mario_l_shoeR", "static Gfx", "[]"),
	0x04017AD8: main.sym_var("gfx_mario_l_shoeR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04017B18: main.sym_var("gfx_mario_l_shoeR_e", "Gfx", "[]", flag={"GLOBL"}),
	0x04017D68: main.sym_var("gfx_mario_l_torso_button", "static Gfx", "[]"),
	0x04017D98: main.sym_var("gfx_mario_l_torso_blue", "static Gfx", "[]"),
	0x04017E20: main.sym_var("gfx_mario_l_torso_red", "static Gfx", "[]"),
	0x04017E78: main.sym_var("gfx_mario_l_torso_shade", "static Gfx", "[]"),
	0x04017EA0: main.sym_var("gfx_mario_l_torso_s", "Gfx", "[]", flag={"GLOBL"}),
	0x04017F20: main.sym_var("gfx_mario_l_torso_e", "Gfx", "[]", flag={"GLOBL"}),
	0x04018270: main.sym_var("gfx_mario_l_cap_logo", "static Gfx", "[]"),
	0x04018298: main.sym_var("gfx_mario_l_cap_eyes", "static Gfx", "[]"),
	0x040182C0: main.sym_var("gfx_mario_l_cap_moustache", "static Gfx", "[]"),
	0x04018300: main.sym_var("gfx_mario_l_cap_skin", "static Gfx", "[]"),
	0x04018370: main.sym_var("gfx_mario_l_cap_red", "static Gfx", "[]"),
	0x040183F0: main.sym_var("gfx_mario_l_cap_hair", "static Gfx", "[]"),
	0x04018420: main.sym_var("gfx_mario_l_cap_shade", "static Gfx", "[]"),
	0x04018460: main.sym_var("gfx_mario_l_cap_open", "Gfx", "[]", flag={"GLOBL"}),
	0x04018530: main.sym_var("gfx_mario_l_cap_half", "Gfx", "[]", flag={"GLOBL"}),
	0x04018600: main.sym_var("gfx_mario_l_cap_closed", "Gfx", "[]", flag={"GLOBL"}),
	0x040186D0: main.sym_var("gfx_mario_l_cap_left", "Gfx", "[]", flag={"GLOBL"}),
	0x040187A0: main.sym_var("gfx_mario_l_cap_right", "Gfx", "[]", flag={"GLOBL"}),
	0x04018870: main.sym_var("gfx_mario_l_cap_up", "Gfx", "[]", flag={"GLOBL"}),
	0x04018940: main.sym_var("gfx_mario_l_cap_down", "Gfx", "[]", flag={"GLOBL"}),
	0x04018A10: main.sym_var("gfx_mario_l_cap_dead", "Gfx", "[]", flag={"GLOBL"}),
	0x04018AE0: main.sym_var("gfx_mario_l_cap", "Gfx", "[]", flag={"GLOBL"}),
	0x04018DC8: main.sym_var("gfx_mario_l_hair_eyes", "static Gfx", "[]"),
	0x04018DF0: main.sym_var("gfx_mario_l_hair_moustache", "static Gfx", "[]"),
	0x04018E30: main.sym_var("gfx_mario_l_hair_skin", "static Gfx", "[]"),
	0x04018EA0: main.sym_var("gfx_mario_l_hair_hair", "static Gfx", "[]"),
	0x04018F68: main.sym_var("gfx_mario_l_hair_shade", "static Gfx", "[]"),
	0x04018F90: main.sym_var("gfx_mario_l_hair_open", "Gfx", "[]", flag={"GLOBL"}),
	0x04019040: main.sym_var("gfx_mario_l_hair_half", "Gfx", "[]", flag={"GLOBL"}),
	0x040190F0: main.sym_var("gfx_mario_l_hair_closed", "Gfx", "[]", flag={"GLOBL"}),
	0x040191A0: main.sym_var("gfx_mario_l_hair_left", "Gfx", "[]", flag={"GLOBL"}),
	0x04019250: main.sym_var("gfx_mario_l_hair_right", "Gfx", "[]", flag={"GLOBL"}),
	0x04019300: main.sym_var("gfx_mario_l_hair_up", "Gfx", "[]", flag={"GLOBL"}),
	0x040193B0: main.sym_var("gfx_mario_l_hair_down", "Gfx", "[]", flag={"GLOBL"}),
	0x04019460: main.sym_var("gfx_mario_l_hair_dead", "Gfx", "[]", flag={"GLOBL"}),
	0x04019510: main.sym_var("gfx_mario_l_hair", "Gfx", "[]", flag={"GLOBL"}),
	0x04019A68: main.sym_var("gfx_mario_handL", "Gfx", "[]", flag={"GLOBL"}),
	0x04019CA0: main.sym_var("gfx_mario_handL_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0401A1F0: main.sym_var("gfx_mario_handR", "static Gfx", "[]"),
	0x0401A428: main.sym_var("gfx_mario_handR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0401A448: main.sym_var("gfx_mario_handR_e", "Gfx", "[]", flag={"GLOBL"}),
	0x0401ABA8: main.sym_var("gfx_mario_capR_logo", "static Gfx", "[]"),
	0x0401ABD0: main.sym_var("gfx_mario_capR_red", "static Gfx", "[]"),
	0x0401AD40: main.sym_var("gfx_mario_capR_white", "static Gfx", "[]"),
	0x0401AED0: main.sym_var("gfx_mario_capR_hair", "static Gfx", "[]"),
	0x0401AF20: main.sym_var("gfx_mario_capR_shade", "static Gfx", "[]"),
	0x0401B080: main.sym_var("gfx_mario_wingsR_l", "static Gfx", "[]"),
	0x0401B0B0: main.sym_var("gfx_mario_wingsR_r", "static Gfx", "[]"),
	0x0401B0E0: main.sym_var("gfx_mario_wingsR_start", "static Gfx", "[]"),
	0x0401B138: main.sym_var("gfx_mario_wingsR_end", "static Gfx", "[]"),
	0x0401B158: main.sym_var("gfx_mario_capR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0401B1D8: main.sym_var("gfx_mario_wingsR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0401B230: main.sym_var("gfx_mario_capR_e", "Gfx", "[]", flag={"GLOBL"}),
	0x0401B278: main.sym_var("gfx_mario_wingsR_e", "Gfx", "[]", flag={"GLOBL"}),
	0x0401BC80: main.sym_var("gfx_mario_peaceR", "Gfx", "[]", flag={"GLOBL"}),
	0x0401BF30: main.sym_var("gfx_mario_peaceR_s", "Gfx", "[]", flag={"GLOBL"}),
	0x0401C330: main.sym_var("gfx_mario_cap_logo", "static Gfx", "[]"),
	0x0401C368: main.sym_var("gfx_mario_cap_red", "static Gfx", "[]"),
	0x0401C4C8: main.sym_var("gfx_mario_cap_hair", "static Gfx", "[]"),
	0x0401C510: main.sym_var("gfx_mario_cap_shade", "static Gfx", "[]"),
	0x0401C678: main.sym_var("gfx_mario_wings_wing_l", "static Gfx", "[]"),
	0x0401C6A8: main.sym_var("gfx_mario_wings_wing_r", "static Gfx", "[]"),
	0x0401C6D8: main.sym_var("gfx_mario_wings_start", "static Gfx", "[]"),
	0x0401C730: main.sym_var("gfx_mario_wings_end", "static Gfx", "[]"),
	0x0401C758: main.sym_var("gfx_mario_cap_s", "Gfx", "[]"), # unused
	0x0401C7E8: main.sym_var("gfx_mario_cap_e", "Gfx", "[]"), # unused
	0x0401C890: main.sym_var("gfx_mario_wings_s", "Gfx", "[]"), # unused
	0x0401C8E8: main.sym_var("gfx_mario_wings_e", "Gfx", "[]"), # unused
	0x0401C9C0: main.sym_var("gfx_mario_wing_wing_l", "static Gfx", "[]"),
	0x0401C9E0: main.sym_var("gfx_mario_wing_wing_r", "static Gfx", "[]"),
	0x0401CA00: main.sym_var("gfx_mario_wing_so", "Gfx", "[]", flag={"GLOBL"}),
	0x0401CAB8: main.sym_var("gfx_mario_wing_sx", "Gfx", "[]", flag={"GLOBL"}),
	0x0401CB70: main.sym_var("gfx_mario_wing_eo", "Gfx", "[]", flag={"GLOBL"}),
	0x0401CC28: main.sym_var("gfx_mario_wing_ex", "Gfx", "[]", flag={"GLOBL"}),

	# bubble
	0x0401CD20: main.sym_var("vtx_bubble", "static Vtx", "[]"),
	0x0401CD60: main.sym_var("txt_bubble_a", "static u16", "[]"),
	0x0401D560: main.sym_var("txt_bubble_b", "static u16", "[]"),
	0x0401DD60: main.sym_var("gfx_bubble_a", "Gfx", "[]", flag={"GLOBL"}),
	0x0401DDE0: main.sym_var("gfx_bubble_b", "Gfx", "[]", flag={"GLOBL"}),

	# dust
	0x0401DE60: main.sym_var("vtx_dust", "static Vtx", "[]"),
	0x0401DEA0: main.sym_var("txt_dust_0", "static u16", "[]"),
	0x0401E6A0: main.sym_var("txt_dust_1", "static u16", "[]"),
	0x0401EEA0: main.sym_var("txt_dust_2", "static u16", "[]"),
	0x0401F6A0: main.sym_var("txt_dust_3", "static u16", "[]"),
	0x0401FEA0: main.sym_var("txt_dust_4", "static u16", "[]"),
	0x040206A0: main.sym_var("txt_dust_5", "static u16", "[]"),
	0x04020EA0: main.sym_var("txt_dust_6", "static u16", "[]"),
	0x040216A0: main.sym_var("gfx_dust", "static Gfx", "[]"),
	0x04021718: main.sym_var("gfx_dust_0", "Gfx", "[]", flag={"GLOBL"}),
	0x04021730: main.sym_var("gfx_dust_1", "Gfx", "[]", flag={"GLOBL"}),
	0x04021748: main.sym_var("gfx_dust_2", "Gfx", "[]", flag={"GLOBL"}),
	0x04021760: main.sym_var("gfx_dust_3", "Gfx", "[]", flag={"GLOBL"}),
	0x04021778: main.sym_var("gfx_dust_4", "Gfx", "[]", flag={"GLOBL"}),
	0x04021790: main.sym_var("gfx_dust_5", "Gfx", "[]", flag={"GLOBL"}),
	0x040217A8: main.sym_var("gfx_dust_6", "Gfx", "[]", flag={"GLOBL"}),

	# smoke
	0x040217C0: main.sym_var("vtx_smoke", "static Vtx", "[]"),
	0x04021800: main.sym_var("txt_smoke", "static u16", "[]"),
	0x04022000: main.sym_var("gfx_smoke_start", "static Gfx", "[]"),
	0x04022028: main.sym_var("gfx_smoke_smoke", "static Gfx", "[]"),
	0x04022048: main.sym_var("gfx_smoke_end", "static Gfx", "[]"),
	0x04022070: main.sym_var("gfx_smoke", "Gfx", "[]", flag={"GLOBL"}),

	# wave
	0x040220C8: main.sym_var("vtx_wave", "static Vtx", "[]"),
	0x04022108: main.sym_var("vtx_wave_red", "static Vtx", "[]"),
	0x04022148: main.sym_var("txt_wave_0", "static u16", "[]"),
	0x04022948: main.sym_var("txt_wave_1", "static u16", "[]"),
	0x04023148: main.sym_var("txt_wave_2", "static u16", "[]"),
	0x04023948: main.sym_var("txt_wave_3", "static u16", "[]"),
	0x04024148: main.sym_var("txt_wave_4", "static u16", "[]"),
	0x04024948: main.sym_var("txt_wave_5", "static u16", "[]"),
	0x04025148: main.sym_var("gfx_wave_start", "static Gfx", "[]"),
	0x04025190: main.sym_var("gfx_wave_end", "static Gfx", "[]"),
	0x040251C8: main.sym_var("gfx_wave", "static Gfx", "[]"),
	0x040251E0: main.sym_var("gfx_wave_red", "static Gfx", "[]"),
	0x040251F8: main.sym_var("gfx_wave_0", "Gfx", "[]", flag={"GLOBL"}),
	0x04025210: main.sym_var("gfx_wave_1", "Gfx", "[]", flag={"GLOBL"}),
	0x04025228: main.sym_var("gfx_wave_2", "Gfx", "[]", flag={"GLOBL"}),
	0x04025240: main.sym_var("gfx_wave_3", "Gfx", "[]", flag={"GLOBL"}),
	0x04025258: main.sym_var("gfx_wave_4", "Gfx", "[]", flag={"GLOBL"}),
	0x04025270: main.sym_var("gfx_wave_5", "Gfx", "[]", flag={"GLOBL"}),
	0x04025288: main.sym_var("gfx_wave_red_0", "Gfx", "[]", flag={"GLOBL"}),
	0x040252A0: main.sym_var("gfx_wave_red_1", "Gfx", "[]", flag={"GLOBL"}),
	0x040252B8: main.sym_var("gfx_wave_red_2", "Gfx", "[]", flag={"GLOBL"}),
	0x040252D0: main.sym_var("gfx_wave_red_3", "Gfx", "[]", flag={"GLOBL"}),
	0x040252E8: main.sym_var("gfx_wave_red_4", "Gfx", "[]", flag={"GLOBL"}),
	0x04025300: main.sym_var("gfx_wave_red_5", "Gfx", "[]", flag={"GLOBL"}),

	# ripple
	0x04025318: main.sym_var("vtx_ripple", "static Vtx", "[]"),
	0x04025358: main.sym_var("txt_ripple_0", "static u16", "[]"),
	0x04025B58: main.sym_var("txt_ripple_1", "static u16", "[]"),
	0x04026358: main.sym_var("txt_ripple_2", "static u16", "[]"),
	0x04026B58: main.sym_var("txt_ripple_3", "static u16", "[]"),
	0x04027358: main.sym_var("gfx_ripple_start", "static Gfx", "[]"),
	0x040273A0: main.sym_var("gfx_ripple_end", "static Gfx", "[]"),
	0x040273D8: main.sym_var("gfx_ripple", "static Gfx", "[]"),
	0x040273F0: main.sym_var("gfx_ripple_0", "Gfx", "[]", flag={"GLOBL"}),
	0x04027408: main.sym_var("gfx_ripple_1", "Gfx", "[]", flag={"GLOBL"}),
	0x04027420: main.sym_var("gfx_ripple_2", "Gfx", "[]", flag={"GLOBL"}),
	0x04027438: main.sym_var("gfx_ripple_3", "Gfx", "[]", flag={"GLOBL"}),

	# sparkle
	0x04027450: main.sym_var("vtx_sparkle", "static Vtx", "[]"),
	0x04027490: main.sym_var("txt_sparkle_0", "static u16", "[]"),
	0x04027C90: main.sym_var("txt_sparkle_1", "static u16", "[]"),
	0x04028490: main.sym_var("txt_sparkle_2", "static u16", "[]"),
	0x04028C90: main.sym_var("txt_sparkle_3", "static u16", "[]"),
	0x04029490: main.sym_var("txt_sparkle_4", "static u16", "[]"),
	0x04029C90: main.sym_var("txt_sparkle_5", "static u16", "[]"),
	0x0402A490: main.sym_var("gfx_sparkle", "static Gfx", "[]"),
	0x0402A4F8: main.sym_var("gfx_sparkle_0", "Gfx", "[]", flag={"GLOBL"}),
	0x0402A510: main.sym_var("gfx_sparkle_1", "Gfx", "[]", flag={"GLOBL"}),
	0x0402A528: main.sym_var("gfx_sparkle_2", "Gfx", "[]", flag={"GLOBL"}),
	0x0402A540: main.sym_var("gfx_sparkle_3", "Gfx", "[]", flag={"GLOBL"}),
	0x0402A558: main.sym_var("gfx_sparkle_4", "Gfx", "[]", flag={"GLOBL"}),
	0x0402A570: main.sym_var("gfx_sparkle_5", "Gfx", "[]", flag={"GLOBL"}),

	# splash
	0x0402A588: main.sym_var("vtx_splash", "static Vtx", "[]"),
	0x0402A5C8: main.sym_var("txt_splash_0", "static u16", "[]"),
	0x0402B5C8: main.sym_var("txt_splash_1", "static u16", "[]"),
	0x0402C5C8: main.sym_var("txt_splash_2", "static u16", "[]"),
	0x0402D5C8: main.sym_var("txt_splash_3", "static u16", "[]"),
	0x0402E5C8: main.sym_var("txt_splash_4", "static u16", "[]"),
	0x0402F5C8: main.sym_var("txt_splash_5", "static u16", "[]"),
	0x040305C8: main.sym_var("txt_splash_6", "static u16", "[]"),
	0x040315C8: main.sym_var("txt_splash_7", "static u16", "[]"),
	0x040325C8: main.sym_var("gfx_splash", "static Gfx", "[]"),
	0x04032640: main.sym_var("gfx_splash_0", "Gfx", "[]", flag={"GLOBL"}),
	0x04032658: main.sym_var("gfx_splash_1", "Gfx", "[]", flag={"GLOBL"}),
	0x04032670: main.sym_var("gfx_splash_2", "Gfx", "[]", flag={"GLOBL"}),
	0x04032688: main.sym_var("gfx_splash_3", "Gfx", "[]", flag={"GLOBL"}),
	0x040326A0: main.sym_var("gfx_splash_4", "Gfx", "[]", flag={"GLOBL"}),
	0x040326B8: main.sym_var("gfx_splash_5", "Gfx", "[]", flag={"GLOBL"}),
	0x040326D0: main.sym_var("gfx_splash_6", "Gfx", "[]", flag={"GLOBL"}),
	0x040326E8: main.sym_var("gfx_splash_7", "Gfx", "[]", flag={"GLOBL"}),

	# droplet
	0x04032700: main.sym_var("vtx_droplet", "static Vtx", "[]"),
	0x04032740: main.sym_var("vtx_droplet_red", "static Vtx", "[]"),
	0x04032780: main.sym_var("txt_droplet", "static u16", "[]"),
	0x04032980: main.sym_var("gfx_droplet_start", "static Gfx", "[]"),
	0x040329E0: main.sym_var("gfx_droplet_end", "static Gfx", "[]"),
	0x04032A18: main.sym_var("gfx_droplet", "Gfx", "[]", flag={"GLOBL"}), # 164
	0x04032A30: main.sym_var("gfx_droplet_red", "Gfx", "[]"), # unused

	# glow
	0x04032A48: main.sym_var("vtx_glow", "static Vtx", "[]"),
	0x04032A88: main.sym_var("txt_glow_0", "static u16", "[]"),
	0x04033288: main.sym_var("txt_glow_1", "static u16", "[]"),
	0x04033A88: main.sym_var("txt_glow_2", "static u16", "[]"),
	0x04034288: main.sym_var("txt_glow_3", "static u16", "[]"),
	0x04034A88: main.sym_var("txt_glow_4", "static u16", "[]"),
	0x04035288: main.sym_var("gfx_glow", "static Gfx", "[]"),
	0x04035300: main.sym_var("gfx_glow_0", "Gfx", "[]", flag={"GLOBL"}),
	0x04035318: main.sym_var("gfx_glow_1", "Gfx", "[]", flag={"GLOBL"}),
	0x04035330: main.sym_var("gfx_glow_2", "Gfx", "[]", flag={"GLOBL"}),
	0x04035348: main.sym_var("gfx_glow_3", "Gfx", "[]", flag={"GLOBL"}),
	0x04035360: main.sym_var("gfx_glow_4", "Gfx", "[]", flag={"GLOBL"}),

	# bubble
	0x17000000: main.sym_var("s_bubble_a", "SHPLANG", "[]", flag={"GLOBL"}), # 168
	0x1700001C: main.sym_var("s_bubble_b", "SHPLANG", "[]", flag={"GLOBL"}), # 170

	# dust
	0x17000038: main.sym_var("s_dust", "SHPLANG", "[]", flag={"GLOBL"}), # 150

	# smoke
	0x17000084: main.sym_var("s_smoke", "SHPLANG", "[]", flag={"GLOBL"}), # 148, 156

	# wave
	0x1700009C: main.sym_var("s_wave", "SHPLANG", "[]", flag={"GLOBL"}), # 165
	0x170000E0: main.sym_var("s_wave_red", "SHPLANG", "[]"), # unused

	# ripple
	0x17000124: main.sym_var("s_ripple_stop", "SHPLANG", "[]", flag={"GLOBL"}), # 166
	0x17000168: main.sym_var("s_ripple_move", "SHPLANG", "[]", flag={"GLOBL"}), # 163

	# sparkle
	0x170001BC: main.sym_var("s_sparkle", "SHPLANG", "[]", flag={"GLOBL"}), # 149

	# splash
	0x17000230: main.sym_var("s_splash", "SHPLANG", "[]", flag={"GLOBL"}), # 167

	# glow
	0x17000284: main.sym_var("s_glow", "SHPLANG", "[]", flag={"GLOBL"}), # 143

	# mario
	0x170002E0: main.sym_var("s_mario_hso_head", "static SHPLANG", "[]"),
	0x1700041C: main.sym_var("s_mario_hso_handL", "static SHPLANG", "[]"),
	0x17000494: main.sym_var("s_mario_hso_handR", "static SHPLANG", "[]"),
	0x1700053C: main.sym_var("s_mario_hso", "static SHPLANG", "[]"),
	0x170006F8: main.sym_var("s_mario_mso_handL", "static SHPLANG", "[]"),
	0x17000770: main.sym_var("s_mario_mso_handR", "static SHPLANG", "[]"),
	0x17000818: main.sym_var("s_mario_mso", "static SHPLANG", "[]"),
	0x170009D4: main.sym_var("s_mario_lso_head", "static SHPLANG", "[]"),
	0x17000B10: main.sym_var("s_mario_lso_handL", "static SHPLANG", "[]"),
	0x17000B88: main.sym_var("s_mario_lso_handR", "static SHPLANG", "[]"),
	0x17000C30: main.sym_var("s_mario_lso", "static SHPLANG", "[]"),
	0x17000DEC: main.sym_var("s_mario_hsx_head", "static SHPLANG", "[]"),
	0x17000F28: main.sym_var("s_mario_hsx_handL", "static SHPLANG", "[]"),
	0x17000FA0: main.sym_var("s_mario_hsx_handR", "static SHPLANG", "[]"),
	0x17001048: main.sym_var("s_mario_hsx", "static SHPLANG", "[]"),
	0x17001204: main.sym_var("s_mario_msx_handL", "static SHPLANG", "[]"),
	0x1700127C: main.sym_var("s_mario_msx_handR", "static SHPLANG", "[]"),
	0x17001324: main.sym_var("s_mario_msx", "static SHPLANG", "[]"),
	0x170014E0: main.sym_var("s_mario_lsx_head", "static SHPLANG", "[]"),
	0x1700161C: main.sym_var("s_mario_lsx_handL", "static SHPLANG", "[]"),
	0x17001694: main.sym_var("s_mario_lsx_handR", "static SHPLANG", "[]"),
	0x1700173C: main.sym_var("s_mario_lsx", "static SHPLANG", "[]"),
	0x170018F8: main.sym_var("s_mario_heo_head", "static SHPLANG", "[]"),
	0x170019A4: main.sym_var("s_mario_heo_handL", "static SHPLANG", "[]"),
	0x17001A1C: main.sym_var("s_mario_heo_handR", "static SHPLANG", "[]"),
	0x17001AC4: main.sym_var("s_mario_heo", "static SHPLANG", "[]"),
	0x17001C80: main.sym_var("s_mario_meo_handL", "static SHPLANG", "[]"),
	0x17001CF8: main.sym_var("s_mario_meo_handR", "static SHPLANG", "[]"),
	0x17001DA0: main.sym_var("s_mario_meo", "static SHPLANG", "[]"),
	0x17001F5C: main.sym_var("s_mario_leo_head", "static SHPLANG", "[]"),
	0x17002008: main.sym_var("s_mario_leo_handL", "static SHPLANG", "[]"),
	0x17002080: main.sym_var("s_mario_leo_handR", "static SHPLANG", "[]"),
	0x17002128: main.sym_var("s_mario_leo", "static SHPLANG", "[]"),
	0x170022E4: main.sym_var("s_mario_hex_head", "static SHPLANG", "[]"),
	0x17002390: main.sym_var("s_mario_hex_handL", "static SHPLANG", "[]"),
	0x17002408: main.sym_var("s_mario_hex_handR", "static SHPLANG", "[]"),
	0x170024B0: main.sym_var("s_mario_hex", "static SHPLANG", "[]"),
	0x1700266C: main.sym_var("s_mario_mex_handL", "static SHPLANG", "[]"),
	0x170026E4: main.sym_var("s_mario_mex_handR", "static SHPLANG", "[]"),
	0x1700278C: main.sym_var("s_mario_mex", "static SHPLANG", "[]"),
	0x17002958: main.sym_var("s_mario_lex_head", "static SHPLANG", "[]"),
	0x17002A04: main.sym_var("s_mario_lex_handL", "static SHPLANG", "[]"),
	0x17002A7C: main.sym_var("s_mario_lex_handR", "static SHPLANG", "[]"),
	0x17002B24: main.sym_var("s_mario_lex", "static SHPLANG", "[]"),
	0x17002CE0: main.sym_var("s_mario_h", "static SHPLANG", "[]"),
	0x17002D14: main.sym_var("s_mario_m", "static SHPLANG", "[]"),
	0x17002D48: main.sym_var("s_mario_l", "static SHPLANG", "[]"),
	0x17002D7C: main.sym_var("s_mario_lod", "static SHPLANG", "[]"),
	0x17002DD4: main.sym_var("s_mario", "SHPLANG", "[]", flag={"GLOBL"}), # 1
}

imm_E0_Player = {
	0x0400CCA8: 0x04000000,
	0x0400CD20: 0x04000000,
	0x0400D1D8: 0x04000000,
	0x0400D8F0: 0x04000000,
	0x0400DDE8: 0x04000000,
	0x0400E458: 0x04000000,
	0x0400E7C0: 0x04000000,
	0x0400E838: 0x04000000,
	0x0400ECA0: 0x04000000,
	0x0400EFB8: 0x04000000,
	0x0400F4E8: 0x04000000,
	0x04010350: 0x04000000,
	0x04011968: 0x04000000,
	0x04011980: 0x04000000,
	0x04011A10: 0x04000000,
	0x04011B00: 0x04000000,
	0x04011BF0: 0x04000000,
	0x04011CE0: 0x04000000,
	0x04011DD0: 0x04000000,
	0x04011EC0: 0x04000000,
	0x04011FB0: 0x04000000,
	0x040120A0: 0x04000000,
	0x040139C8: 0x04000000,
	0x04013A38: 0x04000000,
	0x04013B08: 0x04000000,
	0x04013BD8: 0x04000000,
	0x04013CA8: 0x04000000,
	0x04013D78: 0x04000000,
	0x04013E48: 0x04000000,
	0x04013F18: 0x04000000,
	0x04013FE8: 0x04000000,
	0x04014648: 0x04000000,
	0x040146C0: 0x04000000,
	0x04014840: 0x04000000,
	0x04014DC0: 0x04000000,
	0x04014F40: 0x04000000,
	0x040154E0: 0x04000000,
	0x040156C0: 0x04000000,
	0x04015738: 0x04000000,
	0x04015B60: 0x04000000,
	0x04015D00: 0x04000000,
	0x040160C8: 0x04000000,
	0x040168A8: 0x04000000,
	0x04016AC8: 0x04000000,
	0x04016B40: 0x04000000,
	0x04016C70: 0x04000000,
	0x04016E80: 0x04000000,
	0x04016FB0: 0x04000000,
	0x040171C0: 0x04000000,
	0x04017370: 0x04000000,
	0x040173E8: 0x04000000,
	0x040176A8: 0x04000000,
	0x04017818: 0x04000000,
	0x04017AD8: 0x04000000,
	0x04017E80: 0x04000000,
	0x04018428: 0x04000000,
	0x04018440: 0x04000000,
	0x040184D0: 0x04000000,
	0x040185A0: 0x04000000,
	0x04018670: 0x04000000,
	0x04018740: 0x04000000,
	0x04018810: 0x04000000,
	0x040188E0: 0x04000000,
	0x040189B0: 0x04000000,
	0x04018A80: 0x04000000,
	0x04018F70: 0x04000000,
	0x04018FE0: 0x04000000,
	0x04019090: 0x04000000,
	0x04019140: 0x04000000,
	0x040191F0: 0x04000000,
	0x040192A0: 0x04000000,
	0x04019350: 0x04000000,
	0x04019400: 0x04000000,
	0x040194B0: 0x04000000,
	0x04019CA0: 0x04000000,
	0x0401A428: 0x04000000,
	0x0401AF28: 0x04000000,
	0x0401AF40: 0x04000000,
	0x0401B108: 0x04000000,
	0x0401BF30: 0x04000000,
	0x0401C518: 0x04000000,
	0x0401C718: 0x04000000,
	0x0401C7A8: 0x04000000,
	0x0401C840: 0x04000000,
	0x0401CA40: 0x04000000,
	0x0401CAF8: 0x04000000,
	0x0401CBB0: 0x04000000,
}

sym_E0_Shape1A = {
	0x0012A7E0: main.sym("_Shape1AGfxSegmentRomStart"),
	0x00132850: main.sym("_Shape1AShpSegmentRomStart"),
	0x0C000000: main.sym_var("s_1a_85", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000018: main.sym_var("s_1a_86", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C0001E4: main.sym_var("s_1a_87", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000248: main.sym_var("s_1a_88", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000264: main.sym_var("s_1a_84", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C00028C: main.sym_var("s_1a_89", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Shape1B = {
	0x00132C60: main.sym("_Shape1BGfxSegmentRomStart"),
	0x00134A70: main.sym("_Shape1BShpSegmentRomStart"),

	# bully
	0x050000E0: main.sym_var("txt_bully_horn", "static u16", "[]"),
	0x050002E0: main.sym_var("gfx_bully_horn_horn", "static Gfx", "[]"),
	0x05000398: main.sym_var("gfx_bully_horn", "Gfx", "[]", flag={"GLOBL"}),
	0x05000408: main.sym_var("light_bully", "static Lights1", "[]"),
	0x05000468: main.sym_var("txt_bully_body_l", "static u16", "[]"),
	0x05001468: main.sym_var("txt_bully_body_r", "static u16", "[]"),
	0x05002468: main.sym_var("txt_bully_eye", "static u16", "[]"),
	0x05003708: main.sym_var("gfx_bully_shoeL", "Gfx", "[]", flag={"GLOBL"}),
	0x050037A0: main.sym_var("gfx_bully_shoeR", "Gfx", "[]", flag={"GLOBL"}),
	0x05003838: main.sym_var("gfx_bully_eyes_old", "Gfx", "[]"), # unused
	0x05003878: main.sym_var("gfx_bully_body_old", "Gfx", "[]"), # unused
	0x05003CD0: main.sym_var("gfx_bully_body_body_l", "static Gfx", "[]"),
	0x05003D08: main.sym_var("gfx_bully_body_body_r", "static Gfx", "[]"),
	0x05003D40: main.sym_var("gfx_bully_body", "Gfx", "[]", flag={"GLOBL"}),
	0x05003E38: main.sym_var("gfx_bully_body_big_body_l", "static Gfx", "[]"),
	0x05003E70: main.sym_var("gfx_bully_body_big_body_r", "static Gfx", "[]"),
	0x05003EA8: main.sym_var("gfx_bully_body_big", "Gfx", "[]", flag={"GLOBL"}),
	0x05003F80: main.sym_var("gfx_bully_eyes_eye", "static Gfx", "[]"),
	0x05003FC8: main.sym_var("gfx_bully_eyes", "Gfx", "[]", flag={"GLOBL"}),
	0x050042A4: main.sym_var("anime_bully_2", "static ANIME"),
	0x050043D8: main.sym_var("anime_bully_1", "static ANIME"),
	0x05004598: main.sym_var("anime_bully_0", "static ANIME"),
	0x050046F4: main.sym_var("anime_bully_3", "static ANIME"),
	0x0500470C: main.sym_var("anime_bully", "ANIME *", "[]"),
	0x05004720: main.sym_var("align_0", "UNUSED static long long"),

	# blargg
	0x05004728: main.sym_var("light_blargg", "static Lights1", "[]"),
	0x050058D0: main.sym_var("gfx_blargg_lower_jaw", "Gfx", "[]", flag={"GLOBL"}),
	0x05005A60: main.sym_var("gfx_blargg_upper_jaw", "Gfx", "[]", flag={"GLOBL"}),
	0x05005D00: main.sym_var("gfx_blargg_body", "Gfx", "[]", flag={"GLOBL"}),
	0x05006070: main.sym_var("anime_blargg_1", "static ANIME"),
	0x05006154: main.sym_var("anime_blargg_0", "static ANIME"),
	0x0500616C: main.sym_var("anime_blargg", "ANIME *", "[]"), # unused
	0x05006178: main.sym_var("align_1", "UNUSED static long long"),

	# bully
	0x0C000000: main.sym_var("s_bully", "SHPLANG", "[]", flag={"GLOBL"}), # 86
	0x0C000120: main.sym_var("s_bigbully", "SHPLANG", "[]", flag={"GLOBL"}), # 87

	# blargg
	0x0C000240: main.sym_var("s_blargg", "SHPLANG", "[]", flag={"GLOBL"}), # 84
}

imm_E0_Shape1B = {
	0x05003708: 0x05000408,
	0x050037A0: 0x05000408,
	0x05003838: 0x05000408,
	0x05003878: 0x05000408,
	0x050058D0: 0x05004728,
	0x05005998: 0x05004728,
	0x05005A60: 0x05004728,
	0x05005B28: 0x05004728,
	0x05005D00: 0x05004728,
}

sym_E0_Shape1C = {
	0x00134D20: main.sym("_Shape1CGfxSegmentRomStart"),
	0x0013B5D0: main.sym("_Shape1CShpSegmentRomStart"),
	0x0C000000: main.sym_var("s_1c_86", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000308: main.sym_var("s_1c_84", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000328: main.sym_var("s_1c_85", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Shape1D = {
	0x0013B910: main.sym("_Shape1DGfxSegmentRomStart"),
	0x00145C10: main.sym("_Shape1DShpSegmentRomStart"),
	0x0C000000: main.sym_var("s_1d_88", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000068: main.sym_var("s_1d_86", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C00010C: main.sym_var("s_1d_85", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Shape1E = {
	0x00145E90: main.sym("_Shape1EGfxSegmentRomStart"),
	0x00151B70: main.sym("_Shape1EShpSegmentRomStart"),
	0x05003F20: main.sym("0x05003F20"),
	0x0C000000: main.sym_var("s_1e_87", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C0002AC: main.sym_var("s_1e_0C0002AC", "static SHPLANG", "[]"),
	0x0C0005E4: main.sym_var("s_1e_89", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C0005A8: main.sym_var("s_1e_88", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000610: main.sym_var("s_1e_84", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000644: main.sym_var("s_1e_85", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Shape1F = {
	0x001521D0: main.sym("_Shape1FGfxSegmentRomStart"),
	0x001602E0: main.sym("_Shape1FShpSegmentRomStart"),
	0x0C000000: main.sym_var("s_1f_85", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000110: main.sym_var("s_1f_86", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C00036C: main.sym_var("s_1f_87", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Shape1G = {
	0x00160670: main.sym("_Shape1GGfxSegmentRomStart"),
	0x001656E0: main.sym("_Shape1GShpSegmentRomStart"),
	0x0C000000: main.sym_var("s_1g_84", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000104: main.sym_var("s_1g_87", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C00021C: main.sym_var("s_1g_85", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000348: main.sym_var("s_1g_86", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Shape1H = {
	0x00165A50: main.sym("_Shape1HGfxSegmentRomStart"),
	0x00166BD0: main.sym("_Shape1HShpSegmentRomStart"),
	0x0C000000: main.sym_var("s_1h_0C000000", "SHPLANG", "[]"), # unused
	0x0C000018: main.sym_var("s_1h_0C000018", "SHPLANG", "[]"), # unused
	0x0C000030: main.sym_var("s_1h_0C000030", "SHPLANG", "[]"), # unused
	0x0C000048: main.sym_var("s_1h_85", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Shape1I = {
	0x00166C60: main.sym("_Shape1IGfxSegmentRomStart"),
	0x0016D5C0: main.sym("_Shape1IShpSegmentRomStart"),
	0x0C000000: main.sym_var("s_1i_88", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C0000C0: main.sym_var("s_1i_89", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C0000D8: main.sym_var("s_1i_86", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000188: main.sym_var("s_1i_85", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C0001B4: main.sym_var("s_1i_87", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000224: main.sym_var("s_1i_84", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000274: main.sym_var("s_1i_90", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Shape1J = {
	0x0016D870: main.sym("_Shape1JGfxSegmentRomStart"),
	0x00180540: main.sym("_Shape1JShpSegmentRomStart"),
	0x0C000000: main.sym_var("s_1j_84", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000098: main.sym_var("s_1j_0C000098", "static SHPLANG", "[]"),
	0x0C000254: main.sym_var("s_1j_0C000254", "static SHPLANG", "[]"),
	0x0C000410: main.sym_var("s_1j_222", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000460: main.sym_var("_0C000460", "UNUSED static long long"),
	0x0C000468: main.sym_var("s_1j_85", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Shape1K = {
	0x00180BB0: main.sym("_Shape1KGfxSegmentRomStart"),
	0x00187FA0: main.sym("_Shape1KShpSegmentRomStart"),
	0x0C000000: main.sym_var("s_1k_89", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000030: main.sym_var("s_1k_87", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C0001BC: main.sym_var("s_1k_84", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000290: main.sym_var("s_1k_85", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0C000328: main.sym_var("s_1k_86", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Shape2A = {
	0x00188440: main.sym("_Shape2AGfxSegmentRomStart"),
	0x001B9070: main.sym("_Shape2AShpSegmentRomStart"),
	0x0D000000: main.sym_var("s_2a_103", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D000090: main.sym_var("s_2a_104", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D0000B0: main.sym_var("s_2a_3", "SHPLANG", "[]", flag={"GLOBL"}), # local
	0x0D0000D8: main.sym_var("s_2a_0D0000D8", "static SHPLANG", "[]"),
	0x0D000424: main.sym_var("s_2a_0D000424", "static SHPLANG", "[]"),
	0x0D000770: main.sym_var("s_2a_0D000770", "static SHPLANG", "[]"),
	0x0D000AB8: main.sym_var("s_2a_0D000AB8", "static SHPLANG", "[]"),
	0x0D000AC4: main.sym_var("s_2a_100", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D000B40: main.sym_var("s_2a_105", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D000BBC: main.sym_var("s_2a_101_179", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D000BFC: main.sym_var("s_2a_102", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Shape2B = {
	0x001B9CC0: main.sym("_Shape2BGfxSegmentRomStart"),
	0x001C3DB0: main.sym("_Shape2BShpSegmentRomStart"),

	# skeeter
	0x06000000: main.sym_var("light_skeeter", "UNUSED static Lights1", "[]"), # unused
	0x06000090: main.sym_var("txt_skeeter_sphere", "static u16", "[]"),
	0x06000890: main.sym_var("txt_skeeter_iris", "static u16", "[]"),
	0x060009D0: main.sym_var("gfx_skeeter_body_sphere", "static Gfx", "[]"),
	0x06000A08: main.sym_var("gfx_skeeter_body", "Gfx", "[]", flag={"GLOBL"}),
	0x06000AB8: main.sym_var("gfx_skeeter_tail_end_sphere", "static Gfx", "[]"),
	0x06000AF0: main.sym_var("gfx_skeeter_tail_end", "Gfx", "[]", flag={"GLOBL"}),
	0x06000BA0: main.sym_var("gfx_skeeter_eye_sphere", "static Gfx", "[]"),
	0x06000BD8: main.sym_var("gfx_skeeter_eye", "Gfx", "[]", flag={"GLOBL"}),
	0x06000C78: main.sym_var("gfx_skeeter_irisR_iris", "static Gfx", "[]"),
	0x06000CA8: main.sym_var("gfx_skeeter_irisR", "Gfx", "[]", flag={"GLOBL"}),
	0x06000D48: main.sym_var("gfx_skeeter_irisL_iris", "static Gfx", "[]"),
	0x06000D78: main.sym_var("gfx_skeeter_irisL", "Gfx", "[]", flag={"GLOBL"}),
	0x06000DE8: main.sym_var("light_skeeter_foot", "static Lights1", "[]"),
	0x06000E60: main.sym_var("gfx_skeeter_foot_shade", "static Gfx", "[]"),
	0x06000EC0: main.sym_var("gfx_skeeter_foot", "Gfx", "[]", flag={"GLOBL"}),
	0x06003FF0: main.sym_var("gfx_skeeter_footBR_old", "Gfx", "[]"), # unused
	0x06004040: main.sym_var("gfx_skeeter_llegBR", "Gfx", "[]", flag={"GLOBL"}),
	0x06004070: main.sym_var("gfx_skeeter_ulegBR", "Gfx", "[]", flag={"GLOBL"}),
	0x060040A0: main.sym_var("gfx_skeeter_footFR_old", "Gfx", "[]"), # unused
	0x060040F0: main.sym_var("gfx_skeeter_llegFR", "Gfx", "[]", flag={"GLOBL"}),
	0x06004120: main.sym_var("gfx_skeeter_ulegFR", "Gfx", "[]", flag={"GLOBL"}),
	0x06004150: main.sym_var("gfx_skeeter_footFL_old", "Gfx", "[]"), # unused
	0x060041A0: main.sym_var("gfx_skeeter_llegFL", "Gfx", "[]", flag={"GLOBL"}),
	0x060041D0: main.sym_var("gfx_skeeter_ulegFL", "Gfx", "[]", flag={"GLOBL"}),
	0x06004200: main.sym_var("gfx_skeeter_eyeR_old", "Gfx", "[]"), # unused
	0x060045C8: main.sym_var("gfx_skeeter_footBL_old", "Gfx", "[]"), # unused
	0x06004618: main.sym_var("gfx_skeeter_llegBL", "Gfx", "[]", flag={"GLOBL"}),
	0x06004648: main.sym_var("gfx_skeeter_ulegBL", "Gfx", "[]", flag={"GLOBL"}),
	0x06004678: main.sym_var("gfx_skeeter_eyeL_old", "Gfx", "[]"), # unused
	0x06004A40: main.sym_var("gfx_skeeter_tail_end_old", "Gfx", "[]"), # unused
	0x06005328: main.sym_var("gfx_skeeter_tail", "Gfx", "[]", flag={"GLOBL"}),
	0x06005358: main.sym_var("gfx_skeeter_body_old", "Gfx", "[]"), # unused
	0x06005D44: main.sym_var("anime_skeeter_0", "static ANIME"),
	0x06006B70: main.sym_var("anime_skeeter_1", "static ANIME"),
	0x060071E0: main.sym_var("anime_skeeter_2", "static ANIME"),
	0x06007DC8: main.sym_var("anime_skeeter_3", "static ANIME"),
	0x06007DE0: main.sym_var("anime_skeeter", "ANIME *", "[]"),
	0x06007DF0: main.sym_var("align_0", "UNUSED static long long"),

	# kelp
	0x06007DF8: main.sym_var("light_kelp", "static Lights1", "[]"),
	0x06007E10: main.sym_var("txt_kelp_0", "static u16", "[]"),
	0x06008610: main.sym_var("txt_kelp_1", "static u16", "[]"),
	0x06008E10: main.sym_var("txt_kelp_2", "static u16", "[]"),
	0x06009610: main.sym_var("txt_kelp_3", "static u16", "[]"),
	0x06009E50: main.sym_var("gfx_kelp_0_0", "static Gfx", "[]"),
	0x06009E98: main.sym_var("gfx_kelp_0", "Gfx", "[]", flag={"GLOBL"}),
	0x06009F48: main.sym_var("gfx_kelp_1_1", "static Gfx", "[]"),
	0x06009F90: main.sym_var("gfx_kelp_1", "Gfx", "[]", flag={"GLOBL"}),
	0x0600A040: main.sym_var("gfx_kelp_2_2", "static Gfx", "[]"),
	0x0600A088: main.sym_var("gfx_kelp_2", "Gfx", "[]", flag={"GLOBL"}),
	0x0600A138: main.sym_var("gfx_kelp_3_3", "static Gfx", "[]"),
	0x0600A180: main.sym_var("gfx_kelp_3", "Gfx", "[]", flag={"GLOBL"}),
	0x0600A4BC: main.sym_var("anime_kelp_0", "static ANIME"),
	0x0600A4D4: main.sym_var("anime_kelp", "ANIME *", "[]"),
	0x0600A4D8: main.sym_var("align_1", "UNUSED static long long"),

	# watermine
	0x0600A4E0: main.sym_var("light_watermine", "static Lights1", "[]"),
	0x0600A4F8: main.sym_var("txt_watermine_l", "static u16", "[]"),
	0x0600B4F8: main.sym_var("txt_watermine_r", "static u16", "[]"),
	0x0600C4F8: main.sym_var("txt_watermine_spike", "static u16", "[]"),
	0x0600D1F8: main.sym_var("gfx_watermine_mine_l", "static Gfx", "[]"),
	0x0600D230: main.sym_var("gfx_watermine_mine_r", "static Gfx", "[]"),
	0x0600D268: main.sym_var("gfx_watermine_mine", "Gfx", "[]", flag={"GLOBL"}),
	0x0600D2E0: main.sym_var("gfx_watermine_spike_spike", "static Gfx", "[]"),
	0x0600D3F8: main.sym_var("gfx_watermine_spike", "Gfx", "[]", flag={"GLOBL"}),
	0x0600D458: main.sym_var("align_2", "UNUSED static long long"),

	# piranha
	0x0600D460: main.sym_var("align_piranha_start", "UNUSED static long long"),
	0x0600D468: main.sym_var("txt_piranha", "static u16", "[]"),
	0x0600DC68: main.sym_var("light_piranha_body", "static Lights1", "[]"),
	0x0600DD20: main.sym_var("gfx_piranha_body_piranha", "static Gfx", "[]"),
	0x0600DDD8: main.sym_var("gfx_piranha_body", "Gfx", "[]", flag={"GLOBL"}),
	0x0600DE38: main.sym_var("light_piranha_fin", "static Lights1", "[]"),
	0x0600DE90: main.sym_var("gfx_piranha_fin_piranha", "static Gfx", "[]"),
	0x0600DED8: main.sym_var("gfx_piranha_fin", "Gfx", "[]", flag={"GLOBL"}),
	0x0600DF48: main.sym_var("light_piranha_tail", "static Lights1", "[]"),
	0x0600DFC0: main.sym_var("gfx_piranha_tail_piranha", "static Gfx", "[]"),
	0x0600E038: main.sym_var("gfx_piranha_tail", "Gfx", "[]", flag={"GLOBL"}),
	0x0600E24C: main.sym_var("anime_piranha_0", "static ANIME"),
	0x0600E264: main.sym_var("anime_piranha", "ANIME *", "[]"),
	0x0600E268: main.sym_var("align_piranha_end", "UNUSED static long long"),
	0x0600E270: main.sym_var("align_3", "UNUSED static long long"),

	# bub
	0x0600E278: main.sym_var("light_bub", "static Lights1", "[]"),
	0x0600E2A8: main.sym_var("txt_bub_goggles", "static u16", "[]"),
	0x0600EAA8: main.sym_var("txt_bub_fin", "static u16", "[]"),
	0x0600F2A8: main.sym_var("txt_bub_eyes", "static u16", "[]"),
	0x060102A8: main.sym_var("txt_bub_scale", "static u16", "[]"),
	0x06011848: main.sym_var("gfx_bub_body_goggles", "static Gfx", "[]"),
	0x060118C0: main.sym_var("gfx_bub_body_fin", "static Gfx", "[]"),
	0x06011918: main.sym_var("gfx_bub_body_eyes", "static Gfx", "[]"),
	0x06011968: main.sym_var("gfx_bub_body_scale", "static Gfx", "[]"),
	0x06011A50: main.sym_var("gfx_bub_body_shade", "static Gfx", "[]"),
	0x06011B28: main.sym_var("gfx_bub_body", "Gfx", "[]", flag={"GLOBL"}),
	0x06011C58: main.sym_var("gfx_bub_tail_fin", "static Gfx", "[]"),
	0x06011CF0: main.sym_var("gfx_bub_tail", "Gfx", "[]", flag={"GLOBL"}),
	0x06011DC0: main.sym_var("gfx_bub_finL_fin", "static Gfx", "[]"),
	0x06011E48: main.sym_var("gfx_bub_finL", "Gfx", "[]", flag={"GLOBL"}),
	0x06011F18: main.sym_var("gfx_bub_finR_fin", "static Gfx", "[]"),
	0x06011FA0: main.sym_var("gfx_bub_finR", "Gfx", "[]", flag={"GLOBL"}),
	0x0601233C: main.sym_var("anime_bub_0", "static ANIME"),
	0x06012354: main.sym_var("anime_bub", "ANIME *", "[]"),
	0x06012360: main.sym_var("align_4", "UNUSED static long long"),

	# waterring
	0x06012368: main.sym_var("light_waterring", "static Lights1", "[]"),
	0x06012380: main.sym_var("txt_waterring", "static u16", "[]"),
	0x06013380: main.sym_var("vtx_waterring", "static Vtx", "[]"),
	0x06013AC0: main.sym_var("gfx_waterring", "Gfx", "[]", flag={"GLOBL"}),
	0x06013F64: main.sym_var("anime_waterring_0", "static ANIME"),
	0x06013F7C: main.sym_var("anime_waterring", "ANIME *", "[]"),
	0x06013F88: main.sym_var("align_5", "UNUSED static long long"),

	# chest
	0x06013F90: main.sym_var("light_chest", "static Lights1", "[]"),
	0x06013FA8: main.sym_var("txt_chest_keyhole", "static u16", "[]"),
	0x060147A8: main.sym_var("txt_chest_inside", "static u16", "[]"),
	0x06014FA8: main.sym_var("txt_chest_latch", "static u16", "[]"),
	0x060157A8: main.sym_var("txt_chest_outside", "static u16", "[]"),
	0x06016D58: main.sym_var("gfx_chest_box_keyhole", "static Gfx", "[]"),
	0x06016DA0: main.sym_var("gfx_chest_box_latch", "static Gfx", "[]"),
	0x06016E18: main.sym_var("gfx_chest_box_inside", "static Gfx", "[]"),
	0x06016EE0: main.sym_var("gfx_chest_box_outside", "static Gfx", "[]"),
	0x06016F90: main.sym_var("gfx_chest_box", "Gfx", "[]", flag={"GLOBL"}),
	0x06017680: main.sym_var("gfx_chest_lid_inside", "static Gfx", "[]"),
	0x06017790: main.sym_var("gfx_chest_lid_latch", "static Gfx", "[]"),
	0x06017810: main.sym_var("gfx_chest_lid_outside", "static Gfx", "[]"),
	0x060178C0: main.sym_var("gfx_chest_lid", "Gfx", "[]", flag={"GLOBL"}),
	0x06017958: main.sym_var("align_6", "UNUSED static long long"),

	# skeeter
	0x0D000000: main.sym_var("s_skeeter", "SHPLANG", "[]", flag={"GLOBL"}), # 105

	# kelp
	0x0D000284: main.sym_var("s_kelp", "SHPLANG", "[]", flag={"GLOBL"}), # 193

	# watermine
	0x0D0002F4: main.sym_var("s_watermine", "SHPLANG", "[]", flag={"GLOBL"}), # 179

	# piranha
	0x0D000324: main.sym_var("s_piranha", "SHPLANG", "[]", flag={"GLOBL"}), # 103

	# bub
	0x0D00038C: main.sym_var("s_bub", "SHPLANG", "[]", flag={"GLOBL"}), # 100

	# waterring
	0x0D000414: main.sym_var("s_waterring", "SHPLANG", "[]", flag={"GLOBL"}), # 104

	# chest
	0x0D000450: main.sym_var("s_chest", "SHPLANG", "[]", flag={"GLOBL"}), # 101
	0x0D000468: main.sym_var("s_chestlid", "SHPLANG", "[]", flag={"GLOBL"}), # 102
}

imm_E0_Shape2B = {
	0x06000E60: 0x06000DE8,
	# ideally there would be a full set of normals, but i only need these to
	# be distinct
	0x06000F50: (127, 0, 0),
	0x06000F60: (127, 0, 0),
	0x06000F70: (127, 0, 0),
	0x06000F80: (127, 0, 0),
	0x06000F90: (127, 0, 0),
	0x06001080: (127, 0, 0),
	0x06001090: (127, 0, 0),
	0x060010A0: (127, 0, 0),
	0x060010B0: (127, 0, 0),
	0x060010C0: (127, 0, 0),
	0x060011B0: (127, 0, 0),
	0x060011C0: (127, 0, 0),
	0x060011D0: (127, 0, 0),
	0x060011E0: (127, 0, 0),
	0x060011F0: (127, 0, 0),
	0x06001AE0: (127, 0, 0),
	0x06001AF0: (127, 0, 0),
	0x06001B00: (127, 0, 0),
	0x06001B10: (127, 0, 0),
	0x06001B20: (127, 0, 0),
	0x06009E68: 0x06007DF8,
	0x06009F60: 0x06007DF8,
	0x0600A058: 0x06007DF8,
	0x0600A150: 0x06007DF8,
	0x0600D2F8: 0x0600A4E0,
	0x0600DD38: 0x0600DC68,
	0x0600DEA8: 0x0600DE38,
	0x0600DFD8: 0x0600DF48,
	0x06011860: 0x0600E278,
	0x06011A50: 0x0600E278,
	0x06011AD8: 0x0600E278,
	0x06011C70: 0x0600E278,
	0x06011DD8: 0x0600E278,
	0x06011F30: 0x0600E278,
	0x06013B18: 0x06012368,
	0x06016D70: 0x06013F90,
	0x06017698: 0x06013F90,
}

sym_E0_Shape2C = {
	0x001C4230: main.sym("_Shape2CGfxSegmentRomStart"),
	0x001D7C90: main.sym("_Shape2CShpSegmentRomStart"),
	0x06000A08: main.sym("0x06000A08"),
	0x0D000000: main.sym_var("s_2c_106", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D0000B8: main.sym_var("s_2c_107", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D0000D0: main.sym_var("s_2c_191", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D000214: main.sym_var("s_2c_104", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D000358: main.sym_var("s_2c_100", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D000480: main.sym_var("s_2c_103", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D0005D0: main.sym_var("s_2c_101", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D0005EC: main.sym_var("s_2c_102", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Shape2D = {
	0x001D8310: main.sym("_Shape2DGfxSegmentRomStart"),
	0x001E4BF0: main.sym("_Shape2DShpSegmentRomStart"),

	# lakitu2
	0x06000000: main.sym_var("txt_lakitu2_unused", "UNUSED static u16", "[]"),
	0x06000800: main.sym_var("txt_lakitu2_eyes_open", "static u16", "[]"),
	0x06001800: main.sym_var("txt_lakitu2_eyes_closed", "static u16", "[]"),
	0x06002800: main.sym_var("txt_lakitu2_shell", "static u16", "[]"),
	0x06003000: main.sym_var("txt_lakitu2_mouth", "static u16", "[]"),
	0x06003800: main.sym_var("txt_lakitu2_lens", "static u16", "[]"),
	0x06003A00: main.sym_var("light_lakitu2_body", "static Lights1", "[]"),
	0x06003C80: main.sym_var("gfx_lakitu2_body_shell", "static Gfx", "[]"),
	0x06003DB0: main.sym_var("gfx_lakitu2_body_skin", "static Gfx", "[]"),
	0x06003E30: main.sym_var("gfx_lakitu2_body", "Gfx", "[]", flag={"GLOBL"}),
	0x06003E98: main.sym_var("light_lakitu2_mouth", "static Lights1", "[]"),
	0x06004410: main.sym_var("gfx_lakitu2_mouth_mouth", "static Gfx", "[]"),
	0x06004680: main.sym_var("gfx_lakitu2_mouth", "Gfx", "[]", flag={"GLOBL"}),
	0x060046E0: main.sym_var("light_lakitu2_armR", "static Lights1", "[]"),
	0x060047E8: main.sym_var("gfx_lakitu2_armR", "Gfx", "[]", flag={"GLOBL"}),
	0x060048D8: main.sym_var("light_lakitu2_armL", "static Lights1", "[]"),
	0x060049E0: main.sym_var("gfx_lakitu2_armL", "Gfx", "[]", flag={"GLOBL"}),
	0x06004AD0: main.sym_var("light_lakitu2_eyes", "static Lights1", "[]"),
	0x06004BA8: main.sym_var("gfx_lakitu2_eyes_eyes", "static Gfx", "[]"),
	0x06004BE8: main.sym_var("gfx_lakitu2_eyes_start", "static Gfx", "[]"),
	0x06004C30: main.sym_var("gfx_lakitu2_eyes_end", "static Gfx", "[]"),
	0x06004C60: main.sym_var("gfx_lakitu2_eyes_open", "Gfx", "[]", flag={"GLOBL"}),
	0x06004C88: main.sym_var("gfx_lakitu2_eyes_closed", "Gfx", "[]", flag={"GLOBL"}),
	0x06004CB0: main.sym_var("light_lakitu2_camera", "static Lights1", "[]"),
	0x060051D0: main.sym_var("gfx_lakitu2_camera_lens", "static Gfx", "[]"),
	0x06005218: main.sym_var("gfx_lakitu2_camera_shade", "static Gfx", "[]"),
	0x06005360: main.sym_var("gfx_lakitu2_camera", "Gfx", "[]", flag={"GLOBL"}),
	0x060053D8: main.sym_var("light_lakitu2_rod", "static Lights1", "[]"),
	0x06005598: main.sym_var("gfx_lakitu2_rod0", "Gfx", "[]", flag={"GLOBL"}),
	0x060055E8: main.sym_var("gfx_lakitu2_rod1", "Gfx", "[]", flag={"GLOBL"}),
	0x06005610: main.sym_var("gfx_lakitu2_rod2", "Gfx", "[]", flag={"GLOBL"}),
	0x060058E0: main.sym_var("anime_lakitu2_0", "static ANIME"),
	0x060058F8: main.sym_var("anime_lakitu2", "ANIME *", "[]"),
	0x06005900: main.sym_var("align_0", "UNUSED static long long"),

	# toad
	0x06005908: main.sym_var("light_toad_head", "static Lights1", "[]"),
	0x06005920: main.sym_var("txt_toad_face", "static u16", "[]"),
	0x06006120: main.sym_var("txt_toad_spot", "static u16", "[]"),
	0x06007300: main.sym_var("gfx_toad_head_face", "static Gfx", "[]"),
	0x06007498: main.sym_var("gfx_toad_head_spot", "static Gfx", "[]"),
	0x060076C0: main.sym_var("gfx_toad_head_shade", "static Gfx", "[]"),
	0x06007710: main.sym_var("gfx_toad_head_opa", "Gfx", "[]", flag={"GLOBL"}),
	0x06007788: main.sym_var("gfx_toad_head_xlu", "Gfx", "[]", flag={"GLOBL"}),
	0x06007808: main.sym_var("light_toad_vest", "static Lights1", "[]"),
	0x060079E0: main.sym_var("gfx_toad_vest_shade", "static Gfx", "[]"),
	0x06007AC8: main.sym_var("gfx_toad_vest_opa", "Gfx", "[]", flag={"GLOBL"}),
	0x06007B00: main.sym_var("gfx_toad_vest_xlu", "Gfx", "[]", flag={"GLOBL"}),
	0x06007B28: main.sym_var("light_toad_body", "static Lights1", "[]"),
	0x06007DB8: main.sym_var("gfx_toad_body_shade", "static Gfx", "[]"),
	0x06007F58: main.sym_var("gfx_toad_body", "Gfx", "[]", flag={"GLOBL"}),
	0x06007F80: main.sym_var("light_toad_armR", "static Lights1", "[]"),
	0x06008168: main.sym_var("gfx_toad_armR_shade", "static Gfx", "[]"),
	0x060082A0: main.sym_var("gfx_toad_armR", "Gfx", "[]", flag={"GLOBL"}),
	0x060082C8: main.sym_var("light_toad_armL", "static Lights1", "[]"),
	0x06008490: main.sym_var("gfx_toad_armL_shade", "static Gfx", "[]"),
	0x060085C8: main.sym_var("gfx_toad_armL_opa", "Gfx", "[]", flag={"GLOBL"}),
	0x06008608: main.sym_var("gfx_toad_armL_xlu", "Gfx", "[]", flag={"GLOBL"}),
	0x06008650: main.sym_var("light_toad_shoeR", "static Lights1", "[]"),
	0x06008838: main.sym_var("gfx_toad_shoeR_shade", "static Gfx", "[]"),
	0x06008980: main.sym_var("gfx_toad_shoeR", "Gfx", "[]", flag={"GLOBL"}),
	0x060089A8: main.sym_var("light_toad_shoeL", "static Lights1", "[]"),
	0x06008B80: main.sym_var("gfx_toad_shoeL_shade", "static Gfx", "[]"),
	0x06008CC8: main.sym_var("gfx_toad_shoeL", "Gfx", "[]", flag={"GLOBL"}),
	0x0600906C: main.sym_var("anime_toad_6", "static ANIME"),
	0x06009400: main.sym_var("anime_toad_7", "static ANIME"),
	0x06009AE0: main.sym_var("anime_toad_4", "static ANIME"),
	0x0600A1C0: main.sym_var("anime_toad_5", "static ANIME"),
	0x0600B75C: main.sym_var("anime_toad_0", "static ANIME"),
	0x0600CF68: main.sym_var("anime_toad_1", "static ANIME"),
	0x0600E504: main.sym_var("anime_toad_2", "static ANIME"),
	0x0600FC30: main.sym_var("anime_toad_3", "static ANIME"),
	0x0600FC48: main.sym_var("anime_toad", "ANIME *", "[]"),
	0x0600FC68: main.sym_var("align_1", "UNUSED static long long"),

	# mips
	0x0600FC70: main.sym_var("txt_mips_face", "static u16", "[]"),
	0x06010470: main.sym_var("light_mips_06010470", "static Lights1", "[]"),
	0x060106F0: main.sym_var("gfx_mips_060106F0", "static Gfx", "[]"),
	0x06010838: main.sym_var("gfx_mips_06010838", "static Gfx", "[]"),
	0x060108A8: main.sym_var("gfx_mips_060108A8", "Gfx", "[]", flag={"GLOBL"}),
	0x06010910: main.sym_var("light_mips_06010910", "static Lights1", "[]"),
	0x06010B88: main.sym_var("gfx_mips_06010B88", "static Gfx", "[]"),
	0x06010D30: main.sym_var("gfx_mips_06010D30", "Gfx", "[]", flag={"GLOBL"}),
	0x06010D90: main.sym_var("light_mips_06010D90", "static Lights1", "[]"),
	0x06010EA0: main.sym_var("gfx_mips_06010EA0", "static Gfx", "[]"),
	0x06010F50: main.sym_var("gfx_mips_06010F50", "Gfx", "[]", flag={"GLOBL"}),
	0x06010FB0: main.sym_var("light_mips_06010FB0", "static Lights1", "[]"),
	0x060110E8: main.sym_var("gfx_mips_060110E8", "static Gfx", "[]"),
	0x060111A0: main.sym_var("gfx_mips_060111A0", "Gfx", "[]", flag={"GLOBL"}),
	0x06011200: main.sym_var("light_mips_06011200", "static Lights1", "[]"),
	0x06011330: main.sym_var("gfx_mips_06011330", "static Gfx", "[]"),
	0x06011400: main.sym_var("gfx_mips_06011400", "Gfx", "[]", flag={"GLOBL"}),
	0x06011460: main.sym_var("light_mips_06011460", "static Lights1", "[]"),
	0x06011560: main.sym_var("gfx_mips_06011560", "static Gfx", "[]"),
	0x06011610: main.sym_var("gfx_mips_06011610", "Gfx", "[]", flag={"GLOBL"}),
	0x06011670: main.sym_var("light_mips_06011670", "static Lights1", "[]"),
	0x060117A0: main.sym_var("gfx_mips_060117A0", "static Gfx", "[]"),
	0x06011870: main.sym_var("gfx_mips_06011870", "Gfx", "[]", flag={"GLOBL"}),
	0x060118D0: main.sym_var("light_mips_060118D0", "static Lights1", "[]"),
	0x060119D0: main.sym_var("gfx_mips_060119D0", "static Gfx", "[]"),
	0x06011A80: main.sym_var("gfx_mips_06011A80", "Gfx", "[]", flag={"GLOBL"}),
	0x06011AE0: main.sym_var("light_mips_06011AE0", "static Lights1", "[]"),
	0x06011BF0: main.sym_var("gfx_mips_06011BF0", "static Gfx", "[]"),
	0x06011CA0: main.sym_var("gfx_mips_06011CA0", "Gfx", "[]", flag={"GLOBL"}),
	0x06011D00: main.sym_var("light_mips_06011D00", "static Lights1", "[]"),
	0x06011E00: main.sym_var("gfx_mips_06011E00", "static Gfx", "[]"),
	0x06011EA0: main.sym_var("gfx_mips_06011EA0", "Gfx", "[]", flag={"GLOBL"}),
	0x06011F00: main.sym_var("light_mips_06011F00", "static Lights1", "[]"),
	0x06011F78: main.sym_var("gfx_mips_06011F78", "static Gfx", "[]"),
	0x06011FC8: main.sym_var("gfx_mips_06011FC8", "Gfx", "[]", flag={"GLOBL"}),
	0x06011FE8: main.sym_var("light_mips_06011FE8", "static Lights1", "[]"),
	0x06012060: main.sym_var("gfx_mips_06012060", "static Gfx", "[]"),
	0x060120B0: main.sym_var("gfx_mips_060120B0", "Gfx", "[]", flag={"GLOBL"}),
	0x06013338: main.sym_var("anime_mips_2", "static ANIME"),
	0x0601378C: main.sym_var("anime_mips_4", "static ANIME"),
	0x06013AE8: main.sym_var("anime_mips_1", "static ANIME"),
	0x06014C84: main.sym_var("anime_mips_0", "static ANIME"),
	0x0601570C: main.sym_var("anime_mips_3", "static ANIME"),
	0x06015724: main.sym_var("anime_mips", "ANIME *", "[]"),
	0x06015740: main.sym_var("align_2", "UNUSED static long long"),

	# boo2
	0x06015748: main.sym_var("light_boo2", "static Lights1"),
	0x06015760: main.sym_var("txt_boo2_eyes", "static u16", "[]"),
	0x06016760: main.sym_var("txt_boo2_mouth", "static u16", "[]"),
	0x06017B00: main.sym_var("gfx_boo2_mouth", "static Gfx", "[]"),
	0x06017B68: main.sym_var("gfx_boo2_eyes", "static Gfx", "[]"),
	0x06017BC0: main.sym_var("gfx_boo2_shade", "static Gfx", "[]"),
	0x06017DD0: main.sym_var("gfx_boo2", "Gfx", "[]", flag={"GLOBL"}),
	0x06017E70: main.sym_var("align_3", "UNUSED static long long"),

	# lakitu2
	0x0D000000: main.sym_var("s_lakitu2", "SHPLANG", "[]", flag={"GLOBL"}), # 102

	# toad
	0x0D000114: main.sym_var("s_toad_0D000114", "static SHPLANG", "[]"),
	0x0D00027C: main.sym_var("s_toad_0D00027C", "static SHPLANG", "[]"),
	0x0D0003E4: main.sym_var("s_toad", "SHPLANG", "[]", flag={"GLOBL"}), # 221

	# mips
	0x0D000440: main.sym_var("align_mips_start", "UNUSED static long long"),
	0x0D000448: main.sym_var("s_mips", "SHPLANG", "[]", flag={"GLOBL"}), # 100
	0x0D0005A8: main.sym_var("align_mips_end", "UNUSED static long long"),

	# boo2
	0x0D0005B0: main.sym_var("s_boo2", "SHPLANG", "[]", flag={"GLOBL"}), # 101
}

imm_E0_Shape2D = {
	0x06003C98: 0x06003A00,
	0x06003DB0: 0x06003A00,
	0x06004428: 0x06003E98,
	0x060047E8: 0x060046E0,
	0x060049E0: 0x060048D8,
	0x06004BA8: 0x06004AD0,
	0x060051E8: 0x06004CB0,
	0x06005218: 0x06004CB0,
	0x060052A0: 0x06004CB0,
	0x06005320: 0x06004CB0,
	0x06005598: 0x060053D8,
	0x060055E8: 0x060053D8,
	0x06005610: 0x060053D8,
	0x06007318: 0x06005908,
	0x060079E0: 0x06007808,
	0x06007DB8: 0x06007B28,
	0x06007EC8: 0x06007B28,
	0x06008168: 0x06007F80,
	0x06008490: 0x060082C8,
	0x06008838: 0x06008650,
	0x06008B80: 0x060089A8,
	0x06010708: 0x06010470,
	0x06010838: 0x06010470,
	0x06010868: 0x06010470,
	0x06010BA0: 0x06010910,
	0x06010EB8: 0x06010D90,
	0x06010EF0: 0x06010D90,
	0x06011100: 0x06010FB0,
	0x06011130: 0x06010FB0,
	0x06011150: 0x06010FB0,
	0x06011348: 0x06011200,
	0x06011380: 0x06011200,
	0x06011578: 0x06011460,
	0x060115A8: 0x06011460,
	0x060117B8: 0x06011670,
	0x060117F0: 0x06011670,
	0x060119E8: 0x060118D0,
	0x06011A18: 0x060118D0,
	0x06011C08: 0x06011AE0,
	0x06011C40: 0x06011AE0,
	0x06011E18: 0x06011D00,
	0x06011E50: 0x06011D00,
	0x06011F78: 0x06011F00,
	0x06012060: 0x06011FE8,
}

sym_E0_Shape2E = {
	0x001E51F0: main.sym("_Shape2EGfxSegmentRomStart"),
	0x001E7D90: main.sym("_Shape2EShpSegmentRomStart"),
	0x0D000000: main.sym_var("s_2e_0D000000", "static SHPLANG", "[]"),
	0x0D000078: main.sym_var("s_2e_0D000078", "static SHPLANG", "[]"),
	0x0D0000F0: main.sym_var("s_2e_102", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D000140: main.sym_var("_0D000140", "UNUSED static long long"),
}

sym_E0_Shape2F = {
	0x001E7EE0: main.sym("_Shape2FGfxSegmentRomStart"),
	0x001F1B30: main.sym("_Shape2FShpSegmentRomStart"),
	0x0600DE38: main.sym("0x0600DE38"),
	0x06013AE8: main.sym("0x06013AE8"),
	0x0D000000: main.sym_var("s_2f_103", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D00001C: main.sym_var("s_2f_102", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D0000DC: main.sym_var("s_2f_100", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D0001A0: main.sym_var("s_2f_206", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D000230: main.sym_var("s_2f_104", "SHPLANG", "[]", flag={"GLOBL"}),
	0x0D000394: main.sym_var("s_2f_101", "SHPLANG", "[]", flag={"GLOBL"}),
}

sym_E0_Common = {
	0x001F2200: main.sym("_CommonGfxSegmentRomStart"),
	0x002008D0: main.sym("_CommonShpSegmentRomStart"),

	# bluecoinsw
	0x08000000: main.sym_var("light_bluecoinsw", "static Lights1", "[]"),
	0x08000018: main.sym_var("txt_bluecoinsw_side", "static u16", "[]"),
	0x08000418: main.sym_var("txt_bluecoinsw_top", "static u16", "[]"),
	0x08000D58: main.sym_var("gfx_bluecoinsw_side", "static Gfx", "[]"),
	0x08000DD0: main.sym_var("gfx_bluecoinsw_top", "static Gfx", "[]"),
	0x08000E08: main.sym_var("gfx_bluecoinsw", "Gfx", "[]", flag={"GLOBL"}),
	0x08000E98: main.sym_var("map_bluecoinsw", "MAP", "[]", flag={"GLOBL"}),
	0x08000F10: main.sym_var("align_0", "UNUSED static long long"),

	# amp
	0x08000F18: main.sym_var("txt_amp_arc", "static u16", "[]"),
	0x08001318: main.sym_var("txt_amp_eyes", "static u16", "[]"),
	0x08001B18: main.sym_var("txt_amp_body", "static u16", "[]"),
	0x08002318: main.sym_var("txt_amp_mouth", "static u16", "[]"),
	0x08002B68: main.sym_var("gfx_amp_arc_arc", "static Gfx", "[]"),
	0x08002BA0: main.sym_var("gfx_amp_arc", "Gfx", "[]", flag={"GLOBL"}),
	0x08002C50: main.sym_var("gfx_amp_eyes_eyes", "static Gfx", "[]"),
	0x08002C88: main.sym_var("gfx_amp_eyes", "Gfx", "[]", flag={"GLOBL"}),
	0x08002D38: main.sym_var("gfx_amp_mouth_mouth", "static Gfx", "[]"),
	0x08002D70: main.sym_var("gfx_amp_mouth", "Gfx", "[]", flag={"GLOBL"}),
	0x08002E20: main.sym_var("gfx_amp_body_body", "static Gfx", "[]"),
	0x08002E58: main.sym_var("gfx_amp_body", "Gfx", "[]", flag={"GLOBL"}),
	0x08002EC8: main.sym_var("light_amp_old", "static Lights1", "[]"),
	0x08003910: main.sym_var("gfx_amp_arcA_old", "Gfx", "[]"), # unused
	0x08003940: main.sym_var("gfx_amp_arcB_old", "Gfx", "[]"), # unused
	0x08003970: main.sym_var("gfx_amp_arcC_old", "Gfx", "[]"), # unused
	0x080039A0: main.sym_var("gfx_amp_arcD_old", "Gfx", "[]"), # unused
	0x080039D0: main.sym_var("gfx_amp_body_old", "Gfx", "[]"), # unused
	0x08003DA8: main.sym_var("gfx_amp_mouth_old", "Gfx", "[]"), # unused
	0x08003DD8: main.sym_var("gfx_amp_anger_old", "Gfx", "[]"), # unused
	0x08003E00: main.sym_var("gfx_amp_eyes_old", "Gfx", "[]"), # unused
	0x0800401C: main.sym_var("anime_amp_0", "static ANIME"),
	0x08004034: main.sym_var("anime_amp", "ANIME *", "[]"),
	0x08004038: main.sym_var("align_1", "UNUSED static long long"),

	# cannonlid
	0x08004040: main.sym_var("light_cannonlid", "static Lights1", "[]"),
	0x08004058: main.sym_var("txt_cannonlid_lid", "static u16", "[]"),
	0x08004898: main.sym_var("gfx_cannonlid_lid", "static Gfx", "[]"),
	0x080048E0: main.sym_var("gfx_cannonlid", "Gfx", "[]", flag={"GLOBL"}), # 201
	0x08004950: main.sym_var("map_cannonlid", "MAP", "[]", flag={"GLOBL"}),
	0x08004980: main.sym_var("align_2", "UNUSED static long long"),

	# cannon
	0x08004988: main.sym_var("light_cannon", "static Lights1", "[]"),
	0x080049B8: main.sym_var("txt_cannon_side", "static u16", "[]"),
	0x08005658: main.sym_var("gfx_cannon_side", "static Gfx", "[]"),
	0x080056D0: main.sym_var("gfx_cannon_shade", "static Gfx", "[]"),
	0x080057F8: main.sym_var("gfx_cannon", "Gfx", "[]", flag={"GLOBL"}),
	0x08005870: main.sym_var("align_3", "UNUSED static long long"),

	# cannonbarrel
	0x08005878: main.sym_var("light_cannonbarrel", "static Lights1", "[]"),
	0x080058A8: main.sym_var("txt_cannonbarrel_rim", "static u16", "[]"),
	0x08006408: main.sym_var("gfx_cannonbarrel_rim", "static Gfx", "[]"),
	0x080064C0: main.sym_var("gfx_cannonbarrel_shade", "static Gfx", "[]"),
	0x08006660: main.sym_var("gfx_cannonbarrel", "Gfx", "[]", flag={"GLOBL"}),
	0x080066C8: main.sym_var("align_4", "UNUSED static long long"),

	# chuckya
	0x080066D0: main.sym_var("light_chuckya", "UNUSED static Lights1", "[]"), # unused
	0x08006778: main.sym_var("txt_chuckya_eyes", "static u16", "[]"),
	0x08006F78: main.sym_var("txt_chuckya_purple", "UNUSED static u16", "[]"), # unused
	0x08007778: main.sym_var("txt_chuckya_red", "static u16", "[]"),
	0x08007F78: main.sym_var("txt_chuckya_purple_l", "static u16", "[]"),
	0x08008F78: main.sym_var("txt_chuckya_purple_r", "static u16", "[]"),
	0x08009FF8: main.sym_var("gfx_chuckya_body_purple_l", "static Gfx", "[]"),
	0x0800A030: main.sym_var("gfx_chuckya_body_purple_r", "static Gfx", "[]"),
	0x0800A068: main.sym_var("gfx_chuckya_body", "Gfx", "[]", flag={"GLOBL"}),
	0x0800A160: main.sym_var("gfx_chuckya_armL_purple_l", "static Gfx", "[]"),
	0x0800A198: main.sym_var("gfx_chuckya_armL_purple_r", "static Gfx", "[]"),
	0x0800A1D0: main.sym_var("gfx_chuckya_armL", "Gfx", "[]", flag={"GLOBL"}),
	0x0800A2C8: main.sym_var("gfx_chuckya_armR_purple_l", "static Gfx", "[]"),
	0x0800A300: main.sym_var("gfx_chuckya_armR_purple_r", "static Gfx", "[]"),
	0x0800A338: main.sym_var("gfx_chuckya_armR", "Gfx", "[]", flag={"GLOBL"}),
	0x0800A3F0: main.sym_var("gfx_chuckya_handL_red", "static Gfx", "[]"),
	0x0800A428: main.sym_var("gfx_chuckya_handL", "Gfx", "[]", flag={"GLOBL"}),
	0x0800A4D8: main.sym_var("gfx_chuckya_handR_red", "static Gfx", "[]"),
	0x0800A510: main.sym_var("gfx_chuckya_handR", "Gfx", "[]", flag={"GLOBL"}),
	0x0800A5C0: main.sym_var("gfx_chuckya_antenna_end_red", "static Gfx", "[]"),
	0x0800A5F8: main.sym_var("gfx_chuckya_antenna_end", "Gfx", "[]", flag={"GLOBL"}),
	0x0800A668: main.sym_var("light_chuckya_eyes", "static Lights1", "[]"),
	0x0800A700: main.sym_var("gfx_chuckya_eyes_eyes", "static Gfx", "[]"),
	0x0800A758: main.sym_var("gfx_chuckya_eyes", "Gfx", "[]", flag={"GLOBL"}),
	0x0800A7C8: main.sym_var("light_chuckya_base", "static Lights1", "[]"),
	0x0800A870: main.sym_var("gfx_chuckya_base_base", "static Gfx", "[]"),
	0x0800A8D0: main.sym_var("gfx_chuckya_base", "Gfx", "[]", flag={"GLOBL"}),
	0x0800A8F0: main.sym_var("light_chuckya_antenna", "static Lights1", "[]"),
	0x0800A958: main.sym_var("gfx_chuckya_antenna_antenna", "static Gfx", "[]"),
	0x0800A998: main.sym_var("gfx_chuckya_antenna", "Gfx", "[]", flag={"GLOBL"}),
	0x0800A9B8: main.sym_var("light_chuckya_back", "static Lights1", "[]"),
	0x0800AB70: main.sym_var("gfx_chuckya_back_back", "static Gfx", "[]"),
	0x0800ABE8: main.sym_var("gfx_chuckya_back", "Gfx", "[]", flag={"GLOBL"}),
	0x0800AF68: main.sym_var("anime_chuckya_0", "static ANIME"),
	0x0800B1A8: main.sym_var("anime_chuckya_1", "static ANIME"),
	0x0800B4A8: main.sym_var("anime_chuckya_2", "static ANIME"),
	0x0800B9F8: main.sym_var("anime_chuckya_3", "static ANIME"),
	0x0800BBEC: main.sym_var("anime_chuckya_4", "static ANIME"),
	0x0800C058: main.sym_var("anime_chuckya_5", "static ANIME"),
	0x0800C070: main.sym_var("anime_chuckya", "ANIME *", "[]"),
	0x0800C088: main.sym_var("align_5", "UNUSED static long long"),

	# purplesw
	0x0800C090: main.sym_var("light_purplesw", "static Lights1", "[]"),
	0x0800C0A8: main.sym_var("txt_purplesw_side", "static u16", "[]"),
	0x0800C128: main.sym_var("txt_purplesw_top", "static u16", "[]"),
	0x0800C668: main.sym_var("gfx_purplesw_side", "static Gfx", "[]"),
	0x0800C6E0: main.sym_var("gfx_purplesw_top", "static Gfx", "[]"),
	0x0800C718: main.sym_var("gfx_purplesw", "Gfx", "[]", flag={"GLOBL"}),
	0x0800C7A8: main.sym_var("map_purplesw", "MAP", "[]", flag={"GLOBL"}),
	0x0800C820: main.sym_var("align_6", "UNUSED static long long"),

	# lift
	0x0800C828: main.sym_var("light_lift", "static Lights1", "[]"),
	0x0800C840: main.sym_var("txt_lift_side", "static u16", "[]"),
	0x0800CC40: main.sym_var("txt_lift_face", "static u16", "[]"),
	0x0800D5C0: main.sym_var("gfx_lift_side", "static Gfx", "[]"),
	0x0800D618: main.sym_var("gfx_lift_face", "static Gfx", "[]"),
	0x0800D680: main.sym_var("gfx_lift", "Gfx", "[]", flag={"GLOBL"}),
	0x0800D710: main.sym_var("map_lift", "MAP", "[]", flag={"GLOBL"}),
	0x0800D798: main.sym_var("align_7", "UNUSED static long long"),

	# heart
	0x0800D7E0: main.sym_var("txt_heart", "static u16", "[]"),
	0x0800DFE0: main.sym_var("gfx_heart", "Gfx", "[]", flag={"GLOBL"}),
	0x0800E078: main.sym_var("align_8", "UNUSED static long long"),

	# flyguy
	0x0800E080: main.sym_var("align_flyguy_start", "UNUSED static long long"),
	0x0800E088: main.sym_var("txt_flyguy_cloth", "static u16", "[]"),
	0x0800F088: main.sym_var("txt_flyguy_face", "static u16", "[]"),
	0x0800F888: main.sym_var("txt_flyguy_propeller", "static u16", "[]"),
	0x08010088: main.sym_var("light_flyguy", "static Lights1", "[]"),
	0x08010840: main.sym_var("gfx_flyguy_footR", "Gfx", "[]", flag={"GLOBL"}),
	0x08010968: main.sym_var("gfx_flyguy_footL", "Gfx", "[]", flag={"GLOBL"}),
	0x08010A90: main.sym_var("gfx_flyguy_shaft", "Gfx", "[]"), # unused
	0x08010AE0: main.sym_var("light_flyguy_propeller", "static Lights1", "[]"),
	0x08010B38: main.sym_var("gfx_flyguy_propeller_propeller", "static Gfx", "[]"),
	0x08010B80: main.sym_var("gfx_flyguy_propeller", "Gfx", "[]", flag={"GLOBL"}),
	0x08010BF0: main.sym_var("light_flyguy_body", "static Lights1", "[]"),
	0x080113A8: main.sym_var("gfx_flyguy_body_face", "static Gfx", "[]"),
	0x08011420: main.sym_var("gfx_flyguy_body_cloth", "static Gfx", "[]"),
	0x080116D0: main.sym_var("gfx_flyguy_body_shade", "static Gfx", "[]"),
	0x08011710: main.sym_var("gfx_flyguy_body", "Gfx", "[]", flag={"GLOBL"}),
	0x08011A4C: main.sym_var("anime_flyguy_0", "static ANIME"),
	0x08011A64: main.sym_var("anime_flyguy", "ANIME *", "[]"),
	0x08011A68: main.sym_var("align_flyguy_end", "UNUSED static long long"),
	0x08011A70: main.sym_var("align_9", "UNUSED static long long"),

	# block
	0x08011A78: main.sym_var("light_block", "static Lights1", "[]"),
	0x08011A90: main.sym_var("txt_block_0", "static u16", "[]"),
	0x08012290: main.sym_var("txt_block_1", "static u16", "[]"),
	0x08012C30: main.sym_var("gfx_block_end", "static Gfx", "[]"),
	0x08012CD8: main.sym_var("gfx_block_start", "static Gfx", "[]"),
	0x08012D20: main.sym_var("gfx_block_0", "Gfx", "[]", flag={"GLOBL"}),
	0x08012D48: main.sym_var("gfx_block_1", "Gfx", "[]", flag={"GLOBL"}),
	0x08012D70: main.sym_var("map_block", "MAP", "[]", flag={"GLOBL"}),
	0x08012DF8: main.sym_var("align_block", "UNUSED static long long"),
	0x08012E00: main.sym_var("align_10", "UNUSED static long long"),

	# ironball
	0x08012E08: main.sym_var("align_11", "UNUSED static long long"),

	# itembox
	0x08012E10: main.sym_var("light_itembox", "static Lights1", "[]"),
	0x08012E28: main.sym_var("txt_itembox_face_b", "static u16", "[]"),
	0x08013628: main.sym_var("txt_itembox_side_b", "static u16", "[]"),
	0x08014628: main.sym_var("txt_itembox_face_g", "static u16", "[]"),
	0x08014E28: main.sym_var("txt_itembox_side_g", "static u16", "[]"),
	0x08015E28: main.sym_var("txt_itembox_face_r", "static u16", "[]"),
	0x08016628: main.sym_var("txt_itembox_side_r", "static u16", "[]"),
	0x08017628: main.sym_var("txt_itembox_face_y", "static u16", "[]"),
	0x08017E28: main.sym_var("txt_itembox_side_y", "static u16", "[]"),
	0x08018FA8: main.sym_var("gfx_itembox_32x64_face", "static Gfx", "[]"),
	0x08019008: main.sym_var("gfx_itembox_32x64_side", "static Gfx", "[]"),
	0x08019058: main.sym_var("gfx_itembox_32x64_start", "static Gfx", "[]"),
	0x08019220: main.sym_var("gfx_itembox_64x32_face", "static Gfx", "[]"),
	0x08019280: main.sym_var("gfx_itembox_64x32_side", "static Gfx", "[]"),
	0x080192D0: main.sym_var("gfx_itembox_64x32_start", "static Gfx", "[]"),
	0x08019318: main.sym_var("gfx_itembox_r", "Gfx", "[]", flag={"GLOBL"}),
	0x08019378: main.sym_var("gfx_itembox_g", "Gfx", "[]", flag={"GLOBL"}),
	0x080193D8: main.sym_var("gfx_itembox_b", "Gfx", "[]", flag={"GLOBL"}),
	0x08019438: main.sym_var("gfx_itembox_y", "Gfx", "[]", flag={"GLOBL"}),
	0x08019498: main.sym_var("align_12", "UNUSED static long long"),

	# goomba
	0x080194A0: main.sym_var("light_goomba", "static Lights1", "[]"),
	0x08019530: main.sym_var("txt_goomba_body", "static u16", "[]"),
	0x08019D30: main.sym_var("txt_goomba_head_open", "static u16", "[]"),
	0x0801A530: main.sym_var("txt_goomba_head_closed", "static u16", "[]"),
	0x0801AD30: main.sym_var("light_goomba_body", "static Lights1", "[]"),
	0x0801B2E8: main.sym_var("gfx_goomba_head", "static Gfx", "[]"),
	0x0801B560: main.sym_var("gfx_goomba_head_start", "static Gfx", "[]"),
	0x0801B5A0: main.sym_var("gfx_goomba_head_end", "static Gfx", "[]"),
	0x0801B5C8: main.sym_var("gfx_goomba_head_open", "Gfx", "[]", flag={"GLOBL"}),
	0x0801B5F0: main.sym_var("gfx_goomba_head_closed", "Gfx", "[]", flag={"GLOBL"}),
	0x0801B658: main.sym_var("gfx_goomba_body_body", "static Gfx", "[]"),
	0x0801B690: main.sym_var("gfx_goomba_body", "Gfx", "[]", flag={"GLOBL"}),
	0x0801CE20: main.sym_var("gfx_goomba_footL", "Gfx", "[]", flag={"GLOBL"}),
	0x0801CF78: main.sym_var("gfx_goomba_footR", "Gfx", "[]", flag={"GLOBL"}),
	0x0801D0D0: main.sym_var("gfx_goomba_head_old", "Gfx", "[]"), # unused
	0x0801D360: main.sym_var("gfx_goomba_body_old", "Gfx", "[]"), # unused
	0x0801D760: main.sym_var("gfx_goomba_base", "Gfx", "[]", flag={"GLOBL"}),
	0x0801DA34: main.sym_var("anime_goomba_0", "static ANIME"),
	0x0801DA4C: main.sym_var("anime_goomba", "ANIME *", "[]"),
	0x0801DA50: main.sym_var("align_goomba", "UNUSED static long long"),
	0x0801DA58: main.sym_var("align_13", "UNUSED static long long"),

	# bobomb
	0x0801DA60: main.sym_var("txt_bobomb_black_l", "static u16", "[]"),
	0x0801EA60: main.sym_var("txt_bobomb_black_r", "static u16", "[]"),
	0x0801FA60: main.sym_var("txt_bobomb_red_l", "static u16", "[]"),
	0x08020A60: main.sym_var("txt_bobomb_red_r", "static u16", "[]"),
	0x08021A60: main.sym_var("txt_bobomb_eyes_open", "static u16", "[]"),
	0x08022260: main.sym_var("txt_bobomb_eyes_closed", "static u16", "[]"),
	0x08022AC0: main.sym_var("gfx_bobomb_eyes_start", "static Gfx", "[]"),
	0x08022B08: main.sym_var("gfx_bobomb_eyes_end", "static Gfx", "[]"),
	0x08022B58: main.sym_var("gfx_bobomb_eyes_open", "Gfx", "[]", flag={"GLOBL"}),
	0x08022B88: main.sym_var("gfx_bobomb_eyes_closed", "Gfx", "[]", flag={"GLOBL"}),
	0x08022BB8: main.sym_var("vtx_bobomb_body_l", "static Vtx", "[]"),
	0x08022BF8: main.sym_var("vtx_bobomb_body_r", "static Vtx", "[]"),
	0x08022C38: main.sym_var("gfx_bobomb_body_black", "static Gfx", "[]"),
	0x08022CA0: main.sym_var("gfx_bobomb_body_red", "static Gfx", "[]"),
	0x08022D08: main.sym_var("gfx_bobomb_body", "Gfx", "[]", flag={"GLOBL"}),
	0x08022D78: main.sym_var("gfx_redbobomb_body", "Gfx", "[]", flag={"GLOBL"}),
	0x08022DE8: main.sym_var("light_bobomb", "static Lights1", "[]"),
	0x08023270: main.sym_var("gfx_bobomb_footR", "Gfx", "[]", flag={"GLOBL"}),
	0x08023378: main.sym_var("gfx_bobomb_footL", "Gfx", "[]", flag={"GLOBL"}),
	0x08023480: main.sym_var("gfx_bobomb_cap", "Gfx", "[]", flag={"GLOBL"}),
	0x080237FC: main.sym_var("anime_bobomb_0", "static ANIME"),
	0x08023954: main.sym_var("anime_bobomb_1", "static ANIME"),
	0x0802396C: main.sym_var("anime_bobomb", "ANIME *", "[]"),
	0x08023978: main.sym_var("align_14", "UNUSED static long long"),

	# pushblock
	0x08023980: main.sym_var("light_pushblock", "static Lights1", "[]"),
	0x08023998: main.sym_var("txt_pushblock", "static u16", "[]"),
	0x08024B18: main.sym_var("gfx_pushblock_pushblock", "static Gfx", "[]"),
	0x08024BB8: main.sym_var("gfx_pushblock", "Gfx", "[]", flag={"GLOBL"}), # 218
	0x08024C28: main.sym_var("map_pushblock", "MAP", "[]", flag={"GLOBL"}),
	0x08024CB0: main.sym_var("align_15", "UNUSED static long long"),

	# dotbox
	0x08024CB8: main.sym_var("light_dotbox", "static Lights1", "[]"),
	0x08024EB8: main.sym_var("gfx_dotbox_box", "static Gfx", "[]"),
	0x08024F30: main.sym_var("gfx_dotbox_box_start", "static Gfx", "[]"),
	0x08024F58: main.sym_var("gfx_dotbox_box_end", "static Gfx", "[]"),
	0x08024F88: main.sym_var("gfx_dotbox_box_r", "Gfx", "[]", flag={"GLOBL"}),
	0x08024FA8: main.sym_var("gfx_dotbox_box_g", "Gfx", "[]", flag={"GLOBL"}),
	0x08024FC8: main.sym_var("gfx_dotbox_box_b", "Gfx", "[]", flag={"GLOBL"}),
	0x08024FE8: main.sym_var("gfx_dotbox_box_y", "Gfx", "[]", flag={"GLOBL"}),
	0x08025168: main.sym_var("txt_dotbox_dot", "static u16", "[]"),
	0x08025968: main.sym_var("gfx_dotbox_dot_dot", "static Gfx", "[]"),
	0x080259F8: main.sym_var("gfx_dotbox_dot", "Gfx", "[]", flag={"GLOBL"}),
	0x08025A68: main.sym_var("light_dotboxmark", "static Lights1", "[]"),
	0x08025A80: main.sym_var("txt_dotboxmark", "static u16", "[]"),
	0x08025EC0: main.sym_var("gfx_dotboxmark_mark", "static Gfx", "[]"),
	0x08025F08: main.sym_var("gfx_dotboxmark", "Gfx", "[]", flag={"GLOBL"}), # 132
	0x08025F78: main.sym_var("map_dotbox", "MAP", "[]", flag={"GLOBL"}),
	0x08026000: main.sym_var("align_16", "UNUSED static long long"),

	# testlift
	0x08026008: main.sym_var("light_testlift", "static Lights1", "[]"),
	0x08026260: main.sym_var("gfx_testlift", "Gfx", "[]"), # unused
	0x080262F8: main.sym_var("map_testlift", "MAP", "[]"), # unused
	0x08026380: main.sym_var("align_17", "UNUSED static long long"),

	# shell
	0x08026388: main.sym_var("light_shell_old", "static Lights1", "[]"),
	0x08027108: main.sym_var("gfx_shell_old_top", "static Gfx", "[]"),
	0x08027170: main.sym_var("gfx_shell_old_bottom", "static Gfx", "[]"),
	0x08027258: main.sym_var("gfx_shell_old_side", "static Gfx", "[]"),
	0x080273C8: main.sym_var("gfx_greenshell_old", "Gfx", "[]", flag={"GLOBL"}),
	0x08027420: main.sym_var("gfx_redshell_old", "Gfx", "[]", flag={"GLOBL"}),
	0x08027470: main.sym_var("light_shell", "static Lights1", "[]"),
	0x080274A0: main.sym_var("txt_shell_bottom", "static u16", "[]"),
	0x08027CA0: main.sym_var("txt_shell_top", "static u16", "[]"),
	0x080288E0: main.sym_var("gfx_shell_top", "static Gfx", "[]"),
	0x08028978: main.sym_var("gfx_shell_bottom", "static Gfx", "[]"),
	0x08028A20: main.sym_var("gfx_shell_shade", "static Gfx", "[]"),
	0x08028B78: main.sym_var("gfx_shell", "Gfx", "[]", flag={"GLOBL"}),
	0x08028BE8: main.sym_var("align_18", "UNUSED static long long"),

	# bluecoinsw
	0x0F000000: main.sym_var("s_bluecoinsw", "SHPLANG", "[]", flag={"GLOBL"}), # 140

	# amp
	0x0F000020: main.sym_var("align_amp_start", "UNUSED static long long"),
	0x0F000028: main.sym_var("s_amp", "SHPLANG", "[]", flag={"GLOBL"}), # 194
	0x0F0001A0: main.sym_var("align_amp_end", "UNUSED static long long"),

	# cannon
	0x0F0001A8: main.sym_var("s_cannon", "SHPLANG", "[]", flag={"GLOBL"}), # 128

	# cannonbarrel
	0x0F0001C0: main.sym_var("s_cannonbarrel", "SHPLANG", "[]", flag={"GLOBL"}), # 127

	# chuckya
	0x0F0001D8: main.sym_var("s_chuckya", "SHPLANG", "[]", flag={"GLOBL"}), # 223

	# purplesw
	0x0F0004CC: main.sym_var("s_purplesw", "SHPLANG", "[]", flag={"GLOBL"}), # 207

	# lift
	0x0F0004E4: main.sym_var("s_lift", "SHPLANG", "[]", flag={"GLOBL"}), # 202

	# heart
	0x0F0004FC: main.sym_var("s_heart", "SHPLANG", "[]", flag={"GLOBL"}), # 120

	# flyguy
	0x0F000518: main.sym_var("s_flyguy", "SHPLANG", "[]", flag={"GLOBL"}), # 220

	# block
	0x0F0005D0: main.sym_var("s_block", "SHPLANG", "[]", flag={"GLOBL"}), # 129
	0x0F000610: main.sym_var("s_crate", "SHPLANG", "[]", flag={"GLOBL"}), # 130

	# ironball
	0x0F000640: main.sym_var("s_ironball", "SHPLANG", "[]", flag={"GLOBL"}), # 180
	0x0F00066C: main.sym_var("s_ironball_noshadow", "SHPLANG", "[]", flag={"GLOBL"}), # 225

	# itembox
	0x0F000694: main.sym_var("s_itembox", "SHPLANG", "[]", flag={"GLOBL"}), # 137

	# goomba
	0x0F0006E4: main.sym_var("s_goomba", "SHPLANG", "[]", flag={"GLOBL"}), # 192

	# bobomb
	0x0F0007B8: main.sym_var("s_bobomb", "SHPLANG", "[]", flag={"GLOBL"}), # 188
	0x0F0008F4: main.sym_var("s_redbobomb", "SHPLANG", "[]", flag={"GLOBL"}), # 195

	# pushblock
	0x0F000A30: main.sym_var("s_pushblock", "SHPLANG", "[]", flag={"GLOBL"}), # 217

	# dotbox
	0x0F000A58: main.sym_var("s_dotbox", "SHPLANG", "[]", flag={"GLOBL"}), # 131

	# shell
	0x0F000AB0: main.sym_var("s_shell", "SHPLANG", "[]", flag={"GLOBL"}), # 190
	0x0F000ADC: main.sym_var("s_redshell_old", "SHPLANG", "[]"), # unused
	0x0F000B08: main.sym_var("s_greenshell_old", "SHPLANG", "[]"), # unused
}

imm_E0_Common = {
	0x08000D70: 0x08000000,
	0x08003910: 0x08002EC8,
	0x08003940: 0x08002EC8,
	0x08003970: 0x08002EC8,
	0x080039A0: 0x08002EC8,
	0x080039D0: 0x08002EC8,
	0x08003DA8: 0x08002EC8,
	0x08003DD8: 0x08002EC8,
	0x08003E00: 0x08002EC8,
	0x080048B0: 0x08004040,
	0x08005670: 0x08004988,
	0x080056D0: 0x08004988,
	0x08006420: 0x08005878,
	0x080064C0: 0x08005878,
	0x0800A718: 0x0800A668,
	0x0800A870: 0x0800A7C8,
	0x0800A958: 0x0800A8F0,
	0x0800AB70: 0x0800A9B8,
	0x0800C680: 0x0800C090,
	0x0800D5D8: 0x0800C828,
	0x08010840: 0x08010088,
	0x08010968: 0x08010088,
	0x08010A90: 0x08010088,
	0x08010B50: 0x08010AE0,
	0x080113C0: 0x08010BF0,
	0x08011438: 0x08010BF0,
	0x08011460: 0x08010BF0,
	0x080116D0: 0x08010BF0,
	0x08012C30: 0x08011A78,
	0x08018FA8: 0x08012E10,
	0x08019220: 0x08012E10,
	0x0801B2E8: 0x0801AD30,
	0x0801CE20: 0x080194A0,
	0x0801CF78: 0x080194A0,
	0x0801D0D0: 0x080194A0,
	0x0801D360: 0x080194A0,
	0x08022C50: 0x08022BB8,
	0x08022C80: 0x08022BF8,
	0x08022CB8: 0x08022BB8,
	0x08022CE8: 0x08022BF8,
	0x08023270: 0x08022DE8,
	0x08023378: 0x08022DE8,
	0x08023480: 0x08022DE8,
	0x08024B30: 0x08023980,
	0x08024F90: 0x08024CB8,
	0x08024FB0: 0x08024CB8,
	0x08024FD0: 0x08024CB8,
	0x08024FF0: 0x08024CB8,
	0x08025ED8: 0x08025A68,
	0x08026260: 0x08026008,
	0x080273D0: 0x08026388,
	0x080273F0: 0x08026388,
	0x08027408: 0x08026388,
	0x08027428: 0x08026388,
	0x08027440: 0x08026388,
	0x08027458: 0x08026388,
	0x080288F8: 0x08027470,
	0x08028A20: 0x08027470,
	0x08028A50: 0x08027470,
}

sym_E0_Global = {
	0x00201410: main.sym("_GlobalGfxSegmentRomStart"),
	0x00218DA0: main.sym("_GlobalShpSegmentRomStart"),

	# puff
	0x03000000: main.sym_var("vtx_whitepuff", "static Vtx", "[]"),
	0x03000040: main.sym_var("vtx_blackpuff", "static Vtx", "[]"),
	0x03000080: main.sym_var("txt_puff", "static u16", "[]"),
	0x03000880: main.sym_var("gfx_whitepuff", "Gfx", "[]", flag={"GLOBL"}),
	0x03000920: main.sym_var("gfx_blackpuff", "Gfx", "[]", flag={"GLOBL"}),
	0x030009C0: main.sym_var("align_0", "UNUSED static long long"),

	# explosion
	0x030009C8: main.sym_var("vtx_explosion", "static Vtx", "[]"),
	0x03000A08: main.sym_var("txt_explosion_0", "static u16", "[]"),
	0x03001208: main.sym_var("txt_explosion_1", "static u16", "[]"),
	0x03001A08: main.sym_var("txt_explosion_2", "static u16", "[]"),
	0x03002208: main.sym_var("txt_explosion_3", "static u16", "[]"),
	0x03002A08: main.sym_var("txt_explosion_4", "static u16", "[]"),
	0x03003208: main.sym_var("txt_explosion_5", "static u16", "[]"),
	0x03003A08: main.sym_var("txt_explosion_6", "static u16", "[]"),
	0x03004208: main.sym_var("gfx_explosion", "static Gfx", "[]"),
	0x03004298: main.sym_var("gfx_explosion_0", "Gfx", "[]", flag={"GLOBL"}),
	0x030042B0: main.sym_var("gfx_explosion_1", "Gfx", "[]", flag={"GLOBL"}),
	0x030042C8: main.sym_var("gfx_explosion_2", "Gfx", "[]", flag={"GLOBL"}),
	0x030042E0: main.sym_var("gfx_explosion_3", "Gfx", "[]", flag={"GLOBL"}),
	0x030042F8: main.sym_var("gfx_explosion_4", "Gfx", "[]", flag={"GLOBL"}),
	0x03004310: main.sym_var("gfx_explosion_5", "Gfx", "[]", flag={"GLOBL"}),
	0x03004328: main.sym_var("gfx_explosion_6", "Gfx", "[]", flag={"GLOBL"}),
	0x03004340: main.sym_var("align_1", "UNUSED static long long"),

	# butterfly
	0x030043A8: main.sym_var("txt_butterfly_wing", "static u16", "[]"),
	0x03005408: main.sym_var("gfx_butterfly_l", "Gfx", "[]", flag={"GLOBL"}),
	0x030054A0: main.sym_var("gfx_butterfly_r", "Gfx", "[]", flag={"GLOBL"}),
	0x030055B0: main.sym_var("anime_butterfly_0", "static ANIME"),
	0x03005698: main.sym_var("anime_butterfly_1", "static ANIME"),
	0x030056B0: main.sym_var("anime_butterfly", "ANIME *", "[]"),
	0x030056B8: main.sym_var("align_2", "UNUSED static long long"),

	# coin
	0x030056C0: main.sym_var("vtx_coin", "static Vtx", "[]"),
	0x03005700: main.sym_var("vtx_bluecoin", "static Vtx", "[]"),
	0x03005740: main.sym_var("vtx_redcoin", "static Vtx", "[]"),
	0x03005780: main.sym_var("txt_coin_0", "static u16", "[]"),
	0x03005F80: main.sym_var("txt_coin_1", "static u16", "[]"),
	0x03006780: main.sym_var("txt_coin_2", "static u16", "[]"),
	0x03006F80: main.sym_var("txt_coin_3", "static u16", "[]"),
	0x03007780: main.sym_var("gfx_coin_start", "static Gfx", "[]"),
	0x030077D0: main.sym_var("gfx_coin_end", "static Gfx", "[]"),
	0x03007800: main.sym_var("gfx_coin_0", "Gfx", "[]", flag={"GLOBL"}),
	0x03007828: main.sym_var("gfx_coin_1", "Gfx", "[]", flag={"GLOBL"}),
	0x03007850: main.sym_var("gfx_coin_2", "Gfx", "[]", flag={"GLOBL"}),
	0x03007878: main.sym_var("gfx_coin_3", "Gfx", "[]", flag={"GLOBL"}),
	0x030078A0: main.sym_var("gfx_bluecoin_0", "Gfx", "[]", flag={"GLOBL"}),
	0x030078C8: main.sym_var("gfx_bluecoin_1", "Gfx", "[]", flag={"GLOBL"}),
	0x030078F0: main.sym_var("gfx_bluecoin_2", "Gfx", "[]", flag={"GLOBL"}),
	0x03007918: main.sym_var("gfx_bluecoin_3", "Gfx", "[]", flag={"GLOBL"}),
	0x03007940: main.sym_var("gfx_redcoin_0", "Gfx", "[]", flag={"GLOBL"}),
	0x03007968: main.sym_var("gfx_redcoin_1", "Gfx", "[]", flag={"GLOBL"}),
	0x03007990: main.sym_var("gfx_redcoin_2", "Gfx", "[]", flag={"GLOBL"}),
	0x030079B8: main.sym_var("gfx_redcoin_3", "Gfx", "[]", flag={"GLOBL"}),
	0x030079E0: main.sym_var("align_3", "UNUSED static long long"),

	# pipe
	0x030079E8: main.sym_var("light_pipe_side", "static Lights1", "[]"),
	0x03007E40: main.sym_var("txt_pipe_side", "static u16", "[]"),
	0x03008E40: main.sym_var("gfx_pipe_side_side", "static Gfx", "[]"),
	0x03008F98: main.sym_var("gfx_pipe_side", "Gfx", "[]", flag={"GLOBL"}),
	0x03008FF8: main.sym_var("light_pipe_end", "static Lights1", "[]"),
	0x03009168: main.sym_var("txt_pipe_top", "static u16", "[]"),
	0x03009968: main.sym_var("gfx_pipe_end_top", "static Gfx", "[]"),
	0x03009A20: main.sym_var("gfx_pipe_end_bottom", "static Gfx", "[]"),
	0x03009A50: main.sym_var("gfx_pipe_end", "Gfx", "[]", flag={"GLOBL"}),
	0x03009AC8: main.sym_var("map_pipe", "MAP", "[]"),
	0x03009CD8: main.sym_var("align_4", "UNUSED static long long"),

	# door
	0x03009CE0: main.sym_var("light_door", "static Lights1", "[]"),
	0x03009D10: main.sym_var("txt_door_a_face", "static u16", "[]"),
	0x0300AD10: main.sym_var("txt_door_a_side", "static u16", "[]"),
	0x0300BD10: main.sym_var("txt_door_b_face", "static u16", "[]"),
	0x0300CD10: main.sym_var("txt_door_b_side", "static u16", "[]"),
	0x0300D510: main.sym_var("txt_door_d_face", "static u16", "[]"),
	0x0300E510: main.sym_var("txt_door_d_side", "static u16", "[]"),
	0x0300ED10: main.sym_var("txt_door_e_face", "static u16", "[]"),
	0x0300FD10: main.sym_var("txt_door_e_side", "static u16", "[]"),
	0x03010510: main.sym_var("txt_door_f_face", "static u16", "[]"),
	0x03011510: main.sym_var("txt_door_f_side", "static u16", "[]"),
	0x03011D10: main.sym_var("txt_door_star", "static u16", "[]"),
	0x03012510: main.sym_var("txt_door_star1", "static u16", "[]"),
	0x03012D10: main.sym_var("txt_door_star3", "static u16", "[]"),
	0x03013510: main.sym_var("txt_door_keyhole", "static u16", "[]"),
	0x03013C10: main.sym_var("gfx_door_a_h_panel", "static Gfx", "[]"),
	0x03013CC8: main.sym_var("gfx_door_a_h_knob_f", "static Gfx", "[]"),
	0x03013D78: main.sym_var("gfx_door_a_h_knob_b", "static Gfx", "[]"),
	0x03013E28: main.sym_var("gfx_door_a_h", "Gfx", "[]", flag={"GLOBL"}),
	0x03013EA8: main.sym_var("gfx_door_a_h_x", "Gfx", "[]", flag={"GLOBL"}),
	0x03013FA0: main.sym_var("vtx_door_a_l_knob", "static Vtx", "[]"),
	0x03014020: main.sym_var("gfx_door_a_l_panel", "static Gfx", "[]"),
	0x03014100: main.sym_var("gfx_door_a_l", "Gfx", "[]", flag={"GLOBL"}),
	0x03014128: main.sym_var("gfx_door_a_l_x", "Gfx", "[]", flag={"GLOBL"}),
	0x03014140: main.sym_var("vtx_door_star_h", "static Vtx", "[]"),
	0x03014180: main.sym_var("vtx_door_star_l", "static Vtx", "[]"),
	0x030141C0: main.sym_var("gfx_door_star_start", "static Gfx", "[]"),
	0x03014218: main.sym_var("gfx_door_star_end", "static Gfx", "[]"),
	0x03014250: main.sym_var("gfx_door_star_h", "Gfx", "[]", flag={"GLOBL"}),
	0x03014280: main.sym_var("gfx_door_star_l", "Gfx", "[]", flag={"GLOBL"}),
	0x030142B0: main.sym_var("gfx_door_star1_h", "Gfx", "[]", flag={"GLOBL"}),
	0x030142E0: main.sym_var("gfx_door_star1_l", "Gfx", "[]", flag={"GLOBL"}),
	0x03014310: main.sym_var("gfx_door_star3_h", "Gfx", "[]", flag={"GLOBL"}),
	0x03014340: main.sym_var("gfx_door_star3_l", "Gfx", "[]", flag={"GLOBL"}),
	0x03014370: main.sym_var("vtx_door_keyhole_h", "static Vtx", "[]"),
	0x030143F0: main.sym_var("vtx_door_keyhole_l", "static Vtx", "[]"),
	0x03014470: main.sym_var("gfx_door_keyhole_start", "static Gfx", "[]"),
	0x030144E0: main.sym_var("gfx_door_keyhole_end", "static Gfx", "[]"),
	0x03014528: main.sym_var("gfx_door_keyhole_h", "Gfx", "[]", flag={"GLOBL"}),
	0x03014540: main.sym_var("gfx_door_keyhole_l", "Gfx", "[]", flag={"GLOBL"}),
	0x03014888: main.sym_var("gfx_door_h_knob", "static Gfx", "[]"),
	0x030149C0: main.sym_var("gfx_door_h_side", "static Gfx", "[]"),
	0x03014A20: main.sym_var("gfx_door_h_face", "static Gfx", "[]"),
	0x03014A50: main.sym_var("gfx_door_h_start", "static Gfx", "[]"),
	0x03014A80: main.sym_var("gfx_door_b_h", "Gfx", "[]", flag={"GLOBL"}),
	0x03014B30: main.sym_var("gfx_door_c_h", "Gfx", "[]", flag={"GLOBL"}),
	0x03014BE0: main.sym_var("gfx_door_d_h", "Gfx", "[]", flag={"GLOBL"}),
	0x03014C90: main.sym_var("gfx_door_e_h", "Gfx", "[]", flag={"GLOBL"}),
	0x03014D40: main.sym_var("gfx_door_f_h", "Gfx", "[]", flag={"GLOBL"}),
	0x03014EF0: main.sym_var("gfx_door_l_panel", "static Gfx", "[]"),
	0x03014F30: main.sym_var("gfx_door_l_knob", "static Gfx", "[]"),
	0x03014F68: main.sym_var("gfx_door_l_start", "static Gfx", "[]"),
	0x03014F98: main.sym_var("gfx_door_b_l", "Gfx", "[]", flag={"GLOBL"}),
	0x03015008: main.sym_var("gfx_door_c_l", "Gfx", "[]", flag={"GLOBL"}),
	0x03015078: main.sym_var("gfx_door_d_l", "Gfx", "[]", flag={"GLOBL"}),
	0x030150E8: main.sym_var("gfx_door_e_l", "Gfx", "[]", flag={"GLOBL"}),
	0x03015158: main.sym_var("gfx_door_f_l", "Gfx", "[]", flag={"GLOBL"}),
	0x03015208: main.sym_var("anime_door_0", "static ANIME"),
	0x03015220: main.sym_var("anime_door_1_val", "static s16", "[]"),
	0x03015404: main.sym_var("anime_door_1_tbl", "static u16", "[]"),
	0x03015440: main.sym_var("anime_door_1", "static ANIME"),
	0x03015458: main.sym_var("anime_door_3", "static ANIME"),
	0x03015470: main.sym_var("anime_door_2_val", "static s16", "[]"),
	0x03015654: main.sym_var("anime_door_2_tbl", "static u16", "[]"),
	0x03015690: main.sym_var("anime_door_2", "static ANIME"),
	0x030156A8: main.sym_var("anime_door_4", "static ANIME"),
	0x030156C0: main.sym_var("anime_door", "ANIME *", "[]"),
	0x030156D8: main.sym_var("align_5", "UNUSED static long long"),

	# doorkey
	0x030156E0: main.sym_var("light_doorkey", "static Lights1", "[]"),
	0x030161F8: main.sym_var("gfx_doorkey", "Gfx", "[]", flag={"GLOBL"}),
	0x03016BE8: main.sym_var("anime_doorkey_1", "static ANIME"),
	0x030172B8: main.sym_var("anime_doorkey_0", "static ANIME"),
	0x030172D0: main.sym_var("anime_doorkey", "ANIME *", "[]"),
	0x030172D8: main.sym_var("align_6", "UNUSED static long long"),

	# flame
	0x030172E0: main.sym_var("vtx_flame", "static Vtx", "[]"),
	0x03017320: main.sym_var("txt_flame_0", "static u16", "[]"),
	0x03017B20: main.sym_var("txt_flame_1", "static u16", "[]"),
	0x03018320: main.sym_var("txt_flame_2", "static u16", "[]"),
	0x03018B20: main.sym_var("txt_flame_3", "static u16", "[]"),
	0x03019320: main.sym_var("txt_flame_4", "static u16", "[]"),
	0x03019B20: main.sym_var("txt_flame_5", "static u16", "[]"),
	0x0301A320: main.sym_var("txt_flame_6", "static u16", "[]"),
	0x0301AB20: main.sym_var("txt_flame_7", "static u16", "[]"),
	0x0301B320: main.sym_var("gfx_flame", "static Gfx", "[]"),
	0x0301B3B0: main.sym_var("gfx_flame_0", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B3C8: main.sym_var("gfx_flame_1", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B3E0: main.sym_var("gfx_flame_2", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B3F8: main.sym_var("gfx_flame_3", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B410: main.sym_var("gfx_flame_4", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B428: main.sym_var("gfx_flame_5", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B440: main.sym_var("gfx_flame_6", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B458: main.sym_var("gfx_flame_7", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B470: main.sym_var("gfx_blueflame", "static Gfx", "[]"),
	0x0301B500: main.sym_var("gfx_blueflame_0", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B518: main.sym_var("gfx_blueflame_1", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B530: main.sym_var("gfx_blueflame_2", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B548: main.sym_var("gfx_blueflame_3", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B560: main.sym_var("gfx_blueflame_4", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B578: main.sym_var("gfx_blueflame_5", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B590: main.sym_var("gfx_blueflame_6", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B5A8: main.sym_var("gfx_blueflame_7", "Gfx", "[]", flag={"GLOBL"}),
	0x0301B5C0: main.sym_var("align_7", "UNUSED static long long"),

	# fish
	0x0301B5C8: main.sym_var("light_fish", "static Lights1", "[]"),
	0x0301B5E0: main.sym_var("txt_fish", "static u16", "[]"),
	0x0301BEC0: main.sym_var("gfx_fish_body_fish", "static Gfx", "[]"),
	0x0301BFB8: main.sym_var("gfx_fish_body", "Gfx", "[]", flag={"GLOBL"}),
	0x0301C0A8: main.sym_var("gfx_fish_tail_fish", "static Gfx", "[]"),
	0x0301C150: main.sym_var("gfx_fish_tail", "Gfx", "[]", flag={"GLOBL"}),
	0x0301C298: main.sym_var("anime_fish_0", "static ANIME"),
	0x0301C2B0: main.sym_var("anime_fish", "ANIME *", "[]"),
	0x0301C2B8: main.sym_var("align_8", "UNUSED static long long"),

	# stone
	0x0301C2C0: main.sym_var("vtx_stone", "static Vtx", "[]"),
	0x0301C300: main.sym_var("txt_stone", "static u16", "[]"),
	0x0301CB00: main.sym_var("gfx_stone", "Gfx", "[]", flag={"GLOBL"}), # 161
	0x0301CB98: main.sym_var("align_9", "UNUSED static long long"),

	# leaf
	0x0301CBA0: main.sym_var("vtx_leaf", "static Vtx", "[]"),
	0x0301CBE0: main.sym_var("txt_leaf", "static u16", "[]"),
	0x0301CDE0: main.sym_var("gfx_leaf", "Gfx", "[]", flag={"GLOBL"}),
	0x0301CE70: main.sym_var("align_10", "UNUSED static long long"),

	# map
	0x0301CE78: main.sym_var("map_door", "MAP", "[]"),
	0x0301CECC: main.sym_var("map_13002018", "MAP", "[]"), # this is for some platform in LLL
	0x0301CF00: main.sym_var("align_11", "UNUSED static long long"),

	# cap
	0x0301CF08: main.sym_var("light_cap", "static Lights1", "[]"),
	0x0301CF50: main.sym_var("txt_cap_metal", "static u16", "[]"),
	0x0301DF50: main.sym_var("txt_cap_logo", "static u16", "[]"),
	0x0301E750: main.sym_var("txt_cap_wing_l", "static u16", "[]"),
	0x0301F750: main.sym_var("txt_cap_wing_r", "static u16", "[]"),
	0x03020750: main.sym_var("txt_cap_metal_wing_l", "static u16", "[]"),
	0x03021750: main.sym_var("txt_cap_metal_wing_r", "static u16", "[]"),
	0x03022B30: main.sym_var("gfx_cap_logo", "static Gfx", "[]"),
	0x03022B68: main.sym_var("gfx_cap_red", "static Gfx", "[]"),
	0x03022CC8: main.sym_var("gfx_cap_hair", "static Gfx", "[]"),
	0x03022D10: main.sym_var("gfx_cap_shade", "static Gfx", "[]"),
	0x03022E78: main.sym_var("gfx_wings_wing_l", "static Gfx", "[]"),
	0x03022EA8: main.sym_var("gfx_wings_wing_r", "static Gfx", "[]"),
	0x03022ED8: main.sym_var("gfx_wings_start", "static Gfx", "[]"),
	0x03022F20: main.sym_var("gfx_wings_end", "static Gfx", "[]"),
	0x03022F48: main.sym_var("gfx_cap_s", "Gfx", "[]", flag={"GLOBL"}),
	0x03022FF8: main.sym_var("gfx_cap_e", "Gfx", "[]", flag={"GLOBL"}),
	0x030230B0: main.sym_var("gfx_cap_wings_s", "Gfx", "[]", flag={"GLOBL"}),
	0x03023108: main.sym_var("gfx_cap_wings_e", "Gfx", "[]", flag={"GLOBL"}),
	0x03023160: main.sym_var("gfx_wingcap_s", "Gfx", "[]", flag={"GLOBL"}),
	0x03023298: main.sym_var("gfx_wingcap_e", "Gfx", "[]", flag={"GLOBL"}),
	0x030233D0: main.sym_var("align_12", "UNUSED static long long"),

	# meter
	0x030233D8: main.sym_var("align_meter", "UNUSED static long long"),
	0x030233E0: main.sym_var("txt_meter_0_l", "static u16", "[]"),
	0x030243E0: main.sym_var("txt_meter_0_r", "static u16", "[]"),
	0x030253E0: main.sym_var("txt_meter_8", "static u16", "[]"),
	0x03025BE0: main.sym_var("txt_meter_7", "static u16", "[]"),
	0x030263E0: main.sym_var("txt_meter_6", "static u16", "[]"),
	0x03026BE0: main.sym_var("txt_meter_5", "static u16", "[]"),
	0x030273E0: main.sym_var("txt_meter_4", "static u16", "[]"),
	0x03027BE0: main.sym_var("txt_meter_3", "static u16", "[]"),
	0x030283E0: main.sym_var("txt_meter_2", "static u16", "[]"),
	0x03028BE0: main.sym_var("txt_meter_1", "static u16", "[]"),
	0x030293E0: main.sym_var("txt_meter_n", "u16 *", "[]"),
	0x03029400: main.sym_var("vtx_meter_0", "static Vtx", "[]"),
	0x03029480: main.sym_var("gfx_meter_0", "Gfx", "[]", flag={"GLOBL"}),
	0x03029530: main.sym_var("vtx_meter_n", "static Vtx", "[]"),
	0x03029570: main.sym_var("gfx_meter_n", "Gfx", "[]", flag={"GLOBL"}),
	0x030295A0: main.sym_var("gfx_meter_end", "Gfx", "[]", flag={"GLOBL"}),
	0x030295D8: main.sym_var("align_13", "UNUSED static long long"),

	# number
	0x030295E0: main.sym_var("align_14", "UNUSED static long long"),

	# 1up
	0x030295E8: main.sym_var("vtx_1up", "static Vtx", "[]"),
	0x03029628: main.sym_var("txt_1up", "static u16", "[]"),
	0x0302A628: main.sym_var("gfx_1up_1up", "static Gfx", "[]"),
	0x0302A660: main.sym_var("gfx_1up", "Gfx", "[]", flag={"GLOBL"}),
	0x0302A6D0: main.sym_var("align_15", "UNUSED static long long"),

	# powerstar
	0x0302A6D8: main.sym_var("light_powerstar_star", "static Lights1", "[]"),
	0x0302A6F0: main.sym_var("txt_powerstar_star", "static u16", "[]"),
	0x0302AEF0: main.sym_var("txt_powerstar_eye", "static u16", "[]"),
	0x0302B7B0: main.sym_var("gfx_powerstar_star_shade", "static Gfx", "[]"),
	0x0302B870: main.sym_var("gfx_powerstar_star", "Gfx", "[]", flag={"GLOBL"}),
	0x0302B908: main.sym_var("light_powerstar_eyes", "static Lights1", "[]"),
	0x0302B9C0: main.sym_var("gfx_powerstar_eyes_shade", "static Gfx", "[]"),
	0x0302BA18: main.sym_var("gfx_powerstar_eyes", "Gfx", "[]", flag={"GLOBL"}),
	0x0302BA88: main.sym_var("align_16", "UNUSED static long long"),

	# sand
	0x0302BA90: main.sym_var("vtx_sand", "static Vtx", "[]"),
	0x0302BAD0: main.sym_var("txt_sand", "static u16", "[]"),
	0x0302BCD0: main.sym_var("gfx_sand", "Gfx", "[]", flag={"GLOBL"}), # 159
	0x0302BD60: main.sym_var("align_17", "UNUSED static long long"),

	# shard
	0x0302BD68: main.sym_var("light_shard", "static Lights1", "[]"),
	0x0302BDC8: main.sym_var("vtx_shard_cork", "static Vtx", "[]"),
	0x0302BDF8: main.sym_var("txt_shard_cork", "static u16", "[]"),
	0x0302BFF8: main.sym_var("gfx_shard_cork_cork", "static Gfx", "[]"),
	0x0302C028: main.sym_var("gfx_shard_cork", "Gfx", "[]", flag={"GLOBL"}),
	0x0302C098: main.sym_var("vtx_shard_s", "static Vtx", "[]"),
	0x0302C0C8: main.sym_var("vtx_shard_y", "static Vtx", "[]"),
	0x0302C0F8: main.sym_var("vtx_star_s", "static Vtx", "[]"),
	0x0302C198: main.sym_var("vtx_star_y", "static Vtx", "[]"),
	0x0302C238: main.sym_var("gfx_star_s", "static Gfx", "[]"),
	0x0302C298: main.sym_var("gfx_star_sr", "Gfx", "[]", flag={"GLOBL"}),
	0x0302C2B8: main.sym_var("gfx_star_sg", "Gfx", "[]", flag={"GLOBL"}),
	0x0302C2D8: main.sym_var("gfx_star_sb", "Gfx", "[]", flag={"GLOBL"}),
	0x0302C2F8: main.sym_var("gfx_star_sy", "Gfx", "[]", flag={"GLOBL"}),
	0x0302C318: main.sym_var("gfx_star_y", "Gfx", "[]", flag={"GLOBL"}),
	0x0302C378: main.sym_var("gfx_shard_sr", "Gfx", "[]", flag={"GLOBL"}),
	0x0302C3B0: main.sym_var("gfx_shard_sg", "Gfx", "[]", flag={"GLOBL"}),
	0x0302C3E8: main.sym_var("gfx_shard_sb", "Gfx", "[]", flag={"GLOBL"}),
	0x0302C420: main.sym_var("gfx_shard_sy", "Gfx", "[]", flag={"GLOBL"}),
	0x0302C458: main.sym_var("gfx_shard_y", "Gfx", "[]", flag={"GLOBL"}),
	0x0302C480: main.sym_var("align_18", "UNUSED static long long"),

	# shadestar
	0x0302C488: main.sym_var("light_shadestar", "static Lights1", "[]"),
	0x0302C560: main.sym_var("gfx_shadestar_shade", "static Gfx", "[]"),
	0x0302C620: main.sym_var("gfx_shadestar", "Gfx", "[]", flag={"GLOBL"}),
	0x0302C658: main.sym_var("align_19", "UNUSED static long long"),

	# snow
	0x0302C660: main.sym_var("vtx_snow", "static Vtx", "[]"),
	0x0302C6A0: main.sym_var("txt_snow", "static u16", "[]"),
	0x0302C8A0: main.sym_var("gfx_snow", "Gfx", "[]", flag={"GLOBL"}), # 158
	0x0302C938: main.sym_var("align_20", "UNUSED static long long"),

	# signpost
	0x0302C940: main.sym_var("light_signpost_post", "static Lights1", "[]"),
	0x0302C9C8: main.sym_var("txt_signpost_wood", "static u16", "[]"),
	0x0302D1C8: main.sym_var("txt_signpost_face", "static u16", "[]"),
	0x0302D9C8: main.sym_var("gfx_signpost_post_wood", "static Gfx", "[]"),
	0x0302DA48: main.sym_var("gfx_signpost_post", "Gfx", "[]", flag={"GLOBL"}),
	0x0302DAA8: main.sym_var("light_signpost_sign", "static Lights1", "[]"),
	0x0302DC40: main.sym_var("gfx_signpost_sign_wood", "static Gfx", "[]"),
	0x0302DCD0: main.sym_var("gfx_signpost_sign_face", "static Gfx", "[]"),
	0x0302DD08: main.sym_var("gfx_signpost_sign", "Gfx", "[]", flag={"GLOBL"}),
	0x0302DD80: main.sym_var("map_signpost", "MAP", "[]"),
	0x0302DE08: main.sym_var("align_21", "UNUSED static long long"),

	# tree
	0x0302DE10: main.sym_var("light_tree", "static Lights1", "[]"),
	0x0302DE28: main.sym_var("txt_tree_a_l", "static u16", "[]"),
	0x0302EE28: main.sym_var("txt_tree_a_r", "static u16", "[]"),
	0x0302FE88: main.sym_var("gfx_tree_a_l", "static Gfx", "[]"),
	0x0302FEB8: main.sym_var("gfx_tree_a_r", "static Gfx", "[]"),
	0x0302FEE8: main.sym_var("gfx_tree_a", "Gfx", "[]", flag={"GLOBL"}),
	0x0302FF60: main.sym_var("txt_tree_b", "static u16", "[]"),
	0x03030FA0: main.sym_var("gfx_tree_b", "Gfx", "[]", flag={"GLOBL"}),
	0x03031048: main.sym_var("txt_tree_c", "static u16", "[]"),
	0x03032088: main.sym_var("gfx_tree_c", "Gfx", "[]", flag={"GLOBL"}),
	0x03032170: main.sym_var("gfx_tree_d", "Gfx", "[]", flag={"GLOBL"}),
	0x03032218: main.sym_var("txt_tree_e", "static u16", "[]"),
	0x03033258: main.sym_var("gfx_tree_e", "Gfx", "[]", flag={"GLOBL"}),
	0x03033300: main.sym_var("align_22", "UNUSED static long long"),

	# puff
	0x16000000: main.sym_var("s_whitepuff", "SHPLANG", "[]", flag={"GLOBL"}), # 142
	0x16000020: main.sym_var("s_blackpuff", "SHPLANG", "[]", flag={"GLOBL"}), # 224

	# explosion
	0x16000040: main.sym_var("s_explosion", "SHPLANG", "[]", flag={"GLOBL"}), # 205

	# butterfly
	0x160000A8: main.sym_var("s_butterfly", "SHPLANG", "[]", flag={"GLOBL"}), # 187

	# coin
	0x1600013C: main.sym_var("s_coin", "SHPLANG", "[]", flag={"GLOBL"}), # 116
	0x160001A0: main.sym_var("s_coin_noshadow", "SHPLANG", "[]", flag={"GLOBL"}), # 117
	0x16000200: main.sym_var("s_bluecoin", "SHPLANG", "[]", flag={"GLOBL"}), # 118
	0x16000264: main.sym_var("s_bluecoin_noshadow", "SHPLANG", "[]", flag={"GLOBL"}), # 119
	0x160002C4: main.sym_var("s_redcoin", "SHPLANG", "[]", flag={"GLOBL"}), # 215
	0x16000328: main.sym_var("s_redcoin_noshadow", "SHPLANG", "[]", flag={"GLOBL"}), # 216

	# pipe
	0x16000388: main.sym_var("s_pipe", "SHPLANG", "[]", flag={"GLOBL"}), # 18, 22, 73, local

	# door
	0x160003A8: main.sym_var("s_door_a", "SHPLANG", "[]", flag={"GLOBL"}), # 28, 38, local
	0x1600043C: main.sym_var("s_door_a_noback", "SHPLANG", "[]", flag={"GLOBL"}), # 39, local
	0x160004D0: main.sym_var("s_door_b", "SHPLANG", "[]", flag={"GLOBL"}), # 29, 39, local
	0x16000564: main.sym_var("s_door_c", "SHPLANG", "[]", flag={"GLOBL"}), # 30, 40? unused
	0x160005F8: main.sym_var("s_door_d", "SHPLANG", "[]", flag={"GLOBL"}), # 31, 41, local
	0x1600068C: main.sym_var("s_door_e", "SHPLANG", "[]", flag={"GLOBL"}), # 32, local
	0x16000720: main.sym_var("s_door_f", "SHPLANG", "[]", flag={"GLOBL"}), # 29, local
	0x160007B4: main.sym_var("s_stardoor", "SHPLANG", "[]", flag={"GLOBL"}), # 34, local
	0x16000868: main.sym_var("s_stardoor1", "SHPLANG", "[]", flag={"GLOBL"}), # 35, local
	0x1600091C: main.sym_var("s_stardoor3", "SHPLANG", "[]", flag={"GLOBL"}), # 36, local
	0x160009D0: main.sym_var("s_keydoor", "SHPLANG", "[]", flag={"GLOBL"}), # 37, local

	# doorkey
	0x16000A84: main.sym_var("s_bowserkey", "SHPLANG", "[]", flag={"GLOBL"}), # 204
	0x16000AB0: main.sym_var("s_doorkey", "SHPLANG", "[]", flag={"GLOBL"}), # 200

	# flame
	0x16000B10: main.sym_var("s_flame_shadow", "SHPLANG", "[]", flag={"GLOBL"}), # 203
	0x16000B2C: main.sym_var("s_flame", "SHPLANG", "[]", flag={"GLOBL"}), # 144
	0x16000B8C: main.sym_var("s_blueflame", "SHPLANG", "[]", flag={"GLOBL"}), # 145

	# fish
	0x16000BEC: main.sym_var("s_fish_shadow", "SHPLANG", "[]", flag={"GLOBL"}), # 186
	0x16000C44: main.sym_var("s_fish", "SHPLANG", "[]", flag={"GLOBL"}), # 185

	# leaf
	0x16000C8C: main.sym_var("s_leaf", "SHPLANG", "[]", flag={"GLOBL"}), # 162

	# cap
	0x16000CA4: main.sym_var("s_cap_s", "SHPLANG", "[]", flag={"GLOBL"}), # 136
	0x16000CF0: main.sym_var("s_cap_e", "SHPLANG", "[]", flag={"GLOBL"}), # 134
	0x16000D3C: main.sym_var("s_wingcap_s", "SHPLANG", "[]", flag={"GLOBL"}), # 135
	0x16000DA8: main.sym_var("s_wingcap_e", "SHPLANG", "[]", flag={"GLOBL"}), # 133

	# number
	0x16000E14: main.sym_var("s_number", "SHPLANG", "[]", flag={"GLOBL"}), # 219

	# 1up
	0x16000E84: main.sym_var("s_1up", "SHPLANG", "[]", flag={"GLOBL"}), # 212

	# powerstar
	0x16000EA0: main.sym_var("s_powerstar", "SHPLANG", "[]", flag={"GLOBL"}), # 122

	# shard
	0x16000ED4: main.sym_var("s_shard", "SHPLANG", "[]", flag={"GLOBL"}), # 138
	0x16000F24: main.sym_var("s_star", "SHPLANG", "[]", flag={"GLOBL"}), # 139

	# shadestar
	0x16000F6C: main.sym_var("s_shadestar", "SHPLANG", "[]", flag={"GLOBL"}), # 121

	# snow
	0x16000F98: main.sym_var("s_snowball", "SHPLANG", "[]", flag={"GLOBL"}), # 160

	# signpost
	0x16000FB4: main.sym_var("s_signpost", "SHPLANG", "[]", flag={"GLOBL"}), # 124

	# tree
	0x16000FE8: main.sym_var("s_tree_a", "SHPLANG", "[]", flag={"GLOBL"}), # 23, local
	0x16001000: main.sym_var("s_tree_b", "SHPLANG", "[]", flag={"GLOBL"}), # 24, local
	0x16001018: main.sym_var("s_tree_c", "SHPLANG", "[]", flag={"GLOBL"}), # 25, local
	0x16001030: main.sym_var("s_tree_d", "SHPLANG", "[]", flag={"GLOBL"}), # 26, unused
	0x16001048: main.sym_var("s_tree_e", "SHPLANG", "[]", flag={"GLOBL"}), # 27, local
}

imm_E0_Global = {
	0x03008E58: 0x030079E8,
	0x03009980: 0x03008FF8,
	0x03009A20: 0x03008FF8,
	0x03013C28: 0x03009CE0,
	0x03013CC8: 0x03009CE0,
	0x03013D78: 0x03009CE0,
	0x03014078: 0x03009CE0,
	0x030140C8: 0x03009CE0,
	0x03014200: 0x03009CE0,
	0x030144C8: 0x03009CE0,
	0x030149C0: 0x03009CE0,
	0x03014B18: 0x03009CE0,
	0x03014BC8: 0x03009CE0,
	0x03014C78: 0x03009CE0,
	0x03014D28: 0x03009CE0,
	0x03014DD8: 0x03009CE0,
	0x03014EF0: 0x03009CE0,
	0x03014FF0: 0x03009CE0,
	0x03015060: 0x03009CE0,
	0x030150D0: 0x03009CE0,
	0x03015140: 0x03009CE0,
	0x030151B0: 0x03009CE0,
	0x030161F8: 0x030156E0,
	0x0301BED8: 0x0301B5C8,
	0x0301C0C0: 0x0301B5C8,
	0x03022D18: 0x0301CF08,
	0x03022F98: 0x0301CF08,
	0x03023050: 0x0301CF08,
	0x030231B0: 0x0301CF08,
	0x030232F0: 0x0301CF08,
	0x0302B7B0: 0x0302A6D8,
	0x0302B9D8: 0x0302B908,
	0x0302C298: 0x0302BD68,
	0x0302C2B8: 0x0302BD68,
	0x0302C2D8: 0x0302BD68,
	0x0302C2F8: 0x0302BD68,
	0x0302C378: 0x0302BD68,
	0x0302C3B0: 0x0302BD68,
	0x0302C3E8: 0x0302BD68,
	0x0302C420: 0x0302BD68,
	0x0302C560: 0x0302C488,
	0x0302D9E0: 0x0302C940,
	0x0302DC58: 0x0302DAA8,
	0x03030FF8: 0x0302DE10,
	0x030320E0: 0x0302DE10,
	0x030321C8: 0x0302DE10,
	0x030332B0: 0x0302DE10,
}
