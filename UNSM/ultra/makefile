SRC_OBJ := \
	build/src/parameters.o          \
	build/src/vitbl.o               \
	build/src/settime.o             \
	build/src/maptlb.o              \
	build/src/unmaptlball.o         \
	build/src/sprintf.o             \
	build/src/createmesgqueue.o     \
	build/src/seteventmesg.o        build/src/seteventmesg.data.o       \
	build/src/visetevent.o          \
	build/src/createthread.o        \
	build/src/recvmesg.o            \
	build/src/sptask.o              build/src/sptask.data.o             \
	build/src/sptaskyield.o         \
	build/src/sendmesg.o            \
	build/src/sptaskyielded.o       \
	build/src/startthread.o         \
	build/src/writebackdcacheall.o  \
	build/src/vimgr.o               build/src/vimgr.data.o              \
	build/src/visetmode.o           \
	build/src/viblack.o             \
	build/src/visetspecial.o        \
	build/src/pimgr.o               build/src/pimgr.data.o              \
	build/src/setthreadpri.o        \
	build/src/initialize.o          build/src/initialize.data.o         \
	build/src/viswapbuf.o           \
	build/src/sqrtf.o               \
	build/src/contreaddata.o        \
	build/src/controller.o          build/src/controller.data.o         \
	build/src/conteepprobe.o        \
	build/src/ll.o                  \
	build/src/invaldcache.o         \
	build/src/pidma.o               \
	build/src/bzero.o               \
	build/src/invalicache.o         \
	build/src/conteeplongread.o     \
	build/src/conteeplongwrite.o    \
	build/src/bcopy.o               \
	build/src/ortho.o               \
	build/src/perspective.o         build/src/perspective.data.o        \
	build/src/gettime.o             \
	build/src/llcvt.o               build/src/llcvt.data.o              \
	build/src/cosf.o                build/src/cosf.data.o               \
	build/src/sinf.o                build/src/sinf.data.o               \
	build/src/translate.o           \
	build/src/rotate.o              build/src/rotate.data.o             \
	build/src/scale.o               \
	build/src/aisetfreq.o           \
	build/src/bnkf.o                \
	build/src/writebackdcache.o     \
	build/src/aigetlen.o            \
	build/src/aisetnextbuf.o        build/src/aisetnextbuf.data.o       \
	build/src/timerintr.o           build/src/timerintr.data.o          \
	build/src/xprintf.o             build/src/xprintf.data.o            \
	build/src/string.o              \
	build/src/thread.o              build/src/thread.data.o             \
	build/src/interrupt.o           \
	build/src/vi.o                  build/src/vi.data.o                 \
	build/src/exceptasm.o           \
	build/src/libm_vals.o           \
	build/src/virtualtophysical.o   \
	build/src/spsetstat.o           \
	build/src/spsetpc.o             \
	build/src/sprawdma.o            \
	build/src/sp.o                  \
	build/src/spgetstat.o           \
	build/src/getthreadpri.o        \
	build/src/vigetcurrcontext.o    \
	build/src/viswapcontext.o       \
	build/src/getcount.o            \
	build/src/piacs.o               build/src/piacs.data.o              \
	build/src/pirawdma.o            \
	build/src/devmgr.o              \
	build/src/setsr.o               \
	build/src/getsr.o               \
	build/src/setfpccsr.o           \
	build/src/sirawread.o           \
	build/src/sirawwrite.o          \
	build/src/maptlbrdb.o           \
	build/src/pirawread.o           \
	build/src/siacs.o               build/src/siacs.data.o              \
	build/src/sirawdma.o            \
	build/src/settimer.o            \
	build/src/conteepwrite.o        \
	build/src/jammesg.o             \
	build/src/pigetcmdq.o           \
	build/src/conteepread.o         build/src/conteepread.data.o        \
	build/src/mtx.o                 \
	build/src/normalize.o           \
	build/src/ai.o                  \
	build/src/setcompare.o          \
	build/src/xlitob.o              build/src/xlitob.data.o             \
	build/src/xldtob.o              build/src/xldtob.data.o             \
	build/src/vimodentsclan1.o      \
	build/src/vimodepallan1.o       \
	build/src/kdebugserver.o        build/src/kdebugserver.data.o       \
	build/src/syncputchars.o        build/src/syncputchars.data.o       \
	build/src/setintmask.o          \
	build/src/destroythread.o       \
	build/src/probetlb.o            \
	build/src/si.o                  \
	build/src/ldiv.o                \
	build/src/getcause.o            \
	build/src/atomic.o

OBJ := \
	lib/PR/header.o         \
	lib/PR/ipl3.o           \
	lib/PR/crt0.o           \
	lib/PR/rspboot.o        \
	lib/PR/gspFast3D.fifo.o \
	lib/PR/aspMain.o        \
	lib/libultra_rom.a

CC      := mips-linux-gnu-gcc
AR      := mips-linux-gnu-ar

CCFLAG  := -march=vr4300 -mfix4300 -mfp32 -mno-abicalls -mno-check-zero-division
CCFLAG  += -fno-PIC -ffreestanding -fno-common -fno-zero-initialized-in-bss
CCFLAG  += -fno-toplevel-reorder -G0
CCFLAG  += -Iinclude -Wall -Wextra -Wpedantic -O2

ARMIPS  := armips

.PHONY: default
default: $(OBJ)

lib/libultra_rom.a: $(SRC_OBJ) | lib
	$(AR) rc $@ $^

build/src/%.o: src/%.S | build/src
	$(CC) $(CCFLAG) -c -o $@ $<

build/src/%.o: src/%.c | build/src
	$(CC) $(CCFLAG) -c -o $@ $<

lib/PR/gspFast3D.fifo.o: $(wildcard PR/gspFast3D/*)

lib/PR/%.o: PR/%.asm PR/rsp.inc | build/PR lib/PR
	$(ARMIPS) -sym build/$(<:.asm=.sym) $<
	$(CC) $(CCFLAG) -c -o $@ $(<:.asm=.S)

lib/PR/%.o: PR/%.S | lib/PR
	$(CC) $(CCFLAG) -c -o $@ $<

build/src build/PR lib lib/PR:
	mkdir -p $@

.PHONY: clean
clean:
	rm -rf build lib
