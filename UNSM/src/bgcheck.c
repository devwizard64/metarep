#include <sm64.h>

static int bglist_check_wall(BGLIST *list, WALL_CHECK *check)
{
	register BGFACE *face;
	register float offset;
	register float radius = check->radius;
	register float x = check->x;
	register float y = check->y + check->offset;
	register float z = check->z;
	register float wx, wz;
	register float x0, x1, x2, y0, y1, y2;
	int count = 0;
	if (radius > 200) radius = 200;
	while (list)
	{
		face = list->face;
		list = list->next;
		if (y < face->yl || y > face->yh) continue;
		offset = face->nx*x + face->ny*y + face->nz*z + face->nw;
		if (offset < -radius || offset > radius) continue;
		wx = x;
		wz = z;
		if (face->flag & BG_WALL_Z)
		{
			x0 = -face->v0[2]; x1 = -face->v1[2]; x2 = -face->v2[2];
			y0 =  face->v0[1]; y1 =  face->v1[1]; y2 =  face->v2[1];
			if (face->nx > 0)
			{
				if (cross3(-wz, y, x0, y0, x1, y1) > 0) continue;
				if (cross3(-wz, y, x1, y1, x2, y2) > 0) continue;
				if (cross3(-wz, y, x2, y2, x0, y0) > 0) continue;
			}
			else
			{
				if (cross3(-wz, y, x0, y0, x1, y1) < 0) continue;
				if (cross3(-wz, y, x1, y1, x2, y2) < 0) continue;
				if (cross3(-wz, y, x2, y2, x0, y0) < 0) continue;
			}
		}
		else
		{
			x0 = face->v0[0]; x1 = face->v1[0]; x2 = face->v2[0];
			y0 = face->v0[1]; y1 = face->v1[1]; y2 = face->v2[1];
			if (face->nz > 0)
			{
				if (cross3(wx, y, x0, y0, x1, y1) > 0) continue;
				if (cross3(wx, y, x1, y1, x2, y2) > 0) continue;
				if (cross3(wx, y, x2, y2, x0, y0) > 0) continue;
			}
			else
			{
				if (cross3(wx, y, x0, y0, x1, y1) < 0) continue;
				if (cross3(wx, y, x1, y1, x2, y2) < 0) continue;
				if (cross3(wx, y, x2, y2, x0, y0) < 0) continue;
			}
		}
		if (object_80361180)
		{
			if (face->flag & BG_0002) continue;
		}
		else
		{
			if (face->code == 114) continue;
			if (face->code == 123)
			{
				if (object && (object->flag & 0x40)) continue;
				if (object && object == obj_mario && (mario->flag & 2)) continue;
			}
		}
		check->x += face->nx * (radius-offset);
		check->z += face->nz * (radius-offset);
		if (check->count < 4) check->wall[check->count++] = face;
		count++;
	}
	return count;
}

int bg_hit_wall(float *x, float *y, float *z, float offset, float radius)
{
	WALL_CHECK check;
	int count = 0;
	check.offset = offset;
	check.radius = radius;
	check.x = *x;
	check.y = *y;
	check.z = *z;
	check.count = 0;
	count = bg_check_wall(&check);
	*x = check.x;
	*y = check.y;
	*z = check.z;
	return count;
}

int bg_check_wall(WALL_CHECK *check)
{
	BGLIST *list;
	SHORT ix, iz;
	int count = 0;
	SHORT wx = (short)check->x;
	SHORT wz = (short)check->z;
	check->count = 0;
	if (wx < -8191 || wx > 8191) return count;
	if (wz < -8191 || wz > 8191) return count;
	ix = ((wx+8192)/1024) & 15;
	iz = ((wz+8192)/1024) & 15;
	list = movebg_root[iz][ix].list[BG_WALL].next;
	count += bglist_check_wall(list, check);
	list = statbg_root[iz][ix].list[BG_WALL].next;
	count += bglist_check_wall(list, check);
	bg_debug.wall++;
	return count;
}

static BGFACE *bglist_check_roof(
	BGLIST *list, int x, int y, int z, float *roof_y
)
{
	register BGFACE *face;
	register int x0, z0, x1, z1, x2, z2;
	BGFACE *roof = NULL;
	float nx, ny, nz, nw;
	float py;
	roof = NULL;
	while (list)
	{
		face = list->face;
		list = list->next;
		x0 = face->v0[0]; z0 = face->v0[2];
		z1 = face->v1[2]; x1 = face->v1[0];
		if (cross3(x, z, x0, z0, x1, z1) > 0) continue;
		x2 = face->v2[0]; z2 = face->v2[2];
		if (cross3(x, z, x1, z1, x2, z2) > 0) continue;
		if (cross3(x, z, x2, z2, x0, z0) > 0) continue;
		if (object_80361180)
		{
			if (face->flag & BG_0002) continue;
		}
		else
		{
			if (face->code == 114) continue;
		}
		nx = face->nx;
		ny = face->ny;
		nz = face->nz;
		nw = face->nw;
		if (ny == 0) continue;
		py = -(x*nx + nz*z + nw) / ny;
		if (y - (py-(-78)) > 0) continue;
		*roof_y = py;
		roof = face;
		break;
	}
	return roof;
}

float bg_check_roof(float x, float y, float z, BGFACE **roof)
{
	SHORT iz, ix;
	BGFACE *statbg;
	BGFACE *movebg;
	BGLIST *list;
	float stat_y = 20000;
	float move_y = 20000;
	SHORT wx = (short)x;
	SHORT wy = (short)y;
	SHORT wz = (short)z;
	*roof = NULL;
	if (wx < -8191 || wx > 8191) return stat_y;
	if (wz < -8191 || wz > 8191) return stat_y;
	ix = ((wx+8192)/1024) & 15;
	iz = ((wz+8192)/1024) & 15;
	list = movebg_root[iz][ix].list[BG_ROOF].next;
	movebg = bglist_check_roof(list, wx, wy, wz, &move_y);
	list = statbg_root[iz][ix].list[BG_ROOF].next;
	statbg = bglist_check_roof(list, wx, wy, wz, &stat_y);
	if (move_y < stat_y)
	{
		statbg = movebg;
		stat_y = move_y;
	}
	*roof = statbg;
	bg_debug.roof++;
	return stat_y;
}

UNUSED static
float obj_ground_y(OBJECT *obj)
{
	BGFACE *roof;
	float roof_y = bg_check_ground(
		obj->o_pos_x, obj->o_pos_y, obj->o_pos_z, &roof
	);
	return roof_y;
}

float bg_check_plane(float x, float y, float z, PLANE **plane)
{
	static PLANE ground_plane;
	UNUSED static char pad[56];
	BGFACE *ground;
	float ground_y = bg_check_ground(x, y, z, &ground);
	*plane = NULL;
	if (ground)
	{
		ground_plane.nx = ground->nx;
		ground_plane.ny = ground->ny;
		ground_plane.nz = ground->nz;
		ground_plane.nw = ground->nw;
		*plane = &ground_plane;
	}
	return ground_y;
}

static BGFACE *bglist_check_ground(
	BGLIST *list, int x, int y, int z, float *ground_y
)
{
	register BGFACE *face;
	register int x0, z0, x1, z1, x2, z2;
	float nx, ny, nz, nw;
	float py;
	BGFACE *ground = NULL;
	while (list)
	{
		face = list->face;
		list = list->next;
		x0 = face->v0[0]; z0 = face->v0[2];
		x1 = face->v1[0]; z1 = face->v1[2];
		if (cross3(x, z, x0, z0, x1, z1) < 0) continue;
		x2 = face->v2[0]; z2 = face->v2[2];
		if (cross3(x, z, x1, z1, x2, z2) < 0) continue;
		if (cross3(x, z, x2, z2, x0, z0) < 0) continue;
		if (object_80361180)
		{
			if (face->flag & BG_0002) continue;
		}
		else
		{
			if (face->code == 114) continue;
		}
		nx = face->nx;
		ny = face->ny;
		nz = face->nz;
		nw = face->nw;
		if (ny == 0) continue;
		py = -(x*nx + nz*z + nw) / ny;
		if (y - (py+-78) < 0) continue;
		*ground_y = py;
		ground = face;
		break;
	}
	return ground;
}

float bg_check_ground_y(float x, float y, float z)
{
	BGFACE *ground;
	float ground_y = bg_check_ground(x, y, z, &ground);
	return ground_y;
}

UNUSED static
float bg_check_ground_movebg(float x, float y, float z, BGFACE **ground)
{
	BGLIST *list;
	BGFACE *face;
	float ground_y = -11000;
	SHORT wx = (short)x;
	SHORT wy = (short)y;
	SHORT wz = (short)z;
	SHORT ix = ((wx+8192)/1024) & 15;
	SHORT iz = ((wz+8192)/1024) & 15;
	list = movebg_root[iz][ix].list[BG_GROUND].next;
	face = bglist_check_ground(list, wx, wy, wz, &ground_y);
	*ground = face;
	return ground_y;
}

float bg_check_ground(float x, float y, float z, BGFACE **ground)
{
	SHORT iz, ix;
	BGFACE *statbg;
	BGFACE *movebg;
	BGLIST *list;
	float stat_y = -11000;
	float move_y = -11000;
	SHORT wx = (short)x;
	SHORT wy = (short)y;
	SHORT wz = (short)z;
	*ground = NULL;
	if (wx < -8191 || wx > 8191) return stat_y;
	if (wz < -8191 || wz > 8191) return stat_y;
	ix = ((wx+8192)/1024) & 15;
	iz = ((wz+8192)/1024) & 15;
	list = movebg_root[iz][ix].list[BG_GROUND].next;
	movebg = bglist_check_ground(list, wx, wy, wz, &move_y);
	list = statbg_root[iz][ix].list[BG_GROUND].next;
	statbg = bglist_check_ground(list, wx, wy, wz, &stat_y);
	if (!object_80361182)
	{
		if (statbg && statbg->code == 18)
		{
			statbg = bglist_check_ground(list, wx, stat_y-200, wz, &stat_y);
		}
	}
	else
	{
		object_80361182 = FALSE;
	}
	if (!statbg) nullbg_count++;
	if (move_y > stat_y)
	{
		statbg = movebg;
		stat_y = move_y;
	}
	*ground = statbg;
	bg_debug.ground++;
	return stat_y;
}

float bg_check_water_y(float x, float z)
{
	int i;
	int n;
	short code;
	float xl, xh, zl, zh;
	float y = -11000;
	short *data = object_80361184;
	if (data)
	{
		n = *data++;
		for (i = 0; i < n; i++)
		{
			code = *data++;
			xl = *data++;
			zl = *data++;
			xh = *data++;
			zh = *data++;
			if (x > xl && x < xh && z > zl && z < zh && code < 50)
			{
				y = *data;
				break;
			}
			data++;
		}
	}
	return y;
}

float bg_check_gas_y(float x, float z)
{
	int i;
	int n;
	UNUSED int arg;
	short code;
	float xl, xh, zl, zh;
	float y = -11000;
	short *data = object_80361184;
	if (data)
	{
		n = *data++;
		for (i = 0; i < n; i++)
		{
			code = data[0];
			if (code >= 50)
			{
				xl = data[1];
				zl = data[2];
				xh = data[3];
				zh = data[4];
				if (x > xl && x < xh && z > zl && z < zh && code%10 == 0)
				{
					y = data[5];
					break;
				}
			}
			data += 6;
		}
	}
	return y;
}

static int bglist_len(BGLIST *list)
{
	int len = 0;
	while (list)
	{
		list = list->next;
		len++;
	}
	return len;
}

void bgcheck_debug(float x, float z)
{
	BGLIST *list;
	int ground = 0;
	int wall = 0;
	int roof = 0;
	int ix = (x+8192)/1024;
	int iz = (z+8192)/1024;
	list = statbg_root[iz & 15][ix & 15].list[BG_GROUND].next;
	ground += bglist_len(list);
	list = movebg_root[iz & 15][ix & 15].list[BG_GROUND].next;
	ground += bglist_len(list);
	list = statbg_root[iz & 15][ix & 15].list[BG_WALL].next;
	wall += bglist_len(list);
	list = movebg_root[iz & 15][ix & 15].list[BG_WALL].next;
	wall += bglist_len(list);
	list = statbg_root[iz & 15][ix & 15].list[BG_ROOF].next;
	roof += bglist_len(list);
	list = movebg_root[iz & 15][ix & 15].list[BG_ROOF].next;
	roof += bglist_len(list);
	obj_debug_802CA618("area   %x", 16*iz+ix);
	obj_debug_802CA618("dg %d", ground);
	obj_debug_802CA618("dw %d", wall);
	obj_debug_802CA618("dr %d", roof);
	obj_debug_802CA51C(80, -3);
	obj_debug_802CA618("%d", bg_debug.ground);
	obj_debug_802CA618("%d", bg_debug.wall);
	obj_debug_802CA618("%d", bg_debug.roof);
	obj_debug_802CA51C(-80, 0);
	obj_debug_802CA618("listal %d", bglist_count);
	obj_debug_802CA618("statbg %d", bgface_static);
	obj_debug_802CA618("movebg %d", bgface_count-bgface_static);
	bg_debug.ground = 0;
	bg_debug.roof = 0;
	bg_debug.wall = 0;
}

UNUSED static
int bg_hit_ground_roof(
	int flag, float *x, float *y, float *z, float radius,
	BGFACE **face, float *face_y
)
{
	float nx, ny, nz, nw;
	float wx = *x;
	float wy = *y;
	float wz = *z;
	float offset, dist;
	*face = NULL;
	if (flag)   *face_y = bg_check_roof(wx, wy, wz, face);
	else        *face_y = bg_check_ground(wx, wy, wz, face);
	if (!*face) return -1;
	nx = (*face)->nx;
	ny = (*face)->ny;
	nz = (*face)->nz;
	nw = (*face)->nw;
	offset = nx*wx + ny*wy + nz*wz + nw;
	dist = offset >= 0 ? offset : -offset;
	if (dist < radius)
	{
		*x += nx * (radius-offset);
		*y += ny * (radius-offset);
		*z += nz * (radius-offset);
		return 1;
	}
	return 0;
}
