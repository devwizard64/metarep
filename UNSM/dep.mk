CODE_OBJ :=
ifneq ($(filter P0 J3 C3,$(TARGET)),)
	CODE_OBJ += $(BUILD)/src/fault.o
endif
CODE_OBJ += \
	$(BUILD)/src/main.o \
	$(BUILD)/src/graphics.o \
	$(BUILD)/src/audio.o
ifneq ($(MOTOR),)
	CODE_OBJ += $(BUILD)/src/motor.o
endif
CODE_OBJ += $(BUILD)/src/game.o
ifneq ($(TARGET),DD)
	CODE_OBJ += \
		$(BUILD)/src/collision.o \
		$(BUILD)/src/player.o \
		$(BUILD)/src/physics.o \
		$(BUILD)/src/pldemo.o \
		$(BUILD)/src/plspec.o \
		$(BUILD)/src/plwait.o \
		$(BUILD)/src/plwalk.o \
		$(BUILD)/src/pljump.o \
		$(BUILD)/src/plswim.o \
		$(BUILD)/src/platck.o
endif
CODE_OBJ += \
	$(BUILD)/src/callback.o \
	$(BUILD)/src/memory.o \
	$(BUILD)/src/backup.o \
	$(BUILD)/src/scene.o \
	$(BUILD)/src/draw.o \
	$(BUILD)/src/time.o
ifneq ($(DISK),)
	CODE_OBJ += $(BUILD)/src/disk.o
endif
CODE_OBJ += \
	$(BUILD)/src/slidec.o

CODE_OBJ += \
	$(BUILD)/src/$(TARGET)/camera.o $(BUILD)/src/$(TARGET)/camera.data.o

CODE_OBJ += \
	$(BUILD)/src/course.o \
	$(BUILD)/src/object.o
ifneq ($(TARGET),P0)
	CODE_OBJ += $(BUILD)/src/objectlib.o
endif
CODE_OBJ += \
	$(BUILD)/src/enemya.o \
	$(BUILD)/src/movebg.o
ifneq ($(TARGET),P0)
	CODE_OBJ += $(BUILD)/src/hitcheck.o $(BUILD)/src/objlist.o
endif
CODE_OBJ += \
	$(BUILD)/src/objsound.o \
	$(BUILD)/src/debug.o

CODE_OBJ += \
	$(BUILD)/src/wipe.o \
	$(BUILD)/src/shadow.o \
	$(BUILD)/src/background.o \
	$(BUILD)/src/water.o \
	$(BUILD)/src/objshape.o \
	$(BUILD)/src/wave.o

CODE_OBJ += \
	$(BUILD)/src/dprint.o \
	$(BUILD)/src/message.o \
	$(BUILD)/src/weather.o \
	$(BUILD)/src/lava.o \
	$(BUILD)/src/tag.o \
	$(BUILD)/src/hud.o \
	$(BUILD)/src/$(TARGET)/enemyb.o $(BUILD)/src/$(TARGET)/enemyb.data.o

CODE_OBJ += \
	$(BUILD)/src/$(TARGET)/enemyc.o $(BUILD)/src/$(TARGET)/enemyc.data.o

ULIB_OBJ := \
	$(BUILD)/src/math.o \
	$(BUILD)/src/mathtbl.o \
	$(BUILD)/src/shape.o \
	$(BUILD)/src/shplang.o \
	$(BUILD)/src/seqlang.o \
	$(BUILD)/src/bgcheck.o \
	$(BUILD)/src/bgload.o \
	$(BUILD)/src/objlang.o
ifeq ($(TARGET),DD)
	ULIB_OBJ += \
		$(BUILD)/src/player.o \
		$(BUILD)/src/pldemo.o \
		$(BUILD)/src/plspec.o \
		$(BUILD)/src/plwait.o \
		$(BUILD)/src/plwalk.o \
		$(BUILD)/src/pljump.o \
		$(BUILD)/src/plswim.o \
		$(BUILD)/src/platck.o \
		$(BUILD)/src/collision.o \
		$(BUILD)/src/physics.o
endif
ifeq ($(TARGET),P0)
	ULIB_OBJ += \
		$(BUILD)/src/hitcheck.o \
		$(BUILD)/src/objlist.o \
		$(BUILD)/src/objectlib.o
endif

MENU_OBJ := \
	$(BUILD)/src/title.o \
	$(BUILD)/src/titlebg.o \
	$(BUILD)/src/fileselect.o \
	$(BUILD)/src/starselect.o

AUDIO_OBJ := \
	$(BUILD)/src/audio/$(NA_REVISION)/driver.o $(BUILD)/src/audio/$(NA_REVISION)/driver.data.o \
	$(BUILD)/src/audio/$(NA_REVISION)/memory.o $(BUILD)/src/audio/$(NA_REVISION)/memory.data.o \
	$(BUILD)/src/audio/$(NA_REVISION)/system.o \
	$(BUILD)/src/audio/$(NA_REVISION)/voice.o $(BUILD)/src/audio/$(NA_REVISION)/voice.data.o \
	$(BUILD)/src/audio/$(NA_REVISION)/effect.o $(BUILD)/src/audio/$(NA_REVISION)/effect.data.o \
	$(BUILD)/src/audio/$(NA_REVISION)/sequence.o $(BUILD)/src/audio/$(NA_REVISION)/sequence.data.o \
	$(BUILD)/src/audio/$(NA_REVISION)/game.o $(BUILD)/src/audio/$(NA_REVISION)/game.data.o
ifeq ($(NA_VERSION),2)
	AUDIO_OBJ += $(BUILD)/src/audio/$(NA_REVISION)/h.o $(BUILD)/src/audio/$(NA_REVISION)/h.data.o
endif
AUDIO_OBJ += $(BUILD)/src/audio/$(NA_REVISION)/data.o

BC_OBJ :=
ifeq ($(TARGET),C3)
	BC_OBJ += $(BUILD)/src/bc.o
endif

FACE_OBJ := \
	$(BUILD)/src/face/main.o \
	$(BUILD)/src/face/memory.o \
	$(BUILD)/src/face/sound.o \
	$(BUILD)/src/face/draw.text.o $(BUILD)/src/face/draw.data.o \
	$(BUILD)/src/face/object.text.o $(BUILD)/src/face/object.data.o \
	$(BUILD)/src/face/skin.text.o $(BUILD)/src/face/skin.data.o \
	$(BUILD)/src/face/particle.text.o $(BUILD)/src/face/particle.data.o \
	$(BUILD)/src/face/dynlist.text.o $(BUILD)/src/face/dynlist.data.o \
	$(BUILD)/src/face/gadget.text.o $(BUILD)/src/face/gadget.data.o \
	$(BUILD)/src/face/stdio.text.o $(BUILD)/src/face/stdio.data.o \
	$(BUILD)/src/face/joint.text.o $(BUILD)/src/face/joint.data.o \
	$(BUILD)/src/face/net.text.o $(BUILD)/src/face/net.data.o \
	$(BUILD)/src/face/math.text.o $(BUILD)/src/face/math.data.o \
	$(BUILD)/src/face/shape.text.o $(BUILD)/src/face/shape.data.o \
	$(BUILD)/src/face/gfx.text.o $(BUILD)/src/face/gfx.data.o

FACEDATA_OBJ := \
	$(BUILD)/src/face/data/ico1.o \
	$(BUILD)/src/face/data/spot.o \
	$(BUILD)/src/face/data/mario.o \
	$(BUILD)/src/face/data/mario_anim.o

IDO_C := \
	$(BUILD)/src/fault.o \
	$(BUILD)/src/main.o \
	$(BUILD)/src/graphics.o \
	$(BUILD)/src/audio.o \
	$(BUILD)/src/motor.o \
	$(BUILD)/src/game.o \
	$(BUILD)/src/collision.o \
	$(BUILD)/src/player.o \
	$(BUILD)/src/physics.o \
	$(BUILD)/src/pldemo.o \
	$(BUILD)/src/plspec.o \
	$(BUILD)/src/plwait.o \
	$(BUILD)/src/plwalk.o \
	$(BUILD)/src/pljump.o \
	$(BUILD)/src/plswim.o \
	$(BUILD)/src/platck.o \
	$(BUILD)/src/callback.o \
	$(BUILD)/src/memory.o \
	$(BUILD)/src/backup.o \
	$(BUILD)/src/scene.o \
	$(BUILD)/src/draw.o \
	$(BUILD)/src/time.o \
	$(BUILD)/src/disk.o \
	$(BUILD)/src/course.o \
	$(BUILD)/src/object.o \
	$(BUILD)/src/objectlib.o \
	$(BUILD)/src/enemya.o \
	$(BUILD)/src/movebg.o \
	$(BUILD)/src/hitcheck.o \
	$(BUILD)/src/objlist.o \
	$(BUILD)/src/objsound.o \
	$(BUILD)/src/debug.o \
	$(BUILD)/src/wipe.o \
	$(BUILD)/src/shadow.o \
	$(BUILD)/src/background.o \
	$(BUILD)/src/water.o \
	$(BUILD)/src/objshape.o \
	$(BUILD)/src/wave.o \
	$(BUILD)/src/dprint.o \
	$(BUILD)/src/message.o \
	$(BUILD)/src/weather.o \
	$(BUILD)/src/lava.o \
	$(BUILD)/src/tag.o \
	$(BUILD)/src/hud.o \
	$(BUILD)/src/enemyb.o \
	$(BUILD)/src/enemyc.o \
	$(BUILD)/src/math.o \
	$(BUILD)/src/shape.o \
	$(BUILD)/src/shplang.o \
	$(BUILD)/src/seqlang.o \
	$(BUILD)/src/bgcheck.o \
	$(BUILD)/src/bgload.o \
	$(BUILD)/src/objlang.o \
	$(BUILD)/src/title.o \
	$(BUILD)/src/titlebg.o \
	$(BUILD)/src/fileselect.o \
	$(BUILD)/src/starselect.o \
	$(BUILD)/data/buffer.o \
	$(BUILD)/src/audio/heap.o \
	$(BUILD)/src/face/main.o \
	$(BUILD)/src/face/memory.o \
	$(BUILD)/src/face/sound.o \
	$(BUILD)/src/face/draw.o \
	$(BUILD)/src/face/object.o \
	$(BUILD)/src/face/skin.o \
	$(BUILD)/src/face/particle.o \
	$(BUILD)/src/face/dynlist.o \
	$(BUILD)/src/face/gadget.o \
	$(BUILD)/src/face/stdio.o \
	$(BUILD)/src/face/joint.o \
	$(BUILD)/src/face/net.o \
	$(BUILD)/src/face/math.o \
	$(BUILD)/src/face/shape.o \
	$(BUILD)/src/face/gfx.o \
	$(BUILD)/src/face/data/ico1.o \
	$(BUILD)/src/face/data/spot.o \
	$(BUILD)/src/face/data/mario.o \
	$(BUILD)/src/face/data/mario_anim.o

IDO_S := \
	$(BUILD)/src/slidec.o \
	$(BUILD)/src/mathtbl.o

OBJ := \
	$(BUILD)/lib/PR/rspboot.o \
	$(BUILD)/lib/PR/gspFast3D.fifo.o \
	$(BUILD)/lib/PR/aspMain.o \
	$(BUILD)/code.o \
	$(BUILD)/ulib.o
ifneq ($(TARGET),DD)
	OBJ += $(BUILD)/face.o $(BUILD)/facedata.o
endif

DATA := \
	$(BUILD)/data/cimg.o \
	$(BUILD)/data/zimg.o \
	$(BUILD)/data/timg.o \
	$(BUILD)/data/buffer.o \
	$(BUILD)/data/fifo.o \
	$(BUILD)/src/enemyaobj.o \
	$(BUILD)/src/playerobj.o \
	$(BUILD)/src/enemybobj.o \
	$(BUILD)/src/enemycobj.o \
	$(BUILD)/src/cameraobj.o \
	$(BUILD)/data/main.o \
	$(patsubst %.c,$(BUILD)/%.o,$(wildcard shape/*/shp.c)) \
	$(BUILD)/data/game.o \
	$(patsubst %.sx,$(BUILD)/%.o,$(wildcard stage/*/seq.sx)) \
	$(patsubst %.c,$(BUILD)/%.o,$(wildcard stage/*/shp.c)) \
	$(BUILD)/data/anime.o \
	$(BUILD)/data/demo.o

SZP := \
	$(BUILD)/data/gfx.szp.o \
	$(patsubst %.bin,$(BUILD)/%.szp.o,$(wildcard shape/*/gfx.bin)) \
	$(patsubst %.c,$(BUILD)/%.szp.o,$(wildcard shape/*/gfx.c)) \
	$(patsubst %.c,$(BUILD)/%.szp.o,$(wildcard data/background/*.c)) \
	$(patsubst %.c,$(BUILD)/%.szp.o,$(wildcard data/texture/*.c)) \
	$(BUILD)/data/weather/gfx.szp.o \
	$(BUILD)/stage/title/logo.szp.o \
	$(BUILD)/stage/title/debug.szp.o \
	$(patsubst %.bin,$(BUILD)/%.szp.o,$(wildcard stage/*/gfx.bin)) \
	$(patsubst %.c,$(BUILD)/%.szp.o,$(wildcard stage/*/gfx.c))

AUDIO_DATA := \
	$(BUILD)/src/audio/heap.o \
	$(BUILD)/src/audio/work.o \
	$(BUILD)/audio/ctl.o \
	$(BUILD)/audio/tbl.o \
	$(BUILD)/audio/seq.o \
	$(BUILD)/audio/bnk.o

AUDIO_SEQ := \
	audio/$(TARGET)/seq/se.seq \
	audio/$(TARGET)/seq/starcatch.seq \
	audio/$(TARGET)/seq/title.seq \
	audio/$(TARGET)/seq/field.seq \
	audio/$(TARGET)/seq/castle.seq \
	audio/$(TARGET)/seq/water.seq \
	audio/$(TARGET)/seq/fire.seq \
	audio/$(TARGET)/seq/arena.seq \
	audio/$(TARGET)/seq/snow.seq \
	audio/$(TARGET)/seq/slider.seq \
	audio/$(TARGET)/seq/ghost.seq \
	audio/$(TARGET)/seq/lullaby.seq \
	audio/$(TARGET)/seq/dungeon.seq \
	audio/$(TARGET)/seq/starselect.seq \
	audio/$(TARGET)/seq/special.seq \
	audio/$(TARGET)/seq/metal.seq \
	audio/$(TARGET)/seq/bowsermsg.seq \
	audio/$(TARGET)/seq/bowser.seq \
	audio/$(TARGET)/seq/hiscore.seq \
	audio/$(TARGET)/seq/merrygoround.seq \
	audio/$(TARGET)/seq/fanfare.seq \
	audio/$(TARGET)/seq/starappear.seq \
	audio/$(TARGET)/seq/battle.seq \
	audio/$(TARGET)/seq/arenaclear.seq \
	audio/$(TARGET)/seq/endless.seq \
	audio/$(TARGET)/seq/final.seq \
	audio/$(TARGET)/seq/staff.seq \
	audio/$(TARGET)/seq/solution.seq \
	audio/$(TARGET)/seq/toadmsg.seq \
	audio/$(TARGET)/seq/peachmsg.seq \
	audio/$(TARGET)/seq/intro.seq \
	audio/$(TARGET)/seq/finalclear.seq \
	audio/$(TARGET)/seq/ending.seq \
	audio/$(TARGET)/seq/fileselect.seq
ifneq ($(NA_REVISION),100)
	AUDIO_SEQ += audio/$(TARGET)/seq/lakitumsg.seq
endif

################################################################################
# Player

MARIO_GFX := \
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
	shape/player/mario/h_torso.red.h \
	shape/player/mario/h_torso.blue.h \
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

BULLY_GFX := \
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

BLARGG_GFX := \
	shape/1b/blargg/lower_jaw.h \
	shape/1b/blargg/lower_jaw.teeth.h \
	shape/1b/blargg/lower_jaw.lower_jaw.h \
	shape/1b/blargg/upper_jaw.h \
	shape/1b/blargg/upper_jaw.teeth.h \
	shape/1b/blargg/upper_jaw.upper_jaw.h \
	shape/1b/blargg/body.h \
	shape/1b/blargg/body.body.h

################################################################################
# Shape2B

SKEETER_GFX := \
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

KELP_GFX := \
	shape/2b/kelp/0.h \
	shape/2b/kelp/0.0.h \
	shape/2b/kelp/1.h \
	shape/2b/kelp/1.1.h \
	shape/2b/kelp/2.h \
	shape/2b/kelp/2.2.h \
	shape/2b/kelp/3.h \
	shape/2b/kelp/3.3.h

WATERMINE_GFX := \
	shape/2b/watermine/mine.h \
	shape/2b/watermine/mine.l.h \
	shape/2b/watermine/mine.r.h \
	shape/2b/watermine/spike.h \
	shape/2b/watermine/spike.spike.h

PIRANHA_GFX := \
	shape/2b/piranha/body.h \
	shape/2b/piranha/body.piranha.h \
	shape/2b/piranha/fin.h \
	shape/2b/piranha/fin.piranha.h \
	shape/2b/piranha/tail.h \
	shape/2b/piranha/tail.piranha.h

BUB_GFX := \
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

WATERRING_GFX := \
	shape/2b/waterring/waterring.h \
	shape/2b/waterring/waterring.shade.h

CHEST_GFX := \
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

LAKITU2_GFX := \
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

TOAD_GFX := \
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

MIPS_GFX := \
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

BOO2_GFX := \
	shape/2d/boo2/boo.h \
	shape/2d/boo2/boo.mouth.h \
	shape/2d/boo2/boo.eyes.h \
	shape/2d/boo2/boo.shade.h

################################################################################
# Common

BLUECOINSW_GFX := \
	shape/3common/bluecoinsw/bluecoinsw.h \
	shape/3common/bluecoinsw/bluecoinsw.side.h \
	shape/3common/bluecoinsw/bluecoinsw.top.h

AMP_GFX := \
	shape/3common/amp/arc.h \
	shape/3common/amp/arc.arc.h \
	shape/3common/amp/eyes.h \
	shape/3common/amp/eyes.eyes.h \
	shape/3common/amp/mouth.h \
	shape/3common/amp/mouth.mouth.h \
	shape/3common/amp/body.h \
	shape/3common/amp/body.body.h \
	shape/3common/amp/arcA_old.h \
	shape/3common/amp/arcA_old.arc_old.h \
	shape/3common/amp/arcB_old.h \
	shape/3common/amp/arcB_old.arc_old.h \
	shape/3common/amp/arcC_old.h \
	shape/3common/amp/arcC_old.arc_old.h \
	shape/3common/amp/arcD_old.h \
	shape/3common/amp/arcD_old.arc_old.h \
	shape/3common/amp/body_old.h \
	shape/3common/amp/body_old.shade_old.h \
	shape/3common/amp/mouth_old.h \
	shape/3common/amp/mouth_old.shade_old.h \
	shape/3common/amp/anger_old.h \
	shape/3common/amp/anger_old.shade_old.h \
	shape/3common/amp/eyes_old.h \
	shape/3common/amp/eyes_old.shade_old.h

CANNONLID_GFX := \
	shape/3common/cannonlid/cannonlid.h \
	shape/3common/cannonlid/cannonlid.lid.h

CANNON_GFX := \
	shape/3common/cannon/cannon.h \
	shape/3common/cannon/cannon.side.h \
	shape/3common/cannon/cannon.shade.h

CANNONBARREL_GFX := \
	shape/3common/cannonbarrel/cannonbarrel.h \
	shape/3common/cannonbarrel/cannonbarrel.rim.h \
	shape/3common/cannonbarrel/cannonbarrel.shade.h

CHUCKYA_GFX := \
	shape/3common/chuckya/body.h \
	shape/3common/chuckya/body.purple_l.h \
	shape/3common/chuckya/body.purple_r.h \
	shape/3common/chuckya/armL.h \
	shape/3common/chuckya/armL.purple_l.h \
	shape/3common/chuckya/armL.purple_r.h \
	shape/3common/chuckya/armR.h \
	shape/3common/chuckya/armR.purple_l.h \
	shape/3common/chuckya/armR.purple_r.h \
	shape/3common/chuckya/handL.h \
	shape/3common/chuckya/handL.red.h \
	shape/3common/chuckya/handR.h \
	shape/3common/chuckya/handR.red.h \
	shape/3common/chuckya/antenna_end.h \
	shape/3common/chuckya/antenna_end.red.h \
	shape/3common/chuckya/eyes.h \
	shape/3common/chuckya/eyes.eyes.h \
	shape/3common/chuckya/base.h \
	shape/3common/chuckya/base.base.h \
	shape/3common/chuckya/antenna.h \
	shape/3common/chuckya/antenna.antenna.h \
	shape/3common/chuckya/back.h \
	shape/3common/chuckya/back.back.h

PURPLESW_GFX := \
	shape/3common/purplesw/purplesw.h \
	shape/3common/purplesw/purplesw.side.h \
	shape/3common/purplesw/purplesw.top.h

LIFT_GFX := \
	shape/3common/lift/lift.h \
	shape/3common/lift/lift.side.h \
	shape/3common/lift/lift.face.h

HEART_GFX := \
	shape/3common/heart/heart.h \
	shape/3common/heart/heart.heart.h

FLYGUY_GFX := \
	shape/3common/flyguy/footR.h \
	shape/3common/flyguy/footR.foot.h \
	shape/3common/flyguy/footL.h \
	shape/3common/flyguy/footL.foot.h \
	shape/3common/flyguy/shaft.h \
	shape/3common/flyguy/shaft.shaft.h \
	shape/3common/flyguy/propeller.h \
	shape/3common/flyguy/propeller.propeller.h \
	shape/3common/flyguy/body.h \
	shape/3common/flyguy/body.face.h \
	shape/3common/flyguy/body.cloth_black.h \
	shape/3common/flyguy/body.cloth_red.h \
	shape/3common/flyguy/body.black.h

BLOCK_GFX := \
	shape/3common/block/block.h \
	shape/3common/block/block.block.h

ITEMBOX_GFX := \
	shape/3common/itembox/32x64.h \
	shape/3common/itembox/32x64.32x64_face.h \
	shape/3common/itembox/32x64.32x64_side.h \
	shape/3common/itembox/64x32.h \
	shape/3common/itembox/64x32.64x32_face.h \
	shape/3common/itembox/64x32.64x32_side.h

GOOMBA_GFX := \
	shape/3common/goomba/head.h \
	shape/3common/goomba/head.head.h \
	shape/3common/goomba/body.h \
	shape/3common/goomba/body.body.h \
	shape/3common/goomba/footL.h \
	shape/3common/goomba/footL.footL.h \
	shape/3common/goomba/footR.h \
	shape/3common/goomba/footR.footR.h \
	shape/3common/goomba/head_old.h \
	shape/3common/goomba/head_old.head_old.h \
	shape/3common/goomba/body_old.h \
	shape/3common/goomba/body_old.body_old.h

BOBOMB_GFX := \
	shape/3common/bobomb/eyes.h \
	shape/3common/bobomb/eyes.eyes.h \
	shape/3common/bobomb/footR.h \
	shape/3common/bobomb/footR.foot.h \
	shape/3common/bobomb/footL.h \
	shape/3common/bobomb/footL.foot.h \
	shape/3common/bobomb/cap.h \
	shape/3common/bobomb/cap.cap.h

PUSHBLOCK_GFX := \
	shape/3common/pushblock/pushblock.h \
	shape/3common/pushblock/pushblock.pushblock.h

DOTBOX_GFX := \
	shape/3common/dotbox/box.h \
	shape/3common/dotbox/box.box.h \
	shape/3common/dotbox/dot.h \
	shape/3common/dotbox/dot.dot.h \
	shape/3common/dotbox/mark.h \
	shape/3common/dotbox/mark.mark.h

TESTLIFT_GFX := \
	shape/3common/testlift/testlift.h \
	shape/3common/testlift/testlift.shade.h

SHELL_OLD_GFX := \
	shape/3common/shell/shell_old.h \
	shape/3common/shell/shell_old.top.h \
	shape/3common/shell/shell_old.bottom.h \
	shape/3common/shell/shell_old.side.h

SHELL_GFX := \
	shape/3common/shell/shell.h \
	shape/3common/shell/shell.top.h \
	shape/3common/shell/shell.bottom.h \
	shape/3common/shell/shell.front.h \
	shape/3common/shell/shell.white.h

################################################################################
# Global

BUTTERFLY_GFX := \
	shape/global/butterfly/l.h \
	shape/global/butterfly/l.wing.h \
	shape/global/butterfly/r.h \
	shape/global/butterfly/r.wing.h

PIPE_GFX := \
	shape/global/pipe/side.h \
	shape/global/pipe/side.side.h \
	shape/global/pipe/end.h \
	shape/global/pipe/end.top.h \
	shape/global/pipe/end.bottom.h

DOOR_GFX := \
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

DOORKEY_GFX := \
	shape/global/doorkey/key.h \
	shape/global/doorkey/key.key.h

FISH_GFX := \
	shape/global/fish/body.h \
	shape/global/fish/body.fish.h \
	shape/global/fish/tail.h \
	shape/global/fish/tail.fish.h

CAP_GFX := \
	shape/global/cap/cap.h \
	shape/global/cap/cap.logo.h \
	shape/global/cap/cap.red.h \
	shape/global/cap/cap.hair.h \
	shape/global/cap/wing.h \
	shape/global/cap/wing.wing_l.h \
	shape/global/cap/wing.wing_r.h

POWERSTAR_GFX := \
	shape/global/powerstar/star.h \
	shape/global/powerstar/star.star.h \
	shape/global/powerstar/eyes.h \
	shape/global/powerstar/eyes.eye.h

SHADESTAR_GFX := \
	shape/global/shadestar/star.h \
	shape/global/shadestar/star.star.h

SIGNPOST_GFX := \
	shape/global/signpost/post.h \
	shape/global/signpost/post.wood.h \
	shape/global/signpost/sign.h \
	shape/global/signpost/sign.wood.h \
	shape/global/signpost/sign.face.h

TREE_GFX := \
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

LOGO_GFX := \
	stage/title/logo.h \
	stage/title/logo.marble.h \
	stage/title/logo.wood.h \
	stage/title/logo.shade.h \
	stage/title/symbol.h \
	stage/title/symbol.copyright.h \
	stage/title/symbol.trademark.h

DEBUG_GFX := \
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

FILE_GFX := \
	stage/select/file/file.h \
	stage/select/file/file.edge.h \
	stage/select/file/file.face.h

TILE_GFX := \
	stage/select/tile/tile.h \
	stage/select/tile/tile.tile.h

################################################################################
# BoB

BATTLEFIELD_GFX := \
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

BOB_54_GFX := \
	stage/bob/54/54.h \
	stage/bob/54/54.c16.h

BOB_55_GFX := \
	stage/bob/55/55.h \
	stage/bob/55/55.c12.h

BOB_56_GFX := \
	stage/bob/56/56.h \
	stage/bob/56/56.c16.h

################################################################################
# PSS

MINISLIDER_GFX := \
	stage/pss/minislider/0.h \
	stage/pss/minislider/0.i21_shade.h \
	stage/pss/minislider/0.i21_light.h \
	stage/pss/minislider/0.0_light.h \
	stage/pss/minislider/0.i0_light.h \
	stage/pss/minislider/0.i10_light.h \
	stage/pss/minislider/0.i2_light.h \
	stage/pss/minislider/1.h \
	stage/pss/minislider/1.i21.h \
	stage/pss/minislider/1.i0.h \
	stage/pss/minislider/1.i12.h \
	stage/pss/minislider/2.h \
	stage/pss/minislider/2.i13.h \
	stage/pss/minislider/3.h \
	stage/pss/minislider/3.i12.h \
	stage/pss/minislider/4.h \
	stage/pss/minislider/4.1.h \
	stage/pss/minislider/5.h \
	stage/pss/minislider/5.i12.h \
	stage/pss/minislider/5.0.h \
	stage/pss/minislider/5.i10.h \
	stage/pss/minislider/6.h \
	stage/pss/minislider/6.2.h

################################################################################

FACE_DEP := $(patsubst %.png,%.h,$(wildcard src/face/*.png)) \

GFX_DIR := glbfont staff lgfont camera shadow wipe water minimap
GFX_DEP := \
	$(patsubst %.png,%.h,$(foreach dir,$(GFX_DIR),$(wildcard data/gfx/$(dir)/*.png))) \
	$(patsubst %.txt,%.h,$(wildcard data/gfx/*.txt))

PLAYER_DIR := mario bubble dust smoke wave ripple sparkle splash droplet glow
PLAYER_DEP := \
	$(patsubst %.png,%.h,$(foreach dir,$(PLAYER_DIR),$(wildcard shape/player/$(dir)/*.png))) \
	$(MARIO_GFX)

SHAPE_1A_DEP :=

SHAPE_1B_DIR := bully blargg
SHAPE_1B_DEP := \
	$(patsubst %.png,%.h,$(foreach dir,$(SHAPE_1B_DIR),$(wildcard shape/1b/$(dir)/*.png))) \
	$(BULLY_GFX) \
	$(BLARGG_GFX)

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

SHAPE_2B_DIR := skeeter kelp watermine piranha bub waterring chest
SHAPE_2B_DEP := \
	$(patsubst %.png,%.h,$(foreach dir,$(SHAPE_2B_DIR),$(wildcard shape/2b/$(dir)/*.png))) \
	$(SKEETER_GFX) \
	$(KELP_GFX) \
	$(WATERMINE_GFX) \
	$(PIRANHA_GFX) \
	$(BUB_GFX) \
	$(WATERRING_GFX) \
	$(CHEST_GFX)

SHAPE_2C_DEP :=

SHAPE_2D_DIR := lakitu2 toad mips boo2
SHAPE_2D_DEP := \
	$(patsubst %.png,%.h,$(foreach dir,$(SHAPE_2D_DIR),$(wildcard shape/2d/$(dir)/*.png))) \
	$(LAKITU2_GFX) \
	$(TOAD_GFX) \
	$(MIPS_GFX) \
	$(BOO2_GFX)

SHAPE_2E_DEP :=
SHAPE_2F_DEP :=

COMMON_DIR := bluecoinsw amp cannonlid cannon cannonbarrel chuckya purplesw lift heart flyguy block itembox goomba bobomb pushblock dotbox shell
COMMON_DEP := \
	$(patsubst %.png,%.h,$(foreach dir,$(COMMON_DIR),$(wildcard shape/3common/$(dir)/*.png))) \
	$(BLUECOINSW_GFX) shape/3common/bluecoinsw/map.h \
	$(AMP_GFX) \
	$(CANNONLID_GFX) shape/3common/cannonlid/map.h \
	$(CANNON_GFX) \
	$(CANNONBARREL_GFX) \
	$(CHUCKYA_GFX) \
	$(PURPLESW_GFX) shape/3common/purplesw/map.h \
	$(LIFT_GFX) shape/3common/lift/map.h \
	$(HEART_GFX) \
	$(FLYGUY_GFX) \
	$(BLOCK_GFX) shape/3common/block/map.h \
	$(ITEMBOX_GFX) \
	$(GOOMBA_GFX) \
	$(BOBOMB_GFX) \
	$(PUSHBLOCK_GFX) shape/3common/pushblock/map.h \
	$(DOTBOX_GFX) shape/3common/dotbox/map.h \
	$(TESTLIFT_GFX) shape/3common/testlift/map.h \
	$(SHELL_OLD_GFX) \
	$(SHELL_GFX)

GLOBAL_DIR := puff explosion butterfly coin pipe door flame fish stone leaf cap meter 1up powerstar sand shard snow signpost tree
GLOBAL_DEP := \
	$(patsubst %.png,%.h,$(foreach dir,$(GLOBAL_DIR),$(wildcard shape/global/$(dir)/*.png))) \
	$(BUTTERFLY_GFX) \
	$(PIPE_GFX) shape/global/pipe/map.h \
	$(DOOR_GFX) \
	$(DOORKEY_GFX) \
	$(FISH_GFX) \
	shape/global/map/door.h shape/global/map/13002018.h \
	$(CAP_GFX) \
	$(POWERSTAR_GFX) \
	$(SHADESTAR_GFX) \
	$(SIGNPOST_GFX) shape/global/signpost/map.h \
	$(TREE_GFX)

TITLE_LOGO_DEP := \
	$(patsubst %.png,%.h,$(wildcard stage/title/*.png)) \
	$(LOGO_GFX)

TITLE_DEBUG_DEP := \
	$(DEBUG_GFX)

TITLE_BACK_DEP := $(patsubst %.png,%.h,$(wildcard data/background/title/*.png))

SELECT_DIR := file tile cursor selfont smfont course
SELECT_DEP := \
	$(patsubst %.png,%.h,$(foreach dir,$(SELECT_DIR),$(wildcard stage/select/$(dir)/*.png))) \
	$(FILE_GFX) \
	$(TILE_GFX) \
	stage/select/map.h

BACKGROUND_A_DEP := $(patsubst %.png,%.h,$(wildcard data/background/a/*.png))
BACKGROUND_B_DEP := $(patsubst %.png,%.h,$(wildcard data/background/b/*.png))
BACKGROUND_C_DEP := $(patsubst %.png,%.h,$(wildcard data/background/c/*.png))
BACKGROUND_D_DEP := $(patsubst %.png,%.h,$(wildcard data/background/d/*.png))
BACKGROUND_E_DEP := $(patsubst %.png,%.h,$(wildcard data/background/e/*.png))
BACKGROUND_F_DEP := $(patsubst %.png,%.h,$(wildcard data/background/f/*.png))
BACKGROUND_G_DEP := $(patsubst %.png,%.h,$(wildcard data/background/g/*.png))
BACKGROUND_H_DEP := $(patsubst %.png,%.h,$(wildcard data/background/h/*.png))
BACKGROUND_I_DEP := $(patsubst %.png,%.h,$(wildcard data/background/i/*.png))
BACKGROUND_J_DEP := $(patsubst %.png,%.h,$(wildcard data/background/j/*.png))

TEXTURE_DEP := $(patsubst %.png,%.h,$(wildcard data/texture/*.png))

WEATHER_DIR := flower lava bubble snow
WEATHER_DEP := $(patsubst %.png,%.h,$(foreach dir,$(WEATHER_DIR),$(wildcard data/weather/$(dir)/*.png)))

BBH_DEP :=
CCM_DEP :=
INSIDE_DEP :=
HMC_DEP :=
SSL_DEP :=

BOB_DEP := \
	$(patsubst %.png,%.h,$(wildcard stage/bob/*.png)) \
	$(BATTLEFIELD_GFX) \
	$(BOB_54_GFX) \
	$(BOB_55_GFX) \
	$(BOB_56_GFX) \
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

ENDING_DEP := $(patsubst %.png,%.h,$(wildcard stage/ending/*.png))

COURTYARD_DEP :=

PSS_DEP := \
	$(patsubst %.png,%.h,$(wildcard stage/pss/*.png)) \
	$(MINISLIDER_GFX) \
	stage/pss/minislider/map.h

COTMC_DEP :=
TOTWC_DEP :=
BITDWA_DEP :=
WMOTR_DEP :=
BITFSA_DEP :=
BITSA_DEP :=
TTM_DEP :=

DEP := \
	$(patsubst %.txt,%.h,$(wildcard src/*.txt) $(wildcard src/message/*.txt)) \
	$(FACE_DEP) \
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
	$(BACKGROUND_A_DEP) \
	$(BACKGROUND_B_DEP) \
	$(BACKGROUND_C_DEP) \
	$(BACKGROUND_D_DEP) \
	$(BACKGROUND_E_DEP) \
	$(BACKGROUND_F_DEP) \
	$(BACKGROUND_G_DEP) \
	$(BACKGROUND_H_DEP) \
	$(BACKGROUND_I_DEP) \
	$(BACKGROUND_J_DEP) \
	$(TEXTURE_DEP) \
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

src/message.c: $(patsubst %.txt,%.h,$(wildcard src/message*.txt) $(wildcard src/message/*.txt))
src/fileselect.c: $(patsubst %.txt,%.h,$(wildcard src/fileselect*.txt))
src/starselect.c: $(patsubst %.txt,%.h,$(wildcard src/starselect*.txt))
src/face/gfx.data.c: $(FACE_DEP)
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
data/background/title.c: $(TITLE_BACK_DEP)
stage/select/gfx.c: $(SELECT_DEP)
data/background/a.c: $(BACKGROUND_A_DEP)
data/background/b.c: $(BACKGROUND_B_DEP)
data/background/c.c: $(BACKGROUND_C_DEP)
data/background/d.c: $(BACKGROUND_D_DEP)
data/background/e.c: $(BACKGROUND_E_DEP)
data/background/f.c: $(BACKGROUND_F_DEP)
data/background/g.c: $(BACKGROUND_G_DEP)
data/background/h.c: $(BACKGROUND_H_DEP)
data/background/i.c: $(BACKGROUND_I_DEP)
data/background/j.c: $(BACKGROUND_J_DEP)
data/texture/a.c: $(TEXTURE_DEP)
data/texture/b.c: $(TEXTURE_DEP)
data/texture/c.c: $(TEXTURE_DEP)
data/texture/d.c: $(TEXTURE_DEP)
data/texture/e.c: $(TEXTURE_DEP)
data/texture/f.c: $(TEXTURE_DEP)
data/texture/g.c: $(TEXTURE_DEP)
data/texture/h.c: $(TEXTURE_DEP)
data/texture/i.c: $(TEXTURE_DEP)
data/texture/j.c: $(TEXTURE_DEP)
data/texture/k.c: $(TEXTURE_DEP)
data/texture/l.c: $(TEXTURE_DEP)
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
stage/pss/gfx.c: $(PSS_DEP) $(BUILD)/data/texture/i.szp.h
stage/cotmc/gfx.c: $(COTMC_DEP)
stage/totwc/gfx.c: $(TOTWC_DEP)
stage/bitdwa/gfx.c: $(BITDWA_DEP)
stage/wmotr/gfx.c: $(WMOTR_DEP)
stage/bitfsa/gfx.c: $(BITFSA_DEP)
stage/bitsa/gfx.c: $(BITSA_DEP)
stage/ttm/gfx.c: $(TTM_DEP)

# Player
$(MARIO_GFX)&: shape/player/mario/mario.glb tools/gltf; tools/gltf $<
# Shape1B
$(BULLY_GFX)&: shape/1b/bully/bully.glb tools/gltf; tools/gltf $<
$(BLARGG_GFX)&: shape/1b/blargg/blargg.glb tools/gltf; tools/gltf $<
# Shape2B
$(SKEETER_GFX)&: shape/2b/skeeter/skeeter.glb tools/gltf; tools/gltf $<
$(KELP_GFX)&: shape/2b/kelp/kelp.glb tools/gltf; tools/gltf $<
$(WATERMINE_GFX)&: shape/2b/watermine/watermine.glb tools/gltf; tools/gltf $<
$(PIRANHA_GFX)&: shape/2b/piranha/piranha.glb tools/gltf; tools/gltf $<
$(BUB_GFX)&: shape/2b/bub/bub.glb tools/gltf; tools/gltf $<
$(WATERRING_GFX)&: shape/2b/waterring/waterring.glb tools/gltf; tools/gltf $<
$(CHEST_GFX)&: shape/2b/chest/chest.glb tools/gltf; tools/gltf $<
# Shape2D
$(LAKITU2_GFX)&: shape/2d/lakitu2/lakitu2.glb tools/gltf; tools/gltf $<
$(TOAD_GFX)&: shape/2d/toad/toad.glb tools/gltf; tools/gltf $<
$(MIPS_GFX)&: shape/2d/mips/mips.glb tools/gltf; tools/gltf $<
$(BOO2_GFX)&: shape/2d/boo2/boo2.glb tools/gltf; tools/gltf -g $<
# Common
$(BLUECOINSW_GFX)&: shape/3common/bluecoinsw/bluecoinsw.glb tools/gltf; tools/gltf $<
$(AMP_GFX)&: shape/3common/amp/amp.glb tools/gltf; tools/gltf $<
$(CANNONLID_GFX)&: shape/3common/cannonlid/cannonlid.glb tools/gltf; tools/gltf $<
$(CANNON_GFX)&: shape/3common/cannon/cannon.glb tools/gltf; tools/gltf $<
$(CANNONBARREL_GFX)&: shape/3common/cannonbarrel/cannonbarrel.glb tools/gltf; tools/gltf $<
$(CHUCKYA_GFX)&: shape/3common/chuckya/chuckya.glb tools/gltf; tools/gltf $<
$(PURPLESW_GFX)&: shape/3common/purplesw/purplesw.glb tools/gltf; tools/gltf $<
$(LIFT_GFX)&: shape/3common/lift/lift.glb tools/gltf; tools/gltf $<
$(HEART_GFX)&: shape/3common/heart/heart.glb tools/gltf; tools/gltf $<
$(FLYGUY_GFX)&: shape/3common/flyguy/flyguy.glb tools/gltf; tools/gltf $<
$(BLOCK_GFX)&: shape/3common/block/block.glb tools/gltf; tools/gltf $<
$(ITEMBOX_GFX)&: shape/3common/itembox/itembox.glb tools/gltf; tools/gltf $<
$(GOOMBA_GFX)&: shape/3common/goomba/goomba.glb tools/gltf; tools/gltf $<
$(BOBOMB_GFX)&: shape/3common/bobomb/bobomb.glb tools/gltf; tools/gltf $<
$(PUSHBLOCK_GFX)&: shape/3common/pushblock/pushblock.glb tools/gltf; tools/gltf $<
$(DOTBOX_GFX)&: shape/3common/dotbox/dotbox.glb tools/gltf; tools/gltf $<
$(TESTLIFT_GFX)&: shape/3common/testlift/testlift.glb tools/gltf; tools/gltf -g $<
$(SHELL_OLD_GFX)&: shape/3common/shell/shell_old.glb tools/gltf; tools/gltf -g $<
$(SHELL_GFX)&: shape/3common/shell/shell.glb tools/gltf; tools/gltf $<
# Global
$(BUTTERFLY_GFX)&: shape/global/butterfly/butterfly.glb tools/gltf; tools/gltf -g $<
$(PIPE_GFX)&: shape/global/pipe/pipe.glb tools/gltf; tools/gltf $<
$(DOOR_GFX)&: shape/global/door/door.glb tools/gltf; tools/gltf $<
$(DOORKEY_GFX)&: shape/global/doorkey/doorkey.glb tools/gltf; tools/gltf $<
$(FISH_GFX)&: shape/global/fish/fish.glb tools/gltf; tools/gltf $<
$(CAP_GFX)&: shape/global/cap/cap.glb tools/gltf; tools/gltf $<
$(POWERSTAR_GFX)&: shape/global/powerstar/powerstar.glb tools/gltf; tools/gltf $<
$(SHADESTAR_GFX)&: shape/global/shadestar/shadestar.glb tools/gltf; tools/gltf $<
$(SIGNPOST_GFX)&: shape/global/signpost/signpost.glb tools/gltf; tools/gltf $<
$(TREE_GFX)&: shape/global/tree/tree.glb tools/gltf; tools/gltf $<
# Title
$(LOGO_GFX)&: stage/title/logo.glb tools/gltf; tools/gltf $<
$(DEBUG_GFX)&: stage/title/debug.glb tools/gltf; tools/gltf -g $<
# Select
$(FILE_GFX)&: stage/select/file/file.glb tools/gltf; tools/gltf $<
$(TILE_GFX)&: stage/select/tile/tile.glb tools/gltf; tools/gltf $<
# BoB
$(BATTLEFIELD_GFX)&: stage/bob/battlefield/battlefield.glb tools/gltf; tools/gltf $<
$(BOB_54_GFX)&: stage/bob/54/54.glb tools/gltf; tools/gltf $<
$(BOB_55_GFX)&: stage/bob/55/55.glb tools/gltf; tools/gltf $<
$(BOB_56_GFX)&: stage/bob/56/56.glb tools/gltf; tools/gltf $<
# PSS
$(MINISLIDER_GFX)&: stage/pss/minislider/minislider.glb tools/gltf; tools/gltf $<

# Common
shape/3common/bluecoinsw/map.h: shape/3common/bluecoinsw/bluecoinsw.obj tools/obj; tools/obj $< $@
shape/3common/cannonlid/map.h: shape/3common/cannonlid/cannonlid.obj tools/obj; tools/obj $< $@
shape/3common/purplesw/map.h: shape/3common/purplesw/purplesw.obj tools/obj; tools/obj $< $@
shape/3common/lift/map.h: shape/3common/lift/lift.obj tools/obj; tools/obj $< $@
shape/3common/block/map.h: shape/3common/block/block.obj tools/obj; tools/obj $< $@
shape/3common/pushblock/map.h: shape/3common/pushblock/pushblock.obj tools/obj; tools/obj $< $@
shape/3common/dotbox/map.h: shape/3common/dotbox/dotbox.obj tools/obj; tools/obj $< $@
shape/3common/testlift/map.h: shape/3common/testlift/testlift.obj tools/obj; tools/obj $< $@
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
# PSS
stage/pss/minislider/map.h: stage/pss/minislider/minislider.obj tools/obj; tools/obj $< $@
