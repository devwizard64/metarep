import struct

import table

DALIGN      = 1 << 16
BALIGN      = 1 << 17

A_EXTERN    = 1 << 0
A_ADDR      = 1 << 1
A_CAST      = 1 << 2
A_ARRAY     = 1 << 3

COMM_EXTERN = True
COMM_VAR    = True
COMM_LABEL  = True
COMM_LINE   = True

script = None

tag = ""

fmt_os_readwrite = [
    "OS_READ",
    "OS_WRITE",
]

fmt_os_mesg_pri = [
    "OS_MESG_PRI_NORMAL",
    "OS_MESG_PRI_HIGH",
]

fmt_os_mesg_flag = [
    "OS_MESG_NOBLOCK",
    "OS_MESG_BLOCK",
]

fmt_struct_OSTask = {
    0x04: "OSTask__flags",
    0x10: "OSTask__ucode",
    0x18: "OSTask__ucode_data",
    0x1C: "OSTask__ucode_data_size",
}

flag_button = [
    (0x8000, 0x8000, "A_BUTTON"),
    (0x4000, 0x4000, "B_BUTTON"),
    (0x2000, 0x2000, "Z_TRIG"),
    (0x1000, 0x1000, "START_BUTTON"),
    (0x0800, 0x0800, "U_JPAD"),
    (0x0400, 0x0400, "D_JPAD"),
    (0x0200, 0x0200, "L_JPAD"),
    (0x0100, 0x0100, "R_JPAD"),
    (0x0080, 0x0080, "0x0080"),
    (0x0040, 0x0040, "0x0040"),
    (0x0020, 0x0020, "L_TRIG"),
    (0x0010, 0x0010, "R_TRIG"),
    (0x0008, 0x0008, "U_CBUTTONS"),
    (0x0004, 0x0004, "D_CBUTTONS"),
    (0x0002, 0x0002, "L_CBUTTONS"),
    (0x0001, 0x0001, "R_CBUTTONS"),
]

flag_sp_sw = [
    (0x00000001, 0x00000001, "SP_CLR_HALT"),
    (0x00000002, 0x00000002, "SP_SET_HALT"),
    (0x00000004, 0x00000004, "SP_CLR_BROKE"),
    (0x00000008, 0x00000008, "SP_CLR_INTR"),
    (0x00000010, 0x00000010, "SP_SET_INTR"),
    (0x00000020, 0x00000020, "SP_CLR_SSTEP"),
    (0x00000040, 0x00000040, "SP_SET_SSTEP"),
    (0x00000080, 0x00000080, "SP_CLR_INTR_BREAK"),
    (0x00000100, 0x00000100, "SP_SET_INTR_BREAK"),
    (0x00000200, 0x00000200, "SP_CLR_YIELD"),
    (0x00000400, 0x00000400, "SP_SET_YIELD"),
    (0x00000800, 0x00000800, "SP_CLR_YIELDED"),
    (0x00001000, 0x00001000, "SP_SET_YIELDED"),
    (0x00002000, 0x00002000, "SP_CLR_TASKDONE"),
    (0x00004000, 0x00004000, "SP_SET_TASKDONE"),
    (0x00008000, 0x00008000, "SP_CLR_RSPSIGNAL"),
    (0x00010000, 0x00010000, "SP_SET_RSPSIGNAL"),
    (0x00020000, 0x00020000, "SP_CLR_CPUSIGNAL"),
    (0x00040000, 0x00040000, "SP_SET_CPUSIGNAL"),
]

flag_sp_sr = [
    (0x0001, 0x0001, "SP_STATUS_HALT"),
    (0x0002, 0x0002, "SP_STATUS_BROKE"),
    (0x0004, 0x0004, "SP_STATUS_DMA_BUSY"),
    (0x0008, 0x0008, "SP_STATUS_DMA_FULL"),
    (0x0010, 0x0010, "SP_STATUS_IO_FULL"),
    (0x0020, 0x0020, "SP_STATUS_SSTEP"),
    (0x0040, 0x0040, "SP_STATUS_INTR_BREAK"),
    (0x0080, 0x0080, "SP_STATUS_YIELD"),
    (0x0100, 0x0100, "SP_STATUS_YIELDED"),
    (0x0200, 0x0200, "SP_STATUS_TASKDONE"),
    (0x0400, 0x0400, "SP_STATUS_RSPSIGNAL"),
    (0x0800, 0x0800, "SP_STATUS_CPUSIGNAL"),
]

flag_dpc_sw = [
    (0x0001, 0x0001, "DPC_CLR_XBUS_DMEM_DMA"),
    (0x0002, 0x0002, "DPC_SET_XBUS_DMEM_DMA"),
    (0x0004, 0x0004, "DPC_CLR_FREEZE"),
    (0x0008, 0x0008, "DPC_SET_FREEZE"),
    (0x0010, 0x0010, "DPC_CLR_FLUSH"),
    (0x0020, 0x0020, "DPC_SET_FLUSH"),
    (0x0040, 0x0040, "DPC_CLR_TMEM_CTR"),
    (0x0080, 0x0080, "DPC_CLR_PIPE_CTR"),
    (0x0100, 0x0100, "DPC_CLR_CMD_CTR"),
    (0x0200, 0x0200, "DPC_CLR_CLOCK_CTR"),
]

flag_dpc_sr = [
    (0x0001, 0x0001, "DPC_STATUS_XBUS_DMEM_DMA"),
    (0x0002, 0x0002, "DPC_STATUS_FREEZE"),
    (0x0004, 0x0004, "DPC_STATUS_FLUSH"),
    (0x0008, 0x0008, "DPC_STATUS_START_GCLK"),
    (0x0010, 0x0010, "DPC_STATUS_TMEM_BUSY"),
    (0x0020, 0x0020, "DPC_STATUS_PIPE_BUSY"),
    (0x0040, 0x0040, "DPC_STATUS_CMD_BUSY"),
    (0x0080, 0x0080, "DPC_STATUS_CBUF_READY"),
    (0x0100, 0x0100, "DPC_STATUS_DMA_BUSY"),
    (0x0200, 0x0200, "DPC_STATUS_END_VALID"),
    (0x0400, 0x0400, "DPC_STATUS_START_VALID"),
]

flag_OSTask_flags = [
    (0x0001, 0x0001, "OS_TASK_YIELDED"),
    (0x0002, 0x0002, "OS_TASK_DP_WAIT"),
    (0x0004, 0x0004, "OS_TASK_LOADABLE"),
    (0x0008, 0x0008, "OS_TASK_SP_ONLY"),
    (0x0010, 0x0010, "OS_TASK_USR0"),
    (0x0020, 0x0020, "OS_TASK_USR1"),
    (0x0040, 0x0040, "OS_TASK_USR2"),
    (0x0080, 0x0080, "OS_TASK_USR3"),
]

fmt_OSTask_flags    = lambda x: fmt_flag(flag_OSTask_flags, x)
fmt_sp_sr           = lambda x: fmt_flag(flag_sp_sr, x)
fmt_sp_sw           = lambda x: fmt_flag(flag_sp_sw, x)
fmt_dpc_sr          = lambda x: fmt_flag(flag_dpc_sr, x)

def fmt_flag(flag, x):
    lst = []
    for m, i, s in flag:
        if (x & m) == i:
            lst.append(s)
    return " | ".join(lst) if len(lst) > 0 else "0"

def fmt_s16(x):
    return "-0x%04X" % -x if x < 0 else "0x%04X" % x

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

def fmt_addr(x, extern=False, addr=False, cast=None, array=None):
    s = sym(array[0] if array != None else x, None, "(void *)0x%08X", extern)
    if not s.startswith("(void *)0x") and s != "NULL":
        if addr:            s = "&" + s
        if cast != None:    s = "(%s)%s" % (cast, s)
        if array != None:   s = "%s[%d]" % (s, (x-array[0]) // array[1])
    return s

def fmt_sizefmt(size):
    return "0x%%0%dX" % max(2, (size.bit_length()+3)//4)

def round_cvt(dec, enc, data):
    x = dec(data)
    for i in range(0x100):
        r = round(x, i)
        if enc(r) == data:
            return r
    return x

def addr_chk(seg, dev, addr):
    return False
    if dev < 0x1000: return False
    if seg in {0x02, 0x03, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A}: return False
    if seg == 0x00: return False
    if seg >= 0x20: return False
    return True

def sym(addr, src=None, fmt="0x%08X", extern=False):
    sym = table.sym_addr(script, addr, src)
    if sym != None:
        if extern and hasattr(sym, "fmt"):
            c.extern.add((addr, sym))
        return sym.label
    if addr >= 0x80000010 and addr < 0x80400000:
        print("    0x%08X: table.sym(\"_%08X\")," % (addr, addr))
    dev = script.c_dev(src)
    seg = addr >> 24
    if addr_chk(seg, dev, addr):
        global tag
        sym = table.sym_addr(script, dev)
        if sym != None:
            _, _, name = sym.label.partition("_")
            _, _, name = name.partition("_")
            name, _, _ = name.rpartition("_")
            name += "_"
        else:
            name = ""
        va = {
            "": None,
            "gfx": ("Gfx", "[]"),
            "s_script": ("S_SCRIPT", "[]"),
            "o_script": ("O_SCRIPT", "[]"),
            "map": ("MAP_DATA", "[]"),
            "area": ("AREA_DATA", "[]"),
            "obj": ("OBJ_DATA", "[]"),
            "anime": ("struct anime *", "[]"),
            "splash": ("struct splash"),
        }[tag]
        a, b = ("_var", ", \"%s\", \"%s\"" % va) if va != None else ("", "")
        print("    0x%08X: table.sym%s(\"%s_%s%08X\"%s)," % (
            addr, a, tag if tag != "" else "data", name, addr, b
        ))
        tag = ""
    return fmt % addr

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

def ah(src=None, extern=False):
    return sym(0x04000000 | uh(), src, extern=extern)

def aw(src=None, extern=False):
    return sym(             uw(), src, extern=extern)

def init(self, start, data):
    global script
    script = self
    script.c_init(start, data)

import ultra.asm
import ultra.c
