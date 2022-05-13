#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>

#include "lodepng/lodepng.h"
#include "lodepng/lodepng.cpp"

typedef struct texture
{
    const char *str;
    void (*callback)(
        FILE *f, const unsigned char *src, const unsigned char *pal,
        unsigned w, unsigned h
    );
}
TEXTURE;

static unsigned int texture_pal(
    const unsigned char *src, const unsigned char *pal, unsigned int len
)
{
    unsigned int i;
    for (i = 0; i < len; i++)
    {
        if (memcmp(src, pal + 4*i, 4) == 0) return i;
    }
    return 0;
}

#define cvt(x, n, s)    ((2*((1 << (s))-1)*(x)+0xFF) / (2*0xFF*(n)))

#define r0_8    src[0]
#define g0_8    src[1]
#define b0_8    src[2]
#define a0_8    src[3]
#define a0_4    (src[3] / 0x11)
#define a0_1    (src[3] / 0x80)
#define a1_1    (src[7] / 0x80)
#define r0(s)   cvt(src[0], 1, s)
#define g0(s)   cvt(src[1], 1, s)
#define b0(s)   cvt(src[2], 1, s)
#define a0(s)   cvt(src[3], 1, s)
#define rgb0(s) cvt(src[0]+src[1]+src[2], 3, s)
#define rgb1(s) cvt(src[4]+src[5]+src[6], 3, s)
#define pal0(s) texture_pal(src+0, pal, 1 << (s))
#define pal1(s) texture_pal(src+4, pal, 1 << (s))

#define fmt_rgba16  "0x%04X,",  \
    r0(5) << 11 | g0(5) << 6 | b0(5) << 1 | a0_1
#define fmt_rgba32  "0x%08X,",  \
    r0_8 << 24 | g0_8 << 16 | b0_8 << 8 | a0_8
#define fmt_ci4     "0x%02X,",  pal0(4) << 4 | pal1(4)
#define fmt_ci8     "0x%02X,",  pal0(8)
#define fmt_ia4     "0x%02X,",  \
    rgb0(3) << 5 | a0_1 << 4 | rgb1(3) << 1 | a1_1
#define fmt_ia8     "0x%02X,",  rgb0(4) << 4 | a0_4
#define fmt_ia16    "0x%04X,",  rgb0(8) << 8 | a0_8
#define fmt_i4      "0x%02X,",  rgb0(4) << 4 | rgb1(4)
#define fmt_i8      "0x%02X,",  rgb0(8)

#define len_rgba16  1
#define len_rgba32  1
#define len_ci4     2
#define len_ci8     1
#define len_ia4     2
#define len_ia8     1
#define len_ia16    1
#define len_i4      2
#define len_i8      1

#define TEXTURE(name)               \
static void texture_##name(         \
    FILE *f,                        \
    const unsigned char *src,       \
    const unsigned char *pal,       \
    unsigned w, unsigned h          \
)                                   \
{                                   \
    (void)pal;                      \
    do                              \
    {                               \
        unsigned i = w;             \
        do                          \
        {                           \
            fprintf(f, fmt_##name); \
            src += 4*len_##name;    \
            i   -= 1*len_##name;    \
        }                           \
        while (i > 0);              \
        fputs("\n", f);             \
    }                               \
    while (--h > 0);                \
}
TEXTURE(rgba16)
TEXTURE(rgba32)
TEXTURE(ci4)
TEXTURE(ci8)
TEXTURE(ia4)
TEXTURE(ia8)
TEXTURE(ia16)
TEXTURE(i4)
TEXTURE(i8)
#undef TEXTURE

static const TEXTURE texture_table[] =
{
#define TEXTURE(name)   {"." #name ".", texture_##name},
    TEXTURE(rgba16)
    TEXTURE(rgba32)
    TEXTURE(ci4)
    TEXTURE(ci8)
    TEXTURE(ia4)
    TEXTURE(ia8)
    TEXTURE(ia16)
    TEXTURE(i4)
    TEXTURE(i8)
#undef TEXTURE
};

int main(int argc, char *argv[])
{
    FILE *f;
    unsigned char *src;
    unsigned char *pal;
    unsigned error;
    unsigned w;
    unsigned h;
    int i;
    if (argc < 3 || argc > 4)
    {
        fprintf(stderr, "usage: %s <output> <input> [palette]\n", argv[0]);
        return 1;
    }
    if ((error = lodepng_decode32_file(&src, &w, &h, argv[2])))
    {
        fprintf(stderr, "error %u: %s\n", error, lodepng_error_text(error));
        return 1;
    }
    if (argc > 3)
    {
        unsigned pal_w;
        unsigned pal_h;
        if ((error = lodepng_decode32_file(&pal, &pal_w, &pal_h, argv[3])))
        {
            fprintf(stderr, "error %u: %s\n", error, lodepng_error_text(error));
            return 1;
        }
    }
    else
    {
        pal = NULL;
    }
    if ((f = fopen(argv[1], "w")) == NULL)
    {
        fprintf(stderr, "error: could not write '%s'\n", argv[1]);
        return 1;
    }
    for (i = 0; i < (int)(sizeof(texture_table)/sizeof(TEXTURE)); i++)
    {
        const TEXTURE *texture = &texture_table[i];
        if (strstr(argv[2], texture->str))
        {
            texture->callback(f, src, pal, w, h);
            break;
        }
    }
    fclose(f);
    free(src);
    if (pal != NULL) free(pal);
    return 0;
}
