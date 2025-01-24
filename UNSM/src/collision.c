#include <sm64.h>

#define PH_POUND                0x01
#define PH_PUNCH                0x02
#define PH_KICK                 0x04
#define PH_SWEEPKICK            0x08
#define PH_SLIDEKICK            0x10
#define PH_SLIDING              0x20
#define PH_STOMP                0x40
#define PH_HEADATTACK           0x80

#define PH_LOWATTACK \
	(PH_POUND|PH_PUNCH|PH_KICK|PH_SWEEPKICK|PH_SLIDEKICK|PH_SLIDING|PH_STOMP)
#define PH_ALLATTACK ( \
	PH_POUND|PH_PUNCH|PH_KICK|PH_SWEEPKICK|PH_SLIDEKICK|PH_SLIDING|PH_STOMP| \
	PH_HEADATTACK \
)

typedef struct collision
{
	u32 type;
	int (*proc)(PLAYER *pl, u32 type, OBJECT *obj);
}
COLLISION;

static int PL_CollideCoin(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideRecover(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideStar(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideCage(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollidePipe(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollidePortDoor(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideDoor(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideCannon(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideIgloo(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideTornado(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideWhirlpool(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideWind(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideBurn(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideBullet(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideClam(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideBump(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideElecShock(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideEnemy(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideFlyEnemy(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideBounce(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideSpiny(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideDamage(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideItemBox(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideShell(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollidePole(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideHang(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideCap(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideTake(PLAYER *pl, u32 type, OBJECT *obj);
static int PL_CollideMessage(PLAYER *pl, u32 type, OBJECT *obj);

static COLLISION collisiontab[] =
{
	{HIT_COIN,      PL_CollideCoin},
	{HIT_RECOVER,   PL_CollideRecover},
	{HIT_STAR,      PL_CollideStar},
	{HIT_CAGE,      PL_CollideCage},
	{HIT_PIPE,      PL_CollidePipe},
	{HIT_PORTDOOR,  PL_CollidePortDoor},
	{HIT_DOOR,      PL_CollideDoor},
	{HIT_CANNON,    PL_CollideCannon},
	{HIT_IGLOO,     PL_CollideIgloo},
	{HIT_TORNADO,   PL_CollideTornado},
	{HIT_WHIRLPOOL, PL_CollideWhirlpool},
	{HIT_WIND,      PL_CollideWind},
	{HIT_BURN,      PL_CollideBurn},
	{HIT_BULLET,    PL_CollideBullet},
	{HIT_CLAM,      PL_CollideClam},
	{HIT_BUMP,      PL_CollideBump},
	{HIT_ELECSHOCK, PL_CollideElecShock},
	{HIT_DUMMY,     PL_CollideBounce},
	{HIT_ENEMY,     PL_CollideEnemy},
	{HIT_FLYENEMY,  PL_CollideFlyEnemy},
	{HIT_BOUNCE,    PL_CollideBounce},
	{HIT_DAMAGE,    PL_CollideDamage},
	{HIT_POLE,      PL_CollidePole},
	{HIT_HANG,      PL_CollideHang},
	{HIT_ITEMBOX,   PL_CollideItemBox},
	{HIT_KOOPA,     PL_CollideBounce},
	{HIT_SHELL,     PL_CollideShell},
	{HIT_SPINY,     PL_CollideSpiny},
	{HIT_CAP,       PL_CollideCap},
	{HIT_TAKE,      PL_CollideTake},
	{HIT_MESSAGE,   PL_CollideMessage},
};

static u32 fdamagetab[3][3] =
{
	{PS_MOVE_25, PS_MOVE_23, PS_MOVE_21},
	{PS_JUMP_31, PS_JUMP_31, PS_JUMP_32},
	{PS_SWIM_06, PS_SWIM_06, PS_SWIM_06},
};

static u32 bdamagetab[3][3] =
{
	{PS_MOVE_24, PS_MOVE_22, PS_MOVE_20},
	{PS_JUMP_30, PS_JUMP_30, PS_JUMP_33},
	{PS_SWIM_05, PS_SWIM_05, PS_SWIM_05},
};

static u8 door_flag = FALSE;
static u8 pipe_flag = FALSE;
static u8 silder_flag = FALSE;
static u8 hit_enemy;
static short invincible;

extern OBJLANG o_13003DB8[];
extern OBJLANG o_13003DD8[];
extern OBJLANG o_13003DF8[];
extern OBJLANG o_13003E1C[];

static u32 ObjGetCapFlag(OBJECT *obj)
{
	OBJLANG *script = VirtualToSegment(SEG_OBJECT, obj->script);
	if      (script == o_13003DF8) return PL_DEFCAP;
	else if (script == o_13003DD8) return PL_METALCAP;
	else if (script == o_13003DB8) return PL_WINGCAP;
	else if (script == o_13003E1C) return PL_VANISHCAP;
	return 0;
}

static int PL_IsFacingObj(PLAYER *pl, OBJECT *obj, SHORT range)
{
	float dx = pl->pos[0] - obj->o_posx;
	float dz = pl->pos[2] - obj->o_posz;
	SHORT angy = ATAN2(dz, dx);
	short dang = angy - obj->o_angy;
	if (-range <= dang && dang <= range) return TRUE;
	return FALSE;
}

SHORT PL_GetAngToObj(PLAYER *pl, OBJECT *obj)
{
	float dx = obj->o_posx - pl->pos[0];
	float dz = obj->o_posz - pl->pos[2];
	return ATAN2(dz, dx);
}

static int PL_CheckAttack(PLAYER *pl, OBJECT *obj)
{
	int attack = 0;
	u32 state = pl->state;
	if (state & PF_ATCK)
	{
		if (state == PS_TAKE_00 || state == PS_MOVE_17 || state == PS_JUMP_2C)
		{
			short dang = PL_GetAngToObj(pl, obj) - pl->ang[1];
			if (pl->flag & PL_PUNCH)
			{
				if (-0x2AAA <= dang && dang <= 0x2AAA) attack = PH_PUNCH;
			}
			if (pl->flag & PL_KICK)
			{
				if (-0x2AAA <= dang && dang <= 0x2AAA) attack = PH_KICK;
			}
			if (pl->flag & PL_SWEEPKICK)
			{
				if (-0x4000 <= dang && dang <= 0x4000) attack = PH_SWEEPKICK;
			}
		}
		else if (state == PS_JUMP_29 || state == PS_JUMP_24)
		{
			if (pl->vel[1] < 0) attack = PH_POUND;
		}
		else if (state == PS_WAIT_3C || state == PS_WAIT_38)
		{
			if (pl->vel[1] < 0 && pl->phase == 0) attack = PH_POUND;
		}
		else if (state == PS_JUMP_2A || state == PS_MOVE_1A)
		{
			attack = PH_SLIDEKICK;
		}
		else if (state & PF_RIDE)
		{
			attack = PH_SLIDING;
		}
		else
		{
			if (pl->speed <= -26 || 26 <= pl->speed) attack = PH_SLIDING;
		}
	}
	if (!attack && (state & PF_JUMP))
	{
		if (pl->vel[1] < 0)
		{
			if (pl->pos[1] > obj->o_posy) attack = PH_STOMP;
		}
		else
		{
			if (pl->pos[1] < obj->o_posy) attack = PH_HEADATTACK;
		}
	}
	return attack;
}

static int ObjAttack(OBJECT *obj, int attack)
{
	int result = 0;
	switch (attack)
	{
	case PH_POUND:
		result = 4;
		break;
	case PH_PUNCH:
		result = 1;
		break;
	case PH_KICK:
	case PH_SWEEPKICK:
		result = 2;
		break;
	case PH_SLIDEKICK:
	case PH_SLIDING:
		result = 5;
		break;
	case PH_STOMP:
		result = 3;
		break;
	case PH_HEADATTACK:
		result = 6;
		break;
	}
	obj->o_hit_result = (0x4000|0x8000) + result; /* T:hit_result */
	return result;
}

extern OBJLANG o_13000708[];
extern OBJLANG o_13003464[];
extern OBJLANG o_1300346C[];
extern OBJLANG o_13003474[];

void PL_StopRide(PLAYER *pl)
{
	if (pl->ride)
	{
		pl->ride->o_hit_result = 0x00400000; /* T:hit_result */
		AudStopShellBGM();
		pl->ride = NULL;
	}
}

void PL_TakeObject(PLAYER *pl)
{
	if (!pl->take)
	{
		pl->take = pl->attach;
		ObjectSetTake(pl->take, o_13003464);
	}
}

void PL_DropObject(PLAYER *pl)
{
	if (pl->take)
	{
		if (pl->take->script == SegmentToVirtual(o_13000708))
		{
			AudStopShellBGM();
		}
		ObjectSetTake(pl->take, o_1300346C);
		pl->take->o_posx = pl->shape->hand_pos[0];
		pl->take->o_posy = pl->pos[1];
		pl->take->o_posz = pl->shape->hand_pos[2];
		pl->take->o_angy = pl->ang[1];
		pl->take = NULL;
	}
}

void PL_ThrowObject(PLAYER *pl)
{
	if (pl->take)
	{
		if (pl->take->script == SegmentToVirtual(o_13000708))
		{
			AudStopShellBGM();
		}
		ObjectSetTake(pl->take, o_13003474);
		pl->take->o_posx = pl->shape->hand_pos[0] + 32*SIN(pl->ang[1]);
		pl->take->o_posy = pl->shape->hand_pos[1];
		pl->take->o_posz = pl->shape->hand_pos[2] + 32*COS(pl->ang[1]);
		pl->take->o_angy = pl->ang[1];
		pl->take = NULL;
	}
}

void PL_DropAll(PLAYER *pl)
{
	PL_DropObject(pl);
	PL_StopRide(pl);
	if (pl->state == PS_JUMP_28)
	{
		pl->attach->o_hit_result = 0;
		pl->attach->o_v7 = gfx_frame;
	}
}

int PL_IsWearingDefCap(PLAYER *pl)
{
	return (pl->flag & (PL_ANYCAP|PL_HEADCAP)) == (PL_DEFCAP|PL_HEADCAP);
}

void PL_BlowCap(PLAYER *pl, float speed)
{
	OBJECT *obj;
	if (PL_IsWearingDefCap(pl))
	{
		BuSetCap(pl->pos[0], pl->pos[1], pl->pos[2]);
		pl->flag &= ~(PL_DEFCAP|PL_HEADCAP);
		obj = ObjMakeHere(pl->obj, S_CAP_S, o_13003DF8);
		obj->o_posy += (pl->state & PF_SHRT) ? 120.0F : 180.0F;
		obj->o_velf = speed;
		obj->o_angy = (short)(pl->ang[1] + 0x400);
		if (pl->speed < 0) obj->o_angy = (short)(obj->o_angy+0x8000);
	}
}

int MarioStealCap(int flag)
{
	int result = FALSE;
	if (PL_IsWearingDefCap(mario))
	{
		BuSetFlag(flag == 1 ? BU_CONDORCAP : BU_MONKEYCAP);
		mario->flag &= ~(PL_DEFCAP|PL_HEADCAP);
		result = TRUE;
	}
	return result;
}

void MarioReturnCap(void)
{
	PL_DropObject(mario);
	BuClrFlag(BU_CONDORCAP|BU_MONKEYCAP);
	mario->flag &= ~PL_HEADCAP;
	mario->flag |= PL_DEFCAP|PL_HANDCAP;
}

static int PL_IsTaking(PLAYER *pl, OBJECT *obj)
{
	u32 state = pl->state;
	if (state == PS_MOVE_16 || state == PS_JUMP_0A)
	{
		if (!(obj->o_hit_flag & 4)) return TRUE;
	}
	else if (state == PS_TAKE_00 || state == PS_MOVE_17)
	{
		if (pl->code < 2) return TRUE;
	}
	return FALSE;
}

OBJECT *PL_GetHitObj(PLAYER *pl, int type)
{
	int i;
	for (i = 0; i < pl->obj->hit_count; i++)
	{
		OBJECT *obj = pl->obj->hit[i];
		if (obj->o_hit_type == type) return obj;
	}
	return NULL;
}

extern OBJLANG o_13001850[];

int PL_CheckTaking(PLAYER *pl)
{
	int result = 0;
	if (pl->status & PA_TAKEREQ)
	{
		OBJLANG *script = VirtualToSegment(SEG_OBJECT, pl->collide->script);
		if (script == o_13001850)
		{
			short dang = pl->ang[1] - pl->collide->o_angy;
			if (-0x5555 <= dang && dang <= 0x5555)
			{
				pl->ang[1] = pl->collide->o_angy;
				pl->attach = pl->collide;
				result = PL_SetState(pl, PS_TAKE_10, 0);
			}
		}
		else
		{
			short dang = PL_GetAngToObj(pl, pl->collide) - pl->ang[1];
			if (-0x2AAA <= dang && dang <= 0x2AAA)
			{
				pl->attach = pl->collide;
				if (!(pl->state & PF_JUMP)) PL_SetState(
					pl, (pl->state & PF_DIVE) ? PS_TAKE_05 : PS_TAKE_03, 0
				);
				result = 1;
			}
		}
	}
	return result;
}

static u32 PL_BumpObject(PLAYER *pl)
{
	BUMP pl_bump, ob_bump;
	SHORT pl_angy, ob_angy;
	short pl_dang;
	UNUSED short ob_dang;
	u32 state = PS_NULL;
	OBJECT *obj = pl->collide;
	float pl_power = obj->hit_r * 3/53;
	float ob_power = 53 / obj->hit_r;
	BumpInit(
		&pl_bump, pl->pos[0], pl->pos[2], pl->speed, pl->ang[1], pl_power, 50+2
	);
	BumpInit(
		&ob_bump, obj->o_posx, obj->o_posz, obj->o_velf, obj->o_angy,
		ob_power, obj->hit_r+2
	);
	if (pl->speed != 0) BumpCollision(&pl_bump, &ob_bump);
	else                BumpCollision(&ob_bump, &pl_bump);
	pl_angy = ATAN2(pl_bump.velz, pl_bump.velx);
	ob_angy = ATAN2(ob_bump.velz, ob_bump.velx);
	pl_dang = pl_angy - pl->ang[1];
	ob_dang = ob_angy - obj->o_angy;
	pl->ang[1] = pl_angy;
	pl->speed = DIST2(pl_bump.velx, pl_bump.velz);
	pl->pos[0] = pl_bump.posx;
	pl->pos[2] = pl_bump.posz;
	obj->o_angy = ob_angy;
	obj->o_velf = DIST2(ob_bump.velx, ob_bump.velz);
	obj->o_posx = ob_bump.posx;
	obj->o_posz = ob_bump.posz;
	if (!(-0x4000 <= pl_dang && pl_dang <= 0x4000))
	{
		pl->ang[1] += 0x8000;
		pl->speed *= -1;
		if (pl->state & PF_JUMP)    state = PS_JUMP_30;
		else                        state = PS_MOVE_24;
	}
	else
	{
		if (pl->state & PF_JUMP)    state = PS_JUMP_31;
		else                        state = PS_MOVE_25;
	}
	return state;
}

static void PL_Stomp(PLAYER *pl, OBJECT *obj, float vely)
{
	pl->pos[1] = obj->o_posy + obj->hit_h;
	pl->vel[1] = vely;
	pl->flag &= ~PL_00000100;
	Na_ObjSePlay(NA_SE0_59, pl->obj);
}

static void PL_HeadAttack(PLAYER *pl, UNUSED OBJECT *obj)
{
	pl->vel[1] = 0;
	camera_8027F590(8);
}

UNUSED
static u32 PL_GetBlowState(PLAYER *pl)
{
	u32 state;
	SHORT angy = PL_GetAngToObj(pl, pl->collide);
	short dang = angy - pl->ang[1];
	if (pl->speed < 16) pl->speed = 16;
	pl->ang[1] = angy;
	if (-0x4000 <= dang && dang <= 0x4000)
	{
		pl->speed *= -1;
		if (pl->state & (PF_JUMP|PF_POLE|PF_ROOF))  state = PS_JUMP_30;
		else                                        state = PS_MOVE_24;
	}
	else
	{
		pl->ang[1] += 0x8000;
		if (pl->state & (PF_JUMP|PF_POLE|PF_ROOF))  state = PS_JUMP_31;
		else                                        state = PS_MOVE_25;
	}
	return state;
}

static u32 PL_GetDamageState(PLAYER *pl, UNUSED int ap)
{
	u32 state;
	SHORT i = 0, n = 0;
	SHORT angy = PL_GetAngToObj(pl, pl->collide);
	short dang = angy - pl->ang[1];
	SHORT power = pl->power - 64*pl->damage;
	if      (pl->state & (PF_SWIM|PF_SINK))         i = 2;
	else if (pl->state & (PF_JUMP|PF_POLE|PF_ROOF)) i = 1;
	if      (power < 0x100)             n = 2;
	else if (pl->collide->o_ap >= 4)    n = 2;
	else if (pl->collide->o_ap >= 2)    n = 1;
	pl->ang[1] = angy;
	if (i == 2)
	{
		if (pl->speed < 28) PL_SetSpeed(pl, 28);
		if (pl->pos[1] >= pl->collide->o_posy)
		{
			if (pl->vel[1] < 20) pl->vel[1] = 20;
		}
		else
		{
			if (pl->vel[1] > 0) pl->vel[1] = 0;
		}
	}
	else
	{
		if (pl->speed < 16) PL_SetSpeed(pl, 16);
	}
	if (-0x4000 <= dang && dang <= 0x4000)
	{
		pl->speed *= -1;
		state = bdamagetab[i][n];
	}
	else
	{
		pl->ang[1] += 0x8000;
		state = fdamagetab[i][n];
	}
	return state;
}

static void PL_RepelFromObj(PLAYER *pl, OBJECT *obj, float gap)
{
	float dist = obj->hit_r + pl->obj->hit_r + gap;
	float dx = pl->pos[0] - obj->o_posx;
	float dz = pl->pos[2] - obj->o_posz;
	float d = DIST2(dx, dz);
	if (d < dist)
	{
		BGFACE *ground;
		SHORT angy;
		float posx, posz;
		if (d == 0) angy = pl->ang[1];
		else        angy = ATAN2(dz, dx);
		posx = obj->o_posx + dist*SIN(angy);
		posz = obj->o_posz + dist*COS(angy);
		BGHitWall(&posx, &pl->pos[1], &posz, 60, 50);
		BGCheckGround(posx, pl->pos[1], posz, &ground);
		if (ground)
		{
			pl->pos[0] = posx;
			pl->pos[2] = posz;
		}
	}
}

static void PL_PunchKickRecoil(PLAYER *pl, int attack)
{
	if (attack & (PH_PUNCH|PH_KICK|PH_SWEEPKICK))
	{
		if (pl->state == PS_TAKE_00) pl->state = PS_MOVE_17;
		if (pl->state & PF_JUMP)    PL_SetSpeed(pl, -16);
		else                        PL_SetSpeed(pl, -48);
		camera_8027F590(1);
		pl->effect |= PE_00040000;
	}
	if (attack & (PH_PUNCH|PH_KICK|PH_SWEEPKICK|PH_SLIDING))
	{
		Na_ObjSePlay(NA_SE0_44_B, pl->obj);
	}
}

static int PL_GetDoorCode(PLAYER *pl, OBJECT *obj)
{
	float dx = obj->o_posx - pl->pos[0];
	float dz = obj->o_posz - pl->pos[2];
	short dang = obj->o_angy - ATAN2(dz, dx);
	return -0x4000 <= dang && dang <= 0x4000 ? 1 : 2;
}

static int PL_TakeDamage(PLAYER *pl)
{
	int sp1C, ap = pl->collide->o_ap;
	if      (ap >= 4) sp1C = 5;
	else if (ap >= 2) sp1C = 4;
	else              sp1C = 3;
	if (!(pl->flag & PL_HEADCAP)) ap += (ap+1) / 2;
	if (pl->flag & PL_METALCAP) ap = 0;
	pl->damage += 4*ap;
	camera_8027F590(sp1C);
	return ap;
}

static int PL_CheckDamage(PLAYER *pl, OBJECT *obj)
{
	if (!invincible && !(pl->flag & PL_VANISHCAP) && !(obj->o_hit_flag & 2))
	{
		int ap;
		obj->o_hit_result = 0x2000|0x8000; /* T:hit_result */
		pl->collide = obj;
		ap = PL_TakeDamage(pl);
		if (obj->o_hit_flag & 8) pl->speed = 40;
		if (obj->o_ap > 0) Na_ObjSePlay(NA_SE2_0A, pl->obj);
		player_802521A0(pl);
		return PL_SetStateDrop(pl, PL_GetDamageState(pl, obj->o_ap), ap);
	}
	return 0;
}

static void collision_8024DAAC(PLAYER *pl)
{
	if (
		pl->state == PS_JUMP_09 ||
		pl->state == PS_JUMP_18 ||
		pl->state == PS_JUMP_19
	)
	{
		camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1);
		pl->ang[0] = 0;
	}
}

static int PL_CollideCoin(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	pl->coin += obj->o_ap;
	pl->recover += 4*obj->o_ap;
	obj->o_hit_result = 0x8000; /* T:hit_result */
	if (course_index >= COURSE_MIN && course_index < COURSE_EXT)
	{
		if (pl->coin-obj->o_ap < 100 && pl->coin >= 100) object_a_802AB558(6);
	}
	return 0;
}

static int PL_CollideRecover(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	pl->recover += 4*obj->o_ap;
	obj->o_hit_result = 0x8000; /* T:hit_result */
	return 0;
}

extern OBJLANG o_130038B0[];

static int PL_CollideStar(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	int level;
	u32 state = PS_DEMO_02;
	int stay = (obj->o_hit_flag & 0x400) != 0;
	int sp18 = (obj->o_hit_flag & 0x800) != 0;
	if (pl->power >= 0x100)
	{
		PL_DropAll(pl);
		if (!stay)
		{
			pl->damage = 0;
			pl->recover = 0;
			if (pl->cap_timer > 1) pl->cap_timer = 1;
		}
		if (stay) state = PS_DEMO_07;
		if (pl->state & PF_SWIM) state = PS_DEMO_03;
		if (pl->state & PF_SINK) state = PS_DEMO_03;
		if (pl->state & PF_JUMP) state = PS_DEMO_04;
		ObjMakeHere(obj, 0, o_130038B0);
		obj->o_hit_result = 0x8000; /* T:hit_result */
		pl->collide = obj;
		pl->attach = obj;
		level = ObjGetArg(obj) & 31;
		BuSet(pl->coin, level);
		pl->star = BuStarTotal();
		if (!stay)
		{
			Na_game_80321D38();
			AudFadeoutBGM(NA_TIME(16));
		}
		Na_ObjSePlay(NA_SE7_1E, pl->obj);
#if REVISION > 199606
		player_802521A0(pl);
#endif
		if (sp18) return PL_SetState(pl, PS_DEMO_09, 0);
		return PL_SetState(pl, state, (sp18 << 1) + stay);
	}
	return 0;
}

static int PL_CollideCage(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	if (pl->state != PS_DEMO_35 && pl->state != PS_DEMO_34)
	{
		PL_DropAll(pl);
		obj->o_hit_result = 0x8000; /* T:hit_result */
		pl->collide = obj;
		pl->attach = obj;
		if (pl->state & PF_JUMP) return PL_SetState(pl, PS_DEMO_35, 0);
		return PL_SetState(pl, PS_DEMO_34, 0);
	}
	return 0;
}

extern MAP map_pipe[];

static int PL_CollidePipe(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	if (obj->o_hit_flag & 1)
	{
		u32 state = pl->state;
		if (state == PS_DEMO_37)
		{
			pipe_flag = TRUE;
		}
		else if (!pipe_flag && (
			state == PS_WAIT_01 ||
			state == PS_WAIT_05 ||
			state == PS_WAIT_09 ||
			state == PS_WAIT_20
		))
		{
			pl->collide = obj;
			pl->attach = obj;
			pipe_flag = TRUE;
			return PL_SetState(pl, PS_DEMO_36, 0);
		}
	}
	else
	{
		if (pl->state != PS_DEMO_23)
		{
			obj->o_hit_result = 0x8000; /* T:hit_result */
			pl->collide = obj;
			pl->attach = obj;
			Na_ObjSePlay(
				obj->map == SegmentToVirtual(map_pipe) ? NA_SE7_16 : NA_SE7_19,
				pl->obj
			);
			PL_StopRide(pl);
			return PL_SetState(pl, PS_DEMO_00, 4 << 16 | 2);
		}
	}
	return 0;
}

static int PL_CollidePortDoor(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	u32 state = PS_NULL;
	u32 flag = BuGetFlag();
	SHORT arg = ObjGetArg(obj);
	if (pl->state == PS_MOVE_00 || pl->state == PS_MOVE_0A)
	{
		if (arg == 1 && !(flag & BU_KEYDOOR2))
		{
			if (!(flag & BU_KEY2))
			{
				if (!door_flag) PL_SetState(
					pl, PS_DEMO_05, (flag & BU_KEY1) ? 23 : 22
				);
				door_flag = TRUE;
				return 0;
			}
			state = PS_DEMO_2E;
		}
		if (arg == 2 && !(flag & BU_KEYDOOR1))
		{
			if (!(flag & BU_KEY1))
			{
				if (!door_flag) PL_SetState(
					pl, PS_DEMO_05, (flag & BU_KEY2) ? 23 : 22
				);
				door_flag = TRUE;
				return 0;
			}
			state = PS_DEMO_2E;
		}
		if (pl->state == PS_MOVE_00 || pl->state == PS_MOVE_0A)
		{
			u32 code = 4 + PL_GetDoorCode(pl, obj);
			if (state == PS_NULL)
			{
				if (code & 1)   state = PS_DEMO_20;
				else            state = PS_DEMO_21;
			}
			pl->collide = obj;
			pl->attach = obj;
			return PL_SetState(pl, state, code);
		}
	}
	return 0;
}

u32 PL_GetStarDoorFlag(OBJECT *obj)
{
	u32 flag = 0;
	SHORT arg = ObjGetArg(obj);
	SHORT isleft = obj->o_posx < 0;
	SHORT istop = obj->o_posy > 500;
	switch (arg)
	{
	case 1:
		if (istop)  flag = BU_STARDOOR1T;
		else        flag = BU_STARDOOR1B;
		break;
	case 3:
		if (isleft) flag = BU_STARDOOR3L;
		else        flag = BU_STARDOOR3R;
		break;
	case 8:
		flag = BU_STARDOOR8;
		break;
	case 30:
		flag = BU_STARDOOR30;
		break;
	case 50:
		flag = BU_STARDOOR50;
		break;
	}
	return flag;
}

static int PL_CollideDoor(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	SHORT arg = ObjGetArg(obj);
	SHORT star = BuStarTotal();
	if (pl->state == PS_MOVE_00 || pl->state == PS_MOVE_0A)
	{
		if (star >= arg)
		{
			u32 code = PL_GetDoorCode(pl, obj);
			u32 state, flag;
			if (code & 1)   state = PS_DEMO_20;
			else            state = PS_DEMO_21;
			flag = PL_GetStarDoorFlag(obj);
			pl->collide = obj;
			pl->attach = obj;
			if (obj->o_hit_flag & 0x20) state = PS_DEMO_31;
			if (flag && !(BuGetFlag() & flag)) state = PS_DEMO_2F;
			return PL_SetState(pl, state, code);
		}
		else if (!door_flag)
		{
			u32 code = 22 << 16;
			switch (arg)
			{
			case  1: code = 24 << 16; break;
			case  3: code = 25 << 16; break;
			case  8: code = 26 << 16; break;
			case 30: code = 27 << 16; break;
			case 50: code = 28 << 16; break;
			case 70: code = 29 << 16; break;
			}
			code += arg - star;
			door_flag = TRUE;
			return PL_SetState(pl, PS_DEMO_05, code);
		}
	}
	else if (pl->state == PS_WAIT_01)
	{
		if (ISTRUE(door_flag) && arg == 70)
		{
			pl->collide = obj;
			pl->attach = obj;
			return PL_SetState(pl, PS_DEMO_31, PL_GetDoorCode(pl, obj));
		}
	}
	return 0;
}

static int PL_CollideCannon(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	if (pl->state != PS_SPEC_31)
	{
		PL_DropAll(pl);
		obj->o_hit_result = 0x8000; /* T:hit_result */
		pl->collide = obj;
		pl->attach = obj;
		return PL_SetState(pl, PS_SPEC_31, 0);
	}
	return 0;
}

static int PL_CollideIgloo(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	pl->collide = obj;
	pl->attach = obj;
	PL_RepelFromObj(pl, obj, 5);
	return 0;
}

static int PL_CollideTornado(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	OBJECT *pl_obj = pl->obj;
	if (pl->state != PS_SPEC_32 && pl->state != PS_DEMO_39)
	{
		PL_DropAll(pl);
		PL_SetSpeed(pl, 0);
		player_802521A0(pl);
		obj->o_hit_result = 0x8000; /* T:hit_result */
		pl->collide = obj;
		pl->attach = obj;
		pl_obj->o_v6 = 0x400;
		pl_obj->o_f7 = pl->pos[1] - obj->o_posy;
		Na_ObjSePlay(NA_SE2_10, pl->obj);
		return PL_SetState(pl, PS_SPEC_32, pl->state == PS_JUMP_24);
	}
	return 0;
}

static int PL_CollideWhirlpool(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	OBJECT *pl_obj = pl->obj;
	if (pl->state != PS_SWIM_23)
	{
		PL_DropAll(pl);
		obj->o_hit_result = 0x8000; /* T:hit_result */
		pl->collide = obj;
		pl->attach = obj;
		pl->speed = 0;
		pl_obj->o_f7 = pl->pos[1] - obj->o_posy;
		Na_ObjSePlay(NA_SE2_10, pl->obj);
		return PL_SetState(pl, PS_SWIM_23, 0);
	}
	return 0;
}

static int PL_CollideWind(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	UNUSED OBJECT *pl_obj = pl->obj;
	if (pl->state != PS_JUMP_38)
	{
		PL_DropAll(pl);
		obj->o_hit_result = 0x8000; /* T:hit_result */
		pl->collide = obj;
		pl->attach = obj;
		pl->ang[1] = obj->o_angy+0x8000;
		pl->gravity = 0.4F;
		pl->speed = -24;
		pl->vel[1] = 12;
		Na_ObjSePlay(NA_SE2_10, pl->obj);
		player_802521A0(pl);
		return PL_SetState(pl, PS_JUMP_38, 0);
	}
	return 0;
}

static int PL_CollideBurn(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	u32 state = PS_JUMP_34;
	if (
		!invincible &&
		!(pl->flag & PL_METALCAP) &&
		!(pl->flag & PL_VANISHCAP) &&
		!(obj->o_hit_flag & 2)
	)
	{
		obj->o_hit_result = 0x8000; /* T:hit_result */
		pl->collide = obj;
		if ((pl->state & (PF_SWIM|PF_SINK)) || pl->water-pl->pos[1] > 50)
		{
			Na_ObjSePlay(NA_SE3_03, pl->obj);
		}
		else
		{
			pl->obj->o_v7 = 0;
			player_802521A0(pl);
			Na_ObjSePlay(NA_SE2_14, pl->obj);
			if ((pl->state & PF_JUMP) && pl->vel[1] <= 0) state = PS_JUMP_35;
			return PL_SetStateDrop(pl, state, 1);
		}
	}
	return 0;
}

static int PL_CollideBullet(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	if (!invincible && !(pl->flag & PL_VANISHCAP))
	{
		if (pl->flag & PL_METALCAP)
		{
			obj->o_hit_result = 0x4000|0x8000; /* T:hit_result */
			Na_ObjSePlay(NA_SE0_58, pl->obj);
		}
		else
		{
			obj->o_hit_result = 0x2000|0x8000; /* T:hit_result */
			pl->collide = obj;
			PL_TakeDamage(pl);
			Na_ObjSePlay(NA_SE2_0A, pl->obj);
			player_802521A0(pl);
			return PL_SetStateDrop(
				pl, PL_GetDamageState(pl, obj->o_ap), obj->o_ap
			);
		}
	}
	if (!(obj->o_hit_flag & 2)) hit_enemy = TRUE;
	return 0;
}

static int PL_CollideClam(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	if (obj->o_hit_flag & 0x2000)
	{
		obj->o_hit_result = 0x8000; /* T:hit_result */
		pl->collide = obj;
		return PL_SetState(pl, PS_DEMO_17, 0);
	}
	else
	{
		if (PL_CheckDamage(pl, obj)) return 1;
	}
	if (!(obj->o_hit_flag & 2)) hit_enemy = TRUE;
	return 1;
}

static int PL_CollideBump(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	UNUSED int i;
	int attack;
	if (pl->flag & PL_METALCAP) attack = PH_SLIDING;
	else                        attack = PL_CheckAttack(pl, obj);
	pl->collide = obj;
	if (attack & PH_LOWATTACK)
	{
		PL_RepelFromObj(pl, obj, 5);
		pl->speed = -16;
		obj->o_angy = pl->ang[1];
		obj->o_velf = 3392 / obj->hit_r;
		ObjAttack(obj, attack);
		PL_PunchKickRecoil(pl, attack);
		return 1;
	}
	else if (
		!invincible &&
		!(pl->flag & PL_VANISHCAP) &&
		!(obj->o_hit_flag & 2)
	)
	{
		obj->o_hit_result = 0x8000; /* T:hit_result */
		pl->invincible = 2;
		player_802521A0(pl);
		Na_ObjSePlay(NA_SE2_09, pl->obj);
		Na_ObjSePlay(NA_SE5_17, pl->obj);
		PL_RepelFromObj(pl, obj, 5);
		PL_SetStateDrop(pl, PL_BumpObject(pl), 0);
		return 1;
	}
	return 0;
}

static int PL_CollideElecShock(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	if (!invincible && !(pl->flag & PL_VANISHCAP) && !(obj->o_hit_flag & 2))
	{
		u32 code = (pl->state & (PF_JUMP|PF_POLE|PF_ROOF)) == 0;
		obj->o_hit_result = 0x2000|0x8000; /* T:hit_result */
		pl->collide = obj;
		PL_TakeDamage(pl);
		Na_ObjSePlay(NA_SE2_0A, pl->obj);
		if (pl->state & (PF_SWIM|PF_SINK))
		{
			return PL_SetStateDrop(pl, PS_SWIM_08, 0);
		}
		else
		{
			player_802521A0(pl);
			return PL_SetStateDrop(pl, PS_DEMO_38, code);
		}
	}
	if (!(obj->o_hit_flag & 2)) hit_enemy = TRUE;
	return 0;
}

UNUSED
static int PL_CollideDummy(UNUSED PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	if (!(obj->o_hit_flag & 2)) hit_enemy = TRUE;
	return 0;
}

static int PL_CollideEnemy(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	if (PL_CheckDamage(pl, obj)) return 1;
	if (!(obj->o_hit_flag & 2)) hit_enemy = TRUE;
	return 0;
}

static int PL_CollideFlyEnemy(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	UNUSED int i;
	int attack;
	if (pl->flag & PL_METALCAP) attack = PH_SLIDING;
	else                        attack = PL_CheckAttack(pl, obj);
	if (attack & PH_ALLATTACK)
	{
		ObjAttack(obj, attack);
		PL_PunchKickRecoil(pl, attack);
		if (attack & PH_HEADATTACK) PL_HeadAttack(pl, obj);
		if (attack & PH_STOMP)
		{
			if (obj->o_hit_flag & 0x80)
			{
				PL_Stomp(pl, obj, 80);
				collision_8024DAAC(pl);
#ifdef NEWVOICE
				Na_ObjSePlay(NA_SE2_34, pl->obj);
#endif
				return PL_SetStateDrop(pl, PS_JUMP_24, 0);
			}
			else
			{
				PL_Stomp(pl, obj, 30);
			}
		}
	}
	else
	{
		if (PL_CheckDamage(pl, obj)) return 1;
	}
	if (!(obj->o_hit_flag & 2)) hit_enemy = TRUE;
	return 0;
}

static int PL_CollideBounce(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	int attack;
	if (pl->flag & PL_METALCAP) attack = PH_SLIDING;
	else                        attack = PL_CheckAttack(pl, obj);
	if (attack & PH_LOWATTACK)
	{
		ObjAttack(obj, attack);
		PL_PunchKickRecoil(pl, attack);
		if (attack & PH_STOMP)
		{
			if (obj->o_hit_flag & 0x80)
			{
				PL_Stomp(pl, obj, 80);
				collision_8024DAAC(pl);
#ifdef NEWVOICE
				Na_ObjSePlay(NA_SE2_34, pl->obj);
#endif
				return PL_SetStateDrop(pl, PS_JUMP_24, 0);
			}
			else
			{
				PL_Stomp(pl, obj, 30);
			}
		}
	}
	else
	{
		if (PL_CheckDamage(pl, obj)) return 1;
	}
	if (!(obj->o_hit_flag & 2)) hit_enemy = TRUE;
	return 0;
}

static int PL_CollideSpiny(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	int attack = PL_CheckAttack(pl, obj);
	if (attack & PH_PUNCH)
	{
		obj->o_hit_result = 1|0x4000|0x8000; /* T:hit_result */
		PL_PunchKickRecoil(pl, attack);
	}
	else
	{
		if (PL_CheckDamage(pl, obj)) return 1;
	}
	if (!(obj->o_hit_flag & 2)) hit_enemy = TRUE;
	return 0;
}

static int PL_CollideDamage(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	if (PL_CheckDamage(pl, obj)) return 1;
	if (!(obj->o_hit_flag & 2)) hit_enemy = TRUE;
	return 0;
}

static int PL_CollideItemBox(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	int attack = PL_CheckAttack(pl, obj);
	if (attack & (PH_POUND|PH_PUNCH|PH_KICK|PH_SWEEPKICK|PH_HEADATTACK))
	{
		ObjAttack(obj, attack);
		PL_PunchKickRecoil(pl, attack);
		pl->collide = obj;
		switch (attack)
		{
		case PH_STOMP:      PL_Stomp(pl, obj, 30); break;
		case PH_HEADATTACK: PL_HeadAttack(pl, obj); break;
		}
		return 1;
	}
	return 0;
}

static int PL_CollideShell(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	if (!(pl->state & PF_RIDE))
	{
		int attack = PL_CheckAttack(pl, obj);
		if (
			attack == PH_STOMP ||
			pl->state == PS_MOVE_00 || pl->state == PS_MOVE_02
		)
		{
			pl->collide = obj;
			pl->attach = obj;
			pl->ride = obj;
			ObjAttack(obj, attack);
			player_802521A0(pl);
			AudPlayShellBGM();
			PL_DropObject(pl);
			return PL_SetState(pl, PS_MOVE_06, 0);
		}
		PL_RepelFromObj(pl, obj, 2);
	}
	return 0;
}

static int PL_CheckTaken(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	if (!(pl->state & (PF_JUMP|PF_DMGE|PF_ATCK)) || !invincible)
	{
		if (obj->o_hit_flag & 4)
		{
			if (PL_IsFacingObj(pl, obj, 0x2AAA))
			{
				PL_DropAll(pl);
				obj->o_hit_result = 0x800|0x8000; /* T:hit_result */
				pl->ang[1] = obj->o_angy;
				pl->collide = obj;
				pl->attach = obj;
				player_802521A0(pl);
				Na_ObjSePlay(NA_SE2_0B, pl->obj);
				return PL_SetState(pl, PS_SPEC_30, 0);
			}
		}
	}
	PL_RepelFromObj(pl, obj, -5);
	return 0;
}

static int PL_CollidePole(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	int sp24 = pl->state & PS_MASK;
	if (sp24 >= PC_JUMP+0x00 && sp24 < PC_JUMP+0x20)
	{
		if (!(pl->prevstate & PF_POLE) || pl->attach != obj)
		{
			int sp20 = pl->speed <= 10;
			OBJECT *pl_obj = pl->obj;
			PL_DropAll(pl);
			pl->collide = obj;
			pl->attach = obj;
			pl->vel[1] = 0;
			pl->speed = 0;
			pl_obj->o_v5 = 0;
			pl_obj->o_v6 = 0;
			pl_obj->o_f7 = pl->pos[1] - obj->o_posy;
			if (sp20) return PL_SetState(pl, PS_SPEC_01, 0);
			pl_obj->o_v6 = 0x1000 + 0x100*pl->speed;
			collision_8024DAAC(pl);
			return PL_SetState(pl, PS_SPEC_02, 0);
		}
	}
	return 0;
}

static int PL_CollideHang(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	int sp1C = pl->state & PS_MASK;
	if (sp1C >= PC_JUMP+0x00 && sp1C < PC_JUMP+0x18)
	{
		if (gfx_frame - pl->attach->o_v7 > 30)
		{
			PL_DropAll(pl);
			obj->o_hit_result = 1; /* T:hit_result */
			pl->collide = obj;
			pl->attach = obj;
			player_802521A0(pl);
			return PL_SetState(pl, PS_JUMP_28, 0);
		}
	}
	return 0;
}

static int PL_CollideCap(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	u32 flag = ObjGetCapFlag(obj);
	USHORT bgm = 0;
	USHORT timer = 0;
	if (pl->state != PS_JUMP_38 && flag)
	{
		pl->collide = obj;
		obj->o_hit_result = 0x8000; /* T:hit_result */
		pl->flag &= ~(PL_HEADCAP|PL_HANDCAP);
		pl->flag |= flag;
		switch (flag)
		{
		case PL_VANISHCAP:  timer = 30*20; bgm = NA_BGM_SPECIAL; break;
		case PL_METALCAP:   timer = 30*20; bgm = NA_BGM_METAL;   break;
		case PL_WINGCAP:    timer = 30*60; bgm = NA_BGM_SPECIAL; break;
		}
		if (timer > pl->cap_timer) pl->cap_timer = timer;
		if ((pl->state & PF_READ) || pl->state == PS_MOVE_00)
		{
			pl->flag |= PL_HANDCAP;
			PL_SetState(pl, PS_DEMO_3D, 0);
		}
		else
		{
			pl->flag |= PL_HEADCAP;
		}
		Na_ObjSePlay(NA_SE7_1E, pl->obj);
		Na_ObjSePlay(NA_SE2_0C, pl->obj);
		if (bgm) AudPlaySpecialBGM(bgm);
		return 1;
	}
	return 0;
}

static int PL_CollideTake(PLAYER *pl, u32 type, OBJECT *obj)
{
	OBJLANG *script = VirtualToSegment(SEG_OBJECT, obj->script);
	if (obj->o_hit_flag & 0x100)
	{
		int attack = PL_CheckAttack(pl, obj);
		if (attack & (PH_KICK|PH_SWEEPKICK))
		{
			ObjAttack(obj, attack);
			PL_PunchKickRecoil(pl, attack);
			return 0;
		}
	}
	if (obj->o_hit_flag & 4)
	{
		if (PL_CheckTaken(pl, type, obj)) return 1;
	}
	if (PL_IsTaking(pl, obj) && !(obj->o_hit_flag & 0x200))
	{
		pl->collide = obj;
		pl->status |= PA_TAKEREQ;
		return 1;
	}
	if (script != o_13001850) PL_RepelFromObj(pl, obj, -5);
	return 0;
}

static int PL_CanOpenMessage(PLAYER *pl, int flag)
{
	SHORT anime;
	if (pl->state & PF_READ) return TRUE;
	if (pl->state == PS_MOVE_00)
	{
		if (flag) return TRUE;
		anime = pl->obj->s.skel.index;
		if (anime == 128 || anime == 127 || anime == 108) return TRUE;
	}
	return FALSE;
}

static int PL_CheckReading(PLAYER *pl, OBJECT *obj)
{
	if (
		(pl->status & PA_READREQ) &&
		PL_CanOpenMessage(pl, FALSE) &&
		PL_IsFacingObj(pl, obj, 0x4000)
	)
	{
		short dang = (SHORT)(obj->o_angy+0x8000) - pl->ang[1];
		float posx, posz;
#if REVISION > 199606
		if (-0x4000 <= dang && dang <= 0x4000)
#else
		if (-0x38E3 <= dang && dang <= 0x38E3)
#endif
		{
			posx = obj->o_posx + 105*SIN(obj->o_angy);
			posz = obj->o_posz + 105*COS(obj->o_angy);
			pl->obj->o_v5 = dang;
			pl->obj->o_f6 = posx - pl->pos[0];
			pl->obj->o_f7 = posz - pl->pos[2];
			pl->collide = obj;
			pl->attach = obj;
			return PL_SetState(pl, PS_DEMO_08, 0);
		}
	}
	return 0;
}

static int PL_CheckTalking(PLAYER *pl, OBJECT *obj)
{
	if ((pl->status & PA_READREQ) && PL_CanOpenMessage(pl, TRUE))
	{
		short dang = (SHORT)PL_GetAngToObj(pl, obj) - pl->ang[1];
		if (-0x4000 <= dang && dang <= 0x4000)
		{
			obj->o_hit_result = 0x8000; /* T:hit_result */
			pl->collide = obj;
			pl->attach = obj;
			PL_RepelFromObj(pl, obj, -10);
			return PL_SetState(pl, PS_DEMO_0A, 0);
		}
	}
	PL_RepelFromObj(pl, obj, -10);
	return 0;
}

static int PL_CollideMessage(PLAYER *pl, UNUSED u32 type, OBJECT *obj)
{
	int result = 0;
	if (obj->o_hit_flag & 0x1000)
	{
		result = PL_CheckReading(pl, obj);
	}
	else if (obj->o_hit_flag & 0x4000)
	{
		result = PL_CheckTalking(pl, obj);
	}
	else
	{
		PL_RepelFromObj(pl, obj, 2);
	}
	return result;
}

static void PL_CheckPunchKickWall(PLAYER *pl)
{
	if (pl->flag & (PL_PUNCH|PL_KICK|PL_SWEEPKICK))
	{
		FVEC pos;
		pos[0] = pl->pos[0] + 50*SIN(pl->ang[1]);
		pos[2] = pl->pos[2] + 50*COS(pl->ang[1]);
		pos[1] = pl->pos[1];
		if (PL_CheckWall(pos, 80, 5))
		{
			if (pl->state != PS_MOVE_17 || pl->speed >= 0)
			{
				if (pl->state == PS_TAKE_00) pl->state = PS_MOVE_17;
				PL_SetSpeed(pl, -48);
				Na_ObjSePlay(NA_SE0_44_B, pl->obj);
				pl->effect |= PE_00040000;
			}
			else if (pl->state & PF_JUMP)
			{
				PL_SetSpeed(pl, -16);
				Na_ObjSePlay(NA_SE0_44_B, pl->obj);
				pl->effect |= PE_00040000;
			}
		}
	}
}

void PL_CheckCollision(PLAYER *pl)
{
	int i;
	hit_enemy = FALSE;
	invincible = (pl->state & PF_DMGE) || pl->invincible;
	if (!(pl->state & PF_DEMO) && pl->hit_status)
	{
		for (i = 0; i < (int)lenof(collisiontab); i++)
		{
			u32 type = collisiontab[i].type;
			if (pl->hit_status & type)
			{
				OBJECT *obj = PL_GetHitObj(pl, type);
				pl->hit_status &= ~type;
				if (!(obj->o_hit_result & 0x8000)) /* T:hit_result */
				{
					if (collisiontab[i].proc(pl, type, obj)) break;
				}
			}
		}
	}
	if (pl->invincible > 0 && !hit_enemy) pl->invincible--;
	PL_CheckPunchKickWall(pl);
	pl->flag &= ~(PL_PUNCH|PL_KICK|PL_SWEEPKICK);
	if (!(pl->obj->hit_status & (HIT_DOOR|HIT_PORTDOOR))) door_flag = FALSE;
	if (!(pl->obj->hit_status & HIT_PIPE)) pipe_flag = FALSE;
}

static void PL_CheckFall(PLAYER *pl)
{
	if (pl->pos[1] < pl->ground_y+2048)
	{
		if (PL_Fade(pl, FADE_FALL) == 20)
		{
			if (!(pl->flag & PL_00040000)) Na_ObjSePlay(NA_SE2_10, pl->obj);
		}
	}
}

static void PL_GroundBurn(PLAYER *pl)
{
	if (!(pl->state & PF_RIDE) && pl->pos[1] < pl->ground_y+10)
	{
		if (!(pl->flag & PL_METALCAP))
		{
			pl->damage += (pl->flag & PL_HEADCAP) ? 4*3 : 4*4+2;
		}
		player_802521A0(pl);
		PL_SetStateDrop(pl, PS_JUMP_37, 0);
	}
}

static void PL_StartTimer(UNUSED PLAYER *pl)
{
	if (!(hud.flag & HUD_TIME))
	{
		GmTimeShow();
		GmTimeStart();
		silder_flag = TRUE;
	}
}

static void PL_StopTimer(PLAYER *pl)
{
	if (silder_flag)
	{
		USHORT t = GmTimeStop();
		if (t < 30*21)
		{
			ObjSetArg(pl->obj, 1);
			object_b_802F2B88(-6358, -4300, 4700);
		}
		silder_flag = FALSE;
	}
}

void PL_CheckGroundCollision(PLAYER *pl)
{
	if ((pl->state & PC_MASK) == PC_DEMO) return;
	if (pl->ground)
	{
		int code = pl->ground->code;
		switch (code)
		{
		case BG_10:
		case BG_56:
			PL_CheckFall(pl);
			break;
		case BG_50:
			PL_Fade(pl, FADE_FALL);
			break;
		case BG_51:
			PL_StartTimer(pl);
			break;
		case BG_52:
			PL_StopTimer(pl);
			break;
		}
		if (!(pl->state & PF_JUMP) && !(pl->state & PF_SWIM))
		{
			switch (code)
			{
			case BG_1:
				PL_GroundBurn(pl);
				break;
			}
		}
	}
}
