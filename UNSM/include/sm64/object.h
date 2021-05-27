#ifndef _SM64_OBJECT_H_
#define _SM64_OBJECT_H_

#include <sm64/types.h>
#include <sm64/g.h>

#ifndef __ASSEMBLER__

struct object
{
    /* 0x000 */ struct g_object g;
    /* 0x060 */ struct object *next;
    /* 0x064 */ struct object *prev;
    /* 0x068 */ struct object *parent;
    /* 0x06C */ struct object *child;
    /* 0x070 */ u32     touch;
    /* 0x074 */ s16     flag;
    /* 0x076 */ s16     touch_len;
    /* 0x078 */ struct object *obj_touch[4];
    /* 0x088 */ union
                {
                    s8      s8[4];
                    u8      u8[4];
                    s16     s16[2];
                    u16     u16[2];
                    s32     s32;
                    u32     u32;
                    f32     f32;
                    void   *ptr;
                }
                mem[80];
    /* 0x1C8 */ void   *_1C8;
    /* 0x1CC */ uintptr_t *pc;
    /* 0x1D0 */ uintptr_t  stack_index;
    /* 0x1D4 */ uintptr_t  stack[8];
    /* 0x1F4 */ s16     _1F4;
    /* 0x1F6 */ s16     _1F6;
    /* 0x1F8 */ f32     _1F8;
    /* 0x1FC */ f32     _1FC;
    /* 0x200 */ f32     _200;
    /* 0x204 */ f32     _204;
    /* 0x208 */ f32     _208;
    /* 0x20C */ uintptr_t *script;
    /* 0x210 */ struct object *_210;
    /* 0x214 */ struct object *_214;
    /* 0x218 */ s16    *_218;
    /* 0x21C */ mtxf    mf;
    /* 0x25C */ void   *_25C;
};  /* 0x260 */

#endif /* __ASSEMBLER__ */

#endif /* _SM64_OBJECT_H_ */
