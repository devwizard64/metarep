#ifndef SCRIPT

static void Player_CopyInfo(void)
{
	int i = 0;
	if (object != mario_obj) i++;
	object->o_velx = player_data[i].vel[0];
	object->o_vely = player_data[i].vel[1];
	object->o_velz = player_data[i].vel[2];
	object->o_posx = player_data[i].pos[0];
	object->o_posy = player_data[i].pos[1];
	object->o_posz = player_data[i].pos[2];
	object->o_angx = object->s.ang[0];
	object->o_angy = object->s.ang[1];
	object->o_angz = object->s.ang[2];
	object->o_shapeangx = object->s.ang[0];
	object->o_shapeangy = object->s.ang[1];
	object->o_shapeangz = object->s.ang[2];
	object->o_rotx = player_data[i].rot[0];
	object->o_roty = player_data[i].rot[1];
	object->o_rotz = player_data[i].rot[2];
}

typedef struct pl_effect
{
	u32 code;
	u32 flag;
	u8 shape;
	OBJLANG *script;
}
PL_EFFECT;

extern OBJLANG o_130002B8[];
extern OBJLANG o_13000428[];
extern OBJLANG o_13000A54[];
extern OBJLANG o_13000A98[];
extern OBJLANG o_13000AD8[];
extern OBJLANG o_13000D98[];
extern OBJLANG o_13000E24[];
extern OBJLANG o_13000E3C[];
extern OBJLANG o_13000E58[];
extern OBJLANG o_130011EC[];
extern OBJLANG o_13001390[];
extern OBJLANG o_130024AC[];
extern OBJLANG o_13002B08[];
extern OBJLANG o_13002C14[];
extern OBJLANG o_13002CE0[];
extern OBJLANG o_13002D50[];
extern OBJLANG o_13002D7C[];
extern OBJLANG o_13002DC0[];

static PL_EFFECT pl_effecttab[] =
{
	{PE_00000001, 0x00000001, S_WHITEPUFF, o_130024AC},
	{PE_00000002, 0x00040000, S_NULL, o_13000A54},
	{PE_00000010, 0x00000010, S_NULL, o_13000A98},
	{PE_00000008, 0x00000008, S_SPARKLE, o_13002B08},
	{PE_00000020, 0x00000020, S_BUBBLE_A, o_130002B8},
	{PE_00000040, 0x00000040, S_SPLASH, o_13002C14},
	{PE_00000080, 0x00000080, S_RIPPLE_STOP, o_13002CE0},
	{PE_00000200, 0x00000200, S_DROPLET, o_13000428},
	{PE_00000400, 0x00000400, S_RIPPLE_MOVE, o_13002DC0},
	{PE_00000800, 0x00000800, S_FLAME, o_130011EC},
	{PE_00000100, 0x00000100, S_NULL, o_13002D50},
	{PE_00001000, 0x00001000, S_NULL, o_13002D7C},
	{PE_00002000, 0x00002000, S_NULL, o_13001390},
	{PE_00004000, 0x00010000, S_NULL, o_13000E58},
	{PE_00020000, 0x00020000, S_NULL, o_13000D98},
	{PE_00008000, 0x00004000, S_NULL, o_13000E3C},
	{PE_00010000, 0x00008000, S_NULL, o_13000E24},
	{PE_00040000, 0x00080000, S_NULL, o_13000AD8},
	{0},
};

static void Player_SetEffect(u32 flag, SHORT shape, OBJLANG *script)
{
	if (!(object->o_effect & flag))
	{
		OBJECT *obj;
		object->o_effect |= flag;
		obj = ObjMake(object, 0, shape, script);
		ObjCopyCoord(obj, object);
	}
}

void Mario_Proc(void)
{
	u32 flag = 0;
	int i;
	flag = MarioExec(object);
	object->o_v0 = flag;
	Player_CopyInfo();
	i = 0;
	while (pl_effecttab[i].code)
	{
		if (pl_effecttab[i].code & flag) Player_SetEffect(
			pl_effecttab[i].flag,
			pl_effecttab[i].shape,
			pl_effecttab[i].script
		);
		i++;
	}
}
