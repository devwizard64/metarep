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
typedef s16 vecs[3];
typedef f32 vecf[3];
typedef f32 mtxf[4][4];

#define dalign                  __attribute__((aligned(4)))
#define balign                  __attribute__((aligned(8)))
#define unused                  __attribute__((unused))
#define fallthrough             __attribute__((fallthrough))
#define lenof(x)                (sizeof((x)) / sizeof((x)[0]))

#else /* __ASSEMBLER__ */

.macro li.u rt, imm
    .if (\imm) == 0
    .elseif ((\imm) & 0xFFFF8000) == 0 || ((\imm) & 0xFFFF8000) == 0xFFFF8000
    .elseif (\imm) >> 16 != 0
        lui     \rt, (\imm) >> 16
    .else
    .endif
.endm

.macro li.l rt, imm
    .if (\imm) == 0
        move    \rt, $0
    .elseif ((\imm) & 0xFFFF8000) == 0 || ((\imm) & 0xFFFF8000) == 0xFFFF8000
        addiu   \rt, $0, (\imm) & 0xFFFF
    .elseif (\imm) >> 16 != 0
        .if ((\imm) & 0xFFFF) != 0
            ori     \rt, \rt, (\imm) & 0xFFFF
        .endif
    .else
        ori     \rt, $0, (\imm) & 0xFFFF
    .endif
.endm

.macro li rt, imm
    li.u    \rt, \imm
    li.l    \rt, \imm
.endm

.macro la.u rt, imm
    lui     \rt, %hi(\imm)
.endm

.macro la.l rt, imm
    addiu   \rt, \rt, %lo(\imm)
.endm

#define struct(s, i, x)         (sizeof__##s*(i) + s##__##x)

#endif /* __ASSEMBLER__ */

#endif /* _SM64_TYPES_H_ */
