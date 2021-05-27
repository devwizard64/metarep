#define ASSERT(exp, message)
#define TEXT(fn)    fn
#define DATA(fn)    fn
#define BSS(fn)     fn
#define SECTION(addr, name, section) section
#define CODE(addr, name, code, bss) code bss
#define BUFFER(addr, name, bss) bss
#include "main.h"
