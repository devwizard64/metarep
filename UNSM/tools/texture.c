#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "lodepng/lodepng.h"
#include "lodepng/lodepng.cpp"

#define CVT(x, s, n)    ((2*((1 << (s))-1)*(x)+0xFF) / (2*0xFF*(n)))
#define R(p, s) CVT((p)->r, s, 1)
#define G(p, s) CVT((p)->g, s, 1)
#define B(p, s) CVT((p)->b, s, 1)
#define A(p, s) CVT((p)->a, s, 1)
#define I(p, s) CVT((p)->r+(p)->g+(p)->b, s, 3)
#define R8(p)   ((p)->r)
#define G8(p)   ((p)->g)
#define B8(p)   ((p)->b)
#define A8(p)   ((p)->a)
#define I8(p)   (((p)->r+(p)->g+(p)->b+1)/3)
#define A1(p)   ((p)->a >> 7)

typedef struct rgba
{
	unsigned char r, g, b, a;
}
RGBA;

static int palette(const RGBA *src, const RGBA *pal, int len)
{
	int i;
	for (i = 0; i < len; i++)
	{
		if (!memcmp(src, pal+i, sizeof(RGBA))) return i;
	}
	return 0;
}

static void convert_rgba16(unsigned w, unsigned h, const RGBA *src)
{
	unsigned y, x;
	for (y = 0; y < h; y++)
	{
		for (x = 0; x < w; x++, src++) printf(
			"0x%04X,",
			R(src, 5) << 11 | G(src, 5) << 6 | B(src, 5) << 1 | A1(src)
		);
		putchar('\n');
	}
}

static void convert_rgba32(unsigned w, unsigned h, const RGBA *src)
{
	unsigned y, x;
	for (y = 0; y < h; y++)
	{
		for (x = 0; x < w; x++, src++) printf(
			"0x%08X,", R8(src) << 24 | G8(src) << 16 | B8(src) << 8 | A8(src)
		);
		putchar('\n');
	}
}

static void convert_ci4(
	unsigned w, unsigned h, const RGBA *src, const RGBA *pal
)
{
	unsigned y, x;
	for (y = 0; y < h; y++)
	{
		for (x = 0; x < w; x += 2, src += 2) printf(
			"0x%02X,", palette(src+0, pal, 16) << 4 | palette(src+1, pal, 16)
		);
		putchar('\n');
	}
}

static void convert_ci8(
	unsigned w, unsigned h, const RGBA *src, const RGBA *pal
)
{
	unsigned y, x;
	for (y = 0; y < h; y++)
	{
		for (x = 0; x < w; x++, src++) printf(
			"0x%02X,", palette(src, pal, 256)
		);
		putchar('\n');
	}
}

static void convert_ia4(unsigned w, unsigned h, const RGBA *src)
{
	unsigned y, x;
	for (y = 0; y < h; y++)
	{
		for (x = 0; x < w; x += 2, src += 2) printf(
			"0x%02X,",
			I(src+0, 3) << 5 | A1(src+0) << 4 | I(src+1, 3) << 1 | A1(src+1)
		);
		putchar('\n');
	}
}

static void convert_ia8(unsigned w, unsigned h, const RGBA *src)
{
	unsigned y, x;
	for (y = 0; y < h; y++)
	{
		for (x = 0; x < w; x++, src++) printf(
			"0x%02X,", I(src, 4) << 4 | A(src, 4)
		);
		putchar('\n');
	}
}

static void convert_ia16(unsigned w, unsigned h, const RGBA *src)
{
	unsigned y, x;
	for (y = 0; y < h; y++)
	{
		for (x = 0; x < w; x++, src++) printf(
			"0x%04X,", I8(src) << 8 | A8(src)
		);
		putchar('\n');
	}
}

static void convert_i4(unsigned w, unsigned h, const RGBA *src)
{
	unsigned y, x;
	for (y = 0; y < h; y++)
	{
		for (x = 0; x < w; x += 2, src += 2) printf(
			"0x%02X,", I(src+0, 4) << 4 | I(src+1, 4)
		);
		putchar('\n');
	}
}

static void convert_i8(unsigned w, unsigned h, const RGBA *src)
{
	unsigned y, x;
	for (y = 0; y < h; y++)
	{
		for (x = 0; x < w; x++, src++) printf("0x%02X,", I8(src));
		putchar('\n');
	}
}

typedef struct texture
{
	const char *fmt;
	void (*convert)();
	unsigned int palette;
}
TEXTURE;

static const TEXTURE texturetab[] =
{
	{".rgba16.", convert_rgba16, 0},
	{".rgba32.", convert_rgba32, 0},
	{".ci4.", convert_ci4, 16},
	{".ci8.", convert_ci8, 256},
	{".ia4.", convert_ia4, 0},
	{".ia8.", convert_ia8, 0},
	{".ia16.", convert_ia16, 0},
	{".i4.", convert_i4, 0},
	{".i8.", convert_i8, 0},
	{0},
};

int usage(const char *path)
{
	fprintf(stderr, "usage: %s <texture> [palette]\n", path);
	return 1;
}

int main(int argc, char *argv[])
{
	const TEXTURE *txt = NULL;
	unsigned char *src = NULL, *pal = NULL;
	unsigned error, w, h, pal_w, pal_h;
	if (argc < 2 || argc > 3) return usage(argv[0]);
	for (txt = texturetab; txt->fmt; txt++)
	{
		if (strstr(argv[1], txt->fmt)) break;
	}
	if (!(txt->fmt))
	{
		fprintf(stderr, "error: invalid format\n");
		return 1;
	}
	if ((error = lodepng_decode32_file(&src, &w, &h, argv[1])))
	{
		fprintf(stderr, "error %u: %s\n", error, lodepng_error_text(error));
		return 1;
	}
	if (txt->palette > 0)
	{
		if (argc < 3)
		{
			fprintf(stderr, "error: palette not specified\n");
			return 1;
		}
		if ((error = lodepng_decode32_file(&pal, &pal_w, &pal_h, argv[2])))
		{
			fprintf(stderr, "error %u: %s\n", error, lodepng_error_text(error));
			return 1;
		}
		if (pal_w*pal_h < txt->palette)
		{
			fprintf(stderr, "error: palette is too small\n");
			return 1;
		}
	}
	else
	{
		if (argc > 2) return usage(argv[0]);
	}
	txt->convert(w, h, src, pal);
	free(src);
	free(pal);
	return 0;
}
