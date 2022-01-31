import struct

import main
import table
import ultra
import UNSM

def d_prg_prc(argv):
    ultra.script.c_addr += 6
    dst = ultra.ah()
    return "0, 0, 0, %s" % dst
d_prg = [".half", d_prg_prc]

segment_table = {
    0x02: "MAIN",
    0x03: "GLOBAL",
    0x04: "PLAYER",
    0x05: "SHAPE1",
    0x06: "SHAPE2",
    0x07: "STAGE",
    0x08: "SHAPE3",
    0x09: "TEXTURE",
    0x0A: "BACKGROUND",
    0x0B: "WEATHER",
    0x0C: "SHAPE1",
    0x0D: "SHAPE2",
    0x0E: "STAGE",
    0x0F: "SHAPE3",
    0x13: "OBJECT",
    0x14: "MENU",
    0x15: "GAME",
    0x16: "GLOBAL",
    0x17: "PLAYER",
}

def segment(x, start, end):
    if x.startswith(start) and x.endswith(end): return x[len(start):-len(end)]
    return None

# 00 01
def p_push_jump(argv):
    seg    = segment_table[ultra.uh()]
    start  = ultra.uw()
    end    = ultra.uw()
    script = ultra.uw()
    dev = ultra.script.addr + start
    start  = ultra.sym(start,  dev)
    script = ultra.sym(script, dev)
    name = segment(start, "_", "_dataSegmentRomStart")
    if name == None: raise RuntimeError("UNSM.asm.p_push_jump(): bad segment")
    return (None, seg, name, script)

# 02 07 0A 1B 1C 1D 1E 20
def p_null(argv):
    ultra.script.c_addr += 2
    return (None,)

# 03 04
def p_time(argv):
    time = UNSM.table.fmt_time(ultra.sh())
    return (None, time)

# 05 06 2E 2F 39
def p_script(argv):
    g, = argv
    ultra.script.c_addr += 2
    script = ultra.aw() if g else ultra.asm.aw()
    return (None, script)

# (08) (09)

# 0B 0C
def p_if_jump(argv):
    s, = argv
    cmp_ = (
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
        return (None, cmp_, val, script)
    return (None, cmp_, val)

# (0D) (0E) (0F) (10)

# 11 12
def p_callback(argv):
    arg = "%d" % ultra.uh()
    callback = ultra.aw()
    return (None, callback, arg)

# 13 19
def p_arg(argv):
    x = "%d" % ultra.sh()
    return (None, x)

# (14) (15)

# 16 17 18 1A
def p_load(argv):
    a, b, = argv
    seg = ultra.uh()
    if b != None:
        dst = ultra.aw()
        name = segment(dst, "_", b)
        if name == None: raise RuntimeError("UNSM.asm.p_load(): bad dst")
    start = ultra.uw()
    end   = ultra.uw()
    dev   = ultra.script.addr + start
    start = ultra.sym(start, dev)
    name = segment(start, "_", a)
    if name == None: raise RuntimeError("UNSM.asm.p_load(): bad segment")
    if b != None:
        return (None, name)
    seg = "MENU" if "menu" in start else segment_table[seg]
    return (None, seg, name)

# 1F
def p_scene_start(argv):
    scene = "%d" % ultra.ub()
    ultra.script.c_addr += 1
    script = ultra.aw()
    return (None, scene, script)

# 21
def p_shape_gfx(argv):
    x = ultra.uh()
    layer = UNSM.table.fmt_s_layer_x[x >> 12]
    shape = UNSM.table.fmt_shape(x & 0x0FFF)
    ultra.tag = "gfx"
    gfx = ultra.aw()
    return (None, shape, gfx, layer)

# 22
def p_shape_script(argv):
    shape = UNSM.table.fmt_shape(ultra.uh())
    script = ultra.aw()
    return (None, shape, script)

# (23)

# 24
def p_object(argv):
    mask = ultra.ub()
    shape = UNSM.table.fmt_shape(ultra.ub())
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
        return ("object_globl",
            shape, px, py, pz, rx, ry, rz, arg0, arg1, flag, script
        )
    mask = "0x%02X" % mask
    return (None, mask, shape, px, py, pz, rx, ry, rz, arg0, arg1, flag, script)

# 25
def p_player(argv):
    shape = UNSM.table.fmt_shape(ultra.uh())
    arg0 = ultra.ub()
    arg1 = ultra.ub()
    flag = ultra.uh()
    script = ultra.aw()
    if (shape, arg0, arg1, flag, script) == ("S_MARIO", 0, 0, 1, "o_mario"):
        return ("mario",)
    arg0 = "%d" % arg0
    arg1 = "%d" % arg1
    flag = "%d" % flag # T:flag
    return (None, shape, arg0, arg1, flag, script)

# 26 27
def p_link(argv):
    m, = argv
    index = "%d" % ultra.ub()
    stage = "%d" % ultra.ub() # T:enum(stage)
    scene = "%d" % ultra.ub()
    link  = "%d" % ultra.ub()
    flag  = ultra.ub()
    ultra.script.c_addr += 1
    return (m if flag == 0x80 else None, index, stage, scene, link)

# 28
def p_connect(argv):
    index = "%d" % ultra.ub()
    scene = "%d" % ultra.ub()
    px = "%d" % ultra.sh()
    py = "%d" % ultra.sh()
    pz = "%d" % ultra.sh()
    ultra.script.c_addr += 2
    return (None, index, scene, px, py, pz)

# 29 2A
def p_scene(argv):
    scene = "%d" % ultra.ub()
    ultra.script.c_addr += 1
    return (None, scene)

# 2B
def p_player_open(argv):
    scene = "%d" % ultra.ub()
    ultra.script.c_addr += 1
    ry = "%d" % ultra.sh()
    px = "%d" % ultra.sh()
    py = "%d" % ultra.sh()
    pz = "%d" % ultra.sh()
    return (None, scene, ry, px, py, pz)

# (2C) (2D)

# 30
def p_msg(argv):
    type_ = "%d" % ultra.ub() # T:enum(msgtype)
    msg   = "0x%02X" % ultra.ub() # T:enum(msg)
    return (None, type_, msg)

# 31
def p_env(argv):
    env = (
        "GRASS",
        "ROCK",
        "SNOW",
        "SAND",
        "GHOST",
        "WATER",
        "SLIDER",
    )[ultra.sh()]
    return (None, env)

# 33
def p_wipe(argv):
    type_ = "0x%02X" % ultra.ub() # T:enum(wipe)
    time  = UNSM.table.fmt_time(ultra.ub())
    r     = "0x%02X" % ultra.ub()
    g     = "0x%02X" % ultra.ub()
    b     = "0x%02X" % ultra.ub()
    ultra.script.c_addr += 1
    return (None, type_, time, r, g, b)

# 34
def p_bool(argv):
    x = UNSM.table.fmt_bool[ultra.ub()]
    ultra.script.c_addr += 1
    return (None, x)

# (35)

# 36
def p_bgm(argv):
    type_= "%d" % ultra.uh() # T:enum(bgmtype)
    bgm  = "0x%02X" % ultra.uh() # T:enum(seq)
    ultra.script.c_addr += 2
    return (None, type_, bgm)

# 37
def p_bgm_play(argv):
    bgm = "0x%02X" % ultra.uh() # T:enum(seq)
    return (None, bgm)

# 38
def p_bgm_stop(argv):
    time = "%d" % (ultra.sh()+2) # T:audtime
    return (None, time)

# (3A)

# 3B
def p_jet(argv):
    index = "%d" % ultra.ub()
    mode  = "%d" % ultra.ub()
    px    = "%d" % ultra.sh()
    py    = "%d" % ultra.sh()
    pz    = "%d" % ultra.sh()
    arg   = "%d" % ultra.sh()
    return (None, index, mode, px, py, pz, arg)

# 3C
def p_var(argv):
    cmd = (
        "store",
        "load",
    )[ultra.ub()]
    var = (
        "SAVE",
        "COURSE",
        "LEVEL",
        "STAGE",
        "SCENE",
    )[ultra.ub()]
    return (cmd, var)

p_str = [
    "push_call",    # 0x00 jsl
    "push_jump",    # 0x01 jml
    "pull_return",  # 0x02 rtl
    "sleep",        # 0x03
    "freeze",       # 0x04
    "jump",         # 0x05 jmp
    "call",         # 0x06 jsr
    "return",       # 0x07 rts
    "for",          # 0x08
    "done",         # 0x09
    "do",           # 0x0A
    "while",        # 0x0B
    "if_jump",      # 0x0C b*
    "if_call",      # 0x0D c*
    "if",           # 0x0E
    "else",         # 0x0F
    "endif",        # 0x10
    "callback",     # 0x11
    "process",      # 0x12
    "set",          # 0x13
    "push",         # 0x14
    "pull",         # 0x15
    "load_code",    # 0x16
    "load_data",    # 0x17
    "load_szp",     # 0x18
    "load_face",    # 0x19
    "load_txt",     # 0x1A
    "stage_init",   # 0x1B
    "stage_exit",   # 0x1C
    "stage_start",  # 0x1D
    "stage_end",    # 0x1E
    "scene_start",  # 0x1F
    "scene_end",    # 0x20
    "shape_gfx",    # 0x21
    "shape_script", # 0x22
    "shape_scale",  # 0x23
    "object",       # 0x24
    "player",       # 0x25
    "link",         # 0x26
    "linkbg",       # 0x27
    "connect",      # 0x28
    "scene_open",   # 0x29
    "scene_close",  # 0x2A
    "player_open",  # 0x2B
    "player_close", # 0x2C
    "scene_update", # 0x2D
    "map",          # 0x2E
    "area",         # 0x2F
    "msg",          # 0x30
    "env",          # 0x31
    None,           # 0x32
    "wipe",         # 0x33
    "vi_black",     # 0x34
    "vi_gamma",     # 0x35
    "bgm",          # 0x36
    "bgm_play",     # 0x37
    "bgm_stop",     # 0x38
    "obj",          # 0x39
    "wind",         # 0x3A
    "jet",          # 0x3B
    None,           # 0x3C
]

p_fnc = [
    (p_push_jump,), # 0x00
    (p_push_jump,), # 0x01
    (p_null,), # 0x02
    (p_time,), # 0x03
    (p_time,), # 0x04
    (p_script, False), # 0x05
    (p_script, True), # 0x06
    (p_null,), # 0x07
    None, # 0x08
    None, # 0x09
    (p_null,), # 0x0A
    (p_if_jump, False), # 0x0B
    (p_if_jump, True), # 0x0C
    None, # 0x0D
    None, # 0x0E
    None, # 0x0F
    None, # 0x10
    (p_callback,), # 0x11
    (p_callback,), # 0x12
    (p_arg,), # 0x13
    None, # 0x14
    None, # 0x15
    (p_load, "SegmentRomStart", "SegmentStart"), # 0x16
    (p_load, "_dataSegmentRomStart", None), # 0x17
    (p_load, "_szpSegmentRomStart", None), # 0x18
    (p_arg,), # 0x19 T:enum(face)
    (p_load, "_szpSegmentRomStart", None), # 0x1A
    (p_null,), # 0x1B
    (p_null,), # 0x1C
    (p_null,), # 0x1D
    (p_null,), # 0x1E
    (p_scene_start,), # 0x1F
    (p_null,), # 0x20
    (p_shape_gfx,), # 0x21
    (p_shape_script,), # 0x22
    None, # 0x23
    (p_object,), # 0x24
    (p_player,), # 0x25
    (p_link, "link_mid"), # 0x26
    (p_link, "linkbg_mid"), # 0x27
    (p_connect,), # 0x28
    (p_scene,), # 0x29
    (p_scene,), # 0x2A
    (p_player_open,), # 0x2B
    None, # 0x2C
    None, # 0x2D
    (p_script, True), # 0x2E
    (p_script, True), # 0x2F
    (p_msg,), # 0x30
    (p_env,), # 0x31
    None, # 0x32
    (p_wipe,), # 0x33
    (p_bool,), # 0x34
    None, # 0x35
    (p_bgm,), # 0x36
    (p_bgm_play,), # 0x37
    (p_bgm_stop,), # 0x38
    (p_script, True), # 0x39
    None, # 0x3A
    (p_jet,), # 0x3B
    (p_var,), # 0x3C
]

p_inc = {0x08, 0x0A, 0x0E, 0x0F, 0x1D, 0x1F}
p_dec = {0x09, 0x0B, 0x0F, 0x10, 0x1E, 0x20}

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
    "ANIME", # 0x26
    "0x27", # 0x27
    "0x28", # 0x28
    "0x29", # 0x29
    "COLTYPE", # 0x2A
    "COLFLAG", # 0x2B
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
    "COLARG", # 0x42
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

def mb():
    return mem_table[ultra.ub()]

# 00
def o_init(argv):
    type_ = UNSM.table.fmt_o_type_x[ultra.ub()]
    ultra.script.c_addr += 2
    return (None, type_)

# 01
def o_time(argv):
    ultra.script.c_addr += 1
    time = UNSM.table.fmt_time(ultra.sh())
    return (None, time)

# 02 04 0C 2A 37
def o_script(argv):
    g, = argv
    ultra.script.c_addr += 3
    script = ultra.aw() if g else ultra.asm.aw()
    return (None, script)

# 03 06 07 08 09 0A (0B) 1D 1E 21 22 2D 35
def o_null(argv):
    ultra.script.c_addr += 3
    return (None,)

# 05 32
def o_arg(argv):
    ultra.script.c_addr += 1
    x = "%d" % ultra.sh()
    return (None, x)

# 0D 0E 0F 10
def o_md(argv):
    mem = mb()
    val = "%d" % ultra.sh()
    return (None, mem, val)

# 11 (12)
def o_mh(argv):
    mem = mb()
    val = "0x%04X" % ultra.uh()
    return (None, mem, val)

# 13 14 15 16 (17)
def o_mdd(argv):
    mem = mb()
    val = "%d" % ultra.sh()
    mul = "%d" % ultra.sh()
    ultra.script.c_addr += 2
    return (None, mem, val, mul)

# 1B
def o_shape(argv):
    ultra.script.c_addr += 1
    shape = UNSM.table.fmt_shape(ultra.uh())
    return (None, shape)

# 1C 29 2C
def o_object(argv):
    m, = argv
    ultra.script.c_addr += 1
    arg = "%d" % ultra.sh()
    shape = UNSM.table.fmt_shape(ultra.uw())
    script = ultra.aw()
    if m:
        return (None, shape, script, arg)
    return (None, shape, script)

# 1F (20)
def o_mmm(argv):
    mem = mb()
    a   = mb()
    b   = mb()
    return (None, mem, a, b)

# 23 2B 2E
def o_collision(argv):
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
def o_m(argv):
    mem = mb()
    ultra.script.c_addr += 2
    return (None, mem)

# 27
def o_mp(argv):
    mem = mb()
    ultra.script.c_addr += 2
    script = ultra.aw()
    return (None, mem, script)

# 28
def o_anime(argv):
    anime = "0x%02X" % ultra.ub() # T:enum(anime)
    ultra.script.c_addr += 2
    return (None, anime)

# 2F (31) (36)
def o_w(argv):
    ultra.script.c_addr += 3
    x = "0x%08X" % ultra.uw()
    return (None, x)

# 30
def o_physics(argv):
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
def o_memclrflag(argv):
    mem = mb()
    ultra.script.c_addr += 2
    flag = "0x%08X" % ultra.uw() # T:flag
    return (None, mem, flag)

# 34
def o_mt(argv):
    mem = mb()
    time = UNSM.table.fmt_time(ultra.sh())
    return (None, mem, time)

o_str = [
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
    "shape",    # 0x1B
    "object",   # 0x1C
    "destroy",  # 0x1D
    "ground",   # 0x1E
    "memaddf",  # 0x1F
    "memaddi",  # 0x20
    "billboard",    # 0x21
    "shapehide",    # 0x22
    "colhit",   # 0x23
    None,       # 0x24
    "memsleep", # 0x25
    "for2",     # 0x26
    "ptr",      # 0x27
    "anime",    # 0x28
    "objectarg",    # 0x29
    "map",      # 0x2A
    "coloff",   # 0x2B
    "child",    # 0x2C
    "origin",   # 0x2D
    "coldmg",   # 0x2E
    "coltype",  # 0x2F
    "physics",  # 0x30
    "colarg",   # 0x31
    "scale",    # 0x32
    "memclrflag",   # 0x33
    "inc",      # 0x34
    "shapedisable", # 0x35
    "sets",     # 0x36
    "splash",   # 0x37
]

o_fnc = [
    (o_init,), # 0x00
    (o_time,), # 0x01
    (o_script, True), # 0x02
    (o_null,), # 0x03
    (o_script, False), # 0x04
    (o_arg,), # 0x05
    (o_null,), # 0x06
    (o_null,), # 0x07
    (o_null,), # 0x08
    (o_null,), # 0x09
    (o_null,), # 0x0A
    None, # 0x0B
    (o_script, True), # 0x0C
    (o_md,), # 0x0D
    (o_md,), # 0x0E
    (o_md,), # 0x0F
    (o_md,), # 0x10
    (o_mh,), # 0x11 T:flag
    None, # 0x12
    (o_mdd,), # 0x13
    (o_mdd,), # 0x14
    (o_mdd,), # 0x15
    (o_mdd,), # 0x16
    None, # 0x17
    None, # 0x18
    None, # 0x19
    None, # 0x1A
    (o_shape,), # 0x1B
    (o_object, False), # 0x1C
    (o_null,), # 0x1D
    (o_null,), # 0x1E
    (o_mmm,), # 0x1F
    None, # 0x20
    (o_null,), # 0x21
    (o_null,), # 0x22
    (o_collision, False), # 0x23
    None, # 0x24
    (o_m,), # 0x25
    None, # 0x26
    (o_mp,), # 0x27
    (o_anime,), # 0x28
    (o_object, True), # 0x29
    (o_script, True), # 0x2A
    (o_collision, True), # 0x2B
    (o_object, False), # 0x2C
    (o_null,), # 0x2D
    (o_collision, False), # 0x2E
    (o_w,), # 0x2F T:flag
    (o_physics,), # 0x30
    None, # 0x31
    (o_arg,), # 0x32
    (o_memclrflag,), # 0x33
    (o_mt,), # 0x34
    (o_null,), # 0x35
    None, # 0x36
    (o_script, True), # 0x37
]

o_inc = {0x05, 0x08, 0x26}
o_dec = {0x06, 0x07, 0x09}

s_table = [
    (p_str, p_fnc, p_inc, p_dec, "p"),
    (o_str, o_fnc, o_inc, o_dec, "o"),
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
        if i == 0: self.c_addr += 1
        f = s_fnc[c]
        scrtbl = {
            0x22: "s_script",
            0x2E: "map",
            0x2F: "area",
            0x39: "obj",
        }
        objtbl = {
            0x27: "anime",
            0x2A: "map",
            0x37: "splash",
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
    line.append("TABLE()\ntable_start:\n")
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

def s_anime(self, argv):
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
        # anime
        if t == 0:
            a_flag  = ultra.sh()
            a_waist = ultra.sh()
            a_start = ultra.sh()
            a_end   = ultra.sh()
            a_frame = ultra.sh()
            a_joint = ultra.sh()
            a_val   = self.c_dst + ultra.uw()
            a_tbl   = self.c_dst + ultra.uw()
            a_siz   = self.c_dst + ultra.uw()
            stbl_add(stbl, a_val, 1, s + "_val")
            stbl_add(stbl, a_tbl, 2, s + "_tbl")
            c.append((
                "\tANIME(%s, 0x%04X, %d, %d, %d, %d, %d)\n"
            ) % (s, a_flag, a_waist, a_start, a_end, a_frame, a_joint))
            i += 1
        # val
        elif t == 1:
            c.append("\t.short %s\n" % ", ".join([
                "0x%04X" % ultra.uh()
                for _ in range(min(8, (a_siz-self.c_dst)//2))
            ]))
            if self.c_addr == a_siz:
                c.append("\n")
        # tbl
        elif t == 2:
            c.append("\t.short %s\n" % ", ".join([
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

def s_audio_ctltbl(self, argv):
    return

def s_audio_seqbnk(self, argv):
    seq, bnk, data, tbl = argv
    self.addr = 0-seq
    ultra.asm.init(self, 0, data)
    self.c_addr += 2
    cnt = ultra.uh()
    for i in range(cnt):
        start   = ultra.uw()
        size    = ultra.uw()
        fn = self.path_join(["seq", "%s.seq" % tbl[i]])
        main.mkdir(fn)
        with open(fn, "wb") as f:
            f.write(self.data[self.c_data][seq+start:seq+start+size])
    self.addr = 0-bnk
    ultra.asm.init(self, 0, data)
    line = []
    for i in range(cnt):
        start   = ultra.uh()
        self.c_push()
        self.c_addr = start
        n = ultra.ub()
        line.append("SEQ(%s, %s)\n" % (tbl[i], ", ".join([
            "%d" % ultra.ub() for _ in range(n)
        ])))
        self.c_pull()
    data = "".join(line)
    fn = main.path_join([self.root, "meta", "seq.h"])
    main.mkdir(fn)
    with open(fn, "w") as f:
        f.write(data)
