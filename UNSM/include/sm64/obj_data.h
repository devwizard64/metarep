#ifndef _SM64_OBJ_DATA_H_
#define _SM64_OBJ_DATA_H_

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct obj_data
{
    /* 0x00 */  const uintptr_t *script;
    /* 0x04 */  s16     g;
    /* 0x06 */  s16     arg;
};  /* 0x08 */

struct map_obj
{
    /* 0x00 */  u8      index;
    /* 0x01 */  u8      type;
    /* 0x02 */  u8      arg;
    /* 0x03 */  u8      g;
    /* 0x04 */  const uintptr_t *script;
};  /* 0x08 */

#else /* __ASSEMBLER__ */

#define obj_data__script        0x00
#define obj_data__g             0x04
#define obj_data__arg           0x06
#define sizeof__obj_data        0x08

#define map_obj__index          0x00
#define map_obj__type           0x01
#define map_obj__arg            0x02
#define map_obj__g              0x03
#define map_obj__script         0x04
#define sizeof__map_obj         0x08

#endif /* __ASSEMBLER__ */

#endif /* _SM64_OBJ_DATA_H_ */
