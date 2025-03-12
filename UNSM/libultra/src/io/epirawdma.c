#include <ultra64.h>
#include "osint.h"
#include "piint.h"

s32 osEPiRawStartDma(
	OSPiHandle *pihandle, s32 direction, u32 devAddr, void *dramAddr, u32 size
)
{
#if REVISION >= 199707
	u32 stat;
	u32 domain;
#else
	register u32 stat;
#endif
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
#if REVISION >= 199707
	domain = pihandle->domain;
	if (__osCurrentHandle[domain] != pihandle)
	{
		OSPiHandle *cHandle = __osCurrentHandle[domain];
		if (domain == 0)
		{
			if (cHandle->latency != pihandle->latency)
			{
				IO_WRITE(PI_BSD_DOM1_LAT_REG, pihandle->latency);
			}
			if (cHandle->pageSize != pihandle->pageSize)
			{
				IO_WRITE(PI_BSD_DOM1_PGS_REG, pihandle->pageSize);
			}
			if (cHandle->relDuration != pihandle->relDuration)
			{
				IO_WRITE(PI_BSD_DOM1_RLS_REG, pihandle->relDuration);
			}
			if (cHandle->pulse != pihandle->pulse)
			{
				IO_WRITE(PI_BSD_DOM1_PWD_REG, pihandle->pulse);
			}
		}
		else
		{
			if (cHandle->latency != pihandle->latency)
			{
				IO_WRITE(PI_BSD_DOM2_LAT_REG, pihandle->latency);
			}
			if (cHandle->pageSize != pihandle->pageSize)
			{
				IO_WRITE(PI_BSD_DOM2_PGS_REG, pihandle->pageSize);
			}
			if (cHandle->relDuration != pihandle->relDuration)
			{
				IO_WRITE(PI_BSD_DOM2_RLS_REG, pihandle->relDuration);
			}
			if (cHandle->pulse != pihandle->pulse)
			{
				IO_WRITE(PI_BSD_DOM2_PWD_REG, pihandle->pulse);
			}
		}
		__osCurrentHandle[domain] = pihandle;
	}
#endif
	IO_WRITE(PI_DRAM_ADDR_REG, osVirtualToPhysical(dramAddr));
	IO_WRITE(PI_CART_ADDR_REG, K1_TO_PHYS((u32)pihandle->baseAddress|devAddr));
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
