#include <sm64.h>

extern u16 *txt_glbfont[];
extern Gfx gfx_print_copy_begin[];
extern Gfx gfx_print_copy_char[];
extern Gfx gfx_print_copy_end[];

typedef struct dprint
{
	int x;
	int y;
	short len;
	char str[50];
}
DPRINT;

static DPRINT *dplist[50];
static short nprint = 0;

static unsigned int Powi(int base, int exponent)
{
	unsigned int x = 1;
	int i;
	for (i = 0; i < exponent; i++) x = x*base;
	return x;
}

static void dpFormat(
	int value, int base, char *buf, int *index, UCHAR digit, CHAR zero
)
{
	unsigned int power;
	int e = 0;
	int n, i = 0;
	CHAR c;
	char minus = FALSE;
	char pad = ISTRUE(zero) ? '0' : -1;
	if (value != 0)
	{
		if (value < 0)
		{
			value = -value;
			minus = TRUE;
		}
		/* can hang */
		for (;;)
		{
			power = Powi(base, e);
			if (power > (unsigned int)value) break;
			e++;
		}
		if (digit > e)
		{
			for (i = 0; i < digit-e; i++) *(buf+i) = pad;
			if (ISTRUE(minus)) i--;
		}
		if (ISTRUE(minus))
		{
			*(buf+i) = 'M';
			i++;
		}
		for (n = e-1; n >= 0; n--)
		{
			power = Powi(base, n);
			c = value / power;
			if (c < 10) *(buf+i+e-1-n) = '0' + c- 0;
			else        *(buf+i+e-1-n) = 'A' + c-10;
			value -= c*power;
		}
	}
	else
	{
		e = 1;
		if (digit > e)
		{
			for (i = 0; i < digit-e; i++) *(buf+i) = pad;
		}
		*(buf+i) = '0';
	}
	*index += e + i;
}

static void dpGetFmt(const char *fmt, int *index, u8 *digit, char *zero)
{
	char buf[10];
	CHAR n = 0;
	SHORT i;
	if (fmt[*index] == '0') *zero = TRUE;
	while (fmt[*index] != 'd' && fmt[*index] != 'x')
	{
		buf[n] = fmt[*index] - '0';
		if (buf[n] < 0 || buf[n] > 9)
		{
			*digit = 0;
			return;
		}
		n++;
		(*index)++;
	}
	if (n == 0) return;
	for (i = 0; i < n-1; i++) *digit = *digit + 10*(n-1-i)*buf[i];
	*digit = *digit + buf[n-1];
}

void dprintf(int x, int y, const char *fmt, int value)
{
	char c = 0, zero = FALSE;
	u8 digit = 0;
	int base = 0, n = 0, i = 0;
	if (!(dplist[nprint] = malloc(sizeof(DPRINT)))) return;
	dplist[nprint]->x = x;
	dplist[nprint]->y = y;
	c = fmt[i];
	while (c != '\0')
	{
		if (c == '%')
		{
			i++;
			dpGetFmt(fmt, &i, &digit, &zero);
			if (fmt[i] != 'd' && fmt[i] != 'x') break;
			if (fmt[i] == 'd') base = 10;
			if (fmt[i] == 'x') base = 16;
			i++;
			dpFormat(value, base, &dplist[nprint]->str[n], &n, digit, zero);
		}
		else
		{
			dplist[nprint]->str[n] = c;
			n++;
			i++;
		}
		c = fmt[i];
	}
	dplist[nprint]->len = n;
	nprint++;
}

void dprint(int x, int y, const char *str)
{
	char c = 0;
	int n = 0, i = 0;
	if (!(dplist[nprint] = malloc(sizeof(DPRINT)))) return;
	dplist[nprint]->x = x;
	dplist[nprint]->y = y;
	c = str[i];
	while (c != '\0')
	{
		dplist[nprint]->str[n] = c;
		n++;
		i++;
		c = str[i];
	}
	dplist[nprint]->len = n;
	nprint++;
}

void dprintc(int x, int y, const char *str)
{
	char c = 0;
	UNUSED u8 digit = 0;
	UNUSED int base = 0;
	int n = 0, i = 0;
	if (!(dplist[nprint] = malloc(sizeof(DPRINT)))) return;
	c = str[i];
	while (c != '\0')
	{
		dplist[nprint]->str[n] = c;
		n++;
		i++;
		c = str[i];
	}
	dplist[nprint]->len = n;
	dplist[nprint]->x = x - 12*n/2;
	dplist[nprint]->y = y;
	nprint++;
}

static CHAR dpCvt(CHAR c)
{
	if (c >= 'A' && c <= 'Z') return CH_A + c-'A';
	if (c >= 'a' && c <= 'z') return CH_A + c-'a';
	if (c >= '0' && c <= '9') return CH_0 + c-'0';
	if (c == ' ') return CH16_SPACE;
	if (c == '!') return CH16_BANG;
	if (c == '#') return CH16_BANGBANG;
	if (c == '?') return CH16_QUESTION;
	if (c == '&') return CH16_AMPERSAND;
	if (c == '%') return CH16_PERCENT;
	if (c == '*') return CH16_CROSS;
	if (c == '+') return CH16_COIN;
	if (c == ',') return CH16_MARIO;
	if (c == '-') return CH16_STAR;
	if (c == '.') return CH16_SHADOW;
	if (c == '/') return CH16_KEY;
	return -1;
}

static void dpDrawTxt(CHAR c)
{
	u16 **txt = SegmentToVirtual(txt_glbfont);
	gDPPipeSync(glistp++);
	gDPSetTextureImage(glistp++, G_IM_FMT_RGBA, G_IM_SIZ_16b, 1, txt[c]);
	gSPDisplayList(glistp++, gfx_print_copy_char);
}

static void dpClamp(int *x, int *y)
{
	if (*x <           10) *x =           10;
	if (*x > SCREEN_WD-20) *x = SCREEN_WD-20;
	if (*y <            5) *y =            5;
	if (*y > SCREEN_HT-20) *y = SCREEN_HT-20;
}

static void dpDrawChar(int x, int y, int n)
{
	int sx = 12*n + x;
	int sy = SCREEN_HT - (y+16);
	unsigned int ux, uy;
	dpClamp(&sx, &sy);
	ux = sx;
	uy = sy;
	gSPTextureRectangle(
		glistp++, ux << 2, uy << 2, (ux+16-1) << 2, (uy+16-1) << 2,
		G_TX_RENDERTILE, 0, 0, 4 << 10, 1 << 10
	);
}

void dprintDraw(void)
{
	int i, n;
	CHAR c;
	Mtx *mtx;
	if (nprint == 0) return;
	if (!(mtx = GfxAlloc(sizeof(Mtx))))
	{
		nprint = 0; /* memory leak */
		return;
	}
	guOrtho(mtx, 0, SCREEN_WD, 0, SCREEN_HT, -10, 10, 1);
	gSPPerspNormalize(glistp++, 0xFFFF);
	gSPMatrix(
		glistp++, K0_TO_PHYS(mtx), G_MTX_PROJECTION|G_MTX_LOAD|G_MTX_NOPUSH
	);
	gSPDisplayList(glistp++, gfx_print_copy_begin);
	for (i = 0; i < nprint; i++)
	{
		for (n = 0; n < dplist[i]->len; n++)
		{
			if ((c = dpCvt(dplist[i]->str[n])) != -1)
			{
#ifdef MULTILANG
				if (c == CH16_U_UMLAUT)
				{
					dpDrawTxt(CH_U);
					dpDrawChar(dplist[i]->x, dplist[i]->y, n);
					dpDrawTxt(CH16_UMLAUT);
					dpDrawChar(dplist[i]->x, dplist[i]->y+3, n);
				}
				else
				{
					dpDrawTxt(c);
					dpDrawChar(dplist[i]->x, dplist[i]->y, n);
				}
#else
				dpDrawTxt(c);
				dpDrawChar(dplist[i]->x, dplist[i]->y, n);
#endif
			}
		}
		free(dplist[i]);
	}
	gSPDisplayList(glistp++, gfx_print_copy_end);
	nprint = 0;
}
