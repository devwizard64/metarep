#ifndef __SM64_DEFOBJECT_H__
#define __SM64_DEFOBJECT_H__

#define OBJECT_01           0x01
#define OBJECT_FREEZE       0x02
#define OBJECT_04           0x04
#define OBJECT_FREEZEPLAYER 0x08
#define OBJECT_FREEZEALL    0x10
#define OBJECT_20           0x20
#define OBJECT_FROZEN       0x40

#define OBJ_0001            0x0001
#define OBJ_0002            0x0002
#define OBJ_0008            0x0008
#define OBJ_0010            0x0010
#define OBJ_0020            0x0020
#define OBJ_0040            0x0040
#define OBJ_DITHER          0x0080
#define OBJ_0100            0x0100
#define OBJ_0200            0x0200
#define OBJ_0400            0x0400

#define OT_PLAYER           0
#define OT_ATTACK           2
#define OT_ENEMYA           4
#define OT_ENEMYB           5
#define OT_ITEM             6
#define OT_DEFAULT          8
#define OT_MOVEBG           9
#define OT_ATTACH           10
#define OT_SYSTEM           11
#define OT_EFFECT           12
#define OT_MAX              13

#define ACTORTYPE_NULL      0
#define ACTORTYPE_32        1
#define ACTORTYPE_16        2

#define ACTOR_MARIO         1

#define HIT_HANG            0x00000001
#define HIT_TAKE            0x00000002
#define HIT_DOOR            0x00000004
#define HIT_DAMAGE          0x00000008
#define HIT_COIN            0x00000010
#define HIT_CAP             0x00000020
#define HIT_POLE            0x00000040
#define HIT_KOOPA           0x00000080
#define HIT_SPINY           0x00000100
#define HIT_ITEMBOX         0x00000200
#define HIT_WIND            0x00000400
#define HIT_PORTDOOR        0x00000800
#define HIT_STAR            0x00001000
#define HIT_PIPE            0x00002000
#define HIT_CANNON          0x00004000
#define HIT_BOUNCE          0x00008000
#define HIT_RECOVER         0x00010000
#define HIT_BUMP            0x00020000
#define HIT_BURN            0x00040000
#define HIT_SHELL           0x00080000
#define HIT_DUMMY           0x00100000  /* unused */
#define HIT_ENEMY           0x00200000
#define HIT_FLYENEMY        0x00400000
#define HIT_MESSAGE         0x00800000
#define HIT_TORNADO         0x01000000
#define HIT_WHIRLPOOL       0x02000000
#define HIT_CLAM            0x04000000
#define HIT_CAGE            0x08000000
#define HIT_BULLET          0x10000000
#define HIT_ELECSHOCK       0x20000000
#define HIT_IGLOO           0x40000000

#define HR_000001           0x000001
#define HR_000002           0x000002
#define HR_000004           0x000004
#define HR_000008           0x000008
#define HR_000010           0x000010
#define HR_000040           0x000040
#define HR_000080           0x000080
#define HR_000800           0x000800
#define HR_002000           0x002000
#define HR_004000           0x004000
#define HR_008000           0x008000
#define HR_010000           0x010000
#define HR_020000           0x020000
#define HR_040000           0x040000
#define HR_080000           0x080000
#define HR_100000           0x100000
#define HR_200000           0x200000
#define HR_400000           0x400000
#define HR_800000           0x800000

#define HF_0001             0x0001
#define HF_0002             0x0002
#define HF_0004             0x0004
#define HF_0008             0x0008
#define HF_0010             0x0010
#define HF_0020             0x0020
#define HF_0040             0x0040
#define HF_0080             0x0080
#define HF_0100             0x0100
#define HF_0200             0x0200
#define HF_0400             0x0400
#define HF_0800             0x0800
#define HF_1000             0x1000
#define HF_2000             0x2000
#define HF_4000             0x4000

#define OF_SETSHAPECOORD    0x0001
#define OF_MOVEF            0x0002
#define OF_MOVEY            0x0004
#define OF_SETSHAPEANGY     0x0008
#define OF_SETSHAPEANG      0x0010
#define OF_CALCMTX          0x0020
#define OF_CALCPLDIST       0x0040
#define OF_0080             0x0080
#define OF_0100             0x0100
#define OF_CALCREL          0x0200
#define OF_0400             0x0400
#define OF_SETMTX           0x0800
#define OF_CALCPLANG        0x2000
#define OF_4000             0x4000
#define OF_HITINFO          0x40000000

#define OM_BOUND            0x0001
#define OM_TOUCH            0x0002
#define OM_TAKEOFF          0x0004
#define OM_DIVE             0x0008
#define OM_S_WATER          0x0010
#define OM_U_WATER          0x0020
#define OM_B_WATER          0x0040
#define OM_SKY              0x0080
#define OM_OUT_SCOPE        0x0100
#define OM_0200             0x0200
#define OM_0400             0x0400
#define OM_0800             0x0800
#define OM_1000             0x1000
#define OM_2000             0x2000
#define OM_4000             0x4000

#define OA_0                0
#define OA_1                1
#define OA_2                2
#define OA_3                3

#define O_VAR               0
#define O_FLAG              1
#define O_MSG               2
#define O_HIT_TIMER         5
#define O_POS               6
#define O_POSX              6
#define O_POSY              7
#define O_POSZ              8
#define O_VEL               9
#define O_VELX              9
#define O_VELY              10
#define O_VELZ              11
#define O_VELF              12
#define O_VELL              13
#define O_VELU              14
#define O_ANG               15
#define O_ANGX              15
#define O_ANGY              16
#define O_ANGZ              17
#define O_SHAPEANG          18
#define O_SHAPEANGX         18
#define O_SHAPEANGY         19
#define O_SHAPEANGZ         20
#define O_SHAPEOFF          21
#define O_EFFECT            22
#define O_GRAVITY           23
#define O_GROUND_Y          24
#define O_MOVE              25
#define O_SHAPE             26
#define O_V0                27
#define O_V1                28
#define O_V2                29
#define O_V3                30
#define O_V4                31
#define O_V5                32
#define O_V6                33
#define O_V7                34
#define O_ROT               35
#define O_ROTX              35
#define O_ROTY              36
#define O_ROTZ              37
#define O_ANIMEP            38
#define O_ACTION            39
#define O_WALL_R            40
#define O_DRAG              41
#define O_HIT_TYPE          42
#define O_HIT_RESULT        43
#define O_REL               44
#define O_RELX              44
#define O_RELY              45
#define O_RELZ              46
#define O_CODE              47
#define O_MODE              49
#define O_PHASE             50
#define O_TIMER             51
#define O_DENSITY           52
#define O_TARGETDIST        53
#define O_TARGETANG         54
#define O_SAVE              55
#define O_SAVEX             55
#define O_SAVEY             56
#define O_SAVEZ             57
#define O_FRICTION          58
#define O_BOUNCE            59
#define O_ANIME             60
#define O_ALPHA             61
#define O_AP                62
#define O_HP                63
#define O_ACTORINFO         64
#define O_PREVMODE          65
#define O_HIT_FLAG          66
#define O_CHECKDIST         67
#define O_NCOIN             68
#define O_SHAPEDIST         69
#define O_AREA              70
#define O_TAGINFO           72
#define O_V8                73
#define O_V9                74
#define O_BG_ANG            75
#define O_BGINFO            76
#define O_SAVEANG           77
#define O_GROUND            78
#define O_SOUND             79

#define /* 0x088 */ o_var               work[O_VAR].i
#define /* 0x08C */ o_flag              work[O_FLAG].i
#define /* 0x090 */ o_msg_status        work[O_MSG].s[0]
#define /* 0x092 */ o_msg_phase         work[O_MSG].s[1]
#define /* 0x09C */ o_hit_timer         work[O_HIT_TIMER].i
#define /* 0x0A0 */ o_posx              work[O_POSX].f
#define /* 0x0A4 */ o_posy              work[O_POSY].f
#define /* 0x0A8 */ o_posz              work[O_POSZ].f
#define /* 0x0AC */ o_velx              work[O_VELX].f
#define /* 0x0B0 */ o_vely              work[O_VELY].f
#define /* 0x0B4 */ o_velz              work[O_VELZ].f
#define /* 0x0B8 */ o_velf              work[O_VELF].f
#define /* 0x0BC */ o_vell              work[O_VELL].f
#define /* 0x0C0 */ o_velu              work[O_VELU].f
#define /* 0x0C4 */ o_angx              work[O_ANGX].i
#define /* 0x0C8 */ o_angy              work[O_ANGY].i
#define /* 0x0CC */ o_angz              work[O_ANGZ].i
#define /* 0x0D0 */ o_shapeangx         work[O_SHAPEANGX].i
#define /* 0x0D4 */ o_shapeangy         work[O_SHAPEANGY].i
#define /* 0x0D8 */ o_shapeangz         work[O_SHAPEANGZ].i
#define /* 0x0DC */ o_shapeoff          work[O_SHAPEOFF].f
#define /* 0x0E0 */ o_effect            work[O_EFFECT].i
#define /* 0x0E4 */ o_gravity           work[O_GRAVITY].f
#define /* 0x0E8 */ o_ground_y          work[O_GROUND_Y].f
#define /* 0x0EC */ o_move              work[O_MOVE].i
#define /* 0x0F0 */ o_shape             work[O_SHAPE].i
#define /* 0x0F4 */ o_v0                work[O_V0].i
#define /* 0x0F4 */ o_f0                work[O_V0].f
#define /* 0x0F4 */ o_p0                work[O_V0].p
#define /* 0x0F8 */ o_v1                work[O_V1].i
#define /* 0x0F8 */ o_f1                work[O_V1].f
#define /* 0x0F8 */ o_p1                work[O_V1].p
#define /* 0x0FC */ o_v2                work[O_V2].i
#define /* 0x0FC */ o_f2                work[O_V2].f
#define /* 0x0FC */ o_p2                work[O_V2].p
#define /* 0x100 */ o_v3                work[O_V3].i
#define /* 0x100 */ o_f3                work[O_V3].f
#define /* 0x100 */ o_p3                work[O_V3].p
#define /* 0x104 */ o_v4                work[O_V4].i
#define /* 0x104 */ o_f4                work[O_V4].f
#define /* 0x104 */ o_p4                work[O_V4].p
#define /* 0x108 */ o_v5                work[O_V5].i
#define /* 0x108 */ o_f5                work[O_V5].f
#define /* 0x108 */ o_p5                work[O_V5].p
#define /* 0x10C */ o_v6                work[O_V6].i
#define /* 0x10C */ o_f6                work[O_V6].f
#define /* 0x10C */ o_p6                work[O_V6].p
#define /* 0x110 */ o_v7                work[O_V7].i
#define /* 0x110 */ o_f7                work[O_V7].f
#define /* 0x110 */ o_p7                work[O_V7].p
#define /* 0x114 */ o_rotx              work[O_ROTX].i
#define /* 0x118 */ o_roty              work[O_ROTY].i
#define /* 0x11C */ o_rotz              work[O_ROTZ].i
#define /* 0x120 */ o_animep            work[O_ANIMEP].p
#define /* 0x124 */ o_action            work[O_ACTION].i
#define /* 0x128 */ o_wall_r            work[O_WALL_R].f
#define /* 0x12C */ o_drag              work[O_DRAG].f
#define /* 0x130 */ o_hit_type          work[O_HIT_TYPE].i
#define /* 0x134 */ o_hit_result        work[O_HIT_RESULT].i
#define /* 0x138 */ o_relx              work[O_RELX].f
#define /* 0x13C */ o_rely              work[O_RELY].f
#define /* 0x140 */ o_relz              work[O_RELZ].f
#define /* 0x144 */ o_code              work[O_CODE].i
#define /* 0x14C */ o_mode              work[O_MODE].i
#define /* 0x150 */ o_phase             work[O_PHASE].i
#define /* 0x154 */ o_timer             work[O_TIMER].i
#define /* 0x158 */ o_density           work[O_DENSITY].f
#define /* 0x15C */ o_targetdist        work[O_TARGETDIST].f
#define /* 0x160 */ o_targetang         work[O_TARGETANG].i
#define /* 0x164 */ o_savex             work[O_SAVEX].f
#define /* 0x168 */ o_savey             work[O_SAVEY].f
#define /* 0x16C */ o_savez             work[O_SAVEZ].f
#define /* 0x170 */ o_friction          work[O_FRICTION].f
#define /* 0x174 */ o_bounce            work[O_BOUNCE].f
#define /* 0x178 */ o_anime             work[O_ANIME].i
#define /* 0x17C */ o_alpha             work[O_ALPHA].i
#define /* 0x180 */ o_ap                work[O_AP].i
#define /* 0x184 */ o_hp                work[O_HP].i
#define /* 0x188 */ o_actorinfo         work[O_ACTORINFO].i
#define /* 0x18C */ o_prevmode          work[O_PREVMODE].i
#define /* 0x190 */ o_hit_flag          work[O_HIT_FLAG].i
#define /* 0x194 */ o_checkdist         work[O_CHECKDIST].f
#define /* 0x198 */ o_ncoin             work[O_NCOIN].i
#define /* 0x19C */ o_shapedist         work[O_SHAPEDIST].f
#define /* 0x1A0 */ o_area              work[O_AREA].i
#define /* 0x1A8 */ o_taginfo           work[O_TAGINFO].i
#define /* 0x1AC */ o_v8                work[O_V8].i
#define /* 0x1AC */ o_f8                work[O_V8].f
#define /* 0x1AC */ o_p8                work[O_V8].p
#define /* 0x1B0 */ o_v9                work[O_V9].i
#define /* 0x1B0 */ o_f9                work[O_V9].f
#define /* 0x1B0 */ o_p9                work[O_V9].p
#define /* 0x1B4 */ o_bg_ang            work[O_BG_ANG].i
#define /* 0x1B8 */ o_bgcode            work[O_BGINFO].s[0]
#define /* 0x1BA */ o_bgarea            work[O_BGINFO].s[1]
#define /* 0x1BC */ o_saveang           work[O_SAVEANG].i
#define /* 0x1C0 */ o_ground            work[O_GROUND].p
#define /* 0x1C4 */ o_sound             work[O_SOUND].i

#endif /* __SM64_DEFOBJECT_H__ */
