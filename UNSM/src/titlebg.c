#include <sm64.h>

extern Gfx gfx_wipe_begin[];

extern Gfx gfx_logo[];
extern Gfx gfx_symbol[];
extern float logo_scale_a[];
extern float logo_scale_b[];

extern Gfx gfx_titlebg_begin[];
extern Gfx gfx_titlebg_vtx[];
extern Gfx gfx_titlebg_0[];
extern Gfx gfx_titlebg_1[];
extern Gfx gfx_titlebg_2[];
extern Gfx gfx_titlebg_3[];
extern Gfx gfx_titlebg_end[];
extern u16 *txt_titlebg_mario[];
extern u16 *txt_titlebg_gameover[];

static int titlebg_timer;
static int titlebg_count;
static short titlebg_frame;
static int titlebg_alpha;

void *CtrlTitleLogo(int code, SHAPE *shape, UNUSED void *data)
{
	SCALLBACK *shp = (SCALLBACK *)shape;
	Gfx *gfx = NULL, *g = NULL;
	Mtx *mtx;
	float *a = SegmentToVirtual(logo_scale_a);
	float *b = SegmentToVirtual(logo_scale_b);
	if (code != SC_DRAW)
	{
		titlebg_frame = 0;
	}
	else if (code == SC_DRAW)
	{
		float x, y, z;
		ShpSetLayer(&shp->s, LAYER_OPA_SURF);
		mtx = GfxAlloc(sizeof(Mtx));
		g = gfx = GfxAlloc(sizeof(Gfx)*4);
		if (titlebg_frame >= 0 && titlebg_frame < 0+20)
		{
			x = a[3*(titlebg_frame-0)+0];
			y = a[3*(titlebg_frame-0)+1];
			z = a[3*(titlebg_frame-0)+2];
		}
		else if (titlebg_frame >= 0+20 && titlebg_frame < 75)
		{
			x = 1;
			y = 1;
			z = 1;
		}
		else if (titlebg_frame >= 75 && titlebg_frame < 75+16)
		{
			x = b[3*(titlebg_frame-75)+0];
			y = b[3*(titlebg_frame-75)+1];
			z = b[3*(titlebg_frame-75)+2];
		}
		else
		{
			x = 0;
			y = 0;
			z = 0;
		}
		guScale(mtx, x, y, z);
		gSPMatrix(g++, mtx, G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_PUSH);
		gSPDisplayList(g++, gfx_logo);
		gSPPopMatrix(g++, G_MTX_MODELVIEW);
		gSPEndDisplayList(g);
		titlebg_frame++;
	}
	return gfx;
}

void *CtrlTitleSymbol(int code, SHAPE *shape, UNUSED void *data)
{
	SCALLBACK *shp = (SCALLBACK *)shape;
	Gfx *gfx = NULL, *g = NULL;
	if (code != SC_DRAW)
	{
		titlebg_alpha = 0;
	}
	else if (code == SC_DRAW)
	{
		g = gfx = GfxAlloc(sizeof(Gfx)*5);
		gSPDisplayList(g++, gfx_wipe_begin);
		gDPSetEnvColor(g++, 0xFF, 0xFF, 0xFF, titlebg_alpha);
		switch (titlebg_alpha)
		{
		case 0xFF:
			ShpSetLayer(&shp->s, LAYER_OPA_SURF);
			gDPSetRenderMode(g++, G_RM_AA_OPA_SURF, G_RM_AA_OPA_SURF2);
			break;
		default:
			ShpSetLayer(&shp->s, LAYER_XLU_SURF);
			gDPSetRenderMode(g++, G_RM_AA_XLU_SURF, G_RM_AA_XLU_SURF2);
			break;
		}
		gSPDisplayList(g++, gfx_symbol);
		gSPEndDisplayList(g);
		if (titlebg_frame > 18)
		{
			titlebg_alpha += 26;
			if (titlebg_alpha > 0xFF) titlebg_alpha = 0xFF;
		}
	}
	return gfx;
}

static Gfx *TitleBGTile(int index, s8 *bg)
{
	static Gfx *gfx_titlebg[] =
	{
		gfx_titlebg_0,
		gfx_titlebg_1,
		gfx_titlebg_2,
		gfx_titlebg_3,
	};
	static float x[] = {0, 80, 160, 240, 0, 80, 160, 240, 0, 80, 160, 240};
	static float y[] = {160, 160, 160, 160, 80, 80, 80, 80, 0, 0, 0, 0};
	static u16 **txt_titlebg[] =
	{
		txt_titlebg_mario,
		txt_titlebg_gameover,
	};
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	Gfx *gfx, *g = gfx = GfxAlloc(sizeof(Gfx)*(2 + 4*(7+1) + 2));
	u16 **txt = SegmentToVirtual(txt_titlebg[bg[index]]);
	int i;
	guTranslate(mtx, x[index], y[index], 0);
	gSPMatrix(g++, mtx, G_MTX_MODELVIEW|G_MTX_LOAD|G_MTX_PUSH);
	gSPDisplayList(g++, gfx_titlebg_vtx);
	for (i = 0; i < 4; i++)
	{
		gDPLoadTextureBlock(
			g++, txt[i], G_IM_FMT_RGBA, G_IM_SIZ_16b, 80, 20, 0,
			G_TX_CLAMP, G_TX_CLAMP, 7, 6, G_TX_NOLOD, G_TX_NOLOD
		);
		gSPDisplayList(g++, gfx_titlebg[i]);
	}
	gSPPopMatrix(g++, G_MTX_MODELVIEW);
	gSPEndDisplayList(g);
	return gfx;
}

void *CtrlTitleBG(int code, SHAPE *shape, UNUSED void *data)
{
	static s8 bg_mario[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	static s8 *bg_table[] = {bg_mario};
	SCALLBACK *shp = (SCALLBACK *)shape;
	int index = shp->arg & 0xFF;
	s8 *bg = bg_table[index];
	Gfx *gfx = NULL, *g = NULL;
	int i;
	if (code == SC_DRAW)
	{
		g = gfx = GfxAlloc(sizeof(Gfx)*(2 + 4*3 + 2));
		ShpSetLayer(&shp->s, LAYER_OPA_SURF);
		gSPDisplayList(g++, gfx_wipe_begin);
		gSPDisplayList(g++, gfx_titlebg_begin);
		for (i = 0; i < 4*3; i++)
		{
			gSPDisplayList(g++, TitleBGTile(i, bg));
		}
		gSPDisplayList(g++, gfx_titlebg_end);
		gSPEndDisplayList(g);
	}
	return gfx;
}

void *CtrlGameOverBG(int code, SHAPE *shape, UNUSED void *data)
{
	static s8 bg[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
	static s8 flip[] = {0, 1, 2, 3, 7, 11, 10, 9, 8, 4, 5, 6};
	SCALLBACK *shp = (SCALLBACK *)shape;
	Gfx *gfx = NULL, *g = NULL;
	int i;
	if (code != SC_DRAW)
	{
		int i;
		titlebg_timer = 0;
		titlebg_count = -2;
		for (i = 0; i < 4*3; i++)
		{
			bg[i] = 1;
		}
	}
	else
	{
		g = gfx = GfxAlloc(sizeof(Gfx)*(2 + 4*3 + 2));
		if (titlebg_count == -2)
		{
			if (titlebg_timer == 180)
			{
				titlebg_count++;
				titlebg_timer = 0;
			}
		}
		else if (titlebg_count != 12-1 && !(titlebg_timer & 1))
		{
			titlebg_count++;
			bg[flip[titlebg_count]] = 0;
		}
		if (titlebg_count != 12-1) titlebg_timer++;
		ShpSetLayer(&shp->s, LAYER_OPA_SURF);
		gSPDisplayList(g++, gfx_wipe_begin);
		gSPDisplayList(g++, gfx_titlebg_begin);
		for (i = 0; i < 4*3; i++)
		{
			gSPDisplayList(g++, TitleBGTile(i, bg));
		}
		gSPDisplayList(g++, gfx_titlebg_end);
		gSPEndDisplayList(g);
	}
	return gfx;
}
