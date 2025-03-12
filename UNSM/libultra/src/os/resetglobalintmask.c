#include <ultra64.h>
#include "osint.h"

void __osResetGlobalIntMask(OSHWIntr interrupt)
{
	register u32 saveMask;
	saveMask = __osDisableInt();
	__OSGlobalIntMask &= ~(interrupt & ~0x00000401);
	__osRestoreInt(saveMask);
}
