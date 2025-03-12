#include <ultra64.h>
#include "osint.h"

void osSetThreadPri(OSThread *t, OSPri p)
{
	register u32 saveMask;
#ifdef _DEBUG
	if (p < OS_PRIORITY_IDLE || p > OS_PRIORITY_MAX)
	{
		__osError(ERR_OSSETTHREADPRI, 1, p);
		return;
	}
#endif
	saveMask = __osDisableInt();
	if (!t) t = __osRunningThread;
	if (t->priority != p)
	{
		t->priority = p;
		if (t != __osRunningThread && t->state != OS_STATE_STOPPED)
		{
			__osDequeueThread(t->queue, t);
			__osEnqueueThread(t->queue, t);
		}
		if (__osRunningThread->priority < __osRunQueue->priority)
		{
			__osRunningThread->state = OS_STATE_RUNNABLE;
			__osEnqueueAndYield(&__osRunQueue);
		}
	}
	__osRestoreInt(saveMask);
}
