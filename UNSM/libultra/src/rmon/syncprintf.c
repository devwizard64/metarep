#include <ultra64.h>
#include <PR/rdb.h>
#include <string.h>
#include "xstdio.h"
#include "osint.h"

#ifndef _FINALROM
static void *proutSyncPrintf(void *s, const char *buf, size_t n)
{
	size_t sent = 0;
	while (sent < n)
	{
		sent += __osRdbSend((u8 *)&buf[sent], n-sent, RDB_TYPE_GtoH_PRINT);
	}
	return (void *)1;
}
#endif

void osSyncPrintf(const char *fmt, ...)
{
	int ans;
	va_list ap;
#ifndef _FINALROM
	va_start(ap, fmt);
	ans = _Printf(proutSyncPrintf, NULL, fmt, ap);
	va_end(ap);
#endif
}
