#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

void leoSeek(void)
{
	u32 lba;
	u8 retry = 16;
	if (seek_cmd->lba > 4315-24)
	{
		seek_cmd->header.sense = LEO_SENSE_LBA_OUT_OF_RANGE;
		seek_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
		return;
	}
	lba = seek_cmd->lba+24;
	leoLba_to_phys(lba);
	do
	{
		if (leoSeek_i(0))
		{
			seek_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
			return;
		}
		osRecvMesg(&LEOevent_que, NULL, OS_MESG_BLOCK);
		if (!(seek_cmd->header.sense = leoChk_done_status(0x00010001)))
		{
			seek_cmd->header.status = LEO_STATUS_GOOD;
			return;
		}
	}
	while (retry--);
	seek_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
	return;
}
