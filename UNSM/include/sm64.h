#ifndef _SM64_H_
#define _SM64_H_

#include <ultra64.h>

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct msg_t
{
    /* 0x00 */  s32     arg;
    /* 0x04 */  s8      line;
    /* 0x06 */  s16     x;
    /* 0x08 */  s16     y;
    /* 0x0C */  const u8 *str;
};  /* 0x10 */

#endif /* __ASSEMBLER__ */

#endif /* _SM64_H_ */
