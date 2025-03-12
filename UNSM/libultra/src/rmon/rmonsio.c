#include <ultra64.h>
#include <PR/rdb.h>
#include "osint.h"
#include "rmonint.h"

#ifndef _FINALROM

static OSMesgQueue IOmq;
static OSMesg IOmsgs;

u8 *__osRdb_DbgRead_Buf;
u8 rmonRdbReadBuf[RMON_DBG_BUF_SIZE];

void __rmonSendFault(OSThread *thread)
{
	volatile float f;
	u8 *tPtr;
	u32 sent = 0;
	f = 0;
	tPtr = (u8 *)thread;
	while (sent < sizeof(OSThread)) sent += __osRdbSend(
		&tPtr[sent], sizeof(OSThread)-sent, RDB_TYPE_GtoH_FAULT
	);
}

void __rmonIOflush(void)
{
	int sent = 0;
	unsigned char tstr[4];
	while (sent < 1) sent += __osRdbSend(tstr, 1, RDB_TYPE_GtoH_DEBUG_DONE);
}

void __rmonIOputw(u32 word)
{
	int sent = 0;
	unsigned char *cPtr = (unsigned char *)&word;
	while (sent < 4)
	{
		sent += __osRdbSend(&cPtr[sent], 4-sent, RDB_TYPE_GtoH_DEBUG);
	}
}

void __rmonIOhandler(void)
{
	int sent;
	unsigned char tstr[4];
	osCreateMesgQueue(&IOmq, &IOmsgs, 1);
	osSetEventMesg(OS_EVENT_RDB_DBG_DONE, &IOmq, (OSMesg)0);
	__osRdb_DbgRead_Buf = rmonRdbReadBuf;
	for (;;)
	{
		osRecvMesg(&IOmq, NULL, OS_MESG_BLOCK);
		__rmonExecute((KKHeader *)rmonRdbReadBuf);
		__osRdb_DbgRead_Buf = rmonRdbReadBuf;
		sent = 0;
		while (sent < 1)
		{
			sent += __osRdbSend(tstr, 1, RDB_TYPE_GtoH_DEBUG_READY);
		}
	}
}

#endif
