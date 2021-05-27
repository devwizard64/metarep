#ifndef _SM64_SCROLL_H_
#define _SM64_SCROLL_H_

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct scroll
{
    /* 0x00 */  s32     index;
    /* 0x04 */  s32     texture;
    /* 0x08 */  s32     vtx;
    /* 0x0C */  const s16 *data;
    /* 0x10 */  const Gfx *start;
    /* 0x14 */  const Gfx *end;
    /* 0x18 */  const Gfx *draw;
    /* 0x1C */  u8      r;
    /* 0x1D */  u8      g;
    /* 0x1E */  u8      b;
    /* 0x1F */  u8      a;
    /* 0x20 */  s32     rm;
};  /* 0x24 */

#else /* __ASSEMBLER__ */

#define scroll__index           0x00
#define scroll__texture         0x04
#define scroll__vtx             0x08
#define scroll__data            0x0C
#define scroll__start           0x10
#define scroll__end             0x14
#define scroll__draw            0x18
#define scroll__r               0x1C
#define scroll__g               0x1D
#define scroll__b               0x1E
#define scroll__a               0x1F
#define scroll__rm              0x20
#define sizeof__scroll          0x24

#endif /* __ASSEMBLER__ */

#endif /* _SM64_SCROLL_H_ */
