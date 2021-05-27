#ifndef _SM64_MAIN_H_
#define _SM64_MAIN_H_

#include <sm64/types.h>

#ifndef __ASSEMBLER__

struct sptask
{
    /* 0x00 */  OSTask  task;
    /* 0x40 */  OSMesgQueue *mq;
    /* 0x44 */  OSMesg  msg;
    /* 0x48 */  int     state;
};  /* 0x50 */

struct vq
{
    /* 0x00 */  OSMesgQueue *mq;
    /* 0x04 */  OSMesg  msg;
};  /* 0x08 */

#else /* __ASSEMBLER__ */

#define sptask__task            0x00
#define sptask__mq              0x40
#define sptask__msg             0x44
#define sptask__state           0x48
#define sizeof__sptask          0x50

#define vq__mq                  0x00
#define vq__msg                 0x04
#define sizeof__vq              0x08

#endif /* __ASSEMBLER__ */

#endif /* _SM64_MAIN_H_ */
