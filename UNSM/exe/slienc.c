#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>

#define false   0
#define true    1
#define MIN(a, b)               ((a) < (b) ? (a) : (b))
#define MAX(a, b)               ((a) > (b) ? (a) : (b))
typedef unsigned int uint;
typedef uint8_t u8;

#define SIG_0   'M'
#define SIG_1   'I'
#define SIG_2   'O'
#define SIG_3   '0'
#define BLK_OL  1
#define BLK_SL  3
#define BLK_OH  (BLK_OL+0x0FFF)
#define BLK_SH  (BLK_SL+0x000F)

#define slitbl()                        \
{                                       \
    ti++;                               \
}
#define slicpy()                        \
{                                       \
    *c++ = data[i++];                   \
    tbl[ti/8] |= 1 << (7-(ti & 7));     \
}
#define slipkt()                        \
{                                       \
    *p++ = x >> 8 | (sz-BLK_SL) << 4;   \
    *p++ = x >> 0;                      \
}

static uint sliblk(const u8 *data, uint size, uint i, uint *of, uint *sz)
{
    uint o  = MAX(0, (int)i-BLK_OH);
    uint ms = MIN(BLK_SH, size-i);
    uint found = false;
    while (o < i && *sz < ms)
    {
        uint s = 0;
        uint n = 0;
        while (o+s < i+ms && s < ms)
        {
            if (data[i+s] != data[o+s < i ? o+s : o+(s%n)])
            {
                break;
            }
            if (o+s < i)
            {
                n++;
            }
            s++;
        }
        if (*sz < s)
        {
            *of = o;
            *sz = s;
            found = true;
        }
        o++;
    }
    return found;
}

int main(int argc, const char **argv)
{
    FILE *f;
    char *str;
    u8   *data;
    u8   *tbl;
    u8   *pkt;
    u8   *cpy;
    u8   *p;
    u8   *c;
    uint  size;
    uint  i;
    uint  ti;
    uint  pi;
    uint  ci;
    uint  po;
    uint  co;
    u8    buf[0x10];
    if (argc != 4)
    {
        fprintf(stderr, "usage: %s <output> <input> <sym>\n", argv[0]);
        return EXIT_FAILURE;
    }
    f = fopen(argv[3], "r");
    if (f == NULL)
    {
        fprintf(stderr, "error: could not read '%s'\n", argv[3]);
        return EXIT_FAILURE;
    }
    str = malloc(0x1000);
    i    = ~0;
    size = 0;
    while (fgets(str, 0x1000, f) != NULL)
    {
        uint x;
        uint y;
        sscanf(str, "%*s %*s %X %X", &x, &y);
        if (i > x)
        {
            i = x;
        }
        if (size < x+y)
        {
            size = x+y;
        }
    }
    free(str);
    size -= i;
    data = malloc(size);
    f = fopen(argv[2], "rb");
    if (f == NULL)
    {
        fprintf(stderr, "error: could not read '%s'\n", argv[2]);
        return EXIT_FAILURE;
    }
    fread(data, 1, size, f);
    fclose(f);
    ti = (size+7) / 8;
    tbl =     malloc(ti);
    pkt = p = malloc(size);
    cpy = c = malloc(size);
    memset(tbl, 0x00, ti);
    ti = 0;
    i = 0;
    while (i < size)
    {
        uint of;
        uint sz;
        sz = 2;
        if (sliblk(data, size, i, &of, &sz))
        {
            uint ofn;
            uint szn;
            uint x;
            if (szn = sz+1, sliblk(data, size, i+1, &ofn, &szn))
            {
                slicpy();
                slitbl();
                of = ofn;
                sz = szn;
            }
            x = i-of-BLK_OL;
            slipkt();
            slitbl();
            i += sz;
        }
        else
        {
            slicpy();
            slitbl();
        }
    }
    ti = (ti+7) / 8;
    ti = (ti+3) & ~3;
    pi = p-pkt;
    ci = c-cpy;
    po = 0x10 + ti;
    co = po   + pi;
    buf[0x00] = SIG_0;
    buf[0x01] = SIG_1;
    buf[0x02] = SIG_2;
    buf[0x03] = SIG_3;
    buf[0x04] = size >> 24;
    buf[0x05] = size >> 16;
    buf[0x06] = size >>  8;
    buf[0x07] = size >>  0;
    buf[0x08] = po   >> 24;
    buf[0x09] = po   >> 16;
    buf[0x0A] = po   >>  8;
    buf[0x0B] = po   >>  0;
    buf[0x0C] = co   >> 24;
    buf[0x0D] = co   >> 16;
    buf[0x0E] = co   >>  8;
    buf[0x0F] = co   >>  0;
    f = fopen(argv[1], "wb");
    if (f == NULL)
    {
        fprintf(stderr, "error: could not write '%s'\n", argv[1]);
        return EXIT_FAILURE;
    }
    fwrite(buf, 1, sizeof(buf), f);
    fwrite(tbl, 1, ti, f);
    fwrite(pkt, 1, pi, f);
    fwrite(cpy, 1, ci, f);
    fclose(f);
    free(data);
    free(tbl);
    free(cpy);
    free(pkt);
    return EXIT_SUCCESS;
}
