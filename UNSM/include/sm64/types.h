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

#ifdef DEBUG
#define debugf(x) osSyncPrintf x
#else
#define debugf(x)
#endif

#ifdef sgi
#define ISFALSE(x)              ((x) == FALSE)
#define ISTRUE(x)               ((x) == TRUE)
#define STATIC
typedef signed char CHAR;
typedef unsigned char UCHAR;
typedef short SHORT;
typedef unsigned short USHORT;
typedef int VOID;
#else
#define ISFALSE(x)              (!(x))
#define ISTRUE(x)               (x)
#define STATIC                  static
typedef int CHAR;
typedef int UCHAR;
typedef int SHORT;
typedef int USHORT;
typedef void VOID;
#endif

typedef short SVEC[3];
typedef float FVEC[3];
typedef float FMTX[4][4];

typedef short TAG;
typedef short MAP;
typedef char AREA;
typedef short PATH;

typedef unsigned long SHPLANG;
typedef char SEQLANG;
typedef unsigned long OBJLANG;

typedef long SEQCALL(SHORT code, long status);
typedef void OBJCALL(void);

#endif /* __SM64_TYPES_H__ */
