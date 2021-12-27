VERSION ?= E0
LABEL   := SUPER MARIO 64

BUILD   := build/$(VERSION)

MAIN_OBJ := \
	$(BUILD)/src/main.o             $(BUILD)/src/main.data.o            \
	$(BUILD)/src/app.o              $(BUILD)/src/app.data.o             \
	$(BUILD)/src/audio.o            $(BUILD)/src/audio.data.o           \
	$(BUILD)/src/game.o             $(BUILD)/src/game.data.o            \
	$(BUILD)/src/pl_collision.o     $(BUILD)/src/pl_collision.data.o    \
	$(BUILD)/src/player.o           $(BUILD)/src/player.data.o          \
	$(BUILD)/src/pl_physics.o       $(BUILD)/src/pl_physics.data.o      \
	$(BUILD)/src/pl_demo.o          $(BUILD)/src/pl_demo.data.o         \
	$(BUILD)/src/pl_hang.o          $(BUILD)/src/pl_hang.data.o         \
	$(BUILD)/src/pl_stop.o          $(BUILD)/src/pl_stop.data.o         \
	$(BUILD)/src/pl_ground.o        $(BUILD)/src/pl_ground.data.o       \
	$(BUILD)/src/pl_air.o           $(BUILD)/src/pl_air.data.o          \
	$(BUILD)/src/pl_water.o         $(BUILD)/src/pl_water.data.o        \
	$(BUILD)/src/pl_grab.o          $(BUILD)/src/pl_grab.data.o         \
	$(BUILD)/src/pl_callback.o      $(BUILD)/src/pl_callback.data.o     \
	$(BUILD)/src/mem.o              $(BUILD)/src/mem.data.o             \
	$(BUILD)/src/save.o             $(BUILD)/src/save.data.o            \
	$(BUILD)/src/world.o            $(BUILD)/src/world.data.o           \
	$(BUILD)/src/shape_draw.o       $(BUILD)/src/shape_draw.data.o      \
	$(BUILD)/src/time.o             $(BUILD)/src/time.data.o            \
	$(BUILD)/src/slidec.o           \
	$(BUILD)/src/camera.o           $(BUILD)/src/camera.data.o          \
	$(BUILD)/src/course.o           \
	$(BUILD)/src/object.o           $(BUILD)/src/object.data.o          \
	$(BUILD)/src/obj_lib.o          $(BUILD)/src/obj_lib.data.o         \
	$(BUILD)/src/object_a.o         $(BUILD)/src/object_a.data.o        \
	$(BUILD)/src/obj_physics.o      $(BUILD)/src/obj_physics.data.o     \
	$(BUILD)/src/obj_collision.o    $(BUILD)/src/obj_collision.data.o   \
	$(BUILD)/src/obj_list.o         $(BUILD)/src/obj_list.data.o        \
	$(BUILD)/src/obj_sfx.o          $(BUILD)/src/obj_sfx.data.o         \
	$(BUILD)/src/obj_debug.o        $(BUILD)/src/obj_debug.data.o       \
	$(BUILD)/src/wipe.o             $(BUILD)/src/wipe.data.o            \
	$(BUILD)/src/shadow.o           $(BUILD)/src/shadow.data.o          \
	$(BUILD)/src/background.o       $(BUILD)/src/background.data.o      \
	$(BUILD)/src/scroll.o           $(BUILD)/src/scroll.data.o          \
	$(BUILD)/src/obj_shape.o        $(BUILD)/src/obj_shape.data.o       \
	$(BUILD)/src/ripple.o           $(BUILD)/src/ripple.data.o          \
	$(BUILD)/src/print.o            $(BUILD)/src/print.data.o           \
	$(BUILD)/src/message.o          $(BUILD)/src/message.data.o         \
	$(BUILD)/src/weather_snow.o     $(BUILD)/src/weather_snow.data.o    \
	$(BUILD)/src/weather_lava.o     $(BUILD)/src/weather_lava.data.o    \
	$(BUILD)/src/obj_data.o         $(BUILD)/src/obj_data.data.o        \
	$(BUILD)/src/hud.o              $(BUILD)/src/hud.data.o             \
	$(BUILD)/src/object_b.o         $(BUILD)/src/object_b.data.o        \
	$(BUILD)/src/object_c.o         $(BUILD)/src/object_c.data.o

MAIN2_OBJ := \
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

MAIN_OBJ    += $(AUDIO_OBJ)
SRC_OBJ     := $(MAIN_OBJ) $(MAIN2_OBJ) $(FACE_OBJ)

ULTRA   := ultra
EXE     := exe

RES != make -C $(ULTRA)
RES != make -C $(EXE)

CC      := mips-linux-gnu-gcc
LD      := mips-linux-gnu-ld
CPP     := mips-linux-gnu-cpp
OBJCOPY := mips-linux-gnu-objcopy
NM      := mips-linux-gnu-nm

FLAG    := -I$(ULTRA)/include -Iinclude -I.
FLAG    += -D__$(VERSION)__ -DBUILD=$(BUILD)
CCFLAG  := -march=vr4300 -mfix4300 -mfp32 -mno-abicalls -mno-check-zero-division
CCFLAG  += -fno-PIC -ffreestanding -fno-common -fno-zero-initialized-in-bss
CCFLAG  += -fno-toplevel-reorder -G0
CCFLAG  += $(FLAG) -Os -Wall -Wextra -Wpedantic
ASFLAG  := $(CCFLAG) -Wno-variadic-macros
CPPFLAG := $(FLAG) -DULTRA=$(ULTRA)

ARMIPS  := armips

OBJ := $(shell $(CPP) $(CPPFLAG) -P -o - make/obj.mk | tr "\n" " ")
SEQ := $(shell $(CPP) $(CPPFLAG) -P -o - make/seq.mk | tr "\n" " ")

OBJ := $(sort $(filter $(BUILD)/%, $(OBJ)))

$(BUILD)/app.z64: $(BUILD)/app.elf
	$(OBJCOPY) --pad-to 0x800000 --gap-fill 0xFF -O binary $< $@
	$(EXE)/mask $@ NSM$(VERSION) "$(LABEL)"

$(BUILD)/app.elf: $(BUILD)/make/main.ld $(OBJ)
	$(LD) --accept-unknown-input-arch -Map $(@:.elf=.map) -o $@ -T $<

include $(addsuffix .d,$(basename $(SRC_OBJ) $(OBJ)))

-include $(BUILD)/make/main.d
-include $(BUILD)/make/segment.d
$(BUILD)/make/%: make/% | $(BUILD)/make
	$(CPP) $(CPPFLAG) -MMD -MP -MT $@ -P -o $@ $<

$(BUILD)/src/main.ld.o: $(MAIN_OBJ)
	$(LD) --whole-archive -L$(ULTRA)/lib -r -o $@ $^ -lultra_rom

$(BUILD)/src/main2.ld.o: $(MAIN2_OBJ)
$(BUILD)/src/face.ld.o:  $(FACE_OBJ)
$(BUILD)/src/%.ld.o: | $(BUILD)/src
	$(LD) -r -o $@ $^
$(BUILD)/src/%.ld.d: | $(BUILD)/src
	touch $@

include $(BUILD)/make/segment.mk
$(BUILD)/%.szp.h: $(BUILD)/%.szp.o;
$(BUILD)/%.szp.o: %.c make/szp.ld
	$(CC) $(CCFLAG) -MMD -MP -MF $(@:.o=.d) -MT $@ -c -o $@.o $<
	$(LD) -Ttext $(ADDR) -T make/szp.ld -o $@.elf $@.o
	$(OBJCOPY) -O binary $@.elf $@.bin
	$(NM) -f posix $@.elf > $@.sym
	$(EXE)/slienc $@.szp $(@:.o=.h) $@.bin $@.sym
	$(OBJCOPY) -O elf32-tradbigmips -I binary $@.szp $@.szp.o
	$(LD) --accept-unknown-input-arch -r -o $@ -R $@.elf $@.szp.o
$(BUILD)/%.szp.d: %.c
	$(CC) $(CCFLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.o) $<

$(BUILD)/%.szp.o: %.bin
	printf "a t 0 %x\n" $(shell stat --printf="%s" $<) > $@.sym
	$(EXE)/slienc $@.szp $(@:.o=.h) $< $@.sym
	$(OBJCOPY) -O elf32-tradbigmips -I binary $@.szp $@
$(BUILD)/%.szp.d: %.bin
	touch $@

$(BUILD)/%.o: %.asm
	$(ARMIPS) -strequ BUILD $(BUILD) -sym $(@:.o=.sym) $<
	$(CC) $(ASFLAG) -MMD -MP -c -o $@ $(<:.asm=.S)
$(BUILD)/%.d: %.asm
	$(CC) $(ASFLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.o) $<

$(BUILD)/%.o: %.S
	$(CC) $(ASFLAG) -MMD -MP -c -o $@ $<
$(BUILD)/%.d: %.S
	$(CC) $(ASFLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.o) $<

$(BUILD)/%.o: %.c
	$(CC) $(CCFLAG) -MMD -MP -c -o $@ $<
$(BUILD)/%.d: %.c
	$(CC) $(CCFLAG) -MM -MG -MP -MF $@ -MT $(@:.d=.o) $<

$(BUILD)/%.h: %.png
	$(EXE)/texture $@ $^

-include $(addprefix $(BUILD)/,$(addsuffix .d,$(basename $(call obj,*.ply))))
$(BUILD)/data/shape/global/butterfly/%.h: GFXFLAG += -g
$(BUILD)/data/menu/title/debug/%.h: GFXFLAG += -g
$(BUILD)/%.h: %.ply
	$(EXE)/gfx $(GFXFLAG) -o $@ $<

$(BUILD)/%.h: %.obj
	$(EXE)/map $@ $<

$(BUILD)/%.h: %.txt
	$(EXE)/msg $@ $<

data/%.S: data/%.bin

$(BUILD)/data/audio/seq.o: $(SEQ)
$(BUILD)/data/audio/seq/%.seq: data/audio/seq/%.seq
	cp $< $@

dirs = $(foreach d,$(wildcard $1*),$(call dirs,$d/,$2) \
	$(filter $(subst *,%,$2),$d))
obj = $(call dirs,src/,$1) $(call dirs,data/,$1)
BUILD_OBJ := $(call obj,*.asm *.S *.c *.bin *.png *.ply *.obj *.txt *.seq)
$(foreach f,$(BUILD_OBJ),$(eval $f: | $(addprefix $(BUILD)/,$(dir $f))))
$(BUILD)/make $(BUILD)/src $(sort $(addprefix $(BUILD)/,$(dir $(BUILD_OBJ)))):
	mkdir -p $@

.PHONY: clean
clean:
	rm -rf build

print-%:
	$(info $* = $(flavor $*): [$($*)]) @true
