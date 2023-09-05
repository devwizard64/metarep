#include <sm64.h>

#include "tag_obj.c"
#include "map_obj.c"

extern O_SCRIPT o_1300091C[];
extern O_SCRIPT o_13000C44[];
extern O_SCRIPT o_13002898[];
extern O_SCRIPT o_130028CC[];
extern O_SCRIPT o_130028FC[];
extern O_SCRIPT o_1300292C[];

static SHORT tag_ang(SHORT x)
{
	USHORT y = x & 0xFF;
	y <<= 8;
	if (y == 0x3F00) y = 0x4000;
	if (y == 0x7F00) y = 0x8000;
	if (y == 0xBF00) y = 0xC000;
	if (y == 0xFF00) y = 0x0000;
	return y;
}

static void tag_spawn_arg(
	int shape, O_SCRIPT *script,
	SHORT px, SHORT py, SHORT pz, SHORT ay, SHORT arg
)
{
	if (script)
	{
		OBJECT *obj = objlib_8029E9AC(
			&object_dummy, 0, shape, script, px, py, pz, 0, tag_ang(ay), 0
		);
		obj->o_arg = arg << 16;
	}
}

static void tag_spawn_code(
	int shape, O_SCRIPT *script,
	SHORT px, SHORT py, SHORT pz, SHORT ay, SHORT code
)
{
	if (script)
	{
		OBJECT *obj = objlib_8029E9AC(
			&object_dummy, 0, shape, script, px, py, pz, 0, tag_ang(ay), 0
		);
		obj->o_arg = code << 24;
	}
}

static void tag_spawn_xyz(
	int shape, O_SCRIPT *script,
	SHORT px, SHORT py, SHORT pz,
	SHORT x, SHORT y, SHORT z
)
{
	OBJECT *obj = objlib_8029E9AC(
		&object_dummy, 0, shape, script, px, py, pz, 0, 0, 0
	);
	obj->mem[O_V5].f = x;
	obj->mem[O_V6].f = y;
	obj->mem[O_V7].f = z;
}

UNUSED
static void tag_spawn_old(O_SCRIPT *script, TAG *tag)
{
	OBJECT *obj;
	SHORT shape = script == o_1300091C ? S_COIN : S_NULL;
	obj = objlib_8029E9AC(
		&object_dummy, 0, shape, script,
		tag[1], tag[2], tag[3], 0, tag_ang(tag[0]), 0
	);
	obj->o_tag_arg = tag[4];
	obj->o_arg = (tag[4] & 0xFF) >> 16;
}

void tag_obj_load(SHORT scene, TAG *tag)
{
	object_dummy.list.s.scene = scene;
	object_dummy.list.s.group = scene;
	for (;;)
	{
		UNUSED int i;
		int n;
		TAG buf[5];
		OBJECT *obj;
		s16 shape;
		s16 arg;
		O_SCRIPT *script;
		if (*tag == -1) break;
		n = (*tag & 0x1FF) - TAG_START;
		if (n < 0) break;
		buf[0] = (*tag++ >> 9 & 0x7F) << 1;
		buf[1] = *tag++;
		buf[2] = *tag++;
		buf[3] = *tag++;
		buf[4] = *tag++;
		shape = tag_obj_table[n].shape;
		script = tag_obj_table[n].script;
		arg = tag_obj_table[n].arg;
		if (arg != 0) buf[4] = (buf[4] & 0xFF00) + (arg & 0xFF);
		if ((buf[4] >> 8 & 0xFF) != 0xFF)
		{
			obj = objlib_8029E9AC(
				&object_dummy, 0, shape, script,
				buf[1], buf[2], buf[3], 0, tag_ang(buf[0]), 0
			);
			obj->o_tag_arg = buf[4];
			obj->o_arg = ((buf[4] & 0xFF) << 16) + (buf[4] & 0xFF00);
			obj->o_code = buf[4] & 0xFF;
			obj->_1F6 = 2;
			obj->_25C = tag - 1;
			obj->parent = obj;
		}
	}
}

void tag_load(SHORT scene, TAG *tag)
{
	object_dummy.list.s.scene = scene;
	object_dummy.list.s.group = scene;
	for (;;)
	{
		UNUSED int i;
		UNUSED OBJECT *obj;
		short px;
		short py;
		short pz;
		short index;
		short ay;
		UNUSED TAG buf[5];
		index = *tag++;
		if (index < 0) break;
		px = *tag++;
		py = *tag++;
		pz = *tag++;
		ay = *tag++;
		switch (index)
		{
		case  0: tag_spawn_arg(S_NULL, o_13002898, px, py, pz, ay, 0); break;
		case  1: tag_spawn_arg(54, o_130028CC, px, py, pz, ay, 0); break;
		case  2: tag_spawn_arg(55, o_13000C44, px, py, pz, ay, 0); break;
		case  3: tag_spawn_arg(57, o_130028FC, px, py, pz, ay, 0); break;
		case  4: tag_spawn_arg(58, o_1300292C, px, py, pz, ay, 0); break;
		case 20: tag_spawn_arg(S_COIN, o_1300091C, px, py, pz, ay, 0); break;
		case 21: tag_spawn_arg(S_COIN, o_1300091C, px, py, pz, ay, 0); break;
		default: break;
		}
	}
}

void map_obj_load(SHORT scene, MAP **map)
{
	int len;
	int i;
	len = **map; (*map)++;
	object_dummy.list.s.scene = scene;
	object_dummy.list.s.group = scene;
	for (i = 0; i < len; i++)
	{
		int n;
		short px;
		short py;
		short pz;
		MAP buf[5];
		u8 shape;
		u8 ext;
		u8 index;
		u8 code;
		O_SCRIPT *script;
		index = **map; (*map)++;
		px    = **map; (*map)++;
		py    = **map; (*map)++;
		pz    = **map; (*map)++;
		n = 0;
		for (;;)
		{
			if (map_obj_table[n].index == index) break;
			if (map_obj_table[n].index == 0xFF) {}
			n++;
		}
		shape  = map_obj_table[n].shape;
		script = map_obj_table[n].script;
		ext    = map_obj_table[n].ext;
		code   = map_obj_table[n].code;
		switch (ext)
		{
		case MAP_EXT_NULL:
			tag_spawn_arg(shape, script, px, py, pz, 0, 0);
			break;
		case MAP_EXT_AY:
			buf[0] = **map; (*map)++;
			tag_spawn_arg(shape, script, px, py, pz, buf[0], 0);
			break;
		case MAP_EXT_AY_ARG:
			buf[0] = **map; (*map)++;
			buf[1] = **map; (*map)++;
			tag_spawn_arg(shape, script, px, py, pz, buf[0], buf[1]);
			break;
		case MAP_EXT_XYZ:
			buf[0] = **map; (*map)++;
			buf[1] = **map; (*map)++;
			buf[2] = **map; (*map)++;
			tag_spawn_xyz(shape, script, px, py, pz, buf[0], buf[1], buf[2]);
			break;
		case MAP_EXT_AY_CODE:
			buf[0] = **map; (*map)++;
			tag_spawn_code(shape, script, px, py, pz, buf[0], code);
			break;
		default:
			break;
		}
	}
}
