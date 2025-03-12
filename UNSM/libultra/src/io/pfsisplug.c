#include <ultra64.h>
#include "osint.h"
#include "controller.h"
#include "siint.h"

s32 osPfsIsPlug(OSMesgQueue *queue, u8 *pattern)
{
	s32 ret = 0;
	OSMesg dummy;
	u8 bitpattern;
	OSContStatus data[MAXCONTROLLERS];
	int channel;
	u8 bits = 0;
	int crc_error_cnt = 3;
	__osSiGetAccess();
	do
	{
		__osPfsRequestData(CONT_REQUEST);
		ret = __osSiRawStartDma(OS_WRITE, &__osPfsPifRam);
		osRecvMesg(queue, &dummy, OS_MESG_BLOCK);
		ret = __osSiRawStartDma(OS_READ, &__osPfsPifRam);
		osRecvMesg(queue, &dummy, OS_MESG_BLOCK);
		__osPfsGetInitData(&bitpattern, data);
		for (channel = 0; channel < __osMaxControllers; channel++)
		{
			if (!(data[channel].status & CONT_ADDR_CRC_ER))
			{
				crc_error_cnt--;
				break;
			}
		}
		if (channel == __osMaxControllers) crc_error_cnt = 0;
	}
	while (crc_error_cnt > 0);
	for (channel = 0; channel < __osMaxControllers; channel++)
	{
		if (!data[channel].errno && data[channel].status & CONT_CARD_ON)
		{
			bits |= 1 << channel;
		}
	}
	__osSiRelAccess();
	*pattern = bits;
	return ret;
}

void __osPfsRequestData(u8 cmd)
{
	u8 *ptr;
	__OSContRequesFormat requestformat;
	int i;
	__osContLastCmd = cmd;
#ifdef sgi
	for (i = 0; i < PIFRAMSIZE; i++) __osPfsPifRam.ramarray[i] = 0;
#else
	for (i = 0; i < PIFRAMSIZE-1; i++) __osPfsPifRam.ramarray[i] = 0;
#endif
	__osPfsPifRam.pifstatus = CONT_FORMAT;
	ptr = (u8 *)&__osPfsPifRam;
	requestformat.dummy = 0xFF;
	requestformat.txsize = 1;
	requestformat.rxsize = 3;
	requestformat.cmd = cmd;
	requestformat.typeh = 0xFF;
	requestformat.typel = 0xFF;
	requestformat.status = 0xFF;
	requestformat.dummy1 = 0xFF;
	for (i = 0; i < __osMaxControllers; i++)
	{
		*(__OSContRequesFormat *)ptr = requestformat;
		ptr += sizeof(__OSContRequesFormat);
	}
	*ptr = FORMAT_END;
}

void __osPfsGetInitData(u8 *pattern, OSContStatus *data)
{
	u8 *ptr;
	__OSContRequesFormat requestformat;
	int i;
	u8 bits = 0;
	ptr = (u8 *)&__osPfsPifRam;
	for (
		i = 0; i < __osMaxControllers;
		i++, ptr += sizeof(__OSContRequesFormat), data++
	)
	{
		requestformat = *(__OSContRequesFormat *)ptr;
		data->errno = (requestformat.rxsize & CON_ERR_MASK) >> 4;
		if (data->errno) continue;
		data->type = requestformat.typel << 8 | requestformat.typeh;
		data->status = requestformat.status;
		bits |= 1 << i;
	}
	*pattern = bits;
}
