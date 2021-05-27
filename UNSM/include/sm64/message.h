#ifndef _SM64_MESSAGE_H_
#define _SM64_MESSAGE_H_

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct msg
{
    /* 0x00 */  s32     arg;
    /* 0x04 */  s8      line;
    /* 0x06 */  s16     x;
    /* 0x08 */  s16     y;
    /* 0x0C */  const u8 *str;
};  /* 0x10 */

#else /* __ASSEMBLER__ */

#define msg__arg                0x00
#define msg__line               0x04
#define msg__x                  0x06
#define msg__y                  0x08
#define msg__str                0x0C
#define sizeof__msg             0x10

#endif /* __ASSEMBLER__ */

#endif /* _SM64_MESSAGE_H_ */
