import struct

import table

COMM_EXTERN = True
COMM_VAR    = True
COMM_LABEL  = True
COMM_LINE   = True

script = None

tag = ""

def round_cvt(dec, enc, data):
    x = dec(data)
    for i in range(0x100):
        r = round(x, i)
        if enc(r) == data:
            return r
    return x

def sb():
    x, = struct.unpack(">b", script.c_next(1))
    return x

def ub():
    x, = struct.unpack(">B", script.c_next(1))
    return x

def sh():
    x, = struct.unpack(">h", script.c_next(2))
    return x

def uh():
    x, = struct.unpack(">H", script.c_next(2))
    return x

def sw():
    x, = struct.unpack(">i", script.c_next(4))
    return x

def uw():
    x, = struct.unpack(">I", script.c_next(4))
    return x

def sd():
    x, = struct.unpack(">q", script.c_next(8))
    return x

def ud():
    x, = struct.unpack(">Q", script.c_next(8))
    return x

def f():
    return round_cvt(
        lambda x: struct.unpack(">f", x)[0],
        lambda x: struct.pack(">f", x),
        script.c_next(4)
    )

def d():
    return round_cvt(
        lambda x: struct.unpack(">d", x)[0],
        lambda x: struct.pack(">d", x),
        script.c_next(8)
    )

def sym_addr(addr, src=None):
    if src == None:
        src = script.c_dst
    # print("addr=%08X  src=%08X" % (addr, src))
    return table.sym_addr(script, src, addr)

def addr_chk(seg, addr):
    return False
    # if seg in {0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08}:
    #     return False
    # if script.addr in {
    #     0x80246000-0x00001000,
    #     0x80378800-0x000F5580,
    #     0x8016F000-0x0021F4C0,
    # }:
    #     return False
    if seg == 0 or seg >= 0x20:
        return False
    return True

def sym(addr, src=None, fmt="0x%08X", extern=False):
    sym = sym_addr(addr, src)
    if sym != None:
        if extern and hasattr(sym, "fmt"):
            c.extern.add((addr, sym))
        return sym.label
    if addr >= 0x80246000 and addr < 0x80367460:
        for start, end in (
            (0x8032D950, 0x8032DA9C), # player_touch    0x14C
            (0x8032DAA0, 0x8032DAE8), # player          0x48
            (0x8032DB30, 0x8032DC50), # player_demo     0x120
            (0x8032DC50, 0x8032DD28), # player_ground   0xD8
            (0x8032DF20, 0x8032FEB4), # camera          0x1F94
            (0x8032FEC0, 0x8032FFFC), # object          0x13C
            (0x80330020, 0x80330E1C), # object_a        0xDFC
            (0x80330E40, 0x80330EB2), # object_debug    0x72
            (0x80331750, 0x803317A0), # particle_snow   0x50
            (0x803317A0, 0x803317D8), # particle_lava   0x38
            (0x80332610, 0x8033283C), # object_b        0x22C
            (0x80332840, 0x80332E4C), # object_c        0x60C

            (0x80332E50, 0x80335010), # audio/data      0x21C0

            (0x8033C520, 0x8033CBE0), # camera          0x6C0
            (0x8033CBE0, 0x80361270), # object          0x24690
            (0x80361290, 0x803612B0), # object_debug    0x20
            (0x80361400, 0x80361420), # particle_snow   0x20
            (0x80361420, 0x80361440), # particle_lava   0x20

            (0x80361490, 0x80364BA0), # audio/g         0x3710
        ):
            end = (end+0x0F) & ~0x0F
            # if addr >= start and addr < end: break
        else:
            print("    0x%08X: table.sym(\"_%08X\")," % (addr, addr))
    seg = addr >> 24
    if addr_chk(seg, addr):
        global tag
        segtbl = {
            0x02: "main",
            0x03: "entity",
            0x04: "player",
            0x0A: "",
            0x0B: "particle_a",
            0x13: "",
        }
        if seg in segtbl:
            name = segtbl[seg]
        else:
            x = src-script.addr if src != None else {
                0x05: 0x0C000000,
                0x06: 0x0D000000,
                0x07: 0x0E000000,
                0x08: 0x0F000000,
            }[seg]-script.addr
            sym = sym_addr(x)
            if sym != None:
                _, _, name = sym.label.partition("_")
                _, _, name = name.partition("_")
                name, _, _ = name.rpartition("_")
            else:
                name = ""
        if name != "": name += "_"
        if seg == 0x13: tag = "o"
        va = {
            "": None,
            "gfx": ("const Gfx", "[]"),
            "g": ("const uintptr_t", "[]"),
            "o": ("const uintptr_t", "[]"),
            "map": ("const s16", "[]"),
            "area": ("const u8", "[]"),
            "obj": ("const s16", "[]"),
            "motion": ("const struct motion *const", "[]"),
            "objdata": None,
        }[tag]
        a, b = ("_var", ", \"%s\", \"%s\"" % va) if va != None else ("", "")
        print("    0x%08X: table.sym%s(\"%s_%s%08X\"%s)," % (
            addr, a, tag if tag != "" else "data", name, addr, b
        ))
        tag = ""
    return fmt % addr

def ah(src=None, extern=False):
    return sym(uh(), src, "0x%04X", extern)

def aw(src=None, extern=False):
    return sym(uw(), src, "0x%08X", extern)

def fmt_addr(x, addr=False, fmt=None):
    if x.startswith("0x"):
        x = "(void *)" + x
    elif x != "NULL":
        if addr:
            x = "&" + x
        if fmt != None:
            x = "(%s)%s" % (fmt, x)
    return x

def fmt_flag(flag, x):
    lst = []
    for m, i, s in flag:
        if (x & m) == i:
            lst.append(s)
    return " | ".join(lst) if len(lst) > 0 else "0"

def fmt_float(x, end="", strip=True):
    x = str(x)
    return x[:-2] if strip and x.endswith(".0") else x+end

def fmt_str(x):
    for old, new in (
        ("\\", "\\\\"),
        ("\"", "\\\""),
        ("\n", "\\n"),
        ("\t", "\\t"),
    ):
        x = x.replace(old, new)
    return "\"" + x + "\""

def init(self, start, data):
    global script
    script = self
    script.c_init(start, data)

import ultra.asm
import ultra.c
