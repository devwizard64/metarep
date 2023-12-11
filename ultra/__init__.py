import struct

A_EXTERN    = 1 << 0
A_ADDR      = 1 << 1
A_CAST      = 1 << 2
A_ARRAY     = 1 << 3

COMM_EADDR  = False
COMM_VADDR  = False
COMM_LADDR  = False
COMM_LABEL  = False
COMM_LINE   = False

fmt_bool = ["FALSE", "TRUE"]

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

fmt_OSTask_flags    = lambda self, x: self.fmt_flag(flag_OSTask_flags, x)
fmt_sp_sr           = lambda self, x: self.fmt_flag(flag_sp_sr, x)
fmt_sp_sw           = lambda self, x: self.fmt_flag(flag_sp_sw, x)
fmt_dpc_sr          = lambda self, x: self.fmt_flag(flag_dpc_sr, x)

def fmt_s16(self, x):
	return "-0x%04X" % -x if x < 0 else "0x%04X" % x

def fmt_f32(self, x):
	return self.fmt_float(x, "F")

def fmt_f64(self, x):
	return self.fmt_float(x)

def fmt_addr(self, x, extern=False, addr=False, cast=None, array=None):
	s = sym(
		self,
		array[0] if array is not None else x,
		None,
		"(void *)0x%08X",
		extern
	)
	if not s.startswith("(void *)0x") and s != "NULL":
		if addr:                s = "&" + s
		if cast is not None:    s = "(%s)%s" % (cast, s)
		if array is not None:   s = "%s[%d]" % (s, (x-array[0]) // array[1])
	return s

def fmt_sizefmt(size):
	return "0x%%0%dX" % max(2, (size.bit_length()+3)//4)

def sym(self, addr, src=None, fmt="0x%08X", extern=False):
	if addr == 0: return "NULL"
	sym = self.find_sym(addr, src)
	if sym is not None:
		if extern and hasattr(sym, "fmt"): c.extern.add((addr, sym))
		return sym.label
	return fmt % addr

def sym_rsp(self, addr, src=None, fmt="0x%03X"):
	sym = self.find_sym(0x04000000 | addr, src)
	if sym is not None: return sym.label
	return fmt % addr

def ah(self, src=None):
	return sym_rsp(self, self.u16(), src)

def aw(self, src=None, extern=False):
	return sym(self, self.u32(), src, extern=extern)

def init(self, seg, addr):
	self.c_init(">", seg, addr)

import ultra.asm
import ultra.c
