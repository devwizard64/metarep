import ultra

I_OP    = 0
I_FUNC  = 1
I_RS    = 2
I_RT    = 3
I_RD    = 4
I_SA    = 5
I_CACHE = 6
I_CODE  = 7
I_C0REG = 8
I_C1CTL = 9
I_C1FMT = 10
I_FT    = 11
I_FS    = 12
I_FD    = 13
I_VT    = 14
I_VS    = 15
I_VD    = 16
I_EV    = 17
I_DE    = 18
I_E     = 19
I_OFFS  = 20
I_IMMS  = 21
I_IMMU  = 22
I_IMMH  = 23
I_BDST  = 24
I_JDST  = 25

gpr_cpu = [
	"$0",  "$at", "$v0", "$v1",
	"$a0", "$a1", "$a2", "$a3",
	"$t0", "$t1", "$t2", "$t3",
	"$t4", "$t5", "$t6", "$t7",
	"$s0", "$s1", "$s2", "$s3",
	"$s4", "$s5", "$s6", "$s7",
	"$t8", "$t9", "$k0", "$k1",
	"$gp", "$sp", "$s8", "$ra",
]

gpr_rsp = [
	"$0",  "$1",  "$2",  "$3",
	"$4",  "$5",  "$6",  "$7",
	"$8",  "$9",  "$10", "$11",
	"$12", "$13", "$14", "$15",
	"$16", "$17", "$18", "$19",
	"$20", "$21", "$22", "$23",
	"$24", "$25", "$26", "$27",
	"$28", "$29", "$30", "$ra",
]

cop0_cpu = [
	"C0_INX",
	"C0_RAND",
	"C0_ENTRYLO0",
	"C0_ENTRYLO1",
	"C0_CONTEXT",
	"C0_PAGEMASK",
	"C0_WIRED",
	None,
	"C0_BADVADDR",
	"C0_COUNT",
	"C0_ENTRYHI",
	"C0_COMPARE",
	"C0_SR",
	"C0_CAUSE",
	"C0_EPC",
	"C0_PRID",
	"C0_CONFIG",
	"C0_LLADDR",
	"C0_WATCHLO",
	"C0_WATCHHI",
	None,
	None,
	None,
	None,
	None,
	None,
	"C0_ECC",
	"C0_CACHE_ERR",
	"C0_TAGLO",
	"C0_TAGHI",
	"C0_ERROR_EPC",
	None,
]

cop0_rsp = [
	"SP_MEM_ADDR",
	"SP_DRAM_ADDR",
	"SP_RD_LEN",
	"SP_WR_LEN",
	"SP_STATUS",
	"SP_DMA_FULL",
	"SP_DMA_BUSY",
	"SP_SEMAPHORE",
	"DPC_START",
	"DPC_END",
	"DPC_CURRENT",
	"DPC_STATUS",
	"DPC_CLOCK",
	"DPC_BUFBUSY",
	"DPC_PIPEBUSY",
	"DPC_TMEM",
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
]

cop1_ctl = (
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"$31", # FCSR
)

cop1_fmt = (
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"s",
	"d",
	None,
	None,
	"w",
	"l",
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
)

cop2_ctl = (
	"vco",
	"vcc",
	"vce",
	None,
)

element_table = (
	"", # 0000
	"", # 0001 (invalid)
	"[0q]", # 0010
	"[1q]", # 0011
	"[0h]", # 0100
	"[1h]", # 0101
	"[2h]", # 0110
	"[3h]", # 0111
	"[0]",  # 1000
	"[1]",  # 1001
	"[2]",  # 1010
	"[3]",  # 1011
	"[4]",  # 1100
	"[5]",  # 1101
	"[6]",  # 1110
	"[7]",  # 1111
)

btbl = {}

def sym(self, addr, src=None):
	btbl[self.seg].add(addr)
	sym = self.get_sym(addr)
	if sym is not None: return sym.label
	if mode == 0: return "%d$" % ((addr-addr_s) >> 2)
	return ".L%08X" % addr

def aw(self, src=None):
	return sym(self, self.u32(), src)

def str_prc(self, ptr, argv):
	if imm is not None:
		i = 0
		for arg in argv:
			if arg in {
				I_SA,
				I_CACHE,
				I_CODE,
				I_OFFS,
				I_IMMS,
				I_IMMU,
				I_IMMH,
				I_BDST,
				I_JDST,
			}:
				if imm[i] is not None: inst_fmt[arg] = imm[i]
				i += 1
	lst = tuple([self.fmt(inst_fmt[arg], inst_arg[arg]) for arg in argv])
	if None in lst:
		raise RuntimeError("ultra.asm.str_prc(): bad arg (\"%s\" %% %s)" % (
			ptr, str(lst)
		))
	return ptr % lst

def lst_prc(self, ptr, argv):
	p = ptr[inst_arg[argv[0]]]
	if p is not None:
		ptr, argv = p
		if type(ptr) == list:   return lst_prc(self, ptr, argv)
		if type(ptr) == str:    return str_prc(self, ptr, argv)
		if callable(ptr):       return ptr(self, argv)
		raise RuntimeError("ultra.asm.lst_prc(): bad arg (%s)" % str(p))
	return None

def lui_write(reg, val):
	if lui_flag & 1: lui_table[reg] = val
	if lui_flag & 2: lui_next[reg]  = val

def fnc_clear(self, argv):
	reg = inst_arg[argv[1]]
	op   = inst_arg[I_OP]
	func = inst_arg[I_FUNC]
	rs   = inst_arg[I_RS]
	rt   = inst_arg[I_RT]
	if not (op == 0x00 and func == 0x21) or (reg != rs and reg != rt):
		lui_write(reg, None)
	return str_prc(self, argv[0], argv[1:])

def fnc_clearf(self, argv):
	return str_prc(self, argv[0], argv[1:])

def fnc_clearv(self, argv):
	return str_prc(self, argv[0], argv[1:])

def fnc_or(self, argv):
	ptr, argv = ["or      %s, %s, %s", [I_RD, I_RS, I_RT]]
	if mode == 0:
		if inst_arg[I_RT] == 0:
			ptr, argv = ["move    %s, %s", [I_RD, I_RS]]
	lui_write(inst_arg[I_RD], None)
	return str_prc(self, ptr, argv)

def fnc_j(self, argv):
	if argv[1][0] == I_JDST:
		jdst = inst_arg[I_JDST]
		inst_arg[I_JDST] = ultra.sym(self, jdst, self.save)
		#if argv[0].startswith("j       "):
		#    inst_arg[I_JDST] = sym(self, jdst, self.save)
		#else:
		#    inst_arg[I_JDST] = ultra.sym(self, jdst, self.save)
		inst_fmt[I_JDST] = "%s"
	return str_prc(self, argv[0], argv[1])

def fnc_b(self, argv):
	global lui_next
	global lui_flag
	bdst = inst_arg[I_BDST]
	lui_stack[bdst] = lui_next = lui_table[:]
	inst_arg[I_BDST] = sym(self, bdst)
	inst_fmt[I_BDST] = "%s"
	cnt, ptr = argv[:2]
	argv = [I_RS, I_RT]
	lui_flag = 3
	# regimm
	if inst_arg[I_OP] == 0x01:
		# b?z $0
		if inst_arg[I_RS] == 0:
			# bgezal $0 -> bal
			if inst_arg[I_RT] == 0x11:
				cnt, ptr = [0, "bal     "]
			# bgezall $0 -> ball
			elif inst_arg[I_RT] == 0x13:
				cnt, ptr = [0, "ball    "]
		if inst_arg[I_RT] in {0x02, 0x03, 0x12, 0x13}:
			lui_flag = 2
	# bc1?
	elif inst_arg[I_OP] == 0x11:
		if inst_arg[I_RS] == 0x08:
			if inst_arg[I_RT] in {0x02, 0x03}:
				lui_flag = 2
	# b? rs, $0
	elif inst_arg[I_RT] == 0x00:
		# beq
		if inst_arg[I_OP] == 0x04:
			# beq $0, $0 -> b
			if inst_arg[I_RS] == 0:
				cnt, ptr = [0, "b       "]
			# beq rs, $0 -> beqz rs
			else:
				cnt, ptr = [1, "beqz    "]
		# bne rs, $0 -> bnez rs
		elif inst_arg[I_OP] == 0x05:
			cnt, ptr = [1, "bnez    "]
		# beql rs, $0 -> beqzl rs
		elif inst_arg[I_OP] == 0x14:
			cnt, ptr = [1, "beqzl   "]
		# bnel rs, $0 -> bnezl rs
		elif inst_arg[I_OP] == 0x15:
			cnt, ptr = [1, "bnezl   "]
	for i in range(cnt):
		ptr += "%s, "
	return str_prc(self, ptr + "%s", argv[:cnt] + [I_BDST])

def fnc_addiu(self, argv):
	ptr, argv = ["addiu   %s, %s, %s", [I_RT, I_RS, I_IMMS]]
	if mode == 0:
		# addiu rt, $0, imm -> li rt, imm
		if inst_arg[I_RS] == 0:
			ptr, argv = ["li      %s, %s", [I_RT, I_IMMS]]
		# lui rt, hi(addr) ... addiu rt, rt, lo(addr)
		elif lui_table[inst_arg[I_RS]] is not None:
			ln, immh = lui_table[inst_arg[I_RS]]
			inst_arg[I_IMMS] = ultra.sym(
				self, immh + inst_arg[I_IMMS], self.save
			)
			inst_fmt[I_IMMS] = "%s"
			if inst_arg[I_RT] == inst_arg[I_RS]:
				if macro:
					line[ln] = (
						line[ln][0],
						str_prc(self, "la.u    %s, %s", [I_RS, I_IMMS])
					)
					ptr, argv = ["la.l    %s, %s", [I_RT, I_IMMS]]
				else:
					line[ln] = (
						line[ln][0],
						str_prc(self, "lui     %s, %%hi(%s)", [I_RS, I_IMMS])
					)
					ptr, argv = ["addiu   %s, %%lo(%s)", [I_RT, I_IMMS]]
			else:
				line[ln] = (
					line[ln][0],
					str_prc(self, "lui     %s, %%hi(%s)", [I_RS, I_IMMS])
				)
				ptr, argv = ["addiu   %s, %s, %%lo(%s)", [I_RT, I_RS, I_IMMS]]
	else:
		# ARMIPS rejects this
		# if inst_arg[I_RS] == 0:
		#     inst_arg[I_IMMU] = ultra.sym(self, inst_arg[I_IMMU], self.save)
		#     inst_fmt[I_IMMU] = "%s"
		#     ptr, argv = ["la      %s, %s", [I_RT, I_IMMU]]
		pass
	lui_write(inst_arg[I_RT], None)
	return str_prc(self, ptr, argv)

def fnc_ori(self, argv):
	ptr, argv = ["ori     %s, %s, %s", [I_RT, I_RS, I_IMMU]]
	if inst_arg[I_RS] == 0:
		if mode == 0:
			# ori rt, $0, imm -> li rt, imm
			if inst_arg[I_IMMU] >= 0x8000:
				ptr, argv = ["li      %s, %s", [I_RT, I_IMMU]]
		else:
			pass
	# lui rt, imm ... ori rt, rt, imm -> li.u rt, imm ... li.l rt, imm
	elif inst_arg[I_RT] == inst_arg[I_RS]:
		if lui_table[inst_arg[I_RT]] is not None:
			ln, immh = lui_table[inst_arg[I_RT]]
			inst_arg[I_IMMU] = immh | inst_arg[I_IMMU]
			inst_fmt[I_IMMU] = "0x%08X"
			if line[ln][1].startswith("li"):
				if macro:
					line[ln] = (
						line[ln][0],
						str_prc(self, "li.u    %s, %s", [I_RT, I_IMMU])
					)
					ptr, argv = ["li.l    %s, %s", [I_RT, I_IMMU]]
				else:
					line[ln] = (
						line[ln][0],
						str_prc(self, "lui     %s, %s >> 16", [I_RT, I_IMMU])
					)
					ptr, argv = ["ori     %s, %s & 0xFFFF", [I_RT, I_IMMU]]
	lui_write(inst_arg[I_RT], None)
	return str_prc(self, ptr, argv)

def fnc_lui(self, argv):
	if inst_arg[I_RT] != 0:
		lui_write(inst_arg[I_RT], (len(line), inst_arg[I_IMMH]))
	if imm is not None:
		ptr, argv = "lui     %s, %s", [I_RT, I_IMMU]
	else:
		ptr, argv = "li      %s, %s", [I_RT, I_IMMH]
	return str_prc(self, ptr, argv)

def rsp_prc(self, i):
	sym = self.find_sym(0x04000000 | inst_arg[i], self.save)
	if sym is not None:
		inst_arg[i] = sym.label
		inst_fmt[i] = "lo(%s)"
	# else:
	# 	print("0x%03X," % inst_arg[i])

def fnc_ls(self, argv):
	ptr, argv = [argv[0], [argv[1], I_IMMS, I_RS]]
	if mode == 0:
		if lui_table[inst_arg[I_RS]] is not None:
			ln, immh = lui_table[inst_arg[I_RS]]
			inst_arg[I_IMMS] = ultra.sym(
				self, immh + inst_arg[I_IMMS], self.save
			)
			inst_fmt[I_IMMS] = "%%hi(%s)"
			line[ln] = (
				line[ln][0], str_prc(self, "lui     %s, %s", [I_RS, I_IMMS])
			)
			inst_fmt[I_IMMS] = "%%lo(%s)"
		if ptr in {
			"lb      ",
			"lh      ",
			"lwl     ",
			"lw      ",
			"lbu     ",
			"lhu     ",
			"lwr     ",
			"lwu     ",
		}:
			lui_write(inst_arg[argv[0]], None)
		# this doesn't really make sense, but it fixes libultra
		elif ptr == "cache   ":
			lui_write(inst_arg[argv[2]], None)
	else:
		if inst_arg[I_RS] == 0:
			rsp_prc(self, I_IMMS)
	ptr += "%s, %s(%s)"
	return str_prc(self, ptr, argv)

def fnc_lsv(self, argv):
	inst_arg[I_OFFS] <<= argv[1]
	ptr, argv = [argv[0], [I_VT, I_E, I_OFFS, I_RS]]
	if mode == 0:
		pass
	else:
		if inst_arg[I_RS] == 0:
			rsp_prc(self, I_OFFS)
	ptr += "%s%s, %s(%s)"
	return str_prc(self, ptr, argv)

lst_special = [
	(fnc_clear, ["sll     %s, %s, %s", I_RD, I_RT, I_SA]),
	None,
	(fnc_clear, ["srl     %s, %s, %s", I_RD, I_RT, I_SA]),
	(fnc_clear, ["sra     %s, %s, %s", I_RD, I_RT, I_SA]),
	(fnc_clear, ["sllv    %s, %s, %s", I_RD, I_RT, I_RS]),
	None,
	(fnc_clear, ["srlv    %s, %s, %s", I_RD, I_RT, I_RS]),
	(fnc_clear, ["srav    %s, %s, %s", I_RD, I_RT, I_RS]),
	(fnc_j, ["jr      %s", [I_RS]]),
	(fnc_j, ["jalr    %s", [I_RS]]),
	None,
	None,
	("syscall %s", [I_CODE]),
	("break   %s", [I_CODE]),
	None,
	("sync", []),
	(fnc_clear, ["mfhi    %s", I_RD]),
	("mthi    %s", [I_RS]),
	(fnc_clear, ["mflo    %s", I_RD]),
	("mtlo    %s", [I_RS]),
	(fnc_clear, ["dsllv   %s, %s, %s", I_RD, I_RT, I_RS]),
	None,
	(fnc_clear, ["dsrlv   %s, %s, %s", I_RD, I_RT, I_RS]),
	(fnc_clear, ["dsrav   %s, %s, %s", I_RD, I_RT, I_RS]),
	("mult    %s, %s", [I_RS, I_RT]),
	("multu   %s, %s", [I_RS, I_RT]),
	("div     %s, %s, %s", [I_RD, I_RS, I_RT]),
	("divu    %s, %s, %s", [I_RD, I_RS, I_RT]),
	("dmult   %s, %s", [I_RS, I_RT]),
	("dmultu  %s, %s", [I_RS, I_RT]),
	("ddiv    %s, %s, %s", [I_RD, I_RS, I_RT]),
	("ddivu   %s, %s, %s", [I_RD, I_RS, I_RT]),
	(fnc_clear, ["add     %s, %s, %s", I_RD, I_RS, I_RT]),
	(fnc_clear, ["addu    %s, %s, %s", I_RD, I_RS, I_RT]),
	(fnc_clear, ["sub     %s, %s, %s", I_RD, I_RS, I_RT]),
	(fnc_clear, ["subu    %s, %s, %s", I_RD, I_RS, I_RT]),
	(fnc_clear, ["and     %s, %s, %s", I_RD, I_RS, I_RT]),
	(fnc_or, None),
	(fnc_clear, ["xor     %s, %s, %s", I_RD, I_RS, I_RT]),
	(fnc_clear, ["nor     %s, %s, %s", I_RD, I_RS, I_RT]),
	None,
	None,
	(fnc_clear, ["slt     %s, %s, %s", I_RD, I_RS, I_RT]),
	(fnc_clear, ["sltu    %s, %s, %s", I_RD, I_RS, I_RT]),
	(fnc_clear, ["dadd    %s, %s, %s", I_RD, I_RS, I_RT]),
	(fnc_clear, ["daddu   %s, %s, %s", I_RD, I_RS, I_RT]),
	(fnc_clear, ["dsub    %s, %s, %s", I_RD, I_RS, I_RT]),
	(fnc_clear, ["dsubu   %s, %s, %s", I_RD, I_RS, I_RT]),
	("tge     %s, %s, %s", [I_RS, I_RT, I_SA]),
	("tgeu    %s, %s, %s", [I_RS, I_RT, I_SA]),
	("tlt     %s, %s, %s", [I_RS, I_RT, I_SA]),
	("tltu    %s, %s, %s", [I_RS, I_RT, I_SA]),
	("teq     %s, %s, %s", [I_RS, I_RT, I_SA]),
	None,
	("tne     %s, %s, %s", [I_RS, I_RT, I_SA]),
	None,
	(fnc_clear, ["dsll    %s, %s, %s", I_RD, I_RT, I_SA]),
	None,
	(fnc_clear, ["dsrl    %s, %s, %s", I_RD, I_RT, I_SA]),
	(fnc_clear, ["dsra    %s, %s, %s", I_RD, I_RT, I_SA]),
	(fnc_clear, ["dsll32  %s, %s, %s", I_RD, I_RT, I_SA]),
	None,
	(fnc_clear, ["dsrl32  %s, %s, %s", I_RD, I_RT, I_SA]),
	(fnc_clear, ["dsra32  %s, %s, %s", I_RD, I_RT, I_SA]),
]

lst_regimm = [
	(fnc_b, [1, "bltz    "]),
	(fnc_b, [1, "bgez    "]),
	(fnc_b, [1, "bltzl   "]),
	(fnc_b, [1, "bgezl   "]),
	None,
	None,
	None,
	None,
	None, # tgei
	None, # tgeiu
	None, # tlti
	None, # tltiu
	None, # teqi
	None,
	None, # tnei
	None,
	(fnc_b, [1, "bltzal  "]),
	(fnc_b, [1, "bgezal  "]),
	(fnc_b, [1, "bltzall "]),
	(fnc_b, [1, "bgezall "]),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
]

lst_cop0_func = [
	None,
	("tlbr", []),
	("tlbwi", []),
	None,
	None,
	None,
	("tlbwr", []),
	None,
	("tlbp", []),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	("eret", []),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
]

lst_cop0_rs = [
	(fnc_clear, ["mfc0    %s, %s", I_RT, I_C0REG]),
	(fnc_clear, ["dmfc0   %s, %s", I_RT, I_C0REG]),
	None, # (fnc_clear, ["cfc0    %s, %s", I_RT, I_C0CTL]),
	None,
	("mtc0    %s, %s", [I_RT, I_C0REG]),
	("dmtc0   %s, %s", [I_RT, I_C0REG]),
	None, # ("ctc0    %s, %s", [I_RT, I_C0CTL]),
	None,
	None, # (lst_bc0, [I_RT]),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	(lst_cop0_func, [I_FUNC]),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
]

lst_bc1 = [
	(fnc_b, [0, "bc1f    "]),
	(fnc_b, [0, "bc1t    "]),
	(fnc_b, [0, "bc1fl   "]),
	(fnc_b, [0, "bc1tl   "]),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
]

lst_cop1_func = [
	(fnc_clearf, ["add.%s   %s, %s, %s", I_C1FMT, I_FD, I_FS, I_FT]),
	(fnc_clearf, ["sub.%s   %s, %s, %s", I_C1FMT, I_FD, I_FS, I_FT]),
	(fnc_clearf, ["mul.%s   %s, %s, %s", I_C1FMT, I_FD, I_FS, I_FT]),
	(fnc_clearf, ["div.%s   %s, %s, %s", I_C1FMT, I_FD, I_FS, I_FT]),
	(fnc_clearf, ["sqrt.%s  %s, %s",     I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["abs.%s   %s, %s",     I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["mov.%s   %s, %s",     I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["neg.%s   %s, %s",     I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["round.l.%s %s, %s",   I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["trunc.l.%s %s, %s",   I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["ceil.l.%s %s, %s",    I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["floor.l.%s %s, %s",   I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["round.w.%s %s, %s",   I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["trunc.w.%s %s, %s",   I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["ceil.w.%s %s, %s",    I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["floor.w.%s %s, %s",   I_C1FMT, I_FD, I_FS]),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	(fnc_clearf, ["cvt.s.%s %s, %s",     I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["cvt.d.%s %s, %s",     I_C1FMT, I_FD, I_FS]),
	None,
	None,
	(fnc_clearf, ["cvt.w.%s %s, %s",     I_C1FMT, I_FD, I_FS]),
	(fnc_clearf, ["cvt.l.%s %s, %s",     I_C1FMT, I_FD, I_FS]),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	("c.f.%s   %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.un.%s  %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.eq.%s  %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.ueq.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.olt.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.ult.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.ole.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.ule.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.sf.%s  %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.ngle.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.seq.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.ngl.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.lt.%s  %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.nge.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.le.%s  %s, %s", [I_C1FMT, I_FS, I_FT]),
	("c.ngt.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
]

lst_cop1_rs = [
	(fnc_clear, ["mfc1    %s, %s", I_RT, I_FS]),
	(fnc_clear, ["dmfc1   %s, %s", I_RT, I_FS]),
	(fnc_clear, ["cfc1    %s, %s", I_RT, I_C1CTL]),
	None,
	("mtc1    %s, %s", [I_RT, I_FS]),
	("dmtc1   %s, %s", [I_RT, I_FS]),
	("ctc1    %s, %s", [I_RT, I_C1CTL]),
	None,
	(lst_bc1, [I_RT]),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	(lst_cop1_func, [I_FUNC]),
	(lst_cop1_func, [I_FUNC]),
	None,
	None,
	(lst_cop1_func, [I_FUNC]),
	(lst_cop1_func, [I_FUNC]),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
]

lst_cop2_func = [
	(fnc_clearv, ["vmulf   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmulu   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vrndp   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmulq   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmudl   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmudm   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmudn   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmudh   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmacf   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmacu   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vrndn   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmacq   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmadl   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmadm   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmadn   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmadh   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vadd    %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vsub    %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vsut    %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]), # undoc.
	(fnc_clearv, ["vabs    %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vaddc   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vsubc   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vaddb   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]), # undoc.
	(fnc_clearv, ["vsubb   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]), # undoc.
	(fnc_clearv, ["vaccb   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]), # undoc.
	(fnc_clearv, ["vsucb   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]), # undoc.
	(fnc_clearv, ["vsad    %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]), # undoc.
	(fnc_clearv, ["vsac    %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]), # undoc.
	(fnc_clearv, ["vsum    %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]), # undoc.
	(fnc_clearv, ["vsar    %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	None,
	None,
	(fnc_clearv, ["vlt     %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["veq     %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vne     %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vge     %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vcl     %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vch     %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vcr     %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vmrg    %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vand    %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vnand   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vor     %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vnor    %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vxor    %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	(fnc_clearv, ["vnxor   %s, %s, %s%s", I_VD, I_VS, I_VT, I_EV]),
	None,
	None,
	(fnc_clearv, ["vrcp    %s%s, %s%s", I_VD, I_DE, I_VT, I_EV]),
	(fnc_clearv, ["vrcpl   %s%s, %s%s", I_VD, I_DE, I_VT, I_EV]),
	(fnc_clearv, ["vrcph   %s%s, %s%s", I_VD, I_DE, I_VT, I_EV]),
	(fnc_clearv, ["vmov    %s%s, %s%s", I_VD, I_DE, I_VT, I_EV]),
	(fnc_clearv, ["vrsq    %s%s, %s%s", I_VD, I_DE, I_VT, I_EV]),
	(fnc_clearv, ["vrsql   %s%s, %s%s", I_VD, I_DE, I_VT, I_EV]),
	(fnc_clearv, ["vrsqh   %s%s, %s%s", I_VD, I_DE, I_VT, I_EV]),
	("vnop", []),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
]

lst_cop2_rs = [
	(fnc_clear, ["mfc2    %s, %s%s", I_RT, I_VS, I_E]),
	None,
	(fnc_clear, ["cfc2    %s, %s", I_RT, I_RD]),
	None,
	("mtc2    %s, %s%s", [I_RT, I_VS, I_E]),
	None,
	("ctc2    %s, %s", [I_RT, I_RD]),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
	(lst_cop2_func, [I_FUNC]),
]

lst_lwc2 = [
	(fnc_lsv, ["lbv     ", 0]),
	(fnc_lsv, ["lsv     ", 1]),
	(fnc_lsv, ["llv     ", 2]),
	(fnc_lsv, ["ldv     ", 3]),
	(fnc_lsv, ["lqv     ", 4]),
	(fnc_lsv, ["lrv     ", 4]),
	(fnc_lsv, ["lpv     ", 3]),
	(fnc_lsv, ["luv     ", 3]),
	(fnc_lsv, ["lhv     ", 4]),
	(fnc_lsv, ["lfv     ", 4]),
	(fnc_lsv, ["lwv     ", 4]), # undoc.
	(fnc_lsv, ["ltv     ", 4]),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
]

lst_swc2 = [
	(fnc_lsv, ["sbv     ", 0]),
	(fnc_lsv, ["ssv     ", 1]),
	(fnc_lsv, ["slv     ", 2]),
	(fnc_lsv, ["sdv     ", 3]),
	(fnc_lsv, ["sqv     ", 4]),
	(fnc_lsv, ["srv     ", 4]),
	(fnc_lsv, ["spv     ", 3]),
	(fnc_lsv, ["suv     ", 3]),
	(fnc_lsv, ["shv     ", 4]),
	(fnc_lsv, ["sfv     ", 4]),
	(fnc_lsv, ["swv     ", 4]),
	(fnc_lsv, ["stv     ", 4]),
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
]

lst_op = [
	(lst_special, [I_FUNC]),
	(lst_regimm, [I_RT]),
	(fnc_j, ["j       %s", [I_JDST]]),
	(fnc_j, ["jal     %s", [I_JDST]]),
	(fnc_b, [2, "beq     "]),
	(fnc_b, [2, "bne     "]),
	(fnc_b, [1, "blez    "]),
	(fnc_b, [1, "bgtz    "]),
	(fnc_clear, ["addi    %s, %s, %s", I_RT, I_RS, I_IMMS]),
	(fnc_addiu, None), # handle la/li
	(fnc_clear, ["slti    %s, %s, %s", I_RT, I_RS, I_IMMS]),
	(fnc_clear, ["sltiu   %s, %s, %s", I_RT, I_RS, I_IMMS]),
	(fnc_clear, ["andi    %s, %s, %s", I_RT, I_RS, I_IMMU]),
	(fnc_ori, None), # handle li
	(fnc_clear, ["xori    %s, %s, %s", I_RT, I_RS, I_IMMU]),
	(fnc_lui, None), # handle la/li
	(lst_cop0_rs, [I_RS]),
	(lst_cop1_rs, [I_RS]),
	(lst_cop2_rs, [I_RS]),
	None,
	(fnc_b, [2, "beql    "]),
	(fnc_b, [2, "bnel    "]),
	(fnc_b, [1, "blezl   "]),
	(fnc_b, [1, "bgtzl   "]),
	(fnc_clear, ["daddi   %s, %s, %s", I_RT, I_RS, I_IMMS]),
	(fnc_clear, ["daddiu  %s, %s, %s", I_RT, I_RS, I_IMMS]),
	(fnc_ls, ["ldl     ", I_RT]),
	(fnc_ls, ["ldr     ", I_RT]),
	None,
	None,
	None,
	None,
	(fnc_ls, ["lb      ", I_RT]),
	(fnc_ls, ["lh      ", I_RT]),
	(fnc_ls, ["lwl     ", I_RT]),
	(fnc_ls, ["lw      ", I_RT]),
	(fnc_ls, ["lbu     ", I_RT]),
	(fnc_ls, ["lhu     ", I_RT]),
	(fnc_ls, ["lwr     ", I_RT]),
	(fnc_ls, ["lwu     ", I_RT]),
	(fnc_ls, ["sb      ", I_RT]),
	(fnc_ls, ["sh      ", I_RT]),
	(fnc_ls, ["swl     ", I_RT]),
	(fnc_ls, ["sw      ", I_RT]),
	(fnc_ls, ["sdl     ", I_RT]),
	(fnc_ls, ["sdr     ", I_RT]),
	(fnc_ls, ["swr     ", I_RT]),
	(fnc_ls, ["cache   ", I_CACHE]),
	(fnc_ls, ["ll      ", I_RT]),
	(fnc_ls, ["lwc1    ", I_FT]),
	(lst_lwc2, [I_RD]),
	None,
	(fnc_ls, ["lld     ", I_RT]),
	(fnc_ls, ["ldc1    ", I_FT]),
	None,
	(fnc_ls, ["ld      ", I_RT]),
	(fnc_ls, ["sc      ", I_RT]),
	(fnc_ls, ["swc1    ", I_FT]),
	(lst_swc2, [I_RD]),
	None,
	(fnc_ls, ["scd     ", I_RT]),
	(fnc_ls, ["sdc1    ", I_FT]),
	None,
	(fnc_ls, ["sd      ", I_RT]),
]

def init(self, seg, addr):
	global btbl
	ultra.init(self, seg, addr)
	if self.seg not in btbl: btbl[self.seg] = set()

def fmt(self, line):
	f = self.file[-1][1]
	last = None
	for addr, ln in line:
		if addr is not None:
			if last != addr:
				sym = self.get_sym(addr)
				if sym is not None:
					if "LOCAL" not in sym.flag:
						addr_s = addr
						if last is not None: f.append("\n")
						if ultra.COMM_LABEL and hasattr(sym, "fmt"):
							if ultra.COMM_LADDR:
								start = "/* 0x%08X   " % addr
							else:
								start = "/* "
							f.append(sym.fmt(start, " */")+"\n")
						else:
							if ultra.COMM_LADDR:
								f.append("/* 0x%08X */\n" % addr)
					if "GLOBL" in sym.flag: f.append(".globl %s\n" % sym.label)
					f.append("%s:\n" % sym.label)
				elif addr in btbl[self.seg]:
					if mode == 0:   f.append("%d$:\n" % ((addr-addr_s)//4))
					else:           f.append(".L%08X:\n" % addr)
				last = addr
		if ultra.COMM_LINE: f.append("/*%08X*/\t%s\n" % (addr, ln))
		else:               f.append("\t%s\n" % ln)

def s_code_start(self):
	global addr_s
	global reg_table
	global lui_stack
	global lui_table
	global lui_next
	global lui_flag
	addr_s = self.addr
	reg_table = 64*[False]
	lui_stack = {}
	lui_table = 32*[None]
	lui_next  = None
	lui_flag  = 1

def s_code(self, argv):
	global mode
	global macro
	global sep
	global line
	global inst_arg
	global inst_fmt
	global lui_table
	global lui_flag
	global imm
	seg, start, end, mode, macro, sep = argv
	init(self, seg, start)
	gpr  = (gpr_cpu,  gpr_rsp)[mode]
	cop0 = (cop0_cpu, cop0_rsp)[mode]
	line = []
	s_code_start(self)
	while self.addr < end:
		self.save = self.addr
		sym = self.get_sym(self.save)
		if sym is not None and "LOCAL" not in sym.flag: s_code_start(self)
		if self.save in lui_stack: lui_table = lui_stack[self.save][:]
		flag = lui_flag
		inst = self.u32()
		if inst == 0:
			line.append((self.save, "nop"))
		else:
			f0 = inst >> 26 & 0x3F
			f1 = inst >>  0 & 0x3F
			r0 = inst >> 21 & 0x1F
			r1 = inst >> 16 & 0x1F
			r2 = inst >> 11 & 0x1F
			r3 = inst >>  6 & 0x1F
			e0 = inst >> 21 & 0x0F
			e1 = inst >> 11 & 0x0F
			e2 = inst >>  7 & 0x0F
			i0 = (inst >> 0 & 0x7F) - (inst << 1 & 0x80)
			i1 = inst >>  0 & 0xFFFF
			i2 = i1 - (i1 << 1 & 0x10000)
			i3 = inst <<  0 & 0x03FFFFFF
			i4 = inst >>  6 & 0x000FFFFF
			inst_arg = [
				f0, # op
				f1, # func
				r0, # rs
				r1, # rt
				r2, # rd
				r3, # sa
				r1, # cache
				(r1, i4)[mode], # code
				r2, # c0reg
				r2, # c1ctl
				r0, # c1fmt
				r1, # ft
				r2, # fs
				r3, # fd
				r1, # vt
				r2, # vs
				r3, # vd
				e0, # ev
				e1, # de
				e2, # e
				i0, # offs
				i2, # imms
				i1, # immu
				i1 << 16, # immh
				self.addr + (i2 << 2), # bdst
				(self.addr & 0xF0000000) | (i3 << 2), # jdst
			]
			inst_fmt = [
				"", # op
				"", # func
				gpr, # rs
				gpr, # rt
				gpr, # rd
				"%d", # sa
				"0x%02X", # cache
				"%d", # code
				cop0, # c0reg
				cop1_ctl, # c1ctl
				cop1_fmt, # c1fmt
				"$f%d", # ft
				"$f%d", # fs
				"$f%d", # fd
				"$v%d", # vt
				"$v%d", # vs
				"$v%d", # vd
				element_table, # ev
				element_table, # de
				"[%d]", # e
				ultra.fmt_s16, # offs
				ultra.fmt_s16, # imms
				"0x%04X", # immu
				"0x%08X", # immh
				"", # bdst
				"0x%08X", # jdst
			]
			imm = self.get_imm(self.save)
			ln = lst_prc(self, lst_op, [I_OP])
			if ln is not None:
				line.append((self.save, ln))
			else:
				print("warning: illegal opcode 0x%08X:0x%08X" % (
					self.save, inst
				))
				line.append((self.save, (
					".word 0x%08X",
					"nop :: .org .-4 :: .word 0x%08X",
				)[mode] % inst))
		if flag != 1: lui_flag = 1
	fmt(self, line)

def d_fmt(self, argv, x, fmt="%d"):
	return self.fmt(argv[0] if len(argv) > 0 else fmt, x)

d_sbyte = [".byte", lambda self, argv: d_fmt(self, argv, self.s8())]
d_ubyte = [".byte", lambda self, argv: d_fmt(self, argv, self.u8())]
d_shalf = [".half", lambda self, argv: d_fmt(self, argv, self.s16())]
d_uhalf = [".half", lambda self, argv: d_fmt(self, argv, self.u16())]
d_sword = [".word", lambda self, argv: d_fmt(self, argv, self.s32())]
d_uword = [".word", lambda self, argv: d_fmt(self, argv, self.u32())]
d_flagbyte = [".byte", lambda self, argv: self.fmt_flag(argv[0], self.u8())]
d_flaghalf = [".half", lambda self, argv: self.fmt_flag(argv[0], self.u16())]
d_flagword = [".word", lambda self, argv: self.fmt_flag(argv[0], self.u32())]
d_float  = [".float",  lambda self, argv: self.fmt_float(self.f(), "", False)]
d_double = [".double", lambda self, argv: self.fmt_float(self.d(), "", False)]
d_haddr  = [".half",   lambda self, argv: ultra.ah(self, self.save)]
d_waddr  = [".word",   lambda self, argv: ultra.aw(self, self.save)]

def d_align_prc(self, argv):
	x, = argv
	self.addr = (self.addr+x-1) & -x
	return "%d" % x
d_align = [".align", d_align_prc]

def lst_main(self, line, lst):
	for argv in lst:
		for _ in range(argv[0]):
			if type(argv[1]) == list:
				lst_main(self, line, argv[1])
			else:
				self.save = self.addr
				n = argv[1]
				t = argv[2]
				if type(t) == str and t in {"ascii", "asciz"}:
					line.append((self.save, ".%s \"%s\"" % (
						t, "".join([chr(self.u8()) for _ in range(n)])
					)))
					if t == "asciz": self.addr += 1
				else:
					line.append((self.save, "%s %s" % (t[0], ",".join([
						t[1](self, argv[3:]) for _ in range(n)
					]))))

def s_data(self, argv):
	seg, start, end, lst = argv
	init(self, seg, start)
	line = []
	lst_main(self, line, lst)
	fmt(self, line)

def s_definelabel(self, argv):
	seg, = argv
	f = self.file[-1][1]
	mask = tuple(seg.split("."))
	for i in self.meta.sym:
		if mask == tuple(seg.split(".")[:len(mask)]):
			for addr in sorted(self.meta.sym[i].keys()):
				s = sym[addr]
				if "-" in s.label or "+" in s.label: continue
				if "LOCAL" not in s.flag:
					f.append("%s0x%08X\n" % (
						(".definelabel %s, " % s.label).ljust(64), addr
					))

def s_struct_lst(line, prefix, lst):
	for x in lst:
		if type(x) == list:
			off  = x[0]
			name = x[2]
			lst  = x[3]
			pre  = prefix + (name,)
			line.append((off,) + pre)
			s_struct_lst(line, pre, lst)
		else:
			off = x[0]
			sym = x[1]
			line.append((off,) + prefix + (sym.label,))

def s_struct(self, argv):
	tbl, = argv
	f = self.file[-1][1]
	for size, c, name, lst in tbl:
		fmt = ultra.fmt_sizefmt(size)
		line = []
		s_struct_lst(line, (name,), lst)
		line.append((size, "sizeof", name))
		f += [
			("#define %s " % "__".join(x[1:])).ljust(32) + fmt % x[0] + "\n"
			for x in line
			if x[0] is not None
		]
		f.append("\n")

def s_header(self, argv):
	seg, = argv
	ultra.init(self, seg, 0)
	p = self.u32()
	c = self.u32()
	s = self.u32()
	u = self.u32()
	self.addr += 0x30
	self.file[-1][1].append("%08x%08x\n%08x%08x\n" % (p, c, 0, u))
