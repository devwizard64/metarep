#include <sm64.h>

void objsfx_802CA040(OBJ_SFX *sfx)
{
	int i = object->o_anime_index;
	int frame;
	switch (sfx[i].flag)
	{
	case 0:
		break;
	case 1:
		if ((frame = sfx[i].l) >= 0)
		{
			if (objlib_802A0008(frame)) objsfx_802CA1E0(sfx[i].se);
		}
		if ((frame = sfx[i].r) >= 0)
		{
			if (objlib_802A0008(frame)) objsfx_802CA1E0(sfx[i].se);
		}
		break;
	}
}

extern O_SCRIPT o_1300229C[];

void objsfx_802CA144(NA_SE se)
{
	OBJECT *obj = objlib_8029EDCC(object, 0, o_1300229C);
	obj->mem[O_V0].i = se;
}

void objsfx_802CA190(NA_SE se)
{
	if (object->list.s.s.flag & S_FLAG_ACTIVE) Na_SE_obj(se, object);
}

void objsfx_802CA1E0(NA_SE se)
{
	if (object->list.s.s.flag & S_FLAG_ACTIVE) Na_SE_obj(se, object);
}

UNUSED static
int objsfx_802CA230(float x)
{
	int y;
	if      (x <  500) y = 127;
	else if (x > 1500) y = 0;
	else               y = (x-500)/1000*64 + 60;
	return y;
}

UNUSED static
int objsfx_802CA2D4(float x)
{
	int y;
	if      (x < 1300) y = 127;
	else if (x > 2300) y = 0;
	else               y = (x-1000)/1000*64 + 60;
	return y;
}
