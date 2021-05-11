#ifndef _SM64_TYPES_H_
#define _SM64_TYPES_H_

#include <ultra64.h>

#define false   0
#define true    1

#define _STR(x)                 #x
#define STR(x)                  _STR(x)
#define _ASSET(x)               BUILD/x
#define ASSET(x)                STR(_ASSET(x))

#ifndef __ASSEMBLER__

typedef unsigned int uint;
typedef u8 bool;
typedef s16 vecs[3];
typedef f32 vecf[3];

#define aligned                 __attribute__((aligned(4)))
#define unused                  __attribute__((unused))
#define fallthrough             __attribute__((fallthrough))
#define lenof(x)                (sizeof((x)) / sizeof((x)[0]))

#endif /* __ASSEMBLER__ */

#endif /* _SM64_TYPES_H_ */
