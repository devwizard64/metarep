#include <sm64.h>

#ifdef DISK
#define BankLoad BankLoadAnime
#endif

int PL_IsAnimeLast1F(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	return obj->s.skel.frame+1 == obj->s.skel.anime->frame;
}

int PL_IsAnimeLast2F(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	return obj->s.skel.frame >= obj->s.skel.anime->frame-2;
}

int PL_SetAnime(PLAYER *pl, int index)
{
	OBJECT *obj = pl->obj;
	ANIME *anime = pl->anime->buf;
	if (BankLoad(pl->anime, index))
	{
		anime->val = (void *)K0_TO_PHYS((char *)anime + (long)anime->val);
		anime->tbl = (void *)K0_TO_PHYS((char *)anime + (long)anime->tbl);
	}
	if (obj->s.skel.index != index)
	{
		obj->s.skel.index = index;
		obj->s.skel.anime = anime;
		obj->s.skel.vspeed = 0;
		obj->s.skel.waist = pl->waist;
		if (anime->flag & ANIME_NOSTEP)
		{
			obj->s.skel.frame = anime->start;
		}
		else if (anime->flag & ANIME_REVERSE)
		{
			obj->s.skel.frame = anime->start + 1;
		}
		else
		{
			obj->s.skel.frame = anime->start - 1;
		}
	}
	return obj->s.skel.frame;
}

int PL_SetAnimeV(PLAYER *pl, int index, int vspeed)
{
	OBJECT *obj = pl->obj;
	ANIME *anime = pl->anime->buf;
	if (BankLoad(pl->anime, index))
	{
		anime->val = (void *)K0_TO_PHYS((char *)anime + (long)anime->val);
		anime->tbl = (void *)K0_TO_PHYS((char *)anime + (long)anime->tbl);
	}
	if (obj->s.skel.index != index)
	{
		obj->s.skel.index = index;
		obj->s.skel.anime = anime;
		obj->s.skel.waist = pl->waist;
		if (anime->flag & ANIME_NOSTEP)
		{
			obj->s.skel.vframe = (anime->start << 16);
		}
		else if (anime->flag & ANIME_REVERSE)
		{
			obj->s.skel.vframe = (anime->start << 16) + vspeed;
		}
		else
		{
			obj->s.skel.vframe = (anime->start << 16) - vspeed;
		}
		obj->s.skel.frame = obj->s.skel.vframe >> 16;
	}
	obj->s.skel.vspeed = vspeed;
	return obj->s.skel.frame;
}

void PL_SetAnimeFrame(PLAYER *pl, SHORT frame)
{
	SKELETON *skel = &pl->obj->s.skel;
	ANIME *anime = skel->anime;
	if (skel->vspeed)
	{
		if (anime->flag & ANIME_REVERSE)
		{
			skel->vframe = (frame << 16) + skel->vspeed;
		}
		else
		{
			skel->vframe = (frame << 16) - skel->vspeed;
		}
	}
	else
	{
		if (anime->flag & ANIME_REVERSE)
		{
			skel->frame = frame + 1;
		}
		else
		{
			skel->frame = frame - 1;
		}
	}
}

int PL_IsAnimeAtFrame(PLAYER *pl, SHORT frame)
{
	int result;
	int vframe = frame << 16;
	SKELETON *skel = &pl->obj->s.skel;
	ANIME *anime = skel->anime;
	if (skel->vspeed)
	{
		if (anime->flag & ANIME_REVERSE) result =
			skel->vframe > vframe && vframe >= skel->vframe - skel->vspeed;
		else result =
			skel->vframe < vframe && vframe <= skel->vframe + skel->vspeed;
	}
	else
	{
		if (anime->flag & ANIME_REVERSE)    result = skel->frame-1 == frame;
		else                                result = skel->frame+1 == frame;
	}
	return result;
}

SHORT ObjGetAnimePos(OBJECT *obj, SHORT angy, SVEC pos)
{
	float x, z;
	ANIME *anime = obj->s.skel.anime;
	SHORT frame = SkelStep(&obj->s.skel, NULL);
	u16   *tbl = SegmentToVirtual(anime->tbl);
	short *val = SegmentToVirtual(anime->val);
	float s = SIN(angy);
	float c = COS(angy);
	x      = val[AnimeIndex(frame, &tbl)] / 4.0F;
	pos[1] = val[AnimeIndex(frame, &tbl)] / 4.0F;
	z      = val[AnimeIndex(frame, &tbl)] / 4.0F;
	pos[0] =  x*c + z*s;
	pos[2] = -x*s + z*c;
	return anime->flag;
}

void PL_UseAnimePos(PLAYER *pl)
{
	SVEC pos;
	SHORT flag = ObjGetAnimePos(pl->obj, pl->ang[1], pos);
	if (flag & (ANIME_NOPOS|ANIME_Y))
	{
		pl->pos[0] += pos[0];
		pl->pos[2] += pos[2];
	}
	if (flag & (ANIME_NOPOS|ANIME_XZ))
	{
		pl->pos[1] += pos[1];
	}
}

SHORT PL_GetAnimeY(PLAYER *pl)
{
	SVEC pos;
	ObjGetAnimePos(pl->obj, 0, pos);
	return pos[1];
}

void PL_TrigSound(PLAYER *pl, Na_Se se, u32 flag)
{
	if (!(pl->flag & flag))
	{
		Na_ObjSePlay(se, pl->obj);
		pl->flag |= flag;
	}
}

void PL_TrigJumpVoice(PLAYER *pl)
{
	if (!(pl->flag & PL_VOICE))
	{
#if REVISION >= 199609
		if (pl->state == PS_JUMP_02)    Na_ObjSePlay(Na_Se2_2B(), pl->obj);
		else                            Na_ObjSePlay(Na_Se2_00(), pl->obj);
#else
		Na_ObjSePlay(Na_Se2_00(), pl->obj);
#endif
		pl->flag |= PL_VOICE;
	}
}

void PL_SetSpeedEffect(PLAYER *pl)
{
	int speed = ABS(pl->speed);
	Na_game_803218D8(1, MIN(100, speed));
}

void PL_PlayEffect(PLAYER *pl, Na_Se se, int flag)
{
	if (pl->surface == (2 << 16))
	{
		if (flag)   pl->effect |= PE_00001000;
		else        pl->effect |= PE_00000100;
	}
	else if (pl->surface == (7 << 16))
	{
		pl->effect |= PE_00008000;
	}
	else if (pl->surface == (5 << 16))
	{
		pl->effect |= PE_00004000;
	}
	if (pl->flag & PL_METALCAP || se == NA_SE0_43 || se == NA_SE2_1F)
	{
		Na_ObjSePlay(se, pl->obj);
	}
	else
	{
		Na_ObjSePlay(se + pl->surface, pl->obj);
	}
}

void PL_TrigEffect(PLAYER *pl, Na_Se se, int flag)
{
	if (!(pl->flag & PL_SOUND))
	{
		PL_PlayEffect(pl, se, flag);
		pl->flag |= PL_SOUND;
	}
}

void PL_PlayLandEffect(PLAYER *pl, Na_Se se)
{
	PL_PlayEffect(pl, pl->flag & PL_METALCAP ? NA_SE0_29 : se, TRUE);
}

void PL_TrigLandEffect(PLAYER *pl, Na_Se se)
{
	PL_TrigEffect(pl, pl->flag & PL_METALCAP ? NA_SE0_29 : se, TRUE);
}

void PL_PlayFallEffect(PLAYER *pl, Na_Se se)
{
	PL_PlayEffect(pl, pl->flag & PL_METALCAP ? NA_SE0_2B : se, TRUE);
}

void PL_TrigFallEffect(PLAYER *pl, Na_Se se)
{
	PL_TrigEffect(pl, pl->flag & PL_METALCAP ? NA_SE0_2B : se, TRUE);
}

void PL_TrigJumpEffect(PLAYER *pl, Na_Se se, Na_Se voice)
{
	if (se == NA_SE0_00) PL_TrigEffect(
		pl, pl->flag & PL_METALCAP ? NA_SE0_28 : NA_SE0_00, TRUE
	);
	else PL_TrigSound(pl, se, PL_SOUND);
	if (voice == PL_JUMPVOICE) PL_TrigJumpVoice(pl);
	if (voice != PL_NULLVOICE) PL_TrigSound(pl, voice, PL_VOICE);
}

void PL_SetSpeed(PLAYER *pl, float speed)
{
	pl->speed = speed;
	pl->slide_x = pl->speed * SIN(pl->ang[1]);
	pl->slide_z = pl->speed * COS(pl->ang[1]);
	pl->vel[0] = pl->slide_x;
	pl->vel[2] = pl->slide_z;
}

int PL_GetSlip(PLAYER *pl)
{
	int result = (pl->scene->env & ENV_MASK) == ENV_SLIDER ?
		SLIP_19 : SLIP_DEFAULT;
	if (pl->ground)
	{
		switch (pl->ground->code)
		{
		case BG_21:
		case BG_55:
		case BG_122:
			result = SLIP_21;
			break;
		case BG_20:
		case BG_42:
		case BG_53:
		case BG_121:
			result = SLIP_20;
			break;
		case BG_19:
		case BG_46:
		case BG_54:
		case BG_115:
		case BG_116:
		case BG_117:
		case BG_120:
			result = SLIP_19;
			break;
		}
	}
	if (
		pl->state == PS_WALK_08 && pl->ground->ny > 0.5F &&
		result == SLIP_DEFAULT
	) result = SLIP_21;
	return result;
}

u32 PL_GetSurface(PLAYER *pl)
{
	static char surfacetab[][6] =
	{
		{0, 3, 1, 1, 1, 0}, /* ENV_GRASS  */
		{3, 3, 3, 3, 1, 1}, /* ENV_ROCK   */
		{5, 6, 5, 6, 3, 3}, /* ENV_SNOW   */
		{7, 3, 7, 7, 3, 3}, /* ENV_SAND   */
		{4, 4, 4, 4, 3, 3}, /* ENV_GHOST  */
		{0, 3, 1, 6, 3, 6}, /* ENV_WATER  */
		{3, 3, 3, 3, 6, 6}, /* ENV_SLIDER */
	};
	SHORT index;
	SHORT env = pl->scene->env & ENV_MASK;
	Na_Se result = 0;
	if (pl->ground)
	{
		int code = pl->ground->code;
		if (stage_index != STAGE_LLL && pl->ground_y < pl->water-10)
		{
			result = 2 << 16;
		}
		else if (code >= BG_33 && code <= BG_39)
		{
			result = 7 << 16;
		}
		else
		{
			switch (code)
			{
			default:
				index = 0;
				break;
			case BG_21:
			case BG_48:
			case BG_55:
			case BG_122:
				index = 1;
				break;
			case BG_20:
			case BG_53:
			case BG_121:
				index = 2;
				break;
			case BG_19:
			case BG_46:
			case BG_54:
			case BG_115:
			case BG_116:
			case BG_117:
			case BG_120:
				index = 3;
				break;
			case BG_41:
				index = 4;
				break;
			case BG_42:
				index = 5;
				break;
			}
			result = surfacetab[env][index] << 16;
		}
	}
	return result;
}

BGFACE *PL_CheckWall(FVEC pos, float offset, float radius)
{
	WALLCHECK check;
	BGFACE *wall = NULL;
	check.x = pos[0];
	check.y = pos[1];
	check.z = pos[2];
	check.radius = radius;
	check.offset = offset;
	if (BGCheckWall(&check)) wall = check.wall[check.count-1];
	pos[0] = check.x;
	pos[1] = check.y;
	pos[2] = check.z;
	return wall;
}

float PL_CheckRoof(FVEC pos, float y, BGFACE **roof)
{
	UNUSED int i;
	return BGCheckRoof(pos[0], y+80, pos[2], roof);
}

int PL_IsFaceDownSlope(PLAYER *pl, int flag)
{
	short angy = pl->ang[1];
	if (flag && pl->speed < 0) angy += 0x8000;
	angy = pl->ground_ang - angy;
	return -0x4000 < angy && angy < 0x4000;
}

int PL_IsSlipMin(PLAYER *pl)
{
	float ny;
	if ((pl->scene->env & ENV_MASK) == ENV_SLIDER && pl->ground->ny < COS_1)
	{
		return TRUE;
	}
	switch (PL_GetSlip(pl))
	{
	case SLIP_19:   ny = COS_10; break;
	case SLIP_20:   ny = COS_20; break;
	default:        ny = COS_38; break;
	case SLIP_21:   ny = COS_90; break;
	}
	return pl->ground->ny <= ny;
}

int PL_IsSlipMax(PLAYER *pl)
{
	float ny;
	if ((pl->scene->env & ENV_MASK) == ENV_SLIDER && pl->ground->ny < COS_1)
	{
		return TRUE;
	}
	switch (PL_GetSlip(pl))
	{
	case SLIP_19:   ny = COS_5;  break;
	case SLIP_20:   ny = COS_10; break;
	default:        ny = COS_15; break;
	case SLIP_21:   ny = COS_20; break;
	}
	return pl->ground->ny <= ny;
}

static int PL_IsSlipJump(PLAYER *pl)
{
	float ny;
	int result = FALSE;
	if (!PL_IsFaceDownSlope(pl, FALSE))
	{
		switch (PL_GetSlip(pl))
		{
		case SLIP_19:   ny = COS_15; break;
		case SLIP_20:   ny = COS_20; break;
		default:        ny = COS_30; break;
		case SLIP_21:   ny = COS_30; break;
		}
		result = pl->ground->ny <= ny;
	}
	return result;
}

float PL_CheckGroundYNear(PLAYER *pl, SHORT angy, float dist)
{
	BGFACE *ground;
	float ground_y;
	float dx = dist * SIN(pl->ang[1]+angy);
	float dz = dist * COS(pl->ang[1]+angy);
	ground_y = BGCheckGround(
		pl->pos[0]+dx, pl->pos[1]+100, pl->pos[2]+dz, &ground
	);
	return ground_y;
}

SHORT PL_GetGroundAngX(PLAYER *pl, SHORT angy)
{
	BGFACE *ground;
	float level_f, level_b, dist_f, dist_b;
	SHORT angx;
	float dx = 5 * SIN(pl->ang[1]+angy);
	float dz = 5 * COS(pl->ang[1]+angy);
	level_f = BGCheckGround(
		pl->pos[0]+dx, pl->pos[1]+100, pl->pos[2]+dz, &ground
	);
	level_b = BGCheckGround(
		pl->pos[0]-dx, pl->pos[1]+100, pl->pos[2]-dz, &ground
	);
	dist_f = level_f - pl->pos[1];
	dist_b = pl->pos[1] - level_b;
	if (dist_f*dist_f < dist_b*dist_b)  angx = ATAN2(5, dist_f);
	else                                angx = ATAN2(5, dist_b);
	return angx;
}

void player_802521A0(PLAYER *pl)
{
	u32 state = pl->state;
	int mode = pl->scene->cam->mode;
	if (state == PS_WAIT_27)
	{
		AudClrMute(AUD_QUIET);
		camera_8033C848 &= ~0x2000;
		camera_80286188(pl->scene->cam, -1, 1); /* T:enum */
	}
	else if (state == PS_WAIT_03)
	{
		AudClrMute(AUD_QUIET);
	}
	if (!(state & (PF_SWIM|PF_SINK)) && (mode == 3 || mode == 8)) /* T:enum */
	{
		camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1);
	}
}

static void PL_SetSlipJump(PLAYER *pl)
{
	pl->obj->o_v7 = pl->ang[1];
	if (pl->speed > 0)
	{
		SHORT ground_ang = pl->ground_ang + 0x8000;
		SHORT angy = pl->ang[1] - ground_ang;
		float dx = pl->speed * SIN(angy);
		float dz = pl->speed * COS(angy) * 0.75F;
		pl->speed = DIST2(dx, dz);
		pl->ang[1] = ATAN2(dz, dx) + ground_ang;
	}
	PL_SetStateDrop(pl, PS_JUMP_05, 0);
}

static void PL_SetJumpSpeed(PLAYER *pl, float speed, float scale)
{
	pl->vel[1] = PL_GetTrampolinePower() + speed + pl->speed*scale;
	if (pl->press || pl->sink > 1) pl->vel[1] *= 0.5F;
}

static u32 PL_SetJump(PLAYER *pl, u32 state, u32 code)
{
	float speed;
	if (pl->press || pl->sink >= 1)
	{
		if (state == PS_JUMP_01 || state == PS_JUMP_24) state = PS_JUMP_00;
	}
	switch (state)
	{
	case PS_JUMP_01:
		PL_SetJumpSpeed(pl, 52, 0.25F);
		pl->speed *= 0.8F;
		break;
	case PS_JUMP_03:
		pl->obj->s.skel.index = -1;
		pl->speed = -16;
		PL_SetJumpSpeed(pl, 62, 0);
		break;
	case PS_JUMP_02:
		PL_SetJumpSpeed(pl, 69, 0);
		pl->speed *= 0.8F;
		break;
	case PS_JUMP_14:
		PL_SetJumpSpeed(pl, 82, 0);
		break;
	case PS_JUMP_09:
	case PS_JUMP_23:
		if (code == 0) PL_SetJumpSpeed(pl, 42, 0);
		break;
	case PS_JUMP_34:
		pl->vel[1] = 31.5F;
		pl->speed = 8;
		break;
	case PS_JUMP_1A:
		PL_SetJumpSpeed(pl, 42, 0.25F);
		break;
	case PS_JUMP_00:
	case PS_JUMP_20:
		pl->obj->s.skel.index = -1;
		PL_SetJumpSpeed(pl, 42, 0.25F);
		pl->speed *= 0.8F;
		break;
	case PS_JUMP_06:
	case PS_JUMP_0D:
		PL_SetJumpSpeed(pl, 62, 0);
		if (pl->speed < 24) pl->speed = 24;
		pl->wall_timer = 0;
		break;
	case PS_JUMP_07:
		PL_SetJumpSpeed(pl, 62, 0);
		pl->speed = 8;
		pl->ang[1] = pl->stick_ang;
		break;
	case PS_JUMP_05:
		pl->obj->s.skel.index = -1;
		PL_SetJumpSpeed(pl, 42, 0.25F);
		pl->ang[0] = -0x2000;
		break;
	case PS_JUMP_37:
		pl->vel[1] = 84;
		if (code == 0) pl->speed = 0;
		break;
	case PS_JUMP_0A:
		if ((speed = pl->speed+15) > 48) speed = 48;
		PL_SetSpeed(pl, speed);
		break;
	case PS_JUMP_08:
		pl->obj->s.skel.index = -1;
		PL_SetJumpSpeed(pl, 30, 0);
		pl->obj->o_v7 = pl->speed > 16 ? 0 : 1;
		if ((pl->speed *= 1.5F) > 48) pl->speed = 48;
		break;
	case PS_JUMP_2A:
		pl->vel[1] = 12;
		if (pl->speed < 32) pl->speed = 32;
		break;
	case PS_JUMP_2C:
		pl->vel[1] = 20;
		break;
	}
	pl->peak = pl->pos[1];
	pl->flag |= PL_00000100;
	return state;
}

static u32 PL_SetWalk(PLAYER *pl, u32 state, UNUSED u32 code)
{
	SHORT slip = PL_GetSlip(pl);
	float speed = pl->speed;
	float stick_dist = pl->stick_dist <= 8 ? pl->stick_dist : 8;
	switch (state)
	{
	case PS_WALK_00:
		if (slip != SLIP_19)
		{
			if (0 <= speed && speed < stick_dist) pl->speed = stick_dist;
		}
		pl->obj->o_v7 = 0;
		break;
	case PS_WALK_02:
		if (0 <= speed && speed < stick_dist/2.0F) pl->speed = stick_dist/2.0F;
		break;
	case PS_WALK_10:
		if (PL_IsFaceDownSlope(pl, FALSE))  state = PS_WALK_12;
		else                                state = PS_WALK_13;
		break;
	case PS_WALK_11:
		if (PL_IsFaceDownSlope(pl, FALSE))  state = PS_WALK_14;
		else                                state = PS_WALK_15;
		break;
	}
	return state;
}

static u32 PL_SetSwim(PLAYER *pl, u32 state, UNUSED u32 code)
{
	if (state == PS_SWIM_38 || state == PS_SWIM_39) pl->vel[1] = 32;
	return state;
}

static u32 PL_SetDemo(PLAYER *pl, u32 state, UNUSED u32 code)
{
	switch (state)
	{
	case PS_DEMO_23:
		pl->vel[1] = 52;
		break;
	case PS_DEMO_04:
		PL_SetSpeed(pl, 0);
		break;
	case PS_DEMO_24:
		PL_SetSpeed(pl, 2);
		break;
	case PS_DEMO_2B:
	case PS_DEMO_2C:
		pl->vel[1] = 64;
		break;
	}
	return state;
}

int PL_SetState(PLAYER *pl, u32 state, u32 code)
{
	switch (state & PC_MASK)
	{
	case PC_WALK: state = PL_SetWalk(pl, state, code); break;
	case PC_JUMP: state = PL_SetJump(pl, state, code); break;
	case PC_SWIM: state = PL_SetSwim(pl, state, code); break;
	case PC_DEMO: state = PL_SetDemo(pl, state, code); break;
	}
	pl->flag &= ~(PL_SOUND|PL_VOICE);
	if (!(pl->state & PF_JUMP)) pl->flag &= ~PL_00040000;
	pl->prevstate = pl->state;
	pl->state = state;
	pl->code = code;
	pl->phase = 0;
	pl->timer = 0;
	return TRUE;
}

int PL_SetTripJump(PLAYER *pl)
{
	if (pl->sink >= 11)
	{
		if (!pl->take)  return PL_SetState(pl, PS_WALK_36, 0);
		else            return PL_SetState(pl, PS_WALK_37, 0);
	}
	if (PL_IsSlipJump(pl))
	{
		PL_SetSlipJump(pl);
	}
	else if (!pl->jump_timer || pl->press)
	{
		PL_SetState(pl, PS_JUMP_00, 0);
	}
	else switch (pl->prevstate)
	{
	case PS_WALK_30: PL_SetState(pl, PS_JUMP_01, 0); break;
	case PS_WALK_31: PL_SetState(pl, PS_JUMP_01, 0); break;
	case PS_WAIT_33: PL_SetState(pl, PS_JUMP_01, 0); break;
	case PS_WALK_32:
		if (pl->flag & PL_WINGCAP)  PL_SetState(pl, PS_JUMP_14, 0);
		else if (pl->speed > 20)    PL_SetState(pl, PS_JUMP_02, 0);
		else                        PL_SetState(pl, PS_JUMP_00, 0);
		break;
	default:
		PL_SetState(pl, PS_JUMP_00, 0);
		break;
	}
	pl->jump_timer = 0;
	return TRUE;
}

int PL_SetStateJump(PLAYER *pl, u32 state, u32 code)
{
	UNUSED u32 prevstate = pl->state;
	if (pl->sink >= 11)
	{
		if (!pl->take)  return PL_SetState(pl, PS_WALK_36, 0);
		else            return PL_SetState(pl, PS_WALK_37, 0);
	}
	if (PL_IsSlipJump(pl))  PL_SetSlipJump(pl);
	else                    PL_SetState(pl, state, code);
	return TRUE;
}

int PL_SetStateDrop(PLAYER *pl, u32 state, u32 code)
{
	PL_DropAll(pl);
	return PL_SetState(pl, state, code);
}

int PL_SetStateDamage(PLAYER *pl, u32 state, u32 code, SHORT damage)
{
	pl->damage = damage;
	return PL_SetState(pl, state, code);
}

int PL_CheckMotion(PLAYER *pl)
{
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_JUMP_00, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_0C, 0);
	if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_WALK_00, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_10, 0);
	return FALSE;
}

int PL_CheckMotionTake(PLAYER *pl)
{
	if (pl->status & PA_JUMPREQ) return PL_SetState(pl, PS_JUMP_20, 0);
	if (pl->status & PA_LANDREQ) return PL_SetState(pl, PS_JUMP_21, 0);
	if (pl->status & PA_WALKREQ) return PL_SetState(pl, PS_WALK_02, 0);
	if (pl->status & PA_SLIPREQ) return PL_SetState(pl, PS_WALK_11, 0);
	return FALSE;
}

int PL_EnterField(PLAYER *pl)
{
	camera_80286188(pl->scene->cam, pl->scene->cam->_01, 1); /* T:enum */
	SVecSet(pl->rot, 0, 0, 0);
	if (!pl->take)  return PL_SetState(pl, PS_WALK_00, 0);
	else            return PL_SetState(pl, PS_WALK_02, 0);
}

int PL_EnterWater(PLAYER *pl)
{
	pl->speed /= 4.0F;
	pl->vel[1] /= 2.0F;
	pl->pos[1] = pl->water - 100;
	pl->ang[2] = 0;
	SVecSet(pl->rot, 0, 0, 0);
	if (!(pl->state & PF_DIVE)) pl->ang[0] = 0;
	/* T:enum */
	if (pl->scene->cam->mode != 8) camera_80286188(pl->scene->cam, 8, 1);
	return PL_SetState(pl, PS_SWIM_22, 0);
}

static void PL_ShowPress(PLAYER *pl)
{
	static u8 unpresstab[] =
		{70, 50, 50, 60, 70, 80, 80, 60, 40, 20, 20, 30, 50, 60, 60, 40};
	if (pl->press != 0xFF)
	{
		if (pl->press == 0)
		{
			FVecSet(pl->obj->s.scale, 1, 1, 1);
		}
		else if (pl->press <= 16)
		{
			pl->press -= 1;
			pl->obj->s.scale[1] = 1 - 0.6F*unpresstab[15-pl->press]/100;
			pl->obj->s.scale[0] = 1 + 0.4F*unpresstab[15-pl->press]/100;
			pl->obj->s.scale[2] = pl->obj->s.scale[0];
		}
		else
		{
			pl->press -= 1;
			FVecSet(pl->obj->s.scale, 1.4F, 0.4F, 1.4F);
		}
	}
}

static void PL_CheckDebug(PLAYER *pl)
{
	if (debug_info)
	{
		float x = DIST2(pl->ground->nx, pl->ground->nz);
		float y = pl->ground->ny;
		dprintf(210, 56+16*2, "ANG %d", (float)ATAN2(y, x) * 180/32768);
		dprintf(210, 56+16*1, "SPD %d", pl->speed);
		dprintf(210, 56+16*0, "STA %x", pl->state & 0x1FF);
	}
}

static void PL_CheckButton(PLAYER *pl)
{
	if (pl->cont->down & A_BUTTON) pl->status |= PA_JUMPREQ;
	if (pl->cont->held & A_BUTTON) pl->status |= PA_JUMPSTA;
	if (!pl->press)
	{
		if (pl->cont->down & B_BUTTON)  pl->status |= PA_ATCKREQ;
		if (pl->cont->held & Z_TRIG)    pl->status |= PA_TRIGSTA;
		if (pl->cont->down & Z_TRIG)    pl->status |= PA_TRIGREQ;
	}
	if      (pl->status & PA_JUMPREQ)   pl->a_timer = 0;
	else if (pl->a_timer < 0xFF)        pl->a_timer++;
	if      (pl->status & PA_ATCKREQ)   pl->b_timer = 0;
	else if (pl->b_timer < 0xFF)        pl->b_timer++;
}

static void PL_CheckStick(PLAYER *pl)
{
	CONTROLLER *cont = pl->cont;
	float dist = 64 * SQUARE(cont->dist/64.0F);
	if (!pl->press) pl->stick_dist = dist/2.0F;
	else            pl->stick_dist = dist/8.0F;
	if (pl->stick_dist > 0)
	{
		pl->stick_ang = ATAN2(-cont->y, cont->x) + pl->scene->cam->_02;
		pl->status |= PA_WALKREQ;
	}
	else
	{
		pl->stick_ang = pl->ang[1];
	}
}

static void PL_CheckBG(PLAYER *pl)
{
	float gas;
	BGHitWall(&pl->pos[0], &pl->pos[1], &pl->pos[2], 60, 50);
	BGHitWall(&pl->pos[0], &pl->pos[1], &pl->pos[2], 30, 24);
	pl->ground_y = BGCheckGround(
		pl->pos[0], pl->pos[1], pl->pos[2], &pl->ground
	);
	if (!pl->ground)
	{
		FVecCpy(pl->pos, pl->obj->s.pos);
		pl->ground_y = BGCheckGround(
			pl->pos[0], pl->pos[1], pl->pos[2], &pl->ground
		);
	}
	pl->roof_y = PL_CheckRoof(pl->pos, pl->ground_y, &pl->roof);
	gas = BGCheckGas(pl->pos[0], pl->pos[2]);
	pl->water = BGCheckWater(pl->pos[0], pl->pos[2]);
	if (pl->ground)
	{
		pl->ground_ang = ATAN2(pl->ground->nz, pl->ground->nx);
		pl->surface = PL_GetSurface(pl);
		if (pl->pos[1] > pl->water-40 && PL_IsSlipMin(pl))
		{
			pl->status |= PA_SLIPREQ;
		}
		if (
			pl->ground->flag & BG_MOVE ||
			(pl->roof && pl->roof->flag & BG_MOVE)
		)
		{
			float dist = pl->roof_y - pl->ground_y;
			if (0 <= dist && dist <= 150) pl->status |= PA_PRESREQ;
		}
		if (pl->pos[1] > pl->ground_y+100) pl->status |= PA_LANDREQ;
		if (pl->pos[1] < pl->water-10) pl->status |= PA_WADING;
		if (pl->pos[1] < gas-100) pl->status |= PA_GAS;
	}
	else
	{
		PL_Fade(pl, FADE_DIE);
	}
}

static void PL_CheckStatus(PLAYER *pl)
{
	pl->effect = 0;
	pl->status = 0;
	pl->hit_status = pl->obj->hit_status;
	pl->flag &= 0xFFFFFF;
	PL_CheckButton(pl);
	PL_CheckStick(pl);
	PL_CheckBG(pl);
	PL_CheckDebug(pl);
	if (camera_8033C848 & 0x2000)
	{
		if (pl->state & PF_VIEW) pl->status |= PA_VIEWREQ;
		else camera_8033C848 &= ~0x2000;
	}
	if (!(pl->status & (PA_WALKREQ|PA_JUMPREQ))) pl->status |= PA_WAITREQ;
	if (pl->obj->o_hit_result & (HR_000001|HR_000002|HR_000010))
	{
		pl->status |= PA_HIT;
	}
	PL_CheckTrampoline(pl);
	if (pl->wall_timer > 0) pl->wall_timer--;
	if (pl->jump_timer > 0) pl->jump_timer--;
}

static void PL_ProcSwimCamera(PLAYER *pl)
{
	if ((pl->state & PC_MASK) == PC_SWIM)
	{
		float depth = pl->water-80 - pl->pos[1];
		SHORT mode = pl->scene->cam->mode;
		if (pl->state & PF_SINK)
		{
			if (mode != 4) camera_80286188(pl->scene->cam, 4, 1); /* T:enum */
		}
		else
		{
			/* T:enum */
			if (depth > 800 && mode != 3) camera_80286188(pl->scene->cam, 3, 1);
			if (depth < 400 && mode != 8) camera_80286188(pl->scene->cam, 8, 1);
			if (!(pl->state & PF_DEMO))
			{
				if (pl->pos[1] < pl->water-160 || pl->ang[0] < -0x800)
				{
					pl->effect |= PE_00000020;
				}
			}
		}
	}
}

static void PL_ProcPower(PLAYER *pl)
{
	if (pl->power >= 0x100)
	{
		if (!((unsigned int)pl->recover | (unsigned int)pl->damage))
		{
			if (pl->status & PA_GAS && !(pl->state & PF_DEMO))
			{
				if (!(pl->flag & PL_METALCAP) && !debug_stage) pl->power -= 4;
			}
			else if (pl->state & PF_SWIM && !(pl->state & PF_DEMO))
			{
				int issnow = (pl->scene->env & ENV_MASK) == ENV_SNOW;
				if (pl->pos[1] >= pl->water-140 && !issnow)
				{
					pl->power += 26;
				}
				else
				{
					if (!debug_stage) pl->power -= issnow ? 3 : 1;
				}
			}
		}
		if (pl->recover > 0)
		{
			pl->power += 0x40;
			pl->recover--;
		}
		if (pl->damage > 0)
		{
			pl->power -= 0x40;
			pl->damage--;
		}
		if (pl->power > 0x880) pl->power = 0x880;
		if (pl->power < 0x100) pl->power = 0x0FF;
		if ((pl->state & PC_MASK) == PC_SWIM && pl->power < 0x300)
		{
			Na_FixSePlay(NA_SE1_18);
#ifdef MOTOR
			if (motor_8030CE0C == 0)
			{
				motor_8030CE0C = 36;
				if (motor_8024C8AC()) motor_8024C834(3, 30);
			}
		}
		else
		{
			motor_8030CE0C = 0;
#endif
		}
	}
}

static void PL_SyncInfo(PLAYER *pl)
{
	pl->ctrl->state = pl->state;
	pl->camera->state = pl->state;
	SVecCpy(pl->camera->ang, pl->ang);
	if (!(pl->flag & PL_02000000)) FVecCpy(pl->camera->pos, pl->pos);
}

static void PL_ClearCtrl(PLAYER *pl)
{
	PL_CTRL *ctrl = pl->ctrl;
	ctrl->head = 1;
	ctrl->eyes = 0;
	ctrl->hand = 0;
	ctrl->cap = 0;
	ctrl->wing = 0;
	pl->flag &= ~PL_00000040;
}

static void PL_ShowSink(PLAYER *pl)
{
	OBJECT *obj = pl->obj;
	if (obj->s.m) (*obj->s.m)[3][1] -= pl->sink;
	obj->s.pos[1] -= pl->sink;
}

static u32 PL_ProcCap(PLAYER *pl)
{
	static u64 flash_pattern = 0x4444449249255555ULL;
	u32 flag = pl->flag;
	if (pl->cap_timer > 0)
	{
		u32 state = pl->state;
		if (pl->cap_timer <= 60 || !(
			state == PS_DEMO_05 ||
			state == PS_DEMO_06 ||
			state == PS_DEMO_08 ||
			state == PS_SPEC_31
		)) pl->cap_timer -= 1;
		if (pl->cap_timer == 0)
		{
			AudStopSpecialBGM();
			pl->flag &= ~PL_SPECIALCAP;
			if (!(pl->flag & PL_ANYCAP)) pl->flag &= ~PL_HEADCAP;
		}
		if (pl->cap_timer == 60) AudFadeoutSpecialBGM();
		if (pl->cap_timer < 64 && 1ULL << pl->cap_timer & flash_pattern)
		{
			flag &= ~PL_SPECIALCAP;
			if (!(flag & PL_ANYCAP)) flag &= ~PL_HEADCAP;
		}
	}
	return flag;
}

static void PL_SyncCtrl(PLAYER *pl)
{
	PL_CTRL *ctrl = pl->ctrl;
	u32 flag = PL_ProcCap(pl);
	if (flag & PL_VANISHCAP) ctrl->cap = 0x100 | 0x80;
	if (flag & PL_METALCAP) ctrl->cap |= 0x200;
	if (flag & PL_00000040) ctrl->cap |= 0x200;
	if (pl->invincible > 2 && gfx_frame & 1)
	{
		mario->obj->s.s.flag |= SHP_OBJHIDE;
	}
	if (flag & PL_HANDCAP)
	{
		if (flag & PL_WINGCAP)  ctrl->hand = 4;
		else                    ctrl->hand = 3;
	}
	if (flag & PL_HEADCAP)
	{
		if (flag & PL_WINGCAP)  ctrl->head = 2;
		else                    ctrl->head = 0;
	}
	if (pl->state & PF_SHRT)    pl->obj->hit_h = 100;
	else                        pl->obj->hit_h = 160;
	if (pl->flag & PL_00000080 && pl->alpha != 0xFF)
	{
		ctrl->cap &= ~0xFF;
		ctrl->cap |= 0x100 | pl->alpha;
	}
}

UNUSED
static void DebugCap(USHORT button, u32 flag, USHORT timer, USHORT bgm)
{
	if (cont1->held & Z_TRIG && cont1->down & button && !(mario->flag & flag))
	{
		mario->flag |= PL_HEADCAP + flag;
		if (timer > mario->cap_timer) mario->cap_timer = timer;
		AudPlaySpecialBGM(bgm);
	}
}

#ifdef MOTOR
extern OBJLANG obj_13003174[];

static void PL_ProcMotor(void)
{
	if      (mario->effect & PE_00000010)   motor_8024C834(5, 80);
	else if (mario->effect & PE_00000002)   motor_8024C834(5, 80);
	else if (mario->effect & PE_00040000)   motor_8024C834(5, 80);
	if (mario->take && mario->take->script == SegmentToVirtual(obj_13003174))
	{
		motor_8024C924();
	}
}
#endif

u32 MarioExec(UNUSED OBJECT *obj)
{
	int result = TRUE;
	if (mario->state)
	{
		mario->obj->s.s.flag &= ~SHP_OBJHIDE;
		PL_ClearCtrl(mario);
		PL_CheckStatus(mario);
		PL_CheckGroundCollision(mario);
		PL_CheckCollision(mario);
		if (!mario->ground) return 0;
		while (result)
		{
			switch (mario->state & PC_MASK)
			{
			case PC_WAIT: result = PL_ExecWait(mario); break;
			case PC_WALK: result = PL_ExecWalk(mario); break;
			case PC_JUMP: result = PL_ExecJump(mario); break;
			case PC_SWIM: result = PL_ExecSwim(mario); break;
			case PC_DEMO: result = PL_ExecDemo(mario); break;
			case PC_SPEC: result = PL_ExecSpec(mario); break;
			case PC_ATCK: result = PL_ExecAtck(mario); break;
			}
		}
		PL_ShowSink(mario);
		PL_ShowPress(mario);
		PL_ProcSwimCamera(mario);
		PL_ProcPower(mario);
		PL_SyncInfo(mario);
		PL_SyncCtrl(mario);
		if (mario->ground->code == BG_44)
		{
			enemya_802AE4C0(0, mario->ground->attr << 8);
#if REVISION >= 199609
			Na_ObjSePlay(NA_SE4_10, mario->obj);
#endif
		}
		if (mario->ground->code == BG_56)
		{
			enemya_802AE4C0(1, 0);
#if REVISION >= 199609
			Na_ObjSePlay(NA_SE4_10, mario->obj);
#endif
		}
		AudProcEndlessMusic();
		mario->obj->o_hit_result = 0;
#ifdef MOTOR
		PL_ProcMotor();
#endif
		return mario->effect;
	}
	return 0;
}

extern OBJLANG obj_13003DF8[];

void MarioEnter(void)
{
	UNUSED static int player_8033B280;
	SVEC pos;
	player_8033B280 = 0;
	mario->timer = 0;
	mario->a_timer = 0xFF;
	mario->b_timer = 0xFF;
	mario->invincible = 0;
	if (BuGetFlag() & (BU_LOSTCAP|BU_CONDORCAP|BU_MONKEYCAP|BU_SNOWMANCAP))
	{
		mario->flag = 0;
	}
	else
	{
		mario->flag = PL_DEFCAP|PL_HEADCAP;
	}
	mario->speed = 0;
	mario->press = 0;
	mario->damage = 0;
	mario->recover = 0;
	mario->cap_timer = 0;
	mario->sink = 0;
	mario->take = NULL;
	mario->ride = NULL;
	mario->attach = NULL;
	mario->water = BGCheckWater(mario_actor->pos[0], mario_actor->pos[2]);
	mario->scene = scenep;
	mario->obj = mario_obj;
	mario->obj->s.skel.index = -1;
	SVecCpy(mario->ang, mario_actor->ang);
	SVecSet(mario->rot, 0, 0, 0);
	SVecToFVec(mario->pos, mario_actor->pos);
	FVecSet(mario->vel, 0, 0, 0);
	mario->ground_y = BGCheckGround(
		mario->pos[0], mario->pos[1], mario->pos[2], &mario->ground
	);
	if (mario->pos[1] < mario->ground_y) mario->pos[1] = mario->ground_y;
	mario->obj->s.pos[1] = mario->pos[1];
	mario->state = mario->pos[1] <= mario->water-100 ? PS_SWIM_00 : PS_WAIT_01;
	PL_ClearCtrl(mario);
	PL_SyncInfo(mario);
	mario->ctrl->punch = 0;
	mario->obj->o_posx = mario->pos[0];
	mario->obj->o_posy = mario->pos[1];
	mario->obj->o_posz = mario->pos[2];
	mario->obj->o_angx = mario->ang[0];
	mario->obj->o_angy = mario->ang[1];
	mario->obj->o_angz = mario->ang[2];
	FVecCpy(mario->obj->s.pos, mario->pos);
	SVecSet(mario->obj->s.ang, 0, mario->ang[1], 0);
	if (BuGetCap(pos))
	{
		OBJECT *obj = ObjMakeHere(mario->obj, S_CAP_S, obj_13003DF8);
		obj->o_posx = pos[0];
		obj->o_posy = pos[1];
		obj->o_posz = pos[2];
		obj->work[O_VELF].i = 0;
		obj->o_angy = 0;
	}
}

void MarioInit(void)
{
	mario->index = 0;
	mario->flag = 0;
	mario->state = PS_NULL;
	mario->actor = &player_actor[0];
	mario->camera = &pl_camera_data[0];
	mario->ctrl = &pl_ctrl_data[0];
	mario->cont = &controller_data[0];
	mario->anime = &mario_anime_bank;
	mario->coin = 0;
	mario->star = BuStarTotal();
	mario->key = 0;
	mario->life = 4;
	mario->power = 0x880;
	mario->prevstar = mario->star;
	mario->waist = 189;
	hud.coin = 0;
	hud.power = 8;
}
