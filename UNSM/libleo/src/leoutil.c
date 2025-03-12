#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

u16 leoLba_to_phys(u32 lba)
{
	u16 vzone, start_lba, cylinder, track, bad_track;
	u32 n;
	u16 def_offset, defect;
	u8 def_zone;
	LEOtgt_param.rdwr_blocks = 2 - (lba & 1);
	switch (lba & 3)
	{
	case 0:
	case 3:
		LEOtgt_param.start_block = 0;
		break;
	default:
		LEOtgt_param.start_block = 1;
		break;
	}
	vzone = leoLba_to_vzone(lba);
	LEOtgt_param.zone = def_zone = LEOVZONE_PZONEHD_TBL[LEOdisk_type][vzone];
	LEOtgt_param.head = 0;
	if (LEOtgt_param.zone > 7)
	{
		LEOtgt_param.zone -= 7;
		LEOtgt_param.head = 1;
	}
	cylinder = LEOZONE_SCYL_TBL[def_zone];
	if (vzone)  start_lba = LEOVZONE_TBL[LEOdisk_type][vzone-1];
	else        start_lba = 0;
	track = (lba-start_lba) / 2;
	if (LEOtgt_param.head)
	{
		LEOtgt_param.cylinder = cylinder - track;
		cylinder = LEOZONE_OUTERCYL_TBL[LEOtgt_param.zone-1];
	}
	else
	{
		LEOtgt_param.cylinder = cylinder + track;
	}
	if (def_zone)   def_offset = LEO_sys_data.param.defect_num[def_zone-1];
	else            def_offset = 0;
	bad_track = LEO_sys_data.param.defect_num[def_zone] - def_offset;
	while (bad_track)
	{
		defect = LEO_sys_data.param.defect_data[def_offset] + cylinder;
		if (LEOtgt_param.cylinder < defect) break;
		LEOtgt_param.cylinder++;
		def_offset++;
		bad_track--;
	}
	LEOtgt_param.sec_bytes = LEOBYTE_TBL1[LEOtgt_param.zone];
	LEOtgt_param.blk_bytes = LEOBYTE_TBL2[LEOtgt_param.zone];
	if (LEO_country_code.u32_data == 0 && lba < 12)
	{
		LEOtgt_param.sec_bytes = 192;
		LEOtgt_param.blk_bytes = 192*85;
	}
	return 0;
}

u16 leoLba_to_vzone(u32 lba)
{
	u16 i;
	const u16 *tbl = LEOVZONE_TBL[LEOdisk_type];
	for (i = 0; i < 16; i++)
	{
		if (lba < *tbl) return i;
		tbl++;
	}
	return 0xFF;
}
