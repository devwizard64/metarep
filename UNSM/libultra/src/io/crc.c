#include <ultra64.h>

u8 __osContAddressCrc(u16 addr)
{
	u8 temp = 0;
	u8 temp2;
	int i;
	for (i = 0; i < 16; i++)
	{
		temp2 = temp & 0x10 ? 0x15 : 0;
		temp <<= 1;
		temp |= (u8)(addr & (0x8000/32) ? 1 : 0);
		addr <<= 1;
		temp ^= temp2;
	}
	return temp & 0x1F;
}

u8 __osContDataCrc(u8 *data)
{
	u8 temp = 0;
	u8 temp2;
	int i, j;
	for (i = 0; i < 32+1; i++)
	{
		for (j = 7; j >= 0; j--)
		{
			temp2 = temp & 0x80 ? 0x85 : 0;
			temp <<= 1;
			if (i == 32)    temp |= 0;
			else            temp |= *data & (1 << j) ? 1 : 0;
			temp ^= temp2;
		}
		data++;
	}
	return temp;
}
