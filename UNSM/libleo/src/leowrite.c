#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

void leoWrite(void)
{
	u32 message, lba, blocks;
	u32 count = 0;
	u8 retry = 0;
	lba = write_cmd->lba;
	blocks = write_cmd->xfer_blks;
	if ((lba|blocks) & 0xFFFF0000) goto invalid_lba;
	lba += 24;
	if (lba > 4315 || lba+blocks > 4315+1)
	{
invalid_lba:
		write_cmd->header.sense = LEO_SENSE_LBA_OUT_OF_RANGE;
		write_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
		return;
	}
	if (lba < LEORAM_START_LBA[LEOdisk_type])
	{
		write_cmd->header.sense = LEO_SENSE_WRITE_PROTECT_ERROR;
		write_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
		return;
	}
	if (blocks == 0)
	{
		write_cmd->header.sense = LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
		write_cmd->header.status = LEO_STATUS_GOOD;
		return;
	}
	LEOrw_flags = 0x8000;
	LEOtgt_param.lba = lba;
	osStartThread(&LEOinterruptThread);
	osRecvMesg(&LEOcontrol_que, (OSMesg *)&message, OS_MESG_BLOCK);
	if (message != 0x00090000)
	{
		write_cmd->header.sense = message;
		write_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
		return;
	}
	write_cmd->header.sense = LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
	write_cmd->header.status = LEO_STATUS_GOOD;
}
