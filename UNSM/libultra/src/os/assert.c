#include <ultra64.h>

extern void __assertBreak(void);

void __assert(const char *expr, const char *file, int linenum)
{
#ifndef _FINALROM
	osSyncPrintf("\nASSERTION FAULT: %s, %d: \"%s\"\n", file, linenum, expr);
	__assertBreak;
#endif
}
