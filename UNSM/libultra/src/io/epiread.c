#include <ultra64.h>
#include "osint.h"
#include "piint.h"

s32 osEPiReadIo(OSPiHandle *pihandle, u32 devAddr, u32 *data)
{
	register s32 ret;
#ifdef _DEBUG
	if (devAddr & 0x3)
	{
		__osError(ERR_OSPIREADIO, 1, devAddr);
		return -1;
	}
#endif
	__osPiGetAccess();
	ret = osEPiRawReadIo(pihandle, devAddr, data);
	__osPiRelAccess();
	return ret;
}
