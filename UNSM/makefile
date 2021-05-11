VERSION ?= E0
BUILD   := build/$(VERSION)

MAIN_OBJ := \
	$(BUILD)/src/main.o             \
	$(BUILD)/src/app.o              \
	$(BUILD)/src/audio.o            \
	$(BUILD)/src/game.o             \
	$(BUILD)/src/player_touch.o     \
	$(BUILD)/src/player.o           \
	$(BUILD)/src/player_move.o      \
	$(BUILD)/src/player_demo.o      \
	$(BUILD)/src/player_hang.o      \
	$(BUILD)/src/player_stop.o      \
	$(BUILD)/src/player_ground.o    \
	$(BUILD)/src/player_air.o       \
	$(BUILD)/src/player_water.o     \
	$(BUILD)/src/player_grab.o      \
	$(BUILD)/src/player_gfx.o       \
	$(BUILD)/src/memory.o           \
	$(BUILD)/src/save.o             \
	$(BUILD)/src/world.o            \
	$(BUILD)/src/g_draw.o           \
	$(BUILD)/src/time.o             \
	$(BUILD)/src/szp.o              \
	$(BUILD)/src/camera.o           \
	$(BUILD)/src/course.o           \
	$(BUILD)/src/object_update.o    \
	$(BUILD)/src/object.o           \
	$(BUILD)/src/object_state_a.o   \
	$(BUILD)/src/object_move.o      \
	$(BUILD)/src/object_touch.o     \
	$(BUILD)/src/object_list.o      \
	$(BUILD)/src/object_sfx.o       \
	$(BUILD)/src/coin.o             \
	$(BUILD)/src/door.o             \
	$(BUILD)/src/object_debug.o     \
	$(BUILD)/src/wipe.o             \
	$(BUILD)/src/shadow.o           \
	$(BUILD)/src/background.o       \
	$(BUILD)/src/scroll.o           \
	$(BUILD)/src/object_gfx.o       \
	$(BUILD)/src/ripple.o           \
	$(BUILD)/src/print.o            \
	$(BUILD)/src/message.o          \
	$(BUILD)/src/particle_snow.o    \
	$(BUILD)/src/particle_lava.o    \
	$(BUILD)/src/obj_data.o         \
	$(BUILD)/src/hud.o              \
	$(BUILD)/src/object_state_b.o   \
	$(BUILD)/src/object_state_c.o   \
	$(BUILD)/src/data.o             \
	$(BUILD)/src/audio/a.o          \
	$(BUILD)/src/audio/b.o          \
	$(BUILD)/src/audio/c.o          \
	$(BUILD)/src/audio/d.o          \
	$(BUILD)/src/audio/e.o          \
	$(BUILD)/src/audio/f.o          \
	$(BUILD)/src/audio/g.o          \
	$(BUILD)/src/audio/data.o

MAIN2_OBJ := \
	$(BUILD)/src/math.o             \
	$(BUILD)/src/g.o                \
	$(BUILD)/src/g_script.o         \
	$(BUILD)/src/s_script.o         \
	$(BUILD)/src/map.o              \
	$(BUILD)/src/map_data.o         \
	$(BUILD)/src/o_script.o         \
	$(BUILD)/src/math.data.o        \
	$(BUILD)/src/math_table.o       \
	$(BUILD)/src/g_script.data.o    \
	$(BUILD)/src/s_script.data.o    \
	$(BUILD)/src/o_script.data.o    \
	$(BUILD)/src/map.data.o         \
	$(BUILD)/src/map_data.data.o    \
	$(BUILD)/src/main2.data.o

MENU_OBJ := \
	$(BUILD)/src/title.o            \
	$(BUILD)/src/title.data.o       \
	$(BUILD)/src/title_bg.o         \
	$(BUILD)/src/title_bg.data.o    \
	$(BUILD)/src/file_select.o      \
	$(BUILD)/src/file_select.data.o \
	$(BUILD)/src/star_select.o      \
	$(BUILD)/src/star_select.data.o \
	$(BUILD)/src/menu.data.o

FACE_OBJ := \
	$(BUILD)/src/face/main.o        \
	$(BUILD)/src/face/mem.o         \
	$(BUILD)/src/face/sfx.o         \
	$(BUILD)/src/face/draw.o        \
	$(BUILD)/src/face/object.o      \
	$(BUILD)/src/face/skin.o        \
	$(BUILD)/src/face/particle.o    \
	$(BUILD)/src/face/dynlist.o     \
	$(BUILD)/src/face/gadget.o      \
	$(BUILD)/src/face/stdio.o       \
	$(BUILD)/src/face/joint.o       \
	$(BUILD)/src/face/net.o         \
	$(BUILD)/src/face/math.o        \
	$(BUILD)/src/face/shape.o       \
	$(BUILD)/src/face/gfx.o         \
	$(BUILD)/src/face/data.o

CODE_OBJ := \
	$(BUILD)/src/header.o   \
	$(BUILD)/src/main.ld.o  \
	$(BUILD)/src/main2.ld.o \
	$(MENU_OBJ)             \
	$(BUILD)/src/face.ld.o

SRC_OBJ := $(MAIN_OBJ) $(MAIN2_OBJ) $(MENU_OBJ) $(FACE_OBJ)

CC      := mips-linux-gnu-gcc
LD      := mips-linux-gnu-ld
CPP     := mips-linux-gnu-cpp
OBJCOPY := mips-linux-gnu-objcopy
NM      := mips-linux-gnu-nm
CC      += -march=vr4300 -mfix4300 -mfp32 -mno-abicalls -mno-check-zero-division
CC      += -fno-PIC -ffreestanding -fno-common -fno-zero-initialized-in-bss
CC      += -fno-toplevel-reorder -G 0

FLAG    := -I ultra/include -I include -I . -D BUILD=$(BUILD) -D _$(VERSION)
CC      += $(FLAG) -Wall -Wextra -Wpedantic -O2
CPP     += $(FLAG)

OBJ := $(shell $(CPP) -P -o - make/obj.mk | tr "\n" " ")

$(BUILD)/app.z64: $(BUILD)/app.elf | exe/build
	$(OBJCOPY) --pad-to 0x00800000 --gap-fill 0xFF -O binary $< $@
	exe/build/crc $@

$(BUILD)/app.elf: $(BUILD)/make/main.ld $(CODE_OBJ) $(OBJ)
	$(LD) --accept-unknown-input-arch -Map $(@:.elf=.map) -o $@ -T $<

$(BUILD)/make/%: make/% | $(BUILD)/make
	$(CPP) -MMD -MP -MT $@ -P -o $@ $<

$(BUILD)/src/main.ld.o: $(MAIN_OBJ) | ultra/lib
	$(LD) --whole-archive -L ultra/lib -r -o $@ $^ -l ultra_rom

$(BUILD)/src/main2.ld.o: $(MAIN2_OBJ)
$(BUILD)/src/face.ld.o:  $(FACE_OBJ)
$(BUILD)/%.ld.o:
	$(LD) -r -o $@ $^

include $(BUILD)/make/segment.mk
$(BUILD)/%.szp.o: %.c make/szp.ld | exe/build
	$(CC) -MMD -MP -MF $(@:.o=.d) -MT $@ -c -o $@.o $<
	$(LD) -Ttext $(ADDR) -T make/szp.ld -o $@.elf $@.o
	$(OBJCOPY) -O binary $@.elf $@.bin
	$(NM) -f posix $@.elf > $@.sym
	exe/build/szp $@.szp $@.bin $@.sym
	$(OBJCOPY) -O elf32-tradbigmips -I binary $@.szp $@.szp.o
	$(LD) --accept-unknown-input-arch -r -o $@ -R $@.elf $@.szp.o

$(BUILD)/%.szp.d: %.c
	$(CC) -MM -MG -MP -MF $@ -MT $(@:.d=.o) $<

$(BUILD)/%.szp.o: %.bin | exe/build
	printf "a D 0 %X\n" $(shell stat --printf="%s" $<) > $@.sym
	exe/build/szp $@.szp $< $@.sym
	$(OBJCOPY) -O elf32-tradbigmips -I binary $@.szp $@

$(BUILD)/%.szp.d: %.bin
	touch $@

$(BUILD)/%.o: %.c
	$(CC) -MMD -MP -c -o $@ $<

$(BUILD)/%.o: %.S
	$(CC) -MMD -MP -c -o $@ $<

$(BUILD)/%.d: %.c
	$(CC) -MM -MG -MP -MF $@ -MT $(@:.d=.o) $<

$(BUILD)/%.d: %.S
	$(CC) -MM -MG -MP -MF $@ -MT $(@:.d=.o) $<

$(BUILD)/data/%.o: data/%.bin
	touch $(@:.o=.d)
	$(OBJCOPY) -O elf32-tradbigmips -I binary $< $@

$(BUILD)/data/%.d: data/%.bin
	touch $@

$(BUILD)/%.h: %.png | exe/build
	exe/build/texture $@ $^

$(BUILD)/%.h: %.ply
	exe/gfx $@ $<

$(BUILD)/%.h: %.obj
	exe/map $@ $<

$(BUILD)/%.h: %.txt
	exe/msg $@ $<

dirs = $(foreach d,$(wildcard $1*),$(call dirs,$d/,$2) \
	$(filter $(subst *,%,$2),$d))
obj = $(call dirs,src/,$1) $(call dirs,data/,$1)
BUILD_OBJ := $(call obj,*.c *.S *.bin *.png *.ply *.obj *.txt)
$(foreach f,$(BUILD_OBJ),$(eval $f: | $(addprefix $(BUILD)/,$(dir $f))))
$(BUILD)/make $(sort $(addprefix $(BUILD)/,$(dir $(BUILD_OBJ)))):
	mkdir -p $@

ultra/lib:
	make -C ultra

exe/build:
	make -C exe

clean:
	rm -rf build

print-%:
	$(info $* = $(flavor $*): [$($*)]) @true

-include $(BUILD)/make/main.d
-include $(BUILD)/make/segment.d
include $(addsuffix .d,$(basename $(SRC_OBJ) $(OBJ)))
-include $(addprefix $(BUILD)/,$(addsuffix .d,$(basename $(call obj,*.ply))))

.PHONY: clean
