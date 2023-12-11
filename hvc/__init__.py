COMM_LABEL = True
COMM_LINE = True

def sym(self, x, n, w=False):
	if n == 2:
		if self.save >> 16 >= 0x40 or x >= 0x8000:
			x |= self.save & ~0xFFFF
	sym = self.find_sym(x)
	if sym != None:
		sym = sym.label
	else:
		sym = ("$%%0%dX" % (2*n)) % ((x & 0xFFFF) if n == 2 else x)
		#if 0x008000 <= x < 0x00FFB0 or 0x018000 <= x < 0x020000:
		# debug
		t = self.seg.split(".")[0]
		t = "_"+t if t != "J0" else ""
		if True:
			if asm.op in {0x4C, 0x5C}:
				s = ""
			elif asm.op in {0x20, 0x22}:
				s = "code"
			elif asm.op in {None}:
				s = "addr"
			elif x >= 0x2000 and x < 0x8000:
				s = "bss"
			else:
				s = "data"
			# if s in {"code", ""}:
			# if s == "code":
			# 	print("\t0x%06X: main.sym(\"%s_%06X%s\")," % (x, s, x, t))
			if s == "bss":
				print("\t0x%04X: main.sym(\"%s_%04X%s\")," % (x, s, x, t))
		#
	if w:
		if n == 2 and (x & 0x00FF00) == 0:
			sym = "A:" + sym
		if n == 3 and (x & 0xFF0000) in {0, (self.save & 0xFF0000)}:
			sym = "F:" + sym
	return sym

def ab(self, w=False):
	return sym(self, self.u8(), 1, w)

def aw(self, w=False):
	return sym(self, self.u16(), 2, w)

def al(self, w=False):
	return sym(self, self.u24(), 3, w)

def sym_lh(self, lo, hi):
	return sym(self, lo | hi << 8, 2)

def sym_lhb(self, lo, hi, ba):
	return sym(self, lo | hi << 8 | ba << 16, 3)

def init(self, seg, addr):
	self.c_init("<", seg, addr)

import hvc.asm
