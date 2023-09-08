CODE_OBJ := \
	$(BUILD)/src/main.o \
	$(BUILD)/src/graphics.o \
	$(BUILD)/src/audio.o \
	$(BUILD)/src/game.o $(BUILD)/src/game.data.o \
	$(BUILD)/src/collision.o $(BUILD)/src/collision.data.o \
	$(BUILD)/src/player.o $(BUILD)/src/player.data.o \
	$(BUILD)/src/plphysics.o $(BUILD)/src/plphysics.data.o \
	$(BUILD)/src/pldemo.o $(BUILD)/src/pldemo.data.o \
	$(BUILD)/src/plhang.o $(BUILD)/src/plhang.data.o \
	$(BUILD)/src/plwait.o $(BUILD)/src/plwait.data.o \
	$(BUILD)/src/plwalk.o $(BUILD)/src/plwalk.data.o \
	$(BUILD)/src/pljump.o $(BUILD)/src/pljump.data.o \
	$(BUILD)/src/plswim.o $(BUILD)/src/plswim.data.o \
	$(BUILD)/src/plgrab.o $(BUILD)/src/plgrab.data.o \
	$(BUILD)/src/plcallback.o \
	$(BUILD)/src/memory.o \
	$(BUILD)/src/save.o \
	$(BUILD)/src/scene.o \
	$(BUILD)/src/draw.o \
	$(BUILD)/src/time.o \
	$(BUILD)/src/slidec.o \
	$(BUILD)/src/camera.o $(BUILD)/src/camera.data.o \
	$(BUILD)/src/course.o \
	$(BUILD)/src/object.o $(BUILD)/src/object.data.o \
	$(BUILD)/src/objlib.o $(BUILD)/src/objlib.data.o \
	$(BUILD)/src/object_a.o $(BUILD)/src/object_a.data.o \
	$(BUILD)/src/objphysics.o \
	$(BUILD)/src/objcollision.o $(BUILD)/src/objcollision.data.o \
	$(BUILD)/src/objlist.o \
	$(BUILD)/src/objsfx.o \
	$(BUILD)/src/objdebug.o $(BUILD)/src/objdebug.data.o \
	$(BUILD)/src/wipe.o $(BUILD)/src/wipe.data.o \
	$(BUILD)/src/shadow.o $(BUILD)/src/shadow.data.o \
	$(BUILD)/src/back.o $(BUILD)/src/back.data.o \
	$(BUILD)/src/scroll.o $(BUILD)/src/scroll.data.o \
	$(BUILD)/src/objshape.o \
	$(BUILD)/src/wave.o $(BUILD)/src/wave.data.o \
	$(BUILD)/src/dprint.o \
	$(BUILD)/src/message.o $(BUILD)/src/message.data.o \
	$(BUILD)/src/snow.o $(BUILD)/src/snow.data.o \
	$(BUILD)/src/lava.o $(BUILD)/src/lava.data.o \
	$(BUILD)/src/tag.o \
	$(BUILD)/src/hud.o \
	$(BUILD)/src/object_b.o $(BUILD)/src/object_b.data.o \
	$(BUILD)/src/object_c.o $(BUILD)/src/object_c.data.o

ULIB_OBJ := \
	$(BUILD)/src/math.o \
	$(BUILD)/src/mathtbl.o \
	$(BUILD)/src/shape.o \
	$(BUILD)/src/shplang.o \
	$(BUILD)/src/prglang.o \
	$(BUILD)/src/bgcheck.o \
	$(BUILD)/src/bgload.o \
	$(BUILD)/src/objlang.o $(BUILD)/src/objlang.data.o

MENU_OBJ := \
	$(BUILD)/src/title.o \
	$(BUILD)/src/titlebg.o \
	$(BUILD)/src/fileselect.o $(BUILD)/src/fileselect.data.o \
	$(BUILD)/src/starselect.o $(BUILD)/src/starselect.data.o

AUDIO_OBJ := \
	$(BUILD)/src/audio/a.o $(BUILD)/src/audio/a.data.o \
	$(BUILD)/src/audio/b.o $(BUILD)/src/audio/b.data.o \
	$(BUILD)/src/audio/c.o \
	$(BUILD)/src/audio/d.o $(BUILD)/src/audio/d.data.o \
	$(BUILD)/src/audio/e.o $(BUILD)/src/audio/e.data.o \
	$(BUILD)/src/audio/f.o $(BUILD)/src/audio/f.data.o \
	$(BUILD)/src/audio/g.o $(BUILD)/src/audio/g.data.o \
	$(BUILD)/src/audio/data.o

FACE_OBJ := \
	$(BUILD)/src/face/main.o $(BUILD)/src/face/main.data.o \
	$(BUILD)/src/face/mem.o $(BUILD)/src/face/mem.data.o \
	$(BUILD)/src/face/sfx.o \
	$(BUILD)/src/face/draw.o $(BUILD)/src/face/draw.data.o \
	$(BUILD)/src/face/object.o $(BUILD)/src/face/object.data.o \
	$(BUILD)/src/face/skin.o $(BUILD)/src/face/skin.data.o \
	$(BUILD)/src/face/particle.o $(BUILD)/src/face/particle.data.o \
	$(BUILD)/src/face/dynlist.o $(BUILD)/src/face/dynlist.data.o \
	$(BUILD)/src/face/gadget.o $(BUILD)/src/face/gadget.data.o \
	$(BUILD)/src/face/stdio.o $(BUILD)/src/face/stdio.data.o \
	$(BUILD)/src/face/joint.o $(BUILD)/src/face/joint.data.o \
	$(BUILD)/src/face/net.o $(BUILD)/src/face/net.data.o \
	$(BUILD)/src/face/math.o $(BUILD)/src/face/math.data.o \
	$(BUILD)/src/face/shape.o $(BUILD)/src/face/shape.data.o \
	$(BUILD)/src/face/gfx.o $(BUILD)/src/face/gfx.data.o \
	$(BUILD)/src/face/bss.o

IDO_C := \
	$(BUILD)/src/main.o \
	$(BUILD)/src/graphics.o \
	$(BUILD)/src/audio.o \
	$(BUILD)/src/plcallback.o \
	$(BUILD)/src/memory.o \
	$(BUILD)/src/save.o \
	$(BUILD)/src/scene.o \
	$(BUILD)/src/draw.o \
	$(BUILD)/src/time.o \
	$(BUILD)/src/course.o \
	$(BUILD)/src/objphysics.o \
	$(BUILD)/src/objlist.o \
	$(BUILD)/src/objsfx.o \
	$(BUILD)/src/objshape.o \
	$(BUILD)/src/dprint.o \
	$(BUILD)/src/tag.o \
	$(BUILD)/src/hud.o \
	$(BUILD)/src/math.o \
	$(BUILD)/src/shape.o \
	$(BUILD)/src/shplang.o \
	$(BUILD)/src/prglang.o \
	$(BUILD)/src/bgcheck.o \
	$(BUILD)/src/bgload.o \
	$(BUILD)/src/title.o \
	$(BUILD)/src/titlebg.o \
	$(BUILD)/data/cimg.o \
	$(BUILD)/data/zimg.o \
	$(BUILD)/data/timg.o \
	$(BUILD)/data/buffer.o \
	$(BUILD)/data/fifo.o

OBJ := \
	$(BUILD)/libultra/src/PR/rspboot.o \
	$(BUILD)/libultra/src/PR/gspFast3D.fifo.o \
	$(BUILD)/libultra/src/PR/aspMain.o \
	$(BUILD)/code.o \
	$(BUILD)/ulib.o \
	$(BUILD)/face.o \
	$(BUILD)/src/face/data.o

DATA := \
	$(BUILD)/data/cimg.o \
	$(BUILD)/data/zimg.o \
	$(BUILD)/data/timg.o \
	$(BUILD)/data/buffer.o \
	$(BUILD)/data/fifo.o \
	$(BUILD)/data/main.o \
	$(BUILD)/data/game.o \
	$(BUILD)/data/anime.o \
	$(BUILD)/data/demo.o

SZP := \
	$(BUILD)/data/gfx.szp.o \
	$(BUILD)/data/weather/gfx.szp.o

OBJECT_DATA := \
	$(BUILD)/data/object/object_a.o \
	$(BUILD)/data/object/player.o \
	$(BUILD)/data/object/object_b.o \
	$(BUILD)/data/object/object_c.o \
	$(BUILD)/data/object/camera.o

SHAPE_SZP := \
	$(BUILD)/shape/player/gfx.szp.o \
	$(BUILD)/shape/1a/gfx.szp.o \
	$(BUILD)/shape/1b/gfx.szp.o \
	$(BUILD)/shape/1c/gfx.szp.o \
	$(BUILD)/shape/1d/gfx.szp.o \
	$(BUILD)/shape/1e/gfx.szp.o \
	$(BUILD)/shape/1f/gfx.szp.o \
	$(BUILD)/shape/1g/gfx.szp.o \
	$(BUILD)/shape/1h/gfx.szp.o \
	$(BUILD)/shape/1i/gfx.szp.o \
	$(BUILD)/shape/1j/gfx.szp.o \
	$(BUILD)/shape/1k/gfx.szp.o \
	$(BUILD)/shape/2a/gfx.szp.o \
	$(BUILD)/shape/2b/gfx.szp.o \
	$(BUILD)/shape/2c/gfx.szp.o \
	$(BUILD)/shape/2d/gfx.szp.o \
	$(BUILD)/shape/2e/gfx.szp.o \
	$(BUILD)/shape/2f/gfx.szp.o \
	$(BUILD)/shape/3common/gfx.szp.o \
	$(BUILD)/shape/global/gfx.szp.o

SHAPE_DATA := \
	$(BUILD)/shape/player/shape.o \
	$(BUILD)/shape/1a/shape.o \
	$(BUILD)/shape/1b/shape.o \
	$(BUILD)/shape/1c/shape.o \
	$(BUILD)/shape/1d/shape.o \
	$(BUILD)/shape/1e/shape.o \
	$(BUILD)/shape/1f/shape.o \
	$(BUILD)/shape/1g/shape.o \
	$(BUILD)/shape/1h/shape.o \
	$(BUILD)/shape/1i/shape.o \
	$(BUILD)/shape/1j/shape.o \
	$(BUILD)/shape/1k/shape.o \
	$(BUILD)/shape/2a/shape.o \
	$(BUILD)/shape/2b/shape.o \
	$(BUILD)/shape/2c/shape.o \
	$(BUILD)/shape/2d/shape.o \
	$(BUILD)/shape/2e/shape.o \
	$(BUILD)/shape/2f/shape.o \
	$(BUILD)/shape/3common/shape.o \
	$(BUILD)/shape/global/shape.o

BACK_SZP := \
	$(BUILD)/data/back/title.szp.o \
	$(BUILD)/data/back/a.szp.o \
	$(BUILD)/data/back/b.szp.o \
	$(BUILD)/data/back/c.szp.o \
	$(BUILD)/data/back/d.szp.o \
	$(BUILD)/data/back/e.szp.o \
	$(BUILD)/data/back/f.szp.o \
	$(BUILD)/data/back/g.szp.o \
	$(BUILD)/data/back/h.szp.o \
	$(BUILD)/data/back/i.szp.o \
	$(BUILD)/data/back/j.szp.o

TEXTURE_SZP := \
	$(BUILD)/data/texture/a.szp.o \
	$(BUILD)/data/texture/b.szp.o \
	$(BUILD)/data/texture/c.szp.o \
	$(BUILD)/data/texture/d.szp.o \
	$(BUILD)/data/texture/e.szp.o \
	$(BUILD)/data/texture/f.szp.o \
	$(BUILD)/data/texture/g.szp.o \
	$(BUILD)/data/texture/h.szp.o \
	$(BUILD)/data/texture/i.szp.o \
	$(BUILD)/data/texture/j.szp.o \
	$(BUILD)/data/texture/k.szp.o \
	$(BUILD)/data/texture/l.szp.o

STAGE_SZP := \
	$(BUILD)/stage/title/logo.szp.o \
	$(BUILD)/stage/title/debug.szp.o \
	$(BUILD)/stage/select/gfx.szp.o \
	$(BUILD)/stage/bbh/gfx.szp.o \
	$(BUILD)/stage/ccm/gfx.szp.o \
	$(BUILD)/stage/inside/gfx.szp.o \
	$(BUILD)/stage/hmc/gfx.szp.o \
	$(BUILD)/stage/ssl/gfx.szp.o \
	$(BUILD)/stage/bob/gfx.szp.o \
	$(BUILD)/stage/sl/gfx.szp.o \
	$(BUILD)/stage/wdw/gfx.szp.o \
	$(BUILD)/stage/jrb/gfx.szp.o \
	$(BUILD)/stage/thi/gfx.szp.o \
	$(BUILD)/stage/ttc/gfx.szp.o \
	$(BUILD)/stage/rr/gfx.szp.o \
	$(BUILD)/stage/grounds/gfx.szp.o \
	$(BUILD)/stage/bitdw/gfx.szp.o \
	$(BUILD)/stage/vcutm/gfx.szp.o \
	$(BUILD)/stage/bitfs/gfx.szp.o \
	$(BUILD)/stage/sa/gfx.szp.o \
	$(BUILD)/stage/bits/gfx.szp.o \
	$(BUILD)/stage/lll/gfx.szp.o \
	$(BUILD)/stage/ddd/gfx.szp.o \
	$(BUILD)/stage/wf/gfx.szp.o \
	$(BUILD)/stage/ending/gfx.szp.o \
	$(BUILD)/stage/courtyard/gfx.szp.o \
	$(BUILD)/stage/pss/gfx.szp.o \
	$(BUILD)/stage/cotmc/gfx.szp.o \
	$(BUILD)/stage/totwc/gfx.szp.o \
	$(BUILD)/stage/bitdwa/gfx.szp.o \
	$(BUILD)/stage/wmotr/gfx.szp.o \
	$(BUILD)/stage/bitfsa/gfx.szp.o \
	$(BUILD)/stage/bitsa/gfx.szp.o \
	$(BUILD)/stage/ttm/gfx.szp.o

STAGE_DATA := \
	$(BUILD)/stage/title/program.o \
	$(BUILD)/stage/title/shape.o \
	$(BUILD)/stage/select/program.o \
	$(BUILD)/stage/select/shape.o \
	$(BUILD)/stage/bbh/program.o \
	$(BUILD)/stage/bbh/shape.o \
	$(BUILD)/stage/ccm/program.o \
	$(BUILD)/stage/ccm/shape.o \
	$(BUILD)/stage/inside/program.o \
	$(BUILD)/stage/inside/shape.o \
	$(BUILD)/stage/hmc/program.o \
	$(BUILD)/stage/hmc/shape.o \
	$(BUILD)/stage/ssl/program.o \
	$(BUILD)/stage/ssl/shape.o \
	$(BUILD)/stage/bob/program.o \
	$(BUILD)/stage/bob/shape.o \
	$(BUILD)/stage/sl/program.o \
	$(BUILD)/stage/sl/shape.o \
	$(BUILD)/stage/wdw/program.o \
	$(BUILD)/stage/wdw/shape.o \
	$(BUILD)/stage/jrb/program.o \
	$(BUILD)/stage/jrb/shape.o \
	$(BUILD)/stage/thi/program.o \
	$(BUILD)/stage/thi/shape.o \
	$(BUILD)/stage/ttc/program.o \
	$(BUILD)/stage/ttc/shape.o \
	$(BUILD)/stage/rr/program.o \
	$(BUILD)/stage/rr/shape.o \
	$(BUILD)/stage/grounds/program.o \
	$(BUILD)/stage/grounds/shape.o \
	$(BUILD)/stage/bitdw/program.o \
	$(BUILD)/stage/bitdw/shape.o \
	$(BUILD)/stage/vcutm/program.o \
	$(BUILD)/stage/vcutm/shape.o \
	$(BUILD)/stage/bitfs/program.o \
	$(BUILD)/stage/bitfs/shape.o \
	$(BUILD)/stage/sa/program.o \
	$(BUILD)/stage/sa/shape.o \
	$(BUILD)/stage/bits/program.o \
	$(BUILD)/stage/bits/shape.o \
	$(BUILD)/stage/lll/program.o \
	$(BUILD)/stage/lll/shape.o \
	$(BUILD)/stage/ddd/program.o \
	$(BUILD)/stage/ddd/shape.o \
	$(BUILD)/stage/wf/program.o \
	$(BUILD)/stage/wf/shape.o \
	$(BUILD)/stage/ending/program.o \
	$(BUILD)/stage/ending/shape.o \
	$(BUILD)/stage/courtyard/program.o \
	$(BUILD)/stage/courtyard/shape.o \
	$(BUILD)/stage/pss/program.o \
	$(BUILD)/stage/pss/shape.o \
	$(BUILD)/stage/cotmc/program.o \
	$(BUILD)/stage/cotmc/shape.o \
	$(BUILD)/stage/totwc/program.o \
	$(BUILD)/stage/totwc/shape.o \
	$(BUILD)/stage/bitdwa/program.o \
	$(BUILD)/stage/bitdwa/shape.o \
	$(BUILD)/stage/wmotr/program.o \
	$(BUILD)/stage/wmotr/shape.o \
	$(BUILD)/stage/bitfsa/program.o \
	$(BUILD)/stage/bitfsa/shape.o \
	$(BUILD)/stage/bitsa/program.o \
	$(BUILD)/stage/bitsa/shape.o \
	$(BUILD)/stage/ttm/program.o \
	$(BUILD)/stage/ttm/shape.o

AUDIO_DATA := \
	$(BUILD)/src/audio/heap.o \
	$(BUILD)/src/audio/bss.o \
	$(BUILD)/audio/ctl.o \
	$(BUILD)/audio/tbl.o \
	$(BUILD)/audio/seq.o \
	$(BUILD)/audio/bnk.o

INS := audio/se.ins audio/music.ins
SEQ := \
	audio/se/se.seq \
	audio/music/starcatch.seq \
	audio/music/title.seq \
	audio/music/field.seq \
	audio/music/castle.seq \
	audio/music/water.seq \
	audio/music/fire.seq \
	audio/music/arena.seq \
	audio/music/snow.seq \
	audio/music/slider.seq \
	audio/music/ghost.seq \
	audio/music/lullaby.seq \
	audio/music/dungeon.seq \
	audio/music/starselect.seq \
	audio/music/wing.seq \
	audio/music/metal.seq \
	audio/music/bowsermsg.seq \
	audio/music/bowser.seq \
	audio/music/hiscore.seq \
	audio/music/merrygoround.seq \
	audio/music/fanfare.seq \
	audio/music/star.seq \
	audio/music/battle.seq \
	audio/music/arenaclear.seq \
	audio/music/endless.seq \
	audio/music/final.seq \
	audio/music/staff.seq \
	audio/music/solution.seq \
	audio/music/toadmsg.seq \
	audio/music/peachmsg.seq \
	audio/music/intro.seq \
	audio/music/finalclear.seq \
	audio/music/ending.seq \
	audio/music/fileselect.seq \
	audio/music/lakitumsg.seq

LIBULTRA_OBJ := \
	$(BUILD)/libultra/src/parameters.o \
	$(BUILD)/libultra/src/vitbl.o \
	$(BUILD)/libultra/src/settime.o \
	$(BUILD)/libultra/src/maptlb.o \
	$(BUILD)/libultra/src/unmaptlball.o \
	$(BUILD)/libultra/src/sprintf.o \
	$(BUILD)/libultra/src/createmesgqueue.o \
	$(BUILD)/libultra/src/seteventmesg.o $(BUILD)/libultra/src/seteventmesg.data.o \
	$(BUILD)/libultra/src/visetevent.o \
	$(BUILD)/libultra/src/createthread.o \
	$(BUILD)/libultra/src/recvmesg.o \
	$(BUILD)/libultra/src/sptask.o $(BUILD)/libultra/src/sptask.data.o \
	$(BUILD)/libultra/src/sptaskyield.o \
	$(BUILD)/libultra/src/sendmesg.o \
	$(BUILD)/libultra/src/sptaskyielded.o \
	$(BUILD)/libultra/src/startthread.o \
	$(BUILD)/libultra/src/writebackdcacheall.o \
	$(BUILD)/libultra/src/vimgr.o $(BUILD)/libultra/src/vimgr.data.o \
	$(BUILD)/libultra/src/visetmode.o \
	$(BUILD)/libultra/src/viblack.o \
	$(BUILD)/libultra/src/visetspecial.o \
	$(BUILD)/libultra/src/pimgr.o $(BUILD)/libultra/src/pimgr.data.o \
	$(BUILD)/libultra/src/setthreadpri.o \
	$(BUILD)/libultra/src/initialize.o $(BUILD)/libultra/src/initialize.data.o \
	$(BUILD)/libultra/src/viswapbuf.o \
	$(BUILD)/libultra/src/sqrtf.o \
	$(BUILD)/libultra/src/contreaddata.o \
	$(BUILD)/libultra/src/controller.o $(BUILD)/libultra/src/controller.data.o \
	$(BUILD)/libultra/src/conteepprobe.o \
	$(BUILD)/libultra/src/ll.o \
	$(BUILD)/libultra/src/invaldcache.o \
	$(BUILD)/libultra/src/pidma.o \
	$(BUILD)/libultra/src/bzero.o \
	$(BUILD)/libultra/src/invalicache.o \
	$(BUILD)/libultra/src/conteeplongread.o \
	$(BUILD)/libultra/src/conteeplongwrite.o \
	$(BUILD)/libultra/src/bcopy.o \
	$(BUILD)/libultra/src/ortho.o \
	$(BUILD)/libultra/src/perspective.o $(BUILD)/libultra/src/perspective.data.o \
	$(BUILD)/libultra/src/gettime.o \
	$(BUILD)/libultra/src/llcvt.o $(BUILD)/libultra/src/llcvt.data.o \
	$(BUILD)/libultra/src/cosf.o $(BUILD)/libultra/src/cosf.data.o \
	$(BUILD)/libultra/src/sinf.o $(BUILD)/libultra/src/sinf.data.o \
	$(BUILD)/libultra/src/translate.o \
	$(BUILD)/libultra/src/rotate.o $(BUILD)/libultra/src/rotate.data.o \
	$(BUILD)/libultra/src/scale.o \
	$(BUILD)/libultra/src/aisetfreq.o \
	$(BUILD)/libultra/src/bnkf.o \
	$(BUILD)/libultra/src/writebackdcache.o \
	$(BUILD)/libultra/src/aigetlen.o \
	$(BUILD)/libultra/src/aisetnextbuf.o $(BUILD)/libultra/src/aisetnextbuf.data.o \
	$(BUILD)/libultra/src/timerintr.o $(BUILD)/libultra/src/timerintr.data.o \
	$(BUILD)/libultra/src/xprintf.o $(BUILD)/libultra/src/xprintf.data.o \
	$(BUILD)/libultra/src/string.o \
	$(BUILD)/libultra/src/thread.o $(BUILD)/libultra/src/thread.data.o \
	$(BUILD)/libultra/src/interrupt.o \
	$(BUILD)/libultra/src/vi.o $(BUILD)/libultra/src/vi.data.o \
	$(BUILD)/libultra/src/exceptasm.o \
	$(BUILD)/libultra/src/libm_vals.o \
	$(BUILD)/libultra/src/virtualtophysical.o \
	$(BUILD)/libultra/src/spsetstat.o \
	$(BUILD)/libultra/src/spsetpc.o \
	$(BUILD)/libultra/src/sprawdma.o \
	$(BUILD)/libultra/src/sp.o \
	$(BUILD)/libultra/src/spgetstat.o \
	$(BUILD)/libultra/src/getthreadpri.o \
	$(BUILD)/libultra/src/vigetcurrcontext.o \
	$(BUILD)/libultra/src/viswapcontext.o \
	$(BUILD)/libultra/src/getcount.o \
	$(BUILD)/libultra/src/piacs.o $(BUILD)/libultra/src/piacs.data.o \
	$(BUILD)/libultra/src/pirawdma.o \
	$(BUILD)/libultra/src/devmgr.o \
	$(BUILD)/libultra/src/setsr.o \
	$(BUILD)/libultra/src/getsr.o \
	$(BUILD)/libultra/src/setfpccsr.o \
	$(BUILD)/libultra/src/sirawread.o \
	$(BUILD)/libultra/src/sirawwrite.o \
	$(BUILD)/libultra/src/maptlbrdb.o \
	$(BUILD)/libultra/src/pirawread.o \
	$(BUILD)/libultra/src/siacs.o $(BUILD)/libultra/src/siacs.data.o \
	$(BUILD)/libultra/src/sirawdma.o \
	$(BUILD)/libultra/src/settimer.o \
	$(BUILD)/libultra/src/conteepwrite.o \
	$(BUILD)/libultra/src/jammesg.o \
	$(BUILD)/libultra/src/pigetcmdq.o \
	$(BUILD)/libultra/src/conteepread.o $(BUILD)/libultra/src/conteepread.data.o \
	$(BUILD)/libultra/src/mtx.o \
	$(BUILD)/libultra/src/normalize.o \
	$(BUILD)/libultra/src/ai.o \
	$(BUILD)/libultra/src/setcompare.o \
	$(BUILD)/libultra/src/xlitob.o $(BUILD)/libultra/src/xlitob.data.o \
	$(BUILD)/libultra/src/xldtob.o $(BUILD)/libultra/src/xldtob.data.o \
	$(BUILD)/libultra/src/vimodentsclan1.o \
	$(BUILD)/libultra/src/vimodepallan1.o \
	$(BUILD)/libultra/src/kdebugserver.o $(BUILD)/libultra/src/kdebugserver.data.o \
	$(BUILD)/libultra/src/syncputchars.o $(BUILD)/libultra/src/syncputchars.data.o \
	$(BUILD)/libultra/src/setintmask.o \
	$(BUILD)/libultra/src/destroythread.o \
	$(BUILD)/libultra/src/probetlb.o \
	$(BUILD)/libultra/src/si.o \
	$(BUILD)/libultra/src/ldiv.o \
	$(BUILD)/libultra/src/getcause.o \
	$(BUILD)/libultra/src/atomic.o

IRIX_S := \
	$(BUILD)/libultra/src/PR/Boot.o

IRIX_C := \
	$(BUILD)/libultra/src/string.o

################################################################################
# Player

MARIO_DEP := \
	shape/player/mario/h_waist.h \
	shape/player/mario/h_waist.blue.h \
	shape/player/mario/h_uarmL.h \
	shape/player/mario/h_uarmL.red.h \
	shape/player/mario/h_larmL.h \
	shape/player/mario/h_larmL.red.h \
	shape/player/mario/h_fistL.h \
	shape/player/mario/h_fistL.white.h \
	shape/player/mario/h_uarmR.h \
	shape/player/mario/h_uarmR.red.h \
	shape/player/mario/h_larmR.h \
	shape/player/mario/h_larmR.red.h \
	shape/player/mario/h_fistR.h \
	shape/player/mario/h_fistR.white.h \
	shape/player/mario/h_thighL.h \
	shape/player/mario/h_thighL.blue.h \
	shape/player/mario/h_shinL.h \
	shape/player/mario/h_shinL.blue.h \
	shape/player/mario/h_shoeL.h \
	shape/player/mario/h_shoeL.shoe.h \
	shape/player/mario/h_thighR.h \
	shape/player/mario/h_thighR.blue.h \
	shape/player/mario/h_shinR.h \
	shape/player/mario/h_shinR.blue.h \
	shape/player/mario/h_shoeR.h \
	shape/player/mario/h_shoeR.shoe.h \
	shape/player/mario/h_torso.h \
	shape/player/mario/h_torso.button.h \
	shape/player/mario/h_torso.blue.h \
	shape/player/mario/h_torso.red.h \
	shape/player/mario/h_cap.h \
	shape/player/mario/h_cap.logo.h \
	shape/player/mario/h_cap.eyes.h \
	shape/player/mario/h_cap.sideburn.h \
	shape/player/mario/h_cap.moustache.h \
	shape/player/mario/h_cap.red.h \
	shape/player/mario/h_cap.skin.h \
	shape/player/mario/h_cap.hair.h \
	shape/player/mario/h_hair.h \
	shape/player/mario/h_hair.eyes.h \
	shape/player/mario/h_hair.sideburn.h \
	shape/player/mario/h_hair.moustache.h \
	shape/player/mario/h_hair.skin.h \
	shape/player/mario/h_hair.hair.h \
	shape/player/mario/h_hair.001.h \
	shape/player/mario/h_hair.001.skin.h \
	shape/player/mario/m_waist.h \
	shape/player/mario/m_waist.blue.h \
	shape/player/mario/m_uarmL.h \
	shape/player/mario/m_uarmL.red.h \
	shape/player/mario/m_larmL.h \
	shape/player/mario/m_larmL.red.h \
	shape/player/mario/m_fistL.h \
	shape/player/mario/m_fistL.white.h \
	shape/player/mario/m_uarmR.h \
	shape/player/mario/m_uarmR.red.h \
	shape/player/mario/m_larmR.h \
	shape/player/mario/m_larmR.red.h \
	shape/player/mario/m_fistR.h \
	shape/player/mario/m_fistR.white.h \
	shape/player/mario/m_thighL.h \
	shape/player/mario/m_thighL.blue.h \
	shape/player/mario/m_shinL.h \
	shape/player/mario/m_shinL.blue.h \
	shape/player/mario/m_shoeL.h \
	shape/player/mario/m_shoeL.shoe.h \
	shape/player/mario/m_thighR.h \
	shape/player/mario/m_thighR.blue.h \
	shape/player/mario/m_shinR.h \
	shape/player/mario/m_shinR.blue.h \
	shape/player/mario/m_shoeR.h \
	shape/player/mario/m_shoeR.shoe.h \
	shape/player/mario/m_torso.h \
	shape/player/mario/m_torso.button.h \
	shape/player/mario/m_torso.red.h \
	shape/player/mario/m_torso.blue.h \
	shape/player/mario/l_waist.h \
	shape/player/mario/l_waist.blue.h \
	shape/player/mario/l_uarmL.h \
	shape/player/mario/l_uarmL.red.h \
	shape/player/mario/l_larmL.h \
	shape/player/mario/l_larmL.red.h \
	shape/player/mario/l_fistL.h \
	shape/player/mario/l_fistL.white.h \
	shape/player/mario/l_uarmR.h \
	shape/player/mario/l_uarmR.red.h \
	shape/player/mario/l_larmR.h \
	shape/player/mario/l_larmR.red.h \
	shape/player/mario/l_fistR.h \
	shape/player/mario/l_fistR.white.h \
	shape/player/mario/l_thighL.h \
	shape/player/mario/l_thighL.blue.h \
	shape/player/mario/l_shinL.h \
	shape/player/mario/l_shinL.blue.h \
	shape/player/mario/l_shoeL.h \
	shape/player/mario/l_shoeL.shoe.h \
	shape/player/mario/l_thighR.h \
	shape/player/mario/l_thighR.blue.h \
	shape/player/mario/l_shinR.h \
	shape/player/mario/l_shinR.blue.h \
	shape/player/mario/l_shoeR.h \
	shape/player/mario/l_shoeR.shoe.h \
	shape/player/mario/l_torso.h \
	shape/player/mario/l_torso.button.h \
	shape/player/mario/l_torso.blue.h \
	shape/player/mario/l_torso.red.h \
	shape/player/mario/l_cap.h \
	shape/player/mario/l_cap.logo.h \
	shape/player/mario/l_cap.eyes.h \
	shape/player/mario/l_cap.moustache.h \
	shape/player/mario/l_cap.red.h \
	shape/player/mario/l_cap.skin.h \
	shape/player/mario/l_cap.hair.h \
	shape/player/mario/l_hair.h \
	shape/player/mario/l_hair.eyes.h \
	shape/player/mario/l_hair.moustache.h \
	shape/player/mario/l_hair.skin.h \
	shape/player/mario/l_hair.hair.h \
	shape/player/mario/handL.h \
	shape/player/mario/handL.white.h \
	shape/player/mario/handR.h \
	shape/player/mario/handR.white.h \
	shape/player/mario/capR.h \
	shape/player/mario/capR.logo.h \
	shape/player/mario/capR.white.h \
	shape/player/mario/capR.red.h \
	shape/player/mario/capR.hair.h \
	shape/player/mario/wingsR.h \
	shape/player/mario/wingsR.wing_l.h \
	shape/player/mario/wingsR.wing_r.h \
	shape/player/mario/peaceR.h \
	shape/player/mario/peaceR.white.h \
	shape/player/mario/cap.h \
	shape/player/mario/cap.logo.h \
	shape/player/mario/cap.red.h \
	shape/player/mario/cap.hair.h \
	shape/player/mario/wings.h \
	shape/player/mario/wings.wing_l.h \
	shape/player/mario/wings.wing_r.h \
	shape/player/mario/wing.h \
	shape/player/mario/wing.wing_l.h \
	shape/player/mario/wing.wing_r.h

################################################################################
# Shape1B

BULLY_DEP := \
	shape/1b/bully/horn.h \
	shape/1b/bully/horn.horn.h \
	shape/1b/bully/shoeL.h \
	shape/1b/bully/shoeL.shoe.h \
	shape/1b/bully/shoeR.h \
	shape/1b/bully/shoeR.shoe.h \
	shape/1b/bully/eyes_old.h \
	shape/1b/bully/eyes_old.eye_old.h \
	shape/1b/bully/body_old.h \
	shape/1b/bully/body_old.body_old.h \
	shape/1b/bully/body.h \
	shape/1b/bully/body.body_l.h \
	shape/1b/bully/body.body_r.h \
	shape/1b/bully/body_big.h \
	shape/1b/bully/body_big.body_l.h \
	shape/1b/bully/body_big.body_r.h \
	shape/1b/bully/eyes.h \
	shape/1b/bully/eyes.eye.h

BLARGG_DEP := \
	shape/1b/blargg/upper_jaw.h \
	shape/1b/blargg/upper_jaw.teeth.h \
	shape/1b/blargg/upper_jaw.upper_jaw.h \
	shape/1b/blargg/lower_jaw.h \
	shape/1b/blargg/lower_jaw.teeth.h \
	shape/1b/blargg/lower_jaw.lower_jaw.h \
	shape/1b/blargg/body.h \
	shape/1b/blargg/body.body.h

################################################################################
# Shape2B

SKEETER_DEP := \
	shape/2b/skeeter/body.h \
	shape/2b/skeeter/body.sphere.h \
	shape/2b/skeeter/tail_end.h \
	shape/2b/skeeter/tail_end.sphere.h \
	shape/2b/skeeter/eye.h \
	shape/2b/skeeter/eye.sphere.h \
	shape/2b/skeeter/irisR.h \
	shape/2b/skeeter/irisR.iris.h \
	shape/2b/skeeter/irisL.h \
	shape/2b/skeeter/irisL.iris.h \
	shape/2b/skeeter/foot.h \
	shape/2b/skeeter/foot.foot.h \
	shape/2b/skeeter/footBR_old.h \
	shape/2b/skeeter/footBR_old.shade.h \
	shape/2b/skeeter/llegBR.h \
	shape/2b/skeeter/llegBR.shade.h \
	shape/2b/skeeter/ulegBR.h \
	shape/2b/skeeter/ulegBR.shade.h \
	shape/2b/skeeter/footFR_old.h \
	shape/2b/skeeter/footFR_old.shade.h \
	shape/2b/skeeter/llegFR.h \
	shape/2b/skeeter/llegFR.shade.h \
	shape/2b/skeeter/ulegFR.h \
	shape/2b/skeeter/ulegFR.shade.h \
	shape/2b/skeeter/footFL_old.h \
	shape/2b/skeeter/footFL_old.shade.h \
	shape/2b/skeeter/llegFL.h \
	shape/2b/skeeter/llegFL.shade.h \
	shape/2b/skeeter/ulegFL.h \
	shape/2b/skeeter/ulegFL.shade.h \
	shape/2b/skeeter/eyeR_old.h \
	shape/2b/skeeter/eyeR_old.shade.h \
	shape/2b/skeeter/footBL_old.h \
	shape/2b/skeeter/footBL_old.shade.h \
	shape/2b/skeeter/llegBL.h \
	shape/2b/skeeter/llegBL.shade.h \
	shape/2b/skeeter/ulegBL.h \
	shape/2b/skeeter/ulegBL.shade.h \
	shape/2b/skeeter/eyeL_old.h \
	shape/2b/skeeter/eyeL_old.shade.h \
	shape/2b/skeeter/tail_end_old.h \
	shape/2b/skeeter/tail_end_old.shade.h \
	shape/2b/skeeter/tail.h \
	shape/2b/skeeter/tail.shade.h \
	shape/2b/skeeter/body_old.h \
	shape/2b/skeeter/body_old.shade.h

KELP_DEP := \
	shape/2b/kelp/0.h \
	shape/2b/kelp/0.0.h \
	shape/2b/kelp/1.h \
	shape/2b/kelp/1.1.h \
	shape/2b/kelp/2.h \
	shape/2b/kelp/2.2.h \
	shape/2b/kelp/3.h \
	shape/2b/kelp/3.3.h

WATERMINE_DEP := \
	shape/2b/watermine/mine.h \
	shape/2b/watermine/mine.l.h \
	shape/2b/watermine/mine.r.h \
	shape/2b/watermine/spike.h \
	shape/2b/watermine/spike.spike.h

PIRANHA_DEP := \
	shape/2b/piranha/body.h \
	shape/2b/piranha/body.piranha.h \
	shape/2b/piranha/fin.h \
	shape/2b/piranha/fin.piranha.h \
	shape/2b/piranha/tail.h \
	shape/2b/piranha/tail.piranha.h

BUB_DEP := \
	shape/2b/bub/body.h \
	shape/2b/bub/body.goggles.h \
	shape/2b/bub/body.fin.h \
	shape/2b/bub/body.eyes.h \
	shape/2b/bub/body.scale.h \
	shape/2b/bub/body.mouth.h \
	shape/2b/bub/body.white.h \
	shape/2b/bub/tail.h \
	shape/2b/bub/tail.fin.h \
	shape/2b/bub/finL.h \
	shape/2b/bub/finL.fin.h \
	shape/2b/bub/finR.h \
	shape/2b/bub/finR.fin.h

WATERRING_DEP := \
	shape/2b/waterring/waterring.h \
	shape/2b/waterring/waterring.shade.h

CHEST_DEP := \
	shape/2b/chest/box.h \
	shape/2b/chest/box.keyhole.h \
	shape/2b/chest/box.latch.h \
	shape/2b/chest/box.inside.h \
	shape/2b/chest/box.outside.h \
	shape/2b/chest/lid.h \
	shape/2b/chest/lid.inside.h \
	shape/2b/chest/lid.latch.h \
	shape/2b/chest/lid.outside.h

################################################################################
# Shape2D

LAKITU2_DEP := \
	shape/2d/lakitu2/body.h \
	shape/2d/lakitu2/body.shell.h \
	shape/2d/lakitu2/body.skin.h \
	shape/2d/lakitu2/mouth.h \
	shape/2d/lakitu2/mouth.mouth.h \
	shape/2d/lakitu2/armR.h \
	shape/2d/lakitu2/armR.skin.h \
	shape/2d/lakitu2/armL.h \
	shape/2d/lakitu2/armL.skin.h \
	shape/2d/lakitu2/eyes.h \
	shape/2d/lakitu2/eyes.eyes.h \
	shape/2d/lakitu2/camera.h \
	shape/2d/lakitu2/camera.lens.h \
	shape/2d/lakitu2/camera.camera1.h \
	shape/2d/lakitu2/camera.camera2.h \
	shape/2d/lakitu2/camera.camera3.h \
	shape/2d/lakitu2/rod0.h \
	shape/2d/lakitu2/rod0.rod1.h \
	shape/2d/lakitu2/rod1.h \
	shape/2d/lakitu2/rod1.rod4.h \
	shape/2d/lakitu2/rod2.h \
	shape/2d/lakitu2/rod2.rod4.h

TOAD_DEP := \
	shape/2d/toad/head.h \
	shape/2d/toad/head.face.h \
	shape/2d/toad/head.spot.h \
	shape/2d/toad/head.white.h \
	shape/2d/toad/vest.h \
	shape/2d/toad/vest.vest.h \
	shape/2d/toad/body.h \
	shape/2d/toad/body.white.h \
	shape/2d/toad/body.skin.h \
	shape/2d/toad/armR.h \
	shape/2d/toad/armR.skin.h \
	shape/2d/toad/armL.h \
	shape/2d/toad/armL.skin.h \
	shape/2d/toad/shoeR.h \
	shape/2d/toad/shoeR.shoe.h \
	shape/2d/toad/shoeL.h \
	shape/2d/toad/shoeL.shoe.h

MIPS_DEP := \
	shape/2d/mips/0.h \
	shape/2d/mips/0.face.h \
	shape/2d/mips/0.light1.h \
	shape/2d/mips/0.white.h \
	shape/2d/mips/1.h \
	shape/2d/mips/1.face.h \
	shape/2d/mips/2.h \
	shape/2d/mips/2.face1.h \
	shape/2d/mips/2.face.h \
	shape/2d/mips/3.h \
	shape/2d/mips/3.face1.h \
	shape/2d/mips/3.face2.h \
	shape/2d/mips/3.face.h \
	shape/2d/mips/4.h \
	shape/2d/mips/4.face1.h \
	shape/2d/mips/4.face.h \
	shape/2d/mips/5.h \
	shape/2d/mips/5.face1.h \
	shape/2d/mips/5.face.h \
	shape/2d/mips/6.h \
	shape/2d/mips/6.face1.h \
	shape/2d/mips/6.face.h \
	shape/2d/mips/7.h \
	shape/2d/mips/7.face1.h \
	shape/2d/mips/7.face.h \
	shape/2d/mips/8.h \
	shape/2d/mips/8.face1.h \
	shape/2d/mips/8.face.h \
	shape/2d/mips/9.h \
	shape/2d/mips/9.face1.h \
	shape/2d/mips/9.face.h \
	shape/2d/mips/10.h \
	shape/2d/mips/10.light2.h \
	shape/2d/mips/11.h \
	shape/2d/mips/11.light2.h

BOO2_DEP := \
	shape/2d/boo2/boo.h \
	shape/2d/boo2/boo.mouth.h \
	shape/2d/boo2/boo.eyes.h \
	shape/2d/boo2/boo.shade.h

################################################################################
# Global

BUTTERFLY_DEP := \
	shape/global/butterfly/l.h \
	shape/global/butterfly/l.wing.h \
	shape/global/butterfly/r.h \
	shape/global/butterfly/r.wing.h

PIPE_DEP := \
	shape/global/pipe/side.h \
	shape/global/pipe/side.side.h \
	shape/global/pipe/end.h \
	shape/global/pipe/end.top.h \
	shape/global/pipe/end.bottom.h

DOOR_DEP := \
	shape/global/door/ah.h \
	shape/global/door/ah.a_side.h \
	shape/global/door/ah.a_face.h \
	shape/global/door/ahf.h \
	shape/global/door/ahf.knob.h \
	shape/global/door/ahb.h \
	shape/global/door/ahb.knob.h \
	shape/global/door/al.h \
	shape/global/door/al.a_face.h \
	shape/global/door/h.h \
	shape/global/door/h.knob.h \
	shape/global/door/h.b_side.h \
	shape/global/door/h.b_face.h \
	shape/global/door/l.h \
	shape/global/door/l.b_face.h \
	shape/global/door/l.knob.h

DOORKEY_DEP := \
	shape/global/doorkey/key.h \
	shape/global/doorkey/key.key.h

FISH_DEP := \
	shape/global/fish/body.h \
	shape/global/fish/body.fish.h \
	shape/global/fish/tail.h \
	shape/global/fish/tail.fish.h

CAP_DEP := \
	shape/global/cap/cap.h \
	shape/global/cap/cap.logo.h \
	shape/global/cap/cap.red.h \
	shape/global/cap/cap.hair.h \
	shape/global/cap/wing.h \
	shape/global/cap/wing.wing_l.h \
	shape/global/cap/wing.wing_r.h

POWERSTAR_DEP := \
	shape/global/powerstar/star.h \
	shape/global/powerstar/star.star.h \
	shape/global/powerstar/eyes.h \
	shape/global/powerstar/eyes.eye.h

SHADESTAR_DEP := \
	shape/global/shadestar/star.h \
	shape/global/shadestar/star.star.h

SIGNPOST_DEP := \
	shape/global/signpost/post.h \
	shape/global/signpost/post.wood.h \
	shape/global/signpost/sign.h \
	shape/global/signpost/sign.wood.h \
	shape/global/signpost/sign.face.h

TREE_DEP := \
	shape/global/tree/a.h \
	shape/global/tree/a.a_l.h \
	shape/global/tree/a.a_r.h \
	shape/global/tree/b.h \
	shape/global/tree/b.b.h \
	shape/global/tree/c.h \
	shape/global/tree/c.c.h \
	shape/global/tree/d.h \
	shape/global/tree/d.b.h \
	shape/global/tree/e.h \
	shape/global/tree/e.e.h

################################################################################
# Title

LOGO_DEP := \
	stage/title/logo.h \
	stage/title/logo.marble.h \
	stage/title/logo.wood.h \
	stage/title/logo.shade.h \
	stage/title/symbol.h \
	stage/title/symbol.copyright.h \
	stage/title/symbol.trademark.h

DEBUG_DEP := \
	stage/title/super_s.h \
	stage/title/super_s.super_s.h \
	stage/title/super_u.h \
	stage/title/super_u.super_u.h \
	stage/title/super_p.h \
	stage/title/super_p.super_p.h \
	stage/title/super_e.h \
	stage/title/super_e.super_e.h \
	stage/title/super_r.h \
	stage/title/super_r.super_r.h \
	stage/title/mario_m.h \
	stage/title/mario_m.mario_m.h \
	stage/title/mario_a.h \
	stage/title/mario_a.mario_a.h \
	stage/title/mario_r.h \
	stage/title/mario_r.mario_r.h \
	stage/title/mario_i.h \
	stage/title/mario_i.mario_i.h \
	stage/title/mario_o.h \
	stage/title/mario_o.mario_o.h

################################################################################
# Select

FILE_DEP := \
	stage/select/file/file.h \
	stage/select/file/file.edge.h \
	stage/select/file/file.face.h

TILE_DEP := \
	stage/select/tile/tile.h \
	stage/select/tile/tile.tile.h

################################################################################
# BoB

BATTLEFIELD_DEP := \
	stage/bob/battlefield/smooth.h \
	stage/bob/battlefield/smooth.c11.h \
	stage/bob/battlefield/smooth.c18.h \
	stage/bob/battlefield/smooth.c12.h \
	stage/bob/battlefield/flat.h \
	stage/bob/battlefield/flat.c7.h \
	stage/bob/battlefield/flat.c4.h \
	stage/bob/battlefield/flat.c3.h \
	stage/bob/battlefield/flat.c10.h \
	stage/bob/battlefield/flat.c9.h \
	stage/bob/battlefield/flat.c6.h \
	stage/bob/battlefield/flat.2.h \
	stage/bob/battlefield/flat.3.h \
	stage/bob/battlefield/flat.1.h \
	stage/bob/battlefield/flat.c12.h \
	stage/bob/battlefield/xlu_decal.h \
	stage/bob/battlefield/xlu_decal.c21.h \
	stage/bob/battlefield/tex_edge.h \
	stage/bob/battlefield/tex_edge.c16.h \
	stage/bob/battlefield/tex_edge.0.h \
	stage/bob/battlefield/shade.h \
	stage/bob/battlefield/shade.c17.h \
	stage/bob/battlefield/shade.c17_shade.h \
	stage/bob/battlefield/shade.c11.h \
	stage/bob/battlefield/shade.c18.h \
	stage/bob/battlefield/shade.4.h \
	stage/bob/battlefield/shade.c19.h \
	stage/bob/battlefield/shade.c12.h \
	stage/bob/battlefield/cave.h \
	stage/bob/battlefield/cave.c17_cave.h

BOB_54_DEP := \
	stage/bob/54/54.h \
	stage/bob/54/54.c16.h

BOB_55_DEP := \
	stage/bob/55/55.h \
	stage/bob/55/55.c12.h

BOB_56_DEP := \
	stage/bob/56/56.h \
	stage/bob/56/56.c16.h \

################################################################################

GFX_DEP := \
	data/gfx/dprint/0.rgba16.h \
	data/gfx/dprint/1.rgba16.h \
	data/gfx/dprint/2.rgba16.h \
	data/gfx/dprint/3.rgba16.h \
	data/gfx/dprint/4.rgba16.h \
	data/gfx/dprint/5.rgba16.h \
	data/gfx/dprint/6.rgba16.h \
	data/gfx/dprint/7.rgba16.h \
	data/gfx/dprint/8.rgba16.h \
	data/gfx/dprint/9.rgba16.h \
	data/gfx/dprint/a.rgba16.h \
	data/gfx/dprint/b.rgba16.h \
	data/gfx/dprint/c.rgba16.h \
	data/gfx/dprint/d.rgba16.h \
	data/gfx/dprint/e.rgba16.h \
	data/gfx/dprint/f.rgba16.h \
	data/gfx/dprint/g.rgba16.h \
	data/gfx/dprint/h.rgba16.h \
	data/gfx/dprint/i.rgba16.h \
	data/gfx/dprint/k.rgba16.h \
	data/gfx/dprint/l.rgba16.h \
	data/gfx/dprint/m.rgba16.h \
	data/gfx/dprint/n.rgba16.h \
	data/gfx/dprint/o.rgba16.h \
	data/gfx/dprint/p.rgba16.h \
	data/gfx/dprint/r.rgba16.h \
	data/gfx/dprint/s.rgba16.h \
	data/gfx/dprint/t.rgba16.h \
	data/gfx/dprint/u.rgba16.h \
	data/gfx/dprint/w.rgba16.h \
	data/gfx/dprint/y.rgba16.h \
	data/gfx/dprint/squote.rgba16.h \
	data/gfx/dprint/dquote.rgba16.h \
	data/gfx/dprint/multiply.rgba16.h \
	data/gfx/dprint/coin.rgba16.h \
	data/gfx/dprint/mario.rgba16.h \
	data/gfx/dprint/star.rgba16.h \
	data/gfx/staff/3.rgba16.h \
	data/gfx/staff/4.rgba16.h \
	data/gfx/staff/6.rgba16.h \
	data/gfx/staff/a.rgba16.h \
	data/gfx/staff/b.rgba16.h \
	data/gfx/staff/c.rgba16.h \
	data/gfx/staff/d.rgba16.h \
	data/gfx/staff/e.rgba16.h \
	data/gfx/staff/f.rgba16.h \
	data/gfx/staff/g.rgba16.h \
	data/gfx/staff/h.rgba16.h \
	data/gfx/staff/i.rgba16.h \
	data/gfx/staff/j.rgba16.h \
	data/gfx/staff/k.rgba16.h \
	data/gfx/staff/l.rgba16.h \
	data/gfx/staff/m.rgba16.h \
	data/gfx/staff/n.rgba16.h \
	data/gfx/staff/o.rgba16.h \
	data/gfx/staff/p.rgba16.h \
	data/gfx/staff/q.rgba16.h \
	data/gfx/staff/r.rgba16.h \
	data/gfx/staff/s.rgba16.h \
	data/gfx/staff/t.rgba16.h \
	data/gfx/staff/u.rgba16.h \
	data/gfx/staff/v.rgba16.h \
	data/gfx/staff/w.rgba16.h \
	data/gfx/staff/x.rgba16.h \
	data/gfx/staff/y.rgba16.h \
	data/gfx/staff/z.rgba16.h \
	data/gfx/staff/period.rgba16.h \
	data/gfx/message/0.ia4.h \
	data/gfx/message/1.ia4.h \
	data/gfx/message/2.ia4.h \
	data/gfx/message/3.ia4.h \
	data/gfx/message/4.ia4.h \
	data/gfx/message/5.ia4.h \
	data/gfx/message/6.ia4.h \
	data/gfx/message/7.ia4.h \
	data/gfx/message/8.ia4.h \
	data/gfx/message/9.ia4.h \
	data/gfx/message/u_a.ia4.h \
	data/gfx/message/u_b.ia4.h \
	data/gfx/message/u_c.ia4.h \
	data/gfx/message/u_d.ia4.h \
	data/gfx/message/u_e.ia4.h \
	data/gfx/message/u_f.ia4.h \
	data/gfx/message/u_g.ia4.h \
	data/gfx/message/u_h.ia4.h \
	data/gfx/message/u_i.ia4.h \
	data/gfx/message/u_j.ia4.h \
	data/gfx/message/u_k.ia4.h \
	data/gfx/message/u_l.ia4.h \
	data/gfx/message/u_m.ia4.h \
	data/gfx/message/u_n.ia4.h \
	data/gfx/message/u_o.ia4.h \
	data/gfx/message/u_p.ia4.h \
	data/gfx/message/u_q.ia4.h \
	data/gfx/message/u_r.ia4.h \
	data/gfx/message/u_s.ia4.h \
	data/gfx/message/u_t.ia4.h \
	data/gfx/message/u_u.ia4.h \
	data/gfx/message/u_v.ia4.h \
	data/gfx/message/u_w.ia4.h \
	data/gfx/message/u_x.ia4.h \
	data/gfx/message/u_y.ia4.h \
	data/gfx/message/u_z.ia4.h \
	data/gfx/message/l_a.ia4.h \
	data/gfx/message/l_b.ia4.h \
	data/gfx/message/l_c.ia4.h \
	data/gfx/message/l_d.ia4.h \
	data/gfx/message/l_e.ia4.h \
	data/gfx/message/l_f.ia4.h \
	data/gfx/message/l_g.ia4.h \
	data/gfx/message/l_h.ia4.h \
	data/gfx/message/l_i.ia4.h \
	data/gfx/message/l_j.ia4.h \
	data/gfx/message/l_k.ia4.h \
	data/gfx/message/l_l.ia4.h \
	data/gfx/message/l_m.ia4.h \
	data/gfx/message/l_n.ia4.h \
	data/gfx/message/l_o.ia4.h \
	data/gfx/message/l_p.ia4.h \
	data/gfx/message/l_q.ia4.h \
	data/gfx/message/l_r.ia4.h \
	data/gfx/message/l_s.ia4.h \
	data/gfx/message/l_t.ia4.h \
	data/gfx/message/l_u.ia4.h \
	data/gfx/message/l_v.ia4.h \
	data/gfx/message/l_w.ia4.h \
	data/gfx/message/l_x.ia4.h \
	data/gfx/message/l_y.ia4.h \
	data/gfx/message/l_z.ia4.h \
	data/gfx/message/arrow.ia4.h \
	data/gfx/message/exclaim.ia4.h \
	data/gfx/message/coin.ia4.h \
	data/gfx/message/multiply.ia4.h \
	data/gfx/message/paren_l.ia4.h \
	data/gfx/message/paren_rl.ia4.h \
	data/gfx/message/paren_r.ia4.h \
	data/gfx/message/tilde.ia4.h \
	data/gfx/message/period.ia4.h \
	data/gfx/message/percent.ia4.h \
	data/gfx/message/bullet.ia4.h \
	data/gfx/message/comma.ia4.h \
	data/gfx/message/apostrophe.ia4.h \
	data/gfx/message/question.ia4.h \
	data/gfx/message/star.ia4.h \
	data/gfx/message/star_outline.ia4.h \
	data/gfx/message/quote_l.ia4.h \
	data/gfx/message/quote_r.ia4.h \
	data/gfx/message/colon.ia4.h \
	data/gfx/message/hyphen.ia4.h \
	data/gfx/message/ampersand.ia4.h \
	data/gfx/message/button_a.ia4.h \
	data/gfx/message/button_b.ia4.h \
	data/gfx/message/button_c.ia4.h \
	data/gfx/message/button_z.ia4.h \
	data/gfx/message/button_r.ia4.h \
	data/gfx/message/button_cu.ia4.h \
	data/gfx/message/button_cd.ia4.h \
	data/gfx/message/button_cl.ia4.h \
	data/gfx/message/button_cr.ia4.h \
	data/gfx/camera/camera.rgba16.h \
	data/gfx/camera/lakitu.rgba16.h \
	data/gfx/camera/cross.rgba16.h \
	data/gfx/camera/up.rgba16.h \
	data/gfx/camera/down.rgba16.h \
	data/select.h \
	data/en_us.h \
	data/course.h \
	data/level.h \
	data/gfx/shadow/circle.ia8.h \
	data/gfx/shadow/square.ia8.h \
	data/gfx/wipe/star.ia8.h \
	data/gfx/wipe/circle.ia8.h \
	data/gfx/wipe/mario.ia8.h \
	data/gfx/wipe/bowser.ia8.h \
	data/gfx/scroll/water_0.rgba16.h \
	data/gfx/scroll/water_1.rgba16.h \
	data/gfx/scroll/water_2.rgba16.h \
	data/gfx/scroll/mist.ia16.h \
	data/gfx/scroll/lava.rgba16.h \
	data/gfx/minimap/arrow.ia8.h

PLAYER_DEP := \
	shape/player/mario/metal.rgba16.h \
	shape/player/mario/button.rgba16.h \
	shape/player/mario/logo.rgba16.h \
	shape/player/mario/sideburn.rgba16.h \
	shape/player/mario/moustache.rgba16.h \
	shape/player/mario/eyes_open.rgba16.h \
	shape/player/mario/eyes_half.rgba16.h \
	shape/player/mario/eyes_closed.rgba16.h \
	shape/player/mario/eyes_left.rgba16.h \
	shape/player/mario/eyes_right.rgba16.h \
	shape/player/mario/eyes_up.rgba16.h \
	shape/player/mario/eyes_down.rgba16.h \
	shape/player/mario/eyes_dead.rgba16.h \
	shape/player/mario/wing_l.rgba16.h \
	shape/player/mario/wing_r.rgba16.h \
	shape/player/mario/metal_wing_l.rgba16.h \
	shape/player/mario/metal_wing_r.rgba16.h \
	$(MARIO_DEP) \
	shape/player/bubble/a.rgba16.h \
	shape/player/bubble/b.rgba16.h \
	shape/player/dust/0.ia16.h \
	shape/player/dust/1.ia16.h \
	shape/player/dust/2.ia16.h \
	shape/player/dust/3.ia16.h \
	shape/player/dust/4.ia16.h \
	shape/player/dust/5.ia16.h \
	shape/player/dust/6.ia16.h \
	shape/player/smoke/smoke.ia16.h \
	shape/player/wave/0.ia16.h \
	shape/player/wave/1.ia16.h \
	shape/player/wave/2.ia16.h \
	shape/player/wave/3.ia16.h \
	shape/player/wave/4.ia16.h \
	shape/player/wave/5.ia16.h \
	shape/player/ripple/0.ia16.h \
	shape/player/ripple/1.ia16.h \
	shape/player/ripple/2.ia16.h \
	shape/player/ripple/3.ia16.h \
	shape/player/sparkle/5.rgba16.h \
	shape/player/sparkle/4.rgba16.h \
	shape/player/sparkle/3.rgba16.h \
	shape/player/sparkle/2.rgba16.h \
	shape/player/sparkle/1.rgba16.h \
	shape/player/sparkle/0.rgba16.h \
	shape/player/splash/0.rgba16.h \
	shape/player/splash/1.rgba16.h \
	shape/player/splash/2.rgba16.h \
	shape/player/splash/3.rgba16.h \
	shape/player/splash/4.rgba16.h \
	shape/player/splash/5.rgba16.h \
	shape/player/splash/6.rgba16.h \
	shape/player/splash/7.rgba16.h \
	shape/player/droplet/droplet.rgba16.h \
	shape/player/glow/0.ia16.h \
	shape/player/glow/1.ia16.h \
	shape/player/glow/2.ia16.h \
	shape/player/glow/3.ia16.h \
	shape/player/glow/4.ia16.h

SHAPE_1A_DEP :=

SHAPE_1B_DEP := \
	shape/1b/bully/horn.rgba16.h \
	shape/1b/bully/body_l.rgba16.h \
	shape/1b/bully/body_r.rgba16.h \
	shape/1b/bully/eye.rgba16.h \
	$(BULLY_DEP) \
	$(BLARGG_DEP)

SHAPE_1C_DEP :=
SHAPE_1D_DEP :=
SHAPE_1E_DEP :=
SHAPE_1F_DEP :=
SHAPE_1G_DEP :=
SHAPE_1H_DEP :=
SHAPE_1I_DEP :=
SHAPE_1J_DEP :=
SHAPE_1K_DEP :=

SHAPE_2A_DEP :=

SHAPE_2B_DEP := \
	shape/2b/skeeter/sphere.rgba16.h \
	shape/2b/skeeter/iris.rgba16.h \
	$(SKEETER_DEP) \
	shape/2b/kelp/0.rgba16.h \
	shape/2b/kelp/1.rgba16.h \
	shape/2b/kelp/2.rgba16.h \
	shape/2b/kelp/3.rgba16.h \
	$(KELP_DEP) \
	shape/2b/watermine/l.rgba16.h \
	shape/2b/watermine/r.rgba16.h \
	shape/2b/watermine/spike.rgba16.h \
	$(WATERMINE_DEP) \
	shape/2b/piranha/piranha.rgba16.h \
	$(PIRANHA_DEP) \
	shape/2b/bub/goggles.rgba16.h \
	shape/2b/bub/fin.rgba16.h \
	shape/2b/bub/eyes.rgba16.h \
	shape/2b/bub/scale.rgba16.h \
	$(BUB_DEP) \
	shape/2b/waterring/waterring.rgba16.h \
	$(WATERRING_DEP) \
	shape/2b/chest/keyhole.rgba16.h \
	shape/2b/chest/inside.rgba16.h \
	shape/2b/chest/latch.rgba16.h \
	shape/2b/chest/outside.rgba16.h \
	$(CHEST_DEP)

SHAPE_2C_DEP :=

SHAPE_2D_DEP := \
	shape/2d/lakitu2/unused.rgba16.h \
	shape/2d/lakitu2/eyes_open.rgba16.h \
	shape/2d/lakitu2/eyes_closed.rgba16.h \
	shape/2d/lakitu2/shell.rgba16.h \
	shape/2d/lakitu2/mouth.rgba16.h \
	shape/2d/lakitu2/lens.rgba16.h \
	$(LAKITU2_DEP) \
	shape/2d/toad/face.rgba16.h \
	shape/2d/toad/spot.rgba16.h \
	$(TOAD_DEP) \
	shape/2d/mips/face.rgba16.h \
	$(MIPS_DEP) \
	shape/2d/boo2/eyes.rgba16.h \
	shape/2d/boo2/mouth.rgba16.h \
	$(BOO2_DEP)

SHAPE_2E_DEP :=
SHAPE_2F_DEP :=

COMMON_DEP :=

GLOBAL_DEP := \
	shape/global/puff/puff.ia16.h \
	shape/global/explosion/0.rgba16.h \
	shape/global/explosion/1.rgba16.h \
	shape/global/explosion/2.rgba16.h \
	shape/global/explosion/3.rgba16.h \
	shape/global/explosion/4.rgba16.h \
	shape/global/explosion/5.rgba16.h \
	shape/global/explosion/6.rgba16.h \
	shape/global/butterfly/wing.rgba16.h \
	$(BUTTERFLY_DEP) \
	shape/global/coin/0.ia16.h \
	shape/global/coin/1.ia16.h \
	shape/global/coin/2.ia16.h \
	shape/global/coin/3.ia16.h \
	shape/global/pipe/side.rgba16.h \
	shape/global/pipe/top.rgba16.h \
	$(PIPE_DEP) \
	shape/global/pipe/map.h \
	shape/global/door/a_face.rgba16.h \
	shape/global/door/a_side.rgba16.h \
	shape/global/door/b_face.rgba16.h \
	shape/global/door/b_side.rgba16.h \
	shape/global/door/d_face.rgba16.h \
	shape/global/door/d_side.rgba16.h \
	shape/global/door/e_face.rgba16.h \
	shape/global/door/e_side.rgba16.h \
	shape/global/door/f_face.rgba16.h \
	shape/global/door/f_side.rgba16.h \
	shape/global/door/star.rgba16.h \
	shape/global/door/star1.rgba16.h \
	shape/global/door/star3.rgba16.h \
	shape/global/door/keyhole.rgba16.h \
	$(DOOR_DEP) \
	$(DOORKEY_DEP) \
	shape/global/flame/0.ia16.h \
	shape/global/flame/1.ia16.h \
	shape/global/flame/2.ia16.h \
	shape/global/flame/3.ia16.h \
	shape/global/flame/4.ia16.h \
	shape/global/flame/5.ia16.h \
	shape/global/flame/6.ia16.h \
	shape/global/flame/7.ia16.h \
	shape/global/fish/fish.rgba16.h \
	$(FISH_DEP) \
	shape/global/stone/stone.rgba16.h \
	shape/global/leaf/leaf.rgba16.h \
	shape/global/map/door.h \
	shape/global/map/13002018.h \
	shape/global/cap/metal.rgba16.h \
	shape/global/cap/logo.rgba16.h \
	shape/global/cap/wing_l.rgba16.h \
	shape/global/cap/wing_r.rgba16.h \
	shape/global/cap/metal_wing_l.rgba16.h \
	shape/global/cap/metal_wing_r.rgba16.h \
	$(CAP_DEP) \
	shape/global/meter/0_l.rgba16.h \
	shape/global/meter/0_r.rgba16.h \
	shape/global/meter/8.rgba16.h \
	shape/global/meter/7.rgba16.h \
	shape/global/meter/6.rgba16.h \
	shape/global/meter/5.rgba16.h \
	shape/global/meter/4.rgba16.h \
	shape/global/meter/3.rgba16.h \
	shape/global/meter/2.rgba16.h \
	shape/global/meter/1.rgba16.h \
	shape/global/1up/1up.rgba16.h \
	shape/global/powerstar/star.rgba16.h \
	shape/global/powerstar/eye.rgba16.h \
	$(POWERSTAR_DEP) \
	shape/global/sand/sand.rgba16.h \
	shape/global/shard/cork.rgba16.h \
	$(SHADESTAR_DEP) \
	shape/global/snow/snow.rgba16.h \
	shape/global/signpost/wood.rgba16.h \
	shape/global/signpost/face.rgba16.h \
	$(SIGNPOST_DEP) \
	shape/global/signpost/map.h \
	shape/global/tree/a_l.rgba16.h \
	shape/global/tree/a_r.rgba16.h \
	shape/global/tree/b.rgba16.h \
	shape/global/tree/c.rgba16.h \
	shape/global/tree/e.rgba16.h \
	$(TREE_DEP)

TITLE_LOGO_DEP := \
	stage/title/wood.rgba16.h \
	stage/title/marble.rgba16.h \
	stage/title/copyright.rgba16.h \
	stage/title/trademark.rgba16.h \
	$(LOGO_DEP) \

TITLE_DEBUG_DEP := \
	$(DEBUG_DEP)

TITLE_BACK_DEP := \
	data/back/title/mario.0.rgba16.h \
	data/back/title/mario.1.rgba16.h \
	data/back/title/mario.2.rgba16.h \
	data/back/title/mario.3.rgba16.h \
	data/back/title/gameover.0.rgba16.h \
	data/back/title/gameover.1.rgba16.h \
	data/back/title/gameover.2.rgba16.h \
	data/back/title/gameover.3.rgba16.h

SELECT_DEP := \
	stage/select/file/light.rgba16.h \
	stage/select/file/shade.rgba16.h \
	stage/select/file/mario.rgba16.h \
	stage/select/file/new.rgba16.h \
	$(FILE_DEP) \
	stage/select/tile/erase.rgba16.h \
	stage/select/tile/copy.rgba16.h \
	stage/select/tile/main.rgba16.h \
	stage/select/tile/score.rgba16.h \
	stage/select/tile/sound.rgba16.h \
	$(TILE_DEP) \
	stage/select/cursor/0.rgba16.h \
	stage/select/cursor/1.rgba16.h \
	stage/select/print/k_hu.rgba16.h \
	stage/select/print/k_xa.rgba16.h \
	stage/select/print/k_i.rgba16.h \
	stage/select/print/k_ru.rgba16.h \
	stage/select/print/k_se.rgba16.h \
	stage/select/print/k_re.rgba16.h \
	stage/select/print/k_ku.rgba16.h \
	stage/select/print/k_to.rgba16.h \
	stage/select/print/h_wo.rgba16.h \
	stage/select/print/k_ko.rgba16.h \
	stage/select/print/k_pi.rgba16.h \
	stage/select/print/chouonpu.rgba16.h \
	stage/select/print/h_su.rgba16.h \
	stage/select/print/h_ru.rgba16.h \
	stage/select/print/h_ke.rgba16.h \
	stage/select/print/k_ma.rgba16.h \
	stage/select/print/k_ri.rgba16.h \
	stage/select/print/k_o.rgba16.h \
	stage/select/print/k_su.rgba16.h \
	stage/select/print/k_a.rgba16.h \
	stage/select/print/h_mi.rgba16.h \
	stage/select/print/h_do.rgba16.h \
	stage/select/print/h_no.rgba16.h \
	stage/select/print/question.rgba16.h \
	stage/select/print/k_sa.rgba16.h \
	stage/select/print/k_u.rgba16.h \
	stage/select/print/k_n.rgba16.h \
	stage/select/print/k_do.rgba16.h \
	stage/select/msg8/0.ia8.h \
	stage/select/msg8/1.ia8.h \
	stage/select/msg8/2.ia8.h \
	stage/select/msg8/3.ia8.h \
	stage/select/msg8/4.ia8.h \
	stage/select/msg8/5.ia8.h \
	stage/select/msg8/6.ia8.h \
	stage/select/msg8/7.ia8.h \
	stage/select/msg8/8.ia8.h \
	stage/select/msg8/9.ia8.h \
	stage/select/msg8/u_a.ia8.h \
	stage/select/msg8/u_b.ia8.h \
	stage/select/msg8/u_c.ia8.h \
	stage/select/msg8/u_d.ia8.h \
	stage/select/msg8/u_e.ia8.h \
	stage/select/msg8/u_f.ia8.h \
	stage/select/msg8/u_g.ia8.h \
	stage/select/msg8/u_h.ia8.h \
	stage/select/msg8/u_i.ia8.h \
	stage/select/msg8/u_j.ia8.h \
	stage/select/msg8/u_k.ia8.h \
	stage/select/msg8/u_l.ia8.h \
	stage/select/msg8/u_m.ia8.h \
	stage/select/msg8/u_n.ia8.h \
	stage/select/msg8/u_o.ia8.h \
	stage/select/msg8/u_p.ia8.h \
	stage/select/msg8/u_q.ia8.h \
	stage/select/msg8/u_r.ia8.h \
	stage/select/msg8/u_s.ia8.h \
	stage/select/msg8/u_t.ia8.h \
	stage/select/msg8/u_u.ia8.h \
	stage/select/msg8/u_v.ia8.h \
	stage/select/msg8/u_w.ia8.h \
	stage/select/msg8/u_x.ia8.h \
	stage/select/msg8/u_y.ia8.h \
	stage/select/msg8/u_z.ia8.h \
	stage/select/msg8/coin.ia8.h \
	stage/select/msg8/multiply.ia8.h \
	stage/select/msg8/star.ia8.h \
	stage/select/msg8/hyphen.ia8.h \
	stage/select/msg8/comma.ia8.h \
	stage/select/msg8/apostrophe.ia8.h \
	stage/select/msg8/exclaim.ia8.h \
	stage/select/msg8/question.ia8.h \
	stage/select/msg8/mario_l.ia8.h \
	stage/select/msg8/mario_r.ia8.h \
	stage/select/msg8/period.ia8.h \
	stage/select/msg8/ampersand.ia8.h \
	stage/select/course/h.rgba16.h \
	stage/select/course/l.rgba16.h \
	stage/select/map.h

BACK_A_DEP := \
	data/back/a/0.rgba16.h \
	data/back/a/1.rgba16.h \
	data/back/a/2.rgba16.h \
	data/back/a/3.rgba16.h \
	data/back/a/4.rgba16.h \
	data/back/a/5.rgba16.h \
	data/back/a/6.rgba16.h \
	data/back/a/7.rgba16.h \
	data/back/a/8.rgba16.h \
	data/back/a/9.rgba16.h \
	data/back/a/10.rgba16.h \
	data/back/a/11.rgba16.h \
	data/back/a/12.rgba16.h \
	data/back/a/13.rgba16.h \
	data/back/a/14.rgba16.h \
	data/back/a/15.rgba16.h \
	data/back/a/16.rgba16.h \
	data/back/a/17.rgba16.h \
	data/back/a/18.rgba16.h \
	data/back/a/19.rgba16.h \
	data/back/a/20.rgba16.h \
	data/back/a/21.rgba16.h \
	data/back/a/22.rgba16.h \
	data/back/a/23.rgba16.h \
	data/back/a/24.rgba16.h \
	data/back/a/25.rgba16.h \
	data/back/a/26.rgba16.h \
	data/back/a/27.rgba16.h \
	data/back/a/28.rgba16.h \
	data/back/a/29.rgba16.h \
	data/back/a/30.rgba16.h \
	data/back/a/31.rgba16.h \
	data/back/a/32.rgba16.h \
	data/back/a/33.rgba16.h \
	data/back/a/34.rgba16.h \
	data/back/a/35.rgba16.h \
	data/back/a/36.rgba16.h \
	data/back/a/37.rgba16.h \
	data/back/a/38.rgba16.h \
	data/back/a/39.rgba16.h \
	data/back/a/40.rgba16.h \
	data/back/a/41.rgba16.h \
	data/back/a/42.rgba16.h \
	data/back/a/43.rgba16.h \
	data/back/a/44.rgba16.h \
	data/back/a/45.rgba16.h \
	data/back/a/46.rgba16.h \
	data/back/a/47.rgba16.h \
	data/back/a/48.rgba16.h \
	data/back/a/49.rgba16.h \
	data/back/a/50.rgba16.h \
	data/back/a/51.rgba16.h \
	data/back/a/52.rgba16.h \
	data/back/a/53.rgba16.h \
	data/back/a/54.rgba16.h \
	data/back/a/55.rgba16.h \
	data/back/a/56.rgba16.h \
	data/back/a/57.rgba16.h \
	data/back/a/58.rgba16.h \
	data/back/a/59.rgba16.h \
	data/back/a/60.rgba16.h \
	data/back/a/61.rgba16.h \
	data/back/a/62.rgba16.h \
	data/back/a/63.rgba16.h

BACK_B_DEP := \
	data/back/b/0.rgba16.h \
	data/back/b/1.rgba16.h \
	data/back/b/2.rgba16.h \
	data/back/b/3.rgba16.h \
	data/back/b/4.rgba16.h \
	data/back/b/5.rgba16.h \
	data/back/b/6.rgba16.h \
	data/back/b/7.rgba16.h \
	data/back/b/8.rgba16.h \
	data/back/b/9.rgba16.h \
	data/back/b/10.rgba16.h \
	data/back/b/11.rgba16.h \
	data/back/b/12.rgba16.h \
	data/back/b/13.rgba16.h \
	data/back/b/14.rgba16.h \
	data/back/b/15.rgba16.h \
	data/back/b/16.rgba16.h \
	data/back/b/17.rgba16.h \
	data/back/b/18.rgba16.h \
	data/back/b/19.rgba16.h \
	data/back/b/20.rgba16.h \
	data/back/b/21.rgba16.h \
	data/back/b/22.rgba16.h \
	data/back/b/23.rgba16.h \
	data/back/b/24.rgba16.h \
	data/back/b/25.rgba16.h \
	data/back/b/26.rgba16.h \
	data/back/b/27.rgba16.h \
	data/back/b/28.rgba16.h \
	data/back/b/29.rgba16.h \
	data/back/b/30.rgba16.h \
	data/back/b/31.rgba16.h \
	data/back/b/32.rgba16.h \
	data/back/b/33.rgba16.h \
	data/back/b/34.rgba16.h \
	data/back/b/35.rgba16.h \
	data/back/b/36.rgba16.h \
	data/back/b/37.rgba16.h \
	data/back/b/38.rgba16.h \
	data/back/b/39.rgba16.h \
	data/back/b/40.rgba16.h \
	data/back/b/41.rgba16.h \
	data/back/b/42.rgba16.h \
	data/back/b/43.rgba16.h \
	data/back/b/44.rgba16.h \
	data/back/b/45.rgba16.h \
	data/back/b/46.rgba16.h \
	data/back/b/47.rgba16.h \
	data/back/b/48.rgba16.h \
	data/back/b/49.rgba16.h \
	data/back/b/50.rgba16.h \
	data/back/b/51.rgba16.h \
	data/back/b/52.rgba16.h \
	data/back/b/53.rgba16.h \
	data/back/b/54.rgba16.h \
	data/back/b/55.rgba16.h \
	data/back/b/56.rgba16.h \
	data/back/b/57.rgba16.h \
	data/back/b/58.rgba16.h \
	data/back/b/59.rgba16.h \
	data/back/b/60.rgba16.h \
	data/back/b/61.rgba16.h \
	data/back/b/62.rgba16.h \
	data/back/b/63.rgba16.h

BACK_C_DEP := \
	data/back/c/0.rgba16.h \
	data/back/c/1.rgba16.h \
	data/back/c/2.rgba16.h \
	data/back/c/3.rgba16.h \
	data/back/c/4.rgba16.h \
	data/back/c/5.rgba16.h \
	data/back/c/6.rgba16.h \
	data/back/c/7.rgba16.h \
	data/back/c/8.rgba16.h \
	data/back/c/9.rgba16.h \
	data/back/c/10.rgba16.h \
	data/back/c/11.rgba16.h \
	data/back/c/12.rgba16.h \
	data/back/c/13.rgba16.h \
	data/back/c/14.rgba16.h \
	data/back/c/15.rgba16.h \
	data/back/c/16.rgba16.h \
	data/back/c/17.rgba16.h \
	data/back/c/18.rgba16.h \
	data/back/c/19.rgba16.h \
	data/back/c/20.rgba16.h \
	data/back/c/21.rgba16.h \
	data/back/c/22.rgba16.h \
	data/back/c/23.rgba16.h \
	data/back/c/24.rgba16.h \
	data/back/c/25.rgba16.h \
	data/back/c/26.rgba16.h \
	data/back/c/27.rgba16.h \
	data/back/c/28.rgba16.h \
	data/back/c/29.rgba16.h \
	data/back/c/30.rgba16.h \
	data/back/c/31.rgba16.h \
	data/back/c/32.rgba16.h \
	data/back/c/33.rgba16.h \
	data/back/c/34.rgba16.h \
	data/back/c/35.rgba16.h \
	data/back/c/36.rgba16.h \
	data/back/c/37.rgba16.h \
	data/back/c/38.rgba16.h \
	data/back/c/39.rgba16.h \
	data/back/c/40.rgba16.h

BACK_D_DEP := \
	data/back/d/0.rgba16.h \
	data/back/d/1.rgba16.h \
	data/back/d/2.rgba16.h \
	data/back/d/3.rgba16.h \
	data/back/d/4.rgba16.h \
	data/back/d/5.rgba16.h \
	data/back/d/6.rgba16.h \
	data/back/d/7.rgba16.h \
	data/back/d/8.rgba16.h \
	data/back/d/9.rgba16.h \
	data/back/d/10.rgba16.h \
	data/back/d/11.rgba16.h \
	data/back/d/12.rgba16.h \
	data/back/d/13.rgba16.h \
	data/back/d/14.rgba16.h \
	data/back/d/15.rgba16.h \
	data/back/d/16.rgba16.h \
	data/back/d/17.rgba16.h \
	data/back/d/18.rgba16.h \
	data/back/d/19.rgba16.h \
	data/back/d/20.rgba16.h \
	data/back/d/21.rgba16.h \
	data/back/d/22.rgba16.h \
	data/back/d/23.rgba16.h \
	data/back/d/24.rgba16.h \
	data/back/d/25.rgba16.h \
	data/back/d/26.rgba16.h \
	data/back/d/27.rgba16.h \
	data/back/d/28.rgba16.h \
	data/back/d/29.rgba16.h \
	data/back/d/30.rgba16.h \
	data/back/d/31.rgba16.h \
	data/back/d/32.rgba16.h \
	data/back/d/33.rgba16.h \
	data/back/d/34.rgba16.h \
	data/back/d/35.rgba16.h \
	data/back/d/36.rgba16.h \
	data/back/d/37.rgba16.h \
	data/back/d/38.rgba16.h \
	data/back/d/39.rgba16.h \
	data/back/d/40.rgba16.h \
	data/back/d/41.rgba16.h \
	data/back/d/42.rgba16.h \
	data/back/d/43.rgba16.h \
	data/back/d/44.rgba16.h \
	data/back/d/45.rgba16.h \
	data/back/d/46.rgba16.h \
	data/back/d/47.rgba16.h \
	data/back/d/48.rgba16.h

BACK_E_DEP := \
	data/back/e/0.rgba16.h \
	data/back/e/1.rgba16.h \
	data/back/e/2.rgba16.h \
	data/back/e/3.rgba16.h \
	data/back/e/4.rgba16.h \
	data/back/e/5.rgba16.h \
	data/back/e/6.rgba16.h \
	data/back/e/7.rgba16.h \
	data/back/e/8.rgba16.h \
	data/back/e/9.rgba16.h \
	data/back/e/10.rgba16.h \
	data/back/e/11.rgba16.h \
	data/back/e/12.rgba16.h \
	data/back/e/13.rgba16.h \
	data/back/e/14.rgba16.h \
	data/back/e/15.rgba16.h \
	data/back/e/16.rgba16.h \
	data/back/e/17.rgba16.h \
	data/back/e/18.rgba16.h \
	data/back/e/19.rgba16.h \
	data/back/e/20.rgba16.h \
	data/back/e/21.rgba16.h \
	data/back/e/22.rgba16.h \
	data/back/e/23.rgba16.h \
	data/back/e/24.rgba16.h \
	data/back/e/25.rgba16.h \
	data/back/e/26.rgba16.h \
	data/back/e/27.rgba16.h \
	data/back/e/28.rgba16.h \
	data/back/e/29.rgba16.h \
	data/back/e/30.rgba16.h \
	data/back/e/31.rgba16.h \
	data/back/e/32.rgba16.h \
	data/back/e/33.rgba16.h \
	data/back/e/34.rgba16.h \
	data/back/e/35.rgba16.h \
	data/back/e/36.rgba16.h \
	data/back/e/37.rgba16.h \
	data/back/e/38.rgba16.h \
	data/back/e/39.rgba16.h \
	data/back/e/40.rgba16.h \
	data/back/e/41.rgba16.h \
	data/back/e/42.rgba16.h \
	data/back/e/43.rgba16.h \
	data/back/e/44.rgba16.h \
	data/back/e/45.rgba16.h \
	data/back/e/46.rgba16.h \
	data/back/e/47.rgba16.h \
	data/back/e/48.rgba16.h \
	data/back/e/49.rgba16.h \
	data/back/e/50.rgba16.h \
	data/back/e/51.rgba16.h \
	data/back/e/52.rgba16.h \
	data/back/e/53.rgba16.h \
	data/back/e/54.rgba16.h \
	data/back/e/55.rgba16.h \
	data/back/e/56.rgba16.h \
	data/back/e/57.rgba16.h \
	data/back/e/58.rgba16.h \
	data/back/e/59.rgba16.h \
	data/back/e/60.rgba16.h \
	data/back/e/61.rgba16.h \
	data/back/e/62.rgba16.h \
	data/back/e/63.rgba16.h

BACK_F_DEP := \
	data/back/f/0.rgba16.h \
	data/back/f/1.rgba16.h \
	data/back/f/2.rgba16.h \
	data/back/f/3.rgba16.h \
	data/back/f/4.rgba16.h \
	data/back/f/5.rgba16.h \
	data/back/f/6.rgba16.h \
	data/back/f/7.rgba16.h \
	data/back/f/8.rgba16.h \
	data/back/f/9.rgba16.h \
	data/back/f/10.rgba16.h \
	data/back/f/11.rgba16.h \
	data/back/f/12.rgba16.h \
	data/back/f/13.rgba16.h \
	data/back/f/14.rgba16.h \
	data/back/f/15.rgba16.h \
	data/back/f/16.rgba16.h \
	data/back/f/17.rgba16.h \
	data/back/f/18.rgba16.h \
	data/back/f/19.rgba16.h \
	data/back/f/20.rgba16.h \
	data/back/f/21.rgba16.h \
	data/back/f/22.rgba16.h \
	data/back/f/23.rgba16.h \
	data/back/f/24.rgba16.h \
	data/back/f/25.rgba16.h \
	data/back/f/26.rgba16.h \
	data/back/f/27.rgba16.h \
	data/back/f/28.rgba16.h \
	data/back/f/29.rgba16.h \
	data/back/f/30.rgba16.h \
	data/back/f/31.rgba16.h \
	data/back/f/32.rgba16.h \
	data/back/f/33.rgba16.h \
	data/back/f/34.rgba16.h \
	data/back/f/35.rgba16.h \
	data/back/f/36.rgba16.h \
	data/back/f/37.rgba16.h \
	data/back/f/38.rgba16.h \
	data/back/f/39.rgba16.h \
	data/back/f/40.rgba16.h \
	data/back/f/41.rgba16.h \
	data/back/f/42.rgba16.h \
	data/back/f/43.rgba16.h \
	data/back/f/44.rgba16.h \
	data/back/f/45.rgba16.h \
	data/back/f/46.rgba16.h \
	data/back/f/47.rgba16.h \
	data/back/f/48.rgba16.h \
	data/back/f/49.rgba16.h \
	data/back/f/50.rgba16.h \
	data/back/f/51.rgba16.h \
	data/back/f/52.rgba16.h \
	data/back/f/53.rgba16.h \
	data/back/f/54.rgba16.h \
	data/back/f/55.rgba16.h \
	data/back/f/56.rgba16.h \
	data/back/f/57.rgba16.h \
	data/back/f/58.rgba16.h \
	data/back/f/59.rgba16.h \
	data/back/f/60.rgba16.h \
	data/back/f/61.rgba16.h \
	data/back/f/62.rgba16.h \
	data/back/f/63.rgba16.h

BACK_G_DEP := \
	data/back/g/0.rgba16.h \
	data/back/g/1.rgba16.h \
	data/back/g/2.rgba16.h \
	data/back/g/3.rgba16.h \
	data/back/g/4.rgba16.h \
	data/back/g/5.rgba16.h \
	data/back/g/6.rgba16.h \
	data/back/g/7.rgba16.h \
	data/back/g/8.rgba16.h \
	data/back/g/9.rgba16.h \
	data/back/g/10.rgba16.h \
	data/back/g/11.rgba16.h \
	data/back/g/12.rgba16.h \
	data/back/g/13.rgba16.h \
	data/back/g/14.rgba16.h \
	data/back/g/15.rgba16.h \
	data/back/g/16.rgba16.h \
	data/back/g/17.rgba16.h \
	data/back/g/18.rgba16.h \
	data/back/g/19.rgba16.h \
	data/back/g/20.rgba16.h \
	data/back/g/21.rgba16.h \
	data/back/g/22.rgba16.h \
	data/back/g/23.rgba16.h \
	data/back/g/24.rgba16.h \
	data/back/g/25.rgba16.h \
	data/back/g/26.rgba16.h \
	data/back/g/27.rgba16.h \
	data/back/g/28.rgba16.h \
	data/back/g/29.rgba16.h \
	data/back/g/30.rgba16.h \
	data/back/g/31.rgba16.h \
	data/back/g/32.rgba16.h \
	data/back/g/33.rgba16.h \
	data/back/g/34.rgba16.h \
	data/back/g/35.rgba16.h \
	data/back/g/36.rgba16.h \
	data/back/g/37.rgba16.h \
	data/back/g/38.rgba16.h \
	data/back/g/39.rgba16.h \
	data/back/g/40.rgba16.h \
	data/back/g/41.rgba16.h \
	data/back/g/42.rgba16.h \
	data/back/g/43.rgba16.h \
	data/back/g/44.rgba16.h \
	data/back/g/45.rgba16.h \
	data/back/g/46.rgba16.h \
	data/back/g/47.rgba16.h \
	data/back/g/48.rgba16.h \
	data/back/g/49.rgba16.h \
	data/back/g/50.rgba16.h \
	data/back/g/51.rgba16.h \
	data/back/g/52.rgba16.h \
	data/back/g/53.rgba16.h \
	data/back/g/54.rgba16.h \
	data/back/g/55.rgba16.h \
	data/back/g/56.rgba16.h \
	data/back/g/57.rgba16.h \
	data/back/g/58.rgba16.h \
	data/back/g/59.rgba16.h \
	data/back/g/60.rgba16.h \
	data/back/g/61.rgba16.h \
	data/back/g/62.rgba16.h \
	data/back/g/63.rgba16.h

BACK_H_DEP := \
	data/back/h/0.rgba16.h \
	data/back/h/1.rgba16.h \
	data/back/h/2.rgba16.h \
	data/back/h/3.rgba16.h \
	data/back/h/4.rgba16.h \
	data/back/h/5.rgba16.h \
	data/back/h/6.rgba16.h \
	data/back/h/7.rgba16.h \
	data/back/h/8.rgba16.h \
	data/back/h/9.rgba16.h \
	data/back/h/10.rgba16.h \
	data/back/h/11.rgba16.h \
	data/back/h/12.rgba16.h \
	data/back/h/13.rgba16.h \
	data/back/h/14.rgba16.h \
	data/back/h/15.rgba16.h \
	data/back/h/16.rgba16.h \
	data/back/h/17.rgba16.h \
	data/back/h/18.rgba16.h \
	data/back/h/19.rgba16.h \
	data/back/h/20.rgba16.h \
	data/back/h/21.rgba16.h \
	data/back/h/22.rgba16.h \
	data/back/h/23.rgba16.h \
	data/back/h/24.rgba16.h \
	data/back/h/25.rgba16.h \
	data/back/h/26.rgba16.h \
	data/back/h/27.rgba16.h \
	data/back/h/28.rgba16.h \
	data/back/h/29.rgba16.h \
	data/back/h/30.rgba16.h \
	data/back/h/31.rgba16.h \
	data/back/h/32.rgba16.h \
	data/back/h/33.rgba16.h \
	data/back/h/34.rgba16.h \
	data/back/h/35.rgba16.h \
	data/back/h/36.rgba16.h \
	data/back/h/37.rgba16.h \
	data/back/h/38.rgba16.h \
	data/back/h/39.rgba16.h \
	data/back/h/40.rgba16.h

BACK_I_DEP := \
	data/back/i/0.rgba16.h \
	data/back/i/1.rgba16.h \
	data/back/i/2.rgba16.h \
	data/back/i/3.rgba16.h \
	data/back/i/4.rgba16.h \
	data/back/i/5.rgba16.h \
	data/back/i/6.rgba16.h \
	data/back/i/7.rgba16.h \
	data/back/i/8.rgba16.h \
	data/back/i/9.rgba16.h \
	data/back/i/10.rgba16.h \
	data/back/i/11.rgba16.h \
	data/back/i/12.rgba16.h \
	data/back/i/13.rgba16.h \
	data/back/i/14.rgba16.h \
	data/back/i/15.rgba16.h \
	data/back/i/16.rgba16.h \
	data/back/i/17.rgba16.h \
	data/back/i/18.rgba16.h \
	data/back/i/19.rgba16.h \
	data/back/i/20.rgba16.h \
	data/back/i/21.rgba16.h \
	data/back/i/22.rgba16.h \
	data/back/i/23.rgba16.h \
	data/back/i/24.rgba16.h \
	data/back/i/25.rgba16.h \
	data/back/i/26.rgba16.h \
	data/back/i/27.rgba16.h \
	data/back/i/28.rgba16.h \
	data/back/i/29.rgba16.h \
	data/back/i/30.rgba16.h \
	data/back/i/31.rgba16.h \
	data/back/i/32.rgba16.h \
	data/back/i/33.rgba16.h \
	data/back/i/34.rgba16.h \
	data/back/i/35.rgba16.h \
	data/back/i/36.rgba16.h \
	data/back/i/37.rgba16.h \
	data/back/i/38.rgba16.h \
	data/back/i/39.rgba16.h \
	data/back/i/40.rgba16.h \
	data/back/i/41.rgba16.h \
	data/back/i/42.rgba16.h \
	data/back/i/43.rgba16.h \
	data/back/i/44.rgba16.h \
	data/back/i/45.rgba16.h \
	data/back/i/46.rgba16.h \
	data/back/i/47.rgba16.h \
	data/back/i/48.rgba16.h \
	data/back/i/49.rgba16.h \
	data/back/i/50.rgba16.h \
	data/back/i/51.rgba16.h \
	data/back/i/52.rgba16.h \
	data/back/i/53.rgba16.h \
	data/back/i/54.rgba16.h \
	data/back/i/55.rgba16.h \
	data/back/i/56.rgba16.h \
	data/back/i/57.rgba16.h \
	data/back/i/58.rgba16.h \
	data/back/i/59.rgba16.h \
	data/back/i/60.rgba16.h \
	data/back/i/61.rgba16.h \
	data/back/i/62.rgba16.h \
	data/back/i/63.rgba16.h

BACK_J_DEP := \
	data/back/j/0.rgba16.h \
	data/back/j/1.rgba16.h \
	data/back/j/2.rgba16.h \
	data/back/j/3.rgba16.h \
	data/back/j/4.rgba16.h \
	data/back/j/5.rgba16.h \
	data/back/j/6.rgba16.h \
	data/back/j/7.rgba16.h \
	data/back/j/8.rgba16.h \
	data/back/j/9.rgba16.h \
	data/back/j/10.rgba16.h \
	data/back/j/11.rgba16.h \
	data/back/j/12.rgba16.h \
	data/back/j/13.rgba16.h \
	data/back/j/14.rgba16.h \
	data/back/j/15.rgba16.h \
	data/back/j/16.rgba16.h \
	data/back/j/17.rgba16.h \
	data/back/j/18.rgba16.h \
	data/back/j/19.rgba16.h \
	data/back/j/20.rgba16.h \
	data/back/j/21.rgba16.h \
	data/back/j/22.rgba16.h \
	data/back/j/23.rgba16.h \
	data/back/j/24.rgba16.h \
	data/back/j/25.rgba16.h \
	data/back/j/26.rgba16.h \
	data/back/j/27.rgba16.h \
	data/back/j/28.rgba16.h \
	data/back/j/29.rgba16.h \
	data/back/j/30.rgba16.h \
	data/back/j/31.rgba16.h \
	data/back/j/32.rgba16.h \
	data/back/j/33.rgba16.h \
	data/back/j/34.rgba16.h \
	data/back/j/35.rgba16.h \
	data/back/j/36.rgba16.h \
	data/back/j/37.rgba16.h \
	data/back/j/38.rgba16.h \
	data/back/j/39.rgba16.h \
	data/back/j/40.rgba16.h \
	data/back/j/41.rgba16.h \
	data/back/j/42.rgba16.h \
	data/back/j/43.rgba16.h \
	data/back/j/44.rgba16.h \
	data/back/j/45.rgba16.h \
	data/back/j/46.rgba16.h \
	data/back/j/47.rgba16.h \
	data/back/j/48.rgba16.h \
	data/back/j/49.rgba16.h \
	data/back/j/50.rgba16.h \
	data/back/j/51.rgba16.h \
	data/back/j/52.rgba16.h \
	data/back/j/53.rgba16.h \
	data/back/j/54.rgba16.h \
	data/back/j/55.rgba16.h \
	data/back/j/56.rgba16.h \
	data/back/j/57.rgba16.h \
	data/back/j/58.rgba16.h \
	data/back/j/59.rgba16.h \
	data/back/j/60.rgba16.h \
	data/back/j/61.rgba16.h \
	data/back/j/62.rgba16.h \
	data/back/j/63.rgba16.h

TEXTURE_A_DEP := \
	data/texture/a0.rgba16.h \
	data/texture/a1.rgba16.h \
	data/texture/a2.rgba16.h \
	data/texture/a3.rgba16.h \
	data/texture/a4.rgba16.h \
	data/texture/a5.rgba16.h \
	data/texture/a6.rgba16.h \
	data/texture/a7.rgba16.h \
	data/texture/a8.rgba16.h \
	data/texture/a9.rgba16.h \
	data/texture/a10.rgba16.h \
	data/texture/a11.rgba16.h \
	data/texture/a12.rgba16.h \
	data/texture/a13.rgba16.h \
	data/texture/a14.rgba16.h \
	data/texture/a15.rgba16.h \
	data/texture/a16.rgba16.h \
	data/texture/a17.rgba16.h \
	data/texture/a18.rgba16.h \
	data/texture/a19.rgba16.h \
	data/texture/a20.rgba16.h \
	data/texture/a21.rgba16.h \
	data/texture/a22.rgba16.h \
	data/texture/a23.rgba16.h

TEXTURE_B_DEP := \
	data/texture/b0.rgba16.h \
	data/texture/b1.rgba16.h \
	data/texture/b2.rgba16.h \
	data/texture/b3.rgba16.h \
	data/texture/b4.rgba16.h \
	data/texture/b5.rgba16.h \
	data/texture/b6.rgba16.h \
	data/texture/b7.rgba16.h \
	data/texture/b8.rgba16.h \
	data/texture/b9.rgba16.h \
	data/texture/b10.rgba16.h \
	data/texture/b11.rgba16.h \
	data/texture/b12.rgba16.h \
	data/texture/b13.rgba16.h \
	data/texture/b14.rgba16.h \
	data/texture/b15_g17.ia16.h \
	data/texture/b16.ia16.h \
	data/texture/b17.ia16.h

TEXTURE_C_DEP := \
	data/texture/c0.rgba16.h \
	data/texture/c1.rgba16.h \
	data/texture/c2.rgba16.h \
	data/texture/c3.rgba16.h \
	data/texture/c4.rgba16.h \
	data/texture/c5.rgba16.h \
	data/texture/c6.rgba16.h \
	data/texture/c7.rgba16.h \
	data/texture/c8.rgba16.h \
	data/texture/c9.rgba16.h \
	data/texture/c10.rgba16.h \
	data/texture/c11.rgba16.h \
	data/texture/c12.rgba16.h \
	data/texture/c13.rgba16.h \
	data/texture/c14.rgba16.h \
	data/texture/c15.rgba16.h \
	data/texture/c16.rgba16.h \
	data/texture/c17.rgba16.h \
	data/texture/c18.rgba16.h \
	data/texture/c19.rgba16.h \
	data/texture/c20.rgba16.h \
	data/texture/c21_j22_k22.ia16.h

TEXTURE_D_DEP := \
	data/texture/d0.rgba16.h \
	data/texture/d1.rgba16.h \
	data/texture/d2.rgba16.h \
	data/texture/d3.rgba16.h \
	data/texture/d4.rgba16.h \
	data/texture/d5.rgba16.h \
	data/texture/d6.rgba16.h \
	data/texture/d7.rgba16.h \
	data/texture/d8.rgba16.h \
	data/texture/d9.rgba16.h \
	data/texture/d10.rgba16.h \
	data/texture/d11.rgba16.h \
	data/texture/d12.rgba16.h \
	data/texture/d13.rgba16.h \
	data/texture/d14.rgba16.h

TEXTURE_E_DEP := \
	data/texture/e0.rgba16.h \
	data/texture/e1.rgba16.h \
	data/texture/e2.rgba16.h \
	data/texture/e3.rgba16.h \
	data/texture/e4.rgba16.h \
	data/texture/e5.rgba16.h \
	data/texture/e6.rgba16.h \
	data/texture/e7.rgba16.h \
	data/texture/e8_j12.rgba16.h \
	data/texture/e9.rgba16.h \
	data/texture/e10_i18.rgba16.h \
	data/texture/e11.rgba16.h \
	data/texture/e12.rgba16.h \
	data/texture/e13.rgba16.h \
	data/texture/e14.rgba16.h

TEXTURE_F_DEP := \
	data/texture/f0.rgba16.h \
	data/texture/f1.rgba16.h \
	data/texture/f2.rgba16.h \
	data/texture/f3.rgba16.h \
	data/texture/f4.rgba16.h \
	data/texture/f5.rgba16.h \
	data/texture/f6.rgba16.h \
	data/texture/f7.rgba16.h \
	data/texture/f8.rgba16.h \
	data/texture/f9.rgba16.h \
	data/texture/f10.rgba16.h \
	data/texture/f11.rgba16.h \
	data/texture/f12.rgba16.h \
	data/texture/f13.rgba16.h \
	data/texture/f14.rgba16.h \
	data/texture/f15.rgba16.h \
	data/texture/f16.ia16.h \
	data/texture/f17.ia16.h

TEXTURE_G_DEP := \
	data/texture/g0.rgba16.h \
	data/texture/g1.rgba16.h \
	data/texture/g2.rgba16.h \
	data/texture/g3.rgba16.h \
	data/texture/g4.rgba16.h \
	data/texture/g5.rgba16.h \
	data/texture/g6.rgba16.h \
	data/texture/g7.rgba16.h \
	data/texture/g8.rgba16.h \
	data/texture/g9.rgba16.h \
	data/texture/g10.rgba16.h \
	data/texture/g11.rgba16.h \
	data/texture/g12.rgba16.h \
	data/texture/g13.rgba16.h \
	data/texture/g14.rgba16.h \
	data/texture/g15.rgba16.h \
	data/texture/g16.ia16.h \
	data/texture/b15_g17.ia16.h

TEXTURE_H_DEP := \
	data/texture/h0.rgba16.h \
	data/texture/h1_l6.rgba16.h \
	data/texture/h2.rgba16.h \
	data/texture/h3.rgba16.h \
	data/texture/h4.rgba16.h \
	data/texture/h5.rgba16.h \
	data/texture/h6.rgba16.h \
	data/texture/h7.rgba16.h \
	data/texture/h8.rgba16.h \
	data/texture/h9.rgba16.h \
	data/texture/h10.rgba16.h \
	data/texture/h11.rgba16.h \
	data/texture/h12.rgba16.h \
	data/texture/h13.rgba16.h \
	data/texture/h14.rgba16.h \
	data/texture/h15.rgba16.h \
	data/texture/h16.rgba16.h

TEXTURE_I_DEP := \
	data/texture/i0.rgba16.h \
	data/texture/i1.rgba16.h \
	data/texture/i2.rgba16.h \
	data/texture/i3.rgba16.h \
	data/texture/i4.rgba16.h \
	data/texture/i5.rgba16.h \
	data/texture/i6.rgba16.h \
	data/texture/i7.rgba16.h \
	data/texture/i8.rgba16.h \
	data/texture/i9.rgba16.h \
	data/texture/i10.rgba16.h \
	data/texture/i11.rgba16.h \
	data/texture/i12.rgba16.h \
	data/texture/i13.rgba16.h \
	data/texture/i14.rgba16.h \
	data/texture/i15.rgba16.h \
	data/texture/i16.rgba16.h \
	data/texture/i17.rgba16.h \
	data/texture/e10_i18.rgba16.h \
	data/texture/i19.rgba16.h \
	data/texture/i20.rgba16.h \
	data/texture/i21.rgba16.h \
	data/texture/i22.rgba16.h

TEXTURE_J_DEP := \
	data/texture/j0.rgba16.h \
	data/texture/j1.rgba16.h \
	data/texture/j2.rgba16.h \
	data/texture/j3.rgba16.h \
	data/texture/j4.rgba16.h \
	data/texture/j5.rgba16.h \
	data/texture/j6.rgba16.h \
	data/texture/j7.rgba16.h \
	data/texture/j8.rgba16.h \
	data/texture/j9.rgba16.h \
	data/texture/j10.rgba16.h \
	data/texture/j11.rgba16.h \
	data/texture/e8_j12.rgba16.h \
	data/texture/j13.rgba16.h \
	data/texture/j14.rgba16.h \
	data/texture/j15.rgba16.h \
	data/texture/j16.rgba16.h \
	data/texture/j17.rgba16.h \
	data/texture/j18.rgba16.h \
	data/texture/j19.rgba16.h \
	data/texture/j20.rgba16.h \
	data/texture/j21.rgba16.h \
	data/texture/c21_j22_k22.ia16.h \
	data/texture/j23.ia16.h

TEXTURE_K_DEP := \
	data/texture/k0.rgba16.h \
	data/texture/k1.rgba16.h \
	data/texture/k2.rgba16.h \
	data/texture/k3.rgba16.h \
	data/texture/k4.rgba16.h \
	data/texture/k5.rgba16.h \
	data/texture/k6.rgba16.h \
	data/texture/k7.rgba16.h \
	data/texture/k8.rgba16.h \
	data/texture/k9.rgba16.h \
	data/texture/k10.rgba16.h \
	data/texture/k11.rgba16.h \
	data/texture/k12.rgba16.h \
	data/texture/k13.rgba16.h \
	data/texture/k14.rgba16.h \
	data/texture/k15.rgba16.h \
	data/texture/k16.rgba16.h \
	data/texture/k17.rgba16.h \
	data/texture/k18.rgba16.h \
	data/texture/k19.rgba16.h \
	data/texture/k20.rgba16.h \
	data/texture/k21.rgba16.h \
	data/texture/c21_j22_k22.ia16.h

TEXTURE_L_DEP := \
	data/texture/l0.rgba16.h \
	data/texture/l1.rgba16.h \
	data/texture/l2.rgba16.h \
	data/texture/l3.rgba16.h \
	data/texture/l4.rgba16.h \
	data/texture/l5.rgba16.h \
	data/texture/h1_l6.rgba16.h \
	data/texture/l7.rgba16.h \
	data/texture/l8.rgba16.h \
	data/texture/l9.rgba16.h \
	data/texture/l10.rgba16.h \
	data/texture/l11.rgba16.h \
	data/texture/l12.rgba16.h \
	data/texture/l13.rgba16.h \
	data/texture/l14.rgba16.h \
	data/texture/l15.rgba16.h \
	data/texture/l16.rgba16.h \
	data/texture/l17.rgba16.h

WEATHER_DEP := \
	data/weather/flower/0.rgba16.h \
	data/weather/flower/1.rgba16.h \
	data/weather/flower/2.rgba16.h \
	data/weather/flower/3.rgba16.h \
	data/weather/lava/0.rgba16.h \
	data/weather/lava/1.rgba16.h \
	data/weather/lava/2.rgba16.h \
	data/weather/lava/3.rgba16.h \
	data/weather/lava/4.rgba16.h \
	data/weather/lava/5.rgba16.h \
	data/weather/lava/6.rgba16.h \
	data/weather/lava/7.rgba16.h \
	data/weather/bubble/0.rgba16.h \
	data/weather/snow/a.rgba16.h \
	data/weather/snow/b.rgba16.h

BBH_DEP :=
CCM_DEP :=
INSIDE_DEP :=
HMC_DEP :=
SSL_DEP :=

BOB_DEP := \
	stage/bob/0.rgba16.h \
	stage/bob/1.rgba16.h \
	stage/bob/2.rgba16.h \
	stage/bob/3.rgba16.h \
	stage/bob/4.rgba16.h \
	$(BATTLEFIELD_DEP) \
	$(BOB_54_DEP) \
	$(BOB_55_DEP) \
	$(BOB_56_DEP) \
	stage/bob/battlefield/map.h \
	stage/bob/54/map.h \
	stage/bob/55/map.h \
	stage/bob/56/map.h

SL_DEP :=
WDW_DEP :=
JRB_DEP :=
THI_DEP :=
TTC_DEP :=
RR_DEP :=
GROUNDS_DEP :=
BITDW_DEP :=
VCUTM_DEP :=
BITFS_DEP :=
SA_DEP :=
BITS_DEP :=
LLL_DEP :=
DDD_DEP :=
WF_DEP :=

ENDING_DEP := \
	stage/ending/0.rgba16.h \
	stage/ending/1.rgba16.h \
	stage/ending/2.rgba16.h \
	stage/ending/3.rgba16.h \
	stage/ending/4.rgba16.h \
	stage/ending/5.rgba16.h \
	stage/ending/6.rgba16.h \
	stage/ending/7.rgba16.h \
	stage/ending/8.rgba16.h \
	stage/ending/9.rgba16.h \
	stage/ending/10.rgba16.h \
	stage/ending/11.rgba16.h \
	stage/ending/12.rgba16.h \
	stage/ending/13.rgba16.h \
	stage/ending/14.rgba16.h \
	stage/ending/15.rgba16.h \
	stage/ending/16.rgba16.h \
	stage/ending/17.rgba16.h \
	stage/ending/18.rgba16.h \
	stage/ending/19.rgba16.h \
	stage/ending/20.rgba16.h \
	stage/ending/21.rgba16.h \
	stage/ending/22.rgba16.h \
	stage/ending/23.rgba16.h \
	stage/ending/24.rgba16.h \
	stage/ending/25.rgba16.h \
	stage/ending/26.rgba16.h \
	stage/ending/27.rgba16.h \
	stage/ending/28.rgba16.h \
	stage/ending/29.rgba16.h \
	stage/ending/30.rgba16.h \
	stage/ending/31.rgba16.h \
	stage/ending/32.rgba16.h \
	stage/ending/33.rgba16.h \
	stage/ending/34.rgba16.h \
	stage/ending/35.rgba16.h \
	stage/ending/36.rgba16.h \
	stage/ending/37.rgba16.h \
	stage/ending/38.rgba16.h \
	stage/ending/39.rgba16.h \
	stage/ending/40.rgba16.h \
	stage/ending/41.rgba16.h \
	stage/ending/42.rgba16.h \
	stage/ending/43.rgba16.h \
	stage/ending/44.rgba16.h \
	stage/ending/45.rgba16.h \
	stage/ending/46.rgba16.h \
	stage/ending/47.rgba16.h

COURTYARD_DEP :=
PSS_DEP :=
COTMC_DEP :=
TOTWC_DEP :=
BITDWA_DEP :=
WMOTR_DEP :=
BITFSA_DEP :=
BITSA_DEP :=
TTM_DEP :=

DEP := \
	src/str.h \
	src/803315E4.h \
	$(GFX_DEP) \
	$(PLAYER_DEP) \
	$(SHAPE_1A_DEP) \
	$(SHAPE_1B_DEP) \
	$(SHAPE_1C_DEP) \
	$(SHAPE_1D_DEP) \
	$(SHAPE_1E_DEP) \
	$(SHAPE_1F_DEP) \
	$(SHAPE_1G_DEP) \
	$(SHAPE_1H_DEP) \
	$(SHAPE_1I_DEP) \
	$(SHAPE_1J_DEP) \
	$(SHAPE_1K_DEP) \
	$(SHAPE_2A_DEP) \
	$(SHAPE_2B_DEP) \
	$(SHAPE_2C_DEP) \
	$(SHAPE_2D_DEP) \
	$(SHAPE_2E_DEP) \
	$(SHAPE_2F_DEP) \
	$(COMMON_DEP) \
	$(GLOBAL_DEP) \
	$(TITLE_LOGO_DEP) \
	$(TITLE_DEBUG_DEP) \
	$(TITLE_BACK_DEP) \
	$(SELECT_DEP) \
	$(BACK_A_DEP) \
	$(BACK_B_DEP) \
	$(BACK_C_DEP) \
	$(BACK_D_DEP) \
	$(BACK_E_DEP) \
	$(BACK_F_DEP) \
	$(BACK_G_DEP) \
	$(BACK_H_DEP) \
	$(BACK_I_DEP) \
	$(BACK_J_DEP) \
	$(TEXTURE_A_DEP) \
	$(TEXTURE_B_DEP) \
	$(TEXTURE_C_DEP) \
	$(TEXTURE_D_DEP) \
	$(TEXTURE_E_DEP) \
	$(TEXTURE_F_DEP) \
	$(TEXTURE_G_DEP) \
	$(TEXTURE_H_DEP) \
	$(TEXTURE_I_DEP) \
	$(TEXTURE_J_DEP) \
	$(TEXTURE_K_DEP) \
	$(TEXTURE_L_DEP) \
	$(WEATHER_DEP) \
	$(BBH_DEP) \
	$(CCM_DEP) \
	$(INSIDE_DEP) \
	$(HMC_DEP) \
	$(SSL_DEP) \
	$(BOB_DEP) \
	$(SL_DEP) \
	$(WDW_DEP) \
	$(JRB_DEP) \
	$(THI_DEP) \
	$(TTC_DEP) \
	$(RR_DEP) \
	$(GROUNDS_DEP) \
	$(BITDW_DEP) \
	$(VCUTM_DEP) \
	$(BITFS_DEP) \
	$(SA_DEP) \
	$(BITS_DEP) \
	$(LLL_DEP) \
	$(DDD_DEP) \
	$(WF_DEP) \
	$(ENDING_DEP) \
	$(COURTYARD_DEP) \
	$(PSS_DEP) \
	$(COTMC_DEP) \
	$(TOTWC_DEP) \
	$(BITDWA_DEP) \
	$(WMOTR_DEP) \
	$(BITFSA_DEP) \
	$(BITSA_DEP) \
	$(TTM_DEP)

src/message.data.c: src/str.h src/803315E4.h
src/fileselect.data.c: src/str.h
src/starselect.data.c: src/str.h

data/gfx.c: $(GFX_DEP)
shape/player/gfx.c: $(PLAYER_DEP)
shape/1a/gfx.c: $(SHAPE_1A_DEP)
shape/1b/gfx.c: $(SHAPE_1B_DEP)
shape/1c/gfx.c: $(SHAPE_1C_DEP)
shape/1d/gfx.c: $(SHAPE_1D_DEP)
shape/1e/gfx.c: $(SHAPE_1E_DEP)
shape/1f/gfx.c: $(SHAPE_1F_DEP)
shape/1g/gfx.c: $(SHAPE_1G_DEP)
shape/1h/gfx.c: $(SHAPE_1H_DEP)
shape/1i/gfx.c: $(SHAPE_1I_DEP)
shape/1j/gfx.c: $(SHAPE_1J_DEP)
shape/1k/gfx.c: $(SHAPE_1K_DEP)
shape/2a/gfx.c: $(SHAPE_2A_DEP)
shape/2b/gfx.c: $(SHAPE_2B_DEP)
shape/2c/gfx.c: $(SHAPE_2C_DEP)
shape/2d/gfx.c: $(SHAPE_2D_DEP)
shape/2e/gfx.c: $(SHAPE_2E_DEP)
shape/2f/gfx.c: $(SHAPE_2F_DEP)
shape/3common/gfx.c: $(COMMON_DEP)
shape/global/gfx.c: $(GLOBAL_DEP)
stage/title/logo.c: $(TITLE_LOGO_DEP)
stage/title/debug.c: $(TITLE_DEBUG_DEP)
data/back/title.c: $(TITLE_BACK_DEP)
stage/select/gfx.c: $(SELECT_DEP)
data/back/a.c: $(BACK_A_DEP)
data/back/b.c: $(BACK_B_DEP)
data/back/c.c: $(BACK_C_DEP)
data/back/d.c: $(BACK_D_DEP)
data/back/e.c: $(BACK_E_DEP)
data/back/f.c: $(BACK_F_DEP)
data/back/g.c: $(BACK_G_DEP)
data/back/h.c: $(BACK_H_DEP)
data/back/i.c: $(BACK_I_DEP)
data/back/j.c: $(BACK_J_DEP)
data/texture/a.c: $(TEXTURE_A_DEP)
data/texture/b.c: $(TEXTURE_B_DEP)
data/texture/c.c: $(TEXTURE_C_DEP)
data/texture/d.c: $(TEXTURE_D_DEP)
data/texture/e.c: $(TEXTURE_E_DEP)
data/texture/f.c: $(TEXTURE_F_DEP)
data/texture/g.c: $(TEXTURE_G_DEP)
data/texture/h.c: $(TEXTURE_H_DEP)
data/texture/i.c: $(TEXTURE_I_DEP)
data/texture/j.c: $(TEXTURE_J_DEP)
data/texture/k.c: $(TEXTURE_K_DEP)
data/texture/l.c: $(TEXTURE_L_DEP)
data/weather/gfx.c: $(WEATHER_DEP)
stage/bbh/gfx.c: $(BBH_DEP)
stage/ccm/gfx.c: $(CCM_DEP)
stage/inside/gfx.c: $(INSIDE_DEP)
stage/hmc/gfx.c: $(HMC_DEP)
stage/ssl/gfx.c: $(SSL_DEP)
stage/bob/gfx.c: $(BOB_DEP) $(BUILD)/data/texture/c.szp.h
stage/sl/gfx.c: $(SL_DEP)
stage/wdw/gfx.c: $(WDW_DEP)
stage/jrb/gfx.c: $(JRB_DEP)
stage/thi/gfx.c: $(THI_DEP)
stage/ttc/gfx.c: $(TTC_DEP)
stage/rr/gfx.c: $(RR_DEP)
stage/grounds/gfx.c: $(GROUNDS_DEP)
stage/bitdw/gfx.c: $(BITDW_DEP)
stage/vcutm/gfx.c: $(VCUTM_DEP)
stage/bitfs/gfx.c: $(BITFS_DEP)
stage/sa/gfx.c: $(SA_DEP)
stage/bits/gfx.c: $(BITS_DEP)
stage/lll/gfx.c: $(LLL_DEP)
stage/ddd/gfx.c: $(DDD_DEP)
stage/wf/gfx.c: $(WF_DEP)
stage/ending/gfx.c: $(ENDING_DEP)
stage/courtyard/gfx.c: $(COURTYARD_DEP)
stage/pss/gfx.c: $(PSS_DEP)
stage/cotmc/gfx.c: $(COTMC_DEP)
stage/totwc/gfx.c: $(TOTWC_DEP)
stage/bitdwa/gfx.c: $(BITDWA_DEP)
stage/wmotr/gfx.c: $(WMOTR_DEP)
stage/bitfsa/gfx.c: $(BITFSA_DEP)
stage/bitsa/gfx.c: $(BITSA_DEP)
stage/ttm/gfx.c: $(TTM_DEP)

# Player
$(MARIO_DEP)&: shape/player/mario/mario.glb tools/gltf; tools/gltf $<
# Shape1B
$(BULLY_DEP)&: shape/1b/bully/bully.glb tools/gltf; tools/gltf $<
$(BLARGG_DEP)&: shape/1b/blargg/blargg.glb tools/gltf; tools/gltf $<
# Shape2B
$(SKEETER_DEP)&: shape/2b/skeeter/skeeter.glb tools/gltf; tools/gltf $<
$(KELP_DEP)&: shape/2b/kelp/kelp.glb tools/gltf; tools/gltf $<
$(WATERMINE_DEP)&: shape/2b/watermine/watermine.glb tools/gltf; tools/gltf $<
$(PIRANHA_DEP)&: shape/2b/piranha/piranha.glb tools/gltf; tools/gltf $<
$(BUB_DEP)&: shape/2b/bub/bub.glb tools/gltf; tools/gltf $<
$(WATERRING_DEP)&: shape/2b/waterring/waterring.glb tools/gltf; tools/gltf $<
$(CHEST_DEP)&: shape/2b/chest/chest.glb tools/gltf; tools/gltf $<
# Shape2D
$(LAKITU2_DEP)&: shape/2d/lakitu2/lakitu2.glb tools/gltf; tools/gltf $<
$(TOAD_DEP)&: shape/2d/toad/toad.glb tools/gltf; tools/gltf $<
$(MIPS_DEP)&: shape/2d/mips/mips.glb tools/gltf; tools/gltf $<
$(BOO2_DEP)&: shape/2d/boo2/boo2.glb tools/gltf; tools/gltf -g $<
# Global
$(BUTTERFLY_DEP)&: shape/global/butterfly/butterfly.glb tools/gltf; tools/gltf -g $<
$(PIPE_DEP)&: shape/global/pipe/pipe.glb tools/gltf; tools/gltf $<
$(DOOR_DEP)&: shape/global/door/door.glb tools/gltf; tools/gltf $<
$(DOORKEY_DEP)&: shape/global/doorkey/doorkey.glb tools/gltf; tools/gltf $<
$(FISH_DEP)&: shape/global/fish/fish.glb tools/gltf; tools/gltf $<
$(CAP_DEP)&: shape/global/cap/cap.glb tools/gltf; tools/gltf $<
$(POWERSTAR_DEP)&: shape/global/powerstar/powerstar.glb tools/gltf; tools/gltf $<
$(SHADESTAR_DEP)&: shape/global/shadestar/shadestar.glb tools/gltf; tools/gltf $<
$(SIGNPOST_DEP)&: shape/global/signpost/signpost.glb tools/gltf; tools/gltf $<
$(TREE_DEP)&: shape/global/tree/tree.glb tools/gltf; tools/gltf $<
# Title
$(LOGO_DEP)&: stage/title/logo.glb tools/gltf; tools/gltf $<
$(DEBUG_DEP)&: stage/title/debug.glb tools/gltf; tools/gltf -g $<
# Select
$(FILE_DEP)&: stage/select/file/file.glb tools/gltf; tools/gltf $<
$(TILE_DEP)&: stage/select/tile/tile.glb tools/gltf; tools/gltf $<
# BoB
$(BATTLEFIELD_DEP)&: stage/bob/battlefield/battlefield.glb tools/gltf; tools/gltf $<
$(BOB_54_DEP)&: stage/bob/54/54.glb tools/gltf; tools/gltf $<
$(BOB_55_DEP)&: stage/bob/55/55.glb tools/gltf; tools/gltf $<
$(BOB_56_DEP)&: stage/bob/56/56.glb tools/gltf; tools/gltf $<

# Global
shape/global/pipe/map.h: shape/global/pipe/pipe.obj tools/obj; tools/obj $< $@
shape/global/map/door.h: shape/global/map/door.obj tools/obj; tools/obj $< $@
shape/global/map/13002018.h: shape/global/map/13002018.obj tools/obj; tools/obj $< $@
shape/global/signpost/map.h: shape/global/signpost/signpost.obj tools/obj; tools/obj $< $@
# Select
stage/select/map.h: stage/select/select.obj tools/obj; tools/obj $< $@
# BoB
stage/bob/battlefield/map.h: stage/bob/battlefield/battlefield.obj tools/obj; tools/obj $< $@
stage/bob/54/map.h: stage/bob/54/54.obj tools/obj; tools/obj $< $@
stage/bob/55/map.h: stage/bob/55/55.obj tools/obj; tools/obj $< $@
stage/bob/56/map.h: stage/bob/56/56.obj tools/obj; tools/obj $< $@
