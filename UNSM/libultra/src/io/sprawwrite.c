#include <ultra64.h>
#include <assert.h>
#include "osint.h"












































s32 __osSpRawWriteIo(u32 devAddr, u32 data)
{
#ifdef _DEBUG
	assert((devAddr & 0x3) == 0);
#endif
	if (__osSpDeviceBusy()) return -1;
	IO_WRITE(devAddr, data);
	return 0;
}
