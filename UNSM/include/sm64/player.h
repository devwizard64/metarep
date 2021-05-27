#ifndef _SM64_PLAYER_H_
#define _SM64_PLAYER_H_

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct player_gfx
{
    /* 0x00 */  u32     state;
    /* 0x04 */  s8      head;
    /* 0x05 */  s8      eye;
    /* 0x06 */  s8      glove;
    /* 0x07 */  s8      wing;
    /* 0x08 */  s16     cap;
    /* 0x0A */  s8      hold;
    /* 0x0B */  u8      punch;
    /* 0x0C */  vecs    torso;
    /* 0x12 */  vecs    neck;
    /* 0x18 */  vecf    hand;
    /* 0x24 */  struct object *obj;
};  /* 0x28 */

struct player
{
    /* 0x00 */  u16     index;
    /* 0x02 */  u16     event;
    /* 0x04 */  u32     flag;
    /* 0x08 */  u32     particle;
    /* 0x0C */  u32     state;
    /* 0x10 */  u32     state_prev;
    /* 0x14 */  u32     ground_sfx;
    /* 0x18 */  s16     mode;
    /* 0x1A */  u16     timer;
    /* 0x1C */  u32     arg;
    /* 0x20 */  f32     stick_mag;
    /* 0x24 */  s16     stick_rot;
    /* 0x26 */  s16     invincible;
    /* 0x28 */  u8      timer_a;
    /* 0x29 */  u8      timer_b;
    /* 0x2A */  u8      timer_wall;
    /* 0x2B */  u8      timer_floor;
    /* 0x2C */  vecs    rot;
    /* 0x32 */  vecs    rot_vel;
    /* 0x38 */  s16     ry_slide;
    /* 0x3A */  s16     ry_twirl;
    /* 0x3C */  vecf    pos;
    /* 0x48 */  vecf    vel;
    /* 0x54 */  f32     vel_f;
    /* 0x58 */  f32     vel_h[2];
    /* 0x60 */  void   *wall;
    /* 0x64 */  void   *roof;
    /* 0x68 */  void   *ground;
    /* 0x6C */  f32     y_roof;
    /* 0x70 */  f32     y_ground;
    /* 0x74 */  s16     ry_ground;
    /* 0x76 */  s16     y_water;
    /* 0x78 */  struct object *obj_touch;
    /* 0x7C */  struct object *obj_hold;
    /* 0x80 */  struct object *obj_use;
    /* 0x84 */  struct object *obj_ride;
    /* 0x88 */  struct object *obj;
    /* 0x8C */  void   *_8C;
    /* 0x90 */  struct world *world;
    /* 0x94 */  struct player_cam *cam;
    /* 0x98 */  struct player_gfx *gfx;
    /* 0x9C */  struct controller *cnt;
    /* 0xA0 */  struct motion *motion;
    /* 0xA4 */  u32     touch;
    /* 0xA8 */  s16     coin;
    /* 0xAA */  s16     star;
    /* 0xAC */  s8      key;
    /* 0xAD */  s8      life;
    /* 0xAE */  s16     power;
    /* 0xB0 */  s16     motion_height;
    /* 0xB2 */  u8      timer_hurt;
    /* 0xB3 */  u8      timer_heal;
    /* 0xB4 */  u8      timer_squish;
    /* 0xB5 */  u8      timer_dither;
    /* 0xB6 */  u16     timer_cap;
    /* 0xB8 */  s16     star_prev;
    /* 0xBC */  f32     y_peak;
    /* 0xC0 */  f32     y_sink;
    /* 0xC4 */  f32     gravity;
};  /* 0xC8 */

#else /* __ASSEMBLER__ */

#define player_gfx__state       0x00
#define player_gfx__head        0x04
#define player_gfx__eye         0x05
#define player_gfx__glove       0x06
#define player_gfx__wing        0x07
#define player_gfx__cap         0x08
#define player_gfx__hold        0x0A
#define player_gfx__punch       0x0B
#define player_gfx__torso       0x0C
#define player_gfx__torso__0    0x0C
#define player_gfx__torso__1    0x0E
#define player_gfx__torso__2    0x10
#define player_gfx__neck        0x12
#define player_gfx__neck__0     0x12
#define player_gfx__neck__1     0x14
#define player_gfx__neck__2     0x16
#define player_gfx__hand        0x18
#define player_gfx__hand__0     0x18
#define player_gfx__hand__1     0x1C
#define player_gfx__hand__2     0x20
#define player_gfx__obj         0x24
#define sizeof__player_gfx      0x28

#define player__rot_vel         0x32
#define player__rot_vel__0      0x32
#define player__rot_vel__1      0x34
#define player__rot_vel__2      0x36
#define player__pos             0x3C
#define player__pos__0          0x3C
#define player__pos__1          0x40
#define player__pos__2          0x44
#define player__vel             0x48
#define player__vel__0          0x48
#define player__vel__1          0x4C
#define player__vel__2          0x50
#define sizeof__player          0xC8

#endif /* __ASSEMBLER__ */

#endif /* _SM64_PLAYER_H_ */
