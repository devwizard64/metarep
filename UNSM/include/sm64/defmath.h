#ifndef __SM64_DEFMATH_H__
#define __SM64_DEFMATH_H__

#define COS_1       0.9998477F
#define COS_5       0.9961947F
#define COS_10      0.9848077F
#define COS_15      0.9659258F
#define COS_20      0.9396926F
#define COS_25      0.9063078F
#define COS_30      0.8660254F
#define COS_38      0.7880108F
#define COS_73      0.2923717F
#define COS_80      0.17364818F
#define COS_90      0.0000000F

#define DEG(x)                  ((x)*0x8000/180)

#define ABS(x)                  ((x) > 0 ? (x) : -(x))
#define SQUARE(x)               ((x)*(x))

#define CROSS3(x0, y0, x1, y1, x2, y2) \
	(((y1)-(y0))*((x2)-(x1)) - ((x1)-(x0))*((y2)-(y1)))

#endif /* __SM64_DEFMATH_H__ */
