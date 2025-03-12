import main
import ultra

import UNSM.c

def f_code(seg, start, end, fn, s=""):
	return [main.s_file, fn, [
		[main.f_str, s],
		[main.f_str, ".set noreorder\n.set noat\n\n.align 4\n\n"],
		[ultra.asm.f_code, seg, start, end, 0],
	]]

def f_data(seg, ds, de, rs, re, bs, be, fn, s, dl, rl):
	return [main.s_file, fn, [
		[main.f_str, s],
		[main.f_str, "\n"], [ultra.c.f_data, seg, rs, re, rl],
		[main.f_str, "\n"], [ultra.c.f_bss,  seg, bs, be],
		[main.f_str, "\n"], [ultra.c.f_data, seg, ds, de, dl],
	]]

def d_texture_n(t, w, h, end, fmt="%d", start=0, step=1):
	return [0, 1, [
		[0, 1, 1, UNSM.c.d_texture, t, w, h, fmt % i]
		for i in range(start, end, step)
	]]

# DEBUG
def d_gwords_prc(self, line, tab, argv):
	end, = argv
	while self.addr < end:
		self.save = self.addr
		w0 = self.u32()
		w1 = self.u32()
		line[-1][-1].append(tab + "/*0x%08X*/\t{{0x%08X, 0x%08X}}," % (
			self.save, w0, w1
		))
d_gwords = [True, d_gwords_prc]
