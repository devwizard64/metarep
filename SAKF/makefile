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

AS      := ca65
LD      := ld65
FLAG    := -Iinclude -I$(BUILD)
FLAG    += -DVERSION_$(VERSION) -DREGION=$(REGION) -DREVISION=$(REVISION)
ASFLAG  := --cpu 65816 --feature c_comments -U -s $(FLAG)

.PHONY: default
default: $(BUILD)/app.sfc

.PHONY: clean
clean:
	rm -f -r build $(TOOLS_OBJ)

$(BUILD)/%.sfc: make/main.ld $(OBJ) tools/mask
	@mkdir -p $(dir $@)
	$(LD) -m $(@:.sfc=.map) -o $@ -C make/main.ld $(OBJ)
	tools/mask $@

-include $(OBJ:.o=.d)

$(BUILD)/%.o: %.s | $(BUILD_DIR)
	@mkdir -p $(dir $@)
	$(AS) $(ASFLAG) -o $@ $<

$(TOOLS_OBJ):
tools/%: tools/%.c
	cc -O2 -Wall -Wextra -Wpedantic -s -o $@ $<
