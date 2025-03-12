#include <ultra64.h>
#include <PR/rdb.h>
#include "osint.h"

#ifndef _FINALROM

static u32 __osLogOKtoWrite = 1;
static u32 __osLogInitialized = 0;

static OSMesgQueue __osLogDoneMsgQ;
static OSMesg __osLogMsgBuf;

void osCreateLog(OSLog *log, u32 *base, s32 byteLen)
{
	log->magic = OS_LOG_MAGIC;
	log->base = base;
	log->len = byteLen;
	log->startCount = osGetCount();
	log->writeOffset = 0;
}

void osLogEvent(OSLog *log, s16 code, s16 numArgs, ...)
{
	va_list argPtr;
	if (numArgs > OS_LOG_MAX_ARGS) return;
	va_start(argPtr, numArgs);
	__osLogWrite(log, code, numArgs, argPtr);
	va_end(argPtr);
}

void osFlushLog(OSLog *log)
{
	u32 mask;
	u32 sent;
	u32 count, subcount;
	u8 *base;
	u8 dCount[3];
	if (!__osLogInitialized)
	{
		osCreateMesgQueue(&__osLogDoneMsgQ, &__osLogMsgBuf, 1);
		osSetEventMesg(OS_EVENT_RDB_LOG_DONE, &__osLogDoneMsgQ, (OSMesg)0);
		__osLogInitialized = 1;
	}
	mask = __osDisableInt();
	__osLogOKtoWrite = 0;
	base = (u8 *)log->base;
	count = 4*log->writeOffset;
	__osRestoreInt(mask);
	while (count)
	{
		subcount = MIN(count, RDB_LOG_MAX_BLOCK_SIZE);
		dCount[0] = (subcount & 0xFF0000) >> 16;
		dCount[1] = (subcount & 0x00FF00) >>  8;
		dCount[2] = (subcount & 0x0000FF) >>  0;
		sent = 0;
		while (sent < 3)
		{
			sent += __osRdbSend(&dCount[sent], 3-sent, RDB_TYPE_GtoH_LOG_CT);
		}
		sent = 0;
		while (sent < subcount)
		{
			sent += __osRdbSend(&base[sent], subcount-sent, RDB_TYPE_GtoH_LOG);
		}
		count -= subcount;
		base += subcount;
		osRecvMesg(&__osLogDoneMsgQ, NULL, OS_MESG_BLOCK);
	}
	mask = __osDisableInt();
	log->writeOffset = 0;
	__osLogOKtoWrite = 1;
	__osRestoreInt(mask);
}

void __osLogWrite(OSLog *log, s16 code, s16 numArgs, va_list argPtr)
{
	int i;
	u32 saveEnable;
	u32 buf[sizeof(OSLogItem)/4 + OS_LOG_MAX_ARGS];
	u32 *bufp = buf;
	OSLogItem *hdr = (OSLogItem *)buf;
	u32 *args = &buf[sizeof(OSLogItem)/4];
	u32 *dest;
	int numLongs = numArgs + sizeof(OSLogItem)/4;
	saveEnable = __osDisableInt();
	hdr->magic = log->magic;
	hdr->timeStamp = osGetCount() - log->startCount;
	hdr->argCount = numArgs;
	hdr->eventID = code;
	for (i = 0; i < numArgs; i++) *args++ = va_arg(argPtr, u32);
	if (__osLogOKtoWrite)
	{
		if (log->writeOffset+numLongs < log->len/4)
		{
			dest = log->base + log->writeOffset;
			for (i = 0; i < numLongs; i++) *dest++ = *bufp++;
			log->writeOffset += numLongs;
		}
		else
		{
			__osLogOKtoWrite = 0;
		}
	}
	__osRestoreInt(saveEnable);
}

#endif
