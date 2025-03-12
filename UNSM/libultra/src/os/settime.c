#include <ultra64.h>
#include "osint.h"
#include "viint.h"

void osSetTime(OSTime ticks)
{
#ifdef _DEBUG
	if (!__osViDevMgr.active)
	{
		__osError(ERR_OSSETTIME, 0);
		return;
	}
#endif
	__osCurrentTime = ticks;
}
