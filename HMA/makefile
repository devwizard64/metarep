BUILD := build

CA65  := ca65
LD65  := ld65
CA65FLAGS = -Iinclude -t nes --feature c_comments -U

OBJ := \
	$(BUILD)/src/header.o \
	$(BUILD)/src/main.o \
	$(BUILD)/src/audio.o \
	$(BUILD)/src/chr.o

.PHONY: default
default: $(BUILD)/app.nes

.PHONY: clean
clean:
	rm -f -r build

$(BUILD)/app.nes: hvc.ld $(OBJ)
	@mkdir -p $(dir $@)
	$(LD65) -C hvc.ld -m $(@:.nes=.map) -o $@ $(OBJ)

$(BUILD)/%.o: %.s
	@mkdir -p $(dir $@)
	$(CA65) $(CA65FLAGS) -o $@ $<

-include $(OBJ:.o=.d)
