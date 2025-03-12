import main
import ultra

import UNSM.asm

vitbl = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.code.data", 0x80335010, 0x803358D0, [
		[1, -28, ultra.c.d_OSViMode],
	]],
]

vimodentsclan1 = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.code.data", 0x80335AA0, 0x80335AF0, [
		[0, 1, ultra.c.d_OSViMode],
	]],
]

vimodepallan1 = [
	[main.f_str, "#include <ultra64.h>\n\n"],
	[ultra.c.f_data, "E0.code.data", 0x80335AF0, 0x80335B40, [
		[0, 1, ultra.c.d_OSViMode],
	]],
]


str_ucode = """
.relativeinclude on
.include "rsp.inc"

"""

str_ucode_create = """
.relativeinclude off
.create BUILD+"/%s.bin", %s
.relativeinclude on

"""

str_ucode_base = """
.relativeinclude off
.create BUILD+"/%s.bin", 0
.relativeinclude on
.base %s

"""

str_ucode_close = """
.close

"""

rspboot = [
	[main.f_str, str_ucode],
	[main.f_str, str_ucode_create % ("rspboot.text", "0x04001000")],
	[ultra.asm.f_code, "D.rspboot.text", 0x04001000, 0x040010D0, 1],
	[main.f_str, "\n.align 8\n"],
	[main.f_str, str_ucode_close],
]

gspFast3D_init = [
	[main.f_str, str_ucode_create % ("gspFast3D.fifo.init", "0x04001080")],
	[main.f_str, "prg_init_start:\n\n"],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text", 0x04001080, 0x04001088, 1],
	[main.f_str, str_ucode_close],
]

gspFast3D_main = [
	[main.f_str, str_ucode_create % ("gspFast3D.fifo.main", "0x04001000")],
	[main.f_str, "prg_main_start:\n\n"],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text.main", 0x04001000, 0x04001088, 1],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text", 0x04001088, 0x04001250, 1],
	[main.f_str, "\ncase_G_POPMTX:\n"],
	[main.f_str, ".if REVISION >= 199611\n"],
	[ultra.asm.f_code, "F.gspFast3D_fifo.text", 0x04001250, 0x04001254, 1],
	[main.f_str, ".endif\n"],
	[ultra.asm.f_code, "F.gspFast3D_fifo.text", 0x04001254, 0x04001258, 1],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text", 0x04001254, 0x04001310, 1],
	[main.f_str, ".if REVISION >= 199610\n"],
	[ultra.asm.f_code, "F.gspFast3D_fifo.text", 0x04001314, 0x04001318, 1],
	[main.f_str, ".else\n"],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text", 0x04001310, 0x04001314, 1],
	[main.f_str, ".endif\n"],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text", 0x04001314, 0x04001370, 1],
	[main.f_str, "\n.if REVISION < 199611\n"],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text", 0x04001370, 0x04001378, 1],
	[main.f_str, ".endif\n\n"],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text", 0x04001378, 0x04001768, 1],
	[main.f_str, "\n.align 8\n"],
	[main.f_str, "prg_ext_start:\n\n"],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text", 0x04001768, 0x0400188C, 1],
	[main.f_str, "\n.fill max(prg_clip_end, prg_light_end, prg_exit_end) - .\n"],
	[main.f_str, ".if REVISION < 199611\n"],
	[main.f_str, ".fill 16\n"],
	[main.f_str, ".endif\n\n"],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text", 0x04001998, 0x04001FDC, 1],
	[main.f_str, "\n.align 8\n"],
	[main.f_str, str_ucode_close],
]

gspFast3D_clip = [
	[main.f_str, str_ucode_base % ("gspFast3D.fifo.clip", "prg_ext_start")],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text.clip", 0x04001768, 0x04001988, 1],
	[main.f_str, "\n.align 8\n"],
	[main.f_str, "prg_clip_end:\n"],
	[main.f_str, str_ucode_close],
]

gspFast3D_light = [
	[main.f_str, str_ucode_base % ("gspFast3D.fifo.light", "prg_ext_start")],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text.light", 0x04001768, 0x040018FC, 1],
	[main.f_str, "\n.align 8\n"],
	[main.f_str, "prg_light_end:\n"],
	[main.f_str, str_ucode_close],
]

gspFast3D_exit = [
	[main.f_str, str_ucode_base % ("gspFast3D.fifo.exit", "prg_ext_start")],
	[ultra.asm.f_code, "D.gspFast3D_fifo.text.exit", 0x04001768, 0x040017CC, 1],
	[main.f_str, "\n.align 8\n"],
	[main.f_str, "prg_exit_end:\n"],
	[main.f_str, str_ucode_close],
]

gspFast3D_data = [
	[main.f_str, str_ucode_create % ("gspFast3D.fifo.data", "0")],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x04000000, 0x04000030, 1, [
		[ 5, 1, UNSM.asm.d_prg],
		[ 1, 4, ultra.asm.d_shalf],
	]],
	[main.f_str, "\n.align 16\n"],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x04000030, 0x040000DE, 1, [
		[ 1, 8, ultra.asm.d_shalf],
		[ 1, 8, ultra.asm.d_uhalf, "0x%04X"],
		[ 1, 8, ultra.asm.d_shalf],
		[ 1, 8, ultra.asm.d_shalf],
		[ 3, 8, ultra.asm.d_shalf], # clipping
		[ 1, 1, ultra.asm.d_haddr], # vtx_light
		[ 1, 3, ultra.asm.d_uhalf, "0x%04X"], # arccos
		[ 1, 6, ultra.asm.d_uhalf, "0x%04X"],
		[ 1, 1, ultra.asm.d_shalf],
		[ 1, 1, ultra.asm.d_haddr], # exit
		[ 1, 1, ultra.asm.d_uword, "0x%X"], # segment mask
		[ 4, 1, ultra.asm.d_haddr], # cmd type
		[10, 1, ultra.asm.d_haddr], # cmd DMA
		[ 3, 1, ultra.asm.d_haddr], # cmd IMM
	]],
	[main.f_str, ".if REVISION < 199611\n"],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x040000DE, 0x040000E0, 1, [
		[ 1, 1, ultra.asm.d_haddr], # cmd IMM
	]],
	[main.f_str, ".endif\n"],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x040000E0, 0x040000F6, 1, [
		[11, 1, ultra.asm.d_haddr], # cmd IMM
	]],
	[main.f_str, "IMMTAB_END:\n\n"],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x040000F6, 0x04000108, 1, [
		[ 7, 1, ultra.asm.d_haddr], # clip
		[ 1, 1, ultra.asm.d_haddr], # cmd_next_sync
		[ 1, 1, ultra.asm.d_uhalf], # return
	]],
	[main.f_str, "\n.align 4\n"],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x04000108, 0x04000110, 1, [
		[ 1, 1, ultra.asm.d_uword], # yield
		[ 1, 1, ultra.asm.d_uword], # rdphalf
	]],
	[main.f_str, "\n.align 8\n"],
	[main.f_str, "STATE:\n\n"],
	[main.f_str, ".if REVISION < 199611\n"],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x04000110, 0x04000111, 1, [
		[ 1, 1, ultra.asm.d_ubyte], # DL no
	]],
	[main.f_str, ".endif\n\n"],
	[main.f_str, ".if REVISION >= 199611\n"],
	[main.f_str, ".align 4\n"],
	[ultra.asm.f_data, "F.gspFast3D_fifo.data", 0x04000110, 0x04000114, 1, [
		[ 2, 1, ultra.asm.d_uhalf, "0x%04X"], # perspnorm
	]],
	[main.f_str, ".else\n"],
	[main.f_str, ".align 2\n"],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x04000112, 0x04000114, 1, [
		[ 1, 1, ultra.asm.d_uhalf, "0x%04X"], # perspnorm
	]],
	[main.f_str, ".endif\n"],
	[main.f_str, "\n.align 4\n"],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x04000114, 0x04000150, 1, [
		[ 1, 1, ultra.asm.d_uhalf], # geometrymode
		[ 2, 1, ultra.asm.d_ubyte], # geometrymode
		[ 2, 1, ultra.asm.d_uword, "0x%08X"], # othermode
		[ 4, 1, ultra.asm.d_ubyte], # texture
		[ 2, 1, ultra.asm.d_uhalf], # texture
		[ 1, 1, ultra.asm.d_uword], # output
		[ 1, 1, ultra.asm.d_uword, "0x%08X"], # light no
		[ 2, 1, ultra.asm.d_uword], # stack
		[ 2, 1, ultra.asm.d_uhalf, "0x%04X"],
		[ 2, 1, ultra.asm.d_shalf],
		[ 1, 1, ultra.asm.d_uword], # output
		[ 4, 1, ultra.asm.d_shalf],
	]],
	[main.f_str, "\n.align 8\n"],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x04000150, 0x0400015A, 1, [
		[ 1, 1, ultra.asm.d_uword], # output len
		[ 1, 1, ultra.asm.d_uword],
		[ 1, 1, ultra.asm.d_uhalf], # return
	]],
	[main.f_str, "\n.if REVISION >= 199611\n"],
	[ultra.asm.f_data, "F.gspFast3D_fifo.data", 0x0400015A, 0x0400015B, 1, [
		[ 1, 1, ultra.asm.d_ubyte], # DL no
	]],
	[main.f_str, ".endif\n"],
	[main.f_str, "\n.align 4\n"],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x0400015C, 0x040001A0, 1, [
		[ 1, 1, ultra.asm.d_uword], # stack
		[ 1, 16, ultra.asm.d_uword], # segment table
	]],
	[main.f_str, "\n.align 16\n"],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x040001A0, 0x0400031C, 1, [
		[ 1, 4, ultra.asm.d_uhalf, "0x%04X"], # select S
		[ 1, 2, ultra.asm.d_uword],
		# lights
		# LOOKATX
		[ 1, 4, ultra.asm.d_uhalf, "0x%04X"], # select T
		[ 1, 4, ultra.asm.d_sbyte], # direction
		[ 1, 1, ultra.asm.d_uword],
		[ 1, 8, ultra.asm.d_sbyte], # direction
		[ 1, 2, ultra.asm.d_uword],
		# LOOKATY
		[ 1, 2, ultra.asm.d_uword],
		[ 1, 4, ultra.asm.d_sbyte], # direction
		[ 1, 1, ultra.asm.d_uword],
		[ 1, 8, ultra.asm.d_sbyte], # direction
		[ 1, 2, ultra.asm.d_uword],
		# L0
		[ 1, 6, ultra.asm.d_uword],
		[ 1, 4, ultra.asm.d_shalf], # VCONST3
		# L1
		[ 1, 2, ultra.asm.d_uword, "0x%08X"], # colour
		[ 1, 6, ultra.asm.d_uword],
		[ 1, 8, ultra.asm.d_uword], # L2
		[ 1, 8, ultra.asm.d_uword], # L3
		[ 1, 30, "asciz"], # L4
		[ 1,  1, "ascii"],
		[ 1, 32, "ascii"], # L5
		[ 1, 32, "ascii"], # L6
		[ 1, 26, "ascii"], # L7
		[ 1, 2, ultra.asm.d_ubyte],
		[ 1, 1, ultra.asm.d_uword],
		[15, 1, ultra.asm.d_haddr], # movemem table
		[ 7, 1, ultra.asm.d_haddr], # movemem table
	]],
	[main.f_str, ".if REVISION >= 199611\n"],
	[ultra.asm.f_data, "F.gspFast3D_fifo.data", 0x0400031C, 0x0400031E, 1, [
		[ 1, 1, ultra.asm.d_haddr], # movemem table
	]],
	[main.f_str, ".endif\n"],
	[main.f_str, "\n.align 16\n"],
	[ultra.asm.f_data, "D.gspFast3D_fifo.data", 0x04000320, 0x04000800, 1, [
		[ 1, 8, ultra.asm.d_shalf], # viewport
		[ 1, 3, ultra.asm.d_shalf, "0x%02X"], # fog
		[ 1, 10, ultra.asm.d_uword], # DL stack
	]],
	[main.f_str, "\n.align 16\n"],
	[main.f_str, "\n.if 0x800-orga() > 0\n"],
	[main.f_str, ".fill 0x800-orga()\n"],
	[main.f_str, ".endif\n"],
	[main.f_str, str_ucode_close],
]

aspMain = [
	[main.f_str, str_ucode],
	[main.f_str, str_ucode_create % ("aspMain.text", "0x04001080")],
	[ultra.asm.f_code, "D.aspMain.text", 0x04001080, 0x04001E9C, 1],
	[main.f_str, "\n.align 8\n"],
	[main.f_str, str_ucode_close],
	[main.f_str, str_ucode_create % ("aspMain.data", "0")],
	[ultra.asm.f_data, "D.aspMain.data", 0x04000000, 0x040002C0, 1, [
		[(0x10)//0x10, 4, ultra.asm.d_uword, "0x%08X"],
		[16, 1, ultra.asm.d_haddr],
		[(0x2C0-0x30)//0x10, 4, ultra.asm.d_uword, "0x%08X"],
	]],
	[main.f_str, "\n.align 8\n"],
	[main.f_str, str_ucode_close],
]

def f_romheader(version):
	return [main.s_file, "libultra/2.0"+version+"/lib/PR/romheader", [
		[ultra.f_romheader, version+".romheader"],
	]]

seq = [
	f_romheader("D"),
	f_romheader("F"),
	f_romheader("H"),
	f_romheader("L"),

	[main.s_bin, "libultra/lib/PR/font", "IPL3_6102", 0xA4000B70, 0xA4000FEE],

	[main.s_file, "libultra/src/io/vitbl.c", vitbl],
	[main.s_file, "libultra/src/vimodentsclan1.c", vimodentsclan1],
	[main.s_file, "libultra/src/vimodepallan1.c", vimodepallan1],

	[main.s_file, "libultra/src/PR/rspboot.asm", rspboot],
	[main.s_file, "libultra/src/PR/gspFast3D/init.asm", gspFast3D_init],
	[main.s_file, "libultra/src/PR/gspFast3D/main.asm", gspFast3D_main],
	[main.s_file, "libultra/src/PR/gspFast3D/clip.asm", gspFast3D_clip],
	[main.s_file, "libultra/src/PR/gspFast3D/light.asm", gspFast3D_light],
	[main.s_file, "libultra/src/PR/gspFast3D/exit.asm", gspFast3D_exit],
	[main.s_file, "libultra/src/PR/gspFast3D/data.asm", gspFast3D_data],
	[main.s_file, "libultra/src/PR/aspMain.asm", aspMain],
]
