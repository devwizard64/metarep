#ifndef _SM64_SCRIPT_G_H_
#define _SM64_SCRIPT_G_H_

#include <sm64/script.h>
#include <sm64/g.h>

#define G_NULL                  0
#define G_MARIO                 1
#define G_ENTITY_116            116
#define G_ENTITY_117            117
#define G_ENTITY_118            118
#define G_ENTITY_119            119
#define G_C0_120                120
#define G_ENTITY_121            121
#define G_ENTITY_122            122
#define G_ENTITY_124            124
#define G_C0_127                127
#define G_C0_128                128
#define G_C0_129                129
#define G_C0_130                130
#define G_C0_131                131
#define G_C0_132                132
#define G_ENTITY_133            133
#define G_ENTITY_134            134
#define G_ENTITY_135            135
#define G_ENTITY_136            136
#define G_C0_137                137
#define G_ENTITY_138            138
#define G_ENTITY_139            139
#define G_C0_140                140
#define G_ENTITY_142            142
#define G_GLOW                  143
#define G_ENTITY_144            144
#define G_ENTITY_145            145
#define G_SMOKE                 148
#define G_SPARKLE               149
#define G_DUST                  150
#define G_SMOKE2                156
#define G_ENTITY_158            158
#define G_ENTITY_159            159
#define G_ENTITY_160            160
#define G_ENTITY_161            161
#define G_ENTITY_162            162
#define G_RIPPLE_MOVE           163
#define G_DROPLET_WHITE         164
#define G_WAVE_WHITE            165
#define G_RIPPLE_STOP           166
#define G_SPLASH                167
#define G_BUBBLE_A              168
#define G_BUBBLE_B              170
#define G_C0_180                180
#define G_ENTITY_185            185
#define G_ENTITY_186            186
#define G_ENTITY_187            187
#define G_C0_188                188
#define G_C0_190                190
#define G_C0_192                192
#define G_C0_194                194
#define G_C0_195                195
#define G_ENTITY_200            200
#define G_C0_201                201
#define G_C0_202                202
#define G_ENTITY_203            203
#define G_ENTITY_204            204
#define G_ENTITY_205            205
#define G_C0_207                207
#define G_ENTITY_212            212
#define G_ENTITY_215            215
#define G_ENTITY_216            216
#define G_C0_217                217
#define G_C0_218                218
#define G_DIGIT                 219
#define G_C0_220                220
#define G_C0_223                223
#define G_ENTITY_224            224
#define G_C0_225                225

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

extern void *player_demo_80257198(int, struct g *, void *); /* select */

extern void *g_stage_particle(int, struct g *, void *);
extern void *g_stage_background(int, struct g *, void *);
extern void *g_face_main(int, struct g *, void *);
extern void *g_player_alpha(int, struct g *, void *);
extern void *g_player_select_lod(int, struct g *, void *);
extern void *g_player_select_eye(int, struct g *, void *);
extern void *g_player_rot_torso(int, struct g *, void *);
extern void *g_player_rot_head(int, struct g *, void *);
extern void *g_player_select_glove(int, struct g *, void *);
extern void *g_player_scale(int, struct g *, void *);
extern void *g_player_select_cap(int, struct g *, void *);
extern void *g_player_select_head(int, struct g *, void *);
extern void *g_player_rot_wing(int, struct g *, void *);
extern void *g_player_hand(int, struct g *, void *);
extern void *g_inside_mirror(int, struct g *, void *);
extern void *g_player_mirror(int, struct g *, void *);

extern void *g_stage_camera(int, struct g *, void *);
extern void *g_stage_perspective(int, struct g *, void *);

extern void *object_lib_8029D890(int, struct g *, void *); /* callback */
extern void *object_lib_8029D924(int, struct g *, void *); /* callback */
extern void *object_lib_8029DB48(int, struct g *, void *); /* select */
extern void *object_lib_8029DBD4(int, struct g *, void *); /* select */
extern void *object_lib_802A45E4(int, struct g *, void *); /* callback */

extern void *object_a_802A719C(int, struct g *, void *); /* callback */
extern void *g_mario_pos_child(int, struct g *, void *);
extern void *object_a_802B798C(int, struct g *, void *); /* callback */
extern void *object_a_802B7C64(int, struct g *, void *); /* select */
extern void *object_a_802B7D44(int, struct g *, void *); /* callback */
extern void *object_a_802BA2B0(int, struct g *, void *); /* callback */
extern void *object_a_802BFBAC(int, struct g *, void *); /* select */

extern void *wipe_802CD1E8(int, struct g *, void *); /* callback */

extern void *scroll_802D0080(int, struct g *, void *); /* callback */
extern void *scroll_802D01E0(int, struct g *, void *); /* callback */
extern void *scroll_802D104C(int, struct g *, void *); /* callback */
extern void *scroll_802D1B70(int, struct g *, void *); /* callback */
extern void *scroll_802D1CDC(int, struct g *, void *); /* callback */
extern void *scroll_802D1E48(int, struct g *, void *); /* callback */
extern void *scroll_802D1FA8(int, struct g *, void *); /* callback */
extern void *scroll_802D2108(int, struct g *, void *); /* callback */

extern void *object_gfx_802D2360(int, struct g *, void *); /* callback */
extern void *object_gfx_802D2470(int, struct g *, void *); /* callback */
extern void *object_gfx_802D2520(int, struct g *, void *); /* callback */
extern void *object_gfx_802D28CC(int, struct g *, void *); /* callback */

extern void *ripple_802D5B98(int, struct g *, void *); /* callback */
extern void *ripple_802D5D0C(int, struct g *, void *); /* callback */

extern void *object_c_8030D93C(int, struct g *, void *); /* callback */
extern void *object_c_8030D9AC(int, struct g *, void *); /* callback */

extern void *g_logo_shape(int, struct g *, void *);
extern void *g_logo_text(int, struct g *, void *);
extern void *g_title_bg(int, struct g *, void *);
extern void *g_gameover_bg(int, struct g *, void *);

extern void *g_file_select_main(int, struct g *, void *);

extern void *g_star_select_main(int, struct g *, void *);

#endif /* __ASSEMBLER__ */

#endif /* _SM64_SCRIPT_G_H_ */
