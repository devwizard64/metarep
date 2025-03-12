#include <sm64.h>

extern Gfx gfx_quad0[];
extern Gfx gfx_wipe_begin[];
extern Gfx gfx_wipe_end[];
extern Gfx gfx_wipe_draw[];

static u8 wipe_timer[2] = {0};
static u16 wipe_ang[2] = {0};

extern u8 txt_wipe_star[];
extern u8 txt_wipe_circle[];
extern u8 txt_wipe_mario[];
extern u8 txt_wipe_bowser[];

static u8 *txt_wipe[] =
{
	txt_wipe_star,
	txt_wipe_circle,
	txt_wipe_mario,
	txt_wipe_bowser,
};

static int WpStep(CHAR screen, UCHAR frame)
{
	int result = FALSE;
	wipe_timer[screen]++;
	if (wipe_timer[screen] == frame)
	{
		wipe_timer[screen] = 0;
		wipe_ang[screen] = 0;
		result = TRUE;
	}
	return result;
}

static UCHAR WpFadeAlpha(CHAR code, CHAR screen, UCHAR frame)
{
	UCHAR alpha;
	switch (code)
	{
	case 0:
		alpha = 255.0*       (float)wipe_timer[screen]/(float)(frame-1)  + 0.5;
		break;
	case 1:
		alpha = 255.0*(1.0 - (float)wipe_timer[screen]/(float)(frame-1)) + 0.5;
		break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
	return alpha;
}

static Vtx *WpFadeVtx(WIPE_FADE *fade, UCHAR alpha)
{
	Vtx *vtx = GfxAlloc(sizeof(Vtx)*4);
	u8 r = fade->r;
	u8 g = fade->g;
	u8 b = fade->b;
	if (vtx)
	{
		VtxSet(vtx, 0,         0,         0, -1, 0, 0, r, g, b, alpha);
		VtxSet(vtx, 1, SCREEN_WD,         0, -1, 0, 0, r, g, b, alpha);
		VtxSet(vtx, 2, SCREEN_WD, SCREEN_HT, -1, 0, 0, r, g, b, alpha);
		VtxSet(vtx, 3,         0, SCREEN_HT, -1, 0, 0, r, g, b, alpha);
	}
	else
	{
	}
	return vtx;
}

static int WpFadeGfx(CHAR screen, UCHAR frame, WIPE_FADE *fade, UCHAR alpha)
{
	Vtx *vtx;
	if ((vtx = WpFadeVtx(fade, alpha)))
	{
		gSPDisplayList(glistp++, gfx_wipe_begin);
		gDPSetCombineMode(glistp++, G_CC_SHADE, G_CC_SHADE);
		gDPSetRenderMode(glistp++, G_RM_AA_XLU_SURF, G_RM_AA_XLU_SURF2);
		gSPVertex(glistp++, K0_TO_PHYS(vtx), 4, 0);
		gSPDisplayList(glistp++, gfx_quad0);
		gSPDisplayList(glistp++, gfx_wipe_end);
	}
	return WpStep(screen, frame);
}

static int WpFadeIn(CHAR screen, UCHAR frame, WIPE_FADE *fade)
{
	UCHAR alpha = WpFadeAlpha(1, screen, frame);
	return WpFadeGfx(screen, frame, fade, alpha);
}

static int WpFadeOut(CHAR screen, UCHAR frame, WIPE_FADE *fade)
{
	UCHAR alpha = WpFadeAlpha(0, screen, frame);
	return WpFadeGfx(screen, frame, fade, alpha);
}

static SHORT WpWindowSize(CHAR screen, CHAR frame, WIPE_WINDOW *win)
{
	float dsize = win->esize - win->ssize;
	float ssize = dsize * wipe_timer[screen]/(frame-1);
	float size = win->ssize + ssize;
	return size + 0.5;
}

static float WpWindowDist(CHAR screen, CHAR frame, WIPE_WINDOW *win)
{
	float sx = win->sx;
	float sy = win->sy;
	float ex = win->ex;
	float ey = win->ey;
	float d = DIST2(sx-ex, sy-ey);
	float dist = d * wipe_timer[screen]/(frame-1);
	return dist;
}

static USHORT WpWindowAng(WIPE_WINDOW *win)
{
	float dx = win->ex - win->sx;
	float dy = win->ey - win->sy;
	return ATAN2(dx, dy);
}

static SHORT WpWindowX(WIPE_WINDOW *win, float dist, USHORT ang)
{
	float x = win->sx + dist*COS(ang);
	return x + 0.5;
}

static SHORT WpWindowY(WIPE_WINDOW *win, float dist, USHORT ang)
{
	float y = win->sy + dist*SIN(ang);
	return y + 0.5;
}

static void WpWindowVtxSet(
	Vtx *vtx, int i, CHAR screen, WIPE_WINDOW *win,
	SHORT x, SHORT y, SHORT dx, SHORT dy, SHORT s, SHORT t
)
{
	u8 r = win->r;
	u8 g = win->g;
	u8 b = win->b;
	u16 ang = wipe_ang[screen];
	float xf = x + (dx*COS(ang) - dy*SIN(ang));
	float yf = y + (dx*SIN(ang) + dy*COS(ang));
	SHORT xs = RoundFtoS(xf);
	SHORT ys = RoundFtoS(yf);
	VtxSet(vtx, i, xs, ys, -1, 32*s, 32*t, r, g, b, 0xFF);
}

static void WpWindowVtx(
	Vtx *vtx, CHAR screen, WIPE_WINDOW *win,
	SHORT x, SHORT y, SHORT size, CHAR code
)
{
	switch (code)
	{
	case 0:
		WpWindowVtxSet(vtx, 0, screen, win, x, y, -size, -size, -31, 63);
		WpWindowVtxSet(vtx, 1, screen, win, x, y,  size, -size,  31, 63);
		WpWindowVtxSet(vtx, 2, screen, win, x, y,  size,  size,  31,  0);
		WpWindowVtxSet(vtx, 3, screen, win, x, y, -size,  size, -31,  0);
		break;
	case 1:
		WpWindowVtxSet(vtx, 0, screen, win, x, y, -size, -size,  0, 63);
		WpWindowVtxSet(vtx, 1, screen, win, x, y,  size, -size, 63, 63);
		WpWindowVtxSet(vtx, 2, screen, win, x, y,  size,  size, 63,  0);
		WpWindowVtxSet(vtx, 3, screen, win, x, y, -size,  size,  0,  0);
		break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
	WpWindowVtxSet(vtx, 4, screen, win, x, y, -2000, -2000, 0, 0);
	WpWindowVtxSet(vtx, 5, screen, win, x, y, +2000, -2000, 0, 0);
	WpWindowVtxSet(vtx, 6, screen, win, x, y, +2000, +2000, 0, 0);
	WpWindowVtxSet(vtx, 7, screen, win, x, y, -2000, +2000, 0, 0);
}

static int WpWindow(
	CHAR screen, CHAR frame, WIPE_WINDOW *win, CHAR txt, CHAR code
)
{
	float dist = WpWindowDist(screen, frame, win);
	USHORT ang = WpWindowAng(win);
	SHORT x = WpWindowX(win, dist, ang);
	SHORT y = WpWindowY(win, dist, ang);
	SHORT size = WpWindowSize(screen, frame, win);
	Vtx *vtx = GfxAlloc(sizeof(Vtx)*8);
	if (vtx)
	{
		WpWindowVtx(vtx, screen, win, x, y, size, code);
		gSPDisplayList(glistp++, gfx_wipe_begin);
		gDPSetCombineMode(glistp++, G_CC_SHADE, G_CC_SHADE);
		gDPSetRenderMode(glistp++, G_RM_AA_OPA_SURF, G_RM_AA_OPA_SURF2);
		gSPVertex(glistp++, K0_TO_PHYS(vtx), 8, 0);
		gSPDisplayList(glistp++, gfx_wipe_draw);
		gDPPipeSync(glistp++);
		gDPSetCombineMode(
			glistp++, G_CC_MODULATERGBDECALA, G_CC_MODULATERGBDECALA
		);
		gDPSetRenderMode(glistp++, G_RM_AA_XLU_SURF, G_RM_AA_XLU_SURF2);
		gDPSetTextureFilter(glistp++, G_TF_BILERP);
		switch (code)
		{
		case 0: gDPLoadTextureBlock(
			glistp++, txt_wipe[txt], G_IM_FMT_IA, G_IM_SIZ_8b, 32, 64, 0,
			G_TX_MIRROR, G_TX_MIRROR, 5, 6, 0, 0
		); break;
		case 1: gDPLoadTextureBlock(
			glistp++, txt_wipe[txt], G_IM_FMT_IA, G_IM_SIZ_8b, 64, 64, 0,
			G_TX_CLAMP, G_TX_CLAMP, 6, 6, 0, 0
		); break;
#ifdef __GNUC__
		default: __builtin_unreachable();
#endif
		}
		gSPTexture(glistp++, 0xFFFF, 0xFFFF, G_TX_NOLOD, G_TX_RENDERTILE, G_ON);
		gSPVertex(glistp++, K0_TO_PHYS(vtx), 4, 0);
		gSPDisplayList(glistp++, gfx_quad0);
		gSPTexture(
			glistp++, 0xFFFF, 0xFFFF, G_TX_NOLOD, G_TX_RENDERTILE, G_OFF
		);
		gSPDisplayList(glistp++, gfx_wipe_end);
		wipe_ang[screen] += win->rot;
	}
	else
	{
	}
	return WpStep(screen, frame);
}

int WipeDraw(CHAR screen, CHAR type, UCHAR frame, WIPE_DATA *data)
{
	switch (type)
	{
	case WIPE_FADE_IN:
		return WpFadeIn(screen, frame, &data->fade);
		break;
	case WIPE_FADE_OUT:
		return WpFadeOut(screen, frame, &data->fade);
		break;
	case WIPE_STAR_IN:
		return WpWindow(screen, frame, &data->window, 0, 0);
		break;
	case WIPE_STAR_OUT:
		return WpWindow(screen, frame, &data->window, 0, 0);
		break;
	case WIPE_CIRCLE_IN:
		return WpWindow(screen, frame, &data->window, 1, 0);
		break;
	case WIPE_CIRCLE_OUT:
		return WpWindow(screen, frame, &data->window, 1, 0);
		break;
	case WIPE_MARIO_IN:
		return WpWindow(screen, frame, &data->window, 2, 1);
		break;
	case WIPE_MARIO_OUT:
		return WpWindow(screen, frame, &data->window, 2, 1);
		break;
	case WIPE_BOWSER_IN:
		return WpWindow(screen, frame, &data->window, 3, 0);
		break;
	case WIPE_BOWSER_OUT:
		return WpWindow(screen, frame, &data->window, 3, 0);
		break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
}

static Gfx *CannonOverlayGfx(void)
{
	Vtx *vtx = GfxAlloc(sizeof(Vtx)*4);
	Gfx *gfx, *g = gfx = GfxAlloc(sizeof(Gfx)*(3+7+6));
	if (vtx && gfx)
	{
		VtxSet(vtx, 0,         0,         0, -1, 32*-36, 32*57, 0, 0, 0, 0xFF);
		VtxSet(vtx, 1, SCREEN_WD,         0, -1, 32*+36, 32*57, 0, 0, 0, 0xFF);
		VtxSet(vtx, 2, SCREEN_WD, SCREEN_HT, -1, 32*+36, 32* 6, 0, 0, 0, 0xFF);
		VtxSet(vtx, 3,         0, SCREEN_HT, -1, 32*-36, 32* 6, 0, 0, 0, 0xFF);
		gSPDisplayList(g++, gfx_wipe_begin);
		gDPSetCombineMode(g++, G_CC_MODULATERGBDECALA, G_CC_MODULATERGBDECALA);
		gDPSetTextureFilter(g++, G_TF_BILERP);
		gDPLoadTextureBlock(
			g++, txt_wipe[1], G_IM_FMT_IA, G_IM_SIZ_8b, 32, 64, 0,
			G_TX_MIRROR, G_TX_MIRROR, 5, 6, 0, 0
		);
		gSPTexture(g++, 0xFFFF, 0xFFFF, G_TX_NOLOD, G_TX_RENDERTILE, G_ON);
		gSPVertex(g++, K0_TO_PHYS(vtx), 4, 0);
		gSPDisplayList(g++, gfx_quad0);
		gSPTexture(g++, 0xFFFF, 0xFFFF, G_TX_NOLOD, G_TX_RENDERTILE, G_OFF);
		gSPDisplayList(g++, gfx_wipe_end);
		gSPEndDisplayList(g);
	}
	else
	{
		return NULL;
	}
	return gfx;
}

void *CtrlCannonOverlay(int code, SHAPE *shape, UNUSED void *data)
{
	SCALLBACK *shp = (SCALLBACK *)shape;
	Gfx *gfx = NULL;
	if (code == SC_DRAW)
	{
		if (scenep && scenep->cam->mode == 10) /* T:enum */
		{
			ShpSetLayer(&shp->s, LAYER_XLU_SURF);
			gfx = CannonOverlayGfx();
		}
	}
	return gfx;
}
