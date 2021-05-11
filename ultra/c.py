try:
    import png
except:
    png = None

import main
import ultra
import table

A_ADDR      = 1
A_EXTERN    = 2

extern = None

def init(self, start, data):
    ultra.init(self, start, data)

def fmt(self, lst):
    f = self.file[-1][1]
    last = None
    for addr, sym, extern, line in lst:
        if len(extern) > 0:
            f.append("\n\n")
        for a, s in sorted(extern, key=lambda x: x[0]):
            f.append(s.fmt("/* 0x%08X */ extern " % a, ";") + "\n")
        if len(line) > 1 or line[-1].endswith(",") or line[-1].startswith("#"):
            f.append("\n\n/* 0x%08X */ %s =\n{\n" % (addr, sym.fmt()))
            for ln in line:
                f.append(("%s\n" if ln.startswith("#") else "\t%s\n") % ln)
            f.append("};\n\n")
        else:
            if "\n" in line[0]:
                f.append("\n")
            f.append("/* 0x%08X */ %s =" % (addr, sym.fmt()))
            f.append("\n\t" if len(f[-1]) + 2 + len(line[0]) > 80 else " ")
            f.append(line[0] + ";\n")
            if "\n" in line[0]:
                f.append("\n")

def d_str_prc(argv):
    size, s = argv
    ultra.script.c_addr += size
    return [s]
d_str = [False, d_str_prc]

def d_pathfmt_prc(argv):
    size, fmt, fn = argv
    ultra.script.c_addr += size
    return [fmt % ultra.script.path_join([fn], 1)]
d_pathfmt = [False, d_pathfmt_prc]

d_8     = [False, lambda argv: ["0x%02X"  % ultra.ub()]]
d_s8    = [False, lambda argv: ["%d"      % ultra.sb()]]
d_u8    = [False, lambda argv: ["%d"      % ultra.ub()]]
d_16    = [False, lambda argv: ["0x%04X"  % ultra.uh()]]
d_s16   = [False, lambda argv: ["%d"      % ultra.sh()]]
d_u16   = [False, lambda argv: ["%d"      % ultra.uh()]]
d_32    = [False, lambda argv: ["0x%08X"  % ultra.uw()]]
d_s32   = [False, lambda argv: ["%d"      % ultra.sw()]]
d_u32   = [False, lambda argv: ["%d"      % ultra.uw()]]
d_64    = [False, lambda argv: ["0x%016X" % ultra.ud()]]
d_s64   = [False, lambda argv: ["%d"      % ultra.sd()]]
d_u64   = [False, lambda argv: ["%d"      % ultra.ud()]]
d_f32   = [False, lambda argv: [ultra.fmt_float(ultra.f(), "F", len(argv)==0)]]
d_f64   = [False, lambda argv: [ultra.fmt_float(ultra.d(), "",  len(argv)==0)]]

def d_addr_prc(argv):
    flag = argv[0]
    x = ultra.aw(extern=bool(flag & A_EXTERN))
    if x.startswith("0x"):
        x = "(void *)" + x
    elif x != "NULL":
        if flag & A_ADDR:
            x = "&" + x
        if len(argv) > 1:
            x = "(%s)%s" % (argv[1], x)
    return [x]
d_addr = [False, d_addr_prc]

def d_Lights1_prc(argv):
    r0 = ultra.ub()
    g0 = ultra.ub()
    b0 = ultra.ub()
    ultra.script.c_addr += 5
    r1 = ultra.ub()
    g1 = ultra.ub()
    b1 = ultra.ub()
    ultra.script.c_addr += 5
    x = ultra.sb()
    y = ultra.sb()
    z = ultra.sb()
    ultra.script.c_addr += 5
    return [
        "gdSPDefLights1(",
        "\t0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, %d, %d, %d" % (
            r0, g0, b0, r1, g1, b1, x, y, z
        ),
        ")",
    ]
d_Lights1 = [False, d_Lights1_prc]

def d_Vtx_prc(argv):
    n, = argv
    x = ultra.sh()
    y = ultra.sh()
    z = ultra.sh()
    f = ultra.uh()
    u = ultra.sh()
    v = ultra.sh()
    if n == 0:
        r = ultra.ub()
        g = ultra.ub()
        b = ultra.ub()
    else:
        r = ultra.sb()
        g = ultra.sb()
        b = ultra.sb()
    a = ultra.ub()
    return [(
        "{{{%6d, %6d, %6d}, %d, {%6d, %6d}, "
            "{0x%02X, 0x%02X, 0x%02X, 0x%02X}}}",
        "{{{%6d, %6d, %6d}, %d, {%6d, %6d}, "
            "{%4d, %4d, %4d, 0x%02X}}}",
    )[n] % (x, y, z, f, u, v, r, g, b, a)]
d_Vtx = [False, d_Vtx_prc]

def g_calc_lrs(width, height, siz):
    return min(0x7FF, ((width*height+(3,1,0,0)[siz]) >> (2,1,0,0)[siz])-1)

def g_calc_dxt(width, siz):
    w = max(1, width*(1,2,4,8)[siz]//16)
    return (0x7FF+w) // w

def g_calc_line(width, siz):
    return (width*(1,2,4,8)[siz]//2 + 7) >> 3

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
    # c = "G_TX_CLAMP"  if cm & 2 else "G_TX_WRAP"
    # m = "G_TX_MIRROR" if cm & 1 else "G_TX_NOMIRROR"
    # return (c, m)
    return (
        "G_TX_WRAP",
        "G_TX_MIRROR",
        "G_TX_CLAMP",
        "G_TX_CLAMP | G_TX_MIRROR",
    )[cm]

def g_tx_mask(mask):
    return "G_TX_NOMASK" if mask == 0 else "%d" % mask

def g_tx_lod(lod):
    return "G_TX_NOLOD" if lod == 0 else "%d" % lod

def g_tx_tile(tile):
    if tile == 0:
        return "G_TX_RENDERTILE"
    if tile == 7:
        return "G_TX_LOADTILE"
    return "%d" % tile

def g_null(argv):
    ultra.script.c_addr += 8
    return argv

def g_mtx(argv):
    w0 = ultra.uw()
    m = ultra.aw()
    if not m.startswith("0x"):
        m = "&" + m
    p = w0 >> 16 & 0xFF
    a = "G_MTX_PROJECTION" if p & 0x01 else "G_MTX_MODELVIEW"
    b = "G_MTX_LOAD"       if p & 0x02 else "G_MTX_MUL"
    c = "G_MTX_PUSH"       if p & 0x04 else "G_MTX_NOPUSH"
    return ("SPMatrix", m, (a, b, c))

def g_vtx(argv):
    w0 = ultra.uw()
    v  = ultra.aw()
    n  = "%d" % (w0 >>  4 & 0x0FFF)
    v0 = "%d" % (w0 >> 16 & 0x0F)
    return ("SPVertex", v, n, v0)

def g_dl(argv):
    w0 = ultra.uw()
    w1 = ultra.uw()
    cmd = ("SPDisplayList", "SPBranchList")[w0 >> 16 & 0xFF]
    dl  = ultra.sym(w1)
    return (cmd, dl)

def g_tri1(argv):
    w0 = ultra.uw()
    w1 = ultra.uw()
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

def g_moveword(argv):
    w0 = ultra.uw()
    w1 = ultra.uw()
    if w0 == 0xBC000002 and w1 == 0x80000040:
        a_0  = ultra.uw()
        a_1  = ultra.uw()
        d0_0 = ultra.uw()
        d0_1 = ultra.uw()
        if a_0 == 0x03860010 and d0_0 == 0x03880010 and a_1-d0_1 == 8:
            light = ultra.sym(d0_1)
            return ("SPSetLights1", light)
    return None

def g_texture_prc(s, t, w0):
    level = w0 >> 11 & 0x07
    tile  = w0 >>  8 & 0x07
    on    = ("G_OFF", "G_ON")[w0 & 0xFF]
    level = g_tx_lod(level)
    tile  = g_tx_tile(tile)
    return ("SPTexture", s, t, level, tile, on)

def g_texture(argv):
    w0 = ultra.uw()
    w1 = ultra.uw()
    s = "0x%04X" % (w1 >> 16)
    t = "0x%04X" % (w1 & 0xFFFF)
    return g_texture_prc(s, t, w0)

def g_geometrymode(argv):
    cmd, = argv
    ultra.script.c_addr += 4
    w1 = ultra.uw()
    if w1 == 0xFFFFFFFF:
        flag = ["~0"]
    else:
        flag = [s for m, c, s in g_geometrymode_table if (w1 & m) == c]
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
    # 16 textlod
    # 14 textlut
    12: ("DPSetTextureFilter", {
        0<<12: "G_TF_POINT",
        2<<12: "G_TF_BILERP",
        3<<12: "G_TF_AVERAGE",
    }),
    # 9 textconv
    # 8 combkey
    # 6 rgbdither
    # 4 alphadither
}

g_setothermode_l = {
    3: ("DPSetRenderMode", {
        0x00552078: "G_RM_AA_ZB_OPA_SURF, G_RM_AA_ZB_OPA_SURF2",
        0x005041C8: "G_RM_AA_XLU_SURF, G_RM_AA_XLU_SURF2",
        0x0F0A4000: "G_RM_OPA_SURF, G_RM_OPA_SURF2",
        0x00504240: "G_RM_XLU_SURF, G_RM_XLU_SURF2",
        0x00404240: "G_RM_XLU_SURF, G_RM_NOOP2",
    }),
    # 2
    0: ("DPSetAlphaCompare", {
        0<<0: "G_AC_NONE",
        1<<0: "G_AC_THRESHOLD",
        3<<0: "G_AC_DITHER",
    }),
}

def g_setothermode(argv):
    arg, = argv
    w0 = ultra.uw()
    w1 = ultra.uw()
    #print("%08X %08X" % (w0, w1))
    cmd, table = arg[w0 >> 8 & 0xFF]
    flag = table[w1]
    return (cmd, flag)

def g_perspnorm(argv):
    ultra.script.c_addr += 6
    s = "0x%04X" % ultra.uh()
    return ("SPPerspNormalize", s)

def gx_settimg(w0, w1):
    return (w0 >> 21 & 0x07, w0 >> 19 & 0x03, (w0 & 0x0FFF) + 1, w1)

def gx_settile(w0, w1):
    return (
        w0 >> 21 & 0x07, w0 >> 19 & 0x03, w0 >> 9 & 0x1FF, w0 & 0x1FF,
        w1 >> 24 & 0x07, w1 >> 20 & 0x0F, w1 >> 18 & 0x03, w1 >> 14 & 0x0F,
        w1 >> 10 & 0x0F, w1 >> 8 & 0x03, w1 >> 4 & 0x0F, w1 & 0x0F,
    )

def gx_tile(w0, w1):
    return (
        w1 >> 24 & 0x07,
        w0 >> 12 & 0x0FFF, w0 & 0x0FFF,
        w1 >> 12 & 0x0FFF, w1 & 0x0FFF,
    )

def g_settimg(argv):
    w = [(ultra.uw(), ultra.uw()) for _ in range(7)]
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
            timg    = ultra.sym(timg)
            fmt     = g_im_fmt[fmt]
            width   = "%d" % width
            height  = "%d" % height
            pal     = "%d" % pal
            cms     = g_tx_cm(cms)
            cmt     = g_tx_cm(cmt)
            masks   = g_tx_mask(masks)
            maskt   = g_tx_mask(maskt)
            shifts  = g_tx_lod(shifts)
            shiftt  = g_tx_lod(shiftt)
            arg = (
                width, height, pal, None,
                cms, cmt, masks, maskt, shifts, shiftt
            )
            if siz == 0:
                return ("DPLoadTextureBlock_4b", timg, fmt) + arg
            siz = g_im_siz(siz)
            return ("DPLoadTextureBlock", timg, fmt, siz) + arg
    ultra.script.c_addr -= 8*6
    f = g_im_fmt[c0_f]
    s = "G_IM_SIZ_%db" % (4 << c0_s)
    w = "%d" % c0_w
    i = ultra.sym(c0_i)
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

def g_setcombine_prc(mode):
    w0 = ultra.uw()
    w1 = ultra.uw()
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

def g_setcombine(argv):
    return g_setcombine_prc(g_setcombine_mode)

def g_setrgba(argv):
    cmd, = argv
    ultra.script.c_addr += 4
    r = "0x%02X" % ultra.ub()
    g = "0x%02X" % ultra.ub()
    b = "0x%02X" % ultra.ub()
    a = "0x%02X" % ultra.ub()
    return (cmd, r, g, b, a)

def g_settile(argv):
    w0 = ultra.uw()
    w1 = ultra.uw()
    fmt, siz, line, tmem, tile, palette, cmt, maskt, shiftt, cms, masks, \
        shifts = gx_settile(w0, w1)
    fmt     = g_im_fmt[fmt]
    siz     = g_im_siz(siz)
    line    = "%d" % line
    tmem    = "%d" % tmem
    tile    = g_tx_tile(tile)
    palette = "%d" % palette
    cmt     = g_tx_cm(cmt)
    maskt   = g_tx_mask(maskt)
    shiftt  = g_tx_lod(shiftt)
    cms     = g_tx_cm(cms)
    masks   = g_tx_mask(masks)
    shifts  = g_tx_lod(shifts)
    return (
        "DPSetTile", fmt, siz, line, tmem, tile, palette, None,
        cmt, maskt, shiftt, None,
        cms, masks, shifts,
    )

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
    0xF9: (g_setrgba, "DPSetBlendColor"),
    0xF5: (g_settile,),
    0xE7: (g_null, "DPPipeSync"),
}

def gfx_prc(tab, cmd, argv):
    lst = []
    for i, x in enumerate(argv):
        end = "" if i == len(argv)-1 else ","
        if x == None:
            lst.append(None)
        elif type(x) == str:
            lst.append(x+end)
        else:
            f = " | ".join(x) + end
            if 8+len(f) <= 80:
                lst.append(f)
            else:
                lst.append("")
                for i, f in enumerate(x):
                    f += end if i == len(x)-1 else " |"
                    if 8+len(lst[-1])+1+len(f) > 80:
                        lst.append("")
                    if len(lst[-1]) > 0:
                        lst[-1] += " "
                    lst[-1] += f
    cmd = "gs%s(" % cmd
    if None not in lst:
        a = " ".join(lst)
        if 4*len(tab) + 4+len(cmd)+len(a)+2 <= 80:
            return cmd + a + "),"
    line = [cmd, "\t"]
    for x in lst:
        if x == None:
            line.append("\t")
        else:
            if 4*len(tab) + 4+len(line[-1])+1+len(x) > 80:
                line.append("\t")
            if len(line[-1]) > 1:
                line[-1] += " "
            line[-1] += x
    line.append("),")
    return ("\n\t"+tab).join(line)

def d_Gfx_prc(self, line, tab, argv):
    end, = argv
    table = [self.meta.gfx_table, gfx_table]
    while self.c_addr < end:
        lst_push(self, line)
        cmd = ultra.ub()
        for t in table:
            if cmd in t:
                self.c_pull()
                f = t[cmd]
                c = f[0](f[1:])
                if c != None:
                    line[-1][-1].append(gfx_prc(tab, c[0], c[1:]))
                    break
        else:
            self.c_pull()
            w0 = ultra.uw()
            w1 = ultra.uw()
            line[-1][-1].append(tab + "{{0x%08X, 0x%08X}}," % (w0, w1))
d_Gfx = [True, d_Gfx_prc]

def d_texture_prc(argv):
    fmt, w, h, name = argv
    f, s, n, g, a, t = {
        "rgba16": (ultra.uh, "0x%04X,", 1, False, True, lambda x: (
            (x >> 11       ) * 0xFF//0x1F,
            (x >>  6 & 0x1F) * 0xFF//0x1F,
            (x >>  1 & 0x1F) * 0xFF//0x1F,
            (x       & 0x01) * 0xFF,
        )),
        "ia4": (ultra.ub, "0x%02X,", 2, True, True, lambda x: (
            (x >> 5       ) * 0xFF//0x07,
            (x >> 4 & 0x01) * 0xFF,
            (x >> 1 & 0x07) * 0xFF//0x07,
            (x      & 0x01) * 0xFF,
        )),
        "ia8": (ultra.ub, "0x%02X,", 1, True, True, lambda x: (
            (x >> 4       ) * 0xFF//0x0F,
            (x      & 0x0F) * 0xFF//0x0F,
        )),
        "ia16": (ultra.uh, "0x%04X,", 1, True, True, lambda x: (
            (x >> 8       ),
            (x      & 0xFF),
        )),
    }[fmt]
    if png != None:
        data = [
            [x for x in [t(f()) for _ in range(w//n)] for x in x]
            for _ in range(h)
        ]
        writer = png.Writer(w, h, greyscale=g, alpha=a)
        fn = ultra.script.path_join(["%s.%s.png" % (name, fmt)])
        main.mkdir(fn)
        with open(fn, "wb") as f:
            writer.write(f, data)
        return ["#include ASSET(%s.%s.h)" % (
            ultra.script.path_join([name], 1), fmt
        )]
    return [" ".join([s % f() for _ in range(w//n)]) for _ in range(h)]
d_texture = [False, d_texture_prc]

def d_OSThreadTail_prc(argv):
    next     = ultra.aw()
    priority = ultra.sw()
    return ["{%s, %d}" % (next, priority)]
d_OSThreadTail = [False, d_OSThreadTail_prc]

d_OSViCommonRegs = [
    [0, -9, 1, d_32],
]

d_OSViFieldRegs = [
    [0, -5, 1, d_32],
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

def lst_push(self, line):
    global extern
    self.c_push()
    sym = table.sym_addr(self, self.c_dst, self.c_dst, True)
    if sym != None and not (len(line) > 0 and line[-1][1] == sym):
        if "-" not in sym.label and "+" not in sym.label:
            extern = set()
            line.append((self.c_dst, sym, extern, []))

def lst_main(self, line, lst, tab):
    for argv in lst:
        start = "{"*argv[0]
        end   = "}"*argv[0]
        c = argv[1]
        if c < 0:
            c = -c
            end += ","
        for _ in range(c):
            lst_push(self, line)
            if type(argv[2]) == list:
                if argv[0] > 0:
                    line[-1][-1].append(tab + start)
                    lst_main(self, line, argv[2], tab + "\t")
                    line[-1][-1].append(tab + end)
                else:
                    lst_main(self, line, argv[2], tab)
            else:
                n = argv[2]
                t = argv[3]
                if t == None:
                    self.c_addr += n
                else:
                    if t == "str":
                        line[-1][-1].append(tab + start + "\"" + "".join([
                            (lambda x: chr(x) if x > 0 else "")(ultra.ub())
                            for _ in range(n)
                        ]) + "\"" + end)
                    else:
                        r, f = t
                        if r:
                            for _ in range(n):
                                f(self, line, tab, argv[4:])
                        else:
                            line[-1][-1].append(tab + start + ", ".join([
                                ("\n"+tab).join(f(argv[4:])) for _ in range(n)
                            ]) + end)

def s_data(self, argv):
    start, end, data, lst = argv
    init(self, start, data)
    line = []
    lst_main(self, line, lst, "")
    fmt(self, line)
