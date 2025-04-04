#include <sm64.h>

typedef struct time
{
	short audcpu_i;
	short audrcp_i;
	OSTime gfxcpu[TIME_GFXCPU_MAX];
	OSTime gfxrcp[TIME_GFXRCP_MAX];
	OSTime audcpu[TIME_AUDCPU_MAX];
	OSTime audrcp[TIME_AUDRCP_MAX];
}
TIME;

static TIME time_data[2];
static short time_mode = 0;
static short time_cpu = 1;
static short time_rcp = 0;

void TimeGfxCPU(int index)
{
	time_data[time_cpu].gfxcpu[index] = osGetTime();
	if (index == TIME_GFXCPU_END)
	{
		time_cpu ^= 1;
		time_data[time_cpu].audcpu_i = 0;
	}
}

void TimeAudCPU(void)
{
	TIME *time = &time_data[time_cpu];
	if (time->audcpu_i < TIME_AUDCPU_MAX)
	{
		time->audcpu[time->audcpu_i++] = osGetTime();
	}
}

void TimeGfxRCP(int index)
{
	if (index == TIME_GFXRCP_START)
	{
		time_rcp ^= 1;
		time_data[time_rcp].audrcp_i = 0;
	}
	time_data[time_rcp].gfxrcp[index] = osGetTime();
}

void TimeAudRCP(void)
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

#define TimeDrawRect(xl, xh, y, fill) \
{ \
	gDPPipeSync(glistp++); \
	gDPSetFillColor(glistp++, (fill) << 16 | (fill)); \
	gDPFillRectangle(glistp++, (xl), (y), (xh), (y)+TIME_H-1); \
}

static void TimeDrawD(
	OSTime start, OSTime tl, OSTime th, SHORT y, USHORT fill
)
{
	s64 dl, dh;
	int xl, xh;
	if ((dl = tl-start) < 0) dl = 0;
	if ((dh = th-start) < 0) dh = 0;
	xl = TIME_X + OS_CYCLES_TO_USEC(dl) * 3/1000;
	xh = TIME_X + OS_CYCLES_TO_USEC(dh) * 3/1000;
	/* meant xl, xh */
	if (xl > SCREEN_WD-1) tl = SCREEN_WD-1;
	if (xh > SCREEN_WD-1) th = SCREEN_WD-1;
	if (xl < xh) TimeDrawRect(xl, xh, y, fill);
}

static void TimeDrawScale(void)
{
	TimeDrawRect(TIME_X+49*0, TIME_X+49*1, TIME_Y(0), F_BLUE);
	TimeDrawRect(TIME_X+49*1, TIME_X+49*2, TIME_Y(0), F_YELLOW);
	TimeDrawRect(TIME_X+49*2, TIME_X+49*3, TIME_Y(0), F_ORANGE);
	TimeDrawRect(TIME_X+49*3, TIME_X+49*4, TIME_Y(0), F_RED);
}

/*
red   : aud CPU
yellow: gfx proc
orange: gfx draw
cyan  : gfx RCP

red   : aud RSP
yellow: gfx RSP
orange: gfx RDP
*/

#define GFXCPU_START    time->gfxcpu[TIME_GFXCPU_START]
#define GFXCPU_ENDPRC   time->gfxcpu[TIME_GFXCPU_ENDPRC]
#define GFXCPU_ENDFRM   time->gfxcpu[TIME_GFXCPU_ENDFRM]
#define GFXCPU_ENDRDP   time->gfxcpu[TIME_GFXCPU_ENDRDP]
#define GFXRCP_START    time->gfxrcp[TIME_GFXRCP_START]
#define GFXRCP_ENDRSP   time->gfxrcp[TIME_GFXRCP_ENDRSP]
#define GFXRCP_ENDRDP   time->gfxrcp[TIME_GFXRCP_ENDRDP]
#define AUDCPU_START    time->audcpu[0]

static void TimeDrawAbs(void)
{
	int i;
	TIME *time = &time_data[time_cpu^1];
	OSTime start = AUDCPU_START - OS_USEC_TO_CYCLES(16433);
	TimeDrawD(start, GFXCPU_START,  GFXCPU_ENDPRC, TIME_Y(2), F_YELLOW);
	TimeDrawD(start, GFXCPU_ENDPRC, GFXCPU_ENDFRM, TIME_Y(2), F_ORANGE);
	TimeDrawD(start, GFXCPU_ENDFRM, GFXCPU_ENDRDP, TIME_Y(2), F_CYAN);
	time->audcpu_i &= (USHORT)~1;
	for (i = 0; i < time->audcpu_i; i += 2) TimeDrawD(
		start, time->audcpu[i+0], time->audcpu[i+1], TIME_Y(2), F_RED
	);
	TimeDrawD(start, GFXRCP_START,  GFXRCP_ENDRSP, TIME_Y(1), F_YELLOW);
	TimeDrawD(start, GFXRCP_ENDRSP, GFXRCP_ENDRDP, TIME_Y(1), F_ORANGE);
	time->audrcp_i &= (USHORT)~1;
	for (i = 0; i < time->audrcp_i; i += 2) TimeDrawD(
		start, time->audrcp[i+0], time->audrcp[i+1], TIME_Y(1), F_RED
	);
	TimeDrawScale();
}

static void TimeDrawRel(void)
{
	int i;
	TIME *time = &time_data[time_cpu^1];
	OSTime start = GFXCPU_START <= AUDCPU_START ? GFXCPU_START : AUDCPU_START;
	OSTime gfxprc = GFXCPU_ENDPRC - start;
	OSTime gfxfrm = GFXCPU_ENDFRM - GFXCPU_ENDPRC;
	OSTime audcpu = 0;
	OSTime gfxrsp = GFXRCP_ENDRSP - GFXRCP_START;
	OSTime gfxrdp = GFXRCP_ENDRDP - GFXRCP_START;
	OSTime audrsp = 0;
	time->audcpu_i &= (USHORT)~1;
	for (i = 0; i < time->audcpu_i; i += 2)
	{
		OSTime d = time->audcpu[i+1]-time->audcpu[i+0];
		audcpu += d;
		if      (time->audcpu[i] < GFXCPU_ENDPRC) gfxprc -= d;
		else if (time->audcpu[i] < GFXCPU_ENDFRM) gfxfrm -= d;
	}
	/* meant audrcp_i */
	time->audcpu_i &= (USHORT)~1;
	for (i = 0; i < time->audcpu_i; i += 2)
	{
		audrsp += time->audrcp[i+1]-time->audrcp[i+0];
	}
	start = 0;
	TimeDrawD(0, start, start+audcpu, TIME_Y(2), F_RED   ); start += audcpu;
	TimeDrawD(0, start, start+gfxprc, TIME_Y(2), F_YELLOW); start += gfxprc;
	TimeDrawD(0, start, start+gfxfrm, TIME_Y(2), F_ORANGE);
	TimeDrawD(0, 0, gfxrdp, TIME_Y(1), F_ORANGE);
	TimeDrawD(0, 0, gfxrsp, TIME_Y(1), F_YELLOW);
	TimeDrawD(0, 0, audrsp, TIME_Y(1), F_RED   );
	TimeDrawScale();
}

void TimeDraw(void)
{
	if (cont1->down & L_TRIG) time_mode ^= 1;
	if (time_mode == 0) TimeDrawRel();
	else                TimeDrawAbs();
}
