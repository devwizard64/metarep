import sys
import os
import struct
import shutil
import importlib

def chk(self, s, x, t):
	if type(x) is not t: raise TypeError("%s(): %s: %s must be %s (is %s)" % (
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

# debug print
def arg_repr(x):
	if x is None: return "None"
	if callable(x): return x.__name__
	if type(x) == int:
		return "-0x%X(%d)" % (-x, x) if x < 0 else "0x%X(%d)" % (x, x)
	if type(x) in {bool, str, list, dict, tuple, set}:
		s = repr(x)
		return s[:20]+"..."+s[-20+3:] if len(s) > 40 else s
	print("WARNING: type '%s' has no repr !" % type(x))
	return repr(x)

# call list
def s_call(self, argv):
	lst, = argv
	for argv in lst:
		# debug print
		# if argv[0] != s_call:
		# 	print("[%s]" % ", ".join([arg_repr(x) for x in argv]))
		argv[0](self, argv[1:])

class segment:
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

# load segment table from donor file
# path - path list to donor file
# lst - [start, end, addr, name[, callback]]
#     start, end - physical or logical address of segment (ROM offset)
#     addr - virtual address of segment
#     name - name of segment
#     callback (optional) - function to parse segment (unscramble, decompress)
# callback (optional) - function to parse image (unscramble, extract VROM)
def s_segment(self, argv):
	path, lst = argv[:2]
	fn = os.path.join(*path)
	with open(fn, "rb") as f: data = f.read()
	if len(argv) > 2: data = argv[2](self, argv[3:], data)
	for arg in lst:
		start, end, addr, name = arg[:4]
		seg = data[start:end]
		if len(arg) > 4:
			fn = os.path.join(".cache", "%s.%s.bin" % (self.name, name))
			if os.path.isfile(fn):
				with open(fn, "rb") as f: seg = f.read()
			else:
				seg = arg[4](self, arg[5:], seg)
				mkdir(fn)
				with open(fn, "wb") as f: f.write(seg)
		self.segment[name] = segment(start, end, addr, seg)
		self.segtab[start] = name

# copy from module directory to output directory
# src - path list relative to module directory
# dst - path list relative to output directory
def s_copy(self, argv):
	src, dst = argv
	src = os.path.join(self.name, *src)
	dst = self.path_join(dst)
	mkdir(dst)
	if os.path.islink(src):
		os.symlink(os.readlink(src), dst)
	elif os.path.isdir(src):
		shutil.copytree(src, dst)
	else:
		shutil.copy2(src, dst)

# push directory to directory stack
def s_dir(self, argv):
	path, = argv
	self.path.append(path)

# pop directory
def s_pop(self, argv):
	self.path.pop()

# open file
def s_file(self, argv):
	fn, = argv
	self.file.append((self.path_join([fn]), []))
	if os.path.isfile(self.file[-1][0]):
		with open(self.file[-1][0], "r") as f: self.file[-1][1].append(f.read())

# join line and strip triple newline
def line_prc(line):
	data = "".join(line).strip("\n")
	while "\n\n\n" in data: data = data.replace("\n\n\n", "\n\n")
	if len(data) > 0: data += "\n"
	return data

# write last file
def s_write(self, argv):
	fn, line = self.file.pop()
	data = line_prc(line)
	mkdir(fn)
	with open(fn, "w") as f: f.write(data)

# write binary
# seg - name of segment
# start, end - virtual address range of binary
# path - path list of binary file
def s_bin(self, argv):
	seg, start, end, path = argv
	fn = self.path_join(path)
	mkdir(fn)
	with open(fn, "wb") as f: f.write(self.segment[seg][start:end])

# add string to file
def s_str(self, argv):
	self.file[argv[1] if len(argv) > 1 else -1][1].append(argv[0])

# 0.10000000149011612 -> 0.1F
def round_cvt(dec, enc, data):
	x = dec(data)
	for i in range(64):
		r = round(x, i)
		if enc(r) == data: return r
	return x

class script:
	def __init__(self, name, path):
		self.name = name
		self.meta = importlib.import_module(name)
		self.root = path # root directory of output
		self.path = [] # output directory stack (relative to root)
		self.file = [] # file stack
		self.segment = {} # segment table by segment name
		self.segtab = {} # segment name table by segment start
		self.seg = None # current segment name
		self.addr = None # current address
		self.save = None # save address

	def main(self):
		if os.path.isdir(self.root):
			if os.path.isfile(os.path.join(self.root, "__init__.py")):
				raise RuntimeError("'%s' is a module" % self.root)
			shutil.rmtree(self.root)
		try:
			s_call(self, [self.meta.lst])
		except:
			if len(self.file) > 0:
				fn, line = self.file[-1]
				data = line_prc(line)
				print("%s\n%s%s\nFILE:'%s'" % ("+"*40, data, "+"*40, fn))
			raise
	# join path with root and trim beginning
	def path_join(self, path, i=0):
		return os.path.join(*([self.root] + self.path + path)[i:])
	# with path, get relative path of current file
	def path_rel(self, path):
		start = os.path.dirname(self.file[-1][0])
		return os.path.relpath(self.path_join(path), start)

	# with address, get the intended segment name
	# table.seg - segment name override (for ambiguous case)
	def get_seg(self, addr):
		seg = self.seg
		if seg in self.meta.seg:
			if addr in self.meta.seg[seg]:
				seg = self.meta.seg[seg][addr]
		return seg
	# with address, get the symbol entry
	# src - standing address; if addr is Nth byte of command, src is 0th byte
	def get_sym(self, addr):
		seg = self.seg
		if seg in self.meta.sym:
			if addr in self.meta.sym[seg]:
				return self.meta.sym[seg][addr]
		return None
	# with address, find the symbol entry
	# prefer symbol within current or intended segment
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
	# get next N bytes of output
	def c_next(self, n):
		data = self.segment[self.seg][self.addr:self.addr+n]
		self.addr += n
		# is this necessary?
		# if len(data) < n: data += B"\0" * (n-len(data))
		return data

	# TODO: rename to numbers instead of bhiqfd
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
		if self.e == ">": b, h, l = struct.unpack("<BBB", x)
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
		if type(fmt) == str:
			if "%" in fmt: return fmt % x
			return fmt
		if callable(fmt): return fmt(self, x)
		if hasattr(fmt, "__getitem__"): return fmt[x]
		raise TypeError("bad fmt %s (%s)" % (fmt, type(fmt)))

	# format bit flag
	def fmt_flag(self, flag, x):
		lst = [s for m, i, s in flag if (x & m) == i]
		return "|".join(lst) if len(lst) > 0 else "0"
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
				if byte == None:
					argv.append(x)
				else:
					if byte != x: break
			else:
				x = callback(self, arg, argv)
				if x != None: return x
			self.addr = self.save
		return None

if __name__ == "__main__":
	if len(sys.argv) != 3:
		sys.stderr.write("usage: %s <meta> <output>\n" % argv[0])
		sys.exit(1)
	script(sys.argv[1], sys.argv[2]).main()
