#include <ultra64.h>
#include "osint.h"
#include "controller.h"
#include "siint.h"

s32 osContSetCh(u8 ch)
{
	s32 ret = 0;
	__osSiGetAccess();
	if (ch > MAXCONTROLLERS)    __osMaxControllers = MAXCONTROLLERS;
	else                        __osMaxControllers = ch;
	__osContLastCmd = CONT_SETCH;
	__osSiRelAccess();
	return ret;
}
