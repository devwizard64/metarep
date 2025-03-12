#include <sm64.h>

#define STEP_WL 0x20
#define STEP_WM 0x10
#define STEP_WR 0x08
#define STEP_PL 0x04
#define STEP_PM 0x02
#define STEP_PR 0x01

#define XSTEP   30
#define XPOSX   40
#define XCENT   50
#define YPOSY   60
#define YPOSZ   70
#define YCENT   80
#define TRST    100
#define TNOP    (CHAR)200

typedef struct wavevtx
{
	short x;
	short y;
	short z;
	s8 nx;
	s8 ny;
	s8 nz;
}
WAVEVTX;

typedef struct wavetri
{
	float nx;
	float ny;
	float nz;
}
WAVETRI;

extern Gfx gfx_wave_s_begin[];
extern Gfx gfx_wave_s_end[];
extern Gfx gfx_wave_e_begin[];
extern Gfx gfx_wave_e_end[];
extern Gfx gfx_wave_draw[];
extern short wave_meshdata[];
extern short wave_normdata[];

static short wave_bgcode;
static float wave_posx;
static float wave_posy;
static float wave_posz;
static WAVEVTX *wavevtx;
static WAVETRI *wavetri;
WAVE *wavep;
char wave_8036131C; /* waterport status */

extern WAVE wave_hmc_0702551C;

static WAVE *wavetab0[] =
{
	&wave_hmc_0702551C,
	NULL,
};

extern WAVE wave_inside_07023620;
extern WAVE wave_inside_07023698;
extern WAVE wave_inside_07023710;
extern WAVE wave_inside_07023788;
extern WAVE wave_inside_07023800;
extern WAVE wave_inside_07023878;
extern WAVE wave_inside_070238F0;
extern WAVE wave_inside_07023968;
extern WAVE wave_inside_070239E0;
extern WAVE wave_inside_07023A58;
extern WAVE wave_inside_07023AD0;
extern WAVE wave_inside_07023B48;
extern WAVE wave_inside_07023BC0;
extern WAVE wave_inside_07023C38;

static WAVE *wavetab1[] =
{
	&wave_inside_07023620,
	&wave_inside_07023698,
	&wave_inside_07023710,
	&wave_inside_07023788,
	&wave_inside_07023800,
	&wave_inside_07023878,
	&wave_inside_070238F0,
	&wave_inside_07023968,
	&wave_inside_070239E0,
	&wave_inside_07023A58,
	&wave_inside_07023AD0,
	&wave_inside_07023B48,
	&wave_inside_07023BC0,
	&wave_inside_07023C38,
	NULL,
};

extern WAVE wave_ttm_07012F00;

static WAVE *wavetab2[] =
{
	&wave_ttm_07012F00,
	NULL,
};

static WAVE **wavetab[] =
{
	wavetab0,
	wavetab1,
	wavetab2,
};

static short wave_timer = 1;
static short wave_stamp = 0;

static void WaveStopAll(WAVE *wave, WAVE **table)
{
	SHORT i, code = wave->code;
	i = 0;
	while (table[i])
	{
		WAVE *w = SegmentToVirtual(table[i]);
		if (w->code != code) w->state = WAVE_STILL;
		i++;
	}
}

static float WaveYPosY(WAVE *wave)
{
	float y = wave_posy - wave->posy + 50.0;
	if      (y <        0.0) y = 0;
	else if (y > wave->size) y = wave->size;
	return y;
}

static float WaveYPosZ(WAVE *wave)
{
	float y = wave->posz - wave_posz;
	if      (y <        0.0) y = 0;
	else if (y > wave->size) y = wave->size;
	return y;
}

static float WaveGetCenterY(WAVE *wave, CHAR code)
{
	switch (code)
	{
	case YPOSY: return WaveYPosY(wave); break;
	case YPOSZ: return WaveYPosZ(wave); break;
	case YCENT: return wave->size / 2.0; break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
}

static float WaveXStep(WAVE *wave)
{
	float l = wave->size / 4.0;
	float m = wave->size / 2.0;
	float r = wave->size * 3.0/4.0;
	if      (wave->steptrig & STEP_WL) return l;
	else if (wave->steptrig & STEP_WM) return m;
	else if (wave->steptrig & STEP_WR) return r;
	else if (wave->steptrig & STEP_PL) return l;
	else if (wave->steptrig & STEP_PM) return m;
	else if (wave->steptrig & STEP_PR) return r;
#ifdef __GNUC__
	__builtin_unreachable();
#endif
}

static float WaveXPosX(WAVE *wave)
{
	float x = wave_posx - wave->posx;
	if      (x <        0.0) x = 0;
	else if (x > wave->size) x = wave->size;
	return x;
}

static float WaveGetCenterX(WAVE *wave, CHAR code)
{
	switch (code)
	{
	case XSTEP: return WaveXStep(wave); break;
	case XPOSX: return WaveXPosX(wave); break;
	case XCENT: return wave->size / 2.0; break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
}

static void WaveStart(
	CHAR state, WAVE *wave, WAVE **table, CHAR xcode, CHAR ycode, CHAR tcode
)
{
	WaveStopAll(wave, table);
	switch (state)
	{
	case WAVE_TOUCH:
		wave->depth = wave->touchdepth;
		wave->decay = wave->touchdecay;
		wave->speed = wave->touchspeed;
		wave->scale = wave->touchscale;
		break;
	case WAVE_ENTER:
		wave->depth = wave->enterdepth;
		wave->decay = wave->enterdecay;
		wave->speed = wave->enterspeed;
		wave->scale = wave->enterscale;
		break;
	}
	wave->state = state;
	wave->centerx = WaveGetCenterX(wave, xcode);
	wave->centery = WaveGetCenterY(wave, ycode);
	pool_entry = wave_posy;
	if (tcode == TRST) wave->timer = 0;
	wavep = wave;
}

#define TOUCH(x, y, t) WaveStart(WAVE_TOUCH, wave, table, x, y, t)
#define ENTER(x, y, t) WaveStart(WAVE_ENTER, wave, table, x, y, t)

static void WaveProcV10Still(WAVE *wave, WAVE **table)
{
	if      (wave->steptrig & STEP_WL) TOUCH(XSTEP, YPOSY, TRST);
	else if (wave->steptrig & STEP_WM) TOUCH(XSTEP, YPOSY, TRST);
	else if (wave->steptrig & STEP_WR) TOUCH(XSTEP, YPOSY, TRST);
	else if (wave->steptrig & STEP_PL) ENTER(XSTEP, YPOSY, TRST);
	else if (wave->steptrig & STEP_PM) ENTER(XSTEP, YPOSY, TRST);
	else if (wave->steptrig & STEP_PR) ENTER(XSTEP, YPOSY, TRST);
}

static void WaveProcV10Touch(WAVE *wave, WAVE **table)
{
	if      (wave->steptrig & STEP_PL) ENTER(XSTEP, YPOSY, TRST);
	else if (wave->steptrig & STEP_PM) ENTER(XSTEP, YPOSY, TRST);
	else if (wave->steptrig & STEP_PR) ENTER(XSTEP, YPOSY, TRST);
}

static void WaveProcV20Still(WAVE *wave, WAVE **table)
{
	if      (wave->steptrig & STEP_WL) TOUCH(XCENT, YCENT, TRST);
	else if (wave->steptrig & STEP_WM) TOUCH(XCENT, YCENT, TRST);
	else if (wave->steptrig & STEP_WR) TOUCH(XCENT, YCENT, TRST);
	else if (wave->steptrig & STEP_PL) ENTER(XSTEP, YPOSY, TRST);
	else if (wave->steptrig & STEP_PM) ENTER(XSTEP, YPOSY, TRST);
	else if (wave->steptrig & STEP_PR) ENTER(XSTEP, YPOSY, TRST);
}

static void WaveProcV20Touch(WAVE *wave, WAVE **table)
{
	if      (wave->steptrig & STEP_PL) ENTER(XSTEP, YPOSY, TNOP);
	else if (wave->steptrig & STEP_PM) ENTER(XSTEP, YPOSY, TNOP);
	else if (wave->steptrig & STEP_PR) ENTER(XSTEP, YPOSY, TNOP);
}

static void WaveProcH10Still(WAVE *wave, WAVE **table)
{
	if      (wave->steptrig & STEP_WL) TOUCH(XPOSX, YPOSZ, TRST);
	else if (wave->steptrig & STEP_WM) TOUCH(XPOSX, YPOSZ, TRST);
	else if (wave->steptrig & STEP_WR) TOUCH(XPOSX, YPOSZ, TRST);
	else if (wave->divetrig)
	{
		if      (wave->stepstat & STEP_PL) ENTER(XPOSX, YPOSZ, TRST);
		else if (wave->stepstat & STEP_PM) ENTER(XPOSX, YPOSZ, TRST);
		else if (wave->stepstat & STEP_PR) ENTER(XPOSX, YPOSZ, TRST);
	}
}

static void WaveProcH10Touch(WAVE *wave, WAVE **table)
{
	if (wave->divetrig)
	{
		if      (wave->stepstat & STEP_PL) ENTER(XPOSX, YPOSZ, TRST);
		else if (wave->stepstat & STEP_PM) ENTER(XPOSX, YPOSZ, TRST);
		else if (wave->stepstat & STEP_PR) ENTER(XPOSX, YPOSZ, TRST);
	}
}

static void WaveProcH20Still(WAVE *wave, WAVE **table)
{
	if      (wave->steptrig & STEP_WL) TOUCH(XCENT, YCENT, TRST);
	else if (wave->steptrig & STEP_WM) TOUCH(XCENT, YCENT, TRST);
	else if (wave->steptrig & STEP_WR) TOUCH(XCENT, YCENT, TRST);
	else if (wave->stepstat & STEP_PL) ENTER(XPOSX, YPOSZ, TRST);
	else if (wave->stepstat & STEP_PM) ENTER(XPOSX, YPOSZ, TRST);
	else if (wave->stepstat & STEP_PR) ENTER(XPOSX, YPOSZ, TRST);
}

static void WaveProcH20Touch(WAVE *wave, WAVE **table)
{
	if (wave->divetrig)
	{
		if      (wave->stepstat & STEP_PL) ENTER(XPOSX, YPOSZ, TNOP);
		else if (wave->stepstat & STEP_PM) ENTER(XPOSX, YPOSZ, TNOP);
		else if (wave->stepstat & STEP_PR) ENTER(XPOSX, YPOSZ, TNOP);
	}
}

static void WaveProcFlag(WAVE *wave)
{
	SHORT code = wave->code;
	CHAR wl = 0;
	CHAR wm = 0;
	CHAR wr = 0;
	CHAR pl = 0;
	CHAR pm = 0;
	CHAR pr = 0;
	if (wave_bgcode == BG_WAVEL(code)) wl = STEP_WL;
	if (wave_bgcode == BG_WAVEM(code)) wm = STEP_WM;
	if (wave_bgcode == BG_WAVER(code)) wr = STEP_WR;
	if (wave_bgcode == BG_PORTL(code)) pl = STEP_PL;
	if (wave_bgcode == BG_PORTM(code)) pm = STEP_PM;
	if (wave_bgcode == BG_PORTR(code)) pr = STEP_PR;
	wave->stepprev = wave->stepstat;
	wave->stepstat = wl + wm + wr + pl + pm + pr;
	wave->steptrig = (wave->stepprev^wave->stepstat) & wave->stepstat;
	wave->diveprev = wave->divestat;
	if (wave_posy < wave->posy) wave->divestat = 1;
	else                        wave->divestat = 0;
	wave->divetrig = (wave->diveprev^wave->divestat) & wave->divestat;
}

static void WaveProcMove(WAVE *wave)
{
	if (wave_timer != wave_stamp)
	{
		wave->depth *= wave->decay;
		wave->timer += 1.0;
	}
	if (wave->mode == WAVE_10)
	{
		if (wave->depth <= 1.0)
		{
			wave->state = 0;
			wavep = 0;
		}
	}
	else if (wave->mode == WAVE_20 && wave->state == WAVE_ENTER)
	{
		if (wave->depth <= wave->touchdepth)
		{
			wave->state = WAVE_TOUCH;
			wave->depth = wave->touchdepth;
			wave->decay = wave->touchdecay;
			wave->speed = wave->touchspeed;
			wave->scale = wave->touchscale;
		}
	}
}

static SHORT WaveCalcZ(WAVE *wave, float x, float y)
{
	float depth = wave->depth;
	float speed = wave->speed;
	float scale = wave->scale;
	float timer = wave->timer;
	float centerx = wave->centerx;
	float centery = wave->centery;
	float d, dist;
	x *= wave->size / 614.0;
	y *= wave->size / 614.0;
	d = DIST2(x-centerx, y-centery);
	dist = d / scale;
	if (timer < dist)
	{
		return 0;
	}
	else
	{
		float z = depth * cosf(2*M_PI * speed * (timer-dist));
		return RoundFtoS(z);
	}
}

static SHORT WaveGetZ(WAVE *wave, SHORT flag, SHORT x, SHORT y)
{
	SHORT z = 0;
	if (flag) z = WaveCalcZ(wave, x, y);
	return z;
}

static void WaveMakeVtx(WAVE *wave, short *mesh, SHORT nvtx)
{
	SHORT i;
	if (!(wavevtx = malloc(sizeof(WAVEVTX)*nvtx)))
	{
	}
	for (i = 0; i < nvtx; i++)
	{
		wavevtx[i].x = mesh[1+3*i+0];
		wavevtx[i].y = mesh[1+3*i+1];
		wavevtx[i].z =
			WaveGetZ(wave, mesh[1+3*i+2], wavevtx[i].x, wavevtx[i].y);
	}
}

static void WaveMakeTri(short *mesh, SHORT nvtx, SHORT ntri)
{
	SHORT i;
	if (!(wavetri = malloc(sizeof(WAVETRI)*ntri)))
	{
	}
	for (i = 0; i < ntri; i++)
	{
		SHORT v = 1 + 3*nvtx + 1 + 3*i;
		SHORT v0 = mesh[v+0];
		SHORT v1 = mesh[v+1];
		SHORT v2 = mesh[v+2];
		float x0 = wavevtx[v0].x;
		float y0 = wavevtx[v0].y;
		float z0 = wavevtx[v0].z;
		float x1 = wavevtx[v1].x;
		float y1 = wavevtx[v1].y;
		float z1 = wavevtx[v1].z;
		float x2 = wavevtx[v2].x;
		float y2 = wavevtx[v2].y;
		float z2 = wavevtx[v2].z;
		wavetri[i].nx = CROSS3(z0, y0, z1, y1, z2, y2);
		wavetri[i].ny = CROSS3(x0, z0, x1, z1, x2, z2);
		wavetri[i].nz = CROSS3(y0, x0, y1, x1, y2, x2);
	}
}

static CHAR WaveScaleNormal(float x)
{
	CHAR y;
	if      (x > 0.0)   y = 127.0*x + 0.5;
	else if (x < 0.0)   y = 128.0*x - 0.5;
	else                y = 0;
	return y;
}

static void WaveCalcNormal(short *norm, SHORT nvtx)
{
	UNUSED SHORT x;
	SHORT t, i, n, count, index = 0;
	for (i = 0; i < nvtx; i++)
	{
		float nx = 0, ny = 0, nz = 0, d;
		count = norm[index];
		for (n = 0; n < count; n++)
		{
			t = norm[1+index+n];
			nx += wavetri[t].nx;
			ny += wavetri[t].ny;
			nz += wavetri[t].nz;
		}
		index += 1 + count;
		nx /= count;
		ny /= count;
		nz /= count;
		if ((d = DIST3(nx, ny, nz)) == 0.0)
		{
			wavevtx[i].nx = 0;
			wavevtx[i].ny = 0;
			wavevtx[i].nz = 0;
		}
		else
		{
			wavevtx[i].nx = WaveScaleNormal(nx/d);
			wavevtx[i].ny = WaveScaleNormal(ny/d);
			wavevtx[i].nz = WaveScaleNormal(nz/d);
		}
	}
}

static Gfx *WaveDrawMesh(
	u16 *txt, SHORT wd, SHORT ht, short *mesh, SHORT nvtx, SHORT ntri,
	UCHAR alpha
)
{
	SHORT i, n, index, tri, v, s, t;
	SHORT n5 = ntri / 5;
	SHORT n1 = ntri % 5;
	SHORT vlen = 3*ntri;
	SHORT glen = 5 + 2*n5 + 1 + n1 + 1;
	Vtx *vtx = GfxAlloc(sizeof(Vtx)*vlen);
	Gfx *gfx, *g = gfx = GfxAlloc(sizeof(Gfx)*glen);
	if (!vtx || !gfx)
	{
	}
	gDPLoadImageBlockT(g++, txt, G_IM_FMT_RGBA, G_IM_SIZ_16b, wd, ht);
	for (i = 0; i < n5; i++)
	{
		index = 1 + 3*nvtx + 1 + 3*5*i;
		for (n = 0; n < 15; n++)
		{
			tri = mesh[index+n];
			v = mesh[1+3*tri+0];
			s = mesh[1+3*tri+1];
			t = mesh[1+3*tri+2];
			VtxSet(
				vtx, 15*i+n, wavevtx[v].x, wavevtx[v].y, wavevtx[v].z, s, t,
				wavevtx[v].nx, wavevtx[v].ny, wavevtx[v].nz, alpha
			);
		}
		gSPVertex(g++, K0_TO_PHYS(&vtx[15*i]), 15, 0);
		gSPDisplayList(g++, gfx_wave_draw);
	}
	index = 1 + 3*nvtx + 1 + 3*5*n5;
	for (n = 0; n < 3*n1; n++)
	{
		tri = mesh[index+n];
		v = mesh[1+3*tri+0];
		s = mesh[1+3*tri+1];
		t = mesh[1+3*tri+2];
		VtxSet(
			vtx, 3*5*n5+n, wavevtx[v].x, wavevtx[v].y, wavevtx[v].z, s, t,
			wavevtx[v].nx, wavevtx[v].ny, wavevtx[v].nz, alpha
		);
	}
	gSPVertex(g++, K0_TO_PHYS(&vtx[3*5*n5]), 3*n1, 0);
	for (i = 0; i < n1; i++)
	{
		gSP1Triangle(g++, 3*i+0, 3*i+1, 3*i+2, 0);
	}
	gSPEndDisplayList(g);
	return gfx;
}

static Gfx *WaveTransform(WAVE *wave)
{
	float scale = wave->size / 614.0;
	Mtx *mtxx = GfxAlloc(sizeof(Mtx));
	Mtx *mtxy = GfxAlloc(sizeof(Mtx));
	Mtx *mtxt = GfxAlloc(sizeof(Mtx));
	Mtx *mtxs = GfxAlloc(sizeof(Mtx));
	Gfx *gfx, *g = gfx = GfxAlloc(sizeof(Gfx)*5);
	if (!mtxx || !mtxy || !mtxt || !gfx)
	{
	}
	guTranslate(mtxt, wave->posx, wave->posy, wave->posz);
	guRotate(mtxx, wave->angx, 1, 0, 0);
	guRotate(mtxy, wave->angy, 0, 1, 0);
	guScale(mtxs, scale, scale, scale);
	gSPMatrix(g++, mtxt, G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_PUSH);
	gSPMatrix(g++, mtxx, G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_NOPUSH);
	gSPMatrix(g++, mtxy, G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_NOPUSH);
	gSPMatrix(g++, mtxs, G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_NOPUSH);
	gSPEndDisplayList(g);
	return gfx;
}

static Gfx *WaveGfxShade(WAVE *wave)
{
	SHORT nvtx, ntri, i;
	short *mesh;
	SHORT nmesh = wave->nmesh;
	SHORT wd = wave->wd;
	SHORT ht = wave->ht;
	short **meshlist = SegmentToVirtual(wave->meshlist);
	u16 **txtlist = SegmentToVirtual(wave->txtlist);
	Gfx *gfx, *g = gfx = GfxAlloc(sizeof(Gfx)*(3+nmesh+3));
	if (!gfx) return gfx;
	gSPDisplayList(g++, WaveTransform(wave));
	gSPDisplayList(g++, gfx_wave_s_begin);
	gSPDisplayList(g++, wave->movegfx);
	for (i = 0; i < nmesh; i++)
	{
		mesh = SegmentToVirtual(meshlist[i]);
		nvtx = mesh[0];
		ntri = mesh[1+3*nvtx];
		gSPDisplayList(g++, WaveDrawMesh(
			txtlist[i], wd, ht, mesh, nvtx, ntri, wave->alpha
		));
	}
	WaveProcMove(wave);
	gSPPopMatrix(g++, G_MTX_MODELVIEW);
	gSPDisplayList(g++, gfx_wave_s_end);
	gSPEndDisplayList(g);
	return gfx;
}

static Gfx *WaveGfxEnvMap(WAVE *wave)
{
	SHORT nvtx, ntri;
	short *mesh;
	SHORT wd = wave->wd;
	SHORT ht = wave->ht;
	short **meshlist = SegmentToVirtual(wave->meshlist);
	u16 **txtlist = SegmentToVirtual(wave->txtlist);
	Gfx *gfx, *g = gfx = GfxAlloc(sizeof(Gfx)*7);
	if (!gfx) return gfx;
	gSPDisplayList(g++, WaveTransform(wave));
	gSPDisplayList(g++, gfx_wave_e_begin);
	gSPDisplayList(g++, wave->movegfx);
	mesh = SegmentToVirtual(meshlist[0]);
	nvtx = mesh[0];
	ntri = mesh[1+3*nvtx];
	gSPDisplayList(g++, WaveDrawMesh(
		txtlist[0], wd, ht, mesh, nvtx, ntri, wave->alpha
	));
	WaveProcMove(wave);
	gSPPopMatrix(g++, G_MTX_MODELVIEW);
	gSPDisplayList(g++, gfx_wave_e_end);
	gSPEndDisplayList(g);
	return gfx;
}

static Gfx *WaveGfxMove(WAVE *wave)
{
	short *mesh = SegmentToVirtual(wave_meshdata);
	short *norm = SegmentToVirtual(wave_normdata);
	SHORT nvtx = mesh[0];
	SHORT ntri = mesh[1+3*nvtx];
	Gfx *gfx;
	WaveMakeVtx(wave, mesh, nvtx);
	WaveMakeTri(mesh, nvtx, ntri);
	WaveCalcNormal(norm, nvtx);
	switch (wave->type)
	{
	case WAVE_SHADE:    gfx = WaveGfxShade(wave); break;
	case WAVE_ENVMAP:   gfx = WaveGfxEnvMap(wave); break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
	free(wavevtx);
	free(wavetri);
	return gfx;
}

static Gfx *WaveGfxStat(WAVE *wave)
{
	Gfx *gfx, *g = gfx = GfxAlloc(sizeof(Gfx)*4);
	if (!gfx) return gfx;
	gSPDisplayList(g++, WaveTransform(wave));
	gSPDisplayList(g++, wave->statgfx);
	gSPPopMatrix(g++, G_MTX_MODELVIEW);
	gSPEndDisplayList(g);
	return gfx;
}

static void WaveExit(WAVE *wave)
{
	wave->stepprev = 0;
	wave->stepstat = 0;
	wave->steptrig = 0;
	wave->diveprev = 0;
	wave->divestat = 0;
	wave->divetrig = 0;
	wavep = NULL;
}

static void WaveMoveDemo(WAVE *wave, float start, float end, float speed)
{
	u32 star = BuGetStar(COURSE_DDD-1);
	u32 flag = BuGetFlag();
	u32 havestar = star & 1;
	u32 demoflag = flag & BU_WAVEDEMO;
	if (!havestar && !demoflag)
	{
		wave->posx = start;
		wave_8036131C = 0;
	}
	else if (havestar && !demoflag)
	{
		wave->posx += speed;
		wave_8036131C = 2;
		if (wave->posx >= end)
		{
			wave->posx = end;
			BuSetFlag(BU_WAVEDEMO);
		}
	}
	else if (havestar && demoflag)
	{
		wave->posx = end;
		wave_8036131C = 3;
	}
}

static void WaveSetLayer(SCALLBACK *shp, WAVE *wave)
{
	switch (wave->alpha)
	{
	case 0xFF:  ShpSetLayer(&shp->s, LAYER_OPA_SURF); break;
	default:    ShpSetLayer(&shp->s, LAYER_XLU_SURF); break;
	}
}

static Gfx *WaveGfx(WAVE *wave)
{
	switch (wave->state)
	{
	case WAVE_STILL:    return WaveGfxStat(wave); break;
	default:            return WaveGfxMove(wave); break;
	}
}

static void WaveProcV(WAVE *wave, WAVE **table)
{
	if (wave->mode == WAVE_10)
	{
		switch (wave->state)
		{
		case WAVE_STILL: WaveProcV10Still(wave, table); break;
		case WAVE_TOUCH: WaveProcV10Touch(wave, table); break;
		}
	}
	else if (wave->mode == WAVE_20)
	{
		switch (wave->state)
		{
		case WAVE_STILL: WaveProcV20Still(wave, table); break;
		case WAVE_TOUCH: WaveProcV20Touch(wave, table); break;
		}
	}
}

static void WaveProcH(WAVE *wave, WAVE **table)
{
	if (wave->mode == WAVE_10)
	{
		switch (wave->state)
		{
		case WAVE_STILL: WaveProcH10Still(wave, table); break;
		case WAVE_TOUCH: WaveProcH10Touch(wave, table); break;
		}
	}
	else if (wave->mode == WAVE_20)
	{
		switch (wave->state)
		{
		case WAVE_STILL: WaveProcH20Still(wave, table); break;
		case WAVE_TOUCH: WaveProcH20Touch(wave, table); break;
		}
	}
}

void *CtrlWaveDraw(int code, SHAPE *shape, UNUSED void *data)
{
	SCALLBACK *shp = (SCALLBACK *)shape;
	int i = shp->arg >> 8 & 0xFF;
	int n = shp->arg >> 0 & 0xFF;
	Gfx *gfx = NULL;
	WAVE **table = wavetab[i];
	WAVE *wave = SegmentToVirtual(table[n]);
	if (code != SC_DRAW)
	{
		WaveExit(wave);
	}
	else if (code == SC_DRAW)
	{
		if (i == 1 && n == 7) WaveMoveDemo(wave, 3456, 5529.6F, 20);
		WaveSetLayer(shp, wave);
		gfx = WaveGfx(wave);
		WaveProcFlag(wave);
		switch ((SHORT)wave->angx)
		{
		case 0:     WaveProcV(wave, table); break;
		default:    WaveProcH(wave, table); break;
		}
	}
	return gfx;
}

void *CtrlWaveProc(int code, UNUSED SHAPE *shape, UNUSED void *data)
{
	if (code != SC_DRAW)
	{
		wave_stamp = draw_timer-1;
		wave_timer = draw_timer;
	}
	else
	{
		BGFACE *ground;
		wave_stamp = wave_timer;
		wave_timer = draw_timer;
		BGCheckGround(
			mario_obj->o_posx, mario_obj->o_posy, mario_obj->o_posz, &ground
		);
		/* missing null check */
		wave_bgcode = ground->code;
		wave_posx = mario_obj->o_posx;
		wave_posy = mario_obj->o_posy;
		wave_posz = mario_obj->o_posz;
	}
	return NULL;
}
