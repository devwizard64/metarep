#include <sm64.h>

OBJECT *ObjDebugHit(OBJECT *obj)
{
	OBJECT *hit;
	UNUSED OBJECT *o;
	int i;
	for (i = 0; i < obj->hit_count; i++)
	{
		DbPrint("ON", 0);
		hit = obj->hit[i];
		if (hit != mario_obj) return hit;
	}
	return NULL;
}

static int ObjCheckHit(OBJECT *a, OBJECT *b)
{
	float al = a->o_posy - a->hit_offset;
	float bl = b->o_posy - b->hit_offset;
	float dx = a->o_posx - b->o_posx;
	UNUSED float dy = al - bl;
	float dz = a->o_posz - b->o_posz;
	float radius = a->hit_r + b->hit_r;
	float dist = DIST2(dx, dz);
	if (radius > dist)
	{
		float ah = al + a->hit_h;
		float bh = bl + b->hit_h;
		if (al > bh) return FALSE;
		if (ah < bl) return FALSE;
		if (a->hit_count >= OBJ_HIT_MAX) return FALSE;
		if (b->hit_count >= OBJ_HIT_MAX) return FALSE;
		a->hit[a->hit_count] = b;
		b->hit[b->hit_count] = a;
		a->hit_status |= b->o_hit_type;
		b->hit_status |= a->o_hit_type;
		a->hit_count++;
		b->hit_count++;
		return TRUE;
	}
#ifndef sgi
	return FALSE;
#endif
}

static int ObjCheckDmg(OBJECT *a, OBJECT *b)
{
	float al = a->o_posy - a->hit_offset;
	float bl = b->o_posy - b->hit_offset;
	float dx = a->o_posx - b->o_posx;
	UNUSED float dy = al - bl;
	float dz = a->o_posz - b->o_posz;
	float radius = a->dmg_r + b->dmg_r;
	float dist = DIST2(dx, dz);
	if (a == mario_obj) b->o_hit_flag |= HF_0002;
	if (radius > dist)
	{
		float ah = al + a->hit_h;
		float bh = bl + b->dmg_h;
		if (al > bh) return FALSE;
		if (ah < bl) return FALSE;
		if (a == mario_obj) b->o_hit_flag &= ~HF_0002;
		return TRUE;
	}
#ifndef sgi
	return FALSE;
#endif
}

static void HitClear(OBJECT *root)
{
	OBJECT *obj = root->next;
	while (obj != root)
	{
		obj->hit_count = 0;
		obj->hit_status = 0;
		if (obj->o_hit_timer > 0) obj->o_hit_timer--;
		obj = obj->next;
	}
}

static void HitCheckList(OBJECT *obj, OBJECT *o, OBJECT *root)
{
	if (!obj->o_hit_timer)
	{
		while (o != root)
		{
			if (!o->o_hit_timer)
			{
				if (ObjCheckHit(obj, o) && o->dmg_r) ObjCheckDmg(obj, o);
			}
			o = o->next;
		}
	}
}

#define HITCHECK(obj, i) \
	HitCheckList(obj, obj_rootlist[i].next, (OBJECT *)&obj_rootlist[i])

static void HitCheckPlayer(void)
{
	OBJECT *root = (OBJECT *)&obj_rootlist[OT_PLAYER];
	OBJECT *obj = root->next;
	while (obj != root)
	{
		HitCheckList(obj, obj->next, root);
		HITCHECK(obj, OT_ATTACH);
		HITCHECK(obj, OT_ITEM);
		HITCHECK(obj, OT_ENEMYA);
		HITCHECK(obj, OT_ENEMYB);
		HITCHECK(obj, OT_MOVEBG);
		HITCHECK(obj, OT_ATTACK);
		obj = obj->next;
	}
}

static void HitCheckEnemyB(void)
{
	OBJECT *root = (OBJECT *)&obj_rootlist[OT_ENEMYB];
	OBJECT *obj = root->next;
	while (obj != root)
	{
		HitCheckList(obj, obj->next, root);
		obj = obj->next;
	}
}

static void HitCheckAttack(void)
{
	OBJECT *root = (OBJECT *)&obj_rootlist[OT_ATTACK];
	OBJECT *obj = root->next;
	while (obj != root)
	{
		if (obj->o_targetdist < 2000 && !(obj->flag & OBJ_0200))
		{
			HitCheckList(obj, obj->next, root);
			HITCHECK(obj, OT_ENEMYA);
			HITCHECK(obj, OT_ENEMYB);
			HITCHECK(obj, OT_MOVEBG);
		}
		obj = obj->next;
	}
}

void HitCheck(void)
{
	HitClear((OBJECT *)&obj_rootlist[OT_ATTACH]);
	HitClear((OBJECT *)&obj_rootlist[OT_PLAYER]);
	HitClear((OBJECT *)&obj_rootlist[OT_ENEMYB]);
	HitClear((OBJECT *)&obj_rootlist[OT_ENEMYA]);
	HitClear((OBJECT *)&obj_rootlist[OT_ITEM]);
	HitClear((OBJECT *)&obj_rootlist[OT_MOVEBG]);
	HitClear((OBJECT *)&obj_rootlist[OT_ATTACK]);
	HitCheckPlayer();
	HitCheckAttack();
	HitCheckEnemyB();
}
