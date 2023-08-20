import struct

UNUSED  = 1 << 0
GLOBL   = 1 << 1
LOCAL   = 1 << 2

def fmt_pre(v, j, end=""):
	if v.endswith("*"):
		ts, _, te = v.rpartition(" ")
		te += end
	else:
		ts, te = v, end
	return (ts+" " if ts != "" else ts).ljust(j-len(te)) + te

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
	def fmt(self, start="", end="", j=0):
		return start + fmt_pre(self.var, j) + self.label + self.lst + end

class sym_fnc:
	def __init__(self, label, val="void", arg=("void",), flag=0):
		self.label = label
		self.flag  = flag
		self.val   = val
		self.arg   = arg
	def fmt(self, start="", end="", j=0):
		return fmt_arg(
			start + fmt_pre(self.val, j) + self.label, end, self.arg
		)

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
	def fmt(self, start="", end="", j=0):
		return fmt_arg(
			start + fmt_pre(self.val, j, "(*") + sym_var.fmt(self) + ")",
			end, self.arg
		)

def dev_addr(self, src=None, rej=False):
	addr = self.c_dev(src)
	if src == None: src = self.c_dst
	for start, end, data, sym, dev, imm in self.meta.table.tbl:
		if addr >= start and addr < end and self.c_data.startswith(data):
			if src in dev: return dev[src]
	return None if rej else addr

def sym_addr(self, dst, src=None, rej=False):
	addr = self.c_dev(src) if rej else dev_addr(self, src)
	res = None
	for start, end, data, sym, dev, imm in self.meta.table.tbl:
		if self.c_data.startswith(data) and dst in sym:
			res = sym[dst]
			if addr >= start and addr < end: return res
	return None if rej else res

def sym_range(self, dst_start, dst_end, src=None):
	addr = self.c_dev(src)
	for start, end, data, sym, dev, imm in self.meta.table.tbl:
		if addr >= start and addr < end and self.c_data.startswith(data):
			return [
				(x, sym[x]) for x in sorted(sym.keys())
				if x >= dst_start and x < dst_end
			]
	return []

def imm_addr(self, dst, src=None):
	addr = self.c_dev(src)
	for start, end, data, sym, dev, imm in self.meta.table.tbl:
		if addr >= start and addr < end and self.c_data.startswith(data):
			if dst in imm: return imm[dst]
	return None

def imm_prc(imm, arg):
	if type(imm) == str:
		if "%" in imm: return imm % arg
		return imm
	if type(imm) in {list, tuple, dict}:
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
				if byte != x: break
		else:
			x = callback(arg, argv)
			if x != None: return x
		self.c_pull()
	return None
