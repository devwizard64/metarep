#include <sm64.h>

extern u16 *txt_weather_flower[];
extern u16 *txt_weather_lava[];
extern u16 *txt_weather_bubble[];
extern Gfx gfx_weather_end[];
extern Gfx gfx_lava_start[];
extern Gfx gfx_lava_txt[];

UNUSED static char lava_803317A0 = 0;

short lava_info[10];

static Gfx *lava_glistp;
static int lava_max;
static int lava_len;

static int LavaIsVisible(int i, int x, int z, int radius)
{
	int posx = (weatherp+i)->x;
	int posz = (weatherp+i)->z;
	if (SQUARE(posx-x)+SQUARE(posz-z) > SQUARE(radius)) return FALSE;
	return TRUE;
}

static int FlowerRand(void)
{
	int x = 2000*RandF() - 1000;
	if (x < 0)  x -= 1000;
	else        x += 1000;
	return x;
}

static void LavaMakeFlower(SVEC pos)
{
	int i;
	PLANE *plane;
	unsigned int frame = gfx_frame;
	short x = pos[0];
	UNUSED short y = pos[1];
	short z = pos[2];
	for (i = 0; i < lava_len; i++)
	{
		(weatherp+i)->flag = LavaIsVisible(i, x, z, 3000);
		if (!(weatherp+i)->flag)
		{
			(weatherp+i)->x = FlowerRand() + x;
			(weatherp+i)->z = FlowerRand() + z;
			(weatherp+i)->y =
				BGCheckPlane((weatherp+i)->x, 10000, (weatherp+i)->z, &plane);
			(weatherp+i)->flag = TRUE;
			(weatherp+i)->frame = 5*RandF();
		}
		else if (!(frame & 3))
		{
			(weatherp+i)->frame += 1;
			if ((weatherp+i)->frame >= 6) (weatherp+i)->frame = 0;
		}
	}
}

static void LavaNew(int i, SVEC pos)
{
	BGFACE *ground;
	SHORT ground_y;
	short x = pos[0];
	short y = pos[1];
	short z = pos[2];
	(weatherp+i)->x = 6000*RandF()-3000 + x;
	(weatherp+i)->z = 6000*RandF()-3000 + z;
	if ((weatherp+i)->x > +8000) (weatherp+i)->x = +16000 - (weatherp+i)->x;
	if ((weatherp+i)->x < -8000) (weatherp+i)->x = -16000 - (weatherp+i)->x;
	if ((weatherp+i)->z > +8000) (weatherp+i)->z = +16000 - (weatherp+i)->z;
	if ((weatherp+i)->z < -8000) (weatherp+i)->z = -16000 - (weatherp+i)->z;
	ground_y = BGCheckGround((weatherp+i)->x, y+500, (weatherp+i)->z, &ground);
	if (!ground)
	{
		(weatherp+i)->y = -10000;
		return;
	}
	if (ground->code == BG_1)   (weatherp+i)->y = ground_y;
	else                        (weatherp+i)->y = -10000;
}

static void LavaMakeLava(SVEC pos)
{
	int i;
	unsigned int frame = gfx_frame;
	CHAR r;
	UNUSED short x = pos[0];
	UNUSED short y = pos[1];
	UNUSED short z = pos[2];
	for (i = 0; i < lava_len; i++)
	{
		if (!(weatherp+i)->flag)
		{
			LavaNew(i, pos);
			(weatherp+i)->flag = TRUE;
		}
		else if (!(frame & 1))
		{
			(weatherp+i)->frame += 1;
			if ((weatherp+i)->frame >= 9)
			{
				(weatherp+i)->flag = FALSE;
				(weatherp+i)->frame = 0;
			}
		}
	}
	if ((r = 16*RandF()) == 8) Na_FixSePlay(0x300D0081);
}

static void WhirlpoolMove(int *x, int *y, int *z)
{
	int dx = *x - lava_info[4];
	int dy = *y - lava_info[5];
	int dz = *z - lava_info[6];
	float cx = COS( lava_info[8]);
	float sx = SIN( lava_info[8]);
	float cy = COS(-lava_info[9]);
	float sy = SIN(-lava_info[9]);
	float posx = cy*dx - sy*cx*dy - sx*sy*dz;
	float posy = sy*dx + cx*cy*dy - sx*cy*dz;
	float posz =            sx*dy +    cx*dz;
	*x = lava_info[4] + (int)posx;
	*y = lava_info[5] + (int)posy;
	*z = lava_info[6] + (int)posz;
}

static int WhirlpoolIsVisible(int i)
{
	UNUSED int n;
	if ((weatherp+i)->work[3] < lava_info[5]-100) return FALSE;
	if ((weatherp+i)->work[1] < 10) return FALSE;
	return TRUE;
}

static void LavaMakeWhirlpool(void)
{
	int i;
	for (i = 0; i < lava_len; i++)
	{
		(weatherp+i)->flag = WhirlpoolIsVisible(i);
		if (!(weatherp+i)->flag)
		{
			(weatherp+i)->work[1] = 1000*RandF();
			(weatherp+i)->work[0] = 0x10000*RandF();
			(weatherp+i)->x =
				lava_info[1] + SIN((weatherp+i)->work[0])*(weatherp+i)->work[1];
			(weatherp+i)->z =
				lava_info[3] + COS((weatherp+i)->work[0])*(weatherp+i)->work[1];
			(weatherp+i)->work[3] = lava_info[2] + (100*RandF()-50);
			(weatherp+i)->y = (weatherp+i)->work[3];
			(weatherp+i)->work[2] = 0;
			(weatherp+i)->flag = TRUE;
			WhirlpoolMove(
				&(weatherp+i)->x, &(weatherp+i)->y, &(weatherp+i)->z
			);
		}
		else
		{
			(weatherp+i)->work[1] -= 40;
			(weatherp+i)->work[0] +=
				0x400 + (short)(3000 - 2*(weatherp+i)->work[1]);
			(weatherp+i)->x =
				lava_info[1] + SIN((weatherp+i)->work[0])*(weatherp+i)->work[1];
			(weatherp+i)->z =
				lava_info[3] + COS((weatherp+i)->work[0])*(weatherp+i)->work[1];
			(weatherp+i)->work[3] -= 40 - (short)(weatherp+i)->work[1]/100;
			(weatherp+i)->y = (weatherp+i)->work[3];
			WhirlpoolMove(
				&(weatherp+i)->x, &(weatherp+i)->y, &(weatherp+i)->z
			);
		}
	}
}

static int JetIsVisible(int i)
{
	UNUSED int n;
	if (
		!LavaIsVisible(i, lava_info[1], lava_info[3], 1000) ||
		lava_info[2]+1500 < (weatherp+i)->y
	) return FALSE;
	return TRUE;
}

static void LavaMakeJet(void)
{
	int i;
	for (i = 0; i < lava_len; i++)
	{
		(weatherp+i)->flag = JetIsVisible(i);
		if (!(weatherp+i)->flag)
		{
			(weatherp+i)->work[1] = 300*RandF();
			(weatherp+i)->work[0] = Rand();
			(weatherp+i)->x =
				lava_info[1] + SIN((weatherp+i)->work[0])*(weatherp+i)->work[1];
			(weatherp+i)->z =
				lava_info[3] + COS((weatherp+i)->work[0])*(weatherp+i)->work[1];
			(weatherp+i)->y = lava_info[2] + (400*RandF()-200);
		}
		else
		{
			(weatherp+i)->work[1] += 10;
			(weatherp+i)->x += SIN((weatherp+i)->work[0])*10;
			(weatherp+i)->z += COS((weatherp+i)->work[0])*10;
			(weatherp+i)->y += 50 - (weatherp+i)->work[1]/30;
		}
	}
}

static int LavaInit(int code)
{
	int i;
	switch (code)
	{
	case WEATHER_NULL:
		return FALSE;
	case WEATHER_FLOWER:
		lava_max = 30;
		lava_len = 30;
		break;
	case WEATHER_LAVA:
		lava_max = 15;
		lava_len = 15;
		break;
	case WEATHER_WHIRLPOOL:
		lava_max = 60;
		break;
	case WEATHER_JET:
		lava_max = 60;
		break;
	}
	if (!(weatherp = malloc(sizeof(WEATHER)*lava_max))) return FALSE;
	bzero(weatherp, sizeof(WEATHER)*lava_max);
	bzero(lava_info, sizeof(lava_info));
	switch (code)
	{
	case WEATHER_LAVA:
		for (i = 0; i < lava_max; i++) weatherp[i].frame = 7*RandF();
		break;
	}
	weather_code = code;
	return TRUE;
}

static void LavaMake(int code, SVEC pos, SVEC v0, SVEC v1, SVEC v2)
{
	switch (code)
	{
	case WEATHER_FLOWER:
		LavaMakeFlower(pos);
		v0[0] =  50; v0[1] =  0; v0[2] = 0;
		v1[0] =   0; v1[1] = 75; v1[2] = 0;
		v2[0] = -50; v2[1] =  0; v2[2] = 0;
		break;
	case WEATHER_LAVA:
		LavaMakeLava(pos);
		v0[0] =  100; v0[1] =   0; v0[2] = 0;
		v1[0] =    0; v1[1] = 150; v1[2] = 0;
		v2[0] = -100; v2[1] =   0; v2[2] = 0;
		break;
	case WEATHER_WHIRLPOOL:
		LavaMakeWhirlpool();
		v0[0] =  40; v0[1] =  0; v0[2] = 0;
		v1[0] =   0; v1[1] = 60; v1[2] = 0;
		v2[0] = -40; v2[1] =  0; v2[2] = 0;
		break;
	case WEATHER_JET:
		LavaMakeJet();
		v0[0] =  40; v0[1] =  0; v0[2] = 0;
		v1[0] =   0; v1[1] = 60; v1[2] = 0;
		v2[0] = -40; v2[1] =  0; v2[2] = 0;
		break;
	}
}

static void LavaVtx(Gfx *g, int i, SVEC v0, SVEC v1, SVEC v2, Vtx *template)
{
	int n = 0;
	Vtx *vtx = GfxAlloc(sizeof(Vtx)*15);
	if (!vtx) return;
	for (n = 0; n < 15; n += 3)
	{
		vtx[n+0] = template[0];
		vtx[n+0].v.ob[0] = weatherp[i+n/3].x + v0[0];
		vtx[n+0].v.ob[1] = weatherp[i+n/3].y + v0[1];
		vtx[n+0].v.ob[2] = weatherp[i+n/3].z + v0[2];
		vtx[n+1] = template[1];
		vtx[n+1].v.ob[0] = weatherp[i+n/3].x + v1[0];
		vtx[n+1].v.ob[1] = weatherp[i+n/3].y + v1[1];
		vtx[n+1].v.ob[2] = weatherp[i+n/3].z + v1[2];
		vtx[n+2] = template[2];
		vtx[n+2].v.ob[0] = weatherp[i+n/3].x + v2[0];
		vtx[n+2].v.ob[1] = weatherp[i+n/3].y + v2[1];
		vtx[n+2].v.ob[2] = weatherp[i+n/3].z + v2[2];
	}
	gSPVertex(g, K0_TO_PHYS(vtx), 15, 0);
}

static void LavaTxt(int code, SHORT i)
{
	u16 **txt;
	SHORT frame = (weatherp+i)->frame;
	switch (code)
	{
	case WEATHER_FLOWER:
		txt = SegmentToVirtual(txt_weather_flower);
		frame = (weatherp+i)->frame;
		break;
	case WEATHER_LAVA:
		txt = SegmentToVirtual(txt_weather_lava);
		frame = (weatherp+i)->frame;
		break;
	case WEATHER_WHIRLPOOL:
	case WEATHER_JET:
		txt = SegmentToVirtual(txt_weather_bubble);
		frame = 0;
		break;
	}
	gDPSetTextureImage(
		lava_glistp++, G_IM_FMT_RGBA, G_IM_SIZ_16b, 1, txt[frame]
	);
	gSPDisplayList(lava_glistp++, gfx_lava_txt);
}

static Gfx *LavaGfx(int code, UNUSED SVEC pos, SVEC eye, SVEC look)
{
	static Vtx template[] =
	{
		{{{0, 0, 0}, 0, {1544,  964}, {0xFF, 0xFF, 0xFF, 0xFF}}},
		{{{0, 0, 0}, 0, { 522, -568}, {0xFF, 0xFF, 0xFF, 0xFF}}},
		{{{0, 0, 0}, 0, {-498,  964}, {0xFF, 0xFF, 0xFF, 0xFF}}},
	};
	int i;
	short dist, angx, angy;
	SVEC v0, v1, v2;
	Gfx *gfx = GfxAlloc(sizeof(Gfx)*(1 + 10*(lava_len/5)+lava_len + 2));
	if (!gfx) return NULL;
	lava_glistp = gfx;
	WeatherGetCoord(look, eye, &dist, &angx, &angy);
	LavaMake(code, look, v0, v1, v2);
	WeatherXfm(v0, v1, v2, angx, angy);
	gSPDisplayList(lava_glistp++, gfx_lava_start);
	for (i = 0; i < lava_len; i += 5)
	{
		gDPPipeSync(lava_glistp++);
		LavaTxt(code, i);
		LavaVtx(lava_glistp++, i, v0, v1, v2, template);
		gSP2Triangles(lava_glistp++,  0,  1,  2, 0,  3,  4,  5, 0);
		gSP2Triangles(lava_glistp++,  6,  7,  8, 0,  9, 10, 11, 0);
		gSP1Triangle(lava_glistp++, 12, 13, 14, 0);
	}
	gSPDisplayList(lava_glistp++, gfx_weather_end);
	gSPEndDisplayList(lava_glistp++);
	return gfx;
}

static void LavaProc(int code)
{
	switch (code)
	{
	case WEATHER_WHIRLPOOL:
		lava_len = lava_info[7];
		break;
	case WEATHER_JET:
		lava_len = lava_info[7];
		break;
	}
}

Gfx *LavaDraw(int code, SVEC pos, SVEC look, SVEC eye)
{
	Gfx *gfx;
	if (weather_code == WEATHER_NULL && !LavaInit(code)) return NULL;
	LavaProc(code);
	if (!lava_len) return NULL;
	switch (code)
	{
	case WEATHER_FLOWER:
		gfx = LavaGfx(WEATHER_FLOWER, pos, eye, look);
		break;
	case WEATHER_LAVA:
		gfx = LavaGfx(WEATHER_LAVA, pos, eye, look);
		break;
	case WEATHER_WHIRLPOOL:
		gfx = LavaGfx(WEATHER_WHIRLPOOL, pos, eye, look);
		break;
	case WEATHER_JET:
		gfx = LavaGfx(WEATHER_JET, pos, eye, look);
		break;
	default:
		return NULL;
	}
	return gfx;
}
