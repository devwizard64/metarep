#ifndef _SM64_TIME_H_
#define _SM64_TIME_H_

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct time
{
    /* 0x00 */  s16     _00;
    /* 0x02 */  s16     _02;
    /* 0x08 */  OSTime  _08[5];
    /* 0x30 */  OSTime  _30[3];
    /* 0x48 */  OSTime  _48[8];
    /* 0x88 */  OSTime  _88[8];
};  /* 0xC8 */

#else /* __ASSEMBLER__ */

#define time__00                0x00
#define time__02                0x02
#define time__08                0x08
#define time__30                0x30

#endif /* __ASSEMBLER__ */

#endif /* _SM64_TIME_H_ */
