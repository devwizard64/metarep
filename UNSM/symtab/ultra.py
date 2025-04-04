import main
import ultra

sym_globl = {
	# os/parameters.s
	0x80000300: main.sym("osTvType"),
	0x80000304: main.sym("osRomType"),
	0x80000308: main.sym("osRomBase"),
	0x8000030C: main.sym("osResetType"),
	0x80000310: main.sym("osCicId"),
	0x80000314: main.sym("osVersion"),
	0x80000318: main.sym("osMemSize"),
	0x8000031C: main.sym("osAppNMIBuffer"),
}

sym_IPL3_6102 = {
	# Boot.s
	# bulk_rom
	# cart_rom
	# clear_rsp
	# clear_in_mask
	0xA4000040: main.sym("IPL3"),
	0xA400009C: main.sym("wait_rac", flag={"LOCAL"}),
	0xA40000C0: main.sym("wait_rac1", flag={"LOCAL"}),
	0xA40000DC: main.sym("wait_rdram", flag={"LOCAL"}),
	0xA4000160: main.sym("rcp2", flag={"LOCAL"}),
	0xA4000168: main.sym("loop1", flag={"LOCAL"}),
	0xA40001E0: main.sym("SM", flag={"LOCAL"}),
	0xA40001E8: main.sym("LM", flag={"LOCAL"}),
	0xA4000230: main.sym("toshiba", flag={"LOCAL"}),
	0xA400023C: main.sym("done_manufacture", flag={"LOCAL"}),
	0xA400025C: main.sym("done_loop1", flag={"LOCAL"}),
	0xA4000274: main.sym("loop2", flag={"LOCAL"}),
	0xA40002D8: main.sym("HM", flag={"LOCAL"}),
	0xA400035C: main.sym("done_loop2", flag={"LOCAL"}),
	0xA40003D8: main.sym("init_icache", flag={"LOCAL"}),
	0xA40003F8: main.sym("init_dcache", flag={"LOCAL"}),
	0xA4000410: main.sym("nmi", flag={"LOCAL"}),
	0xA4000428: main.sym("ninit_icache", flag={"LOCAL"}),
	0xA4000448: main.sym("ninit_dcache", flag={"LOCAL"}),
	0xA4000458: main.sym("load_ipl3", flag={"LOCAL"}),
	0xA4000498: main.sym("send2", flag={"LOCAL"}),
	0xA40004C0: main.sym("block17s", flag={"LOCAL"}),
	0xA40004C4: main.sym("cart", flag={"LOCAL"}),
	0xA40004DC: main.sym("waitread", flag={"LOCAL"}),
	0xA4000514: main.sym("waitdma", flag={"LOCAL"}),
	0xA40006BC: main.sym("skip", flag={"LOCAL"}),
	0xA4000728: main.sym("rom", flag={"LOCAL"}),
	# 0xA4000730: main.sym("1", flag={"LOCAL"}),
	0xA4000740: main.sym("del_dmem", flag={"LOCAL"}),
	0xA4000758: main.sym("del_imem", flag={"LOCAL"}),
	0xA4000768: main.sym("game", flag={"LOCAL"}),
	0xA4000774: main.sym("pifipl3e", flag={"LOCAL"}),
	0xA4000778: main.sym("InitCCValue"),
	0xA40007EC: main.sym("CCloop1"),
	0xA4000880: main.sym("FindCC"),
	0xA4000894: main.sym("prepass_loop", flag={"LOCAL"}),
	0xA40008C8: main.sym("next_pass", flag={"LOCAL"}),
	0xA40008F8: main.sym("done_findcc", flag={"LOCAL"}),
	0xA40008FC: main.sym("return_findcc", flag={"LOCAL"}),
	0xA400090C: main.sym("TestCCValue"),
	0xA4000924: main.sym("jloop", flag={"LOCAL"}),
	0xA4000940: main.sym("kloop", flag={"LOCAL"}),
	0xA4000950: main.sym("no_passcount", flag={"LOCAL"}),
	0xA4000980: main.sym("ConvertManualToAuto"),
	0xA40009A0: main.sym("big_loop", flag={"LOCAL"}),
	0xA40009B4: main.sym("coverloop", flag={"LOCAL"}),
	0xA40009F4: main.sym("pos", flag={"LOCAL"}),
	0xA4000A08: main.sym("compare_done", flag={"LOCAL"}),
	0xA4000A28: main.sym("return_value", flag={"LOCAL"}),
	0xA4000A30: main.sym("convert_done", flag={"LOCAL"}),
	0xA4000A40: main.sym("WriteCC"),
	0xA4000A64: main.sym("non_auto", flag={"LOCAL"}),
	0xA4000AC0: main.sym("write_done", flag={"LOCAL"}),
	0xA4000AD0: main.sym("ReadCC"),
}

sym_D_rspboot_text = {
	0x0400100C: main.sym("boot"),
	0x04001024: main.sym("@@dmabusy", flag={"LOCAL"}),
	0x04001040: main.sym("yield_check"),
	0x04001054: main.sym("@@yield", flag={"LOCAL"}),
	0x04001068: main.sym("main"),
	0x04001090: main.sym("@@nodpwait", flag={"LOCAL"}),
	0x0400109C: main.sym("@@dmafull", flag={"LOCAL"}),
	0x040010B4: main.sym("@@dmabusy", flag={"LOCAL"}),
}

def fmt_size(self, x):
	return "0x%04X-1" % (x+1 & 0xFFFF)

imm_D_rspboot_text = {
	0x04001000: ("%d",),
	0x04001008: ("os_task",),
	0x0400100C: (ultra.fmt_struct_OSTask,),
	0x04001010: (fmt_size,),
	0x04001044: (ultra.fmt_sp_sr,),
	0x04001058: (ultra.fmt_sp_sw,),
	0x04001068: (ultra.fmt_struct_OSTask,),
	0x0400106C: (ultra.fmt_OSTask_flags,),
	0x04001084: (ultra.fmt_dpc_sr,),
	0x04001090: (ultra.fmt_struct_OSTask,),
	0x04001094: (ultra.fmt_struct_OSTask,),
	0x04001098: ("%d",),
}

sym_D_gspFast3D_fifo_text = {
	0x04001000: main.sym("_04001000"),
	0x04001058: main.sym("cmd_proc"),
	0x04001060: main.sym(".cmd_proc", flag={"LOCAL"}),
	0x0400109C: main.sym(".cmd_nodma", flag={"LOCAL"}),
	0x040010A8: main.sym("cmd_next"),
	0x040010B8: main.sym("cmd_cont"),
	0x040010C8: main.sym("task_exit"),
	0x040010CC: main.sym(".task_yield", flag={"LOCAL"}),
	0x040010D4: main.sym("cmd_load"),
	0x040010F8: main.sym("prg_load"),
	0x040010FC: main.sym("prg_jump"),
	0x0400111C: main.sym("segment_to_physical"),
	0x0400113C: main.sym("dma_start"),
	0x0400115C: main.sym("@@write", flag={"LOCAL"}),
	0x04001164: main.sym("dma_sync"),
	0x04001178: main.sym("rdp_write"),
	0x04001198: main.sym("@@syncready", flag={"LOCAL"}),
	0x040011A4: main.sym("@@syncwrap", flag={"LOCAL"}),
	0x040011B8: main.sym("@@syncfit", flag={"LOCAL"}),
	0x040011D4: main.sym("@@write", flag={"LOCAL"}),
	0x040011F4: main.sym("@@end", flag={"LOCAL"}),
	0x040011FC: main.sym("case_IMM"),
	0x0400120C: main.sym("case_G_TRI1"),
	0x04001250: main.sym("case_G_POPMTX"),
	0x04001288: main.sym("case_G_MOVEWORD"),
	0x040012A0: main.sym("case_G_TEXTURE"),
	0x040012C4: main.sym("case_G_SETOTHERMODE_H"),
	0x040012CC: main.sym("case_G_SETOTHERMODE_L"),
	0x040012D0: main.sym(".setothermode", flag={"LOCAL"}),
	0x0400130C: main.sym("case_G_CULLDL"),
	0x04001314: main.sym("@@loop", flag={"LOCAL"}),
	0x04001328: main.sym("case_G_ENDDL"),
	0x04001348: main.sym("case_G_SETGEOMETRYMODE"),
	0x04001358: main.sym("case_G_CLEARGEOMETRYMODE"),
	0x04001370: main.sym("case_G_PERSPNORM"),
	0x04001378: main.sym("case_G_RDPHALF_1"),
	0x04001380: main.sym("case_G_RDPHALF_CONT"),
	0x04001384: main.sym("case_G_RDPHALF_2"),
	0x0400138C: main.sym("case_RDP"),
	0x040013A8: main.sym("rdp_cmd"),
	0x040013C4: main.sym("case_DMA"),
	0x040013DC: main.sym("case_G_MTX"),
	0x04001420: main.sym(".L04001420", flag={"LOCAL"}),
	0x04001438: main.sym(".L04001438", flag={"LOCAL"}),
	0x04001444: main.sym("_04001444"),
	0x04001484: main.sym("_04001484"),
	0x040014E8: main.sym("_040014E8"),
	0x04001510: main.sym("_04001510"),
	0x04001524: main.sym("_04001524"),
	0x04001558: main.sym("case_G_MOVEMEM"),
	0x04001568: main.sym("case_G_VTX"),
	0x040015E4: main.sym(".light_return", flag={"LOCAL"}),
	0x040015E8: main.sym(".vtx_clip_return", flag={"LOCAL"}),
	0x04001734: main.sym("case_G_DL"),
	0x04001754: main.sym("@@nopush", flag={"LOCAL"}),

	0x04001768: main.sym("@clip"),
	0x04001774: main.sym("@light"),

	0x04001780: main.sym("init"),
	0x040017E4: main.sym("@@initfifo", flag={"LOCAL"}),
	0x04001800: main.sym("@@noinitfifo", flag={"LOCAL"}),
	0x04001870: main.sym("@@fromyield", flag={"LOCAL"}),
	0x04001998: main.sym("rdp_tri"),
	0x040019C4: main.sym(".clip_return", flag={"LOCAL"}),
	0x04001A30: main.sym(".L04001A30", flag={"LOCAL"}),
}

imm_D_gspFast3D_fifo_text = {
	0x04001200: ("lo(IMMTAB_END-2*0x40)",),
	0x04001328: ("DLINDEX-STATE",),
	0x0400133C: ("DLINDEX-STATE",),
	0x04001738: ("DLINDEX-STATE",),
	0x04001750: ("DLINDEX-STATE",),
}

sym_D_gspFast3D_fifo_text_clip = {
	0x040010FC: main.sym("prg_jump"),
	0x040015E8: main.sym(".vtx_clip_return", flag={"LOCAL"}),
	0x04001768: main.sym("@clip"),
	0x04001774: main.sym("@light"),

	0x04001784: main.sym("clip"),
	0x040017A0: main.sym("ProcClipNext"),
	0x040017BC: main.sym("ProcClipI"),
	0x040017C0: main.sym("ProcClipO"),
	0x040017D4: main.sym(".L040017D4", flag={"LOCAL"}),
	0x04001818: main.sym("ProcClipFI"),
	0x0400182C: main.sym("ProcClipFO"),
	0x04001964: main.sym("ProcClipDraw"),
	0x04001804: main.sym(".L04001804_clip", flag={"LOCAL"}),
	0x04001980: main.sym("_04001980"),

	0x040019C4: main.sym(".clip_return", flag={"LOCAL"}),
}

imm_D_gspFast3D_fifo_text_clip = {
	0x04001808: ("lo(CLIPTAB)",),
}

sym_D_gspFast3D_fifo_text_light = {
	0x040010FC: main.sym("prg_jump"),
	0x040015E4: main.sym(".light_return", flag={"LOCAL"}),
	0x04001768: main.sym("@clip"),
	0x04001774: main.sym("light"),

	0x04001804: main.sym(".L04001804_light", flag={"LOCAL"}),
}

sym_D_gspFast3D_fifo_text_exit = {
	0x04001768: main.sym("@yield"),
	0x04001770: main.sym("exit"),
	0x04001788: main.sym("yield"),
}

def fmt_u16(self, x):
	return "0x%04X" % (x & 0xFFFF)

imm_D_gspFast3D_fifo_text_exit = {
	0x040017C8: (fmt_u16,),
}

sym_D_gspFast3D_fifo_data = {
	0x04001000: main.sym("prg_main_start"),
	0x04001080: main.sym("prg_init_start"),
	0x04001768: main.sym("prg_ext_start"),
	0x04001770: main.sym("exit"),
	0x04001774: main.sym("light"),

	0x04001328: main.sym("case_G_ENDDL"),
	0x0400138C: main.sym("case_RDP"),

	0x04000000: main.sym("prg_init"),
	0x04000008: main.sym("prg_main", flag={"LOCAL"}),
	0x04000010: main.sym("prg_clip", flag={"LOCAL"}),
	0x04000018: main.sym("prg_light", flag={"LOCAL"}),
	0x04000020: main.sym("prg_exit", flag={"LOCAL"}),
	0x04000026: main.sym("prg_exit+6"),
	0x04000028: main.sym("VCONST_028"),
	0x04000030: main.sym("VCONST_030"),
	0x04000040: main.sym("VCONST_040"),
	0x04000050: main.sym("VCONST_050"),
	0x04000060: main.sym("VCONST_060"),
	0x04000070: main.sym("CLIPPING"),
	0x04000076: main.sym("CLIPPING+6"),
	0x040000A0: main.sym("LIGHTPROC"),
	0x040000A8: main.sym("CLIPMASK"),
	0x040000B4: main.sym("ANCHOR"),
	0x040000B6: main.sym("EXITPROC"),
	0x040000B8: main.sym("SEGMENT_MASK"),
	0x040000BE: main.sym("NEXTCOMMAND"),
	0x040000D8: main.sym("IMMTAB"),
	0x040000F6: main.sym("CLIPTAB"),
	0x040000F8: main.sym("CLIPFOUT", flag={"LOCAL"}),
	0x040000FE: main.sym("CLIPDRAW", flag={"LOCAL"}),
	0x04000100: main.sym("CLIPPROC", flag={"LOCAL"}),
	0x04000102: main.sym("CLIPNEXT", flag={"LOCAL"}),
	0x04000104: main.sym("SYNCNEXT"),
	0x04000106: main.sym("RETURN"),

	0x04000108: main.sym("YIELDPTR"),
	0x04000110: main.sym("DLINDEX"),
	0x04000112: main.sym("PERSPNORM"),
	0x0400012C: main.sym("LIGHTNO"),
	0x04000138: main.sym("TXTATT"),
	0x04000158: main.sym("RETURN2"),

	0x04000160: main.sym("SEGMENT_TABLE"),
	0x040001B0: main.sym("LOOKATX"),
	0x040001D0: main.sym("LOOKATY"),
	0x040001F0: main.sym("LIGHT0"),
	0x04000210: main.sym("LIGHT1"),
	0x04000230: main.sym("LIGHT2"),
	0x04000250: main.sym("LIGHT3"),
	0x04000270: main.sym("LIGHT4"),
	0x04000290: main.sym("LIGHT5"),
	0x040002B0: main.sym("LIGHT6"),
	0x040002D0: main.sym("LIGHT7"),
	0x04000320: main.sym("VIEWPORT"),
	0x04000330: main.sym("FOGFACTOR"),

	# 0x040003E0: main.sym(""),
	# 0x040003F0: main.sym(""),
	# 0x04000400: main.sym(""),
	# 0x04000410: main.sym(""),
	# 0x04000420: main.sym(""),
	# 0x040008E4: main.sym(""),
	# 0x040008E8: main.sym(""),
	# 0x040008EC: main.sym(""),
	# 0x040008F0: main.sym(""),
	# 0x04000940: main.sym(""),
	# 0x04000942: main.sym(""),
	# 0x04000944: main.sym(""),
	# 0x04000946: main.sym(""),
	# 0x04000DE0: main.sym(""),
	# 0x04000DE4: main.sym(""),
	# 0x04000DE8: main.sym(""),
	# 0x04000FC4: main.sym(""),
}

sym_F_gspFast3D_fifo_data = {
	0x04000110: main.sym("PERSPNORM_H"),
	0x04000112: main.sym("PERSPNORM", flag={"LOCAL"}),
	0x0400015A: main.sym("DLINDEX"),
}

sym_D_aspMain_text = {
	0x040010D4: main.sym(".cmd_proc", flag={"LOCAL"}),
	0x04001118: main.sym("cmd_next"),
	0x04001150: main.sym("cmd_load"),
	0x04001184: main.sym("dma_read"),
	0x040011B0: main.sym("dma_write"),
	0x040011DC: main.sym("case_A_CLEARBUFF"),
	0x04001214: main.sym("case_A_LOADBUFF"),
	0x04001254: main.sym("case_A_SAVEBUFF"),
	0x04001294: main.sym("case_A_LOADADPCM"),
	0x040012D0: main.sym("case_A_SEGMENT"),
	0x040012EC: main.sym("case_A_SETBUFF"),
	0x04001328: main.sym("case_A_SETVOL"),
	0x0400138C: main.sym("case_A_INTERLEAVE"),
	0x0400140C: main.sym("case_A_DMEMMOVE"),
	0x0400144C: main.sym("case_A_SETLOOP"),
	0x04001470: main.sym("case_A_ADPCM"),
	0x0400170C: main.sym("case_A_POLEF"),
	0x0400187C: main.sym("case_A_RESAMPLE"),
	0x040018E8: main.sym(".L040018E8", flag={"LOCAL"}),
	0x040019D8: main.sym(".L040019D8", flag={"LOCAL"}),
	0x04001B38: main.sym("case_A_ENVMIXER"),
	0x04001BB0: main.sym(".L04001BB0", flag={"LOCAL"}),
	0x04001C48: main.sym(".L04001C48", flag={"LOCAL"}),
	0x04001CB8: main.sym(".L04001CB8", flag={"LOCAL"}),
	0x04001D04: main.sym(".L04001D04", flag={"LOCAL"}),
	0x04001D50: main.sym(".L04001D50", flag={"LOCAL"}),
	0x04001DBC: main.sym(".L04001DBC", flag={"LOCAL"}),
	0x04001E24: main.sym("case_A_MIXER"),
}

sym_D_aspMain_data = {
	0x04001328: main.sym("case_A_SETVOL"),
	0x0400138C: main.sym("case_A_INTERLEAVE"),

	0x04000000: main.sym("vconst"),
}
