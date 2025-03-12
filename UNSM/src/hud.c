#include <sm64.h>

extern u16 *txt_glbfont[];
extern u16 *txt_camera[];
extern Gfx gfx_print_copy_begin[];
extern Gfx gfx_print_copy_char[];
extern Gfx gfx_print_copy_end[];
extern u16 *txt_meter_n[];
extern Gfx gfx_meter_0[];
extern Gfx gfx_meter_n[];
extern Gfx gfx_meter_end[];

#ifdef sgi
#define FRAME(x) (30*(x))
#else
#define FRAME(x) ((int)(30*(x)))
#endif

#define EDGE_X          22
#define EDGE_Y          15

#define HUD_XL          EDGE_X
#define HUD_YL          EDGE_Y
#define HUD_XM          (SCREEN_WD/2)
#define HUD_YM          (SCREEN_HT/2)
#define HUD_XH          (SCREEN_WD-EDGE_X)
#define HUD_YH          (SCREEN_HT-EDGE_Y)

#if REVISION >= 199609
#define HUD_TOP         (HUD_YH-16)
#else
#define HUD_TOP         (HUD_YH-15)
#endif

#define LIFE_X          HUD_XL
#define LIFE_Y          HUD_TOP

#define COIN_X          (HUD_XM+8)
#define COIN_Y          HUD_TOP

#if REVISION >= 199609
#define STAR_X          (HUD_XH-16-16-24)
#else
#define STAR_X          (HUD_XH-16-16-19)
#endif
#define STAR_Y          HUD_TOP

#define KEY_X           (HUD_XH-78)
#define KEY_Y           (HUD_YM+22)

#define TIME_X          (HUD_XH-128)
#define TIME_Y          (HUD_YH-40)
#define TIME_QY         (HUD_YL+17)
#define TIME_MIN_X      (TIME_X+59)
#define TIME_QMS_X      (TIME_MIN_X+10)
#define TIME_SEC_X      (TIME_QMS_X+10)
#define TIME_QSF_X      (TIME_SEC_X+25)
#define TIME_FRC_X      (TIME_QSF_X+9)

#define CAMERA_X        (HUD_XH-32)
#define CAMERA_Y        (HUD_YH-20)

#define METER_X         (HUD_XM-20)
#define METER_Y         (HUD_YH-59)
#define METER_TOP       (HUD_YH-25)
#define METER_OUT       (SCREEN_HT+60)

#define METER_OFF       0
#define METER_ALERT     1
#define METER_SHOW      2
#define METER_HIDE      3
#define METER_ON        4

typedef struct meter
{
	char state;
	short x;
	short y;
	float scale;
}
METER;

static METER meter = {0, METER_X, METER_Y, 1};

static short meter_power;
static int meter_timer = 0;
UNUSED static short hud_80332600 = 0;
UNUSED static short hud_80332604 = 10;

static void HUD_DrawChar(unsigned int x, unsigned int y, u16 *txt)
{
	gDPPipeSync(glistp++);
	gDPSetTextureImage(glistp++, G_IM_FMT_RGBA, G_IM_SIZ_16b, 1, txt);
	gSPDisplayList(glistp++, gfx_print_copy_char);
	gSPTextureRectangle(
		glistp++, x << 2, y << 2, (x+16-1) << 2, (y+16-1) << 2,
		G_TX_RENDERTILE, 0, 0, 4 << 10, 1 << 10
	);
}

static void HUD_Draw8x8(unsigned int x, unsigned int y, u16 *txt)
{
	gDPSetLoadTile(glistp++, G_IM_FMT_RGBA, G_IM_SIZ_16b);
	gDPSetImageBlock(
		glistp++, G_IM_FMT_RGBA, G_IM_SIZ_16b, 8, 8, 0,
		G_TX_CLAMP, G_TX_CLAMP, 3, 3, 0, 0
	);
	gDPPipeSync(glistp++);
	gDPLoadImageBlock(glistp++, txt, G_IM_FMT_RGBA, G_IM_SIZ_16b, 8, 8);
	gSPTextureRectangle(
		glistp++, x << 2, y << 2, (x+8-1) << 2, (y+8-1) << 2,
		G_TX_RENDERTILE, 0, 0, 4 << 10, 1 << 10
	);
}

static void MeterDrawN(SHORT power)
{
	u16 **txt = SegmentToVirtual(txt_meter_n);
	gDPPipeSync(glistp++);
	gDPLoadImageBlock(
		glistp++, txt[power-1], G_IM_FMT_RGBA, G_IM_SIZ_16b, 32, 32
	);
	gSP2Triangles(glistp++, 0, 1, 2, 0, 0, 2, 3, 0);
}

static void MeterDraw(SHORT power)
{
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	if (!mtx) return;
	guTranslate(mtx, meter.x, meter.y, 0);
	gSPMatrix(
		glistp++, K0_TO_PHYS(mtx++), G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_PUSH
	);
	gSPDisplayList(glistp++, gfx_meter_0);
	if (power)
	{
		gSPDisplayList(glistp++, gfx_meter_n);
		MeterDrawN(power);
		gSPDisplayList(glistp++, gfx_meter_end);
	}
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
}

static void MeterAlert(void)
{
	SHORT flag = hud.flag;
	if (!(flag & HUD_ALERT))
	{
		if (meter_timer == FRAME(1.5)) meter.state = METER_SHOW;
	}
	else
	{
		meter_timer = 0;
	}
}

static void MeterShow(void)
{
	SHORT vy = 5;
	if (meter.y > METER_TOP-20) vy = 3;
	if (meter.y > METER_TOP-10) vy = 2;
	if (meter.y > METER_TOP- 5) vy = 1;
	meter.y += vy;
	if (meter.y > METER_TOP)
	{
		meter.y = METER_TOP;
		meter.state = METER_ON;
	}
}

static void MeterHide(void)
{
	meter.y += 20;
	if (meter.y > METER_OUT)
	{
		meter.state = METER_OFF;
		meter_timer = 0;
	}
}

static void MeterProc(SHORT power)
{
	if (power < 8 && meter_power == 8 && meter.state == METER_OFF)
	{
		meter.state = METER_ALERT;
		meter.y = METER_Y;
	}
	if (power == 8 && meter_power == 7) meter_timer = 0;
	if (power == 8 && meter_timer > FRAME(1.5)) meter.state = METER_HIDE;
	meter_power = power;
	if (pl_camera_data[0].state & PF_SWIM)
	{
		if (meter.state == METER_OFF || meter.state == METER_ALERT)
		{
			meter.state = METER_SHOW;
			meter.y = METER_Y;
		}
		meter_timer = 0;
	}
}

static void HUD_DrawPower(void)
{
	SHORT power = hud.power;
	if (meter.state != METER_HIDE) MeterProc(power);
	if (meter.state == METER_OFF) return;
	switch (meter.state)
	{
	case 1: MeterAlert(); break;
	case 2: MeterShow(); break;
	case 3: MeterHide(); break;
	default: break;
	}
	MeterDraw(power);
	meter_timer++;
}

static void HUD_DrawLife(void)
{
	dprint(LIFE_X, LIFE_Y, ",");
	dprint(LIFE_X+16, LIFE_Y, "*");
	dprintf(LIFE_X+16+16, LIFE_Y, "%d", hud.life);
}

static void HUD_DrawCoin(void)
{
	dprint(COIN_X, COIN_Y, "+");
	dprint(COIN_X+16, COIN_Y, "*");
	dprintf(COIN_X+16+14, COIN_Y, "%d", hud.coin);
}

static void HUD_DrawStar(void)
{
	CHAR flag = FALSE;
	if (savemenu_code == 1 && gfx_frame & 8) return;
	if (hud.star < 100) flag = TRUE;
	dprint(STAR_X, STAR_Y, "-");
	if (ISTRUE(flag)) dprint(STAR_X+16, STAR_Y, "*");
	dprintf(STAR_X+16+14*flag, STAR_Y, "%d", hud.star);
}

static void HUD_DrawKey(void)
{
	SHORT i;
	for (i = 0; i < hud.key; i++) dprint(KEY_X+16*i, KEY_Y, "/");
}

static void HUD_DrawTime(void)
{
	u16 **txt = SegmentToVirtual(txt_glbfont);
	USHORT time = hud.time;
	USHORT min = time / (30*60);
	USHORT sec = (time - 30*60*min) / 30;
	USHORT frc = (USHORT)(time - 30*60*min - 30*sec) / 3;
#ifdef MULTILANG
	switch (BuGetLang())
	{
	case 0: dprint(TIME_X-0, TIME_Y, "TIME");   break;
	case 1: dprint(TIME_X-5, TIME_Y, "TEMPS");  break;
	case 2: dprint(TIME_X-0, TIME_Y, "ZEIT");   break;
	}
#else
	dprint(TIME_X, TIME_Y, "TIME");
#endif
	dprintf(TIME_MIN_X, TIME_Y, "%0d", min);
	dprintf(TIME_SEC_X, TIME_Y, "%02d", sec);
	dprintf(TIME_FRC_X, TIME_Y, "%d", frc);
	gSPDisplayList(glistp++, gfx_print_copy_begin);
	HUD_DrawChar(TIME_QMS_X, TIME_QY, txt[56]);
	HUD_DrawChar(TIME_QSF_X, TIME_QY, txt[57]);
	gSPDisplayList(glistp++, gfx_print_copy_end);
}

static short hud_camera = 0;

void HUD_SetCamera(SHORT flag)
{
	hud_camera = flag;
}

static void HUD_DrawCamera(void)
{
	u16 **txt = SegmentToVirtual(txt_camera);
	int x = CAMERA_X;
	int y = CAMERA_Y;
	if (!hud_camera) return;
	gSPDisplayList(glistp++, gfx_print_copy_begin);
	HUD_DrawChar(x, y, txt[0]);
	switch (hud_camera & 7) /* T:hud_camera */
	{
	case 1: HUD_DrawChar(x+16, y, txt[1]); break;
	case 2: HUD_DrawChar(x+16, y, txt[2]); break;
	case 4: HUD_DrawChar(x+16, y, txt[3]); break;
	}
	switch (hud_camera & 24) /* T:hud_camera */
	{
	case  8: HUD_Draw8x8(x+4, y+16, txt[5]); break;
	case 16: HUD_Draw8x8(x+4, y- 8, txt[4]); break;
	}
	gSPDisplayList(glistp++, gfx_print_copy_end);
}

void HUD_Draw(void)
{
	SHORT flag = hud.flag;
	if (!flag)
	{
		meter.state = METER_OFF;
		meter_power = 8;
		meter_timer = 0;
	}
	else
	{
#ifdef PAL
		Mtx *mtx = GfxAlloc(sizeof(Mtx));
		if (!mtx) return;
		GfxLoadIdent();
		guOrtho(mtx, -16, SCREEN_WD+16, 0, SCREEN_HT, -10, 10, 1);
		gSPPerspNormalize(glistp++, 0xFFFF);
		gSPMatrix(
			glistp++, K0_TO_PHYS(mtx), G_MTX_PROJECTION|G_MTX_MUL|G_MTX_NOPUSH
		);
#else
		GfxScreenProj();
#endif
		/* T:enum */
		if (scenep && scenep->cam->mode == 10) DrawCannonReticle();
		if (flag & HUD_LIFE) HUD_DrawLife();
		if (flag & HUD_COIN) HUD_DrawCoin();
		if (flag & HUD_STAR) HUD_DrawStar();
		if (flag & HUD_KEY) HUD_DrawKey();
		if (flag & HUD_METER)
		{
			HUD_DrawPower();
			HUD_DrawCamera();
		}
		if (flag & HUD_TIME) HUD_DrawTime();
	}
}
