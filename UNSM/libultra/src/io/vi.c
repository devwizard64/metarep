#include <ultra64.h>
#ifdef sgi
#include <bstring.h>
#else
#include <string.h>
#endif
#include "viint.h"

static __OSViContext vi[2] = {0};
__OSViContext *__osViCurr = &vi[0];
__OSViContext *__osViNext = &vi[1];
#if REVISION >= 199611
#elif REVISION >= 199609
u32 osViTvType = OS_TV_NTSC; /* unofficial name */
#else
u32 osViNtscEnabled = TRUE;
#endif
u32 osViClock = VI_NTSC_CLOCK;

void __osViInit(void)
{
#if REVISION >= 199609 && REVISION < 199611
	osViTvType = osTvType;
#endif
	bzero(&vi, sizeof(vi));
	__osViCurr = &vi[0];
	__osViNext = &vi[1];
	__osViNext->retraceCount = 1;
	__osViCurr->retraceCount = 1;
#if REVISION >= 199707
	__osViNext->framep = (void *)K0BASE;
	__osViCurr->framep = (void *)K0BASE;
	if      (osTvType == OS_TV_PAL)     __osViNext->modep = &osViModePalLan1;
	else if (osTvType == OS_TV_MPAL)    __osViNext->modep = &osViModeMpalLan1;
	else                                __osViNext->modep = &osViModeNtscLan1;
#elif REVISION >= 199611
	if (osTvType == OS_TV_PAL)
	{
		__osViNext->modep = &osViModePalLan1;
		osViClock = VI_PAL_CLOCK;
	}
	else if (osTvType == OS_TV_MPAL)
	{
		__osViNext->modep = &osViModeMpalLan1;
		osViClock = VI_MPAL_CLOCK;
	}
	else
	{
		__osViNext->modep = &osViModeNtscLan1;
		osViClock = VI_NTSC_CLOCK;
	}
#elif REVISION >= 199609
	if (osViTvType == OS_TV_NTSC)
	{
		__osViNext->modep = &osViModeNtscLan1;
		osViClock = VI_NTSC_CLOCK;
	}
	else
	{
		__osViNext->modep = &osViModePalLan1;
		osViClock = VI_MPAL_CLOCK;
	}
#else
	if (osViNtscEnabled)
	{
		__osViNext->modep = &osViModeNtscLan1;
		osViClock = VI_NTSC_CLOCK;
	}
	else
	{
		__osViNext->modep = &osViModePalLan1;
		osViClock = VI_PAL_CLOCK;
	}
#endif
	__osViNext->state = VI_STATE_BLACK;
	__osViNext->control = __osViNext->modep->comRegs.ctrl;
#if REVISION >= 199609
	while (IO_READ(VI_CURRENT_REG) > 10);
	IO_WRITE(VI_CONTROL_REG, 0);
#endif
	__osViSwapContext();
}
