#include <ultra64.h>
#include <PR/leoappli.h>
#include "leodrive.h"
#include "leoint.h"

u8 leoAnalize_asic_status(u32 asic_stat)
{
	if ((asic_stat ^= 0x01000000) & 0x01C3FFFF)
	{
		if (asic_stat & 0x01C1FFFF) LEOdrive_flag = 0;
		if (asic_stat & 0x0000FFFF) return LEO_SENSE_DEVICE_COMMUNICATION_FAILURE;
		if ((asic_stat & 0x00C00000) == 0x00800000) return LEO_SENSE_COMMAND_PHASE_ERROR;
		if (asic_stat & 0x00400000) return LEO_SENSE_POWERONRESET_DEVICERESET_OCCURED;
		if (asic_stat & 0x01000000) return LEO_SENSE_MEDIUM_NOT_PRESENT;
		if (asic_stat & 0x00010000) return LEO_SENSE_MEDIUM_MAY_HAVE_CHANGED;
		if (asic_stat & 0x00020000) return LEO_SENSE_NO_SEEK_COMPLETE;
	}
	return LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
}

u8 leoChk_asic_ready(u32 asic_cmd, u32 asic_stat)
{
	u32 sense = leoAnalize_asic_status(asic_stat);
	switch (sense)
	{
	case LEO_SENSE_MEDIUM_MAY_HAVE_CHANGED:
		if (asic_cmd == 0x00080000) return LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
	case LEO_SENSE_POWERONRESET_DEVICERESET_OCCURED:
		if (!(asic_stat & 0x00800000))
		{
			if (asic_cmd == 0x00090000) return LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
			osRecvMesg(&LEOevent_que, NULL, OS_MESG_NOBLOCK);
			osEPiWriteIo(LEOPiInfo, ASIC_CMD, 0x00090000);
			osRecvMesg(&LEOevent_que, NULL, OS_MESG_BLOCK);
		}
		break;
	case LEO_SENSE_MEDIUM_NOT_PRESENT:
		if (asic_cmd & 1) break;
	case LEO_SENSE_NO_SEEK_COMPLETE:
		return LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
	}
	return sense;
}

u8 leoChk_done_status(u32 asic_cmd)
{
	u32 asic_stat, sense;
	osEPiReadIo(LEOPiInfo, ASIC_STATUS, &asic_stat);
	sense = leoAnalize_asic_status(asic_stat);
	switch (sense)
	{
	case LEO_SENSE_MEDIUM_MAY_HAVE_CHANGED:
	case LEO_SENSE_POWERONRESET_DEVICERESET_OCCURED:
		if (!(asic_stat & 0x00800000))
		{
			osRecvMesg(&LEOevent_que, NULL, OS_MESG_NOBLOCK);
			osEPiWriteIo(LEOPiInfo, ASIC_CMD, 0x00090000);
			osRecvMesg(&LEOevent_que, NULL, OS_MESG_BLOCK);
		}
		break;
	case LEO_SENSE_MEDIUM_NOT_PRESENT:
		if (asic_cmd & 1) break;
		return LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
	case LEO_SENSE_NO_SEEK_COMPLETE:
		osEPiWriteIo(LEOPiInfo, ASIC_DATA, 0);
		osRecvMesg(&LEOevent_que, NULL, OS_MESG_NOBLOCK);
		osEPiWriteIo(LEOPiInfo, ASIC_CMD, 0x000C0000);
		osRecvMesg(&LEOevent_que, NULL, OS_MESG_BLOCK);
		if ((sense = leoChk_asic_ready(0x000C0000, asic_stat))) return sense;
		osEPiReadIo(LEOPiInfo, ASIC_DATA, &asic_stat);
		if (asic_stat & 0x00010000) return LEO_SENSE_DIAGNOSTIC_FAILURE;
		if (asic_stat & 0x00020000) return LEO_SENSE_NO_REFERENCE_POSITION_FOUND;
		if (asic_stat & 0x00040000) return LEO_SENSE_DRIVE_NOT_READY;
		if (asic_stat & 0x00080000) return LEO_SENSE_NO_SEEK_COMPLETE;
		if (asic_stat & 0x00200000) return LEO_SENSE_INCOMPATIBLE_MEDIUM_INSTALLED;
		return LEO_SENSE_DEVICE_COMMUNICATION_FAILURE;
	}
	return sense;
}

u8 leoSend_asic_cmd_i(u32 asic_cmd, u32 asic_data)
{
	u32 asic_stat;
	u8 sense;
	osEPiReadIo(LEOPiInfo, ASIC_STATUS, &asic_stat);
	if ((sense = leoChk_asic_ready(asic_cmd, asic_stat)))
	{
		return cmd_hdr->sense = sense;
	}
	osEPiWriteIo(LEOPiInfo, ASIC_DATA, asic_data);
	osRecvMesg(&LEOevent_que, NULL, OS_MESG_NOBLOCK);
	osEPiWriteIo(LEOPiInfo, ASIC_CMD, asic_cmd);
	return LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
}

u8 leoSend_asic_cmd_w(u32 asic_cmd, u32 asic_data)
{
	u32 sense;
	if ((sense = leoSend_asic_cmd_i(asic_cmd, asic_data))) return sense;
	osRecvMesg(&LEOevent_que, NULL, OS_MESG_BLOCK);
	if ((sense = leoChk_done_status(asic_cmd))) return cmd_hdr->sense = sense;
	return LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
}

u8 leoDetect_index_w(void)
{
	return leoSend_asic_cmd_w(0x000E0001, 0);
}

u8 leoRecal_i(void)
{
	return leoSend_asic_cmd_i(0x00030001, 0);
}

u8 leoSeek_i(u16 rwmode)
{
	u32 asic_data = (LEOtgt_param.head<<12)+LEOtgt_param.cylinder << 16;
	if (rwmode == 0)    return leoSend_asic_cmd_i(0x00010001, asic_data);
	else                return leoSend_asic_cmd_i(0x00020001, asic_data);
}
