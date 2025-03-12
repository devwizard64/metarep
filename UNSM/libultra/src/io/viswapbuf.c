#include <ultra64.h>
#include <assert.h>
#include "osint.h"
#include "viint.h"
















































void osViSwapBuffer(void *frameBufPtr)
{
	u32 saveMask;
#ifdef _DEBUG
	if (!__osViDevMgr.active)
	{
		__osError(ERR_OSVISWAPBUFFER_VIMGR, 0);
		return;
	}
	assert(frameBufPtr != NULL);
	if ((u32)frameBufPtr & 0x3F)
	{
		__osError(ERR_OSVISWAPBUFFER_ADDR, 1, frameBufPtr);
		return;
	}
#endif
	saveMask = __osDisableInt();
	__osViNext->framep = frameBufPtr;
	__osViNext->state |= VI_STATE_FRAME;
	__osRestoreInt(saveMask);
}
