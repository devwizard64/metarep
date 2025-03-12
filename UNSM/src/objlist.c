#include <sm64.h>

void ListInit(LIST *root, LIST *free, LIST *data, size_t size, int count)
{
	int i;
	LIST *item = data;
	root->next = root;
	root->prev = root;
	free->next = data;
	for (i = 0; i < count-1; i++)
	{
		item = (LIST *)((char *)item + size);
		data->next = item;
		data = item;
	}
	data->next = NULL;
}

LIST *ListAlloc(LIST *root, LIST *free)
{
	LIST *item;
	if ((item = free->next))
	{
		free->next = item->next;
		item->prev = root->prev;
		item->next = root;
		root->prev->next = item;
		root->prev = item;
	}
	return item;
}

static OBJECT *ObjListAlloc(OBJLIST *root, OBJLIST *free)
{
	OBJECT *obj;
	if ((obj = free->next))
	{
		free->next = obj->next;
		obj->prev = root->prev;
		obj->next = (OBJECT *)root;
		root->prev->next = obj;
		root->prev = obj;
	}
	else
	{
		return NULL;
	}
	ShpUnlink(&obj->s.s);
	ShpLink(&sobj_list, &obj->s.s);
	return obj;
}

void ListFree(LIST *free, LIST *item)
{
	item->next->prev = item->prev;
	item->prev->next = item->next;
	item->next = free->next;
	free->next = item;
}

static void ObjListFree(OBJLIST *free, OBJECT *obj)
{
	obj->next->prev = obj->prev;
	obj->prev->next = obj->next;
	obj->next = free->next;
	free->next = obj;
}

void ObjFreeListInit(void)
{
	int i;
	int count = OBJECT_MAX;
	OBJECT *obj = object_data;
	obj_freelist.next = obj;
	for (i = 0; i < count-1; i++)
	{
		obj->next = obj+1;
		obj++;
	}
	obj->next = NULL;
}

void ObjRootListInit(OBJLIST *root)
{
	int i;
	for (i = 0; i < OT_MAX; i++)
	{
		root[i].next = (OBJECT *)&root[i];
		root[i].prev = (OBJECT *)&root[i];
	}
}

UNUSED
static void objlist_802C9AD8(SHAPE *shape)
{
	SHAPE *child;
	SHAPE *next;
	SHAPE *first = shape;
	if ((child = shape->child)) objlist_802C9AD8(child);
	else ObjDestroy((OBJECT *)shape);
	while ((next = shape->next) == first)
	{
		objlist_802C9AD8(next);
		shape = next->next;
	}
}

void ObjFree(OBJECT *obj)
{
	obj->flag = 0;
	obj->child = NULL;
	obj->s.m = NULL;
	Na_ObjSeKill(obj);
	ShpUnlink(&obj->s.s);
	ShpLink(&sobj_list, &obj->s.s);
	obj->s.s.flag &= ~SHP_BILLBOARD;
	obj->s.s.flag &= ~SHP_ACTIVE;
	ObjListFree(&obj_freelist, obj);
}

static OBJECT *ObjAlloc(OBJLIST *root)
{
	int i;
	OBJECT *obj;
	if (!(obj = ObjListAlloc(root, &obj_freelist)))
	{
		OBJECT *o;
		if (!(o = ObjGetEffect()))
		{
			for (;;);
		}
		else
		{
			ObjFree(o);
			obj = ObjListAlloc(root, &obj_freelist);
			if (object == obj)
			{
			}
		}
	}
	obj->flag = OBJ_0001 | OBJ_0100;
	obj->parent = obj;
	obj->child = NULL;
	obj->hit_status = 0;
	obj->hit_count = 0;
	for (i = 0; i < OBJ_WORK_MAX; i++) obj->work[i].i = 0;
	obj->_1C8 = NULL;
	obj->sp = 0;
	obj->sleep = 0;
	obj->hit_r = 50;
	obj->hit_h = 100;
	obj->dmg_r = 0;
	obj->dmg_h = 0;
	obj->hit_offset = 0;
	obj->_210 = NULL;
	obj->movebg = NULL;
	obj->map = NULL;
	obj->o_hit_timer = -1;
	obj->o_ap = 0;
	obj->o_hp = 2048;
	obj->o_checkdist = 1000;
	obj->o_shapedist = stage_index == STAGE_TTC ? 2000.0F : 4000.0F;
	FMtxIdent(obj->mtx);
	obj->actor_type = ACTORTYPE_NULL;
	obj->actor_flag = NULL;
	obj->o_targetdist = 19000; /* T:def */
	obj->o_area = -1;
	obj->s.s.flag &= ~SHP_OBJHIDE;
	obj->s.pos[0] = -10000;
	obj->s.pos[1] = -10000;
	obj->s.pos[2] = -10000;
	obj->s.m = NULL;
	return obj;
}

static void ObjInitGround(OBJECT *obj)
{
	BGFACE *ground;
	obj->o_ground_y = BGCheckGround(
		obj->o_posx, obj->o_posy, obj->o_posz, &ground
	);
	if (obj->o_ground_y+2 > obj->o_posy && obj->o_ground_y-10 < obj->o_posy)
	{
		obj->o_posy = obj->o_ground_y;
		obj->o_move |= OM_TOUCH;
	}
}

OBJECT *ObjCreate(OBJLANG *script)
{
	int type;
	OBJECT *obj;
	OBJLIST *root;
	OBJLANG *s = script;
	if (script[0] >> 24 == OBJ_CMD_INIT)    type = script[0] >> 16 & 0xFFFF;
	else                                    type = OT_DEFAULT;
	root = &obj_rootlist[type];
	obj = ObjAlloc(root);
	obj->pc = script;
	obj->script = s;
	if (type == OT_EFFECT) obj->flag |= OBJ_0010;
	switch (type)
	{
	case OT_ENEMYA:
	case OT_ENEMYB:
	case OT_ATTACH:
		ObjInitGround(obj);
		break;
	default:
		break;
	}
	return obj;
}

void ObjDestroy(OBJECT *obj)
{
	obj->flag = 0;
}
