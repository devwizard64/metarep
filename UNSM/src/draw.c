#include <sm64.h>

#define JOINT_XYZ       1
#define JOINT_Y         2
#define JOINT_XZ        3
#define JOINT_NOPOS     4
#define JOINT_ANG       5

static s16 draw_m;
static FMTX draw_fmtx[32];
static Mtx *draw_mtx[32];

static u8 joint_save_type;
static u8 joint_save_shadow;
static s16 joint_save_frame;
static float joint_save_scale;
static u16 *joint_save_tbl;
static short *joint_save_val;
static u8 joint_type;
static u8 joint_shadow;
static s16 joint_frame;
static float joint_scale;
static u16 *joint_tbl;
static short *joint_val;

static ARENA *draw_arena;

static u32 draw_rendermode_1[2][8] =
{
	{
		G_RM_OPA_SURF,
		G_RM_AA_OPA_SURF,
		G_RM_AA_OPA_SURF,
		G_RM_AA_OPA_SURF,
		G_RM_AA_TEX_EDGE,
		G_RM_AA_XLU_SURF,
		G_RM_AA_XLU_SURF,
		G_RM_AA_XLU_SURF,
	},
	{
		G_RM_ZB_OPA_SURF,
		G_RM_AA_ZB_OPA_SURF,
		G_RM_AA_ZB_OPA_DECAL,
		G_RM_AA_ZB_OPA_INTER,
		G_RM_AA_ZB_TEX_EDGE,
		G_RM_AA_ZB_XLU_SURF,
		G_RM_AA_ZB_XLU_DECAL,
		G_RM_AA_ZB_XLU_INTER,
	},
};

static u32 draw_rendermode_2[2][8] =
{
	{
		G_RM_OPA_SURF2,
		G_RM_AA_OPA_SURF2,
		G_RM_AA_OPA_SURF2,
		G_RM_AA_OPA_SURF2,
		G_RM_AA_TEX_EDGE2,
		G_RM_AA_XLU_SURF2,
		G_RM_AA_XLU_SURF2,
		G_RM_AA_XLU_SURF2,
	},
	{
		G_RM_ZB_OPA_SURF2,
		G_RM_AA_ZB_OPA_SURF2,
		G_RM_AA_ZB_OPA_DECAL2,
		G_RM_AA_ZB_OPA_INTER2,
		G_RM_AA_ZB_TEX_EDGE2,
		G_RM_AA_ZB_XLU_SURF2,
		G_RM_AA_ZB_XLU_DECAL2,
		G_RM_AA_ZB_XLU_INTER2,
	},
};

SSCENE  *draw_scene  = NULL;
SLAYER  *draw_layer  = NULL;
SPERSP  *draw_persp  = NULL;
SCAMERA *draw_camera = NULL;
SOBJECT *draw_object = NULL;
SHAND   *draw_hand   = NULL;
u16 draw_timer = 0;

static void DrawShape(SHAPE *shape);

static void DrawLayerList(SLAYER *shp)
{
	LAYERLIST *list;
	int i;
	int zb = (shp->s.flag & SHP_ZBUFFER) != 0;
	u32 *rm_1 = draw_rendermode_1[zb];
	u32 *rm_2 = draw_rendermode_2[zb];
	if (zb)
	{
		gDPPipeSync(glistp++);
		gSPSetGeometryMode(glistp++, G_ZBUFFER);
	}
	for (i = 0; i < LAYER_MAX; i++)
	{
		if ((list = shp->list[i]))
		{
			gDPSetRenderMode(glistp++, rm_1[i], rm_2[i]);
			while (list)
			{
				gSPMatrix(
					glistp++, K0_TO_PHYS(list->mtx),
					G_MTX_MODELVIEW|G_MTX_LOAD|G_MTX_NOPUSH
				);
				gSPDisplayList(glistp++, list->gfx);
				list = list->next;
			}
		}
	}
	if (zb)
	{
		gDPPipeSync(glistp++);
		gSPClearGeometryMode(glistp++, G_ZBUFFER);
	}
}

static void DrawLayerGfx(Gfx *gfx, SHORT layer)
{
	if (draw_layer)
	{
		LAYERLIST *list = ArenaAlloc(draw_arena, sizeof(LAYERLIST));
		list->mtx = draw_mtx[draw_m];
		list->gfx = gfx;
		list->next = NULL;
		if (!draw_layer->list[layer]) draw_layer->list[layer] = list;
		else draw_layer->next[layer]->next = list;
		draw_layer->next[layer] = list;
	}
}

static void DrawLayer(SLAYER *shp)
{
	if (!draw_layer)
	{
		if (shp->s.child)
		{
			int i;
			draw_layer = shp;
			for (i = 0; i < LAYER_MAX; i++) shp->list[i] = NULL;
			DrawShape(shp->s.child);
			DrawLayerList(shp);
			draw_layer = NULL;
		}
	}
}

static void DrawOrtho(SORTHO *shp)
{
	if (shp->s.child)
	{
		Mtx *mtx = GfxAlloc(sizeof(Mtx));
		float l = (float)(draw_scene->x - draw_scene->w)/2 * shp->scale;
		float r = (float)(draw_scene->x + draw_scene->w)/2 * shp->scale;
		float t = (float)(draw_scene->y - draw_scene->h)/2 * shp->scale;
		float b = (float)(draw_scene->y + draw_scene->h)/2 * shp->scale;
		guOrtho(mtx, l, r, b, t, -2, +2, 1);
		gSPPerspNormalize(glistp++, 0xFFFF);
		gSPMatrix(
			glistp++, K0_TO_PHYS(mtx),
			G_MTX_PROJECTION|G_MTX_LOAD|G_MTX_NOPUSH
		);
		DrawShape(shp->s.child);
	}
}

static void DrawPersp(SPERSP *shp)
{
	if (shp->s.callback) shp->s.callback(SC_DRAW, &shp->s.s, draw_fmtx[draw_m]);
	if (shp->s.s.child)
	{
		u16 perspNorm;
		Mtx *mtx = GfxAlloc(sizeof(Mtx));
		float aspect = (float)draw_scene->w / draw_scene->h;
		guPerspective(
			mtx, &perspNorm, shp->fovy, aspect, shp->near, shp->far, 1
		);
		gSPPerspNormalize(glistp++, perspNorm);
		gSPMatrix(
			glistp++, K0_TO_PHYS(mtx), G_MTX_PROJECTION|G_MTX_LOAD|G_MTX_NOPUSH
		);
		draw_persp = shp;
		DrawShape(shp->s.s.child);
		draw_persp = NULL;
	}
}

static void DrawLOD(SLOD *shp)
{
	short *mtx = (short *)draw_mtx[draw_m];
	short z = -mtx[4*3+2];
	if (shp->min <= z && z < shp->max)
	{
		if (shp->s.child) DrawShape(shp->s.child);
	}
}

static void DrawSelect(SSELECT *shp)
{
	SHAPE *shape = shp->s.s.child;
	int i;
	if (shp->s.callback) shp->s.callback(SC_DRAW, &shp->s.s, draw_fmtx[draw_m]);
	for (i = 0; shape && i < shp->index; i++) shape = shape->next;
	if (shape) DrawShape(shape);
}

static void DrawCamera(SCAMERA *shp)
{
	FMTX m;
	Mtx *maz = GfxAlloc(sizeof(Mtx));
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	if (shp->s.callback) shp->s.callback(SC_DRAW, &shp->s.s, draw_fmtx[draw_m]);
	MtxAngZ(maz, shp->angz_p);
	gSPMatrix(
		glistp++, K0_TO_PHYS(maz), G_MTX_PROJECTION|G_MTX_MUL|G_MTX_NOPUSH
	);
	FMtxLookAt(m, shp->eye, shp->look, shp->angz_m);
	FMtxCatAffine(draw_fmtx[draw_m+1], m, draw_fmtx[draw_m]);
	draw_m++;
	FMtxToMtx(mtx, draw_fmtx[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.s.child)
	{
		draw_camera = shp;
		shp->m = &draw_fmtx[draw_m];
		DrawShape(shp->s.s.child);
		draw_camera = NULL;
	}
	draw_m--;
}

static void DrawCoord(SCOORD *shp)
{
	FMTX m;
	FVEC v;
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	SVecToFVec(v, shp->pos);
	FMtxCoord(m, v, shp->ang);
	FMtxCatAffine(draw_fmtx[draw_m+1], m, draw_fmtx[draw_m]);
	draw_m++;
	FMtxToMtx(mtx, draw_fmtx[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.gfx) DrawLayerGfx(shp->s.gfx, ShpGetLayer(&shp->s.s));
	if (shp->s.s.child) DrawShape(shp->s.s.child);
	draw_m--;
}

static void DrawPos(SPOS *shp)
{
	FMTX m;
	FVEC v;
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	SVecToFVec(v, shp->pos);
	FMtxCoord(m, v, svec_0);
	FMtxCatAffine(draw_fmtx[draw_m+1], m, draw_fmtx[draw_m]);
	draw_m++;
	FMtxToMtx(mtx, draw_fmtx[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.gfx) DrawLayerGfx(shp->s.gfx, ShpGetLayer(&shp->s.s));
	if (shp->s.s.child) DrawShape(shp->s.s.child);
	draw_m--;
}

static void DrawAng(SANG *shp)
{
	FMTX m;
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	FMtxCoord(m, fvec_0, shp->ang);
	FMtxCatAffine(draw_fmtx[draw_m+1], m, draw_fmtx[draw_m]);
	draw_m++;
	FMtxToMtx(mtx, draw_fmtx[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.gfx) DrawLayerGfx(shp->s.gfx, ShpGetLayer(&shp->s.s));
	if (shp->s.s.child) DrawShape(shp->s.s.child);
	draw_m--;
}

static void DrawScale(SSCALE *shp)
{
	UNUSED FMTX m;
	FVEC v;
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	FVecSet(v, shp->scale, shp->scale, shp->scale);
	FMtxScale(draw_fmtx[draw_m+1], draw_fmtx[draw_m], v);
	draw_m++;
	FMtxToMtx(mtx, draw_fmtx[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.gfx) DrawLayerGfx(shp->s.gfx, ShpGetLayer(&shp->s.s));
	if (shp->s.s.child) DrawShape(shp->s.s.child);
	draw_m--;
}

static void DrawBillboard(SBILLBOARD *shp)
{
	FVEC v;
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	draw_m++;
	SVecToFVec(v, shp->pos);
	FMtxBillboard(
		draw_fmtx[draw_m], draw_fmtx[draw_m-1], v, draw_camera->angz_m
	);
	if (draw_hand) FMtxScale(
		draw_fmtx[draw_m], draw_fmtx[draw_m], draw_hand->obj->scale
	);
	else if (draw_object) FMtxScale(
		draw_fmtx[draw_m], draw_fmtx[draw_m], draw_object->scale
	);
	FMtxToMtx(mtx, draw_fmtx[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.gfx) DrawLayerGfx(shp->s.gfx, ShpGetLayer(&shp->s.s));
	if (shp->s.s.child) DrawShape(shp->s.s.child);
	draw_m--;
}

static void DrawGfx(SGFX *shp)
{
	if (shp->gfx) DrawLayerGfx(shp->gfx, ShpGetLayer(&shp->s));
	if (shp->s.child) DrawShape(shp->s.child);
}

static void DrawCallback(SCALLBACK *shp)
{
	if (shp->callback)
	{
		Gfx *gfx = shp->callback(SC_DRAW, &shp->s, draw_fmtx[draw_m]);
		if (gfx) DrawLayerGfx(
			(Gfx *)K0_TO_PHYS(gfx), ShpGetLayer(&shp->s)
		);
	}
	if (shp->s.child) DrawShape(shp->s.child);
}

static void DrawBack(SBACK *shp)
{
	Gfx *gfx = NULL;
	if (shp->s.callback) gfx = shp->s.callback(
		SC_DRAW, &shp->s.s, draw_fmtx[draw_m]
	);
	if (gfx)
	{
		DrawLayerGfx((Gfx *)K0_TO_PHYS(gfx), ShpGetLayer(&shp->s.s));
	}
	else
	{
		if (draw_layer)
		{
			Gfx *gfx, *g = gfx = GfxAlloc(sizeof(Gfx)*7);
			gDPPipeSync(g++);
			gDPSetCycleType(g++, G_CYC_FILL);
			gDPSetFillColor(g++, shp->code);
			gDPFillRectangle(
				g++, 0, BORDER_HT, SCREEN_WD-1, SCREEN_HT-BORDER_HT-1
			);
			gDPPipeSync(g++);
			gDPSetCycleType(g++, G_CYC_1CYCLE);
			gSPEndDisplayList(g++);
			DrawLayerGfx((Gfx *)K0_TO_PHYS(gfx), LAYER_BACK);
		}
	}
	if (shp->s.s.child) DrawShape(shp->s.s.child);
}

#define JOINT()         (joint_val[AnimeIndex(joint_frame, &joint_tbl)])
#define JOINT_POS()     (JOINT() * joint_scale)

static void DrawJoint(SJOINT *shp)
{
	FMTX m;
	SVEC ang;
	FVEC pos;
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	SVecCpy(ang, svec_0);
	FVecSet(pos, shp->pos[0], shp->pos[1], shp->pos[2]);
	if (joint_type == JOINT_XYZ)
	{
		pos[0] += JOINT_POS();
		pos[1] += JOINT_POS();
		pos[2] += JOINT_POS();
		joint_type = JOINT_ANG;
	}
	else if (joint_type == JOINT_XZ)
	{
		pos[0] += JOINT_POS();
		joint_tbl += 2;
		pos[2] += JOINT_POS();
		joint_type = JOINT_ANG;
	}
	else if (joint_type == JOINT_Y)
	{
		joint_tbl += 2;
		pos[1] += JOINT_POS();
		joint_tbl += 2;
		joint_type = JOINT_ANG;
	}
	else if (joint_type == JOINT_NOPOS)
	{
		joint_tbl += 2*3;
		joint_type = JOINT_ANG;
	}
	if (joint_type == JOINT_ANG)
	{
		ang[0] = JOINT();
		ang[1] = JOINT();
		ang[2] = JOINT();
	}
	FMtxJoint(m, pos, ang);
	FMtxCatAffine(draw_fmtx[draw_m+1], m, draw_fmtx[draw_m]);
	draw_m++;
	FMtxToMtx(mtx, draw_fmtx[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.gfx) DrawLayerGfx(shp->s.gfx, ShpGetLayer(&shp->s.s));
	if (shp->s.s.child) DrawShape(shp->s.s.child);
	draw_m--;
}

static void DrawSkeleton(SKELETON *skel, int flag)
{
	ANIME *anime = skel->anime;
	if (flag) skel->frame = SkelStep(skel, &skel->vframe);
	skel->stamp = draw_timer;
	if      (anime->flag & ANIME_Y    ) joint_type = JOINT_Y;
	else if (anime->flag & ANIME_XZ   ) joint_type = JOINT_XZ;
	else if (anime->flag & ANIME_NOPOS) joint_type = JOINT_NOPOS;
	else                                joint_type = JOINT_XYZ;
	joint_frame = skel->frame;
	joint_shadow = (anime->flag & ANIME_FIXSHADOW) == 0;
	joint_tbl = SegmentToVirtual(anime->tbl);
	joint_val = SegmentToVirtual(anime->val);
	if (anime->waist == 0)  joint_scale = 1;
	else                    joint_scale = (float)skel->waist/anime->waist;
}

static void DrawShadow(SSHADOW *shp)
{
	if (draw_camera && draw_object)
	{
		Gfx *gfx;
		FMTX m;
		FVEC pos, joint;
		float scale, size;
		if (draw_hand)
		{
			CalcScenePos(pos, draw_fmtx[draw_m], *draw_camera->m);
			size = shp->size;
		}
		else
		{
			FVecCpy(pos, draw_object->pos);
			size = shp->size * draw_object->scale[0];
		}
		scale = 1;
		if (joint_shadow && (joint_type == 1 || joint_type == 3))
		{
			float s, c;
			SSCALE *child = (SSCALE *)shp->s.child;
			if (child && child->s.s.type == ST_SCALE)
			{
				scale = child->scale;
			}
			joint[0] = JOINT_POS() * scale;
			joint[1] = 0; joint_tbl += 2;
			joint[2] = JOINT_POS() * scale;
			joint_tbl -= 2*3;
			s = SIN(draw_object->ang[1]);
			c = COS(draw_object->ang[1]);
			pos[0] +=  joint[0]*c + joint[2]*s;
			pos[2] += -joint[0]*s + joint[2]*c;
		}
		if ((gfx = ShadowDraw(
			pos[0], pos[1], pos[2], size, shp->alpha, shp->type
		)))
		{
			Mtx *mtx = GfxAlloc(sizeof(Mtx));
			draw_m++;
			FMtxPos(m, pos);
			FMtxCatAffine(draw_fmtx[draw_m], m, *draw_camera->m);
			FMtxToMtx(mtx, draw_fmtx[draw_m]);
			draw_mtx[draw_m] = mtx;
			if      (ISTRUE(shadow_onwater)) DrawLayerGfx(
				(Gfx *)K0_TO_PHYS(gfx), LAYER_TEX_EDGE
			);
			else if (ISTRUE(shadow_ondecal)) DrawLayerGfx(
				(Gfx *)K0_TO_PHYS(gfx), LAYER_XLU_SURF
			);
			else                             DrawLayerGfx(
				(Gfx *)K0_TO_PHYS(gfx), LAYER_XLU_DECAL
			);
			draw_m--;
		}
	}
	if (shp->s.child) DrawShape(shp->s.child);
}

static int SObjIsVisible(SOBJECT *shp, FMTX m)
{
	SHORT dist, ang;
	SCULL *cull;
	float x;
	if (shp->s.flag & SHP_OBJHIDE) return FALSE;
	cull = (SCULL *)shp->shape;
	ang = (draw_persp->fovy/2+1) * 0x8000/180 + 0.5F;
	x = -m[3][2] * SIN(ang)/COS(ang);
	if (cull && cull->s.type == ST_CULL)    dist = (float)cull->dist;
	else                                    dist = 300;
	if (m[3][2] >   -100+(float)dist) return FALSE;
	if (m[3][2] < -20000-(float)dist) return FALSE;
	if (m[3][0] >      x+(float)dist) return FALSE;
	if (m[3][0] <     -x-(float)dist) return FALSE;
	return TRUE;
}

static void DrawObject(SOBJECT *shp)
{
	FMTX m;
	int flag = (shp->s.flag & SHP_ANIME) != 0;
	if (shp->scene == draw_scene->index)
	{
		if (shp->m)
		{
			FMtxCatAffine(draw_fmtx[draw_m+1], *shp->m, draw_fmtx[draw_m]);
		}
		else if (shp->s.flag & SHP_BILLBOARD)
		{
			FMtxBillboard(
				draw_fmtx[draw_m+1], draw_fmtx[draw_m], shp->pos,
				draw_camera->angz_m
			);
		}
		else
		{
			FMtxCoord(m, shp->pos, shp->ang);
			FMtxCatAffine(draw_fmtx[draw_m+1], m, draw_fmtx[draw_m]);
		}
		FMtxScale(draw_fmtx[draw_m+1], draw_fmtx[draw_m+1], shp->scale);
		shp->m = &draw_fmtx[++draw_m];
		shp->view[0] = draw_fmtx[draw_m][3][0];
		shp->view[1] = draw_fmtx[draw_m][3][1];
		shp->view[2] = draw_fmtx[draw_m][3][2];
		if (shp->skel.anime) DrawSkeleton(&shp->skel, flag);
		if (SObjIsVisible(shp, draw_fmtx[draw_m]))
		{
			Mtx *mtx = GfxAlloc(sizeof(Mtx));
			FMtxToMtx(mtx, draw_fmtx[draw_m]);
			draw_mtx[draw_m] = mtx;
			if (shp->shape)
			{
				draw_object = shp;
				shp->shape->parent = &shp->s;
				DrawShape(shp->shape);
				shp->shape->parent = NULL;
				draw_object = NULL;
			}
			if (shp->s.child) DrawShape(shp->s.child);
		}
		draw_m--;
		joint_type = 0;
		shp->m = NULL;
	}
}

static void DrawBranch(SBRANCH *shp)
{
	if (shp->shape)
	{
		shp->shape->parent = &shp->s;
		DrawShape(shp->shape);
		shp->shape->parent = NULL;
	}
	if (shp->s.child) DrawShape(shp->s.child);
}

static void DrawHand(SHAND *shp)
{
	FMTX m;
	FVEC pos;
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	if (shp->s.callback) shp->s.callback(SC_DRAW, &shp->s.s, draw_fmtx[draw_m]);
	if (shp->obj && shp->obj->shape)
	{
		int flag = (shp->obj->s.flag & SHP_ANIME) != 0;
		pos[0] = (float)shp->pos[0]/4;
		pos[1] = (float)shp->pos[1]/4;
		pos[2] = (float)shp->pos[2]/4;
		FMtxPos(m, pos);
		FMtxCpy(draw_fmtx[draw_m+1], *draw_object->m);
		draw_fmtx[draw_m+1][3][0] = draw_fmtx[draw_m][3][0];
		draw_fmtx[draw_m+1][3][1] = draw_fmtx[draw_m][3][1];
		draw_fmtx[draw_m+1][3][2] = draw_fmtx[draw_m][3][2];
		FMtxCatAffine(draw_fmtx[draw_m+1], m, draw_fmtx[draw_m+1]);
		FMtxScale(draw_fmtx[draw_m+1], draw_fmtx[draw_m+1], shp->obj->scale);
		if (shp->s.callback) shp->s.callback(
			SC_MTX, &shp->s.s, draw_fmtx[draw_m+1]
		);
		draw_m++;
		FMtxToMtx(mtx, draw_fmtx[draw_m]);
		draw_mtx[draw_m] = mtx;
		joint_save_type   = joint_type;
		joint_save_shadow = joint_shadow;
		joint_save_frame  = joint_frame;
		joint_save_scale  = joint_scale;
		joint_save_tbl    = joint_tbl;
		joint_save_val    = joint_val;
		joint_type = 0;
		draw_hand = shp;
		if (shp->obj->skel.anime) DrawSkeleton(&shp->obj->skel, flag);
		DrawShape(shp->obj->shape);
		draw_hand = NULL;
		joint_type   = joint_save_type;
		joint_shadow = joint_save_shadow;
		joint_frame  = joint_save_frame;
		joint_scale  = joint_save_scale;
		joint_tbl    = joint_save_tbl;
		joint_val    = joint_save_val;
		draw_m--;
	}
	if (shp->s.s.child) DrawShape(shp->s.s.child);
}

static void DrawChild(SHAPE *shape)
{
	if (shape->child) DrawShape(shape->child);
}

static void DrawShape(SHAPE *shape)
{
	short flag = TRUE;
	SHAPE *shp = shape;
	SHAPE *parent = shp->parent;
	if (parent) flag = parent->type != ST_SELECT;
	do
	{
		if (shp->flag & SHP_ACTIVE)
		{
			if (shp->flag & SHP_HIDE)
			{
				DrawChild(shp);
			}
			else switch (shp->type)
			{
			case ST_ORTHO:      DrawOrtho((SORTHO *)shp);           break;
			case ST_PERSP:      DrawPersp((SPERSP *)shp);           break;
			case ST_LAYER:      DrawLayer((SLAYER *)shp);           break;
			case ST_LOD:        DrawLOD((SLOD *)shp);               break;
			case ST_SELECT:     DrawSelect((SSELECT *)shp);         break;
			case ST_CAMERA:     DrawCamera((SCAMERA *)shp);         break;
			case ST_COORD:      DrawCoord((SCOORD *)shp);           break;
			case ST_POS:        DrawPos((SPOS *)shp);               break;
			case ST_ANG:        DrawAng((SANG *)shp);               break;
			case ST_OBJECT:     DrawObject((SOBJECT *)shp);         break;
			case ST_JOINT:      DrawJoint((SJOINT *)shp);           break;
			case ST_BILLBOARD:  DrawBillboard((SBILLBOARD *)shp);   break;
			case ST_GFX:        DrawGfx((SGFX *)shp);               break;
			case ST_SCALE:      DrawScale((SSCALE *)shp);           break;
			case ST_SHADOW:     DrawShadow((SSHADOW *)shp);         break;
			case ST_BRANCH:     DrawBranch((SBRANCH *)shp);         break;
			case ST_CALLBACK:   DrawCallback((SCALLBACK *)shp);     break;
			case ST_BACK:       DrawBack((SBACK *)shp);             break;
			case ST_HAND:       DrawHand((SHAND *)shp);             break;
			default:            DrawChild(shp);                     break;
			}
		}
		else
		{
			if (shp->type == ST_OBJECT) ((SOBJECT *)shp)->m = NULL;
		}
	}
	while (flag && (shp = shp->next) != shape);
}

void DrawScene(SSCENE *shp, Vp *viewport, Vp *scissor, u32 fill)
{
	if (shp->s.flag & SHP_ACTIVE)
	{
		UNUSED int i;
		Mtx *mtx;
		Vp *vp = GfxAlloc(sizeof(Vp));
		draw_arena = ArenaCreate(MemAvailable()-sizeof(ARENA), MEM_ALLOC_L);
		mtx = GfxAlloc(sizeof(Mtx));
		draw_m = 0;
		joint_type = 0;
		SVecSet(vp->vp.vtrans, 4*shp->x, 4*shp->y, G_MAXZ/2);
		SVecSet(vp->vp.vscale, 4*shp->w, 4*shp->h, G_MAXZ/2);
		if (viewport != NULL)
		{
			GfxClear(fill);
			GfxVpScissor(viewport);
			*vp = *viewport;
		}
		else if (scissor != NULL)
		{
			GfxClear(fill);
			GfxVpScissor(scissor);
		}
		FMtxIdent(draw_fmtx[draw_m]);
		FMtxToMtx(mtx, draw_fmtx[draw_m]);
		draw_mtx[draw_m] = mtx;
		gSPViewport(glistp++, K0_TO_PHYS(vp));
		gSPMatrix(
			glistp++, K0_TO_PHYS(draw_mtx[draw_m]),
			G_MTX_MODELVIEW|G_MTX_LOAD|G_MTX_NOPUSH
		);
		draw_scene = shp;
		if (shp->s.child) DrawShape(shp->s.child);
		draw_scene = NULL;
		if (debug_mem) dprintf(
			180, 20+16, "MEM %d", draw_arena->size-draw_arena->used
		);
		MemFree(draw_arena);
	}
}
