#ifndef _SM64_SHADOW_H_
#define _SM64_SHADOW_H_

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct shadow_rect
{
    /* 0x00 */  f32     sx;
    /* 0x04 */  f32     sz;
    /* 0x08 */  s8      h_scale;
};  /* 0x09 */

#else /* __ASSEMBLER__ */

#define shadow_rect__sx         0x00
#define shadow_rect__sz         0x04
#define shadow_rect__h_scale    0x08
#define sizeof__shadow_rect     0x09

#endif /* __ASSEMBLER__ */

#endif /* _SM64_SHADOW_H_ */
