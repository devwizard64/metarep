import ultra

def aw(self, extern=False, addr=False, cast=None, array=None):
	return ultra.fmt_addr(self, self.u32(), extern, addr, cast, array)

def init(self, seg, addr):
	ultra.init(self, seg, addr)

def fmt(self, lst):
	data = self.file.data
	for addr, sym, extern, ln in lst:
		if len(ln) == 0: continue
		if len(extern) > 0: data.append("\n\n")
		for a, s in sorted(extern, key=lambda x: (x[0], x[1].label)):
			start = "/* 0x%08X */ " % a if ultra.COMM_EADDR else ""
			start += "extern "
			data.append(s.fmt(start, ";") + "\n")
		start = "/* 0x%08X */ " % addr if ultra.COMM_VADDR else ""
		if "DALIGN" in sym.flag: start += "DALIGN "
		s = sym.fmt(start, " =")
		if len(ln) > 1 or ln[0].endswith(",") or ln[0].startswith("#"):
			data.append("\n\n%s\n{\n" % s)
			for s in ln:
				x = s.lstrip("\t")
				if x.startswith("#"):   data.append("%s\n" % x)
				else:                   data.append("\t%s\n" % s)
			data.append("};\n\n")
		else:
			if "\n" in ln[0]: data.append("\n")
			data.append("%s %s;\n" % (s, ln[0]))
			if "\n" in ln[0]: data.append("\n")

def d_str_prc(self, argv):
	size, s = argv
	self.addr += size
	return [s]
d_str = [False, d_str_prc]

def d_pathfmt_prc(self, argv):
	size, fmt, fn = argv
	self.addr += size
	return [fmt % self.path_join([fn], 1)]
d_pathfmt = [False, d_pathfmt_prc]

def d_fmt(self, argv, x, fmt="%d"):
	return [self.fmt(argv[0] if len(argv) > 0 else fmt, x)]

d_s8  = [False, lambda self, argv: d_fmt(self, argv, self.s8())]
d_u8  = [False, lambda self, argv: d_fmt(self, argv, self.u8())]
d_s16 = [False, lambda self, argv: d_fmt(self, argv, self.s16())]
d_u16 = [False, lambda self, argv: d_fmt(self, argv, self.u16())]
d_s32 = [False, lambda self, argv: d_fmt(self, argv, self.s32())]
d_u32 = [False, lambda self, argv: d_fmt(self, argv, self.u32())]
d_s64 = [False, lambda self, argv: d_fmt(self, argv, self.s64())]
d_u64 = [False, lambda self, argv: d_fmt(self, argv, self.u64())]
d_f32 = [False, lambda self, argv: d_fmt(self, argv, self.f(), ultra.fmt_f32)]
d_f64 = [False, lambda self, argv: d_fmt(self, argv, self.d(), ultra.fmt_f64)]
d_flag8  = [False, lambda self, argv: [self.fmt_flag(argv[0], self.u8())]]
d_flag16 = [False, lambda self, argv: [self.fmt_flag(argv[0], self.u16())]]
d_flag32 = [False, lambda self, argv: [self.fmt_flag(argv[0], self.u32())]]
d_align_s8  = [[0, 1, 1, d_s8],  [0, 1, 3, None]]
d_align_u8  = [[0, 1, 1, d_u8],  [0, 1, 3, None]]
d_align_s16 = [[0, 1, 1, d_s16], [0, 1, 2, None]]
d_align_u16 = [[0, 1, 1, d_u16], [0, 1, 2, None]]
d_bool_s8   = [[0, 1, 1, d_s8,  ultra.fmt_bool], [0, 1, 3, None]]
d_bool_u8   = [[0, 1, 1, d_u8,  ultra.fmt_bool], [0, 1, 3, None]]
d_bool_s16  = [[0, 1, 1, d_s16, ultra.fmt_bool], [0, 1, 2, None]]
d_bool_u16  = [[0, 1, 1, d_u16, ultra.fmt_bool], [0, 1, 2, None]]

def d_addr_prc(self, argv):
	x = self.u32()
	extern = False
	addr   = False
	cast   = None
	array  = None
	flag = argv[0]
	i = 1
	if flag & ultra.A_EXTERN:
		extern = True
	if flag & ultra.A_ADDR:
		addr = True
	if flag & ultra.A_CAST:
		cast = argv[i]
		i += 1
	if flag & ultra.A_ARRAY:
		array = (argv[i+0], argv[i+1])
		i += 2
	return [ultra.fmt_addr(self, x, extern, addr, cast, array)]
d_addr = [False, d_addr_prc]

fmt_Vp = {
	640: "4*(SCREEN_WD/2)",
	480: "4*(SCREEN_HT/2)",
	0x1FF: "G_MAXZ/2",
}
def d_Vp_prc(self, argv):
	w = fmt_Vp[self.s16()]
	h = fmt_Vp[self.s16()]
	d = fmt_Vp[self.s16()]
	self.addr += 2
	x = fmt_Vp[self.s16()]
	y = fmt_Vp[self.s16()]
	z = fmt_Vp[self.s16()]
	self.addr += 2
	return ["{{{%s, %s, %s, 0}, {%s, %s, %s, 0}}}" % (w, h, d, x, y, z)]
d_Vp = [False, d_Vp_prc]

def d_Lights1_prc(self, argv):
	ra = self.u8()
	ga = self.u8()
	ba = self.u8()
	self.addr += 5
	r0 = self.u8()
	g0 = self.u8()
	b0 = self.u8()
	self.addr += 5
	x = self.s8()
	y = self.s8()
	z = self.s8()
	self.addr += 5
	return [(
		"gdSPDefLights1"
		"(0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, %d, %d, %d)"
	) % (ra, ga, ba, r0, g0, b0, x, y, z)]
d_Lights1 = [False, d_Lights1_prc]

def d_Vtx_prc(self, argv):
	n, = argv
	x = self.s16()
	y = self.s16()
	z = self.s16()
	f = self.u16()
	s = self.s16()
	t = self.s16()
	if n == 0:
		r = self.u8()
		g = self.u8()
		b = self.u8()
	else:
		r = self.s8()
		g = self.s8()
		b = self.s8()
	a = self.u8()
	return [(
		"{{{%6d, %6d, %6d}, %d, {%6d, %6d}, "
			"{0x%02X, 0x%02X, 0x%02X, 0x%02X}}}",
		"{{{%6d, %6d, %6d}, %d, {%6d, %6d}, "
			"{%4d, %4d, %4d, 0x%02X}}}",
	)[n] % (x, y, z, f, s, t, r, g, b, a)]
d_Vtx = [False, d_Vtx_prc]

def g_words(self, w, n):
	for _ in range(n):
		w0 = self.u32()
		w1 = self.u32()
		if w0 is None or w1 is None: return False
		w.append((w0, w1))
	return True

def g_calc_lrs(width, height, siz):
	return min(0x7FF, ((width*height+(3,1,0,0)[siz]) >> (2,1,0,0)[siz])-1)

def g_calc_dxt(width, siz):
	w = max(1, width << siz >> 4)
	return (0x7FF+w) // w

def g_calc_line(width, siz):
	return ((width << siz >> 1) + 7) >> 3

g_im_fmt = (
	"G_IM_FMT_RGBA",
	"G_IM_FMT_YUV",
	"G_IM_FMT_CI",
	"G_IM_FMT_IA",
	"G_IM_FMT_I",
)

def g_im_siz(siz):
	return "G_IM_SIZ_%db" % (4 << siz)

def g_tx_cm(cm):
	return (
		"G_TX_WRAP",
		"G_TX_MIRROR",
		"G_TX_CLAMP",
		"G_TX_CLAMP|G_TX_MIRROR",
	)[cm]

def g_tx_mask(mask):
	return "G_TX_NOMASK" if mask == 0 else "%d" % mask

def g_tx_lod(lod):
	return "G_TX_NOLOD" if lod == 0 else "%d" % lod

def g_tx_tile(tile):
	if tile == 0:   return "G_TX_RENDERTILE"
	if tile == 7:   return "G_TX_LOADTILE"
	return "%d" % tile

def g_null(self, argv):
	self.addr += 8
	return argv

def g_mtx(self, argv):
	w0 = self.u32()
	m = aw(self)
	if not m.startswith("0x"): m = "&" + m
	p = w0 >> 16 & 0xFF
	a = "G_MTX_PROJECTION" if p & 1 else "G_MTX_MODELVIEW"
	b = "G_MTX_LOAD"       if p & 2 else "G_MTX_MUL"
	c = "G_MTX_PUSH"       if p & 4 else "G_MTX_NOPUSH"
	return ("SPMatrix", m, (a, b, c))

def g_vtx(self, argv):
	w0 = self.u32()
	w1 = self.u32()
	imm = self.get_imm(self.save)
	if imm is not None:
		v = ultra.fmt_addr(self, w1, addr=True, array=(imm, 0x10))
	else:
		v = ultra.fmt_addr(self, w1)
	n  = "%d" % (w0 >>  4 & 0xFFF)
	v0 = "%d" % (w0 >> 16 & 15)
	return ("SPVertex", v, n, v0)

def g_dl(self, argv):
	w0 = self.u32()
	w1 = self.u32()
	cmd = ("SPDisplayList", "SPBranchList")[w0 >> 16 & 0xFF]
	dl  = ultra.sym(self, w1, self.save)
	return (cmd, dl)

def g_tri1(self, argv):
	w0 = self.u32()
	w1 = self.u32()
	v0 = "%2d" % ((w1 >> 16 & 0xFF) // 10)
	v1 = "%2d" % ((w1 >>  8 & 0xFF) // 10)
	v2 = "%2d" % ((w1 >>  0 & 0xFF) // 10)
	flag = "%d" % (w1 >> 24)
	return ("SP1Triangle", v0, v1, v2, flag)

g_geometrymode_table = (
	(0x00000001, 0x00000001, "G_ZBUFFER"),
	(0x00000002, 0x00000002, "G_TEXTURE_ENABLE"),
	(0x00000004, 0x00000004, "G_SHADE"),
	(0x00000200, 0x00000200, "G_SHADING_SMOOTH"),
	(0x00003000, 0x00001000, "G_CULL_FRONT"),
	(0x00003000, 0x00002000, "G_CULL_BACK"),
	(0x00003000, 0x00003000, "G_CULL_BOTH"),
	(0x00010000, 0x00010000, "G_FOG"),
	(0x00020000, 0x00020000, "G_LIGHTING"),
	(0x00040000, 0x00040000, "G_TEXTURE_GEN"),
	(0x00080000, 0x00080000, "G_TEXTURE_GEN_LINEAR"),
	(0x00100000, 0x00100000, "G_LOD"),
)

def g_moveword(self, argv):
	w0 = self.u32()
	w1 = self.u32()
	if w0 == 0xBC000002:
		if w1 == 0x80000040:
			a_0  = self.u32()
			a_1  = self.u32()
			d0_0 = self.u32()
			d0_1 = self.u32()
			if a_0 == 0x03860010 and d0_0 == 0x03880010 and a_1-d0_1 == 8:
				imm = self.get_imm(self.save)
				if imm is not None:
					light = ultra.fmt_addr(self, d0_1, array=(imm, 0x18))
				else:
					light = ultra.fmt_addr(self, d0_1)
				return ("SPSetLights1", light)
			self.addr -= 16
		return ("SPNumLights", "NUMLIGHTS_%d" % ((w1-0x80000000)//32-1))
	if w0 == 0xBC000008:
		fm = w1 >> 16
		fo = (w1 & 0xFFFF) - (w1 << 1 & 0x10000)
		d = 128000 // fm
		l = 500 - d*fo//256
		h = l + d
		return ("SPFogPosition", "%d" % l, "%d" % h)
	return None

def g_texture_prc(s, t, w0):
	level = w0 >> 11 & 7
	tile  = w0 >>  8 & 7
	on    = ("G_OFF", "G_ON")[w0 & 0xFF]
	level = g_tx_lod(level)
	tile  = g_tx_tile(tile)
	return ("SPTexture", s, t, level, tile, on)

def g_texture(self, argv):
	w0 = self.u32()
	w1 = self.u32()
	s = "0x%04X" % (w1 >> 16)
	t = "0x%04X" % (w1 & 0xFFFF)
	return g_texture_prc(s, t, w0)

def g_geometrymode(self, argv):
	cmd, = argv
	self.addr += 4
	w1 = self.u32()
	if w1 == 0xFFFFFFFF: flag = ["~0"]
	else: flag = [s for m, i, s in g_geometrymode_table if (w1 & m) == i]
	return (cmd, flag)

g_setothermode_h = {
	# 23
	20: ("DPSetCycleType", {
		0<<20: "G_CYC_1CYCLE",
		1<<20: "G_CYC_2CYCLE",
		2<<20: "G_CYC_COPY",
		3<<20: "G_CYC_FILL",
	}),
	19: ("DPSetTexturePersp", {
		0<<19: "G_TP_NONE",
		1<<19: "G_TP_PERSP",
	}),
	# 17 textdetail
	17: ("DPSetTextureDetail", {
		0<<17: "G_TD_CLAMP",
		1<<17: "G_TD_SHARPEN",
		2<<17: "G_TD_DETAIL",
	}),
	16: ("DPSetTextureLOD", {
		0<<16: "G_TL_TILE",
		1<<16: "G_TL_LOD",
	}),
	14: ("DPSetTextureLUT", {
		0<<14: "G_TT_NONE",
		2<<14: "G_TT_RGBA16",
		3<<14: "G_TT_IA16",
	}),
	12: ("DPSetTextureFilter", {
		0<<12: "G_TF_POINT",
		2<<12: "G_TF_BILERP",
		3<<12: "G_TF_AVERAGE",
	}),
	9: ("DPSetTextureConvert", {
		0<<9: "G_TC_CONV",
		5<<9: "G_TC_FILTCONV",
		6<<9: "G_TC_FILT",
	}),
	8: ("DPSetCombineKey", {
		0<<8: "G_CK_NONE",
		1<<8: "G_CK_KEY",
	}),
	6: ("DPSetColorDither", {
		0<<6: "G_CD_MAGICSQ",
		1<<6: "G_CD_BAYER",
		2<<6: "G_CD_NOISE",
		3<<6: "G_CD_DISABLE",
	}),
	# 4 alphadither
}

g_setothermode_l = {
	3: ("DPSetRenderMode", {
		0x00552078: "G_RM_AA_ZB_OPA_SURF, G_RM_AA_ZB_OPA_SURF2", # 0
		0x00442078: "G_RM_AA_ZB_OPA_SURF, G_RM_NOOP2", # 42
		0x004049D8: "G_RM_AA_ZB_XLU_SURF, G_RM_NOOP2", # 87
		0x004049F8: "G_RM_AA_ZB_XLU_SURF|Z_UPD, G_RM_NOOP2",
        0x00442D58: "G_RM_AA_ZB_OPA_DECAL, G_RM_NOOP2", # 132
		0x00442478: "G_RM_AA_ZB_OPA_INTER, G_RM_NOOP2", # 222
		0x00553078: "G_RM_AA_ZB_TEX_EDGE, G_RM_AA_ZB_TEX_EDGE2", # 368
		0x00443078: "G_RM_AA_ZB_TEX_EDGE, G_RM_NOOP2", # 402
		0x00552048: "G_RM_AA_OPA_SURF, G_RM_AA_OPA_SURF2", # 828
		0x005041C8: "G_RM_AA_XLU_SURF, G_RM_AA_XLU_SURF2", # 874
		0x00553048: "G_RM_AA_TEX_EDGE, G_RM_AA_TEX_EDGE2", # 1012
		0x0F0A4000: "G_RM_OPA_SURF, G_RM_OPA_SURF2", # 1656
		0x00504240: "G_RM_XLU_SURF, G_RM_XLU_SURF2", # 1702
		0x00404240: "G_RM_XLU_SURF, G_RM_NOOP2", # 1707
		0x0F0A7008: "G_RM_TEX_EDGE, G_RM_TEX_EDGE2", # 1794
		0xC8112078: "G_RM_FOG_SHADE_A, G_RM_AA_ZB_OPA_SURF2", # 2025
		0xC8112D58: "G_RM_FOG_SHADE_A, G_RM_AA_ZB_OPA_DECAL2", # 2027
		0xC8113078: "G_RM_FOG_SHADE_A, G_RM_AA_ZB_TEX_EDGE2", # 2033
	}),
	2: ("DPSetDepthSource", {
		0<<2: "G_ZS_PIXEL",
		1<<2: "G_ZS_PRIM",
	}),
	0: ("DPSetAlphaCompare", {
		0<<0: "G_AC_NONE",
		1<<0: "G_AC_THRESHOLD",
		3<<0: "G_AC_DITHER",
	}),
}

def g_setothermode(self, argv):
	arg, = argv
	w0 = self.u32()
	w1 = self.u32()
	shift = w0 >> 8 & 0xFF
	if shift not in arg: raise RuntimeError("%02X %d" % (w0 >> 24, shift))
	cmd, table = arg[w0 >> 8 & 0xFF]
	if w1 not in table: raise RuntimeError("%s %08X" % (cmd, w1))
	flag = table[w1]
	return (cmd, flag)

def g_perspnorm(self, argv):
	self.addr += 6
	s = "0x%04X" % self.u16()
	return ("SPPerspNormalize", s)

def gx_settimg(w0, w1):
	return (w0 >> 21 & 7, w0 >> 19 & 3, (w0 & 0xFFF) + 1, w1)

def gx_settile(w0, w1):
	return (
		w0 >> 21 & 7, # fmt
		w0 >> 19 & 3, # siz
		w0 >>  9 & 0x1FF, # line
		w0       & 0x1FF, # tmem
		w1 >> 24 & 7, # tile
		w1 >> 20 & 15, # palette
		w1 >> 18 & 3, w1 >> 14 & 15, w1 >> 10 & 15, # cmt maskt shiftt
		w1 >>  8 & 3, w1 >>  4 & 15, w1       & 15, # cms masks shifts
	)

def gx_tile(w0, w1):
	return (
		w1 >> 24 & 7,
		w0 >> 12 & 0xFFF, w0 & 0xFFF,
		w1 >> 12 & 0xFFF, w1 & 0xFFF,
	)

def timgproc(self, addr):
	if addr >> 24 == 0x09:
		if self.get_seg(self.save) == self.seg:
			print("\t0x%08X: \"E0.Texture\"," % self.save)

def g_settimg(self, argv):
	w = []
	if g_words(self, w, 7):
		c0_f, c0_s, c0_w, c0_i = gx_settimg(w[0][0], w[0][1])
		if tuple([x[0] >> 24 for x in w]) == (
			0xFD, 0xF5, 0xE6, 0xF3, 0xE7, 0xF5, 0xF2
		):
			c1_fmt, c1_siz, c1_line, c1_tmem, c1_tile, c1_palette, c1_cmt, \
				c1_maskt, c1_shiftt, c1_cms, c1_masks, c1_shifts = \
				gx_settile(w[1][0], w[1][1])
			c3_tile, c3_uls, c3_ult, c3_lrs, c3_dxt = gx_tile(w[3][0], w[3][1])
			c5_fmt, c5_siz, c5_line, c5_tmem, c5_tile, c5_palette, c5_cmt, \
				c5_maskt, c5_shiftt, c5_cms, c5_masks, c5_shifts = \
				gx_settile(w[5][0], w[5][1])
			c6_t, c6_uls, c6_ult, c6_lrs, c6_lrt = gx_tile(w[6][0], w[6][1])
			timg    = c0_i
			fmt     = c5_fmt
			siz     = c5_siz
			width   = (c6_lrs >> 2) + 1
			height  = (c6_lrt >> 2) + 1
			pal     = c5_palette
			cms     = c5_cms
			cmt     = c5_cmt
			masks   = c5_masks
			maskt   = c5_maskt
			shifts  = c5_shifts
			shiftt  = c5_shiftt
			if (
				c0_f, c0_s, c0_w, c0_i,
				c1_fmt, c1_siz, c1_line, c1_tmem, c1_tile, c1_palette,
				c1_cmt, c1_maskt, c1_shiftt, c1_cms, c1_masks, c1_shifts,
				c3_tile, c3_uls, c3_ult, c3_lrs, c3_dxt,
				c5_fmt, c5_siz, c5_line, c5_tmem, c5_tile, c5_palette,
				c5_cmt, c5_maskt, c5_shiftt, c5_cms, c5_masks, c5_shifts,
				c6_t, c6_uls, c6_ult, c6_lrs, c6_lrt,
			) == (
				fmt, (2,2,2,3)[siz], 1, timg,
				fmt, (2,2,2,3)[siz], 0, 0, 7, 0,
				cmt, maskt, shiftt, cms, masks, shifts,
				7, 0, 0, g_calc_lrs(width, height, siz), g_calc_dxt(width, siz),
				fmt, siz, g_calc_line(width, siz), 0, 0, pal,
				cmt, maskt, shiftt, cms, masks, shifts,
				0, 0, 0, (width-1) << 2, (height-1) << 2,
			):
				timgproc(self, timg)
				timg    = ultra.sym(self, timg, self.save)
				fmt     = g_im_fmt[fmt]
				width   = "%d" % width
				height  = "%d" % height
				pal     = "%d" % pal
				cms     = g_tx_cm(cms)
				cmt     = g_tx_cm(cmt)
				masks   = g_tx_mask(masks)
				maskt   = g_tx_mask(maskt)
				shifts  = "%d" % shifts
				shiftt  = "%d" % shiftt
				arg = (
					width, height, pal,
					cms, cmt, masks, maskt, shifts, shiftt
				)
				if siz == 0:
					return ("DPLoadTextureBlock_4b", timg, fmt) + arg
				siz = g_im_siz(siz)
				return ("DPLoadTextureBlock", timg, fmt, siz) + arg
	self.addr = self.save
	w0 = self.u32()
	w1 = self.u32()
	f, s, w, i = gx_settimg(w0, w1)
	f = g_im_fmt[f]
	s = "G_IM_SIZ_%db" % (4 << s)
	w = "%d" % w
	i = ultra.sym(self, i, self.save)
	return ("DPSetTextureImage", f, s, w, i)

g_setcombine_cc_a = {
	0:  "COMBINED",
	1:  "TEXEL0",
	2:  "TEXEL1",
	3:  "PRIMITIVE",
	4:  "SHADE",
	5:  "ENVIRONMENT",
	6:  "1",
	7:  "NOISE",
	15: "0",
}

g_setcombine_cc_b = {
	0:  "COMBINED",
	1:  "TEXEL0",
	2:  "TEXEL1",
	3:  "PRIMITIVE",
	4:  "SHADE",
	5:  "ENVIRONMENT",
	6:  "CENTER",
	7:  "K4",
	15: "0",
}

g_setcombine_cc_c = {
	0:  "COMBINED",
	1:  "TEXEL0",
	2:  "TEXEL1",
	3:  "PRIMITIVE",
	4:  "SHADE",
	5:  "ENVIRONMENT",
	6:  "SCALE",
	7:  "COMBINED_ALPHA",
	8:  "TEXEL0_ALPHA",
	9:  "TEXEL1_ALPHA",
	10: "PRIMITIVE_ALPHA",
	11: "SHADE_ALPHA",
	12: "ENV_ALPHA",
	13: "LOD_FRACTION",
	14: "PRIM_LOD_FRAC",
	15: "K5",
	31: "0",
}

g_setcombine_cc_d = {
	0: "COMBINED",
	1: "TEXEL0",
	2: "TEXEL1",
	3: "PRIMITIVE",
	4: "SHADE",
	5: "ENVIRONMENT",
	6: "1",
	7: "0",
}

g_setcombine_ac_a = g_setcombine_cc_d

g_setcombine_ac_b = g_setcombine_cc_d

g_setcombine_ac_c = {
	0: "LOD_FRACTION",
	1: "TEXEL0",
	2: "TEXEL1",
	3: "PRIMITIVE",
	4: "SHADE",
	5: "ENVIRONMENT",
	6: "PRIM_LOD_FRAC",
	7: "0",
}

g_setcombine_ac_d = g_setcombine_cc_d

g_cc_combined   = ("0", "0", "0", "COMBINED")
g_cc_texel0     = ("0", "0", "0", "TEXEL0")
g_cc_prim       = ("0", "0", "0", "PRIMITIVE")
g_cc_shade      = ("0", "0", "0", "SHADE")
g_cc_0          = ("0", "0", "0", "0")
g_cc_co_pr      = ("COMBINED", "0", "PRIMITIVE", "0")
g_cc_co_sh      = ("COMBINED", "0", "SHADE", "0")
g_cc_t0_t1      = ("TEXEL0", "0", "TEXEL1", "0")
g_cc_t0_pr      = ("TEXEL0", "0", "PRIMITIVE", "0")
g_cc_t0_sh      = ("TEXEL0", "0", "SHADE", "0")
g_cc_t0_sh_t0a  = ("TEXEL0", "SHADE", "TEXEL0_ALPHA", "SHADE")
g_cc_pr_t0_lf   = ("PRIMITIVE", "TEXEL0", "LOD_FRACTION", "TEXEL0")
g_cc_pr_sh_t0   = ("PRIMITIVE", "SHADE", "TEXEL0", "SHADE")
g_cc_pr_en_t0   = ("PRIMITIVE", "ENVIRONMENT", "TEXEL0", "ENVIRONMENT")
g_cc_en_co_t0   = ("ENVIRONMENT", "COMBINED", "TEXEL0", "COMBINED")
g_cc_en_pr_t0   = ("ENVIRONMENT", "PRIMITIVE", "TEXEL0", "PRIMITIVE")
g_cc_en_sh_co   = ("ENVIRONMENT", "SHADE", "COMBINED", "SHADE")
g_cc_en_sh_t0   = ("ENVIRONMENT", "SHADE", "TEXEL0", "SHADE")
g_cc_t1_t0_lf   = ("TEXEL1", "TEXEL0", "LOD_FRACTION", "TEXEL0")
g_cc_t1_t0_pf   = ("TEXEL1", "TEXEL0", "PRIM_LOD_FRAC", "TEXEL0")
g_cc_1_0_t0_sh  = ("1", "0", "TEXEL0", "SHADE")
g_cc_en_0_t0_sh = ("ENVIRONMENT", "0", "TEXEL0", "SHADE")
g_cc_yuv0       = ("TEXEL0", "K4", "K5", "TEXEL0")
g_cc_yuv1       = ("TEXEL1", "K4", "K5", "TEXEL1")
g_cc_chromakey  = ("TEXEL0", "CENTER", "SCALE", "0")

g_setcombine_mode = {
	g_cc_prim       + g_cc_prim:        "G_CC_PRIMITIVE",
	g_cc_shade      + g_cc_shade:       "G_CC_SHADE",
	g_cc_t0_sh      + g_cc_shade:       "G_CC_MODULATERGB",
	g_cc_t0_sh      + g_cc_t0_sh:       "G_CC_MODULATERGBA",
	g_cc_t0_sh      + g_cc_texel0:      "G_CC_MODULATERGBDECALA",
	g_cc_t0_pr      + g_cc_prim:        "G_CC_MODULATERGB_PRIM",
	g_cc_t0_pr      + g_cc_t0_pr:       "G_CC_MODULATERGBA_PRIM",
	g_cc_t0_pr      + g_cc_texel0:      "G_CC_MODULATERGBDECALA_PRIM",
	g_cc_texel0     + g_cc_shade:       "G_CC_DECALRGB",
	g_cc_texel0     + g_cc_texel0:      "G_CC_DECALRGBA",
	g_cc_en_sh_t0   + g_cc_shade:       "G_CC_BLENDI",
	g_cc_en_sh_t0   + g_cc_t0_sh:       "G_CC_BLENDIA",
	g_cc_en_sh_t0   + g_cc_texel0:      "G_CC_BLENDIDECALA",
	g_cc_t0_sh_t0a  + g_cc_shade:       "G_CC_BLENDRGBA",
	g_cc_t0_sh_t0a  + g_cc_texel0:      "G_CC_BLENDRGBDECALA",
	g_cc_1_0_t0_sh  + g_cc_shade:       "G_CC_ADDRGB",
	g_cc_1_0_t0_sh  + g_cc_texel0:      "G_CC_ADDRGBDECALA",
	g_cc_en_0_t0_sh + g_cc_shade:       "G_CC_REFLECTRGB",
	g_cc_en_0_t0_sh + g_cc_texel0:      "G_CC_REFLECTRGBDECALA",
	g_cc_pr_sh_t0   + g_cc_shade:       "G_CC_HILITERGB",
	g_cc_pr_sh_t0   + g_cc_pr_sh_t0:    "G_CC_HILITERGBA",
	g_cc_en_sh_t0   + g_cc_texel0:      "G_CC_HILITERGBDECALA",
	g_cc_shade      + g_cc_texel0:      "G_CC_SHADEDECALA",
	g_cc_pr_en_t0   + g_cc_t0_sh:       "G_CC_BLENDPE",
	g_cc_pr_en_t0   + g_cc_texel0:      "G_CC_BLENDPEDECALA",
	g_cc_en_pr_t0   + g_cc_t0_sh:       "_G_CC_BLENDPE",
	g_cc_en_pr_t0   + g_cc_texel0:      "_G_CC_BLENDPEDECALA",
	g_cc_pr_sh_t0   + g_cc_shade:       "_G_CC_TWOCOLORTEX",
	g_cc_pr_t0_lf   + g_cc_pr_t0_lf:    "_G_CC_SPARSEST",
	g_cc_t1_t0_pf   + g_cc_t1_t0_pf:    "G_CC_TEMPLERP",
	g_cc_t1_t0_lf   + g_cc_t1_t0_lf:    "G_CC_TRILERP",
	g_cc_t0_t1      + g_cc_t0_t1:       "G_CC_INTERFERENCE",
	g_cc_yuv0       + g_cc_shade:       "G_CC_1CYUV2RGB",
	g_cc_yuv1       + g_cc_0:           "G_CC_YUV2RGB",
	g_cc_combined   + g_cc_combined:    "G_CC_PASS2",
	g_cc_co_sh      + g_cc_shade:       "G_CC_MODULATERGB2",
	g_cc_co_sh      + g_cc_co_sh:       "G_CC_MODULATERGBA2",
	g_cc_co_pr      + g_cc_prim:        "G_CC_MODULATERGB_PRIM2",
	g_cc_co_pr      + g_cc_co_pr:       "G_CC_MODULATERGBA_PRIM2",
	g_cc_combined   + g_cc_shade:       "G_CC_DECALRGB2",
	g_cc_en_sh_co   + g_cc_shade:       "G_CC_BLENDI2",
	g_cc_en_sh_co   + g_cc_co_sh:       "G_CC_BLENDIA2",
	g_cc_chromakey  + g_cc_0:           "G_CC_CHROMA_KEY2",
	g_cc_en_co_t0   + g_cc_shade:       "G_CC_HILITERGB2",
	g_cc_en_co_t0   + g_cc_en_co_t0:    "G_CC_HILITERGBA2",
	g_cc_en_co_t0   + g_cc_texel0:      "G_CC_HILITERGBDECALA2",
	g_cc_en_co_t0   + g_cc_combined:    "G_CC_HILITERGBPASSA2",
}

def g_setcombine_prc(self, mode):
	w0 = self.u32()
	w1 = self.u32()
	c0 = (
		g_setcombine_cc_a[w0 >> 20 & 15],
		g_setcombine_cc_b[w1 >> 28 & 15],
		g_setcombine_cc_c[w0 >> 15 & 31],
		g_setcombine_cc_d[w1 >> 15 &  7],
		g_setcombine_ac_a[w0 >> 12 &  7],
		g_setcombine_ac_b[w1 >> 12 &  7],
		g_setcombine_ac_c[w0 >>  9 &  7],
		g_setcombine_ac_d[w1 >>  9 &  7],
	)
	c1 = (
		g_setcombine_cc_a[w0 >>  5 & 15],
		g_setcombine_cc_b[w1 >> 24 & 15],
		g_setcombine_cc_c[w0 >>  0 & 31],
		g_setcombine_cc_d[w1 >>  6 &  7],
		g_setcombine_ac_a[w1 >> 21 &  7],
		g_setcombine_ac_b[w1 >>  3 &  7],
		g_setcombine_ac_c[w1 >> 18 &  7],
		g_setcombine_ac_d[w1 >>  0 &  7],
	)
	if c0 in mode and c1 in mode:
		return ("DPSetCombineMode", mode[c0], mode[c1])
	return ("DPSetCombineLERP",) + c0 + (None,) + c1

def g_setcombine(self, argv):
	return g_setcombine_prc(self, g_setcombine_mode)

def g_setrgba(self, argv):
	cmd, = argv
	self.addr += 4
	r = "0x%02X" % self.u8()
	g = "0x%02X" % self.u8()
	b = "0x%02X" % self.u8()
	a = "0x%02X" % self.u8()
	return (cmd, r, g, b, a)

def g_setprimcolor(self, argv):
	self.addr += 2
	m = "%d" % self.u8()
	l = "%d" % self.u8()
	r = "0x%02X" % self.u8()
	g = "0x%02X" % self.u8()
	b = "0x%02X" % self.u8()
	a = "0x%02X" % self.u8()
	return ("DPSetPrimColor", m, l, r, g, b, a)

def g_settile(self, argv):
	w0 = self.u32()
	w1 = self.u32()
	fmt, siz, line, tmem, tile, palette, cmt, maskt, shiftt, cms, masks, \
		shifts = gx_settile(w0, w1)
	fmt     = g_im_fmt[fmt]
	siz     = g_im_siz(siz)
	line    = "%d" % line
	tmem    = "%d" % tmem
	tile    = g_tx_tile(tile)
	palette = "%d" % palette
	shiftt  = "%d" % shiftt
	shifts  = "%d" % shifts
	if (tile, cmt, maskt, cms, masks) == ("G_TX_LOADTILE", 0, 0, 0, 0):
		cmt     = "0"
		maskt   = "0"
		cms     = "0"
		masks   = "0"
	else:
		cmt     = g_tx_cm(cmt)
		maskt   = g_tx_mask(maskt)
		cms     = g_tx_cm(cms)
		masks   = g_tx_mask(masks)
	return (
		"DPSetTile", fmt, siz, line, tmem, tile, palette,
		cmt, maskt, shiftt,
		cms, masks, shifts,
	)

def g_noop(self, argv):
	w0 = self.u32()
	w1 = self.u32()
	return ("DPSetBlendMask", "15")

gfx_table = {
	0x01: (g_mtx,),
	0x04: (g_vtx,),
	0x06: (g_dl,),
	0xBF: (g_tri1,),
	# 0xBD
	0xBC: (g_moveword,),
	0xBB: (g_texture,),
	0xBA: (g_setothermode, g_setothermode_h),
	0xB9: (g_setothermode, g_setothermode_l),
	0xB8: (g_null, "SPEndDisplayList"),
	0xB7: (g_geometrymode, "SPSetGeometryMode"),
	0xB6: (g_geometrymode, "SPClearGeometryMode"),
	0xB4: (g_perspnorm,),
	0xFD: (g_settimg,),
	0xFC: (g_setcombine,),
	0xFB: (g_setrgba, "DPSetEnvColor"),
	0xFA: (g_setprimcolor,),
	0xF9: (g_setrgba, "DPSetBlendColor"),
	0xF8: (g_setrgba, "DPSetFogColor"),
	0xF5: (g_settile,),
	0xE7: (g_null, "DPPipeSync"),
	0xC0: (g_noop,),
}

def gfx_prc(tab, cmd, argv):
	y = []
	for x in argv:
		if type(x) == str:  y.append(x)
		else:               y.append("|".join(x))
	return "gs%s(%s)," % (cmd, ", ".join(y))

def d_Gfx_prc(self, line, tab, argv):
	end, = argv
	table = [self.meta.c.gfx_table, gfx_table]
	while self.addr < end:
		f_data_push(self, line)
		cmd = self.u8()
		for t in table:
			if cmd in t:
				self.addr = self.save
				p = t[cmd]
				c = p[0](self, p[1:])
				if c is not None:
					line[-1][-1].append(gfx_prc(tab, c[0], c[1:]))
					break
		else:
			self.addr = self.save
			w0 = self.u32()
			w1 = self.u32()
			line[-1][-1].append(tab + "{{0x%08X, 0x%08X}}," % (w0, w1))
d_Gfx = [True, d_Gfx_prc]

def d_Gfx_cmd_prc(self, argv):
	w0 = self.u32()
	w1 = self.u32()
	if (w0, w1) == (0xB8000000, 0x00000000): return ["gsSPEndDisplayList()"]
	return ["{{0x%08X, 0x%08X}}" % (w0, w1)]
d_Gfx_cmd = [False, d_Gfx_cmd_prc]

def d_OSThreadTail_prc(self, argv):
	next     = aw(self)
	priority = self.s32()
	return ["{%s, %d}" % (next, priority)]
d_OSThreadTail = [False, d_OSThreadTail_prc]

def fmt_vihalf(self, x):
	hi = x >> 16
	lo = x & 0xFFFF
	if hi == 0: return "%d" % lo
	return "%d << 16 | %d" % (hi, lo)

def fmt_viburst(self, x):
	return "%d << 20 | %d << 16 | %d << 8 | %d" % (
		x >> 20 & 0xFF,
		x >> 16 & 0xF,
		x >>  8 & 0xFF,
		x >>  0 & 0xFF,
	)

d_OSViCommonRegs = [
	[0, -1, 1, d_u32, "0x%X"],
	[0, -1, 1, d_u32],
	[0, -1, 1, d_u32, fmt_viburst],
	[0, -1, 1, d_u32],
	[0, -1, 1, d_u32, fmt_vihalf],
	[0, -1, 1, d_u32, fmt_vihalf],
	[0, -1, 1, d_u32, fmt_vihalf],
	[0, -1, 1, d_u32, fmt_vihalf],
	[0, -1, 1, d_u32],
]

d_OSViFieldRegs = [
	[0, -1, 1, d_u32],
	[0, -1, 1, d_u32, fmt_vihalf],
	[0, -1, 1, d_u32, fmt_vihalf],
	[0, -1, 1, d_u32, fmt_vihalf],
	[0, -1, 1, d_u32],
]

d_OSViMode_fldRegs = [
	[1, -1, d_OSViFieldRegs],
	[1, -1, d_OSViFieldRegs],
]

d_OSViMode = [
	[0, -1, 1, d_u8], [0, 1, 3, None],
	[1, -1, d_OSViCommonRegs],
	[1, -1, d_OSViMode_fldRegs],
]

def f_data_push(self, line):
	global extern
	self.save = self.addr
	sym = self.get_sym(self.save)
	if sym is not None and not (line and line[-1][1] == sym):
		extern = set()
		line.append((self.save, sym, extern, []))
		return True
	return False

def f_data_seq(self, line, seq, tab):
	for cmd in seq:
		start = "{"*cmd[0]
		end   = "}"*cmd[0]
		c = cmd[1]
		if c < 0:
			c = -c
			end += ","
		for _ in range(c):
			f_data_push(self, line)
			if isinstance(cmd[2], list):
				if cmd[0] > 0:
					line[-1][-1].append(tab + start)
					f_data_seq(self, line, cmd[2], tab + "\t")
					line[-1][-1].append(tab + end)
				else:
					f_data_seq(self, line, cmd[2], tab)
			else:
				n = cmd[2]
				t = cmd[3]
				if t is None:
					self.addr += n
				else:
					if type(t) is str:
						if t == "ascii": x = "".join(self.ascii(n))
						if t == "asciz": x = "".join(self.asciz(n))
						line[-1][-1].append(tab + start + self.fmt_str(x) + end)
					else:
						r, p = t
						if r:
							for _ in range(n): p(self, line, tab, cmd[4:])
						else:
							line[-1][-1].append(tab + start + ", ".join([
								("\n\t"+tab).join(p(self, cmd[4:]))
								for _ in range(n)
							]) + end)

def f_data(self, argv):
	seg, start, end, seq = argv
	if start|end == 0 and seq: raise RuntimeError("bad seq %s" % str(seq))
	init(self, seg, start)
	line = []
	f_data_seq(self, line, seq, "")
	if self.addr != end:
		print("warning: bad end %08X:%08X (%08X)" % (start, end, self.addr))
	fmt(self, line)

def f_declare_sym(self, comm, extern, sym):
	if not hasattr(sym, "fmt"): return
	s = "/* 0x%08X */ " % addr if comm else ""
	if extern:
		if "GLOBL" not in sym.flag: return
		if "LOCAL" in sym.flag: return
		s += "extern "
	else:
		if "BALIGN" in sym.flag: s += "BALIGN "
	self.file.data.append(sym.fmt(s, ";") + "\n")

def f_declare(self, argv, comm, extern):
	if len(argv) == 2:
		seg, lst = argv
		for addr in lst:
			f_declare_sym(self, comm, extern, self.meta.sym[seg][addr])
	else:
		seg, start, end = argv
		for addr in sorted(self.meta.sym[seg].keys()):
			if addr < start or addr >= end: continue
			f_declare_sym(self, comm, extern, self.meta.sym[seg][addr])

def f_bss(self, argv):
	f_declare(self, argv, ultra.COMM_VADDR, False)

def f_extern(self, argv):
	f_declare(self, argv, ultra.COMM_EADDR, True)

def f_struct_seq(self, seq, tab=""):
	tab += "\t"
	for cmd in seq:
		if isinstance(cmd, str):
			self.file.data.append(cmd + "\n")
		elif isinstance(cmd, list):
			c    = cmd[1]
			name = cmd[2]
			seq  = cmd[3]
			end  = cmd[4] if len(cmd) > 4 else ""
			self.file.data.append(tab+c+"\n" + tab+"{\n")
			f_struct_seq(self, seq, tab)
			self.file.data.append(tab+"}\n" + tab+name+end+";\n")
		else:
			sym = cmd[1]
			self.file.data.append(sym.fmt(tab, ";") + "\n")

def f_struct(self, argv):
	tbl, = argv
	for size, c, sname, dname, seq in tbl:
		if dname:   self.file.data.append("typedef ")
		if sname:   self.file.data.append("%s %s\n{\n" % (c, sname))
		else:       self.file.data.append("%s\n{\n" % c)
		f_struct_seq(self, seq)
		if dname:   self.file.data.append("}\n%s;\n\n" % dname)
		else:       self.file.data.append("};\n\n")
