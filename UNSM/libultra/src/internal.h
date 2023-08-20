#ifndef __INTERNAL_H__
#define __INTERNAL_H__

#ifndef __GNUC__
#define __attribute__(x)
#endif

#define DALIGN                  __attribute__((aligned(4)))
#define BALIGN                  __attribute__((aligned(8)))

typedef struct
{
	OSThread *next;
	OSPri priority;
}
__OSThreadTail;

typedef struct
{
	OSMesgQueue *messageQueue;
	OSMesg message;
}
__OSEventState;

typedef struct
{
	u16 _00;
	u16 _02;
	void *_04;
	OSViMode *_08;
	u32 _0C;
	OSMesgQueue *_10;
	OSMesg *_14;
	f32 _18;
	u16 _1C;
	u32 _20;
	f32 _24;
	u16 _28;
	u32 _2C;
}
__OSViContext;

#endif /* __INTERNAL_H__ */
