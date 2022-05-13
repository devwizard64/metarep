#define TEXT(x) x(.text*); . = ALIGN(16);
#define DATA(x) x(.data*); . = ALIGN(16); x(.rodata*); . = ALIGN(16);
#define BSS(x)  x(.bss*);  . = ALIGN(16);
#define SECTION(addr, name, s_text, s_data, s_bss)                      \
    _##name##SegmentRomStart  = __dev;                                  \
    _##name##SegmentStart     = ADDR(.name.text);                       \
    _##name##SegmentTextStart = ADDR(.name.text);                       \
    .name.text (addr)  : AT(__dev) {s_text}                             \
    _##name##SegmentTextEnd   = ADDR(.name.text) + SIZEOF(.name.text);  \
    __dev += SIZEOF(.name.text);                                        \
    _##name##SegmentDataStart = ADDR(.name.data);                       \
    .name.data         : AT(__dev) {s_data}                             \
    _##name##SegmentDataEnd   = ADDR(.name.data) + SIZEOF(.name.data);  \
    __dev += SIZEOF(.name.data);                                        \
    _##name##SegmentBssStart  = ADDR(.name.bss);                        \
    .name.bss (NOLOAD) : AT(__dev) {s_bss}                              \
    _##name##SegmentBssEnd    = ADDR(.name.bss)  + SIZEOF(.name.bss);   \
    _##name##SegmentEnd       = ADDR(.name.bss)  + SIZEOF(.name.bss);   \
    _##name##SegmentRomEnd    = __dev;

OUTPUT_ARCH(mips)
SECTIONS
{
    .makerom 0xA4000000 : AT(0)
    {
        ULTRA/lib/PR/romheader.o(.text);
        . = ALIGN(64);
        ULTRA/lib/PR/Boot.o(.text);
        ULTRA/lib/PR/font.o(.data);
        . = ALIGN(0x1000);
    }
    __dev = 0x1000;
#include <meta/main.h>
    _bss_size_hi = SIZEOF(.code.bss) >> 16;
    _bss_size_lo = SIZEOF(.code.bss) & 0xFFFF;
    /DISCARD/ : {*(*)}
}
