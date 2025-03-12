#include <ultra64.h>
#include "osint.h"
#include "rmonint.h"

#ifndef _FINALROM

void __rmonMaskIdleThreadInts(void)
{
	register OSThread *tptr = __osGetActiveQueue();
	while (tptr->priority != -1)
	{
		if (tptr->priority == 0)
		{
			tptr->context.sr &= ~OS_IM_CPU;
			tptr->context.sr |= OS_IM_CART|OS_IM_RDBWRITE|OS_IM_RDBREAD;
			break;
		}
		tptr = tptr->tlnext;
	}
}

OSThread *__rmonGetTCB(int threadNumber)
{
	register OSThread *tptr = __osGetActiveQueue();
	if (threadNumber < 1) return 0;
	while (tptr->priority != -1)
	{
		if (tptr->id == threadNumber) return tptr;
		tptr = tptr->tlnext;
	}
	return NULL;
}

int __rmonStopUserThreads(int whichThread)
{
	register int whichOne = 0;
	register OSThread *tptr = __osGetActiveQueue();
	("StopThreads %d\n", whichThread);
	if (whichThread)
	{
		while (tptr->priority != -1)
		{
			if (tptr->id == whichThread) break;
			tptr = tptr->tlnext;
		}
		if (tptr->priority == -1) return 0;
		if (
			tptr->priority > OS_PRIORITY_IDLE &&
			tptr->priority <= OS_PRIORITY_APPMAX
		)
		{
			osStopThread(tptr);
			if (tptr->state != OS_STATE_STOPPED)
			{
				("Couldn't stop thread %d\n", whichThread);
			}
			whichOne = whichThread;
		}
	}
	else
	{
		while (tptr->priority != -1)
		{
			if (
				tptr->priority > OS_PRIORITY_IDLE &&
				tptr->priority <= OS_PRIORITY_APPMAX
			)
			{
				osStopThread(tptr);
				if (tptr->state != OS_STATE_STOPPED)
				{
					("Couldn't stop thread %d\n", whichThread);
				}
				whichOne = -1;
			}
			tptr = tptr->tlnext;
		}
	}
	return whichOne;
}

int __rmonListThreads(KKHeader *req)
{
	register KKObjectRequest *request = (KKObjectRequest *)req;
	KKObjsEvent *reply = (KKObjsEvent *)__rmonUtilityBuffer;
	("ListThreads\n");
	reply->object = request->object == -1 ? 1002 : request->object;
	if (req->method == 1)
	{
		reply->objs.number = 1;
		reply->objs.objects[0] = 1000;
	}
	else
	{
		register OSThread *tptr = __osGetActiveQueue();
		reply->objs.number = 0;
		while (tptr->priority != -1)
		{
			if (tptr->id)
			{
				reply->objs.objects[reply->objs.number] = tptr->id;
				reply->objs.number++;
			}
			tptr = tptr->tlnext;
		}
	}
	reply->header.code = request->header.code;
	reply->header.error = TV_ERROR_NO_ERROR;
	__rmonSendReply(
		(KKHeader *)reply,
		sizeof(KKObjsEvent) + sizeof(TVid)*(reply->objs.number-1), 1
	);
	return 0;
}

int __rmonGetThreadStatus(int method, int id, KKStatusEvent *reply)
{
	u32 inst;
	reply->status.tid = id;
	reply->status.pid = method == 1 ? 1001 : 1002;
	reply->status.why = 1;
	reply->status.what = 0;
	reply->status.info.major = 0;
	reply->status.info.minor = 0;
	reply->status.rv = 0;
	if (method == 1)
	{
		reply->status.start = 0x04001000;
		reply->status.priority = 42;
		if (__rmonRCPrunning())
		{
			reply->status.flags = 4;
			reply->status.info.addr = 0;
			reply->status.instr = 0;
		}
		else
		{
			reply->status.flags = 1;
			reply->status.info.addr =
				0x04001000 + __rmonReadWordAt((u32 *)SP_PC_REG);
			inst = __rmonReadWordAt((u32 *)reply->status.info.addr);
			if (IsBreak(inst)) inst = 0xD;
			if (__rmonRcpAtBreak)
			{
				reply->status.why = 2;
				reply->status.info.major = 2;
				reply->status.info.minor = 4;
			}
			reply->status.instr = inst;
		}
	}
	else
	{
		OSThread *tptr = __osGetActiveQueue();
		while (tptr->priority != -1)
		{
			if (tptr->id == id) break;
			tptr = tptr->tlnext;
		}
		if (tptr->priority == -1) return TV_ERROR_INVALID_ID;
		reply->status.priority = tptr->priority;
		reply->status.flags = tptr->state ? tptr->state : OS_STATE_STOPPED;
		reply->status.info.addr = tptr->context.pc;
		inst = *(int *)tptr->context.pc;
		if (IsBreak(inst)) inst = 0xD;
		reply->status.instr = inst;
		reply->status.start = (int)tptr;
		if (tptr->flags & OS_FLAG_CPU_BREAK)
		{
			reply->status.why = 2;
			reply->status.info.major = 2;
			reply->status.info.minor = 4;
		}
		else if (tptr->flags & OS_FLAG_FAULT)
		{
			reply->status.why = 2;
			reply->status.info.major = 1;
			reply->status.info.minor = 2;
		}
	}
	return 0;
}

int __rmonThreadStatus(KKHeader *req)
{
	KKObjectRequest *request = (KKObjectRequest *)req;
	KKStatusEvent reply;
	("ThreadStatus %d method %d\n", request->object, req->method);
	if (__rmonGetThreadStatus(req->method, request->object, &reply))
	{
		return TV_ERROR_INVALID_ID;
	}
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKStatusEvent), 1);
	return 0;
}

int __rmonStopThread(KKHeader *req)
{
	KKObjectRequest *request = (KKObjectRequest *)req;
	KKStatusEvent reply;
	u32 *pc;
	("StopThread %d\n", request->object);
	switch (req->method)
	{
	case 0:
		__rmonStopUserThreads(request->object);
		break;
	case 1:
		if (__rmonRCPrunning())
		{
			__rmonIdleRCP();
			pc = (u32 *)__rmonReadWordAt((u32 *)SP_PC_REG);
			if (!pc) break;
			pc--;
			if (!(__rmonGetBranchTarget(
				1, 1000, (char *)(0x04001000+(u32)pc)
			) & 3)) __rmonStepRCP();
		}
		break;
	default:
		return TV_ERROR_OP_PROTECTED;
	}
	if (__rmonGetThreadStatus(req->method, request->object, &reply))
	{
		return TV_ERROR_INVALID_ID;
	}
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKStatusEvent), 1);
	if (reply.status.flags == 1)
	{
		reply.header.code = 4;
		__rmonSendReply((KKHeader *)&reply, sizeof(KKStatusEvent), 2);
	}
	return 0;
}

int __rmonRunThread(KKHeader *req)
{
	KKRunThreadRequest *request = (KKRunThreadRequest *)req;
	KKObjectEvent reply;
	KKStatusEvent exceptionReply;
	register OSThread *tptr;
	register int runNeeded = 0;
	("RunThread %d\n", request->tid);
	switch (req->method)
	{
	case 0:
		tptr = __osGetActiveQueue();
		while (tptr->priority != -1)
		{
			if (tptr->id == request->tid) break;
			tptr = tptr->tlnext;
		}
		if (tptr->priority == -1) return TV_ERROR_INVALID_ID;
		if (tptr->state != OS_STATE_STOPPED) return TV_ERROR_OP_PROTECTED;
		tptr->flags &= ~(OS_FLAG_CPU_BREAK|OS_FLAG_FAULT);
		if (request->actions.flags & 2)
		{
			tptr->context.pc = request->actions.vaddr;
		}
		if (request->actions.flags & 1)
		{
			if (!__rmonSetSingleStep(request->tid, (u32 *)tptr->context.pc))
			{
				return TV_ERROR_OP_PROTECTED;
			}
		}
		runNeeded = 1;
		break;
	case 1:
		if (__rmonRCPrunning()) return TV_ERROR_OP_PROTECTED;
		if (request->actions.flags & 2) __rmonWriteWordTo(
			(u32 *)SP_PC_REG, (u32)(request->actions.vaddr-0x04001000)
		);
		if (request->actions.flags & 1)
		{
			if (!(__rmonGetBranchTarget(
				1, 1000, (char *)(0x04001000+__rmonReadWordAt((u32 *)SP_PC_REG))
			) & 3)) __rmonStepRCP();
			__rmonStepRCP();
			__rmonRcpAtBreak = 1;
		}
		else
		{
			__rmonRcpAtBreak = 0;
			__rmonRunRCP();
		}
		reply.header.code = request->header.code;
		reply.header.error = TV_ERROR_NO_ERROR;
		reply.object = request->tid;
		__rmonSendReply((KKHeader *)&reply, sizeof(KKObjectEvent), 1);
		if (request->actions.flags & 1)
		{
			__rmonGetThreadStatus(1, 1000, &exceptionReply);
			__rmonGetExceptionStatus(&exceptionReply);
			__rmonSendReply(
				(KKHeader *)&exceptionReply, sizeof(KKStatusEvent), 2
			);
		}
		return 0;
	default:
		return TV_ERROR_OP_PROTECTED;
	}
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	reply.object = request->tid;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKObjectEvent), 1);
	if (runNeeded) osStartThread(tptr);
	return 1;
}

#endif
