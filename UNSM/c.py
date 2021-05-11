import table
import ultra
import UNSM

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
    depth = ("false", "true")[ultra.ub()]
    ultra.script.c_addr += 2
    return (None, depth)

# 0D
def sg_lod(argv):
    ultra.script.c_addr += 3
    a = "%d" % ultra.sh()
    b = "%d" % ultra.sh()
    return (None, a, b)

# 0E 18 19
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
        rm = UNSM.rm_table[arg & 0x0F]
        ultra.tag = "gfx"
        gfx = ultra.aw(extern=True)
        return ("gfx_"+s, rm, gfx) + a
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
        s = ultra.fmt_float(round(ultra.uw()/65536.0, 4), "F")
        a = (s,)
    if arg & 0x80:
        rm = UNSM.rm_table[arg & 0x0F]
        ultra.tag = "gfx"
        gfx = ultra.aw(extern=True)
        return (c, rm, gfx) + a
    return (None,) + a

# 13
def sg_gfx_pos(argv):
    rm = UNSM.rm_table[ultra.ub()]
    x = "%d" % ultra.sh()
    y = "%d" % ultra.sh()
    z = "%d" % ultra.sh()
    ultra.tag = "gfx"
    gfx = ultra.aw(extern=True)
    return (None, rm, gfx, x, y, z)

# 15
def sg_gfx(argv):
    rm = UNSM.rm_table[ultra.ub()]
    ultra.script.c_addr += 2
    ultra.tag = "gfx"
    gfx = ultra.aw(extern=True)
    return (None, rm, gfx)

# 16
def sg_shadow(argv):
    ultra.script.c_addr += 1
    t     = "%d" % ultra.uh()
    alpha = "0x%02X" % ultra.uh()
    scale = "%d" % ultra.uh()
    return (None, scale, alpha, t)

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
    "start", # 0x04
    "end", # 0x05
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
    (sg_callback,), # 0x19
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
        sym = table.sym_addr(self, self.c_dst, self.c_dst, True)
        if sym != None:
            tab = 0
            line.append((
                self.c_dst, sym,
                set() if len(line) > 0 else ultra.c.extern, []
            ))
        c = ultra.ub()
        f = sg_fnc[c]
        argv = f[0](f[1:])
        s = argv[0] if argv[0] != None else sg_str[c]
        if c in {0x05} and tab > 0:
            tab -= 1
        if c in {0x01}:
            tab = 0
        ln = "%sg_%s(%s)," % ("\t"*tab, s, ", ".join(argv[1:]))
        if c in {0x04}:
            tab += 1
        line[-1][-1].append(ln)
    ultra.c.fmt(self, line)
