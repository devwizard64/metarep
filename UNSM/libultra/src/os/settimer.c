#include <ultra64.h>
#include "osint.h"
#include "viint.h"

int osSetTimer(
	OSTimer *t, OSTime value, OSTime interval, OSMesgQueue *mq, OSMesg msg
)
{
	OSTime tim;
#ifdef _DEBUG
	if (!__osViDevMgr.active)
	{
		__osError(ERR_OSSETTIMER, 0);
		return 0;
	}
#endif
	t->next = NULL;
	t->prev = NULL;
	t->interval = interval;
	t->value = value ? value : interval;
	t->mq = mq;
	t->msg = msg;
	tim = __osInsertTimer(t);
	if (__osTimerList->next == t) __osSetTimerIntr(tim);
	return 0;
}
