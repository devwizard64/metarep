#include "elf.h"
#include <stdlib.h>
#include <string.h>

int elf_open(ELF *elf, const char *path, const char *mode)
{
	uint32_t phoff, shoff;
	uint16_t phnum, shnum;
	memset(elf, 0, sizeof(ELF));
	if (!(elf->fp = fopen(path, mode))) return -1;
	fread(&elf->eh, sizeof(ELFEH), 1, elf->fp);
	phoff = ntohl(elf->eh.phoff);
	shoff = ntohl(elf->eh.shoff);
	phnum = ntohs(elf->eh.phnum);
	shnum = ntohs(elf->eh.shnum);
	fseek(elf->fp, phoff, SEEK_SET);
	fread(elf->ph = malloc(sizeof(ELFPH)*phnum), sizeof(ELFPH), phnum, elf->fp);
	fseek(elf->fp, shoff, SEEK_SET);
	fread(elf->sh = malloc(sizeof(ELFSH)*shnum), sizeof(ELFSH), shnum, elf->fp);
	return 0;
}

void elf_close(ELF *elf)
{
	int i;
	if (elf->section)
	{
		uint16_t shnum = ntohs(elf->eh.shnum);
		for (i = 0; i < shnum; i++) free(elf->section[i]);
		free(elf->section);
	}
	free(elf->sh);
	free(elf->ph);
	fclose(elf->fp);
}

void elf_loadsection(ELF *elf)
{
	int i;
	uint16_t shnum = ntohs(elf->eh.shnum);
	uint16_t shstrndx = ntohs(elf->eh.shstrndx);
	elf->section = calloc(shnum, sizeof(void *));
	for (i = 0; i < shnum; i++)
	{
		uint32_t type = ntohl(elf->sh[i].type);
		uint32_t size = ntohl(elf->sh[i].size);
		if (type == SHT_SYMTAB || type == SHT_STRTAB)
		{
			uint32_t offset = ntohl(elf->sh[i].offset);
			fseek(elf->fp, offset, SEEK_SET);
			fread(elf->section[i] = malloc(size), 1, size, elf->fp);
		}
		if (type == SHT_SYMTAB && !elf->symtab)
		{
			elf->symtab = elf->section[i];
			elf->symnum = size / sizeof(ELFST);
		}
		if (type == SHT_STRTAB && (!elf->strtab || i != shstrndx))
		{
			elf->strtab = elf->section[i];
		}
	}
}

void elf_load(ELF *elf, void *data)
{
	int i;
	size_t size = 0;
	uint16_t phnum = ntohs(elf->eh.phnum);
	for (i = 0; i < phnum; i++)
	{
		uint32_t type = ntohl(elf->ph[i].type);
		if (type == PT_LOAD)
		{
			uint32_t offset = ntohl(elf->ph[i].offset);
			uint32_t filesz = ntohl(elf->ph[i].filesz);
			fseek(elf->fp, offset, SEEK_SET);
			fread((char *)data + size, 1, filesz, elf->fp);
			size += filesz;
		}
	}
}

size_t elf_size(ELF *elf)
{
	int i;
	size_t size = 0;
	uint16_t phnum = ntohs(elf->eh.phnum);
	for (i = 0; i < phnum; i++)
	{
		uint32_t type = ntohl(elf->ph[i].type);
		if (type == PT_LOAD)
		{
			uint32_t filesz = ntohl(elf->ph[i].filesz);
			size += filesz;
		}
	}
	return size;
}

char *elf_shname(ELF *elf, ELFSH *sh)
{
	uint16_t shstrndx = ntohs(elf->eh.shstrndx);
	char *strtab = elf->section[shstrndx];
	uint32_t name = ntohl(sh->name);
	return strtab + name;
}

char *elf_stname(ELF *elf, ELFST *st)
{
	uint32_t name = ntohl(st->name);
	return elf->strtab + name;
}
