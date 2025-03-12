#include <ultra64.h>
#include "osint.h"

OSTime __osCurrentTime;
u32 __osBaseCounter;
u32 __osViIntrCount;
u32 __osTimerCounter;
OSTimer __osBaseTimer;
OSTimer *__osTimerList = &__osBaseTimer;
#ifndef _FINALROM
OSMesgQueue __osProfTimerQ;
OSProf *__osProfileList;
OSProf *__osProfileListEnd;
u32 __osProfileOverflowBin;
#endif

void __osTimerServicesInit(void)
{
	__osCurrentTime = 0;
	__osBaseCounter = 0;
	__osViIntrCount = 0;
	__osTimerList->next = __osTimerList->prev = __osTimerList;
	__osTimerList->interval = __osTimerList->value = 0;
	__osTimerList->mq = NULL;
	__osTimerList->msg = NULL;
}

void __osTimerInterrupt(void)
{
	OSTimer *t;
	u32 count, elapsed_cycles;
#ifndef _FINALROM
	u32 pc;
	s32 offset;
	OSProf *prof = __osProfileList;
#endif
	if (__osTimerList->next == __osTimerList) return;
	for (;;)
	{
		t = __osTimerList->next;
		if (t == __osTimerList)
		{
			__osSetCompare(0);
			__osTimerCounter = 0;
			break;
		}
		count = osGetCount();
		elapsed_cycles = count - __osTimerCounter;
		__osTimerCounter = count;
		if (elapsed_cycles < t->value)
		{
			t->value -= elapsed_cycles;
			__osSetTimerIntr(t->value);
			break;
		}
		t->prev->next = t->next;
		t->next->prev = t->prev;
		t->next = NULL;
		t->prev = NULL;
#ifdef _FINALROM
		if (t->mq) osSendMesg(t->mq, t->msg, OS_MESG_NOBLOCK);
#else
		if (t->mq)
		{
			if (t->mq != &__osProfTimerQ)
			{
				osSendMesg(t->mq, t->msg, OS_MESG_NOBLOCK);
			}
			else
			{
				pc = __osRunQueue->context.pc;
				for (prof = __osProfileList; prof < __osProfileListEnd; prof++)
				{
					offset = pc - (u32)prof->text_start;
					if (offset >= 0 && (s32)((u32)prof->text_end - pc) > 0)
					{
						++*(u16 *)((offset>>2) + prof->histo_base);
						goto __ProfDone;
					}
				}
				++__osProfileOverflowBin;
			}
		}
__ProfDone:
#endif
		if (t->interval)
		{
			t->value = t->interval;
			__osInsertTimer(t);
		}
	}
}

void __osSetTimerIntr(OSTime tim)
{
	OSTime NewTime;
	u32 savedMask;
	savedMask = __osDisableInt();
	__osTimerCounter = osGetCount();
	NewTime = __osTimerCounter + tim;
	__osSetCompare(NewTime);
	__osRestoreInt(savedMask);
}

OSTime __osInsertTimer(OSTimer *t)
{
	OSTimer *timep;
	OSTime tim;
	u32 savedMask;
	savedMask = __osDisableInt();
	timep = __osTimerList->next;
	tim = t->value;
	for (; timep != __osTimerList && tim > timep->value; timep = timep->next)
	{
		tim -= timep->value;
	}
	t->value = tim;
	if (timep != __osTimerList) timep->value -= tim;
	t->next = timep;
	t->prev = timep->prev;
	timep->prev->next = t;
	timep->prev = t;
	__osRestoreInt(savedMask);
	return tim;
}
