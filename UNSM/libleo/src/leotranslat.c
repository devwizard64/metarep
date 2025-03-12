#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

void leoTranslate(void)
{
	u32 lba, nbyte, nblk, n;
	u16 zone, vzone;
	u8 flag;
	if (translate_cmd->start_lba > 4315-24)
	{
		translate_cmd->header.sense = LEO_SENSE_LBA_OUT_OF_RANGE;
		translate_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
		return;
	}
	lba = translate_cmd->start_lba + 24;
	nbyte = nblk = 0;
	flag = vzone = 1;
	if (translate_cmd->header.control & LEO_CONTROL_TBL)
	{
		nbyte = translate_cmd->in_param;
		while (nbyte)
		{
			if (flag || LEOVZONE_TBL[LEOdisk_type][vzone] == lba)
			{
				vzone = leoLba_to_vzone(lba);
				zone = LEOVZONE_PZONEHD_TBL[LEOdisk_type][vzone];
				if (zone > 7) zone -= 7;
				n = LEOBYTE_TBL2[zone];
			}
			if (nbyte < n)  nbyte = 0;
			else            nbyte -= n;
			nblk++;
			lba++;
			if (nbyte && lba > 4315)
			{
				translate_cmd->header.sense = LEO_SENSE_LBA_OUT_OF_RANGE;
				translate_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
				return;
			}
			flag = 0;
		}
		translate_cmd->out_param = nblk;
	}
	else
	{
		nblk = translate_cmd->in_param;
		while (nblk)
		{
			if (flag || LEOVZONE_TBL[LEOdisk_type][vzone] == lba)
			{
				vzone = leoLba_to_vzone(lba);
				zone = LEOVZONE_PZONEHD_TBL[LEOdisk_type][vzone];
				if (zone > 7) zone -= 7;
				n = LEOBYTE_TBL2[zone];
			}
			nbyte += n;
			nblk--;
			lba++;
			if (nblk && lba > 4315)
			{
				translate_cmd->header.sense = LEO_SENSE_LBA_OUT_OF_RANGE;
				translate_cmd->header.status = LEO_STATUS_CHECK_CONDITION;
				return;
			}
			flag = 0;
		}
		translate_cmd->out_param = nbyte;
	}
	translate_cmd->header.status = LEO_STATUS_GOOD;
}
