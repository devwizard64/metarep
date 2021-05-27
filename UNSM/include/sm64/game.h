#ifndef _SM64_GAME_H_
#define _SM64_GAME_H_

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct staff
{
    /* 0x00 */  u8      stage;
    /* 0x01 */  u8      world;
    /* 0x02 */  u8      flag;
    /* 0x03 */  u8      ry;
    /* 0x04 */  vecs    pos;
    /* 0x0C */  const char **str;
};  /* 0x10 */

#else /* __ASSEMBLER__ */

#define staff__stage            0x00
#define staff__world            0x01
#define staff__flag             0x02
#define staff__ry               0x03
#define staff__pos              0x04
#define staff__pos__0           0x04
#define staff__pos__1           0x06
#define staff__pos__2           0x08
#define staff__str              0x0C
#define sizeof__staff           0x10

#endif /* __ASSEMBLER__ */

#endif /* _SM64_GAME_H_ */
