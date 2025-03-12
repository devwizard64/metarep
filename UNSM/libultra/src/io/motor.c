#include <ultra64.h>
#include "osint.h"
#include "controller.h"
#include "siint.h"

OSPifRam _MotorStopData[MAXCONTROLLERS];
OSPifRam _MotorStartData[MAXCONTROLLERS];
u8 _motorstopbuf[BLOCKSIZE];
u8 _motorstartbuf[BLOCKSIZE];
int __osMotorinitialized[MAXCONTROLLERS] = {0};

s32 osMotorStop(OSPfs *pfs)
{
	int i;
	s32 ret;
	u8 *ptr = (u8 *)&__osPfsPifRam;
	__OSContRamReadFormat ramreadformat;
	if (!__osMotorinitialized[pfs->channel]) return PFS_ERR_INVALID;
	__osSiGetAccess();
	__osContLastCmd = CONT_RAM_WRITE;
	__osSiRawStartDma(OS_WRITE, &_MotorStopData[pfs->channel]);
	osRecvMesg(pfs->queue, NULL, OS_MESG_BLOCK);
	ret = __osSiRawStartDma(OS_READ, &__osPfsPifRam);
	osRecvMesg(pfs->queue, NULL, OS_MESG_BLOCK);
	ptr = (u8 *)&__osPfsPifRam;
	if (pfs->channel)
	{
		for (i = 0; i < pfs->channel; i++)
			ptr++;
	}
	ramreadformat = *(__OSContRamReadFormat *)ptr;
	ret = (ramreadformat.rxsize & CON_ERR_MASK) >> 4;
	if (!ret)
	{
		if (ramreadformat.datacrc != __osContDataCrc(_motorstopbuf))
		{
			ret = PFS_ERR_CONTRFAIL;
		}
	}
	__osSiRelAccess();
	return ret;
}

s32 osMotorStart(OSPfs *pfs)
{
	int i;
	s32 ret;
	u8 *ptr = (u8 *)&__osPfsPifRam;
	__OSContRamReadFormat ramreadformat;
	if (!__osMotorinitialized[pfs->channel]) return PFS_ERR_INVALID;
	__osSiGetAccess();
	__osContLastCmd = CONT_RAM_WRITE;
	__osSiRawStartDma(OS_WRITE, &_MotorStartData[pfs->channel]);
	osRecvMesg(pfs->queue, NULL, OS_MESG_BLOCK);
	ret = __osSiRawStartDma(OS_READ, &__osPfsPifRam);
	osRecvMesg(pfs->queue, NULL, OS_MESG_BLOCK);
	ptr = (u8 *)&__osPfsPifRam;
	if (pfs->channel)
	{
		for (i = 0; i < pfs->channel; i++)
			ptr++;
	}
	ramreadformat = *(__OSContRamReadFormat *)ptr;
	ret = (ramreadformat.rxsize & CON_ERR_MASK) >> 4;
	if (!ret)
	{
		if (ramreadformat.datacrc != __osContDataCrc(_motorstartbuf))
		{
			ret = PFS_ERR_CONTRFAIL;
		}
	}
	__osSiRelAccess();
	return ret;
}

static void _MakeMotorData(
	int channel, u16 address, u8 *buffer, OSPifRam *mdata
)
{
	u8 *ptr;
	__OSContRamReadFormat ramreadformat;
	int i;
	for (i = 0, ptr = (u8 *)mdata; i < PIFRAMSIZE-1; i++)
	{
		mdata->ramarray[i] = 0;
	}
	mdata->pifstatus = CONT_FORMAT;
	ramreadformat.dummy = 0xFF;
	ramreadformat.txsize = 35;
	ramreadformat.rxsize = 1;
	ramreadformat.cmd = CONT_RAM_WRITE;
	ramreadformat.addr = address << 5 | __osContAddressCrc(address);
	ramreadformat.datacrc = 0xFF;
	for (i = 0; i < BLOCKSIZE; i++)
		ramreadformat.data[i] = *buffer++;
	if (channel)
	{
		for (i = 0; i < channel; i++)
			*ptr++ = 0;
	}
	*(__OSContRamReadFormat *)ptr = ramreadformat;
	ptr += sizeof(__OSContRamReadFormat);
	*ptr = FORMAT_END;
}

s32 osMotorInit(OSMesgQueue *mq, OSPfs *pfs, int channel)
{
	int i;
	s32 ret;
	u8 temp[BLOCKSIZE];
	pfs->queue = mq;
	pfs->channel = channel;
	pfs->status = 0;
	pfs->activebank = 0x80;
	for (i = 0; i < BLOCKSIZE; i++) temp[i] = 0xFE;
	ret = __osContRamWrite(mq, channel, 0x8000/32, temp, 0);
	if (ret == PFS_ERR_NEW_PACK)
	{
		ret = __osContRamWrite(mq, channel, 0x8000/32, temp, 0);
	}
	if (ret) return ret;
	ret = __osContRamRead(mq, channel, 0x8000/32, temp);
	if (ret == PFS_ERR_NEW_PACK) ret = PFS_ERR_CONTRFAIL;
	if (ret) return ret;
	else if (temp[BLOCKSIZE-1] == 0xFE) return PFS_ERR_DEVICE;
	for (i = 0; i < BLOCKSIZE; i++) temp[i] = 0x80;
	ret = __osContRamWrite(mq, channel, 0x8000/32, temp, 0);
	if (ret == PFS_ERR_NEW_PACK)
	{
		ret = __osContRamWrite(mq, channel, 0x8000/32, temp, 0);
	}
	if (ret) return ret;
	ret = __osContRamRead(mq, channel, 0x8000/32, temp);
	if (ret == PFS_ERR_NEW_PACK) ret = PFS_ERR_CONTRFAIL;
	if (ret) return ret;
	else if (temp[BLOCKSIZE-1] != 0x80) return PFS_ERR_DEVICE;
	if (!__osMotorinitialized[channel])
	{
		for (i = 0; i < BLOCKSIZE; i++)
		{
			_motorstartbuf[i] = 1;
			_motorstopbuf[i] = 0;
		}
		_MakeMotorData(
			channel, 0xC000/32, _motorstartbuf, &_MotorStartData[channel]
		);
		_MakeMotorData(
			channel, 0xC000/32, _motorstopbuf, &_MotorStopData[channel]
		);
		__osMotorinitialized[channel] = 1;
	}
	return 0;
}
