#include <ultra64.h>
#include "osint.h"

void osCreateMesgQueue(OSMesgQueue *mq, OSMesg *msg, s32 msgCount)
{
#ifdef _DEBUG
	if (msgCount <= 0)
	{
		__osError(ERR_OSCREATEMESGQUEUE, 1, msgCount);
		return;
	}
#endif
	mq->mtqueue = (OSThread *)&__osThreadTail;
	mq->fullqueue = (OSThread *)&__osThreadTail;
	mq->validCount = 0;
	mq->first = 0;
	mq->msgCount = msgCount;
	mq->msg = msg;
}
