import struct

UNUSED  = 1 << 0
GLOBL   = 1 << 1

def fmt_pre(v):
    return v if v == "" or v.endswith("*") else v+" "

def fmt_arg(v, e, arg):
    a = ", ".join(arg)
    if len(v) + len(a) + len(e) + 2 > 80:
        a = "\n\t" + ",\n\t".join(arg) + "\n"
    return "%s(%s)%s" % (v, a, e)

class sym:
    def __init__(self, label, flag=0):
        self.label = label
        self.flag  = flag

class sym_var:
    def __init__(self, label, var, lst="", flag=0):
        self.label = label
        self.flag  = flag
        self.var   = var
        self.lst   = lst
    def fmt(self, start="", end=""):
        return start + fmt_pre(self.var) + self.label + self.lst + end

class sym_fnc:
    def __init__(self, label, val="void", arg=("void",), flag=0):
        self.label = label
        self.flag  = flag
        self.val   = val
        self.arg   = arg
    def fmt(self, start="", end=""):
        return fmt_arg(start + fmt_pre(self.val) + self.label, end, self.arg)

class sym_var_fnc:
    def __init__(
        self, label, var="", lst="", val="void", arg=("void",), flag=0
    ):
        self.label = label
        self.flag  = flag
        self.var   = var
        self.lst   = lst
        self.val   = val
        self.arg   = arg
    def fmt(self, start="", end=""):
        return fmt_arg(
            start + fmt_pre(self.val) + "(*" + sym_var.fmt(self) + ")", end,
            self.arg
        )

def sym_addr(self, src, dst, rej=False):
    dev = self.dev if self.dev != None else src-self.addr
    if not rej:
        for start, end, data, sym, fnc, imm in self.meta.table:
            if self.c_data.startswith(data) and src in fnc:
                dev = fnc[src]
    res = None
    for start, end, data, sym, fnc, imm in self.meta.table:
        if self.c_data.startswith(data) and dst in sym:
            res = sym[dst]
            if dev >= start and dev < end:
                return res
    if not rej:
        if res != None:
            return res
    return None

def imm_addr(self, src, dst):
    dev = self.dev if self.dev != None else src-self.addr
    for start, end, data, sym, fnc, imm in self.meta.table:
        if self.c_data.startswith(data) and dev >= start and dev < end:
            if dst in imm:
                return imm[dst]
    return None

def imm_prc(imm, arg):
    if type(imm) == str:
        if "%" in imm:
            return imm % arg
        return imm
    if type(imm) in {list, tuple}:
        return imm[arg]
    return imm(arg)

def macro_prc(self):
    for callback, arg, mask in self.meta.macro:
        argv = []
        for byte in mask:
            x, = struct.unpack(">B", self.c_next(1))
            if byte == None:
                argv.append(x)
            else:
                if byte != x:
                    break
        else:
            return callback(arg, argv)
        self.c_pull()
    return None
