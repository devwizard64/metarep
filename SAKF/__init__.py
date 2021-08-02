import os
import struct

import main
import hvc
from hvc.meta import *

hvc.meta.c_data = "J0"
hvc.meta.c_type = 1
import SAKF.table

def mc_jsx(arg, argv):
    op, = arg
    lo, hi, ba = argv
    return [(hvc.script.c_dst, "%s %s" % (op, hvc.sym_lhb(lo, hi, ba)))]

def mc_ldf(arg, argv):
    lo, hi, ba = argv
    if hvc.script.c_dst+3 in hvc.asm.btbl:
        return None
    sym = hvc.sym_lhb(lo, hi, ba)
    if sym.startswith("$"):
        return None
    return [(hvc.script.c_dst, "ldf %s" % sym)]

mm_jss = [0xA9, None, None, 0xA2, None, 0x00, 0x22, 0x3F, 0x8C, 0x00]
mm_jms = [0xA9, None, None, 0xA2, None, 0x00, 0x5C, 0x3F, 0x8C, 0x00]
mm_jsc = [0xA9, None, None, 0xA2, None, 0x00, 0x22, 0x6D, 0x8C, 0x00]
mm_jmc = [0xA9, None, None, 0xA2, None, 0x00, 0x5C, 0x6D, 0x8C, 0x00]
mm_ldf = [0xA9, None, None, 0xA2, None, 0x00]

macro = [
    (mc_jsx, ("jss",), mm_jss),
    (mc_jsx, ("jms",), mm_jms),
    (mc_jsx, ("jsc",), mm_jsc),
    (mc_jsx, ("jmc",), mm_jmc),
    (mc_ldf, (), mm_ldf),
]

def hal_decode(src):
    dst = B""
    i = 0
    while True:
        x, = struct.unpack(">B", src[i:i+1])
        i += 1
        if x == 0xFF:
            break
        cmd = x >> 5
        siz = x & 0x1F
        if cmd == 7:
            y, = struct.unpack(">B", src[i:i+1])
            i += 1
            cmd = (x >> 2) & 7
            siz = (x & 3) << 8 | y
        siz += 1
        if cmd == 0:
            print("0 C   %02X" % siz)
            dst += src[i:i+siz]
            i += siz
        elif cmd == 1:
            dst += siz*src[i:i+1]
            i += 1
        elif cmd == 2:
            dst += siz*src[i:i+2]
            i += 2
        elif cmd == 3:
            x, = struct.unpack(">B", src[i:i+1])
            i += 1
            for x in range(x, x+siz):
                dst += struct.pack(">B", x & 0xFF)
        elif cmd == 5:
            x, = struct.unpack(">H", src[i:i+2])
            i += 2
            for x in range(x, x+siz):
                x, = struct.unpack(">B", dst[x:x+1])
                y = 0
                if x & 0x80: y |= 0x01
                if x & 0x40: y |= 0x02
                if x & 0x20: y |= 0x04
                if x & 0x10: y |= 0x08
                if x & 0x08: y |= 0x10
                if x & 0x04: y |= 0x20
                if x & 0x02: y |= 0x40
                if x & 0x01: y |= 0x80
                dst += struct.pack(">B", y)
        elif cmd == 6:
            x, = struct.unpack(">H", src[i:i+2])
            i += 2
            dst += dst[x:x-siz:-1]
        else:
            x, = struct.unpack(">H", src[i:i+2])
            i += 2
            for x in range(x, x+siz):
                dst += dst[x:x+1]
    return dst

def s_hal(self, argv):
    start, end, data = argv
    self.data[data+".hal"] = self.cache(start, end, data, hal_decode)
    self.dev = start

def s_halbin(self, argv):
    start, end, data, name = argv
    s_hal(self, [start, end, data])
    main.s_bin(self, [
        0, len(self.data[data+".hal"]), data+".hal",
        ["%s_%s.bin" % (data, name)]
    ])
    self.dev = None

def s_str_code(segment=None):
    s = ".include \"main.inc\"\n\n"
    if segment != None:
        s += (
            ".segment \"%s\"\n"
            ".a16\n"
            ".i16\n"
        ) % segment
    return [main.s_str, s]

def s_bank(start, j, e, p, name):
    return [main.s_call, [
        s_segment(name),
        s_ifdef("__J0__"),
        s_bin(start, j, "J0_%s" % name, "J0"),
        s_endif("__J0__"),
        s_ifdef("__E0__"),
        s_bin(start, e, "E0_%s" % name, "E0"),
        s_endif("__E0__"),
        s_ifdef("__P0__"),
        s_bin(start, p, "P0_%s" % name, "P0"),
        s_endif("__P0__"),
    ]]

d_mem = ["MEM", lambda: "$%02X, $%04X, $%06X, $%04X" % (
    hvc.ub(), hvc.uw(), hvc.ul(), hvc.uw()
)]

def d_mem_n(n):
    return [[n, 1, d_mem], [1, 1, hvc.asm.d_byte]]

src_code = [
    s_str_code(),
    s_code(0x008000, 0x0083E6),
    s_data(0x0083E6, 0x00842C, [
        [1, 2, "lhb"],
        [16, 1, hvc.asm.d_faraddr],
        [5, 1, ["_00841C", lambda: "$%02X, %s" % (hvc.ub(), hvc.aw())]],
        [1, 1, hvc.asm.d_byte],
    ]),
    s_code(0x00842C, 0x00869D),
    s_data(0x00869D, 0x0086E5, [[24, 3, hvc.asm.d_byte]]),
    s_code(0x0086E5, 0x008A9B),
    s_ifndef("__J0__"),
        s_code(0x008A9B, 0x008AC0, "E0"),
    s_endif("__J0__"),
    s_code(0x008A9B, 0x008AED),
    s_data(0x008AED, 0x008B8D, [
        [10, 4, hvc.asm.d_word],
        [4, 4, hvc.asm.d_word],
        [1, 8, hvc.asm.d_byte],
        [4, 4, hvc.asm.d_word],
        [1, 8, hvc.asm.d_byte],
    ]),
    s_code(0x008B8D, 0x008D12),
    s_ifndef("__J0__", 1, -1),
        s_code(0x008D37, 0x008D4F, "E0"),
        s_data(0x008D4F, 0x008D6F, [[4, 4, hvc.asm.d_word]], "E0"),
    s_endif("__J0__"),
    s_data(0x008D12, 0x008D28, "addr"),
    s_code(0x008D28, 0x008F5A),
    s_data(0x008F5A, 0x008F62, "addr"),
    s_code(0x008F62, 0x009287),
    s_data(0x009287, 0x00930B, "addr"),
    s_code(0x00930B, 0x009384),
    s_data(0x009384, 0x0093F6, "addr"),
    s_code(0x0093F6, 0x009672),
    s_data(0x009672, 0x00967A, "addr"),
    s_code(0x00967A, 0x009C58),
    s_data(0x009C58, 0x009C5E, "addr"),
    s_code(0x009C5E, 0x009CCF),
    s_data(0x009CCF, 0x009CDF, "word"),
    s_code(0x009CDF, 0x00B762),
    s_data(0x00B762, 0x00B776, [[4, 5, hvc.asm.d_byte]]),
    s_code(0x00B776, 0x00B7F0),
    s_data(0x00B7F0, 0x00BBCC, [
        [24, 1, hvc.asm.d_faraddr],
        [229, 2, hvc.asm.d_word],
    ]),
    s_code(0x00BBCC, 0x00BC3E),
    s_data(0x00BC3E, 0x00BC71, "faraddr"),
    s_code(0x00BC71, 0x00BD25),
    s_data(0x00BD25, 0x00BD86, "byte"),
    s_code(0x00BD86, 0x00BE3C),
    s_data(0x00BE3C, 0x00BE45, [[3, 3, hvc.asm.d_byte]]),
    s_code(0x00BE45, 0x00BE66),
    s_data(0x00BE66, 0x00BE6C, [[2, 3, hvc.asm.d_byte]]),
    s_code(0x00BE6C, 0x00BF58),
    s_data(0x00BF58, 0x00BF66, [[2, 7, hvc.asm.d_byte]]),
    s_code(0x00BF66, 0x00BF8B),
    s_data(0x00BF8B, 0x00BF99, "addr"),
    s_code(0x00BF99, 0x00C0D2),
    s_ifndef("__J0__"),
        s_code(0x00C12F, 0x00C133, "E0"),
    s_endif("__J0__"),
    s_code(0x00C0D2, 0x00C247),
    s_data(0x00C247, 0x00C251, "addr"),
    s_code(0x00C251, 0x00C324),
    s_data(0x00C324, 0x00C347, [
        [1, d_mem_n(4)],
        [1, 1, hvc.asm.d_word],
    ]),
    s_code(0x00C347, 0x00C35C),
    s_data(0x00C35C, 0x00C36E, "addr"),
    s_code(0x00C36E, 0x00C6DE),
    s_data(0x00C6DE, 0x00C6E5, [[1, 7, hvc.asm.d_byte]]),
    s_code(0x00C6E5, 0x00C7F1),
    s_data(0x00C7F1, 0x00C7F7, "addr"),
    s_code(0x00C7F7, 0x00C926),
    s_data(0x00C926, 0x00C92E, "addr"),
    s_code(0x00C92E, 0x00C970),
    s_data(0x00C970, 0x00CA9C, [[25, 12, hvc.asm.d_byte]]),
    s_code(0x00CA9C, 0x00CB2F),
    s_ifndef("__J0__"),
        s_code(0x00CB90, 0x00CB9A, "E0"),
    s_endif("__J0__"),
    s_code(0x00CB2F, 0x00CD05),
    s_data(0x00CD05, 0x00CD1E, d_mem_n(3)),
    s_code(0x00CD1E, 0x00CD81),
    s_data(0x00CD81, 0x00CDCB, [
        [1, 47, "ascii"],
        [1, 27, "ascii"],
    ]),
    s_code(0x00CDCB, 0x00D632),
    s_data(0x00D632, 0x00D77C, "faraddr"),
    s_data(0x00D77C, 0x00D7BD, "byte"),
    s_code(0x00D7BD, 0x00DA93),
    s_data(0x00DA93, 0x00DAE9, [[43, 1, hvc.asm.d_word]]),
    s_code(0x00DAE9, 0x00DC18),
    s_data(0x00DC18, 0x00DC20, "addr"),
    s_code(0x00DC20, 0x00DDA7),
    s_data(0x00DDA7, 0x00DDBB, [
        [1, d_mem_n(1)],
        [1, 1, hvc.asm.d_word],
        [1, d_mem_n(1)],
    ]),
    s_code(0x00DDBB, 0x00EA23),
    s_data(0x00EA23, 0x00EA45, "word"),
    s_code(0x00EA45, 0x00EA5D),
    s_data(0x00EA5D, 0x00EA73, "addr"),
    s_code(0x00EA73, 0x00EBE4),
    s_data(0x00EBE4, 0x00EBE8, "word"),
    s_code(0x00EBE8, 0x00ED73),
    s_data(0x00ED73, 0x00ED81, [[2, 7, hvc.asm.d_byte]]),
    s_code(0x00ED81, 0x00EDC2),
    s_data(0x00EDC2, 0x00EDC8, "addr"),
    s_code(0x00EDC8, 0x00EEC6),
    s_data(0x00EEC6, 0x00EEC9, [[3, 1, hvc.asm.d_byte]]),
    s_code(0x00EEC9, 0x00F082),
    s_data(0x00F082, 0x00F091, [[5, 3, hvc.asm.d_byte]]),
    s_code(0x00F091, 0x00F11A),
]

src_header = [
    [main.s_str, """
.ifdef __J0__
.define REGCODE "J"
.define REGION  $00
.define VERSION 0
.endif /* __J0__ */
.ifdef __E0__
.define REGCODE "E"
.define REGION  $01
.define VERSION 0
.endif /* __E0__ */
.ifdef __P0__
.define REGCODE "P"
.define REGION  $02
.define VERSION 0
.endif /* __P0__ */
"""],
    s_segment("HEADER"),
    s_data(0x00FFC0, 0x00FFD9, [[1, 21, "ascii"], [4, 1, hvc.asm.d_byte]]),
    [main.s_str, "\t.byte REGION\n"],
    s_data(0x00FFDA, 0x00FFDB, "byte"),
    [main.s_str, "\t.byte VERSION\n"],
    [main.s_str, "\t.word $FFFF, $0000\n"],
    s_data(0x00FFE0, 0x010000, "addr"),
    [main.s_str, "\n"],
    s_segment("REGISTRY"),
    s_data(0x00FFB0, 0x00FFB4, [[1, 2, "ascii"], [1, 3, "ascii"]]),
    [main.s_str, "\t.byte REGCODE\n"],
    [main.s_str, "\t.res 7, 0\n"],
    s_data(0x00FFBD, 0x00FFC0, [[3, 1, hvc.asm.d_byte]]),
]

src_code_01 = [
    s_str_code("CODE_01"),
    s_code(0x018000, 0x0181C0),
    s_data(0x0181C0, 0x0181C6, "addr"),
    s_code(0x0181C6, 0x0183BC),
    s_data(0x0183BC, 0x0183C2, "word"),
    s_code(0x0183C2, 0x018479),
    s_data(0x018479, 0x0184DA, [
        [1, d_mem_n(1)],
        [1, d_mem_n(3)],
        [7, d_mem_n(1)],
    ]),
    s_code(0x0184DA, 0x018574),
    s_data(0x018574, 0x01857A, "addr"),
    s_code(0x01857A, 0x018610),
    s_data(0x018610, 0x018654, [[4, d_mem_n(2)]]),
    s_code(0x018654, 0x01875A),
    s_data(0x01875A, 0x018768, "addr"),
    s_code(0x018768, 0x01897B),
    s_data(0x01897B, 0x0189F3, "word"),
    s_code(0x0189F3, 0x018B1E),
    s_data(0x018B1E, 0x018B30, [[1, 9, hvc.asm.d_word]]),
    s_code(0x018B30, 0x018F2E),
    s_data(0x018F2E, 0x018F40, [[1, 9, hvc.asm.d_word]]),
    s_code(0x018F40, 0x019A15),
    s_data(0x019A15, 0x019A21, "addr"),
    s_code(0x019A21, 0x019C48),
    s_data(0x019C48, 0x019C64, [[2, 7, hvc.asm.d_word]]),
    s_code(0x019C64, 0x019DEF),
    s_data(0x019DEF, 0x019E13, [[6, 6, hvc.asm.d_byte]]),
    s_code(0x019E13, 0x01A049),
    s_data(0x01A049, 0x01A07F, [[9, 3, hvc.asm.d_word]]),
    s_code(0x01A07F, 0x01A568),
    s_data(0x01A568, 0x01A588, "addr"),
    s_code(0x01A588, 0x01A6AF),
    s_data(0x01A6AF, 0x01A6B7, "addr"),
    s_code(0x01A6B7, 0x01A806),
    s_data(0x01A806, 0x01A82B, [
        [17, 1, hvc.asm.d_word],
        [1, 3, hvc.asm.d_byte],
    ]),
    s_code(0x01A82B, 0x01A98D),
    s_data(0x01A98D, 0x01A995, [[4, 2, hvc.asm.d_byte]]),
    s_code(0x01A995, 0x01AB55),
    s_data(0x01AB55, 0x01AB6D, [[3, 4, hvc.asm.d_word]]),
    s_code(0x01AB6D, 0x01AC91),
    s_data(0x01AC91, 0x01ACBD, "addr"),
    s_code(0x01ACBD, 0x01ADAA),
    s_data(0x01ADAA, 0x01ADB2, "addr"),
    s_code(0x01ADB2, 0x01AE7F),
    s_data(0x01AE7F, 0x01AF77, [[31, 4, hvc.asm.d_word]]),
    s_code(0x01AF77, 0x01AFAF),
    s_data(0x01AFAF, 0x01AFFF, "addr"),
    s_data(0x01AFFF, 0x01B04F, "word"),
    s_code(0x01B04F, 0x01B067),
    s_data(0x01B067, 0x01B08F, "word"),
    s_code(0x01B08F, 0x01B0A6),
    s_data(0x01B0A6, 0x01B0CE, "word"),
    s_code(0x01B0CE, 0x01B0E6),
    s_data(0x01B0E6, 0x01B10E, "word"),
    s_code(0x01B10E, 0x01B125),
    s_data(0x01B125, 0x01B14D, "word"),
    s_code(0x01B14D, 0x01B188),
    s_data(0x01B188, 0x01B200, "word"),
    s_code(0x01B200, 0x01B23B),
    s_data(0x01B23B, 0x01B2B3, "word"),
    s_code(0x01B2B3, 0x01B2EE),
    s_data(0x01B2EE, 0x01B366, "word"),
    s_code(0x01B366, 0x01B3A1),
    s_data(0x01B3A1, 0x01B419, "word"),
    s_code(0x01B419, 0x01B5CE),
    s_data(0x01B5CE, 0x01B5FE, "word"),
    s_code(0x01B5FE, 0x01B663),
    s_data(0x01B663, 0x01B66F, "addr"),
    s_code(0x01B66F, 0x01B989),
    s_data(0x01B989, 0x01B9AF, "word"),
    s_data(0x01B9AF, 0x01B9BF, "word"),
    s_code(0x01B9BF, 0x01BAC6),
    s_data(0x01BAC6, 0x01BADE, [[4, 3, hvc.asm.d_word]]),
    s_code(0x01BADE, 0x01BC92),
    s_data(0x01BC92, 0X01C1E0), # word
    s_code(0x01C1E0, 0x01C23A),
    s_data(0x01C23A, 0x01C362), # word
    s_code(0x01C362, 0x01C38E),
    s_data(0x01C38E, 0x01C3AE, "addr"),
    s_code(0x01C3AE, 0x01C466),
    s_data(0x01C466, 0x01C486, "addr"),
    s_code(0x01C486, 0x01C551),
    s_data(0x01C551, 0x01C571, "addr"),
    s_code(0x01C571, 0x01C64D),
    s_data(0x01C64D, 0x01C66D, "addr"),
    s_code(0x01C66D, 0x01C6A0),
    s_data(0x01C6A0, 0x01C6C0, "addr"),
    s_code(0x01C6C0, 0x01C6EB),
    s_data(0x01C6EB, 0x01C70B, "addr"),
    s_code(0x01C70B, 0x01C747),
    s_data(0x01C747, 0x01C767, "addr"),
    s_code(0x01C767, 0x01C845),
    s_data(0x01C845, 0x01C865, "addr"),
    s_code(0x01C865, 0x01C966),
    s_data(0x01C966, 0x01C986, "addr"),
    s_code(0x01C986, 0x01CA95),
    s_data(0x01CA95, 0x01CAB5, "addr"),
    s_code(0x01CAB5, 0x01CB50),
    s_data(0x01CB50, 0x01CB70, "addr"),
    s_code(0x01CB70, 0x01CC1A),
    s_data(0x01CC1A, 0x01CC3A, "addr"),
    s_code(0x01CC3A, 0x01CF2D),
    s_data(0x01CF2D, 0x01D186, [
        [27, 3, hvc.asm.d_byte],
        [1, 8, hvc.asm.d_byte],
        [64, 4, hvc.asm.d_word],
    ]),
    s_data(0x01D186, 0x01DF4E), #
    s_code(0x01DF4E, 0x01E06C),
    s_data(0x01E06C, 0x01E06E),
    s_code(0x01E06E, 0x01E0D6),
    s_data(0x01E0D6, 0x01E116, "addr"),
    s_code(0x01E116, 0x01E51C),
    s_data(0x01E51C, 0x01E534, "word"),
    s_code(0x01E534, 0x01E71B),
    s_data(0x01E71B, 0x01E73F, [[6, 3, hvc.asm.d_word]]),
    s_code(0x01E73F, 0x01E911),
    s_data(0x01E911, 0x01E912, "byte"),
    s_code(0x01E912, 0x01EA6E),
    s_data(0x01EA6E, 0x01EA84, "addr"),
    s_code(0x01EA84, 0x01EA8A),
    s_data(0x01EA8A, 0x01EA92, "addr"),
    s_code(0x01EA92, 0x01EBD0),
    s_data(0x01EBD0, 0x01EBE2, [[2, d_mem_n(1)]]),
    s_code(0x01EBE2, 0x01EBE8),
    s_data(0x01EBE8, 0x01EBF0, "addr"),
    s_code(0x01EBF0, 0x01ED32),
    s_data(0x01ED32, 0x01ED56, [[4, d_mem_n(1)]]),
    s_code(0x01ED56, 0x01EF17),
    s_data(0x01EF17, 0x01EF23, "word"),
    s_code(0x01EF23, 0x01EFD8),
    s_data(0x01EFD8, 0x01EFF9, d_mem_n(4)),
    s_code(0x01EFF9, 0x01F01C),
    s_data(0x01F01C, 0x01F024, "addr"),
    s_code(0x01F024, 0x01F13C),
    s_data(0x01F13C, 0x01F14E, [[2, d_mem_n(1)]]),
    s_code(0x01F14E, 0x01F173),
    s_data(0x01F173, 0x01F17D, "addr"),
    s_code(0x01F17D, 0x01F43E),
    s_data(0x01F43E, 0x01F446, "addr"),
    s_code(0x01F446, 0x01F593),
    s_data(0x01F593, 0x01F5BA, "faraddr"),
    s_code(0x01F5BA, 0x01F63A),
    s_data(0x01F63A, 0x01F642, "addr"),
    s_code(0x01F642, 0x01F6B8),
    s_data(0x01F6B8, 0x01F6F7, "faraddr"),
    s_code(0x01F6F7, 0x01F7BE),
    s_data(0x01F7BE, 0x01F7CF, d_mem_n(2)),
    s_data(0x01F7CF, 0x01F7D5, "word"),
    s_code(0x01F7D5, 0x01F863),
    s_data(0x01F863, 0x01F86C, "byte"),
    s_code(0x01F86C, 0x01FD77),
    s_data(0x01FD77, 0x01FFD8, [
        [154, 1, hvc.asm.d_faraddr],
        [1, d_mem_n(2)],
        [1, 1, hvc.asm.d_byte],
        [40, 1, hvc.asm.d_faraddr],
        [1, d_mem_n(1)],
    ]),
]

src_bank = [
    # s_bank(0x000000, 0x00711A, 0x007185, 0x007185, "CODE"),
    # s_bank(0x008000, 0x00FFD7, 0x00FFE6, 0x00FFD5, "CODE_01"),
    s_bank(0x010000, 0x017266, 0x017A81, 0x017A81, "CODE_02"),
    s_bank(0x018000, 0x01F81A, 0x01F8D0, 0x01F8D0, "CODE_03"),
    s_bank(0x020000, 0x027FC2, 0x027FC8, 0x027FC8, "CODE_04"),
    s_bank(0x028000, 0x02FA8E, 0x02FA93, 0x02FA93, "CODE_05"),
    s_bank(0x030000, 0x0373FF, 0x037BFF, 0x037BFF, "BANK_06"),
    s_bank(0x038000, 0x03F8AA, 0x03FA8F, 0x03F99C, "BANK_07"),
    s_bank(0x040000, 0x04FBF7, 0x04FBF7, 0x04FBF7, "BANK_C4"),
    s_bank(0x050000, 0x05FB64, 0x05FB64, 0x05FB64, "BANK_C5"),
    s_bank(0x060000, 0x06FEF2, 0x06FEF2, 0x06FEF2, "BANK_C6"),
    s_bank(0x070000, 0x07F58E, 0x07F98E, 0x07F98E, "BANK_C7"),
    s_bank(0x080000, 0x08FB92, 0x08FB92, 0x08FB92, "BANK_C8"),
    s_bank(0x090000, 0x09F988, 0x09FFC7, 0x09FFB5, "CODE_C9"),
    s_bank(0x0A0000, 0x0AF7CD, 0x0AF814, 0x0AF7FE, "BANK_CA"),
    s_bank(0x0B0000, 0x0BFB22, 0x0BFBF9, 0x0BFBFA, "BANK_CB"),
    s_bank(0x0C0000, 0x0CF19F, 0x0CF0EB, 0x0CF0EB, "BANK_CC"),
    s_bank(0x0D0000, 0x0DF9AC, 0x0DF9C5, 0x0DF9C5, "BANK_CD"),
    s_bank(0x0E0000, 0x0EF959, 0x0EF86E, 0x0EF86E, "BANK_CE"),
    s_bank(0x0F0000, 0x0FFF14, 0x0FFF9A, 0x0FFF9A, "CODE_CF"),
    s_bank(0x100000, 0x10FC13, 0x10FC5B, 0x10FC5B, "CODE_D0"),
    s_bank(0x110000, 0x11F9A7, 0x11F9B9, 0x11F9C4, "BANK_D1"),
    s_bank(0x120000, 0x12FC82, 0x12FC79, 0x12FC79, "BANK_D2"),
    s_bank(0x130000, 0x13FF0C, 0x13FFAC, 0x13FFAC, "CODE_D3"),
    s_bank(0x140000, 0x14F773, 0x14FC42, 0x14FC42, "BANK_D4"),
    s_bank(0x150000, 0x15FD4F, 0x15FD5B, 0x15FD5B, "CODE_D5"),
    s_bank(0x160000, 0x2FFB0B, 0x2FE984, 0x2FE944, "BANK_D6"),
    s_bank(0x300000, 0x30FD45, 0x30F77D, 0x30F77D, "BANK_F0"),
    s_bank(0x310000, 0x31FFFC, 0x31FFF2, 0x31FFF2, "BANK_F1"),
    s_bank(0x320000, 0x32FFFD, 0x32FFFC, 0x32FFFC, "BANK_F2"),
    s_bank(0x330000, 0x33FFE4, 0x33FFFE, 0x33FFFE, "BANK_F3"),
    s_bank(0x340000, 0x34FFF8, 0x34FFEB, 0x34FFEB, "BANK_F4"),
    s_bank(0x350000, 0x35FFF5, 0x35FFF9, 0x35FFF9, "BANK_F5"),
    s_bank(0x360000, 0x36FFE0, 0x36FFF6, 0x36FFF6, "BANK_F6"),
    s_bank(0x370000, 0x37FFFB, 0x37FFFA, 0x37FFFA, "BANK_F7"),
    s_bank(0x380000, 0x38FFFB, 0x38FFFC, 0x38FFFC, "BANK_F8"),
    s_bank(0x390000, 0x39FFF0, 0x39FFF0, 0x39FFF0, "BANK_F9"),
    s_bank(0x3A0000, 0x3AFFFD, 0x3AFFFD, 0x3AFFFD, "BANK_FA"),
    s_bank(0x3B0000, 0x3BFFE9, 0x3BFFE2, 0x3BFFE2, "BANK_FB"),
    s_bank(0x3C0000, 0x3CFFED, 0x3CFFED, 0x3CFFED, "BANK_FC"),
    s_bank(0x3D0000, 0x3DFFFB, 0x3DFFFB, 0x3DFFFB, "BANK_FD"),
    s_bank(0x3E0000, 0x3EFFF0, 0x3EFFF0, 0x3EFFF0, "BANK_FE"),
    s_bank(0x3F0000, 0x3FFFFC, 0x3FFFFC, 0x3FFFFC, "BANK_FF"),
]

lst = [
    [main.s_data, "J0", ["donor", "SAKFJ0.sfc"]],
    [main.s_data, "E0", ["donor", "SAKFE0.sfc"]],
    [main.s_data, "P0", ["donor", "SAKFP0.sfc"]],
    [main.s_dir, "src"],
        s_file(0x008000-0x000000, "code.s",    src_code),
        s_file(0x008000-0x000000, "header.s",  src_header),
        s_file(0x018000-0x008000, "code_01.s", src_code_01),
        s_file(0x000000-0x000000, "bank.s",    src_bank),
    [main.s_pop],
]
