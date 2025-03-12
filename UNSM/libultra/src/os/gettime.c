#include <ultra64.h>
#include "osint.h"
#include "viint.h"

OSTime osGetTime(void)
{
	u32 CurrentCount;
	u32 elapseCount;
	OSTime tmptime;
	register u32 savedMask;
#ifdef _DEBUG
	if (!__osViDevMgr.active)
	{
		__osError(ERR_OSGETTIME, 0);
		return 0;
	}
#endif
	savedMask = __osDisableInt();
	CurrentCount = osGetCount();
	elapseCount = CurrentCount - __osBaseCounter;
	tmptime = __osCurrentTime;
	__osRestoreInt(savedMask);
	return tmptime + elapseCount;
}
