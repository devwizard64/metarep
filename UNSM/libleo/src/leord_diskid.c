#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

static LEOCmdRead read_id_cmd =
	{{LEO_COMMAND_READ, 0, 0, 0, 0, 0, 0, 0}, 14, 1, LEO_TempBuffer, 0};

static const u8 leo_disk_id_lba[] = {14, 15};

void leoReadDiskId(void)
{
	LEOCmdRead command;
	u8 *ptr;
	unsigned int i;
	ptr = LEOcur_command;
	LEOcur_command = &command;
	for (i = 0; i < 2; i++)
	{
		LEOrw_flags = 0x2000;
		command = read_id_cmd;
		command.lba = leo_disk_id_lba[i];
		leoRead_common(0);
		if (command.header.sense != LEO_SENSE_UNRECOVERED_READ_ERROR) break;
	}
	LEOcur_command = ptr;
	ptr = diskid_cmd->buffer_pointer;
	for (i = 0; i < 32; i += sizeof(int))
	{
		*(int *)ptr = *(int *)&LEO_TempBuffer[i];
		ptr += sizeof(int);
	}
	diskid_cmd->header.sense = command.header.sense;
	diskid_cmd->header.status = command.header.status;
}
