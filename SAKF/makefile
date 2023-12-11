TARGET ?= J0

BUILD := build/$(TARGET)

CC      := gcc
CFLAGS  := -O2 -Wall -Wextra -Wpedantic

SFC_AS  := ca65
SFC_LD  := ld65
SFC_CPPFLAGS := -Iinclude -I$(BUILD) -DTARGET_$(TARGET)
SFC_ASFLAGS := --cpu 65816 --feature c_comments -U -s

ifeq ($(TARGET),J0)
	SFC_CPPFLAGS += -DDESTCODE=0 -DVERSION=0 -DREGION=74
endif
ifeq ($(TARGET),J1)
	SFC_CPPFLAGS += -DDESTCODE=0 -DVERSION=1 -DREGION=74
endif
ifeq ($(TARGET),J2)
	SFC_CPPFLAGS += -DDESTCODE=0 -DVERSION=2 -DREGION=74
endif
ifeq ($(TARGET),E0)
	SFC_CPPFLAGS += -DDESTCODE=1 -DVERSION=0 -DREGION=69
endif
ifeq ($(TARGET),P0)
	SFC_CPPFLAGS += -DDESTCODE=2 -DVERSION=0 -DREGION=80
endif

OBJ := \
	$(BUILD)/src/header.o \
	$(BUILD)/src/code.o \
	$(BUILD)/src/code_01.o \
	$(BUILD)/src/bank.o

TOOLS := tools/checksum

.PHONY: default
default: $(BUILD)/app.sfc

.PHONY: clean
clean:
	rm -f -r build

.PHONY: clobber
clobber:
	rm -f -r build $(TOOLS)

$(BUILD)/app.sfc: main.ld $(OBJ) tools/checksum
	@mkdir -p $(dir $@)
	$(SFC_LD) -m $(@:.sfc=.map) -o $@ -C main.ld $(OBJ)
	tools/checksum $@

-include $(OBJ:.o=.d)

$(BUILD)/%.o: %.s
	@mkdir -p $(dir $@)
	$(SFC_AS) $(SFC_CPPFLAGS) $(SFC_ASFLAGS) -o $@ $<

$(TOOLS):
tools/%: tools/%.c
	$(CC) $(CFLAGS) -s -o $@ $<
