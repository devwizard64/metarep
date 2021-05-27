#define TEXT(fn)    fn(.text*); . = ALIGN(0x10);
#define DATA(fn)    fn(.data*); . = ALIGN(0x10); fn(.rodata*); . = ALIGN(0x10);
#define BSS(fn)     fn(.bss*);  . = ALIGN(0x10);
#define SECTION(addr, name, section)        \
    name##_start = __dev;                   \
    .name addr : AT(__dev)                  \
    {section}                               \
    __dev += SIZEOF(.name);                 \
    name##_end = __dev;
#define SECTION_NOLOAD(addr, name, section) \
    .name.noload addr (NOLOAD) : AT(__dev)  \
    {section}
#define CODE(addr, name, code, bss)                                     \
    code_##name##_start = ADDR(.name);                                  \
    SECTION(addr, name, code)                                           \
    code_##name##_end = ADDR(.name) + SIZEOF(.name);                    \
    bss_##name##_start = ADDR(.name.noload);                            \
    SECTION_NOLOAD(, name, bss)                                         \
    bss_##name##_end = ADDR(.name.noload) + SIZEOF(.name.noload);       \
    bss_##name##_size = SIZEOF(.name.noload);
#define BUFFER(addr, name, bss)                                         \
    bss_##name##_start = ADDR(.name.noload);                            \
    SECTION_NOLOAD(addr, name, bss)                                     \
    bss_##name##_end = ADDR(.name.noload) + SIZEOF(.name.noload);       \
    bss_##name##_size = SIZEOF(.name.noload);

#undef mips
OUTPUT_ARCH(mips)
SECTIONS
{
    __dev = 0;
#include "main.h"
    bss_main_size_hi = bss_main_size >> 16;
    bss_main_size_lo = bss_main_size & 0xFFFF;
    /DISCARD/ : {*(*);}
}
