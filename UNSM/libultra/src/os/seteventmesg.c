#include <ultra64.h>
#include "osint.h"

__OSEventState __osEventStateTab[OS_NUM_EVENTS];

void osSetEventMesg(OSEvent e, OSMesgQueue *mq, OSMesg m)
{
	register u32 saveMask;
	__OSEventState *es;
#ifdef _DEBUG
	if (e >= OS_NUM_EVENTS)
	{
		__osError(ERR_OSSETEVENTMESG, 1, e);
		return;
	}
#endif
	saveMask = __osDisableInt();
	es = &__osEventStateTab[e];
	es->messageQueue = mq;
	es->message = m;
	__osRestoreInt(saveMask);
}
