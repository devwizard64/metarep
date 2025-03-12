#include <ultra64.h>
#include <PR/rdb.h>
#include "osint.h"
#include "rmonint.h"

#ifndef _FINALROM

typedef union
{
	u32 everything;
	struct
	{
		int opcode:6;
		int base:5;
		int rt:5;
		int offset:16;
	}
	scalarop;
	struct
	{
		int opcode:6;
		int base:5;
		int rt:5;
		int size:5;
		int element:4;
		int offset:7;
	}
	vectorop;
}
INSTRUCTION;

static u32 RCPpc, oldIMEMvalue, DMEMbuffer[4];

static void LoadStoreSU(int opcode, int regno)
{
	INSTRUCTION inst;
	inst.everything = 0;
	inst.scalarop.opcode = opcode;
	inst.scalarop.rt = regno;
	__rmonWriteWordTo((u32 *)0x04001000, inst.everything);
	__rmonWriteWordTo((u32 *)SP_PC_REG, 0);
}

static void LoadStoreVU(int opcode, int regno)
{
	INSTRUCTION inst;
	inst.everything = 0;
	inst.vectorop.opcode = opcode;
	inst.vectorop.rt = regno;
	inst.vectorop.size = 4;
	__rmonWriteWordTo((u32 *)0x04001000, inst.everything);
	__rmonWriteWordTo((u32 *)SP_PC_REG, 0);
}

static void SetUpForRCPop(int isVector)
{
	
	RCPpc = __rmonReadWordAt((u32 *)SP_PC_REG);
	oldIMEMvalue = __rmonReadWordAt((u32 *)0x04001000);
	DMEMbuffer[0] = __rmonReadWordAt((u32 *)0x04000000+0);
	if (isVector)
	{
		DMEMbuffer[1] = __rmonReadWordAt((u32 *)0x04000000+1);
		DMEMbuffer[2] = __rmonReadWordAt((u32 *)0x04000000+2);
		DMEMbuffer[3] = __rmonReadWordAt((u32 *)0x04000000+3);
	}
}

static void CleanupFromRCPop(int isVector)
{
	__rmonWriteWordTo((u32 *)0x04000000+0, DMEMbuffer[0]);
	if (isVector)
	{
		__rmonWriteWordTo((u32 *)0x04000000+1, DMEMbuffer[1]);
		__rmonWriteWordTo((u32 *)0x04000000+2, DMEMbuffer[2]);
		__rmonWriteWordTo((u32 *)0x04000000+3, DMEMbuffer[2]);
	}
	__rmonWriteWordTo((u32 *)0x04001000, oldIMEMvalue);
	__rmonWriteWordTo((u32 *)SP_PC_REG, RCPpc);
}

int __rmonGetGRegisters(KKHeader *req)
{
	register KKObjectRequest *request = (KKObjectRequest *)req;
	KKGregEvent reply;
	("GetGRegisters\n");
	reply.tid = request->object;
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	if (request->header.method == 0)
	{
		OSThread *tptr = __rmonGetTCB(request->object);
		u64 *tcbregptr;
		register int i;
		if (!tptr) return TV_ERROR_INVALID_ID;
		for (i = 1, tcbregptr = &tptr->context.at; i < 26; i++, tcbregptr++)
		{
			reply.registers.gregs[i] = *tcbregptr;
		}
		for (i = 28, tcbregptr = &tptr->context.gp; i < 34; i++, tcbregptr++)
		{
			reply.registers.gregs[i] = *tcbregptr;
		}
		reply.registers.gregs[34] = tptr->context.cause;
		reply.registers.gregs[35] = tptr->context.pc;
		reply.registers.gregs[36] = tptr->context.sr;
		reply.registers.gregs[0] = 0;
	}
	else
	{
		return TV_ERROR_INVALID_ID;
	}
	__rmonSendReply((KKHeader *)&reply, sizeof(KKGregEvent), 1);
	return 0;
}

int __rmonSetGRegisters(KKHeader *req)
{
	register KKGRegsetRequest *request = (KKGRegsetRequest *)req;
	KKObjectEvent reply;
	("SetGRegisters\n");
	if (request->header.method == 0)
	{
		OSThread *tptr = __rmonGetTCB(request->tid);
		u64 *tcbregptr;
		register int i;
		if (!tptr) return TV_ERROR_INVALID_ID;
		for (i = 1, tcbregptr = &tptr->context.at; i < 26; i++, tcbregptr++)
		{
			*tcbregptr = (int)request->registers.gregs[i];
		}
		for (i = 28, tcbregptr = &tptr->context.gp; i < 34; i++, tcbregptr++)
		{
			*tcbregptr = (int)request->registers.gregs[i];
		}
		tptr->context.cause = request->registers.gregs[34];
		tptr->context.pc = request->registers.gregs[35];
		tptr->context.sr = request->registers.gregs[36];
	}
	else
	{
		return TV_ERROR_INVALID_ID;
	}
	reply.object = request->tid;
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKObjectEvent), 1);
	return 0;
}

int __rmonGetFRegisters(KKHeader *req)
{
	register KKObjectRequest *request = (KKObjectRequest *)req;
	KKFPregEvent reply;
	OSThread *tptr;
	volatile float f;
	("GetGRegisters\n");
	if (req->method != 0) return TV_ERROR_INVALID_ID;
	f = 0;
	tptr = __rmonGetTCB(request->object);
	if (!tptr) return TV_ERROR_INVALID_ID;
	__rmonCopyWords(
		(u32 *)reply.registers.fpregs.regs, (u32 *)&tptr->context.fp0, 32
	);
	reply.registers.fpcsr = tptr->context.fpcsr;
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	reply.tid = request->object;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKFPregEvent), 1);
	return 0;
}

int __rmonSetFRegisters(KKHeader *req)
{
	register KKFPRegsetRequest *request = (KKFPRegsetRequest *)req;
	KKObjectEvent reply;
	OSThread *tptr;
	volatile float f;
	("SetFRegisters\n");
	if (req->method != 0) return TV_ERROR_INVALID_ID;
	f = 0;
	tptr = __rmonGetTCB(request->tid);
	if (!tptr) return TV_ERROR_INVALID_ID;
	__rmonCopyWords(
		(u32 *)&tptr->context.fp0, (u32 *)request->registers.fpregs.regs, 32
	);
	tptr->context.fpcsr = request->registers.fpcsr;
	reply.object = request->tid;
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKObjectEvent), 1);
	return 0;
}

static u32 rmonGetRcpRegister(int regNumber)
{
	u32 contents;
	if (__rmonRCPrunning()) return 0;
	SetUpForRCPop(0);
	LoadStoreSU(0x2B, regNumber);
	__rmonStepRCP();
	contents = __rmonReadWordAt((u32 *)0x04000000);
	CleanupFromRCPop(0);
	return contents;
}

int __rmonGetSRegs(KKHeader *req)
{
	register KKObjectRequest *request = (KKObjectRequest *)req;
	KKCpSregEvent reply;
	register int i;
	("GetSRegisters\n");
	if (__rmonRCPrunning()) return TV_ERROR_OP_PROTECTED;
	reply.tid = request->object;
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	SetUpForRCPop(0);
	for (i = 0; i < 32; i++)
	{
		LoadStoreSU(0x2B, i);
		__rmonStepRCP();
		reply.registers.sregs[i] = __rmonReadWordAt((u32 *)0x04000000);
	}
	CleanupFromRCPop(0);
	reply.registers.sregs[32] = __rmonReadWordAt((u32 *)SP_DRAM_ADDR_REG);
	reply.registers.sregs[33] = __rmonReadWordAt((u32 *)SP_MEM_ADDR_REG);
	reply.registers.sregs[34] = __rmonReadWordAt((u32 *)SP_RD_LEN_REG);
	reply.registers.sregs[35] = 0x04001000 + __rmonReadWordAt((u32 *)SP_PC_REG);
	reply.registers.sregs[36] = __rmonReadWordAt((u32 *)SP_WR_LEN_REG);
	reply.registers.sregs[37] = __rmonReadWordAt((u32 *)SP_STATUS_REG);
	reply.registers.sregs[38] = __rmonReadWordAt((u32 *)SP_DMA_FULL_REG);
	reply.registers.sregs[39] = __rmonReadWordAt((u32 *)SP_DMA_BUSY_REG);
	__rmonSendReply((KKHeader *)&reply, sizeof(KKCpSregEvent), 1);
	return 0;
}

int __rmonSetSRegs(KKHeader *req)
{
	register KKCpScalarRegsetRequest *request = (KKCpScalarRegsetRequest *)req;
	KKObjectEvent reply;
	register int i;
	("SetSRegisters\n");
	if (__rmonRCPrunning()) return TV_ERROR_OP_PROTECTED;
	SetUpForRCPop(0);
	for (i = 0; i < 32; i++)
	{
		__rmonWriteWordTo((u32 *)0x04000000, request->registers.sregs[i]);
		LoadStoreSU(0x23, i);
		__rmonStepRCP();
	}
	CleanupFromRCPop(0);
	__rmonWriteWordTo((u32 *)SP_DRAM_ADDR_REG, request->registers.sregs[32]);
	__rmonWriteWordTo((u32 *)SP_MEM_ADDR_REG, request->registers.sregs[33]);
	__rmonWriteWordTo((u32 *)SP_PC_REG, request->registers.sregs[35] & 0xFFF);
	__rmonWriteWordTo((u32 *)SP_WR_LEN_REG, request->registers.sregs[36]);
	__rmonWriteWordTo((u32 *)SP_STATUS_REG, request->registers.sregs[37]);
	reply.object = request->tid;
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKObjectEvent), 1);
	return 0;
}

int __rmonGetVRegs(KKHeader *req)
{
	unsigned char *cPtr;
	int sent;
	int dataSize;
	register KKObjectRequest *request = (KKObjectRequest *)req;
	KKCpVregEvent reply;
	register int i;
	("GetVRegisters\n");
	if (__rmonRCPrunning()) return TV_ERROR_OP_PROTECTED;
	reply.tid = request->object;
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	reply.header.length = sizeof(KKCpVregEvent);
	dataSize = sizeof(KKCpVregEvent);
	cPtr = (unsigned char *)&dataSize;
	sent = 0;
	while (sent < 4)
	{
		sent += __osRdbSend(&cPtr[sent], 4-sent, RDB_TYPE_GtoH_DEBUG);
	}
	__rmonSendHeader((KKHeader *)&reply, sizeof(KKHeader)+sizeof(TVid), 1);
	SetUpForRCPop(1);
	for (i = 0; i < 32; i++)
	{
		LoadStoreVU(0x3A, i);
		__rmonStepRCP();
		__rmonSendData((char *)0x04000000, 16);
	}
	CleanupFromRCPop(1);
	return 0;
}

int __rmonSetVRegs(KKHeader *req)
{
	register KKCpVectorRegsetRequest *request = (KKCpVectorRegsetRequest *)req;
	KKObjectEvent reply;
	register int i;
	("SetVRegs\n");
	if (__rmonRCPrunning()) return TV_ERROR_OP_PROTECTED;

	SetUpForRCPop(1);
	for (i = 0; i < 32; i++)
	{
		__rmonCopyWords(
			(u32 *)0x04000000, (u32 *)&request->registers.vregs[i], 4
		);
		LoadStoreVU(0x32, i);
		__rmonStepRCP();
	}
	CleanupFromRCPop(1);
	reply.object = request->tid;
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKObjectEvent), 1);
	return 0;
}

u32 __rmonGetRegisterContents(int method, int threadNumber, int regNumber)
{
	if (method == 0)
	{
		u32 *regPointer;
		OSThread *tptr;
		if      (regNumber >=  1 && regNumber <= 25) regNumber -= 1;
		else if (regNumber >= 28 && regNumber <= 31) regNumber -= 3;
		else return 0;
		tptr = __rmonGetTCB(threadNumber);
		if (!tptr) return 0;
		regPointer = (u32 *)&tptr->context;
		regPointer += regNumber;
		return *regPointer;
	}
	else
	{
		return rmonGetRcpRegister(regNumber);
	}
}

#endif
