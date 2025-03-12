import main
import ultra

import UNSM.c
from . import d_texture_n

################################################################################
# Player
################################################################################

mario_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "mario", [
		("blue", (0.5, 0x00, 0x00, 0xFF)),
		("red", (0.5, 0xFF, 0x00, 0x00)),
		("white", (0.5, 0xFF, 0xFF, 0xFF)),
		("shoe", (0.5, 0x72, 0x1C, 0x0E)),
		("skin", (0.5, 0xFE, 0xC1, 0x79)),
		("hair", (0.5, 0x73, 0x06, 0x00)),
		("button", (0.5, 0xFF, 0xFF, 0xFF), ("button.rgba16.png", 32, 32)),
		("logo", (0.5, 0xFF, 0xFF, 0xFF), ("logo.rgba16.png", 32, 32)),
		("sideburn", (0.5, 0xFF, 0xFF, 0xFF), ("sideburn.rgba16.png", 32, 32)),
		("moustache", (0.5, 0xFF, 0xFF, 0xFF), ("moustache.rgba16.png", 32, 32)),
		("eyes", (0.5, 0xFF, 0xFF, 0xFF), ("eyes_open.rgba16.png", 32, 32)),
		("wing_l", (0.5, 0xFF, 0xFF, 0xFF), ("wing_l.rgba16.png", 32, 64)),
		("wing_r", (0.5, 0xFF, 0xFF, 0xFF), ("wing_r.rgba16.png", 32, 64)),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04000000, 0x0400C090, [
		[0, -6, 1, UNSM.c.d_light, 0.5],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "metal"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "button"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "logo"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "sideburn"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "moustache"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eyes_open"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eyes_half"],
		[0, 3, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eyes_closed"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eyes_left"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eyes_right"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eyes_up"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eyes_down"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eyes_dead"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "wing_l"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "wing_r"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "metal_wing_l"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "metal_wing_r"],
	]],
	[UNSM.c.f_gltf_mesh, "h_waist", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400CA00, 0x0400CD40, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400CD40, "h_waist", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_uarmL", [
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400D090, 0x0400D1F8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400D1F8, "h_uarmL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_larmL", [
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400D2F8, 0x0400D3E8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400D3E8, "h_larmL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_fistL", [
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400D758, 0x0400D910, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400D910, "h_fistL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_uarmR", [
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400DCA0, 0x0400DE08, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400DE08, "h_uarmR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_larmR", [
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400DF08, 0x0400DFF8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400DFF8, "h_larmR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_fistR", [
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400E2C8, 0x0400E4A8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400E4A8, "h_fistR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_thighL", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400E6A8, 0x0400E858, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400E858, "h_thighL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_shinL", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400E918, 0x0400E9C8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400E9C8, "h_shinL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_shoeL", [
		(True, "shoe"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400EBB8, 0x0400ECC0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400ECC0, "h_shoeL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_thighR", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400EEB0, 0x0400EFD8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400EFD8, "h_thighR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_shinR", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400F1D8, 0x0400F290, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400F290, "h_shinR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_shoeR", [
		(True, "shoe"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400F400, 0x0400F568, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0400F568, "h_shoeR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "h_torso", [
		(True, "button"),
		(True, "red"),
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0400FF28, 0x04010410, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04010410, "h_torso", 0, 2, 1],
	]],
	[UNSM.c.f_gltf_mesh, "h_cap", [
		(True, "logo"),
		(True, "eyes"),
		(True, "sideburn"),
		(True, "moustache"),
		(True, "red"),
		(True, "skin"),
		(True, "hair"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x040112B0, 0x04012190, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04012160, "h_cap", 0, 1, 2, 3, 5, 4, 6],
		[0, -2, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "h_hair", [
		(True, "eyes"),
		(True, "sideburn"),
		(True, "moustache"),
		(True, "skin"),
		(True, "hair"),
	]],
	[UNSM.c.f_gltf_mesh, "h_hair.001", [
		(True, "skin"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x040132B0, 0x04014098, [
		[0, 1, 1, UNSM.c.d_gfx, 0x040136B8, "h_hair", 0, 2, 1, 3],
		[0, 1, 1, UNSM.c.d_gfx, 0x04014098,
			"h_hair.001", 0,
			"h_hair", 4,
		],
	]],
	[UNSM.c.f_gltf_mesh, "m_waist", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x040144D8, 0x040146E0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x040146E0, "m_waist", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_uarmL", [
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x040147D0, 0x04014860, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04014860, "m_uarmL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_larmL", [
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04014950, 0x040149C0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x040149C0, "m_larmL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_fistL", [
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04014C90, 0x04014DE0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04014DE0, "m_fistL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_uarmR", [
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04014ED0, 0x04014F60, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04014F60, "m_uarmR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_larmR", [
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04015050, 0x040150C0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x040150C0, "m_larmR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_fistR", [
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x040153B0, 0x04015530, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04015530, "m_fistR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_thighL", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04015620, 0x04015758, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04015758, "m_thighL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_shinL", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04015848, 0x040158D8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x040158D8, "m_shinL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_shoeL", [
		(True, "shoe"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04015A98, 0x04015B80, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04015B80, "m_shoeL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_thighR", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04015C70, 0x04015D20, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04015D20, "m_thighR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_shinR", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04015E10, 0x04015EA0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04015EA0, "m_shinR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_shoeR", [
		(True, "shoe"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04016000, 0x04016148, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04016148, "m_shoeR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "m_torso", [
		(True, "button"),
		(True, "red"),
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04016668, 0x04016968, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04016968, "m_torso", 0, 2, 1],
	]],
	[UNSM.c.f_gltf_mesh, "l_waist", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04016A18, 0x04016B60, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04016B60, "l_waist", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_uarmL", [
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04016C20, 0x04016C90, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04016C90, "l_uarmL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_larmL", [
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04016D50, 0x04016DA0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04016DA0, "l_larmL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_fistL", [
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04016E20, 0x04016EA0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04016EA0, "l_fistL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_uarmR", [
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04016F60, 0x04016FD0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04016FD0, "l_uarmR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_larmR", [
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04017090, 0x040170E0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x040170E0, "l_larmR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_fistR", [
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04017160, 0x04017210, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04017210, "l_fistR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_thighL", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x040172F0, 0x04017408, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04017408, "l_thighL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_shinL", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x040174E8, 0x04017558, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04017558, "l_shinL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_shoeL", [
		(True, "shoe"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04017638, 0x040176C8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x040176C8, "l_shoeL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_thighR", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x040177A8, 0x04017838, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04017838, "l_thighR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_shinR", [
		(True, "blue"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04017918, 0x04017988, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04017988, "l_shinR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_shoeR", [
		(True, "shoe"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04017A68, 0x04017B58, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04017B58, "l_shoeR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "l_torso", [
		(True, "button"),
		(True, "blue"),
		(True, "red"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04017D68, 0x04017F40, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04017F40, "l_torso", 0, 1, 2],
	]],
	[UNSM.c.f_gltf_mesh, "l_cap", [
		(True, "logo"),
		(True, "eyes"),
		(True, "moustache"),
		(True, "red"),
		(True, "skin"),
		(True, "hair"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04018270, 0x04018B18, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04018B18, "l_cap", 0, 1, 2, 4, 3, 5],
	]],
	[UNSM.c.f_gltf_mesh, "l_hair", [
		(True, "eyes"),
		(True, "moustache"),
		(True, "skin"),
		(True, "hair"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04018DC8, 0x04019538, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04019538, "l_hair", 0, 1, 2, 3],
	]],
	[UNSM.c.f_gltf_mesh, "handL", [
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04019A68, 0x04019CC0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x04019CC0, "handL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "handR", [
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0401A1F0, 0x0401A478, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0401A478, "handR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "capR", [
		(True, "logo"),
		(True, "white"),
		(True, "red"),
		(True, "hair"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0401ABA8, 0x0401AF60, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0401AF60, "capR", 0, 2, 1, 3],
	]],
	[UNSM.c.f_gltf_mesh, "wingsR", [
		(True, "wing_l"),
		(True, "wing_r"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0401B080, 0x0401B2D0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0401B2D0, "wingsR", 0, 1],
	]],
	[UNSM.c.f_gltf_mesh, "peaceR", [
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0401BC80, 0x0401BF50, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0401BF50, "peaceR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "cap", [
		(True, "logo"),
		(True, "red"),
		(True, "hair"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0401C330, 0x0401C538, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0401C538, "cap", 0, 1, 2],
	]],
	[UNSM.c.f_gltf_mesh, "wings", [
		(True, "wing_l"),
		(True, "wing_r"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0401C678, 0x0401C940, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0401C940, "wings", 0, 1],
	]],
	[UNSM.c.f_gltf_mesh, "wing", [
		(True, "wing_l"),
		(True, "wing_r"),
	]],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0401C9C0, 0x0401CD20, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0401CD20, "wing", 0, 1],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.code.text", 0x80276F90, 0x80277B14],
	[ultra.c.f_extern, "E0.code.text", 0x80277D6C, 0x80277ED4],
	[ultra.c.f_extern, "E0.code.text", 0x802B1BB0, 0x802B1C54],
	[ultra.c.f_extern, "E0.Player.Gfx", 0x04000000, 0x0401CD20],
	[ultra.c.f_data, "E0.Player.Shp", 0x170002E0, 0x17002E30, [
		[0, 1, 1, UNSM.c.d_shplang, 0x17002E30],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

bubble_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0401CD20, 0x0401DE60, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "a"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "b"],
		[0, 1, 1, ultra.c.d_Gfx, 0x0401DE60],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Player.Gfx", 0x0401CD20, 0x0401DE60],
	[ultra.c.f_data, "E0.Player.Shp", 0x17000000, 0x17000038, [
		[0, 1, 1, UNSM.c.d_shplang, 0x17000038],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

dust_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0401DE60, 0x040217C0, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		d_texture_n("ia16", 32, 32, 7),
		[0, 1, 1, ultra.c.d_Gfx, 0x040217C0],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Player.Gfx", 0x0401DE60, 0x040217C0],
	[ultra.c.f_data, "E0.Player.Shp", 0x17000038, 0x17000084, [
		[0, 1, 1, UNSM.c.d_shplang, 0x17000084],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

smoke_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Player.Gfx", 0x040217C0, 0x040220C8, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "smoke"],
		[0, 1, 1, ultra.c.d_Gfx, 0x040220C8],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Player.Gfx", 0x040217C0, 0x040220C8],
	[ultra.c.f_data, "E0.Player.Shp", 0x17000084, 0x1700009C, [
		[0, 1, 1, UNSM.c.d_shplang, 0x1700009C],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

wave_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Player.Gfx", 0x040220C8, 0x04025318, [
		[0, -8, 1, ultra.c.d_Vtx, False],
		d_texture_n("ia16", 32, 32, 6),
		[0, 1, 1, ultra.c.d_Gfx, 0x04025318],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Player.Gfx", 0x040220C8, 0x04025318],
	[ultra.c.f_data, "E0.Player.Shp", 0x1700009C, 0x17000124, [
		[0, 1, 1, UNSM.c.d_shplang, 0x17000124],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

ripple_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04025318, 0x04027450, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		d_texture_n("ia16", 32, 32, 4),
		[0, 1, 1, ultra.c.d_Gfx, 0x04027450],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Player.Gfx", 0x04025318, 0x04027450],
	[ultra.c.f_data, "E0.Player.Shp", 0x17000124, 0x170001BC, [
		[0, 1, 1, UNSM.c.d_shplang, 0x170001BC],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

sparkle_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04027450, 0x0402A588, [
		[0, -4, 1, ultra.c.d_Vtx, True],
		d_texture_n("rgba16", 32, 32, 6),
		[0, 1, 1, ultra.c.d_Gfx, 0x0402A588],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Player.Gfx", 0x04027450, 0x0402A588],
	[ultra.c.f_data, "E0.Player.Shp", 0x170001BC, 0x17000230, [
		[0, 1, 1, UNSM.c.d_shplang, 0x17000230],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

splash_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Player.Gfx", 0x0402A588, 0x04032700, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		d_texture_n("rgba16", 32, 64, 8),
		[0, 1, 1, ultra.c.d_Gfx, 0x04032700],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Player.Gfx", 0x0402A588, 0x04032700],
	[ultra.c.f_data, "E0.Player.Shp", 0x17000230, 0x17000284, [
		[0, 1, 1, UNSM.c.d_shplang, 0x17000284],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

droplet_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04032700, 0x04032A48, [
		[0, -8, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, "droplet"],
		[0, 1, 1, ultra.c.d_Gfx, 0x04032A48],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

glow_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Player.Gfx", 0x04032A48, 0x04035378, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		d_texture_n("ia16", 32, 32, 5),
		[0, 1, 1, ultra.c.d_Gfx, 0x04035378],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Player.Gfx", 0x04032A48, 0x04035378],
	[ultra.c.f_data, "E0.Player.Shp", 0x17000284, 0x170002E0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x170002E0],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

seq_player = [
	[main.s_file, "shape/player/mario/shape.c", mario_shape],
	[main.s_file, "shape/player/bubble/shape.c", bubble_shape],
	[main.s_file, "shape/player/dust/shape.c", dust_shape],
	[main.s_file, "shape/player/smoke/shape.c", smoke_shape],
	[main.s_file, "shape/player/wave/shape.c", wave_shape],
	[main.s_file, "shape/player/ripple/shape.c", ripple_shape],
	[main.s_file, "shape/player/sparkle/shape.c", sparkle_shape],
	[main.s_file, "shape/player/splash/shape.c", splash_shape],
	[main.s_file, "shape/player/droplet/shape.c", droplet_shape],
	[main.s_file, "shape/player/glow/shape.c", glow_shape],
]

################################################################################
# Shape1A
################################################################################

shape1a_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Shape1A.Shp", 0x0C000000, 0x0C000410, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0C000410],
	]],
]

seq_shape1a = [
	[main.s_bin, "shape/1a/gfx.bin", "E0.Shape1A.Gfx", 0x05000000, 0x05015360],
	[main.s_file, "shape/1a/shp.c", shape1a_shp],
]

################################################################################
# Shape1B
################################################################################

bully_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "bully", [
		("horn", None, ("horn.rgba16.png", 16, 16)),
		("shoe", (0.25, 0x00, 0xE3, 0x00)),
		("eye_old", (0.25, 0xFF, 0xFF, 0xFF), ("eye.rgba16.png", 32, 32)),
		("body_old", (0.25, 0x00, 0x00, 0x00)),
		("body_l", None, ("body_l.rgba16.png", 32, 64)),
		("body_r", None, ("body_r.rgba16.png", 32, 64)),
		("eye", None, ("eye.rgba16.png", 32, 32)),
	]],
	[UNSM.c.f_gltf_mesh, "horn", [
		(False, "horn"),
	]],
	[ultra.c.f_data, "E0.Shape1B.Gfx", 0x050000E0, 0x05002C68, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, "horn"],
		[0, 1, 1, UNSM.c.d_gfx, 0x05000408, "horn", 0],
		[0, -4, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "body_l"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "body_r"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eye"],
	]],
	[UNSM.c.f_gltf_mesh, "shoeL", [
		(True, "shoe"),
	]],
	[UNSM.c.f_gltf_mesh, "shoeR", [
		(True, "shoe"),
	]],
	[UNSM.c.f_gltf_mesh, "eyes_old", [
		(True, "eye_old"),
	]],
	[UNSM.c.f_gltf_mesh, "body_old", [
		(True, "body_old"),
	]],
	[ultra.c.f_data, "E0.Shape1B.Gfx", 0x05003708, 0x05003C50, [
		[0, 1, 1, UNSM.c.d_gfx, 0x05003C50,
			"shoeL", 0,
			"shoeR", 0,
			"eyes_old", 0,
			"body_old", 0,
		],
	]],
	[UNSM.c.f_gltf_mesh, "body", [
		(False, "body_l"),
		(False, "body_r"),
	]],
	[ultra.c.f_data, "E0.Shape1B.Gfx", 0x05003CD0, 0x05003DB8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x05003DB8, "body", 0, 1],
	]],
	[UNSM.c.f_gltf_mesh, "body_big", [
		(False, "body_l"),
		(False, "body_r"),
	]],
	[ultra.c.f_data, "E0.Shape1B.Gfx", 0x05003E38, 0x05003F20, [
		[0, 1, 1, UNSM.c.d_gfx, 0x05003F20, "body_big", 0, 1],
	]],
	[UNSM.c.f_gltf_mesh, "eyes", [
		(False, "eye"),
	]],
	[ultra.c.f_data, "E0.Shape1B.Gfx", 0x05003F80, 0x0500471C, [
		[0, 1, 1, UNSM.c.d_gfx, 0x05004038, "eyes", 0],
		[0, 1, 1, UNSM.c.d_anime, 0x050042A4],
		[0, 1, 1, UNSM.c.d_anime, 0x050043D8],
		[0, 1, 1, UNSM.c.d_anime, 0x05004598],
		[0, 1, 1, UNSM.c.d_anime, 0x050046F4],
		[0, -4, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape1B.Gfx", 0x05000000, 0x05004720],
	[ultra.c.f_data, "E0.Shape1B.Shp", 0x0C000000, 0x0C000240, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0C000240],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

blargg_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "blargg", [
		("lower_jaw", (0.25, 0xFF, 0x36, 0x16)),
		("teeth", (0.25, 0xB2, 0xB2, 0xB2)),
		("upper_jaw", (0.25, 0xFF, 0x2A, 0x1A)),
		("body", (0.25, 0xFF, 0x2E, 0x1F)),
	]],
	[ultra.c.f_data, "E0.Shape1B.Gfx", 0x05004728, 0x050047A0, [
		[0, -5, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "lower_jaw", [
		(True, "teeth"),
		(True, "lower_jaw"),
	]],
	[UNSM.c.f_gltf_mesh, "upper_jaw", [
		(True, "teeth"),
		(True, "upper_jaw"),
	]],
	[UNSM.c.f_gltf_mesh, "body", [
		(True, "body"),
	]],
	[ultra.c.f_data, "E0.Shape1B.Gfx", 0x050058D0, 0x05006174, [
		[0, 1, 1, UNSM.c.d_gfx, 0x05005EB8,
			"lower_jaw", 0, 1,
			"upper_jaw", 0, 1,
			"body", 0,
		],
		[0, 1, 1, UNSM.c.d_anime, 0x05006070],
		[0, 1, 1, UNSM.c.d_anime, 0x05006154],
		[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape1B.Gfx", 0x05004728, 0x05006178],
	[ultra.c.f_data, "E0.Shape1B.Shp", 0x0C000240, 0x0C0002B0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0C0002B0],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

seq_shape1b = [
	[main.s_file, "shape/1b/bully/shape.c", bully_shape],
	[main.s_file, "shape/1b/blargg/shape.c", blargg_shape],
]

################################################################################
# Shape1C
################################################################################

shape1c_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Shape1C.Shp", 0x0C000000, 0x0C000340, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0C000340],
	]],
]

seq_shape1c = [
	[main.s_bin, "shape/1c/gfx.bin", "E0.Shape1C.Gfx", 0x05000000, 0x050110A0],
	[main.s_file, "shape/1c/shp.c", shape1c_shp],
]

################################################################################
# Shape1D
################################################################################

shape1d_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x0302A6D8, 0x0302BA88],
	[ultra.c.f_data, "E0.Shape1D.Shp", 0x0C000000, 0x0C000280, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0C000280],
	]],
]

seq_shape1d = [
	[main.s_bin, "shape/1d/gfx.bin", "E0.Shape1D.Gfx", 0x05000000, 0x05013D30],
	[main.s_file, "shape/1d/shp.c", shape1d_shp],
]

################################################################################
# Shape1E
################################################################################

shape1e_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x03022F48, 0x03022FF8],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x0302A6D8, 0x0302BA88],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x0302C488, 0x0302C658],
	[ultra.c.f_data, "E0.Shape1E.Shp", 0x0C000000, 0x0C000660, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0C000660],
	]],
]

seq_shape1e = [
	[main.s_bin, "shape/1e/gfx.bin", "E0.Shape1E.Gfx", 0x05000000, 0x05014650],
	[main.s_file, "shape/1e/shp.c", shape1e_shp],
]

################################################################################
# Shape1F
################################################################################

shape1f_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x03022F48, 0x03022FF8],
	[ultra.c.f_data, "E0.Shape1F.Shp", 0x0C000000, 0x0C000384, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0C000384],
	]],
]

seq_shape1f = [
	[main.s_bin, "shape/1f/gfx.bin", "E0.Shape1F.Gfx", 0x05000000, 0x050160B8],
	[main.s_file, "shape/1f/shp.c", shape1f_shp],
]

################################################################################
# Shape1G
################################################################################

shape1g_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x03022F48, 0x03022FF8],
	[ultra.c.f_data, "E0.Shape1G.Shp", 0x0C000000, 0x0C000364, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0C000364],
	]],
]

seq_shape1g = [
	[main.s_bin, "shape/1g/gfx.bin", "E0.Shape1G.Gfx", 0x05000000, 0x0500D130],
	[main.s_file, "shape/1g/shp.c", shape1g_shp],
]

################################################################################
# Shape1H
################################################################################

shape1h_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Shape1H.Shp", 0x0C000000, 0x0C000090, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0C000090],
	]],
]

seq_shape1h = [
	[main.s_bin, "shape/1h/gfx.bin", "E0.Shape1H.Gfx", 0x05000000, 0x050034C8],
	[main.s_file, "shape/1h/shp.c", shape1h_shp],
]

################################################################################
# Shape1I
################################################################################

shape1i_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Shape1I.Shp", 0x0C000000, 0x0C0002AC, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0C0002AC],
	]],
]

seq_shape1i = [
	[main.s_bin, "shape/1i/gfx.bin", "E0.Shape1I.Gfx", 0x05000000, 0x05010178],
	[main.s_file, "shape/1i/shp.c", shape1i_shp],
]

################################################################################
# Shape1J
################################################################################

shape1j_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Shape1J.Shp", 0x0C000000, 0x0C000664, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0C00045C],
		[0, 1, 4, None],
		[0, 1, 1, ultra.c.d_s64],
		[0, 1, 1, UNSM.c.d_shplang, 0x0C000664],
	]],
]

seq_shape1j = [
	[main.s_bin, "shape/1j/gfx.bin", "E0.Shape1J.Gfx", 0x05000000, 0x05024200],
	[main.s_file, "shape/1j/shp.c", shape1j_shp],
]

################################################################################
# Shape1K
################################################################################

shape1k_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Shape1K.Shp", 0x0C000000, 0x0C0004A0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0C0004A0],
	]],
]

seq_shape1k = [
	[main.s_bin, "shape/1k/gfx.bin", "E0.Shape1K.Gfx", 0x05000000, 0x05016EC0],
	[main.s_file, "shape/1k/shp.c", shape1k_shp],
]

################################################################################
# Shape2A
################################################################################

shape2a_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Shape2A.Shp", 0x0D000000, 0x0D000C4C, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D000C4C],
	]],
]

seq_shape2a = [
	[main.s_bin, "shape/2a/gfx.bin", "E0.Shape2A.Gfx", 0x06000000, 0x06062F10],
	[main.s_file, "shape/2a/shp.c", shape2a_shp],
]

################################################################################
# Shape2B
################################################################################

skeeter_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "skeeter", [
		("sphere", None, ("sphere.rgba16.png", 32, 32)),
		("iris", None, ("iris.rgba16.png", 16, 8)),
		("foot", (0.5, 0xFF, 0xAA, 0x00)),
		("shade", None),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06000000, 0x06000990, [
		[0, -6, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "sphere"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 8, "iris"],
	]],
	[UNSM.c.f_gltf_mesh, "body", [
		(False, "sphere"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x060009D0, 0x06000A78, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06000A78, "body", 0],
	]],
	[UNSM.c.f_gltf_mesh, "tail_end", [
		(False, "sphere"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06000AB8, 0x06000B60, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06000B60, "tail_end", 0],
	]],
	[UNSM.c.f_gltf_mesh, "eye", [
		(False, "sphere"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06000BA0, 0x06000C48, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06000C48, "eye", 0],
	]],
	[UNSM.c.f_gltf_mesh, "irisR", [
		(False, "iris"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06000C78, 0x06000D18, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06000D18, "irisR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "irisL", [
		(False, "iris"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06000D48, 0x06000E00, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06000DE8, "irisL", 0],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "foot", [
		(True, "foot"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06000E60, 0x06000EF0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06000EF0, "foot", 0],
	]],
	[UNSM.c.f_gltf_mesh, "footBR_old", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "llegBR", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "ulegBR", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "footFR_old", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "llegFR", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "ulegFR", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "footFL_old", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "llegFL", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "ulegFL", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "eyeR_old", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "footBL_old", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "llegBL", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "ulegBL", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "eyeL_old", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "tail_end_old", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "tail", [
		(False, "shade"),
	]],
	[UNSM.c.f_gltf_mesh, "body_old", [
		(False, "shade"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06003FF0, 0x06007DF0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06005720,
			"footBR_old", 0,
			"llegBR", 0,
			"ulegBR", 0,
			"footFR_old", 0,
			"llegFR", 0,
			"ulegFR", 0,
			"footFL_old", 0,
			"llegFL", 0,
			"ulegFL", 0,
			"eyeR_old", 0,
			"footBL_old", 0,
			"llegBL", 0,
			"ulegBL", 0,
			"eyeL_old", 0,
			"tail_end_old", 0,
			"tail", 0,
			"body_old", 0,
		],
		[0, 1, 1, UNSM.c.d_anime, 0x06005D44],
		[0, 1, 1, UNSM.c.d_anime, 0x06006B70],
		[0, 1, 1, UNSM.c.d_anime, 0x060071E0],
		[0, 1, 1, UNSM.c.d_anime, 0x06007DC8],
		[0, -4, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape2B.Gfx", 0x06000000, 0x06007DF0],
	[ultra.c.f_data, "E0.Shape2B.Shp", 0x0D000000, 0x0D000284, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D000284],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

kelp_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "kelp", [
		("0", (0.25, 0xFF, 0xFF, 0xFF), ("0.rgba16.png", 32, 32)),
		("1", (0.25, 0xFF, 0xFF, 0xFF), ("1.rgba16.png", 32, 32)),
		("2", (0.25, 0xFF, 0xFF, 0xFF), ("2.rgba16.png", 32, 32)),
		("3", (0.25, 0xFF, 0xFF, 0xFF), ("3.rgba16.png", 32, 32)),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06007DF8, 0x06009E10, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "0"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "1"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "2"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "3"],
	]],
	[UNSM.c.f_gltf_mesh, "0", [
		(True, "0"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06009E50, 0x06009F08, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06009F08, "0", 0],
	]],
	[UNSM.c.f_gltf_mesh, "1", [
		(True, "1"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06009F48, 0x0600A000, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0600A000, "1", 0],
	]],
	[UNSM.c.f_gltf_mesh, "2", [
		(True, "2"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x0600A040, 0x0600A0F8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0600A0F8, "2", 0],
	]],
	[UNSM.c.f_gltf_mesh, "3", [
		(True, "3"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x0600A138, 0x0600A4D8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0600A1F0, "3", 0],
		[0, 1, 1, UNSM.c.d_anime, 0x0600A4BC],
		[0, -1, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape2B.Gfx", 0x06007DF8, 0x0600A4D8],
	[ultra.c.f_data, "E0.Shape2B.Shp", 0x0D000284, 0x0D0002F4, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D0002F4],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

watermine_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "watermine", [
		("l", None, ("l.rgba16.png", 32, 64)),
		("r", None, ("r.rgba16.png", 32, 64)),
		("spike", (0.25, 0xFF, 0xFF, 0xFF), ("spike.rgba16.png", 32, 32)),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x0600A4E0, 0x0600CCF8, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "l"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "r"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "spike"],
	]],
	[UNSM.c.f_gltf_mesh, "mine", [
		(False, "l"),
		(False, "r"),
	]],
	[UNSM.c.f_gltf_mesh, "spike", [
		(True, "spike"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x0600D1F8, 0x0600D458, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0600D458,
			"mine", 0, 1,
			"spike", 0,
		],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape2B.Gfx", 0x0600A4E0, 0x0600D458],
	[ultra.c.f_data, "E0.Shape2B.Shp", 0x0D0002F4, 0x0D000324, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D000324],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

piranha_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "piranha", [
		("piranha", (0.5, 0xFF, 0xFF, 0xFF), ("piranha.rgba16.png", 32, 32)),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x0600D460, 0x0600DC80, [
		[0, 1, 1, ultra.c.d_s64],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "piranha"],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "body", [
		(True, "piranha"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x0600DD20, 0x0600DE50, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0600DE38, "body", 0],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "fin", [
		(True, "piranha"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x0600DE90, 0x0600DF60, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0600DF48, "fin", 0],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "tail", [
		(True, "piranha"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x0600DFC0, 0x0600E270, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0600E098, "tail", 0],
		[0, 1, 1, UNSM.c.d_anime, 0x0600E24C],
		[0, -1, 1, ultra.c.d_addr, ultra.A_ADDR],
		[0, 1, 1, ultra.c.d_s64],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape2B.Gfx", 0x0600D460, 0x0600E270],
	[ultra.c.f_data, "E0.Shape2B.Shp", 0x0D000324, 0x0D00038C, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D00038C],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

bub_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "bub", [
		("goggles", (0.25, 0xFF, 0xFF, 0xFF), ("goggles.rgba16.png", 32, 32)),
		("fin", (0.25, 0xFF, 0xFF, 0xFF), ("fin.rgba16.png", 32, 32)),
		("eyes", (0.25, 0xFF, 0xFF, 0xFF), ("eyes.rgba16.png", 64, 32)),
		("scale", (0.25, 0xFF, 0xFF, 0xFF), ("scale.rgba16.png", 64, 32)),
		("mouth", (0.25, 0xFF, 0x75, 0x94)),
		("white", (0.25, 0xFF, 0xFF, 0xFF)),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x0600E278, 0x060112A8, [
		[0, -2, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "goggles"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "fin"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "eyes"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "scale"],
	]],
	[UNSM.c.f_gltf_mesh, "body", [
		(True, "goggles"),
		(True, "fin"),
		(True, "eyes"),
		(True, "scale"),
		(True, "mouth"),
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06011848, 0x06011BD8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06011BD8, "body", 0, 1, 2, 3, 4, 5],
	]],
	[UNSM.c.f_gltf_mesh, "tail", [
		(True, "fin"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06011C58, 0x06011D50, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06011D50, "tail", 0],
	]],
	[UNSM.c.f_gltf_mesh, "finL", [
		(True, "fin"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06011DC0, 0x06011EA8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06011EA8, "finL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "finR", [
		(True, "fin"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06011F18, 0x0601235C, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06012000, "finR", 0],
		[0, 1, 1, UNSM.c.d_anime, 0x0601233C],
		[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape2B.Gfx", 0x0600E278, 0x06012360],
	[ultra.c.f_data, "E0.Shape2B.Shp", 0x0D00038C, 0x0D000414, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D000414],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

waterring_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "waterring", [
		("shade", (0.25, 0xFF, 0xFF, 0xFF)),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06012368, 0x06013380, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "waterring"],
	]],
	[UNSM.c.f_gltf_mesh, "waterring", [
		(True, "shade"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06013AC0, 0x06013F84, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06013DD8, "waterring", 0],
		[0, 1, 1, UNSM.c.d_anime, 0x06013F64],
		[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape2B.Gfx", 0x06012368, 0x06013F88],
	[ultra.c.f_data, "E0.Shape2B.Shp", 0x0D000414, 0x0D000450, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D000450],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

chest_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "chest", [
		("keyhole", (0.25, 0xFF, 0xFF, 0xFF), ("keyhole.rgba16.png", 32, 32)),
		("inside", (0.25, 0xFF, 0xFF, 0xFF), ("inside.rgba16.png", 32, 32)),
		("latch", (0.25, 0xFF, 0xFF, 0xFF), ("latch.rgba16.png", 32, 32)),
		("outside", (0.25, 0xFF, 0xFF, 0xFF), ("outside.rgba16.png", 64, 32)),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06013F90, 0x060167A8, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "keyhole"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "inside"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "latch"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "outside"],
	]],
	[UNSM.c.f_gltf_mesh, "box", [
		(True, "keyhole"),
		(True, "latch"),
		(True, "inside"),
		(True, "outside"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06016D58, 0x06017030, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06017030, "box", 0, 1, 2, 3],
	]],
	[UNSM.c.f_gltf_mesh, "lid", [
		(True, "inside"),
		(True, "latch"),
		(True, "outside"),
	]],
	[ultra.c.f_data, "E0.Shape2B.Gfx", 0x06017680, 0x06017958, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06017958, "lid", 0, 1, 2],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape2B.Gfx", 0x06013F90, 0x06017958],
	[ultra.c.f_data, "E0.Shape2B.Shp", 0x0D000450, 0x0D000480, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D000480],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

seq_shape2b = [
	[main.s_file, "shape/2b/skeeter/shape.c", skeeter_shape],
	[main.s_file, "shape/2b/kelp/shape.c", kelp_shape],
	[main.s_file, "shape/2b/watermine/shape.c", watermine_shape],
	[main.s_file, "shape/2b/piranha/shape.c", piranha_shape],
	[main.s_file, "shape/2b/bub/shape.c", bub_shape],
	[main.s_file, "shape/2b/waterring/shape.c", waterring_shape],
	[main.s_file, "shape/2b/chest/shape.c", chest_shape],
]

################################################################################
# Shape2C
################################################################################

shape2c_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Shape2C.Shp", 0x0D000000, 0x0D000678, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D000678],
	]],
]

seq_shape2c = [
	[main.s_bin, "shape/2c/gfx.bin", "E0.Shape2C.Gfx", 0x06000000, 0x06025188],
	[main.s_file, "shape/2c/shp.c", shape2c_shp],
]

################################################################################
# Shape2D
################################################################################

lakitu2_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "lakitu2", [
		("eyes", (0.5, 0xFF, 0xFF, 0xFF), ("eyes_open.rgba16.png", 64, 32)),
		("shell", (0.5, 0xFF, 0xFF, 0xFF), ("shell.rgba16.png", 32, 32)),
		("mouth", (0.5, 0xFF, 0xFF, 0xFF), ("mouth.rgba16.png", 32, 32)),
		("lens", (0.5, 0xFF, 0xFF, 0xFF), ("lens.rgba16.png", 16, 16)),
		("skin", (0.5, 0xF2, 0xAB, 0x00)),
		("camera1", (0.5, 0x19, 0x19, 0x19)),
		("camera2", (0.5, 0x32, 0x44, 0x40)),
		("camera3", (0.5, 0x30, 0x30, 0x30)),
		("rod1", (0.25, 0xA5, 0x4F, 0x1B)),
		("rod4", (0.25, 0x00, 0x00, 0x00)),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06000000, 0x06003A30, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "unused"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "eyes_open"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "eyes_closed"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "shell"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "mouth"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, "lens"],
		[0, -2, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "body", [
		(True, "shell"),
		(True, "skin"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06003C80, 0x06003EB0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06003E98, "body", 0, 1],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "mouth", [
		(True, "mouth"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06004410, 0x060046F8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x060046E0, "mouth", 0],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "armR", [
		(True, "skin"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x060047E8, 0x060048F0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x060048D8, "armR", 0],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "armL", [
		(True, "skin"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x060049E0, 0x06004AE8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06004AD0, "armL", 0],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "eyes", [
		(True, "eyes"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06004BA8, 0x06004D10, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06004CB0, "eyes", 0],
		[0, -4, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "camera", [
		(True, "lens"),
		(True, "camera1"),
		(True, "camera2"),
		(True, "camera3"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x060051D0, 0x06005468, [
		[0, 1, 1, UNSM.c.d_gfx, 0x060053D8, "camera", 0, 1, 2, 3],
		[0, -6, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "rod0", [
		(True, "rod1"),
	]],
	[UNSM.c.f_gltf_mesh, "rod1", [
		(True, "rod4"),
	]],
	[UNSM.c.f_gltf_mesh, "rod2", [
		(True, "rod4"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06005598, 0x060058FC, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06005638,
			"rod0", 0,
			"rod1", 0,
			"rod2", 0,
		],
		[0, 1, 1, UNSM.c.d_anime, 0x060058E0],
		[0, -1, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape2D.Gfx", 0x06000000, 0x06005900],
	[ultra.c.f_data, "E0.Shape2D.Shp", 0x0D000000, 0x0D000114, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D000114],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

toad_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "toad", [
		("face", (0.5, 0xFF, 0xFF, 0xFF), ("face.rgba16.png", 32, 32)),
		("spot", (0.5, 0xFF, 0xFF, 0xFF), ("spot.rgba16.png", 32, 32)),
		("white", (0.5, 0xFF, 0xFF, 0xFF)),
		("vest", (0.5, 0x42, 0x27, 0xB5)),
		("skin", (0.5, 0xFE, 0xD5, 0xA1)),
		("shoe", (0.5, 0x68, 0x40, 0x1B)),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06005908, 0x06006920, [
		[0, -1, 1, UNSM.c.d_light, 0.5],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "face"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "spot"],
	]],
	[UNSM.c.f_gltf_mesh, "head", [
		(True, "face"),
		(True, "spot"),
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06007300, 0x06007820, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06007808, "head", 0, 1, 2],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "vest", [
		(True, "vest"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x060079E0, 0x06007B58, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06007B28, "vest", 0],
		[0, -2, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "body", [
		(True, "white"),
		(True, "skin"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06007DB8, 0x06007F98, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06007F80, "body", 0, 1],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "armR", [
		(True, "skin"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06008168, 0x060082E0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x060082C8, "armR", 0],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "armL", [
		(True, "skin"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06008490, 0x06008668, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06008650, "armL", 0],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "shoeR", [
		(True, "shoe"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06008838, 0x060089C0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x060089A8, "shoeR", 0],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "shoeL", [
		(True, "shoe"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06008B80, 0x0600FC68, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06008CF0, "shoeL", 0],
		[0, 1, 1, UNSM.c.d_anime, 0x0600906C],
		[0, 1, 1, UNSM.c.d_anime, 0x06009400],
		[0, 1, 1, UNSM.c.d_anime, 0x06009AE0],
		[0, 1, 1, UNSM.c.d_anime, 0x0600A1C0],
		[0, 1, 1, UNSM.c.d_anime, 0x0600B75C],
		[0, 1, 1, UNSM.c.d_anime, 0x0600CF68],
		[0, 1, 1, UNSM.c.d_anime, 0x0600E504],
		[0, 1, 1, UNSM.c.d_anime, 0x0600FC30],
		[0, -8, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape2D.Gfx", 0x06005908, 0x0600FC68],
	[ultra.c.f_data, "E0.Shape2D.Shp", 0x0D000114, 0x0D00043C, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D00043C],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

mips_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "mips", [
		("face", (0.4, 0xFF, 0xFF, 0xFF), ("face.rgba16.png", 32, 32)),
		("white", (0.4, 0xFF, 0xFF, 0xFF)),
		("light1", (0.4, 0x27, 0x21, 0x0B)),
		("face1", (0.4, 0x96, 0x96, 0x00), ("face.rgba16.png", 32, 32)),
		("face2", (0.4, 0x85, 0x8E, 0x00), ("face.rgba16.png", 32, 32)),
		("light2", (0.4, 0x82, 0x6E, 0x26)),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x0600FC70, 0x060104A0, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "face"],
		[0, -2, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "0", [
		(True, "face"),
		(True, "light1"),
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x060106F0, 0x06010928, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06010910, "0", 0, 1, 2],
		[0, -1, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "1", [
		(True, "face"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06010B88, 0x06010DC0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06010D90, "1", 0],
		[0, -2, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "2", [
		(True, "face1"),
		(True, "face"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06010EA0, 0x06010FF8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06010FB0, "2", 0, 1],
		[0, -3, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "3", [
		(True, "face1"),
		(True, "face2"),
		(True, "face"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x060110E8, 0x06011230, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06011200, "3", 0, 1, 2],
		[0, -2, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "4", [
		(True, "face1"),
		(True, "face"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06011330, 0x06011490, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06011460, "4", 0, 1],
		[0, -2, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "5", [
		(True, "face1"),
		(True, "face"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06011560, 0x060116A0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06011670, "5", 0, 1],
		[0, -2, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "6", [
		(True, "face1"),
		(True, "face"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x060117A0, 0x06011900, [
		[0, 1, 1, UNSM.c.d_gfx, 0x060118D0, "6", 0, 1],
		[0, -2, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "7", [
		(True, "face1"),
		(True, "face"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x060119D0, 0x06011B10, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06011AE0, "7", 0, 1],
		[0, -2, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "8", [
		(True, "face1"),
		(True, "face"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06011BF0, 0x06011D30, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06011D00, "8", 0, 1],
		[0, -2, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "9", [
		(True, "face1"),
		(True, "face"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06011E00, 0x06011F18, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06011F00, "9", 0, 1],
		[0, -1, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "10", [
		(True, "light2"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06011F78, 0x06012000, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06011FE8, "10", 0],
		[0, -1, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "11", [
		(True, "light2"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06012060, 0x0601573C, [
		[0, 1, 1, UNSM.c.d_gfx, 0x060120D0, "11", 0],
		[0, 1, 1, UNSM.c.d_anime, 0x06013338],
		[0, 1, 1, UNSM.c.d_anime, 0x0601378C],
		[0, 1, 1, UNSM.c.d_anime, 0x06013AE8],
		[0, 1, 1, UNSM.c.d_anime, 0x06014C84],
		[0, 1, 1, UNSM.c.d_anime, 0x0601570C],
		[0, -6, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape2D.Gfx", 0x0600FC70, 0x06015740],
	[ultra.c.f_data, "E0.Shape2D.Shp", 0x0D000440, 0x0D000448, [
		[0, 1, 1, ultra.c.d_s64],
	]],
	[ultra.c.f_data, "E0.Shape2D.Shp", 0x0D000448, 0x0D0005A4, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D0005A4],
	]],
	[ultra.c.f_data, "E0.Shape2D.Shp", 0x0D0005A8, 0x0D0005B0, [
		[0, 1, 1, ultra.c.d_s64],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

boo2_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "boo2", [
		("shade", None),
		("eyes", None, ("eyes.rgba16.png", 64, 32)),
		("mouth", None, ("mouth.rgba16.png", 32, 32)),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06015748, 0x06016F60, [
		[0, 1, 1, ultra.c.d_Lights1],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "eyes"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "mouth"],
	]],
	[UNSM.c.f_gltf_mesh, "boo", [
		(True, "mouth"),
		(True, "eyes"),
		(True, "shade"),
	]],
	[ultra.c.f_data, "E0.Shape2D.Gfx", 0x06017B00, 0x06017E70, [
		[0, 1, 1, UNSM.c.d_gfx, 0x06017E70, "boo", 0, 1, 2],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Shape2D.Gfx", 0x06015748, 0x06017E70],
	[ultra.c.f_data, "E0.Shape2D.Shp", 0x0D0005B0, 0x0D000600, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D000600],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

seq_shape2d = [
	[main.s_file, "shape/2d/lakitu2/shape.c", lakitu2_shape],
	[main.s_file, "shape/2d/toad/shape.c", toad_shape],
	[main.s_file, "shape/2d/mips/shape.c", mips_shape],
	[main.s_file, "shape/2d/boo2/shape.c", boo2_shape],
]

################################################################################
# Shape2E
################################################################################

shape2e_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Shape2E.Shp", 0x0D000000, 0x0D000148, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D000140],
		[0, 1, 1, ultra.c.d_s64],
	]],
]

seq_shape2e = [
	[main.s_bin, "shape/2e/gfx.bin", "E0.Shape2E.Gfx", 0x06000000, 0x06005E78],
	[main.s_file, "shape/2e/shp.c", shape2e_shp],
]

################################################################################
# Shape2F
################################################################################

shape2f_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Shape2F.Shp", 0x0D000000, 0x0D0006D0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0D0006D0],
	]],
]

seq_shape2f = [
	[main.s_bin, "shape/2f/gfx.bin", "E0.Shape2F.Gfx", 0x06000000, 0x06015070],
	[main.s_file, "shape/2f/shp.c", shape2f_shp],
]

################################################################################
# Common
################################################################################

bluecoinsw_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "bluecoinsw", [
		("side", (0.5, 0xFF, 0xFF, 0xFF), ("side.rgba16.png", 32, 16)),
		("top", (0.5, 0xFF, 0xFF, 0xFF), ("top.rgba16.png", 32, 32)),
	]],
	[UNSM.c.f_obj, "bluecoinsw"],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08000000, 0x08000C18, [
		[0, -1, 1, UNSM.c.d_light, 0.5],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 16, "side"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "top"],
	]],
	[UNSM.c.f_gltf_mesh, "bluecoinsw", [
		(True, "side"),
		(True, "top"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08000D58, 0x08000F10, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08000E98, "bluecoinsw", 0, 1],
		[0, 1, 1, UNSM.c.d_map, "map"],
	]],
	[UNSM.c.f_gltf_write],
	[UNSM.c.f_obj_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x08000000, 0x08000F10],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F000000, 0x0F000020, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F000020],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

amp_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "amp", [
		("arc", None, ("arc.rgba16.png", 16, 32)),
		("eyes", None, ("eyes.rgba16.png", 32, 32)),
		("body", None, ("body.rgba16.png", 32, 32)),
		("mouth", None, ("mouth.rgba16.png", 32, 32)),
		("arc_old", (0.25, 0xCF, 0xFF, 0x00)),
		("shade_old", (0.25, 0xFF, 0xFF, 0xFF)), # guess (no entry)
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08000F18, 0x08002B18, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 32, "arc"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eyes"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "body"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "mouth"],
	]],
	[UNSM.c.f_gltf_mesh, "arc", [
		(False, "arc"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08002B68, 0x08002C10, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08002C10, "arc", 0],
	]],
	[UNSM.c.f_gltf_mesh, "eyes", [
		(False, "eyes"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08002C50, 0x08002CF8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08002CF8, "eyes", 0],
	]],
	[UNSM.c.f_gltf_mesh, "mouth", [
		(False, "mouth"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08002D38, 0x08002DE0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08002DE0, "mouth", 0],
	]],
	[UNSM.c.f_gltf_mesh, "body", [
		(False, "body"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08002E20, 0x08002EE0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08002EC8, "body", 0],
		[0, -1, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "arcA_old", [
		(True, "arc_old"),
	]],
	[UNSM.c.f_gltf_mesh, "arcB_old", [
		(True, "arc_old"),
	]],
	[UNSM.c.f_gltf_mesh, "arcC_old", [
		(True, "arc_old"),
	]],
	[UNSM.c.f_gltf_mesh, "arcD_old", [
		(True, "arc_old"),
	]],
	[UNSM.c.f_gltf_mesh, "body_old", [
		(True, "shade_old"),
	]],
	[UNSM.c.f_gltf_mesh, "mouth_old", [
		(True, "shade_old"),
	]],
	[UNSM.c.f_gltf_mesh, "anger_old", [
		(True, "shade_old"),
	]],
	[UNSM.c.f_gltf_mesh, "eyes_old", [
		(True, "shade_old"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08003910, 0x08004038, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08003E30,
			"arcA_old", 0,
			"arcB_old", 0,
			"arcC_old", 0,
			"arcD_old", 0,
			"body_old", 0,
			"mouth_old", 0,
			"anger_old", 0,
			"eyes_old", 0,
		],
		[0, 1, 1, UNSM.c.d_anime, 0x0800401C],
		[0, -1, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x08000F18, 0x08004038],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F000020, 0x0F0001A8, [
		[0, 1, 1, ultra.c.d_s64],
		[0, 1, 1, UNSM.c.d_shplang, 0x0F00019C],
		[0, 1, 4, None],
		[0, 1, 1, ultra.c.d_s64],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

cannonlid_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "cannonlid", [
		("lid", (0.25, 0xFF, 0xFF, 0xFF), ("lid.rgba16.png", 32, 32)),
	]],
	[UNSM.c.f_obj, "cannonlid"],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08004040, 0x08004858, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "lid"],
	]],
	[UNSM.c.f_gltf_mesh, "cannonlid", [
		(True, "lid"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08004898, 0x08004980, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08004950, "cannonlid", 0],
		[0, 1, 1, UNSM.c.d_map, "map"],
	]],
	[UNSM.c.f_gltf_write],
	[UNSM.c.f_obj_write],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

cannon_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "cannon", [
		("side", (0.3, 0xFF, 0xFF, 0xFF), ("side.rgba16.png", 32, 32)),
		("shade", (0.3, 0x30, 0x37, 0xFF)),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08004988, 0x080051B8, [
		[0, -2, 1, UNSM.c.d_light, 0.3],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "side"],
	]],
	[UNSM.c.f_gltf_mesh, "cannon", [
		(True, "side"),
		(True, "shade"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08005658, 0x08005870, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08005870, "cannon", 0, 1],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x08004988, 0x08005870],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F0001A8, 0x0F0001C0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F0001C0],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

cannonbarrel_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "cannonbarrel", [
		("rim", (0.3, 0xFF, 0xFF, 0xFF), ("rim.rgba16.png", 32, 32)),
		("shade", (0.3, 0x00, 0x00, 0x32)),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08005878, 0x080060A8, [
		[0, -2, 1, UNSM.c.d_light, 0.3],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "rim"],
	]],
	[UNSM.c.f_gltf_mesh, "cannonbarrel", [
		(True, "rim"),
		(True, "shade"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08006408, 0x080066C8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x080066C8, "cannonbarrel", 0, 1],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x08005878, 0x080066C8],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F0001C0, 0x0F0001D8, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F0001D8],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

chuckya_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "chuckya", [
		("red", None, ("red.rgba16.png", 32, 32)),
		("purple_l", None, ("purple_l.rgba16.png", 32, 64)),
		("purple_r", None, ("purple_r.rgba16.png", 32, 64)),
		("eyes", (0.4, 0xFF, 0xFF, 0xFF), ("eyes.rgba16.png", 32, 32)),
		("base", (0.3, 0x89, 0x89, 0x8A)),
		("antenna", (0.3, 0xFF, 0xFF, 0x00)),
		("back", (0.25, 0x32, 0x32, 0x32)),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x080066D0, 0x08009F78, [
		[0, -7, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eyes"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "purple"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "red"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "purple_l"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "purple_r"],
	]],
	[UNSM.c.f_gltf_mesh, "body", [
		(False, "purple_l"),
		(False, "purple_r"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08009FF8, 0x0800A0E0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0800A0E0, "body", 0, 1],
	]],
	[UNSM.c.f_gltf_mesh, "armL", [
		(False, "purple_l"),
		(False, "purple_r"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800A160, 0x0800A248, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0800A248, "armL", 0, 1],
	]],
	[UNSM.c.f_gltf_mesh, "armR", [
		(False, "purple_l"),
		(False, "purple_r"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800A2C8, 0x0800A3B0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0800A3B0, "armR", 0, 1],
	]],
	[UNSM.c.f_gltf_mesh, "handL", [
		(False, "red"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800A3F0, 0x0800A498, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0800A498, "handL", 0],
	]],
	[UNSM.c.f_gltf_mesh, "handR", [
		(False, "red"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800A4D8, 0x0800A580, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0800A580, "handR", 0],
	]],
	[UNSM.c.f_gltf_mesh, "antenna_end", [
		(False, "red"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800A5C0, 0x0800A680, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0800A668, "antenna_end", 0],
		[0, -1, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "eyes", [
		(True, "eyes"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800A700, 0x0800A7E0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0800A7C8, "eyes", 0],
		[0, -1, 1, UNSM.c.d_light, 0.3],
	]],
	[UNSM.c.f_gltf_mesh, "base", [
		(True, "base"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800A870, 0x0800A908, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0800A8F0, "base", 0],
		[0, -1, 1, UNSM.c.d_light, 0.3],
	]],
	[UNSM.c.f_gltf_mesh, "antenna", [
		(True, "antenna"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800A958, 0x0800A9D0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0800A9B8, "antenna", 0],
		[0, -1, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "back", [
		(True, "back"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800AB70, 0x0800C088, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0800AC18, "back", 0],
		[0, 1, 1, UNSM.c.d_anime, 0x0800AF68],
		[0, 1, 1, UNSM.c.d_anime, 0x0800B1A8],
		[0, 1, 1, UNSM.c.d_anime, 0x0800B4A8],
		[0, 1, 1, UNSM.c.d_anime, 0x0800B9F8],
		[0, 1, 1, UNSM.c.d_anime, 0x0800BBEC],
		[0, 1, 1, UNSM.c.d_anime, 0x0800C058],
		[0, -6, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x080066D0, 0x0800C088],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F0001D8, 0x0F0004CC, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F0004CC],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

purplesw_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "purplesw", [
		("side", (0.25, 0xFF, 0xFF, 0xFF), ("side.rgba16.png", 16, 4)),
		("top", (0.25, 0xFF, 0xFF, 0xFF), ("top.rgba16.png", 16, 32)),
	]],
	[UNSM.c.f_obj, "purplesw"],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800C090, 0x0800C528, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 4, "side"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 32, "top"],
	]],
	[UNSM.c.f_gltf_mesh, "purplesw", [
		(True, "side"),
		(True, "top"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800C668, 0x0800C820, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0800C7A8, "purplesw", 0, 1],
		[0, 1, 1, UNSM.c.d_map, "map"],
	]],
	[UNSM.c.f_gltf_write],
	[UNSM.c.f_obj_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x0800C090, 0x0800C820],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F0004CC, 0x0F0004E4, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F0004E4],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

lift_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "lift", [
		("side", (0.25, 0xFF, 0xFF, 0xFF), ("side.rgba16.png", 32, 16)),
		("face", (0.25, 0xFF, 0xFF, 0xFF), ("face.rgba16.png", 32, 32)),
	]],
	[UNSM.c.f_obj, "lift"],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800C828, 0x0800D440, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 16, "side"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "face"],
	]],
	[UNSM.c.f_gltf_mesh, "lift", [
		(True, "side"),
		(True, "face"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800D5C0, 0x0800D794, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0800D710, "lift", 0, 1],
		[0, 1, 1, UNSM.c.d_map, "map"],
	]],
	[UNSM.c.f_gltf_write],
	[UNSM.c.f_obj_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x0800C828, 0x0800D798],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F0004E4, 0x0F0004FC, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F0004FC],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

heart_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "heart", [
		("heart", None, ("heart.rgba16.png", 32, 32)),
	]],
	[UNSM.c.f_gltf_mesh, "heart", [
		(False, "heart"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800D7E0, 0x0800E078, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "heart"],
		[0, 1, 1, UNSM.c.d_gfx, 0x0800E078, "heart", 0],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x0800D7E0, 0x0800E078],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F0004FC, 0x0F000518, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F000518],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

flyguy_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "flyguy", [
		("foot", (0.25, 0x02, 0x7F, 0xCC)),
		("shaft", (0.25, 0xFF, 0xC8, 0x23)),
		("propeller", (0.25, 0xFF, 0xFF, 0xFF), ("propeller.ia16.png", 32, 32)),
		("face", (0.5, 0xFF, 0xFF, 0xFF), ("face.rgba16.png", 32, 32)),
		("cloth_black", (0.5, 0x00, 0x00, 0x00), ("cloth.rgba16.png", 64, 32)),
		("cloth_red", (0.5, 0xC4, 0x00, 0x26), ("cloth.rgba16.png", 64, 32)),
		("black", (0.5, 0x00, 0x00, 0x00)),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0800E080, 0x08010130, [
		[0, 1, 1, ultra.c.d_s64],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "cloth"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "face"],
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "propeller"],
		[0, -7, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "footR", [
		(True, "foot"),
	]],
	[UNSM.c.f_gltf_mesh, "footL", [
		(True, "foot"),
	]],
	[UNSM.c.f_gltf_mesh, "shaft", [
		(True, "shaft"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08010840, 0x08010AF8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08010AE0,
			"footR", 0,
			"footL", 0,
			"shaft", 0,
		],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "propeller", [
		(True, "propeller"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08010B38, 0x08010C38, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08010BF0, "propeller", 0],
		[0, -3, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "body", [
		(True, "face"),
		(True, "cloth_black"),
		(True, "cloth_red"),
		(True, "black"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x080113A8, 0x08011A70, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08011798, "body", 0, 1, 2, 3],
		[0, 1, 1, UNSM.c.d_anime, 0x08011A4C],
		[0, -1, 1, ultra.c.d_addr, ultra.A_ADDR],
		[0, 1, 1, ultra.c.d_s64],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x0800E080, 0x08011A70],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F000518, 0x0F0005D0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F0005D0],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

block_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "block", [
		("block", (0.25, 0xFF, 0xFF, 0xFF), ("0.rgba16.png", 32, 32)),
	]],
	[UNSM.c.f_obj, "block"],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08011A78, 0x08012A90, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "0"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "1"],
	]],
	[UNSM.c.f_gltf_mesh, "block", [
		(True, "block"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08012C30, 0x08012E00, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08012D70, "block", 0],
		[0, 1, 1, UNSM.c.d_map, "map"],
		[0, 1, 4, None],
		[0, 1, 1, ultra.c.d_s64],
	]],
	[UNSM.c.f_gltf_write],
	[UNSM.c.f_obj_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x08011A78, 0x08012E00],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F0005D0, 0x0F000640, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F000640],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

ironball_shape = [
	[main.f_str, "#ifdef SCRIPT\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x08022D08, 0x08022D78],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F000640, 0x0F000694, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F000694],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

itembox_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "itembox", [
		("32x64_face", (0.25, 0xFF, 0xFF, 0xFF), ("face_r.rgba16.png", 32, 32)),
		("32x64_side", (0.25, 0xFF, 0xFF, 0xFF), ("side_r.rgba16.png", 32, 64)),
		("64x32_face", (0.25, 0xFF, 0xFF, 0xFF), ("face_y.rgba16.png", 32, 32)),
		("64x32_side", (0.25, 0xFF, 0xFF, 0xFF), ("side_y.rgba16.png", 64, 32)),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08012E10, 0x08018E28, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "face_b"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "side_b"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "face_g"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "side_g"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "face_r"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "side_r"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "face_y"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "side_y"],
	]],
	[UNSM.c.f_gltf_mesh, "32x64", [
		(True, "32x64_face"),
		(True, "32x64_side"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08018FA8, 0x080190A0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x080190A0, "32x64", 0, 1],
	]],
	[UNSM.c.f_gltf_mesh, "64x32", [
		(True, "64x32_face"),
		(True, "64x32_side"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08019220, 0x08019498, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08019498, "64x32", 0, 1],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x08012E10, 0x08019498],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F000694, 0x0F0006E4, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F0006E4],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

goomba_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "goomba", [
		("footL", (0.25, 0x54, 0x2E, 0x10)),
		("footR", (0.25, 0x61, 0x34, 0x13)),
		("head_old", (0.25, 0x77, 0x42, 0x20)),
		("body_old", (0.25, 0xDE, 0xB4, 0x4E)),
		("body", None, ("body.rgba16.png", 32, 32)),
		("head", (0.5, 0xFF, 0xFF, 0xFF), ("head_open.rgba16.png", 32, 32)),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x080194A0, 0x0801AD48, [
		[0, -6, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "body"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "head_open"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "head_closed"],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "head", [
		(True, "head"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0801B2E8, 0x0801B618, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0801B618, "head", 0],
	]],
	[UNSM.c.f_gltf_mesh, "body", [
		(False, "body"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0801B658, 0x0801B700, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0801B700, "body", 0],
	]],
	[UNSM.c.f_gltf_mesh, "footL", [
		(True, "footL"),
	]],
	[UNSM.c.f_gltf_mesh, "footR", [
		(True, "footR"),
	]],
	[UNSM.c.f_gltf_mesh, "head_old", [
		(True, "head_old"),
	]],
	[UNSM.c.f_gltf_mesh, "body_old", [
		(True, "body_old"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0801CE20, 0x0801DA58, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0801D770,
			"footL", 0,
			"footR", 0,
			"head_old", 0,
			"body_old", 0,
		],
		[0, 1, 1, UNSM.c.d_anime, 0x0801DA34],
		[0, -1, 1, ultra.c.d_addr, ultra.A_ADDR],
		[0, 1, 1, ultra.c.d_s64],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x080194A0, 0x0801DA58],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F0006E4, 0x0F0007B8, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F0007B8],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

bobomb_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "bobomb", [
		("eyes", None, ("eyes_open.rgba16.png", 32, 32)),
		("foot", (0.25, 0xFF, 0x99, 0x12)),
		("cap", (0.25, 0xB2, 0xB2, 0xB2)),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x0801DA60, 0x08022A60, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "black_l"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "black_r"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "red_l"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "red_r"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eyes_open"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eyes_closed"],
	]],
	[UNSM.c.f_gltf_mesh, "eyes", [
		(True, "eyes"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08022AC0, 0x08022E30, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08022BB8, "eyes", 0],
		[0, -8, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, ultra.c.d_Gfx, 0x08022DE8],
		[0, -3, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "footR", [
		(True, "foot"),
	]],
	[UNSM.c.f_gltf_mesh, "footL", [
		(True, "foot"),
	]],
	[UNSM.c.f_gltf_mesh, "cap", [
		(True, "cap"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08023270, 0x08023974, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08023528,
			"footR", 0,
			"footL", 0,
			"cap", 0,
		],
		[0, 1, 1, UNSM.c.d_anime, 0x080237FC],
		[0, 1, 1, UNSM.c.d_anime, 0x08023954],
		[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x0801DA60, 0x08023978],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F0007B8, 0x0F000A30, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F000A30],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

pushblock_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "pushblock", [
		("pushblock", (0.5, 0xFF, 0xFF, 0xFF), ("pushblock.rgba16.png", 32, 64)),
	]],
	[UNSM.c.f_obj, "pushblock"],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08023980, 0x08024998, [
		[0, -1, 1, UNSM.c.d_light, 0.5],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "pushblock"],
	]],
	[UNSM.c.f_gltf_mesh, "pushblock", [
		(True, "pushblock"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08024B18, 0x08024CAC, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08024C28, "pushblock", 0],
		[0, 1, 1, UNSM.c.d_map, "map"],
	]],
	[UNSM.c.f_gltf_write],
	[UNSM.c.f_obj_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x08023980, 0x08024CB0],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F000A30, 0x0F000A58, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F000A58],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

dotbox_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "dotbox", [
		("box", (0.5, 0xFF, 0xD4, 0x00)),
		("dot", None, ("dot.rgba16.png", 32, 32)),
		("mark", (0.5, 0xFF, 0xFF, 0xFF), ("mark.rgba16.png", 16, 32)),
	]],
	[UNSM.c.f_obj, "dotbox"],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08024CB8, 0x08024D18, [
		[0, -4, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "box", [
		(True, "box"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08024EB8, 0x08025008, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08025008, "box", 0],
	]],
	[UNSM.c.f_gltf_mesh, "dot", [
		(False, "dot"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08025168, 0x08025E80, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "dot"],
		[0, 1, 1, UNSM.c.d_gfx, 0x08025A68, "dot", 0],
		[0, -1, 1, UNSM.c.d_light, 0.5],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 32, "mark"],
	]],
	[UNSM.c.f_gltf_mesh, "mark", [
		(True, "mark"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08025EC0, 0x08025FFC, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08025F78, "mark", 0],
		[0, 1, 1, UNSM.c.d_map, "map"],
	]],
	[UNSM.c.f_gltf_write],
	[UNSM.c.f_obj_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x08024CB8, 0x08026000],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F000A58, 0x0F000AB0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F000AB0],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

testlift_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "testlift", [
		("shade", (0.25, 0xC8, 0xC8, 0x1E)),
	]],
	[UNSM.c.f_obj, "testlift"],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08026008, 0x08026020, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "testlift", [
		(True, "shade"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08026260, 0x0802637C, [
		[0, 1, 1, UNSM.c.d_gfx, 0x080262F8, "testlift", 0],
		[0, 1, 1, UNSM.c.d_map, "map"],
	]],
	[UNSM.c.f_gltf_write],
	[UNSM.c.f_obj_write],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

shell_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "shell_old", [
		("top", (0.25, 0x45, 0xCD, 0x1A)),
		("bottom", (0.25, 0x84, 0xC3, 0xE5)),
		("side", (0.25, 0xFA, 0xFF, 0xF8)),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08026388, 0x080263E8, [
		[0, -4, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "shell_old", [
		(True, "top"),
		(True, "bottom"),
		(True, "side"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08027108, 0x08027470, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08027470, "shell_old", 0, 1, 2],
	]],
	[UNSM.c.f_gltf_write],
	[UNSM.c.f_gltf, "shell", [
		("top", (0.25, 0xFF, 0xFF, 0xFF), ("top.rgba16.png", 32, 32)),
		("bottom", (0.25, 0xFF, 0xFF, 0xFF), ("bottom.rgba16.png", 32, 32)),
		("front", (0.25, 0xE0, 0xAE, 0x00)),
		("white", (0.25, 0xFF, 0xFF, 0xFF)),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x08027470, 0x080284A0, [
		[0, -2, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "bottom"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "top"],
	]],
	[UNSM.c.f_gltf_mesh, "shell", [
		(True, "top"),
		(True, "bottom"),
		(True, "front"),
		(True, "white"),
	]],
	[ultra.c.f_data, "E0.Common.Gfx", 0x080288E0, 0x08028BE8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x08028BE8, "shell", 0, 1, 2, 3],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Common.Gfx", 0x08026388, 0x08028BE8],
	[ultra.c.f_data, "E0.Common.Shp", 0x0F000AB0, 0x0F000B34, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0F000B34],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

seq_common = [
	[main.s_file, "shape/3common/bluecoinsw/shape.c", bluecoinsw_shape],
	[main.s_file, "shape/3common/amp/shape.c", amp_shape],
	[main.s_file, "shape/3common/cannonlid/shape.c", cannonlid_shape],
	[main.s_file, "shape/3common/cannon/shape.c", cannon_shape],
	[main.s_file, "shape/3common/cannonbarrel/shape.c", cannonbarrel_shape],
	[main.s_file, "shape/3common/chuckya/shape.c", chuckya_shape],
	[main.s_file, "shape/3common/purplesw/shape.c", purplesw_shape],
	[main.s_file, "shape/3common/lift/shape.c", lift_shape],
	[main.s_file, "shape/3common/heart/shape.c", heart_shape],
	[main.s_file, "shape/3common/flyguy/shape.c", flyguy_shape],
	[main.s_file, "shape/3common/block/shape.c", block_shape],
	[main.s_file, "shape/3common/ironball/shape.c", ironball_shape],
	[main.s_file, "shape/3common/itembox/shape.c", itembox_shape],
	[main.s_file, "shape/3common/goomba/shape.c", goomba_shape],
	[main.s_file, "shape/3common/bobomb/shape.c", bobomb_shape],
	[main.s_file, "shape/3common/pushblock/shape.c", pushblock_shape],
	[main.s_file, "shape/3common/dotbox/shape.c", dotbox_shape],
	[main.s_file, "shape/3common/testlift/shape.c", testlift_shape],
	[main.s_file, "shape/3common/shell/shape.c", shell_shape],
]

################################################################################
# Global
################################################################################

puff_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03000000, 0x030009C0, [
		[0, -8, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "puff"],
		[0, 1, 1, ultra.c.d_Gfx, 0x030009C0],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x03000000, 0x030009C0],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000000, 0x16000040, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000040],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

explosion_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x030009C8, 0x03004340, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		d_texture_n("rgba16", 32, 32, 7),
		[0, 1, 1, ultra.c.d_Gfx, 0x03004340],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x030009C8, 0x03004340],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000040, 0x160000A8, [
		[0, 1, 1, UNSM.c.d_shplang, 0x160000A8],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

butterfly_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "butterfly", [
		("wing", None, ("wing.rgba16.png", 32, 64), {"ss": 0.5, "st": 0.5}),
	]],
	[UNSM.c.f_gltf_mesh, "l", [
		(False, "wing"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x030043A8, 0x030053A8, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "wing"],
	]],
	[UNSM.c.f_gltf_mesh, "r", [
		(False, "wing"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03005408, 0x030056B8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x03005538,
			"l", 0,
			"r", 0,
		],
		[0, 1, 1, UNSM.c.d_anime, 0x030055B0],
		[0, 1, 1, UNSM.c.d_anime, 0x03005698],
		[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x03004348, 0x030056B8],
	[ultra.c.f_data, "E0.Global.Shp", 0x160000A8, 0x1600013C, [
		[0, 1, 1, UNSM.c.d_shplang, 0x1600013C],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

coin_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x030056C0, 0x030079E0, [
		[0, -12, 1, ultra.c.d_Vtx, False],
		d_texture_n("ia16", 32, 32, 4),
		[0, 1, 1, ultra.c.d_Gfx, 0x030079E0],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x030056C0, 0x030079E0],
	[ultra.c.f_data, "E0.Global.Shp", 0x1600013C, 0x16000388, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000388],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

pipe_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "pipe", [
		("side", (0.25, 0xFF, 0xFF, 0xFF), ("side.rgba16.png", 32, 64)),
		("top", (0.25, 0xFF, 0xFF, 0xFF), ("top.rgba16.png", 32, 32)),
		("bottom", (0.25, 0x00, 0x00, 0x00)),
	]],
	[UNSM.c.f_obj, "pipe"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x030079E8, 0x03007A00, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "side", [
		(True, "side"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03007E40, 0x03009028, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "side"],
		[0, 1, 1, UNSM.c.d_gfx, 0x03008FF8, "side", 0],
		[0, -2, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "end", [
		(True, "top"),
		(True, "bottom"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03009168, 0x03009CD8, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "top"],
		[0, 1, 1, UNSM.c.d_gfx, 0x03009AC8, "end", 0, 1],
		[0, 1, 1, UNSM.c.d_map, "map"],
	]],
	[UNSM.c.f_gltf_write],
	[UNSM.c.f_obj_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x030079E8, 0x03009CD8],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000388, 0x160003A8, [
		[0, 1, 1, UNSM.c.d_shplang, 0x160003A8],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

door_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "door", [
		("a_face", (0.25, 0xFF, 0xFF, 0xFF), ("a_face.rgba16.png", 32, 64)),
		("a_side", (0.25, 0xFF, 0xFF, 0xFF), ("a_side.rgba16.png", 32, 64)),
		("knob", (0.25, 0xFF, 0xFF, 0x00)),
		("b_face", (0.25, 0xFF, 0xFF, 0xFF), ("b_face.rgba16.png", 32, 64)),
		("b_side", (0.25, 0xFF, 0xFF, 0xFF), ("b_side.rgba16.png", 32, 32)),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03009CE0, 0x03013910, [
		[0, -2, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "a_face"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "a_side"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "b_face"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "b_side"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "d_face"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "d_side"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "e_face"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "e_side"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "f_face"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "f_side"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "star"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "star1"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "star3"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 32, "keyhole"],
	]],
	[UNSM.c.f_gltf_mesh, "ah", [
		(True, "a_side"),
		(True, "a_face"),
	]],
	[UNSM.c.f_gltf_mesh, "ahf", [
		(True, "knob"),
	]],
	[UNSM.c.f_gltf_mesh, "ahb", [
		(True, "knob"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03013C10, 0x03013F20, [
		[0, 1, 1, UNSM.c.d_gfx, 0x03013F20,
			"ah", 0, 1,
			"ahf", 0,
			"ahb", 0,
		],
	]],
	[UNSM.c.f_gltf_mesh, "al", [
		(True, "a_face"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03013FA0, 0x03014558, [
		[0, -8, 1, ultra.c.d_Vtx, True],
		[0, 1, 1, UNSM.c.d_gfx, 0x030140B0, "al", 0],
		[0, 1, 1, ultra.c.d_Gfx, 0x03014140],
		[0, -8, 1, ultra.c.d_Vtx, True],
		[0, 1, 1, ultra.c.d_Gfx, 0x03014370],
		[0, -16, 1, ultra.c.d_Vtx, True],
		[0, 1, 1, ultra.c.d_Gfx, 0x03014558],
	]],
	[UNSM.c.f_gltf_mesh, "h", [
		(True, "b_side"),
		(True, "b_face"),
		(True, "knob"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03014888, 0x03014DF0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x03014DF0, "h", 2, 0, 1],
	]],
	[UNSM.c.f_gltf_mesh, "l", [
		(True, "b_face"),
		(True, "knob"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03014EF0, 0x030156D8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x030151C8, "l", 0, 1],
		[0, 1, 1, UNSM.c.d_anime, 0x03015208],
		[0, 1, 1, UNSM.c.d_anime, 0x03015440],
		[0, 1, 1, UNSM.c.d_anime, 0x03015458],
		[0, 1, 1, UNSM.c.d_anime, 0x03015690],
		[0, 1, 1, UNSM.c.d_anime, 0x030156A8],
		[0, -6, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x03009CE0, 0x030156D8],
	[ultra.c.f_data, "E0.Global.Shp", 0x160003A8, 0x16000A84, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000A84],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

doorkey_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "doorkey", [
		("key", (0.25, 0xFF, 0xB2, 0x00)),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x030156E0, 0x030156F8, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "key", [
		(True, "key"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x030161F8, 0x030172D8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x03016530, "key", 0],
		[0, 1, 1, UNSM.c.d_anime, 0x03016BE8],
		[0, 1, 1, UNSM.c.d_anime, 0x030172B8],
		[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x030156E0, 0x030172D8],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000A84, 0x16000B10, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000B10],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

flame_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x030172E0, 0x0301B5C0, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		d_texture_n("ia16", 32, 32, 8),
		[0, 1, 1, ultra.c.d_Gfx, 0x0301B5C0],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x030172E0, 0x0301B5C0],
	[ultra.c.f_extern, "E0.Global.Shp", 0x16000B2C, 0x16000B8C],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000B10, 0x16000BEC, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000BEC],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

fish_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "fish", [
		("fish", (0.25, 0xFF, 0xFF, 0xFF), ("fish.rgba16.png", 32, 32)),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0301B5C8, 0x0301BDE0, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "fish"],
	]],
	[UNSM.c.f_gltf_mesh, "body", [
		(True, "fish"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0301BEC0, 0x0301C018, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0301C018, "body", 0],
	]],
	[UNSM.c.f_gltf_mesh, "tail", [
		(True, "fish"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0301C0A8, 0x0301C2B8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0301C1B0, "tail", 0],
		[0, 1, 1, UNSM.c.d_anime, 0x0301C298],
		[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x0301B5C8, 0x0301C2B8],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000BEC, 0x16000C8C, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000C8C],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

stone_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0301C2C0, 0x0301CB98, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "stone"],
		[0, 1, 1, ultra.c.d_Gfx, 0x0301CB98],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

leaf_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0301CBA0, 0x0301CE70, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, "leaf"],
		[0, 1, 1, ultra.c.d_Gfx, 0x0301CE70],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x0301CBA0, 0x0301CE70],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000C8C, 0x16000CA4, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000CA4],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

map_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_obj, "door"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0301CE78, 0x0301CECC, [
		[0, 1, 1, UNSM.c.d_map, "door"],
	]],
	[UNSM.c.f_obj_write],
	[UNSM.c.f_obj, "13002018"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0301CECC, 0x0301CEFC, [
		[0, 1, 1, UNSM.c.d_map, "13002018"],
	]],
	[UNSM.c.f_obj_write],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

cap_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "cap", [
		("red", (0.5, 0xFF, 0x00, 0x00)),
		("hair", (0.5, 0x73, 0x06, 0x00)),
		("logo", (0.5, 0xFF, 0xFF, 0xFF), ("logo.rgba16.png", 32, 32)),
		("wing_l", (0.5, 0xFF, 0xFF, 0xFF), ("wing_l.rgba16.png", 32, 64)),
		("wing_r", (0.5, 0xFF, 0xFF, 0xFF), ("wing_r.rgba16.png", 32, 64)),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0301CF08, 0x03022750, [
		[0, -3, 1, UNSM.c.d_light, 0.5],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 64, 32, "metal"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "logo"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "wing_l"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "wing_r"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "metal_wing_l"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "metal_wing_r"],
	]],
	[UNSM.c.f_gltf_mesh, "cap", [
		(True, "logo"),
		(True, "red"),
		(True, "hair"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03022B30, 0x03022D38, [
		[0, 1, 1, UNSM.c.d_gfx, 0x03022D38, "cap", 0, 1, 2],
	]],
	[UNSM.c.f_gltf_mesh, "wing", [
		(True, "wing_l"),
		(True, "wing_r"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03022E78, 0x030233D0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x030233D0, "wing", 0, 1],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x0301CF08, 0x030233D0],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000CA4, 0x16000E14, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000E14],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

meter_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x030233D8, 0x030295D8, [
		[0, 1, 1, ultra.c.d_s64],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "0_l"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "0_r"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "8"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "7"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "6"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "5"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "4"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "3"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "2"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "1"],
		[0, -8, 1, ultra.c.d_addr, 0],
		[0, -8, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, ultra.c.d_Gfx, 0x03029530],
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, ultra.c.d_Gfx, 0x030295D8],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

number_shape = [
	[main.f_str, "#ifdef SCRIPT\n\n"],
	[ultra.c.f_extern, "E0.Gfx", 0x02011ED8, 0x020120B8],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000E14, 0x16000E84, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000E84],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

_1up_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x030295E8, 0x0302A6D0, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "1up"],
		[0, 1, 1, ultra.c.d_Gfx, 0x0302A6D0],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x030295E8, 0x0302A6D0],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000E84, 0x16000EA0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000EA0],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

powerstar_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "powerstar", [
		("star", (0.25, 0xFF, 0xFF, 0xFF)),
		("eye", (0.25, 0xFF, 0xFF, 0xFF), ("eye.rgba16.png", 32, 32)),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302A6D8, 0x0302B6F0, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "star"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "eye"],
	]],
	[UNSM.c.f_gltf_mesh, "star", [
		(True, "star"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302B7B0, 0x0302B920, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0302B908, "star", 0],
		[0, -1, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "eyes", [
		(True, "eye"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302B9C0, 0x0302BA88, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0302BA88, "eyes", 0],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x0302A6D8, 0x0302BA88],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000EA0, 0x16000ED4, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000ED4],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

sand_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302BA90, 0x0302BD60, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, "sand"],
		[0, 1, 1, ultra.c.d_Gfx, 0x0302BD60],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

shard_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302BD68, 0x0302C480, [
		[0, -4, 1, UNSM.c.d_light, 0.25],
		[0, -3, 1, ultra.c.d_Vtx, True],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, "cork"],
		[0, 1, 1, ultra.c.d_Gfx, 0x0302C098],
		[0, -3, 1, ultra.c.d_Vtx, True],
		[0, -3, 1, ultra.c.d_Vtx, False],
		[0, -10, 1, ultra.c.d_Vtx, True],
		[0, -10, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, ultra.c.d_Gfx, 0x0302C480],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x0302BD68, 0x0302C480],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000ED4, 0x16000F6C, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000F6C],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

shadestar_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "shadestar", [
		("star", (0.1, 0x1E, 0x32, 0xE6)),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302C488, 0x0302C4A0, [
		[0, -1, 1, UNSM.c.d_light, 0.1],
	]],
	[UNSM.c.f_gltf_mesh, "star", [
		(True, "star"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302C560, 0x0302C658, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0302C658, "star", 0],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x0302C488, 0x0302C658],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000F6C, 0x16000F98, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000F98],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

snow_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302C660, 0x0302C938, [
		[0, -4, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 16, 16, "snow"],
		[0, 1, 1, ultra.c.d_Gfx, 0x0302C938],
	]],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x0302C660, 0x0302C938],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000F98, 0x16000FB4, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000FB4],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

signpost_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "signpost", [
		("wood", (0.5, 0xFF, 0xFF, 0xFF), ("wood.rgba16.png", 32, 32)),
		("face", (0.5, 0xFF, 0xFF, 0xFF), ("face.rgba16.png", 32, 32)),
	]],
	[UNSM.c.f_obj, "signpost"],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302C940, 0x0302C958, [
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "post", [
		(True, "wood"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302C9C8, 0x0302DAC0, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "wood"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "face"],
		[0, 1, 1, UNSM.c.d_gfx, 0x0302DAA8, "post", 0],
		[0, -1, 1, UNSM.c.d_light, 0.5],
	]],
	[UNSM.c.f_gltf_mesh, "sign", [
		(True, "wood"),
		(True, "face"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302DC40, 0x0302DE04, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0302DD80, "sign", 0, 1],
		[0, 1, 1, UNSM.c.d_map, "map"],
	]],
	[UNSM.c.f_gltf_write],
	[UNSM.c.f_obj_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x0302C940, 0x0302DE08],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000FB4, 0x16000FE8, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16000FE8],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

tree_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "tree", [
		("a_l", None, ("a_l.rgba16.png", 32, 64)),
		("a_r", None, ("a_r.rgba16.png", 32, 64)),
		("b", (0.25, 0xFF, 0xFF, 0xFF), ("b.rgba16.png", 32, 64)),
		("c", (0.25, 0xFF, 0xFF, 0xFF), ("c.rgba16.png", 32, 64)),
		("e", (0.25, 0xFF, 0xFF, 0xFF), ("e.rgba16.png", 32, 64)),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302DE10, 0x0302FE28, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "a_l"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "a_r"],
	]],
	[UNSM.c.f_gltf_mesh, "a", [
		(False, "a_l"),
		(False, "a_r"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x0302FE88, 0x03030F60, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0302FF60, "a", 0, 1],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "b"],
	]],
	[UNSM.c.f_gltf_mesh, "b", [
		(True, "b"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03030FA0, 0x03032048, [
		[0, 1, 1, UNSM.c.d_gfx, 0x03031048, "b", 0],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "c"],
	]],
	[UNSM.c.f_gltf_mesh, "c", [
		(True, "c"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03032088, 0x03032130, [
		[0, 1, 1, UNSM.c.d_gfx, 0x03032130, "c", 0],
	]],
	[UNSM.c.f_gltf_mesh, "d", [
		(True, "b"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03032170, 0x03033218, [
		[0, 1, 1, UNSM.c.d_gfx, 0x03032218, "d", 0],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 64, "e"],
	]],
	[UNSM.c.f_gltf_mesh, "e", [
		(True, "e"),
	]],
	[ultra.c.f_data, "E0.Global.Gfx", 0x03033258, 0x03033300, [
		[0, 1, 1, UNSM.c.d_gfx, 0x03033300, "e", 0],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.Global.Gfx", 0x0302DE10, 0x03033300],
	[ultra.c.f_data, "E0.Global.Shp", 0x16000FE8, 0x16001060, [
		[0, 1, 1, UNSM.c.d_shplang, 0x16001060],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

seq_global = [
	[main.s_file, "shape/global/puff/shape.c", puff_shape],
	[main.s_file, "shape/global/explosion/shape.c", explosion_shape],
	[main.s_file, "shape/global/butterfly/shape.c", butterfly_shape],
	[main.s_file, "shape/global/coin/shape.c", coin_shape],
	[main.s_file, "shape/global/pipe/shape.c", pipe_shape],
	[main.s_file, "shape/global/door/shape.c", door_shape],
	[main.s_file, "shape/global/doorkey/shape.c", doorkey_shape],
	[main.s_file, "shape/global/flame/shape.c", flame_shape],
	[main.s_file, "shape/global/fish/shape.c", fish_shape],
	[main.s_file, "shape/global/stone/shape.c", stone_shape],
	[main.s_file, "shape/global/leaf/shape.c", leaf_shape],
	[main.s_file, "shape/global/map/shape.c", map_shape],
	[main.s_file, "shape/global/cap/shape.c", cap_shape],
	[main.s_file, "shape/global/meter/shape.c", meter_shape],
	[main.s_file, "shape/global/number/shape.c", number_shape],
	[main.s_file, "shape/global/1up/shape.c", _1up_shape],
	[main.s_file, "shape/global/powerstar/shape.c", powerstar_shape],
	[main.s_file, "shape/global/sand/shape.c", sand_shape],
	[main.s_file, "shape/global/shard/shape.c", shard_shape],
	[main.s_file, "shape/global/shadestar/shape.c", shadestar_shape],
	[main.s_file, "shape/global/snow/shape.c", snow_shape],
	[main.s_file, "shape/global/signpost/shape.c", signpost_shape],
	[main.s_file, "shape/global/tree/shape.c", tree_shape],
]
