TARGET  ?= E0

BUILD   := build/$(TARGET)
TITLE   := SUPER MARIO 64
$(eval VERSION := $$$(TARGET))
REGION  := $(subst $(VERSION),,$(TARGET))

CC          := gcc
CFLAGS      := -O2 -Wall -Wextra -Wpedantic

U64_PREFIX  := mips-linux-gnu-
U64_CC      := $(U64_PREFIX)gcc
U64_LD      := $(U64_PREFIX)ld
U64_AR      := $(U64_PREFIX)ar
U64_OBJCOPY := $(U64_PREFIX)objcopy
U64_ARCH    := -mabi=32 -march=vr4300 -mfix4300
U64_OPT     := -Os
U64_WARN    := -Wall -Wextra -Werror=implicit-function-declaration
U64_CPPFLAGS = -Ilibultra/include -Iinclude -I. -I$(BUILD) -D_ULTRA64 -DTARGET_$(TARGET) -DREGION=\'$(REGION)\' -DVERSION=$(VERSION)
U64_CFLAGS = $(U64_ARCH) -mno-abicalls -fno-PIC -mno-check-zero-division -ffreestanding -fno-common -fno-zero-initialized-in-bss -fno-toplevel-reorder -G 0 $(U64_OPT) $(U64_WARN)
U64_ASFLAGS = $(U64_ARCH) -mno-abicalls -fno-PIC

IDO_CC      := $(IDO)/bin/cc
IDO_ARCH    := -mips2
IDO_OPT     := -g
IDO_WARN    := -fullwarn -prototypes
IDO_CPPFLAGS = -I$(IDO)/include $(U64_CPPFLAGS)
IDO_CFLAGS = $(IDO_ARCH) -non_shared -Wab,-r4300_mul -signed -Xcpluscomm -G 0 $(IDO_OPT) $(IDO_WARN)

IRIX_ARCH   := -mips2
IRIX_OPT    := -O3
IRIX_WARN   := -fullwarn -prototypes
IRIX_CPPFLAGS = -I$(IDO)/include -Ilibultra/include -D_ULTRA64
IRIX_CFLAGS = $(IRIX_ARCH) -non_shared -G 0 $(IRIX_OPT) $(IRIX_WARN)
IRIX_ASFLAGS = -D__ASSEMBLER__ $(IRIX_ARCH) -non_shared -O2

ROMHEADER   := libultra/src/PR/romheader
BOOT        := $(BUILD)/libultra/src/PR/Boot
FONT        := libultra/src/PR/font

TOOLS := \
	tools/fixobj \
	tools/makerom \
	tools/nrdc \
	tools/sbc \
	tools/slienc \
	tools/symext \
	tools/texture

.PHONY: default
default: $(BUILD)/app.z64

.PHONY: dist
dist: $(BUILD)/app.bps

.PHONY: clean
clean:
	rm -f -r build

include dep.mk

.PHONY: clobber
clobber: clean
	rm -f -r build $(TOOLS) tools/__pycache__ tools/*.pyc $(DEP)

$(BUILD)/data/%.o: data/%.bin

$(BUILD)/data/gfx.elf:          ADDRESS := 0x02000000
$(BUILD)/shape/global/%.elf:    ADDRESS := 0x03000000
$(BUILD)/shape/player/%.elf:    ADDRESS := 0x04000000
$(BUILD)/shape/1%.elf:          ADDRESS := 0x05000000
$(BUILD)/shape/2%.elf:          ADDRESS := 0x06000000
$(BUILD)/stage/%.elf:           ADDRESS := 0x07000000
$(BUILD)/shape/3%.elf:          ADDRESS := 0x08000000
$(BUILD)/data/texture/%.elf:    ADDRESS := 0x09000000
$(BUILD)/data/back/%.elf:       ADDRESS := 0x0A000000
$(BUILD)/data/weather/%.elf:    ADDRESS := 0x0B000000

$(BUILD)/app.bps: $(BUILD)/app.z64
	flips $(DONOR)/UNSM$(REGION)0$(VERSION).z64 $< $@

$(BUILD)/app.z64: $(BUILD)/app.elf $(ROMHEADER) $(BOOT) $(FONT) tools/makerom tools/nrdc
	tools/makerom -r $@ -h $(ROMHEADER) -b $(BOOT) -F $(FONT) -s 64 -f 0xff $<
	tools/nrdc -b -t "$(TITLE)" -i NSM$(REGION) -v $(VERSION) $@

$(BUILD)/app.elf: $(BUILD)/app.ld $(OBJ) $(MENU_OBJ) $(DATA) $(SZP) $(OBJECT_DATA) $(SHAPE_SZP) $(SHAPE_DATA) $(BACK_SZP) $(TEXTURE_SZP) $(STAGE_SZP) $(STAGE_DATA) $(AUDIO_DATA)
	$(U64_LD) -Map $(@:.elf=.map) -T$(BUILD)/app.ld -o $@

$(BUILD)/app.ld: spec tools/spec
	@mkdir -p $(dir $@)
	BUILD=$(BUILD) tools/spec $(U64_CPPFLAGS) -DNEWSPEC -o $@ $<

$(BUILD)/code.o: $(CODE_OBJ) $(AUDIO_OBJ) $(BUILD)/libultra/libultra.a
	$(U64_LD) --whole-archive -L$(BUILD)/libultra -Trel.ld -r -o $@ $(CODE_OBJ) $(AUDIO_OBJ) -lultra

$(BUILD)/ulib.o: $(ULIB_OBJ)
	$(U64_LD) -Trel.ld -r -o $@ $(ULIB_OBJ)

$(BUILD)/face.o: $(FACE_OBJ)
	$(U64_LD) -Trel.ld -r -o $@ $(FACE_OBJ)

$(BUILD)/%.szp.s: %.bin tools/slienc
	@mkdir -p $(dir $@)
	tools/slienc $< $(@:.szp.s=.szp) > $@

$(BUILD)/%.szp.h: $(BUILD)/%.elf tools/symext
	tools/symext $< > $@

$(BUILD)/%.szp.s: $(BUILD)/%.elf tools/slienc
	tools/slienc $< $(@:.szp.s=.szp) > $@

$(BUILD)/%.elf: $(BUILD)/%.o
	$(U64_LD) -Tdata $(ADDRESS) -Telf.ld -o $@ $<

$(BUILD)/%.o: %.asm
	@mkdir -p $(dir $@)
	armips -strequ BUILD $(BUILD) -sym $(@:.o=.sym) $<
	$(U64_CC) -I$(BUILD) $(U64_ASFLAGS) -c -o $@ $(<:.asm=.s)

$(BUILD)/%.o: %.s
	@mkdir -p $(dir $@)
	$(U64_CC) -Iinclude $(U64_ASFLAGS) -c -o $@ $<

$(BUILD)/%.o: %.sx
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_CPPFLAGS) $(U64_ASFLAGS) -MMD -MP -c -o $@ $<

$(BUILD)/%.o: %.c
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_CPPFLAGS) $(U64_CFLAGS) -MMD -MP -c -o $@ $<

$(IDO_C): $(BUILD)/%.o: %.c
	@mkdir -p $(dir $@)
	$(IDO_CC) $(IDO_CPPFLAGS) $(IDO_CFLAGS) -c -o $@ $<

$(BUILD)/%.o: $(BUILD)/%.s
	$(U64_CC) $(U64_ASFLAGS) -c -o $@ $<

$(BUILD)/audio/ctl.s $(BUILD)/audio/tbl.s&: $(INS) tools/ic
	@mkdir -p $(dir $@)
	tools/ic $(U64_CPPFLAGS) -ctl $(BUILD)/audio/ctl.s -tbl $(BUILD)/audio/tbl.s $(INS)

$(BUILD)/audio/seq.s: $(SEQ) tools/sbc
	@mkdir -p $(dir $@)
	tools/sbc 3 $(@:.s=.bin) $(SEQ) > $@

$(BUILD)/audio/bnk.s: audio/bnk.txt
	@mkdir -p $(dir $@)
	tools/audiobnk $< > $@

$(BUILD)/%.seq: %.asm
	@mkdir -p $(dir $@)
	armips -strequ BUILD $(BUILD) -sym $(@:.seq=.sym) $<

%.h: %.png tools/texture
	tools/texture $(filter %.png,$^) > $@

%.h: %.txt tools/message
	tools/message $< > $@

%.h: %.obj tools/obj
	tools/obj $< $@

%.aifc: %.aiff
	tabledesign -s 1 $< > $(@:.aifc=.table)
	vadpcm_enc -c $(@:.aifc=.table) $< $@

$(BUILD)/libultra/src/PR/gspFast3D.fifo.o: $(wildcard libultra/src/PR/gspFast3D/*)

$(BUILD)/libultra/libultra.a: $(LIBULTRA_OBJ)
	$(U64_AR) rc $@ $(LIBULTRA_OBJ)

$(BUILD)/libultra/src/PR/Boot: $(BUILD)/libultra/src/PR/Boot.elf
	$(U64_OBJCOPY) -O binary $< $@

$(BUILD)/libultra/src/PR/Boot.elf: $(BUILD)/libultra/src/PR/Boot.o
	$(U64_LD) -Tlibultra/src/PR/Boot.ld -o $@ $<

$(BUILD)/libultra/%.o: libultra/%.asm
	@mkdir -p $(dir $@)
	armips -strequ BUILD $(BUILD) -sym $(@:.o=.sym) $<
	$(U64_CC) -I$(BUILD) $(U64_ASFLAGS) -c -o $@ $(<:.asm=.s)

$(BUILD)/libultra/%.o: libultra/%.s
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_ASFLAGS) -c -o $@ $<

$(BUILD)/libultra/%.o: libultra/%.sx
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_CPPFLAGS) $(U64_ASFLAGS) -c -o $@ $<

$(BUILD)/libultra/%.o: libultra/%.c
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_CPPFLAGS) $(U64_CFLAGS) -c -o $@ $<

$(IRIX_S): $(BUILD)/libultra/%.o: libultra/%.s tools/fixobj
	@mkdir -p $(dir $@)
	$(IRIX_CC) $(IRIX_CPPFLAGS) $(IRIX_ASFLAGS) -c -o $@ $<
	tools/fixobj $@

$(IRIX_C): $(BUILD)/libultra/%.o: libultra/%.c
	@mkdir -p $(dir $@)
	$(IRIX_CC) $(IRIX_CPPFLAGS) $(IRIX_CFLAGS) -c -o $@ $<

$(TOOLS):
tools/%: tools/%.c
	$(CC) $(CFLAGS) -s -o $@ $<

print-%:
	$(info $* = $(flavor $*): [$($*)]) @true

$(SZP:.szp.o=.o):
$(SHAPE_SZP:.szp.o=.o):
$(BACK_SZP:.szp.o=.o):
$(TEXTURE_SZP:.szp.o=.o):
$(STAGE_SZP:.szp.o=.o):

-include $(CODE_OBJ:.o=.d)
-include $(ULIB_OBJ:.o=.d)
-include $(MENU_OBJ:.o=.d)
-include $(AUDIO_OBJ:.o=.d)
-include $(FACE_OBJ:.o=.d)

-include $(DATA:.o=.d)
-include $(SZP:.szp.o=.d)
-include $(OBJECT_DATA:.o=.d)
-include $(SHAPE_SZP:.szp.o=.d)
-include $(SHAPE_DATA:.o=.d)
-include $(BACK_SZP:.szp.o=.d)
-include $(TEXTURE_SZP:.szp.o=.d)
-include $(STAGE_SZP:.szp.o=.d)
-include $(STAGE_DATA:.o=.d)
-include $(AUDIO_DATA:.o=.d)
