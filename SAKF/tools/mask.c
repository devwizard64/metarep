#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>

typedef unsigned int uint;
typedef uint8_t u8;

static void crc(char *buf, const u8 *data, uint size)
{
    uint sum = 0;
    uint i;
    for (i = 0; i < size; i++) sum += data[i];
    buf[2] = sum >> 0;
    buf[3] = sum >> 8;
    buf[0] = ~buf[2];
    buf[1] = ~buf[3];
}

int main(int argc, char *argv[])
{
    FILE *f;
    u8 *data;
    size_t size;
    char buf[4];
    if (argc != 2)
    {
        fprintf(stderr, "usage: %s <image>\n", argv[0]);
        return EXIT_FAILURE;
    }
    if ((f = fopen(argv[1], "r+b")) == NULL)
    {
        fprintf(stderr, "error: could not open '%s'\n", argv[1]);
        return EXIT_FAILURE;
    }
    fseek(f, 0, SEEK_END);
    size = ftell(f);
    data = malloc(size);
    fseek(f, 0, SEEK_SET);
    fread(data, 1, size, f);
    crc(buf, data, size);
    free(data);
    fseek(f, 0x7FDC, SEEK_SET);
    fwrite(buf, 1, sizeof(buf), f);
    fclose(f);
    return EXIT_SUCCESS;
}
