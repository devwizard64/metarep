#include <ultra64.h>
#include <PR/rdb.h>
#include "osint.h"

#ifndef _FINALROM
static int readHostInitialized = 0;
static OSMesgQueue readHostMesgQueue;
static OSMesg readHostMesgBuf[1];

u8 *__osRdb_Read_Data_Buf;
u32 __osRdb_Read_Data_Ct;

void osReadHost(void *dramAddr, u32 nbytes)
{
	unsigned char tstr[4];
	u32 sent = 0;
	if (!readHostInitialized)
	{
		osCreateMesgQueue(&readHostMesgQueue, readHostMesgBuf, 1);
		osSetEventMesg(OS_EVENT_RDB_READ_DONE, &readHostMesgQueue, (OSMesg)0);
		readHostInitialized = 1;
	}
	__osRdb_Read_Data_Buf = dramAddr;
	__osRdb_Read_Data_Ct = nbytes;
	while (sent < 1) sent += __osRdbSend(tstr, 1, RDB_TYPE_GtoH_READY_FOR_DATA);
	osRecvMesg(&readHostMesgQueue, NULL, OS_MESG_BLOCK);
	return;
}
#endif
