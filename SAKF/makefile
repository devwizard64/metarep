VERSION ?= J0
BUILD   := build/$(VERSION)

CC65    := $(HOME)/sm64/cc65-2.19
AS      := $(CC65)/bin/ca65
LD      := $(CC65)/bin/ld65

FLAG    := -D _$(VERSION) -I $(BUILD) -I include
AS      += --cpu 65816 --feature c_comments -U -s $(FLAG)

CRC     := build/exe/crc
EXE     := $(CRC)

OBJ := \
	$(BUILD)/src/code.o     \
	$(BUILD)/src/header.o   \
	$(BUILD)/src/code_01.o  \
	$(BUILD)/src/bank.o

BUILD_DIR   := $(sort $(dir $(OBJ)))

$(BUILD)/app.sfc: make/main.ld $(OBJ) $(CRC)
	$(LD) -m $(@:.sfc=.map) -o $@ -C $< $(OBJ)
	$(CRC) $@

$(BUILD)/%.o: %.s | $(BUILD_DIR)
	$(AS) -o $@ $<

build/exe/%: CC := cc -Wall -Wextra -Wpedantic -O2
build/exe/%: exe/%.c | build/exe
	$(CC) -MMD -MP -MF $@.d -o $@ $< $(LIB)

build/exe $(BUILD_DIR):
	mkdir -p $@

clean:
	rm -rf build

-include $(addsuffix .d,$(EXE))
-include $(OBJ:.o=.d)
.PHONY: clean
