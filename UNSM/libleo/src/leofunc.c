#include <ultra64.h>
#include <PR/leoappli.h>
#include "leoint.h"

extern void leoClr_queue(void);

extern void leomain(void *arg);
extern void leointerrupt(void *arg);

void leoInitialize(OSPri compri, OSPri intpri)
{
	leo_bss_804E21F8 = compri;
	leo_bss_804E21FC = OS_PRIORITY_PIMGR;
	osCreateMesgQueue(&LEOcommand_que, LEOcommand_que_buf, 8);
	osCreateMesgQueue(&LEOcontrol_que, &LEOcontrol_que_buf, 1);
	osCreateMesgQueue(&LEOevent_que, &LEOevent_que_buf, 1);
	osCreateMesgQueue(&LEOdma_que, LEOdma_que_buf, 2);
	osCreateMesgQueue(&LEOblock_que, &LEOblock_que_buf, 1);
	osCreateThread(
		&LEOcommandThread, 1, leomain, NULL,
		LEOcommandThreadStack + LEO_STACKSIZE/8, compri
	);
	osStartThread(&LEOcommandThread);
	osCreateThread(
		&LEOinterruptThread, 1, leointerrupt, NULL,
		LEOinterruptThreadStack + LEO_STACKSIZE/8, intpri
	);
	osStartThread(&LEOinterruptThread);
	osSetEventMesg(OS_EVENT_CART, &LEOevent_que, (OSMesg)0x00030000);
	osSendMesg(&LEOblock_que, (OSMesg)0, OS_MESG_NOBLOCK);
}

#define hdr ((LEOCmdHeader *)cmd)

void leoCommand(void *cmd)
{
	osRecvMesg(&LEOblock_que, NULL, OS_MESG_BLOCK);
	hdr->status = 0x00;
	hdr->sense = LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
	switch (hdr->command)
	{
	case LEO_COMMAND_CLEAR_QUE:
		LEOclr_que_flag = 0xFF;
		leoClr_queue();
		LEOclr_que_flag = 0;
		hdr->status = LEO_STATUS_GOOD;
		break;
	case LEO_COMMAND_READ:
	case LEO_COMMAND_WRITE:
		((LEOCmdWrite *)cmd)->rw_bytes = 0;
	default:
		if (osSendMesg(&LEOcommand_que, cmd, OS_MESG_NOBLOCK))
		{
			hdr->status = 0x80;
		}
	}
	osSendMesg(&LEOblock_que, (OSMesg)0, OS_MESG_BLOCK);
}
