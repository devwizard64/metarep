#ifndef _SM64_SCRIPT_O_H_
#define _SM64_SCRIPT_O_H_

#include <sm64/script.h>
#include <sm64/g_script.h>

#define O_T_PLAYER              0x00
#define O_T_0x01                0x01
#define O_T_PLAYERATTACK        0x02
#define O_T_0x03                0x03
#define O_T_OBJECTA             0x04
#define O_T_OBJECTB             0x05
#define O_T_ITEM                0x06
#define O_T_0x07                0x07
#define O_T_DEFAULT             0x08
#define O_T_MOVEBG              0x09
#define O_T_PLAYERUSE           0x0A
#define O_T_SYSTEM              0x0B
#define O_T_PARTICLE            0x0C

#define O_M_0x00                0x00
#define O_M_FLAG                0x01
#define O_M_0x02                0x02
#define O_M_0x03                0x03
#define O_M_0x04                0x04
#define O_M_0x05                0x05
#define O_M_0x06                0x06
#define O_M_0x07                0x07
#define O_M_0x08                0x08
#define O_M_0x09                0x09
#define O_M_0x0A                0x0A
#define O_M_0x0B                0x0B
#define O_M_0x0C                0x0C
#define O_M_0x0D                0x0D
#define O_M_0x0E                0x0E
#define O_M_0x0F                0x0F
#define O_M_0x10                0x10
#define O_M_0x11                0x11
#define O_M_0x12                0x12
#define O_M_0x13                0x13
#define O_M_0x14                0x14
#define O_M_0x15                0x15
#define O_M_0x16                0x16
#define O_M_0x17                0x17
#define O_M_0x18                0x18
#define O_M_0x19                0x19
#define O_M_0x1A                0x1A
#define O_M_0x1B                0x1B
#define O_M_0x1C                0x1C
#define O_M_0x1D                0x1D
#define O_M_0x1E                0x1E
#define O_M_0x1F                0x1F
#define O_M_0x20                0x20
#define O_M_0x21                0x21
#define O_M_0x22                0x22
#define O_M_0x23                0x23
#define O_M_0x24                0x24
#define O_M_0x25                0x25
#define O_M_MOTION              0x26
#define O_M_0x27                0x27
#define O_M_0x28                0x28
#define O_M_0x29                0x29
#define O_M_TOUCHTYPE           0x2A
#define O_M_TOUCH               0x2B
#define O_M_0x2C                0x2C
#define O_M_0x2D                0x2D
#define O_M_0x2E                0x2E
#define O_M_0x2F                0x2F
#define O_M_0x30                0x30
#define O_M_0x31                0x31
#define O_M_0x32                0x32
#define O_M_0x33                0x33
#define O_M_0x34                0x34
#define O_M_0x35                0x35
#define O_M_0x36                0x36
#define O_M_0x37                0x37
#define O_M_0x38                0x38
#define O_M_0x39                0x39
#define O_M_0x3A                0x3A
#define O_M_0x3B                0x3B
#define O_M_0x3C                0x3C
#define O_M_0x3D                0x3D
#define O_M_0x3E                0x3E
#define O_M_0x3F                0x3F
#define O_M_0x40                0x40
#define O_M_0x41                0x41
#define O_M_TOUCHARG            0x42
#define O_M_0x43                0x43
#define O_M_0x44                0x44
#define O_M_0x45                0x45
#define O_M_0x46                0x46
#define O_M_0x47                0x47
#define O_M_0x48                0x48
#define O_M_0x49                0x49
#define O_M_0x4A                0x4A
#define O_M_0x4B                0x4B
#define O_M_0x4C                0x4C
#define O_M_0x4D                0x4D
#define O_M_0x4E                0x4E
#define O_M_0x4F                0x4F

#ifdef __ASSEMBLER__

#define o_init(type)                            \
    _C(0x00, O_T_##type, 0)
#define o_sleep(time)                           \
    _C(0x01, 0, time)
#define o_call(script)                          \
    _C(0x02, 0, 0);                             \
    _P(script)
#define o_return()                              \
    _C(0x03, 0, 0)
#define o_jump(script)                          \
    _C(0x04, 0, 0);                             \
    _P(script)
#define o_for(count)                            \
    _C(0x05, 0, count)
#define o_fend()                                \
    _C(0x06, 0, 0)
#define o_fcontinue()                           \
    _C(0x07, 0, 0)
#define o_while()                               \
    _C(0x08, 0, 0)
#define o_wend()                                \
    _C(0x09, 0, 0)
#define o_exit()                                \
    _C(0x0A, 0, 0)
#define o_exit2()                               \
    _C(0x0B, 0, 0)
#define o_callback(callback)                    \
    _C(0x0C, 0, 0);                             \
    _P(callback)
#define o_addf(mem, val)                        \
    _C(0x0D, O_M_##mem, val)
#define o_setf(mem, val)                        \
    _C(0x0E, O_M_##mem, val)
#define o_addi(mem, val)                        \
    _C(0x0F, O_M_##mem, val)
#define o_seti(mem, val)                        \
    _C(0x10, O_M_##mem, val)
#define o_setflag(mem, val)                     \
    _C(0x11, O_M_##mem, val)
#define o_clrflag(mem, val)                     \
    _C(0x12, O_M_##mem, val)
#define o_setrandr(mem, val, shift)             \
    _C(0x13, O_M_##mem, val);                   \
    _H(shift, 0)
#define o_setrandf(mem, val, mul)               \
    _C(0x14, O_M_##mem, val);                   \
    _H(mul, 0)
#define o_setrandi(mem, val, mul)               \
    _C(0x15, O_M_##mem, val);                   \
    _H(mul, 0)
#define o_addrandf(mem, val, mul)               \
    _C(0x16, O_M_##mem, val);                   \
    _H(mul, 0)
#define o_addrandr(mem, val, shift)             \
    _C(0x17, O_M_##mem, val);                   \
    _H(shift, 0)
/* 0x18 */
/* 0x19 */
/* 0x1A */
#define o_gfx(gfx)                              \
    _C(0x1B, 0, gfx)
#define o_object(gfx, script)                   \
    _C(0x1C, 0, 0);                             \
    _W(gfx);                                    \
    _P(script)
#define o_destroy()                             \
    _C(0x1D, 0, 0)
#define o_ground()                              \
    _C(0x1E, 0, 0)
#define o_memaddf(mem, a, b)                    \
    _B(0x1F, O_M_##mem, O_M_##a, O_M_##b)
#define o_memaddi(mem, a, b)                    \
    _B(0x20, O_M_##mem, O_M_##a, O_M_##b)
#define o_billboard()                           \
    _C(0x21, 0, 0)
#define o_gfxhide()                             \
    _C(0x22, 0, 0)
#define o_hitbox(radius, height)                \
    _C(0x23, 0, 0);                             \
    _H(radius, height)
/* 0x24 */
#define o_memsleep(mem)                         \
    _C(0x25, O_M_##mem, 0)
#define o_for2(count)                           \
    _C(0x26, count, 0)
#define o_ptr(mem, ptr)                         \
    _C(0x27, O_M_##mem, 0);                     \
    _P(ptr)
#define o_motion(motion)                        \
    _C(0x28, motion, 0)
#define o_objectarg(gfx, script, arg)           \
    _C(0x29, 0, arg);                           \
    _W(gfx);                                    \
    _P(script)
#define o_map(map)                              \
    _C(0x2A, 0, 0);                             \
    _P(map)
#define o_hitboxoffset(radius, height, offset)  \
    _C(0x2B, 0, 0);                             \
    _H(radius, height);                         \
    _H(offset, 0)
#define o_child(gfx, script)                    \
    _C(0x2C, 0, 0);                             \
    _W(gfx);                                    \
    _P(script)
#define o_origin()                              \
    _C(0x2D, 0, 0)
#define o_hurtbox(radius, height)               \
    _C(0x2E, 0, 0);                             \
    _H(radius, height)
#define o_touchtype(type)                       \
    _C(0x2F, 0, 0);                             \
    _W(type)
#define o_move(a, b, c, d, e, f, g, h)          \
    _C(0x30, 0, 0);                             \
    _H(a, b);                                   \
    _H(c, d);                                   \
    _H(e, f);                                   \
    _H(g, h)
#define o_toucharg(arg)                         \
    _C(0x31, 0, 0);                             \
    _W(arg)
#define o_scale(scale)                          \
    _C(0x32, 0, scale)
#define o_memclrflag(mem, flag)                 \
    _C(0x33, O_M_##mem, 0);                     \
    _W(flag)
#define o_inc(mem, time)                        \
    _C(0x34, O_M_##mem, time)
#define o_gfxdisable()                          \
    _C(0x35, 0, 0)
#define o_sets(mem, val)                        \
    _C(0x36, 0, 0);                             \
    _W(val)
#define o_objdata(objdata)                      \
    _C(0x37, 0, 0);                             \
    _P(objdata)

#endif /* __ASSEMBLER__ */

#endif /* _SM64_SCRIPT_O_H_ */
