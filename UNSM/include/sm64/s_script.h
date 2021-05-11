#ifndef _SM64_SCRIPT_S_H_
#define _SM64_SCRIPT_S_H_

#include <sm64/segment.h>
#include <sm64/script.h>
#include <sm64/g_script.h>

#define S_O_END                 0x01E
#define S_O_COIN                0x01F
#define S_O_REDCOIN             0x023
#define S_O_CORKBOX             0x064
#define S_O_CORKBOXCOIN         0x065
#define S_O_METALBOX            0x065
#define S_O_SMALLBOX            0x067

#define S_C_AND             0x00
#define S_C_NAND            0x01
#define S_C_EQ              0x02
#define S_C_NE              0x03
#define S_C_GT              0x04
#define S_C_GE              0x05
#define S_C_LT              0x06
#define S_C_LE              0x07

#define S_V_SAVE            0x00
#define S_V_COURSE          0x01
#define S_V_LEVEL           0x02
#define S_V_STAGE           0x03
#define S_V_WORLD           0x04

#ifdef __ASSEMBLER__

#define s_mcall(seg, name, script)              \
    _C(0x00, 0x10, SEGMENT_DATA_##seg >> 24);   \
    _P(data_##name##_start);                    \
    _P(data_##name##_end);                      \
    _P(script)
#define s_mjump(seg, name, script)              \
    _C(0x01, 0x10, SEGMENT_DATA_##seg >> 24);   \
    _P(data_##name##_start);                    \
    _P(data_##name##_end);                      \
    _P(script)
#define s_mreturn()                             \
    _C(0x02, 0x04, 0)
#define s_sleep(x)                              \
    _C(0x03, 0x04, x)
#define s_freeze(x)                             \
    _C(0x04, 0x04, x)
#define s_jump(script)                          \
    _C(0x05, 0x08, 0);                          \
    _P(script)
#define s_call(script)                          \
    _C(0x06, 0x08, 0);                          \
    _P(script)
#define s_return()                              \
    _C(0x07, 0x04, 0)
#define s_for(count)                            \
    _C(0x08, 0x04, count)
#define s_done()                                \
    _C(0x09, 0x04, 0)
#define s_do()                                  \
    _C(0x0A, 0x04, 0)
#define s_while(c, val)                         \
    _B(0x0B, 0x08, S_C_##c, 0);                 \
    _W(val);
#define s_cjump(c, val, script)                 \
    _B(0x0C, 0x0C, S_C_##c, 0);                 \
    _W(val);                                    \
    _P(script)
#define s_ccall(c, val, script)                 \
    _B(0x0D, 0x0C, S_C_##c, 0);                 \
    _W(val);                                    \
    _P(script)
#define s_if(c, val)                            \
    _B(0x0E, 0x0C, S_C_##c, 0);                 \
    _W(val)
#define s_else()                                \
    _C(0x0F, 0x04, 0)
#define s_endif()                               \
    _C(0x10, 0x04, 0)
#define s_acall(callback, arg)                  \
    _C(0x11, 0x08, arg);                        \
    _P(callback)
#define s_aupdate(callback, arg)                \
    _C(0x12, 0x08, arg);                        \
    _P(callback)
#define s_aset(val)                             \
    _C(0x13, 0x04, val)
#define s_mpush()                               \
    _C(0x14, 0x04, 0)
#define s_mpop()                                \
    _C(0x15, 0x04, 0)
#define s_mcode(name)                           \
    _C(0x16, 0x10, 0);                          \
    _P(code_##name##_start);                    \
    _P(name##_start);                           \
    _P(name##_end)
#define s_mdata(seg, name)                      \
    _C(0x17, 0x0C, SEGMENT_DATA_##seg >> 24);   \
    _P(data_##name##_start);                    \
    _P(data_##name##_end)
#define s_mszp(seg, name)                       \
    _C(0x18, 0x0C, SEGMENT_SZP_##seg >> 24);    \
    _P(szp_##name##_start);                     \
    _P(szp_##name##_end)
#define s_mface(arg)                            \
    _C(0x19, 0x04, arg)
#define s_mtexture(seg, name)                   \
    _C(0x1A, 0x0C, SEGMENT_SZP_##seg >> 24);    \
    _P(szp_##name##_start);                     \
    _P(szp_##name##_end)
#define s_sinit()                               \
    _C(0x1B, 0x04, 0)
#define s_sdestroy()                            \
    _C(0x1C, 0x04, 0)
#define s_sstart()                              \
    _C(0x1D, 0x04, 0)
#define s_send()                                \
    _C(0x1E, 0x04, 0)
#define s_wstart(world, script)                 \
    _B(0x1F, 0x08, world, 0);                   \
    _P(script)
#define s_wend()                                \
    _C(0x20, 0x04, 0)
#define s_ggfx(g, gfx, rm)                      \
    _C(0x21, 0x08, G_R_##rm << 12 | (g));       \
    _P(gfx)
#define s_gscript(g, script)                    \
    _C(0x22, 0x08, g);                          \
    _P(script)
#define s_gscale(g, gfx, rm, scale)             \
    _C(0x23, 0x08, G_R_##rm << 12 | (g));       \
    _P(gfx);                                    \
    _F(scale)
#define s_object(mask, g, px, py, pz, rx, ry, rz, arg0, arg1, flag, script) \
    _B(0x24, 0x18, mask, g);                    \
    _H(px, py);                                 \
    _H(pz, rx);                                 \
    _H(ry, rz);                                 \
    _C(arg0, arg1, flag);                       \
    _P(script)
#define s_object_all(g, px, py, pz, rx, ry, rz, arg0, arg1, flag, script)   \
    s_object(0x1F, g, px, py, pz, rx, ry, rz, arg0, arg1, flag, script)
#define s_player(g, arg, script)                \
    _B(0x25, 0x0C, 0, g);                       \
    _W(arg);                                    \
    _P(script)
#define s_mario()                               \
    s_player(0x01, 1, o_mario)
#define s_link(index, stage, world, link)       \
    _B(0x26, 0x08, index, stage);               \
    _B(world, link, 0x00, 0)
#define s_linkm(index, stage, world, link)      \
    _B(0x26, 0x08, index, stage);               \
    _B(world, link, 0x80, 0)
#define s_linkbg(index, stage, world, link)     \
    _B(0x27, 0x08, index, stage);               \
    _B(world, link, 0x00, 0)
#define s_linkbgm(index, stage, world, link)    \
    _B(0x27, 0x08, index, stage);               \
    _B(world, link, 0x80, 0)
#define s_linkw(index, world, px, py, pz)       \
    _B(0x28, 0x0C, index, world);               \
    _H(px, py);                                 \
    _H(pz, 0)
#define s_winit(world)                          \
    _B(0x29, 0x04, world, 0)
#define s_wdestroy(world)                       \
    _B(0x2A, 0x04, world, 0)
#define s_pinit(world, ry, px, py, pz)          \
    _B(0x2B, 0x0C, world, 0);                   \
    _H(ry, px);                                 \
    _H(py, pz)
/* 0x2C pdestroy */
#define s_wupdate()                             \
    _C(0x2D, 0x08, 0)
#define s_map(map)                              \
    _C(0x2E, 0x08, 0);                          \
    _P(map)
#define s_area(area)                            \
    _C(0x2F, 0x08, 0);                          \
    _P(area)
#define s_msg(type, msg)                        \
    _B(0x30, 0x04, type, msg)
#define s_env(env)                              \
    _C(0x31, 0x04, env)
/* 0x32 */
#define s_wipe(type, time, r, g, b)             \
    _B(0x33, 0x08, type, time);                 \
    _B(r, g, b, 0)
#define s_viblack(arg)                          \
    _B(0x34, 0x04, arg, 0)
#define s_vigamma(arg)                          \
    _B(0x35, 0x04, arg, 0)
#define s_bgm(type, bgm)                        \
    _C(0x36, 0x08, type);                       \
    _H(bgm, 0)
#define s_bgmplay(bgm)                          \
    _C(0x37, 0x04, bgm)
#define s_bgmstop(time)                         \
    _C(0x38, 0x04, time)
#define s_obj(obj)                              \
    _C(0x39, 0x08, 0);                          \
    _P(obj)
/* 0x3A wind */
#define s_jet(index, mode, px, py, pz, arg)     \
    _B(0x3B, 0x0C, index, mode);                \
    _H(px, py);                                 \
    _H(pz, arg)
#define s_aw(var)                               \
    _B(0x3C, 0x04, 0, S_V_##var)
#define s_ar(var)                               \
    _B(0x3C, 0x04, 1, S_V_##var)

#endif /* __ASSEMBLER__ */

#endif /* _SM64_SCRIPT_S_H_ */
