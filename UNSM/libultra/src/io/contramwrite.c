#include <ultra64.h>
#include "osint.h"
#include "controller.h"
#include "siint.h"

static void __osPackRamWriteData(int, u16, u8 *);

s32 __osContRamWrite(
	OSMesgQueue *mq, int channel, u16 address, u8 *buffer, int force
)
{
	s32 ret = 0;
	int i;
	u8 *ptr = (u8 *)&__osPfsPifRam;
	__OSContRamReadFormat ramreadformat;
	int retry = 2;
	if (force != 1 && address < 7 && address != 0) return 0;
	__osSiGetAccess();
	__osContLastCmd = CONT_RAM_WRITE;
	__osPackRamWriteData(channel, address, buffer);
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
			if (__osContDataCrc(buffer) != ramreadformat.datacrc)
			{
				if ((ret = __osPfsGetStatus(mq, channel)))
				{
					__osSiRelAccess();
					return ret;
				}
				else
				{
					ret = PFS_ERR_CONTRFAIL;
				}
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

static void __osPackRamWriteData(int channel, u16 address, u8 *buffer)
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
