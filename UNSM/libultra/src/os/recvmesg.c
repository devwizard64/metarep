#include <ultra64.h>
#include "osint.h"

s32 osRecvMesg(OSMesgQueue *mq, OSMesg *msg, s32 flags)
{
	register u32 saveMask;
#ifdef _DEBUG
	if (flags != OS_MESG_NOBLOCK && flags != OS_MESG_BLOCK)
	{
		__osError(ERR_OSRECVMESG, 1, flags);
		return -1;
	}
#endif
	saveMask = __osDisableInt();
	while (MQ_IS_EMPTY(mq))
	{
		if (flags == OS_MESG_NOBLOCK)
		{
			__osRestoreInt(saveMask);
			return -1;
		}
		else
		{
			__osRunningThread->state = OS_STATE_WAITING;
			__osEnqueueAndYield(&mq->mtqueue);
		}
	}
	if (msg) *msg = mq->msg[mq->first];
	mq->first = (mq->first+1) % mq->msgCount;
	mq->validCount--;
	if (mq->fullqueue->next) osStartThread(__osPopThread(&mq->fullqueue));
	__osRestoreInt(saveMask);
	return 0;
}
