#include <sm64.h>

static OBJLIST obj_rootdata[16];

int debug_flag;
int nullbg_count;
int nullroof_count;
int wall_count;
int obj_count;
BGDEBUG bgdebug;
short db_work[16][8];
short db_save[16][8];

int object_flag;
OBJECT object_data[OBJECT_MAX];
OBJECT object_dummy;
OBJLIST *obj_rootlist;
OBJLIST obj_freelist;
OBJECT *mario_obj;
OBJECT *luigi_obj;
OBJECT *object;
OBJLANG *object_pc;
s16 obj_prevcount;

int bglist_count;
int bgface_count;
int bglist_static;
int bgface_static;
HEAP *object_heap;
short object_80361180;
short object_80361182;
MAP *waterp;
int water_table[20];
AREA area_table[60][2];

s16 object_80361250;
s16 object_80361252;
s16 object_80361254;
s16 object_80361256;
s16 object_80361258;
s16 object_8036125A;
s16 object_8036125C;
s16 object_8036125E;
s16 object_80361260;
s16 object_80361262;
s16 object_80361264;

static s8 objproc_table[] =
{
	OT_SYSTEM,
	OT_MOVEBG,
	OT_ATTACH,
	OT_PLAYER,
	OT_ENEMYB,
	OT_ENEMYA,
	OT_ATTACK,
	OT_ITEM,
	OT_DEFAULT,
	OT_EFFECT,
	-1,
};

#include "player/player.c"

static int ObjListExecNormal(OBJECT *root, OBJECT *obj)
{
	int count = 0;
	while (root != obj)
	{
		object = obj;
		object->s.s.flag |= SHP_ANIME;
		ObjLangExec();
		obj = obj->next;
		count++;
	}
	return count;
}

static int ObjListExecFrozen(OBJECT *root, OBJECT *obj)
{
	int count = 0;
	while (root != obj)
	{
		int flag;
		object = obj;
		flag = FALSE;
		if (!(object_flag & OBJECT_FREEZEALL))
		{
			if (
				object == mario_obj &&
				!(object_flag & OBJECT_FREEZEPLAYER)
			) flag = TRUE;
			if (
				(object->o_hit_type & (HIT_DOOR|HIT_PORTDOOR)) &&
				!(object_flag & OBJECT_FREEZEPLAYER)
			) flag = TRUE;
			if (object->flag & (OBJ_0010|OBJ_0020)) flag = TRUE;
		}
		if (flag)
		{
			object->s.s.flag |= SHP_ANIME;
			ObjLangExec();
		}
		else
		{
			object->s.s.flag &= ~SHP_ANIME;
		}
		obj = obj->next;
		count++;
	}
	return count;
}

static int ObjListExec(OBJECT *root)
{
	int count;
	OBJECT *obj = root->next;
	if (!(object_flag & OBJECT_FROZEN)) count = ObjListExecNormal(root, obj);
	else                                count = ObjListExecFrozen(root, obj);
	return count;
}

static int ObjListCleanup(OBJECT *root)
{
	OBJECT *obj = root->next;
	while (root != obj)
	{
		object = obj;
		obj = obj->next;
		if ((object->flag & OBJ_0001) != OBJ_0001)
		{
			if (!(object->o_flag & OF_4000)) ObjSetActorFlag(object, 0xFF);
			ObjFree(object);
		}
	}
	return 0;
}

void ObjSetActorFlag(OBJECT *obj, UCHAR flag)
{
	u32 *w;
	u16 *h;
	switch (obj->actor_type)
	{
	case ACTORTYPE_32: w = obj->actor_flag; *w |= (u8)flag << 8; break;
	case ACTORTYPE_16: h = obj->actor_flag; *h |= (u8)flag << 8; break;
	}
}

void ObjectClose(UNUSED int screen, int group)
{
	OBJECT *o, *obj, *root;
	int i;
	obj_rootlist = obj_rootdata;
	for (i = 0; i < OT_MAX; i++)
	{
		root = (OBJECT *)&obj_rootlist[i];
		obj = root->next;
		while (obj != root)
		{
			o = obj;
			obj = obj->next;
			if (o->s.group == group) ObjFree(o);
		}
	}
}

void ObjectOpen(UNUSED int screen, ACTOR *actor)
{
	OBJECT *obj;
	UNUSED int i;
	OBJLANG *script;
	obj_rootlist = obj_rootdata;
	object_flag = 0;
	object_80361262 = 0;
	object_80361264 = 0;
#if REVISION > 199606
	PLRideClear();
#endif
	if (scene_index == 2) object_8036125C |= 1;
	while (actor)
	{
		UNUSED SHORT flag = actor->info & 0xFFFF;
		script = SegmentToVirtual(actor->script);
		if ((actor->info & 0xFF00) != 0xFF00)
		{
			obj = ObjCreate(script);
			obj->o_actorinfo = actor->info;
			obj->o_code = actor->info >> 16 & 0xFF;
			obj->script = script;
			obj->_1C8 = NULL;
			obj->actor_type = ACTORTYPE_32;
			obj->actor_flag = &actor->info;
			if (actor->info & ACTOR_MARIO)
			{
				mario_obj = obj;
				ShpMakeFirst(&obj->s.s);
			}
			SObjActor(&obj->s, actor);
			obj->o_posx = actor->pos[0];
			obj->o_posy = actor->pos[1];
			obj->o_posz = actor->pos[2];
			obj->o_shapeangx = actor->ang[0];
			obj->o_shapeangy = actor->ang[1];
			obj->o_shapeangz = actor->ang[2];
			obj->o_angx = actor->ang[0];
			obj->o_angy = actor->ang[1];
			obj->o_angz = actor->ang[2];
		}
		actor = actor->next;
	}
}

static void object_8029D1D8(void)
{
}

void ObjectInit(void)
{
	int i;
	object_80361256 = 0;
	object_flag = 0;
	mario_obj = NULL;
	object_80361250 = 0;
	for (i = 0; i < 60; i++)
	{
		area_table[i][0] = 0;
		area_table[i][1] = 0;
	}
	DebugInit();
	ObjFreeListInit();
	ObjRootListInit(obj_rootdata);
	ObjLangInit();
	object_8029D1D8();
	for (i = 0; i < OBJECT_MAX; i++)
	{
		object_data[i].flag = 0;
		SObjInit(&object_data[i].s);
	}
	object_heap = HeapCreate(2048, MEM_ALLOC_L);
	obj_rootlist = obj_rootdata;
	MoveBGClear();
}

static void ObjectExec1(void)
{
	obj_count = ObjListExec((OBJECT *)&obj_rootlist[OT_SYSTEM]);
	/* meant += */
	obj_count = ObjListExec((OBJECT *)&obj_rootlist[OT_MOVEBG]);
}

static void ObjectExec2(void)
{
	UNUSED int i;
	int type, index = 2;
	while ((type = objproc_table[index]) != -1)
	{
		obj_count += ObjListExec((OBJECT *)&obj_rootlist[type]);
		index++;
	}
}

static void ObjectCleanup(void)
{
	UNUSED int i;
	int type, index = 0;
	while ((type = objproc_table[index]) != -1)
	{
		ObjListCleanup((OBJECT *)&obj_rootlist[type]);
		index++;
	}
	object_flag &= ~OBJECT_01;
}

UNUSED
static USHORT object_8029D4D0(OSTime *t, int i)
{
	USHORT s;
#ifdef sgi
	double d = t[i] - t[i-1];
	if (d < 0) d = 0;
	s = OS_CYCLES_TO_USEC(d) / (double)16667 * 1000;
#else
	long long d = t[i] - t[i-1];
	if (d < 0) d = 0;
	s = OS_CYCLES_TO_USEC(d) * 1000 / 16667;
#endif
	if (s > 999) s = 999;
	return s;
}

void ObjectProc(UNUSED int screen)
{
	OSTime t[30];
	t[0] = DbTimeStart();
	object_flag &= ~OBJECT_20;
	object_8036125E = 0;
	object_80361260 = 0;
	object_80361180 = 0;
	DebugClear();
	DebugExec();
	obj_rootlist = obj_rootdata;
	t[1] = DbTimeCount(t[0]);
	MoveBGClear();
	t[2] = DbTimeCount(t[0]);
	ObjectExec1();
	PLRideProc();
	t[3] = DbTimeCount(t[0]);
	HitCheck();
	t[4] = DbTimeCount(t[0]);
	ObjectExec2();
	t[5] = DbTimeCount(t[0]);
	ObjectCleanup();
	t[6] = DbTimeCount(t[0]);
	PLRideFind();
	t[7] = DbTimeCount(t[0]);
	t[0] = 0;
	DebugResult();
	if (object_flag & OBJECT_FREEZE)    object_flag |= OBJECT_FROZEN;
	else                                object_flag &= ~OBJECT_FROZEN;
	obj_prevcount = obj_count;
}
