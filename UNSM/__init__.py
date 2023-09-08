import os
import struct

import main
import ultra

import UNSM.asm
import UNSM.c
import UNSM.tools.lang
import UNSM.table
import UNSM.header

def str_include(lst):
	return "".join([
		("#include \"%s.h\"\n" % x[1:])
		if x.startswith("$") else
		("#include <%s.h>\n" % x)
		for x in lst
	])

def s_include(lst): return [main.s_str, str_include(lst)]

str_gp      = ".set gp=64\n"
str_fp      = ".set fp=32\n"
str_align   = ".align 4\n"
str_data    = ".data\n"
str_rdata   = ".rdata\n"
str_bss     = ".bss\n"
str_script  = "#define SCRIPT\n"

str_ucode = """
.include "libultra/src/PR/rsp.inc"

"""

str_ucode_create = """
.create BUILD+"/libultra/src/PR/%s.bin", %s

"""

str_ucode_base = """
.create BUILD+"/libultra/src/PR/%s.bin", 0
.base %s

"""

str_ucode_close = """
.close

"""

str_ucode_s_text = """
.globl %sTextStart
%sTextStart:
.incbin "libultra/src/PR/%s.text.bin"
.globl %sTextEnd
%sTextEnd:
"""

str_ucode_s_data = """
.data

.globl %sDataStart
%sDataStart:
.incbin "libultra/src/PR/%s.data.bin"
.globl %sDataEnd
%sDataEnd:
"""

str_gspFast3D_fifo = """
.globl gspFast3D_fifoTextStart
gspFast3D_fifoTextStart:

init_start:
.incbin "libultra/src/PR/gspFast3D.fifo.init.bin"
.incbin "libultra/src/PR/gspFast3D.fifo.main.bin", 0x88
init_end:

main_start:
.incbin "libultra/src/PR/gspFast3D.fifo.main.bin", 0, 0x88
main_end:

clip_start:
.incbin "libultra/src/PR/gspFast3D.fifo.clip.bin"
clip_end:

light_start:
.incbin "libultra/src/PR/gspFast3D.fifo.light.bin"
light_end:

exit_start:
.incbin "libultra/src/PR/gspFast3D.fifo.exit.bin"
exit_end:

.globl gspFast3D_fifoTextEnd
gspFast3D_fifoTextEnd:

.data

.globl gspFast3D_fifoDataStart
gspFast3D_fifoDataStart:

.set DATA, 0

.macro prg name
	.word \\name\\()_start - gspFast3D_fifoTextStart
	.half \\name\\()_end - \\name\\()_start - 1
	.incbin "libultra/src/PR/gspFast3D.fifo.data.bin", DATA+6, 2
	.set DATA, DATA+8
.endm

prg init
prg main
prg clip
prg light
prg exit

.incbin "libultra/src/PR/gspFast3D.fifo.data.bin", DATA

.globl gspFast3D_fifoDataEnd
gspFast3D_fifoDataEnd:
"""

str_camera_data = """
#define CAM_WINDEMO(x1, x2, x3, x4, x5, x6, x7) \\
{ \\
	((x1) & 0x0F) | ((x2) & 0x0F) << 4, \\
	((x3) & 0x0F) | ((x4) & 0x0F) << 4, \\
	((x5) & 0x0F) | ((x6) & 0x0F) << 4, \\
	((x7) & 0x0F), \\
}

#define CAM_PAUSE(a1, a2, a3, a4, b1, b2, b3, b4) \\
( \\
	((a1) & 1) << 0 | ((a2) & 1) << 1 | \\
	((a3) & 1) << 2 | ((a4) & 1) << 3 | \\
	((b1) & 1) << 4 | ((b2) & 1) << 5 | \\
	((b3) & 1) << 6 | ((b4) & 1) << 7 \\
)

BALIGN PL_CAMERA pl_camera_data[2];
BALIGN char _camera_bss_48[0x178-0x48];
BALIGN CAMDATA camdata;
BALIGN char _camera_bss_238[0x6C0-0x238];
"""

str_anime = """
#define ANIME(anime, flag, waist, start, loop, frame, joint) \\
	.short flag, waist, start, loop, frame, joint; \\
	.word anime##_val - anime; \\
	.word anime##_tbl - anime; \\
	.word anime##_end - anime

.data

"""

str_demo = """
#define DEMO(stage) .byte stage, 0, 0, 0

.data

"""

str_audio_g_data = """
#define BGMCTL_GE_X     0
#define BGMCTL_GE_Y     1
#define BGMCTL_GE_Z     2
#define BGMCTL_LT_X     3
#define BGMCTL_LT_Y     4
#define BGMCTL_LT_Z     5
#define BGMCTL_SCENE    6
#define BGMCTL_AREA     7

#define BGMCTL(x)       (0x8000 >> BGMCTL_##x)
"""

# temporary

str_audio_g = """
.globl _Na_g_bss
_Na_g_bss:
.space 0x3710
"""

str_audio_bss = """
.globl _Na_bss
_Na_bss:
.space 0x5F1C
"""

str_face_draw = """
.globl _face_draw_data
_face_draw_data:
.incbin "src/face/draw.data.bin"
"""

str_face_object = """
.globl _face_object_data
_face_object_data:
.incbin "src/face/object.data.bin"
"""

str_face_particle = """
.globl _face_particle_data
_face_particle_data:
.incbin "src/face/particle.data.bin"
"""

str_face_dynlist = """
.globl _face_dynlist_data
_face_dynlist_data:
.incbin "src/face/dynlist.data.bin"
"""

str_face_stdio = """
.globl _face_stdio_data
_face_stdio_data:
.incbin "src/face/stdio.data.bin"
"""

str_face_joint = """
.globl _face_joint_data
_face_joint_data:
.incbin "src/face/joint.data.bin"
"""

str_face_shape = """
.globl _face_shape_data
_face_shape_data:
.incbin "src/face/shape.data.bin"
"""

str_face_gfx = """
.globl _face_gfx_data
_face_gfx_data:
.incbin "src/face/gfx.data.bin"
"""

str_face_bss = """
.globl _face_bss
_face_bss:
.space 0x5080
"""

def slidec(src):
	sig, size, p, c = struct.unpack(">4sIII", src[:16])
	s = 16
	dst = B""
	bit = 0
	cnt = 0
	while len(dst) < size:
		if cnt == 0:
			bit, = struct.unpack(">I", src[s:s+4]); s += 4
			cnt = 32
		if bit & 0x80000000:
			dst += src[c:c+1]; c += 1
		else:
			x, = struct.unpack(">H", src[p:p+2]); p += 2
			o = len(dst) - ((x & 0xFFF) + 1)
			n = (x >> 12) + 3
			dst += (n*dst[o:o+n])[:n]
		bit <<= 1
		cnt -= 1
	return dst

def s_szp(self, argv):
	start, end, data = argv
	self.data[data+".szp"] = self.cache(start, end, data, slidec)
	self.dev = start

def s_szpbin(start, end, size, name):
	return [main.s_call, [
		[s_szp, start, end, "E0"],
		[main.s_addr, 0],
		[main.s_bin, 0, size, "E0.szp", ["%s.bin" % name]],
		[main.s_dev, None],
	]]

def s_dirfile(path, fn):
	if path != None:
		return [main.s_call, [
			[main.s_dir, path],
			[main.s_str, "#include \"%s/%s\"\n" % (path, fn)],
			[main.s_file, fn],
		]]
	return [main.s_call, [
		[main.s_str, "#include \"%s\"\n" % fn],
		[main.s_file, fn],
	]]

def s_writepop():
	return [main.s_call, [
		[main.s_write],
		[main.s_pop],
	]]

def s_def(s, l=0, r=0):
	return [main.s_str, "\n"*l + s + "\n"*(1+r)]

def s_ifdef(s, l=0, r=0):   return s_def("#ifdef %s"        % s, l, r)
def s_ifndef(s, l=0, r=0):  return s_def("#ifndef %s"       % s, l, r)
def s_define(s, l=0, r=0):  return s_def("#define %s"       % s, l, r)
def s_else(s, l=0, r=0):    return s_def("#else /* %s */"   % s, l, r)
def s_endif(s, l=0, r=0):   return s_def("#endif /* %s */"  % s, l, r)

def s_script_ifdef():   return s_ifdef("SCRIPT", 1, 1)
def s_script_ifndef():  return s_ifndef("SCRIPT", 1, 1)
def s_script_else():    return s_else("SCRIPT", 1, 1)
def s_script_endif():   return s_endif("SCRIPT", 1, 1)

def s_header_macro(self, argv):
	fmt, = argv
	fn = self.file[-1][0].rpartition("include" + os.path.sep)[-1]
	self.file[-1][1].append(fmt % "".join([
		x if x in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" else "_"
		for x in fn.upper()
	]))

def s_header(name, lst):
	return [main.s_call, [
		[main.s_file, "%s.h" % name],
			[s_header_macro, "#ifndef __%s__\n"],
			[s_header_macro, "#define __%s__\n\n"],
	] + lst + [
			[s_header_macro, "\n#endif /* __%s__ */\n"],
		[main.s_write],
	]]

def s_header_code(ts, te, ds, de, bs, be, name, st=[], s=""):
	return s_header(name, [
			[main.s_str, s],
			[main.s_str, "\n"],
			[ultra.c.s_struct, st],
			[main.s_str, "\n"],
			[ultra.c.s_extern, bs, be, "E0", ds],
			[ultra.c.s_extern, ds, de, "E0", None],
			[main.s_str, "\n"],
			[ultra.c.s_extern, ts, te, "E0", None],
	])

def s_code(start, end, fn, include=[], s="", macro=True, sep=False):
	return [main.s_call, [
		[main.s_file, ("%s.sx" if include else "%s.s") % fn],
			[main.s_str, ".include \"sm64/asm.inc\"\n" if macro else ""],
			s_include(include),
			[main.s_str, "\n"],
			[main.s_str, s],
			[main.s_str, ".set noreorder\n.set noat\n"],
			[main.s_str, "\n"],
			[main.s_str, str_align],
			[main.s_str, "\n"],
			[ultra.asm.s_code, start, end, "E0", 0, macro, sep],
		[main.s_write],
	]]

def s_data(ds, de, rs, re, bs, be, fn, include, dl, rl, s=""):
	return [main.s_call, [
		[main.s_file, "%s.c" % fn],
			s_include(include),
			[main.s_str, "\n"], [main.s_str, s],
			[main.s_str, "\n"], [ultra.c.s_data, rs, re, "E0", rl],
			[main.s_str, "\n"], [ultra.c.s_bss,  bs, be, "E0", ds],
			[main.s_str, "\n"], [ultra.c.s_data, ds, de, "E0", dl],
		[main.s_write],
	]]

def s_databin(start, end, name):
	return [main.s_bin, start, end, "E0", ["%s.bin" % name]]

def s_gfx(start, end, a, name, lst):
	return [main.s_call, [
		[s_szp, start, end, "E0"],
		[main.s_addr, a << 24],
		[main.s_file, "%s.c" % name],
			[main.s_call, lst],
		[main.s_write],
		[main.s_dev, None],
	]]

def s_shapebin(start, end, size, ssize, b, name, shape, s=""):
	return [main.s_call, [
		[main.s_dir, name],
			s_szpbin(start, end, size, "gfx"),
			[main.s_addr, (b << 24) - end],
			[main.s_file, "shape.c"],
				s_include(["sm64/shplang"]),
				[main.s_str, "\n"],
				[main.s_str, s],
				[main.s_str, "\n"],
				[ultra.c.s_data, b << 24, (b << 24) + ssize, "E0", shape],
			[main.s_write],
		[main.s_pop],
	]]

def s_shape(start, end, a, b, name, gfx, shape, s=""):
	return [main.s_call, [
		[main.s_dir, name],
			[s_szp, start, end, "E0"],
			[main.s_addr, (a << 24)],
			[main.s_file, "gfx.c"],
				s_include(["sm64"]),
				[main.s_str, "\n"],
				[main.s_call, gfx],
			[main.s_write],
			[main.s_dev, None],
			[main.s_addr, (b << 24) - end],
			[main.s_file, "shape.c"],
				s_include(["sm64/shplang"]),
				[main.s_str, "\n"],
				[main.s_str, s],
				[main.s_str, "\n"],
				[main.s_call, shape],
			[main.s_write],
		[main.s_pop],
	]]

def s_script(start, end, addr, size, p="", s=""):
	p_start = addr
	p_end   = addr + size
	s_start = (p_end+0x0F) & ~0x0F
	s_end   = addr + end-start
	return [main.s_call, [
		[main.s_addr, addr-start],
		[main.s_file, "program.sx"],
			s_include(["sm64/prglang"]),
			[main.s_str, "\n"],
			[main.s_str, p],
			[main.s_str, "\n"],
			[main.s_str, str_data],
			[main.s_str, "\n"],
			[asm.s_script, p_start, p_end, "E0", 0],
		[main.s_write],
		[main.s_file, "shape.c"],
			s_include(["sm64/shplang"]),
			[main.s_str, "\n"],
			[main.s_str, s],
			[main.s_str, "\n"],
			[ultra.c.s_data, s_start, s_end, "E0", [
				[0, 1, 1, c.d_s_script, s_end],
			]],
		[main.s_write],
	]]

def s_shape_p(start, end, name):
	return [main.s_call, [
		s_dirfile(os.path.join("shape", name), "program.sx"),
			[asm.s_script, start, end, "E0", 0],
		s_writepop(),
	]]

def s_stagebin(a, b, c, size, ssize, name, p="", s=""):
	return [main.s_call, [
		[main.s_dir, name],
			s_szpbin(a, b, size, "gfx"),
			s_script(b, c, 0x0E000000, ssize, p, s),
		[main.s_pop],
	]]

def s_stage(start, end, size, name, gfx, shape, p="", s=""):
	return [main.s_call, [
		[main.s_dir, name],
			[s_szp, start, end, "E0"],
			[main.s_addr, 0x07000000],
			[main.s_file, "gfx.c"],
				s_include(["sm64"]),
				[main.s_str, "\n"],
				[main.s_call, gfx],
			[main.s_write],
			[main.s_dev, None],
			[main.s_addr, 0x0E000000-end],
			[main.s_file, "program.sx"],
				s_include(["sm64/prglang"]),
				[main.s_str, "\n"],
				[main.s_str, p],
				[main.s_str, "\n"],
				[main.s_str, str_data],
				[main.s_str, "\n"],
				[asm.s_script, 0x0E000000, 0x0E000000+size, "E0", 0],
			[main.s_write],
			[main.s_file, "shape.c"],
				s_include(["sm64/shplang"]),
				[main.s_str, "\n"],
				[main.s_str, s],
				[main.s_str, "\n"],
				[main.s_call, shape],
			[main.s_write],
		[main.s_pop],
	]]

def d_texture_n(t, w, h, end, fmt="%d", start=0, step=1):
	return [0, 1, [
		[0, 1, 1, c.d_texture, t, w, h, fmt % i]
		for i in range(start, end, step)
	]]

libultra_src = [
	s_code(0x803223B0, 0x803223D4, "settime",               ["ultra64"], "", False),
	s_code(0x803223E0, 0x80322494, "maptlb",                ["ultra64"], "", False),
	s_code(0x803224A0, 0x803224E4, "unmaptlball",           ["ultra64"], "", False),
	s_code(0x803224F0, 0x80322594, "sprintf",               ["ultra64"], "", False),
	s_code(0x803225A0, 0x803225CC, "createmesgqueue",       ["ultra64"], "", False),
	s_code(0x803225D0, 0x80322638, "seteventmesg",          ["ultra64"], "", False),
	s_code(0x80322640, 0x803226AC, "visetevent",            ["ultra64"], "", False),
	s_code(0x803226B0, 0x803227F4, "createthread",          ["ultra64"], "", False),
	s_code(0x80322800, 0x80322938, "recvmesg",              ["ultra64"], "", False),
	s_code(0x80322940, 0x80322BFC, "sptask",                ["ultra64"], "", False),
	s_code(0x80322C00, 0x80322C20, "sptaskyield",           ["ultra64"], "", False),
	s_code(0x80322C20, 0x80322D6C, "sendmesg",              ["ultra64"], "", False),
	s_code(0x80322D70, 0x80322DF0, "sptaskyielded",         ["ultra64"], "", False),
	s_code(0x80322DF0, 0x80322F40, "startthread",           ["ultra64"], "", False),
	s_code(0x80322F40, 0x80322F68, "writebackdcacheall",    ["ultra64"], "", False),
	s_code(0x80322F70, 0x803232C4, "vimgr",                 ["ultra64"], "", False),
	s_code(0x803232D0, 0x80323338, "visetmode",             ["ultra64"], "", False),
	s_code(0x80323340, 0x803233B0, "viblack",               ["ultra64"], "", False),
	s_code(0x803233B0, 0x80323568, "visetspecial",          ["ultra64"], "", False),
	s_code(0x80323570, 0x803236EC, "pimgr",                 ["ultra64"], "", False),
	s_code(0x803236F0, 0x803237D0, "setthreadpri",          ["ultra64"], "", False),
	s_code(0x803237D0, 0x80323A00, "initialize",            ["ultra64"], "", False),
	s_code(0x80323A00, 0x80323A50, "viswapbuf",             ["ultra64"], "", False),
	s_code(0x80323A50, 0x80323A58, "sqrtf",                 ["ultra64"], "", False),
	s_code(0x80323A60, 0x80323CB8, "contreaddata",          ["ultra64"], "", False),
	s_code(0x80323CC0, 0x80324080, "controller",            ["ultra64"], "", False),
	s_code(0x80324080, 0x803240EC, "conteepprobe",          ["ultra64"], "", False),
	s_code(0x803240F0, 0x803243B0, "ll",                    ["ultra64"], str_gp, False),
	s_code(0x803243B0, 0x8032445C, "invaldcache",           ["ultra64"], "", False),
	s_code(0x80324460, 0x80324564, "pidma",                 ["ultra64"], "", False),
	s_code(0x80324570, 0x8032460C, "bzero",                 ["ultra64"], "", False),
	s_code(0x80324610, 0x80324684, "invalicache",           ["ultra64"], "", False),
	s_code(0x80324690, 0x803247CC, "conteeplongread",       ["ultra64"], "", False),
	s_code(0x803247D0, 0x8032490C, "conteeplongwrite",      ["ultra64"], "", False),
	s_code(0x80324910, 0x80324C14, "bcopy",                 ["ultra64"], "", False),
	s_code(0x80324C20, 0x80324DDC, "ortho",                 ["ultra64"], "", False),
	s_code(0x80324DE0, 0x80325068, "perspective",           ["ultra64"], str_fp, False),
	s_code(0x80325070, 0x803250F4, "gettime",               ["ultra64"], "", False),
	s_code(0x80325100, 0x80325308, "llcvt",                 ["ultra64"], str_gp+str_fp, False),
	s_code(0x80325310, 0x80325478, "cosf",                  ["ultra64"], str_fp, False),
	s_code(0x80325480, 0x80325640, "sinf",                  ["ultra64"], str_fp, False),
	s_code(0x80325640, 0x803256DC, "translate",             ["ultra64"], "", False),
	s_code(0x803256E0, 0x803258C4, "rotate",                ["ultra64"], "", False),
	s_code(0x803258D0, 0x8032596C, "scale",                 ["ultra64"], "", False),
	s_code(0x80325970, 0x80325AD0, "aisetfreq",             ["ultra64"], "", False),
	s_code(0x80325AD0, 0x80325D18, "bnkf",                  ["ultra64"], "", False),
	s_code(0x80325D20, 0x80325D94, "writebackdcache",       ["ultra64"], "", False),
	s_code(0x80325DA0, 0x80325DAC, "aigetlen",              ["ultra64"], "", False),
	s_code(0x80325DB0, 0x80325E58, "aisetnextbuf",          ["ultra64"], "", False),
	s_code(0x80325E60, 0x80326260, "timerintr",             ["ultra64"], "", False),
	s_code(0x80326260, 0x803273E4, "xprintf",               ["ultra64"], "", False),
	# s_code(0x803273F0, 0x80327484, "string",                ["ultra64"], "", False),
	s_code(0x80327490, 0x803274D0, "thread",                ["ultra64"], "", False),
	s_code(0x803274D0, 0x8032750C, "interrupt",             ["ultra64"], "", False),
	s_code(0x80327510, 0x80327634, "vi",                    ["ultra64"], "", False),
	s_code(0x80327640, 0x80327EB0, "exceptasm",             ["ultra64"], str_gp, False),
	s_code(0x80327EB0, 0x80327F2C, "virtualtophysical",     ["ultra64"], "", False),
	s_code(0x80327F30, 0x80327F3C, "spsetstat",             ["ultra64"], "", False),
	s_code(0x80327F40, 0x80327F74, "spsetpc",               ["ultra64"], "", False),
	s_code(0x80327F80, 0x8032800C, "sprawdma",              ["ultra64"], "", False),
	s_code(0x80328010, 0x8032803C, "sp",                    ["ultra64"], "", False),
	s_code(0x80328040, 0x8032804C, "spgetstat",             ["ultra64"], "", False),
	s_code(0x80328050, 0x80328068, "getthreadpri",          ["ultra64"], "", False),
	s_code(0x80328070, 0x8032807C, "vigetcurrcontext",      ["ultra64"], "", False),
	s_code(0x80328080, 0x803283DC, "viswapcontext",         ["ultra64"], "", False),
	s_code(0x803283E0, 0x803283EC, "getcount",              ["ultra64"], "", False),
	s_code(0x803283F0, 0x803284B0, "piacs",                 ["ultra64"], "", False),
	s_code(0x803284B0, 0x80328590, "pirawdma",              ["ultra64"], "", False),
	s_code(0x80328590, 0x80328704, "devmgr",                ["ultra64"], "", False),
	s_code(0x80328710, 0x80328720, "setsr",                 ["ultra64"], "", False),
	s_code(0x80328720, 0x8032872C, "getsr",                 ["ultra64"], "", False),
	s_code(0x80328730, 0x80328740, "setfpccsr",             ["ultra64"], "", False),
	s_code(0x80328740, 0x80328790, "sirawread",             ["ultra64"], "", False),
	s_code(0x80328790, 0x803287DC, "sirawwrite",            ["ultra64"], "", False),
	s_code(0x803287E0, 0x80328838, "maptlbrdb",             ["ultra64"], "", False),
	s_code(0x80328840, 0x80328894, "pirawread",             ["ultra64"], "", False),
	s_code(0x803288A0, 0x80328960, "siacs",                 ["ultra64"], "", False),
	s_code(0x80328960, 0x80328A0C, "sirawdma",              ["ultra64"], "", False),
	s_code(0x80328A10, 0x80328AE4, "settimer",              ["ultra64"], "", False),
	s_code(0x80328AF0, 0x80328FD0, "conteepwrite",          ["ultra64"], "", False),
	s_code(0x80328FD0, 0x80329120, "jammesg",               ["ultra64"], "", False),
	s_code(0x80329120, 0x80329148, "pigetcmdq",             ["ultra64"], "", False),
	s_code(0x80329150, 0x80329444, "conteepread",           ["ultra64"], "", False),
	s_code(0x80329450, 0x803296BC, "mtx",                   ["ultra64"], "", False),
	s_code(0x803296C0, 0x80329744, "normalize",             ["ultra64"], "", False),
	s_code(0x80329750, 0x80329780, "ai",                    ["ultra64"], "", False),
	s_code(0x80329780, 0x8032978C, "setcompare",            ["ultra64"], "", False),
	s_code(0x80329790, 0x80329A90, "xlitob",                ["ultra64"], "", False),
	s_code(0x80329A90, 0x8032A860, "xldtob",                ["ultra64"], str_fp, False),
	s_code(0x8032A860, 0x8032ACD4, "kdebugserver",          ["ultra64"], "", False),
	s_code(0x8032ACE0, 0x8032AE04, "syncputchars",          ["ultra64"], "", False),
	s_code(0x8032AE10, 0x8032AE70, "setintmask",            ["ultra64"], "", False),
	s_code(0x8032AE70, 0x8032AF68, "destroythread",         ["ultra64"], "", False),
	s_code(0x8032AF70, 0x8032B028, "probetlb",              ["ultra64"], "", False),
	s_code(0x8032B030, 0x8032B05C, "si",                    ["ultra64"], "", False),
	s_code(0x8032B060, 0x8032B1E4, "ldiv",                  ["ultra64"], "", False),
	s_code(0x8032B1F0, 0x8032B1FC, "getcause",              ["ultra64"], "", False),
	s_code(0x8032B200, 0x8032B258, "atomic",                ["ultra64"], "", False),
	s_data(0x80335010, 0x803358D0, 0x803397B0, 0x803397B0, 0, 0, "vitbl", ["ultra64", "$internal"], [
		[1, -28, ultra.c.d_OSViMode],
	], []),
	s_data(0x803358D0, 0x803358D0, 0x803397B0, 0x803397B0, 0x80364BA0, 0x80364C18, "seteventmesg.data", ["ultra64", "$internal"], [
	], []),
	s_data(0x803358D0, 0x803358D0, 0x803397B0, 0x803397B0, 0x80364C20, 0x80364C60, "sptask.data", ["ultra64", "$internal"], [
	], []),
	s_data(0x803358D0, 0x803358E8, 0x803397B0, 0x803397B0, 0x80364C60, 0x80365E6E, "vimgr.data", ["ultra64", "$internal"], [
		[1, 1, 1, ultra.c.d_str, 0x18, "0"],
	], []),
	s_data(0x803358F0, 0x80335908, 0x803397B0, 0x803397B0, 0x80365E70, 0x8036703C, "pimgr.data", ["ultra64", "$internal"], [
		[1, 1, 1, ultra.c.d_str, 0x18, "0"],
	], []),
	s_data(0x80335910, 0x8033591C, 0x803397B0, 0x803397B0, 0x80367040, 0x80367044, "initialize.data", ["ultra64", "$internal"], [
		[0, 1, 1, ultra.c.d_u64],
		[0, 1, 1, ultra.c.d_u32],
	], []),
	s_data(0x80335920, 0x80335924, 0x803397B0, 0x803397B0, 0x80367050, 0x803670D4, "controller.data", ["ultra64", "$internal"], [
		[0, 1, 1, ultra.c.d_u32],
	], []),
	s_data(0x80335930, 0x80335930, 0x803397B0, 0x803397B8, 0, 0, "perspective.data", ["ultra64", "$internal"], [], [
		[0, 1, 1, ultra.c.d_f64],
	]),
	s_data(0x80335930, 0x80335930, 0x803397C0, 0x803397D0, 0, 0, "llcvt.data", ["ultra64", "$internal"], [], [
		[0, 2, 1, ultra.c.d_u64, "0x%016X"],
	]),
	s_data(0x80335930, 0x80335930, 0x803397D0, 0x80339814, 0, 0, "cosf.data", ["ultra64", "$internal"], [], [
		[0, -5, 1, ultra.c.d_f64],
		[0,  3, 1, ultra.c.d_f64],
		[0,  1, 1, ultra.c.d_f32],
	]),
	s_data(0x80335930, 0x80335930, 0x80339820, 0x80339864, 0, 0, "sinf.data", ["ultra64", "$internal"], [], [
		[0, -5, 1, ultra.c.d_f64],
		[0,  3, 1, ultra.c.d_f64],
		[0,  1, 1, ultra.c.d_f32],
	]),
	s_data(0x80335930, 0x80335930, 0x80339870, 0x80339874, 0x803670E0, 0x803670E4, "rotate.data", ["ultra64", "$internal"], [], [
		[0, 1, 1, ultra.c.d_f32],
	]),
	s_data(0x80335930, 0x80335931, 0x80339880, 0x80339880, 0, 0, "aisetnextbuf.data", ["ultra64", "$internal"], [
		[0, 1, 1, ultra.c.d_u8],
	], []),
	s_data(0x80335940, 0x80335944, 0x80339880, 0x80339880, 0x803670F0, 0x80367124, "timerintr.data", ["ultra64", "$internal"], [
		[0, 1, 1, ultra.c.d_addr, ultra.A_ADDR],
	], []),
	s_data(0x80335950, 0x80335994, 0x80339880, 0x80339974, 0, 0, "xprintf.data", ["ultra64", "$internal"], [
		[0, 2, 36, "str"],
	], [
		[0, 1, 4, "str"],
		[0, 1, 8, "str"],
		[1, 1, 6, ultra.c.d_u32],
		[0, -52, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x803359A0, 0x803359B8, 0x80339980, 0x80339980, 0, 0, "thread.data", ["ultra64", "$internal"], [
		[0, 1, 1, ultra.c.d_OSThreadTail],
		[0, 4, 1, ultra.c.d_addr, ultra.A_ADDR|ultra.A_CAST, "OSThread *"],
	], []),
	s_data(0x803359C0, 0x80335A30, 0x80339980, 0x80339980, 0, 0, "vi.data", ["ultra64", "$internal"], [
		[1, 1, 1, ultra.c.d_str, 0x60, "0"],
		[0, 2, 1, ultra.c.d_addr, ultra.A_ADDR|ultra.A_ARRAY, 0x803359C0, 0x30],
		[0, 2, 1, ultra.c.d_u32],
	], []),
	[main.s_file, "exceptasm.sx"],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[ultra.asm.s_data, 0x80335A30, 0x80335A4C, "E0", [
			[5, 1, ultra.asm.d_uword],
			[2, 1, ultra.asm.d_uword],
		]],
		[main.s_str, "\n"],
		[main.s_str, str_rdata],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[ultra.asm.s_data, 0x80339980, 0x803399C4, "E0", [
			[4, 8, ultra.asm.d_ubyte, lambda x: "4*%d" % (x//4)],
			[9, 1, ultra.asm.d_waddr],
		]],
	[main.s_write],
	[main.s_file, "libm_vals.sx"],
		s_include(["ultra64"]),
		[main.s_str, "\n"],
		[main.s_str, str_rdata],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[ultra.asm.s_data, 0x803399D0, 0x803399D4, "E0", [
			[1, 1, ultra.asm.d_uword, "0x%08X"],
		]],
	[main.s_write],
	s_data(0x80335A50, 0x80335A54, 0x803399E0, 0x803399E0, 0x80367130, 0x80367150, "piacs.data", ["ultra64", "$internal"], [
		[0, 1, 1, ultra.c.d_u32],
	], []),
	s_data(0x80335A60, 0x80335A64, 0x803399E0, 0x803399E0, 0x80367150, 0x80367170, "siacs.data", ["ultra64", "$internal"], [
		[0, 1, 1, ultra.c.d_u32],
	], []),
	s_data(0x80335A70, 0x80335A70, 0x803399E0, 0x803399E0, 0x80367170, 0x803671B0, "conteepread.data", ["ultra64", "$internal"], [
	], []),
	s_data(0x80335A70, 0x80335A98, 0x803399E0, 0x803399E0, 0, 0, "xlitob.data", ["ultra64", "$internal"], [
		[0, 2, 20, "str"],
	], []),
	s_data(0x80335AA0, 0x80335AA0, 0x803399E0, 0x80339A40, 0, 0, "xldtob.data", ["ultra64", "$internal"], [], [
		[0, -9, 1, ultra.c.d_f64, "%.0E"],
		[0, 3, 4, "str"],
		[0, 1, 4, None],
		[0, 1, 1, ultra.c.d_f64],
	]),
	s_data(0x80335AA0, 0x80335AF0, 0x80339A40, 0x80339A40, 0, 0, "vimodentsclan1", ["ultra64", "$internal"], [
		[0, 1, ultra.c.d_OSViMode],
	], []),
	s_data(0x80335AF0, 0x80335B40, 0x80339A40, 0x80339A40, 0, 0, "vimodepallan1", ["ultra64", "$internal"], [
		[0, 1, ultra.c.d_OSViMode],
	], []),
	s_data(0x80335B40, 0x80335B4C, 0x80339A40, 0x80339A40, 0x803671B0, 0x80367460, "kdebugserver.data", ["ultra64", "$internal"], [
		[0, 3, 1, ultra.c.d_u32],
	], []),
	s_data(0x80335B50, 0x80335B58, 0x80339A40, 0x80339A40, 0, 0, "syncputchars.data", ["ultra64", "$internal"], [
		[0, 2, 1, ultra.c.d_u32],
	], []),
	[main.s_file, "setintmask.sx"],
		[main.s_str, "\n"],
		[main.s_str, str_rdata],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[ultra.asm.s_data, 0x80339A40, 0x80339AC0, "E0", [
			[8, 8, ultra.asm.d_uhalf, "0x%03X"],
		]],
	[main.s_write],
]

libultra_src_PR = [
	# [main.s_addr, 0xA4000040-0x00000040],
	# s_code(0xA4000040, 0xA4000B6C, "Boot", ["ultra64"], "", False),
	[main.s_addr, 0],
	[main.s_file, "romheader"],
		[ultra.asm.s_header, "E0"],
	[main.s_write],
	[main.s_bin, 0x00000B70, 0x00000FEE, "E0", ["font"]],
	[main.s_file, "rspboot.s"],
		[main.s_str, str_ucode_s_text % (
			"rspboot", "rspboot",
			"rspboot",
			"rspboot", "rspboot",
		)],
	[main.s_write],
	[main.s_file, "rspboot.asm"],
		[main.s_str, str_ucode],
		[main.s_str, str_ucode_create % ("rspboot.text", "0x04001000")],
		[main.s_addr, 0x04001000-0x000E6260],
		[ultra.asm.s_code, 0x04001000, 0x040010D0, "E0", 1, False, False],
		[main.s_str, "\n.align 8\n"],
		[main.s_str, str_ucode_close],
	[main.s_write],
	[main.s_file, "gspFast3D.fifo.s"],
		[main.s_str, str_gspFast3D_fifo],
	[main.s_write],
	[main.s_file, "gspFast3D.fifo.asm"],
	[main.s_dir, "gspFast3D"],
		[main.s_str, str_ucode],
		[main.s_str, ".include \"libultra/src/PR/gspFast3D/init.asm\"\n"],
		[main.s_file, "init.asm"],
			[main.s_str, str_ucode_create % ("gspFast3D.fifo.init", "0x04001080")],
			[main.s_str, "prg_init_start:\n\n"],
			[main.s_addr, 0x04001080-0x000E6330],
			[ultra.asm.s_code, 0x04001080, 0x04001088, "E0", 1, False, False],
			[main.s_str, str_ucode_close],
		[main.s_write],
		[main.s_str, ".include \"libultra/src/PR/gspFast3D/main.asm\"\n"],
		[main.s_file, "main.asm"],
			[main.s_str, str_ucode_create % ("gspFast3D.fifo.main", "0x04001000")],
			[main.s_str, "prg_main_start:\n\n"],
			[main.s_addr, 0x04001000-0x000E7290],
			[ultra.asm.s_code, 0x04001000, 0x04001088, "E0", 1, False, False],
			[main.s_addr, 0x04001080-0x000E6330],
			[ultra.asm.s_code, 0x04001088, 0x04001768, "E0", 1, False, False],
			[main.s_str, "\n.align 8\nprg_ext_start:\n\n"],
			[ultra.asm.s_code, 0x04001768, 0x0400188C, "E0", 1, False, False],
			[main.s_str, "\n.fill max(prg_clip_end, prg_light_end, prg_exit_end)-. + 0x10\n"],
			[ultra.asm.s_code, 0x04001998, 0x04001FDC, "E0", 1, False, False],
			[main.s_str, "\n.align 8\n"],
			[main.s_str, str_ucode_close],
		[main.s_write],
		[main.s_str, ".include \"libultra/src/PR/gspFast3D/clip.asm\"\n"],
		[main.s_file, "clip.asm"],
			[main.s_str, str_ucode_base % ("gspFast3D.fifo.clip", "prg_ext_start")],
			[main.s_addr, 0x04001768-0x000E7318],
			[ultra.asm.s_code, 0x04001768, 0x04001988, "E0", 1, False, False],
			[main.s_str, "\n.align 8\nprg_clip_end:\n"],
			[main.s_str, str_ucode_close],
		[main.s_write],
		[main.s_str, ".include \"libultra/src/PR/gspFast3D/light.asm\"\n"],
		[main.s_file, "light.asm"],
			[main.s_str, str_ucode_base % ("gspFast3D.fifo.light", "prg_ext_start")],
			[main.s_addr, 0x04001768-0x000E7538],
			[ultra.asm.s_code, 0x04001768, 0x040018FC, "E0", 1, False, False],
			[main.s_str, "\n.align 8\nprg_light_end:\n"],
			[main.s_str, str_ucode_close],
		[main.s_write],
		[main.s_str, ".include \"libultra/src/PR/gspFast3D/exit.asm\"\n"],
		[main.s_file, "exit.asm"],
			[main.s_str, str_ucode_base % ("gspFast3D.fifo.exit", "prg_ext_start")],
			[main.s_addr, 0x04001768-0x000E76D0],
			[ultra.asm.s_code, 0x04001768, 0x040017CC, "E0", 1, False, False],
			[main.s_str, "\n.align 8\nprg_exit_end:\n"],
			[main.s_str, str_ucode_close],
		[main.s_write],
		[main.s_str, ".include \"libultra/src/PR/gspFast3D/data.asm\"\n"],
		[main.s_file, "data.asm"],
			[main.s_str, str_ucode_create % ("gspFast3D.fifo.data", "0")],
			[main.s_addr, 0x00000000-0x000F4AC0],
			[ultra.asm.s_data, 0x00000000, 0x00000800, "E0", [
				[ 5, 1, asm.d_prg],
				[ 1, 4, ultra.asm.d_shalf],
				[ 1, 1, ultra.asm.d_align, 16],
				[ 1, 8, ultra.asm.d_shalf],
				[ 1, 8, ultra.asm.d_uhalf, "0x%04X"],
				[ 1, 8, ultra.asm.d_shalf],
				[ 1, 8, ultra.asm.d_shalf],
				[ 3, 8, ultra.asm.d_shalf], # clipping
				[ 1, 1, ultra.asm.d_addr], # vtx_light
				[ 1, 3, ultra.asm.d_uhalf, "0x%04X"], # arccos
				[ 1, 6, ultra.asm.d_uhalf, "0x%04X"],
				[ 1, 1, ultra.asm.d_shalf],
				[ 1, 1, ultra.asm.d_addr], # exit
				[ 1, 1, ultra.asm.d_uword, "0x%X"], # segment mask
				[ 4, 1, ultra.asm.d_addr], # cmd type
				[10, 1, ultra.asm.d_addr], # cmd DMA
				[15, 1, ultra.asm.d_addr], # cmd IMM
				[ 7, 1, ultra.asm.d_addr], # clip
				[ 1, 1, ultra.asm.d_addr], # cmd_next_sync
				[ 1, 1, ultra.asm.d_uhalf], # return
				[ 1, 1, ultra.asm.d_uword], # yield
				[ 1, 1, ultra.asm.d_uword], # rdphalf
				[ 1, 1, ultra.asm.d_align, 8], # state
				[ 1, 1, ultra.asm.d_ubyte], # dl no
				[ 1, 1, ultra.asm.d_align, 2],
				[ 1, 1, ultra.asm.d_uhalf, "0x%04X"], # perspnorm
				[ 1, 1, ultra.asm.d_align, 4],
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
				[ 1, 1, ultra.asm.d_align, 8],
				[ 1, 1, ultra.asm.d_uword], # output len
				[ 1, 1, ultra.asm.d_uword],
				[ 1, 1, ultra.asm.d_uhalf], # return
				[ 1, 1, ultra.asm.d_align, 4],
				[ 1, 1, ultra.asm.d_uword], # stack
				[16, 1, ultra.asm.d_uword], # segment table
				[ 1, 1, ultra.asm.d_align, 16],
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
				# L4-L7
				[ 1, 30, "asciz"],
				[ 1, 60, "ascii"],
				[ 1, 31, "ascii"],
				[ 1, 2, ultra.asm.d_ubyte],
				[ 1, 1, ultra.asm.d_uword],
				[15, 1, ultra.asm.d_uhalf, "0x%03X"], # movemem table
				[ 7, 1, ultra.asm.d_uhalf, "0x%03X"], # movemem table
				[ 1, 1, ultra.asm.d_align, 16],
				[ 1, 8, ultra.asm.d_shalf], # viewport
				[ 1, 3, ultra.asm.d_shalf], # fog
				[ 1, 10, ultra.asm.d_uword], # DL stack
				[ 1, 1, ultra.asm.d_align, 16],
			]],
			[main.s_str, "data_end:\n"],
			[main.s_str, "\n"],
			[main.s_str, ".if 0x800-orga() > 0\n"],
			[main.s_str, ".fill 0x800-orga()\n"],
			[main.s_str, ".endif\n"],
			[main.s_str, str_ucode_close],
		[main.s_write],
	[main.s_pop],
	[main.s_write],
	[main.s_file, "aspMain.s"],
		[main.s_str, str_ucode_s_text % (
			"aspMain", "aspMain",
			"aspMain",
			"aspMain", "aspMain",
		)],
		[main.s_str, str_ucode_s_data % (
			"aspMain", "aspMain",
			"aspMain",
			"aspMain", "aspMain",
		)],
	[main.s_write],
	[main.s_file, "aspMain.asm"],
		[main.s_str, str_ucode],
		[main.s_str, str_ucode_create % ("aspMain.text", "0x04001080")],
		[main.s_addr, 0x04001080-0x000E7740],
		[ultra.asm.s_code, 0x04001080, 0x04001E9C, "E0", 1, False, False],
		[main.s_str, "\n.align 8\n"],
		[main.s_str, str_ucode_close],
		[main.s_str, str_ucode_create % ("aspMain.data", "0")],
		[main.s_addr, 0x00000000-0x000F52C0],
		[ultra.asm.s_data, 0x00000000, 0x000002C0, "E0", [
			[(0x10)//0x10, 4, ultra.asm.d_uword, "0x%08X"],
			[16, 1, ultra.asm.d_addr],
			[(0x2C0-0x30)//0x10, 4, ultra.asm.d_uword, "0x%08X"],
		]],
		[main.s_str, "\n.align 8\n"],
		[main.s_str, str_ucode_close],
	[main.s_write],
]

include_code = [
	s_header("buffer", [
		[ultra.c.s_extern, 0x80200200, 0x80220DA0, "E0", 0x8032D560],
	]),
	s_header("main", [
		[main.s_str, header.str_main],
		[main.s_str, "\n"],
		[ultra.c.s_struct, header.struct_main],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x8033A580, 0x8033AF90, "E0", 0x8032D560],
		[ultra.c.s_extern, 0x8032D560, 0x8032D5C4, "E0", None],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x80246050, 0x80246E68, "E0", None],
	]),
	s_header("graphics", [
		[main.s_str, header.str_graphics],
		[main.s_str, "\n"],
		[ultra.c.s_struct, header.struct_graphics],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x8038F800, 0x80400000, "E0", 0x8032D560],
		[ultra.c.s_extern, 0x80000400, 0x80025C00, "E0", 0x8032D560],
		[ultra.c.s_extern, 0x80227000, 0x80246000, "E0", 0x8032D560],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x8033AF90, 0x8033B09C, "E0", 0x8032D5D0],
		[ultra.c.s_extern, 0x8032D5D0, 0x8032D5FC, "E0", None],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x80246E70, 0x80248C3C, "E0", None],
	]),
	s_header("audio", [
		[ultra.c.s_extern, 0x8033B0A0, 0x8033B170, "E0", 0x8032D600],
		[ultra.c.s_extern, 0x8032D600, 0x8032D6C1, "E0", None],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x80248C40, 0x802495DC, "E0", None],
	]),
	s_header("game", [
		[ultra.c.s_struct, header.struct_game],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x8033B170, 0x8033B26F, "E0", 0x8032D6D0],
		[ultra.c.s_extern, 0x8032D6D0, 0x8032D948, "E0", None],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x802495E0, 0x8024BFE4, "E0", None],
	]),
	s_header("collision", [
		[ultra.c.s_struct, header.struct_collision],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x8033B270, 0x8033B274, "E0", 0x8032D950],
		[ultra.c.s_extern, 0x8032D950, 0x8032DA9C, "E0", None],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x8024BFF0, 0x8025093C, "E0", None],
	]),
	s_header("player", [
		[ultra.c.s_struct, header.struct_player],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x8033B280, 0x8033B400, "E0", 0x8032DAA0],
		[ultra.c.s_extern, 0x8032DAA0, 0x8032DD6A, "E0", None],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x80250940, 0x80277ED4, "E0", None],
	]),
	s_header("memory", [
		[main.s_str, header.str_memory],
		[main.s_str, "\n"],
		[ultra.c.s_struct, header.struct_memory],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x801C1000, 0x801CE000, "E0", 0x8032D560],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x8033B400, 0x8033B498, "E0", 0x8032DD70],
		[ultra.c.s_extern, 0x8032DD70, 0x8032DD74, "E0", None],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x80277EE0, 0x80279158, "E0", None],
		[ultra.c.s_extern, 0x8027F4E0, 0x8027F584, "E0", None],
	]),
	s_header("save", [
		[main.s_str, header.str_save],
		[main.s_str, "\n"],
		[ultra.c.s_struct, header.struct_save],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x8033B4A0, 0x8033B4A7, "E0", 0x8032DD80],
		[ultra.c.s_extern, 0x8032DD80, 0x8032DDBE, "E0", None],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x80279160, 0x8027A7C4, "E0", None],
	]),
	s_header_code(0x8027A7D0, 0x8027B6C0, 0x8032DDC0, 0x8032DE70, 0x8033B4B0, 0x8033BAE0, "scene", header.struct_scene, header.str_scene),
	s_header_code(0x8027B6C0, 0x8027E3DC, 0x8032DE70, 0x8032DF0C, 0x8033BAE0, 0x8033C38C, "draw"),
	s_header_code(0x8027E3E0, 0x8027F4D4, 0x8032DF10, 0x8032DF1C, 0x8033C390, 0x8033C520, "time", header.struct_time, header.str_time),
	s_header_code(0x8027F590, 0x8029C764, 0x8032DF20, 0x8032FEB4, 0x8033C520, 0x8033CBE0, "camera", header.struct_camera), # end is wrong
	s_header("object", [
		[main.s_str, header.str_object],
		[main.s_str, "\n"],
		[ultra.c.s_struct, header.struct_object],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x8033CBE0, 0x80361274, "E0", 0x8032FEC0],
		[ultra.c.s_extern, 0x80361290, 0x803612AC, "E0", 0x80330E20],
		[ultra.c.s_extern, 0x8032FEC0, 0x80330018, "E0", None],
		[ultra.c.s_extern, 0x80330E20, 0x80330EB2, "E0", None],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x8029C780, 0x802A5618, "E0", None],
		[ultra.c.s_extern, 0x802C89F0, 0x802CB5B4, "E0", None],
	]),
	s_header_code(0x802A5620, 0x802C89F0, 0x80330020, 0x80330E1C, 0x80361280, 0x80361282, "object_a", header.struct_object_a),
	s_header_code(0x802CB5C0, 0x802CD27C, 0x80330EC0, 0x80330ED8,          0,          0, "wipe", header.struct_wipe),
	s_header_code(0x802CD280, 0x802CF5A4, 0x80330EE0, 0x80330EF8, 0x803612B0, 0x803612B6, "shadow", header.struct_shadow),
	s_header_code(0x802CF5B0, 0x802D007C, 0x80330F00, 0x80330F2E, 0x803612C0, 0x803612E0, "back", header.struct_back),
	s_header_code(0x802D0080, 0x802D2208, 0x80330F30, 0x803312F0, 0x803612E0, 0x803612E2, "scroll", header.struct_scroll),
	s_header_code(0x802D2210, 0x802D29BC, 0x803312F0, 0x803312FC, 0x803612F0, 0x803612F1, "obj_shape"),
	s_header_code(0x802D29C0, 0x802D5E00, 0x80331300, 0x80331360, 0x80361300, 0x8036131D, "wave", header.struct_wave),
	s_header_code(0x802D5E00, 0x802D6F18, 0x80331360, 0x80331364, 0x80361320, 0x803613F0, "dprint", header.struct_dprint),
	s_header_code(0x802D6F20, 0x802DDDEC, 0x80331370, 0x8033174C, 0x803613F0, 0x803613FF, "message", header.struct_message),
	s_header_code(0x802DDDF0, 0x802E2094, 0x80331750, 0x803317D8, 0x80361400, 0x80361440, "weather", header.struct_weather),
	s_header_code(0x802E20A0, 0x802E2CF0, 0x803317E0, 0x803325E8,          0,          0, "tag", header.struct_tag, header.str_tag),
	s_header_code(0x802E2CF0, 0x802E3E50, 0x803325F0, 0x8033260C, 0x80361440, 0x80361442, "hud", header.struct_hud, header.str_hud),
	s_header_code(0x802E3E50, 0x802F972C, 0x80332610, 0x8033283C, 0x80361450, 0x80361454, "object_b", header.struct_object_b),
	s_header_code(0x802F9730, 0x80314A2C, 0x80332840, 0x80332E4C, 0x80361460, 0x8036148C, "object_c", header.struct_object_c),
]

include_ulib = [
	s_header_code(0x80378800, 0x8037B21C, 0x80385F90, 0x8038B802, 0x8038BC90, 0x8038BC9C, "math", header.struct_math, header.str_math),
	s_header("shape", [
			[main.s_str, header.str_shape],
			[main.s_str, "\n"],
			[ultra.c.s_struct, header.struct_shape],
			[main.s_str, "\n"],
			[main.s_str, "typedef void *SHPCALL(int code, SHAPE *shape, void *data);\n"],
			[main.s_str, "\n"],
			[ultra.c.s_struct, header.struct_shp],
			[main.s_str, "\n"],
			[ultra.c.s_extern, 0x8038B810, 0x8038B810, "E0", None],
			[main.s_str, "\n"],
			[ultra.c.s_extern, 0x8037B220, 0x8037CB60, "E0", None],
	]),
	s_header_code(0x80380690, 0x80383B6C, 0x8038B9B0, 0x8038B9B0, 0x8038BE30, 0x8038EED4, "map", header.struct_map, header.str_map),
	s_header("script", [
		[ultra.c.s_extern, 0x8038BCA0, 0x8038BE2C, "E0", 0x8038B810],
		[ultra.c.s_extern, 0x8038EEE0, 0x8038EEE2, "E0", 0x8038B9B0],
		[ultra.c.s_extern, 0x8038B810, 0x8038B9AC, "E0", None],
		[ultra.c.s_extern, 0x8038B9B0, 0x8038BA90, "E0", None],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x8037CB60, 0x80380684, "E0", None],
		[ultra.c.s_extern, 0x80383B70, 0x80385F88, "E0", None],
	]),
]

include_menu = [
	s_header_code(0x8016F000, 0x8016F670, 0x801A7830, 0x801A7C3C,          0,          0, "title"),
	s_header_code(0x8016F670, 0x80170280, 0x801A7C70, 0x801A7D10, 0x801B99E0, 0x801B99F0, "titlebg"),
	s_header_code(0x80170280, 0x801768E0, 0x801A7D10, 0x801A7F3E, 0x801B99F0, 0x801B9A7A, "fileselect", header.struct_fileselect),
	s_header_code(0x801768E0, 0x80177710, 0x801A81A0, 0x801A81B6, 0x801B9A80, 0x801B9AA4, "starselect", header.struct_starselect),
]

include_audio = [
	s_header("Na", [
		[main.s_str, header.str_Na],
		[main.s_str, "\n"],
		[ultra.c.s_struct, header.struct_Na],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x801CE000, 0x80200200, "E0", 0x8032D560],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0, 0, "E0", 0x80332E50],
		[ultra.c.s_extern, 0x80332E50, 0x80335010, "E0", None],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x80314A30, 0x80322364, "E0", None],
	]),
]

include_face = [
	s_header("face", [
		[ultra.c.s_struct, header.struct_face],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0, 0, "E0", 0x801A81E0],
		[ultra.c.s_extern, 0x801A81E0, 0x801A81E0, "E0", None],
		[main.s_str, "\n"],
		[ultra.c.s_extern, 0x80177710, 0x801A7830, "E0", None],
	]),
]

src_code = [
	# s_code(0x80246050, 0x80246E68, "main"),
	# s_code(0x80246E70, 0x80248C3C, "graphics"),
	# s_code(0x80248C40, 0x802495DC, "audio"),
	s_code(0x802495E0, 0x8024BFE4, "game"),
	s_code(0x8024BFF0, 0x8025093C, "collision"),
	s_code(0x80250940, 0x8025507C, "player"),
	s_code(0x80255080, 0x80256DFC, "plphysics"),
	s_code(0x80256E00, 0x8025DD68, "pldemo"),
	s_code(0x8025DD70, 0x802608AC, "plhang"),
	s_code(0x802608B0, 0x80263E5C, "plwait"),
	s_code(0x80263E60, 0x80269F38, "plwalk", [], str_fp),
	s_code(0x80269F40, 0x80270104, "pljump"),
	s_code(0x80270110, 0x80274EAC, "plswim"),
	s_code(0x80274EB0, 0x802761D0, "plgrab"),
	# s_code(0x802761D0, 0x80277ED4, "plcallback"),
	# s_code(0x80277EE0, 0x80279158, "memory"),
	# s_code(0x80279160, 0x8027A7C4, "save"),
	# s_code(0x8027A7D0, 0x8027B6C0, "scene"),
	# s_code(0x8027B6C0, 0x8027E3DC, "draw"),
	# s_code(0x8027E3E0, 0x8027F4D4, "time"),
	# s_code(0x8027F4E0, 0x8027F584, "slidec"),

	s_code(0x8027F590, 0x8029C764, "camera"),

	# s_code(0x8029C770, 0x8029C780, "course"),
	s_code(0x8029C780, 0x8029D884, "object", [], str_fp),
	s_code(0x8029D890, 0x802A5618, "objlib", [], str_fp),
	s_code(0x802A5620, 0x802C89F0, "object_a", [], str_fp),
	# s_code(0x802C89F0, 0x802C8F40, "objphysics"),
	s_code(0x802C8F40, 0x802C97C8, "objcollision"),
	# s_code(0x802C97D0, 0x802CA03C, "objlist"),
	# s_code(0x802CA040, 0x802CA370, "objsfx"),
	s_code(0x802CA370, 0x802CB5B4, "objdebug"),

	s_code(0x802CB5C0, 0x802CD27C, "wipe", [], str_fp),
	s_code(0x802CD280, 0x802CF5A4, "shadow", [], str_fp),
	s_code(0x802CF5B0, 0x802D007C, "back", [], str_fp),
	s_code(0x802D0080, 0x802D2208, "scroll", [], str_fp),
	# s_code(0x802D2210, 0x802D29BC, "obj_shape", [], str_fp),
	s_code(0x802D29C0, 0x802D5E00, "wave", [], str_fp),

	# s_code(0x802D5E00, 0x802D6F18, "dprint"),
	s_code(0x802D6F20, 0x802DDDEC, "message", [], str_fp),
	s_code(0x802DDDF0, 0x802DFD50, "snow"),
	s_code(0x802DFD50, 0x802E2094, "lava"),
	# s_code(0x802E20A0, 0x802E2CF0, "tag"),
	# s_code(0x802E2CF0, 0x802E3E50, "hud"),
	s_code(0x802E3E50, 0x802F972C, "object_b", [], str_fp),

	s_code(0x802F9730, 0x80314A2C, "object_c"),

	# s_data(0x8032D560, 0x8032D5C4, 0x80335B60, 0x80335B74, 0x8033A580, 0x8033AF90, "main.data", ["sm64"], [
	# 	[0,   7, 1, ultra.c.d_addr, 0],
	# 	[0,   1, ultra.c.d_bool_s8],
	# 	[0,   1, 1, ultra.c.d_u32],
	# 	[0,   2, ultra.c.d_align_s8],
	# 	[0,   4, ultra.c.d_bool_s8],
	# 	[0, -16, 1, ultra.c.d_flag16, ultra.flag_button],
	# 	[0,   2, ultra.c.d_align_s16],
	# ], [
	# 	[0, -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
	# ]),
	# s_data(0x8032D5D0, 0x8032D5FC, 0x80335B80, 0x80335B88, 0x8033AF90, 0x8033B09C, "graphics.data", ["sm64"], [
	# 	[0, 2, 1, ultra.c.d_u32],
	# 	[0, 2, ultra.c.d_align_u16],
	# 	[0, 1, 1, ultra.c.d_addr, 0],
	# 	[0, 3, 1, ultra.c.d_addr, ultra.A_ADDR|ultra.A_ARRAY, 0x8033AF90, 0x1C],
	# 	[0, 1, 1, ultra.c.d_addr, 0],
	# 	[0, 1, ultra.c.d_align_u16],
	# 	[1, 1, 1, ultra.c.d_str, 4, "0"],
	# ], [
	# 	[0, 1, 8, "str"],
	# ]),
	# s_data(0x8032D600, 0x8032D6C4, 0x80335B90, 0x80335B94, 0x8033B0A0, 0x8033B170, "audio.data", ["sm64"], [
	# 	[0,  1, ultra.c.d_align_u8],
	# 	[0,  1, ultra.c.d_bool_u8],
	# 	[0,  3, ultra.c.d_align_s16],
	# 	[0,  1, ultra.c.d_bool_u8],
	# 	[1,  1, 1, ultra.c.d_str, 0x10, "0"],
	# 	[1,  1, 3, ultra.c.d_s16],
	# 	[0,  1, 2, None],
	# 	[0, -9, 4, ultra.c.d_u32, "0x%08X"],
	# 	[0,  1, ultra.c.d_bool_u8],
	# ], [
	# 	[0, 1, 1, ultra.c.d_f32],
	# ]),
	s_data(0x8032D6D0, 0x8032D948, 0x80335BA0, 0x803361A8, 0x8033B170, 0x8033B26F, "game.data", ["sm64"], [
		[1, 1, 2, ultra.c.d_addr, 0],
		[1, 1, 3, ultra.c.d_addr, 0],
		[1, 1, 3, ultra.c.d_addr, 0],
		[1, 1, 4, ultra.c.d_addr, 0],
		[1, 1, 4, ultra.c.d_addr, 0],
		[1, 1, 3, ultra.c.d_addr, 0],
		[1, 1, 3, ultra.c.d_addr, 0],
		[1, 1, 4, ultra.c.d_addr, 0],
		[1, 1, 2, ultra.c.d_addr, 0],
		[1, 1, 4, ultra.c.d_addr, 0],
		[1, 1, 3, ultra.c.d_addr, 0],
		[1, 1, 2, ultra.c.d_addr, 0],
		[1, 1, 4, ultra.c.d_addr, 0],
		[1, 1, 2, ultra.c.d_addr, 0],
		[1, 1, 3, ultra.c.d_addr, 0],
		[1, 1, 5, ultra.c.d_addr, 0],
		[1, 1, 4, ultra.c.d_addr, 0],
		[1, 1, 4, ultra.c.d_addr, 0],
		[1, 1, 2, ultra.c.d_addr, 0],
		[1, 1, 2, ultra.c.d_addr, 0],
		[0, -23, 1, c.d_staff],
		[0, 1, 1, ultra.c.d_addr, ultra.A_ADDR|ultra.A_ARRAY, 0x8033B170, 0xC8],
		[0, 1, ultra.c.d_align_s16],
		[0, 1, ultra.c.d_align_s8],
	], [
		[0, 1, 16, "str"],
		[0, 1, 20, "str"],
		[0, 1, 24, "str"],
		[0, 1, 20, "str"],
		[0, 1, 16, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 20, "str"],
		[0, 1, 24, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 20, "str"],
		[0, 1, 16, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 20, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 20, "str"],
		[0, 1, 16, "str"],
		[0, 1, 24, "str"],
		[0, 1, 16, "str"],
		[0, 1, 20, "str"],
		[0, 1, 16, "str"],
		[0, 1, 20, "str"],
		[0, 1, 12, "str"],
		[0, 1, 20, "str"],
		[0, 1, 24, "str"],
		[0, 1, 24, "str"],
		[0, 1, 16, "str"],
		[0, 1, 12, "str"],
		[0, 1, 20, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 12, "str"],
		[0, 1, 20, "str"],
		[0, 1, 12, "str"],
		[0, 1, 20, "str"],
		[0, 1, 12, "str"],
		[0, 1, 24, "str"],
		[0, 1, 20, "str"],
		[0, 1, 12, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, -112, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x8032D950, 0x8032DA9C, 0x803361B0, 0x8033641C, 0x8033B270, 0x8033B274, "collision.data", ["sm64"], [
		[0, -31, 1, c.d_collision],
		[0, -18, 1, ultra.c.d_u32, "0x%08X"],
		[0, 3, ultra.c.d_bool_u8],
	], [
		[0, -152, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0, 3, 1, ultra.c.d_f32],
	]),
	s_data(0x8032DAA0, 0x8032DAE8, 0x80336420, 0x8033666C, 0x8033B280, 0x8033B284, "player.data", ["sm64"], [
		[1, -7, 6, ultra.c.d_s8],
		[0, 1, 2, None],
		[0, -4, 4, ultra.c.d_u8],
		[0, 1, 4, None],
		[0, 1, 1, ultra.c.d_u64, "0x%016X"], # bin
	], [
		[0,   1, 8, "str"],
		[0,   1, 8, "str"],
		[0,   1, 8, "str"],
		[0, -90, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  13, 1, ultra.c.d_f32],
		[0, -33, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   5, 1, ultra.c.d_f32],
	]),
	s_data(0x8032DAF0, 0x8032DB28, 0x80336670, 0x803366C4, 0x8033B290, 0x8033B294, "plphysics.data", ["sm64"], [
		[1, 1, 3, ultra.c.d_s16], [0, 1, 2, None],
		[0, 1, c.d_bgface],
	], [
		[0,   2, 1, ultra.c.d_f32],
		[0, -13, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   6, 1, ultra.c.d_f32],
	]),
	s_data(0x8032DB30, 0x8032DC50, 0x803366D0, 0x80336940, 0x8033B2A0, 0x8033B2C0, "pldemo.data", ["sm64"], [
		[0,   1, 1, ultra.c.d_Vp],
		[0,   1, 1, ultra.c.d_addr, 0],
		[0,   2, ultra.c.d_align_s8],
		[1,   1, 7, ultra.c.d_s8],
		[0,   1, 1, None],
		[1,   1, 6, ultra.c.d_u8],
		[0,   1, 2, None],
		[0, -27, 1, c.d_bspline],
		[0,   2, 1, ultra.c.d_s32],
		[0, -10, 2, ultra.c.d_u8],
	], [
		[0,    1, 1, ultra.c.d_f32],
		[0,   -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    1, 1, ultra.c.d_f32],
		[0,   -7, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    6, 1, ultra.c.d_f32],
		[0, -136, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x8032DC50, 0x8032DC50, 0x80336940, 0x80336964, 0, 0, "plhang.data", ["sm64"], [], [
		[0,  4, 1, ultra.c.d_f32],
		[0, -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x8032DC50, 0x8032DC50, 0x80336970, 0x80336A74, 0, 0, "plwait.data", ["sm64"], [], [
		[0,   2, 1, ultra.c.d_f32],
		[0, -63, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x8032DC50, 0x8032DD28, 0x80336A80, 0x80336BF4, 0x8033B2C0, 0x8033B340, "plwalk.data", ["sm64"], [
		[0, 9, c.d_pl_walk],
	], [
		[0,  29, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   3, 1, ultra.c.d_f32],
		[0, -58, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x8032DD30, 0x8032DD30, 0x80336C00, 0x80336E0C, 0, 0, "pljump.data", ["sm64"], [], [
		[0,    7, 1, ultra.c.d_f32],
		[0,   -7, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    8, 1, ultra.c.d_f32],
		[0,    1, 1, ultra.c.d_f64],
		[0, -107, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x8032DD30, 0x8032DD40, 0x80336E10, 0x80336ECC, 0x8033B340, 0x8033B348, "plswim.data", ["sm64"], [
		[0, 2, ultra.c.d_align_s16],
		[1, 1, 4, ultra.c.d_s16],
	], [
		[0,   1, 1, ultra.c.d_f32],
		[0, -12, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   6, 1, ultra.c.d_f32],
		[0, -28, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x8032DD40, 0x8032DD48, 0x80336ED0, 0x80336F38, 0, 0, "plgrab.data", ["sm64"], [
		[1, 1, 8, ultra.c.d_s8],
	], [
		[0, -26, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	# s_data(0x8032DD50, 0x8032DD6A, 0x80336F40, 0x80336F70, 0x8033B350, 0x8033B400, "plcallback.data", ["sm64"], [
	# 	[1,  1, 8, ultra.c.d_s8],
	# 	[0, -3, 6, ultra.c.d_s8], [0, 1, 2, None],
	# 	[0,  1, ultra.c.d_align_s16],
	# ], [
	# 	[0, -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
	# 	[0,  2, 1, ultra.c.d_f32], [0, 1, 4, None],
	# 	[0,  2, 1, ultra.c.d_f64],
	# ]),
	# s_data(0x8032DD70, 0x8032DD74, 0x80336F70, 0x80336F70, 0x8033B400, 0x8033B498, "memory.data", ["sm64"], [
	# 	[0, 1, 1, ultra.c.d_addr, 0],
	# ], []),
	# s_data(0x8032DD80, 0x8032DDBE, 0x80336F70, 0x80336F70, 0x8033B4A0, 0x8033B4A7, "save.data", ["sm64"], [
	# 	[0, 6, ultra.c.d_align_u8],
	# 	[0, -38, 1, ultra.c.d_u8],
	# ], []),
	# s_data(0x8032DDC0, 0x8032DE70, 0x80336F70, 0x80336F90, 0x8033B4B0, 0x8033BAE0, "scene.data", ["sm64"], [
	# 	[0, 7, 1, ultra.c.d_addr, 0],
	# 	[0, 1, ultra.c.d_align_s16],
	# 	[0, 1, 1, ultra.c.d_u32],
	# 	[0, 1, 1, ultra.c.d_u32],
	# 	[0, 3, ultra.c.d_align_u8],
	# 	[0, 2, ultra.c.d_align_s16],
	# 	[0, -20, 1, ultra.c.d_addr, ultra.A_EXTERN],
	# 	[0, -20, 1, ultra.c.d_u8],
	# 	[0, 1, 1, ultra.c.d_Vp],
	# ], [
	# 	[0, 1, 16, "str"],
	# 	[0, 1,  8, "str"],
	# 	[0, 1,  8, "str"],
	# ]),
	# s_data(0x8032DE70, 0x8032DF0C, 0x80336F90, 0x803370EC, 0x8033BAE0, 0x8033C38C, "draw.data", ["sm64"], [
	# 	[1, -4, [[0, -8, 1, c.d_rendermode]]],
	# 	[0, 6, 1, ultra.c.d_addr, 0],
	# 	[0, 1, ultra.c.d_align_u16],
	# ], [
	# 	[0, 1, 8, "str"],
	# 	[0, 1, 1, ultra.c.d_f32],
	# 	[0, -84, 1, ultra.c.d_addr, ultra.A_EXTERN],
	# ]),
	# s_data(0x8032DF10, 0x8032DF1C, 0x803370F0, 0x803370F0, 0x8033C390, 0x8033C520, "time.data", ["sm64"], [
	# 	[0, 3, ultra.c.d_align_s16],
	# ], []),
	s_data(0x8032DF20, 0x8032FEB4, 0x803370F0, 0x80337794, 0, 0, "camera.data", ["sm64"], [
		[0,    1, 1, ultra.c.d_s32],
		[0,    1, 1, ultra.c.d_addr, 0],
		[0,    2, 1, ultra.c.d_s32],
		[0,    1, 1, ultra.c.d_addr, 0],
		[0,    1, 1, ultra.c.d_s16, "0x%04X"], [0, 1, 2, None],
		[0,    2, 1, ultra.c.d_s32],
		[0,    4, 1, ultra.c.d_f32],
		[0,    4, ultra.c.d_align_u8],
		[0,    2, 1, ultra.c.d_addr, ultra.A_ADDR|ultra.A_ARRAY, 0x8033C520, 0x24],
		[0,    1, 1, ultra.c.d_s32],
		[1,    5, 3, ultra.c.d_f32],
		[0,  -18, 1, ultra.c.d_addr, 0],
		[1,    2, 3, ultra.c.d_f32],
		[1,    1, 7, ultra.c.d_u16], [0, 1, 2, None],
		[1,    1, 5, ultra.c.d_u8], [0, 1, 3, None],
		[0,   -4, 1, c.d_campos],
		[0, -130, 1, c.d_camctl],
		[0,  -40, 1, ultra.c.d_addr, 0],
		[0, -148, 1, c.d_campath],
		[1,    3, 3, ultra.c.d_f32],
		[0,  -88, 1, c.d_campath],
		[0, -102, 1, c.d_camdemo],
		[0, -27, 1, c.d_camera_windemo],
		[0, -19, 1, c.d_camera_pause],
		[0, 1, 1, None],
		[0, -198, 1, c.d_campath],
	], [
		[0,  -10, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    2, 1, ultra.c.d_f32],
		[0,  -10, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   52, 1, ultra.c.d_f32],
		[0,  -17, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    4, 1, ultra.c.d_f32],
		[0,  -29, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    9, 1, ultra.c.d_f32],
		[0,   -6, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    8, 1, ultra.c.d_f32],
		[0,  -11, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   54, 1, ultra.c.d_f32],
		[0, -129, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    9, 1, ultra.c.d_f32],
		[0,  -65, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,    5, 1, ultra.c.d_f32],
		[0,   -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
	], str_camera_data),
	s_data(0x8032FEC0, 0x8032FFFC, 0x803377A0, 0x803377B0, 0x8033CBE0, 0x80361266, "object.data", ["sm64"], [
		[0, -10, 1, ultra.c.d_s8, table.fmt_o_type],
		[0,  -1, 1, ultra.c.d_s8],
		[0,   1, 1, None],
		[0, -19, 1, c.d_pl_pcl],
	], [
		[0, 2, 1, ultra.c.d_f64],
	]),
	s_data(0x80330000, 0x80330018, 0x803377B0, 0x80337848, 0x80361270, 0x80361274, "objlib.data", ["sm64"], [
		[1, 1, 4, ultra.c.d_s8],
		[1, 1, 8, ultra.c.d_s16, "0x%02X"],
		[1, 1, 4, ultra.c.d_s8],
	], [
		[0,  1, 12, "str"],
		[0,  6, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,  3, 1, ultra.c.d_f64],
		[0,  2, 1, ultra.c.d_f32],
		[0,  1, 1, ultra.c.d_f64],
		[0,  1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,  1, 1, ultra.c.d_f64],
		[0,  9, 1, ultra.c.d_f32],
		[0, -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x80330020, 0x80330E1C, 0x80337850, 0x80337DF0, 0x80361280, 0x80361282, "object_a.data", ["sm64"], [
		[0,  -3, 1, ultra.c.d_u32, "0x%08X"], # T:flag(save)
		[0,  -8, 4, ultra.c.d_s16, ultra.fmt_s16],
		[0,  -6, 1, ultra.c.d_addr, 0],
		[0,   1, 1, c.d_obj_col],
		[0,   1, 1, c.d_obj_pcl],
		[0,  -3, 1, ultra.c.d_u8, table.fmt_msg], [0, 1, 1, None],
		[0, -13, 1, ultra.c.d_addr, 0],
		[0, -12, 1, c.d_obj_sfx],
		[0,  -7, 1, ultra.c.d_addr, 0],
		[0,  -5, 1, c.d_object_a_0],
		[0,  -4, 1, ultra.c.d_addr, 0],
		[0,  -2, 1, c.d_object_a_1],
		[0,   1, 1, c.d_obj_col],
		[0,   1, 1, c.d_obj_pcl],
		[0,   2, 1, c.d_obj_col],
		[1,  -8, 2, ultra.c.d_s16],
		[0,  -2, 1, ultra.c.d_addr, 0],
		[1, -13, 2, ultra.c.d_s16],
		[0,  -5, 1, c.d_80330260],
		[0,  -4, 1, ultra.c.d_u32, UNSM.table.fmt_na_se],
		[0,  -5, 1, ultra.c.d_addr, 0],
		[0,  -4, 1, c.d_object_a_2],
		[0,  -4, 1, ultra.c.d_addr, 0],
		[1,  -7, 3, ultra.c.d_s16], [0, 1, 2, None],
		[0,  -5, 1, ultra.c.d_addr, 0],
		[0,   2, 1, c.d_obj_pcl],
		[1,   1, 4, ultra.c.d_s16],
		[0,   1, 1, c.d_obj_pcl],
		[0,  -4, 1, ultra.c.d_addr, 0],
		[1,   1, 4, ultra.c.d_f32, "%.1f"],
		[0,   3, 1, c.d_obj_col],
		[1, -10, 2, ultra.c.d_s16],
		[0,  -4, 1, ultra.c.d_addr, 0],
		[0,   1, 1, c.d_obj_col],
		[0,  -2, 1, ultra.c.d_addr, 0],
		[0,   1, 1, c.d_obj_col],
		[0,  -3, 1, ultra.c.d_addr, 0],
		[0,   1, 1, c.d_obj_col],
		[0,  -8, 1, ultra.c.d_addr, 0],
		[1,   1, 16, ultra.c.d_s8],
		[1,   1, 1, ultra.c.d_s16], [0, 1, 2, None],
		[1,   1, 1, ultra.c.d_s16], [0, 1, 2, None],
		[1,   1, 4, ultra.c.d_s8],
		[0,  -3, 1, ultra.c.d_s16, table.fmt_msg], [0, 1, 2, None],
		[1, -12, 3, ultra.c.d_s16],
		[0, -20, 1, ultra.c.d_addr, 0],
		[0, -27, 1, c.d_obj_sfx],
		[1,   1, 3, ultra.c.d_s8], [0, 1, 1, None],
		[1,   1, 3, ultra.c.d_s8], [0, 1, 1, None],
		[0, -11, 1, c.d_object_a_3],
		[0,  -3, 1, ultra.c.d_addr, 0],
		[0,   2, 1, c.d_obj_col],
		[1,   1, 3, ultra.c.d_f32],
		[0,  -2, 1, c.d_object_a_4],
		[0,   1, 1, c.d_path_data],
		[0, -13, 1, c.d_obj_sfx],
		[0,  -8, 1, ultra.c.d_addr, 0],
		[0,  -6, 4, ultra.c.d_s16], [0, -1, 1, ultra.c.d_s16], [0, 1, 2, None],
		[0,  -6, 4, ultra.c.d_s16], [0, -1, 1, ultra.c.d_s16], [0, 1, 2, None],
		[0,  -6, 1, ultra.c.d_addr, 0],
		[0,   1, 1, c.d_obj_col],
		[0,  -3, 16, ultra.c.d_s8], [0, -1, 4, ultra.c.d_s8],
		[0,  -2, 16, ultra.c.d_s8], [0, -1, 3, ultra.c.d_s8], [0, 1, 1, None],
		[0,  -2, 16, ultra.c.d_s8], [0, -1, 4, ultra.c.d_s8],
		[0, -11, 1, ultra.c.d_addr, 0],
		[1,   1, 5, ultra.c.d_s8], [0, 1, 3, None],
		[0,  -9, 1, ultra.c.d_addr, 0],
		# todo: proper fmt
		[0,  14, [
			[0, -2, 13, ultra.c.d_s8],
			[0, -1, 1, ultra.c.d_s8], [0, 1, 1, None],
		]],
		[0, -14, 1, c.d_object_a_5],
		[0, -29, 1, ultra.c.d_addr, 0],
		[0,   1, 1, c.d_obj_col],
		[0, -16, 1, c.d_object_a_6],
		[0,  -6, 1, ultra.c.d_addr, 0],
		[0,   1, 1, c.d_obj_col],
		[0,  -2, 1, c.d_object_a_7],
		[0,   1, 1, c.d_obj_col],
		[0,  -3, 1, ultra.c.d_addr, 0],
		[0,   1, 1, c.d_obj_col],
		[1,  -3, 3, ultra.c.d_s16], [0, 1, 2, None],
		[0, -15, 1, ultra.c.d_addr, 0],
		[0,   1, 1, c.d_obj_col],
		[0, -10, 1, ultra.c.d_addr, 0],
		[0,   4, 1, c.d_obj_splash],
		[0,   1, 1, c.d_obj_col],
		[0,  -7, 1, c.d_object_a_8],
	], [
		[0,   1,  4, "str"],
		[0,   2,  8, "str"],
		[0,   1,  4, "str"],
		[0,   2,  8, "str"],
		[0,   3, 12, "str"],
		[0,   3,  8, "str"],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   3, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   5, 1, ultra.c.d_f32],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   4, 1, ultra.c.d_f64],
		[0,   4, 1, ultra.c.d_f32],
		[0,   2, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 1, ultra.c.d_f64],
		[0,   9, 1, ultra.c.d_f32],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   3, 1, ultra.c.d_f64],
		[0, -10, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   2, 1, ultra.c.d_f64],
		[0, -10, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   2, 1, ultra.c.d_f64],
		[0,   6, 1, ultra.c.d_f32],
		[0,   1, 1, ultra.c.d_f64],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   2, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   2, 1, ultra.c.d_f32],
		[0,   2, 1, ultra.c.d_f64],
		[0,   2, 1, ultra.c.d_f32],
		[0,   5, 1, ultra.c.d_f64],
		[0, -12, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   2, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32],
		[0, -10, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 1, ultra.c.d_f32],
		[0,   3, 1, ultra.c.d_f64],
		[0, -11, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   4, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   4, 1, ultra.c.d_f32],
		[0,   1, 1, ultra.c.d_f64],
		[0,   2, 1, ultra.c.d_f32],
		[0,   1, 1, ultra.c.d_f64],
		[0,   4, 1, ultra.c.d_f32],
		[0,  -8, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 1, ultra.c.d_f32],
		[0,  -8, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   5, 1, ultra.c.d_f32],
		[0,   1, 1, ultra.c.d_f64],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 1, ultra.c.d_f32],
		[0,   1, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   2, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   8, 1, ultra.c.d_f32],
		[0,   3, 1, ultra.c.d_f64],
		[0,   2, 1, ultra.c.d_f32],
		[0,   1, 1, ultra.c.d_f64],
		[0,   3, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   3, 1, ultra.c.d_f64],
		[0,   5, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   4, 1, ultra.c.d_f64],
		[0,  10, 1, ultra.c.d_f32],
		[0, -11, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   6, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   2, 1, ultra.c.d_f32],
	]),
	# s_data(0x80330E20, 0x80330E38, 0x80337DF0, 0x80337DF0, 0, 0, "objphysics.data", ["sm64"], [
	# 	[0, 1, ultra.c.d_align_s16],
	# 	[1, 1, 1, ultra.c.d_str, 0x10, "0"],
	# 	[0, 1, 1, ultra.c.d_addr, 0],
	# ], []),
	s_data(0x80330E40, 0x80330E40, 0x80337DF0, 0x80337DF4, 0, 0, "objcollision.data", ["sm64"], [], [
		[0, 1, 4, "str"],
	]),
	# s_data(0x80330E40, 0x80330E40, 0x80337E00, 0x80337E10, 0, 0, "objlist.data", ["sm64"], [], [
	# 	[0, 4, 1, ultra.c.d_f32],
	# ]),
	# s_data(0x80330E40, 0x80330E40, 0x80337E10, 0x80337E1C, 0, 0, "objsfx.data", ["sm64"], [], [
	# 	[0, 3, 1, ultra.c.d_f32],
	# ]),
	s_data(0x80330E40, 0x80330EB2, 0x80337E20, 0x80337FF8, 0x80361290, 0x803612AC, "objdebug.data", ["sm64"], [
		[0, -18, 1, ultra.c.d_addr, 0],
		[0,   2, 1, ultra.c.d_s32],
		[0,   6, ultra.c.d_align_s8],
		[0,  -4, 1, ultra.c.d_flag16, ultra.flag_button],
		[0,  -1, 1, ultra.c.d_s16],
	], [
		[0,  8,  8, "str"],
		[0,  1,  4, "str"],
		[0,  8,  8, "str"],
		[0,  1,  4, "str"],
		[0,  1, 12, "str"],
		[0,  7,  8, "str"],
		[0,  6, 12, "str"],
		[0,  1, 16, "str"],
		[0,  2, 12, "str"],
		[0,  1,  8, "str"],
		[0, 10, 12, "str"],
		[0,  1, 16, "str"],
		[0, 1, 4, None],
		[0, 1, 1, ultra.c.d_f64],
	]),
	s_data(0x80330EC0, 0x80330ED8, 0x80338000, 0x80338060, 0, 0, "wipe.data", ["sm64"], [
		[1, 2, 1, ultra.c.d_str, 4, "0"],
		[0, -4, 1, ultra.c.d_addr, ultra.A_EXTERN],
	], [
		[0,   2, 1, ultra.c.d_f64],
		[0, -20, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x80330EE0, 0x80330EF8, 0x80338060, 0x8033813C, 0x803612B0, 0x803612B6, "shadow.data", ["sm64"], [
		[0, -2, 1, c.d_shadow_rect],
	], [
		[0,  15, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   3, 1, ultra.c.d_f64],
		[0, -13, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x80330F00, 0x80330F2E, 0x80338140, 0x80338160, 0x803612C0, 0x803612E0, "back.data", ["sm64"], [
		[0, -10, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[1, -2, 3, ultra.c.d_u8, "0x%02X"],
	], [
		[0, 4, 1, ultra.c.d_f64],
	]),
	s_data(0x80330F30, 0x803312F0, 0x80338160, 0x80338168, 0x803612E0, 0x803612E2, "scroll.data", ["sm64"], [
		[0,   2, ultra.c.d_align_s16],
		[0,   1, ultra.c.d_align_s8],
		[0,   1, 1, ultra.c.d_f32],
		[0,   1, 1, ultra.c.d_s32],
		[0,  -8, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0, -25, 1, c.d_scroll],
		[1,   1, 8, ultra.c.d_s8],
	], [
		[0, 1, 1, ultra.c.d_f64],
	]),
	# s_data(0x803312F0, 0x803312FC, 0x80338170, 0x80338170, 0x803612F0, 0x803612F1, "objshape.data", ["sm64"], [
	# 	[0, 3, ultra.c.d_align_s16],
	# ], []),
	s_data(0x80331300, 0x80331360, 0x80338170, 0x80338198, 0x80361300, 0x8036131D, "wave.data", ["sm64"], [
		[0, -19, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  -3, 1, ultra.c.d_addr, 0],
		[0,   2, ultra.c.d_align_s16],
	], [
		[0, 5, 1, ultra.c.d_f64],
	]),
	# s_data(0x80331360, 0x80331364, 0x803381A0, 0x803381A0, 0x80361320, 0x803613F0, "dprint.data", ["sm64"], [
	# 	[0, 1, ultra.c.d_align_s16],
	# ], []),
	[main.s_file, "message.data.c"],
		s_include(["sm64"]),
		[main.s_str, "\n"],
		[main.s_str, "#include \"str.h\"\n"],
		[main.s_str, "\n"],
		[ultra.c.s_data, 0x803381A0, 0x80338278, "E0", [
			[0,   3, 1, ultra.c.d_f64],
			[0, -48, 1, ultra.c.d_addr, ultra.A_EXTERN],
		]],
		[main.s_str, "\n"],
		[ultra.c.s_bss, 0x803613F0, 0x803613FF, "E0", 0x803381A0],
		[main.s_str, "\n"],
		[ultra.c.s_data, 0x80331370, 0x803314A4, "E0", [
			[0, -16, 16, ultra.c.d_u8],
			[0, 1, ultra.c.d_align_s8],
			[0, 2, 1, ultra.c.d_f32],
			[0, 1, ultra.c.d_align_s16],
			[0, 1, ultra.c.d_align_s8],
			[0, 3, ultra.c.d_align_s16],
			[0, 2, ultra.c.d_align_s8],
			[0, 2, ultra.c.d_align_u8],
			[0, 1, 1, ultra.c.d_s32],
			[1, -1, 4, ultra.c.d_u8, "0x%02X"], [0, 1, 1, None],
			[1, -1, 4, ultra.c.d_u8, "0x%02X"], [0, 1, 3, None],
		]],
		[main.s_str, "unsigned char str_803314B0[] = {STR_PCOIN};\n"],
		[main.s_str, "unsigned char str_803314B4[] = {STR_PX};\n"],
		[main.s_str, "unsigned char str_803314B8[] = {STR_PSTAR};\n"],
		[main.s_str, "unsigned char str_803314BC[] = {STR_PX};\n"],
		[ultra.c.s_data, 0x803314C0, 0x803314FC, "E0", [
			[1, -1, 4, ultra.c.d_u8, "0x%02X"], [0, 1, 1, None],
			[1, -1, 4, ultra.c.d_u8, "0x%02X"], [0, 1, 3, None],
			[1, 1, 5, ultra.c.d_s16], [0, 1, 2, None],
			[1, 1, 4, ultra.c.d_s16],
			[1, 1, 5, ultra.c.d_s16], [0, 1, 2, None],
			[1, 1, 5, ultra.c.d_s16], [0, 1, 2, None],
			[0, 1, ultra.c.d_align_s16],
		]],
		[c.s_message, 0x803315E4, 0x8033160C, "E0", "tbl", "803315E4", "803315E4", "en"],
		[ultra.c.s_data, 0x8033160C, 0x80331624, "E0", [
			[0, 1, ultra.c.d_align_u16],
			[0, 3, ultra.c.d_align_s16],
			[0, 2, ultra.c.d_align_s8],
		]],
		[main.s_str, "unsigned char str_80331624[] = {STR_COURSE};\n"],
		[main.s_str, "unsigned char str_8033162C[] = {STR_MY_SCORE};\n"],
		[main.s_str, "unsigned char str_80331638[] = {STR_STAR};\n"],
		[main.s_str, "unsigned char str_8033163C[] = {STR_NOSTAR};\n"],
		[main.s_str, "unsigned char str_80331640[] = {STR_LAKITU_MARIO};\n"],
		[main.s_str, "unsigned char str_80331650[] = {STR_LAKITU_STOP};\n"],
		[main.s_str, "unsigned char str_80331660[] = {STR_NORMAL_UP_CLOSE};\n"],
		[main.s_str, "unsigned char str_80331674[] = {STR_NORMAL_FIXED};\n"],
		[main.s_str, "unsigned char str_80331684[] = {STR_CONTINUE};\n"],
		[main.s_str, "unsigned char str_80331690[] = {STR_EXIT_COURSE};\n"],
		[main.s_str, "unsigned char str_8033169C[] = {STR_SET_CAMERA_ANGLE_WITH_R};\n"],
		[main.s_str, "unsigned char str_803316B4[] = {STR_PAUSE};\n"],
		[main.s_str, "unsigned char str_803316BC[] = {STR_STAR};\n"],
		[main.s_str, "unsigned char str_803316C0[] = {STR_COIN_X};\n"],
		[main.s_str, "unsigned char str_803316C4[] = {STR_STAR_X};\n"],
		[ultra.c.s_data, 0x803316C8, 0x803316D8, "E0", [
			[0, 1, ultra.c.d_align_s8],
			[0, 2, 1, ultra.c.d_s32],
			[0, 1, ultra.c.d_align_s8],
		]],
		[main.s_str, "unsigned char str_803316D8[] = {STR_HI_SCORE};\n"],
		[main.s_str, "unsigned char str_803316E4[] = {STR_CONGRATULATIONS};\n"],
		[main.s_str, "unsigned char str_803316F4[] = {STR_PCOIN};\n"],
		[main.s_str, "unsigned char str_803316F8[] = {STR_PX};\n"],
		[main.s_str, "unsigned char str_803316FC[] = {STR_COURSE};\n"],
		[main.s_str, "unsigned char str_80331704[] = {STR_CATCH};\n"],
		[main.s_str, "unsigned char str_8033170C[] = {STR_CLEAR};\n"],
		[main.s_str, "unsigned char str_80331714[] = {STR_PSTAR};\n"],
		[main.s_str, "unsigned char str_80331718[] = {STR_SAVE_AND_CONTINUE};\n"],
		[main.s_str, "unsigned char str_80331728[] = {STR_SAVE_AND_QUIT};\n"],
		[main.s_str, "unsigned char str_80331734[] = {STR_CONTINUE_DONT_SAVE};\n"],
	[main.s_write],
	s_data(0x80331750, 0x803317A0, 0x80338280, 0x803382B8, 0x80361400, 0x80361418, "snow.data", ["sm64"], [
		[0, 1, ultra.c.d_align_s8],
		[0, 1, 4, None],
		[0, -3, 1, ultra.c.d_Vtx, False],
		[0, 3, [
			[1, 1, 3, ultra.c.d_s16],
			[0, 1, 2, None],
		]],
	], [
		[0, 7, 1, ultra.c.d_f64],
	]),
	s_data(0x803317A0, 0x803317D8, 0x803382C0, 0x80338310, 0x80361420, 0x80361440, "lava.data", ["sm64"], [
		[0, 1, ultra.c.d_align_s8],
		[0, 1, 4, None],
		[0, -3, 1, ultra.c.d_Vtx, False],
	], [
		[0,   5, 1, ultra.c.d_f32],
		[0, -15, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	# s_data(0x803317E0, 0x803325E8, 0x80338310, 0x8033837C, 0, 0, "tag.data", ["sm64"], [
	# 	[0, -366, 1, c.d_tag_obj, 0x803317E0],
	# 	[0,  -83, 1, c.d_map_obj],
	# ], [
	# 	[0, -27, 1, ultra.c.d_addr, ultra.A_EXTERN],
	# ]),
	s_data(0x803317E0, 0x80332350, 0x80338380, 0x80338380, 0, 0, "tag_obj", [], [
		[0, -366, 1, c.d_tag_obj, 0x803317E0],
	], []),
	s_data(0x80332350, 0x803325E8, 0x80338380, 0x80338380, 0, 0, "map_obj", [], [
		[0,  -83, 1, c.d_map_obj],
	], []),
	# s_data(0x803325F0, 0x8033260C, 0x80338380, 0x803383D0, 0x80361440, 0x80361442, "hud.data", ["sm64"], [
	# 	[0, 1, 1, c.d_meter],
	# 	[0, 1, 1, ultra.c.d_s32],
	# 	[0, 3, ultra.c.d_align_s16],
	# ], [
	# 	[0, 10, 4, "str"],
	# 	[0,  1, 8, "str"],
	# 	[0,  1, 4, "str"],
	# 	[0,  1, 8, "str"],
	# 	[0,  1, 4, "str"],
	# 	[0,  2, 1, ultra.c.d_f64],
	# ]),
	s_data(0x80332610, 0x8033283C, 0x803383D0, 0x803389A4, 0x80361450, 0x80361454, "object_b.data", ["sm64"], [
		[0, 1, ultra.c.d_align_s8],
		[0, 1, ultra.c.d_align_s16],
		[0, 3, ultra.c.d_align_s8],
		[0, 10, 1, c.d_obj_col],
		[0, 2, 1, c.d_path_data],
		[0, 4, 1, c.d_obj_col],
		[0, 1, ultra.c.d_align_s8],
		[0, 1, 1, c.d_obj_col],
		[0, 1, 1, c.d_path_data],
		[0, 3, 1, c.d_obj_col],
		[1, -4, 2, ultra.c.d_s16],
	], [
		[0,  21, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   2, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32],
		[0, -10, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  18, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   2, 1, ultra.c.d_f64],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN], [0, 1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   6, 1, ultra.c.d_f64],
		[0,  11, 1, ultra.c.d_f32],
		[0,  -6, 1, ultra.c.d_addr, ultra.A_EXTERN], [0, 1, 4, None],
		[0,   5, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   3, 1, ultra.c.d_f64],
		[0,  15, 1, ultra.c.d_f32],
		[0, -16, 1, ultra.c.d_addr, ultra.A_EXTERN], [0, 1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  10, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   3, 1, ultra.c.d_f64],
		[0,   4, 1, ultra.c.d_f32],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   6, 1, ultra.c.d_f32],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   4, 1, ultra.c.d_f32],
		[0,   1, 1, ultra.c.d_f64],
		[0, -36, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   3, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   2, 1, ultra.c.d_f64],
		[0,  11, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   3, 1, ultra.c.d_f64],
		[0,  -7, 1, ultra.c.d_addr, ultra.A_EXTERN], [0, 1, 4, None],
		[0,  20, 1, ultra.c.d_f64],
		[0,   3, 1, ultra.c.d_f32], [0, 1, 4, None],
		[0,   2, 1, ultra.c.d_f64],
		[0,   8, 1, ultra.c.d_f32],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   3, 1, ultra.c.d_f32],
		[0,   1, 1, ultra.c.d_f64],
		[0,   4, 1, ultra.c.d_f32],
		[0, -11, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x80332840, 0x80332E4C, 0x803389B0, 0x80338D94, 0x80361460, 0x8036148C, "object_c.data", ["sm64"], [
		[0,   1, 1, c.d_obj_col],
		[1,   1, 6, ultra.c.d_u8], [0, 1, 2, None], # template
		[1,   1, 6, ultra.c.d_u8], [0, 1, 2, None], # template
		[0,  -2, 1, c.d_object_c_0],
		[0,   1, 1, c.d_obj_col],
		[1,   1, 6, ultra.c.d_u8], [0, 1, 2, None], # template
		[0,   2, 1, c.d_obj_col],
		[1,   1, 3, ultra.c.d_s16], [0, 1, 2, None],
		[0,   1, 1, c.d_obj_col],
		[0,  -3, 1, c.d_object_c_1],
		[1,  -2, 6, ultra.c.d_u8], # template
		[0,   3, 1, c.d_obj_col],
		[1,   1, 6, ultra.c.d_u8], [0, 1, 2, None], # template
		[1,   1, 4, ultra.c.d_f32],
		[1,   1, 3, ultra.c.d_s32, table.fmt_msg],
		[0,   1, 1, c.d_obj_col],
		[1,   1, 6, ultra.c.d_u8], [0, 1, 2, None], # template
		[0,   1, 1, c.d_obj_col],
		[1,   1, 6, ultra.c.d_s8], [0, 1, 2, None],
		[0,   1, 1, c.d_obj_pcl],
		[0,   2, 1, c.d_obj_col],
		[0,   1, 1, c.d_obj_pcl],
		[0, -21, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  -2, 1, c.d_object_c_2],
		[0,   1, 1, c.d_obj_col],
		[0,   2, 1, c.d_obj_pcl],
		[0,  -2, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[1,   1, 4, ultra.c.d_u8],
		[1,   1, 4, ultra.c.d_f32],
		[0,  -2, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[1,   2, 4, ultra.c.d_s16],
		[1,   1, 4, ultra.c.d_s8],
		[0,  -2, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[1,   1, 2, ultra.c.d_s8], [0, 1, 2, None],
		[1,   1, 2, ultra.c.d_s16],
		[0,  -2, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[1,  -4, 2, c.d_80332AC0],
		[1,   1, 4, ultra.c.d_s8],
		[1,   1, 2, ultra.c.d_s16],
		[1,  -2, 4, ultra.c.d_s16],
		[1,   1, 4, ultra.c.d_s16],
		[0,   1, 1, c.d_obj_col],
		[0,   1, 1, c.d_obj_pcl],
		[0,   1, 1, c.d_obj_col],
		[0, -10, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[1,   1, 4, ultra.c.d_s16],
		[1,  -3, [
			[0, -5, 1, c.d_object_c_3],
		]],
		[1,   1, 3, ultra.c.d_s16], [0, 1, 2, None],
		[0,  -3, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   5, 1, c.d_obj_col],
		[1,  -3, 2, ultra.c.d_s16],
		[0,   2, 1, c.d_obj_col],
		[1,   1, 2, ultra.c.d_f32, "%g"],
		[0,   4, 1, c.d_obj_col],
		[1,   1, 6, ultra.c.d_s8], [0, 1, 2, None],
		[0,   1, 1, c.d_obj_col],
		[1,  -3, 3, ultra.c.d_f32],
		[1,   1, 6, ultra.c.d_u8], [0, 1, 2, None], # template
		[0,  -2, 1, c.d_object_c_4],
		[1,  -6, 2, ultra.c.d_s16],
		[0,   2, 1, c.d_obj_col],
		[1,  -4, 2, ultra.c.d_s16],
		[1, -31, 3, ultra.c.d_s16], [0, 1, 2, None],
		[0,   1, 1, c.d_obj_col],
		[0,  -2, 1, c.d_object_c_5],
		[0,   1, 1, c.d_obj_col],
	], [
		[0,   2, 1, ultra.c.d_f32],
		[0,  -9, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  21, 1, ultra.c.d_f32],
		[0,  -7, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  22, 1, ultra.c.d_f32],
		[0,  -6, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   4, 1, ultra.c.d_f32],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  23, 1, ultra.c.d_f32],
		[0,  -8, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   4, 1, ultra.c.d_f32],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  18, 1, ultra.c.d_f32],
		[0,  -8, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   8, 1, ultra.c.d_f32],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   7, 1, ultra.c.d_f32],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  12, 1, ultra.c.d_f32],
		[0,  -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   4, 1, ultra.c.d_f32],
		[0, -15, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   6, 1, ultra.c.d_f32],
		[0,  -8, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   8, 1, ultra.c.d_f32],
		[0,  -6, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  18, 1, ultra.c.d_f32],
	]),
]

src_ulib = [
	# s_code(0x80378800, 0x8037B21C, "math", [], str_fp),
	# s_code(0x8037B220, 0x8037CB60, "shape"),
	# s_code(0x8037CB60, 0x8037E19C, "shplang"),
	# s_code(0x8037E1A0, 0x80380684, "prglang"),
	# s_code(0x80380690, 0x8038248C, "bgcheck"),
	# s_code(0x80382490, 0x80383B6C, "bgload", [], str_fp),
	s_code(0x80383B70, 0x80385F88, "objlang", [], str_fp),

	# s_data(0x80385F90, 0x80385FF8, 0x8038BA90, 0x8038BAEC, 0x8038BC90, 0x8038BC9C, "math.data", ["sm64"], [
	# 	[0, 1, 1, c.d_matrix],
	# 	[1, 1, 3, ultra.c.d_f32],
	# 	[1, 1, 3, ultra.c.d_s16], [0, 1, 2, None],
	# 	[1, 1, 3, ultra.c.d_f32],
	# 	[1, 1, 3, ultra.c.d_s16], [0, 1, 2, None],
	# ], [
	# 	[0, 1, 1, ultra.c.d_f64],
	# 	[0, -5, 1, ultra.c.d_addr, ultra.A_EXTERN],
	# 	[0, 16, 1, ultra.c.d_f32],
	# ]),
	[main.s_file, "mathtbl.s"],
		[main.s_str, str_data],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[ultra.asm.s_data, 0x80386000, 0x8038B802, "E0", [
			[0x1400, 1, ultra.asm.d_float],
			[  0x80, 8, ultra.asm.d_uhalf, "0x%04X"],
			[     1, 1, ultra.asm.d_uhalf, "0x%04X"],
		]],
	[main.s_write],
	# s_data(0x8038B810, 0x8038B894, 0x8038BAF0, 0x8038BAF0, 0x8038BCA0, 0x8038BD9C, "shplang.data", ["sm64"], [
	# 	[0, -0x21, 1, ultra.c.d_addr, ultra.A_EXTERN],
	# ], []),
	# s_data(0x8038B8A0, 0x8038B9AC, 0x8038BAF0, 0x8038BB38, 0x8038BDA0, 0x8038BE2C, "prglang.data", ["sm64"], [
	# 	[0, 1, 1, ultra.c.d_addr, 0],
	# 	[0, 2, ultra.c.d_align_u16],
	# 	[0, 1, ultra.c.d_align_s16],
	# 	[0, 2, 1, ultra.c.d_addr, 0],
	# 	[0, -0x3D, 1, ultra.c.d_addr, ultra.A_EXTERN],
	# ], [
	# 	[0, -18, 1, ultra.c.d_addr, ultra.A_EXTERN],
	# ]),
	# s_data(0x8038B9B0, 0x8038B9B0, 0x8038BB40, 0x8038BBB0, 0x8038BE30, 0x8038BE90, "bgcheck.data", ["sm64"], [], [
	# 	[0, 1, 12, "str"],
	# 	[0, 3,  8, "str"],
	# 	[0, 3,  4, "str"],
	# 	[0, 3, 12, "str"],
	# 	[0, 7, 1, ultra.c.d_f32],
	# ]),
	# s_data(0x8038B9B0, 0x8038B9B0, 0x8038BBB0, 0x8038BC84, 0x8038BE90, 0x8038EED4, "bgload.data", ["sm64"], [], [
	# 	[0, 5, 1, ultra.c.d_f64],
	# 	[0, -42, 1, ultra.c.d_addr, ultra.A_EXTERN],
	# 	[0, 1, 1, ultra.c.d_f32],
	# ]),
	s_data(0x8038B9B0, 0x8038BA90, 0x8038BC90, 0x8038BC90, 0x8038EEE0, 0x8038EEE2, "objlang.data", ["sm64"], [
		[0, -0x38, 1, ultra.c.d_addr, ultra.A_EXTERN],
	], []),
]

src_menu = [
	# s_code(0x8016F000, 0x8016F670, "title"),
	# s_code(0x8016F670, 0x80170280, "titlebg"),
	s_code(0x80170280, 0x801768E0, "fileselect", [], str_fp),
	s_code(0x801768E0, 0x80177710, "starselect", [], str_fp),

	# s_data(0x801A7830, 0x801A7C3C, 0x801A7C40, 0x801A7C68, 0, 0, "title.data", ["sm64"], [
	# 	[0, -38, 16, "str"],
	# 	[0, 26, 16, None],
	# 	[0, 1, ultra.c.d_align_u16],
	# 	[0, 2, ultra.c.d_align_s16],
	# ], [
	# 	[0, 1, 16, "str"],
	# 	[0, 1, 20, "str"],
	# 	[0, 1,  4, "str"],
	# ]),
	# s_data(0x801A7C70, 0x801A7D10, 0x801A7D10, 0x801A7D10, 0x801B99E0, 0x801B99F0, "titlebg.data", ["sm64"], [
	# 	[0, -4, 1, ultra.c.d_addr, ultra.A_EXTERN],
	# 	[0, -6, 4, ultra.c.d_f32],
	# 	[0, -2, 1, ultra.c.d_addr, ultra.A_EXTERN],
	# 	[0, -3, 4, ultra.c.d_s8],
	# 	[0, -1, 1, ultra.c.d_addr, 0],
	# 	[0, -3, 4, ultra.c.d_s8],
	# 	[0, -1, 4, ultra.c.d_s8],
	# 	[0, -1, 1, ultra.c.d_s8],
	# 	[0, -1, 4, ultra.c.d_s8],
	# 	[0, -1, 3, ultra.c.d_s8],
	# ], []),
	[main.s_file, "fileselect.data.c"],
		s_include(["sm64"]),
		[main.s_str, "\n"],
		[main.s_str, "#include \"str.h\"\n"],
		[main.s_str, "\n"],
		[ultra.c.s_data, 0x801A7F40, 0x801A8194, "E0", [
			[0,    1, 1, ultra.c.d_f32], [0, 1, 4, None],
			[0,    7, 1, ultra.c.d_f64],
			[0,   -7, 1, ultra.c.d_addr, ultra.A_EXTERN],
			[0,   24, 1, ultra.c.d_f32],
			[0, -102, 1, ultra.c.d_addr, ultra.A_EXTERN],
		]],
		[main.s_str, "\n"],
		[ultra.c.s_bss, 0x801B99F0, 0x801B9A7A, "E0", 0x801A7D10],
		[main.s_str, "\n"],
		[ultra.c.s_data, 0x801A7D10, 0x801A7D54, "E0", [
			[0, 2, ultra.c.d_align_s8],
			[0, 1, ultra.c.d_align_u8],
			[1, 1, 2, ultra.c.d_f32],
			[0, 1, ultra.c.d_align_s16],
			[1, 1, 2, ultra.c.d_s16],
			[0, 3, ultra.c.d_align_s8],
			[0, 1, ultra.c.d_align_u8],
			[0, 1, ultra.c.d_align_s16],
			[0, 5, ultra.c.d_align_s8],
		]],
		[main.s_str, "unsigned char str_801A7D54[] = {STR_RETURN};\n"],
		[main.s_str, "unsigned char str_801A7D5C[] = {STR_CHECK_SCORE};\n"],
		[main.s_str, "unsigned char str_801A7D68[] = {STR_COPY_FILE};\n"],
		[main.s_str, "unsigned char str_801A7D74[] = {STR_ERASE_FILE};\n"],
		[main.s_str, "unsigned char str_801A7D80[][8] =\n"],
		[main.s_str, "{\n"],
		[main.s_str, "\t{STR_STEREO},"],
		[main.s_str, "\t{STR_MONO},"],
		[main.s_str, "\t{STR_HEADSET},"],
		[main.s_str, "};\n"],
		[main.s_str, "unsigned char str_801A7D98[] = {STR_MARIO_A};\n"],
		[main.s_str, "unsigned char str_801A7DA0[] = {STR_MARIO_B};\n"],
		[main.s_str, "unsigned char str_801A7DA8[] = {STR_MARIO_C};\n"],
		[main.s_str, "unsigned char str_801A7DB0[] = {STR_MARIO_D};\n"],
		[main.s_str, "unsigned char str_801A7DB8[] = {STR_NEW};\n"],
		[main.s_str, "unsigned char str_801A7DBC[] = {STR_PSTAR};\n"],
		[main.s_str, "unsigned char str_801A7DC0[] = {STR_PX};\n"],
		[main.s_str, "unsigned char str_801A7DC4[] = {STR_SELECT_FILE};\n"],
		[main.s_str, "unsigned char str_801A7DD0[] = {STR_SCORE};\n"],
		[main.s_str, "unsigned char str_801A7DD8[] = {STR_COPY};\n"],
		[main.s_str, "unsigned char str_801A7DE0[] = {STR_ERASE};\n"],
		[main.s_str, "unsigned char str_801A7DE8[] = {STR_CHECK_FILE};\n"],
		[main.s_str, "unsigned char str_801A7DF4[] = {STR_NO_SAVED_DATA_EXISTS};\n"],
		[main.s_str, "unsigned char str_801A7E0C[] = {STR_COPY_FILE};\n"],
		[main.s_str, "unsigned char str_801A7E18[] = {STR_COPY_IT_TO_WHERE};\n"],
		[main.s_str, "unsigned char str_801A7E2C[] = {STR_NO_SAVED_DATA_EXISTS};\n"],
		[main.s_str, "unsigned char str_801A7E44[] = {STR_COPYING_COMPLETED};\n"],
		[main.s_str, "unsigned char str_801A7E58[] = {STR_SAVED_DATA_EXISTS};\n"],
		[main.s_str, "unsigned char str_801A7E6C[] = {STR_NO_EMPTY_FILE};\n"],
		[main.s_str, "unsigned char str_801A7E7C[] = {STR_YES};\n"],
		[main.s_str, "unsigned char str_801A7E80[] = {STR_NO};\n"],
		[main.s_str, "unsigned char str_801A7E84[] = {STR_ERASE_FILE};\n"],
		[main.s_str, "unsigned char str_801A7E90[] = {STR_SURE};\n"],
		[main.s_str, "unsigned char str_801A7E98[] = {STR_NO_SAVED_DATA_EXISTS};\n"],
		[main.s_str, "unsigned char str_801A7EB0[] = {STR_MARIO_A_JUST_ERASED};\n"],
		[main.s_str, "unsigned char str_801A7EC4[] = {STR_SAVED_DATA_EXISTS};\n"],
		[main.s_str, "unsigned char str_801A7ED8[] = {STR_SOUND_SELECT};\n"],
		[main.s_str, "unsigned char str_801A7EE8[] = {STR_STAR_X};\n"],
		[main.s_str, "unsigned char str_801A7EEC[] = {STR_COIN_X};\n"],
		[main.s_str, "unsigned char str_801A7EF0[] = {STR_STAR};\n"],
		[main.s_str, "unsigned char str_801A7EF4[][8] =\n"],
		[main.s_str, "{\n"],
		[main.s_str, "\t{STR_FILE_NULL},"],
		[main.s_str, "\t{STR_FILE_A},"],
		[main.s_str, "\t{STR_FILE_B},"],
		[main.s_str, "\t{STR_FILE_C},"],
		[main.s_str, "\t{STR_FILE_D},"],
		[main.s_str, "};\n"],
		[main.s_str, "unsigned char str_801A7F1C[] = {STR_MARIO};\n"],
		[main.s_str, "unsigned char str_801A7F24[] = {STR_HI_SCORE};\n"],
		[main.s_str, "unsigned char str_801A7F30[] = {STR_MY_SCORE};\n"],
		[ultra.c.s_data, 0x801A7F3C, 0x801A7F3E, "E0", [
			[0, 1, 1, ultra.c.d_s16, "0x%02X"],
		]],
	[main.s_write],
	[main.s_file, "starselect.data.c"],
		s_include(["sm64"]),
		[main.s_str, "\n"],
		[main.s_str, "#include \"str.h\"\n"],
		[main.s_str, "\n"],
		[ultra.c.s_data, 0x801A81C0, 0x801A81E0, "E0", [
			[0, 3, 1, ultra.c.d_f64],
			[0, 2, 1, ultra.c.d_f32],
		]],
		[main.s_str, "\n"],
		[ultra.c.s_bss, 0x801B9A80, 0x801B9AA4, "E0", 0x801A81A0],
		[main.s_str, "\n"],
		[ultra.c.s_data, 0x801A81A0, 0x801A81AC, "E0", [
			[0, 2, ultra.c.d_align_s8],
			[0, 1, 1, ultra.c.d_s32],
		]],
		[main.s_str, "unsigned char str_801A81AC[] = {STR_MYSCORE};\n"],
		[ultra.c.s_data, 0x801A81B4, 0x801A81B6, "E0", [
			[0, 1, 1, ultra.c.d_u16, "0x%02X"],
		]],
	[main.s_write],
]

src_audio = [
	s_code(0x80314A30, 0x80316E78, "a"),
	s_code(0x80316E80, 0x80318034, "b"),
	s_code(0x80318040, 0x80319914, "c"),
	s_code(0x80319920, 0x8031AEDC, "d"),
	s_code(0x8031AEE0, 0x8031B82C, "e"),
	s_code(0x8031B830, 0x8031E4E4, "f"),
	s_code(0x8031E4F0, 0x80322364, "g", [], str_fp),

	s_data(0x80332E50, 0x80332E50, 0x80338DA0, 0x80338DB4, 0, 0, "a.data", ["sm64"], [], [
		[0, 5, 1, ultra.c.d_f32],
	]),
	s_data(0x80332E50, 0x80332E50, 0x80338DC0, 0x80338E08, 0, 0, "b.data", ["sm64"], [], [
		[0, -16, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   2, 1, ultra.c.d_f32],
	]),
	s_data(0x80332E50, 0x80332E50, 0x80338E10, 0x80338E28, 0, 0, "d.data", ["sm64"], [], [
		[0, 6, 1, ultra.c.d_f32],
	]),
	s_data(0x80332E50, 0x80332E50, 0x80338E30, 0x80338E54, 0, 0, "e.data", ["sm64"], [], [
		[0, -9, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x80332E50, 0x80332E50, 0x80338E60, 0x803394E4, 0, 0, "f.data", ["sm64"], [], [
		[0, -417, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	[main.s_file, "g.s"],
		[main.s_str, "\n"],
		[main.s_str, str_bss],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[main.s_str, str_audio_g],
	[main.s_write],
	s_data(0x80332E50, 0x803332A0, 0x803394F0, 0x803397AC, 0, 0, "g.data", ["sm64"], [
		[0, 2, 1, ultra.c.d_s32],
		[0, -17, 10, ultra.c.d_s8, "%2d"],
		[0, 1, 2, None],
		[0, -11, 1, ultra.c.d_u32, UNSM.table.fmt_na_se],
		[0, 1, 4*4, None],
		[0, 2, ultra.c.d_align_u8],
		[0, 1, 1, c.d_Na_bgmctl, 6],
		[0, 1, 1, c.d_Na_bgmctl, 12],
		[0, 1, 1, c.d_Na_bgmctl, 12],
		[0, 1, 1, c.d_Na_bgmctl, 2],
		[0, 1, 1, c.d_Na_bgmctl, 7],
		[0, 1, 1, c.d_Na_bgmctl, 8],
		[0, 1, 1, c.d_Na_bgmctl, 7],
		[0, 1, 1, c.d_Na_bgmctl, 1],
		[0, 2, ultra.c.d_align_s8],
		[0, -39, 1, ultra.c.d_addr, 0],
		[0, -8, 1, c.d_Na_bgmctl_data],
		[1, -39, 3, ultra.c.d_u8, "0x%02X"],
		[0, 1, 3, None],
		[0, -39, 1, ultra.c.d_u16], # ? - doesnt seem like d
		[0, 1, 2, None],
		[0, -34, 1, ultra.c.d_u8],
		[0, 1, 2, None],
		[0, 2, ultra.c.d_align_s8],
		[0, 4, [
			[1, 1, 10, ultra.c.d_u8],
			[0, 1, 2, None],
		]],
		[1, 1, 10, ultra.c.d_u8, "0x%02X"],
		[0, 1, 2, None],
		[1, 2, 3, ultra.c.d_f32],
		[1, 1, 10, ultra.c.d_u8],
		[0, 1, 2, None],
		[0, 3, ultra.c.d_align_u8],
		[0, 1, ultra.c.d_align_u16],
		[0, 1, ultra.c.d_align_u8],
		[0, 1, ultra.c.d_align_u16],
		[0, 5, ultra.c.d_align_u8],
		[0, -4, 4, ultra.c.d_u32, "0x%08X"],
		[1, 2, 16, ultra.c.d_s8],
	], [
		[0, 1, 12, "str"],
		[0, 1, 28, "str"],
		[0, 1, 12, "str"],
		[0, 1, 28, "str"],
		[0, 1, 12, "str"],
		[0, 1, 20, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1, 12, "str"],
		[0, 1, 20, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 2, 48, "str"],
		[0, 1,  8, "str"],
		[0, 2,  4, "str"],
		[0, 1,  8, "str"],
		[0, 2,  4, "str"],
		[0, 4, 12, "str"],
		[0, 1, 24, "str"],
		[0, 1, 28, "str"],
		[0, 5, 16, "str"],
		[0, 1, 12, "str"],
		[0, 1, 20, "str"],
		[0, 1, 32, "str"],
		[0, 1,  4, None],
		[0,   2, 1, ultra.c.d_f64],
		[0,   7, 1, ultra.c.d_f32],
		[0, -28, 1, ultra.c.d_addr, ultra.A_EXTERN],
	], str_audio_g_data),
	s_data(0x803332A0, 0x8033500C, 0x803397B0, 0x803397B0, 0, 0, "data", ["sm64"], [
		[0, -18, 1, c.d_Na_cfg],
		[0, -128//8, 8, ultra.c.d_u16, "0x%04X"],
		[0, -252//4, 4, ultra.c.d_f32, "%f"],
		[0,      -1, 3, ultra.c.d_f32, "%f"],
		[0, -128//4, 4, ultra.c.d_f32, "%f"],
		[1,  1, 16, ultra.c.d_u8],
		[1,  1, 16, ultra.c.d_u8],
		[1,  1, 16, ultra.c.d_s8],
		[1,  1, 6, ultra.c.d_s16],
		[0, -4*64//8, 8, ultra.c.d_s16, "%6d"],
		[0, -4, 1, ultra.c.d_addr, 0],
		[1,  1, 10, ultra.c.d_u16],
		[0, -3*128//4, 4, ultra.c.d_f32, "%f"],
		[0, 3, [
			[0, -128//4, 4, ultra.c.d_f32, "%.3f"],
			[0, -128//4, 4, ultra.c.d_f32, "%f"],
		]],
		[0,  1, ultra.c.d_align_s16],
		[0,  1, ultra.c.d_align_s8],
		[0,  2, 1, ultra.c.d_u32, "0x%X"],
		[0,  1, 1, ultra.c.d_s32],
		[0,  1, ultra.c.d_align_s8],
	], []),
	[main.s_file, "bss.s"],
		[main.s_str, "\n"],
		[main.s_str, str_bss],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[main.s_str, str_audio_bss],
	[main.s_write],
	# [main.s_file, "heap.c"],
	# 	s_include(["sm64"]),
	# 	[main.s_str, "\n"],
	# 	[ultra.c.s_bss, 0x801CE000, 0x80200200, "E0", 0x8032D560],
	# [main.s_write],
]

src_face = [
	s_code(0x80177710, 0x80177820, "main"),
	s_code(0x80177820, 0x801781DC, "mem", [], str_fp),
	s_code(0x801781E0, 0x80178278, "sfx"),
	s_code(0x80178280, 0x8017BDE4, "draw", [], str_fp),
	s_code(0x8017BDF0, 0x80181718, "object", [], str_fp),
	s_code(0x80181720, 0x80181D38, "skin", [], str_fp),
	s_code(0x80181D40, 0x80183A48, "particle", [], str_fp),
	s_code(0x80183A50, 0x8018B830, "dynlist", [], str_fp),
	s_code(0x8018B830, 0x8018C2F0, "gadget", [], str_fp),
	s_code(0x8018C2F0, 0x8018E660, "stdio", [], str_fp),
	s_code(0x8018E660, 0x80192050, "joint", [], str_fp),
	s_code(0x80192050, 0x80193C70, "net", [], str_fp),
	s_code(0x80193C70, 0x801973C0, "math", [], str_fp),
	s_code(0x801973C0, 0x8019B060, "shape", [], str_fp),
	s_code(0x8019B060, 0x801A7830, "gfx", [], str_fp),

	s_data(0x801A81E0, 0x801A81F8, 0x801B54C0, 0x801B54FC, 0, 0, "main.data", ["sm64"], [
		[0, 2, 1, ultra.c.d_s32, ultra.fmt_bool],
		[0, 1, 1, ultra.c.d_f32],
		[0, 1, 1, ultra.c.d_s32, ultra.fmt_bool],
		[0, 2, 1, ultra.c.d_s32],
	], [
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 20, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 1, ultra.c.d_f32],
	]),
	s_data(0x801A8200, 0x801A8200, 0x801B5500, 0x801B560C, 0, 0, "mem.data", ["sm64"], [], [
		[0, 1, 36, "str"],
		[0, 1, 24, "str"],
		[0, 1, 32, "str"],
		[0, 1, 24, "str"],
		[0, 1, 40, "str"],
		[0, 1, 20, "str"],
		[0, 1,  4, "str"],
		[0, 1, 20, "str"],
		[0, 1,  4, "str"],
		[0, 1, 20, "str"],
		[0, 1,  4, "str"],
		[0, 1, 20, "str"],
		[0, 1,  4, "str"],
		[0, 1, 16, "str"],
	]),
	s_databin(0x801A8200, 0x801A8334, "draw.data"),
	[main.s_file, "draw.s"],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[main.s_str, str_face_draw],
	[main.s_write],
	s_data(0x801A8200, 0x801A8334, 0x801B5610, 0x801B5914, 0, 0, "draw.data", ["sm64"], [
	], [
		[0, 1, 12, "str"],
		[0, 1, 28, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 44, "str"],
		[0, 1,  8, "str"],
		[0, 1, 20, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 16, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 44, "str"],
		[0, 1, 48, "str"],
		[0, 1, 24, "str"],
		[0, 1, 40, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1, 36, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0,   2, 1, ultra.c.d_f64],
		[0, -12, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   4, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32],
	]),
	s_databin(0x801A8340, 0x801A8358, "object.data"),
	[main.s_file, "object.s"],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[main.s_str, str_face_object],
	[main.s_write],
	s_data(0x801A8340, 0x801A8358, 0x801B5920, 0x801B5ED8, 0, 0, "object.data", ["sm64"], [
	], [
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 32, "str"],
		[0, 1, 36, "str"],
		[0, 1,  8, "str"],
		[0, 1, 28, "str"],
		[0, 1,  8, "str"],
		[0, 1, 28, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 20, "str"],
		[0, 1, 28, "str"],
		[0, 1, 24, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1, 12, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1, 12, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1, 28, "str"],
		[0, 1, 44, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 12, "str"],
		[0,   6, 1, ultra.c.d_f32],
		[0, -64, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   2, 1, ultra.c.d_f32],
		[0,   1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32],
		[0, -32, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 4, None],
		[0,   5, 1, ultra.c.d_f64],
		[0,   1, 1, ultra.c.d_f32],
		[0, -11, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   2, 1, ultra.c.d_f64],
	]),
	s_data(0x801A8360, 0x801A8360, 0x801B5EE0, 0x801B5F38, 0, 0, "skin.data", ["sm64"], [], [
		[0, 1, 44, "str"],
		[0, 1, 44, "str"],
	]),
	s_databin(0x801A8360, 0x801A83D8, "particle.data"),
	[main.s_file, "particle.s"],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[main.s_str, str_face_particle],
	[main.s_write],
	s_data(0x801A8360, 0x801A83D8, 0x801B5F40, 0x801B5FD8, 0, 0, "particle.data", ["sm64"], [
	], [
		[0, 1, 36, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 4, 1, ultra.c.d_f64],
		[0, 1, 1, ultra.c.d_f32],
		[0, 1, 4, None],
		[0, 4, 1, ultra.c.d_f64],
	]),
	s_databin(0x801A83E0, 0x801A8404, "dynlist.data"),
	[main.s_file, "dynlist.s"],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[main.s_str, str_face_dynlist],
	[main.s_write],
	s_data(0x801A83E0, 0x801A8404, 0x801B5FE0, 0x801B812C, 0, 0, "dynlist.data", ["sm64"], [
	], [
		[0, 1,  8, "str"],
		[0, 1, 36, "str"],
		[0, 1, 32, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1, 44, "str"],
		[0, 1, 28, "str"],
		[0, 1,  8, "str"],
		[0, 1, 44, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1, 56, "str"],
		[0, 1, 32, "str"],
		[0, 1, 40, "str"],
		[0, 1,  4, "str"],
		[0, 1, 40, "str"],
		[0, 1, 32, "str"],
		[0, 1, 36, "str"],
		[0, 1, 32, "str"],
		[0, 1, 52, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 12, "str"],
		[0, 1, 52, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 20, "str"],
		[0, 1, 32, "str"],
		[0, 1, 36, "str"],
		[0, 1, 32, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 24, "str"],
		[0, 1, 24, "str"],
		[0, 1, 32, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 40, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 40, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 40, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 40, "str"],
		[0, 1, 52, "str"],
		[0, 1, 20, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 20, "str"],
		[0, 1, 40, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 32, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 20, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 20, "str"],
		[0, 1, 56, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 20, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1,  8, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 32, "str"],
		[0, 1, 52, "str"],
		[0, 1, 32, "str"],
		[0, 1, 52, "str"],
		[0, 1, 32, "str"],
		[0, 1, 52, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 28, "str"],
		[0, 1, 12, "str"],
		[0, 1, 52, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 12, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 20, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 16, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 20, "str"],
		[0, 1, 36, "str"],
		[0, 1, 52, "str"],
		[0, 1, 20, "str"],
		[0, -75, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 1, ultra.c.d_f32],
		[0, -73, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x801A8410, 0x801A8410, 0x801B8130, 0x801B82F0, 0, 0, "gadget.data", ["sm64"], [], [
		[0, 1,  24, "str"],
		[0, 1,  16, "str"],
		[0, 1,  12, "str"],
		[0, 1,  24, "str"],
		[0, 1,  76, "str"],
		[0, 1, 120, "str"],
		[0, 1,  24, "str"],
		[0, 1,  16, "str"],
		[0, 1,  24, "str"],
		[0, 1,  16, "str"],
		[0, 1,  36, "str"],
		[0, 1,  24, "str"],
		[0, 1,  16, "str"],
		[0, 1, 4, None],
		[0, 2, 1, ultra.c.d_f64],
	]),
	s_databin(0x801A8410, 0x801A8454, "stdio.data"),
	[main.s_file, "stdio.s"],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[main.s_str, str_face_stdio],
	[main.s_write],
	s_data(0x801A8410, 0x801A8454, 0x801B82F0, 0x801B85B0, 0, 0, "stdio.data", ["sm64"], [
	], [
		[0, 1, 32, "str"],
		[0, 1, 28, "str"],
		[0, 1,  4, "str"],
		[0, 1, 24, "str"],
		[0, 1, 28, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 24, "str"],
		[0, 1, 56, "str"],
		[0, 1, 44, "str"],
		[0, 1, 44, "str"],
		[0, 1, 12, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1, 28, "str"],
		[0, 1,  8, "str"],
		[0, 1, 40, "str"],
		[0, 1, 28, "str"],
		[0, 1, 12, "str"],
		[0, 1, 28, "str"],
		[0, 1, 32, "str"],
		[0, 1, 40, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, -22, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
	]),
	s_databin(0x801A8460, 0x801A8468, "joint.data"),
	[main.s_file, "joint.s"],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[main.s_str, str_face_joint],
	[main.s_write],
	s_data(0x801A8460, 0x801A8468, 0x801B85B0, 0x801B8730, 0, 0, "joint.data", ["sm64"], [
	], [
		[0, 1, 48, "str"],
		[0, 1, 16, "str"],
		[0, 1,  4, "str"],
		[0, 1, 20, "str"],
		[0, 1,  4, "str"],
		[0, 1, 16, "str"],
		[0, 1, 32, "str"],
		[0, 1, 28, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1, 32, "str"],
		[0, 1, 32, "str"],
		[0, 1, 4, None],
		[0, 6, 1, ultra.c.d_f64],
		[0, 2, 1, ultra.c.d_f32],
		[0, 8, 1, ultra.c.d_f64],
	]),
	s_data(0x801A8470, 0x801A8470, 0x801B8730, 0x801B8964, 0, 0, "net.data", ["sm64"], [], [
		[0, 1, 16, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 40, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1,  8, "str"],
		[0, 1, 20, "str"],
		[0, 1, 16, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 20, "str"],
		[0,  3, 1, ultra.c.d_f64],
		[0, -7, 1, ultra.c.d_addr, ultra.A_EXTERN],
	]),
	s_data(0x801A8470, 0x801A8470, 0x801B8970, 0x801B8A60, 0, 0, "math.data", ["sm64"], [], [
		[0, 1, 32, "str"],
		[0, 1, 36, "str"],
		[0, 1, 12, "str"],
		[0, 1,  4, "str"],
		[0, 1, 28, "str"],
		[0, 1, 28, "str"],
		[0, 1, 28, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 5, 1, ultra.c.d_f32],
		[0, 4, 1, ultra.c.d_f64],
	]),
	s_databin(0x801A8470, 0x801A8800, "shape.data"),
	[main.s_file, "shape.s"],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[main.s_str, str_face_shape],
	[main.s_write],
	s_data(0x801A8470, 0x801A8800, 0x801B8A60, 0x801B8E28, 0, 0, "shape.data", ["sm64"], [
	], [
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 16, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 28, "str"],
		[0, 1,  8, "str"],
		[0, 1, 28, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1, 16, "str"],
		[0, 1, 28, "str"],
		[0, 1, 32, "str"],
		[0, 1, 36, "str"],
		[0, 1, 32, "str"],
		[0, 1, 32, "str"],
		[0, 1, 32, "str"],
		[0, 1, 32, "str"],
		[0, 1, 32, "str"],
		[0, 1, 32, "str"],
		[0, 1, 32, "str"],
		[0, 1,  4, "str"],
		[0, 1, 24, "str"],
		[0, 1, 32, "str"],
		[0, 1, 16, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1, 24, "str"],
		[0, 1,  8, "str"],
		[0, 1, 20, "str"],
		[0, 1, 16, "str"],
		[0, 1,  4, "str"],
		[0, 1,  8, "str"],
		[0, 1, 28, "str"],
		[0, 1, 36, "str"],
		[0, 1, 12, "str"],
		[0, 1,  4, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 16, "str"],
		[0, 1,  8, "str"],
		[0, -8, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  5, 1, ultra.c.d_f32],
	]),
	s_databin(0x801A8800, 0x801B54B8, "gfx.data"),
	[main.s_file, "gfx.s"],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[main.s_str, str_face_gfx],
	[main.s_write],
	s_data(0x801A8800, 0x801B54B8, 0x801B8E30, 0x801B99E0, 0, 0, "gfx.data", ["sm64"], [
	], [
		[0, 1,  4, "str"],
		[0, 1, 48, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, 1, 16, "str"],
		[0, 1,  8, "str"],
		[0, 1, 52, "str"],
		[0, 1, 48, "str"],
		[0, 1,  8, "str"],
		[0, 1, 48, "str"],
		[0, 1, 44, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 16, "str"],
		[0, 1, 16, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 12, "str"],
		[0, 1, 16, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1, 16, "str"],
		[0, 1,  8, "str"],
		[0, 1, 16, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 32, "str"],
		[0, 1,  4, "str"],
		[0, 1,  8, "str"],
		[0, 1, 40, "str"],
		[0, 1, 12, "str"],
		[0, 1, 40, "str"],
		[0, 1, 12, "str"],
		[0, 1, 40, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 24, "str"],
		[0, 1, 36, "str"],
		[0, 1, 16, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 32, "str"],
		[0, 1, 16, "str"],
		[0, 1, 56, "str"],
		[0, 1, 48, "str"],
		[0, 1, 40, "str"],
		[0, 1, 24, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, 1, 36, "str"],
		[0, 1, 36, "str"],
		[0, 1, 20, "str"],
		[0, 1, 20, "str"],
		[0, 1, 36, "str"],
		[0, 1,  8, "str"],
		[0, 1, 36, "str"],
		[0, 1,  8, "str"],
		[0, 1, 32, "str"],
		[0, 1, 28, "str"],
		[0, 1, 28, "str"],
		[0, 1, 32, "str"],
		[0, 1,  4, "str"],
		[0, 1, 20, "str"],
		[0, 1, 36, "str"],
		[0, 1, 32, "str"],
		[0, 1, 40, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1,  4, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  4, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1,  8, "str"],
		[0, 1, 12, "str"],
		[0, 1, 44, "str"],
		[0, 1, 28, "str"],
		[0, 1, 36, "str"],
		[0, 1, 32, "str"],
		[0, 1, 24, "str"],
		[0, 1, 28, "str"],
		[0, 1,  8, "str"],
		[0, 1, 24, "str"],
		[0,   1, 1, ultra.c.d_f64],
		[0, -34, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,  16, 1, ultra.c.d_f64],
		[0, -19, 1, ultra.c.d_addr, ultra.A_EXTERN],
		[0,   1, 4, None],
		[0,   1, 1, ultra.c.d_f64],
	]),

	[main.s_file, "bss.s"],
		[main.s_str, "\n"],
		[main.s_str, str_bss],
		[main.s_str, str_align],
		[main.s_str, "\n"],
		[main.s_str, str_face_bss],
	[main.s_write],
]

data_gfx = [
	s_include(["sm64"]),
	[main.s_str, "\n"],
	s_dirfile(os.path.join("gfx", "dprint"), "texture.c"),
		[ultra.c.s_data, 0x02000000, 0x02004A00, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, name]
			for name in list("0123456789abcdefghiklmnoprstuwy") + [
				"squote",
				"dquote",
				"multiply",
				"coin",
				"mario",
				"star",
			]
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "staff"), "texture.c"),
		[ultra.c.s_data, 0x02004A00, 0x02005900, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 8, 8, name]
			for name in list("346abcdefghijklmnopqrstuvwxyz") + ["period"]
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "message"), "texture.c"),
		[ultra.c.s_data, 0x02005900, 0x02007000, "E0.szp", [
			[0, 1, 1, c.d_texture, "ia4", 16, 8, name]
			for name in list("0123456789") + [
				"u_"+x for x in "abcdefghijklmnopqrstuvwxyz"
			] + [
				"l_"+x for x in "abcdefghijklmnopqrstuvwxyz"
			] + [
				"arrow",
				"exclaim",
				"coin",
				"multiply",
				"paren_l",
				"paren_rl",
				"paren_r",
				"tilde",
				"period",
				"percent",
				"bullet",
				"comma",
				"apostrophe",
				"question",
				"star",
				"star_outline",
				"quote_l",
				"quote_r",
				"colon",
				"hyphen",
				"ampersand",
				"button_a",
				"button_b",
				"button_c",
				"button_z",
				"button_r",
				"button_cu",
				"button_cd",
				"button_cl",
				"button_cr",
			]
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "camera"), "texture.c"),
		[ultra.c.s_data, 0x02007000, 0x02007700, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, "camera"],
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, "lakitu"],
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, "cross"],
			[0, 1, 1, c.d_texture, "rgba16",  8,  8, "up"],
			[0, 1, 1, c.d_texture, "rgba16",  8,  8, "down"],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "dprint"), "table.c"),
		[ultra.c.s_data, 0x02007700, 0x020077E8, "E0.szp", [
			[0, -58, 1, ultra.c.d_addr, 0],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "message"), "table.c"),
		[ultra.c.s_data, 0x020077E8, 0x02007BE8, "E0.szp", [
			[0, -0x100, 1, ultra.c.d_addr, 0],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "staff"), "table.c"),
		[ultra.c.s_data, 0x02007BE8, 0x02007C7C, "E0.szp", [
			[0, -37, 1, ultra.c.d_addr, 0],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "camera"), "table.c"),
		[ultra.c.s_data, 0x02007C7C, 0x02007C94, "E0.szp", [
			[0, -6, 1, ultra.c.d_addr, 0],
		]],
	s_writepop(),
	[main.s_str, "\n"],
	[c.s_message, 0x02007D28, 0x02007D34, "E0.szp", "msg", "select", "select", "jp"],
	[c.s_message, 0x02010A68, 0x02010D14, "E0.szp", "msg", "en_us",  "table",  "en.m"],
	[c.s_message, 0x02010F68, 0x02010FD4, "E0.szp", "tbl", "course", "course", "en.m"],
	[c.s_message, 0x0201192C, 0x02011AB4, "E0.szp", "tbl", "level",  "level",  "en.m"],
	[main.s_str, "\n"],
	[ultra.c.s_data, 0x02011AB8, 0x02011AC0, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	[main.s_str, "\n"],
	s_dirfile(os.path.join("gfx", "dprint"), "gfx.c"),
		[ultra.c.s_data, 0x02011AC0, 0x02011C08, "E0.szp", [
			[0, 1, 1, ultra.c.d_Gfx, 0x02011C08],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "message"), "gfx.c"),
		[ultra.c.s_data, 0x02011C08, 0x02011E10, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			[0,  1, 1, ultra.c.d_Gfx, 0x02011C88],
			[0, -4, 1, ultra.c.d_Vtx, False],
			[0,  1, 1, ultra.c.d_Gfx, 0x02011D90],
			[0, -3, 1, ultra.c.d_Vtx, False],
			[0,  1, 1, ultra.c.d_Gfx, 0x02011E10],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "number"), "gfx.c"),
		[ultra.c.s_data, 0x02011E10, 0x020120B8, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			[0,  1, 1, ultra.c.d_Gfx, 0x020120B8],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "shadow"), "texture.c"),
		[ultra.c.s_data, 0x020120B8, 0x020122B8, "E0.szp", [
			[0, 1, 1, c.d_texture, "ia8", 16, 16, "circle"],
			[0, 1, 1, c.d_texture, "ia8", 16, 16, "square"],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "wipe"), "texture.c"),
		[ultra.c.s_data, 0x020122B8, 0x02014AB8, "E0.szp", [
			[0, 1, 1, c.d_texture, "ia8", 32, 64, "star"],
			[0, 1, 1, c.d_texture, "ia8", 32, 64, "circle"],
			[0, 1, 1, c.d_texture, "ia8", 64, 64, "mario"],
			[0, 1, 1, c.d_texture, "ia8", 32, 64, "bowser"],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "scroll"), "texture.c"),
		[ultra.c.s_data, 0x02014AB8, 0x020172B8, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "water_0"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "water_1"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "water_2"],
			[0, 1, 1, c.d_texture, "ia16",   32, 32, "mist"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "lava"],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x020172B8, 0x02017380, "E0.szp", [
		[0, 1, 1, ultra.c.d_Lights1],
		[0, 2, 1, c.d_matrix],
		[0, 1, 1, ultra.c.d_Gfx, 0x02017380],
	]],
	s_dirfile(os.path.join("gfx", "shadow"), "gfx.c"),
		[ultra.c.s_data, 0x02017380, 0x020174C0, "E0.szp", [
			[0, 1, 1, ultra.c.d_Gfx, 0x020174C0],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "wipe"), "gfx.c"),
		[ultra.c.s_data, 0x020174C0, 0x02017568, "E0.szp", [
			[0, 1, 1, ultra.c.d_Gfx, 0x02017568],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "back"), "gfx.c"),
		[ultra.c.s_data, 0x02017568, 0x020175F0, "E0.szp", [
			[0, 1, 1, ultra.c.d_Gfx, 0x020175F0],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "scroll"), "gfx.c"),
		[ultra.c.s_data, 0x020175F0, 0x02017698, "E0.szp", [
			[0, 1, 1, ultra.c.d_Gfx, 0x02017698],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "minimap"), "gfx.c"),
		[ultra.c.s_data, 0x02017698, 0x020177B8, "E0.szp", [
			[0, 1, 1, c.d_texture, "ia8", 8, 8, "arrow"],
			[0, 1, 1, ultra.c.d_Gfx, 0x020177B8],
		]],
	s_writepop(),
	s_dirfile(os.path.join("gfx", "wave"), "gfx.c"),
		[ultra.c.s_data, 0x020177B8, 0x02018A0E, "E0.szp", [
			[0, 1, 1, ultra.c.d_Lights1],
			[0, 1, 1, ultra.c.d_Gfx, 0x020178C0],
			[0, 2, 1, c.d_wave_shape],
			[0, 1, 2, None],
			[0, 1, 1, c.d_wave_shade, 0x02018A0E],
		]],
	s_writepop(),
]

player_gfx = [
	s_dirfile("mario", "gfx.c"),
		[c.s_gltf, "mario", [
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
		[ultra.c.s_data, 0x04000000, 0x0400C090, "E0.szp", [
			[0, -6, 1, c.d_light, 0.5],
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "metal"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "button"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "logo"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "sideburn"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "moustache"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "eyes_open"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "eyes_half"],
			[0, 3, 1, c.d_texture, "rgba16", 32, 32, "eyes_closed"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "eyes_left"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "eyes_right"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "eyes_up"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "eyes_down"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "eyes_dead"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "wing_l"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "wing_r"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "metal_wing_l"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "metal_wing_r"],
		]],
		[c.s_gltf_mesh, "h_waist", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x0400CA00, 0x0400CD40, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400CD40, "h_waist", 0],
		]],
		[c.s_gltf_mesh, "h_uarmL", [
			(True, "red"),
		]],
		[ultra.c.s_data, 0x0400D090, 0x0400D1F8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400D1F8, "h_uarmL", 0],
		]],
		[c.s_gltf_mesh, "h_larmL", [
			(True, "red"),
		]],
		[ultra.c.s_data, 0x0400D2F8, 0x0400D3E8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400D3E8, "h_larmL", 0],
		]],
		[c.s_gltf_mesh, "h_fistL", [
			(True, "white"),
		]],
		[ultra.c.s_data, 0x0400D758, 0x0400D910, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400D910, "h_fistL", 0],
		]],
		[c.s_gltf_mesh, "h_uarmR", [
			(True, "red"),
		]],
		[ultra.c.s_data, 0x0400DCA0, 0x0400DE08, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400DE08, "h_uarmR", 0],
		]],
		[c.s_gltf_mesh, "h_larmR", [
			(True, "red"),
		]],
		[ultra.c.s_data, 0x0400DF08, 0x0400DFF8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400DFF8, "h_larmR", 0],
		]],
		[c.s_gltf_mesh, "h_fistR", [
			(True, "white"),
		]],
		[ultra.c.s_data, 0x0400E2C8, 0x0400E4A8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400E4A8, "h_fistR", 0],
		]],
		[c.s_gltf_mesh, "h_thighL", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x0400E6A8, 0x0400E858, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400E858, "h_thighL", 0],
		]],
		[c.s_gltf_mesh, "h_shinL", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x0400E918, 0x0400E9C8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400E9C8, "h_shinL", 0],
		]],
		[c.s_gltf_mesh, "h_shoeL", [
			(True, "shoe"),
		]],
		[ultra.c.s_data, 0x0400EBB8, 0x0400ECC0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400ECC0, "h_shoeL", 0],
		]],
		[c.s_gltf_mesh, "h_thighR", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x0400EEB0, 0x0400EFD8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400EFD8, "h_thighR", 0],
		]],
		[c.s_gltf_mesh, "h_shinR", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x0400F1D8, 0x0400F290, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400F290, "h_shinR", 0],
		]],
		[c.s_gltf_mesh, "h_shoeR", [
			(True, "shoe"),
		]],
		[ultra.c.s_data, 0x0400F400, 0x0400F568, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0400F568, "h_shoeR", 0],
		]],
		[c.s_gltf_mesh, "h_torso", [
			(True, "button"),
			(True, "blue"),
			(True, "red"),
		]],
		[ultra.c.s_data, 0x0400FF28, 0x04010410, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04010410, "h_torso", 0, 2, 1],
		]],
		[c.s_gltf_mesh, "h_cap", [
			(True, "logo"),
			(True, "eyes"),
			(True, "sideburn"),
			(True, "moustache"),
			(True, "red"),
			(True, "skin"),
			(True, "hair"),
		]],
		[ultra.c.s_data, 0x040112B0, 0x04012190, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04012160, "h_cap", 0, 1, 2, 3, 5, 4, 6],
			[0, -2, 1, c.d_light, 0.25],
		]],
		[c.s_gltf_mesh, "h_hair", [
			(True, "eyes"),
			(True, "sideburn"),
			(True, "moustache"),
			(True, "skin"),
			(True, "hair"),
		]],
		[c.s_gltf_mesh, "h_hair.001", [
			(True, "skin"),
		]],
		[ultra.c.s_data, 0x040132B0, 0x04014098, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x040136B8, "h_hair", 0, 2, 1, 3],
			[0, 1, 1, c.d_gfx, 0x04014098,
				"h_hair.001", 0,
				"h_hair", 4,
			],
		]],
		[c.s_gltf_mesh, "m_waist", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x040144D8, 0x040146E0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x040146E0, "m_waist", 0],
		]],
		[c.s_gltf_mesh, "m_uarmL", [
			(True, "red"),
		]],
		[ultra.c.s_data, 0x040147D0, 0x04014860, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04014860, "m_uarmL", 0],
		]],
		[c.s_gltf_mesh, "m_larmL", [
			(True, "red"),
		]],
		[ultra.c.s_data, 0x04014950, 0x040149C0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x040149C0, "m_larmL", 0],
		]],
		[c.s_gltf_mesh, "m_fistL", [
			(True, "white"),
		]],
		[ultra.c.s_data, 0x04014C90, 0x04014DE0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04014DE0, "m_fistL", 0],
		]],
		[c.s_gltf_mesh, "m_uarmR", [
			(True, "red"),
		]],
		[ultra.c.s_data, 0x04014ED0, 0x04014F60, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04014F60, "m_uarmR", 0],
		]],
		[c.s_gltf_mesh, "m_larmR", [
			(True, "red"),
		]],
		[ultra.c.s_data, 0x04015050, 0x040150C0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x040150C0, "m_larmR", 0],
		]],
		[c.s_gltf_mesh, "m_fistR", [
			(True, "white"),
		]],
		[ultra.c.s_data, 0x040153B0, 0x04015530, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04015530, "m_fistR", 0],
		]],
		[c.s_gltf_mesh, "m_thighL", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x04015620, 0x04015758, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04015758, "m_thighL", 0],
		]],
		[c.s_gltf_mesh, "m_shinL", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x04015848, 0x040158D8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x040158D8, "m_shinL", 0],
		]],
		[c.s_gltf_mesh, "m_shoeL", [
			(True, "shoe"),
		]],
		[ultra.c.s_data, 0x04015A98, 0x04015B80, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04015B80, "m_shoeL", 0],
		]],
		[c.s_gltf_mesh, "m_thighR", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x04015C70, 0x04015D20, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04015D20, "m_thighR", 0],
		]],
		[c.s_gltf_mesh, "m_shinR", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x04015E10, 0x04015EA0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04015EA0, "m_shinR", 0],
		]],
		[c.s_gltf_mesh, "m_shoeR", [
			(True, "shoe"),
		]],
		[ultra.c.s_data, 0x04016000, 0x04016148, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04016148, "m_shoeR", 0],
		]],
		[c.s_gltf_mesh, "m_torso", [
			(True, "button"),
			(True, "red"),
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x04016668, 0x04016968, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04016968, "m_torso", 0, 2, 1],
		]],
		[c.s_gltf_mesh, "l_waist", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x04016A18, 0x04016B60, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04016B60, "l_waist", 0],
		]],
		[c.s_gltf_mesh, "l_uarmL", [
			(True, "red"),
		]],
		[ultra.c.s_data, 0x04016C20, 0x04016C90, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04016C90, "l_uarmL", 0],
		]],
		[c.s_gltf_mesh, "l_larmL", [
			(True, "red"),
		]],
		[ultra.c.s_data, 0x04016D50, 0x04016DA0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04016DA0, "l_larmL", 0],
		]],
		[c.s_gltf_mesh, "l_fistL", [
			(True, "white"),
		]],
		[ultra.c.s_data, 0x04016E20, 0x04016EA0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04016EA0, "l_fistL", 0],
		]],
		[c.s_gltf_mesh, "l_uarmR", [
			(True, "red"),
		]],
		[ultra.c.s_data, 0x04016F60, 0x04016FD0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04016FD0, "l_uarmR", 0],
		]],
		[c.s_gltf_mesh, "l_larmR", [
			(True, "red"),
		]],
		[ultra.c.s_data, 0x04017090, 0x040170E0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x040170E0, "l_larmR", 0],
		]],
		[c.s_gltf_mesh, "l_fistR", [
			(True, "white"),
		]],
		[ultra.c.s_data, 0x04017160, 0x04017210, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04017210, "l_fistR", 0],
		]],
		[c.s_gltf_mesh, "l_thighL", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x040172F0, 0x04017408, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04017408, "l_thighL", 0],
		]],
		[c.s_gltf_mesh, "l_shinL", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x040174E8, 0x04017558, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04017558, "l_shinL", 0],
		]],
		[c.s_gltf_mesh, "l_shoeL", [
			(True, "shoe"),
		]],
		[ultra.c.s_data, 0x04017638, 0x040176C8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x040176C8, "l_shoeL", 0],
		]],
		[c.s_gltf_mesh, "l_thighR", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x040177A8, 0x04017838, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04017838, "l_thighR", 0],
		]],
		[c.s_gltf_mesh, "l_shinR", [
			(True, "blue"),
		]],
		[ultra.c.s_data, 0x04017918, 0x04017988, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04017988, "l_shinR", 0],
		]],
		[c.s_gltf_mesh, "l_shoeR", [
			(True, "shoe"),
		]],
		[ultra.c.s_data, 0x04017A68, 0x04017B58, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04017B58, "l_shoeR", 0],
		]],
		[c.s_gltf_mesh, "l_torso", [
			(True, "button"),
			(True, "blue"),
			(True, "red"),
		]],
		[ultra.c.s_data, 0x04017D68, 0x04017F40, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04017F40, "l_torso", 0, 1, 2],
		]],
		[c.s_gltf_mesh, "l_cap", [
			(True, "logo"),
			(True, "eyes"),
			(True, "moustache"),
			(True, "red"),
			(True, "skin"),
			(True, "hair"),
		]],
		[ultra.c.s_data, 0x04018270, 0x04018B18, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04018B18, "l_cap", 0, 1, 2, 4, 3, 5],
		]],
		[c.s_gltf_mesh, "l_hair", [
			(True, "eyes"),
			(True, "moustache"),
			(True, "skin"),
			(True, "hair"),
		]],
		[ultra.c.s_data, 0x04018DC8, 0x04019538, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04019538, "l_hair", 0, 1, 2, 3],
		]],
		[c.s_gltf_mesh, "handL", [
			(True, "white"),
		]],
		[ultra.c.s_data, 0x04019A68, 0x04019CC0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x04019CC0, "handL", 0],
		]],
		[c.s_gltf_mesh, "handR", [
			(True, "white"),
		]],
		[ultra.c.s_data, 0x0401A1F0, 0x0401A478, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0401A478, "handR", 0],
		]],
		[c.s_gltf_mesh, "capR", [
			(True, "logo"),
			(True, "white"),
			(True, "red"),
			(True, "hair"),
		]],
		[ultra.c.s_data, 0x0401ABA8, 0x0401AF60, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0401AF60, "capR", 0, 2, 1, 3],
		]],
		[c.s_gltf_mesh, "wingsR", [
			(True, "wing_l"),
			(True, "wing_r"),
		]],
		[ultra.c.s_data, 0x0401B080, 0x0401B2D0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0401B2D0, "wingsR", 0, 1],
		]],
		[c.s_gltf_mesh, "peaceR", [
			(True, "white"),
		]],
		[ultra.c.s_data, 0x0401BC80, 0x0401BF50, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0401BF50, "peaceR", 0],
		]],
		[c.s_gltf_mesh, "cap", [
			(True, "logo"),
			(True, "red"),
			(True, "hair"),
		]],
		[ultra.c.s_data, 0x0401C330, 0x0401C538, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0401C538, "cap", 0, 1, 2],
		]],
		[c.s_gltf_mesh, "wings", [
			(True, "wing_l"),
			(True, "wing_r"),
		]],
		[ultra.c.s_data, 0x0401C678, 0x0401C940, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0401C940, "wings", 0, 1],
		]],
		[c.s_gltf_mesh, "wing", [
			(True, "wing_l"),
			(True, "wing_r"),
		]],
		[ultra.c.s_data, 0x0401C9C0, 0x0401CD20, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0401CD20, "wing", 0, 1],
		]],
		[c.s_gltf_write],
	s_writepop(),
	s_dirfile("bubble", "gfx.c"),
		[ultra.c.s_data, 0x0401CD20, 0x0401DE60, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "a"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "b"],
			[0, 1, 1, ultra.c.d_Gfx, 0x0401DE60],
		]],
	s_writepop(),
	s_dirfile("dust", "gfx.c"),
		[ultra.c.s_data, 0x0401DE60, 0x040217C0, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			d_texture_n("ia16", 32, 32, 7),
			[0, 1, 1, ultra.c.d_Gfx, 0x040217C0],
		]],
	s_writepop(),
	s_dirfile("smoke", "gfx.c"),
		[ultra.c.s_data, 0x040217C0, 0x040220C8, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, c.d_texture, "ia16", 32, 32, "smoke"],
			[0, 1, 1, ultra.c.d_Gfx, 0x040220C8],
		]],
	s_writepop(),
	s_dirfile("wave", "gfx.c"),
		[ultra.c.s_data, 0x040220C8, 0x04025318, "E0.szp", [
			[0, -8, 1, ultra.c.d_Vtx, False],
			d_texture_n("ia16", 32, 32, 6),
			[0, 1, 1, ultra.c.d_Gfx, 0x04025318],
		]],
	s_writepop(),
	s_dirfile("ripple", "gfx.c"),
		[ultra.c.s_data, 0x04025318, 0x04027450, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			d_texture_n("ia16", 32, 32, 4),
			[0, 1, 1, ultra.c.d_Gfx, 0x04027450],
		]],
	s_writepop(),
	s_dirfile("sparkle", "gfx.c"),
		[ultra.c.s_data, 0x04027450, 0x0402A588, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, True],
			d_texture_n("rgba16", 32, 32, -1, start=5, step=-1),
			[0, 1, 1, ultra.c.d_Gfx, 0x0402A588],
		]],
	s_writepop(),
	s_dirfile("splash", "gfx.c"),
		[ultra.c.s_data, 0x0402A588, 0x04032700, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			d_texture_n("rgba16", 32, 64, 8),
			[0, 1, 1, ultra.c.d_Gfx, 0x04032700],
		]],
	s_writepop(),
	s_dirfile("droplet", "gfx.c"),
		[ultra.c.s_data, 0x04032700, 0x04032A48, "E0.szp", [
			[0, -8, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, "droplet"],
			[0, 1, 1, ultra.c.d_Gfx, 0x04032A48],
		]],
	s_writepop(),
	s_dirfile("glow", "gfx.c"),
		[ultra.c.s_data, 0x04032A48, 0x04035378, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			d_texture_n("ia16", 32, 32, 5),
			[0, 1, 1, ultra.c.d_Gfx, 0x04035378],
		]],
	s_writepop(),
]

player_shape = [
	s_dirfile("bubble", "shape.c"),
		[ultra.c.s_data, 0x17000000, 0x17000038, "E0", [
			[0, 1, 1, c.d_s_script, 0x17000038],
		]],
	s_writepop(),
	s_dirfile("dust", "shape.c"),
		[ultra.c.s_data, 0x17000038, 0x17000084, "E0", [
			[0, 1, 1, c.d_s_script, 0x17000084],
		]],
	s_writepop(),
	s_dirfile("smoke", "shape.c"),
		[ultra.c.s_data, 0x17000084, 0x1700009C, "E0", [
			[0, 1, 1, c.d_s_script, 0x1700009C],
		]],
	s_writepop(),
	s_dirfile("wave", "shape.c"),
		[ultra.c.s_data, 0x1700009C, 0x17000124, "E0", [
			[0, 1, 1, c.d_s_script, 0x17000124],
		]],
	s_writepop(),
	s_dirfile("ripple", "shape.c"),
		[ultra.c.s_data, 0x17000124, 0x170001BC, "E0", [
			[0, 1, 1, c.d_s_script, 0x170001BC],
		]],
	s_writepop(),
	s_dirfile("sparkle", "shape.c"),
		[ultra.c.s_data, 0x170001BC, 0x17000230, "E0", [
			[0, 1, 1, c.d_s_script, 0x17000230],
		]],
	s_writepop(),
	s_dirfile("splash", "shape.c"),
		[ultra.c.s_data, 0x17000230, 0x17000284, "E0", [
			[0, 1, 1, c.d_s_script, 0x17000284],
		]],
	s_writepop(),
	s_dirfile("droplet", "shape.c"),
	s_writepop(),
	s_dirfile("glow", "shape.c"),
		[ultra.c.s_data, 0x17000284, 0x170002E0, "E0", [
			[0, 1, 1, c.d_s_script, 0x170002E0],
		]],
	s_writepop(),
	s_dirfile("mario", "shape.c"),
		[ultra.c.s_data, 0x170002E0, 0x17002E30, "E0", [
			[0, 1, 1, c.d_s_script, 0x17002E30],
		]],
	s_writepop(),
]

shape_1b_gfx = [
	s_dirfile("bully", "gfx.c"),
		[c.s_gltf, "bully", [
			("horn", None, ("horn.rgba16.png", 16, 16)),
			("shoe", (0.25, 0x00, 0xE3, 0x00)),
			("eye_old", (0.25, 0xFF, 0xFF, 0xFF), ("eye.rgba16.png", 32, 32)),
			("body_old", (0.25, 0x00, 0x00, 0x00)),
			("body_l", None, ("body_l.rgba16.png", 32, 64)),
			("body_r", None, ("body_r.rgba16.png", 32, 64)),
			("eye", None, ("eye.rgba16.png", 32, 32)),
		]],
		[c.s_gltf_mesh, "horn", [
			(False, "horn"),
		]],
		[ultra.c.s_data, 0x050000E0, 0x05002C68, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, "horn"],
			[0, 1, 1, c.d_gfx, 0x05000408, "horn", 0],
			[0, -4, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "body_l"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "body_r"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "eye"],
		]],
		[c.s_gltf_mesh, "shoeL", [
			(True, "shoe"),
		]],
		[c.s_gltf_mesh, "shoeR", [
			(True, "shoe"),
		]],
		[c.s_gltf_mesh, "eyes_old", [
			(True, "eye_old"),
		]],
		[c.s_gltf_mesh, "body_old", [
			(True, "body_old"),
		]],
		[ultra.c.s_data, 0x05003708, 0x05003C50, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x05003C50,
				"shoeL", 0,
				"shoeR", 0,
				"eyes_old", 0,
				"body_old", 0,
			],
		]],
		[c.s_gltf_mesh, "body", [
			(False, "body_l"),
			(False, "body_r"),
		]],
		[ultra.c.s_data, 0x05003CD0, 0x05003DB8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x05003DB8, "body", 0, 1],
		]],
		[c.s_gltf_mesh, "body_big", [
			(False, "body_l"),
			(False, "body_r"),
		]],
		[ultra.c.s_data, 0x05003E38, 0x05003F20, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x05003F20, "body_big", 0, 1],
		]],
		[c.s_gltf_mesh, "eyes", [
			(False, "eye"),
		]],
		[ultra.c.s_data, 0x05003F80, 0x05004720, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x05004038, "eyes", 0],
			[0, 1, 1, c.d_anime, 0x050042A4],
			[0, 1, 1, c.d_anime, 0x050043D8],
			[0, 1, 1, c.d_anime, 0x05004598],
			[0, 1, 1, c.d_anime, 0x050046F4],
			[0, -4, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x05004720, 0x05004728, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("blargg", "gfx.c"),
		[c.s_gltf, "blargg", [
			("upper_jaw", (0.25, 0xFF, 0x36, 0x16)),
			("teeth", (0.25, 0xB2, 0xB2, 0xB2)),
			("lower_jaw", (0.25, 0xFF, 0x2A, 0x1A)),
			("body", (0.25, 0xFF, 0x2E, 0x1F)),
		]],
		[ultra.c.s_data, 0x05004728, 0x050047A0, "E0.szp", [
			[0, -5, 1, c.d_light, 0.25],
		]],
		[c.s_gltf_mesh, "upper_jaw", [
			(True, "teeth"),
			(True, "upper_jaw"),
		]],
		[c.s_gltf_mesh, "lower_jaw", [
			(True, "teeth"),
			(True, "lower_jaw"),
		]],
		[c.s_gltf_mesh, "body", [
			(True, "body"),
		]],
		[ultra.c.s_data, 0x050058D0, 0x05006178, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x05005EB8,
				"upper_jaw", 0, 1,
				"lower_jaw", 0, 1,
				"body", 0,
			],
			[0, 1, 1, c.d_anime, 0x05006070],
			[0, 1, 1, c.d_anime, 0x05006154],
			[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x05006178, 0x05006180, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
]

shape_1b_shape = [
	s_dirfile("bully", "shape.c"),
		[ultra.c.s_data, 0x0C000000, 0x0C000240, "E0", [
			[0, 1, 1, c.d_s_script, 0x0C000240],
		]],
	s_writepop(),
	s_dirfile("blargg", "shape.c"),
		[ultra.c.s_data, 0x0C000240, 0x0C0002B0, "E0", [
			[0, 1, 1, c.d_s_script, 0x0C0002B0],
		]],
	s_writepop(),
]

shape_2b_gfx = [
	s_dirfile("skeeter", "gfx.c"),
		[c.s_gltf, "skeeter", [
			("sphere", None, ("sphere.rgba16.png", 32, 32)),
			("iris", None, ("iris.rgba16.png", 16, 8)),
			("foot", (0.5, 0xFF, 0xAA, 0x00)),
			("shade", None),
		]],
		[ultra.c.s_data, 0x06000000, 0x06000990, "E0.szp", [
			[0, -6, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "sphere"],
			[0, 1, 1, c.d_texture, "rgba16", 16, 8, "iris"],
		]],
		[c.s_gltf_mesh, "body", [
			(False, "sphere"),
		]],
		[ultra.c.s_data, 0x060009D0, 0x06000A78, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06000A78, "body", 0],
		]],
		[c.s_gltf_mesh, "tail_end", [
			(False, "sphere"),
		]],
		[ultra.c.s_data, 0x06000AB8, 0x06000B60, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06000B60, "tail_end", 0],
		]],
		[c.s_gltf_mesh, "eye", [
			(False, "sphere"),
		]],
		[ultra.c.s_data, 0x06000BA0, 0x06000C48, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06000C48, "eye", 0],
		]],
		[c.s_gltf_mesh, "irisR", [
			(False, "iris"),
		]],
		[ultra.c.s_data, 0x06000C78, 0x06000D18, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06000D18, "irisR", 0],
		]],
		[c.s_gltf_mesh, "irisL", [
			(False, "iris"),
		]],
		[ultra.c.s_data, 0x06000D48, 0x06000E00, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06000DE8, "irisL", 0],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "foot", [
			(True, "foot"),
		]],
		[ultra.c.s_data, 0x06000E60, 0x06000EF0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06000EF0, "foot", 0],
		]],
		[c.s_gltf_mesh, "footBR_old", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "llegBR", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "ulegBR", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "footFR_old", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "llegFR", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "ulegFR", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "footFL_old", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "llegFL", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "ulegFL", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "eyeR_old", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "footBL_old", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "llegBL", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "ulegBL", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "eyeL_old", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "tail_end_old", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "tail", [
			(False, "shade"),
		]],
		[c.s_gltf_mesh, "body_old", [
			(False, "shade"),
		]],
		[ultra.c.s_data, 0x06003FF0, 0x06007DF0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06005720,
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
			[0, 1, 1, c.d_anime, 0x06005D44],
			[0, 1, 1, c.d_anime, 0x06006B70],
			[0, 1, 1, c.d_anime, 0x060071E0],
			[0, 1, 1, c.d_anime, 0x06007DC8],
			[0, -4, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x06007DF0, 0x06007DF8, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("kelp", "gfx.c"),
		[c.s_gltf, "kelp", [
			("0", (0.25, 0xFF, 0xFF, 0xFF), ("0.rgba16.png", 32, 32)),
			("1", (0.25, 0xFF, 0xFF, 0xFF), ("1.rgba16.png", 32, 32)),
			("2", (0.25, 0xFF, 0xFF, 0xFF), ("2.rgba16.png", 32, 32)),
			("3", (0.25, 0xFF, 0xFF, 0xFF), ("3.rgba16.png", 32, 32)),
		]],
		[ultra.c.s_data, 0x06007DF8, 0x06009E10, "E0.szp", [
			[0, -1, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "0"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "1"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "2"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "3"],
		]],
		[c.s_gltf_mesh, "0", [
			(True, "0"),
		]],
		[ultra.c.s_data, 0x06009E50, 0x06009F08, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06009F08, "0", 0],
		]],
		[c.s_gltf_mesh, "1", [
			(True, "1"),
		]],
		[ultra.c.s_data, 0x06009F48, 0x0600A000, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0600A000, "1", 0],
		]],
		[c.s_gltf_mesh, "2", [
			(True, "2"),
		]],
		[ultra.c.s_data, 0x0600A040, 0x0600A0F8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0600A0F8, "2", 0],
		]],
		[c.s_gltf_mesh, "3", [
			(True, "3"),
		]],
		[ultra.c.s_data, 0x0600A138, 0x0600A4D8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0600A1F0, "3", 0],
			[0, 1, 1, c.d_anime, 0x0600A4BC],
			[0, -1, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x0600A4D8, 0x0600A4E0, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("watermine", "gfx.c"),
		[c.s_gltf, "watermine", [
			("l", None, ("l.rgba16.png", 32, 64)),
			("r", None, ("r.rgba16.png", 32, 64)),
			("spike", (0.25, 0xFF, 0xFF, 0xFF), ("spike.rgba16.png", 32, 32)),
		]],
		[ultra.c.s_data, 0x0600A4E0, 0x0600CCF8, "E0.szp", [
			[0, -1, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "l"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "r"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "spike"],
		]],
		[c.s_gltf_mesh, "mine", [
			(False, "l"),
			(False, "r"),
		]],
		[c.s_gltf_mesh, "spike", [
			(True, "spike"),
		]],
		[ultra.c.s_data, 0x0600D1F8, 0x0600D458, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0600D458,
				"mine", 0, 1,
				"spike", 0,
			],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x0600D458, 0x0600D460, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("piranha", "gfx.c"),
		[c.s_gltf, "piranha", [
			("piranha", (0.5, 0xFF, 0xFF, 0xFF), ("piranha.rgba16.png", 32, 32)),
		]],
		[ultra.c.s_data, 0x0600D460, 0x0600DC80, "E0.szp", [
			[0, 1, 1, ultra.c.d_u64],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "piranha"],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "body", [
			(True, "piranha"),
		]],
		[ultra.c.s_data, 0x0600DD20, 0x0600DE50, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0600DE38, "body", 0],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "fin", [
			(True, "piranha"),
		]],
		[ultra.c.s_data, 0x0600DE90, 0x0600DF60, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0600DF48, "fin", 0],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "tail", [
			(True, "piranha"),
		]],
		[ultra.c.s_data, 0x0600DFC0, 0x0600E270, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0600E098, "tail", 0],
			[0, 1, 1, c.d_anime, 0x0600E24C],
			[0, -1, 1, ultra.c.d_addr, ultra.A_ADDR],
			[0, 1, 1, ultra.c.d_u64],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x0600E270, 0x0600E278, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("bub", "gfx.c"),
		[c.s_gltf, "bub", [
			("goggles", (0.25, 0xFF, 0xFF, 0xFF), ("goggles.rgba16.png", 32, 32)),
			("fin", (0.25, 0xFF, 0xFF, 0xFF), ("fin.rgba16.png", 32, 32)),
			("eyes", (0.25, 0xFF, 0xFF, 0xFF), ("eyes.rgba16.png", 64, 32)),
			("scale", (0.25, 0xFF, 0xFF, 0xFF), ("scale.rgba16.png", 64, 32)),
			("mouth", (0.25, 0xFF, 0x75, 0x94)),
			("white", (0.25, 0xFF, 0xFF, 0xFF)),
		]],
		[ultra.c.s_data, 0x0600E278, 0x060112A8, "E0.szp", [
			[0, -2, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "goggles"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "fin"],
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "eyes"],
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "scale"],
		]],
		[c.s_gltf_mesh, "body", [
			(True, "goggles"),
			(True, "fin"),
			(True, "eyes"),
			(True, "scale"),
			(True, "mouth"),
			(True, "white"),
		]],
		[ultra.c.s_data, 0x06011848, 0x06011BD8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06011BD8, "body", 0, 1, 2, 3, 4, 5],
		]],
		[c.s_gltf_mesh, "tail", [
			(True, "fin"),
		]],
		[ultra.c.s_data, 0x06011C58, 0x06011D50, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06011D50, "tail", 0],
		]],
		[c.s_gltf_mesh, "finL", [
			(True, "fin"),
		]],
		[ultra.c.s_data, 0x06011DC0, 0x06011EA8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06011EA8, "finL", 0],
		]],
		[c.s_gltf_mesh, "finR", [
			(True, "fin"),
		]],
		[ultra.c.s_data, 0x06011F18, 0x06012360, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06012000, "finR", 0],
			[0, 1, 1, c.d_anime, 0x0601233C],
			[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x06012360, 0x06012368, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("waterring", "gfx.c"),
		[c.s_gltf, "waterring", [
			("shade", (0.25, 0xFF, 0xFF, 0xFF)),
		]],
		[ultra.c.s_data, 0x06012368, 0x06013380, "E0.szp", [
			[0, -1, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "waterring"],
		]],
		[c.s_gltf_mesh, "waterring", [
			(True, "shade"),
		]],
		[ultra.c.s_data, 0x06013AC0, 0x06013F88, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06013DD8, "waterring", 0],
			[0, 1, 1, c.d_anime, 0x06013F64],
			[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x06013F88, 0x06013F90, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("chest", "gfx.c"),
		[c.s_gltf, "chest", [
			("keyhole", (0.25, 0xFF, 0xFF, 0xFF), ("keyhole.rgba16.png", 32, 32)),
			("inside", (0.25, 0xFF, 0xFF, 0xFF), ("inside.rgba16.png", 32, 32)),
			("latch", (0.25, 0xFF, 0xFF, 0xFF), ("latch.rgba16.png", 32, 32)),
			("outside", (0.25, 0xFF, 0xFF, 0xFF), ("outside.rgba16.png", 64, 32)),
		]],
		[ultra.c.s_data, 0x06013F90, 0x060167A8, "E0.szp", [
			[0, -1, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "keyhole"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "inside"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "latch"],
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "outside"],
		]],
		[c.s_gltf_mesh, "box", [
			(True, "keyhole"),
			(True, "latch"),
			(True, "inside"),
			(True, "outside"),
		]],
		[ultra.c.s_data, 0x06016D58, 0x06017030, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06017030, "box", 0, 1, 2, 3],
		]],
		[c.s_gltf_mesh, "lid", [
			(True, "inside"),
			(True, "latch"),
			(True, "outside"),
		]],
		[ultra.c.s_data, 0x06017680, 0x06017958, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06017958, "lid", 0, 1, 2],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x06017958, 0x06017960, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
]

shape_2b_shape = [
	s_dirfile("skeeter", "shape.c"),
		[ultra.c.s_data, 0x0D000000, 0x0D000284, "E0", [
			[0, 1, 1, c.d_s_script, 0x0D000284],
		]],
	s_writepop(),
	s_dirfile("kelp", "shape.c"),
		[ultra.c.s_data, 0x0D000284, 0x0D0002F4, "E0", [
			[0, 1, 1, c.d_s_script, 0x0D0002F4],
		]],
	s_writepop(),
	s_dirfile("watermine", "shape.c"),
		[ultra.c.s_data, 0x0D0002F4, 0x0D000324, "E0", [
			[0, 1, 1, c.d_s_script, 0x0D000324],
		]],
	s_writepop(),
	s_dirfile("piranha", "shape.c"),
		[ultra.c.s_data, 0x0D000324, 0x0D00038C, "E0", [
			[0, 1, 1, c.d_s_script, 0x0D00038C],
		]],
	s_writepop(),
	s_dirfile("bub", "shape.c"),
		[ultra.c.s_data, 0x0D00038C, 0x0D000414, "E0", [
			[0, 1, 1, c.d_s_script, 0x0D000414],
		]],
	s_writepop(),
	s_dirfile("waterring", "shape.c"),
		[ultra.c.s_data, 0x0D000414, 0x0D000450, "E0", [
			[0, 1, 1, c.d_s_script, 0x0D000450],
		]],
	s_writepop(),
	s_dirfile("chest", "shape.c"),
		[ultra.c.s_data, 0x0D000450, 0x0D000480, "E0", [
			[0, 1, 1, c.d_s_script, 0x0D000480],
		]],
	s_writepop(),
]

shape_2d_gfx = [
	s_dirfile("lakitu2", "gfx.c"),
		[c.s_gltf, "lakitu2", [
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
		[ultra.c.s_data, 0x06000000, 0x06003A30, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "unused"],
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "eyes_open"],
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "eyes_closed"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "shell"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "mouth"],
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, "lens"],
			[0, -2, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "body", [
			(True, "shell"),
			(True, "skin"),
		]],
		[ultra.c.s_data, 0x06003C80, 0x06003EB0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06003E98, "body", 0, 1],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "mouth", [
			(True, "mouth"),
		]],
		[ultra.c.s_data, 0x06004410, 0x060046F8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x060046E0, "mouth", 0],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "armR", [
			(True, "skin"),
		]],
		[ultra.c.s_data, 0x060047E8, 0x060048F0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x060048D8, "armR", 0],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "armL", [
			(True, "skin"),
		]],
		[ultra.c.s_data, 0x060049E0, 0x06004AE8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06004AD0, "armL", 0],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "eyes", [
			(True, "eyes"),
		]],
		[ultra.c.s_data, 0x06004BA8, 0x06004D10, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06004CB0, "eyes", 0],
			[0, -4, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "camera", [
			(True, "lens"),
			(True, "camera1"),
			(True, "camera2"),
			(True, "camera3"),
		]],
		[ultra.c.s_data, 0x060051D0, 0x06005468, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x060053D8, "camera", 0, 1, 2, 3],
			[0, -6, 1, c.d_light, 0.25],
		]],
		[c.s_gltf_mesh, "rod0", [
			(True, "rod1"),
		]],
		[c.s_gltf_mesh, "rod1", [
			(True, "rod4"),
		]],
		[c.s_gltf_mesh, "rod2", [
			(True, "rod4"),
		]],
		[ultra.c.s_data, 0x06005598, 0x06005900, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06005638,
				"rod0", 0,
				"rod1", 0,
				"rod2", 0,
			],
			[0, 1, 1, c.d_anime, 0x060058E0],
			[0, -1, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x06005900, 0x06005908, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("toad", "gfx.c"),
		[c.s_gltf, "toad", [
			("face", (0.5, 0xFF, 0xFF, 0xFF), ("face.rgba16.png", 32, 32)),
			("spot", (0.5, 0xFF, 0xFF, 0xFF), ("spot.rgba16.png", 32, 32)),
			("white", (0.5, 0xFF, 0xFF, 0xFF)),
			("vest", (0.5, 0x42, 0x27, 0xB5)),
			("skin", (0.5, 0xFE, 0xD5, 0xA1)),
			("shoe", (0.5, 0x68, 0x40, 0x1B)),
		]],
		[ultra.c.s_data, 0x06005908, 0x06006920, "E0.szp", [
			[0, -1, 1, c.d_light, 0.5],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "face"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "spot"],
		]],
		[c.s_gltf_mesh, "head", [
			(True, "face"),
			(True, "spot"),
			(True, "white"),
		]],
		[ultra.c.s_data, 0x06007300, 0x06007820, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06007808, "head", 0, 1, 2],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "vest", [
			(True, "vest"),
		]],
		[ultra.c.s_data, 0x060079E0, 0x06007B58, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06007B28, "vest", 0],
			[0, -2, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "body", [
			(True, "white"),
			(True, "skin"),
		]],
		[ultra.c.s_data, 0x06007DB8, 0x06007F98, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06007F80, "body", 0, 1],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "armR", [
			(True, "skin"),
		]],
		[ultra.c.s_data, 0x06008168, 0x060082E0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x060082C8, "armR", 0],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "armL", [
			(True, "skin"),
		]],
		[ultra.c.s_data, 0x06008490, 0x06008668, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06008650, "armL", 0],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "shoeR", [
			(True, "shoe"),
		]],
		[ultra.c.s_data, 0x06008838, 0x060089C0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x060089A8, "shoeR", 0],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "shoeL", [
			(True, "shoe"),
		]],
		[ultra.c.s_data, 0x06008B80, 0x06008, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06008CF0, "shoeL", 0],
			[0, 1, 1, c.d_anime, 0x0600906C],
			[0, 1, 1, c.d_anime, 0x06009400],
			[0, 1, 1, c.d_anime, 0x06009AE0],
			[0, 1, 1, c.d_anime, 0x0600A1C0],
			[0, 1, 1, c.d_anime, 0x0600B75C],
			[0, 1, 1, c.d_anime, 0x0600CF68],
			[0, 1, 1, c.d_anime, 0x0600E504],
			[0, 1, 1, c.d_anime, 0x0600FC30],
			[0, -8, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x0600FC68, 0x0600FC70, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("mips", "gfx.c"),
		[c.s_gltf, "mips", [
			("face", (0.4, 0xFF, 0xFF, 0xFF), ("face.rgba16.png", 32, 32)),
			("white", (0.4, 0xFF, 0xFF, 0xFF)),
			("light1", (0.4, 0x27, 0x21, 0x0B)),
			("face1", (0.4, 0x96, 0x96, 0x00), ("face.rgba16.png", 32, 32)),
			("face2", (0.4, 0x85, 0x8E, 0x00), ("face.rgba16.png", 32, 32)),
			("light2", (0.4, 0x82, 0x6E, 0x26)),
		]],
		[ultra.c.s_data, 0x0600FC70, 0x060104A0, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "face"],
			[0, -2, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "0", [
			(True, "face"),
			(True, "light1"),
			(True, "white"),
		]],
		[ultra.c.s_data, 0x060106F0, 0x06010928, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06010910, "0", 0, 1, 2],
			[0, -1, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "1", [
			(True, "face"),
		]],
		[ultra.c.s_data, 0x06010B88, 0x06010DC0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06010D90, "1", 0],
			[0, -2, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "2", [
			(True, "face1"),
			(True, "face"),
		]],
		[ultra.c.s_data, 0x06010EA0, 0x06010FF8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06010FB0, "2", 0, 1],
			[0, -3, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "3", [
			(True, "face1"),
			(True, "face2"),
			(True, "face"),
		]],
		[ultra.c.s_data, 0x060110E8, 0x06011230, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06011200, "3", 0, 1, 2],
			[0, -2, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "4", [
			(True, "face1"),
			(True, "face"),
		]],
		[ultra.c.s_data, 0x06011330, 0x06011490, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06011460, "4", 0, 1],
			[0, -2, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "5", [
			(True, "face1"),
			(True, "face"),
		]],
		[ultra.c.s_data, 0x06011560, 0x060116A0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06011670, "5", 0, 1],
			[0, -2, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "6", [
			(True, "face1"),
			(True, "face"),
		]],
		[ultra.c.s_data, 0x060117A0, 0x06011900, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x060118D0, "6", 0, 1],
			[0, -2, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "7", [
			(True, "face1"),
			(True, "face"),
		]],
		[ultra.c.s_data, 0x060119D0, 0x06011B10, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06011AE0, "7", 0, 1],
			[0, -2, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "8", [
			(True, "face1"),
			(True, "face"),
		]],
		[ultra.c.s_data, 0x06011BF0, 0x06011D30, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06011D00, "8", 0, 1],
			[0, -2, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "9", [
			(True, "face1"),
			(True, "face"),
		]],
		[ultra.c.s_data, 0x06011E00, 0x06011F30, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06011F00, "9", 0, 1],
			[0, -1, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "10", [
			(True, "light2"),
		]],
		[ultra.c.s_data, 0x06011F78, 0x06011FE8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06011FE8, "10", 0],
			[0, -1, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "11", [
			(True, "light2"),
		]],
		[ultra.c.s_data, 0x06012060, 0x060120D0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x060120D0, "11", 0],
			[0, 1, 1, c.d_anime, 0x06013338],
			[0, 1, 1, c.d_anime, 0x0601378C],
			[0, 1, 1, c.d_anime, 0x06013AE8],
			[0, 1, 1, c.d_anime, 0x06014C84],
			[0, 1, 1, c.d_anime, 0x0601570C],
			[0, -6, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x06015740, 0x06015748, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("boo2", "gfx.c"),
		[c.s_gltf, "boo2", [
			("shade", None),
			("eyes", None, ("eyes.rgba16.png", 64, 32)),
			("mouth", None, ("mouth.rgba16.png", 32, 32)),
		]],
		[ultra.c.s_data, 0x06015748, 0x06017E70, "E0.szp", [
			[0, 1, 1, ultra.c.d_Lights1],
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "eyes"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "mouth"],
		]],
		[c.s_gltf_mesh, "boo", [
			(True, "mouth"),
			(True, "eyes"),
			(True, "shade"),
		]],
		[ultra.c.s_data, 0x06017B00, 0x06017E70, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x06017E70, "boo", 0, 1, 2],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x06017E70, 0x06017E78, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
]

shape_2d_shape = [
	s_dirfile("lakitu2", "shape.c"),
		[ultra.c.s_data, 0x0D000000, 0x0D000114, "E0", [
			[0, 1, 1, c.d_s_script, 0x0D000114],
		]],
	s_writepop(),
	s_dirfile("toad", "shape.c"),
		[ultra.c.s_data, 0x0D000114, 0x0D00043C, "E0", [
			[0, 1, 1, c.d_s_script, 0x0D00043C],
		]],
	s_writepop(),
	s_dirfile("mips", "shape.c"),
		[ultra.c.s_data, 0x0D000440, 0x0D000448, "E0", [
			[0, 1, 1, ultra.c.d_u64],
		]],
		[ultra.c.s_data, 0x0D000448, 0x0D0005A4, "E0", [
			[0, 1, 1, c.d_s_script, 0x0D0005A4],
		]],
		[ultra.c.s_data, 0x0D0005A8, 0x0D0005B0, "E0", [
			[0, 1, 1, ultra.c.d_u64],
		]],
	s_writepop(),
	s_dirfile("boo2", "shape.c"),
		[ultra.c.s_data, 0x0D0005B0, 0x0D000600, "E0", [
			[0, 1, 1, c.d_s_script, 0x0D000600],
		]],
	s_writepop(),
]

global_gfx = [
	s_dirfile("puff", "gfx.c"),
		[ultra.c.s_data, 0x03000000, 0x030009C8, "E0.szp", [
			[0, -8, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, c.d_texture, "ia16", 32, 32, "puff"],
			[0, 1, 1, ultra.c.d_Gfx, 0x030009C0],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x030009C0, 0x030009C8, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("explosion", "gfx.c"),
		[ultra.c.s_data, 0x030009C8, 0x03004340, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			d_texture_n("rgba16", 32, 32, 7),
			[0, 1, 1, ultra.c.d_Gfx, 0x03004340],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x03004340, 0x03004348, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("butterfly", "gfx.c"),
		[c.s_gltf, "butterfly", [
			("wing", None, ("wing.rgba16.png", 32, 64), {"ss": 0.5, "st": 0.5}),
		]],
		[c.s_gltf_mesh, "l", [
			(False, "wing"),
		]],
		[ultra.c.s_data, 0x030043A8, 0x030053A8, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "wing"],
		]],
		[c.s_gltf_mesh, "r", [
			(False, "wing"),
		]],
		[ultra.c.s_data, 0x03005408, 0x030056B8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x03005538,
				"l", 0,
				"r", 0,
			],
			[0, 1, 1, c.d_anime, 0x030055B0],
			[0, 1, 1, c.d_anime, 0x03005698],
			[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x030056B8, 0x030056C0, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("coin", "gfx.c"),
		[ultra.c.s_data, 0x030056C0, 0x030079E0, "E0.szp", [
			[0, -12, 1, ultra.c.d_Vtx, False],
			d_texture_n("ia16", 32, 32, 4),
			[0, 1, 1, ultra.c.d_Gfx, 0x030079E0],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x030079E0, 0x030079E8, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("pipe", "gfx.c"),
		[c.s_gltf, "pipe", [
			("side", (0.25, 0xFF, 0xFF, 0xFF), ("side.rgba16.png", 32, 64)),
			("top", (0.25, 0xFF, 0xFF, 0xFF), ("top.rgba16.png", 32, 32)),
			("bottom", (0.25, 0x00, 0x00, 0x00)),
		]],
		[c.s_obj, "pipe"],
		[ultra.c.s_data, 0x030079E8, 0x03007A00, "E0.szp", [
			[0, -1, 1, c.d_light, 0.25],
		]],
		[c.s_gltf_mesh, "side", [
			(True, "side"),
		]],
		[ultra.c.s_data, 0x03007E40, 0x03009028, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "side"],
			[0, 1, 1, c.d_gfx, 0x03008FF8, "side", 0],
			[0, -2, 1, c.d_light, 0.25],
		]],
		[c.s_gltf_mesh, "end", [
			(True, "top"),
			(True, "bottom"),
		]],
		[ultra.c.s_data, 0x03009168, 0x03009CD8, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "top"],
			[0, 1, 1, c.d_gfx, 0x03009AC8, "end", 0, 1],
			[0, 1, 1, c.d_map, "map"],
		]],
		[c.s_gltf_write],
		[c.s_obj_write],
	s_writepop(),
	[ultra.c.s_data, 0x03009CD8, 0x03009CE0, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("door", "gfx.c"),
		[c.s_gltf, "door", [
			("a_face", (0.25, 0xFF, 0xFF, 0xFF), ("a_face.rgba16.png", 32, 64)),
			("a_side", (0.25, 0xFF, 0xFF, 0xFF), ("a_side.rgba16.png", 32, 64)),
			("knob", (0.25, 0xFF, 0xFF, 0x00)),
			("b_face", (0.25, 0xFF, 0xFF, 0xFF), ("b_face.rgba16.png", 32, 64)),
			("b_side", (0.25, 0xFF, 0xFF, 0xFF), ("b_side.rgba16.png", 32, 32)),
		]],
		[ultra.c.s_data, 0x03009CE0, 0x03013910, "E0.szp", [
			[0, -2, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "a_face"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "a_side"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "b_face"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "b_side"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "d_face"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "d_side"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "e_face"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "e_side"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "f_face"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "f_side"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "star"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "star1"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "star3"],
			[0, 1, 1, c.d_texture, "rgba16", 16, 32, "keyhole"],
		]],
		[c.s_gltf_mesh, "ah", [
			(True, "a_side"),
			(True, "a_face"),
		]],
		[c.s_gltf_mesh, "ahf", [
			(True, "knob"),
		]],
		[c.s_gltf_mesh, "ahb", [
			(True, "knob"),
		]],
		[ultra.c.s_data, 0x03013C10, 0x03013F20, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x03013F20,
				"ah", 0, 1,
				"ahf", 0,
				"ahb", 0,
			],
		]],
		[c.s_gltf_mesh, "al", [
			(True, "a_face"),
		]],
		[ultra.c.s_data, 0x03013FA0, 0x03014558, "E0.szp", [
			[0, -8, 1, ultra.c.d_Vtx, True],
			[0, 1, 1, c.d_gfx, 0x030140B0, "al", 0],
			[0, 1, 1, ultra.c.d_Gfx, 0x03014140],
			[0, -8, 1, ultra.c.d_Vtx, True],
			[0, 1, 1, ultra.c.d_Gfx, 0x03014370],
			[0, -16, 1, ultra.c.d_Vtx, True],
			[0, 1, 1, ultra.c.d_Gfx, 0x03014558],
		]],
		[c.s_gltf_mesh, "h", [
			(True, "b_side"),
			(True, "b_face"),
			(True, "knob"),
		]],
		[ultra.c.s_data, 0x03014888, 0x03014DF0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x03014DF0, "h", 2, 0, 1],
		]],
		[c.s_gltf_mesh, "l", [
			(True, "b_face"),
			(True, "knob"),
		]],
		[ultra.c.s_data, 0x03014EF0, 0x030156D4, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x030151C8, "l", 0, 1],
			[0, 1, 1, c.d_anime, 0x03015208],
			[0, 1, 1, c.d_anime, 0x03015440],
			[0, 1, 1, c.d_anime, 0x03015458],
			[0, 1, 1, c.d_anime, 0x03015690],
			[0, 1, 1, c.d_anime, 0x030156A8],
			[0, -6, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x030156D8, 0x030156E0, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("doorkey", "gfx.c"),
		[c.s_gltf, "doorkey", [
			("key", (0.25, 0xFF, 0xB2, 0x00)),
		]],
		[ultra.c.s_data, 0x030156E0, 0x030156F8, "E0.szp", [
			[0, -1, 1, c.d_light, 0.25],
		]],
		[c.s_gltf_mesh, "key", [
			(True, "key"),
		]],
		[ultra.c.s_data, 0x030161F8, 0x030172D8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x03016530, "key", 0],
			[0, 1, 1, c.d_anime, 0x03016BE8],
			[0, 1, 1, c.d_anime, 0x030172B8],
			[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x030172D8, 0x030172E0, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("flame", "gfx.c"),
		[ultra.c.s_data, 0x030172E0, 0x0301B5C0, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			d_texture_n("ia16", 32, 32, 8),
			[0, 1, 1, ultra.c.d_Gfx, 0x0301B5C0],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x0301B5C0, 0x0301B5C8, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("fish", "gfx.c"),
		[c.s_gltf, "fish", [
			("fish", (0.25, 0xFF, 0xFF, 0xFF), ("fish.rgba16.png", 32, 32)),
		]],
		[ultra.c.s_data, 0x0301B5C8, 0x0301BDE0, "E0.szp", [
			[0, -1, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "fish"],
		]],
		[c.s_gltf_mesh, "body", [
			(True, "fish"),
		]],
		[ultra.c.s_data, 0x0301BEC0, 0x0301C018, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0301C018, "body", 0],
		]],
		[c.s_gltf_mesh, "tail", [
			(True, "fish"),
		]],
		[ultra.c.s_data, 0x0301C0A8, 0x0301C2B4, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0301C1B0, "tail", 0],
			[0, 1, 1, c.d_anime, 0x0301C298],
			[0, -2, 1, ultra.c.d_addr, ultra.A_ADDR],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x0301C2B8, 0x0301C2C0, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("stone", "gfx.c"),
		[ultra.c.s_data, 0x0301C2C0, 0x0301CB98, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "stone"],
			[0, 1, 1, ultra.c.d_Gfx, 0x0301CB98],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x0301CB98, 0x0301CBA0, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("leaf", "gfx.c"),
		[ultra.c.s_data, 0x0301CBA0, 0x0301CE70, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, "leaf"],
			[0, 1, 1, ultra.c.d_Gfx, 0x0301CE70],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x0301CE70, 0x0301CE78, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("map", "gfx.c"),
		[c.s_obj, "door"],
		[ultra.c.s_data, 0x0301CE78, 0x0301CECC, "E0.szp", [
			[0, 1, 1, c.d_map, "door"],
		]],
		[c.s_obj_write],
		[c.s_obj, "13002018"],
		[ultra.c.s_data, 0x0301CECC, 0x0301CF00, "E0.szp", [
			[0, 1, 1, c.d_map, "13002018"],
		]],
		[c.s_obj_write],
	s_writepop(),
	[ultra.c.s_data, 0x0301CF00, 0x0301CF08, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("cap", "gfx.c"),
		[c.s_gltf, "cap", [
			("red", (0.5, 0xFF, 0x00, 0x00)),
			("hair", (0.5, 0x73, 0x06, 0x00)),
			("logo", (0.5, 0xFF, 0xFF, 0xFF), ("logo.rgba16.png", 32, 32)),
			("wing_l", (0.5, 0xFF, 0xFF, 0xFF), ("wing_l.rgba16.png", 32, 64)),
			("wing_r", (0.5, 0xFF, 0xFF, 0xFF), ("wing_r.rgba16.png", 32, 64)),
		]],
		[ultra.c.s_data, 0x0301CF08, 0x03022750, "E0.szp", [
			[0, -3, 1, c.d_light, 0.5],
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "metal"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "logo"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "wing_l"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "wing_r"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "metal_wing_l"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "metal_wing_r"],
		]],
		[c.s_gltf_mesh, "cap", [
			(True, "logo"),
			(True, "red"),
			(True, "hair"),
		]],
		[ultra.c.s_data, 0x03022B30, 0x03022D38, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x03022D38, "cap", 0, 1, 2],
		]],
		[c.s_gltf_mesh, "wing", [
			(True, "wing_l"),
			(True, "wing_r"),
		]],
		[ultra.c.s_data, 0x03022E78, 0x030233D0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x030233D0, "wing", 0, 1],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x030233D0, 0x030233D8, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("meter", "gfx.c"),
		[ultra.c.s_data, 0x030233D8, 0x030295D8, "E0.szp", [
			[0, 1, 1, ultra.c.d_u64],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "0_l"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "0_r"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "8"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "7"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "6"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "5"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "4"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "3"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "2"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "1"],
			[0, -8, 1, ultra.c.d_addr, 0],
			[0, -8, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, ultra.c.d_Gfx, 0x03029530],
			[0, -4, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, ultra.c.d_Gfx, 0x030295D8],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x030295D8, 0x030295E0, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("number", "gfx.c"),
	s_writepop(),
	[ultra.c.s_data, 0x030295E0, 0x030295E8, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("1up", "gfx.c"),
		[ultra.c.s_data, 0x030295E8, 0x0302A6D0, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "1up"],
			[0, 1, 1, ultra.c.d_Gfx, 0x0302A6D0],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x0302A6D0, 0x0302A6D8, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("powerstar", "gfx.c"),
		[c.s_gltf, "powerstar", [
			("star", (0.25, 0xFF, 0xFF, 0xFF)),
			("eye", (0.25, 0xFF, 0xFF, 0xFF), ("eye.rgba16.png", 32, 32)),
		]],
		[ultra.c.s_data, 0x0302A6D8, 0x0302B6F0, "E0.szp", [
			[0, -1, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "star"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "eye"],
		]],
		[c.s_gltf_mesh, "star", [
			(True, "star"),
		]],
		[ultra.c.s_data, 0x0302B7B0, 0x0302B920, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0302B908, "star", 0],
			[0, -1, 1, c.d_light, 0.25],
		]],
		[c.s_gltf_mesh, "eyes", [
			(True, "eye"),
		]],
		[ultra.c.s_data, 0x0302B9C0, 0x0302BA88, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0302BA88, "eyes", 0],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x0302BA88, 0x0302BA90, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("sand", "gfx.c"),
		[ultra.c.s_data, 0x0302BA90, 0x0302BD60, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, "sand"],
			[0, 1, 1, ultra.c.d_Gfx, 0x0302BD60],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x0302BD60, 0x0302BD68, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("shard", "gfx.c"),
		[ultra.c.s_data, 0x0302BD68, 0x0302C480, "E0.szp", [
			[0, -4, 1, c.d_light, 0.25],
			[0, -3, 1, ultra.c.d_Vtx, True],
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, "cork"],
			[0, 1, 1, ultra.c.d_Gfx, 0x0302C098],
			[0, -3, 1, ultra.c.d_Vtx, True],
			[0, -3, 1, ultra.c.d_Vtx, False],
			[0, -10, 1, ultra.c.d_Vtx, True],
			[0, -10, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, ultra.c.d_Gfx, 0x0302C480],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x0302C480, 0x0302C488, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("shadestar", "gfx.c"),
		[c.s_gltf, "shadestar", [
			("star", (0.1, 0x1E, 0x32, 0xE6)),
		]],
		[ultra.c.s_data, 0x0302C488, 0x0302C4A0, "E0.szp", [
			[0, -1, 1, c.d_light, 0.1],
		]],
		[c.s_gltf_mesh, "star", [
			(True, "star"),
		]],
		[ultra.c.s_data, 0x0302C560, 0x0302C658, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0302C658, "star", 0],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x0302C658, 0x0302C660, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("snow", "gfx.c"),
		[ultra.c.s_data, 0x0302C660, 0x0302C938, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, "snow"],
			[0, 1, 1, ultra.c.d_Gfx, 0x0302C938],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x0302C938, 0x0302C940, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("signpost", "gfx.c"),
		[c.s_gltf, "signpost", [
			("wood", (0.5, 0xFF, 0xFF, 0xFF), ("wood.rgba16.png", 32, 32)),
			("face", (0.5, 0xFF, 0xFF, 0xFF), ("face.rgba16.png", 32, 32)),
		]],
		[c.s_obj, "signpost"],
		[ultra.c.s_data, 0x0302C940, 0x0302C958, "E0.szp", [
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "post", [
			(True, "wood"),
		]],
		[ultra.c.s_data, 0x0302C9C8, 0x0302DAC0, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "wood"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "face"],
			[0, 1, 1, c.d_gfx, 0x0302DAA8, "post", 0],
			[0, -1, 1, c.d_light, 0.5],
		]],
		[c.s_gltf_mesh, "sign", [
			(True, "wood"),
			(True, "face"),
		]],
		[ultra.c.s_data, 0x0302DC40, 0x0302DE04, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0302DD80, "sign", 0, 1],
			[0, 1, 1, c.d_map, "map"],
		]],
		[c.s_gltf_write],
		[c.s_obj_write],
	s_writepop(),
	[ultra.c.s_data, 0x0302DE08, 0x0302DE10, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("tree", "gfx.c"),
		[c.s_gltf, "tree", [
			("a_l", None, ("a_l.rgba16.png", 32, 64)),
			("a_r", None, ("a_r.rgba16.png", 32, 64)),
			("b", (0.25, 0xFF, 0xFF, 0xFF), ("b.rgba16.png", 32, 64)),
			("c", (0.25, 0xFF, 0xFF, 0xFF), ("c.rgba16.png", 32, 64)),
			("e", (0.25, 0xFF, 0xFF, 0xFF), ("e.rgba16.png", 32, 64)),
		]],
		[ultra.c.s_data, 0x0302DE10, 0x0302FE28, "E0.szp", [
			[0, -1, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "a_l"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "a_r"],
		]],
		[c.s_gltf_mesh, "a", [
			(False, "a_l"),
			(False, "a_r"),
		]],
		[ultra.c.s_data, 0x0302FE88, 0x03030F60, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0302FF60, "a", 0, 1],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "b"],
		]],
		[c.s_gltf_mesh, "b", [
			(True, "b"),
		]],
		[ultra.c.s_data, 0x03030FA0, 0x03032048, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x03031048, "b", 0],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "c"],
		]],
		[c.s_gltf_mesh, "c", [
			(True, "c"),
		]],
		[ultra.c.s_data, 0x03032088, 0x03032130, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x03032130, "c", 0],
		]],
		[c.s_gltf_mesh, "d", [
			(True, "b"),
		]],
		[ultra.c.s_data, 0x03032170, 0x03033218, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x03032218, "d", 0],
			[0, 1, 1, c.d_texture, "rgba16", 32, 64, "e"],
		]],
		[c.s_gltf_mesh, "e", [
			(True, "e"),
		]],
		[ultra.c.s_data, 0x03033258, 0x03033300, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x03033300, "e", 0],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[ultra.c.s_data, 0x03033300, 0x03033308, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
]

global_shape = [
	s_dirfile("puff", "shape.c"),
		[ultra.c.s_data, 0x16000000, 0x16000040, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000040],
		]],
	s_writepop(),
	s_dirfile("explosion", "shape.c"),
		[ultra.c.s_data, 0x16000040, 0x160000A8, "E0", [
			[0, 1, 1, c.d_s_script, 0x160000A8],
		]],
	s_writepop(),
	s_dirfile("butterfly", "shape.c"),
		[ultra.c.s_data, 0x160000A8, 0x1600013C, "E0", [
			[0, 1, 1, c.d_s_script, 0x1600013C],
		]],
	s_writepop(),
	s_dirfile("coin", "shape.c"),
		[ultra.c.s_data, 0x1600013C, 0x16000388, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000388],
		]],
	s_writepop(),
	s_dirfile("pipe", "shape.c"),
		[ultra.c.s_data, 0x16000388, 0x160003A8, "E0", [
			[0, 1, 1, c.d_s_script, 0x160003A8],
		]],
	s_writepop(),
	s_dirfile("door", "shape.c"),
		[ultra.c.s_data, 0x160003A8, 0x16000A84, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000A84],
		]],
	s_writepop(),
	s_dirfile("doorkey", "shape.c"),
		[ultra.c.s_data, 0x16000A84, 0x16000B10, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000B10],
		]],
	s_writepop(),
	s_dirfile("flame", "shape.c"),
		[ultra.c.s_data, 0x16000B10, 0x16000BEC, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000BEC],
		]],
	s_writepop(),
	s_dirfile("fish", "shape.c"),
		[ultra.c.s_data, 0x16000BEC, 0x16000C8C, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000C8C],
		]],
	s_writepop(),
	s_dirfile("stone", "shape.c"),
	s_writepop(),
	s_dirfile("leaf", "shape.c"),
		[ultra.c.s_data, 0x16000C8C, 0x16000CA4, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000CA4],
		]],
	s_writepop(),
	s_dirfile("map", "shape.c"),
	s_writepop(),
	s_dirfile("cap", "shape.c"),
		[ultra.c.s_data, 0x16000CA4, 0x16000E14, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000E14],
		]],
	s_writepop(),
	s_dirfile("meter", "shape.c"),
	s_writepop(),
	s_dirfile("number", "shape.c"),
		[ultra.c.s_data, 0x16000E14, 0x16000E84, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000E84],
		]],
	s_writepop(),
	s_dirfile("1up", "shape.c"),
		[ultra.c.s_data, 0x16000E84, 0x16000EA0, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000EA0],
		]],
	s_writepop(),
	s_dirfile("powerstar", "shape.c"),
		[ultra.c.s_data, 0x16000EA0, 0x16000ED4, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000ED4],
		]],
	s_writepop(),
	s_dirfile("sand", "shape.c"),
	s_writepop(),
	s_dirfile("shard", "shape.c"),
		[ultra.c.s_data, 0x16000ED4, 0x16000F6C, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000F6C],
		]],
	s_writepop(),
	s_dirfile("shadestar", "shape.c"),
		[ultra.c.s_data, 0x16000F6C, 0x16000F98, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000F98],
		]],
	s_writepop(),
	s_dirfile("snow", "shape.c"),
		[ultra.c.s_data, 0x16000F98, 0x16000FB4, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000FB4],
		]],
	s_writepop(),
	s_dirfile("signpost", "shape.c"),
		[ultra.c.s_data, 0x16000FB4, 0x16000FE8, "E0", [
			[0, 1, 1, c.d_s_script, 0x16000FE8],
		]],
	s_writepop(),
	s_dirfile("tree", "shape.c"),
		[ultra.c.s_data, 0x16000FE8, 0x16001060, "E0", [
			[0, 1, 1, c.d_s_script, 0x16001060],
		]],
	s_writepop(),
]

data_object = [
	[main.s_file, "object_a.sx"],
		s_include(["sm64/objlang"]),
		[main.s_str, "\n"],
		[main.s_str, str_script],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, "\n"],
		[asm.s_script, 0x13000000, 0x13002EB8, "E0", 1],
	[main.s_write],
	[main.s_file, "player.sx"],
		s_include(["sm64/objlang"]),
		[main.s_str, "\n"],
		[main.s_str, str_script],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, "\n"],
		[asm.s_script, 0x13002EC0, 0x13002F98, "E0", 1],
	[main.s_write],
	[main.s_file, "object_b.sx"],
		s_include(["sm64/objlang"]),
		[main.s_str, "\n"],
		[main.s_str, str_script],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, "\n"],
		[asm.s_script, 0x13002FA0, 0x13004580, "E0", 1],
	[main.s_write],
	[main.s_file, "object_c.sx"],
		s_include(["sm64/objlang"]),
		[main.s_str, "\n"],
		[main.s_str, str_script],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, "\n"],
		[asm.s_script, 0x13004580, 0x13005610, "E0", 1],
	[main.s_write],
	[main.s_file, "camera.sx"],
		s_include(["sm64/objlang"]),
		[main.s_str, "\n"],
		[main.s_str, str_script],
		[main.s_str, "\n"],
		[main.s_str, str_data],
		[main.s_str, "\n"],
		[asm.s_script, 0x13005610, 0x130056BC, "E0", 1],
	[main.s_write],
]

title_shape = [
	[ultra.c.s_data, 0x140002D0, 0x14000414, "E0", [
		[0, 1, 1, c.d_s_script, 0x14000414],
	]],
	[ultra.c.s_data, 0x14000414, 0x140004FC, "E0", [
		[0, 1, 1, c.d_s_script, 0x140004FC],
	]],
]

title_logo = [
	s_include(["sm64"]),
	[main.s_str, "\n"],
	[c.s_gltf, "logo", [
		("wood", None, ("wood.rgba16.png", 32, 32)),
		("marble", None, ("marble.rgba16.png", 32, 32)),
		("shade", None),
		("copyright", None, ("copyright.rgba16.png", 128, 16)),
		("trademark", None, ("trademark.rgba16.png", 16, 16)),
	]],
	[c.s_gltf_mesh, "logo", [
		(False, "marble"),
		(False, "wood"),
		(False, "shade"),
	]],
	[ultra.c.s_data, 0x07007EA0, 0x0700B420, "E0.szp", [
		[0, 1, 1, c.d_texture, "rgba16", 32, 32, "wood"],
		[0, 1, 1, c.d_texture, "rgba16", 32, 32, "marble"],
		[0, 1, 1, c.d_gfx, 0x0700B420, "logo", 0, 1, 2],
	]],
	[c.s_gltf_mesh, "symbol", [
		(False, "copyright"),
		(False, "trademark"),
	]],
	[ultra.c.s_data, 0x0700B4A0, 0x0700C790, "E0.szp", [
		[0, 1, 1, c.d_texture, "rgba16", 128, 16, "copyright"],
		[0, 1, 1, c.d_texture, "rgba16",  16, 16, "trademark"],
		[0, 1, 1, c.d_gfx, 0x0700C790, "symbol", 0, 1],
	]],
	[c.s_gltf_write],
	[ultra.c.s_data, 0x0700C790, 0x0700C940, "E0.szp", [
		[0, -(20+16), 3, ultra.c.d_f32, "%.4f"],
	]],
]

title_debug = [
	s_include(["sm64"]),
	[main.s_str, "\n"],
	[c.s_gltf, "debug", [
		("super_s", (0.5, 0xFF, 0x00, 0x00)),
		("super_u", (0.5, 0x00, 0x00, 0xFF)),
		("super_p", (0.5, 0x00, 0xAD, 0x00)),
		("super_e", (0.5, 0xFF, 0x00, 0x00)),
		("super_r", (0.5, 0x00, 0x00, 0xFF)),
		("mario_m", (0.5, 0xFF, 0x00, 0x00)),
		("mario_a", (0.5, 0x00, 0x00, 0xFF)),
		("mario_r", (0.5, 0x00, 0xB2, 0x00)),
		("mario_i", (0.5, 0xFF, 0x00, 0x00)),
		("mario_o", (0.5, 0x00, 0x00, 0xFF)),
	]],
	[ultra.c.s_data, 0x07000000, 0x07000018, "E0.szp", [
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[c.s_gltf_mesh, "super_s", [
		(True, "super_s"),
	]],
	[ultra.c.s_data, 0x07000858, 0x07000A40, "E0.szp", [
		[0, 1, 1, c.d_gfx, 0x07000A28, "super_s", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[c.s_gltf_mesh, "super_u", [
		(True, "super_u"),
	]],
	[ultra.c.s_data, 0x07001100, 0x070012A0, "E0.szp", [
		[0, 1, 1, c.d_gfx, 0x07001288, "super_u", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[c.s_gltf_mesh, "super_p", [
		(True, "super_p"),
	]],
	[ultra.c.s_data, 0x07001BA0, 0x07001DB0, "E0.szp", [
		[0, 1, 1, c.d_gfx, 0x07001D98, "super_p", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[c.s_gltf_mesh, "super_e", [
		(True, "super_e"),
	]],
	[ultra.c.s_data, 0x070025F0, 0x070027D8, "E0.szp", [
		[0, 1, 1, c.d_gfx, 0x070027C0, "super_e", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[c.s_gltf_mesh, "super_r", [
		(True, "super_r"),
	]],
	[ultra.c.s_data, 0x07003258, 0x070034B8, "E0.szp", [
		[0, 1, 1, c.d_gfx, 0x070034A0, "super_r", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[c.s_gltf_mesh, "mario_m", [
		(True, "mario_m"),
	]],
	[ultra.c.s_data, 0x07003DB8, 0x07003FC8, "E0.szp", [
		[0, 1, 1, c.d_gfx, 0x07003FB0, "mario_m", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[c.s_gltf_mesh, "mario_a", [
		(True, "mario_a"),
	]],
	[ultra.c.s_data, 0x070048C8, 0x07004AD8, "E0.szp", [
		[0, 1, 1, c.d_gfx, 0x07004AC0, "mario_a", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[c.s_gltf_mesh, "mario_r", [
		(True, "mario_r"),
	]],
	[ultra.c.s_data, 0x07005558, 0x070057B8, "E0.szp", [
		[0, 1, 1, c.d_gfx, 0x070057A0, "mario_r", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[c.s_gltf_mesh, "mario_i", [
		(True, "mario_i"),
	]],
	[ultra.c.s_data, 0x070059F8, 0x07005AB0, "E0.szp", [
		[0, 1, 1, c.d_gfx, 0x07005A98, "mario_i", 0],
		[0, 1, 1, ultra.c.d_Lights1],
	]],
	[c.s_gltf_mesh, "mario_o", [
		(True, "mario_o"),
	]],
	[ultra.c.s_data, 0x070063B0, 0x070065A8, "E0.szp", [
		[0, 1, 1, c.d_gfx, 0x070065A8, "mario_o", 0],
	]],
	[c.s_gltf_write],
]

select_shape = [
	s_dirfile("file", "shape.c"),
		[ultra.c.s_data, 0x140001D0, 0x14000290, "E0", [
			[0, 1, 1, c.d_s_script, 0x14000290],
		]],
	s_writepop(),
	s_dirfile("tile", "shape.c"),
		[ultra.c.s_data, 0x14000290, 0x14000380, "E0", [
			[0, 1, 1, c.d_s_script, 0x14000380],
		]],
	s_writepop(),
	[ultra.c.s_data, 0x14000380, 0x14000490, "E0", [
		[0, 1, 1, c.d_s_script, 0x14000490],
	]],
]

select_gfx = [
	s_include(["sm64"]),
	[main.s_str, "\n"],
	s_dirfile("file", "gfx.c"),
		[c.s_gltf, "file", [
			("edge", (0.25, 0xFF, 0xFF, 0xFF), ("light.rgba16.png", 32, 32)),
			("face", (0.25, 0xFF, 0xFF, 0xFF), ("new.rgba16.png", 64, 32)),
		]],
		[ultra.c.s_data, 0x07000000, 0x07003018, "E0.szp", [
			[0, -1, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "light"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "shade"],
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "mario"],
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "new"],
		]],
		[c.s_gltf_mesh, "file", [
			(True, "edge"),
			(True, "face"),
		]],
		[ultra.c.s_data, 0x07003158, 0x07003450, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x07003258, "file", 0, 1],
			[0, -4, 1, ultra.c.d_Vtx, True],
			[0, 1, 1, ultra.c.d_Gfx, 0x07003450],
		]],
		[c.s_gltf_write],
	s_writepop(),
	s_dirfile("tile", "gfx.c"),
		[c.s_gltf, "tile", [
			("tile", (0.25, 0xFF, 0xFF, 0xFF), ("main.rgba16.png", 32, 32)),
		]],
		[ultra.c.s_data, 0x07003450, 0x07005C68, "E0.szp", [
			[0, -1, 1, c.d_light, 0.25],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "erase"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "copy"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "main"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "score"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "sound"],
		]],
		[c.s_gltf_mesh, "tile", [
			(True, "tile"),
		]],
		[ultra.c.s_data, 0x07006038, 0x070062E8, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x070062E8, "tile", 0],
		]],
		[c.s_gltf_write],
	s_writepop(),
	s_dirfile("cursor", "gfx.c"),
		[ultra.c.s_data, 0x070062E8, 0x070073D0, "E0.szp", [
			[0, -4, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "0"],
			[0, 1, 1, c.d_texture, "rgba16", 32, 32, "1"],
			[0, 1, 1, ultra.c.d_Gfx, 0x070073D0],
		]],
	s_writepop(),
	s_dirfile("print", "gfx.c"),
		[ultra.c.s_data, 0x070073D0, 0x0700ABD0, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, name]
			for name in [
				"k_hu",
				"k_xa",
				"k_i",
				"k_ru",
				"k_se",
				"k_re",
				"k_ku",
				"k_to",
				"h_wo",
				"k_ko",
				"k_pi",
				"chouonpu",
				"h_su",
				"h_ru",
				"h_ke",
				"k_ma",
				"k_ri",
				"k_o",
				"k_su",
				"k_a",
				"h_mi",
				"h_do",
				"h_no",
				"question",
				"k_sa",
				"k_u",
				"k_n",
				"k_do",
			]
		]],
		[ultra.c.s_data, 0x0700ABD0, 0x0700AC40, "E0.szp", [
			[0, -28, 1, ultra.c.d_addr, 0],
		]],
	s_writepop(),
	s_dirfile("msg8", "gfx.c"),
		[ultra.c.s_data, 0x0700AC40, 0x0700B840, "E0.szp", [
			[0, 1, 1, c.d_texture, "ia8", 8, 8, name]
			for name in list("0123456789") + [
				"u_"+x for x in "abcdefghijklmnopqrstuvwxyz"
			] + [
				"coin",
				"multiply",
				"star",
				"hyphen",
				"comma",
				"apostrophe",
				"exclaim",
				"question",
				"mario_l",
				"mario_r",
				"period",
				"ampersand",
			]
		]],
		[ultra.c.s_data, 0x0700B840, 0x0700BCD8, "E0.szp", [
			[0, -256, 1, ultra.c.d_addr, 0],
			[0, 1, 1, ultra.c.d_Gfx, 0x0700BCD8],
		]],
	s_writepop(),
	[main.s_str, "\n"],
	[ultra.c.s_data, 0x0700BCD8, 0x0700BCE0, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	s_dirfile("course", "gfx.c"),
		[ultra.c.s_data, 0x0700BCE0, 0x0700DE30, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "h"],
			[0, 1, 1, c.d_texture, "rgba16", 64, 32, "l"],
			[0, -8, 1, ultra.c.d_Vtx, False],
			[0, 1, 1, ultra.c.d_Gfx, 0x0700DE30],
		]],
	s_writepop(),
	[c.s_obj, "select"],
	[ultra.c.s_data, 0x0700DE30, 0x0700DE60, "E0.szp", [
		[0, 1, 1, c.d_map, "map"],
	]],
	[c.s_obj_write],
]

data_game = [
]

data_weather = [
	s_include(["sm64"]),
	[main.s_str, "\n"],
	[ultra.c.s_data, 0x0B000000, 0x0B000008, "E0.szp", [
		[0, 1, 1, ultra.c.d_u64],
	]],
	[main.s_str, "\n"],
	s_dirfile("flower", "texture.c"),
		[ultra.c.s_data, 0x0B000008, 0x0B002020, "E0.szp", [
			d_texture_n("rgba16", 32, 32, 4),
			[0, -6, 1, ultra.c.d_addr, 0],
		]],
	s_writepop(),
	s_dirfile("lava", "texture.c"),
		[ultra.c.s_data, 0x0B002020, 0x0B006048, "E0.szp", [
			d_texture_n("rgba16", 32, 32, 8),
			[0, -10, 1, ultra.c.d_addr, 0],
		]],
	s_writepop(),
	s_dirfile("bubble", "texture.c"),
		[ultra.c.s_data, 0x0B006048, 0x0B00684C, "E0.szp", [
			d_texture_n("rgba16", 32, 32, 1),
			[0, -1, 1, ultra.c.d_addr, 0],
		]],
	s_writepop(),
	s_dirfile("snow", "gfx.c"),
		[ultra.c.s_data, 0x0B00684C, 0x0B006D98, "E0.szp", [
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, "a"],
			[0, 1, 4, None],
			[0, 1, 1, ultra.c.d_Gfx, 0x0B006AD8],
			[0, 1, 1, c.d_texture, "rgba16", 16, 16, "b"],
			[0, 1, 1, ultra.c.d_Gfx, 0x0B006D98],
		]],
	s_writepop(),
]

"""
0 = grass
1 = path
2 = bridge

3 = stone ground (beginning cannon)
4 = stone wall (inside cannon, bridge pivot, etc)
5 = rocks
6 = switch tunnel
7 = chain chomp area
8 = below island cannon, stairs
9 = flower top
10 = flower side
11 = arrow sign face
12 = arrow sign back

13 = shadow

14 = barred fence
15 = wire fence

16 = dirt
17 = dirt shadow
18 = mountain grass
19 = mountain path
20 = elevator pulley
21 = mountain path?
22 = elevator track

23 = mountain teleport

54 = chain chomp gate
55 = seesaw bridge
56 = barred gate
"""

bob_gfx = [
	[main.s_str, "#include \"data/texture/c.szp.h\"\n"],
	[main.s_str, "\n"],
	[ultra.c.s_data, 0x07000000, 0x07002800, "E0.szp", [
		d_texture_n("rgba16", 32, 32, 5),
	]],
	s_dirfile("battlefield", "gfx.c"),
		[c.s_gltf, "battlefield", [
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
		[ultra.c.s_data, 0x07002800, 0x07002818, "E0.szp", [
			[0, -1, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "smooth", [
			(True, "c11"),
			(True, "c18"),
			(True, "c12"),
		]],
		[ultra.c.s_data, 0x07003CA8, 0x07004490, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x07004478, "smooth", 0, 1, 2],
			[0, -1, 1, c.d_light, 0.4],
		]],
		[c.s_gltf_mesh, "flat", [
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
		[ultra.c.s_data, 0x07008AF0, 0x07009E98, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x07009E98, "flat", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
		]],
		[c.s_gltf_mesh, "xlu_decal", [
			(False, "c21"),
		]],
		[ultra.c.s_data, 0x0700A318, 0x0700A4E0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0700A4E0, "xlu_decal", 0],
		]],
		[c.s_gltf_mesh, "tex_edge", [
			(False, "c16"),
			(False, "0"),
		]],
		[ultra.c.s_data, 0x0700A800, 0x0700AA10, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0700A9E0, "tex_edge", 0, 1],
			[0, -2, 1, c.d_light, 0.2],
		]],
		[c.s_gltf_mesh, "shade", [
			(True, "c17"),
			(True, "c17_shade"),
			(True, "c11"),
			(True, "c18"),
			(True, "4"),
			(True, "c19"),
			(True, "c12"),
		]],
		[ultra.c.s_data, 0x0700CFC0, 0x0700DE48, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0700DE30, "shade", 0, 1, 2, 3, 4, 5, 6],
			[0, -1, 1, c.d_light, 0.2],
		]],
		[c.s_gltf_mesh, "cave", [
			(True, "c17_cave"),
		]],
		[ultra.c.s_data, 0x0700E1E8, 0x0700E3E0, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0700E3E0, "cave", 0],
		]],
		[c.s_gltf_write],
	s_writepop(),
	s_dirfile("54", "gfx.c"),
		[c.s_gltf, "54", [
			("c16", None, ("../../../data/texture/c16.rgba16.png", 32, 32)),
		]],
		[c.s_gltf_mesh, "54", [
			(False, "c16"),
		]],
		[ultra.c.s_data, 0x0700E420, 0x0700E510, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0700E510, "54", 0],
		]],
		[c.s_gltf_write],
	s_writepop(),
	s_dirfile("55", "gfx.c"),
		[c.s_gltf, "55", [
			("c12", (0.25, 0xFF, 0xFF, 0xFF), ("../../../data/texture/c12.rgba16.png", 32, 64)),
		]],
		[ultra.c.s_data, 0x0700E510, 0x0700E528, "E0.szp", [
			[0, -1, 1, c.d_light, 0.25],
		]],
		[c.s_gltf_mesh, "55", [
			(True, "c12"),
		]],
		[ultra.c.s_data, 0x0700E6C8, 0x0700E810, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0700E810, "55", 0],
		]],
		[c.s_gltf_write],
	s_writepop(),
	s_dirfile("56", "gfx.c"),
		[c.s_gltf, "56", [
			("c16", None, ("../../../data/texture/c16.rgba16.png", 32, 32)),
		]],
		[c.s_gltf_mesh, "56", [
			(False, "c16"),
		]],
		[ultra.c.s_data, 0x0700E860, 0x0700E958, "E0.szp", [
			[0, 1, 1, c.d_gfx, 0x0700E958, "56", 0],
		]],
		[c.s_gltf_write],
	s_writepop(),
	[main.s_dir, "battlefield"],
		[c.s_obj, "battlefield"],
		[ultra.c.s_data, 0x0700E958, 0x070113C0, "E0.szp", [
			[0, 1, 1, c.d_map, "map"],
			[0, 1, 1, c.d_tag],
		]],
		[c.s_obj_write],
	[main.s_pop],
	[main.s_dir, "54"],
		[c.s_obj, "54"],
		[ultra.c.s_data, 0x070113C0, 0x070113F0, "E0.szp", [
			[0, 1, 1, c.d_map, "map"],
		]],
		[c.s_obj_write],
	[main.s_pop],
	[main.s_dir, "55"],
		[c.s_obj, "55"],
		[ultra.c.s_data, 0x070113F0, 0x07011474, "E0.szp", [
			[0, 1, 1, c.d_map, "map"],
		]],
		[c.s_obj_write],
	[main.s_pop],
	[main.s_dir, "56"],
		[c.s_obj, "56"],
		[ultra.c.s_data, 0x07011474, 0x07011530, "E0.szp", [
			[0, 1, 1, c.d_map, "map"],
		]],
		[c.s_obj_write],
	[main.s_pop],
	[ultra.c.s_data, 0x07011530, 0x070117C2, "E0.szp", [
		[0, 3, 1, c.d_path_data],
	]],
]

bob_shape = [
	s_dirfile("54", "shape.c"),
		[ultra.c.s_data, 0x0E000440, 0x0E000458, "E0", [
			[0, 1, 1, c.d_s_script, 0x0E000458],
		]],
	s_writepop(),
	s_dirfile("55", "shape.c"),
		[ultra.c.s_data, 0x0E000458, 0x0E000470, "E0", [
			[0, 1, 1, c.d_s_script, 0x0E000470],
		]],
	s_writepop(),
	s_dirfile("56", "shape.c"),
		[ultra.c.s_data, 0x0E000470, 0x0E000488, "E0", [
			[0, 1, 1, c.d_s_script, 0x0E000488],
		]],
	s_writepop(),
	s_dirfile("battlefield", "shape.c"),
		[ultra.c.s_data, 0x0E000488, 0x0E00054C, "E0", [
			[0, 1, 1, c.d_s_script, 0x0E00054C],
		]],
	s_writepop(),
]

ending_gfx = [
	[ultra.c.s_data, 0x07000000, 0x07027350, "E0.szp", [
		d_texture_n("rgba16", 80, 20, 48, "%d"),
		[0, -192, 1, ultra.c.d_Vtx, False],
		[0, 1, 1, ultra.c.d_Gfx, 0x07027350],
	]],
]

ending_shape = [
	[ultra.c.s_data, 0x0E000050, 0x0E0000BC, "E0", [
		[0, 1, 1, c.d_s_script, 0x0E0000BC],
	]],
]

lst = [
	# [main.s_data, "J0", ["donor", "UNSMJ00.z64"]],
	[main.s_data, "E0", ["donor", "UNSME00.z64"]],
	# [main.s_data, "G0", ["donor", "UNSMG00.z64"]],
	[main.s_copy, ["makefile"], ["makefile"]],
	[main.s_copy, ["dep.mk"],   ["dep.mk"]],
	[main.s_copy, ["spec"],     ["spec"]],
	[main.s_copy, ["rel.ld"],   ["rel.ld"]],
	[main.s_copy, ["elf.ld"],   ["elf.ld"]],
	[main.s_copy, ["tools"],    ["tools"]],
	[main.s_copy, ["include"],  ["include"]],
	[main.s_copy, ["src"],      ["src"]],
	[main.s_copy, ["data"],     ["data"]],
	[main.s_copy, ["libultra"], ["libultra"]],
	# [main.s_file, "J0.code.s"],
	# 	[main.s_addr, 0x80246000-0x00001000],
	# 	[ultra.asm.s_code, 0x80246000, 0x8032A320, "J0", 0, True, True],
	# [main.s_write],
	# [main.s_file, "J0.ulib.s"],
	# 	[main.s_addr, 0x80378800-0x000F4210],
	# 	[ultra.asm.s_code, 0x80378800, 0x80385F90, "J0", 0, True, True],
	# [main.s_write],
	# [main.s_file, "J0.menu.s"],
	# 	[main.s_addr, 0x8016F000-0x0021D7D0],
	# 	[ultra.asm.s_code, 0x8016F000, 0x801A76F0, "J0", 0, True, True],
	# [main.s_write],
	# [main.s_file, "E0.code.s"],
	# 	[main.s_addr, 0x80246000-0x00001000],
	# 	[ultra.asm.s_code, 0x80246000, 0x8032B260, "E0", 0, True, True],
	# [main.s_write],
	# [main.s_file, "E0.ulib.s"],
	# 	[main.s_addr, 0x80378800-0x000F5580],
	# 	[ultra.asm.s_code, 0x80378800, 0x80385F90, "E0", 0, True, True],
	# [main.s_write],
	# [main.s_file, "E0.menu.s"],
	# 	[main.s_addr, 0x8016F000-0x0021F4C0],
	# 	[ultra.asm.s_code, 0x8016F000, 0x801A7830, "E0", 0, True, True],
	# [main.s_write],
	[main.s_dir, "include"],
		# [main.s_file, "sm64.inc"],
		# 	[main.s_str, ".ifdef TARGET_E0\n"],
		# 	[ultra.asm.s_definelabel, "E0"],
		# 	[main.s_str, ".endif /* TARGET_E0 */\n"],
		# [main.s_write],
		[main.s_dir, "sm64"],
			[main.s_addr, 0x80246000-0x00001000],
			[main.s_call, include_code],
			[main.s_call, include_audio],
			[main.s_addr, 0x80378800-0x000F5580],
			[main.s_call, include_ulib],
			[main.s_addr, 0x8016F000-0x0021F4C0],
			[main.s_call, include_menu],
			[main.s_call, include_face],
		[main.s_pop],
	[main.s_pop],
	[main.s_dir, "libultra"],
		[main.s_addr, 0x80246000-0x00001000],
		[main.s_dir, "src"],
			[main.s_call, libultra_src],
			[main.s_dir, "PR"],
				[main.s_call, libultra_src_PR],
			[main.s_pop],
		[main.s_pop],
	[main.s_pop],
	[main.s_dir, "src"],
		[main.s_addr, 0x80246000-0x00001000],
		[main.s_call, src_code],
		[main.s_dir, "audio"],
			[main.s_call, src_audio],
		[main.s_pop],
		[main.s_addr, 0x80378800-0x000F5580],
		[main.s_call, src_ulib],
		[main.s_addr, 0x8016F000-0x0021F4C0],
		[main.s_call, src_menu],
		[main.s_dir, "face"],
			[main.s_call, src_face],
			[main.s_addr, 0x04000000-0x002739A0],
			[main.s_bin, 0x04000000, 0x04032780, "E0", ["data.bin"]],
			[main.s_file, "data.s"],
				[main.s_str, ".data\n.incbin \"src/face/data.bin\"\n"],
			[main.s_write],
		[main.s_pop],
	[main.s_pop],
	[main.s_dir, "data"],
		[main.s_addr, 0x10000000-0x00108A10],
		[main.s_file, "main.sx"],
			s_include(["sm64/prglang"]),
			[main.s_str, "\n"],
			[main.s_str, str_data],
			[main.s_str, "\n"],
			[main.s_str, "#define STAGE   0\n\n"],
			[asm.s_script, 0x10000000, 0x1000000C, "E0", 0],
			[main.s_str, "\tpSet(STAGE)\n"],
			[main.s_str, "#if STAGE == 0\n"],
			[asm.s_script, 0x10000010, 0x10000020, "E0", 0],
			[main.s_str, "#else\n"],
			[main.s_str, "\tpExecute(SEG_GAME, _GameSegmentRomStart, _GameSegmentRomEnd, p_game)\n"],
			[main.s_str, "#endif\n"],
			[asm.s_script, 0x10000020, 0x10000028, "E0", 0],
		[main.s_write],
		s_gfx(0x00108A40, 0x00114750, 0x02, "gfx", data_gfx),
		# [s_szp, 0x001076D0, 0x00112B50, "J0"],
		# [main.s_addr, 0x02000000],
		# [main.s_file, ""],
		# [c.s_message, 0x0200DFE8, 0x0200E294, "J0.szp", "msg", "ja_jp", "table", "jp"],
		# [main.s_dev, None],
		[main.s_dir, "object"],
			[main.s_addr, 0x13000000-0x00219E00],
			[main.s_call, data_object],
		[main.s_pop],
		[main.s_addr, 0x15000000-0x002ABCA0],
		[main.s_file, "game.sx"],
			s_include(["sm64/prglang"]),
			[main.s_str, "\n"],
			[main.s_str, str_data],
			[main.s_str, "\n"],
			[asm.s_script, 0x15000000, 0x15000660, "E0", 0],
			[main.s_str, "\n"],
	[main.s_pop],
			s_shape_p(0x15000660, 0x1500071C, "3common"),
			s_shape_p(0x1500071C, 0x15000750, "1a"),
			s_shape_p(0x15000750, 0x1500076C, "1b"),
			s_shape_p(0x1500076C, 0x15000788, "1c"),
			s_shape_p(0x15000788, 0x150007B4, "1d"),
			s_shape_p(0x150007B4, 0x150007E8, "1e"),
			s_shape_p(0x150007E8, 0x1500080C, "1f"),
			s_shape_p(0x1500080C, 0x15000830, "1g"),
			s_shape_p(0x15000830, 0x1500084C, "1h"),
			s_shape_p(0x1500084C, 0x15000888, "1i"),
			s_shape_p(0x15000888, 0x150008A4, "1j"),
			s_shape_p(0x150008A4, 0x150008D8, "1k"),
			s_shape_p(0x150008D8, 0x15000914, "2a"),
			s_shape_p(0x15000914, 0x15000958, "2b"),
			s_shape_p(0x15000958, 0x1500099C, "2c"),
			s_shape_p(0x1500099C, 0x150009C0, "2d"),
			s_shape_p(0x150009C0, 0x150009DC, "2e"),
			s_shape_p(0x150009DC, 0x15000A10, "2f"),
		[main.s_write],
	[main.s_dir, "data"],
		[main.s_dir, "back"],
			s_gfx(0x002708C0, 0x002739A0, 0x0A, "title", [
				[main.s_dir, "title"],
				s_include(["sm64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x0A000000, 0x0A0065E8, "E0.szp", [
					[0, -16, 1, ultra.c.d_Vtx, False],
					[0, 1, 1, ultra.c.d_Gfx, 0x0A0001C0],
					d_texture_n("rgba16", 80, 20, 4, "mario.%d"),
					d_texture_n("rgba16", 80, 20, 4, "gameover.%d"),
					[0, -8, 1, ultra.c.d_addr, 0],
					[0, 1, 1, ultra.c.d_u64],
				]],
				[main.s_pop],
			]),
			s_gfx(0x002AC6B0, 0x002B8F10, 0x0A, "a", [
				[main.s_dir, "a"],
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x0A000000, 0x0A020140, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 64),
					[0, -80, 1, ultra.c.d_addr, 0],
				]],
				[main.s_pop],
			]),
			s_gfx(0x002B8F10, 0x002C73D0, 0x0A, "b", [
				[main.s_dir, "b"],
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x0A000000, 0x0A020140, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 64),
					[0, -80, 1, ultra.c.d_addr, 0],
				]],
				[main.s_pop],
			]),
			s_gfx(0x002C73D0, 0x002D0040, 0x0A, "c", [
				[main.s_dir, "c"],
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x0A000000, 0x0A014940, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 41),
					[0, -80, 1, ultra.c.d_addr, 0],
				]],
				[main.s_pop],
			]),
			s_gfx(0x002D0040, 0x002D64F0, 0x0A, "d", [
				[main.s_dir, "d"],
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x0A000000, 0x0A018940, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 49),
					[0, -80, 1, ultra.c.d_addr, 0],
				]],
				[main.s_pop],
			]),
			s_gfx(0x002D64F0, 0x002E7880, 0x0A, "e", [
				[main.s_dir, "e"],
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x0A000000, 0x0A020140, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 64),
					[0, -80, 1, ultra.c.d_addr, 0],
				]],
				[main.s_pop],
			]),
			s_gfx(0x002E7880, 0x002F14E0, 0x0A, "f", [
				[main.s_dir, "f"],
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x0A000000, 0x0A020140, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 64),
					[0, -80, 1, ultra.c.d_addr, 0],
				]],
				[main.s_pop],
			]),
			s_gfx(0x002F14E0, 0x002FB1B0, 0x0A, "g", [
				[main.s_dir, "g"],
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x0A000000, 0x0A020140, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 64),
					[0, -80, 1, ultra.c.d_addr, 0],
				]],
				[main.s_pop],
			]),
			s_gfx(0x002FB1B0, 0x00301CD0, 0x0A, "h", [
				[main.s_dir, "h"],
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x0A000000, 0x0A014940, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 41),
					[0, -80, 1, ultra.c.d_addr, 0],
				]],
				[main.s_pop],
			]),
			s_gfx(0x00301CD0, 0x0030CEC0, 0x0A, "i", [
				[main.s_dir, "i"],
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x0A000000, 0x0A020140, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 64),
					[0, -80, 1, ultra.c.d_addr, 0],
				]],
				[main.s_pop],
			]),
			s_gfx(0x0030CEC0, 0x0031E1D0, 0x0A, "j", [
				[main.s_dir, "j"],
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x0A000000, 0x0A020140, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 64),
					[0, -80, 1, ultra.c.d_addr, 0],
				]],
				[main.s_pop],
			]),
		[main.s_pop],
		[main.s_dir, "texture"],
			s_gfx(0x0031E1D0, 0x00326E40, 0x09, "a", [
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x09000000, 0x0900C000, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 24, "a%d"),
				]],
			]),
			s_gfx(0x00326E40, 0x0032D070, 0x09, "b", [
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x09000000, 0x0900C800, "E0.szp", [
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "b0"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "b1"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "b2"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "b3"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "b4"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "b5"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "b6"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "b7"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "b8"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "b9"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "b10"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "b11"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "b12"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "b13"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "b14"],
					[0, 1, 1, c.d_texture, "ia16", 32, 32, "b15_g17"], # light spot
					[0, 1, 1, c.d_texture, "ia16", 32, 32, "b16"], # light edge 1
					[0, 1, 1, c.d_texture, "ia16", 32, 64, "b17"], # light torch
				]],
			]),
			s_gfx(0x0032D070, 0x00334B30, 0x09, "c", [
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x09000000, 0x0900B800, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 12, "c%d", 0),
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "c12"],
					d_texture_n("rgba16", 32, 32, 21, "c%d", 13),
					[0, 1, 1, c.d_texture, "ia16", 32, 32, "c21_j22_k22"], # shadow circle
				]],
			]),
			s_gfx(0x00334B30, 0x0033D710, 0x09, "d", [
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x09000000, 0x0900C800, "E0.szp", [
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "d0"],
					d_texture_n("rgba16", 64, 32, 6, "d%d", 1),
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "d6"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "d7"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "d8"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "d9"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "d10"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "d11"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "d12"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "d13"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "d14"],
				]],
			]),
			s_gfx(0x0033D710, 0x00341140, 0x09, "e", [
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x09000000, 0x09008800, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 4, "e%d"),
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "e4"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "e5"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "e6"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "e7"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "e8_j12"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "e9"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "e10_i18"],
					d_texture_n("rgba16", 32, 32, 15, "e%d", 11),
				]],
			]),
			s_gfx(0x00341140, 0x00347A50, 0x09, "f", [
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x09000000, 0x0900A000, "E0.szp", [
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "f0"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "f1"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "f2"],
					d_texture_n("rgba16", 32, 32, 13, "f%d", 3),
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "f13"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "f14"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "f15"],
					[0, 1, 1, c.d_texture, "ia16", 32, 32, "f16"], # ice?
					[0, 1, 1, c.d_texture, "ia16", 32, 32, "f17"], # shadow snowtree
				]],
			]),
			s_gfx(0x00347A50, 0x0034E760, 0x09, "g", [
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x09000000, 0x0900C800, "E0.szp", [
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "g0"],
					d_texture_n("rgba16", 32, 32, 6, "g%d", 1),
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "g6"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "g7"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "g8"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "g9"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "g10"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "g11"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "g12"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "g13"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "g14"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "g15"],
					[0, 1, 1, c.d_texture, "ia16", 32, 32, "g16"], # light edge 2
					[0, 1, 1, c.d_texture, "ia16", 32, 32, "b15_g17"],
				]],
			]),
			s_gfx(0x0034E760, 0x00351960, 0x09, "h", [
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x09000000, 0x09008C00, "E0.szp", [
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "h0"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "h1_l6"],
					d_texture_n("rgba16", 32, 32, 8, "h%d", 2),
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "h8"],
					d_texture_n("rgba16", 32, 32, 14, "h%d", 9),
					[0, 1, 1, c.d_texture, "rgba16", 16, 64, "h14"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 8, "h15"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "h16"],
				]],
			]),
			s_gfx(0x00351960, 0x00357350, 0x09, "i", [
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x09000000, 0x0900C800, "E0.szp", [
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "i0"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "i1"],
					d_texture_n("rgba16", 32, 32, 16, "i%d", 2),
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "i16"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "i17"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "e10_i18"],
					d_texture_n("rgba16", 32, 32, 23, "i%d", 19),
				]],
			]),
			s_gfx(0x00357350, 0x0035ED10, 0x09, "j", [
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x09000000, 0x0900C000, "E0.szp", [
					d_texture_n("rgba16", 32, 32, 12, "j%d"),
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "e8_j12"],
					d_texture_n("rgba16", 32, 32, 22, "j%d", 13),
					[0, 1, 1, c.d_texture, "ia16", 32, 32, "c21_j22_k22"],
					[0, 1, 1, c.d_texture, "ia16", 32, 32, "j23"], # cloud?
				]],
			]),
			s_gfx(0x0035ED10, 0x00365980, 0x09, "k", [
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x09000000, 0x0900C400, "E0.szp", [
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "k0"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "k1"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "k2"],
					d_texture_n("rgba16", 32, 32, 12, "k%d", 3),
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "k12"],
					d_texture_n("rgba16", 32, 32, 20, "k%d", 13),
					[0, 1, 1, c.d_texture, "rgba16", 16, 32, "k20"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "k21"],
					[0, 1, 1, c.d_texture, "ia16", 32, 32, "c21_j22_k22"],
				]],
			]),
			s_gfx(0x00365980, 0x0036F530, 0x09, "l", [
				s_include(["ultra64"]),
				[main.s_str, "\n"],
				[ultra.c.s_data, 0x09000000, 0x0900C800, "E0.szp", [
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "l0"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "l1"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "l2"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "l3"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "l4"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "l5"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "h1_l6"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "l7"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "l8"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "l9"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "l10"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "l11"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "l12"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "l13"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "l14"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 64, "l15"],
					[0, 1, 1, c.d_texture, "rgba16", 32, 32, "l16"],
					[0, 1, 1, c.d_texture, "rgba16", 64, 32, "l17"],
				]],
			]),
		[main.s_pop],
		[main.s_dir, "weather"],
			s_gfx(0x0036F530, 0x00371C40, 0x0B, "gfx", data_weather),
		[main.s_pop],
		[main.s_addr, 0-0x004EC000],
		[main.s_file, "anime.sx"],
			s_include(["sm64/defshape", "sm64/bank"]),
			[main.s_str, str_anime],
			[asm.s_anime, 0x0008DC18, "E0", "anime", (table.stbl_anime, table.ctbl_anime)],
		[main.s_write],
		[main.s_addr, 0-0x00579C20],
		[main.s_file, "demo.sx"],
			s_include(["sm64/defstage", "sm64/bank"]),
			[main.s_str, str_demo],
			[asm.s_demo, 0x00001B00, "E0", "demo", (table.stbl_demo, table.ctbl_demo)],
		[main.s_write],
	[main.s_pop],
	[main.s_dir, "shape"],
		s_shape(0x00114750, 0x001279B0, 0x04, 0x17, "player", player_gfx, player_shape),
		s_shapebin(0x0012A7E0, 0x00132850, 0x00015360, 0x0410, 0x0C, "1a", [
			[0, 1, 1, c.d_s_script, 0x0C000410],
		]),
		s_shape(0x00132C60, 0x00134A70, 0x05, 0x0C, "1b", shape_1b_gfx, shape_1b_shape),
		s_shapebin(0x00134D20, 0x0013B5D0, 0x000110A0, 0x0340, 0x0C, "1c", [
			[0, 1, 1, c.d_s_script, 0x0C000340],
		]),
		s_shapebin(0x0013B910, 0x00145C10, 0x00013D30, 0x0280, 0x0C, "1d", [
			[0, 1, 1, c.d_s_script, 0x0C000280],
		]),
		s_shapebin(0x00145E90, 0x00151B70, 0x00014650, 0x0660, 0x0C, "1e", [
			[0, 1, 1, c.d_s_script, 0x0C000660],
		]),
		s_shapebin(0x001521D0, 0x001602E0, 0x000160B8, 0x0384, 0x0C, "1f", [
			[0, 1, 1, c.d_s_script, 0x0C000384],
		]),
		s_shapebin(0x00160670, 0x001656E0, 0x0000D130, 0x0364, 0x0C, "1g", [
			[0, 1, 1, c.d_s_script, 0x0C000364],
		]),
		s_shapebin(0x00165A50, 0x00166BD0, 0x000034C8, 0x0090, 0x0C, "1h", [
			[0, 1, 1, c.d_s_script, 0x0C000090],
		]),
		s_shapebin(0x00166C60, 0x0016D5C0, 0x00010178, 0x02AC, 0x0C, "1i", [
			[0, 1, 1, c.d_s_script, 0x0C0002AC],
		]),
		s_shapebin(0x0016D870, 0x00180540, 0x00024200, 0x0664, 0x0C, "1j", [
			[0, 1, 1, c.d_s_script, 0x0C00045C],
			[0, 1, 4, None],
			[0, 1, 1, ultra.c.d_u64],
			[0, 1, 1, c.d_s_script, 0x0C000664],
		]),
		s_shapebin(0x00180BB0, 0x00187FA0, 0x00016EC0, 0x04A0, 0x0C, "1k", [
			[0, 1, 1, c.d_s_script, 0x0C0004A0],
		]),
		s_shapebin(0x00188440, 0x001B9070, 0x00062F10, 0x0C4C, 0x0D, "2a", [
			[0, 1, 1, c.d_s_script, 0x0D000C4C],
		]),
		s_shape(0x001B9CC0, 0x001C3DB0, 0x06, 0x0D, "2b", shape_2b_gfx, shape_2b_shape),
		s_shapebin(0x001C4230, 0x001D7C90, 0x00025188, 0x0678, 0x0D, "2c", [
			[0, 1, 1, c.d_s_script, 0x0D000678],
		]),
		s_shape(0x001D8310, 0x001E4BF0, 0x06, 0x0D, "2d", shape_2d_gfx, shape_2d_shape),
		s_shapebin(0x001E51F0, 0x001E7D90, 0x00005E78, 0x0148, 0x0D, "2e", [
			[0, 1, 1, c.d_s_script, 0x0D000140],
			[0, 1, 1, ultra.c.d_u64],
		]),
		s_shapebin(0x001E7EE0, 0x001F1B30, 0x00015070, 0x06D0, 0x0D, "2f", [
			[0, 1, 1, c.d_s_script, 0x0D0006D0],
		]),
		s_shapebin(0x001F2200, 0x002008D0, 0x00028BF0, 0x0B34, 0x0F, "3common", [
			[0, 1, 1, c.d_s_script, 0x0F000020],
			[0, 1, 1, ultra.c.d_u64],
			[0, 1, 1, c.d_s_script, 0x0F00019C],
			[0, 1, 4, None],
			[0, 1, 1, ultra.c.d_u64],
			[0, 1, 1, c.d_s_script, 0x0F000B34],
		]),
		s_shape(0x00201410, 0x00218DA0, 0x03, 0x16, "global", global_gfx, global_shape),
	[main.s_pop],
	[main.s_dir, "stage"],
		[main.s_dir, "title"],
			[main.s_addr, 0x14000000-0x00269EA0],
			[main.s_file, "program.sx"],
				s_include(["sm64/prglang"]),
				[main.s_str, "\n"],
				[main.s_str, str_data],
				[main.s_str, "\n"],
				[asm.s_script, 0x14000000, 0x140002D0, "E0", 0],
			[main.s_write],
			[main.s_file, "shape.c"],
				s_include(["sm64/shplang"]),
				[main.s_str, "\n"],
				[main.s_call, title_shape],
			[main.s_write],
			s_gfx(0x0026A3A0, 0x0026F420, 0x07, "logo",  title_logo),
			s_gfx(0x0026F420, 0x002708C0, 0x07, "debug", title_debug),
		[main.s_pop],
		[main.s_dir, "select"],
			[main.s_addr, 0x14000000-0x002A6120],
			[main.s_file, "program.sx"],
				s_include(["sm64/prglang"]),
				[main.s_str, "\n"],
				[main.s_str, str_data],
				[main.s_str, "\n"],
				[asm.s_script, 0x14000000, 0x140001C4, "E0", 0],
			[main.s_write],
			[main.s_file, "shape.c"],
				s_include(["sm64/shplang"]),
				[main.s_str, "\n"],
				[main.s_call, select_shape],
			[main.s_write],
			s_gfx(0x002A65B0, 0x002ABCA0, 0x07, "gfx", select_gfx),
		[main.s_pop],
		s_stagebin(0x00371C40, 0x003828C0, 0x00383950, 0x00026E44, 0x5A8, "bbh"),
		s_stagebin(0x00383950, 0x00395C90, 0x00396340, 0x000237A6, 0x3DC, "ccm"),
		s_stagebin(0x00396340, 0x003CF0D0, 0x003D0DC0, 0x00079118, 0xEFC, "inside", "\n\n.globl gfx_inside_0702A880; gfx_inside_0702A880 = 0x0702A880;\n\n"),
		s_stagebin(0x003D0DC0, 0x003E6A00, 0x003E76B0, 0x0002B968, 0x530, "hmc"),
		s_stagebin(0x003E76B0, 0x003FB990, 0x003FC2AC, 0x000288B0, 0x5B4, "ssl"),
		s_stage(0x003FC2B0, 0x00405A60, 0x43C, "bob", bob_gfx, bob_shape),
		s_stagebin(0x00405FB0, 0x0040E840, 0x0040ED64, 0x0000FA88, 0x360, "sl"),
		s_stagebin(0x0040ED70, 0x00419F90, 0x0041A75C, 0x00018788, 0x57C, "wdw"),
		s_stagebin(0x0041A760, 0x00423B20, 0x004246C4, 0x000113AC, 0x900, "jrb"),
		s_stagebin(0x004246D0, 0x0042C6E0, 0x0042CF1C, 0x0000E3BC, 0x5A4, "thi"),
		s_stagebin(0x0042CF20, 0x00437400, 0x00437868, 0x00016A20, 0x240, "ttc"),
		s_stagebin(0x00437870, 0x0044A140, 0x0044ABB4, 0x0002EE76, 0x658, "rr", "\n\n.globl rr_07019080; rr_07019080 = 0x07019080;\n.globl gfx_rr_07019128; gfx_rr_07019128 = 0x07019128;\n.globl gfx_rr_07019198; gfx_rr_07019198 = 0x07019198;\n.globl gfx_rr_07019200; gfx_rr_07019200 = 0x07019200;\n\n"),
		s_stagebin(0x0044ABC0, 0x004545E0, 0x00454E00, 0x00011878, 0x65C, "grounds"),
		s_stagebin(0x00454E00, 0x0045BF60, 0x0045C600, 0x0000FE30, 0x3B4, "bitdw"),
		s_stagebin(0x0045C600, 0x00461220, 0x004614C8, 0x0000ACC8, 0x1F0, "vcutm"),
		s_stagebin(0x004614D0, 0x0046A840, 0x0046B088, 0x00015C08, 0x4A4, "bitfs"),
		s_stagebin(0x0046B090, 0x0046C1A0, 0x0046C3A0, 0x00003330, 0x168, "sa"),
		s_stagebin(0x0046C3A0, 0x00477D00, 0x004784A0, 0x0001B7F4, 0x42C, "bits"),
		s_stagebin(0x004784A0, 0x0048C9B0, 0x0048D930, 0x000288D0, 0x9D8, "lll"),
		s_stagebin(0x0048D930, 0x00495A60, 0x00496090, 0x0000FD10, 0x450, "ddd"),
		s_stagebin(0x00496090, 0x0049DA50, 0x0049E70C, 0x00011E18, 0x7E0, "wf"),
		s_stage(0x0049E710, 0x004AC4B0, 0x050, "ending", ending_gfx, ending_shape),
		s_stagebin(0x004AC570, 0x004AF670, 0x004AF930, 0x00006E7C, 0x1FC, "courtyard"),
		s_stagebin(0x004AF930, 0x004B7F10, 0x004B80C8, 0x0001109C, 0x0F8, "pss"),
		s_stagebin(0x004B80D0, 0x004BE9E0, 0x004BEC28, 0x0000BFA8, 0x194, "cotmc"),
		s_stagebin(0x004BEC30, 0x004C2700, 0x004C2920, 0x000089C6, 0x158, "totwc"),
		s_stagebin(0x004C2920, 0x004C41C0, 0x004C4318, 0x00002AC8, 0x0D0, "bitdwa"),
		s_stagebin(0x004C4320, 0x004CD930, 0x004CDBCC, 0x000137AE, 0x1E4, "wmotr"),
		s_stagebin(0x004CDBD0, 0x004CE9F0, 0x004CEC00, 0x00001BA0, 0x16C, "bitfsa"),
		s_stagebin(0x004CEC00, 0x004D14F0, 0x004D1910, 0x000050BC, 0x28C, "bitsa"),
		s_stagebin(0x004D1910, 0x004EB1F0, 0x004EBFFC, 0x00030474, 0x710, "ttm"),
	[main.s_pop],
	[main.s_dir, "audio"],
		[main.s_file, "se.ins"],
			[asm.s_audio_ctltbl, 0x0057B720, 0x00593560, "E0", table.ctlname_se, table.tblname_se],
		[main.s_write],
		[main.s_file, "music.ins"],
			[asm.s_audio_ctltbl, 0x0057B720, 0x00593560, "E0", table.ctlname_music, table.tblname_music],
		[main.s_write],
		[main.s_file, "bnk.txt"],
			[asm.s_audio_seqbnk, 0x007B0860, 0x007CC620, "E0", table.seqpath],
		[main.s_write],
	[main.s_pop],
]
