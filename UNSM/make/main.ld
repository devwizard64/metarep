#define TEXT(fn)    fn(.text*); . = ALIGN(0x10);
#define DATA(fn)    fn(.data*); . = ALIGN(0x10); fn(.rodata*); . = ALIGN(0x10);
#define BSS(fn)     fn(.bss*);  . = ALIGN(0x10);
#define SECTION(addr, name, section)        \
    name##_start = __dev;                   \
    .name addr : AT(__dev) SUBALIGN(0x10)   \
    {section}                               \
    __dev += SIZEOF(.name);                 \
    name##_end = __dev;
#define SECTION_NOLOAD(name, section)       \
    .name.noload (NOLOAD) : SUBALIGN(0x10)  \
    {section}
#define CODE(addr, name, code, bss)                                     \
    code_##name##_start = ADDR(.name);                                  \
    SECTION(addr, name, code)                                           \
    code_##name##_end = ADDR(.name) + SIZEOF(.name);                    \
    bss_##name##_start = ADDR(.name.noload);                            \
    SECTION_NOLOAD(name, bss)                                           \
    bss_##name##_end = ADDR(.name.noload) + SIZEOF(.name.noload);       \
    bss_##name##_size = SIZEOF(.name.noload);

#define FILE(addr, name, fn)    \
    SECTION(                    \
        addr, data_##name,      \
        TEXT(BUILD/data/fn.o)   \
        DATA(BUILD/data/fn.o)   \
    )
#define SCRIPT(addr, name)              \
    SECTION(                            \
        addr, data_stage_##name,        \
        TEXT(BUILD/data/stage/name/s.o) \
        TEXT(BUILD/data/stage/name/g.o) \
        DATA(BUILD/data/stage/name/s.o) \
        DATA(BUILD/data/stage/name/g.o) \
    )
#define SZP(name, fn)   SECTION(0, szp_##name, DATA(BUILD/data/fn.szp.o))

#undef mips
OUTPUT_ARCH(mips)
SECTIONS
{
    __dev = 0;
#include "symbol.h"
    SECTION(
        0xA4000000, boot,
        TEXT(BUILD/src/header.o)
        TEXT(ultra/lib/PR/ipl3.o)
    )
#include "main.h"
    bss_main_size_hi = bss_main_size >> 16;
    bss_main_size_lo = bss_main_size & 0xFFFF;
    /DISCARD/ : {*(*);}
}
