#include <sm64.h>

static void ShpInit(SHAPE *shape, int type)
{
	shape->type = type;
	shape->flag = SHP_ACTIVE;
	shape->prev = shape;
	shape->next = shape;
	shape->parent = NULL;
	shape->child = NULL;
}

SSCENE *ShpCreateScene(
	ARENA *arena, SSCENE *shp, SHORT index, SHORT x, SHORT y, SHORT w, SHORT h
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SSCENE));
	if (shp)
	{
		ShpInit(&shp->s, ST_SCENE);
		shp->index = index;
		shp->screen = 0;
		shp->x = x;
		shp->y = y;
		shp->w = w;
		shp->h = h;
		shp->reftab = NULL;
		shp->reflen = 0;
	}
	return shp;
}

SORTHO *ShpCreateOrtho(ARENA *arena, SORTHO *shp, float scale)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SORTHO));
	if (shp)
	{
		ShpInit(&shp->s, ST_ORTHO);
		shp->scale = scale;
	}
	return shp;
}

SPERSP *ShpCreatePersp(
	ARENA *arena, SPERSP *shp, float fovy, SHORT near, SHORT far,
	SHPCALL *callback, unsigned long arg
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SPERSP));
	if (shp)
	{
		ShpInit(&shp->s.s, ST_PERSP);
		shp->fovy = fovy;
		shp->near = near;
		shp->far = far;
		shp->s.callback = callback;
		shp->s.arg = arg;
		if (callback) callback(SC_INIT, &shp->s.s, arena);
	}
	return shp;
}

SHAPE *ShpCreateEmpty(ARENA *arena, SHAPE *shp)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SHAPE));
	if (shp)
	{
		ShpInit(shp, ST_EMPTY);
	}
	return shp;
}

SLAYER *ShpCreateLayer(ARENA *arena, SLAYER *shp, SHORT zb)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SLAYER));
	if (shp)
	{
		ShpInit(&shp->s, ST_LAYER);
		if (zb) shp->s.flag |= SHP_ZBUFFER;
	}
	return shp;
}

SLOD *ShpCreateLOD(ARENA *arena, SLOD *shp, SHORT min, SHORT max)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SLOD));
	if (shp)
	{
		ShpInit(&shp->s, ST_LOD);
		shp->min = min;
		shp->max = max;
	}
	return shp;
}

SSELECT *ShpCreateSelect(
	ARENA *arena, SSELECT *shp, SHORT code, SHORT index,
	SHPCALL *callback, unsigned long arg
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SSELECT));
	if (shp)
	{
		ShpInit(&shp->s.s, ST_SELECT);
		shp->code = code;
		shp->index = index;
		shp->s.callback = callback;
		shp->s.arg = arg;
		if (callback) callback(SC_INIT, &shp->s.s, arena);
	}
	return shp;
}

SCAMERA *ShpCreateCamera(
	ARENA *arena, SCAMERA *shp, FVEC eye, FVEC look,
	SHPCALL *callback, unsigned long arg
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SCAMERA));
	if (shp)
	{
		ShpInit(&shp->s.s, ST_CAMERA);
		FVecCpy(shp->eye, eye);
		FVecCpy(shp->look, look);
		shp->s.callback = callback;
		shp->s.arg = arg;
		shp->angz_m = 0;
		shp->angz_p = 0;
		if (callback) callback(SC_INIT, &shp->s.s, arena);
	}
	return shp;
}

SCOORD *ShpCreateCoord(
	ARENA *arena, SCOORD *shp, int layer, Gfx *gfx, SVEC pos, SVEC ang
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SCOORD));
	if (shp)
	{
		ShpInit(&shp->s.s, ST_COORD);
		SVecCpy(shp->pos, pos);
		SVecCpy(shp->ang, ang);
		ShpSetLayer(&shp->s.s, layer);
		shp->s.gfx = gfx;
	}
	return shp;
}

SPOS *ShpCreatePos(ARENA *arena, SPOS *shp, int layer, Gfx *gfx, SVEC pos)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SPOS));
	if (shp)
	{
		ShpInit(&shp->s.s, ST_POS);
		SVecCpy(shp->pos, pos);
		ShpSetLayer(&shp->s.s, layer);
		shp->s.gfx = gfx;
	}
	return shp;
}

SANG *ShpCreateAng(ARENA *arena, SANG *shp, int layer, Gfx *gfx, SVEC ang)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SANG));
	if (shp)
	{
		ShpInit(&shp->s.s, ST_ANG);
		SVecCpy(shp->ang, ang);
		ShpSetLayer(&shp->s.s, layer);
		shp->s.gfx = gfx;
	}
	return shp;
}

SSCALE *ShpCreateScale(
	ARENA *arena, SSCALE *shp, int layer, Gfx *gfx, float scale
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SSCALE));
	if (shp)
	{
		ShpInit(&shp->s.s, ST_SCALE);
		ShpSetLayer(&shp->s.s, layer);
		shp->scale = scale;
		shp->s.gfx = gfx;
	}
	return shp;
}

SOBJECT *ShpCreateObject(
	ARENA *arena, SOBJECT *shp, SHAPE *shape, FVEC pos, SVEC ang, FVEC scale
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SOBJECT));
	if (shp)
	{
		ShpInit(&shp->s, ST_OBJECT);
		FVecCpy(shp->pos, pos);
		FVecCpy(shp->scale, scale);
		SVecCpy(shp->ang, ang);
		shp->shape = shape;
		shp->m = NULL;
		shp->skel.index = 0;
		shp->skel.anime = NULL;
		shp->skel.frame = 0;
		shp->skel.vframe = 0;
		shp->skel.vspeed = 1 << 16;
		shp->skel.stamp = 0;
		shp->s.flag |= SHP_ANIME;
	}
	return shp;
}

SCULL *ShpCreateCull(ARENA *arena, SCULL *shp, SHORT dist)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SCULL));
	if (shp)
	{
		ShpInit(&shp->s, ST_CULL);
		shp->dist = dist;
	}
	return shp;
}

SJOINT *ShpCreateJoint(
	ARENA *arena, SJOINT *shp, int layer, Gfx *gfx, SVEC pos
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SJOINT));
	if (shp)
	{
		ShpInit(&shp->s.s, ST_JOINT);
		SVecCpy(shp->pos, pos);
		ShpSetLayer(&shp->s.s, layer);
		shp->s.gfx = gfx;
	}
	return shp;
}

SBILLBOARD *ShpCreateBillboard(
	ARENA *arena, SBILLBOARD *shp, int layer, Gfx *gfx, SVEC pos
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SBILLBOARD));
	if (shp)
	{
		ShpInit(&shp->s.s, ST_BILLBOARD);
		SVecCpy(shp->pos, pos);
		ShpSetLayer(&shp->s.s, layer);
		shp->s.gfx = gfx;
	}
	return shp;
}

SGFX *ShpCreateGfx(ARENA *arena, SGFX *shp, int layer, Gfx *gfx)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SGFX));
	if (shp)
	{
		ShpInit(&shp->s, ST_GFX);
		ShpSetLayer(&shp->s, layer);
		shp->gfx = gfx;
	}
	return shp;
}

SSHADOW *ShpCreateShadow(
	ARENA *arena, SSHADOW *shp, SHORT size, UCHAR alpha, UCHAR type
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SSHADOW));
	if (shp)
	{
		ShpInit(&shp->s, ST_SHADOW);
		shp->size = size;
		shp->alpha = alpha;
		shp->type = type;
	}
	return shp;
}

SBRANCH *ShpCreateBranch(ARENA *arena, SBRANCH *shp, SHAPE *shape)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SBRANCH));
	if (shp)
	{
		ShpInit(&shp->s, ST_BRANCH);
		shp->shape = shape;
	}
	return shp;
}

SCALLBACK *ShpCreateCallback(
	ARENA *arena, SCALLBACK *shp, SHPCALL *callback, unsigned long arg
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SCALLBACK));
	if (shp)
	{
		ShpInit(&shp->s, ST_CALLBACK);
		shp->callback = callback;
		shp->arg = arg;
		if (callback) callback(SC_INIT, &shp->s, arena);
	}
	return shp;
}

SBACK *ShpCreateBack(
	ARENA *arena, SBACK *shp, USHORT code, SHPCALL *callback, unsigned long arg
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SBACK));
	if (shp)
	{
		ShpInit(&shp->s.s, ST_BACK);
		shp->code = code << 16 | (u16)code;
		shp->s.callback = callback;
		shp->s.arg = arg;
		if (callback) callback(SC_INIT, &shp->s.s, arena);
	}
	return shp;
}

SHAND *ShpCreateHand(
	ARENA *arena, SHAND *shp, SOBJECT *obj, SVEC pos,
	SHPCALL *callback, unsigned long arg
)
{
	if (arena) shp = ArenaAlloc(arena, sizeof(SHAND));
	if (shp)
	{
		ShpInit(&shp->s.s, ST_HAND);
		SVecCpy(shp->pos, pos);
		shp->obj = obj;
		shp->s.callback = callback;
		shp->s.arg = arg;
		if (callback) callback(SC_INIT, &shp->s.s, arena);
	}
	return shp;
}

SHAPE *ShpLink(SHAPE *parent, SHAPE *shape)
{
	if (shape)
	{
		SHAPE *child;
		shape->parent = parent;
		if (!(child = parent->child))
		{
			parent->child = shape;
			shape->prev = shape;
			shape->next = shape;
		}
		else
		{
			SHAPE *prev = child->prev;
			shape->prev = prev;
			shape->next = child;
			child->prev = shape;
			prev->next = shape;
		}
	}
	return shape;
}

SHAPE *ShpUnlink(SHAPE *shape)
{
	SHAPE *parent = shape->parent;
	SHAPE **child = &parent->child;
	shape->prev->next = shape->next;
	shape->next->prev = shape->prev;
	if (*child == shape)
	{
		if (shape->next == shape)   *child = NULL;
		else                        *child = shape->next;
	}
	return parent;
}

SHAPE *ShpMakeFirst(SHAPE *shape)
{
	SHAPE *prev;
	SHAPE *parent = shape->parent;
	SHAPE **child = &parent->child;
	if (*child != shape)
	{
		if ((*child)->prev != shape)
		{
			shape->prev->next = shape->next;
			shape->next->prev = shape->prev;
			prev = (*child)->prev;
			shape->prev = prev;
			shape->next = *child;
			(*child)->prev = shape;
			prev->next = shape;
		}
		*child = shape;
	}
	return parent;
}

static void ShpNotify(SHAPE *shape, int code)
{
	SHAPE **sptr;
	SHAPE *shp = shape;
	do
	{
		SCALLBACK *cb = (SCALLBACK *)shp;
		if (shp->type & SF_CALLBACK)
		{
			if (cb->callback) cb->callback(code, shp, NULL);
		}
		if (shp->child)
		{
			switch (shp->type)
			{
			case ST_LAYER:  sptr = (SHAPE **)&draw_layer;   break;
			case ST_PERSP:  sptr = (SHAPE **)&draw_persp;   break;
			case ST_CAMERA: sptr = (SHAPE **)&draw_camera;  break;
			case ST_OBJECT: sptr = (SHAPE **)&draw_object;  break;
			default:        sptr = NULL;                    break;
			}
			if (sptr) *sptr = shp;
			ShpNotify(shp->child, code);
			if (sptr) *sptr = NULL;
		}
	}
	while ((shp = shp->next) != shape);
}

void SSceneNotify(SSCENE *shp, int code)
{
	if (shp->s.flag & SHP_ACTIVE)
	{
		draw_scene = shp;
		if (shp->s.child) ShpNotify(shp->s.child, code);
		draw_scene = 0;
	}
}

void SObjInit(SOBJECT *shp)
{
	ShpCreateObject(NULL, shp, NULL, fvec_0, svec_0, fvec_1);
	ShpLink(&sobj_list, &shp->s);
	shp->s.flag &= ~SHP_ACTIVE;
}

void SObjEnter(SOBJECT *shp, SHAPE *shape, FVEC pos, SVEC ang)
{
	FVecSet(shp->scale, 1, 1, 1);
	FVecCpy(shp->pos, pos);
	SVecCpy(shp->ang, ang);
	shp->shape = shape;
	shp->actor = NULL;
	shp->m = NULL;
	shp->skel.anime = NULL;
	shp->s.flag |= SHP_ACTIVE;
	shp->s.flag &= ~SHP_OBJHIDE;
	shp->s.flag |= SHP_ANIME;
	shp->s.flag &= ~SHP_BILLBOARD;
}

void SObjActor(SOBJECT *shp, ACTOR *actor)
{
	FVecSet(shp->scale, 1, 1, 1);
	SVecCpy(shp->ang, actor->ang);
	shp->pos[0] = actor->pos[0];
	shp->pos[1] = actor->pos[1];
	shp->pos[2] = actor->pos[2];
	shp->scene = actor->scene;
	shp->group = actor->group;
	shp->shape = actor->shape;
	shp->actor = actor;
	shp->m = NULL;
	shp->skel.anime = NULL;
	shp->s.flag |= SHP_ACTIVE;
	shp->s.flag &= ~SHP_OBJHIDE;
	shp->s.flag |= SHP_ANIME;
	shp->s.flag &= ~SHP_BILLBOARD;
}

void SObjSetAnime(SOBJECT *shp, ANIME **animep)
{
	ANIME **ap = SegmentToVirtual(animep);
	ANIME *anime = SegmentToVirtual(*ap);
	if (shp->skel.anime != anime)
	{
		shp->skel.anime = anime;
		shp->skel.frame =
			anime->start + ((anime->flag & ANIME_REVERSE) ? 1 : -1);
		shp->skel.vspeed = 0;
		shp->skel.waist = 0;
	}
}

void SObjSetAnimeV(SOBJECT *shp, ANIME **animep, int speed)
{
	ANIME **ap = SegmentToVirtual(animep);
	ANIME *anime = SegmentToVirtual(*ap);
	if (shp->skel.anime != anime)
	{
		shp->skel.anime = anime;
		shp->skel.waist = 0;
		shp->skel.vframe =
			(anime->start << 16) +
			((anime->flag & ANIME_REVERSE) ? speed : -speed);
		shp->skel.frame = shp->skel.vframe >> 16;
	}
	shp->skel.vspeed = speed;
}

int AnimeIndex(int frame, u16 **tbl)
{
	int index;
	if (frame < (*tbl)[0])  index = (*tbl)[1] + frame;
	else                    index = (*tbl)[1] + (*tbl)[0]-1;
	*tbl += 2;
	return index;
}

#ifdef sgi
#define GETFRAME()  (*(s16 *)&frame)
#define SETFRAME(x) (*(s16 *)&frame = (x))
#else
#define GETFRAME()  (frame >> 16)
#define SETFRAME(x) (frame = (frame & 0xFFFF) | (x) << 16)
#endif
int SkelStep(SKELETON *skel, s32 *vframe)
{
	s32 frame;
	ANIME *anime = skel->anime;
	if (skel->stamp == draw_timer || (anime->flag & ANIME_NOSTEP))
	{
		if (vframe) *vframe = skel->vframe;
		return skel->frame;
	}
	if (anime->flag & ANIME_REVERSE)
	{
		if (skel->vspeed)   frame = skel->vframe - skel->vspeed;
		else                frame = (skel->frame-1) << 16;
		if (GETFRAME() < anime->loop)
		{
			if (anime->flag & ANIME_NOLOOP) SETFRAME(anime->loop);
			else                            SETFRAME(anime->frame-1);
		}
	}
	else
	{
		if (skel->vspeed)   frame = skel->vframe + skel->vspeed;
		else                frame = (skel->frame+1) << 16;
		if (GETFRAME() >= anime->frame)
		{
			if (anime->flag & ANIME_NOLOOP) SETFRAME(anime->frame-1);
			else                            SETFRAME(anime->loop);
		}
	}
	if (vframe) *vframe = frame;
	return GETFRAME();
}
#undef GETFRAME
#undef SETFRAME

UNUSED static
void SObjGetAnimePos(SOBJECT *shp, FVEC pos)
{
	ANIME *anime = shp->skel.anime;
	if (anime)
	{
		u16 *tbl = SegmentToVirtual(anime->tbl);
		short *val = SegmentToVirtual(anime->val);
		SHORT frame = shp->skel.frame;
		if (frame < 0) frame = 0;
		pos[0] = val[AnimeIndex(frame, &tbl)];
		pos[1] = val[AnimeIndex(frame, &tbl)];
		pos[2] = val[AnimeIndex(frame, &tbl)];
	}
	else
	{
		FVecSet(pos, 0, 0, 0);
	}
}

UNUSED static
SSCENE *ShpGetScene(SHAPE *shape)
{
	SSCENE *shp = NULL;
	while (shape->parent) shape = shape->parent;
	if (shape->type == ST_SCENE) shp = (SSCENE *)shape;
	return shp;
}
