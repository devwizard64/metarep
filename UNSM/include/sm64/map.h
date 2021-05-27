#ifndef _SM64_MAP_H_
#define _SM64_MAP_H_

#include <sm64/types.h>

#define M_VTX                   0x40
#define M_BREAK                 0x41
#define M_END                   0x42
#define M_OBJ                   0x43
#define M_WATER                 0x44

#define M_O_COIN                1

#ifndef __ASSEMBLER__

struct map_face
{
    /* 0x00 */  s16     type;
    /* 0x02 */  s16     arg;
    /* 0x04 */  s8      flag;
    /* 0x05 */  s8      area;
    /* 0x06 */  s16     y_min;
    /* 0x08 */  s16     y_max;
    /* 0x0A */  vecs    v0;
    /* 0x10 */  vecs    v1;
    /* 0x16 */  vecs    v2;
    /* 0x1C */  f32     nx;
    /* 0x20 */  f32     ny;
    /* 0x24 */  f32     nz;
    /* 0x28 */  f32     nw;
    /* 0x2C */  struct object *obj;
};  /* 0x30 */

struct map_list
{
    /* 0x00 */  struct map_list *next;
    /* 0x04 */  struct map_face *face;
};  /* 0x08 */

#else /* __ASSEMBLER__ */

#define map_face__type          0x00
#define map_face__arg           0x02
#define map_face__flag          0x04
#define map_face__area          0x05
#define map_face__y_min         0x06
#define map_face__y_max         0x08
#define map_face__v0            0x0A
#define map_face__v0__0         0x0A
#define map_face__v0__1         0x0C
#define map_face__v0__2         0x0E
#define map_face__v1            0x10
#define map_face__v1__0         0x10
#define map_face__v1__1         0x12
#define map_face__v1__2         0x14
#define map_face__v2            0x16
#define map_face__v2__0         0x16
#define map_face__v2__1         0x18
#define map_face__v2__2         0x1A
#define map_face__nx            0x1C
#define map_face__ny            0x20
#define map_face__nz            0x24
#define map_face__nw            0x28
#define map_face__obj           0x2C
#define sizeof__map_face        0x30

#define map_list__next          0x00
#define map_list__face          0x02
#define sizeof__map_list        0x08

#endif /* __ASSEMBLER__ */

#endif /* _SM64_MAP_H_ */
