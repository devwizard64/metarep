#include <sm64.h>

static s16 ride_80330E20 = 0;
UNUSED static int ride_80330E24[4] = {0};
static OBJECT *plride_obj = NULL;

void PLRideFind(void)
{
	BGFACE *ground;
	UNUSED OBJECT *obj;
	float x, y, z, ground_y;
	int code;
	if (!mario_obj) return;
	x = mario_obj->o_posx;
	y = mario_obj->o_posy;
	z = mario_obj->o_posz;
	ground_y = BGCheckGround(x, y, z, &ground);
	if (fabsf(y-ground_y) < 4)  code = 0;
	else                        code = 1;
	switch (code)
	{
	case 1:
		plride_obj = NULL;
		mario_obj->ride = NULL;
		break;
	case 0:
		if (ground && ground->obj)
		{
			plride_obj = ground->obj;
			mario_obj->ride = ground->obj;
		}
		else
		{
			plride_obj = NULL;
			mario_obj->ride = NULL;
		}
		break;
	}
}

void MarioGetPos(float *x, float *y, float *z)
{
	*x = player_data[0].pos[0];
	*y = player_data[0].pos[1];
	*z = player_data[0].pos[2];
}

void MarioSetPos(float x, float y, float z)
{
	player_data[0].pos[0] = x;
	player_data[0].pos[1] = y;
	player_data[0].pos[2] = z;
}

void RideProc(int ismario, OBJECT *obj)
{
	float posx, posy, posz, gndx, gndy, gndz;
	FVEC pos, off, new;
	SVEC rot;
	rot[0] = obj->o_rotx;
	rot[1] = obj->o_roty;
	rot[2] = obj->o_rotz;
	if (ismario)
	{
		ride_80330E20 = 0;
		MarioGetPos(&posx, &posy, &posz);
	}
	else
	{
		posx = object->o_posx;
		posy = object->o_posy;
		posz = object->o_posz;
	}
	posx += obj->o_velx;
	posz += obj->o_velz;
	if (rot[0] != 0 || rot[1] != 0 || rot[2] != 0)
	{
		UNUSED short rotx = rot[0];
		UNUSED short rotz = rot[2];
		UNUSED short angy = obj->o_shapeangy;
		FMTX m;
		if (ismario) player_data[0].ang[1] += rot[1];
		gndx = obj->o_posx;
		gndy = obj->o_posy;
		gndz = obj->o_posz;
		pos[0] = posx - gndx;
		pos[1] = posy - gndy;
		pos[2] = posz - gndz;
		rot[0] = obj->o_shapeangx - obj->o_rotx;
		rot[1] = obj->o_shapeangy - obj->o_roty;
		rot[2] = obj->o_shapeangz - obj->o_rotz;
		FMtxCoord(m, pos, rot);
		InvTransform3(m, off, pos);
		rot[0] = obj->o_shapeangx;
		rot[1] = obj->o_shapeangy;
		rot[2] = obj->o_shapeangz;
		FMtxCoord(m, pos, rot);
		MtxTransform3(m, new, off);
		posx = new[0] + gndx;
		posy = new[1] + gndy;
		posz = new[2] + gndz;
	}
	if (ismario)
	{
		MarioSetPos(posx, posy, posz);
	}
	else
	{
		object->o_posx = posx;
		object->o_posy = posy;
		object->o_posz = posz;
	}
}

void PLRideProc(void)
{
	OBJECT *obj = plride_obj;
	if (!(object_flag & OBJECT_FROZEN))
	{
		if (mario_obj && obj) RideProc(TRUE, obj);
	}
}

#if REVISION > 199606
void PLRideClear(void)
{
	plride_obj = NULL;
}
#endif
