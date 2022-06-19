#include <sm64/types.h>
#include <sm64/segment.h>
#include <sm64/app.h>
#include <sm64/mem.h>
#include <sm64/slidec.h>
#include <sm64/timg.h>

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
    uint segment = (unsigned int)addr >> 24;
    uint offset  = SEGMENT_OFFSET(addr);
    return (void *)PHYS_TO_K0(segment_table[segment] + offset);
}

void *virtual_to_segment(int segment, const void *addr)
{
    uint offset = K0_TO_PHYS(addr) - segment_table[segment];
    return (void *)SEGMENT_ADDR(segment, offset);
}

void segment_write(void)
{
    int i;
    for (i = 0; i < 16; i++) gSPSegment(video_gfx++, i, segment_table[i]);
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
        while (new->next != NULL) new = new->next;
        mem_blockl = old;
        mem_blockl->next = NULL;
        mem_size += (char *)new - (char *)mem_blockl;
    }
    else
    {
        while (new->prev != NULL) new = new->prev;
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
    if ((ptr = mem_alloc(size, mode)) != NULL) mem_dma(ptr, start, end);
    return ptr;
}

void *mem_load_data(int segment, const char *start, const char *end, int mode)
{
    char *ptr;
    if ((ptr = mem_load(start, end, mode)) != NULL) segment_set(segment, ptr);
    return ptr;
}

void *mem_load_code(char *dst, const char *start, const char *end)
{
    char *ptr = NULL;
    size_t devsize = ALIGN16(end-start);
    size_t alcsize = ALIGN16((char *)mem_blockr - dst);
    if (devsize <= alcsize)
    {
        if ((ptr = mem_alloc(alcsize, MEM_ALLOC_R)) != NULL)
        {
            bzero(ptr, alcsize);
            osWritebackDCacheAll();
            mem_dma(ptr, start, end);
            osInvalICache(ptr, alcsize);
            osInvalDCache(ptr, alcsize);
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
    size_t devsize = ALIGN16(end-start);
    char *src = mem_alloc(devsize, MEM_ALLOC_R);
    u32 *alcsize = (u32 *)(src + 4);
    if (src != NULL)
    {
        mem_dma(src, start, end);
        if ((ptr = mem_alloc(*alcsize, MEM_ALLOC_L)) != NULL)
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
    unused char *ptr = NULL;
    size_t devsize = ALIGN16(end-start);
    char *src = mem_alloc(devsize, MEM_ALLOC_R);
    unused u32 *alcsize = (u32 *)(src + 4);
    if (src != NULL)
    {
        mem_dma(src, start, end);
        slidec(src, (char *)texture_buffer);
        segment_set(segment, texture_buffer);
        mem_free(src);
    }
    else
    {
    }
    return texture_buffer;
}

extern const char _libSegmentRomStart[];
extern const char _libSegmentRomEnd[];

void mem_load_lib(void)
{
    char *addr = (char *)SEGMENT_LIB;
    size_t alcsize = SEGMENT_CIMG-SEGMENT_LIB;
    unused size_t devsize = ALIGN16(_libSegmentRomEnd-_libSegmentRomStart);
    bzero(addr, alcsize);
    osWritebackDCacheAll();
    mem_dma(addr, _libSegmentRomStart, _libSegmentRomEnd);
    osInvalICache(addr, alcsize);
    osInvalDCache(addr, alcsize);
}

ARENA *arena_init(size_t size, int mode)
{
    void *ptr;
    ARENA *arena = NULL;
    size = ALIGN4(size);
    if ((ptr = mem_alloc(size+sizeof(ARENA), mode)) != NULL)
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
    if ((ptr = mem_realloc(arena, size+sizeof(ARENA))) != NULL)
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
    if ((ptr = mem_alloc(size+sizeof(HEAP), mode)) != NULL)
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
    while (*free != NULL)
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
    if (heap->free == NULL)
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
        while (free->next != NULL)
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
            block->next != NULL &&
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
    if (video_mem-size >= (char *)video_gfx)
    {
        video_mem -= size;
        ptr = video_mem;
    }
    else
    {
    }
    return ptr;
}

FILE_TABLE *file_init_table(const char *src)
{
    FILE_TABLE *table = mem_load(src, src+sizeof(table->len), MEM_ALLOC_L);
    size_t size =
        sizeof(FILE_TABLE)-sizeof(table->table) +
        sizeof(table->table[0])*table->len;
    mem_free(table);
    table = mem_load(src, src+size, MEM_ALLOC_L);
    table->src = src;
    return table;
}

void file_init(FILE *file, const char *src, void *buf)
{
    if (src != NULL) file->table = file_init_table(src);
    file->src = NULL;
    file->buf = buf;
}

int file_update(FILE *file, uint index)
{
    int flag = FALSE;
    FILE_TABLE *table = file->table;
    if (index < table->len)
    {
        const char *src  = table->table[index].start + table->src;
        size_t      size = table->table[index].size;
        if (file->src != src)
        {
            mem_dma(file->buf, src, src+size);
            file->src = src;
            flag = TRUE;
        }
    }
    return flag;
}
