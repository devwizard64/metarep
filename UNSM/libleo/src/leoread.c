#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

void leoRead(void)
{
	LEOrw_flags = 0;
	leoRead_common(24);
}

void leoRead_common(u32 offset)
{
	u32 lba, blocks, message;
	u8 retry;
	lba = read_cmd->lba;
	blocks = read_cmd->xfer_blks;
	if ((lba|blocks) & 0xFFFF0000) goto invalid_lba;
	lba += offset;
	if (lba+blocks > 4315+1)
	{
invalid_lba:
		read_cmd->header.sense = LEO_SENSE_LBA_OUT_OF_RANGE;
		read_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
		return;
	}
	if (blocks == 0)
	{
		if (lba > 4315) goto invalid_lba;
		read_cmd->header.sense = LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
		read_cmd->header.status = LEO_STATUS_GOOD;
		return;
	}
	LEOtgt_param.lba = lba;
	LEOrw_flags &= ~0xC100;
	osSendMesg(&LEOc2ctrl_que, (OSMesg)0, OS_MESG_NOBLOCK);
	osStartThread(&LEOinterruptThread);
	for (;;)
	{
		osRecvMesg(&LEOcontrol_que, (OSMesg *)&message, OS_MESG_BLOCK);
		switch (message)
		{
		case 0x00090000:
			goto read_ok;
		case 0x00080000:
			leoC2_Correction();
			LEOrw_flags &= ~0x4000;
			osSendMesg(&LEOc2ctrl_que, (OSMesg)0, OS_MESG_NOBLOCK);
			continue;
		default:
			read_cmd->header.sense = message;
			read_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
			return;
		}
	}
read_ok:
	read_cmd->header.sense = LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
	read_cmd->header.status = LEO_STATUS_GOOD;
}
