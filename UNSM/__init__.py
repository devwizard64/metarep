import os
import struct

import main
import table
import ultra

import UNSM.asm
import UNSM.c
import UNSM.exe.lang

rm_table = (
    "BACKGROUND",
    "OPA_SURF",
    "OPA_DECAL",
    "OPA_INTER",
    "TEX_EDGE",
    "XLU_SURF",
    "XLU_DECAL",
    "XLU_INTER",
)

def fmt_time(x):
    if x >= 30:
        s = "30*%d" % (x//30)
        x %= 30
        if x != 0:
            s += "+%d" % x
        return s
    else:
        return "%d" % x

def fmt_g(x):
    return "%3d" % x

sym_E0_t_crt0 = {
    0x80200600: table.sym("stack_main+0x400"),

    # ultra/crt0.S
    0x80246000: table.sym("start", table.GLOBL),

    0x8033A580: table.sym("bss_main_start"),
}

imm_E0_t_crt0 = {
    0x80246004: "bss_main_size_hi",
    0x8024600C: "bss_main_size_lo",
}

sym_E0_t_ultra = {
    0x00000000: table.sym("NULL"),

    # ultra/src/parameter.S
    0x80000300: table.sym("osTvType"),
    0x80000304: table.sym("osRomType"),
    0x80000308: table.sym("osRomBase"),
    0x8000030C: table.sym("osResetType"),
    0x80000310: table.sym("osCicId"),
    0x80000314: table.sym("osVersion"),
    0x80000318: table.sym("osMemSize"),
    0x8000031C: table.sym("osAppNMIBuffer"),

    # ultra/src/osSetTime.S
    0x803223B0: table.sym_fnc("osSetTime", arg=(
        "OSTime time",
    ), flag=table.GLOBL),

    # ultra/src/osMapTLB.S
    0x803223E0: table.sym_fnc("osMapTLB", arg=(
        "s32 index",
        "OSPageMask pm",
        "void *vaddr",
        "u32 evenpaddr",
        "u32 oddpaddr",
        "s32 asid",
    ), flag=table.GLOBL),

    # ultra/src/osUnmapTLBAll.S
    0x803224A0: table.sym_fnc("osUnmapTLBAll", flag=table.GLOBL),

    # ultra/src/sprintf.S
    0x803224F0: table.sym_fnc("sprintf", "int", (
        "char *",
        "const char *",
        "..."
    ), table.GLOBL),
    0x8032255C: table.sym("ultra_8032255C"),

    # ultra/src/osCreateMesgQueue.S
    0x803225A0: table.sym_fnc("osCreateMesgQueue", arg=(
        "OSMesgQueue *mq",
        "OSMesg *msg",
        "s32 count",
    ), flag=table.GLOBL),

    # ultra/src/osSetEventMesg.S
    0x803225D0: table.sym_fnc("osSetEventMesg", arg=(
        "OSEvent e",
        "OSMesgQueue *mq",
        "OSMesg m",
    ), flag=table.GLOBL),

    # ultra/src/osViSetEvent.S
    0x80322640: table.sym_fnc("osViSetEvent", arg=(
        "OSMesgQueue *mq",
        "OSMesg msg",
        "u32 retraceCount",
    ), flag=table.GLOBL),

    # ultra/src/osCreateThread.S
    0x803226B0: table.sym_fnc("osCreateThread", arg=(
        "OSThread *t",
        "OSId id",
        "void (*entry)(void *)",
        "void *arg",
        "void *sp",
        "OSPri pri",
    ), flag=table.GLOBL),

    # ultra/src/osRecvMesg.S
    0x80322800: table.sym_fnc("osRecvMesg", "s32", (
        "OSMesgQueue *mq",
        "OSMesg *msg",
        "s32 flag",
    ), table.GLOBL),

    # ultra/src/osSpTaskStart.S
    0x80322940: table.sym("ultra_80322940"),
    0x80322A5C: table.sym_fnc("osSpTaskLoad", arg=(
        "OSTask *task",
    ), flag=table.GLOBL),
    0x80322BBC: table.sym_fnc("osSpTaskStartGo", "s32", (
        "OSTask *task",
    ), table.GLOBL),

    # ultra/src/osSpTaskYield.S
    0x80322C00: table.sym_fnc("osSpTaskYield", "s32", flag=table.GLOBL),

    # ultra/src/osSendMesg.S
    0x80322C20: table.sym_fnc("osSendMesg", arg=(
        "OSMesgQueue *mq",
        "OSMesg msg",
        "s32 flag",
    ), flag=table.GLOBL),

    # ultra/src/osSpTaskYielded.S
    0x80322D70: table.sym_fnc("osSpTaskYielded", "OSYieldResult", (
        "OSTask *task"
    ), table.GLOBL),

    # ultra/src/osStartThread.S
    0x80322DF0: table.sym_fnc("osStartThread", arg=(
        "OSThread *t",
    ), flag=table.GLOBL),

    # ultra/src/osWritebackDCacheAll.S
    0x80322F40: table.sym_fnc("osWritebackDCacheAll", flag=table.GLOBL),

    # ultra/src/osCreateViManager.S
    0x80322F70: table.sym_fnc("osCreateViManager", arg=(
        "OSPri pri",
    ), flag=table.GLOBL),
    0x803230F4: table.sym("viMgrMain"),

    # ultra/src/osViSetMode.S
    0x803232D0: table.sym_fnc("osViSetMode", arg=(
        "OSViMode *mode"
    ), flag=table.GLOBL),

    # ultra/src/osViBlack.S
    0x80323340: table.sym_fnc("osViBlack", arg=(
        "u8 active"
    ), flag=table.GLOBL),

    # ultra/src/osViSetSpecialFeatures.S
    0x803233B0: table.sym_fnc("osViSetSpecialFeatures", arg=(
        "u32 func"
    ), flag=table.GLOBL),

    # ultra/src/osCreatePiManager.S
    0x80323570: table.sym_fnc("osCreatePiManager", arg=(
        "OSPri pri",
        "OSMesgQueue *cmdQ",
        "OSMesg *cmdBuf",
        "s32 cmdMsgCnt",
    ), flag=table.GLOBL),

    # ultra/src/osSetThreadPri.S
    0x803236F0: table.sym_fnc("osSetThreadPri", arg=(
        "OSThread *t",
        "OSPri pri"
    ), flag=table.GLOBL),

    # ultra/src/osInitialize.S
    0x803237D0: table.sym_fnc("osInitialize", flag=table.GLOBL),

    # ultra/src/osViSwapBuffer.S
    0x80323A00: table.sym_fnc("osViSwapBuffer", arg=(
        "void *vaddr",
    ), flag=table.GLOBL),

    # ultra/src/sqrtf.S
    0x80323A50: table.sym_fnc("sqrtf", "float", arg=(
        "float value",
    ), flag=table.GLOBL),

    # ultra/src/osContReadData.S
    0x80323A60: table.sym_fnc("osContStartReadData", "s32", (
        "OSMesgQueue *mq"
    ), table.GLOBL),
    0x80323B24: table.sym_fnc("osContGetReadData", arg=(
        "OSContPad *pad"
    ), flag=table.GLOBL),
    0x80323BCC: table.sym("__osPackReadData"),

    # ultra/src/osContInit.S
    0x80323CC0: table.sym_fnc("osContInit", "s32", (
        "OSMesgQueue *mq",
        "u8 *bitpattern",
        "OSContStatus *status",
    ), table.GLOBL),
    0x80323EBC: table.sym("__osContGetInitData"),
    0x80323F8C: table.sym("__osPackRequestData"),

    # ultra/src/osEepromProbe.S
    0x80324080: table.sym_fnc("osEepromProbe", "s32", (
        "OSMesgQueue *mq"
    ), table.GLOBL),

    # ultra/src/ll_multdiv.S
    0x803240F0: table.sym("__ull_rshift", table.GLOBL), # unused
    0x8032411C: table.sym("__ull_rem", table.GLOBL),
    0x80324158: table.sym("__ull_div", table.GLOBL),
    0x80324194: table.sym("__ll_lshift", table.GLOBL),
    0x803241C0: table.sym("__ll_rem", table.GLOBL), # unused
    0x803241FC: table.sym("__ll_div", table.GLOBL),
    0x80324258: table.sym("__ll_mul", table.GLOBL),
    0x80324288: table.sym("__ull_divremi", table.GLOBL), # unused
    0x803242E8: table.sym("__ll_mod", table.GLOBL), # unused
    0x80324384: table.sym("__ll_rshift", table.GLOBL), # unused

    # ultra/src/osInvalDCache.S
    0x803243B0: table.sym_fnc("osInvalDCache", arg=(
        "void *vaddr",
        "s32 nbytes",
    ), flag=table.GLOBL),

    # ultra/src/osPiStartDma.S
    0x80324460: table.sym_fnc("osPiStartDma", arg=(
        "OSIoMesg *mb",
        "s32 priority",
        "s32 direction",
        "u32 devAddr",
        "void *vAddr",
        "u32 nbytes",
        "OSMesgQueue *mq",
    ), flag=table.GLOBL),

    # ultra/src/bzero.S
    0x80324570: table.sym_fnc("bzero", arg=(
        "void *",
        "size_t"
    ), flag=table.GLOBL),

    # ultra/src/osInvalICache.S
    0x80324610: table.sym_fnc("osInvalICache", arg=(
        "void *vaddr",
        "s32 nbytes",
    ), flag=table.GLOBL),

    # ultra/src/osEepromLongRead.S
    0x80324690: table.sym_fnc("osEepromLongRead", arg=(
        "OSMesgQueue *mq",
        "u8 address",
        "u8 *buffer",
        "s32 nbytes",
    ), flag=table.GLOBL),

    # ultra/src/osEepromLongWrite.S
    0x803247D0: table.sym_fnc("osEepromLongWrite", arg=(
        "OSMesgQueue *mq",
        "u8 address",
        "u8 *buffer",
        "s32 nbytes",
    ), flag=table.GLOBL),

    # ultra/src/bcopy.S
    0x80324910: table.sym_fnc("bcopy", arg=(
        "const void *",
        "void *",
        "size_t",
    ), flag=table.GLOBL),

    # ultra/src/guOrtho.S
    0x80324C20: table.sym_fnc("guOrthoF", arg=(
        "float mf[4][4]",
        "float l",
        "float r",
        "float b",
        "float t",
        "float n",
        "float f",
        "float scale",
    ), flag=table.GLOBL),
    0x80324D74: table.sym_fnc("guOrtho", arg=(
        "Mtx *m",
        "float l",
        "float r",
        "float b",
        "float t",
        "float n",
        "float f",
        "float scale",
    ), flag=table.GLOBL),

    # ultra/src/guPerspective.S
    0x80324DE0: table.sym_fnc("guPerspectiveF", arg=(
        "float mf[4][4]",
        "u16 *perspNorm",
        "float fovy",
        "float aspect",
        "float near",
        "float far",
        "float scale",
    ), flag=table.GLOBL),
    0x80325010: table.sym_fnc("guPerspective", arg=(
        "Mtx *m",
        "u16 *perspNorm",
        "float fovy",
        "float aspect",
        "float near",
        "float far",
        "float scale",
    ), flag=table.GLOBL),

    # ultra/src/osGetTime.S
    0x80325070: table.sym_fnc("osGetTime", "OSTime", flag=table.GLOBL),

    # ultra/src/ll_cvt.S
    0x80325100: table.sym("__d_to_ll", table.GLOBL), # unused
    0x8032511C: table.sym("__f_to_ll", table.GLOBL), # unused
    0x80325138: table.sym("__d_to_ull", table.GLOBL),
    0x803251D8: table.sym("__f_to_ull", table.GLOBL), # unused
    0x80325274: table.sym("__ll_to_d", table.GLOBL), # unused
    0x8032528C: table.sym("__ll_to_f", table.GLOBL), # unused
    0x803252A4: table.sym("__ull_to_d", table.GLOBL),
    0x803252D8: table.sym("__ull_to_f", table.GLOBL), # unused

    # ultra/src/cosf.S
    0x80325310: table.sym_fnc("cosf", "float", (
        "float angle",
    ), table.GLOBL),

    # ultra/src/sinf.S
    0x80325480: table.sym_fnc("sinf", "float", (
        "float angle",
    ), table.GLOBL),

    # ultra/src/guTranslate.S
    0x80325640: table.sym_fnc("guTranslateF", arg=(
        "float mf[4][4]",
        "float x",
        "float y",
        "float z",
    ), flag=table.GLOBL), # unused
    0x80325688: table.sym_fnc("guTranslate", arg=(
        "Mtx *m",
        "float x",
        "float y",
        "float z",
    ), flag=table.GLOBL),

    # ultra/src/guRotate.S
    0x803256E0: table.sym_fnc("guRotateF", arg=(
        "float mf[4][4]",
        "float a",
        "float x",
        "float y",
        "float z",
    ), flag=table.GLOBL),
    0x80325874: table.sym_fnc("guRotate", arg=(
        "Mtx *m",
        "float a",
        "float x",
        "float y",
        "float z",
    ), flag=table.GLOBL),

    # ultra/src/guScale.S
    0x803258D0: table.sym_fnc("guScaleF", arg=(
        "float mf[4][4]",
        "float x",
        "float y",
        "float z",
    ), flag=table.GLOBL),
    0x80325924: table.sym_fnc("guScale", arg=(
        "Mtx *m",
        "float x",
        "float y",
        "float z",
    ), flag=table.GLOBL),

    # ultra/src/osAiSetFrequency.S
    0x80325970: table.sym_fnc("osAiSetFrequency", arg=(
        "u32 frequency",
    ), flag=table.GLOBL),

    # ultra/src/80325AE0.S
    0x80325AD0: table.sym("ultra_80325AD0"), # unused
    0x80325AD8: table.sym("ultra_80325AD8"), # unused
    0x80325AE0: table.sym("ultra_80325AE0"),
    0x80325BD4: table.sym("alBnkfNew"), # unused
    0x80325CD8: table.sym_fnc("alSeqFileNew", arg=(
        "ALSeqFile *file",
        "u8 *base",
    ), flag=table.GLOBL),

    # ultra/src/osWritebackDCache.S
    0x80325D20: table.sym_fnc("osWritebackDCache", arg=(
        "void *vaddr",
        "s32 nbytes"
    ), flag=table.GLOBL),

    # ultra/src/osAiGetLength.S
    0x80325DA0: table.sym_fnc("osAiGetLength", "u32", flag=table.GLOBL),

    # ultra/src/osAiSetNextBuffer.S
    0x80325DB0: table.sym_fnc("osAiSetNextBuffer", "s32", (
        "void *vaddr",
        "u32 nbytes"
    ), table.GLOBL),

    # ultra/src/__osTimerService.S
    0x80325E60: table.sym("__osTimerServicesInit", table.GLOBL),
    0x80325EEC: table.sym("__osTimerInterrupt", table.GLOBL),
    0x80326064: table.sym("__osSetTimerIntr", table.GLOBL),
    0x803260D8: table.sym("__osInsertTimer", table.GLOBL),

    # ultra/src/printf.o
    0x80326260: table.sym("ultra_80326260", table.GLOBL),
    0x80326A8C: table.sym("ultra_80326A8C"),
    0x80326B40: table.sym_fnc("L80326B40", flag=table.GLOBL),
    0x80326B90: table.sym_fnc("L80326B90", flag=table.GLOBL),
    0x80326D90: table.sym_fnc("L80326D90", flag=table.GLOBL),
    0x80326F74: table.sym_fnc("L80326F74", flag=table.GLOBL),
    0x8032717C: table.sym_fnc("L8032717C", flag=table.GLOBL),
    0x803272A4: table.sym_fnc("L803272A4", flag=table.GLOBL),
    0x80327308: table.sym_fnc("L80327308", flag=table.GLOBL),
    0x803273A0: table.sym_fnc("L803273A0", flag=table.GLOBL),

    # ultra/src/string.S
    0x803273F0: table.sym_fnc("memcpy", "void *", (
        "void *",
        "const void *",
        "size_t",
    ), table.GLOBL),
    0x8032741C: table.sym_fnc("strlen", "size_t", (
        "const char *",
    ), table.GLOBL),
    0x80327444: table.sym_fnc("strchr", "const char *", (
        "const char *",
        "int",
    ), table.GLOBL),

    # ultra/src/__osDequeueThread.S
    0x80327490: table.sym("__osDequeueThread", table.GLOBL),

    # ultra/src/__osInterrupt.S
    0x803274D0: table.sym("__osDisableInt", table.GLOBL),
    0x803274F0: table.sym("__osRestoreInt", table.GLOBL),

    # ultra/src/__osViInit.S
    0x80327510: table.sym("__osViInit", table.GLOBL),

    # ultra/src/__osException.S
    0x80327640: table.sym("__osExceptionPreamble", table.GLOBL),
    0x80327650: table.sym("__osException"),
    0x803278E4: table.sym_fnc("L803278E4", flag=table.GLOBL),
    0x80327904: table.sym_fnc("L80327904", flag=table.GLOBL),
    0x80327938: table.sym_fnc("L80327938", flag=table.GLOBL),
    0x80327A68: table.sym_fnc("L80327A68", flag=table.GLOBL),
    0x80327AC4: table.sym_fnc("L80327AC4", flag=table.GLOBL),
    0x80327AE4: table.sym_fnc("L80327AE4", flag=table.GLOBL),
    0x80327B1C: table.sym_fnc("L80327B1C", flag=table.GLOBL),
    0x80327B68: table.sym_fnc("L80327B68", flag=table.GLOBL),
    0x80327B98: table.sym("send_mesg"),
    0x80327C80: table.sym("__osEnqueueAndYield", table.GLOBL),
    0x80327D10: table.sym("__osEnqueueThread", table.GLOBL),
    0x80327D58: table.sym("__osPopThread", table.GLOBL),
    0x80327D68: table.sym("__osDispatchThread", table.GLOBL),
    0x80327EA8: table.sym("__osCleanupThread", table.GLOBL),

    # ultra/src/osVirtualToPhysical.S
    0x80327EB0: table.sym_fnc("osVirtualToPhysical", "u32", (
        "void *vaddr",
    ), table.GLOBL),

    # ultra/src/__osSpSetStatus.S
    0x80327F30: table.sym("__osSpSetStatus", table.GLOBL),

    # ultra/src/__osSpSetPc.S
    0x80327F40: table.sym("__osSpSetPc", table.GLOBL),

    # ultra/src/__osSpRawStartDma.S
    0x80327F80: table.sym("__osSpRawStartDma", table.GLOBL),

    # ultra/src/__osSpDeviceBusy.S
    0x80328010: table.sym("__osSpDeviceBusy", table.GLOBL),

    # ultra/src/__osSpGetStatus.S
    0x80328040: table.sym("__osSpGetStatus", table.GLOBL),

    # ultra/src/osGetThreadPri.S
    0x80328050: table.sym_fnc("osGetThreadPri", "OSPri", (
        "OSThread *t",
    ), table.GLOBL),

    # ultra/src/__osViGetCurrentContext.S
    0x80328070: table.sym("__osViGetCurrentContext", table.GLOBL),

    # ultra/src/__osViSwapContext.S
    0x80328080: table.sym("__osViSwapContext", table.GLOBL),

    # ultra/src/osGetCount.S
    0x803283E0: table.sym_fnc("osGetCount", "u32", flag=table.GLOBL),

    # ultra/src/__osPiAccess.S
    0x803283F0: table.sym("__osPiCreateAccessQueue", table.GLOBL),
    0x80328440: table.sym("__osPiGetAccess"), # unused
    0x80328484: table.sym("__osPiRelAccess"), # unused

    # ultra/src/osPiRawStartDma.S
    0x803284B0: table.sym("osPiRawStartDma", table.GLOBL),

    # ultra/src/__osDevMgrMain.S
    0x80328590: table.sym("__osDevMgrMain", table.GLOBL),

    # ultra/src/__osSetSR.S
    0x80328710: table.sym_fnc("__osSetSR", arg=(
        "u32 value",
    ), flag=table.GLOBL),

    # ultra/src/__osGetSR.S
    0x80328720: table.sym_fnc("__osGetSR", "u32", flag=table.GLOBL),

    # ultra/src/__osSetFpcCsr.S
    0x80328730: table.sym_fnc("__osSetFpcCsr", "u32", (
        "u32 value",
    ), table.GLOBL),

    # ultra/src/__osSiRawReadIo.S
    0x80328740: table.sym("__osSiRawReadIo", table.GLOBL),

    # ultra/src/__osSiRawWriteIo.S
    0x80328790: table.sym("__osSiRawWriteIo", table.GLOBL),

    # ultra/src/osMapTLBRdb.S
    0x803287E0: table.sym_fnc("osMapTLBRdb", flag=table.GLOBL),

    # ultra/src/osPiRawReadIo.S
    0x80328840: table.sym_fnc("osPiRawReadIo", "s32", (
        "u32 devAddr",
        "u32 *data",
    ), table.GLOBL),

    # ultra/src/__osSiAccess.S
    0x803288A0: table.sym("__osSiCreateAccessQueue", table.GLOBL),
    0x803288F0: table.sym("__osSiGetAccess", table.GLOBL),
    0x80328934: table.sym("__osSiRelAccess", table.GLOBL),

    # ultra/src/__osSiRawStartDma.S
    0x80328960: table.sym("__osSiRawStartDma", table.GLOBL),

    # ultra/src/osSetTimer.S
    0x80328A10: table.sym_fnc("osSetTimer", arg=(
        "OSTimer *timer",
        "OSTime countdown",
        "OSTime interval",
        "OSMesgQueue *mq",
        "OSMesg msg",
    ), flag=table.GLOBL),

    # ultra/src/osEepromWrite.S
    0x80328AF0: table.sym_fnc("osEepromWrite", arg=(
        "OSMesgQueue *mq",
        "u8 address",
        "u8 *buffer",
    ), flag=table.GLOBL),
    0x80328CA0: table.sym("__osPackEepWriteData"),
    0x80328DAC: table.sym("__osEepStatus", table.GLOBL),

    # ultra/src/osJamMesg.S
    0x80328FD0: table.sym_fnc("osJamMesg", arg=(
        "OSMesgQueue *mq",
        "OSMesg msg",
        "s32 flag",
    ), flag=table.GLOBL),

    # ultra/src/osPiGetCmdQueue.S
    0x80329120: table.sym_fnc("osPiGetCmdQueue", "OSMesgQueue *",
    flag=table.GLOBL),

    # ultra/src/osEepromRead.S
    0x80329150: table.sym_fnc("osEepromRead", arg=(
        "OSMesgQueue *mq",
        "u8 address",
        "u8 *buffer",
    ), flag=table.GLOBL),
    0x80329340: table.sym("__osPackEepReadData"),

    # ultra/src/guMtxIdent.S
    0x80329450: table.sym_fnc("guMtxF2L", arg=(
        "float mf[4][4]",
        "Mtx *m",
    ), flag=table.GLOBL),
    0x80329550: table.sym_fnc("guMtxIdentF", arg=(
        "float mf[4][4]",
    ), flag=table.GLOBL),
    0x803295D8: table.sym_fnc("guMtxIdent", arg=(
        "Mtx *m",
    ), flag=table.GLOBL), # unused
    0x80329608: table.sym_fnc("guMtxL2F", arg=(
        "float mf[4][4]",
        "Mtx *m",
    ), flag=table.GLOBL), # unused

    # ultra/src/guNormalize.S
    0x803296C0: table.sym_fnc("guNormalize", arg=(
        "float *x",
        "float *y",
        "float *z",
    ), flag=table.GLOBL),

    # ultra/src/__osAiDeviceBusy.S
    0x80329750: table.sym("__osAiDeviceBusy", table.GLOBL),

    # ultra/src/__osSetCompare.S
    0x80329780: table.sym_fnc("__osSetCompare", arg=(
        "u32 value",
    ), flag=table.GLOBL),

    # ultra/src/_Litob.S
    0x80329790: table.sym("_Litob", table.GLOBL),

    # ultra/src/_Ldtob.S
    0x80329A90: table.sym("_Ldtob", table.GLOBL),
    0x8032A090: table.sym("ultra_8032A090"),
    0x8032A170: table.sym("ultra_8032A170"),

    # ultra/src/8032A860.S
    0x8032A860: table.sym("ultra_8032A860"), # unused
    0x8032A890: table.sym("ultra_8032A890"),
    0x8032A8E8: table.sym("ultra_8032A8E8"),
    0x8032A9A8: table.sym("ultra_8032A9A8"),
    0x8032AA80: table.sym("ultra_8032AA80"),
    0x8032AACC: table.sym("ultra_8032AACC"),
    0x8032AAF8: table.sym("ultra_8032AAF8", table.GLOBL),

    # ultra/src/__osSyncPutChars.S
    0x8032ACE0: table.sym("__osSyncPutChars", table.GLOBL), # unused

    # ultra/src/osSetIntMask.S
    0x8032AE10: table.sym_fnc("osSetIntMask", "OSIntMask", (
        "OSIntMask im",
    ), table.GLOBL), # unused

    # ultra/src/osDestroyThread.S
    0x8032AE70: table.sym_fnc("osDestroyThread", arg=(
        "OSThread *t",
    ), flag=table.GLOBL),

    # ultra/src/__osProbeTLB.S
    0x8032AF70: table.sym("__osProbeTLB", table.GLOBL),

    # ultra/src/__osSiDeviceBusy.S
    0x8032B030: table.sym("__osSiDeviceBusy", table.GLOBL),

    # ultra/src/ldiv.S
    0x8032B060: table.sym("lldiv", table.GLOBL),
    0x8032B160: table.sym("ldiv", table.GLOBL),

    # ultra/src/__osGetCause.S
    0x8032B1F0: table.sym_fnc("__osGetCause", "u32", flag=table.GLOBL),

    # ultra/src/__osAtomicDec.S
    0x8032B200: table.sym("__osAtomicDec", table.GLOBL),

    0x803358D0: table.sym("__osViDevMgr+0x00"),
    0x803358D4: table.sym("__osViDevMgr+0x04"),
    0x803358D8: table.sym("__osViDevMgr+0x08"),
    0x803358DC: table.sym("__osViDevMgr+0x0C"),
    0x803358E0: table.sym("__osViDevMgr+0x10"),
    0x803358E4: table.sym("__osViDevMgr+0x14"),

    0x803358F0: table.sym("__osPiDevMgr+0x00"),
    0x803358F4: table.sym("__osPiDevMgr+0x04"),
    0x803358F8: table.sym("__osPiDevMgr+0x08"),
    0x803358FC: table.sym("__osPiDevMgr+0x0C"),
    0x80335900: table.sym("__osPiDevMgr+0x10"),
    0x80335904: table.sym("__osPiDevMgr+0x14"),

    0x80335910: table.sym("osClockRate+0"),
    0x80335914: table.sym("osClockRate+4"),

    0x80364BA0: table.sym("ultra_bss+0x0000"),
    0x80364C20: table.sym("ultra_bss+0x0080"),
    0x80364C60: table.sym("ultra_bss+0x00C0"),
    0x80364E10: table.sym("ultra_bss+0x0270"),
    0x80365E10: table.sym("ultra_bss+0x1270"),
    0x80365E28: table.sym("ultra_bss+0x1288"),
    0x80365E40: table.sym("ultra_bss+0x12A0"),
    0x80365E42: table.sym("ultra_bss+0x12A2"),
    0x80365E44: table.sym("ultra_bss+0x12A4"),
    0x80365E58: table.sym("ultra_bss+0x12B8"),
    0x80365E5A: table.sym("ultra_bss+0x12BA"),
    0x80365E5C: table.sym("ultra_bss+0x12BC"),
    0x80365E6C: table.sym("ultra_bss+0x12CC"),
    0x80365E70: table.sym("ultra_bss+0x12D0"),
    0x80366020: table.sym("ultra_bss+0x1480"),
    0x80367020: table.sym("ultra_bss+0x2480"),
    0x80367038: table.sym("ultra_bss+0x2498"),
    0x80367040: table.sym("ultra_bss+0x24A0"),
    0x80367050: table.sym("ultra_bss+0x24B0"),
    0x8036708C: table.sym("ultra_bss+0x24EC"),
    0x80367090: table.sym("ultra_bss+0x24F0"),
    0x80367091: table.sym("ultra_bss+0x24F1"),
    0x80367098: table.sym("ultra_bss+0x24F8"),
    0x803670B8: table.sym("ultra_bss+0x2518"),
    0x803670D0: table.sym("ultra_bss+0x2530"),
    0x803670E0: table.sym("ultra_bss+0x2540"),
    0x803670F0: table.sym("ultra_bss+0x2550"),
    0x80367110: table.sym("ultra_bss+0x2570"),
    0x80367114: table.sym("ultra_bss+0x2574"),
    0x80367118: table.sym("ultra_bss+0x2578"),
    0x8036711C: table.sym("ultra_bss+0x257C"),
    0x80367120: table.sym("ultra_bss+0x2580"),
    0x80367130: table.sym("ultra_bss+0x2590"),
    0x80367138: table.sym("ultra_bss+0x2598"),
    0x80367150: table.sym("ultra_bss+0x25B0"),
    0x80367158: table.sym("ultra_bss+0x25B8"),
    0x80367170: table.sym("ultra_bss+0x25D0"),
    0x803671AC: table.sym("ultra_bss+0x260C"),
    0x803671B0: table.sym("ultra_bss+0x2610"),
    0x803672B0: table.sym("ultra_bss+0x2710"),
}

imm_E0_t_ultra = {
    0x80325454: "%hi(ultra_rodata_80339810)",
    0x8032546C: "%lo(ultra_rodata_80339810)",
    0x8032561C: "%hi(ultra_rodata_80339860)",
    0x80325634: "%lo(ultra_rodata_80339860)",
}

sym_E0_d_ultra = {
    # ==========================================================================
    # text
    # ==========================================================================

    # ultra/src/osViModeTable.c
    0x80335010: table.sym_var("osViModeTable", "OSViMode", "[]"),

    # ultra/src/osCreateViManager.data.c
    0x803358D0: table.sym_var("__osViDevMgr", "struct ultra_0"),

    # ultra/src/osCreatePiManager.data.c
    0x803358F0: table.sym_var("__osPiDevMgr", "struct ultra_0"),

    # ultra/src/osInitialize.data.c
    0x80335910: table.sym_var("osClockRate", "u64"),
    0x80335918: table.sym_var("osViClock", "u32"),

    # ultra/src/osContInit.data.c
    0x80335920: table.sym_var("__osContinitialized", "u32"),

    # ultra/src/osAiSetNextBuffer.data.c
    0x80335930: table.sym_var("ultra_data_80335930", "u8"),

    # ultra/src/__osTimerService.c
    0x80335940: table.sym_var("__osTimerList", "void *"),

    # ultra/src/printf.data.c
    0x80335950: table.sym_var("ultra_data_80335950", "char", "[]"),
    0x80335974: table.sym_var("ultra_data_80335974", "char", "[]"),

    # ultra/src/__osDequeueThread.data.c
    0x803359A0: table.sym_var("__osThreadTail", "__OSThreadTail"),
    0x803359A8: table.sym_var("__osRunQueue", "OSThread *"),
    0x803359AC: table.sym_var("__osActiveQueue", "OSThread *"),
    0x803359B0: table.sym_var("__osRunningThread", "OSThread *"),
    0x803359B4: table.sym_var("__osFaultedThread", "OSThread *"),

    # ultra/src/__osViInit.data.c
    0x803359C0: table.sym_var("ultra_data_803359C0", "OSViContext"),
    0x803359F0: table.sym_var("ultra_data_803359F0", "OSViContext"),
    0x80335A20: table.sym_var("__osViCurr", "OSViContext *"),
    0x80335A24: table.sym_var("__osViNext", "OSViContext *"),
    0x80335A28: table.sym_var("ultra_data_80335A28", "u32"),
    0x80335A2C: table.sym_var("ultra_data_80335A2C", "u32"),

    # ultra/src/__osException.data.c
    0x80335A30: table.sym_var_fnc("__osHwIntTable", lst="[5]"),
    0x80335A44: table.sym_var("ultra_data_80335A44", "u32"),
    0x80335A48: table.sym_var("ultra_data_80335A48", "u32"),

    # ultra/src/__osPiAccess.data.c
    0x80335A50: table.sym_var("__osPiAccessQueueEnabled", "u32"),

    # ultra/src/__osSiAccess.data.c
    0x80335A60: table.sym_var("__osSiAccessQueueEnabled", "u32"),

    # ultra/src/_Litob.data.c
    0x80335A70: table.sym_var("ultra_data_80335A70", "char", "[]"),
    0x80335A84: table.sym_var("ultra_data_80335A84", "char", "[]"),

    # ultra/src/osViModeNtscLan1.c
    0x80335AA0: table.sym_var("osViModeNtscLan1", "OSViMode"),

    # ultra/src/osViModePalLan1.c
    0x80335AF0: table.sym_var("osViModePalLan1", "OSViMode"),

    # ultra/src/8032A860.data.c
    0x80335B40: table.sym_var("ultra_data_80335B40", "u32"),
    0x80335B44: table.sym_var("ultra_data_80335B44", "u32"),
    0x80335B48: table.sym_var("ultra_data_80335B48", "u32"),

    # ultra/src/__osSyncPutChars.data.c
    0x80335B50: table.sym_var("__osRdbSendMessage", "u32", flag=table.GLOBL),
    0x80335B54: table.sym_var("__osRdbWriteOK", "u32", flag=table.GLOBL),

    # ==========================================================================
    # rodata
    # ==========================================================================

    # ultra/src/guPerspective.data.c
    0x803397B0: table.sym_var("ultra_rodata_803397B0", "const double"),

    # ultra/src/ll_cvt.data.c
    0x803397C0: table.sym_var("ultra_rodata_803397C0", "const u64"),
    0x803397C8: table.sym_var("ultra_rodata_803397C8", "const u64"),

    # ultra/src/cosf.data.c
    0x803397D0: table.sym_var("ultra_rodata_803397D0", "const double", "[]"),
    0x803397F8: table.sym_var("ultra_rodata_803397F8", "const double"),
    0x80339800: table.sym_var("ultra_rodata_80339800", "const double"),
    0x80339808: table.sym_var("ultra_rodata_80339808", "const double"),
    0x80339810: table.sym_var("ultra_rodata_80339810", "const float"),

    # ultra/src/sinf.data.c
    0x80339820: table.sym_var("ultra_rodata_80339820", "const double", "[]"),
    0x80339848: table.sym_var("ultra_rodata_80339848", "const double"),
    0x80339850: table.sym_var("ultra_rodata_80339850", "const double"),
    0x80339858: table.sym_var("ultra_rodata_80339858", "const double"),
    0x80339860: table.sym_var("ultra_rodata_80339860", "const double"),

    # ultra/src/guRotate.data.c
    0x80339870: table.sym_var("ultra_rodata_80339870", "const float"),

    # ultra/src/printf.data.c
    0x80339880: table.sym_var("ultra_rodata_80339880", "const char", "[]"),
    0x80339884: table.sym_var("ultra_rodata_80339884", "const char", "[]"),
    0x8033988C: table.sym_var("ultra_rodata_8033988C", "const u32", "[]"),
    0x803398A4: table.sym_var_fnc("ultra_rodata_803398A4", "const", "[]"),

    # ultra/src/__osException.data.c
    0x80339980: table.sym_var("ultra_rodata_80339980", "const u8", "[]"),
    0x803399A0: table.sym_var_fnc("ultra_rodata_803399A0", "const", "[]"),

    # ultra/src/__libm_qnan_f.c
    0x803399D0: table.sym_var("__libm_qnan_f", "const u32"),

    # ultra/src/_Ldtob.data.c
    0x803399E0: table.sym_var("ultra_rodata_803399E0", "const f64", "[]"),
    0x80339A28: table.sym_var("ultra_rodata_80339A28", "const char", "[]"),
    0x80339A2C: table.sym_var("ultra_rodata_80339A2C", "const char", "[]"),
    0x80339A30: table.sym_var("ultra_rodata_80339A30", "const char", "[]"),
    0x80339A38: table.sym_var("ultra_rodata_80339A38", "const double"),

    # ultra/src/osSetIntMask.data.c
    0x80339A40: table.sym_var("__osRcpImTable", "const u16", "[]"),

    # ==========================================================================
    # bss
    # ==========================================================================
}

sym_E0_t_spboot = {
    0x0400100C: table.sym("_0400100C"),
    0x04001040: table.sym("_04001040"),
    0x04001068: table.sym("_04001068"),
}

sym_E0_t_gF3D_0 = {
    0x0400109C: table.sym(".L0400109C"),
    0x040010A8: table.sym("_040010A8"),
    0x040010B8: table.sym("_040010B8"),
    0x040010C8: table.sym("_040010C8"),
    0x040010D4: table.sym("_040010D4"),
    0x040010F8: table.sym("_040010F8"),
    0x040010FC: table.sym("_040010FC"),
    0x0400111C: table.sym("_0400111C"),
    0x0400113C: table.sym("_0400113C"),
    0x04001164: table.sym("_04001164"),
    0x04001178: table.sym("_04001178"),
    0x040012D0: table.sym("_040012D0"),
    0x040013A8: table.sym("_040013A8"),
    0x04001420: table.sym("_04001420"),
    0x04001438: table.sym("_04001438"),
    0x04001444: table.sym("_04001444"),
    0x04001484: table.sym("_04001484"),
    0x040014E8: table.sym("_040014E8"),
    0x04001510: table.sym("_04001510"),
    0x04001524: table.sym("_04001524"),
    0x040015E4: table.sym(".L040015E4"),
    0x040015E8: table.sym("_040015E8"),
    0x04001780: table.sym("_04001780"),
    0x04001800: table.sym("_04001800"),
    0x04001998: table.sym("_04001998"),
    0x040019C4: table.sym(".L040019C4"),
    0x04001A30: table.sym("_04001A30"),
}

sym_E0_t_gF3D_1 = {
    0x04001000: table.sym("_04001000"),
    0x04001058: table.sym("_04001058"),
    0x04001060: table.sym(".L04001060"),
}

sym_E0_t_gF3D_2 = {
    0x040010FC: table.sym("_040010FC"),
    0x040017D4: table.sym("_040017D4"),
    0x04001804: table.sym(".L04001804_2"),
    0x04001980: table.sym("_04001980"),
}

sym_E0_t_gF3D_3 = {
    0x040010FC: table.sym("_040010FC"),
    0x04001804: table.sym(".L04001804_3"),
}

sym_E0_t_gF3D_4 = {
    0x04001788: table.sym("_04001788"),
}

sym_E0_d_gF3D = {
}

sym_E0_t_aMain = {
    0x040010D4: table.sym("_040010D4"),
    0x04001118: table.sym("_04001118"),
    0x04001150: table.sym("_04001150"),
    0x04001184: table.sym("_04001184"),
    0x040011B0: table.sym("_040011B0"),
    0x040018E8: table.sym("_040018E8"),
    0x040019D8: table.sym("_040019D8"),
    0x04001BB0: table.sym("_04001BB0"),
    0x04001C48: table.sym("_04001C48"),
    0x04001CB8: table.sym("_04001CB8"),
    0x04001D04: table.sym("_04001D04"),
    0x04001D50: table.sym("_04001D50"),
    0x04001DBC: table.sym("_04001DBC"),
}

sym_E0_d_aMain = {
}

sym_E0_t_main = {
    # src/main.S
    0x80246050: table.sym_fnc("debug_update"), # unused
    0x80246170: table.sym_fnc("dummy"), # unused
    0x802461CC: table.sym_fnc("debug_main"),
    0x802461DC: table.sym_fnc("debug_scheduler_main"),
    0x802461EC: table.sym_fnc("debug_scheduler_vi"),
    0x802461FC: table.sym_fnc("scheduler_init"),
    0x802462E0: table.sym_fnc("scheduler_init_mem"),
    0x80246338: table.sym_fnc("thread_create", arg=(
        "OSThread *t",
        "OSId id",
        "void (*entry)(void *)",
        "void *arg",
        "void *sp",
        "OSPri pri",
    )),
    0x8024639C: table.sym_fnc("scheduler_msg_prenmi"),
    0x802463EC: table.sym_fnc("scheduler_flush"),
    0x8024651C: table.sym_fnc("scheduler_task_start", arg=(
        "int type",
    )),
    0x8024659C: table.sym_fnc("scheduler_task_yield"),
    0x802465EC: table.sym_fnc("scheduler_msg_gfxtask"),
    0x80246648: table.sym_fnc("scheduler_audtask_skip"),
    0x8024669C: table.sym_fnc("scheduler_msg_vi"),
    0x802467FC: table.sym_fnc("scheduler_msg_sp"),
    0x8024694C: table.sym_fnc("scheduler_msg_dp"),
    0x802469B8: table.sym_fnc("scheduler_main", arg=(
        "unused void *arg",
    )),
    0x80246B14: table.sym_fnc("scheduler_vq_init", arg=(
        "int i",
        "struct scheduler_vq_t *vq",
        "OSMesgQueue *mq",
        "OSMesg msg",
    ), flag=table.GLOBL),
    0x80246B74: table.sym_fnc("scheduler_queue_task", arg=(
        "struct sptask_t *task",
    )), # unused
    0x80246BB4: table.sym_fnc("scheduler_queue_audtask", arg=(
        "struct sptask_t *task",
    ), flag=table.GLOBL),
    0x80246C10: table.sym_fnc("scheduler_queue_gfxtask", arg=(
        "struct sptask_t *task",
    ), flag=table.GLOBL),
    0x80246C9C: table.sym_fnc("scheduler_audio_enable"), # unused
    0x80246CB8: table.sym_fnc("scheduler_audio_disable"), # unused
    0x80246CF0: table.sym_fnc("idle_main", arg=(
        "unused void *arg",
    )),
    0x80246DF8: table.sym_fnc("main", flag=table.GLOBL),

    # src/app.S
    0x80246E70: table.sym_fnc("video_draw_dp"),
    0x802471A4: table.sym_fnc("video_draw_sp"),
    0x80247284: table.sym_fnc("video_draw_zimg"),
    0x802473C8: table.sym_fnc("video_draw_cimg"),
    0x802474B8: table.sym_fnc("video_cimg_clear", arg=(
        "u32 fill",
    ), flag=table.GLOBL),
    0x80247620: table.sym_fnc("video_vp_clear", arg=(
        "Vp *vp",
    ), flag=table.GLOBL),
    0x8024784C: table.sym_fnc("video_draw_border"),
    0x802479BC: table.sym_fnc("video_vp_scissor", arg=(
        "Vp *vp",
    ), flag=table.GLOBL),
    0x80247B3C: table.sym_fnc("video_draw_task"),
    0x80247CCC: table.sym_fnc("video_draw_start", flag=table.GLOBL),
    0x80247D14: table.sym_fnc("video_draw_end", flag=table.GLOBL),
    0x80247DB4: table.sym_fnc("video_draw_reset"),
    0x80247F08: table.sym_fnc("video_init"),
    0x80247FDC: table.sym_fnc("video_start"),
    0x80248090: table.sym_fnc("video_end"),
    0x802481E0: table.sym_fnc("input_update_record"), # unused
    0x80248304: table.sym_fnc("input_update_stick", arg=(
        "struct controller_t *cnt",
    )),
    0x80248498: table.sym_fnc("input_update_demo"),
    0x80248638: table.sym_fnc("input_update"),
    0x80248824: table.sym_fnc("input_init"),
    0x80248964: table.sym_fnc("app_init"),
    0x80248AF0: table.sym_fnc("app_main", arg=(
        "unused void *arg",
    ), flag=table.GLOBL),

    # src/audio.S
    0x80248C40: table.sym("audio_80248C40", table.GLOBL),
    0x80248C58: table.sym("audio_80248C58", table.GLOBL),
    0x80248CE8: table.sym("audio_80248CE8", table.GLOBL),
    0x80248D78: table.sym("audio_80248D78", table.GLOBL),
    0x80248DC0: table.sym("audio_80248DC0", table.GLOBL),
    0x80248E08: table.sym("audio_80248E08", table.GLOBL),
    0x80248E54: table.sym("audio_80248E54", table.GLOBL),
    0x80248FEC: table.sym("audio_80248FEC", table.GLOBL),
    0x80249070: table.sym("audio_80249070", table.GLOBL),
    0x80249178: table.sym("audio_80249178", table.GLOBL),
    0x8024922C: table.sym("audio_8024922C", table.GLOBL),
    0x8024927C: table.sym("audio_8024927C", table.GLOBL),
    0x802492D0: table.sym("audio_802492D0", table.GLOBL),
    0x80249310: table.sym("audio_80249310", table.GLOBL),
    0x8024934C: table.sym("audio_8024934C", table.GLOBL),
    0x80249398: table.sym("audio_80249398", table.GLOBL),
    0x80249404: table.sym("audio_80249404", table.GLOBL),
    0x80249448: table.sym("audio_80249448", table.GLOBL),
    0x80249494: table.sym("audio_80249494"),
    0x802494D8: table.sym("audio_802494D8", table.GLOBL),
    0x80249500: table.sym_fnc("audio_main", arg=(
        "unused void *arg",
    ), flag=table.GLOBL),

    # src/game.S
    0x802495E0: table.sym("game_802495E0", table.GLOBL),
    0x802496B8: table.sym("game_802496B8"),
    0x80249764: table.sym("game_80249764"),
    0x8024978C: table.sym("game_8024978C"),
    0x802497B8: table.sym("game_802497B8", table.GLOBL),
    0x8024982C: table.sym("game_8024982C"), # unused
    0x8024983C: table.sym("game_8024983C", table.GLOBL),
    0x8024995C: table.sym("game_8024995C"),
    0x80249A10: table.sym("game_80249A10"),
    0x80249AB4: table.sym("game_80249AB4"),
    0x80249CD8: table.sym("game_80249CD8"),
    0x8024A124: table.sym("game_8024A124"),
    0x8024A18C: table.sym("game_8024A18C"),
    0x8024A1D8: table.sym("game_8024A1D8"),
    0x8024A374: table.sym("game_8024A374"),
    0x8024A584: table.sym("game_8024A584"),
    0x8024A700: table.sym("game_8024A700"),
    0x8024A7B4: table.sym("game_8024A7B4"),
    0x8024A85C: table.sym("game_8024A85C"),
    0x8024A9CC: table.sym("game_8024A9CC", table.GLOBL),
    0x8024AEDC: table.sym("game_8024AEDC"),
    0x8024B13C: table.sym("game_8024B13C"),
    0x8024B390: table.sym("game_8024B390"),
    0x8024B3E4: table.sym("game_8024B3E4"),
    0x8024B5D4: table.sym("game_8024B5D4"),
    0x8024B6CC: table.sym("game_8024B6CC"),
    0x8024B798: table.sym("game_8024B798", table.GLOBL),
    0x8024B7C0: table.sym("game_8024B7C0"),
    0x8024B880: table.sym("game_8024B880"),
    0x8024B940: table.sym("game_8024B940"), # unused
    0x8024B9B8: table.sym("game_8024B9B8"),
    0x8024BA8C: table.sym("game_8024BA8C"),
    0x8024BCD8: table.sym("game_8024BCD8", table.GLOBL), # s callback
    0x8024BD5C: table.sym("game_8024BD5C", table.GLOBL), # s callback
    0x8024BE14: table.sym("game_8024BE14", table.GLOBL), # s callback
    0x8024BFA0: table.sym("game_8024BFA0", table.GLOBL), # s callback

    # src/player_touch.S
    0x8024BFF0: table.sym("player_touch_8024BFF0"),
    0x8024C0B8: table.sym("player_touch_8024C0B8"),
    0x8024C16C: table.sym("player_touch_8024C16C", table.GLOBL),
    0x8024C1D8: table.sym("player_touch_8024C1D8"),
    0x8024C51C: table.sym("player_touch_8024C51C"),
    0x8024C618: table.sym("player_touch_8024C618", table.GLOBL),
    0x8024C66C: table.sym("player_touch_8024C66C", table.GLOBL),
    0x8024C6C0: table.sym("player_touch_8024C6C0", table.GLOBL),
    0x8024C780: table.sym("player_touch_8024C780", table.GLOBL),
    0x8024C894: table.sym("player_touch_8024C894", table.GLOBL),
    0x8024C8FC: table.sym("player_touch_8024C8FC", table.GLOBL),
    0x8024C928: table.sym("player_touch_8024C928", table.GLOBL),
    0x8024CA68: table.sym("player_touch_8024CA68", table.GLOBL),
    0x8024CAF8: table.sym("player_touch_8024CAF8", table.GLOBL),
    0x8024CB58: table.sym("player_touch_8024CB58"),
    0x8024CBFC: table.sym("player_touch_8024CBFC", table.GLOBL),
    0x8024CC7C: table.sym("player_touch_8024CC7C", table.GLOBL),
    0x8024CE08: table.sym("player_touch_8024CE08"),
    0x8024D0B4: table.sym("player_touch_8024D0B4"),
    0x8024D130: table.sym("player_touch_8024D130"),
    0x8024D16C: table.sym("player_touch_8024D16C"), # unused
    0x8024D2BC: table.sym("player_touch_8024D2BC"),
    0x8024D578: table.sym("player_touch_8024D578"),
    0x8024D72C: table.sym("player_touch_8024D72C"),
    0x8024D804: table.sym("player_touch_8024D804"),
    0x8024D8B0: table.sym("player_touch_8024D8B0"),
    0x8024D998: table.sym("player_touch_8024D998"),
    0x8024DAAC: table.sym("player_touch_8024DAAC"),
    0x8024DB2C: table.sym("player_touch_8024DB2C", table.GLOBL), # data
    0x8024DBF0: table.sym("player_touch_8024DBF0", table.GLOBL), # data
    0x8024DC28: table.sym("player_touch_8024DC28", table.GLOBL), # data
    0x8024DE4C: table.sym("player_touch_8024DE4C", table.GLOBL), # data
    0x8024DF10: table.sym("player_touch_8024DF10", table.GLOBL), # data
    0x8024E0C4: table.sym("player_touch_8024E0C4", table.GLOBL), # data
    0x8024E2FC: table.sym("player_touch_8024E2FC", table.GLOBL),
    0x8024E420: table.sym("player_touch_8024E420", table.GLOBL), # data
    0x8024E6EC: table.sym("player_touch_8024E6EC", table.GLOBL), # data
    0x8024E778: table.sym("player_touch_8024E778", table.GLOBL), # data
    0x8024E7D4: table.sym("player_touch_8024E7D4", table.GLOBL), # data
    0x8024E8F0: table.sym("player_touch_8024E8F0", table.GLOBL), # data
    0x8024E9D0: table.sym("player_touch_8024E9D0", table.GLOBL), # data
    0x8024EAD8: table.sym("player_touch_8024EAD8", table.GLOBL), # data
    0x8024EC54: table.sym("player_touch_8024EC54", table.GLOBL), # data
    0x8024ED84: table.sym("player_touch_8024ED84", table.GLOBL), # data
    0x8024EE44: table.sym("player_touch_8024EE44", table.GLOBL), # data
    0x8024EFF8: table.sym("player_touch_8024EFF8", table.GLOBL), # data
    0x8024F134: table.sym("player_touch_8024F134"), # unused
    0x8024F170: table.sym("player_touch_8024F170", table.GLOBL), # data
    0x8024F1E0: table.sym("player_touch_8024F1E0", table.GLOBL), # data
    0x8024F354: table.sym("player_touch_8024F354", table.GLOBL), # data
    0x8024F4AC: table.sym("player_touch_8024F4AC", table.GLOBL), # data
    0x8024F55C: table.sym("player_touch_8024F55C", table.GLOBL), # data
    0x8024F5CC: table.sym("player_touch_8024F5CC", table.GLOBL), # data
    0x8024F6A4: table.sym("player_touch_8024F6A4", table.GLOBL), # data
    0x8024F7A8: table.sym("player_touch_8024F7A8"),
    0x8024F8BC: table.sym("player_touch_8024F8BC", table.GLOBL), # data
    0x8024FA60: table.sym("player_touch_8024FA60", table.GLOBL), # data
    0x8024FB30: table.sym("player_touch_8024FB30", table.GLOBL), # data
    0x8024FD2C: table.sym("player_touch_8024FD2C", table.GLOBL), # data
    0x8024FE6C: table.sym("player_touch_8024FE6C"),
    0x8024FF04: table.sym("player_touch_8024FF04"),
    0x80250098: table.sym("player_touch_80250098"),
    0x80250198: table.sym("player_touch_80250198", table.GLOBL), # data
    0x80250230: table.sym("player_touch_80250230"),
    0x802503F0: table.sym("player_touch_802503F0", table.GLOBL),
    0x802505C8: table.sym("player_touch_802505C8"),
    0x8025065C: table.sym("player_touch_8025065C"),
    0x80250724: table.sym("player_touch_80250724"),
    0x80250778: table.sym("player_touch_80250778"),
    0x802507FC: table.sym("player_touch_802507FC", table.GLOBL),

    # src/player.S
    0x80250940: table.sym("player_80250940", table.GLOBL),
    0x8025097C: table.sym("player_8025097C", table.GLOBL),
    0x802509B8: table.sym("player_802509B8", table.GLOBL),
    0x80250B04: table.sym("player_80250B04", table.GLOBL),
    0x80250C7C: table.sym("player_80250C7C", table.GLOBL),
    0x80250D38: table.sym("player_80250D38", table.GLOBL),
    0x80250E54: table.sym("player_80250E54", table.GLOBL),
    0x80251020: table.sym("player_80251020", table.GLOBL),
    0x802510DC: table.sym("player_802510DC", table.GLOBL),
    0x80251120: table.sym("player_80251120", table.GLOBL),
    0x8025118C: table.sym("player_8025118C", table.GLOBL),
    0x80251274: table.sym("player_80251274", table.GLOBL),
    0x80251310: table.sym("player_80251310", table.GLOBL),
    0x80251444: table.sym("player_80251444", table.GLOBL),
    0x802514AC: table.sym("player_802514AC", table.GLOBL),
    0x80251510: table.sym("player_80251510", table.GLOBL),
    0x80251574: table.sym("player_80251574", table.GLOBL),
    0x802515D8: table.sym("player_802515D8", table.GLOBL),
    0x8025163C: table.sym("player_8025163C", table.GLOBL),
    0x80251708: table.sym("player_80251708", table.GLOBL),
    0x8025177C: table.sym("player_8025177C", table.GLOBL),
    0x802518A8: table.sym("player_802518A8", table.GLOBL),
    0x80251A48: table.sym("player_80251A48", table.GLOBL),
    0x80251AFC: table.sym("player_80251AFC", table.GLOBL),
    0x80251B54: table.sym("player_80251B54", table.GLOBL),
    0x80251BD4: table.sym("player_80251BD4", table.GLOBL),
    0x80251CFC: table.sym("player_80251CFC", table.GLOBL),
    0x80251E24: table.sym("player_80251E24"),
    0x80251F24: table.sym("player_80251F24", table.GLOBL),
    0x80252000: table.sym("player_80252000", table.GLOBL),
    0x802521A0: table.sym("player_802521A0", table.GLOBL),
    0x8025229C: table.sym("player_8025229C"),
    0x802523C8: table.sym("player_802523C8"),
    0x80252460: table.sym("player_80252460"),
    0x802529E4: table.sym("player_802529E4"),
    0x80252BD4: table.sym("player_80252BD4"),
    0x80252C18: table.sym("player_80252C18"),
    0x80252CF4: table.sym("player_80252CF4", table.GLOBL),
    0x80252E5C: table.sym("player_80252E5C", table.GLOBL),
    0x802530A0: table.sym("player_802530A0", table.GLOBL),
    0x80253178: table.sym("player_80253178", table.GLOBL),
    0x802531C4: table.sym("player_802531C4", table.GLOBL),
    0x80253218: table.sym("player_80253218", table.GLOBL),
    0x80253300: table.sym("player_80253300", table.GLOBL),
    0x802533E4: table.sym("player_802533E4", table.GLOBL),
    0x80253488: table.sym("player_80253488", table.GLOBL),
    0x80253588: table.sym("player_80253588"),
    0x80253720: table.sym("player_80253720"),
    0x80253838: table.sym("player_80253838"),
    0x8025395C: table.sym("player_8025395C"),
    0x80253A60: table.sym("player_80253A60"),
    0x80253D58: table.sym("player_80253D58"),
    0x80253EC0: table.sym("player_80253EC0"),
    0x80254060: table.sym("player_80254060"),
    0x802542B4: table.sym("player_802542B4"),
    0x80254338: table.sym("player_80254338"),
    0x80254390: table.sym("player_80254390"),
    0x802543E8: table.sym("player_802543E8"),
    0x80254588: table.sym("player_80254588"),
    0x80254768: table.sym("player_80254768"), # unused
    0x80254830: table.sym("player_80254830", table.GLOBL),
    0x80254B20: table.sym("player_80254B20", table.GLOBL),
    0x80254F44: table.sym("player_80254F44", table.GLOBL),

    # src/player_move.S
    0x80255080: table.sym("player_move_80255080", table.GLOBL),
    0x8025509C: table.sym("player_move_8025509C", table.GLOBL),
    0x802550B0: table.sym("player_move_802550B0", table.GLOBL),
    0x802550C0: table.sym("player_move_802550C0", table.GLOBL),
    0x80255238: table.sym("player_move_80255238", table.GLOBL),
    0x802552FC: table.sym("player_move_802552FC", table.GLOBL),
    0x80255414: table.sym("player_move_80255414", table.GLOBL),
    0x80255654: table.sym("player_move_80255654", table.GLOBL),
    0x8025570C: table.sym("player_move_8025570C", table.GLOBL),
    0x8025580C: table.sym("player_move_8025580C", table.GLOBL),
    0x802559B0: table.sym("player_move_802559B0", table.GLOBL),
    0x80255A34: table.sym("player_move_80255A34", table.GLOBL),
    0x80255B04: table.sym("player_move_80255B04"),
    0x80255D88: table.sym("player_move_80255D88", table.GLOBL),
    0x80255EC4: table.sym("player_move_80255EC4"),
    0x802560AC: table.sym("player_move_802560AC"),
    0x802564E0: table.sym("player_move_802564E0"),
    0x80256584: table.sym("player_move_80256584"),
    0x8025661C: table.sym("player_move_8025661C"),
    0x802569F8: table.sym("player_move_802569F8"),
    0x80256B24: table.sym("player_move_80256B24", table.GLOBL),
    0x80256CD8: table.sym("player_move_80256CD8"), # unused
    0x80256D8C: table.sym("player_move_80256D8C"), # unused

    # src/player_demo.S
    0x80256E00: table.sym("player_demo_80256E00"),
    0x80256E88: table.sym("player_demo_80256E88", table.GLOBL),
    0x80257060: table.sym("player_demo_80257060", table.GLOBL), # o callback
    0x802570DC: table.sym("player_demo_802570DC", table.GLOBL), # o callback
    0x80257198: table.sym("player_demo_80257198", table.GLOBL), # g callback
    0x80257270: table.sym("player_demo_80257270"), # unused
    0x802572B0: table.sym("player_demo_802572B0"),
    0x8025733C: table.sym("player_demo_8025733C"),
    0x80257450: table.sym("player_demo_80257450"),
    0x802574E8: table.sym("player_demo_802574E8"),
    0x80257548: table.sym("player_demo_80257548"),
    0x802575A8: table.sym("player_demo_802575A8", table.GLOBL),
    0x80257640: table.sym("player_demo_80257640", table.GLOBL),
    0x80257748: table.sym("player_demo_80257748"),
    0x80257980: table.sym("player_demo_80257980"),
    0x80257A0C: table.sym("player_demo_80257A0C"),
    0x80257AB0: table.sym("player_demo_80257AB0"),
    0x80257CE4: table.sym("player_demo_80257CE4"),
    0x80257EAC: table.sym("player_demo_80257EAC"),
    0x80258184: table.sym("player_demo_80258184"),
    0x80258420: table.sym("player_demo_80258420"),
    0x802584DC: table.sym("player_demo_802584DC"),
    0x802585C0: table.sym("player_demo_802585C0"),
    0x802586CC: table.sym("player_demo_802586CC"),
    0x80258744: table.sym("player_demo_80258744"),
    0x802587EC: table.sym("player_demo_802587EC"),
    0x8025883C: table.sym("player_demo_8025883C"),
    0x8025888C: table.sym("player_demo_8025888C"),
    0x802588F8: table.sym("player_demo_802588F8"),
    0x80258964: table.sym("player_demo_80258964"),
    0x80258A7C: table.sym("player_demo_80258A7C"),
    0x80258B24: table.sym("player_demo_80258B24"),
    0x80258BA8: table.sym("player_demo_80258BA8"),
    0x80258DAC: table.sym("player_demo_80258DAC"),
    0x80258F94: table.sym("player_demo_80258F94"),
    0x80259264: table.sym("player_demo_80259264"),
    0x802593CC: table.sym("player_demo_802593CC"),
    0x802594D4: table.sym("player_demo_802594D4"),
    0x80259608: table.sym("player_demo_80259608"),
    0x80259740: table.sym("player_demo_80259740"),
    0x802597AC: table.sym("player_demo_802597AC"),
    0x80259854: table.sym("player_demo_80259854"),
    0x802598D0: table.sym("player_demo_802598D0"),
    0x80259C30: table.sym("player_demo_80259C30"),
    0x80259CE8: table.sym("player_demo_80259CE8"),
    0x80259D74: table.sym("player_demo_80259D74"),
    0x80259E00: table.sym("player_demo_80259E00"),
    0x80259EF8: table.sym("player_demo_80259EF8"),
    0x80259FCC: table.sym("player_demo_80259FCC"),
    0x8025A040: table.sym("player_demo_8025A040"),
    0x8025A0BC: table.sym("player_demo_8025A0BC"),
    0x8025A494: table.sym("player_demo_8025A494"),
    0x8025A610: table.sym("player_demo_8025A610"),
    0x8025A6FC: table.sym("player_demo_8025A6FC"),
    0x8025A858: table.sym("player_demo_8025A858"),
    0x8025A9AC: table.sym("player_demo_8025A9AC"),
    0x8025AE0C: table.sym("player_demo_8025AE0C"),
    0x8025AEA8: table.sym("player_demo_8025AEA8"),
    0x8025AFFC: table.sym("player_demo_8025AFFC"),
    0x8025B050: table.sym("player_demo_8025B050"),
    0x8025B0A4: table.sym("player_demo_8025B0A4"),
    0x8025B0F8: table.sym("player_demo_8025B0F8"),
    0x8025B11C: table.sym("player_demo_8025B11C"),
    0x8025B178: table.sym("player_demo_8025B178"),
    0x8025B234: table.sym("player_demo_8025B234"),
    0x8025B2EC: table.sym("player_demo_8025B2EC"),
    0x8025B404: table.sym("player_demo_8025B404"),
    0x8025B454: table.sym("player_demo_8025B454"),
    0x8025B520: table.sym("player_demo_8025B520"),
    0x8025B58C: table.sym("player_demo_8025B58C"),
    0x8025B654: table.sym("player_demo_8025B654"),
    0x8025B760: table.sym("player_demo_8025B760"),
    0x8025B9A8: table.sym("player_demo_8025B9A8"),
    0x8025BBEC: table.sym("player_demo_8025BBEC"),
    0x8025BC80: table.sym("player_demo_8025BC80"),
    0x8025BEB8: table.sym("player_demo_8025BEB8"),
    0x8025BF64: table.sym("player_demo_8025BF64"),
    0x8025C014: table.sym("player_demo_8025C014"),
    0x8025C0C4: table.sym("player_demo_8025C0C4"),
    0x8025C1C0: table.sym("player_demo_8025C1C0"),
    0x8025C498: table.sym("player_demo_8025C498"),
    0x8025C600: table.sym("player_demo_8025C600"),
    0x8025C6F8: table.sym("player_demo_8025C6F8"),
    0x8025C904: table.sym("player_demo_8025C904"),
    0x8025CA48: table.sym("player_demo_8025CA48"),
    0x8025CBDC: table.sym("player_demo_8025CBDC"),
    0x8025CD6C: table.sym("player_demo_8025CD6C"),
    0x8025CEF0: table.sym("player_demo_8025CEF0"),
    0x8025CFE4: table.sym("player_demo_8025CFE4"),
    0x8025D040: table.sym("player_demo_8025D040"),
    0x8025D1D4: table.sym("player_demo_8025D1D4"),
    0x8025D4F0: table.sym("player_demo_8025D4F0"),
    0x8025D70C: table.sym("player_demo_8025D70C"),
    0x8025D798: table.sym("player_demo_main", table.GLOBL),

    # src/player_hang.S
    0x8025DD70: table.sym("player_hang_8025DD70"),
    0x8025DE1C: table.sym("player_hang_8025DE1C"),
    0x8025DF04: table.sym("player_hang_8025DF04"),
    0x8025E21C: table.sym("player_hang_8025E21C"),
    0x8025E5A8: table.sym("player_hang_8025E5A8"),
    0x8025E7A4: table.sym("player_hang_8025E7A4"),
    0x8025E830: table.sym("player_hang_8025E830"),
    0x8025E930: table.sym("player_hang_8025E930"),
    0x8025EA30: table.sym("player_hang_8025EA30"),
    0x8025EB50: table.sym("player_hang_8025EB50"),
    0x8025ECFC: table.sym("player_hang_8025ECFC"),
    0x8025EED0: table.sym("player_hang_8025EED0"),
    0x8025EF58: table.sym("player_hang_8025EF58"),
    0x8025F0B4: table.sym("player_hang_8025F0B4"),
    0x8025F1E4: table.sym("player_hang_8025F1E4"),
    0x8025F384: table.sym("player_hang_8025F384"),
    0x8025F4B4: table.sym("player_hang_8025F4B4"),
    0x8025F560: table.sym("player_hang_8025F560"),
    0x8025F644: table.sym("player_hang_8025F644"),
    0x8025F6C0: table.sym("player_hang_8025F6C0"),
    0x8025F970: table.sym("player_hang_8025F970"),
    0x8025FA64: table.sym("player_hang_8025FA64"),
    0x8025FAE8: table.sym("player_hang_8025FAE8"),
    0x8025FB90: table.sym("player_hang_8025FB90"),
    0x8025FC6C: table.sym("player_hang_8025FC6C"),
    0x80260154: table.sym("player_hang_80260154"),
    0x80260568: table.sym("player_hang_80260568"),
    0x802605D0: table.sym("player_hang_main", table.GLOBL),

    # src/player_stop.S
    0x802608B0: table.sym("player_stop_802608B0"),
    0x80260AAC: table.sym("player_stop_80260AAC"),
    0x80260CB4: table.sym("player_stop_80260CB4"),
    0x80260F94: table.sym("player_stop_80260F94"),
    0x80261000: table.sym("player_stop_80261000"),
    0x80261268: table.sym("player_stop_80261268"),
    0x802614FC: table.sym("player_stop_802614FC"),
    0x8026168C: table.sym("player_stop_8026168C"),
    0x802618D8: table.sym("player_stop_802618D8"),
    0x802619D0: table.sym("player_stop_802619D0"),
    0x80261AD0: table.sym("player_stop_80261AD0"),
    0x80261BF8: table.sym("player_stop_80261BF8"),
    0x80261CEC: table.sym("player_stop_80261CEC"),
    0x80261DB4: table.sym("player_stop_80261DB4"),
    0x80261F70: table.sym("player_stop_80261F70"),
    0x80262080: table.sym("player_stop_80262080"),
    0x8026217C: table.sym("player_stop_8026217C"),
    0x802621DC: table.sym("player_stop_802621DC"),
    0x802622DC: table.sym("player_stop_802622DC"),
    0x80262398: table.sym("player_stop_80262398"),
    0x80262490: table.sym("player_stop_80262490"),
    0x80262530: table.sym("player_stop_80262530"),
    0x80262650: table.sym("player_stop_80262650"),
    0x80262770: table.sym("player_stop_80262770"),
    0x80262890: table.sym("player_stop_80262890"),
    0x80262980: table.sym("player_stop_80262980"),
    0x80262BC4: table.sym("player_stop_80262BC4"),
    0x80262C34: table.sym("player_stop_80262C34"),
    0x80262D68: table.sym("player_stop_80262D68"),
    0x80262DC4: table.sym("player_stop_80262DC4"),
    0x80262E20: table.sym("player_stop_80262E20"),
    0x80262E94: table.sym("player_stop_80262E94"),
    0x80262EF0: table.sym("player_stop_80262EF0"),
    0x80262F50: table.sym("player_stop_80262F50"),
    0x80262FEC: table.sym("player_stop_80262FEC"),
    0x8026305C: table.sym("player_stop_8026305C"),
    0x802630F8: table.sym("player_stop_802630F8"),
    0x802631F0: table.sym("player_stop_802631F0"),
    0x802632E8: table.sym("player_stop_802632E8"),
    0x802633B4: table.sym("player_stop_802633B4"),
    0x8026350C: table.sym("player_stop_8026350C"),
    0x802635E8: table.sym("player_stop_802635E8"),
    0x80263784: table.sym("player_stop_80263784"),
    0x80263898: table.sym("player_stop_main", table.GLOBL),

    # src/player_ground.S
    0x80263E60: table.sym("player_ground_80263E60"),
    0x80263EE4: table.sym("player_ground_80263EE4", table.GLOBL),
    0x80264024: table.sym("player_ground_80264024"),
    0x8026409C: table.sym("player_ground_8026409C"),
    0x802640FC: table.sym("player_ground_802640FC"),
    0x802642B4: table.sym("player_ground_802642B4"),
    0x80264340: table.sym("player_ground_80264340"),
    0x8026440C: table.sym("player_ground_8026440C"),
    0x80264740: table.sym("player_ground_80264740"),
    0x80264B54: table.sym("player_ground_80264B54"),
    0x80264D80: table.sym("player_ground_80264D80"),
    0x80264E18: table.sym("player_ground_80264E18"),
    0x80265080: table.sym("player_ground_80265080"),
    0x802651B0: table.sym("player_ground_802651B0"),
    0x80265244: table.sym("player_ground_80265244"),
    0x80265458: table.sym("player_ground_80265458"),
    0x80265514: table.sym("player_ground_80265514"),
    0x80265558: table.sym("player_ground_80265558"),
    0x80265620: table.sym("player_ground_80265620"),
    0x80265700: table.sym("player_ground_80265700"),
    0x80265B1C: table.sym("player_ground_80265B1C"),
    0x80265D90: table.sym("player_ground_80265D90"),
    0x80265DF8: table.sym("player_ground_80265DF8"),
    0x80266038: table.sym("player_ground_80266038"),
    0x802661CC: table.sym("player_ground_802661CC"),
    0x80266354: table.sym("player_ground_80266354"),
    0x802665B4: table.sym("player_ground_802665B4"),
    0x80266734: table.sym("player_ground_80266734"),
    0x8026699C: table.sym("player_ground_8026699C"),
    0x80266AF8: table.sym("player_ground_80266AF8"),
    0x80266D4C: table.sym("player_ground_80266D4C"),
    0x80266E48: table.sym("player_ground_80266E48"),
    0x80266FC8: table.sym("player_ground_80266FC8"),
    0x80267240: table.sym("player_ground_80267240"),
    0x80267504: table.sym("player_ground_80267504"),
    0x80267728: table.sym("player_ground_80267728"),
    0x8026795C: table.sym("player_ground_8026795C"),
    0x80267C24: table.sym("player_ground_80267C24"),
    0x80267CE4: table.sym("player_ground_80267CE4"),
    0x80267FA4: table.sym("player_ground_80267FA4"),
    0x80268074: table.sym("player_ground_80268074"),
    0x802680D4: table.sym("player_ground_802680D4"),
    0x80268168: table.sym("player_ground_80268168"),
    0x80268338: table.sym("player_ground_80268338"),
    0x802684AC: table.sym("player_ground_802684AC"),
    0x802685C0: table.sym("player_ground_802685C0"),
    0x80268608: table.sym("player_ground_80268608"),
    0x80268684: table.sym("player_ground_80268684"),
    0x802687B8: table.sym("player_ground_802687B8"),
    0x802689F8: table.sym("player_ground_802689F8"),
    0x80268ADC: table.sym("player_ground_80268ADC"),
    0x80268B64: table.sym("player_ground_80268B64"),
    0x80268BB0: table.sym("player_ground_80268BB0"),
    0x80268BFC: table.sym("player_ground_80268BFC"),
    0x80268C48: table.sym("player_ground_80268C48"),
    0x80268C94: table.sym("player_ground_80268C94"),
    0x80268D04: table.sym("player_ground_80268D04"),
    0x80268DCC: table.sym("player_ground_80268DCC"),
    0x80268F78: table.sym("player_ground_80268F78"),
    0x80269108: table.sym("player_ground_80269108"),
    0x80269170: table.sym("player_ground_80269170"),
    0x802691D8: table.sym("player_ground_802691D8"),
    0x80269264: table.sym("player_ground_80269264"),
    0x80269300: table.sym("player_ground_80269300"),
    0x8026939C: table.sym("player_ground_8026939C"),
    0x8026947C: table.sym("player_ground_8026947C"),
    0x802694E4: table.sym("player_ground_802694E4"),
    0x80269588: table.sym("player_ground_80269588"),
    0x80269640: table.sym("player_ground_80269640"),
    0x80269788: table.sym("player_ground_80269788"),
    0x802697DC: table.sym("player_ground_802697DC"),
    0x80269830: table.sym("player_ground_80269830"),
    0x80269954: table.sym("player_ground_main", table.GLOBL),

    # src/player_air.S
    0x80269F40: table.sym("player_air_80269F40"),
    0x80269FC0: table.sym("player_air_80269FC0"),
    0x8026A090: table.sym("player_air_8026A090"),
    0x8026A12C: table.sym("player_air_8026A12C"),
    0x8026A224: table.sym("player_air_8026A224"),
    0x8026A400: table.sym("player_air_8026A400"),
    0x8026A494: table.sym("player_air_8026A494"),
    0x8026A598: table.sym("player_air_8026A598"),
    0x8026A62C: table.sym("player_air_8026A62C"),
    0x8026A818: table.sym("player_air_8026A818"),
    0x8026AA48: table.sym("player_air_8026AA48"),
    0x8026ACD8: table.sym("player_air_8026ACD8"),
    0x8026AE5C: table.sym("player_air_8026AE5C"),
    0x8026B004: table.sym("player_air_8026B004"),
    0x8026B17C: table.sym("player_air_8026B17C"),
    0x8026B444: table.sym("player_air_8026B444"),
    0x8026B6A0: table.sym("player_air_8026B6A0"),
    0x8026B740: table.sym("player_air_8026B740"),
    0x8026B814: table.sym("player_air_8026B814"),
    0x8026B90C: table.sym("player_air_8026B90C"),
    0x8026B9AC: table.sym("player_air_8026B9AC"),
    0x8026BAB8: table.sym("player_air_8026BAB8"),
    0x8026BBB4: table.sym("player_air_8026BBB4"),
    0x8026BCC0: table.sym("player_air_8026BCC0"),
    0x8026BDCC: table.sym("player_air_8026BDCC"),
    0x8026BE78: table.sym("player_air_8026BE78"),
    0x8026BF40: table.sym("player_air_8026BF40"),
    0x8026C034: table.sym("player_air_8026C034"),
    0x8026C1E0: table.sym("player_air_8026C1E0"),
    0x8026C4B8: table.sym("player_air_8026C4B8"),
    0x8026C5D0: table.sym("player_air_8026C5D0"),
    0x8026C738: table.sym("player_air_8026C738"),
    0x8026C880: table.sym("player_air_8026C880"),
    0x8026C9FC: table.sym("player_air_8026C9FC"),
    0x8026CD0C: table.sym("player_air_8026CD0C"),
    0x8026CE50: table.sym("player_air_8026CE50"),
    0x8026CF28: table.sym("player_air_8026CF28"),
    0x8026D1B0: table.sym("player_air_8026D1B0"),
    0x8026D33C: table.sym("player_air_8026D33C"),
    0x8026D3C8: table.sym("player_air_8026D3C8"),
    0x8026D43C: table.sym("player_air_8026D43C"),
    0x8026D4B0: table.sym("player_air_8026D4B0"),
    0x8026D508: table.sym("player_air_8026D508"),
    0x8026D560: table.sym("player_air_8026D560"),
    0x8026D608: table.sym("player_air_8026D608"),
    0x8026D6FC: table.sym("player_air_8026D6FC"),
    0x8026D770: table.sym("player_air_8026D770"),
    0x8026D988: table.sym("player_air_8026D988"),
    0x8026DB54: table.sym("player_air_8026DB54"),
    0x8026DCF4: table.sym("player_air_8026DCF4"),
    0x8026DE98: table.sym("player_air_8026DE98"),
    0x8026E088: table.sym("player_air_8026E088"),
    0x8026E2B4: table.sym("player_air_8026E2B4"),
    0x8026E59C: table.sym("player_air_8026E59C"),
    0x8026E810: table.sym("player_air_8026E810"),
    0x8026E968: table.sym("player_air_8026E968"),
    0x8026EC00: table.sym("player_air_8026EC00"),
    0x8026F158: table.sym("player_air_8026F158"),
    0x8026F2EC: table.sym("player_air_8026F2EC"),
    0x8026F614: table.sym("player_air_8026F614"),
    0x8026F660: table.sym("player_air_8026F660"),
    0x8026F840: table.sym("player_air_8026F840"),
    0x8026FA18: table.sym("player_air_8026FA18"),
    0x8026FB04: table.sym("player_air_main", table.GLOBL),

    # src/player_water.S
    0x80270110: table.sym("player_water_80270110"),
    0x802701CC: table.sym("player_water_802701CC"),
    0x80270234: table.sym("player_water_80270234"),
    0x80270304: table.sym("player_water_80270304"),
    0x80270500: table.sym("player_water_80270500"),
    0x80270918: table.sym("player_water_80270918"),
    0x80270A74: table.sym("player_water_80270A74"),
    0x80270B4C: table.sym("player_water_80270B4C"),
    0x80270C94: table.sym("player_water_80270C94"),
    0x80270E40: table.sym("player_water_80270E40"),
    0x80270FD8: table.sym("player_water_80270FD8"),
    0x802710C4: table.sym("player_water_802710C4"),
    0x802711D4: table.sym("player_water_802711D4"),
    0x802712C0: table.sym("player_water_802712C0"),
    0x802713BC: table.sym("player_water_802713BC"),
    0x802714A8: table.sym("player_water_802714A8"),
    0x802715EC: table.sym("player_water_802715EC"),
    0x8027163C: table.sym("player_water_8027163C"),
    0x80271704: table.sym("player_water_80271704"),
    0x80271918: table.sym("player_water_80271918"),
    0x8027197C: table.sym("player_water_8027197C"),
    0x80271AA0: table.sym("player_water_80271AA0"),
    0x80271D04: table.sym("player_water_80271D04"),
    0x80271EB4: table.sym("player_water_80271EB4"),
    0x8027202C: table.sym("player_water_8027202C"),
    0x8027226C: table.sym("player_water_8027226C"),
    0x802723F0: table.sym("player_water_802723F0"),
    0x80272548: table.sym("player_water_80272548"),
    0x8027267C: table.sym("player_water_8027267C"),
    0x80272778: table.sym("player_water_80272778"),
    0x80272870: table.sym("player_water_80272870"),
    0x80272A60: table.sym("player_water_80272A60"),
    0x80272B1C: table.sym("player_water_80272B1C"),
    0x80272B64: table.sym("player_water_80272B64"),
    0x80272BAC: table.sym("player_water_80272BAC"),
    0x80272CBC: table.sym("player_water_80272CBC"),
    0x80272DC0: table.sym("player_water_80272DC0"),
    0x80272E3C: table.sym("player_water_80272E3C"),
    0x80273160: table.sym("player_water_80273160"),
    0x80273518: table.sym("player_water_80273518"),
    0x802735A4: table.sym("player_water_802735A4"),
    0x80273618: table.sym("player_water_80273618"),
    0x802737F4: table.sym("player_water_802737F4"),
    0x80273A2C: table.sym("player_water_80273A2C"),
    0x80273BD4: table.sym("player_water_80273BD4"),
    0x80273CD0: table.sym("player_water_80273CD0"),
    0x80273E74: table.sym("player_water_80273E74"),
    0x80274030: table.sym("player_water_80274030"),
    0x80274134: table.sym("player_water_80274134"),
    0x80274268: table.sym("player_water_80274268"),
    0x80274384: table.sym("player_water_80274384"),
    0x802744AC: table.sym("player_water_802744AC"),
    0x80274580: table.sym("player_water_80274580"),
    0x80274688: table.sym("player_water_80274688"),
    0x8027475C: table.sym("player_water_8027475C"),
    0x80274864: table.sym("player_water_80274864"),
    0x8027499C: table.sym("player_water_main", table.GLOBL),

    # src/player_grab.S
    0x80274EB0: table.sym("player_grab_80274EB0"),
    0x80274F10: table.sym("player_grab_80274F10", table.GLOBL),
    0x80275328: table.sym("player_grab_80275328"),
    0x8027546C: table.sym("player_grab_8027546C"),
    0x802755FC: table.sym("player_grab_802755FC"),
    0x802756C8: table.sym("player_grab_802756C8"),
    0x80275794: table.sym("player_grab_80275794"),
    0x802758C0: table.sym("player_grab_802758C0"),
    0x802759B4: table.sym("player_grab_802759B4"),
    0x80275A80: table.sym("player_grab_80275A80"),
    0x80275B34: table.sym("player_grab_80275B34"),
    0x80275E78: table.sym("player_grab_80275E78"),
    0x80275F0C: table.sym("player_grab_80275F0C"),
    0x80275FE0: table.sym("player_grab_main", table.GLOBL),

    # src/player_gfx.S
    0x802761D0: table.sym("player_gfx_802761D0", table.GLOBL), # g callback
    0x802763D4: table.sym("player_gfx_802763D4", table.GLOBL), # g callback
    0x802764B0: table.sym("player_gfx_802764B0", table.GLOBL), # g callback
    0x8027657C: table.sym("player_gfx_8027657C"),
    0x802765FC: table.sym("player_gfx_802765FC"),
    0x802766B4: table.sym("player_gfx_802766B4"),
    0x802767B8: table.sym("player_gfx_802767B8"),
    0x80276804: table.sym("player_gfx_80276804"),
    0x8027684C: table.sym("player_gfx_8027684C", table.GLOBL), # o callback
    0x80276910: table.sym("player_gfx_80276910", table.GLOBL), # o callback
    0x80276AA0: table.sym("player_gfx_80276AA0"),
    0x80276BB8: table.sym("player_gfx_80276BB8", table.GLOBL), # o callback
    0x80276CCC: table.sym("player_gfx_80276CCC", table.GLOBL), # o callback
    0x80276F90: table.sym("player_gfx_80276F90"),
    0x802770A4: table.sym("g_player_alpha",         table.GLOBL), # g callback
    0x80277150: table.sym("g_player_select_lod",    table.GLOBL), # g callback
    0x802771BC: table.sym("g_player_select_eye",    table.GLOBL), # g callback
    0x80277294: table.sym("g_player_rot_torso",     table.GLOBL), # g callback
    0x802773A4: table.sym("g_player_rot_head",      table.GLOBL), # g callback
    0x802774F4: table.sym("g_player_select_glove",  table.GLOBL), # g callback
    0x802775CC: table.sym("g_player_scale",         table.GLOBL), # g callback
    0x802776D8: table.sym("g_player_select_cap",    table.GLOBL), # g callback
    0x80277740: table.sym("g_player_select_head",   table.GLOBL), # g callback
    0x80277824: table.sym("g_player_rot_wing",      table.GLOBL), # g callback
    0x8027795C: table.sym("g_player_hand",          table.GLOBL), # g callback
    0x80277B14: table.sym("g_inside_mirror",        table.GLOBL), # g callback
    0x80277D6C: table.sym("g_player_mirror",        table.GLOBL), # g callback

    # src/memory.S
    0x80277EE0: table.sym("segment_set", table.GLOBL),
    0x80277F20: table.sym("segment_get"), # unused
    0x80277F50: table.sym("segment_to_virtual", table.GLOBL),
    0x80277FA8: table.sym("virtual_to_segment", table.GLOBL),
    0x80277FF0: table.sym("segment_draw", table.GLOBL),
    0x80278074: table.sym("mem_init", table.GLOBL),
    0x80278120: table.sym("mem_alloc", table.GLOBL),
    0x80278238: table.sym("mem_free", table.GLOBL),
    0x80278358: table.sym("mem_resize"),
    0x802783C8: table.sym("mem_size", table.GLOBL),
    0x802783E8: table.sym("mem_push", table.GLOBL),
    0x80278498: table.sym("mem_pull", table.GLOBL),
    0x80278504: table.sym("mem_dma"),
    0x80278610: table.sym("mem_load"),
    0x8027868C: table.sym("mem_load_data", table.GLOBL),
    0x802786F0: table.sym("mem_load_code", table.GLOBL),
    0x802787D8: table.sym("mem_load_szp", table.GLOBL),
    0x802788B4: table.sym("mem_load_texture", table.GLOBL),
    0x80278974: table.sym("mem_load_main2", table.GLOBL),
    0x80278A14: table.sym("arena_init", table.GLOBL),
    0x80278AB8: table.sym("arena_alloc", table.GLOBL),
    0x80278B28: table.sym("arena_resize", table.GLOBL),
    0x80278B98: table.sym("heap_init", table.GLOBL),
    0x80278C58: table.sym("heap_alloc", table.GLOBL),
    0x80278D74: table.sym("heap_free", table.GLOBL),
    0x80278F2C: table.sym("gfx_alloc", table.GLOBL),
    0x80278FA0: table.sym("ft_init_table"),
    0x80279028: table.sym("ft_init", table.GLOBL),
    0x80279084: table.sym("ft_read", table.GLOBL),

    # src/save.S
    0x80279160: table.sym("save_80279160"),
    0x80279174: table.sym("save_80279174"),
    0x80279218: table.sym("save_80279218"),
    0x802792C0: table.sym("save_802792C0"),
    0x80279314: table.sym("save_80279314"),
    0x8027939C: table.sym("save_8027939C"),
    0x802793FC: table.sym("save_802793FC"),
    0x802794A0: table.sym("save_802794A0"),
    0x8027951C: table.sym("save_8027951C"),
    0x802795A0: table.sym("save_802795A0"),
    0x802795D4: table.sym("save_802795D4"),
    0x80279650: table.sym("save_80279650"),
    0x80279700: table.sym("save_80279700"),
    0x80279748: table.sym("save_80279748"),
    0x80279840: table.sym("save_80279840", table.GLOBL),
    0x802798FC: table.sym("save_802798FC", table.GLOBL),
    0x80279960: table.sym("save_80279960", table.GLOBL),
    0x802799DC: table.sym("save_802799DC", table.GLOBL),
    0x80279BC8: table.sym("save_80279BC8", table.GLOBL),
    0x80279C44: table.sym("save_80279C44", table.GLOBL),
    0x80279E44: table.sym("save_80279E44", table.GLOBL),
    0x80279E80: table.sym("save_80279E80", table.GLOBL),
    0x80279F80: table.sym("save_80279F80", table.GLOBL),
    0x8027A010: table.sym("save_8027A010", table.GLOBL),
    0x8027A0A8: table.sym("save_8027A0A8", table.GLOBL),
    0x8027A0F4: table.sym("save_8027A0F4", table.GLOBL),
    0x8027A16C: table.sym("save_8027A16C", table.GLOBL),
    0x8027A1C8: table.sym("save_8027A1C8", table.GLOBL),
    0x8027A23C: table.sym("save_8027A23C"),
    0x8027A310: table.sym("save_8027A310", table.GLOBL),
    0x8027A340: table.sym("save_8027A340", table.GLOBL),
    0x8027A390: table.sym("save_8027A390", table.GLOBL),
    0x8027A418: table.sym("save_8027A418", table.GLOBL),
    0x8027A4AC: table.sym("save_8027A4AC", table.GLOBL),
    0x8027A564: table.sym("save_8027A564", table.GLOBL),
    0x8027A5B4: table.sym("save_8027A5B4", table.GLOBL),
    0x8027A5D4: table.sym("save_8027A5D4", table.GLOBL),
    0x8027A698: table.sym("save_8027A698", table.GLOBL),
    0x8027A6B0: table.sym("save_8027A6B0", table.GLOBL),
    0x8027A718: table.sym("save_8027A718", table.GLOBL),

    # src/world.S
    0x8027A7D0: table.sym("world_8027A7D0", table.GLOBL),
    0x8027A83C: table.sym("world_8027A83C"),
    0x8027A8B0: table.sym("world_8027A8B0", table.GLOBL),
    0x8027A93C: table.sym("world_8027A93C", table.GLOBL),
    0x8027A9C8: table.sym("world_8027A9C8", table.GLOBL),
    0x8027AA28: table.sym("world_8027AA28"),
    0x8027AA74: table.sym("world_8027AA74"),
    0x8027AB04: table.sym("world_8027AB04", table.GLOBL),
    0x8027AD74: table.sym("world_8027AD74", table.GLOBL),
    0x8027AE44: table.sym("world_8027AE44", table.GLOBL),
    0x8027AF48: table.sym("world_8027AF48", table.GLOBL),
    0x8027AFBC: table.sym("world_8027AFBC", table.GLOBL),
    0x8027B038: table.sym("world_8027B038", table.GLOBL),
    0x8027B0C0: table.sym("world_8027B0C0", table.GLOBL),
    0x8027B164: table.sym("world_8027B164", table.GLOBL),
    0x8027B1A0: table.sym("world_8027B1A0", table.GLOBL),
    0x8027B35C: table.sym("world_8027B35C", table.GLOBL),
    0x8027B3B4: table.sym("world_draw", table.GLOBL),

    # src/g_draw.S
    0x8027B6C0: table.sym("g_draw_8027B6C0"),
    0x8027B904: table.sym("g_draw_8027B904"),
    0x8027BA00: table.sym("g_draw_8027BA00"),
    0x8027BA98: table.sym("g_draw_8027BA98"),
    0x8027BC74: table.sym("g_draw_8027BC74"),
    0x8027BDF0: table.sym("g_draw_8027BDF0"),
    0x8027BE84: table.sym("g_draw_8027BE84"),
    0x8027BF58: table.sym("g_draw_8027BF58"),
    0x8027C114: table.sym("g_draw_8027C114"),
    0x8027C238: table.sym("g_draw_8027C238"),
    0x8027C35C: table.sym("g_draw_8027C35C"),
    0x8027C474: table.sym("g_draw_8027C474"),
    0x8027C594: table.sym("g_draw_8027C594"),
    0x8027C73C: table.sym("g_draw_8027C73C"),
    0x8027C7A4: table.sym("g_draw_8027C7A4"),
    0x8027C858: table.sym("g_draw_8027C858"),
    0x8027CA70: table.sym("g_draw_8027CA70"),
    0x8027CF38: table.sym("g_draw_8027CF38"),
    0x8027D0B8: table.sym("g_draw_8027D0B8"),
    0x8027D518: table.sym("g_draw_8027D518"),
    0x8027D6FC: table.sym("g_draw_8027D6FC"),
    0x8027DA10: table.sym("g_draw_8027DA10"),
    0x8027DA84: table.sym("g_draw_8027DA84"),
    0x8027DE68: table.sym("g_draw_8027DE68"),
    0x8027DEA8: table.sym("g_draw_8027DEA8"),
    0x8027E130: table.sym("g_draw_world", table.GLOBL),

    # src/time.S
    0x8027E3E0: table.sym("time_8027E3E0", table.GLOBL),
    0x8027E490: table.sym("time_8027E490", table.GLOBL),
    0x8027E520: table.sym("time_8027E520", table.GLOBL),
    0x8027E5CC: table.sym("time_8027E5CC", table.GLOBL),
    0x8027E65C: table.sym("time_8027E65C"),
    0x8027E958: table.sym("time_8027E958"),
    0x8027EBCC: table.sym("time_8027EBCC"),
    0x8027EEAC: table.sym("time_8027EEAC"),
    0x8027F460: table.sym("time_draw", table.GLOBL),

    # src/szp.S
    0x8027F4E0: table.sym_fnc("szp_decode", arg=(
        "const u8 *src",
        "u8 *dst",
    ), flag=table.GLOBL),

    # src/camera.S
    0x8027F590: table.sym("camera_8027F590", table.GLOBL),
    0x8027F8B8: table.sym("camera_8027F8B8", table.GLOBL),
    0x8027F9F0: table.sym("camera_8027F9F0", table.GLOBL),
    0x8027FB74: table.sym("camera_8027FB74"), # unused
    0x8027FC18: table.sym("camera_8027FC18"),
    0x8027FE20: table.sym("camera_8027FE20"),
    0x8027FF00: table.sym("camera_8027FF00"), # unused
    0x8027FFF8: table.sym("camera_8027FFF8"),
    0x80280368: table.sym("camera_80280368"),
    0x802804F4: table.sym("camera_802804F4"),
    0x802806A4: table.sym("camera_802806A4"),
    0x80280810: table.sym("camera_80280810", table.GLOBL), # data
    0x80280970: table.sym("camera_80280970", table.GLOBL), # data
    0x80280B00: table.sym("camera_80280B00"),
    0x80281188: table.sym("camera_80281188"),
    0x802813BC: table.sym("camera_802813BC"),
    0x802813EC: table.sym("camera_802813EC"),
    0x8028146C: table.sym("camera_8028146C"),
    0x80281588: table.sym("camera_80281588"),
    0x802816A0: table.sym("camera_802816A0", table.GLOBL), # data
    0x802817FC: table.sym("camera_802817FC"),
    0x80281904: table.sym("camera_80281904", table.GLOBL), # data
    0x80282280: table.sym("camera_80282280", table.GLOBL), # data
    0x802826A0: table.sym("camera_802826A0", table.GLOBL), # data
    0x80282C0C: table.sym("camera_80282C0C", table.GLOBL), # data
    0x80282C28: table.sym("camera_80282C28"), # unused
    0x80282C3C: table.sym("camera_80282C3C"),
    0x80282C7C: table.sym("camera_80282C7C"),
    0x80282CE0: table.sym("camera_80282CE0"),
    0x80282D78: table.sym("camera_80282D78", table.GLOBL), # data
    0x80283340: table.sym("camera_80283340"),
    0x80283578: table.sym("camera_80283578"),
    0x802839E4: table.sym("camera_802839E4"),
    0x80283A18: table.sym("camera_80283A18", table.GLOBL), # data
    0x80283A34: table.sym("camera_80283A34"),
    0x80283A68: table.sym("camera_80283A68", table.GLOBL), # data
    0x80283AF8: table.sym("camera_80283AF8"),
    0x80284CB8: table.sym("camera_80284CB8"),
    0x80284CFC: table.sym("camera_80284CFC"),
    0x80284D38: table.sym("camera_80284D38"),
    0x80284D74: table.sym("camera_80284D74", table.GLOBL), # data
    0x802850AC: table.sym("camera_802850AC"),
    0x802850EC: table.sym("camera_802850EC", table.GLOBL), # data
    0x8028517C: table.sym("camera_8028517C"), # unused
    0x802851DC: table.sym("camera_802851DC"),
    0x8028526C: table.sym("camera_8028526C"),
    0x802852F4: table.sym("camera_802852F4"),
    0x80285370: table.sym("camera_80285370"),
    0x80285808: table.sym("camera_80285808", table.GLOBL), # data
    0x802858A4: table.sym("camera_802858A4"),
    0x80285A2C: table.sym("camera_80285A2C"),
    0x80285D20: table.sym("camera_80285D20"),
    0x80285ED8: table.sym("camera_80285ED8", table.GLOBL), # data
    0x80285F60: table.sym("camera_80285F60"),
    0x8028603C: table.sym("camera_8028603C"),
    0x80286088: table.sym("camera_80286088"),
    0x80286188: table.sym("camera_80286188", table.GLOBL),
    0x80286420: table.sym("camera_80286420"),
    0x802868F8: table.sym("camera_802868F8", table.GLOBL),
    0x80286F68: table.sym("camera_80286F68", table.GLOBL),
    0x8028724C: table.sym("camera_8028724C"),
    0x802879EC: table.sym("camera_802879EC"),
    0x80287BC4: table.sym("camera_80287BC4", table.GLOBL),
    0x80287BE0: table.sym("camera_80287BE0"),
    0x80287CB8: table.sym("camera_80287CB8"),
    0x80287D30: table.sym("camera_80287D30", table.GLOBL), # g callback
    0x80287DC0: table.sym("camera_80287DC0"),
    0x80287DD4: table.sym("camera_80287DD4"),
    0x80287DE8: table.sym("camera_80287DE8"),
    0x80287E28: table.sym("camera_80287E28"),
    0x80287E50: table.sym("camera_80287E50"),
    0x80287E78: table.sym("camera_80287E78"), # unused
    0x80287EA0: table.sym("camera_80287EA0"),
    0x802882E4: table.sym("camera_802882E4"),
    0x80288624: table.sym("camera_80288624", table.GLOBL),
    0x80288718: table.sym("camera_80288718"),
    0x80288888: table.sym("camera_80288888"),
    0x802889B0: table.sym("camera_802889B0"),
    0x80288CE4: table.sym("camera_80288CE4"),
    0x80288E68: table.sym("camera_80288E68"),
    0x80288F5C: table.sym("camera_80288F5C"),
    0x80289198: table.sym("camera_80289198"),
    0x80289214: table.sym("camera_80289214"),
    0x802892D8: table.sym("camera_802892D8"),
    0x8028935C: table.sym("camera_8028935C"),
    0x802893F4: table.sym("camera_802893F4"),
    0x80289488: table.sym("camera_80289488"),
    0x802894B4: table.sym("camera_802894B4"),
    0x8028956C: table.sym("camera_8028956C"),
    0x80289610: table.sym("camera_80289610"),
    0x80289684: table.sym("camera_80289684"),
    0x802896F8: table.sym("camera_802896F8"),
    0x8028976C: table.sym("camera_8028976C"),
    0x8028984C: table.sym("camera_8028984C"),
    0x8028993C: table.sym("camera_8028993C"),
    0x802899CC: table.sym("camera_802899CC"),
    0x80289B0C: table.sym("camera_80289B0C", table.GLOBL),
    0x80289C00: table.sym("camera_80289C00"),
    0x80289D20: table.sym("camera_80289D20"),
    0x80289F88: table.sym("camera_80289F88"),
    0x8028A080: table.sym("camera_8028A080"),
    0x8028A0F4: table.sym("camera_8028A0F4"),
    0x8028A4EC: table.sym("camera_8028A4EC"),
    0x8028A6BC: table.sym("camera_8028A6BC"),
    0x8028A7EC: table.sym("camera_8028A7EC"),
    0x8028A834: table.sym("camera_8028A834"),
    0x8028A8E8: table.sym("camera_8028A8E8"),
    0x8028AA28: table.sym("camera_8028AA28"),
    0x8028AAD8: table.sym("camera_8028AAD8"),
    0x8028AB60: table.sym("camera_8028AB60"),
    0x8028AC28: table.sym("camera_8028AC28"),
    0x8028ACCC: table.sym("camera_8028ACCC"),
    0x8028AD4C: table.sym("camera_8028AD4C"),
    0x8028AE1C: table.sym("camera_8028AE1C"),
    0x8028AEF0: table.sym("camera_8028AEF0"),
    0x8028AF4C: table.sym("camera_8028AF4C"),
    0x8028B00C: table.sym("camera_8028B00C"),
    0x8028B068: table.sym("camera_8028B068"),
    0x8028B11C: table.sym("camera_8028B11C"), # unused
    0x8028B1D0: table.sym("camera_8028B1D0"),
    0x8028B218: table.sym("camera_8028B218"),
    0x8028B32C: table.sym("camera_8028B32C"),
    0x8028B438: table.sym("camera_8028B438"),
    0x8028B50C: table.sym("camera_8028B50C"),
    0x8028B724: table.sym("camera_8028B724"),
    0x8028B754: table.sym("camera_8028B754"),
    0x8028B784: table.sym("camera_8028B784"),
    0x8028B7C4: table.sym("camera_8028B7C4"),
    0x8028B804: table.sym("camera_8028B804"),
    0x8028B850: table.sym("camera_8028B850"),
    0x8028B884: table.sym("camera_8028B884"),
    0x8028B8B8: table.sym("camera_8028B8B8"),
    0x8028B8EC: table.sym("camera_8028B8EC"),
    0x8028B920: table.sym("camera_8028B920"),
    0x8028B954: table.sym("camera_8028B954"),
    0x8028B9C4: table.sym("camera_8028B9C4"),
    0x8028BD34: table.sym("camera_8028BD34", table.GLOBL),
    0x8028BD98: table.sym("camera_8028BD98"),
    0x8028C038: table.sym("camera_8028C038"),
    0x8028C13C: table.sym("camera_8028C13C"),
    0x8028C18C: table.sym("camera_8028C18C"),
    0x8028C26C: table.sym("camera_8028C26C"),
    0x8028C2C8: table.sym("camera_8028C2C8"),
    0x8028C7A0: table.sym("camera_8028C7A0", table.GLOBL),
    0x8028C8F0: table.sym("camera_8028C8F0"),
    0x8028C9AC: table.sym("camera_8028C9AC"), # unused
    0x8028C9CC: table.sym("camera_8028C9CC"),
    0x8028CB08: table.sym("camera_8028CB08"), # unused
    0x8028CBF0: table.sym("camera_8028CBF0"),
    0x8028CD94: table.sym("camera_8028CD94"),
    0x8028CDEC: table.sym("camera_8028CDEC"),
    0x8028CE24: table.sym("camera_8028CE24"),
    0x8028D41C: table.sym("camera_8028D41C"), # unused
    0x8028D44C: table.sym("camera_8028D44C"),
    0x8028D5AC: table.sym("camera_8028D5AC"),
    0x8028D5FC: table.sym("camera_8028D5FC"),
    0x8028D658: table.sym("camera_8028D658"),
    0x8028D698: table.sym("camera_8028D698"),
    0x8028D79C: table.sym("camera_8028D79C"),
    0x8028D888: table.sym("camera_8028D888"),
    0x8028D92C: table.sym("camera_8028D92C"),
    0x8028DA18: table.sym("camera_8028DA18", table.GLOBL), # data
    0x8028DA50: table.sym("camera_8028DA50", table.GLOBL), # data
    0x8028DAEC: table.sym("camera_8028DAEC", table.GLOBL), # data
    0x8028DB38: table.sym("camera_8028DB38", table.GLOBL), # data
    0x8028DBB4: table.sym("camera_8028DBB4", table.GLOBL), # data
    0x8028DBF4: table.sym("camera_8028DBF4", table.GLOBL), # data
    0x8028DC1C: table.sym("camera_8028DC1C", table.GLOBL), # data
    0x8028DC70: table.sym("camera_8028DC70", table.GLOBL), # data
    0x8028DCA4: table.sym("camera_8028DCA4"),
    0x8028DD48: table.sym("camera_8028DD48", table.GLOBL), # data
    0x8028DE2C: table.sym("camera_8028DE2C", table.GLOBL), # data
    0x8028DE5C: table.sym("camera_8028DE5C", table.GLOBL), # data
    0x8028DE90: table.sym("camera_8028DE90", table.GLOBL), # data
    0x8028DEC4: table.sym("camera_8028DEC4", table.GLOBL), # data
    0x8028DEF8: table.sym("camera_8028DEF8", table.GLOBL), # data
    0x8028DF24: table.sym("camera_8028DF24", table.GLOBL), # data
    0x8028DF6C: table.sym("camera_8028DF6C", table.GLOBL), # data
    0x8028DFB4: table.sym("camera_8028DFB4", table.GLOBL), # data
    0x8028DFE8: table.sym("camera_8028DFE8", table.GLOBL), # data
    0x8028E01C: table.sym("camera_8028E01C", table.GLOBL), # data
    0x8028E064: table.sym("camera_8028E064", table.GLOBL), # data
    0x8028E098: table.sym("camera_8028E098", table.GLOBL), # data
    0x8028E0EC: table.sym("camera_8028E0EC", table.GLOBL), # data
    0x8028E164: table.sym("camera_8028E164", table.GLOBL), # data
    0x8028E210: table.sym("camera_8028E210", table.GLOBL), # data
    0x8028E298: table.sym("camera_8028E298", table.GLOBL), # data
    0x8028E300: table.sym("camera_8028E300", table.GLOBL), # data
    0x8028E334: table.sym("camera_8028E334"), # unused
    0x8028E38C: table.sym("camera_8028E38C", table.GLOBL), # data
    0x8028E3B8: table.sym("camera_8028E3B8", table.GLOBL), # data
    0x8028E3F0: table.sym("camera_8028E3F0", table.GLOBL), # data
    0x8028E41C: table.sym("camera_8028E41C", table.GLOBL), # data
    0x8028E450: table.sym("camera_8028E450", table.GLOBL), # data
    0x8028E47C: table.sym("camera_8028E47C", table.GLOBL), # data
    0x8028E524: table.sym("camera_8028E524", table.GLOBL), # data
    0x8028E55C: table.sym("camera_8028E55C", table.GLOBL), # data
    0x8028E594: table.sym("camera_8028E594", table.GLOBL), # data
    0x8028E5CC: table.sym("camera_8028E5CC", table.GLOBL), # data
    0x8028E604: table.sym("camera_8028E604", table.GLOBL), # data
    0x8028E63C: table.sym("camera_8028E63C", table.GLOBL), # data
    0x8028E674: table.sym("camera_8028E674", table.GLOBL), # data
    0x8028E6C4: table.sym("camera_8028E6C4", table.GLOBL), # data
    0x8028E714: table.sym("camera_8028E714", table.GLOBL), # data
    0x8028E758: table.sym("camera_8028E758", table.GLOBL), # data
    0x8028E790: table.sym("camera_8028E790", table.GLOBL), # data
    0x8028E7C8: table.sym("camera_8028E7C8", table.GLOBL), # data
    0x8028E818: table.sym("camera_8028E818", table.GLOBL), # data
    0x8028E868: table.sym("camera_8028E868", table.GLOBL), # data
    0x8028E8A0: table.sym("camera_8028E8A0", table.GLOBL), # data
    0x8028E8CC: table.sym("camera_8028E8CC", table.GLOBL), # data
    0x8028E930: table.sym("camera_8028E930", table.GLOBL), # data
    0x8028E974: table.sym("camera_8028E974", table.GLOBL), # data
    0x8028E9A0: table.sym("camera_8028E9A0", table.GLOBL), # data
    0x8028E9D8: table.sym("camera_8028E9D8", table.GLOBL), # data
    0x8028EA28: table.sym("camera_8028EA28", table.GLOBL), # data
    0x8028EA60: table.sym("camera_8028EA60", table.GLOBL), # data
    0x8028EAB0: table.sym("camera_8028EAB0", table.GLOBL), # data
    0x8028EAE8: table.sym("camera_8028EAE8", table.GLOBL), # data
    0x8028EB38: table.sym("camera_8028EB38", table.GLOBL), # data
    0x8028EB88: table.sym("camera_8028EB88", table.GLOBL), # data
    0x8028EBC0: table.sym("camera_8028EBC0", table.GLOBL), # data
    0x8028EC04: table.sym("camera_8028EC04", table.GLOBL), # data
    0x8028EC2C: table.sym("camera_8028EC2C", table.GLOBL), # data
    0x8028EC58: table.sym("camera_8028EC58"),
    0x8028ED30: table.sym("camera_8028ED30"),
    0x8028ED98: table.sym("camera_8028ED98"),
    0x8028EEB0: table.sym("camera_8028EEB0"),
    0x8028F670: table.sym("camera_8028F670"),
    0x8028F914: table.sym("camera_8028F914"),
    0x8028FC9C: table.sym("camera_8028FC9C"),
    0x8028FE24: table.sym("camera_8028FE24"),
    0x8028FE58: table.sym("camera_8028FE58"),
    0x8028FE84: table.sym("camera_8028FE84"), # unused
    0x8028FF04: table.sym("camera_8028FF04", table.GLOBL),
    0x8028FFC8: table.sym("camera_8028FFC8", table.GLOBL),
    0x8029000C: table.sym("camera_8029000C", table.GLOBL),
    0x80290098: table.sym("camera_80290098"),
    0x802900E0: table.sym("camera_802900E0"),
    0x80290104: table.sym("camera_80290104"),
    0x80290168: table.sym("camera_80290168"),
    0x802901A4: table.sym("camera_802901A4"),
    0x802901FC: table.sym("camera_802901FC"),
    0x802903B8: table.sym("camera_802903B8"),
    0x8029040C: table.sym("camera_8029040C"), # unused
    0x80290440: table.sym("camera_80290440", table.GLOBL), # data
    0x80290474: table.sym("camera_80290474"), # unused
    0x802904A8: table.sym("camera_802904A8"),
    0x802904E4: table.sym("camera_802904E4"),
    0x8029051C: table.sym("camera_8029051C"),
    0x8029053C: table.sym("camera_8029053C"),
    0x80290784: table.sym("camera_80290784"),
    0x802907F4: table.sym("camera_802907F4"),
    0x80290864: table.sym("camera_80290864"),
    0x802908E8: table.sym("camera_802908E8"),
    0x80290938: table.sym("camera_80290938"), # unused
    0x80290984: table.sym("camera_80290984"), # unused
    0x802909D0: table.sym("camera_802909D0"),
    0x80290A5C: table.sym("camera_80290A5C"),
    0x80290A90: table.sym("camera_80290A90"), # unused
    0x80290ABC: table.sym("camera_80290ABC"),
    0x80290B54: table.sym("camera_80290B54"),
    0x80290BA4: table.sym("camera_80290BA4"),
    0x80290BD8: table.sym("camera_80290BD8"),
    0x80290C08: table.sym("camera_80290C08"), # unused
    0x80290C1C: table.sym("camera_80290C1C", table.GLOBL), # data
    0x80290C30: table.sym("camera_80290C30", table.GLOBL), # data
    0x80290C44: table.sym("camera_80290C44"),
    0x80290C9C: table.sym("camera_80290C9C"),
    0x80290D90: table.sym("camera_80290D90", table.GLOBL), # data
    0x80290E00: table.sym("camera_80290E00", table.GLOBL), # data
    0x80290E74: table.sym("camera_80290E74"),
    0x80290EB0: table.sym("camera_80290EB0"),
    0x80290F1C: table.sym("camera_80290F1C", table.GLOBL), # data
    0x80290F8C: table.sym("camera_80290F8C", table.GLOBL), # data
    0x80291074: table.sym("camera_80291074"),
    0x80291108: table.sym("camera_80291108", table.GLOBL), # data
    0x802911C8: table.sym("camera_802911C8"),
    0x80291208: table.sym("camera_80291208"),
    0x8029127C: table.sym("camera_8029127C"),
    0x802912B8: table.sym("camera_802912B8"),
    0x80291354: table.sym("camera_80291354", table.GLOBL), # data
    0x8029142C: table.sym("camera_8029142C", table.GLOBL), # data
    0x802914CC: table.sym("camera_802914CC"),
    0x80291514: table.sym("camera_80291514", table.GLOBL), # data
    0x802915D4: table.sym("camera_802915D4", table.GLOBL), # data
    0x80291654: table.sym("camera_80291654"),
    0x802916B8: table.sym("camera_802916B8"),
    0x80291774: table.sym("camera_80291774", table.GLOBL), # data
    0x802917E4: table.sym("camera_802917E4"),
    0x8029184C: table.sym("camera_8029184C"),
    0x80291870: table.sym("camera_80291870", table.GLOBL), # data
    0x80291924: table.sym("camera_80291924", table.GLOBL), # data
    0x80291964: table.sym("camera_80291964"),
    0x802919DC: table.sym("camera_802919DC"),
    0x80291AB4: table.sym("camera_80291AB4"),
    0x80291B18: table.sym("camera_80291B18"),
    0x80291B68: table.sym("camera_80291B68"),
    0x80291BF4: table.sym("camera_80291BF4"),
    0x80291C3C: table.sym("camera_80291C3C"),
    0x80291CD0: table.sym("camera_80291CD0", table.GLOBL), # data
    0x80291DB0: table.sym("camera_80291DB0"),
    0x80291E84: table.sym("camera_80291E84"),
    0x80291F18: table.sym("camera_80291F18"),
    0x80292038: table.sym("camera_80292038"),
    0x80292164: table.sym("camera_80292164", table.GLOBL), # data
    0x802921FC: table.sym("camera_802921FC"),
    0x8029228C: table.sym("camera_8029228C"),
    0x80292324: table.sym("camera_80292324"),
    0x80292370: table.sym("camera_80292370"),
    0x802923B8: table.sym("camera_802923B8"),
    0x80292400: table.sym("camera_80292400"), # unused
    0x80292414: table.sym("camera_80292414"),
    0x8029244C: table.sym("camera_8029244C"),
    0x80292484: table.sym("camera_80292484"),
    0x802924B8: table.sym("camera_802924B8", table.GLOBL), # data
    0x80292628: table.sym("camera_80292628"),
    0x802926DC: table.sym("camera_802926DC"),
    0x802927D0: table.sym("camera_802927D0"),
    0x80292868: table.sym("camera_80292868"),
    0x80292974: table.sym("camera_80292974"),
    0x80292A20: table.sym("camera_80292A20"),
    0x80292A4C: table.sym("camera_80292A4C"),
    0x80292A80: table.sym("camera_80292A80", table.GLOBL), # data
    0x80292C00: table.sym("camera_80292C00"),
    0x80292D80: table.sym("camera_80292D80"),
    0x80292E2C: table.sym("camera_80292E2C"),
    0x80292EC4: table.sym("camera_80292EC4"),
    0x80292F40: table.sym("camera_80292F40"),
    0x80292F98: table.sym("camera_80292F98"),
    0x80292FE4: table.sym("camera_80292FE4"),
    0x80293018: table.sym("camera_80293018", table.GLOBL), # data
    0x802930F0: table.sym("camera_802930F0"),
    0x80293164: table.sym("camera_80293164"),
    0x802931C0: table.sym("camera_802931C0"),
    0x80293220: table.sym("camera_80293220"),
    0x8029328C: table.sym("camera_8029328C"),
    0x802932F4: table.sym("camera_802932F4"),
    0x80293328: table.sym("camera_80293328"),
    0x80293354: table.sym("camera_80293354"),
    0x8029338C: table.sym("camera_8029338C", table.GLOBL), # data
    0x80293488: table.sym("camera_80293488"),
    0x802934B4: table.sym("camera_802934B4"),
    0x802934D8: table.sym("camera_802934D8"),
    0x80293548: table.sym("camera_80293548"),
    0x802935E0: table.sym("camera_802935E0"),
    0x80293624: table.sym("camera_80293624"),
    0x8029369C: table.sym("camera_8029369C"),
    0x802936DC: table.sym("camera_802936DC"),
    0x80293708: table.sym("camera_80293708"),
    0x80293734: table.sym("camera_80293734"),
    0x802937E8: table.sym("camera_802937E8"),
    0x8029386C: table.sym("camera_8029386C", table.GLOBL), # data
    0x802938C8: table.sym("camera_802938C8", table.GLOBL), # data
    0x80293944: table.sym("camera_80293944", table.GLOBL), # data
    0x80293ABC: table.sym("camera_80293ABC"),
    0x80293AE8: table.sym("camera_80293AE8"),
    0x80293B70: table.sym("camera_80293B70"),
    0x80293BF4: table.sym("camera_80293BF4"),
    0x80293C2C: table.sym("camera_80293C2C", table.GLOBL), # data
    0x80293CB0: table.sym("camera_80293CB0", table.GLOBL), # data
    0x80293D5C: table.sym("camera_80293D5C", table.GLOBL), # data
    0x80293D90: table.sym("camera_80293D90"),
    0x80293DD4: table.sym("camera_80293DD4"),
    0x80293E7C: table.sym("camera_80293E7C", table.GLOBL), # data
    0x80293ED8: table.sym("camera_80293ED8", table.GLOBL), # data
    0x80293F2C: table.sym("camera_80293F2C"),
    0x80293F70: table.sym("camera_80293F70", table.GLOBL), # data
    0x80293FCC: table.sym("camera_80293FCC"),
    0x80294024: table.sym("camera_80294024"),
    0x80294088: table.sym("camera_80294088"),
    0x802940CC: table.sym("camera_802940CC"),
    0x8029410C: table.sym("camera_8029410C"),
    0x802942CC: table.sym("camera_802942CC"),
    0x802942F0: table.sym("camera_802942F0", table.GLOBL), # data
    0x802943D4: table.sym("camera_802943D4", table.GLOBL), # data
    0x80294428: table.sym("camera_80294428"),
    0x80294718: table.sym("camera_80294718"),
    0x802947A4: table.sym("camera_802947A4"),
    0x8029480C: table.sym("camera_8029480C"),
    0x802948A0: table.sym("camera_802948A0"),
    0x80294A14: table.sym("camera_80294A14", table.GLOBL), # data
    0x80294A94: table.sym("camera_80294A94", table.GLOBL), # data
    0x80294AE8: table.sym("camera_80294AE8"),
    0x80294B78: table.sym("camera_80294B78"),
    0x80294BB4: table.sym("camera_80294BB4"),
    0x80294C28: table.sym("camera_80294C28"),
    0x80294C5C: table.sym("camera_80294C5C", table.GLOBL), # data
    0x80294CC4: table.sym("camera_80294CC4"),
    0x80294D48: table.sym("camera_80294D48"),
    0x80294D88: table.sym("camera_80294D88"), # unused
    0x80294DB4: table.sym("camera_80294DB4", table.GLOBL), # data
    0x80294E24: table.sym("camera_80294E24"),
    0x80294EA8: table.sym("camera_80294EA8"),
    0x80294EE8: table.sym("camera_80294EE8", table.GLOBL), # data
    0x80294F58: table.sym("camera_80294F58"),
    0x80294F94: table.sym("camera_80294F94"),
    0x80294FEC: table.sym("camera_80294FEC", table.GLOBL), # data
    0x802950B0: table.sym("camera_802950B0"),
    0x80295140: table.sym("camera_80295140"),
    0x802951F0: table.sym("camera_802951F0"),
    0x80295270: table.sym("camera_80295270", table.GLOBL), # data
    0x80295310: table.sym("camera_80295310"),
    0x802953DC: table.sym("camera_802953DC"),
    0x80295418: table.sym("camera_80295418", table.GLOBL), # data
    0x80295480: table.sym("camera_80295480"),
    0x802954EC: table.sym("camera_802954EC"),
    0x80295518: table.sym("camera_80295518"),
    0x80295580: table.sym("camera_80295580"),
    0x80295670: table.sym("camera_80295670"),
    0x80295740: table.sym("camera_80295740"),
    0x8029576C: table.sym("camera_8029576C"),
    0x802957C8: table.sym("camera_802957C8", table.GLOBL), # data
    0x80295894: table.sym("camera_80295894", table.GLOBL), # data
    0x802958D4: table.sym("camera_802958D4"),
    0x80295930: table.sym("camera_80295930", table.GLOBL), # data
    0x802959CC: table.sym("camera_802959CC"), # unused
    0x80295A58: table.sym("camera_80295A58"),
    0x80295BF0: table.sym("camera_80295BF0"),
    0x80295E24: table.sym("camera_80295E24"),
    0x80295E8C: table.sym("camera_80295E8C", table.GLOBL), # data
    0x80295FB0: table.sym("camera_80295FB0", table.GLOBL), # data
    0x80295FD8: table.sym("camera_80295FD8", table.GLOBL), # data
    0x80296020: table.sym("camera_80296020"),
    0x802960B0: table.sym("camera_802960B0"), # unused
    0x80296160: table.sym("camera_80296160", table.GLOBL), # data
    0x802962C8: table.sym("camera_802962C8", table.GLOBL), # data
    0x802962F0: table.sym("camera_802962F0", table.GLOBL), # data
    0x80296318: table.sym("camera_80296318"),
    0x802963B8: table.sym("camera_802963B8"),
    0x8029652C: table.sym("camera_8029652C"),
    0x8029665C: table.sym("camera_8029665C"),
    0x8029669C: table.sym("camera_8029669C"),
    0x802966E4: table.sym("camera_802966E4"),
    0x80296710: table.sym("camera_80296710", table.GLOBL), # data
    0x802967C4: table.sym("camera_802967C4", table.GLOBL), # data
    0x8029685C: table.sym("camera_8029685C"),
    0x802968A0: table.sym("camera_802968A0", table.GLOBL), # data
    0x8029695C: table.sym("camera_8029695C"),
    0x802969F8: table.sym("camera_802969F8", table.GLOBL), # data
    0x80296A64: table.sym("camera_80296A64"),
    0x80296B30: table.sym("camera_80296B30", table.GLOBL), # data
    0x80296BC8: table.sym("camera_80296BC8"),
    0x80296C4C: table.sym("camera_80296C4C"),
    0x80296D60: table.sym("camera_80296D60"),
    0x80296DA8: table.sym("camera_80296DA8"),
    0x80296EB4: table.sym("camera_80296EB4"),
    0x80296F38: table.sym("camera_80296F38"),
    0x80296F70: table.sym("camera_80296F70"), # unused
    0x80296FA8: table.sym("camera_80296FA8", table.GLOBL), # data
    0x80297148: table.sym("camera_80297148"),
    0x8029720C: table.sym("camera_8029720C"),
    0x80297290: table.sym("camera_80297290"),
    0x802972EC: table.sym("camera_802972EC"),
    0x80297300: table.sym("camera_80297300"),
    0x80297384: table.sym("camera_80297384"),
    0x802973B0: table.sym("camera_802973B0", table.GLOBL), # data
    0x80297464: table.sym("camera_80297464"),
    0x80297560: table.sym("camera_80297560"),
    0x8029758C: table.sym("camera_8029758C"),
    0x802975C4: table.sym("camera_802975C4"),
    0x8029762C: table.sym("camera_8029762C", table.GLOBL), # data
    0x802976BC: table.sym("camera_802976BC"),
    0x80297728: table.sym("camera_80297728"),
    0x80297748: table.sym("camera_80297748"),
    0x80297784: table.sym("camera_80297784"),
    0x802977C8: table.sym("camera_802977C8"),
    0x802977F4: table.sym("camera_802977F4"),
    0x80297820: table.sym("camera_80297820"),
    0x8029784C: table.sym("camera_8029784C", table.GLOBL), # data
    0x80297908: table.sym("camera_80297908", table.GLOBL), # data
    0x80297A38: table.sym("camera_80297A38", table.GLOBL), # data
    0x80297A64: table.sym("camera_80297A64", table.GLOBL), # data
    0x80297B58: table.sym("camera_80297B58"),
    0x80297B84: table.sym("camera_80297B84", table.GLOBL), # data
    0x80297C14: table.sym("camera_80297C14"),
    0x80297C40: table.sym("camera_80297C40", table.GLOBL), # data
    0x802980DC: table.sym("camera_802980DC"),
    0x8029819C: table.sym("camera_8029819C"),
    0x80298218: table.sym("camera_80298218"),
    0x80298254: table.sym("camera_80298254"),
    0x80298290: table.sym("camera_80298290"),
    0x802983B4: table.sym("camera_802983B4", table.GLOBL), # data
    0x80298458: table.sym("camera_80298458", table.GLOBL), # data
    0x802984A0: table.sym("camera_802984A0"),
    0x802984B4: table.sym("camera_802984B4", table.GLOBL), # data
    0x802987B0: table.sym("camera_802987B0"),
    0x8029894C: table.sym("camera_8029894C"),
    0x802989E8: table.sym("camera_802989E8"),
    0x80298AF8: table.sym("camera_80298AF8", table.GLOBL), # data
    0x80298BA0: table.sym("camera_80298BA0", table.GLOBL), # data
    0x80298C2C: table.sym("camera_80298C2C", table.GLOBL), # data
    0x80298CCC: table.sym("camera_80298CCC", table.GLOBL), # data
    0x80298D44: table.sym("camera_80298D44", table.GLOBL), # data
    0x80298D9C: table.sym("camera_80298D9C", table.GLOBL), # data
    0x80298FE8: table.sym("camera_80298FE8", table.GLOBL), # data
    0x80299100: table.sym("camera_80299100", table.GLOBL), # data
    0x80299154: table.sym("camera_80299154", table.GLOBL), # data
    0x802991A8: table.sym("camera_802991A8", table.GLOBL), # data
    0x802991F0: table.sym("camera_802991F0", table.GLOBL), # data
    0x802992CC: table.sym("camera_802992CC", table.GLOBL), # data
    0x80299360: table.sym("camera_80299360", table.GLOBL), # data
    0x80299404: table.sym("camera_80299404", table.GLOBL), # data
    0x802994E8: table.sym("camera_802994E8"),
    0x8029A2F8: table.sym("camera_8029A2F8"),
    0x8029A37C: table.sym("camera_8029A37C"),
    0x8029A3B4: table.sym("camera_8029A3B4"),
    0x8029A41C: table.sym("camera_8029A41C"),
    0x8029A4D0: table.sym("camera_8029A4D0"),
    0x8029A5BC: table.sym("camera_8029A5BC"), # unused
    0x8029A5E8: table.sym("camera_8029A5E8"),
    0x8029A60C: table.sym("camera_8029A60C"),
    0x8029A64C: table.sym("camera_8029A64C"),
    0x8029A670: table.sym("camera_8029A670"),
    0x8029A694: table.sym("camera_8029A694"),
    0x8029A6F4: table.sym("camera_8029A6F4"),
    0x8029A81C: table.sym("camera_8029A81C"), # unused
    0x8029A858: table.sym("camera_8029A858"),
    0x8029A894: table.sym("camera_8029A894"),
    0x8029A8D0: table.sym("camera_8029A8D0"),
    0x8029A968: table.sym("camera_8029A968"),
    0x8029A9A4: table.sym("camera_8029A9A4"),
    0x8029AA3C: table.sym("camera_8029AA3C", table.GLOBL), # g callback
    0x8029AB94: table.sym("camera_8029AB94"),
    0x8029ABB0: table.sym("camera_8029ABB0"),
    0x8029AC30: table.sym("camera_8029AC30"),
    0x8029AD80: table.sym("camera_8029AD80"), # unused
    0x8029AE40: table.sym("camera_8029AE40"), # unused
    0x8029AEF8: table.sym("camera_8029AEF8"),
    0x8029AF98: table.sym("camera_8029AF98"),
    0x8029B08C: table.sym("camera_8029B08C", table.GLOBL), # o callback
    0x8029B28C: table.sym("camera_8029B28C"),
    0x8029B358: table.sym("camera_8029B358"),
    0x8029B3C8: table.sym("camera_8029B3C8"),
    0x8029B49C: table.sym("camera_8029B49C", table.GLOBL), # o callback
    0x8029BDE4: table.sym("camera_8029BDE4", table.GLOBL), # o callback
    0x8029BF64: table.sym("camera_8029BF64", table.GLOBL), # o callback
    0x8029C0E4: table.sym("camera_8029C0E4"),
    0x8029C254: table.sym("camera_8029C254", table.GLOBL), # o callback

    # src/course.S
    0x8029C770: table.sym("course_8029C770", table.GLOBL),

    # src/object_update.S
    0x8029C780: table.sym("object_update_8029C780"),
    0x8029C9CC: table.sym("object_update_8029C9CC"),
    0x8029CA58: table.sym("object_update_8029CA58", table.GLOBL), # o callback
    0x8029CB34: table.sym("object_update_8029CB34"),
    0x8029CBC8: table.sym("object_update_8029CBC8"),
    0x8029CD28: table.sym("object_update_8029CD28"),
    0x8029CD98: table.sym("object_update_8029CD98"),
    0x8029CE58: table.sym("object_update_8029CE58", table.GLOBL),
    0x8029CEDC: table.sym("object_update_8029CEDC", table.GLOBL),
    0x8029CFB0: table.sym("object_update_8029CFB0", table.GLOBL),
    0x8029D1D8: table.sym("object_update_8029D1D8"),
    0x8029D1E8: table.sym("object_update_8029D1E8", table.GLOBL),
    0x8029D324: table.sym("object_update_8029D324"),
    0x8029D374: table.sym("object_update_8029D374"),
    0x8029D428: table.sym("object_update_8029D428"),
    0x8029D4D0: table.sym("object_update_8029D4D0"), # unused
    0x8029D690: table.sym("object_update_8029D690", table.GLOBL),

    # src/object.S
    0x8029D890: table.sym("object_8029D890", table.GLOBL), # g callback
    0x8029D924: table.sym("object_8029D924", table.GLOBL), # g callback
    0x8029DB48: table.sym("object_8029DB48", table.GLOBL), # g callback
    0x8029DBD4: table.sym("object_8029DBD4", table.GLOBL), # g callback
    0x8029DCD4: table.sym("object_8029DCD4", table.GLOBL),
    0x8029DDA8: table.sym("object_8029DDA8", table.GLOBL),
    0x8029DE80: table.sym("object_8029DE80", table.GLOBL),
    0x8029E1B0: table.sym("object_8029E1B0", table.GLOBL),
    0x8029E27C: table.sym("object_8029E27C", table.GLOBL),
    0x8029E2F8: table.sym("object_8029E2F8", table.GLOBL),
    0x8029E398: table.sym("object_8029E398", table.GLOBL),
    0x8029E3E8: table.sym("object_8029E3E8", table.GLOBL),
    0x8029E494: table.sym("object_8029E494", table.GLOBL),
    0x8029E530: table.sym("object_8029E530", table.GLOBL),
    0x8029E5EC: table.sym("object_8029E5EC", table.GLOBL),
    0x8029E694: table.sym("object_8029E694", table.GLOBL),
    0x8029E714: table.sym("object_8029E714", table.GLOBL),
    0x8029E8BC: table.sym("object_8029E8BC", table.GLOBL),
    0x8029E914: table.sym("object_8029E914", table.GLOBL),
    0x8029E96C: table.sym("object_8029E96C", table.GLOBL),
    0x8029E9AC: table.sym("object_8029E9AC", table.GLOBL),
    0x8029EA24: table.sym("object_8029EA24", table.GLOBL),
    0x8029EAAC: table.sym("object_8029EAAC"), # unused
    0x8029EB04: table.sym("object_8029EB04", table.GLOBL),
    0x8029ED20: table.sym("object_8029ED20", table.GLOBL),
    0x8029EDCC: table.sym("object_8029EDCC", table.GLOBL),
    0x8029EE24: table.sym("object_8029EE24", table.GLOBL),
    0x8029EEB8: table.sym("object_8029EEB8", table.GLOBL),
    0x8029EF20: table.sym("object_8029EF20"),
    0x8029EF64: table.sym("object_8029EF64", table.GLOBL),
    0x8029EFFC: table.sym("object_8029EFFC", table.GLOBL),
    0x8029F070: table.sym("object_8029F070"), # unused
    0x8029F0C8: table.sym("object_8029F0C8", table.GLOBL),
    0x8029F0E0: table.sym("object_8029F0E0", table.GLOBL),
    0x8029F120: table.sym("object_8029F120", table.GLOBL),
    0x8029F148: table.sym("object_8029F148"),
    0x8029F188: table.sym("object_8029F188", table.GLOBL),
    0x8029F1B0: table.sym("object_8029F1B0"), # unused
    0x8029F200: table.sym("object_8029F200", table.GLOBL),
    0x8029F274: table.sym("object_8029F274", table.GLOBL),
    0x8029F2EC: table.sym("object_8029F2EC"),
    0x8029F3A8: table.sym("object_8029F3A8", table.GLOBL),
    0x8029F3D0: table.sym("object_8029F3D0", table.GLOBL),
    0x8029F404: table.sym("object_8029F404", table.GLOBL),
    0x8029F430: table.sym("object_8029F430", table.GLOBL),
    0x8029F464: table.sym("object_8029F464", table.GLOBL),
    0x8029F4B4: table.sym("object_8029F4B4", table.GLOBL),
    0x8029F514: table.sym("object_8029F514", table.GLOBL),
    0x8029F59C: table.sym("object_8029F59C", table.GLOBL),
    0x8029F600: table.sym("object_8029F600"), # unused
    0x8029F620: table.sym("object_8029F620", table.GLOBL),
    0x8029F644: table.sym("object_8029F644"), # unused
    0x8029F66C: table.sym("object_8029F66C", table.GLOBL),
    0x8029F694: table.sym("object_8029F694", table.GLOBL),
    0x8029F6BC: table.sym("object_8029F6BC", table.GLOBL),
    0x8029F6E0: table.sym("object_8029F6E0", table.GLOBL),
    0x8029F7D8: table.sym("object_8029F7D8"),
    0x8029F820: table.sym("object_8029F820", table.GLOBL),
    0x8029F848: table.sym("object_8029F848"), # unused
    0x8029F8EC: table.sym("object_8029F8EC", table.GLOBL),
    0x8029F914: table.sym("object_8029F914", table.GLOBL),
    0x8029F95C: table.sym("object_8029F95C", table.GLOBL),
    0x8029F998: table.sym("object_8029F998", table.GLOBL),
    0x8029F9EC: table.sym("object_8029F9EC", table.GLOBL),
    0x8029FB1C: table.sym("object_8029FB1C", table.GLOBL),
    0x8029FB68: table.sym("object_8029FB68"), # unused
    0x8029FBDC: table.sym("object_8029FBDC", table.GLOBL),
    0x8029FC9C: table.sym("object_8029FC9C", table.GLOBL),
    0x8029FD8C: table.sym("object_8029FD8C"),
    0x8029FDB4: table.sym("object_8029FDB4", table.GLOBL),
    0x8029FE00: table.sym("object_8029FE00", table.GLOBL),
    0x8029FE6C: table.sym("object_8029FE6C", table.GLOBL),
    0x8029FEA4: table.sym("object_8029FEA4", table.GLOBL),
    0x8029FF04: table.sym("object_8029FF04", table.GLOBL),
    0x8029FFA4: table.sym("object_8029FFA4", table.GLOBL),
    0x802A0008: table.sym("object_802A0008", table.GLOBL),
    0x802A0050: table.sym("object_802A0050", table.GLOBL),
    0x802A00AC: table.sym("object_802A00AC"), # unused
    0x802A0114: table.sym("object_802A0114", table.GLOBL),
    0x802A0154: table.sym("object_802A0154", table.GLOBL),
    0x802A0198: table.sym("object_802A0198", table.GLOBL),
    0x802A01D8: table.sym("object_802A01D8", table.GLOBL),
    0x802A0234: table.sym("object_802A0234"),
    0x802A0380: table.sym("object_802A0380", table.GLOBL),
    0x802A0474: table.sym("object_802A0474", table.GLOBL),
    0x802A04C0: table.sym("object_802A04C0", table.GLOBL),
    0x802A04F0: table.sym("object_802A04F0"), # unused
    0x802A0514: table.sym("object_802A0514", table.GLOBL),
    0x802A0568: table.sym("object_802A0568", table.GLOBL),
    0x802A057C: table.sym("object_802A057C", table.GLOBL),
    0x802A05B4: table.sym("object_802A05B4", table.GLOBL),
    0x802A05D4: table.sym("object_802A05D4", table.GLOBL),
    0x802A05F0: table.sym("object_802A05F0", table.GLOBL),
    0x802A0604: table.sym("object_802A0604", table.GLOBL),
    0x802A064C: table.sym("object_802A064C", table.GLOBL),
    0x802A069C: table.sym("object_802A069C"),
    0x802A079C: table.sym("object_802A079C", table.GLOBL),
    0x802A07E8: table.sym("object_802A07E8"),
    0x802A0AB0: table.sym("object_802A0AB0"),
    0x802A0BDC: table.sym("object_802A0BDC"),
    0x802A0D84: table.sym("object_802A0D84"),
    0x802A0E68: table.sym("object_802A0E68", table.GLOBL),
    0x802A10E0: table.sym("object_802A10E0"), # unused
    0x802A10F0: table.sym("object_802A10F0"),
    0x802A113C: table.sym("object_802A113C"), # unused
    0x802A11A8: table.sym("object_802A11A8", table.GLOBL),
    0x802A120C: table.sym("object_802A120C", table.GLOBL),
    0x802A12A4: table.sym("object_802A12A4", table.GLOBL),
    0x802A1308: table.sym("object_802A1308", table.GLOBL), # o callback
    0x802A1370: table.sym("object_802A1370", table.GLOBL),
    0x802A1424: table.sym("object_802A1424", table.GLOBL),
    0x802A148C: table.sym("object_802A148C", table.GLOBL),
    0x802A14C4: table.sym("object_802A14C4", table.GLOBL),
    0x802A14FC: table.sym("object_802A14FC", table.GLOBL),
    0x802A1554: table.sym("object_802A1554", table.GLOBL),
    0x802A15AC: table.sym("object_802A15AC", table.GLOBL),
    0x802A1634: table.sym("object_802A1634", table.GLOBL),
    0x802A16AC: table.sym("object_802A16AC"), # unused
    0x802A1774: table.sym("object_802A1774"), # unused
    0x802A184C: table.sym("object_802A184C", table.GLOBL),
    0x802A188C: table.sym("object_802A188C", table.GLOBL),
    0x802A18DC: table.sym("object_802A18DC", table.GLOBL),
    0x802A1930: table.sym("object_802A1930", table.GLOBL),
    0x802A1960: table.sym("object_802A1960"), # unused
    0x802A19AC: table.sym("object_802A19AC", table.GLOBL),
    0x802A19C8: table.sym("object_802A19C8", table.GLOBL),
    0x802A19F0: table.sym("object_802A19F0", table.GLOBL),
    0x802A1A18: table.sym("object_802A1A18"),
    0x802A1B34: table.sym("object_802A1B34"),
    0x802A1B8C: table.sym("object_802A1B8C", table.GLOBL),
    0x802A1BDC: table.sym("object_802A1BDC", table.GLOBL),
    0x802A1C68: table.sym("object_802A1C68"), # unused
    0x802A1CC4: table.sym("object_802A1CC4"), # unused
    0x802A1D7C: table.sym("object_802A1D7C"),
    0x802A1F3C: table.sym("object_802A1F3C", table.GLOBL),
    0x802A20F4: table.sym("object_802A20F4"),
    0x802A21D4: table.sym("object_802A21D4"),
    0x802A2320: table.sym("object_802A2320", table.GLOBL), # o callback
    0x802A2348: table.sym("object_802A2348", table.GLOBL),
    0x802A24D0: table.sym("object_802A24D0"),
    0x802A25B4: table.sym("object_802A25B4", table.GLOBL),
    0x802A2644: table.sym("object_802A2644", table.GLOBL), # o callback
    0x802A2674: table.sym("object_802A2674"), # unused
    0x802A2748: table.sym("object_802A2748", table.GLOBL),
    0x802A27B0: table.sym("object_802A27B0", table.GLOBL),
    0x802A2804: table.sym("object_802A2804", table.GLOBL),
    0x802A2930: table.sym("object_802A2930", table.GLOBL),
    0x802A2A18: table.sym("object_802A2A18", table.GLOBL),
    0x802A2A84: table.sym("object_802A2A84", table.GLOBL),
    0x802A2B28: table.sym("object_802A2B28"), # unused
    0x802A2B6C: table.sym("object_802A2B6C"), # unused
    0x802A2BC4: table.sym("object_802A2BC4", table.GLOBL), # o callback
    0x802A2C1C: table.sym("object_802A2C1C"), # unused
    0x802A2C5C: table.sym("object_802A2C5C", table.GLOBL),
    0x802A2ED4: table.sym("object_802A2ED4", table.GLOBL),
    0x802A2F14: table.sym("object_802A2F14", table.GLOBL),
    0x802A2F5C: table.sym("object_802A2F5C", table.GLOBL),
    0x802A2FC0: table.sym("object_802A2FC0", table.GLOBL),
    0x802A308C: table.sym("object_802A308C", table.GLOBL),
    0x802A3124: table.sym("object_802A3124"),
    0x802A31E0: table.sym("object_802A31E0", table.GLOBL),
    0x802A3268: table.sym("object_802A3268", table.GLOBL),
    0x802A32AC: table.sym("object_802A32AC", table.GLOBL),
    0x802A34A4: table.sym("object_802A34A4", table.GLOBL),
    0x802A3604: table.sym("object_802A3604", table.GLOBL),
    0x802A3634: table.sym("object_802A3634", table.GLOBL),
    0x802A3674: table.sym("object_802A3674", table.GLOBL),
    0x802A36A4: table.sym("object_802A36A4", table.GLOBL),
    0x802A3754: table.sym("object_802A3754", table.GLOBL),
    0x802A37AC: table.sym("object_802A37AC", table.GLOBL),
    0x802A37DC: table.sym("object_802A37DC", table.GLOBL),
    0x802A3818: table.sym("object_802A3818", table.GLOBL),
    0x802A390C: table.sym("object_802A390C", table.GLOBL),
    0x802A399C: table.sym("object_802A399C", table.GLOBL), # o callback
    0x802A3A3C: table.sym("object_802A3A3C"), # unused
    0x802A3A4C: table.sym("object_802A3A4C", table.GLOBL),
    0x802A3A88: table.sym("object_802A3A88", table.GLOBL),
    0x802A3B28: table.sym("object_802A3B28"), # unused
    0x802A3B40: table.sym("object_802A3B40", table.GLOBL),
    0x802A3C18: table.sym("object_802A3C18", table.GLOBL),
    0x802A3CEC: table.sym("object_802A3CEC"), # unused
    0x802A3CFC: table.sym("object_802A3CFC", table.GLOBL),
    0x802A3D40: table.sym("object_802A3D40"), # unused
    0x802A3DD4: table.sym("object_802A3DD4", table.GLOBL),
    0x802A3E30: table.sym("object_802A3E30", table.GLOBL),
    0x802A3E80: table.sym("object_802A3E80"),
    0x802A3EF8: table.sym("object_802A3EF8"), # unused
    0x802A3F24: table.sym("object_802A3F24", table.GLOBL),
    0x802A3F48: table.sym("object_802A3F48", table.GLOBL),
    0x802A404C: table.sym("object_802A404C", table.GLOBL),
    0x802A40B8: table.sym("object_802A40B8", table.GLOBL),
    0x802A4110: table.sym("object_802A4110"), # unused
    0x802A4120: table.sym("object_802A4120", table.GLOBL), # o callback
    0x802A4210: table.sym("object_802A4210", table.GLOBL),
    0x802A4360: table.sym("object_802A4360", table.GLOBL),
    0x802A4440: table.sym("object_802A4440", table.GLOBL),
    0x802A44F4: table.sym("object_802A44F4", table.GLOBL),
    0x802A452C: table.sym("object_802A452C", table.GLOBL),
    0x802A4564: table.sym("object_802A4564", table.GLOBL),
    0x802A45E4: table.sym("object_802A45E4", table.GLOBL), # g callback
    0x802A462C: table.sym("object_802A462C"), # unused
    0x802A46CC: table.sym("object_802A46CC", table.GLOBL),
    0x802A4704: table.sym("object_802A4704", table.GLOBL),
    0x802A4728: table.sym("object_802A4728", table.GLOBL),
    0x802A4750: table.sym("object_802A4750", table.GLOBL),
    0x802A4774: table.sym("object_802A4774", table.GLOBL),
    0x802A47A0: table.sym("object_802A47A0", table.GLOBL),
    0x802A48BC: table.sym("object_802A48BC", table.GLOBL),
    0x802A48FC: table.sym("object_802A48FC"),
    0x802A4960: table.sym("object_802A4960", table.GLOBL),
    0x802A4BE4: table.sym("object_802A4BE4", table.GLOBL),
    0x802A4F04: table.sym("object_802A4F04", table.GLOBL),
    0x802A4F58: table.sym("object_802A4F58", table.GLOBL),
    0x802A5034: table.sym("object_802A5034"), # unused
    0x802A50FC: table.sym("object_802A50FC", table.GLOBL),
    0x802A513C: table.sym("object_802A513C", table.GLOBL),
    0x802A51AC: table.sym("object_802A51AC", table.GLOBL),
    0x802A5228: table.sym("object_802A5228", table.GLOBL),
    0x802A5248: table.sym("object_802A5248", table.GLOBL),
    0x802A5288: table.sym("object_802A5288", table.GLOBL),
    0x802A52C4: table.sym("object_802A52C4", table.GLOBL),
    0x802A52F8: table.sym("object_802A52F8", table.GLOBL),
    0x802A5358: table.sym("object_802A5358", table.GLOBL),
    0x802A540C: table.sym("object_802A540C"), # unused
    0x802A5460: table.sym("object_802A5460"), # unused
    0x802A5498: table.sym("object_802A5498", table.GLOBL),
    0x802A54D8: table.sym("object_802A54D8", table.GLOBL),
    0x802A5524: table.sym("object_802A5524", table.GLOBL),
    0x802A5588: table.sym("object_802A5588", table.GLOBL),

    # src/object_state_a.S
    0x802A5620: table.sym("object_state_a_802A5620"),
    0x802A56BC: table.sym("object_state_a_802A56BC", table.GLOBL), # o callback
    0x802A58DC: table.sym("object_state_a_802A58DC", table.GLOBL), # o callback
    0x802A597C: table.sym("object_state_a_802A597C", table.GLOBL), # data
    0x802A5A44: table.sym("object_state_a_802A5A44", table.GLOBL), # data
    0x802A5AA0: table.sym("object_state_a_802A5AA0", table.GLOBL), # o callback
    0x802A5ACC: table.sym("object_state_a_802A5ACC"),
    0x802A5BD4: table.sym("object_state_a_802A5BD4", table.GLOBL), # o callback
    0x802A5D4C: table.sym("object_state_a_802A5D4C", table.GLOBL), # data
    0x802A6518: table.sym("object_state_a_802A6518", table.GLOBL), # data
    0x802A68A0: table.sym("object_state_a_802A68A0", table.GLOBL), # data
    0x802A6AD8: table.sym("object_state_a_802A6AD8", table.GLOBL), # data
    0x802A6B7C: table.sym("object_state_a_802A6B7C", table.GLOBL), # o callback
    0x802A6C20: table.sym("object_state_a_802A6C20", table.GLOBL), # o callback
    0x802A6C74: table.sym("object_state_a_802A6C74", table.GLOBL), # o callback
    0x802A6CF4: table.sym("object_state_a_802A6CF4", table.GLOBL), # o callback
    0x802A6D64: table.sym("object_state_a_802A6D64", table.GLOBL), # o callback
    0x802A6EE4: table.sym("object_state_a_802A6EE4", table.GLOBL), # data
    0x802A7020: table.sym("object_state_a_802A7020", table.GLOBL), # data
    0x802A708C: table.sym("object_state_a_802A708C", table.GLOBL), # data
    0x802A7160: table.sym("object_state_a_802A7160", table.GLOBL), # data
    0x802A7170: table.sym("object_state_a_802A7170", table.GLOBL), # o callback
    0x802A719C: table.sym("object_state_a_802A719C", table.GLOBL), # g callback
    0x802A7230: table.sym("object_state_a_802A7230", table.GLOBL), # o callback
    0x802A7264: table.sym("object_state_a_802A7264", table.GLOBL), # data
    0x802A7384: table.sym("object_state_a_802A7384"),
    0x802A73D8: table.sym("object_state_a_802A73D8", table.GLOBL), # data
    0x802A7598: table.sym("object_state_a_802A7598", table.GLOBL), # data
    0x802A7804: table.sym("object_state_a_802A7804", table.GLOBL), # data
    0x802A78D8: table.sym("object_state_a_802A78D8", table.GLOBL), # data
    0x802A7A60: table.sym("object_state_a_802A7A60", table.GLOBL), # data
    0x802A7B1C: table.sym("object_state_a_802A7B1C", table.GLOBL), # data
    0x802A7B5C: table.sym("object_state_a_802A7B5C", table.GLOBL), # data
    0x802A7D14: table.sym("object_state_a_802A7D14", table.GLOBL), # data
    0x802A7FBC: table.sym("object_state_a_802A7FBC"),
    0x802A8064: table.sym("object_state_a_802A8064", table.GLOBL), # o callback
    0x802A816C: table.sym("object_state_a_802A816C", table.GLOBL), # o callback
    0x802A81E8: table.sym("object_state_a_802A81E8", table.GLOBL), # o callback
    0x802A821C: table.sym("object_state_a_802A821C", table.GLOBL), # o callback
    0x802A8370: table.sym("object_state_a_802A8370", table.GLOBL), # o callback
    0x802A83A0: table.sym("object_state_a_802A83A0", table.GLOBL), # o callback
    0x802A8630: table.sym("object_state_a_802A8630", table.GLOBL), # o callback
    0x802A86BC: table.sym("object_state_a_802A86BC"), # unused
    0x802A870C: table.sym("object_state_a_802A870C", table.GLOBL), # o callback
    0x802A88A4: table.sym("object_state_a_802A88A4", table.GLOBL), # o callback
    0x802A8A38: table.sym("object_state_a_802A8A38"),
    0x802A8B18: table.sym("object_state_a_802A8B18", table.GLOBL), # o callback
    0x802A8BC0: table.sym("object_state_a_802A8BC0", table.GLOBL), # o callback
    0x802A8C88: table.sym("object_state_a_802A8C88", table.GLOBL), # o callback
    0x802A8CDC: table.sym("object_state_a_802A8CDC", table.GLOBL), # o callback
    0x802A8D48: table.sym("object_state_a_802A8D48", table.GLOBL), # o callback
    0x802A8D98: table.sym("object_state_a_802A8D98", table.GLOBL), # o callback
    0x802A8DC0: table.sym("object_state_a_802A8DC0", table.GLOBL), # data
    0x802A8F40: table.sym("object_state_a_802A8F40", table.GLOBL), # data
    0x802A9114: table.sym("object_state_a_802A9114", table.GLOBL), # data
    0x802A92FC: table.sym("object_state_a_802A92FC", table.GLOBL), # data
    0x802A93F8: table.sym("object_state_a_802A93F8", table.GLOBL), # data
    0x802A9440: table.sym("object_state_a_802A9440", table.GLOBL), # data
    0x802A9460: table.sym("object_state_a_802A9460", table.GLOBL), # data
    0x802A9498: table.sym("object_state_a_802A9498", table.GLOBL), # o callback
    0x802A94F8: table.sym("object_state_a_802A94F8", table.GLOBL), # o callback
    0x802A958C: table.sym("object_state_a_802A958C"),
    0x802A9708: table.sym("object_state_a_802A9708", table.GLOBL), # o callback
    0x802A973C: table.sym("object_state_a_802A973C"), # unused
    0x802A98C4: table.sym("object_state_a_802A98C4"),
    0x802A9994: table.sym("object_state_a_802A9994", table.GLOBL), # data
    0x802A9D08: table.sym("object_state_a_802A9D08", table.GLOBL), # data
    0x802A9F54: table.sym("object_state_a_802A9F54", table.GLOBL), # data
    0x802A9FC8: table.sym("object_state_a_802A9FC8", table.GLOBL), # data
    0x802AA02C: table.sym("object_state_a_802AA02C"),
    0x802AA0AC: table.sym("object_state_a_802AA0AC", table.GLOBL), # o callback
    0x802AA1B8: table.sym("object_state_a_802AA1B8", table.GLOBL), # o callback
    0x802AA280: table.sym("object_state_a_802AA280"),
    0x802AA3C8: table.sym("object_state_a_802AA3C8"),
    0x802AA3F4: table.sym("object_state_a_802AA3F4", table.GLOBL), # o callback
    0x802AA700: table.sym("object_state_a_802AA700", table.GLOBL), # o callback
    0x802AA774: table.sym("object_state_a_802AA774", table.GLOBL), # o callback
    0x802AA830: table.sym("object_state_a_802AA830", table.GLOBL), # o callback
    0x802AA948: table.sym("object_state_a_802AA948"),
    0x802AA97C: table.sym("object_state_a_802AA97C", table.GLOBL), # o callback
    0x802AAA60: table.sym("object_state_a_802AAA60", table.GLOBL), # o callback
    0x802AAB54: table.sym("object_state_a_802AAB54", table.GLOBL), # o callback
    0x802AAC48: table.sym("object_state_a_802AAC48", table.GLOBL), # o callback
    0x802AAE8C: table.sym("object_state_a_802AAE8C", table.GLOBL),
    0x802AAF48: table.sym("object_state_a_802AAF48", table.GLOBL), # o callback
    0x802AAFFC: table.sym("object_state_a_802AAFFC"),
    0x802AB060: table.sym("object_state_a_802AB060"),
    0x802AB158: table.sym("object_state_a_802AB158"),
    0x802AB18C: table.sym("object_state_a_802AB18C"),
    0x802AB1C8: table.sym("object_state_a_802AB1C8", table.GLOBL), # o callback
    0x802AB558: table.sym("object_state_a_802AB558", table.GLOBL),
    0x802AB5C8: table.sym("object_state_a_802AB5C8"),
    0x802AB650: table.sym("object_state_a_802AB650", table.GLOBL), # o callback
    0x802AB70C: table.sym("object_state_a_802AB70C", table.GLOBL), # o callback
    0x802AB748: table.sym("object_state_a_802AB748", table.GLOBL), # o callback
    0x802AB7A4: table.sym("object_state_a_802AB7A4", table.GLOBL), # o callback
    0x802AB860: table.sym("object_state_a_802AB860", table.GLOBL), # o callback
    0x802ABA40: table.sym("object_state_a_802ABA40", table.GLOBL), # o callback
    0x802ABC04: table.sym("object_state_a_802ABC04"),
    0x802ABEE4: table.sym("object_state_a_802ABEE4", table.GLOBL), # o callback
    0x802ABF0C: table.sym("object_state_a_802ABF0C", table.GLOBL), # o callback
    0x802AC068: table.sym("object_state_a_802AC068", table.GLOBL), # data
    0x802AC15C: table.sym("object_state_a_802AC15C", table.GLOBL), # data
    0x802AC294: table.sym("object_state_a_802AC294", table.GLOBL), # o callback
    0x802AC2C0: table.sym("object_state_a_802AC2C0", table.GLOBL), # o callback
    0x802AC2EC: table.sym("object_state_a_802AC2EC", table.GLOBL), # o callback
    0x802AC3A8: table.sym("object_state_a_802AC3A8", table.GLOBL), # o callback
    0x802AC4A0: table.sym("object_state_a_802AC4A0", table.GLOBL), # o callback
    0x802AC5B4: table.sym("object_state_a_802AC5B4", table.GLOBL), # o callback
    0x802AC678: table.sym("object_state_a_802AC678", table.GLOBL), # o callback
    0x802AC78C: table.sym("object_state_a_802AC78C", table.GLOBL), # o callback
    0x802AC864: table.sym("object_state_a_802AC864", table.GLOBL), # o callback
    0x802AC910: table.sym("object_state_a_802AC910"),
    0x802AC958: table.sym("object_state_a_802AC958"),
    0x802AC9D0: table.sym("object_state_a_802AC9D0"),
    0x802ACA6C: table.sym("object_state_a_802ACA6C"),
    0x802ACAC8: table.sym("object_state_a_802ACAC8", table.GLOBL), # o callback
    0x802ACC3C: table.sym("object_state_a_802ACC3C", table.GLOBL), # o callback
    0x802ACE80: table.sym("object_state_a_802ACE80", table.GLOBL), # o callback
    0x802AD078: table.sym("object_state_a_802AD078", table.GLOBL), # data
    0x802AD10C: table.sym("object_state_a_802AD10C", table.GLOBL), # data
    0x802AD1A4: table.sym("object_state_a_802AD1A4", table.GLOBL), # data
    0x802AD238: table.sym("object_state_a_802AD238", table.GLOBL), # data
    0x802AD2D0: table.sym("object_state_a_802AD2D0", table.GLOBL), # data
    0x802AD34C: table.sym("object_state_a_802AD34C", table.GLOBL), # o callback
    0x802AD378: table.sym("object_state_a_802AD378", table.GLOBL), # o callback
    0x802AD580: table.sym("object_state_a_802AD580", table.GLOBL), # data
    0x802AD76C: table.sym("object_state_a_802AD76C", table.GLOBL), # data
    0x802AD7F4: table.sym("object_state_a_802AD7F4", table.GLOBL), # data
    0x802AD828: table.sym("object_state_a_802AD828", table.GLOBL), # data
    0x802AD890: table.sym("object_state_a_802AD890", table.GLOBL), # o callback
    0x802AD8BC: table.sym("object_state_a_802AD8BC"),
    0x802AD8F0: table.sym("object_state_a_802AD8F0", table.GLOBL), # data
    0x802ADA4C: table.sym("object_state_a_802ADA4C", table.GLOBL), # data
    0x802ADB88: table.sym("object_state_a_802ADB88", table.GLOBL), # data
    0x802ADCE4: table.sym("object_state_a_802ADCE4", table.GLOBL), # data
    0x802ADD70: table.sym("object_state_a_802ADD70", table.GLOBL), # data
    0x802ADDF8: table.sym("object_state_a_802ADDF8", table.GLOBL), # o callback
    0x802ADF6C: table.sym("object_state_a_802ADF6C", table.GLOBL), # o callback
    0x802ADF98: table.sym("object_state_a_802ADF98", table.GLOBL), # o callback
    0x802ADFD8: table.sym("object_state_a_802ADFD8", table.GLOBL), # o callback
    0x802AE0CC: table.sym("object_state_a_802AE0CC", table.GLOBL),
    0x802AE238: table.sym("object_state_a_802AE238", table.GLOBL), # o callback
    0x802AE304: table.sym("object_state_a_802AE304", table.GLOBL), # o callback
    0x802AE334: table.sym("object_state_a_802AE334", table.GLOBL),
    0x802AE360: table.sym("object_state_a_802AE360", table.GLOBL), # o callback
    0x802AE394: table.sym("object_state_a_802AE394"), # unused
    0x802AE45C: table.sym("object_state_a_802AE45C"),
    0x802AE48C: table.sym("object_state_a_802AE48C", table.GLOBL), # o callback
    0x802AE4C0: table.sym("object_state_a_802AE4C0", table.GLOBL),
    0x802AE534: table.sym("object_state_a_802AE534", table.GLOBL), # o callback
    0x802AE85C: table.sym("object_state_a_802AE85C", table.GLOBL), # o callback
    0x802AE908: table.sym("object_state_a_802AE908", table.GLOBL), # o callback
    0x802AEA6C: table.sym("object_state_a_802AEA6C", table.GLOBL), # data
    0x802AEAB8: table.sym("object_state_a_802AEAB8", table.GLOBL), # data
    0x802AEB1C: table.sym("object_state_a_802AEB1C", table.GLOBL), # data
    0x802AEB74: table.sym("object_state_a_802AEB74", table.GLOBL), # data
    0x802AEB9C: table.sym("object_state_a_802AEB9C", table.GLOBL), # o callback
    0x802AEBC8: table.sym("object_state_a_802AEBC8", table.GLOBL), # o callback
    0x802AEC40: table.sym("object_state_a_802AEC40", table.GLOBL), # o callback
    0x802AECA8: table.sym("object_state_a_802AECA8", table.GLOBL), # o callback
    0x802AECDC: table.sym("object_state_a_802AECDC", table.GLOBL), # o callback
    0x802AEDC0: table.sym("object_state_a_802AEDC0", table.GLOBL), # o callback
    0x802AEEA4: table.sym("object_state_a_802AEEA4", table.GLOBL), # o callback
    0x802AEF1C: table.sym("object_state_a_802AEF1C", table.GLOBL), # o callback
    0x802AF1E8: table.sym("object_state_a_802AF1E8", table.GLOBL), # o callback
    0x802AF3FC: table.sym("object_state_a_802AF3FC", table.GLOBL), # o callback
    0x802AF448: table.sym("object_state_a_802AF448", table.GLOBL), # o callback
    0x802AF5F8: table.sym("object_state_a_802AF5F8", table.GLOBL), # o callback
    0x802AF7C4: table.sym("object_state_a_802AF7C4", table.GLOBL), # o callback
    0x802AF9CC: table.sym("object_state_a_802AF9CC", table.GLOBL), # o callback
    0x802AFA0C: table.sym("object_state_a_802AFA0C", table.GLOBL), # o callback
    0x802AFAE4: table.sym("object_state_a_802AFAE4", table.GLOBL), # o callback
    0x802AFBF8: table.sym("object_state_a_802AFBF8", table.GLOBL), # o callback
    0x802AFCE4: table.sym("object_state_a_802AFCE4", table.GLOBL), # o callback
    0x802AFD1C: table.sym("object_state_a_802AFD1C", table.GLOBL), # o callback
    0x802AFEE8: table.sym("object_state_a_802AFEE8", table.GLOBL), # o callback
    0x802AFF30: table.sym("object_state_a_802AFF30", table.GLOBL), # o callback
    0x802B00E4: table.sym("object_state_a_802B00E4", table.GLOBL), # o callback
    0x802B0244: table.sym("object_state_a_802B0244"),
    0x802B039C: table.sym("object_state_a_802B039C"),
    0x802B04B4: table.sym("object_state_a_802B04B4", table.GLOBL), # o callback
    0x802B0614: table.sym("object_state_a_802B0614", table.GLOBL), # o callback
    0x802B0974: table.sym("object_state_a_802B0974", table.GLOBL), # o callback
    0x802B0B9C: table.sym("object_state_a_802B0B9C"),
    0x802B0BEC: table.sym("object_state_a_802B0BEC", table.GLOBL), # o callback
    0x802B0D48: table.sym("object_state_a_802B0D48", table.GLOBL), # o callback
    0x802B0DF0: table.sym("object_state_a_802B0DF0", table.GLOBL), # o callback
    0x802B1278: table.sym("object_state_a_802B1278", table.GLOBL), # o callback
    0x802B14F4: table.sym("object_state_a_802B14F4"),
    0x802B15E8: table.sym("object_state_a_802B15E8", table.GLOBL), # o callback
    0x802B1714: table.sym("object_state_a_802B1714"),
    0x802B17F4: table.sym("object_state_a_802B17F4"),
    0x802B19D8: table.sym("object_state_a_802B19D8"),
    0x802B1AE0: table.sym("object_state_a_802B1AE0", table.GLOBL), # o callback
    0x802B1B2C: table.sym("object_state_a_802B1B2C", table.GLOBL), # o callback
    0x802B1BB0: table.sym("g_mario_pos_child", table.GLOBL), # g callback
    0x802B1C54: table.sym("object_state_a_802B1C54", table.GLOBL), # o callback
    0x802B1D7C: table.sym("object_state_a_802B1D7C", table.GLOBL), # data
    0x802B1E6C: table.sym("object_state_a_802B1E6C", table.GLOBL), # data
    0x802B1FF4: table.sym("object_state_a_802B1FF4", table.GLOBL), # data
    0x802B20A0: table.sym("object_state_a_802B20A0", table.GLOBL), # data
    0x802B2154: table.sym("object_state_a_802B2154"),
    0x802B2278: table.sym("object_state_a_802B2278", table.GLOBL), # o callback
    0x802B2340: table.sym("object_state_a_802B2340", table.GLOBL), # o callback
    0x802B23E0: table.sym("object_state_a_802B23E0", table.GLOBL), # o callback
    0x802B2494: table.sym("object_state_a_802B2494", table.GLOBL), # o callback
    0x802B25AC: table.sym("object_state_a_802B25AC", table.GLOBL), # o callback
    0x802B26A4: table.sym("object_state_a_802B26A4", table.GLOBL), # data
    0x802B27D8: table.sym("object_state_a_802B27D8", table.GLOBL), # data
    0x802B2824: table.sym("object_state_a_802B2824"),
    0x802B288C: table.sym("object_state_a_802B288C", table.GLOBL), # o callback
    0x802B29B8: table.sym("object_state_a_802B29B8", table.GLOBL), # o callback
    0x802B2BC8: table.sym("object_state_a_802B2BC8"),
    0x802B2D10: table.sym("object_state_a_802B2D10", table.GLOBL), # o callback
    0x802B2DAC: table.sym("object_state_a_802B2DAC", table.GLOBL), # data
    0x802B2F34: table.sym("object_state_a_802B2F34", table.GLOBL), # data
    0x802B3064: table.sym("object_state_a_802B3064", table.GLOBL), # data
    0x802B3108: table.sym("object_state_a_802B3108", table.GLOBL), # o callback
    0x802B3134: table.sym("object_state_a_802B3134"),
    0x802B3250: table.sym("object_state_a_802B3250"),
    0x802B329C: table.sym("object_state_a_802B329C", table.GLOBL), # o callback
    0x802B3600: table.sym("object_state_a_802B3600", table.GLOBL), # o callback
    0x802B37B8: table.sym("object_state_a_802B37B8", table.GLOBL), # o callback
    0x802B3810: table.sym("object_state_a_802B3810", table.GLOBL), # o callback
    0x802B3830: table.sym("object_state_a_802B3830", table.GLOBL), # data
    0x802B38B8: table.sym("object_state_a_802B38B8", table.GLOBL), # data
    0x802B394C: table.sym("object_state_a_802B394C", table.GLOBL), # data
    0x802B3B08: table.sym("object_state_a_802B3B08", table.GLOBL), # data
    0x802B3B24: table.sym("object_state_a_802B3B24", table.GLOBL), # data
    0x802B3BE0: table.sym("object_state_a_802B3BE0", table.GLOBL), # o callback
    0x802B3C2C: table.sym("object_state_a_802B3C2C", table.GLOBL), # data
    0x802B3CDC: table.sym("object_state_a_802B3CDC", table.GLOBL), # data
    0x802B3D10: table.sym("object_state_a_802B3D10", table.GLOBL), # data
    0x802B3D74: table.sym("object_state_a_802B3D74", table.GLOBL), # o callback
    0x802B3DF4: table.sym("object_state_a_802B3DF4", table.GLOBL), # o callback
    0x802B4080: table.sym("object_state_a_802B4080", table.GLOBL), # o callback
    0x802B4184: table.sym("object_state_a_802B4184"),
    0x802B41FC: table.sym("object_state_a_802B41FC"),
    0x802B4288: table.sym("object_state_a_802B4288"),
    0x802B4300: table.sym("object_state_a_802B4300"),
    0x802B4368: table.sym("object_state_a_802B4368"),
    0x802B43DC: table.sym("object_state_a_802B43DC"),
    0x802B4478: table.sym("object_state_a_802B4478", table.GLOBL), # data
    0x802B44BC: table.sym("object_state_a_802B44BC", table.GLOBL), # data
    0x802B459C: table.sym("object_state_a_802B459C"), # unused
    0x802B45F4: table.sym("object_state_a_802B45F4"),
    0x802B473C: table.sym("object_state_a_802B473C"),
    0x802B48D4: table.sym("object_state_a_802B48D4"),
    0x802B4A1C: table.sym("object_state_a_802B4A1C"),
    0x802B4A3C: table.sym("object_state_a_802B4A3C"),
    0x802B4AF4: table.sym("object_state_a_802B4AF4"),
    0x802B4BAC: table.sym("object_state_a_802B4BAC", table.GLOBL), # data
    0x802B4BE8: table.sym("object_state_a_802B4BE8", table.GLOBL), # data
    0x802B4CA4: table.sym("object_state_a_802B4CA4", table.GLOBL), # data
    0x802B4D14: table.sym("object_state_a_802B4D14", table.GLOBL), # data
    0x802B4F00: table.sym("object_state_a_802B4F00", table.GLOBL), # data
    0x802B5104: table.sym("object_state_a_802B5104", table.GLOBL), # data
    0x802B5218: table.sym("object_state_a_802B5218", table.GLOBL), # data
    0x802B53F4: table.sym("object_state_a_802B53F4"),
    0x802B5444: table.sym("object_state_a_802B5444"),
    0x802B5554: table.sym("object_state_a_802B5554"),
    0x802B55CC: table.sym("object_state_a_802B55CC", table.GLOBL), # data
    0x802B5798: table.sym("object_state_a_802B5798", table.GLOBL), # data
    0x802B58BC: table.sym("object_state_a_802B58BC", table.GLOBL), # data
    0x802B59CC: table.sym("object_state_a_802B59CC", table.GLOBL), # data
    0x802B5AEC: table.sym("object_state_a_802B5AEC"),
    0x802B5C00: table.sym("object_state_a_802B5C00", table.GLOBL), # data
    0x802B5C40: table.sym("object_state_a_802B5C40", table.GLOBL), # data
    0x802B5F6C: table.sym("object_state_a_802B5F6C"),
    0x802B5FEC: table.sym("object_state_a_802B5FEC", table.GLOBL), # data
    0x802B611C: table.sym("object_state_a_802B611C"),
    0x802B6190: table.sym("object_state_a_802B6190", table.GLOBL), # data
    0x802B6568: table.sym("object_state_a_802B6568", table.GLOBL), # data
    0x802B65D0: table.sym("object_state_a_802B65D0"),
    0x802B6670: table.sym("object_state_a_802B6670"),
    0x802B6730: table.sym("object_state_a_802B6730"),
    0x802B67D4: table.sym("object_state_a_802B67D4"),
    0x802B6878: table.sym("object_state_a_802B6878"),
    0x802B6A10: table.sym("object_state_a_802B6A10"),
    0x802B6A78: table.sym("object_state_a_802B6A78"),
    0x802B6BAC: table.sym("object_state_a_802B6BAC"),
    0x802B6CF0: table.sym("object_state_a_802B6CF0", table.GLOBL), # data
    0x802B6E40: table.sym("object_state_a_802B6E40"),
    0x802B6EE0: table.sym("object_state_a_802B6EE0", table.GLOBL), # data
    0x802B711C: table.sym("object_state_a_802B711C"),
    0x802B71E4: table.sym("object_state_a_802B71E4"),
    0x802B72D4: table.sym("object_state_a_802B72D4"),
    0x802B7418: table.sym("object_state_a_802B7418"),
    0x802B75A4: table.sym("object_state_a_802B75A4", table.GLOBL), # o callback
    0x802B7878: table.sym("object_state_a_802B7878", table.GLOBL), # o callback
    0x802B798C: table.sym("object_state_a_802B798C", table.GLOBL), # g callback
    0x802B7A20: table.sym("object_state_a_802B7A20"),
    0x802B7C64: table.sym("object_state_a_802B7C64", table.GLOBL), # g callback
    0x802B7D44: table.sym("object_state_a_802B7D44", table.GLOBL), # g callback
    0x802B7E68: table.sym("object_state_a_802B7E68", table.GLOBL), # data
    0x802B7EF0: table.sym("object_state_a_802B7EF0", table.GLOBL), # data
    0x802B8024: table.sym("object_state_a_802B8024", table.GLOBL), # data
    0x802B8384: table.sym("object_state_a_802B8384", table.GLOBL), # o callback
    0x802B83B0: table.sym("object_state_a_802B83B0"),
    0x802B8434: table.sym("object_state_a_802B8434"),
    0x802B84AC: table.sym("object_state_a_802B84AC", table.GLOBL), # o callback
    0x802B85B0: table.sym("object_state_a_802B85B0", table.GLOBL), # o callback
    0x802B8654: table.sym("object_state_a_802B8654"),
    0x802B8734: table.sym("object_state_a_802B8734", table.GLOBL), # o callback
    0x802B8960: table.sym("object_state_a_802B8960", table.GLOBL), # o callback
    0x802B89EC: table.sym("object_state_a_802B89EC", table.GLOBL), # o callback
    0x802B8B1C: table.sym("object_state_a_802B8B1C", table.GLOBL), # o callback
    0x802B8C38: table.sym("object_state_a_802B8C38", table.GLOBL), # o callback
    0x802B8D68: table.sym("object_state_a_802B8D68", table.GLOBL), # o callback
    0x802B8E7C: table.sym("object_state_a_802B8E7C", table.GLOBL), # o callback
    0x802B9034: table.sym("object_state_a_802B9034", table.GLOBL), # o callback
    0x802B90EC: table.sym("object_state_a_802B90EC", table.GLOBL), # o callback
    0x802B921C: table.sym("object_state_a_802B921C", table.GLOBL), # o callback
    0x802B935C: table.sym("object_state_a_802B935C", table.GLOBL), # o callback
    0x802B9790: table.sym("object_state_a_802B9790", table.GLOBL), # o callback
    0x802B98D4: table.sym("object_state_a_802B98D4"),
    0x802B98FC: table.sym("object_state_a_802B98FC", table.GLOBL), # o callback
    0x802B9A78: table.sym("object_state_a_802B9A78"),
    0x802B9AF8: table.sym("object_state_a_802B9AF8"),
    0x802B9BB4: table.sym("object_state_a_802B9BB4", table.GLOBL), # o callback
    0x802B9BD8: table.sym("object_state_a_802B9BD8", table.GLOBL), # o callback
    0x802B9E94: table.sym("object_state_a_802B9E94", table.GLOBL), # o callback
    0x802B9EFC: table.sym("object_state_a_802B9EFC"),
    0x802BA13C: table.sym("object_state_a_802BA13C"),
    0x802BA19C: table.sym("object_state_a_802BA19C", table.GLOBL), # o callback
    0x802BA1E0: table.sym("object_state_a_802BA1E0", table.GLOBL), # o callback
    0x802BA25C: table.sym("object_state_a_802BA25C", table.GLOBL), # o callback
    0x802BA2B0: table.sym("object_state_a_802BA2B0", table.GLOBL), # g callback
    0x802BA2F8: table.sym("object_state_a_802BA2F8", table.GLOBL), # o callback
    0x802BA458: table.sym("object_state_a_802BA458", table.GLOBL), # o callback
    0x802BA5BC: table.sym("object_state_a_802BA5BC", table.GLOBL), # o callback
    0x802BA608: table.sym("object_state_a_802BA608", table.GLOBL), # o callback
    0x802BA7E0: table.sym("object_state_a_802BA7E0"),
    0x802BA868: table.sym("object_state_a_802BA868"),
    0x802BA8C4: table.sym("object_state_a_802BA8C4"), # unused
    0x802BA958: table.sym("object_state_a_802BA958"),
    0x802BAB7C: table.sym("object_state_a_802BAB7C", table.GLOBL), # data
    0x802BAE40: table.sym("object_state_a_802BAE40", table.GLOBL), # data
    0x802BAEC4: table.sym("object_state_a_802BAEC4", table.GLOBL), # data
    0x802BAF10: table.sym("object_state_a_802BAF10", table.GLOBL), # data
    0x802BAF64: table.sym("object_state_a_802BAF64", table.GLOBL), # data
    0x802BB07C: table.sym("object_state_a_802BB07C", table.GLOBL), # data
    0x802BB288: table.sym("object_state_a_802BB288", table.GLOBL), # data
    0x802BB3B8: table.sym("object_state_a_802BB3B8", table.GLOBL), # data
    0x802BB798: table.sym("object_state_a_802BB798"),
    0x802BB838: table.sym("object_state_a_802BB838"), # unused
    0x802BB888: table.sym("object_state_a_802BB888"),
    0x802BBA3C: table.sym("object_state_a_802BBA3C"),
    0x802BBB98: table.sym("object_state_a_802BBB98", table.GLOBL), # o callback
    0x802BBC0C: table.sym("object_state_a_802BBC0C", table.GLOBL), # o callback
    0x802BBD6C: table.sym("object_state_a_802BBD6C"),
    0x802BBFD8: table.sym("object_state_a_802BBFD8"),
    0x802BC0F0: table.sym("object_state_a_802BC0F0", table.GLOBL), # o callback
    0x802BC22C: table.sym("object_state_a_802BC22C", table.GLOBL), # o callback
    0x802BC294: table.sym("object_state_a_802BC294", table.GLOBL), # o callback
    0x802BC348: table.sym("object_state_a_802BC348"),
    0x802BC4F4: table.sym("object_state_a_802BC4F4", table.GLOBL), # data
    0x802BC538: table.sym("object_state_a_802BC538", table.GLOBL), # data
    0x802BC590: table.sym("object_state_a_802BC590", table.GLOBL), # data
    0x802BC5FC: table.sym("object_state_a_802BC5FC", table.GLOBL), # data
    0x802BC618: table.sym("object_state_a_802BC618", table.GLOBL), # o callback
    0x802BC660: table.sym("object_state_a_802BC660", table.GLOBL), # o callback
    0x802BC728: table.sym("object_state_a_802BC728", table.GLOBL), # o callback
    0x802BC898: table.sym("object_state_a_802BC898", table.GLOBL), # o callback
    0x802BC934: table.sym("object_state_a_802BC934"),
    0x802BCA74: table.sym("object_state_a_802BCA74", table.GLOBL), # o callback
    0x802BCCE8: table.sym("object_state_a_802BCCE8"),
    0x802BCDA8: table.sym("object_state_a_802BCDA8", table.GLOBL), # o callback
    0x802BCE58: table.sym("object_state_a_802BCE58", table.GLOBL), # o callback
    0x802BCE9C: table.sym("object_state_a_802BCE9C"),
    0x802BCF40: table.sym("object_state_a_802BCF40", table.GLOBL), # o callback
    0x802BCFC4: table.sym("object_state_a_802BCFC4"),
    0x802BD058: table.sym("object_state_a_802BD058", table.GLOBL), # o callback
    0x802BD3E4: table.sym("object_state_a_802BD3E4"),
    0x802BD488: table.sym("object_state_a_802BD488", table.GLOBL), # o callback
    0x802BD5DC: table.sym("object_state_a_802BD5DC"),
    0x802BD62C: table.sym("object_state_a_802BD62C"),
    0x802BD680: table.sym("object_state_a_802BD680", table.GLOBL), # o callback
    0x802BD8D0: table.sym("object_state_a_802BD8D0"),
    0x802BD91C: table.sym("object_state_a_802BD91C"),
    0x802BDB04: table.sym("object_state_a_802BDB04", table.GLOBL), # data
    0x802BDB3C: table.sym("object_state_a_802BDB3C", table.GLOBL), # data
    0x802BDB74: table.sym("object_state_a_802BDB74", table.GLOBL), # data
    0x802BDBAC: table.sym("object_state_a_802BDBAC", table.GLOBL), # data
    0x802BDBE4: table.sym("object_state_a_802BDBE4", table.GLOBL), # data
    0x802BDC7C: table.sym("object_state_a_802BDC7C", table.GLOBL), # data
    0x802BDCC8: table.sym("object_state_a_802BDCC8", table.GLOBL), # data
    0x802BDD14: table.sym("object_state_a_802BDD14", table.GLOBL), # data
    0x802BDD68: table.sym("object_state_a_802BDD68", table.GLOBL), # o callback
    0x802BDD9C: table.sym("object_state_a_802BDD9C", table.GLOBL), # data
    0x802BDE10: table.sym("object_state_a_802BDE10"),
    0x802BDEEC: table.sym("object_state_a_802BDEEC", table.GLOBL), # data
    0x802BE034: table.sym("object_state_a_802BE034", table.GLOBL), # data
    0x802BE0B8: table.sym("object_state_a_802BE0B8"),
    0x802BE0EC: table.sym("object_state_a_802BE0EC", table.GLOBL), # data
    0x802BE150: table.sym("object_state_a_802BE150", table.GLOBL), # data
    0x802BE234: table.sym("object_state_a_802BE234", table.GLOBL), # data
    0x802BE278: table.sym("object_state_a_802BE278", table.GLOBL), # data
    0x802BE350: table.sym("object_state_a_802BE350", table.GLOBL), # data
    0x802BE49C: table.sym("object_state_a_802BE49C"),
    0x802BE50C: table.sym("object_state_a_802BE50C", table.GLOBL), # data
    0x802BE5A0: table.sym("object_state_a_802BE5A0", table.GLOBL), # o callback
    0x802BE628: table.sym("object_state_a_802BE628"),
    0x802BE6D4: table.sym("object_state_a_802BE6D4"),
    0x802BE79C: table.sym("object_state_a_802BE79C", table.GLOBL), # o callback
    0x802BE8A8: table.sym("object_state_a_802BE8A8", table.GLOBL), # data
    0x802BE8B8: table.sym("object_state_a_802BE8B8", table.GLOBL), # data
    0x802BE8F4: table.sym("object_state_a_802BE8F4"),
    0x802BE9DC: table.sym("object_state_a_802BE9DC"),
    0x802BEB14: table.sym("object_state_a_802BEB14", table.GLOBL), # data
    0x802BEB54: table.sym("object_state_a_802BEB54", table.GLOBL), # data
    0x802BEB8C: table.sym("object_state_a_802BEB8C", table.GLOBL), # data
    0x802BEBC4: table.sym("object_state_a_802BEBC4", table.GLOBL), # data
    0x802BEBFC: table.sym("object_state_a_802BEBFC", table.GLOBL), # data
    0x802BEC34: table.sym("object_state_a_802BEC34", table.GLOBL), # o callback
    0x802BECB0: table.sym("object_state_a_802BECB0"),
    0x802BED7C: table.sym("object_state_a_802BED7C", table.GLOBL),
    0x802BEDEC: table.sym("object_state_a_802BEDEC", table.GLOBL), # data
    0x802BEF8C: table.sym("object_state_a_802BEF8C", table.GLOBL), # data
    0x802BF1D8: table.sym("object_state_a_802BF1D8", table.GLOBL), # data
    0x802BF3C0: table.sym("object_state_a_802BF3C0", table.GLOBL), # o callback
    0x802BF424: table.sym("object_state_a_802BF424"),
    0x802BF474: table.sym("object_state_a_802BF474", table.GLOBL), # data
    0x802BF57C: table.sym("object_state_a_802BF57C", table.GLOBL), # data
    0x802BF648: table.sym("object_state_a_802BF648", table.GLOBL), # data
    0x802BF6E4: table.sym("object_state_a_802BF6E4", table.GLOBL), # data
    0x802BF760: table.sym("object_state_a_802BF760", table.GLOBL), # data
    0x802BF90C: table.sym("object_state_a_802BF90C", table.GLOBL), # data
    0x802BFA14: table.sym("object_state_a_802BFA14"),
    0x802BFA88: table.sym("object_state_a_802BFA88", table.GLOBL), # o callback
    0x802BFBAC: table.sym("object_state_a_802BFBAC", table.GLOBL), # g callback
    0x802BFCD8: table.sym("object_state_a_802BFCD8", table.GLOBL), # data
    0x802BFEB8: table.sym("object_state_a_802BFEB8", table.GLOBL), # data
    0x802BFF20: table.sym("object_state_a_802BFF20", table.GLOBL), # data
    0x802BFF3C: table.sym("object_state_a_802BFF3C", table.GLOBL), # o callback
    0x802BFF68: table.sym("object_state_a_802BFF68"),
    0x802C00B4: table.sym("object_state_a_802C00B4", table.GLOBL), # data
    0x802C0348: table.sym("object_state_a_802C0348", table.GLOBL), # data
    0x802C06A8: table.sym("object_state_a_802C06A8", table.GLOBL), # data
    0x802C0768: table.sym("object_state_a_802C0768", table.GLOBL), # o callback
    0x802C08A8: table.sym("object_state_a_802C08A8", table.GLOBL), # o callback
    0x802C0AAC: table.sym("object_state_a_802C0AAC", table.GLOBL), # data
    0x802C0B50: table.sym("object_state_a_802C0B50", table.GLOBL), # data
    0x802C0BA4: table.sym("object_state_a_802C0BA4", table.GLOBL), # data
    0x802C0BC4: table.sym("object_state_a_802C0BC4", table.GLOBL), # data
    0x802C0BE0: table.sym("object_state_a_802C0BE0", table.GLOBL), # o callback
    0x802C0C0C: table.sym("object_state_a_802C0C0C"),
    0x802C0CD4: table.sym("object_state_a_802C0CD4", table.GLOBL), # data
    0x802C0D44: table.sym("object_state_a_802C0D44", table.GLOBL), # data
    0x802C0F90: table.sym("object_state_a_802C0F90", table.GLOBL), # data
    0x802C1204: table.sym("object_state_a_802C1204", table.GLOBL), # o callback
    0x802C12C0: table.sym("object_state_a_802C12C0", table.GLOBL), # o callback
    0x802C1308: table.sym("object_state_a_802C1308", table.GLOBL), # data
    0x802C13EC: table.sym("object_state_a_802C13EC", table.GLOBL), # data
    0x802C14B0: table.sym("object_state_a_802C14B0", table.GLOBL), # data
    0x802C15B8: table.sym("object_state_a_802C15B8", table.GLOBL), # data
    0x802C17BC: table.sym("object_state_a_802C17BC"),
    0x802C18D0: table.sym("object_state_a_802C18D0", table.GLOBL), # data
    0x802C1988: table.sym("object_state_a_802C1988", table.GLOBL), # data
    0x802C19C0: table.sym("object_state_a_802C19C0", table.GLOBL), # o callback
    0x802C19FC: table.sym("object_state_a_802C19FC", table.GLOBL), # o callback
    0x802C1A40: table.sym("object_state_a_802C1A40", table.GLOBL), # o callback
    0x802C1A80: table.sym("object_state_a_802C1A80", table.GLOBL), # o callback
    0x802C1A90: table.sym("object_state_a_802C1A90", table.GLOBL), # o callback
    0x802C1C44: table.sym("object_state_a_802C1C44", table.GLOBL), # o callback
    0x802C1CD4: table.sym("object_state_a_802C1CD4", table.GLOBL), # o callback
    0x802C1E10: table.sym("object_state_a_802C1E10", table.GLOBL), # o callback
    0x802C2190: table.sym("object_state_a_802C2190", table.GLOBL), # o callback
    0x802C2274: table.sym("object_state_a_802C2274", table.GLOBL), # o callback
    0x802C22B8: table.sym("object_state_a_802C22B8", table.GLOBL), # o callback
    0x802C242C: table.sym("object_state_a_802C242C", table.GLOBL), # o callback
    0x802C263C: table.sym("object_state_a_802C263C", table.GLOBL), # o callback
    0x802C26F8: table.sym("object_state_a_802C26F8", table.GLOBL), # o callback
    0x802C2930: table.sym("object_state_a_802C2930", table.GLOBL), # o callback
    0x802C2A24: table.sym("object_state_a_802C2A24", table.GLOBL), # o callback
    0x802C2CE8: table.sym("object_state_a_802C2CE8"),
    0x802C2EBC: table.sym("object_state_a_802C2EBC", table.GLOBL), # data
    0x802C2FBC: table.sym("object_state_a_802C2FBC", table.GLOBL), # data
    0x802C31C4: table.sym("object_state_a_802C31C4", table.GLOBL), # data
    0x802C329C: table.sym("object_state_a_802C329C", table.GLOBL), # o callback
    0x802C32E8: table.sym("object_state_a_802C32E8", table.GLOBL), # o callback
    0x802C33F4: table.sym("object_state_a_802C33F4"),
    0x802C3440: table.sym("object_state_a_802C3440", table.GLOBL), # o callback
    0x802C3460: table.sym("object_state_a_802C3460"),
    0x802C3534: table.sym("object_state_a_802C3534"),
    0x802C3684: table.sym("object_state_a_802C3684", table.GLOBL), # o callback
    0x802C3748: table.sym("object_state_a_802C3748"),
    0x802C3884: table.sym("object_state_a_802C3884"),
    0x802C39D4: table.sym("object_state_a_802C39D4"),
    0x802C3B08: table.sym("object_state_a_802C3B08"),
    0x802C3C04: table.sym("object_state_a_802C3C04"),
    0x802C3CD0: table.sym("object_state_a_802C3CD0"),
    0x802C3D50: table.sym("object_state_a_802C3D50"),
    0x802C3D9C: table.sym("object_state_a_802C3D9C"),
    0x802C3E80: table.sym("object_state_a_802C3E80"),
    0x802C3F8C: table.sym("object_state_a_802C3F8C"),
    0x802C4118: table.sym("object_state_a_802C4118"),
    0x802C4158: table.sym("object_state_a_802C4158"),
    0x802C4210: table.sym("object_state_a_802C4210"),
    0x802C43F4: table.sym("object_state_a_802C43F4", table.GLOBL), # data
    0x802C4508: table.sym("object_state_a_802C4508", table.GLOBL), # data
    0x802C45B0: table.sym("object_state_a_802C45B0", table.GLOBL), # data
    0x802C46D8: table.sym("object_state_a_802C46D8", table.GLOBL), # data
    0x802C4720: table.sym("object_state_a_802C4720", table.GLOBL), # data
    0x802C4790: table.sym("object_state_a_802C4790", table.GLOBL), # data
    0x802C4824: table.sym("object_state_a_802C4824", table.GLOBL), # o callback
    0x802C48C0: table.sym("object_state_a_802C48C0", table.GLOBL), # data
    0x802C49F0: table.sym("object_state_a_802C49F0", table.GLOBL), # data
    0x802C4B54: table.sym("object_state_a_802C4B54", table.GLOBL), # data
    0x802C4B9C: table.sym("object_state_a_802C4B9C"),
    0x802C4BD4: table.sym("object_state_a_802C4BD4"),
    0x802C4C10: table.sym("object_state_a_802C4C10"),
    0x802C4C70: table.sym("object_state_a_802C4C70", table.GLOBL), # data
    0x802C4DD4: table.sym("object_state_a_802C4DD4", table.GLOBL), # data
    0x802C4F30: table.sym("object_state_a_802C4F30", table.GLOBL), # o callback
    0x802C4FB0: table.sym("object_state_a_802C4FB0", table.GLOBL), # data
    0x802C503C: table.sym("object_state_a_802C503C", table.GLOBL), # data
    0x802C50D8: table.sym("object_state_a_802C50D8", table.GLOBL), # data
    0x802C5120: table.sym("object_state_a_802C5120", table.GLOBL), # data
    0x802C515C: table.sym("object_state_a_802C515C", table.GLOBL), # o callback
    0x802C51D4: table.sym("object_state_a_802C51D4", table.GLOBL), # o callback
    0x802C5224: table.sym("object_state_a_802C5224", table.GLOBL), # o callback
    0x802C53CC: table.sym("object_state_a_802C53CC"),
    0x802C53EC: table.sym("object_state_a_802C53EC", table.GLOBL), # o callback
    0x802C5414: table.sym("object_state_a_802C5414", table.GLOBL), # o callback
    0x802C5688: table.sym("object_state_a_802C5688", table.GLOBL), # o callback
    0x802C5890: table.sym("object_state_a_802C5890", table.GLOBL), # o callback
    0x802C5A38: table.sym("object_state_a_802C5A38", table.GLOBL), # o callback
    0x802C5B54: table.sym("object_state_a_802C5B54"),
    0x802C5CA8: table.sym("object_state_a_802C5CA8", table.GLOBL), # o callback
    0x802C5DC0: table.sym("object_state_a_802C5DC0", table.GLOBL), # o callback
    0x802C5F48: table.sym("object_state_a_802C5F48", table.GLOBL), # o callback
    0x802C5FDC: table.sym("object_state_a_802C5FDC", table.GLOBL), # o callback
    0x802C6050: table.sym("object_state_a_802C6050", table.GLOBL), # o callback
    0x802C60AC: table.sym("object_state_a_802C60AC", table.GLOBL), # o callback
    0x802C6150: table.sym("object_state_a_802C6150"),
    0x802C61D4: table.sym("object_state_a_802C61D4"),
    0x802C6278: table.sym("object_state_a_802C6278"),
    0x802C62BC: table.sym("object_state_a_802C62BC"),
    0x802C6328: table.sym("object_state_a_802C6328"),
    0x802C6348: table.sym("object_state_a_802C6348", table.GLOBL), # o callback
    0x802C63E8: table.sym("object_state_a_802C63E8", table.GLOBL), # o callback
    0x802C64A4: table.sym("object_state_a_802C64A4", table.GLOBL), # o callback
    0x802C6538: table.sym("object_state_a_802C6538"),
    0x802C65C0: table.sym("object_state_a_802C65C0", table.GLOBL), # o callback
    0x802C6B6C: table.sym("object_state_a_802C6B6C", table.GLOBL), # o callback
    0x802C6CA0: table.sym("object_state_a_802C6CA0"),
    0x802C6D6C: table.sym("object_state_a_802C6D6C", table.GLOBL), # data
    0x802C6EC8: table.sym("object_state_a_802C6EC8", table.GLOBL), # data
    0x802C6FB0: table.sym("object_state_a_802C6FB0", table.GLOBL), # data
    0x802C710C: table.sym("object_state_a_802C710C", table.GLOBL), # data
    0x802C7254: table.sym("object_state_a_802C7254", table.GLOBL), # data
    0x802C72B4: table.sym("object_state_a_802C72B4", table.GLOBL), # data
    0x802C7380: table.sym("object_state_a_802C7380", table.GLOBL), # data
    0x802C7428: table.sym("object_state_a_802C7428"),
    0x802C75FC: table.sym("object_state_a_802C75FC"),
    0x802C76D4: table.sym("object_state_a_802C76D4", table.GLOBL), # data
    0x802C7858: table.sym("object_state_a_802C7858", table.GLOBL), # data
    0x802C7998: table.sym("object_state_a_802C7998", table.GLOBL), # data
    0x802C79D8: table.sym("object_state_a_802C79D8", table.GLOBL), # o callback
    0x802C7A70: table.sym("object_state_a_802C7A70", table.GLOBL), # o callback
    0x802C7B14: table.sym("object_state_a_802C7B14", table.GLOBL), # o callback
    0x802C7CAC: table.sym("object_state_a_802C7CAC", table.GLOBL), # o callback
    0x802C7D40: table.sym("object_state_a_802C7D40", table.GLOBL), # o callback
    0x802C7D90: table.sym("object_state_a_802C7D90", table.GLOBL), # o callback
    0x802C7DFC: table.sym("object_state_a_802C7DFC", table.GLOBL), # o callback
    0x802C7E5C: table.sym("object_state_a_802C7E5C", table.GLOBL), # o callback
    0x802C7F98: table.sym("object_state_a_802C7F98", table.GLOBL), # o callback
    0x802C81B4: table.sym("object_state_a_802C81B4", table.GLOBL),
    0x802C834C: table.sym("object_state_a_802C834C", table.GLOBL), # o callback
    0x802C85A4: table.sym("object_state_a_802C85A4"),
    0x802C863C: table.sym("object_state_a_802C863C", table.GLOBL), # o callback

    # src/object_move.S
    0x802C89F0: table.sym("object_move_802C89F0", table.GLOBL),
    0x802C8B4C: table.sym("object_move_802C8B4C", table.GLOBL),
    0x802C8B8C: table.sym("object_move_802C8B8C", table.GLOBL),
    0x802C8BC8: table.sym("object_move_802C8BC8", table.GLOBL),
    0x802C8EC0: table.sym("object_move_802C8EC0", table.GLOBL),
    0x802C8F28: table.sym("object_move_802C8F28", table.GLOBL),

    # src/object_touch.S
    0x802C8F40: table.sym("object_touch_802C8F40"), # unused
    0x802C8FE4: table.sym("object_touch_802C8FE4"),
    0x802C91EC: table.sym("object_touch_802C91EC"),
    0x802C9388: table.sym("object_touch_802C9388"),
    0x802C93F8: table.sym("object_touch_802C93F8"),
    0x802C94AC: table.sym("object_touch_802C94AC"),
    0x802C95B4: table.sym("object_touch_802C95B4"),
    0x802C9630: table.sym("object_touch_802C9630"),
    0x802C9724: table.sym("object_touch_802C9724", table.GLOBL),

    # src/object_list.S
    0x802C97D0: table.sym("object_list_802C97D0"), # unused
    0x802C9840: table.sym("object_list_802C9840"), # unused
    0x802C98A4: table.sym("object_list_802C98A4"),
    0x802C9950: table.sym("object_list_802C9950"), # unused
    0x802C9984: table.sym("object_list_802C9984"),
    0x802C99B8: table.sym("object_list_802C99B8", table.GLOBL),
    0x802C9A3C: table.sym("object_list_802C9A3C", table.GLOBL),
    0x802C9AD8: table.sym("object_list_802C9AD8"),
    0x802C9B68: table.sym("object_list_802C9B68", table.GLOBL),
    0x802C9C00: table.sym("object_list_802C9C00"),
    0x802C9E5C: table.sym("object_list_802C9E5C"),
    0x802C9F04: table.sym("object_list_802C9F04", table.GLOBL),
    0x802CA028: table.sym("object_list_802CA028", table.GLOBL),

    # src/object_sfx.S
    0x802CA040: table.sym("object_sfx_802CA040", table.GLOBL),
    0x802CA144: table.sym("object_sfx_802CA144", table.GLOBL),
    0x802CA190: table.sym("object_sfx_802CA190", table.GLOBL),
    0x802CA1E0: table.sym("object_sfx_802CA1E0", table.GLOBL),
    0x802CA230: table.sym("object_sfx_802CA230"), # unused
    0x802CA2D4: table.sym("object_sfx_802CA2D4"), # unused

    # src/coin.S
    0x802CA370: table.sym("coin_802CA370"), # unused
    0x802CA380: table.sym("coin_802CA380"), # unused

    # src/door.S
    0x802CA390: table.sym("door_802CA390"), # unused
    0x802CA3A0: table.sym("door_802CA3A0"), # unused

    # src/object_debug.S
    0x802CA3B0: table.sym("object_debug_802CA3B0", table.GLOBL),
    0x802CA3E0: table.sym("object_debug_802CA3E0", table.GLOBL),
    0x802CA418: table.sym("object_debug_802CA418"),
    0x802CA460: table.sym("object_debug_802CA460"),
    0x802CA51C: table.sym("object_debug_802CA51C", table.GLOBL),
    0x802CA568: table.sym("object_debug_802CA568", table.GLOBL),
    0x802CA5B8: table.sym("object_debug_802CA5B8", table.GLOBL),
    0x802CA618: table.sym("object_debug_802CA618", table.GLOBL),
    0x802CA680: table.sym("object_debug_802CA680"),
    0x802CA6D0: table.sym("object_debug_802CA6D0"),
    0x802CA8E8: table.sym("object_debug_802CA8E8"),
    0x802CA918: table.sym("object_debug_802CA918"),
    0x802CA94C: table.sym("object_debug_802CA94C"),
    0x802CA990: table.sym("object_debug_802CA990"),
    0x802CAA6C: table.sym("object_debug_802CAA6C"),
    0x802CAAA8: table.sym("object_debug_802CAAA8"),
    0x802CAAE4: table.sym("object_debug_802CAAE4"),
    0x802CABAC: table.sym("object_debug_802CABAC", table.GLOBL),
    0x802CAC20: table.sym("object_debug_802CAC20", table.GLOBL),
    0x802CACC8: table.sym("object_debug_802CACC8"), # unused
    0x802CADC8: table.sym("object_debug_802CADC8"), # unused
    0x802CAE9C: table.sym("object_debug_802CAE9C"), # unused
    0x802CB0B0: table.sym("object_debug_802CB0B0", table.GLOBL),
    0x802CB0C0: table.sym("object_debug_802CB0C0", table.GLOBL),
    0x802CB1C0: table.sym("object_debug_802CB1C0", table.GLOBL), # o callback
    0x802CB264: table.sym("object_debug_802CB264", table.GLOBL), # o callback
    0x802CB394: table.sym("object_debug_802CB394"), # unused
    0x802CB564: table.sym("object_debug_802CB564"), # unused

    # src/wipe.S
    0x802CB5C0: table.sym("wipe_802CB5C0"),
    0x802CB640: table.sym("wipe_802CB640"),
    0x802CB894: table.sym("wipe_802CB894"),
    0x802CBA18: table.sym("wipe_802CBA18"),
    0x802CBBC4: table.sym("wipe_802CBBC4"),
    0x802CBC20: table.sym("wipe_802CBC20"),
    0x802CBC7C: table.sym("wipe_802CBC7C"),
    0x802CBD54: table.sym("wipe_802CBD54"),
    0x802CBE64: table.sym("wipe_802CBE64"),
    0x802CBEE0: table.sym("wipe_802CBEE0"),
    0x802CBF64: table.sym("wipe_802CBF64"),
    0x802CBFE8: table.sym("wipe_802CBFE8"),
    0x802CC180: table.sym("wipe_802CC180"),
    0x802CC4D8: table.sym("wipe_802CC4D8"),
    0x802CCBE8: table.sym("wipe_802CCBE8", table.GLOBL),
    0x802CCDC8: table.sym("wipe_802CCDC8"),
    0x802CD1E8: table.sym("wipe_802CD1E8", table.GLOBL), # g callback

    # src/shadow.S
    0x802CD280: table.sym("shadow_802CD280"),
    0x802CD328: table.sym("shadow_802CD328"),
    0x802CD388: table.sym("shadow_802CD388"),
    0x802CD444: table.sym("shadow_802CD444"),
    0x802CD48C: table.sym("shadow_802CD48C"),
    0x802CD614: table.sym("shadow_802CD614"),
    0x802CD6C4: table.sym("shadow_802CD6C4"),
    0x802CD938: table.sym("shadow_802CD938"),
    0x802CD988: table.sym("shadow_802CD988"),
    0x802CD9EC: table.sym("shadow_802CD9EC"),
    0x802CDB20: table.sym("shadow_802CDB20"),
    0x802CDB74: table.sym("shadow_802CDB74"),
    0x802CDC40: table.sym("shadow_802CDC40"),
    0x802CDE94: table.sym("shadow_802CDE94"),
    0x802CDF3C: table.sym("shadow_802CDF3C"),
    0x802CE128: table.sym("shadow_802CE128"),
    0x802CE2BC: table.sym("shadow_802CE2BC"),
    0x802CE3EC: table.sym("shadow_802CE3EC"),
    0x802CE524: table.sym("shadow_802CE524"),
    0x802CE690: table.sym("shadow_802CE690"),
    0x802CE79C: table.sym("shadow_802CE79C"),
    0x802CE9D0: table.sym("shadow_802CE9D0"),
    0x802CEAE8: table.sym("shadow_802CEAE8"),
    0x802CEC04: table.sym("shadow_802CEC04"),
    0x802CEDC0: table.sym("shadow_802CEDC0"),
    0x802CEF6C: table.sym("shadow_802CEF6C"),
    0x802CF080: table.sym("shadow_802CF080"),
    0x802CF1F0: table.sym("shadow_802CF1F0"),
    0x802CF34C: table.sym("shadow_802CF34C", table.GLOBL),

    # src/background.S
    0x802CF5B0: table.sym("background_802CF5B0"),
    0x802CF69C: table.sym("background_802CF69C"),
    0x802CF77C: table.sym("background_802CF77C"),
    0x802CF804: table.sym("background_802CF804"),
    0x802CFA2C: table.sym("background_802CFA2C"),
    0x802CFC68: table.sym("background_802CFC68"),
    0x802CFD88: table.sym("background_802CFD88"),
    0x802CFEF4: table.sym("background_802CFEF4", table.GLOBL),

    # src/scroll.S
    0x802D0080: table.sym("scroll_802D0080", table.GLOBL), # g callback
    0x802D01E0: table.sym("scroll_802D01E0", table.GLOBL), # g callback
    0x802D0254: table.sym("scroll_802D0254"),
    0x802D0484: table.sym("scroll_802D0484"),
    0x802D0A84: table.sym("scroll_802D0A84"),
    0x802D0BB0: table.sym("scroll_802D0BB0"),
    0x802D0C84: table.sym("scroll_802D0C84"),
    0x802D0F28: table.sym("scroll_802D0F28"),
    0x802D104C: table.sym("scroll_802D104C", table.GLOBL), # g callback
    0x802D1330: table.sym("scroll_802D1330"),
    0x802D13CC: table.sym("scroll_802D13CC"),
    0x802D1574: table.sym("scroll_802D1574"),
    0x802D18B4: table.sym("scroll_802D18B4"),
    0x802D1B70: table.sym("scroll_802D1B70", table.GLOBL), # g callback
    0x802D1CDC: table.sym("scroll_802D1CDC", table.GLOBL), # g callback
    0x802D1E48: table.sym("scroll_802D1E48", table.GLOBL), # g callback
    0x802D1FA8: table.sym("scroll_802D1FA8", table.GLOBL), # g callback
    0x802D2108: table.sym("scroll_802D2108", table.GLOBL), # g callback

    # src/object_gfx.S
    0x802D2210: table.sym("object_gfx_802D2210", table.GLOBL),
    0x802D22C4: table.sym("object_gfx_802D22C4", table.GLOBL),
    0x802D2360: table.sym("object_gfx_802D2360", table.GLOBL), # g callback
    0x802D2470: table.sym("object_gfx_802D2470", table.GLOBL), # g callback
    0x802D2520: table.sym("object_gfx_802D2520", table.GLOBL), # g callback
    0x802D28CC: table.sym("object_gfx_802D28CC", table.GLOBL), # g callback

    # src/ripple.S
    0x802D29C0: table.sym("ripple_802D29C0"),
    0x802D2A74: table.sym("ripple_802D2A74"),
    0x802D2B08: table.sym("ripple_802D2B08"),
    0x802D2B84: table.sym("ripple_802D2B84"),
    0x802D2C40: table.sym("ripple_802D2C40"),
    0x802D2D80: table.sym("ripple_802D2D80"),
    0x802D2DFC: table.sym("ripple_802D2DFC"),
    0x802D2EB8: table.sym("ripple_802D2EB8"),
    0x802D2FFC: table.sym("ripple_802D2FFC"),
    0x802D319C: table.sym("ripple_802D319C"),
    0x802D327C: table.sym("ripple_802D327C"),
    0x802D341C: table.sym("ripple_802D341C"),
    0x802D34FC: table.sym("ripple_802D34FC"),
    0x802D36AC: table.sym("ripple_802D36AC"),
    0x802D379C: table.sym("ripple_802D379C"),
    0x802D393C: table.sym("ripple_802D393C"),
    0x802D3A2C: table.sym("ripple_802D3A2C"),
    0x802D3BEC: table.sym("ripple_802D3BEC"),
    0x802D3CEC: table.sym("ripple_802D3CEC"),
    0x802D3E6C: table.sym("ripple_802D3E6C"),
    0x802D3EE4: table.sym("ripple_802D3EE4"),
    0x802D404C: table.sym("ripple_802D404C"),
    0x802D43F8: table.sym("ripple_802D43F8"),
    0x802D44BC: table.sym("ripple_802D44BC"),
    0x802D47D0: table.sym("ripple_802D47D0"),
    0x802D4EDC: table.sym("ripple_802D4EDC"),
    0x802D50DC: table.sym("ripple_802D50DC"),
    0x802D5354: table.sym("ripple_802D5354"),
    0x802D556C: table.sym("ripple_802D556C"),
    0x802D568C: table.sym("ripple_802D568C"),
    0x802D5778: table.sym("ripple_802D5778"),
    0x802D57A8: table.sym("ripple_802D57A8"),
    0x802D58E4: table.sym("ripple_802D58E4"),
    0x802D593C: table.sym("ripple_802D593C"),
    0x802D59A8: table.sym("ripple_802D59A8"),
    0x802D5AA0: table.sym("ripple_802D5AA0"),
    0x802D5B98: table.sym("ripple_802D5B98", table.GLOBL), # g callback
    0x802D5D0C: table.sym("ripple_802D5D0C", table.GLOBL), # g callback

    # src/print.S
    0x802D5E00: table.sym("print_802D5E00"),
    0x802D5E54: table.sym("print_802D5E54"),
    0x802D6144: table.sym("print_802D6144"),
    0x802D62D8: table.sym("print_int", table.GLOBL),
    0x802D6554: table.sym("print", table.GLOBL),
    0x802D66C0: table.sym("print_centre", table.GLOBL),
    0x802D6858: table.sym("print_802D6858"),
    0x802D69F8: table.sym("print_802D69F8"),
    0x802D6ACC: table.sym("print_802D6ACC"),
    0x802D6B3C: table.sym("print_802D6B3C"),
    0x802D6C88: table.sym("print_draw", table.GLOBL),

    # src/message.S
    0x802D6F20: table.sym("message_802D6F20"),
    0x802D7070: table.sym("message_802D7070", table.GLOBL),
    0x802D7174: table.sym("message_802D7174"),
    0x802D7280: table.sym("message_802D7280"),
    0x802D7384: table.sym("message_802D7384", table.GLOBL),
    0x802D7480: table.sym("message_802D7480"), # unused
    0x802D75DC: table.sym("message_802D75DC"),
    0x802D76C8: table.sym("message_802D76C8"),
    0x802D77DC: table.sym("message_802D77DC", table.GLOBL),
    0x802D7B84: table.sym("message_802D7B84", table.GLOBL),
    0x802D7E88: table.sym("message_802D7E88", table.GLOBL),
    0x802D82D4: table.sym("message_802D82D4"),
    0x802D862C: table.sym("message_802D862C", table.GLOBL),
    0x802D8844: table.sym("message_802D8844", table.GLOBL),
    0x802D8934: table.sym("message_802D8934"),
    0x802D89B8: table.sym("message_802D89B8", table.GLOBL),
    0x802D8A80: table.sym("message_802D8A80"),
    0x802D8B34: table.sym("message_802D8B34", table.GLOBL),
    0x802D8C6C: table.sym("message_802D8C6C", table.GLOBL),
    0x802D8C88: table.sym("message_802D8C88", table.GLOBL),
    0x802D8CC4: table.sym("message_802D8CC4", table.GLOBL),
    0x802D8D08: table.sym("message_802D8D08", table.GLOBL),
    0x802D8D48: table.sym("message_802D8D48", table.GLOBL),
    0x802D8D90: table.sym("message_802D8D90", table.GLOBL),
    0x802D8E2C: table.sym("message_802D8E2C"),
    0x802D9148: table.sym("message_802D9148"),
    0x802D9388: table.sym("message_802D9388"),
    0x802D944C: table.sym("message_802D944C"),
    0x802D9634: table.sym("message_802D9634"),
    0x802D9800: table.sym("message_802D9800"),
    0x802D982C: table.sym("message_802D982C"),
    0x802D9CB0: table.sym("message_802D9CB0"),
    0x802D9DFC: table.sym("message_802D9DFC"),
    0x802D9F84: table.sym("message_802D9F84"),
    0x802DA1AC: table.sym("message_802DA1AC"),
    0x802DA810: table.sym("message_802DA810", table.GLOBL),
    0x802DA844: table.sym("message_802DA844", table.GLOBL),
    0x802DA85C: table.sym("message_802DA85C", table.GLOBL),
    0x802DA8E4: table.sym("message_802DA8E4", table.GLOBL),
    0x802DA964: table.sym("message_802DA964"),
    0x802DAA34: table.sym("message_802DAA34", table.GLOBL),
    0x802DAAE4: table.sym("message_802DAAE4", table.GLOBL),
    0x802DAB58: table.sym("message_802DAB58", table.GLOBL),
    0x802DAD54: table.sym("message_802DAD54"),
    0x802DB08C: table.sym("message_802DB08C", table.GLOBL),
    0x802DB350: table.sym("message_802DB350", table.GLOBL),
    0x802DB368: table.sym("message_802DB368"),
    0x802DB3B8: table.sym("message_802DB3B8"),
    0x802DB498: table.sym("message_802DB498"),
    0x802DB6E8: table.sym("message_802DB6E8"),
    0x802DB760: table.sym("message_802DB760"),
    0x802DBB24: table.sym("message_802DBB24"),
    0x802DBE68: table.sym("message_802DBE68"),
    0x802DC15C: table.sym("message_802DC15C"),
    0x802DC418: table.sym("message_802DC418"),
    0x802DC478: table.sym("message_802DC478"),
    0x802DC570: table.sym("message_802DC570"),
    0x802DC718: table.sym("message_802DC718"),
    0x802DCA88: table.sym("message_802DCA88"),
    0x802DCD04: table.sym("message_802DCD04"),
    0x802DCF30: table.sym("message_802DCF30"),
    0x802DD194: table.sym("message_802DD194"),
    0x802DD210: table.sym("message_802DD210"),
    0x802DD838: table.sym("message_802DD838"),
    0x802DDAE0: table.sym("message_802DDAE0"),
    0x802DDCA4: table.sym("message_802DDCA4", table.GLOBL),

    # src/particle_snow.S
    0x802DDDF0: table.sym("particle_snow_802DDDF0"),
    0x802DDF38: table.sym("particle_snow_802DDF38"),
    0x802DE0BC: table.sym("particle_snow_802DE0BC"),
    0x802DE114: table.sym("particle_snow_802DE114", table.GLOBL),
    0x802DE23C: table.sym("particle_snow_802DE23C"),
    0x802DE360: table.sym("particle_snow_802DE360"),
    0x802DE458: table.sym("particle_snow_802DE458"),
    0x802DE888: table.sym("particle_snow_802DE888"),
    0x802DECD4: table.sym("particle_snow_802DECD4"), # unused
    0x802DED38: table.sym("particle_snow_802DED38"),
    0x802DEF2C: table.sym("particle_snow_802DEF2C", table.GLOBL),
    0x802DF334: table.sym("particle_snow_802DF334"),
    0x802DF748: table.sym("particle_snow_802DF748"),
    0x802DFBC8: table.sym("particle_snow_802DFBC8", table.GLOBL),

    # src/particle_lava.S
    0x802DFD50: table.sym("particle_lava_802DFD50"),
    0x802DFE00: table.sym("particle_lava_802DFE00"),
    0x802DFE80: table.sym("particle_lava_802DFE80"),
    0x802E0120: table.sym("particle_lava_802E0120"),
    0x802E048C: table.sym("particle_lava_802E048C"),
    0x802E065C: table.sym("particle_lava_802E065C"),
    0x802E08A8: table.sym("particle_lava_802E08A8"),
    0x802E0934: table.sym("particle_lava_802E0934"),
    0x802E0E24: table.sym("particle_lava_802E0E24"),
    0x802E0EB8: table.sym("particle_lava_802E0EB8"),
    0x802E1238: table.sym("particle_lava_802E1238"),
    0x802E1414: table.sym("particle_lava_802E1414"),
    0x802E1618: table.sym("particle_lava_802E1618"),
    0x802E1A20: table.sym("particle_lava_802E1A20"),
    0x802E1BB8: table.sym("particle_lava_802E1BB8"),
    0x802E1ED8: table.sym("particle_lava_802E1ED8"),
    0x802E1F48: table.sym("particle_lava_802E1F48", table.GLOBL),

    # src/obj_data.S
    0x802E20A0: table.sym("obj_data_802E20A0"),
    0x802E2134: table.sym("obj_data_802E2134"),
    0x802E21DC: table.sym("obj_data_802E21DC"),
    0x802E2284: table.sym("obj_data_802E2284"),
    0x802E233C: table.sym("obj_data_802E233C"), # unused
    0x802E2414: table.sym("obj_data_802E2414", table.GLOBL),
    0x802E2690: table.sym("obj_data_802E2690", table.GLOBL),
    0x802E28EC: table.sym("obj_data_802E28EC", table.GLOBL),

    # src/hud.S
    0x802E2CF0: table.sym("hud_802E2CF0"),
    0x802E2E58: table.sym("hud_802E2E58"),
    0x802E30B4: table.sym("hud_802E30B4"),
    0x802E3214: table.sym("hud_802E3214"),
    0x802E33B8: table.sym("hud_802E33B8"),
    0x802E3430: table.sym("hud_802E3430"),
    0x802E34E4: table.sym("hud_802E34E4"),
    0x802E352C: table.sym("hud_802E352C"),
    0x802E3654: table.sym("hud_802E3654"),
    0x802E3744: table.sym("hud_802E3744"),
    0x802E37A8: table.sym("hud_802E37A8"),
    0x802E380C: table.sym("hud_802E380C"),
    0x802E38E4: table.sym("hud_802E38E4"),
    0x802E395C: table.sym("hud_802E395C"),
    0x802E3B1C: table.sym("hud_802E3B1C", table.GLOBL),
    0x802E3B3C: table.sym("hud_802E3B3C"),
    0x802E3D2C: table.sym("hud_802E3D2C", table.GLOBL),

    # src/object_state_b.S
    0x802E3E50: table.sym("object_state_b_802E3E50", table.GLOBL),
    0x802E3E68: table.sym("object_state_b_802E3E68"), # unused
    0x802E3F68: table.sym("object_state_b_802E3F68"),
    0x802E3FAC: table.sym("object_state_b_802E3FAC"),
    0x802E405C: table.sym("object_state_b_802E405C"),
    0x802E41A4: table.sym("object_state_b_802E41A4"),
    0x802E42E0: table.sym("object_state_b_802E42E0"),
    0x802E43E4: table.sym("object_state_b_802E43E4"),
    0x802E445C: table.sym("object_state_b_802E445C"),
    0x802E4814: table.sym("object_state_b_802E4814"),
    0x802E4CEC: table.sym("object_state_b_802E4CEC"),
    0x802E4D88: table.sym("object_state_b_802E4D88"),
    0x802E4E90: table.sym("object_state_b_802E4E90"),
    0x802E5114: table.sym("object_state_b_802E5114"),
    0x802E5160: table.sym("object_state_b_802E5160"),
    0x802E5208: table.sym("object_state_b_802E5208"),
    0x802E52B8: table.sym("object_state_b_802E52B8"),
    0x802E5360: table.sym("object_state_b_802E5360"),
    0x802E53F4: table.sym("object_state_b_802E53F4"),
    0x802E54B0: table.sym("object_state_b_802E54B0"),
    0x802E55D0: table.sym("object_state_b_802E55D0"),
    0x802E569C: table.sym("object_state_b_802E569C"),
    0x802E5760: table.sym("object_state_b_802E5760"),
    0x802E5824: table.sym("object_state_b_802E5824"),
    0x802E58B4: table.sym("object_state_b_802E58B4"),
    0x802E5948: table.sym("object_state_b_802E5948"),
    0x802E5A80: table.sym("object_state_b_802E5A80"),
    0x802E5B18: table.sym("object_state_b_802E5B18"),
    0x802E5C6C: table.sym("object_state_b_802E5C6C"),
    0x802E5D04: table.sym("object_state_b_802E5D04"), # unused
    0x802E5DE8: table.sym("object_state_b_802E5DE8"),
    0x802E5E6C: table.sym("object_state_b_802E5E6C"),
    0x802E5EA4: table.sym("object_state_b_802E5EA4"),
    0x802E5EE8: table.sym("object_state_b_802E5EE8", table.GLOBL), # o callback
    0x802E5F64: table.sym("object_state_b_802E5F64", table.GLOBL), # o callback
    0x802E6098: table.sym("object_state_b_802E6098", table.GLOBL), # o callback
    0x802E6114: table.sym("object_state_b_802E6114", table.GLOBL), # o callback
    0x802E62A4: table.sym("object_state_b_802E62A4", table.GLOBL), # o callback
    0x802E631C: table.sym("object_state_b_802E631C"),
    0x802E63EC: table.sym("object_state_b_802E63EC"),
    0x802E6474: table.sym("object_state_b_802E6474", table.GLOBL), # o callback
    0x802E6628: table.sym("object_state_b_802E6628", table.GLOBL), # o callback
    0x802E6790: table.sym("object_state_b_802E6790", table.GLOBL), # o callback
    0x802E67DC: table.sym("object_state_b_802E67DC", table.GLOBL), # o callback
    0x802E6A2C: table.sym("object_state_b_802E6A2C", table.GLOBL), # o callback
    0x802E6A8C: table.sym("object_state_b_802E6A8C"),
    0x802E6AF8: table.sym("object_state_b_802E6AF8"),
    0x802E6BD4: table.sym("object_state_b_802E6BD4"),
    0x802E6CF0: table.sym("object_state_b_802E6CF0"),
    0x802E6DC8: table.sym("object_state_b_802E6DC8"),
    0x802E6E84: table.sym("object_state_b_802E6E84"),
    0x802E6ED8: table.sym("object_state_b_802E6ED8"),
    0x802E7020: table.sym("object_state_b_802E7020"),
    0x802E7134: table.sym("object_state_b_802E7134"),
    0x802E7180: table.sym("object_state_b_802E7180"),
    0x802E7220: table.sym("object_state_b_802E7220"),
    0x802E7280: table.sym("object_state_b_802E7280"),
    0x802E7324: table.sym("object_state_b_802E7324"),
    0x802E742C: table.sym("object_state_b_802E742C", table.GLOBL), # o callback
    0x802E75A0: table.sym("object_state_b_802E75A0", table.GLOBL), # o callback
    0x802E76AC: table.sym("object_state_b_802E76AC", table.GLOBL), # o callback
    0x802E770C: table.sym("object_state_b_802E770C"),
    0x802E7814: table.sym("object_state_b_802E7814"),
    0x802E79DC: table.sym("object_state_b_802E79DC"),
    0x802E7B00: table.sym("object_state_b_802E7B00"),
    0x802E7BB0: table.sym("object_state_b_802E7BB0"),
    0x802E7C4C: table.sym("object_state_b_802E7C4C", table.GLOBL), # o callback
    0x802E7C90: table.sym("object_state_b_802E7C90", table.GLOBL), # o callback
    0x802E7D4C: table.sym("object_state_b_802E7D4C"),
    0x802E7E54: table.sym("object_state_b_802E7E54", table.GLOBL), # o callback
    0x802E7F70: table.sym("object_state_b_802E7F70", table.GLOBL), # o callback
    0x802E7FB8: table.sym("object_state_b_802E7FB8"),
    0x802E7FEC: table.sym("object_state_b_802E7FEC"),
    0x802E80DC: table.sym("object_state_b_802E80DC", table.GLOBL), # o callback
    0x802E82B0: table.sym("object_state_b_802E82B0", table.GLOBL), # o callback
    0x802E8388: table.sym("object_state_b_802E8388", table.GLOBL), # o callback
    0x802E844C: table.sym("object_state_b_802E844C"),
    0x802E84CC: table.sym("object_state_b_802E84CC"),
    0x802E8618: table.sym("object_state_b_802E8618"),
    0x802E885C: table.sym("object_state_b_802E885C"),
    0x802E8920: table.sym("object_state_b_802E8920"),
    0x802E89D4: table.sym("object_state_b_802E89D4", table.GLOBL), # o callback
    0x802E8AE4: table.sym("object_state_b_802E8AE4", table.GLOBL), # o callback
    0x802E8C18: table.sym("object_state_b_802E8C18"),
    0x802E8D98: table.sym("object_state_b_802E8D98"),
    0x802E8ECC: table.sym("object_state_b_802E8ECC", table.GLOBL), # o callback
    0x802E8F68: table.sym("object_state_b_802E8F68", table.GLOBL), # o callback
    0x802E9018: table.sym("object_state_b_802E9018"),
    0x802E9278: table.sym("object_state_b_802E9278"),
    0x802E9470: table.sym("object_state_b_802E9470"),
    0x802E94E4: table.sym("object_state_b_802E94E4"),
    0x802E9548: table.sym("object_state_b_802E9548"),
    0x802E96C8: table.sym("object_state_b_802E96C8", table.GLOBL), # o callback
    0x802E9764: table.sym("object_state_b_802E9764", table.GLOBL), # o callback
    0x802E97FC: table.sym("object_state_b_802E97FC"),
    0x802E98C0: table.sym("object_state_b_802E98C0"),
    0x802E9A4C: table.sym("object_state_b_802E9A4C"),
    0x802E9CF4: table.sym("object_state_b_802E9CF4"),
    0x802E9D98: table.sym("object_state_b_802E9D98"),
    0x802E9F60: table.sym("object_state_b_802E9F60"),
    0x802EA144: table.sym("object_state_b_802EA144"),
    0x802EA258: table.sym("object_state_b_802EA258"),
    0x802EA3F0: table.sym("object_state_b_802EA3F0"),
    0x802EA4EC: table.sym("object_state_b_802EA4EC"),
    0x802EA588: table.sym("object_state_b_802EA588", table.GLOBL), # o callback
    0x802EA6A8: table.sym("object_state_b_802EA6A8", table.GLOBL), # o callback
    0x802EA6F8: table.sym("object_state_b_802EA6F8"),
    0x802EA75C: table.sym("object_state_b_802EA75C"),
    0x802EA7E0: table.sym("object_state_b_802EA7E0", table.GLOBL), # o callback
    0x802EA888: table.sym("object_state_b_802EA888", table.GLOBL), # o callback
    0x802EA934: table.sym("object_state_b_802EA934", table.GLOBL), # o callback
    0x802EAA10: table.sym("object_state_b_802EAA10", table.GLOBL), # o callback
    0x802EAA50: table.sym("object_state_b_802EAA50", table.GLOBL), # o callback
    0x802EAA8C: table.sym("object_state_b_802EAA8C", table.GLOBL), # o callback
    0x802EAAD0: table.sym("object_state_b_802EAAD0", table.GLOBL), # o callback
    0x802EABF0: table.sym("object_state_b_802EABF0", table.GLOBL), # o callback
    0x802EAC3C: table.sym("object_state_b_802EAC3C", table.GLOBL), # o callback
    0x802EAD3C: table.sym("object_state_b_802EAD3C", table.GLOBL), # o callback
    0x802EAEF8: table.sym("object_state_b_802EAEF8", table.GLOBL), # o callback
    0x802EAF84: table.sym("object_state_b_802EAF84"),
    0x802EB05C: table.sym("object_state_b_802EB05C", table.GLOBL), # o callback
    0x802EB104: table.sym("object_state_b_802EB104", table.GLOBL), # o callback
    0x802EB1C0: table.sym("object_state_b_802EB1C0"),
    0x802EB288: table.sym("object_state_b_802EB288"),
    0x802EB3F0: table.sym("object_state_b_802EB3F0"),
    0x802EB510: table.sym("object_state_b_802EB510"),
    0x802EB5C4: table.sym("object_state_b_802EB5C4"),
    0x802EB630: table.sym("object_state_b_802EB630"),
    0x802EB744: table.sym("object_state_b_802EB744"),
    0x802EB7E0: table.sym("object_state_b_802EB7E0"),
    0x802EB8B0: table.sym("object_state_b_802EB8B0"),
    0x802EB9D0: table.sym("object_state_b_802EB9D0", table.GLOBL), # o callback
    0x802EBB74: table.sym("object_state_b_802EBB74"),
    0x802EBC00: table.sym("object_state_b_802EBC00", table.GLOBL), # o callback
    0x802EBC88: table.sym("object_state_b_802EBC88"),
    0x802EBCE0: table.sym("object_state_b_802EBCE0", table.GLOBL), # o callback
    0x802EBF70: table.sym("object_state_b_802EBF70"),
    0x802EC030: table.sym("object_state_b_802EC030"),
    0x802EC1B0: table.sym("object_state_b_802EC1B0", table.GLOBL), # o callback
    0x802EC200: table.sym("object_state_b_802EC200"),
    0x802EC3D0: table.sym("object_state_b_802EC3D0"),
    0x802EC4E0: table.sym("object_state_b_802EC4E0"),
    0x802EC59C: table.sym("object_state_b_802EC59C"),
    0x802EC75C: table.sym("object_state_b_802EC75C", table.GLOBL), # o callback
    0x802EC7CC: table.sym("object_state_b_802EC7CC"), # unused
    0x802EC818: table.sym("object_state_b_802EC818"),
    0x802EC908: table.sym("object_state_b_802EC908", table.GLOBL), # o callback
    0x802EC9B8: table.sym("object_state_b_802EC9B8", table.GLOBL), # o callback
    0x802EC9F0: table.sym("object_state_b_802EC9F0"),
    0x802ECBA4: table.sym("object_state_b_802ECBA4", table.GLOBL), # o callback
    0x802ECC14: table.sym("object_state_b_802ECC14", table.GLOBL), # o callback
    0x802ECD0C: table.sym("object_state_b_802ECD0C", table.GLOBL), # o callback
    0x802ECEA0: table.sym("object_state_b_802ECEA0", table.GLOBL), # o callback
    0x802ECFAC: table.sym("object_state_b_802ECFAC", table.GLOBL), # o callback
    0x802ED10C: table.sym("object_state_b_802ED10C"),
    0x802ED28C: table.sym("object_state_b_802ED28C"),
    0x802ED39C: table.sym("object_state_b_802ED39C", table.GLOBL), # o callback
    0x802ED40C: table.sym("object_state_b_802ED40C", table.GLOBL), # o callback
    0x802ED45C: table.sym("object_state_b_802ED45C", table.GLOBL), # o callback
    0x802ED498: table.sym("object_state_b_802ED498", table.GLOBL), # o callback
    0x802ED62C: table.sym("object_state_b_802ED62C", table.GLOBL), # o callback
    0x802ED78C: table.sym("object_state_b_802ED78C", table.GLOBL), # o callback
    0x802ED7FC: table.sym("object_state_b_802ED7FC", table.GLOBL), # o callback
    0x802EDACC: table.sym("object_state_b_802EDACC", table.GLOBL), # o callback
    0x802EDB2C: table.sym("object_state_b_802EDB2C", table.GLOBL), # o callback
    0x802EDDFC: table.sym("object_state_b_802EDDFC", table.GLOBL), # o callback
    0x802EDF28: table.sym("object_state_b_802EDF28", table.GLOBL), # o callback
    0x802EE124: table.sym("object_state_b_802EE124", table.GLOBL), # o callback
    0x802EE1A0: table.sym("object_state_b_802EE1A0"),
    0x802EE268: table.sym("object_state_b_802EE268"),
    0x802EE46C: table.sym("object_state_b_802EE46C"),
    0x802EE598: table.sym("object_state_b_802EE598"),
    0x802EE728: table.sym("object_state_b_802EE728"),
    0x802EE778: table.sym("object_state_b_802EE778"),
    0x802EE7E0: table.sym("object_state_b_802EE7E0", table.GLOBL), # o callback
    0x802EE8F4: table.sym("object_state_b_802EE8F4", table.GLOBL), # o callback
    0x802EE9CC: table.sym("object_state_b_802EE9CC", table.GLOBL), # o callback
    0x802EEA24: table.sym("object_state_b_802EEA24"),
    0x802EEA7C: table.sym("object_state_b_802EEA7C"),
    0x802EEB64: table.sym("object_state_b_802EEB64"),
    0x802EECB8: table.sym("object_state_b_802EECB8"),
    0x802EEDF0: table.sym("object_state_b_802EEDF0", table.GLOBL), # o callback
    0x802EEEB4: table.sym("object_state_b_802EEEB4", table.GLOBL), # o callback
    0x802EEF9C: table.sym("object_state_b_802EEF9C", table.GLOBL), # o callback
    0x802EF0E8: table.sym("object_state_b_802EF0E8", table.GLOBL), # o callback
    0x802EF21C: table.sym("object_state_b_802EF21C", table.GLOBL), # o callback
    0x802EF274: table.sym("object_state_b_802EF274", table.GLOBL), # o callback
    0x802EF34C: table.sym("object_state_b_802EF34C", table.GLOBL), # o callback
    0x802EF3F4: table.sym("object_state_b_802EF3F4"),
    0x802EF524: table.sym("object_state_b_802EF524", table.GLOBL), # o callback
    0x802EF63C: table.sym("object_state_b_802EF63C", table.GLOBL), # o callback
    0x802EF66C: table.sym("object_state_b_802EF66C", table.GLOBL), # o callback
    0x802EF820: table.sym("object_state_b_802EF820", table.GLOBL), # o callback
    0x802EF858: table.sym("object_state_b_802EF858", table.GLOBL), # o callback
    0x802EFCD0: table.sym("object_state_b_802EFCD0", table.GLOBL), # o callback
    0x802EFD8C: table.sym("object_state_b_802EFD8C", table.GLOBL), # o callback
    0x802EFE64: table.sym("object_state_b_802EFE64", table.GLOBL), # o callback
    0x802EFEF4: table.sym("object_state_b_802EFEF4", table.GLOBL), # o callback
    0x802F0104: table.sym("object_state_b_802F0104", table.GLOBL), # o callback
    0x802F0168: table.sym("object_state_b_802F0168", table.GLOBL), # o callback
    0x802F0288: table.sym("object_state_b_802F0288"),
    0x802F04A0: table.sym("object_state_b_802F04A0"),
    0x802F05B4: table.sym("object_state_b_802F05B4", table.GLOBL), # o callback
    0x802F06A8: table.sym("object_state_b_802F06A8", table.GLOBL), # o callback
    0x802F0714: table.sym("object_state_b_802F0714", table.GLOBL), # o callback
    0x802F0788: table.sym("object_state_b_802F0788", table.GLOBL), # o callback
    0x802F07F4: table.sym("object_state_b_802F07F4", table.GLOBL), # o callback
    0x802F0820: table.sym("object_state_b_802F0820", table.GLOBL), # o callback
    0x802F084C: table.sym("object_state_b_802F084C", table.GLOBL), # o callback
    0x802F0898: table.sym("object_state_b_802F0898", table.GLOBL), # o callback
    0x802F0950: table.sym("object_state_b_802F0950", table.GLOBL), # o callback
    0x802F09A4: table.sym("object_state_b_802F09A4", table.GLOBL), # o callback
    0x802F09F0: table.sym("object_state_b_802F09F0", table.GLOBL), # o callback
    0x802F0A40: table.sym("object_state_b_802F0A40", table.GLOBL), # o callback
    0x802F0B7C: table.sym("object_state_b_802F0B7C"),
    0x802F0BD4: table.sym("object_state_b_802F0BD4"),
    0x802F0C94: table.sym("object_state_b_802F0C94"),
    0x802F0DF0: table.sym("object_state_b_802F0DF0"),
    0x802F0FA8: table.sym("object_state_b_802F0FA8"),
    0x802F105C: table.sym("object_state_b_802F105C", table.GLOBL), # o callback
    0x802F120C: table.sym("object_state_b_802F120C", table.GLOBL), # o callback
    0x802F1370: table.sym("object_state_b_802F1370", table.GLOBL), # o callback
    0x802F151C: table.sym("object_state_b_802F151C", table.GLOBL), # o callback
    0x802F15A8: table.sym("object_state_b_802F15A8", table.GLOBL), # o callback
    0x802F162C: table.sym("object_state_b_802F162C"),
    0x802F1714: table.sym("object_state_b_802F1714", table.GLOBL), # o callback
    0x802F17F0: table.sym("object_state_b_802F17F0", table.GLOBL), # o callback
    0x802F1954: table.sym("object_state_b_802F1954"),
    0x802F19C8: table.sym("object_state_b_802F19C8"),
    0x802F1A10: table.sym("object_state_b_802F1A10"),
    0x802F1BB8: table.sym("object_state_b_802F1BB8"),
    0x802F1D64: table.sym("object_state_b_802F1D64", table.GLOBL), # o callback
    0x802F1DC0: table.sym("object_state_b_802F1DC0"),
    0x802F1E5C: table.sym("object_state_b_802F1E5C"),
    0x802F1F3C: table.sym("object_state_b_802F1F3C", table.GLOBL), # o callback
    0x802F1FD0: table.sym("object_state_b_802F1FD0", table.GLOBL), # o callback
    0x802F2030: table.sym("object_state_b_802F2030"),
    0x802F20AC: table.sym("object_state_b_802F20AC", table.GLOBL), # o callback
    0x802F2140: table.sym("object_state_b_802F2140", table.GLOBL), # o callback
    0x802F21E0: table.sym("object_state_b_802F21E0"),
    0x802F2284: table.sym("object_state_b_802F2284"),
    0x802F23A8: table.sym("object_state_b_802F23A8", table.GLOBL), # o callback
    0x802F2498: table.sym("object_state_b_802F2498", table.GLOBL), # o callback
    0x802F24F4: table.sym("object_state_b_802F24F4", table.GLOBL), # o callback
    0x802F25B0: table.sym("object_state_b_802F25B0", table.GLOBL), # o callback
    0x802F2614: table.sym("object_state_b_802F2614", table.GLOBL), # o callback
    0x802F2768: table.sym("object_state_b_802F2768", table.GLOBL), # o callback
    0x802F2AA0: table.sym("object_state_b_802F2AA0"),
    0x802F2B88: table.sym("object_state_b_802F2B88", table.GLOBL),
    0x802F2BD4: table.sym("object_state_b_802F2BD4"),
    0x802F2C24: table.sym("object_state_b_802F2C24"),
    0x802F2C84: table.sym("object_state_b_802F2C84", table.GLOBL), # o callback
    0x802F2D8C: table.sym("object_state_b_802F2D8C", table.GLOBL), # o callback
    0x802F2E6C: table.sym("object_state_b_802F2E6C", table.GLOBL), # o callback
    0x802F2F2C: table.sym("object_state_b_802F2F2C", table.GLOBL), # o callback
    0x802F3014: table.sym("object_state_b_802F3014", table.GLOBL), # o callback
    0x802F30F0: table.sym("object_state_b_802F30F0", table.GLOBL), # o callback
    0x802F31BC: table.sym("object_state_b_802F31BC", table.GLOBL), # o callback
    0x802F328C: table.sym("object_state_b_802F328C", table.GLOBL), # o callback
    0x802F336C: table.sym("object_state_b_802F336C", table.GLOBL), # o callback
    0x802F341C: table.sym("object_state_b_802F341C"),
    0x802F36A4: table.sym("object_state_b_802F36A4", table.GLOBL), # o callback
    0x802F38B0: table.sym("object_state_b_802F38B0"),
    0x802F39B4: table.sym("object_state_b_802F39B4"),
    0x802F3A30: table.sym("object_state_b_802F3A30", table.GLOBL), # o callback
    0x802F3B98: table.sym("object_state_b_802F3B98", table.GLOBL), # o callback
    0x802F3C54: table.sym("object_state_b_802F3C54"),
    0x802F3CC8: table.sym("object_state_b_802F3CC8", table.GLOBL), # o callback
    0x802F3D30: table.sym("object_state_b_802F3D30", table.GLOBL), # o callback
    0x802F3DD0: table.sym("object_state_b_802F3DD0"),
    0x802F3EA8: table.sym("object_state_b_802F3EA8"),
    0x802F401C: table.sym("object_state_b_802F401C"),
    0x802F40CC: table.sym("object_state_b_802F40CC", table.GLOBL), # o callback
    0x802F4248: table.sym("object_state_b_802F4248", table.GLOBL), # o callback
    0x802F43B8: table.sym("object_state_b_802F43B8"),
    0x802F44C0: table.sym("object_state_b_802F44C0", table.GLOBL), # o callback
    0x802F45B8: table.sym("object_state_b_802F45B8", table.GLOBL), # o callback
    0x802F45F0: table.sym("object_state_b_802F45F0", table.GLOBL), # o callback
    0x802F4710: table.sym("object_state_b_802F4710", table.GLOBL), # o callback
    0x802F48F4: table.sym("object_state_b_802F48F4", table.GLOBL), # o callback
    0x802F496C: table.sym("object_state_b_802F496C", table.GLOBL), # o callback
    0x802F4B00: table.sym("object_state_b_802F4B00", table.GLOBL), # o callback
    0x802F4B78: table.sym("object_state_b_802F4B78", table.GLOBL), # o callback
    0x802F4C68: table.sym("object_state_b_802F4C68"),
    0x802F4CE0: table.sym("object_state_b_802F4CE0"),
    0x802F4D78: table.sym("object_state_b_802F4D78", table.GLOBL), # o callback
    0x802F4EB4: table.sym("object_state_b_802F4EB4", table.GLOBL), # o callback
    0x802F5010: table.sym("object_state_b_802F5010"),
    0x802F5068: table.sym("object_state_b_802F5068"),
    0x802F52C0: table.sym("object_state_b_802F52C0"),
    0x802F547C: table.sym("object_state_b_802F547C"),
    0x802F55A4: table.sym("object_state_b_802F55A4", table.GLOBL), # o callback
    0x802F5CD4: table.sym("object_state_b_802F5CD4", table.GLOBL), # o callback
    0x802F5D78: table.sym("object_state_b_802F5D78"),
    0x802F5E44: table.sym("object_state_b_802F5E44"),
    0x802F5F48: table.sym("object_state_b_802F5F48"),
    0x802F6014: table.sym("object_state_b_802F6014"),
    0x802F60D8: table.sym("object_state_b_802F60D8"),
    0x802F6150: table.sym("object_state_b_802F6150"),
    0x802F6228: table.sym("object_state_b_802F6228", table.GLOBL), # o callback
    0x802F62E4: table.sym("object_state_b_802F62E4", table.GLOBL), # o callback
    0x802F6448: table.sym("object_state_b_802F6448", table.GLOBL), # o callback
    0x802F6588: table.sym("object_state_b_802F6588"),
    0x802F665C: table.sym("object_state_b_802F665C"),
    0x802F6984: table.sym("object_state_b_802F6984", table.GLOBL), # o callback
    0x802F6A44: table.sym("object_state_b_802F6A44"),
    0x802F6B2C: table.sym("object_state_b_802F6B2C"),
    0x802F6C0C: table.sym("object_state_b_802F6C0C", table.GLOBL), # o callback
    0x802F6D20: table.sym("object_state_b_802F6D20", table.GLOBL), # o callback
    0x802F6D58: table.sym("object_state_b_802F6D58", table.GLOBL), # o callback
    0x802F6E40: table.sym("object_state_b_802F6E40", table.GLOBL), # o callback
    0x802F6EB0: table.sym("object_state_b_802F6EB0"),
    0x802F7068: table.sym("object_state_b_802F7068"),
    0x802F7264: table.sym("object_state_b_802F7264", table.GLOBL), # o callback
    0x802F7348: table.sym("object_state_b_802F7348", table.GLOBL), # o callback
    0x802F7398: table.sym("object_state_b_802F7398"),
    0x802F7418: table.sym("object_state_b_802F7418"),
    0x802F74DC: table.sym("object_state_b_802F74DC", table.GLOBL), # o callback
    0x802F7760: table.sym("object_state_b_802F7760", table.GLOBL), # o callback
    0x802F7924: table.sym("object_state_b_802F7924", table.GLOBL), # o callback
    0x802F7978: table.sym("object_state_b_802F7978", table.GLOBL), # o callback
    0x802F79B0: table.sym("object_state_b_802F79B0", table.GLOBL), # o callback
    0x802F7A58: table.sym("object_state_b_802F7A58", table.GLOBL), # o callback
    0x802F7C9C: table.sym("object_state_b_802F7C9C", table.GLOBL), # o callback
    0x802F7D04: table.sym("object_state_b_802F7D04", table.GLOBL), # o callback
    0x802F7F1C: table.sym("object_state_b_802F7F1C"),
    0x802F7FA0: table.sym("object_state_b_802F7FA0", table.GLOBL), # o callback
    0x802F8044: table.sym("object_state_b_802F8044", table.GLOBL), # o callback
    0x802F8158: table.sym("object_state_b_802F8158", table.GLOBL), # o callback
    0x802F8208: table.sym("object_state_b_802F8208", table.GLOBL), # o callback
    0x802F82F8: table.sym("object_state_b_802F82F8", table.GLOBL), # o callback
    0x802F83A4: table.sym("object_state_b_802F83A4", table.GLOBL), # o callback
    0x802F8490: table.sym("object_state_b_802F8490", table.GLOBL), # o callback
    0x802F85E0: table.sym("object_state_b_802F85E0"),
    0x802F8760: table.sym("object_state_b_802F8760"),
    0x802F8808: table.sym("object_state_b_802F8808"),
    0x802F893C: table.sym("object_state_b_802F893C"),
    0x802F8988: table.sym("object_state_b_802F8988"),
    0x802F8A34: table.sym("object_state_b_802F8A34"),
    0x802F8AB4: table.sym("object_state_b_802F8AB4"),
    0x802F8B54: table.sym("object_state_b_802F8B54"),
    0x802F8C74: table.sym("object_state_b_802F8C74"),
    0x802F8CF8: table.sym("object_state_b_802F8CF8"),
    0x802F8DAC: table.sym("object_state_b_802F8DAC", table.GLOBL), # o callback
    0x802F8E54: table.sym("object_state_b_802F8E54", table.GLOBL), # o callback
    0x802F8F08: table.sym("object_state_b_802F8F08"),
    0x802F9054: table.sym("object_state_b_802F9054"),
    0x802F923C: table.sym("object_state_b_802F923C"),
    0x802F93A8: table.sym("object_state_b_802F93A8"),
    0x802F9500: table.sym("object_state_b_802F9500"),
    0x802F95AC: table.sym("object_state_b_802F95AC"),
    0x802F965C: table.sym("object_state_b_802F965C", table.GLOBL), # o callback

    # src/object_state_c.S
    0x802F9730: table.sym("object_state_c_802F9730"),
    0x802F9770: table.sym("object_state_c_802F9770"),
    0x802F97BC: table.sym("object_state_c_802F97BC"),
    0x802F9820: table.sym("object_state_c_802F9820"),
    0x802F9890: table.sym("object_state_c_802F9890"),
    0x802F9904: table.sym("object_state_c_802F9904"),
    0x802F9A28: table.sym("object_state_c_802F9A28"),
    0x802F9E28: table.sym("object_state_c_802F9E28"),
    0x802FA158: table.sym("object_state_c_802FA158"),
    0x802FA1B0: table.sym("object_state_c_802FA1B0"),
    0x802FA1F8: table.sym("object_state_c_802FA1F8"),
    0x802FA25C: table.sym("object_state_c_802FA25C"),
    0x802FA2BC: table.sym("object_state_c_802FA2BC"),
    0x802FA32C: table.sym("object_state_c_802FA32C"),
    0x802FA360: table.sym("object_state_c_802FA360"),
    0x802FA39C: table.sym("object_state_c_802FA39C"),
    0x802FA3DC: table.sym("object_state_c_802FA3DC"),
    0x802FA428: table.sym("object_state_c_802FA428"),
    0x802FA4C4: table.sym("object_state_c_802FA4C4"),
    0x802FA544: table.sym("object_state_c_802FA544"),
    0x802FA5D0: table.sym("object_state_c_802FA5D0"),
    0x802FA618: table.sym("object_state_c_802FA618"),
    0x802FA660: table.sym("object_state_c_802FA660"),
    0x802FA6D4: table.sym("object_state_c_802FA6D4"),
    0x802FA748: table.sym("object_state_c_802FA748"),
    0x802FA7BC: table.sym("object_state_c_802FA7BC"),
    0x802FA830: table.sym("object_state_c_802FA830"),
    0x802FA900: table.sym("object_state_c_802FA900"),
    0x802FA964: table.sym("object_state_c_802FA964"),
    0x802FA9D8: table.sym("object_state_c_802FA9D8"),
    0x802FAA64: table.sym("object_state_c_802FAA64"),
    0x802FAAC8: table.sym("object_state_c_802FAAC8"),
    0x802FAC18: table.sym("object_state_c_802FAC18"),
    0x802FAD34: table.sym("object_state_c_802FAD34"),
    0x802FADD4: table.sym("object_state_c_802FADD4"),
    0x802FB01C: table.sym("object_state_c_802FB01C"),
    0x802FB0CC: table.sym("object_state_c_802FB0CC"),
    0x802FB128: table.sym("object_state_c_802FB128"),
    0x802FB254: table.sym("object_state_c_802FB254"), # unused
    0x802FB288: table.sym("object_state_c_802FB288"),
    0x802FB3A0: table.sym("object_state_c_802FB3A0"),
    0x802FB3DC: table.sym("object_state_c_802FB3DC"),
    0x802FB518: table.sym("object_state_c_802FB518"),
    0x802FB6E8: table.sym("object_state_c_802FB6E8"),
    0x802FB778: table.sym("object_state_c_802FB778"),
    0x802FB87C: table.sym("object_state_c_802FB87C"),
    0x802FB938: table.sym("object_state_c_802FB938"),
    0x802FBA40: table.sym("object_state_c_802FBA40"),
    0x802FBAB4: table.sym("object_state_c_802FBAB4"),
    0x802FBC4C: table.sym("object_state_c_802FBC4C", table.GLOBL), # o callback
    0x802FBD5C: table.sym("object_state_c_802FBD5C"),
    0x802FBDD4: table.sym("object_state_c_802FBDD4"),
    0x802FBE50: table.sym("object_state_c_802FBE50"),
    0x802FBECC: table.sym("object_state_c_802FBECC"),
    0x802FBF58: table.sym("object_state_c_802FBF58"),
    0x802FBFDC: table.sym("object_state_c_802FBFDC"),
    0x802FC03C: table.sym("object_state_c_802FC03C"),
    0x802FC16C: table.sym("object_state_c_802FC16C"),
    0x802FC288: table.sym("object_state_c_802FC288"),
    0x802FC338: table.sym("object_state_c_802FC338"),
    0x802FC414: table.sym("object_state_c_802FC414"),
    0x802FC510: table.sym("object_state_c_802FC510"),
    0x802FC670: table.sym("object_state_c_802FC670"),
    0x802FC914: table.sym("object_state_c_802FC914"),
    0x802FCAF4: table.sym("object_state_c_802FCAF4"),
    0x802FCB1C: table.sym("object_state_c_802FCB1C"),
    0x802FCC00: table.sym("object_state_c_802FCC00"),
    0x802FCCC8: table.sym("object_state_c_802FCCC8"),
    0x802FCD64: table.sym("object_state_c_802FCD64"),
    0x802FCE94: table.sym("object_state_c_802FCE94"),
    0x802FD014: table.sym("object_state_c_802FD014"),
    0x802FD068: table.sym("object_state_c_802FD068"),
    0x802FD3E4: table.sym("object_state_c_802FD3E4"),
    0x802FD464: table.sym("object_state_c_802FD464"),
    0x802FD4B0: table.sym("object_state_c_802FD4B0"),
    0x802FD6AC: table.sym("object_state_c_802FD6AC"),
    0x802FD7F8: table.sym("object_state_c_802FD7F8", table.GLOBL), # o callback
    0x802FD950: table.sym("object_state_c_802FD950", table.GLOBL), # o callback
    0x802FDA28: table.sym("object_state_c_802FDA28", table.GLOBL), # o callback
    0x802FDEA8: table.sym("object_state_c_802FDEA8"),
    0x802FDFC4: table.sym("object_state_c_802FDFC4"),
    0x802FE37C: table.sym("object_state_c_802FE37C"),
    0x802FE3B0: table.sym("object_state_c_802FE3B0", table.GLOBL), # o callback
    0x802FE450: table.sym("object_state_c_802FE450"),
    0x802FE520: table.sym("object_state_c_802FE520"),
    0x802FE8B4: table.sym("object_state_c_802FE8B4", table.GLOBL), # o callback
    0x802FE988: table.sym("object_state_c_802FE988"),
    0x802FEB00: table.sym("object_state_c_802FEB00"),
    0x802FED50: table.sym("object_state_c_802FED50"),
    0x802FEF18: table.sym("object_state_c_802FEF18"),
    0x802FF040: table.sym("object_state_c_802FF040", table.GLOBL), # o callback
    0x802FF214: table.sym("object_state_c_802FF214", table.GLOBL), # o callback
    0x802FF408: table.sym("object_state_c_802FF408", table.GLOBL), # o callback
    0x802FF518: table.sym("object_state_c_802FF518"),
    0x802FF584: table.sym("object_state_c_802FF584"),
    0x802FF600: table.sym("object_state_c_802FF600"),
    0x802FF868: table.sym("object_state_c_802FF868"),
    0x802FF8E8: table.sym("object_state_c_802FF8E8"),
    0x802FF94C: table.sym("object_state_c_802FF94C"),
    0x802FF96C: table.sym("object_state_c_802FF96C", table.GLOBL), # o callback
    0x802FFB38: table.sym("object_state_c_802FFB38", table.GLOBL), # o callback
    0x802FFC60: table.sym("object_state_c_802FFC60"),
    0x802FFDAC: table.sym("object_state_c_802FFDAC"),
    0x8030009C: table.sym("object_state_c_8030009C"),
    0x803000E4: table.sym("object_state_c_803000E4"),
    0x803002F4: table.sym("object_state_c_803002F4"),
    0x803004F0: table.sym("object_state_c_803004F0"),
    0x8030059C: table.sym("object_state_c_8030059C"),
    0x80300778: table.sym("object_state_c_80300778"),
    0x803008A8: table.sym("object_state_c_803008A8"),
    0x803008EC: table.sym("object_state_c_803008EC"),
    0x80300940: table.sym("object_state_c_80300940"),
    0x80300DD4: table.sym("object_state_c_80300DD4"),
    0x80300E40: table.sym("object_state_c_80300E40", table.GLOBL), # o callback
    0x80300ECC: table.sym("object_state_c_80300ECC", table.GLOBL), # o callback
    0x80301148: table.sym("object_state_c_80301148", table.GLOBL), # o callback
    0x80301180: table.sym("object_state_c_80301180", table.GLOBL), # o callback
    0x80301210: table.sym("object_state_c_80301210", table.GLOBL), # o callback
    0x803014CC: table.sym("object_state_c_803014CC"),
    0x803016E0: table.sym("object_state_c_803016E0"),
    0x80301940: table.sym("object_state_c_80301940"),
    0x80301C88: table.sym("object_state_c_80301C88"),
    0x80301E84: table.sym("object_state_c_80301E84"),
    0x80301F70: table.sym("object_state_c_80301F70"),
    0x80302024: table.sym("object_state_c_80302024"),
    0x803020E4: table.sym("object_state_c_803020E4"),
    0x80302154: table.sym("object_state_c_80302154", table.GLOBL), # o callback
    0x80302358: table.sym("object_state_c_80302358"),
    0x803023E4: table.sym("object_state_c_803023E4"),
    0x8030267C: table.sym("object_state_c_8030267C"),
    0x803027AC: table.sym("object_state_c_803027AC"),
    0x80302910: table.sym("object_state_c_80302910", table.GLOBL), # o callback
    0x803029B8: table.sym("object_state_c_803029B8"),
    0x80302A54: table.sym("object_state_c_80302A54"),
    0x80302B20: table.sym("object_state_c_80302B20"),
    0x80302C84: table.sym("object_state_c_80302C84"),
    0x80302DB0: table.sym("object_state_c_80302DB0"),
    0x80302E84: table.sym("object_state_c_80302E84"),
    0x80302F04: table.sym("object_state_c_80302F04"),
    0x80303028: table.sym("object_state_c_80303028", table.GLOBL), # o callback
    0x803030A8: table.sym("object_state_c_803030A8"),
    0x803031B4: table.sym("object_state_c_803031B4"),
    0x8030320C: table.sym("object_state_c_8030320C"),
    0x80303498: table.sym("object_state_c_80303498"),
    0x80303634: table.sym("object_state_c_80303634"),
    0x8030369C: table.sym("object_state_c_8030369C", table.GLOBL), # o callback
    0x80303744: table.sym("object_state_c_80303744", table.GLOBL), # o callback
    0x80303984: table.sym("object_state_c_80303984", table.GLOBL), # o callback
    0x80303A20: table.sym("object_state_c_80303A20"),
    0x80303B08: table.sym("object_state_c_80303B08"),
    0x80303C14: table.sym("object_state_c_80303C14"),
    0x80303F64: table.sym("object_state_c_80303F64", table.GLOBL), # o callback
    0x803041A0: table.sym("object_state_c_803041A0"),
    0x80304274: table.sym("object_state_c_80304274"),
    0x803043F8: table.sym("object_state_c_803043F8", table.GLOBL), # o callback
    0x80304474: table.sym("object_state_c_80304474"),
    0x803044C0: table.sym("object_state_c_803044C0", table.GLOBL), # o callback
    0x803044DC: table.sym("object_state_c_803044DC"),
    0x80304710: table.sym("object_state_c_80304710"),
    0x803047AC: table.sym("object_state_c_803047AC"),
    0x80304864: table.sym("object_state_c_80304864"),
    0x803048EC: table.sym("object_state_c_803048EC"),
    0x80304958: table.sym("object_state_c_80304958"),
    0x80304A14: table.sym("object_state_c_80304A14"),
    0x80304A70: table.sym("object_state_c_80304A70"),
    0x80304AE0: table.sym("object_state_c_80304AE0"),
    0x80304BA8: table.sym("object_state_c_80304BA8", table.GLOBL), # o callback
    0x80304E28: table.sym("object_state_c_80304E28"),
    0x80304F74: table.sym("object_state_c_80304F74"),
    0x80304FD4: table.sym("object_state_c_80304FD4", table.GLOBL), # o callback
    0x8030505C: table.sym("object_state_c_8030505C"),
    0x8030508C: table.sym("object_state_c_8030508C"),
    0x80305100: table.sym("object_state_c_80305100", table.GLOBL), # o callback
    0x8030522C: table.sym("object_state_c_8030522C"),
    0x803053DC: table.sym("object_state_c_803053DC"),
    0x80305474: table.sym("object_state_c_80305474"),
    0x8030586C: table.sym("object_state_c_8030586C"),
    0x803058A4: table.sym("object_state_c_803058A4"),
    0x80305904: table.sym("object_state_c_80305904"),
    0x80305A58: table.sym("object_state_c_80305A58", table.GLOBL), # o callback
    0x80305BB0: table.sym("object_state_c_80305BB0", table.GLOBL), # o callback
    0x80305C14: table.sym("object_state_c_80305C14", table.GLOBL), # o callback
    0x80305C90: table.sym("object_state_c_80305C90", table.GLOBL), # o callback
    0x80305E2C: table.sym("object_state_c_80305E2C", table.GLOBL), # o callback
    0x80305F24: table.sym("object_state_c_80305F24", table.GLOBL), # o callback
    0x80306084: table.sym("object_state_c_80306084", table.GLOBL), # o callback
    0x803062A8: table.sym("object_state_c_803062A8"),
    0x80306304: table.sym("object_state_c_80306304"),
    0x80306364: table.sym("object_state_c_80306364"),
    0x8030668C: table.sym("object_state_c_8030668C"),
    0x803066D8: table.sym("object_state_c_803066D8"),
    0x803067E8: table.sym("object_state_c_803067E8", table.GLOBL), # o callback
    0x803068C0: table.sym("object_state_c_803068C0", table.GLOBL), # o callback
    0x8030699C: table.sym("object_state_c_8030699C", table.GLOBL), # o callback
    0x80306A38: table.sym("object_state_c_80306A38", table.GLOBL), # o callback
    0x80306CC4: table.sym("object_state_c_80306CC4", table.GLOBL), # o callback
    0x80306D38: table.sym("object_state_c_80306D38", table.GLOBL), # o callback
    0x80306F48: table.sym("object_state_c_80306F48", table.GLOBL), # o callback
    0x80307010: table.sym("object_state_c_80307010", table.GLOBL), # o callback
    0x803071B8: table.sym("object_state_c_803071B8", table.GLOBL), # o callback
    0x80307240: table.sym("object_state_c_80307240"),
    0x80307348: table.sym("object_state_c_80307348"),
    0x803073F8: table.sym("object_state_c_803073F8"),
    0x80307434: table.sym("object_state_c_80307434"),
    0x803075F8: table.sym("object_state_c_803075F8"),
    0x80307670: table.sym("object_state_c_80307670", table.GLOBL), # o callback
    0x80307760: table.sym("object_state_c_80307760", table.GLOBL), # o callback
    0x803077E0: table.sym("object_state_c_803077E0", table.GLOBL), # o callback
    0x80307930: table.sym("object_state_c_80307930", table.GLOBL), # o callback
    0x803079C8: table.sym("object_state_c_803079C8", table.GLOBL), # o callback
    0x80307AE4: table.sym("object_state_c_80307AE4", table.GLOBL), # o callback
    0x80307B58: table.sym("object_state_c_80307B58", table.GLOBL), # o callback
    0x80307C88: table.sym("object_state_c_80307C88", table.GLOBL), # o callback
    0x80307CF8: table.sym("object_state_c_80307CF8", table.GLOBL), # o callback
    0x80307EA4: table.sym("object_state_c_80307EA4", table.GLOBL), # o callback
    0x80307FB8: table.sym("object_state_c_80307FB8"),
    0x8030803C: table.sym("object_state_c_8030803C", table.GLOBL), # o callback
    0x80308110: table.sym("object_state_c_80308110"),
    0x80308228: table.sym("object_state_c_80308228"),
    0x803082EC: table.sym("object_state_c_803082EC"),
    0x80308454: table.sym("object_state_c_80308454"),
    0x80308734: table.sym("object_state_c_80308734"),
    0x80308A74: table.sym("object_state_c_80308A74"),
    0x80308AF0: table.sym("object_state_c_80308AF0"),
    0x80308BB8: table.sym("object_state_c_80308BB8"),
    0x80308D6C: table.sym("object_state_c_80308D6C", table.GLOBL), # o callback
    0x80308F08: table.sym("object_state_c_80308F08"),
    0x80308F94: table.sym("object_state_c_80308F94"),
    0x803090B8: table.sym("object_state_c_803090B8"),
    0x80309154: table.sym("object_state_c_80309154", table.GLOBL), # o callback
    0x803091E0: table.sym("object_state_c_803091E0", table.GLOBL), # o callback
    0x80309354: table.sym("object_state_c_80309354", table.GLOBL), # o callback
    0x80309454: table.sym("object_state_c_80309454", table.GLOBL), # o callback
    0x803094D0: table.sym("object_state_c_803094D0", table.GLOBL), # o callback
    0x803094F8: table.sym("object_state_c_803094F8", table.GLOBL), # o callback
    0x80309530: table.sym("object_state_c_80309530", table.GLOBL), # o callback
    0x803097A4: table.sym("object_state_c_803097A4", table.GLOBL), # o callback
    0x803098C0: table.sym("object_state_c_803098C0", table.GLOBL), # o callback
    0x80309B64: table.sym("object_state_c_80309B64", table.GLOBL), # o callback
    0x80309CEC: table.sym("object_state_c_80309CEC", table.GLOBL), # o callback
    0x80309ED4: table.sym("object_state_c_80309ED4"),
    0x80309F68: table.sym("object_state_c_80309F68"),
    0x8030A0E8: table.sym("object_state_c_8030A0E8"),
    0x8030A11C: table.sym("object_state_c_8030A11C", table.GLOBL), # o callback
    0x8030A1C0: table.sym("object_state_c_8030A1C0", table.GLOBL), # o callback
    0x8030A2A8: table.sym("object_state_c_8030A2A8"),
    0x8030A390: table.sym("object_state_c_8030A390"),
    0x8030A514: table.sym("object_state_c_8030A514"),
    0x8030A614: table.sym("object_state_c_8030A614"),
    0x8030A93C: table.sym("object_state_c_8030A93C", table.GLOBL), # o callback
    0x8030AABC: table.sym("object_state_c_8030AABC", table.GLOBL), # o callback
    0x8030AD04: table.sym("object_state_c_8030AD04"),
    0x8030AE9C: table.sym("object_state_c_8030AE9C"),
    0x8030B0B8: table.sym("object_state_c_8030B0B8"),
    0x8030B0F0: table.sym("object_state_c_8030B0F0"),
    0x8030B220: table.sym("object_state_c_8030B220"),
    0x8030B2F4: table.sym("object_state_c_8030B2F4", table.GLOBL), # o callback
    0x8030B658: table.sym("object_state_c_8030B658", table.GLOBL), # o callback
    0x8030B6D8: table.sym("object_state_c_8030B6D8"),
    0x8030BA68: table.sym("object_state_c_8030BA68"),
    0x8030BC90: table.sym("object_state_c_8030BC90", table.GLOBL), # o callback
    0x8030BD2C: table.sym("object_state_c_8030BD2C"),
    0x8030BDF8: table.sym("object_state_c_8030BDF8"),
    0x8030BFD0: table.sym("object_state_c_8030BFD0", table.GLOBL), # o callback
    0x8030C06C: table.sym("object_state_c_8030C06C"),
    0x8030C0F0: table.sym("object_state_c_8030C0F0"),
    0x8030C210: table.sym("object_state_c_8030C210"),
    0x8030C2C8: table.sym("object_state_c_8030C2C8"),
    0x8030C364: table.sym("object_state_c_8030C364", table.GLOBL), # o callback
    0x8030C4B0: table.sym("object_state_c_8030C4B0", table.GLOBL), # o callback
    0x8030C564: table.sym("object_state_c_8030C564"),
    0x8030C60C: table.sym("object_state_c_8030C60C"),
    0x8030C6A4: table.sym("object_state_c_8030C6A4"),
    0x8030C828: table.sym("object_state_c_8030C828"),
    0x8030C894: table.sym("object_state_c_8030C894"),
    0x8030C8EC: table.sym("object_state_c_8030C8EC", table.GLOBL), # o callback
    0x8030C98C: table.sym("object_state_c_8030C98C", table.GLOBL), # o callback
    0x8030CD30: table.sym("object_state_c_8030CD30", table.GLOBL),
    0x8030CDDC: table.sym("object_state_c_8030CDDC", table.GLOBL), # o callback
    0x8030CEC0: table.sym("object_state_c_8030CEC0"),
    0x8030D140: table.sym("object_state_c_8030D140"),
    0x8030D2F0: table.sym("object_state_c_8030D2F0", table.GLOBL), # o callback
    0x8030D42C: table.sym("object_state_c_8030D42C"),
    0x8030D4D4: table.sym("object_state_c_8030D4D4"),
    0x8030D598: table.sym("object_state_c_8030D598", table.GLOBL), # o callback
    0x8030D640: table.sym("object_state_c_8030D640", table.GLOBL), # o callback
    0x8030D8D4: table.sym("object_state_c_8030D8D4", table.GLOBL), # o callback
    0x8030D93C: table.sym("object_state_c_8030D93C", table.GLOBL), # g callback
    0x8030D9AC: table.sym("object_state_c_8030D9AC", table.GLOBL), # g callback
    0x8030DA14: table.sym("object_state_c_8030DA14"),
    0x8030DB38: table.sym("object_state_c_8030DB38"),
    0x8030DC70: table.sym("object_state_c_8030DC70", table.GLOBL), # o callback
    0x8030DFC4: table.sym("object_state_c_8030DFC4", table.GLOBL), # o callback
    0x8030E14C: table.sym("object_state_c_8030E14C", table.GLOBL), # o callback
    0x8030E16C: table.sym("object_state_c_8030E16C", table.GLOBL), # o callback
    0x8030E384: table.sym("object_state_c_8030E384"),
    0x8030E3E0: table.sym("object_state_c_8030E3E0"),
    0x8030E488: table.sym("object_state_c_8030E488"),
    0x8030E52C: table.sym("object_state_c_8030E52C"),
    0x8030E688: table.sym("object_state_c_8030E688"),
    0x8030E6D4: table.sym("object_state_c_8030E6D4"),
    0x8030E9E0: table.sym("object_state_c_8030E9E0"),
    0x8030EA9C: table.sym("object_state_c_8030EA9C", table.GLOBL), # o callback
    0x8030EB3C: table.sym("object_state_c_8030EB3C"),
    0x8030ECA8: table.sym("object_state_c_8030ECA8"),
    0x8030ECF8: table.sym("object_state_c_8030ECF8"),
    0x8030EF08: table.sym("object_state_c_8030EF08"),
    0x8030F118: table.sym("object_state_c_8030F118"),
    0x8030F21C: table.sym("object_state_c_8030F21C"),
    0x8030F440: table.sym("object_state_c_8030F440"),
    0x8030F508: table.sym("object_state_c_8030F508"),
    0x8030F58C: table.sym("object_state_c_8030F58C"),
    0x8030F5CC: table.sym("object_state_c_8030F5CC"),
    0x8030F628: table.sym("object_state_c_8030F628"),
    0x8030F6BC: table.sym("object_state_c_8030F6BC"),
    0x8030F840: table.sym("object_state_c_8030F840"),
    0x8030F9C0: table.sym("object_state_c_8030F9C0"),
    0x8030FB3C: table.sym("object_state_c_8030FB3C"),
    0x8030FC34: table.sym("object_state_c_8030FC34"),
    0x8030FCF4: table.sym("object_state_c_8030FCF4"),
    0x8030FE38: table.sym("object_state_c_8030FE38"),
    0x8030FFF8: table.sym("object_state_c_8030FFF8", table.GLOBL), # o callback
    0x803101DC: table.sym("object_state_c_803101DC"),
    0x80310258: table.sym("object_state_c_80310258"),
    0x80310318: table.sym("object_state_c_80310318"),
    0x80310498: table.sym("object_state_c_80310498", table.GLOBL), # o callback
    0x8031054C: table.sym("object_state_c_8031054C"),
    0x80310774: table.sym("object_state_c_80310774"),
    0x8031097C: table.sym("object_state_c_8031097C"),
    0x80310A7C: table.sym("object_state_c_80310A7C"),
    0x80310B2C: table.sym("object_state_c_80310B2C"),
    0x80310C3C: table.sym("object_state_c_80310C3C"),
    0x80310F04: table.sym("object_state_c_80310F04"),
    0x80311018: table.sym("object_state_c_80311018"),
    0x8031111C: table.sym("object_state_c_8031111C"),
    0x8031126C: table.sym("object_state_c_8031126C"),
    0x8031129C: table.sym("object_state_c_8031129C", table.GLOBL), # o callback
    0x8031157C: table.sym("object_state_c_8031157C"),
    0x803116C0: table.sym("object_state_c_803116C0"),
    0x80311874: table.sym("object_state_c_80311874", table.GLOBL), # o callback
    0x803118E4: table.sym("object_state_c_803118E4", table.GLOBL), # o callback
    0x80311954: table.sym("object_state_c_80311954"),
    0x803119E4: table.sym("object_state_c_803119E4"),
    0x80311B18: table.sym("object_state_c_80311B18"),
    0x80311B7C: table.sym("object_state_c_80311B7C"),
    0x80311DD8: table.sym("object_state_c_80311DD8"),
    0x80311EA4: table.sym("object_state_c_80311EA4"),
    0x80312070: table.sym("object_state_c_80312070", table.GLOBL), # o callback
    0x80312168: table.sym("object_state_c_80312168", table.GLOBL), # o callback
    0x80312200: table.sym("object_state_c_80312200", table.GLOBL), # o callback
    0x80312248: table.sym("object_state_c_80312248", table.GLOBL), # o callback
    0x80312370: table.sym("object_state_c_80312370"),
    0x8031262C: table.sym("object_state_c_8031262C"),
    0x8031274C: table.sym("object_state_c_8031274C", table.GLOBL), # o callback
    0x80312804: table.sym("object_state_c_80312804"),
    0x80312900: table.sym("object_state_c_80312900"),
    0x80312A54: table.sym("object_state_c_80312A54", table.GLOBL), # o callback
    0x80312AF4: table.sym("object_state_c_80312AF4"),
    0x80312B80: table.sym("object_state_c_80312B80"),
    0x80312D0C: table.sym("object_state_c_80312D0C"),
    0x80312EA8: table.sym("object_state_c_80312EA8"),
    0x80313110: table.sym("object_state_c_80313110", table.GLOBL), # o callback
    0x803131E8: table.sym("object_state_c_803131E8", table.GLOBL), # o callback
    0x8031326C: table.sym("object_state_c_8031326C", table.GLOBL), # o callback
    0x80313294: table.sym("object_state_c_80313294", table.GLOBL), # o callback
    0x80313354: table.sym("object_state_c_80313354", table.GLOBL), # o callback
    0x80313530: table.sym("object_state_c_80313530", table.GLOBL), # o callback
    0x803136CC: table.sym("object_state_c_803136CC", table.GLOBL), # o callback
    0x80313754: table.sym("object_state_c_80313754", table.GLOBL), # o callback
    0x803137F4: table.sym("object_state_c_803137F4", table.GLOBL), # o callback
    0x8031381C: table.sym("object_state_c_8031381C"),
    0x803139F0: table.sym("object_state_c_803139F0"),
    0x80313BE4: table.sym("object_state_c_80313BE4"),
    0x80313E1C: table.sym("object_state_c_80313E1C"),
    0x80313FC0: table.sym("object_state_c_80313FC0", table.GLOBL), # o callback
    0x80314098: table.sym("object_state_c_80314098"),
    0x8031427C: table.sym("object_state_c_8031427C"),
    0x803145D4: table.sym("object_state_c_803145D4", table.GLOBL), # o callback

    # src/audio/a.S
    0x80314A30: table.sym("audio_a_80314A30"),
    0x80314CC0: table.sym("audio_a_80314CC0"),
    0x80314DE4: table.sym("audio_a_80314DE4", table.GLOBL),
    0x80314F64: table.sym("audio_a_80314F64"),
    0x80315590: table.sym("audio_a_80315590"),
    0x80316010: table.sym("audio_a_80316010"),
    0x803160DC: table.sym("audio_a_803160DC"),
    0x80316138: table.sym("audio_a_80316138"),
    0x8031619C: table.sym("audio_a_8031619C"),
    0x803166FC: table.sym("audio_a_803166FC"),
    0x80316AC8: table.sym("audio_a_80316AC8", table.GLOBL),
    0x80316AF4: table.sym("audio_a_80316AF4", table.GLOBL),
    0x80316DA8: table.sym("audio_a_80316DA8", table.GLOBL),
    0x80316DB4: table.sym("audio_a_80316DB4", table.GLOBL),
    0x80316E00: table.sym("audio_a_80316E00", table.GLOBL),

    # src/audio/b.S
    0x80316E80: table.sym("audio_b_80316E80"),
    0x80316EC4: table.sym("audio_b_80316EC4"),
    0x80316FB4: table.sym("audio_b_80316FB4"),
    0x80317040: table.sym("audio_b_80317040", table.GLOBL),
    0x803170B4: table.sym("audio_b_803170B4"),
    0x803170D4: table.sym("audio_b_803170D4"),
    0x803170E8: table.sym("audio_b_803170E8"),
    0x80317118: table.sym("audio_b_80317118"), # unused
    0x80317128: table.sym("audio_b_80317128", table.GLOBL),
    0x80317184: table.sym("audio_b_80317184"),
    0x80317200: table.sym("audio_b_80317200"),
    0x8031727C: table.sym("audio_b_8031727C"),
    0x80317338: table.sym("audio_b_80317338"),
    0x803173F4: table.sym("audio_b_803173F4"), # unused
    0x803173FC: table.sym("audio_b_803173FC", table.GLOBL),
    0x8031782C: table.sym("audio_b_8031782C", table.GLOBL),
    0x803178EC: table.sym("audio_b_803178EC"),
    0x80317914: table.sym("audio_b_80317914"),
    0x80317948: table.sym("audio_b_80317948", table.GLOBL),

    # src/audio/c.S
    0x80318040: table.sym("audio_c_80318040"),
    0x803180C4: table.sym("audio_c_803180C4"),
    0x80318130: table.sym("audio_c_80318130", table.GLOBL),
    0x803181EC: table.sym("audio_c_803181EC", table.GLOBL),
    0x80318300: table.sym("audio_c_80318300", table.GLOBL),
    0x80318634: table.sym("audio_c_80318634", table.GLOBL),
    0x803188EC: table.sym("audio_c_803188EC"), # unused
    0x803188F4: table.sym("audio_c_803188F4", table.GLOBL),
    0x80318B30: table.sym("audio_c_80318B30"),
    0x80318C8C: table.sym("audio_c_80318C8C"),
    0x80318DC4: table.sym("audio_c_80318DC4"),
    0x80318E70: table.sym("audio_c_80318E70"),
    0x80318FAC: table.sym("audio_c_80318FAC"),
    0x803190F4: table.sym("audio_c_803190F4"),
    0x80319220: table.sym("audio_c_80319220", table.GLOBL),
    0x80319328: table.sym("audio_c_80319328", table.GLOBL),
    0x80319388: table.sym("audio_c_80319388"),
    0x8031950C: table.sym("audio_c_8031950C", table.GLOBL),

    # src/audio/d.S
    0x80319920: table.sym("audio_d_80319920"),
    0x80319998: table.sym("audio_d_80319998"),
    0x803199B8: table.sym("audio_d_803199B8", table.GLOBL),
    0x80319DB8: table.sym("audio_d_80319DB8"),
    0x80319F64: table.sym("audio_d_80319F64", table.GLOBL),
    0x80319F84: table.sym("audio_d_80319F84"),
    0x80319FA4: table.sym("audio_d_80319FA4"),
    0x8031A1D0: table.sym("audio_d_8031A1D0", table.GLOBL),
    0x8031A254: table.sym("audio_d_8031A254"),
    0x8031A264: table.sym("audio_d_8031A264", table.GLOBL),
    0x8031A2B4: table.sym("audio_d_8031A2B4", table.GLOBL),
    0x8031A368: table.sym("audio_d_8031A368", table.GLOBL),
    0x8031A494: table.sym("audio_d_8031A494", table.GLOBL),
    0x8031A5D0: table.sym("audio_d_8031A5D0"),
    0x8031A610: table.sym("audio_d_8031A610", table.GLOBL),
    0x8031A63C: table.sym("audio_d_8031A63C"),
    0x8031A6CC: table.sym("audio_d_8031A6CC"),
    0x8031A794: table.sym("audio_d_8031A794"),
    0x8031A7C8: table.sym("audio_d_8031A7C8"),
    0x8031A820: table.sym("audio_d_8031A820"),
    0x8031A89C: table.sym("audio_d_8031A89C"),
    0x8031A8F0: table.sym("audio_d_8031A8F0"),
    0x8031A94C: table.sym("audio_d_8031A94C", table.GLOBL),
    0x8031AC34: table.sym("audio_d_8031AC34", table.GLOBL),
    0x8031ADAC: table.sym("audio_d_8031ADAC", table.GLOBL),

    # src/audio/e.S
    0x8031AEE0: table.sym("audio_e_8031AEE0"), # unused
    0x8031AEE8: table.sym("audio_e_8031AEE8", table.GLOBL),
    0x8031B0CC: table.sym("audio_e_8031B0CC"),
    0x8031B1C0: table.sym("audio_e_8031B1C0"),
    0x8031B248: table.sym("audio_e_8031B248"),
    0x8031B440: table.sym("audio_e_8031B440", table.GLOBL),
    0x8031B4A0: table.sym("audio_e_8031B4A0", table.GLOBL),
    0x8031B58C: table.sym("audio_e_8031B58C", table.GLOBL),
    0x8031B5AC: table.sym("audio_e_8031B5AC", table.GLOBL),

    # src/audio/f.S
    0x8031B830: table.sym("audio_f_8031B830"),
    0x8031B940: table.sym("audio_f_8031B940"),
    0x8031BA30: table.sym("audio_f_8031BA30", table.GLOBL),
    0x8031BA6C: table.sym("audio_f_8031BA6C"),
    0x8031BAF0: table.sym("audio_f_8031BAF0", table.GLOBL),
    0x8031BB5C: table.sym("audio_f_8031BB5C"),
    0x8031BBA4: table.sym("audio_f_8031BBA4"),
    0x8031BCD0: table.sym("audio_f_8031BCD0"),
    0x8031BDA0: table.sym("audio_f_8031BDA0"),
    0x8031BE44: table.sym("audio_f_8031BE44", table.GLOBL),
    0x8031BF14: table.sym("audio_f_8031BF14", table.GLOBL),
    0x8031BF54: table.sym("audio_f_8031BF54", table.GLOBL),
    0x8031BF94: table.sym("audio_f_8031BF94"),
    0x8031C03C: table.sym("audio_f_8031C03C"),
    0x8031C050: table.sym("audio_f_8031C050"),
    0x8031C080: table.sym("audio_f_8031C080"),
    0x8031C0C4: table.sym("audio_f_8031C0C4"),
    0x8031CE54: table.sym("audio_f_8031CE54"),
    0x8031CFD4: table.sym("audio_f_8031CFD4"),
    0x8031D068: table.sym("audio_f_8031D068"),
    0x8031D08C: table.sym("audio_f_8031D08C"),
    0x8031D9EC: table.sym("audio_f_8031D9EC"),
    0x8031E240: table.sym("audio_f_8031E240", table.GLOBL),
    0x8031E2E8: table.sym("audio_f_8031E2E8", table.GLOBL),
    0x8031E374: table.sym("audio_f_8031E374", table.GLOBL),

    # src/audio/g.S
    0x8031E4F0: table.sym("audio_g_8031E4F0"), # unused
    0x8031E568: table.sym("audio_g_8031E568"), # unused
    0x8031E578: table.sym("audio_g_8031E578"),
    0x8031E5C0: table.sym("audio_g_8031E5C0"),
    0x8031E60C: table.sym("audio_g_8031E60C"),
    0x8031E6A4: table.sym("audio_g_8031E6A4"),
    0x8031E710: table.sym("audio_g_8031E710"),
    0x8031E7B8: table.sym("audio_g_8031E7B8", table.GLOBL),
    0x8031EB00: table.sym("audio_g_8031EB00", table.GLOBL),
    0x8031EB30: table.sym("audio_g_8031EB30"),
    0x8031EDEC: table.sym("audio_g_8031EDEC"),
    0x8031EE70: table.sym("audio_g_8031EE70"),
    0x8031EF6C: table.sym("audio_g_8031EF6C"),
    0x8031EFF4: table.sym("audio_g_8031EFF4"),
    0x8031F810: table.sym("audio_g_8031F810"),
    0x8031F96C: table.sym("audio_g_8031F96C"),
    0x8031FB20: table.sym("audio_g_8031FB20"),
    0x8031FBE8: table.sym("audio_g_8031FBE8"),
    0x8031FD7C: table.sym("audio_g_8031FD7C"),
    0x8031FD84: table.sym("audio_g_8031FD84", table.GLOBL),
    0x8031FDAC: table.sym("audio_g_8031FDAC"),
    0x80320544: table.sym("audio_g_80320544"),
    0x80320678: table.sym("audio_g_80320678", table.GLOBL),
    0x803206BC: table.sym("audio_g_803206BC", table.GLOBL),
    0x80320734: table.sym("audio_g_80320734"),
    0x8032080C: table.sym("audio_g_8032080C"),
    0x803208EC: table.sym("audio_g_803208EC"),
    0x80320D70: table.sym("audio_g_80320D70"), # unused
    0x80320E3C: table.sym("audio_g_80320E3C", table.GLOBL),
    0x80320EC4: table.sym("audio_g_80320EC4", table.GLOBL),
    0x80320F68: table.sym("audio_g_80320F68"),
    0x803210D4: table.sym("audio_g_803210D4", table.GLOBL),
    0x8032112C: table.sym("audio_g_8032112C", table.GLOBL),
    0x80321398: table.sym("audio_g_80321398"), # unused
    0x80321474: table.sym("audio_g_80321474", table.GLOBL),
    0x80321584: table.sym("audio_g_80321584", table.GLOBL),
    0x80321668: table.sym("audio_g_80321668"),
    0x8032171C: table.sym("audio_g_8032171C", table.GLOBL),
    0x8032174C: table.sym("audio_g_8032174C", table.GLOBL),
    0x803217A8: table.sym("audio_g_803217A8"),
    0x8032180C: table.sym("audio_g_8032180C", table.GLOBL),
    0x80321864: table.sym("audio_g_80321864"), # unused
    0x803218D8: table.sym("audio_g_803218D8", table.GLOBL),
    0x803218F4: table.sym("audio_g_803218F4", table.GLOBL),
    0x803219AC: table.sym("audio_g_803219AC", table.GLOBL),
    0x80321BAC: table.sym("audio_g_80321BAC", table.GLOBL),
    0x80321CE4: table.sym("audio_g_80321CE4", table.GLOBL),
    0x80321D38: table.sym("audio_g_80321D38", table.GLOBL),
    0x80321D5C: table.sym("audio_g_80321D5C", table.GLOBL),
    0x80321D9C: table.sym("audio_g_80321D9C"),
    0x80321E48: table.sym("audio_g_80321E48", table.GLOBL),
    0x80321F48: table.sym("audio_g_80321F48", table.GLOBL),
    0x80321F9C: table.sym("audio_g_80321F9C", table.GLOBL),
    0x80322078: table.sym("audio_g_80322078", table.GLOBL),
    0x803220B4: table.sym("audio_g_803220B4", table.GLOBL),
    0x803220F0: table.sym("audio_g_803220F0", table.GLOBL),
    0x8032212C: table.sym("audio_g_8032212C", table.GLOBL),
    0x80322168: table.sym("audio_g_80322168", table.GLOBL),
    0x803221B8: table.sym("audio_g_803221B8", table.GLOBL),
    0x803221F4: table.sym("audio_g_803221F4", table.GLOBL),
    0x80322230: table.sym("audio_g_80322230", table.GLOBL),
    0x8032231C: table.sym("audio_g_8032231C", table.GLOBL),
    0x80322348: table.sym("audio_g_80322348"), # unused
    0x8032235C: table.sym("audio_g_8032235C"), # unused

    0x00108A40: table.sym("data_main_end"),
}

fnc_E0_t_main = {
    0x80248AA4: 0x00108A10,
    # 0x80248AA8: 0x00108A10,
    # 0x80248AAC: 0x00108A10,
    0x80248AB0: 0x00108A10,
    0x80248AC0: 0x00108A40,
    0x80248AC4: 0x00108A40,
    0x80248AC8: 0x00108A40,
    0x80248ACC: 0x00108A40,

    0x80278994: 0x000F5580,
    0x80278998: 0x000F5580,
    0x8027899C: 0x000F5580,
    0x802789A0: 0x000F5580,
    0x802789CC: 0x000F5580,
    0x802789D0: 0x000F5580,
    0x802789D4: 0x000F5580,
    0x802789D8: 0x000F5580,
}

imm_E0_t_main = {
    0x802462E8: "SEGMENT_MEM_START >> 16",
    0x802462EC: "SEGMENT_MEM_START & 0xFFFF",
    0x802462F4: "SEGMENT_MEM_END >> 16",
    0x802462F8: "SEGMENT_MEM_END & 0xFFFF",

    0x8027897C: "SEGMENT_MAIN2 >> 16",
    0x80278980: "SEGMENT_MAIN2 & 0xFFFF",
    0x80278988: "(SEGMENT_CIMG-SEGMENT_MAIN2) >> 16",
    0x8027898C: "(SEGMENT_CIMG-SEGMENT_MAIN2) & 0xFFFF",
}

sym_E0_d_main = {
    # ==========================================================================
    # data
    # ==========================================================================

    # src/main.data.c
    0x8032D560: table.sym_var("scheduler_vq_audio",     "struct vq_t *"),
    0x8032D564: table.sym_var("scheduler_vq_video",     "struct vq_t *"),
    0x8032D568: table.sym_var("scheduler_task",         "struct sptask_t *"),
    0x8032D56C: table.sym_var("scheduler_audtask",      "struct sptask_t *"),
    0x8032D570: table.sym_var("scheduler_gfxtask",      "struct sptask_t *"),
    0x8032D574: table.sym_var("scheduler_audtask_next", "struct sptask_t *"),
    0x8032D578: table.sym_var("scheduler_gfxtask_next", "struct sptask_t *"),
    0x8032D57C: table.sym_var("scheduler_audio",        "s8"),
    0x8032D580: table.sym_var("scheduler_vi",           "u32"),
    0x8032D584: table.sym_var("scheduler_reset",        "s8"),
    0x8032D588: table.sym_var("scheduler_reset_timer",  "s8"),
    0x8032D58C: table.sym_var("debug_stage",            "s8"),
    0x8032D590: table.sym_var("debug_thread",           "s8"),
    0x8032D594: table.sym_var("debug_time",             "s8"),
    0x8032D598: table.sym_var("debug_mem",              "s8"),
    0x8032D59C: table.sym_var("debug_time_table",       "u16", "[]"),
    0x8032D5AC: table.sym_var("debug_mem_table",        "u16", "[]"),
    0x8032D5BC: table.sym_var("debug_time_index",       "s16"),
    0x8032D5C0: table.sym_var("debug_mem_index",        "s16"),

    # src/app.data.c
    0x8032D5D4: table.sym_var("video_frame",    "u32"),
    0x8032D5D8: table.sym_var("video_vi",       "u16"),
    0x8032D5DC: table.sym_var("video_dl",       "u16"),
    0x8032D5E0: table.sym_var_fnc("video_callback"),
    0x8032D5EC: table.sym_var("controller_p1",  "struct controller_t *"),

    0x80330D30: table.sym("_80330D30"),
    0x80330D78: table.sym("_80330D78"),

    # ==========================================================================
    # rodata
    # ==========================================================================

    # ==========================================================================
    # bss
    # ==========================================================================

    # src/main.data.c
    0x8033A580: table.sym_var("thread_fault",       "OSThread"),
    0x8033A730: table.sym_var("thread_idle",        "OSThread"),
    0x8033A8E0: table.sym_var("thread_scheduler",   "OSThread"),
    0x8033AA90: table.sym_var("thread_app",         "OSThread"),
    0x8033AC40: table.sym_var("thread_audio",       "OSThread"),
    0x8033ADF0: table.sym_var("mq_pi",              "OSMesgQueue"),
    0x8033AE08: table.sym_var("mq_scheduler",       "OSMesgQueue"),
    0x8033AE20: table.sym_var("mq_scheduler_task",  "OSMesgQueue"),
    0x8033AE38: table.sym_var("msg_app",            "OSMesg", "[2]"),
    0x8033AE40: table.sym_var("msg_pi",             "OSMesg", "[32]"),
    0x8033AEC0: table.sym_var("msg_si",             "OSMesg", "[2]"),
    0x8033AEC8: table.sym_var("msg_scheduler",      "OSMesg", "[16]"),
    0x8033AF08: table.sym_var("msg_scheduler_task", "OSMesg", "[16]"),
    0x8033AF48: table.sym_var("iomesg_app",         "OSIoMesg"),
    0x8033AF5C: table.sym_var("msg_null",           "OSMesg", "[1]"),
    0x8033AF60: table.sym_var("mq_app",             "OSMesgQueue"),
    0x8033AF78: table.sym_var("mq_si",              "OSMesgQueue"),

    # src/app.data.c
    0x8033AF90: table.sym_var("controller_table", "struct controller_t", "[3]"),
    0x8033AFE8: table.sym_var("contstatus_table", "OSContStatus", "[4]"),
    0x8033AFF8: table.sym_var("contpad_table",    "OSContPad", "[4]"),
    0x8033B010: table.sym_var("video_vq",   "struct vq_t"),
    0x8033B068: table.sym_var("video_task", "OSTask *"),
    0x8033B06C: table.sym_var("video_gfx",  "Gfx *"),
    0x8033B070: table.sym_var("video_mem",  "u8 *"),
    0x8033B074: table.sym_var("video_buf",  "struct video_buf_t *"),

    0x004EC000: table.sym("data_motion_player_start"),
    0x00579C20: table.sym("data_demo_start"),
    0x0057B720: table.sym("data_audio_ctl_start"),
    0x00593560: table.sym("data_audio_tbl_start"),
    0x007B0860: table.sym("data_audio_seq_start"),
    0x007CC620: table.sym("data_audio_bnk_start"),
}

sym_E0_t_main2 = {
    0x000F5580: table.sym("main2_start"),
    0x00108A10: table.sym("main2_end"),

    # src/math.S
    0x80378800: table.sym("math_80378800", table.GLOBL),
    0x80378840: table.sym("math_80378840", table.GLOBL),
    0x8037888C: table.sym("math_8037888C", table.GLOBL),
    0x803788E4: table.sym("math_803788E4"), # unused
    0x8037893C: table.sym("math_8037893C", table.GLOBL),
    0x8037897C: table.sym("math_8037897C", table.GLOBL),
    0x803789C8: table.sym("math_803789C8"), # unused
    0x80378A20: table.sym("math_80378A20"), # unused
    0x80378A78: table.sym("math_80378A78"), # unused
    0x80378AD0: table.sym("math_80378AD0", table.GLOBL),
    0x80378B34: table.sym("math_80378B34", table.GLOBL),
    0x80378C50: table.sym("math_80378C50"),
    0x80378D38: table.sym("math_80378D38"),
    0x80378DC0: table.sym("math_80378DC0"),
    0x80378E68: table.sym("math_80378E68", table.GLOBL),
    0x80378EB4: table.sym("math_80378EB4", table.GLOBL),
    0x80378F24: table.sym("math_80378F24", table.GLOBL),
    0x80378F84: table.sym("math_80378F84", table.GLOBL),
    0x80379440: table.sym("math_80379440", table.GLOBL),
    0x803795F0: table.sym("math_803795F0", table.GLOBL),
    0x80379798: table.sym("math_80379798", table.GLOBL),
    0x80379918: table.sym("math_80379918", table.GLOBL),
    0x80379AA4: table.sym("math_80379AA4", table.GLOBL),
    0x80379F60: table.sym("math_80379F60", table.GLOBL),
    0x8037A29C: table.sym("math_8037A29C", table.GLOBL),
    0x8037A348: table.sym("math_8037A348"), # unused
    0x8037A434: table.sym("math_8037A434", table.GLOBL),
    0x8037A4B8: table.sym("math_8037A4B8", table.GLOBL),
    0x8037A550: table.sym("math_8037A550", table.GLOBL),
    0x8037A69C: table.sym("math_8037A69C", table.GLOBL),
    0x8037A788: table.sym("math_8037A788", table.GLOBL),
    0x8037A860: table.sym("math_8037A860", table.GLOBL),
    0x8037A8B4: table.sym("math_8037A8B4", table.GLOBL),
    0x8037A924: table.sym("math_8037A924"),
    0x8037A9A8: table.sym("math_8037A9A8", table.GLOBL),
    0x8037AB88: table.sym("math_8037AB88"), # unused
    0x8037ABEC: table.sym("math_8037ABEC"),
    0x8037AC74: table.sym_fnc("L8037AC74", flag=table.GLOBL),
    0x8037AD04: table.sym_fnc("L8037AD04", flag=table.GLOBL),
    0x8037ADC0: table.sym_fnc("L8037ADC0", flag=table.GLOBL),
    0x8037AE5C: table.sym_fnc("L8037AE5C", flag=table.GLOBL),
    0x8037AF18: table.sym_fnc("L8037AF18", flag=table.GLOBL),
    0x8037AFB8: table.sym("math_8037AFB8", table.GLOBL),
    0x8037AFE8: table.sym("math_8037AFE8", table.GLOBL),

    # src/g.S
    0x8037B220: table.sym("g_8037B220"),
    0x8037B24C: table.sym("g_8037B24C", table.GLOBL),
    0x8037B30C: table.sym("g_8037B30C", table.GLOBL),
    0x8037B380: table.sym("g_8037B380", table.GLOBL),
    0x8037B448: table.sym("g_8037B448", table.GLOBL),
    0x8037B4AC: table.sym("g_8037B4AC", table.GLOBL),
    0x8037B530: table.sym("g_8037B530", table.GLOBL),
    0x8037B5B4: table.sym("g_8037B5B4", table.GLOBL),
    0x8037B670: table.sym("g_8037B670", table.GLOBL),
    0x8037B744: table.sym("g_8037B744", table.GLOBL),
    0x8037B7F8: table.sym("g_8037B7F8", table.GLOBL),
    0x8037B89C: table.sym("g_8037B89C", table.GLOBL),
    0x8037B940: table.sym("g_8037B940", table.GLOBL),
    0x8037B9E0: table.sym("g_8037B9E0", table.GLOBL),
    0x8037BAD4: table.sym("g_8037BAD4", table.GLOBL),
    0x8037BB48: table.sym("g_8037BB48", table.GLOBL),
    0x8037BBEC: table.sym("g_8037BBEC", table.GLOBL),
    0x8037BC90: table.sym("g_8037BC90", table.GLOBL),
    0x8037BD24: table.sym("g_8037BD24", table.GLOBL),
    0x8037BDB4: table.sym("g_8037BDB4", table.GLOBL),
    0x8037BE28: table.sym("g_8037BE28", table.GLOBL),
    0x8037BECC: table.sym("g_8037BECC", table.GLOBL),
    0x8037BF84: table.sym("g_8037BF84", table.GLOBL),
    0x8037C044: table.sym("g_8037C044", table.GLOBL),
    0x8037C0BC: table.sym("g_8037C0BC", table.GLOBL),
    0x8037C138: table.sym("g_8037C138", table.GLOBL),
    0x8037C1E4: table.sym("g_8037C1E4"),
    0x8037C360: table.sym("g_8037C360", table.GLOBL),
    0x8037C3D0: table.sym("g_8037C3D0", table.GLOBL),
    0x8037C448: table.sym("g_8037C448", table.GLOBL),
    0x8037C51C: table.sym("g_8037C51C", table.GLOBL),
    0x8037C658: table.sym("g_8037C658", table.GLOBL),
    0x8037C708: table.sym("g_8037C708", table.GLOBL),
    0x8037C7D8: table.sym("g_8037C7D8", table.GLOBL),
    0x8037C844: table.sym("g_8037C844", table.GLOBL),
    0x8037C9E8: table.sym("g_8037C9E8"), # unused
    0x8037CB10: table.sym("g_8037CB10"), # unused
    0x8037CB60: table.sym("g_8037CB60", table.GLOBL),
    0x8037CBC0: table.sym("g_8037CBC0", table.GLOBL),
    0x8037CBFC: table.sym("g_8037CBFC", table.GLOBL),
    0x8037CC74: table.sym("g_8037CC74", table.GLOBL),

    # src/g_script.S
    0x8037CD60: table.sym_fnc("g_script_00", flag=table.GLOBL), # data
    0x8037CE24: table.sym_fnc("g_script_01", flag=table.GLOBL), # data
    0x8037CEE8: table.sym_fnc("g_script_02", flag=table.GLOBL), # data
    0x8037CF70: table.sym_fnc("g_script_03", flag=table.GLOBL), # data
    0x8037CFC0: table.sym_fnc("g_script_04", flag=table.GLOBL), # data
    0x8037D018: table.sym_fnc("g_script_05", flag=table.GLOBL), # data
    0x8037D050: table.sym_fnc("g_script_06", flag=table.GLOBL), # data
    0x8037D0D0: table.sym_fnc("g_script_07", flag=table.GLOBL), # data
    0x8037D1D0: table.sym_fnc("g_script_08", flag=table.GLOBL), # data
    0x8037D328: table.sym_fnc("g_script_09", flag=table.GLOBL), # data
    0x8037D3A4: table.sym_fnc("g_script_0A", flag=table.GLOBL), # data
    0x8037D48C: table.sym_fnc("g_script_0B", flag=table.GLOBL), # data
    0x8037D4DC: table.sym_fnc("g_script_1F", flag=table.GLOBL), # data
    0x8037D500: table.sym_fnc("g_script_0C", flag=table.GLOBL), # data
    0x8037D55C: table.sym_fnc("g_script_0D", flag=table.GLOBL), # data
    0x8037D5D4: table.sym_fnc("g_script_0E", flag=table.GLOBL), # data
    0x8037D640: table.sym_fnc("g_script_0F", flag=table.GLOBL), # data
    0x8037D6F0: table.sym_fnc("g_script_10", flag=table.GLOBL), # data
    0x8037D8D4: table.sym_fnc("g_script_11", flag=table.GLOBL), # data
    0x8037D998: table.sym_fnc("g_script_12", flag=table.GLOBL), # data
    0x8037DA5C: table.sym_fnc("g_script_1D", flag=table.GLOBL), # data
    0x8037DB50: table.sym_fnc("g_script_1E", flag=table.GLOBL), # data
    0x8037DB74: table.sym_fnc("g_script_13", flag=table.GLOBL), # data
    0x8037DC10: table.sym_fnc("g_script_14", flag=table.GLOBL), # data
    0x8037DCD4: table.sym_fnc("g_script_15", flag=table.GLOBL), # data
    0x8037DD4C: table.sym_fnc("g_script_16", flag=table.GLOBL), # data
    0x8037DDDC: table.sym_fnc("g_script_17", flag=table.GLOBL), # data
    0x8037DE34: table.sym_fnc("g_script_18", flag=table.GLOBL), # data
    0x8037DE94: table.sym_fnc("g_script_19", flag=table.GLOBL), # data
    0x8037DEF8: table.sym_fnc("g_script_1A", flag=table.GLOBL), # data
    0x8037DF1C: table.sym_fnc("g_script_1B", flag=table.GLOBL), # data
    0x8037DFD4: table.sym_fnc("g_script_1C", flag=table.GLOBL), # data
    0x8037E058: table.sym_fnc("g_script_20", flag=table.GLOBL), # data
    0x8037E0B4: table.sym("g_script_main", table.GLOBL),

    # src/s_script.S
    0x8037E1A0: table.sym("s_script_8037E1A0"),
    0x8037E1D4: table.sym_fnc("L8037E1D4", flag=table.GLOBL),
    0x8037E1EC: table.sym_fnc("L8037E1EC", flag=table.GLOBL),
    0x8037E20C: table.sym_fnc("L8037E20C", flag=table.GLOBL),
    0x8037E228: table.sym_fnc("L8037E228", flag=table.GLOBL),
    0x8037E244: table.sym_fnc("L8037E244", flag=table.GLOBL),
    0x8037E25C: table.sym_fnc("L8037E25C", flag=table.GLOBL),
    0x8037E278: table.sym_fnc("L8037E278", flag=table.GLOBL),
    0x8037E290: table.sym_fnc("L8037E290", flag=table.GLOBL),
    0x8037E2C4: table.sym_fnc("s_script_00", flag=table.GLOBL), # data
    0x8037E388: table.sym_fnc("s_script_01", flag=table.GLOBL), # data
    0x8037E404: table.sym_fnc("s_script_02", flag=table.GLOBL), # data
    0x8037E47C: table.sym_fnc("s_script_03", flag=table.GLOBL), # data
    0x8037E4FC: table.sym_fnc("s_script_04", flag=table.GLOBL), # data
    0x8037E580: table.sym_fnc("s_script_05", flag=table.GLOBL), # data
    0x8037E5B8: table.sym_fnc("s_script_06", flag=table.GLOBL), # data
    0x8037E620: table.sym_fnc("s_script_07", flag=table.GLOBL), # data
    0x8037E650: table.sym_fnc("s_script_08", flag=table.GLOBL), # data
    0x8037E6D4: table.sym_fnc("s_script_09", flag=table.GLOBL), # data
    0x8037E780: table.sym_fnc("s_script_0A", flag=table.GLOBL), # data
    0x8037E7F8: table.sym_fnc("s_script_0B", flag=table.GLOBL), # data
    0x8037E878: table.sym_fnc("s_script_0C", flag=table.GLOBL), # data
    0x8037E8E8: table.sym_fnc("s_script_0D", flag=table.GLOBL), # data
    0x8037E988: table.sym_fnc("s_script_0E", flag=table.GLOBL), # data
    0x8037EA18: table.sym_fnc("s_script_0F", flag=table.GLOBL), # data
    0x8037EA70: table.sym_fnc("s_script_10", flag=table.GLOBL), # data
    0x8037EA98: table.sym_fnc("s_script_11", flag=table.GLOBL), # data
    0x8037EB04: table.sym_fnc("s_script_12", flag=table.GLOBL), # data
    0x8037EB98: table.sym_fnc("s_script_13", flag=table.GLOBL), # data
    0x8037EBD4: table.sym_fnc("s_script_14", flag=table.GLOBL), # data
    0x8037EC14: table.sym_fnc("s_script_15", flag=table.GLOBL), # data
    0x8037EC54: table.sym_fnc("s_script_16", flag=table.GLOBL), # data
    0x8037ECA4: table.sym_fnc("s_script_17", flag=table.GLOBL), # data
    0x8037ECF8: table.sym_fnc("s_script_18", flag=table.GLOBL), # data
    0x8037ED48: table.sym_fnc("s_script_19", flag=table.GLOBL), # data
    0x8037EDF8: table.sym_fnc("s_script_1A", flag=table.GLOBL), # data
    0x8037EE48: table.sym_fnc("s_script_1B", flag=table.GLOBL), # data
    0x8037EEA8: table.sym_fnc("s_script_1C", flag=table.GLOBL), # data
    0x8037EF00: table.sym_fnc("s_script_1D", flag=table.GLOBL), # data
    0x8037EF70: table.sym_fnc("s_script_1E", flag=table.GLOBL), # data
    0x8037F010: table.sym_fnc("s_script_1F", flag=table.GLOBL), # data
    0x8037F130: table.sym_fnc("s_script_20", flag=table.GLOBL), # data
    0x8037F164: table.sym_fnc("s_script_21", flag=table.GLOBL), # data
    0x8037F214: table.sym_fnc("s_script_22", flag=table.GLOBL), # data
    0x8037F2A4: table.sym_fnc("s_script_23", flag=table.GLOBL), # data
    0x8037F36C: table.sym_fnc("s_script_25", flag=table.GLOBL), # data
    0x8037F45C: table.sym_fnc("s_script_24", flag=table.GLOBL), # data
    0x8037F67C: table.sym_fnc("s_script_26", flag=table.GLOBL), # data
    0x8037F790: table.sym_fnc("s_script_28", flag=table.GLOBL), # data
    0x8037F920: table.sym_fnc("s_script_31", flag=table.GLOBL), # data
    0x8037F994: table.sym_fnc("s_script_27", flag=table.GLOBL), # data
    0x8037FB18: table.sym_fnc("s_script_3A", flag=table.GLOBL), # data
    0x8037FC38: table.sym_fnc("s_script_3B", flag=table.GLOBL), # data
    0x8037FDE4: table.sym_fnc("s_script_34", flag=table.GLOBL), # data
    0x8037FE2C: table.sym_fnc("s_script_35", flag=table.GLOBL), # data
    0x8037FE94: table.sym_fnc("s_script_2E", flag=table.GLOBL), # data
    0x8037FF14: table.sym_fnc("s_script_2F", flag=table.GLOBL), # data
    0x8037FF94: table.sym_fnc("s_script_39", flag=table.GLOBL), # data
    0x80380014: table.sym_fnc("s_script_29", flag=table.GLOBL), # data
    0x8038007C: table.sym_fnc("s_script_2A", flag=table.GLOBL), # data
    0x803800BC: table.sym_fnc("s_script_2B", flag=table.GLOBL), # data
    0x80380160: table.sym_fnc("s_script_2C", flag=table.GLOBL), # data
    0x803801A0: table.sym_fnc("s_script_2D", flag=table.GLOBL), # data
    0x803801E0: table.sym_fnc("s_script_33", flag=table.GLOBL), # data
    0x8038024C: table.sym_fnc("s_script_32", flag=table.GLOBL), # data
    0x80380274: table.sym_fnc("s_script_30", flag=table.GLOBL), # data
    0x80380300: table.sym_fnc("s_script_36", flag=table.GLOBL), # data
    0x8038039C: table.sym_fnc("s_script_37", flag=table.GLOBL), # data
    0x803803EC: table.sym_fnc("s_script_38", flag=table.GLOBL), # data
    0x80380434: table.sym_fnc("s_script_3C", flag=table.GLOBL), # data
    0x80380478: table.sym_fnc("L80380478", flag=table.GLOBL),
    0x80380490: table.sym_fnc("L80380490", flag=table.GLOBL),
    0x803804A8: table.sym_fnc("L803804A8", flag=table.GLOBL),
    0x803804C0: table.sym_fnc("L803804C0", flag=table.GLOBL),
    0x803804D8: table.sym_fnc("L803804D8", flag=table.GLOBL),
    0x80380528: table.sym_fnc("L80380528", flag=table.GLOBL),
    0x80380540: table.sym_fnc("L80380540", flag=table.GLOBL),
    0x80380558: table.sym_fnc("L80380558", flag=table.GLOBL),
    0x80380570: table.sym_fnc("L80380570", flag=table.GLOBL),
    0x80380588: table.sym_fnc("L80380588", flag=table.GLOBL),
    0x803805C8: table.sym("s_script_main", table.GLOBL),

    # src/map.S
    0x80380690: table.sym("map_80380690"),
    0x80380DE8: table.sym("map_80380DE8", table.GLOBL),
    0x80380E8C: table.sym("map_80380E8C", table.GLOBL),
    0x80381038: table.sym("map_80381038"),
    0x80381264: table.sym("map_80381264", table.GLOBL),
    0x80381470: table.sym("map_80381470"), # unused
    0x803814B8: table.sym("map_803814B8", table.GLOBL),
    0x8038156C: table.sym("map_8038156C"),
    0x80381794: table.sym("map_80381794", table.GLOBL),
    0x803817E0: table.sym("map_803817E0"), # unused
    0x80381900: table.sym("map_80381900", table.GLOBL),
    0x80381BA0: table.sym("map_80381BA0", table.GLOBL),
    0x80381D3C: table.sym("map_80381D3C", table.GLOBL),
    0x80381EC8: table.sym("map_80381EC8"),
    0x80381F08: table.sym("map_80381F08", table.GLOBL),
    0x80382294: table.sym("map_80382294"), # unused

    # src/map_data.S
    0x80382490: table.sym("map_data_80382490"),
    0x803824F8: table.sym("map_data_803824F8"),
    0x80382590: table.sym("map_data_80382590"),
    0x803825D0: table.sym("map_data_803825D0"),
    0x803825FC: table.sym("map_data_803825FC"),
    0x8038283C: table.sym("map_data_8038283C"),
    0x8038289C: table.sym("map_data_8038289C"),
    0x803828FC: table.sym("map_data_803828FC"),
    0x80382990: table.sym("map_data_80382990"),
    0x80382A2C: table.sym("map_data_80382A2C"),
    0x80382B6C: table.sym("map_data_80382B6C"), # unused
    0x80382B7C: table.sym("map_data_80382B7C"),
    0x80382F84: table.sym("map_data_80382F84"),
    0x80382FBC: table.sym_fnc("L80382FBC", flag=table.GLOBL),
    0x80382FCC: table.sym_fnc("L80382FCC", flag=table.GLOBL),
    0x80382FEC: table.sym("map_data_80382FEC"),
    0x80383068: table.sym("map_data_80383068"),
    0x803831D0: table.sym("map_data_803831D0"),
    0x80383228: table.sym("map_data_80383228"),
    0x80383340: table.sym("map_data_80383340", table.GLOBL),
    0x803833B8: table.sym("map_data_803833B8", table.GLOBL),
    0x803835A4: table.sym("map_data_803835A4", table.GLOBL),
    0x80383604: table.sym("map_data_80383604"), # unused
    0x80383614: table.sym("map_data_80383614"),
    0x80383828: table.sym("map_data_80383828"),
    0x803839CC: table.sym("map_data_803839CC", table.GLOBL), # o callback

    # src/o_script.S
    0x80383B70: table.sym("o_script_80383B70"), # unused
    0x80383BB0: table.sym("o_script_80383BB0", table.GLOBL),
    0x80383CB4: table.sym("o_script_80383CB4", table.GLOBL),
    0x80383D1C: table.sym("o_script_80383D1C", table.GLOBL),
    0x80383D68: table.sym("o_script_80383D68"),
    0x80383DBC: table.sym("o_script_80383DBC"),
    0x80383DF8: table.sym("o_script_80383DF8"),
    0x80383E44: table.sym("o_script_80383E44"), # unused
    0x80383E5C: table.sym_fnc("o_script_22", "int", flag=table.GLOBL), # data
    0x80383EA0: table.sym_fnc("o_script_35", "int", flag=table.GLOBL), # data
    0x80383EE4: table.sym_fnc("o_script_21", "int", flag=table.GLOBL), # data
    0x80383F24: table.sym_fnc("o_script_1B", "int", flag=table.GLOBL), # data
    0x80383F94: table.sym_fnc("o_script_1C", "int", flag=table.GLOBL), # data
    0x8038401C: table.sym_fnc("o_script_2C", "int", flag=table.GLOBL), # data
    0x803840B4: table.sym_fnc("o_script_29", "int", flag=table.GLOBL), # data
    0x80384164: table.sym_fnc("o_script_1D", "int", flag=table.GLOBL), # data
    0x80384188: table.sym_fnc("o_script_0A", "int", flag=table.GLOBL), # data
    0x803841A0: table.sym_fnc("o_script_0B", "int", flag=table.GLOBL), # data
    0x803841B8: table.sym_fnc("o_script_02", "int", flag=table.GLOBL), # data
    0x80384224: table.sym_fnc("o_script_03", "int", flag=table.GLOBL), # data
    0x8038425C: table.sym_fnc("o_script_01", "int", flag=table.GLOBL), # data
    0x803842E4: table.sym_fnc("o_script_25", "int", flag=table.GLOBL), # data
    0x8038438C: table.sym_fnc("o_script_04", "int", flag=table.GLOBL), # data
    0x803843E0: table.sym_fnc("o_script_26", "int", flag=table.GLOBL), # data
    0x80384450: table.sym_fnc("o_script_05", "int", flag=table.GLOBL), # data
    0x803844C0: table.sym_fnc("o_script_06", "int", flag=table.GLOBL), # data
    0x80384554: table.sym_fnc("o_script_07", "int", flag=table.GLOBL), # data
    0x803845E8: table.sym_fnc("o_script_08", "int", flag=table.GLOBL), # data
    0x80384634: table.sym_fnc("o_script_09", "int", flag=table.GLOBL), # data
    0x80384678: table.sym_fnc("o_script_0C", "int", flag=table.GLOBL), # data
    0x803846D0: table.sym_fnc("o_script_0E", "int", flag=table.GLOBL), # data
    0x8038475C: table.sym_fnc("o_script_10", "int", flag=table.GLOBL), # data
    0x803847D4: table.sym_fnc("o_script_36", "int", flag=table.GLOBL), # data
    0x80384854: table.sym_fnc("o_script_14", "int", flag=table.GLOBL), # data
    0x80384928: table.sym_fnc("o_script_15", "int", flag=table.GLOBL), # data
    0x803849F8: table.sym_fnc("o_script_13", "int", flag=table.GLOBL), # data
    0x80384AB4: table.sym_fnc("o_script_16", "int", flag=table.GLOBL), # data
    0x80384B90: table.sym_fnc("o_script_17", "int", flag=table.GLOBL), # data
    0x80384C5C: table.sym_fnc("o_script_0D", "int", flag=table.GLOBL), # data
    0x80384CF0: table.sym_fnc("o_script_0F", "int", flag=table.GLOBL), # data
    0x80384D70: table.sym_fnc("o_script_11", "int", flag=table.GLOBL), # data
    0x80384E04: table.sym_fnc("o_script_12", "int", flag=table.GLOBL), # data
    0x80384E9C: table.sym_fnc("o_script_27", "int", flag=table.GLOBL), # data
    0x80384F08: table.sym_fnc("o_script_28", "int", flag=table.GLOBL), # data
    0x80384F8C: table.sym_fnc("o_script_1E", "int", flag=table.GLOBL), # data
    0x8038503C: table.sym_fnc("o_script_18", "int", flag=table.GLOBL), # data
    0x80385084: table.sym_fnc("o_script_1A", "int", flag=table.GLOBL), # data
    0x803850CC: table.sym_fnc("o_script_19", "int", flag=table.GLOBL), # data
    0x80385114: table.sym_fnc("o_script_1F", "int", flag=table.GLOBL), # data
    0x803851D0: table.sym_fnc("o_script_20", "int", flag=table.GLOBL), # data
    0x8038528C: table.sym_fnc("o_script_23", "int", flag=table.GLOBL), # data
    0x8038531C: table.sym_fnc("o_script_2E", "int", flag=table.GLOBL), # data
    0x803853AC: table.sym_fnc("o_script_2B", "int", flag=table.GLOBL), # data
    0x8038546C: table.sym_fnc("o_script_24", "int", flag=table.GLOBL), # data
    0x803854CC: table.sym_fnc("o_script_00", "int", flag=table.GLOBL), # data
    0x8038556C: table.sym("o_script_8038556C"), # unused
    0x803856A0: table.sym_fnc("o_script_2A", "int", flag=table.GLOBL), # data
    0x80385700: table.sym_fnc("o_script_2D", "int", flag=table.GLOBL), # data
    0x8038575C: table.sym_fnc("o_script_2F", "int", flag=table.GLOBL), # data
    0x803857A0: table.sym_fnc("o_script_31", "int", flag=table.GLOBL), # data
    0x803857E4: table.sym_fnc("o_script_32", "int", flag=table.GLOBL), # data
    0x8038586C: table.sym_fnc("o_script_30", "int", flag=table.GLOBL), # data
    0x80385A60: table.sym_fnc("o_script_33", "int", flag=table.GLOBL), # data
    0x80385AF0: table.sym_fnc("o_script_37", "int", flag=table.GLOBL), # data
    0x80385B4C: table.sym_fnc("o_script_34", "int", flag=table.GLOBL), # data
    0x80385BF0: table.sym("o_script_80385BF0", table.GLOBL),
    0x80385C00: table.sym("o_script_main", table.GLOBL),
}

sym_E0_d_main2 = {
    # src/math.data.c
    0x80385F90: table.sym_var("mtx_identity", "Mtx"), # unused
    0x80385FD0: table.sym_var("vecf_0", "vecf"),
    0x80385FDC: table.sym_var("vecs_0", "vecs"),
    0x80385FE4: table.sym_var("vecf_1", "vecf"),
    0x80385FF0: table.sym_var("vecs_1", "vecs"), # unused

    # src/math_table.c
    0x80386000: table.sym_var("math_sin", "f32", "[]"),
    0x80387000: table.sym_var("math_cos", "f32", "[]"),
    0x8038B000: table.sym_var("math_atan", "s16", "[]"),

    # src/g_script.data.c
    0x8038B810: table.sym_var_fnc("g_script_table", lst="[]"),

    # src/s_script.data.c
    0x8038B8A0: table.sym_var("s_script_arena", "void *"),
    0x8038B8A4: table.sym_var("s_script_8038B8A4", "aligned u16"),
    0x8038B8A8: table.sym_var("s_script_8038B8A8", "aligned u16"),
    0x8038B8AC: table.sym_var("s_script_8038B8AC", "aligned s16"),
    0x8038B8B0: table.sym_var("s_script_8038B8B0", "void *"),
    0x8038B8B4: table.sym_var("s_script_8038B8B4", "void *"),
    0x8038B8B8: table.sym_var_fnc("s_script_table", lst="[]"),

    # src/o_script.data.c
    0x8038B9B0: table.sym_var_fnc("o_script_table", lst="[]", val="int"),

    # src/math.data.c
    0x8038BA90: table.sym_var("math_8038BA90", "const f64"),
    0x8038BA98: table.sym_var_fnc("math_8038BA98", "const", "[]"),
    0x8038BAAC: table.sym_var("math_8038BAAC", "const f32"),
    0x8038BAB0: table.sym_var("math_8038BAB0", "const f32"),
    0x8038BAB4: table.sym_var("math_8038BAB4", "const f32"),
    0x8038BAB8: table.sym_var("math_8038BAB8", "const f32"),
    0x8038BABC: table.sym_var("math_8038BABC", "const f32"),
    0x8038BAC0: table.sym_var("math_8038BAC0", "const f32"),
    0x8038BAC4: table.sym_var("math_8038BAC4", "const f32"),
    0x8038BAC8: table.sym_var("math_8038BAC8", "const f32"),
    0x8038BACC: table.sym_var("math_8038BACC", "const f32"),
    0x8038BAD0: table.sym_var("math_8038BAD0", "const f32"),
    0x8038BAD4: table.sym_var("math_8038BAD4", "const f32"),
    0x8038BAD8: table.sym_var("math_8038BAD8", "const f32"),
    0x8038BADC: table.sym_var("math_8038BADC", "const f32"),
    0x8038BAE0: table.sym_var("math_8038BAE0", "const f32"),
    0x8038BAE4: table.sym_var("math_8038BAE4", "const f32"),
    0x8038BAE8: table.sym_var("math_8038BAE8", "const f32"),

    # src/s_script.data.c
    0x8038BAF0: table.sym_var_fnc("s_script_8038BAF0", "const", "[]"),
    0x8038BB10: table.sym_var_fnc("s_script_8038BB10", "const", "[]"),
    0x8038BB24: table.sym_var_fnc("s_script_8038BB24", "const", "[]"),

    # src/map.data.c
    0x8038BB40: table.sym_var("map_8038BB40", "const char", "[]"),
    0x8038BB4C: table.sym_var("map_8038BB4C", "const char", "[]"),
    0x8038BB54: table.sym_var("map_8038BB54", "const char", "[]"),
    0x8038BB5C: table.sym_var("map_8038BB5C", "const char", "[]"),
    0x8038BB64: table.sym_var("map_8038BB64", "const char", "[]"),
    0x8038BB68: table.sym_var("map_8038BB68", "const char", "[]"),
    0x8038BB6C: table.sym_var("map_8038BB6C", "const char", "[]"),
    0x8038BB70: table.sym_var("map_8038BB70", "const char", "[]"),
    0x8038BB7C: table.sym_var("map_8038BB7C", "const char", "[]"),
    0x8038BB88: table.sym_var("map_8038BB88", "const char", "[]"),
    0x8038BB94: table.sym_var("map_8038BB94", "const f32"),
    0x8038BB98: table.sym_var("map_8038BB98", "const f32"),
    0x8038BB9C: table.sym_var("map_8038BB9C", "const f32"),
    0x8038BBA0: table.sym_var("map_8038BBA0", "const f32"),
    0x8038BBA4: table.sym_var("map_8038BBA4", "const f32"),
    0x8038BBA8: table.sym_var("map_8038BBA8", "const f32"),
    0x8038BBAC: table.sym_var("map_8038BBAC", "const f32"),

    # src/map_data.data.c
    0x8038BBB0: table.sym_var("map_data_8038BBB0", "const f64"),
    0x8038BBB8: table.sym_var("map_data_8038BBB8", "const f64"),
    0x8038BBC0: table.sym_var("map_data_8038BBC0", "const f64"),
    0x8038BBC8: table.sym_var("map_data_8038BBC8", "const f64"),
    0x8038BBD0: table.sym_var("map_data_8038BBD0", "const f64"),
    0x8038BBD8: table.sym_var_fnc("map_data_8038BBD8", "const", "[]"),
    0x8038BC80: table.sym_var("map_data_8038BC80", "const f32"),
}

sym_E0_t_menu = {
    0x0021F4C0: table.sym("menu_start"),

    # src/title.S
    0x8016F000: table.sym("title_8016F000"),
    0x8016F128: table.sym("title_8016F128"),
    0x8016F3CC: table.sym("title_8016F3CC"),
    0x8016F4B0: table.sym("title_8016F4B0"),
    0x8016F564: table.sym("title_8016F564"),
    0x8016F5B0: table.sym("title_8016F5B0", table.GLOBL), # s callback

    # src/title_bg.S
    0x8016F670: table.sym("title_bg_8016F670", table.GLOBL), # g callback
    0x8016F984: table.sym("title_bg_8016F984", table.GLOBL), # g callback
    0x8016FBB0: table.sym("title_bg_8016FBB0"),
    0x8016FE70: table.sym("title_bg_8016FE70", table.GLOBL), # g callback
    0x8016FFFC: table.sym("title_bg_8016FFFC", table.GLOBL), # g callback

    # src/file_select.S
    0x80170280: table.sym("file_select_80170280", table.GLOBL), # o callback
    0x801702B8: table.sym("file_select_801702B8", table.GLOBL), # o callback
    0x801702E8: table.sym("file_select_801702E8"),
    0x80170488: table.sym("file_select_80170488"),
    0x801705DC: table.sym("file_select_801705DC"),
    0x80170710: table.sym("file_select_80170710"),
    0x80170838: table.sym("file_select_80170838"),
    0x8017096C: table.sym("file_select_8017096C"),
    0x80170A4C: table.sym("file_select_80170A4C"),
    0x80170A9C: table.sym("file_select_80170A9C"),
    0x80170AEC: table.sym("file_select_80170AEC", table.GLOBL), # o callback
    0x80170B1C: table.sym("file_select_80170B1C", table.GLOBL), # o callback
    0x80170CB4: table.sym("file_select_80170CB4"),
    0x80170D60: table.sym("file_select_80170D60"),
    0x80171168: table.sym("file_select_80171168"),
    0x8017137C: table.sym("file_select_8017137C"),
    0x80171784: table.sym("file_select_80171784"),
    0x80171A2C: table.sym("file_select_80171A2C"),
    0x80171C0C: table.sym("file_select_80171C0C"),
    0x80172014: table.sym("file_select_80172014"),
    0x801721AC: table.sym("file_select_801721AC"),
    0x8017236C: table.sym("file_select_8017236C"),
    0x801724B8: table.sym("file_select_801724B8"),
    0x8017261C: table.sym("file_select_8017261C"),
    0x80172644: table.sym("file_select_80172644"),
    0x80172818: table.sym("file_select_80172818"),
    0x801729E0: table.sym("file_select_801729E0"),
    0x80172BA8: table.sym("file_select_80172BA8"),
    0x80172D70: table.sym("file_select_80172D70", table.GLOBL), # o callback
    0x801731A8: table.sym("file_select_801731A8"),
    0x80173430: table.sym("file_select_80173430", table.GLOBL), # o callback
    0x80173780: table.sym("file_select_80173780"),
    0x80173900: table.sym("file_select_80173900"),
    0x80173AE0: table.sym("file_select_80173AE0"),
    0x80173C6C: table.sym("file_select_80173C6C"),
    0x80173D64: table.sym("file_select_80173D64"),
    0x80173E54: table.sym("file_select_80173E54"),
    0x80173EE4: table.sym("file_select_80173EE4"),
    0x80173FD4: table.sym("file_select_80173FD4"),
    0x80174324: table.sym("file_select_80174324"),
    0x801743AC: table.sym("file_select_801743AC"),
    0x801746F8: table.sym("file_select_801746F8"),
    0x80174804: table.sym("file_select_80174804"),
    0x801749B0: table.sym("file_select_801749B0"),
    0x80174CA8: table.sym("file_select_80174CA8"),
    0x80175238: table.sym("file_select_80175238"),
    0x80175404: table.sym("file_select_80175404"),
    0x801755A8: table.sym("file_select_801755A8"),
    0x801758A0: table.sym("file_select_801758A0"),
    0x80175B14: table.sym("file_select_80175B14"),
    0x80175B90: table.sym("file_select_80175B90"),
    0x80175D2C: table.sym("file_select_80175D2C"),
    0x80175DFC: table.sym("file_select_80175DFC"),
    0x801764E0: table.sym("file_select_801764E0"),
    0x80176688: table.sym("file_select_80176688", table.GLOBL), # g callback
    0x801766DC: table.sym("file_select_801766DC", table.GLOBL), # s callback
    0x801768A0: table.sym("file_select_801768A0", table.GLOBL), # s callback

    # src/star_select.S
    0x801768E0: table.sym("star_select_801768E0", table.GLOBL), # o callback
    0x80176A74: table.sym("star_select_80176A74"),
    0x80176B20: table.sym("star_select_80176B20", table.GLOBL), # o callback
    0x80176DF0: table.sym("star_select_80176DF0", table.GLOBL), # o callback
    0x80176FC4: table.sym("star_select_80176FC4"),
    0x80177144: table.sym("star_select_80177144"),
    0x80177518: table.sym("star_select_80177518", table.GLOBL), # g callback
    0x80177560: table.sym("star_select_80177560", table.GLOBL), # s callback
    0x80177610: table.sym("star_select_80177610", table.GLOBL), # s callback

    # src/face/main.S
    0x80177710: table.sym("face_main_80177710"), # unused

    # src/face/mem.S
    0x80177820: table.sym("face_mem_80177820"),
    0x80177924: table.sym("face_mem_80177924"),
    0x801779DC: table.sym("face_mem_801779DC"),
    0x80177BB8: table.sym("face_mem_80177BB8", table.GLOBL),
    0x80177C58: table.sym("face_mem_80177C58", table.GLOBL),
    0x80177E7C: table.sym("face_mem_80177E7C", table.GLOBL),
    0x80177F0C: table.sym("face_mem_80177F0C", table.GLOBL),
    0x80177F34: table.sym("face_mem_80177F34"),
    0x801780B0: table.sym("face_mem_801780B0", table.GLOBL),

    # src/face/sfx.S
    0x801781E0: table.sym("face_sfx_801781E0", table.GLOBL),
    0x80178200: table.sym("face_sfx_80178200", table.GLOBL),
    0x8017822C: table.sym("face_sfx_8017822C", table.GLOBL),
    0x80178254: table.sym("face_sfx_80178254", table.GLOBL),

    # src/face/draw.S
    0x80178280: table.sym("face_draw_80178280"),
    0x8017831C: table.sym("face_draw_8017831C"), # unused
    0x801785DC: table.sym("face_draw_801785DC"),
    0x8017894C: table.sym("face_draw_8017894C"),
    0x80178A40: table.sym("face_draw_80178A40", table.GLOBL),
    0x80178C5C: table.sym("face_draw_80178C5C", table.GLOBL),
    0x80178D90: table.sym("face_draw_80178D90"),
    0x80178DEC: table.sym("face_draw_80178DEC"), # unused
    0x80178ED8: table.sym("face_draw_80178ED8", table.GLOBL),
    0x8017900C: table.sym("face_draw_8017900C"), # unused
    0x80179120: table.sym("face_draw_80179120", table.GLOBL),
    0x80179368: table.sym("face_draw_80179368"),
    0x801793CC: table.sym("face_draw_801793CC"),
    0x80179430: table.sym("face_draw_80179430"), # unused
    0x80179490: table.sym("face_draw_80179490", table.GLOBL),
    0x80179768: table.sym("face_draw_80179768", table.GLOBL),
    0x801798AC: table.sym("face_draw_801798AC", table.GLOBL),
    0x801799AC: table.sym("face_draw_801799AC", table.GLOBL),
    0x80179C0C: table.sym("face_draw_80179C0C"),
    0x80179CA4: table.sym("face_draw_80179CA4"),
    0x80179CDC: table.sym("face_draw_80179CDC", table.GLOBL),
    0x80179E08: table.sym("face_draw_80179E08"),
    0x8017A010: table.sym("face_draw_8017A010"),
    0x8017A344: table.sym("face_draw_8017A344", table.GLOBL),
    0x8017A358: table.sym("face_draw_8017A358"),
    0x8017A44C: table.sym("face_draw_8017A44C", table.GLOBL),
    0x8017A690: table.sym("face_draw_8017A690", table.GLOBL),
    0x8017A7E4: table.sym("face_draw_8017A7E4", table.GLOBL),
    0x8017A900: table.sym("face_draw_8017A900", table.GLOBL),
    0x8017A958: table.sym("face_draw_8017A958", table.GLOBL),
    0x8017A9E0: table.sym("face_draw_8017A9E0", table.GLOBL),
    0x8017AA5C: table.sym("face_draw_8017AA5C"),
    0x8017AAF0: table.sym("face_draw_8017AAF0"),
    0x8017AED8: table.sym("face_draw_8017AED8"),
    0x8017AFC8: table.sym("face_draw_8017AFC8"),
    0x8017B01C: table.sym("face_draw_8017B01C"), # unused
    0x8017B088: table.sym("face_draw_8017B088"),
    0x8017B168: table.sym("face_draw_8017B168", table.GLOBL),
    0x8017B1A4: table.sym("face_draw_8017B1A4", table.GLOBL),
    0x8017B258: table.sym("face_draw_8017B258"),
    0x8017B3DC: table.sym("face_draw_8017B3DC"),
    0x8017B538: table.sym("face_draw_8017B538", table.GLOBL),
    0x8017B608: table.sym("face_draw_8017B608"), # unused
    0x8017B654: table.sym("face_draw_8017B654"),
    0x8017B730: table.sym("face_draw_8017B730"),
    0x8017B764: table.sym("face_draw_8017B764", table.GLOBL),
    0x8017BDD4: table.sym("face_draw_8017BDD4"), # unused

    # src/face/object.S
    0x8017BDF0: table.sym("face_object_8017BDF0", table.GLOBL),
    0x8017BE60: table.sym("face_object_8017BE60", table.GLOBL),
    0x8017BFA0: table.sym("face_object_8017BFA0", table.GLOBL),
    0x8017C010: table.sym("face_object_8017C010", table.GLOBL),
    0x8017C034: table.sym("face_object_8017C034"),
    0x8017C300: table.sym("face_object_8017C300", table.GLOBL),
    0x8017C810: table.sym("face_object_8017C810", table.GLOBL),
    0x8017C8E0: table.sym("face_object_8017C8E0"), # unused
    0x8017C940: table.sym("face_object_8017C940", table.GLOBL),
    0x8017CA00: table.sym("face_object_8017CA00", table.GLOBL),
    0x8017CAC4: table.sym("face_object_8017CAC4", table.GLOBL),
    0x8017CB4C: table.sym("face_object_8017CB4C", table.GLOBL),
    0x8017CF7C: table.sym("face_object_8017CF7C", table.GLOBL),
    0x8017D010: table.sym("face_object_8017D010", table.GLOBL),
    0x8017D22C: table.sym("face_object_8017D22C", table.GLOBL),
    0x8017D2D4: table.sym("face_object_8017D2D4", table.GLOBL),
    0x8017D3E8: table.sym("face_object_8017D3E8", table.GLOBL),
    0x8017D67C: table.sym("face_object_8017D67C", table.GLOBL),
    0x8017D6F4: table.sym("face_object_8017D6F4", table.GLOBL),
    0x8017D76C: table.sym("face_object_8017D76C", table.GLOBL),
    0x8017D838: table.sym("face_object_8017D838", table.GLOBL),
    0x8017DA04: table.sym("face_object_8017DA04", table.GLOBL),
    0x8017DC14: table.sym("face_object_8017DC14", table.GLOBL),
    0x8017DD00: table.sym("face_object_8017DD00", table.GLOBL),
    0x8017DDFC: table.sym("face_object_8017DDFC", table.GLOBL),
    0x8017DE80: table.sym("face_object_8017DE80"), # unused
    0x8017E328: table.sym("face_object_8017E328"), # unused
    0x8017E34C: table.sym("face_object_8017E34C", table.GLOBL),
    0x8017E370: table.sym("face_object_8017E370"),
    0x8017E3F8: table.sym("face_object_8017E3F8", table.GLOBL),
    0x8017E430: table.sym("face_object_8017E430"),
    0x8017E520: table.sym("face_object_8017E520", table.GLOBL),
    0x8017E6C4: table.sym("face_object_8017E6C4", table.GLOBL),
    0x8017E978: table.sym("face_object_8017E978", table.GLOBL),
    0x8017EB2C: table.sym("face_object_8017EB2C", table.GLOBL),
    0x8017EBD4: table.sym("face_object_8017EBD4"), # unused
    0x8017EC64: table.sym("face_object_8017EC64"), # unused
    0x8017EE40: table.sym("face_object_8017EE40"), # unused
    0x8017EF0C: table.sym("face_object_8017EF0C"), # unused
    0x8017EF9C: table.sym("face_object_8017EF9C", table.GLOBL),
    0x8017F194: table.sym("face_object_8017F194", table.GLOBL),
    0x8017F350: table.sym("face_object_8017F350"),
    0x8017F50C: table.sym("face_object_8017F50C"), # unused
    0x8017F544: table.sym("face_object_8017F544"),
    0x8017F564: table.sym("face_object_8017F564"),
    0x8017F704: table.sym("face_object_8017F704"),
    0x80180764: table.sym("face_object_80180764"),
    0x80180A64: table.sym("face_object_80180A64"),
    0x80180AB4: table.sym("face_object_80180AB4", table.GLOBL),
    0x80180AF0: table.sym("face_object_80180AF0"),
    0x80181114: table.sym("face_object_80181114"),
    0x8018114C: table.sym("face_object_8018114C"),
    0x801814B8: table.sym("face_object_801814B8"),
    0x801814F0: table.sym("face_object_801814F0"),
    0x8018159C: table.sym("face_object_8018159C", table.GLOBL),
    0x80181634: table.sym("face_object_80181634", table.GLOBL),
    0x80181678: table.sym("face_object_80181678", table.GLOBL),

    # src/face/skin.S
    0x80181720: table.sym("face_skin_80181720"), # unused
    0x801818A0: table.sym("face_skin_801818A0", table.GLOBL),
    0x8018197C: table.sym("face_skin_8018197C", table.GLOBL),
    0x801819D4: table.sym("face_skin_801819D4", table.GLOBL),
    0x80181B10: table.sym("face_skin_80181B10"),
    0x80181C20: table.sym("face_skin_80181C20"),
    0x80181CC8: table.sym("face_skin_80181CC8", table.GLOBL),

    # src/face/particle.S
    0x80181D40: table.sym("face_particle_80181D40"),
    0x80181E54: table.sym("face_particle_80181E54"),
    0x80181FF0: table.sym("face_particle_80181FF0"),
    0x801821C8: table.sym("face_particle_801821C8"),
    0x801824E0: table.sym("face_particle_801824E0", table.GLOBL),
    0x80182630: table.sym("face_particle_80182630", table.GLOBL),
    0x8018273C: table.sym("face_particle_8018273C"),
    0x801828B8: table.sym("face_particle_801828B8"),
    0x80182B48: table.sym("face_particle_80182B48"),
    0x80182DC4: table.sym("face_particle_80182DC4"),
    0x801836B0: table.sym("face_particle_801836B0", table.GLOBL),
    0x80183708: table.sym("face_particle_80183708"), # unused
    0x801839B0: table.sym("face_particle_801839B0"), # unused
    0x801839C4: table.sym("face_particle_801839C4"), # unused
    0x801839D8: table.sym("face_particle_801839D8"), # unused
    0x801839F4: table.sym("face_particle_801839F4"), # unused
    0x80183A10: table.sym("face_particle_80183A10"),

    # src/face/dynlist.S
    0x80183A50: table.sym("face_dynlist_80183A50", table.GLOBL),
    0x80183A80: table.sym("face_dynlist_80183A80", table.GLOBL),
    0x80183AB0: table.sym("face_dynlist_80183AB0", table.GLOBL),
    0x80183B20: table.sym("face_dynlist_80183B20", table.GLOBL),
    0x8018435C: table.sym("face_dynlist_8018435C", table.GLOBL),
    0x80184400: table.sym("face_dynlist_80184400"), # unused
    0x801844A8: table.sym("face_dynlist_801844A8"),
    0x801844DC: table.sym("face_dynlist_801844DC"),
    0x80184510: table.sym("face_dynlist_80184510"),
    0x80184630: table.sym("face_dynlist_80184630"), # unused
    0x8018468C: table.sym("face_dynlist_8018468C"),
    0x80184740: table.sym("face_dynlist_80184740"),
    0x801847AC: table.sym("face_dynlist_801847AC"),
    0x80184828: table.sym("face_dynlist_80184828"),
    0x801848A0: table.sym("face_dynlist_801848A0"),
    0x801848E8: table.sym("face_dynlist_801848E8"),
    0x80184B84: table.sym("face_dynlist_80184B84"),
    0x80184BF8: table.sym("face_dynlist_80184BF8", table.GLOBL),
    0x80184EFC: table.sym("face_dynlist_80184EFC"),
    0x80184FC4: table.sym("face_dynlist_80184FC4"),
    0x8018536C: table.sym("face_dynlist_8018536C"),
    0x80185410: table.sym("face_dynlist_80185410"),
    0x8018545C: table.sym("face_dynlist_8018545C"),
    0x80185A18: table.sym("face_dynlist_80185A18"),
    0x801861B0: table.sym("face_dynlist_801861B0"),
    0x80186350: table.sym("face_dynlist_80186350"),
    0x80186440: table.sym("face_dynlist_80186440"),
    0x801864DC: table.sym("face_dynlist_801864DC"),
    0x80186588: table.sym("face_dynlist_80186588"),
    0x8018666C: table.sym("face_dynlist_8018666C"),
    0x801866F8: table.sym("face_dynlist_801866F8"),
    0x80186784: table.sym("face_dynlist_80186784"),
    0x801868A4: table.sym("face_dynlist_801868A4", table.GLOBL),
    0x80186A60: table.sym("face_dynlist_80186A60"),
    0x80186BFC: table.sym("face_dynlist_80186BFC", table.GLOBL),
    0x80186C84: table.sym("face_dynlist_80186C84", table.GLOBL),
    0x80186CAC: table.sym("face_dynlist_80186CAC", table.GLOBL),
    0x80186CDC: table.sym("face_dynlist_80186CDC", table.GLOBL),
    0x80186DE0: table.sym("face_dynlist_80186DE0"),
    0x80186E5C: table.sym("face_dynlist_80186E5C", table.GLOBL),
    0x80186E74: table.sym("face_dynlist_80186E74", table.GLOBL),
    0x8018710C: table.sym("face_dynlist_8018710C"), # unused
    0x80187244: table.sym("face_dynlist_80187244"), # unused
    0x8018739C: table.sym("face_dynlist_8018739C"), # unused
    0x80187480: table.sym("face_dynlist_80187480", table.GLOBL),
    0x80187608: table.sym("face_dynlist_80187608", table.GLOBL),
    0x80187794: table.sym("face_dynlist_80187794", table.GLOBL),
    0x80187AB0: table.sym("face_dynlist_80187AB0"), # unused
    0x80187C80: table.sym("face_dynlist_80187C80", table.GLOBL),
    0x80187E78: table.sym("face_dynlist_80187E78", table.GLOBL),
    0x80187F54: table.sym("face_dynlist_80187F54"), # unused
    0x80188030: table.sym("face_dynlist_80188030", table.GLOBL),
    0x801881B8: table.sym("face_dynlist_801881B8"),
    0x8018837C: table.sym("face_dynlist_8018837C"),
    0x801884D0: table.sym("face_dynlist_801884D0"), # unused
    0x80188624: table.sym("face_dynlist_80188624"), # unused
    0x80188738: table.sym("face_dynlist_80188738", table.GLOBL),
    0x801889A8: table.sym("face_dynlist_801889A8"),
    0x80188AB0: table.sym("face_dynlist_80188AB0"), # unused
    0x80188B7C: table.sym("face_dynlist_80188B7C", table.GLOBL),
    0x801891F4: table.sym("face_dynlist_801891F4"),
    0x80189240: table.sym("face_dynlist_80189240", table.GLOBL),
    0x8018945C: table.sym("face_dynlist_8018945C"),
    0x80189584: table.sym("face_dynlist_80189584"),
    0x80189660: table.sym("face_dynlist_80189660"),
    0x8018973C: table.sym("face_dynlist_8018973C", table.GLOBL),
    0x801898D8: table.sym("face_dynlist_801898D8", table.GLOBL),
    0x80189990: table.sym("face_dynlist_80189990"),
    0x80189CD8: table.sym("face_dynlist_80189CD8"),
    0x80189DA8: table.sym("face_dynlist_80189DA8", table.GLOBL),
    0x80189FB4: table.sym("face_dynlist_80189FB4"),
    0x8018A12C: table.sym("face_dynlist_8018A12C", table.GLOBL),
    0x8018A358: table.sym("face_dynlist_8018A358", table.GLOBL),
    0x8018A530: table.sym("face_dynlist_8018A530", table.GLOBL),
    0x8018A590: table.sym("face_dynlist_8018A590", table.GLOBL),
    0x8018A700: table.sym("face_dynlist_8018A700"),
    0x8018A828: table.sym("face_dynlist_8018A828", table.GLOBL),
    0x8018A9EC: table.sym("face_dynlist_8018A9EC"),
    0x8018AA9C: table.sym("face_dynlist_8018AA9C"),
    0x8018AB78: table.sym("face_dynlist_8018AB78"),
    0x8018AC24: table.sym("face_dynlist_8018AC24"),
    0x8018AD00: table.sym("face_dynlist_8018AD00", table.GLOBL),
    0x8018AE30: table.sym("face_dynlist_8018AE30"),
    0x8018AEDC: table.sym("face_dynlist_8018AEDC", table.GLOBL),
    0x8018AFB0: table.sym("face_dynlist_8018AFB0", table.GLOBL),
    0x8018B0FC: table.sym("face_dynlist_8018B0FC"), # unused
    0x8018B210: table.sym("face_dynlist_8018B210"), # unused
    0x8018B2E8: table.sym("face_dynlist_8018B2E8", table.GLOBL),
    0x8018B3A4: table.sym("face_dynlist_8018B3A4", table.GLOBL),
    0x8018B4D4: table.sym("face_dynlist_8018B4D4", table.GLOBL),
    0x8018B5E8: table.sym("face_dynlist_8018B5E8", table.GLOBL),
    0x8018B6BC: table.sym("face_dynlist_8018B6BC", table.GLOBL),
    0x8018B758: table.sym("face_dynlist_8018B758"),

    # src/face/gadget.S
    0x8018B830: table.sym("face_gadget_8018B830", table.GLOBL),
    0x8018B8E8: table.sym("face_gadget_8018B8E8"), # unused
    0x8018B97C: table.sym("face_gadget_8018B97C"),
    0x8018B9D8: table.sym("face_gadget_8018B9D8"),
    0x8018BA40: table.sym("face_gadget_8018BA40"), # unused
    0x8018BB00: table.sym("face_gadget_8018BB00", table.GLOBL),
    0x8018BBC0: table.sym("face_gadget_8018BBC0", table.GLOBL),
    0x8018BC9C: table.sym("face_gadget_8018BC9C"),
    0x8018BD54: table.sym("face_gadget_8018BD54"),
    0x8018BDF8: table.sym("face_gadget_8018BDF8"),
    0x8018BE40: table.sym("face_gadget_8018BE40"), # unused
    0x8018C0F4: table.sym("face_gadget_8018C0F4", table.GLOBL),
    0x8018C2B0: table.sym("face_gadget_8018C2B0", table.GLOBL),

    # src/face/stdio.S
    0x8018C2F0: table.sym("face_stdio_8018C2F0"),
    0x8018C3A4: table.sym("face_stdio_8018C3A4"),
    0x8018C44C: table.sym("face_stdio_8018C44C", table.GLOBL),
    0x8018C550: table.sym("face_stdio_8018C550"), # unused
    0x8018C598: table.sym("face_stdio_8018C598", table.GLOBL),
    0x8018C704: table.sym("face_stdio_8018C704", table.GLOBL),
    0x8018C790: table.sym("face_stdio_8018C790", table.GLOBL),
    0x8018C7B4: table.sym("face_stdio_8018C7B4", table.GLOBL),
    0x8018C86C: table.sym("face_stdio_8018C86C", table.GLOBL),
    0x8018C920: table.sym("face_stdio_8018C920", table.GLOBL),
    0x8018C938: table.sym("face_stdio_8018C938", table.GLOBL),
    0x8018C954: table.sym("face_stdio_8018C954", table.GLOBL),
    0x8018CA88: table.sym("face_stdio_8018CA88"),
    0x8018CB34: table.sym("face_stdio_8018CB34"),
    0x8018CBF4: table.sym("face_stdio_8018CBF4"),
    0x8018CC54: table.sym("face_stdio_8018CC54", table.GLOBL),
    0x8018CCC0: table.sym("face_stdio_8018CCC0"),
    0x8018CD9C: table.sym("face_stdio_8018CD9C"), # unused
    0x8018CE0C: table.sym("face_stdio_8018CE0C"), # unused
    0x8018CEA0: table.sym("face_stdio_8018CEA0", table.GLOBL),
    0x8018CF70: table.sym("face_stdio_8018CF70", table.GLOBL),
    0x8018D02C: table.sym("face_stdio_8018D02C", table.GLOBL),
    0x8018D088: table.sym("face_stdio_8018D088", table.GLOBL),
    0x8018D160: table.sym("face_stdio_8018D160", table.GLOBL),
    0x8018D1A8: table.sym("face_stdio_8018D1A8"), # unused
    0x8018D1F8: table.sym("face_stdio_8018D1F8", table.GLOBL),
    0x8018D228: table.sym("face_stdio_8018D228"),
    0x8018D298: table.sym("face_stdio_8018D298", table.GLOBL),
    0x8018D560: table.sym("face_stdio_8018D560", table.GLOBL),
    0x8018D5F0: table.sym("face_stdio_8018D5F0", table.GLOBL),
    0x8018D6A0: table.sym("face_stdio_8018D6A0", table.GLOBL),
    0x8018D7E8: table.sym("face_stdio_8018D7E8", table.GLOBL),
    0x8018D948: table.sym("face_stdio_8018D948", table.GLOBL),
    0x8018D988: table.sym("face_stdio_8018D988"),
    0x8018D9E8: table.sym("face_stdio_8018D9E8"),
    0x8018DAE4: table.sym("face_stdio_8018DAE4"),
    0x8018DB38: table.sym("face_stdio_8018DB38", table.GLOBL),
    0x8018DDD8: table.sym("face_stdio_8018DDD8", table.GLOBL),
    0x8018DE1C: table.sym("face_stdio_8018DE1C"), # unused
    0x8018DE9C: table.sym("face_stdio_8018DE9C", table.GLOBL),
    0x8018DF18: table.sym("face_stdio_8018DF18", table.GLOBL),
    0x8018DF6C: table.sym("face_stdio_8018DF6C", table.GLOBL),
    0x8018DFF0: table.sym("face_stdio_8018DFF0", table.GLOBL),
    0x8018E098: table.sym("face_stdio_8018E098", table.GLOBL),
    0x8018E128: table.sym("face_stdio_8018E128", table.GLOBL),
    0x8018E14C: table.sym("face_stdio_8018E14C"),
    0x8018E16C: table.sym("face_stdio_8018E16C", table.GLOBL),
    0x8018E37C: table.sym("face_stdio_8018E37C", table.GLOBL),
    0x8018E4A8: table.sym("face_stdio_8018E4A8", table.GLOBL),
    0x8018E4C4: table.sym("face_stdio_8018E4C4", table.GLOBL),
    0x8018E4E0: table.sym("face_stdio_8018E4E0"),
    0x8018E518: table.sym("face_stdio_8018E518", table.GLOBL),

    # src/face/joint.S
    0x8018E660: table.sym("face_joint_8018E660"),
    0x8018ED28: table.sym("face_joint_8018ED28", table.GLOBL),
    0x8018EF9C: table.sym("face_joint_8018EF9C"), # unused
    0x8018F0B8: table.sym("face_joint_8018F0B8"),
    0x8018F188: table.sym("face_joint_8018F188", table.GLOBL),
    0x8018F388: table.sym("face_joint_8018F388", table.GLOBL),
    0x8018F468: table.sym("face_joint_8018F468", table.GLOBL),
    0x8018F60C: table.sym("face_joint_8018F60C"),
    0x8018F660: table.sym("face_joint_8018F660"),
    0x8018F9DC: table.sym("face_joint_8018F9DC"),
    0x8018FBA8: table.sym("face_joint_8018FBA8", table.GLOBL),
    0x8018FC08: table.sym("face_joint_8018FC08", table.GLOBL),
    0x8018FC98: table.sym("face_joint_8018FC98", table.GLOBL),
    0x8018FDE4: table.sym("face_joint_8018FDE4", table.GLOBL),
    0x8018FEDC: table.sym("face_joint_8018FEDC", table.GLOBL),
    0x80190054: table.sym("face_joint_80190054"), # unused
    0x80190068: table.sym("face_joint_80190068"), # unused
    0x801900C8: table.sym("face_joint_801900C8"), # unused
    0x80190128: table.sym("face_joint_80190128"),
    0x801902A8: table.sym("face_joint_801902A8"),
    0x80190528: table.sym("face_joint_80190528"),
    0x801906B4: table.sym("face_joint_801906B4"),
    0x80190AF4: table.sym("face_joint_80190AF4"),
    0x80190B60: table.sym("face_joint_80190B60"), # unused
    0x80190C94: table.sym("face_joint_80190C94"),
    0x80190FA8: table.sym("face_joint_80190FA8"), # unused
    0x8019107C: table.sym("face_joint_8019107C"),
    0x801912E8: table.sym("face_joint_801912E8", table.GLOBL),
    0x80191360: table.sym("face_joint_80191360", table.GLOBL),
    0x80191500: table.sym("face_joint_80191500", table.GLOBL),
    0x80191530: table.sym("face_joint_80191530", table.GLOBL),
    0x80191638: table.sym("face_joint_80191638", table.GLOBL),
    0x8019164C: table.sym("face_joint_8019164C"), # unused
    0x80191744: table.sym("face_joint_80191744", table.GLOBL),
    0x80191964: table.sym("face_joint_80191964", table.GLOBL),
    0x80191A34: table.sym("face_joint_80191A34"), # unused
    0x80191B5C: table.sym("face_joint_80191B5C"), # unused
    0x80191D38: table.sym("face_joint_80191D38"),
    0x80191EA0: table.sym("face_joint_80191EA0"),
    0x80191F94: table.sym("face_joint_80191F94"),
    0x80191FC8: table.sym("face_joint_80191FC8", table.GLOBL),
    0x80192028: table.sym("face_joint_80192028", table.GLOBL),

    # src/face/net.S
    0x80192050: table.sym("face_net_80192050"),
    0x80192204: table.sym("face_net_80192204", table.GLOBL),
    0x801923D4: table.sym("face_net_801923D4"),
    0x8019243C: table.sym("face_net_8019243C"),
    0x801924F4: table.sym("face_net_801924F4", table.GLOBL),
    0x80192668: table.sym("face_net_80192668"),
    0x801927E4: table.sym("face_net_801927E4"),
    0x80192C10: table.sym("face_net_80192C10"), # unused
    0x80192D9C: table.sym("face_net_80192D9C"),
    0x80192E0C: table.sym("face_net_80192E0C"),
    0x801930D8: table.sym("face_net_801930D8"),
    0x80193424: table.sym("face_net_80193424"),
    0x8019353C: table.sym("face_net_8019353C", table.GLOBL),
    0x80193610: table.sym("face_net_80193610"),
    0x801936DC: table.sym("face_net_801936DC"),
    0x80193804: table.sym("face_net_80193804", table.GLOBL),
    0x8019387C: table.sym("face_net_8019387C"),
    0x80193988: table.sym("face_net_80193988", table.GLOBL),
    0x801939FC: table.sym("face_net_801939FC"), # unused
    0x80193C50: table.sym("face_net_80193C50", table.GLOBL),

    # src/face/math.S
    0x80193C70: table.sym("face_math_80193C70"),
    0x80193CA8: table.sym("face_math_80193CA8", table.GLOBL),
    0x8019429C: table.sym("face_math_8019429C", table.GLOBL),
    0x80194360: table.sym("face_math_80194360", table.GLOBL),
    0x80194424: table.sym("face_math_80194424", table.GLOBL),
    0x80194498: table.sym("face_math_80194498", table.GLOBL),
    0x80194868: table.sym("face_math_80194868", table.GLOBL),
    0x801948B0: table.sym("face_math_801948B0", table.GLOBL),
    0x801949C0: table.sym("face_math_801949C0", table.GLOBL),
    0x80194ACC: table.sym("face_math_80194ACC"), # unused
    0x80194B94: table.sym("face_math_80194B94", table.GLOBL),
    0x80194CD8: table.sym("face_math_80194CD8", table.GLOBL),
    0x80194D34: table.sym("face_math_80194D34", table.GLOBL),
    0x80194E54: table.sym("face_math_80194E54", table.GLOBL),
    0x80194EF8: table.sym("face_math_80194EF8", table.GLOBL),
    0x80194F3C: table.sym("face_math_80194F3C"), # unused
    0x80194FBC: table.sym("face_math_80194FBC", table.GLOBL),
    0x801950D0: table.sym("face_math_801950D0"),
    0x801956B8: table.sym("face_math_801956B8"),
    0x80195984: table.sym("face_math_80195984"),
    0x80195A4C: table.sym("face_math_80195A4C"),
    0x80195A90: table.sym("face_math_80195A90"), # unused
    0x80195B20: table.sym("face_math_80195B20"), # unused
    0x80195C44: table.sym("face_math_80195C44"), # unused
    0x80195DB8: table.sym("face_math_80195DB8"),
    0x80195ED8: table.sym("face_math_80195ED8"), # unused
    0x80196114: table.sym("face_math_80196114"),
    0x80196334: table.sym("face_math_80196334", table.GLOBL),
    0x801963C0: table.sym("face_math_801963C0", table.GLOBL),
    0x801964A0: table.sym("face_math_801964A0", table.GLOBL),
    0x80196570: table.sym("face_math_80196570", table.GLOBL),
    0x80196680: table.sym("face_math_80196680", table.GLOBL),
    0x80196754: table.sym("face_math_80196754", table.GLOBL),
    0x801970CC: table.sym("face_math_801970CC", table.GLOBL),
    0x801970E8: table.sym("face_math_801970E8", table.GLOBL),
    0x80197104: table.sym("face_math_80197104", table.GLOBL),
    0x801971A8: table.sym("face_math_801971A8"), # unused
    0x80197230: table.sym("face_math_80197230"), # unused

    # src/face/shape.S
    0x801973C0: table.sym("face_shape_801973C0"),
    0x80197400: table.sym("face_shape_80197400", table.GLOBL),
    0x8019764C: table.sym("face_shape_8019764C", table.GLOBL),
    0x80197764: table.sym("face_shape_80197764", table.GLOBL),
    0x80197810: table.sym("face_shape_80197810"),
    0x8019787C: table.sym("face_shape_8019787C"), # unused
    0x80197904: table.sym("face_shape_80197904", table.GLOBL),
    0x8019797C: table.sym("face_shape_8019797C", table.GLOBL),
    0x80197B14: table.sym("face_shape_80197B14"),
    0x80197B44: table.sym("face_shape_80197B44"),
    0x80197B70: table.sym("face_shape_80197B70"),
    0x80197BD4: table.sym("face_shape_80197BD4"),
    0x80197C54: table.sym("face_shape_80197C54"),
    0x80197C8C: table.sym("face_shape_80197C8C"),
    0x80197CC4: table.sym("face_shape_80197CC4"),
    0x80197DB0: table.sym("face_shape_80197DB0"),
    0x80197E90: table.sym("face_shape_80197E90"),
    0x80198028: table.sym("face_shape_80198028"),
    0x801981A8: table.sym("face_shape_801981A8"), # unused
    0x801981BC: table.sym("face_shape_801981BC"),
    0x80198228: table.sym("face_shape_80198228"),
    0x80198294: table.sym("face_shape_80198294"), # unused
    0x801982C4: table.sym("face_shape_801982C4"), # unused
    0x80198330: table.sym("face_shape_80198330"),
    0x801983F8: table.sym("face_shape_801983F8"),
    0x8019848C: table.sym("face_shape_8019848C", table.GLOBL),
    0x80198514: table.sym("face_shape_80198514"), # unused
    0x80198584: table.sym("face_shape_80198584"),
    0x80198664: table.sym("face_shape_80198664"),
    0x80198728: table.sym("face_shape_80198728"), # unused
    0x80198844: table.sym("face_shape_80198844"),
    0x80198D40: table.sym("face_shape_80198D40"),
    0x801990D0: table.sym("face_shape_801990D0"),
    0x801991F4: table.sym("face_shape_801991F4"),
    0x80199330: table.sym("face_shape_80199330"),
    0x801997A0: table.sym("face_shape_801997A0"), # unused
    0x801998E8: table.sym("face_shape_801998E8"), # unused
    0x80199F84: table.sym("face_shape_80199F84"), # unused
    0x80199FC8: table.sym("face_shape_80199FC8"),
    0x8019A024: table.sym("face_shape_8019A024", table.GLOBL),
    0x8019A0E0: table.sym("face_shape_8019A0E0", table.GLOBL),
    0x8019A1A8: table.sym("face_shape_8019A1A8", table.GLOBL),
    0x8019A4B8: table.sym("face_shape_8019A4B8", table.GLOBL),
    0x8019ABF8: table.sym("face_shape_8019ABF8", table.GLOBL),
    0x8019ACD8: table.sym("face_shape_8019ACD8"), # unused
    0x8019AF04: table.sym("face_shape_8019AF04"), # unused
    0x8019B004: table.sym("face_shape_8019B004"), # unused

    # src/face/gfx.S
    0x8019B060: table.sym("face_gfx_8019B060", table.GLOBL),
    0x8019B080: table.sym("face_gfx_8019B080", table.GLOBL),
    0x8019B0B0: table.sym("face_gfx_8019B0B0", table.GLOBL),
    0x8019B0D0: table.sym("face_gfx_8019B0D0"),
    0x8019B158: table.sym("face_gfx_8019B158"),
    0x8019B1E4: table.sym("face_gfx_8019B1E4"),
    0x8019B278: table.sym("face_gfx_8019B278"),
    0x8019B304: table.sym("face_gfx_8019B304"),
    0x8019B390: table.sym("face_gfx_8019B390"),
    0x8019B41C: table.sym("face_gfx_8019B41C", table.GLOBL),
    0x8019B45C: table.sym("face_gfx_8019B45C", table.GLOBL),
    0x8019B49C: table.sym("face_gfx_8019B49C", table.GLOBL),
    0x8019B514: table.sym("face_gfx_8019B514"), # unused
    0x8019B53C: table.sym("face_gfx_8019B53C", table.GLOBL),
    0x8019BB0C: table.sym("face_gfx_8019BB0C", table.GLOBL),
    0x8019BB44: table.sym("face_gfx_8019BB44", table.GLOBL),
    0x8019BB90: table.sym("face_gfx_8019BB90", table.GLOBL),
    0x8019BC88: table.sym("face_gfx_8019BC88", table.GLOBL),
    0x8019BD58: table.sym("face_gfx_8019BD58", table.GLOBL),
    0x8019BD90: table.sym("face_gfx_8019BD90", table.GLOBL),
    0x8019BDC8: table.sym("face_gfx_8019BDC8"), # unused
    0x8019BE14: table.sym("face_gfx_8019BE14"), # unused
    0x8019BE4C: table.sym("face_gfx_8019BE4C", table.GLOBL),
    0x8019BF08: table.sym("face_gfx_8019BF08"),
    0x8019BF80: table.sym("face_gfx_8019BF80"), # unused
    0x8019BFB0: table.sym("face_gfx_8019BFB0"),
    0x8019C240: table.sym("face_gfx_8019C240"),
    0x8019C3B0: table.sym("face_gfx_8019C3B0"), # unused
    0x8019C3C8: table.sym("face_gfx_8019C3C8"), # unused
    0x8019C418: table.sym("face_gfx_8019C418", table.GLOBL),
    0x8019C450: table.sym("face_gfx_8019C450", table.GLOBL),
    0x8019C4EC: table.sym("face_gfx_8019C4EC", table.GLOBL),
    0x8019C588: table.sym("face_gfx_8019C588"), # unused
    0x8019C59C: table.sym("face_gfx_8019C59C"), # unused
    0x8019C5F0: table.sym("face_gfx_8019C5F0"),
    0x8019C684: table.sym("face_gfx_8019C684", table.GLOBL),
    0x8019C828: table.sym("face_gfx_8019C828"), # unused
    0x8019C840: table.sym("face_gfx_8019C840"), # unused
    0x8019C874: table.sym("face_gfx_8019C874", table.GLOBL),
    0x8019C930: table.sym("face_gfx_8019C930", table.GLOBL),
    0x8019C9C8: table.sym("face_gfx_8019C9C8", table.GLOBL),
    0x8019C9F8: table.sym("face_gfx_8019C9F8", table.GLOBL),
    0x8019CD88: table.sym("face_gfx_8019CD88"), # unused
    0x8019CE3C: table.sym("face_gfx_8019CE3C"),
    0x8019CF18: table.sym("face_gfx_8019CF18"),
    0x8019CF44: table.sym("face_gfx_8019CF44"),
    0x8019D01C: table.sym("face_gfx_8019D01C"),
    0x8019D110: table.sym("face_gfx_8019D110"),
    0x8019D168: table.sym("face_gfx_8019D168"),
    0x8019D3B8: table.sym("face_gfx_8019D3B8"), # unused
    0x8019D42C: table.sym("face_gfx_8019D42C"), # unused
    0x8019D4A0: table.sym("face_gfx_8019D4A0", table.GLOBL),
    0x8019D848: table.sym("face_gfx_8019D848", table.GLOBL),
    0x8019E438: table.sym("face_gfx_8019E438", table.GLOBL),
    0x8019E724: table.sym("face_gfx_8019E724"),
    0x8019E780: table.sym("face_gfx_8019E780"),
    0x8019E89C: table.sym("face_gfx_8019E89C"),
    0x8019E93C: table.sym("face_gfx_8019E93C"),
    0x8019E9B4: table.sym("face_gfx_8019E9B4", table.GLOBL),
    0x8019E9D4: table.sym("face_gfx_8019E9D4", table.GLOBL),
    0x8019E9F4: table.sym("face_gfx_8019E9F4", table.GLOBL),
    0x8019EB44: table.sym("face_gfx_8019EB44"),
    0x8019EBAC: table.sym("face_gfx_8019EBAC", table.GLOBL),
    0x8019ED0C: table.sym("face_gfx_8019ED0C"), # unused
    0x8019ED48: table.sym("face_gfx_8019ED48"),
    0x8019EDC8: table.sym("face_gfx_8019EDC8"), # unused
    0x8019EE34: table.sym("face_gfx_8019EE34"),
    0x8019EFAC: table.sym("face_gfx_8019EFAC"),
    0x8019F054: table.sym("face_gfx_8019F054", table.GLOBL),
    0x8019F100: table.sym("face_gfx_8019F100"), # unused
    0x8019F16C: table.sym("face_gfx_8019F16C", table.GLOBL),
    0x8019F1D8: table.sym("face_gfx_8019F1D8", table.GLOBL),
    0x8019F224: table.sym("face_gfx_8019F224", table.GLOBL),
    0x8019F2DC: table.sym("face_gfx_8019F2DC", table.GLOBL),
    0x8019F398: table.sym("face_gfx_8019F398", table.GLOBL),
    0x8019F404: table.sym("face_gfx_8019F404", table.GLOBL),
    0x8019F458: table.sym("face_gfx_8019F458", table.GLOBL),
    0x8019FB18: table.sym("face_gfx_8019FB18", table.GLOBL),
    0x8019FBA0: table.sym("face_gfx_8019FBA0", table.GLOBL),
    0x801A0030: table.sym("face_gfx_801A0030", table.GLOBL),
    0x801A0094: table.sym("face_gfx_801A0094", table.GLOBL),
    0x801A0178: table.sym("face_gfx_801A0178", table.GLOBL),
    0x801A01B0: table.sym("face_gfx_801A01B0", table.GLOBL),
    0x801A032C: table.sym("face_gfx_801A032C"),
    0x801A039C: table.sym("face_gfx_801A039C"),
    0x801A03F8: table.sym("face_gfx_801A03F8", table.GLOBL),
    0x801A0464: table.sym("face_gfx_801A0464", table.GLOBL),
    0x801A047C: table.sym("face_gfx_801A047C", table.GLOBL),
    0x801A0494: table.sym("face_gfx_801A0494", table.GLOBL),
    0x801A0588: table.sym("face_gfx_801A0588", table.GLOBL),
    0x801A05B8: table.sym("face_gfx_801A05B8", table.GLOBL),
    0x801A09AC: table.sym("face_gfx_801A09AC", table.GLOBL),
    0x801A1728: table.sym("face_gfx_801A1728", table.GLOBL),
    0x801A1804: table.sym("face_gfx_801A1804", table.GLOBL),
    0x801A18F0: table.sym("face_gfx_801A18F0", table.GLOBL),
    0x801A194C: table.sym("face_gfx_801A194C"),
    0x801A1B40: table.sym("face_gfx_801A1B40"),
    0x801A1C70: table.sym("face_gfx_801A1C70"), # unused
    0x801A1FB0: table.sym("face_gfx_801A1FB0"), # unused
    0x801A2450: table.sym("face_gfx_801A2450", table.GLOBL),
    0x801A24A0: table.sym("face_gfx_801A24A0"), # unused
    0x801A24B4: table.sym("face_gfx_801A24B4", table.GLOBL),
    0x801A24C8: table.sym("face_gfx_801A24C8"),
    0x801A2588: table.sym("face_gfx_801A2588", table.GLOBL),
    0x801A2984: table.sym("face_gfx_801A2984"),
    0x801A338C: table.sym("face_gfx_801A338C"), # unused
    0x801A3434: table.sym("face_gfx_801A3434"), # unused
    0x801A3464: table.sym("face_gfx_801A3464"),
    0x801A34B0: table.sym("face_gfx_801A34B0"),
    0x801A3538: table.sym("face_gfx_801A3538"), # unused
    0x801A35BC: table.sym("face_gfx_801A35BC"), # unused
    0x801A3620: table.sym("face_gfx_801A3620", table.GLOBL),
    0x801A36B4: table.sym("face_gfx_801A36B4", table.GLOBL),
    0x801A371C: table.sym("face_gfx_801A371C", table.GLOBL),
    0x801A3788: table.sym("face_gfx_801A3788", table.GLOBL),
    0x801A3C20: table.sym("face_gfx_801A3C20"), # unused
    0x801A3C30: table.sym("face_gfx_801A3C30", table.GLOBL),
    0x801A3DCC: table.sym("face_gfx_801A3DCC", table.GLOBL),
    0x801A3F9C: table.sym("face_gfx_801A3F9C", table.GLOBL),
    0x801A4468: table.sym("face_gfx_801A4468", table.GLOBL),
    0x801A451C: table.sym("face_gfx_801A451C", table.GLOBL),
    0x801A4530: table.sym("face_gfx_801A4530", table.GLOBL),
    0x801A4550: table.sym("face_gfx_801A4550", table.GLOBL),
    0x801A4564: table.sym("face_gfx_801A4564", table.GLOBL),
    0x801A4578: table.sym("face_gfx_801A4578", table.GLOBL),
    0x801A45E0: table.sym("face_gfx_801A45E0"),
    0x801A4724: table.sym("face_gfx_801A4724"), # unused
    0x801A48F8: table.sym("face_gfx_801A48F8"), # unused
    0x801A4924: table.sym("face_gfx_801A4924"), # unused
    0x801A4934: table.sym("face_gfx_801A4934"), # unused
    0x801A4948: table.sym("face_gfx_801A4948"),
    0x801A4988: table.sym("face_gfx_801A4988"),
    0x801A49F4: table.sym("face_gfx_801A49F4"),
    0x801A4A04: table.sym("face_gfx_801A4A04", table.GLOBL),
    0x801A4A18: table.sym("face_gfx_801A4A18", table.GLOBL),
    0x801A4A30: table.sym("face_gfx_801A4A30", table.GLOBL),
    0x801A4A48: table.sym("face_gfx_801A4A48"), # unused
    0x801A4A58: table.sym("face_gfx_801A4A58"),
    0x801A4C44: table.sym("face_gfx_801A4C44"), # unused
    0x801A4D4C: table.sym("face_gfx_801A4D4C"),
    0x801A5098: table.sym("face_gfx_801A5098"), # unused
    0x801A5250: table.sym("face_gfx_801A5250"),
    0x801A52A8: table.sym("face_gfx_801A52A8"),
    0x801A534C: table.sym("face_gfx_801A534C", table.GLOBL),
    0x801A5484: table.sym("face_gfx_801A5484"), # unused
    0x801A5538: table.sym("face_gfx_801A5538", table.GLOBL),
    0x801A5A50: table.sym("face_gfx_801A5A50"), # unused
    0x801A5AD8: table.sym("face_gfx_801A5AD8", table.GLOBL),
    0x801A5AEC: table.sym("face_gfx_801A5AEC", table.GLOBL),
    0x801A5B00: table.sym("face_gfx_801A5B00", table.GLOBL),
    0x801A5B14: table.sym("face_gfx_801A5B14", table.GLOBL),
    0x801A5B44: table.sym("face_gfx_801A5B44", table.GLOBL),
    0x801A5B8C: table.sym("face_gfx_801A5B8C", table.GLOBL),
    0x801A5BC0: table.sym("face_gfx_801A5BC0"), # unused
    0x801A5BD4: table.sym("face_gfx_801A5BD4"), # unused
    0x801A5BE8: table.sym("face_gfx_801A5BE8"), # unused
    0x801A5BF8: table.sym("face_gfx_801A5BF8"), # unused
    0x801A5C20: table.sym("face_gfx_801A5C20"), # unused
    0x801A5C98: table.sym("face_gfx_801A5C98", table.GLOBL),
    0x801A5D28: table.sym("face_gfx_801A5D28"),
    0x801A5D64: table.sym("face_gfx_801A5D64"),
    0x801A5DC0: table.sym("face_gfx_801A5DC0"), # unused
    0x801A5ED0: table.sym("face_gfx_801A5ED0"), # unused
    0x801A6138: table.sym("face_gfx_801A6138"), # unused
    0x801A6430: table.sym("face_gfx_801A6430"),
    0x801A676C: table.sym("face_gfx_801A676C"),
    0x801A6904: table.sym("face_gfx_801A6904"),
    0x801A6954: table.sym("face_gfx_801A6954"), # unused
    0x801A6F70: table.sym("face_gfx_801A6F70"), # unused
    0x801A6F84: table.sym("face_gfx_801A6F84"), # unused
    0x801A6F98: table.sym("face_gfx_801A6F98"),
    0x801A7074: table.sym("face_gfx_801A7074", table.GLOBL),
    0x801A72F8: table.sym("face_gfx_801A72F8"), # unused
    0x801A730C: table.sym("face_gfx_801A730C"), # unused
    0x801A7820: table.sym("face_gfx_801A7820"), # unused
}

sym_E0_d_menu = {
    # src/title.data.c
    0x801A7830: table.sym_var("str_stage", "char", "[64][16]"),
    0x801A7C30: table.sym_var("title_801A7C30", "aligned u16"),
    0x801A7C34: table.sym_var("title_801A7C34", "aligned s16"),
    0x801A7C38: table.sym_var("title_801A7C38", "aligned s16"),

    # src/title.data.c
    0x801A7C40: table.sym_var("title_801A7C40", "const char", "[]"),
    0x801A7C50: table.sym_var("title_801A7C50", "const char", "[]"),
    0x801A7C64: table.sym_var("title_801A7C64", "const char", "[]"),
    0x801A7C68: table.sym_var("title_801A7C68", "const char", "[]"),

    # src/title_bg.data.c
    0x801A7C70: table.sym_var("gfx_title_bg", "const Gfx *", "[]"),
    0x801A7C80: table.sym_var("title_bg_x", "f32", "[]"),
    0x801A7CB0: table.sym_var("title_bg_y", "f32", "[]"),
    0x801A7CE0: table.sym_var("texture_title_bg", "const u16 *", "[]"),
    0x801A7CE8: table.sym_var("title_bg_mario", "static s8", "[]"),
    0x801A7CF4: table.sym_var("title_bg_table", "s8 *", "[]"),
    0x801A7CF8: table.sym_var("title_bg_game_over", "s8", "[]"),
    0x801A7D04: table.sym_var("title_bg_flip", "s8", "[]"),

    # src/star_select.data.c
    0x801A81A0: table.sym_var("star_select_801A81A0", "aligned s8"),
    0x801A81A4: table.sym_var("star_select_801A81A4", "aligned s8"),
    0x801A81A8: table.sym_var("star_select_801A81A8", "s32"),
    0x801A81AC: table.sym_var("str_myscore", "u8", "[]"),
    0x801A81B4: table.sym_var("star_select_801A81B4", "aligned u16"),

    # src/star_select.data.c
    0x801A81C0: table.sym_var("star_select_801A81C0", "const double"),
    0x801A81C8: table.sym_var("star_select_801A81C8", "const double"),
    0x801A81D0: table.sym_var("star_select_801A81D0", "const double"),
    0x801A81D8: table.sym_var("star_select_801A81D8", "const float"),
    0x801A81DC: table.sym_var("star_select_801A81DC", "const float"),

    0x002739A0: table.sym("data_face_start"),
    0x002A6120: table.sym("data_face_end"),
    0x04000000: table.sym("data_face_04000000"),
    0x04000650: table.sym("data_face_04000650"),
    0x04004F90: table.sym("data_face_04004F90"),
}

sym_E0_main = {
    0x00108A10: table.sym("data_main_start"),
    0x00108A40: table.sym("szp_main_start"),
    0x00114750: table.sym("szp_main_end"),
    0x10000000: table.sym("s_main", table.GLOBL),

    0x02000000: table.sym_var("texture_print_0", "static const u16", "[]"),
    0x02000200: table.sym_var("texture_print_1", "static const u16", "[]"),
    0x02000400: table.sym_var("texture_print_2", "static const u16", "[]"),
    0x02000600: table.sym_var("texture_print_3", "static const u16", "[]"),
    0x02000800: table.sym_var("texture_print_4", "static const u16", "[]"),
    0x02000A00: table.sym_var("texture_print_5", "static const u16", "[]"),
    0x02000C00: table.sym_var("texture_print_6", "static const u16", "[]"),
    0x02000E00: table.sym_var("texture_print_7", "static const u16", "[]"),
    0x02001000: table.sym_var("texture_print_8", "static const u16", "[]"),
    0x02001200: table.sym_var("texture_print_9", "static const u16", "[]"),
    0x02001400: table.sym_var("texture_print_a", "static const u16", "[]"),
    0x02001600: table.sym_var("texture_print_b", "static const u16", "[]"),
    0x02001800: table.sym_var("texture_print_c", "static const u16", "[]"),
    0x02001A00: table.sym_var("texture_print_d", "static const u16", "[]"),
    0x02001C00: table.sym_var("texture_print_e", "static const u16", "[]"),
    0x02001E00: table.sym_var("texture_print_f", "static const u16", "[]"),
    0x02002000: table.sym_var("texture_print_g", "static const u16", "[]"),
    0x02002200: table.sym_var("texture_print_h", "static const u16", "[]"),
    0x02002400: table.sym_var("texture_print_i", "static const u16", "[]"),
    0x02002600: table.sym_var("texture_print_k", "static const u16", "[]"),
    0x02002800: table.sym_var("texture_print_l", "static const u16", "[]"),
    0x02002A00: table.sym_var("texture_print_m", "static const u16", "[]"),
    0x02002C00: table.sym_var("texture_print_n", "static const u16", "[]"),
    0x02002E00: table.sym_var("texture_print_o", "static const u16", "[]"),
    0x02003000: table.sym_var("texture_print_p", "static const u16", "[]"),
    0x02003200: table.sym_var("texture_print_r", "static const u16", "[]"),
    0x02003400: table.sym_var("texture_print_s", "static const u16", "[]"),
    0x02003600: table.sym_var("texture_print_t", "static const u16", "[]"),
    0x02003800: table.sym_var("texture_print_u", "static const u16", "[]"),
    0x02003A00: table.sym_var("texture_print_w", "static const u16", "[]"),
    0x02003C00: table.sym_var("texture_print_y", "static const u16", "[]"),
    0x02003E00: table.sym_var("texture_print_squote",   "static const u16", "[]"),
    0x02004000: table.sym_var("texture_print_dquote",   "static const u16", "[]"),
    0x02004200: table.sym_var("texture_print_multiply", "static const u16", "[]"),
    0x02004400: table.sym_var("texture_print_coin",     "static const u16", "[]"),
    0x02004600: table.sym_var("texture_print_mario",    "static const u16", "[]"),
    0x02004800: table.sym_var("texture_print_star",     "static const u16", "[]"),
    0x02004A00: table.sym_var("texture_credit_3", "static const u16", "[]"),
    0x02004A80: table.sym_var("texture_credit_4", "static const u16", "[]"),
    0x02004B00: table.sym_var("texture_credit_6", "static const u16", "[]"),
    0x02004B80: table.sym_var("texture_credit_a", "static const u16", "[]"),
    0x02004C00: table.sym_var("texture_credit_b", "static const u16", "[]"),
    0x02004C80: table.sym_var("texture_credit_c", "static const u16", "[]"),
    0x02004D00: table.sym_var("texture_credit_d", "static const u16", "[]"),
    0x02004D80: table.sym_var("texture_credit_e", "static const u16", "[]"),
    0x02004E00: table.sym_var("texture_credit_f", "static const u16", "[]"),
    0x02004E80: table.sym_var("texture_credit_g", "static const u16", "[]"),
    0x02004F00: table.sym_var("texture_credit_h", "static const u16", "[]"),
    0x02004F80: table.sym_var("texture_credit_i", "static const u16", "[]"),
    0x02005000: table.sym_var("texture_credit_j", "static const u16", "[]"),
    0x02005080: table.sym_var("texture_credit_k", "static const u16", "[]"),
    0x02005100: table.sym_var("texture_credit_l", "static const u16", "[]"),
    0x02005180: table.sym_var("texture_credit_m", "static const u16", "[]"),
    0x02005200: table.sym_var("texture_credit_n", "static const u16", "[]"),
    0x02005280: table.sym_var("texture_credit_o", "static const u16", "[]"),
    0x02005300: table.sym_var("texture_credit_p", "static const u16", "[]"),
    0x02005380: table.sym_var("texture_credit_q", "static const u16", "[]"),
    0x02005400: table.sym_var("texture_credit_r", "static const u16", "[]"),
    0x02005480: table.sym_var("texture_credit_s", "static const u16", "[]"),
    0x02005500: table.sym_var("texture_credit_t", "static const u16", "[]"),
    0x02005580: table.sym_var("texture_credit_u", "static const u16", "[]"),
    0x02005600: table.sym_var("texture_credit_v", "static const u16", "[]"),
    0x02005680: table.sym_var("texture_credit_w", "static const u16", "[]"),
    0x02005700: table.sym_var("texture_credit_x", "static const u16", "[]"),
    0x02005780: table.sym_var("texture_credit_y", "static const u16", "[]"),
    0x02005800: table.sym_var("texture_credit_z", "static const u16", "[]"),
    0x02005880: table.sym_var("texture_credit_period", "static const u16", "[]"),
    0x02005900: table.sym_var("texture_message_02005900", "static const u8", "[]"),
    0x02005940: table.sym_var("texture_message_02005940", "static const u8", "[]"),
    0x02005980: table.sym_var("texture_message_02005980", "static const u8", "[]"),
    0x020059C0: table.sym_var("texture_message_020059C0", "static const u8", "[]"),
    0x02005A00: table.sym_var("texture_message_02005A00", "static const u8", "[]"),
    0x02005A40: table.sym_var("texture_message_02005A40", "static const u8", "[]"),
    0x02005A80: table.sym_var("texture_message_02005A80", "static const u8", "[]"),
    0x02005AC0: table.sym_var("texture_message_02005AC0", "static const u8", "[]"),
    0x02005B00: table.sym_var("texture_message_02005B00", "static const u8", "[]"),
    0x02005B40: table.sym_var("texture_message_02005B40", "static const u8", "[]"),
    0x02005B80: table.sym_var("texture_message_02005B80", "static const u8", "[]"),
    0x02005BC0: table.sym_var("texture_message_02005BC0", "static const u8", "[]"),
    0x02005C00: table.sym_var("texture_message_02005C00", "static const u8", "[]"),
    0x02005C40: table.sym_var("texture_message_02005C40", "static const u8", "[]"),
    0x02005C80: table.sym_var("texture_message_02005C80", "static const u8", "[]"),
    0x02005CC0: table.sym_var("texture_message_02005CC0", "static const u8", "[]"),
    0x02005D00: table.sym_var("texture_message_02005D00", "static const u8", "[]"),
    0x02005D40: table.sym_var("texture_message_02005D40", "static const u8", "[]"),
    0x02005D80: table.sym_var("texture_message_02005D80", "static const u8", "[]"),
    0x02005DC0: table.sym_var("texture_message_02005DC0", "static const u8", "[]"),
    0x02005E00: table.sym_var("texture_message_02005E00", "static const u8", "[]"),
    0x02005E40: table.sym_var("texture_message_02005E40", "static const u8", "[]"),
    0x02005E80: table.sym_var("texture_message_02005E80", "static const u8", "[]"),
    0x02005EC0: table.sym_var("texture_message_02005EC0", "static const u8", "[]"),
    0x02005F00: table.sym_var("texture_message_02005F00", "static const u8", "[]"),
    0x02005F40: table.sym_var("texture_message_02005F40", "static const u8", "[]"),
    0x02005F80: table.sym_var("texture_message_02005F80", "static const u8", "[]"),
    0x02005FC0: table.sym_var("texture_message_02005FC0", "static const u8", "[]"),
    0x02006000: table.sym_var("texture_message_02006000", "static const u8", "[]"),
    0x02006040: table.sym_var("texture_message_02006040", "static const u8", "[]"),
    0x02006080: table.sym_var("texture_message_02006080", "static const u8", "[]"),
    0x020060C0: table.sym_var("texture_message_020060C0", "static const u8", "[]"),
    0x02006100: table.sym_var("texture_message_02006100", "static const u8", "[]"),
    0x02006140: table.sym_var("texture_message_02006140", "static const u8", "[]"),
    0x02006180: table.sym_var("texture_message_02006180", "static const u8", "[]"),
    0x020061C0: table.sym_var("texture_message_020061C0", "static const u8", "[]"),
    0x02006200: table.sym_var("texture_message_02006200", "static const u8", "[]"),
    0x02006240: table.sym_var("texture_message_02006240", "static const u8", "[]"),
    0x02006280: table.sym_var("texture_message_02006280", "static const u8", "[]"),
    0x020062C0: table.sym_var("texture_message_020062C0", "static const u8", "[]"),
    0x02006300: table.sym_var("texture_message_02006300", "static const u8", "[]"),
    0x02006340: table.sym_var("texture_message_02006340", "static const u8", "[]"),
    0x02006380: table.sym_var("texture_message_02006380", "static const u8", "[]"),
    0x020063C0: table.sym_var("texture_message_020063C0", "static const u8", "[]"),
    0x02006400: table.sym_var("texture_message_02006400", "static const u8", "[]"),
    0x02006440: table.sym_var("texture_message_02006440", "static const u8", "[]"),
    0x02006480: table.sym_var("texture_message_02006480", "static const u8", "[]"),
    0x020064C0: table.sym_var("texture_message_020064C0", "static const u8", "[]"),
    0x02006500: table.sym_var("texture_message_02006500", "static const u8", "[]"),
    0x02006540: table.sym_var("texture_message_02006540", "static const u8", "[]"),
    0x02006580: table.sym_var("texture_message_02006580", "static const u8", "[]"),
    0x020065C0: table.sym_var("texture_message_020065C0", "static const u8", "[]"),
    0x02006600: table.sym_var("texture_message_02006600", "static const u8", "[]"),
    0x02006640: table.sym_var("texture_message_02006640", "static const u8", "[]"),
    0x02006680: table.sym_var("texture_message_02006680", "static const u8", "[]"),
    0x020066C0: table.sym_var("texture_message_020066C0", "static const u8", "[]"),
    0x02006700: table.sym_var("texture_message_02006700", "static const u8", "[]"),
    0x02006740: table.sym_var("texture_message_02006740", "static const u8", "[]"),
    0x02006780: table.sym_var("texture_message_02006780", "static const u8", "[]"),
    0x020067C0: table.sym_var("texture_message_020067C0", "static const u8", "[]"),
    0x02006800: table.sym_var("texture_message_02006800", "static const u8", "[]"),
    0x02006840: table.sym_var("texture_message_02006840", "static const u8", "[]"),
    0x02006880: table.sym_var("texture_message_02006880", "static const u8", "[]"),
    0x020068C0: table.sym_var("texture_message_020068C0", "static const u8", "[]"),
    0x02006900: table.sym_var("texture_message_02006900", "static const u8", "[]"),
    0x02006940: table.sym_var("texture_message_02006940", "static const u8", "[]"),
    0x02006980: table.sym_var("texture_message_02006980", "static const u8", "[]"),
    0x020069C0: table.sym_var("texture_message_020069C0", "static const u8", "[]"),
    0x02006A00: table.sym_var("texture_message_02006A00", "static const u8", "[]"),
    0x02006A40: table.sym_var("texture_message_02006A40", "static const u8", "[]"),
    0x02006A80: table.sym_var("texture_message_02006A80", "static const u8", "[]"),
    0x02006AC0: table.sym_var("texture_message_02006AC0", "static const u8", "[]"),
    0x02006B00: table.sym_var("texture_message_02006B00", "static const u8", "[]"),
    0x02006B40: table.sym_var("texture_message_02006B40", "static const u8", "[]"),
    0x02006B80: table.sym_var("texture_message_02006B80", "static const u8", "[]"),
    0x02006BC0: table.sym_var("texture_message_02006BC0", "static const u8", "[]"),
    0x02006C00: table.sym_var("texture_message_02006C00", "static const u8", "[]"),
    0x02006C40: table.sym_var("texture_message_02006C40", "static const u8", "[]"),
    0x02006C80: table.sym_var("texture_message_02006C80", "static const u8", "[]"),
    0x02006CC0: table.sym_var("texture_message_02006CC0", "static const u8", "[]"),
    0x02006D00: table.sym_var("texture_message_02006D00", "static const u8", "[]"),
    0x02006D40: table.sym_var("texture_message_02006D40", "static const u8", "[]"),
    0x02006D80: table.sym_var("texture_message_02006D80", "static const u8", "[]"),
    0x02006DC0: table.sym_var("texture_message_02006DC0", "static const u8", "[]"),
    0x02006E00: table.sym_var("texture_message_02006E00", "static const u8", "[]"),
    0x02006E40: table.sym_var("texture_message_02006E40", "static const u8", "[]"),
    0x02006E80: table.sym_var("texture_message_02006E80", "static const u8", "[]"),
    0x02006EC0: table.sym_var("texture_message_02006EC0", "static const u8", "[]"),
    0x02006F00: table.sym_var("texture_message_02006F00", "static const u8", "[]"),
    0x02006F40: table.sym_var("texture_message_02006F40", "static const u8", "[]"),
    0x02006F80: table.sym_var("texture_message_02006F80", "static const u8", "[]"),
    0x02006FC0: table.sym_var("texture_message_02006FC0", "static const u8", "[]"),
    0x02007000: table.sym_var("texture_camera_camera",  "static const u16", "[]"),
    0x02007200: table.sym_var("texture_camera_lakitu",  "static const u16", "[]"),
    0x02007400: table.sym_var("texture_camera_cross",   "static const u16", "[]"),
    0x02007600: table.sym_var("texture_camera_up",      "static const u16", "[]"),
    0x02007680: table.sym_var("texture_camera_down",    "static const u16", "[]"),
    0x02007700: table.sym_var("texture_print",      "const u16 *const", "[]"),
    0x020077E8: table.sym_var("texture_message",    "const u8 *const", "[]"),
    0x02007BE8: table.sym_var("texture_credit",     "const u16 *const", "[]"),
    0x02007C7C: table.sym_var("texture_camera",     "const u16 *const", "[]"),
    0x02007D28: table.sym_var("msg_select", "const struct msg_t *const", "[]"),
    0x02010A68: table.sym_var("msg_table", "const struct msg_t *const", "[]"),
    0x02010F68: table.sym_var("str_course", "const u8 *const", "[]"),
    0x0201192C: table.sym_var("str_level", "const u8 *const", "[]"),
    0x02011AB8: table.sym_var("align_0", "unused static const u64"),
    0x02011AC0: table.sym_var("gfx_print_copy_start",   "const Gfx", "[]"),
    0x02011AF8: table.sym_var("gfx_print_copy_char",    "const Gfx", "[]"),
    0x02011B28: table.sym_var("gfx_print_copy_end",     "const Gfx", "[]"),
    0x02011B60: table.sym_var("gfx_print_1cyc_start",   "const Gfx", "[]"),
    0x02011B98: table.sym_var("gfx_print_1cyc_char",    "const Gfx", "[]"),
    0x02011BC8: table.sym_var("gfx_print_1cyc_end",     "const Gfx", "[]"),
    0x02011C08: table.sym_var("vtx_message_box",    "static const Vtx", "[]"),
    0x02011C48: table.sym_var("gfx_message_box",    "const Gfx", "[]"),
    0x02011C88: table.sym_var("vtx_message_char",   "static const Vtx", "[]"),
    0x02011CC8: table.sym_var("gfx_message_start",  "const Gfx", "[]"),
    0x02011D08: table.sym_var("gfx_message_char",   "const Gfx", "[]"),
    0x02011D50: table.sym_var("gfx_message_end",    "const Gfx", "[]"),
    0x02011D90: table.sym_var("vtx_message_cursor", "static const Vtx", "[]"),
    0x02011DC0: table.sym_var("gfx_message_cursor", "const Gfx", "[]"),
    0x02011E10: table.sym_var("vtx_digit",          "static const Vtx", "[]"),
    0x02011E50: table.sym_var("gfx_digit_start",    "static const Gfx", "[]"),
    0x02011E98: table.sym_var("gfx_digit_end",      "static const Gfx", "[]"),
    0x02011ED8: table.sym_var("gfx_digit_0", "const Gfx", "[]"),
    0x02011F08: table.sym_var("gfx_digit_1", "const Gfx", "[]"),
    0x02011F38: table.sym_var("gfx_digit_2", "const Gfx", "[]"),
    0x02011F68: table.sym_var("gfx_digit_3", "const Gfx", "[]"),
    0x02011F98: table.sym_var("gfx_digit_4", "const Gfx", "[]"),
    0x02011FC8: table.sym_var("gfx_digit_5", "const Gfx", "[]"),
    0x02011FF8: table.sym_var("gfx_digit_6", "const Gfx", "[]"),
    0x02012028: table.sym_var("gfx_digit_7", "const Gfx", "[]"),
    0x02012058: table.sym_var("gfx_digit_8", "const Gfx", "[]"),
    0x02012088: table.sym_var("gfx_digit_9", "const Gfx", "[]"),
    0x020120B8: table.sym_var("texture_shadow_circle", "static const u8", "[]"),
    0x020121B8: table.sym_var("texture_shadow_square", "static const u8", "[]"),
    0x020122B8: table.sym_var("texture_wipe_star", "static const u8", "[]"),
    0x02012AB8: table.sym_var("texture_wipe_circle", "static const u8", "[]"),
    0x020132B8: table.sym_var("texture_wipe_mario", "static const u8", "[]"),
    0x020142B8: table.sym_var("texture_wipe_bowser", "static const u8", "[]"),
    0x02014AB8: table.sym_var("texture_water_0", "static const u16", "[]"),
    0x020152B8: table.sym_var("texture_water_1", "static const u16", "[]"),
    0x02015AB8: table.sym_var("texture_water_2", "static const u16", "[]"),
    0x020162B8: table.sym_var("texture_mist", "static const u16", "[]"),
    0x02016AB8: table.sym_var("texture_lava", "static const u16", "[]"),
    0x020172B8: table.sym_var("light_unused", "unused static const Lights1"), # unused
    0x020172D0: table.sym_var("mtx_identity",   "static const Mtx"),
    0x02017310: table.sym_var("mtx_ortho",      "static const Mtx"),
    0x02017350: table.sym_var("gfx_quad0", "const Gfx", "[]"),
    0x02017368: table.sym_var("gfx_quad1", "const Gfx", "[]"), # unused
    0x02017380: table.sym_var("gfx_shadow_start",   "static const Gfx", "[]"),
    0x020173A8: table.sym_var("gfx_shadow_circle",  "const Gfx", "[]"),
    0x020173F0: table.sym_var("gfx_shadow_square",  "const Gfx", "[]"),
    0x02017438: table.sym_var("gfx_shadow_9",   "const Gfx", "[]"),
    0x02017480: table.sym_var("gfx_shadow_4",   "const Gfx", "[]"),
    0x02017498: table.sym_var("gfx_shadow_end", "const Gfx", "[]"),
    0x020174C0: table.sym_var("gfx_wipe_start", "const Gfx", "[]"),
    0x020174F8: table.sym_var("gfx_wipe_end",   "const Gfx", "[]"),
    0x02017520: table.sym_var("gfx_wipe_draw",  "const Gfx", "[]"),
    0x02017568: table.sym_var("gfx_background_start",   "const Gfx", "[]"),
    0x02017598: table.sym_var("gfx_background_tile",    "const Gfx", "[]"),
    0x020175C8: table.sym_var("gfx_background_end",     "const Gfx", "[]"),
    0x020175F0: table.sym_var("gfx_scroll_rgba", "const Gfx", "[]"),
    0x02017630: table.sym_var("gfx_scroll_ia", "const Gfx", "[]"),
    0x02017670: table.sym_var("gfx_scroll_end", "const Gfx", "[]"),
    0x02017698: table.sym_var("texture_minimap", "static const u8", "[]"),
    0x020176D8: table.sym_var("gfx_minimap_start",  "static const Gfx", "[]"), # unused
    0x02017710: table.sym_var("gfx_minimap_tile",   "static const Gfx", "[]"), # unused
    0x02017740: table.sym_var("gfx_minimap_arrow",  "static const Gfx", "[]"), # unused
    0x02017798: table.sym_var("gfx_minimap_end",    "static const Gfx", "[]"), # unused
    0x020177B8: table.sym_var("light_ripple", "static const Lights1"),
    0x020177D0: table.sym_var("gfx_ripple_s_start", "const Gfx", "[]"),
    0x02017808: table.sym_var("gfx_ripple_s_end",   "const Gfx", "[]"),
    0x02017828: table.sym_var("gfx_ripple_e_start", "const Gfx", "[]"),
    0x02017860: table.sym_var("gfx_ripple_e_end",   "const Gfx", "[]"),
    0x02017890: table.sym_var("gfx_ripple_draw",    "const Gfx", "[]"),
    0x020178C0: table.sym_var("ripple_0", "const s16", "[]"),
    0x020182A4: table.sym_var("ripple_1", "const s16", "[]"),
}

sym_E0_o_player = {
    0x00114750: table.sym("szp_object_player_start"),
    0x001279B0: table.sym("data_object_player_start"),

    # mario
    0x04000000: table.sym_var("light_mario_blue",   "static const Lights1"),
    0x04000018: table.sym_var("light_mario_red",    "static const Lights1"),
    0x04000030: table.sym_var("light_mario_white",  "static const Lights1"),
    0x04000048: table.sym_var("light_mario_shoe",   "static const Lights1"),
    0x04000060: table.sym_var("light_mario_skin",   "static const Lights1"),
    0x04000078: table.sym_var("light_mario_hair",   "static const Lights1"),
    0x04000090: table.sym_var("texture_mario_metal",        "static const u16", "[]"),
    0x04001090: table.sym_var("texture_mario_button",       "static const u16", "[]"),
    0x04001890: table.sym_var("texture_mario_logo",         "static const u16", "[]"),
    0x04002090: table.sym_var("texture_mario_sideburn",     "static const u16", "[]"),
    0x04002890: table.sym_var("texture_mario_moustache",    "static const u16", "[]"),
    0x04003090: table.sym_var("texture_mario_eye_open",     "static const u16", "[]"),
    0x04003890: table.sym_var("texture_mario_eye_half",     "static const u16", "[]"),
    0x04004090: table.sym_var("texture_mario_eye_closed",   "static const u16", "[]"),
    0x04005890: table.sym_var("texture_mario_eye_left",     "static const u16", "[]"),
    0x04006090: table.sym_var("texture_mario_eye_right",    "static const u16", "[]"),
    0x04006890: table.sym_var("texture_mario_eye_up",       "static const u16", "[]"),
    0x04007090: table.sym_var("texture_mario_eye_down",     "static const u16", "[]"),
    0x04007890: table.sym_var("texture_mario_eye_dead",     "static const u16", "[]"),
    0x04008090: table.sym_var("texture_mario_wing_l",       "static const u16", "[]"),
    0x04009090: table.sym_var("texture_mario_wing_r",       "static const u16", "[]"),
    0x0400A090: table.sym_var("texture_mario_metal_wing_l", "static const u16", "[]"),
    0x0400B090: table.sym_var("texture_mario_metal_wing_r", "static const u16", "[]"),
    0x0400CA00: table.sym_var("gfx_mario_h_waist",      "static const Gfx", "[]"),
    0x0400CC98: table.sym_var("gfx_mario_h_waist_s",    "const Gfx", "[]"),
    0x0400CCC8: table.sym_var("gfx_mario_h_waist_e",    "const Gfx", "[]"),
    0x0400D090: table.sym_var("gfx_mario_h_uarmL",      "const Gfx", "[]"),
    0x0400D1D8: table.sym_var("gfx_mario_h_uarmL_s",    "const Gfx", "[]"),
    0x0400D2F8: table.sym_var("gfx_mario_h_larmL",      "const Gfx", "[]"),
    0x0400D758: table.sym_var("gfx_mario_h_fistL",      "const Gfx", "[]"),
    0x0400D8F0: table.sym_var("gfx_mario_h_fistL_s",    "const Gfx", "[]"),
    0x0400DCA0: table.sym_var("gfx_mario_h_uarmR",      "const Gfx", "[]"),
    0x0400DDE8: table.sym_var("gfx_mario_h_uarmR_s",    "const Gfx", "[]"),
    0x0400DF08: table.sym_var("gfx_mario_h_larmR",      "const Gfx", "[]"),
    0x0400E2C8: table.sym_var("gfx_mario_h_fistR",      "static const Gfx", "[]"),
    0x0400E458: table.sym_var("gfx_mario_h_fistR_s",    "const Gfx", "[]"),
    0x0400E478: table.sym_var("gfx_mario_h_fistR_e",    "const Gfx", "[]"),
    0x0400E6A8: table.sym_var("gfx_mario_h_thighL",     "static const Gfx", "[]"),
    0x0400E7B0: table.sym_var("gfx_mario_h_thighL_s",   "const Gfx", "[]"),
    0x0400E7E0: table.sym_var("gfx_mario_h_thighL_e",   "const Gfx", "[]"),
    0x0400E918: table.sym_var("gfx_mario_h_shinL",      "const Gfx", "[]"),
    0x0400EBB8: table.sym_var("gfx_mario_h_shoeL",      "const Gfx", "[]"),
    0x0400ECA0: table.sym_var("gfx_mario_h_shoeL_s",    "const Gfx", "[]"),
    0x0400EEB0: table.sym_var("gfx_mario_h_thighR",     "const Gfx", "[]"),
    0x0400EFB8: table.sym_var("gfx_mario_h_thighR_s",   "const Gfx", "[]"),
    0x0400F1D8: table.sym_var("gfx_mario_h_shinR",      "const Gfx", "[]"),
    0x0400F400: table.sym_var("gfx_mario_h_shoeR",      "static const Gfx", "[]"),
    0x0400F4E8: table.sym_var("gfx_mario_h_shoeR_s",    "const Gfx", "[]"),
    0x0400F528: table.sym_var("gfx_mario_h_shoeR_e",    "const Gfx", "[]"),
    0x0400FF28: table.sym_var("gfx_mario_h_torso0",     "static const Gfx", "[]"),
    0x0400FF88: table.sym_var("gfx_mario_h_torso1",     "static const Gfx", "[]"),
    0x04010260: table.sym_var("gfx_mario_h_torso2",     "static const Gfx", "[]"),
    0x04010348: table.sym_var("gfx_mario_h_torso12_s",  "static const Gfx", "[]"),
    0x04010370: table.sym_var("gfx_mario_h_torso_s",    "const Gfx", "[]"),
    0x040103F0: table.sym_var("gfx_mario_h_torso",      "const Gfx", "[]"),
    0x040112B0: table.sym_var("gfx_mario_h_cap0",       "static const Gfx", "[]"),
    0x040112E8: table.sym_var("gfx_mario_h_cap1",       "static const Gfx", "[]"),
    0x04011350: table.sym_var("gfx_mario_h_cap2",       "static const Gfx", "[]"),
    0x040113A0: table.sym_var("gfx_mario_h_cap3",       "static const Gfx", "[]"),
    0x04011438: table.sym_var("gfx_mario_h_cap4",       "static const Gfx", "[]"),
    0x040116F8: table.sym_var("gfx_mario_h_cap5",       "static const Gfx", "[]"),
    0x04011870: table.sym_var("gfx_mario_h_cap6",       "static const Gfx", "[]"),
    0x04011960: table.sym_var("gfx_mario_h_cap456_s",   "static const Gfx", "[]"),
    0x040119A0: table.sym_var("gfx_mario_h_cap_open",   "const Gfx", "[]"),
    0x04011A90: table.sym_var("gfx_mario_h_cap_half",   "const Gfx", "[]"),
    0x04011B80: table.sym_var("gfx_mario_h_cap_closed", "const Gfx", "[]"),
    0x04011C70: table.sym_var("gfx_mario_h_cap_left",   "const Gfx", "[]"),
    0x04011D60: table.sym_var("gfx_mario_h_cap_right",  "const Gfx", "[]"),
    0x04011E50: table.sym_var("gfx_mario_h_cap_up",     "const Gfx", "[]"),
    0x04011F40: table.sym_var("gfx_mario_h_cap_down",   "const Gfx", "[]"),
    0x04012030: table.sym_var("gfx_mario_h_cap_dead",   "const Gfx", "[]"),
    0x04012120: table.sym_var("gfx_mario_h_cap",        "const Gfx", "[]"),
    0x04012160: table.sym_var("light_mario_skin_old",   "static const Lights1"),
    0x04012178: table.sym_var("light_mario_hair_old",   "static const Lights1"),
    0x040132B0: table.sym_var("gfx_mario_h_hair0",      "static const Gfx", "[]"),
    0x04013318: table.sym_var("gfx_mario_h_hair1",      "static const Gfx", "[]"),
    0x040133A8: table.sym_var("gfx_mario_h_hair2",      "static const Gfx", "[]"),
    0x040133F8: table.sym_var("gfx_mario_h_hair3",      "static const Gfx", "[]"),
    0x040136D0: table.sym_var("gfx_mario_h_hair4",      "static const Gfx", "[]"),
    0x040139C0: table.sym_var("gfx_mario_h_hair34_s",   "static const Gfx", "[]"),
    0x040139E8: table.sym_var("gfx_mario_h_hair_open",      "const Gfx", "[]"),
    0x04013AB8: table.sym_var("gfx_mario_h_hair_half",      "const Gfx", "[]"),
    0x04013B88: table.sym_var("gfx_mario_h_hair_closed",    "const Gfx", "[]"),
    0x04013C58: table.sym_var("gfx_mario_h_hair_left",      "const Gfx", "[]"),
    0x04013D28: table.sym_var("gfx_mario_h_hair_right",     "const Gfx", "[]"),
    0x04013DF8: table.sym_var("gfx_mario_h_hair_up",        "const Gfx", "[]"),
    0x04013EC8: table.sym_var("gfx_mario_h_hair_down",      "const Gfx", "[]"),
    0x04013F98: table.sym_var("gfx_mario_h_hair_dead",      "const Gfx", "[]"),
    0x04014068: table.sym_var("gfx_mario_h_hair",           "const Gfx", "[]"),
    0x040144D8: table.sym_var("gfx_mario_m_waist",      "static const Gfx", "[]"),
    0x04014638: table.sym_var("gfx_mario_m_waist_s",    "const Gfx", "[]"),
    0x04014668: table.sym_var("gfx_mario_m_waist_e",    "const Gfx", "[]"),
    0x040147D0: table.sym_var("gfx_mario_m_uarmL",      "const Gfx", "[]"),
    0x04014840: table.sym_var("gfx_mario_m_uarmL_s",    "const Gfx", "[]"),
    0x04014950: table.sym_var("gfx_mario_m_larmL",      "const Gfx", "[]"),
    0x04014C90: table.sym_var("gfx_mario_m_fistL",      "const Gfx", "[]"),
    0x04014DC0: table.sym_var("gfx_mario_m_fistL_s",    "const Gfx", "[]"),
    0x04014ED0: table.sym_var("gfx_mario_m_uarmR",      "const Gfx", "[]"),
    0x04014F40: table.sym_var("gfx_mario_m_uarmR_s",    "const Gfx", "[]"),
    0x04015050: table.sym_var("gfx_mario_m_larmR",      "const Gfx", "[]"),
    0x040153B0: table.sym_var("gfx_mario_m_fistR",      "const Gfx", "[]"),
    0x040154E0: table.sym_var("gfx_mario_m_fistR_s",    "const Gfx", "[]"),
    0x04015500: table.sym_var("gfx_mario_m_fistR_e",    "const Gfx", "[]"),
    0x04015620: table.sym_var("gfx_mario_m_thighL",     "static const Gfx", "[]"),
    0x040156B0: table.sym_var("gfx_mario_m_thighL_s",   "const Gfx", "[]"),
    0x040156E0: table.sym_var("gfx_mario_m_thighL_e",   "const Gfx", "[]"),
    0x04015848: table.sym_var("gfx_mario_m_shinL",      "const Gfx", "[]"),
    0x04015A98: table.sym_var("gfx_mario_m_shoeL",      "const Gfx", "[]"),
    0x04015B60: table.sym_var("gfx_mario_m_shoeL_s",    "const Gfx", "[]"),
    0x04015C70: table.sym_var("gfx_mario_m_thighR",     "const Gfx", "[]"),
    0x04015D00: table.sym_var("gfx_mario_m_thighR_s",   "const Gfx", "[]"),
    0x04015E10: table.sym_var("gfx_mario_m_shinR",      "const Gfx", "[]"),
    0x04016000: table.sym_var("gfx_mario_m_shoeR",      "static const Gfx", "[]"),
    0x040160C8: table.sym_var("gfx_mario_m_shoeR_s",    "const Gfx", "[]"),
    0x04016108: table.sym_var("gfx_mario_m_shoeR_e",    "const Gfx", "[]"),
    0x04016668: table.sym_var("gfx_mario_m_torso0",     "static const Gfx", "[]"),
    0x040166B8: table.sym_var("gfx_mario_m_torso1",     "static const Gfx", "[]"),
    0x04016800: table.sym_var("gfx_mario_m_torso2",     "static const Gfx", "[]"),
    0x040168A0: table.sym_var("gfx_mario_m_torso12_s",  "static const Gfx", "[]"),
    0x040168C8: table.sym_var("gfx_mario_m_torso_s",    "const Gfx", "[]"),
    0x04016948: table.sym_var("gfx_mario_m_torso_e",    "const Gfx", "[]"),
    0x04016A18: table.sym_var("gfx_mario_l_waist",      "static const Gfx", "[]"),
    0x04016AB8: table.sym_var("gfx_mario_l_waist_s",    "const Gfx", "[]"),
    0x04016AE8: table.sym_var("gfx_mario_l_waist_e",    "const Gfx", "[]"),
    0x04016C20: table.sym_var("gfx_mario_l_uarmL",      "const Gfx", "[]"),
    0x04016C70: table.sym_var("gfx_mario_l_uarmL_s",    "const Gfx", "[]"),
    0x04016D50: table.sym_var("gfx_mario_l_larmL",      "const Gfx", "[]"),
    0x04016E20: table.sym_var("gfx_mario_l_fistL",      "const Gfx", "[]"),
    0x04016E80: table.sym_var("gfx_mario_l_fistL_s",    "const Gfx", "[]"),
    0x04016F60: table.sym_var("gfx_mario_l_uarmR",      "const Gfx", "[]"),
    0x04016FB0: table.sym_var("gfx_mario_l_uarmR_s",    "const Gfx", "[]"),
    0x04017090: table.sym_var("gfx_mario_l_larmR",      "const Gfx", "[]"),
    0x04017160: table.sym_var("gfx_mario_l_fistR",      "static const Gfx", "[]"),
    0x040171C0: table.sym_var("gfx_mario_l_fistR_s",    "const Gfx", "[]"),
    0x040171E0: table.sym_var("gfx_mario_l_fistR_e",    "const Gfx", "[]"),
    0x040172F0: table.sym_var("gfx_mario_l_thighL",     "static const Gfx", "[]"),
    0x04017360: table.sym_var("gfx_mario_l_thighL_s",   "const Gfx", "[]"),
    0x04017390: table.sym_var("gfx_mario_l_thighL_e",   "const Gfx", "[]"),
    0x040174E8: table.sym_var("gfx_mario_l_shinL",      "const Gfx", "[]"),
    0x04017638: table.sym_var("gfx_mario_l_shoeL",      "const Gfx", "[]"),
    0x040176A8: table.sym_var("gfx_mario_l_shoeL_s",    "const Gfx", "[]"),
    0x040177A8: table.sym_var("gfx_mario_l_thighR",     "const Gfx", "[]"),
    0x04017818: table.sym_var("gfx_mario_l_thighR_s",   "const Gfx", "[]"),
    0x04017918: table.sym_var("gfx_mario_l_shinR",      "const Gfx", "[]"),
    0x04017A68: table.sym_var("gfx_mario_l_shoeR",      "static const Gfx", "[]"),
    0x04017AD8: table.sym_var("gfx_mario_l_shoeR_s",    "const Gfx", "[]"),
    0x04017B18: table.sym_var("gfx_mario_l_shoeR_e",    "const Gfx", "[]"),
    0x04017D68: table.sym_var("gfx_mario_l_torso0",     "static const Gfx", "[]"),
    0x04017D98: table.sym_var("gfx_mario_l_torso1",     "static const Gfx", "[]"),
    0x04017E20: table.sym_var("gfx_mario_l_torso2",     "static const Gfx", "[]"),
    0x04017E78: table.sym_var("gfx_mario_l_torso12_s",  "static const Gfx", "[]"),
    0x04017EA0: table.sym_var("gfx_mario_l_torso_s",    "const Gfx", "[]"),
    0x04017F20: table.sym_var("gfx_mario_l_torso_e",    "const Gfx", "[]"),
    0x04018270: table.sym_var("gfx_mario_l_cap0",       "static const Gfx", "[]"),
    0x04018298: table.sym_var("gfx_mario_l_cap1",       "static const Gfx", "[]"),
    0x040182C0: table.sym_var("gfx_mario_l_cap2",       "static const Gfx", "[]"),
    0x04018300: table.sym_var("gfx_mario_l_cap3",       "static const Gfx", "[]"),
    0x04018370: table.sym_var("gfx_mario_l_cap4",       "static const Gfx", "[]"),
    0x040183F0: table.sym_var("gfx_mario_l_cap5",       "static const Gfx", "[]"),
    0x04018420: table.sym_var("gfx_mario_l_cap345_s",   "static const Gfx", "[]"),
    0x04018460: table.sym_var("gfx_mario_l_cap_open",   "const Gfx", "[]"),
    0x04018530: table.sym_var("gfx_mario_l_cap_half",   "const Gfx", "[]"),
    0x04018600: table.sym_var("gfx_mario_l_cap_closed", "const Gfx", "[]"),
    0x040186D0: table.sym_var("gfx_mario_l_cap_left",   "const Gfx", "[]"),
    0x040187A0: table.sym_var("gfx_mario_l_cap_right",  "const Gfx", "[]"),
    0x04018870: table.sym_var("gfx_mario_l_cap_up",     "const Gfx", "[]"),
    0x04018940: table.sym_var("gfx_mario_l_cap_down",   "const Gfx", "[]"),
    0x04018A10: table.sym_var("gfx_mario_l_cap_dead",   "const Gfx", "[]"),
    0x04018AE0: table.sym_var("gfx_mario_l_cap",        "const Gfx", "[]"),
    0x04018DC8: table.sym_var("gfx_mario_l_hair0",      "static const Gfx", "[]"),
    0x04018DF0: table.sym_var("gfx_mario_l_hair1",      "static const Gfx", "[]"),
    0x04018E30: table.sym_var("gfx_mario_l_hair2",      "static const Gfx", "[]"),
    0x04018EA0: table.sym_var("gfx_mario_l_hair3",      "static const Gfx", "[]"),
    0x04018F68: table.sym_var("gfx_mario_l_hair23_s",   "static const Gfx", "[]"),
    0x04018F90: table.sym_var("gfx_mario_l_hair_open",      "const Gfx", "[]"),
    0x04019040: table.sym_var("gfx_mario_l_hair_half",      "const Gfx", "[]"),
    0x040190F0: table.sym_var("gfx_mario_l_hair_closed",    "const Gfx", "[]"),
    0x040191A0: table.sym_var("gfx_mario_l_hair_left",      "const Gfx", "[]"),
    0x04019250: table.sym_var("gfx_mario_l_hair_right",     "const Gfx", "[]"),
    0x04019300: table.sym_var("gfx_mario_l_hair_up",        "const Gfx", "[]"),
    0x040193B0: table.sym_var("gfx_mario_l_hair_down",      "const Gfx", "[]"),
    0x04019460: table.sym_var("gfx_mario_l_hair_dead",      "const Gfx", "[]"),
    0x04019510: table.sym_var("gfx_mario_l_hair",           "const Gfx", "[]"),
    0x04019A68: table.sym_var("gfx_mario_handL",        "const Gfx", "[]"),
    0x04019CA0: table.sym_var("gfx_mario_handL_s",      "const Gfx", "[]"),
    0x0401A1F0: table.sym_var("gfx_mario_handR",        "static const Gfx", "[]"),
    0x0401A428: table.sym_var("gfx_mario_handR_s",      "const Gfx", "[]"),
    0x0401A448: table.sym_var("gfx_mario_handR_e",      "const Gfx", "[]"),
    0x0401ABA8: table.sym_var("gfx_mario_capR0",        "static const Gfx", "[]"),
    0x0401ABD0: table.sym_var("gfx_mario_capR1",        "static const Gfx", "[]"),
    0x0401AD40: table.sym_var("gfx_mario_capR2",        "static const Gfx", "[]"),
    0x0401AED0: table.sym_var("gfx_mario_capR3",        "static const Gfx", "[]"),
    0x0401AF20: table.sym_var("gfx_mario_capR123_s",    "static const Gfx", "[]"),
    0x0401B080: table.sym_var("gfx_mario_wingsR_l",         "static const Gfx", "[]"),
    0x0401B0B0: table.sym_var("gfx_mario_wingsR_r",         "static const Gfx", "[]"),
    0x0401B0E0: table.sym_var("gfx_mario_wingsR_start",     "static const Gfx", "[]"),
    0x0401B138: table.sym_var("gfx_mario_wingsR_end",       "static const Gfx", "[]"),
    0x0401B158: table.sym_var("gfx_mario_capR_s",       "const Gfx", "[]"),
    0x0401B1D8: table.sym_var("gfx_mario_wingsR_s",     "const Gfx", "[]"),
    0x0401B230: table.sym_var("gfx_mario_capR_e",       "const Gfx", "[]"),
    0x0401B278: table.sym_var("gfx_mario_wingsR_e",     "const Gfx", "[]"),
    0x0401BC80: table.sym_var("gfx_mario_peaceR",       "const Gfx", "[]"),
    0x0401BF30: table.sym_var("gfx_mario_peaceR_s",     "const Gfx", "[]"),
    0x0401C330: table.sym_var("gfx_mario_cap0",         "static const Gfx", "[]"),
    0x0401C368: table.sym_var("gfx_mario_cap1",         "static const Gfx", "[]"),
    0x0401C4C8: table.sym_var("gfx_mario_cap2",         "static const Gfx", "[]"),
    0x0401C510: table.sym_var("gfx_mario_cap12_s",      "static const Gfx", "[]"),
    0x0401C678: table.sym_var("gfx_mario_wings_l",      "static const Gfx", "[]"),
    0x0401C6A8: table.sym_var("gfx_mario_wings_r",      "static const Gfx", "[]"),
    0x0401C6D8: table.sym_var("gfx_mario_wings_start",  "static const Gfx", "[]"),
    0x0401C730: table.sym_var("gfx_mario_wings_end",    "static const Gfx", "[]"),
    0x0401C758: table.sym_var("gfx_mario_cap_s",        "const Gfx", "[]"), # unused
    0x0401C7E8: table.sym_var("gfx_mario_wings_s",      "const Gfx", "[]"), # unused
    0x0401C890: table.sym_var("gfx_mario_cap_e",        "const Gfx", "[]"), # unused
    0x0401C8E8: table.sym_var("gfx_mario_wings_e",      "const Gfx", "[]"), # unused
    0x0401C9C0: table.sym_var("gfx_mario_wing_l",       "static const Gfx", "[]"),
    0x0401C9E0: table.sym_var("gfx_mario_wing_r",       "static const Gfx", "[]"),
    0x0401CA00: table.sym_var("gfx_mario_wing_so",      "const Gfx", "[]"),
    0x0401CAB8: table.sym_var("gfx_mario_wing_sx",      "const Gfx", "[]"),
    0x0401CB70: table.sym_var("gfx_mario_wing_eo",      "const Gfx", "[]"),
    0x0401CC28: table.sym_var("gfx_mario_wing_ex",      "const Gfx", "[]"),

    # bubble
    0x0401CD20: table.sym_var("vtx_bubble", "static const Vtx", "[]"),
    0x0401CD60: table.sym_var("texture_bubble_0", "static const u16", "[]"),
    0x0401D560: table.sym_var("texture_bubble_1", "static const u16", "[]"),
    0x0401DD60: table.sym_var("gfx_bubble_0", "const Gfx", "[]"),
    0x0401DDE0: table.sym_var("gfx_bubble_1", "const Gfx", "[]"),

    # dust
    0x0401DE60: table.sym_var("vtx_dust", "static const Vtx", "[]"),
    0x0401DEA0: table.sym_var("texture_dust_0", "static const u16", "[]"),
    0x0401E6A0: table.sym_var("texture_dust_1", "static const u16", "[]"),
    0x0401EEA0: table.sym_var("texture_dust_2", "static const u16", "[]"),
    0x0401F6A0: table.sym_var("texture_dust_3", "static const u16", "[]"),
    0x0401FEA0: table.sym_var("texture_dust_4", "static const u16", "[]"),
    0x040206A0: table.sym_var("texture_dust_5", "static const u16", "[]"),
    0x04020EA0: table.sym_var("texture_dust_6", "static const u16", "[]"),
    0x040216A0: table.sym_var("gfx_dust", "static const Gfx", "[]"),
    0x04021718: table.sym_var("gfx_dust_0", "const Gfx", "[]"),
    0x04021730: table.sym_var("gfx_dust_1", "const Gfx", "[]"),
    0x04021748: table.sym_var("gfx_dust_2", "const Gfx", "[]"),
    0x04021760: table.sym_var("gfx_dust_3", "const Gfx", "[]"),
    0x04021778: table.sym_var("gfx_dust_4", "const Gfx", "[]"),
    0x04021790: table.sym_var("gfx_dust_5", "const Gfx", "[]"),
    0x040217A8: table.sym_var("gfx_dust_6", "const Gfx", "[]"),

    # smoke
    0x040217C0: table.sym_var("vtx_smoke", "static const Vtx", "[]"),
    0x04021800: table.sym_var("texture_smoke", "static const u16", "[]"),
    0x04022000: table.sym_var("gfx_smoke_start", "static const Gfx", "[]"),
    0x04022028: table.sym_var("gfx_smoke_draw", "static const Gfx", "[]"),
    0x04022048: table.sym_var("gfx_smoke_end", "static const Gfx", "[]"),
    0x04022070: table.sym_var("gfx_smoke", "const Gfx", "[]"),

    # wave
    0x040220C8: table.sym_var("vtx_wave_white", "static const Vtx", "[]"),
    0x04022108: table.sym_var("vtx_wave_red", "static const Vtx", "[]"),
    0x04022148: table.sym_var("texture_wave_0", "static const u16", "[]"),
    0x04022948: table.sym_var("texture_wave_1", "static const u16", "[]"),
    0x04023148: table.sym_var("texture_wave_2", "static const u16", "[]"),
    0x04023948: table.sym_var("texture_wave_3", "static const u16", "[]"),
    0x04024148: table.sym_var("texture_wave_4", "static const u16", "[]"),
    0x04024948: table.sym_var("texture_wave_5", "static const u16", "[]"),
    0x04025148: table.sym_var("gfx_wave_start", "static const Gfx", "[]"),
    0x04025190: table.sym_var("gfx_wave_end", "static const Gfx", "[]"),
    0x040251C8: table.sym_var("gfx_wave_white", "static const Gfx", "[]"),
    0x040251E0: table.sym_var("gfx_wave_red", "static const Gfx", "[]"),
    0x040251F8: table.sym_var("gfx_wave_white_0", "const Gfx", "[]"),
    0x04025210: table.sym_var("gfx_wave_white_1", "const Gfx", "[]"),
    0x04025228: table.sym_var("gfx_wave_white_2", "const Gfx", "[]"),
    0x04025240: table.sym_var("gfx_wave_white_3", "const Gfx", "[]"),
    0x04025258: table.sym_var("gfx_wave_white_4", "const Gfx", "[]"),
    0x04025270: table.sym_var("gfx_wave_white_5", "const Gfx", "[]"),
    0x04025288: table.sym_var("gfx_wave_red_0", "const Gfx", "[]"),
    0x040252A0: table.sym_var("gfx_wave_red_1", "const Gfx", "[]"),
    0x040252B8: table.sym_var("gfx_wave_red_2", "const Gfx", "[]"),
    0x040252D0: table.sym_var("gfx_wave_red_3", "const Gfx", "[]"),
    0x040252E8: table.sym_var("gfx_wave_red_4", "const Gfx", "[]"),
    0x04025300: table.sym_var("gfx_wave_red_5", "const Gfx", "[]"),

    # ripple
    0x04025318: table.sym_var("vtx_ripple", "static const Vtx", "[]"),
    0x04025358: table.sym_var("texture_ripple_0", "static const u16", "[]"),
    0x04025B58: table.sym_var("texture_ripple_1", "static const u16", "[]"),
    0x04026358: table.sym_var("texture_ripple_2", "static const u16", "[]"),
    0x04026B58: table.sym_var("texture_ripple_3", "static const u16", "[]"),
    0x04027358: table.sym_var("gfx_ripple_start", "static const Gfx", "[]"),
    0x040273A0: table.sym_var("gfx_ripple_end", "static const Gfx", "[]"),
    0x040273D8: table.sym_var("gfx_ripple", "static const Gfx", "[]"),
    0x040273F0: table.sym_var("gfx_ripple_0", "const Gfx", "[]"),
    0x04027408: table.sym_var("gfx_ripple_1", "const Gfx", "[]"),
    0x04027420: table.sym_var("gfx_ripple_2", "const Gfx", "[]"),
    0x04027438: table.sym_var("gfx_ripple_3", "const Gfx", "[]"),

    # sparkle
    0x04027450: table.sym_var("vtx_sparkle", "static const Vtx", "[]"),
    0x04027490: table.sym_var("texture_sparkle_5", "static const u16", "[]"),
    0x04027C90: table.sym_var("texture_sparkle_4", "static const u16", "[]"),
    0x04028490: table.sym_var("texture_sparkle_3", "static const u16", "[]"),
    0x04028C90: table.sym_var("texture_sparkle_2", "static const u16", "[]"),
    0x04029490: table.sym_var("texture_sparkle_1", "static const u16", "[]"),
    0x04029C90: table.sym_var("texture_sparkle_0", "static const u16", "[]"),
    0x0402A490: table.sym_var("gfx_sparkle", "static const Gfx", "[]"),
    0x0402A4F8: table.sym_var("gfx_sparkle_5", "const Gfx", "[]"),
    0x0402A510: table.sym_var("gfx_sparkle_4", "const Gfx", "[]"),
    0x0402A528: table.sym_var("gfx_sparkle_3", "const Gfx", "[]"),
    0x0402A540: table.sym_var("gfx_sparkle_2", "const Gfx", "[]"),
    0x0402A558: table.sym_var("gfx_sparkle_1", "const Gfx", "[]"),
    0x0402A570: table.sym_var("gfx_sparkle_0", "const Gfx", "[]"),

    # splash
    0x0402A588: table.sym_var("vtx_splash", "static const Vtx", "[]"),
    0x0402A5C8: table.sym_var("texture_splash_0", "static const u16", "[]"),
    0x0402B5C8: table.sym_var("texture_splash_1", "static const u16", "[]"),
    0x0402C5C8: table.sym_var("texture_splash_2", "static const u16", "[]"),
    0x0402D5C8: table.sym_var("texture_splash_3", "static const u16", "[]"),
    0x0402E5C8: table.sym_var("texture_splash_4", "static const u16", "[]"),
    0x0402F5C8: table.sym_var("texture_splash_5", "static const u16", "[]"),
    0x040305C8: table.sym_var("texture_splash_6", "static const u16", "[]"),
    0x040315C8: table.sym_var("texture_splash_7", "static const u16", "[]"),
    0x040325C8: table.sym_var("gfx_splash", "static const Gfx", "[]"),
    0x04032640: table.sym_var("gfx_splash_0", "const Gfx", "[]"),
    0x04032658: table.sym_var("gfx_splash_1", "const Gfx", "[]"),
    0x04032670: table.sym_var("gfx_splash_2", "const Gfx", "[]"),
    0x04032688: table.sym_var("gfx_splash_3", "const Gfx", "[]"),
    0x040326A0: table.sym_var("gfx_splash_4", "const Gfx", "[]"),
    0x040326B8: table.sym_var("gfx_splash_5", "const Gfx", "[]"),
    0x040326D0: table.sym_var("gfx_splash_6", "const Gfx", "[]"),
    0x040326E8: table.sym_var("gfx_splash_7", "const Gfx", "[]"),

    # droplet
    0x04032700: table.sym_var("vtx_droplet_white", "static const Vtx", "[]"),
    0x04032740: table.sym_var("vtx_droplet_red", "static const Vtx", "[]"),
    0x04032780: table.sym_var("texture_droplet", "static const u16", "[]"),
    0x04032980: table.sym_var("gfx_droplet_start", "static const Gfx", "[]"),
    0x040329E0: table.sym_var("gfx_droplet_end", "static const Gfx", "[]"),
    0x04032A18: table.sym_var("gfx_droplet_white", "const Gfx", "[]"), # 164
    0x04032A30: table.sym_var("gfx_droplet_red", "const Gfx", "[]"), # unused

    # glow
    0x04032A48: table.sym_var("vtx_glow", "static const Vtx", "[]"),
    0x04032A88: table.sym_var("texture_glow_0", "static const u16", "[]"),
    0x04033288: table.sym_var("texture_glow_1", "static const u16", "[]"),
    0x04033A88: table.sym_var("texture_glow_2", "static const u16", "[]"),
    0x04034288: table.sym_var("texture_glow_3", "static const u16", "[]"),
    0x04034A88: table.sym_var("texture_glow_4", "static const u16", "[]"),
    0x04035288: table.sym_var("gfx_glow", "static const Gfx", "[]"),
    0x04035300: table.sym_var("gfx_glow_0", "const Gfx", "[]"),
    0x04035318: table.sym_var("gfx_glow_1", "const Gfx", "[]"),
    0x04035330: table.sym_var("gfx_glow_2", "const Gfx", "[]"),
    0x04035348: table.sym_var("gfx_glow_3", "const Gfx", "[]"),
    0x04035360: table.sym_var("gfx_glow_4", "const Gfx", "[]"),

    # bubble
    0x17000000: table.sym_var("g_bubble_0", "const uintptr_t", "[]", table.GLOBL), # 168
    0x1700001C: table.sym_var("g_bubble_1", "const uintptr_t", "[]", table.GLOBL), # 170

    # dust
    0x17000038: table.sym_var("g_dust", "const uintptr_t", "[]", table.GLOBL), # 150

    # smoke
    0x17000084: table.sym_var("g_smoke", "const uintptr_t", "[]", table.GLOBL), # 148, 156

    # wave
    0x1700009C: table.sym_var("g_wave_white", "const uintptr_t", "[]", table.GLOBL), # 165
    0x170000E0: table.sym_var("g_wave_red", "const uintptr_t", "[]"), # unused

    # ripple
    0x17000124: table.sym_var("g_ripple_stop", "const uintptr_t", "[]", table.GLOBL), # 166
    0x17000168: table.sym_var("g_ripple_move", "const uintptr_t", "[]", table.GLOBL), # 163

    # sparkle
    0x170001BC: table.sym_var("g_sparkle", "const uintptr_t", "[]", table.GLOBL), # 149

    # splash
    0x17000230: table.sym_var("g_splash", "const uintptr_t", "[]", table.GLOBL), # 167

    # glow
    0x17000284: table.sym_var("g_glow", "const uintptr_t", "[]", table.GLOBL), # 143

    # mario
    0x170002E0: table.sym_var("g_mario_hso_head",   "static const uintptr_t", "[]"),
    0x1700041C: table.sym_var("g_mario_hso_gloveL", "static const uintptr_t", "[]"),
    0x17000494: table.sym_var("g_mario_hso_gloveR", "static const uintptr_t", "[]"),
    0x1700053C: table.sym_var("g_mario_hso",        "static const uintptr_t", "[]"),
    0x170006F8: table.sym_var("g_mario_mso_gloveL", "static const uintptr_t", "[]"),
    0x17000770: table.sym_var("g_mario_mso_gloveR", "static const uintptr_t", "[]"),
    0x17000818: table.sym_var("g_mario_mso",        "static const uintptr_t", "[]"),
    0x170009D4: table.sym_var("g_mario_lso_head",   "static const uintptr_t", "[]"),
    0x17000B10: table.sym_var("g_mario_lso_gloveL", "static const uintptr_t", "[]"),
    0x17000B88: table.sym_var("g_mario_lso_gloveR", "static const uintptr_t", "[]"),
    0x17000C30: table.sym_var("g_mario_lso",        "static const uintptr_t", "[]"),
    0x17000DEC: table.sym_var("g_mario_hsx_head",   "static const uintptr_t", "[]"),
    0x17000F28: table.sym_var("g_mario_hsx_gloveL", "static const uintptr_t", "[]"),
    0x17000FA0: table.sym_var("g_mario_hsx_gloveR", "static const uintptr_t", "[]"),
    0x17001048: table.sym_var("g_mario_hsx",        "static const uintptr_t", "[]"),
    0x17001204: table.sym_var("g_mario_msx_gloveL", "static const uintptr_t", "[]"),
    0x1700127C: table.sym_var("g_mario_msx_gloveR", "static const uintptr_t", "[]"),
    0x17001324: table.sym_var("g_mario_msx",        "static const uintptr_t", "[]"),
    0x170014E0: table.sym_var("g_mario_lsx_head",   "static const uintptr_t", "[]"),
    0x1700161C: table.sym_var("g_mario_lsx_gloveL", "static const uintptr_t", "[]"),
    0x17001694: table.sym_var("g_mario_lsx_gloveR", "static const uintptr_t", "[]"),
    0x1700173C: table.sym_var("g_mario_lsx",        "static const uintptr_t", "[]"),
    0x170018F8: table.sym_var("g_mario_heo_head",   "static const uintptr_t", "[]"),
    0x170019A4: table.sym_var("g_mario_heo_gloveL", "static const uintptr_t", "[]"),
    0x17001A1C: table.sym_var("g_mario_heo_gloveR", "static const uintptr_t", "[]"),
    0x17001AC4: table.sym_var("g_mario_heo",        "static const uintptr_t", "[]"),
    0x17001C80: table.sym_var("g_mario_meo_gloveL", "static const uintptr_t", "[]"),
    0x17001CF8: table.sym_var("g_mario_meo_gloveR", "static const uintptr_t", "[]"),
    0x17001DA0: table.sym_var("g_mario_meo",        "static const uintptr_t", "[]"),
    0x17001F5C: table.sym_var("g_mario_leo_head",   "static const uintptr_t", "[]"),
    0x17002008: table.sym_var("g_mario_leo_gloveL", "static const uintptr_t", "[]"),
    0x17002080: table.sym_var("g_mario_leo_gloveR", "static const uintptr_t", "[]"),
    0x17002128: table.sym_var("g_mario_leo",        "static const uintptr_t", "[]"),
    0x170022E4: table.sym_var("g_mario_hex_head",   "static const uintptr_t", "[]"),
    0x17002390: table.sym_var("g_mario_hex_gloveL", "static const uintptr_t", "[]"),
    0x17002408: table.sym_var("g_mario_hex_gloveR", "static const uintptr_t", "[]"),
    0x170024B0: table.sym_var("g_mario_hex",        "static const uintptr_t", "[]"),
    0x1700266C: table.sym_var("g_mario_mex_gloveL", "static const uintptr_t", "[]"),
    0x170026E4: table.sym_var("g_mario_mex_gloveR", "static const uintptr_t", "[]"),
    0x1700278C: table.sym_var("g_mario_mex",        "static const uintptr_t", "[]"),
    0x17002958: table.sym_var("g_mario_lex_head",   "static const uintptr_t", "[]"),
    0x17002A04: table.sym_var("g_mario_lex_gloveL", "static const uintptr_t", "[]"),
    0x17002A7C: table.sym_var("g_mario_lex_gloveR", "static const uintptr_t", "[]"),
    0x17002B24: table.sym_var("g_mario_lex",        "static const uintptr_t", "[]"),
    0x17002CE0: table.sym_var("g_mario_h",          "static const uintptr_t", "[]"),
    0x17002D14: table.sym_var("g_mario_m",          "static const uintptr_t", "[]"),
    0x17002D48: table.sym_var("g_mario_l",          "static const uintptr_t", "[]"),
    0x17002D7C: table.sym_var("g_mario_lod",        "static const uintptr_t", "[]"),
    0x17002DD4: table.sym_var("g_mario", "const uintptr_t", "[]", table.GLOBL), # 1
}

sym_E0_o_a0 = {
    0x0012A7E0: table.sym("szp_object_a0_start"),
    0x00132850: table.sym("data_object_a0_start"),
    0x0C000000: table.sym_var("g_a0_85", "const uintptr_t", "[]", table.GLOBL),
    0x0C000018: table.sym_var("g_a0_86", "const uintptr_t", "[]", table.GLOBL),
    0x0C0001E4: table.sym_var("g_a0_87", "const uintptr_t", "[]", table.GLOBL),
    0x0C000248: table.sym_var("g_a0_88", "const uintptr_t", "[]", table.GLOBL),
    0x0C000264: table.sym_var("g_a0_84", "const uintptr_t", "[]", table.GLOBL),
    0x0C00028C: table.sym_var("g_a0_89", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_a1 = {
    0x00132C60: table.sym("szp_object_a1_start"),
    0x00134A70: table.sym("data_object_a1_start"),
    0x0C000000: table.sym_var("g_a1_86", "const uintptr_t", "[]", table.GLOBL),
    0x0C000120: table.sym_var("g_a1_87", "const uintptr_t", "[]", table.GLOBL),
    0x0C000240: table.sym_var("g_a1_84", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_a2 = {
    0x00134D20: table.sym("szp_object_a2_start"),
    0x0013B5D0: table.sym("data_object_a2_start"),
    0x0C000000: table.sym_var("g_a2_86", "const uintptr_t", "[]", table.GLOBL),
    0x0C000308: table.sym_var("g_a2_84", "const uintptr_t", "[]", table.GLOBL),
    0x0C000328: table.sym_var("g_a2_85", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_a3 = {
    0x0013B910: table.sym("szp_object_a3_start"),
    0x00145C10: table.sym("data_object_a3_start"),
    0x0C000000: table.sym_var("g_a3_88", "const uintptr_t", "[]", table.GLOBL),
    0x0C000068: table.sym_var("g_a3_86", "const uintptr_t", "[]", table.GLOBL),
    0x0C00010C: table.sym_var("g_a3_85", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_a4 = {
    0x00145E90: table.sym("szp_object_a4_start"),
    0x00151B70: table.sym("data_object_a4_start"),
    0x0C000000: table.sym_var("g_a4_87", "const uintptr_t", "[]", table.GLOBL),
    0x0C0002AC: table.sym_var("g_a4_0C0002AC", "static const uintptr_t", "[]"),
    0x0C0005E4: table.sym_var("g_a4_88", "const uintptr_t", "[]", table.GLOBL),
    0x0C0005A8: table.sym_var("g_a4_89", "const uintptr_t", "[]", table.GLOBL),
    0x0C000610: table.sym_var("g_a4_84", "const uintptr_t", "[]", table.GLOBL),
    0x0C000644: table.sym_var("g_a4_85", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_a5 = {
    0x001521D0: table.sym("szp_object_a5_start"),
    0x001602E0: table.sym("data_object_a5_start"),
    0x0C000000: table.sym_var("g_a5_85", "const uintptr_t", "[]", table.GLOBL),
    0x0C000110: table.sym_var("g_a5_86", "const uintptr_t", "[]", table.GLOBL),
    0x0C00036C: table.sym_var("g_a5_87", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_a6 = {
    0x00160670: table.sym("szp_object_a6_start"),
    0x001656E0: table.sym("data_object_a6_start"),
    0x0C000000: table.sym_var("g_a6_84", "const uintptr_t", "[]", table.GLOBL),
    0x0C000104: table.sym_var("g_a6_87", "const uintptr_t", "[]", table.GLOBL),
    0x0C00021C: table.sym_var("g_a6_85", "const uintptr_t", "[]", table.GLOBL),
    0x0C000348: table.sym_var("g_a6_86", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_a7 = {
    0x00165A50: table.sym("szp_object_a7_start"),
    0x00166BD0: table.sym("data_object_a7_start"),
    0x0C000000: table.sym_var("g_a7_0C000000", "const uintptr_t", "[]"), # unused
    0x0C000018: table.sym_var("g_a7_0C000018", "const uintptr_t", "[]"), # unused
    0x0C000030: table.sym_var("g_a7_0C000030", "const uintptr_t", "[]"), # unused
    0x0C000048: table.sym_var("g_a7_85", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_a8 = {
    0x00166C60: table.sym("szp_object_a8_start"),
    0x0016D5C0: table.sym("data_object_a8_start"),
    0x0C000000: table.sym_var("g_a8_88", "const uintptr_t", "[]", table.GLOBL),
    0x0C0000C0: table.sym_var("g_a8_89", "const uintptr_t", "[]", table.GLOBL),
    0x0C0000D8: table.sym_var("g_a8_86", "const uintptr_t", "[]", table.GLOBL),
    0x0C000188: table.sym_var("g_a8_85", "const uintptr_t", "[]", table.GLOBL),
    0x0C0001B4: table.sym_var("g_a8_87", "const uintptr_t", "[]", table.GLOBL),
    0x0C000224: table.sym_var("g_a8_84", "const uintptr_t", "[]", table.GLOBL),
    0x0C000274: table.sym_var("g_a8_90", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_a9 = {
    0x0016D870: table.sym("szp_object_a9_start"),
    0x00180540: table.sym("data_object_a9_start"),
    0x0C000000: table.sym_var("g_a9_84", "const uintptr_t", "[]", table.GLOBL),
    0x0C000098: table.sym_var("g_a9_0C000098", "static const uintptr_t", "[]"),
    0x0C000254: table.sym_var("g_a9_0C000254", "static const uintptr_t", "[]"),
    0x0C000410: table.sym_var("g_a9_222", "const uintptr_t", "[]", table.GLOBL),
    0x0C000468: table.sym_var("g_a9_85", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_a10 = {
    0x00180BB0: table.sym("szp_object_a10_start"),
    0x00187FA0: table.sym("data_object_a10_start"),
    0x0C000000: table.sym_var("g_a10_89", "const uintptr_t", "[]", table.GLOBL),
    0x0C000030: table.sym_var("g_a10_87", "const uintptr_t", "[]", table.GLOBL),
    0x0C0001BC: table.sym_var("g_a10_84", "const uintptr_t", "[]", table.GLOBL),
    0x0C000290: table.sym_var("g_a10_85", "const uintptr_t", "[]", table.GLOBL),
    0x0C000328: table.sym_var("g_a10_86", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_b0 = {
    0x00188440: table.sym("szp_object_b0_start"),
    0x001B9070: table.sym("data_object_b0_start"),
    0x0D000000: table.sym_var("g_b0_103", "const uintptr_t", "[]", table.GLOBL),
    0x0D000090: table.sym_var("g_b0_104", "const uintptr_t", "[]", table.GLOBL),
    0x0D0000B0: table.sym_var("g_b0_3", "const uintptr_t", "[]", table.GLOBL), # local
    0x0D0000D8: table.sym_var("g_b0_0D0000D8", "static const uintptr_t", "[]"),
    0x0D000424: table.sym_var("g_b0_0D000424", "static const uintptr_t", "[]"),
    0x0D000770: table.sym_var("g_b0_0D000770", "static const uintptr_t", "[]"),
    0x0D000AB8: table.sym_var("g_b0_0D000AB8", "static const uintptr_t", "[]"),
    0x0D000AC4: table.sym_var("g_b0_100", "const uintptr_t", "[]", table.GLOBL),
    0x0D000B40: table.sym_var("g_b0_105", "const uintptr_t", "[]", table.GLOBL),
    0x0D000BBC: table.sym_var("g_b0_101_179", "const uintptr_t", "[]", table.GLOBL),
    0x0D000BFC: table.sym_var("g_b0_102", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_b1 = {
    0x001B9CC0: table.sym("szp_object_b1_start"),
    0x001C3DB0: table.sym("data_object_b1_start"),
    0x0D000000: table.sym_var("g_b1_105", "const uintptr_t", "[]", table.GLOBL),
    0x0D000284: table.sym_var("g_b1_193", "const uintptr_t", "[]", table.GLOBL),
    0x0D0002F4: table.sym_var("g_b1_179", "const uintptr_t", "[]", table.GLOBL),
    0x0D000324: table.sym_var("g_b1_103", "const uintptr_t", "[]", table.GLOBL),
    0x0D00038C: table.sym_var("g_b1_100", "const uintptr_t", "[]", table.GLOBL),
    0x0D000414: table.sym_var("g_b1_104", "const uintptr_t", "[]", table.GLOBL),
    0x0D000450: table.sym_var("g_b1_101", "const uintptr_t", "[]", table.GLOBL),
    0x0D000468: table.sym_var("g_b1_102", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_b2 = {
    0x001C4230: table.sym("szp_object_b2_start"),
    0x001D7C90: table.sym("data_object_b2_start"),
    0x0D000000: table.sym_var("g_b2_106", "const uintptr_t", "[]", table.GLOBL),
    0x0D0000B8: table.sym_var("g_b2_107", "const uintptr_t", "[]", table.GLOBL),
    0x0D0000D0: table.sym_var("g_b2_191", "const uintptr_t", "[]", table.GLOBL),
    0x0D000214: table.sym_var("g_b2_104", "const uintptr_t", "[]", table.GLOBL),
    0x0D000358: table.sym_var("g_b2_100", "const uintptr_t", "[]", table.GLOBL),
    0x0D000480: table.sym_var("g_b2_103", "const uintptr_t", "[]", table.GLOBL),
    0x0D0005D0: table.sym_var("g_b2_101", "const uintptr_t", "[]", table.GLOBL),
    0x0D0005EC: table.sym_var("g_b2_102", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_b3 = {
    0x001D8310: table.sym("szp_object_b3_start"),
    0x001E4BF0: table.sym("data_object_b3_start"),
    0x0D000000: table.sym_var("g_b3_102", "const uintptr_t", "[]", table.GLOBL),
    0x0D000114: table.sym_var("g_b3_0D000114", "static const uintptr_t", "[]"),
    0x0D00027C: table.sym_var("g_b3_0D00027C", "static const uintptr_t", "[]"),
    0x0D0003E4: table.sym_var("g_b3_221", "const uintptr_t", "[]", table.GLOBL),
    0x0D000448: table.sym_var("g_b3_100", "const uintptr_t", "[]", table.GLOBL),
    0x0D0005B0: table.sym_var("g_b3_101", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_b4 = {
    0x001E51F0: table.sym("szp_object_b4_start"),
    0x001E7D90: table.sym("data_object_b4_start"),
    0x0D000000: table.sym_var("g_b4_0D000000", "static const uintptr_t", "[]"),
    0x0D000078: table.sym_var("g_b4_0D000078", "static const uintptr_t", "[]"),
    0x0D0000F0: table.sym_var("g_b4_102", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_b5 = {
    0x001E7EE0: table.sym("szp_object_b5_start"),
    0x001F1B30: table.sym("data_object_b5_start"),
    0x0D000000: table.sym_var("g_b5_103", "const uintptr_t", "[]", table.GLOBL),
    0x0D00001C: table.sym_var("g_b5_102", "const uintptr_t", "[]", table.GLOBL),
    0x0D0000DC: table.sym_var("g_b5_100", "const uintptr_t", "[]", table.GLOBL),
    0x0D0001A0: table.sym_var("g_b5_206", "const uintptr_t", "[]", table.GLOBL),
    0x0D000230: table.sym_var("g_b5_104", "const uintptr_t", "[]", table.GLOBL),
    0x0D000394: table.sym_var("g_b5_101", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_o_c0 = {
    0x001F2200: table.sym("szp_object_c0_start"),
    0x002008D0: table.sym("data_object_c0_start"),
    0x0F000000: table.sym_var("g_c0_140", "const uintptr_t", "[]", table.GLOBL),
    0x0F000028: table.sym_var("g_c0_194", "const uintptr_t", "[]", table.GLOBL),
    0x0F0001A8: table.sym_var("g_c0_128", "const uintptr_t", "[]", table.GLOBL),
    0x0F0001C0: table.sym_var("g_c0_127", "const uintptr_t", "[]", table.GLOBL),
    0x0F0001D8: table.sym_var("g_c0_223", "const uintptr_t", "[]", table.GLOBL),
    0x0F0004CC: table.sym_var("g_c0_207", "const uintptr_t", "[]", table.GLOBL),
    0x0F0004E4: table.sym_var("g_c0_202", "const uintptr_t", "[]", table.GLOBL),
    0x0F0004FC: table.sym_var("g_c0_120", "const uintptr_t", "[]", table.GLOBL),
    0x0F000518: table.sym_var("g_c0_220", "const uintptr_t", "[]", table.GLOBL),
    0x0F0005D0: table.sym_var("g_c0_129", "const uintptr_t", "[]", table.GLOBL),
    0x0F000610: table.sym_var("g_c0_130", "const uintptr_t", "[]", table.GLOBL),
    0x0F000640: table.sym_var("g_c0_180", "const uintptr_t", "[]", table.GLOBL),
    0x0F00066C: table.sym_var("g_c0_225", "const uintptr_t", "[]", table.GLOBL),
    0x0F000694: table.sym_var("g_c0_137", "const uintptr_t", "[]", table.GLOBL),
    0x0F0006E4: table.sym_var("g_c0_192", "const uintptr_t", "[]", table.GLOBL),
    0x0F0007B8: table.sym_var("g_c0_188", "const uintptr_t", "[]", table.GLOBL),
    0x0F0008F4: table.sym_var("g_c0_195", "const uintptr_t", "[]", table.GLOBL),
    0x0F000A30: table.sym_var("g_c0_217", "const uintptr_t", "[]", table.GLOBL),
    0x0F000A58: table.sym_var("g_c0_131", "const uintptr_t", "[]", table.GLOBL),
    0x0F000AB0: table.sym_var("g_c0_190", "const uintptr_t", "[]", table.GLOBL),
    0x0F000ADC: table.sym_var("g_c0_0F000ADC", "const uintptr_t", "[]"), # unused
    0x0F000B08: table.sym_var("g_c0_0F000B08", "const uintptr_t", "[]"), # unused
}

sym_E0_o_entity = {
    0x00201410: table.sym("szp_object_entity_start"),
    0x00218DA0: table.sym("data_object_entity_start"),
    0x16000000: table.sym_var("g_entity_142", "const uintptr_t", "[]", table.GLOBL),
    0x16000020: table.sym_var("g_entity_224", "const uintptr_t", "[]", table.GLOBL),
    0x16000040: table.sym_var("g_entity_205", "const uintptr_t", "[]", table.GLOBL),
    0x160000A8: table.sym_var("g_entity_187", "const uintptr_t", "[]", table.GLOBL),
    0x1600013C: table.sym_var("g_entity_116", "const uintptr_t", "[]", table.GLOBL),
    0x160001A0: table.sym_var("g_entity_117", "const uintptr_t", "[]", table.GLOBL),
    0x16000200: table.sym_var("g_entity_118", "const uintptr_t", "[]", table.GLOBL),
    0x16000264: table.sym_var("g_entity_119", "const uintptr_t", "[]", table.GLOBL),
    0x160002C4: table.sym_var("g_entity_215", "const uintptr_t", "[]", table.GLOBL),
    0x16000328: table.sym_var("g_entity_216", "const uintptr_t", "[]", table.GLOBL),
    0x16000388: table.sym_var("g_entity_18_22_73", "const uintptr_t", "[]", table.GLOBL), # local
    0x160003A8: table.sym_var("g_entity_28_38", "const uintptr_t", "[]", table.GLOBL), # local
    0x1600043C: table.sym_var("g_entity_39", "const uintptr_t", "[]", table.GLOBL), # local
    0x160004D0: table.sym_var("g_entity_29_39", "const uintptr_t", "[]", table.GLOBL), # local
    0x16000564: table.sym_var("g_entity_16000564", "const uintptr_t", "[]"), # unused
    0x160005F8: table.sym_var("g_entity_31_41", "const uintptr_t", "[]", table.GLOBL), # local
    0x1600068C: table.sym_var("g_entity_32", "const uintptr_t", "[]", table.GLOBL), # local
    0x16000720: table.sym_var("g_entity_29", "const uintptr_t", "[]", table.GLOBL), # local
    0x160007B4: table.sym_var("g_entity_34", "const uintptr_t", "[]", table.GLOBL), # local
    0x16000868: table.sym_var("g_entity_35", "const uintptr_t", "[]", table.GLOBL), # local
    0x1600091C: table.sym_var("g_entity_36", "const uintptr_t", "[]", table.GLOBL), # local
    0x160009D0: table.sym_var("g_entity_37", "const uintptr_t", "[]", table.GLOBL), # local
    0x16000A84: table.sym_var("g_entity_204", "const uintptr_t", "[]", table.GLOBL),
    0x16000AB0: table.sym_var("g_entity_200", "const uintptr_t", "[]", table.GLOBL),
    0x16000B10: table.sym_var("g_entity_203", "const uintptr_t", "[]", table.GLOBL),
    0x16000B2C: table.sym_var("g_entity_144", "const uintptr_t", "[]", table.GLOBL),
    0x16000B8C: table.sym_var("g_entity_145", "const uintptr_t", "[]", table.GLOBL),
    0x16000BEC: table.sym_var("g_entity_186", "const uintptr_t", "[]", table.GLOBL),
    0x16000C44: table.sym_var("g_entity_185", "const uintptr_t", "[]", table.GLOBL),
    0x16000C8C: table.sym_var("g_entity_162", "const uintptr_t", "[]", table.GLOBL),
    0x16000CA4: table.sym_var("g_entity_136", "const uintptr_t", "[]", table.GLOBL),
    0x16000CF0: table.sym_var("g_entity_134", "const uintptr_t", "[]", table.GLOBL),
    0x16000D3C: table.sym_var("g_entity_135", "const uintptr_t", "[]", table.GLOBL),
    0x16000DA8: table.sym_var("g_entity_133", "const uintptr_t", "[]", table.GLOBL),
    0x16000E14: table.sym_var("g_entity_219", "const uintptr_t", "[]", table.GLOBL),
    0x16000E84: table.sym_var("g_entity_212", "const uintptr_t", "[]", table.GLOBL),
    0x16000EA0: table.sym_var("g_entity_122", "const uintptr_t", "[]", table.GLOBL),
    0x16000ED4: table.sym_var("g_entity_138", "const uintptr_t", "[]", table.GLOBL),
    0x16000F24: table.sym_var("g_entity_139", "const uintptr_t", "[]", table.GLOBL),
    0x16000F6C: table.sym_var("g_entity_121", "const uintptr_t", "[]", table.GLOBL),
    0x16000F98: table.sym_var("g_entity_160", "const uintptr_t", "[]", table.GLOBL),
    0x16000FB4: table.sym_var("g_entity_124", "const uintptr_t", "[]", table.GLOBL),
    0x16000FE8: table.sym_var("g_entity_23", "const uintptr_t", "[]", table.GLOBL), # local
    0x16001000: table.sym_var("g_entity_24", "const uintptr_t", "[]", table.GLOBL), # local
    0x16001018: table.sym_var("g_entity_25", "const uintptr_t", "[]", table.GLOBL), # local
    0x16001030: table.sym_var("g_entity_16001030", "const uintptr_t", "[]"), # unused
    0x16001048: table.sym_var("g_entity_27", "const uintptr_t", "[]", table.GLOBL), # local
}

sym_E0_object = {
    0x00219E00: table.sym("data_object_start"),
    0x13000000: table.sym("o_13000000", table.GLOBL),
    0x13000054: table.sym("o_13000054", table.GLOBL),
    0x1300008C: table.sym("o_1300008C", table.GLOBL),
    0x130000AC: table.sym("o_130000AC", table.GLOBL),
    0x130000F8: table.sym("o_130000F8", table.GLOBL),
    0x13000118: table.sym("o_13000118", table.GLOBL),
    0x13000144: table.sym("o_13000144", table.GLOBL),
    0x13000174: table.sym("o_13000174", table.GLOBL),
    0x13000194: table.sym("o_13000194", table.GLOBL),
    0x130001AC: table.sym("o_130001AC", table.GLOBL),
    0x130001CC: table.sym("o_130001CC", table.GLOBL),
    0x130001F4: table.sym("o_130001F4", table.GLOBL),
    0x13000254: table.sym("o_13000254", table.GLOBL),
    0x13000278: table.sym("o_13000278", table.GLOBL),
    0x1300029C: table.sym("o_1300029C", table.GLOBL),
    0x130002B8: table.sym("o_130002B8", table.GLOBL),
    0x130002E4: table.sym("o_130002E4", table.GLOBL),
    0x13000338: table.sym("o_13000338", table.GLOBL),
    0x13000398: table.sym("o_13000398", table.GLOBL),
    0x130003BC: table.sym("o_130003BC", table.GLOBL),
    0x13000400: table.sym("o_13000400", table.GLOBL),
    0x13000428: table.sym("o_13000428", table.GLOBL),
    0x13000444: table.sym("o_13000444", table.GLOBL),
    0x1300046C: table.sym("o_1300046C", table.GLOBL),
    0x13000494: table.sym("o_13000494", table.GLOBL),
    0x130004A8: table.sym("o_130004A8", table.GLOBL),
    0x130004E4: table.sym("o_130004E4", table.GLOBL),
    0x13000528: table.sym("o_13000528", table.GLOBL),
    0x13000584: table.sym("o_13000584", table.GLOBL),
    0x130005B4: table.sym("o_130005B4", table.GLOBL),
    0x130005D8: table.sym("o_130005D8", table.GLOBL),
    0x13000600: table.sym("o_13000600", table.GLOBL),
    0x13000624: table.sym("o_13000624", table.GLOBL),
    0x13000638: table.sym("o_13000638", table.GLOBL),
    0x1300066C: table.sym("o_1300066C", table.GLOBL),
    0x130006A4: table.sym("o_130006A4", table.GLOBL),
    0x130006D8: table.sym("o_130006D8", table.GLOBL),
    0x130006E0: table.sym("o_130006E0", table.GLOBL),
    0x13000708: table.sym("o_13000708", table.GLOBL),
    0x13000720: table.sym("o_13000720", table.GLOBL),
    0x1300075C: table.sym("o_1300075C", table.GLOBL),
    0x13000780: table.sym("o_13000780", table.GLOBL),
    0x130007A0: table.sym("o_130007A0", table.GLOBL),
    0x130007DC: table.sym("o_130007DC", table.GLOBL),
    0x130007F8: table.sym("o_130007F8", table.GLOBL),
    0x1300080C: table.sym("o_1300080C", table.GLOBL),
    0x13000830: table.sym("o_13000830", table.GLOBL),
    0x13000888: table.sym("o_13000888", table.GLOBL),
    0x130008D0: table.sym("o_130008D0", table.GLOBL),
    0x130008EC: table.sym("o_130008EC", table.GLOBL),
    0x1300090C: table.sym("o_1300090C", table.GLOBL),
    0x1300091C: table.sym("o_1300091C", table.GLOBL),
    0x13000940: table.sym("o_13000940", table.GLOBL),
    0x13000964: table.sym("o_13000964", table.GLOBL),
    0x13000984: table.sym("o_13000984", table.GLOBL),
    0x130009A4: table.sym("o_130009A4", table.GLOBL),
    0x130009E0: table.sym("o_130009E0", table.GLOBL),
    0x13000A14: table.sym("o_13000A14", table.GLOBL),
    0x13000A34: table.sym("o_13000A34", table.GLOBL),
    0x13000A54: table.sym("o_13000A54", table.GLOBL),
    0x13000A78: table.sym("o_13000A78", table.GLOBL),
    0x13000A98: table.sym("o_13000A98", table.GLOBL),
    0x13000ABC: table.sym("o_13000ABC", table.GLOBL),
    0x13000AD8: table.sym("o_13000AD8", table.GLOBL),
    0x13000AFC: table.sym("o_13000AFC", table.GLOBL),
    0x13000B0C: table.sym("o_13000B0C", table.GLOBL),
    0x13000B58: table.sym("o_13000B58", table.GLOBL),
    0x13000B8C: table.sym("o_13000B8C", table.GLOBL),
    0x13000BC8: table.sym("o_13000BC8", table.GLOBL),
    0x13000C04: table.sym("o_13000C04", table.GLOBL),
    0x13000C28: table.sym("o_13000C28", table.GLOBL),
    0x13000C44: table.sym("o_13000C44", table.GLOBL),
    0x13000C64: table.sym("o_13000C64", table.GLOBL),
    0x13000C84: table.sym("o_13000C84", table.GLOBL),
    0x13000CFC: table.sym("o_13000CFC", table.GLOBL),
    0x13000D30: table.sym("o_13000D30", table.GLOBL),
    0x13000D6C: table.sym("o_13000D6C", table.GLOBL),
    0x13000D98: table.sym("o_13000D98", table.GLOBL),
    0x13000DB4: table.sym("o_13000DB4", table.GLOBL),
    0x13000DD8: table.sym("o_13000DD8", table.GLOBL),
    0x13000E24: table.sym("o_13000E24", table.GLOBL),
    0x13000E3C: table.sym("o_13000E3C", table.GLOBL),
    0x13000E58: table.sym("o_13000E58", table.GLOBL),
    0x13000E70: table.sym("o_13000E70", table.GLOBL),
    0x13000E88: table.sym("o_13000E88", table.GLOBL),
    0x13000EAC: table.sym("o_13000EAC", table.GLOBL),
    0x13000F08: table.sym("o_13000F08", table.GLOBL),
    0x13000F14: table.sym("o_13000F14", table.GLOBL),
    0x13000F2C: table.sym("o_13000F2C", table.GLOBL),
    0x13000F48: table.sym("o_13000F48", table.GLOBL),
    0x13000F9C: table.sym("o_13000F9C", table.GLOBL),
    0x13000FC8: table.sym("o_13000FC8", table.GLOBL),
    0x13001000: table.sym("o_13001000", table.GLOBL),
    0x13001030: table.sym("o_13001030", table.GLOBL),
    0x13001064: table.sym("o_13001064", table.GLOBL),
    0x130010B8: table.sym("o_130010B8", table.GLOBL),
    0x130010D8: table.sym("o_130010D8", table.GLOBL),
    0x13001108: table.sym("o_13001108", table.GLOBL),
    0x13001124: table.sym("o_13001124", table.GLOBL),
    0x13001168: table.sym("o_13001168", table.GLOBL),
    0x13001184: table.sym("o_13001184", table.GLOBL),
    0x130011D0: table.sym("o_130011D0", table.GLOBL),
    0x130011EC: table.sym("o_130011EC", table.GLOBL),
    0x13001214: table.sym("o_13001214", table.GLOBL),
    0x13001254: table.sym("o_13001254", table.GLOBL),
    0x1300127C: table.sym("o_1300127C", table.GLOBL),
    0x13001298: table.sym("o_13001298", table.GLOBL),
    0x130012B4: table.sym("o_130012B4", table.GLOBL),
    0x130012F4: table.sym("o_130012F4", table.GLOBL),
    0x13001318: table.sym("o_13001318", table.GLOBL),
    0x13001340: table.sym("o_13001340", table.GLOBL),
    0x13001368: table.sym("o_13001368", table.GLOBL),
    0x13001390: table.sym("o_13001390", table.GLOBL),
    0x130013A8: table.sym("o_130013A8", table.GLOBL),
    0x130013C4: table.sym("o_130013C4", table.GLOBL),
    0x130013DC: table.sym("o_130013DC", table.GLOBL),
    0x13001408: table.sym("o_13001408", table.GLOBL),
    0x1300142C: table.sym("o_1300142C", table.GLOBL),
    0x13001448: table.sym("o_13001448", table.GLOBL),
    0x13001468: table.sym("o_13001468", table.GLOBL),
    0x13001478: table.sym("o_13001478", table.GLOBL),
    0x130014AC: table.sym("o_130014AC", table.GLOBL),
    0x130014BC: table.sym("o_130014BC", table.GLOBL),
    0x130014E0: table.sym("o_130014E0", table.GLOBL),
    0x13001518: table.sym("o_13001518", table.GLOBL),
    0x13001548: table.sym("o_13001548", table.GLOBL),
    0x130015A4: table.sym("o_130015A4", table.GLOBL),
    0x130015C0: table.sym("o_130015C0", table.GLOBL),
    0x13001608: table.sym("o_13001608", table.GLOBL),
    0x13001634: table.sym("o_13001634", table.GLOBL),
    0x13001650: table.sym("o_13001650", table.GLOBL),
    0x1300167C: table.sym("o_1300167C", table.GLOBL),
    0x130016B8: table.sym("o_130016B8", table.GLOBL),
    0x130016E4: table.sym("o_130016E4", table.GLOBL),
    0x13001714: table.sym("o_13001714", table.GLOBL),
    0x13001778: table.sym("o_13001778", table.GLOBL),
    0x1300179C: table.sym("o_1300179C", table.GLOBL),
    0x130017F4: table.sym("o_130017F4", table.GLOBL),
    0x13001828: table.sym("o_13001828", table.GLOBL),
    0x13001850: table.sym("o_13001850", table.GLOBL),
    0x130018CC: table.sym("o_130018CC", table.GLOBL),
    0x13001904: table.sym("o_13001904", table.GLOBL),
    0x13001920: table.sym("o_13001920", table.GLOBL),
    0x13001958: table.sym("o_13001958", table.GLOBL),
    0x13001984: table.sym("o_13001984", table.GLOBL),
    0x130019C8: table.sym("o_130019C8", table.GLOBL),
    0x13001A0C: table.sym("o_13001A0C", table.GLOBL),
    0x13001A30: table.sym("o_13001A30", table.GLOBL),
    0x13001A74: table.sym("o_13001A74", table.GLOBL),
    0x13001AA4: table.sym("o_13001AA4", table.GLOBL),
    0x13001AE8: table.sym("o_13001AE8", table.GLOBL),
    0x13001B2C: table.sym("o_13001B2C", table.GLOBL),
    0x13001B54: table.sym("o_13001B54", table.GLOBL),
    0x13001B70: table.sym("o_13001B70", table.GLOBL),
    0x13001B88: table.sym("o_13001B88", table.GLOBL),
    0x13001BB4: table.sym("o_13001BB4", table.GLOBL),
    0x13001BD4: table.sym("o_13001BD4", table.GLOBL),
    0x13001BF4: table.sym("o_13001BF4", table.GLOBL),
    0x13001C04: table.sym("o_13001C04", table.GLOBL),
    0x13001C34: table.sym("o_13001C34", table.GLOBL),
    0x13001C58: table.sym("o_13001C58", table.GLOBL),
    0x13001C7C: table.sym("o_13001C7C", table.GLOBL),
    0x13001C8C: table.sym("o_13001C8C", table.GLOBL),
    0x13001CB0: table.sym("o_13001CB0", table.GLOBL),
    0x13001D0C: table.sym("o_13001D0C", table.GLOBL),
    0x13001D14: table.sym("o_13001D14", table.GLOBL),
    0x13001D40: table.sym("o_13001D40", table.GLOBL),
    0x13001D78: table.sym("o_13001D78", table.GLOBL),
    0x13001DA4: table.sym("o_13001DA4", table.GLOBL),
    0x13001DA8: table.sym("o_13001DA8", table.GLOBL),
    0x13001DCC: table.sym("o_13001DCC", table.GLOBL),
    0x13001E04: table.sym("o_13001E04", table.GLOBL),
    0x13001E30: table.sym("o_13001E30", table.GLOBL),
    0x13001E4C: table.sym("o_13001E4C", table.GLOBL),
    0x13001E6C: table.sym("o_13001E6C", table.GLOBL),
    0x13001E94: table.sym("o_13001E94", table.GLOBL),
    0x13001EC4: table.sym("o_13001EC4", table.GLOBL),
    0x13001EF8: table.sym("o_13001EF8", table.GLOBL),
    0x13001F3C: table.sym("o_13001F3C", table.GLOBL),
    0x13001F68: table.sym("o_13001F68", table.GLOBL),
    0x13001F90: table.sym("o_13001F90", table.GLOBL),
    0x13001FBC: table.sym("o_13001FBC", table.GLOBL),
    0x13002018: table.sym("o_13002018", table.GLOBL),
    0x13002038: table.sym("o_13002038", table.GLOBL),
    0x13002068: table.sym("o_13002068", table.GLOBL),
    0x13002088: table.sym("o_13002088", table.GLOBL),
    0x130020D8: table.sym("o_130020D8", table.GLOBL),
    0x130020E0: table.sym("o_130020E0", table.GLOBL),
    0x130020E8: table.sym("o_130020E8", table.GLOBL),
    0x1300213C: table.sym("o_1300213C", table.GLOBL),
    0x1300214C: table.sym("o_1300214C", table.GLOBL),
    0x1300215C: table.sym("o_1300215C", table.GLOBL),
    0x13002178: table.sym("o_13002178", table.GLOBL),
    0x13002194: table.sym("o_13002194", table.GLOBL),
    0x130021C0: table.sym("o_130021C0", table.GLOBL),
    0x130021E4: table.sym("o_130021E4", table.GLOBL),
    0x1300220C: table.sym("o_1300220C", table.GLOBL),
    0x13002250: table.sym("o_13002250", table.GLOBL),
    0x1300227C: table.sym("o_1300227C", table.GLOBL),
    0x1300229C: table.sym("o_1300229C", table.GLOBL),
    0x130022B8: table.sym("o_130022B8", table.GLOBL),
    0x130022D8: table.sym("o_130022D8", table.GLOBL),
    0x13002308: table.sym("o_13002308", table.GLOBL),
    0x13002338: table.sym("o_13002338", table.GLOBL),
    0x13002388: table.sym("o_13002388", table.GLOBL),
    0x130023A4: table.sym("o_130023A4", table.GLOBL),
    0x130023D0: table.sym("o_130023D0", table.GLOBL),
    0x130023EC: table.sym("o_130023EC", table.GLOBL),
    0x1300241C: table.sym("o_1300241C", table.GLOBL),
    0x1300243C: table.sym("o_1300243C", table.GLOBL),
    0x1300244C: table.sym("o_1300244C", table.GLOBL),
    0x1300246C: table.sym("o_1300246C", table.GLOBL),
    0x13002480: table.sym("o_13002480", table.GLOBL),
    0x130024AC: table.sym("o_130024AC", table.GLOBL),
    0x130024DC: table.sym("o_130024DC", table.GLOBL),
    0x13002500: table.sym("o_13002500", table.GLOBL),
    0x13002528: table.sym("o_13002528", table.GLOBL),
    0x13002568: table.sym("o_13002568", table.GLOBL),
    0x13002588: table.sym("o_13002588", table.GLOBL),
    0x130025C0: table.sym("o_130025C0", table.GLOBL),
    0x130025E0: table.sym("o_130025E0", table.GLOBL),
    0x130025F8: table.sym("o_130025F8", table.GLOBL),
    0x13002620: table.sym("o_13002620", table.GLOBL),
    0x13002634: table.sym("o_13002634", table.GLOBL),
    0x13002650: table.sym("o_13002650", table.GLOBL),
    0x13002684: table.sym("o_13002684", table.GLOBL),
    0x130026D4: table.sym("o_130026D4", table.GLOBL),
    0x13002710: table.sym("o_13002710", table.GLOBL),
    0x13002768: table.sym("o_13002768", table.GLOBL),
    0x1300277C: table.sym("o_1300277C", table.GLOBL),
    0x13002790: table.sym("o_13002790", table.GLOBL),
    0x130027D0: table.sym("o_130027D0", table.GLOBL),
    0x130027E4: table.sym("o_130027E4", table.GLOBL),
    0x130027F4: table.sym("o_130027F4", table.GLOBL),
    0x13002804: table.sym("o_13002804", table.GLOBL),
    0x1300286C: table.sym("o_1300286C", table.GLOBL),
    0x13002898: table.sym("o_13002898", table.GLOBL),
    0x130028CC: table.sym("o_130028CC", table.GLOBL),
    0x130028FC: table.sym("o_130028FC", table.GLOBL),
    0x1300292C: table.sym("o_1300292C", table.GLOBL),
    0x13002968: table.sym("o_13002968", table.GLOBL),
    0x13002998: table.sym("o_13002998", table.GLOBL),
    0x130029B0: table.sym("o_130029B0", table.GLOBL),
    0x13002A20: table.sym("o_13002A20", table.GLOBL),
    0x13002A48: table.sym("o_13002A48", table.GLOBL),
    0x13002A5C: table.sym("o_13002A5C", table.GLOBL),
    0x13002A7C: table.sym("o_13002A7C", table.GLOBL),
    0x13002AA4: table.sym("o_13002AA4", table.GLOBL),
    0x13002AD0: table.sym("o_13002AD0", table.GLOBL),
    0x13002AF0: table.sym("o_13002AF0", table.GLOBL),
    0x13002B08: table.sym("o_13002B08", table.GLOBL),
    0x13002B5C: table.sym("o_13002B5C", table.GLOBL),
    0x13002BA0: table.sym("o_13002BA0", table.GLOBL),
    0x13002BB8: table.sym("o_13002BB8", table.GLOBL),
    0x13002BCC: table.sym("o_13002BCC", table.GLOBL),
    0x13002C14: table.sym("o_13002C14", table.GLOBL),
    0x13002C60: table.sym("o_13002C60", table.GLOBL),
    0x13002C7C: table.sym("o_13002C7C", table.GLOBL),
    0x13002CB0: table.sym("o_13002CB0", table.GLOBL),
    0x13002CE0: table.sym("o_13002CE0", table.GLOBL),
    0x13002D28: table.sym("o_13002D28", table.GLOBL),
    0x13002D50: table.sym("o_13002D50", table.GLOBL),
    0x13002D7C: table.sym("o_13002D7C", table.GLOBL),
    0x13002DB0: table.sym("o_13002DB0", table.GLOBL),
    0x13002DC0: table.sym("o_13002DC0", table.GLOBL),
    0x13002E04: table.sym("o_13002E04", table.GLOBL),
    0x13002E20: table.sym("o_13002E20", table.GLOBL),
    0x13002E3C: table.sym("o_13002E3C", table.GLOBL),
    0x13002E58: table.sym("o_13002E58", table.GLOBL),
    0x13002EA8: table.sym("o_13002EA8", table.GLOBL),
    0x13002EC0: table.sym("o_mario", table.GLOBL),
    0x13002EF8: table.sym("o_13002EF8", table.GLOBL),
    0x13002F40: table.sym("o_13002F40", table.GLOBL),
    0x13002F60: table.sym("o_13002F60", table.GLOBL),
    0x13002F64: table.sym("o_13002F64", table.GLOBL),
    0x13002F68: table.sym("o_13002F68", table.GLOBL),
    0x13002F6C: table.sym("o_13002F6C", table.GLOBL),
    0x13002F70: table.sym("o_13002F70", table.GLOBL),
    0x13002F74: table.sym("o_13002F74", table.GLOBL),
    0x13002F78: table.sym("o_13002F78", table.GLOBL),
    0x13002F7C: table.sym("o_13002F7C", table.GLOBL),
    0x13002F80: table.sym("o_13002F80", table.GLOBL),
    0x13002F84: table.sym("o_13002F84", table.GLOBL),
    0x13002F88: table.sym("o_13002F88", table.GLOBL),
    0x13002F8C: table.sym("o_13002F8C", table.GLOBL),
    0x13002F90: table.sym("o_13002F90", table.GLOBL),
    0x13002F94: table.sym("o_13002F94", table.GLOBL),
    0x13002FC0: table.sym("o_13002FC0", table.GLOBL),
    0x13002FE4: table.sym("o_13002FE4", table.GLOBL),
    0x13003008: table.sym("o_13003008", table.GLOBL),
    0x1300302C: table.sym("o_1300302C", table.GLOBL),
    0x13003048: table.sym("o_13003048", table.GLOBL),
    0x13003068: table.sym("o_13003068", table.GLOBL),
    0x130030A4: table.sym("o_130030A4", table.GLOBL),
    0x130030D4: table.sym("o_130030D4", table.GLOBL),
    0x13003104: table.sym("o_13003104", table.GLOBL),
    0x13003134: table.sym("o_13003134", table.GLOBL),
    0x13003158: table.sym("o_13003158", table.GLOBL),
    0x13003174: table.sym("o_13003174", table.GLOBL),
    0x130031AC: table.sym("o_130031AC", table.GLOBL),
    0x130031DC: table.sym("o_130031DC", table.GLOBL),
    0x13003228: table.sym("o_13003228", table.GLOBL),
    0x13003274: table.sym("o_13003274", table.GLOBL),
    0x130032A8: table.sym("o_130032A8", table.GLOBL),
    0x130032C8: table.sym("o_130032C8", table.GLOBL),
    0x130032E0: table.sym("o_130032E0", table.GLOBL),
    0x13003324: table.sym("o_13003324", table.GLOBL),
    0x13003354: table.sym("o_13003354", table.GLOBL),
    0x13003388: table.sym("o_13003388", table.GLOBL),
    0x130033BC: table.sym("o_130033BC", table.GLOBL),
    0x130033EC: table.sym("o_130033EC", table.GLOBL),
    0x13003454: table.sym("o_13003454", table.GLOBL),
    0x13003464: table.sym("o_13003464", table.GLOBL),
    0x1300346C: table.sym("o_1300346C", table.GLOBL),
    0x13003474: table.sym("o_13003474", table.GLOBL),
    0x13003484: table.sym("o_13003484", table.GLOBL),
    0x130034C4: table.sym("o_130034C4", table.GLOBL),
    0x13003510: table.sym("o_13003510", table.GLOBL),
    0x13003558: table.sym("o_13003558", table.GLOBL),
    0x13003588: table.sym("o_13003588", table.GLOBL),
    0x130035B0: table.sym("o_130035B0", table.GLOBL),
    0x13003600: table.sym("o_13003600", table.GLOBL),
    0x13003614: table.sym("o_13003614", table.GLOBL),
    0x1300362C: table.sym("o_1300362C", table.GLOBL),
    0x13003660: table.sym("o_13003660", table.GLOBL),
    0x13003694: table.sym("o_13003694", table.GLOBL),
    0x13003700: table.sym("o_13003700", table.GLOBL),
    0x13003738: table.sym("o_13003738", table.GLOBL),
    0x13003750: table.sym("o_13003750", table.GLOBL),
    0x13003798: table.sym("o_13003798", table.GLOBL),
    0x130037E0: table.sym("o_130037E0", table.GLOBL),
    0x130037EC: table.sym("o_130037EC", table.GLOBL),
    0x1300381C: table.sym("o_1300381C", table.GLOBL),
    0x13003840: table.sym("o_13003840", table.GLOBL),
    0x13003868: table.sym("o_13003868", table.GLOBL),
    0x13003888: table.sym("o_13003888", table.GLOBL),
    0x130038B0: table.sym("o_130038B0", table.GLOBL),
    0x130038D0: table.sym("o_130038D0", table.GLOBL),
    0x130038E8: table.sym("o_130038E8", table.GLOBL),
    0x13003910: table.sym("o_13003910", table.GLOBL),
    0x13003940: table.sym("o_13003940", table.GLOBL),
    0x13003970: table.sym("o_13003970", table.GLOBL),
    0x130039A0: table.sym("o_130039A0", table.GLOBL),
    0x130039D4: table.sym("o_130039D4", table.GLOBL),
    0x13003A08: table.sym("o_13003A08", table.GLOBL),
    0x13003A30: table.sym("o_13003A30", table.GLOBL),
    0x13003A58: table.sym("o_13003A58", table.GLOBL),
    0x13003A80: table.sym("o_13003A80", table.GLOBL),
    0x13003AA4: table.sym("o_13003AA4", table.GLOBL),
    0x13003AC8: table.sym("o_13003AC8", table.GLOBL),
    0x13003AE0: table.sym("o_13003AE0", table.GLOBL),
    0x13003B00: table.sym("o_13003B00", table.GLOBL),
    0x13003B30: table.sym("o_13003B30", table.GLOBL),
    0x13003B60: table.sym("o_13003B60", table.GLOBL),
    0x13003B98: table.sym("o_13003B98", table.GLOBL),
    0x13003BB4: table.sym("o_13003BB4", table.GLOBL),
    0x13003BEC: table.sym("o_13003BEC", table.GLOBL),
    0x13003C0C: table.sym("o_13003C0C", table.GLOBL),
    0x13003C30: table.sym("o_13003C30", table.GLOBL),
    0x13003C44: table.sym("o_13003C44", table.GLOBL),
    0x13003C58: table.sym("o_13003C58", table.GLOBL),
    0x13003C7C: table.sym("o_13003C7C", table.GLOBL),
    0x13003C90: table.sym("o_13003C90", table.GLOBL),
    0x13003CA4: table.sym("o_13003CA4", table.GLOBL),
    0x13003CB8: table.sym("o_13003CB8", table.GLOBL),
    0x13003CE4: table.sym("o_13003CE4", table.GLOBL),
    0x13003D0C: table.sym("o_13003D0C", table.GLOBL),
    0x13003D34: table.sym("o_13003D34", table.GLOBL),
    0x13003D4C: table.sym("o_13003D4C", table.GLOBL),
    0x13003D74: table.sym("o_13003D74", table.GLOBL),
    0x13003DA0: table.sym("o_13003DA0", table.GLOBL),
    0x13003DB8: table.sym("o_13003DB8", table.GLOBL),
    0x13003DD8: table.sym("o_13003DD8", table.GLOBL),
    0x13003DF8: table.sym("o_13003DF8", table.GLOBL),
    0x13003E1C: table.sym("o_13003E1C", table.GLOBL),
    0x13003E3C: table.sym("o_13003E3C", table.GLOBL),
    0x13003E64: table.sym("o_13003E64", table.GLOBL),
    0x13003E8C: table.sym("o_13003E8C", table.GLOBL),
    0x13003EAC: table.sym("o_13003EAC", table.GLOBL),
    0x13003EE4: table.sym("o_13003EE4", table.GLOBL),
    0x13003EFC: table.sym("o_13003EFC", table.GLOBL),
    0x13003F1C: table.sym("o_13003F1C", table.GLOBL),
    0x13003F40: table.sym("o_13003F40", table.GLOBL),
    0x13003F78: table.sym("o_13003F78", table.GLOBL),
    0x13003FA4: table.sym("o_13003FA4", table.GLOBL),
    0x13003FDC: table.sym("o_13003FDC", table.GLOBL),
    0x13004010: table.sym("o_13004010", table.GLOBL),
    0x13004044: table.sym("o_13004044", table.GLOBL),
    0x1300407C: table.sym("o_1300407C", table.GLOBL),
    0x130040B4: table.sym("o_130040B4", table.GLOBL),
    0x130040EC: table.sym("o_130040EC", table.GLOBL),
    0x13004124: table.sym("o_13004124", table.GLOBL),
    0x13004148: table.sym("o_13004148", table.GLOBL),
    0x13004180: table.sym("o_13004180", table.GLOBL),
    0x130041A4: table.sym("o_130041A4", table.GLOBL),
    0x130041BC: table.sym("o_130041BC", table.GLOBL),
    0x130041F0: table.sym("o_130041F0", table.GLOBL),
    0x13004218: table.sym("o_13004218", table.GLOBL),
    0x13004244: table.sym("o_13004244", table.GLOBL),
    0x13004270: table.sym("o_13004270", table.GLOBL),
    0x13004284: table.sym("o_13004284", table.GLOBL),
    0x130042B4: table.sym("o_130042B4", table.GLOBL),
    0x130042E4: table.sym("o_130042E4", table.GLOBL),
    0x13004314: table.sym("o_13004314", table.GLOBL),
    0x13004348: table.sym("o_13004348", table.GLOBL),
    0x13004370: table.sym("o_13004370", table.GLOBL),
    0x130043A0: table.sym("o_130043A0", table.GLOBL),
    0x130043C4: table.sym("o_130043C4", table.GLOBL),
    0x130043E0: table.sym("o_130043E0", table.GLOBL),
    0x1300442C: table.sym("o_1300442C", table.GLOBL),
    0x1300444C: table.sym("o_1300444C", table.GLOBL),
    0x13004470: table.sym("o_13004470", table.GLOBL),
    0x13004494: table.sym("o_13004494", table.GLOBL),
    0x130044B8: table.sym("o_130044B8", table.GLOBL),
    0x130044E0: table.sym("o_130044E0", table.GLOBL),
    0x130044FC: table.sym("o_130044FC", table.GLOBL),
    0x13004538: table.sym("o_13004538", table.GLOBL),
    0x13004580: table.sym("o_13004580", table.GLOBL),
    0x130045D0: table.sym("o_130045D0", table.GLOBL),
    0x130045F8: table.sym("o_130045F8", table.GLOBL),
    0x13004634: table.sym("o_13004634", table.GLOBL),
    0x13004668: table.sym("o_13004668", table.GLOBL),
    0x13004698: table.sym("o_13004698", table.GLOBL),
    0x130046DC: table.sym("o_130046DC", table.GLOBL),
    0x1300472C: table.sym("o_1300472C", table.GLOBL),
    0x13004770: table.sym("o_13004770", table.GLOBL),
    0x1300478C: table.sym("o_1300478C", table.GLOBL),
    0x130047E4: table.sym("o_130047E4", table.GLOBL),
    0x1300481C: table.sym("o_1300481C", table.GLOBL),
    0x13004868: table.sym("o_13004868", table.GLOBL),
    0x13004898: table.sym("o_13004898", table.GLOBL),
    0x130048E0: table.sym("o_130048E0", table.GLOBL),
    0x13004918: table.sym("o_13004918", table.GLOBL),
    0x13004954: table.sym("o_13004954", table.GLOBL),
    0x13004988: table.sym("o_13004988", table.GLOBL),
    0x130049AC: table.sym("o_130049AC", table.GLOBL),
    0x130049C8: table.sym("o_130049C8", table.GLOBL),
    0x13004A00: table.sym("o_13004A00", table.GLOBL),
    0x13004A58: table.sym("o_13004A58", table.GLOBL),
    0x13004A78: table.sym("o_13004A78", table.GLOBL),
    0x13004AB0: table.sym("o_13004AB0", table.GLOBL),
    0x13004AF4: table.sym("o_13004AF4", table.GLOBL),
    0x13004B1C: table.sym("o_13004B1C", table.GLOBL),
    0x13004B44: table.sym("o_13004B44", table.GLOBL),
    0x13004B6C: table.sym("o_13004B6C", table.GLOBL),
    0x13004B8C: table.sym("o_13004B8C", table.GLOBL),
    0x13004BA8: table.sym("o_13004BA8", table.GLOBL),
    0x13004BD4: table.sym("o_13004BD4", table.GLOBL),
    0x13004BF0: table.sym("o_13004BF0", table.GLOBL),
    0x13004C24: table.sym("o_13004C24", table.GLOBL),
    0x13004C5C: table.sym("o_13004C5C", table.GLOBL),
    0x13004C94: table.sym("o_13004C94", table.GLOBL),
    0x13004CCC: table.sym("o_13004CCC", table.GLOBL),
    0x13004CF8: table.sym("o_13004CF8", table.GLOBL),
    0x13004D28: table.sym("o_13004D28", table.GLOBL),
    0x13004D64: table.sym("o_13004D64", table.GLOBL),
    0x13004D90: table.sym("o_13004D90", table.GLOBL),
    0x13004DBC: table.sym("o_13004DBC", table.GLOBL),
    0x13004E08: table.sym("o_13004E08", table.GLOBL),
    0x13004E4C: table.sym("o_13004E4C", table.GLOBL),
    0x13004E78: table.sym("o_13004E78", table.GLOBL),
    0x13004EA0: table.sym("o_13004EA0", table.GLOBL),
    0x13004ECC: table.sym("o_13004ECC", table.GLOBL),
    0x13004EF8: table.sym("o_13004EF8", table.GLOBL),
    0x13004F10: table.sym("o_13004F10", table.GLOBL),
    0x13004F28: table.sym("o_13004F28", table.GLOBL),
    0x13004F40: table.sym("o_13004F40", table.GLOBL),
    0x13004F78: table.sym("o_13004F78", table.GLOBL),
    0x13004F90: table.sym("o_13004F90", table.GLOBL),
    0x13004FD4: table.sym("o_13004FD4", table.GLOBL),
    0x13005024: table.sym("o_13005024", table.GLOBL),
    0x1300506C: table.sym("o_1300506C", table.GLOBL),
    0x130050B4: table.sym("o_130050B4", table.GLOBL),
    0x130050D4: table.sym("o_130050D4", table.GLOBL),
    0x130050F4: table.sym("o_130050F4", table.GLOBL),
    0x13005120: table.sym("o_13005120", table.GLOBL),
    0x13005158: table.sym("o_13005158", table.GLOBL),
    0x1300518C: table.sym("o_1300518C", table.GLOBL),
    0x130051AC: table.sym("o_130051AC", table.GLOBL),
    0x130051E0: table.sym("o_130051E0", table.GLOBL),
    0x1300521C: table.sym("o_1300521C", table.GLOBL),
    0x1300525C: table.sym("o_1300525C", table.GLOBL),
    0x130052B4: table.sym("o_130052B4", table.GLOBL),
    0x130052D0: table.sym("o_130052D0", table.GLOBL),
    0x13005310: table.sym("o_13005310", table.GLOBL),
    0x13005354: table.sym("o_13005354", table.GLOBL),
    0x13005380: table.sym("o_13005380", table.GLOBL),
    0x130053C4: table.sym("o_130053C4", table.GLOBL),
    0x130053DC: table.sym("o_130053DC", table.GLOBL),
    0x130053F4: table.sym("o_130053F4", table.GLOBL),
    0x13005414: table.sym("o_13005414", table.GLOBL),
    0x13005440: table.sym("o_13005440", table.GLOBL),
    0x13005468: table.sym("o_13005468", table.GLOBL),
    0x130054A0: table.sym("o_130054A0", table.GLOBL),
    0x130054B8: table.sym("o_130054B8", table.GLOBL),
    0x130054EC: table.sym("o_130054EC", table.GLOBL),
    0x13005504: table.sym("o_13005504", table.GLOBL),
    0x13005528: table.sym("o_13005528", table.GLOBL),
    0x1300556C: table.sym("o_1300556C", table.GLOBL),
    0x13005598: table.sym("o_13005598", table.GLOBL),
    0x130055DC: table.sym("o_130055DC", table.GLOBL),
    0x13005610: table.sym("o_13005610", table.GLOBL),
    0x13005638: table.sym("o_13005638", table.GLOBL),
    0x1300565C: table.sym("o_1300565C", table.GLOBL),
    0x13005680: table.sym("o_13005680", table.GLOBL),
    0x130056A4: table.sym("o_130056A4", table.GLOBL),
}

# title

sym_E0_s_title = {
    0x8016F000: table.sym("code_menu_start"),
    0x00269EA0: table.sym("data_stage_title_start"),
    0x14000000: table.sym("s_logo", table.GLOBL),
    0x14000078: table.sym("s_face_title", table.GLOBL),
    0x14000104: table.sym("s_face_game_over", table.GLOBL),
    0x14000190: table.sym("s_select_stage", table.GLOBL),
    0x140002D0: table.sym_var("g_logo", "const uintptr_t", "[]", table.GLOBL),
    0x1400035C: table.sym_var("g_face_title", "const uintptr_t", "[]", table.GLOBL),
    0x140003B8: table.sym_var("g_face_game_over", "const uintptr_t", "[]", table.GLOBL),
    0x14000414: table.sym_var("g_select_stage", "const uintptr_t", "[]", table.GLOBL),
    0x0026A3A0: table.sym("szp_stage_title_a_start"),
    0x0026F420: table.sym("szp_stage_title_b_start"),
    0x002708C0: table.sym("szp_background_title_start"),
}

# background/title

# face/data

sym_E0_s_menu = {
    0x002A6120: table.sym("data_stage_menu_start"),
    0x002A65B0: table.sym("szp_stage_menu_start"),
    0x14000000: table.sym("s_file_select", table.GLOBL),
    0x14000118: table.sym("s_star_select", table.GLOBL),
    0x140001D0: table.sym_var("g_menu_3", "const uintptr_t", "[]", table.GLOBL),
    0x14000200: table.sym_var("g_menu_8", "const uintptr_t", "[]", table.GLOBL),
    0x14000230: table.sym_var("g_menu_9", "const uintptr_t", "[]", table.GLOBL),
    0x14000260: table.sym_var("g_menu_10", "const uintptr_t", "[]", table.GLOBL),
    0x14000290: table.sym_var("g_menu_4", "const uintptr_t", "[]", table.GLOBL),
    0x140002B8: table.sym_var("g_menu_5", "const uintptr_t", "[]", table.GLOBL),
    0x140002E0: table.sym_var("g_menu_6", "const uintptr_t", "[]", table.GLOBL),
    0x14000308: table.sym_var("g_menu_7", "const uintptr_t", "[]", table.GLOBL),
    0x14000330: table.sym_var("g_menu_11", "const uintptr_t", "[]", table.GLOBL),
    0x14000358: table.sym_var("g_menu_12", "const uintptr_t", "[]", table.GLOBL),
    0x14000380: table.sym_var("g_file_select", "const uintptr_t", "[]", table.GLOBL),
    0x14000408: table.sym_var("g_star_select", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_game = {
    0x002ABCA0: table.sym("data_game_start"),
    0x15000000: table.sym("s_game", table.GLOBL),
    0x15000278: table.sym("s_game_stage"),
    0x15000660: table.sym("s_object_c0", table.GLOBL),
    0x1500071C: table.sym("s_object_a0", table.GLOBL),
    0x15000750: table.sym("s_object_a1", table.GLOBL),
    0x1500076C: table.sym("s_object_a2", table.GLOBL),
    0x15000788: table.sym("s_object_a3", table.GLOBL),
    0x150007B4: table.sym("s_object_a4", table.GLOBL),
    0x150007E8: table.sym("s_object_a5", table.GLOBL),
    0x1500080C: table.sym("s_object_a6", table.GLOBL),
    0x15000830: table.sym("s_object_a7", table.GLOBL),
    0x1500084C: table.sym("s_object_a8", table.GLOBL),
    0x15000888: table.sym("s_object_a9", table.GLOBL),
    0x150008A4: table.sym("s_object_a10", table.GLOBL),
    0x150008D8: table.sym("s_object_b0", table.GLOBL),
    0x15000914: table.sym("s_object_b1", table.GLOBL),
    0x15000958: table.sym("s_object_b2", table.GLOBL),
    0x1500099C: table.sym("s_object_b3", table.GLOBL),
    0x150009C0: table.sym("s_object_b4", table.GLOBL),
    0x150009DC: table.sym("s_object_b5", table.GLOBL),
}

fnc_E0_game = {
    0x15000724: 0x0012A7E0,
    0x1500072C: 0x0012A7E0,
    0x15000758: 0x00132C60,
    0x15000774: 0x00134D20,
    0x1500077C: 0x00134D20,
    0x150007A8: 0x0013B910,
    0x150007CC: 0x00145E90,
    0x150007F0: 0x001521D0,
    0x1500080C: 0x00160670,
    0x1500086C: 0x00166C60,
    0x15000888: 0x0016D870,
    0x150008F8: 0x00188440,
    0x1500094C: 0x001B9CC0,
    0x15000988: 0x001C4230,
    0x150009A4: 0x001D8310,
    0x150009AC: 0x001D8310,
}

sym_E0_bg = {
    0x002AC6B0: table.sym("szp_background_a_start"),
    0x002B8F10: table.sym("szp_background_b_start"),
    0x002C73D0: table.sym("szp_background_c_start"),
    0x002D0040: table.sym("szp_background_d_start"),
    0x002D64F0: table.sym("szp_background_e_start"),
    0x002E7880: table.sym("szp_background_f_start"),
    0x002F14E0: table.sym("szp_background_g_start"),
    0x002FB1B0: table.sym("szp_background_h_start"),
    0x00301CD0: table.sym("szp_background_i_start"),
    0x0030CEC0: table.sym("szp_background_j_start"),
}

sym_E0_texture = {
    0x0031E1D0: table.sym("szp_texture_a_start"),
    0x00326E40: table.sym("szp_texture_b_start"),
    0x0032D070: table.sym("szp_texture_c_start"),
    0x00334B30: table.sym("szp_texture_d_start"),
    0x0033D710: table.sym("szp_texture_e_start"),
    0x00341140: table.sym("szp_texture_f_start"),
    0x00347A50: table.sym("szp_texture_g_start"),
    0x0034E760: table.sym("szp_texture_h_start"),
    0x00351960: table.sym("szp_texture_i_start"),
    0x00357350: table.sym("szp_texture_j_start"),
    0x0035ED10: table.sym("szp_texture_k_start"),
    0x00365980: table.sym("szp_texture_l_start"),
}

sym_E0_particle = {
    0x0036F530: table.sym("szp_particle_a_start"),
}

sym_E0_s_bbh = {
    0x00371C40: table.sym("szp_stage_bbh_start"),
    0x003828C0: table.sym("data_stage_bbh_start"),
    0x0E000000: table.sym("s_bbh_0E000000"),
    0x0E000094: table.sym("s_bbh_0E000094"),
    0x0E000128: table.sym("s_bbh_0E000128"),
    0x0E0003CC: table.sym("s_bbh_0E0003CC"),
    0x0E000418: table.sym("s_bbh", table.GLOBL),
    0x0E0005B0: table.sym_var("g_bbh_53", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005C8: table.sym_var("g_bbh_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005E0: table.sym_var("g_bbh_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005F8: table.sym_var("g_bbh_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E000610: table.sym_var("g_bbh_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E000628: table.sym_var("g_bbh_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E000640: table.sym_var("g_bbh_59", "const uintptr_t", "[]", table.GLOBL),
    0x0E000658: table.sym_var("g_bbh_60", "const uintptr_t", "[]", table.GLOBL),
    0x0E000670: table.sym_var("g_bbh1_1", "static const uintptr_t", "[]"),
    0x0E0006B0: table.sym_var("g_bbh1_2", "static const uintptr_t", "[]"),
    0x0E0006E8: table.sym_var("g_bbh1_3", "static const uintptr_t", "[]"),
    0x0E000730: table.sym_var("g_bbh1_4", "static const uintptr_t", "[]"),
    0x0E000750: table.sym_var("g_bbh1_5", "static const uintptr_t", "[]"),
    0x0E000768: table.sym_var("g_bbh1_6", "static const uintptr_t", "[]"),
    0x0E0007B0: table.sym_var("g_bbh1_7", "static const uintptr_t", "[]"),
    0x0E0007D0: table.sym_var("g_bbh1_8", "static const uintptr_t", "[]"),
    0x0E000800: table.sym_var("g_bbh1_9", "static const uintptr_t", "[]"),
    0x0E000828: table.sym_var("g_bbh1_10", "static const uintptr_t", "[]"),
    0x0E000860: table.sym_var("g_bbh1_11", "static const uintptr_t", "[]"),
    0x0E000888: table.sym_var("g_bbh1_12", "static const uintptr_t", "[]"),
    0x0E0008B0: table.sym_var("g_bbh1_13", "static const uintptr_t", "[]"),
    0x0E0008E8: table.sym_var("g_bbh1_14", "static const uintptr_t", "[]"),
    0x0E000950: table.sym_var("g_bbh1_15", "static const uintptr_t", "[]"),
    0x0E0009C8: table.sym_var("g_bbh1_16", "static const uintptr_t", "[]"),
    0x0E000A18: table.sym_var("g_bbh1_17", "static const uintptr_t", "[]"),
    0x0E000A60: table.sym_var("g_bbh1_18", "static const uintptr_t", "[]"),
    0x0E000AD8: table.sym_var("g_bbh1_19", "static const uintptr_t", "[]"),
    0x0E000B28: table.sym_var("g_bbh1_20", "static const uintptr_t", "[]"),
    0x0E000B88: table.sym_var("g_bbh1_21", "static const uintptr_t", "[]"),
    0x0E000BF0: table.sym_var("g_bbh1_22", "static const uintptr_t", "[]"),
    0x0E000C38: table.sym_var("g_bbh1_23", "static const uintptr_t", "[]"),
    0x0E000C88: table.sym_var("g_bbh1_24", "static const uintptr_t", "[]"),
    0x0E000CE8: table.sym_var("g_bbh1_25", "static const uintptr_t", "[]"),
    0x0E000D20: table.sym_var("g_bbh1_26", "static const uintptr_t", "[]"),
    0x0E000D68: table.sym_var("g_bbh1_27", "static const uintptr_t", "[]"),
    0x0E000DB0: table.sym_var("g_bbh1_28", "static const uintptr_t", "[]"),
    0x0E000DF0: table.sym_var("g_bbh1_29", "static const uintptr_t", "[]"),
    0x0E000E40: table.sym_var("g_bbh1_30", "static const uintptr_t", "[]"),
    0x0E000E80: table.sym_var("g_bbh1_31", "static const uintptr_t", "[]"),
    0x0E000EB0: table.sym_var("g_bbh1_32", "static const uintptr_t", "[]"),
    0x0E000F00: table.sym_var("g_bbh", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_ccm = {
    0x00383950: table.sym("szp_stage_ccm_start"),
    0x00395C90: table.sym("data_stage_ccm_start"),
    0x0E000000: table.sym("s_ccm_0E000000"),
    0x0E00001C: table.sym("s_ccm_0E00001C"),
    0x0E000098: table.sym("s_ccm_0E000098"),
    0x0E000114: table.sym("s_ccm_0E000114"),
    0x0E000178: table.sym("s_ccm", table.GLOBL),
    0x0E0003E0: table.sym_var("g_ccm_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000400: table.sym_var("g_ccm_210", "const uintptr_t", "[]", table.GLOBL),
    0x0E00041C: table.sym_var("g_ccm_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E00043C: table.sym_var("g_ccm_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E00046C: table.sym_var("g_ccm_4", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004A4: table.sym_var("g_ccm_5", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004CC: table.sym_var("g_ccm_6", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004F4: table.sym_var("g_ccm_7", "const uintptr_t", "[]", table.GLOBL),
    0x0E00052C: table.sym_var("g_ccm1", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005F8: table.sym_var("g_ccm2", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_inside = {
    0x00396340: table.sym("szp_stage_inside_start"),
    0x003CF0D0: table.sym("data_stage_inside_start"),
    0x0E000000: table.sym("s_inside_0E000000"),
    0x0E0003F4: table.sym("s_inside_0E0003F4"),
    0x0E000790: table.sym("s_inside_0E000790"),
    0x0E0009BC: table.sym("s_inside_0E0009BC"),
    0x0E000AF8: table.sym("s_inside", table.GLOBL),
    0x0E000F00: table.sym_var("g_inside_208_209_213_214", "const uintptr_t", "[]", table.GLOBL),
    0x0E000F18: table.sym_var("g_inside_53", "const uintptr_t", "[]", table.GLOBL),
    0x0E000F30: table.sym_var("g_inside1_1", "static const uintptr_t", "[]"),
    0x0E000F70: table.sym_var("g_inside1_2", "static const uintptr_t", "[]"),
    0x0E000F88: table.sym_var("g_inside1_3", "static const uintptr_t", "[]"),
    0x0E000FA8: table.sym_var("g_inside1_4", "static const uintptr_t", "[]"),
    0x0E000FD0: table.sym_var("g_inside1_5", "static const uintptr_t", "[]"),
    0x0E001000: table.sym_var("g_inside1_6", "static const uintptr_t", "[]"),
    0x0E001038: table.sym_var("g_inside1_7", "static const uintptr_t", "[]"),
    0x0E001088: table.sym_var("g_inside1_8", "static const uintptr_t", "[]"),
    0x0E0010C8: table.sym_var("g_inside1_9", "static const uintptr_t", "[]"),
    0x0E001110: table.sym_var("g_inside1_10", "static const uintptr_t", "[]"),
    0x0E001158: table.sym_var("g_inside1_11", "static const uintptr_t", "[]"),
    0x0E0011A8: table.sym_var("g_inside1_12", "static const uintptr_t", "[]"),
    0x0E001200: table.sym_var("g_inside1_13", "static const uintptr_t", "[]"),
    0x0E001260: table.sym_var("g_inside1_14", "static const uintptr_t", "[]"),
    0x0E0012C8: table.sym_var("g_inside1_15", "static const uintptr_t", "[]"),
    0x0E001348: table.sym_var("g_inside1_16", "static const uintptr_t", "[]"),
    0x0E0013B8: table.sym_var("g_inside1_17", "static const uintptr_t", "[]"),
    0x0E001400: table.sym_var("g_inside1", "const uintptr_t", "[]", table.GLOBL),
    0x0E001518: table.sym_var("g_inside_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E001530: table.sym_var("g_inside_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E001548: table.sym_var("g_inside_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E001560: table.sym_var("g_inside2_1", "static const uintptr_t", "[]"),
    0x0E001578: table.sym_var("g_inside2_2", "static const uintptr_t", "[]"),
    0x0E0015B8: table.sym_var("g_inside2_3", "static const uintptr_t", "[]"),
    0x0E0015F8: table.sym_var("g_inside2_4", "static const uintptr_t", "[]"),
    0x0E001628: table.sym_var("g_inside2_5", "static const uintptr_t", "[]"),
    0x0E001668: table.sym_var("g_inside2_6", "static const uintptr_t", "[]"),
    0x0E001690: table.sym_var("g_inside2_7", "static const uintptr_t", "[]"),
    0x0E0016D8: table.sym_var("g_inside2_8", "static const uintptr_t", "[]"),
    0x0E001740: table.sym_var("g_inside2_9", "static const uintptr_t", "[]"),
    0x0E001798: table.sym_var("g_inside2_10", "static const uintptr_t", "[]"),
    0x0E001800: table.sym_var("g_inside2_11", "static const uintptr_t", "[]"),
    0x0E001858: table.sym_var("g_inside2", "const uintptr_t", "[]", table.GLOBL),
    0x0E001940: table.sym_var("g_inside_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E001958: table.sym_var("g_inside3_1", "static const uintptr_t", "[]"),
    0x0E001980: table.sym_var("g_inside3_2", "static const uintptr_t", "[]"),
    0x0E0019C8: table.sym_var("g_inside3_3", "static const uintptr_t", "[]"),
    0x0E0019F8: table.sym_var("g_inside3_4", "static const uintptr_t", "[]"),
    0x0E001A30: table.sym_var("g_inside3_5", "static const uintptr_t", "[]"),
    0x0E001A58: table.sym_var("g_inside3_6", "static const uintptr_t", "[]"),
    0x0E001AB8: table.sym_var("g_inside3_7", "static const uintptr_t", "[]"),
    0x0E001AF8: table.sym_var("g_inside3_8", "static const uintptr_t", "[]"),
    0x0E001B48: table.sym_var("g_inside3_9", "static const uintptr_t", "[]"),
    0x0E001BB0: table.sym_var("g_inside3_10", "static const uintptr_t", "[]"),
    0x0E001C10: table.sym_var("g_inside3", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_hmc = {
    0x003D0DC0: table.sym("szp_stage_hmc_start"),
    0x003E6A00: table.sym("data_stage_hmc_start"),
    0x0E000000: table.sym("s_hmc_0E000000"),
    0x0E0001CC: table.sym("s_hmc_0E0001CC"),
    0x0E000290: table.sym("s_hmc_0E000290"),
    0x0E0002F4: table.sym("s_hmc_0E0002F4"),
    0x0E000388: table.sym("s_hmc", table.GLOBL),
    0x0E000530: table.sym_var("g_hmc_60", "const uintptr_t", "[]", table.GLOBL),
    0x0E000548: table.sym_var("g_hmc_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E000570: table.sym_var("g_hmc_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E000588: table.sym_var("g_hmc_59", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005A0: table.sym_var("g_hmc_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005B8: table.sym_var("g_hmc_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005D0: table.sym_var("g_hmc_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005E8: table.sym_var("g_hmc1_1", "static const uintptr_t", "[]"),
    0x0E000618: table.sym_var("g_hmc1_2", "static const uintptr_t", "[]"),
    0x0E000658: table.sym_var("g_hmc1_3", "static const uintptr_t", "[]"),
    0x0E0006A8: table.sym_var("g_hmc1_4", "static const uintptr_t", "[]"),
    0x0E0006E0: table.sym_var("g_hmc1_5", "static const uintptr_t", "[]"),
    0x0E000700: table.sym_var("g_hmc1_6", "static const uintptr_t", "[]"),
    0x0E000748: table.sym_var("g_hmc1_7", "static const uintptr_t", "[]"),
    0x0E000770: table.sym_var("g_hmc1_8", "static const uintptr_t", "[]"),
    0x0E000798: table.sym_var("g_hmc1_9", "static const uintptr_t", "[]"),
    0x0E0007F8: table.sym_var("g_hmc1_10", "static const uintptr_t", "[]"),
    0x0E000850: table.sym_var("g_hmc1_11", "static const uintptr_t", "[]"),
    0x0E0008D0: table.sym_var("g_hmc1_12", "static const uintptr_t", "[]"),
    0x0E000938: table.sym_var("g_hmc1_13", "static const uintptr_t", "[]"),
    0x0E000998: table.sym_var("g_hmc1_14", "static const uintptr_t", "[]"),
    0x0E000A18: table.sym_var("g_hmc1_15", "static const uintptr_t", "[]"),
    0x0E000A88: table.sym_var("g_hmc1_16", "static const uintptr_t", "[]"),
    0x0E000AE8: table.sym_var("g_hmc1_17", "static const uintptr_t", "[]"),
    0x0E000B48: table.sym_var("g_hmc1_18", "static const uintptr_t", "[]"),
    0x0E000B90: table.sym_var("g_hmc1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_ssl = {
    0x003E76B0: table.sym("szp_stage_ssl_start"),
    0x003FB990: table.sym("data_stage_ssl_start"),
    0x0E000000: table.sym("s_ssl_0E000000"),
    0x0E00001C: table.sym("s_ssl_0E00001C"),
    0x0E0000E0: table.sym("s_ssl_0E0000E0"),
    0x0E000114: table.sym("s_ssl_0E000114"),
    0x0E000268: table.sym("s_ssl_0E000268"),
    0x0E00029C: table.sym("s_ssl_0E00029C"),
    0x0E0002B8: table.sym("s_ssl", table.GLOBL),
    0x0E0005C0: table.sym_var("g_ssl_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005D8: table.sym_var("g_ssl_4", "const uintptr_t", "[]", table.GLOBL),
    0x0E000618: table.sym_var("g_ssl_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E000630: table.sym_var("g_ssl_199", "const uintptr_t", "[]", table.GLOBL),
    0x0E000648: table.sym_var("g_ssl1", "const uintptr_t", "[]", table.GLOBL),
    0x0E000734: table.sym_var("g_ssl_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000764: table.sym_var("g_ssl_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E000794: table.sym_var("g_ssl_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E0007AC: table.sym_var("g_ssl_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E0007CC: table.sym_var("g_ssl2", "const uintptr_t", "[]", table.GLOBL),
    0x0E00088C: table.sym_var("g_ssl3", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_bob = {
    0x003FC2B0: table.sym("szp_stage_bob_start"),
    0x00405A60: table.sym("data_stage_bob_start"),
    0x0E000000: table.sym("s_bob_0E000000"),
    0x0E00007C: table.sym("s_bob_0E00007C"),
    0x0E0001E8: table.sym("s_bob_0E0001E8"),
    0x0E000264: table.sym("s_bob", table.GLOBL),
    0x0E000440: table.sym_var("g_bob_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000458: table.sym_var("g_bob_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E000470: table.sym_var("g_bob_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E000488: table.sym_var("g_bob1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_sl = {
    0x00405FB0: table.sym("szp_stage_sl_start"),
    0x0040E840: table.sym("data_stage_sl_start"),
    0x0E000000: table.sym("s_sl_0E000000"),
    0x0E00004C: table.sym("s_sl_0E00004C"),
    0x0E000068: table.sym("s_sl_0E000068"),
    0x0E0000E4: table.sym("s_sl_0E0000E4"),
    0x0E000100: table.sym("s_sl", table.GLOBL),
    0x0E000360: table.sym_var("g_sl_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E000378: table.sym_var("g_sl_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E000390: table.sym_var("g_sl_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E0003A8: table.sym_var("g_sl1", "const uintptr_t", "[]", table.GLOBL),
    0x0E000484: table.sym_var("g_sl2", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_wdw = {
    0x0040ED70: table.sym("szp_stage_wdw_start"),
    0x00419F90: table.sym("data_stage_wdw_start"),
    0x0E000000: table.sym("s_wdw_0E000000"),
    0x0E0002A4: table.sym("s_wdw_0E0002A4"),
    0x0E000308: table.sym("s_wdw_0E000308"),
    0x0E00033C: table.sym("s_wdw_0E00033C"),
    0x0E000370: table.sym("s_wdw", table.GLOBL),
    0x0E000580: table.sym_var("g_wdw_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000598: table.sym_var("g_wdw_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005C0: table.sym_var("g_wdw_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005E8: table.sym_var("g_wdw_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E000610: table.sym_var("g_wdw_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E000628: table.sym_var("g_wdw_59", "const uintptr_t", "[]", table.GLOBL),
    0x0E000640: table.sym_var("g_wdw_60", "const uintptr_t", "[]", table.GLOBL),
    0x0E000658: table.sym_var("g_wdw1", "const uintptr_t", "[]", table.GLOBL),
    0x0E000724: table.sym_var("g_wdw2", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_jrb = {
    0x0041A760: table.sym("szp_stage_jrb_start"),
    0x00423B20: table.sym("data_stage_jrb_start"),
    0x0E000000: table.sym("s_jrb_0E000000"),
    0x0E0001B4: table.sym("s_jrb_0E0001B4"),
    0x0E000680: table.sym("s_jrb_0E000680"),
    0x0E0006CC: table.sym("s_jrb_0E0006CC"),
    0x0E0006E8: table.sym("s_jrb_0E0006E8"),
    0x0E0006EC: table.sym("s_jrb", table.GLOBL),
    0x0E000900: table.sym_var("g_jrb_61", "const uintptr_t", "[]", table.GLOBL),
    0x0E000918: table.sym_var("g_jrb_62", "const uintptr_t", "[]", table.GLOBL),
    0x0E000930: table.sym_var("g_jrb_59", "const uintptr_t", "[]", table.GLOBL),
    0x0E000948: table.sym_var("g_jrb_63", "const uintptr_t", "[]", table.GLOBL),
    0x0E000960: table.sym_var("g_jrb_60", "const uintptr_t", "[]", table.GLOBL),
    0x0E000978: table.sym_var("g_jrb_53", "const uintptr_t", "[]", table.GLOBL),
    0x0E000990: table.sym_var("g_jrb_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009C8: table.sym_var("g_jrb_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009B0: table.sym_var("g_jrb_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009E8: table.sym_var("g_jrb_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A00: table.sym_var("g_jrb_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A18: table.sym_var("g_jrb1", "const uintptr_t", "[]", table.GLOBL),
    0x0E000AFC: table.sym_var("g_jrb2", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_thi = {
    0x004246D0: table.sym("szp_stage_thi_start"),
    0x0042C6E0: table.sym("data_stage_thi_start"),
    0x0E000000: table.sym("s_thi_0E000000"),
    0x0E000004: table.sym("s_thi_0E000004"),
    0x0E000020: table.sym("s_thi_0E000020"),
    0x0E000054: table.sym("s_thi_0E000054"),
    0x0E000178: table.sym("s_thi_0E000178"),
    0x0E000194: table.sym("s_thi_0E000194"),
    0x0E0001C8: table.sym("s_thi_0E0001C8"),
    0x0E00022C: table.sym("s_thi_0E00022C"),
    0x0E000290: table.sym("s_thi", table.GLOBL),
    0x0E0005B0: table.sym_var("g_thi_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005C8: table.sym_var("g_thi_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005F0: table.sym_var("g_thi_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E000608: table.sym_var("g_thi1", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006D4: table.sym_var("g_thi2", "const uintptr_t", "[]", table.GLOBL),
    0x0E00079C: table.sym_var("g_thi3", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_ttc = {
    0x0042CF20: table.sym("szp_stage_ttc_start"),
    0x00437400: table.sym("data_stage_ttc_start"),
    0x0E000000: table.sym("s_ttc_0E000000"),
    0x0E000034: table.sym("s_ttc_0E000034"),
    0x0E0000C8: table.sym("s_ttc", table.GLOBL),
    0x0E000240: table.sym_var("g_ttc_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000258: table.sym_var("g_ttc_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E000270: table.sym_var("g_ttc_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E000288: table.sym_var("g_ttc_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E0002A8: table.sym_var("g_ttc_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E0002C8: table.sym_var("g_ttc_59", "const uintptr_t", "[]", table.GLOBL),
    0x0E0002E0: table.sym_var("g_ttc_60", "const uintptr_t", "[]", table.GLOBL),
    0x0E0002F8: table.sym_var("g_ttc_61", "const uintptr_t", "[]", table.GLOBL),
    0x0E000310: table.sym_var("g_ttc_62", "const uintptr_t", "[]", table.GLOBL),
    0x0E000328: table.sym_var("g_ttc_63", "const uintptr_t", "[]", table.GLOBL),
    0x0E000340: table.sym_var("g_ttc_64", "const uintptr_t", "[]", table.GLOBL),
    0x0E000358: table.sym_var("g_ttc_65", "const uintptr_t", "[]", table.GLOBL),
    0x0E000370: table.sym_var("g_ttc_66", "const uintptr_t", "[]", table.GLOBL),
    0x0E000388: table.sym_var("g_ttc_67", "const uintptr_t", "[]", table.GLOBL),
    0x0E0003A0: table.sym_var("g_ttc_68", "const uintptr_t", "[]", table.GLOBL),
    0x0E0003B8: table.sym_var("g_ttc1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_rr = {
    0x00437870: table.sym("szp_stage_rr_start"),
    0x0044A140: table.sym("data_stage_rr_start"),
    0x0E000000: table.sym("s_rr_0E000000"),
    0x0E0002EC: table.sym("s_rr_0E0002EC"),
    0x0E000368: table.sym("s_rr_0E000368"),
    0x0E0003E4: table.sym("s_rr", table.GLOBL),
    0x0E000660: table.sym_var("g_rr_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E000678: table.sym_var("g_rr_4", "const uintptr_t", "[]", table.GLOBL),
    0x0E000690: table.sym_var("g_rr_5", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006A8: table.sym_var("g_rr_6", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006C0: table.sym_var("g_rr_7", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006D8: table.sym_var("g_rr_8", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006F0: table.sym_var("g_rr_9", "const uintptr_t", "[]", table.GLOBL),
    0x0E000708: table.sym_var("g_rr_10", "const uintptr_t", "[]", table.GLOBL),
    0x0E000720: table.sym_var("g_rr_11", "const uintptr_t", "[]", table.GLOBL),
    0x0E000738: table.sym_var("g_rr_12", "const uintptr_t", "[]", table.GLOBL),
    0x0E000758: table.sym_var("g_rr_13", "const uintptr_t", "[]", table.GLOBL),
    0x0E000770: table.sym_var("g_rr_14", "const uintptr_t", "[]", table.GLOBL),
    0x0E000788: table.sym_var("g_rr_15", "const uintptr_t", "[]", table.GLOBL),
    0x0E0007A0: table.sym_var("g_rr_16", "const uintptr_t", "[]", table.GLOBL),
    0x0E0007B8: table.sym_var("g_rr_17", "const uintptr_t", "[]", table.GLOBL),
    0x0E0007D0: table.sym_var("g_rr_18", "const uintptr_t", "[]", table.GLOBL),
    0x0E0007E8: table.sym_var("g_rr_19", "const uintptr_t", "[]", table.GLOBL),
    0x0E000800: table.sym_var("g_rr_20", "const uintptr_t", "[]", table.GLOBL),
    0x0E000818: table.sym_var("g_rr_21", "const uintptr_t", "[]", table.GLOBL),
    0x0E000830: table.sym_var("g_rr_22", "const uintptr_t", "[]", table.GLOBL),
    0x0E000848: table.sym_var("g_rr_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E000860: table.sym_var("g_rr_62", "const uintptr_t", "[]", table.GLOBL),
    0x0E000878: table.sym_var("g_rr_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E000890: table.sym_var("g_rr_59", "const uintptr_t", "[]", table.GLOBL),
    0x0E0008A8: table.sym_var("g_rr_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E0008C0: table.sym_var("g_rr_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E0008D8: table.sym_var("g_rr_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E0008F0: table.sym_var("g_rr_64", "const uintptr_t", "[]", table.GLOBL),
    0x0E000908: table.sym_var("g_rr_60", "const uintptr_t", "[]", table.GLOBL),
    0x0E000920: table.sym_var("g_rr_63", "const uintptr_t", "[]", table.GLOBL),
    0x0E000940: table.sym_var("g_rr_61", "const uintptr_t", "[]", table.GLOBL),
    0x0E000958: table.sym_var("g_rr_65", "const uintptr_t", "[]", table.GLOBL),
    0x0E000970: table.sym_var("g_rr_66", "const uintptr_t", "[]", table.GLOBL),
    0x0E000988: table.sym_var("g_rr_67", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009A0: table.sym_var("g_rr_68", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009B8: table.sym_var("g_rr_69", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009D0: table.sym_var("g_rr1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_ground = {
    0x0044ABC0: table.sym("szp_stage_grounds_start"),
    0x004545E0: table.sym("data_stage_grounds_start"),
    0x0E000000: table.sym("s_grounds_0E000000"),
    0x0E00013C: table.sym("s_grounds_0E00013C"),
    0x0E000368: table.sym("s_grounds_0E000368"),
    0x0E0003CC: table.sym("s_grounds_0E0003CC", table.GLOBL),
    0x0E000508: table.sym("s_grounds", table.GLOBL),
    0x0E000660: table.sym_var("g_grounds_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006F4: table.sym_var("g_grounds_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E00070C: table.sym_var("g_grounds_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000724: table.sym_var("g_grounds_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E00073C: table.sym_var("g_grounds1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_bitdw = {
    0x00454E00: table.sym("szp_stage_bitdw_start"),
    0x0045BF60: table.sym("data_stage_bitdw_start"),
    0x0E000000: table.sym("s_bitdw_0E000000"),
    0x0E000124: table.sym("s_bitdw_0E000124"),
    0x0E000158: table.sym("s_bitdw_0E000158"),
    0x0E000174: table.sym("s_bitdw", table.GLOBL),
    0x0E0003C0: table.sym_var("g_bitdw_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E0003D8: table.sym_var("g_bitdw_4", "const uintptr_t", "[]", table.GLOBL),
    0x0E0003F0: table.sym_var("g_bitdw_5", "const uintptr_t", "[]", table.GLOBL),
    0x0E000408: table.sym_var("g_bitdw_6", "const uintptr_t", "[]", table.GLOBL),
    0x0E000420: table.sym_var("g_bitdw_7", "const uintptr_t", "[]", table.GLOBL),
    0x0E000438: table.sym_var("g_bitdw_8", "const uintptr_t", "[]", table.GLOBL),
    0x0E000450: table.sym_var("g_bitdw_9", "const uintptr_t", "[]", table.GLOBL),
    0x0E000468: table.sym_var("g_bitdw_10", "const uintptr_t", "[]", table.GLOBL),
    0x0E000480: table.sym_var("g_bitdw_11", "const uintptr_t", "[]", table.GLOBL),
    0x0E000498: table.sym_var("g_bitdw_12", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004B0: table.sym_var("g_bitdw_13", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004C8: table.sym_var("g_bitdw_14", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004E0: table.sym_var("g_bitdw_15", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004F8: table.sym_var("g_bitdw_16", "const uintptr_t", "[]", table.GLOBL),
    0x0E000510: table.sym_var("g_bitdw_17", "const uintptr_t", "[]", table.GLOBL),
    0x0E000528: table.sym_var("g_bitdw_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E000540: table.sym_var("g_bitdw_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E000558: table.sym_var("g_bitdw_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000570: table.sym_var("g_bitdw_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E000588: table.sym_var("g_bitdw_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005A0: table.sym_var("g_bitdw_59", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005B8: table.sym_var("g_bitdw_60", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005D0: table.sym_var("g_bitdw_61", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005E8: table.sym_var("g_bitdw_62", "const uintptr_t", "[]", table.GLOBL),
    0x0E000600: table.sym_var("g_bitdw_63", "const uintptr_t", "[]", table.GLOBL),
    0x0E000618: table.sym_var("g_bitdw1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_vcutm = {
    0x0045C600: table.sym("szp_stage_vcutm_start"),
    0x00461220: table.sym("data_stage_vcutm_start"),
    0x0E0000B0: table.sym("s_vcutm_0E0000B0"),
    0x0E000000: table.sym("s_vcutm_0E000000"),
    0x0E000094: table.sym("s_vcutm_0E000094"),
    0x0E0000CC: table.sym("s_vcutm", table.GLOBL),
    0x0E0001F0: table.sym_var("g_vcutm_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000208: table.sym_var("g_vcutm1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_bitfs = {
    0x004614D0: table.sym("szp_stage_bitfs_start"),
    0x0046A840: table.sym("data_stage_bitfs_start"),
    0x0E000000: table.sym("s_bitfs_0E000000"),
    0x0E0001CC: table.sym("s_bitfs_0E0001CC"),
    0x0E000218: table.sym("s_bitfs_0E000218"),
    0x0E000234: table.sym("s_bitfs", table.GLOBL),
    0x0E0004B0: table.sym_var("g_bitfs_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004C8: table.sym_var("g_bitfs_4", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004E0: table.sym_var("g_bitfs_5", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004F8: table.sym_var("g_bitfs_6", "const uintptr_t", "[]", table.GLOBL),
    0x0E000510: table.sym_var("g_bitfs_7", "const uintptr_t", "[]", table.GLOBL),
    0x0E000528: table.sym_var("g_bitfs_8", "const uintptr_t", "[]", table.GLOBL),
    0x0E000540: table.sym_var("g_bitfs_9", "const uintptr_t", "[]", table.GLOBL),
    0x0E000558: table.sym_var("g_bitfs_10", "const uintptr_t", "[]", table.GLOBL),
    0x0E000570: table.sym_var("g_bitfs_11", "const uintptr_t", "[]", table.GLOBL),
    0x0E000588: table.sym_var("g_bitfs_12", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005A0: table.sym_var("g_bitfs_13", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005B8: table.sym_var("g_bitfs_14", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005D0: table.sym_var("g_bitfs_15", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005E8: table.sym_var("g_bitfs_16", "const uintptr_t", "[]", table.GLOBL),
    0x0E000600: table.sym_var("g_bitfs_17", "const uintptr_t", "[]", table.GLOBL),
    0x0E000618: table.sym_var("g_bitfs_18", "const uintptr_t", "[]", table.GLOBL),
    0x0E000630: table.sym_var("g_bitfs_19", "const uintptr_t", "[]", table.GLOBL),
    0x0E000648: table.sym_var("g_bitfs_20", "const uintptr_t", "[]", table.GLOBL),
    0x0E000660: table.sym_var("g_bitfs_21", "const uintptr_t", "[]", table.GLOBL),
    0x0E000678: table.sym_var("g_bitfs_59", "const uintptr_t", "[]", table.GLOBL),
    0x0E000690: table.sym_var("g_bitfs_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006A8: table.sym_var("g_bitfs_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006C0: table.sym_var("g_bitfs_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006D8: table.sym_var("g_bitfs_64", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006F0: table.sym_var("g_bitfs_65", "const uintptr_t", "[]", table.GLOBL),
    0x0E000708: table.sym_var("g_bitfs_60", "const uintptr_t", "[]", table.GLOBL),
    0x0E000728: table.sym_var("g_bitfs_62", "const uintptr_t", "[]", table.GLOBL),
    0x0E000740: table.sym_var("g_bitfs_63", "const uintptr_t", "[]", table.GLOBL),
    0x0E000758: table.sym_var("g_bitfs_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000770: table.sym_var("g_bitfs_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E000788: table.sym_var("g_bitfs_61", "const uintptr_t", "[]", table.GLOBL),
    0x0E0007A0: table.sym_var("g_bitfs1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_sa = {
    0x0046B090: table.sym("szp_stage_sa_start"),
    0x0046C1A0: table.sym("data_stage_sa_start"),
    0x0E000000: table.sym("s_sa_0E000000"),
    0x0E000034: table.sym("s_sa_0E000034"),
    0x0E000050: table.sym("s_sa", table.GLOBL),
    0x0E000170: table.sym_var("g_sa1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_bits = {
    0x0046C3A0: table.sym("szp_stage_bits_start"),
    0x00477D00: table.sym("data_stage_bits_start"),
    0x0E000000: table.sym("s_bits_0E000000"),
    0x0E0001CC: table.sym("s_bits_0E0001CC"),
    0x0E0001E8: table.sym("s_bits", table.GLOBL),
    0x0E000430: table.sym_var("g_bits_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E000448: table.sym_var("g_bits_4", "const uintptr_t", "[]", table.GLOBL),
    0x0E000460: table.sym_var("g_bits_5", "const uintptr_t", "[]", table.GLOBL),
    0x0E000478: table.sym_var("g_bits_6", "const uintptr_t", "[]", table.GLOBL),
    0x0E000490: table.sym_var("g_bits_7", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004A8: table.sym_var("g_bits_8", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004C0: table.sym_var("g_bits_9", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004D8: table.sym_var("g_bits_10", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004F0: table.sym_var("g_bits_11", "const uintptr_t", "[]", table.GLOBL),
    0x0E000508: table.sym_var("g_bits_12", "const uintptr_t", "[]", table.GLOBL),
    0x0E000520: table.sym_var("g_bits_13", "const uintptr_t", "[]", table.GLOBL),
    0x0E000538: table.sym_var("g_bits_14", "const uintptr_t", "[]", table.GLOBL),
    0x0E000550: table.sym_var("g_bits_15", "const uintptr_t", "[]", table.GLOBL),
    0x0E000568: table.sym_var("g_bits_16", "const uintptr_t", "[]", table.GLOBL),
    0x0E000580: table.sym_var("g_bits_17", "const uintptr_t", "[]", table.GLOBL),
    0x0E000598: table.sym_var("g_bits_18", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005B0: table.sym_var("g_bits_19", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005C8: table.sym_var("g_bits_20", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005E0: table.sym_var("g_bits_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E0005F8: table.sym_var("g_bits_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E000610: table.sym_var("g_bits_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E000628: table.sym_var("g_bits_60", "const uintptr_t", "[]", table.GLOBL),
    0x0E000640: table.sym_var("g_bits_61", "const uintptr_t", "[]", table.GLOBL),
    0x0E000658: table.sym_var("g_bits_62", "const uintptr_t", "[]", table.GLOBL),
    0x0E000670: table.sym_var("g_bits_63", "const uintptr_t", "[]", table.GLOBL),
    0x0E000688: table.sym_var("g_bits_64", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006A0: table.sym_var("g_bits_65", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006B8: table.sym_var("g_bits_66", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006D0: table.sym_var("g_bits_67", "const uintptr_t", "[]", table.GLOBL),
    0x0E0006E8: table.sym_var("g_bits_68", "const uintptr_t", "[]", table.GLOBL),
    0x0E000700: table.sym_var("g_bits_69", "const uintptr_t", "[]", table.GLOBL),
    0x0E000718: table.sym_var("g_bits1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_lll = {
    0x004784A0: table.sym("szp_stage_lll_start"),
    0x0048C9B0: table.sym("data_stage_lll_start"),
    0x0E000000: table.sym("s_lll_0E000000"),
    0x0E000154: table.sym("s_lll_0E000154"),
    0x0E000290: table.sym("s_lll_0E000290"),
    0x0E000324: table.sym("s_lll_0E000324"),
    0x0E0004C0: table.sym("s_lll_0E0004C0"),
    0x0E0004F4: table.sym("s_lll_0E0004F4"),
    0x0E000648: table.sym("s_lll_0E000648"),
    0x0E00067C: table.sym("s_lll", table.GLOBL),
    0x0E0009E0: table.sym_var("g_lll_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009F8: table.sym_var("g_lll_4", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A10: table.sym_var("g_lll_5", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A28: table.sym_var("g_lll_6", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A40: table.sym_var("g_lll_7", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A60: table.sym_var("g_lll_8", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A78: table.sym_var("g_lll_9", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A90: table.sym_var("g_lll_10", "const uintptr_t", "[]", table.GLOBL),
    0x0E000AA8: table.sym_var("g_lll_11", "const uintptr_t", "[]", table.GLOBL),
    0x0E000AC0: table.sym_var("g_lll_12", "const uintptr_t", "[]", table.GLOBL),
    0x0E000AD8: table.sym_var("g_lll_13", "const uintptr_t", "[]", table.GLOBL),
    0x0E000AF0: table.sym_var("g_lll_14", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B08: table.sym_var("g_lll_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B20: table.sym_var("g_lll_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B38: table.sym_var("g_lll_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B50: table.sym_var("g_lll_53", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B68: table.sym_var("g_lll_59", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B80: table.sym_var("g_lll_60", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B98: table.sym_var("g_lll_61", "const uintptr_t", "[]", table.GLOBL),
    0x0E000BB0: table.sym_var("g_lll_62", "const uintptr_t", "[]", table.GLOBL),
    0x0E000BC8: table.sym_var("g_lll_63", "const uintptr_t", "[]", table.GLOBL),
    0x0E000BE0: table.sym_var("g_lll_64", "const uintptr_t", "[]", table.GLOBL),
    0x0E000BF8: table.sym_var("g_lll_65", "const uintptr_t", "[]", table.GLOBL),
    0x0E000C10: table.sym_var("g_lll_67", "const uintptr_t", "[]", table.GLOBL),
    0x0E000C30: table.sym_var("g_lll_68", "const uintptr_t", "[]", table.GLOBL),
    0x0E000C50: table.sym_var("g_lll_69", "const uintptr_t", "[]", table.GLOBL),
    0x0E000C70: table.sym_var("g_lll_70", "const uintptr_t", "[]", table.GLOBL),
    0x0E000C90: table.sym_var("g_lll_71", "const uintptr_t", "[]", table.GLOBL),
    0x0E000CB0: table.sym_var("g_lll_72", "const uintptr_t", "[]", table.GLOBL),
    0x0E000CD0: table.sym_var("g_lll_73", "const uintptr_t", "[]", table.GLOBL),
    0x0E000CF0: table.sym_var("g_lll_74", "const uintptr_t", "[]", table.GLOBL),
    0x0E000D10: table.sym_var("g_lll_75", "const uintptr_t", "[]", table.GLOBL),
    0x0E000D30: table.sym_var("g_lll_76", "const uintptr_t", "[]", table.GLOBL),
    0x0E000D50: table.sym_var("g_lll_77", "const uintptr_t", "[]", table.GLOBL),
    0x0E000D70: table.sym_var("g_lll_78", "const uintptr_t", "[]", table.GLOBL),
    0x0E000D90: table.sym_var("g_lll_79", "const uintptr_t", "[]", table.GLOBL),
    0x0E000DB0: table.sym_var("g_lll_80", "const uintptr_t", "[]", table.GLOBL),
    0x0E000DD0: table.sym_var("g_lll_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E000DE8: table.sym_var("g_lll_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E000E00: table.sym_var("g_lll1", "const uintptr_t", "[]", table.GLOBL),
    0x0E000EA8: table.sym_var("g_lll_83", "const uintptr_t", "[]", table.GLOBL),
    0x0E000EC0: table.sym_var("g_lll2", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_ddd = {
    0x0048D930: table.sym("szp_stage_ddd_start"),
    0x00495A60: table.sym("data_stage_ddd_start"),
    0x0E000000: table.sym("s_ddd_0E000000"),
    0x0E0000AC: table.sym("s_ddd_0E0000AC"),
    0x0E0000E0: table.sym("s_ddd_0E0000E0"),
    0x0E0001EC: table.sym("s_ddd_0E0001EC"),
    0x0E000208: table.sym("s_ddd_0E000208"),
    0x0E00026C: table.sym("s_ddd", table.GLOBL),
    0x0E000450: table.sym_var("g_ddd_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E000478: table.sym_var("g_ddd_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004A0: table.sym_var("g_ddd_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E0004C0: table.sym_var("g_ddd1", "const uintptr_t", "[]", table.GLOBL),
    0x0E000570: table.sym_var("g_ddd2", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_wf = {
    0x00496090: table.sym("szp_stage_wf_start"),
    0x0049DA50: table.sym("data_stage_wf_start"),
    0x0E000000: table.sym("s_wf_0E000000"),
    0x0E0000DC: table.sym("s_wf_0E0000DC"),
    0x0E000260: table.sym("s_wf_0E000260"),
    0x0E0004D4: table.sym("s_wf_0E0004D4"),
    0x0E000568: table.sym("s_wf", table.GLOBL),
    0x0E0007E0: table.sym_var("g_wf_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E000820: table.sym_var("g_wf_4", "const uintptr_t", "[]", table.GLOBL),
    0x0E000860: table.sym_var("g_wf_5", "const uintptr_t", "[]", table.GLOBL),
    0x0E000878: table.sym_var("g_wf_6", "const uintptr_t", "[]", table.GLOBL),
    0x0E000890: table.sym_var("g_wf_7", "const uintptr_t", "[]", table.GLOBL),
    0x0E0008A8: table.sym_var("g_wf_8", "const uintptr_t", "[]", table.GLOBL),
    0x0E0008E8: table.sym_var("g_wf_9", "const uintptr_t", "[]", table.GLOBL),
    0x0E000900: table.sym_var("g_wf_10", "const uintptr_t", "[]", table.GLOBL),
    0x0E000940: table.sym_var("g_wf_12", "const uintptr_t", "[]", table.GLOBL),
    0x0E000958: table.sym_var("g_wf_14", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009A0: table.sym_var("g_wf_15", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009B8: table.sym_var("g_wf_16", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009D0: table.sym_var("g_wf_17", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009E8: table.sym_var("g_wf_18", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A00: table.sym_var("g_wf_174", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A40: table.sym_var("g_wf_177", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A58: table.sym_var("g_wf_175", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A98: table.sym_var("g_wf_173", "const uintptr_t", "[]", table.GLOBL),
    0x0E000AB0: table.sym_var("g_wf_176", "const uintptr_t", "[]", table.GLOBL),
    0x0E000AC8: table.sym_var("g_wf_178", "const uintptr_t", "[]", table.GLOBL),
    0x0E000AE0: table.sym_var("g_wf_13", "const uintptr_t", "[]", table.GLOBL),
    0x0E000AF8: table.sym_var("g_wf_44", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B10: table.sym_var("g_wf_45", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B38: table.sym_var("g_wf_46", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B60: table.sym_var("g_wf_47", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B78: table.sym_var("g_wf_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B90: table.sym_var("g_wf_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E000BA8: table.sym_var("g_wf_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E000BC8: table.sym_var("g_wf_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E000BE0: table.sym_var("g_wf_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E000BF8: table.sym_var("g_wf1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_end = {
    0x0049E710: table.sym("szp_stage_end_start"),
    0x004AC4B0: table.sym("data_stage_end_start"),
    0x0E000000: table.sym("s_end", table.GLOBL),
    0x0E000050: table.sym_var("g_end1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_courty = {
    0x004AC570: table.sym("szp_stage_courtyard_start"),
    0x004AF670: table.sym("data_stage_courtyard_start"),
    0x0E000000: table.sym("s_courtyard_0E000000"),
    0x0E00004C: table.sym("s_courtyard_0E00004C"),
    0x0E000098: table.sym("s_courtyard", table.GLOBL),
    0x0E000200: table.sym_var("g_courtyard_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E000218: table.sym_var("g_courtyard1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_pss = {
    0x004AF930: table.sym("szp_stage_pss_start"),
    0x004B7F10: table.sym("data_stage_pss_start"),
    0x0E000000: table.sym("s_pss", table.GLOBL),
    0x0E000100: table.sym_var("g_pss1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_cotmc = {
    0x004B80D0: table.sym("szp_stage_cotmc_start"),
    0x004BE9E0: table.sym("data_stage_cotmc_start"),
    0x0E000000: table.sym("s_cotmc_0E000000"),
    0x0E00004C: table.sym("s_cotmc_0E00004C"),
    0x0E000068: table.sym("s_cotmc", table.GLOBL),
    0x0E0001A0: table.sym_var("g_cotmc1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_totwc = {
    0x004BEC30: table.sym("szp_stage_totwc_start"),
    0x004C2700: table.sym("data_stage_totwc_start"),
    0x0E000000: table.sym("s_totwc_0E000000"),
    0x0E00001C: table.sym("s_totwc_0E00001C"),
    0x0E000038: table.sym("s_totwc", table.GLOBL),
    0x0E000160: table.sym_var("g_totwc_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E000188: table.sym_var("g_totwc1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_bitdwa = {
    0x004C2920: table.sym("szp_stage_bitdwa_start"),
    0x004C41C0: table.sym("data_stage_bitdwa_start"),
    0x0E000000: table.sym("s_bitdwa", table.GLOBL),
    0x0E0000D0: table.sym_var("g_bitdwa1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_wmotr = {
    0x004C4320: table.sym("szp_stage_wmotr_start"),
    0x004CD930: table.sym("data_stage_wmotr_start"),
    0x0E000000: table.sym("s_wmotr_0E000000"),
    0x0E000094: table.sym("s_wmotr_0E000094"),
    0x0E0000B0: table.sym("s_wmotr", table.GLOBL),
    0x0E0001F0: table.sym_var("g_wmotr1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_bitfsa = {
    0x004CDBD0: table.sym("szp_stage_bitfsa_start"),
    0x004CE9F0: table.sym("data_stage_bitfsa_start"),
    0x0E000000: table.sym("s_bitfsa_0E000000"),
    0x0E00007C: table.sym("s_bitfsa", table.GLOBL),
    0x0E000170: table.sym_var("g_bitfsa_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000188: table.sym_var("g_bitfsa1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_bitsa = {
    0x004CEC00: table.sym("szp_stage_bitsa_start"),
    0x004D14F0: table.sym("data_stage_bitsa_start"),
    0x0E000000: table.sym("s_bitsa_0E000000"),
    0x0E00016C: table.sym("s_bitsa", table.GLOBL),
    0x0E000290: table.sym_var("g_bitsa_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E0002A8: table.sym_var("g_bitsa_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E0002C0: table.sym_var("g_bitsa_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E0002D8: table.sym_var("g_bitsa_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E0002F0: table.sym_var("g_bitsa_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E000308: table.sym_var("g_bitsa_59", "const uintptr_t", "[]", table.GLOBL),
    0x0E000320: table.sym_var("g_bitsa_60", "const uintptr_t", "[]", table.GLOBL),
    0x0E000338: table.sym_var("g_bitsa_61", "const uintptr_t", "[]", table.GLOBL),
    0x0E000350: table.sym_var("g_bitsa_62", "const uintptr_t", "[]", table.GLOBL),
    0x0E000368: table.sym_var("g_bitsa_63", "const uintptr_t", "[]", table.GLOBL),
    0x0E000380: table.sym_var("g_bitsa_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E000398: table.sym_var("g_bitsa1", "const uintptr_t", "[]", table.GLOBL),
}

sym_E0_s_ttm = {
    0x004D1910: table.sym("szp_stage_ttm_start"),
    0x004EB1F0: table.sym("data_stage_ttm_start"),
    0x0E000000: table.sym("s_ttm_0E000000"),
    0x0E00001C: table.sym("s_ttm_0E00001C"),
    0x0E0001B8: table.sym("s_ttm_0E0001B8"),
    0x0E00024C: table.sym("s_ttm_0E00024C"),
    0x0E0002B0: table.sym("s_ttm_0E0002B0"),
    0x0E000344: table.sym("s_ttm_0E000344"),
    0x0E000390: table.sym("s_ttm_0E000390"),
    0x0E000394: table.sym("s_ttm", table.GLOBL),
    0x0E000710: table.sym_var("g_ttm_54", "const uintptr_t", "[]", table.GLOBL),
    0x0E000730: table.sym_var("g_ttm_53", "const uintptr_t", "[]", table.GLOBL),
    0x0E000748: table.sym_var("g_ttm_3", "const uintptr_t", "[]", table.GLOBL),
    0x0E000778: table.sym_var("g_ttm_4", "const uintptr_t", "[]", table.GLOBL),
    0x0E0007A8: table.sym_var("g_ttm_5", "const uintptr_t", "[]", table.GLOBL),
    0x0E0007D8: table.sym_var("g_ttm_6", "const uintptr_t", "[]", table.GLOBL),
    0x0E000808: table.sym_var("g_ttm_7", "const uintptr_t", "[]", table.GLOBL),
    0x0E000830: table.sym_var("g_ttm_8", "const uintptr_t", "[]", table.GLOBL),
    0x0E000858: table.sym_var("g_ttm_9", "const uintptr_t", "[]", table.GLOBL),
    0x0E000880: table.sym_var("g_ttm_10", "const uintptr_t", "[]", table.GLOBL),
    0x0E0008A8: table.sym_var("g_ttm_11", "const uintptr_t", "[]", table.GLOBL),
    0x0E0008D0: table.sym_var("g_ttm_12", "const uintptr_t", "[]", table.GLOBL),
    0x0E0008F8: table.sym_var("g_ttm_13", "const uintptr_t", "[]", table.GLOBL),
    0x0E000920: table.sym_var("g_ttm_15", "const uintptr_t", "[]", table.GLOBL),
    0x0E000948: table.sym_var("g_ttm_16", "const uintptr_t", "[]", table.GLOBL),
    0x0E000970: table.sym_var("g_ttm_17", "const uintptr_t", "[]", table.GLOBL),
    0x0E000990: table.sym_var("g_ttm_18", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009C0: table.sym_var("g_ttm_19", "const uintptr_t", "[]", table.GLOBL),
    0x0E0009F0: table.sym_var("g_ttm_20", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A18: table.sym_var("g_ttm_21", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A40: table.sym_var("g_ttm_22", "const uintptr_t", "[]", table.GLOBL),
    0x0E000A70: table.sym_var("g_ttm1", "const uintptr_t", "[]", table.GLOBL),
    0x0E000B5C: table.sym_var("g_ttm2", "const uintptr_t", "[]", table.GLOBL),
    0x0E000BEC: table.sym_var("g_ttm3", "const uintptr_t", "[]", table.GLOBL),
    0x0E000C84: table.sym_var("g_ttm4", "const uintptr_t", "[]", table.GLOBL),
    0x0E000D14: table.sym_var("g_ttm_55", "const uintptr_t", "[]", table.GLOBL),
    0x0E000D4C: table.sym_var("g_ttm_56", "const uintptr_t", "[]", table.GLOBL),
    0x0E000D84: table.sym_var("g_ttm_57", "const uintptr_t", "[]", table.GLOBL),
    0x0E000DBC: table.sym_var("g_ttm_58", "const uintptr_t", "[]", table.GLOBL),
    0x0E000DF4: table.sym_var("g_ttm_123", "const uintptr_t", "[]", table.GLOBL),
}

table = [
    (0x00001000, 0x00001050, "E0", sym_E0_t_crt0,   {}, imm_E0_t_crt0),
    (0x000DD370, 0x000E6260, "E0", sym_E0_t_ultra,  {}, imm_E0_t_ultra),
    (0x000F0010, 0x000F4AC0, "E0", sym_E0_d_ultra,  {}, {}),
    (0x000E6260, 0x000E6330, "E0", sym_E0_t_spboot, {}, {}),
    (0x000E6330, 0x000E7290, "E0", sym_E0_t_gF3D_0, {}, {}),
    (0x000E7290, 0x000E7318, "E0", sym_E0_t_gF3D_1, {}, {}),
    (0x000E7318, 0x000E7538, "E0", sym_E0_t_gF3D_2, {}, {}),
    (0x000E7538, 0x000E76D0, "E0", sym_E0_t_gF3D_3, {}, {}),
    (0x000E76D0, 0x000E7740, "E0", sym_E0_t_gF3D_4, {}, {}),
    (0x000F4AC0, 0x000F52C0, "E0", sym_E0_d_gF3D,   {}, {}),
    (0x000E7740, 0x000E8560, "E0", sym_E0_t_aMain,  {}, {}),
    (0x000F52C0, 0x000F5580, "E0", sym_E0_d_aMain,  {}, {}),
    (0x00001050, 0x000DD370, "E0", sym_E0_t_main,   fnc_E0_t_main, {}),
    (0x000E8560, 0x000F0010, "E0", sym_E0_d_main,   {}, {}),
    (0x000F5580, 0x00102D10, "E0", sym_E0_t_main2,  {}, {}),
    (0x00102D10, 0x00108A10, "E0", sym_E0_d_main2,  {}, {}),
    (0x00108A10, 0x00114750, "E0", sym_E0_main,     {}, {}),
    (0x00114750, 0x0012A7E0, "E0", sym_E0_o_player, {}, {}),
    (0x0012A7E0, 0x00132C60, "E0", sym_E0_o_a0,     {}, {}),
    (0x00132C60, 0x00134D20, "E0", sym_E0_o_a1,     {}, {}),
    (0x00134D20, 0x0013B910, "E0", sym_E0_o_a2,     {}, {}),
    (0x0013B910, 0x00145E90, "E0", sym_E0_o_a3,     {}, {}),
    (0x00145E90, 0x001521D0, "E0", sym_E0_o_a4,     {}, {}),
    (0x001521D0, 0x00160670, "E0", sym_E0_o_a5,     {}, {}),
    (0x00160670, 0x00165A50, "E0", sym_E0_o_a6,     {}, {}),
    (0x00165A50, 0x00166C60, "E0", sym_E0_o_a7,     {}, {}),
    (0x00166C60, 0x0016D870, "E0", sym_E0_o_a8,     {}, {}),
    (0x0016D870, 0x00180BB0, "E0", sym_E0_o_a9,     {}, {}),
    (0x00180BB0, 0x00188440, "E0", sym_E0_o_a10,    {}, {}),
    (0x00188440, 0x001B9CC0, "E0", sym_E0_o_b0,     {}, {}),
    (0x001B9CC0, 0x001C4230, "E0", sym_E0_o_b1,     {}, {}),
    (0x001C4230, 0x001D8310, "E0", sym_E0_o_b2,     {}, {}),
    (0x001D8310, 0x001E51F0, "E0", sym_E0_o_b3,     {}, {}),
    (0x001E51F0, 0x001E7EE0, "E0", sym_E0_o_b4,     {}, {}),
    (0x001E7EE0, 0x001F2200, "E0", sym_E0_o_b5,     {}, {}),
    (0x001F2200, 0x00201410, "E0", sym_E0_o_c0,     {}, {}),
    (0x00201410, 0x00219E00, "E0", sym_E0_o_entity, {}, {}),
    (0x00219E00, 0x0021F4C0, "E0", sym_E0_object,   {}, {}),
    (0x0021F4C0, 0x00257CF0, "E0", sym_E0_t_menu,   {}, {}),
    (0x00257CF0, 0x00269EA0, "E0", sym_E0_d_menu,   {}, {}),
    (0x00269EA0, 0x002A6120, "E0", sym_E0_s_title,  {}, {}),
    (0x002A6120, 0x002ABCA0, "E0", sym_E0_s_menu,   {}, {}),
    (0x002ABCA0, 0x002AC6B0, "E0", sym_E0_game,     fnc_E0_game, {}),
    (0x002AC6B0, 0x0031E1D0, "E0", sym_E0_bg,       {}, {}),
    (0x0031E1D0, 0x0036F530, "E0", sym_E0_texture,  {}, {}),
    (0x0036F530, 0x00371C40, "E0", sym_E0_particle, {}, {}),
    (0x00371C40, 0x00383950, "E0", sym_E0_s_bbh,    {}, {}),
    (0x00383950, 0x00396340, "E0", sym_E0_s_ccm,    {}, {}),
    (0x00396340, 0x003D0DC0, "E0", sym_E0_s_inside, {}, {}),
    (0x003D0DC0, 0x003E76B0, "E0", sym_E0_s_hmc,    {}, {}),
    (0x003E76B0, 0x003FC2B0, "E0", sym_E0_s_ssl,    {}, {}),
    (0x003FC2B0, 0x00405FB0, "E0", sym_E0_s_bob,    {}, {}),
    (0x00405FB0, 0x0040ED70, "E0", sym_E0_s_sl,     {}, {}),
    (0x0040ED70, 0x0041A760, "E0", sym_E0_s_wdw,    {}, {}),
    (0x0041A760, 0x004246D0, "E0", sym_E0_s_jrb,    {}, {}),
    (0x004246D0, 0x0042CF20, "E0", sym_E0_s_thi,    {}, {}),
    (0x0042CF20, 0x00437870, "E0", sym_E0_s_ttc,    {}, {}),
    (0x00437870, 0x0044ABC0, "E0", sym_E0_s_rr,     {}, {}),
    (0x0044ABC0, 0x00454E00, "E0", sym_E0_s_ground, {}, {}),
    (0x00454E00, 0x0045C600, "E0", sym_E0_s_bitdw,  {}, {}),
    (0x0045C600, 0x004614D0, "E0", sym_E0_s_vcutm,  {}, {}),
    (0x004614D0, 0x0046B090, "E0", sym_E0_s_bitfs,  {}, {}),
    (0x0046B090, 0x0046C3A0, "E0", sym_E0_s_sa,     {}, {}),
    (0x0046C3A0, 0x004784A0, "E0", sym_E0_s_bits,   {}, {}),
    (0x004784A0, 0x0048D930, "E0", sym_E0_s_lll,    {}, {}),
    (0x0048D930, 0x00496090, "E0", sym_E0_s_ddd,    {}, {}),
    (0x00496090, 0x0049E710, "E0", sym_E0_s_wf,     {}, {}),
    (0x0049E710, 0x004AC570, "E0", sym_E0_s_end,    {}, {}),
    (0x004AC570, 0x004AF930, "E0", sym_E0_s_courty, {}, {}),
    (0x004AF930, 0x004B80D0, "E0", sym_E0_s_pss,    {}, {}),
    (0x004B80D0, 0x004BEC30, "E0", sym_E0_s_cotmc,  {}, {}),
    (0x004BEC30, 0x004C2920, "E0", sym_E0_s_totwc,  {}, {}),
    (0x004C2920, 0x004C4320, "E0", sym_E0_s_bitdwa, {}, {}),
    (0x004C4320, 0x004CDBD0, "E0", sym_E0_s_wmotr,  {}, {}),
    (0x004CDBD0, 0x004CEC00, "E0", sym_E0_s_bitfsa, {}, {}),
    (0x004CEC00, 0x004D1910, "E0", sym_E0_s_bitsa,  {}, {}),
    (0x004D1910, 0x004EC000, "E0", sym_E0_s_ttm,    {}, {}),
]

msg_table = [
    "MSG_0",
    "MSG_1",
    "MSG_2",
    "MSG_3",
    "MSG_4",
    "MSG_5",
    "MSG_6",
    "MSG_7",
    "MSG_8",
    "MSG_9",
    "MSG_10",
    "MSG_11",
    "MSG_12",
    "MSG_13",
    "MSG_14",
    "MSG_15",
    "MSG_16",
    "MSG_17",
    "MSG_18",
    "MSG_19",
    "MSG_20",
    "MSG_21",
    "MSG_22",
    "MSG_23",
    "MSG_24",
    "MSG_25",
    "MSG_26",
    "MSG_27",
    "MSG_28",
    "MSG_29",
    "MSG_30",
    "MSG_31",
    "MSG_32",
    "MSG_33",
    "MSG_34",
    "MSG_35",
    "MSG_36",
    "MSG_37",
    "MSG_38",
    "MSG_39",
    "MSG_40",
    "MSG_41",
    "MSG_42",
    "MSG_43",
    "MSG_44",
    "MSG_45",
    "MSG_46",
    "MSG_47",
    "MSG_48",
    "MSG_49",
    "MSG_50",
    "MSG_51",
    "MSG_52",
    "MSG_53",
    "MSG_54",
    "MSG_55",
    "MSG_56",
    "MSG_57",
    "MSG_58",
    "MSG_59",
    "MSG_60",
    "MSG_61",
    "MSG_62",
    "MSG_63",
    "MSG_64",
    "MSG_65",
    "MSG_66",
    "MSG_67",
    "MSG_68",
    "MSG_69",
    "MSG_70",
    "MSG_71",
    "MSG_72",
    "MSG_73",
    "MSG_74",
    "MSG_75",
    "MSG_76",
    "MSG_77",
    "MSG_78",
    "MSG_79",
    "MSG_80",
    "MSG_81",
    "MSG_82",
    "MSG_83",
    "MSG_84",
    "MSG_85",
    "MSG_86",
    "MSG_87",
    "MSG_88",
    "MSG_89",
    "MSG_90",
    "MSG_91",
    "MSG_92",
    "MSG_93",
    "MSG_94",
    "MSG_95",
    "MSG_96",
    "MSG_97",
    "MSG_98",
    "MSG_99",
    "MSG_100",
    "MSG_101",
    "MSG_102",
    "MSG_103",
    "MSG_104",
    "MSG_105",
    "MSG_106",
    "MSG_107",
    "MSG_108",
    "MSG_109",
    "MSG_110",
    "MSG_111",
    "MSG_112",
    "MSG_113",
    "MSG_114",
    "MSG_115",
    "MSG_116",
    "MSG_117",
    "MSG_118",
    "MSG_119",
    "MSG_120",
    "MSG_121",
    "MSG_122",
    "MSG_123",
    "MSG_124",
    "MSG_125",
    "MSG_126",
    "MSG_127",
    "MSG_128",
    "MSG_129",
    "MSG_130",
    "MSG_131",
    "MSG_132",
    "MSG_133",
    "MSG_134",
    "MSG_135",
    "MSG_136",
    "MSG_137",
    "MSG_138",
    "MSG_139",
    "MSG_140",
    "MSG_141",
    "MSG_142",
    "MSG_143",
    "MSG_144",
    "MSG_145",
    "MSG_146",
    "MSG_147",
    "MSG_148",
    "MSG_149",
    "MSG_150",
    "MSG_151",
    "MSG_152",
    "MSG_153",
    "MSG_154",
    "MSG_155",
    "MSG_156",
    "MSG_157",
    "MSG_158",
    "MSG_159",
    "MSG_160",
    "MSG_161",
    "MSG_162",
    "MSG_163",
    "MSG_164",
    "MSG_165",
    "MSG_166",
    "MSG_167",
    "MSG_168",
    "MSG_169",
]

msg_course = [
    "COURSE_BOB; 1",
    "COURSE_WF",
    "COURSE_JRB",
    "COURSE_CCM",
    "COURSE_BBH",
    "COURSE_HMC",
    "COURSE_LLL",
    "COURSE_SSL",
    "COURSE_DDD",
    "COURSE_SL",
    "COURSE_WDW",
    "COURSE_TTM",
    "COURSE_THI",
    "COURSE_TTC",
    "COURSE_RR",
    "COURSE_BITDW",
    "COURSE_BITFS",
    "COURSE_BITS",
    "COURSE_PSS",
    "COURSE_COTMC",
    "COURSE_TOTWC",
    "COURSE_VCUTM",
    "COURSE_WMOTR",
    "COURSE_SA",
    "COURSE_END",
    None,
]

str_code_u = """
#include <ultra64.h>

.set noreorder
.set noat
"""

str_code_d = str_code_u + ".set gp = 64\n"

str_data_u = """
#include <ultra64.h>

"""

str_ucode_text = """
.include "PR/rsp.inc"
.create "build/PR/%s.text.bin", 0x%08X

"""

str_ucode_base = """

.base %s
"""

str_ucode_data = """

.close

.create "build/PR/%s.data.bin", 0

"""

str_ucode_end = """

.close
"""

str_code = """
#include <ultra64.h>

#include <sm64.h>

.set noreorder
.set noat
"""

str_data = """
#include <ultra64.h>

#include <sm64.h>

"""

str_gfx = """
#include <ultra64.h>

#include <sm64.h>
#include <sm64/gbi_ext.h>

"""

str_g_script = """
#include <ultra64.h>

#include <sm64.h>
#include <sm64/g_script.h>

#define _SCRIPT

"""

str_s_script = """
#include <ultra64.h>

#include <sm64.h>
#include <sm64/s_script.h>

"""

str_o_script = """
#include <ultra64.h>

#include <sm64.h>
#include <sm64/o_script.h>

#define _SCRIPT

"""

def szp_decode(src):
    sig, size, ci, di = struct.unpack(">4sIII", src[:0x10])
    ti  = 0x10
    dst = B""
    bit = 0
    bi  = 0
    while len(dst) < size:
        if bi == 0:
            bit, = struct.unpack(">I", src[ti:ti+4])
            ti += 4
            bi = 32
        if bit & 0x80000000:
            dst += src[di:di+1]
            di += 1
        else:
            so, = struct.unpack(">H", src[ci:ci+2])
            ci += 2
            of = len(dst) - ((so & 0x0FFF) + 1)
            sz = (so >> 12) + 3
            dst += (sz*dst[of:of+sz])[:sz]
        bit <<= 1
        bi -= 1
    return dst

def s_szp(self, argv):
    start, end, data = argv
    fn = ".cache/UNSM%s_%08X.bin" % (data, start)
    if os.path.isfile(fn):
        with open(fn, "rb") as f:
            self.data[data+".szp"] = f.read()
    else:
        self.data[data+".szp"] = szp_decode(self.data[data][start:end])
        with open(fn, "wb") as f:
            f.write(self.data[data+".szp"])
    self.dev = start

def s_szpbin(start, end, size, name):
    return [main.s_call, [
        [s_szp, start, end, "E0"],
        [main.s_bin, 0, size, "E0.szp", ["%s.bin" % name]],
        [main.s_dev, None],
    ]]

def s_msg_str(self, lang, line):
    lst = []
    while True:
        x = ultra.ub()
        if x == 0xFF:
            break
        lst.append(x)
    i = 0
    while i < len(lst):
        for s, c in lang:
            n = len(c)
            if lst[i:i+n] == c:
                line.append(s)
                i += n
                break
        else:
            raise RuntimeError("illegal character 0x%02X" % lst[i])
    if not line[-1].endswith("\n"):
        line.append("\n")
    self.c_addr = (self.c_addr+3) & ~3

def s_msg(self, argv):
    start, end, data, lang, m, name, table = argv
    ultra.init(self, start, data)
    line = ["$lang: %s\n" % lang]
    i = 0
    lang = UNSM.exe.lang.table[lang]
    while self.c_addr < end:
        if m == 0:
            cmd, arg = "str", []
        else:
            x = ultra.uw()
            if x == 0:
                break
            addr = self.c_addr
            self.c_addr = x
            if m == 1:
                cmd, arg = "tbl", []
            else:
                arg = ultra.sw()
                ln  = ultra.sb()
                self.c_addr += 1
                x   = ultra.sh()
                y   = ultra.sh()
                self.c_addr += 2
                self.c_addr = ultra.uw()
                cmd, arg = "msg", ["%d, %d, %d, %d" % (arg, ln, x, y)]
        if table != None and table[i] != None:
            arg.append(table[i])
        i += 1
        line.append("\n$%s:" % cmd)
        if len(arg) > 0:
            line.append(" " + "; ".join(arg))
        line.append("\n")
        s_msg_str(self, lang, line)
        if m != 0:
            self.c_addr = addr
    data = "".join(line)
    fn = self.path_join([name + ".txt"])
    main.mkdir(fn)
    with open(fn, "w") as f:
        f.write(data)
    self.file[-1][1].append(
        "#include ASSET(%s.h)\n" % self.path_join([name], 1)
    )

def s_dirfile(path, fn):
    if path != None:
        return [main.s_call, [
            [main.s_dir, path],
            [main.s_str, "#include \"%s/%s\"\n" % (path, fn)],
            [main.s_file, fn],
        ]]
    return [main.s_call, [
        [main.s_str, "#include \"%s\"\n" % fn],
        [main.s_file, fn],
    ]]

def s_writepop():
    return [main.s_call, [
        [main.s_write],
        [main.s_pop],
    ]]

def s_gfx_ifndef():
    return [main.s_str, "\n\n#ifndef _SCRIPT\n\n"]

def s_gfx_else():
    return [main.s_str, "\n\n#else\n\n"]

def s_gfx_endif():
    return [main.s_str, "\n\n#endif\n\n"]

def s_code(start, end, fn, s=str_code, sep=False):
    return [main.s_call, [
        [main.s_file, "%s.S" % fn],
            [main.s_str, s],
            [ultra.asm.s_code, start, end, "E0", 0, sep],
        [main.s_write],
    ]]

def s_data(start, end, fn, lst, s=str_data):
    return [main.s_call, [
        [main.s_file, "%s.c" % fn],
            [main.s_str, s],
            [ultra.c.s_data, start, end, "E0", lst],
        [main.s_write],
    ]]

def s_databin(start, end, name):
    end = (end+0x0F) & ~0x0F
    return [main.s_bin, start, end, "E0", ["%s.bin" % name]]

def s_objectbin(start, end, size, gsize, b, name):
    return [main.s_call, [
        [main.s_dir, name],
            s_szpbin(start, end, size, "gfx"),
            [main.s_addr, (b << 24) - end],
            [main.s_file, "g.c"],
                [main.s_str, str_g_script],
                [UNSM.c.s_script_g, b << 24, (b << 24) + gsize, "E0"],
            [main.s_write],
            [main.s_addr, 0],
        [main.s_pop],
    ]]

def s_object(start, end, a, b, name, gfx, g):
    return [main.s_call, [
        [main.s_dir, name],
            [s_szp, start, end, "E0"],
            [main.s_addr, (a << 24)],
            [main.s_file, "gfx.c"],
                [main.s_str, str_gfx],
                [main.s_call, gfx],
            [main.s_write],
            [main.s_dev, None],
            [main.s_addr, (b << 24) - end],
            [main.s_file, "g.c"],
                [main.s_str, str_g_script],
                [main.s_call, g],
            [main.s_write],
            [main.s_addr, 0],
        [main.s_pop],
    ]]

def s_script(start, end, addr, size):
    s_start = addr
    s_end   = addr + size
    g_start = (s_end+0x0F) & ~0x0F
    g_end   = addr + end-start
    return [main.s_call, [
        [main.s_addr, addr-start],
        [main.s_file, "s.S"],
            [main.s_str, str_s_script],
            [UNSM.asm.s_script, s_start, s_end, "E0", 0],
        [main.s_write],
        [main.s_file, "g.c"],
            [main.s_str, str_g_script],
            [UNSM.c.s_script_g, g_start, g_end, "E0"],
        [main.s_write],
        [main.s_addr, 0],
    ]]

def s_texture(start, end, size, a, name, lst):
    return [main.s_call, [
        [main.s_dir, name],
            [s_szp, start, end, "E0"],
            [main.s_addr, (a << 24)],
            [main.s_file, "gfx.c"],
                [main.s_str, str_data],
                [ultra.c.s_data, (a << 24), (a << 24) + size, "E0.szp", lst],
            [main.s_write],
            [main.s_dev, None],
            [main.s_addr, 0],
        [main.s_pop],
    ]]

def s_stagebin(a, b, c, size, g, name):
    return [main.s_call, [
        [main.s_dir, name],
            s_szpbin(a, b, size, "gfx"),
            s_script(b, c, 0x0E000000, g),
        [main.s_pop],
    ]]

def d_prg_prc():
    src = ultra.uw()
    siz = ultra.uh()+1
    dst = ultra.uh()
    return ".dw 0x%08X :: .dh 0x%04X-1, 0x%04X" % (src, siz, dst)
d_prg = ["", d_prg_prc]

def d_light_prc(argv):
    a, = argv
    a = ultra.fmt_float(a, "F")
    ultra.script.c_addr += 8
    r = ultra.ub()
    g = ultra.ub()
    b = ultra.ub()
    ultra.script.c_addr += 13
    return ["gdSPDefLight(%s, 0x%02X, 0x%02X, 0x%02X)" % (a, r, g, b)]
d_light = [False, d_light_prc]

def d_matrix_prc(argv):
    h = [ultra.sh() for i in range(16)]
    l = [ultra.uh() for i in range(16)]
    return ["gdSPDefMatrix("] + ["\t" + " ".join([
        ultra.fmt_float(
            float(h[i] << 16 | l[i]) / 0x10000, "F", len(argv) == 0
        ) + ("," if i != 15 else "") for i in range(i, i+4)
    ]) for i in range(0, 16, 4)] + [")"]
d_matrix = [False, d_matrix_prc]

def s_shape_vtx(self, argv):
    name, = argv
    self.file[-1][1].append(
        "#include ASSET(%s.vtx.h)\n" % ultra.script.path_join([name], 1)
    )

def d_shape_gfx_prc(argv):
    end, name, light, scale = argv
    alpha = False
    vtx = []
    tri = []
    buf = 16*[None]
    while ultra.script.c_addr < end:
        w0 = ultra.uw()
        w1 = ultra.uw()
        cmd = w0 >> 24
        if cmd == 0x04:
            addr = ultra.script.c_addr
            ultra.script.c_addr = w1
            e = w1 + (w0 & 0xFFFF)
            i = w0 >> 16 & 0x0F
            while ultra.script.c_addr < e:
                x = ultra.sh()
                y = ultra.sh()
                z = ultra.sh()
                ultra.script.c_addr += 2
                s = ultra.sh()
                t = ultra.sh()
                if light:
                    r = ultra.sb()
                    g = ultra.sb()
                    b = ultra.sb()
                else:
                    r = ultra.ub()
                    g = ultra.ub()
                    b = ultra.ub()
                a = ultra.ub()
                buf[i] = (x, y, z, s, t, r, g, b, a)
                i += 1
            ultra.script.c_addr = addr
        elif cmd == 0xBF:
            t = (
                (w1 >> 16 & 0xFF) // 10,
                (w1 >>  8 & 0xFF) // 10,
                (w1       & 0xFF) // 10,
            )
            b = []
            for v in t:
                if buf[v] in vtx:
                    b.append(vtx.index(buf[v]))
                else:
                    b.append(len(vtx))
                    vtx.append(buf[v])
                    if vtx[-1][8] != 0:
                        alpha = True
            tri.append(tuple(b))
        else:
            raise RuntimeError("bad shape gfx 0x%08X : %08X %08X" % (
                ultra.script.c_addr-8, w0, w1
            ))
    path = ultra.script.path_join([name])
    data = ""
    if scale != None:
        w = scale[0]
        h = scale[1]
        s = scale[2] if len(scale) > 2 else 1
        t = scale[3] if len(scale) > 3 else -0.5
        if type(s) == tuple:
            ss, st = s
        else:
            ss = st = s
        if type(t) == tuple:
            ts, tt = t
        else:
            ts = tt = t
        scale = (float(w)/ss, float(h)/st, ts, tt)
        data += "t=%s,%s,%s,%s\n" % tuple([ultra.fmt_float(x) for x in scale])
    if not light or alpha:
        data += "s=%s,%s\n" % (
            "x,y,z" if light else "r,g,b",
            "a"     if alpha else "0",
        )
    if len(data) > 0:
        fn = path + ".ini"
        with open(fn, "w") as f:
            f.write(data)
    data = (
        "ply\n"
        "format ascii 1.0\n"
        "comment metarep (UNSM) - %s_%s\n"
        "element vertex %d\n"
        "property short x\n"
        "property short y\n"
        "property short z\n"
    ) % (ultra.script.path[-1], name, len(vtx))
    if scale != None:
        data += (
            "property float s\n"
            "property float t\n"
        )
    if light:
        data += (
            "property float nx\n"
            "property float ny\n"
            "property float nz\n"
        )
    else:
        data += (
            "property uchar red\n"
            "property uchar green\n"
            "property uchar blue\n"
        )
    if alpha:
        data += (
            "property uchar alpha\n"
        )
    data += (
        "element face %d\n"
        "property list uchar uint vertex_indices\n"
        "end_header\n"
    ) % len(tri)
    for v in vtx:
        data += "%d %d %d" % v[:3]
        if scale != None:
            s = (v[3]/32.0 - scale[2]) / scale[0]
            t = (v[4]/32.0 - scale[3]) / scale[1]
            data += " %s %s" % (str(s), str(1.0-t))
        if light:
            nx = v[5]/128.0
            ny = v[6]/128.0
            nz = v[7]/128.0
            data += " %s %s %s" % (str(nx), str(ny), str(nz))
        else:
            data += " %d %d %d" % v[5:8]
        if alpha:
            data += " %d" % v[8]
        data += "\n"
    data += "".join(["3 %d %d %d\n" % t for t in tri])
    fn = path + ".ply"
    main.mkdir(fn)
    with open(fn, "w") as f:
        f.write(data)
    return ["#include ASSET(%s.h)" % ultra.script.path_join([name], 1)]
d_shape_gfx = [False, d_shape_gfx_prc]

def d_ripple_0_prc(argv):
    n = ultra.sh()
    lst = ["%d," % n]
    for _ in range(n):
        x = ultra.sh()
        y = ultra.sh()
        z = ultra.sh()
        lst.append("\t%d, %d, %d," % (x, y, z))
    return lst
d_ripple_0 = [False, d_ripple_0_prc]

def d_ripple_1_prc(argv):
    end, = argv
    lst = []
    while ultra.script.c_addr < end:
        n = ultra.sh()
        f = [n] + [ultra.sh() for _ in range(n)]
        lst.append("\t" + " ".join(["%d," % x for x in f]))
    lst[0] = lst[0][1:]
    return lst
d_ripple_1 = [False, d_ripple_1_prc]

def g_movemem(argv):
    a_0  = ultra.uw()
    a_1  = ultra.uw()
    d0_0 = ultra.uw()
    d0_1 = ultra.uw()
    if a_0 == 0x03860010 and d0_0 == 0x03880010 and a_1-d0_1 == 8:
        light = ultra.sym(d0_1)
        return ("SPSetLights1N", light)
    return None

def g_tri1(argv):
    w0_0 = ultra.uw()
    w1_0 = ultra.uw()
    w0_1 = ultra.uw()
    w1_1 = ultra.uw()
    if w0_0 == 0xBF000000 and w0_1 == 0xBF000000:
        v00 = "%2d" % ((w1_0 >> 16 & 0xFF) // 10)
        v01 = "%2d" % ((w1_0 >>  8 & 0xFF) // 10)
        v02 = "%2d" % ((w1_0 >>  0 & 0xFF) // 10)
        flag0 = "%d" % (w1_0 >> 24)
        v10 = "%2d" % ((w1_1 >> 16 & 0xFF) // 10)
        v11 = "%2d" % ((w1_1 >>  8 & 0xFF) // 10)
        v12 = "%2d" % ((w1_1 >>  0 & 0xFF) // 10)
        flag1 = "%d" % (w1_1 >> 24)
        return ("SP2Triangles", v00, v01, v02, flag0, v10, v11, v12, flag1)
    return None

def g_texture(argv):
    w0 = ultra.uw()
    w1 = ultra.uw()
    s = (w1 >> 16) // 62
    t = (w1 & 0xFFFF) // 62
    for x in (s, t):
        if x == 0 or (x & ~(1 << x.bit_length()-1)) != 0:
            return None
    s = "62*%d" % s
    t = "62*%d" % t
    return ultra.c.g_texture_prc(s, t, w0)

def g_loadimageblock(cmd, timg, fmt, siz, width, w):
    tile, uls, ult, lrs, dxt = ultra.c.gx_tile(w[0], w[1])
    if (width, tile, uls, ult) != (1, 7, 0, 0):
        return None
    width  = 0x800*(1,2,4,8)[siz] // dxt
    height = ((lrs+1) << (2,1,0,0)[siz]) // width
    timg   = ultra.sym(timg)
    fmt    = ultra.c.g_im_fmt[fmt]
    siz    = ultra.c.g_im_siz(siz)
    width  = "%d" % width
    height = "%d" % height
    return (cmd, timg, fmt, siz, width, height)

def g_settimg(argv):
    w = [(ultra.uw(), ultra.uw()) for _ in range(3)]
    fmt, siz, width, timg = ultra.c.gx_settimg(w[0][0], w[0][1])
    if tuple([x[0] >> 24 for x in w]) == (0xFD, 0xE6, 0xF3):
        return g_loadimageblock("DPLoadImageBlock", timg, fmt, siz, width, w[2])
    w += [(ultra.uw(), ultra.uw()) for _ in range(2)]
    c = tuple([x[0] >> 24 for x in w])
    if tuple([x[0] >> 24 for x in w]) == (0xFD, 0xE8, 0xF5, 0xE6, 0xF3):
        if ultra.c.gx_settile(w[2][0], w[2][1]) == (
            fmt, siz, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0
        ):
            return g_loadimageblock(
                "DPLoadImageBlockT", timg, fmt, siz, width, w[4]
            )
    return None

def g_rdptilesync(argv):
    w = [(ultra.uw(), ultra.uw()) for _ in range(3)]
    if tuple([x[0] >> 24 for x in w]) == (0xE8, 0xF5, 0xF2):
        fmt, siz, line, tmem, c1_tile, pal, cmt, maskt, shiftt, cms, masks, \
            shifts = ultra.c.gx_settile(w[1][0], w[1][1])
        c2_tile, uls, ult, lrs, lrt = ultra.c.gx_tile(w[2][0], w[2][1])
        width  = (lrs >> 2) + 1
        height = (lrt >> 2) + 1
        if (line, tmem, c1_tile, c2_tile, uls, ult, lrs, lrt) == (
            ultra.c.g_calc_line(width, siz), 0, 0,
            0, 0, 0, (width-1) << 2, (height-1) << 2
        ):
            fmt     = ultra.c.g_im_fmt[fmt]
            siz     = ultra.c.g_im_siz(siz)
            width   = "%d" % width
            height  = "%d" % height
            pal     = "%d" % pal
            cms     = ultra.c.g_tx_cm(cms)
            cmt     = ultra.c.g_tx_cm(cmt)
            masks   = ultra.c.g_tx_mask(masks)
            maskt   = ultra.c.g_tx_mask(maskt)
            shifts  = ultra.c.g_tx_lod(shifts)
            shiftt  = ultra.c.g_tx_lod(shiftt)
            return ("DPSetImageBlock",
                fmt, siz, width, height, pal, None,
                cms, cmt, masks, maskt, shifts, shiftt
            )
    return None

g_cc_env        = ("0", "0", "0", "ENVIRONMENT")
g_cc_t0_en      = ("TEXEL0", "0", "ENVIRONMENT", "0")
g_cc_sh_en      = ("SHADE", "0", "ENVIRONMENT", "0")

g_setcombine_mode = {
    ultra.c.g_cc_shade      + g_cc_env:     "G_CC_SHADE_ENV",
    ultra.c.g_cc_texel0     + g_cc_env:     "G_CC_DECALRGB_ENV",
    ultra.c.g_cc_texel0     + g_cc_t0_en:   "G_CC_DECALRGBA_ENV",
    ultra.c.g_cc_t0_sh_t0a  + g_cc_env:     "G_CC_BLENDRGB_ENVA",
    ultra.c.g_cc_t0_sh      + g_cc_env:     "G_CC_MODULATERGB_ENVA",
    ultra.c.g_cc_t0_sh      + g_cc_t0_en:   "G_CC_MODULATERGBA_ENVA",
    g_cc_t0_en  + g_cc_t0_en:   "G_CC_MODULATERGBA_ENV",
    g_cc_sh_en  + g_cc_sh_en:   "G_CC_MODULATESE",
}

def g_setcombine(argv):
    x = ultra.c.g_setcombine_prc(g_setcombine_mode)
    if len(x) == 3:
        return x
    return None

def g_settile(argv):
    w = [(ultra.uw(), ultra.uw()) for _ in range(5)]
    c = tuple([x[0] >> 24 for x in w])
    if c == (0xF5, 0xE6, 0xF3, 0xF5, 0xF2):
        c0_fmt, c0_siz, c0_line, c0_tmem, c0_tile, c0_palette, c0_cmt, \
            c0_maskt, c0_shiftt, c0_cms, c0_masks, c0_shifts = \
            ultra.c.gx_settile(w[0][0], w[0][1])
        c2_tile, c2_uls, c2_ult, c2_lrs, c2_dxt = \
            ultra.c.gx_tile(w[2][0], w[2][1])
        c3_fmt, c3_siz, c3_line, c3_tmem, c3_tile, c3_palette, c3_cmt, \
            c3_maskt, c3_shiftt, c3_cms, c3_masks, c3_shifts = \
            ultra.c.gx_settile(w[3][0], w[3][1])
        c4_t, c4_uls, c4_ult, c4_lrs, c4_lrt = ultra.c.gx_tile(w[4][0], w[4][1])
        fmt     = c3_fmt
        siz     = c3_siz
        width   = (c4_lrs >> 2) + 1
        height  = (c4_lrt >> 2) + 1
        pal     = c3_palette
        cms     = c3_cms
        cmt     = c3_cmt
        masks   = c3_masks
        maskt   = c3_maskt
        shifts  = c3_shifts
        shiftt  = c3_shiftt
        if (
            c0_fmt, c0_siz, c0_line, c0_tmem, c0_tile, c0_palette,
            c0_cmt, c0_maskt, c0_shiftt, c0_cms, c0_masks, c0_shifts,
            c2_tile, c2_uls, c2_ult, c2_lrs, c2_dxt,
            c3_fmt, c3_siz, c3_line, c3_tmem, c3_tile, c3_palette,
            c3_cmt, c3_maskt, c3_shiftt, c3_cms, c3_masks, c3_shifts,
            c4_t, c4_uls, c4_ult, c4_lrs, c4_lrt,
        ) == (
            fmt, (2,2,2,3)[siz], 0, 0, 7, 0,
            cmt, maskt, shiftt, cms, masks, shifts,
            7, 0, 0, ultra.c.g_calc_lrs(width, height, siz),
            ultra.c.g_calc_dxt(width, siz),
            fmt, siz, ultra.c.g_calc_line(width, siz), 0, 0, pal,
            cmt, maskt, shiftt, cms, masks, shifts,
            0, 0, 0, (width-1) << 2, (height-1) << 2,
        ):
            fmt     = ultra.c.g_im_fmt[fmt]
            width   = "%d" % width
            height  = "%d" % height
            pal     = "%d" % pal
            cms     = ultra.c.g_tx_cm(cms)
            cmt     = ultra.c.g_tx_cm(cmt)
            masks   = ultra.c.g_tx_mask(masks)
            maskt   = ultra.c.g_tx_mask(maskt)
            shifts  = ultra.c.g_tx_lod(shifts)
            shiftt  = ultra.c.g_tx_lod(shiftt)
            arg = (
                width, height, pal, None,
                cms, cmt, None,
                masks, maskt, shifts, shiftt,
            )
            if siz == 0:
                return ("DPLoadTextureBlock_4bN", fmt) + arg
            siz = ultra.c.g_im_siz(siz)
            return ("DPLoadTextureBlockN", fmt, siz) + arg
    return None

gfx_table = {
    0x03: (g_movemem,),
    0xBF: (g_tri1,),
    0xBB: (g_texture,),
    0xFD: (g_settimg,),
    0xFC: (g_setcombine,),
    0xF5: (g_settile,),
    0xE8: (g_rdptilesync,),
}

def s_shape(start, gfx, end, name, light=False, scale=None):
    return [main.s_call, [
        [s_shape_vtx, name],
        [ultra.c.s_data, start, end, "E0.szp", [
            [0, 1, 1, d_shape_gfx, gfx, name, light, scale],
            [0, 1, 1, ultra.c.d_Gfx, end],
        ]],
    ]]

def d_texture_n(t, w, h, end, fmt="%d", start=0, step=1):
    return [0, 1, [
        [0, 1, 1, ultra.c.d_texture, t, w, h, fmt % i]
        for i in range(start, end, step)
    ]]

ultra_src = [
    s_code(0x803223B0, 0x803223D4, "osSetTime", str_code_u),
    s_code(0x803223E0, 0x80322494, "osMapTLB", str_code_u),
    s_code(0x803224A0, 0x803224E4, "osUnmapTLBAll", str_code_u),
    s_code(0x803224F0, 0x80322594, "sprintf", str_code_u),
    s_code(0x803225A0, 0x803225CC, "osCreateMesgQueue", str_code_u),
    s_code(0x803225D0, 0x80322638, "osSetEventMesg", str_code_u),
    s_code(0x80322640, 0x803226AC, "osViSetEvent", str_code_u),
    s_code(0x803226B0, 0x803227F4, "osCreateThread", str_code_u),
    s_code(0x80322800, 0x80322938, "osRecvMesg", str_code_u),
    s_code(0x80322940, 0x80322BFC, "osSpTaskStart", str_code_u),
    s_code(0x80322C00, 0x80322C20, "osSpTaskYield", str_code_u),
    s_code(0x80322C20, 0x80322D6C, "osSendMesg", str_code_u),
    s_code(0x80322D70, 0x80322DF0, "osSpTaskYielded", str_code_u),
    s_code(0x80322DF0, 0x80322F40, "osStartThread", str_code_u),
    s_code(0x80322F40, 0x80322F68, "osWritebackDCacheAll", str_code_u),
    s_code(0x80322F70, 0x803232C4, "osCreateViManager", str_code_u),
    s_code(0x803232D0, 0x80323338, "osViSetMode", str_code_u),
    s_code(0x80323340, 0x803233B0, "osViBlack", str_code_u),
    s_code(0x803233B0, 0x80323568, "osViSetSpecialFeatures", str_code_u),
    s_code(0x80323570, 0x803236EC, "osCreatePiManager", str_code_u),
    s_code(0x803236F0, 0x803237D0, "osSetThreadPri", str_code_u),
    s_code(0x803237D0, 0x80323A00, "osInitialize", str_code_u),
    s_code(0x80323A00, 0x80323A50, "osViSwapBuffer", str_code_u),
    s_code(0x80323A50, 0x80323A58, "sqrtf", str_code_u),
    s_code(0x80323A60, 0x80323CB8, "osContReadData", str_code_u),
    s_code(0x80323CC0, 0x80324080, "osContInit", str_code_u),
    s_code(0x80324080, 0x803240EC, "osEepromProbe", str_code_u),
    s_code(0x803240F0, 0x803243B0, "ll_multdiv", str_code_d),
    s_code(0x803243B0, 0x8032445C, "osInvalDCache", str_code_u),
    s_code(0x80324460, 0x80324564, "osPiStartDma", str_code_u),
    s_code(0x80324570, 0x8032460C, "bzero", str_code_u),
    s_code(0x80324610, 0x80324684, "osInvalICache", str_code_u),
    s_code(0x80324690, 0x803247CC, "osEepromLongRead", str_code_u),
    s_code(0x803247D0, 0x8032490C, "osEepromLongWrite", str_code_u),
    s_code(0x80324910, 0x80324C14, "bcopy", str_code_u),
    s_code(0x80324C20, 0x80324DDC, "guOrtho", str_code_u),
    s_code(0x80324DE0, 0x80325068, "guPerspective", str_code_u),
    s_code(0x80325070, 0x803250F4, "osGetTime", str_code_u),
    s_code(0x80325100, 0x80325308, "ll_cvt", str_code_d),
    s_code(0x80325310, 0x80325478, "cosf", str_code_u),
    s_code(0x80325480, 0x80325640, "sinf", str_code_u),
    s_code(0x80325640, 0x803256DC, "guTranslate", str_code_u),
    s_code(0x803256E0, 0x803258C4, "guRotate", str_code_u),
    s_code(0x803258D0, 0x8032596C, "guScale", str_code_u),
    s_code(0x80325970, 0x80325AD0, "osAiSetFrequency", str_code_u),
    s_code(0x80325AD0, 0x80325D18, "alBnkfNew", str_code_u),
    s_code(0x80325D20, 0x80325D94, "osWritebackDCache", str_code_u),
    s_code(0x80325DA0, 0x80325DAC, "osAiGetLength", str_code_u),
    s_code(0x80325DB0, 0x80325E58, "osAiSetNextBuffer", str_code_u),
    s_code(0x80325E60, 0x80326260, "__osTimerService", str_code_u),
    s_code(0x80326260, 0x803273E4, "printf", str_code_u),
    s_code(0x803273F0, 0x80327484, "string", str_code_u),
    s_code(0x80327490, 0x803274D0, "__osDequeueThread", str_code_u),
    s_code(0x803274D0, 0x8032750C, "__osInterrupt", str_code_u),
    s_code(0x80327510, 0x80327634, "__osViInit", str_code_u),
    s_code(0x80327640, 0x80327EB0, "__osException", str_code_d),
    s_code(0x80327EB0, 0x80327F2C, "osVirtualToPhysical", str_code_u),
    s_code(0x80327F30, 0x80327F3C, "__osSpSetStatus", str_code_u),
    s_code(0x80327F40, 0x80327F74, "__osSpSetPc", str_code_u),
    s_code(0x80327F80, 0x8032800C, "__osSpRawStartDma", str_code_u),
    s_code(0x80328010, 0x8032803C, "__osSpDeviceBusy", str_code_u),
    s_code(0x80328040, 0x8032804C, "__osSpGetStatus", str_code_u),
    s_code(0x80328050, 0x80328068, "osGetThreadPri", str_code_u),
    s_code(0x80328070, 0x8032807C, "__osViGetCurrentContext", str_code_u),
    s_code(0x80328080, 0x803283DC, "__osViSwapContext", str_code_u),
    s_code(0x803283E0, 0x803283EC, "osGetCount", str_code_u),
    s_code(0x803283F0, 0x803284B0, "__osPiAccess", str_code_u),
    s_code(0x803284B0, 0x80328590, "osPiRawStartDma", str_code_u),
    s_code(0x80328590, 0x80328704, "__osDevMgrMain", str_code_u),
    s_code(0x80328710, 0x80328720, "__osSetSR", str_code_u),
    s_code(0x80328720, 0x8032872C, "__osGetSR", str_code_u),
    s_code(0x80328730, 0x80328740, "__osSetFpcCsr", str_code_u),
    s_code(0x80328740, 0x80328790, "__osSiRawReadIo", str_code_u),
    s_code(0x80328790, 0x803287DC, "__osSiRawWriteIo", str_code_u),
    s_code(0x803287E0, 0x80328838, "osMapTLBRdb", str_code_u),
    s_code(0x80328840, 0x80328894, "osPiRawReadIo", str_code_u),
    s_code(0x803288A0, 0x80328960, "__osSiAccess", str_code_u),
    s_code(0x80328960, 0x80328A0C, "__osSiRawStartDma", str_code_u),
    s_code(0x80328A10, 0x80328AE4, "osSetTimer", str_code_u),
    s_code(0x80328AF0, 0x80328FD0, "osEepromWrite", str_code_u),
    s_code(0x80328FD0, 0x80329120, "osJamMesg", str_code_u),
    s_code(0x80329120, 0x80329148, "osPiGetCmdQueue", str_code_u),
    s_code(0x80329150, 0x80329444, "osEepromRead", str_code_u),
    s_code(0x80329450, 0x803296BC, "guMtxIdent", str_code_u),
    s_code(0x803296C0, 0x80329744, "guNormalize", str_code_u),
    s_code(0x80329750, 0x80329780, "__osAiDeviceBusy", str_code_u),
    s_code(0x80329780, 0x8032978C, "__osSetCompare", str_code_u),
    s_code(0x80329790, 0x80329A90, "_Litob", str_code_u),
    s_code(0x80329A90, 0x8032A860, "_Ldtob", str_code_u),
    s_code(0x8032A860, 0x8032ACD4, "8032A860", str_code_u),
    s_code(0x8032ACE0, 0x8032AE04, "__osSyncPutChars", str_code_u),
    s_code(0x8032AE10, 0x8032AE70, "osSetIntMask", str_code_u),
    s_code(0x8032AE70, 0x8032AF68, "osDestroyThread", str_code_u),
    s_code(0x8032AF70, 0x8032B028, "__osProbeTLB", str_code_u),
    s_code(0x8032B030, 0x8032B05C, "__osSiDeviceBusy", str_code_u),
    s_code(0x8032B060, 0x8032B1E4, "ldiv", str_code_u),
    s_code(0x8032B1F0, 0x8032B1FC, "__osGetCause", str_code_u),
    s_code(0x8032B200, 0x8032B258, "__osAtomicDec", str_code_u),
    s_data(0x80335010, 0x803358D0, "osViModeTable", [
        [1, -28, ultra.c.d_OSViMode],
    ], str_data_u),
    s_data(0x803358D0, 0x803358E8, "osCreateViManager.data", [
        [1, 1, 1, ultra.c.d_str, 0x18, "0"],
    ], str_data_u),
    s_data(0x803358F0, 0x80335908, "osCreatePiManager.data", [
        [1, 1, 1, ultra.c.d_str, 0x18, "0"],
    ], str_data_u),
    s_data(0x80335910, 0x8033591C, "osInitialize.data", [
        [0, 1, 1, ultra.c.d_u64],
        [0, 1, 1, ultra.c.d_u32],
    ], str_data_u),
    s_data(0x80335920, 0x80335924, "osContInit.data", [
        [0, 1, 1, ultra.c.d_u32],
    ], str_data_u),
    s_data(0x80335930, 0x80335931, "osAiSetNextBuffer.data", [
        [0, 1, 1, ultra.c.d_u8],
    ], str_data_u),
    s_data(0x80335940, 0x80335944, "__osTimerService.data", [
        [0, 1, 1, ultra.c.d_addr, 0],
    ], str_data_u),
    s_data(0x80335950, 0x80335994, "printf.data", [
        [0, 2, 36, "str"],
    ], str_data_u),
    s_data(0x803359A0, 0x803359B8, "__osDequeueThread.data", [
        [0, 1, 1, ultra.c.d_OSThreadTail],
        [0, 4, 1, ultra.c.d_addr, ultra.c.A_ADDR, "OSThread *"],
    ], str_data_u),
    s_data(0x803359C0, 0x80335A30, "__osViInit.data", [
        [1, 2, 1, ultra.c.d_str, 0x30, "0"],
        [0, 2, 1, ultra.c.d_addr, ultra.c.A_ADDR],
        [0, 2, 1, ultra.c.d_u32],
    ], str_data_u),
    s_data(0x80335A30, 0x80335A4C, "__osException.data", [
        [1, 1, 1, ultra.c.d_str, 0x14, "0"],
        [0, 2, 1, ultra.c.d_u32],
    ], str_data_u),
    s_data(0x80335A50, 0x80335A54, "__osPiAccess.data", [
        [0, 1, 1, ultra.c.d_u32],
    ], str_data_u),
    s_data(0x80335A60, 0x80335A64, "__osSiAccess.data", [
        [0, 1, 1, ultra.c.d_u32],
    ], str_data_u),
    s_data(0x80335A70, 0x80335A98, "_Litob.data", [
        [0, 2, 20, "str"],
    ], str_data_u),
    s_data(0x80335AA0, 0x80335AF0, "osViModeNtscLan1", [
        [0, 1, ultra.c.d_OSViMode],
    ], str_data_u),
    s_data(0x80335AF0, 0x80335B40, "osViModePalLan1", [
        [0, 1, ultra.c.d_OSViMode],
    ], str_data_u),
    s_data(0x80335B40, 0x80335B4C, "8032A860.data", [
        [0, 3, 1, ultra.c.d_u32],
    ], str_data_u),
    s_data(0x80335B50, 0x80335B58, "__osSyncPutChars.data", [
        [0, 2, 1, ultra.c.d_u32],
    ], str_data_u),
    s_data(0x803397B0, 0x803397B8, "guPerspective.data", [
        [0, 1, 1, ultra.c.d_f64],
    ], str_data_u),
    s_data(0x803397C0, 0x803397D0, "ll_cvt.data", [
        [0, 2, 1, ultra.c.d_64],
    ], str_data_u),
    s_data(0x803397D0, 0x80339814, "cosf.data", [
        [1, 1, 5, ultra.c.d_f64],
        [0, 3, 1, ultra.c.d_f64],
        [0, 1, 1, ultra.c.d_f32],
    ], str_data_u),
    s_data(0x80339820, 0x80339864, "sinf.data", [
        [1, 1, 5, ultra.c.d_f64],
        [0, 3, 1, ultra.c.d_f64],
        [0, 1, 1, ultra.c.d_f32],
    ], str_data_u),
    s_data(0x80339870, 0x80339874, "guRotate.data", [
        [0, 1, 1, ultra.c.d_f32],
    ], str_data_u),
    s_data(0x80339880, 0x80339974, "printf.data", [
        [0, 1, 4, "str"],
        [0, 1, 8, "str"],
        [1, 1, 6, ultra.c.d_u32],
        [0, -52, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], ""),
    s_data(0x80339980, 0x803399C4, "__osException.data", [
        [0, -2, 16, ultra.c.d_u8],
        [0, -9, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], ""),
    s_data(0x803399D0, 0x803399D4, "__libm_qnan_f", [
        [0, 1, 1, ultra.c.d_32],
    ], str_data_u),
    s_data(0x803399E0, 0x80339A40, "_Ldtob.data", [
        [0, -9, 1, ultra.c.d_f64],
        [0, 3, 4, "str"],
        [0, 1, 4, None],
        [0, 1, 1, ultra.c.d_f64],
    ], str_data_u),
    s_data(0x80339A40, 0x80339AC0, "osSetIntMask.data", [
        [0, -8, 8, ultra.c.d_16],
    ], str_data_u),
]

ultra_PR = [
    s_code(0x80246000, 0x80246050, "crt0", str_code_u),
    [main.s_addr, 0xA4000000-0x00000000],
    # s_code(0xA4000040, 0xA4000B6C, "ipl3"),
    # s_databin(0xA4000B70, 0xA4001000, "ipl3.data"),
    s_databin(0xA4000040, 0xA4001000, "ipl3"),
    [main.s_file, "rspboot.asm"],
        [main.s_str, str_ucode_text % ("rspboot", 0x04001000)],
        [main.s_addr, 0x04001000 - 0x000E6260],
        [ultra.asm.s_code, 0x04001000, 0x040010D0, "E0", 1, False],
        [main.s_str, str_ucode_end],
    [main.s_write],
    [main.s_file, "gspFast3D.fifo.asm"],
        [main.s_str, str_ucode_text % ("gspFast3D.fifo", 0x04001080)],
        [main.s_addr, 0x04001080 - 0x000E6330],
        [ultra.asm.s_code, 0x04001080, 0x04001FE0, "E0", 1, False],
        [main.s_str, str_ucode_base % "0x04001000"],
        [main.s_addr, 0x04001000 - 0x000E7290],
        [ultra.asm.s_code, 0x04001000, 0x04001088, "E0", 1, False],
        [main.s_str, str_ucode_base % "0x04001768"],
        [main.s_addr, 0x04001768 - 0x000E7318],
        [ultra.asm.s_code, 0x04001768, 0x04001988, "E0", 1, False],
        [main.s_str, str_ucode_base % "0x04001768"],
        [main.s_addr, 0x04001768 - 0x000E7538],
        [ultra.asm.s_code, 0x04001768, 0x04001900, "E0", 1, False],
        [main.s_str, str_ucode_base % "0x04001768"],
        [main.s_addr, 0x04001768 - 0x000E76D0],
        [ultra.asm.s_code, 0x04001768, 0x040017D0, "E0", 1, False],
        [main.s_str, str_ucode_data % "gspFast3D.fifo"],
        [main.s_addr, 0x00000000 - 0x000F4AC0],
        [ultra.asm.s_data, 0x00000000, 0x00000800, "E0", [
            [5, 1, d_prg],
            [1, 2, ultra.asm.d_shalf], # VCONST_SCREENCLAMP
            [1, 2, ultra.asm.d_half],
            [1, 4, ultra.asm.d_shalf], # VCONST_OFFSET
            [1, 4, ultra.asm.d_half],
            [1, 8, ultra.asm.d_half], # VCONST1_OFFSET
            [1, 8, ultra.asm.d_shalf], # VOPENGL_OFFSET
            [1, 8, ultra.asm.d_shalf], # VNEWT_OFFSET
            [12, 1, ultra.asm.d_word], # CLIP_SELECT
            [1, 1, ultra.asm.d_addr], # DOLIGHT
            [3, 1, ultra.asm.d_half], # arccos
            [1, 6, ultra.asm.d_half], # CLIPMASKS
            [1, 1, ultra.asm.d_shalf], # ANCHOR
            [1, 1, ultra.asm.d_addr], # TASKDONE
            [1, 1, ultra.asm.d_word], # SEGADDR_MASK_OFFSET
            [4, 1, ultra.asm.d_addr], # op type
            [10, 1, ultra.asm.d_addr], # op 00
            [15, 1, ultra.asm.d_addr], # op 80
            [7, 1, ultra.asm.d_addr], # clip
            [1, 1, ultra.asm.d_addr], # DMAWAITDL
            [(0x800-0x106), 1, ultra.asm.d_byte],
        ]],
        [main.s_str, str_ucode_end],
    [main.s_write],
    [main.s_file, "aspMain.asm"],
        [main.s_str, str_ucode_text % ("aspMain", 0x04001080)],
        [main.s_addr, 0x04001080 - 0x000E7740],
        [ultra.asm.s_code, 0x04001080, 0x04001EA0, "E0", 1, False],
        [main.s_str, str_ucode_data % "aspMain"],
        [main.s_addr, 0x00000000 - 0x000F52C0],
        [ultra.asm.s_data, 0x00000000, 0x000002C0, "E0", [
            [0x2C, 4, ultra.asm.d_word],
        ]],
        [main.s_str, str_ucode_end],
    [main.s_write],
]

src_main = [
    s_code(0x80246050, 0x80246E68, "main"),
    s_code(0x80246E70, 0x80248C3C, "app"),
    s_code(0x80248C40, 0x802495DC, "audio"),
    s_code(0x802495E0, 0x8024BFE4, "game"),
    s_code(0x8024BFF0, 0x8025093C, "player_touch"),
    s_code(0x80250940, 0x8025507C, "player"),
    s_code(0x80255080, 0x80256DFC, "player_move"),
    s_code(0x80256E00, 0x8025DD68, "player_demo"),
    s_code(0x8025DD70, 0x802608AC, "player_hang"),
    s_code(0x802608B0, 0x80263E5C, "player_stop"),
    s_code(0x80263E60, 0x80269F38, "player_ground"),
    s_code(0x80269F40, 0x80270104, "player_air"),
    s_code(0x80270110, 0x80274EAC, "player_water"),
    s_code(0x80274EB0, 0x802761D0, "player_grab"),
    s_code(0x802761D0, 0x80277ED4, "player_gfx"),
    s_code(0x80277EE0, 0x80279158, "memory"),
    s_code(0x80279160, 0x8027A7C4, "save"),
    s_code(0x8027A7D0, 0x8027B6C0, "world"),
    s_code(0x8027B6C0, 0x8027E3DC, "g_draw"),
    s_code(0x8027E3E0, 0x8027F4D4, "time"),
    s_code(0x8027F4E0, 0x8027F584, "szp"),

    s_code(0x8027F590, 0x8029C764, "camera"),

    s_code(0x8029C770, 0x8029C780, "course"),
    s_code(0x8029C780, 0x8029D884, "object_update"),
    s_code(0x8029D890, 0x802A5618, "object"),
    s_code(0x802A5620, 0x802C89F0, "object_state_a"),
    s_code(0x802C89F0, 0x802C8F40, "object_move"),
    s_code(0x802C8F40, 0x802C97C8, "object_touch"),
    s_code(0x802C97D0, 0x802CA03C, "object_list"),
    s_code(0x802CA040, 0x802CA370, "object_sfx"),
    s_code(0x802CA370, 0x802CA390, "coin"),
    s_code(0x802CA390, 0x802CA3B0, "door"),
    s_code(0x802CA3B0, 0x802CB5B4, "object_debug"),

    s_code(0x802CB5C0, 0x802CD27C, "wipe"),
    s_code(0x802CD280, 0x802CF5A4, "shadow"),
    s_code(0x802CF5B0, 0x802D007C, "background"),
    s_code(0x802D0080, 0x802D2208, "scroll"),
    s_code(0x802D2210, 0x802D29BC, "object_gfx"),
    s_code(0x802D29C0, 0x802D5E00, "ripple"),

    s_code(0x802D5E00, 0x802D6F18, "print"),
    s_code(0x802D6F20, 0x802DDDEC, "message"),
    s_code(0x802DDDF0, 0x802DFD50, "particle_snow"),
    s_code(0x802DFD50, 0x802E2094, "particle_lava"),
    s_code(0x802E20A0, 0x802E2CF0, "obj_data"),
    s_code(0x802E2CF0, 0x802E3E50, "hud"),
    s_code(0x802E3E50, 0x802F972C, "object_state_b"),

    s_code(0x802F9730, 0x80314A2C, "object_state_c"),

    s_databin(0x8032D560, 0x80332E50, "data"),
    s_databin(0x80335B60, 0x80338DA0, "rodata"),
]

src_audio = [
    s_code(0x80314A30, 0x80316E78, "a"),
    s_code(0x80316E80, 0x80318034, "b"),
    s_code(0x80318040, 0x80319914, "c"),
    s_code(0x80319920, 0x8031AEDC, "d"),
    s_code(0x8031AEE0, 0x8031B82C, "e"),
    s_code(0x8031B830, 0x8031E4E4, "f"),
    s_code(0x8031E4F0, 0x80322364, "g"),
    s_databin(0x80332E50, 0x80335010, "data"),
    s_databin(0x80338DA0, 0x803397B0, "rodata"),
]

src_main2 = [
    s_code(0x80378800, 0x8037B21C, "math"),
    s_code(0x8037B220, 0x8037CD60, "g"),
    s_code(0x8037CD60, 0x8037E19C, "g_script"),
    s_code(0x8037E1A0, 0x80380684, "s_script"),
    s_code(0x80380690, 0x8038248C, "map"),
    s_code(0x80382490, 0x80383B6C, "map_data"),
    s_code(0x80383B70, 0x80385F88, "o_script"),
    s_data(0x80385F90, 0x80385FF6, "math.data", [
        [0, 1, 1, d_matrix],
        [1, 1, 3, ultra.c.d_f32],
        [1, 1, 3, ultra.c.d_s16],
        [0, 1, 2, None],
        [1, 1, 3, ultra.c.d_f32],
        [1, 1, 3, ultra.c.d_s16],
    ], str_gfx),
    s_data(0x80386000, 0x8038B802, "math_table", [
        [0, -0x1400, 1, ultra.c.d_f32, None],
        [0,   -0x80, 8, ultra.c.d_16],
        [0,      -1, 1, ultra.c.d_16],
    ]),
    s_data(0x8038B810, 0x8038B894, "g_script.data", [
        [0, -0x21, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ]),
    s_data(0x8038B8A0, 0x8038B9AC, "s_script.data", [
        [0, 1, 1, ultra.c.d_addr, 0],
        [0, 1, 1, ultra.c.d_u16], [0, 1, 2, None],
        [0, 1, 1, ultra.c.d_u16], [0, 1, 2, None],
        [0, 1, 1, ultra.c.d_s16], [0, 1, 2, None],
        [0, 2, 1, ultra.c.d_addr, 0],
        [0, -0x3D, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ]),
    s_data(0x8038B9B0, 0x8038BA90, "o_script.data", [
        [0, -0x38, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ]),
    s_data(0x8038BA90, 0x8038BAEC, "math.data", [
        [0, 1, 1, ultra.c.d_f64],
        [0, -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0, 16, 1, ultra.c.d_f32],
    ], "\n\n"),
    s_data(0x8038BAF0, 0x8038BB38, "s_script.data", [
        [0, -18, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], "\n\n"),
    s_data(0x8038BB40, 0x8038BBB0, "map.data", [
        [0, 1, 12, "str"],
        [0, 3,  8, "str"],
        [0, 3,  4, "str"],
        [0, 3, 12, "str"],
        [0, 7, 1, ultra.c.d_f32],
    ]),
    s_data(0x8038BBB0, 0x8038BC84, "map_data.data", [
        [0, 5, 1, ultra.c.d_f64],
        [0, -42, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0, 1, 1, ultra.c.d_f32],
    ]),
]

src_menu = [
    s_code(0x8016F000, 0x8016F670, "title"),
    s_code(0x8016F670, 0x80170280, "title_bg"),
    s_code(0x80170280, 0x801768E0, "file_select"),
    s_code(0x801768E0, 0x80177710, "star_select"),
    s_data(0x801A7830, 0x801A7C3C, "title.data", [
        [0, -38, 16, "str"],
        [0, 26, 16, None],
        [0, 1, 1, ultra.c.d_u16], [0, 1, 2, None],
        [0, 1, 1, ultra.c.d_s16], [0, 1, 2, None],
        [0, 1, 1, ultra.c.d_s16], [0, 1, 2, None],
    ]),
    s_data(0x801A7C40, 0x801A7C68, "title.data", [
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0, 1,  4, "str"],
    ], ""),
    s_data(0x801A7C70, 0x801A7D10, "title_bg.data", [
        [0, -4, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0, -6, 4, ultra.c.d_f32],
        [0, -2, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0, -3, 4, ultra.c.d_s8],
        [0, -1, 1, ultra.c.d_addr, 0],
        [0, -3, 4, ultra.c.d_s8],
        [0, -1, 4, ultra.c.d_s8],
        [0, -1, 1, ultra.c.d_s8],
        [0, -1, 4, ultra.c.d_s8],
        [0, -1, 3, ultra.c.d_s8],
    ]),
    s_databin(0x801A7D10, 0x801A7F40, "file_select.data"),
    s_databin(0x801A7F40, 0x801A81A0, "file_select.rodata"),
    [main.s_file, "star_select.data.c"],
        [main.s_str, str_data],
        [ultra.c.s_data, 0x801A81A0, 0x801A81AC, "E0", [
            [0, 1, 1, ultra.c.d_s8], [0, 1, 3, None],
            [0, 1, 1, ultra.c.d_s8], [0, 1, 3, None],
            [0, 1, 1, ultra.c.d_s32],
        ]],
        [s_msg, 0x801A81AC, 0x801A81B4, "E0", "en", 0, "star_select", [
            "myscore",
        ]],
        [ultra.c.s_data, 0x801A81B4, 0x801A81B6, "E0", [
            [0, 1, 1, ultra.c.d_u16],
        ]],
        [ultra.c.s_data, 0x801A81C0, 0x801A81E0, "E0", [
            [0, 3, 1, ultra.c.d_f64],
            [0, 2, 1, ultra.c.d_f32],
        ]],
    [main.s_write],
]

src_face = [
    s_code(0x80177710, 0x80177820, "main"),
    s_code(0x80177820, 0x801781E0, "mem"),
    s_code(0x801781E0, 0x80178280, "sfx"),
    s_code(0x80178280, 0x8017BDF0, "draw"),
    s_code(0x8017BDF0, 0x80181720, "object"),
    s_code(0x80181720, 0x80181D40, "skin"),
    s_code(0x80181D40, 0x80183A50, "particle"),
    s_code(0x80183A50, 0x8018B830, "dynlist"),
    s_code(0x8018B830, 0x8018C2F0, "gadget"),
    s_code(0x8018C2F0, 0x8018E660, "stdio"),
    s_code(0x8018E660, 0x80192050, "joint"),
    s_code(0x80192050, 0x80193C70, "net"),
    s_code(0x80193C70, 0x801973C0, "math"),
    s_code(0x801973C0, 0x8019B060, "shape"),
    s_code(0x8019B060, 0x801A7830, "gfx"),
    s_databin(0x801A81E0, 0x801B54C0, "data"),
    s_databin(0x801B54C0, 0x801B99E0, "rodata"),
]

data_main_gfx = [
    s_dirfile("print", "texture.c"),
        [ultra.c.s_data, 0x02000000, 0x02004A00, "E0.szp", [
            [0, 1, 1, ultra.c.d_texture, "rgba16", 16, 16, name]
            for name in tuple("0123456789abcdefghiklmnoprstuwy") + (
                "squote", "dquote", "multiply", "coin", "mario", "star"
            )
        ]],
    s_writepop(),
    s_dirfile("credit", "texture.c"),
        [ultra.c.s_data, 0x02004A00, 0x02005900, "E0.szp", [
            [0, 1, 1, ultra.c.d_texture, "rgba16", 8, 8, name]
            for name in tuple("346abcdefghijklmnopqrstuvwxyz") + ("period",)
        ]],
    s_writepop(),
    s_dirfile("message", "texture.c"),
        [ultra.c.s_data, 0x02005900, 0x02007000, "E0.szp", [
            [0, 1, 1, ultra.c.d_texture, "ia4", 16, 8, "%08X" % i]
            for i in range(0x02005900, 0x02007000, 0x40)
        ]],
    s_writepop(),
    s_dirfile("camera", "texture.c"),
        [ultra.c.s_data, 0x02007000, 0x02007700, "E0.szp", [
            [0, 1, 1, ultra.c.d_texture, "rgba16", 16, 16, "camera"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 16, 16, "lakitu"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 16, 16, "cross"],
            [0, 1, 1, ultra.c.d_texture, "rgba16",  8,  8, "up"],
            [0, 1, 1, ultra.c.d_texture, "rgba16",  8,  8, "down"],
        ]],
    s_writepop(),
    s_dirfile("print", "table.c"),
        [ultra.c.s_data, 0x02007700, 0x020077E8, "E0.szp", [
            [0, -58, 1, ultra.c.d_addr, 0],
        ]],
    s_writepop(),
    s_dirfile("message", "table.c"),
        [ultra.c.s_data, 0x020077E8, 0x02007BE8, "E0.szp", [
            [0, -0x100, 1, ultra.c.d_addr, 0],
        ]],
    s_writepop(),
    s_dirfile("credit", "table.c"),
        [ultra.c.s_data, 0x02007BE8, 0x02007C7C, "E0.szp", [
            [0, -37, 1, ultra.c.d_addr, 0],
        ]],
    s_writepop(),
    s_dirfile("camera", "table.c"),
        [ultra.c.s_data, 0x02007C7C, 0x02007C94, "E0.szp", [
            [0, -6, 1, ultra.c.d_addr, 0],
        ]],
    s_writepop(),
    [main.s_str, "\n"],
    [s_msg, 0x02007D28, 0x02007D34, "E0.szp", "jp", 2, "select", None],
    [s_msg, 0x02010A68, 0x02010D14, "E0.szp", "en", 2, "table", msg_table],
    [s_msg, 0x02010F68, 0x02010FD4, "E0.szp", "en", 1, "course", msg_course],
    [s_msg, 0x0201192C, 0x02011AB4, "E0.szp", "en", 1, "level", None],
    [main.s_str, "\n"],
    [ultra.c.s_data, 0x02011AB8, 0x02011AC0, "E0.szp", [
        [0, 1, 1, ultra.c.d_u64],
    ]],
    [main.s_str, "\n"],
    s_dirfile("print", "gfx.c"),
        [ultra.c.s_data, 0x02011AC0, 0x02011C08, "E0.szp", [
            [0, 1, 1, ultra.c.d_Gfx, 0x02011C08],
        ]],
    s_writepop(),
    s_dirfile("message", "gfx.c"),
        [ultra.c.s_data, 0x02011C08, 0x02011E10, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            [0,  1, 1, ultra.c.d_Gfx, 0x02011C88],
            [0, -4, 1, ultra.c.d_Vtx, False],
            [0,  1, 1, ultra.c.d_Gfx, 0x02011D90],
            [0, -3, 1, ultra.c.d_Vtx, False],
            [0,  1, 1, ultra.c.d_Gfx, 0x02011E10],
        ]],
    s_writepop(),
    s_dirfile("print", "digit.c"),
        [ultra.c.s_data, 0x02011E10, 0x020120B8, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            [0,  1, 1, ultra.c.d_Gfx, 0x020120B8],
        ]],
    s_writepop(),
    s_dirfile("shadow", "texture.c"),
        [ultra.c.s_data, 0x020120B8, 0x020122B8, "E0.szp", [
            [0, 1, 1, ultra.c.d_texture, "ia8", 16, 16, "circle"],
            [0, 1, 1, ultra.c.d_texture, "ia8", 16, 16, "square"],
        ]],
    s_writepop(),
    s_dirfile("wipe", "texture.c"),
        [ultra.c.s_data, 0x020122B8, 0x02014AB8, "E0.szp", [
            [0, 1, 1, ultra.c.d_texture, "ia8", 32, 64, "star"],
            [0, 1, 1, ultra.c.d_texture, "ia8", 32, 64, "circle"],
            [0, 1, 1, ultra.c.d_texture, "ia8", 64, 64, "mario"],
            [0, 1, 1, ultra.c.d_texture, "ia8", 32, 64, "bowser"],
        ]],
    s_writepop(),
    s_dirfile("scroll", "texture.c"),
        [ultra.c.s_data, 0x02014AB8, 0x020172B8, "E0.szp", [
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "water_0"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "water_1"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "water_2"],
            [0, 1, 1, ultra.c.d_texture, "ia16",   32, 32, "mist"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "lava"],
        ]],
    s_writepop(),
    [ultra.c.s_data, 0x020172B8, 0x02017380, "E0.szp", [
        [0, 1, 1, ultra.c.d_Lights1],
        [0, 2, 1, d_matrix],
        [0, 1, 1, ultra.c.d_Gfx, 0x02017380],
    ]],
    s_dirfile("shadow", "gfx.c"),
        [ultra.c.s_data, 0x02017380, 0x020174C0, "E0.szp", [
            [0, 1, 1, ultra.c.d_Gfx, 0x020174C0],
        ]],
    s_writepop(),
    s_dirfile("wipe", "gfx.c"),
        [ultra.c.s_data, 0x020174C0, 0x02017568, "E0.szp", [
            [0, 1, 1, ultra.c.d_Gfx, 0x02017568],
        ]],
    s_writepop(),
    s_dirfile("background", "gfx.c"),
        [ultra.c.s_data, 0x02017568, 0x020175F0, "E0.szp", [
            [0, 1, 1, ultra.c.d_Gfx, 0x020175F0],
        ]],
    s_writepop(),
    s_dirfile("scroll", "gfx.c"),
        [ultra.c.s_data, 0x020175F0, 0x02017698, "E0.szp", [
            [0, 1, 1, ultra.c.d_Gfx, 0x02017698],
        ]],
    s_writepop(),
    s_dirfile("minimap", "gfx.c"),
        [ultra.c.s_data, 0x02017698, 0x020177B8, "E0.szp", [
            [0, 1, 1, ultra.c.d_texture, "ia8", 8, 8, "arrow"],
            [0, 1, 1, ultra.c.d_Gfx, 0x020177B8],
        ]],
    s_writepop(),
    s_dirfile("ripple", "gfx.c"),
        [ultra.c.s_data, 0x020177B8, 0x02018A0E, "E0.szp", [
            [0, 1, 1, ultra.c.d_Lights1],
            [0, 1, 1, ultra.c.d_Gfx, 0x020178C0],
            [0, 2, 1, d_ripple_0],
            [0, 1, 2, None],
            [0, 1, 1, d_ripple_1, 0x02018A0E],
        ]],
    s_writepop(),
]

data_player_gfx = [
    s_dirfile("mario", "gfx.c"),
        s_gfx_ifndef(),
        [ultra.c.s_data, 0x04000000, 0x0400C090, "E0.szp", [
            [0, 6, 1, d_light, 0.5],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 64, 32, "metal"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "button"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "logo"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "sideburn"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "moustache"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "eye_open"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "eye_half"],
            [0, 3, 1, ultra.c.d_texture, "rgba16", 32, 32, "eye_closed"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "eye_left"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "eye_right"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "eye_up"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "eye_down"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "eye_dead"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 64, "wing_l"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 64, "wing_r"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 64, "metal_wing_l"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 64, "metal_wing_r"],
        ]],
        s_shape(0x0400CA00, 0x0400CC90, 0x0400CD40, "h_waist",  True),
        s_shape(0x0400D090, 0x0400D1D0, 0x0400D1F8, "h_uarmL",  True),
        s_shape(0x0400D2F8, 0x0400D3E0, 0x0400D3E8, "h_larmL",  True),
        s_shape(0x0400D758, 0x0400D8E8, 0x0400D910, "h_fistL",  True),
        s_shape(0x0400DCA0, 0x0400DDE0, 0x0400DE08, "h_uarmR",  True),
        s_shape(0x0400DF08, 0x0400DFF0, 0x0400DFF8, "h_larmR",  True),
        s_shape(0x0400E2C8, 0x0400E450, 0x0400E4A8, "h_fistR",  True),
        s_shape(0x0400E6A8, 0x0400E7A8, 0x0400E858, "h_thighL", True),
        s_shape(0x0400E918, 0x0400E9C0, 0x0400E9C8, "h_shinL",  True),
        s_shape(0x0400EBB8, 0x0400EC98, 0x0400ECC0, "h_shoeL",  True),
        s_shape(0x0400EEB0, 0x0400EFB0, 0x0400EFD8, "h_thighR", True),
        s_shape(0x0400F1D8, 0x0400F288, 0x0400F290, "h_shinR",  True),
        s_shape(0x0400F400, 0x0400F4E0, 0x0400F568, "h_shoeR",  True),
        [s_shape_vtx, "h_torso0"],
        [s_shape_vtx, "h_torso2"],
        [s_shape_vtx, "h_torso1"],
        [ultra.c.s_data, 0x0400FF28, 0x04010410, "E0.szp", [
            [0, 1, 1, d_shape_gfx, 0x0400FF80, "h_torso0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0400FF88],
            [0, 1, 1, d_shape_gfx, 0x04010258, "h_torso1", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04010260],
            [0, 1, 1, d_shape_gfx, 0x04010340, "h_torso2", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04010410],
        ]],
        [s_shape_vtx, "h_cap0"],
        [s_shape_vtx, "h_cap1"],
        [s_shape_vtx, "h_cap2"],
        [s_shape_vtx, "h_cap3"],
        [s_shape_vtx, "h_cap5"],
        [s_shape_vtx, "h_cap4"],
        [s_shape_vtx, "h_cap6"],
        [ultra.c.s_data, 0x040112B0, 0x04012190, "E0.szp", [
            [0, 1, 1, d_shape_gfx, 0x040112E0, "h_cap0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040112E8],
            [0, 1, 1, d_shape_gfx, 0x04011348, "h_cap1", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04011350],
            [0, 1, 1, d_shape_gfx, 0x04011398, "h_cap2", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040113A0],
            [0, 1, 1, d_shape_gfx, 0x04011430, "h_cap3", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04011438],
            [0, 1, 1, d_shape_gfx, 0x040116F0, "h_cap4", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040116F8],
            [0, 1, 1, d_shape_gfx, 0x04011868, "h_cap5", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04011870],
            [0, 1, 1, d_shape_gfx, 0x04011958, "h_cap6", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04012160],
            [0, 2, 1, d_light, 0.25],
        ]],
        [s_shape_vtx, "h_hair0"],
        [s_shape_vtx, "h_hair2"],
        [s_shape_vtx, "h_hair1"],
        [s_shape_vtx, "h_hair3a"],
        [s_shape_vtx, "h_hair4"],
        [s_shape_vtx, "h_hair3b"],
        [ultra.c.s_data, 0x040132B0, 0x04014098, "E0.szp", [
            [0, 1, 1, d_shape_gfx, 0x04013310, "h_hair0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04013318],
            [0, 1, 1, d_shape_gfx, 0x040133A0, "h_hair1", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040133A8],
            [0, 1, 1, d_shape_gfx, 0x040133F0, "h_hair2", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040133F8],
            [0, 1, 1, d_shape_gfx, 0x040136B8, "h_hair3a", True, None],
            [0, 1, 1, d_shape_gfx, 0x040136C8, "h_hair3b", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x040136D0],
            [0, 1, 1, d_shape_gfx, 0x040139B8, "h_hair4", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04014098],
        ]],
        s_shape(0x040144D8, 0x04014630, 0x040146E0, "m_waist",  True),
        s_shape(0x040147D0, 0x04014838, 0x04014860, "m_uarmL",  True),
        s_shape(0x04014950, 0x040149B8, 0x040149C0, "m_larmL",  True),
        s_shape(0x04014C90, 0x04014DB8, 0x04014DE0, "m_fistL",  True),
        s_shape(0x04014ED0, 0x04014F38, 0x04014F60, "m_uarmR",  True),
        s_shape(0x04015050, 0x040150B8, 0x040150C0, "m_larmR",  True),
        s_shape(0x040153B0, 0x040154D8, 0x04015530, "m_fistR",  True),
        s_shape(0x04015620, 0x040156A8, 0x04015758, "m_thighL", True),
        s_shape(0x04015848, 0x040158D0, 0x040158D8, "m_shinL",  True),
        s_shape(0x04015A98, 0x04015B58, 0x04015B80, "m_shoeL",  True),
        s_shape(0x04015C70, 0x04015CF8, 0x04015D20, "m_thighR", True),
        s_shape(0x04015E10, 0x04015E98, 0x04015EA0, "m_shinR",  True),
        s_shape(0x04016000, 0x040160C0, 0x04016148, "m_shoeR",  True),
        [s_shape_vtx, "m_torso0"],
        [s_shape_vtx, "m_torso2"],
        [s_shape_vtx, "m_torso1"],
        [ultra.c.s_data, 0x04016668, 0x04016968, "E0.szp", [
            [0, 1, 1, d_shape_gfx, 0x040166B0, "m_torso0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040166B8],
            [0, 1, 1, d_shape_gfx, 0x040167F8, "m_torso1", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04016800],
            [0, 1, 1, d_shape_gfx, 0x04016898, "m_torso2", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04016968],
        ]],
        s_shape(0x04016A18, 0x04016AB0, 0x04016B60, "l_waist",  True),
        s_shape(0x04016C20, 0x04016C68, 0x04016C90, "l_uarmL",  True),
        s_shape(0x04016D50, 0x04016D98, 0x04016DA0, "l_larmL",  True),
        s_shape(0x04016E20, 0x04016E78, 0x04016EA0, "l_fistL",  True),
        s_shape(0x04016F60, 0x04016FA8, 0x04016FD0, "l_uarmR",  True),
        s_shape(0x04017090, 0x040170D8, 0x040170E0, "l_larmR",  True),
        s_shape(0x04017160, 0x040171B8, 0x04017210, "l_fistR",  True),
        s_shape(0x040172F0, 0x04017358, 0x04017408, "l_thighL", True),
        s_shape(0x040174E8, 0x04017550, 0x04017558, "l_shinL",  True),
        s_shape(0x04017638, 0x040176A0, 0x040176C8, "l_shoeL",  True),
        s_shape(0x040177A8, 0x04017810, 0x04017838, "l_thighR", True),
        s_shape(0x04017918, 0x04017980, 0x04017988, "l_shinR",  True),
        s_shape(0x04017A68, 0x04017AD0, 0x04017B58, "l_shoeR",  True),
        [s_shape_vtx, "l_torso0"],
        [s_shape_vtx, "l_torso1"],
        [s_shape_vtx, "l_torso2"],
        [ultra.c.s_data, 0x04017D68, 0x04017F40, "E0.szp", [
            [0, 1, 1, d_shape_gfx, 0x04017D90, "l_torso0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04017D98],
            [0, 1, 1, d_shape_gfx, 0x04017E18, "l_torso1", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04017E20],
            [0, 1, 1, d_shape_gfx, 0x04017E70, "l_torso2", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04017F40],
        ]],
        [s_shape_vtx, "l_cap0"],
        [s_shape_vtx, "l_cap1"],
        [s_shape_vtx, "l_cap2"],
        [s_shape_vtx, "l_cap4"],
        [s_shape_vtx, "l_cap3"],
        [s_shape_vtx, "l_cap5"],
        [ultra.c.s_data, 0x04018270, 0x04018B18, "E0.szp", [
            [0, 1, 1, d_shape_gfx, 0x04018290, "l_cap0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018298],
            [0, 1, 1, d_shape_gfx, 0x040182B8, "l_cap1", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040182C0],
            [0, 1, 1, d_shape_gfx, 0x040182F8, "l_cap2", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018300],
            [0, 1, 1, d_shape_gfx, 0x04018368, "l_cap3", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018370],
            [0, 1, 1, d_shape_gfx, 0x040183E8, "l_cap4", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x040183F0],
            [0, 1, 1, d_shape_gfx, 0x04018418, "l_cap5", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018B18],
        ]],
        [s_shape_vtx, "l_hair0"],
        [s_shape_vtx, "l_hair1"],
        [s_shape_vtx, "l_hair2"],
        [s_shape_vtx, "l_hair3"],
        [ultra.c.s_data, 0x04018DC8, 0x04019538, "E0.szp", [
            [0, 1, 1, d_shape_gfx, 0x04018DE8, "l_hair0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018DF0],
            [0, 1, 1, d_shape_gfx, 0x04018E28, "l_hair1", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018E30],
            [0, 1, 1, d_shape_gfx, 0x04018E98, "l_hair2", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018EA0],
            [0, 1, 1, d_shape_gfx, 0x04018F60, "l_hair3", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04019538],
        ]],
        s_shape(0x04019A68, 0x04019C98, 0x04019CC0, "handL", True),
        s_shape(0x0401A1F0, 0x0401A420, 0x0401A478, "handR", True),
        [s_shape_vtx, "capR0"],
        [s_shape_vtx, "capR2"],
        [s_shape_vtx, "capR1"],
        [s_shape_vtx, "capR3"],
        [ultra.c.s_data, 0x0401ABA8, 0x0401AF60, "E0.szp", [
            [0, 1, 1, d_shape_gfx, 0x0401ABC8, "capR0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401ABD0],
            [0, 1, 1, d_shape_gfx, 0x0401AD38, "capR1", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401AD40],
            [0, 1, 1, d_shape_gfx, 0x0401AEC8, "capR2", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401AED0],
            [0, 1, 1, d_shape_gfx, 0x0401AF18, "capR3", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401AF60],
        ]],
        [s_shape_vtx, "wingsR_l"],
        [s_shape_vtx, "wingsR_r"],
        [ultra.c.s_data, 0x0401B080, 0x0401B2D0, "E0.szp", [
            [0, 1, 1, d_shape_gfx, 0x0401B0A8, "wingsR_l", True, (32, 64)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401B0B0],
            [0, 1, 1, d_shape_gfx, 0x0401B0D8, "wingsR_r", True, (32, 64)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401B2D0],
        ]],
        s_shape(0x0401BC80, 0x0401BF28, 0x0401BF50, "peaceR"),
        [s_shape_vtx, "cap0"],
        [s_shape_vtx, "cap1"],
        [s_shape_vtx, "cap2"],
        [ultra.c.s_data, 0x0401C330, 0x0401C538, "E0.szp", [
            [0, 1, 1, d_shape_gfx, 0x0401C360, "cap0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401C368],
            [0, 1, 1, d_shape_gfx, 0x0401C4C0, "cap1", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401C4C8],
            [0, 1, 1, d_shape_gfx, 0x0401C508, "cap2", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401C538],
        ]],
        [s_shape_vtx, "wings_l"],
        [s_shape_vtx, "wings_r"],
        [ultra.c.s_data, 0x0401C678, 0x0401C940, "E0.szp", [
            [0, 1, 1, d_shape_gfx, 0x0401C6A0, "wings_l", True, (32, 64)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401C6A8],
            [0, 1, 1, d_shape_gfx, 0x0401C6D0, "wings_r", True, (32, 64)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401C940],
        ]],
        [s_shape_vtx, "wing_l"],
        [s_shape_vtx, "wing_r"],
        [ultra.c.s_data, 0x0401C9C0, 0x04019538, "E0.szp", [
            [0, 1, 1, d_shape_gfx, 0x0401C9D8, "wing_l", True, (32, 64)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401C9E0],
            [0, 1, 1, d_shape_gfx, 0x0401C9F8, "wing_r", True, (32, 64)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401CD20],
        ]],
        s_gfx_else(),
    s_writepop(),
    s_dirfile("bubble", "gfx.c"),
        s_gfx_ifndef(),
        [ultra.c.s_data, 0x0401CD20, 0x0401DE60, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "bubble_0"],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 32, 32, "bubble_1"],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401DE60],
        ]],
        s_gfx_else(),
    s_writepop(),
    s_dirfile("dust", "gfx.c"),
        s_gfx_ifndef(),
        [ultra.c.s_data, 0x0401DE60, 0x040217C0, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            d_texture_n("ia16", 32, 32, 7, "dust_%d"),
            [0, 1, 1, ultra.c.d_Gfx, 0x040217C0],
        ]],
        s_gfx_else(),
    s_writepop(),
    s_dirfile("smoke", "gfx.c"),
        s_gfx_ifndef(),
        [ultra.c.s_data, 0x040217C0, 0x040220C8, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            [0, 1, 1, ultra.c.d_texture, "ia16", 32, 32, "smoke"],
            [0, 1, 1, ultra.c.d_Gfx, 0x040220C8],
        ]],
        s_gfx_else(),
    s_writepop(),
    s_dirfile("wave", "gfx.c"),
        s_gfx_ifndef(),
        [ultra.c.s_data, 0x040220C8, 0x04025318, "E0.szp", [
            [0, -8, 1, ultra.c.d_Vtx, False],
            d_texture_n("ia16", 32, 32, 6, "wave_%d"),
            [0, 1, 1, ultra.c.d_Gfx, 0x04025318],
        ]],
        s_gfx_else(),
    s_writepop(),
    s_dirfile("ripple", "gfx.c"),
        s_gfx_ifndef(),
        [ultra.c.s_data, 0x04025318, 0x04027450, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            d_texture_n("ia16", 32, 32, 4, "ripple_%d"),
            [0, 1, 1, ultra.c.d_Gfx, 0x04027450],
        ]],
        s_gfx_else(),
    s_writepop(),
    s_dirfile("sparkle", "gfx.c"),
        s_gfx_ifndef(),
        [ultra.c.s_data, 0x04027450, 0x0402A588, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            d_texture_n("rgba16", 32, 32, -1, start=5, step=-1),
            [0, 1, 1, ultra.c.d_Gfx, 0x0402A588],
        ]],
        s_gfx_else(),
    s_writepop(),
    s_dirfile("splash", "gfx.c"),
        s_gfx_ifndef(),
        [ultra.c.s_data, 0x0402A588, 0x04032700, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            d_texture_n("rgba16", 32, 64, 8, "splash_%d"),
            [0, 1, 1, ultra.c.d_Gfx, 0x04032700],
        ]],
        s_gfx_else(),
    s_writepop(),
    s_dirfile("droplet", "gfx.c"),
        s_gfx_ifndef(),
        [ultra.c.s_data, 0x04032700, 0x04032A48, "E0.szp", [
            [0, -8, 1, ultra.c.d_Vtx, False],
            [0, 1, 1, ultra.c.d_texture, "rgba16", 16, 16, "droplet"],
            [0, 1, 1, ultra.c.d_Gfx, 0x04032A48],
        ]],
    s_writepop(),
    s_dirfile("glow", "gfx.c"),
        s_gfx_ifndef(),
        [ultra.c.s_data, 0x04032A48, 0x04035378, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            d_texture_n("ia16", 32, 32, 5),
            [0, 1, 1, ultra.c.d_Gfx, 0x04035378],
        ]],
        s_gfx_else(),
    s_writepop(),
]

data_player_g = [
    s_dirfile("bubble", "gfx.c"),
        [UNSM.c.s_script_g, 0x17000000, 0x17000038, "E0"],
        s_gfx_endif(),
    s_writepop(),
    s_dirfile("dust", "gfx.c"),
        [UNSM.c.s_script_g, 0x17000038, 0x17000084, "E0"],
        s_gfx_endif(),
    s_writepop(),
    s_dirfile("smoke", "gfx.c"),
        [UNSM.c.s_script_g, 0x17000084, 0x1700009C, "E0"],
        s_gfx_endif(),
    s_writepop(),
    s_dirfile("wave", "gfx.c"),
        [UNSM.c.s_script_g, 0x1700009C, 0x17000124, "E0"],
        s_gfx_endif(),
    s_writepop(),
    s_dirfile("ripple", "gfx.c"),
        [UNSM.c.s_script_g, 0x17000124, 0x170001BC, "E0"],
        s_gfx_endif(),
    s_writepop(),
    s_dirfile("sparkle", "gfx.c"),
        [UNSM.c.s_script_g, 0x170001BC, 0x17000230, "E0"],
        s_gfx_endif(),
    s_writepop(),
    s_dirfile("splash", "gfx.c"),
        [UNSM.c.s_script_g, 0x17000230, 0x17000284, "E0"],
        s_gfx_endif(),
    s_writepop(),
    s_dirfile("droplet", "gfx.c"),
        s_gfx_endif(),
    s_writepop(),
    s_dirfile("glow", "gfx.c"),
        [UNSM.c.s_script_g, 0x17000284, 0x170002E0, "E0"],
        s_gfx_endif(),
    s_writepop(),
    s_dirfile("mario", "gfx.c"),
        [UNSM.c.s_script_g, 0x170002E0, 0x17002E30, "E0"],
        s_gfx_endif(),
    s_writepop(),
]

data_object = [
    [UNSM.asm.s_script, 0x13000000, 0x130056BC, "E0", 1],
]

def s_object_s(start, end, name):
    return [main.s_call, [
        s_dirfile(os.path.join("object", name), "s.S"),
            [UNSM.asm.s_script, start, end, "E0", 0],
        s_writepop(),
    ]]

data_game = [
    [UNSM.asm.s_script, 0x15000000, 0x15000660, "E0", 0],
    [main.s_str, "\n"],
    s_object_s(0x15000660, 0x1500071C, "c0"),
    s_object_s(0x1500071C, 0x15000750, "a0"),
    s_object_s(0x15000750, 0x1500076C, "a1"),
    s_object_s(0x1500076C, 0x15000788, "a2"),
    s_object_s(0x15000788, 0x150007B4, "a3"),
    s_object_s(0x150007B4, 0x150007E8, "a4"),
    s_object_s(0x150007E8, 0x1500080C, "a5"),
    s_object_s(0x1500080C, 0x15000830, "a6"),
    s_object_s(0x15000830, 0x1500084C, "a7"),
    s_object_s(0x1500084C, 0x15000888, "a8"),
    s_object_s(0x15000888, 0x150008A4, "a9"),
    s_object_s(0x150008A4, 0x150008D8, "a10"),
    s_object_s(0x150008D8, 0x15000914, "b0"),
    s_object_s(0x15000914, 0x15000958, "b1"),
    s_object_s(0x15000958, 0x1500099C, "b2"),
    s_object_s(0x1500099C, 0x150009C0, "b3"),
    s_object_s(0x150009C0, 0x150009DC, "b4"),
    s_object_s(0x150009DC, 0x15000A10, "b5"),
]

lst = [
    [main.s_data, "E0", ["donor", "UNSME0.z64"]],
    [main.s_dir, "ultra"],
        [main.s_addr, 0x80246000-0x00001000],
        [main.s_dir, "src"],
            [main.s_call, ultra_src],
        [main.s_pop],
        [main.s_dir, "PR"],
            [main.s_call, ultra_PR],
        [main.s_pop],
        [main.s_addr, 0],
    [main.s_pop],
    [main.s_dir, "src"],
        [main.s_file, "header.S"],
            [ultra.asm.s_header, "E0"],
        [main.s_write],
        [main.s_addr, 0x80246000-0x00001000],
        [main.s_call, src_main],
        [main.s_dir, "audio"],
            [main.s_call, src_audio],
        [main.s_pop],
        [main.s_addr, 0x80378800-0x000F5580],
        [main.s_call, src_main2],
        [main.s_addr, 0x8016F000-0x0021F4C0],
        [main.s_call, src_menu],
        [main.s_dir, "face"],
            [main.s_call, src_face],
        [main.s_pop],
        [main.s_addr, 0],
    [main.s_pop],
    [main.s_dir, "data"],
        [main.s_dir, "main"],
            [main.s_addr, 0x10000000-0x00108A10],
            [main.s_file, "s.S"],
                [main.s_str, str_s_script],
                [UNSM.asm.s_script, 0x10000000, 0x10000028, "E0", 0],
            [main.s_write],
            [s_szp, 0x00108A40, 0x00114750, "E0"],
            [main.s_addr, 0x02000000],
            [main.s_file, "gfx.c"],
                [main.s_str, str_gfx],
                [main.s_call, data_main_gfx],
            [main.s_write],
            [main.s_dev, None],
            [main.s_addr, 0],
        [main.s_pop],
        [main.s_dir, "object"],
            s_object(
                0x00114750, 0x001279B0, 0x04, 0x17, "player",
                data_player_gfx, data_player_g
            ),
            s_objectbin(0x0012A7E0, 0x00132850, 0x00015360, 0x00000410, 0x0C, "a0"),
            s_objectbin(0x00132C60, 0x00134A70, 0x00006180, 0x000002B0, 0x0C, "a1"),
            s_objectbin(0x00134D20, 0x0013B5D0, 0x000110A0, 0x00000340, 0x0C, "a2"),
            s_objectbin(0x0013B910, 0x00145C10, 0x00013D30, 0x00000280, 0x0C, "a3"),
            s_objectbin(0x00145E90, 0x00151B70, 0x00014650, 0x00000660, 0x0C, "a4"),
            s_objectbin(0x001521D0, 0x001602E0, 0x000160B8, 0x00000384, 0x0C, "a5"),
            s_objectbin(0x00160670, 0x001656E0, 0x0000D130, 0x00000364, 0x0C, "a6"),
            s_objectbin(0x00165A50, 0x00166BD0, 0x000034C8, 0x00000090, 0x0C, "a7"),
            s_objectbin(0x00166C60, 0x0016D5C0, 0x00010178, 0x000002AC, 0x0C, "a8"),
            [main.s_dir, "a9"],
                s_szpbin(0x0016D870, 0x00180540, 0x00024200, "gfx"),
                [main.s_addr, 0x0C000000-0x00180540],
                [main.s_file, "g.c"],
                    [main.s_str, str_g_script],
                    [UNSM.c.s_script_g, 0x0C000000, 0x0C00045C, "E0"],
                    [main.s_str, "\n\nunused static const u64 _0C000460 = 0;\n\n"],
                    [UNSM.c.s_script_g, 0x0C000468, 0x0C000664, "E0"],
                [main.s_write],
                [main.s_addr, 0],
            [main.s_pop],
            s_objectbin(0x00180BB0, 0x00187FA0, 0x00016EC0, 0x000004A0, 0x0C, "a10"),
            s_objectbin(0x00188440, 0x001B9070, 0x00062F10, 0x00000C4C, 0x0D, "b0"),
            s_objectbin(0x001B9CC0, 0x001C3DB0, 0x00017960, 0x00000480, 0x0D, "b1"),
            s_objectbin(0x001C4230, 0x001D7C90, 0x00025188, 0x00000678, 0x0D, "b2"),
            [main.s_dir, "b3"],
                s_szpbin(0x001D8310, 0x001E4BF0, 0x00017E78, "gfx"),
                [main.s_addr, 0x0D000000-0x001E4BF0],
                [main.s_file, "g.c"],
                    [main.s_str, str_g_script],
                    [UNSM.c.s_script_g, 0x0D000000, 0x0D00043C, "E0"],
                    [main.s_str, "\n\nunused static const u64 _0D000440 = 0;\n\n"],
                    [UNSM.c.s_script_g, 0x0D000448, 0x0D0005A4, "E0"],
                    [main.s_str, "\n\nunused static const u64 _0D0005A8 = 0;\n\n"],
                    [UNSM.c.s_script_g, 0x0D0005B0, 0x0D000600, "E0"],
                [main.s_write],
                [main.s_addr, 0],
            [main.s_pop],
            [main.s_dir, "b4"],
                s_szpbin(0x001E51F0, 0x001E7D90, 0x00005E78, "gfx"),
                [main.s_addr, 0x0D000000-0x001E7D90],
                [main.s_file, "g.c"],
                    [main.s_str, str_g_script],
                    [UNSM.c.s_script_g, 0x0D000000, 0x0D000140, "E0"],
                    [main.s_str, "\n\nunused static const u64 _0D000140 = 0;\n\n"],
                [main.s_write],
                [main.s_addr, 0],
            [main.s_pop],
            s_objectbin(0x001E7EE0, 0x001F1B30, 0x00015070, 0x000006D0, 0x0D, "b5"),
            [main.s_dir, "c0"],
                s_szpbin(0x001F2200, 0x002008D0, 0x00028BF0, "gfx"),
                [main.s_addr, 0x0F000000-0x002008D0],
                [main.s_file, "g.c"],
                    [main.s_str, str_g_script],
                    [UNSM.c.s_script_g, 0x0F000000, 0x0F000020, "E0"],
                    [main.s_str, "\n\nunused static const u64 _0F000020 = 0;\n\n"],
                    [UNSM.c.s_script_g, 0x0F000028, 0x0F00019C, "E0"],
                    [main.s_str, "\n\nunused static const u64 _0F0001A0 = 0;\n\n"],
                    [UNSM.c.s_script_g, 0x0F0001A8, 0x0F000B34, "E0"],
                [main.s_write],
                [main.s_addr, 0],
            [main.s_pop],
            [main.s_dir, "entity"],
                s_szpbin(0x00201410, 0x00218DA0, 0x00033308, "gfx"),
                [main.s_addr, 0x16000000-0x00218DA0],
                [main.s_file, "g.c"],
                    [main.s_str, str_g_script],
                    [main.s_str, "\n\nextern const uintptr_t g_entity_144[];\n\n"],
                    [UNSM.c.s_script_g, 0x16000000, 0x16001060, "E0"],
                [main.s_write],
                [main.s_addr, 0],
            [main.s_pop],
            [main.s_addr, 0x13000000-0x00219E00],
            [main.s_file, "o.S"],
                [main.s_str, str_o_script],
                [main.s_call, data_object],
            [main.s_write],
            [main.s_addr, 0],
        [main.s_pop],
        [main.s_dir, "face"],
            s_databin(0x002739A0, 0x002A6120, "data"),
        [main.s_pop],
        [main.s_addr, 0x15000000-0x002ABCA0],
        [main.s_file, "game.S"],
            [main.s_str, str_s_script],
            [main.s_call, data_game],
        [main.s_write],
        [main.s_addr, 0],
        [main.s_dir, "background"],
            s_szpbin(0x002708C0, 0x002739A0, 0x000065E8, "title"),
            s_szpbin(0x002AC6B0, 0x002B8F10, 0x00020140, "a"), # 20000 + 140
            s_szpbin(0x002B8F10, 0x002C73D0, 0x00020140, "b"), # 20000 + 140
            s_szpbin(0x002C73D0, 0x002D0040, 0x00014940, "c"), # 14800 + 140
            s_szpbin(0x002D0040, 0x002D64F0, 0x00018940, "d"), # 18800 + 140
            s_szpbin(0x002D64F0, 0x002E7880, 0x00020140, "e"), # 20000 + 140
            s_szpbin(0x002E7880, 0x002F14E0, 0x00020140, "f"), # 20000 + 140
            s_szpbin(0x002F14E0, 0x002FB1B0, 0x00020140, "g"), # 20000 + 140
            s_szpbin(0x002FB1B0, 0x00301CD0, 0x00014940, "h"), # 14800 + 140
            s_szpbin(0x00301CD0, 0x0030CEC0, 0x00020140, "i"), # 20000 + 140
            s_szpbin(0x0030CEC0, 0x0031E1D0, 0x00020140, "j"), # 20000 + 140
        [main.s_pop],
        [main.s_dir, "texture"],
            # s_texture(0x0031E1D0, 0x00326E40, 0x0000C000, 0x09, "a", [
            #     d_texture_n("rgba16", 32, 32, 24),
            # ]),
            s_szpbin(0x0031E1D0, 0x00326E40, 0x0000C000, "a"),
            s_szpbin(0x00326E40, 0x0032D070, 0x0000C800, "b"),
            s_szpbin(0x0032D070, 0x00334B30, 0x0000B800, "c"),
            s_szpbin(0x00334B30, 0x0033D710, 0x0000C800, "d"),
            s_szpbin(0x0033D710, 0x00341140, 0x00008800, "e"),
            s_szpbin(0x00341140, 0x00347A50, 0x0000A000, "f"),
            s_szpbin(0x00347A50, 0x0034E760, 0x0000C800, "g"),
            s_szpbin(0x0034E760, 0x00351960, 0x00008C00, "h"),
            s_szpbin(0x00351960, 0x00357350, 0x0000C800, "i"),
            s_szpbin(0x00357350, 0x0035ED10, 0x0000C000, "j"),
            s_szpbin(0x0035ED10, 0x00365980, 0x0000C400, "k"),
            s_szpbin(0x00365980, 0x0036F530, 0x0000C800, "l"),
        [main.s_pop],
        [main.s_dir, "particle"],
            s_szpbin(0x0036F530, 0x00371C40, 0x00006D98, "a"),
        [main.s_pop],
        [main.s_dir, "stage"],
            [main.s_dir, "title"],
                s_script(0x00269EA0, 0x0026A39C, 0x14000000, 0x2D0),
                s_szpbin(0x0026A3A0, 0x0026F420, 0x0000C940, "gfx_a"),
                s_szpbin(0x0026F420, 0x002708C0, 0x000065A8, "gfx_b"),
            [main.s_pop],
            [main.s_dir, "menu"],
                s_script(0x002A6120, 0x002A65B0, 0x14000000, 0x1C4),
                s_szpbin(0x002A65B0, 0x002ABCA0, 0x0000DE60, "gfx"),
            [main.s_pop],
            s_stagebin(0x00371C40, 0x003828C0, 0x00383950, 0x00026E44, 0x5A8, "bbh"),
            s_stagebin(0x00383950, 0x00395C90, 0x00396340, 0x000237A6, 0x3DC, "ccm"),
            s_stagebin(0x00396340, 0x003CF0D0, 0x003D0DC0, 0x00079118, 0xEFC, "inside"),
            s_stagebin(0x003D0DC0, 0x003E6A00, 0x003E76B0, 0x0002B968, 0x530, "hmc"),
            s_stagebin(0x003E76B0, 0x003FB990, 0x003FC2AC, 0x000288B0, 0x5B4, "ssl"),
            s_stagebin(0x003FC2B0, 0x00405A60, 0x00405FAC, 0x000117C2, 0x43C, "bob"),
            s_stagebin(0x00405FB0, 0x0040E840, 0x0040ED64, 0x0000FA88, 0x360, "sl"),
            s_stagebin(0x0040ED70, 0x00419F90, 0x0041A75C, 0x00018788, 0x57C, "wdw"),
            s_stagebin(0x0041A760, 0x00423B20, 0x004246C4, 0x000113AC, 0x900, "jrb"),
            s_stagebin(0x004246D0, 0x0042C6E0, 0x0042CF1C, 0x0000E3BC, 0x5A4, "thi"),
            s_stagebin(0x0042CF20, 0x00437400, 0x00437868, 0x00016A20, 0x240, "ttc"),
            s_stagebin(0x00437870, 0x0044A140, 0x0044ABB4, 0x0002EE76, 0x658, "rr"),
            s_stagebin(0x0044ABC0, 0x004545E0, 0x00454E00, 0x00011878, 0x65C, "grounds"),
            s_stagebin(0x00454E00, 0x0045BF60, 0x0045C600, 0x0000FE30, 0x3B4, "bitdw"),
            s_stagebin(0x0045C600, 0x00461220, 0x004614C8, 0x0000ACC8, 0x1F0, "vcutm"),
            s_stagebin(0x004614D0, 0x0046A840, 0x0046B088, 0x00015C08, 0x4A4, "bitfs"),
            s_stagebin(0x0046B090, 0x0046C1A0, 0x0046C3A0, 0x00003330, 0x168, "sa"),
            s_stagebin(0x0046C3A0, 0x00477D00, 0x004784A0, 0x0001B7F4, 0x42C, "bits"),
            s_stagebin(0x004784A0, 0x0048C9B0, 0x0048D930, 0x000288D0, 0x9D8, "lll"),
            s_stagebin(0x0048D930, 0x00495A60, 0x00496090, 0x0000FD10, 0x450, "ddd"),
            s_stagebin(0x00496090, 0x0049DA50, 0x0049E70C, 0x00011E18, 0x7E0, "wf"),
            s_stagebin(0x0049E710, 0x004AC4B0, 0x004AC56C, 0x00027350, 0x050, "end"),
            s_stagebin(0x004AC570, 0x004AF670, 0x004AF930, 0x00006E7C, 0x1FC, "courtyard"),
            s_stagebin(0x004AF930, 0x004B7F10, 0x004B80C8, 0x0001109C, 0x0F8, "pss"),
            s_stagebin(0x004B80D0, 0x004BE9E0, 0x004BEC28, 0x0000BFA8, 0x194, "cotmc"),
            s_stagebin(0x004BEC30, 0x004C2700, 0x004C2920, 0x000089C6, 0x158, "totwc"),
            s_stagebin(0x004C2920, 0x004C41C0, 0x004C4318, 0x00002AC8, 0x0D0, "bitdwa"),
            s_stagebin(0x004C4320, 0x004CD930, 0x004CDBCC, 0x000137AE, 0x1E4, "wmotr"),
            s_stagebin(0x004CDBD0, 0x004CE9F0, 0x004CEC00, 0x00001BA0, 0x16C, "bitfsa"),
            s_stagebin(0x004CEC00, 0x004D14F0, 0x004D1910, 0x000050BC, 0x28C, "bitsa"),
            s_stagebin(0x004D1910, 0x004EB1F0, 0x004EBFFC, 0x00030474, 0x710, "ttm"),
        [main.s_pop],
        [main.s_dir, "motion_player"],
            s_databin(0x004EC000, 0x00579C20, "data"),
        [main.s_pop],
        [main.s_dir, "demo"],
            s_databin(0x00579C20, 0x0057B720, "data"),
        [main.s_pop],
        [main.s_dir, "audio"],
            s_databin(0x0057B720, 0x00593560, "ctl"),
            s_databin(0x00593560, 0x007B0860, "tbl"),
            s_databin(0x007B0860, 0x007CC620, "seq"),
            s_databin(0x007CC620, 0x007CC6C0, "bnk"),
        [main.s_pop],
    [main.s_pop],
]
