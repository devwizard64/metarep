def fmt_mask(x):
	fd, fx, x = ("~%d", "~0x%02X", ~x) if x < 0 else ("%d", "0x%02X", x)
	return fd % x if x < 10 else fx % x

def fmt_time(x):
	x, y = x//30, x%30
	if x == 0: return    "%d" % y
	if y == 0: return "30*%d" % x
	return "30*%d+%d" % (x, y)

def fmt_coursename(self, x):
	return "%d" % (1+x)

def fmt_levelname(self, x):
	if x < 6*15: return "%d.%d" % (1+x//6, 1+x%6)
	return "%d" % x

fmt_exit = {
	-1: "EXIT_ENDING",
	-2: "EXIT_FACE",
	-3: "EXIT_GAMEOVER",
	-8: "EXIT_LOGO",
	-9: "EXIT_DEBUG",
}

fmt_stage = [
	"STAGE_NULL",
	"1",
	"2",
	"3",
	"STAGE_BBH",
	"STAGE_CCM",
	"STAGE_INSIDE",
	"STAGE_HMC",
	"STAGE_SSL",
	"STAGE_BOB",
	"STAGE_SL",
	"STAGE_WDW",
	"STAGE_JRB",
	"STAGE_THI",
	"STAGE_TTC",
	"STAGE_RR",
	"STAGE_GROUNDS",
	"STAGE_BITDW",
	"STAGE_VCUTM",
	"STAGE_BITFS",
	"STAGE_SA",
	"STAGE_BITS",
	"STAGE_LLL",
	"STAGE_DDD",
	"STAGE_WF",
	"STAGE_ENDING",
	"STAGE_COURTYARD",
	"STAGE_PSS",
	"STAGE_COTMC",
	"STAGE_TOTWC",
	"STAGE_BITDWA",
	"STAGE_WMOTR",
	"32",
	"STAGE_BITFSA",
	"STAGE_BITSA",
	"35",
	"STAGE_TTM",
	"37",
	"38",
]

fmt_port_x = {
	240: "WIN",
	241: "DIE",
	242: "ROOF",
	243: "FALL",
	248: "FINAL",
	249: "STAFF",
	250: "STAFFEND",
}

def fmt_port(self, x):
	if x in fmt_port_x: return "PORT_" + fmt_port_x[x]
	return "%d" % x

fmt_mem_alloc = [
	"MEM_ALLOC_L",
	"MEM_ALLOC_R",
]

flag_save = [
	(0x000001, 0x000001, "SAVE_ACTIVE"),
	(0x000002, 0x000002, "SAVE_REDSW"),
	(0x000004, 0x000004, "SAVE_GREENSW"),
	(0x000008, 0x000008, "SAVE_BLUESW"),
	(0x000010, 0x000010, "SAVE_KEY1"),
	(0x000020, 0x000020, "SAVE_KEY2"),
	(0x000040, 0x000040, "SAVE_KEYDOOR1"),
	(0x000080, 0x000080, "SAVE_KEYDOOR2"),
	(0x000100, 0x000100, "SAVE_WATERPORT"),
	(0x000200, 0x000200, "SAVE_DRAIN"),
	(0x000400, 0x000400, "SAVE_STARDOOR1T"),
	(0x000800, 0x000800, "SAVE_STARDOOR1B"),
	(0x001000, 0x001000, "SAVE_STARDOOR3L"),
	(0x002000, 0x002000, "SAVE_STARDOOR3R"),
	(0x004000, 0x004000, "SAVE_STARDOOR8"),
	(0x008000, 0x008000, "SAVE_STARDOOR30"),
	(0x100000, 0x100000, "SAVE_STARDOOR50"),
	(0x010000, 0x010000, "SAVE_GROUNDCAP"),
	(0x020000, 0x020000, "SAVE_CONDORCAP"),
	(0x040000, 0x040000, "SAVE_MONKEYCAP"),
	(0x080000, 0x080000, "SAVE_SNOWMANCAP"),
]
fmt_save_flag = lambda self, x: self.fmt_flag(flag_save, x)

flag_anime = [
	(0x0001, 0x0000, "ANIME_LOOP"),
	(0x0001, 0x0001, "ANIME_NOLOOP"),
	(0x0002, 0x0002, "ANIME_REVERSE"),
	(0x0004, 0x0004, "ANIME_NOSTEP"),
	(0x0058, 0x0000, "ANIME_XYZ"),
	(0x0008, 0x0008, "ANIME_Y"),
	(0x0010, 0x0010, "ANIME_XZ"),
	(0x0020, 0x0020, "ANIME_FIXSHADOW"),
	(0x0040, 0x0040, "ANIME_NOPOS"),
]
fmt_anime_flag = lambda self, x: self.fmt_flag(flag_anime, x)

fmt_layer_x = [
	"BACK",
	"OPA_SURF",
	"OPA_DECAL",
	"OPA_INTER",
	"TEX_EDGE",
	"XLU_SURF",
	"XLU_DECAL",
	"XLU_INTER",
]

def fmt_layer(self, x):
	return "LAYER_" + fmt_layer_x[x]

fmt_ot = [
	"OT_PLAYER",
	"1",
	"OT_ATTACK",
	"3",
	"OT_ENEMYA",
	"OT_ENEMYB",
	"OT_ITEM",
	"7",
	"OT_DEFAULT",
	"OT_MOVEBG",
	"OT_ATTACH",
	"OT_SYSTEM",
	"OT_EFFECT",
]

flag_actor = [
	(1, 1, "ACTOR_MARIO"),
]
fmt_actor_flag = lambda self, x: self.fmt_flag(flag_actor, x)

flag_oflag = [
	(0x0001, 0x0001, "OF_0001"),
	(0x0002, 0x0002, "OF_0002"),
	(0x0004, 0x0004, "OF_0004"),
	(0x0008, 0x0008, "OF_0008"),
	(0x0010, 0x0010, "OF_0010"),
	(0x0020, 0x0020, "OF_0020"),
	(0x0040, 0x0040, "OF_0040"),
	(0x0080, 0x0080, "OF_0080"),
	(0x0100, 0x0100, "OF_0100"),
	(0x0200, 0x0200, "OF_0200"),
	(0x0400, 0x0400, "OF_0400"),
	(0x0800, 0x0800, "OF_0800"),
	# (0x1000, 0x1000, "OF_1000"),
	(0x2000, 0x2000, "OF_2000"),
	(0x4000, 0x4000, "OF_4000"),
	# (0x8000, 0x8000, "OF_8000"),
]
fmt_oflag = lambda self, x: self.fmt_flag(flag_oflag, x)

fmt_o = (
	"O_VAR", # 0
	"O_FLAG", # 1
	"O_MSG", # 2
	"3", # 3
	"4", # 4
	"O_HIT_TIMER", # 5
	"O_POS_X", # 6
	"O_POS_Y", # 7
	"O_POS_Z", # 8
	"O_VEL_X", # 9
	"O_VEL_Y", # 10
	"O_VEL_Z", # 11
	"O_VEL_F", # 12
	"O_VEL_L", # 13
	"O_VEL_U", # 14
	"O_ANG_X", # 15
	"O_ANG_Y", # 16
	"O_ANG_Z", # 17
	"O_SHAPE_ANG_X", # 18
	"O_SHAPE_ANG_Y", # 19
	"O_SHAPE_ANG_Z", # 20
	"O_SHAPE_OFFSET", # 21
	"O_EFFECT", # 22
	"O_GRAVITY", # 23
	"O_GROUND_Y", # 24
	"O_MOVE_STATUS", # 25
	"O_SHAPE_CODE", # 26
	"O_V0", # 27
	"O_V1", # 28
	"O_V2", # 29
	"O_V3", # 30
	"O_V4", # 31
	"O_V5", # 32
	"O_V6", # 33
	"O_V7", # 34
	"O_ANG_VEL_X", # 35
	"O_ANG_VEL_Y", # 36
	"O_ANG_VEL_Z", # 37
	"O_ANIME", # 38
	"O_HOLD", # 39
	"O_WALL_R", # 40
	"O_DRAG", # 41
	"O_HIT_CODE", # 42
	"O_HIT_RESULT", # 43
	"O_OFF_X", # 44
	"O_OFF_Y", # 45
	"O_OFF_Z", # 46
	"O_CODE", # 47
	"48", # 48
	"O_STATE", # 49
	"O_MODE", # 50
	"O_TIMER", # 51
	"O_BOUNCE", # 52
	"O_PL_DIST", # 53
	"O_PL_ANG", # 54
	"O_SAVE_X", # 55
	"O_SAVE_Y", # 56
	"O_SAVE_Z", # 57
	"O_FRICTION", # 58
	"O_DENSITY", # 59
	"O_ANIME_INDEX", # 60
	"O_ALPHA", # 61
	"O_AP", # 62
	"O_HP", # 63
	"O_ACTOR_INFO", # 64
	"O_PREVSTATE", # 65
	"O_HIT_FLAG", # 66
	"O_CHECK_DIST", # 67
	"O_NCOIN", # 68
	"O_SHAPE_DIST", # 69
	"O_AREA", # 70
	"71", # 71
	"O_TAG_INFO", # 72
	"O_V8", # 73
	"O_V9", # 74
	"O_WALL_ANG", # 75
	"O_BG_INFO", # 76
	"O_SAVE_ANG", # 77
	"O_GROUND", # 78
	"O_DIE_SE", # 79
)

fmt_msg_x = [
	None, # 0
	None, # 1
	None, # 2
	None, # 3
	None, # 4
	None, # 5
	None, # 6
	None, # 7
	None, # 8
	None, # 9
	None, # 10
	None, # 11
	None, # 12
	None, # 13
	None, # 14
	None, # 15
	None, # 16
	None, # 17
	None, # 18
	None, # 19
	None, # 20
	None, # 21
	None, # 22
	None, # 23
	None, # 24
	None, # 25
	None, # 26
	None, # 27
	None, # 28
	None, # 29
	None, # 30
	None, # 31
	None, # 32
	None, # 33
	None, # 34
	None, # 35
	None, # 36
	None, # 37
	None, # 38
	None, # 39
	None, # 40
	None, # 41
	None, # 42
	None, # 43
	None, # 44
	None, # 45
	None, # 46
	None, # 47
	None, # 48
	None, # 49
	None, # 50
	None, # 51
	None, # 52
	None, # 53
	None, # 54
	None, # 55
	None, # 56
	None, # 57
	None, # 58
	None, # 59
	None, # 60
	None, # 61
	None, # 62
	None, # 63
	None, # 64
	None, # 65
	None, # 66
	None, # 67
	None, # 68
	None, # 69
	None, # 70
	None, # 71
	None, # 72
	None, # 73
	None, # 74
	None, # 75
	None, # 76
	None, # 77
	None, # 78
	None, # 79
	None, # 80
	None, # 81
	None, # 82
	None, # 83
	None, # 84
	None, # 85
	None, # 86
	None, # 87
	None, # 88
	None, # 89
	None, # 90
	None, # 91
	None, # 92
	None, # 93
	None, # 94
	None, # 95
	None, # 96
	None, # 97
	None, # 98
	None, # 99
	None, # 100
	None, # 101
	None, # 102
	None, # 103
	None, # 104
	None, # 105
	None, # 106
	None, # 107
	None, # 108
	None, # 109
	None, # 110
	None, # 111
	None, # 112
	None, # 113
	None, # 114
	None, # 115
	None, # 116
	None, # 117
	None, # 118
	None, # 119
	None, # 120
	None, # 121
	None, # 122
	None, # 123
	None, # 124
	None, # 125
	None, # 126
	None, # 127
	None, # 128
	None, # 129
	None, # 130
	None, # 131
	None, # 132
	None, # 133
	None, # 134
	None, # 135
	None, # 136
	None, # 137
	None, # 138
	None, # 139
	None, # 140
	None, # 141
	None, # 142
	None, # 143
	None, # 144
	None, # 145
	None, # 146
	None, # 147
	None, # 148
	None, # 149
	None, # 150
	None, # 151
	None, # 152
	None, # 153
	None, # 154
	None, # 155
	None, # 156
	None, # 157
	None, # 158
	None, # 159
	None, # 160
	None, # 161
	None, # 162
	None, # 163
	None, # 164
	None, # 165
	None, # 166
	None, # 167
	None, # 168
	None, # 169
]

def fmt_msg(self, x):
	s = fmt_msg_x[x]
	if s is not None: return "MSG_" + s
	return "%d" % x

fmt_tag_x = [
	"COIN",
	"1", # coin
	"2", # bluecoin (slider)
	"3", # unused, bluecoin (running)
	"REDCOIN",
	None,
	"6", # coin h line (ground)
	"7", # coin h ring (ground)
	"8", # coin arrow (ground)
	"9", # coin h line (air)
	"10", # coin v line (air)
	"11", # coin h ring (air)
	"12", # coin v ring (air)
	"13", # unused, coin arrow (air)
	"14", # secret
	None,
	None,
	None,
	None,
	None,
	"20", # unused, ? (rotating star)
	"SIGNPOST",
	"22", # bob-omb cannon
	"23", # bob-omb buddy
	"24", # unused, butterfly
	"25", # unused, jumping fire
	"26", # unused, 20 fish
	"27", # 5 fish
	"28", # unused, ? (fish related?)
	"29", # secret 1up (chasing)
	"30", # huge goomba
	"31", # tiny goomba
	"32", # 3 goomba
	"33", # unused, 5 goomba
	"34", # wall sign
	"CHUCKYA",
	"CANNON",
	"37", # goomba
	"38", # amp (large path)
	"39", # amp (circular path)
	"40", # unused, ?
	"41", # unused, springboard
	"42", # unused, ball (stands still?)
	"43", # snufit
	"44", # heart
	"45", # 1up (slider)
	"46", # 1up (still)
	"47", # unused, 1up (jumps, then walks away)
	"48", # 1up (reveals, then walks away)
	"49", # ? (1up related?)
	"50", # 1up (still)
	"51", # 1up (still)
	None,
	"BLUECOINSW",
	"54", # hidden bluecoin
	"55", # unused, switch (wing cap)
	"56", # unused, switch (metal cap)
	"57", # unused, switch (vanish cap)
	"58", # unused, switch (yellow)
	"59", # unused, ? (crazy box shape)
	"ITEMBOX_RED",
	"ITEMBOX_GREEN",
	"ITEMBOX_BLUE",
	"ITEMBOX_SHELL",
	"ITEMBOX_COIN", # unused
	"ITEMBOX_COIN3",
	"ITEMBOX_COIN10",
	"67", # itembox (1up)
	"ITEMBOX_STAR1",
	"69", # corkbox
	"70", # corkbox (3 coin)
	"71", # metal box
	"72", # small corkbox
	"73", # corkbox switch
	"74", # hidden corkbox
	"75", # unused, hidden corkbox (wdw?)
	"76", # unused, hidden corkbox (wdw?)
	"77", # large corkbox
	"78", # water shell
	"79", # itembox (1up, running?)
	None,
	"81", # unused, bullet bill
	"82", # heave ho
	None,
	"84", # unused, thwomp
	"85", # fire spit
	"86", # flyguy
	"87", # crazy box
	"88", # 3 butterfly (attack)
	"89", # 3 butterfly
	None,
	None,
	None,
	"93", # bully
	"94", # unused, big bully
	None,
	"96", # unused, (stub)
	"97", # jumping fire
	"98", # v flamethrower
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"106", # wooden stake
	"107", # bubble bomb
	"108", # lakitu
	"109", # unused, koopa the quick
	"110", # unused, koopa the quick flag
	"111", # bob-omb (walk)
	"112", # unused, auto cannon
	"113", # unused, bob-omb buddy
	"114", # auto cannon
	"115", # bob-omb (stand)
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"123", # unused, ? (rotating manta ray)
	None,
	"125", # unused, unagi
	"126", # unused, shark
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"137", # unused, (stub) (klepto model)
	"138", # unused, tornado
	"139", # pokey
	"140", # unused, pokey
	"141", # unused, tox box
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"151", # unused, monty mole (tunnel)
	"152", # monty mole (attack)
	"153", # monty mole hole
	"154", # flyguy
	None,
	"156", # unused, wiggler
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"165", # spindrift
	"166", # snowman
	"167", # unused, snowman
	None,
	"169", # unused, baby penguin
	"170", # unused, mother penguin
	"171", # unused, mother penguin
	"172", # unused, bridge snowman
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"189", # unused, ghost chair
	"190", # ghost chair
	"191", # unused, ghost chair
	"192", # unused, ghost (coin)
	"193", # unused, ghost (coin)
	"194", # unused, ?
	"195", # unused, ?
	"196", # unused, ghost key
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"234", # unused, cheep cheep
	"235", # seaweed
	"CHEST", # unused
	"237", # unused, naval mine
	"238", # unused, 20 piranha
	"239", # 5 piranha
	"240", # unused, water ring
	"241", # unused, water ring
	"SKEETER",
	"243", # clam
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"251", # unused, ukkiki (star)
	"252", # unused, ukkiki (cap)
	"253", # unused, piranha flower (chomp)
	None,
	"255", # whomp
	"256", # chain chomp
	None,
	"258", # koopa
	"259", # unused, koopa (no shell)
	"260", # unused, wooden stake
	"261", # tiny piranha flower (fire)
	"262", # unused, huge piranha flower (fire)
	"263", # tiny koopa
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"281", # moneybag
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"289", # bat
	"290", # bat
	"MR_I",
	"292", # scuttlebug (jump out)
	"293", # scuttlebug
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"303", # unused, unfinished / assume A10 (coin script)
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	# TTC object
	"313",
	"314",
	"315",
	"316",
	"317",
	"318",
	"319",
	"320",
	"321",
	"322", # unused
	"323",
	"324",
	"325",
	"326",
	"327",
	"328",
	"329",
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	None,
	"ITEMBOX_STAR2",
	"ITEMBOX_STAR3",
	"ITEMBOX_STAR4",
	"ITEMBOX_STAR5", # unused
	"ITEMBOX_STAR6",
	None,
	None,
	None,
	None,
	None,
	None,
	# BitS object
	"350", # unused
	"351", # unused
	"352", # unused
	"353", # unused
	"354", # unused
	None,
	None,
	"357", # unused
	"358", # unused
	"359", # unused
	"360", # unused
	None,
	None,
	None,
	None,
	None,
]

def fmt_tag(x):
	s = fmt_tag_x[x]
	if s is not None: return "TAG_" + s
	return "%d" % x

fmt_map_obj_x = {
	0: "PLAYER",
	1: "COIN", # unused
	2: "2", # unused, coin
	3: "3", # unused
	4: "4", # unused, ?
	5: "5", # unused
	6: "6", # unused
	7: "7", # unused
	8: "8", # unused
	10: "10", # unused
	11: "11", # unused
	12: "12", # unused
	13: "13", # unused
	14: "14", # unused
	15: "15", # unused
	16: "16", # unused
	17: "17", # unused
	18: "MR_I", # unused
	19: "BULLY", # unused
	20: "20", # unused, big bully
	26: "26", # unused, coin (slider)
	27: "CHEST", # unused
	28: "28", # unused, water ring
	29: "29", # bowser mine
	32: "BUTTERFLY", # unused
	33: "33", # bowser
	34: "34", # unused
	35: "35", # unused
	36: "36", # unused
	37: "37", # unused
	38: "38", # unused
	39: "39", # unused
	40: "40", # unused
	101: "101",
	102: "102",
	103: "103",
	104: "104",
	105: "105",
	106: "106",
	107: "107",
	108: "108",
	109: "109",
	110: "110",
	111: "111",
	112: "112",
	113: "113",
	114: "114",
	115: "115",
	116: "116",
	117: "117",
	118: "118",
	119: "119",
	120: "120",
	121: "TREE_A",
	122: "TREE_B",
	123: "TREE_C",
	124: "TREE_D", # unused
	125: "TREE_E",
	137: "DOOR_A", # unused
	126: "DOOR_B",
	127: "DOOR_C", # unused
	128: "DOOR_D",
	129: "DOOR_E",
	130: "DOOR_F", # unused
	138: "STARDOOR",
	139: "STARDOOR1",
	140: "STARDOOR3",
	141: "KEYDOOR", # unused
	136: "PORTDOOR_A",
	131: "PORTDOOR_B",
	132: "PORTDOOR_C", # unused
	133: "PORTDOOR_D",
	134: "PORTDOOR_E", # unused
	135: "PORTDOOR_F", # unused
}

def fmt_map_obj(x):
	if x in fmt_map_obj_x: return "MAP_OBJ_" + fmt_map_obj_x[x]
	if x == 255: return "-1"
	return "%d" % x

shp_globl = {
	0: "NULL",

	1: "MARIO",
	143: "GLOW",
	148: "SMOKE",
	149: "SPARKLE",
	150: "DUST",
	156: "SMOKE2",
	163: "RIPPLE_MOVE",
	164: "DROPLET",
	165: "WAVE",
	166: "RIPPLE_STOP",
	167: "SPLASH",
	168: "BUBBLE_A",
	170: "BUBBLE_B",

	23: "TREE_A",
	24: "TREE_B",
	25: "TREE_C",
	26: "TREE_D", # unused
	27: "TREE_E",
	28: "DOOR_A",
	29: "DOOR_B",
	30: "DOOR_C", # unused
	31: "DOOR_D",
	32: "DOOR_E",
	33: "DOOR_F",
	34: "STARDOOR",
	35: "STARDOOR1",
	36: "STARDOOR3",
	37: "KEYDOOR",
	38: "PORTDOOR_A",
	39: "PORTDOOR_B",
	40: "PORTDOOR_C", # unused
	41: "PORTDOOR_D",
	42: "PORTDOOR_E", # unused
	43: "PORTDOOR_F", # unused
	116: "COIN",
	117: "COIN_NOSHADOW",
	118: "BLUECOIN",
	119: "BLUECOIN_NOSHADOW",
	121: "SHADESTAR",
	122: "POWERSTAR",
	124: "SIGNPOST",
	133: "WINGCAP_E",
	134: "CAP_E",
	135: "WINGCAP_S",
	136: "CAP_S",
	138: "SHARD",
	139: "STAR",
	142: "WHITEPUFF",
	144: "FLAME",
	145: "BLUEFLAME",
	158: "SNOW",
	159: "SAND",
	160: "SNOWBALL",
	161: "STONE",
	162: "LEAF",
	185: "FISH",
	186: "FISH_SHADOW",
	187: "BUTTERFLY",
	200: "DOORKEY",
	203: "FLAME_SHADOW",
	204: "BOWSERKEY",
	205: "EXPLOSION",
	212: "1UP",
	215: "REDCOIN",
	216: "REDCOIN_NOSHADOW",
	219: "NUMBER",
	224: "BLACKPUFF",

	120: "HEART",
	127: "CANNONBARREL",
	128: "CANNON",
	129: "BLOCK",
	130: "CRATE",
	131: "DOTBOX",
	132: "DOTBOXMARK",
	137: "ITEMBOX",
	140: "BLUECOINSW",
	180: "IRONBALL",
	188: "BOBOMB",
	190: "SHELL",
	192: "GOOMBA",
	194: "AMP",
	195: "REDBOBOMB",
	201: "CANNONLID",
	202: "LIFT",
	207: "PURPLESW",
	217: "PUSHBLOCK",
	218: "PUSHBLOCK_NOSHADOW",
	220: "FLYGUY",
	223: "CHUCKYA",
	225: "IRONBALL_NOSHADOW",
}

shp_1A = {
	84: "1A_84",
	85: "1A_85",
	86: "1A_86",
	87: "1A_87",
	88: "1A_88",
	89: "1A_89",
}

shp_1B = {
	84: "BLARGG",
	86: "BULLY",
	87: "BIGBULLY",
}

shp_1C = {
	84: "1C_84",
	85: "1C_85",
	86: "1C_86",
}

shp_1D = {
	84: "1D_84",
	85: "1D_85",
	86: "1D_86",
	87: "1D_87",
	88: "1D_88",
}

shp_1E = {
	84: "1E_84",
	85: "1E_85",
	86: "1E_86",
	87: "1E_87",
	88: "1E_88",
	89: "1E_89",
}

shp_1F = {
	84: "1F_84",
	85: "1F_85",
	86: "1F_86",
	87: "1F_87",
}

shp_1G = {
	84: "1G_84",
	85: "1G_85",
	86: "1G_86",
	87: "1G_87",
}

shp_1H = {
	84: "1H_84",
	85: "1H_85",
	86: "1H_86",
}

shp_1I = {
	84: "1I_84",
	85: "1I_85",
	86: "1I_86",
	87: "1I_87",
	88: "1I_88",
	89: "1I_89",
	90: "1I_90",
}

shp_1J = {
	84: "1J_84",
	85: "1J_85",
	222: "1J_222",
}

shp_1K = {
	84: "1K_84",
	85: "1K_85",
	86: "1K_86",
	87: "1K_87",
	88: "1K_88",
	89: "1K_89",
}

shp_2A = {
	100: "2A_100",
	101: "2A_101",
	102: "2A_102",
	103: "2A_103",
	104: "2A_104",
	105: "2A_105",
	179: "2A_179",
}

shp_2B = {
	100: "BUB",
	101: "CHEST",
	102: "CHESTLID",
	103: "PIRANHA",
	104: "WATERRING",
	105: "SKEETER",
	179: "WATERMINE",
	193: "KELP",
}

shp_2C = {
	100: "2C_100",
	101: "2C_101",
	102: "2C_102",
	103: "2C_103",
	104: "2C_104",
	106: "2C_106",
	107: "2C_107",
	191: "2C_191",
}

shp_2D = {
	100: "MIPS",
	101: "BOO2",
	102: "LAKITU2",
	221: "TOAD",
}

shp_2E = {
	100: "2E_100",
	101: "2E_101",
	102: "2E_102",
}

shp_2F = {
	100: "2F_100",
	101: "2F_101",
	102: "2F_102",
	103: "2F_103",
	104: "2F_104",
	206: "2F_206",
}

shp_Select = {
	3: "FILE_MARIO",
	4: "TILE_RED",
	5: "TILE_BLUE",
	6: "TILE_YELLOW",
	7: "TILE_GREEN",
	8: "FILE_MARIO_S",
	9: "FILE_NEW",
	10: "FILE_NEW_S",
	11: "TILE_PURPLE",
	12: "TILE_BUTTON",
}

shp_BBH = {
	53: "BBH_53",
	54: "BBH_54",
	55: "BBH_55",
	56: "BBH_56",
	57: "BBH_57",
	58: "BBH_58",
	59: "BBH_59",
	60: "BBH_60",
}

shp_CCM = {
	3: "CCM_3",
	4: "CCM_4",
	5: "CCM_5",
	6: "CCM_6",
	7: "CCM_7",
	54: "CCM_54",
	55: "CCM_55",
	210: "CCM_210",
}

shp_Inside = {
	53: "INSIDE_53",
	54: "INSIDE_54",
	55: "INSIDE_55",
	56: "INSIDE_56",
	57: "INSIDE_57",
	208: "INSIDE_208",
	209: "INSIDE_209",
	213: "INSIDE_213",
	214: "INSIDE_214",
}

shp_HMC = {
	54: "HMC_54",
	55: "HMC_55",
	56: "HMC_56",
	57: "HMC_57",
	58: "HMC_58",
	59: "HMC_59",
	60: "HMC_60",
}

shp_SSL = {
	3: "SSL_3",
	4: "SSL_4",
	54: "SSL_54",
	55: "SSL_55",
	56: "SSL_56",
	57: "SSL_57",
	58: "SSL_58",
	199: "SSL_199",
}

shp_BoB = {
	54: "BOB_54",
	55: "BOB_55",
	56: "BOB_56",
}

shp_SL = {
	54: "SL_54",
	55: "SL_55",
	56: "SL_56",
}

shp_WDW = {
	54: "WDW_54",
	55: "WDW_55",
	56: "WDW_56",
	57: "WDW_57",
	58: "WDW_58",
	59: "WDW_59",
	60: "WDW_60",
}

shp_JRB = {
	53: "JRB_53",
	54: "JRB_54",
	55: "JRB_55",
	56: "JRB_56",
	57: "JRB_57",
	58: "JRB_58",
	59: "JRB_59",
	60: "JRB_60",
	61: "JRB_61",
	62: "JRB_62",
	63: "JRB_63",
}

shp_THI = {
	3: "THI_3",
	22: "PIPE",
	54: "THI_54",
	55: "THI_55",
}

shp_TTC = {
	54: "TTC_54",
	55: "TTC_55",
	56: "TTC_56",
	57: "TTC_57",
	58: "TTC_58",
	59: "TTC_59",
	60: "TTC_60",
	61: "TTC_61",
	62: "TTC_62",
	63: "TTC_63",
	64: "TTC_64",
	65: "TTC_65",
	66: "TTC_66",
	67: "TTC_67",
	68: "TTC_68",
}

shp_RR = {
	3: "RR_3",
	4: "RR_4",
	5: "RR_5",
	6: "RR_6",
	7: "RR_7",
	8: "RR_8",
	9: "RR_9",
	10: "RR_10",
	11: "RR_11",
	12: "RR_12",
	13: "RR_13",
	14: "RR_14",
	15: "RR_15",
	16: "RR_16",
	17: "RR_17",
	18: "RR_18",
	19: "RR_19",
	20: "RR_20",
	21: "RR_21",
	22: "RR_22",
	54: "RR_54",
	55: "RR_55",
	56: "RR_56",
	57: "RR_57",
	58: "RR_58",
	59: "RR_59",
	60: "RR_60",
	61: "RR_61",
	62: "RR_62",
	63: "RR_63",
	64: "RR_64",
	65: "RR_65",
	66: "RR_66",
	67: "RR_67",
	68: "RR_68",
	69: "RR_69",
}

shp_Grounds = {
	3: "GROUNDS_3",
	22: "PIPE",
	54: "GROUNDS_54",
	55: "GROUNDS_55",
	56: "GROUNDS_56",
}

shp_BitDW = {
	3: "BITDW_3",
	4: "BITDW_4",
	5: "BITDW_5",
	6: "BITDW_6",
	7: "BITDW_7",
	8: "BITDW_8",
	9: "BITDW_9",
	10: "BITDW_10",
	11: "BITDW_11",
	12: "BITDW_12",
	13: "BITDW_13",
	14: "BITDW_14",
	15: "BITDW_15",
	16: "BITDW_16",
	17: "BITDW_17",
	18: "BITDW_PIPE",
	54: "BITDW_54",
	55: "BITDW_55",
	56: "BITDW_56",
	57: "BITDW_57",
	58: "BITDW_58",
	59: "BITDW_59",
	60: "BITDW_60",
	61: "BITDW_61",
	62: "BITDW_62",
	63: "BITDW_63",
}

shp_VCutM = {
	22: "PIPE",
	54: "VCUTM_54",
	55: "VCUTM_55", # invalid
}

shp_BitFS = {
	3: "BITFS_3",
	4: "BITFS_4",
	5: "BITFS_5",
	6: "BITFS_6",
	7: "BITFS_7",
	8: "BITFS_8",
	9: "BITFS_9",
	10: "BITFS_10",
	11: "BITFS_11",
	12: "BITFS_12",
	13: "BITFS_13",
	14: "BITFS_14",
	15: "BITFS_15",
	16: "BITFS_16",
	17: "BITFS_17",
	18: "BITFS_18",
	19: "BITFS_19",
	20: "BITFS_20",
	21: "BITFS_21",
	54: "BITFS_54",
	55: "BITFS_55",
	56: "BITFS_56",
	57: "BITFS_57",
	58: "BITFS_58",
	59: "BITFS_59",
	60: "BITFS_60",
	61: "BITFS_61",
	62: "BITFS_62",
	63: "BITFS_63",
	64: "BITFS_64",
	65: "BITFS_65",
}

shp_SA = {
}

shp_BitS = {
	3: "BITS_3",
	4: "BITS_4",
	5: "BITS_5",
	6: "BITS_6",
	7: "BITS_7",
	8: "BITS_8",
	9: "BITS_9",
	10: "BITS_10",
	11: "BITS_11",
	12: "BITS_12",
	13: "BITS_13",
	14: "BITS_14",
	15: "BITS_15",
	16: "BITS_16",
	17: "BITS_17",
	18: "BITS_18",
	19: "BITS_19",
	20: "BITS_20",
	54: "BITS_54",
	55: "BITS_55",
	57: "BITS_57",
	60: "BITS_60",
	61: "BITS_61",
	62: "BITS_62",
	63: "BITS_63",
	64: "BITS_64",
	65: "BITS_65",
	66: "BITS_66",
	67: "BITS_67",
	68: "BITS_68",
	69: "BITS_69",
	73: "BITS_PIPE",
}

shp_LLL = {
	3: "LLL_3",
	4: "LLL_4",
	5: "LLL_5",
	6: "LLL_6",
	7: "LLL_7",
	8: "LLL_8",
	9: "LLL_9",
	10: "LLL_10",
	11: "LLL_11",
	12: "LLL_12",
	13: "LLL_13",
	14: "LLL_14",
	53: "LLL_53",
	54: "LLL_54",
	55: "LLL_55",
	56: "LLL_56",
	57: "LLL_57",
	58: "LLL_58",
	59: "LLL_59",
	60: "LLL_60",
	61: "LLL_61",
	62: "LLL_62",
	63: "LLL_63",
	64: "LLL_64",
	65: "LLL_65",
	67: "LLL_67",
	68: "LLL_68",
	69: "LLL_69",
	70: "LLL_70",
	71: "LLL_71",
	72: "LLL_72",
	73: "LLL_73",
	74: "LLL_74",
	75: "LLL_75",
	76: "LLL_76",
	77: "LLL_77",
	78: "LLL_78",
	79: "LLL_79",
	80: "LLL_80",
	83: "LLL_83",
}

shp_DDD = {
	54: "DDD_54",
	55: "DDD_55",
	56: "DDD_56",
}

shp_WF = {
	3: "WF_3",
	4: "WF_4",
	5: "WF_5",
	6: "WF_6",
	7: "WF_7",
	8: "WF_8",
	9: "WF_9",
	10: "WF_10",
	12: "WF_12",
	13: "WF_13",
	14: "WF_14",
	15: "WF_15",
	16: "WF_16",
	17: "WF_17",
	18: "WF_18",
	44: "WF_44",
	45: "WF_45",
	46: "WF_46",
	47: "WF_47",
	54: "WF_54",
	55: "WF_55",
	56: "WF_56",
	57: "WF_57",
	58: "WF_58",
	173: "WF_173",
	174: "WF_174",
	175: "WF_175",
	176: "WF_176",
	177: "WF_177",
	178: "WF_178",
}

shp_Ending = {
}

shp_Courtyard = {
	3: "COURTYARD_3",
}

shp_PSS = {
}

shp_CotMC = {
}

shp_TotWC = {
	3: "TOTWC_3",
}

shp_BitDWA = {
	3: "2A_3",
}

shp_WMotR = {
}

shp_BitFSA = {
	54: "BITFSA_54",
}

shp_BitSA = {
	3: "BITSA_3",
	54: "BITSA_54",
	55: "BITSA_55",
	56: "BITSA_56",
	57: "BITSA_57",
	58: "BITSA_58",
	59: "BITSA_59",
	60: "BITSA_60",
	61: "BITSA_61",
	62: "BITSA_62",
	63: "BITSA_63",
}

shp_TTM = {
	3: "TTM_3",
	4: "TTM_4",
	5: "TTM_5",
	6: "TTM_6",
	7: "TTM_7",
	8: "TTM_8",
	9: "TTM_9",
	10: "TTM_10",
	11: "TTM_11",
	12: "TTM_12",
	13: "TTM_13",
	15: "TTM_15",
	16: "TTM_16",
	17: "TTM_17",
	18: "TTM_18",
	19: "TTM_19",
	20: "TTM_20",
	21: "TTM_21",
	22: "TTM_22",
	53: "TTM_53",
	54: "TTM_54",
	55: "TTM_55",
	56: "TTM_56",
	57: "TTM_57",
	58: "TTM_58",
	123: "TTM_123",
}

shp_E0_code_data = {
	# 0x80331920: shp_, # prg 40 125 (3a?)
	# 0x80331928: shp_, # prg 41 181 (3a?)
	0x80331938: shp_2F, # prg 43
	0x80331998: shp_1H, # prg 55
	0x803319A0: shp_1H, # prg 56
	0x803319A8: shp_1H, # prg 57
	0x803319B0: shp_1H, # prg 58
	0x80331A68: shp_1A, # prg 81
	0x80331A70: shp_1A, # prg 82
	0x80331A80: shp_1A, # prg 84
	0x80331AC8: shp_1B, # prg 93
	0x80331AD0: shp_1B, # prg 94
	0x80331AE0: shp_1B, # prg 96 88
	0x80331B30: shp_2C, # prg 106
	0x80331B40: shp_1K, # prg 108
	0x80331B48: shp_2C, # prg 109
	0x80331BB8: shp_1D, # prg 123
	0x80331BC8: shp_1D, # prg 125
	0x80331BD0: shp_1D, # prg 126
	0x80331C28: shp_1E, # prg 137
	0x80331C30: shp_1E, # prg 138
	0x80331C48: shp_SSL, # prg 141
	0x80331C98: shp_1F, # prg 151
	0x80331CA0: shp_1F, # prg 152
	0x80331CA8: shp_1F, # prg 153
	0x80331CC0: shp_1K, # prg 156
	0x80331D08: shp_1G, # prg 165
	0x80331D10: shp_1G, # prg 166
	0x80331D18: shp_1G, # prg 167
	0x80331D28: shp_1G, # prg 169
	0x80331D30: shp_1G, # prg 170
	0x80331D38: shp_1G, # prg 171
	0x80331D40: shp_1G, # prg 172
	0x80331DC8: shp_1I, # prg 189
	0x80331DD0: shp_1I, # prg 190
	0x80331DD8: shp_1I, # prg 191
	0x80331DE0: shp_1I, # prg 192
	0x80331DE8: shp_1I, # prg 193
	0x80331DF0: shp_1I, # prg 194
	0x80331DF8: shp_1I, # prg 195
	0x80331E00: shp_1I, # prg 196
	0x80331F40: shp_2B, # prg 236
	0x80331F48: shp_2B, # prg 237
	0x80331F60: shp_2B, # prg 240
	0x80331F68: shp_2B, # prg 241
	0x80331F70: shp_2B, # prg 242
	0x80331F78: shp_1D, # prg 243
	0x80331FB8: shp_1F, # prg 251
	0x80331FC0: shp_1F, # prg 252
	0x80331FC8: shp_2C, # prg 253
	0x80331FD8: shp_2C, # prg 255
	0x80331FE0: shp_2C, # prg 256
	0x80331FF0: shp_2C, # prg 258
	0x80331FF8: shp_2C, # prg 259
	0x80332000: shp_2C, # prg 260
	0x80332008: shp_2C, # prg 261
	0x80332010: shp_2C, # prg 262
	0x80332018: shp_2C, # prg 263
	0x803320E8: shp_2F, # prg 289
	0x803320F0: shp_2F, # prg 290
	0x80332108: shp_2F, # prg 293
	0x80332158: shp_1K, # prg 303

	# TTC object
	# 0x803321A8: shp_, # prg 313
	# 0x803321B0: shp_, # prg 314
	# 0x803321B8: shp_, # prg 315
	# 0x803321C0: shp_, # prg 316
	# 0x803321C8: shp_, # prg 317
	# 0x803321D0: shp_, # prg 318
	# 0x803321D8: shp_, # prg 319
	# 0x803321E0: shp_, # prg 320
	# 0x803321E8: shp_, # prg 321
	# 0x803321F0: shp_, # prg 322
	# 0x803321F8: shp_, # prg 323
	# 0x80332200: shp_, # prg 324
	# 0x80332208: shp_, # prg 325
	# 0x80332210: shp_, # prg 326
	# 0x80332218: shp_, # prg 327
	# 0x80332220: shp_, # prg 328
	# 0x80332228: shp_, # prg 329

	# BitS object
	# 0x803322D0: shp_, # prg 350 54
	# 0x803322D8: shp_, # prg 351 55
	# 0x803322E0: shp_, # prg 352 56
	# 0x803322E8: shp_, # prg 353 57
	# 0x803322F0: shp_, # prg 354 65
	# 0x80332308: shp_, # prg 357 61
	# 0x80332310: shp_, # prg 358 62
	# 0x80332318: shp_, # prg 359 63
	# 0x80332320: shp_, # prg 360 64

	0x80332370: shp_1I, # map 4
	# 0x80332378: shp_, # map 5 172 (inside)

	# LLL object
	# 0x80332380: shp_, # map 6 54
	# 0x80332388: shp_, # map 7 55
	# 0x80332390: shp_, # map 8 56
	# 0x803323A0: shp_, # map 10 58
	# 0x803323B8: shp_, # map 13 62
	# 0x803323C0: shp_, # map 14 63
	# 0x803323C8: shp_, # map 15 64
	# 0x803323D0: shp_, # map 16 65

	0x803323E8: shp_1B, # map 19
	0x803323F0: shp_1B, # map 20
	0x80332428: shp_2B, # map 27
	0x80332430: shp_2B, # map 28
	0x80332438: shp_2A, # map 29
	0x80332458: shp_2A, # map 33

	# WF object
	# 0x80332460: shp_, # map 34 175
	# 0x80332468: shp_, # map 35 174
	# 0x80332470: shp_, # map 36 173
	# 0x80332488: shp_, # map 39 178
	# 0x80332490: shp_, # map 40 177

	# stageshape
	# 0x80332498: shp_, # map 101
	# 0x803324A0: shp_, # map 102
	# 0x803324A8: shp_, # map 103
	# 0x803324B0: shp_, # map 104
	# 0x803324B8: shp_, # map 105
	# 0x803324C0: shp_, # map 106
	# 0x803324C8: shp_, # map 107
	# 0x803324D0: shp_, # map 108
	# 0x803324D8: shp_, # map 109
	# 0x803324E0: shp_, # map 110
	# 0x803324E8: shp_, # map 111
	# 0x803324F0: shp_, # map 112
	# 0x803324F8: shp_, # map 113
	# 0x80332500: shp_, # map 114
	# 0x80332508: shp_, # map 115
	# 0x80332510: shp_, # map 116
	# 0x80332518: shp_, # map 117
	# 0x80332520: shp_, # map 118
	# 0x80332528: shp_, # map 119
	# 0x80332530: shp_, # map 120
}

shp_E0_Game = [
	(0x1500071C, 0x15000750, shp_1A),
	(0x15000750, 0x1500076C, shp_1B),
	(0x1500076C, 0x15000788, shp_1C),
	(0x15000788, 0x150007B4, shp_1D),
	(0x150007B4, 0x150007E8, shp_1E),
	(0x150007E8, 0x1500080C, shp_1F),
	(0x1500080C, 0x15000830, shp_1G),
	(0x15000830, 0x1500084C, shp_1H),
	(0x1500084C, 0x15000888, shp_1I),
	(0x15000888, 0x150008A4, shp_1J),
	(0x150008A4, 0x150008D8, shp_1K),
	(0x150008D8, 0x15000914, shp_2A),
	(0x15000914, 0x15000958, shp_2B),
	(0x15000958, 0x1500099C, shp_2C),
	(0x1500099C, 0x150009C0, shp_2D),
	(0x150009C0, 0x150009DC, shp_2E),
	(0x150009DC, 0x15000A10, shp_2F),
]

shp_table = {
	"E0.code.data": shp_E0_code_data,
	"E0.Shape1A.Shp": (shp_1A,),
	"E0.Shape1B.Shp": (shp_1B,),
	"E0.Shape1C.Shp": (shp_1C,),
	"E0.Shape1D.Shp": (shp_1D,),
	"E0.Shape1E.Shp": (shp_1E,),
	"E0.Shape1F.Shp": (shp_1F,),
	"E0.Shape1G.Shp": (shp_1G,),
	"E0.Shape1H.Shp": (shp_1H,),
	"E0.Shape1I.Shp": (shp_1I,),
	"E0.Shape1J.Shp": (shp_1J,),
	"E0.Shape1K.Shp": (shp_1K,),
	"E0.Shape2A.Shp": (shp_2A,),
	"E0.Shape2B.Shp": (shp_2B,),
	"E0.Shape2C.Shp": (shp_2C,),
	"E0.Shape2D.Shp": (shp_2D,),
	"E0.Shape2E.Shp": (shp_2E,),
	"E0.Shape2F.Shp": (shp_2F,),
	"E0.Select": (shp_Select,),
	"E0.Game": shp_E0_Game,
	"E0.BBH":       (shp_1I, shp_2F, shp_BBH),
	"E0.CCM":       (shp_1G, shp_2E, shp_CCM),
	"E0.Inside":    (        shp_2D, shp_Inside),
	"E0.HMC":       (shp_1F, shp_2F, shp_HMC),
	"E0.SSL":       (shp_1E,         shp_SSL),
	"E0.BoB":       (shp_1C, shp_2C, shp_BoB),
	"E0.SL":        (shp_1G, shp_2E, shp_SL),
	"E0.WDW":       (shp_1A, shp_2B, shp_WDW),
	"E0.JRB":       (shp_1D, shp_2B, shp_JRB),
	"E0.THI":       (shp_1K, shp_2C, shp_THI),
	"E0.TTC":       (shp_1A,         shp_TTC),
	"E0.RR":        (shp_1K,         shp_RR),
	"E0.Grounds":   (shp_1J, shp_2D, shp_Grounds),
	"E0.BitDW":     (shp_1K, shp_2F, shp_BitDW),
	"E0.VCutM":     (shp_1H,         shp_VCutM),
	"E0.BitFS":     (shp_1B, shp_2F, shp_BitFS),
	"E0.SA":        (shp_1D, shp_2B, shp_SA),
	"E0.BitS":      (        shp_2C, shp_BitS),
	"E0.LLL":       (shp_1B, shp_2F, shp_LLL),
	"E0.DDD":       (shp_1D, shp_2B, shp_DDD),
	"E0.WF":        (shp_1A, shp_2C, shp_WF),
	"E0.Ending":    (                shp_Ending),
	"E0.Courtyard": (shp_1I,         shp_Courtyard),
	"E0.PSS":       (shp_1H,         shp_PSS),
	"E0.CotMC":     (shp_1H, shp_2F, shp_CotMC),
	"E0.TotWC":     (shp_1H,         shp_TotWC),
	"E0.BitDWA":    (        shp_2A, shp_BitDWA),
	"E0.WMotR":     (shp_1B, shp_2F, shp_WMotR),
	"E0.BitFSA":    (        shp_2A, shp_BitFSA),
	"E0.BitSA":     (        shp_2A, shp_BitSA),
	"E0.TTM":       (shp_1F,         shp_TTM),
}

def fmt_shape_x(self, x):
	if self.seg in shp_table:
		shp = shp_table[self.seg]
		if type(shp) is tuple:
			for shp in shp:
				if x in shp: return shp[x]
		if type(shp) is list:
			for start, end, shp in shp:
				if self.save >= start and self.save < end: return shp[x]
		if type(shp) is dict:
			if self.save in shp:
				shp = shp[self.save]
				if x in shp: return shp[x]
	if x in shp_globl: return shp_globl[x]
	return None

def fmt_shape(self, x):
	s = fmt_shape_x(self, x)
	if s is not None: return "S_" + s
	return "%d" % x

fmt_na_mode = [
	"NA_MODE_DEFAULT",
	"NA_MODE_CASTLE",
	"NA_MODE_ARENA",
	"NA_MODE_WATER",
	"NA_MODE_DUNGEON",
	"NA_MODE_FIELD",
	"NA_MODE_GHOST",
	"NA_MODE_STAFF",
]

fmt_na_bgm = {
	0: "NA_BGM_NULL",
	0x000 |  2: "NA_BGM_TITLE",
	0x080 |  2: "NA_BGM_GAMEOVER",
	0x000 |  3: "NA_BGM_FIELD",
	0x000 |  4: "NA_BGM_CASTLE",
	0x000 |  5: "NA_BGM_WATER",
	0x080 |  5: "NA_BGM_AQUARIUM",
	0x000 |  6: "NA_BGM_FIRE",
	0x000 |  7: "NA_BGM_ARENA",
	0x000 |  8: "NA_BGM_SNOW",
	0x000 |  9: "NA_BGM_SLIDER",
	0x000 | 10: "NA_BGM_GHOST",
	0x000 | 12: "NA_BGM_DUNGEON",
	0x000 | 13: "NA_BGM_STARSELECT",
	0x480 | 14: "NA_BGM_SHELL",
	0x000 | 17: "NA_BGM_BOWSER",
	0x000 | 24: "NA_BGM_ENDLESS",
	0x000 | 25: "NA_BGM_FINAL",
	0x000 | 33: "NA_BGM_FILESELECT",
}

fmt_na_se_x = {
	0x00000000: "NA_SE_NULL",

	0x14000001: "NA_SE1_00 + (0 << 16)",
	0x14010001: "NA_SE1_00 + (1 << 16)",
	0x14020001: "NA_SE1_00 + (2 << 16)",
	0x14030001: "NA_SE1_00 + (3 << 16)",
	0x14040001: "NA_SE1_00 + (4 << 16)",
	0x14050001: "NA_SE1_00 + (5 << 16)",
	0x14060001: "NA_SE1_00 + (6 << 16)",
	0x14100001: "NA_SE1_10",
	0x14100001: "NA_SE1_11",
	0x14128001: "NA_SE1_12",
	0x14140001: "NA_SE1_14",
	0x1D192001: "NA_SE1_19",
	0x14200001: "NA_SE1_20",

	0x3004C081: "NA_SE3_04",
	0x3005C081: "NA_SE3_05",
	0x3006C081: "NA_SE3_06",
	0x3007C081: "NA_SE3_07",
	0x30703081: "NA_SE3_70",

	0x40000001: "NA_SE4_00",
	0x40010001: "NA_SE4_01",
	0x40020001: "NA_SE4_02",
	0x41030001: "NA_SE4_03",
	0x40040001: "NA_SE4_04",
	0x40050001: "NA_SE4_05",
	0x40080001: "NA_SE4_08",
	0x40090001: "NA_SE4_09",
	0x400A0001: "NA_SE4_0A",
	0x400B0001: "NA_SE4_0B",
	0x400C0001: "NA_SE4_0C",
	0x400D0001: "NA_SE4_0D_0",

	0x50030081: "NA_SE5_03",
	0x50050081: "NA_SE5_05",
	0x50060081: "NA_SE5_06",
	0x50158081: "NA_SE5_15_80",
	0x50210081: "NA_SE5_21",
	0x502D0081: "NA_SE5_2D",
	0x50388081: "NA_SE5_38",
	0x50390081: "NA_SE5_39",
	0x503A0081: "NA_SE5_3A",
	0x503B0081: "NA_SE5_3B",
	0x503C0081: "NA_SE5_3C",
	0x503DA081: "NA_SE5_3D",
	0x50410081: "NA_SE5_41",
	0x50480081: "NA_SE5_48",
	0x50514001: "NA_SE5_51",
	0x50558081: "NA_SE5_55",
	0x50584081: "NA_SE5_58",
	0x505F8091: "NA_SE5_5F",
	0x5060B081: "NA_SE5_60",
	0x5061B081: "NA_SE5_61",
	0x506F0081: "NA_SE5_6F",

	0x60000001: "NA_SE6_00",
	0x60028001: "NA_SE6_02_80",
	0x60034001: "NA_SE6_03",
	0x60044001: "NA_SE6_04_40",
	0x60048001: "NA_SE6_04_80",
	0x60104001: "NA_SE6_10",

	0x80504001: "NA_SE8_50",

	0x90040081: "NA_SE9_04",
	0x90524001: "NA_SE9_52",
	0x90694081: "NA_SE9_69",
}

def fmt_na_se(self, x):
	if x not in fmt_na_se_x:
		print("\t0x%08X: \"NA_SE%X_%02X\"," % (
			x, x >> 28 & 0x0F, x >> 16 & 0xFF
		))
		return "0x%08X" % x
	return fmt_na_se_x[x]
