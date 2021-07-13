VERSION ?= J0
BUILD   := build/$(VERSION)

CC65    := $(HOME)/sm64/cc65-2.19
AS      := $(CC65)/bin/ca65
LD      := $(CC65)/bin/ld65

FLAG    := -D __$(VERSION)__ -I $(BUILD) -I include
AS      += --cpu 65816 --feature c_comments -U -s $(FLAG)

EXE     := exe

OBJ != make -C $(EXE)

OBJ := \
	$(BUILD)/src/code.o     \
	$(BUILD)/src/header.o   \
	$(BUILD)/src/code_01.o  \
	$(BUILD)/src/bank.o

$(BUILD)/app.sfc: make/main.ld $(OBJ)
	$(LD) -m $(@:.sfc=.map) -o $@ -C $^
	$(EXE)/crc $@

-include $(OBJ:.o=.d)

$(BUILD)/%.o: %.s | $(BUILD_DIR)
	$(AS) -o $@ $<

dirs = $(foreach d,$(wildcard $1*),$(call dirs,$d/,$2) \
	$(filter $(subst *,%,$2),$d))
obj = $(call dirs,src/,$1)
BUILD_OBJ := $(call obj,*.s)
$(foreach f,$(BUILD_OBJ),$(eval $f: | $(addprefix $(BUILD)/,$(dir $f))))
$(sort $(addprefix $(BUILD)/,$(dir $(BUILD_OBJ)))):
	mkdir -p $@

.PHONY: clean
clean:
	rm -rf build
