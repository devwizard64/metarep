#include <ultra64.h>
#include <PR/leoappli.h>
#include "leodrive.h"
#include "leoint.h"

void leoInquiry(void)
{
	u32 asic_id;
	osEPiReadIo(LEOPiInfo, ASIC_ID_REG, &asic_id);
	inquiry_cmd->dev_type = 0;
	inquiry_cmd->version = asic_id >> 16;
	inquiry_cmd->dev_num = 1;
	inquiry_cmd->leo_bios_ver = 0;
	inquiry_cmd->header.status = LEO_STATUS_GOOD;
}
