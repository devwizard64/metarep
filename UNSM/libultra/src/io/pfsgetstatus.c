#include <ultra64.h>
#include "osint.h"
#include "controller.h"
#include "siint.h"

s32 __osPfsGetStatus(OSMesgQueue *queue, int channel)
{
	s32 ret = 0;
	OSMesg dummy;
	u8 bitpattern;
	OSContStatus data[MAXCONTROLLERS];
	__osPfsRequestData(CONT_REQUEST);
	ret = __osSiRawStartDma(OS_WRITE, &__osPfsPifRam);
	osRecvMesg(queue, &dummy, OS_MESG_BLOCK);
	ret = __osSiRawStartDma(OS_READ, &__osPfsPifRam);
	osRecvMesg(queue, &dummy, OS_MESG_BLOCK);
	__osPfsGetInitData(&bitpattern, data);
	if (
		data[channel].status & CONT_CARD_ON &&
		data[channel].status & CONT_CARD_PULL
	) return PFS_ERR_NEW_PACK;
	if (data[channel].errno || !(data[channel].status & CONT_CARD_ON))
	{
		return PFS_ERR_NOPACK;
	}
	if (data[channel].status & CONT_ADDR_CRC_ER) return PFS_ERR_CONTRFAIL;
	return ret;
}
