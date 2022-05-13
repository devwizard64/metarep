#include <sm64/types.h>
#include <sm64/main.h>
#include <sm64/app.h>
#include <sm64/time.h>

TIME time_data[2];
s16 time_mode = 0;
s16 time_cpu = 1;
s16 time_rcp = 0;

void time_gfxcpu(int index)
{
    time_data[time_cpu].gfxcpu[index] = osGetTime();
    if (index == TIME_GFXCPU_END)
    {
        time_cpu ^= 1;
        time_data[time_cpu].audcpu_i = 0;
    }
}

void time_audcpu(void)
{
    TIME *time = &time_data[time_cpu];
    if (time->audcpu_i < TIME_AUDCPU_MAX)
    {
        time->audcpu[time->audcpu_i++] = osGetTime();
    }
}

void time_gfxrcp(int index)
{
    if (index == TIME_GFXRCP_START)
    {
        time_rcp ^= 1;
        time_data[time_rcp].audrcp_i = 0;
    }
    time_data[time_rcp].gfxrcp[index] = osGetTime();
}

void time_audrcp(void)
{
    TIME *time = &time_data[time_rcp];
    if (time->audrcp_i < TIME_AUDRCP_MAX)
    {
        time->audrcp[time->audrcp_i++] = osGetTime();
    }
}

#define TIME_X      30
#define TIME_H      3
#define TIME_Y(y)   (SCREEN_HT-20 - (TIME_H+1)*(y))

#define F_BLUE      GPACK_RGBA5551(0x28, 0x50, 0xFF, 1)
#define F_YELLOW    GPACK_RGBA5551(0xFF, 0xFF, 0x28, 1)
#define F_ORANGE    GPACK_RGBA5551(0xFF, 0x78, 0x28, 1)
#define F_RED       GPACK_RGBA5551(0xFF, 0x28, 0x28, 1)
#define F_CYAN      GPACK_RGBA5551(0x28, 0xC0, 0xE0, 1)

#define time_draw_rect(xl, xh, y, fill)                             \
{                                                                   \
    gDPPipeSync(video_gfx++);                                       \
    gDPSetFillColor(video_gfx++, (fill) << 16 | (fill));            \
    gDPFillRectangle(video_gfx++, (xl), (y), (xh), (y)+TIME_H-1);   \
}

static void time_draw_d(
    OSTime start, OSTime tl, OSTime th, SHORT y, USHORT fill
)
{
    s64 dl;
    s64 dh;
    int xl;
    int xh;
    if ((dl = tl-start) < 0) dl = 0;
    if ((dh = th-start) < 0) dh = 0;
    xl = TIME_X + dl * 1000000/osClockRate * 3/1000;
    xh = TIME_X + dh * 1000000/osClockRate * 3/1000;
    /* meant xl, xh */
    if (xl > SCREEN_WD-1) tl = SCREEN_WD-1;
    if (xh > SCREEN_WD-1) th = SCREEN_WD-1;
    if (xl < xh) time_draw_rect(xl, xh, y, fill);
}

static void time_draw_scale(void)
{
    time_draw_rect(TIME_X+49*0, TIME_X+49*1, TIME_Y(0), F_BLUE);
    time_draw_rect(TIME_X+49*1, TIME_X+49*2, TIME_Y(0), F_YELLOW);
    time_draw_rect(TIME_X+49*2, TIME_X+49*3, TIME_Y(0), F_ORANGE);
    time_draw_rect(TIME_X+49*3, TIME_X+49*4, TIME_Y(0), F_RED);
}

/*
red   : aud CPU
yellow: app update
orange: app gfx
cyan  : gfx RCP

red   : aud RSP
yellow: gfx RSP
orange: gfx RDP
*/

#define GFXCPU_START    time->gfxcpu[TIME_GFXCPU_START]
#define GFXCPU_ENDUPD   time->gfxcpu[TIME_GFXCPU_ENDUPD]
#define GFXCPU_ENDGFX   time->gfxcpu[TIME_GFXCPU_ENDGFX]
#define GFXCPU_ENDRDP   time->gfxcpu[TIME_GFXCPU_ENDRDP]
#define GFXRCP_START    time->gfxrcp[TIME_GFXRCP_START]
#define GFXRCP_ENDRSP   time->gfxrcp[TIME_GFXRCP_ENDRSP]
#define GFXRCP_ENDRDP   time->gfxrcp[TIME_GFXRCP_ENDRDP]
#define AUDCPU_START    time->audcpu[0]

static void time_draw_abs(void)
{
    int i;
    TIME *time = &time_data[time_cpu^1];
    OSTime start = AUDCPU_START - 16433*osClockRate/1000000;
    time_draw_d(start, GFXCPU_START,  GFXCPU_ENDUPD, TIME_Y(2), F_YELLOW);
    time_draw_d(start, GFXCPU_ENDUPD, GFXCPU_ENDGFX, TIME_Y(2), F_ORANGE);
    time_draw_d(start, GFXCPU_ENDGFX, GFXCPU_ENDRDP, TIME_Y(2), F_CYAN);
    time->audcpu_i &= (USHORT)~1;
    for (i = 0; i < time->audcpu_i; i += 2) time_draw_d(
        start, time->audcpu[i+0], time->audcpu[i+1], TIME_Y(2), F_RED
    );
    time_draw_d(start, GFXRCP_START,  GFXRCP_ENDRSP, TIME_Y(1), F_YELLOW);
    time_draw_d(start, GFXRCP_ENDRSP, GFXRCP_ENDRDP, TIME_Y(1), F_ORANGE);
    time->audrcp_i &= (USHORT)~1;
    for (i = 0; i < time->audrcp_i; i += 2) time_draw_d(
        start, time->audrcp[i+0], time->audrcp[i+1], TIME_Y(1), F_RED
    );
    time_draw_scale();
}

static void time_draw_rel(void)
{
    int i;
    TIME *time = &time_data[time_cpu^1];
    OSTime start = GFXCPU_START <= AUDCPU_START ? GFXCPU_START : AUDCPU_START;
    OSTime appupd = GFXCPU_ENDUPD - start;
    OSTime appgfx = GFXCPU_ENDGFX - GFXCPU_ENDUPD;
    OSTime audcpu = 0;
    OSTime gfxrsp = GFXRCP_ENDRSP - GFXRCP_START;
    OSTime gfxrdp = GFXRCP_ENDRDP - GFXRCP_START;
    OSTime audrsp = 0;
    time->audcpu_i &= (USHORT)~1;
    for (i = 0; i < time->audcpu_i; i += 2)
    {
        OSTime d = time->audcpu[i+1]-time->audcpu[i+0];
        audcpu += d;
        if      (time->audcpu[i] < GFXCPU_ENDUPD) appupd -= d;
        else if (time->audcpu[i] < GFXCPU_ENDGFX) appgfx -= d;
    }
    /* meant audrcp_i */
    time->audcpu_i &= (USHORT)~1;
    for (i = 0; i < time->audcpu_i; i += 2)
    {
        audrsp += time->audrcp[i+1]-time->audrcp[i+0];
    }
    start = 0;
    time_draw_d(0, start, start+audcpu, TIME_Y(2), F_RED   ); start += audcpu;
    time_draw_d(0, start, start+appupd, TIME_Y(2), F_YELLOW); start += appupd;
    time_draw_d(0, start, start+appgfx, TIME_Y(2), F_ORANGE);
    time_draw_d(0, 0, gfxrdp, TIME_Y(1), F_ORANGE);
    time_draw_d(0, 0, gfxrsp, TIME_Y(1), F_YELLOW);
    time_draw_d(0, 0, audrsp, TIME_Y(1), F_RED   );
    time_draw_scale();
}

void time_draw(void)
{
    if (cont_1->down & L_TRIG) time_mode ^= 1;
    if (time_mode == 0) time_draw_rel();
    else                time_draw_abs();
}