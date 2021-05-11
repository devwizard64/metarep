import table
import ultra

T_LST   = 0x00
T_FNC   = 0x01
T_STR   = 0x02

I_OP    = 0x00
I_FUNC  = 0x01
I_RS    = 0x02
I_RT    = 0x03
I_RD    = 0x04
I_SA    = 0x05
I_CACHE = 0x06
I_C0REG = 0x07
I_C1CTL = 0x08
I_C1FMT = 0x09
I_FT    = 0x0A
I_FS    = 0x0B
I_FD    = 0x0C
I_VT    = 0x0D
I_VS    = 0x0E
I_VD    = 0x0F
I_IMM   = 0x10
I_IMMS  = 0x11
I_IMMHI = 0x12
I_CODE  = 0x13
I_BDST  = 0x14
I_JDST  = 0x15

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

btbl        = None

line        = None
inst_int    = None
inst_str    = None
reg_table   = None
lui_table   = None
have_imm    = None

def sym(addr, src=None):
    btbl.add(addr)
    if src == None:
        src = ultra.script.c_dst
    sym = table.sym_addr(ultra.script, src, addr, True)
    if sym != None:
        return sym.label
    return ".L%08X" % addr

def aw(src=None):
    return sym(ultra.uw(), src)

def str_prc(ptr, argv):
    argv = tuple([inst_str[arg] for arg in argv])
    if None in argv:
        raise RuntimeError("ultra.asm.str_prc(): bad arg")
    return ptr % argv

def lst_prc(ptr, argv):
    p = ptr[inst_int[argv[0]]]
    if p == None:
        return None
    else:
        t, ptr, argv = p
        if t == T_LST:
            return lst_prc(ptr, argv)
        if t == T_FNC:
            return ptr(argv)
        if t == T_STR:
            return str_prc(ptr, argv)
    raise RuntimeError("ultra.asm.lst_prc(): bad arg")

def fnc_or(argv):
    ptr, argv = ["or      %s, %s, %s", [I_RD, I_RS, I_RT]]
    if mode == 0:
        if inst_int[I_RT] == 0:
            # if inst_int[I_RS] == 0:
            #     if not have_imm:
            #         inst_str[I_IMM] = "0"
            #     ptr, argv = ["li      %s, %s", [I_RD, I_IMM]]
            # else:
                ptr, argv = ["move    %s, %s", [I_RD, I_RS]]
    return str_prc(ptr, argv)

def fnc_j(argv):
    if argv[1][0] == I_JDST:
        jdst = inst_int[I_JDST]
        inst_str[I_JDST] = ultra.sym(jdst)
    return str_prc(argv[0], argv[1])

def fnc_b(argv):
    inst_str[I_BDST] = sym(inst_int[I_BDST])
    cnt, ptr = argv[:2]
    argv = [I_RS, I_RT]
    # regimm
    if inst_int[I_OP] == 0x01:
        # b?z $0
        if inst_int[I_RS] == 0x00:
            # bgezal $0 -> bal
            if inst_int[I_RT] == 0x11:
                cnt, ptr = [0, "bal     "]
            # bgezall $0 -> ball
            elif inst_int[I_RT] == 0x13:
                cnt, ptr = [0, "ball    "]
    # b? rs, $0
    elif inst_int[I_RT] == 0x00:
        # beq
        if inst_int[I_OP] == 0x04:
            # beq $0, $0 -> b
            if inst_int[I_RS] == 0x00:
                cnt, ptr = [0, "b       "]
            # beq rs, $0 -> beqz rs
            else:
                cnt, ptr = [1, "beqz    "]
        # bne rs, $0 -> bnez rs
        elif inst_int[I_OP] == 0x05:
            cnt, ptr = [1, "bnez    "]
        # beql rs, $0 -> beqzl rs
        elif inst_int[I_OP] == 0x14:
            cnt, ptr = [1, "beqzl   "]
        # bnel rs, $0 -> bnezl rs
        elif inst_int[I_OP] == 0x15:
            cnt, ptr = [1, "bnezl   "]
    for i in range(cnt):
        ptr += "%s, "
    return str_prc(ptr + "%s", argv[:cnt] + [I_BDST])

def fnc_addiu(argv):
    ptr, argv = ["addiu   %s, %s, %s", [I_RT, I_RS, I_IMMS]]
    if mode == 0:
        # addiu rt, $0, imm -> li rt, imm
        if inst_int[I_RS] == 0x00 and inst_int[I_IMMS] != 0:
            ptr, argv = ["li      %s, %s", [I_RT, I_IMMS]]
        # lui rt, hi(addr) ... addiu rt, rt, lo(addr)
        elif inst_int[I_RT] == inst_int[I_RS]:
            if lui_table[inst_int[I_RT]] != None:
                ln, immhi = lui_table[inst_int[I_RT]]
                sym = ultra.sym(immhi + inst_int[I_IMMS])
                inst_str[I_IMMS] = "%%hi(%s)" % sym
                line[ln] = (
                    line[ln][0], str_prc("lui     %s, %s", [I_RT, I_IMMS])
                )
                inst_str[I_IMMS] = "%%lo(%s)" % sym
                ptr, argv = ["addiu   %s, %s, %s", [I_RT, I_RT, I_IMMS]]
        lui_table[inst_int[I_RT]] = None
    else:
        # if inst_int[I_RS] == 0x00:
        #     inst_str[I_IMM] = ultra.sym(inst_int[I_IMM])
        #     ptr, argv = ["la      %s, %s", [I_RT, I_IMM]]
        pass
    return str_prc(ptr, argv)

def fnc_ori(argv):
    ptr, argv = ["ori     %s, %s, %s", [I_RT, I_RS, I_IMM]]
    if inst_int[I_RS] == 0x00:
        if mode == 0:
            # ori rt, $0, imm -> li rt, imm
            if inst_int[I_IMM] >= 0x8000:
                ptr, argv = ["li      %s, %s", [I_RT, I_IMM]]
        else:
            # ori rt, rs, 0 -> move rt, rs
            # if inst_int[I_IMM] == 0:
            #     ptr, argv = ["move    %s, %s", [I_RT, I_RS]]
            pass
    # lui rt, imm ... ori rt, rt, imm -> li.u rt, imm ... li.l rt, imm
    elif inst_int[I_RT] == inst_int[I_RS]:
        if lui_table[inst_int[I_RT]] != None:
            ln, immhi = lui_table[inst_int[I_RT]]
            if not have_imm:
                inst_str[I_IMM] = "0x%08X" % (immhi | inst_int[I_IMM])
                line[ln] = (
                    line[ln][0], str_prc("lui     %s, %s >> 16", [I_RT, I_IMM])
                )
                ptr, argv = ["ori     %s, %s, %s & 0xFFFF", [I_RT, I_RT, I_IMM]]
    lui_table[inst_int[I_RT]] = None
    return str_prc(ptr, argv)

def fnc_lui(argv):
    if inst_int[I_RT] != 0x00:
        lui_table[inst_int[I_RT]] = (len(line), inst_int[I_IMMHI])
    if have_imm:
        ptr, argv = "lui     %s, %s", [I_RT, I_IMM]
    else:
        ptr, argv = "li      %s, %s", [I_RT, I_IMMHI]
    return str_prc(ptr, argv)

def fnc_ls(argv):
    ptr, argv = [argv[0], [argv[1], I_IMMS, I_RS]]
    if mode == 0:
        if lui_table[inst_int[I_RS]] != None:
            ln, immhi = lui_table[inst_int[I_RS]]
            sym = ultra.sym(immhi + inst_int[I_IMMS])
            inst_str[I_IMMS] = "%%hi(%s)" % sym
            line[ln] = (
                line[ln][0], str_prc("lui     %s, %s", [I_RS, I_IMMS])
            )
            inst_str[I_IMMS] = "%%lo(%s)" % sym
        if ptr in (
            "lb      ",
            "lh      ",
            "lwl     ",
            "lw      ",
            "lbu     ",
            "lhu     ",
            "lwr     ",
            "lwu     ",
        ):
            lui_table[inst_int[argv[0]]] = None
    else:
        pass
    ptr += "%s, %s(%s)"
    return str_prc(ptr, argv)

lst_special = [
    (T_STR, "sll     %s, %s, %s", [I_RD, I_RT, I_SA]),
    None,
    (T_STR, "srl     %s, %s, %s", [I_RD, I_RT, I_SA]),
    (T_STR, "sra     %s, %s, %s", [I_RD, I_RT, I_SA]),
    (T_STR, "sllv    %s, %s, %s", [I_RD, I_RT, I_RS]),
    None,
    (T_STR, "srlv    %s, %s, %s", [I_RD, I_RT, I_RS]),
    (T_STR, "srav    %s, %s, %s", [I_RD, I_RT, I_RS]),
    (T_FNC, fnc_j, ["jr      %s", [I_RS]]),
    (T_FNC, fnc_j, ["jalr    %s", [I_RS]]),
    None,
    None,
    (T_STR, "syscall %s", [I_CODE]),
    (T_STR, "break   %s", [I_CODE]),
    None,
    (T_STR, "sync", []),
    (T_STR, "mfhi    %s", [I_RD]),
    (T_STR, "mthi    %s", [I_RS]),
    (T_STR, "mflo    %s", [I_RD]),
    (T_STR, "mtlo    %s", [I_RS]),
    (T_STR, "dsllv   %s, %s, %s", [I_RD, I_RT, I_RS]),
    None,
    (T_STR, "dsrlv   %s, %s, %s", [I_RD, I_RT, I_RS]),
    (T_STR, "dsrav   %s, %s, %s", [I_RD, I_RT, I_RS]),
    (T_STR, "mult    %s, %s", [I_RS, I_RT]),
    (T_STR, "multu   %s, %s", [I_RS, I_RT]),
    (T_STR, "div     %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "divu    %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "dmult   %s, %s", [I_RS, I_RT]),
    (T_STR, "dmultu  %s, %s", [I_RS, I_RT]),
    (T_STR, "ddiv    %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "ddivu   %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "add     %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "addu    %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "sub     %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "subu    %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "and     %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_FNC, fnc_or, None),
    (T_STR, "xor     %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "nor     %s, %s, %s", [I_RD, I_RS, I_RT]),
    None,
    None,
    (T_STR, "slt     %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "sltu    %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "dadd    %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "daddu   %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "dsub    %s, %s, %s", [I_RD, I_RS, I_RT]),
    (T_STR, "dsubu   %s, %s, %s", [I_RD, I_RS, I_RT]),
    None, # tge
    None, # tgeu
    None, # tlt
    None, # tltu
    None, # teq
    None,
    None, # tne
    None,
    (T_STR, "dsll    %s, %s, %s", [I_RD, I_RT, I_SA]),
    None,
    (T_STR, "dsrl    %s, %s, %s", [I_RD, I_RT, I_SA]),
    (T_STR, "dsra    %s, %s, %s", [I_RD, I_RT, I_SA]),
    (T_STR, "dsll32  %s, %s, %s", [I_RD, I_RT, I_SA]),
    None,
    (T_STR, "dsrl32  %s, %s, %s", [I_RD, I_RT, I_SA]),
    (T_STR, "dsra32  %s, %s, %s", [I_RD, I_RT, I_SA]),
]

lst_regimm = [
    (T_FNC, fnc_b, [1, "bltz    "]),
    (T_FNC, fnc_b, [1, "bgez    "]),
    (T_FNC, fnc_b, [1, "bltzl   "]),
    (T_FNC, fnc_b, [1, "bgezl   "]),
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
    (T_FNC, fnc_b, [1, "bltzal  "]),
    (T_FNC, fnc_b, [1, "bgezal  "]),
    (T_FNC, fnc_b, [1, "bltzall "]),
    (T_FNC, fnc_b, [1, "bgezall "]),
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
    (T_STR, "tlbr", []),
    (T_STR, "tlbwi", []),
    None,
    None,
    None,
    (T_STR, "tlbwr", []),
    None,
    (T_STR, "tlbp", []),
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
    (T_STR, "eret", []),
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
    (T_STR, "mfc0    %s, %s", [I_RT, I_C0REG]),
    (T_STR, "dmfc0   %s, %s", [I_RT, I_C0REG]),
    None, # (T_STR, "cfc0    %s, %s", [I_RT, I_C0CTL]),
    None,
    (T_STR, "mtc0    %s, %s", [I_RT, I_C0REG]),
    (T_STR, "dmtc0   %s, %s", [I_RT, I_C0REG]),
    None, # (T_STR, "ctc0    %s, %s", [I_RT, I_C0CTL]),
    None,
    None, # (T_LST, lst_bc0, [I_RT]),
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    (T_LST, lst_cop0_func, [I_FUNC]),
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
    (T_FNC, fnc_b, [0, "bc1f    "]),
    (T_FNC, fnc_b, [0, "bc1t    "]),
    (T_FNC, fnc_b, [0, "bc1fl   "]),
    (T_FNC, fnc_b, [0, "bc1tl   "]),
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
    (T_STR, "add.%s   %s, %s, %s", [I_C1FMT, I_FD, I_FS, I_FT]),
    (T_STR, "sub.%s   %s, %s, %s", [I_C1FMT, I_FD, I_FS, I_FT]),
    (T_STR, "mul.%s   %s, %s, %s", [I_C1FMT, I_FD, I_FS, I_FT]),
    (T_STR, "div.%s   %s, %s, %s", [I_C1FMT, I_FD, I_FS, I_FT]),
    (T_STR, "sqrt.%s  %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "abs.%s   %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "mov.%s   %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "neg.%s   %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "round.l.%s %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "trunc.l.%s %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "ceil.l.%s %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "floor.l.%s %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "round.w.%s %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "trunc.w.%s %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "ceil.w.%s %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "floor.w.%s %s, %s", [I_C1FMT, I_FD, I_FS]),
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
    (T_STR, "cvt.s.%s %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "cvt.d.%s %s, %s", [I_C1FMT, I_FD, I_FS]),
    None,
    None,
    (T_STR, "cvt.w.%s %s, %s", [I_C1FMT, I_FD, I_FS]),
    (T_STR, "cvt.l.%s %s, %s", [I_C1FMT, I_FD, I_FS]),
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
    (T_STR, "c.f.%s   %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.un.%s  %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.eq.%s  %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.ueq.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.olt.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.ult.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.ole.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.ule.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.sf.%s  %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.ngle.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.seq.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.ngl.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.lt.%s  %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.nge.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.le.%s  %s, %s", [I_C1FMT, I_FS, I_FT]),
    (T_STR, "c.ngt.%s %s, %s", [I_C1FMT, I_FS, I_FT]),
]

lst_cop1_rs = [
    (T_STR, "mfc1    %s, %s", [I_RT, I_FS]),
    (T_STR, "dmfc1   %s, %s", [I_RT, I_FS]),
    (T_STR, "cfc1    %s, %s", [I_RT, I_C1CTL]),
    None,
    (T_STR, "mtc1    %s, %s", [I_RT, I_FS]),
    (T_STR, "dmtc1   %s, %s", [I_RT, I_FS]),
    (T_STR, "ctc1    %s, %s", [I_RT, I_C1CTL]),
    None,
    (T_LST, lst_bc1, [I_RT]),
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    (T_LST, lst_cop1_func, [I_FUNC]),
    (T_LST, lst_cop1_func, [I_FUNC]),
    None,
    None,
    (T_LST, lst_cop1_func, [I_FUNC]),
    (T_LST, lst_cop1_func, [I_FUNC]),
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

lst_cop2_rs = [
    None, # mfc2
    None,
    (T_STR, "cfc2    %s, %s", [I_RT, I_RD]),
    None,
    None, # mtc2
    None,
    (T_STR, "ctc2    %s, %s", [I_RT, I_RD]),
    None,
    None, # 08
    None, # 09
    None, # 0A
    None, # 0B
    None, # 0C
    None, # 0D
    None, # 0E
    None, # 0F
    None, # 10
    None, # 11
    None, # 12
    None, # 13
    None, # 14
    None, # 15
    None, # 16
    None, # 17
    None, # 18
    None, # 19
    None, # 1A
    None, # 1B
    None, # 1C
    None, # 1D
    None, # 1E
    None, # 1F
]

lst_lwc2 = [
]

lst_swc2 = [
]

lst_op = [
    (T_LST, lst_special, [I_FUNC]),
    (T_LST, lst_regimm, [I_RT]),
    (T_FNC, fnc_j, ["j       %s", [I_JDST]]),
    (T_FNC, fnc_j, ["jal     %s", [I_JDST]]),
    (T_FNC, fnc_b, [2, "beq     "]),
    (T_FNC, fnc_b, [2, "bne     "]),
    (T_FNC, fnc_b, [1, "blez    "]),
    (T_FNC, fnc_b, [1, "bgtz    "]),
    (T_STR, "addi    %s, %s, %s", [I_RT, I_RS, I_IMMS]),
    (T_FNC, fnc_addiu, None), # handle la/li
    (T_STR, "slti    %s, %s, %s", [I_RT, I_RS, I_IMMS]),
    (T_STR, "sltiu   %s, %s, %s", [I_RT, I_RS, I_IMMS]),
    (T_STR, "andi    %s, %s, %s", [I_RT, I_RS, I_IMM]),
    (T_FNC, fnc_ori, None), # handle li
    (T_STR, "xori    %s, %s, %s", [I_RT, I_RS, I_IMM]),
    (T_FNC, fnc_lui, None), # handle la/li
    (T_LST, lst_cop0_rs, [I_RS]),
    (T_LST, lst_cop1_rs, [I_RS]),
    (T_LST, lst_cop2_rs, [I_RS]),
    None,
    (T_FNC, fnc_b, [2, "beql    "]),
    (T_FNC, fnc_b, [2, "bnel    "]),
    (T_FNC, fnc_b, [1, "blezl   "]),
    (T_FNC, fnc_b, [1, "bgtzl   "]),
    (T_STR, "daddi   %s, %s, %s", [I_RT, I_RS, I_IMMS]),
    (T_STR, "daddiu  %s, %s, %s", [I_RT, I_RS, I_IMMS]),
    (T_FNC, fnc_ls, ["ldl     ", I_RT]),
    (T_FNC, fnc_ls, ["ldr     ", I_RT]),
    None,
    None,
    None,
    None,
    (T_FNC, fnc_ls, ["lb      ", I_RT]),
    (T_FNC, fnc_ls, ["lh      ", I_RT]),
    (T_FNC, fnc_ls, ["lwl     ", I_RT]),
    (T_FNC, fnc_ls, ["lw      ", I_RT]),
    (T_FNC, fnc_ls, ["lbu     ", I_RT]),
    (T_FNC, fnc_ls, ["lhu     ", I_RT]),
    (T_FNC, fnc_ls, ["lwr     ", I_RT]),
    (T_FNC, fnc_ls, ["lwu     ", I_RT]),
    (T_FNC, fnc_ls, ["sb      ", I_RT]),
    (T_FNC, fnc_ls, ["sh      ", I_RT]),
    (T_FNC, fnc_ls, ["swl     ", I_RT]),
    (T_FNC, fnc_ls, ["sw      ", I_RT]),
    (T_FNC, fnc_ls, ["sdl     ", I_RT]),
    (T_FNC, fnc_ls, ["sdr     ", I_RT]),
    (T_FNC, fnc_ls, ["swr     ", I_RT]),
    (T_FNC, fnc_ls, ["cache   ", I_CACHE]),
    (T_FNC, fnc_ls, ["ll      ", I_RT]),
    (T_FNC, fnc_ls, ["lwc1    ", I_FT]),
    None, # (T_LST, lst_lwc2, [I_RD]),
    None,
    (T_FNC, fnc_ls, ["lld     ", I_RT]),
    (T_FNC, fnc_ls, ["ldc1    ", I_FT]),
    None,
    (T_FNC, fnc_ls, ["ld      ", I_RT]),
    (T_FNC, fnc_ls, ["sc      ", I_RT]),
    (T_FNC, fnc_ls, ["swc1    ", I_FT]),
    None, # (T_LST, lst_swc2, [I_RD]),
    None,
    (T_FNC, fnc_ls, ["scd     ", I_RT]),
    (T_FNC, fnc_ls, ["sdc1    ", I_FT]),
    None,
    (T_FNC, fnc_ls, ["sd      ", I_RT]),
]

def init(self, start, data):
    global btbl
    ultra.init(self, start, data)
    btbl = set()

def fmt(self, line, code=False):
    f = self.file[-1][1]
    last = None
    for addr, ln in line:
        if addr != None:
            if last != addr:
                sym = table.sym_addr(self, addr, addr, True)
                if sym != None:
                    if not sym.label.startswith("L80"):
                        f.append("\n")
                        if hasattr(sym, "fmt"):
                            f.append(sym.fmt("/* 0x%08X   " % addr, " */")+"\n")
                        else:
                            f.append("/* 0x%08X */\n" % addr)
                    if sym.flag & table.GLOBL:
                        f.append(".globl %s\n" % sym.label)
                    f.append("%s:\n" % sym.label)
                elif addr in btbl:
                    f.append(".L%08X:\n" % addr)
                last = addr
        if code:
            f.append("/*0x%08X*/  %s\n" % (addr, ln))
        else:
            f.append("\t%s\n" % ln)

def s_code(self, argv):
    global mode
    global sep
    global line
    global inst_int
    global inst_str
    global reg_table
    global lui_table
    global have_imm
    start, end, data, mode, sep = argv
    init(self, start, data)
    gpr  = (gpr_cpu,  gpr_rsp)[mode]
    cop0 = (cop0_cpu, cop0_rsp)[mode]
    line = []
    reg_table = 64*[False]
    lui_table = 32*[None]
    while self.c_addr < end:
        self.c_push()
        inst = ultra.uw()
        if inst == 0:
            line.append((self.c_dst, "nop"))
        else:
            f0 = inst >> 26 & 0x3F
            r0 = inst >> 21 & 0x1F
            r1 = inst >> 16 & 0x1F
            r2 = inst >> 11 & 0x1F
            r3 = inst >>  6 & 0x1F
            f1 = inst >>  0 & 0x3F
            i0 = inst >>  0 & 0xFFFF
            i1 = i0 - (i0 << 1 & 0x10000)
            i2 = i0 << 16
            i3 = inst >>  0 & 0x03FFFFFF
            i4 = inst >>  6 & 0x000FFFFF
            inst_int = [
                f0, # op
                f1, # func
                r0, # rs
                r1, # rt
                r2, # rd
                r3, # sa
                r1, # cache
                r2, # c0 reg
                r2, # c1 ctl
                r0, # c1 fmt
                r1, # ft
                r2, # fs
                r3, # fd
                r1, # vt
                r2, # vs
                r3, # vd
                i0, # imm
                i1, # imms
                i2, # immhi
                (r1, i4)[mode], # code
                self.c_addr + (i1 << 2), # bdst
                (self.c_addr & 0xF0000000) | (i3 << 2), # jdst
            ]
            inst_str = [
                "", # op
                "", # func
                gpr[r0], # rs
                gpr[r1], # rt
                gpr[r2], # rd
                "%d" % r3, # sa
                "0x%02X" % r1, # cache
                cop0[r2], # c0
                cop1_ctl[r2], # c1 ctl
                cop1_fmt[r0], # c1 fmt
                "$f%d" % r1, # ft
                "$f%d" % r2, # fs
                "$f%d" % r3, # fd
                "$v%d" % r1, # vt
                "$v%d" % r2, # vs
                "$v%d" % r3, # vd
                "0x%04X" % inst_int[I_IMM], # imm
                "-0x%04X" % -i1 if i1 < 0 else "0x%04X" % i1, # imms
                "0x%08X" % inst_int[I_IMMHI], # immhi
                "%d" % inst_int[I_CODE], # code
                ".L%08X" % inst_int[I_BDST], # bdst
                "0x%08X" % inst_int[I_JDST], # jdst
            ]
            imm = table.imm_addr(self, self.c_dst, self.c_dst)
            have_imm = imm != None
            if have_imm:
                inst_str[I_SA]    = imm
                inst_str[I_CACHE] = imm
                inst_str[I_IMM]   = imm
                inst_str[I_IMMS]  = imm
                inst_str[I_IMMHI] = imm
                inst_str[I_CODE]  = imm
            ln = lst_prc(lst_op, [I_OP])
            if ln != None:
                line.append((self.c_dst, ln))
            else:
                # print("warning: illegal opcode 0x%08X:0x%08X" % (
                #     self.c_dst, inst
                # ))
                line.append((
                    self.c_dst, "nop :: .org .-4 :: .word 0x%08X" % inst
                ))
    fmt(self, line, True)

d_byte    = [".db", lambda: "0x%02X" % ultra.ub()]
d_sbyte   = [".db", lambda: "%d"     % ultra.sb()]
d_ubyte   = [".db", lambda: "%d"     % ultra.ub()]
d_half    = [".dh", lambda: "0x%04X" % ultra.uh()]
d_shalf   = [".dh", lambda: "%d"     % ultra.sh()]
d_uhalf   = [".dh", lambda: "%d"     % ultra.uh()]
d_word    = [".dw", lambda: "0x%08X" % ultra.uw()]
d_sword   = [".dw", lambda: "%d"     % ultra.sw()]
d_uword   = [".dw", lambda: "%d"     % ultra.uw()]
d_addr    = [".dh", lambda: ultra.ah()]

def lst_main(self, line, lst):
    for argv in lst:
        for _ in range(argv[0]):
            if type(argv[1]) == list:
                lst_main(self, line, argv[1])
            else:
                self.c_push()
                n = argv[1]
                t = argv[2]
                if type(t) == str and t in {"ascii", "asciiz"}:
                    line.append((self.c_dst, ".%s \"%s\"" % (
                        t, "".join([chr(ultra.ub()) for _ in range(n)])
                    )))
                else:
                    line.append((self.c_dst, "%s %s" % (
                        t[0], ", ".join([t[1]() for _ in range(n)])
                    )))

def s_data(self, argv):
    start, end, data, lst = argv
    init(self, start, data)
    line = []
    lst_main(self, line, lst)
    fmt(self, line)

def s_header(self, argv):
    data, = argv
    ultra.init(self, 0, data)
    p0 = ultra.ub()
    p1 = ultra.ub()
    p2 = ultra.ub()
    p3 = ultra.ub()
    c  = ultra.uw()
    start = ultra.aw()
    self.c_addr += 2
    u0 = ultra.ub()
    u1 = ultra.ub()
    self.c_addr += 16
    label = self.c_next(20).decode("shift-jis")
    self.c_addr += 7
    m  = ultra.ub()
    i0 = ultra.ub()
    i1 = ultra.ub()
    r  = ultra.ub()
    v  = ultra.ub()
    self.file[-1][1].append((
        ".byte 0x%02X, 0x%02X, 0x%02X, 0x%02X\n"
        ".word 0x%08X\n"
        ".word %s\n"
        ".byte 0, 0, %d, '%c'\n"
        ".word 0, 0, 0, 0\n"
        ".ascii \"%s\"\n"
        ".fill 7\n"
        ".ascii \"%c\"\n"
        ".ascii \"%c%c\"\n"
        ".ascii \"%c\"\n"
        ".byte %d\n"
    ) % (p0, p1, p2, p3, c, start, u0, u1, label, m, i0, i1, r, v))
