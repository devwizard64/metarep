#ifndef _SM64_MEM_H_
#define _SM64_MEM_H_

#include <sm64/types.h>

#define MEM_ALLOC_L 0
#define MEM_ALLOC_R 1

#ifndef __ASSEMBLER__

struct mem_link
{
    /* 0x00 */  struct mem_link *prev;
    /* 0x04 */  struct mem_link *next;
    /* 0x08 */  u64     pad;
};  /* 0x10 */

struct mem
{
    /* 0x00 */  size_t  size;
    /* 0x04 */  struct mem_link *l;
    /* 0x08 */  struct mem_link *r;
    /* 0x0C */  struct mem *mem;
};  /* 0x10 */

struct arena
{
    /* 0x00 */  size_t  size;
    /* 0x04 */  size_t  used;
    /* 0x08 */  u8     *start;
    /* 0x0C */  u8     *free;
};  /* 0x10 */

struct heap_link
{
    /* 0x00 */  struct heap_link *next;
    /* 0x04 */  size_t  size;
};  /* 0x08 */

struct heap
{
    /* 0x00 */  size_t  size;
    /* 0x04 */  struct heap_link *start;
    /* 0x08 */  struct heap_link *free;
    /* 0x0C */  u32     pad;
};  /* 0x10 */

struct file_meta
{
    /* 0x00 */  uint    len;
    /* 0x04 */  void   *src;
    /* 0x08 */  struct
                {
                    /* 0x00 */  uint    start;
                    /* 0x04 */  uint    size;
                }
                table[1];
};

struct file
{
    /* 0x00 */  struct file_meta *meta;
    /* 0x04 */  void    *current;
    /* 0x08 */  void    *dst;
};  /* 0x0C */

#else  /* __ASSEMBLER__ */

#define mem_link__prev          0x00
#define mem_link__next          0x04
#define sizeof__mem_link        0x10

#define mem__size               0x00
#define mem__l                  0x04
#define mem__r                  0x08
#define mem__mem                0x0C
#define sizeof__mem             0x10

#define arena__size             0x00
#define arena__used             0x04
#define arena__start            0x08
#define arena__free             0x0C
#define sizeof__arena           0x10

#define heap_link__next         0x00
#define heap_link__size         0x04
#define sizeof__heap_link       0x08

#define heap__size              0x00
#define heap__start             0x04
#define heap__free              0x08
#define sizeof__heap            0x10

#define file_meta__len          0x00
#define file_meta__src          0x04
#define file_meta__table        0x08
#define file_meta__table__start 0x00
#define file_meta__table__size  0x04
#define sizeof__file_meta       0x08

#define file__meta              0x00
#define file__current           0x04
#define file__dst               0x08
#define sizeof__file            0x0C

#endif /* __ASSEMBLER__ */

#endif /* _SM64_MEM_H_ */
