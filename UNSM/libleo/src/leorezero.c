#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

void leoRezero(void)
{
	u8 retry = 16;
	do
	{
		if (leoRecal_i())
		{
			rezero_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
			return;
		}
		osRecvMesg(&LEOevent_que, NULL, OS_MESG_BLOCK);
		if (!(rezero_cmd->header.sense = leoChk_done_status(0x00030001)))
		{
			goto rezero_ok;
		}
	}
	while (retry--);
	rezero_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
	return;
rezero_ok:
	LEOtgt_param.cylinder = 0;
	LEOtgt_param.head = 0;
	LEOtgt_param.zone = 0;
	rezero_cmd->header.status = LEO_STATUS_GOOD;
}
