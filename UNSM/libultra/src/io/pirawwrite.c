#include <ultra64.h>
#include "osint.h"

s32 osPiRawWriteIo(u32 devAddr, u32 data)
{
	register u32 stat;
#ifdef _DEBUG
	if (devAddr & 0x3)
	{
		__osError(ERR_OSPIRAWWRITEIO, 1, devAddr);
		return -1;
	}
#endif
	stat = IO_READ(PI_STATUS_REG);
	while (stat & (PI_STATUS_IO_BUSY|PI_STATUS_DMA_BUSY))
	{
		stat = IO_READ(PI_STATUS_REG);
	}
	IO_WRITE((u32)osRomBase|devAddr, data);
	return 0;
}
