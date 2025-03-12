#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

void leoRd_capacity(void)
{
	if (capacity_cmd->header.control & LEO_CONTROL_WRT)
	{
		capacity_cmd->start_lba = LEORAM_START_LBA[LEOdisk_type]-24;
		capacity_cmd->end_lba = 4315-24;
		capacity_cmd->capa_bytes = LEORAM_BYTE[LEOdisk_type];
	}
	else
	{
		capacity_cmd->start_lba = 0;
		capacity_cmd->end_lba = 4315-24;
		capacity_cmd->capa_bytes = 0x3DEC800 - 232*85*24;
	}
	capacity_cmd->header.status = LEO_STATUS_GOOD;
}
