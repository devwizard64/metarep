#include <ultra64.h>
#include "osint.h"
#include "rmonint.h"

#ifndef _FINALROM

typedef struct
{
	u32 *breakAddress;
	u32 oldInstruction;
}
BREAKINFO;

static BREAKINFO breakpoints[16];
static BREAKINFO altBreak;
static BREAKINFO RCPbreakpoints[16];

u8 __rmonRcpAtBreak;

static void rmonFindFaultedThreads(void);

#define breakinst(n) (0xD | (16+(n) & 0xFFFFF) << 6)

static void SetTempBreakpoint(u32 *addr1, u32 *addr2)
{
	("Set temp BP at %08x", addr1);
	if (addr2) (" and %08x", addr2);
	("\n");
	breakpoints[0].oldInstruction = *addr1;
	*addr1 = breakinst(0);
	osWritebackDCache(addr1, 4);
	osInvalICache(addr1, 4);
	breakpoints[0].breakAddress = addr1;
	if (addr2)
	{
		altBreak.oldInstruction = *addr2;
		*addr2 = breakinst(0);
		osWritebackDCache(addr2, 4);
		osInvalICache(addr2, 4);
		altBreak.breakAddress = addr2;
	}
}

static void ClearTempBreakpoint(void)
{
	u32 inst;
	if (breakpoints[0].breakAddress)
	{
		inst = *breakpoints[0].breakAddress;
		if (IsBreak(inst))
		{
			*breakpoints[0].breakAddress = breakpoints[0].oldInstruction;
			osWritebackDCache(breakpoints[0].breakAddress, 4);
			osInvalICache(breakpoints[0].breakAddress, 4);
		}
		breakpoints[0].breakAddress = NULL;
	}
	if (altBreak.breakAddress)
	{
		inst = *altBreak.breakAddress;
		if (IsBreak(inst))
		{
			*altBreak.breakAddress = altBreak.oldInstruction;
			osWritebackDCache(altBreak.breakAddress, 4);
			osInvalICache(altBreak.breakAddress, 4);
		}
		altBreak.breakAddress = NULL;
	}
}

int __rmonSetBreak(KKHeader *req)
{
	register KKSetBkptRequest *request = (KKSetBkptRequest *)req;
	register BREAKINFO *breakBase, *whichBreak, *lastBreak;
	KKBkptEvent reply;
	("SetBreak at %08x, method %d\n", request->addr, req->method);
	if (req->method == 1)
	{
		breakBase = RCPbreakpoints;
		whichBreak = &RCPbreakpoints[1];
		lastBreak = &RCPbreakpoints[16];
	}
	else
	{
		breakBase = breakpoints;
		whichBreak = &breakpoints[1];
		lastBreak = &breakpoints[16];
	}
	for (; whichBreak < lastBreak; whichBreak++)
	{
		if (whichBreak->breakAddress)
		{
			if ((u32)whichBreak->breakAddress == request->addr) break;
			continue;
		}
		else break;
	}
	if (whichBreak == lastBreak) return TV_ERROR_NO_MORE_IDS;
	if (!whichBreak->breakAddress)
	{
		if (req->method == 1)
		{
			whichBreak->oldInstruction = __rmonReadWordAt((u32 *)request->addr);
			__rmonWriteWordTo(
				(u32 *)request->addr, breakinst(whichBreak-breakBase)
			);
		}
		else
		{
			whichBreak->oldInstruction = *(u32 *)request->addr;
			*(u32 *)request->addr = breakinst(whichBreak-breakBase);
			osWritebackDCache((void *)request->addr, 4);
			osInvalICache((void *)request->addr, 4);
			(
				"* (%08x) = %08x (was %08x)\n",
				request->addr,
				breakinst(whichBreak-breakBase),
				whichBreak->oldInstruction
			);
		}
		whichBreak->breakAddress = (u32 *)request->addr;
	}
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	reply.object = request->object;
	reply.bp = whichBreak-breakBase;
	reply.instruction = whichBreak->oldInstruction;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKBkptEvent), 1);
	return 0;
}

int __rmonListBreak(KKHeader *request)
{
	("ListBreak\n");
	return TV_ERROR_ILLEGAL_CALL;
}

int __rmonClearBreak(KKHeader *req)
{
	register KKClrBkptRequest *request = (KKClrBkptRequest *)req;
	register BREAKINFO *whichBreak;
	KKBkptEvent reply;
	u32 inst;
	("ClearBreak\n");
	if (request->bp >= 16) return TV_ERROR_INVALID_ID;
	if (req->method == 1)
	{
		whichBreak = &RCPbreakpoints[request->bp];
		if (!whichBreak->breakAddress) return TV_ERROR_INVALID_ID;
		inst = __rmonReadWordAt(whichBreak->breakAddress);
		if (IsBreak(inst)) __rmonWriteWordTo(
			whichBreak->breakAddress, whichBreak->oldInstruction
		);
	}
	else
	{
		whichBreak = &breakpoints[request->bp];
		if (!whichBreak->breakAddress) return TV_ERROR_INVALID_ID;
		inst = *whichBreak->breakAddress;
		if (IsBreak(inst))
		{
			*whichBreak->breakAddress = whichBreak->oldInstruction;
			osWritebackDCache(whichBreak->breakAddress, 4);
			osInvalICache(whichBreak->breakAddress, 4);
		}
	}
	whichBreak->breakAddress = NULL;
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	reply.object = request->object;
	reply.bp = request->bp;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKBkptEvent), 1);
	return 0;
}

u32 __rmonGetBranchTarget(int method, int thread, char *addr)
{
	int inst;
	if (method == 1)    inst = __rmonReadWordAt((u32 *)addr);
	else                inst = *(int *)addr;
	switch (inst >> 26 & 0x3F)
	{
	case 0x0:
		if ((inst >> 5 & 0x7FFF) == 0x0 && (inst & 0x3F) == 0x8)
		{
			return __rmonGetRegisterContents(method, thread, inst >> 21 & 0x1F);
		}
		if ((inst >> 16 & 0x1F) == 0x0 && (inst & 0x7FF) == 0x9)
		{
			return __rmonGetRegisterContents(method, thread, inst >> 21 & 0x1F);
		}
		break;
	case 0x1:
		switch (inst >> 16 & 0x1F)
		{
		case 0x0:
		case 0x1:
		case 0x2:
		case 0x3:
		case 0x10:
		case 0x11:
		case 0x12:
		case 0x13:
			return (inst << 16 >> 14) + (int)addr+4;
		}
		break;
	case 0x2:
	case 0x3:
		return ((u32)inst << 6 >> 4) + ((int)addr+4 >> 28 << 28);
	case 0x4:
	case 0x5:
	case 0x14:
	case 0x15:
		return (inst << 16 >> 14) + (int)addr+4;
	case 0x6:
	case 0x7:
	case 0x16:
	case 0x17:
		if ((inst >> 16 & 0x1F) == 0x0) return (inst << 16 >> 14) + (int)addr+4;
		break;
	case 0x10:
	case 0x11:
	case 0x12:
	case 0x13:
		if ((inst >> 21 & 0x1F) == 0x8)
		{
			switch (inst >> 16 & 0x1F)
			{
			case 0x0:
			case 0x1:
			case 0x2:
			case 0x3:
				return (inst << 16 >> 14) + (int)addr+4;
			}
		}
		break;
	}
	return -1;
}

static int IsJump(u32 inst)
{
	switch (inst >> 26 & 0x3F)
	{
	case 0x0:
		if ((inst >> 5 & 0x7FFF) == 0x0 && (inst & 0x3F) == 0x8) return 1;
		if ((inst >> 16 & 0x1F) == 0x0 && (inst & 0x7FF) == 0x9) return 1;
		break;
	case 0x2:
	case 0x3:
		return 1;
	}
	return 0;
}

int __rmonSetSingleStep(int thread, u32 *instptr)
{
	u32 branchTarget;
	("SingleStep\n");
	branchTarget = __rmonGetBranchTarget(0, thread, (char *)instptr);
	if (branchTarget & 3)
	{
		SetTempBreakpoint(instptr+1, 0);
	}
	else if (branchTarget == (u32)instptr)
	{
		return 0;
	}
	else if (IsJump(*instptr) || branchTarget == (u32)(instptr+2))
	{
		SetTempBreakpoint((u32 *)branchTarget, 0);
	}
	else
	{
		SetTempBreakpoint((u32 *)branchTarget, instptr+2);
	}
	return 1;
}

void __rmonGetExceptionStatus(KKStatusEvent *reply)
{
	reply->status.flags = 1;
	reply->status.why = 2;
	reply->status.what = 0;
	reply->status.rv = 0;
	reply->status.info.major = 2;
	reply->status.info.minor = 4;
	reply->header.code = 4;
	reply->header.error = TV_ERROR_NO_ERROR;
	reply->header.length = sizeof(KKStatusEvent);
}

static void rmonSendBreakMessage(s32 whichThread, int breakNumber)
{
	KKStatusEvent reply;
	("Break %d in thread %d\n", breakNumber, whichThread);
	__rmonGetThreadStatus(0, whichThread ? whichThread : 1003, &reply);
	__rmonGetExceptionStatus(&reply);
	if (breakNumber == 15)
	{
		reply.status.info.major = 1;
		reply.status.info.minor = 2;
	}
	if (breakNumber < 16)   breakNumber = 0;
	else                    breakNumber -= 16;
	if (breakNumber) reply.status.instr = 0xD;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKStatusEvent), 2);
}

void __rmonHitBreak(void)
{
	("HitBreak\n");
	ClearTempBreakpoint();
	__rmonStopUserThreads(0);
	rmonFindFaultedThreads();
}

void __rmonHitSpBreak(void)
{
	KKStatusEvent exceptionReply;
	("Hit SP Break\n");
	__rmonWriteWordTo((u32 *)SP_PC_REG, __rmonReadWordAt((u32 *)SP_PC_REG)-4);
	__rmonGetThreadStatus(1, 1000, &exceptionReply);
	__rmonGetExceptionStatus(&exceptionReply);
	__rmonSendReply((KKHeader *)&exceptionReply, sizeof(KKStatusEvent), 2);
	__rmonRcpAtBreak = 1;
}

void __rmonHitCpuFault(void)
{
	("HitCpuFault\n");
	__rmonMaskIdleThreadInts();
	__rmonStopUserThreads(0);
	rmonFindFaultedThreads();
}

static void rmonFindFaultedThreads(void)
{
	register OSThread *tptr = __osGetActiveQueue();
	while (tptr->priority != -1)
	{
		if (
			tptr->priority > OS_PRIORITY_IDLE &&
			tptr->priority <= OS_PRIORITY_APPMAX
		)
		{
			int inst;
			if (tptr->flags & OS_FLAG_CPU_BREAK)
			{
				inst = *(int *)tptr->context.pc;
				(
					"Brk in thread %d @ %08x, inst %08x\r\n",
					tptr->id, tptr->context.pc, inst
				);
				if (IsBreak(inst))
				{
					rmonSendBreakMessage(tptr->id, inst >> 6);
				}
				else
				{
					rmonSendBreakMessage(tptr->id, 0);
				}
			}
			if (tptr->flags & OS_FLAG_FAULT)
			{
				__rmonSendFault(tptr);
				rmonSendBreakMessage(tptr->id, 15);
			}
		}
		tptr = tptr->tlnext;
	}
}

#endif
