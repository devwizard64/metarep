#ifdef JAPANESE
#include "caption.ja_jp.h"
#endif
#ifdef ENGLISH
#include "caption.en_us.h"
#endif

static u16 demo_alpha = 0;
static short caption = -1;
static short demo_frame = -1;
static short demo_timer = 0;
static short caption_x;
static short caption_y;

void StaffClear(void)
{
	demo_alpha = 0;
}

void StaffBegin(void)
{
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, demo_alpha);
}

void StaffEnd(void)
{
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
	if (demo_alpha < 250)   demo_alpha += 25;
	else                    demo_alpha = 0xFF;
}

static UCHAR StaffCvt(UCHAR c)
{
	if (c >= 'A' && c <= 'Z') return CH_A + c-'A';
	if (c >= 'a' && c <= 'z') return CH_A + c-'a';
	if (c == ' ') return CH_SPACE;
	if (c == '.') return CH8_PERIOD;
	if (c == '3') return CH_3;
	if (c == '4') return CH_4;
	if (c == '6') return CH_6;
	return CH_SPACE;
}

void StaffPrint(SHORT x, SHORT y, const char *str)
{
	int i = 0;
	unsigned char c;
	unsigned char buf[100];
	c = str[i];
	while (c != '\0')
	{
		buf[i] = StaffCvt(c);
		i++;
		c = str[i];
	}
	buf[i] = CH_NUL;
	Print8(x, y, buf);
}

void CaptionOpen(SHORT x, SHORT y, SHORT code, SHORT frame)
{
	if (caption == -1)
	{
		caption = code;
		demo_frame = frame;
		demo_timer = 0;
		caption_x = x;
		caption_y = y;
		demo_alpha = 0;
	}
}

void CaptionDraw(void)
{
	SHORT x;
	if (caption == -1) return;
	GfxScreenProj();
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, demo_alpha);
	x = StrCenterX(caption_x, captiontab[caption], 10);
	PrintLg(x, SCREEN_HT-caption_y, captiontab[caption]);
	gSPDisplayList(glistp++, gfx_lgfont_end);
	if (demo_timer <             5) demo_alpha += 50;
	if (demo_timer > demo_frame+ 5) demo_alpha -= 50;
	if (demo_timer > demo_frame+10)
	{
		caption = -1;
		demo_alpha = 0;
		demo_timer = 0;
		return;
	}
	demo_timer++;
}

#if REVISION >= 199609
#define OPENING_TIME (30*9)
#else
#define OPENING_TIME (30*6+10)
#endif

#ifdef JAPANESE
#define OPENING_X   53
#define OPENING_Y   136
#endif
#ifdef ENGLISH
#define OPENING_X   38
#define OPENING_Y   142
#endif

extern Gfx gfx_grounds_0700EA58[];
extern Gfx gfx_grounds_0700F2E8[];

static void OpeningDraw(void)
{
	MESSAGE **msgtab = SegmentToVirtual(messagetab);
	MESSAGE *msg = SegmentToVirtual(msgtab[msg_code]);
	unsigned char *str = SegmentToVirtual(msg->str);
	GfxTranslate(GFX_PUSH, 97, 118, 0);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, demo_alpha);
	gSPDisplayList(glistp++, gfx_grounds_0700EA58);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 20, 20, 20, demo_alpha);
	PrintLg(OPENING_X, OPENING_Y, str);
#if REVISION >= 199609
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 0xFF);
	gSPDisplayList(glistp++, gfx_lgfont_end);
	gDPSetEnvColor(glistp++, 200, 80, 120, demo_alpha);
	gSPDisplayList(glistp++, gfx_grounds_0700F2E8);
#else
	gSPDisplayList(glistp++, gfx_lgfont_end);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 0xFF);
#endif
	if (demo_timer == 0) demo_alpha = 0;
	if (demo_timer <              20) demo_alpha += 10;
	if (demo_timer > OPENING_TIME-20) demo_alpha -= 10;
	if (demo_timer > OPENING_TIME)
	{
		caption = -1;
		demo_alpha = 0;
		msg_code = MSG_NULL;
		demo_timer = 0;
		return;
	}
	demo_timer++;
}

void DrawCannonReticle(void)
{
	GfxTranslate(GFX_PUSH, SCREEN_WD/2, SCREEN_HT/2, 0);
	gDPSetEnvColor(glistp++, 50, 50, 50, 180);
	GfxTranslate(GFX_PUSH, -20, -8, 0);
	gSPDisplayList(glistp++, gfx_message_cursor);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	GfxTranslate(GFX_PUSH, 20, 8, 0);
	GfxRotate(GFX_NOPUSH, 180, 0, 0, 1);
	gSPDisplayList(glistp++, gfx_message_cursor);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	GfxTranslate(GFX_PUSH, 8, -20, 0);
	GfxRotate(GFX_NOPUSH, 90, 0, 0, 1);
	gSPDisplayList(glistp++, gfx_message_cursor);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	GfxTranslate(GFX_PUSH, -8, 20, 0);
	GfxRotate(GFX_NOPUSH, -90, 0, 0, 1);
	gSPDisplayList(glistp++, gfx_message_cursor);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
}
