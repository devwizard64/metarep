ULTRA_ARCH := -mips2
ULTRA_COPT :=
ULTRA_ASOPT :=
ULTRA_CPPFLAGS = -I$(CURDIR)/$(LIBULTRA)/include -I. -D_ULTRA64 -DREVISION=$(LIBULTRA_REVISION)
ULTRA_CFLAGS = $(ULTRA_ARCH) -non_shared -Wab,-r4300_mul -G 0 $(ULTRA_COPT) -fullwarn -prototypes
ULTRA_ASFLAGS = $(ULTRA_ARCH) -non_shared -G 0 $(ULTRA_ASOPT)
ULTRA_ARMIPSFLAGS = -equ REVISION $(LIBULTRA_REVISION)
ifeq ($(filter $(LIBULTRA_VERSION),D F),)
	ULTRA_CPPFLAGS += -DF3DEX_GBI
endif

ifneq ($(filter J0 E0 G0,$(TARGET)),)
	ULTRA_OBJ :=
	ifeq ($(TARGET),E0)
		ULTRA_OBJ += os/parameters.o
	endif
	ULTRA_OBJ += \
		io/vitbl.o \
		os/settime.o \
		os/maptlb.o \
		os/unmaptlball.o \
		rmon/sprintf.o \
		os/createmesgqueue.o \
		os/seteventmesg.o \
		io/visetevent.o \
		os/createthread.o \
		os/recvmesg.o \
		io/sptask.o \
		io/sptaskyield.o \
		os/sendmesg.o \
		io/sptaskyielded.o \
		os/startthread.o \
		os/writebackdcacheall.o
	ifeq ($(TARGET),G0)
		ULTRA_OBJ += os/parameters.o
	endif
	ULTRA_OBJ += \
		io/vimgr.o \
		io/visetmode.o \
		io/viblack.o \
		io/visetspecial.o \
		io/pimgr.o \
		os/setthreadpri.o \
		os/initialize.o
	ifeq ($(TARGET),G0)
		ULTRA_OBJ += io/piacs.o io/contreaddata.o
	endif
	ULTRA_OBJ += io/viswapbuf.o gu/sqrtf.o
	ifneq ($(TARGET),G0)
		ULTRA_OBJ += io/contreaddata.o
	endif
	ULTRA_OBJ += \
		io/controller.o \
		io/conteepprobe.o \
		libc/ll.o \
		os/invaldcache.o \
		io/pidma.o \
		libc/bzero.o \
		os/invalicache.o \
		io/conteeplongread.o \
		io/conteeplongwrite.o \
		libc/bcopy.o \
		gu/ortho.o \
		gu/perspective.o \
		os/gettime.o \
		libc/llcvt.o \
		gu/cosf.o \
		gu/sinf.o \
		gu/translate.o \
		gu/rotate.o \
		gu/scale.o \
		io/aisetfreq.o \
		audio/bnkf.o \
		os/writebackdcache.o \
		io/aigetlen.o \
		io/aisetnextbuf.o \
		os/timerintr.o \
		rmon/xprintf.o \
		libc/string.o \
		os/thread.o \
		os/interrupt.o \
		io/vi.o \
		os/exceptasm.o \
		gu/libm_vals.o \
		os/virtualtophysical.o \
		io/spsetstat.o \
		io/spsetpc.o \
		io/sprawdma.o \
		io/sp.o \
		io/spgetstat.o \
		os/getthreadpri.o \
		io/vigetcurrcontext.o \
		io/viswapcontext.o \
		os/getcount.o
	ifneq ($(TARGET),G0)
		ULTRA_OBJ += io/piacs.o
	endif
	ULTRA_OBJ += \
		io/pirawdma.o \
		io/devmgr.o \
		os/setsr.o \
		os/getsr.o \
		os/setfpccsr.o \
		io/sirawread.o \
		io/sirawwrite.o \
		os/maptlbrdb.o \
		io/pirawread.o
	ifeq ($(TARGET),J0)
		ULTRA_OBJ += os/parameters.o
	endif
	ULTRA_OBJ += \
		io/siacs.o \
		io/sirawdma.o \
		os/settimer.o \
		io/conteepwrite.o \
		os/jammesg.o \
		io/pigetcmdq.o \
		io/conteepread.o \
		gu/mtxutil.o \
		gu/normalize.o \
		io/ai.o \
		os/setcompare.o \
		rmon/xlitob.o \
		rmon/xldtob.o \
		vimodentsclan1.o \
		vimodepallan1.o \
		os/kdebugserver.o \
		os/syncputchars.o \
		os/setintmask.o \
		os/destroythread.o \
		os/probetlb.o \
		io/si.o \
		libc/ldiv.o \
		os/getcause.o \
		os/atomic.o
endif
ifeq ($(TARGET),DD)
	ULTRA_OBJ := \
		io/vitbl.o \
		os/settime.o \
		os/maptlb.o \
		os/unmaptlball.o \
		rmon/sprintf.o \
		os/createmesgqueue.o \
		os/seteventmesg.o \
		io/visetevent.o \
		os/createthread.o \
		os/recvmesg.o \
		io/sptask.o \
		io/sptaskyield.o \
		os/sendmesg.o \
		io/sptaskyielded.o \
		os/startthread.o \
		os/writebackdcacheall.o \
		io/vimgr.o \
		io/visetmode.o \
		io/viblack.o \
		io/visetspecial.o \
		io/pimgr.o \
		os/setthreadpri.o \
		os/initialize.o \
		io/viswapbuf.o \
		gu/sqrtf.o \
		io/contreaddata.o \
		io/controller.o \
		libc/bzero.o \
		os/invalicache.o \
		os/invaldcache.o \
		libc/bcopy.o \
		gu/ortho.o \
		gu/perspective.o \
		os/gettime.o \
		libc/ll.o \
		libc/llcvt.o \
		gu/cosf.o \
		gu/sinf.o \
		gu/translate.o \
		gu/rotate.o \
		gu/scale.o \
		io/aisetfreq.o \
		io/pidma.o \
		os/parameters.o \
		io/aigetlen.o \
		io/aisetnextbuf.o \
		os/getcount.o \
		io/leodiskinit.o \
		io/epiread.o \
		io/epiwrite.o \
		os/stopthread.o \
		os/writebackdcache.o \
		io/epidma.o \
		os/timerintr.o \
		os/errorasm.o \
		rmon/xprintf.o \
		libc/string.o \
		os/thread.o \
		os/interrupt.o \
		io/vi.o \
		os/assert.o \
		os/exceptasm.o \
		gu/libm_vals.o \
		os/virtualtophysical.o \
		io/spsetstat.o \
		io/spsetpc.o \
		io/sprawdma.o \
		io/sp.o \
		io/spgetstat.o \
		os/getthreadpri.o \
		io/vigetcurrcontext.o \
		io/viswapcontext.o \
		io/piacs.o \
		io/pirawdma.o \
		io/epirawdma.o \
		io/devmgr.o \
		os/rdbsend.o \
		os/setsr.o \
		os/getsr.o \
		os/setfpccsr.o \
		io/sirawread.o \
		io/sirawwrite.o \
		os/maptlbrdb.o \
		io/pirawread.o \
		os/sethwinterrupt.o \
		io/leointerrupt.o \
		io/siacs.o \
		io/sirawdma.o \
		os/settimer.o \
		gu/mtxutil.o \
		gu/normalize.o \
		os/jammesg.o \
		io/pigetcmdq.o \
		io/ai.o \
		io/epirawread.o \
		io/epirawwrite.o \
		os/setcompare.o \
		os/error.o \
		rmon/xlitob.o \
		rmon/xldtob.o \
		vimodentsclan1.o \
		vimodepallan1.o \
		rmon/syncprintf.o \
		os/assertbreak.o \
		os/kdebugserver.o \
		os/readhost.o \
		rmon/rmonsio.o \
		os/initrdb.o \
		os/setintmask.o \
		os/destroythread.o \
		os/probetlb.o \
		os/resetglobalintmask.o \
		os/setglobalintmask.o \
		os/yieldthread.o \
		io/si.o \
		log/log.o \
		libc/ldiv.o \
		os/getcause.o \
		rmon/rmoncmds.o \
		rmon/rmonmem.o \
		rmon/rmontask.o \
		rmon/rmonmisc.o \
		rmon/rmonregs.o \
		rmon/rmonbrk.o \
		rmon/rmonmain.o \
		io/sprawwrite.o \
		io/sprawread.o \
		os/getactivequeue.o \
		rmon/rmonrcp.o
endif

ULTRA_CO3 := \
	gu/ortho.o \
	gu/perspective.o \
	gu/cosf.o \
	gu/sinf.o \
	gu/translate.o \
	gu/rotate.o \
	gu/scale.o \
	audio/bnkf.o \
	libc/string.o \
	gu/mtxutil.o \
	gu/normalize.o \
	libc/ldiv.o
ifeq ($(filter $(TARGET),J0 E0 G0 DD),)
	# libc
	ULTRA_CO3 += \
		rmon/xprintf.o \
		rmon/sprintf.o \
		rmon/xlitob.o \
		rmon/xldtob.o
endif

ULTRA_CMIPS3 := libc/ll.o libc/llcvt.o

ULTRA_SMIPS3 := os/exceptasm.o

################################################################################
# libultra_rom

LIBULTRA_ROM_OBJ := $(addprefix $(BUILD)/libultra_rom/,$(ULTRA_OBJ))
LIBULTRA_ROM_CMIPS3 := $(addprefix $(BUILD)/libultra_rom/,$(ULTRA_CMIPS3))
LIBULTRA_ROM_CO3 := $(addprefix $(BUILD)/libultra_rom/,$(ULTRA_CO3))
LIBULTRA_ROM_SMIPS3 := $(addprefix $(BUILD)/libultra_rom/,$(ULTRA_SMIPS3))

$(BUILD)/libultra_rom/%.o: ULTRA_CPPFLAGS += -DNDEBUG -D_FINALROM
$(BUILD)/libultra_rom/libc/%.o: ULTRA_ASOPT := -O2

$(LIBULTRA_ROM_CMIPS3): ULTRA_ARCH := -32 -mips3
$(LIBULTRA_ROM_CO3): ULTRA_COPT := -O3
$(LIBULTRA_ROM_SMIPS3): ULTRA_ARCH := -32 -mips3

$(BUILD)/libultra_rom/src/gu/cosf.o: U64_CFLAGS += -fno-strict-aliasing
$(BUILD)/libultra_rom/src/gu/sinf.o: U64_CFLAGS += -fno-strict-aliasing
$(BUILD)/libultra_rom/src/os/kdebugserver.o: U64_CFLAGS += -fno-strict-aliasing
$(BUILD)/libultra_rom/src/rmon/xldtob.o: U64_CFLAGS += -fno-single-precision-constant
$(BUILD)/libultra_rom/src/rmon/xprintf.o: U64_CFLAGS += -fno-strict-aliasing

$(BUILD)/lib/libultra_rom.a: $(LIBULTRA_ROM_OBJ)
	@mkdir -p $(dir $@)
	$(U64_AR) rc $@ $(LIBULTRA_ROM_OBJ)

$(BUILD)/libultra_rom/%.o: libultra/src/%.c
	@mkdir -p $(dir $@)
	cd libultra/src/include; $(IDO_CC) -I$(IDO)/include $(ULTRA_CPPFLAGS) $(ULTRA_CFLAGS) -c -o $(CURDIR)/$@ $(<:libultra/src/%=../%)

$(LIBULTRA_ROM_CMIPS3): $(BUILD)/libultra_rom/%.o: libultra/src/%.c tools/fixabi
	@mkdir -p $(dir $@)
	cd libultra/src/include; $(IDO_CC) -I$(IDO)/include $(ULTRA_CPPFLAGS) $(ULTRA_CFLAGS) -c -o $(CURDIR)/$@ $(<:libultra/src/%=../%)
	tools/fixabi $@

$(LIBULTRA_ROM_CO3): $(BUILD)/libultra_rom/%.o: libultra/src/%.c
	@mkdir -p $(dir $@)
	cd libultra/src/include; $(IRIX_CC) -I$(IDO)/include $(ULTRA_CPPFLAGS) $(ULTRA_CFLAGS) -c -o $(CURDIR)/$@ $(<:libultra/src/%=../%)

$(BUILD)/libultra_rom/%.o: libultra/src/%.s tools/fixsym
	@mkdir -p $(dir $@)
	cd libultra/src/include; $(IRIX_CC) -I$(IDO)/include $(ULTRA_CPPFLAGS) $(ULTRA_ASFLAGS) -c -o $(CURDIR)/$@ $(<:libultra/src/%=../%)
	tools/fixsym $@

$(LIBULTRA_ROM_SMIPS3): $(BUILD)/libultra_rom/%.o: libultra/src/%.s tools/fixabi tools/fixsym
	@mkdir -p $(dir $@)
	cd libultra/src/include; $(IRIX_CC) -I$(IDO)/include $(ULTRA_CPPFLAGS) $(ULTRA_ASFLAGS) -c -o $(CURDIR)/$@ $(<:libultra/src/%=../%)
	tools/fixabi $@
	tools/fixsym $@

################################################################################
# libultra_d

LIBULTRA_D_OBJ := $(addprefix $(BUILD)/libultra_d/,$(ULTRA_OBJ))
LIBULTRA_D_CMIPS3 := $(addprefix $(BUILD)/libultra_d/,$(ULTRA_CMIPS3))
LIBULTRA_D_SMIPS3 := $(addprefix $(BUILD)/libultra_d/,$(ULTRA_SMIPS3))

$(BUILD)/libultra_d/%.o: ULTRA_CPPFLAGS += -D_DEBUG
$(BUILD)/libultra_d/%.o: ULTRA_CFLAGS += -g
$(BUILD)/libultra_d/%.o: ULTRA_ASFLAGS += -g

$(LIBULTRA_D_CMIPS3): ULTRA_ARCH := -32 -mips3
$(LIBULTRA_D_SMIPS3): ULTRA_ARCH := -32 -mips3

$(BUILD)/lib/libultra_d.a: $(LIBULTRA_D_OBJ)
	@mkdir -p $(dir $@)
	$(U64_AR) rc $@ $(LIBULTRA_D_OBJ)

$(BUILD)/libultra_d/%.o: libultra/src/%.c
	@mkdir -p $(dir $@)
	cd libultra/src/include; $(IDO_CC) -I$(IDO)/include $(ULTRA_CPPFLAGS) $(ULTRA_CFLAGS) -c -o $(CURDIR)/$@ $(<:libultra/src/%=../%)

$(LIBULTRA_D_CMIPS3): $(BUILD)/libultra_d/%.o: libultra/src/%.c tools/fixabi
	@mkdir -p $(dir $@)
	cd libultra/src/include; $(IDO_CC) -I$(IDO)/include $(ULTRA_CPPFLAGS) $(ULTRA_CFLAGS) -c -o $(CURDIR)/$@ $(<:libultra/src/%=../%)
	tools/fixabi $@

$(BUILD)/libultra_d/%.o: libultra/src/%.s tools/fixsym
	@mkdir -p $(dir $@)
	cd libultra/src/include; $(IRIX_CC) -I$(IDO)/include $(ULTRA_CPPFLAGS) $(ULTRA_ASFLAGS) -c -o $(CURDIR)/$@ $(<:libultra/src/%=../%)
	tools/fixsym $@

$(LIBULTRA_D_SMIPS3): $(BUILD)/libultra_d/%.o: libultra/src/%.s tools/fixabi tools/fixsym
	@mkdir -p $(dir $@)
	cd libultra/src/include; $(IRIX_CC) -I$(IDO)/include $(ULTRA_CPPFLAGS) $(ULTRA_ASFLAGS) -c -o $(CURDIR)/$@ $(<:libultra/src/%=../%)
	tools/fixabi $@
	tools/fixsym $@

################################################################################
# Boot

BOOT_CPPFLAGS = -I$(LIBULTRA)/include -D_ULTRA64
BOOT_ASFLAGS = -mips2 -non_shared -G 0 -O2

$(BUILD)/Boot/Boot.o: ULTRA_ASOPT := -O2

$(BUILD)/lib/PR/Boot: $(BUILD)/Boot/Boot.elf
	$(U64_OBJCOPY) -O binary $< $@

$(BUILD)/Boot/Boot.elf: $(BUILD)/Boot/Boot.o
	$(U64_LD) -Tlibultra/src/PR/Boot.ld -o $@ $<

$(BUILD)/Boot/Boot.o: libultra/src/PR/Boot.s tools/fixsym
	@mkdir -p $(dir $@)
	$(IRIX_CC) -I$(IDO)/include $(BOOT_CPPFLAGS) $(BOOT_ASFLAGS) -c -o $@ $<
	tools/fixsym $@

################################################################################
# ucode

UCODE_BUILD := $(BUILD)/ucode

$(BUILD)/lib/PR/gspFast3D.fifo.o: $(wildcard libultra/src/PR/gspFast3D/*)

$(BUILD)/lib/PR/%.o: libultra/src/PR/%.asm
	@mkdir -p $(UCODE_BUILD)
	armips -equ REVISION $(LIBULTRA_REVISION) -strequ BUILD $(UCODE_BUILD) -sym $(UCODE_BUILD)/$(notdir $(<:.asm=.sym)) $<
	@mkdir -p $(dir $@)
	$(U64_CC) -I$(UCODE_BUILD) $(U64_ASFLAGS) -c -o $@ $(<:.asm=.s)
