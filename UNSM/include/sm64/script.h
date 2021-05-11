#ifndef _SM64_SCRIPT_H_
#define _SM64_SCRIPT_H_

#include <ultra64.h>

#ifndef __ASSEMBLER__

#define _C(c, x, y) ((u32)(u8)(c) << 24 | (u32)(u8)(x) << 16 | (u32)(u16)(y))
#define _H(x, y)    ((u32)(u16)(x) << 16 | (u32)(u16)(y))
#define _W(x)       ((u32)(x))
#define _F(x)       ((u32)(0x10000*(x)))
#define _P(x)       ((uintptr_t)(x))

#else /* __ASSEMBLER__ */

#define _B(c, x, y, z)      .byte (c), (x), (y), (z)
#define _C(c, x, y)         .byte (c), (x); .hword (y)
#define _H(x, y)            .hword (x), (y)
#define _W(x)               .word (x)
#define _F(x)               .float (x)
#define _P(x)               .word (x)

#endif /* __ASSEMBLER__ */

#endif /* _SM64_SCRIPT_H_ */
