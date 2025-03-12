#include <ultra64.h>
#include <PR/leoappli.h>
#include "osint.h"
#include "leodrive.h"

extern s32 __osLeoEnabled;

u64 leoDiskStack[4096/8];

static void __osLeoAbnormalResume(void);
static void __osLeoResume(void);

#if REVISION != 199703
#define PIBUSY (PI_STATUS_IO_BUSY|PI_STATUS_DMA_BUSY)
#define ERR(x) x->errStatus
#else
#define PIBUSY PI_STATUS_IO_BUSY
#define ERR(x) info->errStatus
#endif

#define PIWait() \
	pi_stat = IO_READ(PI_STATUS_REG); \
	while (pi_stat & PIBUSY) \
	{ \
		pi_stat = IO_READ(PI_STATUS_REG); \
	}

#define LeoAbort(errCode) \
	ERR(blockInfo) = errCode; \
	__osLeoAbnormalResume(); \
	return 1;

s32 __osLeoInterrupt(void)
{
#if REVISION >= 199707
	u32 stat = 0;
	volatile u32 pi_stat;
#else
	u32 stat;
	u32 pi_stat;
#endif
	u32 bm_stat;
	__OSTranxInfo *info;
	__OSBlockInfo *blockInfo;
#if REVISION < 199707
	if (!__osLeoEnabled) return 0;
#endif
	info = &__osDiskHandle->transferInfo;
	blockInfo = &info->block[info->blockNum];
	pi_stat = IO_READ(PI_STATUS_REG);
	if (pi_stat & PI_STATUS_DMA_BUSY)
	{
#if REVISION != 199703
#if REVISION >= 199707
		__OSGlobalIntMask &= ~(OS_IM_CART & ~0x401);
		blockInfo->errStatus = 29;
#else
		blockInfo->errStatus = 240;
		__OSGlobalIntMask &= ~OS_IM_CART;
#endif
		__osLeoResume();
		return 1;
#else
		IO_WRITE(PI_STATUS_REG, PI_STATUS_RESET|PI_STATUS_CLR_INTR);
		PIWait();
		stat = IO_READ(ASIC_STATUS);
		if (stat & 0x02000000)
		{
			PIWait();
			IO_WRITE(ASIC_BM_CTL, info->bmCtlShadow|0x01000000);
		}
		LeoAbort(LEO_SENSE_DATA_PHASE_ERROR);
#endif
	}
	PIWait();
	stat = IO_READ(ASIC_STATUS);
	if (stat & 0x02000000)
	{
		PIWait();
		IO_WRITE(ASIC_BM_CTL, info->bmCtlShadow|0x01000000);
		ERR(blockInfo) = LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
		return 0;
	}
#if REVISION >= 199707
	if (info->cmdType == OS_OTHERS) return 1;
#endif
	if (stat & 0x08000000)
	{
#if REVISION >= 199707
		PIWait();
		stat = IO_READ(ASIC_STATUS);
#endif
		ERR(blockInfo) = LEO_SENSE_WRITE_FAULT;
		__osLeoResume();
#if REVISION != 199703
		IO_WRITE(PI_STATUS_REG, PI_STATUS_CLR_INTR);
		__OSGlobalIntMask |= OS_IM_PI;
#endif
		return 1;
	}
	if (info->cmdType == OS_WRITE)
	{
		if (!(stat & 0x40000000))
		{
			if (info->sectorNum+1 != 85*info->transferMode)
			{
				LeoAbort(LEO_SENSE_NO_REFERENCE_POSITION_FOUND);
			}
			IO_WRITE(PI_STATUS_REG, PI_STATUS_CLR_INTR);
			__OSGlobalIntMask |= OS_IM_PI;
			ERR(blockInfo) = LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
			__osLeoResume();
			return 1;
		}
		else
		{
			blockInfo->dramAddr =
				(char *)blockInfo->dramAddr + blockInfo->sectorSize;
			info->sectorNum++;
			osEPiRawStartDma(
				__osDiskHandle, OS_WRITE, ASIC_SECTOR_BUFF, blockInfo->dramAddr,
				blockInfo->sectorSize
			);
			return 1;
		}
	}
	else if (info->cmdType == OS_READ)
	{
		if (info->transferMode == LEO_SECTOR_MODE)
		{
			if (info->sectorNum > (int)blockInfo->C1ErrNum + 85/5)
			{
				LeoAbort(LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION);
			}
			if (!(stat & 0x40000000))
			{
				LeoAbort(LEO_SENSE_UNRECOVERED_READ_ERROR);
			}
		}
		else
		{
			blockInfo->dramAddr =
				(char *)blockInfo->dramAddr + blockInfo->sectorSize;
		}
		bm_stat = IO_READ(ASIC_BM_STATUS);
		if (
			(bm_stat & 0x00200000 && bm_stat & 0x00400000) ||
			bm_stat & 0x02000000
		)
		{
			if (blockInfo->C1ErrNum >= 4)
			{
				if (
					info->transferMode != LEO_SECTOR_MODE ||
					info->sectorNum >= 85-2
				)
				{
					LeoAbort(LEO_SENSE_UNRECOVERED_READ_ERROR);
				}
			}
			else
			{
				int errNum = blockInfo->C1ErrNum;
				blockInfo->C1ErrSector[errNum] = info->sectorNum + 1;
			}
			blockInfo->C1ErrNum++;
		}
		if (stat & 0x10000000)
		{
			if (info->sectorNum+1 != 85+4-1)
			{
				ERR(blockInfo) = LEO_SENSE_NO_REFERENCE_POSITION_FOUND;
				__osLeoAbnormalResume();
			}
			if (info->transferMode == LEO_TRACK_MODE && info->blockNum == 0)
			{
				info->blockNum = 1;
				info->sectorNum = -1;
				info->block[1].dramAddr =
					(char *)info->block[1].dramAddr - info->block[1].sectorSize;
#if REVISION >= 199707
				blockInfo->errStatus = LEO_SENSE_WRITE_FAULT;
#endif
			}
			else
			{
				IO_WRITE(PI_STATUS_REG, PI_STATUS_CLR_INTR);
				__OSGlobalIntMask |= OS_IM_PI;
#if REVISION >= 199707
				info->cmdType = OS_OTHERS;
				blockInfo->errStatus =
					LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
#endif
			}
			osEPiRawStartDma(
				__osDiskHandle, OS_READ, ASIC_C2_BUFF, blockInfo->C2Addr,
				blockInfo->sectorSize*4
			);
#if REVISION < 199707
			ERR(blockInfo) = LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
#endif
			return 1;
		}
		if (
			info->sectorNum == -1 && info->transferMode == LEO_TRACK_MODE &&
			info->blockNum == 1
		)
		{
			__OSBlockInfo *bptr;
			bptr = &info->block[0];
			if (bptr->C1ErrNum == 0)
			{
				if (
					*((int *)bptr->C2Addr+0) |
					*((int *)bptr->C2Addr+1) |
					*((int *)bptr->C2Addr+2) |
					*((int *)bptr->C2Addr+3)
				)
				{
					ERR(bptr) = LEO_SENSE_NO_REFERENCE_POSITION_FOUND;
					__osLeoAbnormalResume();
					return 1;
				}
			}
#if REVISION >= 199707
			bptr->errStatus = LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
#else
			ERR(blockInfo) = LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
#endif
			__osLeoResume();
		}
		info->sectorNum++;
		if (stat & 0x40000000)
		{
			if (info->sectorNum >= 85)
			{
				LeoAbort(LEO_SENSE_NO_REFERENCE_POSITION_FOUND);
			}
			osEPiRawStartDma(
				__osDiskHandle, OS_READ, ASIC_SECTOR_BUFF, blockInfo->dramAddr,
				blockInfo->sectorSize
			);
			ERR(blockInfo) = LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION;
			return 1;
		}
		else if (info->sectorNum < 85)
		{
			LeoAbort(LEO_SENSE_NO_REFERENCE_POSITION_FOUND);
		}
		return 1;
	}
	else
	{
		LeoAbort(LEO_SENSE_DATA_PHASE_ERROR);
	}
}

static void __osLeoAbnormalResume(void)
{
	__OSTranxInfo *info;
	u32 pi_stat;
	info = &__osDiskHandle->transferInfo;
	PIWait();
	IO_WRITE(ASIC_BM_CTL, info->bmCtlShadow|0x10000000);
	PIWait();
	IO_WRITE(ASIC_BM_CTL, info->bmCtlShadow);
	__osLeoResume();
	IO_WRITE(PI_STATUS_REG, PI_STATUS_CLR_INTR);
	__OSGlobalIntMask |= OS_IM_PI;
}

static void __osLeoResume(void)
{
	__OSEventState *es;
	OSMesgQueue *mq;
	s32 last;
	es = &__osEventStateTab[OS_EVENT_PI];
	mq = es->messageQueue;
	if (!mq || MQ_IS_FULL(mq)) return;
	last = (mq->first + mq->validCount) % mq->msgCount;
	mq->msg[last] = es->message;
	mq->validCount++;
	if (mq->mtqueue->next)
	{
		__osEnqueueThread(&__osRunQueue, __osPopThread(&mq->mtqueue));
	}
}
