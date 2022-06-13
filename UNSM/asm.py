import struct
import math

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
    if b != None: return (None, name)
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
    if mask == 0x1F: return ("object_globl",
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
    stage = UNSM.table.fmt_stage(ultra.ub())
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
    msg   = UNSM.msg_table[ultra.ub()]
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
    x = ultra.fmt_bool[ultra.ub()]
    ultra.script.c_addr += 1
    return (None, x)

# (35)

# 36
def p_bgm(argv):
    mode = UNSM.table.fmt_na_mode(ultra.uh())
    bgm  = UNSM.table.fmt_na_bgm(ultra.uh())
    ultra.script.c_addr += 2
    return (None, mode, bgm)

# 37
def p_bgm_play(argv):
    bgm = UNSM.table.fmt_na_bgm(ultra.uh())
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
    "VAR", # 0
    "FLAG", # 1
    "MSG", # 2
    "3", # 3
    "4", # 4
    "COL_TIMER", # 5
    "POS_X", # 6
    "POS_Y", # 7
    "POS_Z", # 8
    "VEL_X", # 9
    "VEL_Y", # 10
    "VEL_Z", # 11
    "VEL_F", # 12
    "VEL_L", # 13
    "VEL_U", # 14
    "ROT_X", # 15
    "ROT_Y", # 16
    "ROT_Z", # 17
    "SHAPE_ROT_X", # 18
    "SHAPE_ROT_Y", # 19
    "SHAPE_ROT_Z", # 20
    "SHAPE_OFF_Y", # 21
    "PARTICLE", # 22
    "GRAVITY", # 23
    "GROUND_Y", # 24
    "MOVE_FLAG", # 25
    "ANIME_CODE", # 26
    "V0", # 27
    "V1", # 28
    "V2", # 29
    "V3", # 30
    "V4", # 31
    "V5", # 32
    "V6", # 33
    "V7", # 34
    "ROT_VEL_X", # 35
    "ROT_VEL_Y", # 36
    "ROT_VEL_Z", # 37
    "ANIME", # 38
    "HOLD", # 39
    "WALL_R", # 40
    "DRAG", # 41
    "COL_TYPE", # 42
    "COL_FLAG", # 43
    "OFF_X", # 44
    "OFF_Y", # 45
    "OFF_Z", # 46
    "CODE", # 47
    "48", # 48
    "STATE", # 49
    "MODE", # 50
    "TIMER", # 51
    "BOUNCE", # 52
    "PL_DIST", # 53
    "PL_ROT", # 54
    "ORG_X", # 55
    "ORG_Y", # 56
    "ORG_Z", # 57
    "FRICTION", # 58
    "DENSITY", # 59
    "ANIME_INDEX", # 60
    "ALPHA", # 61
    "AP", # 62
    "HP", # 63
    "ARG", # 64
    "STATE_PREV", # 65
    "COL_ARG", # 66
    "COL_DIST", # 67
    "COIN", # 68
    "SHAPE_DIST", # 69
    "AREA", # 70
    "71", # 71
    "PRG_ARG", # 72
    "V8", # 73
    "V9", # 74
    "WALL_RY", # 75
    "GROUND_ARG", # 76
    "ORG_RY", # 77
    "GROUND", # 78
    "SE_DIE", # 79
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
    if m: return (None, shape, script, arg)
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
    "col_hit",  # 0x23
    None,       # 0x24
    "memsleep", # 0x25
    "for2",     # 0x26
    "ptr",      # 0x27
    "anime",    # 0x28
    "objectarg",    # 0x29
    "map",      # 0x2A
    "col_off",  # 0x2B
    "child",    # 0x2C
    "origin",   # 0x2D
    "col_dmg",  # 0x2E
    "col_type", # 0x2F
    "physics",  # 0x30
    "col_arg",  # 0x31
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
        if c in s_dec: tab -= 1
        ln = "%s%s_%s(%s)" % ("\t"*tab, s_t, s, ", ".join(argv[1:]))
        if c in s_inc: tab += 1
        line.append((self.c_dst, ln))
    ultra.asm.fmt(self, line)

def stbl_add(stbl, i, t, s):
    if i not in stbl: stbl[i] = [t]
    stbl[i].append(s)

def etbl_add(etbl, i, s):
    if i not in etbl: etbl[i] = []
    etbl[i].append(s)

def file_init(self, argv):
    end, data, name, tbl = argv
    ultra.asm.init(self, 0, data)
    cnt = ultra.uw()
    self.c_addr += 4
    line = self.file[-1][1]
    stbl = {}
    etbl = {}
    line.append("TABLE()\ntable:\n")
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
        for s in label[1:]: line.append("%s:\n" % s)
        return label
    return None

def file_e(self, line, etbl):
    if self.c_addr in etbl:
        for s in etbl[self.c_addr]: line.append("%s_end:\n" % s)
        return True
    return False

def s_anime(self, argv):
    end, name, tbl, cnt, line, stbl, etbl = file_init(self, argv)
    init = True
    i = 0
    while self.c_addr < end:
        if init:
            fn = (tbl[1][i] if i in tbl[1] else tbl[0][i]) + ".sx"
            line.append("#include \"%s/%s\"\n" % (name, fn))
            c = [".balign 4\n"]
        label = file_s(self, c, stbl)
        if label != None:
            t = label[0]
            if t == 0: s = label[-1]
        init = False
        # anime
        if t == 0:
            a_flag  = UNSM.table.fmt_anime_flag(ultra.sh())
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
                "\tANIME(%s, %s, %d, %d, %d, %d, %d)\n"
            ) % (s, a_flag, a_waist, a_start, a_end, a_frame, a_joint))
            i += 1
        # val
        elif t == 1:
            c.append("\t.short %s\n" % ", ".join([
                "0x%04X" % ultra.uh()
                for _ in range(min(8, (a_siz-self.c_dst)//2))
            ]))
            if self.c_addr == a_siz: c.append("\n")
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
            with open(fn, "w") as f: f.write(data)
            self.c_addr = (self.c_addr+3) & ~3
            init = True

def s_demo(self, argv):
    end, name, tbl, cnt, line, stbl, etbl = file_init(self, argv)
    while self.c_addr < end:
        if file_s(self, line, stbl) != None:
            stage = UNSM.table.fmt_stage(ultra.ub())
            self.c_addr += 3
            line.append("\tDEMO(%s)\n" % stage)
        else:
            count   = ultra.ub()
            stick_x = ultra.sb()
            stick_y = ultra.sb()
            button  = ultra.ub()
            line.append("\t.byte %3d, %3d, %3d, 0x%02X\n" % (
                count, stick_x, stick_y, button
            ))
        file_e(self, line, etbl)

def pstr(s):
    return struct.pack(">B", len(s)) + s

def iff_chunk(code, data):
    return struct.pack(">4sI", code, len(data)) + data

def aifc_pack(rate, wave, book=None, loop=None):
    x, = struct.unpack(">Q", struct.pack(">d", rate))
    e = 0x3FFF + (x >> 52)-0x3FF
    f = 1 << 63 | (x & 0xFFFFFFFFFFFFF) << 11
    data = B"AIFC"
    data += iff_chunk(
        B"COMM", struct.pack(">HIHHQ", 1, 16*len(wave)//9, 16, e, f) +
        B"VAPC" + pstr(B"VADPCM ~4-1")
    )
    if book: data += iff_chunk(
        B"APPL", B"stoc" + pstr(B"VADPCMCODES") +
        struct.pack(">HHH", 1, book[0], book[1]) + book[2]
    )
    if loop: data += iff_chunk(
        B"APPL", B"stoc" + pstr(B"VADPCMLOOPS") +
        struct.pack(">HHIII", 1, 1, loop[0], loop[1], loop[2]) +
        (loop[3] if loop[2] > 0 else struct.pack(">32x"))
    )
    data += iff_chunk(B"SSND", struct.pack(">II", 0, 0) + wave)
    if len(data) & 1: data += B"\0"
    return iff_chunk(B"FORM", data)

def al_book(self, book):
    if book == 0: return None
    self.c_addr = book
    order       = ultra.uw()
    npredictors = ultra.uw()
    book = self.c_next(16 << npredictors)
    return (order, npredictors, book)

def al_loop(self, loop):
    if loop == 0: return None
    self.c_addr = loop
    start = ultra.uw()
    end   = ultra.uw()
    count = ultra.uw()
    if count > 0:
        self.c_addr += 4
        state = self.c_next(32)
        return (start, end, count, state)
    return (start, end, count)

def al_sound(self, bankdata, wavedata, tbl, snd, key):
    if snd == 0: return None
    self.c_addr = snd
    self.c_addr += 4
    wave = ultra.uw()
    loop = ultra.uw()
    book = ultra.uw()
    size = ultra.uw()
    x = key
    key *= 32000
    wave = tbl+wave
    imm = table.imm_addr(self, wave)
    rate = imm[0] if imm[0] != None else int(round(key))
    name = imm[1]
    if wave not in wavedata:
        path = imm[2]
        book = al_book(self, book)
        loop = al_loop(self, loop)
        wavedata[wave] = [size, book, loop, rate, path, name]
    return (name, int(round(12*math.log2(round(key/rate, 6)))))

def al_envelope(self, bankdata, env):
    self.c_addr = env
    if env not in bankdata[1]:
        envelope = []
        while True:
            envelope.append((ultra.sh(), ultra.sh()))
            if envelope[-1][0] in {-1, -2, -3}: break
        name = "env%d" % bankdata[0]
        bankdata[0] += 1
        bankdata[1][env] = (name, ", ".join("%d, %d" % x for x in envelope))

def al_note(x):
    return (
        "C", "Cs", "D", "Eb", "E",
        "F", "Fs", "G", "Ab", "A", "Bb", "B",
    )[(x+9) % 12] + "%d" % ((x+9) // 12)

def al_instrument(self, bankdata, wavedata, tbl, inst, i):
    if inst == 0: return
    self.c_push()
    self.c_addr = inst
    self.c_addr += 1
    min_ = ultra.ub()
    max_ = ultra.ub()
    rel = ultra.ub()
    env = ultra.uw()
    sound = [(ultra.uw(), ultra.f()) for i in range(3)]
    al_envelope(self, bankdata, env)
    if self.c_addr-self.addr in {0x57D350, 0x57D3C0}:
        al_envelope(self, bankdata, (self.c_addr+15) & ~15)
    sound = [
        al_sound(self, bankdata, wavedata, tbl, snd, key)
        for snd, key in sound
    ]
    bankdata[2].append((
        "    instrument[%d] =\n"
        "    {\n"
        "        release = %d;\n"
        "        envelope = %s;\n"
    ) % (i, rel, bankdata[1][env][0]))
    if sound[0] != None: bankdata[2].append((
        "        soundL = {%s, %s, %s};\n"
    ) % (al_note(min_), sound[0][0], al_note(39-sound[0][1])))
    bankdata[2].append((
        "        sound = {%s, %s};\n"
    ) % (               sound[1][0], al_note(39-sound[1][1])))
    if sound[2] != None: bankdata[2].append((
        "        soundH = {%s, %s, %s};\n"
    ) % (al_note(max_), sound[2][0], al_note(39-sound[2][1])))
    bankdata[2].append("    };\n")
    self.c_pull()

def al_percussion(self, bankdata, wavedata, tbl, perc, i):
    if perc == 0: return
    self.c_push()
    self.c_addr = perc
    rel = ultra.ub()
    pan = ultra.ub()
    self.c_addr += 2
    snd, key = ultra.uw(), ultra.f()
    env = ultra.uw()
    al_envelope(self, bankdata, env)
    snd, note = al_sound(self, bankdata, wavedata, tbl, snd, key)
    bankdata[2].append((
        "    percussion[%d] =\n"
        "    {\n"
        "        release = %d;\n"
        "        pan = %d;\n"
        "        envelope = %s;\n"
        "        sound = {%s, %s};\n"
        "    };\n"
    ) % (i, rel, pan, bankdata[1][env][0], snd, al_note(39+note)))
    self.c_pull()

def s_audio_ctltbl(self, argv):
    ctl, tbl, data, ctlname, tblname = argv
    line = self.file[-1][1]
    wavetbl = {i: {} for i in tblname}
    banktbl = {}
    self.addr = 0-tbl
    ultra.asm.init(self, 0, data)
    self.c_addr += 2
    cnt = ultra.uh()
    for i in range(cnt):
        start = ultra.uw()
        self.c_addr += 4
        if i not in ctlname: continue
        banktbl[i] = [[0, {}, []], wavetbl[tbl+start], ctl, tbl+start]
    self.addr = 0-ctl
    ultra.asm.init(self, 0, self.c_data)
    self.c_addr += 2
    cnt = ultra.uh()
    for i in range(cnt):
        start = ultra.uw()
        self.c_addr += 4
        if i not in ctlname: continue
        self.c_push()
        self.c_addr = start
        icnt = ultra.uw()
        pcnt = ultra.uw()
        flag = ultra.uw()
        date = ultra.uw()
        banktbl[i][2] += self.c_addr
        banktbl[i] += [icnt, pcnt, flag, date]
        self.c_pull()
    for i in banktbl:
        bankdata, wavedata, ctl, tbl, icnt, pcnt, flag, date = banktbl[i]
        self.addr = 0-ctl
        ultra.asm.init(self, 0, self.c_data)
        imm = table.imm_addr(self, ctl)
        perc = ultra.uw()
        itbl = [ultra.uw() for i in range(icnt)]
        self.c_addr = perc
        ptbl = [ultra.uw() for i in range(pcnt)]
        for inst in sorted(itbl):
            i = itbl.index(inst)
            if i == imm:
                for perc in sorted(ptbl):
                    p = ptbl.index(perc)
                    al_percussion(self, bankdata, wavedata, tbl, perc, p)
            al_instrument(self, bankdata, wavedata, tbl, inst, i)
    for tbl in sorted(wavetbl.keys()):
        wavedata = wavetbl[tbl]
        line.append("wave %s\n{\n" % tblname[tbl])
        for wave in sorted(wavedata.keys()):
            size, book, loop, rate, path, name = wavedata[wave]
            wave = self.data[self.c_data][wave:wave+size]
            data = aifc_pack(rate, wave, book, loop)
            fn = self.path_join(path)
            main.mkdir(fn)
            with open(fn, "wb") as f: f.write(data)
            line.append("    sound %s \"%s\";\n" % (name, "/".join(path)))
        line.append("};\n\n")
    for i in sorted(banktbl.keys()):
        bankdata, wavedata, ctl, tbl, icnt, pcnt, flag, date = banktbl[i]
        line.append("bank %s\n{\n" % ctlname[i])
        line.append("    date = {%X, %X, %X};\n" % (
            date >> 16, date >> 8 & 0xFF, date >> 0 & 0xFF
        ))
        line.append("    wave %s;\n" % tblname[tbl])
        for env in sorted(bankdata[1].keys()):
            line.append("    envelope %s {%s};\n" % bankdata[1][env])
        line += bankdata[2]
        line.append("};\n\n")

def s_audio_seqbnk(self, argv):
    seq, bnk, data, seqname, path = argv
    line = self.file[-1][1]
    self.addr = 0-seq
    ultra.asm.init(self, 0, data)
    self.c_addr += 2
    cnt = ultra.uh()
    for i in range(cnt):
        start = ultra.uw()
        size  = ultra.uw()
        if i not in seqname: continue
        start = seq+start
        imm = table.imm_addr(self, start)
        if imm != None: size = imm
        data = self.data[self.c_data][start:start+size]
        fn = self.path_join(path + ["%s.seq" % seqname[i]])
        main.mkdir(fn)
        with open(fn, "wb") as f: f.write(data)
    self.addr = 0-bnk
    ultra.asm.init(self, 0, self.c_data)
    for i in range(cnt):
        start = ultra.uh()
        if i not in seqname: continue
        self.c_push()
        self.c_addr = start
        line.append("\"%s\" %s\n" % (
            "/".join(path + ["%s.seq" % seqname[i]]),
            " ".join(["%d" % ultra.ub() for _ in range(ultra.ub())])
        ))
        self.c_pull()
