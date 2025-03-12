#include <ultra64.h>
#include "osint.h"

#define ERROR_LOG_LEN (sizeof(OSLogItem) + 4*OS_LOG_MAX_ARGS)

void __osDefaultHandler(s16, s16, ...);

static u32 errorLogData[ERROR_LOG_LEN/4];
static OSLog errorLog = {OS_ERROR_MAGIC, ERROR_LOG_LEN, errorLogData, 0, 0};
OSErrorHandler __osErrorHandler = __osDefaultHandler;

void __osDefaultHandler(s16 code, s16 numArgs, ...)
{
	va_list argPtr;
	va_start(argPtr, numArgs);
	__osLogWrite(&errorLog, code, numArgs, argPtr);
	va_end(argPtr);
	osFlushLog(&errorLog);
}
