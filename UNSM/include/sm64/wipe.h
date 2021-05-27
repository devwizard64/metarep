#ifndef _SM64_WIPE_H_
#define _SM64_WIPE_H_

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct wipe
{
    /* 0x00 */  u8      active;
    /* 0x01 */  u8      type;
    /* 0x02 */  u8      _02;
    /* 0x03 */  u8      _03;
    /* 0x04 */  u8      r;
    /* 0x05 */  u8      g;
    /* 0x06 */  u8      b;
    /* 0x08 */  s16     _08;
    /* 0x0A */  s16     _0A;
    /* 0x0C */  s16     _0C;
    /* 0x0E */  s16     _0E;
    /* 0x10 */  s16     _10;
    /* 0x12 */  s16     _12;
    /* 0x14 */  s16     _14;
};  /* 0x16 */

#else /* __ASSEMBLER__ */

#define wipe__active            0x00
#define wipe__type              0x01
#define wipe__02                0x02
#define wipe__03                0x03
#define wipe__r                 0x04
#define wipe__g                 0x05
#define wipe__b                 0x06
#define wipe__08                0x08
#define wipe__0A                0x0A
#define wipe__0C                0x0C
#define wipe__0E                0x0E
#define wipe__10                0x10
#define wipe__12                0x12
#define wipe__14                0x14
#define sizeof__wipe            0x16

#endif /* __ASSEMBLER__ */

#endif /* _SM64_WIPE_H_ */
