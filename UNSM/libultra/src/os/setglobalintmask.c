#include <ultra64.h>
#include "osint.h"

void __osSetGlobalIntMask(OSHWIntr interrupt)
{
	register u32 saveMask;
	saveMask = __osDisableInt();
	__OSGlobalIntMask |= interrupt;
	__osRestoreInt(saveMask);
}
