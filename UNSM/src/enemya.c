#include <sm64.h>

void enemya_802A958C(float, float, int);
void enemya_802ACE80(void);
void enemya_802AE334(void);
void enemya_802AE45C(int);
int enemya_802B14F4(float, float);
int enemya_802B3134(float *, float *, float, float);
void enemya_802B98D4(float *, float *);
void enemya_802C63E8(void);
int enemya_802C6538(int *);

static u32 enemya_80330020[] =
{
	BU_REDSW,
	BU_GREENSW,
	BU_BLUESW,
};

static short enemya_8033002C[] =
{
	0x179F,0x1620,0x14AC,0x1346,0x11EB,0x109E,0x0F5D,0x0E28,
	0x0D01,0x0BE6,0x0AD7,0x09D5,0x08DF,0x07F7,0x071A,0x064B,
	0x0588,0x04D1,0x0427,0x038A,0x02F9,0x0275,0x01FD,0x0192,
	0x0134,0x00E2,0x009D,0x0064,0x0038,0x0019,0x0004,0x0000,
};

static void enemya_802A5620(void)
{
	object->o_velx = object->o_vell *  COS(object->o_angy);
	object->o_velz = object->o_vell * -SIN(object->o_angy);
	object->o_posx += object->o_velx;
	object->o_posz += object->o_velz;
}

extern OBJLANG obj_13000000[];

void enemya_802A56BC(void)
{
	UNUSED int i;
	OBJECT *o = ObjectFindObj(obj_13000000);
	switch (object->o_mode)
	{
	case 0:
		ObjectHitON();
		if (object->o_hit_result & (HR_010000|HR_020000))
		{
			object->o_mode = 1;
		}
		if (o && o->o_mode != 0) object->o_mode = 1;
		break;
	case 1:
		if (object->o_timer == 0 && (short)object->o_angy >= 0)
		{
			ObjectPlaySound(NA_SE3_4E);
#ifdef MOTOR
			motor_8024C834(35, 30);
#endif
		}
		ObjectHitOFF();
		object->o_vell = -8;
		enemya_802A5620();
		if (object->o_timer > 15) object->o_mode++;
		break;
	case 2:
		if (object->o_timer > 30) object->o_mode++;
		break;
	case 3:
		if (object->o_timer == 0 && (short)object->o_angy >= 0)
		{
			ObjectPlaySound(NA_SE3_4F);
#ifdef MOTOR
			motor_8024C834(35, 30);
#endif
		}
		object->o_vell = 8;
		enemya_802A5620();
		if (object->o_timer > 15) object->o_mode++;
		break;
	case 4:
		object->o_hit_result = 0;
		object->o_mode = 0;
		break;
	}
}

void enemya_802A58DC(void)
{
	if (object->o_timer == 0)
	{
		object->o_vely = 20 + 20*RandF();
		object->o_velf = 20 + 20*RandF();
		object->o_angy = Rand();
	}
	ObjectProcMoveF();
}

static void enemya_802A597C(void)
{
	ObjectSetScale(3);
	object->o_velf = 20;
	objectlib_802A2320();
	if (object->o_hit_result & HR_008000)
	{
		object->o_mode = 1;
	}
	else if (
		object->o_timer > 100 || object->o_move & OM_0200 ||
		object->flag & OBJ_0008
	)
	{
		ObjKill(object);
		objectlib_802A37AC();
	}
}

extern OBJLANG obj_130000F8[];

static void enemya_802A5A44(void)
{
	int i;
	ObjKill(object);
	for (i = 0; i < 10; i++) ObjMakeHere(object, S_BUBBLE_B, obj_130000F8);
}

static OBJCALL *enemya_8033006C[] =
{
	enemya_802A597C,
	enemya_802A5A44,
};

void enemya_802A5AA0(void)
{
	ObjectCallMode(enemya_8033006C);
}

extern OBJLANG obj_130000AC[];

static void enemya_802A5ACC(void)
{
	OBJECT *o;
	float scale = object->s.scale[1];
	o = ObjMakeHere(object, S_BUBBLE_B, obj_130000AC);
	o->o_posy += 50*scale;
	o->o_posx += SIN(object->o_angy) * 90*scale;
	o->o_posz += COS(object->o_angy) * 90*scale;
	ObjectPlaySound(NA_SE5_01);
}

void enemya_802A5BD4(void)
{
	ObjCopyCoord(object, object->parent);
	if (!(object->flag & OBJ_0008))
	{
		ObjCopyScale(object, object->parent);
		ObjSetRel(object, 0, 0, 100*object->s.scale[1]);
		ObjCalcMtx(object, O_REL, O_ANG);
		ObjAddTransform(object, O_POS, O_REL);
		object->o_shapeangx = object->o_angx;
		object->o_shapeoff = 100*object->s.scale[1];
	}
	if (object->parent->o_v7 != 1)
	{
		object->o_shape = -1;
	}
	else
	{
		object->o_shape++;
		if (object->o_shape == 15) object->parent->o_v7 = 0;
	}
	if (!object->parent->flag) ObjKill(object);
}

static void enemya_802A5D4C(void)
{
	short angy, rot;
	float s, t;
	UNUSED int i, n;
	float scale, scaling;
	if (object->o_code != 0)    scaling = 2;
	else                        scaling = 1;
	if (object->o_v3 < 0)   rot = +0x1000;
	else                    rot = -0x1000;
	t = (float)(1+object->o_timer) / 96;
	if (object->o_timer < 64)
	{
		angy = object->o_angy;
		object->o_angy += rot * COS(0x4000*t);
		if (angy < 0 && object->o_angy >= 0) ObjectPlaySound(NA_SE9_6B);
		object->o_angx = -0x4000 * (1.0-COS(0x4000*t));
		ObjectShake(4);
	}
	else if (object->o_timer < 96)
	{
		if (object->o_timer == 64) ObjectPlaySound(NA_SE5_14);
		s = (float)(1+object->o_timer-64) / 32;
		object->o_angy += rot * COS(0x4000*t);
		object->o_angx = -0x4000 * (1.0-COS(0x4000*t));
		ObjectShake((int)(4*(1-s)));
		scale = 0.6 + 0.4*COS(0x4000*s);
		ObjectSetScale(scale*scaling);
	}
	else if (object->o_timer < 104)
	{
	}
	else if (object->o_timer < 168)
	{
		if (object->o_timer == 104)
		{
			ObjectHitOFF();
			objectlib_802A37AC();
			object->o_f6 = 0.6*scaling;
			if (object->o_code != 0)
			{
				object->o_posy += 100;
				enemyb_802F2B88(1370, 2000, -320);
				ObjKill(object);
			}
			else
			{
				objectlib_802A5524();
			}
		}
		object->o_f6 -= 0.2*scaling;
		if (object->o_f6 < 0) object->o_f6 = 0;
		ObjectSetScale(object->o_f6);
	}
	else
	{
		ObjKill(object);
	}
}

static void enemya_802A6518(void)
{
	SHORT angy = object->o_angy;
	short dang;
	if (object->o_timer == 0)
	{
		if (object->o_code != 0)    object->o_v0 = 200;
		else                        object->o_v0 = 120;
		object->o_v2 = 0;
		object->o_v3 = 0;
		object->o_v4 = 0;
	}
	ObjectTurnTo(object, mario_obj, O_ANGY, 0x800);
	ObjectTurnTo(object, mario_obj, O_ANGX, 0x400);
	dang = angy - (SHORT)object->o_angy;
	if (dang == 0)
	{
		object->o_v2 = 0;
		object->o_v3 = 0;
	}
	else if (dang > 0)
	{
		if (object->o_v3 > 0)   object->o_v2 += dang;
		else                    object->o_v2 = 0;
		object->o_v3 = 1;
	}
	else
	{
		if (object->o_v3 < 0)   object->o_v2 -= dang;
		else                    object->o_v2 = 0;
		object->o_v3 = -1;
	}
	if (object->o_v2 == 0) object->o_v0 = 120;
	if (object->o_v2 > 0x10000) object->o_mode = 3;
	object->o_v0--;
	if (object->o_v0 == 0)
	{
		object->o_v0 = 120;
		object->o_v2 = 0;
	}
	if (object->o_v2 < 5000)
	{
		if (object->o_v4 == object->o_v5) object->o_v7 = 1;
		if (object->o_v4 == object->o_v5+20)
		{
			enemya_802A5ACC();
			object->o_v4 = 0;
			object->o_v5 = 50 + 50*RandF();
		}
		object->o_v4++;
	}
	else
	{
		object->o_v4 = 0;
		object->o_v5 = 50 + 50*RandF();
	}
	if (object->o_targetdist > 800) object->o_mode = 1;
}

static void enemya_802A68A0(void)
{
	SHORT target = ObjCalcAngY(object, mario_obj);
	SHORT target_dang = DeltaAng(object->o_angy, target);
	SHORT player_dang = DeltaAng(object->o_angy, mario_obj->o_shapeangy);
	if (!object->o_timer)
	{
		ObjectHitON();
		object->o_angx = 0;
		object->o_v4 = 30;
		object->o_v5 = 20*RandF();
		if (object->o_v5 & 1)   object->o_roty = -0x100;
		else                    object->o_roty = +0x100;
	}
	if (target_dang < 0x400 && player_dang > 0x4000)
	{
		if (object->o_targetdist < 700) object->o_mode = 2;
		else object->o_v4++;
	}
	else
	{
		object->o_angy += object->o_roty;
		object->o_v4 = 30;
	}
	if (object->o_v4 == object->o_v5+60) object->o_v7 = 1;
	if (object->o_v4 > object->o_v5+80)
	{
		object->o_v4 = 0;
		object->o_v5 = 80*RandF();
		enemya_802A5ACC();
	}
}

static void enemya_802A6AD8(void)
{
#if REVISION >= 199609
	ObjSetAng(object, 0, 0, 0);
#else
	object->o_angx = 0;
	object->o_angy = 0;
	object->o_angz = 0;
#endif
	ObjectSetScale(1+object->o_code);
	if (object->o_timer == 0) ObjectSavePos();
	if (object->o_targetdist < 1500) object->o_mode = 1;
}

static OBJCALL *enemya_80330074[] =
{
	enemya_802A6AD8,
	enemya_802A68A0,
	enemya_802A6518,
	enemya_802A5D4C,
};

HITINFO enemya_80330084 =
{
	/*type   */	HIT_DAMAGE,
	/*offset */	0,
	/*ap     */	2,
	/*hp     */	2,
	/*ncoin  */	5,
	/*hit r,h*/	80, 150,
	/*dmg r,h*/	0, 0,
};

void enemya_802A6B7C(void)
{
	ObjSetHitInfo(object, &enemya_80330084);
	ObjectCallMode(enemya_80330074);
	if (object->o_mode != 3)
	{
		if (object->o_targetdist > 3000 || object->flag & OBJ_0008)
		{
			object->o_mode = 0;
		}
	}
	object->o_hit_result = 0;
}

void enemya_802A6C20(void)
{
	int code = object->o_actorinfo >> 16 & 0xFF;
	object->hit_h = 10*code;
}

extern OBJLANG obj_13002EA8[];

void enemya_802A6C74(void)
{
	if (object->o_timer == 0)
	{
		OBJECT *o = ObjMakeHere(object, 85, obj_13002EA8); /* T:shape */
		o->o_posy += object->hit_h + 50;
	}
	enemya_802C63E8();
}

void enemya_802A6CF4(void)
{
	if (object_80361256 & 1)
	{
		if (object->o_timer == 0) waterp[1+6*2+5] = 3000;
		ObjectHide();
	}
	else
	{
		ObjectMapLoad();
	}
}

static PARTICLE enemya_80330094 =
{
	/*arg    */	0,
	/*count  */	30,
	/*shape  */	S_DROPLET,
	/*offset */	0,
	/*velf   */	40, 0,
	/*vely   */	20, 40,
	/*gravity*/	-4,
	/*drag   */	30,
	/*scale  */	20, 0,
};

void enemya_802A6D64(void)
{
	if (!(object_80361256 & 1))
	{
		if (object->o_mode == 0)
		{
			if (
				object->o_targetdist < 500 &&
				player_data[0].state == PS_WAIT_3C
			)
			{
				object->o_mode++;
				ObjectMakeParticle(&enemya_80330094);
				enemya_802AE0CC(20, S_SHARD, 0.3F, 3);
				ObjectPlaySound(NA_SE3_00);
				ObjectHide();
			}
		}
		else
		{
			if (object->o_timer < 50)
			{
				waterp[1+6*2+5]--;
				ObjectLevelSound(NA_SE4_16);
			}
			else
			{
				object_80361256 |= 1;
				Na_Solution();
				object->o_mode++;
			}
		}
	}
	else
	{
		if (object->o_timer == 0) waterp[1+6*2+5] = 700;
		ObjectHide();
	}
}

UNUSED static u8 enemya_803300A8[] = {MSG_10, MSG_11, MSG_12};

extern OBJLANG obj_130001AC[];

static void enemya_802A6EE4(void)
{
	object->o_shape = object->o_code;
	ObjectSetScale(0.5F);
	object->o_posy += 71;
	ObjMakeOffScale(0, 0, -71, 0, 0.5F, object, 86, obj_130001AC); /* T:shape */
	if (stage_index != STAGE_32)
	{
		if (BuGetFlag() & enemya_80330020[object->o_code])
		{
			object->o_mode = 3;
			object->s.scale[1] = 0.1F;
		}
		else
		{
			object->o_mode = 1;
		}
	}
	else
	{
		object->o_mode = 1;
	}
}

static void enemya_802A7020(void)
{
	if (ObjectIsMarioBG())
	{
		BuSetFlag(enemya_80330020[object->o_code]);
		object->o_mode = 2;
		ObjectPlaySound(NA_SE3_00);
	}
}

static void enemya_802A708C(void)
{
	if (object->o_timer < 5)
	{
		ObjectScaleTime(2, 4, 0.5F, 0.1F);
		if (object->o_timer == 4)
		{
			objectlib_802A50FC(1);
			objectlib_802A37AC();
			enemya_802AE0CC(60, S_STAR, 0.3F, object->o_code);
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
		}
	}
	else
	{
		int result = objectlib_802A4BE4(1, 12, 161, 0);
		if (result) object->o_mode = 3;
	}
}

static void enemya_802A7160(void)
{
}

static OBJCALL *enemya_803300AC[] =
{
	enemya_802A6EE4,
	enemya_802A7020,
	enemya_802A708C,
	enemya_802A7160,
};

void enemya_802A7170(void)
{
	ObjectCallMode(enemya_803300AC);
}

void *Ctrl_enemya_802A719C(int code, UNUSED SHAPE *shape, void *data)
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

void enemya_802A7230(void)
{
	enemya_802A958C(50, 50, 0x40);
}

static void enemya_802A7264(void)
{
#if REVISION >= 199609
	object->o_velf = 0;
	object->o_vely = 0;
#endif
	if (object->o_phase == 0)
	{
		ObjectHitOFF();
		camera_8032DF30 = object;
		ObjectSetAnime(5);
		ObjectSavePos();
		object->o_hp = 3;
		if (objectlib_802A48BC(500, 100))
		{
			object->o_phase++;
			Na_SeqMute(0, 60, 40);
		}
	}
	else
	{
		if (objectlib_802A4BE4(2, 1, 162, MSG_17))
		{
			object->o_mode = 2;
			object->o_flag |= OF_0400;
		}
	}
}

static int enemya_802A7384(float a0)
{
	if (object->o_posy-mario_obj->o_posy > a0)  return TRUE;
	else                                        return FALSE;
}

static void enemya_802A73D8(void)
{
	ObjectHitON();
	if (object->o_posy-object->o_savey < -100)
	{
		object->o_mode = 5;
		ObjectHitOFF();
	}
	if (object->o_v3 == 0)
	{
		if (ObjectIsAnimeFrame(15)) objectlib_802A50FC(1);
		if (objectlib_802A5288(4)) object->o_v3++;
	}
	else
	{
		if (object->o_v3 == 1)
		{
			ObjectSetAnimeFrame(11, 7);
			object->o_v3 = 2;
		}
		else
		{
			ObjectSetAnime(11);
		}
		if (object->o_v5 == 0)
		{
			object->o_velf = 3;
			ObjectTurn(object->o_targetang, 0x100);
		}
		else
		{
			object->o_velf = 0;
			object->o_v5--;
		}
	}
	if (objectlib_802A52F8()) object->o_mode = 3;
	if (enemya_802A7384(1200))
	{
		object->o_mode = 0;
		Na_BgmStop(NA_BGM_BATTLE);
	}
}

static void enemya_802A7598(void)
{
	if (object->o_phase == 0)
	{
		object->o_velf = 0;
		object->o_v4 = 0;
		object->o_v2 = 0;
		if (object->o_timer == 0) ObjectPlaySound(NA_SE5_1D);
		if (objectlib_802A5288(0))
		{
			object->o_phase++;
			ObjectSetAnimeFrame(1, 0);
		}
	}
	else if (object->o_phase == 1)
	{
		ObjectSetAnime(1);
		object->o_v2 += objectlib_802A5358();
		DbPrintErr("%d", object->o_v2);
		if (object->o_v2 > 10)
		{
			object->o_var = 3;
			object->o_mode = 2;
			object->o_v5 = 35;
			object->o_hit_result &= ~HR_000800;
		}
		else
		{
			object->o_velf = 3;
			if (object->o_v4 > 20 && ObjectTurn(0, 0x400))
			{
				object->o_phase++;
				ObjectSetAnimeFrame(9, 22);
			}
		}
		object->o_v4++;
	}
	else
	{
		ObjectSetAnime(9);
		if (ObjectIsAnimeFrame(31))
		{
			object->o_var = 2;
			ObjectPlaySound(NA_SE5_1E);
		}
		else
		{
			if (objectlib_8029FF04())
			{
				object->o_mode = 1;
				object->o_hit_result &= ~HR_000800;
			}
		}
	}
}

static void enemya_802A7804(void)
{
	object->o_velf = 0;
	object->o_vely = 0;
	ObjectSetAnime(11);
	object->o_angy = ApproachAng(object->o_angy, object->o_targetang, 0x200);
	if (object->o_targetdist < 2500) object->o_mode = 2;
	if (enemya_802A7384(1200))
	{
		object->o_mode = 0;
		Na_BgmStop(NA_BGM_BATTLE);
	}
}

static void enemya_802A78D8(void)
{
	if (object->o_phase == 0)
	{
		if (object->o_timer == 0)
		{
			object->o_v4 = 0;
			ObjectPlaySound(NA_SE5_16_80);
			ObjectPlaySound(NA_SE9_42);
			objectlib_802A50FC(1);
			enemya_802AAE8C(0, 0, 100);
			object->o_hit_type = HIT_DAMAGE;
			ObjectHitON();
		}
		if (objectlib_802A5288(2)) object->o_v4++;
		if (object->o_v4 > 3) object->o_phase++;
	}
	else if (object->o_phase == 1)
	{
		if (objectlib_802A5288(10))
		{
			object->o_phase++;
			object->o_hit_type = HIT_TAKE;
			ObjectHitOFF();
		}
	}
	else
	{
		ObjectSetAnime(11);
		if (ISTRUE(ObjectTurn(object->o_targetang, 0x800)))
		{
			object->o_mode = 2;
		}
	}
}

static void enemya_802A7A60(void)
{
	ObjectSetAnime(2);
	if (objectlib_802A4BE4(2, 2, 162, MSG_116))
	{
		ObjectMakeSound(NA_SE5_47);
		ObjectHide();
		ObjectHitOFF();
		enemya_802AAE8C(0, 0, 200);
		enemya_802AE0CC(20, S_SHARD, 3, 4);
		objectlib_802A50FC(1);
#if REVISION >= 199609
		objectlib_802A5588(2000, 4500, -4500, 200);
#else
		object->o_posy += 100;
		enemyb_802F2B88(2000, 4500, -4500);
#endif
		object->o_mode = 8;
	}
}

static void enemya_802A7B1C(void)
{
	if (object->o_timer == 60) Na_BgmStop(NA_BGM_BATTLE);
}

static void enemya_802A7B5C(void)
{
	if (object->o_posy-object->o_savey > -100)
	{
		if (object->o_move & OM_BOUND)
		{
			object->o_hp--;
			object->o_velf = 0;
			object->o_vely = 0;
			ObjectPlaySound(NA_SE5_16_80);
			if (object->o_hp)   object->o_mode = 6;
			else                object->o_mode = 7;
		}
	}
	else if (object->o_phase == 0)
	{
		if (object->o_move & OM_TOUCH)
		{
			object->o_velf = 0;
			object->o_vely = 0;
			object->o_phase++;
		}
		else if (object->o_move & OM_BOUND)
		{
			ObjectPlaySound(NA_SE5_16_80);
		}
	}
	else
	{
		if (objectlib_802A5288(10)) object->o_mode = 5;
		object->o_phase++;
	}
}

static void enemya_802A7D14(void)
{
	switch (object->o_phase)
	{
	case 0:
		if (object->o_timer == 0) ObjectPlaySound(NA_SE5_46);
		object->o_v1 = 1;
		ObjectSetAnimeHoldEnd(8);
		object->o_angy = ObjectAngToSave();
		if (object->o_posy < object->o_savey)
		{
			object->o_vely = 100;
		}
		else
		{
			enemya_802B3134(&object->o_savex, &object->o_posx, 100, -4);
			object->o_phase++;
		}
		break;
	case 1:
		ObjectSetAnimeHoldEnd(8);
		if (object->o_vely < 0 && object->o_posy < object->o_savey)
		{
			object->o_posy = object->o_savey;
			object->o_vely = 0;
			object->o_velf = 0;
			object->o_gravity = -4;
			object->o_v1 = 0;
			ObjectSetAnime(7);
			ObjectPlaySound(NA_SE5_16_80);
			objectlib_802A50FC(1);
			object->o_phase++;
		}
		break;
	case 2:
		if (objectlib_802A5288(7)) object->o_phase++;
		break;
	case 3:
		if (enemya_802A7384(1200))
		{
			object->o_mode = 0;
			Na_BgmStop(NA_BGM_BATTLE);
		}
		if (objectlib_802A48BC(500, 100)) object->o_phase++;
		break;
	case 4:
		if (objectlib_802A4BE4(2, 1, 162, MSG_128)) object->o_mode = 2;
		break;
	}
}

static OBJCALL *enemya_803300BC[] =
{
	enemya_802A7264,
	enemya_802A7804,
	enemya_802A73D8,
	enemya_802A7598,
	enemya_802A7B5C,
	enemya_802A7D14,
	enemya_802A78D8,
	enemya_802A7A60,
	enemya_802A7B1C,
};

static STEPSOUND enemya_803300E0[] =
{
	{0,  0,  0, NA_SE_NULL},
	{1,  1, 20, NA_SE5_15_80},
	{0,  0,  0, NA_SE_NULL},
	{0,  0,  0, NA_SE_NULL},
	{1, 15, -1, NA_SE5_15_80},
	{0,  0,  0, NA_SE_NULL},
	{0,  0,  0, NA_SE_NULL},
	{0,  0,  0, NA_SE_NULL},
	{0,  0,  0, NA_SE_NULL},
	{1, 33, -1, NA_SE5_15_80},
	{0,  0,  0, NA_SE_NULL},
	{1,  1, 15, NA_SE5_15_80},
};

static void enemya_802A7FBC(void)
{
	objectlib_802A2320();
	if (object->o_v1 == 0) objectlib_802A2348(-78);
	else ObjectProcMoveF();
	ObjectCallMode(enemya_803300BC);
	ObjectStepSound(enemya_803300E0);
	if (object->o_targetdist < 5000)    ObjectSetActive();
	else                                ObjectClrActive();
}

void enemya_802A8064(void)
{
	float sp34 = 20;
	float sp30 = 50;
	UNUSED int i, n;
	object->o_hit_flag |= HF_0004;
	switch (object->o_action)
	{
	case OA_0:
		enemya_802A7FBC();
		break;
	case OA_1:
		objectlib_802A01D8(6, 1);
		break;
	case OA_2:
	case OA_3:
		objectlib_802A0380(sp34, sp30, 4);
		ObjectHitOFF();
		object->o_posy += 20;
		break;
	}
	object->o_hit_result = 0;
}

extern OBJLANG obj_1300029C[];

void enemya_802A816C(void)
{
	ObjectSetShape(S_CHEST);
	object->o_angy = Rand();
	object->o_angy = 0;
	ObjMakeOff(0, 0, 97, -77, object, S_CHESTLID, obj_1300029C);
}

void enemya_802A81E8(void)
{
	ObjectRepelMario3D(200, 200);
}

extern OBJLANG obj_130003BC[];

void enemya_802A821C(void)
{
	switch (object->o_mode)
	{
	case 0:
		if (ObjCalcDist3D(object->parent, mario_obj) < 300) object->o_mode++;
		break;
	case 1:
		if (object->o_timer == 0)
		{
			ObjMakeOff(0, 0, -80, 120, object, S_BUBBLE_A, obj_130003BC);
			Na_ObjSePlay(NA_SE3_22, object);
		}
		object->o_shapeangx -= 0x400;
		if (object->o_shapeangx < -0x4000) object->o_mode++;
		FALLTHROUGH;
	case 2:
		break;
	}
}

void enemya_802A8370(void)
{
	ObjectSetScale(4);
}

extern OBJLANG obj_130002E4[];

void enemya_802A83A0(void)
{
	int i;
	object->s.scale[0] = 4 + 0.5* SIN(object->o_v0);
	object->s.scale[1] = 4 + 0.5*-SIN(object->o_v0);
	object->o_v0 += 0x400;
	if (object->o_timer < 30)
	{
		ObjectHitOFF();
		object->o_posy += 3;
	}
	else
	{
		ObjectHitON();
		ObjectAccelerate(2, 10);
		object->o_angy = ObjCalcAngY(object, mario_obj);
		ObjectProcMoveF();
	}
	object->o_posx += RandF()*4 - 2;
	object->o_posz += RandF()*4 - 2;
	if (object->o_hit_result & HR_008000 || object->o_timer > 200)
	{
		ObjectPlaySound(NA_SE3_0B);
		ObjKill(object);
		for (i = 0; i < 30; i++) ObjMakeHere(object, S_BUBBLE_A, obj_130002E4);
	}
	if (BGCheckWater(object->o_posx, object->o_posz) < object->o_posy)
	{
		ObjKill(object);
	}
	object->o_hit_result = 0;
}

void enemya_802A8630(void)
{
	object->o_v2 = 0x800 + (int)(0x800*RandF());
	object->o_v3 = 0x800 + (int)(0x800*RandF());
	ObjectPlaySound(NA_SE3_0B);
}

void enemya_802A86BC(void)
{
	ObjectSetScale(1.0+RandF());
}

void enemya_802A870C(void)
{
	object->o_posy += RandF()* 3 + 6;
	object->o_posx += RandF()*10 - 5;
	object->o_posz += RandF()*10 - 5;
	object->s.scale[0] = 1 + 0.2*SIN(object->o_v0);
	object->o_v0 += object->o_v2;
	object->s.scale[1] = 1 + 0.2*SIN(object->o_v1);
	object->o_v1 += object->o_v3;
}

extern OBJLANG obj_13002D28[];

void enemya_802A88A4(void)
{
	float water_y = BGCheckWater(object->o_posx, object->o_posz);
	object->s.scale[0] = 1 + 0.2*SIN(object->o_v0);
	object->o_v0 += object->o_v2;
	object->s.scale[1] = 1 + 0.2*SIN(object->o_v1);
	object->o_v1 += object->o_v3;
	if (object->o_posy > water_y)
	{
		object->flag = 0;
		object->o_posy += 5;
		if (obj_freelist.next) ObjMakeHere(object, S_WAVE, obj_13002D28);
	}
	if (object->o_hit_result & HR_008000) ObjKill(object);
}

static void enemya_802A8A38(void)
{
	object->s.scale[0] = 2 + 0.5*SIN(object->o_v0);
	object->o_v0 += object->o_v2;
	object->s.scale[1] = 2 + 0.5*SIN(object->o_v1);
	object->o_v1 += object->o_v3;
}

void enemya_802A8B18(void)
{
	ObjSetScaleXYZ(object, 2, 2, 1);
	object->o_v2 = 0x800 + (int)(0x800*RandF());
	object->o_v3 = 0x800 + (int)(0x800*RandF());
	ObjRandOff3D(object, 100);
}

extern OBJLANG obj_13002D28[];

void enemya_802A8BC0(void)
{
	float water_y = BGCheckWater(object->o_posx, object->o_posz);
	object->o_posy += 5;
	ObjRandOff2D(object, 4);
	enemya_802A8A38();
	if (object->o_posy > water_y && object->o_timer != 0)
	{
		ObjKill(object);
		ObjMakeEffect(5, 0, object, S_WAVE, obj_13002D28);
	}
}

void enemya_802A8C88(void)
{
	object->o_posy += 5;
	ObjRandOff2D(object, 4);
	enemya_802A8A38();
}

extern OBJLANG obj_1300046C[];

void enemya_802A8CDC(void)
{
	if (object_80361250 == 15 || object_80361250 == 7)
	{
		if (gfx_frame & 1) ObjMakeHere(object, S_DROPLET, obj_1300046C);
	}
}

extern OBJLANG obj_13000400[];

void enemya_802A8D48(void)
{
	int i;
	for (i = 0; i < 3; i++) ObjMakeHere(object, S_DROPLET, obj_13000400);
}

void enemya_802A8D98(void)
{
	object->o_posy += object->o_vely;
}

static void enemya_802A8DC0(void)
{
	if (object->o_timer == 0)
	{
		object->o_hit_result = 0;
		object->o_posx = object->o_savex;
		object->o_posy = object->o_savey;
		object->o_posz = object->o_savez;
		object->o_angx = 0;
		object->o_angy = (short)(object->o_code << 8);
		object->o_v0 = 0;
		object->o_v6 = 0;
		ObjectSetActive();
		ObjectHitON();
	}
	if (object->o_targetdist < 500)
	{
		ObjectHitON();
		ObjectSetActive();
		if (
			object->o_hit_result & HR_008000 &&
			!(object->o_hit_result & HR_800000)
		)
		{
			object->o_mode = 4;
			object->o_v6 = 1;
			object->o_v1 = 1;
		}
		else
		{
			object->o_hit_result = 0;
		}
	}
	else
	{
		ObjectHitOFF();
		ObjectClrActive();
		object->o_v6 = 0;
	}
}

static void enemya_802A8F40(void)
{
	if (object->o_timer == 0) ObjectPlaySound(NA_SE5_0D);
	object->o_posy += 5;
	object->o_posx += (float)((object->o_timer/2 & 1)-0.5) * 2;
	object->o_posz += (float)((object->o_timer/2 & 1)-0.5) * 2;
	if (object->o_timer > 67)
	{
		object->o_posx += (float)((object->o_timer/2 & 1)-0.5) * 4;
		object->o_posz += (float)((object->o_timer/2 & 1)-0.5) * 4;
		object->o_mode = 6;
	}
}

static void enemya_802A9114(void)
{
	if (object->o_timer == 0) ObjectPlaySound(NA_SE5_0E);
	if (object->o_timer < 4)
	{
		object->o_posx += (float)((object->o_timer/2 & 1)-0.5) * 4;
		object->o_posz += (float)((object->o_timer/2 & 1)-0.5) * 4;
	}
	else if (object->o_timer < 6)
	{
	}
	else if (object->o_timer < 22)
	{
		object->o_angy =
			SIN(object->o_v0)*0x4000 + (short)(object->o_code << 8);
		object->o_v0 += 0x400;
	}
	else if (object->o_timer < 26)
	{
	}
	else
	{
		object->o_v0 = 0;
		object->o_mode = 5;
	}
}

static void enemya_802A92FC(void)
{
	if (object->o_timer == 0) ObjectPlaySound(NA_SE5_0F);
	if (object->o_timer < 4)
	{
	}
	else if (object->o_timer < 20)
	{
		object->o_v0 += 0x400;
		object->o_angx = 0x2000*SIN(object->o_v0);
	}
	else if (object->o_timer < 25)
	{
	}
	else
	{
		object->o_mode = 1;
	}
}

static void enemya_802A93F8(void)
{
	UNUSED int i;
	ObjectHitOFF();
	ObjectClrActive();
	object->o_v6 = 0;
	object_8036125A = TRUE;
}

static void enemya_802A9440(void)
{
	object->o_mode = 3;
}

static void enemya_802A9460(void)
{
	UNUSED int i;
	if (object->o_timer > 3) object->o_mode = 0;
}

static OBJCALL *enemya_80330140[] =
{
	enemya_802A8DC0,
	enemya_802A93F8,
	enemya_802A9440,
	enemya_802A9460,
	enemya_802A8F40,
	enemya_802A92FC,
	enemya_802A9114,
};

void enemya_802A9498(void)
{
	ObjectCallMode(enemya_80330140);
	if (object->o_v1 != 0) object->o_v1++;
	object->o_hit_result = 0;
}

void enemya_802A94F8(void)
{
	OBJECT *parent = object->parent;
	if (parent->s.s.flag & SHP_ACTIVE)
	{
		ObjectSetActive();
		ObjCopyPos(object, object->parent);
		object->o_angy = object->parent->o_angy;
		object->o_shapeangx = object->parent->o_angx;
	}
	else
	{
		ObjectClrActive();
	}
}

struct enemya0
{
	short _00;
	float _04;
	float _08;
};

UNUSED static struct enemya0 enemya_8033015C[] =
{
	{0x200,  0, 1},
	{0x200, 10, 1},
	{0x200, 20, 1},
	{0x200, 20, 1},
	{0x800, 10, 1},
};

void enemya_802A958C(float speed, float vely, int hit_result)
{
	switch (object->parent->o_var)
	{
	case 0:
		break;
	case 1:
		ObjCopyCoordToShape(mario_obj, object);
		break;
	case 2:
		mario_obj->o_hit_result |= HR_000004+hit_result;
		player_data[0].speed = speed;
		player_data[0].vel[1] = vely;
		object->parent->o_var = 0;
		break;
	case 3:
		mario_obj->o_hit_result |= HR_000004+HR_000040;
		player_data[0].speed = 10;
		player_data[0].vel[1] = 10;
		object->parent->o_var = 0;
		break;
	}
	object->o_angy = object->parent->o_angy;
	if (!object->parent->flag) ObjKill(object);
}

void enemya_802A9708(void)
{
	enemya_802A958C(40, 40, 0x40);
}

int enemya_802A973C(int a0, float a1, float a2, SHORT a3)
{
	int result = 0;
	if (object->o_v1 != 4)
	{
		if (ObjectDistMarioToSave() > a1)
		{
			if (ObjectDistToSave() < 200)
			{
				result = 0;
			}
			else
			{
				result = 1;
				object->o_targetang = ObjectAngToSave();
			}
		}
		else if (object->o_targetdist > a2)
		{
			if (!(gfx_frame % a3))
			{
				object->o_targetang = ObjCalcAngY(object, mario_obj);
			}
			result = 2;
		}
		else
		{
			result = 3;
		}
		if (a0 && enemya_802C6538(&object->o_targetang))
		{
			result = 4;
			object->o_v1 = 4;
		}
	}
	else
	{
		result = 4;
	}
	return result;
}

static int enemya_802A98C4(float *x, float target, float speed)
{
	int result = FALSE;
	if (*x > target)
	{
		*x -= speed;
		if (*x < target) *x = target;
	}
	else if (*x < target)
	{
		*x += speed;
		if (*x > target) *x = target;
	}
	else
	{
		result = TRUE;
	}
	return result;
}

static void enemya_802A9994(void)
{
#ifdef sgi
	int fg;
#else
	int fg = 0;
#endif
	UNUSED int sp38, sp34, sp30, sp2C;
	int phase;
	if (object->o_timer == 0) object->o_v2 = 0;
	object->o_targetang = ObjCalcAngY(object, mario_obj);
	switch (phase = object->o_phase)
	{
	case 0:
		object->o_velf = 0;
		if (ObjectDistMarioToSave() < 2000)
		{
			ObjectTurn(object->o_targetang, 0x400);
			if (
				object->o_v2 > 40 ||
				DeltaAng(object->o_angy, object->o_targetang) < 0x1000
			) object->o_phase = 1;
		}
		else
		{
			object->o_phase = 3;
		}
		break;
	case 1:
		enemya_802A98C4(&object->o_velf, 30, 4);
		if (DeltaAng(object->o_angy, object->o_targetang) > 0x4000)
		{
			object->o_phase = 2;
		}
		if (ObjectDistMarioToSave() > 2000) object->o_phase = 3;
		break;
	case 2:
		enemya_802A98C4(&object->o_velf, 0, 4);
		if (object->o_v2 > 48) object->o_phase = 0;
		break;
	case 3:
		if (ObjectDistToSave() < 500)
		{
			object->o_velf = 0;
		}
		else
		{
			enemya_802A98C4(&object->o_velf, 10, 4);
			object->o_targetang = ObjectAngToSave();
			ObjectTurn(object->o_targetang, 0x800);
		}
		if (ObjectDistMarioToSave() < 1900) object->o_phase = 0;
		break;
	}
	if (object->o_phase != phase)   object->o_v2 = 0;
	else                            object->o_v2++;
	ObjectSetAnime(4);
	if (object->o_velf > 1) ObjectLevelSound(NA_SE6_0A);
	DbPrintErr("fg %d", fg);
	DbPrintErr("sp %d", object->o_velf);
}

static void enemya_802A9D08(void)
{
	if (object->o_phase == 0)
	{
		if (objectlib_802A5288(0)) object->o_phase++;
		object->o_v2 = 10 + 30*RandF();
		object->o_v3 = 0;
		object->o_velf = 0;
	}
	else if (object->o_phase == 1)
	{
		object->o_v3 += objectlib_802A5358();
		DbPrintErr("%d", object->o_v3);
		if (object->o_v3 > 10)
		{
			object->o_var = 3;
			object->o_mode = 3;
			object->o_hit_result &= ~HR_000800;
		}
		else
		{
			ObjectSetAnime(1);
			object->o_angy += 0x800;
			if (object->o_v2-- < 0)
			{
				if (enemya_802B14F4(50, 150) || object->o_v2 < -16)
				{
					object->o_phase++;
				}
			}
		}
	}
	else
	{
		ObjectSetAnime(3);
		if (ObjectIsAnimeFrame(18))
		{
			ObjectPlaySound(NA_SE5_1E);
			object->o_var = 2;
			object->o_mode = 3;
			object->o_hit_result &= ~HR_000800;
		}
	}
}

static void enemya_802A9F54(void)
{
	object->o_velf = 0;
	object->o_vely = 0;
	ObjectSetAnime(4);
	if (object->o_timer > 100) object->o_mode = 0;
}

static void enemya_802A9FC8(void)
{
	if (object->o_move & (
		OM_BOUND|OM_DIVE|OM_S_WATER|OM_U_WATER|OM_B_WATER|OM_0200
	))
	{
		ObjKill(object);
		ObjectMakeCoin(object, 5, 20);
		objectlib_802A37DC(NA_SE5_6E);
	}
}

static OBJCALL *enemya_80330198[] =
{
	enemya_802A9994,
	enemya_802A9D08,
	enemya_802A9FC8,
	enemya_802A9F54,
};

static void enemya_802AA02C(void)
{
	objectlib_802A2320();
	ObjectCallMode(enemya_80330198);
	objectlib_802A2348(-30);
	if (object->o_hit_result & HR_000800)
	{
		object->o_mode = 1;
		object->o_var = 1;
		ObjectPlaySound(NA_SE5_1D);
	}
}

void enemya_802AA0AC(void)
{
	float sp2C = 20;
	float sp28 = 50;
	ObjectSetScale(2);
	object->o_hit_flag |= HF_0004;
	switch (object->o_action)
	{
	case OA_0:
		enemya_802AA02C();
		break;
	case OA_1:
		objectlib_802A01D8(2, 0);
		break;
	case OA_2:
	case OA_3:
		objectlib_802A0380(sp2C, sp28, 2);
		break;
	}
	object->o_hit_result = 0;
	DbPrintErr("md %d", object->o_mode);
}

extern OBJLANG obj_13000624[];

void enemya_802AA1B8(void)
{
	if (player_data[0].state == PS_JUMP_18)
	{
		ObjectHitON();
		if (ObjIsObjHit(object, mario_obj))
		{
			if (ObjectHasScript(obj_13000624)) Na_Solution();
			ObjectMakeSound(NA_SE3_0F);
			object->o_hit_type = HIT_DAMAGE;
			object->o_ap = 1;
			objectlib_802A4440(80, 0);
		}
	}
	else
	{
		ObjectHitOFF();
	}
}

static int enemya_802AA280(UNUSED int a0)
{
	if (ObjIsObjHit(object, mario_obj))
	{
		if (DeltaAng(object->o_angy, mario_obj->o_angy) > 0x6000)
		{
			if (player_data[0].state == PS_JUMP_2A) return 1;
			if (player_data[0].state == PS_ATCK_00) return 1;
			if (player_data[0].state == PS_WALK_17) return 1;
			if (player_data[0].state == PS_WALK_1A) return 1;
			if (player_data[0].state == PS_JUMP_2C) return 2;
			if (player_data[0].state == PS_JUMP_06) return 2;
		}
	}
	return 0;
}

static void enemya_802AA3C8(void)
{
	object->o_v1 = 1600;
	object->o_v0 = 0;
}

void enemya_802AA3F4(void)
{
	switch (object->o_mode)
	{
	case 0:
		object->o_shapeangx = 0;
		if (enemya_802AA280(0))
		{
			enemya_802AA3C8();
			object->o_mode++;
		}
		ObjectMapLoad();
		break;
	case 1:
		object->o_shapeangx = 0;
		ObjectMapLoad();
		object->o_shapeangx = -SIN(object->o_v0)*object->o_v1;
		if (object->o_timer > 30)
		{
			int result = enemya_802AA280(0);
			if (result)
			{
				if (mario_obj->o_posy > object->o_posy+160 && result == 2)
				{
					object->o_mode++;
					ObjectPlaySound(NA_SE3_5A_40);
				}
				else
				{
					object->o_timer = 0;
				}
			}
		}
		if (object->o_timer != 0)
		{
			object->o_v1 -= 8;
			if (object->o_v1 < 0) object->o_mode = 0;
		}
		else
		{
			enemya_802AA3C8();
		}
		if (!(object->o_v0 & 0x7FFF)) ObjectPlaySound(NA_SE3_5A_40);
		object->o_v0 += 0x400;
		break;
	case 2:
		ObjectHitOFF();
		ObjectSetShape(58); /* T:shape */
		object->o_rotx -= 0x80;
		object->o_shapeangx += object->o_rotx;
		if (object->o_shapeangx < -0x4000)
		{
			object->o_shapeangx = -0x4000;
			object->o_rotx = 0;
			object->o_mode++;
			objectlib_802A50FC(1);
			ObjectPlaySound(NA_SE3_3D_80);
		}
		ObjectMapLoad();
		break;
	case 3:
		ObjectMapLoad();
		break;
	}
	object->s.m = NULL;
}

void enemya_802AA700(void)
{
	if (object->o_timer == 0) object->o_angy -= 0x4000;
	if (enemya_802AA280(0))
	{
		objectlib_802A4440(80, 0);
		ObjectMakeSound(NA_SE3_0F);
	}
}

void enemya_802AA774(void)
{
	if (object->o_mode == 0)
	{
		object->o_roty = 0;
		if (object->o_timer > 60) object->o_mode++;
	}
	else
	{
		object->o_roty = 0x100;
		if (object->o_timer > 126) object->o_mode = 0;
		ObjectLevelSound(NA_SE4_08);
	}
	ObjectRotateShape();
}

struct enemya1
{
	short flag;
	short scale;
	MAP *map;
	short checkdist;
};

extern MAP map_inside_0700FD30[];
extern MAP map_inside_070186B4[];

static struct enemya1 enemya_803301A8[] =
{
	{0, 100, map_inside_0700FD30, 2000},
	{0, 150, map_inside_070186B4, 1000},
};

void enemya_802AA830(void)
{
	CHAR arg = ObjGetArg(object);
	if (object->o_timer == 0)
	{
		ObjSetMap(object, enemya_803301A8[object->o_code].map);
		object->o_checkdist = enemya_803301A8[object->o_code].checkdist;
		ObjectSetScale(0.01F*enemya_803301A8[object->o_code].scale);
	}
	object->o_roty = 0x10*arg;
	object->o_shapeangy += object->o_roty;
}

static HITINFO enemya_803301C0 =
{
	/*type   */	HIT_TAKE,
	/*offset */	0,
	/*ap     */	0,
	/*hp     */	1,
	/*ncoin  */	0,
	/*hit r,h*/	80, 50,
	/*dmg r,h*/	0, 0,
};

static void enemya_802AA948(void)
{
	ObjSetHitInfo(object, &enemya_803301C0);
}

void enemya_802AA97C(void)
{
	switch (object->o_action)
	{
	case OA_0:
		enemya_802AA948();
		break;
	case OA_1:
		objectlib_802A01D8(-1, 0);
		break;
	case OA_2:
	case OA_3:
		ObjKill(object);
		objectlib_802A37AC();
		break;
	}
	if (object->o_hit_result & HR_400000)
	{
		ObjKill(object);
		objectlib_802A37AC();
	}
	object->o_hit_result = 0;
}

void enemya_802AAA60(void)
{
	if (object->o_timer == 0)
	{
		USHORT arg = ObjGetArg(object) & 0xFF;
		if      (arg ==    0)   object->hit_r = 50;
		else if (arg == 0xFF)   object->hit_r = 10000;
		else                    object->hit_r = 10.0*arg;
		object->hit_h = 50;
	}
	object->o_hit_result = 0;
}

void enemya_802AAB54(void)
{
	if (object->o_timer == 0)
	{
		USHORT arg = ObjGetArg(object) & 0xFF;
		if      (arg ==    0)   object->hit_r = 85;
		else if (arg == 0xFF)   object->hit_r = 10000;
		else                    object->hit_r = 10.0*arg;
		object->hit_h = 50;
	}
	object->o_hit_result = 0;
}

void enemya_802AAC48(void)
{
	if (object->o_timer == 0)
	{
		ObjectCalcVelF();
		object->o_f0 = object->s.scale[0];
		switch (object->o_code)
		{
		case 2:
			object->o_alpha = 0xFE;
			object->o_v1 = -21;
			object->o_v2 = 0;
			break;
		case 3:
			object->o_alpha = 0xFE;
			object->o_v1 = -13;
			object->o_v2 = 1;
			break;
		}
	}
	ObjectProcMove();
	ObjectCalcDrag(object->o_drag);
	if (object->o_vely > 100) object->o_vely = 100;
	if (object->o_timer > 20) ObjKill(object);
	if (object->o_alpha)
	{
		float scale;
		object->o_alpha += object->o_v1;
		if (object->o_alpha < 2) ObjKill(object);
		if (object->o_v2)   scale = object->o_f0*((254-object->o_alpha)/254.0);
		else                scale = object->o_f0*((    object->o_alpha)/254.0);
		ObjectSetScale(scale);
	}
}

static PARTICLE enemya_803301D0 =
{
	/*arg    */	2,
	/*count  */	20,
	/*shape  */	S_WHITEPUFF,
	/*offset */	0,
	/*velf   */	40, 5,
	/*vely   */	30, 20,
	/*gravity*/	-4,
	/*drag   */	30,
	/*scale  */	330, 10,
};

void enemya_802AAE8C(int count, int offset, float scale)
{
	enemya_803301D0.scale_start = scale;
	enemya_803301D0.scale_range = scale/20.0;
	enemya_803301D0.offset = offset;
	if      (count == 0)    enemya_803301D0.count = 20;
	else if (count > 20)    enemya_803301D0.count = count;
	else                    enemya_803301D0.count = 4;
	ObjectMakeParticle(&enemya_803301D0);
}

void enemya_802AAF48(void)
{
	int level;
	if (!(object->o_hit_flag & HF_0400))
	{
		object->o_actorinfo = object->parent->o_actorinfo;
	}
	level = ObjGetArg(object) & 0xFF;
	if (GetBit(level) & BuGetStar(course_index-1)) ObjectSetShape(S_SHADESTAR);
	ObjectPlaySound(NA_SE8_57);
}

static HITINFO enemya_803301E4 =
{
	/*type   */	HIT_STAR,
	/*offset */	0,
	/*ap     */	0,
	/*hp     */	0,
	/*ncoin  */	0,
	/*hit r,h*/	80, 50,
	/*dmg r,h*/	0, 0,
};

static void enemya_802AAFFC(void)
{
	ObjSetHitInfo(object, &enemya_803301E4);
	if (object->o_hit_result & HR_008000)
	{
		ObjDestroy(object);
		object->o_hit_result = 0;
	}
}

static void enemya_802AB060(void)
{
	float dx, dz;
	object->o_savex = mario_obj->o_posx;
	object->o_savez = mario_obj->o_posz;
	object->o_savey = mario_obj->o_posy;
	object->o_savey += 250;
	object->o_posy = object->o_savey;
	dx = object->o_savex - object->o_posx;
	dz = object->o_savez - object->o_posz;
	object->o_velf = DIST2(dx, dz) / 23;
}

static void enemya_802AB158(void)
{
	object->o_velf = 0;
	object->o_savey = object->o_posy;
}

static void enemya_802AB18C(void)
{
	if (object->o_roty > 0x400) object->o_roty -= 0x40;
}

extern OBJLANG obj_13002AF0[];

void enemya_802AB1C8(void)
{
	if (object->o_mode == 0)
	{
		if (object->o_timer == 0)
		{
			camera_8029000C(173, object);
			objectlib_802A4750(10);
			object->flag |= OBJ_0020;
			object->o_roty = 0x800;
			if (object->o_code == 0)    enemya_802AB060();
			else                        enemya_802AB158();
			object->o_angy = ObjectAngToSave();
			object->o_vely = 50;
			object->o_gravity = -4;
			objectlib_802A37AC();
		}
		ObjectLevelSound(NA_SE4_14);
		ObjMakeHere(object, S_NULL, obj_13002AF0);
		if (object->o_vely < 0 && object->o_posy < object->o_savey)
		{
			object->o_mode++;
			object->o_velf = 0;
			object->o_vely = 20;
			object->o_gravity = -1;
#if NA_REVISION >= 101
			if (object->o_hit_flag & HF_0400)   Na_StarAppear(1);
			else                                Na_StarAppear(1);
#else
			if (object->o_hit_flag & HF_0400)   Na_StarAppear(0);
			else                                Na_StarAppear(1);
#endif
		}
	}
	else if (object->o_mode == 1)
	{
		if (object->o_vely < -4) object->o_vely = -4;
		if (object->o_vely < 0 && object->o_posy < object->o_savey)
		{
			camera_8033CBC8 = 1;
			object->o_vely = 0;
			object->o_gravity = 0;
			object->o_mode++;
		}
		ObjMakeHere(object, S_NULL, obj_13002AF0);
	}
	else if (object->o_mode == 2)
	{
		if (!camerap->demo && !camera_8032DF54)
		{
			objectlib_802A4774(10);
			object->flag &= ~OBJ_0020;
			object->o_mode++;
		}
	}
	else
	{
		enemya_802AAFFC();
		enemya_802AB18C();
	}
	ObjectProcMoveF();
	object->o_shapeangy += object->o_roty;
	object->o_hit_result = 0;
}

extern OBJLANG obj_1300080C[];

void enemya_802AB558(int level)
{
	OBJECT *o = ObjMakeHere(object, S_POWERSTAR, obj_1300080C);
	o->o_actorinfo = level << 24;
	o->o_hit_flag = HF_0400;
	ObjSetAng(o, 0, 0, 0);
}

static HITINFO enemya_803301F4 =
{
	/*type   */	HIT_COIN,
	/*offset */	0,
	/*ap     */	1,
	/*hp     */	0,
	/*ncoin  */	0,
	/*hit r,h*/	100, 64,
	/*dmg r,h*/	0, 0,
};

extern OBJLANG obj_13000A14[];

static int enemya_802AB5C8(void)
{
	if (object->o_hit_result & HR_008000 && !(object->o_hit_result & HR_800000))
	{
		ObjMakeHere(object, S_SPARKLE, obj_13000A14);
		ObjKill(object);
		return TRUE;
	}
	object->o_hit_result = 0;
	return FALSE;
}

extern OBJLANG obj_coin[];

void enemya_802AB650(void)
{
	ObjectSetScript(obj_coin);
	ObjSetHitInfo(object, &enemya_803301F4);
	ObjectInitArea();
	ObjectCheckGroundY();
	if (fabsf(object->o_posy-object->o_ground_y) > 500)
	{
		ObjectSetShape(S_COIN_NOSHADOW);
	}
	if (object->o_ground_y < -10000) ObjKill(object);
}

void enemya_802AB70C(void)
{
	enemya_802AB5C8();
	object->o_shape++;
}

void enemya_802AB748(void)
{
	object->o_shape++;
	if (ObjectFlash(200, 20)) ObjKill(object);
	enemya_802AB5C8();
}

void enemya_802AB7A4(void)
{
	object->o_vely = RandF()*10 + 30 + object->o_f7;
	object->o_velf = RandF()*10;
	object->o_angy = Rand();
	ObjectSetScript(obj_coin);
	ObjSetHitInfo(object, &enemya_803301F4);
	ObjectHitOFF();
}

void enemya_802AB860(void)
{
	BGFACE *ground;
	objectlib_802A2320();
	objectlib_802A452C();
	objectlib_802A2348(-62);
	if ((ground = object->o_ground))
	{
		if (object->o_move & OM_TOUCH) object->o_phase = 1;
		if (object->o_phase == 1)
		{
			object->o_density = 0;
			if (ground->ny < 0.9)
			{
				SHORT angy = ATAN2(ground->nz, ground->nx);
				ObjectTurn(angy, 0x400);
			}
		}
	}
	if (object->o_timer == 0) ObjectPlaySound(NA_SE3_30);
	if (object->o_vely < 0) ObjectHitON();
#if REVISION >= 199609
	if (object->o_move & OM_BOUND)
	{
		if (object->o_move & (OM_0800|OM_4000)) ObjKill(object);
	}
	if (object->o_move & OM_2000)
	{
		if (object->o_v9 < 5) ObjectPlaySound(NA_SE3_36);
		object->o_v9++;
	}
#else
	if (object->o_move & OM_BOUND)
	{
		if (object->o_move & OM_0800) ObjKill(object);
	}
	if (object->o_move & OM_2000) ObjectPlaySound(NA_SE3_36);
#endif
	if (ObjectFlash(400, 20)) ObjKill(object);
	enemya_802AB5C8();
}

void enemya_802ABA40(void)
{
	if (object->o_timer == 0)
	{
		ObjectSetScript(obj_coin);
		ObjSetHitInfo(object, &enemya_803301F4);
		ObjectInitArea();
		if (object->o_v1)
		{
			object->o_posy += 300;
			ObjectCheckGroundY();
			if (
				object->o_posy < object->o_ground_y ||
				object->o_ground_y < -10000
			) ObjKill(object);
			else object->o_posy = object->o_ground_y;
		}
		else
		{
			ObjectCheckGroundY();
			if (fabsf(object->o_posy-object->o_ground_y) > 250)
			{
				ObjectSetShape(S_COIN_NOSHADOW);
			}
		}
	}
	else
	{
		if (enemya_802AB5C8()) object->parent->o_v0 |= GetBit(object->o_code);
		object->o_shape++;
	}
	if (object->parent->o_mode == 2) ObjKill(object);
}

static short enemya_80330204[][2] =
{
	{   0, -150},
	{   0,  -50},
	{   0,   50},
	{   0,  150},
	{ -50,  100},
	{-100,   50},
	{  50,  100},
	{ 100,   50},
};

extern OBJLANG obj_130008D0[];

static void enemya_802ABC04(int a0, int a1)
{
	OBJECT *o;
	int off[3];
	int sp3C = TRUE;
	int sp38 = 1;
	off[0] = off[1] = off[2] = 0;
	switch (a1 & 7)
	{
	case 0:
		off[2] = 160*a0 - 320;
		if (a0 > 4) sp3C = FALSE;
		break;
	case 1:
		sp38 = 0;
		off[1] = 160*a0 * 0.8;
		if (a0 > 4) sp3C = FALSE;
		break;
	case 2:
		off[0] = 300*SIN(0x2000*a0);
		off[2] = 300*COS(0x2000*a0);
		break;
	case 3:
		sp38 = 0;
		off[0] = 200*COS(0x2000*a0);
		off[1] = 200*SIN(0x2000*a0) + 200;
		break;
	case 4:
		off[0] = enemya_80330204[a0][0];
		off[2] = enemya_80330204[a0][1];
		break;
	}
	if (a1 & 0x10) sp38 = 0;
	if (sp3C)
	{
		o = ObjMakeOff(
			a0, off[0], off[1], off[2], object, S_COIN, obj_130008D0
		);
		o->o_v1 = sp38;
	}
}

void enemya_802ABEE4(void)
{
	object->o_v0 = object->o_actorinfo >> 8 & 0xFF;
}

void enemya_802ABF0C(void)
{
	int i;
	switch (object->o_mode)
	{
	case 0:
		if (object->o_targetdist < 2000)
		{
			for (i = 0; i < 8; i++)
			{
				if (!(object->o_v0 & (1 << i)))
				{
					enemya_802ABC04(i, object->o_code);
				}
			}
			object->o_mode++;
		}
		break;
	case 1:
		if (object->o_targetdist > 2100) object->o_mode++;
		break;
	case 2:
		object->o_mode = 0;
		break;
	}
	ObjSetActorFlag(object, object->o_v0 & 0xFF);
}

static void enemya_802AC068(void)
{
	objectlib_802A2320();
	objectlib_802A452C();
	if (object->o_move & OM_2000) ObjectPlaySound(NA_SE3_36);
	if (object->o_timer > 90 || object->o_move & OM_BOUND)
	{
		ObjSetHitInfo(object, &enemya_803301F4);
		ObjectHitON();
		ObjectSetScript(obj_coin);
	}
	objectlib_802A2348(-30);
	enemya_802AB5C8();
	if (ObjectHasShapeID(S_BLUECOIN)) object->o_ap = 5;
	if (ObjectFlash(400, 20)) ObjKill(object);
}

static void enemya_802AC15C(void)
{
	SHORT angy;
	float speed;
	OBJECT *parent = object->parent;
	ObjectHitOFF();
	if (object->o_timer == 0)
	{
		if (stage_index == STAGE_BBH)
		{
			ObjectSetShape(S_BLUECOIN);
			ObjectSetScale(0.7F);
		}
	}
	ObjCopyPos(object, parent);
	if (parent->o_var == 1)
	{
		object->o_mode = 1;
		angy = mario_obj->o_angy;
		speed = 3;
		object->o_velx = speed * SIN(angy);
		object->o_velz = speed * COS(angy);
		object->o_vely = 35;
	}
}

static OBJCALL *enemya_80330224[] =
{
	enemya_802AC15C,
	enemya_802AC068,
};

void enemya_802AC294(void)
{
	ObjectCallMode(enemya_80330224);
}

void enemya_802AC2C0(void)
{
	ObjectSetScale(0.6F);
}

extern OBJLANG obj_130009E0[];

void enemya_802AC2EC(void)
{
	OBJECT *o;
	UNUSED int i;
	float offset = 30;
	o = ObjMakeHere(object, S_SPARKLE, obj_130009E0);
	o->o_posx += RandF()*offset - offset/2;
	o->o_posz += RandF()*offset - offset/2;
}

void enemya_802AC3A8(void)
{
	if (object->o_timer == 0)
	{
		short angy = object->o_angy;
		object->o_f0 = 1.28F;
		ObjectSetPosOff(mario_obj, 0, 60, 100);
		object->o_angy = angy;
	}
	ObjectProcMoveF();
	object->o_shape = 5;
	ObjectSetScale(object->o_f0);
	object->o_f0 -= 0.2F;
	if (object->o_timer > 6+db_work[4][0]) ObjKill(object);
}

static short enemya_8033022C[] =
{
	DEG(-67.5), DEG(0),
	DEG( 67.5), DEG(0),
	DEG(-47.25), DEG( 47.25),
	DEG( 47.25), DEG( 47.25),
	DEG(-47.25), DEG(-47.25),
	DEG( 47.25), DEG(-47.25),
};

extern OBJLANG obj_13000ABC[];

void enemya_802AC4A0(void)
{
	int i;
	UNUSED int n;
	for (i = 0; i < 6; i++)
	{
		OBJECT *o = ObjMakeHere(object, S_SHARD, obj_13000ABC);
		o->o_angy = mario_obj->o_angy+0x8000 + enemya_8033022C[2*i+0];
		o->o_vely = 25*SIN(enemya_8033022C[2*i+1]);
		o->o_velf = 25*COS(enemya_8033022C[2*i+1]);
	}
}

void enemya_802AC5B4(void)
{
	if (object->o_timer == 0)
	{
		short angy = object->o_angy;
		object->o_f0 = 0.28F;
		ObjectSetPosOff(mario_obj, 0, 30, 110);
		object->o_angy = angy;
	}
	ObjectProcMoveF();
	object->o_shape = 4;
	ObjectSetScale(object->o_f0);
	object->o_f0 -= 0.015F;
}

static short enemya_80330244[] =
{
	DEG(-45), DEG(0),
	DEG(  0), DEG(0),
	DEG( 45), DEG(0),
	DEG(-31.5), DEG( 31.5),
	DEG( 31.5), DEG( 31.5),
	DEG(-31.5), DEG(-31.5),
	DEG( 31.5), DEG(-31.5),
};

extern OBJLANG obj_13000A34[];

void enemya_802AC678(void)
{
	int i;
	UNUSED int n;
	for (i = 0; i < 7; i++)
	{
		OBJECT *o = ObjMakeHere(object, S_STAR, obj_13000A34);
		o->o_angy = mario_obj->o_angy+0x8000 + enemya_80330244[2*i+0];
		o->o_vely = 25*SIN(enemya_80330244[2*i+1]);
		o->o_velf = 25*COS(enemya_80330244[2*i+1]);
	}
}

void enemya_802AC78C(void)
{
	if (object->o_timer == 0)
	{
		object->o_f0 = 0.28F;
		object->o_velf = 25;
		object->o_posy -= 20;
		object->o_vely = 14;
	}
	ObjectProcMoveF();
	object->o_shape = 4;
	ObjectSetScale(object->o_f0);
	object->o_f0 -= 0.015F;
}

extern OBJLANG obj_13000A78[];

void enemya_802AC864(void)
{
	int i, n = 8;
	for (i = 0; i < n; i++)
	{
		OBJECT *o = ObjMakeHere(object, S_STAR, obj_13000A78);
		o->o_angy = 0x10000*i/n;
	}
}

typedef struct struct80330260
{
	u32 hit_result;
	int mode;
}
STRUCT80330260;

static STRUCT80330260 enemya_80330260[] =
{
	{HR_040000, 3},
	{HR_080000, 4},
	{HR_010000, 1},
	{HR_020000, 2},
	{-1, 0},
};

static void enemya_802AC910(int anime)
{
	ObjectSetAnime(anime);
	if (objectlib_8029FF04()) object->o_mode = 0;
}

extern OBJLANG obj_door[];

static void enemya_802AC958(void)
{
	if (object->script == SegmentToVirtual(obj_door))
	{
		pl_camera_data[0].demo = 6;
	}
	else
	{
		pl_camera_data[0].demo = 5;
	}
	pl_camera_data[0].obj = object;
}

static Na_Se enemya_80330288[] = {NA_SE3_04, NA_SE3_06};
static Na_Se enemya_80330290[] = {NA_SE3_05, NA_SE3_07};

static void enemya_802AC9D0(void)
{
	int i = ObjectHasShapeID(S_DOOR_D);
	if (object->o_timer == 0)
	{
		ObjectPlaySound(enemya_80330288[i]);
		object_flag |= OBJECT_20;
	}
	if (object->o_timer == 70) ObjectPlaySound(enemya_80330290[i]);
}

static void enemya_802ACA6C(void)
{
	int i = ObjectHasShapeID(S_DOOR_D);
	if (object->o_timer == 30) ObjectPlaySound(enemya_80330290[i]);
}

void enemya_802ACAC8(void)
{
	int i = 0;
	while (enemya_80330260[i].hit_result != (u32)-1)
	{
		if (ObjectCheckHitResult(enemya_80330260[i].hit_result))
		{
			enemya_802AC958();
			ObjectInitMode(enemya_80330260[i].mode);
		}
		i++;
	}
	switch (object->o_mode)
	{
	case 0:
		ObjectSetAnime(0);
		break;
	case 1:
		enemya_802AC910(1);
		enemya_802AC9D0();
		break;
	case 2:
		enemya_802AC910(2);
		enemya_802AC9D0();
		break;
	case 3:
		enemya_802AC910(3);
		enemya_802ACA6C();
		break;
	case 4:
		enemya_802AC910(4);
		enemya_802ACA6C();
		break;
	}
	if (object->o_mode == 0) ObjectMapLoad();
	enemya_802ACE80();
}

void enemya_802ACC3C(void)
{
	float posx, posz;
	BGFACE *ground;
	posx = object->o_posx;
	posz = object->o_posz;
	BGCheckGround(posx, object->o_posy, posz, &ground);
	if (ground) object->o_v1 = ground->area;
	posx = object->o_posx +  200*SIN(object->o_angy);
	posz = object->o_posz +  200*COS(object->o_angy);
	BGCheckGround(posx, object->o_posy, posz, &ground);
	if (ground) object->o_v2 = ground->area;
	posx = object->o_posx + -200*SIN(object->o_angy);
	posz = object->o_posz + -200*COS(object->o_angy);
	BGCheckGround(posx, object->o_posy, posz, &ground);
	if (ground) object->o_v3 = ground->area;
	if (object->o_v1 > 0 && object->o_v1 < 60)
	{
		area_table[object->o_v1][0] = object->o_v2;
		area_table[object->o_v1][1] = object->o_v3;
	}
}

void enemya_802ACE80(void)
{
	int flag = FALSE;
	if (object_80361250 != 0)
	{
		if      (object_80361250 == object->o_v1) flag = TRUE;
		else if (object_80361250 == object->o_v2) flag = TRUE;
		else if (object_80361250 == object->o_v3) flag = TRUE;
		else if (area_table[object_80361250][0] == object->o_v2) flag = TRUE;
		else if (area_table[object_80361250][0] == object->o_v3) flag = TRUE;
		else if (area_table[object_80361250][1] == object->o_v2) flag = TRUE;
		else if (area_table[object_80361250][1] == object->o_v3) flag = TRUE;
	}
	else
	{
		flag = TRUE;
	}
	if (ISTRUE(flag))
	{
		object->s.s.flag |= SHP_ACTIVE;
		object_80361254++;
	}
	if (ISFALSE(flag)) object->s.s.flag &= ~SHP_ACTIVE;
	object->o_var = flag;
}

static void enemya_802AD078(void)
{
	if (object->o_timer == 0) object->o_v0 = 20 + 10*RandF();
	if (object->o_timer > object->o_v0) object->o_mode = 0;
}

static void enemya_802AD10C(void)
{
	object->o_vely += -4;
	object->o_posy += object->o_vely;
	if (object->o_posy < object->o_savey)
	{
		object->o_posy = object->o_savey;
		object->o_vely = 0;
		object->o_mode = 3;
	}
}

static void enemya_802AD1A4(void)
{
	if (object->o_timer == 0)
	{
		if (object->o_targetdist < 1500)
		{
			objectlib_802A50FC(1);
			ObjectPlaySound(NA_SE5_0C);
		}
	}
	if (object->o_timer >= 10) object->o_mode = 4;
}

static void enemya_802AD238(void)
{
	if (object->o_timer == 0) object->o_v0 = 10 + 30*RandF();
	if (object->o_timer > object->o_v0) object->o_mode = 2;
}

static void enemya_802AD2D0(void)
{
	if (object->o_timer > 40+object->o_code)
	{
		object->o_mode = 1;
		object->o_posy += 5;
	}
	else
	{
		object->o_posy += 10;
	}
}

static OBJCALL *enemya_80330298[] =
{
	enemya_802AD2D0,
	enemya_802AD238,
	enemya_802AD10C,
	enemya_802AD1A4,
	enemya_802AD078,
};

void enemya_802AD34C(void)
{
	ObjectCallMode(enemya_80330298);
}

void enemya_802AD378(void)
{
	switch (object->o_mode)
	{
	case 0:
		if (mario_obj->movebg == object)
		{
			object->o_mode++;
			object->o_v0 = 0x80*RandSign();
		}
		break;
	case 1:
		ObjectCheckGroundY();
		if (object->o_timer > 5)
		{
			object->o_mode++;
			ObjectPlaySound(NA_SE3_2D);
		}
		break;
	case 2:
		if (object->o_rotx < 0x400) object->o_rotx += 0x80;
		if (-0x400 < object->o_rotz && object->o_rotz < 0x400)
		{
			object->o_rotz += object->o_v0;
		}
		object->o_gravity = -3;
		ObjectRotateShape();
		ObjectProcMoveF();
		if (object->o_posy < object->o_ground_y-300) object->o_mode++;
		break;
	case 3:
		break;
	}
	if (object->parent->o_mode == 3) ObjKill(object);
}

struct enemya2
{
	short count;
	short start;
	short stride;
	short shape;
	MAP *map;
};

extern MAP map_0700FAEC[];
extern MAP map_07026B1C[];
extern MAP map_0701D18C[];
extern MAP map_07015288[];

static struct enemya2 enemya_803302AC[] =
{
	{9, -512, 128, 176, map_0700FAEC}, /* T:shape */
	{9, -412, 103,  56, map_07026B1C}, /* T:shape */
	{9, -512, 128,  60, map_0701D18C}, /* T:shape */
	{9, -512, 128,  64, map_07015288}, /* T:shape */
};

extern OBJLANG obj_13000C04[];
extern OBJLANG obj_13000C64[];

static void enemya_802AD580(void)
{
	OBJECT *o;
	int i, n = object->o_code;
	int x, z, y = 0, offy = 0;
	for (i = 0; i < enemya_803302AC[n].count; i++)
	{
		x = 0;
		z = 0;
		if (n == 3) x = enemya_803302AC[n].start + enemya_803302AC[n].stride*i;
		else        z = enemya_803302AC[n].start + enemya_803302AC[n].stride*i;
		if (ObjectHasScript(obj_13000C64))
		{
			if (!(i % 3)) y -= 150;
			offy = 450;
		}
		o = ObjMakeOff(
			0, x, y+offy, z, object, enemya_803302AC[n].shape, obj_13000C04
		);
		ObjSetMap(o, enemya_803302AC[n].map);
	}
	object->o_mode = 2;
}

static void enemya_802AD76C(void)
{
	ObjectHide();
	if (ObjectHasScript(obj_13000C64))
	{
		ObjectShow();
	}
	else if (object->o_targetdist > 1200)
	{
		object->o_mode = 3;
		ObjectShow();
	}
}

static void enemya_802AD7F4(void)
{
	ObjectShow();
	object->o_mode = 0;
}

static void enemya_802AD828(void)
{
	if (ObjectHasScript(obj_13000C64) || object->o_targetdist < 1000)
	{
		object->o_mode = 1;
	}
}

static OBJCALL *enemya_803302DC[] =
{
	enemya_802AD828,
	enemya_802AD580,
	enemya_802AD76C,
	enemya_802AD7F4,
};

void enemya_802AD890(void)
{
	ObjectCallMode(enemya_803302DC);
}

static void enemya_802AD8BC(void)
{
	ObjectPlaySound(NA_SE3_40_40);
	objectlib_802A50FC(1);
}

static void enemya_802AD8F0(void)
{
	object->o_vely = 0;
	if (object->o_v3 == 2)
	{
		if (mario_obj->movebg == object)
		{
			if (object->o_posy > object->o_f2)  object->o_mode = 2;
			else                                object->o_mode = 1;
		}
	}
	else if (mario_obj->o_posy > object->o_f2 || object->o_v3 == 1)
	{
		object->o_posy = object->o_f1;
		if (mario_obj->movebg == object) object->o_mode = 2;
	}
	else
	{
		object->o_posy = object->o_f0;
		if (mario_obj->movebg == object) object->o_mode = 1;
	}
}

static void enemya_802ADA4C(void)
{
	ObjectLevelSound(NA_SE4_02);
	if (object->o_timer == 0)
	{
		if (ObjectIsMarioBG()) enemya_802AD8BC();
	}
	Accelerate(&object->o_vely, 10, 2);
	object->o_posy += object->o_vely;
	if (object->o_posy > object->o_f1)
	{
		object->o_posy = object->o_f1;
		if (object->o_v3 == 2 || object->o_v3 == 1) object->o_mode = 3;
		else if (mario_obj->o_posy < object->o_f2)  object->o_mode = 2;
		else                                        object->o_mode = 3;
	}
}

static void enemya_802ADB88(void)
{
	ObjectLevelSound(NA_SE4_02);
	if (object->o_timer == 0)
	{
		if (ObjectIsMarioBG()) enemya_802AD8BC();
	}
	Accelerate(&object->o_vely, -10, -2);
	object->o_posy += object->o_vely;
	if (object->o_posy < object->o_f0)
	{
		object->o_posy = object->o_f0;
		if      (object->o_v3 == 1)                 object->o_mode = 4;
		else if (object->o_v3 == 2)                 object->o_mode = 3;
		else if (mario_obj->o_posy > object->o_f2)  object->o_mode = 1;
		else                                        object->o_mode = 3;
	}
}

static void enemya_802ADCE4(void)
{
	object->o_vely = 0;
	if (object->o_timer == 0)
	{
		objectlib_802A50FC(1);
		ObjectPlaySound(NA_SE3_6B);
	}
	if (!Player1IsJump() && !ObjectIsMarioBG()) object->o_mode = 1;
}

static void enemya_802ADD70(void)
{
	object->o_vely = 0;
	if (object->o_timer == 0)
	{
		objectlib_802A50FC(1);
		ObjectPlaySound(NA_SE3_6B);
	}
	if (!Player1IsJump() && !ObjectIsMarioBG()) object->o_mode = 0;
}

static short enemya_803302EC[] =
{
	  -51,    0, FALSE,
	 -461,    0, FALSE,
	 -512,    0, FALSE,
	-2611,    0, FALSE,
	-2360,    0, FALSE,
	  214,    0, FALSE,
	  -50, 1945, TRUE,
};

extern OBJLANG obj_13000CFC[];

void enemya_802ADDF8(void)
{
	int flag = enemya_803302EC[3*object->o_code+2];
	if (!flag)
	{
		object->o_f0 = enemya_803302EC[3*object->o_code+0];
		object->o_f1 = object->o_savey;
		object->o_f2 = (object->o_f0+object->o_f1)/2;
		object->o_v3 = ObjectHasScript(obj_13000CFC);
	}
	else
	{
		object->o_f0 = enemya_803302EC[3*object->o_code+0];
		object->o_f1 = enemya_803302EC[3*object->o_code+1];
		object->o_f2 = (object->o_f0+object->o_f1)/2;
		object->o_v3 = 2;
	}
}

static OBJCALL *enemya_80330318[] =
{
	enemya_802AD8F0,
	enemya_802ADA4C,
	enemya_802ADB88,
	enemya_802ADD70,
	enemya_802ADCE4,
};

void enemya_802ADF6C(void)
{
	ObjectCallMode(enemya_80330318);
}

extern OBJLANG obj_13000D6C[];

void enemya_802ADF98(void)
{
	enemya_802AE45C(0x00020000);
	ObjMakeHere(object, S_WHITEPUFF, obj_13000D6C);
}

void enemya_802ADFD8(void)
{
	float scale;
	if (object->o_timer == 0)
	{
		object->o_angy = mario_obj->o_angy;
		ObjRandOff2D(object, 10);
	}
	ObjectProcMoveF();
	object->o_alpha -= 42;
	scale = (254-object->o_alpha)/254.0 * 1.0 + 0.5;
	ObjectSetScale(scale);
	if (object->o_alpha <= 1) ObjKill(object);
}

extern OBJLANG obj_13000DB4[];

void enemya_802AE0CC(SHORT count, SHORT shape, float scale, SHORT frame)
{
	OBJECT *o;
	int i;
	for (i = 0; i < count; i++)
	{
		o = ObjMakeHere(object, shape, obj_13000DB4);
		o->o_shape = frame;
		o->o_posy += 100;
		o->o_angy = Rand();
		o->o_shapeangy = o->o_angy;
		o->o_shapeangx = Rand();
		o->o_vely = RandRange(50);
		if (shape == S_SHARD || shape == 56) /* T:shape */
		{
			o->o_rotx = 0xF00;
			o->o_roty = 0x500;
			o->o_velf = 30;
		}
		else
		{
			o->o_rotx = 0x80*(int)(50+RandF());
			o->o_velf = 30;
		}
		ObjSetScale(o, scale);
	}
}

void enemya_802AE238(void)
{
	object->o_posy = BGCheckWater(object->o_savex, object->o_savez) + 20;
	object->o_posx = object->o_savex + RandRange(150);
	object->o_posz = object->o_savez + RandRange(150);
	object->o_alpha = 200 + 50*RandF();
}

void enemya_802AE304(void)
{
	enemya_802AE45C(0x8000);
	enemya_802AE334();
}

static PARTICLE enemya_8033032C =
{
	/*arg    */	3,
	/*count  */	20,
	/*shape  */	S_WHITEPUFF,
	/*offset */	20,
	/*velf   */	10, 5,
	/*vely   */	0, 0,
	/*gravity*/	0,
	/*drag   */	30,
	/*scale  */	30, 1.5,
};

void enemya_802AE334(void)
{
	ObjectMakeParticle(&enemya_8033032C);
}

static PARTICLE enemya_80330340 =
{
	/*arg    */	0,
	/*count  */	5,
	/*shape  */	S_SAND,
	/*offset */	0,
	/*velf   */	0, 20,
	/*vely   */	20, 0,
	/*gravity*/	-4,
	/*drag   */	30,
	/*scale  */	5, 2,
};

void enemya_802AE360(void)
{
	enemya_802AE45C(0x4000);
	ObjectMakeParticle(&enemya_80330340);
}

static short enemya_80330354[] = {2, -8, 1, 4};

extern OBJLANG obj_13002528[];

void enemya_802AE394(void)
{
	OBJECT *o = ObjMakeHereScale(object, S_DUST, obj_13002528, 1);
	o->o_velf = enemya_80330354[0];
	o->o_vely = enemya_80330354[1];
	o->o_gravity = enemya_80330354[2];
	ObjRandOff3D(o, enemya_80330354[3]);
}

void enemya_802AE45C(int a0)
{
	object->parent->o_effect &= ~0^a0;
}

static PARTICLE enemya_8033035C =
{
	/*arg    */	0,
	/*count  */	5,
	/*shape  */	S_SNOW,
	/*offset */	0,
	/*velf   */	0, 20,
	/*vely   */	20, 0,
	/*gravity*/	-4,
	/*drag   */	30,
	/*scale  */	2, 2,
};

void enemya_802AE48C(void)
{
	enemya_802AE45C(0x00010000);
	ObjectMakeParticle(&enemya_8033035C);
}

extern OBJLANG obj_13000E70[];

void enemya_802AE4C0(short angx, short angy)
{
	int i;
	for (i = 0; i < 3; i++)
	{
		OBJECT *o = ObjMakeHere(object, S_WHITEPUFF, obj_13000E70);
		o->o_angy = angy;
		o->o_angx = angx;
	}
}

void enemya_802AE534(void)
{
	SHORT speed = 500;
	float scale = 1;
	if (object->o_timer == 0)
	{
		object->o_alpha = 100;
		if (object->o_angx == 0)
		{
			ObjRandOff2D(object, 900);
			object->o_posx += SIN(object->o_angy+0x8000) * speed;
			object->o_posy += 80 + RandRange(200);
			object->o_posz += COS(object->o_angy+0x8000) * speed;
			object->o_angy += RandRange(4000);
			object->o_velf = 50 + 70*RandF();
		}
		else
		{
			ObjRandOff2D(object, 600);
			object->o_posy -= speed - 200;
			object->o_vely = 50 + 30*RandF();
			object->o_angy = Rand();
			object->o_velf = 10;
		}
		ObjSetBillboard(object);
		ObjectSetScale(scale);
	}
	if (object->o_timer > 8) ObjKill(object);
	object->o_shapeangx += 4000 + 2000*RandF();
	object->o_shapeangy += 4000 + 2000*RandF();
	ObjectProcMoveF();
}

extern OBJLANG obj_130000F8[];

void enemya_802AE85C(void)
{
	int i;
	objectlib_802A2320();
	objectlib_802A2348(78);
	if (object->o_move & OM_TOUCH) ObjKill(object);
	if (ObjIsObjHit(object, mario_obj))
	{
		ObjKill(object);
		for (i = 0; i < 10; i++) ObjMakeHere(object, S_BUBBLE_B, obj_130000F8);
	}
}

void enemya_802AE908(void)
{
	switch (object->o_mode)
	{
	case 0:
		if (object->o_timer == 0)
		{
			if (GetBit(1) & BuGetStar(course_index-1))
			{
				ObjectSetShape(S_SHADESTAR);
			}
		}
		ObjCopyPos(object, object->parent);
		ObjCopyActorInfo(object, object->parent);
		if (object->parent->o_mode == 3) object->o_mode++;
		break;
	case 1:
		ObjKill(object);
		objectlib_802A37AC();
		enemya_802AE0CC(20, S_SHARD, 0.7F, 3);
		enemyb_802F2B88(2500, -1200, 1300);
		break;
	}
	object->o_shapeangy += 0x400;
}

static void enemya_802AEA6C(void)
{
	if (object->o_var != 0) object->o_mode = 1;
	ObjectMapLoad();
}

static void enemya_802AEAB8(void)
{
	if (object->o_var != 1) object->o_mode = 2;
	object->o_angy += 0x800;
	ObjectMapLoad();
}

static void enemya_802AEB1C(void)
{
	objectlib_802A2320();
	objectlib_802A2348(78);
	if (object->o_move & (OM_BOUND|OM_DIVE)) object->o_mode = 3;
}

static void enemya_802AEB74(void)
{
	ObjectHide();
}

static OBJCALL *enemya_80330370[] =
{
	enemya_802AEA6C,
	enemya_802AEAB8,
	enemya_802AEB1C,
	enemya_802AEB74,
};

void enemya_802AEB9C(void)
{
	ObjectCallMode(enemya_80330370);
}

void enemya_802AEBC8(void)
{
	object->s.scale[1] = 0.4 + 0.3*(1.0+SIN(object->o_v0));
	object->o_v0 += 0x80;
}

void enemya_802AEC40(void)
{
	object->o_posy -= SIN(object->o_v0) * 0.58;
	object->o_v0 += 0x100;
}

void enemya_802AECA8(void)
{
	ObjCopyCoord(object, object->parent);
}

void enemya_802AECDC(void)
{
	if (object->o_code != 0)
	{
		if (object->o_timer == 0) object->o_posy -= 300;
		object->o_posy += SIN(object->o_v0) * 7;
	}
	else
	{
		object->o_posy -= SIN(object->o_v0) * 3;
	}
	object->o_v0 += 0x100;
}

extern OBJLANG obj_130010B8[];

void enemya_802AEDC0(void)
{
	object->o_targetdist = ObjCalcDist2D(object, mario_obj);
	object->o_posy -= 100;
	switch (object->o_mode)
	{
	case 0:
	case 1:
	case 2:
	case 3:
	case 4:
	case 5:
	case 6:
	case 7:
		ObjMakeHere(object, S_FLAME, obj_130010B8);
		object->o_mode++;
		break;
	case 8:
		break;
	case 9:
		object->o_mode++;
		break;
	}
}

void enemya_802AEEA4(void)
{
	ObjectSetScale(5);
	object->o_velf = 70*SIN(object->o_v0);
	object->o_v0 += 0x800;
}

void enemya_802AEF1C(void)
{
	float scale;
	int sp18;
	if (object->o_timer == 0)
	{
		object->o_shape = 10*RandF();
		ObjRandOff3D(object, 10);
	}
	if (object->o_code == 2)
	{
		scale = 2 + object->o_timer*(object->o_velf-   6)/100.0;
	}
	else
	{
		scale = 1 + object->o_timer*(object->o_velf-20.0)/100.0;
	}
	if (object->o_code == 3)
	{
		object->hit_h = 200;
		object->hit_offset = 150;
		object->o_vely = -28;
		ObjectCheckGroundY();
		if (object->o_posy-25*scale < object->o_ground_y)
		{
			object->o_vely = 0;
			object->o_posy = object->o_ground_y + 25*scale;
		}
		sp18 = object->parent->o_v7 / 1.2;
	}
	else
	{
		sp18 = object->parent->o_v7;
	}
	ObjectSetScale(scale);
	if (object->o_code == 4)
	{
		object->o_posy += object->o_velf;
	}
	else
	{
		ObjectProcMoveF();
	}
	if (object->o_timer > sp18) ObjKill(object);
	object->o_hit_result = 0;
}

extern OBJLANG obj_13001124[];

void enemya_802AF1E8(void)
{
	if (object->o_mode == 0)
	{
		if (stage_index != STAGE_BBH || ISTRUE(object_80361264))
		{
			if (object->o_targetdist < 2000) object->o_mode++;
		}
	}
	else if (object->o_mode == 1)
	{
		OBJECT *o;
		float speed;
		int sp34, shape = S_FLAME;
		UNUSED int i;
		speed = 95;
		if (object->o_code == 1) shape = S_BLUEFLAME;
		if (object->o_code == 2) speed = 50;
		sp34 = 1;
		if      (object->o_timer < 60) sp34 = 15;
		else if (object->o_timer < 74) sp34 = 75 - object->o_timer;
		else                           object->o_mode++;
		object->o_v7 = sp34;
		o = ObjMakeOff(object->o_code, 0, 0, 0, object, shape, obj_13001124);
		o->o_velf = speed;
		ObjectLevelSound(NA_SE6_04_80);
	}
	else if (object->o_timer > 60)
	{
		object->o_mode = 0;
	}
}

void enemya_802AF3FC(void)
{
	object->o_angy -= 0x80;
	object->o_roty = -0x80;
	enemya_802AF1E8();
}

void enemya_802AF448(void)
{
	object->flag |= OBJ_0400;
	objectlib_802A2320();
	switch (object->o_mode)
	{
	case 0:
		if (object->o_timer == 0)
		{
			object->o_shape = 10*RandF();
			object->o_vely = 30;
		}
		if (object->o_move & OM_BOUND) object->o_mode++;
		break;
	case 1:
		if (object->o_timer == 0)
		{
			object->o_vely = 50;
			object->o_velf = 30;
		}
		if (
			object->o_move & (OM_TOUCH|OM_S_WATER|OM_B_WATER) &&
			object->o_timer > 100
		) ObjKill(object);
		break;
	}
	if (object->o_timer > 300) ObjKill(object);
	objectlib_802A2348(78);
	object->o_hit_result = 0;
}

extern OBJLANG obj_13001184[];

void enemya_802AF5F8(void)
{
	OBJECT *o;
	float scale;
	switch (object->o_mode)
	{
	case 0:
		if (object->o_targetdist < 2000) object->o_mode = 1;
		break;
	case 1:
		o = ObjMakeHere(object, S_FLAME, obj_13001184);
		scale = 0.5*(10-object->o_timer);
		ObjSetScaleXYZ(o, scale, scale, scale);
		if (object->o_timer == 0) ObjHitON(o);
		if (object->o_timer > 10) object->o_mode++;
		break;
	case 2:
		if (object->o_timer == 0) object->o_v0 = 100*RandF();
		if (object->o_timer > 100+object->o_v0) object->o_mode = 0;
		break;
	}
}

static float enemya_80330380[] = {1.9, 2.4, 4.0, 4.8};

void enemya_802AF7C4(void)
{
	float sp2C, sp28, sp24, sp20;
	SHORT sp1E = 70;
	object->o_f0 = 10*object->o_timer;
	ObjectSetScale(object->o_f0);
	if (gfx_frame % 3) object->o_alpha--;
	if (object->o_timer > sp1E) object->o_alpha -= 5;
	if (object->o_alpha < 1) ObjKill(object);
	if (object->o_timer < sp1E)
	{
		if (!Player1IsJump())
		{
			sp2C = object->o_f0 * enemya_80330380[0];
			sp28 = object->o_f0 * enemya_80330380[1];
			sp24 = object->o_f0 * enemya_80330380[2];
			sp20 = object->o_f0 * enemya_80330380[3];
			if ((
				sp2C < object->o_targetdist && object->o_targetdist < sp28
			) || (
				sp24 < object->o_targetdist && object->o_targetdist < sp20
			)) mario_obj->o_hit_result |= HR_000010;
		}
	}
}

extern OBJLANG obj_13001254[];

void enemya_802AF9CC(void)
{
	ObjMakeHereScale(object, S_SMOKE, obj_13001254, object->s.scale[0]);
}

void enemya_802AFA0C(void)
{
	if (object->o_timer == 0)
	{
		object->o_velf = 0.5 + 2*RandF();
		object->o_angy = Rand();
		object->o_vely = 8;
		object->o_f0 = object->s.scale[0];
	}
	object->o_angy += object->o_roty;
	object->o_posy += object->o_vely;
}

void enemya_802AFAE4(void)
{
	if (object->o_timer == 0)
	{
		ObjectSetPosOff(mario_obj, 0, 0, -30);
		object->o_velf = 0.5 + 2*RandF();
		object->o_angy = mario_obj->o_angy+0x7000 + 0x2000*RandF();
		object->o_vely = 8;
	}
	object->o_angy += object->o_roty;
	object->o_posy += object->o_vely;
}

extern OBJLANG obj_13001214[];

void enemya_802AFBF8(void)
{
	ObjectSetScale(2);
	if (object->o_timer != 0)
	{
		if (object->o_timer & 1) ObjMakeHere(object, S_SMOKE, obj_13001214);
	}
	mario_obj->child = object;
	ObjSetRel(object, 40, -120, 0);
	if (!(mario_obj->o_v0 & 0x800))
	{
		object->parent->o_effect &= ~0x800;
		ObjKill(object);
		mario_obj->child = NULL;
	}
}

void enemya_802AFCE4(void)
{
	UNUSED FVEC v;
	UNUSED float water_y = BGCheckWater(object->o_posx, object->o_posz);
}

static HITINFO enemya_80330390 =
{
	/*type   */	HIT_BOUNCE,
	/*offset */	0,
	/*ap     */	2,
	/*hp     */	1,
	/*ncoin  */	3,
	/*hit r,h*/	90, 80,
	/*dmg r,h*/	80, 70,
};

void enemya_802AFD1C(void)
{
	object->flag |= OBJ_0400;
	if (objectlib_802A4360(&enemya_80330390, NA_SE5_24, 0)) ObjectInitMode(1);
	objectlib_802A2320();
	switch (object->o_mode)
	{
	case 0:
		enemya_802A98C4(&object->o_velf, 4, 1);
		if (ObjectDistMarioToSave() > 1000)
		{
			object->o_targetang = ObjectAngToSave();
		}
		else if (object->o_targetdist > 300)
		{
			object->o_targetang = ObjCalcAngY(object, mario_obj);
		}
		ObjectTurn(object->o_targetang, 0x400);
		break;
	case 1:
		object->o_flag &= ~OF_SETSHAPEANGY;
		object->o_velf = -10;
		if (object->o_timer > 20)
		{
			object->o_mode = 0;
			object->o_hit_result = 0;
			object->o_flag |= OF_SETSHAPEANGY;
		}
		break;
	}
	objectlib_802A2348(-60);
}

void enemya_802AFEE8(void)
{
	if (object->parent->o_mode == 3) ObjKill(object);
}

void enemya_802AFF30(void)
{
	switch (object->o_mode)
	{
	case 0:
		if (mario_obj->movebg == object) object->o_mode++;
		break;
	case 1:
		ObjectLevelSound(NA_SE4_02);
		if (object->o_timer > 140) object->o_mode++;
		else object->o_posy += 5;
		break;
	case 2:
		if (object->o_timer > 60) object->o_mode++;
		break;
	case 3:
		ObjectLevelSound(NA_SE4_02);
		if (object->o_timer > 140) object->o_mode = 0;
		else object->o_posy -= 5;
		break;
	}
	if (object->parent->o_mode == 3) ObjKill(object);
}

void enemya_802B00E4(void)
{
	int sp24 = object->o_f7 / object->o_f6;
	switch (object->o_mode)
	{
	case 0:
		if (object->o_timer > sp24) object->o_mode++;
		object->o_velf = -object->o_f6;
		break;
	case 1:
		if (object->o_timer > sp24) object->o_mode = 0;
		object->o_velf = object->o_f6;
		break;
	}
	ObjectCalcVelF();
	object->o_posx += object->o_velx;
	object->o_posz += object->o_velz;
	if (object->parent->o_mode == 3) ObjKill(object);
}

static void enemya_802B0244(SHORT shape, OBJLANG *script)
{
	short angy;
	OBJECT *o;
	o = ObjMakeHere(object, shape, script);
	angy = object->o_v0*object->o_v2 + object->o_v1;
	o->o_angy = angy;
	o->o_posx += object->o_f3 * SIN(angy);
	o->o_posy += 100*object->o_v0;
	o->o_posz += object->o_f3 * COS(angy);
	o->o_f7 = object->o_f4;
	o->o_f6 = object->o_f5;
	object->o_v0++;
}

extern OBJLANG obj_13001318[];
extern OBJLANG obj_13001340[];
extern OBJLANG obj_13001368[];

static void enemya_802B039C(void)
{
	UNUSED int n = 8;
	object->o_v0 = 0;
	object->o_v1 = 0;
	object->o_v2 = 0x2000;
	object->o_f3 = 704;
	object->o_f4 = 380;
	object->o_f5 = 3;
	enemya_802B0244(45, obj_13001368); /* T:shape */
	enemya_802B0244(45, obj_13001318); /* T:shape */
	enemya_802B0244(45, obj_13001368); /* T:shape */
	enemya_802B0244(45, obj_13001318); /* T:shape */
	enemya_802B0244(45, obj_13001368); /* T:shape */
	enemya_802B0244(45, obj_13001318); /* T:shape */
	enemya_802B0244(45, obj_13001368); /* T:shape */
	enemya_802B0244(47, obj_13001340); /* T:shape */
}

void enemya_802B04B4(void)
{
	float mario_y = mario_obj->o_posy;
	object->o_targetdist = ObjCalcDist3D(object, mario_obj);
	switch (object->o_mode)
	{
	case 0:
		if (mario_y > object->o_savey-1000) object->o_mode++;
		break;
	case 1:
		enemya_802B039C();
		object->o_mode++;
		break;
	case 2:
		if (mario_y < object->o_savey-1000) object->o_mode++;
		break;
	case 3:
		object->o_mode = 0;
		break;
	}
}

void enemya_802B0614(void)
{
	ObjectCheckGroundY();
	if (object->o_timer == 0)
	{
		object->o_rotx = 0x1000 * (RandF()-0.5);
		object->o_rotz = 0x1000 * (RandF()-0.5);
		object->o_v1 = 4;
		object->o_v2 = 0x600 + 0x400*RandF();
	}
	if (object->o_posy < object->o_ground_y) ObjKill(object);
	if (object->o_ground_y < -11000) ObjKill(object);
	if (object->o_timer > 100) ObjKill(object);
	if (obj_prevcount > 212) ObjKill(object);
	object->o_shapeangx += object->o_rotx;
	object->o_shapeangz += object->o_rotz;
	object->o_vely += -3;
	if (object->o_vely < -8) object->o_vely = -8;
	if (object->o_velf > 0) object->o_velf -= 0.3;
	else                    object->o_velf = 0;
	object->o_posx += SIN(object->o_angy) * SIN(object->o_v0) * object->o_v1;
	object->o_posz += COS(object->o_angy) * SIN(object->o_v0) * object->o_v1;
	object->o_v0 += object->o_v2;
	object->o_posy += object->o_vely;
}

extern OBJLANG obj_130013A8[];
extern OBJLANG obj_130013C4[];

void enemya_802B0974(void)
{
	OBJECT *o;
	UNUSED int i;
	int snow;
	float scale;
	UNUSED int n;
	mario_obj->o_effect &= ~0x2000;
	if (stage_index == STAGE_CCM || stage_index == STAGE_SL)    snow = TRUE;
	else                                                        snow = FALSE;
	if (snow)
	{
		if (RandF() < 0.5)
		{
			o = ObjMakeHere(object, S_SNOW, obj_130013A8);
			scale = RandF();
			ObjSetScaleXYZ(o, scale, scale, scale);
			o->o_angy = Rand();
			o->o_velf = 5*RandF();
			o->o_vely = 15*RandF();
		}
	}
	else
	{
		if (RandF() < 0.3)
		{
			o = ObjMakeHere(object, S_LEAF, obj_130013C4);
			scale = 3*RandF();
			ObjSetScaleXYZ(o, scale, scale, scale);
			o->o_angy = Rand();
			o->o_velf = 5 + 5*RandF();
			o->o_vely = 15*RandF();
			o->o_shapeangx = Rand();
			o->o_shapeangz = Rand();
			o->o_shapeangy = Rand();
		}
	}
}

static int enemya_802B0B9C(unsigned short angy, int a1)
{
	object->o_angy = angy;
	if (object->o_timer > a1)   return TRUE;
	else                        return FALSE;
}

void enemya_802B0BEC(void)
{
	object->o_velf = 10;
	switch (object->o_mode)
	{
	case 0: object->o_mode = 1 + (object->o_code & 3); break;
	case 1: if (enemya_802B0B9C(0x0000, 60)) object->o_mode++; break;
	case 2: if (enemya_802B0B9C(0x4000, 60)) object->o_mode++; break;
	case 3: if (enemya_802B0B9C(0x8000, 60)) object->o_mode++; break;
	case 4: if (enemya_802B0B9C(0xC000, 60)) object->o_mode = 1; break;
	default: break;
	}
	ObjectProcMoveF();
	ObjectMapLoad();
}

void enemya_802B0D48(void)
{
	if (object->o_timer == 0)
	{
		object->o_vely = 5 + 10*RandF();
		object->o_velf = 5 + 10*RandF();
		object->o_angy = Rand();
	}
	ObjectProcMoveF();
}

extern OBJLANG obj_13001448[];

void enemya_802B0DF0(void)
{
	OBJECT *parent = object->parent;
	float scale = 0;
	int i;
	int frame = parent->s.skel.frame;
	int end = parent->s.skel.anime->frame - 2;
	UNUSED int n;
	ObjectSetPosOff(parent, 0, 72, 180);
	switch (object->o_mode)
	{
	case 0:
		ObjectClrActive();
		scale = 0;
		if (parent->o_mode == 1) object->o_mode++;
		break;
	case 1:
		if (parent->o_targetdist < parent->o_shapedist)
		{
			ObjectSetActive();
			if (parent->o_mode == 1)
			{
				float h1 = end/2.0F-4;
				float h2 = end/2.0F+4;
				if (frame < h1)
				{
					scale = 1.0 + 4*COS((frame             )/h1*0x4000);
				}
				else if (frame > h2)
				{
					/* meant h1 */
					scale = 1.0 + 4*SIN((frame-(end/2.0F+4))/h2*0x4000);
				}
				else
				{
					scale = 1.0;
				}
			}
			else
			{
				object->o_mode++;
			}
		}
		else
		{
			ObjectClrActive();
		}
		break;
	case 2:
		ObjectClrActive();
		scale = 0;
		for (i = 0; i < 15; i++)
		{
			ObjMakeEffect(0, 1, object, S_BUBBLE_A, obj_13001448);
		}
		object->o_mode = 0;
		scale = 1;
		break;
	}
	ObjectSetScale(scale);
}

void enemya_802B1278(void)
{
	UNUSED int i;
	switch (object->o_mode)
	{
	case 0:
		ObjectSetShape(S_PURPLESW);
		ObjectSetScale(1.5F);
		if (mario_obj->movebg == object && !(player_data[0].state & PF_SWIM))
		{
			if (ObjCalcDist2D(object, mario_obj) < 127.5) object->o_mode = 1;
		}
		break;
	case 1:
		ObjectScaleTime(2, 3, 1.5F, 0.2F);
		if (object->o_timer == 3)
		{
			ObjectPlaySound(NA_SE8_3E);
			object->o_mode = 2;
			objectlib_802A50FC(1);
#ifdef MOTOR
			motor_8024C834(5, 80);
#endif
		}
		break;
	case 2:
		if (object->o_code != 0)
		{
			if (object->o_code == 1 && mario_obj->movebg != object)
			{
				object->o_mode++;
			}
			else
			{
				if (object->o_timer < 360)  Na_FixSePlay(NA_SE8_54);
				else                        Na_FixSePlay(NA_SE8_55);
				if (object->o_timer > 400) object->o_mode = 4;
			}
		}
		break;
	case 3:
		ObjectScaleTime(2, 3, 0.2F, 1.5F);
		if (object->o_timer == 3) object->o_mode = 0;
		break;
	case 4:
		if (!ObjectIsMarioBG()) object->o_mode = 3;
		break;
	}
}

int enemya_802B14F4(float a0, float a1)
{
	BGFACE *ground;
	float x, y, z;
	x = object->o_posx + a1*SIN(object->o_angy);
	z = object->o_posz + a1*COS(object->o_angy);
	y = BGCheckGround(x, object->o_posy, z, &ground);
	if (fabsf(y-object->o_posy) < a0)   return TRUE;
	else                                return FALSE;
}

static HITINFO enemya_803303A0 =
{
	/*type   */	0,
	/*offset */	0,
	/*ap     */	0,
	/*hp     */	1,
	/*ncoin  */	0,
	/*hit r,h*/	220, 300,
	/*dmg r,h*/	220, 300,
};

void enemya_802B15E8(void)
{
	UNUSED SHORT i;
	ObjSetHitInfo(object, &enemya_803303A0);
	object->o_velf = 0;
	if (ObjIsObjHit(object, mario_obj) && player_data[0].flag & PL_80000000)
	{
		SHORT angy = ObjCalcAngY(object, mario_obj);
		if (DeltaAng(angy, mario_obj->o_angy) > 0x4000)
		{
			object->o_angy = (short)((mario_obj->o_angy+0x2000) & 0xC000);
			if (enemya_802B14F4(8, 150))
			{
				object->o_velf = 4;
				ObjectLevelSound(NA_SE4_17);
			}
		}
	}
	ObjectProcMoveF();
}

static void enemya_802B1714(void)
{
	object->o_v0 = 0;
	object->o_shape = 1;
	switch (object->o_code)
	{
	case 0: object->o_ncoin = 0; break;
	case 1: object->o_ncoin = 3; break;
	case 2: object->o_ncoin = 5; break;
	case 3: ObjectSetScale(1.5F); break;
	}
}

static HITINFO enemya_803303B0 =
{
	/*type   */	HIT_ITEMBOX,
	/*offset */	20,
	/*ap     */	0,
	/*hp     */	1,
	/*ncoin  */	0,
	/*hit r,h*/	150, 200,
	/*dmg r,h*/	150, 200,
};

extern OBJLANG obj_130014AC[];

static void enemya_802B17F4(void)
{
	OBJECT *o;
	ObjSetHitInfo(object, &enemya_803303B0);
	ObjectSetShape(S_CRATE);
	if (object->o_mode == 0)
	{
		ObjectClrActive();
		ObjectHitOFF();
		if (object->o_timer == 0) enemya_802B1714();
		if (!object->o_p0) object->o_p0 = ObjectFindObj(obj_130014AC);
		if ((o = object->o_p0))
		{
			if (o->o_mode == 2)
			{
				object->o_mode++;
				ObjectSetActive();
				ObjectShow();
			}
		}
	}
	else if (object->o_mode == 1)
	{
		ObjectHitON();
		if (ObjectFlash(360, 20)) object->o_mode = 0;
		if (objectlib_802A51AC())
		{
			objectlib_802A37AC();
			enemya_802AE0CC(30, S_SHARD, 3, 4);
			object->o_mode++;
			ObjectPlaySound(NA_SE3_41);
		}
		ObjectMapLoad();
	}
	else
	{
		ObjectHitOFF();
		ObjectClrActive();
		object->o_hit_result = 0;
		if ((o = object->o_p0))
		{
			if (o->o_mode == 0) object->o_mode = 0;
		}
	}
}

extern MAP map_07018528[];

static void enemya_802B19D8(void)
{
	OBJECT *o;
	ObjSetMap(object, map_07018528);
	if (object->o_mode == 0)
	{
		ObjectClrActive();
		ObjectHitOFF();
		if (!object->o_p0) object->o_p0 = ObjectFindObj(obj_130014AC);
		if ((o = object->o_p0))
		{
			if (o->o_mode == 2)
			{
				object->o_mode++;
				ObjectSetActive();
				ObjectShow();
			}
		}
	}
	else
	{
		ObjectHitON();
		if (ObjectFlash(360, 20)) object->o_mode = 0;
		ObjectMapLoad();
	}
}

void enemya_802B1AE0(void)
{
	if (object->o_code == 0)    enemya_802B17F4();
	else                        enemya_802B19D8();
}

void enemya_802B1B2C(void)
{
	ObjSetHitInfo(object, &enemya_803303B0);
	ObjectSetShape(S_CRATE);
	if (object->o_timer == 0) enemya_802B1714();
	if (objectlib_802A51AC())
	{
		objectlib_802A4440(46, 1);
		ObjectMakeSound(NA_SE3_41);
	}
}

void *CtrlMarioCopyParentPos(int code, UNUSED SHAPE *shape, void *data)
{
	if (code == SC_DRAW)
	{
		FMTX m;
		OBJECT *obj = (OBJECT *)draw_object;
		if (obj == mario_obj && obj->child)
		{
			FMtxInvCatAffine(m, data, *draw_camera->m);
			ObjSetPosRelXFM(m, obj->child);
			ObjSetShapePos(obj->child);
		}
	}
	return NULL;
}

void enemya_802B1C54(void)
{
	object->o_relx = 200;
	object->o_rely = -50;
	object->o_relz = 0;
	object->o_angy = object->parent->o_angy;
	switch (object->parent->o_var)
	{
	case 0:
		break;
	case 1:
		break;
	case 2:
		ObjectPlaySound(NA_SE5_5D);
		mario_obj->o_hit_result |= HR_000004;
		player_data[0].speed = -45;
		player_data[0].vel[1] = 95;
		object->parent->o_var = 0;
		break;
	}
}

static short enemya_803303C0[][2] =
{
	{30, 0},
	{42, 1},
	{52, 0},
	{64, 1},
	{74, 0},
	{86, 1},
	{96, 0},
	{108, 1},
	{118, 0},
	{-1, 0},
};

static void enemya_802B1D7C(void)
{
	int i = 0;
	object->o_velf = 0;
	ObjectAnimeHold();
	for (;;)
	{
		if (enemya_803303C0[i][0] == -1)
		{
			object->o_mode = 2;
			break;
		}
		if (object->o_timer < enemya_803303C0[i][0])
		{
			ObjectSetAnimeV(2, enemya_803303C0[i][1]);
			break;
		}
		i++;
	}
}

static void enemya_802B1E6C(void)
{
	UNUSED int i;
	short rot;
	if (ObjectDistMarioToSave() > 1000) object->o_targetang = ObjectAngToSave();
	if (object->o_timer > 150)
	{
		object->o_f0 = (302-object->o_timer) / 152.0F;
		if (object->o_f0 < 0.1)
		{
			object->o_f0 = 0.1;
			object->o_mode = 1;
		}
	}
	else
	{
		object->o_f0 = 1;
	}
	ObjectSetAnimeV(0, object->o_f0);
	object->o_velf = 10*object->o_f0;
	rot = 0x400*object->o_f0;
	object->o_angy = ApproachAng(object->o_angy, object->o_targetang, rot);
}

static void enemya_802B1FF4(void)
{
	object->o_velf = 0;
	if (object->o_timer == 0) object->o_var = 2;
	if (object->o_timer == 1)
	{
		ObjectSetAnimeV(1, 1);
		object->hit_count = 20;
	}
	if (objectlib_8029FF04()) object->o_mode = 1;
}

static void enemya_802B20A0(void)
{
	ObjectSavePos();
	if (
		BGCheckWater(object->o_posx, object->o_posz) < object->o_posy &&
		object->o_targetdist < 4000
	)
	{
		ObjectHitON();
		ObjectShow();
		object->o_mode = 1;
	}
	else
	{
		ObjectHitOFF();
		ObjectHide();
	}
}

static OBJCALL *enemya_803303E8[] =
{
	enemya_802B20A0,
	enemya_802B1D7C,
	enemya_802B1E6C,
	enemya_802B1FF4,
};

static void enemya_802B2154(void)
{
	objectlib_802A2320();
	ObjectCallMode(enemya_803303E8);
	objectlib_802A2348(-78);
	if (object->o_move & (OM_DIVE|OM_S_WATER|OM_U_WATER|OM_B_WATER))
	{
		object->o_shapeoff = -15;
	}
	else
	{
		object->o_shapeoff = 0;
	}
	if (object->o_velf > 3) ObjectLevelSound(NA_SE6_06);
	if (
		object->o_mode != 0 &&
		object->o_move & (OM_DIVE|OM_S_WATER|OM_U_WATER|OM_B_WATER)
	) object->o_mode = 0;
	if (object->o_hit_result & HR_000800)
	{
		object->o_hit_result = 0;
		object->o_var = 1;
		object->o_mode = 3;
	}
}

void enemya_802B2278(void)
{
	ObjectSetScale(2);
	switch (object->o_action)
	{
	case OA_0: enemya_802B2154(); break;
	case OA_1: objectlib_802A01D8(0, 0); break;
	case OA_2: objectlib_802A0474(); break;
	case OA_3: objectlib_802A0474(); break;
	}
	object->o_hit_result = 0;
}

void enemya_802B2340(void)
{
	if (object_8036125C & 1)
	{
		object->o_posy += 100;
		object->o_posx = 2780;
		object->o_posz = 4666;
		enemyb_802F2B88(2500, -4350, 5750);
		ObjKill(object);
	}
}

void enemya_802B23E0(void)
{
	ObjectSetScale(1.02F);
	if (object->o_mode == 0)
	{
		if (objectlib_802A3754())
		{
			objectlib_802A37AC();
			enemya_802AE0CC(20, 56, 3, 0); /* T:shape */
			object->o_mode++;
		}
	}
	else
	{
		if (object->o_timer >= 8) ObjKill(object);
	}
	ObjectMapLoad();
}

void enemya_802B2494(void)
{
	float scale, dist;
	ObjCopyCoord(object, object->parent);
	ObjCopyShapeOff(object, object->parent);
	object->o_posy -= 75;
	if ((dist = object->o_posy-object->o_savey) >= 0)
	{
		scale = 1 + dist/10.0;
	}
	else
	{
		dist = -dist;
		scale = 1 - dist/500.0;
	}
	ObjSetScaleXYZ(object, 1, scale, 1);
}

extern OBJLANG obj_13001634[];
extern OBJLANG obj_13002A48[];

void enemya_802B25AC(void)
{
	OBJECT *o;
	ObjectSetShape(181); /* T:shape */
	if (object->o_timer == 0)
	{
		o = ObjMakeHere(object, 182, obj_13001634); /* T:shape */
		o->o_posy -= 75;
		o = ObjMakeHere(object, 183, obj_13002A48); /* T:shape */
		o->o_posy -= 150;
	}
	if (mario_obj->movebg == object)
	{
		object->o_v7 = 1;
	}
	else
	{
		object->o_v7 = 0;
		object->o_posy = object->o_savey;
	}
	TrampolineProc();
}

static void enemya_802B26A4(void)
{
	if (object->o_phase == 0)
	{
		if (object->o_v1-- < 0) object->o_phase++;
		if (object->o_timer > object->o_v0)
		{
			object->o_vely = 15 + 5*RandF();
			object->o_phase++;
		}
	}
	else
	{
		if (object->o_move & OM_TOUCH)
		{
			object->o_phase = 0;
			object->o_v1 = 30 + 60*RandF();
		}
	}
}

static void enemya_802B27D8(void)
{
	if (object->o_move & (
		OM_BOUND|OM_DIVE|OM_S_WATER|OM_U_WATER|OM_B_WATER|OM_0200
	))
	{
		ObjKill(object);
		objectlib_802A37AC();
	}
}

static HITINFO enemya_803303F8 =
{
	/*type   */	HIT_TAKE,
	/*offset */	20,
	/*ap     */	0,
	/*hp     */	1,
	/*ncoin  */	5,
	/*hit r,h*/	150, 250,
	/*dmg r,h*/	150, 250,
};

static OBJCALL *enemya_80330408[] =
{
	enemya_802B26A4,
	enemya_802B27D8,
};

static void enemya_802B2824(void)
{
	ObjectSetShape(S_BLOCK);
	ObjectSetScale(0.5F);
	ObjSetHitInfo(object, &enemya_803303F8);
	objectlib_802A2320();
	objectlib_802A2348(78);
	ObjectCallMode(enemya_80330408);
}

void enemya_802B288C(void)
{
	switch (object->o_action)
	{
	case OA_0:
		enemya_802B2824();
		break;
	case OA_1:
		ObjCopyPos(object, mario_obj);
		ObjectSetShape(S_CRATE);
		objectlib_802A01D8(-1, 0);
		break;
	case OA_2:
		objectlib_802A0380(40, 20, 1);
		break;
	case OA_3:
		objectlib_802A0474();
		object->o_mode = 1;
		break;
	}
	if (object->o_hit_result & HR_400000)
	{
		ObjectMakeSound(NA_SE3_41);
		objectlib_802A4440(46, 1);
	}
	object->o_hit_result = 0;
}

static HITINFO enemya_80330410 =
{
	/*type   */	HIT_CAGE,
	/*offset */	0,
	/*ap     */	0,
	/*hp     */	0,
	/*ncoin  */	0,
	/*hit r,h*/	120, 300,
	/*dmg r,h*/	0, 0,
};

extern OBJLANG obj_13002AF0[];

void enemya_802B29B8(void)
{
	UNUSED int i;
	ObjSetHitInfo(object, &enemya_80330410);
	switch (object->o_mode)
	{
	case 0:
		ObjectHitOFF();
		ObjectSetScale(1);
		if (object->parent->o_var)
		{
			object->o_mode++;
			object->o_vely = 60;
			Na_Solution();
		}
		else
		{
			ObjCopyCoord(object, object->parent);
		}
		break;
	case 1:
		object->o_shapeangx = 0;
		object->o_shapeangz = 0;
		objectlib_802A2320();
		objectlib_802A2348(-78);
		ObjMakeHere(object, S_NULL, obj_13002AF0);
		if (object->o_move & OM_BOUND) ObjectPlaySound(NA_SE3_5E);
		if (object->o_move & (OM_TOUCH|OM_S_WATER|OM_B_WATER)) object->o_mode++;
		break;
	case 2:
		ObjectHitON();
		ObjectSetScale(1);
		if (ObjIsObjHit(object, mario_obj)) object->o_mode++;
		break;
	case 3:
		if (object->o_timer > 100) object->o_mode++;
		break;
	case 4:
		break;
	}
}

extern OBJLANG obj_13002AF0[];

static void enemya_802B2BC8(int count, int a1, int a2, int rot)
{
	static short enemya_80361280;
	int i;
	short ang = 0x10000 / count;
	for (i = 0; i < count; i++) ObjMakeOff(
		0,
		a1*SIN(enemya_80361280 + i*ang),
		a2*(1+i),
		a1*COS(enemya_80361280 + i*ang),
		object, S_NULL, obj_13002AF0
	);
	enemya_80361280 += 0x100*rot;
}

extern OBJLANG obj_13000A14[];

void enemya_802B2D10(void)
{
	object->o_shapeangz += 0x200;
	object->o_shapeangy += 0x200;
	if (ObjIsObjHit(object, mario_obj))
	{
		object->parent->o_var = 1;
		ObjKill(object);
		ObjMakeHere(object, S_SPARKLE, obj_13000A14);
	}
}

static void enemya_802B2DAC(void)
{
	objectlib_802A2320();
	objectlib_802A2348(78);
	if (object->o_shapeoff < 26) object->o_shapeoff += 2;
	if (object->o_shapeangz & 0xFFFF)
	{
		object->o_shapeangz &= 0xF800;
		object->o_shapeangz += 0x800;
	}
	if (object->o_move & OM_TOUCH)
	{
		object->o_velx = 0;
		object->o_velz = 0;
	}
	object->o_shapeangy += 0x800;
	if (object->o_timer > 90 || object->o_move & OM_BOUND)
	{
		ObjectHitON();
		if (ObjIsObjHit(object, mario_obj))
		{
			object->parent->o_hit_result = HR_000001;
			ObjKill(object);
			ObjMakeHere(object, S_SPARKLE, obj_13000A14);
		}
	}
}

static void enemya_802B2F34(void)
{
	SHORT angy;
	float speed;
	OBJECT *parent = object->parent;
	ObjCopyPos(object, parent);
	if (object->o_timer == 0)
	{
		object->parent = parent->parent;
		object->o_mode = 2;
		angy = mario_obj->o_angy;
		speed = 3;
		object->o_velx = speed * SIN(angy);
		object->o_velz = speed * COS(angy);
		object->o_vely = 40;
	}
	object->o_shapeangy += 0x200;
	object->o_shapeangz += 0x200;
}

static void enemya_802B3064(void)
{
	OBJECT *parent = object->parent;
	ObjCopyPos(object, parent);
	object->o_posy += 40;
	if (parent->o_var != 0) object->o_mode = 1;
	object->o_shapeangz += 0x200;
	object->o_shapeangy += 0x200;
}

static OBJCALL *enemya_80330420[] =
{
	enemya_802B3064,
	enemya_802B2F34,
	enemya_802B2DAC,
};

void enemya_802B3108(void)
{
	ObjectCallMode(enemya_80330420);
}

int enemya_802B3134(float *a0, float *a1, float vely, float gravity)
{
	float dx = a0[0] - a1[0];
	float dz = a0[2] - a1[2];
	float dist = DIST2(dx, dz);
	int sp18;
	object->o_angy = ATAN2(dz, dx);
	object->o_vely = vely;
	object->o_gravity = gravity;
	sp18 = -2/object->o_gravity*vely - 1;
	object->o_velf = dist/sp18;
	return sp18;
}

static void enemya_802B3250(void)
{
	object->o_gravity = 0;
	object->o_vely = 0;
	object->o_velf = 0;
}

void enemya_802B329C(void)
{
	UNUSED int i;
	FVEC sp28;
	sp28[0] = sp28[1] = sp28[2] = 0;
	if (object->o_mode == 0)
	{
		if (object->o_timer == 0)
		{
			ObjSetAng(object, 0, 0, 0);
			object->o_roty = 0x400;
			ObjectPlaySound(NA_SE8_57);
		}
		if (object->o_timer > 70) object->o_mode++;
		enemya_802B2BC8(3, 200, 80, -60);
	}
	else if (object->o_mode == 1)
	{
		if (object->o_timer == 0)
		{
			ObjectPlaySound(NA_SE3_73);
			camera_8029000C(173, object);
			object->o_v5 = enemya_802B3134(sp28, &object->o_posx, 80, -2);
		}
		ObjectProcMoveF();
		if (object->o_phase == 0)
		{
			if (object->o_posy < object->o_savey)
			{
				object->o_posy = object->o_savey;
				object->o_vely = 60;
				object->o_velf = 0;
				object->o_phase++;
				ObjectPlaySound(NA_SE3_74);
			}
		}
		else
		{
			if (object->o_vely < 0 && object->o_posy < object->o_savey+200)
			{
				object->o_posy = object->o_savey+200;
				enemya_802B3250();
				camera_8033CBC8 = 1;
				pldemo_80257640(0);
				object->o_mode++;
				object->o_hit_result = 0;
				ObjectPlaySound(NA_SE3_74);
			}
		}
		enemya_802B2BC8(3, 200, 80, -60);
	}
	else
	{
		ObjectHitON();
		if (object->o_hit_result & HR_008000)
		{
			ObjKill(object);
			object->o_hit_result = 0;
		}
	}
	if (object->o_roty > 0x400) object->o_roty -= 0x100;
	object->o_shapeangy += object->o_roty;
	ObjectSetScale(2);
	object->o_shapeoff = 110;
}

static HITINFO enemya_8033042C =
{
	/*type   */	HIT_STAR,
	/*offset */	0,
	/*ap     */	0,
	/*hp     */	0,
	/*ncoin  */	0,
	/*hit r,h*/	160, 100,
	/*dmg r,h*/	160, 100,
};

void enemya_802B3600(void)
{
	ObjectSetScale(0.5F);
	if (object->o_roty > 0x400) object->o_roty -= 0x100;
	object->o_shapeangy += object->o_roty;
	object->o_shapeangz = -0x4000;
	object->o_shapeoff = 165;
	if (object->o_mode == 0)
	{
		if (object->o_timer == 0) object->o_vely = 70;
		enemya_802B2BC8(3, 200, 80, -60);
		ObjMakeHere(object, S_NULL, obj_13002AF0);
		objectlib_802A2320();
		objectlib_802A2348(78);
		if (object->o_move & OM_TOUCH) object->o_mode++;
		else if (object->o_move & OM_BOUND) ObjectPlaySound(NA_SE3_37);
	}
	else
	{
		ObjSetHitInfo(object, &enemya_8033042C);
		if (object->o_hit_result & HR_008000)
		{
			ObjDestroy(object);
			object->o_hit_result = 0;
		}
	}
}

void enemya_802B37B8(void)
{
	ObjectSetScale(2.0 + 2*RandF());
}

void enemya_802B3810(void)
{
	object->o_v1 = object->o_angy;
}

static void enemya_802B3830(void)
{
	ObjectHitON();
	object->o_velf = 0;
	object->o_angy = object->o_v1;
	object->o_shapeangx = 0;
	object->o_shapeangz = 0;
	object->o_move = 0;
	ObjectSavePos();
	object->o_mode = 1;
}

static void enemya_802B38B8(void)
{
	SHORT dang = DeltaAng(object->o_targetang, object->o_angy);
	if (dang < 0x2000)
	{
		if (400 < object->o_targetdist && object->o_targetdist < 1500)
		{
			object->o_mode = 2;
		}
	}
}

extern OBJLANG obj_130017F4[];

static void enemya_802B394C(void)
{
	if (object->o_timer < 40)
	{
		object->o_velf = 3;
	}
	else if (object->o_timer < 50)
	{
		if (object->o_timer % 2)    object->o_velf = 3;
		else                        object->o_velf = -3;
	}
	else
	{
		if (object->o_timer > 70) objectlib_802A2320();
		ObjMakeHere(object, S_DUST, obj_130017F4);
		object->o_velf = 30;
		if (object->o_targetdist > 300) ObjectTurn(object->o_targetang, 0x100);
		if (object->o_timer == 50)
		{
			ObjectPlaySound(NA_SE5_1A);
			objectlib_802A50FC(1);
		}
		if (object->o_timer > 150 || object->o_move & OM_0200)
		{
			object->o_mode = 3;
			objectlib_802A37AC();
		}
	}
}

static void enemya_802B3B08(void)
{
	object->o_mode = 0;
}

static void enemya_802B3B24(void)
{
	if (object->o_timer == 0)
	{
		object->o_velf = -30;
		ObjectHitOFF();
	}
	object->o_shapeangx += 0x1000;
	object->o_shapeangz += 0x1000;
	object->o_posy += 20;
	if (object->o_timer > 90) object->o_mode = 0;
}

static OBJCALL *enemya_8033043C[] =
{
	enemya_802B3830,
	enemya_802B38B8,
	enemya_802B394C,
	enemya_802B3B08,
	enemya_802B3B24,
};

void enemya_802B3BE0(void)
{
	ObjectCallMode(enemya_8033043C);
	if (objectlib_802A54D8()) object->o_mode = 4;
}

static void enemya_802B3C2C(void)
{
	OBJECT *parent = object->parent;
	ObjectHitON();
	ObjectSetScale(1);
	if (parent->o_mode == 19)
	{
		parent->o_hit_timer = -1;
	}
	else
	{
		if (ObjIsObjHit(object, mario_obj))
		{
			parent->o_hit_timer = 0;
			object->o_mode = 2;
		}
		else
		{
			parent->o_hit_timer = -1;
		}
	}
}

static void enemya_802B3CDC(void)
{
	if (object->o_timer > 30) object->o_mode = 0;
}

static void enemya_802B3D10(void)
{
	if (object->parent->o_mode == 19)
	{
		object->parent->o_hit_timer = -1;
		object->o_mode = 0;
	}
	ObjectHitOFF();
}

static OBJCALL *enemya_80330450[] =
{
	enemya_802B3C2C,
	enemya_802B3CDC,
	enemya_802B3D10,
};

void enemya_802B3D74(void)
{
	ObjectCallMode(enemya_80330450);
	object->o_relx = 90;
	if (object->parent->o_mode == 4) object->parent->o_hit_timer = -1;
	object->o_hit_result = 0;
}

extern short _0605784C[];
extern OBJLANG obj_13001A74[];

void enemya_802B3DF4(void)
{
	OBJECT *parent = object->parent;
	int frame;
	float x, z;
	float c = COS(parent->o_angy);
	float s = SIN(parent->o_angy);
	short *sp1C = SegmentToVirtual(_0605784C);
	if (parent->o_anime == 6)
	{
		frame = (float)parent->s.skel.frame+1;
		if (frame == parent->s.skel.anime->frame) frame = 0;
		if (frame >= 46 && frame < 85)
		{
			ObjectLevelSound(NA_SE6_00);
			x = sp1C[5*frame+0];
			z = sp1C[5*frame+2];
			object->o_posx = parent->o_posx + (z*s + x*c);
			object->o_posy = parent->o_posy + sp1C[5*frame+1];
			object->o_posz = parent->o_posz + (z*c - x*s);
			object->o_angx = sp1C[5*frame+4] + 0xC00;
			object->o_angy = sp1C[5*frame+3] + (short)parent->o_angy;
			if (!(frame & 1)) ObjMakeHere(object, S_FLAME, obj_13001A74);
		}
	}
}

void enemya_802B4080(void)
{
	ObjCopyCoord(object, object->parent);
	if (object->parent->o_mode == 4)
	{
#if REVISION >= 199609
		if (object->parent->o_phase == 11)  object->o_hit_type = 0;
		else                                object->o_hit_type = HIT_MESSAGE;
#else
		object->o_hit_type = HIT_MESSAGE;
#endif
	}
	else
	{
		object->o_hit_type = HIT_DAMAGE;
		if (object->parent->o_alpha < 100)  ObjectHitOFF();
		else                                ObjectHitON();
	}
	if (object->parent->o_action != OA_0) ObjectHitOFF();
	object->o_hit_result = 0;
}

extern OBJLANG obj_130011D0[];

static int enemya_802B4184(void)
{
	if (object->o_code == 2)
	{
		OBJECT *o = ObjMakeHere(object, 104, obj_130011D0); /* T:shape */
		o->o_posy = object->o_ground_y;
		return TRUE;
	}
	return FALSE;
}

static void enemya_802B41FC(int *a0)
{
	if (object->o_move & OM_BOUND)
	{
		(*a0)++;
		if (*a0 < 4)
		{
			objectlib_802A1930(object, 8);
			enemya_802AAE8C(0, 0, 60);
			ObjectPlaySound(NA_SE5_03);
		}
	}
}

static int enemya_802B4288(void)
{
	ObjectSetAnime(15);
	if (ObjectIsAnimeFrame(21)) object->o_velf = 3;
	if (objectlib_8029FF04())   return TRUE;
	else                        return FALSE;
}

static int enemya_802B4300(void)
{
	object->o_velf = 3;
	ObjectSetAnime(13);
	if (objectlib_8029FF04())   return TRUE;
	else                        return FALSE;
}

static int enemya_802B4368(void)
{
	ObjectSetAnime(14);
	if (ObjectIsAnimeFrame(20)) object->o_velf = 0;
	if (objectlib_8029FF04())   return TRUE;
	else                        return FALSE;
}

static void enemya_802B43DC(void)
{
	if      (object->o_var == 0)    object->o_mode = 5;
	else if (object->o_var == 1)    object->o_mode = 6;
	else if (object->o_code == 1)   object->o_mode = 13;
	else                            object->o_mode = 0;
}

static void enemya_802B4478(void)
{
	object->o_velf = 0;
	ObjectSetAnime(12);
	enemya_802B43DC();
}

static void enemya_802B44BC(void)
{
	if (object->o_phase == 0)
	{
		if (enemya_802B4288()) object->o_phase++;
	}
	else if (object->o_phase == 1)
	{
		if (enemya_802B4300()) object->o_phase++;
	}
	else
	{
		if (enemya_802B4368())
		{
			if (object->o_var == 1) object->o_var = 0;
			enemya_802B43DC();
		}
	}
}

static s8 enemya_8033045C[] =
	{7, 8, 9, 12, 13, 14, 15, 4, 3, 16, 17, 19, 3, 3, 3, 3};

UNUSED
static void enemya_802B459C(void)
{
	if (db_work[5][1])
	{
		object->o_mode = enemya_8033045C[db_work[5][2] & 15];
		db_work[5][1] = 0;
	}
}

static void enemya_802B45F4(void)
{
	float sp1C = RandF();
	if (object->work[O_V7].s[0] == 0)
	{
		if (object->o_v0 & 2)
		{
			if (object->o_targetdist < 1500)    object->o_mode = 15;
			else                                object->o_mode = 17;
		}
		else
		{
			object->o_mode = 14;
		}
		object->work[O_V7].s[0]++;
	}
	else
	{
		object->work[O_V7].s[0] = 0;
#if REVISION >= 199609
		if (!demop)
		{
			if (sp1C < 0.1) object->o_mode = 3;
			else            object->o_mode = 14;
		}
		else
		{
			object->o_mode = 14;
		}
#else
		if (sp1C < 0.1) object->o_mode = 3;
		else            object->o_mode = 14;
#endif
	}
}

static void enemya_802B473C(void)
{
	float sp1C = RandF();
	if (object->work[O_V7].s[0] == 0)
	{
		if (object->o_v0 & 2)
		{
			if (object->o_targetdist < 1300)
			{
				if (sp1C < 0.5) object->o_mode = 16;
				else            object->o_mode = 9;
			}
			else
			{
				object->o_mode = 7;
				if (500 < object->o_f2 && object->o_f2 < 1500)
				{
					if (sp1C < 0.5) object->o_mode = 13;
				}
			}
		}
		else
		{
			object->o_mode = 14;
		}
		object->work[O_V7].s[0]++;
	}
	else
	{
		object->work[O_V7].s[0] = 0;
		object->o_mode = 14;
	}
}

static void enemya_802B48D4(void)
{
	float sp1C = RandF();
	if (object->o_v0 & 2)
	{
		if (object->o_targetdist < 1000)
		{
			if      (sp1C < 0.4)    object->o_mode = 9;
			else if (sp1C < 0.8)    object->o_mode = 8;
			else                    object->o_mode = 15;
		}
		else if (sp1C < 0.5)
		{
			object->o_mode = 13;
		}
		else
		{
			object->o_mode = 7;
		}
	}
	else
	{
		object->o_mode = 14;
	}
}

static void enemya_802B4A1C(void)
{
	object->o_mode = 13;
}

static void enemya_802B4A3C(void)
{
	switch (object->work[O_V7].s[0])
	{
	case 0:
		if (object->work[O_V4].s[1] == 0)   enemya_802B48D4();
		else                                enemya_802B4A1C();
		object->work[O_V7].s[0] = 1;
		break;
	case 1:
		object->work[O_V7].s[0] = 0;
		object->o_mode = 14;
		break;
	}
}

#if REVISION >= 199609
static void enemya_802B4AF4(void)
{
	if (object->o_vely < 0 && object->o_posy < object->o_savey-300)
	{
		object->o_posx = object->o_posz = 0;
		object->o_posy = object->o_savey + 2000;
		object->o_vely = 0;
		object->o_velf = 0;
	}
}
#endif

static void enemya_802B4BAC(void)
{
	if (objectlib_802A5288(12)) object->o_mode = 0;
}

static void enemya_802B4BE8(void)
{
	object->work[O_V9].s[0] = 0;
	ObjectSetAnime(12);
	object->o_roty = 0;
	object->o_velf = 0;
	object->o_vely = 0;
	if      (object->o_code == 0)   enemya_802B45F4();
	else if (object->o_code == 1)   enemya_802B473C();
	else                            enemya_802B4A3C();
}

static void enemya_802B4CA4(void)
{
	object->o_velf = 0;
	if (object->o_timer == 0) ObjectPlaySound(NA_SE5_08);
	if (objectlib_802A5288(6)) object->o_mode = 0;
}

static void enemya_802B4D14(void)
{
	UNUSED int result;
	SHORT rot, dang = DeltaAng(object->o_angy, object->o_targetang);
	if      (object->o_code == 1)   rot = 0x400;
	else if (object->o_hp >= 3)     rot = 0x400;
	else if (object->o_hp == 2)     rot = 0x300;
	else                            rot = 0x200;
	result = ObjectTurn(object->o_targetang, rot);
	if (object->o_phase == 0)
	{
		object->o_v1 = 0;
		if (enemya_802B4288()) object->o_phase++;
	}
	else if (object->o_phase == 1)
	{
		if (enemya_802B4300())
		{
			object->o_v1++;
			if (object->o_v0 & 0x20000)
			{
				if (object->o_v1 > 4) object->o_v0 &= ~0x20000;
			}
			else
			{
				if (dang < 0x2000) object->o_phase++;
			}
		}
	}
	else
	{
		if (enemya_802B4368()) object->o_mode = 0;
	}
}

static void enemya_802B4F00(void)
{
	switch (object->o_phase)
	{
	case 0:
		ObjectHitOFF();
		object->work[O_V8].s[0] = 0;
		object->o_v1 = 30;
		if (object->o_timer == 0) ObjectPlaySound(NA_SE9_66);
		if (object->o_alpha == 0)
		{
			object->o_phase++;
			object->o_angy = object->o_targetang;
		}
		break;
	case 1:
		if (object->o_v1--)
		{
			object->o_velf = 100;
		}
		else
		{
			object->o_phase = 2;
			object->o_angy = object->o_targetang;
		}
		if (
			DeltaAng(object->o_angy, object->o_targetang) > 0x4000 &&
			object->o_targetdist > 500
		)
		{
			object->o_phase = 2;
			object->o_angy = object->o_targetang;
			ObjectPlaySound(NA_SE9_66);
		}
		break;
	case 2:
		object->o_velf = 0;
		object->work[O_V8].s[0] = 0xFF;
		if (object->o_alpha == 0xFF) object->o_mode = 0;
		ObjectHitON();
		break;
	}
}

extern OBJLANG obj_13001984[];

static void enemya_802B5104(void)
{
	int frame;
	ObjectSetAnime(11);
	frame = object->s.skel.frame;
	if (frame >= 25 && frame <= 35)
	{
		ObjectLevelSound(NA_SE6_00);
		if (frame == 35)
		{
			ObjMakeOff(1, 0, 400, 100, object, S_FLAME, obj_13001984);
		}
		else
		{
			ObjMakeOff(0, 0, 400, 100, object, S_FLAME, obj_13001984);
		}
	}
	if (objectlib_8029FF04()) object->o_mode = 0;
	object->o_v0 |= 0x20000;
}

static void enemya_802B5218(void)
{
	if (object->o_timer == 0)
	{
		object->o_velf = -400;
		object->o_vely = 100;
		object->o_angy = object->work[O_V7].s[1] + 0x8000;
		object->work[O_V9].s[0] = 1;
	}
	if (object->o_phase == 0)
	{
		ObjectSetAnime(25);
		object->o_phase++;
		object->o_v1 = 0;
	}
	else if (object->o_phase == 1)
	{
		ObjectSetAnime(25);
		ObjectAnimeHoldEnd();
		enemya_802B41FC(&object->o_v1);
		if (object->o_v1 > 2)
		{
			ObjectSetAnime(26);
			object->o_vely = 0;
			object->o_velf = 0;
			object->o_phase++;
		}
	}
	else if (object->o_phase == 2)
	{
		if (objectlib_8029FF04())
		{
			if (object->o_hp == 1)  object->o_mode = 3;
			else                    object->o_mode = 0;
			object->work[O_V9].s[0] = 0;
		}
	}
	else
	{
	}
}

static int enemya_802B53F4(void)
{
	ObjectSetAnime(9);
	if (ObjectIsAnimeFrame(11)) return TRUE;
	else                        return FALSE;
}

static int enemya_802B5444(void)
{
	if (object->o_move & OM_BOUND)
	{
		object->o_velf = 0;
		object->o_vely = 0;
		enemya_802AAE8C(0, 0, 60);
		ObjectSetAnime(8);
		object->s.skel.frame = 0;
		objectlib_802A1930(object, 7);
		if (object->o_code == 0)
		{
			if (object->o_targetdist < 850)
			{
				mario_obj->o_hit_result |= HR_000002;
			}
			else
			{
				mario_obj->o_hit_result |= HR_000001;
			}
		}
		return TRUE;
	}
	else
	{
		return FALSE;
	}
}

static void enemya_802B5554(void)
{
	if (object->o_code == 2 && object->o_v0 & 0x10000)
	{
		if (object->o_f2 > 1000) object->o_velf = 60;
	}
}

static void enemya_802B55CC(void)
{
	UNUSED int i;
	if (object->o_phase == 0)
	{
		if (enemya_802B53F4())
		{
			if (object->o_code == 2 && object->o_v0 & 0x10000)
			{
				object->o_vely = 70;
			}
			else
			{
				object->o_vely = 80;
			}
			object->o_v1 = 0;
			enemya_802B5554();
			object->o_phase++;
		}
	}
	else if (object->o_phase == 1)
	{
#if REVISION >= 199609
		if (object->o_code == 2 && object->o_v0 & 0x10000) enemya_802B4AF4();
#endif
		if (enemya_802B5444())
		{
			object->o_v0 &= ~0x10000;
			object->o_velf = 0;
			object->o_phase++;
			enemya_802B4184();
			if (object->o_code == 1) object->o_mode = 19;
		}
		else
		{
		}
	}
	else
	{
		if (objectlib_8029FF04()) object->o_mode = 0;
	}
}

static short enemya_8033046C[] = {60};
static short enemya_80330470[] = {50};

static void enemya_802B5798(void)
{
	float vely = enemya_8033046C[0];
	float velf = enemya_80330470[0];
	if (object->o_phase == 0)
	{
		if (enemya_802B53F4())
		{
			object->o_vely = vely;
			object->o_velf = velf;
			object->o_v1 = 0;
			object->o_phase++;
		}
	}
	else if (object->o_phase == 1)
	{
		if (enemya_802B5444()) object->o_phase++;
	}
	else
	{
		if (objectlib_8029FF04()) object->o_mode = 0;
	}
}

static void enemya_802B58BC(void)
{
	object->o_velf = 0;
	if (object->o_timer == 0) object->o_v1 = 0;
	switch (object->o_phase)
	{
	case 0:
		ObjectSetAnime(23);
		if (objectlib_8029FF04()) object->o_v1++;
		if (object->o_v1 > 0) object->o_phase++;
		break;
	case 1:
		ObjectSetAnime(24);
		if (objectlib_8029FF04()) object->o_mode = 11;
		break;
	}
}

static void enemya_802B59CC(void)
{
	if (hud.power < 4)  object->work[O_V5].s[0] = 3;
	else                object->work[O_V5].s[0] = 1 + 3*RandF();
	ObjectSetAnime(22);
	if (ObjectIsAnimeFrame(5))
	{
		enemyc_8030CD30(0, 200, 180, 7, S_FLAME, 30, 10, 0x1000);
	}
	if (objectlib_8029FF04()) object->o_phase++;
	if (object->o_phase >= object->work[O_V5].s[0]) object->o_mode = 0;
}

static int enemya_802B5AEC(int a0, short a1)
{
	if (object->o_phase == 0)
	{
		if (objectlib_802A5288(15)) object->o_phase++;
	}
	else if (object->o_phase == 1)
	{
		if (objectlib_802A5288(14)) object->o_phase++;
	}
	else
	{
		ObjectSetAnime(12);
	}
	object->o_velf = 0;
	object->o_angy += a1;
	if (object->o_timer >= a0)  return TRUE;
	else                        return FALSE;
}

static void enemya_802B5C00(void)
{
	if (enemya_802B5AEC(63, 0x200)) object->o_mode = 0;
}

extern OBJLANG obj_13002528[];

static void enemya_802B5C40(void)
{
	int sp34;
	if (object->o_timer == 0) object->o_velf = 0;
	switch (object->o_phase)
	{
	case 0:
		object->o_v1 = 0;
		if (objectlib_802A5288(18)) object->o_phase = 1;
		break;
	case 1:
		object->o_velf = 50;
		if (objectlib_802A5288(19))
		{
			object->o_v1++;
			if (object->o_v1 > 5) object->o_phase = 3;
			if (object->o_v1 > 1)
			{
				if (DeltaAng(object->o_targetang, object->o_angy) > 0x2000)
				{
					object->o_phase = 3;
				}
			}
		}
		ObjectTurn(object->o_targetang, 0x200);
		break;
	case 3:
		object->o_v1 = 0;
		ObjectSetAnime(21);
		ObjMakeOffScale(0,  100, -50, 0, 3, object, S_DUST, obj_13002528);
		ObjMakeOffScale(0, -100, -50, 0, 3, object, S_DUST, obj_13002528);
		if (Accelerate(&object->o_velf, 0, -1)) object->o_phase = 2;
		ObjectAnimeHoldEnd();
		break;
	case 2:
		object->o_velf = 0;
		ObjectSetAnime(20);
		if (objectlib_8029FF04())
		{
			if (object->o_code == 2)    sp34 = 10;
			else                        sp34 = 30;
			if (object->o_v1 > sp34) object->o_mode = 0;
			object->o_v1++;
		}
		ObjectAnimeHoldEnd();
		break;
	}
	if (object->o_move & OM_0400) object->o_mode = 10;
}

extern OBJLANG obj_130037EC[];

static int enemya_802B5F6C(void)
{
	OBJECT *o;
	float dist;
	if ((o = ObjectFind(obj_130037EC, &dist)) && dist < 800)
	{
		o->o_hit_result |= HR_200000;
		return TRUE;
	}
	return FALSE;
}

static void enemya_802B5FEC(void)
{
	UNUSED int i;
	if (object->o_timer < 2) object->o_v1 = 0;
	if (object->o_phase == 0)
	{
		ObjectSetAnime(2);
		enemya_802B41FC(&object->o_v1);
		if (object->o_move & OM_TOUCH)
		{
			object->o_velf = 0;
			object->o_phase++;
		}
	}
	else
	{
		if (objectlib_802A5288(0)) object->o_mode = 0;
	}
	if (enemya_802B5F6C())
	{
		object->o_hp--;
		if (object->o_hp < 1)   object->o_mode = 4;
		else                    object->o_mode = 12;
	}
}

static void enemya_802B611C(void)
{
	object->work[O_V8].s[0] = 0;
	if (object->o_alpha == 0)
	{
		object->o_velf = 0;
		object->o_vely = 0;
		object->o_posy = object->o_savey - 1000;
	}
}

static void enemya_802B6190(void)
{
	int on_movebg;
	UNUSED int i;
	BGFACE *ground = object->o_ground;
	if (ground && ground->flag & BG_MOVE)   on_movebg = TRUE;
	else                                    on_movebg = FALSE;
	object->o_v0 |= 0x10000;
	switch (object->o_phase)
	{
	case 0:
		if (object->o_timer == 0)
		{
			object->o_shapeangx = 0;
			object->o_shapeangz = 0;
		}
		object->o_shapeangx += 0x800;
		object->o_shapeangz += 0x800;
		if (!(object->o_shapeangx & 0xFFFF)) object->o_phase++;
		enemya_802B611C();
		break;
	case 1:
		ObjectSetAnime(9);
		if (ObjectIsAnimeFrame(11))
		{
			object->o_angy = object->work[O_V7].s[1];
			object->o_vely = 150;
			object->work[O_V8].s[0] = 0xFF;
			object->o_v1 = 0;
			object->o_phase++;
		}
		else
		{
			enemya_802B611C();
		}
		break;
	case 2:
		if (object->o_posy > object->o_savey)
		{
			object->o_drag = 0;
			if (object->o_f2 < 2500)
			{
				if (fabsf(object->o_ground_y-object->o_savey) < 100)
				{
					Accelerate(&object->o_velf, 0, -5);
				}
				else
				{
					ObjectAccelerate(150, 2);
				}
			}
			else
			{
				ObjectAccelerate(150, 2);
			}
		}
		if (enemya_802B5444())
		{
			object->o_drag = 10;
			object->o_phase++;
			if (!on_movebg)
			{
				enemya_802B4184();
			}
			else
			{
				if (object->o_code == 2) object->o_mode = 13;
			}
			if (object->o_code == 1) object->o_mode = 19;
		}
#if REVISION >= 199609
		enemya_802B4AF4();
#else
		if (object->o_vely < 0 && object->o_posy < object->o_savey-300)
		{
			object->o_posx = object->o_posz = 0;
			object->o_posy = object->o_savey + 2000;
			object->o_vely = 0;
		}
#endif
		break;
	case 3:
		if (objectlib_8029FF04())
		{
			object->o_mode = 0;
			object->o_v0 &= ~0x10000;
			ObjectAnimeHoldEnd();
		}
		break;
	}
	DbPrintErr("sp %d", object->o_velf);
}

static s8 enemya_80330474[] = {24, 42, 60, -1};

static void enemya_802B6568(void)
{
	if (InTable(object->o_timer, enemya_80330474)) ObjectPlaySound(NA_SE5_03);
	if (objectlib_802A5288(10)) object->o_mode = 0;
}

extern OBJLANG obj_130016E4[];
extern OBJLANG obj_13001714[];

static void enemya_802B65D0(void)
{
	if (object->o_code == 2)
	{
		camera_8032DF30 = ObjMakeHere(object, S_POWERSTAR, obj_13001714);
	}
	else
	{
		camera_8032DF30 = ObjMakeHere(object, S_BOWSERKEY, obj_130016E4);
		ObjectPlaySound(NA_SE8_61);
	}
	camera_8032DF30->o_roty = object->o_roty;
}

static void enemya_802B6670(void)
{
	ObjectSetAnime(16);
	if (object->o_code == 2)    object->o_velf = -400;
	else                        object->o_velf = -200;
	object->o_vely = 100;
	object->o_angy = object->work[O_V7].s[1] + 0x8000;
	object->o_v1 = 0;
	object->o_phase++;
}

static void enemya_802B6730(void)
{
	object->work[O_V9].s[0] = 1;
	enemya_802B41FC(&object->o_v1);
	if (object->o_move & OM_BOUND) ObjectPlaySound(NA_SE5_03);
	if (object->o_move & OM_TOUCH)
	{
		object->o_velf = 0;
		object->o_phase++;
	}
}

static int enemya_802B67D4(void)
{
	int result = FALSE;
	ObjectHitOFF();
	if (
		objectlib_802A5288(17) && object->o_targetdist < 700 &&
		DeltaAng(mario_obj->o_angy, object->o_targetang) > 0x6000
	) result = TRUE;
	ObjectAnimeHoldEnd();
	object->o_v1 = 0;
	return result;
}

static int enemya_802B6878(void)
{
	int result = FALSE;
	if (object->s.scale[0] < 0.8) object->o_roty += 0x80;
	if (object->s.scale[0] > 0.2)
	{
		object->s.scale[0] -= 0.02;
		object->s.scale[2] -= 0.02;
	}
	else
	{
		object->s.scale[1] -= 0.01;
		object->o_vely = 20;
		object->o_gravity = 0;
	}
	if (object->s.scale[1] < 0.5) result = TRUE;
	object->o_angy += object->o_roty;
	if (object->o_alpha > 2) object->o_alpha -= 2;
	return result;
}

static void enemya_802B6A10(void)
{
	ObjectSetScale(0);
	object->o_velf = 0;
	object->o_vely = 0;
	object->o_gravity = 0;
}

static short enemya_80330478[] = {MSG_119, MSG_120, MSG_121};

static int enemya_802B6A78(void)
{
	int result = FALSE;
	if (object->o_v1 < 2)
	{
		if (object->o_v1 == 0)
		{
			Na_SeqMute(0, 60, 40);
			object->o_v1++;
		}
		if (objectlib_802A4960(2, 18, enemya_80330478[object->o_code], 0))
		{
			object->o_v1++;
			ObjectPlaySound(NA_SE8_60);
			Na_SeqUnmute(0, 60);
			Na_SeqFadeout(0, 1);
		}
	}
	else
	{
		if (enemya_802B6878())
		{
			enemya_802B6A10();
			enemya_802AE0CC(20, S_COIN, 1, 0);
			enemya_802B65D0();
			pldemo_80257640(0);
			result = TRUE;
		}
	}
	return result;
}

static int enemya_802B6BAC(void)
{
	UNUSED int i;
	int result = FALSE;
	if (object->o_v1 < 2)
	{
		int msg;
		if (hud.star < 120) msg = MSG_121;
		else                msg = MSG_163;
		if (object->o_v1 == 0)
		{
			Na_SeqMute(0, 60, 40);
			object->o_v1++;
		}
		if (objectlib_802A4960(2, 18, msg, 0))
		{
			ObjectSetShape(105); /* T:shape */
			Na_SeqUnmute(0, 60);
			Na_SeqFadeout(0, 1);
			enemya_802B65D0();
			object->o_v1++;
		}
	}
	else
	{
		if (object->o_alpha > 4)
		{
			object->o_alpha -= 4;
		}
		else
		{
			enemya_802B6A10();
			result = TRUE;
		}
	}
	return result;
}

static void enemya_802B6CF0(void)
{
	switch (object->o_phase)
	{
	case 0:
		enemya_802B6670();
		break;
	case 1:
		enemya_802B6730();
		break;
	case 2:
		if (enemya_802B67D4())
		{
			object->o_v1 = 0;
			if (object->o_code == 2)
			{
				object->o_phase = 10;
			}
			else
			{
				object->flag |= OBJ_DITHER;
				object->o_phase++;
			}
		}
		break;
	case 3:
		if (enemya_802B6A78()) object->o_phase++;
		break;
	case 4:
		break;
	case 10:
		if (enemya_802B6BAC()) object->o_phase++;
		break;
	case 11:
		break;
	}
}

static void enemya_802B6E40(OBJECT *obj, SHORT rot)
{
	SHORT angy = object->work[O_V7].s[1] + 0x8000;
	obj->o_rotx = rot* COS(angy);
	obj->o_rotz = rot*-SIN(angy);
}

static short enemya_80330480[][3] =
{
	{ 1,   10,  40},
	{ 0,    0,  74},
	{-1,  -10, 114},
	{ 1,  -20, 134},
	{-1,   20, 154},
	{ 1,   40, 164},
	{-1,  -40, 174},
	{ 1,  -80, 179},
	{-1,   80, 184},
	{ 1,  160, 186},
	{-1, -160, 186},
	{ 1,    0,   0},
};

extern OBJLANG obj_13001920[];

static void enemya_802B6EE0(void)
{
	OBJECT *o = ObjectFindObj(obj_13001920);
	UNUSED SHORT sp2A = object->work[O_V7].s[1] + 0x8000;
	if (!o)
	{
		object->o_mode = 0;
	}
	else
	{
		short sp28;
		UNUSED int n;
		int i = 0;
		int sp1C = TRUE;
		while (enemya_80330480[i][2])
		{
			if (object->o_timer < enemya_80330480[i][2])
			{
				sp28 = enemya_80330480[i][1];
				if (enemya_80330480[i][0] > 0)
				{
					sp28 = (enemya_80330480[i][2]-object->o_timer-1) * sp28;
				}
				else
				{
					sp28 = (object->o_timer-enemya_80330480[i-1][2]) * sp28;
				}
				enemya_802B6E40(o, sp28);
				if (sp28) Na_ObjSePlay(NA_SE4_15, o);
				sp1C = FALSE;
				break;
			}
			i++;
		}
		if (sp1C)
		{
			object->o_mode = 0;
			o->o_rotx = 0;
			o->o_rotz = 0;
			o->o_shapeangx = 0;
			o->o_shapeangz = 0;
		}
	}
	ObjectAnimeHoldEnd();
}

static int enemya_802B711C(void)
{
	if (object->o_mode != 2 && object->o_mode != 19)
	{
		if (object->o_posy < object->o_savey-1000) return TRUE;
		if (object->o_move & OM_BOUND)
		{
			if (object->o_bgcode == BG_1) return TRUE;
			if (object->o_bgcode == BG_10) return TRUE;
		}
	}
	return FALSE;
}

static OBJCALL *enemya_803304C8[] =
{
	enemya_802B4BE8,
	enemya_802B5FEC,
	enemya_802B6190,
	enemya_802B6568,
	enemya_802B6CF0,
	enemya_802B4478,
	enemya_802B44BC,
	enemya_802B5C40,
	enemya_802B5104,
	enemya_802B59CC,
	enemya_802B58BC,
	enemya_802B5C00,
	enemya_802B5218,
	enemya_802B55CC,
	enemya_802B4D14,
	enemya_802B4CA4,
	enemya_802B4F00,
	enemya_802B5798,
	enemya_802B4BAC,
	enemya_802B6EE0,
};

static STEPSOUND enemya_80330518[] =
{
	{0,  0,   0, NA_SE_NULL},
	{0,  0,   0, NA_SE_NULL},
	{0,  0,   0, NA_SE_NULL},
	{0,  0,   0, NA_SE_NULL},
	{0,  0,   0, NA_SE_NULL},
	{0,  0,   0, NA_SE_NULL},
	{0,  0,   0, NA_SE_NULL},
	{0,  0,   0, NA_SE_NULL},
	{1,  0,  -1, NA_SE5_03},
	{1,  0,  -1, NA_SE9_04},
	{1,  0,  -1, NA_SE9_04},
	{0,  0,   0, NA_SE_NULL},
	{0,  0,   0, NA_SE_NULL},
	{1, 20,  40, NA_SE5_03},
	{1, 20,  -1, NA_SE5_03},
	{1, 20,  40, NA_SE5_03},
	{1,  0,  -1, NA_SE5_05},
	{1,  0,  -1, NA_SE5_06},
	{1,  8,  -1, NA_SE5_03},
	{1,  8,  17, NA_SE5_03},
	{1,  8, -10, NA_SE5_03},
	{0,  0,   0, NA_SE_NULL},
	{1,  5,  -1, NA_SE5_55},
	{0,  0,   0, NA_SE_NULL},
	{0,  0,   0, NA_SE_NULL},
	{1,  0,  -1, NA_SE5_05},
	{1,  0,  -1, NA_SE9_04},
};

static void enemya_802B71E4(void)
{
	BGFACE *ground;
	OBJECT *movebg;
	UNUSED float ground_y;
	if ((movebg = object->movebg)) MoveBGProc(FALSE, movebg);
	object->work[O_V6].s[1] = 0;
	objectlib_802A2320();
	ObjectCallMode(enemya_803304C8);
	objectlib_802A2348(-78);
	if (enemya_802B711C()) object->o_mode = 2;
	ground_y = BGCheckGround(
		object->o_posx, object->o_posy, object->o_posz, &ground
	);
	if (ground && ground->obj)  object->movebg = ground->obj;
	else                        object->movebg = NULL;
	ObjectStepSound(enemya_80330518);
}

static void enemya_802B72D4(void)
{
	object->o_v0 &= ~0x20000;
	ObjectHitOFF();
	switch (object->work[O_V6].s[1])
	{
	case 0:
		ObjectPlaySound(NA_SE5_05);
		objectlib_802A01D8(3, 1);
		object->work[O_V6].s[1]++;
		break;
	case 1:
		if (objectlib_8029FF04())
		{
			ObjectSetAnime(2);
			object->work[O_V6].s[1]++;
		}
		break;
	case 2:
		break;
	}
	object->o_move = 0;
	object->work[O_V5].s[1] = mario_obj->o_angx;
	object->work[O_V6].s[0] = mario_obj->o_roty;
	object->o_angy = mario_obj->o_angy;
}

static void enemya_802B7418(void)
{
	float speed;
	object->work[O_V6].s[1] = 0;
	objectlib_802A0380(1, 1, 1);
	speed = object->work[O_V6].s[0]/3000.0 * 70;
	if (speed < 0) speed = -speed;
	if (speed > 90) speed *= 2.5;
	object->o_velf = speed* COS(object->o_v5);
	object->o_vely = speed*-SIN(object->o_v5);
	ObjectHitOFF();
	object->child->o_mode = 1;
	object->child->o_timer = 0;
	object->child->o_phase = 0;
	object->o_timer = 0;
	object->o_phase = 0;
}

void enemya_802B75A4(void)
{
	SHORT sp26, sp24;
	object->o_f2 = DIST2(object->o_posx, object->o_posz);
	object->work[O_V7].s[1] = ATAN2(0-object->o_posz, 0-object->o_posx);
	sp26 = DeltaAng(object->o_angy, object->o_targetang);
	sp24 = DeltaAng(object->o_angy, object->work[O_V7].s[1]);
	object->o_v0 &= ~0xFF;
	if (sp26 < 0x2000) object->o_v0 |= 2;
	if (sp24 < 0x3800) object->o_v0 |= 4;
	if (object->o_f2 < 1000) object->o_v0 |= 16;
	if (object->o_targetdist < 850) object->o_v0 |= 8;
	switch (object->o_action)
	{
	case OA_0: enemya_802B71E4(); break;
	case OA_1: enemya_802B72D4(); break;
	case OA_2: enemya_802B7418(); break;
	case OA_3: enemya_802B7418(); break;
	}
	ObjectStand();
	if (object->o_mode != 4)
	{
		if (object->work[O_V8].s[0] != object->o_alpha)
		{
			if (object->work[O_V8].s[0] > object->o_alpha)
			{
				object->o_alpha += 20;
				if (object->o_alpha > 0xFF) object->o_alpha = 0xFF;
			}
			else
			{
				object->o_alpha -= 20;
				if (object->o_alpha < 0) object->o_alpha = 0;
			}
		}
	}
}

static s8 enemya_803305F0[] = {0, 0, 1};
static s8 enemya_803305F4[] = {1, 1, 3};

void enemya_802B7878(void)
{
	int code;
	object->work[O_V7].s[0] = 1;
	object->o_alpha = 0xFF;
	object->work[O_V8].s[0] = 0xFF;
	if      (stage_index == STAGE_BITFSA)   code = 1;
	else if (stage_index == STAGE_BITSA)    code = 2;
	else                                    code = 0;
	object->o_code = code;
	object->work[O_V9].s[1] = enemya_803305F0[code];
	object->o_hp = enemya_803305F4[code];
	objectlib_802A1930(object, 4);
	object->o_mode = 5;
	object->work[O_V8].s[1] = 0;
	object->work[O_V9].s[0] = 0;
}

void *Ctrl_enemya_802B798C(int code, UNUSED SHAPE *shape, void *data)
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

static void enemya_802B7A20(OBJECT *obj, SSELECT *shp)
{
	int index;
	SHORT dang = DeltaAng(obj->o_angy, obj->o_targetang);
	switch (index = shp->index)
	{
	case 0:
		if (dang > 0x2000)
		{
			if (obj->o_roty > 0) shp->index = 5;
			if (obj->o_roty < 0) shp->index = 3;
		}
		if (obj->work[O_V8].s[1] > 50) shp->index = 1;
		break;
	case 1:
		if (obj->work[O_V8].s[1] > 2) shp->index = 2;
		break;
	case 2:
		if (obj->work[O_V8].s[1] > 2) shp->index = 9;
		break;
	case 9:
		if (obj->work[O_V8].s[1] > 2) shp->index = 0;
		break;
	case 5:
		if (obj->work[O_V8].s[1] > 2)
		{
			shp->index = 6;
			if (obj->o_roty <= 0) shp->index = 0;
		}
		break;
	case 6:
		if (obj->o_roty <= 0) shp->index = 5;
		break;
	case 3:
		if (obj->work[O_V8].s[1] > 2)
		{
			shp->index = 4;
			if (obj->o_roty >= 0) shp->index = 0;
		}
		break;
	case 4:
		if (obj->o_roty >= 0) shp->index = 3;
		break;
	default:
		shp->index = 0;
	}
	if (shp->index != index) obj->work[O_V8].s[1] = -1;
}

void *Ctrl_enemya_802B7C64(int code, SHAPE *shape, UNUSED void *data)
{
	short sp36;
	UNUSED int i;
	OBJECT *obj = (OBJECT *)draw_object;
	SSELECT *shp = (SSELECT *)shape;
	if (code == SC_DRAW)
	{
		if (draw_hand) obj = (OBJECT *)draw_hand->obj;
		switch (sp36 = obj->work[O_V9].s[0])
		{
		case 0:
			enemya_802B7A20(obj, shp);
			break;
		case 1:
			shp->index = 2;
			break;
		}
		obj->work[O_V8].s[1]++;
	}
	return NULL;
}

void *Ctrl_enemya_802B7D44(int code, SHAPE *shape, UNUSED void *data)
{
	Gfx *gfx = NULL;
	if (code == SC_DRAW)
	{
		Gfx *g;
		OBJECT *obj = (OBJECT *)draw_object;
		SSELECT *shp = (SSELECT *)shape;
		if (draw_hand) obj = (OBJECT *)draw_hand->obj;
		if (obj->o_alpha == 0xFF)   ShpSetLayer(&shp->s.s, LAYER_OPA_SURF);
		else                        ShpSetLayer(&shp->s.s, LAYER_XLU_SURF);
		g = gfx = GfxAlloc(sizeof(Gfx)*2);
		if (obj->work[O_V9].s[1] != 0)
		{
			gSPClearGeometryMode(g++, G_LIGHTING);
		}
		gSPEndDisplayList(g);
	}
	return gfx;
}

struct enemya3
{
	MAP *map;
	short posx;
	short posz;
	short angy;
};

extern MAP map_07004B94[];
extern MAP map_07004C18[];
extern MAP map_07004C9C[];
extern MAP map_07004D20[];
extern MAP map_07004DA4[];
extern MAP map_07004E28[];
extern MAP map_07004EAC[];
extern MAP map_07004F30[];
extern MAP map_07004FB4[];
extern MAP map_07005038[];

static struct enemya3 enemya_803305F8[] =
{
	{0},
	{map_07004B94,  -800, -1000, -0x5200},
	{map_07004C18, -1158,   390, -0x4800},
	{map_07004C9C, -1158,   390, -0x1E00},
	{map_07004D20,     0,  1240, -0x1800},
	{map_07004DA4,     0,  1240,  0x1800},
	{map_07004E28,  1158,   390,  0x1E00},
	{map_07004EAC,  1158,   390,  0x4800},
	{map_07004F30,   800, -1000,  0x5200},
	{map_07004FB4,   800, -1000, -0x7C00},
	{map_07005038,  -800, -1000,  0x7C00},
};

extern OBJLANG obj_13001850[];

static void enemya_802B7E68(void)
{
	object->o_p1 = ObjectFindObj(obj_13001850);
	ObjSetMap(object, enemya_803305F8[object->o_code].map);
	if (object->o_p1) object->o_mode = 1;
}

static void enemya_802B7EF0(void)
{
	UNUSED int i;
	OBJECT *o = object->o_p1;
	if (o->movebg == object)
	{
		if (o->o_mode == 13 && o->o_v0 & 0x10000) object->o_mode = 2;
	}
	if (o->o_hp == 1 && (o->o_mode == 3 || o->o_action != OA_0))
	{
		object->o_phase = 1;
	}
	if (object->o_phase == 0)
	{
		object->o_v2 = 0;
	}
	else
	{
		if ((20+db_work[4][6])*(object->o_code-1) < object->o_v2)
		{
			object->o_mode = 2;
		}
		object->o_v2++;
	}
}

static void enemya_802B8024(void)
{
	FVEC sp24;
	short angy;
	float dist;
	UNUSED OBJECT *o = object->o_p1;
	if (object->o_timer == 0 || object->o_timer == 22)
	{
		ObjectPlaySound(NA_SE3_62);
	}
	if (object->o_timer < 22)
	{
		camera_8027F8B8(10);
		object->o_vely = 8;
		object->o_gravity = 0;
	}
	else
	{
		object->o_gravity = -4;
	}
	if (!(object->o_timer & 1) && object->o_timer < 14)
	{
		angy = enemya_803305F8[object->o_code].angy + 0x100*db_work[4][1];
		dist = 1740 + 290*-(object->o_timer/2);
		enemya_802B98D4(sp24, &object->o_posx);
		object->o_posx =
			enemya_803305F8[object->o_code].posx + dist*SIN(angy+0x14B0);
		object->o_posz =
			enemya_803305F8[object->o_code].posz + dist*COS(angy+0x14B0);
		object->o_posy = 307;
		enemya_802AAE8C(4, 0, 100);
		object->o_posx =
			enemya_803305F8[object->o_code].posx + dist*SIN(angy-0x14B0);
		object->o_posz =
			enemya_803305F8[object->o_code].posz + dist*COS(angy-0x14B0);
		enemya_802AAE8C(4, 0, 100);
		enemya_802B98D4(&object->o_posx, sp24);
	}
	ObjectProcMoveF();
	if (object->o_timer > 300) ObjKill(object);
}

static OBJCALL *enemya_8033067C[] =
{
	enemya_802B7E68,
	enemya_802B7EF0,
	enemya_802B8024,
};

void enemya_802B8384(void)
{
	ObjectCallMode(enemya_8033067C);
}

static HITINFO enemya_80330688 =
{
	/*type   */	HIT_BURN,
	/*offset */	20,
	/*ap     */	1,
	/*hp     */	0,
	/*ncoin  */	0,
	/*hit r,h*/	10, 40,
	/*dmg r,h*/	0, 0,
};

static HITINFO enemya_80330698 =
{
	/*type   */	HIT_BURN,
	/*offset */	0,
	/*ap     */	1,
	/*hp     */	0,
	/*ncoin  */	0,
	/*hit r,h*/	10, 40,
	/*dmg r,h*/	0, 0,
};

extern OBJLANG obj_13000940[];
extern OBJLANG obj_1300127C[];

static void enemya_802B83B0(void)
{
	ObjKill(object);
	ObjMakeHereScale(object, S_NULL, obj_1300127C, 1);
	if (RandF() < 0.1) ObjMakeHere(object, S_COIN, obj_13000940);
}

static int enemya_802B8434(int a0)
{
	if (object->o_timer > a0) return TRUE;
	if (object->o_bgcode == BG_1) return TRUE;
	if (object->o_bgcode == BG_10) return TRUE;
	return FALSE;
}

void enemya_802B84AC(void)
{
	object->o_shape = 10*RandF();
	object->o_angy = Rand();
	if (RandF() < 0.2)  object->o_vely = 80;
	else                object->o_vely = 20;
	object->o_velf = 10;
	object->o_gravity = -1;
	object->o_f0 = 1+RandF();
}

void enemya_802B85B0(void)
{
	object->o_shape = 10*RandF();
	object->o_angy = Rand();
	object->o_vely = 10;
	object->o_velf = 0;
	object->o_f0 = 7;
}

static void enemya_802B8654(void)
{
	int angx = 0x400*((object->o_v1+gfx_frame) & 63);
	object->o_posx += SIN(object->o_angy) * SIN(angx) * 4;
	object->o_posz += COS(object->o_angy) * SIN(angx) * 4;
}

extern OBJLANG obj_13001AE8[];

void enemya_802B8734(void)
{
	objectlib_802A2320();
	objectlib_802A2348(78);
	if (object->o_vely < -4) object->o_vely = -4;
	if (object->o_mode == 0)
	{
		ObjectHitOFF();
		enemya_802B8654();
		if (object->o_move & OM_BOUND)
		{
			object->o_mode++;
			if (ObjectHasScript(obj_13001AE8))  object->o_f0 = 8;
			else                                object->o_f0 = 6 + 2*RandF();
			object->o_velf = 0;
			object->o_vely = 0;
			object->o_gravity = 0;
		}
	}
	else
	{
		ObjectHitON();
		if (object->o_timer > 5 + 10*object->o_f0)
		{
			object->o_f0 -= 0.15;
			if (object->o_f0 <= 0) enemya_802B83B0();
		}
	}
	ObjectSetScale(object->o_f0);
	object->o_shapeoff = 14*object->s.scale[1];
	ObjSetHitInfo(object, &enemya_80330698);
}

void enemya_802B8960(void)
{
	object->o_velf = 30;
	ObjRandOff2D(object, 80);
	object->o_shape = 10*RandF();
	object->o_f0 = 3;
}

extern OBJLANG obj_13001AA4[];

void enemya_802B89EC(void)
{
	UNUSED int i;
	UNUSED OBJECT *o;
	ObjSetHitInfo(object, &enemya_80330688);
	object->o_f0 += 0.5;
	ObjectSetScale(object->o_f0);
	if (object->o_angx > 0x800) object->o_angx -= 0x200;
	ObjectMoveULF();
	ObjectCheckGroundY();
	if (object->o_f0 > 30) ObjKill(object);
	if (object->o_posy < object->o_ground_y)
	{
		object->o_posy = object->o_ground_y;
		o = ObjMakeHere(object, S_FLAME, obj_13001AA4);
		ObjKill(object);
	}
}

void enemya_802B8B1C(void)
{
	object->o_shape = 10*RandF();
	object->o_angy = Rand();
	if (object->o_code != 0) object->o_velf = 5*RandF();
	else object->o_velf = 70*RandF();
	object->o_vely = 20*RandF();
	object->o_gravity = -1;
	object->o_v1 = 64*RandF();
}

static float enemya_803306A8[] = {-8, -6, -3};

extern OBJLANG obj_13001A0C[];

void enemya_802B8C38(void)
{
	UNUSED int i;
	objectlib_802A2320();
	objectlib_802A2348(78);
	enemya_802B8654();
	if (enemya_802B8434(900)) ObjKill(object);
	if (object->o_vely < enemya_803306A8[object->o_code])
	{
		object->o_vely = enemya_803306A8[object->o_code];
	}
	if (object->o_move & OM_BOUND)
	{
		if (object->o_code == 0)    ObjMakeHere(object, S_FLAME, obj_13001AE8);
		else                        ObjMakeHere(object, S_NULL, obj_13001A0C);
		ObjKill(object);
	}
	object->o_shapeoff = 14*object->s.scale[1];
}

void enemya_802B8D68(void)
{
	ObjRandOff2D(object, 80);
	object->o_shape = 10*RandF();
	object->o_vely = 7;
	object->o_velf = 35;
	object->o_f0 = 3;
	object->o_f2 = 0.5*RandF();
	object->o_gravity = 1;
	object->o_v1 = 64*RandF();
}

extern OBJLANG obj_130019C8[];

void enemya_802B8E7C(void)
{
	int i;
	ObjSetHitInfo(object, &enemya_80330688);
	if (object->o_f0 < 16) object->o_f0 += 0.5;
	ObjectSetScale(object->o_f0);
	objectlib_802A2320();
	objectlib_802A2348(78);
	if (object->o_timer > 20)
	{
		if (object->o_code == 0)
		{
			for (i = 0; i < 3; i++)
			{
				ObjMakeOffScale(0, 0, 0, 0, 5, object, S_FLAME, obj_130019C8);
			}
		}
		else
		{
			ObjMakeOffScale(1, 0, 0, 0, 8, object, S_BLUEFLAME, obj_130019C8);
			ObjMakeOffScale(2, 0, 0, 0, 8, object, S_BLUEFLAME, obj_130019C8);
		}
		ObjKill(object);
	}
}

void enemya_802B9034(void)
{
	object->o_shape = 10*RandF();
	object->o_vely = 30;
	object->o_velf = 20;
	object->o_f0 = object->s.scale[0];
	object->o_v1 = 64*RandF();
}

extern OBJLANG obj_13001850[];

void enemya_802B90EC(void)
{
	OBJECT *o;
	if (object->o_timer == 0) object->o_p3 = ObjectFindObj(obj_13001850);
	o = object->o_p3;
	object->o_velf = 15;
	object->o_density = -1;
	ObjectSetScale(object->o_f0);
	ObjSetHitInfo(object, &enemya_80330688);
	objectlib_802A2320();
	objectlib_802A2348(78);
	if (enemya_802B8434(300)) ObjKill(object);
	if (o)
	{
		if (o->o_action == OA_0)
		{
			if (ObjCalcDist2D(object, o) < 300) ObjKill(object);
		}
	}
}

extern OBJLANG obj_13001A30[];

void enemya_802B921C(void)
{
	OBJECT *o;
	int i;
	if (object->o_timer == 0)
	{
		object->o_angy = ObjCalcAngY(object, mario_obj);
		object->o_f1 = 5;
	}
	if (object->o_timer < 16)
	{
		if (!(object->o_timer & 1))
		{
			for (i = 0; i < 3; i++)
			{
				o = ObjMakeHere(object, S_BLUEFLAME, obj_13001A30);
				o->o_angy += DEG(120)*i;
				o->s.scale[0] = object->o_f1;
			}
			object->o_f1 -= 0.5;
		}
	}
	else
	{
		ObjKill(object);
	}
}

void enemya_802B935C(void)
{
	switch (object->o_mode)
	{
	case 0:
		ObjectSetAnimeV(0, 1);
		if (object->o_timer == 0)
		{
			float r;
			object->o_f3 = 0x800*RandSign();
			object->o_f0 = 2*RandF();
			object->o_v1 = (int)(30*RandF()) & 0xFE;
			r = 5*RandF();
			if (r < 2)  object->o_rotx = RandRange(0x80);
			else        object->o_rotx = 0;
		}
		object->o_velf = 3 + object->o_f0;
		if (object->o_timer >= 60+object->o_v1) object->o_mode++;
		if (object->o_timer < (60+object->o_v1)/2)
		{
			object->o_shapeangx += object->o_rotx;
		}
		else
		{
			object->o_shapeangx -= object->o_rotx;
		}
		object->o_vely = -SIN(object->o_shapeangx)*object->o_velf;
		break;
	case 1:
		ObjectSetAnimeV(0, 2);
		object->o_angy += object->o_f3;
		if (object->o_timer == 15) object->o_mode++;
		break;
	case 2:
		ObjectSetAnimeV(0, 1);
		if (object->o_timer >= 60+object->o_v1) object->o_mode++;
		if (object->o_timer < (60+object->o_v1)/2)
		{
			object->o_shapeangx -= object->o_rotx;
		}
		else
		{
			object->o_shapeangx += object->o_rotx;
		}
		break;
	case 3:
		ObjectSetAnimeV(0, 2);
		object->o_angy += object->o_f3;
		if (object->o_timer == 15) object->o_mode = 0;
		break;
	}
	object->o_vely = -SIN(object->o_shapeangx)*object->o_velf;
	ObjectProcMoveF();
	if (object->parent->o_mode == 2) ObjKill(object);
}

extern OBJLANG obj_13001B2C[];

void enemya_802B9790(void)
{
	OBJECT *o;
	int i;
	switch (object->o_mode)
	{
	case 0:
		if (object_80361250 == 15 || object_80361250 == 7)
		{
			for (i = 0; i < 15; i++)
			{
				o = ObjMakeOff(0, 300, 0, -200, object, S_FISH, obj_13001B2C);
				ObjRandOff3D(o, 200);
			}
			object->o_mode++;
		}
		break;
	case 1:
		if (!(object_80361250 == 15 || object_80361250 == 7)) object->o_mode++;
		break;
	case 2:
		object->o_mode = 0;
		break;
	}
}

void enemya_802B98D4(float *dst, float *src)
{
	dst[0] = src[0];
	dst[1] = src[1];
	dst[2] = src[2];
}

struct enemya4
{
	int offset;
	FVEC scale;
	float vel;
};

static struct enemya4 enemya_803306B4[] =
{
	{145, {0.7, 1.5, 0.7}, 7},
	{235, {1.2, 2, 1.2}, 11.6},
};

extern OBJLANG obj_13001B88[];

void enemya_802B98FC(void)
{
	int y, z, n, i;
	OBJECT *o;
	if (object->o_code == 0) object->o_code = 65;
	y = 10 * object->o_code;
	n = ObjGetArg(object) & 0xFF;
	for (i = 0; i < 2; i++)
	{
		if (i == 0) z = -enemya_803306B4[n].offset;
		else        z =  enemya_803306B4[n].offset;
		o = ObjMakeOff(i, 0, i*y, z, object, S_LIFT, obj_13001B88);
		o->o_f8 = enemya_803306B4[n].vel;
		enemya_802B98D4(o->s.scale, enemya_803306B4[n].scale);
	}
}

static void enemya_802B9A78(UNUSED int a0, float vely, int a2)
{
	object->o_angx = 0;
	object->o_rotx = 0;
	object->o_velf = 0;
	object->o_vely = vely;
	if (object->o_timer > a2) object->o_mode++;
}

static void enemya_802B9AF8(int a0, short a1)
{
	object->o_vely = 0;
	object->o_rotx = a1;
	if (object->o_timer+1 == 0x8000/abs(a1)) object->o_mode = a0;
	object->o_v1 = a0;
}

void enemya_802B9BB4(void)
{
	object->o_v2 = object->parent->o_code;
}

void enemya_802B9BD8(void)
{
	float speed = object->o_f8;
	object->o_v1 = 0;
	if (object->o_targetdist < 1000) ObjectLevelSound(NA_SE4_0D_00);
	switch (object->o_mode)
	{
	case 0:
		if (object->o_code == 0)    object->o_mode = 1;
		else                        object->o_mode = 3;
		break;
	case 1:
		enemya_802B9A78(2, 10, object->o_v2);
		break;
	case 2:
		enemya_802B9AF8(3, 0x200);
		break;
	case 3:
		enemya_802B9A78(4, -10, object->o_v2);
		break;
	case 4:
		enemya_802B9AF8(1, -0x200);
		break;
	}
	object->o_angx += abs(object->o_rotx);
	object->o_shapeangx += abs(object->o_rotx);
	object->o_shapeangy = object->o_angy;
	if (object->o_angx != 0)
	{
		object->o_velf = GetSign(object->o_rotx) * SIN(object->o_angx) * speed;
		object->o_vely = GetSign(object->o_rotx) * COS(object->o_angx) * speed;
	}
	if (object->o_v1 == 1)
	{
		object->o_rotx = 0;
		object->o_shapeangx &= ~0x7FFF;
		ObjectProcMoveF();
	}
	else ObjectProcMoveF();
	ObjectMapLoad();
}

extern MAP map_0707768C[];
extern MAP map_070775B4[];

void enemya_802B9E94(void)
{
	if (wave_8036131C & 2)  object->map = SegmentToVirtual(map_0707768C);
	else                    object->map = SegmentToVirtual(map_070775B4);
}

extern OBJLANG obj_13001C04[];

static void enemya_802B9EFC(void)
{
	OBJECT *o;
	switch (object->o_mode)
	{
	case 0:
		if (objectlib_802A3754())
		{
			object->o_mode++;
			objectlib_802A37AC();
		}
		break;
	case 1:
		if (object->o_timer < 4)    object->o_posy -= 20;
		else                        object->o_mode++;
		break;
	case 2:
		if ((o = ObjectFindObj(obj_13001C04)))
		{
			if (o->o_mode < 2) object->o_mode++;
		}
		break;
	case 3:
		if ((o = ObjectFindObj(obj_13001C04)))
		{
			if (o->o_mode >= 2)
			{
				object->o_mode++;
				BuSetFlag(BU_DRAIN);
				Na_Solution();
			}
		}
		break;
	case 4:
		ObjectLevelSound(NA_SE4_16);
		if (object->o_timer < 300)
		{
			water_table[2] = ApproachPos(water_table[2], -2450, 5);
			water_table[0] = ApproachPos(water_table[0], -2450, 5);
#ifdef MOTOR
			motor_8024C974(2);
#endif
		}
		else
		{
			object->o_mode++;
		}
		break;
	case 5:
		break;
	}
}

static void enemya_802BA13C(void)
{
	if (object->o_timer == 0)
	{
		object->o_posy -= 80;
		water_table[2] = -2450;
		water_table[0] = -2450;
	}
}

void enemya_802BA19C(void)
{
	if (BuGetFlag() & BU_DRAIN) object->o_v1 = 1;
}

void enemya_802BA1E0(void)
{
	if (object->o_v1)   enemya_802BA13C();
	else                enemya_802B9EFC();
	waterp[1+6*2+5] = water_table[2];
	waterp[1+6*0+5] = water_table[0];
}

void enemya_802BA25C(void)
{
	if (BuGetFlag() & BU_DRAIN)
	{
		waterp[1+6*0+5] = -800;
		waterp[1+6*1+5] = -800;
	}
}

void *Ctrl_enemya_802BA2B0(int code, SHAPE *shape, UNUSED void *data)
{
	if (code == SC_DRAW)
	{
		OBJECT *obj = (OBJECT *)draw_object;
		((SSCALE *)shape->next)->scale = obj->o_f0;
	}
	return NULL;
}

void enemya_802BA2F8(void)
{
	int frame = object->s.skel.frame;
	ObjectSetAnime(0);
	if      (frame < 38)    object->o_f0 = 0;
	else if (frame < 49)    object->o_f0 = 0.2;
	else if (frame < 58)    object->o_f0 = 0.2 + 0.11875F*(frame-53);
	else if (frame < 59)    object->o_f0 = 1.1;
	else if (frame < 60)    object->o_f0 = 1.05;
	else                    object->o_f0 = 1;
	if (object->o_timer > 150) ObjKill(object);
}

void enemya_802BA458(void)
{
	int frame = object->s.skel.frame;
	ObjectSetAnime(1);
	if      (frame <  38)   object->o_f0 = 0.2;
	else if (frame <  52)   object->o_f0 = 0.2 + 0.042857F*(frame-42);
	else if (frame <  94)   object->o_f0 = 0.8;
	else if (frame < 101)   object->o_f0 = 0.2 + 0.085714F*(101-frame);
	else                    object->o_f0 = 0.2;
	if (object->o_timer > 138) ObjKill(object);
}

void enemya_802BA5BC(void)
{
	if (BuGetFlag() & BU_DRAIN) ObjectSetShape(S_NULL);
	else                        ObjectMapLoad();
}

extern OBJLANG obj_13001C7C[];

#define BG_0 0

void enemya_802BA608(void)
{
	BGFACE *ground;
	unsigned short angz = object->o_shapeangz;
	object->o_ground_y = BGCheckGround(
		mario_obj->o_posx, mario_obj->o_posy, mario_obj->o_posz, &ground
	);
	if (object->o_mode == 0)
	{
		if (ground->code == BG_0 && object->o_timer > 3) object->o_mode++;
	}
	else if (object->o_mode == 1)
	{
		if (ground && (
			ground->code == BG_PORTL(11) ||
			ground->code == BG_PORTM(11) ||
			ground->code == BG_PORTR(11)
		))
		{
			if (ObjectHasScript(obj_13001C7C))
			{
				if      (angz < DEG(15)* 1) object_80361258 = 3; /*12:00-12:30*/
				else if (angz < DEG(15)*10) object_80361258 = 1; /*12:30- 5:00*/
				else if (angz < DEG(15)*14) object_80361258 = 2; /* 5:00- 7:00*/
				else if (angz < DEG(15)*23) object_80361258 = 0; /* 7:00-11:30*/
				else                        object_80361258 = 3; /*11:30-12:00*/
			}
			object->o_mode++;
		}
		else
		{
		}
	}
	if (object->o_mode < 2) ObjectRotateShape();
}

static void enemya_802BA7E0(void)
{
	if (object->o_code == 1)
	{
		if (objectlib_802A3F48())
		{
			ObjectSavePosStop();
			object->o_mode = 0;
		}
		else if (object->o_move & (OM_DIVE|OM_S_WATER|OM_U_WATER|OM_B_WATER))
		{
			object->o_mode = 5;
		}
	}
}

static int enemya_802BA868(void)
{
	if (object->o_code == 1)
	{
		if (PL_IsWearingDefCap(mario)) return TRUE;
	}
	return FALSE;
}

void *enemya_802BA8C4(int code, UNUSED SHAPE *shape, void *data)
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

static void enemya_802BA958(void)
{
	object->o_velf = 0;
	if (object->o_phase == 0)
	{
		object->o_phase = 1 + 4*RandF();
		object->work[O_V0].s[0] = 0;
		object->work[O_V0].s[1] = 2 + 4*RandF();
	}
	switch (object->o_phase)
	{
	case 1:
		ObjectSetAnime(9);
		if (objectlib_8029FF04()) object->o_phase = 0;
		break;
	case 2:
		ObjectSetAnime(4);
		if (objectlib_8029FF04()) object->work[O_V0].s[0]++;
		if (object->work[O_V0].s[0] >= 2*object->work[O_V0].s[1])
		{
			object->o_phase = 0;
		}
		break;
	case 3:
		ObjectSetAnime(5);
		if (objectlib_8029FF04()) object->work[O_V0].s[0]++;
		if (object->work[O_V0].s[0] >= object->work[O_V0].s[1])
		{
			object->o_phase = 0;
		}
		break;
	case 4:
		ObjectSetAnime(10);
		if (objectlib_8029FF04()) object->o_phase = 0;
		break;
	}
}

static void enemya_802BAB7C(void)
{
	enemya_802BA958();
	if (enemya_802BA868())
	{
		if (object->o_targetdist > 700 && object->o_targetdist < 1000)
		{
			object->o_mode = 1;
		}
		else if (object->o_targetdist <= 700 && object->o_targetdist > 200)
		{
			if (DeltaAng(object->o_targetang, object->o_angy) > 0x1000)
			{
				object->o_mode = 2;
			}
		}
	}
	else
	{
		if (object->o_targetdist < 300) object->o_mode = 1;
	}
	if (object->work[O_V8].s[0] == 2) object->o_mode = 4;
	if (object->work[O_V8].s[0] == 3)
	{
		object->o_angy = mario_obj->o_angy + 0x8000;
		if (enemya_802B14F4(50, 150)) object->o_mode = 3;
		else
		{
			object->o_angy = mario_obj->o_angy + 0x4000;
			if (enemya_802B14F4(50, 150)) object->o_mode = 3;
			else
			{
				object->o_angy = mario_obj->o_angy - 0x4000;
				if (enemya_802B14F4(50, 150)) object->o_mode = 3;
			}
		}
		object->work[O_V8].s[0] = 4;
	}
	if (object->o_code == 1)
	{
		if (object->o_posy < -1550) object->o_mode = 7;
	}
}

static void enemya_802BAE40(void)
{
	UNUSED int i;
	ObjectSetAnime(0);
	object->o_angy = ObjectAngToSave();
	object->o_velf = 10;
	if (object->o_posy > -1550) object->o_mode = 0;
}

static void enemya_802BAEC4(void)
{
	enemya_802BA958();
	if (objectlib_802A3F48())
	{
		ObjectSavePosStop();
		object->o_mode = 0;
	}
}

static void enemya_802BAF10(void)
{
	enemya_802BA958();
	if (object->o_phase == 3) ObjectTurn(object->o_targetang, 0x400);
}

static void enemya_802BAF64(void)
{
	int result;
	if (object->o_timer == 0) object->o_velf = 2 + 3*RandF();
	ObjectSetAnime(11);
	if ((result = ObjectTurn(object->o_targetang, 0x800))) object->o_mode = 0;
	if (enemya_802BA868())
	{
		if (object->o_targetdist > 500) object->o_mode = 1;
	}
	else
	{
		if (object->o_targetdist < 300) object->o_mode = 1;
	}
}

static void enemya_802BB07C(void)
{
	int sp1C = TRUE;
	short sp1A = object->o_targetang + 0x8000;
	if (enemya_802BA868())
	{
		sp1C = FALSE;
		sp1A = object->o_targetang;
	}
	if (object->o_timer == 0) object->o_f7 = 350 + 100*RandF();
	ObjectSetAnime(0);
	ObjectTurn(sp1A, 0x800);
	ObjectMatchP1Speed(20, 0.9F);
	if (sp1C)
	{
		if (object->o_targetdist > object->o_f7) object->o_mode = 2;
	}
	else
	{
		if (object->o_targetdist < object->o_f7) object->o_mode = 2;
	}
	if (sp1C && object->o_targetdist < 200)
	{
		if (object->o_move & OM_0200 && objectlib_802A404C(10))
		{
			object->o_mode = 3;
			object->o_angy = object->o_bg_ang;
		}
		else if (object->o_move & OM_0400 && objectlib_802A404C(10))
		{
			object->o_mode = 3;
			object->o_angy += 0x8000;
		}
	}
}

static void enemya_802BB288(void)
{
	object->o_velf = 10;
	ObjectHitOFF();
	if (object->o_phase == 0)
	{
		if (object->o_timer == 0)
		{
			ObjectSetAnimeJump(45 + 10*RandF(), 8);
		}
		else
		{
			if (object->o_move & (OM_BOUND|OM_TOUCH|OM_S_WATER|OM_B_WATER))
			{
				object->o_phase++;
				object->o_vely = 0;
			}
		}
	}
	else
	{
		object->o_velf = 0;
		ObjectSetAnime(7);
		ObjectHitON();
		if (objectlib_8029FF04()) object->o_mode = 1;
	}
}

static PATH enemya_803306DC[] =
{
	0, 1011, 2306, -285,
	0, 1151, 2304, -510,
	0, 1723, 1861, -964,
	0, 2082, 1775, -1128,
	0, 2489, 1717, -1141,
	0, 2662, 1694, -1140,
	0, 2902, 1536, -947,
	0, 2946, 1536, -467,
	0, 2924, 1536, 72,
	0, 2908, 1536, 536,
	0, 2886, 1536, 783,
	-1,
};

extern OBJLANG obj_13000F14[];

static void enemya_802BB3B8(void)
{
	OBJECT *o;
	float dist = 0;
	SHORT angy = 0;
	if ((o = ObjectFindObj(obj_13000F14)))
	{
		dist = ObjCalcDist2D(object, o->parent);
		angy = ObjCalcAngY(object, o->parent);
	}
	ObjectHitOFF();
	object->o_flag |= OF_0080;
	switch (object->o_phase)
	{
	case 0:
		ObjectSetAnime(0);
		object->o_p2 = enemya_803306DC;
		if (ObjectProcPath(0) != -1)
		{
			object->o_velf = 10;
			ObjectTurn(object->o_v6, 0x400);
			object->o_posy = object->o_ground_y;
		}
		else
		{
			object->o_velf = 0;
			object->o_phase++;
		}
		break;
	case 1:
		ObjectSetAnime(5);
		ObjectTurn(object->o_targetang, 0x400);
		if (objectlib_802A47A0(200, 30, 0x7FFF))    object->o_phase++;
		else                                        break;
		FALLTHROUGH;
	case 2:
		ObjectSetAnime(10);
		if (objectlib_802A4BE4(3, 1, 162, MSG_80)) object->o_phase++;
		break;
	case 3:
		ObjectSetAnime(0);
		if (ObjectTurn(angy, 0x400))
		{
			object->o_velf = 10;
			object->o_phase++;
		}
		break;
	case 4:
		ObjectSetAnimeJump(55, 8);
		object->o_velf = 36;
		object->o_phase++;
		break;
	case 5:
		if (dist < 50) object->o_velf = 0;
		if (object->o_move & OM_BOUND)
		{
			Na_Solution();
			ObjectSetAnime(5);
			object->o_phase++;
			object->work[O_V9].s[0] = 32;
			o->parent->o_var = 1;
			object->o_velf = 0;
		}
		break;
	case 6:
		object->o_angy += 0x800;
		object->work[O_V9].s[0]--;
		if (object->work[O_V9].s[0] < 0)
		{
			object->o_phase++;
			o->parent->o_var = 2;
		}
		break;
	case 7:
		if (object->o_posy < -1300) ObjKill(object);
		break;
	}
}

static STEPSOUND enemya_80330738[] =
{
	{1, 1, 10, NA_SE5_3B},
	{0, 0, 0, NA_SE_NULL},
	{0, 0, 0, NA_SE_NULL},
	{0, 0, 0, NA_SE_NULL},
	{1, 0, -1, NA_SE5_39},
	{1, 0, -1, NA_SE5_21},
	{0, 0, 0, NA_SE_NULL},
	{0, 0, 0, NA_SE_NULL},
	{1, 0, -1, NA_SE5_21},
	{1, 0, -1, NA_SE5_3C},
	{1, 0, -1, NA_SE5_3A},
	{0, 0, 0, NA_SE_NULL},
	{0, 0, 0, NA_SE_NULL},
};

static OBJCALL *enemya_803307A0[] =
{
	enemya_802BAB7C,
	enemya_802BB07C,
	enemya_802BAF64,
	enemya_802BB288,
	enemya_802BB3B8,
	enemya_802BAEC4,
	enemya_802BAF10,
	enemya_802BAE40,
};

static void enemya_802BB798(void)
{
	int sp1C;
	objectlib_802A2320();
	ObjectCallMode(enemya_803307A0);
	if (object->o_mode == 4 || object->o_mode == 7) sp1C = -88;
	else                                            sp1C = -20;
	objectlib_802A2348(sp1C);
	enemya_802BA7E0();
	if (!(object->o_move & (OM_DIVE|OM_S_WATER|OM_U_WATER|OM_B_WATER)))
	{
		ObjectStepSound(enemya_80330738);
	}
}

UNUSED
static void enemya_802BB838(void)
{
	if (gfx_frame % 50 < 7) object->o_shape = 1;
	else                    object->o_shape = 0;
}

static void enemya_802BB888(void)
{
	if (object->o_posy-object->o_savey > -100)
	{
		switch (object->work[O_V8].s[0])
		{
		case 0:
			if (pldemo_80257640(2) == 2)
			{
				MsgOpenPrompt(MSG_79);
				object->work[O_V8].s[0] = 1;
			}
			break;
		case 1:
			if (msg_answer)
			{
				pldemo_80257640(0);
				if (msg_answer == 1)
				{
					object->o_hit_flag |= HF_0040;
					object->work[O_V8].s[0] = 2;
				}
				else
				{
					object->work[O_V8].s[0] = 6;
					object->work[O_V8].s[1] = 60;
				}
			}
			break;
		case 2:
			break;
		case 6:
			if (object->work[O_V8].s[1]-- < 0) object->work[O_V8].s[0] = 0;
			break;
		}
	}
	else
	{
		object->work[O_V8].s[0] = 0;
		object->o_timer = 0;
		object->o_mode = 5;
	}
}

static void enemya_802BBA3C(void)
{
	switch (object->work[O_V8].s[0])
	{
	case 0:
		if (MarioStealCap(2))
		{
			object->work[O_V8].s[0] = 7;
			object->work[O_V9].s[1] |= 1;
		}
		else
		{
		}
		break;
	case 7:
		if (objectlib_802A4960(2, 2, MSG_100, 0))
		{
			object->o_hit_flag |= HF_0040;
			object->work[O_V8].s[0] = 3;
		}
		break;
	case 3:
		break;
	case 4:
		if (objectlib_802A4960(2, 18, MSG_101, 0))
		{
			MarioReturnCap();
			pldemo_80257640(0);
			object->work[O_V9].s[1] &= ~1;
			object->work[O_V8].s[0] = 5;
		}
		break;
	case 5:
		object->work[O_V8].s[0] = 0;
		object->o_mode = 0;
		break;
	}
}

void enemya_802BBB98(void)
{
	if (object->o_code == 1)
	{
		if (BuGetFlag() & BU_MONKEYCAP)
		{
			object->work[O_V8].s[0] = 4;
			object->work[O_V9].s[1] |= 1;
		}
	}
}

void enemya_802BBC0C(void)
{
	switch (object->o_action)
	{
	case OA_0:
		object->work[O_V8].s[1] = 0;
		enemya_802BB798();
		break;
	case OA_1:
		objectlib_802A01D8(12, 0);
		ObjCopyPos(object, mario_obj);
		if (object->o_code == 1)    enemya_802BBA3C();
		else                        enemya_802BB888();
		break;
	case OA_2:
	case OA_3:
		objectlib_802A0474();
		break;
	}
	if (object->work[O_V9].s[1] & 1)    object->o_shape = 2;
	else                                object->o_shape = 0;
	object->o_hit_result = 0;
	DbPrintErr("mode   %d\n", object->o_mode);
	DbPrintErr("action %d\n", object->o_action);
}

static int enemya_802BBD6C(short *data, int i)
{
	switch (data[i+0])
	{
	case 4:
		object->o_angy = data[i+2];
		object->o_velf = data[i+3]/100.0F;
		if (ObjectIsMarioBG())
		{
			i += 4;
			object->o_timer = 0;
		}
		break;
	case 2:
		object->o_angy = data[i+2];
		object->o_velf = data[i+3]/100.0F;
		if (object->o_timer > data[i+1])
		{
			i += 4;
			object->o_timer = 0;
		}
		break;
	case 1:
		Accelerate(&object->o_velf, data[i+2]/100.0F, data[i+3]/100.0F);
		if (object->o_timer > data[i+1])
		{
			i += 4;
			object->o_timer = 0;
		}
		break;
	case 3:
		object->o_velf = 0;
		i = 0;
		break;
	}
	return i;
}

static int enemya_802BBFD8(int *a0, float *a1, int a2, int a3)
{
	if (ObjectIsMarioBG())
	{
		if (*a0 < 0x4000)   *a0 += a2;
		else                *a0 = 0x4000;
	}
	else
	{
		if (*a0 > 0)    *a0 -= a2;
		else            *a0 = 0;
	}
	*a1 = a3*SIN(*a0);
	if (*a0 == 0 || *a0 == 0x4000)  return TRUE;
	else                            return FALSE;
}

static short enemya_803307C0[] =
{
	2,  30,  16384,   0,
	1, 220,    900,  30,
	1,  30,      0, -30,
	2,  30, -16384,   0,
	1, 220,    900,  30,
	1,  30,      0, -30,
	3,
};

static short enemya_803307F4[] =
{
	4,   0,      0,   0,
	1, 475,    900,  30,
	1,  30,      0, -30,
	2,  30, -32768,   0,
	1, 475,    900,  30,
	1,  30,      0, -30,
	3,
};

static short *enemya_80330828[] = {enemya_803307C0, enemya_803307F4};

void enemya_802BC0F0(void)
{
	if (object->o_mode == 0)
	{
		object->o_v1 = 0;
		object->o_mode++;
	}
	else
	{
		object->o_v1 = enemya_802BBD6C(
			enemya_80330828[object->o_code], object->o_v1
		);
	}
	DbPrint("number %d\n", object->o_v1);
	ObjectProcMoveF();
	if (enemya_802BBFD8(&object->o_v4, &object->o_f5, 0x400, -80))
	{
		object->o_v0 += 0x800;
		object->o_f3 -= SIN(object->o_v0)*2;
	}
	object->o_posy = object->o_f3 + object->o_savey + object->o_f5;
}

void enemya_802BC22C(void)
{
	enemya_802BBFD8(&object->o_v4, &object->o_f5, 0x7C, -110);
	object->o_shapeoff = 0;
	object->o_posy = object->o_savey + object->o_f5;
}

void enemya_802BC294(void)
{
	float sp24 = object->o_f0;
	float sp20 = object->o_f1;
	float sp1C = object->o_f2;
	ObjectSetPosOff(object->parent, sp24, sp20, sp1C);
	object->o_posy = object->parent->o_posy + 100;
	if (object->parent->o_mode == 3) ObjKill(object);
}

extern OBJLANG obj_13001DCC[];

static void enemya_802BC348(SHORT angy)
{
	OBJECT *o;
	UNUSED int n;
	int i, count;
	float x = 200*SIN(angy);
	float z = 200*COS(angy);
	if (object->o_code == 0)    count = 4;
	else                        count = 3;
	for (i = 0; i < count; i++)
	{
		o = ObjMakeHere(object, S_FLAME, obj_13001DCC);
		o->o_f0 += x;
		o->o_f1 = object->o_posy - 200;
		o->o_f2 += z;
		ObjSetScaleXYZ(o, 6, 6, 6);
		x += SIN(angy)*150;
		z += COS(angy)*150;
	}
}

static void enemya_802BC4F4(void)
{
	if (object->o_targetdist < 3000) object->o_mode = 1;
}

static void enemya_802BC538(void)
{
	enemya_802BC348(0);
	enemya_802BC348(-0x8000);
	object->o_roty = 0;
	object->o_angy = 0;
	object->o_mode = 2;
}

static void enemya_802BC590(void)
{
	object->o_roty = -0x100;
	object->o_angy += object->o_roty;
	if (object->o_targetdist > 3200) object->o_mode = 3;
}

static void enemya_802BC5FC(void)
{
	object->o_mode = 0;
}

static OBJCALL *enemya_80330830[] =
{
	enemya_802BC4F4,
	enemya_802BC538,
	enemya_802BC590,
	enemya_802BC5FC,
};

void enemya_802BC618(void)
{
	ObjectCallMode(enemya_80330830);
	if (object->o_code == 0) ObjectMapLoad();
}

void enemya_802BC660(void)
{
	if (object->o_timer == 0) object->o_posy -= 100;
	object->o_posy += SIN(object->o_v0)*3;
	object->o_v0 += 0x400;
	if (object->parent->o_mode == 2) ObjKill(object);
}

extern OBJLANG obj_13001E04[];

void enemya_802BC728(void)
{
	OBJECT *o;
	int i;
	switch (object->o_mode)
	{
	case 0:
		if (object->o_targetdist < 2500)
		{
			for (i = 1; i < 4; i++)
			{
				o = ObjMakeOff(0, 300*i-600, 0, 0, object, 53, obj_13001E04); /* T:shape */
				o->o_v0 = 0x1000*i;
			}
			object->o_mode = 1;
		}
		break;
	case 1:
		if (object->o_targetdist > 2600) object->o_mode = 2;
		break;
	case 2:
		object->o_mode = 0;
		break;
	}
}

void enemya_802BC898(void)
{
	ObjectCheckGroundY();
	ObjectCalcVelF();
	object->o_posx += object->o_velx;
	object->o_posz += object->o_velz;
	objectlib_802A0E68(-4, -0.7F, 2);
	if (object->o_move & (OM_BOUND|OM_TOUCH|OM_S_WATER|OM_U_WATER))
	{
		ObjKill(object);
	}
}

extern OBJLANG obj_13001E4C[];

static void enemya_802BC934(void)
{
	OBJECT *o;
	float scale;
	o = ObjMakeHere(object, S_FLAME, obj_13001E4C);
	o->o_posy += 550;
	o->o_angy = (short)Rand();
	o->o_velf = 20 + 40*RandF();
	o->o_vely = 10 + 50*RandF();
	scale = 3 + 6.0*RandF();
	ObjSetScaleXYZ(o, scale, scale, scale);
	if (RandF() < 0.1) ObjectPlaySound(NA_SE3_0C);
}

void enemya_802BCA74(void)
{
	UNUSED int i;
	object->o_checkdist = 4000;
	object->o_shapedist = 8000;
	switch (object->o_mode)
	{
	case 0:
		if (mario_obj->movebg == object) object->o_mode++;
		object->o_roty = 0x100;
		break;
	case 1:
		object->o_roty = 0x100 - 0x100*SIN(object->o_timer << 7);
		if (object->o_timer > 128) object->o_mode++;
		break;
	case 2:
		if (mario_obj->movebg != object) object->o_mode++;
		if (object->o_timer > 128) object->o_mode++;
		object->o_roty = 0;
		enemya_802BC934();
		break;
	case 3:
		object->o_roty = 0x100*SIN(object->o_timer << 7);
		if (object->o_timer > 128) object->o_mode = 0;
		break;
	case 4:
		object->o_mode = 0;
		break;
	}
	object->o_roty = -object->o_roty;
	object->o_angy += object->o_roty;
}

static void enemya_802BCCE8(float a0, int a1)
{
	switch (object->o_mode)
	{
	case 0:
		object->o_mode++;
		break;
	case 1:
		object->o_posy -= SIN(object->o_v0) * a0;
		object->o_v0 += a1;
		break;
	case 2:
		break;
		break;
	}
}

void enemya_802BCDA8(void)
{
	float sp1C = 0.4F;
	int sp18 = 0x100;
	if (object->o_angy)
	{
		enemya_802BCCE8(sp1C, sp18);
	}
	else
	{
		object->o_shapeangx = 0x200*SIN(object->o_v0);
		object->o_v0 += 0x100;
	}
}

void enemya_802BCE58(void)
{
	float sp1C = 0.5F;
	int sp18 = 0x100;
	enemya_802BCCE8(sp1C, sp18);
}

static void enemya_802BCE9C(FMTX m, float x, float y, float z)
{
	FVEC v, pos;
	pos[0] = object->o_posx;
	pos[1] = object->o_posy;
	pos[2] = object->o_posz;
	v[0] = x;
	v[1] = y;
	v[2] = z;
	FMtxStand(m, v, pos, 0);
}

void enemya_802BCF40(void)
{
	FMTX *m = &object->mtx;
	object->o_f0 = 0;
	object->o_f1 = 1;
	object->o_f2 = 0;
	enemya_802BCE9C(*m, 0, 1, 0);
}

static float enemya_802BCFC4(float a0, float a1, float a2)
{
	float sp04;
	if (a0 >= a1)
	{
		if (a0-a1 < a2) sp04 = a0;
		else            sp04 = a1 + a2;
	}
	else
	{
		if (a0-a1 > -a2)    sp04 = a0;
		else                sp04 = a1 - a2;
	}
	return sp04;
}

void enemya_802BD058(void)
{
	float dx, dy, dz, d;
	FVEC sp64, sp58, sp4C;
	float posx, posy, posz;
	int flag = 0;
	UNUSED int sp38;
	FMTX *m = &object->mtx;
	UNUSED FVEC sp28, sp1C;
	if (mario_obj->movebg == object)
	{
		Player1GetPos(&posx, &posy, &posz);
		sp64[0] = mario_obj->o_posx - object->o_posx;
		sp64[1] = mario_obj->o_posy - object->o_posy;
		sp64[2] = mario_obj->o_posz - object->o_posz;
		MtxTransform3(*m, sp58, sp64);
		dx = mario_obj->o_posx - object->o_posx;
		dy = 500;
		dz = mario_obj->o_posz - object->o_posz;
		d = DIST3(dx, dy, dz);
		if (d != 0)
		{
			d = 1.0 / d;
			dx *= d;
			dy *= d;
			dz *= d;
		}
		else
		{
			dx = 0;
			dy = 1;
			dz = 0;
		}
		if (object->o_v6 == 1) flag++;
		object->o_v6 = 1;
	}
	else
	{
		dx = 0;
		dy = 1;
		dz = 0;
		object->o_v6 = 0;
	}
	object->o_f0 = enemya_802BCFC4(dx, object->o_f0, 0.01F);
	object->o_f1 = enemya_802BCFC4(dy, object->o_f1, 0.01F);
	object->o_f2 = enemya_802BCFC4(dz, object->o_f2, 0.01F);
	enemya_802BCE9C(*m, object->o_f0, object->o_f1, object->o_f2);
	if (flag)
	{
		MtxTransform3(*m, sp4C, sp64);
		posx += sp4C[0] - sp58[0];
		posy += sp4C[1] - sp58[1];
		posz += sp4C[2] - sp58[2];
		Player1SetPos(posx, posy, posz);
	}
	object->s.m = m;
}

extern OBJLANG obj_13002DB0[];
extern OBJLANG obj_13002C60[];

static void enemya_802BD3E4(void)
{
	UNUSED int i;
	ObjMakeHere(object, S_RIPPLE_MOVE, obj_13002DB0);
	if (player_data[0].speed > 10)
	{
		OBJECT *o = ObjMakeHereScale(object, S_DROPLET, obj_13002C60, 1.5F);
		o->o_vely = 30*RandF();
		ObjRandOff2D(o, 110);
	}
}

void enemya_802BD488(void)
{
	if (object->o_timer == 0)
	{
		object->o_angy = Rand();
		object->o_vely = 30*RandF();
		object->o_gravity = -4;
		object->o_shape = 10*RandF();
		ObjRandOff2D(object, 110);
		object->o_f1 = 4;
	}
	ObjectCheckGroundY();
	ObjectProcMoveF();
	if (object->o_ground_y > object->o_posy || object->o_timer > 10)
	{
		ObjKill(object);
	}
	object->o_f1 += -0.3;
	ObjectSetScale(object->o_f1);
}

extern OBJLANG obj_13001F68[];

static void enemya_802BD5DC(void)
{
	int i;
	for (i = 0; i < 2; i++) ObjMakeHere(object, S_FLAME, obj_13001F68);
}

extern OBJLANG obj_13002AF0[];

static void enemya_802BD62C(float offy)
{
	OBJECT *o = ObjMakeHere(object, S_NULL, obj_13002AF0);
	o->o_posy += offy;
}

static HITINFO enemya_80330840 =
{
	/*type   */	HIT_SHELL,
	/*offset */	0,
	/*ap     */	4,
	/*hp     */	1,
	/*ncoin  */	1,
	/*hit r,h*/	50, 50,
	/*dmg r,h*/	50, 50,
};

void enemya_802BD680(void)
{
	BGFACE *ground;
	ObjSetHitInfo(object, &enemya_80330840);
	ObjectSetScale(1);
	switch (object->o_mode)
	{
	case 0:
		objectlib_802A2320();
		objectlib_802A452C();
		if (object->o_hit_result & HR_008000) object->o_mode++;
		object->o_shapeangy += 0x1000;
		objectlib_802A2348(-20);
		enemya_802BD62C(10);
		break;
	case 1:
		ObjCopyPos(object, mario_obj);
		ground = ObjectCheckGround();
		if (fabsf(
			BGCheckWater(object->o_posx, object->o_posz)-object->o_posy
		) < 10) enemya_802BD3E4();
		else if (fabsf(object->o_posy-object->o_ground_y) < 5)
		{
			if (ground && ground->code == BG_1) enemya_802BD5DC();
			else                                enemya_802BD62C(10);
		}
		else
		{
			enemya_802BD62C(10);
		}
		object->o_shapeangy = mario_obj->o_angy;
		if (object->o_hit_result & HR_400000)
		{
			ObjKill(object);
			objectlib_802A37AC();
			object->o_mode = 0;
		}
		break;
	}
	object->o_hit_result = 0;
}

static void enemya_802BD8D0(void)
{
	if (object->o_targetdist < 3000) objectlib_802A50FC(1);
}

static void enemya_802BD91C(float a0, float a1, short a2, short a3)
{
	object->o_posy =
		99.41124*SIN((float)(object->o_timer+1)/8*0x8000) + object->o_savey + 3;
	object->o_velf = a0;
	object->o_velu = a1;
	object->o_shapeangx += a2;
	if ((short)object->o_shapeangx < 0) a3 = -a3;
	object->o_shapeangz += a3;
	ObjectMoveULF();
	if (object->o_timer == 7)
	{
		object->o_mode = objectlib_802A3A88();
		ObjectPlaySound(NA_SE3_46);
	}
}

static void enemya_802BDB04(void)
{
	enemya_802BD91C(64, 0, 0x800, 0);
}

static void enemya_802BDB3C(void)
{
	enemya_802BD91C(-64, 0, -0x800, 0);
}

static void enemya_802BDB74(void)
{
	enemya_802BD91C(0, -64, 0, 0x800);
}

static void enemya_802BDBAC(void)
{
	enemya_802BD91C(0, 64, 0, -0x800);
}

static void enemya_802BDBE4(void)
{
	object->o_velf = 0;
	if (object->o_timer == 0) enemya_802BD8D0();
	object->o_posy = object->o_savey + 3;
	if (object->o_timer == 20) object->o_mode = objectlib_802A3A88();
}

static void enemya_802BDC7C(void)
{
	if (object->o_timer == 20) object->o_mode = objectlib_802A3A88();
}

static void enemya_802BDCC8(void)
{
	if (object->o_timer == 20) object->o_mode = objectlib_802A3A88();
}

static s8 enemya_80330850[] =
{
	4,1,4,1,6,1,6,1,5,1,5,1,6,1,6,1,
	5,1,2,4,1,4,1,4,1,2,5,1,5,1,7,1,
	7,1,4,1,4,1,7,1,7,1,5,1,5,1,5,1,
	2,4,1,-1,
};

static s8 enemya_80330884[] =
{
	4,1,4,1,7,1,7,1,7,1,2,6,1,6,1,6,
	1,5,1,5,1,6,1,5,1,5,1,2,4,1,4,1,
	7,1,-1,
};

static s8 enemya_803308A8[] =
{
	4,1,4,1,4,1,4,1,4,1,2,5,1,5,1,5,
	1,5,1,5,1,7,1,2,6,1,6,1,5,1,2,4,
	1,7,1,-1,
};

static s8 *enemya_803308CC[] =
{
	enemya_80330850,
	enemya_80330884,
	enemya_803308A8,
};

static void enemya_802BDD14(void)
{
	s8 *table = enemya_803308CC[object->o_code];
	object->o_mode = objectlib_802A3A4C(table);
}

static OBJCALL *enemya_803308D8[] =
{
	enemya_802BDD14,
	enemya_802BDBE4,
	enemya_802BDC7C,
	enemya_802BDCC8,
	enemya_802BDB04,
	enemya_802BDB3C,
	enemya_802BDB74,
	enemya_802BDBAC,
};

void enemya_802BDD68(void)
{
	ObjectCallMode(enemya_803308D8);
	ObjectMapLoad();
}

static int enemya_802BE49C(void);

static void enemya_802BDD9C(void)
{
	ObjectHitOFF();
	ObjectSetAnime(8);
#if REVISION >= 199609
	ObjectSetScale(1);
#endif
	if (object->o_targetdist < 1200) object->o_mode = 1;
}

extern OBJLANG obj_130000F8[];

static int enemya_802BDE10(void)
{
	int i, result = TRUE;
	if (object->o_hit_result & HR_008000)
	{
		Na_SeqPull(50);
		if (object->o_hit_result & HR_004000)
		{
			ObjectPlaySound(NA_SE9_11);
			for (i = 0; i < 20; i++)
			{
				ObjMakeHere(object, S_BUBBLE_B, obj_130000F8);
			}
			object->o_mode = 5;
		}
		else
		{
			object->o_mode = 3;
		}
		object->o_hit_result = 0;
	}
	else
	{
		result = FALSE;
	}
	return result;
}

static void enemya_802BDEEC(void)
{
	ObjectHitON();
	object->o_hit_type = 0x8000;
	ObjectSetAnime(8);
	ObjectSetHitBox(250, 200);
	ObjectSetDmgBox(150, 100);
#if REVISION == 199703
	object->o_ap = 3;
#elif REVISION >= 199609
	object->o_ap = 0;
#endif
	if (object->o_targetdist < 400)
	{
		if (enemya_802BE49C()) object->o_mode = 3;
	}
	else if (object->o_targetdist < 1000)
	{
		Na_SeqPush(NA_BGM_LULLABY, 0, 0xFF, 1000);
		object->o_v0 = 0;
	}
	else
	{
		if (object->o_v0 == 0)
		{
			object->o_v0++;
			Na_SeqPull(50);
		}
	}
	enemya_802BDE10();
}

static void enemya_802BE034(void)
{
#if REVISION >= 199609
	object->o_ap = 3;
#endif
	if (object->o_timer == 0) Na_SeqPull(50);
	if (!enemya_802BDE10() && object->o_timer > 10) object->o_mode = 2;
}

#if REVISION >= 199609
static void enemya_802BE0B8(void)
{
	if (object->flag & OBJ_0002) object->o_mode = 0;
}
#endif

static void enemya_802BE0EC(void)
{
	ObjectHitOFF();
	ObjectSetAnime(2);
	object->o_hit_result = 0;
	if (objectlib_8029FF04()) object->o_mode = 6;
#if REVISION >= 199609
	enemya_802BE0B8();
#endif
}

static void enemya_802BE150(void)
{
	if (object->o_timer == 0)
	{
		ObjectPlaySound(NA_SE5_74);
		object->o_f1 = 1;
	}
	if (object->o_f1 > 0)
	{
		object->o_f1 -= 0.04;
	}
	else
	{
		object->o_f1 = 0;
		objectlib_802A5524();
		object->o_mode = 7;
	}
	ObjectSetScale(object->o_f1);
#if REVISION >= 199609
	enemya_802BE0B8();
#endif
}

static void enemya_802BE234(void)
{
	if (object->o_targetdist > 1200) object->o_mode = 8;
}

static void enemya_802BE278(void)
{
	ObjectSetAnime(8);
	if (object->o_timer == 0) object->o_f1 = 0.3F;
	if (object->o_f1 < 1.0)
	{
		object->o_f1 += 0.02;
	}
	else
	{
		object->o_f1 = 1;
		object->o_mode = 0;
	}
	ObjectSetScale(object->o_f1);
}

static s8 enemya_803308F8[] = {12, 28, 50, 64, -1};

static void enemya_802BE350(void)
{
	int frame = object->s.skel.frame;
	ObjectHitON();
	object->o_hit_type = 8;
	ObjectSetAnime(0);
	ObjectSetHitBox(150, 100);
	ObjectSetDmgBox(150, 100);
	if (InTable(frame, enemya_803308F8)) ObjectPlaySound(NA_SE9_10);
	object->o_angy = ApproachAng(object->o_angy, object->o_targetang, 0x400);
	if (object->o_targetdist > 500 && objectlib_8029FF04()) object->o_mode = 4;
	if (object->o_hit_result & HR_008000)
	{
		if (mario->flag & PL_METALCAP) object->o_mode = 5;
	}
}

static int enemya_802BE49C(void)
{
	if (player_data[0].vel[1] > 10) return TRUE;
	if (player_data[0].speed > 10) return TRUE;
	return FALSE;
}

static void enemya_802BE50C(void)
{
	ObjectHitOFF();
	ObjectSetAnime(6);
	if (objectlib_8029FF04()) object->o_mode = 1;
	if (object->o_targetdist < 400 && enemya_802BE49C()) object->o_mode = 2;
}

static OBJCALL *enemya_80330900[] =
{
	enemya_802BDD9C,
	enemya_802BDEEC,
	enemya_802BE350,
	enemya_802BE034,
	enemya_802BE50C,
	enemya_802BE0EC,
	enemya_802BE150,
	enemya_802BE234,
	enemya_802BE278,
};

void enemya_802BE5A0(void)
{
	ObjectCallMode(enemya_80330900);
	if (stage_index == STAGE_WF)
	{
		if (mario_obj->o_posy > 3400) ObjectHide();
		else ObjectShow();
	}
	object->o_hit_result = 0;
}

static void enemya_802BE628(
	SHORT shape, OBJLANG *script, float offx, float offz, CHAR mode, s8 *data
)
{
	OBJECT *sp1C = ObjMakeHere(object, shape, script);
	sp1C->o_posx += offx;
	sp1C->o_posy += 50;
	sp1C->o_posz += offz;
	sp1C->o_mode = mode;
	sp1C->o_p6 = data;
	sp1C->o_p7 = data;
}

static s8 enemya_80330924[] =
	{2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,2,-1};
static s8 enemya_80330940[] =
	{2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,2,2,-1};
static s8 enemya_8033095C[] =
	{2,2,2,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,2,2,2,-1};
static s8 enemya_80330978[] =
	{2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,2,2,2,2,-1};
static s8 enemya_80330994[] =
	{2,2,2,2,2,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,2,2,2,2,2,-1};
static s8 enemya_803309B0[] =
	{2,2,2,2,2,2,4,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,-1};
static s8 enemya_803309CC[] =
	{2,2,2,2,2,2,2,5,2,2,2,2,2,2,2,2,2,2,6,2,2,2,2,2,2,2,-1};
static s8 enemya_803309E8[] =
	{2,2,2,2,2,2,2,2,4,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,-1};
static s8 enemya_80330A04[] =
	{2,2,2,2,2,2,2,2,2,6,2,2,2,2,2,2,5,2,2,2,2,2,2,2,2,2,-1};
static s8 enemya_80330A20[] =
	{2,2,2,2,2,2,2,2,2,2,4,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,-1};
static s8 enemya_80330A3C[] =
	{2,2,2,2,2,2,2,2,2,2,2,6,2,2,5,2,2,2,2,2,2,2,2,2,2,2,-1};
static s8 enemya_80330A58[] =
	{2,2,2,2,2,2,2,2,2,2,2,2,3,4,2,2,2,2,2,2,2,2,2,2,2,2,-1};
static s8 enemya_80330A74[] =
	{2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,-1};
static s8 enemya_80330A90[] =
	{2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,-1};

struct enemya5
{
	u8 shape;
	s8 offx;
	s8 offz;
	s8 mode;
	s8 *data;
};

static struct enemya5 enemya_80330AAC[] =
{
	{67,  -5, -15, 1, enemya_80330924}, /* T:shape */
	{68,   5, -15, 0, enemya_80330940}, /* T:shape */
	{69, -15,  -5, 0, enemya_80330A3C}, /* T:shape */
	{70,  -5,  -5, 0, enemya_80330A58}, /* T:shape */
	{71,   5,  -5, 0, enemya_8033095C}, /* T:shape */
	{72,  15,  -5, 0, enemya_80330978}, /* T:shape */
	{73, -15,   5, 0, enemya_80330A20}, /* T:shape */
	{74,  -5,   5, 0, enemya_80330A04}, /* T:shape */
	{75,   5,   5, 0, enemya_803309B0}, /* T:shape */
	{76,  15,   5, 0, enemya_80330994}, /* T:shape */
	{77, -15,  15, 0, enemya_80330A74}, /* T:shape */
	{78,  -5,  15, 0, enemya_803309E8}, /* T:shape */
	{79,   5,  15, 0, enemya_803309CC}, /* T:shape */
	{80,  15,  15, 0, enemya_80330A90}, /* T:shape */
};

extern OBJLANG obj_13002038[];

static void enemya_802BE6D4(float a0)
{
	int i;
	for (i = 0; i < 14; i++) enemya_802BE628(
		enemya_80330AAC[i].shape, obj_13002038,
		enemya_80330AAC[i].offx*a0/10,
		enemya_80330AAC[i].offz*a0/10,
		enemya_80330AAC[i].mode,
		enemya_80330AAC[i].data
	);
	object->o_mode++;
}

extern OBJLANG obj_130009A4[];

void enemya_802BE79C(void)
{
	int i;
	switch (object->o_mode)
	{
	case 0:
		enemya_802BE6D4(480);
		break;
	case 1:
		if (object->o_v0 == 3 && object->o_targetdist < 1000)
		{
			for (i = 0; i < 5; i++)
			{
				UNUSED OBJECT *o = ObjMakeHere(object, S_COIN, obj_130009A4);
			}
			object->o_v0 = 0;
			object->o_mode++;
		}
		break;
	case 2:
		break;
	}
}

static void enemya_802BE8A8(void)
{
}

static void enemya_802BE8B8(void)
{
	object->o_posy += 50;
	object->o_mode = 3;
}

static void enemya_802BE8F4(void)
{
	s8 *data = object->o_p7;
	if (mario_obj->movebg == object) object->parent->o_v0 = 1;
	if (!object->o_v5)
	{
		ObjectInitMode(*data);
		data++;
		object->o_p7 = data;
		if (*data == -1)
		{
			object->parent->o_v0 |= 2;
			object->o_v7 = object->o_v6;
		}
		object->o_v5 = TRUE;
	}
}

static void enemya_802BE9DC(float a0, float a1, int a2, UNUSED int a3)
{
	if (object->o_timer < 20)
	{
		if (object->o_timer % 2) object->o_f3 = 0;
		else object->o_f3 = -6;
	}
	else
	{
		if (object->o_timer == 20)
		{
			ObjectPlaySound(NA_SE9_19);
		}
		if (object->o_timer < 20+a2)
		{
			object->o_f2 += a0;
			object->o_f4 += a1;
		}
		else
		{
			object->o_mode = 2;
			object->o_v5 = 0;
		}
	}
}

static void enemya_802BEB14(void)
{
	UNUSED int sp04;
	if (object->o_timer < 24)   sp04 = 0;
	else                        object->o_v5 = 0;
}

static void enemya_802BEB54(void)
{
	enemya_802BE9DC(-120, 0, 4, 4);
}

static void enemya_802BEB8C(void)
{
	enemya_802BE9DC(120, 0, 4, 5);
}

static void enemya_802BEBC4(void)
{
	enemya_802BE9DC(0, -120, 4, 6);
}

static void enemya_802BEBFC(void)
{
	enemya_802BE9DC(0, 120, 4, 3);
}

static OBJCALL *enemya_80330B1C[] =
{
	enemya_802BE8A8,
	enemya_802BE8B8,
	enemya_802BEB14,
	enemya_802BEB54,
	enemya_802BEB8C,
	enemya_802BEBC4,
	enemya_802BEBFC,
};

void enemya_802BEC34(void)
{
	enemya_802BE8F4();
	ObjectCallMode(enemya_80330B1C);
	object->o_posx = object->o_f2 + object->o_savex;
	object->o_posy = object->o_f3 + object->o_savey;
	object->o_posz = object->o_f4 + object->o_savez;
}

static int enemya_802BECB0(SHORT a0, SHORT a1, Na_Se se)
{
	float speed;
	if ((speed = object->s.skel.vspeed/65536.0F) == 0) speed = 1;
	if (
		ObjectIsAnimeFrameRange(a0, speed) ||
		ObjectIsAnimeFrameRange(a1, speed)
	)
	{
		ObjectPlaySound(se);
		return TRUE;
	}
	return FALSE;
}

void enemya_802BED7C(int flag)
{
	if (object->o_anime == 0)
	{
		Na_Se se = !flag ? NA_SE5_02 : NA_SE5_09;
		enemya_802BECB0(1, 11, se);
	}
}

extern OBJLANG obj_130020E0[];
extern OBJLANG obj_130020E8[];

static void enemya_802BEDEC(void)
{
	float dist;
	UNUSED int i;
	OBJECT *o = ObjectFind(obj_130020E8, &dist);
	if (ObjectFindTake(obj_130020E0, 1000))
	{
		if (object->o_phase == 0)
		{
			ObjectSetAnime(0);
			object->o_velf = 10;
			if (ObjectDistMarioToSave() > 800) object->o_phase = 1;
			ObjectTurn(object->o_targetang, 0x400);
		}
		else
		{
			object->o_velf = 0;
			ObjectSetAnime(3);
			if (ObjectDistMarioToSave() < 700) object->o_phase = 0;
		}
	}
	else
	{
		object->o_velf = 0;
		ObjectSetAnime(3);
	}
	if (o && dist < 300 && o->o_action != OA_0)
	{
		object->o_mode = 1;
		o->o_var = 1;
		object->child = o;
	}
}

extern OBJLANG obj_130020D8[];

static void enemya_802BEF8C(void)
{
	switch (object->o_phase)
	{
	case 0:
		ObjectSetAnime(3);
		if (!ObjectIsMarioBG())
		{
			int self_code = object->o_actorinfo >> 16 & 0xFF;
			int child_code = object->child->o_actorinfo >> 16 & 0xFF;
			int msg;
			if (self_code == child_code)    msg = MSG_58;
			else                            msg = MSG_59;
			if (objectlib_802A4BE4(2, 1, 162, msg))
			{
				if (msg == MSG_58)  object->o_phase = 1;
				else                object->o_phase = 2;
				object->child->o_hit_flag |= HF_0040;
			}
		}
		else
		{
			ObjectSetAnime(0);
		}
		break;
	case 1:
		if (object->child->o_action == OA_0)
		{
			object->child->work[object->o_hit_flag].i &= ~HF_0040;
			ObjSetScript(object->child, obj_130020E0);
#if REVISION >= 199609
			objectlib_802A5588(3167, -4300, 5108, 200);
#else
			enemyb_802F2B88(3167, -4300, 4650);
#endif
			object->o_mode = 2;
		}
		break;
	case 2:
		if (object->child->o_action == OA_0)
		{
			object->child->work[object->o_hit_flag].i &= ~HF_0040;
			ObjSetScript(object->child, obj_130020D8);
			object->o_mode = 2;
		}
		break;
	}
}

static void enemya_802BF1D8(void)
{
	int flag = FALSE;
	float dist;
	OBJECT *o = ObjectFind(obj_130020E8, &dist);
	ObjectSetScale(4);
	ObjectSetAnime(3);
	if (dist < 500) flag = TRUE;
	if (o && dist < 300 && o->o_action != OA_0)
	{
		object->o_mode = 1;
		o->o_var = 1;
		object->child = o;
	}
	else
	{
		switch (object->o_phase)
		{
		case 0:
			if (objectlib_802A48BC(300, 100) && !flag) object->o_phase++;
			break;
		case 1:
			if (objectlib_802A4BE4(2, 1, 162, MSG_57)) object->o_phase++;
			break;
		case 2:
			if (object->o_targetdist > 450) object->o_phase = 0;
			break;
		}
	}
	if (ObjectIsAnimeFrame(1)) ObjectPlaySound(NA_SE5_2D);
}

static OBJCALL *enemya_80330B38[] =
{
	enemya_802BF1D8,
	enemya_802BEF8C,
	enemya_802BEDEC,
};

void enemya_802BF3C0(void)
{
	object->flag |= OBJ_0400;
	objectlib_802A2320();
	ObjectCallMode(enemya_80330B38);
	objectlib_802A2348(-78);
	enemya_802BED7C(TRUE);
	object->o_hit_result = 0;
}

static void enemya_802BF424(void)
{
	if (objectlib_802A0154())
	{
		object->o_v3 = object->o_mode;
		object->o_mode = 3;
	}
}

extern OBJLANG obj_13002088[];

static void enemya_802BF474(void)
{
	int flag = FALSE;
	if (object->o_timer == 0)
	{
		if (ObjectFindDist(obj_13002088) < 1000) flag = TRUE;
	}
	ObjectSetAnime(0);
	object->o_velf = 3 + object->o_f4;
	ObjectTurn(object->o_targetang+0x8000, 0x600+object->o_v7);
	if (object->o_targetdist > object->o_f5+500) object->o_mode = 0;
	enemya_802BF424();
	if (flag) object->o_mode = 5;
}

static void enemya_802BF57C(void)
{
	ObjectSetAnime(0);
	object->o_velf = 3 + object->o_f4;
	ObjectTurn(object->o_targetang, 0x600+object->o_v7);
	if (object->o_targetdist < object->o_f5+300) object->o_mode = 0;
	if (object->o_targetdist > 1100) object->o_mode = 0;
	enemya_802BF424();
}

static void enemya_802BF648(void)
{
	if (object->o_timer >= 6)
	{
		if (object->o_timer == 6) ObjectPlaySound(NA_SE5_1F);
		ObjectSetAnime(1);
		if (object->o_timer > 25)
		{
			if (!objectlib_802A0154()) object->o_mode = 4;
		}
	}
}

static void enemya_802BF6E4(void)
{
	if (object->o_timer > 20)
	{
		object->o_velf = 0;
		ObjectSetAnime(2);
		if (object->o_timer > 40) object->o_mode = object->o_v3;
	}
}

static void enemya_802BF760(void)
{
	int flag = FALSE;
	ObjectSetAnime(3);
	if (object->o_timer == 0)
	{
		object->o_v7 = 0x400*RandF();
		object->o_f5 = 100*RandF();
		object->o_f4 = RandF();
		object->o_velf = 0;
		if (ObjectFindDist(obj_13002088) < 1000) flag = TRUE;
	}
	if (object->o_targetdist < 1000 && object->o_f5+600 < object->o_targetdist)
	{
		object->o_mode = 1;
	}
	else if (object->o_targetdist < object->o_f5+300)
	{
		object->o_mode = 2;
	}
	if (flag) object->o_mode = 5;
	if (objectlib_802A3F48()) ObjectSavePos();
}

static void enemya_802BF90C(void)
{
	float dist;
	SHORT angy;
	OBJECT *o;
	if ((o = ObjectFindObj(obj_13002088)))
	{
		if (object->o_targetdist < 1000)    object->o_velf = 2;
		else                                object->o_velf = 0;
		dist = ObjCalcDist3D(object, o);
		angy = ObjCalcAngY(object, o);
		if (dist > 200) ObjectTurn(angy,        0x400);
		else            ObjectTurn(angy+0x8000, 0x400);
		ObjectSetAnime(0);
	}
	enemya_802BF424();
}

static OBJCALL *enemya_80330B44[] =
{
	enemya_802BF760,
	enemya_802BF57C,
	enemya_802BF474,
	enemya_802BF648,
	enemya_802BF6E4,
	enemya_802BF90C,
};

static void enemya_802BFA14(void)
{
	if (object->o_var != 0)
	{
		object->o_mode = 5;
		object->o_var = 0;
	}
	objectlib_802A2320();
	ObjectCallMode(enemya_80330B44);
	objectlib_802A2348(-78);
	enemya_802BED7C(FALSE);
}

void enemya_802BFA88(void)
{
	switch (object->o_action)
	{
	case OA_0:
		enemya_802BFA14();
		break;
	case OA_1:
		objectlib_802A01D8(0, 0);
		if (ObjectHasScript(obj_130020D8)) ObjSetScript(object, obj_130020E8);
		ObjCopyPos(object, mario_obj);
#if REVISION >= 199609
		if (!(gfx_frame % 30)) Na_ObjSePlay(NA_SE9_45, mario_obj);
#else
		if (!(gfx_frame % 30)) Na_ObjSePlay(NA_SE9_45, object);
#endif
		break;
	case OA_2:
		objectlib_802A0380(0, 0, 0);
		break;
	case OA_3:
		objectlib_802A0474();
		break;
	}
}

void *Ctrl_enemya_802BFBAC(int code, SHAPE *shape, UNUSED void *data)
{
	if (code == SC_DRAW)
	{
		OBJECT *obj = (OBJECT *)draw_object;
		SSELECT *shp = (SSELECT *)shape;
		int frame;
		shp->index = 0;
		frame = gfx_frame % 50;
		if      (frame < 43) shp->index = 0;
		else if (frame < 45) shp->index = 1;
		else if (frame < 47) shp->index = 2;
		else                 shp->index = 1;
		if (obj->script == SegmentToVirtual(obj_13002088))
		{
			if (obj->o_velf > 5) shp->index = 3;
		}
	}
	return NULL;
}

extern ANIME *anime_piranha[];
extern ANIME *anime_fish[];
extern OBJLANG obj_13002178[];

static void enemya_802BFCD8(void)
{
	int i, n;
	SHORT shape;
	float d;
	ANIME **anime;
	switch (object->o_code)
	{
	case 0: shape = S_FISH;    n = 20; d = 1500; anime = anime_fish;    break;
	case 1: shape = S_FISH;    n =  5; d = 1500; anime = anime_fish;    break;
	case 2: shape = S_PIRANHA; n = 20; d = 1500; anime = anime_piranha; break;
	case 3: shape = S_PIRANHA; n =  5; d = 1500; anime = anime_piranha; break;
#ifdef __GNUC__
	default: return;
#endif
	}
	if (object->o_targetdist < d || stage_index == STAGE_SA)
	{
		for (i = 0; i < n; i++)
		{
			OBJECT *o = ObjMakeHere(object, shape, obj_13002178);
			o->o_code = object->o_code;
			ObjInitAnime(o, anime, 0);
			ObjRandOff3D(o, 700);
		}
		object->o_mode = 1;
	}
}

static void enemya_802BFEB8(void)
{
	if (stage_index != STAGE_SA)
	{
		if (mario_obj->o_posy-object->o_posy > 2000) object->o_mode = 2;
	}
}

static void enemya_802BFF20(void)
{
	object->o_mode = 0;
}

static OBJCALL *enemya_80330B5C[] =
{
	enemya_802BFCD8,
	enemya_802BFEB8,
	enemya_802BFF20,
};

void enemya_802BFF3C(void)
{
	ObjectCallMode(enemya_80330B5C);
}

static void enemya_802BFF68(int a0)
{
	float parenty = object->parent->o_posy;
	if (stage_index == STAGE_SA)
	{
		if (fabsf(object->o_posy-object->o_f1) > 500) a0 = 10;
		object->o_posy = ApproachPos(object->o_posy, object->o_f1, a0);
	}
	else
	{
		if (
			parenty-100-object->o_f6 < object->o_posy &&
			object->o_posy < parenty+1000+object->o_f6
		) object->o_posy = ApproachPos(object->o_posy, object->o_f1, a0);
	}
}

static void enemya_802C00B4(void)
{
	float dy = object->o_posy - mario_obj->o_posy;
	if (object->o_timer < 10)   ObjectSetAnimeV(0, 2);
	else                        ObjectSetAnimeV(0, 1);
	if (object->o_timer == 0)
	{
		object->o_velf = 3 + 2*RandF();
		if (stage_index == STAGE_SA)    object->o_f2 = 700*RandF();
		else                            object->o_f2 = 100*RandF();
		object->o_f4 = 200 + 500*RandF();
	}
	object->o_f1 = mario_obj->o_posy + object->o_f2;
	ObjectTurn(object->o_targetang, 0x400);
	if (object->o_posy < object->o_f0-50)
	{
		if (dy < 0) dy = 0-dy;
		if (dy < 500)   enemya_802BFF68(2);
		else            enemya_802BFF68(4);
	}
	else
	{
		object->o_posy = object->o_f0 - 50;
		if (dy > 300) object->o_posy -= 1;
	}
	if (object->o_targetdist < object->o_f4+150) object->o_mode = 2;
}

static void enemya_802C0348(void)
{
	float dy = object->o_posy - mario_obj->o_posy;
	object->o_f1 = mario_obj->o_posy + object->o_f2;
	if (object->o_timer == 0)
	{
		int sp18;
		object->o_f7 = 300*RandF();
		object->o_v3 = 0x400 + 0x400*RandF();
		object->o_f5 = 8 + 4*RandF() + 5;
		if (object->o_targetdist < 600) sp18 = 1;
		else                            sp18 = 1 / (object->o_targetdist/600.0);
		sp18 *= 0x7F;
		ObjectPlaySound(NA_SE3_09);
	}
	if (object->o_timer < 20)   ObjectSetAnimeV(0, 4);
	else                        ObjectSetAnimeV(0, 1);
	if (object->o_velf < object->o_f5) object->o_velf += 0.5;
	object->o_f1 = mario_obj->o_posy + object->o_f2;
	ObjectTurn(object->o_targetang+0x8000, object->o_v3);
	if (object->o_posy < object->o_f0-50)
	{
		if (dy < 0) dy = 0-dy;
		if (dy < 500)   enemya_802BFF68(2);
		else            enemya_802BFF68(4);
	}
	else
	{
		object->o_posy = object->o_f0 - 50;
		if (dy > 300) object->o_posy -= 1;
	}
	if (object->o_targetdist > object->o_f7+500) object->o_mode = 1;
}

static void enemya_802C06A8(void)
{
	ObjectSetAnimeV(0, 1);
	object->s.skel.frame = 28*RandF();
	object->o_f6 = 300*RandF();
	ObjectSetScale(0.8 + 0.4*RandF());
	object->o_mode = 1;
}

static OBJCALL *enemya_80330B68[] =
{
	enemya_802C06A8,
	enemya_802C00B4,
	enemya_802C0348,
};

void enemya_802C0768(void)
{
	UNUSED FVEC v;
	ObjectSetScale(1);
	object->o_f0 = BGCheckWater(object->o_posx, object->o_posz);
	if (stage_index == STAGE_SA) object->o_f0 = 0;
	object->o_wall_r = 30;
	ObjectCheckWall();
	if (stage_index != STAGE_32)
	{
		if (object->o_f0 < -10000)
		{
			ObjKill(object);
			return;
		}
	}
	else
	{
		object->o_f0 = 1000;
	}
	ObjectCallMode(enemya_80330B68);
	ObjectProcMoveF();
	if (object->parent->o_mode == 2) ObjKill(object);
}

void enemya_802C08A8(void)
{
	object->o_vely = 0;
	if (object->o_mode == 0)
	{
		if (ObjectIsMarioBG()) object->o_mode++;
	}
	else if (object->o_mode == 1)
	{
		object->o_vely = -20;
		object->o_posy += object->o_vely;
		ObjectLevelSound(NA_SE4_0D_00);
		if (object->o_timer > 132) object->o_mode++;
	}
	else if (object->o_mode == 2)
	{
		if (object->o_timer > 110) object->o_mode++;
	}
	else if (object->o_mode == 3)
	{
		object->o_vely = 10;
		object->o_posy += object->o_vely;
		ObjectLevelSound(NA_SE4_0D_00);
		if (object->o_posy >= object->o_savey)
		{
			object->o_posy = object->o_savey;
			object->o_mode++;
		}
	}
	else
	{
		if (!ObjectIsMarioBG()) object->o_mode = 0;
	}
}

extern OBJLANG obj_1300220C[];

static void enemya_802C0AAC(void)
{
	int i, count = object->o_v0;
	if (object->o_targetdist < 1500)
	{
		/* T:shape */
		for (i = 0; i < count; i++) ObjMakeHere(object, 100, obj_1300220C);
		object->o_mode = 1;
	}
}

static void enemya_802C0B50(void)
{
	if (mario_obj->o_posy-object->o_posy > 2000) object->o_mode = 2;
}

static void enemya_802C0BA4(void)
{
	object->o_mode = 3;
}

static void enemya_802C0BC4(void)
{
	object->o_mode = 0;
}

static OBJCALL *enemya_80330B74[] =
{
	enemya_802C0AAC,
	enemya_802C0B50,
	enemya_802C0BA4,
	enemya_802C0BC4,
};

void enemya_802C0BE0(void)
{
	ObjectCallMode(enemya_80330B74);
}

static void enemya_802C0C0C(int a0)
{
	float parenty = object->parent->o_posy;
	if (
		parenty-100-object->o_f4 < object->o_posy &&
		object->o_posy < parenty+1000+object->o_f4
	) object->o_posy = ApproachPos(object->o_posy, object->o_f1, a0);
	else {}
}

static void enemya_802C0CD4(void)
{
	object->o_f2 = 100*RandF();
	object->o_f4 = 300*RandF();
	object->o_mode = 1;
}

static void enemya_802C0D44(void)
{
	float dy;
	if (object->o_timer == 0)
	{
		object->o_velf = 2 + 2*RandF();
		object->o_f5 = RandF();
	}
	dy = object->o_posy - mario_obj->o_posy;
	if (object->o_posy < object->o_f0-50)
	{
		if (dy < 0) dy = 0-dy;
		if (dy < 500)   enemya_802C0C0C(1);
		else            enemya_802C0C0C(4);
	}
	else
	{
		object->o_posy = object->o_f0 - 50;
		if (dy > 300) object->o_posy -= 1;
	}
	if (ObjectDistMarioToSave() > 800) object->o_targetang = ObjectAngToSave();
	ObjectTurn(object->o_targetang, 0x100);
	if (object->o_targetdist < 200)
	{
		if (object->o_f5 < 0.5) object->o_mode = 2;
	}
	if (object->o_hit_result & HR_008000) object->o_mode = 2;
}

extern OBJLANG obj_13000444[];

static void enemya_802C0F90(void)
{
	float dy;
	if (object->o_timer < 20)
	{
		if (object->o_hit_result & HR_008000)
		{
			ObjMakeHere(object, S_DROPLET, obj_13000444);
		}
	}
	else
	{
		object->o_hit_result = 0;
	}
	if (object->o_timer == 0) ObjectPlaySound(NA_SE3_09);
	if (object->o_velf == 0) object->o_velf = 6;
	dy = object->o_posy - mario_obj->o_posy;
	if (object->o_posy < object->o_f0-50)
	{
		if (dy < 0) dy = 0-dy;
		if (dy < 500)   enemya_802C0C0C(2);
		else            enemya_802C0C0C(4);
	}
	else
	{
		object->o_posy = object->o_f0-50;
		if (dy > 300) object->o_posy -= 1;
	}
	if (ObjectDistMarioToSave() > 800) object->o_targetang = ObjectAngToSave();
	ObjectTurn(object->o_targetang + 0x8000, 0x400);
	if (object->o_timer > 200 && object->o_targetdist > 600) object->o_mode = 1;
}

static OBJCALL *enemya_80330B84[] =
{
	enemya_802C0CD4,
	enemya_802C0D44,
	enemya_802C0F90,
};

void enemya_802C1204(void)
{
	object->o_f0 = BGCheckWater(object->o_posx, object->o_posz);
	object->o_f1 = mario_obj->o_posy + object->o_f2;
	object->o_wall_r = 30;
	objectlib_802A2320();
	ObjectCallMode(enemya_80330B84);
	ObjectProcMoveF();
	if (object->parent->o_mode == 2) ObjKill(object);
}

void enemya_802C12C0(void)
{
	if (object->parent->o_mode != 1) ObjKill(object);
}

static void enemya_802C1308(void)
{
	if (object->o_code < 3)
	{
		object->o_shape = object->o_code;
		if (
			BuGetFlag() & enemya_80330020[object->o_code] ||
			(ObjGetArg(object) & 0xFF) != 0
		)       object->o_mode = 2;
		else    object->o_mode = 1;
	}
	else
	{
		object->o_shape = 3;
		object->o_mode = 2;
	}
}

extern OBJLANG obj_1300227C[];

static void enemya_802C13EC(void)
{
	ObjectHitOFF();
	if (object->o_timer == 0)
	{
		ObjMakeHere(object, S_DOTBOXMARK, obj_1300227C);
		ObjectSetShape(S_DOTBOX);
	}
	if (
		BuGetFlag() & enemya_80330020[object->o_code] ||
		(ObjGetArg(object) & 0xFF) != 0
	)
	{
		object->o_mode = 2;
		ObjectSetShape(S_ITEMBOX);
	}
}

static HITINFO enemya_80330B90 =
{
	/*type   */	HIT_ITEMBOX,
	/*offset */	5,
	/*ap     */	0,
	/*hp     */	1,
	/*ncoin  */	0,
	/*hit r,h*/	40, 30,
	/*dmg r,h*/	40, 30,
};

static void enemya_802C14B0(void)
{
	ObjSetHitInfo(object, &enemya_80330B90);
	if (object->o_timer == 0)
	{
		ObjectShow();
		ObjectHitON();
		object->o_hit_result = 0;
		object->o_posy = object->o_savey;
		object->o_shapeoff = 0;
	}
	if (objectlib_802A51AC())
	{
		ObjectHitOFF();
		object->o_v2 = 0x4000;
		object->o_vely = 30;
		object->o_gravity = -8;
		object->o_ground_y = object->o_posy;
		object->o_mode = 3;
#ifdef MOTOR
		motor_8024C834(5, 80);
#endif
	}
	ObjectMapLoad();
}

static void enemya_802C15B8(void)
{
	UNUSED int i;
	ObjectProcMoveF();
	if (object->o_vely < 0)
	{
		object->o_vely = 0;
		object->o_gravity = 0;
	}
	object->o_f1 = ( SIN(object->o_v2)+1.0)*0.3+0,4;
	object->o_f0 = (-SIN(object->o_v2)+1.0)*0.5+1.0;
	object->o_shapeoff = 2.0F*13*(-SIN(object->o_v2)+1.0);
	object->o_v2 += 0x1000;
	object->s.scale[0] = 2.0F*object->o_f0;
	object->s.scale[1] = 2.0F*object->o_f1;
	object->s.scale[2] = 2.0F*object->o_f0;
	if (object->o_timer == 7) object->o_mode = 4;
}

struct enemya6
{
	u8 index;
	u8 flag;
	u8 arg;
	u8 shape;
	OBJLANG *script;
};

static void enemya_802C17BC(struct enemya6 *a0, UCHAR index)
{
	OBJECT *o = NULL;
	while (a0->index != 99)
	{
		if (index == a0->index)
		{
			o = ObjMakeHere(object, a0->shape, a0->script);
			o->o_vely = 20;
			o->o_velf = 3;
			o->o_angy = mario_obj->o_angy;
			object->o_actorinfo |= a0->arg << 24;
			if (a0->shape == S_POWERSTAR) object->o_flag |= OF_4000;
			break;
		}
		a0++;
	}
}

extern OBJLANG obj_130007F8[];
extern OBJLANG obj_13000964[];
extern OBJLANG obj_13000984[];
extern OBJLANG obj_130009A4[];
extern OBJLANG obj_13001F3C[];
extern OBJLANG obj_13003DB8[];
extern OBJLANG obj_13003DD8[];
extern OBJLANG obj_13003E1C[];
extern OBJLANG obj_13003FDC[];
extern OBJLANG obj_13004010[];

static struct enemya6 enemya_80330BA0[] =
{
	{ 0, 0, 0, S_WINGCAP_S, obj_13003DB8},
	{ 1, 0, 0, S_CAP_E, obj_13003DD8},
	{ 2, 0, 0, S_CAP_S, obj_13003E1C},
	{ 3, 0, 0, S_SHELL, obj_13001F3C},
	{ 4, 0, 0, S_COIN, obj_130009A4},
	{ 5, 0, 0, S_NULL, obj_13000964},
	{ 6, 0, 0, S_NULL, obj_13000984},
	{ 7, 0, 0, S_1UP, obj_13003FDC},
	{ 8, 0, 0, S_POWERSTAR, obj_130007F8},
	{ 9, 0, 0, S_1UP, obj_13004010},
	{10, 0, 1, S_POWERSTAR, obj_130007F8},
	{11, 0, 2, S_POWERSTAR, obj_130007F8},
	{12, 0, 3, S_POWERSTAR, obj_130007F8},
	{13, 0, 4, S_POWERSTAR, obj_130007F8},
	{14, 0, 5, S_POWERSTAR, obj_130007F8},
	{99, 0, 0, S_NULL, NULL},
};

static void enemya_802C18D0(void)
{
	enemya_802C17BC(enemya_80330BA0, object->o_code);
	enemya_802AAE8C(0, 0, 46);
	enemya_802AE0CC(20, S_STAR, 0.3F, object->o_shape);
	ObjectMakeSound(NA_SE3_41);
	if (object->o_code < 3)
	{
		object->o_mode = 5;
		ObjectHide();
	}
	else
	{
		ObjKill(object);
	}
}

static void enemya_802C1988(void)
{
	if (object->o_timer > 300) object->o_mode = 2;
}

static OBJCALL *enemya_80330C20[] =
{
	enemya_802C1308,
	enemya_802C13EC,
	enemya_802C14B0,
	enemya_802C15B8,
	enemya_802C18D0,
	enemya_802C1988,
};

void enemya_802C19C0(void)
{
	ObjectSetScale(2);
	ObjectCallMode(enemya_80330C20);
}

void enemya_802C19FC(void)
{
	Na_Se se = object->o_v0;
	Na_ObjSePlay(se, object);
}

void enemya_802C1A40(void)
{
	if (BuGetFlag() & (BU_KEY2|BU_KEYDOOR2)) ObjKill(object);
}

void enemya_802C1A80(void)
{
}

extern OBJLANG obj_13002DB0[];

void enemya_802C1A90(void)
{
	float water_y = BGCheckWater(object->o_posx, object->o_posz);
	object->o_posx =           object->o_savex + 1700*SIN(object->o_v0);
	object->o_posz =           object->o_savez + 1700*COS(object->o_v0);
	object->o_posy = water_y + object->o_savey +  200*SIN(object->o_v0);
	object->o_angy = object->o_v0 + 0x4000;
	object->o_v0 += 0x80;
	if (mario_obj->o_posy-water_y > -500)
	{
		if (object->o_posy-water_y > -200)
		{
			ObjMakeHereScale(object, S_RIPPLE_MOVE, obj_13002DB0, 4);
		}
	}
	if (!(object->o_timer & 15)) ObjectPlaySound(NA_SE5_00);
	object->o_hit_result = 0;
}

void enemya_802C1C44(void)
{
	if (object->o_targetdist > 10000)
	{
		object->o_alpha = 140;
	}
	else
	{
		object->o_alpha = 140 * object->o_targetdist/10000.0;
	}
	ObjectClrActive();
}

void enemya_802C1CD4(void)
{
	short angx = object->o_shapeangx;
	short angz = object->o_shapeangz;
	ObjectDebugPos();
	object->o_v0 += 0x100;
	object->o_shapeangx = 0x400*SIN(object->o_v0);
	object->o_shapeangz = 0x400*SIN(object->o_v1);
	object->o_rotx = object->o_shapeangx - angx;
	object->o_rotz = object->o_shapeangz - angz;
	if (mario_obj->o_posy > 1000) ObjectLevelSound(NA_SE4_0B);
}

static HITINFO enemya_80330C38 =
{
	/*type   */	HIT_DAMAGE,
	/*offset */	0,
	/*ap     */	1,
	/*hp     */	1,
	/*ncoin  */	0,
	/*hit r,h*/	130, 100,
	/*dmg r,h*/	0, 0,
};

extern OBJLANG obj_130023EC[];

void enemya_802C1E10(void)
{
	FMTX m;
	FVEC sp54, sp48;
	SVEC sp40;
	OBJECT *o;
	BGFACE *ground;
	UNUSED FVEC sp2C;
	FVEC sp20;
#ifdef sgi
	short angx;
#else
	short angx = object->o_shapeangx;
#endif
	if (!object->o_p0)
	{
		if ((o = ObjectFindObj(obj_130023EC))) object->o_p0 = o;
		object->o_relx = object->o_posx - o->o_posx;
		object->o_rely = object->o_posy - o->o_posy;
		object->o_relz = object->o_posz - o->o_posz;
	}
	else
	{
		o = object->o_p0;
		sp40[0] = o->o_shapeangx;
		sp40[1] = o->o_shapeangy;
		sp40[2] = o->o_shapeangz;
		sp54[0] = object->o_relx;
		sp54[1] = object->o_rely;
		sp54[2] = object->o_relz;
		FMtxCoord(m, sp54, sp40);
		MtxTransform3(m, sp48, sp54);
		object->o_posx = o->o_posx + sp48[0];
		object->o_posy = o->o_posy + sp48[1];
		object->o_posz = o->o_posz + sp48[2];
		angx = o->o_shapeangx;
	}
	sp20[0] = object->o_posx;
	sp20[1] = object->o_posy;
	sp20[2] = object->o_posz;
	BGCheckGround(sp20[0], sp20[1], sp20[2], &ground);
	if (ground)
	{
		sp2C[0] = ground->nx;
		sp2C[1] = ground->ny;
		sp2C[2] = ground->nz;
		object->o_shapeangx = angx;
	}
	object->o_f2 = 20*SIN(object->o_v1);
	object->o_v1 += 0x100;
	object->o_relz += object->o_f2;
	if (mario_obj->o_posy > 1000 && fabsf(object->o_f2) > 3)
	{
		ObjectLevelSound(NA_SE6_05);
	}
	ObjSetHitInfo(object, &enemya_80330C38);
	if (!(object->o_v1 & 0x7FFF)) ObjectHitON();
	if (ObjIsObjHit(object, mario_obj))
	{
		object->o_hit_result = 0;
		ObjectHitOFF();
	}
}

void enemya_802C2190(void)
{
	float sp1C = 0.1F;
	float sp18 = 0.5F;
	if (object->o_timer == 0)
	{
		ObjRandOff2D(object, 40);
		object->o_posy += 30;
	}
	ObjectSetScale(sp1C + sp18*object->o_timer);
	object->o_alpha = 50;
	ObjectProcMoveF();
	if (object->o_timer > 4) ObjKill(object);
}

void enemya_802C2274(void)
{
	if (object->o_timer == 0) ObjRandOff2D(object, 40);
}

extern OBJLANG obj_13000A14[];
extern OBJLANG obj_bluecoinsw[];

void enemya_802C22B8(void)
{
	OBJECT *o;
	switch (object->o_mode)
	{
	case 0:
		ObjectClrActive();
		ObjectHitOFF();
		object->o_p1 = ObjectFindObj(obj_bluecoinsw);
		if (object->o_p1) object->o_mode++;
		break;
	case 1:
		o = object->o_p1;
		if (o->o_mode == 2) object->o_mode++;
		break;
	case 2:
		ObjectSetActive();
		ObjectHitON();
		if (object->o_hit_result & HR_008000)
		{
			ObjMakeHere(object, S_SPARKLE, obj_13000A14);
			ObjKill(object);
		}
		if (ObjectFlash(200, 20)) ObjKill(object);
		break;
	}
	object->o_hit_result = 0;
}

extern OBJLANG obj_13002588[];

void enemya_802C242C(void)
{
	ObjectSetScale(3);
	switch (object->o_mode)
	{
	case 0:
		if (mario_obj->movebg == object && player_data[0].state == PS_WAIT_3C)
		{
			object->o_mode++;
			object->o_vely = -20;
			object->o_gravity = 0;
			ObjectPlaySound(NA_SE3_67);
		}
		ObjectMapLoad();
		break;
	case 1:
		if (object->o_timer > 5)
		{
			ObjectHide();
			object->o_mode++;
			object->o_posy = mario_obj->o_posy - 40;
			enemya_802AAE8C(0, 0, 46);
		}
		else
		{
			ObjectMapLoad();
			ObjectProcMoveF();
		}
		break;
	case 2:
		if (object->o_timer < 200)  Na_FixSePlay(NA_SE8_54);
		else                        Na_FixSePlay(NA_SE8_55);
		if (!ObjectFindObj(obj_13002588) || object->o_timer > 240)
		{
			ObjKill(object);
		}
		break;
	}
}

void enemya_802C263C(void)
{
	if (object->o_mode == 0)
	{
		if (object->parent->o_var != 0) object->o_mode++;
	}
	else if (object->o_mode == 1)
	{
		if (object->o_timer < 64)   object->o_angy -= object->o_code << 8;
		else                        object->o_mode++;
	}
}

struct enemya7
{
	short offset;
	short shape;
	MAP *map;
};

extern MAP map_bob_56[];
extern MAP map_0702B65C[];

static struct enemya7 enemya_80330C48[] =
{
	{320, 56, map_bob_56}, /* T:shape */
	{410, 60, map_0702B65C}, /* T:shape */
};

extern OBJLANG obj_130025C0[];
extern OBJLANG obj_13001478[];

void enemya_802C26F8(void)
{
	OBJECT *o;
	int i;
	switch (object->o_mode)
	{
	case 0:
		i = object->o_code;
		o = ObjMakeOff(
			-1, enemya_80330C48[i].offset, 0, 0, object,
			enemya_80330C48[i].shape, obj_130025C0
		);
		o->o_angy += 0x8000;
		ObjSetMap(o, enemya_80330C48[i].map);
		o = ObjMakeOff(
			1, -enemya_80330C48[i].offset, 0, 0, object,
			enemya_80330C48[i].shape, obj_130025C0
		);
		ObjSetMap(o, enemya_80330C48[i].map);
		object->o_mode++;
		break;
	case 1:
		if ((object->o_p0 = ObjectFindObj(obj_13001478))) object->o_mode++;
		break;
	case 2:
		o = object->o_p0;
		if (o->o_mode == 2)
		{
			object->o_var = 2;
			ObjectPlaySound(NA_SE3_3F);
			object->o_mode++;
			if (object->o_code != 0) Na_Solution();
		}
		break;
	case 3:
		break;
	}
}

void enemya_802C2930(void)
{
	if (object->o_mode == 0)
	{
		if (waterp) object->o_mode++;
	}
	else
	{
		if (object->o_timer < 10)
		{
			water_table[0] = waterp[1+6*0+5];
		}
		else
		{
			waterp[1+6*0+5] = water_table[0] + 20*SIN(object->o_v0);
			object->o_v0 += 0x200;
		}
	}
}

void enemya_802C2A24(void)
{
	if (waterp)
	{
		switch (object->o_mode)
		{
		case 0:
			object->o_shapeangy = 0;
			object->o_v1 = object->o_posy;
			if (object->o_timer > 10) object->o_mode++;
			break;
		case 1:
			if (ObjIsObjHit(object, mario_obj) && !object_80361262)
			{
				object->o_mode++;
				object_80361262 = 1;
			}
			break;
		case 2:
			object->o_roty = 0;
			water_table[0] = ApproachPos(water_table[0], object->o_v1, 10);
			if (water_table[0] == object->o_v1)
			{
				if ((short)object->o_shapeangy == 0)    object->o_mode++;
				else                                    object->o_roty = 0x800;
			}
			else
			{
				if (object->o_timer == 0)
				{
					ObjectPlaySound(NA_SE3_66);
				}
				else if (water_table[0] > object->o_v1)
				{
					ObjectLevelSound(NA_SE4_16);
				}
				else
				{
					ObjectLevelSound(NA_SE4_16);
				}
				object->o_roty = 0x800;
#ifdef MOTOR
				motor_8024C974(2);
#endif
			}
			break;
		case 3:
			if (!ObjIsObjHit(object, mario_obj))
			{
				object_80361262 = 0;
				object->o_mode = 1;
				object->o_roty = 0;
			}
			break;
		}
		object->o_shapeangy += object->o_roty;
	}
}

static void enemya_802C2CE8(float scale)
{
	SHORT roty = 0x2C00;
	float s = 0.4*scale;
	object->s.scale[0] = s*(( COS(object->o_v0)+1.0)*0.5*0.3 + 1.0);
	object->s.scale[1] = s*((-COS(object->o_v0)+1.0)*0.5*0.5 + 0.5);
	object->s.scale[2] = s*(( COS(object->o_v0)+1.0)*0.5*0.3 + 1.0);
	object->o_v0 += 0x200;
	object->o_velf = 14;
	object->o_shapeangy += roty;
}

static void enemya_802C2EBC(void)
{
	if (object->o_phase == 0)
	{
		ObjectHitON();
		ObjectSavePos();
		ObjectSetScale(0);
		object->o_v1 = 0;
		if (object->o_targetdist < 1500) object->o_phase++;
		object->o_timer = 0;
	}
	else
	{
		ObjectLevelSound(NA_SE4_05);
		enemya_802C2CE8((float)object->o_timer/60);
		if (object->o_timer >= 60) object->o_mode = 1;
	}
}

extern OBJLANG obj_13002634[];

static void enemya_802C2FBC(void)
{
	float dist = 100*object->o_code;
	object->o_saveang = ObjectAngToSave();
	ObjectLevelSound(NA_SE4_05);
	if (ObjectDistMarioToSave() < dist && object->o_phase == 0)
	{
		object->o_velf = 20;
		ObjectTurn(object->o_targetang, 0x200);
		DbPrint("off ", 0);
		if (player_data[0].state == PS_JUMP_24) object->o_phase++;
	}
	else
	{
		object->o_velf = 20;
		ObjectTurn(object->o_saveang, 0x200);
		if (ObjectDistToSave() < 200) object->o_mode = 2;
	}
	if (object->o_targetdist > 3000) object->o_mode = 2;
	objectlib_802A2320();
	if (object->o_move & OM_0200) object->o_angy = object->o_bg_ang;
	objectlib_802A2348(60);
	enemya_802C2CE8(1);
	ObjMakeHere(object, S_SAND, obj_13002634);
}

static void enemya_802C31C4(void)
{
	float scale = (float)60-object->o_timer;
	if (scale >= 0)
	{
		enemya_802C2CE8(scale/60);
	}
	else
	{
		ObjectHitOFF();
		if (ObjectDistMarioToSave() > 2500) object->o_mode = 0;
		if (object->o_timer > 360) object->o_mode = 0;
	}
}

static HITINFO enemya_80330C58 =
{
	/*type   */	HIT_TORNADO,
	/*offset */	0,
	/*ap     */	0,
	/*hp     */	0,
	/*ncoin  */	0,
	/*hit r,h*/	1500, 4000,
	/*dmg r,h*/	0, 0,
};

static OBJCALL *enemya_80330C68[] =
{
	enemya_802C2EBC,
	enemya_802C2FBC,
	enemya_802C31C4,
};

void enemya_802C329C(void)
{
	ObjSetHitInfo(object, &enemya_80330C58);
	ObjectCallMode(enemya_80330C68);
	object->o_hit_result = 0;
}

void enemya_802C32E8(void)
{
	object->o_angy += 0x3700;
	object->o_velf += 15;
	object->o_posy += 22;
	ObjectSetScale(1.0+RandF());
	if (object->o_timer == 0)
	{
		ObjRandOff2D(object, 100);
		object->o_shapeangx = Rand();
		object->o_shapeangy = Rand();
	}
	if (object->o_timer > 15) ObjKill(object);
}

static void enemya_802C53CC(void);

static HITINFO enemya_80330C74 =
{
	/*type   */	0,
	/*offset */	0,
	/*ap     */	3,
	/*hp     */	3,
	/*ncoin  */	0,
	/*hit r,h*/	140, 80,
	/*dmg r,h*/	40, 60,
};

static void enemya_802C33F4(void)
{
	object->o_velf = 0;
	object->o_vely = 0;
	object->o_gravity = 0;
}

void enemya_802C3440(void)
{
	object->o_v7 = object->o_angy;
}

extern OBJLANG obj_1300277C[];
extern OBJLANG obj_130027F4[];

static int enemya_802C3460(void)
{
	if (ObjectHasScript(obj_1300277C) || ObjectHasScript(obj_130027F4))
	{
		if (!object_80361264)   return TRUE;
		else                    return FALSE;
	}
	else
	{
		if (object->flag & OBJ_0008) return TRUE;
		if (object->o_area == 10 && object_flag & OBJECT_20) return TRUE;
	}
	return FALSE;
}

extern OBJLANG obj_13002768[];

static int enemya_802C3534(void)
{
	float dist = ObjectHasScript(obj_13002768) ? 5000.0F : 1500.0F;
	if (ObjectHasScript(obj_1300277C) || ObjectHasScript(obj_130027F4))
	{
		if (ISTRUE(object_80361264))    return TRUE;
		else                            return FALSE;
	}
	else
	{
		if (object->o_area == -1)
		{
			if (object->o_targetdist < dist) return TRUE;
		}
		else if (!enemya_802C3460())
		{
			if (object->o_targetdist < dist && (
				object->o_area == object_80361250 || object_80361250 == 0
			)) return TRUE;
		}
	}
	return FALSE;
}

static SVEC enemya_80330C84[] =
{
	{   0,  50,    0},
	{ 210, 110,  210},
	{-210,  70, -210},
};

extern OBJLANG obj_13002804[];

void enemya_802C3684(void)
{
	int i;
	if (hud.star < 12)
	{
		ObjKill(object);
	}
	else
	{
		for (i = 0; i < 3; i++)
		{
			OBJECT *o = ObjMakeOff(
				1,
				enemya_80330C84[i][0],
				enemya_80330C84[i][1],
				enemya_80330C84[i][2],
				object, 84, obj_13002804
			); /* T:shape */
			o->o_angy = Rand();
		}
	}
}

static void enemya_802C3748(void)
{
	float scale;
	if (object->o_v0 != object->o_alpha)
	{
		if (object->o_v0 > object->o_alpha)
		{
			object->o_alpha += 20;
			if (object->o_v0 < object->o_alpha) object->o_alpha = object->o_v0;
		}
		else
		{
			object->o_alpha -= 20;
			if (object->o_v0 > object->o_alpha) object->o_alpha = object->o_v0;
		}
	}
	scale = ((float)object->o_alpha/0xFF*0.4 + 0.6) * object->o_f1;
	ObjSetScale(object, scale);
}

static void enemya_802C3884(int a0)
{
	object->o_shapeangx = 0x400*SIN(object->o_v2);
	if (object->o_alpha == 0xFF || ISTRUE(a0))
	{
		object->s.scale[0] =  SIN(object->o_v2)*0.08 + object->o_f1;
		object->s.scale[1] = -SIN(object->o_v2)*0.08 + object->o_f1;
		object->s.scale[2] = object->s.scale[0];
		object->o_gravity = SIN(object->o_v2) * object->o_f1;
		object->o_v2 += 0x400;
	}
}

static int enemya_802C39D4(void)
{
	SHORT sp26 = DeltaAng(object->o_targetang, object->o_angy);
	SHORT sp24 = DeltaAng(object->o_angy, mario_obj->o_shapeangy);
	SHORT sp22 = 0x1568;
	SHORT sp20 = 0x6B58;
	int result = FALSE;
	object->o_vely = 0;
	if (sp26 > sp22 || sp24 < sp20)
	{
		if (object->o_alpha == 40)
		{
			object->o_v0 = 0xFF;
			ObjectPlaySound(NA_SE5_48);
		}
		if (object->o_alpha > 180) result = TRUE;
	}
	else
	{
		if (object->o_alpha == 0xFF) object->o_v0 = 40;
	}
	return result;
}

static void enemya_802C3B08(int a0)
{
	ObjectHitOFF();
	object->o_flag &= ~OF_SETSHAPEANGY;
	object->o_f4 = object->o_angy;
	if (a0)
	{
		object->o_v3 = mario_obj->o_angy;
	}
	else if (COS((SHORT)object->o_angy-(SHORT)object->o_targetang) < 0)
	{
		object->o_v3 = object->o_angy;
	}
	else
	{
		object->o_v3 = (short)(object->o_angy+0x8000);
	}
}

static void enemya_802C3C04(int a0, float a1)
{
	int ang = 0x800 + 0x800*object->o_timer;
	object->o_velf = a1;
	object->o_vely = COS(ang);
	object->o_angy = object->o_v3;
	if (a0)
	{
		object->o_shapeangy += enemya_8033002C[object->o_timer];
		object->o_shapeangz += enemya_8033002C[object->o_timer];
	}
}

static void enemya_802C3CD0(void)
{
	int ang = 0x2000*object->o_timer - 0x3E000;
	object->o_shapeangy += COS(ang)*0x400;
}

static void enemya_802C3D50(void)
{
	object->o_angy = object->o_f4;
	object->o_flag |= OF_SETSHAPEANGY;
	object->o_hit_result = 0;
}

static int enemya_802C3D9C(float a0)
{
	enemya_802C33F4();
	if (object->o_timer == 0) enemya_802C3B08(0);
	if (object->o_timer < 32)
	{
		enemya_802C3C04(FALSE, enemya_8033002C[object->o_timer]/5000.0F*a0);
	}
	else
	{
		ObjectHitON();
		enemya_802C3D50();
		object->o_mode = 1;
		return TRUE;
	}
	return FALSE;
}

static int enemya_802C3E80(float a0)
{
	enemya_802C33F4();
	if (object->o_timer == 0) enemya_802C3B08(1);
	if (object->o_timer < 32)
	{
		enemya_802C3C04(TRUE, enemya_8033002C[object->o_timer]/5000.0F*a0);
	}
	else if (object->o_timer < 48)
	{
		enemya_802C3CD0();
	}
	else
	{
		ObjectHitON();
		enemya_802C3D50();
		object->o_mode = 1;
		return TRUE;
	}
	return FALSE;
}

extern OBJLANG obj_130027E4[];

static int enemya_802C3F8C(void)
{
	OBJECT *o;
	if (object->o_timer == 0)
	{
		object->o_velf = 40;
		object->o_angy = mario_obj->o_angy;
		object->o_var = 1;
		object->o_flag &= ~OF_SETSHAPEANGY;
	}
	else
	{
		if (object->o_timer == 5)
		{
			object->o_v0 = 0;
		}
		if (object->o_timer > 30 || object->o_move & OM_0200)
		{
			objectlib_802A37AC();
			object->o_var = 2;
			if (object->o_p5)
			{
				o = object->o_p5;
#if REVISION >= 199609
				if (!ObjectHasScript(obj_130027E4)) o->o_v8++;
#else
				o->o_v8++;
#endif
			}
			return TRUE;
		}
	}
	object->o_vely = 5;
	object->o_shapeangz += 0x800;
	object->o_shapeangy += 0x800;
	return FALSE;
}

static int enemya_802C4118(int a0)
{
	if ((object->o_hit_result & 0xFF) == a0)    return TRUE;
	else                                        return FALSE;
}

static int enemya_802C4158(void)
{
	int result = 0;
	if (object->o_hit_result & HR_008000)
	{
		if (object->o_hit_result & HR_004000 && !enemya_802C4118(3))
		{
			ObjectHitOFF();
			object->o_hit_result = 0;
			ObjectPlaySound(NA_SE5_0B);
			result = 1;
		}
		else
		{
			ObjectPlaySound(NA_SE5_0A);
			object->o_hit_result = 0;
			result = -1;
		}
	}
	return result;
}

static void enemya_802C4210(float a0, SHORT rot, float speed_scale)
{
	if (enemya_802C39D4())
	{
		float dy;
		short angy;
		object->o_hit_type = HIT_BOUNCE;
		if (ObjectDistMarioToSave() > 1500) angy = ObjectAngToSave();
		else                                angy = object->o_targetang;
		ObjectTurn(angy, rot);
		object->o_vely = 0;
		if (!Player1IsJump())
		{
			dy = object->o_posy - mario_obj->o_posy;
			if (a0 < dy && dy < 500) object->o_vely =
				objectlib_802A1370(object->o_posy, mario_obj->o_posy+50, 10, 2);
		}
		ObjectMatchP1Speed(10-object->o_f6, speed_scale);
		if (object->o_velf != 0) enemya_802C3884(0);
	}
	else
	{
		object->o_hit_type = 0;
		object->o_velf = 0;
		object->o_vely = 0;
		object->o_gravity = 0;
	}
}

extern OBJLANG obj_13002790[];

static void enemya_802C43F4(void)
{
	object->flag |= OBJ_0040;
	if (object->o_code == 2) object->o_area = 10;
	ObjectSavePos();
	object->o_angy = object->o_v7;
	enemya_802C33F4();
	object->o_p5 = ObjectFindObj(obj_13002790);
	object->o_f1 = 1;
	object->o_v0 = 0xFF;
	if (enemya_802C3534())
	{
		if (object->o_code == 2)
		{
			object->o_v5 = 0;
			object->o_mode = 5;
		}
		else
		{
			object->o_mode = 1;
		}
	}
}

static void enemya_802C4508(void)
{
	if (object->o_timer < 30)
	{
		object->o_vely = 0;
		object->o_velf = 13;
		enemya_802C3884(0);
		object->o_wall_r = 0;
	}
	else
	{
		object->o_mode = 1;
		object->o_wall_r = 30;
	}
}

static void enemya_802C45B0(void)
{
	int result;
	if (object->o_timer == 0)
	{
		object->o_f6 = -RandF()*5;
		object->work[O_V9].s[0] = 0x80*RandF();
	}
	enemya_802C4210(-100, object->work[O_V9].s[0]+0x180, 0.5F);
	result = enemya_802C4158();
	if (enemya_802C3460()) object->o_mode = 0;
	if (result == -1) object->o_mode = 2;
	if (result == 1) object->o_mode = 3;
	if (result == 1) ObjectMakeSound(NA_SE5_24);
}

static void enemya_802C46D8(void)
{
	if (enemya_802C3D9C(20)) object->o_mode = 1;
}

static void enemya_802C4720(void)
{
	if (enemya_802C3F8C())
	{
		if (object->o_code != 0)
		{
			ObjKill(object);
		}
		else
		{
			object->o_mode = 4;
			objectlib_802A057C();
		}
	}
}

static void enemya_802C4790(void)
{
	int msg;
	if (!ObjectFindObj(obj_13002804))   msg = MSG_108;
	else                                msg = MSG_107;
	if (objectlib_802A4960(2, 2, msg, 0))
	{
		ObjectMakeSound(NA_SE5_24);
		ObjKill(object);
		if (msg == MSG_108) Na_Solution();
	}
}

static OBJCALL *enemya_80330C98[] =
{
	enemya_802C43F4,
	enemya_802C45B0,
	enemya_802C46D8,
	enemya_802C4720,
	enemya_802C4790,
	enemya_802C4508,
};

extern OBJLANG obj_13002684[];

void enemya_802C4824(void)
{
	objectlib_802A2320();
	ObjectCallMode(enemya_80330C98);
	objectlib_802A2348(78);
	enemya_802C3748();
	if (ObjHasScript(object->parent, obj_13002684) && !object->flag)
	{
		object->parent->o_var++;
	}
	object->o_hit_result = 0;
}

static void enemya_802C48C0(void)
{
	if (ObjectHasScript(obj_13002768))
	{
		enemya_802C53CC();
		object->o_v8 = 10;
	}
	object->o_v5 = 0;
#if REVISION >= 199609
	if (enemya_802C3534() && object->o_v8 >= 5+db_work[5][0])
#else
	if (enemya_802C3534() && object->o_v8 >= 5)
#endif
	{
		object->o_mode = 1;
		ObjectSavePos();
		object->o_angy = object->o_v7;
		ObjectShow();
		object->o_v0 = 0xFF;
		object->o_f1 = 3;
		object->o_hp = 3;
		ObjectSetScale(3);
		ObjectHitON();
	}
	else
	{
		ObjectHide();
		ObjectHitOFF();
		enemya_802C33F4();
	}
}

static void enemya_802C49F0(void)
{
	int result;
	SHORT rot;
	float speed_scale;
	if      (object->o_hp == 3) {rot = 0x180; speed_scale = 0.5F;}
	else if (object->o_hp == 2) {rot = 0x240; speed_scale = 0.6F;}
	else                        {rot = 0x300; speed_scale = 0.8F;}
	enemya_802C4210(-100, rot, speed_scale);
	result = enemya_802C4158();
	if (ObjectHasScript(obj_1300277C))
	{
		if (!object_80361264) object->o_mode = 0;
	}
	else
	{
		if (enemya_802C3460()) object->o_mode = 0;
	}
	if (result == -1) object->o_mode = 2;
	if (result == 1) object->o_mode = 3;
	if (result == 1) ObjectMakeSound(NA_SE5_0C);
}

static void enemya_802C4B54(void)
{
	if (enemya_802C3D9C(20)) object->o_mode = 1;
}

static void enemya_802C4B9C(void)
{
	enemyb_802F2B88(980, 1100, 250);
}

static void enemya_802C4BD4(void)
{
	enemyb_802F2B88(700, 3200, 1900);
}

extern OBJLANG obj_13002968[];

static void enemya_802C4C10(void)
{
	OBJECT *o;
	enemyb_802F2B88(-1600, -2100, 205);
	if ((o = ObjectFindObj(obj_13002968))) o->o_var = 1;
}

static void enemya_802C4C70(void)
{
	if (object->o_timer == 0) object->o_hp--;
	if (object->o_hp == 0)
	{
		if (enemya_802C3F8C())
		{
			objectlib_802A057C();
			object->o_mode = 4;
			ObjSetAng(object, 0, 0, 0);
			if      (object->o_code == 0)   enemya_802C4B9C();
			else if (object->o_code == 1)   enemya_802C4C10();
			else                            enemya_802C4BD4();
		}
	}
	else
	{
		if (object->o_timer == 0)
		{
			objectlib_802A37AC();
			object->o_f1 -= 0.5;
		}
		if (enemya_802C3E80(40)) object->o_mode = 1;
	}
}

extern OBJLANG obj_13002898[];

static void enemya_802C4DD4(void)
{
#if REVISION >= 199609
	enemya_802C33F4();
#endif
	if (object->o_code == 0)
	{
		ObjSetPos(object, 973, 0, 626);
		if (object->o_timer > 60 && object->o_targetdist < 600)
		{
			ObjSetPos(object, 973, 0, 717);
			ObjMakeOff(0, 0, 0,    0, object, 53, obj_13002898); /* T:shape */
			ObjMakeOff(1, 0, 0, -200, object, 53, obj_13002898); /* T:shape */
			ObjMakeOff(2, 0, 0,  200, object, 53, obj_13002898); /* T:shape */
			ObjKill(object);
		}
	}
	else
	{
		ObjKill(object);
	}
}

static OBJCALL *enemya_80330CB0[] =
{
	enemya_802C48C0,
	enemya_802C49F0,
	enemya_802C4B54,
	enemya_802C4C70,
	enemya_802C4DD4,
};

void enemya_802C4F30(void)
{
	ObjSetHitInfo(object, &enemya_80330C74);
	object->o_shapeoff = 60*object->o_f1;
	objectlib_802A2320();
	ObjectCallMode(enemya_80330CB0);
	objectlib_802A2348(78);
	enemya_802C3748();
	object->o_hit_result = 0;
}

static void enemya_802C4FB0(void)
{
	object->o_v5 = 0;
	object->o_v0 = 0xFF;
	object->o_f1 = 2;
	ObjectSetScale(2);
	ObjectHitON();
	if (enemya_802C3534()) object->o_mode = 1;
}

static void enemya_802C503C(void)
{
	int result;
	enemya_802C4210(100, 0x200, 0.5F);
	result = enemya_802C4158();
	if (enemya_802C3460()) object->o_mode = 0;
	if (result == -1) object->o_mode = 2;
	if (result == 1) object->o_mode = 3;
}

static void enemya_802C50D8(void)
{
	if (enemya_802C3D9C(20)) object->o_mode = 1;
}

static void enemya_802C5120(void)
{
	if (enemya_802C3F8C()) ObjKill(object);
}

extern OBJLANG obj_1300167C[];

void enemya_802C515C(void)
{
	if (hud.star < 12)
	{
		ObjKill(object);
	}
	else
	{
		OBJECT *o = ObjMakeHere(object, 90, obj_1300167C); /* T:shape */
		o->o_actorinfo = object->o_actorinfo;
	}
}

static OBJCALL *enemya_80330CC4[] =
{
	enemya_802C4FB0,
	enemya_802C503C,
	enemya_802C50D8,
	enemya_802C5120,
};

void enemya_802C51D4(void)
{
	objectlib_802A2320();
	ObjectCallMode(enemya_80330CC4);
	objectlib_802A2348(78);
	enemya_802C3748();
	object->o_hit_result = 0;
}

void enemya_802C5224(void)
{
	OBJECT *o;
	switch (object->o_mode)
	{
	case 0:
		if (object->o_targetdist < 1000)
		{
			if (object->o_var < 5)
			{
				if (object->o_v2 != 5)
				{
					if (object->o_v2-object->o_var < 2)
					{
						ObjMakeHere(object, 84, obj_130027F4); /* T:shape */
						object->o_v2++;
					}
				}
				object->o_mode++;
			}
			if (object->o_var >= 5)
			{
				o = ObjMakeHere(object, 84, obj_1300277C); /* T:shape */
				ObjCopyActorInfo(o, object);
				object->o_mode = 2;
#if REVISION >= 199609
				Na_Solution();
#else
				Na_FixSePlay(NA_SE8_6A);
#endif
			}
		}
		break;
	case 1:
		if (object->o_timer > 60) object->o_mode = 0;
		break;
	case 2:
		break;
	}
}

static void enemya_802C53CC(void)
{
	camera_8032DF30 = object;
}

void enemya_802C53EC(void)
{
	ObjectDebugPos();
}

void enemya_802C5414(void)
{
	short angy;
	object->o_f1 = 2;
	if (object->o_mode == 0)
	{
		ObjectHide();
		if (hud.star < 12) ObjKill(object);
		if (object_80361250 == 1) object->o_mode++;
	}
	else if (object->o_mode == 1)
	{
		ObjectShow();
		object->o_alpha = 180;
		if (object->o_timer == 0) ObjectSetScale(object->o_f1);
		if (object->o_targetdist < 1000)
		{
			object->o_mode++;
			ObjectPlaySound(NA_SE5_48);
		}
		object->o_velf = 0;
		angy = object->o_targetang;
	}
	else
	{
		ObjectAccelerate(32, 1);
		object->o_savex = -1000;
		object->o_savez = -9000;
		angy = ObjectAngToSave();
		if (object->o_posz < -5000)
		{
			if (object->o_alpha > 0)    object->o_alpha -= 20;
			else                        object->o_alpha = 0;
		}
		if (object->flag & OBJ_0008) object->o_mode = 1;
	}
	object->o_vely = 0;
	angy = ObjectAngToSave();
	ObjectTurn(angy, 0x5A8);
	enemya_802C3884(1);
	ObjectProcMoveF();
}

void enemya_802C5688(void)
{
	float level;
	switch (object->o_code)
	{
	case 1: level =    0; break;
	case 0: level = -206; break;
	case 2: level = -413; break;
#ifdef __GNUC__
	default: return;
#endif
	}
	switch (object->o_mode)
	{
	case 0:
		object->o_posy = object->o_savey - 620;
		object->o_mode++;
		FALLTHROUGH;
	case 1:
		object->o_posy += 8;
		ObjectLevelSound(NA_SE4_08);
		if (object->o_posy > level)
		{
			object->o_posy = level;
			object->o_mode++;
		}
		break;
	case 2:
		if (object->o_timer == 0) ObjectPlaySound(NA_SE3_3D_00);
		if (objectlib_802A3DD4(object->o_timer)) object->o_mode++;
		break;
	case 3:
		if (object->o_timer == 0 && object->o_code == 1) Na_Solution();
		break;
	}
}

void enemya_802C5890(void)
{
	UNUSED int i;
#if REVISION >= 199609
	if (mario_obj->movebg == object)    object->o_mode = 0;
	else                                object->o_mode = 1;
	if (object->o_mode == 0)
	{
		object->o_rotx = object->o_targetdist * COS(object->o_targetang);
		object->o_shapeangx += object->o_rotx;
	}
	else if (abs(object->o_shapeangx) < 3000 || object->o_timer > 15)
#else
	if (mario_obj->movebg == object)
	{
		object->o_rotx = object->o_targetdist * COS(object->o_targetang);
		object->o_shapeangx += object->o_rotx;
	}
	else
#endif
	{
		object->o_rotx = 0;
		if ((short)object->o_shapeangx > 0)
		{
			if (object->o_shapeangx < 200)  object->o_shapeangx = 0;
			else                            object->o_rotx = -200;
		}
		else if (object->o_shapeangx > -200)
		{
			object->o_shapeangx = 0;
		}
		else
		{
			object->o_rotx = 200;
		}
	}
	object->o_shapeangx += object->o_rotx;
}

void enemya_802C5A38(void)
{
	object->o_targetdist = ObjCalcDist3D(object, mario_obj);
	object->o_shapeangy = 0;
	switch (object->o_mode)
	{
	case 0:
		if (object->o_timer == 0)
		{
		}
		if (object->o_var != 0) object->o_mode++;
		break;
	case 1:
		object->o_posx += 5;
		ObjectLevelSound(NA_SE4_0D_1);
		if (object->o_timer > 101) ObjKill(object);
		break;
	default:
		break;
	}
}

static void enemya_802C5B54(void)
{
	if (object->o_v1 == 0)
	{
		if (object_80361250 == 10)
		{
			Na_SeqPush(NA_BGM_MERRYGOROUND, 45, 20, 200);
			object->o_v1++;
		}
	}
	else
	{
		BGFACE *ground;
		USHORT bgcode;
		BGCheckGround(
			mario_obj->o_posx, mario_obj->o_posy, mario_obj->o_posz, &ground
		);
		if (!ground)    bgcode = BG_0;
		else            bgcode = ground->code;
		if (ObjectIsMarioBG() || bgcode == BG_26)
		{
			Na_SeqPush(NA_BGM_MERRYGOROUND, 0, 78, 50);
			object_80361264 = TRUE;
		}
		else
		{
			Na_SeqPush(NA_BGM_MERRYGOROUND, 45, 20, 200);
			object_80361264 = FALSE;
		}
		if (object_80361250 != 0 && object_80361250 != 10)
		{
			Na_SeqPull(300);
			object->o_v1 = 0;
		}
		else
		{
			ObjectLevelSound(NA_SE4_0F);
		}
	}
}

void enemya_802C5CA8(void)
{
	if (!object->o_v2)
	{
		if (object_80361250 == 13) object->o_v2++;
	}
	else
	{
		Na_FixSePlay(NA_SE6_09);
		if (object_80361250 != 13 && object_80361250) object->o_v2 = 0;
	}
	if (object->o_var == 0)
	{
		object->o_roty = 0x80;
		object->o_angy += object->o_roty;
		object->o_shapeangy += object->o_roty;
		enemya_802C5B54();
	}
	else
	{
		object->o_roty = 0;
		Na_SeqPull(300);
	}
}

void enemya_802C5DC0(void)
{
	if (db_work[5][0] == 1)
	{
		ObjSetAng(object, 0, 0, 0);
		object->o_rotx = 0;
		object->o_roty = 0;
		object->o_rotz = 0;
	}
	if (db_work[5][0] == 2)
	{
		object->o_shapeangx = 0x1000*db_work[5][1];
		object->o_shapeangy = 0x1000*db_work[5][2];
		object->o_shapeangz = 0x1000*db_work[5][3];
	}
	object->o_rotx = db_work[5][4];
	object->o_roty = db_work[5][5];
	object->o_rotz = db_work[5][6];
	if (db_work[5][0] == 3)
	{
		object->o_shapeangx += object->o_rotx;
		object->o_shapeangy += object->o_roty;
		object->o_shapeangz += object->o_rotz;
	}
}

void enemya_802C5F48(void)
{
	ObjectSetPosOff(mario_obj, 0, 30, 300);
	object->hit_r = 100 + db_work[4][0];
	object->hit_h = 300 + db_work[4][1];
	objectlib_802A513C(object);
}

#if REVISION >= 199609
void enemya_802C5FDC(void)
{
	if (object->o_mode == 0)
	{
		if (object->o_targetdist < 200)
		{
			Na_Solution();
			object->o_mode++;
		}
	}
}
#endif

void enemya_802C6050(void)
{
	if (mario_obj->movebg == object) object->parent->o_hit_result |= HR_100000;
	object->o_shapeangz = object->parent->o_shapeangz;
}

extern OBJLANG obj_13002A7C[];

void enemya_802C60AC(void)
{
	OBJECT *o;
	o = ObjMakeOff(0, -358, 0, 0, object, 53, obj_13002A7C); /* T:shape */
	o = ObjMakeOff(0,  358, 0, 0, object, 53, obj_13002A7C); /* T:shape */
	o->o_angy += 0x8000;
}

static void enemya_802C6150(void)
{
	if (
		player_data[0].state == PS_DEMO_2B ||
		player_data[0].state == PS_DEMO_2C
	)
	{
		object->o_mode = 4;
	}
	else
	{
		object->o_rotz = 0x400;
		if (object->o_hit_result & HR_100000) object->o_mode = 1;
	}
}

static void enemya_802C61D4(void)
{
	if (object->o_timer == 0) ObjectPlaySound(NA_SE3_0E);
	object->o_rotz -= 0x100;
	object->o_shapeangz += object->o_rotz;
	if (object->o_shapeangz < -0x4000)
	{
		object->o_shapeangz = -0x4000;
		object->o_mode = 2;
	}
}

static void enemya_802C6278(void)
{
	if (object->o_targetdist > 1000) object->o_mode = 3;
}

static void enemya_802C62BC(void)
{
	object->o_shapeangz += 0x400;
	if (object->o_shapeangz > 0)
	{
		object->o_shapeangz = 0;
		object->o_mode = 0;
		object->o_hit_result &= ~HR_100000;
	}
}

static void enemya_802C6328(void)
{
	object->o_shapeangz = -0x3C00;
}

void enemya_802C6348(void)
{
	UNUSED FVEC v;
	switch (object->o_mode)
	{
	case 0: enemya_802C6150(); break;
	case 1: enemya_802C61D4(); break;
	case 2: enemya_802C6278(); break;
	case 3: enemya_802C62BC(); break;
	case 4: enemya_802C6328(); break;
	}
}

void enemya_802C63E8(void)
{
	if (
		object->o_posy-10 < mario_obj->o_posy &&
		mario_obj->o_posy < object->o_posy+object->hit_h+30
	)
	{
		if (object->o_timer > 10 && !(player_data[0].state & PF_POLE))
		{
			ObjectRepelMario2D(70);
		}
	}
}

extern OBJLANG obj_13002AD0[];

void enemya_802C64A4(void)
{
	OBJECT *o = ObjMakeEffect(0, 1, object, S_GLOW, obj_13002AD0);
	if (o)
	{
		ObjRandOff3D(o, 90);
		ObjRandScale(o, 1, 0);
	}
	if (object->o_timer > 1) ObjKill(object);
}

int enemya_802C6538(int *a0)
{
	if (object->o_move & OM_0200)
	{
		*a0 = object->o_bg_ang;
		return 1;
	}
	else if (object->o_move & OM_0400)
	{
		*a0 = object->o_angy + 0x8000;
		return -1;
	}
	return 0;
}

static HITINFO enemya_80330CD4 =
{
	/*type   */	HIT_BOUNCE,
	/*offset */	0,
	/*ap     */	1,
	/*hp     */	1,
	/*ncoin  */	3,
	/*hit r,h*/	130, 70,
	/*dmg r,h*/	90, 60,
};

void enemya_802C65C0(void)
{
	UNUSED int i;
	float animev;
	objectlib_802A2320();
	if (
		object->o_phase != 0 &&
		objectlib_802A4360(&enemya_80330CD4, NA_SE5_24, object->o_v0)
	) object->o_phase = 3;
	if (object->o_phase != 1) object->o_v1 = 0;
	switch (object->o_phase)
	{
	case 0:
		if (object->o_move & OM_BOUND) ObjectPlaySound(NA_SE5_2F_00);
		if (object->o_move & (OM_BOUND|OM_TOUCH))
		{
			object->o_savex = object->o_posx;
			object->o_savey = object->o_posy;
			object->o_savez = object->o_posz;
			object->o_phase++;
		}
		break;
	case 1:
		object->o_velf = 5;
		if (ObjectDistMarioToSave() > 1000)
		{
			object->o_targetang = ObjectAngToSave();
		}
		else
		{
			if (object->o_v1 == 0)
			{
				object->o_v2 = 0;
				object->o_targetang = ObjCalcAngY(object, mario_obj);
				if (DeltaAng(object->o_targetang, object->o_angy) < 0x800)
				{
					object->o_v1 = 1;
					object->o_vely = 20;
					ObjectPlaySound(NA_SE9_44);
				}
			}
			else if (object->o_v1 == 1)
			{
				object->o_velf = 15;
				object->o_v2++;
				if (object->o_v2 > 50) object->o_v1 = 0;
			}
		}
		if (enemya_802C6538(&object->o_targetang)) object->o_phase = 2;
		ObjectTurn(object->o_targetang, 0x200);
		break;
	case 2:
		object->o_velf = 5;
		if ((short)object->o_angy == (short)object->o_targetang)
		{
			object->o_phase = 1;
		}
		if (object->o_posy-object->o_savey < -200) ObjKill(object);
		ObjectTurn(object->o_targetang, 0x400);
		break;
	case 3:
		object->o_flag &= ~OF_SETSHAPEANGY;
		object->o_velf = -10;
		object->o_vely = 30;
		ObjectPlaySound(NA_SE9_44);
		object->o_phase++;
		break;
	case 4:
		object->o_velf = -10;
		if (object->o_move & OM_BOUND)
		{
			object->o_phase++;
			object->o_vely = 0;
			object->o_v2 = 0;
			object->o_flag |= OF_SETSHAPEANGY;
			object->o_hit_result = 0;
		}
		break;
	case 5:
		object->o_velf = 2;
		object->o_v2++;
		if (object->o_v2 > 30) object->o_phase = 0;
		break;
	}
	if (object->o_velf < 10)    animev = 1;
	else                        animev = 3;
	ObjectSetAnimeV(0, animev);
	if (object->o_move & (OM_BOUND|OM_TOUCH)) enemya_802BECB0(1, 23, NA_SE9_43);
	if (object->parent != object)
	{
		if (ObjIsHide(object)) ObjKill(object);
		if (!object->flag) object->parent->o_var = 1;
	}
	objectlib_802A2348(-50);
}

extern OBJLANG obj_13002B5C[];

void enemya_802C6B6C(void)
{
	if (object->o_mode == 0)
	{
		if (
			object->o_timer > 30 &&
			500 < object->o_targetdist && object->o_targetdist < 1500
		)
		{
			OBJECT *o;
			ObjectPlaySound(NA_SE9_44);
			o = ObjMakeHere(object, 101, obj_13002B5C); /* T:shape */
			o->o_v0 = object->o_v0;
			o->o_velf = 30;
			o->o_vely = 80;
			object->o_mode++;
			object->o_v0 = 1;
		}
	}
	else
	{
		if (object->o_var != 0)
		{
			object->o_var = 0;
			object->o_mode = 0;
		}
	}
}

static void enemya_802C6CA0(void)
{
	UNUSED int frame = object->s.skel.frame;
	int flag = FALSE;
	if (object->o_velf < 5)
	{
		flag  = ObjectIsAnimeFrame(0);
		flag |= ObjectIsAnimeFrame(23);
	}
	else
	{
		flag  = ObjectIsAnimeFrameRange( 0, 3);
		flag |= ObjectIsAnimeFrameRange(23, 3);
	}
	if (flag) ObjectPlaySound(NA_SE5_15_50);
}

static void enemya_802C6D6C(void)
{
	ObjectSetAnimeV(0, 1);
	ObjectSavePos();
	if (object->o_code != 0)
	{
		camera_8032DF30 = object;
		ObjectSetScale(2);
		if (object->o_phase == 0)
		{
			if (object->o_targetdist < 600)
			{
				object->o_phase++;
				Na_SeqMute(0, 60, 40);
			}
			else
			{
				ObjectSavePos();
				object->o_hp = 3;
			}
		}
		else
		{
			if (objectlib_802A4BE4(2, 1, 162, MSG_114)) object->o_mode = 2;
		}
	}
	else
	{
		if (object->o_targetdist < 500) object->o_mode = 1;
	}
	enemya_802C6CA0();
}

static void enemya_802C6EC8(void)
{
	if (object->o_phase == 0)
	{
		object->o_velf = 0;
		ObjectSetAnimeV(0, 1);
		if (object->o_timer > 31)   object->o_phase++;
		else                        object->o_angy += 0x400;
	}
	else
	{
		object->o_velf = 3;
		if (object->o_timer > 42) object->o_mode = 1;
	}
	enemya_802C6CA0();
}

static void enemya_802C6FB0(void)
{
	SHORT dang = DeltaAng(object->o_targetang, object->o_angy);
	float dist = ObjectDistToSave();
	float range = stage_index == STAGE_BITS ? 200.0F : 700.0F;
	ObjectSetAnimeV(0, 1);
	object->o_velf = 3;
	if (dist > range)
	{
		object->o_mode = 7;
	}
	else
	{
		if (dang < 0x2000)
		{
			if (object->o_targetdist < 1500)
			{
				object->o_velf = 9;
				ObjectSetAnimeV(0, 3);
			}
			if (object->o_targetdist < 300) object->o_mode = 3;
		}
	}
	enemya_802C6CA0();
}

static void enemya_802C710C(void)
{
	ObjectSetAnimeV(0, 1);
	object->o_velf = 3;
	ObjectTurn(object->o_targetang, 0x200);
	if (object->o_timer > 30)
	{
		SHORT dang = DeltaAng(object->o_targetang, object->o_angy);
		if (dang < 0x2000)
		{
			if (object->o_targetdist < 1500)
			{
				object->o_velf = 9;
				ObjectSetAnimeV(0, 3);
			}
			if (object->o_targetdist < 300) object->o_mode = 3;
		}
	}
	enemya_802C6CA0();
	if (enemya_802A7384(1000))
	{
		object->o_mode = 0;
		Na_BgmStop(NA_BGM_BATTLE);
	}
}

static void enemya_802C7254(void)
{
	object->o_velf = 0;
	ObjectSetAnimeV(1, 1);
	if (objectlib_8029FF04()) object->o_mode = 4;
}

static void enemya_802C72B4(void)
{
	if (object->o_timer == 0) object->o_vely = 40;
	if (object->o_timer < 8)
	{
	}
	else
	{
		object->o_rotx += 0x100;
		object->o_shapeangx += object->o_rotx;
		if (object->o_shapeangx > 0x4000)
		{
			object->o_rotx = 0;
			object->o_shapeangx = 0x4000;
			object->o_mode = 5;
		}
	}
}

static void enemya_802C7380(void)
{
	if (object->o_phase == 0 && object->o_move & OM_BOUND)
	{
		ObjectPlaySound(NA_SE5_16_60);
		objectlib_802A50FC(1);
		object->o_vely = 0;
		object->o_phase++;
	}
	if (object->o_move & OM_TOUCH) object->o_mode = 6;
}

static void enemya_802C7428(void)
{
	if (object->o_phase == 0)
	{
		if (objectlib_802A3754())
		{
			object->o_hp--;
			ObjectPlaySound(NA_SE9_5A_C0);
			ObjectPlaySound(NA_SE5_47);
			if (object->o_hp == 0)
			{
				object->o_mode = 8;
			}
			else
			{
				FVEC sp1C;
				enemya_802B98D4(sp1C, &object->o_posx);
				enemya_802B98D4(&object->o_posx, &mario_obj->o_posx);
				enemya_802AAE8C(0, 0, 100);
				enemya_802AE0CC(20, S_SHARD, 3, 4);
				objectlib_802A50FC(1);
				enemya_802B98D4(&object->o_posx, sp1C);
			}
			object->o_phase++;
		}
		object->o_v1 = 0;
	}
	else
	{
		if (object->o_v1 < 10)
		{
			if (object->o_v1 % 2) object->o_posy += 8;
			else object->o_posy -= 8;
		}
		else
		{
			object->o_phase = 10;
		}
		object->o_v1++;
	}
}

static void enemya_802C75FC(void)
{
	if (object->o_phase == 0)
	{
		if (mario_obj->movebg == object)
		{
			if (objectlib_802A3754())
			{
				object->o_ncoin = 5;
				ObjectMakeCoin(object, 5, 20);
				object->o_mode = 8;
			}
			else
			{
				objectlib_802A1BDC();
				object->o_phase++;
			}
		}
	}
	else
	{
		if (!ObjectIsMarioBG()) object->o_phase = 0;
	}
}

static void enemya_802C76D4(void)
{
	if (object->o_phase != 10)
	{
		object->o_velf = 0;
		object->o_rotx = 0;
		object->o_roty = 0;
		object->o_rotz = 0;
		if (object->o_code != 0)    enemya_802C7428();
		else                        enemya_802C75FC();
		if (
			object->o_timer > 100 ||
			(mario->state == PS_DEMO_39 && object->o_timer > 30)
		) object->o_phase = 10;
	}
	else
	{
		if (object->o_shapeangx > 0)
		{
			object->o_rotx = -0x200;
			object->o_shapeangx += object->o_rotx;
		}
		else
		{
			object->o_rotx = 0;
			object->o_shapeangx = 0;
			if (object->o_code != 0)    object->o_mode = 2;
			else                        object->o_mode = 1;
		}
	}
}

static void enemya_802C7858(void)
{
	if (object->o_code != 0)
	{
		if (objectlib_802A4BE4(2, 2, 162, MSG_115))
		{
			ObjSetAng(object, 0, 0, 0);
			ObjectHide();
			ObjectHitOFF();
			enemya_802AAE8C(0, 0, 200);
			enemya_802AE0CC(20, S_SHARD, 3, 4);
			objectlib_802A50FC(1);
			object->o_posy += 100;
			enemyb_802F2B88(180, 3880, 340);
			ObjectPlaySound(NA_SE5_47);
			object->o_mode = 9;
		}
	}
	else
	{
		enemya_802AAE8C(0, 0, 100);
		enemya_802AE0CC(20, S_SHARD, 3, 4);
		objectlib_802A50FC(1);
		ObjectMakeSound(NA_SE5_0C);
		ObjKill(object);
	}
}

static void enemya_802C7998(void)
{
	if (object->o_timer == 60) Na_BgmStop(NA_BGM_BATTLE);
}

static OBJCALL *enemya_80330CE4[] =
{
	enemya_802C6D6C,
	enemya_802C6FB0,
	enemya_802C710C,
	enemya_802C7254,
	enemya_802C72B4,
	enemya_802C7380,
	enemya_802C76D4,
	enemya_802C6EC8,
	enemya_802C7858,
	enemya_802C7998,
};

void enemya_802C79D8(void)
{
	objectlib_802A2320();
	ObjectCallMode(enemya_80330CE4);
	objectlib_802A2348(-20);
	if (object->o_mode != 9)
	{
		if (object->o_code != 0)    objectlib_802A4564(2000);
		else                        objectlib_802A4564(1000);
		ObjectMapLoad();
	}
}

extern OBJLANG obj_13002C60[];

static SPLASH enemya_80330D0C =
{
	0x0002, S_DROPLET, obj_13002C60,
	/*ang  */	0x0000,
	/*pos  */	0,
	/*velf */	5, 3,
	/*vely */	30, 20,
	/*scale*/	0.5, 1,
};

void enemya_802C7A70(void)
{
	int i;
	if (object->o_timer == 0)
	{
		object->o_posy = BGCheckWater(object->o_posx, object->o_posz);
	}
	if (object->o_posy > -10000)
	{
		for (i = 0; i < 3; i++) ObjMakeSplash(object, &enemya_80330D0C);
	}
}

extern OBJLANG obj_13002C7C[];

void enemya_802C7B14(void)
{
	UNUSED int i;
	float water_y = BGCheckWater(object->o_posx, object->o_posz);
	if (object->o_timer == 0)
	{
		if (ObjectHasShapeID(S_FISH))   object->s.s.flag &= ~SHP_BILLBOARD;
		else                            object->s.s.flag |= SHP_BILLBOARD;
		object->o_shapeangy = Rand();
	}
	object->o_vely -= 4;
	object->o_posy += object->o_vely;
	if (object->o_vely < 0)
	{
		if (water_y > object->o_posy)
		{
			ObjMakeEffect(0, 1, object, S_WAVE, obj_13002C7C);
			ObjKill(object);
		}
		else
		{
			if (object->o_timer > 20) ObjKill(object);
		}
	}
	if (water_y < -10000) ObjKill(object);
}

void enemya_802C7CAC(void)
{
	ObjCopyPos(object, mario_obj);
	object->o_posy = player_data[0].water + 5;
	if (!(mario_obj->o_v0 & 0x80))
	{
		mario_obj->o_effect &= ~0x80 & 0xFFFF;
		object->flag = 0;
	}
}

void enemya_802C7D40(void)
{
	ObjectSetScale(1.5+RandF());
}

void enemya_802C7D90(void)
{
	float water_y = BGCheckWater(object->o_posx, object->o_posz);
	ObjSetScaleXYZ(object, 0.5F, 1, 0.5F);
	object->o_posy = water_y + 5;
}

extern OBJLANG obj_13002C60[];

SPLASH enemya_80330D30 =
{
	0x0022, S_DROPLET, obj_13002C60,
	/*ang  */	0x0000,
	/*pos  */	0,
	/*velf */	2, 3,
	/*vely */	20, 20,
	/*scale*/	0.5, 1,
};

static SPLASH enemya_80330D54 =
{
	0x0022, S_FISH, obj_13002C60,
	/*ang  */	0x0000,
	/*pos  */	0,
	/*velf */	2, 3,
	/*vely */	20, 20,
	/*scale*/	1, 0,
};

SPLASH enemya_80330D78 =
{
	0x0062, S_DROPLET, obj_13002C60,
	/*ang  */	0x6000,
	/*pos  */	0,
	/*velf */	2, 8,
	/*vely */	10, 10,
	/*scale*/	0.5, 1,
};

extern ANIME *anime_fish[];

void enemya_802C7DFC(void)
{
	if ((Rand() & 0xFF) < 1)
	{
		OBJECT *o = ObjMakeSplash(object, &enemya_80330D54);
		ObjInitAnime(o, anime_fish, 0);
	}
}

void enemya_802C7E5C(void)
{
	float water_y = BGCheckWater(object->o_posx, object->o_posz);
	if (object->o_timer == 0)
	{
		if (gfx_frame & 1) ObjKill(object);
	}
	object->o_posy = water_y + 5;
	if (object->o_timer == 0) object->o_f1 = object->s.scale[0];
	if (object->o_shape >= 4)
	{
		object->o_f1 -= 0.1;
		if (object->o_f1 < 0) object->o_f1 = 0;
		object->s.scale[0] = object->o_f1;
		object->s.scale[2] = object->o_f1;
	}
}

static HITINFO enemya_80330D9C =
{
	/*type   */	HIT_WIND,
	/*offset */	0,
	/*ap     */	0,
	/*hp     */	0,
	/*ncoin  */	0,
	/*hit r,h*/	20, 70,
	/*dmg r,h*/	20, 70,
};

extern OBJLANG obj_13002E58[];

void enemya_802C7F98(void)
{
	OBJECT *o;
	ObjSetHitInfo(object, &enemya_80330D9C);
	if (object->o_timer == 0)
	{
		object->o_p0 = ObjectFindObj(obj_13002E58);
		ObjRandOff3D(object, 100);
		object->o_velf =  100*COS(object->o_angx);
		object->o_vely = -100*SIN(object->o_angx);
		object->o_angy += RandRange(500*object->o_code);
		object->o_alpha = 100;
	}
	ObjectProcMoveF();
	if (object->o_timer > 15) ObjKill(object);
	o = object->o_p0;
	if (o)
	{
		float d;
		float dx = o->o_f3 - object->o_posx;
		float dz = o->o_f4 - object->o_posz;
		if ((d = DIST2(dx, dz)) < 300)
		{
			ObjKill(object);
			ObjectHitOFF();
		}
	}
}

extern OBJLANG obj_13002E04[];
extern OBJLANG obj_13002E20[];

void enemya_802C81B4(int code, float scale, float offx, float offy, float offz)
{
	if (gfx_frame & 1)
	{
		ObjMakeOffScale(
			code, offx, offy, offz, 0.5F, object, S_SNOW, obj_13002E04
		);
		ObjMakeOffScale(
			code, offx, offy, offz, scale, object, S_NULL, obj_13002E20
		);
	}
	else
	{
		ObjMakeOffScale(
			code, offx, offy, offz, scale, object, S_WHITEPUFF, obj_13002E20
		);
	}
	ObjMakeOffScale(
		code, offx, offy, offz, scale, object, S_NULL, obj_13002E20
	);
}

void enemya_802C834C(void)
{
	UNUSED int result = 0;
	short dang;
	if (object->o_timer == 0) object->o_v0 = object->o_angy;
	if (object->o_phase == 0)
	{
		FVEC sp24;
		object->o_targetdist = 0;
		enemya_802B98D4(sp24, &object->o_posx);
		ObjSetPos(object, 1100, 3328, 1164);
		if (objectlib_802A47A0(1000, 30, 0x7FFF)) object->o_phase++;
		enemya_802B98D4(&object->o_posx, sp24);
	}
	else if (object->o_phase == 1)
	{
		if (objectlib_802A4960(2, 2, MSG_153, 0)) object->o_phase++;
	}
	else
	{
		if (
			object->o_targetdist < 1500 &&
			fabsf(mario_obj->o_posy-object->o_savey) < 500
		)
		{
			if ((dang = object->o_targetang-object->o_v0) > 0)
			{
				if (dang < +0x1500) object->o_angy = object->o_targetang;
				else                object->o_angy = object->o_v0 + 0x1500;
			}
			else
			{
				if (dang > -0x1500) object->o_angy = object->o_targetang;
				else                object->o_angy = object->o_v0 - 0x1500;
			}
			enemya_802C81B4(12, 3, 0, 0, 0);
			ObjectLevelSound(NA_SE6_04_40);
		}
	}
}

static int enemya_802C85A4(void)
{
	object->o_velf = 0;
	ObjectSetAnimeV(0, 1);
	object->o_roty = 0x400;
	object->o_angy += object->o_roty;
	if (object->o_timer == 31)  return TRUE;
	else                        return FALSE;
}

struct enemya8
{
	int time;
	int anime;
	float speed;
	float anime_speed;
};

static struct enemya8 enemya_80330DAC[] =
{
	{60, 0,  6, 1},
	{30, 3,  0, 1},
	{30, 0, 12, 2},
	{30, 3,  0, 1},
	{30, 0, -6, 1},
	{30, 3,  0, 1},
	{-1, 0,  0, 0},
};

void enemya_802C863C(void)
{
	float posx, posz, speed = 100;
	object->o_roty = 0;
	objectlib_802A2320();
	switch (object->o_mode)
	{
	case 0:
		if (object->o_timer == 0)
		{
			object->o_v6 = 0;
			object->o_v7 = 0;
		}
		if (object->o_v7 < enemya_80330DAC[object->o_v6].time)
		{
			object->o_v7++;
		}
		else
		{
			object->o_v7 = 0;
			object->o_v6++;
			if (enemya_80330DAC[object->o_v6].time < 0) object->o_v6 = 0;
		}
		if (object->o_posx < 300)
		{
			object->o_mode++;
		}
		else
		{
			object->o_velf = enemya_80330DAC[object->o_v6].speed;
			ObjectSetAnimeV(
				enemya_80330DAC[object->o_v6].anime,
				enemya_80330DAC[object->o_v6].anime_speed
			);
		}
		break;
	case 1:
		if (enemya_802C85A4()) object->o_mode++;
		break;
	case 2:
		object->o_velf = 12;
		ObjectSetAnimeV(0, 2);
		if (object->o_posx > 1700) object->o_mode++;
		break;
	case 3:
		if (enemya_802C85A4()) object->o_mode = 0;
		break;
	}
	objectlib_802A2348(-78);
	if (!objectlib_802A4564(1000)) enemya_802BED7C(TRUE);
	posx = object->o_posx + 60*SIN(DEG(309));
	posz = object->o_posz + 60*COS(DEG(309));
	posx += speed * SIN(DEG(39));
	posz += speed * COS(DEG(39));
	object->o_f3 = posx;
	object->o_f4 = posz;
	DbPrintErr("x %d", object->o_posx);
	DbPrintErr("z %d", object->o_posz);
}
