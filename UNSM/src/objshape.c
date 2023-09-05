#include <sm64.h>

void vtx_set(
	Vtx *vtx, int i,
	SHORT x, SHORT y, SHORT z,
	SHORT s, SHORT t,
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

SHORT roundftos(float x)
{
	if (x >= (DOUBLE)0) return x + (DOUBLE)0.5F;
	else return x - (DOUBLE)0.5F;
}

/* TotWC entry */
extern Gfx gfx_inside_0702A880[];
void *s_obj_shape_802D2360(int code, SHAPE *shape, UNUSED void *data)
{
	u32 flag;
	S_CALLBACK *shp;
	Gfx *g = NULL;
	Gfx *gfx = NULL;
	if (code == S_CODE_DRAW)
	{
		flag = save_flag_get();
		if (hud.star >= 10 && !(flag & SAVE_000002))
		{
			if (!(gfx = gfx_alloc(sizeof(Gfx)*2))) return NULL;
			else g = gfx;
			shp = (S_CALLBACK *)shape;
			shape_layer_set(&shp->s, LAYER_XLU_SURF);
			gSPDisplayList(g++, gfx_inside_0702A880);
			gSPEndDisplayList(g);
		}
	}
	return gfx;
}

s8 obj_shape_803612F0;
static s16 obj_shape_803312F0 = 1;
static s16 obj_shape_803312F4 = 0;
static s16 obj_shape_803312F8 = 0;

/* RR carpet */
void *s_obj_shape_802D2470(int code, UNUSED SHAPE *shape, UNUSED void *data)
{
	if (code != S_CODE_DRAW)
	{
		obj_shape_803312F8 = 0;
		obj_shape_803312F4 = draw_timer - 1;
		obj_shape_803312F0 = draw_timer;
		obj_shape_803612F0 = 0;
	}
	else
	{
		obj_shape_803312F4 = obj_shape_803312F0;
		obj_shape_803312F0 = draw_timer;
		if (obj_shape_803312F4 != obj_shape_803312F0)
		{
			obj_shape_803312F8 += 0x400;
		}
	}
	return NULL;
}

/* RR carpet */
extern short rr_07019080[];
extern Gfx gfx_rr_07019128[];
extern Gfx gfx_rr_07019198[];
extern Gfx gfx_rr_07019200[];
void *s_obj_shape_802D2520(int code, SHAPE *shape, UNUSED void *data)
{
	SHORT i;
	SHORT a, b, x, y, z, s, t;
	Vtx *vtx;
	S_CALLBACK *shp = (S_CALLBACK *)shape;
	short *info = segment_to_virtual(rr_07019080);
	Gfx *gfx = NULL;
	Gfx *g = NULL;
	OBJECT *obj;
	if (code == S_CODE_DRAW)
	{
		vtx = gfx_alloc(sizeof(Vtx)*21);
		g = gfx = gfx_alloc(sizeof(Gfx)*7);
		if (!vtx || !gfx) return NULL;
		shape_layer_set(&shp->s, LAYER_OPA_SURF);
		for (i = 0; i < 21; i++)
		{
			a = i / 3;
			b = i % 3;
			x = info[4*i+0];
			y = roundftos(
				sin(obj_shape_803312F8 + 0x1000*a + 0x4000*b) * (DOUBLE)20
			);
			z = info[4*i+1];
			s = info[4*i+2];
			t = info[4*i+3];
			vtx_set(vtx, i, x, y, z, s, t, 0, 127, 0, 0xFF);
		}
		gSPDisplayList(g++, gfx_rr_07019128);
		gSPVertex(g++, &vtx[0], 12, 0);
		gSPDisplayList(g++, gfx_rr_07019198);
		gSPVertex(g++, &vtx[9], 12, 0);
		gSPDisplayList(g++, gfx_rr_07019198);
		gSPDisplayList(g++, gfx_rr_07019200);
		gSPEndDisplayList(g);
		obj = (OBJECT *)s_object;
		if (obj_mario->obj_ground == obj) obj_shape_803612F0 = 2;
		else if (obj->o_vel_f != (DOUBLE)0) obj_shape_803612F0 = 1;
		else obj_shape_803612F0 = 0;
	}
	return gfx;
}

/* Ending */
extern Gfx gfx_wipe_start[];
extern Gfx gfx_ending[];
void *s_obj_shape_802D28CC(int code, SHAPE *shape, UNUSED void *data)
{
	S_CALLBACK *shp = (S_CALLBACK *)shape;
	Gfx *gfx = NULL;
	Gfx *g = NULL;
	if (code == S_CODE_DRAW)
	{
		g = gfx = gfx_alloc(sizeof(Gfx)*3);
		shape_layer_set(&shp->s, LAYER_OPA_SURF);
		gSPDisplayList(g++, gfx_wipe_start);
		gSPDisplayList(g++, gfx_ending);
		gSPEndDisplayList(g);
	}
	return gfx;
}
