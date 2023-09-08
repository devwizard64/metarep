#include <sm64.h>

#define BGLIST_MAX              7000
#define BGFACE_MAX              2300

static int bgload_8038BE90;
BGROOT statbg_root[16][16];
BGROOT movebg_root[16][16];
BGLIST *bglist_data;
BGFACE *bgface_data;
#define bglist_max BGLIST_MAX
s16 bgface_max;
int bgload_8038EEA4[12];

static BGLIST *bglist_alloc(void)
{
	BGLIST *list = &bglist_data[bglist_count]; bglist_count++;
	list->next = NULL;
	if (bglist_count >= bglist_max)
	{
	}
	return list;
}

static BGFACE *bgface_alloc(void)
{
	BGFACE *face = &bgface_data[bgface_count]; bgface_count++;
	if (bgface_count >= bgface_max)
	{
	}
	face->code = 0;
	face->arg = 0;
	face->flag = 0;
	face->area = 0;
	face->obj = 0;
	return face;
}

static void bgroot_clear(BGROOT *root)
{
	register int n = 16*16;
	while (n--)
	{
		root->list[BG_GROUND].next = NULL;
		root->list[BG_ROOF].next = NULL;
		root->list[BG_WALL].next = NULL;
		root++;
	}
}

static void statbg_clear(void)
{
	bgroot_clear(&statbg_root[0][0]);
}

static void bglist_create(SHORT flag, SHORT ix, SHORT iz, BGFACE *face)
{
	BGLIST *list = bglist_alloc();
	BGLIST *root;
	SHORT face_y;
	SHORT list_y;
	SHORT m;
	SHORT index;
	if (face->ny > (DOUBLE)0.01)
	{
		index = BG_GROUND;
		m = 1;
	}
	else if (face->ny < (DOUBLE)-0.01)
	{
		index = BG_ROOF;
		m = -1;
	}
	else
	{
		index = BG_WALL;
		m = 0;
		if (face->nx < (DOUBLE)-0.707 || face->nx > (DOUBLE)0.707)
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

static SHORT min3(SHORT x, SHORT y, SHORT z)
{
	if (x > y) x = y;
	if (x > z) x = z;
	return x;
}

static SHORT max3(SHORT x, SHORT y, SHORT z)
{
	if (x < y) x = y;
	if (x < z) x = z;
	return x;
}

static SHORT bgarea_min(SHORT x)
{
	SHORT i;
	x += 8192;
	if (x < 0) x = 0;
	i = x / 1024;
	if (x % 1024 < 50) i--;
	if (i < 0) i = 0;
	return i;
}

static SHORT bgarea_max(SHORT x)
{
	SHORT i;
	x += 8192;
	if (x < 0) x = 0;
	i = x / 1024;
	if (x % 1024 > 1024-50) i++;
	if (i > 15) i = 15;
	return i;
}

static void bgface_link(BGFACE *face, int flag)
{
	UNUSED int yl, yh;
	SHORT xl, zl, xh, zh;
	SHORT ixl, izl, ixh, izh;
	SHORT iz, ix;
	UNUSED int iy = 0;
	xl = min3(face->v0[0], face->v1[0], face->v2[0]);
	zl = min3(face->v0[2], face->v1[2], face->v2[2]);
	xh = max3(face->v0[0], face->v1[0], face->v2[0]);
	zh = max3(face->v0[2], face->v1[2], face->v2[2]);
	ixl = bgarea_min(xl);
	ixh = bgarea_max(xh);
	izl = bgarea_min(zl);
	izh = bgarea_max(zh);
	for (iz = izl; iz <= izh; iz++)
	{
		for (ix = ixl; ix <= ixh; ix++)
		{
			bglist_create(flag, ix, iz, face);
		}
	}
}

UNUSED
static void bgload_80382B6C(void)
{
}

static BGFACE *bgface_create(MAP *vtx, MAP **map)
{
	BGFACE *face;
	register int x0, y0, z0;
	register int x1, y1, z1;
	register int x2, y2, z2;
	int yh, yl;
	float nx, ny, nz;
	float d;
	SHORT v0 = 3 * (*map)[0];
	SHORT v1 = 3 * (*map)[1];
	SHORT v2 = 3 * (*map)[2];
	x0 = vtx[v0+0]; y0 = vtx[v0+1]; z0 = vtx[v0+2];
	x1 = vtx[v1+0]; y1 = vtx[v1+1]; z1 = vtx[v1+2];
	x2 = vtx[v2+0]; y2 = vtx[v2+1]; z2 = vtx[v2+2];
	nx = cross3(z0, y0, z1, y1, z2, y2);
	ny = cross3(x0, z0, x1, z1, x2, z2);
	nz = cross3(y0, x0, y1, x1, y2, x2);
	d = sqrtf(nx*nx + ny*ny + nz*nz);
	yl = y0;
	if (yl > y1) yl = y1;
	if (yl > y2) yl = y2;
	yh = y0;
	if (yh < y1) yh = y1;
	if (yh < y2) yh = y2;
	if (d < (DOUBLE)0.0001) return NULL;
	d = (DOUBLE)1 / d;
	nx *= d;
	ny *= d;
	nz *= d;
	face = bgface_alloc();
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

static int bgface_isarg(SHORT code)
{
	int result = FALSE;
	switch (code)
	{
	case 4:
	case 14:
	case 36:
	case 37:
	case 39:
	case 44:
	case 45:
		result = TRUE;
		break;
	default:
		break;
	}
	return result;
}

static int bgface_flag(SHORT code)
{
	int flag = 0;
	switch (code)
	{
	case 118:
	case 119:
	case 120:
	case 122:
		flag = BG_0002;
		break;
	default:
		break;
	}
	return flag;
}

static void statbg_face(MAP **map, MAP *vtx, SHORT code, AREA **area)
{
	int i;
	int n;
	BGFACE *face;
	AREA a = 0;
	SHORT isarg = bgface_isarg(code);
	SHORT flag = bgface_flag(code);
	n = **map; (*map)++;
	for (i = 0; i < n; i++)
	{
		if (*area)
		{
			a = **area; (*area)++;
		}
		if ((face = bgface_create(vtx, map)))
		{
			face->area = a;
			face->code = code;
			face->flag = (CHAR)flag;
			if (isarg)  face->arg = (*map)[3];
			else        face->arg = 0;
			bgface_link(face, 0);
		}
		*map += 3;
		if (isarg) (*map)++;
	}
}

static MAP *statbg_vtx(MAP **map)
{
	int n;
	UNUSED char pad[16];
	MAP *vtx;
	n = **map; (*map)++;
	vtx = *map;
	*map += 3*n;
	return vtx;
}

static void statbg_water(MAP **map)
{
	int n;
	int i;
	object_80361184 = *map;
	n = *(*map)++;
	if (n > 20)
	{
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
		object_80361188[i] = y;
	}
}

void map_init(void)
{
	bgface_max = BGFACE_MAX;
	bglist_data = mem_alloc(sizeof(BGLIST)*bglist_max, MEM_ALLOC_L);
	bgface_data = mem_alloc(sizeof(BGFACE)*bgface_max, MEM_ALLOC_L);
	object_8036125C = 0;
	message_802DB350();
}

void map_load(SHORT scene, MAP *map, AREA *area, TAG *tag)
{
	MAP code;
#ifdef sgi
	MAP *vtx;
#else
	MAP *vtx = NULL;
#endif
	UNUSED int i;
	object_80361184 = NULL;
	bgload_8038BE90 = 0;
	bglist_count = 0;
	bgface_count = 0;
	statbg_clear();
	for (;;)
	{
		code = *map; map++;
		if      (code < 64) statbg_face(&map, vtx, code, &area);
		else if (code == MAP_VTX) vtx = statbg_vtx(&map);
		else if (code == MAP_OBJECT) map_obj_load(scene, &map);
		else if (code == MAP_WATER) statbg_water(&map);
		else if (code == MAP_BGEND) continue;
		else if (code == MAP_END) break;
		else if (code > 100) statbg_face(&map, vtx, code, &area);
		else
		{
		}
	}
	if (tag && *tag != -1)
	{
		if (*tag >= 0 && *tag < TAG_END) tag_load(scene, tag);
		else tag_obj_load(scene, tag);
	}
	bglist_static = bglist_count;
	bgface_static = bgface_count;
}

void movebg_clear(void)
{
	if (!(object_8033D480 & 0x40))
	{
		bgface_count = bgface_static;
		bglist_count = bglist_static;
		bgroot_clear(&movebg_root[0][0]);
	}
}

UNUSED
static void bgload_80383604(void)
{
}

static void movebg_vtx(MAP **map, MAP *vtx)
{
	register MAP *v;
	register float x, y, z;
	register int n;
	MTXF *m;
	MTXF mf;
	m = &object->mf;
	n = **map; (*map)++;
	v = *map;
	if (!object->list.s.mf)
	{
		object->list.s.mf = m;
		objlib_802A2930(object, O_POS_X, O_SHAPE_ANG_X);
	}
	objlib_8029DDA8(object, mf, *m);
	while (n--)
	{
		x = *v++; y = *v++; z = *v++;
		*vtx++ = x*mf[0][0] + y*mf[1][0] + z*mf[2][0] + mf[3][0];
		*vtx++ = x*mf[0][1] + y*mf[1][1] + z*mf[2][1] + mf[3][1];
		*vtx++ = x*mf[0][2] + y*mf[1][2] + z*mf[2][2] + mf[3][2];
	}
	*map = v;
}

extern O_SCRIPT o_13001C34[];

static void movebg_face(MAP **map, MAP *vtx)
{
	int code;
	int i;
	int n;
	SHORT isarg;
	SHORT flag;
	SHORT area;
	code = **map; (*map)++;
	n = **map; (*map)++;
	isarg = bgface_isarg(code);
	flag = bgface_flag(code);
	flag |= BG_MOVE;
	if (object->script == segment_to_virtual(o_13001C34)) area = 5;
	else area = 0;
	for (i = 0; i < n; i++)
	{
		BGFACE *face;
		if ((face = bgface_create(vtx, map)))
		{
			face->obj = object;
			face->code = code;
			if (isarg)  face->arg = (*map)[3];
			else        face->arg = 0;
			face->flag |= flag;
			face->area = (CHAR)area;
			bgface_link(face, 1);
		}
		if (isarg)  *map += 4;
		else        *map += 3;
	}
}

void object_map_load(void)
{
	UNUSED int i;
	MAP vtx[3*200];
	MAP *map = object->map;
	float pl_dist = object->o_pl_dist;
	float col_dist = object->o_col_dist;
	if (object->o_pl_dist == 19000)
	{
		pl_dist = objlib_8029E2F8(object, obj_mario);
	}
	if (object->o_col_dist > 4000)
	{
		object->o_shape_dist = object->o_col_dist;
	}
	if (!(object_8033D480 & 0x40) && pl_dist < col_dist && !(object->flag & 8))
	{
		map++;
		movebg_vtx(&map, vtx);
		while (*map != MAP_BGEND) movebg_face(&map, vtx);
	}
	if (pl_dist < object->o_shape_dist)
	{
		object->list.s.s.flag |= S_FLAG_ACTIVE;
	}
	else
	{
		object->list.s.s.flag &= ~S_FLAG_ACTIVE;
	}
}
