#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <getopt.h>

typedef struct bank
{
	char *path;
	unsigned int offset, size;
}
BANK;

static int usage(const char *path)
{
	fprintf(
		stderr, "usage: %s [-c code] [-a align] -o output input [...]\n", path
	);
	return 1;
}

int main(int argc, char *argv[])
{
	static char buffer[0x10000];
	int i, n, c, count, index = 0, code = 0, align = 0;
	unsigned int offset, size;
	const char *output = NULL;
	BANK *bank;
	FILE *fp, *in;
	while ((c = getopt(argc, argv, "c:a:o:")) != -1)
	{
		switch (c)
		{
		case 'c':
			code = strtol(optarg, NULL, 0);
			break;
		case 'a':
			align = strtol(optarg, NULL, 0);
			break;
		case 'o':
			output = optarg;
			break;
		case '?':
			return usage(argv[0]);
		}
	}
	if (!output || (count = argc-optind) < 1) return usage(argv[0]);
	bank = malloc(sizeof(BANK)*count);
	printf(".data\n.incbin \"%s\"\n", output);
	if (!(fp = fopen(output, "wb")))
	{
		fprintf(stderr, "error: could not open '%s'\n", output);
		return 1;
	}
	fputc(code >> 8, fp);
	fputc(code >> 0, fp);
	fputc(count >> 8, fp);
	fputc(count >> 0, fp);
	offset = ((4+8*count)+15) & ~15;
	for (i = 0; i < count; i++)
	{
		char *path = argv[optind+i];
		for (n = 0; n < index; n++)
		{
			if (!strcmp(bank[n].path, path)) break;
		}
		if (n == index)
		{
			if (!(in = fopen(path, "rb")))
			{
				fprintf(stderr, "error: could not open '%s'\n", path);
				return 1;
			}
			fseek(in, 0, SEEK_END);
			size = (ftell(in)+15) & ~15;
			fclose(in);
			bank[n].path = path;
			bank[n].offset = offset;
			bank[n].size = size;
			offset += size;
			index++;
		}
		fputc(bank[n].offset >> 24, fp);
		fputc(bank[n].offset >> 16, fp);
		fputc(bank[n].offset >>  8, fp);
		fputc(bank[n].offset >>  0, fp);
		fputc(bank[n].size   >> 24, fp);
		fputc(bank[n].size   >> 16, fp);
		fputc(bank[n].size   >>  8, fp);
		fputc(bank[n].size   >>  0, fp);
	}
	fwrite(buffer, 1, -(4+8*count) & 15, fp);
	for (i = 0; i < index; i++)
	{
		if (!(in = fopen(bank[i].path, "rb")))
		{
			fprintf(stderr, "error: could not open '%s'\n", bank[i].path);
			return 1;
		}
		for (size = bank[i].size; size > 0; size -= n)
		{
			n = size < sizeof(buffer) ? size : sizeof(buffer);
			fread(buffer, 1, n, in);
			fwrite(buffer, 1, n, fp);
		}
		fclose(in);
	}
	if (align > 0)
	{
		n = align - (ftell(fp) & (align-1));
		for (i = 0; i < n; i++) fputc(0, fp);
	}
	fclose(fp);
	free(bank);
	return 0;
}
