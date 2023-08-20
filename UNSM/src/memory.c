#include <sm64.h>

#define ALIGN4(x)   (((uintptr_t)(x)+ 3) & ~ 3)
#define ALIGN8(x)   (((uintptr_t)(x)+ 7) & ~ 7)
#define ALIGN16(x)  (((uintptr_t)(x)+15) & ~15)
#define BOUND16(x)  (((uintptr_t)(x)   ) & ~15)

uintptr_t segment_table[NUM_SEGMENTS+16];
size_t mem_size;
char *mem_start;
char *mem_end;
MEM_BLOCK *mem_blockl;
MEM_BLOCK *mem_blockr;
HEAP *mem_heap;
MEM_FRAME *mem_frame = NULL;

uintptr_t segment_set(int segment, void *addr)
{
	segment_table[segment] = K0_TO_PHYS(addr);
	return segment_table[segment];
}

void *segment_get(int segment)
{
	return (void *)PHYS_TO_K0(segment_table[segment]);
}

void *segment_to_virtual(const void *addr)
{
	int segment = (uintptr_t)addr >> 24;
	intptr_t offset = SEGMENT_OFFSET(addr);
	return (void *)PHYS_TO_K0(segment_table[segment] + offset);
}

void *virtual_to_segment(int segment, const void *addr)
{
	intptr_t offset = K0_TO_PHYS(addr) - segment_table[segment];
	return (void *)SEGMENT_ADDR(segment, offset);
}

void segment_write(void)
{
	int i;
	for (i = 0; i < 16; i++) gSPSegment(gfx_ptr++, i, segment_table[i]);
}

void mem_init(void *start, void *end)
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

void *mem_alloc(size_t size, int mode)
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

size_t mem_free(void *ptr)
{
	MEM_BLOCK *old = (MEM_BLOCK *)ptr - 1;
	MEM_BLOCK *new = (MEM_BLOCK *)ptr - 1;
	if (new < mem_blockl)
	{
		while (new->next) new = new->next;
		mem_blockl = old;
		mem_blockl->next = NULL;
		mem_size += (char *)new - (char *)mem_blockl;
	}
	else
	{
		while (new->prev) new = new->prev;
		mem_blockr = old->next;
		mem_blockr->prev = NULL;
		mem_size += (char *)mem_blockr - (char *)new;
	}
	return mem_size;
}

void *mem_realloc(void *ptr, size_t size)
{
	void *new = NULL;
	MEM_BLOCK *block = (MEM_BLOCK *)ptr - 1;
	if (block->next == mem_blockl)
	{
		mem_free(ptr);
		new = mem_alloc(size, MEM_ALLOC_L);
	}
	return new;
}

size_t mem_available(void)
{
	return mem_size - sizeof(MEM_BLOCK);
}

size_t mem_push(void)
{
	MEM_FRAME *frame  = mem_frame;
	size_t     size   = mem_size;
	MEM_BLOCK *blockl = mem_blockl;
	MEM_BLOCK *blockr = mem_blockr;
	mem_frame = mem_alloc(sizeof(MEM_FRAME), MEM_ALLOC_L);
	mem_frame->size   = size;
	mem_frame->blockl = blockl;
	mem_frame->blockr = blockr;
	mem_frame->frame  = frame;
	return mem_size;
}

size_t mem_pull(void)
{
	mem_size   = mem_frame->size;
	mem_blockl = mem_frame->blockl;
	mem_blockr = mem_frame->blockr;
	mem_frame  = mem_frame->frame;
	return mem_size;
}

void mem_dma(char *dst, const char *start, const char *end)
{
	size_t size = ALIGN16(end-start);
	osInvalDCache(dst, size);
	while (size > 0)
	{
		size_t n = size >= 0x1000 ? 0x1000 : size;
		osPiStartDma(
			&dma_mb, OS_MESG_PRI_NORMAL, OS_READ, (uintptr_t)start, dst, n,
			&dma_mq
		);
		osRecvMesg(&dma_mq, &null_msg, OS_MESG_BLOCK);
		dst   += n;
		start += n;
		size  -= n;
	}
}

void *mem_load(const char *start, const char *end, int mode)
{
	char *ptr;
	size_t size = ALIGN16(end-start);
	if ((ptr = mem_alloc(size, mode))) mem_dma(ptr, start, end);
	return ptr;
}

void *mem_load_data(int segment, const char *start, const char *end, int mode)
{
	char *ptr;
	if ((ptr = mem_load(start, end, mode))) segment_set(segment, ptr);
	return ptr;
}

void *mem_load_code(char *dst, const char *start, const char *end)
{
	char *ptr = NULL;
	size_t srcsize = ALIGN16(end-start);
	size_t dstsize = ALIGN16((char *)mem_blockr - dst);
	if (srcsize <= dstsize)
	{
		if ((ptr = mem_alloc(dstsize, MEM_ALLOC_R)))
		{
			bzero(ptr, dstsize);
			osWritebackDCacheAll();
			mem_dma(ptr, start, end);
			osInvalICache(ptr, dstsize);
			osInvalDCache(ptr, dstsize);
		}
	}
	else
	{
	}
	return ptr;
}

void *mem_load_szp(int segment, const char *start, const char *end)
{
	char *ptr = NULL;
	size_t srcsize = ALIGN16(end-start);
	char *src = mem_alloc(srcsize, MEM_ALLOC_R);
	u32 *dstsize = (u32 *)(src + 4);
	if (src)
	{
		mem_dma(src, start, end);
		if ((ptr = mem_alloc(*dstsize, MEM_ALLOC_L)))
		{
			slidec(src, ptr);
			segment_set(segment, ptr);
			mem_free(src);
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

void *mem_load_txt(int segment, const char *start, const char *end)
{
	UNUSED char *ptr = NULL;
	size_t srcsize = ALIGN16(end-start);
	char *src = mem_alloc(srcsize, MEM_ALLOC_R);
	UNUSED u32 *dstsize = (u32 *)(src + 4);
	if (src)
	{
		mem_dma(src, start, end);
		slidec(src, (char *)t_image);
		segment_set(segment, t_image);
		mem_free(src);
	}
	else
	{
	}
	return t_image;
}

extern const char _ulibSegmentRomStart[];
extern const char _ulibSegmentRomEnd[];

void mem_load_ulib(void)
{
	char *addr = (char *)ADDRESS_ULIB;
	size_t dstsize = ADDRESS_CIMG-ADDRESS_ULIB;
	UNUSED size_t srcsize = ALIGN16(_ulibSegmentRomEnd-_ulibSegmentRomStart);
	bzero(addr, dstsize);
	osWritebackDCacheAll();
	mem_dma(addr, _ulibSegmentRomStart, _ulibSegmentRomEnd);
	osInvalICache(addr, dstsize);
	osInvalDCache(addr, dstsize);
}

ARENA *arena_init(size_t size, int mode)
{
	void *ptr;
	ARENA *arena = NULL;
	size = ALIGN4(size);
	if ((ptr = mem_alloc(size+sizeof(ARENA), mode)))
	{
		arena = ptr;
		arena->size  = size;
		arena->used  = 0;
		arena->start = (char *)((ARENA *)ptr + 1);
		arena->free  = (char *)((ARENA *)ptr + 1);
	}
	return arena;
}

void *arena_alloc(ARENA *arena, long size)
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

void *arena_resize(ARENA *arena, size_t size)
{
	void *ptr;
	size = ALIGN4(size);
	if ((ptr = mem_realloc(arena, size+sizeof(ARENA))))
	{
		arena->size = size;
	}
	return ptr;
}

HEAP *heap_init(size_t size, int mode)
{
	void *ptr;
	HEAP_BLOCK *block;
	HEAP *heap = NULL;
	size = ALIGN4(size);
	if ((ptr = mem_alloc(size+sizeof(HEAP), mode)))
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

void *heap_alloc(HEAP *heap, size_t size)
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

void heap_free(HEAP *heap, void *addr)
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

void *gfx_alloc(size_t size)
{
	void *ptr = NULL;
	size = ALIGN8(size);
	if (gfx_mem-size >= (char *)gfx_ptr)
	{
		gfx_mem -= size;
		ptr = gfx_mem;
	}
	else
	{
	}
	return ptr;
}

BANK_TABLE *bank_table_init(const char *src)
{
	BANK_TABLE *table = mem_load(src, src+sizeof(table->len), MEM_ALLOC_L);
	size_t size =
		sizeof(BANK_TABLE)-sizeof(table->table) +
		sizeof(table->table[0])*table->len;
	mem_free(table);
	table = mem_load(src, src+size, MEM_ALLOC_L);
	table->src = src;
	return table;
}

void bank_init(BANK *bank, const char *src, void *buf)
{
	if (src) bank->table = bank_table_init(src);
	bank->src = NULL;
	bank->buf = buf;
}

int bank_load(BANK *bank, unsigned int index)
{
	int flag = FALSE;
	BANK_TABLE *table = bank->table;
	if (index < table->len)
	{
		const char *src  = table->table[index].start + table->src;
		size_t      size = table->table[index].size;
		if (bank->src != src)
		{
			mem_dma(bank->buf, src, src+size);
			bank->src = src;
			flag = TRUE;
		}
	}
	return flag;
}
