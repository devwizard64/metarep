#include <ultra64.h>
#include "rmonint.h"

#ifndef _FINALROM

static int NotImplemented(KKHeader *dummy)
{
	return TV_ERROR_ILLEGAL_CALL;
}

static int (*dispatchTable[])(KKHeader *) =
{
	__rmonLoadProgram,
	__rmonListProcesses,
	__rmonGetExeName,
	__rmonListThreads,
	__rmonThreadStatus,
	NotImplemented,
	__rmonStopThread,
	__rmonRunThread,
	NotImplemented,
	NotImplemented,
	__rmonSetFault,
	NotImplemented,
	__rmonGetRegionCount,
	__rmonGetRegions,
	__rmonGetGRegisters,
	__rmonSetGRegisters,
	__rmonGetFRegisters,
	__rmonSetFRegisters,
	__rmonReadMem,
	__rmonWriteMem,
	__rmonSetBreak,
	__rmonClearBreak,
	__rmonListBreak,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	__rmonSetComm,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	NotImplemented,
	__rmonGetSRegs,
	__rmonSetSRegs,
	__rmonGetVRegs,
	__rmonSetVRegs,
	NotImplemented,
};

int __rmonExecute(KKHeader *request)
{
	int retval;
	KKHeader reply;
	if (request->code > 52) return TV_ERROR_ILLEGAL_CALL;
	if ((retval = dispatchTable[request->code](request)) < 0)
	{
		reply.code = request->code;
		reply.error = retval;
		__rmonSendReply(&reply, sizeof(KKHeader), 1);
	}
	return retval;
}

#endif
