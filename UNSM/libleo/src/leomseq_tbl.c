#include <ultra64.h>
#include <PR/leoappli.h>
#include "leodrive.h"
#include "leoint.h"

static u32 mseq_tbl[16];

static const u32 rd_mseq_code[16] =
{
	0x00010000,0x00020000,0x80030100,0x82040000,
	0xAC050000,0xA0060600,0x31760000,0x00020000,
	0x00000000,0x00000000,0x00000000,0x00000000,
	0x00000000,0x00000000,0x00000000,0x00060000,
};

static const u32 wt_mseq_code[16] =
{
	0x40020000,0x00020000,0x40130B00,0x42140100,
	0x68050000,0x50060600,0x401702FF,0x01870000,
	0x40020000,0x00000000,0x00000000,0x00000000,
	0x00000000,0x00000000,0x00000000,0x040F0000,
};

void leoSet_mseq(u16 rwmode)
{
	OSMesg msg;
	u32 sec_bytes;
	u8 i;
	osEPiWriteIo(LEOPiInfo, ASIC_SEQ_CTL, LEOasic_seq_ctl_shadow &= ~0x40000000);
	sec_bytes = LEOtgt_param.sec_bytes;
	if (rwmode == 0)
	{
		for (i = 0; i < 16; i++) mseq_tbl[i] = rd_mseq_code[i];
		mseq_tbl[1] |= leo_rodata_804B21A8[LEOtgt_param.zone] << 8;
		mseq_tbl[7] |= leo_rodata_804B21B4[LEOtgt_param.zone] << 8;
		mseq_tbl[4] |= sec_bytes-1 << 8;
	}
	else
	{
		for (i = 0; i < 16; i++) mseq_tbl[i] = wt_mseq_code[i];
		mseq_tbl[1] |= leo_rodata_804B21C0[LEOtgt_param.zone] << 8;
		mseq_tbl[8] |= leo_rodata_804B21CC[LEOtgt_param.zone] << 8;
		mseq_tbl[4] |= sec_bytes-1 << 8;
	}
	osWritebackDCache(mseq_tbl, sizeof(mseq_tbl));
	LEOPiDmaParam.dramAddr = mseq_tbl;
	LEOPiDmaParam.devAddr = MSEQ_RAM_ADDR;
	LEOPiDmaParam.size = sizeof(mseq_tbl);
	LEOPiInfo->transferInfo.cmdType = OS_OTHERS;
	osEPiStartDma(LEOPiInfo, &LEOPiDmaParam, OS_WRITE);
	osRecvMesg(&LEOdma_que, &msg, OS_MESG_BLOCK);
	osEPiWriteIo(LEOPiInfo, ASIC_SEC_BYTE, (sec_bytes+6 | 0x5900) << 16);
	osEPiWriteIo(LEOPiInfo, ASIC_HOST_SECBYTE, sec_bytes-1 << 16);
	osEPiWriteIo(LEOPiInfo, ASIC_SEQ_CTL, LEOasic_seq_ctl_shadow |= 0x40000000);
}
