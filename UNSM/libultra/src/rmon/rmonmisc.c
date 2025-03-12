#include <ultra64.h>
#include "rmonint.h"

#ifndef _FINALROM

int __rmonSetFault(KKHeader *req)
{
	KKFaultRequest *request = (KKFaultRequest *)req;
	KKObjectEvent reply;
	("SetFault\n");
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	reply.object = request->tid;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKObjectEvent), 1);
	return 0;
}

OSMesgQueue __rmonMQ;

static OSThread rmonIOThread;
static OSMesg rmonMsgs[8];
static u64 rmonIOStack[16384/8];
static OSMesg rmonPiMsgs[8];
static OSMesgQueue rmonPiMQ;

extern void __rmonIOhandler(void *);

void __rmonInit(void)
{
	osCreateMesgQueue(&__rmonMQ, rmonMsgs, 8);
	osSetEventMesg(OS_EVENT_CPU_BREAK, &__rmonMQ, (OSMesg)2);
	osSetEventMesg(OS_EVENT_SP_BREAK, &__rmonMQ, (OSMesg)4);
	osSetEventMesg(OS_EVENT_FAULT, &__rmonMQ, (OSMesg)8);
	osSetEventMesg(OS_EVENT_THREADSTATUS, &__rmonMQ, (OSMesg)0);
	osCreateThread(
		&rmonIOThread, 0, __rmonIOhandler, NULL, rmonIOStack+16384/8,
		OS_PRIORITY_MAX
	);
	osCreatePiManager(OS_PRIORITY_PIMGR, &rmonPiMQ, rmonPiMsgs, 8);
	osStartThread(&rmonIOThread);
}

void __rmonPanic(void)
{
	("PANIC!!\n");
	for (;;);
}

int __rmonSetComm(KKHeader *req)
{
	KKObjectEvent reply;
	("SetComm\n");
	reply.header.code = req->code;
	reply.object = 0;
	reply.header.error = TV_ERROR_NO_ERROR;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKObjectEvent), 1);
	return 0;
}

#endif
