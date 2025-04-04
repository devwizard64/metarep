#include <ultra64.h>
#include <PR/rdb.h>
#include "osint.h"

#ifndef _FINALROM
extern rdbPacket *__osRdb_IP6_Data;
extern u32 __osRdb_IP6_Size;
extern u32 __osRdb_IP6_Ct;
extern u32 __osRdb_IP6_CurWrite;

u32 __osRdb_IP6_Empty = 1;

u32 __osRdbSend(u8 *buf, u32 size, u32 type)
{
	rdbPacket *pPtr, pkt;
	u32 len, c, inCt = 0;
	u32 needFirst = 0;
	u32 mask;
	u32 sent = 0;
	mask = __osDisableInt();
	if (__osRdb_IP6_Empty)
	{
		__osRdb_IP6_Empty = 0;
		pkt.type = type;
		len = MIN(size, 3);
		pkt.length = len;
		c = 0;
		while (c < len) pkt.buf[c++] = buf[inCt++];
		size -= len;
		sent = len;
		needFirst = 1;
	}
	while (size > 0 && __osRdb_IP6_Ct < __osRdb_IP6_Size)
	{
		len = MIN(size, 3);
		pPtr = &__osRdb_IP6_Data[__osRdb_IP6_CurWrite];
		pPtr->type = type;
		pPtr->length = len;
		c = 0;
		while (c < len) pPtr->buf[c++] = buf[inCt++];
		__osRdb_IP6_CurWrite++;
		if (__osRdb_IP6_CurWrite >= __osRdb_IP6_Size) __osRdb_IP6_CurWrite = 0;
		__osRdb_IP6_Ct++;
		size -= len;
		sent += len;
	}
	if (needFirst) *(u32 *)RDB_BASE_REG = *(u32 *)&pkt;
	__osRestoreInt(mask);
	return sent;
}
#endif
