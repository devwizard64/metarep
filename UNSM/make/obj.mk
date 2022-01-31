#define ASSERT(exp, message)
#define TEXT(x) x
#define DATA(x) x
#define BSS(x)  x
#define SECTION(addr, name, s_text, s_data, s_bss) s_text s_data s_bss
#include <meta/main.h>
