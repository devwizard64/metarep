#include <sm64.h>

#define BGLIST_MAX              7000
#define BGFACE_MAX              2300

int bgload_8038BE90;
BGROOT statbg_root[BGAREA_N][BGAREA_N];
BGROOT movebg_root[BGAREA_N][BGAREA_N];
BGLIST *bglist_data;
BGFACE *bgface_data;
#define bglist_max BGLIST_MAX
short bgface_max;
int bgload_8038EEA4[12];

static BGLIST *BGListAlloc(void)
{
	BGLIST *list = &bglist_data[bglist_count]; bglist_count++;
	list->next = NULL;
	if (bglist_count >= bglist_max)
	{
		debugf((" mcMakeBGCheckList OVERFLOW\n"));
	}
	return list;
}

static BGFACE *BGFaceAlloc(void)
{
	BGFACE *face = &bgface_data[bgface_count]; bgface_count++;
	if (bgface_count >= bgface_max)
	{
		debugf((" mcMakeBGCheckData OVERFLOW\n"));
	}
	face->code = 0;
	face->attr = 0;
	face->flag = 0;
	face->area = 0;
	face->obj = NULL;
	return face;
}

static void BGRootClear(BGROOT *root)
{
	register int n = BGAREA_N*BGAREA_N;
	while (n--)
	{
		root->list[BG_GROUND].next = NULL;
		root->list[BG_ROOF].next = NULL;
		root->list[BG_WALL].next = NULL;
		root++;
	}
}

static void StatBGClear(void)
{
	BGRootClear(&statbg_root[0][0]);
}

static void BGListCreate(SHORT flag, SHORT ix, SHORT iz, BGFACE *face)
{
	BGLIST *list = BGListAlloc();
	BGLIST *root;
	SHORT face_y, list_y, m, index;
	if (face->ny > 0.01)
	{
		index = BG_GROUND;
		m = 1;
	}
	else if (face->ny < -0.01)
	{
		index = BG_ROOF;
		m = -1;
	}
	else
	{
		index = BG_WALL;
		m = 0;
		if (face->nx < -0.707 || face->nx > 0.707)
		{
			face->flag |= BG_WALL_Z;
		}
	}
	face_y = face->v0[1] * m;
	list->face = face;
	if (flag)   root = &movebg_root[iz][ix].list[index];
	else        root = &statbg_root[iz][ix].list[index];
	while (root->next)
	{
		list_y = root->next->face->v0[1] * m;
		if (face_y > list_y) break;
		root = root->next;
	}
	list->next = root->next;
	root->next = list;
}

static SHORT Min3(SHORT x, SHORT y, SHORT z)
{
	if (x > y) x = y;
	if (x > z) x = z;
	return x;
}

static SHORT Max3(SHORT x, SHORT y, SHORT z)
{
	if (x < y) x = y;
	if (x < z) x = z;
	return x;
}

static SHORT BGAreaMin(SHORT x)
{
	SHORT i;
	x += MAP_HALF;
	if (x < 0) x = 0;
	i = x / BGAREA_SIZE;
	if (x % BGAREA_SIZE < BGAREA_FUZZ) i--;
	if (i < 0) i = 0;
	return i;
}

static SHORT BGAreaMax(SHORT x)
{
	SHORT i;
	x += MAP_HALF;
	if (x < 0) x = 0;
	i = x / BGAREA_SIZE;
	if (x % BGAREA_SIZE > BGAREA_SIZE-BGAREA_FUZZ) i++;
	if (i > BGAREA_N-1) i = BGAREA_N-1;
	return i;
}

static void BGFaceLink(BGFACE *face, int flag)
{
	UNUSED int yl, yh;
	SHORT xl, zl, xh, zh, ixl, izl, ixh, izh, iz, ix;
	UNUSED int iy = 0;
	xl = Min3(face->v0[0], face->v1[0], face->v2[0]);
	zl = Min3(face->v0[2], face->v1[2], face->v2[2]);
	xh = Max3(face->v0[0], face->v1[0], face->v2[0]);
	zh = Max3(face->v0[2], face->v1[2], face->v2[2]);
	ixl = BGAreaMin(xl);
	ixh = BGAreaMax(xh);
	izl = BGAreaMin(zl);
	izh = BGAreaMax(zh);
	for (iz = izl; iz <= izh; iz++)
	{
		for (ix = ixl; ix <= ixh; ix++)
		{
			BGListCreate(flag, ix, iz, face);
		}
	}
}

UNUSED
static void bgload_80382B6C(void)
{
}

static BGFACE *BGFaceCreate(MAP *vtx, MAP **map)
{
	BGFACE *face;
	register int x0, y0, z0, x1, y1, z1, x2, y2, z2;
	int yh, yl;
	float nx, ny, nz, d;
	SHORT v0 = 3 * (*map)[0];
	SHORT v1 = 3 * (*map)[1];
	SHORT v2 = 3 * (*map)[2];
	x0 = vtx[v0+0]; y0 = vtx[v0+1]; z0 = vtx[v0+2];
	x1 = vtx[v1+0]; y1 = vtx[v1+1]; z1 = vtx[v1+2];
	x2 = vtx[v2+0]; y2 = vtx[v2+1]; z2 = vtx[v2+2];
	nx = CROSS3(z0, y0, z1, y1, z2, y2);
	ny = CROSS3(x0, z0, x1, z1, x2, z2);
	nz = CROSS3(y0, x0, y1, x1, y2, x2);
	d = DIST3(nx, ny, nz);
	yl = y0;
	if (yl > y1) yl = y1;
	if (yl > y2) yl = y2;
	yh = y0;
	if (yh < y1) yh = y1;
	if (yh < y2) yh = y2;
	if (d < 0.0001) return NULL;
	d = 1.0 / d;
	nx *= d;
	ny *= d;
	nz *= d;
	face = BGFaceAlloc();
	face->v0[0] = x0; face->v1[0] = x1; face->v2[0] = x2;
	face->v0[1] = y0; face->v1[1] = y1; face->v2[1] = y2;
	face->v0[2] = z0; face->v1[2] = z1; face->v2[2] = z2;
	face->nx = nx;
	face->ny = ny;
	face->nz = nz;
	face->nw = -(nx*x0 + ny*y0 + nz*z0);
	face->yl = yl - 5;
	face->yh = yh + 5;
	return face;
}

static int BGFaceHasAttr(SHORT code)
{
	int result = FALSE;
	switch (code)
	{
	case BG_4:
	case BG_14:
	case BG_36:
	case BG_37:
	case BG_39:
	case BG_44:
	case BG_45:
		result = TRUE;
		break;
	default:
		break;
	}
	return result;
}

static int BGFaceFlag(SHORT code)
{
	int flag = 0;
	switch (code)
	{
	case BG_118:
	case BG_119:
	case BG_120:
	case BG_122:
		flag = BG_0002;
		break;
	default:
		break;
	}
	return flag;
}

static void StatBGFace(MAP **map, MAP *vtx, SHORT code, AREA **area)
{
	int i, n;
	BGFACE *face;
	AREA a = 0;
	SHORT hasattr = BGFaceHasAttr(code);
	SHORT flag = BGFaceFlag(code);
	n = **map; (*map)++;
	for (i = 0; i < n; i++)
	{
		if (*area)
		{
			a = **area; (*area)++;
		}
		if ((face = BGFaceCreate(vtx, map)))
		{
			face->area = a;
			face->code = code;
			face->flag = (CHAR)flag;
			if (hasattr)    face->attr = (*map)[3];
			else            face->attr = 0;
			BGFaceLink(face, 0);
		}
		*map += 3;
		if (hasattr) (*map)++;
	}
}

static MAP *StatBGVtx(MAP **map)
{
	int n;
	UNUSED char pad[16];
	MAP *vtx;
	n = **map; (*map)++;
	vtx = *map;
	*map += 3*n;
	return vtx;
}

static void StatBGWater(MAP **map)
{
	int n, i;
	waterp = *map;
	n = *(*map)++;
	if (n > 20)
	{
		debugf(("Error Water Over\n"));
	}
	for (i = 0; i < n; i++)
	{
		UNUSED MAP code, xl, zl, xh, zh;
		MAP y;
		code = *(*map)++;
		xl = *(*map)++;
		xh = *(*map)++;
		zl = *(*map)++;
		zh = *(*map)++;
		y = *(*map)++;
		water_table[i] = y;
	}
}

void MapInit(void)
{
	bgface_max = BGFACE_MAX;
	bglist_data = MemAlloc(sizeof(BGLIST)*bglist_max, MEM_ALLOC_L);
	bgface_data = MemAlloc(sizeof(BGFACE)*bgface_max, MEM_ALLOC_L);
	object_8036125C = 0;
	PauseMenu_Init();
}

void MapLoad(SHORT scene, MAP *map, AREA *area, TAG *tag)
{
	MAP code;
#ifdef sgi
	MAP *vtx;
#else
	MAP *vtx = NULL;
#endif
	UNUSED int i;
	waterp = NULL;
	bgload_8038BE90 = 0;
	bglist_count = 0;
	bgface_count = 0;
	StatBGClear();
	for (;;)
	{
		code = *map; map++;
		if      (code < MAP_VTX) StatBGFace(&map, vtx, code, &area);
		else if (code == MAP_VTX) vtx = StatBGVtx(&map);
		else if (code == MAP_OBJECT) MapObjLoad(scene, &map);
		else if (code == MAP_WATER) StatBGWater(&map);
		else if (code == MAP_BGEND) continue;
		else if (code == MAP_END) break;
		else if (code > MAP_FACE) StatBGFace(&map, vtx, code, &area);
		else
		{
			debugf((" BGCode Error \n"));
		}
	}
	if (tag && *tag != -1)
	{
		if (*tag >= 0 && *tag < TAG_END) TagLoad(scene, tag);
		else TagObjLoad(scene, tag);
	}
	bglist_static = bglist_count;
	bgface_static = bgface_count;
}

void MoveBGClear(void)
{
	if (!(object_flag & OBJECT_FROZEN))
	{
		bgface_count = bgface_static;
		bglist_count = bglist_static;
		BGRootClear(&movebg_root[0][0]);
	}
}

UNUSED
static void bgload_80383604(void)
{
}

static void MoveBGVtx(MAP **map, MAP *vtx)
{
	register MAP *v;
	register float x, y, z;
	register int n;
	FMTX *m, fm;
	m = &object->mtx;
	n = **map; (*map)++;
	v = *map;
	if (!object->s.m)
	{
		object->s.m = m;
		ObjCalcMtx(object, O_POS, O_SHAPEANG);
	}
	ObjFMtxScaleCopy(object, fm, *m);
	while (n--)
	{
		x = *v++; y = *v++; z = *v++;
		*vtx++ = x*fm[0][0] + y*fm[1][0] + z*fm[2][0] + fm[3][0];
		*vtx++ = x*fm[0][1] + y*fm[1][1] + z*fm[2][1] + fm[3][1];
		*vtx++ = x*fm[0][2] + y*fm[1][2] + z*fm[2][2] + fm[3][2];
	}
	*map = v;
}

extern OBJLANG obj_13001C34[];

static void MoveBGFace(MAP **map, MAP *vtx)
{
	int code, i, n;
	SHORT hasattr, flag, area;
	code = **map; (*map)++;
	n = **map; (*map)++;
	hasattr = BGFaceHasAttr(code);
	flag = BGFaceFlag(code);
	flag |= BG_MOVE;
	if (object->script == SegmentToVirtual(obj_13001C34)) area = 5;
	else area = 0;
	for (i = 0; i < n; i++)
	{
		BGFACE *face;
		if ((face = BGFaceCreate(vtx, map)))
		{
			face->obj = object;
			face->code = code;
			if (hasattr)    face->attr = (*map)[3];
			else            face->attr = 0;
			face->flag |= flag;
			face->area = (CHAR)area;
			BGFaceLink(face, 1);
		}
		if (hasattr)    *map += 4;
		else            *map += 3;
	}
}

void ObjectMapLoad(void)
{
	UNUSED int i;
	MAP vtx[3*200];
	MAP *map = object->map;
	float targetdist = object->o_targetdist;
	float checkdist = object->o_checkdist;
	if (object->o_targetdist == 19000) /* T:def */
	{
		targetdist = ObjCalcDist3D(object, mario_obj);
	}
	if (object->o_checkdist > 4000) object->o_shapedist = object->o_checkdist;
	if (
		!(object_flag & OBJECT_FROZEN) &&
		targetdist < checkdist &&
		!(object->flag & OBJ_0008)
	)
	{
		map++;
		MoveBGVtx(&map, vtx);
		while (*map != MAP_BGEND) MoveBGFace(&map, vtx);
	}
	if (targetdist < object->o_shapedist)   object->s.s.flag |= SHP_ACTIVE;
	else                                    object->s.s.flag &= ~SHP_ACTIVE;
}
