#include <sm64/types.h>
#include <sm64/main.h>
#include <sm64/app.h>
#include <sm64/mem.h>
#include <sm64/dprint.h>

DPRINT *dprint_table[50];
s16 dprint_index = 0;

static uint dprint_powi(int base, int exponent)
{
    uint x = 1;
    int i;
    for (i = 0; i < exponent; i++) x = x*base;
    return x;
}

static void dprintf_write(
    int value, int base, char *buf, int *index, u8 digit, s8 zero
)
{
    uint power;
    int e = 0;
    int n;
    int i = 0;
    s8 c;
    s8 minus = false;
    char pad = zero == true ? '0' : -1;
    if (value != 0)
    {
        if (value < 0)
        {
            value = -value;
            minus = true;
        }
        /* can hang */
        while (true)
        {
            power = dprint_powi(base, e);
            if (power > (uint)value) break;
            e++;
        }
        if (digit > e)
        {
            for (i = 0; i < digit-e; i++) *(buf+i) = pad;
            if (minus == true) i--;
        }
        if (minus == true)
        {
            *(buf+i) = 'M';
            i++;
        }
        for (n = e-1; n >= 0; n--)
        {
            power = dprint_powi(base, n);
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

static void dprintf_read(const char *fmt, int *index, u8 *digit, s8 *zero)
{
    char buf[10];
    s8 n = 0;
    s16 i;
    if (fmt[*index] == '0') *zero = true;
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
    char c = 0;
    s8 zero = false;
    u8 digit = 0;
    int base = 0;
    int n = 0;
    int i = 0;
    if ((dprint_table[dprint_index] = malloc(sizeof(DPRINT))) == NULL) return;
    dprint_table[dprint_index]->x = x;
    dprint_table[dprint_index]->y = y;
    c = fmt[i];
    while (c != 0)
    {
        if (c == '%')
        {
            i++;
            dprintf_read(fmt, &i, &digit, &zero);
            if (fmt[i] != 'd' && fmt[i] != 'x') break;
            if (fmt[i] == 'd') base = 10;
            if (fmt[i] == 'x') base = 16;
            i++;
            dprintf_write(
                value, base, &dprint_table[dprint_index]->str[n], &n,
                digit, zero
            );
        }
        else
        {
            dprint_table[dprint_index]->str[n] = c;
            n++;
            i++;
        }
        c = fmt[i];
    }
    dprint_table[dprint_index]->len = n;
    dprint_index++;
}

void dprint(int x, int y, const char *str)
{
    char c = 0;
    int n = 0;
    int i = 0;
    if ((dprint_table[dprint_index] = malloc(sizeof(DPRINT))) == NULL) return;
    dprint_table[dprint_index]->x = x;
    dprint_table[dprint_index]->y = y;
    c = str[i];
    while (c != 0)
    {
        dprint_table[dprint_index]->str[n] = c;
        n++;
        i++;
        c = str[i];
    }
    dprint_table[dprint_index]->len = n;
    dprint_index++;
}

void dprintc(int x, int y, const char *str)
{
    char c = 0;
    unused u8 digit = 0;
    unused int base = 0;
    int n = 0;
    int i = 0;
    if ((dprint_table[dprint_index] = malloc(sizeof(DPRINT))) == NULL) return;
    c = str[i];
    while (c != 0)
    {
        dprint_table[dprint_index]->str[n] = c;
        n++;
        i++;
        c = str[i];
    }
    dprint_table[dprint_index]->len = n;
    dprint_table[dprint_index]->x = x - 12*n/2;
    dprint_table[dprint_index]->y = y;
    dprint_index++;
}

extern u16 *txt_dprint[];
extern Gfx gfx_dprint_copy_start[];
extern Gfx gfx_dprint_copy_char[];
extern Gfx gfx_dprint_copy_end[];

static char dprint_cvt(char c)
{
    if (c >= 'A' && c <= 'Z') return 10 + c-'A';
    if (c >= 'a' && c <= 'z') return 10 + c-'a';
    if (c >= '0' && c <= '9') return  0 + c-'0';
    if (c == ' ') return -1;
    if (c == '!') return 36;
    if (c == '#') return 37;
    if (c == '?') return 38;
    if (c == '&') return 39;
    if (c == '%') return 40;
    if (c == '*') return 50;
    if (c == '+') return 51;
    if (c == ',') return 52;
    if (c == '-') return 53;
    if (c == '.') return 54;
    if (c == '/') return 55;
    return -1;
}

static void dprint_draw_txt(char c)
{
    u16 **txt = segment_to_virtual(txt_dprint);
    gDPPipeSync(video_gfx++);
    gDPSetTextureImage(
        video_gfx++, G_IM_FMT_RGBA, G_IM_SIZ_16b, 1, txt[(int)c]
    );
    gSPDisplayList(video_gfx++, gfx_dprint_copy_char);
}

static void dprint_clamp(int *x, int *y)
{
    if (*x <           10) *x =           10;
    if (*x > SCREEN_WD-20) *x = SCREEN_WD-20;
    if (*y <            5) *y =            5;
    if (*y > SCREEN_HT-20) *y = SCREEN_HT-20;
}

static void dprint_draw_char(int x, int y, int n)
{
    int sx = 12*n + x;
    int sy = (SCREEN_HT-2*BORDER_HT) - y;
    uint ux;
    uint uy;
    dprint_clamp(&sx, &sy);
    ux = sx;
    uy = sy;
    gSPTextureRectangle(
        video_gfx++,
        (ux     ) << 2, (uy     ) << 2,
        (ux+16-1) << 2, (uy+16-1) << 2,
        G_TX_RENDERTILE, 0, 0, 4 << 10, 1 << 10
    );
}

void dprint_draw(void)
{
    int i;
    int n;
    char c;
    Mtx *mtx;
    if (dprint_index == 0) return;
    if ((mtx = gfx_alloc(sizeof(Mtx))) == NULL)
    {
        dprint_index = 0; /* memory leak */
        return;
    }
    guOrtho(mtx, 0, SCREEN_WD, 0, SCREEN_HT, -10, 10, 1);
    gSPPerspNormalize(video_gfx++, 0xFFFF);
    gSPMatrix(
        video_gfx++, K0_TO_PHYS(mtx),
        G_MTX_PROJECTION | G_MTX_LOAD | G_MTX_NOPUSH
    );
    gSPDisplayList(video_gfx++, gfx_dprint_copy_start);
    for (i = 0; i < dprint_index; i++)
    {
        for (n = 0; n < dprint_table[i]->len; n++)
        {
            if ((c = dprint_cvt(dprint_table[i]->str[n])) != -1)
            {
                dprint_draw_txt(c);
                dprint_draw_char(dprint_table[i]->x, dprint_table[i]->y, n);
            }
        }
        free(dprint_table[i]);
    }
    gSPDisplayList(video_gfx++, gfx_dprint_copy_end);
    dprint_index = 0;
}
