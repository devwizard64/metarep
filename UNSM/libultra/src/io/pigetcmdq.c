#include <ultra64.h>

extern OSDevMgr __osPiDevMgr;

OSMesgQueue *osPiGetCmdQueue(void)
{
	if (!__osPiDevMgr.active) return NULL;
	else return __osPiDevMgr.cmdQueue;
}
