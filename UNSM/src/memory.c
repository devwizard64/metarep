#include <sm64.h>

#define ALIGN4(x)   (((unsigned long)(x)+ 3) & ~ 3)
#define ALIGN8(x)   (((unsigned long)(x)+ 7) & ~ 7)
#define ALIGN16(x)  (((unsigned long)(x)+15) & ~15)
#define BOUND16(x)  (((unsigned long)(x)   ) & ~15)

static unsigned long segment_table[32];
static size_t mem_size;
static char *mem_start;
static char *mem_end;
static MEM_BLOCK *mem_blockl;
static MEM_BLOCK *mem_blockr;
static MEM_FRAME *mem_frame = NULL;

HEAP *mem_heap;

unsigned long SegmentSet(int number, void *addr)
{
	segment_table[number] = K0_TO_PHYS(addr);
	return segment_table[number];
}

void *SegmentGet(int number)
{
	return (void *)PHYS_TO_K0(segment_table[number]);
}

void *SegmentToVirtual(const void *addr)
{
	int number = (unsigned int)(addr) >> 24;
	int offset = SEGMENT_OFFSET(addr);
	return (void *)PHYS_TO_K0(segment_table[number] + offset);
}

void *VirtualToSegment(int number, const void *addr)
{
	int offset = K0_TO_PHYS(addr) - segment_table[number];
	return (void *)SEGMENT_ADDR(number, offset);
}

void SegmentWrite(void)
{
	int i;
	for (i = 0; i < 16; i++) gSPSegment(glistp++, i, segment_table[i]);
}

void MemInit(void *start, void *end)
{
	mem_start  = (char *)((MEM_BLOCK *)ALIGN16(start) + 1);
	mem_end    = (char *)((MEM_BLOCK *)BOUND16(end)   - 1);
	mem_size   = mem_end - mem_start;
	mem_blockl = (MEM_BLOCK *)mem_start - 1;
	mem_blockr = (MEM_BLOCK *)mem_end;
	mem_blockl->prev = NULL;
	mem_blockl->next = NULL;
	mem_blockr->prev = NULL;
	mem_blockr->next = NULL;
}

void *MemAlloc(size_t size, int mode)
{
	MEM_BLOCK *block;
	void *ptr = NULL;
	size = ALIGN16(size) + sizeof(MEM_BLOCK);
	if (0 < size && size <= mem_size)
	{
		mem_size -= size;
		if (mode == MEM_ALLOC_L)
		{
			block = (MEM_BLOCK *)((char *)mem_blockl + size);
			mem_blockl->next = block;
			block->prev = mem_blockl;
			block->next = NULL;
			ptr = mem_blockl + 1;
			mem_blockl = block;
		}
		else
		{
			block = (MEM_BLOCK *)((char *)mem_blockr - size);
			mem_blockr->prev = block;
			block->next = mem_blockr;
			block->prev = NULL;
			mem_blockr = block;
			ptr = mem_blockr + 1;
		}
	}
	return ptr;
}

size_t MemFree(void *ptr)
{
	MEM_BLOCK *old = (MEM_BLOCK *)ptr - 1;
	MEM_BLOCK *new = (MEM_BLOCK *)ptr - 1;
	if (new < mem_blockl)
	{
		while (new->next) new = new->next;
		mem_blockl = old;
		mem_blockl->next = NULL;
		mem_size += (unsigned int)new - (unsigned int)mem_blockl;
	}
	else
	{
		while (new->prev) new = new->prev;
		mem_blockr = old->next;
		mem_blockr->prev = NULL;
		mem_size += (unsigned int)mem_blockr - (unsigned int)new;
	}
	return mem_size;
}

void *MemRealloc(void *ptr, size_t size)
{
	void *new = NULL;
	MEM_BLOCK *block = (MEM_BLOCK *)ptr - 1;
	if (block->next == mem_blockl)
	{
		MemFree(ptr);
		new = MemAlloc(size, MEM_ALLOC_L);
	}
	return new;
}

size_t MemGetFree(void)
{
	return mem_size - sizeof(MEM_BLOCK);
}

size_t MemPush(void)
{
	MEM_FRAME *frame  = mem_frame;
	size_t     size   = mem_size;
	MEM_BLOCK *blockl = mem_blockl;
	MEM_BLOCK *blockr = mem_blockr;
	mem_frame = MemAlloc(sizeof(MEM_FRAME), MEM_ALLOC_L);
	mem_frame->size   = size;
	mem_frame->blockl = blockl;
	mem_frame->blockr = blockr;
	mem_frame->frame  = frame;
	return mem_size;
}

size_t MemPull(void)
{
	mem_size   = mem_frame->size;
	mem_blockl = mem_frame->blockl;
	mem_blockr = mem_frame->blockr;
	mem_frame  = mem_frame->frame;
	return mem_size;
}

#ifndef DISK
void RomRead(char *dst, const char *start, const char *end)
{
	size_t size = ALIGN16(end-start);
	osInvalDCache(dst, size);
	while (size > 0)
	{
		size_t n = size >= 0x1000 ? 0x1000 : size;
		osPiStartDma(
			&dma_mb, OS_MESG_PRI_NORMAL, OS_READ, (long)start, dst, n, &dma_mq
		);
		osRecvMesg(&dma_mq, &null_msg, OS_MESG_BLOCK);
		dst   += n;
		start += n;
		size  -= n;
	}
}
#endif

void *MemLoad(const char *start, const char *end, int mode)
{
	char *ptr;
	size_t size = ALIGN16(end-start);
	if ((ptr = MemAlloc(size, mode))) RomRead(ptr, start, end);
	return ptr;
}

void *MemLoadData(int seg, const char *start, const char *end, int mode)
{
	char *ptr;
	if ((ptr = MemLoad(start, end, mode))) SegmentSet(seg, ptr);
	return ptr;
}

void *MemLoadCode(char *addr, const char *start, const char *end)
{
	char *ptr = NULL;
	size_t srcsize = ALIGN16(end-start);
	size_t dstsize = ALIGN16((char *)mem_blockr - addr);
	if (srcsize <= dstsize)
	{
		if ((ptr = MemAlloc(dstsize, MEM_ALLOC_R)))
		{
			bzero(ptr, dstsize);
			osWritebackDCacheAll();
			RomRead(ptr, start, end);
			osInvalICache(ptr, dstsize);
			osInvalDCache(ptr, dstsize);
		}
	}
	else
	{
	}
	return ptr;
}

void *MemLoadPres(int seg, const char *start, const char *end)
{
	char *ptr = NULL;
	size_t srcsize = ALIGN16(end-start);
	char *src = MemAlloc(srcsize, MEM_ALLOC_R);
	u32 *dstsize = (u32 *)(src + 4);
	if (src)
	{
		RomRead(src, start, end);
		if ((ptr = MemAlloc(*dstsize, MEM_ALLOC_L)))
		{
			slidec(src, ptr);
			SegmentSet(seg, ptr);
			MemFree(src);
		}
		else
		{
		}
	}
	else
	{
	}
	return ptr;
}

void *MemLoadText(int seg, const char *start, const char *end)
{
	UNUSED char *ptr = NULL;
	size_t srcsize = ALIGN16(end-start);
	char *src = MemAlloc(srcsize, MEM_ALLOC_R);
	UNUSED u32 *dstsize = (u32 *)(src + 4);
	if (src)
	{
		RomRead(src, start, end);
		slidec(src, (char *)t_image);
		SegmentSet(seg, t_image);
		MemFree(src);
	}
	else
	{
	}
	return t_image;
}

extern const char _ulibSegmentRomStart[];
extern const char _ulibSegmentRomEnd[];

void MemLoadULib(void)
{
	char *addr = (char *)ADDRESS_ULIB;
	size_t dstsize = ADDRESS_ULIB_END-ADDRESS_ULIB;
	UNUSED size_t srcsize = ALIGN16(_ulibSegmentRomEnd-_ulibSegmentRomStart);
	bzero(addr, dstsize);
	osWritebackDCacheAll();
	RomRead(addr, _ulibSegmentRomStart, _ulibSegmentRomEnd);
	osInvalICache(addr, dstsize);
	osInvalDCache(addr, dstsize);
}

ARENA *ArenaCreate(size_t size, int mode)
{
	void *ptr;
	ARENA *arena = NULL;
	size = ALIGN4(size);
	if ((ptr = MemAlloc(size+sizeof(ARENA), mode)))
	{
		arena = ptr;
		arena->size  = size;
		arena->used  = 0;
		arena->start = (char *)((ARENA *)ptr + 1);
		arena->free  = (char *)((ARENA *)ptr + 1);
	}
	return arena;
}

void *ArenaAlloc(ARENA *arena, long size)
{
	void *ptr = NULL;
	size = ALIGN4(size);
	if (0 < size && arena->used+size <= arena->size)
	{
		ptr = arena->free;
		arena->free += size;
		arena->used += size;
	}
	return ptr;
}

void *ArenaResize(ARENA *arena, size_t size)
{
	void *ptr;
	size = ALIGN4(size);
	if ((ptr = MemRealloc(arena, size+sizeof(ARENA))))
	{
		arena->size = size;
	}
	return ptr;
}

HEAP *HeapCreate(size_t size, int mode)
{
	void *ptr;
	HEAP_BLOCK *block;
	HEAP *heap = NULL;
	size = ALIGN4(size);
	if ((ptr = MemAlloc(size+sizeof(HEAP), mode)))
	{
		heap = ptr;
		heap->size  = size;
		heap->block = (HEAP_BLOCK *)((HEAP *)ptr + 1);
		heap->free  = (HEAP_BLOCK *)((HEAP *)ptr + 1);
		block = heap->block;
		block->next = NULL;
		block->size = heap->size;
	}
	return heap;
}

void *HeapAlloc(HEAP *heap, size_t size)
{
	HEAP_BLOCK **free = &heap->free;
	void *ptr = NULL;
	size = ALIGN4(size) + sizeof(HEAP_BLOCK);
	while (*free)
	{
		if (size <= (*free)->size)
		{
			ptr = *free + 1;
			if ((*free)->size-size <= sizeof(HEAP_BLOCK))
			{
				*free = (*free)->next;
			}
			else
			{
				HEAP_BLOCK *block = (HEAP_BLOCK *)((char *)*free + size);
				block->size = (*free)->size - size;
				block->next = (*free)->next;
				(*free)->size = size;
				*free = block;
			}
			break;
		}
		free = &(*free)->next;
	}
	return ptr;
}

void HeapFree(HEAP *heap, void *addr)
{
	HEAP_BLOCK *block = (HEAP_BLOCK *)addr - 1;
	HEAP_BLOCK *free = heap->free;
	if (!heap->free)
	{
		heap->free = block;
		block->next = NULL;
	}
	else if (block < heap->free)
	{
		if (heap->free == (HEAP_BLOCK *)((char *)block + block->size))
		{
			block->size += free->size;
			block->next = free->next;
			heap->free = block;
		}
		else
		{
			block->next = heap->free;
			heap->free = block;
		}
	}
	else
	{
		while (free->next)
		{
			if (free < block && block < free->next) break;
			free = free->next;
		}
		if (block == (HEAP_BLOCK *)((char *)free + free->size))
		{
			free->size += block->size;
			block = free;
		}
		else
		{
			block->next = free->next;
			free->next = block;
		}
		if (
			block->next &&
			block->next == (HEAP_BLOCK *)((char *)block + block->size)
		)
		{
			block->size += block->next->size;
			block->next = block->next->next;
		}
	}
}

void *GfxAlloc(size_t size)
{
	void *ptr = NULL;
	size = ALIGN8(size);
	if (gfx_mem-size >= (char *)glistp)
	{
		gfx_mem -= size;
		ptr = gfx_mem;
	}
	else
	{
	}
	return ptr;
}

BANKINFO *BankLoadInfo(const char *src)
{
	BANKINFO *info = MemLoad(src, src+sizeof(info->len), MEM_ALLOC_L);
	size_t size =
		sizeof(BANKINFO)-sizeof(info->table) +
		sizeof(info->table[0])*info->len;
	MemFree(info);
	info = MemLoad(src, src+size, MEM_ALLOC_L);
	info->src = src;
	return info;
}

void BankInit(BANK *bank, const char *src, void *buf)
{
	if (src) bank->info = BankLoadInfo(src);
	bank->src = NULL;
	bank->buf = buf;
}

int BankLoad(BANK *bank, int index)
{
	int result = FALSE;
	BANKINFO *info = bank->info;
	if ((unsigned int)index < info->len)
	{
		const char *src  = info->table[index].start + info->src;
		size_t      size = info->table[index].size;
		if (bank->src != src)
		{
			RomRead(bank->buf, src, src+size);
			bank->src = src;
			result = TRUE;
		}
	}
	return result;
}

#ifdef DISK
void BankInitAnime(BANK *bank, const char *start, const char *end, void *buf)
{
	void *ptr = (void *)ADDRESS_ANIME;
	BANKINFO *info = (BANKINFO *)ptr;
	RomRead(ptr, start, end);
	bank->info = info;
	info->src = (const char *)ptr;
	bank->src = NULL;
	bank->buf = buf;
}

int BankLoadAnime(BANK *bank, int index)
{
	int result = FALSE;
	BANKINFO *info = bank->info;
	if ((unsigned int)index < info->len)
	{
		const char *src  = info->table[index].start + info->src;
		size_t      size = info->table[index].size;
		if (bank->src != src)
		{
			bcopy(src, bank->buf, size);
			bank->src = src;
			result = TRUE;
		}
	}
	return result;
}
#endif
