#include <sm64.h>

static s16 draw_m;
static MTXF draw_mtxf[32];
static Mtx *draw_mtx[32];

static u8 joint_prev_type;
static u8 joint_prev_shadow;
static s16 joint_prev_frame;
static float joint_prev_scale;
static u16 *joint_prev_tbl;
static short *joint_prev_val;
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

S_SCENE  *s_scene  = NULL;
S_LAYER  *s_layer  = NULL;
S_PERSP  *s_persp  = NULL;
S_CAMERA *s_camera = NULL;
S_OBJECT *s_object = NULL;
S_HAND   *s_hand   = NULL;
u16 draw_timer = 0;

static void draw_shape(SHAPE *shape);

static void draw_layer_list(S_LAYER *shp)
{
	LAYER_LIST *list;
	int i;
	int zb = (shp->s.flag & S_FLAG_ZBUFFER) != 0;
	u32 *rm_1 = draw_rendermode_1[zb];
	u32 *rm_2 = draw_rendermode_2[zb];
	if (zb)
	{
		gDPPipeSync(gfx_ptr++);
		gSPSetGeometryMode(gfx_ptr++, G_ZBUFFER);
	}
	for (i = 0; i < LAYER_MAX; i++)
	{
		if ((list = shp->list[i]))
		{
			gDPSetRenderMode(gfx_ptr++, rm_1[i], rm_2[i]);
			while (list)
			{
				gSPMatrix(
					gfx_ptr++, K0_TO_PHYS(list->mtx),
					G_MTX_MODELVIEW|G_MTX_LOAD|G_MTX_NOPUSH
				);
				gSPDisplayList(gfx_ptr++, list->gfx);
				list = list->next;
			}
		}
	}
	if (zb)
	{
		gDPPipeSync(gfx_ptr++);
		gSPClearGeometryMode(gfx_ptr++, G_ZBUFFER);
	}
}

static void draw_layer_gfx(Gfx *gfx, SHORT layer)
{
	if (s_layer)
	{
		LAYER_LIST *list = arena_alloc(draw_arena, sizeof(LAYER_LIST));
		list->mtx = draw_mtx[draw_m];
		list->gfx = gfx;
		list->next = NULL;
		if (!s_layer->list[layer]) s_layer->list[layer] = list;
		else s_layer->next[layer]->next = list;
		s_layer->next[layer] = list;
	}
}

static void draw_layer(S_LAYER *shp)
{
	if (!s_layer)
	{
		if (shp->s.child)
		{
			int i;
			s_layer = shp;
			for (i = 0; i < LAYER_MAX; i++) shp->list[i] = NULL;
			draw_shape(shp->s.child);
			draw_layer_list(shp);
			s_layer = NULL;
		}
	}
}

static void draw_ortho(S_ORTHO *shp)
{
	if (shp->s.child)
	{
		Mtx *mtx = gfx_alloc(sizeof(Mtx));
		float l = (float)(s_scene->x-s_scene->w)/2 * shp->scale;
		float r = (float)(s_scene->x+s_scene->w)/2 * shp->scale;
		float t = (float)(s_scene->y-s_scene->h)/2 * shp->scale;
		float b = (float)(s_scene->y+s_scene->h)/2 * shp->scale;
		guOrtho(mtx, l, r, b, t, -2, +2, 1);
		gSPPerspNormalize(gfx_ptr++, 0xFFFF);
		gSPMatrix(
			gfx_ptr++, K0_TO_PHYS(mtx),
			G_MTX_PROJECTION|G_MTX_LOAD|G_MTX_NOPUSH
		);
		draw_shape(shp->s.child);
	}
}

static void draw_persp(S_PERSP *shp)
{
	if (shp->s.callback) shp->s.callback(
		S_CODE_DRAW, &shp->s.s, draw_mtxf[draw_m]
	);
	if (shp->s.s.child)
	{
		u16 perspNorm;
		Mtx *mtx = gfx_alloc(sizeof(Mtx));
		float aspect = (float)s_scene->w/s_scene->h;
		guPerspective(
			mtx, &perspNorm, shp->fovy, aspect, shp->near, shp->far, 1
		);
		gSPPerspNormalize(gfx_ptr++, perspNorm);
		gSPMatrix(
			gfx_ptr++, K0_TO_PHYS(mtx),
			G_MTX_PROJECTION|G_MTX_LOAD|G_MTX_NOPUSH
		);
		s_persp = shp;
		draw_shape(shp->s.s.child);
		s_persp = NULL;
	}
}

static void draw_lod(S_LOD *shp)
{
	short *mtx = (short *)draw_mtx[draw_m];
	short z = -mtx[4*3+2];
	if (shp->min <= z && z < shp->max)
	{
		if (shp->s.child) draw_shape(shp->s.child);
	}
}

static void draw_select(S_SELECT *shp)
{
	SHAPE *shape = shp->s.s.child;
	int i;
	if (shp->s.callback) shp->s.callback(
		S_CODE_DRAW, &shp->s.s, draw_mtxf[draw_m]
	);
	for (i = 0; shape && i < shp->index; i++) shape = shape->next;
	if (shape) draw_shape(shape);
}

static void draw_camera(S_CAMERA *shp)
{
	MTXF mf;
	Mtx *maz = gfx_alloc(sizeof(Mtx));
	Mtx *mtx = gfx_alloc(sizeof(Mtx));
	if (shp->s.callback) shp->s.callback(
		S_CODE_DRAW, &shp->s.s, draw_mtxf[draw_m]
	);
	mtx_az(maz, shp->az_p);
	gSPMatrix(
		gfx_ptr++, K0_TO_PHYS(maz), G_MTX_PROJECTION|G_MTX_MUL|G_MTX_NOPUSH
	);
	mtxf_lookat(mf, shp->eye, shp->look, shp->az_m);
	mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m]);
	draw_m++;
	mtxf_to_mtx(mtx, draw_mtxf[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.s.child)
	{
		s_camera = shp;
		shp->mf = &draw_mtxf[draw_m];
		draw_shape(shp->s.s.child);
		s_camera = NULL;
	}
	draw_m--;
}

static void draw_coord(S_COORD *shp)
{
	MTXF mf;
	VECF vf;
	Mtx *mtx = gfx_alloc(sizeof(Mtx));
	vecs_to_vecf(vf, shp->pos);
	mtxf_coord(mf, vf, shp->ang);
	mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m]);
	draw_m++;
	mtxf_to_mtx(mtx, draw_mtxf[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.gfx) draw_layer_gfx(shp->s.gfx, shape_layer_get(&shp->s.s));
	if (shp->s.s.child) draw_shape(shp->s.s.child);
	draw_m--;
}

static void draw_pos(S_POS *shp)
{
	MTXF mf;
	VECF vf;
	Mtx *mtx = gfx_alloc(sizeof(Mtx));
	vecs_to_vecf(vf, shp->pos);
	mtxf_coord(mf, vf, vecs_0);
	mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m]);
	draw_m++;
	mtxf_to_mtx(mtx, draw_mtxf[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.gfx) draw_layer_gfx(shp->s.gfx, shape_layer_get(&shp->s.s));
	if (shp->s.s.child) draw_shape(shp->s.s.child);
	draw_m--;
}

static void draw_ang(S_ANG *shp)
{
	MTXF mf;
	Mtx *mtx = gfx_alloc(sizeof(Mtx));
	mtxf_coord(mf, vecf_0, shp->ang);
	mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m]);
	draw_m++;
	mtxf_to_mtx(mtx, draw_mtxf[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.gfx) draw_layer_gfx(shp->s.gfx, shape_layer_get(&shp->s.s));
	if (shp->s.s.child) draw_shape(shp->s.s.child);
	draw_m--;
}

static void draw_scale(S_SCALE *shp)
{
	UNUSED MTXF mf;
	VECF vf;
	Mtx *mtx = gfx_alloc(sizeof(Mtx));
	vecf_set(vf, shp->scale, shp->scale, shp->scale);
	mtxf_scale(draw_mtxf[draw_m+1], draw_mtxf[draw_m], vf);
	draw_m++;
	mtxf_to_mtx(mtx, draw_mtxf[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.gfx) draw_layer_gfx(shp->s.gfx, shape_layer_get(&shp->s.s));
	if (shp->s.s.child) draw_shape(shp->s.s.child);
	draw_m--;
}

static void draw_billboard(S_BILLBOARD *shp)
{
	VECF vf;
	Mtx *mtx = gfx_alloc(sizeof(Mtx));
	draw_m++;
	vecs_to_vecf(vf, shp->pos);
	mtxf_billboard(
		draw_mtxf[draw_m], draw_mtxf[draw_m-1], vf, s_camera->az_m
	);
	if (s_hand) mtxf_scale(
		draw_mtxf[draw_m], draw_mtxf[draw_m], s_hand->obj->scale
	);
	else if (s_object) mtxf_scale(
		draw_mtxf[draw_m], draw_mtxf[draw_m], s_object->scale
	);
	mtxf_to_mtx(mtx, draw_mtxf[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.gfx) draw_layer_gfx(shp->s.gfx, shape_layer_get(&shp->s.s));
	if (shp->s.s.child) draw_shape(shp->s.s.child);
	draw_m--;
}

static void draw_gfx(S_GFX *shp)
{
	if (shp->gfx) draw_layer_gfx(shp->gfx, shape_layer_get(&shp->s));
	if (shp->s.child) draw_shape(shp->s.child);
}

static void draw_callback(S_CALLBACK *shp)
{
	if (shp->callback)
	{
		Gfx *gfx = shp->callback(S_CODE_DRAW, &shp->s, draw_mtxf[draw_m]);
		if (gfx) draw_layer_gfx(
			(Gfx *)K0_TO_PHYS(gfx), shape_layer_get(&shp->s)
		);
	}
	if (shp->s.child) draw_shape(shp->s.child);
}

static void draw_back(S_BACK *shp)
{
	Gfx *gfx = NULL;
	if (shp->s.callback) gfx = shp->s.callback(
		S_CODE_DRAW, &shp->s.s, draw_mtxf[draw_m]
	);
	if (gfx)
	{
		draw_layer_gfx((Gfx *)K0_TO_PHYS(gfx), shape_layer_get(&shp->s.s));
	}
	else
	{
		if (s_layer)
		{
			Gfx *gfx;
			Gfx *g = gfx = gfx_alloc(sizeof(Gfx)*7);
			gDPPipeSync(g++);
			gDPSetCycleType(g++, G_CYC_FILL);
			gDPSetFillColor(g++, shp->code);
			gDPFillRectangle(
				g++, 0, BORDER_HT, SCREEN_WD-1, SCREEN_HT-BORDER_HT-1
			);
			gDPPipeSync(g++);
			gDPSetCycleType(g++, G_CYC_1CYCLE);
			gSPEndDisplayList(g++);
			draw_layer_gfx((Gfx *)K0_TO_PHYS(gfx), LAYER_BACK);
		}
	}
	if (shp->s.s.child) draw_shape(shp->s.s.child);
}

#define JOINT()         (joint_val[anime_index(joint_frame, &joint_tbl)])
#define JOINT_POS()     (JOINT() * joint_scale)

static void draw_joint(S_JOINT *shp)
{
	MTXF mf;
	VECS ang;
	VECF pos;
	Mtx *mtx = gfx_alloc(sizeof(Mtx));
	vecs_cpy(ang, vecs_0);
	vecf_set(pos, shp->pos[0], shp->pos[1], shp->pos[2]);
	if (joint_type == 1)
	{
		pos[0] += JOINT_POS();
		pos[1] += JOINT_POS();
		pos[2] += JOINT_POS();
		joint_type = 5;
	}
	else if (joint_type == 3)
	{
		pos[0] += JOINT_POS();
		joint_tbl += 2;
		pos[2] += JOINT_POS();
		joint_type = 5;
	}
	else if (joint_type == 2)
	{
		joint_tbl += 2;
		pos[1] += JOINT_POS();
		joint_tbl += 2;
		joint_type = 5;
	}
	else if (joint_type == 4)
	{
		joint_tbl += 2*3;
		joint_type = 5;
	}
	if (joint_type == 5)
	{
		ang[0] = JOINT();
		ang[1] = JOINT();
		ang[2] = JOINT();
	}
	mtxf_joint(mf, pos, ang);
	mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m]);
	draw_m++;
	mtxf_to_mtx(mtx, draw_mtxf[draw_m]);
	draw_mtx[draw_m] = mtx;
	if (shp->s.gfx) draw_layer_gfx(shp->s.gfx, shape_layer_get(&shp->s.s));
	if (shp->s.s.child) draw_shape(shp->s.s.child);
	draw_m--;
}

static void draw_skeleton(SKELETON *skel, int flag)
{
	ANIME *anime = skel->anime;
	if (flag) skel->frame = anime_step(skel, &skel->frame_amt);
	skel->timer = draw_timer;
	if      (anime->flag & ANIME_Y    ) joint_type = 2;
	else if (anime->flag & ANIME_XZ   ) joint_type = 3;
	else if (anime->flag & ANIME_NOPOS) joint_type = 4;
	else                                joint_type = 1;
	joint_frame = skel->frame;
	joint_shadow = (anime->flag & ANIME_FIXSHADOW) == 0;
	joint_tbl = segment_to_virtual(anime->tbl);
	joint_val = segment_to_virtual(anime->val);
	if (anime->waist == 0)  joint_scale = 1;
	else                    joint_scale = (float)skel->waist/anime->waist;
}

static void draw_shadow(S_SHADOW *shp)
{
	if (s_camera && s_object)
	{
		Gfx *gfx;
		MTXF mf;
		VECF pos;
		VECF joint;
		float scale;
		float size;
		if (s_hand)
		{
			vecf_untransform(pos, draw_mtxf[draw_m], *s_camera->mf);
			size = shp->size;
		}
		else
		{
			vecf_cpy(pos, s_object->pos);
			size = shp->size * s_object->scale[0];
		}
		scale = 1;
		if (joint_shadow && (joint_type == 1 || joint_type == 3))
		{
			float s, c;
			S_SCALE *child = (S_SCALE *)shp->s.child;
			if (child && child->s.s.type == S_TYPE_SCALE)
			{
				scale = child->scale;
			}
			joint[0] = JOINT_POS() * scale;
			joint[1] = 0; joint_tbl += 2;
			joint[2] = JOINT_POS() * scale;
			joint_tbl -= 2*3;
			s = sin(s_object->ang[1]);
			c = cos(s_object->ang[1]);
			pos[0] +=  joint[0]*c + joint[2]*s;
			pos[2] += -joint[0]*s + joint[2]*c;
		}
		if ((gfx = shadow_802CF34C(
			pos[0], pos[1], pos[2], size, shp->alpha, shp->type
		)))
		{
			Mtx *mtx = gfx_alloc(sizeof(Mtx));
			draw_m++;
			mtxf_pos(mf, pos);
			mtxf_cat(draw_mtxf[draw_m], mf, *s_camera->mf);
			mtxf_to_mtx(mtx, draw_mtxf[draw_m]);
			draw_mtx[draw_m] = mtx;
			if      (shadow_803612B4 == 1) draw_layer_gfx(
				(Gfx *)K0_TO_PHYS(gfx), LAYER_TEX_EDGE
			);
			else if (shadow_803612B5 == 1) draw_layer_gfx(
				(Gfx *)K0_TO_PHYS(gfx), LAYER_XLU_SURF
			);
			else                           draw_layer_gfx(
				(Gfx *)K0_TO_PHYS(gfx), LAYER_XLU_DECAL
			);
			draw_m--;
		}
	}
	if (shp->s.child) draw_shape(shp->s.child);
}

static int sobj_isvisible(S_OBJECT *shp, MTXF mf)
{
	SHORT dist;
	SHORT ang;
	S_CULL *cull;
	float x;
	if (shp->s.flag & S_FLAG_OBJHIDE) return FALSE;
	cull = (S_CULL *)shp->shape;
	ang = (s_persp->fovy/2+1) * 0x8000/180 + 0.5F;
	x = -mf[3][2] * sin(ang)/cos(ang);
	if (cull && cull->s.type == S_TYPE_CULL)    dist = (float)cull->dist;
	else                                        dist = 300;
	if (mf[3][2] >   -100+(float)dist) return FALSE;
	if (mf[3][2] < -20000-(float)dist) return FALSE;
	if (mf[3][0] >      x+(float)dist) return FALSE;
	if (mf[3][0] <     -x-(float)dist) return FALSE;
	return TRUE;
}

static void draw_object(S_OBJECT *shp)
{
	MTXF mf;
	int flag = (shp->s.flag & S_FLAG_ANIME) != 0;
	if (shp->scene == s_scene->index)
	{
		if (shp->mf)
		{
			mtxf_cat(draw_mtxf[draw_m+1], *shp->mf, draw_mtxf[draw_m]);
		}
		else if (shp->s.flag & S_FLAG_BILLBOARD)
		{
			mtxf_billboard(
				draw_mtxf[draw_m+1], draw_mtxf[draw_m], shp->pos,
				s_camera->az_m
			);
		}
		else
		{
			mtxf_coord(mf, shp->pos, shp->ang);
			mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m]);
		}
		mtxf_scale(draw_mtxf[draw_m+1], draw_mtxf[draw_m+1], shp->scale);
		shp->mf = &draw_mtxf[++draw_m];
		shp->view[0] = draw_mtxf[draw_m][3][0];
		shp->view[1] = draw_mtxf[draw_m][3][1];
		shp->view[2] = draw_mtxf[draw_m][3][2];
		if (shp->skeleton.anime) draw_skeleton(&shp->skeleton, flag);
		if (sobj_isvisible(shp, draw_mtxf[draw_m]))
		{
			Mtx *mtx = gfx_alloc(sizeof(Mtx));
			mtxf_to_mtx(mtx, draw_mtxf[draw_m]);
			draw_mtx[draw_m] = mtx;
			if (shp->shape)
			{
				s_object = shp;
				shp->shape->parent = &shp->s;
				draw_shape(shp->shape);
				shp->shape->parent = NULL;
				s_object = NULL;
			}
			if (shp->s.child) draw_shape(shp->s.child);
		}
		draw_m--;
		joint_type = 0;
		shp->mf = NULL;
	}
}

static void draw_list(S_LIST *shp)
{
	if (shp->shape)
	{
		shp->shape->parent = &shp->s;
		draw_shape(shp->shape);
		shp->shape->parent = NULL;
	}
	if (shp->s.child) draw_shape(shp->s.child);
}

static void draw_hand(S_HAND *shp)
{
	MTXF mf;
	VECF pos;
	Mtx *mtx = gfx_alloc(sizeof(Mtx));
	if (shp->s.callback) shp->s.callback(
		S_CODE_DRAW, &shp->s.s, draw_mtxf[draw_m]
	);
	if (shp->obj && shp->obj->shape)
	{
		int flag = (shp->obj->s.flag & S_FLAG_ANIME) != 0;
		pos[0] = (float)shp->pos[0]/4;
		pos[1] = (float)shp->pos[1]/4;
		pos[2] = (float)shp->pos[2]/4;
		mtxf_pos(mf, pos);
		mtxf_cpy(draw_mtxf[draw_m+1], *s_object->mf);
		draw_mtxf[draw_m+1][3][0] = draw_mtxf[draw_m][3][0];
		draw_mtxf[draw_m+1][3][1] = draw_mtxf[draw_m][3][1];
		draw_mtxf[draw_m+1][3][2] = draw_mtxf[draw_m][3][2];
		mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m+1]);
		mtxf_scale(draw_mtxf[draw_m+1], draw_mtxf[draw_m+1], shp->obj->scale);
		if (shp->s.callback) shp->s.callback(
			S_CODE_MTX, &shp->s.s, draw_mtxf[draw_m+1]
		);
		draw_m++;
		mtxf_to_mtx(mtx, draw_mtxf[draw_m]);
		draw_mtx[draw_m] = mtx;
		joint_prev_type   = joint_type;
		joint_prev_shadow = joint_shadow;
		joint_prev_frame  = joint_frame;
		joint_prev_scale  = joint_scale;
		joint_prev_tbl    = joint_tbl;
		joint_prev_val    = joint_val;
		joint_type = 0;
		s_hand = shp;
		if (shp->obj->skeleton.anime) draw_skeleton(&shp->obj->skeleton, flag);
		draw_shape(shp->obj->shape);
		s_hand = NULL;
		joint_type   = joint_prev_type;
		joint_shadow = joint_prev_shadow;
		joint_frame  = joint_prev_frame;
		joint_scale  = joint_prev_scale;
		joint_tbl    = joint_prev_tbl;
		joint_val    = joint_prev_val;
		draw_m--;
	}
	if (shp->s.s.child) draw_shape(shp->s.s.child);
}

static void draw_child(SHAPE *shape)
{
	if (shape->child) draw_shape(shape->child);
}

static void draw_shape(SHAPE *shape)
{
	short flag = TRUE;
	SHAPE *shp = shape;
	SHAPE *parent = shp->parent;
	if (parent) flag = parent->type != S_TYPE_SELECT;
	do
	{
		if (shp->flag & S_FLAG_ACTIVE)
		{
			if (shp->flag & S_FLAG_HIDE)
			{
				draw_child(shp);
			}
			else switch (shp->type)
			{
			case S_TYPE_ORTHO:      draw_ortho((S_ORTHO *)shp);         break;
			case S_TYPE_PERSP:      draw_persp((S_PERSP *)shp);         break;
			case S_TYPE_LAYER:      draw_layer((S_LAYER *)shp);         break;
			case S_TYPE_LOD:        draw_lod((S_LOD *)shp);             break;
			case S_TYPE_SELECT:     draw_select((S_SELECT *)shp);       break;
			case S_TYPE_CAMERA:     draw_camera((S_CAMERA *)shp);       break;
			case S_TYPE_COORD:      draw_coord((S_COORD *)shp);         break;
			case S_TYPE_POS:        draw_pos((S_POS *)shp);             break;
			case S_TYPE_ANG:        draw_ang((S_ANG *)shp);             break;
			case S_TYPE_OBJECT:     draw_object((S_OBJECT *)shp);       break;
			case S_TYPE_JOINT:      draw_joint((S_JOINT *)shp);         break;
			case S_TYPE_BILLBOARD:  draw_billboard((S_BILLBOARD *)shp); break;
			case S_TYPE_GFX:        draw_gfx((S_GFX *)shp);             break;
			case S_TYPE_SCALE:      draw_scale((S_SCALE *)shp);         break;
			case S_TYPE_SHADOW:     draw_shadow((S_SHADOW *)shp);       break;
			case S_TYPE_LIST:       draw_list((S_LIST *)shp);           break;
			case S_TYPE_CALLBACK:   draw_callback((S_CALLBACK *)shp);   break;
			case S_TYPE_BACK:       draw_back((S_BACK *)shp);           break;
			case S_TYPE_HAND:       draw_hand((S_HAND *)shp);           break;
			default:                draw_child(shp);                    break;
			}
		}
		else
		{
			if (shp->type == S_TYPE_OBJECT) ((S_OBJECT *)shp)->mf = NULL;
		}
	}
	while (flag && (shp = shp->next) != shape);
}

void draw_scene(S_SCENE *shp, Vp *viewport, Vp *scissor, u32 fill)
{
	if (shp->s.flag & S_FLAG_ACTIVE)
	{
		UNUSED int i;
		Mtx *mtx;
		Vp *vp;
		vp = gfx_alloc(sizeof(Vp));
		draw_arena = arena_init(mem_available()-sizeof(ARENA), MEM_ALLOC_L);
		mtx = gfx_alloc(sizeof(Mtx));
		draw_m = 0;
		joint_type = 0;
		vecs_set(vp->vp.vtrans, 4*shp->x, 4*shp->y, G_MAXZ/2);
		vecs_set(vp->vp.vscale, 4*shp->w, 4*shp->h, G_MAXZ/2);
		if (viewport != NULL)
		{
			gfx_clear(fill);
			gfx_vp_scissor(viewport);
			*vp = *viewport;
		}
		else if (scissor != NULL)
		{
			gfx_clear(fill);
			gfx_vp_scissor(scissor);
		}
		mtxf_identity(draw_mtxf[draw_m]);
		mtxf_to_mtx(mtx, draw_mtxf[draw_m]);
		draw_mtx[draw_m] = mtx;
		gSPViewport(gfx_ptr++, K0_TO_PHYS(vp));
		gSPMatrix(
			gfx_ptr++, K0_TO_PHYS(draw_mtx[draw_m]),
			G_MTX_MODELVIEW|G_MTX_LOAD|G_MTX_NOPUSH
		);
		s_scene = shp;
		if (shp->s.child) draw_shape(shp->s.child);
		s_scene = NULL;
		if (debug_mem) dprintf(
			180, 20+16, "MEM %d", draw_arena->size-draw_arena->used
		);
		mem_free(draw_arena);
	}
}
