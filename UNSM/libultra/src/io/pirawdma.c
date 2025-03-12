#include <ultra64.h>
#include "osint.h"

s32 osPiRawStartDma(s32 direction, u32 devAddr, void *dramAddr, u32 size)
{
	register u32 stat;
#ifdef _DEBUG
	if (direction != OS_READ && direction != OS_WRITE)
	{
		__osError(ERR_OSPIRAWSTARTDMA_DIR, 1, direction);
		return -1;
	}
	if (devAddr & 0x1)
	{
		__osError(ERR_OSPIRAWSTARTDMA_DEVADDR, 1, devAddr);
		return -1;
	}
	if ((u32)dramAddr & 0x7)
	{
		__osError(ERR_OSPIRAWSTARTDMA_ADDR, 1, dramAddr);
		return -1;
	}
	if (size & 0x1)
	{
		__osError(ERR_OSPIRAWSTARTDMA_SIZE, 1, size);
		return -1;
	}
	if (size == 0 || size > 0x1000000)
	{
		__osError(ERR_OSPIRAWSTARTDMA_RANGE, 1, size);
		return -1;
	}
#endif
	stat = IO_READ(PI_STATUS_REG);
	while (stat & (PI_STATUS_IO_BUSY|PI_STATUS_DMA_BUSY))
	{
		stat = IO_READ(PI_STATUS_REG);
	}
	IO_WRITE(PI_DRAM_ADDR_REG, osVirtualToPhysical(dramAddr));
	IO_WRITE(PI_CART_ADDR_REG, K1_TO_PHYS((u32)osRomBase|devAddr));
	switch (direction)
	{
	case OS_READ:
		IO_WRITE(PI_WR_LEN_REG, size-1);
		break;
	case OS_WRITE:
		IO_WRITE(PI_RD_LEN_REG, size-1);
		break;
	default:
		return -1;
	}
	return 0;
}
