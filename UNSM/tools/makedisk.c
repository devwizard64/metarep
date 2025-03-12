#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <getopt.h>

#include <sm64/defdisk.h>

#include "lib/elf.h"
#include "lib/elf.c"

#define HI(x)   (((x) >> 16) + ((x) >> 15 & 1))
#define LO(x)   ((x) & 0xFFFF)

typedef struct diskheader
{
	uint32_t country;
	uint8_t fmt_type;
	uint8_t disk_type;
	uint16_t ipl_load_len;
	uint8_t defect_num[20];
	uint32_t loadptr;
	uint8_t defect_data[192];
	uint16_t rom_end_lba;
	uint16_t ram_start_lba;
	uint16_t ram_end_lba;
}
DISKHEADER;

static void makeheader(DISKHEADER *hdr, ELF *elf, int len)
{
	static const uint8_t defect[] =
	{
		0x04,0x0C,0x14,0x1C,0x24,0x2C,0x34,0x3C,0x44,0x4C,0x54,0x5C,
		0x10,0x16,0x1C,0x22,0x28,0x2E,0x34,0x3A,0x40,0x46,0x4C,0x52,
		0x01,0x0C,0x14,0x1C,0x24,0x2C,0x34,0x3C,0x44,0x4C,0x54,0x5C,
		0x04,0x0C,0x14,0x1C,0x24,0x2C,0x34,0x3C,0x44,0x4C,0x56,0x5C,
		0x56,0x5C,0x62,0x68,0x6E,0x74,0x7A,0x80,0x86,0x8C,0x92,0x98,
	};
	static const uint8_t defmap[16] = {12,0,24,0,0,36,0,0,48};
	int i;
	memset(hdr, ~0, sizeof(DISKHEADER));
	for (i = 0; i < 16; i++)
	{
		hdr->defect_num[i] = 12*(i+1);
		memcpy(&hdr->defect_data[12*i], &defect[defmap[i]], 12);
	}
	hdr->country = htonl(0xE848D316);
	hdr->fmt_type = 0x10;
	hdr->disk_type = 0x10;
	hdr->ipl_load_len = htons(len);
	hdr->loadptr = elf->eh.entry;
	hdr->rom_end_lba = htons(108);
}

static void makecrt0(unsigned char *data, ELF *elf)
{
	int i;
	uint32_t *p = (uint32_t *)data;
	uint32_t entry = 0;
	uint32_t stack = 0;
	uint32_t bssStart = 0;
	uint32_t bssEnd = 0;
	uint32_t bssSize;
	for (i = 0; i < elf->symnum; i++)
	{
		const char *name = elf_stname(elf, &elf->symtab[i]);
		uint32_t value = ntohl(elf->symtab[i].value);
		if (!entry    && !strcmp(name, "__crt0Entry"))      entry    = value;
		if (!stack    && !strcmp(name, "__crt0Stack"))      stack    = value;
		if (!bssStart && !strcmp(name, "__crt0BssStart"))   bssStart = value;
		if (!bssEnd   && !strcmp(name, "__crt0BssEnd"))     bssEnd   = value;
		if (entry && stack && bssStart && bssEnd) break;
	}
	if ((bssSize = bssEnd-bssStart) > 0)
	{
		uint16_t bssSizeHi = bssSize >> 16;
		uint16_t bssSizeLo = bssSize;
		if      (bssStart)  *p++ = htonl(0x3C080000 | HI(bssStart));
		if      (bssSizeHi) *p++ = htonl(0x3C090000 | bssSizeHi);
		if      (bssStart)  *p++ = htonl(0x25080000 | LO(bssStart));
		if      (bssSizeHi) *p++ = htonl(0x35290000 | bssSizeLo);
		else if (bssSize > 0x7FFF)  *p++ = htonl(0x34090000 | bssSize);
		else                        *p++ = htonl(0x24090000 | bssSize);
		*p++ = htonl(0x2129FFF8);
		*p++ = htonl(0xAD000000);
		*p++ = htonl(0xAD000004);
		*p++ = htonl(0x1520FFFC);
		*p++ = htonl(0x21080008);
	}
	if      (entry) *p++ = htonl(0x3C0A0000 | HI(entry));
	if      (stack) *p++ = htonl(0x3C1D0000 | HI(stack));
	if      (entry) *p++ = htonl(0x254A0000 | LO(entry));
	if      (entry) *p++ = htonl(0x01400008);
	if      (stack) *p++ = htonl(0x27BD0000 | LO(stack));
	else if (entry) *p++ = htonl(0x00000000);
}

typedef struct zone
{
	unsigned short size;
	short lba;
}
ZONE;

static const ZONE zonetab[] =
{
	{232*85,    0},
	{216*85,  292},
	{208*85,  584},
	{208*85,  858},
	{216*85, 1150},
	{192*85, 1442},
	{176*85, 1716},
	{160*85, 1990},
	{144*85, 2264},
	{128*85, 2538},
	{112*85, 2742},
	{128*85, 2946},
	{144*85, 3220},
	{160*85, 3494},
	{176*85, 3768},
	{192*85, 4042},
	{     0, 4316},
};

static void diskcopy(
	char *disk, int lba, int nblk, const unsigned char *data, size_t size
)
{
	static char buffer[0x100000];
	const ZONE *zone;
	lba += 24;
	for (zone = zonetab; zone[1].lba < lba; zone++)
	{
		disk += zone->size * (zone[1].lba-zone[0].lba);
	}
	disk += zone->size * (lba-zone->lba);
	while (size > 0 && nblk > 0)
	{
		size_t n, len;
		for (len = 0; len < size && nblk > 0; nblk--)
		{
			if (len+zone->size > sizeof(buffer)) break;
			len += zone->size;
			if (++lba >= zone[1].lba) zone++;
		}
		n = len < size ? len : size;
		memcpy(buffer, data, n);
		data += n;
		size -= n;
		memcpy(disk, buffer, len);
		disk += len;
	}
}

static int diskcalc(int lba, size_t size)
{
	int nblk = 0;
	const ZONE *zone;
	lba += 24;
	for (zone = zonetab; zone[1].lba < lba; zone++);
	while (size >= zone->size)
	{
		size -= zone->size;
		if (lba + ++nblk >= zone[1].lba) zone++;
	}
	if (size > 0) nblk++;
	return nblk;
}

static int usage(const char *path)
{
	fprintf(
		stderr,
		"usage: %s [options] elffile\n"
		"\t-R diskfile\n",
		path
	);
	return 1;
}

int main(int argc, char *argv[])
{
	static char disk[0x3DEC800];
	int i, c, ipl_len;
	size_t size, ipl_size = 0x100000;
	const char *path = "disk";
	unsigned char *data;
	unsigned char *wave = NULL;
	DISKHEADER header;
	FILE *fp;
	ELF elf;
	while ((c = getopt(argc, argv, "R:")) != -1)
	{
		switch (c)
		{
		case 'R':
			path = optarg;
			break;
		case '?':
			return usage(argv[0]);
		}
	}
	if (argc-optind != 1) return usage(argv[0]);
	if (elf_open(&elf, argv[optind], "rb"))
	{
		fprintf(stderr, "error: could not open '%s'\n", argv[optind]);
		return 1;
	}
	elf_loadsection(&elf);
	data = calloc(size = 0x1000+elf_size(&elf), 1);
	elf_load(&elf, data+0x1000);
	makecrt0(data+0x1000, &elf);
	for (i = 0; i < elf.symnum; i++)
	{
		const char *name = elf_stname(&elf, &elf.symtab[i]);
#if 0
		if (!strcmp(name, "_codeSegmentRomEnd"))
		{
			uint32_t value = ntohl(elf.symtab[i].value);
			ipl_size = value - 0x1000;
			break;
		}
#else
		if (!strcmp(name, "_AudiotblSegmentRomStart"))
		{
			uint32_t value = ntohl(elf.symtab[i].value);
			unsigned char *audiotbl = data + value;
			uint32_t wave_start = ntohl(*(uint32_t *)(audiotbl+4));
			uint32_t wave_size  = ntohl(*(uint32_t *)(audiotbl+8));
			if (wave_size != WAVE_SIZE)
			{
				fprintf(stderr, "error: WAVE_SIZE must be 0x%08X\n", wave_size);
				return 1;
			}
			if (diskcalc(WAVE_LBA, wave_size) < WAVE_LEN)
			{
				fprintf(stderr, "error: WAVE_LEN must be >= %d\n", wave_len);
				return 1;
			}
			wave = audiotbl + wave_start;
			break;
		}
#endif
	}
	ipl_len = diskcalc(0, ipl_size);
	makeheader(&header, &elf, ipl_len);
	elf_close(&elf);
	for (i = 0; i < 85; i++) memcpy(disk+232*i, &header, 232);
	memcpy(disk+232*85*1, disk+232*85*0, 232*85*1);
	memcpy(disk+232*85*8, disk+232*85*0, 232*85*2);
#if 0
	diskcopy(disk, 0, 4292, data+0x1000, size-0x1000);
#else
	diskcopy(disk, 0, ipl_len, data+0x1000, size-0x1000);
	if (size > ROM_START)
	{
		diskcopy(disk, ROM_LBA, 566, data+ROM_START, size-ROM_START);
	}
	if (wave) diskcopy(disk, WAVE_LBA, WAVE_BLK, wave, data+size-wave);
#endif
	free(data);
	if (!(fp = fopen(path, "wb")))
	{
		fprintf(stderr, "error: could not open '%s'\n", path);
		return 1;
	}
	fwrite(disk, 1, sizeof(disk), fp);
	fclose(fp);
	return 0;
}
