#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

void leoReset(void)
{
}

#define hdr ((LEOCmdHeader *)cmd)

void leoClr_queue(void)
{
	OSMesg cmd;
	while (!osRecvMesg(&LEOcommand_que, &cmd, OS_MESG_NOBLOCK))
	{
		hdr->sense = LEO_SENSE_COMMAND_TERMINATED;
		hdr->status = 0x04;
	}
}
