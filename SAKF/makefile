TARGET  ?= J00

BUILD   := build/$(TARGET)
$(eval VERSION := $$$(TARGET))
REGION  := $(subst $(VERSION),,$(TARGET))
REGION  := $(subst J,0,$(REGION))
REGION  := $(subst E,1,$(REGION))
REGION  := $(subst P,2,$(REGION))

OBJ := \
	$(BUILD)/src/code.o     \
	$(BUILD)/src/header.o   \
	$(BUILD)/src/code_01.o  \
	$(BUILD)/src/bank.o

TOOLS := tools/checksum

CC      := gcc
CFLAGS  := -O2 -Wall -Wextra -Wpedantic

FLAGS   := -Iinclude -I$(BUILD)
FLAGS   += -DTARGET_$(TARGET) -DREGION=$(REGION) -DVERSION=$(VERSION)

SFC_AS      := ca65
SFC_LD      := ld65
SFC_ASFLAGS := --cpu 65816 --feature c_comments -U -s $(FLAGS)

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
	$(SFC_AS) $(SFC_ASFLAGS) -o $@ $<

$(TOOLS):
tools/%: tools/%.c
	$(CC) $(CFLAGS) -s -o $@ $<
