#include <ultra64.h>
#ifdef sgi
#include <bstring.h>
#else
#include <string.h>
#endif
#include "osint.h"
#include "piint.h"

OSPiHandle __LeoDiskHandle;
OSPiHandle *__osDiskHandle;

OSPiHandle *osLeoDiskInit(void)
{
	u32 saveMask;
	__LeoDiskHandle.type = DEVICE_TYPE_64DD;
	__LeoDiskHandle.baseAddress = PHYS_TO_K1(PI_DOM2_ADDR1);
	__LeoDiskHandle.latency = 3;
	__LeoDiskHandle.pulse = 6;
	__LeoDiskHandle.pageSize = 6;
	__LeoDiskHandle.relDuration = 2;
#if REVISION >= 199707
	__LeoDiskHandle.domain = 1;
#endif
	IO_WRITE(PI_BSD_DOM2_LAT_REG, __LeoDiskHandle.latency);
	IO_WRITE(PI_BSD_DOM2_PWD_REG, __LeoDiskHandle.pulse);
	IO_WRITE(PI_BSD_DOM2_PGS_REG, __LeoDiskHandle.pageSize);
	IO_WRITE(PI_BSD_DOM2_RLS_REG, __LeoDiskHandle.relDuration);
	bzero(&__LeoDiskHandle.transferInfo, sizeof(__OSTranxInfo));
	saveMask = __osDisableInt();
	__LeoDiskHandle.next = __osPiTable;
	__osPiTable = &__LeoDiskHandle;
	__osDiskHandle = &__LeoDiskHandle;
	__osRestoreInt(saveMask);
	return &__LeoDiskHandle;
}
