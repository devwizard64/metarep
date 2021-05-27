#ifndef _SM64_SEGMENT_H_
#define _SM64_SEGMENT_H_

#define SEGMENT_CIMG            0x8038F800
#define SEGMENT_ZIMG            0x80000400
#define SEGMENT_MEM_START       0x8005C000
#define SEGMENT_MEM_END         0x801C1000
#define SEGMENT_BUFFER          0x801C1000
#define SEGMENT_FIFO            0x80227000
#define SEGMENT_MAIN            0x80246000
#define SEGMENT_MAIN2           0x80378800
#define SEGMENT_MENU            0x8016F000

#define SEGMENT_DATA_FACE       0x04000000

#define SEGMENT_VIDEO           0x01000000
#define SEGMENT_SZP_MAIN        0x02000000
#define SEGMENT_SZP_ENTITY      0x03000000
#define SEGMENT_SZP_PLAYER      0x04000000
#define SEGMENT_SZP_GFXA        0x05000000
#define SEGMENT_SZP_GFXB        0x06000000
#define SEGMENT_SZP_STAGE       0x07000000
#define SEGMENT_SZP_MENU        0x07000000
#define SEGMENT_SZP_GFXC        0x08000000
#define SEGMENT_SZP_TEXTURE     0x09000000
#define SEGMENT_SZP_BACKGROUND  0x0A000000
#define SEGMENT_SZP_PARTICLE    0x0B000000
#define SEGMENT_DATA_GFXA       0x0C000000
#define SEGMENT_DATA_GFXB       0x0D000000
#define SEGMENT_DATA_STAGE      0x0E000000
#define SEGMENT_DATA_GFXC       0x0F000000
#define SEGMENT_DATA_MAIN       0x10000000
#define SEGMENT_MOTION_MARIO    0x11000000
#define SEGMENT_MOTION_LUIGI    0x12000000
#define SEGMENT_DATA_OBJECT     0x13000000
#define SEGMENT_DATA_MENU       0x14000000
#define SEGMENT_DATA_GAME       0x15000000
#define SEGMENT_DATA_ENTITY     0x16000000
#define SEGMENT_DATA_PLAYER     0x17000000
#define SEGMENT_DEMO            0x18000000

#endif /* _SM64_SEGMENT_H_ */
