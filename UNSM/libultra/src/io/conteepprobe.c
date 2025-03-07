#include <ultra64.h>
#include "controller.h"
#include "siint.h"

s32 osEepromProbe(OSMesgQueue *mq)
{
	s32 ret = 0;
	OSContStatus sdata;
	__osSiGetAccess();
	ret = __osEepStatus(mq, &sdata);
	if (!ret && (sdata.type & CONT_EEPROM)) ret = 1;
	else                                    ret = 0;
	__osSiRelAccess();
	return ret;
}
