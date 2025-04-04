#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "lib/elf.h"
#include "lib/elf.c"

#define BLK_OL  1
#define BLK_SL  3
#define BLK_OH  (BLK_OL+0xFFF)
#define BLK_SH  (BLK_SL+0xF)
#define BITCNT 32
#define slitbl() \
{ \
	t = s; s += 4; \
	t[0] = 0; t[1] = 0; t[2] = 0; t[3] = 0; \
}
#define slipkt() \
{ \
	*p++ = x >> 8 | (sz-BLK_SL) << 4; \
	*p++ = x >> 0; \
}
#define slicpy() \
{ \
	*c++ = data[i++]; \
	t[n>>3] |= 0x80 >> (n&7); \
}
#define slicnt() \
{ \
	n = (n+1) & (BITCNT-1); \
}

static int sliblk(const char *data, size_t size, size_t i, int *of, int *sz)
{
	int result = 0;
	size_t o = i < BLK_OH ? 0 : i-BLK_OH;
	int c = size-i < BLK_SH ? size-i : BLK_SH;
	while (o < i && *sz < c)
	{
		int s = 0;
		int n = 0;
		while (o+s < i+c && s < c)
		{
			if (data[i+s] != data[o+s < i ? o+s : o+(s%n)]) break;
			if (o+s < i) n++;
			s++;
		}
		if (*sz < s)
		{
			*of = o;
			*sz = s;
			result = 1;
		}
		o++;
	}
	return result;
}

static size_t slielf(ELF *elf, const char *data, size_t size)
{
	int i;
	uint32_t end = 0;
	for (i = 0; i < elf->symnum; i++)
	{
		uint32_t value = ntohl(elf->symtab[i].value);
		uint32_t size = ntohl(elf->symtab[i].size);
		if (end < value+size) end = value+size;
		if (ST_BIND(elf->symtab[i].info) != STB_LOCAL)
		{
			const char *name = elf_stname(elf, &elf->symtab[i]);
			printf(".globl %s; %s = 0x%08X\n", name, name, value);
		}
	}
	end &= 0xFFFFFF;
	if (size-end >= 16) return size;
	for (i = 0; i < (int)(size-end); i++)
	{
		if (data[end+i]) return size;
	}
	return end;
}

int main(int argc, char *argv[])
{
	size_t i, n, size;
	char *data, *stm, *pkt, *cpy, *s, *p, *c, *t;
	size_t poff, coff;
	FILE *fp;
	if (argc != 3)
	{
		fprintf(stderr, "usage: %s <input> <szp>\n", argv[0]);
		return 1;
	}
	if (!strcmp(argv[1]+strlen(argv[1])-4, ".elf"))
	{
		ELF elf;
		if (elf_open(&elf, argv[1], "rb"))
		{
			fprintf(stderr, "error: could not open '%s'\n", argv[1]);
			return 1;
		}
		elf_loadsection(&elf);
		elf_load(&elf, data = malloc(size = elf_size(&elf)));
		size = slielf(&elf, data, size);
		elf_close(&elf);
	}
	else
	{
		if (!(fp = fopen(argv[1], "rb")))
		{
			fprintf(stderr, "error: could not open '%s'\n", argv[1]);
			return 1;
		}
		fseek(fp, 0, SEEK_END);
		data = malloc(size = ftell(fp));
		fseek(fp, 0, SEEK_SET);
		fread(data, 1, size, fp);
		fclose(fp);
	}
	s = stm = malloc((size+31) / 8);
	p = pkt = malloc(size);
	c = cpy = malloc(size);
	i = 0;
	n = 0;
	while (i < size)
	{
		int x, of, sz, ofn, szn;
		if (sz = BLK_SL-1, sliblk(data, size, i, &of, &sz))
		{
			if (szn = sz+1, sliblk(data, size, i+1, &ofn, &szn))
			{
				if (n == 0) slitbl();
				slicpy();
				slicnt();
				of = ofn;
				sz = szn;
			}
			x = i-of-BLK_OL;
			if (n == 0) slitbl();
			slipkt();
			slicnt();
			i += sz;
		}
		else
		{
			if (n == 0) slitbl();
			slicpy();
			slicnt();
		}
	}
	free(data);
	printf(".data\n.incbin \"%s\"\n", argv[2]);
	if (!(fp = fopen(argv[2], "wb")))
	{
		fprintf(stderr, "error: could not open '%s'\n", argv[2]);
		return 1;
	}
	poff = 16   + (s-stm);
	coff = poff + (p-pkt);
	fwrite("MIO0", 1, 4, fp);
	fputc(size >> 24, fp);
	fputc(size >> 16, fp);
	fputc(size >>  8, fp);
	fputc(size >>  0, fp);
	fputc(poff >> 24, fp);
	fputc(poff >> 16, fp);
	fputc(poff >>  8, fp);
	fputc(poff >>  0, fp);
	fputc(coff >> 24, fp);
	fputc(coff >> 16, fp);
	fputc(coff >>  8, fp);
	fputc(coff >>  0, fp);
	fwrite(stm, 1, s-stm, fp); free(stm);
	fwrite(pkt, 1, p-pkt, fp); free(pkt);
	fwrite(cpy, 1, c-cpy, fp); free(cpy);
	fclose(fp);
	return 0;
}
