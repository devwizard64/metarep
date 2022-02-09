VERSION ?= J0
BUILD   := build/$(VERSION)

OBJ := \
	$(BUILD)/src/code.o     \
	$(BUILD)/src/header.o   \
	$(BUILD)/src/code_01.o  \
	$(BUILD)/src/bank.o

TOOLS   := tools
RES != make -C $(TOOLS)

AS      := ca65
LD      := ld65
FLAG    := -Iinclude -I$(BUILD) -D__$(VERSION)__
ASFLAG  := --cpu 65816 --feature c_comments -U -s $(FLAG)

.PHONY: default
default: $(BUILD)/app.sfc

.PHONY: clean
clean:
	rm -f -r build

$(BUILD)/%.sfc: make/main.ld $(OBJ)
	$(LD) -m $(@:.sfc=.map) -o $@ -C $^
	$(TOOLS)/mask $@

-include $(OBJ:.o=.d)

$(BUILD)/%.o: %.s | $(BUILD_DIR)
	$(AS) $(ASFLAG) -o $@ $<

dirs = $(foreach d,$(wildcard $1*),$(call dirs,$d/,$2) $(filter $(subst *,%,$2),$d))
obj = $(call dirs,src/,$1)
BUILD_OBJ := $(call obj,*.s)
$(foreach f,$(BUILD_OBJ),$(eval $f: | $(addprefix $(BUILD)/,$(dir $f))))
$(sort $(addprefix $(BUILD)/,$(dir $(BUILD_OBJ)))):
	mkdir -p $@
