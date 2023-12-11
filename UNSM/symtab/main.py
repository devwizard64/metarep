import main

sym_J0_Main = {
	0x001076A0: main.sym("_MainSegmentRomStart"),

	0x10000000: main.sym("p_main", flag={"GLOBL"}),
}

sym_E0_Main = {
	0x00108A10: main.sym("_MainSegmentRomStart"),

	0x10000000: main.sym("p_main", flag={"GLOBL"}),
}
