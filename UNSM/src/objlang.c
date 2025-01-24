#include <sm64.h>

#define OBJ_UCHARA(i)   ((u8)(object_pc[i] >> 24 & 0xFF))
#define OBJ_UCHARB(i)   ((u8)(object_pc[i] >> 16 & 0xFF))
#define OBJ_UCHARC(i)   ((u8)(object_pc[i] >>  8 & 0xFF))
#define OBJ_UCHARD(i)   ((u8)(object_pc[i] >>  0 & 0xFF))
#define OBJ_SHORTH(i)   ((short)(object_pc[i] >> 16))
#define OBJ_SHORTL(i)   ((short)(object_pc[i] & 0xFFFF))
#define OBJ_INT(i)      ((int)object_pc[i])
#define OBJ_PTR(i)      ((void *)object_pc[i])
#define OBJ_CALL(i)     ((OBJCALL *)object_pc[i])

#define OBJ_CMD         (object_pc[0] >> 24)

UNUSED
static void ObjectScriptEntry(OBJLANG *script)
{
	object_pc = SegmentToVirtual(script);
	object->sp = 0;
}

u16 Rand(void)
{
	static u16 seed;
	USHORT a, b;
	if (seed == 0x560A) seed = 0;
	a = (seed & 0xFF) << 8;
	a ^= seed;
	seed = ((a & 0x00FF) << 8) + ((a & 0xFF00) >> 8);
	a = ((a & 0xFF) << 1) ^ seed;
	b = (a >> 1) ^ 0xFF80;
	if (!(a & 1))
	{
		if (b == 0xAA55)    seed = 0;
		else                seed = b ^ 0x1FF4;
	}
	else
	{
		seed = b ^ 0x8180;
	}
	return seed;
}

float RandF(void)
{
	float x = Rand();
	return x / 65536.0;
}

int RandSign(void)
{
	if (Rand() >= 0x7FFF)   return 1;
	else                    return -1;
}

static void ObjSetShapeCoord(OBJECT *obj)
{
	obj->s.pos[0] = obj->o_posx;
	obj->s.pos[1] = obj->o_posy + obj->o_shapeoff;
	obj->s.pos[2] = obj->o_posz;
	obj->s.ang[0] = obj->o_shapeangx & 0xFFFF;
	obj->s.ang[1] = obj->o_shapeangy & 0xFFFF;
	obj->s.ang[2] = obj->o_shapeangz & 0xFFFF;
}

static void ObjectPush(unsigned long x)
{
	object->stack[object->sp] = x;
	object->sp++;
}

static unsigned long ObjectPull(void)
{
	unsigned long x;
	object->sp--;
	x = object->stack[object->sp];
	return x;
}

UNUSED
static void ObjectError(void)
{
	for (;;);
}

static int ObjCmdHide(void)
{
	ObjectHide();
	object_pc += 1;
	return 0;
}

static int ObjCmdClrActive(void)
{
	object->s.s.flag &= ~SHP_ACTIVE;
	object_pc += 1;
	return 0;
}

static int ObjCmdBillboard(void)
{
	object->s.s.flag |= SHP_BILLBOARD;
	object_pc += 1;
	return 0;
}

static int ObjCmdShape(void)
{
	int shape = OBJ_SHORTL(0);
	object->s.shape = shape_table[shape];
	object_pc += 1;
	return 0;
}

static int ObjCmdMakeObj(void)
{
	int shape = OBJ_INT(1);
	OBJLANG *script = OBJ_PTR(2);
	OBJECT *obj = ObjMake(object, 0, shape, script);
	ObjCopyCoord(obj, object);
	object_pc += 3;
	return 0;
}

static int ObjCmdMakeChild(void)
{
	int shape = OBJ_INT(1);
	OBJLANG *script = OBJ_PTR(2);
	OBJECT *obj = ObjMake(object, 0, shape, script);
	ObjCopyCoord(obj, object);
	object->child = obj;
	object_pc += 3;
	return 0;
}

static int ObjCmdMakeObjCode(void)
{
	int code = OBJ_SHORTL(0);
	int shape = OBJ_INT(1);
	OBJLANG *script = OBJ_PTR(2);
	OBJECT *obj = ObjMake(object, 0, shape, script);
	ObjCopyCoord(obj, object);
	obj->o_code = code;
	object_pc += 3;
	return 0;
}

static int ObjCmdDestroy(void)
{
	object->flag = 0;
	return 1;
}

static int ObjCmdExit(void)
{
	return 1;
}

static int ObjCmdEnd(void)
{
	return 1;
}

static int ObjCmdCall(void)
{
	OBJLANG *pc;
	object_pc += 1;
	ObjectPush((unsigned long)(object_pc+1));
	pc = SegmentToVirtual(OBJ_PTR(0));
	object_pc = pc;
	return 0;
}

static int ObjCmdReturn(void)
{
	object_pc = (void *)ObjectPull();
	return 0;
}

static int ObjCmdSleep(void)
{
	SHORT time = OBJ_SHORTL(0);
	if (object->sleep < time-1)
	{
		object->sleep++;
	}
	else
	{
		object->sleep = 0;
		object_pc += 1;
	}
	return 1;
}

static int ObjCmdMemSleep(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	int time = object->mem[mem].i;
	if (object->sleep < time-1)
	{
		object->sleep++;
	}
	else
	{
		object->sleep = 0;
		object_pc += 1;
	}
	return 1;
}

static int ObjCmdJump(void)
{
	object_pc += 1;
	object_pc = SegmentToVirtual(OBJ_PTR(0));
	return 0;
}

static int ObjCmdFor2(void)
{
	unsigned long count = OBJ_UCHARB(0);
	ObjectPush((unsigned long)(object_pc+1));
	ObjectPush(count);
	object_pc += 1;
	return 0;
}

static int ObjCmdFor(void)
{
	unsigned long count = OBJ_SHORTL(0);
	ObjectPush((unsigned long)(object_pc+1));
	ObjectPush(count);
	object_pc += 1;
	return 0;
}

static int ObjCmdFend(void)
{
	unsigned long count = ObjectPull();
	count--;
	if (count > 0)
	{
		object_pc = (void *)ObjectPull();
		ObjectPush((unsigned long)object_pc);
		ObjectPush(count);
	}
	else
	{
		ObjectPull();
		object_pc += 1;
	}
	return 1;
}

static int ObjCmdFcontinue(void)
{
	unsigned long count = ObjectPull();
	count--;
	if (count > 0)
	{
		object_pc = (void *)ObjectPull();
		ObjectPush((unsigned long)object_pc);
		ObjectPush(count);
	}
	else
	{
		ObjectPull();
		object_pc += 1;
	}
	return 0;
}

static int ObjCmdWhile(void)
{
	ObjectPush((unsigned long)(object_pc+1));
	object_pc += 1;
	return 0;
}

static int ObjCmdWend(void)
{
	object_pc = (void *)ObjectPull();
	ObjectPush((unsigned long)object_pc);
	return 1;
}

static int ObjCmdCallback(void)
{
	OBJCALL *callback = OBJ_CALL(1);
	callback();
	object_pc += 2;
	return 0;
}

static int ObjCmdSetF(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	float x = OBJ_SHORTL(0);
	object->mem[mem].f = x;
	object_pc += 1;
	return 0;
}

static int ObjCmdSetI(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	SHORT x = OBJ_SHORTL(0);
	object->mem[mem].i = x;
	object_pc += 1;
	return 0;
}

static int ObjCmdSetS(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	int x = OBJ_SHORTL(1);
	object->mem[mem].i = x;
	object_pc += 2;
	return 0;
}

static int ObjCmdSetRandF(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	float add = OBJ_SHORTL(0);
	float mul = OBJ_SHORTH(1);
	object->mem[mem].f = add + mul*RandF();
	object_pc += 2;
	return 0;
}

static int ObjCmdSetRandI(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	int add = OBJ_SHORTL(0);
	int mul = OBJ_SHORTH(1);
	object->mem[mem].i = add + (int)(mul*RandF());
	object_pc += 2;
	return 0;
}

static int ObjCmdSetRandA(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	int add = OBJ_SHORTL(0);
	int shift = OBJ_SHORTH(1);
	object->mem[mem].i = add + (Rand() >> shift);
	object_pc += 2;
	return 0;
}

static int ObjCmdAddRandF(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	float add = OBJ_SHORTL(0);
	float mul = OBJ_SHORTH(1);
	object->mem[mem].f = object->mem[mem].f + add + mul*RandF();
	object_pc += 2;
	return 0;
}

static int ObjCmdAddRandA(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	int add = OBJ_SHORTL(0);
	int shift = OBJ_SHORTH(1);
	int x = Rand();
	object->mem[mem].i = object->mem[mem].i + add + (x >> shift);
	object_pc += 2;
	return 0;
}

static int ObjCmdAddF(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	float val = OBJ_SHORTL(0);
	object->mem[mem].f += val;
	object_pc += 1;
	return 0;
}

static int ObjCmdAddI(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	SHORT val = OBJ_SHORTL(0);
	object->mem[mem].i += val;
	object_pc += 1;
	return 0;
}

static int ObjCmdSetFlag(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	int flag = OBJ_SHORTL(0);
	flag &= 0xFFFF;
	object->mem[mem].i |= flag;
	object_pc += 1;
	return 0;
}

static int ObjCmdClrFlag(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	int flag = OBJ_SHORTL(0);
	flag = (flag & 0xFFFF) ^ 0xFFFF;
	object->mem[mem].i &= flag;
	object_pc += 1;
	return 0;
}

static int ObjCmdPtr(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	object->mem[mem].p = OBJ_PTR(1);
	object_pc += 2;
	return 0;
}

static int ObjCmdAnime(void)
{
	int anime = OBJ_UCHARB(0);
	ANIME **animetab = object->o_animep;
	SObjSetAnime(&object->s, &animetab[anime]);
	object_pc += 1;
	return 0;
}

static int ObjCmdGround(void)
{
	float x = object->o_posx;
	float y = object->o_posy;
	float z = object->o_posz;
	float ground_y = BGCheckGroundY(x, y+200, z);
	object->o_posy = ground_y;
	object->o_move |= OM_TOUCH;
	object_pc += 1;
	return 0;
}

static int ObjCmd24(void)
{
	UNUSED UCHAR mem = OBJ_UCHARB(0);
	object_pc += 1;
	return 0;
}

static int ObjCmd26(void)
{
	UNUSED UCHAR mem = OBJ_UCHARB(0);
	object_pc += 1;
	return 0;
}

static int ObjCmd25(void)
{
	UNUSED UCHAR mem = OBJ_UCHARB(0);
	object_pc += 1;
	return 0;
}

static int ObjCmdMemAddF(void)
{
	int mem = OBJ_UCHARB(0);
	int a = OBJ_UCHARC(0);
	int b = OBJ_UCHARD(0);
	object->mem[mem].f = object->mem[a].f + object->mem[b].f;
	object_pc += 1;
	return 0;
}

static int ObjCmdMemAddI(void)
{
	int mem = OBJ_UCHARB(0);
	int a = OBJ_UCHARC(0);
	int b = OBJ_UCHARD(0);
	object->mem[mem].i = object->mem[a].i + object->mem[b].i;
	object_pc += 1;
	return 0;
}

static int ObjCmdHitBox(void)
{
	SHORT radius = OBJ_SHORTH(1);
	SHORT height = OBJ_SHORTL(1);
	object->hit_r = radius;
	object->hit_h = height;
	object_pc += 2;
	return 0;
}

static int ObjCmdDmgBox(void)
{
	SHORT radius = OBJ_SHORTH(1);
	SHORT height = OBJ_SHORTL(1);
	object->dmg_r = radius;
	object->dmg_h = height;
	object_pc += 2;
	return 0;
}

static int ObjCmdHitBoxOff(void)
{
	SHORT radius = OBJ_SHORTH(1);
	SHORT height = OBJ_SHORTL(1);
	SHORT offset = OBJ_SHORTH(2);
	object->hit_r = radius;
	object->hit_h = height;
	object->hit_offset = offset;
	object_pc += 3;
	return 0;
}

static int ObjCmd36(void)
{
	UNUSED SHORT mem = OBJ_UCHARB(0);
	UNUSED SHORT x = OBJ_SHORTL(0);
	object_pc += 1;
	return 0;
}

extern OBJLANG o_signpost[];
extern OBJLANG o_13004FD4[];
extern OBJLANG o_13005024[];

static int ObjCmdInit(void)
{
	if (ObjectHasScript(o_13004FD4)) ObjectInitArea();
	if (ObjectHasScript(o_13005024)) ObjectInitArea();
	if (ObjectHasScript(o_signpost)) object->o_checkdist = 150;
	object_pc += 1;
	return 0;
}

UNUSED
static void ObjLangSetRandTbl(int len)
{
	UCHAR mem = OBJ_UCHARB(0);
	int table[16];
	int i;
	for (i = 0; i <= len/2; i += 2)
	{
		table[i+0] = OBJ_SHORTH(1+i);
		table[i+1] = OBJ_SHORTL(1+i);
	}
	object->mem[mem].i = table[(int)(RandF() * len)];
}

static int ObjCmdMap(void)
{
	MAP *map = SegmentToVirtual(OBJ_PTR(1));
	object->map = map;
	object_pc += 2;
	return 0;
}

static int ObjCmdSavePos(void)
{
	object->o_savex = object->o_posx;
	object->o_savey = object->o_posy;
	object->o_savez = object->o_posz;
	object_pc += 1;
	return 0;
}

static int ObjCmdHitType(void)
{
	object->o_hit_type = OBJ_INT(1);
	object_pc += 2;
	return 0;
}

static int ObjCmdHitFlag(void)
{
	object->o_hit_flag = OBJ_INT(1);
	object_pc += 2;
	return 0;
}

static int ObjCmdScale(void)
{
	UNUSED UCHAR mem = OBJ_UCHARB(0);
	SHORT scale = OBJ_SHORTL(0);
	ObjectSetScale((float)scale / 100);
	object_pc += 1;
	return 0;
}

static int ObjCmdPhysics(void)
{
	UNUSED float g, h;
	object->o_wall_r    = OBJ_SHORTH(1);
	object->o_gravity   = OBJ_SHORTL(1) / (float)100;
	object->o_density   = OBJ_SHORTH(2) / (float)100;
	object->o_drag      = OBJ_SHORTL(2) / (float)100;
	object->o_friction  = OBJ_SHORTH(3) / (float)100;
	object->o_bounce    = OBJ_SHORTL(3) / (float)100;
	g                   = OBJ_SHORTH(4) / (float)100;
	h                   = OBJ_SHORTL(4) / (float)100;
	object_pc += 5;
	return 0;
}

static int ObjCmdMemClrParentFlag(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	int flag = OBJ_INT(1);
	flag ^= 0xFFFFFFFF;
	object->parent->mem[mem].i &= flag;
	object_pc += 2;
	return 0;
}

static int ObjCmdSplash(void)
{
	SPLASH *splash = OBJ_PTR(1);
	ObjMakeSplash(object, splash);
	object_pc += 2;
	return 0;
}

static int ObjCmdInc(void)
{
	UCHAR mem = OBJ_UCHARB(0);
	SHORT period = OBJ_SHORTL(0);
	if (!(gfx_frame % period)) object->mem[mem].i++;
	object_pc += 1;
	return 0;
}

static int (*obj_cmdtab[])(void) =
{
	ObjCmdInit,
	ObjCmdSleep,
	ObjCmdCall,
	ObjCmdReturn,
	ObjCmdJump,
	ObjCmdFor,
	ObjCmdFend,
	ObjCmdFcontinue,
	ObjCmdWhile,
	ObjCmdWend,
	ObjCmdExit,
	ObjCmdEnd,
	ObjCmdCallback,
	ObjCmdAddF,
	ObjCmdSetF,
	ObjCmdAddI,
	ObjCmdSetI,
	ObjCmdSetFlag,
	ObjCmdClrFlag,
	ObjCmdSetRandA,
	ObjCmdSetRandF,
	ObjCmdSetRandI,
	ObjCmdAddRandF,
	ObjCmdAddRandA,
	ObjCmd24,
	ObjCmd25,
	ObjCmd26,
	ObjCmdShape,
	ObjCmdMakeObj,
	ObjCmdDestroy,
	ObjCmdGround,
	ObjCmdMemAddF,
	ObjCmdMemAddI,
	ObjCmdBillboard,
	ObjCmdHide,
	ObjCmdHitBox,
	ObjCmd36,
	ObjCmdMemSleep,
	ObjCmdFor2,
	ObjCmdPtr,
	ObjCmdAnime,
	ObjCmdMakeObjCode,
	ObjCmdMap,
	ObjCmdHitBoxOff,
	ObjCmdMakeChild,
	ObjCmdSavePos,
	ObjCmdDmgBox,
	ObjCmdHitType,
	ObjCmdPhysics,
	ObjCmdHitFlag,
	ObjCmdScale,
	ObjCmdMemClrParentFlag,
	ObjCmdInc,
	ObjCmdClrActive,
	ObjCmdSetS,
	ObjCmdSplash,
};

void ObjLangInit(void)
{
}

void ObjLangExec(void)
{
	UNUSED int i;
	SHORT flag = object->o_flag;
	float dist;
	int (*cmd)(void);
	int result;
	if (flag & OF_CALCPLDIST)
	{
		object->o_pl_dist = ObjCalcDist3D(object, mario_obj);
		dist = object->o_pl_dist;
	}
	else
	{
		dist = 0;
	}
	if (flag & OF_CALCPLANG)
	{
		object->o_pl_ang = ObjCalcAngY(object, mario_obj);
	}
	if (object->o_state != object->o_prevstate)
	{
		object->o_timer = 0, object->o_phase = 0,
		object->o_prevstate = object->o_state;
	}
	object_pc = object->pc;
	do
	{
		cmd = obj_cmdtab[OBJ_CMD];
		result = cmd();
	}
	while (!result);
	object->pc = object_pc;
	if (object->o_timer < 0x3FFFFFFF) object->o_timer++;
	if (object->o_state != object->o_prevstate)
	{
		object->o_timer = 0, object->o_phase = 0,
		object->o_prevstate = object->o_state;
	}
	flag = object->o_flag;
	if (flag & OF_SETSHAPEANG) ObjSetShapeAng(object);
	if (flag & OF_SETSHAPEANGY) object->o_shapeangy = object->o_angy;
	if (flag & OF_MOVEF) ObjectMoveF();
	if (flag & OF_MOVEY) ObjectMoveY();
	if (flag & OF_CALCREL) ObjCalcRel(object);
	if (flag & OF_SETMTX) ObjSetMtx(object);
	if (flag & OF_SETSHAPECOORD) ObjSetShapeCoord(object);
	if (object->o_area != -1)
	{
		ObjectProcArea();
	}
	else if (flag & OF_CALCPLDIST)
	{
		if (!(object->map || (flag & OF_0080)))
		{
			if (dist > object->o_shapedist)
			{
				object->s.s.flag &= ~SHP_ACTIVE;
				object->flag |= OBJ_0002;
			}
			else if (!object->o_take)
			{
				object->s.s.flag |= SHP_ACTIVE;
				object->flag &= ~OBJ_0002;
			}
		}
	}
}
