#include <ultra64.h>
#include "osint.h"

s32 osAiSetNextBuffer(void *bufPtr, u32 size)
{
	static u8 hdwrBugFlag = 0;
	void *bPtr;
#ifdef _DEBUG
	if ((u32)bufPtr & 0x7)
	{
		__osError(ERR_OSAISETNEXTBUFFER_ADDR, 1, bufPtr);
		return -1;
	}
	if (size & 0x7)
	{
		__osError(ERR_OSAISETNEXTBUFFER_SIZE, 1, size);
		return -1;
	}
#endif
	bPtr = bufPtr;
	if (hdwrBugFlag) bPtr = (char *)bufPtr-0x2000;
	if ((((u32)bufPtr+size) & 0x3FFF) == 0x2000) hdwrBugFlag = 1;
	else hdwrBugFlag = 0;
	if (__osAiDeviceBusy()) return -1;
	IO_WRITE(AI_DRAM_ADDR_REG, osVirtualToPhysical(bPtr));
	IO_WRITE(AI_LEN_REG, size);
	return 0;
}
