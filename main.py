#!/usr/bin/env python3

import sys
import os
import struct
import shutil
import importlib

import time

def chk(self, s, x, t):
	if not isinstance(x, t):
		raise TypeError("%s(): %s: %s must be %s (is %s)" % (
			type(self).__name__, self.label, s, t.__name__, repr(x)
		))

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

# symbol
class sym:
	def __init__(self, label, flag=set()):
		self.label = label
		self.flag  = flag
		chk(self, "flag", self.flag, set)

# symbol of C variable
class sym_var:
	def __init__(self, label, var, lst="", flag=set()):
		self.label = label
		self.flag  = flag
		self.var   = var
		self.lst   = lst
		chk(self, "flag", self.flag, set)
		chk(self, "var",  self.var,  str)
		chk(self, "lst",  self.lst,  str)
	def fmt(self, start="", end="", j=0):
		return start + fmt_pre(self.var, j) + self.label + self.lst + end

# symbol of C function
class sym_fnc:
	def __init__(self, label, val="void", arg=("void",), flag=set()):
		self.label = label
		self.flag  = flag
		self.val   = val
		self.arg   = arg
		chk(self, "flag", self.flag, set)
		chk(self, "val",  self.val,  str)
		chk(self, "arg",  self.arg,  tuple)
	def fmt(self, start="", end="", j=0):
		return fmt_arg(
			start + fmt_pre(self.val, j) + self.label, end, self.arg
		)

# symbol of C function variable
class sym_var_fnc:
	def __init__(
		self, label, var="", lst="", val="void", arg=("void",), flag=set()
	):
		self.label = label
		self.flag  = flag
		self.var   = var
		self.lst   = lst
		self.val   = val
		self.arg   = arg
		chk(self, "flag", self.flag, set)
		chk(self, "var",  self.var,  str)
		chk(self, "lst",  self.lst,  str)
		chk(self, "val",  self.val,  str)
		chk(self, "arg",  self.arg,  tuple)
	def fmt(self, start="", end="", j=0):
		return fmt_arg(
			start + fmt_pre(self.val, j, "(*") + sym_var.fmt(self) + ")",
			end, self.arg
		)

# equivalent to mkdir -p
def mkdir(fn):
	os.makedirs(os.path.dirname(fn), exist_ok=True)

# 0.10000000149011612 -> 0.1F
def round_cvt(decode, encode, data):
	x = decode(data)
	for i in range(64):
		r = round(x, i)
		if encode(r) == data: return r
	return x

# debug print
def arg_repr(x):
	if x is None: return "None"
	if callable(x): return x.__name__
	if isinstance(x, int):
		s = "-0x%X" % -x if x < 0 else "0x%X" % x
		return "%s(%d)" % (s, x)
	if type(x) in {bool, str, list, dict, tuple, set}:
		s = repr(x)
		return s[:20]+"..."+s[-20+3:] if len(s) > 40 else s
	print("WARNING: type '%s' has no repr !" % type(x))
	return repr(x)

# donor format: name:[donor, start, end, addr, name[, callback]]
# name - name of segment
# donor: [path[, callback]]
#     path - name of donor file
#     callback (optional) - function to parse image (unscramble/extract ROM)
# start, end - physical or logical address of segment (ROM offset)
# addr - virtual address of segment
# callback (optional) - function to parse segment (unscramble/decompress)
class SEGMENT:
	def __init__(self, start, end, addr, data):
		self.start = start
		self.end   = end
		self.addr  = addr
		self.data  = data
	# index or slice in virtual address space
	def __getitem__(self, key):
		if type(key) is slice:
			start = key.start
			stop  = key.stop
			step  = key.step
			if start is not None: start -= self.addr
			if stop  is not None: stop  -= self.addr
			return self.data[start:stop:step]
		raise TypeError("bad key %s (%s)" % (key, type(key)))

class FILE:
	def __init__(self, work, path):
		self.path = path
		self.fn = os.path.join(work.root, path)
		self.data = []
	def process(self):
		data = "".join(self.data).strip("\n")
		while "\n\n\n" in data: data = data.replace("\n\n\n", "\n\n")
		if data: data += "\n"
		return data
	def write(self):
		data = self.process()
		mkdir(self.fn)
		with open(self.fn, "w") as f: f.write(data)

class WORK:
	def __init__(self, name, root, meta):
		self.name = name
		self.root = root # root directory of output
		self.meta = meta
		self.segment = {} # segment table by segment name
		self.seg = None # current segment name
		self.addr = None # current address
		self.save = None # save address
		self.file = None
	def load(self, seg):
		for arg in self.meta.donor[seg]:
			donor, start, end, addr = arg[:4]
			fn = os.path.join("donor", donor[0])
			if not os.path.isfile(fn): continue
			size = end-start
			with open(fn, "rb") as f:
				if len(donor) > 1:
					data = donor[1](self, donor[2:], f, start, size)
				else:
					f.seek(start)
					data = f.read(size)
			if len(arg) > 4: data = arg[4](self, arg[5:], data)
			self.segment[seg] = SEGMENT(start, end, addr, data)
			break
	def exec(self, seq):
		for cmd in seq:
			try:
				# debug print
				# print("[%s]" % ", ".join([arg_repr(x) for x in cmd]))
				cmd[0](self, cmd[1:])
			except:
				if self.file: print("%s\n%s%s\nFILE:'%s'" % (
					"+"*40, self.file.process(), "+"*40, self.file.path
				))
				raise
	# with address, get the intended segment name
	# table.seg - segment name override (for ambiguous case)
	def get_seg(self, addr):
		seg = self.seg
		if seg in self.meta.seg:
			if addr in self.meta.seg[seg]:
				seg = self.meta.seg[seg][addr]
		return seg
	# with address, get the symbol entry
	def get_sym(self, addr):
		seg = self.seg
		if seg in self.meta.sym:
			if addr in self.meta.sym[seg]:
				return self.meta.sym[seg][addr]
		return None
	# with address, find the symbol entry
	# prefer symbol within current or intended segment
	# src - standing address; if addr is Nth byte of command, src is 0th byte
	def find_sym(self, addr, src=None):
		seg = self.seg
		if src is not None: seg = self.get_seg(src)
		if seg in self.meta.sym:
			if addr in self.meta.sym[seg]:
				return self.meta.sym[seg][addr]
		mask = tuple(self.seg.split("."))
		for i in range(len(mask), 0, -1):
			m = mask[:i]
			for seg in self.meta.sym:
				if m == tuple(seg.split(".")[:i]):
					if addr in self.meta.sym[seg]:
						return self.meta.sym[seg][addr]
		if "" in self.meta.sym:
			if addr in self.meta.sym[""]:
				return self.meta.sym[""][addr]
		return None
	# with address, get immediate (allpurpose parameter for processing)
	def get_imm(self, addr):
		seg = self.seg
		if seg in self.meta.imm:
			if addr in self.meta.imm[seg]:
				return self.meta.imm[seg][addr]
		return None

	def c_init(self, e, seg, addr):
		self.e = e # endianness ("<"=LE, ">"=BE)
		self.seg = seg # segment name
		self.addr = addr # address
	# get next N bytes of content
	def c_next(self, n):
		data = self.segment[self.seg][self.addr:self.addr+n]
		self.addr += n
		# is this necessary?
		# if len(data) < n: data += B"\0" * (n-len(data))
		return data

	def s8(self):
		x = self.c_next(1)
		if len(x) != 1: return None
		x, = struct.unpack(self.e+"b", x)
		return x
	def u8(self):
		x = self.c_next(1)
		if len(x) != 1: return None
		x, = struct.unpack(self.e+"B", x)
		return x
	def s16(self):
		x = self.c_next(2)
		if len(x) != 2: return None
		x, = struct.unpack(self.e+"h", x)
		return x
	def u16(self):
		x = self.c_next(2)
		if len(x) != 2: return None
		x, = struct.unpack(self.e+"H", x)
		return x
	def u24(self):
		x = self.c_next(3)
		if len(x) != 3: return None
		if self.e == "<": l, h, b = struct.unpack("<BBB", x)
		if self.e == ">": b, h, l = struct.unpack(">BBB", x)
		return l | h << 8 | b << 16
	def s32(self):
		x = self.c_next(4)
		if len(x) != 4: return None
		x, = struct.unpack(self.e+"i", x)
		return x
	def u32(self):
		x = self.c_next(4)
		if len(x) != 4: return None
		x, = struct.unpack(self.e+"I", x)
		return x
	def s64(self):
		x = self.c_next(8)
		if len(x) != 8: return None
		x, = struct.unpack(self.e+"q", x)
		return x
	def u64(self):
		x = self.c_next(8)
		if len(x) != 8: return None
		x, = struct.unpack(self.e+"Q", x)
		return x
	def f(self):
		x = self.c_next(4)
		if len(x) != 4: return None
		return round_cvt(
			lambda x: struct.unpack(self.e+"f", x)[0],
			lambda x: struct.pack(self.e+"f", x),
			x
		)
	def d(self):
		x = self.c_next(8)
		if len(x) != 8: return None
		return round_cvt(
			lambda x: struct.unpack(self.e+"d", x)[0],
			lambda x: struct.pack(self.e+"d", x),
			x
		)
	# generator for ASCII string
	def ascii(self, n):
		for i in range(n):
			c = self.u8()
			if c == 0: continue
			yield chr(c)
	# generator for ASCII string (NUL-terminated)
	def asciz(self, n):
		while True:
			c = self.u8()
			if c == 0: break
			yield chr(c)
		self.addr = (self.addr+n-1) & -n

	# allpurpose format
	def fmt(self, fmt, x):
		if isinstance(fmt, str):
			if "%" in fmt: return fmt % x
			return fmt
		if callable(fmt): return fmt(self, x)
		if hasattr(fmt, "__getitem__"): return fmt[x]
		raise TypeError("bad fmt %s (%s)" % (fmt, type(fmt)))

	# format bit flag
	def fmt_flag(self, flag, x):
		lst = [s for m, i, s in flag if (x & m) == i]
		return "|".join(lst) if lst else "0"
	# format s16 in hexadecimal
	def fmt_s16(self, x):
		return "-0x%04X" % -x if x < 0 else "0x%04X" % x
	# format float, optionally strip trailing .0
	def fmt_float(self, x, end="", strip=True):
		x = str(x)
		return x[:-2] if strip and x.endswith(".0") else x+end
	# format string literal
	def fmt_str(self, x):
		for old, new in (
			("\\", "\\\\"),
			("\"", "\\\""),
			("\n", "\\n"),
			("\t", "\\t"),
			("\0", "\\0"),
		): x = x.replace(old, new)
		return "\"" + x + "\""

	def macro(self):
		for callback, arg, mask in self.meta.macro:
			argv = []
			for byte in mask:
				x, = struct.unpack(">B", self.c_next(1))
				if byte is None:
					argv.append(x)
				else:
					if byte != x: break
			else:
				x = callback(self, arg, argv)
				if x is not None: return x
			self.addr = self.save
		return None

def s_if_cmp(self, cmp):
	if isinstance(cmp, str):
		return cmp in self.segment
	if isinstance(cmp, tuple): # and
		for seg in cmp:
			if seg not in self.segment: return False
		return True
	if isinstance(cmp, set): # or
		for seg in cmp:
			if seg in self.segment: return True
		return False
	raise TypeError("s_if(): invalid seg type")

def s_if(self, argv):
	for i in range(0, len(argv), 2):
		cmp = argv[i+0]
		seq = argv[i+1]
		if s_if_cmp(self, cmp):
			self.exec(seq)
			break

# write binary
# path - path of binary file
# seg - name of segment
# start, end - virtual address range of binary
def s_bin(self, argv):
	path, seg, start, end = argv
	fn = os.path.join(self.root, path)
	mkdir(fn)
	with open(fn, "wb") as f: f.write(self.segment[seg][start:end])

# open text file
# path - path of text file
# seq - sequence to execute
def s_file(self, argv):
	path, seq = argv
	self.file = FILE(self, path)
	self.exec(seq)
	self.file.write()
	self.file = None

# add string to file
def f_str(self, argv):
	s, = argv
	self.file.data.append(s)

def f_load(self, argv):
	path, = argv
	fn = os.path.join(self.root, path)
	with open(fn, "r") as f: self.file.data.append(f.read())

class SEQUENCE:
	def __init__(self, name, root, work=None):
		self.name = name
		self.root = root
		self.work = work
		self.meta = importlib.import_module(name)
	def exec(self):
		if os.path.isdir(self.root):
			if os.path.isfile(os.path.join(self.root, "__init__.py")):
				raise RuntimeError("'%s' is a module" % self.root)
			shutil.rmtree(self.root)
		copy, work = self.meta.work[self.work]
		for arg in copy:
			if isinstance(arg, str): src = dst = arg
			else: src, dst = arg
			src = os.path.join(self.name, src)
			dst = os.path.join(self.root, dst)
			mkdir(dst)
			if os.path.islink(src): os.symlink(os.readlink(src), dst)
			elif os.path.isdir(src): shutil.copytree(src, dst)
			else: shutil.copy2(src, dst)
		if 0:
			for seg, seq in work:
				w = WORK(self.name, self.root, self.meta)
				for seg in seg: w.load(seg)
				w.exec(seq)
		else:
			pidtab = []
			for seg, seq in work:
				pid = os.fork()
				if pid == 0:
					w = WORK(self.name, self.root, self.meta)
					for seg in seg: w.load(seg)
					w.exec(seq)
					return
				pidtab.append(pid)
			for pid in pidtab: os.waitpid(pid, 0)
	def check(self):
		segtab = {}
		for seg in self.meta.donor:
			for arg in self.meta.donor[seg]:
				donor, start, end, addr = arg[:4]
				fn = os.path.join("donor", donor[0])
				size = end-start
				with open(fn, "rb") as f:
					if len(donor) > 1:
						data = donor[1](self, donor[2:], f, start, size)
					else:
						f.seek(start)
						data = f.read(size)
				if len(arg) > 4: data = arg[4](self, arg[5:], data)
				if data not in segtab: segtab[data] = []
				segtab[data].append(seg)
		for x in segtab.values():
			if len(x) > 1: print(" ".join(x))

if __name__ == "__main__":
	if len(sys.argv) < 3 or len(sys.argv) > 4:
		sys.stderr.write("usage: %s <meta> <output> [work]\n" % argv[0])
		sys.exit(1)
	work = sys.argv[3] if len(sys.argv) > 3 else None
	seq = SEQUENCE(sys.argv[1], sys.argv[2], work)
	# seq.check()
	seq.exec()
