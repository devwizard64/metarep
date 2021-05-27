import struct

import table

script = None

def sb():
    x, = struct.unpack("<b", script.c_next(1))
    return x

def ub():
    x, = struct.unpack("<B", script.c_next(1))
    return x

def uw():
    x, = struct.unpack("<H", script.c_next(2))
    return x

def ul():
    x, y = struct.unpack("<HB", script.c_next(3))
    return x | y << 16

def sym_addr(x, n, w=False):
    if n == 2:
        if script.c_dst >> 16 >= 0x40 or x >= 0x8000:
            x |= script.c_dst & ~0xFFFF
    sym = table.sym_addr(script, script.c_dst, x)
    if sym != None:
        sym = sym.label
    else:
        sym = ("$%%0%dX" % (2*n)) % ((x & 0xFFFF) if n == 2 else x)
        #if 0x008000 <= x < 0x00FFB0 or 0x018000 <= x < 0x020000:
        if True:
            if asm.op in {0x4C, 0x5C}:
                s = ""
            elif asm.op in {0x20, 0x22}:
                s = "code"
            elif asm.op in {None}:
                s = "addr"
            else:
                s = "macr"
            if s=="code" or s=="": print("    0x%06X: table.sym(\"%s_%06X\")," % (x, s, x))
        if True and x >= 0x8000:
            if asm.op == 0x4C:
                s = ""
            elif asm.op == 0x20:
                s = "code"
            elif asm.op == None:
                s = "addr"
            else:
                s = "data"
            if s!="code" and s!="": print("    0x%04X: table.sym(\"%s_%04X\")," % (x, s, x))
    if w:
        if n == 2 and (x & 0x00FF00) == 0:
            sym = "A:" + sym
        if n == 3 and (x & 0xFF0000) in {0, (script.c_dst & 0xFF0000)}:
            sym = "F:" + sym
    return sym

def ab(w=False):
    return sym_addr(ub(), 1, w)

def aw(w=False):
    return sym_addr(uw(), 2, w)

def al(w=False):
    return sym_addr(ul(), 3, w)

def sym_lh(lo, hi):
    return sym_addr(lo | hi << 8, 2)

def sym_lhb(lo, hi, ba):
    return sym_addr(lo | hi << 8 | ba << 16, 3)

def init(self, start, data):
    global script
    script = self
    script.c_init(start, data)

import hvc.asm
