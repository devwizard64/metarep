#include <ultra64.h>
#include <PR/rdb.h>
#include "osint.h"
#include "rmonint.h"

#ifndef _FINALROM

u8 __rmonUtilityBuffer[256];

void __rmonWriteWordTo(u32 *addr, u32 val)
{
	while (__osSpRawWriteIo((u32)addr, val));
}

u32 __rmonReadWordAt(u32 *addr)
{
	if ((u32)addr >= 0x04000000 && (u32)addr <= 0x04FFFFFF)
	{
		u32 data;
		__osSpRawReadIo((u32)addr, &data);
		return data;
	}
	return 0;
}

void __rmonMemcpy(u8 *dest, u8 *srce, u32 count)
{
	while (count--) *dest++ = *srce++;
}

void __rmonCopyWords(u32 *dest, u32 *srce, u32 count)
{
	while (count--) *dest++ = *srce++;
}

static void strcpy(char *dest, char *srce)
{
	while (*dest++ = *srce++);
}

#define InRange(addr, size, min, max) \
	(((addr) < (min) || (addr)+(size) > (max)) ? 0 : 1)

int __rmonReadMem(KKHeader *req)
{
	u8 *cPtr;
	int sent;
	int dataSize;
	KKReadRequest *request = (KKReadRequest *)req;
	KKBufferEvent *reply = (KKBufferEvent *)__rmonUtilityBuffer;
	u8 *blockStart;
	("ReadMem @ %08x for %d\n", request->addr, request->nbytes);
	reply->header.code = request->header.code;
	reply->object = request->object;
	reply->header.error = TV_ERROR_NO_ERROR;
	if (request->addr == (u32)-1) return TV_ERROR_INVALID_ADDRESS;
	if (request->nbytes > 1024) return TV_ERROR_INVALID_CAPABILITY;
	if (req->method == 1)
	{
		if (
			!InRange(request->addr, request->nbytes, 0x04001000, 0x04001FFF) &&
			!InRange(request->addr, request->nbytes, 0x04000000, 0x04000FFF)
		) return TV_ERROR_INVALID_ADDRESS;
	}
	else
	{
		if (osVirtualToPhysical((void *)request->addr) == (u32)-1)
		{
			return TV_ERROR_INVALID_ADDRESS;
		}
	}
	blockStart = (u8 *)request->addr;
	reply->header.length = sizeof(KKHeader) + sizeof(TVid) + request->nbytes;
	dataSize = sizeof(KKHeader) + sizeof(TVid) + request->nbytes;
	cPtr = (u8 *)&dataSize;
	sent = 0;
	while (sent < 4)
	{
		sent += __osRdbSend(&cPtr[sent], 4-sent, RDB_TYPE_GtoH_DEBUG);
	}
	__rmonSendHeader((KKHeader *)reply, sizeof(KKHeader)+4, 1);
	__rmonSendData(blockStart, request->nbytes);
	return 0;
}

int __rmonWriteMem(KKHeader *req)
{
	register KKWriteRequest *request = (KKWriteRequest *)req;
	KKObjectEvent reply;
	("WriteMem\n");
	if (
		req->method == 0 &&
		osVirtualToPhysical((void *)request->writeHeader.addr) == (u32)-1
	) return TV_ERROR_INVALID_ADDRESS;
	if (request->writeHeader.nbytes > 1024) return TV_ERROR_INVALID_CAPABILITY;
	if (InRange(
		request->writeHeader.addr, request->writeHeader.nbytes,
		0x04000000, 0x04FFFFFF
	))
	{
		int align;
		u32 word;
		if ((align = request->writeHeader.addr & 3))
		{
			if (request->writeHeader.nbytes != 1)
			{
				("Long unaligned write...\n");
				return TV_ERROR_INVALID_ADDRESS;
			}
			word = __rmonReadWordAt((u32 *)(request->writeHeader.addr & ~3));
			if (align == 1)
			{
				word = (word & ~(0xFF << 16)) | request->buffer[0] << 16;
			}
			else if (align == 2)
			{
				word = (word & ~(0xFF <<  8)) | request->buffer[0] <<  8;
			}
			else
			{
				word = (word & ~(0xFF <<  0)) | request->buffer[0] <<  0;
			}
			__rmonWriteWordTo((u32 *)(request->writeHeader.addr & ~3), word);
		}
		else
		{
			int wordCount = request->writeHeader.nbytes / 4;
			u32 *wordPointer = (u32 *)request->buffer;
			if (request->writeHeader.nbytes & 3)
			{
				("RCP write not an integral number of words\n");
				return TV_ERROR_INVALID_ADDRESS;
			}
			while (wordCount--)
			{
				__rmonWriteWordTo(
					(u32 *)request->writeHeader.addr, *wordPointer++
				);
				request->writeHeader.addr += 4;
			}
		}
	}
	else
	{
		__rmonMemcpy(
			(u8 *)request->writeHeader.addr, (u8 *)request->buffer,
			request->writeHeader.nbytes
		);
	}
	reply.header.code = request->writeHeader.header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	reply.object = request->writeHeader.object;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKObjectEvent), 1);
	return 0;
}

int __rmonListProcesses(KKHeader *req)
{
	KKObjectRequest *request = (KKObjectRequest *)req;
	KKObjsEvent reply;
	("ListProcesses\n");
	reply.object = 0;
	reply.objs.number = 1;
	reply.objs.objects[0] = req->method == 1 ? 1001 : 1002;
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKObjsEvent), 1);
	return 0;
}

int __rmonLoadProgram(KKHeader *request)
{
	("LoadProgram\n");
	return TV_ERROR_ILLEGAL_CALL;
}

int __rmonGetExeName(KKHeader *req)
{
	KKObjectRequest *request = (KKObjectRequest *)req;
	KKBufferEvent *reply = (KKBufferEvent *)__rmonUtilityBuffer;
	("GetExeName\n");
	reply->header.code = request->header.code;
	reply->header.error = TV_ERROR_NO_ERROR;
	reply->object = request->object;
	if (req->method == 1)   strcpy(reply->buffer, "imem");
	else                    strcpy(reply->buffer, "rmon");
	__rmonSendReply((KKHeader *)reply, sizeof(KKBufferEvent)+4, 1);
	return 0;
}

int __rmonGetRegionCount(KKHeader *req)
{
	KKObjectRequest *request = (KKObjectRequest *)req;
	KKNumberEvent reply;
	("GetRegionCount\n");
	reply.header.code = request->header.code;
	reply.header.error = TV_ERROR_NO_ERROR;
	reply.object = request->object;
	reply.number = req->method == 1 ? 2 : 5;
	__rmonSendReply((KKHeader *)&reply, sizeof(KKNumberEvent), 1);
	return 0;
}

int __rmonGetRegions(KKHeader *req)
{
	KKObjectRequest *request = (KKObjectRequest *)req;
	KKRegionEvent *reply = (KKRegionEvent *)__rmonUtilityBuffer;
	int numRegions;
	("GetRegions\n");
	numRegions = req->method == 1 ? 2 : 6;
	reply->header.length = sizeof(KKRegionEvent) + sizeof(KKRegion)*numRegions;
	reply->header.code = request->header.code;
	reply->header.error = TV_ERROR_NO_ERROR;
	reply->object = request->object;
	reply->number = numRegions;
	reply->regions[1].vaddr = 0x04001000;
	reply->regions[1].size = 0x1000;
	reply->regions[1].flags = 1|2|4;
	reply->regions[1].paddr = 0x04001000;
	reply->regions[0].vaddr = 0x04000000;
	reply->regions[0].size = 0x1000;
	reply->regions[0].flags = 1|2;
	reply->regions[0].paddr = 0x04000000;
	if (numRegions > 2)
	{
		reply->regions[2].vaddr = 0x88200000;
		reply->regions[2].size = 0x6130;
		reply->regions[2].flags = 1|4;
		reply->regions[2].paddr = 0;
		reply->regions[3].vaddr = 4;
		reply->regions[3].size = 0x00200000;
		reply->regions[3].flags = 1|2;
		reply->regions[3].paddr = 0;
		reply->regions[4].vaddr = 0x04002000;
		reply->regions[4].size = 0x00800000;
		reply->regions[4].flags = 1|2;
		reply->regions[4].paddr = 0;
		reply->regions[5].vaddr = 0x88206130;
		reply->regions[5].size = 0x9000;
		reply->regions[5].flags = 1|2;
		reply->regions[5].paddr = 0;
	}
	__rmonSendReply((KKHeader *)reply, reply->header.length, 1);
	return 0;
}

#endif
