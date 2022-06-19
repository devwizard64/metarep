VERSION ?= E0
LABEL   := SUPER MARIO 64

BUILD   := build/$(VERSION)

CODE_OBJ := \
	$(BUILD)/src/crt0.o             \
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
	$(BUILD)/src/mem.o              \
	$(BUILD)/src/save.o             $(BUILD)/src/save.data.o            \
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
	$(BUILD)/src/mem.o              \
	$(BUILD)/src/scene.o            \
	$(BUILD)/src/draw.o             \
	$(BUILD)/src/time.o             \
	$(BUILD)/src/course.o           \
	$(BUILD)/src/obj_physics.o      \
	$(BUILD)/src/obj_sfx.o          \
	$(BUILD)/src/dprint.o           \
	$(BUILD)/src/obj_data.o         \
	$(BUILD)/src/title.o

INS_SRC := data/audio/se.ins data/audio/music.ins
SBK_SRC := data/audio/se.sbk data/audio/music.sbk

TOOLS_OBJ := tools/mask tools/slienc tools/texture

$(eval REVISION := $$$(VERSION))
REGION  := $(subst $(REVISION),,$(VERSION))

CROSS   := mips-linux-gnu-
ARMIPS  := armips
FLIPS   := flips
IDO     := ido53
DONOR   := donor

ULTRA   := ultra
RES != $(MAKE) -C $(ULTRA)

CC      := $(CROSS)gcc
LD      := $(CROSS)ld
CPP     := $(CROSS)cpp
OBJCOPY := $(CROSS)objcopy
NM      := $(CROSS)nm
ARCH    := -mabi=32 -march=vr4300 -mfix4300 -mno-abicalls -fno-PIC -G 0
FLAG    := -I$(ULTRA)/include -Iinclude -I.
FLAG    += -DVERSION_$(VERSION) -DREGION=\'$(REGION)\' -DREVISION=$(REVISION)
FLAG    += -DBUILD=$(BUILD)
OPT     := -Os
WFLAG   := -Wall -Wextra -Werror=implicit-function-declaration
CCFLAG  := $(ARCH) -mno-check-zero-division -ffreestanding
CCFLAG  += -fno-common -fno-zero-initialized-in-bss -fno-toplevel-reorder
CCFLAG  += $(FLAG) $(OPT) $(WFLAG)
ASFLAG  := $(ARCH) $(FLAG) $(WFLAG) -Wno-variadic-macros
CPPFLAG := $(FLAG) -DULTRA=$(ULTRA) -Umips

IDO_CC      := $(IDO)/bin/cc
IDO_OPT     := -g
IDO_WFLAG   := -fullwarn -prototypes
IDO_CCFLAG  := -Wab,-r4300_mul -mips2 -non_shared -signed -G 0 -Xcpluscomm
IDO_CCFLAG  += -I$(IDO)/include $(FLAG) $(IDO_OPT) $(IDO_WFLAG)

OBJ := $(shell $(CPP) $(CPPFLAG) -P make/obj.mk)
OBJ := $(sort $(filter $(BUILD)/%, $(OBJ)))

.PHONY: default
default: $(BUILD)/app.z64

.PHONY: dist
dist: $(BUILD)/app.bps

.PHONY: clean
clean:
	rm -f -r build $(TOOLS_OBJ) tools/__pycache__ tools/*.pyc

$(BUILD)/app.bps: $(BUILD)/app.z64
	$(FLIPS) $(DONOR)/UNSM$(VERSION).z64 $< $@

$(BUILD)/app.z64: $(BUILD)/app.elf tools/mask
	$(OBJCOPY) --pad-to 0x800000 --gap-fill 0xFF -O binary $< $@
	tools/mask $@ NSM$(VERSION) "$(LABEL)"

$(BUILD)/app.elf: $(OBJ)
$(BUILD)/%.elf: $(BUILD)/make/%.ld
	$(LD) -Map $(@:.elf=.map) -o $@ -T $<

-include $(BUILD)/make/app.d
-include $(BUILD)/make/segment.d
$(BUILD)/make/app.ld:
$(BUILD)/make/%: make/% | $(BUILD)/make
	$(CPP) $(CPPFLAG) -MMD -MP -MT $@ -P -o $@ $<

include $(addsuffix .d,$(basename $(OBJ) $(CODE_OBJ) $(LIB_OBJ) $(AUDIO_OBJ) $(FACE_OBJ)))

$(BUILD)/code.o: make/rel.ld $(CODE_OBJ) $(AUDIO_OBJ)
	$(LD) --whole-archive -L$(ULTRA)/lib -r -o $@ -T $^ -lultra_rom

$(BUILD)/lib.o: make/rel.ld $(LIB_OBJ)
	$(LD) -r -o $@ -T $^

$(BUILD)/face.o: make/rel.ld $(FACE_OBJ)
	$(LD) -r -o $@ -T $^

$(BUILD)/code.d $(BUILD)/lib.d $(BUILD)/face.d:
	@echo $(@:.d=.o): $< > $@

include $(BUILD)/make/segment.mk
$(BUILD)/%.szp.h: $(BUILD)/%.szp.s;
$(BUILD)/%.szp.s: %.c make/szp.ld tools/slienc
	$(CC) $(CCFLAG) -c -o $(@:.szp.s=.o) $<
	$(LD) -Ttext $(ADDR) -T make/szp.ld -o $(@:.szp.s=.elf) $(@:.szp.s=.o)
	$(OBJCOPY) -O binary $(@:.szp.s=.elf) $(@:.szp.s=.bin)
	$(NM) -f posix $(@:.szp.s=.elf) > $(@:.szp.s=.sym)
	tools/slienc $@ $(@:.s=.h) $(@:.szp.s=.szp) $(@:.szp.s=.bin) $(@:.szp.s=.sym)
$(BUILD)/%.szp.d: %.c
	$(CC) $(CCFLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.s) $<

$(BUILD)/%.szp.s: %.bin tools/slienc
	@python3 -c "import os; print(\"a t 0 %x\" % os.path.getsize(\"$<\"))" > $(@:.szp.s=.sym)
	tools/slienc $@ $(@:.s=.h) $(@:.szp.s=.szp) $< $(@:.szp.s=.sym)
$(BUILD)/%.szp.d: %.bin
	@echo $(@:.d=.s): $< > $@

$(BUILD)/data/audio/tbl.s: $(BUILD)/data/audio/ctl.s;
$(BUILD)/data/audio/ctl.s: $(INS_SRC) tools/ic
	tools/ic $(FLAG) -ctl $@ -tbl $(@:ctl.s=tbl.s) $(INS_SRC)
$(BUILD)/data/audio/tbl.d: $(BUILD)/data/audio/ctl.d;
$(BUILD)/data/audio/ctl.d: $(INS_SRC) tools/ic
	tools/ic $(FLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.s) $(INS_SRC)

$(BUILD)/data/audio/bnk.s: $(BUILD)/data/audio/seq.s;
$(BUILD)/data/audio/seq.s: $(SBK_SRC)  tools/sbc
	tools/sbc $(FLAG) -seq $@ -bnk $(@:seq.s=bnk.s) $(SBK_SRC)
$(BUILD)/data/audio/bnk.d: $(BUILD)/data/audio/seq.d;
$(BUILD)/data/audio/seq.d: $(SBK_SRC) tools/sbc
	tools/sbc $(FLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.s) $(SBK_SRC)

$(BUILD)/%.o: $(BUILD)/%.s
	$(CC) $(ASFLAG) -c -o $@ $<

$(IDO_OBJ): $(BUILD)/%.o: %.c
	$(IDO_CC) $(IDO_CCFLAG) -c -o $@ $<

$(BUILD)/%.o: %.asm
	$(ARMIPS) -strequ BUILD $(BUILD) -sym $(@:.o=.sym) $<
	$(CC) $(ASFLAG) -c -o $@ $(<:.asm=.s)
$(BUILD)/%.d: %.asm
	@echo $(@:.d=.o): $< > $@

$(BUILD)/%.o: %.s
	$(CC) $(ASFLAG) -c -o $@ $<
$(BUILD)/%.d: %.s
	@echo $(@:.d=.o): $< > $@

$(BUILD)/%.o: %.sx
	$(CC) $(ASFLAG) -c -o $@ $<
$(BUILD)/%.d: %.sx
	$(CC) $(ASFLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.o) $<

$(BUILD)/%.o: %.c
	$(CC) $(CCFLAG) -c -o $@ $<
$(BUILD)/%.d: %.c
	$(CC) $(CCFLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.o) $<

$(BUILD)/%.h: %.png tools/texture
	tools/texture $@ $(filter %.png,$^)

-include $(addprefix $(BUILD)/,$(addsuffix .d,$(basename $(call obj,*.ply))))
$(BUILD)/data/shape/global/butterfly/%.h: GFXFLAG += -g
$(BUILD)/data/menu/title/debug/%.h: GFXFLAG += -g
$(BUILD)/%.h: %.ply tools/gfx
	tools/gfx $(GFXFLAG) -o $@ $<

$(BUILD)/%.h: %.obj tools/map
	tools/map $@ $<

$(BUILD)/%.inc.h: $(BUILD)/%.h;
$(BUILD)/%.h: %.txt tools/msg
	tools/msg $@ $<

$(BUILD)/data/%.o: data/%.bin

$(TOOLS_OBJ):
tools/%: tools/%.c
	cc -O2 -Wall -Wextra -Wpedantic -s -o $@ $<

dirs = $(foreach d,$(wildcard $1*),$(call dirs,$d/,$2) $(filter $(subst *,%,$2),$d))
obj = $(call dirs,src/,$1) $(call dirs,data/,$1)
BUILD_OBJ := $(call obj,*.c *.s *.sx *.asm *.bin *.png *.ply *.obj *.txt *.ins *.sbk)
$(foreach f,$(BUILD_OBJ),$(eval $f: | $(addprefix $(BUILD)/,$(dir $f))))
$(BUILD)/make $(sort $(addprefix $(BUILD)/,$(dir $(BUILD_OBJ)))):
	mkdir -p $@

print-%:
	$(info $* = $(flavor $*): [$($*)]) @true
