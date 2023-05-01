#include <stdlib.h>
#include <stdio.h>

static void checksum(char *buf, const unsigned char *data, size_t size)
{
    size_t i;
    unsigned int sum = 0;
    for (i = 0; i < size; i++) sum += data[i];
    buf[0] = ~(buf[2] = sum >> 0);
    buf[1] = ~(buf[3] = sum >> 8);
}

int main(int argc, char *argv[])
{
    FILE *fp;
    unsigned char *data;
    size_t size;
    char buf[4];
    if (argc != 2)
    {
        fprintf(stderr, "usage: %s <image>\n", argv[0]);
        return 1;
    }
    if ((fp = fopen(argv[1], "r+b")) == NULL)
    {
        fprintf(stderr, "error: could not open '%s'\n", argv[1]);
        return 1;
    }
    fseek(fp, 0, SEEK_END);
    data = malloc(size = ftell(fp));
    fseek(fp, 0, SEEK_SET);
    fread(data, 1, size, fp);
    checksum(buf, data, size);
    free(data);
    fseek(fp, 0x7FDC, SEEK_SET);
    fwrite(buf, 1, sizeof(buf), fp);
    fclose(fp);
    return 0;
}
