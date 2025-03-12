TARGET ?= E0

BUILD := build/$(TARGET)

CC := gcc
CPPFLAGS = -Iinclude
CFLAGS = -O2 -Wall -Wextra -Wpedantic
LDFLAGS = -s

U64_PREFIX  := mips-linux-gnu-
U64_CC      := $(U64_PREFIX)gcc
U64_CPP     := $(U64_PREFIX)cpp
U64_LD      := $(U64_PREFIX)ld
U64_AR      := $(U64_PREFIX)ar
U64_OBJCOPY := $(U64_PREFIX)objcopy

U64_ARCH := -mabi=32 -march=vr4300 -mfix4300
U64_OPT := -Os
U64_CPPFLAGS = -I$(LIBULTRA)/include -Iinclude -I. -I$(BUILD) -D_ULTRA64 -DREVISION=$(REVISION) -DNA_REVISION=$(NA_REVISION)
U64_CFLAGS = $(U64_ARCH) -mno-abicalls -fno-PIC -mno-check-zero-division -fno-builtin -ffast-math -ftrapping-math -fno-associative-math -fsingle-precision-constant -G 0 $(U64_OPT) -Wall -Wextra -Werror=implicit-function-declaration
U64_ASFLAGS = $(U64_ARCH) -mno-abicalls -fno-PIC -G 0 $(U64_OPT)
U64_ARMIPSFLAGS = -strequ BUILD $(BUILD)

IDO_CC := $(IDO)/bin/cc
IDO_ARCH := -mips2
IDO_OPT := -O2
IDO_CFLAGS = $(IDO_ARCH) -non_shared -Wab,-r4300_mul -signed -Xcpluscomm -G 0 $(IDO_OPT) -fullwarn -prototypes
IDO_ASFLAGS = $(IDO_ARCH) -non_shared -Wab,-r4300_mul -Xcpluscomm -G 0 $(IDO_OPT)

APP := app

ifeq ($(TARGET),P0)
	U64_CPPFLAGS += -DPAL
else
	U64_CPPFLAGS += -DNTSC
endif

ifeq ($(TARGET),J0)
	ICODE := NSMJ
	VERSION := 0
	REVISION := 199606
	NA_VERSION := 1
	NA_REVISION := 100
	LIBULTRA_VERSION := D
	LIBULTRA_REVISION := 199606
	U64_CPPFLAGS += -DJAPANESE
endif
ifeq ($(TARGET),E0)
	ICODE := NSME
	VERSION := 0
	REVISION := 199609
	NA_VERSION := 1
	NA_REVISION := 101
	LIBULTRA_VERSION := D
	LIBULTRA_REVISION := 199609
	U64_CPPFLAGS += -DENGLISH
endif
ifeq ($(TARGET),G0)
	ICODE := NSMG
	VERSION := 0
	REVISION := 199610
	NA_VERSION := 1
	NA_REVISION := 101
	LIBULTRA_VERSION := D
	LIBULTRA_REVISION := 199610
	U64_CPPFLAGS += -DENGLISH
	GATEWAY ?= 1
endif
ifeq ($(TARGET),DD)
	ICODE := DSMJ
	VERSION := 0
	REVISION := 199605
	NA_VERSION := 2
	NA_REVISION := 200
	LIBULTRA_VERSION := F
	LIBULTRA_REVISION := 199611
	U64_CPPFLAGS += -DJAPANESE
	DISK ?= 1
endif
ifeq ($(TARGET),P0)
	ICODE := NSMP
	VERSION := 0
	REVISION := 199703
	NA_VERSION := 2
	NA_REVISION := 201
	LIBULTRA_VERSION := F
	LIBULTRA_REVISION := 199703
	U64_CPPFLAGS += -DMULTILANG
endif
ifeq ($(TARGET),J3)
	ICODE := NSMJ
	VERSION := 3
	REVISION := 199707
	NA_VERSION := 2
	NA_REVISION := 300
	LIBULTRA_VERSION := H
	LIBULTRA_REVISION := 199707
	U64_CPPFLAGS += -DJAPANESE
	MOTOR ?= 1
endif
ifeq ($(TARGET),C3)
	ICODE := NSMC
	VERSION := 3
	REVISION := 200311
	NA_VERSION := 2
	NA_REVISION := 300
	LIBULTRA_VERSION := L
	LIBULTRA_REVISION := 200311
	U64_CPPFLAGS += -DCHINESE -DDEBUG
	MOTOR ?= 1
endif

ifneq ($(GATEWAY),)
	U64_CPPFLAGS += -DGATEWAY
endif
ifneq ($(DISK),)
	U64_CPPFLAGS += -DDISK
endif
ifneq ($(MOTOR),)
	U64_CPPFLAGS += -DMOTOR
endif

ifeq ($(TARGET),DD)
	OUTPUT := $(BUILD)/$(APP).ndd
else
	OUTPUT := $(BUILD)/$(APP).z64
endif

ifeq ($(VERSION),0)
	TITLE := SUPER MARIO 64
else
	TITLE := SUPERMARIO64
endif

ifneq ($(filter J0 E0,$(TARGET)),)
	IDO_OPT := -g
endif

AUDIO       := audio/v$(NA_VERSION)
LIBULTRA    := libultra/2.0$(LIBULTRA_VERSION)
ROMHEADER   := $(LIBULTRA)/lib/PR/romheader
BOOT        := $(BUILD)/lib/PR/Boot
FONT        := libultra/lib/PR/font
ifeq ($(LIBULTRA_VERSION),L)
	LIBULTRA := libultra/2.0H
endif

TOOLS := $(patsubst %.c,%,$(wildcard tools/*.c))

.PHONY: default
default: $(OUTPUT)

.PHONY: dist
dist: $(BUILD)/$(APP).bps

include dep.mk

.PHONY: dep
dep: $(DEP)

.PHONY: clean
clean:
	rm -f -r build

.PHONY: clobber
clobber: clean
	rm -f -r build $(TOOLS) $(DEP)

$(BUILD)/src/face/%.o: IDO_CFLAGS = -non_shared -Wab,-r4300_mul -signed -Xcpluscomm -G 0 -fullwarn -prototypes -g
$(BUILD)/src/%.data.o $(BUILD)/src/audio/$(NA_REVISION)/data.o $(BUILD)/src/audio/work.o $(BUILD)/data/%.o $(BUILD)/shape/%.o $(BUILD)/stage/%.o: U64_CFLAGS = $(U64_ARCH) -mno-abicalls -fno-PIC -fno-common -fno-zero-initialized-in-bss -fno-toplevel-reorder -G 0 -Wall -Wextra

$(BUILD)/data/gfx.elf:          ADDRESS := 0x02000000
$(BUILD)/shape/global/%.elf:    ADDRESS := 0x03000000
$(BUILD)/shape/player/%.elf:    ADDRESS := 0x04000000
$(BUILD)/shape/1%.elf:          ADDRESS := 0x05000000
$(BUILD)/shape/2%.elf:          ADDRESS := 0x06000000
$(BUILD)/stage/%.elf:           ADDRESS := 0x07000000
$(BUILD)/shape/3%.elf:          ADDRESS := 0x08000000
$(BUILD)/data/texture/%.elf:    ADDRESS := 0x09000000
$(BUILD)/data/background/%.elf: ADDRESS := 0x0A000000
$(BUILD)/data/weather/%.elf:    ADDRESS := 0x0B000000

$(BUILD)/$(APP).bps: $(OUTPUT)
	flips $(DONOR)/U$(ICODE)0$(VERSION)$(suffix $<) $< $@

ifeq ($(TARGET),C3)
$(BUILD)/$(APP).z64: $(BUILD)/$(APP).elf $(ROMHEADER) $(BOOT) $(FONT) tools/makerom
	tools/makerom -r $@ -h $(ROMHEADER) -b $(BOOT) -F $(FONT) -a 14 $<
else
$(BUILD)/$(APP).z64: $(BUILD)/$(APP).elf $(ROMHEADER) $(BOOT) $(FONT) tools/makerom tools/nrdc
	tools/makerom -r $@ -h $(ROMHEADER) -b $(BOOT) -F $(FONT) -s 64 -f 0xff $<
	tools/nrdc -b -t "$(TITLE)" -i $(ICODE) -v $(VERSION) $@
endif

$(BUILD)/$(APP).ndd: $(BUILD)/$(APP).elf tools/makedisk
	tools/makedisk -R $@ $<

$(BUILD)/$(APP).elf: $(BUILD)/$(APP).ld $(OBJ) $(MENU_OBJ) $(DATA) $(SZP) $(AUDIO_DATA)
	$(U64_LD) -N -Map $(@:.elf=.map) -T$(BUILD)/$(APP).ld -o $@

$(BUILD)/$(APP).ld: spec tools/spec
	@mkdir -p $(dir $@)
	$(U64_CPP) $(U64_CPPFLAGS) -DNEWSPEC $< | BUILD=$(BUILD) tools/spec > $@

ifeq ($(TARGET),DD)
$(BUILD)/code.o: $(CODE_OBJ) $(AUDIO_OBJ) $(BUILD)/lib/libultra_d.a $(BUILD)/lib/libleo.a
	$(U64_LD) --whole-archive -L$(BUILD)/lib -Trel.ld -r -o $@ $(CODE_OBJ) $(AUDIO_OBJ) -lleo -lultra_d
else
$(BUILD)/code.o: $(CODE_OBJ) $(AUDIO_OBJ) $(BUILD)/lib/libultra_rom.a
	$(U64_LD) --whole-archive -L$(BUILD)/lib -Trel.ld -r -o $@ $(CODE_OBJ) $(AUDIO_OBJ) -lultra_rom
endif

$(BUILD)/ulib.o: $(ULIB_OBJ)
	$(U64_LD) -Trel.ld -r -o $@ $(ULIB_OBJ)

$(BUILD)/face.o: $(FACE_OBJ)
	$(U64_LD) -Trel.ld -r -o $@ $(FACE_OBJ)

$(BUILD)/facedata.o: $(FACEDATA_OBJ)
	$(U64_LD) -Trel.ld -r -o $@ $(FACEDATA_OBJ)

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
	armips $(U64_ARMIPSFLAGS) -sym $(@:.o=.sym) $<
	$(U64_CC) -I$(BUILD) $(U64_ASFLAGS) -c -o $@ $(<:.asm=.s)

$(BUILD)/%.o: %.c
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_CPPFLAGS) $(U64_CFLAGS) -MMD -MP -c -o $@ $<

$(BUILD)/%.o: %.s
	@mkdir -p $(dir $@)
	$(U64_CC) -Iinclude $(U64_ASFLAGS) -c -o $@ $<

$(BUILD)/%.o: %.sx
	@mkdir -p $(dir $@)
	$(U64_CC) $(U64_CPPFLAGS) $(U64_ASFLAGS) -MMD -MP -c -o $@ $<

$(IDO_C): $(BUILD)/%.o: %.c
	@mkdir -p $(dir $@)
	@rm -f $@ $(@:.o=.d)
	$(IDO_CC) -I$(IDO)/include $(U64_CPPFLAGS) $(IDO_CFLAGS) -MDupdate $(@:.o=.d) -c -o $@ $<

$(IDO_S): $(BUILD)/%.o: %.s tools/fixsym
	@mkdir -p $(dir $@)
	@rm -f $@ $(@:.o=.d)
	$(IRIX_CC) -I$(IDO)/include $(U64_CPPFLAGS) $(IDO_ASFLAGS) -MDupdate $(@:.o=.d) -c -o $@ $<
	tools/fixsym $@

$(BUILD)/%.o: $(BUILD)/%.s
	$(U64_CC) $(U64_ASFLAGS) -c -o $@ $<

$(BUILD)/audio/ctl.s: $(BUILD)/audio/inst tools/sbc
	@mkdir -p $(dir $@)
	tools/sbc -c 1 -a 64 -o $(@:.s=.sbk) $(shell grep ctl$$ $<) > $@

$(BUILD)/audio/tbl.s: $(BUILD)/audio/inst tools/sbc
	@mkdir -p $(dir $@)
	tools/sbc -c 2 -a 64 -o $(@:.s=.sbk) $(shell grep tbl$$ $<) > $@

$(BUILD)/audio/seq.s: $(AUDIO_SEQ) tools/sbc
	@mkdir -p $(dir $@)
	tools/sbc -c 3 -o $(@:.s=.sbk) $(AUDIO_SEQ) > $@

$(BUILD)/audio/bnk.s: audio/$(TARGET)/bnk.txt tools/audiobnk
	@mkdir -p $(dir $@)
	tools/audiobnk $< > $@

$(BUILD)/audio/inst: audio/$(TARGET)/inst.ins tools/ic
	@mkdir -p $(dir $@)
	$(U64_CPP) $(U64_CPPFLAGS) $< | tools/ic $(dir $@) > $@

$(BUILD)/%.seq: %.asm
	@mkdir -p $(dir $@)
	armips $(U64_ARMIPSFLAGS) -sym $(@:.seq=.sym) $<

%.h: %.png tools/texture
	tools/texture $(filter %.png,$^) > $@

%.h: %.txt tools/message
	tools/message $< > $@

%.h: %.obj tools/obj
	tools/obj $< $@

%.aifc: %.aiff
	tabledesign -s 1 $< > $(@:.aifc=.table)
	vadpcm_enc -c $(@:.aifc=.table) $< $@

$(TOOLS):
tools/%: tools/%.c
	$(CC) $(LDFLAGS) $(CPPFLAGS) $(CFLAGS) -o $@ $<

print-%:
	$(info $* = $(flavor $*): [$($*)]) @true

$(SZP:.szp.o=.o):

-include $(CODE_OBJ:.o=.d)
-include $(ULIB_OBJ:.o=.d)
-include $(MENU_OBJ:.o=.d)
-include $(AUDIO_OBJ:.o=.d)
-include $(FACE_OBJ:.o=.d)

-include $(DATA:.o=.d)
-include $(SZP:.szp.o=.d)
-include $(AUDIO_DATA:.o=.d)

include libultra/ultra.mk
include libleo/leo.mk
