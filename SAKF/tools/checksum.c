#include <stdio.h>

int main(int argc, char *argv[])
{
	int c;
	int sum = 0;
	FILE *fp;
	if (argc != 2)
	{
		fprintf(stderr, "usage: %s <image>\n", argv[0]);
		return 1;
	}
	if (!(fp = fopen(argv[1], "r+b")))
	{
		fprintf(stderr, "error: could not open '%s'\n", argv[1]);
		return 1;
	}
	while ((c = fgetc(fp)) >= 0) sum += c;
	fseek(fp, 0x7FDC, SEEK_SET);
	fputc(~sum >> 0, fp);
	fputc(~sum >> 8, fp);
	fputc( sum >> 0, fp);
	fputc( sum >> 8, fp);
	fclose(fp);
	return 0;
}
