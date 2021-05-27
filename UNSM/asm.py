import struct

import main
import table
import ultra
import UNSM

def d_prg_prc():
    src = ultra.uw()
    siz = ultra.uh()+1
    dst = ultra.uh()
    return ".dw 0x%08X :: .dh 0x%04X-1, 0x%04X" % (src, siz, dst)
d_prg = ["", d_prg_prc]

segment_table = {
    0x02: "MAIN",
    0x03: "ENTITY",
    0x04: "PLAYER",
    0x05: "GFXA",
    0x06: "GFXB",
    0x07: "STAGE",
    0x08: "GFXC",
    0x09: "TEXTURE",
    0x0A: "BACKGROUND",
    0x0B: "PARTICLE",
    0x0C: "GFXA",
    0x0D: "GFXB",
    0x0E: "STAGE",
    0x0F: "GFXC",
    0x13: "OBJECT",
    0x14: "MENU",
    0x15: "GAME",
    0x16: "ENTITY",
    0x17: "PLAYER",
}

def chk_seg(sym, s):
    if s != None and not sym.startswith(s+"_"):
        return True
    return not sym.endswith("_start")

# 00 01
def ss_mjump(argv):
    seg    = segment_table[ultra.uh()]
    start  = ultra.uw()
    end    = ultra.uw()
    script = ultra.uw()
    dev = ultra.script.addr + start
    start  = ultra.sym(start,  dev)
    script = ultra.sym(script, dev)
    if chk_seg(start, "data"):
        raise RuntimeError("UNSM.asm.ss_mjump(): bad seg")
    name = start[5:-6]
    return (None, seg, name, script)

# 02 07 0A 1B 1C 1D 1E 20
def ss_null(argv):
    ultra.script.c_addr += 2
    return (None,)

# 03 04
def ss_time(argv):
    time = UNSM.fmt_time(ultra.sh())
    return (None, time)

# 05 06 2E 2F 39
def ss_script(argv):
    g, = argv
    ultra.script.c_addr += 2
    script = ultra.aw() if g else ultra.asm.aw()
    return (None, script)

# (08) (09)

# 0B 0C
def ss_cond(argv):
    s, = argv
    c = (
        "AND",
        "NAND",
        "EQ",
        "NE",
        "GT",
        "GE",
        "LT",
        "LE",
    )[ultra.ub()]
    ultra.script.c_addr += 1
    val = "%d" % ultra.sw()
    if s:
        script = ultra.asm.aw()
        return (None, c, val, script)
    return (None, c, val)

# (0D) (0E) (0F) (10)

# 11 12
def ss_callback(argv):
    arg = "%d" % ultra.uh()
    callback = ultra.aw()
    return (None, callback, arg)

# 13 19 31 38
def ss_arg(argv):
    x = "%d" % ultra.sh()
    return (None, x)

# (14) (15)

# 16 17 18 1A
def ss_mdata(argv):
    s, = argv
    seg = ultra.uh()
    if s == None:
        dst = ultra.aw()
        if chk_seg(dst, "code"):
            raise RuntimeError("UNSM.asm.ss_mdata(): bad dst")
    start = ultra.uw()
    end   = ultra.uw()
    dev   = ultra.script.addr + start
    start = ultra.sym(start, dev)
    if chk_seg(start, s):
        raise RuntimeError("UNSM.asm.ss_mdata(): bad seg")
    name = start[:-6]
    if s != None:
        seg  = "MENU" if "menu" in start else segment_table[seg]
        name = name[len(s)+1:]
        return (None, seg, name)
    return (None, name)

# 1F
def ss_wstart(argv):
    world = "%d" % ultra.ub()
    ultra.script.c_addr += 1
    script = ultra.aw()
    return (None, world, script)

# 21
def ss_ggfx(argv):
    x = ultra.uh()
    rm = UNSM.rm_table[x >> 12]
    g = UNSM.fmt_g(x & 0x0FFF)
    ultra.tag = "gfx"
    gfx = ultra.aw()
    return (None, g, gfx, rm)

# 22
def ss_gscript(argv):
    g = UNSM.fmt_g(ultra.uh())
    script = ultra.aw()
    return (None, g, script)

# (23)

# 24
def ss_object(argv):
    mask = ultra.ub()
    g = UNSM.fmt_g(ultra.ub())
    px = "%d" % ultra.sh()
    py = "%d" % ultra.sh()
    pz = "%d" % ultra.sh()
    rx = "%d" % ultra.sh()
    ry = "%d" % ultra.sh()
    rz = "%d" % ultra.sh()
    arg0 = "%d" % ultra.ub()
    arg1 = "%d" % ultra.ub()
    flag = "%d" % ultra.uh()
    script = ultra.aw()
    if mask == 0x1F:
        return (
            "object_all", g, px, py, pz, rx, ry, rz, arg0, arg1, flag, script
        )
    mask = "0x%02X" % mask
    return (None, mask, g, px, py, pz, rx, ry, rz, arg0, arg1, flag, script)

# 25
def ss_player(argv):
    g = ultra.uh()
    arg = ultra.uw()
    script = ultra.aw()
    if g == 0x01 and arg == 1 and script == "o_mario":
        return ("mario",)
    g = UNSM.fmt_g(g)
    arg = "%d" % arg
    return (None, g, arg, script)

# 26 27
def ss_link(argv):
    m, = argv
    index = "%d" % ultra.ub()
    stage = "%d" % ultra.ub()
    world = "%d" % ultra.ub()
    link  = "%d" % ultra.ub()
    flag  = ultra.ub()
    ultra.script.c_addr += 1
    return (m if flag == 0x80 else None, index, stage, world, link)

# 28
def ss_linkw(argv):
    index = "%d" % ultra.ub()
    world = "%d" % ultra.ub()
    px = "%d" % ultra.sh()
    py = "%d" % ultra.sh()
    pz = "%d" % ultra.sh()
    ultra.script.c_addr += 2
    return (None, index, world, px, py, pz)

# 29 2A
def ss_world(argv):
    world = "%d" % ultra.ub()
    ultra.script.c_addr += 1
    return (None, world)

# 2B
def ss_pinit(argv):
    world = "%d" % ultra.ub()
    ultra.script.c_addr += 1
    ry = "%d" % ultra.sh()
    px = "%d" % ultra.sh()
    py = "%d" % ultra.sh()
    pz = "%d" % ultra.sh()
    return (None, world, ry, px, py, pz)

# (2C) (2D)

# 30
def ss_msg(argv):
    t   = "%d" % ultra.ub() # T:enum ?
    msg = "0x%02X" % ultra.ub() # T:enum
    return (None, t, msg)

# 33
def ss_wipe(argv):
    t    = "0x%02X" % ultra.ub() # T:enum
    time = UNSM.fmt_time(ultra.ub())
    r    = "0x%02X" % ultra.ub()
    g    = "0x%02X" % ultra.ub()
    b    = "0x%02X" % ultra.ub()
    ultra.script.c_addr += 1
    return (None, t, time, r, g, b)

# 34
def ss_bool(argv):
    x = UNSM.fmt_bool[ultra.ub()]
    ultra.script.c_addr += 1
    return (None, x)

# (35)

# 36
def ss_bgm(argv):
    t   = "%d" % ultra.uh() # T:enum
    bgm = "0x%02X" % ultra.uh() # T:enum
    ultra.script.c_addr += 2
    return (None, t, bgm)

# 37
def ss_bgmplay(argv):
    bgm = "0x%02X" % ultra.uh() # T:enum
    return (None, bgm)

# (3A)

# 3B
def ss_jet(argv):
    index = "%d" % ultra.ub()
    mode  = "%d" % ultra.ub()
    px    = "%d" % ultra.sh()
    py    = "%d" % ultra.sh()
    pz    = "%d" % ultra.sh()
    arg   = "%d" % ultra.uh()
    return (None, index, mode, px, py, pz, arg)

# 3C
def ss_arw(argv):
    t = (
        "aw",
        "ar",
    )[ultra.ub()]
    v = (
        "SAVE",
        "COURSE",
        "LEVEL",
        "STAGE",
        "WORLD",
    )[ultra.ub()]
    return (t, v)

ss_str = [
    "mcall",    # 0x00 jsl
    "mjump",    # 0x01 jml
    "mreturn",  # 0x02 rtl
    "sleep",    # 0x03
    "freeze",   # 0x04
    "jump",     # 0x05 jmp
    "call",     # 0x06 jsr
    "return",   # 0x07 rts
    "for",      # 0x08
    "done",     # 0x09
    "do",       # 0x0A
    "while",    # 0x0B
    "cjump",    # 0x0C b*
    "ccall",    # 0x0D c*
    "if",       # 0x0E
    "else",     # 0x0F
    "endif",    # 0x10
    "acall",    # 0x11
    "aupdate",  # 0x12
    "aset",     # 0x13
    "mpush",    # 0x14
    "mpop",     # 0x15
    "mcode",    # 0x16
    "mdata",    # 0x17
    "mszp",     # 0x18
    "mface",    # 0x19
    "mtexture", # 0x1A
    "sinit",    # 0x1B
    "sdestroy", # 0x1C
    "sstart",   # 0x1D
    "send",     # 0x1E
    "wstart",   # 0x1F
    "wend",     # 0x20
    "ggfx",     # 0x21
    "gscript",  # 0x22
    "gscale",   # 0x23
    "object",   # 0x24
    "player",   # 0x25
    "link",     # 0x26
    "linkbg",   # 0x27
    "linkw",    # 0x28
    "winit",    # 0x29
    "wdestroy", # 0x2A
    "pinit",    # 0x2B
    "pdestroy", # 0x2C
    "wupdate",  # 0x2D
    "map",      # 0x2E
    "area",     # 0x2F
    "msg",      # 0x30
    "env",      # 0x31
    None,       # 0x32
    "wipe",     # 0x33
    "viblack",  # 0x34
    "vigamma",  # 0x35
    "bgm",      # 0x36
    "bgmplay",  # 0x37
    "bgmstop",  # 0x38
    "obj",      # 0x39
    "wind",     # 0x3A
    "jet",      # 0x3B
    None,       # 0x3C
]

ss_fnc = [
    (ss_mjump,), # 0x00
    (ss_mjump,), # 0x01
    (ss_null,), # 0x02
    (ss_time,), # 0x03
    (ss_time,), # 0x04
    (ss_script, False), # 0x05
    (ss_script, True), # 0x06
    (ss_null,), # 0x07
    None, # 0x08
    None, # 0x09
    (ss_null,), # 0x0A
    (ss_cond, False), # 0x0B
    (ss_cond, True), # 0x0C
    None, # 0x0D
    None, # 0x0E
    None, # 0x0F
    None, # 0x10
    (ss_callback,), # 0x11
    (ss_callback,), # 0x12
    (ss_arg,), # 0x13
    None, # 0x14
    None, # 0x15
    (ss_mdata, None), # 0x16
    (ss_mdata, "data"), # 0x17
    (ss_mdata, "szp"), # 0x18
    (ss_arg,), # 0x19 T:enum
    (ss_mdata, "szp"), # 0x1A
    (ss_null,), # 0x1B
    (ss_null,), # 0x1C
    (ss_null,), # 0x1D
    (ss_null,), # 0x1E
    (ss_wstart,), # 0x1F
    (ss_null,), # 0x20
    (ss_ggfx,), # 0x21
    (ss_gscript,), # 0x22
    None, # 0x23
    (ss_object,), # 0x24
    (ss_player,), # 0x25
    (ss_link, "linkm"), # 0x26
    (ss_link, "linkbgm"), # 0x27
    (ss_linkw,), # 0x28
    (ss_world,), # 0x29
    (ss_world,), # 0x2A
    (ss_pinit,), # 0x2B
    None, # 0x2C
    None, # 0x2D
    (ss_script, True), # 0x2E
    (ss_script, True), # 0x2F
    (ss_msg,), # 0x30
    (ss_arg,), # 0x31 T:enum
    None, # 0x32
    (ss_wipe,), # 0x33
    (ss_bool,), # 0x34
    None, # 0x35
    (ss_bgm,), # 0x36
    (ss_bgmplay,), # 0x37
    (ss_arg,), # 0x38 T:time2
    (ss_script, True), # 0x39
    None, # 0x3A
    (ss_jet,), # 0x3B
    (ss_arw,), # 0x3C
]

ss_inc = {0x08, 0x0A, 0x0E, 0x0F, 0x1D, 0x1F}
ss_dec = {0x09, 0x0B, 0x0F, 0x10, 0x1E, 0x20}

mem_table = (
    "0x00", # 0x00
    "FLAG", # 0x01
    "0x02", # 0x02
    "0x03", # 0x03
    "0x04", # 0x04
    "0x05", # 0x05
    "0x06", # 0x06
    "0x07", # 0x07
    "0x08", # 0x08
    "0x09", # 0x09
    "0x0A", # 0x0A
    "0x0B", # 0x0B
    "0x0C", # 0x0C
    "0x0D", # 0x0D
    "0x0E", # 0x0E
    "0x0F", # 0x0F
    "0x10", # 0x10
    "0x11", # 0x11
    "0x12", # 0x12
    "0x13", # 0x13
    "0x14", # 0x14
    "0x15", # 0x15
    "0x16", # 0x16
    "0x17", # 0x17
    "0x18", # 0x18
    "0x19", # 0x19
    "0x1A", # 0x1A
    "0x1B", # 0x1B
    "0x1C", # 0x1C
    "0x1D", # 0x1D
    "0x1E", # 0x1E
    "0x1F", # 0x1F
    "0x20", # 0x20
    "0x21", # 0x21
    "0x22", # 0x22
    "0x23", # 0x23
    "0x24", # 0x24
    "0x25", # 0x25
    "MOTION", # 0x26
    "0x27", # 0x27
    "0x28", # 0x28
    "0x29", # 0x29
    "TOUCHTYPE", # 0x2A
    "TOUCH", # 0x2B
    "0x2C", # 0x2C
    "0x2D", # 0x2D
    "0x2E", # 0x2E
    "0x2F", # 0x2F
    "0x30", # 0x30
    "0x31", # 0x31
    "0x32", # 0x32
    "0x33", # 0x33
    "0x34", # 0x34
    "0x35", # 0x35
    "0x36", # 0x36
    "0x37", # 0x37
    "0x38", # 0x38
    "0x39", # 0x39
    "0x3A", # 0x3A
    "0x3B", # 0x3B
    "0x3C", # 0x3C
    "0x3D", # 0x3D
    "0x3E", # 0x3E
    "0x3F", # 0x3F
    "0x40", # 0x40
    "0x41", # 0x41
    "TOUCHARG", # 0x42
    "0x43", # 0x43
    "0x44", # 0x44
    "0x45", # 0x45
    "0x46", # 0x46
    "0x47", # 0x47
    "0x48", # 0x48
    "0x49", # 0x49
    "0x4A", # 0x4A
    "0x4B", # 0x4B
    "0x4C", # 0x4C
    "0x4D", # 0x4D
    "0x4E", # 0x4E
    "0x4F", # 0x4F
)

def um():
    return mem_table[ultra.ub()]

# 00
def so_init(argv):
    t = (
        "PLAYER",
        "0x01",
        "PLAYERATTACK",
        "0x03",
        "OBJECTA",
        "OBJECTB",
        "ITEM",
        "0x07",
        "DEFAULT",
        "MOVEBG",
        "PLAYERUSE",
        "SYSTEM",
        "PARTICLE",
    )[ultra.ub()]
    ultra.script.c_addr += 2
    return (None, t)

# 01
def so_time(argv):
    ultra.script.c_addr += 1
    time = UNSM.fmt_time(ultra.sh())
    return (None, time)

# 02 04 0C 2A 37
def so_script(argv):
    g, = argv
    ultra.script.c_addr += 3
    script = ultra.aw() if g else ultra.asm.aw()
    return (None, script)

# 03 06 07 08 09 0A (0B) 1D 1E 21 22 2D 35
def so_null(argv):
    ultra.script.c_addr += 3
    return (None,)

# 05 32
def so_arg(argv):
    ultra.script.c_addr += 1
    x = "%d" % ultra.sh()
    return (None, x)

# 0D 0E 0F 10
def so_md(argv):
    mem = um()
    val = "%d" % ultra.sh()
    return (None, mem, val)

# 11 (12)
def so_mh(argv):
    mem = um()
    val = "0x%04X" % ultra.uh()
    return (None, mem, val)

# 13 14 15 16 (17)
def so_mdd(argv):
    mem = um()
    val = "%d" % ultra.sh()
    mul = "%d" % ultra.sh()
    ultra.script.c_addr += 2
    return (None, mem, val, mul)

# 1B
def so_gfx(argv):
    ultra.script.c_addr += 1
    g = UNSM.fmt_g(ultra.uh())
    return (None, g)

# 1C 29 2C
def so_object(argv):
    m, = argv
    ultra.script.c_addr += 1
    arg = "%d" % ultra.sh()
    gfx = "0x%02X" % ultra.uw()
    script = ultra.aw()
    if m:
        return (None, gfx, script, arg)
    return (None, gfx, script)

# 1F (20)
def so_mmm(argv):
    mem = um()
    a   = um()
    b   = um()
    return (None, mem, a, b)

# 23 2B 2E
def so_hitbox(argv):
    m, = argv
    ultra.script.c_addr += 3
    radius = "%d" % ultra.sh()
    height = "%d" % ultra.sh()
    if m:
        offset = "%d" % ultra.sh()
        ultra.script.c_addr += 2
        return (None, radius, height, offset)
    return (None, radius, height)

# 25 (26)
def so_m(argv):
    mem = um()
    ultra.script.c_addr += 2
    return (None, mem)

# 27
def so_mp(argv):
    mem = um()
    ultra.script.c_addr += 2
    script = ultra.aw()
    return (None, mem, script)

# 28
def so_motion(argv):
    motion = "0x%02X" % ultra.ub() # T:enum
    ultra.script.c_addr += 2
    return (None, motion)

# 2F (31) (36)
def so_w(argv):
    ultra.script.c_addr += 3
    x = "0x%08X" % ultra.uw()
    return (None, x)

# 30
def so_move(argv):
    ultra.script.c_addr += 3
    a = "%d" % ultra.sh()
    b = "%d" % ultra.sh()
    c = "%d" % ultra.sh()
    d = "%d" % ultra.sh()
    e = "%d" % ultra.sh()
    f = "%d" % ultra.sh()
    g = "%d" % ultra.sh()
    h = "%d" % ultra.sh()
    return (None, a, b, c, d, e, f, g, h)

# 33
def so_memclrflag(argv):
    mem = um()
    ultra.script.c_addr += 2
    flag = "0x%08X" % ultra.uw() # T:flag
    return (None, mem, flag)

# 34
def so_mt(argv):
    mem = um()
    time = UNSM.fmt_time(ultra.sh())
    return (None, mem, time)

so_str = [
    "init",     # 0x00
    "sleep",    # 0x01
    "call",     # 0x02
    "return",   # 0x03
    "jump",     # 0x04
    "for",      # 0x05
    "fend",     # 0x06
    "fcontinue",    # 0x07
    "while",    # 0x08
    "wend",     # 0x09
    "exit",     # 0x0A
    "exit2",    # 0x0B
    "callback", # 0x0C
    "addf",     # 0x0D
    "setf",     # 0x0E
    "addi",     # 0x0F
    "seti",     # 0x10
    "setflag",  # 0x11
    "clrflag",  # 0x12
    "setrandr", # 0x13
    "setrandf", # 0x14
    "setrandi", # 0x15
    "addrandf", # 0x16
    "addrandr", # 0x17
    None,       # 0x18
    None,       # 0x19
    None,       # 0x1A
    "gfx",      # 0x1B
    "object",   # 0x1C
    "destroy",  # 0x1D
    "ground",   # 0x1E
    "memaddf",  # 0x1F
    "memaddi",  # 0x20
    "billboard",    # 0x21
    "gfxhide",  # 0x22
    "hitbox",   # 0x23
    None,       # 0x24
    "memsleep", # 0x25
    "for2",     # 0x26
    "ptr",      # 0x27
    "motion",   # 0x28
    "objectarg",    # 0x29
    "map",      # 0x2A
    "hitboxoffset", # 0x2B
    "child",    # 0x2C
    "origin",   # 0x2D
    "hurtbox",  # 0x2E
    "touchtype",    # 0x2F
    "move",     # 0x30
    "toucharg", # 0x31
    "scale",    # 0x32
    "memclrflag",   # 0x33
    "inc",      # 0x34
    "gfxdisable",   # 0x35
    "sets",     # 0x36
    "objdata",  # 0x37
]

so_fnc = [
    (so_init,), # 0x00
    (so_time,), # 0x01
    (so_script, True), # 0x02
    (so_null,), # 0x03
    (so_script, False), # 0x04
    (so_arg,), # 0x05
    (so_null,), # 0x06
    (so_null,), # 0x07
    (so_null,), # 0x08
    (so_null,), # 0x09
    (so_null,), # 0x0A
    None, # 0x0B
    (so_script, True), # 0x0C
    (so_md,), # 0x0D
    (so_md,), # 0x0E
    (so_md,), # 0x0F
    (so_md,), # 0x10
    (so_mh,), # 0x11 T:flag
    None, # 0x12
    (so_mdd,), # 0x13
    (so_mdd,), # 0x14
    (so_mdd,), # 0x15
    (so_mdd,), # 0x16
    None, # 0x17
    None, # 0x18
    None, # 0x19
    None, # 0x1A
    (so_gfx,), # 0x1B
    (so_object, False), # 0x1C
    (so_null,), # 0x1D
    (so_null,), # 0x1E
    (so_mmm,), # 0x1F
    None, # 0x20
    (so_null,), # 0x21
    (so_null,), # 0x22
    (so_hitbox, False), # 0x23
    None, # 0x24
    (so_m,), # 0x25
    None, # 0x26
    (so_mp,), # 0x27
    (so_motion,), # 0x28
    (so_object, True), # 0x29
    (so_script, True), # 0x2A
    (so_hitbox, True), # 0x2B
    (so_object, False), # 0x2C
    (so_null,), # 0x2D
    (so_hitbox, False), # 0x2E
    (so_w,), # 0x2F T:flag
    (so_move,), # 0x30
    None, # 0x31
    (so_arg,), # 0x32
    (so_memclrflag,), # 0x33
    (so_mt,), # 0x34
    (so_null,), # 0x35
    None, # 0x36
    (so_script, True), # 0x37
]

so_inc = {0x05, 0x08, 0x26}
so_dec = {0x06, 0x07, 0x09}

s_table = [
    (ss_str, ss_fnc, ss_inc, ss_dec, "s"),
    (so_str, so_fnc, so_inc, so_dec, "o"),
]

def s_script(self, argv):
    start, end, data, i = argv
    ultra.asm.init(self, start, data)
    s_str, s_fnc, s_inc, s_dec, s_t = s_table[i]
    line = []
    tab = 0
    while self.c_addr < end:
        self.c_push()
        c = ultra.ub()
        if i == 0:
            self.c_addr += 1
        f = s_fnc[c]
        if i == 0:
            if c in {0x2E, 0x2F, 0x39}: ultra.tag = s_str[c]
            elif c == 0x22: ultra.tag = "g"
        scrtbl = {
            0x22: "g",
            0x2E: "map",
            0x2F: "area",
            0x39: "obj",
        }
        objtbl = {
            0x27: "motion",
            0x2A: "map",
            0x37: "objdata",
        }
        if i == 0 and c in scrtbl: ultra.tag = scrtbl[c]
        if i == 1 and c in objtbl: ultra.tag = objtbl[c]
        argv = f[0](f[1:])
        s = argv[0] if argv[0] != None else s_str[c]
        if c in s_dec:
            tab -= 1
        ln = "%s%s_%s(%s)" % ("\t"*tab, s_t, s, ", ".join(argv[1:]))
        if c in s_inc:
            tab += 1
        line.append((self.c_dst, ln))
    ultra.asm.fmt(self, line)

def stbl_add(stbl, i, t, s):
    if i not in stbl:
        stbl[i] = [t]
    stbl[i].append(s)

def etbl_add(etbl, i, s):
    if i not in etbl:
        etbl[i] = []
    etbl[i].append(s)

def file_init(self, argv):
    end, data, name, tbl = argv
    ultra.asm.init(self, 0, data)
    cnt = ultra.uw()
    self.c_addr += 4
    line = self.file[-1][1]
    stbl = {}
    etbl = {}
    line.append("TABLE(table)\n\ntable_start:\n")
    for i in range(cnt):
        s = "%s_%s" % (name, tbl[0][i])
        line.append("\tFILE(%s)\n" % s)
        start = ultra.uw()
        size  = ultra.uw()
        stbl_add(stbl, start, 0, s)
        etbl_add(etbl, start+size, s)
    line.append("table_end:\n\n")
    return end, name, tbl, cnt, line, stbl, etbl

def file_s(self, line, stbl):
    self.c_push()
    if self.c_addr in stbl:
        label = stbl[self.c_addr]
        line.append("\n")
        for s in label[1:]:
            line.append("%s:\n" % s)
        return label
    return None

def file_e(self, line, etbl):
    if self.c_addr in etbl:
        for s in etbl[self.c_addr]:
            line.append("%s_end:\n" % s)
        return True
    return False

def s_motion(self, argv):
    end, name, tbl, cnt, line, stbl, etbl = file_init(self, argv)
    init = True
    i = 0
    while self.c_addr < end:
        if init:
            fn = (tbl[1][i] if i in tbl[1] else tbl[0][i]) + ".S"
            line.append("#include \"%s/%s\"\n" % (name, fn))
            c = [".balign 4\n"]
        label = file_s(self, c, stbl)
        if label != None:
            t = label[0]
            if t == 0:
                s = label[-1]
        init = False
        # motion
        if t == 0:
            m_flag   = ultra.sh()
            m_height = ultra.sh()
            m_start  = ultra.sh()
            m_end    = ultra.sh()
            m_frame  = ultra.sh()
            m_joint  = ultra.sh()
            m_val    = self.c_dst + ultra.uw()
            m_tbl    = self.c_dst + ultra.uw()
            m_siz    = self.c_dst + ultra.uw()
            stbl_add(stbl, m_val, 1, s + "_val")
            stbl_add(stbl, m_tbl, 2, s + "_tbl")
            c.append((
                "\tMOTION(%s, 0x%04X, %d, %d, %d, %d, %d)\n"
            ) % (s, m_flag, m_height, m_start, m_end, m_frame, m_joint))
            i += 1
        # val
        elif t == 1:
            c.append("\t.half %s\n" % ", ".join([
                "0x%04X" % ultra.uh()
                for _ in range(min(8, (m_siz-self.c_dst)//2))
            ]))
            if self.c_addr == m_siz:
                c.append("\n")
        # tbl
        elif t == 2:
            c.append("\t.half %s\n" % ", ".join([
                "%5d" % ultra.uh()
                for _ in range(6)
            ]))
        else:
            raise RuntimeError("bad mode")
        if file_e(self, c, etbl):
            data = main.line_prc(c)
            fn = self.path_join([name, fn])
            main.mkdir(fn)
            with open(fn, "w") as fd:
                fd.write(data)
            self.c_addr = (self.c_addr+3) & ~3
            init = True

def s_demo(self, argv):
    end, name, tbl, cnt, line, stbl, etbl = file_init(self, argv)
    while self.c_addr < end:
        if file_s(self, line, stbl) != None:
            stage = ultra.ub()
            self.c_addr += 3
            line.append("\tDEMO(%d)\n" % stage)
        else:
            count   = ultra.ub()
            stick_x = ultra.sb()
            stick_y = ultra.sb()
            button  = ultra.ub()
            line.append("\t.byte %3d, %3d, %3d, 0x%02X\n" % (
                count, stick_x, stick_y, button
            ))
        file_e(self, line, etbl)
