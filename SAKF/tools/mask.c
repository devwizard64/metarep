#include <stdio.h>
#include <stdlib.h>

static void crc(char *buf, const unsigned char *data, size_t size)
{
    unsigned int sum = 0;
    size_t i;
    for (i = 0; i < size; i++) sum += data[i];
    buf[0] = ~(buf[2] = sum >> 0);
    buf[1] = ~(buf[3] = sum >> 8);
}

int main(int argc, char *argv[])
{
    FILE *f;
    unsigned char *data;
    size_t size;
    char buf[4];
    if (argc != 2)
    {
        fprintf(stderr, "usage: %s <image>\n", argv[0]);
        return 1;
    }
    if ((f = fopen(argv[1], "r+b")) == NULL)
    {
        fprintf(stderr, "error: could not open '%s'\n", argv[1]);
        return 1;
    }
    fseek(f, 0, SEEK_END);
    data = malloc(size = ftell(f));
    fseek(f, 0, SEEK_SET);
    fread(data, 1, size, f);
    crc(buf, data, size);
    free(data);
    fseek(f, 0x7FDC, SEEK_SET);
    fwrite(buf, 1, sizeof(buf), f);
    fclose(f);
    return 0;
}
