#include <sm64/types.h>
#include <sm64/app.h>
#include <sm64/mem.h>
#include <sm64/shadow.h>
#include <sm64/dprint.h>
#include <sm64/math.h>
#include <sm64/shape.h>
#include <sm64/s_script.h>

s16  draw_m;
mtxf draw_mtxf[32];
Mtx *draw_mtx[32];

u8   joint_prev_type;
u8   joint_prev_shadow;
s16  joint_prev_frame;
f32  joint_prev_scale;
u16 *joint_prev_tbl;
s16 *joint_prev_val;
u8   joint_type;
u8   joint_shadow;
s16  joint_frame;
f32  joint_scale;
u16 *joint_tbl;
s16 *joint_val;

ARENA *draw_arena;

u32 draw_rendermode_1[2][8] =
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

u32 draw_rendermode_2[2][8] =
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

SHAPE_SCENE  *shape_scene  = NULL;
SHAPE_LAYER  *shape_layer  = NULL;
SHAPE_PERSP  *shape_persp  = NULL;
SHAPE_CAMERA *shape_camera = NULL;
SHAPE_OBJECT *shape_object = NULL;
SHAPE_HAND   *shape_hand   = NULL;
u16 draw_timer = 0;

static void draw_shape(SHAPE *shape);

static void draw_layer_list(SHAPE_LAYER *layer)
{
    LAYER_LIST *list;
    int i;
    int zb = (layer->s.flag & S_FLAG_ZBUFFER) != 0;
    u32 *rm_1 = draw_rendermode_1[zb];
    u32 *rm_2 = draw_rendermode_2[zb];
    if (zb)
    {
        gDPPipeSync(video_gfx++);
        gSPSetGeometryMode(video_gfx++, G_ZBUFFER);
    }
    for (i = 0; i < S_LAYER_MAX; i++)
    {
        if ((list = layer->list[i]) != NULL)
        {
            gDPSetRenderMode(video_gfx++, rm_1[i], rm_2[i]);
            while (list != NULL)
            {
                gSPMatrix(
                    video_gfx++, K0_TO_PHYS(list->mtx),
                    G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH
                );
                gSPDisplayList(video_gfx++, list->gfx);
                list = list->next;
            }
        }
    }
    if (zb)
    {
        gDPPipeSync(video_gfx++);
        gSPClearGeometryMode(video_gfx++, G_ZBUFFER);
    }
}

static void draw_layer_gfx(const Gfx *gfx, SHORT layer)
{
    if (shape_layer != NULL)
    {
        LAYER_LIST *list = arena_alloc(draw_arena, sizeof(LAYER_LIST));
        list->mtx = draw_mtx[draw_m];
        list->gfx = gfx;
        list->next = NULL;
        if (shape_layer->list[layer] == NULL) shape_layer->list[layer] = list;
        else shape_layer->next[layer]->next = list;
        shape_layer->next[layer] = list;
    }
}

static void draw_layer(SHAPE_LAYER *layer)
{
    if (shape_layer == NULL)
    {
        if (layer->s.child != NULL)
        {
            int i;
            shape_layer = layer;
            for (i = 0; i < S_LAYER_MAX; i++) layer->list[i] = NULL;
            draw_shape(layer->s.child);
            draw_layer_list(layer);
            shape_layer = NULL;
        }
    }
}

static void draw_ortho(SHAPE_ORTHO *ortho)
{
    if (ortho->s.child != NULL)
    {
        Mtx *mtx = gfx_alloc(sizeof(Mtx));
        float l = (float)(shape_scene->x-shape_scene->w)/2 * ortho->scale;
        float r = (float)(shape_scene->x+shape_scene->w)/2 * ortho->scale;
        float t = (float)(shape_scene->y-shape_scene->h)/2 * ortho->scale;
        float b = (float)(shape_scene->y+shape_scene->h)/2 * ortho->scale;
        guOrtho(mtx, l, r, b, t, -2, +2, 1);
        gSPPerspNormalize(video_gfx++, 0xFFFF);
        gSPMatrix(
            video_gfx++, K0_TO_PHYS(mtx),
            G_MTX_PROJECTION | G_MTX_LOAD | G_MTX_NOPUSH
        );
        draw_shape(ortho->s.child);
    }
}

static void draw_persp(SHAPE_PERSP *persp)
{
    if (persp->s.callback != NULL) persp->s.callback(
        S_CODE_DRAW, &persp->s.s, draw_mtxf[draw_m]
    );
    if (persp->s.s.child != NULL)
    {
        u16 perspNorm;
        Mtx *mtx = gfx_alloc(sizeof(Mtx));
        float aspect = (float)shape_scene->w/shape_scene->h;
        guPerspective(
            mtx, &perspNorm, persp->fovy, aspect, persp->near, persp->far, 1
        );
        gSPPerspNormalize(video_gfx++, perspNorm);
        gSPMatrix(
            video_gfx++, K0_TO_PHYS(mtx),
            G_MTX_PROJECTION | G_MTX_LOAD | G_MTX_NOPUSH
        );
        shape_persp = persp;
        draw_shape(persp->s.s.child);
        shape_persp = NULL;
    }
}

static void draw_lod(SHAPE_LOD *lod)
{
    s16 *mtx = (s16 *)draw_mtx[draw_m];
    SHORT z = -mtx[4*3+2];
    if (lod->min <= z && z < lod->max)
    {
        if (lod->s.child != NULL) draw_shape(lod->s.child);
    }
}

static void draw_select(SHAPE_SELECT *select)
{
    SHAPE *shape = select->s.s.child;
    int i;
    if (select->s.callback != NULL) select->s.callback(
        S_CODE_DRAW, &select->s.s, draw_mtxf[draw_m]
    );
    for (i = 0; shape != NULL && i < select->index; i++) shape = shape->next;
    if (shape != NULL) draw_shape(shape);
}

static void draw_camera(SHAPE_CAMERA *camera)
{
    mtxf mf;
    Mtx *mrz = gfx_alloc(sizeof(Mtx));
    Mtx *mtx = gfx_alloc(sizeof(Mtx));
    if (camera->s.callback != NULL) camera->s.callback(
        S_CODE_DRAW, &camera->s.s, draw_mtxf[draw_m]
    );
    mtx_rz(mrz, camera->rz_p);
    gSPMatrix(
        video_gfx++, K0_TO_PHYS(mrz),
        G_MTX_PROJECTION | G_MTX_MUL | G_MTX_NOPUSH
    );
    mtxf_lookat(mf, camera->eye, camera->look, camera->rz_m);
    mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m]);
    draw_m++;
    mtx_mtxf(mtx, draw_mtxf[draw_m]);
    draw_mtx[draw_m] = mtx;
    if (camera->s.s.child != NULL)
    {
        shape_camera = camera;
        camera->mf = &draw_mtxf[draw_m];
        draw_shape(camera->s.s.child);
        shape_camera = NULL;
    }
    draw_m--;
}

static void draw_posrot(SHAPE_POSROT *posrot)
{
    mtxf mf;
    vecf vf;
    Mtx *mtx = gfx_alloc(sizeof(Mtx));
    vecf_vecs(vf, posrot->pos);
    mtxf_posrot(mf, vf, posrot->rot);
    mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m]);
    draw_m++;
    mtx_mtxf(mtx, draw_mtxf[draw_m]);
    draw_mtx[draw_m] = mtx;
    if (posrot->s.gfx != NULL) draw_layer_gfx(
        posrot->s.gfx, shape_layer_get(posrot)
    );
    if (posrot->s.s.child != NULL) draw_shape(posrot->s.s.child);
    draw_m--;
}

static void draw_pos(SHAPE_POS *pos)
{
    mtxf mf;
    vecf vf;
    Mtx *mtx = gfx_alloc(sizeof(Mtx));
    vecf_vecs(vf, pos->pos);
    mtxf_posrot(mf, vf, vecs_0);
    mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m]);
    draw_m++;
    mtx_mtxf(mtx, draw_mtxf[draw_m]);
    draw_mtx[draw_m] = mtx;
    if (pos->s.gfx != NULL) draw_layer_gfx(
        pos->s.gfx, shape_layer_get(pos)
    );
    if (pos->s.s.child != NULL) draw_shape(pos->s.s.child);
    draw_m--;
}

static void draw_rot(SHAPE_ROT *rot)
{
    mtxf mf;
    Mtx *mtx = gfx_alloc(sizeof(Mtx));
    mtxf_posrot(mf, vecf_0, rot->rot);
    mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m]);
    draw_m++;
    mtx_mtxf(mtx, draw_mtxf[draw_m]);
    draw_mtx[draw_m] = mtx;
    if (rot->s.gfx != NULL) draw_layer_gfx(
        rot->s.gfx, shape_layer_get(rot)
    );
    if (rot->s.s.child != NULL) draw_shape(rot->s.s.child);
    draw_m--;
}

static void draw_scale(SHAPE_SCALE *scale)
{
    unused mtxf mf;
    vecf vf;
    Mtx *mtx = gfx_alloc(sizeof(Mtx));
    vecf_set(vf, scale->scale, scale->scale, scale->scale);
    mtxf_scale(draw_mtxf[draw_m+1], draw_mtxf[draw_m], vf);
    draw_m++;
    mtx_mtxf(mtx, draw_mtxf[draw_m]);
    draw_mtx[draw_m] = mtx;
    if (scale->s.gfx != NULL) draw_layer_gfx(
        scale->s.gfx, shape_layer_get(scale)
    );
    if (scale->s.s.child != NULL) draw_shape(scale->s.s.child);
    draw_m--;
}

static void draw_billboard(SHAPE_BILLBOARD *billboard)
{
    vecf vf;
    Mtx *mtx = gfx_alloc(sizeof(Mtx));
    draw_m++;
    vecf_vecs(vf, billboard->pos);
    mtxf_billboard(
        draw_mtxf[draw_m], draw_mtxf[draw_m-1], vf, shape_camera->rz_m
    );
    if (shape_hand != NULL) mtxf_scale(
        draw_mtxf[draw_m], draw_mtxf[draw_m], shape_hand->object->scale
    );
    else if (shape_object != NULL) mtxf_scale(
        draw_mtxf[draw_m], draw_mtxf[draw_m], shape_object->scale
    );
    mtx_mtxf(mtx, draw_mtxf[draw_m]);
    draw_mtx[draw_m] = mtx;
    if (billboard->s.gfx != NULL) draw_layer_gfx(
        billboard->s.gfx, shape_layer_get(billboard)
    );
    if (billboard->s.s.child != NULL) draw_shape(billboard->s.s.child);
    draw_m--;
}

static void draw_gfx(SHAPE_GFX *gfx)
{
    if (gfx->gfx != NULL) draw_layer_gfx(gfx->gfx, shape_layer_get(gfx));
    if (gfx->s.child != NULL) draw_shape(gfx->s.child);
}

static void draw_callback(SHAPE_CALLBACK *callback)
{
    if (callback->callback != NULL)
    {
        Gfx *gfx = callback->callback(
            S_CODE_DRAW, &callback->s, draw_mtxf[draw_m]
        );
        if (gfx != NULL) draw_layer_gfx(
            (void *)K0_TO_PHYS(gfx), shape_layer_get(callback)
        );
    }
    if (callback->s.child != NULL) draw_shape(callback->s.child);
}

static void draw_background(SHAPE_BACKGROUND *background)
{
    Gfx *gfx = NULL;
    if (background->s.callback != NULL) gfx = background->s.callback(
        S_CODE_DRAW, &background->s.s, draw_mtxf[draw_m]
    );
    if (gfx != NULL)
    {
        draw_layer_gfx((void *)K0_TO_PHYS(gfx), shape_layer_get(background));
    }
    else
    {
        if (shape_layer != NULL)
        {
            Gfx *gfx;
            Gfx *g = gfx = gfx_alloc(sizeof(Gfx)*7);
            gDPPipeSync(g++);
            gDPSetCycleType(g++, G_CYC_FILL);
            gDPSetFillColor(g++, background->arg);
            gDPFillRectangle(
                g++, 0, BORDER_HT, SCREEN_WD-1, SCREEN_HT-BORDER_HT-1
            );
            gDPPipeSync(g++);
            gDPSetCycleType(g++, G_CYC_1CYCLE);
            gSPEndDisplayList(g++);
            draw_layer_gfx((void *)K0_TO_PHYS(gfx), S_LAYER_BACKGROUND);
        }
    }
    if (background->s.s.child != NULL) draw_shape(background->s.s.child);
}

#define JOINT()         (joint_val[shape_8037C7D8(joint_frame, &joint_tbl)])
#define JOINT_POS()     (JOINT() * joint_scale)

static void draw_joint(SHAPE_JOINT *joint)
{
    mtxf mf;
    vecs rot;
    vecf pos;
    Mtx *mtx = gfx_alloc(sizeof(Mtx));
    vecs_cpy(rot, vecs_0);
    vecf_set(pos, joint->pos[0], joint->pos[1], joint->pos[2]);
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
        rot[0] = JOINT();
        rot[1] = JOINT();
        rot[2] = JOINT();
    }
    mtxf_joint(mf, pos, rot);
    mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m]);
    draw_m++;
    mtx_mtxf(mtx, draw_mtxf[draw_m]);
    draw_mtx[draw_m] = mtx;
    if (joint->s.gfx != NULL) draw_layer_gfx(
        joint->s.gfx, shape_layer_get(joint)
    );
    if (joint->s.s.child != NULL) draw_shape(joint->s.s.child);
    draw_m--;
}

static void draw_skeleton(SKELETON *skeleton, int flag)
{
    ANIME *anime = skeleton->anime;
    if (flag) skeleton->frame = shape_8037C844(skeleton, &skeleton->frame_amt);
    skeleton->timer = draw_timer;
    if      (anime->flag & ANIME_Y    ) joint_type = 2;
    else if (anime->flag & ANIME_XZ   ) joint_type = 3;
    else if (anime->flag & ANIME_NOPOS) joint_type = 4;
    else                                joint_type = 1;
    joint_frame = skeleton->frame;
    joint_shadow = (anime->flag & ANIME_FIXSHADOW) == 0;
    joint_tbl = segment_to_virtual(anime->tbl);
    joint_val = segment_to_virtual(anime->val);
    if (anime->waist == 0)  joint_scale = 1;
    else                    joint_scale = (float)skeleton->waist/anime->waist;
}

static void draw_shadow(SHAPE_SHADOW *shadow)
{
    if (shape_camera != NULL && shape_object != NULL)
    {
        Gfx *gfx;
        mtxf mf;
        vecf pos;
        vecf joint;
        float scale;
        float size;
        if (shape_hand != NULL)
        {
            vecf_untransform(pos, draw_mtxf[draw_m], *shape_camera->mf);
            size = shadow->size;
        }
        else
        {
            vecf_cpy(pos, shape_object->pos);
            size = shadow->size * shape_object->scale[0];
        }
        scale = 1;
        if (joint_shadow && (joint_type == 1 || joint_type == 3))
        {
            float s;
            float c;
            SHAPE_SCALE *child = (SHAPE_SCALE *)shadow->s.child;
            if (child != NULL && child->s.s.type == S_TYPE_SCALE)
            {
                scale = child->scale;
            }
            joint[0] = JOINT_POS() * scale;
            joint[1] = 0; joint_tbl += 2;
            joint[2] = JOINT_POS() * scale;
            joint_tbl -= 2*3;
            s = sin(shape_object->rot[1]);
            c = cos(shape_object->rot[1]);
            pos[0] +=  joint[0]*c + joint[2]*s;
            pos[2] += -joint[0]*s + joint[2]*c;
        }
        if ((gfx = shadow_802CF34C(
            pos[0], pos[1], pos[2], size, shadow->alpha, shadow->type
        )) != NULL)
        {
            Mtx *mtx = gfx_alloc(sizeof(Mtx));
            draw_m++;
            mtxf_pos(mf, pos);
            mtxf_cat(draw_mtxf[draw_m], mf, *shape_camera->mf);
            mtx_mtxf(mtx, draw_mtxf[draw_m]);
            draw_mtx[draw_m] = mtx;
            if      (shadow_803612B4 == 1) draw_layer_gfx(
                (void *)K0_TO_PHYS(gfx), S_LAYER_TEX_EDGE
            );
            else if (shadow_803612B5 == 1) draw_layer_gfx(
                (void *)K0_TO_PHYS(gfx), S_LAYER_XLU_SURF
            );
            else                           draw_layer_gfx(
                (void *)K0_TO_PHYS(gfx), S_LAYER_XLU_DECAL
            );
            draw_m--;
        }
    }
    if (shadow->s.child != NULL) draw_shape(shadow->s.child);
}

static int draw_object_isvisible(SHAPE_OBJECT *object, mtxf mf)
{
    SHORT d;
    SHORT y;
    SHAPE_CULL *cull;
    float x;
    if (object->s.flag & S_FLAG_OBJHIDE) return FALSE;
    cull = (SHAPE_CULL *)object->shape;
    y = (shape_persp->fovy/2+1) * 0x8000/180 + 0.5F;
    x = -mf[3][2] * sin(y)/cos(y);
    if (cull != NULL && cull->s.type == S_TYPE_CULL) d = (float)cull->dist;
    else                                             d = 300;
    if (mf[3][2] >   -100+(float)d) return FALSE;
    if (mf[3][2] < -20000-(float)d) return FALSE;
    if (mf[3][0] >      x+(float)d) return FALSE;
    if (mf[3][0] <     -x-(float)d) return FALSE;
    return TRUE;
}

static void draw_object(SHAPE_OBJECT *object)
{
    mtxf mf;
    int flag = (object->s.flag & S_FLAG_ANIME) != 0;
    if (object->scene == shape_scene->index)
    {
        if (object->mf != NULL)
        {
            mtxf_cat(draw_mtxf[draw_m+1], *object->mf, draw_mtxf[draw_m]);
        }
        else if (object->s.flag & S_FLAG_BILLBOARD)
        {
            mtxf_billboard(
                draw_mtxf[draw_m+1], draw_mtxf[draw_m], object->pos,
                shape_camera->rz_m
            );
        }
        else
        {
            mtxf_posrot(mf, object->pos, object->rot);
            mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m]);
        }
        mtxf_scale(draw_mtxf[draw_m+1], draw_mtxf[draw_m+1], object->scale);
        object->mf = &draw_mtxf[++draw_m];
        object->view[0] = draw_mtxf[draw_m][3][0];
        object->view[1] = draw_mtxf[draw_m][3][1];
        object->view[2] = draw_mtxf[draw_m][3][2];
        if (object->skeleton.anime != NULL) draw_skeleton(
            &object->skeleton, flag
        );
        if (draw_object_isvisible(object, draw_mtxf[draw_m]))
        {
            Mtx *mtx = gfx_alloc(sizeof(Mtx));
            mtx_mtxf(mtx, draw_mtxf[draw_m]);
            draw_mtx[draw_m] = mtx;
            if (object->shape != NULL)
            {
                shape_object = object;
                object->shape->parent = &object->s;
                draw_shape(object->shape);
                object->shape->parent = NULL;
                shape_object = NULL;
            }
            if (object->s.child != NULL) draw_shape(object->s.child);
        }
        draw_m--;
        joint_type = 0;
        object->mf = NULL;
    }
}

static void draw_list(SHAPE_LIST *list)
{
    if (list->shape != NULL)
    {
        list->shape->parent = &list->s;
        draw_shape(list->shape);
        list->shape->parent = NULL;
    }
    if (list->s.child != NULL) draw_shape(list->s.child);
}

static void draw_hand(SHAPE_HAND *hand)
{
    mtxf mf;
    vecf pos;
    Mtx *mtx = gfx_alloc(sizeof(Mtx));
    if (hand->s.callback != NULL) hand->s.callback(
        S_CODE_DRAW, &hand->s.s, draw_mtxf[draw_m]
    );
    if (hand->object != NULL && hand->object->shape != NULL)
    {
        int flag = (hand->object->s.flag & S_FLAG_ANIME) != 0;
        pos[0] = (float)hand->pos[0]/4;
        pos[1] = (float)hand->pos[1]/4;
        pos[2] = (float)hand->pos[2]/4;
        mtxf_pos(mf, pos);
        mtxf_cpy(draw_mtxf[draw_m+1], *shape_object->mf);
        draw_mtxf[draw_m+1][3][0] = draw_mtxf[draw_m][3][0];
        draw_mtxf[draw_m+1][3][1] = draw_mtxf[draw_m][3][1];
        draw_mtxf[draw_m+1][3][2] = draw_mtxf[draw_m][3][2];
        mtxf_cat(draw_mtxf[draw_m+1], mf, draw_mtxf[draw_m+1]);
        mtxf_scale(
            draw_mtxf[draw_m+1], draw_mtxf[draw_m+1], hand->object->scale
        );
        if (hand->s.callback != NULL) hand->s.callback(
            S_CODE_MTX, &hand->s.s, draw_mtxf[draw_m+1]
        );
        draw_m++;
        mtx_mtxf(mtx, draw_mtxf[draw_m]);
        draw_mtx[draw_m] = mtx;
        joint_prev_type   = joint_type;
        joint_prev_shadow = joint_shadow;
        joint_prev_frame  = joint_frame;
        joint_prev_scale  = joint_scale;
        joint_prev_tbl    = joint_tbl;
        joint_prev_val    = joint_val;
        joint_type = 0;
        shape_hand = hand;
        if (hand->object->skeleton.anime != NULL) draw_skeleton(
            &hand->object->skeleton, flag
        );
        draw_shape(hand->object->shape);
        shape_hand = NULL;
        joint_type   = joint_prev_type;
        joint_shadow = joint_prev_shadow;
        joint_frame  = joint_prev_frame;
        joint_scale  = joint_prev_scale;
        joint_tbl    = joint_prev_tbl;
        joint_val    = joint_prev_val;
        draw_m--;
    }
    if (hand->s.s.child != NULL) draw_shape(hand->s.s.child);
}

static void draw_child(SHAPE *shape)
{
    if (shape->child != NULL) draw_shape(shape->child);
}

static void draw_shape(SHAPE *shape)
{
    SHORT flag = TRUE;
    SHAPE *s = shape;
    SHAPE *parent = s->parent;
    if (parent != NULL) flag = parent->type != S_TYPE_SELECT;
    do
    {
        if (s->flag & S_FLAG_ACTIVE)
        {
            if (s->flag & S_FLAG_HIDE)
            {
                draw_child(s);
            }
            else switch (s->type)
            {
                case S_TYPE_ORTHO:      draw_ortho((void *)s);      break;
                case S_TYPE_PERSP:      draw_persp((void *)s);      break;
                case S_TYPE_LAYER:      draw_layer((void *)s);      break;
                case S_TYPE_LOD:        draw_lod((void *)s);        break;
                case S_TYPE_SELECT:     draw_select((void *)s);     break;
                case S_TYPE_CAMERA:     draw_camera((void *)s);     break;
                case S_TYPE_POSROT:     draw_posrot((void *)s);     break;
                case S_TYPE_POS:        draw_pos((void *)s);        break;
                case S_TYPE_ROT:        draw_rot((void *)s);        break;
                case S_TYPE_OBJECT:     draw_object((void *)s);     break;
                case S_TYPE_JOINT:      draw_joint((void *)s);      break;
                case S_TYPE_BILLBOARD:  draw_billboard((void *)s);  break;
                case S_TYPE_GFX:        draw_gfx((void *)s);        break;
                case S_TYPE_SCALE:      draw_scale((void *)s);      break;
                case S_TYPE_SHADOW:     draw_shadow((void *)s);     break;
                case S_TYPE_LIST:       draw_list((void *)s);       break;
                case S_TYPE_CALLBACK:   draw_callback((void *)s);   break;
                case S_TYPE_BACKGROUND: draw_background((void *)s); break;
                case S_TYPE_HAND:       draw_hand((void *)s);       break;
                default:                draw_child(s);              break;
            }
        }
        else
        {
            if (s->type == S_TYPE_OBJECT) ((SHAPE_OBJECT *)s)->mf = NULL;
        }
    }
    while (flag && (s = s->next) != shape);
}

void draw_scene(SHAPE_SCENE *scene, Vp *viewport, Vp *scissor, u32 fill)
{
    if (scene->s.flag & S_FLAG_ACTIVE)
    {
        unused int i;
        Mtx *mtx;
        Vp *vp;
        vp = gfx_alloc(sizeof(Vp));
        draw_arena = arena_init(mem_available()-sizeof(ARENA), 0);
        mtx = gfx_alloc(sizeof(Mtx));
        draw_m = 0;
        joint_type = 0;
        vecs_set(vp->vp.vtrans, 4*scene->x, 4*scene->y, G_MAXZ/2);
        vecs_set(vp->vp.vscale, 4*scene->w, 4*scene->h, G_MAXZ/2);
        if (viewport != NULL)
        {
            video_clear(fill);
            video_vp_scissor(viewport);
            *vp = *viewport;
        }
        else if (scissor != NULL)
        {
            video_clear(fill);
            video_vp_scissor(scissor);
        }
        mtxf_identity(draw_mtxf[draw_m]);
        mtx_mtxf(mtx, draw_mtxf[draw_m]);
        draw_mtx[draw_m] = mtx;
        gSPViewport(video_gfx++, K0_TO_PHYS(vp));
        gSPMatrix(
            video_gfx++, K0_TO_PHYS(draw_mtx[draw_m]),
            G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH
        );
        shape_scene = scene;
        if (scene->s.child != NULL) draw_shape(scene->s.child);
        shape_scene = NULL;
        if (debug_mem) dprintf(
            180, 20+16, "MEM %d", draw_arena->size-draw_arena->used
        );
        mem_free(draw_arena);
    }
}