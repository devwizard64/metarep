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

#define _STR(x)                 #x
#define STR(x)                  _STR(x)
#define _BUILDPATH(x)           BUILD/x
#define BUILDPATH(x)            STR(_BUILDPATH(x))

typedef short VECS[3];
typedef float VECF[3];
typedef float MTXF[4][4];

#ifdef sgi
typedef signed char CHAR;
typedef unsigned char UCHAR;
typedef short SHORT;
typedef unsigned short USHORT;
#else
typedef int CHAR;
typedef unsigned int UCHAR;
typedef int SHORT;
typedef unsigned int USHORT;
#endif

typedef uintptr_t S_SCRIPT;
typedef uintptr_t P_SCRIPT;
typedef uintptr_t O_SCRIPT;
typedef void O_CALLBACK(void);

typedef short OBJ_DATA;
typedef short MAP_DATA;
typedef u8 AREA_DATA;
typedef short PATH_DATA;

typedef struct dummy0 DUMMY0;
typedef struct dummy1 DUMMY1;

#endif /* __SM64_TYPES_H__ */
