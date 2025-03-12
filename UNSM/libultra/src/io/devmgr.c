#include <ultra64.h>
#if REVISION >= 199611
#include <PR/leoappli.h>
#endif
#include "osint.h"
#include "leodrive.h"

void __osDevMgrMain(void *arg)
{
	OSIoMesg *mb;
	OSMesg em, dummy;
	s32 ret;
	OSDevMgr *dm;
#if REVISION == 199703
	s32 rv = 0;
#endif
#if REVISION >= 199611
	s32 messageSend = 0;
#endif
	dm = arg;
	mb = NULL;
	ret = 0;
	for (;;)
	{
		osRecvMesg(dm->cmdQueue, (OSMesg *)&mb, OS_MESG_BLOCK);
#if REVISION >= 199611
		if (mb->piHandle && mb->piHandle->type == DEVICE_TYPE_64DD && (
			mb->piHandle->transferInfo.cmdType == OS_READ ||
			mb->piHandle->transferInfo.cmdType == OS_WRITE
		))
		{
#if REVISION < 199707 && REVISION != 199703
			u32 stat;
			u32 pi_stat;
			__OSBlockInfo *bptr;
#endif
			__OSBlockInfo *blockInfo;
			__OSTranxInfo *info;
			info = &mb->piHandle->transferInfo;
			blockInfo = &info->block[info->blockNum];
			info->sectorNum = -1;
			if (info->transferMode != LEO_SECTOR_MODE) blockInfo->dramAddr =
				(void *)((u32)blockInfo->dramAddr - blockInfo->sectorSize);
			if (
				info->transferMode == LEO_TRACK_MODE &&
				mb->piHandle->transferInfo.cmdType == OS_READ
			)       messageSend = 1;
			else    messageSend = 0;
			osRecvMesg(dm->acsQueue, &dummy, OS_MESG_BLOCK);
			__osResetGlobalIntMask(OS_IM_PI);
			osEPiRawWriteIo(
				mb->piHandle, ASIC_BM_CTL, info->bmCtlShadow|0x80000000
			);
readblock1:
			osRecvMesg(dm->evtQueue, &em, OS_MESG_BLOCK);
#if REVISION >= 199707
			info = &mb->piHandle->transferInfo;
			blockInfo = &info->block[info->blockNum];
			if (blockInfo->errStatus == 29)
			{
				u32 stat;
				osEPiRawWriteIo(
					mb->piHandle, ASIC_BM_CTL, info->bmCtlShadow|0x10000000
				);
				osEPiRawWriteIo(mb->piHandle, ASIC_BM_CTL, info->bmCtlShadow);
				osEPiRawReadIo(mb->piHandle, ASIC_STATUS, &stat);
				if (stat & 0x02000000) osEPiRawWriteIo(
					mb->piHandle, ASIC_BM_CTL, info->bmCtlShadow|0x01000000
				);
				blockInfo->errStatus = LEO_SENSE_DATA_PHASE_ERROR;
				IO_WRITE(PI_STATUS_REG, PI_STATUS_CLR_INTR);
				__osSetGlobalIntMask(OS_IM_CART|OS_IM_PI);
			}
			osSendMesg(mb->hdr.retQueue, (OSMesg)mb, OS_MESG_NOBLOCK);
#elif REVISION != 199703
			bptr = blockInfo;
			if (bptr->errStatus == 240)
			{
				bptr->errStatus = LEO_SENSE_DATA_PHASE_ERROR;
				__osSetGlobalIntMask(OS_IM_PI);
				osRecvMesg(dm->evtQueue, &em, OS_MESG_BLOCK);
				stat = IO_READ(ASIC_STATUS);
				if (stat & 0x02000000)
				{
					IO_WRITE(ASIC_BM_CTL, info->bmCtlShadow|0x01000000);
				}
				pi_stat = IO_READ(PI_STATUS_REG);
				while (pi_stat & PI_STATUS_IO_BUSY)
				{
					pi_stat = IO_READ(PI_STATUS_REG);
				}
				IO_WRITE(ASIC_BM_CTL, info->bmCtlShadow|0x10000000);
				pi_stat = IO_READ(PI_STATUS_REG);
				while (pi_stat & PI_STATUS_IO_BUSY)
				{
					pi_stat = IO_READ(PI_STATUS_REG);
				}
				IO_WRITE(ASIC_BM_CTL, info->bmCtlShadow);
				__osSetGlobalIntMask(OS_IM_CART);
			}
			osSendMesg(mb->hdr.retQueue, (OSMesg)mb, OS_MESG_NOBLOCK);
#else
			rv = osSendMesg(mb->hdr.retQueue, (OSMesg)mb, OS_MESG_NOBLOCK);
#endif
			if (
#if REVISION != 199703
				messageSend == 1 &&
				mb->piHandle->transferInfo.block[0].errStatus ==
#else
				messageSend == 1 && mb->piHandle->transferInfo.errStatus ==
#endif
					LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION
			)
			{
				messageSend = 0;
				goto readblock1;
			}
			osSendMesg(dm->acsQueue, (OSMesg)0, OS_MESG_NOBLOCK);
			if (mb->piHandle->transferInfo.blockNum == 1) osYieldThread();
		}
		else
		{
			switch (mb->hdr.type)
			{
			case OS_MESG_TYPE_DMAREAD:
				osRecvMesg(dm->acsQueue, &dummy, OS_MESG_BLOCK);
				ret = dm->dma(OS_READ, mb->devAddr, mb->dramAddr, mb->size);
				break;
			case OS_MESG_TYPE_DMAWRITE:
				osRecvMesg(dm->acsQueue, &dummy, OS_MESG_BLOCK);
				ret = dm->dma(OS_WRITE, mb->devAddr, mb->dramAddr, mb->size);
				break;
			case OS_MESG_TYPE_EDMAREAD:
				osRecvMesg(dm->acsQueue, &dummy, OS_MESG_BLOCK);
				ret = dm->edma(
					mb->piHandle, OS_READ, mb->devAddr, mb->dramAddr, mb->size
				);
				break;
			case OS_MESG_TYPE_EDMAWRITE:
				osRecvMesg(dm->acsQueue, &dummy, OS_MESG_BLOCK);
				ret = dm->edma(
					mb->piHandle, OS_WRITE, mb->devAddr, mb->dramAddr, mb->size
				);
				break;
			case OS_MESG_TYPE_LOOPBACK:
				osSendMesg(mb->hdr.retQueue, (OSMesg)mb, OS_MESG_NOBLOCK);
				ret = -1;
				break;
			default:
				ret = -1;
				break;
			}
			if (!ret)
			{
				osRecvMesg(dm->evtQueue, &em, OS_MESG_BLOCK);
#if REVISION != 199703
				osSendMesg(mb->hdr.retQueue, (OSMesg)mb, OS_MESG_NOBLOCK);
#else
				rv = osSendMesg(mb->hdr.retQueue, (OSMesg)mb, OS_MESG_NOBLOCK);
#endif
				osSendMesg(dm->acsQueue, (OSMesg)0, OS_MESG_NOBLOCK);
			}
		}
#else
		switch (mb->hdr.type)
		{
		case OS_MESG_TYPE_DMAREAD:
			osRecvMesg(dm->acsQueue, &dummy, OS_MESG_BLOCK);
			ret = dm->dma(OS_READ, mb->devAddr, mb->dramAddr, mb->size);
			break;
		case OS_MESG_TYPE_DMAWRITE:
			osRecvMesg(dm->acsQueue, &dummy, OS_MESG_BLOCK);
			ret = dm->dma(OS_WRITE, mb->devAddr, mb->dramAddr, mb->size);
			break;
		case OS_MESG_TYPE_LOOPBACK:
			osSendMesg(mb->hdr.retQueue, (OSMesg)mb, OS_MESG_NOBLOCK);
			ret = -1;
			break;
		default:
			ret = -1;
			break;
		}
		if (!ret)
		{
			osRecvMesg(dm->evtQueue, &em, OS_MESG_BLOCK);
			osSendMesg(mb->hdr.retQueue, (OSMesg)mb, OS_MESG_NOBLOCK);
			osSendMesg(dm->acsQueue, (OSMesg)0, OS_MESG_NOBLOCK);
		}
#endif
	}
}
