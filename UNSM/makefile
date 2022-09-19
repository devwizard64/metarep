VERSION ?= E00
LABEL   := SUPER MARIO 64

BUILD   := build/$(VERSION)

CODE_OBJ := \
	$(BUILD)/src/main.o             \
	$(BUILD)/src/app.o              \
	$(BUILD)/src/audio.o            \
	$(BUILD)/src/game.o             $(BUILD)/src/game.data.o            \
	$(BUILD)/src/pl_collision.o     $(BUILD)/src/pl_collision.data.o    \
	$(BUILD)/src/player.o           $(BUILD)/src/player.data.o          \
	$(BUILD)/src/pl_physics.o       $(BUILD)/src/pl_physics.data.o      \
	$(BUILD)/src/pl_demo.o          $(BUILD)/src/pl_demo.data.o         \
	$(BUILD)/src/pl_hang.o          $(BUILD)/src/pl_hang.data.o         \
	$(BUILD)/src/pl_wait.o          $(BUILD)/src/pl_wait.data.o         \
	$(BUILD)/src/pl_walk.o          $(BUILD)/src/pl_walk.data.o         \
	$(BUILD)/src/pl_jump.o          $(BUILD)/src/pl_jump.data.o         \
	$(BUILD)/src/pl_swim.o          $(BUILD)/src/pl_swim.data.o         \
	$(BUILD)/src/pl_grab.o          $(BUILD)/src/pl_grab.data.o         \
	$(BUILD)/src/pl_callback.o      $(BUILD)/src/pl_callback.data.o     \
	$(BUILD)/src/memory.o           \
	$(BUILD)/src/save.o             \
	$(BUILD)/src/scene.o            \
	$(BUILD)/src/draw.o             \
	$(BUILD)/src/time.o             \
	$(BUILD)/src/slidec.o           \
	$(BUILD)/src/camera.o           $(BUILD)/src/camera.data.o          \
	$(BUILD)/src/course.o           \
	$(BUILD)/src/object.o           $(BUILD)/src/object.data.o          \
	$(BUILD)/src/obj_lib.o          $(BUILD)/src/obj_lib.data.o         \
	$(BUILD)/src/object_a.o         $(BUILD)/src/object_a.data.o        \
	$(BUILD)/src/obj_physics.o      \
	$(BUILD)/src/obj_collision.o    $(BUILD)/src/obj_collision.data.o   \
	$(BUILD)/src/obj_list.o         $(BUILD)/src/obj_list.data.o        \
	$(BUILD)/src/obj_sfx.o          \
	$(BUILD)/src/obj_debug.o        $(BUILD)/src/obj_debug.data.o       \
	$(BUILD)/src/wipe.o             $(BUILD)/src/wipe.data.o            \
	$(BUILD)/src/shadow.o           $(BUILD)/src/shadow.data.o          \
	$(BUILD)/src/background.o       $(BUILD)/src/background.data.o      \
	$(BUILD)/src/scroll.o           $(BUILD)/src/scroll.data.o          \
	$(BUILD)/src/obj_shape.o        $(BUILD)/src/obj_shape.data.o       \
	$(BUILD)/src/ripple.o           $(BUILD)/src/ripple.data.o          \
	$(BUILD)/src/dprint.o           \
	$(BUILD)/src/message.o          $(BUILD)/src/message.data.o         \
	$(BUILD)/src/weather_snow.o     $(BUILD)/src/weather_snow.data.o    \
	$(BUILD)/src/weather_lava.o     $(BUILD)/src/weather_lava.data.o    \
	$(BUILD)/src/obj_data.o         \
	$(BUILD)/src/hud.o              $(BUILD)/src/hud.data.o             \
	$(BUILD)/src/object_b.o         $(BUILD)/src/object_b.data.o        \
	$(BUILD)/src/object_c.o         $(BUILD)/src/object_c.data.o

LIB_OBJ := \
	$(BUILD)/src/math.o             $(BUILD)/src/math.data.o            \
	$(BUILD)/src/math_table.o       \
	$(BUILD)/src/shape.o            \
	$(BUILD)/src/s_script.o         $(BUILD)/src/s_script.data.o        \
	$(BUILD)/src/p_script.o         $(BUILD)/src/p_script.data.o        \
	$(BUILD)/src/map.o              $(BUILD)/src/map.data.o             \
	$(BUILD)/src/map_data.o         $(BUILD)/src/map_data.data.o        \
	$(BUILD)/src/o_script.o         $(BUILD)/src/o_script.data.o

AUDIO_OBJ := \
	$(BUILD)/src/audio/a.o          $(BUILD)/src/audio/a.data.o         \
	$(BUILD)/src/audio/b.o          $(BUILD)/src/audio/b.data.o         \
	$(BUILD)/src/audio/c.o          \
	$(BUILD)/src/audio/d.o          $(BUILD)/src/audio/d.data.o         \
	$(BUILD)/src/audio/e.o          $(BUILD)/src/audio/e.data.o         \
	$(BUILD)/src/audio/f.o          $(BUILD)/src/audio/f.data.o         \
	$(BUILD)/src/audio/g.o          $(BUILD)/src/audio/g.data.o         \
	$(BUILD)/src/audio/data.o

FACE_OBJ := \
	$(BUILD)/src/face/main.o        $(BUILD)/src/face/main.data.o       \
	$(BUILD)/src/face/mem.o         $(BUILD)/src/face/mem.data.o        \
	$(BUILD)/src/face/sfx.o         \
	$(BUILD)/src/face/draw.o        $(BUILD)/src/face/draw.data.o       \
	$(BUILD)/src/face/object.o      $(BUILD)/src/face/object.data.o     \
	$(BUILD)/src/face/skin.o        $(BUILD)/src/face/skin.data.o       \
	$(BUILD)/src/face/particle.o    $(BUILD)/src/face/particle.data.o   \
	$(BUILD)/src/face/dynlist.o     $(BUILD)/src/face/dynlist.data.o    \
	$(BUILD)/src/face/gadget.o      $(BUILD)/src/face/gadget.data.o     \
	$(BUILD)/src/face/stdio.o       $(BUILD)/src/face/stdio.data.o      \
	$(BUILD)/src/face/joint.o       $(BUILD)/src/face/joint.data.o      \
	$(BUILD)/src/face/net.o         $(BUILD)/src/face/net.data.o        \
	$(BUILD)/src/face/math.o        $(BUILD)/src/face/math.data.o       \
	$(BUILD)/src/face/shape.o       $(BUILD)/src/face/shape.data.o      \
	$(BUILD)/src/face/gfx.o         $(BUILD)/src/face/gfx.data.o        \
	$(BUILD)/src/face/data.o

IDO_OBJ := \
	$(BUILD)/src/main.o             \
	$(BUILD)/src/app.o              \
	$(BUILD)/src/audio.o            \
	$(BUILD)/src/memory.o           \
	$(BUILD)/src/save.o             \
	$(BUILD)/src/scene.o            \
	$(BUILD)/src/draw.o             \
	$(BUILD)/src/time.o             \
	$(BUILD)/src/course.o           \
	$(BUILD)/src/obj_physics.o      \
	$(BUILD)/src/obj_sfx.o          \
	$(BUILD)/src/dprint.o           \
	$(BUILD)/src/obj_data.o         \
	$(BUILD)/src/title.o            \
	$(BUILD)/src/title_bg.o

INS_SRC := data/audio/se.ins data/audio/music.ins
SBK_SRC := data/audio/se.sbk data/audio/music.sbk

TOOLS_OBJ := tools/mask tools/slienc tools/texture

$(eval REVISION := $$$(VERSION))
REGION  := $(subst $(REVISION),,$(VERSION))

DONOR   := donor

ULTRA   := ultra
RES != $(MAKE) -C $(ULTRA)

FLAG    := -I$(ULTRA)/include -Iinclude -I. -D_ULTRA64
FLAG    += -DVERSION_$(VERSION) -DREGION=\'$(REGION)\' -DREVISION=0x$(REVISION)
FLAG    += -DBUILD=$(BUILD)

CC          := gcc
CCFLAG      := -O2 -Wall -Wextra -Wpedantic

U64_HOST    := mips-linux-gnu
U64_CC      := $(U64_HOST)-gcc
U64_LD      := $(U64_HOST)-ld
U64_CPP     := $(U64_HOST)-cpp
U64_OBJCOPY := $(U64_HOST)-objcopy
U64_NM      := $(U64_HOST)-nm
U64_ARCH    := -mabi=32 -march=vr4300 -mfix4300 -mno-abicalls -fno-PIC -G 0
U64_OPT     := -Os
U64_WARN    := -Wall -Wextra -Werror=implicit-function-declaration
U64_CCFLAG  := $(U64_ARCH) -mno-check-zero-division -ffreestanding
U64_CCFLAG  += -fno-common -fno-zero-initialized-in-bss -fno-toplevel-reorder
U64_CCFLAG  += $(FLAG) $(U64_OPT) $(U64_WARN)
U64_ASFLAG  := $(U64_ARCH) $(FLAG) -Wno-variadic-macros
U64_CPPFLAG := $(FLAG) -DULTRA=$(ULTRA) -Umips

IDO_CC      := $(IDO)/bin/cc
IDO_OPT     := -g
IDO_WARN    := -fullwarn -prototypes
IDO_CCFLAG  := -Wab,-r4300_mul -mips2 -non_shared -signed -G 0 -Xcpluscomm
IDO_CCFLAG  += -I$(IDO)/include $(FLAG) $(IDO_OPT) $(IDO_WARN)

OBJ := $(shell $(U64_CPP) $(U64_CPPFLAG) -P make/obj.mk)
OBJ := $(sort $(filter $(BUILD)/%, $(OBJ)))

.PHONY: default
default: $(BUILD)/app.z64

.PHONY: dist
dist: $(BUILD)/app.bps

.PHONY: clean
clean:
	rm -f -r build $(TOOLS_OBJ) tools/__pycache__ tools/*.pyc

$(BUILD)/app.bps: $(BUILD)/app.z64
	flips $(DONOR)/UNSM$(VERSION).z64 $< $@

$(BUILD)/app.z64: $(BUILD)/app.elf tools/mask
	$(U64_OBJCOPY) --pad-to 0x800000 --gap-fill 0xFF -O binary $< $@
	tools/mask $@ NSM$(VERSION) "$(LABEL)"

$(BUILD)/app.elf: $(OBJ)
$(BUILD)/%.elf: $(BUILD)/make/%.ld
	@mkdir -p $(dir $@)
	$(U64_LD) -Map $(@:.elf=.map) -o $@ -T $<

-include $(BUILD)/make/app.d
-include $(BUILD)/make/segment.d
$(BUILD)/make/app.ld:
$(BUILD)/make/%: make/%
	@mkdir -p $(dir $@)
	$(U64_CPP) $(U64_CPPFLAG) -MMD -MP -MT $@ -P -o $@ $<

include $(addsuffix .d,$(basename $(OBJ) $(CODE_OBJ) $(LIB_OBJ) $(AUDIO_OBJ) $(FACE_OBJ)))

$(BUILD)/code.o: make/rel.ld $(CODE_OBJ) $(AUDIO_OBJ)
	@mkdir -p $(dir $@)
	$(U64_LD) --whole-archive -L$(ULTRA)/lib -r -o $@ -T $^ -lultra_rom

$(BUILD)/lib.o: make/rel.ld $(LIB_OBJ)
	@mkdir -p $(dir $@)
	$(U64_LD) -r -o $@ -T $^

$(BUILD)/face.o: make/rel.ld $(FACE_OBJ)
	@mkdir -p $(dir $@)
	$(U64_LD) -r -o $@ -T $^

$(BUILD)/code.d $(BUILD)/lib.d $(BUILD)/face.d:
	@mkdir -p $(dir $@)
	@echo $(@:.d=.o): $< > $@

$(BUILD)/%.o: %.asm
	@mkdir -p $(dir $@)
	armips -strequ BUILD $(BUILD) -sym $(@:.o=.sym) $<
	$(U64_CC) $(U64_ASFLAG) -c -o $@ $(<:.asm=.s)
$(BUILD)/%.d: %.asm
	@mkdir -p $(dir $@)
	@echo $(@:.d=.o): $< > $@

$(BUILD)/%.o: %.s
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_ASFLAG) -c -o $@ $<
$(BUILD)/%.d: %.s
	@mkdir -p $(dir $@)
	@echo $(@:.d=.o): $< > $@

$(BUILD)/%.o: %.sx
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_ASFLAG) -c -o $@ $<
$(BUILD)/%.d: %.sx
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_ASFLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.o) $<

$(BUILD)/%.o: %.c
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_CCFLAG) -c -o $@ $<
$(BUILD)/%.d: %.c
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_CCFLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.o) $<

$(IDO_OBJ): $(BUILD)/%.o: %.c
	@mkdir -p $(dir $@)
	$(IDO_CC) $(IDO_CCFLAG) -c -o $@ $<

$(BUILD)/%.o: $(BUILD)/%.s
	$(U64_CC) $(U64_ASFLAG) -c -o $@ $<

include $(BUILD)/make/segment.mk
$(BUILD)/%.szp.h: $(BUILD)/%.szp.s;
$(BUILD)/%.szp.s: %.c make/szp.ld tools/slienc
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_CCFLAG) -c -o $(@:.szp.s=.o) $<
	$(U64_LD) -Ttext $(ADDR) -T make/szp.ld -o $(@:.szp.s=.elf) $(@:.szp.s=.o)
	$(U64_OBJCOPY) -O binary $(@:.szp.s=.elf) $(@:.szp.s=.bin)
	$(U64_NM) -f posix $(@:.szp.s=.elf) > $(@:.szp.s=.sym)
	tools/slienc $@ $(@:.s=.h) $(@:.szp.s=.szp) $(@:.szp.s=.bin) $(@:.szp.s=.sym)
$(BUILD)/%.szp.d: %.c
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_CCFLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.s) $<

$(BUILD)/%.szp.s: %.bin tools/slienc
	@mkdir -p $(dir $@)
	@python3 -c "import os; print(\"a t 0 %x\" % os.path.getsize(\"$<\"))" > $(@:.szp.s=.sym)
	tools/slienc $@ $(@:.s=.h) $(@:.szp.s=.szp) $< $(@:.szp.s=.sym)
$(BUILD)/%.szp.d: %.bin
	@mkdir -p $(dir $@)
	@echo $(@:.d=.s): $< > $@

$(BUILD)/data/audio/tbl.s: $(BUILD)/data/audio/ctl.s;
$(BUILD)/data/audio/ctl.s: $(INS_SRC) tools/ic
	@mkdir -p $(dir $@)
	tools/ic $(FLAG) -ctl $@ -tbl $(@:ctl.s=tbl.s) $(INS_SRC)
$(BUILD)/data/audio/tbl.d: $(BUILD)/data/audio/ctl.d;
$(BUILD)/data/audio/ctl.d: $(INS_SRC) tools/ic
	@mkdir -p $(dir $@)
	tools/ic $(FLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.s) $(INS_SRC)

$(BUILD)/data/audio/bnk.s: $(BUILD)/data/audio/seq.s;
$(BUILD)/data/audio/seq.s: $(SBK_SRC) tools/sbc
	@mkdir -p $(dir $@)
	tools/sbc $(FLAG) -seq $@ -bnk $(@:seq.s=bnk.s) $(SBK_SRC)
$(BUILD)/data/audio/bnk.d: $(BUILD)/data/audio/seq.d;
$(BUILD)/data/audio/seq.d: $(SBK_SRC) tools/sbc
	@mkdir -p $(dir $@)
	tools/sbc $(FLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.s) $(SBK_SRC)

$(BUILD)/%.h: %.png tools/texture
	@mkdir -p $(dir $@)
	tools/texture $@ $(filter %.png,$^)

-include $(addprefix $(BUILD)/,$(addsuffix .d,$(basename $(call obj,*.ply))))
$(BUILD)/data/shape/global/butterfly/%.h: GFXFLAG += -g
$(BUILD)/data/menu/title/debug/%.h: GFXFLAG += -g
$(BUILD)/%.h: %.ply tools/gfx
	@mkdir -p $(dir $@)
	tools/gfx $(GFXFLAG) -o $@ $<

$(BUILD)/%.h: %.obj tools/map
	@mkdir -p $(dir $@)
	tools/map $@ $<

$(BUILD)/%.inc.h: $(BUILD)/%.h;
$(BUILD)/%.h: %.txt tools/msg
	@mkdir -p $(dir $@)
	tools/msg $@ $<

$(BUILD)/%.aifc: %.aiff
	@mkdir -p $(dir $@)
	tabledesign -s 1 $< > $(@:.aifc=.table)
	vadpcm_enc -c $(@:.aifc=.table) $< $@

$(BUILD)/data/%.o: data/%.bin

$(TOOLS_OBJ):
tools/%: tools/%.c
	$(CC) $(CCFLAG) -s -o $@ $<

print-%:
	$(info $* = $(flavor $*): [$($*)]) @true
