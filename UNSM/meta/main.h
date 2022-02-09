#include <sm64/segment.h>

#define DATA1(segment, name, fn)    \
    SECTION(SEGMENT_DATA_##segment, name##_data,    \
        ,                                           \
        DATA(BUILD/data/fn.o)                       \
        ,                                           \
    )
#define DATA2(segment, name, fn)                    \
    SECTION(SEGMENT_DATA_##segment, name##_data,    \
        ,                                           \
        DATA(BUILD/data/fn/program.o)               \
        DATA(BUILD/data/fn/shape.o)                 \
        ,                                           \
    )
#define SZP(name, fn)               \
    SECTION(0, name##_szp,          \
        ,                           \
        DATA(BUILD/data/fn.szp.o)   \
        ,                           \
    )
#define FILE(name, fn)              \
    SECTION(0, name,                \
        ,                           \
        DATA(BUILD/data/fn.o)       \
        ,                           \
    )

#define SHAPE(segment, name)                \
    SZP(shape_##name, shape/name/gfx)       \
    DATA1(segment, shape_##name, shape/name/shape)
#define BACKGROUND(name)                    \
    SZP(background_##name, background/name)
#define TEXTURE(name)                       \
    SZP(texture_##name, texture/name)
#define STAGE(name)                         \
    SZP(stage_##name, stage/name/gfx)       \
    DATA2(STAGE, stage_##name, stage/name)

SECTION(SEGMENT_ZIMG, zimg,
    ,
    ,
    BSS(BUILD/src/zimg.o)
)
ASSERT(. <= SEGMENT_MEM_START, "error: ZIMG exceeds memory size.")
SECTION(SEGMENT_BUFFER, buffer,
    ,
    ,
    BSS(BUILD/src/timg.o)
    BSS(BUILD/src/audio/heap.o)
    BSS(BUILD/src/buffer.o)
    BSS(BUILD/src/audio/bss.o)
)
ASSERT(. <= SEGMENT_FIFO, "error: BUFFER exceeds memory size.")
SECTION(SEGMENT_FIFO, fifo,
    ,
    ,
    BSS(BUILD/src/fifo.o)
)
ASSERT(. <= SEGMENT_MAIN, "error: FIFO exceeds memory size.")
SECTION(SEGMENT_MAIN, main,
    TEXT(ULTRA/lib/PR/crt0.o)
    TEXT(BUILD/src/main.ld.o)
    TEXT(ULTRA/lib/PR/rspboot.o)
    TEXT(ULTRA/lib/PR/gspFast3D.fifo.o)
    TEXT(ULTRA/lib/PR/aspMain.o)
    ,
    DATA(BUILD/src/main.ld.o)
    DATA(ULTRA/lib/PR/rspboot.o)
    DATA(ULTRA/lib/PR/gspFast3D.fifo.o)
    DATA(ULTRA/lib/PR/aspMain.o)
    ,
    BSS(BUILD/src/main.ld.o)
    BSS(ULTRA/lib/PR/rspboot.o)
    BSS(ULTRA/lib/PR/gspFast3D.fifo.o)
    BSS(ULTRA/lib/PR/aspMain.o)
)
ASSERT(__dev <= 0x00101000, "error: MAIN exceeds device size.")
ASSERT(. <= SEGMENT_MAIN2, "error: MAIN exceeds memory size.")
SECTION(SEGMENT_MAIN2, main2,
    TEXT(BUILD/src/main2.ld.o)
    ,
    DATA(BUILD/src/main2.ld.o)
    ,
    BSS(BUILD/src/main2.ld.o)
)
ASSERT(. <= SEGMENT_CIMG, "error: MAIN2 exceeds memory size.")
SECTION(SEGMENT_CIMG, cimg,
    ,
    ,
    BSS(BUILD/src/cimg.o)
)
ASSERT(. <= 0x80400000, "error: CIMG exceeds memory size.")
DATA1(MAIN, main, main)
SZP(main, main/gfx)
SHAPE(PLAYER, player)
SHAPE(SHAPE1, 1a)
SHAPE(SHAPE1, 1b)
SHAPE(SHAPE1, 1c)
SHAPE(SHAPE1, 1d)
SHAPE(SHAPE1, 1e)
SHAPE(SHAPE1, 1f)
SHAPE(SHAPE1, 1g)
SHAPE(SHAPE1, 1h)
SHAPE(SHAPE1, 1i)
SHAPE(SHAPE1, 1j)
SHAPE(SHAPE1, 1k)
SHAPE(SHAPE2, 2a)
SHAPE(SHAPE2, 2b)
SHAPE(SHAPE2, 2c)
SHAPE(SHAPE2, 2d)
SHAPE(SHAPE2, 2e)
SHAPE(SHAPE2, 2f)
SHAPE(SHAPE3, 3common)
SHAPE(GLOBAL, global)
SECTION(SEGMENT_DATA_OBJECT, object_data,
    ,
    DATA(BUILD/data/object/object_a.o)
    DATA(BUILD/data/object/player.o)
    DATA(BUILD/data/object/object_b.o)
    DATA(BUILD/data/object/object_c.o)
    DATA(BUILD/data/object/camera.o)
    ,
)
SECTION(SEGMENT_MENU, menu,
    TEXT(BUILD/src/title.o)
    TEXT(BUILD/src/title_bg.o)
    TEXT(BUILD/src/file_select.o)
    TEXT(BUILD/src/star_select.o)
    TEXT(BUILD/src/face.ld.o)
    ,
    DATA(BUILD/src/title.data.o)
    DATA(BUILD/src/title_bg.data.o)
    DATA(BUILD/src/file_select.data.o)
    DATA(BUILD/src/star_select.data.o)
    DATA(BUILD/src/face.ld.o)
    ,
    BSS(BUILD/src/title.data.o)
    BSS(BUILD/src/title_bg.data.o)
    BSS(BUILD/src/file_select.data.o)
    BSS(BUILD/src/star_select.data.o)
    BSS(BUILD/src/face.ld.o)
)
ASSERT(. <= SEGMENT_MEM_END-0x10, "error: MENU exceeds memory size.")
DATA2(MENU, menu_title, menu/title)
SZP(menu_title, menu/title/gfx)
SZP(menu_debug, menu/title/debug)
BACKGROUND(title)
SECTION(SEGMENT_DATA_FACE, face_data,
    ,
    DATA(BUILD/data/face/data.o)
    ,
)
ASSERT(. <= SEGMENT_DATA_FACE+0x70000, "error: DATA_FACE exceeds memory size.")
DATA2(MENU, menu_select, menu/select)
SZP(menu_select, menu/select/gfx)
DATA1(GAME, game, game)
BACKGROUND(a)
BACKGROUND(b)
BACKGROUND(c)
BACKGROUND(d)
BACKGROUND(e)
BACKGROUND(f)
BACKGROUND(g)
BACKGROUND(h)
BACKGROUND(i)
BACKGROUND(j)
TEXTURE(a)
TEXTURE(b)
TEXTURE(c)
TEXTURE(d)
TEXTURE(e)
TEXTURE(f)
TEXTURE(g)
TEXTURE(h)
TEXTURE(i)
TEXTURE(j)
TEXTURE(k)
TEXTURE(l)
SZP(weather, weather/gfx)
STAGE(bbh)
STAGE(ccm)
STAGE(inside)
STAGE(hmc)
STAGE(ssl)
STAGE(bob)
STAGE(sl)
STAGE(wdw)
STAGE(jrb)
STAGE(thi)
STAGE(ttc)
STAGE(rr)
STAGE(grounds)
STAGE(bitdw)
STAGE(vcutm)
STAGE(bitfs)
STAGE(sa)
STAGE(bits)
STAGE(lll)
STAGE(ddd)
STAGE(wf)
STAGE(ending)
STAGE(courtyard)
STAGE(pss)
STAGE(cotmc)
STAGE(totwc)
STAGE(bitdwa)
STAGE(wmotr)
STAGE(bitfsa)
STAGE(bitsa)
STAGE(ttm)
FILE(anime, anime)
FILE(demo,  demo)
FILE(audioctl, audio/ctl)
FILE(audiotbl, audio/tbl)
FILE(audioseq, audio/seq)
FILE(audiobnk, audio/bnk)
