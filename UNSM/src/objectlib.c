#include <sm64.h>

void *CtrlObjectHand(int code, UNUSED SHAPE *shape, void *data)
{
	if (code == SC_DRAW)
	{
		FMTX m;
		OBJECT *obj = (OBJECT *)draw_object;
		if (obj->child)
		{
			FMtxInvCatAffine(m, data, *draw_camera->m);
			ObjSetPosRelXFM(m, obj->child);
			ObjSetShapePos(obj->child);
		}
	}
	return NULL;
}

extern OBJLANG obj_13001850[];

void *CtrlObjectAlpha(int code, SHAPE *shape, UNUSED void *data)
{
	Gfx *gfx = NULL, *g;
	if (code == SC_DRAW)
	{
		OBJECT *obj = (OBJECT *)draw_object;
		SCALLBACK *shp = (SCALLBACK *)shape;
		UNUSED SHAPE *s = shape;
		int alpha;
		if (draw_hand) obj = (OBJECT *)draw_hand->obj;
		alpha = obj->o_alpha;
		g = gfx = GfxAlloc(sizeof(Gfx)*3);
		if (alpha == 0xFF)
		{
			if (shp->arg == 20) ShpSetLayer(&shp->s, LAYER_XLU_DECAL);
			else                ShpSetLayer(&shp->s, LAYER_OPA_SURF);
			obj->o_shape = 0;
		}
		else
		{
			if (shp->arg == 20) ShpSetLayer(&shp->s, LAYER_XLU_DECAL);
			else                ShpSetLayer(&shp->s, LAYER_XLU_SURF);
			obj->o_shape = 1;
#if REVISION >= 199609
			if (alpha == 0 && SegmentToVirtual(obj_13001850) == obj->script)
			{
				obj->o_shape = 2;
			}
			if (shp->arg != 10 && obj->flag & OBJ_DITHER)
			{
				gDPSetAlphaCompare(g++, G_AC_DITHER);
			}
#else
			if (shp->arg == 10)
			{
				if (db_work[5][3]) gDPSetAlphaCompare(g++, G_AC_DITHER);
			}
			else if (1 && obj->flag & OBJ_DITHER)
			{
				gDPSetAlphaCompare(g++, G_AC_DITHER);
			}
#endif
		}
		gDPSetEnvColor(g++, 0xFF, 0xFF, 0xFF, alpha);
		gSPEndDisplayList(g);
	}
	return gfx;
}

#ifdef sgi
void *CtrlObjectShape(int code, SHAPE *shape)
#else
void *CtrlObjectShape(int code, SHAPE *shape, UNUSED void *data)
#endif
{
	if (code == SC_DRAW)
	{
		OBJECT *obj = (OBJECT *)draw_object;
		SSELECT *shp = (SSELECT *)shape;
		if (draw_hand) obj = (OBJECT *)draw_hand->obj;
		if (obj->o_shape >= shp->code) obj->o_shape = 0;
		shp->index = obj->o_shape;
	}
	return NULL;
}

#ifdef sgi
void *CtrlArea(int code, SHAPE *shape)
#else
void *CtrlArea(int code, SHAPE *shape, UNUSED void *data)
#endif
{
	SHORT index;
	BGFACE *ground;
	UNUSED OBJECT *obj = (OBJECT *)draw_object;
	SSELECT *shp = (SSELECT *)shape;
	if (code == SC_DRAW)
	{
		if (!mario_obj)
		{
			shp->index = 0;
		}
		else
		{
			object_80361182 = TRUE;
			BGCheckGround(
				mario_obj->o_posx,
				mario_obj->o_posy,
				mario_obj->o_posz,
				&ground
			);
			if (ground)
			{
				object_80361250 = ground->area;
				index = ground->area - 1;
				DbPrint("areainfo %d", ground->area);
				if (index >= 0) shp->index = index;
			}
		}
	}
	else
	{
		shp->index = 0;
	}
	return NULL;
}

void ObjSetPosRelXFM(FMTX m, OBJECT *obj)
{
	float x = obj->o_relx;
	float y = obj->o_rely;
	float z = obj->o_relz;
	obj->o_posx = x*m[0][0] + y*m[1][0] + z*m[2][0] + m[3][0];
	obj->o_posy = x*m[0][1] + y*m[1][1] + z*m[2][1] + m[3][1];
	obj->o_posz = x*m[0][2] + y*m[1][2] + z*m[2][2] + m[3][2];
}

void ObjFMtxScaleCopy(OBJECT *obj, FMTX dst, FMTX src)
{
	dst[0][0] = src[0][0] * obj->s.scale[0];
	dst[1][0] = src[1][0] * obj->s.scale[1];
	dst[2][0] = src[2][0] * obj->s.scale[2];
	dst[3][0] = src[3][0];
	dst[0][1] = src[0][1] * obj->s.scale[0];
	dst[1][1] = src[1][1] * obj->s.scale[1];
	dst[2][1] = src[2][1] * obj->s.scale[2];
	dst[3][1] = src[3][1];
	dst[0][2] = src[0][2] * obj->s.scale[0];
	dst[1][2] = src[1][2] * obj->s.scale[1];
	dst[2][2] = src[2][2] * obj->s.scale[2];
	dst[3][2] = src[3][2];
	dst[0][3] = src[0][3];
	dst[1][3] = src[1][3];
	dst[2][3] = src[2][3];
	dst[3][3] = src[3][3];
}

#define ICAT(a, b, y, x) \
	((a)[y][0]*(b)[x][0] + (a)[y][1]*(b)[x][1] + (a)[y][2]*(b)[x][2])

void FMtxInvCatAffine(FMTX dst, FMTX src, FMTX cam)
{
	float x = ICAT(cam, cam, 3, 0);
	float y = ICAT(cam, cam, 3, 1);
	float z = ICAT(cam, cam, 3, 2);
	dst[0][0] = ICAT(src, cam, 0, 0);
	dst[0][1] = ICAT(src, cam, 0, 1);
	dst[0][2] = ICAT(src, cam, 0, 2);
	dst[1][0] = ICAT(src, cam, 1, 0);
	dst[1][1] = ICAT(src, cam, 1, 1);
	dst[1][2] = ICAT(src, cam, 1, 2);
	dst[2][0] = ICAT(src, cam, 2, 0);
	dst[2][1] = ICAT(src, cam, 2, 1);
	dst[2][2] = ICAT(src, cam, 2, 2);
	dst[3][0] = ICAT(src, cam, 3, 0) - x;
	dst[3][1] = ICAT(src, cam, 3, 1) - y;
	dst[3][2] = ICAT(src, cam, 3, 2) - z;
	dst[0][3] = 0;
	dst[1][3] = 0;
	dst[2][3] = 0;
	dst[3][3] = 1;
}

extern OBJLANG obj_13003464[];
extern OBJLANG obj_1300346C[];
extern OBJLANG obj_13003474[];

void ObjectSetAction(OBJECT *o, OBJLANG *script)
{
	o->parent = object;
	if (o->o_flag & OF_0400)
	{
		if (script == obj_13003464) o->o_action = OA_1;
		if (script == obj_13003474) o->o_action = OA_2;
		if (script == obj_1300346C) o->o_action = OA_3;
	}
	else
	{
		o->pc = SegmentToVirtual(script);
		o->sp = 0;
	}
}

float ObjCalcDist2D(OBJECT *obj, OBJECT *o)
{
	float dx = obj->o_posx - o->o_posx;
	float dz = obj->o_posz - o->o_posz;
	return DIST2(dx, dz);
}

float ObjCalcDist3D(OBJECT *obj, OBJECT *o)
{
	float dx = obj->o_posx - o->o_posx;
	float dy = obj->o_posy - o->o_posy;
	float dz = obj->o_posz - o->o_posz;
	return DIST3(dx, dy, dz);
}

void ObjectAccelerate(float limit, float accel)
{
	if (object->o_velf >= limit)    object->o_velf = limit;
	else                            object->o_velf += accel;
}

int Accelerate(float *speed, float limit, float accel)
{
	int result = FALSE;
	*speed += accel;
	if (accel >= 0)
	{
		if (*speed > limit)
		{
			*speed = limit;
			result = TRUE;
		}
	}
	else
	{
		if (*speed < limit)
		{
			*speed = limit;
			result = TRUE;
		}
	}
	return result;
}

float ApproachPos(float x, float target, float speed)
{
	float d;
	if ((d = target-x) >= 0)
	{
		if (d > +speed) x += speed;
		else            x = target;
	}
	else
	{
		if (d < -speed) x -= speed;
		else            x = target;
	}
	return x;
}

short ApproachAng(short x, short target, short speed)
{
	short d;
	if ((d = target-x) >= 0)
	{
		if (d > +speed) x += speed;
		else            x = target;
	}
	else
	{
		if (d < -speed) x -= speed;
		else            x = target;
	}
	return x;
}

int ObjectTurn(SHORT target, SHORT speed)
{
	short angy = object->o_angy;
	object->o_angy = ApproachAng(object->o_angy, target, speed);
	if ((object->o_roty = (short)((SHORT)object->o_angy-angy)) == 0)
	{
		return TRUE;
	}
	else
	{
		return FALSE;
	}
}

SHORT ObjCalcAngY(OBJECT *obj, OBJECT *o)
{
	float objz, objx, oz, ox;
	SHORT angy;
	objz = obj->o_posz; oz = o->o_posz;
	objx = obj->o_posx; ox = o->o_posx;
	angy = ATAN2(oz-objz, ox-objx);
	return angy;
}

short ObjectTurnTo(OBJECT *a, OBJECT *b, SHORT work, SHORT speed)
{
	float az, ax, bz, bx;
	UNUSED float z;
	SHORT target, ang;
	switch (work)
	{
	case O_ANGX:
	case O_SHAPEANGX:
		az = b->o_posx - a->o_posx;
		bz = b->o_posz - a->o_posz;
		az = DIST2(az, bz);
		ax = -a->o_posy;
		bx = -b->o_posy;
		target = ATAN2(az, bx-ax);
		break;
	case O_ANGY:
	case O_SHAPEANGY:
		az = a->o_posz;
		bz = b->o_posz;
		ax = a->o_posx;
		bx = b->o_posx;
		target = ATAN2(bz-az, bx-ax);
		break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
	ang = object->work[work].i;
	object->work[work].i = ApproachAng(ang, target, speed);
	return target;
}

void ObjSetRel(OBJECT *obj, SHORT relx, SHORT rely, SHORT relz)
{
	obj->o_relx = (short)relx;
	obj->o_rely = (short)rely;
	obj->o_relz = (short)relz;
}

void ObjSetPos(OBJECT *obj, SHORT posx, SHORT posy, SHORT posz)
{
	obj->o_posx = (short)posx;
	obj->o_posy = (short)posy;
	obj->o_posz = (short)posz;
}

void ObjSetAng(OBJECT *obj, SHORT angx, SHORT angy, SHORT angz)
{
	obj->o_shapeangx = (short)angx;
	obj->o_shapeangy = (short)angy;
	obj->o_shapeangz = (short)angz;
	obj->o_angx = (short)angx;
	obj->o_angy = (short)angy;
	obj->o_angz = (short)angz;
}

OBJECT *ObjMakeAt(
	OBJECT *parent, SHORT arg, int shape, OBJLANG *script,
	SHORT posx, SHORT posy, SHORT posz,
	SHORT angx, SHORT angy, SHORT angz
)
{
	OBJECT *obj = ObjMake(parent, arg, shape, script);
	ObjSetPos(obj, posx, posy, posz);
	ObjSetAng(obj, angx, angy, angz);
	return obj;
}

OBJECT *ObjMakeRel(
	OBJECT *parent, int shape, OBJLANG *script,
	SHORT relx, SHORT rely, SHORT relz,
	SHORT angx, SHORT angy, UNUSED SHORT angz
)
{
	OBJECT *obj = ObjMake(parent, 0, shape, script);
	obj->o_flag |= OF_CALCREL;
	ObjSetRel(obj, relx, rely, relz);
	ObjSetAng(obj, angx, angy, relz);
	return obj;
}

OBJECT *ObjMakeHereMtx(OBJECT *parent, int shape, OBJLANG *script)
{
	OBJECT *obj = ObjMakeHere(parent, shape, script);
	obj->o_flag |= OF_CALCMTX|OF_SETMTX;
	return obj;
}

OBJECT *ObjMakeSplash(OBJECT *parent, SPLASH *splash)
{
	float scale;
	OBJECT *obj = ObjMakeHere(parent, splash->shape, splash->script);
	if (splash->flag & 0x02) obj->o_angy = Rand();
	if (splash->flag & 0x40)
	{
		obj->o_angy =
			(short)(obj->o_angy+0x8000) +
			(short)RandRange(splash->ang_range);
	}
	if (splash->flag & 0x80)
	{
		obj->o_angy =
			(short)(obj->o_angy) +
			(short)RandRange(splash->ang_range);
	}
	if (splash->flag & 0x20)
	{
		obj->o_posy = BGCheckWater(obj->o_posx, obj->o_posz);
	}
	if (splash->flag & 0x04) ObjRandOff2D(obj, splash->pos_range);
	if (splash->flag & 0x08) ObjRandOff3D(obj, splash->pos_range);
	obj->o_velf = RandF()*splash->velf_range + splash->velf_start;
	obj->o_vely = RandF()*splash->vely_range + splash->vely_start;
	scale = RandF()*splash->scale_range + splash->scale_start;
	ObjSetScale(obj, scale);
	return obj;
}

OBJECT *ObjMake(OBJECT *parent, UNUSED SHORT arg, int shape, OBJLANG *script)
{
	OBJECT *obj;
	OBJLANG *addr = SegmentToVirtual(script);
	obj = ObjCreate(addr);
	obj->parent = parent;
	obj->s.scene = parent->s.scene;
	obj->s.group = parent->s.scene;
	SObjEnter(&obj->s, shape_table[shape], fvec_0, svec_0);
	return obj;
}

OBJECT *ObjMakeHere(OBJECT *parent, int shape, OBJLANG *script)
{
	OBJECT *obj = ObjMake(parent, 0, shape, script);
	ObjCopyCoord(obj, parent);
	return obj;
}

OBJECT *ObjMakeEffect(
	SHORT offy, float scale, OBJECT *parent, int shape, OBJLANG *script
)
{
	if (obj_freelist.next)
	{
		OBJECT *obj = ObjMakeHere(parent, shape, script);
		obj->o_posy += offy;
		ObjSetScale(obj, scale);
		return obj;
	}
	else
	{
		return NULL;
	}
}

OBJECT *ObjMakeHereScale(
	OBJECT *parent, int shape, OBJLANG *script, float scale
)
{
	OBJECT *obj = ObjMake(parent, 0, shape, script);
	ObjCopyCoord(obj, parent);
	ObjSetScale(obj, scale);
	return obj;
}

static void ObjAddRelPos(OBJECT *obj)
{
	ObjCalcMtx(obj, O_REL, O_SHAPEANG);
	ObjAddTransform(obj, O_POS, O_REL);
}

OBJECT *ObjMakeOff(
	SHORT code, SHORT offx, SHORT offy, SHORT offz,
	OBJECT *parent, int shape, OBJLANG *script
)
{
	OBJECT *obj = ObjMake(parent, 0, shape, script);
	ObjCopyCoord(obj, parent);
	ObjSetRel(obj, offx, offy, offz);
	ObjAddRelPos(obj);
	obj->o_code = code;
	ObjSetCode(obj, code);
	return obj;
}

OBJECT *ObjMakeOffScale(
	SHORT code, SHORT offx, SHORT offy, SHORT offz, float scale,
	OBJECT *parent, int shape, OBJLANG *script
)
{
	OBJECT *obj = ObjMakeOff(code, offx, offy, offz, parent, shape, script);
	ObjSetScale(obj, scale);
	return obj;
}

void ObjectMove3D(void)
{
	object->o_posx += object->o_velx;
	object->o_posy += object->o_vely;
	object->o_posz += object->o_velz;
}

void ObjCopyShapeOff(OBJECT *obj, OBJECT *o)
{
	obj->o_shapeoff = o->o_shapeoff;
}

void ObjCopyCoord(OBJECT *obj, OBJECT *o)
{
	ObjCopyPos(obj, o);
	ObjCopyAng(obj, o);
}

void ObjCopyPos(OBJECT *obj, OBJECT *o)
{
	obj->o_posx = o->o_posx;
	obj->o_posy = o->o_posy;
	obj->o_posz = o->o_posz;
}

void ObjCopyAng(OBJECT *obj, OBJECT *o)
{
	obj->o_angx = o->o_angx;
	obj->o_angy = o->o_angy;
	obj->o_angz = o->o_angz;
	obj->o_shapeangx = o->o_shapeangx;
	obj->o_shapeangy = o->o_shapeangy;
	obj->o_shapeangz = o->o_shapeangz;
}

void ObjSetShapePos(OBJECT *obj)
{
	obj->s.pos[0] = obj->o_posx;
	obj->s.pos[1] = obj->o_posy;
	obj->s.pos[2] = obj->o_posz;
}

void ObjStartAnime(OBJECT *obj, int anime)
{
	ANIME **animetab = object->o_animep;
	SObjSetAnime(&obj->s, &animetab[anime]);
}

void MtxTransform3(FMTX m, FVEC dst, FVEC src)
{
	int i;
	for (i = 0; i < 3; i++) dst[i] = MDOT3(m, i, src[0], src[1], src[2]);
}

void InvTransform3(FMTX m, FVEC dst, FVEC src)
{
	int i;
	for (i = 0; i < 3; i++) dst[i] = IDOT3(m, i, src[0], src[1], src[2]);
}

static void ObjScaleMtx(OBJECT *obj)
{
	float scalex = obj->s.scale[0];
	float scaley = obj->s.scale[1];
	float scalez = obj->s.scale[2];
	obj->mtx[0][0] *= scalex;
	obj->mtx[0][1] *= scalex;
	obj->mtx[0][2] *= scalex;
	obj->mtx[1][0] *= scaley;
	obj->mtx[1][1] *= scaley;
	obj->mtx[1][2] *= scaley;
	obj->mtx[2][0] *= scalez;
	obj->mtx[2][1] *= scalez;
	obj->mtx[2][2] *= scalez;
}

void ObjCopyScale(OBJECT *obj, OBJECT *o)
{
	obj->s.scale[0] = o->s.scale[0];
	obj->s.scale[1] = o->s.scale[1];
	obj->s.scale[2] = o->s.scale[2];
}

void ObjSetScaleXYZ(OBJECT *obj, float scalex, float scaley, float scalez)
{
	obj->s.scale[0] = scalex;
	obj->s.scale[1] = scaley;
	obj->s.scale[2] = scalez;
}

void ObjSetScale(OBJECT *obj, float scale)
{
	obj->s.scale[0] = scale;
	obj->s.scale[1] = scale;
	obj->s.scale[2] = scale;
}

void ObjectSetScale(float scale)
{
	object->s.scale[0] = scale;
	object->s.scale[1] = scale;
	object->s.scale[2] = scale;
}

void ObjectStartAnime(int anime)
{
	ANIME **animetab = object->o_animep;
	SObjSetAnime(&object->s, &animetab[anime]);
}

void ObjectSetAnime(int anime)
{
	ANIME **animetab = object->o_animep;
	SObjSetAnime(&object->s, &animetab[anime]);
	object->o_anime = anime;
}

void ObjectSetAnimeV(int anime, float speed)
{
	ANIME **animetab = object->o_animep;
	int vspeed = VSPEED(speed);
	SObjSetAnimeV(&object->s, &animetab[anime], vspeed);
	object->o_anime = anime;
}

void ObjInitAnime(OBJECT *obj, void *animep, int anime)
{
	ANIME **animetab = animep;
	obj->o_animep = animep;
	SObjSetAnime(&obj->s, &animetab[anime]);
	obj->o_anime = anime;
}

void ObjActivate(OBJECT *obj)
{
	obj->s.s.flag |= SHP_ACTIVE;
	obj->o_hit_timer = 0;
}

void ObjectSetActive(void)
{
	object->s.s.flag |= SHP_ACTIVE;
}

void ObjDeactivate(OBJECT *obj)
{
	obj->s.s.flag &= ~SHP_ACTIVE;
	obj->o_hit_timer = -1;
}

void ObjectClrActive(void)
{
	object->s.s.flag &= ~SHP_ACTIVE;
}

void ObjectShow(void)
{
	object->s.s.flag &= ~SHP_OBJHIDE;
}

void ObjectHide(void)
{
	object->s.s.flag |= SHP_OBJHIDE;
}

void ObjectSetPosOff(OBJECT *o, float offx, float offy, float offz)
{
	float cy = COS(o->o_angy);
	float sy = SIN(o->o_angy);
	float dz = offz*cy - offx*sy;
	float dx = offz*sy + offx*cy;
	object->o_angy = o->o_angy;
	object->o_posx = o->o_posx + dx;
	object->o_posy = o->o_posy + offy;
	object->o_posz = o->o_posz + dz;
}

static void ObjectSetPosOffParent(float offx, float offy, float offz)
{
	ObjectSetPosOff(object->parent, offx, offy, offz);
}

void objectlib_8029F820(void)
{
	ObjectSetActive();
}

void objectlib_8029F848(void)
{
	ObjectSetActive();
	object->o_posy = BGCheckGroundY(
		object->o_posx, object->o_posy, object->o_posz
	);
	if (object->o_posy < -10000)
	{
		ObjectSetPosOffParent(0, 0, -70);
		object->o_posy = BGCheckGroundY(
			object->o_posx, object->o_posy, object->o_posz
		);
	}
}

void ObjSetShapeAng(OBJECT *obj)
{
	obj->o_shapeangx = obj->o_angx;
	obj->o_shapeangy = obj->o_angy;
	obj->o_shapeangz = obj->o_angz;
}

int ObjGetScriptType(OBJLANG *script)
{
	int type;
	if (script[0] >> 24 == OBJ_CMD_INIT)    type = script[0] >> 16 & 0xFFFF;
	else                                    type = OT_DEFAULT;
	return type;
}

OBJECT *ObjectFindObj(OBJLANG *script)
{
	OBJECT *o;
	float dist;
	o = ObjectFind(script, &dist);
	return o;
}

float ObjectFindDist(OBJLANG *script)
{
	OBJECT *o;
	float dist;
	o = ObjectFind(script, &dist);
	if (!o) dist = 15000;
	return dist;
}

OBJECT *ObjectFind(OBJLANG *script, float *distp)
{
	void *vaddr = SegmentToVirtual(script);
	OBJECT *result = NULL, *o, *root;
	float dist = 131072;
	root = (OBJECT *)&obj_rootlist[ObjGetScriptType(vaddr)];
	o = root->next;
	while (root != o)
	{
		if (o->script == vaddr)
		{
			if (o->flag && o != object)
			{
				float d = ObjCalcDist3D(object, o);
				if (d < dist)
				{
					result = o;
					dist = d;
				}
			}
		}
		o = o->next;
	}
	*distp = dist;
	return result;
}

OBJECT *ObjGetEffect(void)
{
	OBJECT *root = (OBJECT *)&obj_rootlist[OT_EFFECT];
	OBJECT *o = root->next;
	if (root == o) o = NULL;
	return o;
}

int ObjCountEffect(void)
{
	OBJECT *root = (OBJECT *)&obj_rootlist[OT_EFFECT];
	OBJECT *o = root->next;
	int count = 0;
	while (root != o)
	{
		count++;
		o = o->next;
	}
	return count;
}

int ObjCount(OBJLANG *script)
{
	OBJLANG *vaddr = SegmentToVirtual(script);
	OBJECT *root = (OBJECT *)&obj_rootlist[ObjGetScriptType(vaddr)];
	OBJECT *o = root->next;
	int count = 0;
	while (root != o)
	{
		if (o->script == vaddr) count++;
		o = o->next;
	}
	return count;
}

OBJECT *ObjectFindTake(OBJLANG *script, float dist)
{
	OBJLANG *vaddr = SegmentToVirtual(script);
	OBJECT *root = (OBJECT *)&obj_rootlist[OT_ENEMYA];
	OBJECT *o = root->next;
	OBJECT *result = NULL;
	while (root != o)
	{
		if (o->script == vaddr)
		{
			if (o->flag)
			{
				if (o->o_action != OA_0)
				{
					if (ObjCalcDist3D(object, o) < dist)
					{
						result = o;
						break;
					}
				}
			}
		}
		o = o->next;
	}
	return result;
}

static void ObjectResetMode(void)
{
	object->o_timer = 0;
	object->o_phase = 0;
}

void ObjectInitMode(int mode)
{
	object->o_mode = mode;
	object->o_prevmode = mode;
	ObjectResetMode();
}

void ObjectMatchP1Speed(float min, float scale)
{
	float speed = player_data[0].speed;
	float minspeed = min * scale;
	if (speed < minspeed)
	{
		object->o_velf = minspeed;
	}
	else
	{
		object->o_velf = speed * scale;
	}
}

void ObjectAnimeHold(void)
{
	if (object->s.skel.frame >= 0) object->s.skel.frame--;
}

VOID ObjectAnimeHoldEnd(void)
{
	int f = object->s.skel.frame;
	int end = object->s.skel.anime->frame - 2;
	if (f == end) object->s.skel.frame--;
}

int objectlib_8029FF04(void)
{
	int flag = object->s.skel.anime->flag;
	int f = object->s.skel.frame;
	int end = object->s.skel.anime->frame - 2;
	int result = FALSE;
	if (flag & ANIME_NOLOOP && f == end+1) result = TRUE;
	if (f == end) result = TRUE;
	return result;
}

int objectlib_8029FFA4(void)
{
	int f = object->s.skel.frame;
	int end = object->s.skel.anime->frame - 1;
	if (f == end)   return TRUE;
	else            return FALSE;
}

int ObjectIsAnimeFrame(int frame)
{
	int f = object->s.skel.frame;
	if (f == frame) return TRUE;
	else            return FALSE;
}

int ObjectIsAnimeFrameRange(int start, int count)
{
	int f = object->s.skel.frame;
	if (f >= start && f < start+count)  return TRUE;
	else                                return FALSE;
}

int ObjectIsAnimeFrameTable(short *table)
{
	SHORT f = object->s.skel.frame;
	while (*table != -1)
	{
		if (f == *table) return TRUE;
		table++;
	}
	return FALSE;
}

int Player1IsJump(void)
{
	if (player_data[0].state & PF_JUMP) return TRUE;
	else return FALSE;
}

int objectlib_802A0154(void)
{
	if (player_data[0].state == PS_WALK_16) return TRUE;
	else return FALSE;
}

void ObjectSetAnimeJump(float vely, int anime)
{
	object->o_vely = vely;
	ObjectSetAnime(anime);
}

void objectlib_802A01D8(int anime, int mode)
{
	ObjectHitOFF();
	ObjectClrActive();
	if (anime >= 0) ObjectSetAnime(anime);
	object->o_mode = mode;
}

static void objectlib_802A0234(float velf, float vely)
{
	object->o_move = 0;
	object->o_ground_y = BGCheckGroundY(
		object->o_posx, object->o_posy+160, object->o_posz
	);
	if (object->o_ground_y > object->o_posy)
	{
		object->o_posy = object->o_ground_y;
	}
	else if (object->o_ground_y < -10000)
	{
		ObjCopyPos(object, mario_obj);
		object->o_ground_y = BGCheckGroundY(
			object->o_posx, object->o_posy, object->o_posz
		);
	}
	object->o_velf = velf;
	object->o_vely = vely;
	if (object->o_velf != 0) objectlib_802A0E68(-4, -0.1F, 2);
}

void objectlib_802A0380(float velf, float vely, int mode)
{
	if (object->script == SegmentToVirtual(obj_13001850))
	{
		ObjectSetPosOffParent(-41.684F, 85.859F, 321.577F);
	}
	else
	{
	}
	ObjectHitON();
	ObjectSetActive();
	object->o_action = OA_0;
	if (object->o_hit_flag & HF_0010 || velf == 0)
	{
		objectlib_802A0234(0, 0);
	}
	else
	{
		object->o_mode = mode;
		objectlib_802A0234(velf, vely);
	}
}

void objectlib_802A0474(void)
{
	ObjectHitON();
	ObjectSetActive();
	object->o_action = OA_0;
	objectlib_802A0234(0, 0);
}

void ObjectSetShape(int shape)
{
	object->s.shape = shape_table[shape];
}

void Player1SetFlag(u32 flag)
{
	player_data[0].flag |= flag;
}

int ObjectCheckHitResult(int flag)
{
	if (object->o_hit_result & flag)
	{
		object->o_hit_result &= ~0^flag;
		return TRUE;
	}
	return FALSE;
}

void ObjKill(OBJECT *obj)
{
	obj->flag = 0;
}

void objectlib_802A057C(void)
{
	ObjectClrActive();
	ObjectHide();
	ObjectHitOFF();
}

void ObjectHitOFF(void)
{
	object->o_hit_timer = -1;
}

void ObjectHitON(void)
{
	object->o_hit_timer = 0;
}

void ObjHitON(OBJECT *obj)
{
	obj->o_hit_timer = 0;
}

void ObjectCheckGroundY(void)
{
	BGFACE *ground;
	object->o_ground_y = BGCheckGround(
		object->o_posx, object->o_posy, object->o_posz, &ground
	);
}

BGFACE *ObjectCheckGround(void)
{
	BGFACE *ground;
	object->o_ground_y = BGCheckGround(
		object->o_posx, object->o_posy, object->o_posz, &ground
	);
	return ground;
}

static void CalcDrag(float *vel, float drag)
{
	if (*vel != 0)
	{
		float decel = SQUARE(*vel) * (drag*0.0001);
		if (*vel > 0)
		{
			*vel -= decel;
			if (*vel < +0.001) *vel = 0;
		}
		else
		{
			*vel += decel;
			if (*vel > -0.001) *vel = 0;
		}
	}
}

void ObjectCalcDrag(float drag)
{
	CalcDrag(&object->o_velx, drag);
	CalcDrag(&object->o_velz, drag);
}

static int objectlib_802A07E8(float ny, int flag)
{
	BGFACE *ground;
	float x = object->o_posx + object->o_velx;
	float z = object->o_posz + object->o_velz;
	float y = BGCheckGround(x, object->o_posy, z, &ground);
	float dy = y - object->o_ground_y;
	UNUSED float f;
	object->o_move &= ~OM_0400;
	if (object->o_area != -1 && ground)
	{
		if (
			ground->area != 0 && object->o_area != ground->area &&
			ground->area != 18
		) return FALSE;
	}
	if (y < -10000)
	{
		object->o_move |= OM_0400;
		return FALSE;
	}
	else if (dy < 5)
	{
		if (!flag)
		{
			object->o_posx = x;
			object->o_posz = z;
			return TRUE;
		}
		else if (dy < -50 && object->o_move & OM_TOUCH)
		{
			object->o_move |= OM_0400;
			return FALSE;
		}
		else if (ground->ny > ny)
		{
			object->o_posx = x;
			object->o_posz = z;
			return TRUE;
		}
		else
		{
			object->o_move |= OM_0400;
			return FALSE;
		}
	}
	else
	{
		float ground_ny;
		if ((ground_ny = ground->ny) > ny || object->o_posy > y)
		{
			object->o_posx = x;
			object->o_posz = z;
		}
	}
	return FALSE;
}

static void objectlib_802A0AB0(void)
{
	float accy = sqrtf(SQUARE(object->o_vely)) * (7*object->o_drag) / 100.0;
	if (object->o_vely > 0) object->o_vely -= accy;
	else                    object->o_vely += accy;
	if (object->o_posy < object->o_ground_y)
	{
		object->o_posy = object->o_ground_y;
		object->o_move |= OM_B_WATER;
	}
	else
	{
		object->o_move |= OM_U_WATER;
	}
}

static void objectlib_802A0BDC(UNUSED float gravity, float density)
{
	object->o_move &= ~OM_2000;
	if (object->o_posy < object->o_ground_y)
	{
		if (!(object->o_move & OM_TOUCH))
		{
			if (CheckFlag(&object->o_move, OM_BOUND))
			{
				object->o_move |= OM_TOUCH;
			}
			else
			{
				object->o_move |= OM_BOUND;
			}
		}
		object->o_posy = object->o_ground_y;
		if (object->o_vely < 0) object->o_vely *= density;
		if (object->o_vely > 5) object->o_move |= OM_2000;
	}
	else
	{
		object->o_move &= ~OM_BOUND;
		if (CheckFlag(&object->o_move, OM_TOUCH))
		{
			object->o_move |= OM_TAKEOFF;
		}
	}
	object->o_move &= ~(OM_DIVE|OM_S_WATER|OM_U_WATER|OM_B_WATER);
}

static float objectlib_802A0D84(float gravity, float bounce)
{
	float water_y;
	object->o_vely += gravity + bounce;
	if (object->o_vely < -78) object->o_vely = -78;
	object->o_posy += object->o_vely;
	if (object->flag & OBJ_0400) water_y = -11000;
	else water_y = BGCheckWater(object->o_posx, object->o_posz);
	return water_y;
}

void objectlib_802A0E68(float gravity, float density, float bounce)
{
	float water_y;
	object->o_move &= ~OM_TAKEOFF;
	if (object->o_move & OM_S_WATER)
	{
		if (object->o_vely > 5)
		{
			object->o_move &= ~(OM_DIVE|OM_S_WATER|OM_U_WATER|OM_B_WATER);
			object->o_move |= OM_1000;
		}
	}
	if (!(object->o_move & (OM_DIVE|OM_S_WATER|OM_U_WATER|OM_B_WATER)))
	{
		water_y = objectlib_802A0D84(gravity, 0);
		if (object->o_posy > water_y)
		{
			objectlib_802A0BDC(gravity, density);
		}
		else
		{
			object->o_move |= OM_DIVE;
			object->o_move &= ~(OM_BOUND|OM_TOUCH);
		}
	}
	else
	{
		object->o_move &= ~OM_DIVE;
		water_y = objectlib_802A0D84(gravity, bounce);
		if (object->o_posy < water_y)
		{
			objectlib_802A0AB0();
		}
		else if (object->o_posy < object->o_ground_y)
		{
			object->o_posy = object->o_ground_y;
			object->o_move &= ~(OM_DIVE|OM_S_WATER|OM_U_WATER|OM_B_WATER);
		}
		else
		{
			object->o_posy = water_y;
			object->o_vely = 0;
			object->o_move &= ~(OM_U_WATER|OM_B_WATER);
			object->o_move |= OM_S_WATER;
		}
	}
	if (object->o_move & (OM_BOUND|OM_TOUCH|OM_S_WATER|OM_U_WATER))
	{
		object->o_move &= ~OM_SKY;
	}
	else
	{
		object->o_move |= OM_SKY;
	}
}

UNUSED static void objectlib_802A10E0(void)
{
}

int CheckFlag(int *flag, int mask)
{
	if (*flag & mask)
	{
		*flag &= ~0^mask;
		return TRUE;
	}
	else
	{
		return FALSE;
	}
}

void ObjectHitWall(float offset, float radius)
{
	if (radius > 0.1) BGHitWall(
		&object->o_posx, &object->o_posy, &object->o_posz, offset, radius
	);
}

SHORT DeltaAng(SHORT a, SHORT b)
{
	short d = b - a;
	if (d == -0x8000) d = -0x7FFF;
	if (d < 0) d = -d;
	return d;
}

void ObjectMoveF(void)
{
	object->o_velx = object->o_velf * SIN(object->o_angy);
	object->o_velz = object->o_velf * COS(object->o_angy);
	object->o_posx += object->o_velx;
	object->o_posz += object->o_velz;
}

void ObjectMoveY(void)
{
	if (object->o_vely < -70) object->o_vely = -70;
	object->o_posy += object->o_vely;
}

void ObjectCalcVelF(void)
{
	object->o_velx = object->o_velf * SIN(object->o_angy);
	object->o_velz = object->o_velf * COS(object->o_angy);
}

float objectlib_802A1370(float x, float target, float limit, float speed)
{
	float d;
	if ((d = x-target) > 0)
	{
		if (d < +limit) return 0;
		else return -speed;
	}
	else
	{
		if (d > -limit) return 0;
		else return +speed;
	}
}

int ObjIsObjHit(OBJECT *obj, OBJECT *o)
{
	int i;
	for (i = 0; i < obj->hit_count; i++)
	{
		if (obj->hit[i] == o) return TRUE;
	}
	return FALSE;
}

void ObjectSetScript(OBJLANG *script)
{
	object->script = SegmentToVirtual(script);
}

void ObjSetScript(OBJECT *obj, OBJLANG *script)
{
	obj->script = SegmentToVirtual(script);
}

int ObjectHasScript(OBJLANG *script)
{
	if (object->script == SegmentToVirtual(script)) return TRUE;
	else return FALSE;
}

int ObjHasScript(OBJECT *obj, OBJLANG *script)
{
	if (obj->script == SegmentToVirtual(script)) return TRUE;
	else return FALSE;
}

float ObjectDistMarioToSave(void)
{
	float dist;
	float dx = object->o_savex - mario_obj->o_posx;
	float dz = object->o_savez - mario_obj->o_posz;
	dist = DIST2(dx, dz);
	return dist;
}

float ObjectDistToSave(void)
{
	float dist;
	float dx = object->o_savex - object->o_posx;
	float dz = object->o_savez - object->o_posz;
	dist = DIST2(dx, dz);
	return dist;
}

int ObjectInSaveSquare(float size)
{
	if (object->o_savex-size > object->o_posx) return TRUE;
	if (object->o_savex+size < object->o_posx) return TRUE;
	if (object->o_savez-size > object->o_posz) return TRUE;
	if (object->o_savez+size < object->o_posz) return TRUE;
	return FALSE;
}

int ObjectInSaveRect(float xmin, float xmax, float zmin, float zmax)
{
	if (object->o_savex+xmin > object->o_posx) return TRUE;
	if (object->o_savex+xmax < object->o_posx) return TRUE;
	if (object->o_savez+zmin > object->o_posz) return TRUE;
	if (object->o_savez+zmax < object->o_posz) return TRUE;
	return FALSE;
}

void ObjectSavePos(void)
{
	object->o_posx = object->o_savex;
	object->o_posy = object->o_savey;
	object->o_posz = object->o_savez;
}

void ObjectSavePosStop(void)
{
	ObjectSavePos();
	object->o_velf = 0;
	object->o_vely = 0;
}

void ObjectShake(float offy)
{
	if (!(object->o_timer & 1)) object->o_posy += offy;
	else                        object->o_posy -= offy;
}

void objectlib_802A1930(UNUSED OBJECT *obj, int a1)
{
	pl_camera_data[0].demo = a1;
	camera_8032DF30 = object;
}

void objectlib_802A1960(UNUSED OBJECT *obj, UNUSED int a1, float dist)
{
	if (object->o_targetdist < dist) mario_obj->o_hit_result = HR_000001;
}

void ObjSetBillboard(OBJECT *obj)
{
	obj->s.s.flag |= SHP_BILLBOARD;
}

void ObjectSetHitBox(float radius, float height)
{
	object->hit_r = radius;
	object->hit_h = height;
}

void ObjectSetDmgBox(float radius, float height)
{
	object->dmg_r = radius;
	object->dmg_h = height;
}

static void ObjectMakeCoinCommon(
	OBJECT *obj, int max, float f7, OBJLANG *script, SHORT range, SHORT shape
)
{
	int i;
	float y;
	BGFACE *ground;
	y = BGCheckGround(obj->o_posx, obj->o_posy, obj->o_posz, &ground);
	if (obj->o_posy-y > 100) y = obj->o_posy;
	for (i = 0; i < max; i++)
	{
		OBJECT *o;
		if (obj->o_ncoin <= 0) break;
		obj->o_ncoin--;
		o = ObjMakeHere(obj, shape, script);
		ObjRandOff2D(o, range);
		o->o_posy = y;
		o->o_f7 = f7;
	}
}

extern OBJLANG obj_130009A4[];
extern OBJLANG obj_13003104[];

static void objectlib_802A1B34(OBJECT *obj, int max, float f7, SHORT range)
{
	ObjectMakeCoinCommon(obj, max, f7, obj_13003104, range, S_BLUECOIN);
}

void ObjectMakeCoin(OBJECT *obj, int max, float f7)
{
	ObjectMakeCoinCommon(obj, max, f7, obj_130009A4, 0, S_COIN);
}

void objectlib_802A1BDC(void)
{
	OBJECT *o;
	if (object->o_ncoin <= 0) return;
	object->o_ncoin--;
	o = ObjMakeHere(object, S_COIN, obj_130009A4);
	o->o_vely = 30;
	ObjCopyPos(o, mario_obj);
}

float ObjectDistToSaveY(void)
{
	float dy = object->o_savey - object->o_posy;
	if (dy < 0) dy = -dy;
	return dy;
}

int objectlib_802A1CC4(void)
{
	int f = object->s.skel.frame;
	int frame = object->s.skel.anime->frame;
	int result;
	if      (f < 0)         f = 0;
	else if (f == frame-1)  f = 0;
	else                    f++;
	result = 0x10000*f/frame;
	return result;
}

static int objectlib_802A1D7C(SHORT ang)
{
	BGFACE *ground;
	float x, y, z, dy, ny = COS(182*ang);
	if (object->o_velf != 0)
	{
		x = object->o_posx + object->o_velx;
		z = object->o_posz + object->o_velz;
		y = BGCheckGround(x, object->o_posy, z, &ground);
		dy = y - object->o_ground_y;
		if (y < -10000)
		{
			object->o_bg_ang = object->o_angy + 0x8000;
			return 2;
		}
		else if (ground->ny < ny && dy > 0 && y > object->o_posy)
		{
			object->o_bg_ang = ATAN2(ground->nz, ground->nx);
			return 1;
		}
		else
		{
			return 0;
		}
	}
	return 0;
}

int ObjectCheckWall(void)
{
	int count;
	BGFACE *wall;
	WALLCHECK check;
	float offset = 10;
	float radius = object->o_wall_r;
	if (radius > 0.1)
	{
		check.offset = offset;
		check.radius = radius;
		check.x = (short)object->o_posx;
		check.y = (short)object->o_posy;
		check.z = (short)object->o_posz;
		if ((count = BGCheckWall(&check)))
		{
			object->o_posx = check.x;
			object->o_posy = check.y;
			object->o_posz = check.z;
			wall = check.wall[check.count-1];
			object->o_bg_ang = ATAN2(wall->nz, wall->nx);
			if (DeltaAng(object->o_bg_ang, object->o_angy) > 0x4000)
			{
				return TRUE;
			}
			else
			{
				return FALSE;
			}
		}
	}
	return FALSE;
}

static void objectlib_802A20F4(void)
{
	BGFACE *ground = ObjectCheckGround();
	object->o_ground = ground;
	if (ground)
	{
		if      (ground->code == BG_1)  object->o_move |= OM_0800;
#if REVISION >= 199609
		else if (ground->code == BG_10) object->o_move |= OM_4000;
#endif
		object->o_bgcode = ground->code;
		object->o_bgarea = ground->area;
	}
	else
	{
		object->o_bgcode = 0;
		object->o_bgarea = 0;
	}
}

static void objectlib_802A21D4(SHORT ang)
{
#if REVISION >= 199609
	object->o_move &= ~(OM_0800|OM_4000);
#else
	object->o_move &= ~OM_0800;
#endif
	if (object->flag & (OBJ_0002|OBJ_0008))
	{
		objectlib_802A20F4();
		object->o_move &= ~(OM_DIVE|OM_S_WATER|OM_U_WATER|OM_B_WATER|OM_0200);
		if (object->o_posy > object->o_ground_y) object->o_move |= OM_SKY;
	}
	else
	{
		object->o_move &= ~OM_0200;
		if (ObjectCheckWall()) object->o_move |= OM_0200;
		objectlib_802A20F4();
		if (object->o_posy > object->o_ground_y) object->o_move |= OM_SKY;
		if (objectlib_802A1D7C(ang)) object->o_move |= OM_0200;
	}
}

/* objcall */
void objectlib_802A2320(void)
{
	objectlib_802A21D4(60);
}

void objectlib_802A2348(SHORT ang)
{
	float gravity = object->o_gravity;
	float density = object->o_density;
	float bounce = object->o_bounce;
	float drag = object->o_drag;
	float ny;
	int negang = FALSE;
	int negvel = FALSE;
	if (!(object->flag & (OBJ_0002|OBJ_0008)))
	{
		if (ang < 0) {negang = TRUE; ang = -ang;}
		ny = COS(182 * ang);
		ObjectCalcVelF();
		ObjectCalcDrag(drag);
		objectlib_802A07E8(ny, negang);
		objectlib_802A0E68(gravity, density, bounce);
		if (object->o_velf < 0) negvel = TRUE;
		object->o_velf = DIST2(object->o_velx, object->o_velz);
		if (ISTRUE(negvel)) object->o_velf = -object->o_velf;
	}
}

static int objectlib_802A24D0(void)
{
	if (object->o_posx < -12000 || 12000 < object->o_posx) return FALSE;
	if (object->o_posy < -12000 || 12000 < object->o_posy) return FALSE;
	if (object->o_posz < -12000 || 12000 < object->o_posz) return FALSE;
	return TRUE;
}

void ObjectProcMove(void)
{
	if (objectlib_802A24D0())
	{
		object->o_posx += object->o_velx;
		object->o_posz += object->o_velz;
		object->o_vely += object->o_gravity;
		object->o_posy += object->o_vely;
	}
}

void ObjectProcMoveF(void)
{
	ObjectCalcVelF();
	ObjectProcMove();
}

void ObjCopyCoordOff(
	OBJECT *obj, OBJECT *o, float offx, float offy, float offz
)
{
	float cy = COS(o->o_angy);
	float sy = SIN(o->o_angy);
	float z = offz*cy - offx*sy;
	float x = offz*sy + offx*cy;
	obj->o_angy = o->o_angy;
	obj->o_posx = o->o_posx + x;
	obj->o_posy = o->o_posy + offy;
	obj->o_posz = o->o_posz + z;
}

SHORT ObjectAngToSave(void)
{
	SHORT angy;
	float dx = object->o_savex - object->o_posx;
	float dz = object->o_savez - object->o_posz;
	angy = ATAN2(dz, dx);
	return angy;
}

void ObjCopyCoordToShape(OBJECT *obj, OBJECT *o)
{
	obj->s.pos[0] = o->o_posx;
	obj->s.pos[1] = o->o_posy + o->o_shapeoff;
	obj->s.pos[2] = o->o_posz;
	obj->s.ang[0] = o->o_angx & 0xFFFF;
	obj->s.ang[1] = o->o_angy & 0xFFFF;
	obj->s.ang[2] = o->o_angz & 0xFFFF;
}

void ObjAddTransform(OBJECT *obj, SHORT dst, SHORT src)
{
	float x = obj->work[src+0].f;
	float y = obj->work[src+1].f;
	float z = obj->work[src+2].f;
	obj->work[dst+0].f += MDOT3(obj->mtx, 0, x, y, z);
	obj->work[dst+1].f += MDOT3(obj->mtx, 1, x, y, z);
	obj->work[dst+2].f += MDOT3(obj->mtx, 2, x, y, z);
}

void ObjCalcMtx(OBJECT *obj, SHORT pos, SHORT ang)
{
	FVEC vpos;
	SVEC vang;
	vpos[0] = obj->work[pos+0].f;
	vpos[1] = obj->work[pos+1].f;
	vpos[2] = obj->work[pos+2].f;
	vang[0] = obj->work[ang+0].i;
	vang[1] = obj->work[ang+1].i;
	vang[2] = obj->work[ang+2].i;
	FMtxCoord(obj->mtx, vpos, vang);
}

void ObjSetMtx(OBJECT *obj)
{
	if (obj->o_flag & OF_CALCMTX)
	{
		ObjCalcMtx(obj, O_POS, O_SHAPEANG);
		ObjScaleMtx(obj);
	}
	obj->s.m = &obj->mtx;
	ObjectSetScale(1);
}

void ObjCalcRel(OBJECT *obj)
{
	OBJECT *parent = obj->parent;
	ObjCalcMtx(obj, O_REL, O_SHAPEANG);
	ObjScaleMtx(obj);
	FMtxCatAffine(obj->mtx, obj->mtx, parent->mtx);
	obj->o_posx = obj->mtx[3][0];
	obj->o_posy = obj->mtx[3][1];
	obj->o_posz = obj->mtx[3][2];
	obj->s.m = &obj->mtx;
	ObjectSetScale(1);
}

void ObjClrRel(OBJECT *obj)
{
	obj->o_flag &= ~OF_CALCREL;
	obj->o_flag |= OF_SETMTX;
	obj->mtx[3][0] = obj->o_posx;
	obj->mtx[3][1] = obj->o_posy;
	obj->mtx[3][2] = obj->o_posz;
}

void ObjectRotate(void)
{
	object->o_angx += object->o_rotx;
	object->o_angy += object->o_roty;
	object->o_angz += object->o_rotz;
}

void ObjectRotateShape(void)
{
	object->o_shapeangx += object->o_rotx;
	object->o_shapeangy += object->o_roty;
	object->o_shapeangz += object->o_rotz;
}

void ObjectSyncAng(void)
{
	object->o_shapeangx = object->o_angx;
	object->o_shapeangy = object->o_angy;
	object->o_shapeangz = object->o_angz;
}

int ObjectProcPath(UNUSED int status)
{
	PATH *end, *path, *next;
	float dx, dy, dz;
	UNUSED float d;
	float dist, distx, disty, distz;
	if (object->o_v4 == 0)
	{
		object->o_p3 = object->o_p2;
		object->o_v4 = 0x8000;
	}
	end = object->o_p2;
	path = object->o_p3;
	if (path[4+0] != -1)    next = path + 4;
	else                    next = end;
	object->o_v4 = path[0] | 0x8000;
	dx = next[1] - path[1];
	dy = next[2] - path[2];
	dz = next[3] - path[3];
	distx = next[1] - object->o_posx;
	disty = next[2] - object->o_posy;
	distz = next[3] - object->o_posz;
	dist = DIST2(distx, distz);
	object->o_v6 = ATAN2(distz, distx);
	object->o_v5 = ATAN2(dist, -disty);
	if (dx*distx + dy*disty + dz*distz <= 0)
	{
		object->o_p3 = next;
		if (next[4+0] == -1)    return -1;
		else                    return 1;
	}
	return 0;
}

void ChainInit(CHAIN *chain)
{
	chain->posx = 0;
	chain->posy = 0;
	chain->posz = 0;
	chain->angx = 0;
	chain->angy = 0;
	chain->angz = 0;
}

float RandRange(float range)
{
	return RandF()*range - range/2;
}

void ObjRandScale(OBJECT *obj, float range, float start)
{
	float scale = RandF()*range + start;
	ObjSetScaleXYZ(obj, scale, scale, scale);
}

void ObjRandOff3D(OBJECT *obj, float range)
{
	obj->o_posx += RandF()*range - range*0.5F;
	obj->o_posy += RandF()*range - range*0.5F;
	obj->o_posz += RandF()*range - range*0.5F;
}

void ObjRandOff2D(OBJECT *obj, float range)
{
	obj->o_posx += RandF()*range - range*0.5F;
	obj->o_posz += RandF()*range - range*0.5F;
}

static void ObjCalcVelULF(OBJECT *obj)
{
	float u = obj->o_velu;
	float l = obj->o_vell;
	float f = obj->o_velf;
	obj->o_velx = MDOT3(obj->mtx, 0, u, l, f);
	obj->o_vely = MDOT3(obj->mtx, 1, u, l, f);
	obj->o_velz = MDOT3(obj->mtx, 2, u, l, f);
}

void ObjectMoveULF(void)
{
	ObjCalcMtx(object, O_REL, O_ANG);
	ObjCalcVelULF(object);
	object->o_posx += object->o_velx;
	object->o_posy += object->o_vely;
	object->o_posz += object->o_velz;
}

short objectlib_802A3268(void)
{
	short angy =
		object->o_bg_ang - ((short)object->o_angy-(short)object->o_bg_ang) +
		0x8000;
	return angy;
}

extern OBJLANG obj_130007DC[];

void ObjectMakeParticle(PARTICLE *part)
{
	OBJECT *o;
	int i;
	float scale;
	int count = part->count;
	if (obj_prevcount > 150)
	{
		if (count > 10) count = 10;
	}
	if (obj_prevcount > 210) count = 0;
	for (i = 0; i < count; i++)
	{
		scale = RandF()*(part->scale_range*0.1F) + (part->scale_start*0.1F);
		o = ObjMakeHere(object, part->shape, obj_130007DC);
		o->o_code = part->code;
		o->o_angy = Rand();
		o->o_gravity = part->gravity;
		o->o_drag = part->drag;
		o->o_posy += part->offset;
		o->o_velf = RandF()*part->velf_range + part->velf_start;
		o->o_vely = RandF()*part->vely_range + part->vely_start;
		ObjSetScaleXYZ(o, scale, scale, scale);
	}
}

void ObjSetHitInfo(OBJECT *obj, HITINFO *hit)
{
	if (!(obj->o_flag & OF_HITINFO))
	{
		obj->o_flag |= OF_HITINFO;
		obj->o_hit_type = hit->type;
		obj->o_ap = hit->ap;
		obj->o_hp = hit->hp;
		obj->o_ncoin = hit->ncoin;
		ObjectHitON();
	}
	obj->hit_r = obj->s.scale[0] * hit->hit_r;
	obj->hit_h = obj->s.scale[1] * hit->hit_h;
	obj->dmg_r = obj->s.scale[0] * hit->dmg_r;
	obj->dmg_h = obj->s.scale[1] * hit->dmg_h;
	obj->hit_offset = obj->s.scale[1] * hit->offset;
}

int GetSign(int x)
{
	if (x >= 0) return +1;
	else        return -1;
}

float fabsf(float x)
{
	if (x >= 0) return +x;
	else        return -x;
}

int abs(int i)
{
	if (i >= 0) return +i;
	else        return -i;
}

int ObjectFlash(int start, int count)
{
	int result = FALSE;
	if (object->o_timer >= start)
	{
		int t;
		if ((t = object->o_timer-start) & 1)
		{
			object->s.s.flag |= SHP_OBJHIDE;
			if (t/2 > count) result = TRUE;
		}
		else
		{
			object->s.s.flag &= ~SHP_OBJHIDE;
		}
	}
	return result;
}

int objectlib_802A3754(void)
{
	if (object == mario_obj->movebg)
	{
		if (player_data[0].state == PS_WAIT_3C) return TRUE;
	}
	return FALSE;
}

void objectlib_802A37AC(void)
{
	enemya_802AAE8C(0, 0, 46);
}

void objectlib_802A37DC(Na_Se se)
{
	enemya_802AAE8C(0, 0, 46);
	ObjectMakeSound(se);
}

void ObjectRepelMario2D(float radius)
{
	float dx = mario_obj->o_posx - object->o_posx;
	float dz = mario_obj->o_posz - object->o_posz;
	float dist = DIST2(dx, dz);
	if (dist < radius)
	{
		player_data[0].pos[0] += (radius-dist)/radius * dx;
		player_data[0].pos[2] += (radius-dist)/radius * dz;
	}
}

void ObjectRepelMario3D(float radius, float height)
{
	float dy = mario_obj->o_posy - object->o_posy;
	if (dy < 0) dy = -dy;
	if (dy < height) ObjectRepelMario2D(radius);
}

void objectlib_802A399C(void)
{
	object->o_posx += object->o_velx;
	object->o_posy += object->o_vely;
	object->o_posz += object->o_velz;
	if (object->o_v0 == 10) ObjKill(object);
	object->o_v0++;
}

UNUSED static void objectlib_802A3A3C(void)
{
}

CHAR objectlib_802A3A4C(void *table)
{
	object->o_p8 = table;
	object->o_v9 = 0;
	return ((s8 *)object->o_p8)[0];
}

CHAR objectlib_802A3A88(void)
{
	CHAR result;
	s8 *table = object->o_p8;
	int index = object->o_v9 + 1;
	if (table[index] != -1)
	{
		result = table[index];
		object->o_v9++;
	}
	else
	{
		result = table[0];
		object->o_v9 = 0;
	}
	return result;
}

void objectlib_802A3B28(UNUSED OBJECT *obj, UNUSED OBJECT *o)
{
}

void ObjectScaleTime(int flag, int time, float min, float max)
{
	float range = max - min;
	float t = (float)object->o_timer / time;
	if (flag & 1) object->s.scale[0] = min + range*t;
	if (flag & 2) object->s.scale[1] = min + range*t;
	if (flag & 4) object->s.scale[2] = min + range*t;
}

void ObjectDebugPos(void)
{
	object->o_posx = object->o_savex + db_work[5][0];
	object->o_posy = object->o_savey + db_work[5][1];
	object->o_posz = object->o_savez + db_work[5][2];
	ObjectSetScale((float)db_work[5][3]/100 + 1.0);
}

UNUSED static void objectlib_802A3CEC(void)
{
}

int ObjectIsMarioBG(void)
{
	if (object == mario_obj->movebg)    return TRUE;
	else                                return FALSE;
}

int objectlib_802A3D40(int count, int offy)
{
	if (object->o_timer & 1)    object->o_posy -= offy;
	else                        object->o_posy += offy;
	if (object->o_timer == 2*count) return TRUE;
	else                            return FALSE;
}

int objectlib_802A3DD4(int index)
{
	static signed char table[] = {-8, 8, -4, 4};
	if (index >= 4 || index < 0) return TRUE;
	object->o_posy += table[index];
	return FALSE;
}

void ObjectCallMode(OBJCALL **modetab)
{
	OBJCALL *call = modetab[object->o_mode];
	call();
}

extern OBJLANG obj_1300080C[];

static OBJECT *objectlib_802A3E80(int code, int v9)
{
	OBJECT *o = ObjMakeHere(object, S_POWERSTAR, obj_1300080C);
	o->o_v9 = v9;
	o->o_actorinfo = object->o_actorinfo;
	o->o_code = code;
	return o;
}

void objectlib_802A3EF8(void)
{
	objectlib_802A3E80(0, 0);
}

int GetBit(int index)
{
	static short bittab[] = {0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80};
	return bittab[index];
}

int objectlib_802A3F48(void)
{
	float dx = object->o_savex - mario_obj->o_posx;
	float dy = object->o_savey - mario_obj->o_posy;
	float dz = object->o_savez - mario_obj->o_posz;
	float dist = DIST3(dx, dy, dz);
	if (object->o_targetdist > 2000 && dist > 2000) return TRUE;
	else                                            return FALSE;
}

int objectlib_802A404C(int speed)
{
	if (player_data[0].speed > speed)   return TRUE;
	if (player_data[0].state & PF_JUMP) return TRUE;
	else                                return FALSE;
}

int InTable(CHAR value, s8 *table)
{
	while (*table != -1)
	{
		if (*table == value) return TRUE;
		table++;
	}
	return FALSE;
}

UNUSED static void objectlib_802A4110(void)
{
}

void ObjectInitArea(void)
{
	static s8 areastagetab[] =
	{
		STAGE_BBH,
		STAGE_INSIDE,
		STAGE_HMC,
		-1,
	};
	if (InTable(stage_index, areastagetab))
	{
		BGFACE *ground;
		float ground_y = BGCheckGround(
			object->o_posx, object->o_posy, object->o_posz, &ground
		);
		if (ground)
		{
			if (ground->area != 0)
			{
				object->o_area = ground->area;
			}
			else
			{
				BGCheckGround(
					object->o_posx, ground_y-100, object->o_posz, &ground
				);
				if (ground) object->o_area = ground->area;
			}
		}
	}
	else
	{
		object->o_area = -1;
	}
}

void ObjectProcArea(void)
{
	if (object->o_area != -1 && object_80361250 != 0)
	{
		register int flag;
		if      (object_80361250 == object->o_area)                flag = TRUE;
		else if (area_table[object_80361250][0] == object->o_area) flag = TRUE;
		else if (area_table[object_80361250][1] == object->o_area) flag = TRUE;
		else                                                       flag = FALSE;
		if (flag)
		{
			ObjectSetActive();
			object->flag &= ~OBJ_0008;
			object_8036125E++;
		}
		else
		{
			ObjectClrActive();
			object->flag |= OBJ_0008;
			object_80361260++;
		}
	}
}

int objectlib_802A4360(HITINFO *hit, Na_Se se, int nocoin)
{
	int result = FALSE;
	ObjSetHitInfo(object, hit);
	if (nocoin) object->o_ncoin = 0;
	if (object->o_hit_result & HR_008000)
	{
		if (object->o_hit_result & HR_004000)
		{
			objectlib_802A37AC();
			ObjectMakeCoin(object, object->o_ncoin, 20);
			ObjKill(object);
			ObjectMakeSound(se);
		}
		else
		{
			result = TRUE;
		}
	}
	object->o_hit_result = 0;
	return result;
}

void objectlib_802A4440(float a0, int a1)
{
	enemya_802AAE8C(0, 0, a0);
	enemya_802AE0CC(30, S_SHARD, 3, 4);
	ObjKill(object);
	if      (a1 == 1)   ObjectMakeCoin(object, object->o_ncoin, 20);
	else if (a1 == 2)   objectlib_802A1B34(object, object->o_ncoin, 20, 150);
}

void ObjSetMap(OBJECT *obj, MAP *map)
{
	obj->map = SegmentToVirtual(map);
}

void objectlib_802A452C(void)
{
	if (object->o_move & OM_0200) object->o_angy = object->o_bg_ang;
}

int objectlib_802A4564(float height)
{
	if (fabsf(object->o_posy - mario_obj->o_posy) < height)
	{
		ObjectShow();
		return FALSE;
	}
	else
	{
		ObjectHide();
		return TRUE;
	}
}

void *Ctrl_objectlib_802A45E4(int code, SHAPE *shape, UNUSED void *data)
{
	if (code == SC_DRAW)
	{
		((SCOORD *)shape->next)->pos[0] = 300;
		((SCOORD *)shape->next)->pos[1] = 300;
		((SCOORD *)shape->next)->pos[2] = 0;
	}
	return NULL;
}

void *Ctrl_objectlib_802A462C(int code, SHAPE *shape, UNUSED void *data)
{
	if (code == SC_DRAW)
	{
		((SCOORD *)shape->next)->pos[0] = db_work[4][0];
		((SCOORD *)shape->next)->pos[1] = db_work[4][1];
		((SCOORD *)shape->next)->pos[2] = db_work[4][2];
		((SCOORD *)shape->next)->ang[0] = db_work[4][3];
		((SCOORD *)shape->next)->ang[1] = db_work[4][4];
		((SCOORD *)shape->next)->ang[2] = db_work[4][5];
	}
	return NULL;
}

int ObjIsHide(OBJECT *obj)
{
	if (obj->s.s.flag & SHP_OBJHIDE)    return TRUE;
	else                                return FALSE;
}

void objectlib_802A4704(void)
{
	object_flag |= OBJECT_FREEZE;
}

void objectlib_802A4728(void)
{
	object_flag &= ~OBJECT_FREEZE;
}

void objectlib_802A4750(unsigned int flag)
{
	object_flag |= flag;
}

void objectlib_802A4774(unsigned int flag)
{
	object_flag = (~0^flag) & object_flag;
}

int objectlib_802A47A0(float radius, float height, UNUSED SHORT range)
{
	if (object->o_targetdist < 1500)
	{
		float dist = ObjCalcDist2D(object, mario_obj);
		UNUSED SHORT dang = ObjCalcAngY(mario_obj, object);
		if (
			dist < radius &&
			object->o_posy < mario_obj->o_posy+160 &&
			mario_obj->o_posy < object->o_posy+height &&
			!(player_data[0].state & PF_JUMP) &&
			pldemo_802575A8()
		) return TRUE;
	}
	return FALSE;
}

int objectlib_802A48BC(float radius, float height)
{
	return objectlib_802A47A0(radius, height, 0x1000);
}

static void objectlib_802A48FC(int flag, int status)
{
	object->o_msg_status = status;
	object->o_msg_phase++;
	if (!(flag & 0x10)) pldemo_80257640(0);
}

int objectlib_802A4960(int a0, int flag, int msg, UNUSED int a3)
{
	int result = 0;
	UNUSED int inrange = TRUE;
	switch (object->o_msg_phase)
	{
	case 0:
#if REVISION >= 199609
		if (pldemo_802575A8() || mario->state == PS_DEMO_06)
		{
			object_flag |= OBJECT_FREEZE;
			object->flag |= OBJ_0020;
			object->o_msg_phase++;
		}
		else
		{
			break;
		}
		FALLTHROUGH;
#else
		if (mario->power >= 0x100)
		{
			object_flag |= OBJECT_FREEZE;
			object->flag |= OBJ_0020;
			object->o_msg_phase++;
		}
		break;
#endif
	case 1:
		if (pldemo_80257640(a0) == 2) object->o_msg_phase++;
		break;
	case 2:
		if      (flag & 4)  MsgOpenPrompt(msg);
		else if (flag & 2)  MsgOpen(msg);
		object->o_msg_phase++;
		break;
	case 3:
		if (flag & 4)
		{
			if (msg_answer) objectlib_802A48FC(flag, msg_answer);
		}
		else if (flag & 2)
		{
			if (MsgGet() == MSG_NULL) objectlib_802A48FC(flag, 3);
		}
		else
		{
			objectlib_802A48FC(flag, 3);
		}
		break;
	case 4:
		if (mario->state != PS_DEMO_06 || flag & 0x10)
		{
			object_flag &= ~OBJECT_FREEZE;
			object->flag &= ~OBJ_0020;
			result = object->o_msg_status;
			object->o_msg_phase = 0;
		}
		break;
	default:
		object->o_msg_phase = 0;
		break;
	}
	return result;
}

int objectlib_802A4BE4(int a0, int flag, int a2, int msg)
{
	int result = 0;
	int inrange = TRUE;
	switch (object->o_msg_phase)
	{
	case 0:
#if REVISION >= 199609
		if (pldemo_802575A8() || mario->state == PS_DEMO_06)
		{
			object_flag |= OBJECT_FREEZE;
			object->flag |= OBJ_0020;
			object->o_msg_phase++;
			object->o_msg_status = 0;
		}
		else
		{
			break;
		}
		FALLTHROUGH;
#else
		if (mario->power >= 0x100)
		{
			object_flag |= OBJECT_FREEZE;
			object->flag |= OBJ_0020;
			object->o_msg_phase++;
			object->o_msg_status = 0;
		}
		break;
#endif
	case 1:
		if (flag & 1)
		{
			inrange = ObjectTurn(ObjCalcAngY(object, mario_obj), 0x800);
			if (object->o_msg_status > 32) inrange = TRUE;
		}
		if (pldemo_80257640(a0) == 2 && inrange)
		{
			object->o_msg_status = 0;
			object->o_msg_phase++;
		}
		else
		{
			object->o_msg_status++;
		}
		break;
	case 2:
		if (a2 == 161)
		{
			if ((object->o_msg_status = camera_8028FFC8(a2, object)))
			{
				object->o_msg_phase++;
			}
		}
		else
		{
			if ((object->o_msg_status = camera_8028FF04(a2, object, msg)))
			{
				object->o_msg_phase++;
			}
		}
		break;
	case 3:
		if (flag & 0x10)
		{
			result = object->o_msg_status;
			object->o_msg_phase = 0;
		}
		else if (mario->state != PS_DEMO_06)
		{
			object_flag &= ~OBJECT_FREEZE;
			object->flag &= ~OBJ_0020;
			result = object->o_msg_status;
			object->o_msg_phase = 0;
		}
		else
		{
			pldemo_80257640(0);
		}
		break;
	}
	return result;
}

int ObjectHasShapeID(USHORT shape)
{
	if (object->s.shape == shape_table[shape])  return TRUE;
	else                                        return FALSE;
}

void ObjectStand(void)
{
	BGFACE *ground;
	FVEC normal, pos;
	pos[0] = object->o_posx;
	pos[1] = object->o_posy;
	pos[2] = object->o_posz;
	BGCheckGround(pos[0], pos[1], pos[2], &ground);
	if (ground)
	{
		normal[0] = ground->nx;
		normal[1] = ground->ny;
		normal[2] = ground->nz;
		FMtxStand(object->mtx, normal, pos, object->o_shapeangy);
		object->s.m = &object->mtx;
	}
}

int MarioInRect(SHORT xmin, SHORT xmax, SHORT zmin, SHORT zmax)
{
	if (mario_obj->o_posx < xmin || xmax < mario_obj->o_posx) return FALSE;
	if (mario_obj->o_posz < zmin || zmax < mario_obj->o_posz) return FALSE;
	return TRUE;
}

void objectlib_802A50FC(int a0)
{
	camera_8027F9F0(a0, object->o_posx, object->o_posy, object->o_posz);
}

int objectlib_802A513C(OBJECT *obj)
{
	int count;
	OBJECT *o;
	int result = FALSE;
	count = obj->hit_count;
	if (count != 0)
	{
		o = obj->hit[0];
		if (o != mario_obj)
		{
			o->o_hit_result |= HR_000001|HR_004000|HR_008000|HR_800000;
			result = TRUE;
		}
	}
	return result;
}

int objectlib_802A51AC(void)
{
	int result = FALSE;
	if (object->o_hit_result & HR_008000 && object->o_hit_result & HR_004000)
	{
		result = TRUE;
	}
	if (objectlib_802A3754()) result = TRUE;
	object->o_hit_result = 0;
	return result;
}

void ObjCopyActorInfo(OBJECT *obj, OBJECT *o)
{
	obj->o_actorinfo = o->o_actorinfo;
	obj->o_code = o->o_code;
}

void ObjectSetAnimeFrame(int anime, int frame)
{
	ObjectSetAnime(anime);
	object->s.skel.frame = frame;
}

int objectlib_802A5288(int anime)
{
	ObjectSetAnime(anime);
	return objectlib_8029FF04();
}

void ObjectSetAnimeHoldEnd(int anime)
{
	ObjectSetAnime(anime);
	ObjectAnimeHoldEnd();
}

int objectlib_802A52F8(void)
{
	if (object->o_hit_result & HR_000800)
	{
		object->work[O_VAR].i = 1;
		ObjectHitOFF();
		return TRUE;
	}
	return FALSE;
}

int objectlib_802A5358(void)
{
	static int stick_flag;
	int result = 0;
	if (cont1->dist < 30) stick_flag = FALSE;
	if (!stick_flag && cont1->dist > 40)
	{
		stick_flag = TRUE;
		result = TRUE;
	}
	if (cont1->down & A_BUTTON) result = TRUE;
	return result;
}

void objectlib_802A540C(int l, int r, Na_Se se)
{
	if (ObjectIsAnimeFrame(l) || ObjectIsAnimeFrame(r))
	{
		ObjectPlaySound(se);
	}
}

void objectlib_802A5460(void)
{
	object_flag |= OBJECT_FREEZE|OBJECT_FREEZEPLAYER;
	object->flag |= OBJ_0020;
}

void objectlib_802A5498(void)
{
	object_flag &= ~(OBJECT_FREEZE|OBJECT_FREEZEPLAYER);
	object->flag &= ~OBJ_0020;
}

int objectlib_802A54D8(void)
{
	if (object->o_hit_result & HR_008000)
	{
		object->o_hit_result = 0;
		return TRUE;
	}
	else
	{
		return FALSE;
	}
}

extern OBJLANG obj_13000830[];

void objectlib_802A5524(void)
{
	if (object->o_ncoin >= 5)
	{
		ObjMakeHere(object, S_BLUECOIN, obj_13000830);
		object->o_ncoin -= 5;
	}
}

#if REVISION >= 199609
void objectlib_802A5588(float x, float y, float z, float offy)
{
	float posy = object->o_posy;
	object->o_posy += offy + db_work[5][0];
	enemyb_802F2B88(x, y, z);
	object->o_posy = posy;
}
#endif
