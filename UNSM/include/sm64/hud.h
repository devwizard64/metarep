#ifndef _SM64_HUD_H_
#define _SM64_HUD_H_

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct hud
{
    /* 0x00 */  s16     life;
    /* 0x02 */  s16     coin;
    /* 0x04 */  s16     star;
    /* 0x06 */  s16     power;
    /* 0x08 */  s16     key;
    /* 0x0A */  s16     flag;
    /* 0x0C */  u16     timer;
};  /* 0x0E */

struct power
{
    /* 0x00 */  s8      mode;
    /* 0x02 */  s16     x;
    /* 0x04 */  s16     y;
    /* 0x08 */  f32     scale;
};  /* 0x0C */

#else /* __ASSEMBLER__ */

#define hud__life               0x00
#define hud__coin               0x02
#define hud__star               0x04
#define hud__power              0x06
#define hud__key                0x08
#define hud__flag               0x0A
#define hud__timer              0x0C
#define sizeof__hud             0x0E

#define power__mode             0x00
#define power__x                0x02
#define power__y                0x04
#define power__scale            0x08
#define sizeof__power           0x0C

#endif /* __ASSEMBLER__ */

#endif /* _SM64_HUD_H_ */
