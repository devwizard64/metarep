#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>

#define MIN(a, b)               ((a) < (b) ? (a) : (b))
typedef unsigned int uint;
typedef uint8_t u8;
typedef uint32_t u32;

static void crc(char *buf, const u8 *data, uint size)
{
    u32   c0;
    u32   c1;
    u32   c0a;
    u32   c0b;
    u32   c1a;
    u32   c1b;
    uint  i;
    c0 = c1 = c0a = c0b = c1a = c1b = 0xF8CA4DDC;
    for (i = 0; i < size; i += 4)
    {
        u32 x;
        u32 o;
        u32 s;
        u32 r;
        x = data[i+0] << 24 | data[i+1] << 16 | data[i+2] << 8 | data[i+3];
        o = c0 + x;
        if (o < c0) c0a++;
        s    = x & 0x1F;
        r    = x << s | x >> (32-s);
        c0   = o;
        c0b ^= x;
        c1  += r;
        c1a ^= c1a < x ? c0^x : r;
        c1b += c1^x;
    }
    for (; i < 0x100000; i += 4)
    {
        c1b += c1;
    }
    c0 ^= c0a^c0b;
    c1 ^= c1a^c1b;
    buf[0] = c0 >> 24;
    buf[1] = c0 >> 16;
    buf[2] = c0 >>  8;
    buf[3] = c0 >>  0;
    buf[4] = c1 >> 24;
    buf[5] = c1 >> 16;
    buf[6] = c1 >>  8;
    buf[7] = c1 >>  0;
}

int main(int argc, const char **argv)
{
    FILE *f;
    u8   *data;
    uint  size;
    char  buf[0x30];
    if (argc != 4)
    {
        fprintf(stderr, "usage: %s <image> <label> <code>\n", argv[0]);
        return EXIT_FAILURE;
    }
    memset(buf, 0x00, sizeof(buf));
    memset(&buf[0x10], ' ', 20);
    size = strlen(argv[2]);
    memcpy(&buf[0x10], argv[2], MIN(20, size));
    memcpy(&buf[0x2B], argv[3], 4);
    buf[0x2F] = strtol(&argv[3][4], NULL, 0);
    f = fopen(argv[1], "r+b");
    if (f == NULL)
    {
        fprintf(stderr, "error: could not open '%s'\n", argv[1]);
        return EXIT_FAILURE;
    }
    fseek(f, 0x1000, SEEK_END);
    size = ftell(f);
    if (size > 0x100000) size = 0x100000;
    data = malloc(size);
    fseek(f, 0x1000, SEEK_SET);
    fread(data, 1, size, f);
    crc(&buf[0x00], data, size);
    free(data);
    fseek(f, 0x10, SEEK_SET);
    fwrite(buf, 1, sizeof(buf), f);
    fclose(f);
    return EXIT_SUCCESS;
}
