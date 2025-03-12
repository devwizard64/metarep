#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

void leoTest_unit_rdy(void)
{
	test_cmd->header.sense = LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
	test_cmd->header.status = LEO_STATUS_GOOD;
}

u8 leoChk_cur_drvmode(u32 asic_stat)
{
	u8 stat = 0;
	if (!(asic_stat & 0x01000000)) stat |= LEO_TEST_UNIT_MR;
	if ( (asic_stat & 0x00080000)) stat |= LEO_TEST_UNIT_RE;
	if ( (asic_stat & 0x00100000)) stat |= LEO_TEST_UNIT_SS;
	return stat;
}
