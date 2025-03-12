#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

void leoMode_sel(void)
{
	if (leoSend_asic_cmd_w(0x00060000, mode_cmd->standby_time << 16))
	{
		mode_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
		return;
	}
	if (leoSend_asic_cmd_w(0x00070000, mode_cmd->sleep_time << 16))
	{
		mode_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
		return;
	}
	if (leoSend_asic_cmd_w(0x00150000, *(u32 *)&mode_cmd->led_on_time))
	{
		mode_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
		return;
	}
	mode_cmd->header.status = LEO_STATUS_GOOD;
	return;
}
