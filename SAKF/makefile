VERSION ?= J00

BUILD   := build/$(VERSION)

OBJ := \
	$(BUILD)/src/code.o     \
	$(BUILD)/src/header.o   \
	$(BUILD)/src/code_01.o  \
	$(BUILD)/src/bank.o

TOOLS_OBJ := tools/mask

$(eval REVISION := $$$(VERSION))
REGION  := $(subst $(REVISION),,$(VERSION))
REGION  := $(subst J,0,$(REGION))
REGION  := $(subst E,1,$(REGION))
REGION  := $(subst P,2,$(REGION))

FLAG    := -Iinclude -I$(BUILD)
FLAG    += -DVERSION_$(VERSION) -DREGION=$(REGION) -DREVISION=$(REVISION)

CC      := gcc
CCFLAG  := -O2 -Wall -Wextra -Wpedantic

SFC_AS      := ca65
SFC_LD      := ld65
SFC_ASFLAG  := --cpu 65816 --feature c_comments -U -s $(FLAG)

.PHONY: default
default: $(BUILD)/app.sfc

.PHONY: clean
clean:
	rm -f -r build $(TOOLS_OBJ)

$(BUILD)/app.sfc: main.ld $(OBJ) tools/mask
	@mkdir -p $(dir $@)
	$(SFC_LD) -m $(@:.sfc=.map) -o $@ -C main.ld $(OBJ)
	tools/mask $@

-include $(OBJ:.o=.d)

$(BUILD)/%.o: %.s
	@mkdir -p $(dir $@)
	$(SFC_AS) $(SFC_ASFLAG) -o $@ $<

$(TOOLS_OBJ):
tools/%: tools/%.c
	$(CC) $(CCFLAG) -s -o $@ $<
