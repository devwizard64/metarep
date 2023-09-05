#ifndef __SM64_TYPES_H__
#define __SM64_TYPES_H__

#ifndef __GNUC__
#define __attribute__(x)
#endif

#define DALIGN                  __attribute__((aligned(4)))
#define BALIGN                  __attribute__((aligned(8)))
#define UNUSED                  __attribute__((unused))
#define FALLTHROUGH             __attribute__((fallthrough))

#define lenof(x)                (sizeof((x)) / sizeof((x)[0]))

typedef short VECS[3];
typedef float VECF[3];
typedef float MTXF[4][4];

#ifdef sgi
typedef signed char CHAR;
typedef unsigned char UCHAR;
typedef short SHORT;
typedef unsigned short USHORT;
typedef double DOUBLE;
#else
typedef int CHAR;
typedef unsigned int UCHAR;
typedef int SHORT;
typedef unsigned int USHORT;
typedef float DOUBLE;
#endif

typedef short TAG;
typedef short MAP;
typedef char AREA;
typedef short PATH;

typedef uintptr_t S_SCRIPT;
typedef char P_SCRIPT;
typedef uintptr_t O_SCRIPT;

typedef int PRGCALL(SHORT arg, int code);
typedef void OBJCALL(void);

#endif /* __SM64_TYPES_H__ */
