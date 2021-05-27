#ifndef _SM64_WORLD_H_
#define _SM64_WORLD_H_

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct spawn
{
    /* 0x00 */  vecs    pos;
    /* 0x06 */  vecs    rot;
    /* 0x0C */  s8      world;
    /* 0x0D */  s8      _0D;
    /* 0x0E */  u16     _0E;
    /* 0x10 */  u32     _10;
    /* 0x14 */  const uintptr_t *script;
    /* 0x18 */  struct object *obj;
    /* 0x1C */  struct spawn *next;
};  /* 0x20 */

struct world
{
    /* 0x00 */  s8      index;
    /* 0x01 */  s8      _01;
    /* 0x02 */  u16     env;
    /* 0x04 */  struct g_world *g;
    /* 0x08 */  const s16 *map_data;
    /* 0x0C */  const s8  *area_data;
    /* 0x10 */  const s16 *obj_data;
    /* 0x14 */  void   *link;
    /* 0x18 */  void   *linkbg;
    /* 0x1C */  void   *linkw;
    /* 0x20 */  void   *spawn;
    /* 0x24 */  void   *cam;
    /* 0x28 */  void   *wind;
    /* 0x2C */  void   *jet[2];
    /* 0x34 */  u8      msg[2];
    /* 0x36 */  u16     bgm_arg;
    /* 0x38 */  u16     bgm_index;
    /* 0x3A */  u16     pad;
};  /* 0x3C */

#else /* __ASSEMBLER__ */

#define world__index            0x00
#define world__01               0x01
#define world__env              0x02
#define world__g                0x04
#define world__map_data         0x08
#define world__area_data        0x0C
#define world__obj_data         0x10
#define world__link             0x14
#define world__linkbg           0x18
#define world__linkw            0x1C
#define world__spawn            0x20
#define world__cam              0x24
#define world__wind             0x28
#define world__jet              0x2C
#define world__jet__0           0x2C
#define world__jet__1           0x30
#define world__msg              0x34
#define world__msg__0           0x34
#define world__msg__1           0x35
#define world__bgm_arg          0x36
#define world__bgm_index        0x38
#define sizeof__world           0x3C

#endif /* __ASSEMBLER__ */

#endif /* _SM64_WORLD_H_ */
