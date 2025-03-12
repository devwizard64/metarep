#include <ultra64.h>
#ifdef sgi
#include <bstring.h>
#else
#include <string.h>
#endif
#include "osint.h"
#include "piint.h"

OSPiHandle __CartRomHandle;

OSPiHandle *osCartRomInit(void)
{
	u32 value = 0;
	u32 saveMask;
	if (__CartRomHandle.baseAddress == PHYS_TO_K1(PI_DOM1_ADDR2))
	{
		return &__CartRomHandle;
	}
	__CartRomHandle.type = DEVICE_TYPE_CART;
	__CartRomHandle.baseAddress = PHYS_TO_K1(PI_DOM1_ADDR2);
	osPiRawReadIo(0, &value);
	__CartRomHandle.latency = value & 0xFF;
	__CartRomHandle.pulse = value >> 8 & 0xFF;
	__CartRomHandle.pageSize = value >> 16 & 0xF;
	__CartRomHandle.relDuration = value >> 20 & 0xF;
	__CartRomHandle.domain = 0;
	bzero(&__CartRomHandle.transferInfo, sizeof(__OSTranxInfo));
	saveMask = __osDisableInt();
	__CartRomHandle.next = __osPiTable;
	__osPiTable = &__CartRomHandle;
	__osRestoreInt(saveMask);
	return &__CartRomHandle;
}
