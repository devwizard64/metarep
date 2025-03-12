#include <ultra64.h>
#include "osint.h"
#include "piint.h"

s32 osEPiWriteIo(OSPiHandle *pihandle, u32 devAddr, u32 data)
{
	register s32 ret;
#ifdef _DEBUG
	if (devAddr & 0x3)
	{
		__osError(ERR_OSPIWRITEIO, 1, devAddr);
		return -1;
	}
#endif
	__osPiGetAccess();
	ret = osEPiRawWriteIo(pihandle, devAddr, data);
	__osPiRelAccess();
	return ret;
}
