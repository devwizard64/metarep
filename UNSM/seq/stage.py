import main
import ultra

import UNSM.asm

from . import d_texture_n

################################################################################
# BBH
################################################################################

str_bbh_gfx = """
.globl water_0400; water_0400 = 0x07026E24
.globl water_0401; water_0401 = 0x07026E34
"""

bbh_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_bbh_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.BBH", 0x0E000000, 0x0E0005A8],
]

bbh_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.BBH", 0x0E0005B0, 0x0E001090, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E001090],
	]],
]

seq_bbh = [
	[main.s_bin, "stage/bbh/gfx.bin", "E0.BBH.Gfx", 0x07000000, 0x07026E44],
	[main.s_file, "stage/bbh/seq.sx", bbh_seq],
	[main.s_file, "stage/bbh/shp.c", bbh_shp],
]

################################################################################
# CCM
################################################################################

str_ccm_gfx = """
.globl water_0501; water_0501 = 0x07016708
"""

ccm_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_ccm_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.CCM", 0x0E000000, 0x0E0003DC],
]

ccm_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.CCM", 0x0E0003E0, 0x0E0006B0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E0006B0],
	]],
]

seq_ccm = [
	[main.s_bin, "stage/ccm/gfx.bin", "E0.CCM.Gfx", 0x07000000, 0x070237A6],
	[main.s_file, "stage/ccm/seq.sx", ccm_seq],
	[main.s_file, "stage/ccm/shp.c", ccm_shp],
]

################################################################################
# Inside
################################################################################

str_inside_gfx = """
.globl map_inside_0700FD30; map_inside_0700FD30 = 0x0700FD30
.globl map_inside_070186B4; map_inside_070186B4 = 0x070186B4
.globl wave_inside_07023620; wave_inside_07023620 = 0x07023620
.globl wave_inside_07023698; wave_inside_07023698 = 0x07023698
.globl wave_inside_07023710; wave_inside_07023710 = 0x07023710
.globl wave_inside_07023788; wave_inside_07023788 = 0x07023788
.globl wave_inside_07023800; wave_inside_07023800 = 0x07023800
.globl wave_inside_07023878; wave_inside_07023878 = 0x07023878
.globl wave_inside_070238F0; wave_inside_070238F0 = 0x070238F0
.globl wave_inside_07023968; wave_inside_07023968 = 0x07023968
.globl wave_inside_070239E0; wave_inside_070239E0 = 0x070239E0
.globl wave_inside_07023A58; wave_inside_07023A58 = 0x07023A58
.globl wave_inside_07023AD0; wave_inside_07023AD0 = 0x07023AD0
.globl wave_inside_07023B48; wave_inside_07023B48 = 0x07023B48
.globl wave_inside_07023BC0; wave_inside_07023BC0 = 0x07023BC0
.globl wave_inside_07023C38; wave_inside_07023C38 = 0x07023C38
.globl gfx_inside_0702A880; gfx_inside_0702A880 = 0x0702A880
.globl water_0600; water_0600 = 0x070790F0
.globl water_0612; water_0612 = 0x07079100

.globl map_0700FAEC; map_0700FAEC = 0x0700FAEC
.globl map_07026B1C; map_07026B1C = 0x07026B1C
.globl map_0701D18C; map_0701D18C = 0x0701D18C
.globl map_07015288; map_07015288 = 0x07015288

.globl map_07018528; map_07018528 = 0x07018528

.globl _0605784C; _0605784C = 0x0605784C

.globl map_07004B94; map_07004B94 = 0x07004B94
.globl map_07004C18; map_07004C18 = 0x07004C18
.globl map_07004C9C; map_07004C9C = 0x07004C9C
.globl map_07004D20; map_07004D20 = 0x07004D20
.globl map_07004DA4; map_07004DA4 = 0x07004DA4
.globl map_07004E28; map_07004E28 = 0x07004E28
.globl map_07004EAC; map_07004EAC = 0x07004EAC
.globl map_07004F30; map_07004F30 = 0x07004F30
.globl map_07004FB4; map_07004FB4 = 0x07004FB4
.globl map_07005038; map_07005038 = 0x07005038

.globl map_0707768C; map_0707768C = 0x0707768C
.globl map_070775B4; map_070775B4 = 0x070775B4

.globl map_0702B65C; map_0702B65C = 0x0702B65C
"""

str_inside_shp = """
extern void *CtrlInsideMirror(int code, SHAPE *shape, void *data);
extern void *Ctrl_objshape_802D2360(int code, SHAPE *shape, void *data);
"""

inside_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_inside_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.Inside", 0x0E000000, 0x0E000EFC],
]

inside_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, str_inside_shp],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.Inside", 0x0E000F00, 0x0E001CF0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E001CF0],
	]],
]

seq_inside = [
	[main.s_bin, "stage/inside/gfx.bin", "E0.Inside.Gfx", 0x07000000, 0x07079118],
	[main.s_file, "stage/inside/seq.sx", inside_seq],
	[main.s_file, "stage/inside/shp.c", inside_shp],
]

################################################################################
# HMC
################################################################################

str_hmc_gfx = """
.globl wave_hmc_0702551C; wave_hmc_0702551C = 0x0702551C
.globl water_0701; water_0701 = 0x0702B900
.globl water_0702; water_0702 = 0x0702B950
"""

hmc_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_hmc_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.HMC", 0x0E000000, 0x0E000530],
]

hmc_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.HMC", 0x0E000530, 0x0E000CB0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000CB0],
	]],
]

seq_hmc = [
	[main.s_bin, "stage/hmc/gfx.bin", "E0.HMC.Gfx", 0x07000000, 0x0702B968],
	[main.s_file, "stage/hmc/seq.sx", hmc_seq],
	[main.s_file, "stage/hmc/shp.c", hmc_shp],
]

################################################################################
# SSL
################################################################################

str_ssl_gfx = """
.globl txt_ssl_07001000; txt_ssl_07001000 = 0x07001000
.globl txt_ssl_07004018; txt_ssl_07004018 = 0x07004018
.globl gfx_ssl_07004818; gfx_ssl_07004818 = 0x07004818
.globl gfx_ssl_07004860; gfx_ssl_07004860 = 0x07004860
.globl gfx_ssl_07004880; gfx_ssl_07004880 = 0x07004880
.globl gfx_ssl_070048F8; gfx_ssl_070048F8 = 0x070048F8
.globl fluid_0801S; fluid_0801S = 0x07004930
.globl fluid_0802S; fluid_0802S = 0x070049B4
.globl gfx_ssl_07004A38; gfx_ssl_07004A38 = 0x07004A38
.globl water_0801; water_0801 = 0x07012778
.globl water_0851; water_0851 = 0x070127C8
.globl gfx_ssl_070127E0; gfx_ssl_070127E0 = 0x070127E0
.globl gfx_ssl_070127E8; gfx_ssl_070127E8 = 0x070127E8
.globl fluid_0801L; fluid_0801L = 0x070127F0
.globl gfx_ssl_070128B8; gfx_ssl_070128B8 = 0x070128B8
.globl fluid_0802L; fluid_0802L = 0x07012900
.globl gfx_ssl_07012A08; gfx_ssl_07012A08 = 0x07012A08
.globl fluid_0803L; fluid_0803L = 0x07012A50
.globl gfx_ssl_07012B48; gfx_ssl_07012B48 = 0x07012B48
.globl gfx_ssl_070285F0; gfx_ssl_070285F0 = 0x070285F0
.globl gfx_ssl_07028660; gfx_ssl_07028660 = 0x07028660
.globl gfx_ssl_070286A0; gfx_ssl_070286A0 = 0x070286A0
.globl gfx_ssl_07028718; gfx_ssl_07028718 = 0x07028718
.globl fluid_0801; fluid_0801 = 0x07028760
.globl gfx_ssl_070287B8; gfx_ssl_070287B8 = 0x070287B8
.globl fluid_0802; fluid_0802 = 0x070287F0
.globl fluid_0803; fluid_0803 = 0x07028844
.globl gfx_ssl_07028888; gfx_ssl_07028888 = 0x07028888
"""

ssl_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_ssl_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.SSL", 0x0E000000, 0x0E0005B4],
]

ssl_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.SSL", 0x0E0005C0, 0x0E00091C, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E00091C],
	]],
]

seq_ssl = [
	[main.s_bin, "stage/ssl/gfx.bin", "E0.SSL.Gfx", 0x07000000, 0x070288B0],
	[main.s_file, "stage/ssl/seq.sx", ssl_seq],
	[main.s_file, "stage/ssl/shp.c", ssl_shp],
]

################################################################################
# BoB
################################################################################

battlefield_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "battlefield", [
		("c3", (0.4, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c3.rgba16.png", 32, 32)),
		("c4", (0.4, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c4.rgba16.png", 32, 32)),
		("c6", (0.4, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c6.rgba16.png", 32, 32)),
		("c7", (0.4, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c7.rgba16.png", 32, 32)),
		("c9", (0.4, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c9.rgba16.png", 32, 32)),
		("c10", (0.4, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c10.rgba16.png", 32, 32)),
		("c11", (0.4, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c11.rgba16.png", 32, 32)),
		("c12", (0.4, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c12.rgba16.png", 32, 64)),
		("c16", None, ("../../../data/texture/c16.rgba16.png", 32, 32)),
		("c17", (0.4, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c17.rgba16.png", 32, 32)),
		("c17_shade", (0.4, 0x64, 0x64, 0x64), ("../../../data/texture/c17.rgba16.png", 32, 32)),
		("c17_cave", (0.2, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c17.rgba16.png", 32, 32)),
		("c18", (0.4, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c18.rgba16.png", 32, 32)),
		("c19", (0.4, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c19.rgba16.png", 32, 32)),
		("c21", None, ("../../../data/texture/c21_j22_k22.ia16.png", 32, 32)),
		("0", None, ("../0.rgba16.png", 32, 32)),
		("1", (0.4, 0xFF, 0xFF, 0xFF), ("../1.rgba16.png", 32, 32)),
		("2", (0.4, 0xFF, 0xFF, 0xFF), ("../2.rgba16.png", 32, 32)),
		("3", (0.4, 0xFF, 0xFF, 0xFF), ("../3.rgba16.png", 32, 32)),
		("4", (0.4, 0xFF, 0xFF, 0xFF), ("../4.rgba16.png", 32, 32)),
	]],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x07002800, 0x07002818, [
		[0, -1, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "smooth", [
		(True, "c11"),
		(True, "c18"),
		(True, "c12"),
	]],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x07003CA8, 0x07004490, [
		[0, 1, 1, UNSM.c.d_gfx, 0x07004478, "smooth", 0, 1, 2],
		[0, -1, 1, UNSM.c.d_light, 0.4],
	]],
	[UNSM.c.f_gltf_mesh, "flat", [
		(True, "c7"),
		(True, "c4"),
		(True, "c3"),
		(True, "c10"),
		(True, "c9"),
		(True, "c6"),
		(True, "2"),
		(True, "3"),
		(True, "1"),
		(True, "c12"),
	]],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x07008AF0, 0x07009E98, [
		[0, 1, 1, UNSM.c.d_gfx, 0x07009E98, "flat", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
	]],
	[UNSM.c.f_gltf_mesh, "xlu_decal", [
		(False, "c21"),
	]],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x0700A318, 0x0700A4E0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700A4E0, "xlu_decal", 0],
	]],
	[UNSM.c.f_gltf_mesh, "tex_edge", [
		(False, "c16"),
		(False, "0"),
	]],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x0700A800, 0x0700AA10, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700A9E0, "tex_edge", 0, 1],
		[0, -2, 1, UNSM.c.d_light, 0.2],
	]],
	[UNSM.c.f_gltf_mesh, "shade", [
		(True, "c17"),
		(True, "c17_shade"),
		(True, "c11"),
		(True, "c18"),
		(True, "4"),
		(True, "c19"),
		(True, "c12"),
	]],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x0700CFC0, 0x0700DE48, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700DE30, "shade", 0, 1, 2, 3, 4, 5, 6],
		[0, -1, 1, UNSM.c.d_light, 0.2],
	]],
	[UNSM.c.f_gltf_mesh, "cave", [
		(True, "c17_cave"),
	]],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x0700E1E8, 0x0700E3E0, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700E3E0, "cave", 0],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.BoB.Gfx", 0x07002800, 0x0700E3E0],
	[ultra.c.f_data, "E0.BoB", 0x0E000488, 0x0E00054C, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E00054C],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

# chain chomp gate
bob54_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "54", [
		("c16", None, ("../../../data/texture/c16.rgba16.png", 32, 32)),
	]],
	[UNSM.c.f_gltf_mesh, "54", [
		(False, "c16"),
	]],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x0700E420, 0x0700E510, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700E510, "54", 0],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.BoB.Gfx", 0x0700E3E0, 0x0700E510],
	[ultra.c.f_data, "E0.BoB", 0x0E000440, 0x0E000458, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000458],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

# seesaw bridge
bob55_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "55", [
		("c12", (0.25, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c12.rgba16.png", 32, 64)),
	]],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x0700E510, 0x0700E528, [
		[0, -1, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "55", [
		(True, "c12"),
	]],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x0700E6C8, 0x0700E810, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700E810, "55", 0],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.BoB.Gfx", 0x0700E510, 0x0700E810],
	[ultra.c.f_data, "E0.BoB", 0x0E000458, 0x0E000470, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000470],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

# barred gate
bob56_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "56", [
		("c16", None, ("../../../data/texture/c16.rgba16.png", 32, 32)),
	]],
	[UNSM.c.f_gltf_mesh, "56", [
		(False, "c16"),
	]],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x0700E860, 0x0700E958, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700E958, "56", 0],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.BoB.Gfx", 0x0700E810, 0x0700E958],
	[ultra.c.f_data, "E0.BoB", 0x0E000470, 0x0E000488, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000488],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

bob_gfx = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[main.f_str, "#include \"data/texture/c.szp.h\"\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x07000000, 0x07002800, [
		d_texture_n("rgba16", 32, 32, 5),
	]],
	[main.f_str, "#include \"battlefield/shape.c\"\n"],
	[main.f_str, "#include \"54/shape.c\"\n"],
	[main.f_str, "#include \"55/shape.c\"\n"],
	[main.f_str, "#include \"56/shape.c\"\n"],
	[UNSM.c.f_obj, "battlefield/battlefield"],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x0700E958, 0x070113C0, [
		[0, 1, 1, UNSM.c.d_map, "battlefield/map"],
		[0, 1, 1, UNSM.c.d_tag],
	]],
	[UNSM.c.f_obj_write],
	[UNSM.c.f_obj, "54/54"],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x070113C0, 0x070113F0, [
		[0, 1, 1, UNSM.c.d_map, "54/map"],
	]],
	[UNSM.c.f_obj_write],
	[UNSM.c.f_obj, "55/55"],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x070113F0, 0x07011474, [
		[0, 1, 1, UNSM.c.d_map, "55/map"],
	]],
	[UNSM.c.f_obj_write],
	[UNSM.c.f_obj, "56/56"],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x07011474, 0x07011530, [
		[0, 1, 1, UNSM.c.d_map, "56/map"],
	]],
	[UNSM.c.f_obj_write],
	[ultra.c.f_data, "E0.BoB.Gfx", 0x07011530, 0x070117C4, [
		[0, 3, 1, UNSM.c.d_path_data],
	]],
]

bob_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.BoB", 0x0E000000, 0x0E00043C],
]

seq_bob = [
	[main.s_file, "stage/bob/battlefield/shape.c", battlefield_shape],
	[main.s_file, "stage/bob/54/shape.c", bob54_shape],
	[main.s_file, "stage/bob/55/shape.c", bob55_shape],
	[main.s_file, "stage/bob/56/shape.c", bob56_shape],
	[main.s_file, "stage/bob/gfx.c", bob_gfx],
	[main.s_file, "stage/bob/seq.sx", bob_seq],
]

################################################################################
# SL
################################################################################

str_sl_gfx = """
.globl water_1001; water_1001 = 0x0700FA70
"""

sl_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_sl_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.SL", 0x0E000000, 0x0E000360],
]

sl_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.SL", 0x0E000360, 0x0E000524, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000524],
	]],
]

seq_sl = [
	[main.s_bin, "stage/sl/gfx.bin", "E0.SL.Gfx", 0x07000000, 0x0700FA88],
	[main.s_file, "stage/sl/seq.sx", sl_seq],
	[main.s_file, "stage/sl/shp.c", sl_shp],
]

################################################################################
# WDW
################################################################################

str_wdw_gfx = """
.globl water_1101; water_1101 = 0x07018748
.globl water_1102; water_1102 = 0x07018778
"""

wdw_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_wdw_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.WDW", 0x0E000000, 0x0E00057C],
]

wdw_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.WDW", 0x0E000580, 0x0E0007CC, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E0007CC],
	]],
]

seq_wdw = [
	[main.s_bin, "stage/wdw/gfx.bin", "E0.WDW.Gfx", 0x07000000, 0x07018788],
	[main.s_file, "stage/wdw/seq.sx", wdw_seq],
	[main.s_file, "stage/wdw/shp.c", wdw_shp],
]

################################################################################
# JRB
################################################################################

str_jrb_gfx = """
.globl water_1201; water_1201 = 0x0700D2CC
.globl water_1205; water_1205 = 0x0700D304
.globl water_1202; water_1202 = 0x0701139C
"""

jrb_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_jrb_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.JRB", 0x0E000000, 0x0E000900],
]

jrb_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.JRB", 0x0E000900, 0x0E000BA4, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000BA4],
	]],
]

seq_jrb = [
	[main.s_bin, "stage/jrb/gfx.bin", "E0.JRB.Gfx", 0x07000000, 0x070113AC],
	[main.s_file, "stage/jrb/seq.sx", jrb_seq],
	[main.s_file, "stage/jrb/shp.c", jrb_shp],
]

################################################################################
# THI
################################################################################

str_thi_gfx = """
.globl water_1301; water_1301 = 0x0700E31C
.globl water_1302; water_1302 = 0x0700E39C
"""

thi_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_thi_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.THI", 0x0E000000, 0x0E0005A4],
]

thi_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.THI", 0x0E0005B0, 0x0E00083C, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E00083C],
	]],
]

seq_thi = [
	[main.s_bin, "stage/thi/gfx.bin", "E0.THI.Gfx", 0x07000000, 0x0700E3BC],
	[main.s_file, "stage/thi/seq.sx", thi_seq],
	[main.s_file, "stage/thi/shp.c", thi_shp],
]

################################################################################
# TTC
################################################################################

str_ttc_gfx = """
.globl txt_ttc_07015F90; txt_ttc_07015F90 = 0x07015F90
.globl gfx_ttc_07016790; gfx_ttc_07016790 = 0x07016790
.globl gfx_ttc_07016808; gfx_ttc_07016808 = 0x07016808
.globl fluid_1400L; fluid_1400L = 0x07016840
.globl fluid_1401L; fluid_1401L = 0x07016904
.globl gfx_ttc_070169C8; gfx_ttc_070169C8 = 0x070169C8
"""

ttc_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_ttc_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.TTC", 0x0E000000, 0x0E000240],
]

ttc_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.TTC", 0x0E000240, 0x0E000468, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000468],
	]],
]

seq_ttc = [
	[main.s_bin, "stage/ttc/gfx.bin", "E0.TTC.Gfx", 0x07000000, 0x07016A20],
	[main.s_file, "stage/ttc/seq.sx", ttc_seq],
	[main.s_file, "stage/ttc/shp.c", ttc_shp],
]

################################################################################
# RR
################################################################################

str_rr_gfx = """
.globl rr_07019080; rr_07019080 = 0x07019080
.globl gfx_rr_07019128; gfx_rr_07019128 = 0x07019128
.globl gfx_rr_07019198; gfx_rr_07019198 = 0x07019198
.globl gfx_rr_07019200; gfx_rr_07019200 = 0x07019200
"""

str_rr_shp = """
extern void *Ctrl_objshape_802D2470(int code, SHAPE *shape, void *data);
extern void *Ctrl_objshape_802D2520(int code, SHAPE *shape, void *data);
"""

rr_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_rr_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.RR", 0x0E000000, 0x0E000658],
]

rr_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, str_rr_shp],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.RR", 0x0E000660, 0x0E000A74, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000A74],
	]],
]

seq_rr = [
	[main.s_bin, "stage/rr/gfx.bin", "E0.RR.Gfx", 0x07000000, 0x0702EE76],
	[main.s_file, "stage/rr/seq.sx", rr_seq],
	[main.s_file, "stage/rr/shp.c", rr_shp],
]

################################################################################
# Grounds
################################################################################

str_grounds_gfx = """
.globl gfx_grounds_0700EA58; gfx_grounds_0700EA58 = 0x0700EA58
.globl gfx_grounds_0700F2E8; gfx_grounds_0700F2E8 = 0x0700F2E8
.globl water_1601; water_1601 = 0x07011738
.globl fluid_1601; fluid_1601 = 0x07011750
.globl gfx_grounds_070117E8; gfx_grounds_070117E8 = 0x070117E8
"""

grounds_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_grounds_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.Grounds", 0x0E000000, 0x0E00065C],
]

grounds_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.Grounds", 0x0E000660, 0x0E000820, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000820],
	]],
]

seq_grounds = [
	[main.s_bin, "stage/grounds/gfx.bin", "E0.Grounds.Gfx", 0x07000000, 0x07011878],
	[main.s_file, "stage/grounds/seq.sx", grounds_seq],
	[main.s_file, "stage/grounds/shp.c", grounds_shp],
]

################################################################################
# BitDW
################################################################################

bitdw_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.BitDW", 0x0E000000, 0x0E0003B4],
]

bitdw_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.BitDW", 0x0E0003C0, 0x0E0006A0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E0006A0],
	]],
]

seq_bitdw = [
	[main.s_bin, "stage/bitdw/gfx.bin", "E0.BitDW.Gfx", 0x07000000, 0x0700FE30],
	[main.s_file, "stage/bitdw/seq.sx", bitdw_seq],
	[main.s_file, "stage/bitdw/shp.c", bitdw_shp],
]

################################################################################
# VCutM
################################################################################

vcutm_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.VCutM", 0x0E000000, 0x0E0001F0],
]

vcutm_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.VCutM", 0x0E0001F0, 0x0E0002A8, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E0002A8],
	]],
]

seq_vcutm = [
	[main.s_bin, "stage/vcutm/gfx.bin", "E0.VCutM.Gfx", 0x07000000, 0x0700ACC8],
	[main.s_file, "stage/vcutm/seq.sx", vcutm_seq],
	[main.s_file, "stage/vcutm/shp.c", vcutm_shp],
]

################################################################################
# BitFS
################################################################################

str_bitfs_gfx = """
.globl fluid_1901; fluid_1901 = 0x07015AF0
.globl fluid_1902; fluid_1902 = 0x07015B1C
.globl fluid_1903; fluid_1903 = 0x07015B48
.globl gfx_bitfs_07015BA8; gfx_bitfs_07015BA8 = 0x07015BA8
.globl gfx_bitfs_07015BC0; gfx_bitfs_07015BC0 = 0x07015BC0
"""

bitfs_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_bitfs_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.BitFS", 0x0E000000, 0x0E0004A4],
]

bitfs_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.BitFS", 0x0E0004B0, 0x0E000848, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000848],
	]],
]

seq_bitfs = [
	[main.s_bin, "stage/bitfs/gfx.bin", "E0.BitFS.Gfx", 0x07000000, 0x07015C08],
	[main.s_file, "stage/bitfs/seq.sx", bitfs_seq],
	[main.s_file, "stage/bitfs/shp.c", bitfs_shp],
]

################################################################################
# SA
################################################################################

sa_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.SA", 0x0E000000, 0x0E000168],
]

sa_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.SA", 0x0E000170, 0x0E000200, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000200],
	]],
]

seq_sa = [
	[main.s_bin, "stage/sa/gfx.bin", "E0.SA.Gfx", 0x07000000, 0x07003330],
	[main.s_file, "stage/sa/seq.sx", sa_seq],
	[main.s_file, "stage/sa/shp.c", sa_shp],
]

################################################################################
# BitS
################################################################################

bits_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.BitS", 0x0E000000, 0x0E00042C],
]

bits_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.BitS", 0x0E000430, 0x0E0007A0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E0007A0],
	]],
]

seq_bits = [
	[main.s_bin, "stage/bits/gfx.bin", "E0.BitS.Gfx", 0x07000000, 0x0701B7F4],
	[main.s_file, "stage/bits/seq.sx", bits_seq],
	[main.s_file, "stage/bits/shp.c", bits_shp],
]

################################################################################
# LLL
################################################################################

str_lll_gfx = """
.globl fluid_2201; fluid_2201 = 0x070286BC
.globl gfx_lll_07028718; gfx_lll_07028718 = 0x07028718
.globl water_2202; water_2202 = 0x07028780
.globl fluid_2202; fluid_2202 = 0x07028790
.globl gfx_lll_07028838; gfx_lll_07028838 = 0x07028838
"""

lll_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_lll_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.LLL", 0x0E000000, 0x0E0009D8],
]

lll_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.LLL", 0x0E0009E0, 0x0E000F80, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000F80],
	]],
]

seq_lll = [
	[main.s_bin, "stage/lll/gfx.bin", "E0.LLL.Gfx", 0x07000000, 0x070288D0],
	[main.s_file, "stage/lll/seq.sx", lll_seq],
	[main.s_file, "stage/lll/shp.c", lll_shp],
]

################################################################################
# DDD
################################################################################

str_ddd_gfx = """
.globl water_2301; water_2301 = 0x0700FCB4
.globl water_2302; water_2302 = 0x0700FD00
"""

ddd_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_ddd_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.DDD", 0x0E000000, 0x0E000450],
]

ddd_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.DDD", 0x0E000450, 0x0E000630, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000630],
	]],
]

seq_ddd = [
	[main.s_bin, "stage/ddd/gfx.bin", "E0.DDD.Gfx", 0x07000000, 0x0700FD10],
	[main.s_file, "stage/ddd/seq.sx", ddd_seq],
	[main.s_file, "stage/ddd/shp.c", ddd_shp],
]

################################################################################
# WF
################################################################################

str_wf_gfx = """
.globl water_2401; water_2401 = 0x07011E08
"""

wf_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_wf_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.WF", 0x0E000000, 0x0E0007E0],
]

wf_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.WF", 0x0E0007E0, 0x0E000CBC, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000CBC],
	]],
]

seq_wf = [
	[main.s_bin, "stage/wf/gfx.bin", "E0.WF.Gfx", 0x07000000, 0x07011E18],
	[main.s_file, "stage/wf/seq.sx", wf_seq],
	[main.s_file, "stage/wf/shp.c", wf_shp],
]

################################################################################
# Ending
################################################################################

ending_gfx = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[ultra.c.f_data, "E0.Ending.Gfx", 0x07000000, 0x07027350, [
		d_texture_n("rgba16", 80, 20, 48, "%d"),
		[0, -192, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, ultra.c.d_Gfx, 0x07027350],
	]],
]

ending_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.Ending", 0x0E000000, 0x0E000050],
]

ending_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[ultra.c.f_extern, "E0.code.text", 0x802D28CC, 0x802D29BC],
	[ultra.c.f_data, "E0.Ending", 0x0E000050, 0x0E0000BC, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E0000BC],
	]],
]

seq_ending = [
	[main.s_file, "stage/ending/gfx.c", ending_gfx],
	[main.s_file, "stage/ending/seq.sx", ending_seq],
	[main.s_file, "stage/ending/shp.c", ending_shp],
]

################################################################################
# Courtyard
################################################################################

str_courtyard_gfx = """
.globl water_2601; water_2601 = 0x07006E6C
"""

courtyard_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_courtyard_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.Courtyard", 0x0E000000, 0x0E0001FC],
]

courtyard_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.Courtyard", 0x0E000200, 0x0E0002C0, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E0002C0],
	]],
]

seq_courtyard = [
	[main.s_bin, "stage/courtyard/gfx.bin", "E0.Courtyard.Gfx", 0x07000000, 0x07006E7C],
	[main.s_file, "stage/courtyard/seq.sx", courtyard_seq],
	[main.s_file, "stage/courtyard/shp.c", courtyard_shp],
]

################################################################################
# PSS
################################################################################

minislider_shape = [
	[main.f_str, "#ifndef SCRIPT\n\n"],
	[UNSM.c.f_gltf, "minislider", [
		("i0", None, ("../../../data/texture/i0.rgba16.png", 32, 32)),
		("i0_light", (0.25, 0xFF, 0xFF, 0xFF), ("../../../data/texture/i0.rgba16.png", 32, 32)),
		("i2_light", (0.25, 0xFF, 0xFF, 0xFF), ("../../../data/texture/i2.rgba16.png", 32, 32)),
		("i10", None, ("../../../data/texture/i10.rgba16.png", 32, 64)),
		("i10_light", (0.25, 0xFF, 0xFF, 0xFF), ("../../../data/texture/i10.rgba16.png", 32, 64)),
		("i12", None, ("../../../data/texture/i12.rgba16.png", 32, 32)),
		("i13", None, ("../../../data/texture/i13.rgba16.png", 32, 32)),
		("i21", None, ("../../../data/texture/i21.rgba16.png", 32, 32)),
		("i21_shade", (0.25, 0x8C, 0x8C, 0x8C), ("../../../data/texture/i21.rgba16.png", 32, 32)),
		("i21_light", (0.25, 0xFF, 0xFF, 0xFF), ("../../../data/texture/i21.rgba16.png", 32, 32)),
		("0", None, ("../0.rgba16.png", 32, 32)),
		("0_light", (0.25, 0xFF, 0xFF, 0xFF), ("../0.rgba16.png", 32, 32)),
		("1", None, ("../1.ia16.png", 32, 32)),
		("2", (0.25, 0xFF, 0xFF, 0xFF), ("../2.rgba16.png", 32, 32)),
	]],
	[ultra.c.f_data, "E0.PSS.Gfx", 0x07001800, 0x07001830, [
		[0, -2, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "0", [
		(True, "i21_shade"),
		(True, "i21_light"),
		(True, "0_light"),
		(True, "i0_light"),
		(True, "i10_light"),
		(True, "i2_light"),
	]],
	[ultra.c.f_data, "E0.PSS.Gfx", 0x070083B0, 0x0700A8B8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700A8B8, "0", 0, 1, 2, 3, 4, 5],
	]],
	[UNSM.c.f_gltf_mesh, "1", [
		(False, "i21"),
		(False, "i0"),
		(False, "i12"),
	]],
	[ultra.c.f_data, "E0.PSS.Gfx", 0x0700ADA8, 0x0700B070, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700B070, "1", 0, 1, 2],
	]],
	[UNSM.c.f_gltf_mesh, "2", [
		(False, "i13"),
	]],
	[ultra.c.f_data, "E0.PSS.Gfx", 0x0700B340, 0x0700B4A8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700B4A8, "2", 0],
	]],
	[UNSM.c.f_gltf_mesh, "3", [
		(False, "i12"),
	]],
	[ultra.c.f_data, "E0.PSS.Gfx", 0x0700CCA8, 0x0700D3A8, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700D3A8, "3", 0],
	]],
	[UNSM.c.f_gltf_mesh, "4", [
		(False, "1"),
	]],
	[ultra.c.f_data, "E0.PSS.Gfx", 0x0700D928, 0x0700DB48, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700DB48, "4", 0],
	]],
	[UNSM.c.f_gltf_mesh, "5", [
		(False, "i12"),
		(False, "0"),
		(False, "i10"),
	]],
	[ultra.c.f_data, "E0.PSS.Gfx", 0x0700E0A8, 0x0700E360, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700E348, "5", 0, 1, 2],
		[0, -1, 1, UNSM.c.d_light, 0.25],
	]],
	[UNSM.c.f_gltf_mesh, "6", [
		(True, "2"),
	]],
	[ultra.c.f_data, "E0.PSS.Gfx", 0x0700E3A0, 0x0700E490, [
		[0, 1, 1, UNSM.c.d_gfx, 0x0700E490, "6", 0],
	]],
	[UNSM.c.f_gltf_write],
	[main.f_str, "\n#else /* SCRIPT */\n\n"],
	[ultra.c.f_extern, "E0.PSS.Gfx", 0x07001800, 0x0700E490],
	[ultra.c.f_data, "E0.PSS", 0x0E000100, 0x0E0001B8, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E0001B8],
	]],
	[main.f_str, "\n#endif /* SCRIPT */\n"],
]

pss_gfx = [
	[main.f_str, "#include <sm64.h>\n\n"],
	[main.f_str, "#include \"data/texture/i.szp.h\"\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.PSS.Gfx", 0x07000000, 0x07001800, [
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "0"],
		[0, 1, 1, UNSM.c.d_texture, "ia16", 32, 32, "1"],
		[0, 1, 1, UNSM.c.d_texture, "rgba16", 32, 32, "2"],
	]],
	[main.f_str, "#include \"minislider/shape.c\"\n"],
	[UNSM.c.f_obj, "minislider/minislider"],
	[ultra.c.f_data, "E0.PSS.Gfx", 0x0700E490, 0x0701109C, [
		[0, 1, 1, UNSM.c.d_map, "minislider/map"],
		[0, 1, 1, UNSM.c.d_tag],
	]],
	[UNSM.c.f_obj_write],
]

pss_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.PSS", 0x0E000000, 0x0E0000F8],
]

seq_pss = [
	[main.s_file, "stage/pss/minislider/shape.c", minislider_shape],
	[main.s_file, "stage/pss/gfx.c", pss_gfx],
	[main.s_file, "stage/pss/seq.sx", pss_seq],
]

################################################################################
# CotMC
################################################################################

str_cotmc_gfx = """
.globl gfx_cotmc_0700BE10; gfx_cotmc_0700BE10 = 0x0700BE10
.globl gfx_cotmc_0700BE88; gfx_cotmc_0700BE88 = 0x0700BE88
.globl fluid_2801; fluid_2801 = 0x0700BED0
.globl gfx_cotmc_0700BF60; gfx_cotmc_0700BF60 = 0x0700BF60
"""

cotmc_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_cotmc_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.CotMC", 0x0E000000, 0x0E000194],
]

cotmc_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.CotMC", 0x0E0001A0, 0x0E000248, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000248],
	]],
]

seq_cotmc = [
	[main.s_bin, "stage/cotmc/gfx.bin", "E0.CotMC.Gfx", 0x07000000, 0x0700BFA8],
	[main.s_file, "stage/cotmc/seq.sx", cotmc_seq],
	[main.s_file, "stage/cotmc/shp.c", cotmc_shp],
]

################################################################################
# TotWC
################################################################################

totwc_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.TotWC", 0x0E000000, 0x0E000158],
]

totwc_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.TotWC", 0x0E000160, 0x0E000220, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000220],
	]],
]

seq_totwc = [
	[main.s_bin, "stage/totwc/gfx.bin", "E0.TotWC.Gfx", 0x07000000, 0x070089C6],
	[main.s_file, "stage/totwc/seq.sx", totwc_seq],
	[main.s_file, "stage/totwc/shp.c", totwc_shp],
]

################################################################################
# BitDWA
################################################################################

bitdwa_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.BitDWA", 0x0E000000, 0x0E0000D0],
]

bitdwa_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.BitDWA", 0x0E0000D0, 0x0E000158, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000158],
	]],
]

seq_bitdwa = [
	[main.s_bin, "stage/bitdwa/gfx.bin", "E0.BitDWA.Gfx", 0x07000000, 0x07002AC8],
	[main.s_file, "stage/bitdwa/seq.sx", bitdwa_seq],
	[main.s_file, "stage/bitdwa/shp.c", bitdwa_shp],
]

################################################################################
# WMotR
################################################################################

wmotr_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.WMotR", 0x0E000000, 0x0E0001E4],
]

wmotr_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.WMotR", 0x0E0001F0, 0x0E00029C, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E00029C],
	]],
]

seq_wmotr = [
	[main.s_bin, "stage/wmotr/gfx.bin", "E0.WMotR.Gfx", 0x07000000, 0x070137AE],
	[main.s_file, "stage/wmotr/seq.sx", wmotr_seq],
	[main.s_file, "stage/wmotr/shp.c", wmotr_shp],
]

################################################################################
# BitFSA
################################################################################

bitfsa_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.BitFSA", 0x0E000000, 0x0E00016C],
]

bitfsa_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.BitFSA", 0x0E000170, 0x0E000210, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000210],
	]],
]

seq_bitfsa = [
	[main.s_bin, "stage/bitfsa/gfx.bin", "E0.BitFSA.Gfx", 0x07000000, 0x07001BA0],
	[main.s_file, "stage/bitfsa/seq.sx", bitfsa_seq],
	[main.s_file, "stage/bitfsa/shp.c", bitfsa_shp],
]

################################################################################
# BitSA
################################################################################

bitsa_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[UNSM.asm.f_seqlang, "E0.BitSA", 0x0E000000, 0x0E00028C],
]

bitsa_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.BitSA", 0x0E000290, 0x0E000420, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000420],
	]],
]

seq_bitsa = [
	[main.s_bin, "stage/bitsa/gfx.bin", "E0.BitSA.Gfx", 0x07000000, 0x070050BC],
	[main.s_file, "stage/bitsa/seq.sx", bitsa_seq],
	[main.s_file, "stage/bitsa/shp.c", bitsa_shp],
]

################################################################################
# TTM
################################################################################

str_ttm_gfx = """
.globl wave_ttm_07012F00; wave_ttm_07012F00 = 0x07012F00
.globl water_3601; water_3601 = 0x07017124
.globl fluid_3601; fluid_3601 = 0x07017134
.globl fluid_3603; fluid_3603 = 0x07017174
.globl fluid_3602; fluid_3602 = 0x070171A0
.globl fluid_3604; fluid_3604 = 0x070171E0
.globl fluid_3605; fluid_3605 = 0x0701720C
.globl gfx_ttm_07017260; gfx_ttm_07017260 = 0x07017260
.globl gfx_ttm_07017288; gfx_ttm_07017288 = 0x07017288
.globl gfx_ttm_070172A0; gfx_ttm_070172A0 = 0x070172A0
"""

ttm_seq = [
	[main.f_str, "#include <sm64/seqlang.h>\n\n.data\n\n"],
	[main.f_str, str_ttm_gfx],
	[main.f_str, "\n"],
	[UNSM.asm.f_seqlang, "E0.TTM", 0x0E000000, 0x0E000710],
]

ttm_shp = [
	[main.f_str, "#include <sm64/shplang.h>\n\n#define SCRIPT\n\n"],
	[main.f_str, "\n"],
	[ultra.c.f_data, "E0.TTM", 0x0E000710, 0x0E000E0C, [
		[0, 1, 1, UNSM.c.d_shplang, 0x0E00093C],
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000940, 1],
		[0, 1, 1, UNSM.c.d_shplang, 0x0E000E0C, 1],
	]],
]

seq_ttm = [
	[main.s_bin, "stage/ttm/gfx.bin", "E0.TTM.Gfx", 0x07000000, 0x07030474],
	[main.s_file, "stage/ttm/seq.sx", ttm_seq],
	[main.s_file, "stage/ttm/shp.c", ttm_shp],
]
