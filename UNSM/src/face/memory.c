#include "face.h"

static MEMBLOCK *free_list;
static MEMBLOCK *used_list;
static MEMBLOCK *empty_list;

static MEMBLOCK *MakeMemBlock(int type, unsigned char flag);

static void DeleteMemBlock(MEMBLOCK *blk)
{
	if (blk->next) blk->next->prev = blk->prev;
	if (blk->prev) blk->prev->next = blk->next;
	switch (blk->type)
	{
	case MEM_FREE:
		if (!blk->prev) free_list = blk->next;
		break;
	case MEM_USED:
		if (!blk->prev) used_list = blk->next;
		break;
	}
	blk->next = empty_list;
	if (blk->next) empty_list->prev = blk;
	empty_list = blk;
	blk->prev = NULL;
	blk->addr = NULL;
	blk->size = 0;
}

static MEMBLOCK *FreeMemBlock(MEMBLOCK *blk)
{
	MEMBLOCK *new;
	char *addr;
	unsigned char flag;
	size_t size;
	addr = blk->addr;
	size = blk->size;
	flag = blk->flag;
	DeleteMemBlock(blk);
	new = MakeMemBlock(MEM_FREE, flag);
	new->addr = addr;
	new->size = size;
	new->flag = flag;
	return new;
}

static MEMBLOCK *MakeMemBlock(int type, unsigned char flag)
{
	MEMBLOCK *blk;
	if (!empty_list)
	{
		if (!(empty_list = gd_allocblock(sizeof(MEMBLOCK))))
		{
			face_stdio_8018D298("MakeMemBlock() unable to allocate");
		}
		empty_list->next = NULL;
		empty_list->prev = NULL;
	}
	blk = empty_list;
	if ((empty_list = blk->next)) blk->next->prev = NULL;
	switch (type)
	{
	case MEM_FREE:
		blk->next = free_list;
		if (blk->next) free_list->prev = blk;
		free_list = blk;
		break;
	case MEM_USED:
		blk->next = used_list;
		if (blk->next) used_list->prev = blk;
		used_list = blk;
		break;
	default:
		face_stdio_8018D298("unkown memblock type");
	}
	blk->prev = NULL;
	blk->type = type;
	blk->flag = flag;
	return blk;
}

size_t Free(void *ptr)
{
	register MEMBLOCK *blk;
	size_t size;
	register char *addr = ptr;
	for (blk = used_list; blk; blk = blk->next)
	{
		if (blk->addr == addr)
		{
			size = blk->size;
			FreeMemBlock(blk);
			return size;
		}
	}
	face_stdio_8018D298("Free() Not a valid memory block");
	return 0;
}

void *Alloc(size_t size, unsigned char flag)
{
	MEMBLOCK *blk = NULL, *fblk, *new = MakeMemBlock(MEM_USED, flag);
	fblk = free_list;
	while (fblk)
	{
		if (fblk->flag & flag)
		{
			if (fblk->size == size)
			{
				blk = fblk;
				break;
			}
			else if (fblk->size > size)
			{
				if (blk)
				{
					if (fblk->size < blk->size) blk = fblk;
				}
				else
				{
					blk = fblk;
				}
			}
		}
		fblk = fblk->next;
	}
	if (!blk) return NULL;
	if (blk->size > size)
	{
		new->addr = blk->addr;
		new->size = size;
		blk->size -= size;
		blk->addr += size;
	}
	else if (blk->size == size)
	{
		new->addr = blk->addr;
		new->size = size;
		DeleteMemBlock(blk);
	}
	return new->addr;
}

MEMBLOCK *face_mem_80177E7C(size_t size, void *addr, unsigned char flag)
{
	MEMBLOCK *blk;
	size = (size-8) & ~7;
	addr = (void *)(((unsigned long)addr+8) & ~7);
	blk = MakeMemBlock(MEM_FREE, flag);
	blk->addr = addr;
	blk->size = size;
	return blk;
}

void face_mem_80177F0C(void)
{
	free_list = NULL;
	used_list = NULL;
	empty_list = NULL;
}

static int PrintMemList(MEMBLOCK *blk, int verbose, int flag)
{
	int count = 0;
	size_t total = 0;
	while (blk)
	{
		if (blk->flag & flag)
		{
			count++;
			if (verbose) gd_printf(
				"     %6.2fk (%d bytes)\n",
				(float)blk->size/1024.0, blk->size
			);
			total += blk->size;
		}
		blk = blk->next;
	}
	gd_printf(
		"Total %6.2fk (%d bytes) in %d entries\n",
		(float)total/1024.0, total, count
	);
	return count;
}

void PrintMemInfo(void)
{
	MEMBLOCK *blk;
	gd_printf("Perm Used blocks:\n");
	blk = used_list;
	PrintMemList(blk, FALSE, 0xF0);
	gd_printf("\n");
	gd_printf("Perm Free blocks:\n");
	blk = free_list;
	PrintMemList(blk, FALSE, 0xF0);
	gd_printf("\n");
	gd_printf("Temp Used blocks:\n");
	blk = used_list;
	PrintMemList(blk, FALSE, 0x0F);
	gd_printf("\n");
	gd_printf("Temp Free blocks:\n");
	blk = free_list;
	PrintMemList(blk, FALSE, 0x0F);
	gd_printf("\n");
	gd_printf("Empty blocks:\n");
	blk = empty_list;
	PrintMemList(blk, FALSE, 0xFF);
}
