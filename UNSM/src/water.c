#include <sm64.h>

typedef struct fluidinfo
{
	unsigned long code;
	int txt;
	int n;
	short *data;
	Gfx *begin;
	Gfx *end;
	Gfx *draw;
	u8 r;
	u8 g;
	u8 b;
	u8 alpha;
	int layer;
}
FLUIDINFO;

static short water_txt;
static short water_timer = 1;
static short water_stamp = 0;
static char water_color = 0;

float pool_entry = 0;
static int pool_flag = FALSE;

extern u16 txt_water_0[];
extern u16 txt_water_1[];
extern u16 txt_water_2[];
extern u16 txt_mist[];
extern u16 txt_lava[];
extern u16 txt_ssl_07001000[];
extern u16 txt_ssl_07004018[];
extern u16 txt_ttc_07015F90[];

static u16 *txt_water[] =
{
	txt_water_0,
	txt_mist,
	txt_water_1,
	txt_water_2,
	txt_lava,
	txt_ssl_07004018,
	txt_ssl_07001000,
	txt_ttc_07015F90,
};

extern Gfx gfx_water_rgba[];
extern Gfx gfx_water_ia[];
extern Gfx gfx_water_end[];

extern Gfx gfx_ssl_07004818[];
extern Gfx gfx_ssl_07004860[];
extern Gfx gfx_ssl_07004880[];
extern Gfx gfx_ssl_070048F8[];
extern Gfx gfx_ssl_07004A38[];
extern Gfx gfx_ssl_070127E0[];
extern Gfx gfx_ssl_070127E8[];
extern Gfx gfx_ssl_070128B8[];
extern Gfx gfx_ssl_07012A08[];
extern Gfx gfx_ssl_07012B48[];
extern Gfx gfx_ssl_070285F0[];
extern Gfx gfx_ssl_07028660[];
extern Gfx gfx_ssl_070286A0[];
extern Gfx gfx_ssl_07028718[];
extern Gfx gfx_ssl_070287B8[];
extern Gfx gfx_ssl_07028888[];
extern Gfx gfx_ttc_07016790[];
extern Gfx gfx_ttc_07016808[];
extern Gfx gfx_ttc_070169C8[];
extern Gfx gfx_grounds_070117E8[];
extern Gfx gfx_bitfs_07015BA8[];
extern Gfx gfx_bitfs_07015BC0[];
extern Gfx gfx_lll_07028718[];
extern Gfx gfx_lll_07028838[];
extern Gfx gfx_cotmc_0700BE10[];
extern Gfx gfx_cotmc_0700BE88[];
extern Gfx gfx_cotmc_0700BF60[];
extern Gfx gfx_ttm_07017260[];
extern Gfx gfx_ttm_07017288[];
extern Gfx gfx_ttm_070172A0[];

extern short fluid_0801S[];
extern short fluid_0802S[];
extern short fluid_0801L[];
extern short fluid_0802L[];
extern short fluid_0803L[];
extern short fluid_0801[];
extern short fluid_0802[];
extern short fluid_0803[];
extern short fluid_1400L[];
extern short fluid_1401L[];
extern short fluid_1601[];
extern short fluid_1901[];
extern short fluid_1902[];
extern short fluid_1903[];
extern short fluid_2201[];
extern short fluid_2202[];
extern short fluid_2801[];
extern short fluid_3601[];
extern short fluid_3603[];
extern short fluid_3602[];
extern short fluid_3604[];
extern short fluid_3605[];

static FLUIDINFO fluidtab[] =
{
	{0x0801, 6,  8, fluid_0801, gfx_ssl_070286A0, gfx_ssl_07028718, gfx_ssl_070287B8, 0xFF, 0xFF, 0xFF, 0xFF, LAYER_XLU_INTER},
	{0x0802, 6,  8, fluid_0802, gfx_ssl_070285F0, gfx_ssl_07028660, gfx_ssl_070287B8, 0xFF, 0xFF, 0xFF, 0xFF, LAYER_OPA_INTER},
	{0x0803, 6,  6, fluid_0803, gfx_ssl_070286A0, gfx_ssl_07028718, gfx_ssl_07028888, 0xFF, 0xFF, 0xFF, 0xFF, LAYER_XLU_INTER},
	{0x1601, 0, 15, fluid_1601, gfx_water_rgba, gfx_water_end, gfx_grounds_070117E8, 0xFF, 0xFF, 0xFF, 0xB4, LAYER_XLU_INTER},
	{0x1901, 4,  4, fluid_1901, gfx_water_rgba, gfx_water_end, gfx_bitfs_07015BA8, 0xFF, 0xFF, 0xFF, 0xFF, LAYER_OPA_SURF},
	{0x1902, 4,  4, fluid_1902, gfx_water_rgba, gfx_water_end, gfx_bitfs_07015BA8, 0xFF, 0xFF, 0xFF, 0xB4, LAYER_XLU_SURF},
	{0x1903, 4,  9, fluid_1903, gfx_water_rgba, gfx_water_end, gfx_bitfs_07015BC0, 0xFF, 0xFF, 0xFF, 0xB4, LAYER_XLU_SURF},
	{0x2201, 4,  9, fluid_2201, gfx_water_rgba, gfx_water_end, gfx_lll_07028718, 0xFF, 0xFF, 0xFF, 0xC8, LAYER_XLU_SURF},
	{0x2202, 4, 16, fluid_2202, gfx_water_rgba, gfx_water_end, gfx_lll_07028838, 0xFF, 0xFF, 0xFF, 0xB4, LAYER_XLU_INTER},
	{0x2801, 0, 14, fluid_2801, gfx_cotmc_0700BE10, gfx_cotmc_0700BE88, gfx_cotmc_0700BF60, 0xFF, 0xFF, 0xFF, 0xB4, LAYER_XLU_INTER},
	{0x3601, 0,  6, fluid_3601, gfx_water_rgba, gfx_water_end, gfx_ttm_07017260, 0xFF, 0xFF, 0xFF, 0xB4, LAYER_XLU_SURF},
	{0x3602, 0,  6, fluid_3602, gfx_water_rgba, gfx_water_end, gfx_ttm_07017260, 0xFF, 0xFF, 0xFF, 0xB4, LAYER_XLU_SURF},
	{0x3603, 0,  4, fluid_3603, gfx_water_rgba, gfx_water_end, gfx_ttm_07017288, 0xFF, 0xFF, 0xFF, 0xB4, LAYER_XLU_INTER},
	{0x3604, 0,  4, fluid_3604, gfx_water_rgba, gfx_water_end, gfx_ttm_07017288, 0xFF, 0xFF, 0xFF, 0xB4, LAYER_XLU_INTER},
	{0x3605, 0,  8, fluid_3605, gfx_water_rgba, gfx_water_end, gfx_ttm_070172A0, 0xFF, 0xFF, 0xFF, 0xB4, LAYER_XLU_INTER},
	{0},
};

static FLUIDINFO fluidtabL[] =
{
	{0x0801, 5, 12, fluid_0801L, gfx_ssl_070127E0, gfx_ssl_070127E8, gfx_ssl_070128B8, 0xFF, 0xFF, 0xFF, 0xFF, LAYER_OPA_SURF},
	{0x0802, 5, 16, fluid_0802L, gfx_ssl_070127E0, gfx_ssl_070127E8, gfx_ssl_07012A08, 0xFF, 0xFF, 0xFF, 0xFF, LAYER_OPA_SURF},
	{0x0803, 5, 15, fluid_0803L, gfx_ssl_070127E0, gfx_ssl_070127E8, gfx_ssl_07012B48, 0xFF, 0xFF, 0xFF, 0xFF, LAYER_OPA_SURF},
	{0x1400, 7, 12, fluid_1400L, gfx_ttc_07016790, gfx_ttc_07016808, gfx_ttc_070169C8, 0xFF, 0xFF, 0xFF, 0xFF, LAYER_OPA_SURF},
	{0x1401, 7, 12, fluid_1401L, gfx_ttc_07016790, gfx_ttc_07016808, gfx_ttc_070169C8, 0xFF, 0xFF, 0xFF, 0xFF, LAYER_OPA_SURF},
	{0},
};

static FLUIDINFO fluidtabS[] =
{
	{0x0801, 5,  8, fluid_0801S, gfx_ssl_07004818, gfx_ssl_07004860, gfx_ssl_07004A38, 0xFF, 0xFF, 0xFF, 0xFF, LAYER_OPA_SURF},
	{0x0802, 6,  8, fluid_0802S, gfx_ssl_07004880, gfx_ssl_070048F8, gfx_ssl_07004A38, 0xFF, 0xFF, 0xFF, 0xFF, LAYER_OPA_SURF},
	{0},
};

void *CtrlPoolLevel(int code, UNUSED SHAPE *shape, UNUSED void *data)
{
	int i;
	UNUSED STATIC short leveltab[] = {256, 1024, 1792, 2560};
	if (code != SC_DRAW)
	{
		pool_flag = FALSE;
	}
	else if (code == SC_DRAW)
	{
		if (waterp && !pool_flag)
		{
			SHORT level;
			if      (pool_entry <= 1382.4)  level = 31;
			else if (pool_entry >= 1600.0)  level = 2816;
			else                            level = 1024;
			for (i = 0; i < waterp[0]; i++) waterp[1+6*i+5] = level;
			pool_flag = TRUE;
		}
	}
	return NULL;
}

void *CtrlWaterProc(int code, UNUSED SHAPE *shape, UNUSED void *data)
{
	if (code != SC_DRAW)
	{
		water_stamp = draw_timer-1;
		water_timer = draw_timer;
	}
	else
	{
		water_stamp = water_timer;
		water_timer = draw_timer;
	}
	return NULL;
}

static void WaterSetVtx(
	Vtx *vtx, int i, SHORT x, SHORT y, SHORT z, SHORT ang, SHORT off,
	float scale, UCHAR alpha
)
{
	SHORT s = 32.0 * (32.0*scale-1) * SIN(ang+off);
	SHORT t = 32.0 * (32.0*scale-1) * COS(ang+off);
	if (water_color == 1)
	{
		VtxSet(vtx, i, x, y, z, s, t, 0xFF, 0xFF, 0x00, alpha);
	}
	else if (water_color == 2)
	{
		VtxSet(vtx, i, x, y, z, s, t, 0xFF, 0x00, 0x00, alpha);
	}
	else
	{
		VtxSet(vtx, i, x, y, z, s, t, 0xFF, 0xFF, 0xFF, alpha);
	}
}

extern Gfx gfx_quad0[];

static Gfx *WaterDrawPlane(SHORT y, short *plane)
{
	SHORT ang;
	SHORT angvel = plane[1+0];
	SHORT scale = plane[1+1];
	SHORT x0 = plane[1+2];
	SHORT z0 = plane[1+3];
	SHORT x1 = plane[1+4];
	SHORT z1 = plane[1+5];
	SHORT x2 = plane[1+6];
	SHORT z2 = plane[1+7];
	SHORT x3 = plane[1+8];
	SHORT z3 = plane[1+9];
	SHORT order = plane[1+10];
	SHORT alpha = plane[1+11];
	SHORT txt = plane[1+12];
	Vtx *vtx = GfxAlloc(sizeof(Vtx)*4);
	Gfx *gfx, *g;
	if (txt == water_txt)   gfx = GfxAlloc(sizeof(Gfx)*(  3));
	else                    gfx = GfxAlloc(sizeof(Gfx)*(5+3));
	if (!gfx || !vtx) return NULL;
	g = gfx;
	if (water_timer != water_stamp) plane[0] += angvel;
	ang = plane[0];
	if (order == 0)
	{
		WaterSetVtx(vtx, 0, x0, y, z0, ang, (short)0x0000, scale, alpha);
		WaterSetVtx(vtx, 1, x1, y, z1, ang, (short)0x4000, scale, alpha);
		WaterSetVtx(vtx, 2, x2, y, z2, ang, (short)0x8000, scale, alpha);
		WaterSetVtx(vtx, 3, x3, y, z3, ang, (short)0xC000, scale, alpha);
	}
	else
	{
		WaterSetVtx(vtx, 0, x0, y, z0, ang, (short)0x0000, scale, alpha);
		WaterSetVtx(vtx, 1, x1, y, z1, ang, (short)0xC000, scale, alpha);
		WaterSetVtx(vtx, 2, x2, y, z2, ang, (short)0x8000, scale, alpha);
		WaterSetVtx(vtx, 3, x3, y, z3, ang, (short)0x4000, scale, alpha);
	}
	if (txt != water_txt)
	{
		switch (txt)
		{
		case 1:
			gDPLoadImageBlockT(
				g++, txt_water[txt], G_IM_FMT_IA, G_IM_SIZ_16b, 32, 32
			);
			break;
		default:
			gDPLoadImageBlockT(
				g++, txt_water[txt], G_IM_FMT_RGBA, G_IM_SIZ_16b, 32, 32
			);
			break;
		}
		water_txt = txt;
	}
	gSPVertex(g++, OS_K0_TO_PHYSICAL(vtx), 4, 0);
	gSPDisplayList(g++, gfx_quad0);
	gSPEndDisplayList(g);
	return gfx;
}

static Gfx *WaterDraw(SHORT y, short *data)
{
	short *planedata = SegmentToVirtual(data);
	SHORT n = planedata[0];
	Gfx *gfx, *g = gfx = GfxAlloc(sizeof(Gfx)*(n+1));
	Gfx *planegfx;
	int i;
	if (!gfx) return NULL;
	for (i = 0; i < n; i++)
	{
		if ((planegfx = WaterDrawPlane(y, &planedata[1+14*i])))
		{
			gSPDisplayList(g++, K0_TO_PHYS(planegfx));
		}
	}
	gSPEndDisplayList(g);
	return gfx;
}

static void *WaterGfx(SHORT code, SHORT y, WATERINFO *info)
{
	WATERINFO *wi = SegmentToVirtual(info);
	int i = 0;
	while (wi[i].code != -1)
	{
		if (wi[i].code == code) return WaterDraw(y, wi[i].data);
		i++;
	}
	return NULL;
}

extern WATERINFO water_0400;
extern WATERINFO water_0401;
extern WATERINFO water_0501;
extern WATERINFO water_0600;
extern WATERINFO water_0612;
extern WATERINFO water_0701;
extern WATERINFO water_0702;
extern WATERINFO water_0801;
extern WATERINFO water_0851;
extern WATERINFO water_1001;
extern WATERINFO water_1101;
extern WATERINFO water_1102;
extern WATERINFO water_1201;
extern WATERINFO water_1205;
extern WATERINFO water_1202;
extern WATERINFO water_1301;
extern WATERINFO water_1302;
extern WATERINFO water_1601;
extern WATERINFO water_2202;
extern WATERINFO water_2301;
extern WATERINFO water_2302;
extern WATERINFO water_2401;
extern WATERINFO water_2601;
extern WATERINFO water_3601;

static WATERINFO *WaterGetInfo(unsigned int code)
{
	switch (code)
	{
	case 0x0400: return &water_0400;
	case 0x0401: return &water_0401;
	case 0x0501: return &water_0501;
	case 0x0600: return &water_0600;
	case 0x0612: return &water_0612;
	case 0x0701: return &water_0701;
	case 0x0702: return &water_0702;
	case 0x0801: return &water_0801;
	case 0x0851: return &water_0851;
	case 0x1001: return &water_1001;
	case 0x1101: return &water_1101;
	case 0x1102: return &water_1102;
	case 0x1201: return &water_1201;
	case 0x1205: return &water_1205;
	case 0x1202: return &water_1202;
	case 0x1301: return &water_1301;
	case 0x1302: return &water_1302;
	case 0x1601: return &water_1601;
	case 0x2202: return &water_2202;
	case 0x2301: return &water_2301;
	case 0x2302: return &water_2302;
	case 0x2401: return &water_2401;
	case 0x2601: return &water_2601;
	case 0x3601: return &water_3601;
	}
	return NULL;
}

static void WaterGfxBegin(unsigned int code, Gfx **g)
{
	switch (code)
	{
	case 0x0702:    gSPDisplayList((*g)++, gfx_water_ia);   break;
	case 0x0851:    gSPDisplayList((*g)++, gfx_water_ia);   break;
	case 0x1205:    gSPDisplayList((*g)++, gfx_water_ia);   break;
	default:        gSPDisplayList((*g)++, gfx_water_rgba); break;
	}
}

void *CtrlWaterDraw(int code, SHAPE *shape, UNUSED void *data)
{
	Gfx *gfx = NULL, *g = NULL;
	if (code == SC_DRAW)
	{
		Gfx *watergfx;
		WATERINFO *info;
		SCALLBACK *shp;
		SHORT n, c, y;
		int i;
		water_color = 0;
		if (!waterp) return NULL;
		n = waterp[0];
		if (!(gfx = GfxAlloc(sizeof(Gfx)*(1+n+2)))) return NULL;
		else g = gfx;
		shp = (SCALLBACK *)shape;
		if (shp->arg == 0x1205)
		{
			if (camdata._24[1] < 1024.0) return NULL;
			if (BuGetStar(COURSE_JRB-1) & 1) return NULL;
		}
		else if (shp->arg == 0x0702)
		{
			water_color = 1;
		}
		else if (shp->arg == 0x0851)
		{
			water_color = 2;
		}
		if (!(info = WaterGetInfo(shp->arg))) return NULL;
		ShpSetLayer(&shp->s, LAYER_XLU_INTER);
		WaterGfxBegin(shp->arg, &g);
		water_txt = -1;
		for (i = 0; i < n; i++)
		{
			c = waterp[1+6*i+0];
			y = waterp[1+6*i+5];
			if ((watergfx = WaterGfx(c, y, info)))
			{
				gSPDisplayList(g++, K0_TO_PHYS(watergfx));
			}
		}
		gSPDisplayList(g++, gfx_water_end);
		gSPEndDisplayList(g);
	}
	return gfx;
}

static void FluidProc(short *data, int i)
{
	SHORT speed = data[0];
	short *coord = &data[i];
	if (water_timer != water_stamp)
	{
		*coord += speed;
		if (*coord >= +32*32) *coord -= 32*32;
		if (*coord <= -32*32) *coord += 32*32;
	}
}

static void FluidSetVtx0(Vtx *vtx, short *data, FLUIDINFO *info, CHAR type)
{
	SHORT x = data[1+0];
	SHORT y = data[1+1];
	SHORT z = data[1+2];
	UCHAR a = info->alpha;
	UCHAR r, g, b;
	CHAR nx, ny, nz;
	SHORT s, t;
	switch (type)
	{
	case 0:
		r = info->r;
		g = info->g;
		b = info->b;
		s = data[1+3];
		t = data[1+4];
		VtxSet(vtx, 0, x, y, z, s, t, r, g, b, a);
		break;
	case 1:
		nx = data[1+3];
		ny = data[1+4];
		nz = data[1+5];
		s = data[1+6];
		t = data[1+7];
		VtxSet(vtx, 0, x, y, z, s, t, nx, ny, nz, a);
		break;
	}
}

static void FluidSetVtxN(
	Vtx *vtx, int i, short *data, FLUIDINFO *info, CHAR type
)
{
	UCHAR a = info->alpha;
	SHORT x, y, z, s0, s1, s, t, tx, ty;
	UCHAR r, g, b;
	CHAR nx, ny, nz;
	switch (type)
	{
	case 0:
		x = data[1+5*i+0];
		y = data[1+5*i+1];
		z = data[1+5*i+2];
		s0 = data[1+5*0+3];
		s1 = data[1+5*0+4];
		tx = data[1+5*i+3];
		ty = data[1+5*i+4];
		s = s0 + ((32*tx) << 5);
		t = s1 + ((32*ty) << 5);
		r = info->r;
		g = info->g;
		b = info->b;
		VtxSet(vtx, i, x, y, z, s, t, r, g, b, a);
		break;
	case 1:
		x = data[1+8*i+0];
		y = data[1+8*i+1];
		z = data[1+8*i+2];
		s0 = data[1+8*0+6];
		s1 = data[1+8*0+7];
		tx = data[1+8*i+6];
		ty = data[1+8*i+7];
		s = s0 + ((32*tx) << 5);
		t = s1 + ((32*ty) << 5);
		nx = data[1+8*i+3];
		ny = data[1+8*i+4];
		nz = data[1+8*i+5];
		VtxSet(vtx, i, x, y, z, s, t, nx, ny, nz, a);
		break;
	}
}

static Gfx *FluidGfx(short *data, FLUIDINFO *info, CHAR type)
{
	Vtx *vtx = GfxAlloc(sizeof(Vtx)*info->n);
	Gfx *gfx, *g = gfx = GfxAlloc(sizeof(Gfx)*11);
	int i;
	if (!vtx || !gfx) return NULL;
	FluidSetVtx0(vtx, data, info, type);
	for (i = 1; i < info->n; i++) FluidSetVtxN(vtx, i, data, info, type);
	gSPDisplayList(g++, info->begin);
	gDPLoadImageBlockT(
		g++, txt_water[info->txt], G_IM_FMT_RGBA, G_IM_SIZ_16b, 32, 32
	);
	gSPVertex(g++, OS_K0_TO_PHYSICAL(vtx), info->n, 0);
	gSPDisplayList(g++, info->draw);
	gSPDisplayList(g++, info->end);
	gSPEndDisplayList(g);
	return gfx;
}

void *CtrlFluid(int code, SHAPE *shape, UNUSED void *data)
{
	int i;
	short *fluid;
	SCALLBACK *shp;
	Gfx *gfx = NULL;
	if (code == SC_DRAW)
	{
		i = 0;
		shp = (SCALLBACK *)shape;
		while (fluidtab[i].data)
		{
			if (fluidtab[i].code == shp->arg)
			{
				ShpSetLayer(&shp->s, fluidtab[i].layer);
				fluid = SegmentToVirtual(fluidtab[i].data);
				FluidProc(fluid, 4);
				gfx = FluidGfx(fluid, &fluidtab[i], 0);
				break;
			}
			i++;
		}
	}
	return gfx;
}

void *CtrlFluidL(int code, SHAPE *shape, UNUSED void *data)
{
	int i;
	short *fluid;
	SCALLBACK *shp;
	Gfx *gfx = NULL;
	if (code == SC_DRAW)
	{
		i = 0;
		shp = (SCALLBACK *)shape;
		while (fluidtabL[i].data)
		{
			if (fluidtabL[i].code == shp->arg)
			{
				ShpSetLayer(&shp->s, fluidtabL[i].layer);
				fluid = SegmentToVirtual(fluidtabL[i].data);
				FluidProc(fluid, 7);
				gfx = FluidGfx(fluid, &fluidtabL[i], 1);
				break;
			}
			i++;
		}
	}
	return gfx;
}

void *CtrlFluidDrawL(int code, SHAPE *shape, UNUSED void *data)
{
	int i;
	short *fluid;
	SCALLBACK *shp;
	Gfx *gfx = NULL;
	if (code == SC_DRAW)
	{
		i = 0;
		shp = (SCALLBACK *)shape;
		while (fluidtabL[i].data)
		{
			if (fluidtabL[i].code == shp->arg)
			{
				ShpSetLayer(&shp->s, fluidtabL[i].layer);
				fluid = SegmentToVirtual(fluidtabL[i].data);
				gfx = FluidGfx(fluid, &fluidtabL[i], 1);
				break;
			}
			i++;
		}
	}
	return gfx;
}

void *CtrlFluidDrawS(int code, SHAPE *shape, UNUSED void *data)
{
	int i;
	short *fluid;
	SCALLBACK *shp;
	Gfx *gfx = NULL;
	if (code == SC_DRAW)
	{
		i = 0;
		shp = (SCALLBACK *)shape;
		while (fluidtabS[i].data)
		{
			if (fluidtabS[i].code == shp->arg)
			{
				ShpSetLayer(&shp->s, fluidtabS[i].layer);
				fluid = SegmentToVirtual(fluidtabS[i].data);
				gfx = FluidGfx(fluid, &fluidtabS[i], 1);
				break;
			}
			i++;
		}
	}
	return gfx;
}

void *CtrlFluidProc(int code, SHAPE *shape, UNUSED void *data)
{
	if (code == SC_DRAW)
	{
		short *fluid;
		SCALLBACK *shp = (SCALLBACK *)shape;
		switch (shp->arg)
		{
		case 0x0801: fluid = SegmentToVirtual(fluid_0801S); break;
		case 0x0802: fluid = SegmentToVirtual(fluid_0802S); break;
		case 0x1400: fluid = SegmentToVirtual(fluid_1400L); break;
		case 0x1401: fluid = SegmentToVirtual(fluid_1401L); break;
#ifdef __GNUC__
		default: __builtin_unreachable();
#endif
		}
		FluidProc(fluid, 7);
	}
	return NULL;
}
