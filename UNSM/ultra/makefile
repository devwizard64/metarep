SRC_OBJ := \
	build/src/parameters.o              \
	build/src/osViModeTable.o           \
	build/src/osSetTime.o               \
	build/src/osMapTLB.o                \
	build/src/osUnmapTLBAll.o           \
	build/src/sprintf.o                 \
	build/src/osCreateMesgQueue.o       \
	build/src/osSetEventMesg.o          \
	build/src/osViSetEvent.o            \
	build/src/osCreateThread.o          \
	build/src/osRecvMesg.o              \
	build/src/osSpTaskStart.o           \
	build/src/osSpTaskYield.o           \
	build/src/osSendMesg.o              \
	build/src/osSpTaskYielded.o         \
	build/src/osStartThread.o           \
	build/src/osWritebackDCacheAll.o    \
	build/src/osCreateViManager.o       build/src/osCreateViManager.data.o  \
	build/src/osViSetMode.o             \
	build/src/osViBlack.o               \
	build/src/osViSetSpecialFeatures.o  \
	build/src/osCreatePiManager.o       build/src/osCreatePiManager.data.o  \
	build/src/osSetThreadPri.o          \
	build/src/osInitialize.o            build/src/osInitialize.data.o       \
	build/src/osViSwapBuffer.o          \
	build/src/sqrtf.o                   \
	build/src/osContReadData.o          \
	build/src/osContInit.o              build/src/osContInit.data.o         \
	build/src/osEepromProbe.o           \
	build/src/ll_multdiv.o              \
	build/src/osInvalDCache.o           \
	build/src/osPiStartDma.o            \
	build/src/bzero.o                   \
	build/src/osInvalICache.o           \
	build/src/osEepromLongRead.o        \
	build/src/osEepromLongWrite.o       \
	build/src/bcopy.o                   \
	build/src/guOrtho.o                 \
	build/src/guPerspective.o           build/src/guPerspective.data.o      \
	build/src/osGetTime.o               \
	build/src/ll_cvt.o                  build/src/ll_cvt.data.o             \
	build/src/cosf.o                    build/src/cosf.data.o               \
	build/src/sinf.o                    build/src/sinf.data.o               \
	build/src/guTranslate.o             \
	build/src/guRotate.o                build/src/guRotate.data.o           \
	build/src/guScale.o                 \
	build/src/osAiSetFrequency.o        \
	build/src/alBnkfNew.o               \
	build/src/osWritebackDCache.o       \
	build/src/osAiGetLength.o           \
	build/src/osAiSetNextBuffer.o       build/src/osAiSetNextBuffer.data.o  \
	build/src/__osTimerService.o        build/src/__osTimerService.data.o   \
	build/src/printf.o                  build/src/printf.data.o             \
	build/src/string.o                  \
	build/src/__osDequeueThread.o       build/src/__osDequeueThread.data.o  \
	build/src/__osInterrupt.o           \
	build/src/__osViInit.o              build/src/__osViInit.data.o         \
	build/src/__osException.o           build/src/__osException.data.o      \
	build/src/__libm_qnan_f.o           \
	build/src/osVirtualToPhysical.o     \
	build/src/__osSpSetStatus.o         \
	build/src/__osSpSetPc.o             \
	build/src/__osSpRawStartDma.o       \
	build/src/__osSpDeviceBusy.o        \
	build/src/__osSpGetStatus.o         \
	build/src/osGetThreadPri.o          \
	build/src/__osViGetCurrentContext.o \
	build/src/__osViSwapContext.o       \
	build/src/osGetCount.o              \
	build/src/__osPiAccess.o            build/src/__osPiAccess.data.o       \
	build/src/osPiRawStartDma.o         \
	build/src/__osDevMgrMain.o          \
	build/src/__osSetSR.o               \
	build/src/__osGetSR.o               \
	build/src/__osSetFpcCsr.o           \
	build/src/__osSiRawReadIo.o         \
	build/src/__osSiRawWriteIo.o        \
	build/src/osMapTLBRdb.o             \
	build/src/osPiRawReadIo.o           \
	build/src/__osSiAccess.o            build/src/__osSiAccess.data.o       \
	build/src/__osSiRawStartDma.o       \
	build/src/osSetTimer.o              \
	build/src/osEepromWrite.o           \
	build/src/osJamMesg.o               \
	build/src/osPiGetCmdQueue.o         \
	build/src/osEepromRead.o            \
	build/src/guMtxIdent.o              \
	build/src/guNormalize.o             \
	build/src/__osAiDeviceBusy.o        \
	build/src/__osSetCompare.o          \
	build/src/_Litob.o                  build/src/_Litob.data.o             \
	build/src/_Ldtob.o                  build/src/_Ldtob.data.o             \
	build/src/osViModeNtscLan1.o        \
	build/src/osViModePalLan1.o         \
	build/src/8032A860.o                build/src/8032A860.data.o           \
	build/src/__osSyncPutChars.o        build/src/__osSyncPutChars.data.o   \
	build/src/osSetIntMask.o            build/src/osSetIntMask.data.o       \
	build/src/osDestroyThread.o         \
	build/src/__osProbeTLB.o            \
	build/src/__osSiDeviceBusy.o        \
	build/src/ldiv.o                    \
	build/src/__osGetCause.o            \
	build/src/__osAtomicDec.o           \
	build/src/data.o

OBJ := \
	lib/PR/ipl3.o           \
	lib/PR/crt0.o           \
	lib/PR/rspboot.o        \
	lib/PR/gspFast3D.fifo.o \
	lib/PR/aspMain.o        \
	lib/libultra_rom.a

CC      := mips-linux-gnu-gcc
LD      := mips-linux-gnu-ld
CPP     := mips-linux-gnu-cpp
OBJCOPY := mips-linux-gnu-objcopy
NM      := mips-linux-gnu-nm
CC      += -march=vr4300 -mfix4300 -mfp32 -mno-abicalls -mno-check-zero-division
CC      += -fno-PIC -ffreestanding -fno-common -fno-zero-initialized-in-bss
CC      += -fno-toplevel-reorder -G 0

CC      += -I include -Wall -Wextra -Wpedantic -O2

ARMIPS  := $(HOME)/sm64/exe/armips

default: $(OBJ)

lib/libultra_rom.a: $(SRC_OBJ) | lib
	$(AR) rc $@ $^

build/src/%.o: src/%.c | build/src
	$(CC) -c -o $@ $<

build/src/%.o: src/%.S | build/src
	$(CC) -c -o $@ $<

lib/PR/%.o: PR/%.S | lib/PR
	$(CC) -c -o $@ $<

lib/PR/%.o: PR/%.asm | build/PR lib/PR
	$(ARMIPS) $<
	$(CC) -c -o $@ $(<:.asm=.s)

build/src build/PR lib lib/PR:
	mkdir -p $@

clean:
	rm -rf build lib

.PHONY: default clean
