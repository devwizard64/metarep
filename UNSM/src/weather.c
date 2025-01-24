#include <sm64.h>

extern Gfx gfx_snow_a[];
extern Gfx gfx_weather_end[];
extern Gfx gfx_snow_b[];

WEATHER *weatherp;
s8 weather_code = WEATHER_NULL;

static int snow_pos[3];
static s16 snow_len;
static s16 snow_max;

static int SnowInit(int code)
{
	switch (code)
	{
	case WEATHER_NULL:
		return FALSE;
	case WEATHER_SNOW:
		snow_max = 140;
		snow_len = 5;
		break;
	case WEATHER_BUBBLE:
		snow_max = 30;
		snow_len = 30;
		break;
	case WEATHER_BLIZZARD:
		snow_max = 140;
		snow_len = 140;
		break;
	}
	if (!(weatherp = malloc(sizeof(WEATHER)*snow_max))) return FALSE;
	bzero(weatherp, sizeof(WEATHER)*snow_max);
	weather_code = code;
	return TRUE;
}

static void SnowProc(int code, SVEC pos)
{
	unsigned int frame = gfx_frame;
	float water_y;
	switch (code)
	{
	case WEATHER_SNOW:
		if (snow_max > snow_len && !(frame & 63)) snow_len += 5;
		break;
	case WEATHER_BUBBLE:
		water_y = BGCheckWater(pos[0], pos[2]);
		snow_len = 5 * (SHORT)(0.001 * (water_y-400-pos[1]));
		if (snow_len < 0) snow_len = 0;
		if (snow_len > snow_max) snow_len = snow_max;
		break;
	case WEATHER_BLIZZARD:
		break;
	}
}

static void WeatherFree(WEATHER *weather)
{
	if (weather_code != WEATHER_NULL)
	{
		if (weather) free(weather);
		weather_code = WEATHER_NULL;
	}
}

void WeatherGetCoord(SVEC look, SVEC eye, short *dist, short *angx, short *angy)
{
	float dx = eye[0] - look[0];
	float dy = eye[1] - look[1];
	float dz = eye[2] - look[2];
	*dist = DIST3(dx, dy, dz);
	*angx = ATAN2(DIST2(dx, dz), dy);
	*angy = ATAN2(dz, dx);
}

static void WeatherSetCoord(
	SVEC look, SVEC eye, SHORT dist, SHORT angx, SHORT angy
)
{
	eye[0] = look[0] + dist*COS(angx)*SIN(angy);
	eye[1] = look[1] + dist*SIN(angx);
	eye[2] = look[2] + dist*COS(angx)*COS(angy);
}

static int SnowIsVisible(int i, int x, int y, int z)
{
	int posx = (weatherp+i)->x;
	int posy = (weatherp+i)->y;
	int posz = (weatherp+i)->z;
	if (SQUARE(posx-x)+SQUARE(posz-z) > SQUARE(300)) return FALSE;
	if (posy < y-201 || posy > y+201) return FALSE;
	return TRUE;
}

static void SnowMakeSnow(int x, int y, int z)
{
	int i;
	int dx = x - snow_pos[0];
	int dy = y - snow_pos[1];
	int dz = z - snow_pos[2];
	for (i = 0; i < snow_len; i++)
	{
		(weatherp+i)->flag = SnowIsVisible(i, x, y, z);
		if (!(weatherp+i)->flag)
		{
			(weatherp+i)->x = x + (400*RandF() - 200) + (SHORT)(2*dx);
			(weatherp+i)->z = z + (400*RandF() - 200) + (SHORT)(2*dz);
			(weatherp+i)->y = y + (200*RandF());
			(weatherp+i)->flag = TRUE;
		}
		else
		{
			(weatherp+i)->x += (RandF()*2-1) + (SHORT)(dx/1.2);
			(weatherp+i)->y -=               - (SHORT)(dy*0.8) + 2;
			(weatherp+i)->z += (RandF()*2-1) + (SHORT)(dz/1.2);
		}
	}
	snow_pos[0] = x;
	snow_pos[1] = y;
	snow_pos[2] = z;
}

static void SnowMakeBlizzard(int x, int y, int z)
{
	int i;
	int dx = x - snow_pos[0];
	int dy = y - snow_pos[1];
	int dz = z - snow_pos[2];
	for (i = 0; i < snow_len; i++)
	{
		(weatherp+i)->flag = SnowIsVisible(i, x, y, z);
		if (!(weatherp+i)->flag)
		{
			(weatherp+i)->x = x + (400*RandF() - 200) + (SHORT)(2*dx);
			(weatherp+i)->z = z + (400*RandF() - 200) + (SHORT)(2*dz);
			(weatherp+i)->y = y + (400*RandF() - 200);
			(weatherp+i)->flag = TRUE;
		}
		else
		{
			(weatherp+i)->x += (RandF()*2-1) + (SHORT)(dx/1.2) + 20;
			(weatherp+i)->y -=               - (SHORT)(dy*0.8) + 5;
			(weatherp+i)->z += (RandF()*2-1) + (SHORT)(dz/1.2);
		}
	}
	snow_pos[0] = x;
	snow_pos[1] = y;
	snow_pos[2] = z;
}

UNUSED
static int BubbleIsVisible(int x, UNUSED int y, int z)
{
	if (SQUARE(x-3380)+SQUARE(z+520) < SQUARE(3000)) return TRUE;
	return FALSE;
}

static void SnowMakeBubble(int x, int y, int z)
{
	int i;
	for (i = 0; i < snow_len; i++)
	{
		(weatherp+i)->flag = SnowIsVisible(i, x, y, z);
		if (!(weatherp+i)->flag)
		{
			(weatherp+i)->x = x + (400*RandF() - 200);
			(weatherp+i)->z = z + (400*RandF() - 200);
			(weatherp+i)->y = y + (400*RandF() - 200);
			(weatherp+i)->flag = TRUE;
		}
	}
}

void WeatherXfm(SVEC v0, SVEC v1, SVEC v2, SHORT angx, SHORT angy)
{
	float cx = COS( angx);
	float sx = SIN( angx);
	float cy = COS(-angy);
	float sy = SIN(-angy);
	FVEC f0, f1, f2;
	f0[0] = v0[0]; f0[1] = v0[1]; f0[2] = v0[2];
	f1[0] = v1[0]; f1[1] = v1[1]; f1[2] = v1[2];
	f2[0] = v2[0]; f2[1] = v2[1]; f2[2] = v2[2];
	v0[0] = f0[0]*cy + f0[1]*( sx*sy) + f0[2]*(-sy*cx);
	v0[1] =            f0[1]*( cx   ) + f0[2]*( sx   );
	v0[2] = f0[0]*sy + f0[1]*(-sx*cy) + f0[2]*( cx*cy);
	v1[0] = f1[0]*cy + f1[1]*( sx*sy) + f1[2]*(-sy*cx);
	v1[1] =            f1[1]*( cx   ) + f1[2]*( sx   );
	v1[2] = f1[0]*sy + f1[1]*(-sx*cy) + f1[2]*( cx*cy);
	v2[0] = f2[0]*cy + f2[1]*( sx*sy) + f2[2]*(-sy*cx);
	v2[1] =            f2[1]*( cx   ) + f2[2]*( sx   );
	v2[2] = f2[0]*sy + f2[1]*(-sx*cy) + f2[2]*( cx*cy);
}

static void SnowVtx(Gfx *g, int i, SVEC v0, SVEC v1, SVEC v2)
{
	static Vtx template[] =
	{
		{{{-5,  5, 0}, 0, {  0,   0}, {0x7F, 0x7F, 0x7F, 0xFF}}},
		{{{-5, -5, 0}, 0, {  0, 960}, {0x7F, 0x7F, 0x7F, 0xFF}}},
		{{{ 5,  5, 0}, 0, {960,   0}, {0x7F, 0x7F, 0x7F, 0xFF}}},
	};
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

static Gfx *SnowGfx(int code, SVEC pos, SVEC eye, SVEC look)
{
	int i;
	short dist, angx, angy;
	SVEC coord;
	SVEC v0 = {-5,  5, 0};
	SVEC v1 = {-5, -5, 0};
	SVEC v2 = { 5,  5, 0};
	Gfx *gfx, *g = gfx = GfxAlloc(sizeof(Gfx)*(1+(1+5)*snow_len+2));
	if (!gfx) return NULL;
	SnowProc(code, pos);
	WeatherGetCoord(look, eye, &dist, &angx, &angy);
	switch (code)
	{
	case WEATHER_SNOW:
		if (dist > 250) dist -= 250;
		else dist = 1;
		WeatherSetCoord(look, coord, dist, angx, angy);
		SnowMakeSnow(coord[0], coord[1], coord[2]);
		break;
	case WEATHER_BUBBLE:
		if (dist > 500) dist -= 500;
		else dist = 1;
		WeatherSetCoord(look, coord, dist, angx, angy);
		SnowMakeBubble(coord[0], coord[1], coord[2]);
		break;
	case WEATHER_BLIZZARD:
		if (dist > 250) dist -= 250;
		else dist = 1;
		WeatherSetCoord(look, coord, dist, angx, angy);
		SnowMakeBlizzard(coord[0], coord[1], coord[2]);
		break;
	}
	WeatherXfm(v0, v1, v2, angx, angy);
	if (code == WEATHER_SNOW || code == WEATHER_BLIZZARD)
	{
		gSPDisplayList(g++, gfx_snow_a);
	}
	else if (code == WEATHER_BUBBLE)
	{
		gSPDisplayList(g++, gfx_snow_b);
	}
	for (i = 0; i < snow_len; i += 5)
	{
		SnowVtx(g++, i, v0, v1, v2);
		gSP2Triangles(g++,  0,  1,  2, 0,  3,  4,  5, 0);
		gSP2Triangles(g++,  6,  7,  8, 0,  9, 10, 11, 0);
		gSP1Triangle(g++, 12, 13, 14, 0);
	}
	gSPDisplayList(g++, gfx_weather_end);
	gSPEndDisplayList(g++);
	return gfx;
}

Gfx *WeatherDraw(int code, SVEC pos, SVEC look, SVEC eye)
{
	Gfx *gfx;
	if (MsgGet() != -1) return NULL;
	if (weather_code != WEATHER_NULL && weather_code != code)
	{
		code = WEATHER_NULL;
	}
	if (code >= WEATHER_LAVA_MIN)
	{
		gfx = LavaDraw(code, pos, look, eye);
		return gfx;
	}
	if (weather_code == WEATHER_NULL && !SnowInit(code)) return NULL;
	switch (code)
	{
	case WEATHER_NULL:
		WeatherFree(weatherp);
		return NULL;
	case WEATHER_SNOW:
		gfx = SnowGfx(WEATHER_SNOW, pos, eye, look);
		break;
	case WEATHER_BUBBLE:
		gfx = SnowGfx(WEATHER_BUBBLE, pos, eye, look);
		break;
	case WEATHER_BLIZZARD:
		gfx = SnowGfx(WEATHER_BLIZZARD, pos, eye, look);
		break;
	default:
		return NULL;
	}
	return gfx;
}
