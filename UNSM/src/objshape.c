#include <sm64.h>

void VtxSet(
	Vtx *vtx, int i, SHORT x, SHORT y, SHORT z, SHORT s, SHORT t,
	UCHAR r, UCHAR g, UCHAR b, UCHAR a
)
{
	vtx[i].v.ob[0] = x;
	vtx[i].v.ob[1] = y;
	vtx[i].v.ob[2] = z;
	vtx[i].v.flag  = 0;
	vtx[i].v.tc[0] = s;
	vtx[i].v.tc[1] = t;
	vtx[i].v.cn[0] = r;
	vtx[i].v.cn[1] = g;
	vtx[i].v.cn[2] = b;
	vtx[i].v.cn[3] = a;
}

SHORT RoundFtoS(float x)
{
	if (x >= 0.0) return x + 0.5;
	else return x - 0.5;
}

/* TotWC entry */
extern Gfx gfx_inside_0702A880[];
void *Ctrl_objshape_802D2360(int code, SHAPE *shape, UNUSED void *data)
{
	u32 flag;
	SCALLBACK *shp;
	Gfx *g = NULL, *gfx = NULL;
	if (code == SC_DRAW)
	{
		flag = BuGetFlag();
		if (hud.star >= 10 && !(flag & BU_REDSW))
		{
			if (!(gfx = GfxAlloc(sizeof(Gfx)*2))) return NULL;
			else g = gfx;
			shp = (SCALLBACK *)shape;
			ShpSetLayer(&shp->s, LAYER_XLU_SURF);
			gSPDisplayList(g++, gfx_inside_0702A880);
			gSPEndDisplayList(g);
		}
	}
	return gfx;
}

s8 objshape_803612F0;
static s16 objshape_803312F0 = 1;
static s16 objshape_803312F4 = 0;
static s16 objshape_803312F8 = 0;

/* RR carpet */
void *Ctrl_objshape_802D2470(int code, UNUSED SHAPE *shape, UNUSED void *data)
{
	if (code != SC_DRAW)
	{
		objshape_803312F8 = 0;
		objshape_803312F4 = draw_timer - 1;
		objshape_803312F0 = draw_timer;
		objshape_803612F0 = 0;
	}
	else
	{
		objshape_803312F4 = objshape_803312F0;
		objshape_803312F0 = draw_timer;
		if (objshape_803312F4 != objshape_803312F0)
		{
			objshape_803312F8 += 0x400;
		}
	}
	return NULL;
}

/* RR carpet */
extern short rr_07019080[];
extern Gfx gfx_rr_07019128[];
extern Gfx gfx_rr_07019198[];
extern Gfx gfx_rr_07019200[];
void *Ctrl_objshape_802D2520(int code, SHAPE *shape, UNUSED void *data)
{
	SHORT i;
	SHORT a, b, x, y, z, s, t;
	Vtx *vtx;
	SCALLBACK *shp = (SCALLBACK *)shape;
	short *info = SegmentToVirtual(rr_07019080);
	Gfx *gfx = NULL, *g = NULL;
	OBJECT *obj;
	if (code == SC_DRAW)
	{
		vtx = GfxAlloc(sizeof(Vtx)*21);
		g = gfx = GfxAlloc(sizeof(Gfx)*7);
		if (!vtx || !gfx) return NULL;
		ShpSetLayer(&shp->s, LAYER_OPA_SURF);
		for (i = 0; i < 21; i++)
		{
			a = i / 3;
			b = i % 3;
			x = info[4*i+0];
			y = RoundFtoS(SIN(objshape_803312F8 + 0x1000*a + 0x4000*b) * 20.0);
			z = info[4*i+1];
			s = info[4*i+2];
			t = info[4*i+3];
			VtxSet(vtx, i, x, y, z, s, t, 0, 127, 0, 0xFF);
		}
		gSPDisplayList(g++, gfx_rr_07019128);
		gSPVertex(g++, &vtx[0], 12, 0);
		gSPDisplayList(g++, gfx_rr_07019198);
		gSPVertex(g++, &vtx[9], 12, 0);
		gSPDisplayList(g++, gfx_rr_07019198);
		gSPDisplayList(g++, gfx_rr_07019200);
		gSPEndDisplayList(g);
		obj = (OBJECT *)draw_object;
		if (mario_obj->ride == obj) objshape_803612F0 = 2;
		else if (obj->o_velf != 0.0) objshape_803612F0 = 1;
		else objshape_803612F0 = 0;
	}
	return gfx;
}

extern Gfx gfx_wipe_start[];
extern Gfx gfx_ending[];
void *EndingDraw(int code, SHAPE *shape, UNUSED void *data)
{
	SCALLBACK *shp = (SCALLBACK *)shape;
	Gfx *gfx = NULL, *g = NULL;
	if (code == SC_DRAW)
	{
		g = gfx = GfxAlloc(sizeof(Gfx)*3);
		ShpSetLayer(&shp->s, LAYER_OPA_SURF);
		gSPDisplayList(g++, gfx_wipe_start);
		gSPDisplayList(g++, gfx_ending);
		gSPEndDisplayList(g);
	}
	return gfx;
}
