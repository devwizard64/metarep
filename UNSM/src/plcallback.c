#include <sm64.h>

static S_OBJECT sobj_mirror;
PL_SHAPE pl_shape_data[2];

void *s_stage_weather(int code, SHAPE *shape, UNUSED void *data)
{
	VECS pos;
	VECS eye;
	VECS look;
	Gfx *g;
	Gfx *gfx = NULL;
	if (code == S_CODE_DRAW && s_camera)
	{
		S_CALLBACK *shp = (S_CALLBACK *)shape;
#ifdef sgi
		u16 *arg = (u16 *)&shp->arg;
		if (arg[0] != draw_timer)
#else
		if (shp->arg >> 16 != draw_timer)
#endif
		{
			UNUSED CAMERA *cam = (CAMERA *)s_camera->s.arg;
#ifdef sgi
			int code = arg[1];
#else
			int code = shp->arg & 0xFFFF;
#endif
			vecf_to_vecs(look, s_camera->look);
			vecf_to_vecs(eye, s_camera->eye);
			vecf_to_vecs(pos, pl_camera_data[0].pos);
			if ((g = snow_802DFBC8(code, pos, look, eye)))
			{
				Mtx *mtx = gfx_alloc(sizeof(Mtx));
				gfx = gfx_alloc(sizeof(Gfx)*2);
				mtxf_to_mtx(mtx, data);
				gSPMatrix(
					&gfx[0], K0_TO_PHYS(mtx),
					G_MTX_MODELVIEW|G_MTX_LOAD|G_MTX_NOPUSH
				);
				gSPBranchList(&gfx[1], K0_TO_PHYS(g));
				shape_layer_set(&shp->s, LAYER_TEX_EDGE);
			}
#ifdef sgi
			arg[0] = draw_timer;
#else
			shp->arg = (shp->arg & 0xFFFF) | draw_timer << 16;
#endif
		}
	}
	else if (code == S_CODE_EXIT)
	{
		vecs_cpy(look, vecs_0);
		vecs_cpy(eye, vecs_0);
		vecs_cpy(pos, vecs_0);
		snow_802DFBC8(0, pos, look, eye);
	}
	return gfx;
}

void *s_stage_back(int code, SHAPE *shape, UNUSED void *data)
{
	Gfx *gfx = NULL;
	S_BACK *shp = (S_BACK *)shape;
	if (code == S_CODE_OPEN)
	{
		shp->s.arg = 0;
	}
	else if (code == S_CODE_DRAW)
	{
		S_CAMERA *cam = (S_CAMERA *)s_scene->table[0];
		S_PERSP *persp = (S_PERSP *)cam->s.s.parent;
		gfx = back_802CFEF4(
			0, shp->code, persp->fovy,
			camdata.eye[0], camdata.eye[1], camdata.eye[2],
			camdata.look[0], camdata.look[1], camdata.look[2]
		);
	}
	return gfx;
}

void *s_face_main(int code, SHAPE *shape, void *data)
{
	Gfx *gfx = 0;
	SHORT sfx = 0;
	S_CALLBACK *shp = (S_CALLBACK *)shape;
	UNUSED MTXF *mf = data;
	if (code == S_CODE_DRAW)
	{
		if (cont1->pad && !wipe.active)
		{
			face_gfx_8019C930(cont1->pad);
		}
		gfx = (Gfx *)PHYS_TO_K0(gdm_gettestdl(shp->arg));
		gfx_callback = face_gfx_8019C874;
		sfx = face_gfx_8019C9C8();
		aud_face_sfx(sfx);
	}
	return gfx;
}

static void pl_callback_8027657C(void)
{
	if (object->o_pl_dist > 700) object->mem[O_V6].i = FALSE;
	if (!object->mem[O_V6].i && object->o_pl_dist < 600)
	{
		object->mem[O_V7].i = 2;
	}
}

static void pl_callback_802765FC(void)
{
	if (object->o_pl_dist > 700)
	{
		object->mem[O_V7].i = 3;
	}
	else if (!object->mem[O_V6].i)
	{
		object->o_col_arg = 0x4000;
		if (object->o_col_flag & 0x8000)
		{
			object->o_col_flag = 0;
			object->mem[O_V7].i = 4;
			Na_g_803221F4();
		}
	}
}

static void pl_callback_802766B4(void)
{
	if (objlib_802A4BE4(3, 1, 162, object->mem[O_V5].i))
	{
		object->mem[O_V6].i = TRUE;
		object->mem[O_V7].i = 3;
		switch (object->mem[O_V5].i)
		{
		case 82:
			object->mem[O_V5].i = 154;
			object_a_802AB558(0);
			break;
		case 76:
			object->mem[O_V5].i = 155;
			object_a_802AB558(1);
			break;
		case 83:
			object->mem[O_V5].i = 156;
			object_a_802AB558(2);
			break;
		}
	}
}

static void pl_callback_802767B8(void)
{
	if ((object->o_alpha += 6) == 0xFF) object->mem[O_V7].i = 1;
}

static void pl_callback_80276804(void)
{
	if ((object->o_alpha -= 6) == 0x51) object->mem[O_V7].i = 0;
}

void pl_callback_8027684C(void)
{
	if (object->list.s.s.flag & S_FLAG_ACTIVE)
	{
		object->o_col_arg = 0;
		switch (object->mem[O_V7].i)
		{
		case 0: pl_callback_8027657C(); break;
		case 1: pl_callback_802765FC(); break;
		case 2: pl_callback_802767B8(); break;
		case 3: pl_callback_80276804(); break;
		case 4: pl_callback_802766B4(); break;
		}
	}
}

void pl_callback_80276910(void)
{
	u32 flag = save_flag_get();
	int total = save_star_total();
	int msg = object->o_arg >> 24 & 0xFF;
	int has_msg = TRUE;
	switch (msg)
	{
	case 82:
		has_msg = total >= 12;
		if (flag & 0x01000000) msg = 154;
		break;
	case 76:
		has_msg = total >= 25;
		if (flag & 0x02000000) msg = 155;
		break;
	case 83:
		has_msg = total >= 35;
		if (flag & 0x04000000) msg = 156;
		break;
	}
	if (has_msg)
	{
		object->mem[O_V5].i = msg;
		object->mem[O_V6].i = FALSE;
		object->mem[O_V7].i = 0;
		object->o_alpha = 0x51;
	}
	else
	{
		objlib_802A0568(object);
	}
}

extern O_SCRIPT o_13002AF0[];

static void pl_callback_80276AA0(SHORT ay)
{
	OBJECT *obj = objlib_8029EDCC(object, 0, o_13002AF0);
	obj->o_pos_x += 100 * sin(0x2800*object->mem[O_V6].i + ay);
	obj->o_pos_z += 100 * cos(0x2800*object->mem[O_V6].i + ay);
	obj->o_pos_y -= object->mem[O_V6].i * (float)10;
}

void pl_callback_80276BB8(void)
{
	object->mem[O_V5].i = 0;
	object->mem[O_V6].i = 0;
	object->mem[O_V7].i = 0x1000;
	object->o_pos_x += 30 * sin(mario->ang[1]-0x4000);
	object->o_pos_y += 160;
	object->o_pos_z += 30 * cos(mario->ang[1]-0x4000);
	object->o_ang_y = 0x7800;
	objlib_8029F404(object, 0.5F);
}

void pl_callback_80276CCC(void)
{
	UNUSED int i;
	short ang = object->o_ang_y;
	if (object->mem[O_V7].i < 0x2400) object->mem[O_V7].i += 0x60;
	switch (object->mem[O_V5].i)
	{
	case 0:
		object->o_pos_y += 3.4F;
		object->o_ang_y += object->mem[O_V7].i;
		objlib_8029F404(object, 0.5F + (float)object->mem[O_V6].i/50);
		if (++object->mem[O_V6].i == 30)
		{
			object->mem[O_V6].i = 0;
			object->mem[O_V5].i++;
		}
		break;
	case 1:
		object->o_ang_y += object->mem[O_V7].i;
		if (++object->mem[O_V6].i == 30)
		{
			Na_SE_obj(NA_SE7_1E, object);
			objlib_8029F6BC();
			object->mem[O_V6].i = 0;
			object->mem[O_V5].i++;
		}
		break;
	case 2:
		pl_callback_80276AA0(0);
		pl_callback_80276AA0(-0x8000);
		if (object->mem[O_V6].i++ == 20)
		{
			object->mem[O_V6].i = 0;
			object->mem[O_V5].i++;
		}
		break;
	case 3:
		if (object->mem[O_V6].i++ == 50)
		{
			objlib_802A0568(object);
		}
		break;
	}
	if (ang > (short)object->o_ang_y) Na_SE_obj(0x30160091, object);
}

static Gfx *pl_callback_80276F90(S_CALLBACK *shp, SHORT alpha)
{
	Gfx *g;
	Gfx *gfx = NULL;
	if (alpha == 0xFF)
	{
		shape_layer_set(&shp->s, LAYER_OPA_SURF);
		g = gfx = gfx_alloc(sizeof(Gfx)*2);
	}
	else
	{
		shape_layer_set(&shp->s, LAYER_XLU_SURF);
		g = gfx = gfx_alloc(sizeof(Gfx)*3);
		gDPSetAlphaCompare(g++, G_AC_DITHER);
	}
	gDPSetEnvColor(g++, 0xFF, 0xFF, 0xFF, alpha);
	gSPEndDisplayList(g);
	return gfx;
}

void *s_player_alpha(int code, SHAPE *shape, UNUSED void *data)
{
	UNUSED int i;
	Gfx *gfx = NULL;
	S_CALLBACK *shp = (S_CALLBACK *)shape;
	PL_SHAPE *pls = &pl_shape_data[shp->arg];
	if (code == S_CODE_DRAW)
	{
		SHORT alpha = (pls->cap & 0x100) ? (pls->cap & 0xFF) : 0xFF;
		gfx = pl_callback_80276F90(shp, alpha);
	}
	return gfx;
}

void *s_player_select_lod(int code, SHAPE *shape, UNUSED void *data)
{
	S_SELECT *shp = (S_SELECT *)shape;
	PL_SHAPE *pls = &pl_shape_data[shp->code];
	if (code == S_CODE_DRAW)
	{
		shp->index = (pls->state & 0x200) == 0;
	}
	return NULL;
}

void *s_player_select_eyes(int code, SHAPE *shape, UNUSED void *data)
{
	static s8 table[] = {1, 2, 1, 0, 1, 2, 1, 0};
	S_SELECT *shp = (S_SELECT *)shape;
	PL_SHAPE *pls = &pl_shape_data[shp->code];
	if (code == S_CODE_DRAW)
	{
		if (pls->eyes == 0)
		{
			SHORT i = (32*shp->code + draw_timer) >> 1 & 31;
			if (i < 7)  shp->index = table[i];
			else        shp->index = 0;
		}
		else
		{
			shp->index = pls->eyes - 1;
		}
	}
	return NULL;
}

void *s_player_ang_torso(int code, SHAPE *shape, UNUSED void *data)
{
	S_CALLBACK *shp = (S_CALLBACK *)shape;
	PL_SHAPE *pls = &pl_shape_data[shp->arg];
	u32 state = pls->state;
	if (code == S_CODE_DRAW)
	{
		S_ANG *ang = (S_ANG *)shape->next;
		if (
			state != 0x00840452 &&
			state != 0x00840454 &&
			state != 0x04000440 &&
			state != 0x20810446
		) vecs_cpy(pls->torso, vecs_0);
		ang->ang[0] = pls->torso[1];
		ang->ang[1] = pls->torso[2];
		ang->ang[2] = pls->torso[0];
	}
	return NULL;
}

void *s_player_ang_neck(int code, SHAPE *shape, UNUSED void *data)
{
	S_CALLBACK *shp = (S_CALLBACK *)shape;
	PL_SHAPE *pls = &pl_shape_data[shp->arg];
	u32 state = pls->state;
	if (code == S_CODE_DRAW)
	{
		S_ANG *ang = (S_ANG *)shape->next;
		CAMERA *cam = (CAMERA *)s_camera->s.arg;
		if (cam->mode == 6)
		{
			ang->ang[0] = pl_camera_data[0].neck_y;
			ang->ang[2] = pl_camera_data[0].neck_x;
		}
		else if (state & 0x20000000)
		{
			ang->ang[0] = pls->neck[1];
			ang->ang[1] = pls->neck[2];
			ang->ang[2] = pls->neck[0];
		}
		else
		{
			vecs_set(pls->neck, 0, 0, 0);
			vecs_set(ang->ang, 0, 0, 0);
		}
	}
	return NULL;
}

void *s_mario_select_glove(int code, SHAPE *shape, UNUSED void *data)
{
	S_SELECT *shp = (S_SELECT *)shape;
	PL_SHAPE *pls = &pl_shape_data[0];
	if (code == S_CODE_DRAW)
	{
		if (pls->glove == 0)
		{
			shp->index = (pls->state & 0x10000000) != 0;
		}
		else if (shp->code == 0)
		{
			shp->index = pls->glove < 5 ? pls->glove : 1;
		}
		else
		{
			shp->index = pls->glove < 2 ? pls->glove : 0;
		}
	}
	return NULL;
}

void *s_mario_punch(int code, SHAPE *shape, UNUSED void *data)
{
	static s8 table[][6] =
	{
		{10, 12, 16, 24, 10, 10},
		{10, 14, 20, 30, 10, 10},
		{10, 16, 20, 26, 26, 20},
	};
	static s16 timer = 0;
	S_CALLBACK *shp = (S_CALLBACK *)shape;
	S_SCALE *scale = (S_SCALE *)shape->next;
	PL_SHAPE *pls = &pl_shape_data[0];
	if (code == S_CODE_DRAW)
	{
		scale->scale = 1;
		if (shp->arg == (pls->punch >> 6))
		{
			if (timer != draw_timer && (pls->punch & 0x3F) > 0)
			{
				pls->punch--;
				timer = draw_timer;
			}
			scale->scale = (float)table[shp->arg][pls->punch & 0x3F]/10;
		}
	}
	return NULL;
}

void *s_player_select_cap(int code, SHAPE *shape, UNUSED void *data)
{
	S_SELECT *shp = (S_SELECT *)shape;
	PL_SHAPE *pls = &pl_shape_data[shp->code];
	if (code == S_CODE_DRAW)
	{
		shp->index = pls->cap >> 8;
	}
	return NULL;
}

void *s_player_select_head(int code, SHAPE *shape, UNUSED void *data)
{
	SHAPE *next = shape->next;
	S_SELECT *shp = (S_SELECT *)shape;
	PL_SHAPE *pls = &pl_shape_data[shp->code];
	if (code == S_CODE_DRAW)
	{
		shp->index = pls->head & 1;
		while (next != shape)
		{
			if (next->type == S_TYPE_COORD)
			{
				if (pls->head & 2)  next->flag |= S_FLAG_ACTIVE;
				else                next->flag &= ~S_FLAG_ACTIVE;
			}
			next = next->next;
		}
	}
	return NULL;
}

void *s_player_ang_wing(int code, SHAPE *shape, UNUSED void *data)
{
	SHORT x;
	S_CALLBACK *shp = (S_CALLBACK *)shape;
	if (code == S_CODE_DRAW)
	{
		S_ANG *ang = (S_ANG *)shape->next;
		if (pl_shape_data[shp->arg >> 1].wing == 0)
		{
			x = 0x1000 * (1+cos(0x1000*(draw_timer & 15)));
		}
		else
		{
			x = 0x1800 * (1+cos(0x2000*(draw_timer & 7)));
		}
		if (!(shp->arg & 1))    ang->ang[0] = -x;
		else                    ang->ang[0] = +x;
	}
	return NULL;
}

void *s_player_hand(int code, SHAPE *shape, void *data)
{
	S_HAND *shp = (S_HAND *)shape;
	MTXF *mf = data;
	PLAYER *pl = &player_data[shp->s.arg];
	if (code == S_CODE_DRAW)
	{
		shp->obj = NULL;
		if (pl->obj_hold)
		{
			shp->obj = &pl->obj_hold->list.s;
			switch (pl->shape->hold)
			{
			case 1:
				if (pl->state & 0x80000000)
				{
					vecs_set(shp->pos, 50, 0, 0);
				}
				else
				{
					vecs_set(shp->pos, 50, 0, 110);
				}
				break;
			case 2:
				vecs_set(shp->pos, 145, -173, 180);
				break;
			case 3:
				vecs_set(shp->pos, 80, -270, 1260);
				break;
			}
		}
	}
	else if (code == S_CODE_MTX)
	{
		vecf_untransform(pl->shape->hand, *mf, *s_camera->mf);
	}
	return NULL;
}

void *s_inside_mirror(int code, SHAPE *shape, UNUSED void *data)
{
	float x;
	S_OBJECT *obj = &player_data[0].obj->list.s;
	switch (code)
	{
	case S_CODE_INIT:
		s_create_object(NULL, &sobj_mirror, NULL, vecf_0, vecs_0, vecf_1);
		break;
	case S_CODE_OPEN:
		shape_link(shape, &sobj_mirror.s);
		break;
	case S_CODE_CLOSE:
		shape_unlink(&sobj_mirror.s);
		break;
	case S_CODE_DRAW:
		if (obj->pos[0] > 1700)
		{
			sobj_mirror.shape = obj->shape;
			sobj_mirror.scene = obj->scene;
			vecs_cpy(sobj_mirror.ang, obj->ang);
			vecf_cpy(sobj_mirror.pos, obj->pos);
			vecf_cpy(sobj_mirror.scale, obj->scale);
			sobj_mirror.skeleton = obj->skeleton;
			x = (DOUBLE)4331.53 - sobj_mirror.pos[0];
			sobj_mirror.pos[0] = (DOUBLE)4331.53 + x;
			sobj_mirror.ang[1] = -sobj_mirror.ang[1];
			sobj_mirror.scale[0] *= -1;
			((SHAPE *)(&sobj_mirror.s))->flag |= S_FLAG_ACTIVE;
		}
		else
		{
			((SHAPE *)(&sobj_mirror.s))->flag &= ~S_FLAG_ACTIVE;
		}
		break;
	}
	return NULL;
}

void *s_player_mirror(int code, SHAPE *shape, UNUSED void *data)
{
	S_CALLBACK *shp = (S_CALLBACK *)shape;
	Gfx *gfx = NULL;
	if (code == S_CODE_DRAW)
	{
		if (s_object == &sobj_mirror)
		{
			gfx = gfx_alloc(sizeof(Gfx)*3);
			if (shp->arg == 0)
			{
				gSPClearGeometryMode(&gfx[0], G_CULL_BACK);
				gSPSetGeometryMode(&gfx[1], G_CULL_FRONT);
				gSPEndDisplayList(&gfx[2]);
			}
			else
			{
				gSPClearGeometryMode(&gfx[0], G_CULL_FRONT);
				gSPSetGeometryMode(&gfx[1], G_CULL_BACK);
				gSPEndDisplayList(&gfx[2]);
			}
			shape_layer_set(&shp->s, LAYER_OPA_SURF);
		}
	}
	return gfx;
}
