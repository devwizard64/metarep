import struct

import table

import ultra.asm
import ultra.c

script = None

tag = ""

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
    x, = struct.unpack(">f", script.c_next(4))
    return x

def d():
    x, = struct.unpack(">d", script.c_next(8))
    return x

def sym_addr(addr, src=None):
    if src == None:
        src = script.c_dst
    # print("addr=%08X  src=%08X" % (addr, src))
    return table.sym_addr(script, src, addr)

def addr_chk(seg, addr):
    return False
    # if seg in {0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08}:
    #     return False
    # if ultra.script.addr in {
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
    seg = addr >> 24
    if seg == 4:
        print("    0x%08X: table.sym(\"_%08X\")," % (addr, addr))
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
            "o": None,
            "map": ("const s16", "[]"),
            "area": ("const u8", "[]"),
            "obj": ("const s16", "[]"),
            "motion": ("const struct motion_t *const", "[]"),
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

def fmt_float(x, end="", strip=True):
    x = str(x)
    return x[:-2] if strip and x.endswith(".0") else x+end

def init(self, start, data):
    global script
    script = self
    script.c_init(start, data)
