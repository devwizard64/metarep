#ifndef _SM64_APP_H_
#define _SM64_APP_H_

#include <sm64/types.h>
#include <sm64/main.h>

#ifndef __ASSEMBLER__

struct video
{
    /* 0x0000 */    Gfx     gfx[6400];
    /* 0xC800 */    struct sptask sptask;
};  /* 0xC850 */

struct controller
{
    /* 0x00 */  s16     stick_x;
    /* 0x02 */  s16     stick_y;
    /* 0x04 */  f32     stick[2];
    /* 0x0C */  f32     stick_mag;
    /* 0x10 */  u16     held;
    /* 0x12 */  u16     down;
    /* 0x14 */  OSContStatus *status;
    /* 0x18 */  OSContPad *pad;
};  /* 0x1C */

struct demo
{
    /* 0x00 */  u8      count;
    /* 0x01 */  s8      stick_x;
    /* 0x02 */  s8      stick_y;
    /* 0x03 */  u8      button;
};  /* 0x04 */

#else /* __ASSEMBLER__ */

#define video__gfx              0x0000
#define video__sptask           0xC800
#define sizeof__video           0xC850

#define controller__stick_x     0x00
#define controller__stick_y     0x02
#define controller__stick       0x04
#define controller__stick__0    0x04
#define controller__stick__1    0x08
#define controller__stick_mag   0x0C
#define controller__held        0x10
#define controller__down        0x12
#define controller__status      0x14
#define controller__pad         0x18
#define sizeof__controller      0x1C

#define demo__count             0x00
#define demo__stick_x           0x01
#define demo__stick_y           0x02
#define demo__button            0x03
#define sizeof__demo            0x04

#endif /* __ASSEMBLER__ */

#endif /* _SM64_APP_H_ */
