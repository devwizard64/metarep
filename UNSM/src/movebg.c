#include <sm64.h>

static short movebg_80330E20 = 0;
UNUSED static int movebg_80330E24[4] = {0};
static OBJECT *mario_movebg = NULL;

void MarioFindMoveBG(void)
{
	BGFACE *ground;
	UNUSED OBJECT *movebg;
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
		mario_movebg = NULL;
		mario_obj->movebg = NULL;
		break;
	case 0:
		if (ground && ground->obj)
		{
			mario_movebg = ground->obj;
			mario_obj->movebg = ground->obj;
		}
		else
		{
			mario_movebg = NULL;
			mario_obj->movebg = NULL;
		}
		break;
	}
}

void Player1GetPos(float *x, float *y, float *z)
{
	*x = player_data[0].pos[0];
	*y = player_data[0].pos[1];
	*z = player_data[0].pos[2];
}

void Player1SetPos(float x, float y, float z)
{
	player_data[0].pos[0] = x;
	player_data[0].pos[1] = y;
	player_data[0].pos[2] = z;
}

void MoveBGProc(int flag, OBJECT *movebg)
{
	float posx, posy, posz, gndx, gndy, gndz;
	FVEC pos, off, new;
	SVEC rot;
	rot[0] = movebg->o_rotx;
	rot[1] = movebg->o_roty;
	rot[2] = movebg->o_rotz;
	if (flag)
	{
		movebg_80330E20 = 0;
		Player1GetPos(&posx, &posy, &posz);
	}
	else
	{
		posx = object->o_posx;
		posy = object->o_posy;
		posz = object->o_posz;
	}
	posx += movebg->o_velx;
	posz += movebg->o_velz;
	if (rot[0] != 0 || rot[1] != 0 || rot[2] != 0)
	{
		UNUSED short rotx = rot[0];
		UNUSED short rotz = rot[2];
		UNUSED short angy = movebg->o_shapeangy;
		FMTX m;
		if (flag) player_data[0].ang[1] += rot[1];
		gndx = movebg->o_posx;
		gndy = movebg->o_posy;
		gndz = movebg->o_posz;
		pos[0] = posx - gndx;
		pos[1] = posy - gndy;
		pos[2] = posz - gndz;
		rot[0] = movebg->o_shapeangx - movebg->o_rotx;
		rot[1] = movebg->o_shapeangy - movebg->o_roty;
		rot[2] = movebg->o_shapeangz - movebg->o_rotz;
		FMtxCoord(m, pos, rot);
		InvTransform3(m, off, pos);
		rot[0] = movebg->o_shapeangx;
		rot[1] = movebg->o_shapeangy;
		rot[2] = movebg->o_shapeangz;
		FMtxCoord(m, pos, rot);
		MtxTransform3(m, new, off);
		posx = new[0] + gndx;
		posy = new[1] + gndy;
		posz = new[2] + gndz;
	}
	if (flag)
	{
		Player1SetPos(posx, posy, posz);
	}
	else
	{
		object->o_posx = posx;
		object->o_posy = posy;
		object->o_posz = posz;
	}
}

void MarioProcMoveBG(void)
{
	OBJECT *movebg = mario_movebg;
	if (!(object_flag & OBJECT_FROZEN))
	{
		if (mario_obj && movebg) MoveBGProc(TRUE, movebg);
	}
}

#if REVISION >= 199609
void MarioClearMoveBG(void)
{
	mario_movebg = NULL;
}
#endif
