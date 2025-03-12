#include <ultra64.h>
#include <PR/rdb.h>
#include "osint.h"

#ifndef _FINALROM
rdbPacket *__osRdb_IP6_Data;
u32 __osRdb_IP6_Size;
u32 __osRdb_IP6_Ct;
u32 __osRdb_IP6_CurWrite;
u32 __osRdb_IP6_CurSend;

void __osInitRdb(u8 *sendBuf, u32 sendSize)
{
	u32 mask;
	sendSize /= 4;
	if ((u32)sendBuf & 0x3)
	{
		sendBuf = (u8 *)((u32)sendBuf & 0x3) + 4;
		sendSize--;
	}
	mask = __osDisableInt();
	__osRdb_IP6_Data = (rdbPacket *)sendBuf;
	__osRdb_IP6_Size = sendSize;
	__osRdb_IP6_Ct = 0;
	__osRdb_IP6_CurWrite = 0;
	__osRdb_IP6_CurSend = 0;
	__osRestoreInt(mask);
}
#endif
