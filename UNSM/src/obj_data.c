#include <sm64.h>

#include "prg_obj.c"
#include "map_obj.c"

extern O_SCRIPT o_1300091C[];
extern O_SCRIPT o_13000C44[];
extern O_SCRIPT o_13002898[];
extern O_SCRIPT o_130028CC[];
extern O_SCRIPT o_130028FC[];
extern O_SCRIPT o_1300292C[];

static SHORT cvt_ang(SHORT x)
{
	USHORT y = x & 0xFF;
	y <<= 8;
	if (y == 0x3F00) y = 0x4000;
	if (y == 0x7F00) y = 0x8000;
	if (y == 0xBF00) y = 0xC000;
	if (y == 0xFF00) y = 0x0000;
	return y;
}

static void spawn_arg(
	int shape, O_SCRIPT *script,
	SHORT px, SHORT py, SHORT pz, SHORT ay, SHORT arg
)
{
	if (script)
	{
		OBJECT *obj = obj_lib_8029E9AC(
			&object_dummy, 0, shape, script, px, py, pz, 0, cvt_ang(ay), 0
		);
		obj->o_arg = arg << 16;
	}
}

static void spawn_code(
	int shape, O_SCRIPT *script,
	SHORT px, SHORT py, SHORT pz, SHORT ay, SHORT code
)
{
	if (script)
	{
		OBJECT *obj = obj_lib_8029E9AC(
			&object_dummy, 0, shape, script, px, py, pz, 0, cvt_ang(ay), 0
		);
		obj->o_arg = code << 24;
	}
}

static void spawn_xyz(
	int shape, O_SCRIPT *script,
	SHORT px, SHORT py, SHORT pz,
	SHORT x, SHORT y, SHORT z
)
{
	OBJECT *obj = obj_lib_8029E9AC(
		&object_dummy, 0, shape, script, px, py, pz, 0, 0, 0
	);
	obj->mem[O_V5].f32 = x;
	obj->mem[O_V6].f32 = y;
	obj->mem[O_V7].f32 = z;
}

UNUSED static void spawn_old(O_SCRIPT *script, OBJ_DATA *data)
{
	OBJECT *obj;
	SHORT shape = script == o_1300091C ? S_COIN : S_NULL;
	obj = obj_lib_8029E9AC(
		&object_dummy, 0, shape, script,
		data[1], data[2], data[3], 0, cvt_ang(data[0]), 0
	);
	obj->o_prg_arg = data[4];
	obj->o_arg = (data[4] & 0xFF) >> 16;
}

void prg_obj_main(SHORT scene, OBJ_DATA *data)
{
	object_dummy.list.s.scene = scene;
	object_dummy.list.s.group = scene;
	for (;;)
	{
		UNUSED int i;
		int n;
		OBJ_DATA buf[5];
		OBJECT *obj;
		s16 shape;
		s16 arg;
		O_SCRIPT *script;
		if (*data == -1) break;
		n = (*data & 0x1FF) - P_OBJ_START;
		if (n < 0) break;
		buf[0] = (*data++ >> 9 & 0x7F) << 1;
		buf[1] = *data++;
		buf[2] = *data++;
		buf[3] = *data++;
		buf[4] = *data++;
		shape = prg_obj_data[n].shape;
		script = prg_obj_data[n].script;
		arg = prg_obj_data[n].arg;
		if (arg != 0) buf[4] = (buf[4] & 0xFF00) + (arg & 0xFF);
		if ((buf[4] >> 8 & 0xFF) != 0xFF)
		{
			obj = obj_lib_8029E9AC(
				&object_dummy, 0, shape, script,
				buf[1], buf[2], buf[3], 0, cvt_ang(buf[0]), 0
			);
			obj->o_prg_arg = buf[4];
			obj->o_arg = ((buf[4] & 0xFF) << 16) + (buf[4] & 0xFF00);
			obj->o_code = buf[4] & 0xFF;
			obj->_1F6 = 2;
			obj->_25C = data - 1;
			obj->parent = obj;
		}
	}
}

void obj_data_main(SHORT scene, OBJ_DATA *data)
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
		UNUSED OBJ_DATA buf[5];
		index = *data++;
		if (index < 0) break;
		px = *data++;
		py = *data++;
		pz = *data++;
		ay = *data++;
		switch (index)
		{
		case  0: spawn_arg(S_NULL, o_13002898, px, py, pz, ay, 0); break;
		case  1: spawn_arg(54, o_130028CC, px, py, pz, ay, 0); break;
		case  2: spawn_arg(55, o_13000C44, px, py, pz, ay, 0); break;
		case  3: spawn_arg(57, o_130028FC, px, py, pz, ay, 0); break;
		case  4: spawn_arg(58, o_1300292C, px, py, pz, ay, 0); break;
		case 20: spawn_arg(S_COIN, o_1300091C, px, py, pz, ay, 0); break;
		case 21: spawn_arg(S_COIN, o_1300091C, px, py, pz, ay, 0); break;
		default: break;
		}
	}
}

void map_obj_main(SHORT scene, MAP_DATA **data)
{
	int len;
	int i;
	len = **data; (*data)++;
	object_dummy.list.s.scene = scene;
	object_dummy.list.s.group = scene;
	for (i = 0; i < len; i++)
	{
		int n;
		short px;
		short py;
		short pz;
		MAP_DATA buf[5];
		u8 shape;
		u8 ext;
		u8 index;
		u8 code;
		O_SCRIPT *script;
		index = **data; (*data)++;
		px    = **data; (*data)++;
		py    = **data; (*data)++;
		pz    = **data; (*data)++;
		n = 0;
		for (;;)
		{
			if (map_obj_data[n].index == index) break;
			if (map_obj_data[n].index == 0xFF) {}
			n++;
		}
		shape  = map_obj_data[n].shape;
		script = map_obj_data[n].script;
		ext    = map_obj_data[n].ext;
		code   = map_obj_data[n].code;
		switch (ext)
		{
		case M_EXT_NULL:
			spawn_arg(shape, script, px, py, pz, 0, 0);
			break;
		case M_EXT_AY:
			buf[0] = **data; (*data)++;
			spawn_arg(shape, script, px, py, pz, buf[0], 0);
			break;
		case M_EXT_AY_ARG:
			buf[0] = **data; (*data)++;
			buf[1] = **data; (*data)++;
			spawn_arg(shape, script, px, py, pz, buf[0], buf[1]);
			break;
		case M_EXT_XYZ:
			buf[0] = **data; (*data)++;
			buf[1] = **data; (*data)++;
			buf[2] = **data; (*data)++;
			spawn_xyz(shape, script, px, py, pz, buf[0], buf[1], buf[2]);
			break;
		case M_EXT_AY_CODE:
			buf[0] = **data; (*data)++;
			spawn_code(shape, script, px, py, pz, buf[0], code);
			break;
		default:
			break;
		}
	}
}
