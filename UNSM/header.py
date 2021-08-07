import table

str_ultra_internal_c = """
#define dalign                  __attribute__((aligned(4)))
#define balign                  __attribute__((aligned(8)))
"""

str_ultra_parameters = """
.globl osTvType;        osTvType        = 0x80000300
.globl osRomType;       osRomType       = 0x80000304
.globl osRomBase;       osRomBase       = 0x80000308
.globl osResetType;     osResetType     = 0x8000030C
.globl osCicId;         osCicId         = 0x80000310
.globl osVersion;       osVersion       = 0x80000314
.globl osMemSize;       osMemSize       = 0x80000318
.globl osAppNMIBuffer;  osAppNMIBuffer  = 0x8000031C
.space 64
"""

str_sm64_globl = """
#include <sm64/types.h>
#include <sm64/gbi_ext.h>
#include <sm64/segment.h>

#include <sm64/main.h>
#include <sm64/app.h>
#include <sm64/audio.h>
#include <sm64/game.h>
#include <sm64/pl_collision.h>
#include <sm64/player.h>
#include <sm64/pl_physics.h>
#include <sm64/pl_demo.h>
#include <sm64/pl_hang.h>
#include <sm64/pl_stop.h>
#include <sm64/pl_ground.h>
#include <sm64/pl_air.h>
#include <sm64/pl_water.h>
#include <sm64/pl_grab.h>
#include <sm64/pl_callback.h>
#include <sm64/mem.h>
#include <sm64/save.h>
#include <sm64/world.h>
#include <sm64/shape_draw.h>
#include <sm64/time.h>
#include <sm64/slidec.h>
#include <sm64/camera.h>
#include <sm64/course.h>
#include <sm64/object.h>
#include <sm64/obj_lib.h>
#include <sm64/object_a.h>
#include <sm64/obj_physics.h>
#include <sm64/obj_collision.h>
#include <sm64/obj_list.h>
#include <sm64/obj_sfx.h>
#include <sm64/obj_debug.h>
#include <sm64/wipe.h>
#include <sm64/shadow.h>
#include <sm64/background.h>
#include <sm64/scroll.h>
#include <sm64/obj_shape.h>
#include <sm64/ripple.h>
#include <sm64/print.h>
#include <sm64/message.h>
#include <sm64/weather_snow.h>
#include <sm64/weather_lava.h>
#include <sm64/obj_data.h>
#include <sm64/hud.h>
#include <sm64/object_b.h>
#include <sm64/object_c.h>
#include <sm64/math.h>
#include <sm64/shape.h>
#include <sm64/s_script.h>
#include <sm64/p_script.h>
#include <sm64/map.h>
#include <sm64/map_data.h>
#include <sm64/o_script.h>
#include <sm64/title.h>
#include <sm64/title_bg.h>
#include <sm64/file_select.h>
#include <sm64/star_select.h>
#include <sm64/buffer.h>

#include <sm64/audio/a.h>
#include <sm64/audio/b.h>
#include <sm64/audio/c.h>
#include <sm64/audio/d.h>
#include <sm64/audio/e.h>
#include <sm64/audio/f.h>
#include <sm64/audio/g.h>
#include <sm64/audio/data.h>
#include <sm64/audio/bss.h>
#include <sm64/audio/heap.h>

#include <sm64/face/main.h>
#include <sm64/face/mem.h>
#include <sm64/face/sfx.h>
#include <sm64/face/draw.h>
#include <sm64/face/object.h>
#include <sm64/face/skin.h>
#include <sm64/face/particle.h>
#include <sm64/face/dynlist.h>
#include <sm64/face/gadget.h>
#include <sm64/face/stdio.h>
#include <sm64/face/joint.h>
#include <sm64/face/net.h>
#include <sm64/face/math.h>
#include <sm64/face/shape.h>
#include <sm64/face/gfx.h>
"""

str_types_globl = """
#include <ultra64.h>

#define false   0
#define true    1

#define _STR(x)                 #x
#define STR(x)                  _STR(x)
#define _ASSET(x)               BUILD/x
#define ASSET(x)                STR(_ASSET(x))
"""

str_types_c = """
typedef unsigned int uint;
typedef s16 vecs[3];
typedef f32 vecf[3];
typedef f32 mtxf[4][4];

#define dalign                  __attribute__((aligned(4)))
#define balign                  __attribute__((aligned(8)))
#define unused                  __attribute__((unused))
#define fallthrough             __attribute__((fallthrough))
#define lenof(x)                (sizeof((x)) / sizeof((x)[0]))

/* todo: move to header */
typedef u8 AREA_DATA;
typedef s16 PATH_DATA;
"""

str_types_asm = """
#define struct(s, i, x)         (sizeof__##s*(i) + s##__##x)

.macro li.u rt, imm
    .if (\\imm) == 0
    .elseif ((\\imm) & 0xFFFF8000) == 0 || ((\\imm) & 0xFFFF8000) == 0xFFFF8000
    .elseif (\\imm) >> 16 != 0
        lui     \\rt, (\\imm) >> 16
    .else
    .endif
.endm

.macro li.l rt, imm
    .if (\\imm) == 0
        move    \\rt, $0
    .elseif ((\\imm) & 0xFFFF8000) == 0 || ((\\imm) & 0xFFFF8000) == 0xFFFF8000
        addiu   \\rt, $0, (\\imm) & 0xFFFF
    .elseif (\\imm) >> 16 != 0
        .if ((\\imm) & 0xFFFF) != 0
            ori     \\rt, \\rt, (\\imm) & 0xFFFF
        .endif
    .else
        ori     \\rt, $0, (\\imm) & 0xFFFF
    .endif
.endm

.macro li rt, imm
    li.u    \\rt, \\imm
    li.l    \\rt, \\imm
.endm

.macro la.u rt, imm
    lui     \\rt, %hi(\\imm)
.endm

.macro la.l rt, imm
    addiu   \\rt, \\rt, %lo(\\imm)
.endm
"""

str_gbi_ext_c = """
#define G_CC_SHADE_ENV          0, 0, 0, SHADE, 0, 0, 0, ENVIRONMENT
#define G_CC_MODULATERGB_ENVA   TEXEL0, 0, SHADE, 0, 0, 0, 0, ENVIRONMENT
#define G_CC_MODULATERGBA_ENVA  TEXEL0, 0, SHADE, 0, TEXEL0, 0, ENVIRONMENT, 0
#define G_CC_MODULATERGBA_ENV   \\
    TEXEL0, 0, ENVIRONMENT, 0, TEXEL0, 0, ENVIRONMENT, 0
#define G_CC_DECALRGB_ENV       0, 0, 0, TEXEL0, 0, 0, 0, ENVIRONMENT
#define G_CC_DECALRGBA_ENV      0, 0, 0, TEXEL0, TEXEL0, 0, ENVIRONMENT, 0
#define G_CC_BLENDRGB_ENVA      \\
    TEXEL0, SHADE, TEXEL0_ALPHA, SHADE, 0, 0, 0, ENVIRONMENT
#define G_CC_MODULATESE         \\
    SHADE, 0, ENVIRONMENT, 0, SHADE, 0, ENVIRONMENT, 0

#define gdSPDefViewport(w, h, x, y) \\
{{                                  \\
    {2*(w), 2*(h), G_MAXZ/2, 0},    \\
    {4*(x), 4*(y), G_MAXZ/2, 0},    \\
}}

#define __gdSPDefMatrixI(x, y)  \\
    (((u32)(int)(0x10000*(x)) & ~0xFFFF) | (u32)(int)(0x10000*(y)) >> 16)
#define __gdSPDefMatrixF(x, y)  \\
    ((u32)(int)(0x10000*(x)) << 16 | ((u32)(int)(0x10000*(y)) & 0xFFFF))

#define gdSPDefMatrix(              \\
    m00, m01, m02, m03,             \\
    m10, m11, m12, m13,             \\
    m20, m21, m22, m23,             \\
    m30, m31, m32, m33              \\
)                                   \\
{{                                  \\
    {                               \\
        __gdSPDefMatrixI(m00, m01), \\
        __gdSPDefMatrixI(m02, m03), \\
        __gdSPDefMatrixI(m10, m11), \\
        __gdSPDefMatrixI(m12, m13), \\
    },                              \\
    {                               \\
        __gdSPDefMatrixI(m20, m21), \\
        __gdSPDefMatrixI(m22, m23), \\
        __gdSPDefMatrixI(m30, m31), \\
        __gdSPDefMatrixI(m32, m33), \\
    },                              \\
    {                               \\
        __gdSPDefMatrixF(m00, m01), \\
        __gdSPDefMatrixF(m02, m03), \\
        __gdSPDefMatrixF(m10, m11), \\
        __gdSPDefMatrixF(m12, m13), \\
    },                              \\
    {                               \\
        __gdSPDefMatrixF(m20, m21), \\
        __gdSPDefMatrixF(m22, m23), \\
        __gdSPDefMatrixF(m30, m31), \\
        __gdSPDefMatrixF(m32, m33), \\
    },                              \\
}}

#define gdSPDefLight(a, r, g, b)    \\
        gdSPDefLights1((a)*(r), (a)*(g), (a)*(b), r, g, b, 40, 40, 40)

#ifndef gsSP2Triangles
#define gsSP2Triangles(v00, v01, v02, flag0, v10, v11, v12, flag1)  \\
        gsSP1Triangle(v00, v01, v02, flag0),    \\
        gsSP1Triangle(v10, v11, v12, flag1)
#endif

#define gsSPSetLights1N(name)                                           \\
        gsSPLight(&name.l[0],1),                                        \\
        gsSPLight(&name.a,2)

#define gsDPLoadTextureBlockN(fmt, siz, width, height,                  \\
                pal, cms, cmt, masks, maskt, shifts, shiftt)            \\
                                                                        \\
        gsDPSetTile(fmt, siz##_LOAD_BLOCK, 0, 0,                        \\
                G_TX_LOADTILE,  0 , cmt, maskt, shiftt, cms,            \\
                masks, shifts),                                         \\
        gsDPLoadSync(),                                                 \\
        gsDPLoadBlock(G_TX_LOADTILE, 0, 0,                              \\
                (((width)*(height) + siz##_INCR) >> siz##_SHIFT)-1,     \\
                CALC_DXT(width, siz##_BYTES)),                          \\
        gsDPSetTile(fmt, siz, ((((width) * siz##_LINE_BYTES)+7)>>3), 0, \\
                G_TX_RENDERTILE, pal, cmt, maskt, shiftt, cms, masks,   \\
                shifts),                                                \\
        gsDPSetTileSize(G_TX_RENDERTILE, 0, 0,                          \\
                ((width)-1) << G_TEXTURE_IMAGE_FRAC,                    \\
                ((height)-1) << G_TEXTURE_IMAGE_FRAC)

#define gsDPLoadTextureBlock_4bN(fmt, width, height,                    \\
                pal, cms, cmt, masks, maskt, shifts, shiftt)            \\
                                                                        \\
        gsDPSetTile(fmt, G_IM_SIZ_16b, 0, 0, G_TX_LOADTILE, 0 , cmt,    \\
                maskt, shiftt, cms, masks, shifts),                     \\
        gsDPLoadSync(),                                                 \\
        gsDPLoadBlock(G_TX_LOADTILE, 0, 0, (((width)*(height)+3)>>2)-1, \\
                CALC_DXT_4b(width)),                                    \\
        gsDPSetTile(fmt, G_IM_SIZ_4b, ((((width)>>1)+7)>>3), 0,         \\
                G_TX_RENDERTILE, pal, cmt, maskt, shiftt, cms, masks,   \\
                shifts),                                                \\
        gsDPSetTileSize(G_TX_RENDERTILE, 0, 0,                          \\
                ((width)-1) << G_TEXTURE_IMAGE_FRAC,                    \\
                ((height)-1) << G_TEXTURE_IMAGE_FRAC)

#define gsDPLoadImageBlockT(timg, fmt, siz, width, height)              \\
                                                                        \\
        gsDPSetTextureImage(fmt, siz, 1, timg),                         \\
        gsDPTileSync(),                                                 \\
        gsDPSetTile(fmt, siz, 0, 0, G_TX_LOADTILE, 0,                   \\
                G_TX_WRAP, G_TX_NOMASK, G_TX_NOLOD,                     \\
                G_TX_WRAP, G_TX_NOMASK, G_TX_NOLOD),                    \\
        gsDPLoadSync(),                                                 \\
        gsDPLoadBlock(G_TX_LOADTILE, 0, 0, (width)*(height)-1,          \\
                CALC_DXT(width, siz##_BYTES))

#define gsDPLoadImageBlock(timg, fmt, siz, width, height)               \\
                                                                        \\
        gsDPSetTextureImage(fmt, siz, 1, timg),                         \\
        gsDPLoadSync(),                                                 \\
        gsDPLoadBlock(G_TX_LOADTILE, 0, 0, (width)*(height)-1,          \\
                CALC_DXT(width, siz##_BYTES))

#define gsDPSetImageBlock(fmt, siz, width, height,                      \\
                pal, cms, cmt, masks, maskt, shifts, shiftt)            \\
                                                                        \\
        gsDPTileSync(),                                                 \\
        gsDPSetTile(fmt, siz, ((((width) * siz##_LINE_BYTES)+7)>>3), 0, \\
                G_TX_RENDERTILE, pal, cmt, maskt, shiftt, cms, masks,   \\
                shifts),                                                \\
        gsDPSetTileSize(G_TX_RENDERTILE, 0, 0,                          \\
                ((width)-1) << G_TEXTURE_IMAGE_FRAC,                    \\
                ((height)-1) << G_TEXTURE_IMAGE_FRAC)
"""

str_segment_globl = """
#define SEGMENT_CIMG            0x8038F800
#define SEGMENT_ZIMG            0x80000400
#define SEGMENT_MEM_START       0x8005C000
#define SEGMENT_MEM_END         0x801C1000
#define SEGMENT_BUFFER          0x801C1000
#define SEGMENT_FIFO            0x80227000
#define SEGMENT_MAIN            0x80246000
#define SEGMENT_MAIN2           0x80378800
#define SEGMENT_MENU            0x8016F000

#define SEGMENT_DATA_FACE       0x04000000

#define SEGMENT_VIDEO           0x01000000
#define SEGMENT_SZP_MAIN        0x02000000
#define SEGMENT_SZP_ENTITY      0x03000000
#define SEGMENT_SZP_PLAYER      0x04000000
#define SEGMENT_SZP_SHAPEA      0x05000000
#define SEGMENT_SZP_SHAPEB      0x06000000
#define SEGMENT_SZP_STAGE       0x07000000
#define SEGMENT_SZP_MENU        0x07000000
#define SEGMENT_SZP_SHAPEC      0x08000000
#define SEGMENT_SZP_TEXTURE     0x09000000
#define SEGMENT_SZP_BACKGROUND  0x0A000000
#define SEGMENT_SZP_WEATHER     0x0B000000
#define SEGMENT_DATA_SHAPEA     0x0C000000
#define SEGMENT_DATA_SHAPEB     0x0D000000
#define SEGMENT_DATA_STAGE      0x0E000000
#define SEGMENT_DATA_SHAPEC     0x0F000000
#define SEGMENT_DATA_MAIN       0x10000000
#define SEGMENT_ANIME_MARIO     0x11000000
#define SEGMENT_ANIME_LUIGI     0x12000000
#define SEGMENT_DATA_OBJECT     0x13000000
#define SEGMENT_DATA_MENU       0x14000000
#define SEGMENT_DATA_GAME       0x15000000
#define SEGMENT_DATA_ENTITY     0x16000000
#define SEGMENT_DATA_PLAYER     0x17000000
#define SEGMENT_DEMO            0x18000000
"""

str_script_c = """
#define _C(c, x, y) ((u32)(u8)(c) << 24 | (u32)(u8)(x) << 16 | (u32)(u16)(y))
#define _H(x, y)    ((u32)(u16)(x) << 16 | (u32)(u16)(y))
#define _W(x)       ((u32)(x))
#define _F(x)       ((u32)(0x10000*(x)))
#define _P(x)       ((uintptr_t)(x))
"""

str_script_asm = """
#define _B(c, x, y, z)      .byte (c), (x), (y), (z)
#define _C(c, x, y)         .byte (c), (x); .short (y)
#define _H(x, y)            .short (x), (y)
#define _W(x)               .int (x)
#define _F(x)               .float (x)
#define _P(x)               .word (x)
"""

str_obj_data_globl = """
#define P_OBJ_END               30
#define P_OBJ_COIN              31
#define P_OBJ_REDCOIN           35
#define P_OBJ_CORKBOX           100
#define P_OBJ_CORKBOXCOIN       101
#define P_OBJ_METALBOX          102
#define P_OBJ_SMALLBOX          103

#define M_OBJ_COIN              1
"""

str_obj_data_c = """
typedef s16 OBJ_DATA;
"""

str_s_script_globl = """
#define S_NULL                  0

#define S_MARIO                 1
#define S_GLOW                  143
#define S_SMOKE                 148
#define S_SPARKLE               149
#define S_DUST                  150
#define S_SMOKE2                156
#define S_RIPPLE_MOVE           163
#define S_DROPLET_WHITE         164
#define S_WAVE_WHITE            165
#define S_RIPPLE_STOP           166
#define S_SPLASH                167
#define S_BUBBLE_A              168
#define S_BUBBLE_B              170

/* local */
#define S_ENTITY_18             18
#define S_ENTITY_22             22
#define S_ENTITY_23             23
#define S_ENTITY_24             24
#define S_ENTITY_25             25
#define S_ENTITY_27             27
#define S_ENTITY_28             28
#define S_ENTITY_29             29
#define S_ENTITY_31             31
#define S_ENTITY_32             32
#define S_ENTITY_34             34
#define S_ENTITY_35             35
#define S_ENTITY_36             36
#define S_ENTITY_37             37
#define S_ENTITY_38             38
#define S_ENTITY_39             39
#define S_ENTITY_41             41
#define S_ENTITY_73             73

#define S_ENTITY_116            116
#define S_ENTITY_117            117
#define S_ENTITY_118            118
#define S_ENTITY_119            119
#define S_ENTITY_121            121
#define S_ENTITY_122            122
#define S_ENTITY_124            124
#define S_ENTITY_133            133
#define S_ENTITY_134            134
#define S_ENTITY_135            135
#define S_ENTITY_136            136
#define S_ENTITY_138            138
#define S_ENTITY_139            139
#define S_ENTITY_142            142
#define S_ENTITY_144            144
#define S_ENTITY_145            145
#define S_ENTITY_158            158
#define S_ENTITY_159            159
#define S_ENTITY_160            160
#define S_ENTITY_161            161
#define S_ENTITY_162            162
#define S_ENTITY_185            185
#define S_ENTITY_186            186
#define S_ENTITY_187            187
#define S_ENTITY_200            200
#define S_ENTITY_203            203
#define S_ENTITY_204            204
#define S_ENTITY_205            205
#define S_ENTITY_212            212
#define S_ENTITY_215            215
#define S_ENTITY_216            216
#define S_DIGIT                 219
#define S_ENTITY_224            224

#define S_C0_120                120
#define S_C0_127                127
#define S_C0_128                128
#define S_C0_129                129
#define S_C0_130                130
#define S_C0_131                131
#define S_C0_132                132
#define S_C0_137                137
#define S_C0_140                140
#define S_C0_180                180
#define S_C0_188                188
#define S_C0_190                190
#define S_C0_192                192
#define S_C0_194                194
#define S_C0_195                195
#define S_C0_201                201
#define S_C0_202                202
#define S_C0_207                207
#define S_C0_217                217
#define S_C0_218                218
#define S_C0_220                220
#define S_C0_223                223
#define S_C0_225                225

#define S_A0_84                 84
#define S_A0_85                 85
#define S_A0_86                 86
#define S_A0_87                 87
#define S_A0_88                 88
#define S_A0_89                 89

#define S_A1_84                 84
#define S_A1_86                 86
#define S_A1_87                 87

#define S_A2_84                 84
#define S_A2_85                 85
#define S_A2_86                 86

#define S_A3_84                 84
#define S_A3_85                 85
#define S_A3_86                 86
#define S_A3_87                 87
#define S_A3_88                 88

#define S_A4_84                 84
#define S_A4_85                 85
#define S_A4_86                 86
#define S_A4_87                 87
#define S_A4_88                 88
#define S_A4_89                 89

#define S_A5_84                 84
#define S_A5_85                 85
#define S_A5_86                 86
#define S_A5_87                 87

#define S_A6_84                 84
#define S_A6_85                 85
#define S_A6_86                 86
#define S_A6_87                 87

#define S_A7_84                 84
#define S_A7_85                 85
#define S_A7_86                 86

#define S_A8_84                 84
#define S_A8_85                 85
#define S_A8_86                 86
#define S_A8_87                 87
#define S_A8_88                 88
#define S_A8_89                 89
#define S_A8_90                 90

#define S_A9_84                 84
#define S_A9_85                 85
#define S_A9_222                222

#define S_A10_84                84
#define S_A10_85                85
#define S_A10_86                86
#define S_A10_87                87
#define S_A10_88                88
#define S_A10_89                89

/* local */
#define S_B0_3                  3

#define S_B0_100                100
#define S_B0_101                101
#define S_B0_102                102
#define S_B0_103                103
#define S_B0_104                104
#define S_B0_105                105
#define S_B0_179                179

#define S_B1_100                100
#define S_B1_101                101
#define S_B1_102                102
#define S_B1_103                103
#define S_B1_104                104
#define S_B1_105                105
#define S_B1_179                179
#define S_B1_193                193

#define S_B2_100                100
#define S_B2_101                101
#define S_B2_102                102
#define S_B2_103                103
#define S_B2_104                104
#define S_B2_106                106
#define S_B2_107                107
#define S_B2_191                191

#define S_B3_100                100
#define S_B3_101                101
#define S_B3_102                102
#define S_B3_221                221

#define S_B4_100                100
#define S_B4_101                101
#define S_B4_102                102

#define S_B5_100                100
#define S_B5_101                101
#define S_B5_102                102
#define S_B5_103                103
#define S_B5_104                104
#define S_B5_206                206

#define S_SELECT_3              3
#define S_SELECT_4              4
#define S_SELECT_5              5
#define S_SELECT_6              6
#define S_SELECT_7              7
#define S_SELECT_8              8
#define S_SELECT_9              9
#define S_SELECT_10             10
#define S_SELECT_11             11
#define S_SELECT_12             12

#define S_BBH_53                53
#define S_BBH_54                54
#define S_BBH_55                55
#define S_BBH_56                56
#define S_BBH_57                57
#define S_BBH_58                58
#define S_BBH_59                59
#define S_BBH_60                60

#define S_CCM_3                 3
#define S_CCM_4                 4
#define S_CCM_5                 5
#define S_CCM_6                 6
#define S_CCM_7                 7
#define S_CCM_54                54
#define S_CCM_55                55
#define S_CCM_210               210

#define S_INSIDE_53             53
#define S_INSIDE_54             54
#define S_INSIDE_55             55
#define S_INSIDE_56             56
#define S_INSIDE_57             57
#define S_INSIDE_208            208
#define S_INSIDE_209            209
#define S_INSIDE_213            213
#define S_INSIDE_214            214

#define S_HMC_54                54
#define S_HMC_55                55
#define S_HMC_56                56
#define S_HMC_57                57
#define S_HMC_58                58
#define S_HMC_59                59
#define S_HMC_60                60

#define S_SSL_3                 3
#define S_SSL_4                 4
#define S_SSL_54                54
#define S_SSL_55                55
#define S_SSL_56                56
#define S_SSL_57                57
#define S_SSL_58                58
#define S_SSL_199               199

#define S_BOB_54                54
#define S_BOB_55                55
#define S_BOB_56                56

#define S_SL_54                 54
#define S_SL_55                 55
#define S_SL_56                 56

#define S_WDW_54                54
#define S_WDW_55                55
#define S_WDW_56                56
#define S_WDW_57                57
#define S_WDW_58                58
#define S_WDW_59                59
#define S_WDW_60                60

#define S_JRB_53                53
#define S_JRB_54                54
#define S_JRB_55                55
#define S_JRB_56                56
#define S_JRB_57                57
#define S_JRB_58                58
#define S_JRB_59                59
#define S_JRB_60                60
#define S_JRB_61                61
#define S_JRB_62                62
#define S_JRB_63                63

#define S_THI_3                 3
#define S_THI_54                54
#define S_THI_55                55

#define S_TTC_54                54
#define S_TTC_55                55
#define S_TTC_56                56
#define S_TTC_57                57
#define S_TTC_58                58
#define S_TTC_59                59
#define S_TTC_60                60
#define S_TTC_61                61
#define S_TTC_62                62
#define S_TTC_63                63
#define S_TTC_64                64
#define S_TTC_65                65
#define S_TTC_66                66
#define S_TTC_67                67
#define S_TTC_68                68

#define S_RR_3                  3
#define S_RR_4                  4
#define S_RR_5                  5
#define S_RR_6                  6
#define S_RR_7                  7
#define S_RR_8                  8
#define S_RR_9                  9
#define S_RR_10                 10
#define S_RR_11                 11
#define S_RR_12                 12
#define S_RR_13                 13
#define S_RR_14                 14
#define S_RR_15                 15
#define S_RR_16                 16
#define S_RR_17                 17
#define S_RR_18                 18
#define S_RR_19                 19
#define S_RR_20                 20
#define S_RR_21                 21
#define S_RR_22                 22
#define S_RR_54                 54
#define S_RR_55                 55
#define S_RR_56                 56
#define S_RR_57                 57
#define S_RR_58                 58
#define S_RR_59                 59
#define S_RR_60                 60
#define S_RR_61                 61
#define S_RR_62                 62
#define S_RR_63                 63
#define S_RR_64                 64
#define S_RR_65                 65
#define S_RR_66                 66
#define S_RR_67                 67
#define S_RR_68                 68
#define S_RR_69                 69

#define S_GROUNDS_3             3
#define S_GROUNDS_54            54
#define S_GROUNDS_55            55
#define S_GROUNDS_56            56

#define S_BITDW_3               3
#define S_BITDW_4               4
#define S_BITDW_5               5
#define S_BITDW_6               6
#define S_BITDW_7               7
#define S_BITDW_8               8
#define S_BITDW_9               9
#define S_BITDW_10              10
#define S_BITDW_11              11
#define S_BITDW_12              12
#define S_BITDW_13              13
#define S_BITDW_14              14
#define S_BITDW_15              15
#define S_BITDW_16              16
#define S_BITDW_17              17
#define S_BITDW_54              54
#define S_BITDW_55              55
#define S_BITDW_56              56
#define S_BITDW_57              57
#define S_BITDW_58              58
#define S_BITDW_59              59
#define S_BITDW_60              60
#define S_BITDW_61              61
#define S_BITDW_62              62
#define S_BITDW_63              63

#define S_VCUTM_54              54

#define S_BITFS_3               3
#define S_BITFS_4               4
#define S_BITFS_5               5
#define S_BITFS_6               6
#define S_BITFS_7               7
#define S_BITFS_8               8
#define S_BITFS_9               9
#define S_BITFS_10              10
#define S_BITFS_11              11
#define S_BITFS_12              12
#define S_BITFS_13              13
#define S_BITFS_14              14
#define S_BITFS_15              15
#define S_BITFS_16              16
#define S_BITFS_17              17
#define S_BITFS_18              18
#define S_BITFS_19              19
#define S_BITFS_20              20
#define S_BITFS_21              21
#define S_BITFS_54              54
#define S_BITFS_55              55
#define S_BITFS_56              56
#define S_BITFS_57              57
#define S_BITFS_58              58
#define S_BITFS_59              59
#define S_BITFS_60              60
#define S_BITFS_61              61
#define S_BITFS_62              62
#define S_BITFS_63              63
#define S_BITFS_64              64
#define S_BITFS_65              65

#define S_BITS_3                3
#define S_BITS_4                4
#define S_BITS_5                5
#define S_BITS_6                6
#define S_BITS_7                7
#define S_BITS_8                8
#define S_BITS_9                9
#define S_BITS_10               10
#define S_BITS_11               11
#define S_BITS_12               12
#define S_BITS_13               13
#define S_BITS_14               14
#define S_BITS_15               15
#define S_BITS_16               16
#define S_BITS_17               17
#define S_BITS_18               18
#define S_BITS_19               19
#define S_BITS_20               20
#define S_BITS_54               54
#define S_BITS_55               55
#define S_BITS_57               57
#define S_BITS_60               60
#define S_BITS_61               61
#define S_BITS_62               62
#define S_BITS_63               63
#define S_BITS_64               64
#define S_BITS_65               65
#define S_BITS_66               66
#define S_BITS_67               67
#define S_BITS_68               68
#define S_BITS_69               69

#define S_LLL_3                 3
#define S_LLL_4                 4
#define S_LLL_5                 5
#define S_LLL_6                 6
#define S_LLL_7                 7
#define S_LLL_8                 8
#define S_LLL_9                 9
#define S_LLL_10                10
#define S_LLL_11                11
#define S_LLL_12                12
#define S_LLL_13                13
#define S_LLL_14                14
#define S_LLL_53                53
#define S_LLL_54                54
#define S_LLL_55                55
#define S_LLL_56                56
#define S_LLL_57                57
#define S_LLL_58                58
#define S_LLL_59                59
#define S_LLL_60                60
#define S_LLL_61                61
#define S_LLL_62                62
#define S_LLL_63                63
#define S_LLL_64                64
#define S_LLL_65                65
#define S_LLL_67                67
#define S_LLL_68                68
#define S_LLL_69                69
#define S_LLL_70                70
#define S_LLL_71                71
#define S_LLL_72                72
#define S_LLL_73                73
#define S_LLL_74                74
#define S_LLL_75                75
#define S_LLL_76                76
#define S_LLL_77                77
#define S_LLL_78                78
#define S_LLL_79                79
#define S_LLL_80                80
#define S_LLL_83                83

#define S_DDD_54                54
#define S_DDD_55                55
#define S_DDD_56                56

#define S_WF_3                  3
#define S_WF_4                  4
#define S_WF_5                  5
#define S_WF_6                  6
#define S_WF_7                  7
#define S_WF_8                  8
#define S_WF_9                  9
#define S_WF_10                 10
#define S_WF_12                 12
#define S_WF_13                 13
#define S_WF_14                 14
#define S_WF_15                 15
#define S_WF_16                 16
#define S_WF_17                 17
#define S_WF_18                 18
#define S_WF_44                 44
#define S_WF_45                 45
#define S_WF_46                 46
#define S_WF_47                 47
#define S_WF_54                 54
#define S_WF_55                 55
#define S_WF_56                 56
#define S_WF_57                 57
#define S_WF_58                 58
#define S_WF_173                173
#define S_WF_174                174
#define S_WF_175                175
#define S_WF_176                176
#define S_WF_177                177
#define S_WF_178                178

#define S_COURTYARD_3           3

#define S_TOTWC_3               3

#define S_BITFSA_54             54

#define S_BITSA_3               3
#define S_BITSA_54              54
#define S_BITSA_55              55
#define S_BITSA_56              56
#define S_BITSA_57              57
#define S_BITSA_58              58
#define S_BITSA_59              59
#define S_BITSA_60              60
#define S_BITSA_61              61
#define S_BITSA_62              62
#define S_BITSA_63              63

#define S_TTM_3                 3
#define S_TTM_4                 4
#define S_TTM_5                 5
#define S_TTM_6                 6
#define S_TTM_7                 7
#define S_TTM_8                 8
#define S_TTM_9                 9
#define S_TTM_10                10
#define S_TTM_11                11
#define S_TTM_12                12
#define S_TTM_13                13
#define S_TTM_15                15
#define S_TTM_16                16
#define S_TTM_17                17
#define S_TTM_18                18
#define S_TTM_19                19
#define S_TTM_20                20
#define S_TTM_21                21
#define S_TTM_22                22
#define S_TTM_53                53
#define S_TTM_54                54
#define S_TTM_55                55
#define S_TTM_56                56
#define S_TTM_57                57
#define S_TTM_58                58
#define S_TTM_123               123

#define S_LAYER_BACKGROUND      0
#define S_LAYER_OPA_SURF        1
#define S_LAYER_OPA_DECAL       2
#define S_LAYER_OPA_INTER       3
#define S_LAYER_TEX_EDGE        4
#define S_LAYER_XLU_SURF        5
#define S_LAYER_XLU_DECAL       6
#define S_LAYER_XLU_INTER       7
"""

str_s_script_c = """
#define s_script(script)                        \\
    _C(0x00, 0, 0),                             \\
    _P(script)
#define s_exit()                                \\
    _C(0x01, 0, 0)
#define s_jump(script)                          \\
    _C(0x02, 0, 0),                             \\
    _P(script)
#define s_call(script)                          \\
    _C(0x02, 1, 0),                             \\
    _P(script)
#define s_return()                              \\
    _C(0x03, 0, 0)
#define s_push()                                \\
    _C(0x04, 0, 0)
#define s_pull()                                \\
    _C(0x05, 0, 0)
/* 0x06 */
/* 0x07 */
#define s_world(x, y, w, h, n)                  \\
    _C(0x08, 0, n),                             \\
    _H(x, y),                                   \\
    _H(w, h)
#define s_ortho(scale)                          \\
    _C(0x09, 0, scale)
#define s_persp(fovy, n, f)                     \\
    _C(0x0A, 0, fovy),                          \\
    _H(n, f)
#define s_perspective(fovy, n, f, callback)     \\
    _C(0x0A, 1, fovy),                          \\
    _H(n, f),                                   \\
    _P(callback)
#define s_empty()                               \\
    _C(0x0B, 0, 0)
#define s_layer(depth)                          \\
    _C(0x0C, depth, 0)
#define s_lod(min, max)                         \\
    _C(0x0D, 0, 0),                             \\
    _H(min, max)
#define s_select(arg, callback)                 \\
    _C(0x0E, 0, arg),                           \\
    _P(callback)
#define s_camera(arg, px, py, pz, lx, ly, lz, callback)    \\
    _C(0x0F, 0, arg),                           \\
    _H(px, py),                                 \\
    _H(pz, lx),                                 \\
    _H(ly, lz),                                 \\
    _P(callback)
#define s_posrot(px, py, pz, rx, ry, rz)        \\
    _C(0x10, 0x00, 0),                          \\
    _H(px, py),                                 \\
    _H(pz, rx),                                 \\
    _H(ry, rz)
#define s_prp(px, py, pz)                       \\
    _C(0x10, 0x10, px),                         \\
    _H(py, pz)
#define s_prr(rx, ry, rz)                       \\
    _C(0x10, 0x20, rx),                         \\
    _H(ry, rz)
#define s_pry(ry)                               \\
    _C(0x10, 0x30, ry)
#define s_gfx_posrot(layer, gfx, px, py, pz, rx, ry, rz)    \\
    _C(0x10, 0x80 | S_LAYER_##layer, 0),        \\
    _H(px, py),                                 \\
    _H(pz, rx),                                 \\
    _H(ry, rz),                                 \\
    _P(gfx)
#define s_gfx_prp(layer, gfx, px, py, pz)       \\
    _C(0x10, 0x90 | S_LAYER_##layer, px),       \\
    _H(py, pz)
#define s_gfx_prr(layer, gfx, rx, ry, rz)       \\
    _C(0x10, 0xA0 | S_LAYER_##layer, rx),       \\
    _H(ry, rz),                                 \\
    _P(gfx)
#define s_gfx_pry(layer, gfx, ry)               \\
    _C(0x10, 0xB0 | S_LAYER_##layer, ry),       \\
    _P(gfx)
#define s_pos(px, py, pz)                       \\
    _C(0x11, 0x00, px),                         \\
    _H(py, pz)
#define s_gfx_pos(layer, gfx, px, py, pz)       \\
    _C(0x11, 0x80 | S_LAYER_##layer, px),       \\
    _H(py, pz),                                 \\
    _P(gfx)
#define s_rot(rx, ry, rz)                       \\
    _C(0x12, 0x00, rx),                         \\
    _H(ry, rz)
#define s_gfx_rot(layer, gfx, rx, ry, rz)       \\
    _C(0x11, 0x80 | S_LAYER_##layer, rx),       \\
    _H(ry, rz),                                 \\
    _P(gfx)
#define s_joint(layer, gfx, px, py, pz)         \\
    _C(0x13, S_LAYER_##layer, px),              \\
    _H(py, pz),                                 \\
    _P(gfx)
#define s_billboard(px, py, pz)                 \\
    _C(0x14, 0x00, px),                         \\
    _H(py, pz)
#define s_gfx_billboard(layer, gfx, px, py, pz) \\
    _C(0x14, 0x80 | S_LAYER_##layer, px),       \\
    _H(py, pz),                                 \\
    _P(gfx)
#define s_gfx(layer, gfx)                       \\
    _C(0x15, S_LAYER_##layer, 0),               \\
    _P(gfx)
#define s_shadow(scale, alpha, type)            \\
    _C(0x16, 0, type),                          \\
    _H(alpha, scale)
#define s_object()                              \\
    _C(0x17, 0, 0)
#define s_callback(arg, callback)               \\
    _C(0x18, 0, arg),                           \\
    _P(callback)
#define s_background(arg, callback)             \\
    _C(0x19, 0, arg),                           \\
    _P(callback)
/* 0x1A */
/* 0x1B */
#define s_hand(px, py, pz, arg, callback)       \\
    _C(0x1C, arg, px),                          \\
    _H(py, pz),                                 \\
    _P(callback)
#define s_scale(scale)                          \\
    _C(0x1D, 0x00, 0),                          \\
    _F(scale)
#define s_gfx_scale(layer, gfx, scale)          \\
    _C(0x1D, 0x80 | S_LAYER_##layer, 0),        \\
    _F(scale),                                  \\
    _P(gfx)
/* 0x1E */
/* 0x1F */
#define s_cull(distance)                        \\
    _C(0x20, 0, distance)

typedef uintptr_t S_SCRIPT;

extern void *s_pl_demo_80257198(int, struct shape *, void *); /* select */

extern void *s_stage_weather(int, struct shape *, void *);
extern void *s_stage_background(int, struct shape *, void *);
extern void *s_face_main(int, struct shape *, void *);
extern void *s_player_alpha(int, struct shape *, void *);
extern void *s_player_select_lod(int, struct shape *, void *);
extern void *s_player_select_eye(int, struct shape *, void *);
extern void *s_player_rot_torso(int, struct shape *, void *);
extern void *s_player_rot_head(int, struct shape *, void *);
extern void *s_player_select_glove(int, struct shape *, void *);
extern void *s_player_scale(int, struct shape *, void *);
extern void *s_player_select_cap(int, struct shape *, void *);
extern void *s_player_select_head(int, struct shape *, void *);
extern void *s_player_rot_wing(int, struct shape *, void *);
extern void *s_player_hand(int, struct shape *, void *);
extern void *s_inside_mirror(int, struct shape *, void *);
extern void *s_player_mirror(int, struct shape *, void *);

extern void *s_stage_camera(int, struct shape *, void *);
extern void *s_stage_perspective(int, struct shape *, void *);

extern void *s_obj_lib_8029D890(int, struct shape *, void *); /* callback */
extern void *s_obj_lib_8029D924(int, struct shape *, void *); /* callback */
extern void *s_obj_lib_8029DB48(int, struct shape *, void *); /* select */
extern void *s_obj_lib_8029DBD4(int, struct shape *, void *); /* select */
extern void *s_obj_lib_802A45E4(int, struct shape *, void *); /* callback */

extern void *s_object_a_802A719C(int, struct shape *, void *); /* callback */
extern void *s_mario_pos_child(int, struct shape *, void *);
extern void *s_object_a_802B798C(int, struct shape *, void *); /* callback */
extern void *s_object_a_802B7C64(int, struct shape *, void *); /* select */
extern void *s_object_a_802B7D44(int, struct shape *, void *); /* callback */
extern void *s_object_a_802BA2B0(int, struct shape *, void *); /* callback */
extern void *s_object_a_802BFBAC(int, struct shape *, void *); /* select */

extern void *s_wipe_802CD1E8(int, struct shape *, void *); /* callback */

extern void *s_scroll_802D0080(int, struct shape *, void *); /* callback */
extern void *s_scroll_802D01E0(int, struct shape *, void *); /* callback */
extern void *s_scroll_802D104C(int, struct shape *, void *); /* callback */
extern void *s_scroll_802D1B70(int, struct shape *, void *); /* callback */
extern void *s_scroll_802D1CDC(int, struct shape *, void *); /* callback */
extern void *s_scroll_802D1E48(int, struct shape *, void *); /* callback */
extern void *s_scroll_802D1FA8(int, struct shape *, void *); /* callback */
extern void *s_scroll_802D2108(int, struct shape *, void *); /* callback */

extern void *s_obj_shape_802D2360(int, struct shape *, void *); /* callback */
extern void *s_obj_shape_802D2470(int, struct shape *, void *); /* callback */
extern void *s_obj_shape_802D2520(int, struct shape *, void *); /* callback */
extern void *s_obj_shape_802D28CC(int, struct shape *, void *); /* callback */

extern void *s_ripple_802D5B98(int, struct shape *, void *); /* callback */
extern void *s_ripple_802D5D0C(int, struct shape *, void *); /* callback */

extern void *s_object_c_8030D93C(int, struct shape *, void *); /* callback */
extern void *s_object_c_8030D9AC(int, struct shape *, void *); /* callback */

extern void *s_logo_shape(int, struct shape *, void *);
extern void *s_logo_text(int, struct shape *, void *);
extern void *s_title_bg(int, struct shape *, void *);
extern void *s_gameover_bg(int, struct shape *, void *);

extern void *s_file_select_main(int, struct shape *, void *);

extern void *s_star_select_main(int, struct shape *, void *);
"""

str_p_script_globl = """
#define P_CMP_AND               0
#define P_CMP_NAND              1
#define P_CMP_EQ                2
#define P_CMP_NE                3
#define P_CMP_GT                4
#define P_CMP_GE                5
#define P_CMP_LT                6
#define P_CMP_LE                7

#define P_VAR_SAVE              0
#define P_VAR_COURSE            1
#define P_VAR_LEVEL             2
#define P_VAR_STAGE             3
#define P_VAR_WORLD             4
"""

str_p_script_c = """
typedef uintptr_t P_SCRIPT;
"""

str_p_script_asm = """
#define p_push_call(seg, name, script)          \\
    _C(0x00, 0x10, SEGMENT_DATA_##seg >> 24);   \\
    _P(data_##name##_start);                    \\
    _P(data_##name##_end);                      \\
    _P(script)
#define p_push_jump(seg, name, script)          \\
    _C(0x01, 0x10, SEGMENT_DATA_##seg >> 24);   \\
    _P(data_##name##_start);                    \\
    _P(data_##name##_end);                      \\
    _P(script)
#define p_pull_return()                         \\
    _C(0x02, 0x04, 0)
#define p_sleep(x)                              \\
    _C(0x03, 0x04, x)
#define p_freeze(x)                             \\
    _C(0x04, 0x04, x)
#define p_jump(script)                          \\
    _C(0x05, 0x08, 0);                          \\
    _P(script)
#define p_call(script)                          \\
    _C(0x06, 0x08, 0);                          \\
    _P(script)
#define p_return()                              \\
    _C(0x07, 0x04, 0)
#define p_for(count)                            \\
    _C(0x08, 0x04, count)
#define p_done()                                \\
    _C(0x09, 0x04, 0)
#define p_do()                                  \\
    _C(0x0A, 0x04, 0)
#define p_while(cmp, val)                       \\
    _B(0x0B, 0x08, P_CMP_##cmp, 0);             \\
    _W(val);
#define p_if_jump(cmp, val, script)             \\
    _B(0x0C, 0x0C, P_CMP_##cmp, 0);             \\
    _W(val);                                    \\
    _P(script)
#define p_if_call(cmp, val, script)             \\
    _B(0x0D, 0x0C, P_CMP_##cmp, 0);             \\
    _W(val);                                    \\
    _P(script)
#define p_if(cmp, val)                          \\
    _B(0x0E, 0x0C, P_CMP_##cmp, 0);             \\
    _W(val)
#define p_else()                                \\
    _C(0x0F, 0x04, 0)
#define p_endif()                               \\
    _C(0x10, 0x04, 0)
#define p_callback(callback, arg)               \\
    _C(0x11, 0x08, arg);                        \\
    _P(callback)
#define p_process(callback, arg)                \\
    _C(0x12, 0x08, arg);                        \\
    _P(callback)
#define p_set(val)                              \\
    _C(0x13, 0x04, val)
#define p_push()                                \\
    _C(0x14, 0x04, 0)
#define p_pull()                                \\
    _C(0x15, 0x04, 0)
#define p_load_code(name)                       \\
    _C(0x16, 0x10, 0);                          \\
    _P(code_##name##_start);                    \\
    _P(name##_start);                           \\
    _P(name##_end)
#define p_load_data(seg, name)                  \\
    _C(0x17, 0x0C, SEGMENT_DATA_##seg >> 24);   \\
    _P(data_##name##_start);                    \\
    _P(data_##name##_end)
#define p_load_szp(seg, name)                   \\
    _C(0x18, 0x0C, SEGMENT_SZP_##seg >> 24);    \\
    _P(szp_##name##_start);                     \\
    _P(szp_##name##_end)
#define p_load_face(arg)                        \\
    _C(0x19, 0x04, arg)
#define p_load_texture(seg, name)               \\
    _C(0x1A, 0x0C, SEGMENT_SZP_##seg >> 24);    \\
    _P(szp_##name##_start);                     \\
    _P(szp_##name##_end)
#define p_stage_init()                          \\
    _C(0x1B, 0x04, 0)
#define p_stage_free()                          \\
    _C(0x1C, 0x04, 0)
#define p_stage_start()                         \\
    _C(0x1D, 0x04, 0)
#define p_stage_end()                           \\
    _C(0x1E, 0x04, 0)
#define p_world_start(world, script)            \\
    _B(0x1F, 0x08, world, 0);                   \\
    _P(script)
#define p_world_end()                           \\
    _C(0x20, 0x04, 0)
#define p_shape_gfx(shape, gfx, layer)          \\
    _C(0x21, 0x08, S_LAYER_##layer << 12 | (shape));    \\
    _P(gfx)
#define p_shape_script(shape, script)           \\
    _C(0x22, 0x08, shape);                      \\
    _P(script)
#define p_shape_scale(shape, gfx, layer, scale) \\
    _C(0x23, 0x08, S_LAYER_##layer << 12 | (shape));    \\
    _P(gfx);                                    \\
    _F(scale)
#define p_object(m, shape, px, py, pz, rx, ry, rz, arg0, arg1, flag, script)   \
\\
    _B(0x24, 0x18, m, shape);                   \\
    _H(px, py);                                 \\
    _H(pz, rx);                                 \\
    _H(ry, rz);                                 \\
    _C(arg0, arg1, flag);                       \\
    _P(script)
#define p_object_all(shape, px, py, pz, rx, ry, rz, arg0, arg1, flag, script)  \
\\
    p_object(0x1F, shape, px, py, pz, rx, ry, rz, arg0, arg1, flag, script)
#define p_player(shape, arg0, arg1, flag, script)   \\
    _B(0x25, 0x0C, 0, shape);                   \\
    _C(arg0, arg1, flag);                       \\
    _P(script)
#define p_mario()                               \\
    p_player(S_MARIO, 0, 0, 1, o_mario)
#define p_link(index, stage, world, link)       \\
    _B(0x26, 0x08, index, stage);               \\
    _B(world, link, 0x00, 0)
#define p_link_mid(index, stage, world, link)   \\
    _B(0x26, 0x08, index, stage);               \\
    _B(world, link, 0x80, 0)
#define p_linkbg(index, stage, world, link)     \\
    _B(0x27, 0x08, index, stage);               \\
    _B(world, link, 0x00, 0)
#define p_linkbg_mid(index, stage, world, link) \\
    _B(0x27, 0x08, index, stage);               \\
    _B(world, link, 0x80, 0)
#define p_connect(index, world, px, py, pz)     \\
    _B(0x28, 0x0C, index, world);               \\
    _H(px, py);                                 \\
    _H(pz, 0)
#define p_world_open(world)                     \\
    _B(0x29, 0x04, world, 0)
#define p_world_close(world)                    \\
    _B(0x2A, 0x04, world, 0)
#define p_player_open(world, ry, px, py, pz)    \\
    _B(0x2B, 0x0C, world, 0);                   \\
    _H(ry, px);                                 \\
    _H(py, pz)
/* 0x2C player_close */
#define p_world_update()                        \\
    _C(0x2D, 0x08, 0)
#define p_map(map)                              \\
    _C(0x2E, 0x08, 0);                          \\
    _P(map)
#define p_area(area)                            \\
    _C(0x2F, 0x08, 0);                          \\
    _P(area)
#define p_msg(type, msg)                        \\
    _B(0x30, 0x04, type, msg)
#define p_env(env)                              \\
    _C(0x31, 0x04, env)
/* 0x32 */
#define p_wipe(type, time, r, g, b)             \\
    _B(0x33, 0x08, type, time);                 \\
    _B(r, g, b, 0)
#define p_vi_black(arg)                         \\
    _B(0x34, 0x04, arg, 0)
#define p_vi_gamma(arg)                         \\
    _B(0x35, 0x04, arg, 0)
#define p_bgm(type, bgm)                        \\
    _C(0x36, 0x08, type);                       \\
    _H(bgm, 0)
#define p_bgm_play(bgm)                         \\
    _C(0x37, 0x04, bgm)
#define p_bgm_stop(time)                        \\
    _C(0x38, 0x04, (time)-2)
#define p_obj(obj)                              \\
    _C(0x39, 0x08, 0);                          \\
    _P(obj)
/* 0x3A wind */
#define p_jet(index, mode, px, py, pz, arg)     \\
    _B(0x3B, 0x0C, index, mode);                \\
    _H(px, py);                                 \\
    _H(pz, arg)
#define p_store(var)                            \\
    _B(0x3C, 0x04, 0, P_VAR_##var)
#define p_load(var)                             \\
    _B(0x3C, 0x04, 1, P_VAR_##var)
"""

str_map_data_globl = """
#define M_VTX                   0x40
#define M_FACEEND               0x41
#define M_END                   0x42
#define M_OBJ                   0x43
#define M_WATER                 0x44
"""

str_map_data_c = """
typedef s16 MAP_DATA;
"""

str_o_script_globl = """
#define O_MEM_0x00              0x00
#define O_MEM_FLAG              0x01
#define O_MEM_0x02              0x02
#define O_MEM_0x03              0x03
#define O_MEM_0x04              0x04
#define O_MEM_0x05              0x05
#define O_MEM_0x06              0x06
#define O_MEM_0x07              0x07
#define O_MEM_0x08              0x08
#define O_MEM_0x09              0x09
#define O_MEM_0x0A              0x0A
#define O_MEM_0x0B              0x0B
#define O_MEM_0x0C              0x0C
#define O_MEM_0x0D              0x0D
#define O_MEM_0x0E              0x0E
#define O_MEM_0x0F              0x0F
#define O_MEM_0x10              0x10
#define O_MEM_0x11              0x11
#define O_MEM_0x12              0x12
#define O_MEM_0x13              0x13
#define O_MEM_0x14              0x14
#define O_MEM_0x15              0x15
#define O_MEM_0x16              0x16
#define O_MEM_0x17              0x17
#define O_MEM_0x18              0x18
#define O_MEM_0x19              0x19
#define O_MEM_0x1A              0x1A
#define O_MEM_0x1B              0x1B
#define O_MEM_0x1C              0x1C
#define O_MEM_0x1D              0x1D
#define O_MEM_0x1E              0x1E
#define O_MEM_0x1F              0x1F
#define O_MEM_0x20              0x20
#define O_MEM_0x21              0x21
#define O_MEM_0x22              0x22
#define O_MEM_0x23              0x23
#define O_MEM_0x24              0x24
#define O_MEM_0x25              0x25
#define O_MEM_ANIME             0x26
#define O_MEM_0x27              0x27
#define O_MEM_0x28              0x28
#define O_MEM_0x29              0x29
#define O_MEM_COLTYPE           0x2A
#define O_MEM_COLFLAG           0x2B
#define O_MEM_0x2C              0x2C
#define O_MEM_0x2D              0x2D
#define O_MEM_0x2E              0x2E
#define O_MEM_0x2F              0x2F
#define O_MEM_0x30              0x30
#define O_MEM_0x31              0x31
#define O_MEM_0x32              0x32
#define O_MEM_0x33              0x33
#define O_MEM_0x34              0x34
#define O_MEM_0x35              0x35
#define O_MEM_0x36              0x36
#define O_MEM_0x37              0x37
#define O_MEM_0x38              0x38
#define O_MEM_0x39              0x39
#define O_MEM_0x3A              0x3A
#define O_MEM_0x3B              0x3B
#define O_MEM_0x3C              0x3C
#define O_MEM_0x3D              0x3D
#define O_MEM_0x3E              0x3E
#define O_MEM_0x3F              0x3F
#define O_MEM_0x40              0x40
#define O_MEM_0x41              0x41
#define O_MEM_COLARG            0x42
#define O_MEM_0x43              0x43
#define O_MEM_0x44              0x44
#define O_MEM_0x45              0x45
#define O_MEM_0x46              0x46
#define O_MEM_0x47              0x47
#define O_MEM_0x48              0x48
#define O_MEM_0x49              0x49
#define O_MEM_0x4A              0x4A
#define O_MEM_0x4B              0x4B
#define O_MEM_0x4C              0x4C
#define O_MEM_0x4D              0x4D
#define O_MEM_0x4E              0x4E
#define O_MEM_0x4F              0x4F

#define O_TYPE_PLAYER           0
#define O_TYPE_1                1
#define O_TYPE_PLAYERATTACK     2
#define O_TYPE_3                3
#define O_TYPE_OBJECTA          4
#define O_TYPE_OBJECTB          5
#define O_TYPE_ITEM             6
#define O_TYPE_7                7
#define O_TYPE_DEFAULT          8
#define O_TYPE_MOVEBG           9
#define O_TYPE_PLAYERUSE        10
#define O_TYPE_SYSTEM           11
#define O_TYPE_EFFECT           12
"""

str_o_script_c = """
typedef uintptr_t O_SCRIPT;
typedef void O_CALLBACK(void);
"""

str_o_script_asm = """
#define o_init(type)                            \\
    _C(0x00, O_TYPE_##type, 0)
#define o_sleep(time)                           \\
    _C(0x01, 0, time)
#define o_call(script)                          \\
    _C(0x02, 0, 0);                             \\
    _P(script)
#define o_return()                              \\
    _C(0x03, 0, 0)
#define o_jump(script)                          \\
    _C(0x04, 0, 0);                             \\
    _P(script)
#define o_for(count)                            \\
    _C(0x05, 0, count)
#define o_fend()                                \\
    _C(0x06, 0, 0)
#define o_fcontinue()                           \\
    _C(0x07, 0, 0)
#define o_while()                               \\
    _C(0x08, 0, 0)
#define o_wend()                                \\
    _C(0x09, 0, 0)
#define o_exit()                                \\
    _C(0x0A, 0, 0)
#define o_exit2()                               \\
    _C(0x0B, 0, 0)
#define o_callback(callback)                    \\
    _C(0x0C, 0, 0);                             \\
    _P(callback)
#define o_addf(mem, val)                        \\
    _C(0x0D, O_MEM_##mem, val)
#define o_setf(mem, val)                        \\
    _C(0x0E, O_MEM_##mem, val)
#define o_addi(mem, val)                        \\
    _C(0x0F, O_MEM_##mem, val)
#define o_seti(mem, val)                        \\
    _C(0x10, O_MEM_##mem, val)
#define o_setflag(mem, val)                     \\
    _C(0x11, O_MEM_##mem, val)
#define o_clrflag(mem, val)                     \\
    _C(0x12, O_MEM_##mem, val)
#define o_setrandr(mem, val, shift)             \\
    _C(0x13, O_MEM_##mem, val);                 \\
    _H(shift, 0)
#define o_setrandf(mem, val, mul)               \\
    _C(0x14, O_MEM_##mem, val);                 \\
    _H(mul, 0)
#define o_setrandi(mem, val, mul)               \\
    _C(0x15, O_MEM_##mem, val);                 \\
    _H(mul, 0)
#define o_addrandf(mem, val, mul)               \\
    _C(0x16, O_MEM_##mem, val);                 \\
    _H(mul, 0)
#define o_addrandr(mem, val, shift)             \\
    _C(0x17, O_MEM_##mem, val);                 \\
    _H(shift, 0)
/* 0x18 */
/* 0x19 */
/* 0x1A */
#define o_shape(shape)                          \\
    _C(0x1B, 0, shape)
#define o_object(shape, script)                 \\
    _C(0x1C, 0, 0);                             \\
    _W(shape);                                  \\
    _P(script)
#define o_destroy()                             \\
    _C(0x1D, 0, 0)
#define o_ground()                              \\
    _C(0x1E, 0, 0)
#define o_memaddf(mem, a, b)                    \\
    _B(0x1F, O_MEM_##mem, O_MEM_##a, O_MEM_##b)
#define o_memaddi(mem, a, b)                    \\
    _B(0x20, O_MEM_##mem, O_MEM_##a, O_MEM_##b)
#define o_billboard()                           \\
    _C(0x21, 0, 0)
#define o_shapehide()                           \\
    _C(0x22, 0, 0)
#define o_colhit(radius, height)                \\
    _C(0x23, 0, 0);                             \\
    _H(radius, height)
/* 0x24 */
#define o_memsleep(mem)                         \\
    _C(0x25, O_MEM_##mem, 0)
#define o_for2(count)                           \\
    _C(0x26, count, 0)
#define o_ptr(mem, ptr)                         \\
    _C(0x27, O_MEM_##mem, 0);                   \\
    _P(ptr)
#define o_anime(anime)                          \\
    _C(0x28, anime, 0)
#define o_objectarg(shape, script, arg)         \\
    _C(0x29, 0, arg);                           \\
    _W(shape);                                  \\
    _P(script)
#define o_map(map)                              \\
    _C(0x2A, 0, 0);                             \\
    _P(map)
#define o_coloff(radius, height, offset)        \\
    _C(0x2B, 0, 0);                             \\
    _H(radius, height);                         \\
    _H(offset, 0)
#define o_child(shape, script)                  \\
    _C(0x2C, 0, 0);                             \\
    _W(shape);                                  \\
    _P(script)
#define o_origin()                              \\
    _C(0x2D, 0, 0)
#define o_coldmg(radius, height)                \\
    _C(0x2E, 0, 0);                             \\
    _H(radius, height)
#define o_coltype(type)                         \\
    _C(0x2F, 0, 0);                             \\
    _W(type)
#define o_physics(a, b, c, d, e, f, g, h)       \\
    _C(0x30, 0, 0);                             \\
    _H(a, b);                                   \\
    _H(c, d);                                   \\
    _H(e, f);                                   \\
    _H(g, h)
#define o_colarg(arg)                           \\
    _C(0x31, 0, 0);                             \\
    _W(arg)
#define o_scale(scale)                          \\
    _C(0x32, 0, scale)
#define o_memclrflag(mem, flag)                 \\
    _C(0x33, O_MEM_##mem, 0);                   \\
    _W(flag)
#define o_inc(mem, time)                        \\
    _C(0x34, O_MEM_##mem, time)
#define o_shapedisable()                        \\
    _C(0x35, 0, 0)
#define o_sets(mem, val)                        \\
    _C(0x36, 0, 0);                             \\
    _W(val)
#define o_splash(splash)                        \\
    _C(0x37, 0, 0);                             \\
    _P(splash)
"""

str_anime = """
#include <sm64/mem.h>

#define ANIME(anime, flag, waist, start, end, frame, joint)     \\
    .short flag, waist, start, end, frame, joint;               \\
    .word anime##_val - anime;                                  \\
    .word anime##_tbl - anime;                                  \\
    .word anime##_end - anime

.data

"""

str_demo = """
#include <sm64/mem.h>

#define DEMO(stage)             .byte stage, 0, 0, 0

.data

"""

str_audio_file_asm = """
#define TABLE(code)             .short code, (table_end-table_start)/8
#define FILE(file)              .word file, file##_end-file
"""

str_audio_ctl = """
.data
.incbin "data/audio/ctl.bin"
"""

str_audio_tbl = """
.data
.incbin "data/audio/tbl.bin"
"""

str_audio_seq = """
#include <sm64/types.h>
#include <sm64/audio/file.h>

.data

TABLE(3)
table_start:
#define SEQ(file, vol, ...)     FILE(file)
#include <meta/seq.h>
#undef SEQ
table_end:

#define SEQ(file, vol, ...)                 \\
    .balign 0x10; file:                     \\
    .incbin ASSET(data/audio/seq/file.seq); \\
    .balign 0x10; file##_end:
#include <meta/seq.h>
#undef SEQ
"""

str_audio_bnk = """
.data

table:
#define SEQ(file, vol, ...)     .short file-table
#include <meta/seq.h>
#undef SEQ

#define SEQ(file, vol, ...)     \\
    file:                       \\
    .byte file##_end-file - 1;  \\
    .byte __VA_ARGS__;          \\
    file##_end:
#include <meta/seq.h>
#undef SEQ
"""

struct_main = [
    [0x4C, "sc_task", [
        (0x00, table.sym_var("task",    "OSTask")),
        (0x40, table.sym_var("mq",      "OSMesgQueue *")),
        (0x44, table.sym_var("msg",     "OSMesg")),
        (0x48, table.sym_var("state",   "s32")),
    ]],
    [0x08, "sc_client", [
        (0x00, table.sym_var("mq",  "OSMesgQueue *")),
        (0x04, table.sym_var("msg", "OSMesg")),
    ]],
]

struct_app = [
    [0xC84C, "video", [
        (0x0000, table.sym_var("gfx",       "Gfx", "[6400]")),
        (0xC800, table.sym_var("task",      "struct sc_task")),
    ]],
    [0x1C, "controller", [
        (0x00, table.sym_var("stick_x",     "s16")),
        (0x02, table.sym_var("stick_y",     "s16")),
        (0x04, table.sym_var("stick",       "f32", "[2]")),
        (0x0C, table.sym_var("stick_mag",   "f32")),
        (0x10, table.sym_var("held",        "u16")),
        (0x12, table.sym_var("down",        "u16")),
        (0x14, table.sym_var("status",      "OSContStatus *")),
        (0x18, table.sym_var("pad",         "OSContPad *")),
    ]],
    [0x04, "demo", [
        (0x00, table.sym_var("count",   "u8")),
        (0x01, table.sym_var("stick_x", "s8")),
        (0x02, table.sym_var("stick_y", "s8")),
        (0x03, table.sym_var("button",  "u8")),
    ]],
]

struct_audio = [
]

struct_game = [
    [0x10, "staff", [
        (0x00, table.sym_var("stage",   "u8")),
        (0x01, table.sym_var("world",   "u8")),
        (0x02, table.sym_var("flag",    "u8")),
        (0x03, table.sym_var("ry",      "u8")),
        (0x04, table.sym_var("pos",     "vecs")),
        (0x0C, table.sym_var("str",     "const char **")),
    ]],
    [0x08, "struct_8033B248", [
        (0x00, table.sym_var("_00", "u8")),
        (0x01, table.sym_var("_01", "u8")),
        (0x02, table.sym_var("_02", "u8")),
        (0x03, table.sym_var("_03", "u8")),
        (0x04, table.sym_var("_04", "u32")),
    ]],
]

struct_pl_collision = [
    [0x08, "pl_collision", [
        (0x00, table.sym_var("type", "u32")),
        (0x04, table.sym_var_fnc("callback", val="int", arg=(
            "struct player *pl",
            "u32 flag",
            "struct object *obj",
        ))),
    ]],
]

struct_player = [
    [0xC8, "player", [
        (0x00, table.sym_var("index",       "u16")),
        (0x02, table.sym_var("event",       "u16")),
        (0x04, table.sym_var("flag",        "u32")),
        (0x08, table.sym_var("particle",    "u32")),
        (0x0C, table.sym_var("state",       "u32")),
        (0x10, table.sym_var("state_prev",  "u32")),
        (0x14, table.sym_var("ground_sfx",  "u32")),
        (0x18, table.sym_var("mode",        "s16")),
        (0x1A, table.sym_var("timer",       "u16")),
        (0x1C, table.sym_var("arg",         "u32")),
        (0x20, table.sym_var("stick_mag",   "f32")),
        (0x24, table.sym_var("stick_rot",   "s16")),
        (0x26, table.sym_var("invincible",  "s16")),
        (0x28, table.sym_var("timer_a",     "u8")),
        (0x29, table.sym_var("timer_b",     "u8")),
        (0x2A, table.sym_var("timer_wall",  "u8")),
        (0x2B, table.sym_var("timer_floor", "u8")),
        (0x2C, table.sym_var("rot",         "vecs")),
        (0x32, table.sym_var("rot_vel",     "vecs")),
        (0x38, table.sym_var("ry_slide",    "s16")),
        (0x3A, table.sym_var("ry_twirl",    "s16")),
        (0x3C, table.sym_var("pos",         "vecf")),
        (0x48, table.sym_var("vel",         "vecf")),
        (0x54, table.sym_var("vel_f",       "f32")),
        (0x58, table.sym_var("vel_h",       "f32", "[2]")),
        (0x60, table.sym_var("wall",        "struct map_face *")),
        (0x64, table.sym_var("roof",        "struct map_face *")),
        (0x68, table.sym_var("ground",      "struct map_face *")),
        (0x6C, table.sym_var("y_roof",      "f32")),
        (0x70, table.sym_var("y_ground",    "f32")),
        (0x74, table.sym_var("ry_ground",   "s16")),
        (0x76, table.sym_var("y_water",     "s16")),
        (0x78, table.sym_var("obj_col",     "struct object *")),
        (0x7C, table.sym_var("obj_hold",    "struct object *")),
        (0x80, table.sym_var("obj_use",     "struct object *")),
        (0x84, table.sym_var("obj_ride",    "struct object *")),
        (0x88, table.sym_var("obj",         "struct object *")),
        (0x8C, table.sym_var("_8C",         "void *")),
        (0x90, table.sym_var("world",       "struct world *")),
        (0x94, table.sym_var("camera",      "struct pl_camera *")),
        (0x98, table.sym_var("shape",       "struct pl_shape *")),
        (0x9C, table.sym_var("cont",        "struct controller *")),
        (0xA0, table.sym_var("anime",       "struct anime *")),
        (0xA4, table.sym_var("collision",   "u32")),
        (0xA8, table.sym_var("coin",        "s16")),
        (0xAA, table.sym_var("star",        "s16")),
        (0xAC, table.sym_var("key",         "s8")),
        (0xAD, table.sym_var("life",        "s8")),
        (0xAE, table.sym_var("power",       "s16")),
        (0xB0, table.sym_var("waist",       "s16")),
        (0xB2, table.sym_var("hurt",        "u8")),
        (0xB3, table.sym_var("heal",        "u8")),
        (0xB4, table.sym_var("squish",      "u8")),
        (0xB5, table.sym_var("alpha",       "u8")),
        (0xB6, table.sym_var("timer_cap",   "u16")),
        (0xB8, table.sym_var("star_prev",   "s16")),
        (0xBC, table.sym_var("y_peak",      "f32")),
        (0xC0, table.sym_var("y_sink",      "f32")),
        (0xC4, table.sym_var("gravity",     "f32")),
    ]],
]

struct_pl_physics = [
]

struct_pl_demo = [
]

struct_pl_hang = [
]

struct_pl_stop = [
]

struct_pl_ground = [
    [0x18, "pl_ground", [
        (0x00, table.sym_var("time",        "s16")),
        (0x02, table.sym_var("timer_floor", "s16")),
        (0x04, table.sym_var("state_slip",  "u32")),
        (0x08, table.sym_var("state_next",  "u32")),
        (0x0C, table.sym_var("state_jump",  "u32")),
        (0x10, table.sym_var("state_fall",  "u32")),
        (0x14, table.sym_var("state_slide", "u32")),
    ]],
]

struct_pl_air = [
]

struct_pl_water = [
]

struct_pl_grab = [
]

struct_pl_callback = [
    [0x28, "pl_shape", [
        (0x00, table.sym_var("state",   "u32")),
        (0x04, table.sym_var("head",    "s8")),
        (0x05, table.sym_var("eye",     "s8")),
        (0x06, table.sym_var("glove",   "s8")),
        (0x07, table.sym_var("wing",    "s8")),
        (0x08, table.sym_var("cap",     "s16")),
        (0x0A, table.sym_var("hold",    "s8")),
        (0x0B, table.sym_var("punch",   "u8")),
        (0x0C, table.sym_var("torso",   "vecs")),
        (0x12, table.sym_var("neck",    "vecs")),
        (0x18, table.sym_var("hand",    "vecf")),
        (0x24, table.sym_var("obj",     "struct object *")),
    ]],
]

struct_mem = [
    [0x10, "mem_link", [
        (0x00, table.sym_var("prev",    "struct mem_link *")),
        (0x04, table.sym_var("next",    "struct mem_link *")),
        (0x08, table.sym_var("pad",     "u64")),
    ]],
    [0x10, "mem", [
        (0x00, table.sym_var("size",    "size_t")),
        (0x04, table.sym_var("l",       "struct mem_link *")),
        (0x08, table.sym_var("r",       "struct mem_link *")),
        (0x0C, table.sym_var("mem",     "struct mem *")),
    ]],
    [0x10, "arena", [
        (0x00, table.sym_var("size",    "size_t")),
        (0x04, table.sym_var("used",    "size_t")),
        (0x08, table.sym_var("start",   "u8 *")),
        (0x0C, table.sym_var("free",    "u8 *")),
    ]],
    [0x08, "heap_link", [
        (0x00, table.sym_var("next",    "struct heap_link *")),
        (0x04, table.sym_var("size",    "size_t")),
    ]],
    [0x10, "heap", [
        (0x00, table.sym_var("size",    "size_t")),
        (0x04, table.sym_var("start",   "struct heap_link *")),
        (0x08, table.sym_var("free",    "struct heap_link *")),
        (0x0C, table.sym_var("pad",     "u32")),
    ]],
    [0x08, "file_table", [
        (0x00, table.sym_var("len", "uint")),
        (0x04, table.sym_var("src", "void *")),
        [0x08, "struct", "table", [
            (0x00, table.sym_var("start",   "uint")),
            (0x04, table.sym_var("size",    "uint")),
        ], "[1]"],
    ]],
    [0x0C, "file", [
        (0x00, table.sym_var("table",   "struct file_table *")),
        (0x04, table.sym_var("src",     "void *")),
        (0x08, table.sym_var("buf",     "void *")),
    ]],
]

struct_world = [
    [0x20, "spawn", [
        (0x00, table.sym_var("pos",     "vecs")),
        (0x06, table.sym_var("rot",     "vecs")),
        (0x0C, table.sym_var("world",   "s8")),
        (0x0D, table.sym_var("_0D",     "s8")),
        (0x0E, table.sym_var("_0E",     "u16")),
        (0x10, table.sym_var("_10",     "u32")),
        (0x14, table.sym_var("script",  "const O_SCRIPT *")),
        (0x18, table.sym_var("obj",     "struct object *")),
        (0x1C, table.sym_var("next",    "struct spawn *")),
    ]],
    [0x3C, "world", [
        (0x00, table.sym_var("index",       "s8")),
        (0x01, table.sym_var("_01",         "s8")),
        (0x02, table.sym_var("env",         "u16")),
        (0x04, table.sym_var("s",           "struct shape_world *")),
        (0x08, table.sym_var("map",         "const MAP_DATA *")),
        (0x0C, table.sym_var("area",        "const AREA_DATA *")),
        (0x10, table.sym_var("obj",         "const OBJ_DATA *")),
        (0x14, table.sym_var("link",        "void *")),
        (0x18, table.sym_var("linkbg",      "void *")),
        (0x1C, table.sym_var("connect",     "void *")),
        (0x20, table.sym_var("spawn",       "void *")),
        (0x24, table.sym_var("cam",         "void *")),
        (0x28, table.sym_var("wind",        "void *")),
        (0x2C, table.sym_var("jet",         "void *", "[2]")),
        (0x34, table.sym_var("msg",         "u8", "[2]")),
        (0x36, table.sym_var("bgm_arg",     "u16")),
        (0x38, table.sym_var("bgm_index",   "u16")),
        (0x3A, table.sym_var("pad",         "u16")),
    ]],
]

struct_save = [
]

struct_shape_draw = [
]

struct_time = [
    [0xC8, "time", [
        (0x00, table.sym_var("_00", "s16")),
        (0x02, table.sym_var("_02", "s16")),
        (0x08, table.sym_var("_08", "OSTime", "[5]")),
        (0x30, table.sym_var("_30", "OSTime", "[3]")),
        (0x48, table.sym_var("_48", "OSTime", "[8]")),
        (0x88, table.sym_var("_88", "OSTime", "[8]")),
    ]],
]

struct_slidec = [
]

struct_camera = [
    [0x01, "camera", [
        (0x00, table.sym_var("mode",    "u8")),
        # todo: finish
    ]],
    [0x18, "campos", [
        (0x00, table.sym_var("code",    "s16")),
        (0x04, table.sym_var("pos",     "vecf")),
        (0x10, table.sym_var("_10",     "f32")),
        (0x14, table.sym_var("dist",    "f32")),
    ]],
    [0x16, "camctl", [
        (0x00, table.sym_var("world",   "s8")),
        (0x04, table.sym_var_fnc("callback", arg=(
            "struct camera *",
        ))),
        (0x08, table.sym_var("pos",     "vecs")),
        (0x0E, table.sym_var("size",    "vecs")),
        (0x14, table.sym_var("ry",      "s16")),
    ]],
    [0x08, "campath", [
        (0x00, table.sym_var("code",    "s8")),
        (0x01, table.sym_var("time",    "u8")),
        (0x02, table.sym_var("pos",     "vecs")),
    ]],
    [0x06, "camdemo", [
        (0x00, table.sym_var_fnc("callback", arg=(
            "struct camera *",
        ))),
        (0x04, table.sym_var("time",    "s16")),
    ]],
]

struct_course = [
]

struct_object = [
    [0x68, "obj_list", [
        (0x000, table.sym_var("s",      "struct shape_object")),
        (0x060, table.sym_var("next",   "struct obj_list *")),
        (0x064, table.sym_var("prev",   "struct obj_list *")),
    ]],
    [0x260, "object", [
        (0x000, table.sym_var("list",   "struct obj_list")),
        (0x068, table.sym_var("parent", "struct object *")),
        (0x06C, table.sym_var("child",  "struct object *")),
        (0x070, table.sym_var("collision",  "u32")),
        (0x074, table.sym_var("flag",       "s16")),
        (0x076, table.sym_var("col_len",    "s16")),
        (0x078, table.sym_var("obj_col",    "struct object *", "[4]")),
        [0x088, "union", "mem", [
            (None, table.sym_var("s8",  "s8", "[4]")),
            (None, table.sym_var("u8",  "u8", "[4]")),
            (None, table.sym_var("s16", "s16", "[2]")),
            (None, table.sym_var("u16", "u16", "[2]")),
            (None, table.sym_var("s32", "s32")),
            (None, table.sym_var("u32", "u32")),
            (None, table.sym_var("f32", "f32")),
            (None, table.sym_var("ptr", "void *")),
        ], "[80]"],
        (0x1C8, table.sym_var("_1C8",           "void *")),
        (0x1CC, table.sym_var("pc",             "const O_SCRIPT *")),
        (0x1D0, table.sym_var("stack_index",    "uint")),
        (0x1D4, table.sym_var("stack",          "void *", "[8]")),
        (0x1F4, table.sym_var("_1F4",   "s16")),
        (0x1F6, table.sym_var("_1F6",   "s16")),
        (0x1F8, table.sym_var("col_hit_r",  "f32")),
        (0x1FC, table.sym_var("col_hit_h",  "f32")),
        (0x200, table.sym_var("col_dmg_r",  "f32")),
        (0x204, table.sym_var("col_dmg_h",  "f32")),
        (0x208, table.sym_var("col_offset", "f32")),
        (0x20C, table.sym_var("script", "const O_SCRIPT *")),
        (0x210, table.sym_var("_210",   "struct object *")),
        (0x214, table.sym_var("_214",   "struct object *")),
        (0x218, table.sym_var("_218",   "s16 *")),
        (0x21C, table.sym_var("mf",     "mtxf")),
        (0x25C, table.sym_var("_25C",   "void *")),
    ]],
    [0x10, "pl_pcl", [
        (0x00, table.sym_var("code",    "u32")),
        (0x04, table.sym_var("flag",    "u32")),
        (0x08, table.sym_var("shape",   "u8")),
        (0x0C, table.sym_var("script",  "const O_SCRIPT *")),
    ]],
    [0x06, "struct_8033D274", [
        (0x00, table.sym_var("ground",  "s16")),
        (0x02, table.sym_var("roof",    "s16")),
        (0x04, table.sym_var("wall",    "s16")),
    ]],
]

struct_obj_lib = [
    [0x24, "obj_splash", [
        (0x00, table.sym_var("flag",    "s16")),
        (0x02, table.sym_var("shape",   "s16")),
        (0x04, table.sym_var("script",  "const O_SCRIPT *")),
        (0x08, table.sym_var("ry_mul",  "s16")),
        (0x0A, table.sym_var("p_mul",   "s16")),
        (0x0C, table.sym_var("vf_add",  "f32")),
        (0x10, table.sym_var("vf_mul",  "f32")),
        (0x14, table.sym_var("vy_add",  "f32")),
        (0x18, table.sym_var("vy_mul",  "f32")),
        (0x1C, table.sym_var("s_add",   "f32")),
        (0x20, table.sym_var("s_mul",   "f32")),
    ]],
    [0x14, "obj_pcl", [
        (0x00, table.sym_var("arg",     "s8")),
        (0x01, table.sym_var("count",   "s8")),
        (0x02, table.sym_var("shape",   "u8")),
        (0x03, table.sym_var("offset",  "s8")),
        (0x04, table.sym_var("vf_add",  "s8")),
        (0x05, table.sym_var("vf_mul",  "s8")),
        (0x06, table.sym_var("vy_add",  "s8")),
        (0x07, table.sym_var("vy_mul",  "s8")),
        (0x08, table.sym_var("gravity", "s8")),
        (0x09, table.sym_var("drag",    "s8")),
        (0x0C, table.sym_var("s_add",   "f32")),
        (0x10, table.sym_var("s_mul",   "f32")),
    ]],
    [0x10, "obj_col", [
        (0x00, table.sym_var("type",    "u32")),
        (0x04, table.sym_var("offset",  "u8")),
        (0x05, table.sym_var("ap",      "s8")),
        (0x06, table.sym_var("hp",      "s8")),
        (0x07, table.sym_var("coin",    "s8")),
        (0x08, table.sym_var("hit_r",   "s16")),
        (0x0A, table.sym_var("hit_h",   "s16")),
        (0x0C, table.sym_var("dmg_r",   "s16")),
        (0x0E, table.sym_var("dmg_h",   "s16")),
    ]],
]

struct_object_a = [
    [0x0C, "object_a_0", [
        (0x00, table.sym_var("_00", "s16")),
        (0x04, table.sym_var("_04", "f32")),
        (0x08, table.sym_var("_08", "f32")),
    ]],
    [0x0A, "object_a_1", [
        (0x00, table.sym_var("flag",    "s16")),
        (0x02, table.sym_var("scale",   "s16")),
        (0x04, table.sym_var("map",     "const MAP_DATA *")),
        (0x08, table.sym_var("dist",    "s16")),
    ]],
    [0x0C, "object_a_2", [
        (0x00, table.sym_var("count",   "s16")),
        (0x02, table.sym_var("add",     "s16")),
        (0x04, table.sym_var("mul",     "s16")),
        (0x06, table.sym_var("shape",   "s16")),
        (0x08, table.sym_var("map",     "const MAP_DATA *")),
    ]],
    [0x0A, "object_a_3", [
        (0x00, table.sym_var("map", "const MAP_DATA *")),
        (0x04, table.sym_var("px",  "s16")),
        (0x06, table.sym_var("pz",  "s16")),
        (0x08, table.sym_var("ry",  "s16")),
    ]],
    [0x14, "object_a_4", [
        (0x00, table.sym_var("offset",  "s32")),
        (0x04, table.sym_var("scale",   "vecf")),
        (0x10, table.sym_var("vel",     "f32")),
    ]],
    [0x08, "object_a_5", [
        (0x00, table.sym_var("shape",   "u8")),
        (0x01, table.sym_var("px",      "s8")),
        (0x02, table.sym_var("pz",      "s8")),
        (0x03, table.sym_var("state",   "s8")),
        (0x04, table.sym_var("data",    "const s8 *")),
    ]],
    [0x08, "object_a_6", [
        (0x00, table.sym_var("index",   "u8")),
        (0x01, table.sym_var("flag",    "u8")),
        (0x02, table.sym_var("arg",     "u8")),
        (0x03, table.sym_var("shape",   "u8")),
        (0x04, table.sym_var("script",  "const O_SCRIPT *")),
    ]],
    [0x08, "object_a_7", [
        (0x00, table.sym_var("offset",  "s16")),
        (0x02, table.sym_var("shape",   "s16")),
        (0x04, table.sym_var("map",     "const MAP_DATA *")),
    ]],
    [0x10, "object_a_8", [
        (0x00, table.sym_var("time",        "s32")),
        (0x04, table.sym_var("anime",       "s32")),
        (0x08, table.sym_var("vel",         "f32")),
        (0x0C, table.sym_var("anime_vel",   "f32")),
    ]],
]

struct_obj_physics = [
]

struct_obj_collision = [
]

struct_obj_list = [
]

struct_obj_sfx = [
    [0x08, "obj_sfx", [
        (0x00, table.sym_var("flag",    "s16")),
        (0x02, table.sym_var("l",       "s8")),
        (0x03, table.sym_var("r",       "s8")),
        (0x04, table.sym_var("sfx",     "u32")),
    ]],
]

struct_obj_debug = [
    [0x0C, "obj_debug", [
        (0x00, table.sym_var("flag",    "s16")),
        (0x02, table.sym_var("x",       "s16")),
        (0x04, table.sym_var("y",       "s16")),
        (0x06, table.sym_var("min",     "s16")),
        (0x08, table.sym_var("max",     "s16")),
        (0x0A, table.sym_var("height",  "s16")),
    ]],
]

struct_wipe = [
    [0x16, "wipe", [
        (0x00, table.sym_var("flag",    "u8")),
        (0x01, table.sym_var("type",    "u8")),
        (0x02, table.sym_var("_02",     "u8")),
        (0x03, table.sym_var("_03",     "u8")),
        (0x04, table.sym_var("r",       "u8")),
        (0x05, table.sym_var("g",       "u8")),
        (0x06, table.sym_var("b",       "u8")),
        (0x08, table.sym_var("_08",     "s16")),
        (0x0A, table.sym_var("_0A",     "s16")),
        (0x0C, table.sym_var("_0C",     "s16")),
        (0x0E, table.sym_var("_0E",     "s16")),
        (0x10, table.sym_var("_10",     "s16")),
        (0x12, table.sym_var("_12",     "s16")),
        (0x14, table.sym_var("_14",     "s16")),
    ]],
]

struct_shadow = [
    [0x09, "shadow_rect", [
        (0x00, table.sym_var("sx",      "f32")),
        (0x04, table.sym_var("sz",      "f32")),
        (0x08, table.sym_var("y_scale", "s8")),
    ]],
]

struct_background = [
    [0x10, "struct_803612C0", [
        (0x00, table.sym_var("_00", "u16")),
        (0x02, table.sym_var("_02", "s16")),
        (0x04, table.sym_var("_04", "s32")),
        (0x08, table.sym_var("_08", "s32")),
        (0x0C, table.sym_var("_0C", "s32")),
    ]],
]

struct_scroll = [
    [0x24, "scroll", [
        (0x00, table.sym_var("index",   "int")),
        (0x04, table.sym_var("texture", "int")),
        (0x08, table.sym_var("len",     "int")),
        (0x0C, table.sym_var("data",    "const s16 *")),
        (0x10, table.sym_var("start",   "const Gfx *")),
        (0x14, table.sym_var("end",     "const Gfx *")),
        (0x18, table.sym_var("draw",    "const Gfx *")),
        (0x1C, table.sym_var("r",       "u8")),
        (0x1D, table.sym_var("g",       "u8")),
        (0x1E, table.sym_var("b",       "u8")),
        (0x1F, table.sym_var("a",       "u8")),
        (0x20, table.sym_var("layer",   "int")),
    ]],
]

struct_obj_shape = [
]

struct_ripple = [
]

struct_print = [
]

struct_message = [
    [0x10, "msg", [
        (0x00, table.sym_var("arg",     "s32")),
        (0x04, table.sym_var("line",    "s8")),
        (0x06, table.sym_var("x",       "s16")),
        (0x08, table.sym_var("y",       "s16")),
        (0x0C, table.sym_var("str",     "const u8 *")),
    ]],
]

struct_weather_snow = [
]

struct_weather_lava = [
]

struct_obj_data = [
    [0x08, "prg_obj", [
        (0x00, table.sym_var("script",  "const O_SCRIPT *")),
        (0x04, table.sym_var("shape",   "s16")),
        (0x06, table.sym_var("arg",     "s16")),
    ]],
    [0x08, "map_obj", [
        (0x00, table.sym_var("index",   "u8")),
        (0x01, table.sym_var("type",    "u8")),
        (0x02, table.sym_var("arg",     "u8")),
        (0x03, table.sym_var("shape",   "u8")),
        (0x04, table.sym_var("script",  "const O_SCRIPT *")),
    ]],
]

struct_hud = [
    [0x0E, "hud", [
        (0x00, table.sym_var("life",    "s16")),
        (0x02, table.sym_var("coin",    "s16")),
        (0x04, table.sym_var("star",    "s16")),
        (0x06, table.sym_var("power",   "s16")),
        (0x08, table.sym_var("key",     "s16")),
        (0x0A, table.sym_var("flag",    "s16")),
        (0x0C, table.sym_var("timer",   "u16")),
    ]],
    [0x0C, "power", [
        (0x00, table.sym_var("mode",    "s8")),
        (0x02, table.sym_var("x",       "s16")),
        (0x04, table.sym_var("y",       "s16")),
        (0x08, table.sym_var("scale",   "f32")),
    ]],
]

struct_object_b = [
]

struct_object_c = [
    [0x0E, "object_c_0", [
        (0x00, table.sym_var("msg_start",   "s16")),
        (0x02, table.sym_var("msg_win",     "s16")),
        (0x04, table.sym_var("path",        "const PATH_DATA *")),
        (0x08, table.sym_var("star",        "vecs")),
    ]],
    [0x0B, "object_c_1", [
        (0x00, table.sym_var("scale",   "f32")),
        (0x04, table.sym_var("sfx",     "u32")),
        (0x08, table.sym_var("dist",    "s16")),
        (0x0A, table.sym_var("damage",  "s8")),
    ]],
    [0x0A, "object_c_2", [
        (0x00, table.sym_var("map",     "const MAP_DATA *")),
        (0x04, table.sym_var("p_map",   "const MAP_DATA *")),
        (0x08, table.sym_var("p_shape", "s16")),
    ]],
    [0x06, "object_c_3", [
        (0x00, table.sym_var("map",     "const MAP_DATA *")),
        (0x04, table.sym_var("shape",   "s16")),
    ]],
    [0x0C, "object_c_4", [
        (0x00, table.sym_var("msg",     "s16")),
        (0x04, table.sym_var("radius",  "f32")),
        (0x08, table.sym_var("height",  "f32")),
    ]],
    [0x0C, "object_c_5", [
        (0x00, table.sym_var("shape",   "int")),
        (0x04, table.sym_var("script",  "const O_SCRIPT *")),
        (0x08, table.sym_var("scale",   "f32")),
    ]],
]

struct_math = [
    [0x08, "bspline", [
        (0x00, table.sym_var("time",    "s16")),
        (0x02, table.sym_var("pos",     "vecs")),
    ]],
]

struct_shape = [
    [0x18, "anime", [
        (0x00, table.sym_var("flag",    "s16")),
        (0x02, table.sym_var("waist",   "s16")),
        (0x04, table.sym_var("start",   "s16")),
        (0x06, table.sym_var("end",     "s16")),
        (0x08, table.sym_var("frame",   "s16")),
        (0x0A, table.sym_var("joint",   "s16")),
        (0x0C, table.sym_var("val",     "const s16 *")),
        (0x10, table.sym_var("tbl",     "const u16 *")),
        (0x14, table.sym_var("size",    "size_t")),
    ]],
    [0x14, "skeleton", [
        (0x00, table.sym_var("index",       "s16")),
        (0x02, table.sym_var("waist",       "s16")),
        (0x04, table.sym_var("anime",       "struct anime *")),
        (0x08, table.sym_var("frame",       "s16")),
        (0x0A, table.sym_var("timer",       "u16")),
        (0x0C, table.sym_var("frame_amt",   "s32")),
        (0x10, table.sym_var("frame_vel",   "s32")),
    ]],
    [0x14, "shape", [
        (0x00, table.sym_var("type",    "s16")),
        (0x02, table.sym_var("flag",    "s16")),
        (0x04, table.sym_var("prev",    "struct shape *")),
        (0x08, table.sym_var("next",    "struct shape *")),
        (0x0C, table.sym_var("parent",  "struct shape *")),
        (0x10, table.sym_var("child",   "struct shape *")),
    ]],
    [0x1C, "shape_callback", [
        (0x00, table.sym_var("s",       "struct shape")),
        (0x14, table.sym_var_fnc("callback", val="void *", arg=(
            "int mode",
            "struct shape *shape",
            "void *data",
        ))),
        (0x18, table.sym_var("arg", "int")),
    ]],
    [0x3C, "shape_camera", [
        (0x00, table.sym_var("s",       "struct shape_callback")),
        (0x1C, table.sym_var("eye",     "vecf")),
        (0x28, table.sym_var("look",    "vecf")),
        (0x34, table.sym_var("mf",      "mtxf *")),
        (0x38, table.sym_var("rz_m",    "s16")),
        (0x3A, table.sym_var("rz_p",    "s16")),
    ]],
    [0x18, "shape_gfx", [
        (0x00, table.sym_var("s",   "struct shape")),
        (0x14, table.sym_var("gfx", "const Gfx *")),
    ]],
    [0x1E, "shape_billboard", [
        (0x00, table.sym_var("s",   "struct shape_gfx")),
        (0x18, table.sym_var("pos", "vecs")),
    ]],
    [0x1C, "shape_scale", [
        (0x00, table.sym_var("s",       "struct shape_gfx")),
        (0x18, table.sym_var("scale",   "f32")),
    ]],
    [0x60, "shape_object", [
        (0x00, table.sym_var("s",           "struct shape")),
        (0x14, table.sym_var("list",        "struct shape *")),
        (0x18, table.sym_var("world",       "s8")),
        (0x19, table.sym_var("shape",       "s8")),
        (0x1A, table.sym_var("rot",         "vecs")),
        (0x20, table.sym_var("pos",         "vecf")),
        (0x2C, table.sym_var("scale",       "vecf")),
        (0x38, table.sym_var("skeleton",    "struct skeleton")),
        (0x4C, table.sym_var("_4C",         "void *")),
        (0x50, table.sym_var("mf",          "mtxf *")),
        (0x54, table.sym_var("view",        "vecf")),
    ]],
]

struct_s_script = [
]

struct_p_script = [
]

struct_map = [
    [0x30, "map_face", [
        (0x00, table.sym_var("type",    "s16")),
        (0x02, table.sym_var("arg",     "s16")),
        (0x04, table.sym_var("flag",    "s8")),
        (0x05, table.sym_var("area",    "s8")),
        (0x06, table.sym_var("y_min",   "s16")),
        (0x08, table.sym_var("y_max",   "s16")),
        (0x0A, table.sym_var("v0",      "vecs")),
        (0x10, table.sym_var("v1",      "vecs")),
        (0x16, table.sym_var("v2",      "vecs")),
        (0x1C, table.sym_var("nx",      "f32")),
        (0x20, table.sym_var("ny",      "f32")),
        (0x24, table.sym_var("nz",      "f32")),
        (0x28, table.sym_var("nw",      "f32")),
        (0x2C, table.sym_var("obj",     "struct object *")),
    ]],
    [0x08, "map_list", [
        (0x00, table.sym_var("next",    "struct map_list *")),
        (0x04, table.sym_var("face",    "struct map_face *")),
    ]],
]

struct_map_data = [
]

struct_o_script = [
]

struct_title = [
]

struct_title_bg = [
]

struct_file_select = [
]

struct_star_select = [
]

struct_audio_a = [
]

struct_audio_b = [
]

struct_audio_c = [
]

struct_audio_d = [
]

struct_audio_e = [
]

struct_audio_f = [
]

struct_audio_g = [
    [0x0C, "bgmctl", [
        (0x00, table.sym_var("a_voice", "s16")),
        (0x02, table.sym_var("a_vol",   "s16")),
        (0x04, table.sym_var("a_time",  "s16")),
        (0x06, table.sym_var("b_voice", "s16")),
        (0x08, table.sym_var("b_vol",   "s16")),
        (0x0A, table.sym_var("b_time",  "s16")),
    ]],
]

struct_audio_data = [
    [0x1C, "audio_cfg", [
        (0x00, table.sym_var("freq",    "u32")),
        (0x04, table.sym_var("voice",   "u8")),
        (0x05, table.sym_var("e_filt",  "u8")),
        (0x06, table.sym_var("e_size",  "u16")),
        (0x08, table.sym_var("e_vol",   "u16")),
        (0x0A, table.sym_var("vol",     "u16")),
        (0x0C, table.sym_var("_0C",     "size_t")),
        (0x10, table.sym_var("_10",     "size_t")),
        (0x14, table.sym_var("_14",     "size_t")),
        (0x18, table.sym_var("_18",     "size_t")),
    ]],
]

struct_audio_bss = [
]

struct_face_main = [
]

struct_face_mem = [
]

struct_face_sfx = [
]

struct_face_draw = [
]

struct_face_object = [
]

struct_face_skin = [
]

struct_face_particle = [
]

struct_face_dynlist = [
]

struct_face_gadget = [
]

struct_face_stdio = [
]

struct_face_joint = [
]

struct_face_net = [
]

struct_face_math = [
]

struct_face_shape = [
]

struct_face_gfx = [
]
