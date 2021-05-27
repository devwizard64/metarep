#ifndef _MAKE_MAIN_H_
#define _MAKE_MAIN_H_

#include <sm64/segment.h>

#define DATA1(segment, name, fn)    \
    SECTION(                        \
        SEGMENT_DATA_##segment,     \
        data_##name,                \
        DATA(BUILD/data/fn.o)       \
    )
#define DATA2(segment, name, fn)    \
    SECTION(                        \
        SEGMENT_DATA_##segment,     \
        data_##name,                \
        DATA(BUILD/data/fn/s.o)     \
        DATA(BUILD/data/fn/g.o)     \
    )
#define SZP(name, fn)               \
    SECTION(                        \
        0, szp_##name,              \
        DATA(BUILD/data/fn.szp.o)   \
    )
#define FILE(name, fn)              \
    SECTION(                        \
        0, file_##name,             \
        DATA(BUILD/data/fn.o)       \
    )
#define GFX(segment, name)                      \
    SZP(gfx_##name, gfx/name/gfx)               \
    DATA1(segment, gfx_##name, gfx/name/g)
#define BACKGROUND(name)                        \
    SZP(background_##name, background/name)
#define TEXTURE(name)                           \
    SZP(texture_##name, texture/name)
#define PARTICLE(name)                          \
    SZP(particle_##name, particle/name)
#define STAGE(name)                             \
    SZP(stage_##name, stage/name/gfx)           \
    DATA2(STAGE, stage_##name, stage/name)

#endif /* _MAKE_MAIN_H_ */

SECTION(
    0xA4000000, header,
    TEXT(BUILD/src/header.o)
    TEXT(ULTRA/lib/PR/ipl3.o)
)
BUFFER(
    SEGMENT_ZIMG, zimg,
    BSS(BUILD/src/buffer/depth.o)
)
BUFFER(
    SEGMENT_BUFFER, buffer,
    BSS(BUILD/src/buffer/texture.o)
    BSS(BUILD/src/audio/heap.o)
    BSS(BUILD/src/buffer/buffer.o)
    BSS(BUILD/src/audio/bss.o)
)
BUFFER(
    SEGMENT_FIFO, fifo,
    BSS(BUILD/src/buffer/fifo.o)
)
CODE(
    SEGMENT_MAIN, main,
    TEXT(ULTRA/lib/PR/crt0.o)
    TEXT(BUILD/src/main.ld.o)
    TEXT(ULTRA/lib/PR/rspboot.o)
    TEXT(ULTRA/lib/PR/gspFast3D.fifo.o)
    TEXT(ULTRA/lib/PR/aspMain.o)
    DATA(BUILD/src/main.ld.o)
    DATA(ULTRA/lib/PR/rspboot.o)
    DATA(ULTRA/lib/PR/gspFast3D.fifo.o)
    DATA(ULTRA/lib/PR/aspMain.o),
    BSS(BUILD/src/main.ld.o)
    BSS(ULTRA/lib/PR/rspboot.o)
    BSS(ULTRA/lib/PR/gspFast3D.fifo.o)
    BSS(ULTRA/lib/PR/aspMain.o)
)
ASSERT(__dev <= 0x00101000, "error: MAIN exceeds device size.")
ASSERT(. <= SEGMENT_MAIN2, "error: MAIN exceeds memory size.")
CODE(
    SEGMENT_MAIN2, main2,
    TEXT(BUILD/src/main2.ld.o)
    DATA(BUILD/src/main2.ld.o),
    BSS(BUILD/src/main2.ld.o)
)
ASSERT(. <= SEGMENT_CIMG, "error: MAIN2 exceeds memory size.")
BUFFER(
    SEGMENT_CIMG, cimg,
    BSS(BUILD/src/buffer/frame.o)
)
DATA1(MAIN, main, main)
SZP(main, main/gfx)
GFX(PLAYER, player)
GFX(GFXA, a0)
GFX(GFXA, a1)
GFX(GFXA, a2)
GFX(GFXA, a3)
GFX(GFXA, a4)
GFX(GFXA, a5)
GFX(GFXA, a6)
GFX(GFXA, a7)
GFX(GFXA, a8)
GFX(GFXA, a9)
GFX(GFXA, a10)
GFX(GFXB, b0)
GFX(GFXB, b1)
GFX(GFXB, b2)
GFX(GFXB, b3)
GFX(GFXB, b4)
GFX(GFXB, b5)
GFX(GFXC, c0)
GFX(ENTITY, entity)
SECTION(
    SEGMENT_DATA_OBJECT, data_object,
    DATA(BUILD/data/object/object_a.o)
    DATA(BUILD/data/object/player.o)
    DATA(BUILD/data/object/object_b.o)
    DATA(BUILD/data/object/object_c.o)
    DATA(BUILD/data/object/camera.o)
)
CODE(
    SEGMENT_MENU, menu,
    TEXT(BUILD/src/title.o)
    TEXT(BUILD/src/title_bg.o)
    TEXT(BUILD/src/file_select.o)
    TEXT(BUILD/src/star_select.o)
    TEXT(BUILD/src/face.ld.o)
    DATA(BUILD/src/title.data.o)
    DATA(BUILD/src/title_bg.data.o)
    DATA(BUILD/src/file_select.data.o)
    DATA(BUILD/src/star_select.data.o)
    DATA(BUILD/src/face.ld.o),
    BSS(BUILD/src/title.data.o)
    BSS(BUILD/src/title_bg.data.o)
    BSS(BUILD/src/file_select.data.o)
    BSS(BUILD/src/star_select.data.o)
    BSS(BUILD/src/face.ld.o)
)
DATA2(MENU, menu_title, menu/title)
SZP(menu_title_a, menu/title/gfx_a)
SZP(menu_title_b, menu/title/gfx_b)
BACKGROUND(title)
SECTION(
    SEGMENT_DATA_FACE, data_face,
    DATA(BUILD/data/face/data.o)
)
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
PARTICLE(a)
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
STAGE(end)
STAGE(courtyard)
STAGE(pss)
STAGE(cotmc)
STAGE(totwc)
STAGE(bitdwa)
STAGE(wmotr)
STAGE(bitfsa)
STAGE(bitsa)
STAGE(ttm)
FILE(motion_player, motion_player)
FILE(demo,          demo)
FILE(audio_ctl,     audio/ctl)
FILE(audio_tbl,     audio/tbl)
FILE(audio_seq,     audio/seq)
FILE(audio_bnk,     audio/bnk)
