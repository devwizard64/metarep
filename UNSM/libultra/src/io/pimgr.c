#include <ultra64.h>
#include "osint.h"
#include "piint.h"

static OSThread piThread;
static u64 piThreadStack[OS_PIM_STACKSIZE/8];

#ifndef _FINALROM
#include <PR/rdb.h>
#define OS_PIM_RAMROM_STACKSIZE 1024
static OSThread ramromThread;
static u64 ramromThreadStack[OS_PIM_RAMROM_STACKSIZE/8];
static OSMesgQueue getRamromQ;
static OSMesg getRamromBuf[1];
static OSMesgQueue freeRamromQ;
static OSMesg freeRamromBuf[1];
static void ramromMain(void *);
#endif

static OSMesgQueue piEventQueue;
static OSMesg piEventBuf[1];

OSDevMgr __osPiDevMgr = {0};
#if REVISION >= 199611
OSPiHandle *__osPiTable;
#endif
#if REVISION >= 199707
OSPiHandle __Dom1SpeedParam, __Dom2SpeedParam;
OSPiHandle *__osCurrentHandle[2] = {&__Dom1SpeedParam, &__Dom2SpeedParam};
#endif

extern OSMesgQueue __osPiAccessQueue;
extern int __osPiAccessQueueEnabled;
extern void __osPiCreateAccessQueue(void);

void osCreatePiManager(
	OSPri pri, OSMesgQueue *cmdQ, OSMesg *cmdBuf, s32 cmdMsgCnt
)
{
	u32 savedMask;
	OSPri oldPri, myPri;
#ifdef _DEBUG
	if (pri < OS_PRIORITY_IDLE || pri > OS_PRIORITY_MAX)
	{
		__osError(ERR_OSCREATEPIMANAGER, 1, pri);
		return;
	}
#endif
	if (__osPiDevMgr.active) return;
	osCreateMesgQueue(cmdQ, cmdBuf, cmdMsgCnt);
	osCreateMesgQueue(&piEventQueue, piEventBuf, 1);
	if (!__osPiAccessQueueEnabled) __osPiCreateAccessQueue();
	osSetEventMesg(OS_EVENT_PI, &piEventQueue, (OSMesg)0x22222222);
	oldPri = -1;
	myPri = osGetThreadPri(NULL);
	if (myPri < pri)
	{
		oldPri = myPri;
		osSetThreadPri(NULL, pri);
	}
	savedMask = __osDisableInt();
	__osPiDevMgr.active = 1;
	__osPiDevMgr.thread = &piThread;
	__osPiDevMgr.cmdQueue = cmdQ;
	__osPiDevMgr.evtQueue = &piEventQueue;
	__osPiDevMgr.acsQueue = &__osPiAccessQueue;
	__osPiDevMgr.dma = osPiRawStartDma;
#if REVISION >= 199611
	__osPiDevMgr.edma = osEPiRawStartDma;
#endif
	osCreateThread(
		&piThread, 0, __osDevMgrMain, &__osPiDevMgr,
		piThreadStack+OS_PIM_STACKSIZE/8, pri
	);
	osStartThread(&piThread);
#ifndef _FINALROM
	osCreateThread(
		&ramromThread, 0, ramromMain, NULL,
		ramromThreadStack+OS_PIM_RAMROM_STACKSIZE/8, pri-1
	);
	osStartThread(&ramromThread);
#endif
	__osRestoreInt(savedMask);
	if (oldPri != -1) osSetThreadPri(NULL, oldPri);
}

#ifndef _FINALROM
static void ramromMain(void *arg)
{
	u32 sent;
	u8 tmp[3];
	(void)arg;
	osCreateMesgQueue(&getRamromQ, getRamromBuf, 1);
	osCreateMesgQueue(&freeRamromQ, freeRamromBuf, 1);
	osSetEventMesg(OS_EVENT_RDB_REQ_RAMROM, &getRamromQ, (OSMesg)0);
	osSetEventMesg(OS_EVENT_RDB_FREE_RAMROM, &freeRamromQ, (OSMesg)0);
	for (;;)
	{
		osRecvMesg(&getRamromQ, NULL, OS_MESG_BLOCK);
		__osPiGetAccess();
		sent = 0;
		while (sent < 1) sent += __osRdbSend(tmp, 1, RDB_TYPE_GtoH_RAMROM);
		osRecvMesg(&freeRamromQ, NULL, OS_MESG_BLOCK);
		__osPiRelAccess();
	}
}
#endif
