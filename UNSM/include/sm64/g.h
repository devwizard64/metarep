#ifndef _SM64_G_H_
#define _SM64_G_H_

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct motion
{
    /* 0x00 */  s16    flag;
    /* 0x02 */  s16    height;
    /* 0x04 */  s16    start;
    /* 0x06 */  s16    end;
    /* 0x08 */  s16    frame;
    /* 0x0A */  s16    joint;
    /* 0x0C */  s16   *val;
    /* 0x10 */  u16   *tbl;
    /* 0x14 */  size_t size;
};  /* 0x18 */

struct skeleton
{
    /* 0x00 0x38 */ s16     index;
    /* 0x02 0x3A */ s16     height;
    /* 0x04 0x3C */ struct motion *motion;
    /* 0x08 0x40 */ s16     frame;
    /* 0x0A 0x42 */ u16     timer;
    /* 0x0C 0x44 */ s32     frame_amt;
    /* 0x10 0x48 */ s32     frame_vel;
};  /* 0x14 0x4C */

struct g
{
    /* 0x00 */  s16     type;
    /* 0x02 */  s16     flag;
    /* 0x04 */  struct g *prev;
    /* 0x08 */  struct g *next;
    /* 0x0C */  struct g *parent;
    /* 0x10 */  struct g *child;
};  /* 0x14 */

struct gc
{
    /* 0x00 */  struct g g;
    /* 0x14 */  void *(*callback)(int, struct g *, void *);
    /* 0x18 */  int     arg;
};  /* 0x1C */

struct gg
{
    /* 0x00 */  struct g g;
    /* 0x14 */  Gfx    *gfx;
};  /* 0x18 */

struct g_billboard
{
    /* 0x00 */  struct gg g;
    /* 0x18 */  vecs    pos;
};  /* 0x1E */

struct g_scale
{
    /* 0x00 */  struct gg g;
    /* 0x18 */  f32     scale;
};  /* 0x1C */

struct g_object
{
    /* 0x00 */  struct g g;
    /* 0x14 */  struct g *list;
    /* 0x18 */  s8      world;
    /* 0x19 */  s8      gfx;
    /* 0x1A */  vecs    rot;
    /* 0x20 */  vecf    pos;
    /* 0x2C */  vecf    scale;
    /* 0x38 */  struct skeleton skeleton;
    /* 0x4C */  void   *_4C;
    /* 0x50 */  mtxf   *mf;
    /* 0x54 */  vecf    pos_sfx;
};  /* 0x60 */

struct g_camera
{
    /* 0x00 */  struct gc g;
    /* 0x1C */  vecf    pos;
    /* 0x28 */  vecf    look;
    /* 0x34 */  mtxf   *mf;
    /* 0x38 */  s16     rz_m;
    /* 0x3A */  s16     rz_p;
};  /* 0x3C */

#else /* __ASSEMBLER__ */

#define g__type                 0x00
#define g__flag                 0x02
#define g__prev                 0x04
#define g__next                 0x08
#define g__parent               0x0C
#define g__child                0x10
#define sizeof__g               0x14

#define g_object__list          0x14
#define g_object__world         0x18

#endif /* __ASSEMBLER__ */

#endif /* _SM64_G_H_ */
