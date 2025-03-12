#include <ultra64.h>
#include "osint.h"
#include "controller.h"
#include "siint.h"

static void __osPackRamReadData(int, u16);

s32 __osContRamRead(OSMesgQueue *mq, int channel, u16 address, u8 *buffer)
{
	s32 ret = 0;
	int i;
	u8 *ptr = (u8 *)&__osPfsPifRam;
	__OSContRamReadFormat ramreadformat;
	int retry = 2;
	__osSiGetAccess();
	__osContLastCmd = CONT_RAM_READ;
	__osPackRamReadData(channel, address);
	ret = __osSiRawStartDma(OS_WRITE, &__osPfsPifRam);
	osRecvMesg(mq, NULL, OS_MESG_BLOCK);
	do
	{
		ret = __osSiRawStartDma(OS_READ, &__osPfsPifRam);
		osRecvMesg(mq, NULL, OS_MESG_BLOCK);
		ptr = (u8 *)&__osPfsPifRam;
		if (channel)
		{
			for (i = 0; i < channel; i++)
				ptr++;
		}
		ramreadformat = *(__OSContRamReadFormat *)ptr;
		ret = (ramreadformat.rxsize & CON_ERR_MASK) >> 4;
		if (!ret)
		{
			u8 crc = __osContDataCrc(ramreadformat.data);
			if (crc != ramreadformat.datacrc)
			{
				ret = __osPfsGetStatus(mq, channel);
				if (ret)
				{
					__osSiRelAccess();
					return ret;
				}
				ret = PFS_ERR_CONTRFAIL;
			}
			else
			{
				for (i = 0; i < BLOCKSIZE; i++)
					*buffer++ = ramreadformat.data[i];
			}
		}
		else
		{
			ret = PFS_ERR_NOPACK;
		}
	}
	while (ret == PFS_ERR_CONTRFAIL && retry-- >= 0);
	__osSiRelAccess();
	return ret;
}

static void __osPackRamReadData(int channel, unsigned short address)
{
	u8 *ptr = (u8 *)&__osPfsPifRam;
	__OSContRamReadFormat ramreadformat;
	int i;
#ifdef sgi
	for (i = 0; i < PIFRAMSIZE; i++) __osPfsPifRam.ramarray[i] = 0;
#else
	for (i = 0; i < PIFRAMSIZE-1; i++) __osPfsPifRam.ramarray[i] = 0;
#endif
	__osPfsPifRam.pifstatus = CONT_FORMAT;
	ramreadformat.dummy = 0xFF;
	ramreadformat.txsize = 3;
	ramreadformat.rxsize = 33;
	ramreadformat.cmd = CONT_RAM_READ;
	ramreadformat.addr = address << 5 | __osContAddressCrc(address);
	ramreadformat.datacrc = 0xFF;
	for (i = 0; i < BLOCKSIZE; i++) ramreadformat.data[i] = 0xFF;
	if (channel)
	{
		for (i = 0; i < channel; i++)
			*ptr++ = 0;
	}
	*(__OSContRamReadFormat *)ptr = ramreadformat;
	ptr += sizeof(__OSContRamReadFormat);
	*ptr = FORMAT_END;
}
