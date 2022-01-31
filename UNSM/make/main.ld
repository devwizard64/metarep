#define TEXT(x) x(.text*); . = ALIGN(0x10);
#define DATA(x) x(.data*); . = ALIGN(0x10); x(.rodata*); . = ALIGN(0x10);
#define BSS(x)  x(.bss*);  . = ALIGN(0x10);
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

#undef mips
OUTPUT_ARCH(mips)
SECTIONS
{
    __dev = 0;
    SECTION(0xA4000000, mask,
        TEXT(ULTRA/lib/PR/mask.o)
        TEXT(ULTRA/lib/PR/ipl3.o)
    ,
        DATA(ULTRA/lib/PR/ipl3.o)
    ,
    )
#include <meta/main.h>
    _stack       = stack_main + 0x400;
    _bss_start   = ADDR(.main.bss);
    _bss_size_hi = SIZEOF(.main.bss) >> 16;
    _bss_size_lo = SIZEOF(.main.bss) & 0xFFFF;
    /DISCARD/ : {*(*)}
}
