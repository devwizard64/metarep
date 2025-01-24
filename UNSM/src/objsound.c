#include <sm64.h>

void ObjectStepSound(STEPSOUND *ss)
{
	int i = object->o_anime;
	int frame;
	switch (ss[i].flag)
	{
	case 0:
		break;
	case 1:
		if ((frame = ss[i].l) >= 0)
		{
			if (ObjectIsAnimeFrame(frame)) ObjectPlaySound(ss[i].se);
		}
		if ((frame = ss[i].r) >= 0)
		{
			if (ObjectIsAnimeFrame(frame)) ObjectPlaySound(ss[i].se);
		}
		break;
	}
}

extern OBJLANG o_1300229C[];

void ObjectMakeSound(Na_Se se)
{
	OBJECT *obj = ObjMakeHere(object, 0, o_1300229C);
	obj->o_v0 = se;
}

void ObjectLevelSound(Na_Se se)
{
	if (object->s.s.flag & SHP_ACTIVE) Na_ObjSePlay(se, object);
}

void ObjectPlaySound(Na_Se se)
{
	if (object->s.s.flag & SHP_ACTIVE) Na_ObjSePlay(se, object);
}

UNUSED static
int CalcSeVol1(float dist)
{
	int vol;
	if      (dist <  500)   vol = 127;
	else if (dist > 1500)   vol = 0;
	else                    vol = (dist-500)/1000*64 + 60;
	return vol;
}

UNUSED static
int CalcSeVol2(float dist)
{
	int vol;
	if      (dist < 1300)   vol = 127;
	else if (dist > 2300)   vol = 0;
	else                    vol = (dist-1000)/1000*64 + 60;
	return vol;
}
