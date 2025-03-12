#include <PR/ultratypes.h>
#include <PR/os.h>
#include <PR/ultralog.h>
#include <PR/rdb.h>
#include "osint.h"
#include "rmonint.h"

#ifndef _FINALROM

int __rmonActive = 0;

static vu32 somethingToDo;
static u32 inbuffer[280];
static u8 cmdinptr, cmdoutptr;
static int state;
static char *inPointer;

void __rmonSendHeader(KKHeader *const block, u32 blockSize, u32 type)
{
	int sent;
	unsigned char *cPtr = (unsigned char *)block;
	block->rev = 2;
	block->type = type;
	sent = 0;
	while (sent < blockSize)
	{
		sent += __osRdbSend(cPtr+sent, blockSize-sent, RDB_TYPE_GtoH_DEBUG);
	}
}

void __rmonSendReply(KKHeader *const block, u32 blockSize, u32 replyType)
{
	unsigned char *cPtr;
	int sent = 0;
	block->length = blockSize;
	cPtr = (unsigned char *)&blockSize;
	while (sent < 4)
	{
		sent += __osRdbSend(&cPtr[sent], 4-sent, RDB_TYPE_GtoH_DEBUG);
	}
	__rmonSendHeader(block, blockSize, replyType);
	__rmonIOflush();
}

void __rmonSendData(const char *block, unsigned int blockSize)
{
	int *blockPointer = (int *)block;
	unsigned int wordCount;
	u32 data;
	union
	{
		char bufBytes[4];
		u32 bufWord;
	}
	buffer;
	wordCount = blockSize+3 >> 2;
	if (!((u32)block & 3))
	{
		while (wordCount--)
		{
			if (
				(u32)blockPointer >= 0x04000000 &&
				(u32)blockPointer <= 0x04FFFFFF
			)
			{
				__osSpRawReadIo((u32)blockPointer++, &data);
				__rmonIOputw(data);
			}
			else
			{
				__rmonIOputw(*blockPointer++);
			}
		}
	}
	else
	{
		while (wordCount--)
		{
			__rmonMemcpy(buffer.bufBytes, (u8 *)blockPointer, 4);
			__rmonIOputw(buffer.bufWord);
			blockPointer++;
		}
	}
	__rmonIOflush();
}

void rmonMain(void)
{
	register int newChars;
	somethingToDo = 0;
	cmdinptr = cmdoutptr = 0;
	__rmonInit();
	__rmonActive = 1;
	for (state = 0, newChars = 0, inPointer = (char *)inbuffer;;)
	{
		OSMesg work;
		osRecvMesg(&__rmonMQ, &work, OS_MESG_BLOCK);
		somethingToDo |= (u32)work;
		if (somethingToDo & 2)
		{
			somethingToDo &= ~2;
			__rmonHitBreak();
		}
		if (somethingToDo & 4)
		{
			somethingToDo &= ~4;
			__rmonHitSpBreak();
		}
		if (somethingToDo & 8)
		{
			somethingToDo &= ~8;
			__rmonHitCpuFault();
		}
		if (somethingToDo & 16)
		{
			("rmon: Thread %d created\n", somethingToDo >> 8);
			somethingToDo &= ~16 & 0xFF;
		}
		if (somethingToDo & 32)
		{
			("rmon: Thread %d destroyed\n", somethingToDo >> 8);
			somethingToDo &= ~32 & 0xFF;
		}
	}
}

#endif
