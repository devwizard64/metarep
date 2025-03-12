#include <ultra64.h>
#include "osint.h"

void osStopThread(OSThread *t)
{
	register u32 saveMask;
	register u16 state;
	saveMask = __osDisableInt();
	state = !t ? OS_STATE_RUNNING : t->state;
	switch (state)
	{
	case OS_STATE_RUNNING:
		__osRunningThread->state = OS_STATE_STOPPED;
		__osEnqueueAndYield(NULL);
		break;
	case OS_STATE_RUNNABLE:
	case OS_STATE_WAITING:
		t->state = OS_STATE_STOPPED;
		__osDequeueThread(t->queue, t);
		break;
	}
	__osRestoreInt(saveMask);
}
