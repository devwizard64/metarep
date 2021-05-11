#ifndef _SM64_SCRIPT_G_H_
#define _SM64_SCRIPT_G_H_

#include <sm64/script.h>

#define G_R_BACKGROUND          0
#define G_R_OPA_SURF            1
#define G_R_OPA_DECAL           2
#define G_R_OPA_INTER           3
#define G_R_TEX_EDGE            4
#define G_R_XLU_SURF            5
#define G_R_XLU_DECAL           6
#define G_R_XLU_INTER           7

#ifndef __ASSEMBLER__

#define g_script(script)                        \
    _C(0x00, 0, 0),                             \
    _P(script)
#define g_exit()                                \
    _C(0x01, 0, 0)
#define g_jump(script)                          \
    _C(0x02, 0, 0),                             \
    _P(script)
#define g_call(script)                          \
    _C(0x02, 1, 0),                             \
    _P(script)
#define g_return()                              \
    _C(0x03, 0, 0)
#define g_start()                               \
    _C(0x04, 0, 0)
#define g_end()                                 \
    _C(0x05, 0, 0)
/* 0x06 */
/* 0x07 */
#define g_world(x, y, w, h, n)                  \
    _C(0x08, 0, n),                             \
    _H(x, y),                                   \
    _H(w, h)
#define g_ortho(scale)                          \
    _C(0x09, 0, scale)
#define g_persp(fovy, n, f)                     \
    _C(0x0A, 0, fovy),                          \
    _H(n, f)
#define g_perspective(fovy, n, f, callback)     \
    _C(0x0A, 1, fovy),                          \
    _H(n, f),                                   \
    _P(callback)
#define g_empty()                               \
    _C(0x0B, 0, 0)
#define g_layer(depth)                          \
    _C(0x0C, depth, 0)
#define g_lod(min, max)                         \
    _C(0x0D, 0, 0),                             \
    _H(min, max)
#define g_select(arg, callback)                 \
    _C(0x0E, 0, arg),                           \
    _P(callback)
#define g_camera(arg, px, py, pz, lx, ly, lz, callback)    \
    _C(0x0F, 0, arg),                           \
    _H(px, py),                                 \
    _H(pz, lx),                                 \
    _H(ly, lz),                                 \
    _P(callback)
#define g_posrot(px, py, pz, rx, ry, rz)        \
    _C(0x10, 0x00, 0),                          \
    _H(px, py),                                 \
    _H(pz, rx),                                 \
    _H(ry, rz)
#define g_prp(px, py, pz)                       \
    _C(0x10, 0x10, px),                         \
    _H(py, pz)
#define g_prr(rx, ry, rz)                       \
    _C(0x10, 0x20, rx),                         \
    _H(ry, rz)
#define g_pry(ry)                               \
    _C(0x10, 0x30, ry)
#define g_gfx_posrot(rm, gfx, px, py, pz, rx, ry, rz)   \
    _C(0x10, 0x80 | G_R_##rm, 0),               \
    _H(px, py),                                 \
    _H(pz, rx),                                 \
    _H(ry, rz),                                 \
    _P(gfx)
#define g_gfx_prp(rm, gfx, px, py, pz)          \
    _C(0x10, 0x90 | G_R_##rm, px),              \
    _H(py, pz)
#define g_gfx_prr(rm, gfx, rx, ry, rz)          \
    _C(0x10, 0xA0 | G_R_##rm, rx),              \
    _H(ry, rz),                                 \
    _P(gfx)
#define g_gfx_pry(rm, gfx, ry)                  \
    _C(0x10, 0xB0 | G_R_##rm, ry),              \
    _P(gfx)
#define g_pos(px, py, pz)                       \
    _C(0x11, 0x00, px),                         \
    _H(py, pz)
#define g_gfx_pos(rm, gfx, px, py, pz)          \
    _C(0x11, 0x80 | G_R_##rm, px),              \
    _H(py, pz),                                 \
    _P(gfx)
#define g_rot(rx, ry, rz)                       \
    _C(0x12, 0x00, rx),                         \
    _H(ry, rz)
#define g_gfx_rot(rm, gfx, rx, ry, rz)          \
    _C(0x11, 0x80 | G_R_##rm, rx),              \
    _H(ry, rz),                                 \
    _P(gfx)
#define g_joint(rm, gfx, px, py, pz)            \
    _C(0x13, G_R_##rm, px),                     \
    _H(py, pz),                                 \
    _P(gfx)
#define g_billboard(px, py, pz)                 \
    _C(0x14, 0x00, px),                         \
    _H(py, pz)
#define g_gfx_billboard(rm, gfx, px, py, pz)    \
    _C(0x14, 0x80 | G_R_##rm, px),              \
    _H(py, pz),                                 \
    _P(gfx)
#define g_gfx(rm, gfx)                          \
    _C(0x15, G_R_##rm, 0),                      \
    _P(gfx)
#define g_shadow(scale, alpha, type)            \
    _C(0x16, 0, type),                          \
    _H(alpha, scale)
#define g_object()                              \
    _C(0x17, 0, 0)
#define g_callback(arg, callback)               \
    _C(0x18, 0, arg),                           \
    _P(callback)
#define g_background(arg, callback)             \
    _C(0x19, 0, arg),                           \
    _P(callback)
/* 0x1A */
/* 0x1B */
#define g_hand(px, py, pz, arg, callback)       \
    _C(0x1C, arg, px),                          \
    _H(py, pz),                                 \
    _P(callback)
#define g_scale(scale)                          \
    _C(0x1D, 0x00, 0),                          \
    _F(scale)
#define g_gfx_scale(rm, gfx, scale)             \
    _C(0x1D, 0x80 | G_R_##rm, 0),               \
    _F(scale),                                  \
    _P(gfx)
/* 0x1E */
/* 0x1F */
#define g_cull(distance)                        \
    _C(0x20, 0, distance)

extern void *player_demo_80257198(int, void *, void *); /* select */

extern void *player_gfx_802761D0(int, void *, void *); /* callback */
extern void *player_gfx_802763D4(int, void *, void *); /* background */
extern void *player_gfx_802764B0(int, void *, void *); /* callback */
extern void *g_player_alpha(int, void *, void *); /* callback */
extern void *g_player_select_lod(int, void *, void *); /* select */
extern void *g_player_select_eye(int, void *, void *); /* select */
extern void *g_player_rot_torso(int, void *, void *); /* callback */
extern void *g_player_rot_head(int, void *, void *); /* callback */
extern void *g_player_select_glove(int, void *, void *); /* select */
extern void *g_player_scale(int, void *, void *); /* callback */
extern void *g_player_select_cap(int, void *, void *); /* select */
extern void *g_player_select_head(int, void *, void *); /* select */
extern void *g_player_rot_wing(int, void *, void *); /* callback */
extern void *g_player_hand(int, void *, void *); /* hand */
extern void *g_inside_mirror(int, void *, void *); /* callback */
extern void *g_player_mirror(int, void *, void *); /* callback */

extern void *camera_80287D30(int, void *, void *); /* camera */
extern void *camera_8029AA3C(int, void *, void *); /* perspective */

extern void *object_8029D890(int, void *, void *); /* callback */
extern void *object_8029D924(int, void *, void *); /* callback */
extern void *object_8029DB48(int, void *, void *); /* select */
extern void *object_8029DBD4(int, void *, void *); /* select */
extern void *object_802A45E4(int, void *, void *); /* callback */

extern void *object_state_a_802A719C(int, void *, void *); /* callback */
extern void *g_mario_pos_child(int, void *, void *); /* callback */
extern void *object_state_a_802B798C(int, void *, void *); /* callback */
extern void *object_state_a_802B7C64(int, void *, void *); /* select */
extern void *object_state_a_802B7D44(int, void *, void *); /* callback */
extern void *object_state_a_802BA2B0(int, void *, void *); /* callback */
extern void *object_state_a_802BFBAC(int, void *, void *); /* select */

extern void *wipe_802CD1E8(int, void *, void *); /* callback */

extern void *scroll_802D0080(int, void *, void *); /* callback */
extern void *scroll_802D01E0(int, void *, void *); /* callback */
extern void *scroll_802D104C(int, void *, void *); /* callback */
extern void *scroll_802D1B70(int, void *, void *); /* callback */
extern void *scroll_802D1CDC(int, void *, void *); /* callback */
extern void *scroll_802D1E48(int, void *, void *); /* callback */
extern void *scroll_802D1FA8(int, void *, void *); /* callback */
extern void *scroll_802D2108(int, void *, void *); /* callback */

extern void *object_gfx_802D2360(int, void *, void *); /* callback */
extern void *object_gfx_802D2470(int, void *, void *); /* callback */
extern void *object_gfx_802D2520(int, void *, void *); /* callback */
extern void *object_gfx_802D28CC(int, void *, void *); /* callback */

extern void *ripple_802D5B98(int, void *, void *); /* callback */
extern void *ripple_802D5D0C(int, void *, void *); /* callback */

extern void *object_state_c_8030D93C(int, void *, void *); /* callback */
extern void *object_state_c_8030D9AC(int, void *, void *); /* callback */

extern void *title_bg_8016F670(int, void *, void *); /* callback */
extern void *title_bg_8016F984(int, void *, void *); /* callback */
extern void *title_bg_8016FE70(int, void *, void *); /* callback */
extern void *title_bg_8016FFFC(int, void *, void *); /* callback */

extern void *file_select_80176688(int, void *, void *); /* callback */

extern void *star_select_80177518(int, void *, void *); /* callback */

#endif /* __ASSEMBLER__ */

#endif /* _SM64_SCRIPT_G_H_ */
