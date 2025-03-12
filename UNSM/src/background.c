#include <sm64.h>

extern Gfx gfx_quad0[];
extern Gfx gfx_background_begin[];
extern Gfx gfx_background_tile[];
extern Gfx gfx_background_end[];

extern BACKGROUND background_a;
extern BACKGROUND background_d;
extern BACKGROUND background_e;
extern BACKGROUND background_f;
extern BACKGROUND background_b;
extern BACKGROUND background_g;
extern BACKGROUND background_h;
extern BACKGROUND background_i;
extern BACKGROUND background_c;
extern BACKGROUND background_j;

static BACKGROUND *backtab[] =
{
	&background_a,
	&background_d,
	&background_e,
	&background_f,
	&background_b,
	&background_g,
	&background_h,
	&background_i,
	&background_c,
	&background_j,
};

#define BACK_WD (SCREEN_WD*4)
#define BACK_HT (SCREEN_HT*4)
#define TILE_WD (SCREEN_WD/2)
#define TILE_HT (SCREEN_HT/2)

typedef struct backdata
{
	unsigned short angy;
	short angx;
	int posx;
	int posy;
	int index;
}
BACKDATA;

static BACKDATA backdata[2];

static int BackPosX(CHAR screen, float fovy)
{
	float angy = backdata[screen].angy;
	float xf = (SCREEN_WD*360.0*angy) / (fovy*65536.0);
	int x = xf + 0.5;
	if (x > BACK_WD) x -= x/BACK_WD*BACK_WD;
	return BACK_WD - x;
}

static int BackPosY(CHAR screen, UNUSED float fovy)
{
	float deg = (float)backdata[screen].angx * 360.0/65535.0;
	float yf = 360 * deg / 90.0;
	int yi = RoundFtoS(yf);
	int y = yi + TILE_HT*5;
	if (y > BACK_HT) y = BACK_HT;
	if (y < SCREEN_HT) y = SCREEN_HT;
	return y;
}

static int BackIndex(CHAR screen)
{
	int x = (          backdata[screen].posx) / TILE_WD;
	int y = (BACK_HT - backdata[screen].posy) / TILE_HT;
	return BACK_TW*y + x;
}

#define BackSetVtx(vtx, i, x, y, s, t, rgb) \
	VtxSet(vtx, i, x, y, -1, 32*(s), 32*(t), rgb[0], rgb[1], rgb[2], 0xFF)

static Vtx *BackVtx(int index, CHAR shade)
{
	static u8 rgb[][3] =
	{
		{  80,  100,   90},
		{0xFF, 0xFF, 0xFF},
	};
	Vtx *vtx = GfxAlloc(sizeof(Vtx)*4);
	SHORT x =           TILE_WD*(index%BACK_TW);
	SHORT y = BACK_HT - TILE_HT*(index/BACK_TW);
	if (vtx)
	{
		BackSetVtx(vtx, 0, x        , y        ,  0,  0, rgb[shade]);
		BackSetVtx(vtx, 1, x        , y-TILE_HT,  0, 31, rgb[shade]);
		BackSetVtx(vtx, 2, x+TILE_WD, y-TILE_HT, 31, 31, rgb[shade]);
		BackSetVtx(vtx, 3, x+TILE_WD, y        , 31,  0, rgb[shade]);
	}
	else
	{
	}
	return vtx;
}

static void BackTile(Gfx **g, CHAR type, CHAR screen, CHAR shade)
{
	int y, x;
	for (y = 0; y < 3; y++)
	{
		for (x = 0; x < 3; x++)
		{
			int index = backdata[screen].index + BACK_TW*y + x;
			u16 *txt = ((BACKGROUND *)SegmentToVirtual(backtab[type]))->txt[index];
			Vtx *vtx = BackVtx(index, shade);
			gDPLoadImageBlockT(
				(*g)++, txt, G_IM_FMT_RGBA, G_IM_SIZ_16b, 32, 32
			);
			gSPVertex((*g)++, K0_TO_PHYS(vtx), 4, 0);
			gSPDisplayList((*g)++, gfx_quad0);
		}
	}
}

static Mtx *BackMtx(CHAR screen)
{
	float l = backdata[screen].posx;
	float r = backdata[screen].posx + SCREEN_WD;
	float b = backdata[screen].posy - SCREEN_HT;
	float t = backdata[screen].posy;
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	if (mtx)
	{
		guOrtho(mtx, l, r, b, t, 0, 3, 1);
	}
	else
	{
	}
	return mtx;
}

static Gfx *BackGfx(CHAR screen, CHAR type, CHAR shade)
{
	int len = 3 + 7*3*3 + 2;
	Gfx *gfx, *g = gfx = GfxAlloc(sizeof(Gfx)*len);
	if (!gfx)
	{
		return NULL;
	}
	else
	{
		Mtx *mtx = BackMtx(screen);
		gSPDisplayList(g++, gfx_background_begin);
		gSPMatrix(
			g++, K0_TO_PHYS(mtx), G_MTX_PROJECTION|G_MTX_MUL|G_MTX_NOPUSH
		);
		gSPDisplayList(g++, gfx_background_tile);
		BackTile(&g, type, screen, shade);
		gSPDisplayList(g++, gfx_background_end);
		gSPEndDisplayList(g);
	}
	return gfx;
}

Gfx *BackgroundDraw(
	CHAR screen, CHAR type, float fovy,
	float eye_x, float eye_y, float eye_z,
	float look_x, float look_y, float look_z
)
{
	float dx = look_x - eye_x;
	float dy = look_y - eye_y;
	float dz = look_z - eye_z;
	CHAR shade = 1;
	if (type == BACK_C && !(BuGetStar(COURSE_JRB-1) & 1)) shade = 0;
	fovy = 90;
	backdata[screen].angy = ATAN2(dz, dx);
	backdata[screen].angx = ATAN2(DIST2(dx, dz), dy);
	backdata[screen].posx = BackPosX(screen, fovy);
	backdata[screen].posy = BackPosY(screen, fovy);
	backdata[screen].index = BackIndex(screen);
	return BackGfx(screen, type, shade);
}
