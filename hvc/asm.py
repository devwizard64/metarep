import main
import hvc

A_Y     = 0x00  # Y
A_A     = 0x01  # A
A_X     = 0x02  # X

A_IB    = 0x04  # imm byte
A_IW    = 0x05  # imm word
A_IA    = 0x06  # imm A
A_IX    = 0x07  # imm XY

A_AB    = 0x10  # addr byte
A_AW    = 0x11  # addr word
A_AL    = 0x12  # addr long
A_AA    = 0x13  # addr abs
A_AF    = 0x14  # addr far

A_RB    = 0x18  # rel byte

A_XB    = 0x20  # index byte
A_XW    = 0x21  # index word

A_NB    = 0x28  # indirect byte
A_NW    = 0x29  # indirect word
A_NWX   = 0x2A  # indirect word X

A_MV    = 0x40  # move

op_hvc = [
	("brk",),           # 0x00
	None, # 0x01
	None, # 0x02
	None, # 0x03
	None, # 0x04
	("ora", A_AB),      # 0x05
	("asl", A_AB),      # 0x06
	None, # 0x07
	("php",),           # 0x08
	("ora", A_IB),      # 0x09
	("asl", A_A),       # 0x0A
	None, # 0x0B
	None, # 0x0C
	("ora", A_AA),      # 0x0D
	("asl", A_AA),      # 0x0E
	None, # 0x0F
	("bpl", A_RB),      # 0x10
	("ora", A_NB, A_Y), # 0x11
	None, # 0x12
	None, # 0x13
	None, # 0x14
	("ora", A_AB, A_X), # 0x15
	("asl", A_AB, A_X), # 0x16
	None, # 0x17
	("clc",),           # 0x18
	("ora", A_AB, A_Y), # 0x19
	None, # 0x1A
	None, # 0x1B
	None, # 0x1C
	("ora", A_AA, A_X), # 0x1D
	("asl", A_AA, A_X), # 0x1E
	None, # 0x1F
	("jsr", A_AW),      # 0x20
	None, # 0x21
	None, # 0x22
	None, # 0x23
	("bit", A_AB),      # 0x24
	("and", A_AB),      # 0x25
	("rol", A_AB),      # 0x26
	None, # 0x27
	None, # 0x28
	("and", A_IB),      # 0x29
	("rol", A_A),       # 0x2A
	None, # 0x2B
	("bit", A_AA),      # 0x2C
	("and", A_AA),      # 0x2D
	None, # 0x2E
	None, # 0x2F
	("bmi", A_RB),      # 0x30
	None, # 0x31
	None, # 0x32
	None, # 0x33
	None, # 0x34
	None, # 0x35
	None, # 0x36
	None, # 0x37
	("sec",),           # 0x38
	None, # 0x39
	None, # 0x3A
	None, # 0x3B
	None, # 0x3C
	None, # 0x3D
	None, # 0x3E
	None, # 0x3F
	("rti",),           # 0x40
	None, # 0x41
	None, # 0x42
	None, # 0x43
	None, # 0x44
	("eor", A_AB),      # 0x45
	("lsr", A_AB),      # 0x46
	None, # 0x47
	("pha",),           # 0x48
	("eor", A_IB),      # 0x49
	("lsr",),           # 0x4A
	None, # 0x4B
	("jmp", A_AW),      # 0x4C
	None, # 0x4D
	None, # 0x4E
	None, # 0x4F
	None, # 0x50
	None, # 0x51
	None, # 0x52
	None, # 0x53
	None, # 0x54
	None, # 0x55
	None, # 0x56
	None, # 0x57
	None, # 0x58
	None, # 0x59
	None, # 0x5A
	None, # 0x5B
	None, # 0x5C
	None, # 0x5D
	None, # 0x5E
	None, # 0x5F
	("rts",),           # 0x60
	None, # 0x61
	None, # 0x62
	None, # 0x63
	None, # 0x64
	("adc", A_AB),      # 0x65
	None, # 0x66
	None, # 0x67
	("pla",),           # 0x68
	("adc", A_IB),      # 0x69
	("ror", A_A),       # 0x6A
	None, # 0x6B
	("jmp", A_NW),      # 0x6C
	("adc", A_AA),      # 0x6D
	("ror", A_AA),      # 0x6E
	None, # 0x6F
	("bvs", A_RB),      # 0x70
	None, # 0x71
	None, # 0x72
	None, # 0x73
	None, # 0x74
	None, # 0x75
	None, # 0x76
	None, # 0x77
	("sei",),           # 0x78
	("adc", A_AA, A_Y), # 0x79
	None, # 0x7A
	None, # 0x7B
	None, # 0x7C
	None, # 0x7D
	("ror", A_AA, A_X), # 0x7E
	None, # 0x7F
	None, # 0x80
	None, # 0x81
	None, # 0x82
	None, # 0x83
	("sty", A_AB),      # 0x84
	("sta", A_AB),      # 0x85
	("stx", A_AB),      # 0x86
	None, # 0x87
	("dey",),           # 0x88
	None, # 0x89
	("txa",),           # 0x8A
	None, # 0x8B
	("sty", A_AA),      # 0x8C
	("sta", A_AA),      # 0x8D
	("stx", A_AA),      # 0x8E
	None, # 0x8F
	("bcc", A_RB),      # 0x90
	("sta", A_NB, A_Y), # 0x91
	None, # 0x92
	None, # 0x93
	None, # 0x94
	("sta", A_AB, A_X), # 0x95
	None, # 0x96
	None, # 0x97
	("tya",),           # 0x98
	("sta", A_AA, A_Y), # 0x99
	("txs",),           # 0x9A
	None, # 0x9B
	None, # 0x9C
	("sta", A_AA, A_X), # 0x9D
	None, # 0x9E
	None, # 0x9F
	("ldy", A_IB),      # 0xA0
	None, # 0xA1
	("ldx", A_IB),      # 0xA2
	None, # 0xA3
	("ldy", A_AB),      # 0xA4
	("lda", A_AB),      # 0xA5
	("ldx", A_AB),      # 0xA6
	None, # 0xA7
	("tay",),           # 0xA8
	("lda", A_IB),      # 0xA9
	("tax",),           # 0xAA
	None, # 0xAB
	("ldy", A_AA),      # 0xAC
	("lda", A_AA),      # 0xAD
	("ldx", A_AA),      # 0xAE
	None, # 0xAF
	("bcs", A_RB),      # 0xB0
	("lda", A_NB, A_Y), # 0xB1
	None, # 0xB2
	None, # 0xB3
	("ldy", A_AB, A_X), # 0xB4
	("lda", A_AB, A_X), # 0xB5
	("ldx", A_AB, A_Y), # 0xB6
	None, # 0xB7
	None, # 0xB8
	("lda", A_AA, A_Y), # 0xB9
	None, # 0xBA
	None, # 0xBB
	("ldy", A_AA, A_X), # 0xBC
	("lda", A_AA, A_X), # 0xBD
	("ldx", A_AA, A_Y), # 0xBE
	None, # 0xBF
	("cpy", A_IB),      # 0xC0
	None, # 0xC1
	None, # 0xC2
	None, # 0xC3
	("cpy", A_AB),      # 0xC4
	("cmp", A_AB),      # 0xC5
	("dec", A_AB),      # 0xC6
	None, # 0xC7
	("iny",),           # 0xC8
	("cmp", A_IB),      # 0xC9
	("dex",),           # 0xCA
	None, # 0xCB
	None, # 0xCC
	("cmp", A_AA),      # 0xCD
	("dec", A_AA),      # 0xCE
	None, # 0xCF
	("bne", A_RB),      # 0xD0
	None, # 0xD1
	None, # 0xD2
	None, # 0xD3
	None, # 0xD4
	None, # 0xD5
	("dec", A_AB, A_X), # 0xD6
	None, # 0xD7
	("cld",),           # 0xD8
	("cmp", A_AA, A_Y), # 0xD9
	None, # 0xDA
	None, # 0xDB
	None, # 0xDC
	("cmp", A_AA, A_X), # 0xDD
	("dec", A_AA, A_X), # 0xDE
	None, # 0xDF
	("cpx", A_IB),      # 0xE0
	None, # 0xE1
	None, # 0xE2
	None, # 0xE3
	None, # 0xE4
	("sbc", A_AB),      # 0xE5
	("inc", A_AB),      # 0xE6
	None, # 0xE7
	("inx",),           # 0xE8
	("sbc", A_IB),      # 0xE9
	("nop",),           # 0xEA
	None, # 0xEB
	None, # 0xEC
	("sbc", A_AA),      # 0xED
	("inc", A_AA),      # 0xEE
	None, # 0xEF
	("beq", A_RB),      # 0xF0
	None, # 0xF1
	None, # 0xF2
	None, # 0xF3
	None, # 0xF4
	None, # 0xF5
	None, # 0xF6
	None, # 0xF7
	None, # 0xF8
	None, # 0xF9
	None, # 0xFA
	None, # 0xFB
	None, # 0xFC
	("sbc", A_AA, A_X), # 0xFD
	("inc", A_AA, A_X), # 0xFE
	None, # 0xFF
]

op_shvc = [
	None, # 0x00
	None, # 0x01
	None, # 0x02
	None, # 0x03
	("tsb", A_AB),      # 0x04
	("ora", A_AB),      # 0x05
	("asl", A_AB),      # 0x06
	("ora", A_XB),      # 0x07
	("php",),           # 0x08
	("ora", A_IA),      # 0x09
	("asl", A_A),       # 0x0A
	("phd",),           # 0x0B
	("tsb", A_AA),      # 0x0C
	("ora", A_AA),      # 0x0D
	("asl", A_AA),      # 0x0E
	None, # 0x0F
	("bpl", A_RB),      # 0x10
	None, # 0x11
	("ora", A_NB),      # 0x12
	None, # 0x13
	None, # 0x14
	("ora", A_AB, A_X), # 0x15
	None, # 0x16
	("ora", A_XB, A_Y), # 0x17
	("clc",),           # 0x18
	None, # 0x19
	("inc", A_A),       # 0x1A
	None, # 0x1B
	("trb", A_AA),      # 0x1C
	("ora", A_AA, A_X), # 0x1D
	None, # 0x1E
	("ora", A_AF, A_X), # 0x1F
	("jsr", A_AW),      # 0x20
	None, # 0x21
	("jsl", A_AL),      # 0x22
	None, # 0x23
	("bit", A_AB),      # 0x24
	("and", A_AB),      # 0x25
	("rol", A_AB),      # 0x26
	None, # 0x27
	("plp",),           # 0x28
	("and", A_IA),      # 0x29
	("rol", A_A),       # 0x2A
	("pld",),           # 0x2B
	("bit", A_AA),      # 0x2C
	("and", A_AA),      # 0x2D
	None, # 0x2E
	None, # 0x2F
	("bmi", A_RB),      # 0x30
	None, # 0x31
	("and", A_NB),      # 0x32
	None, # 0x33
	("bit", A_AB, A_X), # 0x34
	None, # 0x35
	None, # 0x36
	("and", A_XB, A_Y), # 0x37
	("sec",),           # 0x38
	("and", A_AA, A_Y), # 0x39
	("dec", A_A),       # 0x3A
	None, # 0x3B
	("bit", A_AA, A_X), # 0x3C
	("and", A_AA, A_X), # 0x3D
	None, # 0x3E
	("and", A_AF, A_X), # 0x3F
	("rti",),           # 0x40
	None, # 0x41
	None, # 0x42
	None, # 0x43
	("mvp", A_MV),      # 0x44
	("eor", A_AB),      # 0x45
	("lsr", A_AB),      # 0x46
	None, # 0x47
	("pha",),           # 0x48
	("eor", A_IA),      # 0x49
	("lsr", A_A),       # 0x4A
	("phk",),           # 0x4B
	("jmp", A_AW),      # 0x4C
	None, # 0x4D
	None, # 0x4E
	None, # 0x4F
	("bvc", A_RB),      # 0x50
	None, # 0x51
	("eor", A_NB),      # 0x52
	None, # 0x53
	("mvn", A_MV),      # 0x54
	None, # 0x55
	None, # 0x56
	None, # 0x57
	("cli",),           # 0x58
	None, # 0x59
	("phy",),           # 0x5A
	("tcd",),           # 0x5B
	("jml", A_AL),      # 0x5C
	None, # 0x5D
	("lsr", A_AA, A_X), # 0x5E
	None, # 0x5F
	("rts",),           # 0x60
	None, # 0x61
	None, # 0x62
	None, # 0x63
	("stz", A_AB),      # 0x64
	("adc", A_AB),      # 0x65
	("ror", A_AB),      # 0x66
	("adc", A_XB),      # 0x67
	("pla",),           # 0x68
	("adc", A_IA),      # 0x69
	("ror", A_A),       # 0x6A
	("rtl",),           # 0x6B
	("jmp", A_NW),      # 0x6C
	("adc", A_AA),      # 0x6D
	("ror", A_AA),      # 0x6E
	("adc", A_AF),      # 0x6F
	("bvs", A_RB),      # 0x70
	None, # 0x71
	("adc", A_NB),      # 0x72
	None, # 0x73
	None, # 0x74
	None, # 0x75
	None, # 0x76
	("adc", A_XB, A_Y), # 0x77
	("sei",),           # 0x78
	("adc", A_AA, A_Y), # 0x79
	("ply",),           # 0x7A
	None, # 0x7B
	("jmp", A_NWX),     # 0x7C
	("adc", A_AA, A_X), # 0x7D
	None, # 0x7E
	("adc", A_AF, A_X), # 0x7F
	("bra", A_RB),      # 0x80
	None, # 0x81
	None, # 0x82
	None, # 0x83
	("sty", A_AB),      # 0x84
	("sta", A_AB),      # 0x85
	("stx", A_AB),      # 0x86
	("sta", A_XB),      # 0x87
	("dey",),           # 0x88
	("bit", A_IA),      # 0x89
	("txa",),           # 0x8A
	("phb",),           # 0x8B
	("sty", A_AA),      # 0x8C
	("sta", A_AA),      # 0x8D
	("stx", A_AA),      # 0x8E
	("sta", A_AF),      # 0x8F
	("bcc", A_RB),      # 0x90
	("sta", A_NB, A_Y), # 0x91
	("sta", A_NB),      # 0x92
	None, # 0x93
	None, # 0x94
	("sta", A_AB, A_X), # 0x95
	None, # 0x96
	("sta", A_XB, A_Y), # 0x97
	("tya",),           # 0x98
	("sta", A_AA, A_Y), # 0x99
	("txs",),           # 0x9A
	("txy",),           # 0x9B
	("stz", A_AA),      # 0x9C
	("sta", A_AA, A_X), # 0x9D
	("stz", A_AA, A_X), # 0x9E
	("sta", A_AF, A_X), # 0x9F
	("ldy", A_IX),      # 0xA0
	None, # 0xA1
	("ldx", A_IX),      # 0xA2
	None, # 0xA3
	("ldy", A_AB),      # 0xA4
	("lda", A_AB),      # 0xA5
	("ldx", A_AB),      # 0xA6
	("lda", A_XB),      # 0xA7
	("tay",),           # 0xA8
	("lda", A_IA),      # 0xA9
	("tax",),           # 0xAA
	("plb",),           # 0xAB
	("ldy", A_AA),      # 0xAC
	("lda", A_AA),      # 0xAD
	("ldx", A_AA),      # 0xAE
	("lda", A_AF),      # 0xAF
	("bcs", A_RB),      # 0xB0
	("lda", A_NB, A_Y), # 0xB1
	("lda", A_NB),      # 0xB2
	None, # 0xB3
	("ldy", A_AB, A_X), # 0xB4
	("lda", A_AB, A_X), # 0xB5
	("ldx", A_AB, A_Y), # 0xB6
	("lda", A_XB, A_Y), # 0xB7
	None, # 0xB8
	("lda", A_AA, A_Y), # 0xB9
	None, # 0xBA
	("tyx",),           # 0xBB
	("ldy", A_AA, A_X), # 0xBC
	("lda", A_AA, A_X), # 0xBD
	("ldx", A_AA, A_Y), # 0xBE
	("lda", A_AF, A_X), # 0xBF
	("cpy", A_IX),      # 0xC0
	None, # 0xC1
	("rep", A_IB),      # 0xC2
	None, # 0xC3
	("cpy", A_AB),      # 0xC4
	("cmp", A_AB),      # 0xC5
	("dec", A_AB),      # 0xC6
	("cmp", A_XB),      # 0xC7
	("iny",),           # 0xC8
	("cmp", A_IA),      # 0xC9
	("dex",),           # 0xCA
	None, # 0xCB
	("cpy", A_AA),      # 0xCC
	("cmp", A_AA),      # 0xCD
	("dec", A_AA),      # 0xCE
	None, # 0xCF
	("bne", A_RB),      # 0xD0
	None, # 0xD1
	("cmp", A_NB),      # 0xD2
	None, # 0xD3
	None, # 0xD4
	None, # 0xD5
	None, # 0xD6
	None, # 0xD7
	None, # 0xD8
	("cmp", A_AA, A_Y), # 0xD9
	("phx",),           # 0xDA
	None, # 0xDB
	("jmp", A_XW),      # 0xDC
	("cmp", A_AA, A_X), # 0xDD
	("dec", A_AA, A_X), # 0xDE
	("cmp", A_AF, A_X), # 0xDF
	("cpx", A_IX),      # 0xE0
	None, # 0xE1
	("sep", A_IB),      # 0xE2
	None, # 0xE3
	("cpx", A_AB),      # 0xE4
	("sbc", A_AB),      # 0xE5
	("inc", A_AB),      # 0xE6
	None, # 0xE7
	("inx",),           # 0xE8
	("sbc", A_IA),      # 0xE9
	("nop",),           # 0xEA
	("xba",),           # 0xEB
	("cpx", A_AA),      # 0xEC
	("sbc", A_AA),      # 0xED
	("inc", A_AA),      # 0xEE
	None, # 0xEF
	("beq", A_RB),      # 0xF0
	("sbc", A_NB, A_Y), # 0xF1
	("sbc", A_NB),      # 0xF2
	None, # 0xF3
	("pea", A_AA),      # 0xF4
	None, # 0xF5
	None, # 0xF6
	None, # 0xF7
	None, # 0xF8
	("sbc", A_AA, A_Y), # 0xF9
	("plx",),           # 0xFA
	("xce",),           # 0xFB
	("jsr", A_NWX),     # 0xFC
	("sbc", A_AA, A_X), # 0xFD
	("inc", A_AA, A_X), # 0xFE
	("sbc", A_AF, A_X), # 0xFF
]

op_table = None
fmt_addr = None
btbl = {}

def init(self, seg, addr, i):
	global op_table
	global fmt_addr
	global op
	hvc.init(self, seg, addr)
	op_table = (op_hvc, op_shvc)[i]
	fmt_addr = "%%0%dX" % (2*(2+i))
	op = None

def fmt(self, line, btbl, code=False):
	f = self.file[-1][1]
	last = None
	for addr, ln in line:
		if last != addr:
			sym = self.get_sym(addr)
			if sym is not None:
				if "-" not in sym.label and "+" not in sym.label:
					#if code == sym.label.startswith("data_"): print(sym.label)
					if "A16" in sym.flag: f.append(".a16\n")
					if "A8"  in sym.flag: f.append(".a8\n")
					if "I16" in sym.flag: f.append(".i16\n")
					if "I8"  in sym.flag: f.append(".i8\n")
					if "LOCAL" not in sym.flag and \
						not sym.label.startswith("_"):
						f.append("\n")
						if hvc.COMM_LABEL:
							f.append("; $%s\n" % (fmt_addr % addr))
					if "GLOBL" in sym.flag: f.append(".global %s\n" % sym.label)
					f.append("%s:\n" % sym.label)
			elif addr in btbl: f.append("_%s:\n" % (fmt_addr % addr))
			last = addr
		if hvc.COMM_LINE and not 0xFFB0 <= addr < 0x10000:
			f.append("/*%s*/" % (fmt_addr % addr))
		f.append("\t%s\n" % ln)
	if last is None and self.addr in btbl:
		f.append("_%s:\n" % (fmt_addr % self.addr))
		btbl.remove(self.addr)

def s_code(self, argv):
	global op
	seg, start, end, i, p = argv
	init(self, seg, start, i)
	if seg not in btbl: btbl[seg] = set()
	line = []
	while self.addr < end:
		self.save = self.addr
		sym = self.get_sym(self.save)
		if sym is not None:
			if "A16" in sym.flag: p &= ~0x20
			if "A8"  in sym.flag: p |=  0x20
			if "I16" in sym.flag: p &= ~0x10
			if "I8"  in sym.flag: p |=  0x10
		ln = self.macro()
		if ln is not None:
			line.extend(ln)
			continue
		self.addr = self.save
		op = self.u8()
		# rep
		if op == 0xC2:
			p &= ~self.u8()
			self.addr -= 1
		# sep
		if op == 0xE2:
			p |= self.u8()
			self.addr -= 1
		argv = op_table[op]
		if argv is not None:
			lst = []
			imm = self.get_imm(self.save)
			for i, arg in enumerate(argv[1:]):
				if arg == A_IA: arg = A_IB if (p & 0x20) else A_IW
				if arg == A_IX: arg = A_IB if (p & 0x10) else A_IW
				if   arg == A_Y:  lst.append("y")
				elif arg == A_A:  lst.append("a")
				elif arg == A_X:  lst.append("x")
				elif arg == A_IB: lst.append(self.fmt(
					imm[i] if imm is not None and imm[i] is not None
					else "#$%02X",
					self.u8()
				))
				elif arg == A_IW: lst.append(self.fmt(
					imm[i] if imm is not None and imm[i] is not None
					else "#$%04X",
					self.u16()
				))
				elif arg == A_AB: lst.append(hvc.ab(self))
				elif arg == A_AW: lst.append(hvc.aw(self))
				elif arg == A_AL: lst.append(hvc.al(self))
				elif arg == A_AA: lst.append(hvc.aw(self, True))
				elif arg == A_AF: lst.append(hvc.al(self, True))
				elif arg == A_RB:
					bdst = self.s8() + self.addr
					sym = self.get_sym(bdst)
					if sym is not None:
						lst.append(sym.label)
					else:
						btbl[seg].add(bdst)
						lst.append("_%s" % (fmt_addr % bdst))
				elif arg == A_XB: lst.append("[%s]" % hvc.ab(self))
				elif arg == A_XW: lst.append("[%s]" % hvc.aw(self))
				elif arg == A_NB: lst.append("(%s)" % hvc.ab(self))
				elif arg == A_NW: lst.append("(%s)" % hvc.aw(self))
				elif arg == A_NWX:
					lst.append("(.loword(%s),x)" % hvc.aw(self))
					if False:
						self.addr-=2
						if self.u16() == (self.addr&0xffff):
							print("---> STOP 0x%06X" % self.addr)
				elif arg == A_MV:
					y = self.u8()
					x = self.u8()
					lst.append("#$%02X" % x)
					lst.append("#$%02X" % y)
				else:
					raise RuntimeError("hvc.asm.s_code(): bad arg")
			ln = argv[0]
			if len(lst) > 0: ln += " " + ",".join(lst)
			line.append((self.save, ln))
			sym = self.get_sym(self.save)
			if sym is not None:
				if "-" not in sym.label and "+" not in sym.label:
					if sym.label.startswith("data_"):
						raise RuntimeError(sym.label)
			if False:
				if 0x01F446 <= self.save < 0x020000:
					print("0x%06X %s" % line[-1])
			if False:
				print("0x%04X %s" % line[-1])
				if line[-1][-1] == "jsr $8E04":
					print("---> STOP 0x%04X" % self.addr)
		else:
			raise RuntimeError(
				"hvc.asm.s_code(): illegal opcode 0x%s $%02X (p=$%02X)" % (
					fmt_addr % self.save, op, p
				)
			)
	fmt(self, line, btbl[seg], True)

d_byte    = [".byte",    lambda self: "$%02X" % self.u8()]
d_sbyte   = [".byte",    lambda self: "%d"    % self.s8()]
d_ubyte   = [".byte",    lambda self: "%d"    % self.u8()]
d_word    = [".word",    lambda self: "$%04X" % self.u16()]
d_sword   = [".word",    lambda self: "%d"    % self.s16()]
d_uword   = [".word",    lambda self: "%d"    % self.u16()]
d_addr    = [".addr",    lambda self: hvc.aw(self)]
d_faraddr = [".faraddr", lambda self: hvc.al(self)]

def lst_main(self, line, lst):
	for argv in lst:
		for _ in range(argv[0]):
			if type(argv[1]) == list:
				lst_main(self, line, argv[1])
			else:
				self.save = self.addr
				n = argv[1]
				t = argv[2]
				if t == "ascii":
					line.append((self.save, ".byte \"%s\"" % "".join([
						chr(self.u8()) for _ in range(n)]
					)))
				elif t == "lh":
					b = [[self.u8() for _ in range(n)] for _ in range(2)]
					s = ",".join([
						hvc.sym_lh(self, lo, hi)
						for lo, hi in zip(b[0], b[1])
					])
					for i, c in enumerate(("lobytes", "hibytes")):
						line.append((self.save + n*i, ".%s %s" % (c, s)))
				elif t == "lhb":
					b = [[self.u8() for _ in range(n)] for _ in range(3)]
					s = ",".join([
						hvc.sym_lhb(self, lo, hi, ba)
						for lo, hi, ba in zip(b[0], b[1], b[2])
					])
					for i, c in enumerate(("lobytes", "hibytes", "bankbytes")):
						line.append((self.save + n*i, ".%s %s" % (
							c.ljust(10), s
						)))
				else:
					line.append((self.save, "%s %s" % (
						t[0], ",".join([t[1](self) for _ in range(n)])
					)))

def s_data(self, argv):
	seg, start, end, i = argv[:4]
	init(self, seg, start, i)
	line = []
	if len(argv) > 4:
		lst = argv[4]
		if type(lst) is str:
			table = {
				"byte":    (8, 1, d_byte),
				"word":    (4, 2, d_word),
				"addr":    (1, 2, d_addr),
				"faraddr": (1, 3, d_faraddr),
			}
			if lst in table:
				w, s, f = table[lst]
				t = lst
				l = (end-start)//s
				r = l % w
				lst = [[l//w, w, f]]
				if r > 0: lst.append([1, r, f])
	else:
		lst = [[end-start, 1, d_byte]]
	lst_main(self, line, lst)
	fmt(self, line, set())
