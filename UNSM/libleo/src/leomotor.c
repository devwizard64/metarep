#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

void leoStart_stop(void)
{
	u32 asic_cmd, asic_data;
	u8 sense, retry = 16;
	asic_data = 0;
	do
	{
		if (motor_cmd->header.control & LEO_CONTROL_START)
		{
			asic_cmd = 0x00050001;
		}
		else if (motor_cmd->header.control & LEO_CONTROL_STBY)
		{
			asic_cmd = 0x000D0000;
		}
		else
		{
			asic_cmd = 0x00040000;
		}
		if (!(sense = leoSend_asic_cmd_w(asic_cmd, asic_data))) goto motor_ok;
		if (
			sense == LEO_SENSE_MEDIUM_NOT_PRESENT ||
			sense == LEO_SENSE_POWERONRESET_DEVICERESET_OCCURED ||
			sense == LEO_SENSE_MEDIUM_MAY_HAVE_CHANGED
		) break;
	}
	while (retry--);
	motor_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
	return;
motor_ok:
	motor_cmd->header.status = LEO_STATUS_GOOD;
}
