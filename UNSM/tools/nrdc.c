#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <getopt.h>

static int error(const char *err)
{
	fprintf(stderr, "error: %s\n", err);
	return 1;
}

static int usage(const char *path)
{
	fprintf(
		stderr,
		"usage: %s [options] romfile\n"
		"\t-b big endian\n"
		"\t-l little endian\n"
		"\t-t title\n"
		"\t-i icode\n"
		"\t-v version\n",
		path
	);
	return 1;
}

int main(int argc, char *argv[])
{
	int c, endian = -1, version = -1;
	const char *title = NULL, *icode = NULL;
	FILE *fp;
	while ((c = getopt(argc, argv, "blt:i:v:")) != -1)
	{
		switch (c)
		{
		case 'b':
			endian = 0;
			break;
		case 'l':
			endian = 1;
			break;
		case 't':
			title = optarg;
			break;
		case 'i':
			if (strlen(optarg) < 4) return error("invalid initial code");
			icode = optarg;
			break;
		case 'v':
			c = optarg[0];
			if      (c >= '0' && c <= '9') version =  0 + c-'0';
			else if (c >= 'A' && c <= 'Z') version = 10 + c-'A';
			else if (c >= 'a' && c <= 'z') version = 10 + c-'a';
			else return error("invalid version number");
			break;
		case '?':
			return usage(argv[0]);
		}
	}
	if (argc-optind != 1) return usage(argv[0]);
	if (endian < 0) return error("unknown endianness");
	if (endian != 0) return error("invalid endianness");
	if (!(fp = fopen(argv[optind], "r+b")))
	{
		fprintf(stderr, "error: could not open '%s'\n", argv[optind]);
		return 1;
	}
	if (title)
	{
		size_t i, n = strlen(title);
		if (n > 20) n = 20;
		fseek(fp, 0x20, SEEK_SET);
		fwrite(title, 1, n, fp);
		for (i = n; i < 20; i++) fputc(' ', fp);
	}
	if (icode)
	{
		fseek(fp, 0x3B, SEEK_SET);
		fwrite(icode, 1, 4, fp);
	}
	if (version >= 0)
	{
		fseek(fp, 0x3F, SEEK_SET);
		fputc(version, fp);
	}
	fclose(fp);
	return 0;
}
