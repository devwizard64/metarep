#include <ultra64.h>
#include <PR/leoappli.h>
#include "leodrive.h"
#include "leoint.h"

OSPiHandle *LEOPiInfo;
OSIoMesg LEOPiDmaParam;

static u8 leoRead_system_area(void);

extern void leoReset(void);
extern void leoClr_queue(void);
extern void leoInquiry(void);
extern void leoTest_unit_rdy(void);
extern void leoRezero(void);
extern void leoRead(void);
extern void leoWrite(void);
extern void leoSeek(void);
extern void leoStart_stop(void);
extern void leoRd_capacity(void);
extern void leoTranslate(void);
extern void leoMode_sel(void);
extern void leoReadDiskId(void);

static void (*cmd_tbl[])(void) =
{
	leoReset,
	leoClr_queue,
	leoInquiry,
	leoTest_unit_rdy,
	leoRezero,
	leoRead,
	leoWrite,
	leoSeek,
	leoStart_stop,
	leoRd_capacity,
	leoTranslate,
	leoMode_sel,
	leoReadDiskId,
};

void leomain(void *arg)
{
	u32 stat, sense;
	LEO_country_code.u8_data[0] = *(u8 *)PHYS_TO_K1(0x00000010);
	LEO_country_code.u8_data[1] = *(u8 *)PHYS_TO_K1(0x00000090);
	LEO_country_code.u8_data[2] = *(u8 *)PHYS_TO_K1(0x00000110);
	LEO_country_code.u8_data[3] = *(u8 *)PHYS_TO_K1(0x00000190);
	LEOasic_seq_ctl_shadow = 0;
	LEOasic_bm_ctl_shadow = 0;
	LEOdrive_flag = 0;
	LEOclr_que_flag = 0;
	LEOPiInfo = osLeoDiskInit();
	LEOPiDmaParam.hdr.pri = OS_MESG_PRI_HIGH;
	LEOPiDmaParam.hdr.retQueue = &LEOdma_que;
	osEPiReadIo(LEOPiInfo, ASIC_STATUS, &stat);
	if (!(stat & 0x00400000))
	{
		if (stat & (0x00800000|0x02000000|0x04000000))
		{
			osEPiWriteIo(LEOPiInfo, ASIC_HARD_RESET, 0xAAAA0000);
		}
	}
	for (;;)
	{
		osRecvMesg(&LEOcommand_que, (OSMesg *)&LEOcur_command, OS_MESG_BLOCK);
		if (cmd_hdr->command > LEO_COMMAND_READ_DISK_ID || cmd_hdr->command == 0)
		{
			cmd_hdr->sense = LEO_SENSE_INVALID_COMMAND_OPERATION_CODE;
			cmd_hdr->status = 0x81;
			continue;
		}
		osEPiReadIo(LEOPiInfo, ASIC_STATUS, &stat);
		sense = leoChk_asic_ready(0x00010001, stat);
		if (cmd_hdr->command == LEO_COMMAND_TEST_UNIT_READY)
		{
			test_cmd->test = leoChk_cur_drvmode(stat);
		}
		if (sense != LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION)
		{
			switch (sense)
			{
			case LEO_SENSE_DEVICE_COMMUNICATION_FAILURE:
				cmd_hdr->sense = sense;
				cmd_hdr->status = 0x83;
				goto post_exe;
			case LEO_SENSE_MEDIUM_NOT_PRESENT:
				if (cmd_hdr->command == LEO_COMMAND_MODE_SELECT) break;
			default:
				if (cmd_hdr->command == LEO_COMMAND_INQUIRY) break;
				cmd_hdr->sense = sense;
				cmd_hdr->status = LEO_STATUS_CHECK_CONDITION;
				goto post_exe;
			}
		}
		if (LEOdrive_flag == 0)
		{
			switch (cmd_hdr->command)
			{
			case LEO_COMMAND_INQUIRY:
			case LEO_COMMAND_TEST_UNIT_READY:
			case LEO_COMMAND_MODE_SELECT:
				break;
			default:
				if (LEO_country_code.u32_data == 0)
				{
					osEPiReadIo(LEOPiInfo, ASIC_ID_REG, &stat);
					if ((stat & (7 << 16)) != (4 << 16)) for (;;);
				}
				if (leoRead_system_area())
				{
					cmd_hdr->status = LEO_STATUS_CHECK_CONDITION;
					goto post_exe;
				}
				if (leoSend_asic_cmd_w(0x000B0001, LEO_sys_data.param.disk_type << 16))
				{
					cmd_hdr->status = LEO_STATUS_CHECK_CONDITION;
					goto post_exe;
				}
				if ((LEO_sys_data.param.disk_type & 0xF0) != 0x10)
				{
					goto invalid_disktype;
				}
				LEOdisk_type = LEO_sys_data.param.disk_type & 0x0F;
				if (LEOdisk_type >= 7)
				{
invalid_disktype:
					cmd_hdr->sense = LEO_SENSE_INCOMPATIBLE_MEDIUM_INSTALLED;
					cmd_hdr->status = LEO_STATUS_CHECK_CONDITION;
					goto post_exe;
				}
				LEOdrive_flag = 0xFF;
			}
		}
		cmd_tbl[cmd_hdr->command]();
post_exe:
		if (cmd_hdr->control & LEO_CONTROL_POST) osSendMesg(*(OSMesgQueue **)(
			(char *)LEOcur_command + leo_rodata_804B23A4[cmd_hdr->command]
		), LEOcur_command, OS_MESG_BLOCK);
		if (LEOclr_que_flag) leoClr_queue();
	}
}

static LEOCmdRead system_read_cmd =
	{{LEO_COMMAND_READ, 0, 0, 0, 0, 0, 0, 0}, 12, 1, NULL, 0, 0};

static const u8 system_lba[] = {0, 1, 8, 9};

static u8 leoRead_system_area(void)
{
	LEOCmdRead command;
	void *backup;
	u8 retry_cntr;
	backup = LEOcur_command;
	LEOcur_command = &command;
	LEOdisk_type = 0;
	retry_cntr = 64;
	do
	{
		LEOrw_flags = 0x3000;
		LEO_sys_data.param.defect_num[0] = 0;
		command = system_read_cmd;
		command.lba = 12;
		command.buff_ptr = &LEO_sys_data;
		leoRead_common(0);
		switch (command.header.sense)
		{
		case LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION:
			do {} while (LEO_country_code.u32_data != 0);
			goto sys_read;
		case LEO_SENSE_UNRECOVERED_READ_ERROR:
			do {} while (LEO_country_code.u32_data == 0);
			goto sys_read;
		}
	}
	while (--retry_cntr);
	goto sys_read_end;
sys_read:
	retry_cntr = 64;
	do
	{
		LEO_sys_data.param.defect_num[0] = 0;
		command = system_read_cmd;
		command.buff_ptr = &LEO_sys_data;
		command.lba = system_lba[retry_cntr & 3];
		if (LEO_country_code.u32_data == 0) command.lba += 2;
		LEOrw_flags = 0x3000;
		leoRead_common(0);
		if (command.header.status == LEO_STATUS_GOOD)
		{
			do {} while (LEO_sys_data.param.country != LEO_country_code.u32_data);
			break;
		}
	}
	while (--retry_cntr);
sys_read_end:
	LEOcur_command = backup;
	return cmd_hdr->sense = command.header.sense;
}
