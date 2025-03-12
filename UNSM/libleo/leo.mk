LEO_CPPFLAGS = -I$(LIBULTRA)/include -Ilibultra/src/include -D_ULTRA64 -DNDEBUG
LEO_CFLAGS = -mips2 -non_shared -Wab,-r4300_mul -G 0 -g -fullwarn -prototypes
LEO_ASFLAGS = -mips2 -non_shared -G 0 -g

LEO_OBJ := \
	leofunc.o \
	leoram.o \
	leocmdex.o \
	leoint.o \
	leo_tbl.o \
	leoreset.o \
	leoinquiry.o \
	leotestunit.o \
	leorezero.o \
	leoread.o \
	leowrite.o \
	leoseek.o \
	leomotor.o \
	leord_capa.o \
	leotranslat.o \
	leomode_sel.o \
	leord_diskid.o \
	leomecha.o \
	leotempbuffer.o \
	leoc2_syndrome.o \
	leoc2ecc.o \
	leoutil.o \
	leomseq_tbl.o

LIBLEO_OBJ := $(addprefix $(BUILD)/libleo/,$(LEO_OBJ))

$(BUILD)/lib/libleo.a: $(LIBLEO_OBJ)
	@mkdir -p $(dir $@)
	$(U64_AR) rc $@ $(LIBLEO_OBJ)

$(BUILD)/libleo/%.o: libleo/src/%.c
	@mkdir -p $(dir $@)
	$(IDO_CC) -I$(IDO)/include $(LEO_CPPFLAGS) $(LEO_CFLAGS) -c -o $@ $<

$(BUILD)/libleo/%.o: libleo/src/%.s tools/fixsym
	@mkdir -p $(dir $@)
	$(IRIX_CC) -I$(IDO)/include $(LEO_CPPFLAGS) $(LEO_ASFLAGS) -c -o $@ $<
	tools/fixsym $@
