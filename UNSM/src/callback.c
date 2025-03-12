#include <sm64.h>

static SOBJECT mario_mirror;
PL_CTRL pl_ctrl_data[2];

void *CtrlWeather(int code, SHAPE *shape, UNUSED void *data)
{
	SVEC pos, eye, look;
	Gfx *g, *gfx = NULL;
	if (code == SC_DRAW && draw_camera)
	{
		SCALLBACK *shp = (SCALLBACK *)shape;
#ifdef sgi
		u16 *arg = (u16 *)&shp->arg;
		if (arg[0] != draw_timer)
#else
		if (shp->arg >> 16 != draw_timer)
#endif
		{
			UNUSED CAMERA *cam = (CAMERA *)draw_camera->s.arg;
#ifdef sgi
			int code = arg[1];
#else
			int code = shp->arg & 0xFFFF;
#endif
			FVecToSVec(look, draw_camera->look);
			FVecToSVec(eye, draw_camera->eye);
			FVecToSVec(pos, pl_camera_data[0].pos);
			if ((g = WeatherDraw(code, pos, look, eye)))
			{
				Mtx *mtx = GfxAlloc(sizeof(Mtx));
				gfx = GfxAlloc(sizeof(Gfx)*2);
				FMtxToMtx(mtx, data);
				gSPMatrix(
					&gfx[0], K0_TO_PHYS(mtx),
					G_MTX_MODELVIEW|G_MTX_LOAD|G_MTX_NOPUSH
				);
				gSPBranchList(&gfx[1], K0_TO_PHYS(g));
				ShpSetLayer(&shp->s, LAYER_TEX_EDGE);
			}
#ifdef sgi
			arg[0] = draw_timer;
#else
			shp->arg = (shp->arg & 0xFFFF) | draw_timer << 16;
#endif
		}
	}
	else if (code == SC_EXIT)
	{
		SVecCpy(look, svec_0);
		SVecCpy(eye, svec_0);
		SVecCpy(pos, svec_0);
		WeatherDraw(WEATHER_NULL, pos, look, eye);
	}
	return gfx;
}

void *CtrlBackground(int code, SHAPE *shape, UNUSED void *data)
{
	Gfx *gfx = NULL;
	SBACK *shp = (SBACK *)shape;
	if (code == SC_OPEN)
	{
		shp->s.arg = 0;
	}
	else if (code == SC_DRAW)
	{
		SCAMERA *cam = (SCAMERA *)draw_scene->reftab[0];
		SPERSP *persp = (SPERSP *)cam->s.s.parent;
		gfx = BackgroundDraw(
			0, shp->code, persp->fovy,
			camdata.eye[0], camdata.eye[1], camdata.eye[2],
			camdata.look[0], camdata.look[1], camdata.look[2]
		);
	}
	return gfx;
}

void *CtrlFace(int code, SHAPE *shape, void *data)
{
	Gfx *gfx = NULL;
#if REVISION == 199605
	(void)code;
	(void)shape;
	(void)data;
#else
	SHORT sound = 0;
	SCALLBACK *shp = (SCALLBACK *)shape;
	UNUSED FMTX *m = data;
	if (code == SC_DRAW)
	{
		if (cont1->pad && !wipe.active) face_gfx_8019C930(cont1->pad);
		gfx = (Gfx *)PHYS_TO_K0(gdm_gettestdl(shp->arg));
		gfx_callback = face_gfx_8019C874;
		sound = face_gfx_8019C9C8();
		AudPlayFaceSound(sound);
	}
#endif
	return gfx;
}

static void callback_8027657C(void)
{
	if (object->o_targetdist > 700) object->o_v6 = FALSE;
	if (!object->o_v6 && object->o_targetdist < 600) object->o_v7 = 2;
}

static void callback_802765FC(void)
{
	if (object->o_targetdist > 700)
	{
		object->o_v7 = 3;
	}
	else if (!object->o_v6)
	{
		object->o_hit_flag = HF_4000;
		if (object->o_hit_result & HR_008000)
		{
			object->o_hit_result = 0;
			object->o_v7 = 4;
			Na_ToadMessage();
		}
	}
}

static void callback_802766B4(void)
{
	if (objectlib_802A4BE4(3, 1, MSG_162, object->o_v5))
	{
		object->o_v6 = TRUE;
		object->o_v7 = 3;
		switch (object->o_v5)
		{
		case MSG_82: object->o_v5 = MSG_154; enemya_802AB558(0); break;
		case MSG_76: object->o_v5 = MSG_155; enemya_802AB558(1); break;
		case MSG_83: object->o_v5 = MSG_156; enemya_802AB558(2); break;
		}
	}
}

static void callback_802767B8(void)
{
	if ((object->o_alpha += 6) == 0xFF) object->o_v7 = 1;
}

static void callback_80276804(void)
{
	if ((object->o_alpha -= 6) == 0x51) object->o_v7 = 0;
}

void callback_8027684C(void)
{
	if (object->s.s.flag & SHP_ACTIVE)
	{
		object->o_hit_flag = 0;
		switch (object->o_v7)
		{
		case 0: callback_8027657C(); break;
		case 1: callback_802765FC(); break;
		case 2: callback_802767B8(); break;
		case 3: callback_80276804(); break;
		case 4: callback_802766B4(); break;
		}
	}
}

void callback_80276910(void)
{
	u32 flag = BuGetFlag();
	int total = BuStarTotal();
	int msg = ObjGetArg(object) & 0xFF;
	int has_msg = TRUE;
	switch (msg)
	{
	case MSG_82:
		has_msg = total >= 12;
		if (flag & ((1 << 0) << 24)) msg = MSG_154;
		break;
	case MSG_76:
		has_msg = total >= 25;
		if (flag & ((1 << 1) << 24)) msg = MSG_155;
		break;
	case MSG_83:
		has_msg = total >= 35;
		if (flag & ((1 << 2) << 24)) msg = MSG_156;
		break;
	}
	if (has_msg)
	{
		object->o_v5 = msg;
		object->o_v6 = FALSE;
		object->o_v7 = 0;
		object->o_alpha = 0x51;
	}
	else
	{
		ObjKill(object);
	}
}

extern OBJLANG obj_13002AF0[];

static void callback_80276AA0(SHORT angy)
{
	OBJECT *obj = ObjMakeHere(object, 0, obj_13002AF0);
	obj->o_posx += 100 * SIN(0x2800*object->o_v6 + angy);
	obj->o_posz += 100 * COS(0x2800*object->o_v6 + angy);
	obj->o_posy -= object->o_v6 * (float)10;
}

void callback_80276BB8(void)
{
	object->o_v5 = 0;
	object->o_v6 = 0;
	object->o_v7 = 0x1000;
	object->o_posx += 30 * SIN(mario->ang[1]-0x4000);
	object->o_posy += 160;
	object->o_posz += 30 * COS(mario->ang[1]-0x4000);
	object->o_angy = 0x7800;
	ObjSetScale(object, 0.5F);
}

void callback_80276CCC(void)
{
	UNUSED int i;
	short ang = object->o_angy;
	if (object->o_v7 < 0x2400) object->o_v7 += 0x60;
	switch (object->o_v5)
	{
	case 0:
		object->o_posy += 3.4F;
		object->o_angy += object->o_v7;
		ObjSetScale(object, 0.5F + (float)object->o_v6/50);
		if (++object->o_v6 == 30)
		{
			object->o_v6 = 0;
			object->o_v5++;
		}
		break;
	case 1:
		object->o_angy += object->o_v7;
		if (++object->o_v6 == 30)
		{
			Na_ObjSePlay(NA_SE7_1E, object);
			ObjectHide();
			object->o_v6 = 0;
			object->o_v5++;
		}
		break;
	case 2:
		callback_80276AA0(0);
		callback_80276AA0(-0x8000);
		if (object->o_v6++ == 20)
		{
			object->o_v6 = 0;
			object->o_v5++;
		}
		break;
	case 3:
		if (object->o_v6++ == 50)
		{
			ObjKill(object);
		}
		break;
	}
	if (ang > (short)object->o_angy) Na_ObjSePlay(NA_SE3_16, object);
}

static Gfx *callback_80276F90(SCALLBACK *shp, SHORT alpha)
{
	Gfx *g, *gfx = NULL;
	if (alpha == 0xFF)
	{
		ShpSetLayer(&shp->s, LAYER_OPA_SURF);
		g = gfx = GfxAlloc(sizeof(Gfx)*2);
	}
	else
	{
		ShpSetLayer(&shp->s, LAYER_XLU_SURF);
		g = gfx = GfxAlloc(sizeof(Gfx)*3);
		gDPSetAlphaCompare(g++, G_AC_DITHER);
	}
	gDPSetEnvColor(g++, 0xFF, 0xFF, 0xFF, alpha);
	gSPEndDisplayList(g);
	return gfx;
}

void *CtrlPlayerAlpha(int code, SHAPE *shape, UNUSED void *data)
{
	UNUSED int i;
	Gfx *gfx = NULL;
	SCALLBACK *shp = (SCALLBACK *)shape;
	PL_CTRL *ctrl = &pl_ctrl_data[shp->arg];
	if (code == SC_DRAW)
	{
		SHORT alpha = ctrl->cap & 0x100 ? ctrl->cap & 0xFF : 0xFF; /* T: */
		gfx = callback_80276F90(shp, alpha);
	}
	return gfx;
}

void *CtrlPlayerLOD(int code, SHAPE *shape, UNUSED void *data)
{
	SSELECT *shp = (SSELECT *)shape;
	PL_CTRL *ctrl = &pl_ctrl_data[shp->code];
	if (code == SC_DRAW)
	{
		shp->index = (ctrl->state & PF_WAIT) == 0;
	}
	return NULL;
}

void *CtrlPlayerEyes(int code, SHAPE *shape, UNUSED void *data)
{
	static char eyestab[] = {1, 2, 1, 0, 1, 2, 1, 0};
	SSELECT *shp = (SSELECT *)shape;
	PL_CTRL *ctrl = &pl_ctrl_data[shp->code];
	if (code == SC_DRAW)
	{
		if (ctrl->eyes == 0)
		{
			SHORT i = (32*shp->code + draw_timer) >> 1 & 31;
			if (i < 7)  shp->index = eyestab[i];
			else        shp->index = 0;
		}
		else
		{
			shp->index = ctrl->eyes - 1;
		}
	}
	return NULL;
}

void *CtrlPlayerTorso(int code, SHAPE *shape, UNUSED void *data)
{
	SCALLBACK *shp = (SCALLBACK *)shape;
	PL_CTRL *ctrl = &pl_ctrl_data[shp->arg];
	u32 state = ctrl->state;
	if (code == SC_DRAW)
	{
		SANG *torso = (SANG *)shape->next;
		if (!(
			state == PS_WALK_12 ||
			state == PS_WALK_14 ||
			state == PS_WALK_00 ||
			state == PS_WALK_06
		)) SVecCpy(ctrl->torso_ang, svec_0);
		torso->ang[0] = ctrl->torso_ang[1];
		torso->ang[1] = ctrl->torso_ang[2];
		torso->ang[2] = ctrl->torso_ang[0];
	}
	return NULL;
}

void *CtrlPlayerNeck(int code, SHAPE *shape, UNUSED void *data)
{
	SCALLBACK *shp = (SCALLBACK *)shape;
	PL_CTRL *ctrl = &pl_ctrl_data[shp->arg];
	u32 state = ctrl->state;
	if (code == SC_DRAW)
	{
		SANG *neck = (SANG *)shape->next;
		CAMERA *cam = (CAMERA *)draw_camera->s.arg;
		if (cam->mode == 6) /* T:enum */
		{
			neck->ang[0] = pl_camera_data[0].neck_angy;
			neck->ang[2] = pl_camera_data[0].neck_angx;
		}
		else if (state & PF_HEAD)
		{
			neck->ang[0] = ctrl->neck_ang[1];
			neck->ang[1] = ctrl->neck_ang[2];
			neck->ang[2] = ctrl->neck_ang[0];
		}
		else
		{
			SVecSet(ctrl->neck_ang, 0, 0, 0);
			SVecSet(neck->ang, 0, 0, 0);
		}
	}
	return NULL;
}

void *CtrlMarioHand(int code, SHAPE *shape, UNUSED void *data)
{
	SSELECT *shp = (SSELECT *)shape;
	PL_CTRL *ctrl = &pl_ctrl_data[0];
	if (code == SC_DRAW)
	{
		if (ctrl->hand == 0)
		{
			shp->index = (ctrl->state & PF_HAND) != 0;
		}
		else if (shp->code == 0)
		{
			shp->index = ctrl->hand < 5 ? ctrl->hand : 1;
		}
		else
		{
			shp->index = ctrl->hand < 2 ? ctrl->hand : 0;
		}
	}
	return NULL;
}

void *CtrlMarioPunch(int code, SHAPE *shape, UNUSED void *data)
{
	static char punchtab[][6] =
	{
		{10, 12, 16, 24, 10, 10},
		{10, 14, 20, 30, 10, 10},
		{10, 16, 20, 26, 26, 20},
	};
	static short stamp = 0;
	SCALLBACK *shp = (SCALLBACK *)shape;
	SSCALE *scale = (SSCALE *)shape->next;
	PL_CTRL *ctrl = &pl_ctrl_data[0];
	if (code == SC_DRAW)
	{
		scale->scale = 1;
		if (shp->arg == (ctrl->punch >> 6))
		{
			if (stamp != draw_timer && (ctrl->punch & 63) > 0)
			{
				ctrl->punch -= 1;
				stamp = draw_timer;
			}
			scale->scale = (float)punchtab[shp->arg][ctrl->punch & 63]/10;
		}
	}
	return NULL;
}

void *CtrlPlayerCap(int code, SHAPE *shape, UNUSED void *data)
{
	SSELECT *shp = (SSELECT *)shape;
	PL_CTRL *ctrl = &pl_ctrl_data[shp->code];
	if (code == SC_DRAW)
	{
		shp->index = ctrl->cap >> 8;
	}
	return NULL;
}

void *CtrlPlayerHead(int code, SHAPE *shape, UNUSED void *data)
{
	SHAPE *next = shape->next;
	SSELECT *shp = (SSELECT *)shape;
	PL_CTRL *ctrl = &pl_ctrl_data[shp->code];
	if (code == SC_DRAW)
	{
		shp->index = ctrl->head & 1; /* T:flag */
		while (next != shape)
		{
			if (next->type == ST_COORD)
			{
				if (ctrl->head & 2) next->flag |= SHP_ACTIVE; /* T:flag */
				else                next->flag &= ~SHP_ACTIVE;
			}
			next = next->next;
		}
	}
	return NULL;
}

void *CtrlPlayerWing(int code, SHAPE *shape, UNUSED void *data)
{
	SHORT x;
	SCALLBACK *shp = (SCALLBACK *)shape;
	if (code == SC_DRAW)
	{
		SANG *wing = (SANG *)shape->next;
		if (pl_ctrl_data[shp->arg >> 1].wing == 0)
		{
			x = 0x1000 * (1+COS(0x1000*(draw_timer & 15)));
		}
		else
		{
			x = 0x1800 * (1+COS(0x2000*(draw_timer & 7)));
		}
		if (!(shp->arg & 1))    wing->ang[0] = -x;
		else                    wing->ang[0] = +x;
	}
	return NULL;
}

void *CtrlPlayerHand(int code, SHAPE *shape, void *data)
{
	SHAND *shp = (SHAND *)shape;
	FMTX *m = data;
	PLAYER *pl = &player_data[shp->s.arg];
	if (code == SC_DRAW)
	{
		shp->obj = NULL;
		if (pl->take)
		{
			shp->obj = &pl->take->s;
			switch (pl->ctrl->take)
			{
			case 1:
				if (pl->state & PF_THRW)    SVecSet(shp->pos, 50, 0, 0);
				else                        SVecSet(shp->pos, 50, 0, 110);
				break;
			case 2:
				SVecSet(shp->pos, 145, -173, 180);
				break;
			case 3:
				SVecSet(shp->pos, 80, -270, 1260);
				break;
			}
		}
	}
	else if (code == SC_MTX)
	{
		CalcScenePos(pl->ctrl->hand_pos, *m, *draw_camera->m);
	}
	return NULL;
}

void *CtrlInsideMirror(int code, SHAPE *shape, UNUSED void *data)
{
	float x;
	SOBJECT *shp = &player_data[0].obj->s;
	switch (code)
	{
	case SC_INIT:
		ShpCreateObject(NULL, &mario_mirror, NULL, fvec_0, svec_0, fvec_1);
		break;
	case SC_OPEN:
		ShpLink(shape, &mario_mirror.s);
		break;
	case SC_CLOSE:
		ShpUnlink(&mario_mirror.s);
		break;
	case SC_DRAW:
		if (shp->pos[0] > 1700)
		{
			mario_mirror.shape = shp->shape;
			mario_mirror.scene = shp->scene;
			SVecCpy(mario_mirror.ang, shp->ang);
			FVecCpy(mario_mirror.pos, shp->pos);
			FVecCpy(mario_mirror.scale, shp->scale);
			mario_mirror.skel = shp->skel;
			x = 4331.53 - mario_mirror.pos[0];
			mario_mirror.pos[0] = 4331.53 + x;
			mario_mirror.ang[1] = -mario_mirror.ang[1];
			mario_mirror.scale[0] *= -1;
			((SHAPE *)(&mario_mirror.s))->flag |= SHP_ACTIVE;
		}
		else
		{
			((SHAPE *)(&mario_mirror.s))->flag &= ~SHP_ACTIVE;
		}
		break;
	}
	return NULL;
}

void *CtrlMarioMirror(int code, SHAPE *shape, UNUSED void *data)
{
	SCALLBACK *shp = (SCALLBACK *)shape;
	Gfx *gfx = NULL;
	if (code == SC_DRAW)
	{
		if (draw_object == &mario_mirror)
		{
			gfx = GfxAlloc(sizeof(Gfx)*3);
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
			ShpSetLayer(&shp->s, LAYER_OPA_SURF);
		}
	}
	return gfx;
}
