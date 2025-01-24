#include <sm64.h>

#include "tagobj.c"
#include "mapobj.c"

extern OBJLANG o_coin[];
extern OBJLANG o_13000C44[];
extern OBJLANG o_13002898[];
extern OBJLANG o_130028CC[];
extern OBJLANG o_130028FC[];
extern OBJLANG o_1300292C[];

static SHORT TagAng(SHORT x)
{
	USHORT y = x & 0xFF;
	y <<= 8;
	if (y == 0x3F00) y = 0x4000;
	if (y == 0x7F00) y = 0x8000;
	if (y == 0xBF00) y = 0xC000;
	if (y == 0xFF00) y = 0x0000;
	return y;
}

static void TagEnterCode(
	int shape, OBJLANG *script,
	SHORT posx, SHORT posy, SHORT posz, SHORT angy, SHORT code
)
{
	if (script)
	{
		OBJECT *obj = ObjMakeAt(
			&object_dummy, 0, shape, script,
			posx, posy, posz, 0, TagAng(angy), 0
		);
		obj->o_actorinfo = code << 16;
	}
}

static void TagEnterArg(
	int shape, OBJLANG *script,
	SHORT posx, SHORT posy, SHORT posz, SHORT angy, SHORT arg
)
{
	if (script)
	{
		OBJECT *obj = ObjMakeAt(
			&object_dummy, 0, shape, script,
			posx, posy, posz, 0, TagAng(angy), 0
		);
		obj->o_actorinfo = arg << 24;
	}
}

static void TagEnterXYZ(
	int shape, OBJLANG *script,
	SHORT posx, SHORT posy, SHORT posz,
	SHORT x, SHORT y, SHORT z
)
{
	OBJECT *obj = ObjMakeAt(
		&object_dummy, 0, shape, script, posx, posy, posz, 0, 0, 0
	);
	obj->o_f5 = x;
	obj->o_f6 = y;
	obj->o_f7 = z;
}

UNUSED
static void TagEnterOLD(OBJLANG *script, TAG *tag)
{
	OBJECT *obj;
	SHORT shape = script == o_coin ? S_COIN : S_NULL;
	obj = ObjMakeAt(
		&object_dummy, 0, shape, script,
		tag[1], tag[2], tag[3], 0, TagAng(tag[0]), 0
	);
	obj->o_taginfo = tag[4];
	obj->o_actorinfo = (tag[4] & 0xFF) >> 16;
}

void TagObjLoad(SHORT scene, TAG *tag)
{
	object_dummy.s.scene = scene;
	object_dummy.s.group = scene;
	for (;;)
	{
		UNUSED int i;
		int n;
		TAG buf[5];
		OBJECT *obj;
		s16 shape, code;
		OBJLANG *script;
		if (*tag == -1) break;
		n = (*tag & 0x1FF) - TAG_START;
		if (n < 0) break;
		buf[0] = (*tag++ >> 9 & 0x7F) << 1;
		buf[1] = *tag++;
		buf[2] = *tag++;
		buf[3] = *tag++;
		buf[4] = *tag++;
		shape = tagobjtab[n].shape;
		script = tagobjtab[n].script;
		code = tagobjtab[n].code;
		if (code) buf[4] = (buf[4] & 0xFF00) + (code & 0xFF);
		if ((buf[4] >> 8 & 0xFF) != 0xFF)
		{
			obj = ObjMakeAt(
				&object_dummy, 0, shape, script,
				buf[1], buf[2], buf[3], 0, TagAng(buf[0]), 0
			);
			obj->o_taginfo = buf[4];
			obj->o_actorinfo = ((buf[4] & 0xFF) << 16) + (buf[4] & 0xFF00);
			obj->o_code = buf[4] & 0xFF;
			obj->actor_type = ACTORTYPE_16;
			obj->actor_flag = tag - 1;
			obj->parent = obj;
		}
	}
}

void TagLoad(SHORT scene, TAG *tag)
{
	object_dummy.s.scene = scene;
	object_dummy.s.group = scene;
	for (;;)
	{
		UNUSED int i;
		UNUSED OBJECT *obj;
		short posx, posy, posz, index, angy;
		UNUSED TAG buf[5];
		index = *tag++;
		if (index < 0) break;
		posx = *tag++;
		posy = *tag++;
		posz = *tag++;
		angy = *tag++;
		switch (index)
		{
		case 0:
			TagEnterCode(S_NULL, o_13002898, posx, posy, posz, angy, 0);
			break;
		case 1:
			TagEnterCode(54, o_130028CC, posx, posy, posz, angy, 0);
			break;
		case 2:
			TagEnterCode(55, o_13000C44, posx, posy, posz, angy, 0);
			break;
		case 3:
			TagEnterCode(57, o_130028FC, posx, posy, posz, angy, 0);
			break;
		case 4:
			TagEnterCode(58, o_1300292C, posx, posy, posz, angy, 0);
			break;
		case 20:
			TagEnterCode(S_COIN, o_coin, posx, posy, posz, angy, 0);
			break;
		case 21:
			TagEnterCode(S_COIN, o_coin, posx, posy, posz, angy, 0);
			break;
		default:
			break;
		}
	}
}

void MapObjLoad(SHORT scene, MAP **map)
{
	int len;
	int i;
	len = **map; (*map)++;
	object_dummy.s.scene = scene;
	object_dummy.s.group = scene;
	for (i = 0; i < len; i++)
	{
		int n;
		MAP posx, posy, posz;
		MAP buf[5];
		u8 shape, ext, index, arg;
		OBJLANG *script;
		index = **map; (*map)++;
		posx  = **map; (*map)++;
		posy  = **map; (*map)++;
		posz  = **map; (*map)++;
		n = 0;
		for (;;)
		{
			if (mapobjtab[n].index == index) break;
			if (mapobjtab[n].index == 0xFF) {}
			n++;
		}
		shape  = mapobjtab[n].shape;
		script = mapobjtab[n].script;
		ext    = mapobjtab[n].ext;
		arg    = mapobjtab[n].arg;
		switch (ext)
		{
		case MAP_EXT_NULL:
			TagEnterCode(shape, script, posx, posy, posz, 0, 0);
			break;
		case MAP_EXT_ANG:
			buf[0] = **map; (*map)++;
			TagEnterCode(shape, script, posx, posy, posz, buf[0], 0);
			break;
		case MAP_EXT_ANG_CODE:
			buf[0] = **map; (*map)++;
			buf[1] = **map; (*map)++;
			TagEnterCode(shape, script, posx, posy, posz, buf[0], buf[1]);
			break;
		case MAP_EXT_XYZ:
			buf[0] = **map; (*map)++;
			buf[1] = **map; (*map)++;
			buf[2] = **map; (*map)++;
			TagEnterXYZ(
				shape, script, posx, posy, posz, buf[0], buf[1], buf[2]
			);
			break;
		case MAP_EXT_ANG_ARG:
			buf[0] = **map; (*map)++;
			TagEnterArg(shape, script, posx, posy, posz, buf[0], arg);
			break;
		default:
			break;
		}
	}
}
