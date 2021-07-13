try:
    import png
except:
    png = None

import main
import table
import ultra
import UNSM

d_bool_s8   = [[0, 1, 1, ultra.c.d_s8,  UNSM.fmt_bool], [0, 1, 3, None]]
d_bool_u8   = [[0, 1, 1, ultra.c.d_u8,  UNSM.fmt_bool], [0, 1, 3, None]]
d_bool_s16  = [[0, 1, 1, ultra.c.d_s16, UNSM.fmt_bool], [0, 1, 2, None]]
d_bool_u16  = [[0, 1, 1, ultra.c.d_u16, UNSM.fmt_bool], [0, 1, 2, None]]

# main.h
# app.h
# audio.h

# game.h

def d_staff_prc(argv):
    stage   = ultra.ub()
    world   = ultra.ub()
    flag    = ultra.ub()
    ry      = ultra.ub()
    x       = ultra.sh()
    y       = ultra.sh()
    z       = ultra.sh()
    ultra.script.c_addr += 2
    s       = ultra.aw()
    return ["{%2d, %d, 0x%02X, 0x%02X, {%5d, %5d, %5d}, %s}" % (
        stage, world, flag, ry, x, y, z, s
    )]
d_staff = [False, d_staff_prc]

# player_touch.h

def d_player_touch_prc(argv):
    flag     = ultra.uw() # T:flag
    callback = ultra.aw()
    return ["{0x%08X, %s}" % (flag, callback)]
d_player_touch = [False, d_player_touch_prc]

# player.h
# player_move.h
# player_demo.h
# player_hang.h
# player_stop.h

# player_ground.h

d_player_ground = [
    [0, -2, 1, ultra.c.d_s16],
    [0, -5, 1, ultra.c.d_u32, "0x%08X"],
]

# player_air.h
# player_water.h
# player_grab.h
# player_callback.h
# mem.h
# save.h
# world.h
# g_draw.h
# time.h
# slidec.h
# camera.h
# course.h

# object.h

def d_particle_prc(argv):
    code    = ultra.uw()
    flag    = ultra.uw()
    shape   = UNSM.fmt_shape(ultra.ub())
    ultra.script.c_addr += 3
    script  = ultra.aw(extern=True)
    if (code, flag, shape, script) == (0, 0, "S_NULL", "NULL"):
        return ["{0}"]
    return ["{0x%08X, 0x%08X, %s, %s}" % (code, flag, shape, script)]
d_particle = [False, d_particle_prc]

# object_lib.h
# object_a.h
# object_move.h
# object_touch.h
# object_list.h
# object_sfx.h
# object_debug.h
# wipe.h

# shadow.h

def d_shadow_rect_prc(argv):
    sx = ultra.fmt_float(ultra.f(), "F")
    sz = ultra.fmt_float(ultra.f(), "F")
    y_scale = UNSM.fmt_bool[ultra.sb()]
    ultra.script.c_addr += 3
    return ["{%s, %s, %s}" % (sx, sz, y_scale)]
d_shadow_rect = [False, d_shadow_rect_prc]

# background.h

# scroll.h

def d_scroll_prc(argv):
    index   = ultra.sw()
    texture = ultra.sw()
    length  = ultra.sw()
    # tmp
    data    = ultra.fmt_addr(ultra.aw(extern=True))
    start   = ultra.fmt_addr(ultra.aw(extern=True))
    end     = ultra.fmt_addr(ultra.aw(extern=True))
    draw    = ultra.fmt_addr(ultra.aw(extern=True))
    r       = ultra.ub()
    g       = ultra.ub()
    b       = ultra.ub()
    a       = ultra.ub()
    layer   = ultra.sw()
    arg0    = (index, texture, length, data)
    arg1    = (start, end, draw)
    arg2    = (r, g, b, a, UNSM.fmt_glayer[layer])
    if arg0+arg1+arg2 == (
        0, 0, 0, "NULL",
        "NULL", "NULL", "NULL",
        0, 0, 0, 0, "G_LAYER_BACKGROUND"
    ):
        return ["{0}"]
    return [
        "{",
            "\t0x%04X, %d, %2d, %s," % arg0,
            "\t%s, %s, %s," % arg1,
            "\t0x%02X, 0x%02X, 0x%02X, 0x%02X, %s," % arg2,
        "}",
    ]
d_scroll = [False, d_scroll_prc]

# object_gfx.h

# ripple.h

def d_ripple_0_prc(argv):
    n = ultra.sh()
    lst = ["%d," % n]
    for _ in range(n):
        x = ultra.sh()
        y = ultra.sh()
        z = ultra.sh()
        lst.append("%d, %d, %d," % (x, y, z))
    return lst
d_ripple_0 = [False, d_ripple_0_prc]

def d_ripple_1_prc(argv):
    end, = argv
    lst = []
    while ultra.script.c_addr < end:
        n = ultra.sh()
        f = [n] + [ultra.sh() for _ in range(n)]
        lst.append(" ".join(["%d," % x for x in f]))
    return lst
d_ripple_1 = [False, d_ripple_1_prc]

# print.h
# message.h
# particle_snow.h
# particle_lava.h

# obj_data.h

def d_obj_data_prc(argv):
    script  = ultra.aw(extern=True)
    shape   = UNSM.fmt_shape(ultra.sh())
    arg     = ultra.sh()
    return ["{%s, %s, %d}" % (script, shape, arg)]
d_obj_data = [False, d_obj_data_prc]

def d_map_obj_prc(argv):
    index   = ultra.ub()
    t       = ultra.ub()
    arg     = ultra.ub()
    shape   = UNSM.fmt_shape(ultra.ub())
    script  = ultra.aw(extern=True)
    return ["{%3d, %d, %d, %s, %s}" % (index, t, arg, shape, script)]
d_map_obj = [False, d_map_obj_prc]

# hud.h

def d_power_prc(argv):
    mode    = ultra.sb()
    ultra.script.c_addr += 1
    x       = ultra.sh()
    y       = ultra.sh()
    ultra.script.c_addr += 2
    scale   = ultra.fmt_float(ultra.f())
    return ["{%d, %d, %d, %s}" % (mode, x, y, scale)]
d_power = [False, d_power_prc]

# object_b.h
# object_c.h

# math.h

def d_bspline_prc(argv):
    time = ultra.sh()
    x    = ultra.sh()
    y    = ultra.sh()
    z    = ultra.sh()
    return ["{%2d, {%5d, %5d, %5d}}" % (time, x, y, z)]
d_bspline = [None, d_bspline_prc]

# g.h
# g_script.h
# s_script.h

# map.h

d_map_face = [
    [0, -1, 2, ultra.c.d_s16],
    [0, -2, 1, ultra.c.d_s8],
    [0, -1, 2, ultra.c.d_s16],
    [1, -3, 3, ultra.c.d_s16],
    [0, -1, 4, ultra.c.d_f32],
    [0, -1, 1, ultra.c.d_addr, 0],
]

# map_data.h
# o_script.h

def d_rendermode_prc(argv):
    return [{
        0x00442078: "G_RM_AA_ZB_OPA_SURF",
        0x00112078: "G_RM_AA_ZB_OPA_SURF2",
        0x004049D8: "G_RM_AA_ZB_XLU_SURF",
        0x001049D8: "G_RM_AA_ZB_XLU_SURF2",
        0x00442D58: "G_RM_AA_ZB_OPA_DECAL",
        0x00112D58: "G_RM_AA_ZB_OPA_DECAL2",
        0x00404DD8: "G_RM_AA_ZB_XLU_DECAL",
        0x00104DD8: "G_RM_AA_ZB_XLU_DECAL2",
        0x00442478: "G_RM_AA_ZB_OPA_INTER",
        0x00112478: "G_RM_AA_ZB_OPA_INTER2",
        0x004045D8: "G_RM_AA_ZB_XLU_INTER",
        0x001045D8: "G_RM_AA_ZB_XLU_INTER2",
        0x00443078: "G_RM_AA_ZB_TEX_EDGE",
        0x00113078: "G_RM_AA_ZB_TEX_EDGE2",
        0x00442048: "G_RM_AA_OPA_SURF",
        0x00112048: "G_RM_AA_OPA_SURF2",
        0x004041C8: "G_RM_AA_XLU_SURF",
        0x001041C8: "G_RM_AA_XLU_SURF2",
        0x00443048: "G_RM_AA_TEX_EDGE",
        0x00113048: "G_RM_AA_TEX_EDGE2",
        0x00442230: "G_RM_ZB_OPA_SURF",
        0x00112230: "G_RM_ZB_OPA_SURF2",
        0x0C084000: "G_RM_OPA_SURF",
        0x03024000: "G_RM_OPA_SURF2",
    }[ultra.uw()]]
d_rendermode = [False, d_rendermode_prc]

d_vp_table = {
}

def d_vp_prc(argv):
    w = ultra.sh() // 2
    h = ultra.sh() // 2
    ultra.script.c_addr += 4
    x = ultra.sh() // 4
    y = ultra.sh() // 4
    ultra.script.c_addr += 4
    return ["gdSPDefViewport(%s, %s, %s, %s)" % tuple([
        d_vp_table[x] if x in d_vp_table else "%d" % x for x in (w, h, x, y)
    ])]
d_vp = [False, d_vp_prc]

def d_light_prc(argv):
    a, = argv
    a = ultra.fmt_float(a)
    ultra.script.c_addr += 8
    r = ultra.ub()
    g = ultra.ub()
    b = ultra.ub()
    ultra.script.c_addr += 13
    return ["gdSPDefLight(%s, 0x%02X, 0x%02X, 0x%02X)" % (a, r, g, b)]
d_light = [False, d_light_prc]

def d_matrix_prc(argv):
    h = [ultra.sh() for i in range(16)]
    l = [ultra.uh() for i in range(16)]
    return ["gdSPDefMatrix("] + ["\t" + " ".join([
        ultra.fmt_float(
            float(h[i] << 16 | l[i]) / 0x10000, "", len(argv) == 0
        ) + ("," if i != 15 else "") for i in range(i, i+4)
    ]) for i in range(0, 16, 4)] + [")"]
d_matrix = [False, d_matrix_prc]

texture_cvt_rgba16 = [
    False, True, 1, ultra.uh, "0x%04X,", lambda x: (
        (x >> 11       ) * 0xFF//0x1F,
        (x >>  6 & 0x1F) * 0xFF//0x1F,
        (x >>  1 & 0x1F) * 0xFF//0x1F,
        (x       & 0x01) * 0xFF,
    )
]
texture_cvt_ia4 = [
    True, True, 2, ultra.ub, "0x%02X,", lambda x: (
        (x >> 5       ) * 0xFF//0x07,
        (x >> 4 & 0x01) * 0xFF,
        (x >> 1 & 0x07) * 0xFF//0x07,
        (x      & 0x01) * 0xFF,
    )
]
texture_cvt_ia8 = [
    True, True, 1, ultra.ub, "0x%02X,", lambda x: (
        (x >> 4       ) * 0x11,
        (x      & 0x0F) * 0x11,
    )
]
texture_cvt_ia16 = [
    True, True, 1, ultra.uh, "0x%04X,", lambda x: (
        (x >> 8       ),
        (x      & 0xFF),
    )
]

def d_texture_prc(argv):
    fmt, w, h, name = argv
    g, a, n, f, s, c = {
        "rgba16":   texture_cvt_rgba16,
        "ia4":      texture_cvt_ia4,
        "ia8":      texture_cvt_ia8,
        "ia16":     texture_cvt_ia16,
    }[fmt]
    if png != None:
        data = [
            [x for x in [c(f()) for _ in range(w//n)] for x in x]
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

def s_ply_vtx(self, argv):
    name, = argv
    self.file[-1][1].append(
        "#include ASSET(%s.vtx.h)\n" % ultra.script.path_join([name], 1)
    )

def d_ply_gfx_prc(argv):
    end, name, light, scale = argv
    alpha = False
    vtx = []
    tri = []
    buf = 16*[None]
    while ultra.script.c_addr < end:
        w0 = ultra.uw()
        w1 = ultra.uw()
        cmd = w0 >> 24
        if cmd == 0x04:
            addr = ultra.script.c_addr
            ultra.script.c_addr = w1
            e = w1 + (w0 & 0xFFFF)
            i = w0 >> 16 & 0x0F
            while ultra.script.c_addr < e:
                x = ultra.sh()
                y = ultra.sh()
                z = ultra.sh()
                ultra.script.c_addr += 2
                s = ultra.sh()
                t = ultra.sh()
                if light:
                    r = ultra.sb()
                    g = ultra.sb()
                    b = ultra.sb()
                else:
                    r = ultra.ub()
                    g = ultra.ub()
                    b = ultra.ub()
                a = ultra.ub()
                buf[i] = (x, y, z, s, t, r, g, b, a)
                i += 1
            ultra.script.c_addr = addr
        elif cmd == 0xBF:
            t = (
                (w1 >> 16 & 0xFF) // 10,
                (w1 >>  8 & 0xFF) // 10,
                (w1       & 0xFF) // 10,
            )
            b = []
            for v in t:
                if buf[v] in vtx:
                    b.append(vtx.index(buf[v]))
                else:
                    b.append(len(vtx))
                    vtx.append(buf[v])
                    if vtx[-1][8] != 0:
                        alpha = True
            tri.append(tuple(b))
        else:
            raise RuntimeError("bad shape gfx 0x%08X : %08X %08X" % (
                ultra.script.c_addr-8, w0, w1
            ))
    path = ultra.script.path_join([name])
    data = ""
    if scale != None:
        w = scale[0]
        h = scale[1]
        s = scale[2] if len(scale) > 2 else 1
        t = scale[3] if len(scale) > 3 else -0.5
        if type(s) == tuple:
            ss, st = s
        else:
            ss = st = s
        if type(t) == tuple:
            ts, tt = t
        else:
            ts = tt = t
        scale = (float(w)/ss, float(h)/st, ts, tt)
        data += "t=%s,%s,%s,%s\n" % tuple([ultra.fmt_float(x) for x in scale])
    if not light:
        data += "s=r,g,b,a\n"
    if len(data) > 0:
        fn = path + ".ini"
        with open(fn, "w") as f:
            f.write(data)
    data = (
        "ply\n"
        "format ascii 1.0\n"
        "comment metarep (UNSM) - %s_%s\n"
        "element vertex %d\n"
        "property short x\n"
        "property short y\n"
        "property short z\n"
    ) % (ultra.script.path[-1], name, len(vtx))
    if scale != None:
        data += (
            "property float s\n"
            "property float t\n"
        )
    if light:
        data += (
            "property float nx\n"
            "property float ny\n"
            "property float nz\n"
        )
    else:
        data += (
            "property uchar red\n"
            "property uchar green\n"
            "property uchar blue\n"
        )
    if alpha:
        data += (
            "property uchar alpha\n"
        )
    data += (
        "element face %d\n"
        "property list uchar uint vertex_indices\n"
        "end_header\n"
    ) % len(tri)
    for v in vtx:
        data += "%d %d %d" % v[:3]
        if scale != None:
            s = (v[3]/32.0 - scale[2]) / scale[0]
            t = (v[4]/32.0 - scale[3]) / scale[1]
            data += " %s %s" % (str(s), str(1.0-t))
        if light:
            nx = v[5]/128.0
            ny = v[6]/128.0
            nz = v[7]/128.0
            data += " %s %s %s" % (str(nx), str(ny), str(nz))
        else:
            data += " %d %d %d" % v[5:8]
        if alpha:
            data += " %d" % v[8]
        data += "\n"
    data += "".join(["3 %d %d %d\n" % t for t in tri])
    fn = path + ".ply"
    main.mkdir(fn)
    with open(fn, "w") as f:
        f.write(data)
    return ["#include ASSET(%s.h)" % ultra.script.path_join([name], 1)]
d_ply_gfx = [False, d_ply_gfx_prc]

def g_movemem(argv):
    a_0  = ultra.uw()
    a_1  = ultra.uw()
    d0_0 = ultra.uw()
    d0_1 = ultra.uw()
    if a_0 == 0x03860010 and d0_0 == 0x03880010 and a_1-d0_1 == 8:
        light = ultra.sym(d0_1)
        return ("SPSetLights1N", light)
    return None

def g_tri1(argv):
    w0_0 = ultra.uw()
    w1_0 = ultra.uw()
    w0_1 = ultra.uw()
    w1_1 = ultra.uw()
    if w0_0 == 0xBF000000 and w0_1 == 0xBF000000:
        v00 = "%2d" % ((w1_0 >> 16 & 0xFF) // 10)
        v01 = "%2d" % ((w1_0 >>  8 & 0xFF) // 10)
        v02 = "%2d" % ((w1_0 >>  0 & 0xFF) // 10)
        flag0 = "%d" % (w1_0 >> 24)
        v10 = "%2d" % ((w1_1 >> 16 & 0xFF) // 10)
        v11 = "%2d" % ((w1_1 >>  8 & 0xFF) // 10)
        v12 = "%2d" % ((w1_1 >>  0 & 0xFF) // 10)
        flag1 = "%d" % (w1_1 >> 24)
        return ("SP2Triangles", v00, v01, v02, flag0, v10, v11, v12, flag1)
    return None

def g_texture(argv):
    w0 = ultra.uw()
    w1 = ultra.uw()
    s = (w1 >> 16) // 62
    t = (w1 & 0xFFFF) // 62
    for x in (s, t):
        if x == 0 or (x & ~(1 << x.bit_length()-1)) != 0:
            return None
    s = "62*%d" % s
    t = "62*%d" % t
    return ultra.c.g_texture_prc(s, t, w0)

def g_loadimageblock(cmd, timg, fmt, siz, width, w):
    tile, uls, ult, lrs, dxt = ultra.c.gx_tile(w[0], w[1])
    if (width, tile, uls, ult) != (1, 7, 0, 0):
        return None
    width  = max(16 >> siz, (0x800 << siz) // dxt)
    height = (lrs+1) // width
    timg   = ultra.sym(timg)
    fmt    = ultra.c.g_im_fmt[fmt]
    siz    = ultra.c.g_im_siz(siz)
    width  = "%d" % width
    height = "%d" % height
    return (cmd, timg, fmt, siz, width, height)

def g_settimg(argv):
    w = [(ultra.uw(), ultra.uw()) for _ in range(3)]
    fmt, siz, width, timg = ultra.c.gx_settimg(w[0][0], w[0][1])
    if tuple([x[0] >> 24 for x in w]) == (0xFD, 0xE6, 0xF3):
        return g_loadimageblock("DPLoadImageBlock", timg, fmt, siz, width, w[2])
    w += [(ultra.uw(), ultra.uw()) for _ in range(2)]
    c = tuple([x[0] >> 24 for x in w])
    if tuple([x[0] >> 24 for x in w]) == (0xFD, 0xE8, 0xF5, 0xE6, 0xF3):
        if ultra.c.gx_settile(w[2][0], w[2][1]) == (
            fmt, siz, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0
        ):
            return g_loadimageblock(
                "DPLoadImageBlockT", timg, fmt, siz, width, w[4]
            )
    return None

def g_rdptilesync(argv):
    w = [(ultra.uw(), ultra.uw()) for _ in range(3)]
    if tuple([x[0] >> 24 for x in w]) == (0xE8, 0xF5, 0xF2):
        fmt, siz, line, tmem, c1_tile, pal, cmt, maskt, shiftt, cms, masks, \
            shifts = ultra.c.gx_settile(w[1][0], w[1][1])
        c2_tile, uls, ult, lrs, lrt = ultra.c.gx_tile(w[2][0], w[2][1])
        width  = (lrs >> 2) + 1
        height = (lrt >> 2) + 1
        if (line, tmem, c1_tile, c2_tile, uls, ult, lrs, lrt) == (
            ultra.c.g_calc_line(width, siz), 0, 0,
            0, 0, 0, (width-1) << 2, (height-1) << 2
        ):
            fmt     = ultra.c.g_im_fmt[fmt]
            siz     = ultra.c.g_im_siz(siz)
            width   = "%d" % width
            height  = "%d" % height
            pal     = "%d" % pal
            cms     = ultra.c.g_tx_cm(cms)
            cmt     = ultra.c.g_tx_cm(cmt)
            masks   = ultra.c.g_tx_mask(masks)
            maskt   = ultra.c.g_tx_mask(maskt)
            shifts  = ultra.c.g_tx_lod(shifts)
            shiftt  = ultra.c.g_tx_lod(shiftt)
            return ("DPSetImageBlock",
                fmt, siz, width, height, pal, None,
                cms, cmt, masks, maskt, shifts, shiftt
            )
    return None

g_cc_env        = ("0", "0", "0", "ENVIRONMENT")
g_cc_t0_en      = ("TEXEL0", "0", "ENVIRONMENT", "0")
g_cc_sh_en      = ("SHADE", "0", "ENVIRONMENT", "0")

g_setcombine_mode = {
    ultra.c.g_cc_shade      + g_cc_env:     "G_CC_SHADE_ENV",
    ultra.c.g_cc_texel0     + g_cc_env:     "G_CC_DECALRGB_ENV",
    ultra.c.g_cc_texel0     + g_cc_t0_en:   "G_CC_DECALRGBA_ENV",
    ultra.c.g_cc_t0_sh_t0a  + g_cc_env:     "G_CC_BLENDRGB_ENVA",
    ultra.c.g_cc_t0_sh      + g_cc_env:     "G_CC_MODULATERGB_ENVA",
    ultra.c.g_cc_t0_sh      + g_cc_t0_en:   "G_CC_MODULATERGBA_ENVA",
    g_cc_t0_en  + g_cc_t0_en:   "G_CC_MODULATERGBA_ENV",
    g_cc_sh_en  + g_cc_sh_en:   "G_CC_MODULATESE",
}

def g_setcombine(argv):
    x = ultra.c.g_setcombine_prc(g_setcombine_mode)
    if len(x) == 3:
        return x
    return None

def g_settile(argv):
    w = [(ultra.uw(), ultra.uw()) for _ in range(5)]
    c = tuple([x[0] >> 24 for x in w])
    if c == (0xF5, 0xE6, 0xF3, 0xF5, 0xF2):
        c0_fmt, c0_siz, c0_line, c0_tmem, c0_tile, c0_palette, c0_cmt, \
            c0_maskt, c0_shiftt, c0_cms, c0_masks, c0_shifts = \
            ultra.c.gx_settile(w[0][0], w[0][1])
        c2_tile, c2_uls, c2_ult, c2_lrs, c2_dxt = \
            ultra.c.gx_tile(w[2][0], w[2][1])
        c3_fmt, c3_siz, c3_line, c3_tmem, c3_tile, c3_palette, c3_cmt, \
            c3_maskt, c3_shiftt, c3_cms, c3_masks, c3_shifts = \
            ultra.c.gx_settile(w[3][0], w[3][1])
        c4_t, c4_uls, c4_ult, c4_lrs, c4_lrt = ultra.c.gx_tile(w[4][0], w[4][1])
        fmt     = c3_fmt
        siz     = c3_siz
        width   = (c4_lrs >> 2) + 1
        height  = (c4_lrt >> 2) + 1
        pal     = c3_palette
        cms     = c3_cms
        cmt     = c3_cmt
        masks   = c3_masks
        maskt   = c3_maskt
        shifts  = c3_shifts
        shiftt  = c3_shiftt
        if (
            c0_fmt, c0_siz, c0_line, c0_tmem, c0_tile, c0_palette,
            c0_cmt, c0_maskt, c0_shiftt, c0_cms, c0_masks, c0_shifts,
            c2_tile, c2_uls, c2_ult, c2_lrs, c2_dxt,
            c3_fmt, c3_siz, c3_line, c3_tmem, c3_tile, c3_palette,
            c3_cmt, c3_maskt, c3_shiftt, c3_cms, c3_masks, c3_shifts,
            c4_t, c4_uls, c4_ult, c4_lrs, c4_lrt,
        ) == (
            fmt, (2,2,2,3)[siz], 0, 0, 7, 0,
            cmt, maskt, shiftt, cms, masks, shifts,
            7, 0, 0, ultra.c.g_calc_lrs(width, height, siz),
            ultra.c.g_calc_dxt(width, siz),
            fmt, siz, ultra.c.g_calc_line(width, siz), 0, 0, pal,
            cmt, maskt, shiftt, cms, masks, shifts,
            0, 0, 0, (width-1) << 2, (height-1) << 2,
        ):
            fmt     = ultra.c.g_im_fmt[fmt]
            width   = "%d" % width
            height  = "%d" % height
            pal     = "%d" % pal
            cms     = ultra.c.g_tx_cm(cms)
            cmt     = ultra.c.g_tx_cm(cmt)
            masks   = ultra.c.g_tx_mask(masks)
            maskt   = ultra.c.g_tx_mask(maskt)
            shifts  = ultra.c.g_tx_lod(shifts)
            shiftt  = ultra.c.g_tx_lod(shiftt)
            arg = (
                width, height, pal, None,
                cms, cmt, None,
                masks, maskt, shifts, shiftt,
            )
            if siz == 0:
                return ("DPLoadTextureBlock_4bN", fmt) + arg
            siz = ultra.c.g_im_siz(siz)
            return ("DPLoadTextureBlockN", fmt, siz) + arg
    return None

gfx_table = {
    0x03: (g_movemem,),
    0xBF: (g_tri1,),
    0xBB: (g_texture,),
    0xFD: (g_settimg,),
    0xFC: (g_setcombine,),
    0xF5: (g_settile,),
    0xE8: (g_rdptilesync,),
}

def s_msg_lang(self, lang, line, s):
    if s != None:
        x = UNSM.exe.lang.table[s]
        if lang != x:
            lang = x
            line.append("$lang: %s\n\n" % s)
    return lang

def s_msg_str(self, lang, line):
    lst = []
    while True:
        x = ultra.ub()
        if x == 0xFF:
            break
        lst.append(x)
    i = 0
    while i < len(lst):
        for s, c in lang:
            n = len(c)
            if lst[i:i+n] == c:
                line.append(s)
                i += n
                break
        else:
            raise RuntimeError("illegal character 0x%02X" % lst[i])
    if not line[-1].endswith("\n"):
        line.append("\n")
    self.c_addr = (self.c_addr+3) & ~3

def s_msg(self, argv):
    start, end, data, m, name, s, table = argv
    ultra.init(self, start, data)
    line = []
    lang = s_msg_lang(self, None, line, s)
    i = 0
    while self.c_addr < end:
        n = None
        if m == 0:
            x = table[i]
            lang = s_msg_lang(self, lang, line, x[1])
            if x[0] == 0:
                cmd, arg = "str", [x[2]]
            else:
                cmd, arg = "multi", [x[2], "%d" % x[3]]
                n = x[3:]
        else:
            x = ultra.uw()
            if x == 0:
                break
            addr = self.c_addr
            self.c_addr = x
            if m == 1:
                cmd, arg = "tbl", []
            else:
                arg = ultra.sw()
                ln  = ultra.sb()
                self.c_addr += 1
                x   = ultra.sh()
                y   = ultra.sh()
                self.c_addr += 2
                self.c_addr = ultra.uw()
                cmd, arg = "msg", ["%d, %d, %d, %d" % (arg, ln, x, y)]
            if table != None and table[i] != None:
                arg.append(table[i])
        i += 1
        line.append("$%s:" % cmd)
        if len(arg) > 0:
            line.append(" " + "; ".join(arg))
        line.append("\n")
        if n != None:
            for _ in range(n[1]):
                self.c_push()
                s_msg_str(self, lang, line)
                self.c_pull()
                self.c_addr += n[0]
        else:
            s_msg_str(self, lang, line)
        line.append("\n")
        if m != 0:
            self.c_addr = addr
    data = "".join(line).rstrip("\n") + "\n"
    fn = self.path_join([name + ".txt"])
    main.mkdir(fn)
    with open(fn, "w") as f:
        f.write(data)
    self.file[-1][1].append(
        "#include ASSET(%s.h)\n" % self.path_join([name], 1)
    )

# 00 02
def sg_call(argv):
    arg = ultra.ub()
    ultra.script.c_addr += 2
    script = ultra.aw()
    if arg == 1:
        return ("call", script)
    return (None, script)

# 01 03 04 05 0B 17
def sg_null(argv):
    ultra.script.c_addr += 3
    return (None,)

# 08
def sg_world(argv):
    ultra.script.c_addr += 1
    n = "%d" % ultra.sh()
    x = "%d" % ultra.sh()
    y = "%d" % ultra.sh()
    w = "%d" % ultra.sh()
    h = "%d" % ultra.sh()
    return (None, x, y, w, h, n)

# 09 20
def sg_arg(argv):
    ultra.script.c_addr += 1
    arg = "%d" % ultra.sh()
    return (None, arg)

# 0A
def sg_persp(argv):
    c    = ultra.ub()
    fovy = "%d" % ultra.sh()
    n    = "%d" % ultra.sh()
    f    = "%d" % ultra.sh()
    if c:
        callback = ultra.aw()
        return ("perspective", fovy, n, f, callback)
    return (None, fovy, n, f)

# 0C
def sg_layer(argv):
    depth = UNSM.fmt_bool[ultra.ub()]
    ultra.script.c_addr += 2
    return (None, depth)

# 0D
def sg_lod(argv):
    ultra.script.c_addr += 3
    a = "%d" % ultra.sh()
    b = "%d" % ultra.sh()
    return (None, a, b)

# 0E 18
def sg_callback(argv):
    ultra.script.c_addr += 1
    arg = "%d" % ultra.sh() # T:enum ?
    callback = ultra.aw()
    return (None, arg, callback)

# 0F
def sg_camera(argv):
    ultra.script.c_addr += 1
    arg = "%d" % ultra.sh() # T:enum
    px  = "%d" % ultra.sh()
    py  = "%d" % ultra.sh()
    pz  = "%d" % ultra.sh()
    lx  = "%d" % ultra.sh()
    ly  = "%d" % ultra.sh()
    lz  = "%d" % ultra.sh()
    callback = ultra.aw()
    return (None, arg, px, py, pz, lx, ly, lz, callback)

# 10
def sg_gfx_posrot(argv):
    arg = ultra.ub()
    x = arg >> 4 & 7
    if x == 0:
        ultra.script.c_addr += 2
        px = "%d" % ultra.sh()
        py = "%d" % ultra.sh()
        pz = "%d" % ultra.sh()
        rx = "%d" % ultra.sh()
        ry = "%d" % ultra.sh()
        rz = "%d" % ultra.sh()
        s = "posrot"
        a = (px, py, pz, rx, ry, rz)
    if x == 1:
        px = "%d" % ultra.sh()
        py = "%d" % ultra.sh()
        pz = "%d" % ultra.sh()
        s = "prp"
        a = (px, py, pz)
    if x == 2:
        rx = "%d" % ultra.sh()
        ry = "%d" % ultra.sh()
        rz = "%d" % ultra.sh()
        s = "prr"
        a = (rx, ry, rz)
    if x == 3:
        ry = "%d" % ultra.sh()
        s = "pry"
        a = (ry,)
    if arg & 0x80:
        layer = UNSM.fmt_glayer[arg & 0x0F][8:]
        ultra.tag = "gfx"
        gfx = ultra.aw(extern=True)
        return ("gfx_"+s, layer, gfx) + a
    return (s,) + a

# 11 12 14 1D
def sg_gfx_arg(argv):
    c, m = argv
    arg = ultra.ub()
    if m == 0:
        x = "%d" % ultra.sh()
        y = "%d" % ultra.sh()
        z = "%d" % ultra.sh()
        a = (x, y, z)
    else:
        ultra.script.c_addr += 2
        s = ultra.fmt_float(ultra.round_cvt(
            lambda x: float(x)/0x10000,
            lambda x: int(0x10000*x),
            ultra.sw()
        ))
        a = (s,)
    if arg & 0x80:
        layer = UNSM.fmt_glayer[arg & 0x0F][8:]
        ultra.tag = "gfx"
        gfx = ultra.aw(extern=True)
        return (c, layer, gfx) + a
    return (None,) + a

# 13
def sg_gfx_pos(argv):
    layer = UNSM.fmt_glayer[ultra.ub()][8:]
    x = "%d" % ultra.sh()
    y = "%d" % ultra.sh()
    z = "%d" % ultra.sh()
    ultra.tag = "gfx"
    gfx = ultra.aw(extern=True)
    return (None, layer, gfx, x, y, z)

# 15
def sg_gfx(argv):
    layer = UNSM.fmt_glayer[ultra.ub()][8:]
    ultra.script.c_addr += 2
    ultra.tag = "gfx"
    gfx = ultra.aw(extern=True)
    return (None, layer, gfx)

# 16
def sg_shadow(argv):
    ultra.script.c_addr += 1
    t     = "%d" % ultra.uh()
    alpha = "0x%02X" % ultra.uh()
    scale = "%d" % ultra.uh()
    return (None, scale, alpha, t)

# 19
def sg_background(argv):
    ultra.script.c_addr += 1
    arg = ultra.sh() # T:enum
    callback = ultra.aw()
    if callback == "NULL":
        r = (arg >> 11 & 0x1F) * 0xFF//0x1F
        g = (arg >>  6 & 0x1F) * 0xFF//0x1F
        b = (arg >>  1 & 0x1F) * 0xFF//0x1F
        a = arg & 1
        arg = "GPACK_RGBA5551(0x%02X, 0x%02X, 0x%02X, %d)" % (r, g, b, a)
    else:
        arg = "%d" % arg
    return (None, arg, callback)

# 1C
def sg_hand(argv):
    arg = "%d" % ultra.ub()
    x = "%d" % ultra.sh()
    y = "%d" % ultra.sh()
    z = "%d" % ultra.sh()
    callback = ultra.aw()
    return (None, x, y, z, arg, callback)

sg_str = (
    "script", # 0x00
    "exit", # 0x01
    "jump", # 0x02
    "return", # 0x03
    "push", # 0x04
    "pull", # 0x05
    None, # 0x06
    None, # 0x07
    "world", # 0x08
    "ortho", # 0x09
    "persp", # 0x0A
    "empty", # 0x0B
    "layer", # 0x0C
    "lod", # 0x0D
    "select", # 0x0E
    "camera", # 0x0F
    "posrot", # 0x10
    "pos", # 0x11
    "rot", # 0x12
    "joint", # 0x13
    "billboard", # 0x14
    "gfx", # 0x15
    "shadow", # 0x16
    "object", # 0x17
    "callback", # 0x18
    "background", # 0x19
    None, # 0x1A
    None, # 0x1B
    "hand", # 0x1C
    "scale", # 0x1D
    None, # 0x1E
    None, # 0x1F
    "cull", # 0x20
)

sg_fnc = (
    (sg_call,), # 0x00
    (sg_null,), # 0x01
    (sg_call,), # 0x02
    (sg_null,), # 0x03
    (sg_null,), # 0x04
    (sg_null,), # 0x05
    None, # 0x06
    None, # 0x07
    (sg_world,), # 0x08
    (sg_arg,), # 0x09
    (sg_persp,), # 0x0A
    (sg_null,), # 0x0B
    (sg_layer,), # 0x0C
    (sg_lod,), # 0x0D
    (sg_callback,), # 0x0E
    (sg_camera,), # 0x0F
    (sg_gfx_posrot,), # 0x10
    (sg_gfx_arg, "gfx_pos", 0), # 0x11
    (sg_gfx_arg, "gfx_rot", 0), # 0x12
    (sg_gfx_pos,), # 0x13
    (sg_gfx_arg, "gfx_billboard", 0), # 0x14
    (sg_gfx,), # 0x15
    (sg_shadow,), # 0x16
    (sg_null,), # 0x17
    (sg_callback,), # 0x18
    (sg_background,), # 0x19
    None, # 0x1A
    None, # 0x1B
    (sg_hand,), # 0x1C
    (sg_gfx_arg, "gfx_scale", 1), # 0x1D
    None, # 0x1E
    None, # 0x1F
    (sg_arg,), # 0x20
)

def s_script_g(self, argv):
    start, end, data = argv
    ultra.c.init(self, start, data)
    ultra.c.extern = set()
    line = []
    while self.c_addr < end:
        self.c_push()
        sym = table.sym_addr(self, self.c_dst, rej=True)
        if sym != None:
            tab = 0
            line.append((
                self.c_dst, sym, set() if len(line) > 0 else ultra.c.extern, []
            ))
        c = ultra.ub()
        f = sg_fnc[c]
        argv = f[0](f[1:])
        s = argv[0] if argv[0] != None else sg_str[c]
        if self.addr == 0x0E000000-0x004EB1F0 and self.c_dst == 0x0E00093C:
            c = 0x05
        if c in {0x05} and tab > 0:
            tab -= 1
        if c in {0x01}:
            tab = 0
        ln = "%sg_%s(%s)," % ("\t"*tab, s, ", ".join(argv[1:]))
        if c in {0x04}:
            tab += 1
        line[-1][-1].append(ln)
    ultra.c.fmt(self, line)
