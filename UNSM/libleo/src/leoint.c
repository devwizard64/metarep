#include <ultra64.h>
#include <PR/leoappli.h>
#include "leodrive.h"
#include "leoint.h"

static OSMesg LEOc2ctrl_que_buf[1];
OSMesgQueue LEOc2ctrl_que;

u32 read_write_track(void);
u32 leoChk_mecha_int(void);
void leosetup_BM(void);
u32 leochk_err_reg(void);
u32 leoChk_err_retry(u32 sense);

void leointerrupt(void *arg)
{
	u32 result, blocks;
	osCreateMesgQueue(&LEOc2ctrl_que, LEOc2ctrl_que_buf, 1);
	for (;;)
	{
		osStopThread(&LEOinterruptThread);
		blocks = read_cmd->xfer_blks;
		LEOwrite_pointer = read_cmd->buff_ptr;
		do
		{
			leoLba_to_phys(LEOtgt_param.lba);
			if (LEOrw_flags & 0x8000)   result = leoSeek_i(1);
			else                        result = leoSeek_i(0);
			if (result) goto complete;
			if (LEOtgt_param.rdwr_blocks > blocks) LEOtgt_param.rdwr_blocks = blocks;
			LEOtgt_param.lba += LEOtgt_param.rdwr_blocks;
			blocks -= LEOtgt_param.rdwr_blocks;
			result = read_write_track();
			if (result) goto complete;
			read_cmd->rw_bytes = LEOwrite_pointer - (u8 *)read_cmd->buff_ptr;
		}
		while (blocks);
		result = 0x00090000;
complete:
		osSendMesg(&LEOcontrol_que, (OSMesg)result, OS_MESG_BLOCK);
	}
}

u32 read_write_track(void)
{
	u32 result, block, retry;
	struct block_param_form block_param;
	block_param.bytes = LEOtgt_param.sec_bytes;
	block_param.blkbytes = LEOtgt_param.blk_bytes;
	block_param.pntr = LEOwrite_pointer;
	LEOwrite_pointer += block_param.blkbytes;
	if (LEOtgt_param.rdwr_blocks == 2) LEOwrite_pointer += block_param.blkbytes;
	retry = 0;
	for (;;)
	{
		LEOPiInfo->transferInfo.transferMode = LEO_BLOCK_MODE;
		LEOPiInfo->transferInfo.blockNum = 0;
		LEOPiInfo->transferInfo.block[0].C1ErrNum = 0;
		LEOPiInfo->transferInfo.block[0].sectorSize = block_param.bytes;
		LEOPiInfo->transferInfo.block[0].dramAddr = block_param.pntr;
		LEOPiInfo->transferInfo.block[0].C2Addr = LEOC2_Syndrome[0][0];
		if (LEOrw_flags & 0x2000)
		{
			LEOtgt_param.rdwr_blocks = 1;
			LEOPiInfo->transferInfo.transferMode = LEO_SECTOR_MODE;
		}
		else if (LEOtgt_param.rdwr_blocks == 2)
		{
			LEOPiInfo->transferInfo.transferMode = LEO_TRACK_MODE;
			LEOPiInfo->transferInfo.block[1] = LEOPiInfo->transferInfo.block[0];
			LEOPiInfo->transferInfo.block[1].C2Addr = LEOC2_Syndrome[1][0];
			LEOPiInfo->transferInfo.block[1].dramAddr =
				(char *)LEOPiInfo->transferInfo.block[1].dramAddr + block_param.blkbytes;
		}
		osRecvMesg(&LEOevent_que, (OSMesg *)&result, OS_MESG_BLOCK);
		if ((result = leoChk_mecha_int())) goto track_end;
		if (LEOrw_flags & 0x8000)   leoSet_mseq(1);
		else                        leoSet_mseq(0);
		leosetup_BM();
		LEOPiInfo->transferInfo.bmCtlShadow = LEOasic_bm_ctl_shadow;
		LEOPiInfo->transferInfo.seqCtlShadow = LEOasic_seq_ctl_shadow;
		if (LEOrw_flags & 0x8000)
		{
			u16 bnum;
			LEOPiInfo->transferInfo.cmdType = OS_WRITE;
			osWritebackDCache(block_param.pntr, block_param.blkbytes*LEOtgt_param.rdwr_blocks);
			osEPiStartDma(LEOPiInfo, &LEOPiDmaParam, OS_WRITE);
			osRecvMesg(&LEOdma_que, (OSMesg *)&result, OS_MESG_BLOCK);
			LEOasic_bm_ctl_shadow = LEOPiInfo->transferInfo.bmCtlShadow;
			LEOasic_seq_ctl_shadow = LEOPiInfo->transferInfo.seqCtlShadow;
			bnum = LEOPiInfo->transferInfo.blockNum;
			result = LEOPiInfo->transferInfo.block[bnum].errStatus;
			if (!result) return result;
			goto track_end;
		}
		if (LEOrw_flags & 0x4000)
		{
			osRecvMesg(&LEOc2ctrl_que, NULL, OS_MESG_BLOCK);
			osSendMesg(&LEOc2ctrl_que, (OSMesg)0, OS_MESG_NOBLOCK);
		}
		LEOPiInfo->transferInfo.cmdType = OS_READ;
		if (LEOrw_flags & 0x2000) osInvalDCache(block_param.pntr, block_param.bytes);
		else osInvalDCache(block_param.pntr, block_param.blkbytes*LEOtgt_param.rdwr_blocks);
		osEPiStartDma(LEOPiInfo, &LEOPiDmaParam, OS_READ);
		for (block = 0; LEOtgt_param.rdwr_blocks; LEOtgt_param.rdwr_blocks--, block++)
		{
			osRecvMesg(&LEOdma_que, (OSMesg *)&result, OS_MESG_BLOCK);
			LEOasic_bm_ctl_shadow = LEOPiInfo->transferInfo.bmCtlShadow;
			LEOasic_seq_ctl_shadow = LEOPiInfo->transferInfo.seqCtlShadow;
			result = LEOPiInfo->transferInfo.block[block].errStatus;
			if (result) goto track_end;
			if (LEOrw_flags & 0x2000) return LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
			if (LEOPiInfo->transferInfo.block[block].C1ErrNum)
			{
				if (LEOPiInfo->transferInfo.block[block].C1ErrSector[0] < 85)
				{
					u8 *temp;
					u32 c2datasize;
					if (LEOtgt_param.rdwr_blocks == 1)
					{
						osEPiReadIo(LEOPiInfo, ASIC_ERR_SECTOR, &result);
						if (result & 0x10000000)
						{
							result = LEO_SENSE_DATA_PHASE_ERROR;
							goto track_end;
						}
					}
					if (block == 0) temp = LEOC2_Syndrome[0][0];
					else            temp = LEOC2_Syndrome[1][0];
					c2datasize = block_param.bytes * 4;
					block_param.c2buff_e = temp + c2datasize;
					osInvalDCache(temp, c2datasize);
					block_param.err_num    = LEOPiInfo->transferInfo.block[block].C1ErrNum;
					block_param.err_pos[0] = LEOPiInfo->transferInfo.block[block].C1ErrSector[0];
					block_param.err_pos[1] = LEOPiInfo->transferInfo.block[block].C1ErrSector[1];
					block_param.err_pos[2] = LEOPiInfo->transferInfo.block[block].C1ErrSector[2];
					block_param.err_pos[3] = LEOPiInfo->transferInfo.block[block].C1ErrSector[3];
					osRecvMesg(&LEOc2ctrl_que, NULL, OS_MESG_BLOCK);
					LEOrw_flags |= 0x4000;
					LEOc2_param = block_param;
					osSendMesg(&LEOcontrol_que, (OSMesg)0x00080000, OS_MESG_BLOCK);
				}
			}
			else
			{
				if (LEOtgt_param.rdwr_blocks == 1)
				{
					if (
						*(u32 *)&LEOC2_Syndrome[block][0][ 0] |
						*(u32 *)&LEOC2_Syndrome[block][0][ 4] |
						*(u32 *)&LEOC2_Syndrome[block][0][ 8] |
						*(u32 *)&LEOC2_Syndrome[block][0][12]
					)
					{
						result = LEO_SENSE_NO_REFERENCE_POSITION_FOUND;
						goto track_end;
					}
				}
			}
			LEOtgt_param.start_block ^= 1;
			block_param.pntr += block_param.blkbytes;
		}
		return LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
track_end:
		if (result == LEO_SENSE_WRITE_FAULT) result = leochk_err_reg();
do_retry:
		if (LEOrw_flags & 0x1000) break;
		if (retry++ == 64) break;
		if (leoChk_err_retry(result)) break;
		if ((retry & 7) == 0)
		{
			result = leoSend_asic_cmd_w(0x00030001, 0);
			if (result) goto do_retry;
		}
		if (result == LEO_SENSE_NO_REFERENCE_POSITION_FOUND)
		{
			result = leoDetect_index_w();
			if (result) goto do_retry;
		}
		if (LEOrw_flags & 0x8000)   result = leoSeek_i(1);
		else                        result = leoSeek_i(0);
		if (result) goto do_retry;
	}
	return result;
}

u32 leoChk_mecha_int(void)
{
	u32 sense, index_stat;
	if (!(sense = leoChk_done_status(0x00010001)))
	{
		osEPiReadIo(LEOPiInfo, ASIC_CUR_TK, &index_stat);
		if ((index_stat & 0x60000000) != 0x60000000) sense = LEO_SENSE_NO_REFERENCE_POSITION_FOUND;
	}
	return sense;
}

void leosetup_BM(void)
{
	osEPiWriteIo(LEOPiInfo, ASIC_BM_CTL, LEOasic_bm_ctl_shadow|0x10000000);
	osEPiWriteIo(LEOPiInfo, ASIC_BM_CTL, LEOasic_bm_ctl_shadow);
	if (LEOtgt_param.start_block)   LEOasic_bm_ctl_shadow = 0x005A0000;
	else                            LEOasic_bm_ctl_shadow = 0x00000000;
	if (!(LEOrw_flags & 0x8000)) LEOasic_bm_ctl_shadow |= 0x40000000;
	if (LEOtgt_param.rdwr_blocks == 2) LEOasic_bm_ctl_shadow |= 0x02000000;
	osEPiWriteIo(LEOPiInfo, ASIC_BM_CTL, LEOasic_bm_ctl_shadow);
}

u32 leochk_err_reg(void)
{
	u32 stat, index_stat;
	osEPiReadIo(LEOPiInfo, ASIC_ERR_SECTOR, &stat);
	osEPiWriteIo(LEOPiInfo, ASIC_BM_CTL, LEOasic_bm_ctl_shadow|0x10000000);
	osEPiWriteIo(LEOPiInfo, ASIC_BM_CTL, LEOasic_bm_ctl_shadow);
	if      (stat & 0x04000000) return LEO_SENSE_MEDIUM_NOT_PRESENT;
	else if (stat & 0x10000000) return LEO_SENSE_DATA_PHASE_ERROR;
	else if (stat & 0x42000000)
	{
		if (LEOrw_flags & 0x8000) return LEO_SENSE_WRITE_FAULT;
		return LEO_SENSE_UNRECOVERED_READ_ERROR;
	}
	else if (stat & 0x80000000) return LEO_SENSE_NO_REFERENCE_POSITION_FOUND;
	else
	{
		osEPiReadIo(LEOPiInfo, ASIC_CUR_TK, &index_stat);
		if ((index_stat & 0x60000000) == 0x60000000)    return LEO_SENSE_TRACK_FOLLOWING_ERROR;
		else                                            return LEO_SENSE_NO_REFERENCE_POSITION_FOUND;
	}
}

u32 leoChk_err_retry(u32 sense)
{
	switch (sense)
	{
	case LEO_SENSE_MEDIUM_MAY_HAVE_CHANGED:
	case LEO_SENSE_POWERONRESET_DEVICERESET_OCCURED:
	case LEO_SENSE_MEDIUM_NOT_PRESENT:
		return -1;
	}
	return 0;
}
