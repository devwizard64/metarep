#include <sm64.h>

UNUSED static
void list_init(LIST *root, LIST *free, LIST *data, size_t size, int count)
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

UNUSED static
LIST *list_alloc(LIST *root, LIST *free)
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

static OBJECT *objlist_alloc(OBJLIST *root, OBJLIST *free)
{
	OBJLIST *item;
	if ((item = free->next))
	{
		free->next = item->next;
		item->prev = root->prev;
		item->next = root;
		root->prev->next = item;
		root->prev = item;
	}
	else
	{
		return NULL;
	}
	shape_unlink(&item->s.s);
	shape_link(&sobj_list, &item->s.s);
	return (OBJECT *)item;
}

UNUSED static
void list_free(LIST *free, LIST *item)
{
	item->next->prev = item->prev;
	item->prev->next = item->next;
	item->next = free->next;
	free->next = item;
}

static void objlist_free(OBJLIST *free, OBJLIST *item)
{
	item->next->prev = item->prev;
	item->prev->next = item->next;
	item->next = free->next;
	free->next = item;
}

void obj_freelist_init(void)
{
	int i;
	int count = 240;
	OBJECT *obj = object_data;
	obj_freelist.next = &obj->list;
	for (i = 0; i < count-1; i++)
	{
		obj->list.next = &(obj+1)->list;
		obj++;
	}
	obj->list.next = NULL;
}

void obj_rootlist_init(OBJLIST *root)
{
	int i;
	for (i = 0; i < 13; i++)
	{
		root[i].next = &root[i];
		root[i].prev = &root[i];
	}
}

UNUSED static
void objlist_802C9AD8(SHAPE *shape)
{
	SHAPE *child;
	SHAPE *next;
	SHAPE *first = shape;
	if ((child = shape->child)) objlist_802C9AD8(child);
	else obj_destroy((OBJECT *)shape);
	while ((next = shape->next) == first)
	{
		objlist_802C9AD8(next);
		shape = next->next;
	}
}

void obj_free(OBJECT *obj)
{
	obj->flag = 0;
	obj->child = NULL;
	obj->list.s.mf = NULL;
	Na_g_80321584(obj->list.s.view);
	shape_unlink(&obj->list.s.s);
	shape_link(&sobj_list, &obj->list.s.s);
	obj->list.s.s.flag &= ~S_FLAG_BILLBOARD;
	obj->list.s.s.flag &= ~S_FLAG_ACTIVE;
	objlist_free(&obj_freelist, &obj->list);
}

static OBJECT *obj_alloc(OBJLIST *root)
{
	int i;
	OBJECT *obj;
	if (!(obj = objlist_alloc(root, &obj_freelist)))
	{
		OBJECT *o;
		if (!(o = objlib_8029FB1C()))
		{
			for (;;);
		}
		else
		{
			obj_free(o);
			obj = objlist_alloc(root, &obj_freelist);
			if (object == obj)
			{
			}
		}
	}
	obj->flag = 1 | 0x100;
	obj->parent = obj;
	obj->child = NULL;
	obj->collision = 0;
	obj->col_count = 0;
	for (i = 0; i < 80; i++) obj->mem[i].i = 0;
	obj->_1C8 = NULL;
	obj->sp = 0;
	obj->_1F4 = 0;
	obj->col_hit_r = 50;
	obj->col_hit_h = 100;
	obj->col_dmg_r = 0;
	obj->col_dmg_h = 0;
	obj->col_offset = 0;
	obj->_210 = NULL;
	obj->obj_ground = NULL;
	obj->map = NULL;
	obj->o_col_timer = -1;
	obj->o_ap = 0;
	obj->o_hp = 2048;
	obj->o_col_dist = 1000;
	if (stage_index == STAGE_TTC)   obj->o_shape_dist = 2000;
	else                            obj->o_shape_dist = 4000;
	mtxf_identity(obj->mf);
	obj->_1F6 = 0;
	obj->_25C = NULL;
	obj->o_pl_dist = 19000;
	obj->o_area = -1;
	obj->list.s.s.flag &= ~S_FLAG_OBJHIDE;
	obj->list.s.pos[0] = -10000;
	obj->list.s.pos[1] = -10000;
	obj->list.s.pos[2] = -10000;
	obj->list.s.mf = NULL;
	return obj;
}

static void obj_init_ground(OBJECT *obj)
{
	BGFACE *ground;
	obj->o_ground_y = bg_check_ground(
		obj->o_pos_x, obj->o_pos_y, obj->o_pos_z, &ground
	);
	if (obj->o_ground_y+2 > obj->o_pos_y && obj->o_ground_y-10 < obj->o_pos_y)
	{
		obj->o_pos_y = obj->o_ground_y;
		obj->o_move_flag |= 2;
	}
}

OBJECT *obj_create(O_SCRIPT *script)
{
	int i;
	OBJECT *obj;
	OBJLIST *root;
	O_SCRIPT *s = script;
	if (script[0] >> 24 == 0)   i = script[0] >> 16 & 0xFFFF;
	else                        i = O_TYPE_DEFAULT;
	root = &obj_rootlist[i];
	obj = obj_alloc(root);
	obj->pc = script;
	obj->script = s;
	if (i == O_TYPE_EFFECT) obj->flag |= 16;
	switch (i)
	{
	case O_TYPE_ENEMYA:
	case O_TYPE_ENEMYB:
	case O_TYPE_PL_USE:
		obj_init_ground(obj);
		break;
	default:
		break;
	}
	return obj;
}

void obj_destroy(OBJECT *obj)
{
	obj->flag = 0;
}
