import table

str_ultra_internal_c = """
#ifdef __GNUC__
#define DALIGN                  __attribute__((aligned(4)))
#define BALIGN                  __attribute__((aligned(8)))
#else
#define DALIGN
#define BALIGN
#endif

typedef struct
{
    OSThread           *next;
    OSPri               priority;
}
__OSThreadTail;

typedef struct
{
    OSMesgQueue        *messageQueue;
    OSMesg              message;
}
__OSEventState;

typedef struct
{
    u16 _00;
    u16 _02;
    void *_04;
    OSViMode *_08;
    u32 _0C;
    OSMesgQueue *_10;
    OSMesg *_14;
    f32 _18;
    u16 _1C;
    u32 _20;
    f32 _24;
    u16 _28;
    u32 _2C;
}
__OSViContext;
"""

str_types_g = """
#define _STR(x)                 #x
#define STR(x)                  _STR(x)
#define _ASSET(x)               BUILD/x
#define ASSET(x)                STR(_ASSET(x))
"""

str_types_c = """
typedef unsigned int uint;
typedef s16 VECS[3];
typedef f32 VECF[3];
typedef f32 MTXF[4][4];

#ifdef sgi
typedef signed char CHAR;
typedef unsigned char UCHAR;
typedef short SHORT;
typedef unsigned short USHORT;
#else
typedef int CHAR;
typedef uint UCHAR;
typedef int SHORT;
typedef uint USHORT;
#endif

#ifdef __GNUC__
#define DALIGN                  __attribute__((aligned(4)))
#define BALIGN                  __attribute__((aligned(8)))
#define UNUSED                  __attribute__((unused))
#define FALLTHROUGH             __attribute__((fallthrough))
#else
#define DALIGN
#define BALIGN
#define UNUSED
#define FALLTHROUGH
#endif
#define lenof(x)                (sizeof((x)) / sizeof((x)[0]))

/* todo: move to header */
typedef s16 PATH_DATA;

typedef struct dummy0 DUMMY0;
typedef struct dummy1 DUMMY1;
typedef struct dummy2 DUMMY2;
typedef struct dummy3 DUMMY3;
"""

str_types_s = """
.macro li.u rt, imm
    .if ((\\imm) & 0xFFFF8000) == 0 || ((\\imm) & 0xFFFF8000) == 0xFFFF8000
    .elseif (\\imm) >> 16 == 0
    .else
        lui     \\rt, (\\imm) >> 16
    .endif
.endm

.macro li.l rt, imm
    .if ((\\imm) & 0xFFFF8000) == 0 || ((\\imm) & 0xFFFF8000) == 0xFFFF8000
        addiu   \\rt, $0, (\\imm) & 0xFFFF
    .elseif (\\imm) >> 16 == 0
        ori     \\rt, $0, (\\imm) & 0xFFFF
    .else
        ori     \\rt, (\\imm) & 0xFFFF
    .endif
.endm

.macro la.u rt, imm
    lui     \\rt, %hi(\\imm)
.endm

.macro la.l rt, imm
    addiu   \\rt, %lo(\\imm)
.endm
"""

str_gbi_ext_c = """
#undef G_BL_CLR_FOG
#define G_BL_CLR_FOG 3U

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

str_segment_g = """
#define SEGMENT_CIMG            0x8038F800
#define SEGMENT_ZIMG            0x80000400
#define SEGMENT_MEM_START       0x8005C000
#define SEGMENT_MEM_END         0x801C1000
#define SEGMENT_BUFFER          0x801C1000
#define SEGMENT_FIFO            0x80227000
#define SEGMENT_CODE            0x80246000
#define SEGMENT_LIB             0x80378800
#define SEGMENT_MENU            0x8016F000

#define SEGMENT_DATA_FACE       0x04000000

#define SEGMENT_VIDEO           0x01000000
#define SEGMENT_SZP_MAIN        0x02000000
#define SEGMENT_SZP_GLOBAL      0x03000000
#define SEGMENT_SZP_PLAYER      0x04000000
#define SEGMENT_SZP_SHAPE1      0x05000000
#define SEGMENT_SZP_SHAPE2      0x06000000
#define SEGMENT_SZP_STAGE       0x07000000
#define SEGMENT_SZP_MENU        0x07000000
#define SEGMENT_SZP_SHAPE3      0x08000000
#define SEGMENT_SZP_TEXTURE     0x09000000
#define SEGMENT_SZP_BACKGROUND  0x0A000000
#define SEGMENT_SZP_WEATHER     0x0B000000
#define SEGMENT_DATA_SHAPE1     0x0C000000
#define SEGMENT_DATA_SHAPE2     0x0D000000
#define SEGMENT_DATA_STAGE      0x0E000000
#define SEGMENT_DATA_SHAPE3     0x0F000000
#define SEGMENT_DATA_MAIN       0x10000000
#define SEGMENT_ANIME_MARIO     0x11000000
#define SEGMENT_ANIME_LUIGI     0x12000000
#define SEGMENT_DATA_OBJECT     0x13000000
#define SEGMENT_DATA_MENU       0x14000000
#define SEGMENT_DATA_GAME       0x15000000
#define SEGMENT_DATA_GLOBAL     0x16000000
#define SEGMENT_DATA_PLAYER     0x17000000
#define SEGMENT_DEMO            0x18000000

#define SEG_VIDEO               (SEGMENT_VIDEO          >> 24)
#define SEG_SZP_MAIN            (SEGMENT_SZP_MAIN       >> 24)
#define SEG_SZP_GLOBAL          (SEGMENT_SZP_GLOBAL     >> 24)
#define SEG_SZP_PLAYER          (SEGMENT_SZP_PLAYER     >> 24)
#define SEG_SZP_SHAPE1          (SEGMENT_SZP_SHAPE1     >> 24)
#define SEG_SZP_SHAPE2          (SEGMENT_SZP_SHAPE2     >> 24)
#define SEG_SZP_STAGE           (SEGMENT_SZP_STAGE      >> 24)
#define SEG_SZP_MENU            (SEGMENT_SZP_MENU       >> 24)
#define SEG_SZP_SHAPE3          (SEGMENT_SZP_SHAPE3     >> 24)
#define SEG_SZP_TEXTURE         (SEGMENT_SZP_TEXTURE    >> 24)
#define SEG_SZP_BACKGROUND      (SEGMENT_SZP_BACKGROUND >> 24)
#define SEG_SZP_WEATHER         (SEGMENT_SZP_WEATHER    >> 24)
#define SEG_DATA_SHAPE1         (SEGMENT_DATA_SHAPE1    >> 24)
#define SEG_DATA_SHAPE2         (SEGMENT_DATA_SHAPE2    >> 24)
#define SEG_DATA_STAGE          (SEGMENT_DATA_STAGE     >> 24)
#define SEG_DATA_SHAPE3         (SEGMENT_DATA_SHAPE3    >> 24)
#define SEG_DATA_MAIN           (SEGMENT_DATA_MAIN      >> 24)
#define SEG_ANIME_MARIO         (SEGMENT_ANIME_MARIO    >> 24)
#define SEG_ANIME_LUIGI         (SEGMENT_ANIME_LUIGI    >> 24)
#define SEG_DATA_OBJECT         (SEGMENT_DATA_OBJECT    >> 24)
#define SEG_DATA_MENU           (SEGMENT_DATA_MENU      >> 24)
#define SEG_DATA_GAME           (SEGMENT_DATA_GAME      >> 24)
#define SEG_DATA_GLOBAL         (SEGMENT_DATA_GLOBAL    >> 24)
#define SEG_DATA_PLAYER         (SEGMENT_DATA_PLAYER    >> 24)
#define SEG_DEMO                (SEGMENT_DEMO           >> 24)
"""

str_script_c = """
#define _C(c, x, y) ((u32)(u8)(c) << 24 | (u32)(u8)(x) << 16 | (u32)(u16)(y))
#define _H(x, y)    ((u32)(u16)(x) << 16 | (u32)(u16)(y))
#define _W(x)       ((u32)(x))
#define _F(x)       ((u32)(int)(0x10000*(x)))
#define _P(x)       ((uintptr_t)(x))
"""

str_script_s = """
#define _B(c, x, y, z)          .byte (c), (x), (y), (z)
#define _C(c, x, y)             .byte (c), (x); .short (y)
#define _H(x, y)                .short (x), (y)
#define _W(x)                   .int (x)
#define _F(x)                   .float (x)
#define _P(x)                   .word (x)
"""

str_main_g = """
#define SCREEN_WD               320
#define SCREEN_HT               240
#define BORDER_HT               8

"""

str_app_g = """
#define GFX_LEN                 6400
#define FIFO_SIZE               0x1F000

#define CONTROLLER_LEN          2
"""

str_game_g = """
#define STAGE_NULL              0
#define STAGE_1                 1
#define STAGE_2                 2
#define STAGE_3                 3
#define STAGE_BBH               4
#define STAGE_CCM               5
#define STAGE_INSIDE            6
#define STAGE_HMC               7
#define STAGE_SSL               8
#define STAGE_BOB               9
#define STAGE_SL                10
#define STAGE_WDW               11
#define STAGE_JRB               12
#define STAGE_THI               13
#define STAGE_TTC               14
#define STAGE_RR                15
#define STAGE_GROUNDS           16
#define STAGE_BITDW             17
#define STAGE_VCUTM             18
#define STAGE_BITFS             19
#define STAGE_SA                20
#define STAGE_BITS              21
#define STAGE_LLL               22
#define STAGE_DDD               23
#define STAGE_WF                24
#define STAGE_ENDING            25
#define STAGE_COURTYARD         26
#define STAGE_PSS               27
#define STAGE_COTMC             28
#define STAGE_TOTWC             29
#define STAGE_BITDWA            30
#define STAGE_WMOTR             31
#define STAGE_32                32
#define STAGE_BITFSA            33
#define STAGE_BITSA             34
#define STAGE_35                35
#define STAGE_TTM               36
#define STAGE_37                37
#define STAGE_38                38
"""

str_memory_g = """
#define MEM_ALLOC_L 0
#define MEM_ALLOC_R 1
"""

str_memory_c = """
#define malloc(size)            heap_alloc(mem_heap, size)
#define free(ptr)               heap_free(mem_heap, ptr)
"""

str_memory_s = """
#define TABLE()     .word (table_end-table)/8, 0
#define FILE(name)  .word name, name##_end-name
"""

str_save_g = """
#define SAVE_ACTIVE             0x000001
#define SAVE_000002             0x000002
#define SAVE_000004             0x000004
#define SAVE_000008             0x000008
#define SAVE_000010             0x000010
#define SAVE_000020             0x000020
#define SAVE_000040             0x000040
#define SAVE_000080             0x000080
#define SAVE_000100             0x000100
#define SAVE_000200             0x000200
#define SAVE_000400             0x000400
#define SAVE_000800             0x000800
#define SAVE_001000             0x001000
#define SAVE_002000             0x002000
#define SAVE_004000             0x004000
#define SAVE_008000             0x008000
#define SAVE_010000             0x010000
#define SAVE_020000             0x020000
#define SAVE_040000             0x040000
#define SAVE_080000             0x080000
#define SAVE_100000             0x100000
"""

str_save_c = """
#define stage_to_course(stage)  course_table[(stage)-1]

#define save_file_star_total(file)  save_file_star_range(file, 0, 24)

#define save_write()                save_file_write(save_index-1)
#define save_erase()                save_file_erase(save_index-1)
#define save_isactive()             save_file_isactive(save_index-1)
#define save_star_count(course)     save_file_star_count(save_index-1, course)
#define save_star_range(min, max)   save_file_star_range(save_index-1, min, max)
#define save_star_total()           save_file_star_total(save_index-1)
#define save_star_get(course)       save_file_star_get(save_index-1, course)
#define save_star_set(course, flag) \
    save_file_star_set(save_index-1, course, flag)
#define save_coin_get(course)       save_file_coin_get(save_index-1, course)
"""

str_scene_g = """
#define SCENE_LEN               8
#define SHAPE_LEN               0x100

#define SCENE_FLAG_01           0x01

#define ENV_GRASS               0
#define ENV_ROCK                1
#define ENV_SNOW                2
#define ENV_SAND                3
#define ENV_GHOST               4
#define ENV_WATER               5
#define ENV_SLIDER              6
"""

str_time_g = """
#define TIME_GFXCPU_START       0
#define TIME_GFXCPU_ENDUPD      1
#define TIME_GFXCPU_ENDGFX      2
#define TIME_GFXCPU_ENDRDP      3
#define TIME_GFXCPU_END         4
#define TIME_GFXCPU_MAX         5

#define TIME_GFXRCP_START       0
#define TIME_GFXRCP_ENDRSP      1
#define TIME_GFXRCP_ENDRDP      2
#define TIME_GFXRCP_MAX         3

#define TIME_AUDCPU_MAX         8

#define TIME_AUDRCP_MAX         8
"""

str_object_c = """
#define /* 0x08C */ o_flag              mem[O_MEM_FLAG].s32
#define /* 0x090 */ o_msg_code          mem[O_MEM_MSG].s16[0]
#define /* 0x092 */ o_msg_state         mem[O_MEM_MSG].s16[1]
#define /* 0x09C */ o_col_timer         mem[O_MEM_COL_TIMER].s32
#define /* 0x0A0 */ o_pos_x             mem[O_MEM_POS_X].f32
#define /* 0x0A4 */ o_pos_y             mem[O_MEM_POS_Y].f32
#define /* 0x0A8 */ o_pos_z             mem[O_MEM_POS_Z].f32
#define /* 0x0AC */ o_vel_x             mem[O_MEM_VEL_X].f32
#define /* 0x0B0 */ o_vel_y             mem[O_MEM_VEL_Y].f32
#define /* 0x0B4 */ o_vel_z             mem[O_MEM_VEL_Z].f32
#define /* 0x0B8 */ o_vel_f             mem[O_MEM_VEL_F].f32
#define /* 0x0BC */ o_vel_l             mem[O_MEM_VEL_L].f32
#define /* 0x0C0 */ o_vel_u             mem[O_MEM_VEL_U].f32
#define /* 0x0C4 */ o_rot_x             mem[O_MEM_ROT_X].s32
#define /* 0x0C8 */ o_rot_y             mem[O_MEM_ROT_Y].s32
#define /* 0x0CC */ o_rot_z             mem[O_MEM_ROT_Z].s32
#define /* 0x0D0 */ o_shape_rot_x       mem[O_MEM_SHAPE_ROT_X].s32
#define /* 0x0D4 */ o_shape_rot_y       mem[O_MEM_SHAPE_ROT_Y].s32
#define /* 0x0D8 */ o_shape_rot_z       mem[O_MEM_SHAPE_ROT_Z].s32
#define /* 0x0DC */ o_shape_off_y       mem[O_MEM_SHAPE_OFF_Y].f32
#define /* 0x0E0 */ o_particle          mem[O_MEM_PARTICLE].s32
#define /* 0x0E4 */ o_gravity           mem[O_MEM_GRAVITY].f32
#define /* 0x0E8 */ o_ground_y          mem[O_MEM_GROUND_Y].f32
#define /* 0x0EC */ o_move_flag         mem[O_MEM_MOVE_FLAG].s32
#define /* 0x0F0 */ o_anime_code        mem[O_MEM_ANIME_CODE].s32
#define /* 0x114 */ o_rot_vel_x         mem[O_MEM_ROT_VEL_X].s32
#define /* 0x118 */ o_rot_vel_y         mem[O_MEM_ROT_VEL_Y].s32
#define /* 0x11C */ o_rot_vel_z         mem[O_MEM_ROT_VEL_Z].s32
#define /* 0x120 */ o_anime             mem[O_MEM_ANIME].ptr
#define /* 0x124 */ o_hold              mem[O_MEM_HOLD].s32
#define /* 0x128 */ o_wall_r            mem[O_MEM_WALL_R].f32
#define /* 0x12C */ o_drag              mem[O_MEM_DRAG].f32
#define /* 0x130 */ o_col_type          mem[O_MEM_COL_TYPE].s32
#define /* 0x134 */ o_col_flag          mem[O_MEM_COL_FLAG].s32
#define /* 0x138 */ o_off_x             mem[O_MEM_OFF_X].f32
#define /* 0x13C */ o_off_y             mem[O_MEM_OFF_Y].f32
#define /* 0x140 */ o_off_z             mem[O_MEM_OFF_Z].f32
#define /* 0x144 */ o_code              mem[O_MEM_CODE].s32
#define /* 0x14C */ o_state             mem[O_MEM_STATE].s32
#define /* 0x150 */ o_mode              mem[O_MEM_MODE].s32
#define /* 0x154 */ o_timer             mem[O_MEM_TIMER].s32
#define /* 0x158 */ o_bounce            mem[O_MEM_BOUNCE].f32
#define /* 0x15C */ o_pl_dist           mem[O_MEM_PL_DIST].f32
#define /* 0x160 */ o_pl_rot            mem[O_MEM_PL_ROT].s32
#define /* 0x164 */ o_org_x             mem[O_MEM_ORG_X].f32
#define /* 0x168 */ o_org_y             mem[O_MEM_ORG_Y].f32
#define /* 0x16C */ o_org_z             mem[O_MEM_ORG_Z].f32
#define /* 0x170 */ o_friction          mem[O_MEM_FRICTION].f32
#define /* 0x174 */ o_density           mem[O_MEM_DENSITY].f32
#define /* 0x178 */ o_anime_index       mem[O_MEM_ANIME_INDEX].s32
#define /* 0x17C */ o_alpha             mem[O_MEM_ALPHA].s32
#define /* 0x180 */ o_ap                mem[O_MEM_AP].s32
#define /* 0x184 */ o_hp                mem[O_MEM_HP].s32
#define /* 0x188 */ o_arg               mem[O_MEM_ARG].s32
#define /* 0x18C */ o_state_prev        mem[O_MEM_STATE_PREV].s32
#define /* 0x190 */ o_col_arg           mem[O_MEM_COL_ARG].s32
#define /* 0x194 */ o_col_dist          mem[O_MEM_COL_DIST].f32
#define /* 0x198 */ o_coin              mem[O_MEM_COIN].s32
#define /* 0x19C */ o_shape_dist        mem[O_MEM_SHAPE_DIST].f32
#define /* 0x1A0 */ o_area              mem[O_MEM_AREA].s32
#define /* 0x1A8 */ o_prg_arg           mem[O_MEM_PRG_ARG].s32
#define /* 0x1B4 */ o_wall_ry           mem[O_MEM_WALL_RY].s32
#define /* 0x1B8 */ o_ground_type       mem[O_MEM_GROUND_ARG].s16[0]
#define /* 0x1BA */ o_ground_area       mem[O_MEM_GROUND_ARG].s16[1]
#define /* 0x1BC */ o_org_ry            mem[O_MEM_ORG_RY].s32
#define /* 0x1C0 */ o_ground            mem[O_MEM_GROUND].ptr
#define /* 0x1C4 */ o_se_die            mem[O_MEM_SE_DIE].s32

#define obj_code_get(obj)               (((obj)->o_arg & 0x00FF0000) >> 16)
"""

str_obj_data_g = """
#define P_OBJ_START             31
#define P_OBJ_END               (P_OBJ_START+(-1))

#define P_OBJ_COIN              0
#define P_OBJ_1                 1
#define P_OBJ_2                 2
#define P_OBJ_3                 3
#define P_OBJ_REDCOIN           4
#define P_OBJ_6                 6
#define P_OBJ_7                 7
#define P_OBJ_8                 8
#define P_OBJ_9                 9
#define P_OBJ_10                10
#define P_OBJ_11                11
#define P_OBJ_12                12
#define P_OBJ_13                13
#define P_OBJ_14                14
#define P_OBJ_20                20
#define P_OBJ_SIGNPOST          21
#define P_OBJ_22                22
#define P_OBJ_23                23
#define P_OBJ_24                24
#define P_OBJ_25                25
#define P_OBJ_26                26
#define P_OBJ_27                27
#define P_OBJ_28                28
#define P_OBJ_29                29
#define P_OBJ_30                30
#define P_OBJ_31                31
#define P_OBJ_32                32
#define P_OBJ_33                33
#define P_OBJ_34                34
#define P_OBJ_35                35
#define P_OBJ_36                36
#define P_OBJ_37                37
#define P_OBJ_38                38
#define P_OBJ_39                39
#define P_OBJ_40                40
#define P_OBJ_41                41
#define P_OBJ_42                42
#define P_OBJ_43                43
#define P_OBJ_44                44
#define P_OBJ_45                45
#define P_OBJ_46                46
#define P_OBJ_47                47
#define P_OBJ_48                48
#define P_OBJ_49                49
#define P_OBJ_50                50
#define P_OBJ_51                51
#define P_OBJ_53                53
#define P_OBJ_54                54
#define P_OBJ_55                55
#define P_OBJ_56                56
#define P_OBJ_57                57
#define P_OBJ_58                58
#define P_OBJ_59                59
#define P_OBJ_60                60
#define P_OBJ_61                61
#define P_OBJ_62                62
#define P_OBJ_63                63
#define P_OBJ_64                64
#define P_OBJ_65                65
#define P_OBJ_66                66
#define P_OBJ_67                67
#define P_OBJ_68                68
#define P_OBJ_69                69  /* CORKBOX */
#define P_OBJ_70                70  /* CORKBOXCOIN */
#define P_OBJ_71                71  /* METALBOX */
#define P_OBJ_72                72  /* SMALLBOX */
#define P_OBJ_73                73
#define P_OBJ_74                74
#define P_OBJ_75                75
#define P_OBJ_76                76
#define P_OBJ_77                77
#define P_OBJ_78                78
#define P_OBJ_79                79
#define P_OBJ_81                81
#define P_OBJ_82                82
#define P_OBJ_84                84
#define P_OBJ_85                85
#define P_OBJ_86                86
#define P_OBJ_87                87
#define P_OBJ_88                88
#define P_OBJ_89                89
#define P_OBJ_93                93
#define P_OBJ_94                94
#define P_OBJ_96                96
#define P_OBJ_97                97
#define P_OBJ_98                98
#define P_OBJ_106               106
#define P_OBJ_107               107
#define P_OBJ_108               108
#define P_OBJ_109               109
#define P_OBJ_110               110
#define P_OBJ_111               111
#define P_OBJ_112               112
#define P_OBJ_113               113
#define P_OBJ_114               114
#define P_OBJ_115               115
#define P_OBJ_123               123
#define P_OBJ_125               125
#define P_OBJ_126               126
#define P_OBJ_137               137
#define P_OBJ_138               138
#define P_OBJ_139               139
#define P_OBJ_140               140
#define P_OBJ_141               141
#define P_OBJ_151               151
#define P_OBJ_152               152
#define P_OBJ_153               153
#define P_OBJ_154               154
#define P_OBJ_156               156
#define P_OBJ_165               165
#define P_OBJ_166               166
#define P_OBJ_167               167
#define P_OBJ_169               169
#define P_OBJ_170               170
#define P_OBJ_171               171
#define P_OBJ_172               172
#define P_OBJ_189               189
#define P_OBJ_190               190
#define P_OBJ_191               191
#define P_OBJ_192               192
#define P_OBJ_193               193
#define P_OBJ_194               194
#define P_OBJ_195               195
#define P_OBJ_196               196
#define P_OBJ_234               234
#define P_OBJ_235               235
#define P_OBJ_236               236
#define P_OBJ_237               237
#define P_OBJ_238               238
#define P_OBJ_239               239
#define P_OBJ_240               240
#define P_OBJ_241               241
#define P_OBJ_242               242
#define P_OBJ_243               243
#define P_OBJ_251               251
#define P_OBJ_252               252
#define P_OBJ_253               253
#define P_OBJ_255               255
#define P_OBJ_256               256
#define P_OBJ_258               258
#define P_OBJ_259               259
#define P_OBJ_260               260
#define P_OBJ_261               261
#define P_OBJ_262               262
#define P_OBJ_263               263
#define P_OBJ_281               281
#define P_OBJ_289               289
#define P_OBJ_290               290
#define P_OBJ_291               291
#define P_OBJ_292               292
#define P_OBJ_293               293
#define P_OBJ_303               303
#define P_OBJ_313               313
#define P_OBJ_314               314
#define P_OBJ_315               315
#define P_OBJ_316               316
#define P_OBJ_317               317
#define P_OBJ_318               318
#define P_OBJ_319               319
#define P_OBJ_320               320
#define P_OBJ_321               321
#define P_OBJ_322               322
#define P_OBJ_323               323
#define P_OBJ_324               324
#define P_OBJ_325               325
#define P_OBJ_326               326
#define P_OBJ_327               327
#define P_OBJ_328               328
#define P_OBJ_329               329
#define P_OBJ_339               339
#define P_OBJ_340               340
#define P_OBJ_341               341
#define P_OBJ_342               342
#define P_OBJ_343               343
#define P_OBJ_350               350
#define P_OBJ_351               351
#define P_OBJ_352               352
#define P_OBJ_353               353
#define P_OBJ_354               354
#define P_OBJ_357               357
#define P_OBJ_358               358
#define P_OBJ_359               359
#define P_OBJ_360               360

#define M_EXT_NULL      0
#define M_EXT_RY        1
#define M_EXT_RY_ARG    2
#define M_EXT_XYZ       3
#define M_EXT_RY_CODE   4

#define M_OBJ_PLAYER            0
#define M_OBJ_COIN              1
#define M_OBJ_2                 2
#define M_OBJ_3                 3
#define M_OBJ_4                 4
#define M_OBJ_5                 5
#define M_OBJ_6                 6
#define M_OBJ_7                 7
#define M_OBJ_8                 8
#define M_OBJ_10                10
#define M_OBJ_11                11
#define M_OBJ_12                12
#define M_OBJ_13                13
#define M_OBJ_14                14
#define M_OBJ_15                15
#define M_OBJ_16                16
#define M_OBJ_17                17
#define M_OBJ_18                18
#define M_OBJ_BULLY             19
#define M_OBJ_20                20
#define M_OBJ_26                26
#define M_OBJ_27                27
#define M_OBJ_28                28
#define M_OBJ_29                29
#define M_OBJ_BUTTERFLY         32
#define M_OBJ_33                33
#define M_OBJ_34                34
#define M_OBJ_35                35
#define M_OBJ_36                36
#define M_OBJ_37                37
#define M_OBJ_38                38
#define M_OBJ_39                39
#define M_OBJ_40                40
#define M_OBJ_101               101
#define M_OBJ_102               102
#define M_OBJ_103               103
#define M_OBJ_104               104
#define M_OBJ_105               105
#define M_OBJ_106               106
#define M_OBJ_107               107
#define M_OBJ_108               108
#define M_OBJ_109               109
#define M_OBJ_110               110
#define M_OBJ_111               111
#define M_OBJ_112               112
#define M_OBJ_113               113
#define M_OBJ_114               114
#define M_OBJ_115               115
#define M_OBJ_116               116
#define M_OBJ_117               117
#define M_OBJ_118               118
#define M_OBJ_119               119
#define M_OBJ_120               120
#define M_OBJ_TREE_A            121
#define M_OBJ_TREE_B            122
#define M_OBJ_TREE_C            123
#define M_OBJ_TREE_D            124
#define M_OBJ_TREE_E            125
#define M_OBJ_DOOR_A            137
#define M_OBJ_DOOR_B            126
#define M_OBJ_DOOR_C            127
#define M_OBJ_DOOR_D            128
#define M_OBJ_DOOR_E            129
#define M_OBJ_DOOR_F            130
#define M_OBJ_STARDOOR          138
#define M_OBJ_STARDOOR1         139
#define M_OBJ_STARDOOR3         140
#define M_OBJ_KEYDOOR           141
#define M_OBJ_LINKDOOR_A        136
#define M_OBJ_LINKDOOR_B        131
#define M_OBJ_LINKDOOR_C        132
#define M_OBJ_LINKDOOR_D        133
#define M_OBJ_LINKDOOR_E        134
#define M_OBJ_LINKDOOR_F        135
"""

str_obj_data_c = """
#define P_OBJ(obj, ry, px, py, pz, arg) \\
    (OBJ_DATA)((P_OBJ_START+P_OBJ_##obj) | (ry) << 9), px, py, pz, arg
"""

str_math_c = """
#define sin(x)  math_sin[(u16)(x) >> 4]
#define cos(x)  math_cos[(u16)(x) >> 4]
"""

str_shape_g = """
#define S_TYPE_SCENE            (1)
#define S_TYPE_ORTHO            (2)
#define S_TYPE_PERSP            (3 | 0x100)
#define S_TYPE_LAYER            (4)

#define S_TYPE_EMPTY            (10)
#define S_TYPE_LOD              (11)
#define S_TYPE_SELECT           (12 | 0x100)

#define S_TYPE_CAMERA           (20 | 0x100)
#define S_TYPE_POSROT           (21)
#define S_TYPE_POS              (22)
#define S_TYPE_ROT              (23)
#define S_TYPE_OBJECT           (24)
#define S_TYPE_JOINT            (25)
#define S_TYPE_BILLBOARD        (26)
#define S_TYPE_GFX              (27)
#define S_TYPE_SCALE            (28)

#define S_TYPE_SHADOW           (40)
#define S_TYPE_LIST             (41)
#define S_TYPE_CALLBACK         (42 | 0x100)
#define S_TYPE_BACKGROUND       (44 | 0x100)
#define S_TYPE_HAND             (46 | 0x100)
#define S_TYPE_CULL             (47)

#define S_FLAG_ACTIVE           0x0001
#define S_FLAG_HIDE             0x0002
#define S_FLAG_BILLBOARD        0x0004
#define S_FLAG_ZBUFFER          0x0008
#define S_FLAG_OBJHIDE          0x0010
#define S_FLAG_ANIME            0x0020

#define S_CODE_INIT             0
#define S_CODE_DRAW             1
#define S_CODE_CLOSE            2
#define S_CODE_OPEN             3
#define S_CODE_EXIT             4
#define S_CODE_MTX              5

#define S_LAYER_BACKGROUND      0
#define S_LAYER_OPA_SURF        1
#define S_LAYER_OPA_DECAL       2
#define S_LAYER_OPA_INTER       3
#define S_LAYER_TEX_EDGE        4
#define S_LAYER_XLU_SURF        5
#define S_LAYER_XLU_DECAL       6
#define S_LAYER_XLU_INTER       7
#define S_LAYER_MAX             8

#define ANIME_LOOP              0x0000
#define ANIME_NOLOOP            0x0001
#define ANIME_REVERSE           0x0002
#define ANIME_FIXFRAME          0x0004
#define ANIME_XYZ               0x0000
#define ANIME_Y                 0x0008
#define ANIME_XZ                0x0010
#define ANIME_FIXSHADOW         0x0020
#define ANIME_NOPOS             0x0040
"""

str_shape_c = """
#define shape_layer_get(shp)  (((SHAPE *)(shp))->flag >> 8)
#define shape_layer_set(shp, layer) \\
    (((SHAPE *)(shp))->flag = (layer) << 8 | (((SHAPE *)(shp))->flag & 0xFF))
"""

str_s_script_g = """
#define S_NULL                  0

#define S_MARIO                 1
#define S_GLOW                  143
#define S_SMOKE                 148
#define S_SPARKLE               149
#define S_DUST                  150
#define S_SMOKE2                156
#define S_RIPPLE_MOVE           163
#define S_DROPLET               164
#define S_WAVE                  165
#define S_RIPPLE_STOP           166
#define S_SPLASH                167
#define S_BUBBLE_A              168
#define S_BUBBLE_B              170

/* local */
#define S_PIPE                  22

#define S_TREE_A                23
#define S_TREE_B                24
#define S_TREE_C                25
#define S_TREE_D                26
#define S_TREE_E                27
#define S_DOOR_A                28
#define S_DOOR_B                29
#define S_DOOR_C                30
#define S_DOOR_D                31
#define S_DOOR_E                32
#define S_DOOR_F                33
#define S_STARDOOR              34
#define S_STARDOOR1             35
#define S_STARDOOR3             36
#define S_KEYDOOR               37
#define S_LINKDOOR_A            38
#define S_LINKDOOR_B            39
#define S_LINKDOOR_C            40
#define S_LINKDOOR_D            41
#define S_LINKDOOR_E            42
#define S_LINKDOOR_F            43
#define S_COIN                  116
#define S_COIN_NOSHADOW         117
#define S_BLUECOIN              118
#define S_BLUECOIN_NOSHADOW     119
#define S_SHADOWSTAR            121
#define S_POWERSTAR             122
#define S_SIGNPOST              124
#define S_WINGCAP_E             133
#define S_CAP_E                 134
#define S_WINGCAP_S             135
#define S_CAP_S                 136
#define S_SHARD                 138
#define S_STAR                  139
#define S_WHITEPUFF             142
#define S_FLAME                 144
#define S_BLUEFLAME             145
#define S_SNOW                  158
#define S_SAND                  159
#define S_SNOWBALL              160
#define S_STONE                 161
#define S_LEAF                  162
#define S_FISH                  185
#define S_FISH_SHADOW           186
#define S_BUTTERFLY             187
#define S_DOORKEY               200
#define S_FLAME_SHADOW          203
#define S_BOWSERKEY             204
#define S_EXPLOSION             205
#define S_1UP                   212
#define S_REDCOIN               215
#define S_REDCOIN_NOSHADOW      216
#define S_NUMBER                219
#define S_BLACKPUFF             224

#define S_3A_120                120
#define S_3A_127                127
#define S_3A_128                128
#define S_3A_129                129
#define S_3A_130                130
#define S_3A_131                131
#define S_3A_132                132
#define S_3A_137                137
#define S_3A_140                140
#define S_3A_180                180
#define S_3A_188                188
#define S_3A_190                190
#define S_3A_192                192
#define S_3A_194                194
#define S_3A_195                195
#define S_3A_201                201
#define S_3A_202                202
#define S_3A_207                207
#define S_3A_217                217
#define S_3A_218                218
#define S_3A_220                220
#define S_3A_223                223
#define S_3A_225                225

#define S_1A_84                 84
#define S_1A_85                 85
#define S_1A_86                 86
#define S_1A_87                 87
#define S_1A_88                 88
#define S_1A_89                 89

#define S_BLARGG                84
#define S_BULLY                 86
#define S_BIGBULLY              87

#define S_1C_84                 84
#define S_1C_85                 85
#define S_1C_86                 86

#define S_1D_84                 84
#define S_1D_85                 85
#define S_1D_86                 86
#define S_1D_87                 87
#define S_1D_88                 88

#define S_1E_84                 84
#define S_1E_85                 85
#define S_1E_86                 86
#define S_1E_87                 87
#define S_1E_88                 88
#define S_1E_89                 89

#define S_1F_84                 84
#define S_1F_85                 85
#define S_1F_86                 86
#define S_1F_87                 87

#define S_1G_84                 84
#define S_1G_85                 85
#define S_1G_86                 86
#define S_1G_87                 87

#define S_1H_84                 84
#define S_1H_85                 85
#define S_1H_86                 86

#define S_1I_84                 84
#define S_1I_85                 85
#define S_1I_86                 86
#define S_1I_87                 87
#define S_1I_88                 88
#define S_1I_89                 89
#define S_1I_90                 90

#define S_1J_84                 84
#define S_1J_85                 85
#define S_1J_222                222

#define S_1K_84                 84
#define S_1K_85                 85
#define S_1K_86                 86
#define S_1K_87                 87
#define S_1K_88                 88
#define S_1K_89                 89

/* local */
#define S_2A_3                  3

#define S_2A_100                100
#define S_2A_101                101
#define S_2A_102                102
#define S_2A_103                103
#define S_2A_104                104
#define S_2A_105                105
#define S_2A_179                179

#define S_2B_100                100
#define S_2B_101                101
#define S_2B_102                102
#define S_2B_103                103
#define S_2B_104                104
#define S_2B_105                105
#define S_2B_179                179
#define S_2B_193                193

#define S_2C_100                100
#define S_2C_101                101
#define S_2C_102                102
#define S_2C_103                103
#define S_2C_104                104
#define S_2C_106                106
#define S_2C_107                107
#define S_2C_191                191

#define S_2D_100                100
#define S_2D_101                101
#define S_2D_102                102
#define S_2D_221                221

#define S_2E_100                100
#define S_2E_101                101
#define S_2E_102                102

#define S_2F_100                100
#define S_2F_101                101
#define S_2F_102                102
#define S_2F_103                103
#define S_2F_104                104
#define S_2F_206                206

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
#define S_BITDW_PIPE            18
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
#define S_VCUTM_55              55

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
#define S_BITS_PIPE             73

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
"""

str_s_script_c = """
#define s_script(script)                        \\
    _C(0x00, 0, 0),                             \\
    _P(script)
#define s_end()                                 \\
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
#define s_store(index)                          \\
    _C(0x06, 0, index)
#define s_flag(flag)                            \\
    _C(0x07, 0, flag)
#define s_setflag(flag)                         \\
    _C(0x07, 1, flag)
#define s_clrflag(flag)                         \\
    _C(0x07, 2, flag)
#define s_scene(x, y, w, h, n)                  \\
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
#define s_shadow(size, alpha, type)             \\
    _C(0x16, 0, type),                          \\
    _H(alpha, size)
#define s_object()                              \\
    _C(0x17, 0, 0)
#define s_callback(arg, callback)               \\
    _C(0x18, 0, arg),                           \\
    _P(callback)
#define s_background(arg, callback)             \\
    _C(0x19, 0, arg),                           \\
    _P(callback)
/* 0x1A */
#define s_load(index)                           \\
    _C(0x1B, 0, index)
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
#define s_cull(dist)                            \\
    _C(0x20, 0, dist)

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
extern void *s_logo_symbol(int, struct shape *, void *);
extern void *s_title_bg(int, struct shape *, void *);
extern void *s_gameover_bg(int, struct shape *, void *);

extern void *s_file_select_main(int, struct shape *, void *);

extern void *s_star_select_main(int, struct shape *, void *);
"""

str_p_script_g = """
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
#define P_VAR_SCENE             4
"""

str_p_script_c = """
typedef uintptr_t P_SCRIPT;
"""

str_p_script_s = """
#define p_push_call(seg, name, script)          \\
    _C(0x00, 0x10, SEG_DATA_##seg);             \\
    _P(_##name##_dataSegmentRomStart);          \\
    _P(_##name##_dataSegmentRomEnd);            \\
    _P(script)
#define p_push_jump(seg, name, script)          \\
    _C(0x01, 0x10, SEG_DATA_##seg);             \\
    _P(_##name##_dataSegmentRomStart);          \\
    _P(_##name##_dataSegmentRomEnd);            \\
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
    _P(_##name##SegmentStart);                  \\
    _P(_##name##SegmentRomStart);               \\
    _P(_##name##SegmentRomEnd)
#define p_load_data(seg, name)                  \\
    _C(0x17, 0x0C, SEG_DATA_##seg);             \\
    _P(_##name##_dataSegmentRomStart);          \\
    _P(_##name##_dataSegmentRomEnd)
#define p_load_szp(seg, name)                   \\
    _C(0x18, 0x0C, SEG_SZP_##seg);              \\
    _P(_##name##_szpSegmentRomStart);           \\
    _P(_##name##_szpSegmentRomEnd)
#define p_load_face(arg)                        \\
    _C(0x19, 0x04, arg)
#define p_load_txt(seg, name)                   \\
    _C(0x1A, 0x0C, SEG_SZP_##seg);              \\
    _P(_##name##_szpSegmentRomStart);           \\
    _P(_##name##_szpSegmentRomEnd)
#define p_stage_init()                          \\
    _C(0x1B, 0x04, 0)
#define p_stage_exit()                          \\
    _C(0x1C, 0x04, 0)
#define p_stage_start()                         \\
    _C(0x1D, 0x04, 0)
#define p_stage_end()                           \\
    _C(0x1E, 0x04, 0)
#define p_scene_start(scene, script)            \\
    _B(0x1F, 0x08, scene, 0);                   \\
    _P(script)
#define p_scene_end()                           \\
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
#define p_object(                               \\
    mask, shape, px, py, pz, rx, ry, rz,        \\
    arg0, arg1, flag, script                    \\
)                                               \\
    _B(0x24, 0x18, mask, shape);                \\
    _H(px, py);                                 \\
    _H(pz, rx);                                 \\
    _H(ry, rz);                                 \\
    _C(arg0, arg1, flag);                       \\
    _P(script)
#define p_object_globl(                         \\
    shape, px, py, pz, rx, ry, rz,              \\
    arg0, arg1, flag, script                    \\
)                                               \\
    p_object(0x1F, shape, px, py, pz, rx, ry, rz, arg0, arg1, flag, script)
#define p_player(shape, arg0, arg1, flag, script)   \\
    _B(0x25, 0x0C, 0, shape);                   \\
    _C(arg0, arg1, flag);                       \\
    _P(script)
#define p_mario()                               \\
    p_player(S_MARIO, 0, 0, 1, o_mario)
#define p_link(index, stage, scene, link)       \\
    _B(0x26, 0x08, index, stage);               \\
    _B(scene, link, 0x00, 0)
#define p_link_mid(index, stage, scene, link)   \\
    _B(0x26, 0x08, index, stage);               \\
    _B(scene, link, 0x80, 0)
#define p_linkbg(index, stage, scene, link)     \\
    _B(0x27, 0x08, index, stage);               \\
    _B(scene, link, 0x00, 0)
#define p_linkbg_mid(index, stage, scene, link) \\
    _B(0x27, 0x08, index, stage);               \\
    _B(scene, link, 0x80, 0)
#define p_connect(index, scene, px, py, pz)     \\
    _B(0x28, 0x0C, index, scene);               \\
    _H(px, py);                                 \\
    _H(pz, 0)
#define p_scene_open(scene)                     \\
    _B(0x29, 0x04, scene, 0)
#define p_scene_close(scene)                    \\
    _B(0x2A, 0x04, scene, 0)
#define p_player_open(scene, ry, px, py, pz)    \\
    _B(0x2B, 0x0C, scene, 0);                   \\
    _H(ry, px);                                 \\
    _H(py, pz)
/* 0x2C player_close */
#define p_scene_update()                        \\
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
    _C(0x31, 0x04, ENV_##env)
/* 0x32 */
#define p_wipe(type, time, r, g, b)             \\
    _B(0x33, 0x08, type, time);                 \\
    _B(r, g, b, 0)
#define p_vi_black(arg)                         \\
    _B(0x34, 0x04, arg, 0)
#define p_vi_gamma(arg)                         \\
    _B(0x35, 0x04, arg, 0)
#define p_bgm(mode, bgm)                        \\
    _C(0x36, 0x08, mode);                       \\
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

str_map_data_g = """
#define M_VTX                   0x40
#define M_PLANEEND              0x41
#define M_END                   0x42
#define M_OBJ                   0x43
#define M_WATER                 0x44
"""

str_map_data_c = """
typedef s16 OBJ_DATA;
typedef s16 MAP_DATA;
typedef u8 AREA_DATA;
"""

str_o_script_g = """
#define O_MEM_VAR               0
#define O_MEM_FLAG              1
#define O_MEM_MSG               2
#define O_MEM_3                 3
#define O_MEM_4                 4
#define O_MEM_COL_TIMER         5
#define O_MEM_POS_X             6
#define O_MEM_POS_Y             7
#define O_MEM_POS_Z             8
#define O_MEM_VEL_X             9
#define O_MEM_VEL_Y             10
#define O_MEM_VEL_Z             11
#define O_MEM_VEL_F             12
#define O_MEM_VEL_L             13
#define O_MEM_VEL_U             14
#define O_MEM_ROT_X             15
#define O_MEM_ROT_Y             16
#define O_MEM_ROT_Z             17
#define O_MEM_SHAPE_ROT_X       18
#define O_MEM_SHAPE_ROT_Y       19
#define O_MEM_SHAPE_ROT_Z       20
#define O_MEM_SHAPE_OFF_Y       21
#define O_MEM_PARTICLE          22
#define O_MEM_GRAVITY           23
#define O_MEM_GROUND_Y          24
#define O_MEM_MOVE_FLAG         25
#define O_MEM_ANIME_CODE        26
#define O_MEM_V0                27
#define O_MEM_V1                28
#define O_MEM_V2                29
#define O_MEM_V3                30
#define O_MEM_V4                31
#define O_MEM_V5                32
#define O_MEM_V6                33
#define O_MEM_V7                34
#define O_MEM_ROT_VEL_X         35
#define O_MEM_ROT_VEL_Y         36
#define O_MEM_ROT_VEL_Z         37
#define O_MEM_ANIME             38
#define O_MEM_HOLD              39
#define O_MEM_WALL_R            40
#define O_MEM_DRAG              41
#define O_MEM_COL_TYPE          42
#define O_MEM_COL_FLAG          43
#define O_MEM_OFF_X             44
#define O_MEM_OFF_Y             45
#define O_MEM_OFF_Z             46
#define O_MEM_CODE              47
#define O_MEM_48                48
#define O_MEM_STATE             49
#define O_MEM_MODE              50
#define O_MEM_TIMER             51
#define O_MEM_BOUNCE            52
#define O_MEM_PL_DIST           53
#define O_MEM_PL_ROT            54
#define O_MEM_ORG_X             55
#define O_MEM_ORG_Y             56
#define O_MEM_ORG_Z             57
#define O_MEM_FRICTION          58
#define O_MEM_DENSITY           59
#define O_MEM_ANIME_INDEX       60
#define O_MEM_ALPHA             61
#define O_MEM_AP                62
#define O_MEM_HP                63
#define O_MEM_ARG               64
#define O_MEM_STATE_PREV        65
#define O_MEM_COL_ARG           66
#define O_MEM_COL_DIST          67
#define O_MEM_COIN              68
#define O_MEM_SHAPE_DIST        69
#define O_MEM_AREA              70
#define O_MEM_71                71
#define O_MEM_PRG_ARG           72
#define O_MEM_V8                73
#define O_MEM_V9                74
#define O_MEM_WALL_RY           75
#define O_MEM_GROUND_ARG        76
#define O_MEM_ORG_RY            77
#define O_MEM_GROUND            78
#define O_MEM_SE_DIE            79

#define O_TYPE_PLAYER           0
#define O_TYPE_1                1
#define O_TYPE_PL_ATTACK        2
#define O_TYPE_3                3
#define O_TYPE_ENEMYA           4
#define O_TYPE_ENEMYB           5
#define O_TYPE_ITEM             6
#define O_TYPE_7                7
#define O_TYPE_DEFAULT          8
#define O_TYPE_MOVEBG           9
#define O_TYPE_PL_USE           10
#define O_TYPE_SYSTEM           11
#define O_TYPE_EFFECT           12
"""

str_o_script_c = """
typedef uintptr_t O_SCRIPT;
typedef void O_CALLBACK(void);
"""

str_o_script_s = """
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
#define o_col_hit(radius, height)               \\
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
#define o_col_off(radius, height, offset)       \\
    _C(0x2B, 0, 0);                             \\
    _H(radius, height);                         \\
    _H(offset, 0)
#define o_child(shape, script)                  \\
    _C(0x2C, 0, 0);                             \\
    _W(shape);                                  \\
    _P(script)
#define o_origin()                              \\
    _C(0x2D, 0, 0)
#define o_col_dmg(radius, height)               \\
    _C(0x2E, 0, 0);                             \\
    _H(radius, height)
#define o_col_type(type)                        \\
    _C(0x2F, 0, 0);                             \\
    _W(type)
#define o_physics(wall_r, gravity, bounce, drag, friction, density, g, h)   \\
    _C(0x30, 0, 0);                             \\
    _H(wall_r, gravity);                        \\
    _H(bounce, drag);                           \\
    _H(friction, density);                      \\
    _H(g, h)
#define o_col_arg(arg)                          \\
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

str_audio_g_g = """
#define NA_MODE_DEFAULT         0
#define NA_MODE_CASTLE          1
#define NA_MODE_ARENA           2
#define NA_MODE_WATER           3
#define NA_MODE_DUNGEON         4
#define NA_MODE_FIELD           5
#define NA_MODE_GHOST           6
#define NA_MODE_STAFF           7

#define NA_SEQ_SE               0
#define NA_SEQ_STAR_CATCH       1
#define NA_SEQ_TITLE            2
#define NA_SEQ_FIELD            3
#define NA_SEQ_CASTLE           4
#define NA_SEQ_WATER            5
#define NA_SEQ_FIRE             6
#define NA_SEQ_ARENA            7
#define NA_SEQ_SNOW             8
#define NA_SEQ_SLIDER           9
#define NA_SEQ_GHOST            10
#define NA_SEQ_LULLABY          11
#define NA_SEQ_DUNGEON          12
#define NA_SEQ_STAR_SELECT      13
#define NA_SEQ_WING             14
#define NA_SEQ_METAL            15
#define NA_SEQ_MSG_BOWSER       16
#define NA_SEQ_BOWSER           17
#define NA_SEQ_HI_SCORE         18
#define NA_SEQ_MERRY_GO_ROUND   19
#define NA_SEQ_FANFARE          20
#define NA_SEQ_STAR             21
#define NA_SEQ_BATTLE           22
#define NA_SEQ_ARENA_CLEAR      23
#define NA_SEQ_ENDLESS          24
#define NA_SEQ_FINAL            25
#define NA_SEQ_STAFF            26
#define NA_SEQ_SOLUTION         27
#define NA_SEQ_MSG_TOAD         28
#define NA_SEQ_MSG_PEACH        29
#define NA_SEQ_INTRO            30
#define NA_SEQ_FINAL_CLEAR      31
#define NA_SEQ_ENDING           32
#define NA_SEQ_FILE_SELECT      33
#define NA_SEQ_MSG_LAKITU       34

#define NA_BGM_NULL             0
/* #define NA_BGM_STAR_CATCH       NA_SEQ_STAR_CATCH */
#define NA_BGM_TITLE            NA_SEQ_TITLE
#define NA_BGM_GAMEOVER         (0x080 | NA_SEQ_TITLE)
#define NA_BGM_FIELD            NA_SEQ_FIELD
#define NA_BGM_CASTLE           NA_SEQ_CASTLE
#define NA_BGM_WATER            NA_SEQ_WATER
#define NA_BGM_AQUARIUM         (0x080 | NA_SEQ_WATER)
#define NA_BGM_FIRE             NA_SEQ_FIRE
#define NA_BGM_ARENA            NA_SEQ_ARENA
#define NA_BGM_SNOW             NA_SEQ_SNOW
#define NA_BGM_SLIDER           NA_SEQ_SLIDER
#define NA_BGM_GHOST            NA_SEQ_GHOST
/* #define NA_BGM_LULLABY          NA_SEQ_LULLABY */
#define NA_BGM_DUNGEON          NA_SEQ_DUNGEON
#define NA_BGM_STAR_SELECT      NA_SEQ_STAR_SELECT
/* #define NA_BGM_WING             NA_SEQ_WING */
#define NA_BGM_SHELL            (0x480 | NA_SEQ_WING)
/* #define NA_BGM_METAL            NA_SEQ_METAL */
/* #define NA_BGM_MSG_BOWSER       NA_SEQ_MSG_BOWSER */
#define NA_BGM_BOWSER           NA_SEQ_BOWSER
/* #define NA_BGM_HI_SCORE         NA_SEQ_HI_SCORE */
/* #define NA_BGM_MERRY_GO_ROUND   NA_SEQ_MERRY_GO_ROUND */
/* #define NA_BGM_FANFARE          NA_SEQ_FANFARE */
/* #define NA_BGM_STAR             NA_SEQ_STAR */
/* #define NA_BGM_BATTLE           NA_SEQ_BATTLE */
/* #define NA_BGM_ARENA_CLEAR      NA_SEQ_ARENA_CLEAR */
#define NA_BGM_ENDLESS          NA_SEQ_ENDLESS
#define NA_BGM_FINAL            NA_SEQ_FINAL
/* #define NA_BGM_STAFF            NA_SEQ_STAFF */
/* #define NA_BGM_SOLUTION         NA_SEQ_SOLUTION */
/* #define NA_BGM_MSG_TOAD         NA_SEQ_MSG_TOAD */
/* #define NA_BGM_MSG_PEACH        NA_SEQ_MSG_PEACH */
/* #define NA_BGM_INTRO            NA_SEQ_INTRO */
/* #define NA_BGM_FINAL_CLEAR      NA_SEQ_FINAL_CLEAR */
/* #define NA_BGM_ENDING           NA_SEQ_ENDING */
#define NA_BGM_FILE_SELECT      NA_SEQ_FILE_SELECT
/* #define NA_BGM_MSG_LAKITU       NA_SEQ_MSG_LAKITU */

#define NA_SE_NULL              0x00000000

#define NA_SE1_00               0x14000001
#define NA_SE1_10               0x14100001
#define NA_SE1_11               0x14110001
#define NA_SE1_12               0x14128001
#define NA_SE1_14               0x14140001
#define NA_SE1_19               0x1D192001
#define NA_SE1_20               0x14200001

#define NA_SE2_31               0x2431FF81
#define NA_SE2_32               0x2432FF81
#define NA_SE2_33               0x2433FFA1

#define NA_SE3_04               0x3004C081
#define NA_SE3_05               0x3005C081
#define NA_SE3_06               0x3006C081
#define NA_SE3_07               0x3007C081
#define NA_SE3_28               0x39280081
#define NA_SE3_2B               0x302B0081
#define NA_SE3_70               0x30703081

#define NA_SE4_00               0x40000001
#define NA_SE4_01               0x40010001
#define NA_SE4_02               0x40020001
#define NA_SE4_03               0x41030001
#define NA_SE4_04               0x40040001
#define NA_SE4_05               0x40050001
#define NA_SE4_08               0x40080001
#define NA_SE4_09               0x40090001
#define NA_SE4_0A               0x400A0001
#define NA_SE4_0B               0x400B0001
#define NA_SE4_0C               0x400C0001
#define NA_SE4_0D_0             0x400D0001
#define NA_SE4_0D_1             0x400D1001

#define NA_SE5_03               0x50030081
#define NA_SE5_05               0x50050081
#define NA_SE5_06               0x50060081
#define NA_SE5_15_50            0x50155081
#define NA_SE5_15_80            0x50158081
#define NA_SE5_21               0x50210081
#define NA_SE5_2D               0x502D0081
#define NA_SE5_38               0x50388081
#define NA_SE5_39               0x50390081
#define NA_SE5_3A               0x503A0081
#define NA_SE5_3B               0x503B0081
#define NA_SE5_3C               0x503C0081
#define NA_SE5_3D               0x503DA081
#define NA_SE5_41               0x50410081
#define NA_SE5_48               0x50480081
#define NA_SE5_51               0x50514001
#define NA_SE5_55               0x50558081
#define NA_SE5_58               0x50584081
#define NA_SE5_5F               0x505F8091
#define NA_SE5_60               0x5060B081
#define NA_SE5_61               0x5061B081
#define NA_SE5_6F               0x506F0081

#define NA_SE6_00               0x60000001
#define NA_SE6_02_80            0x60028001
#define NA_SE6_02_FF            0x6002FF01
#define NA_SE6_03               0x60034001
#define NA_SE6_04_40            0x60044001
#define NA_SE6_04_80            0x60048001
#define NA_SE6_10               0x60104001

#define NA_SE7_06               0x70060081
#define NA_SE7_07               0x70070081
#define NA_SE7_08               0x70080081
#define NA_SE7_09               0x70090081
#define NA_SE7_0A               0x700A0081
#define NA_SE7_0B               0x700B0081
#define NA_SE7_0C               0x700C0081
#define NA_SE7_14               0x70140081
#define NA_SE7_1E               0x701EFF81

#define NA_SE8_50               0x80504001

#define NA_SE9_04               0x90040081
#define NA_SE9_52               0x90524001
#define NA_SE9_69               0x90694081
"""

str_audio_g_c = """
#define Na_SE_fixed(se)         Na_SE_play(se, Na_0)
#define Na_SE_obj(se, obj)      Na_SE_play(se, (obj)->list.s.view)

#define Na_SE_lock()            Na_IO_lock(2, 0x037A)
#define Na_SE_unlock()          Na_IO_unlock(2, 0x037A)

typedef u32 NA_SE;
"""

struct_main = [
    [0x4C, "struct", "sc_task", [
        (0x00, table.sym_var("task",    "OSTask")),
        (0x40, table.sym_var("mq",      "OSMesgQueue *")),
        (0x44, table.sym_var("msg",     "OSMesg")),
        (0x48, table.sym_var("state",   "s32")),
    ]],
    [0x08, "struct", "sc_client", [
        (0x00, table.sym_var("mq",  "OSMesgQueue *")),
        (0x04, table.sym_var("msg", "OSMesg")),
    ]],
]

struct_app = [
    [0xC84C, "struct", "video", [
        (0x0000, table.sym_var("gfx",       "Gfx", "[GFX_LEN]")),
        (0xC800, table.sym_var("task",      "SC_TASK")),
    ]],
    [0x1C, "struct", "controller", [
        (0x00, table.sym_var("stick_x",     "s16")),
        (0x02, table.sym_var("stick_y",     "s16")),
        (0x04, table.sym_var("x",           "f32")),
        (0x08, table.sym_var("y",           "f32")),
        (0x0C, table.sym_var("d",           "f32")),
        (0x10, table.sym_var("held",        "u16")),
        (0x12, table.sym_var("down",        "u16")),
        (0x14, table.sym_var("status",      "OSContStatus *")),
        (0x18, table.sym_var("pad",         "OSContPad *")),
    ]],
    [0x04, "struct", "demo", [
        (0x00, table.sym_var("count",   "u8")),
        (0x01, table.sym_var("stick_x", "s8")),
        (0x02, table.sym_var("stick_y", "s8")),
        (0x03, table.sym_var("button",  "u8")),
    ]],
]

struct_audio = [
]

struct_game = [
    [0x10, "struct", "staff", [
        (0x00, table.sym_var("stage",   "u8")),
        (0x01, table.sym_var("scene",   "u8")),
        (0x02, table.sym_var("flag",    "u8")),
        (0x03, table.sym_var("ry",      "u8")),
        (0x04, table.sym_var("pos",     "VECS")),
        (0x0C, table.sym_var("str",     "const char **")),
    ]],
    [0x08, "struct", "struct_8033B248", [
        (0x00, table.sym_var("_00", "u8")),
        (0x01, table.sym_var("_01", "u8")),
        (0x02, table.sym_var("_02", "u8")),
        (0x03, table.sym_var("_03", "u8")),
        (0x04, table.sym_var("_04", "u32")),
    ]],
]

struct_pl_collision = [
    [0x08, "struct", "pl_collision", [
        (0x00, table.sym_var("type", "u32")),
        (0x04, table.sym_var_fnc("callback", val="int", arg=(
            "struct player *pl",
            "u32 flag",
            "struct object *obj",
        ))),
    ]],
]

struct_player = [
    [0xC8, "struct", "player", [
        (0x00, table.sym_var("index",       "u16")),
        (0x02, table.sym_var("event",       "u16")),
        (0x04, table.sym_var("flag",        "u32")),
        (0x08, table.sym_var("particle",    "u32")),
        (0x0C, table.sym_var("state",       "u32")),
        (0x10, table.sym_var("state_prev",  "u32")),
        (0x14, table.sym_var("ground_se",   "u32")),
        (0x18, table.sym_var("mode",        "s16")),
        (0x1A, table.sym_var("timer",       "u16")),
        (0x1C, table.sym_var("arg",         "u32")),
        (0x20, table.sym_var("stick_d",     "f32")),
        (0x24, table.sym_var("stick_ry",    "s16")),
        (0x26, table.sym_var("invincible",  "s16")),
        (0x28, table.sym_var("timer_a",         "u8")),
        (0x29, table.sym_var("timer_b",         "u8")),
        (0x2A, table.sym_var("timer_wall",      "u8")),
        (0x2B, table.sym_var("timer_ground",    "u8")),
        (0x2C, table.sym_var("rot",         "VECS")),
        (0x32, table.sym_var("rot_vel",     "VECS")),
        (0x38, table.sym_var("slide_ry",    "s16")),
        (0x3A, table.sym_var("twirl_ry",    "s16")),
        (0x3C, table.sym_var("pos",         "VECF")),
        (0x48, table.sym_var("vel",         "VECF")),
        (0x54, table.sym_var("vel_f",       "f32")),
        (0x58, table.sym_var("vel_h",       "f32", "[2]")),
        (0x60, table.sym_var("wall",        "struct map_plane *")),
        (0x64, table.sym_var("roof",        "struct map_plane *")),
        (0x68, table.sym_var("ground",      "struct map_plane *")),
        (0x6C, table.sym_var("roof_y",      "f32")),
        (0x70, table.sym_var("ground_y",    "f32")),
        (0x74, table.sym_var("ground_ry",   "s16")),
        (0x76, table.sym_var("water",       "s16")),
        (0x78, table.sym_var("obj_col",     "struct object *")),
        (0x7C, table.sym_var("obj_hold",    "struct object *")),
        (0x80, table.sym_var("obj_use",     "struct object *")),
        (0x84, table.sym_var("obj_ride",    "struct object *")),
        (0x88, table.sym_var("obj",         "struct object *")),
        (0x8C, table.sym_var("spawn",       "struct spawn *")),
        (0x90, table.sym_var("scene",       "struct scene *")),
        (0x94, table.sym_var("camera",      "struct pl_camera *")),
        (0x98, table.sym_var("shape",       "struct pl_shape *")),
        (0x9C, table.sym_var("cont",        "struct controller *")),
        (0xA0, table.sym_var("file_anime",  "struct file *")),
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
        (0xBC, table.sym_var("peak",        "f32")),
        (0xC0, table.sym_var("sink",        "f32")),
        (0xC4, table.sym_var("gravity",     "f32")),
    ]],
]

struct_pl_physics = [
]

struct_pl_demo = [
]

struct_pl_hang = [
]

struct_pl_wait = [
]

struct_pl_walk = [
    [0x18, "struct", "pl_walk", [
        (0x00, table.sym_var("time",            "s16")),
        (0x02, table.sym_var("timer_ground",    "s16")),
        (0x04, table.sym_var("state_slip",      "u32")),
        (0x08, table.sym_var("state_next",      "u32")),
        (0x0C, table.sym_var("state_jump",      "u32")),
        (0x10, table.sym_var("state_fall",      "u32")),
        (0x14, table.sym_var("state_slide",     "u32")),
    ]],
]

struct_pl_jump = [
]

struct_pl_swim = [
]

struct_pl_grab = [
]

struct_pl_callback = [
    [0x28, "struct", "pl_shape", [
        (0x00, table.sym_var("state",   "u32")),
        (0x04, table.sym_var("head",    "s8")),
        (0x05, table.sym_var("eye",     "s8")),
        (0x06, table.sym_var("glove",   "s8")),
        (0x07, table.sym_var("wing",    "s8")),
        (0x08, table.sym_var("cap",     "s16")),
        (0x0A, table.sym_var("hold",    "s8")),
        (0x0B, table.sym_var("punch",   "u8")),
        (0x0C, table.sym_var("torso",   "VECS")),
        (0x12, table.sym_var("neck",    "VECS")),
        (0x18, table.sym_var("hand",    "VECF")),
        (0x24, table.sym_var("obj",     "struct object *")),
    ]],
]

struct_memory = [
    [0x10, "struct", "mem_block", [
        (0x00, table.sym_var("prev",    "struct mem_block *")),
        (0x04, table.sym_var("next",    "struct mem_block *")),
        (0x08, table.sym_var("pad",     "u64")),
    ]],
    [0x10, "struct", "mem_frame", [
        (0x00, table.sym_var("size",    "size_t")),
        (0x04, table.sym_var("blockl",  "MEM_BLOCK *")),
        (0x08, table.sym_var("blockr",  "MEM_BLOCK *")),
        (0x0C, table.sym_var("frame",   "struct mem_frame *")),
    ]],
    [0x10, "struct", "arena", [
        (0x00, table.sym_var("size",    "long")),
        (0x04, table.sym_var("used",    "long")),
        (0x08, table.sym_var("start",   "char *")),
        (0x0C, table.sym_var("free",    "char *")),
    ]],
    [0x08, "struct", "heap_block", [
        (0x00, table.sym_var("next",    "struct heap_block *")),
        (0x04, table.sym_var("size",    "size_t")),
    ]],
    [0x10, "struct", "heap", [
        (0x00, table.sym_var("size",    "size_t")),
        (0x04, table.sym_var("block",   "HEAP_BLOCK *")),
        (0x08, table.sym_var("free",    "HEAP_BLOCK *")),
        (0x0C, table.sym_var("pad",     "u32")),
    ]],
    [0x08, "struct", "file_table", [
        (0x00, table.sym_var("len", "uint")),
        (0x04, table.sym_var("src", "const char *")),
        [0x08, "struct", "table", [
            (0x00, table.sym_var("start",   "uint")),
            (0x04, table.sym_var("size",    "uint")),
        ], "[1]"],
    ]],
    [0x0C, "struct", "file", [
        (0x00, table.sym_var("table",   "FILE_TABLE *")),
        (0x04, table.sym_var("src",     "const char *")),
        (0x08, table.sym_var("buf",     "char *")),
    ]],
]

struct_save = [
    [0x04, "struct", "save_check", [
        (0x00, table.sym_var("key", "u16")),
        (0x02, table.sym_var("sum", "u16")),
    ]],
    [0x20, "struct", "save_data", [
        (0x00, table.sym_var("time",    "u32",  "[4]")),
        (0x10, table.sym_var("output",  "u16")),
        (0x12, table.sym_var("pad",     "char", "[10]")),
        (0x1C, table.sym_var("check",   "SAVE_CHECK")),
    ]],
    [0x38, "struct", "save_file", [
        (0x00, table.sym_var("stage",   "u8")),
        (0x01, table.sym_var("scene",   "u8")),
        (0x02, table.sym_var("pos",     "VECS")),
        (0x08, table.sym_var("flag",    "u32")),
        (0x0C, table.sym_var("star",    "u8",   "[25]")),
        (0x25, table.sym_var("coin",    "u8",   "[15]")),
        (0x34, table.sym_var("check",   "SAVE_CHECK")),
    ]],
    [0x200, "struct", "save", [
        (0x000, table.sym_var("file",   "SAVE_FILE",    "[4][2]")),
        (0x1C0, table.sym_var("data",   "SAVE_DATA",    "[2]")),
    ]],
]

struct_scene = [
    [0x20, "struct", "spawn", [
        (0x00, table.sym_var("pos",     "VECS")),
        (0x06, table.sym_var("rot",     "VECS")),
        (0x0C, table.sym_var("scene",   "s8")),
        (0x0D, table.sym_var("group",   "s8")),
        (0x10, table.sym_var("arg",     "u32")),
        (0x14, table.sym_var("script",  "const O_SCRIPT *")),
        (0x18, table.sym_var("shape",   "struct shape *")),
        (0x1C, table.sym_var("next",    "struct spawn *")),
    ]],
    [0x0C, "struct", "link", [
        (0x00, table.sym_var("index",   "u8")),
        (0x01, table.sym_var("stage",   "u8")),
        (0x02, table.sym_var("scene",   "u8")),
        (0x03, table.sym_var("link",    "u8")),
        (0x04, table.sym_var("obj",     "struct object *")),
        (0x08, table.sym_var("next",    "struct link *")),
    ]],
    [0x3A, "struct", "scene", [
        (0x00, table.sym_var("index",       "s8")),
        (0x01, table.sym_var("flag",        "s8")),
        (0x02, table.sym_var("env",         "u16")),
        (0x04, table.sym_var("s",           "SHAPE_SCENE *")),
        (0x08, table.sym_var("map",         "const MAP_DATA *")),
        (0x0C, table.sym_var("area",        "const AREA_DATA *")),
        (0x10, table.sym_var("obj",         "OBJ_DATA *")),
        (0x14, table.sym_var("link",        "struct link *")),
        (0x18, table.sym_var("linkbg",      "void *")),
        (0x1C, table.sym_var("connect",     "void *")),
        (0x20, table.sym_var("spawn",       "struct spawn *")),
        (0x24, table.sym_var("cam",         "struct camera *")),
        (0x28, table.sym_var("wind",        "void *")),
        (0x2C, table.sym_var("jet",         "void *", "[2]")),
        (0x34, table.sym_var("msg",         "u8", "[2]")),
        (0x36, table.sym_var("bgm_mode",    "u16")),
        (0x38, table.sym_var("bgm",         "u16")),
    ]],
]

struct_draw = [
]

struct_time = [
    [0xC8, "struct", "time", [
        (0x00, table.sym_var("audcpu_i", "s16")),
        (0x02, table.sym_var("audrcp_i", "s16")),
        (0x08, table.sym_var("gfxcpu", "OSTime", "[TIME_GFXCPU_MAX]")),
        (0x30, table.sym_var("gfxrcp", "OSTime", "[TIME_GFXRCP_MAX]")),
        (0x48, table.sym_var("audcpu", "OSTime", "[TIME_AUDCPU_MAX]")),
        (0x88, table.sym_var("audrcp", "OSTime", "[TIME_AUDRCP_MAX]")),
    ]],
]

struct_slidec = [
]

struct_camera = [
    [0x01, "struct", "camera", [
        (0x00, table.sym_var("mode",    "u8")),
        # ...
    ]],
    [0x18, "struct", "campos", [
        (0x00, table.sym_var("code",    "s16")),
        (0x04, table.sym_var("pos",     "VECF")),
        (0x10, table.sym_var("_10",     "f32")),
        (0x14, table.sym_var("dist",    "f32")),
    ]],
    [0x16, "struct", "camctl", [
        (0x00, table.sym_var("scene",   "s8")),
        (0x04, table.sym_var_fnc("callback", arg=(
            "struct camera *cam",
        ))),
        (0x08, table.sym_var("pos",     "VECS")),
        (0x0E, table.sym_var("size",    "VECS")),
        (0x14, table.sym_var("ry",      "s16")),
    ]],
    [0x08, "struct", "campath", [
        (0x00, table.sym_var("code",    "s8")),
        (0x01, table.sym_var("time",    "u8")),
        (0x02, table.sym_var("pos",     "VECS")),
    ]],
    [0x06, "struct", "camdemo", [
        (0x00, table.sym_var_fnc("callback", arg=(
            "struct camera *cam",
        ))),
        (0x04, table.sym_var("time",    "s16")),
    ]],
]

struct_course = [
]

struct_object = [
    [0x68, "struct", "obj_list", [
        (0x000, table.sym_var("s",      "SHAPE_OBJECT")),
        (0x060, table.sym_var("next",   "struct obj_list *")),
        (0x064, table.sym_var("prev",   "struct obj_list *")),
    ]],
    [0x260, "struct", "object", [
        (0x000, table.sym_var("list",   "OBJ_LIST")),
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
        (0x1F4, table.sym_var("_1F4",       "s16")),
        (0x1F6, table.sym_var("_1F6",       "s16")),
        (0x1F8, table.sym_var("col_hit_r",  "f32")),
        (0x1FC, table.sym_var("col_hit_h",  "f32")),
        (0x200, table.sym_var("col_dmg_r",  "f32")),
        (0x204, table.sym_var("col_dmg_h",  "f32")),
        (0x208, table.sym_var("col_offset", "f32")),
        (0x20C, table.sym_var("script",     "const O_SCRIPT *")),
        (0x210, table.sym_var("_210",       "struct object *")),
        (0x214, table.sym_var("obj_ground", "struct object *")),
        (0x218, table.sym_var("_218",       "s16 *")),
        (0x21C, table.sym_var("mf",         "MTXF")),
        (0x25C, table.sym_var("_25C",       "void *")),
    ]],
    [0x10, "struct", "pl_pcl", [
        (0x00, table.sym_var("code",    "u32")),
        (0x04, table.sym_var("flag",    "u32")),
        (0x08, table.sym_var("shape",   "u8")),
        (0x0C, table.sym_var("script",  "const O_SCRIPT *")),
    ]],
    [0x06, "struct", "struct_8033D274", [
        (0x00, table.sym_var("ground",  "s16")),
        (0x02, table.sym_var("roof",    "s16")),
        (0x04, table.sym_var("wall",    "s16")),
    ]],
]

struct_obj_lib = [
    [0x24, "struct", "obj_splash", [
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
    [0x14, "struct", "obj_pcl", [
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
    [0x10, "struct", "obj_col", [
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
    [0x0C, "struct", "object_a_0", [
        (0x00, table.sym_var("_00", "s16")),
        (0x04, table.sym_var("_04", "f32")),
        (0x08, table.sym_var("_08", "f32")),
    ]],
    [0x0A, "struct", "object_a_1", [
        (0x00, table.sym_var("flag",    "s16")),
        (0x02, table.sym_var("scale",   "s16")),
        (0x04, table.sym_var("map",     "const MAP_DATA *")),
        (0x08, table.sym_var("dist",    "s16")),
    ]],
    [0x0C, "struct", "object_a_2", [
        (0x00, table.sym_var("count",   "s16")),
        (0x02, table.sym_var("add",     "s16")),
        (0x04, table.sym_var("mul",     "s16")),
        (0x06, table.sym_var("shape",   "s16")),
        (0x08, table.sym_var("map",     "const MAP_DATA *")),
    ]],
    [0x0A, "struct", "object_a_3", [
        (0x00, table.sym_var("map", "const MAP_DATA *")),
        (0x04, table.sym_var("px",  "s16")),
        (0x06, table.sym_var("pz",  "s16")),
        (0x08, table.sym_var("ry",  "s16")),
    ]],
    [0x14, "struct", "object_a_4", [
        (0x00, table.sym_var("offset",  "s32")),
        (0x04, table.sym_var("scale",   "VECF")),
        (0x10, table.sym_var("vel",     "f32")),
    ]],
    [0x08, "struct", "object_a_5", [
        (0x00, table.sym_var("shape",   "u8")),
        (0x01, table.sym_var("px",      "s8")),
        (0x02, table.sym_var("pz",      "s8")),
        (0x03, table.sym_var("state",   "s8")),
        (0x04, table.sym_var("data",    "const s8 *")),
    ]],
    [0x08, "struct", "object_a_6", [
        (0x00, table.sym_var("index",   "u8")),
        (0x01, table.sym_var("flag",    "u8")),
        (0x02, table.sym_var("arg",     "u8")),
        (0x03, table.sym_var("shape",   "u8")),
        (0x04, table.sym_var("script",  "const O_SCRIPT *")),
    ]],
    [0x08, "struct", "object_a_7", [
        (0x00, table.sym_var("offset",  "s16")),
        (0x02, table.sym_var("shape",   "s16")),
        (0x04, table.sym_var("map",     "const MAP_DATA *")),
    ]],
    [0x10, "struct", "object_a_8", [
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
    [0x08, "struct", "obj_sfx", [
        (0x00, table.sym_var("flag",    "s16")),
        (0x02, table.sym_var("l",       "s8")),
        (0x03, table.sym_var("r",       "s8")),
        (0x04, table.sym_var("se",      "NA_SE")),
    ]],
]

struct_obj_debug = [
    [0x0C, "struct", "obj_debug", [
        (0x00, table.sym_var("flag",    "s16")),
        (0x02, table.sym_var("x",       "s16")),
        (0x04, table.sym_var("y",       "s16")),
        (0x06, table.sym_var("min",     "s16")),
        (0x08, table.sym_var("max",     "s16")),
        (0x0A, table.sym_var("height",  "s16")),
    ]],
]

struct_wipe = [
    [0x03, "struct", "wipe_arg_fade", [
        (0x00, table.sym_var("r",       "u8")),
        (0x01, table.sym_var("g",       "u8")),
        (0x02, table.sym_var("b",       "u8")),
    ]],
    [0x12, "struct", "wipe_arg_window", [
        (0x00, table.sym_var("r",       "u8")),
        (0x01, table.sym_var("g",       "u8")),
        (0x02, table.sym_var("b",       "u8")),
        (0x04, table.sym_var("s_size",  "s16")),
        (0x06, table.sym_var("e_size",  "s16")),
        (0x08, table.sym_var("s_x",     "s16")),
        (0x0A, table.sym_var("s_y",     "s16")),
        (0x0C, table.sym_var("e_x",     "s16")),
        (0x0E, table.sym_var("e_y",     "s16")),
        (0x10, table.sym_var("rot_vel", "s16")),
    ]],
    [0x04, "union", "wipe_arg", [
        (0x00, table.sym_var("fade",    "WIPE_ARG_FADE")),
        (0x00, table.sym_var("window",  "WIPE_ARG_WINDOW")),
    ]],
    [0x16, "struct", "wipe", [
        (0x00, table.sym_var("active",  "u8")),
        (0x01, table.sym_var("type",    "u8")),
        (0x02, table.sym_var("frame",   "u8")),
        (0x03, table.sym_var("blank",   "u8")),
        (0x04, table.sym_var("arg",     "WIPE_ARG")),
    ]],
]

struct_shadow = [
    [0x09, "struct", "shadow_rect", [
        (0x00, table.sym_var("sx",      "f32")),
        (0x04, table.sym_var("sz",      "f32")),
        (0x08, table.sym_var("y_scale", "s8")),
    ]],
]

struct_background = [
    [0x10, "struct", "struct_803612C0", [
        (0x00, table.sym_var("_00", "u16")),
        (0x02, table.sym_var("_02", "s16")),
        (0x04, table.sym_var("_04", "s32")),
        (0x08, table.sym_var("_08", "s32")),
        (0x0C, table.sym_var("_0C", "s32")),
    ]],
]

struct_scroll = [
    [0x24, "struct", "scroll", [
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
    [0x78, "struct", "ripple", [
        (0x00, table.sym_var("_00", "s16")),
        (0x02, table.sym_var("_02", "s8")),
        (0x03, table.sym_var("_03", "s8")),
        (0x04, table.sym_var("_04", "s8")),
        (0x05, table.sym_var("_05", "s8")),
        (0x06, table.sym_var("_06", "s8")),
        (0x07, table.sym_var("_07", "s8")),
        # ...
    ]],
]

struct_dprint = [
    [0x3C, "struct", "dprint", [
        (0x00, table.sym_var("x",   "s32")),
        (0x04, table.sym_var("y",   "s32")),
        (0x08, table.sym_var("len", "s16")),
        (0x0A, table.sym_var("str", "char", "[50]")),
    ]],
]

struct_message = [
    [0x10, "struct", "msg", [
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
    [0x08, "struct", "prg_obj", [
        (0x00, table.sym_var("script",  "const O_SCRIPT *")),
        (0x04, table.sym_var("shape",   "s16")),
        (0x06, table.sym_var("arg",     "s16")),
    ]],
    [0x08, "struct", "map_obj", [
        (0x00, table.sym_var("index",   "u8")),
        (0x01, table.sym_var("ext",     "u8")),
        (0x02, table.sym_var("code",    "u8")),
        (0x03, table.sym_var("shape",   "u8")),
        (0x04, table.sym_var("script",  "const O_SCRIPT *")),
    ]],
]

struct_hud = [
    [0x0E, "struct", "hud", [
        (0x00, table.sym_var("life",    "s16")),
        (0x02, table.sym_var("coin",    "s16")),
        (0x04, table.sym_var("star",    "s16")),
        (0x06, table.sym_var("power",   "s16")),
        (0x08, table.sym_var("key",     "s16")),
        (0x0A, table.sym_var("flag",    "s16")),
        (0x0C, table.sym_var("timer",   "u16")),
    ]],
    [0x0C, "struct", "meter", [
        (0x00, table.sym_var("mode",    "s8")),
        (0x02, table.sym_var("x",       "s16")),
        (0x04, table.sym_var("y",       "s16")),
        (0x08, table.sym_var("scale",   "f32")),
    ]],
]

struct_object_b = [
]

struct_object_c = [
    [0x0E, "struct", "object_c_0", [
        (0x00, table.sym_var("msg_start",   "s16")),
        (0x02, table.sym_var("msg_win",     "s16")),
        (0x04, table.sym_var("path",        "const PATH_DATA *")),
        (0x08, table.sym_var("star",        "VECS")),
    ]],
    [0x0B, "struct", "object_c_1", [
        (0x00, table.sym_var("scale",   "f32")),
        (0x04, table.sym_var("se",      "NA_SE")),
        (0x08, table.sym_var("dist",    "s16")),
        (0x0A, table.sym_var("damage",  "s8")),
    ]],
    [0x0A, "struct", "object_c_2", [
        (0x00, table.sym_var("map",     "const MAP_DATA *")),
        (0x04, table.sym_var("p_map",   "const MAP_DATA *")),
        (0x08, table.sym_var("p_shape", "s16")),
    ]],
    [0x06, "struct", "object_c_3", [
        (0x00, table.sym_var("map",     "const MAP_DATA *")),
        (0x04, table.sym_var("shape",   "s16")),
    ]],
    [0x0C, "struct", "object_c_4", [
        (0x00, table.sym_var("msg",     "s16")),
        (0x04, table.sym_var("radius",  "f32")),
        (0x08, table.sym_var("height",  "f32")),
    ]],
    [0x0C, "struct", "object_c_5", [
        (0x00, table.sym_var("shape",   "int")),
        (0x04, table.sym_var("script",  "const O_SCRIPT *")),
        (0x08, table.sym_var("scale",   "float")),
    ]],
]

struct_math = [
    [0x08, "struct", "bspline", [
        (0x00, table.sym_var("time",    "s16")),
        (0x02, table.sym_var("pos",     "VECS")),
    ]],
]

struct_shape = [
    [0x18, "struct", "anime", [
        (0x00, table.sym_var("flag",    "s16")),
        (0x02, table.sym_var("waist",   "s16")),
        (0x04, table.sym_var("start",   "s16")),
        (0x06, table.sym_var("end",     "s16")),
        (0x08, table.sym_var("frame",   "s16")),
        (0x0A, table.sym_var("joint",   "s16")),
        (0x0C, table.sym_var("val",     "s16 *")),
        (0x10, table.sym_var("tbl",     "u16 *")),
        (0x14, table.sym_var("size",    "size_t")),
    ]],
    [0x14, "struct", "skeleton", [
        (0x00, table.sym_var("index",       "s16")),
        (0x02, table.sym_var("waist",       "s16")),
        (0x04, table.sym_var("anime",       "ANIME *")),
        (0x08, table.sym_var("frame",       "s16")),
        (0x0A, table.sym_var("timer",       "u16")),
        (0x0C, table.sym_var("frame_amt",   "s32")),
        (0x10, table.sym_var("frame_vel",   "s32")),
    ]],
    [0x0C, "struct", "layer_list", [
        (0x00, table.sym_var("mtx",     "Mtx *")),
        (0x04, table.sym_var("gfx",     "const Gfx *")),
        (0x08, table.sym_var("next",    "struct layer_list *")),
    ]],
    [0x14, "struct", "shape", [
        (0x00, table.sym_var("type",    "s16")),
        (0x02, table.sym_var("flag",    "s16")),
        (0x04, table.sym_var("prev",    "struct shape *")),
        (0x08, table.sym_var("next",    "struct shape *")),
        (0x0C, table.sym_var("parent",  "struct shape *")),
        (0x10, table.sym_var("child",   "struct shape *")),
    ]],
    [0x1C, "struct", "shape_callback", [
        (0x00, table.sym_var("s",   "SHAPE")),
        (0x14, table.sym_var_fnc("callback", val="void *", arg=(
            "int code",
            "SHAPE *shape",
            "void *data",
        ))),
        (0x18, table.sym_var("arg", "int")),
    ]],
    [0x18, "struct", "shape_gfx", [
        (0x00, table.sym_var("s",   "SHAPE")),
        (0x14, table.sym_var("gfx", "const Gfx *")),
    ]],
    [0x24, "struct", "shape_scene", [
        (0x00, table.sym_var("s",       "SHAPE")),
        (0x14, table.sym_var("index",   "u8")),
        (0x15, table.sym_var("_15",     "u8")),
        (0x16, table.sym_var("x",       "s16")),
        (0x18, table.sym_var("y",       "s16")),
        (0x1A, table.sym_var("w",       "s16")),
        (0x1C, table.sym_var("h",       "s16")),
        (0x1E, table.sym_var("len",     "u16")),
        (0x20, table.sym_var("table",   "SHAPE *")),
    ]],
    [0x18, "struct", "shape_ortho", [
        (0x00, table.sym_var("s",       "SHAPE")),
        (0x14, table.sym_var("scale",   "f32")),
    ]],
    [0x24, "struct", "shape_persp", [
        (0x00, table.sym_var("s",       "SHAPE_CALLBACK")),
        (0x1C, table.sym_var("fovy",    "f32")),
        (0x20, table.sym_var("near",    "s16")),
        (0x22, table.sym_var("far",     "s16")),
    ]],
    [0x54, "struct", "shape_layer", [
        (0x00, table.sym_var("s",       "SHAPE")),
        (0x14, table.sym_var("list",    "LAYER_LIST *", "[S_LAYER_MAX]")),
        (0x34, table.sym_var("next",    "LAYER_LIST *", "[S_LAYER_MAX]")),
    ]],
    [0x3C, "struct", "shape_camera", [
        (0x00, table.sym_var("s",       "SHAPE_CALLBACK")),
        (0x1C, table.sym_var("eye",     "VECF")),
        (0x28, table.sym_var("look",    "VECF")),
        (0x34, table.sym_var("mf",      "MTXF *")),
        (0x38, table.sym_var("rz_m",    "s16")),
        (0x3A, table.sym_var("rz_p",    "s16")),
    ]],
    [0x18, "struct", "shape_lod", [
        (0x00, table.sym_var("s",   "SHAPE")),
        (0x14, table.sym_var("min", "s16")),
        (0x16, table.sym_var("max", "s16")),
    ]],
    [0x20, "struct", "shape_select", [
        (0x00, table.sym_var("s",       "SHAPE_CALLBACK")),
        (0x1C, table.sym_var("arg",     "s16")),
        (0x1E, table.sym_var("index",   "s16")),
    ]],
    [0x24, "struct", "shape_posrot", [
        (0x00, table.sym_var("s",   "SHAPE_GFX")),
        (0x18, table.sym_var("pos", "VECS")),
        (0x1E, table.sym_var("rot", "VECS")),
    ]],
    [0x1E, "struct", "shape_pos", [
        (0x00, table.sym_var("s",   "SHAPE_GFX")),
        (0x18, table.sym_var("pos", "VECS")),
    ]],
    [0x1E, "struct", "shape_rot", [
        (0x00, table.sym_var("s",   "SHAPE_GFX")),
        (0x18, table.sym_var("rot", "VECS")),
    ]],
    [0x1C, "struct", "shape_scale", [
        (0x00, table.sym_var("s",       "SHAPE_GFX")),
        (0x18, table.sym_var("scale",   "f32")),
    ]],
    [0x1E, "struct", "shape_billboard", [
        (0x00, table.sym_var("s",   "SHAPE_GFX")),
        (0x18, table.sym_var("pos", "VECS")),
    ]],
    [0x1E, "struct", "shape_joint", [
        (0x00, table.sym_var("s",   "SHAPE_GFX")),
        (0x18, table.sym_var("pos", "VECS")),
    ]],
    [0x18, "struct", "shape_shadow", [
        (0x00, table.sym_var("s",       "SHAPE")),
        (0x14, table.sym_var("size",    "s16")),
        (0x16, table.sym_var("alpha",   "u8")),
        (0x17, table.sym_var("type",    "u8")),
    ]],
    [0x20, "struct", "shape_background", [
        (0x00, table.sym_var("s",       "SHAPE_CALLBACK")),
        (0x1C, table.sym_var("arg",     "u32")),
    ]],
    [0x60, "struct", "shape_object", [
        (0x00, table.sym_var("s",           "SHAPE")),
        (0x14, table.sym_var("shape",       "SHAPE *")),
        (0x18, table.sym_var("scene",       "s8")),
        (0x19, table.sym_var("group",       "s8")),
        (0x1A, table.sym_var("rot",         "VECS")),
        (0x20, table.sym_var("pos",         "VECF")),
        (0x2C, table.sym_var("scale",       "VECF")),
        (0x38, table.sym_var("skeleton",    "SKELETON")),
        (0x4C, table.sym_var("spawn",       "struct spawn *")),
        (0x50, table.sym_var("mf",          "MTXF *")),
        (0x54, table.sym_var("view",        "VECF")),
    ]],
    [0x18, "struct", "shape_list", [
        (0x00, table.sym_var("s",       "SHAPE")),
        (0x14, table.sym_var("shape",   "SHAPE *")),
    ]],
    [0x26, "struct", "shape_hand", [
        (0x00, table.sym_var("s",       "SHAPE_CALLBACK")),
        (0x1C, table.sym_var("object",  "SHAPE_OBJECT *")),
        (0x20, table.sym_var("pos",     "VECS")),
    ]],
    [0x16, "struct", "shape_cull", [
        (0x00, table.sym_var("s",       "SHAPE")),
        (0x14, table.sym_var("dist",    "s16")),
    ]],
]

struct_s_script = [
]

struct_p_script = [
]

struct_map = [
    [0x30, "struct", "map_plane", [
        (0x00, table.sym_var("type",    "s16")),
        (0x02, table.sym_var("arg",     "s16")),
        (0x04, table.sym_var("flag",    "s8")),
        (0x05, table.sym_var("area",    "s8")),
        (0x06, table.sym_var("y_min",   "s16")),
        (0x08, table.sym_var("y_max",   "s16")),
        (0x0A, table.sym_var("v0",      "VECS")),
        (0x10, table.sym_var("v1",      "VECS")),
        (0x16, table.sym_var("v2",      "VECS")),
        (0x1C, table.sym_var("nx",      "f32")),
        (0x20, table.sym_var("ny",      "f32")),
        (0x24, table.sym_var("nz",      "f32")),
        (0x28, table.sym_var("nw",      "f32")),
        (0x2C, table.sym_var("obj",     "struct object *")),
    ]],
    [0x08, "struct", "map_list", [
        (0x00, table.sym_var("next",    "struct map_list *")),
        (0x04, table.sym_var("plane",   "MAP_PLANE *")),
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
    [0x0C, "struct", "bgmctl", [
        (0x00, table.sym_var("a_voice", "s16")),
        (0x02, table.sym_var("a_vol",   "s16")),
        (0x04, table.sym_var("a_time",  "s16")),
        (0x06, table.sym_var("b_voice", "s16")),
        (0x08, table.sym_var("b_vol",   "s16")),
        (0x0A, table.sym_var("b_time",  "s16")),
    ]],
]

struct_audio_data = [
    [0x1C, "struct", "Na_cfg", [
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
