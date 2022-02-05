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
#define lenof(x)                (sizeof((x)) / sizeof((x)[0]))

#define SIG     "MIO0"
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
            if (data[i+s] != data[o+s < i ? o+s : o+(s%n)]) break;
            if (o+s < i) n++;
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
    char str[0x1000];
    FILE *f;
    FILE *s;
    FILE *h;
    u8 *data;
    u8 *tbl;
    u8 *pkt;
    u8 *cpy;
    u8 *p;
    u8 *c;
    uint size;
    uint i;
    uint ti;
    uint pi;
    uint ci;
    uint po;
    uint co;
    u8 buf[0x10];
    if (argc != 6)
    {
        fprintf(
            stderr, "usage: %s <a.s> <a.h> <a.szp> <a.bin> <a.sym>\n", argv[0]
        );
        return EXIT_FAILURE;
    }
    if ((f = fopen(argv[5], "r")) == NULL)
    {
        fprintf(stderr, "error: could not read '%s'\n", argv[5]);
        return EXIT_FAILURE;
    }
    if ((s = fopen(argv[1], "w")) == NULL)
    {
        fprintf(stderr, "error: could not write '%s'\n", argv[1]);
        return EXIT_FAILURE;
    }
    if ((h = fopen(argv[2], "w")) == NULL)
    {
        fprintf(stderr, "error: could not write '%s'\n", argv[2]);
        return EXIT_FAILURE;
    }
    i = ~0;
    size = 0;
    while (fgets(str, lenof(str), f) != NULL)
    {
        char sym[lenof(str)];
        char sec;
        uint adr;
        uint siz;
        sscanf(str, "%s %c %x %x", sym, &sec, &adr, &siz);
        if (i    > adr    ) i    = adr;
        if (size < adr+siz) size = adr+siz;
        if (sec < 'a')
        {
            fprintf(s, ".globl %s; %s = 0x%08X\n", sym, sym, adr);
            fprintf(h, "#define %s 0x%08X\n", sym, adr);
        }
    }
    fprintf(s, ".data\n.incbin \"%s\"\n", argv[3]);
    fclose(f);
    fclose(s);
    fclose(h);
    size -= i;
    data = malloc(size);
    if ((f = fopen(argv[4], "rb")) == NULL)
    {
        fprintf(stderr, "error: could not read '%s'\n", argv[4]);
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
    buf[0x00] = SIG[0];
    buf[0x01] = SIG[1];
    buf[0x02] = SIG[2];
    buf[0x03] = SIG[3];
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
    if ((f = fopen(argv[3], "wb")) == NULL)
    {
        fprintf(stderr, "error: could not write '%s'\n", argv[3]);
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
