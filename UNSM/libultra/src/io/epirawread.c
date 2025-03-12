#include <ultra64.h>
#include <assert.h>
#include "osint.h"




























s32 osEPiRawReadIo(OSPiHandle *pihandle, u32 devAddr, u32 *data)
{
	register u32 stat;
#ifdef _DEBUG
	if (devAddr & 0x3)
	{
		__osError(ERR_OSPIRAWREADIO, 1, devAddr);
		return -1;
	}
	assert(data != NULL);
#endif
	stat = IO_READ(PI_STATUS_REG);
	while (stat & (PI_STATUS_IO_BUSY|PI_STATUS_DMA_BUSY))
	{
		stat = IO_READ(PI_STATUS_REG);
	}
	*data = IO_READ((u32)pihandle->baseAddress|devAddr);
	return 0;
}
