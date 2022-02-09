import table
import ultra

fmt_bool = ["false", "true"]

def fmt_mask(x):
    fd, fx, x = ("~%d", "~0x%02X", ~x) if x < 0 else ("%d", "0x%02X", x)
    return fd % x if x < 10 else fx % x

def fmt_time(x):
    x, y = x//30, x%30
    if x == 0: return    "%d" % y
    if y == 0: return "30*%d" % x
    return "30*%d+%d" % (x, y)

fmt_stage_x = [
    "NULL",
    "1",
    "2",
    "3",
    "BBH",
    "CCM",
    "INSIDE",
    "HMC",
    "SSL",
    "BOB",
    "SL",
    "WDW",
    "JRB",
    "THI",
    "TTC",
    "RR",
    "GROUNDS",
    "BITDW",
    "VCUTM",
    "BITFS",
    "SA",
    "BITS",
    "LLL",
    "DDD",
    "WF",
    "ENDING",
    "COURTYARD",
    "PSS",
    "COTMC",
    "TOTWC",
    "BITDWA",
    "WMOTR",
    "32",
    "BITFSA",
    "BITSA",
    "35",
    "TTM",
    "37",
    "38",
]

def fmt_stage(x):
    return "STAGE_" + fmt_stage_x[x]

fmt_mem_alloc = [
    "MEM_ALLOC_L",
    "MEM_ALLOC_R",
]

fmt_s_layer_x = [
    "BACKGROUND",
    "OPA_SURF",
    "OPA_DECAL",
    "OPA_INTER",
    "TEX_EDGE",
    "XLU_SURF",
    "XLU_DECAL",
    "XLU_INTER",
]

def fmt_s_layer(x):
    return "S_LAYER_" + fmt_s_layer_x[x]

fmt_o_type_x = [
    "PLAYER",
    "1",
    "PL_ATTACK",
    "3",
    "ENEMYA",
    "ENEMYB",
    "ITEM",
    "7",
    "DEFAULT",
    "MOVEBG",
    "PL_USE",
    "SYSTEM",
    "EFFECT",
]

def fmt_o_type(x):
    return "O_TYPE_" + fmt_o_type_x[x]

fmt_p_obj_x = [
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
    "35", # chuckya
    "36", # cannon
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
    "53", # bluecoin switch
    "54", # hidden bluecoin
    "55", # unused, switch (wing cap)
    "56", # unused, switch (metal cap)
    "57", # unused, switch (vanish cap)
    "58", # unused, switch (yellow)
    "59", # unused, ? (crazy box shape)
    "60", # itembox (wing cap)
    "61", # itembox (metal cap)
    "62", # itembox (vanish cap)
    "63", # itembox (shell)
    "64", # unused, itembox (1 coin)
    "65", # itembox (3 coin)
    "66", # itembox (10 coin)
    "67", # itembox (1up)
    "68", # itembox (power star 1)
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
    "236", # unused, chest
    "237", # unused, naval mine
    "238", # unused, 20 piranha
    "239", # 5 piranha
    "240", # unused, water ring
    "241", # unused, water ring
    "242", # skeeter
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
    "291", # mr. i
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
    "339", # itembox (power star 2)
    "340", # itembox (power star 3)
    "341", # itembox (power star 4)
    "342", # unused, itembox (power star 5)
    "343", # itembox (power star 6)
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

def fmt_p_obj(x):
    s = fmt_p_obj_x[x]
    if s != None: return "P_OBJ_" + s
    return "%d" % x

fmt_m_obj_x = {
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
    18: "18", # unused, mr. i
    19: "BULLY", # unused
    20: "20", # unused, big bully
    26: "26", # unused, coin (slider)
    27: "27", # unused, chest
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
    136: "LINKDOOR_A",
    131: "LINKDOOR_B",
    132: "LINKDOOR_C", # unused
    133: "LINKDOOR_D",
    134: "LINKDOOR_E", # unused
    135: "LINKDOOR_F", # unused
}

def fmt_m_obj(x):
    if x in fmt_m_obj_x: return "M_OBJ_" + fmt_m_obj_x[x]
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
    38: "LINKDOOR_A",
    39: "LINKDOOR_B",
    40: "LINKDOOR_C", # unused
    41: "LINKDOOR_D",
    42: "LINKDOOR_E", # unused
    43: "LINKDOOR_F", # unused
    116: "COIN",
    117: "COIN_NOSHADOW",
    118: "BLUECOIN",
    119: "BLUECOIN_NOSHADOW",
    121: "SHADOWSTAR",
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

    120: "3A_120",
    127: "3A_127",
    128: "3A_128",
    129: "3A_129",
    130: "3A_130",
    131: "3A_131",
    132: "3A_132",
    137: "3A_137",
    140: "3A_140",
    180: "3A_180",
    188: "3A_188",
    190: "3A_190",
    192: "3A_192",
    194: "3A_194",
    195: "3A_195",
    201: "3A_201",
    202: "3A_202",
    207: "3A_207",
    217: "3A_217",
    218: "3A_218",
    220: "3A_220",
    223: "3A_223",
    225: "3A_225",
}

shp_1a = {
    84: "1A_84",
    85: "1A_85",
    86: "1A_86",
    87: "1A_87",
    88: "1A_88",
    89: "1A_89",
}

shp_1b = {
    84: "BLARGG",
    86: "BULLY",
    87: "BIGBULLY",
}

shp_1c = {
    84: "1C_84",
    85: "1C_85",
    86: "1C_86",
}

shp_1d = {
    84: "1D_84",
    85: "1D_85",
    86: "1D_86",
    87: "1D_87",
    88: "1D_88",
}

shp_1e = {
    84: "1E_84",
    85: "1E_85",
    86: "1E_86",
    87: "1E_87",
    88: "1E_88",
    89: "1E_89",
}

shp_1f = {
    84: "1F_84",
    85: "1F_85",
    86: "1F_86",
    87: "1F_87",
}

shp_1g = {
    84: "1G_84",
    85: "1G_85",
    86: "1G_86",
    87: "1G_87",
}

shp_1h = {
    84: "1H_84",
    85: "1H_85",
    86: "1H_86",
}

shp_1i = {
    84: "1I_84",
    85: "1I_85",
    86: "1I_86",
    87: "1I_87",
    88: "1I_88",
    89: "1I_89",
    90: "1I_90",
}

shp_1j = {
    84: "1J_84",
    85: "1J_85",
    222: "1J_222",
}

shp_1k = {
    84: "1K_84",
    85: "1K_85",
    86: "1K_86",
    87: "1K_87",
    88: "1K_88",
    89: "1K_89",
}

shp_2a = {
    100: "2A_100",
    101: "2A_101",
    102: "2A_102",
    103: "2A_103",
    104: "2A_104",
    105: "2A_105",
    179: "2A_179",
}

shp_2b = {
    100: "2B_100",
    101: "2B_101",
    102: "2B_102",
    103: "2B_103",
    104: "2B_104",
    105: "2B_105",
    179: "2B_179",
    193: "2B_193",
}

shp_2c = {
    100: "2C_100",
    101: "2C_101",
    102: "2C_102",
    103: "2C_103",
    104: "2C_104",
    106: "2C_106",
    107: "2C_107",
    191: "2C_191",
}

shp_2d = {
    100: "2D_100",
    101: "2D_101",
    102: "2D_102",
    221: "2D_221",
}

shp_2e = {
    100: "2E_100",
    101: "2E_101",
    102: "2E_102",
}

shp_2f = {
    100: "2F_100",
    101: "2F_101",
    102: "2F_102",
    103: "2F_103",
    104: "2F_104",
    206: "2F_206",
}

shp_select = {
    3: "SELECT_3",
    4: "SELECT_4",
    5: "SELECT_5",
    6: "SELECT_6",
    7: "SELECT_7",
    8: "SELECT_8",
    9: "SELECT_9",
    10: "SELECT_10",
    11: "SELECT_11",
    12: "SELECT_12",
}

shp_bbh = {
    53: "BBH_53",
    54: "BBH_54",
    55: "BBH_55",
    56: "BBH_56",
    57: "BBH_57",
    58: "BBH_58",
    59: "BBH_59",
    60: "BBH_60",
}

shp_ccm = {
    3: "CCM_3",
    4: "CCM_4",
    5: "CCM_5",
    6: "CCM_6",
    7: "CCM_7",
    54: "CCM_54",
    55: "CCM_55",
    210: "CCM_210",
}

shp_inside = {
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

shp_hmc = {
    54: "HMC_54",
    55: "HMC_55",
    56: "HMC_56",
    57: "HMC_57",
    58: "HMC_58",
    59: "HMC_59",
    60: "HMC_60",
}

shp_ssl = {
    3: "SSL_3",
    4: "SSL_4",
    54: "SSL_54",
    55: "SSL_55",
    56: "SSL_56",
    57: "SSL_57",
    58: "SSL_58",
    199: "SSL_199",
}

shp_bob = {
    54: "BOB_54",
    55: "BOB_55",
    56: "BOB_56",
}

shp_sl = {
    54: "SL_54",
    55: "SL_55",
    56: "SL_56",
}

shp_wdw = {
    54: "WDW_54",
    55: "WDW_55",
    56: "WDW_56",
    57: "WDW_57",
    58: "WDW_58",
    59: "WDW_59",
    60: "WDW_60",
}

shp_jrb = {
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

shp_thi = {
    3: "THI_3",
    22: "PIPE",
    54: "THI_54",
    55: "THI_55",
}

shp_ttc = {
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

shp_rr = {
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

shp_ground = {
    3: "GROUNDS_3",
    22: "PIPE",
    54: "GROUNDS_54",
    55: "GROUNDS_55",
    56: "GROUNDS_56",
}

shp_bitdw = {
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

shp_vcutm = {
    22: "PIPE",
    54: "VCUTM_54",
    55: "VCUTM_55", # invalid
}

shp_bitfs = {
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

shp_sa = {
}

shp_bits = {
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

shp_lll = {
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

shp_ddd = {
    54: "DDD_54",
    55: "DDD_55",
    56: "DDD_56",
}

shp_wf = {
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

shp_ending = {
}

shp_courty = {
    3: "COURTYARD_3",
}

shp_pss = {
}

shp_cotmc = {
}

shp_totwc = {
    3: "TOTWC_3",
}

shp_bitdwa = {
    3: "2A_3",
}

shp_wmotr = {
}

shp_bitfsa = {
    54: "BITFSA_54",
}

shp_bitsa = {
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

shp_ttm = {
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

shp_table = (
    (0x0012A7E0, 0x00132C60, "E0", shp_1a),
    (0x00132C60, 0x00134D20, "E0", shp_1b),
    (0x00134D20, 0x0013B910, "E0", shp_1c),
    (0x0013B910, 0x00145E90, "E0", shp_1d),
    (0x00145E90, 0x001521D0, "E0", shp_1e),
    (0x001521D0, 0x00160670, "E0", shp_1f),
    (0x00160670, 0x00165A50, "E0", shp_1g),
    (0x00165A50, 0x00166C60, "E0", shp_1h),
    (0x00166C60, 0x0016D870, "E0", shp_1i),
    (0x0016D870, 0x00180BB0, "E0", shp_1j),
    (0x00180BB0, 0x00188440, "E0", shp_1k),
    (0x00188440, 0x001B9CC0, "E0", shp_2a),
    (0x001B9CC0, 0x001C4230, "E0", shp_2b),
    (0x001C4230, 0x001D8310, "E0", shp_2c),
    (0x001D8310, 0x001E51F0, "E0", shp_2d),
    (0x001E51F0, 0x001E7EE0, "E0", shp_2e),
    (0x001E7EE0, 0x001F2200, "E0", shp_2f),
    (0x002A6120, 0x002ABCA0, "E0", shp_select),
    (0x002AC3BC, 0x002AC3F0, "E0", shp_1a),
    (0x002AC3F0, 0x002AC40C, "E0", shp_1b),
    (0x002AC40C, 0x002AC428, "E0", shp_1c),
    (0x002AC428, 0x002AC454, "E0", shp_1d),
    (0x002AC454, 0x002AC488, "E0", shp_1e),
    (0x002AC488, 0x002AC4AC, "E0", shp_1f),
    (0x002AC4AC, 0x002AC4EC, "E0", shp_1g),
    (0x002AC4D0, 0x002AC4EC, "E0", shp_1h),
    (0x002AC4EC, 0x002AC528, "E0", shp_1i),
    (0x002AC528, 0x002AC544, "E0", shp_1j),
    (0x002AC544, 0x002AC578, "E0", shp_1k),
    (0x002AC578, 0x002AC5B4, "E0", shp_2a),
    (0x002AC5B4, 0x002AC5F8, "E0", shp_2b),
    (0x002AC5F8, 0x002AC63C, "E0", shp_2c),
    (0x002AC63C, 0x002AC660, "E0", shp_2d),
    (0x002AC660, 0x002AC67C, "E0", shp_2e),
    (0x002AC67C, 0x002AC6B0, "E0", shp_2f),
    (0x00371C40, 0x00383950, "E0", shp_1i, shp_2f, shp_bbh),
    (0x00383950, 0x00396340, "E0", shp_1g, shp_2e, shp_ccm),
    (0x00396340, 0x003D0DC0, "E0",         shp_2d, shp_inside),
    (0x003D0DC0, 0x003E76B0, "E0", shp_1f, shp_2f, shp_hmc),
    (0x003E76B0, 0x003FC2B0, "E0", shp_1e,         shp_ssl),
    (0x003FC2B0, 0x00405FB0, "E0", shp_1c, shp_2c, shp_bob),
    (0x00405FB0, 0x0040ED70, "E0", shp_1g, shp_2e, shp_sl),
    (0x0040ED70, 0x0041A760, "E0", shp_1a, shp_2b, shp_wdw),
    (0x0041A760, 0x004246D0, "E0", shp_1d, shp_2b, shp_jrb),
    (0x004246D0, 0x0042CF20, "E0", shp_1k, shp_2c, shp_thi),
    (0x0042CF20, 0x00437870, "E0", shp_1a,         shp_ttc),
    (0x00437870, 0x0044ABC0, "E0", shp_1k,         shp_rr),
    (0x0044ABC0, 0x00454E00, "E0", shp_1j, shp_2d, shp_ground),
    (0x00454E00, 0x0045C600, "E0", shp_1k, shp_2f, shp_bitdw),
    (0x0045C600, 0x004614D0, "E0", shp_1h,         shp_vcutm),
    (0x004614D0, 0x0046B090, "E0", shp_1b, shp_2f, shp_bitfs),
    (0x0046B090, 0x0046C3A0, "E0", shp_1d, shp_2b, shp_sa),
    (0x0046C3A0, 0x004784A0, "E0",         shp_2c, shp_bits),
    (0x004784A0, 0x0048D930, "E0", shp_1b, shp_2f, shp_lll),
    (0x0048D930, 0x00496090, "E0", shp_1d, shp_2b, shp_ddd),
    (0x00496090, 0x0049E710, "E0", shp_1a, shp_2c, shp_wf),
    (0x0049E710, 0x004AC570, "E0",                 shp_ending),
    (0x004AC570, 0x004AF930, "E0", shp_1i,         shp_courty),
    (0x004AF930, 0x004B80D0, "E0", shp_1h,         shp_pss),
    (0x004B80D0, 0x004BEC30, "E0", shp_1h, shp_2f, shp_cotmc),
    (0x004BEC30, 0x004C2920, "E0", shp_1h,         shp_totwc),
    (0x004C2920, 0x004C4320, "E0",         shp_2a, shp_bitdwa),
    (0x004C4320, 0x004CDBD0, "E0", shp_1b, shp_2f, shp_wmotr),
    (0x004CDBD0, 0x004CEC00, "E0",         shp_2a, shp_bitfsa),
    (0x004CEC00, 0x004D1910, "E0",         shp_2a, shp_bitsa),
    (0x004D1910, 0x004EC000, "E0", shp_1f,         shp_ttm),
)

shp_dev_E0 = {
    # 0x000EC920: shp_, # prg 40 125 (3a?)
    # 0x000EC928: shp_, # prg 41 181 (3a?)
    0x000EC938: shp_2f, # prg 43
    0x000EC998: shp_1h, # prg 55
    0x000EC9A0: shp_1h, # prg 56
    0x000EC9A8: shp_1h, # prg 57
    0x000EC9B0: shp_1h, # prg 58
    0x000ECA68: shp_1a, # prg 81
    0x000ECA70: shp_1a, # prg 82
    0x000ECA80: shp_1a, # prg 84
    0x000ECAC8: shp_1b, # prg 93
    0x000ECAD0: shp_1b, # prg 94
    0x000ECAE0: shp_1b, # prg 96 88
    0x000ECB30: shp_2c, # prg 106
    0x000ECB40: shp_1k, # prg 108
    0x000ECB48: shp_2c, # prg 109
    0x000ECBB8: shp_1d, # prg 123
    0x000ECBC8: shp_1d, # prg 125
    0x000ECBD0: shp_1d, # prg 126
    0x000ECC28: shp_1e, # prg 137
    0x000ECC30: shp_1e, # prg 138
    0x000ECC48: shp_ssl, # prg 141
    0x000ECC98: shp_1f, # prg 151
    0x000ECCA0: shp_1f, # prg 152
    0x000ECCA8: shp_1f, # prg 153
    0x000ECCC0: shp_1k, # prg 156
    0x000ECD08: shp_1g, # prg 165
    0x000ECD10: shp_1g, # prg 166
    0x000ECD18: shp_1g, # prg 167
    0x000ECD28: shp_1g, # prg 169
    0x000ECD30: shp_1g, # prg 170
    0x000ECD38: shp_1g, # prg 171
    0x000ECD40: shp_1g, # prg 172
    0x000ECDC8: shp_1i, # prg 189
    0x000ECDD0: shp_1i, # prg 190
    0x000ECDD8: shp_1i, # prg 191
    0x000ECDE0: shp_1i, # prg 192
    0x000ECDE8: shp_1i, # prg 193
    0x000ECDF0: shp_1i, # prg 194
    0x000ECDF8: shp_1i, # prg 195
    0x000ECE00: shp_1i, # prg 196
    0x000ECF40: shp_2b, # prg 236
    0x000ECF48: shp_2b, # prg 237
    0x000ECF60: shp_2b, # prg 240
    0x000ECF68: shp_2b, # prg 241
    0x000ECF70: shp_2b, # prg 242
    0x000ECF78: shp_1d, # prg 243
    0x000ECFB8: shp_1f, # prg 251
    0x000ECFC0: shp_1f, # prg 252
    0x000ECFC8: shp_2c, # prg 253
    0x000ECFD8: shp_2c, # prg 255
    0x000ECFE0: shp_2c, # prg 256
    0x000ECFF0: shp_2c, # prg 258
    0x000ECFF8: shp_2c, # prg 259
    0x000ED000: shp_2c, # prg 260
    0x000ED008: shp_2c, # prg 261
    0x000ED010: shp_2c, # prg 262
    0x000ED018: shp_2c, # prg 263
    0x000ED0E8: shp_2f, # prg 289
    0x000ED0F0: shp_2f, # prg 290
    0x000ED108: shp_2f, # prg 293
    0x000ED158: shp_1k, # prg 303

    # TTC object
    # 0x000ED1A8: shp_, # prg 313
    # 0x000ED1B0: shp_, # prg 314
    # 0x000ED1B8: shp_, # prg 315
    # 0x000ED1C0: shp_, # prg 316
    # 0x000ED1C8: shp_, # prg 317
    # 0x000ED1D0: shp_, # prg 318
    # 0x000ED1D8: shp_, # prg 319
    # 0x000ED1E0: shp_, # prg 320
    # 0x000ED1E8: shp_, # prg 321
    # 0x000ED1F0: shp_, # prg 322
    # 0x000ED1F8: shp_, # prg 323
    # 0x000ED200: shp_, # prg 324
    # 0x000ED208: shp_, # prg 325
    # 0x000ED210: shp_, # prg 326
    # 0x000ED218: shp_, # prg 327
    # 0x000ED220: shp_, # prg 328
    # 0x000ED228: shp_, # prg 329

    # BitS object
    # 0x000ED2D0: shp_, # prg 350 54
    # 0x000ED2D8: shp_, # prg 351 55
    # 0x000ED2E0: shp_, # prg 352 56
    # 0x000ED2E8: shp_, # prg 353 57
    # 0x000ED2F0: shp_, # prg 354 65
    # 0x000ED308: shp_, # prg 357 61
    # 0x000ED310: shp_, # prg 358 62
    # 0x000ED318: shp_, # prg 359 63
    # 0x000ED320: shp_, # prg 360 64

    0x000ED370: shp_1i, # map 4
    # 0x000ED378: shp_, # map 5 172 (inside)

    # LLL object
    # 0x000ED380: shp_, # map 6 54
    # 0x000ED388: shp_, # map 7 55
    # 0x000ED390: shp_, # map 8 56
    # 0x000ED3A0: shp_, # map 10 58
    # 0x000ED3B8: shp_, # map 13 62
    # 0x000ED3C0: shp_, # map 14 63
    # 0x000ED3C8: shp_, # map 15 64
    # 0x000ED3D0: shp_, # map 16 65

    0x000ED3E8: shp_1b, # map 19
    0x000ED3F0: shp_1b, # map 20
    0x000ED428: shp_2b, # map 27
    0x000ED430: shp_2b, # map 28
    0x000ED438: shp_2a, # map 29
    0x000ED458: shp_2a, # map 33

    # WF object
    # 0x000ED460: shp_, # map 34 175
    # 0x000ED468: shp_, # map 35 174
    # 0x000ED470: shp_, # map 36 173
    # 0x000ED488: shp_, # map 39 178
    # 0x000ED490: shp_, # map 40 177

    # stageshape
    # 0x000ED498: shp_, # map 101
    # 0x000ED4A0: shp_, # map 102
    # 0x000ED4A8: shp_, # map 103
    # 0x000ED4B0: shp_, # map 104
    # 0x000ED4B8: shp_, # map 105
    # 0x000ED4C0: shp_, # map 106
    # 0x000ED4C8: shp_, # map 107
    # 0x000ED4D0: shp_, # map 108
    # 0x000ED4D8: shp_, # map 109
    # 0x000ED4E0: shp_, # map 110
    # 0x000ED4E8: shp_, # map 111
    # 0x000ED4F0: shp_, # map 112
    # 0x000ED4F8: shp_, # map 113
    # 0x000ED500: shp_, # map 114
    # 0x000ED508: shp_, # map 115
    # 0x000ED510: shp_, # map 116
    # 0x000ED518: shp_, # map 117
    # 0x000ED520: shp_, # map 118
    # 0x000ED528: shp_, # map 119
    # 0x000ED530: shp_, # map 120
}

shp_dev = (
    ("E0", shp_dev_E0),
)

def fmt_shape_x(x):
    self = ultra.script
    dev = table.dev_addr(self)
    for data, shp in shp_dev:
        if self.c_data.startswith(data):
            if dev in shp and x in shp[dev]: return shp[dev][x]
    for shp in shp_table:
        if dev >= shp[0] and dev < shp[1] and self.c_data.startswith(shp[2]):
            for s in shp[3:]:
                if x in s: return s[x]
    if x in shp_globl: return shp_globl[x]
    return None

def fmt_shape(x):
    s = fmt_shape_x(x)
    if s != None: return "S_" + s
    return "%d" % x

seq_table = [
    "se",
    "star_catch",
    "title",
    "field",
    "castle",
    "water",
    "fire",
    "arena",
    "snow",
    "slider",
    "ghost",
    "lullaby",
    "dungeon",
    "star_select",
    "wing",
    "metal",
    "msg_bowser",
    "bowser",
    "hi_score",
    "merry_go_round",
    "fanfare",
    "star",
    "battle",
    "arena_clear",
    "endless",
    "final",
    "staff",
    "solution",
    "msg_toad",
    "msg_peach",
    "intro",
    "final_clear",
    "ending",
    "file_select",
    "msg_lakitu",
]

fmt_na_mode_x = [
    "DEFAULT",
    "CASTLE",
    "ARENA",
    "WATER",
    "DUNGEON",
    "FIELD",
    "GHOST",
    "STAFF",
]

def fmt_na_mode(x):
    return "NA_MODE_" + fmt_na_mode_x[x]

fmt_na_bgm_x = {
    0: "NULL",
    0x000 |  2: "TITLE",
    0x080 |  2: "GAMEOVER",
    0x000 |  3: "FIELD",
    0x000 |  4: "CASTLE",
    0x000 |  5: "WATER",
    0x080 |  5: "AQUARIUM",
    0x000 |  6: "FIRE",
    0x000 |  7: "ARENA",
    0x000 |  8: "SNOW",
    0x000 |  9: "SLIDER",
    0x000 | 10: "GHOST",
    0x000 | 12: "DUNGEON",
    0x000 | 13: "STAR_SELECT",
    0x480 | 14: "SHELL",
    0x000 | 17: "BOWSER",
    0x000 | 24: "ENDLESS",
    0x000 | 25: "FINAL",
    0x000 | 33: "FILE_SELECT",
}

def fmt_na_bgm(x):
    return "NA_BGM_" + fmt_na_bgm_x[x]

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

def fmt_na_se(x):
    if x not in fmt_na_se_x:
        print("    0x%08X: \"NA_SE%X_%02X\"," % (
            x, x >> 28 & 0x0F, x >> 16 & 0xFF
        ))
        return "0x%08X" % x
    return fmt_na_se_x[x]

sym_E0_t_ipl3 = {
    0xA40004C0: table.sym("_A40004C0"), # la
    0xA4000774: table.sym("_A4000774"), # la
    0xA4000778: table.sym("_A4000778"),
    0xA4000880: table.sym("_A4000880"),
    0xA400090C: table.sym("_A400090C"),
    0xA4000980: table.sym("_A4000980"),
    0xA4000A40: table.sym("_A4000A40"),
    0xA4000AD0: table.sym("_A4000AD0"),
}

sym_E0_t_crt0 = {
    # ==========================================================================
    # text
    # ==========================================================================

    # ultra/PR/crt0.S
    0x80246000: table.sym("_start", table.GLOBL),

    0x80200600: table.sym("_stack"),
    0x8033A580: table.sym("_bss_start"),
}

imm_E0_t_crt0 = {
    0x80246004: ("_bss_size_hi",),
    0x8024600C: ("_bss_size_lo",),
}

sym_E0_t_ultra = {
    0x00000000: table.sym("NULL"),

    # ==========================================================================
    # text
    # ==========================================================================

    # ultra/src/parameters.S
    0x80000300: table.sym("osTvType"),
    0x80000304: table.sym("osRomType"),
    0x80000308: table.sym("osRomBase"),
    0x8000030C: table.sym("osResetType"),
    0x80000310: table.sym("osCicId"),
    0x80000314: table.sym("osVersion"),
    0x80000318: table.sym("osMemSize"),
    0x8000031C: table.sym("osAppNMIBuffer"),

    # ultra/src/settime.S
    0x803223B0: table.sym_fnc("osSetTime", arg=(
        "OSTime time",
    ), flag=table.GLOBL),

    # ultra/src/maptlb.S
    0x803223E0: table.sym_fnc("osMapTLB", arg=(
        "s32 index",
        "OSPageMask pm",
        "void *vaddr",
        "u32 evenpaddr",
        "u32 oddpaddr",
        "s32 asid",
    ), flag=table.GLOBL),

    # ultra/src/unmaptlball.S
    0x803224A0: table.sym_fnc("osUnmapTLBAll", flag=table.GLOBL),

    # ultra/src/sprintf.S
    0x803224F0: table.sym_fnc("sprintf", "int", (
        "char *",
        "const char *",
        "...",
    ), table.GLOBL),
    0x8032255C: table.sym("proutSprintf"),

    # ultra/src/createmesgqueue.S
    0x803225A0: table.sym_fnc("osCreateMesgQueue", arg=(
        "OSMesgQueue *mq",
        "OSMesg *msg",
        "s32 count",
    ), flag=table.GLOBL),

    # ultra/src/seteventmesg.S
    0x803225D0: table.sym_fnc("osSetEventMesg", arg=(
        "OSEvent e",
        "OSMesgQueue *mq",
        "OSMesg m",
    ), flag=table.GLOBL),

    # ultra/src/visetevent.S
    0x80322640: table.sym_fnc("osViSetEvent", arg=(
        "OSMesgQueue *mq",
        "OSMesg msg",
        "u32 retraceCount",
    ), flag=table.GLOBL),

    # ultra/src/createthread.S
    0x803226B0: table.sym_fnc("osCreateThread", arg=(
        "OSThread *t",
        "OSId id",
        "void (*entry)(void *)",
        "void *arg",
        "void *sp",
        "OSPri pri",
    ), flag=table.GLOBL),

    # ultra/src/recvmesg.S
    0x80322800: table.sym_fnc("osRecvMesg", "s32", (
        "OSMesgQueue *mq",
        "OSMesg *msg",
        "s32 flag",
    ), table.GLOBL),

    # ultra/src/sptask.S
    0x80322940: table.sym("_VirtualToPhysicalTask"),
    0x80322A5C: table.sym_fnc("osSpTaskLoad", arg=(
        "OSTask *task",
    ), flag=table.GLOBL),
    0x80322BBC: table.sym_fnc("osSpTaskStartGo", "s32", (
        "OSTask *task",
    ), table.GLOBL),

    # ultra/src/sptaskyield.S
    0x80322C00: table.sym_fnc("osSpTaskYield", "s32", flag=table.GLOBL),

    # ultra/src/sendmesg.S
    0x80322C20: table.sym_fnc("osSendMesg", arg=(
        "OSMesgQueue *mq",
        "OSMesg msg",
        "s32 flag",
    ), flag=table.GLOBL),

    # ultra/src/sptaskyielded.S
    0x80322D70: table.sym_fnc("osSpTaskYielded", "OSYieldResult", (
        "OSTask *task",
    ), table.GLOBL),

    # ultra/src/startthread.S
    0x80322DF0: table.sym_fnc("osStartThread", arg=(
        "OSThread *t",
    ), flag=table.GLOBL),

    # ultra/src/writebackdcacheall.S
    0x80322F40: table.sym_fnc("osWritebackDCacheAll", flag=table.GLOBL),

    # ultra/src/vimgr.S
    0x80322F70: table.sym_fnc("osCreateViManager", arg=(
        "OSPri pri",
    ), flag=table.GLOBL),
    0x803230F4: table.sym("viMgrMain"),

    # ultra/src/visetmode.S
    0x803232D0: table.sym_fnc("osViSetMode", arg=(
        "OSViMode *mode",
    ), flag=table.GLOBL),

    # ultra/src/viblack.S
    0x80323340: table.sym_fnc("osViBlack", arg=(
        "u8 active",
    ), flag=table.GLOBL),

    # ultra/src/visetspecial.S
    0x803233B0: table.sym_fnc("osViSetSpecialFeatures", arg=(
        "u32 func",
    ), flag=table.GLOBL),

    # ultra/src/pimgr.S
    0x80323570: table.sym_fnc("osCreatePiManager", arg=(
        "OSPri pri",
        "OSMesgQueue *cmdQ",
        "OSMesg *cmdBuf",
        "s32 cmdMsgCnt",
    ), flag=table.GLOBL),

    # ultra/src/setthreadpri.S
    0x803236F0: table.sym_fnc("osSetThreadPri", arg=(
        "OSThread *t",
        "OSPri pri",
    ), flag=table.GLOBL),

    # ultra/src/initialize.S
    0x803237D0: table.sym_fnc("osInitialize", flag=table.GLOBL),

    # ultra/src/viswapbuf.S
    0x80323A00: table.sym_fnc("osViSwapBuffer", arg=(
        "void *vaddr",
    ), flag=table.GLOBL),

    # ultra/src/sqrtf.S
    0x80323A50: table.sym_fnc("sqrtf", "float", arg=(
        "float value",
    ), flag=table.GLOBL),

    # ultra/src/contreaddata.S
    0x80323A60: table.sym_fnc("osContStartReadData", "s32", (
        "OSMesgQueue *mq",
    ), table.GLOBL),
    0x80323B24: table.sym_fnc("osContGetReadData", arg=(
        "OSContPad *pad",
    ), flag=table.GLOBL),
    0x80323BCC: table.sym("__osPackReadData"),

    # ultra/src/controller.S
    0x80323CC0: table.sym_fnc("osContInit", "s32", (
        "OSMesgQueue *mq",
        "u8 *bitpattern",
        "OSContStatus *status",
    ), table.GLOBL),
    0x80323EBC: table.sym("__osContGetInitData"),
    0x80323F8C: table.sym("__osPackRequestData"),

    # ultra/src/conteepprobe.S
    0x80324080: table.sym_fnc("osEepromProbe", "s32", (
        "OSMesgQueue *mq",
    ), table.GLOBL),

    # ultra/src/ll.S
    0x803240F0: table.sym("__ull_rshift", table.GLOBL), # unused
    0x8032411C: table.sym("__ull_rem", table.GLOBL),
    0x80324158: table.sym("__ull_div", table.GLOBL),
    0x80324194: table.sym("__ll_lshift", table.GLOBL),
    0x803241C0: table.sym("__ll_rem", table.GLOBL), # unused
    0x803241FC: table.sym("__ll_div", table.GLOBL),
    0x80324258: table.sym("__ll_mul", table.GLOBL),
    0x80324288: table.sym("__ull_divremi", table.GLOBL), # unused
    0x803242E8: table.sym("__ll_mod", table.GLOBL), # unused
    0x80324384: table.sym("__ll_rshift", table.GLOBL), # unused

    # ultra/src/invaldcache.S
    0x803243B0: table.sym_fnc("osInvalDCache", arg=(
        "void *vaddr",
        "s32 nbytes",
    ), flag=table.GLOBL),

    # ultra/src/pidma.S
    0x80324460: table.sym_fnc("osPiStartDma", arg=(
        "OSIoMesg *mb",
        "s32 priority",
        "s32 direction",
        "u32 devAddr",
        "void *vAddr",
        "u32 nbytes",
        "OSMesgQueue *mq",
    ), flag=table.GLOBL),

    # ultra/src/bzero.S
    0x80324570: table.sym_fnc("bzero", arg=(
        "void *",
        "size_t",
    ), flag=table.GLOBL),

    # ultra/src/invalicache.S
    0x80324610: table.sym_fnc("osInvalICache", arg=(
        "void *vaddr",
        "s32 nbytes",
    ), flag=table.GLOBL),

    # ultra/src/conteeplongread.S
    0x80324690: table.sym_fnc("osEepromLongRead", arg=(
        "OSMesgQueue *mq",
        "u8 address",
        "u8 *buffer",
        "s32 nbytes",
    ), flag=table.GLOBL),

    # ultra/src/conteeplongwrite.S
    0x803247D0: table.sym_fnc("osEepromLongWrite", arg=(
        "OSMesgQueue *mq",
        "u8 address",
        "u8 *buffer",
        "s32 nbytes",
    ), flag=table.GLOBL),

    # ultra/src/bcopy.S
    0x80324910: table.sym_fnc("bcopy", arg=(
        "const void *",
        "void *",
        "size_t",
    ), flag=table.GLOBL),

    # ultra/src/ortho.S
    0x80324C20: table.sym_fnc("guOrthoF", arg=(
        "float mf[4][4]",
        "float l",
        "float r",
        "float b",
        "float t",
        "float n",
        "float f",
        "float scale",
    ), flag=table.GLOBL),
    0x80324D74: table.sym_fnc("guOrtho", arg=(
        "Mtx *m",
        "float l",
        "float r",
        "float b",
        "float t",
        "float n",
        "float f",
        "float scale",
    ), flag=table.GLOBL),

    # ultra/src/perspective.S
    0x80324DE0: table.sym_fnc("guPerspectiveF", arg=(
        "float mf[4][4]",
        "u16 *perspNorm",
        "float fovy",
        "float aspect",
        "float near",
        "float far",
        "float scale",
    ), flag=table.GLOBL),
    0x80325010: table.sym_fnc("guPerspective", arg=(
        "Mtx *m",
        "u16 *perspNorm",
        "float fovy",
        "float aspect",
        "float near",
        "float far",
        "float scale",
    ), flag=table.GLOBL),

    # ultra/src/gettime.S
    0x80325070: table.sym_fnc("osGetTime", "OSTime", flag=table.GLOBL),

    # ultra/src/llcvt.S
    0x80325100: table.sym("__d_to_ll", table.GLOBL), # unused
    0x8032511C: table.sym("__f_to_ll", table.GLOBL), # unused
    0x80325138: table.sym("__d_to_ull", table.GLOBL),
    0x803251D8: table.sym("__f_to_ull", table.GLOBL), # unused
    0x80325274: table.sym("__ll_to_d", table.GLOBL), # unused
    0x8032528C: table.sym("__ll_to_f", table.GLOBL), # unused
    0x803252A4: table.sym("__ull_to_d", table.GLOBL),
    0x803252D8: table.sym("__ull_to_f", table.GLOBL), # unused

    # ultra/src/cosf.S
    0x80325310: table.sym_fnc("cosf", "float", (
        "float angle",
    ), table.GLOBL),

    # ultra/src/sinf.S
    0x80325480: table.sym_fnc("sinf", "float", (
        "float angle",
    ), table.GLOBL),

    # ultra/src/translate.S
    0x80325640: table.sym_fnc("guTranslateF", arg=(
        "float mf[4][4]",
        "float x",
        "float y",
        "float z",
    ), flag=table.GLOBL), # unused
    0x80325688: table.sym_fnc("guTranslate", arg=(
        "Mtx *m",
        "float x",
        "float y",
        "float z",
    ), flag=table.GLOBL),

    # ultra/src/rotate.S
    0x803256E0: table.sym_fnc("guRotateF", arg=(
        "float mf[4][4]",
        "float a",
        "float x",
        "float y",
        "float z",
    ), flag=table.GLOBL),
    0x80325874: table.sym_fnc("guRotate", arg=(
        "Mtx *m",
        "float a",
        "float x",
        "float y",
        "float z",
    ), flag=table.GLOBL),

    # ultra/src/scale.S
    0x803258D0: table.sym_fnc("guScaleF", arg=(
        "float mf[4][4]",
        "float x",
        "float y",
        "float z",
    ), flag=table.GLOBL),
    0x80325924: table.sym_fnc("guScale", arg=(
        "Mtx *m",
        "float x",
        "float y",
        "float z",
    ), flag=table.GLOBL),

    # ultra/src/aisetfreq.S
    0x80325970: table.sym_fnc("osAiSetFrequency", arg=(
        "u32 frequency",
    ), flag=table.GLOBL),

    # ultra/src/bnkf.S
    0x80325AD0: table.sym("_bnkfPatchBank"), # unused
    0x80325AD8: table.sym("_bnkfPatchInst"), # unused
    0x80325AE0: table.sym("_bnkfPatchSound"),
    0x80325BD4: table.sym("alBnkfNew", table.GLOBL), # unused
    0x80325BCC: table.sym("_bnkfPatchWaveTable"), # unused
    0x80325CD8: table.sym_fnc("alSeqFileNew", arg=(
        "ALSeqFile *file",
        "u8 *base",
    ), flag=table.GLOBL),

    # ultra/src/writebackdcache.S
    0x80325D20: table.sym_fnc("osWritebackDCache", arg=(
        "void *vaddr",
        "s32 nbytes",
    ), flag=table.GLOBL),

    # ultra/src/aigetlen.S
    0x80325DA0: table.sym_fnc("osAiGetLength", "u32", flag=table.GLOBL),

    # ultra/src/aisetnextbuf.S
    0x80325DB0: table.sym_fnc("osAiSetNextBuffer", "s32", (
        "void *vaddr",
        "u32 nbytes",
    ), table.GLOBL),

    # ultra/src/timerintr.S
    0x80325E60: table.sym("__osTimerServicesInit", table.GLOBL),
    0x80325EEC: table.sym("__osTimerInterrupt", table.GLOBL),
    0x80326064: table.sym("__osSetTimerIntr", table.GLOBL),
    0x803260D8: table.sym("__osInsertTimer", table.GLOBL),

    # ultra/src/xprintf.o
    0x80326260: table.sym("_Printf", table.GLOBL),
    0x80326A8C: table.sym("_Putfld"),
    0x80326B40: table.sym_fnc("L80326B40", flag=table.GLOBL|table.LOCAL),
    0x80326B90: table.sym_fnc("L80326B90", flag=table.GLOBL|table.LOCAL),
    0x80326D90: table.sym_fnc("L80326D90", flag=table.GLOBL|table.LOCAL),
    0x80326F74: table.sym_fnc("L80326F74", flag=table.GLOBL|table.LOCAL),
    0x8032717C: table.sym_fnc("L8032717C", flag=table.GLOBL|table.LOCAL),
    0x803272A4: table.sym_fnc("L803272A4", flag=table.GLOBL|table.LOCAL),
    0x80327308: table.sym_fnc("L80327308", flag=table.GLOBL|table.LOCAL),
    0x803273A0: table.sym_fnc("L803273A0", flag=table.GLOBL|table.LOCAL),

    # ultra/src/string.S
    0x803273F0: table.sym_fnc("memcpy", "void *", (
        "void *",
        "const void *",
        "size_t",
    ), table.GLOBL),
    0x8032741C: table.sym_fnc("strlen", "size_t", (
        "const char *",
    ), table.GLOBL),
    0x80327444: table.sym_fnc("strchr", "const char *", (
        "const char *",
        "int",
    ), table.GLOBL),

    # ultra/src/thread.S
    0x80327490: table.sym("__osDequeueThread", table.GLOBL),

    # ultra/src/interrupt.S
    0x803274D0: table.sym("__osDisableInt", table.GLOBL),
    0x803274F0: table.sym("__osRestoreInt", table.GLOBL),

    # ultra/src/vi.S
    0x80327510: table.sym("__osViInit", table.GLOBL),

    # ultra/src/exceptasm.S
    0x80327640: table.sym("__osExceptionPreamble", table.GLOBL),
    0x80327650: table.sym("__osException"),
    0x803276B4: table.sym("notIP7", table.LOCAL),
    0x803276D0: table.sym("savecontext", table.LOCAL),
    0x80327834: table.sym("no_kdebug", table.LOCAL),
    0x80327880: table.sym("no_rdb_mesg", table.LOCAL),
    0x803278A8: table.sym("handle_interrupt"),
    0x803278AC: table.sym("next_interrupt", table.LOCAL),
    0x803278E4: table.sym("counter"),
    0x80327904: table.sym("cart"),
    0x80327938: table.sym("rcp"),
    0x80327988: table.sym("sp_other_break", table.LOCAL),
    0x80327998: table.sym("vi", table.LOCAL),
    0x803279BC: table.sym("ai", table.LOCAL),
    0x803279E8: table.sym("si", table.LOCAL),
    0x80327A0C: table.sym("pi", table.LOCAL),
    0x80327A38: table.sym("dp", table.LOCAL),
    0x80327A5C: table.sym("NoMoreRcpInts", table.LOCAL),
    0x80327A68: table.sym("prenmi"),
    0x80327A94: table.sym("firstnmi", table.LOCAL),
    0x80327AC4: table.sym("sw2"),
    0x80327AE4: table.sym("sw1"),
    0x80327B04: table.sym("handle_break"),
    0x80327B1C: table.sym("redispatch"),
    0x80327B50: table.sym("enqueueRunning", table.LOCAL),
    0x80327B68: table.sym("panic"),
    0x80327B98: table.sym("send_mesg"),
    0x80327C44: table.sym("send_done", table.LOCAL),
    0x80327C4C: table.sym("handle_CpU"),
    0x80327C80: table.sym("__osEnqueueAndYield", table.GLOBL),
    0x80327D08: table.sym("noEnqueue", table.LOCAL),
    0x80327D10: table.sym("__osEnqueueThread", table.GLOBL),
    0x80327D58: table.sym("__osPopThread", table.GLOBL),
    0x80327D68: table.sym("__osDispatchThread", table.GLOBL),
    0x80327D88: table.sym("__osDispatchThreadSave", table.LOCAL),
    0x80327EA8: table.sym("__osCleanupThread", table.GLOBL),

    # ultra/src/virtualtophysical.S
    0x80327EB0: table.sym_fnc("osVirtualToPhysical", "u32", (
        "void *vaddr",
    ), table.GLOBL),

    # ultra/src/spsetstat.S
    0x80327F30: table.sym("__osSpSetStatus", table.GLOBL),

    # ultra/src/spsetpc.S
    0x80327F40: table.sym("__osSpSetPc", table.GLOBL),

    # ultra/src/sprawdma.S
    0x80327F80: table.sym("__osSpRawStartDma", table.GLOBL),

    # ultra/src/sp.S
    0x80328010: table.sym("__osSpDeviceBusy", table.GLOBL),

    # ultra/src/spgetstat.S
    0x80328040: table.sym("__osSpGetStatus", table.GLOBL),

    # ultra/src/getthreadpri.S
    0x80328050: table.sym_fnc("osGetThreadPri", "OSPri", (
        "OSThread *t",
    ), table.GLOBL),

    # ultra/src/vigetcurrcontext.S
    0x80328070: table.sym("__osViGetCurrentContext", table.GLOBL),

    # ultra/src/viswapcontext.S
    0x80328080: table.sym("__osViSwapContext", table.GLOBL),

    # ultra/src/getcount.S
    0x803283E0: table.sym_fnc("osGetCount", "u32", flag=table.GLOBL),

    # ultra/src/piacs.S
    0x803283F0: table.sym("__osPiCreateAccessQueue", table.GLOBL),
    0x80328440: table.sym("__osPiGetAccess"), # unused
    0x80328484: table.sym("__osPiRelAccess"), # unused

    # ultra/src/pirawdma.S
    0x803284B0: table.sym("osPiRawStartDma", table.GLOBL),

    # ultra/src/devmgr.S
    0x80328590: table.sym("__osDevMgrMain", table.GLOBL),

    # ultra/src/setsr.S
    0x80328710: table.sym_fnc("__osSetSR", arg=(
        "u32 value",
    ), flag=table.GLOBL),

    # ultra/src/getsr.S
    0x80328720: table.sym_fnc("__osGetSR", "u32", flag=table.GLOBL),

    # ultra/src/setfpccsr.S
    0x80328730: table.sym_fnc("__osSetFpcCsr", "u32", (
        "u32 value",
    ), table.GLOBL),

    # ultra/src/sirawread.S
    0x80328740: table.sym("__osSiRawReadIo", table.GLOBL),

    # ultra/src/sirawwrite.S
    0x80328790: table.sym("__osSiRawWriteIo", table.GLOBL),

    # ultra/src/maptlbrdb.S
    0x803287E0: table.sym_fnc("osMapTLBRdb", flag=table.GLOBL),

    # ultra/src/pirawread.S
    0x80328840: table.sym_fnc("osPiRawReadIo", "s32", (
        "u32 devAddr",
        "u32 *data",
    ), table.GLOBL),

    # ultra/src/siacs.S
    0x803288A0: table.sym("__osSiCreateAccessQueue", table.GLOBL),
    0x803288F0: table.sym("__osSiGetAccess", table.GLOBL),
    0x80328934: table.sym("__osSiRelAccess", table.GLOBL),

    # ultra/src/sirawdma.S
    0x80328960: table.sym("__osSiRawStartDma", table.GLOBL),

    # ultra/src/settimer.S
    0x80328A10: table.sym_fnc("osSetTimer", arg=(
        "OSTimer *timer",
        "OSTime countdown",
        "OSTime interval",
        "OSMesgQueue *mq",
        "OSMesg msg",
    ), flag=table.GLOBL),

    # ultra/src/conteepwrite.S
    0x80328AF0: table.sym_fnc("osEepromWrite", arg=(
        "OSMesgQueue *mq",
        "u8 address",
        "u8 *buffer",
    ), flag=table.GLOBL),
    0x80328CA0: table.sym("__osPackEepWriteData"),
    0x80328DAC: table.sym("__osEepStatus", table.GLOBL),

    # ultra/src/jammesg.S
    0x80328FD0: table.sym_fnc("osJamMesg", arg=(
        "OSMesgQueue *mq",
        "OSMesg msg",
        "s32 flag",
    ), flag=table.GLOBL),

    # ultra/src/pigetcmdq.S
    0x80329120: table.sym_fnc("osPiGetCmdQueue", "OSMesgQueue *",
    flag=table.GLOBL),

    # ultra/src/conteepread.S
    0x80329150: table.sym_fnc("osEepromRead", arg=(
        "OSMesgQueue *mq",
        "u8 address",
        "u8 *buffer",
    ), flag=table.GLOBL),
    0x80329340: table.sym("__osPackEepReadData"),

    # ultra/src/mtx.S
    0x80329450: table.sym_fnc("guMtxF2L", arg=(
        "float mf[4][4]",
        "Mtx *m",
    ), flag=table.GLOBL),
    0x80329550: table.sym_fnc("guMtxIdentF", arg=(
        "float mf[4][4]",
    ), flag=table.GLOBL),
    0x803295D8: table.sym_fnc("guMtxIdent", arg=(
        "Mtx *m",
    ), flag=table.GLOBL), # unused
    0x80329608: table.sym_fnc("guMtxL2F", arg=(
        "float mf[4][4]",
        "Mtx *m",
    ), flag=table.GLOBL), # unused

    # ultra/src/normalize.S
    0x803296C0: table.sym_fnc("guNormalize", arg=(
        "float *x",
        "float *y",
        "float *z",
    ), flag=table.GLOBL),

    # ultra/src/ai.S
    0x80329750: table.sym("__osAiDeviceBusy", table.GLOBL),

    # ultra/src/setcompare.S
    0x80329780: table.sym_fnc("__osSetCompare", arg=(
        "u32 value",
    ), flag=table.GLOBL),

    # ultra/src/xlitob.S
    0x80329790: table.sym("_Litob", table.GLOBL),

    # ultra/src/xldtob.S
    0x80329A90: table.sym("_Ldtob", table.GLOBL),
    0x8032A090: table.sym("_Ldunscale"),
    0x8032A170: table.sym("_Genld"),

    # ultra/src/kdebugserver.S
    0x8032A860: table.sym("u32_to_string"), # unused
    0x8032A890: table.sym("string_to_u32"),
    0x8032A8E8: table.sym("send_packet"),
    0x8032A9A8: table.sym("send"),
    0x8032AA80: table.sym("process_command_memory"),
    0x8032AACC: table.sym("process_command_register"),
    0x8032AAF8: table.sym("kdebugserver", table.GLOBL),

    # ultra/src/syncputchars.S
    0x8032ACE0: table.sym("__osSyncPutChars", table.GLOBL), # unused

    # ultra/src/setintmask.S
    0x8032AE10: table.sym_fnc("osSetIntMask", "OSIntMask", (
        "OSIntMask im",
    ), table.GLOBL), # unused

    # ultra/src/destroythread.S
    0x8032AE70: table.sym_fnc("osDestroyThread", arg=(
        "OSThread *t",
    ), flag=table.GLOBL),

    # ultra/src/probetlb.S
    0x8032AF70: table.sym("__osProbeTLB", table.GLOBL),

    # ultra/src/si.S
    0x8032B030: table.sym("__osSiDeviceBusy", table.GLOBL),

    # ultra/src/ldiv.S
    0x8032B060: table.sym("lldiv", table.GLOBL),
    0x8032B160: table.sym("ldiv", table.GLOBL),

    # ultra/src/getcause.S
    0x8032B1F0: table.sym_fnc("__osGetCause", "u32", flag=table.GLOBL),

    # ultra/src/atomic.S
    0x8032B200: table.sym("__osAtomicDec", table.GLOBL),

    0x803358D0: table.sym("__osViDevMgr+0x00"),
    0x803358D4: table.sym("__osViDevMgr+0x04"),
    0x803358D8: table.sym("__osViDevMgr+0x08"),
    0x803358DC: table.sym("__osViDevMgr+0x0C"),
    0x803358E0: table.sym("__osViDevMgr+0x10"),
    0x803358E4: table.sym("__osViDevMgr+0x14"),

    0x803358F0: table.sym("__osPiDevMgr+0x00"),
    0x803358F4: table.sym("__osPiDevMgr+0x04"),
    0x803358F8: table.sym("__osPiDevMgr+0x08"),
    0x803358FC: table.sym("__osPiDevMgr+0x0C"),
    0x80335900: table.sym("__osPiDevMgr+0x10"),
    0x80335904: table.sym("__osPiDevMgr+0x14"),

    0x80335910: table.sym("osClockRate+0"),
    0x80335914: table.sym("osClockRate+4"),

    0x80365E40: table.sym("viRetraceMsg+0"),
    0x80365E42: table.sym("viRetraceMsg+2"),
    0x80365E44: table.sym("viRetraceMsg+4"),

    0x80365E58: table.sym("viCounterMsg+0"),
    0x80365E5A: table.sym("viCounterMsg+2"),
    0x80365E5C: table.sym("viCounterMsg+4"),

    0x8036708C: table.sym("__osContPifRam+0x3C"),

    0x80367110: table.sym("__osCurrentTime+0"),
    0x80367114: table.sym("__osCurrentTime+4"),

    0x803671AC: table.sym("__osEepPifRam+0x3C"),
}

sym_E0_d_ultra = {
    # ==========================================================================
    # data
    # ==========================================================================

    # ultra/src/vitbl.c
    0x80335010: table.sym_var("osViModeTable",  "OSViMode", "[]"),

    # ultra/src/vimgr.c
    0x803358D0: table.sym_var("__osViDevMgr",   "OSDevMgr"),

    # ultra/src/pimgr.c
    0x803358F0: table.sym_var("__osPiDevMgr",   "OSDevMgr"),

    # ultra/src/initialize.c
    0x80335910: table.sym_var("osClockRate",    "u64"),
    0x80335918: table.sym_var("__osShutdown",   "u32",  flag=ultra.DALIGN),

    # ultra/src/controller.c
    0x80335920: table.sym_var("__osContinitialized",    "u32",  flag=ultra.DALIGN),

    # ultra/src/aisetnextbuf.c
    0x80335930: table.sym_var("hdwrBugFlag",    "u8",   flag=ultra.DALIGN),

    # ultra/src/timerintr.c
    0x80335940: table.sym_var("__osTimerList",  "OSTimer *",    flag=ultra.DALIGN),

    # ultra/src/xprintf.c
    0x80335950: table.sym_var("spaces", "char", "[]"),
    0x80335974: table.sym_var("zeroes", "char", "[]"),

    # ultra/src/thread.c
    0x803359A0: table.sym_var("__osThreadTail",     "__OSThreadTail"),
    0x803359A8: table.sym_var("__osRunQueue",       "OSThread *",  flag=ultra.DALIGN),
    0x803359AC: table.sym_var("__osActiveQueue",    "OSThread *",  flag=ultra.DALIGN),
    0x803359B0: table.sym_var("__osRunningThread",  "OSThread *",  flag=ultra.DALIGN),
    0x803359B4: table.sym_var("__osFaultedThread",  "OSThread *",  flag=ultra.DALIGN),

    # ultra/src/vi.c
    0x803359C0: table.sym_var("vi", "__OSViContext",  "[2]"),
    0x80335A20: table.sym_var("__osViCurr", "__OSViContext *",  flag=ultra.DALIGN),
    0x80335A24: table.sym_var("__osViNext", "__OSViContext *",  flag=ultra.DALIGN),
    0x80335A28: table.sym_var("osViNtscEnabled",    "u32",  flag=ultra.DALIGN),
    0x80335A2C: table.sym_var("osViClock",  "u32",  flag=ultra.DALIGN),

    # ultra/src/exceptasm.S
    0x80335A30: table.sym("__osHwIntTable"),
    0x80335A44: table.sym("__osIsRdbWrite"),
    0x80335A48: table.sym("__osIsRdbRead"),

    # ultra/src/piacs.c
    0x80335A50: table.sym_var("__osPiAccessQueueEnabled",   "u32",  flag=ultra.DALIGN),

    # ultra/src/siacs.c
    0x80335A60: table.sym_var("__osSiAccessQueueEnabled",   "u32",  flag=ultra.DALIGN),

    # ultra/src/xlitob.c
    0x80335A70: table.sym_var("ldigs",  "char", "[]"),
    0x80335A84: table.sym_var("udigs",  "char", "[]"),

    # ultra/src/vimodentsclan1.c
    0x80335AA0: table.sym_var("osViModeNtscLan1",   "OSViMode"),

    # ultra/src/vimodepallan1.c
    0x80335AF0: table.sym_var("osViModePalLan1",    "OSViMode"),

    # ultra/src/kdebugserver.c
    0x80335B40: table.sym_var("debug_state",        "u32",  flag=ultra.DALIGN),
    0x80335B44: table.sym_var("numChars",           "u32",  flag=ultra.DALIGN),
    0x80335B48: table.sym_var("numCharsToReceive",  "u32",  flag=ultra.DALIGN),

    # ultra/src/syncputchars.c
    0x80335B50: table.sym_var("__osRdbSendMessage", "u32",  flag=ultra.DALIGN),
    0x80335B54: table.sym_var("__osRdbWriteOK",     "u32",  flag=ultra.DALIGN),

    # ==========================================================================
    # rodata
    # ==========================================================================

    # ultra/src/perspective.c
    0x803397B0: table.sym_var("guPerspectiveF__803397B0", "const double"),

    # ultra/src/llcvt.c
    0x803397C0: table.sym_var("__d_to_ull__803397C0", "const u64"),
    0x803397C8: table.sym_var("__f_to_ull__803397C8", "const u64"),

    # ultra/src/cosf.c
    0x803397D0: table.sym_var("cosf__P",    "const double", "[]"),
    0x803397F8: table.sym_var("cosf__rpi",  "const double"),
    0x80339800: table.sym_var("cosf__pihi", "const double"),
    0x80339808: table.sym_var("cosf__pilo", "const double"),
    0x80339810: table.sym_var("cosf__zero", "const float"),

    # ultra/src/sinf.c
    0x80339820: table.sym_var("sinf__P",    "const double", "[]"),
    0x80339848: table.sym_var("sinf__rpi",  "const double"),
    0x80339850: table.sym_var("sinf__pihi", "const double"),
    0x80339858: table.sym_var("sinf__pilo", "const double"),
    0x80339860: table.sym_var("sinf__zero", "const float"),

    # ultra/src/rotate.c
    0x80339870: table.sym_var("guRotateF__80339870", "const float"),

    # ultra/src/xprintf.c
    0x80339880: table.sym_var("_Printf__80339880", "const char", "[]"),
    0x80339884: table.sym_var("fchar",  "const char", "[]"),
    0x8033988C: table.sym_var("fbit",   "const u32", "[]"),
    0x803398A4: table.sym_var_fnc("_Putfld__803398A4", "const", "[]"),

    # ultra/src/exceptasm.S
    0x80339980: table.sym("__osIntOffTable"),
    0x803399A0: table.sym("__osIntTable"),

    # ultra/src/libm_vals.S
    0x803399D0: table.sym("__libm_qnan_f",  table.GLOBL),

    # ultra/src/xldtob.c
    0x803399E0: table.sym_var("pows",   "const f64", "[]"),
    0x80339A28: table.sym_var("_Ldtob__80339A28", "const char", "[]"),
    0x80339A2C: table.sym_var("_Ldtob__80339A2C", "const char", "[]"),
    0x80339A30: table.sym_var("_Genld__80339A30", "const char", "[]"),
    0x80339A38: table.sym_var("_Ldtob__80339A38", "const double"),

    # ultra/src/setintmask.S
    0x80339A40: table.sym("__osRcpImTable", table.GLOBL),

    # ==========================================================================
    # bss
    # ==========================================================================

    # ultra/src/seteventmesg.c
    0x80364BA0: table.sym_var("__osEventStateTab",  "__OSEventState",   "[OS_NUM_EVENTS]",  ultra.BALIGN),

    # ultra/src/sptask.c
    0x80364C20: table.sym_var("tmp_task",   "OSTask",   flag=ultra.BALIGN),

    # ultra/src/vimgr.c
    0x80364C60: table.sym_var("viThread",       "OSThread", flag=ultra.BALIGN),
    0x80364E10: table.sym_var("viThreadStack",  "u64",  "[0x1000/sizeof(u64)]", ultra.BALIGN),
    0x80365E10: table.sym_var("viEventQueue",   "OSMesgQueue",  flag=ultra.BALIGN),
    0x80365E28: table.sym_var("viEventBuf",     "OSMesg",   "[5]",  ultra.BALIGN),
    0x80365E40: table.sym_var("viRetraceMsg",   "OSIoMesg", flag=ultra.BALIGN),
    0x80365E58: table.sym_var("viCounterMsg",   "OSIoMesg", flag=ultra.BALIGN),
    0x80365E6C: table.sym_var("viMgrMain__retrace", "u16"), # static

    # ultra/src/pimgr.c
    0x80365E70: table.sym_var("piThread",       "OSThread", flag=ultra.BALIGN),
    0x80366020: table.sym_var("piThreadStack",  "u64",  "[0x1000/sizeof(u64)]", ultra.BALIGN),
    0x80367020: table.sym_var("piEventQueue",   "OSMesgQueue",  flag=ultra.BALIGN),
    0x80367038: table.sym_var("piEventBuf",     "OSMesg",   "[1]",  ultra.BALIGN),

    # ultra/src/initialize.c
    0x80367040: table.sym_var("__osFinalrom",   "int"),

    # ultra/src/controller.c
    0x80367050: table.sym_var("__osContPifRam",     "u32",  "[0x40/sizeof(u32)]",   ultra.BALIGN),
    0x80367090: table.sym_var("__osContLastCmd",    "u8"),
    0x80367091: table.sym_var("__osMaxControllers", "u8"),
    0x80367098: table.sym_var("__osEepromTimer",    "OSTimer",  flag=ultra.BALIGN),
    0x803670B8: table.sym_var("__osEepromTimerQ",   "OSMesgQueue",  flag=ultra.BALIGN),
    0x803670D0: table.sym_var("__osEepromTimerMsg", "OSMesg",   "[1]",  ultra.BALIGN),

    # ultra/src/rotate.c
    0x803670E0: table.sym_var("guRotateF__dtor",    "float"), # static

    # ultra/src/timerintr.c
    0x803670F0: table.sym_var("__osBaseTimer",      "OSTimer",  flag=ultra.BALIGN),
    0x80367110: table.sym_var("__osCurrentTime",    "OSTime"),
    0x80367118: table.sym_var("__osBaseCounter",    "u32"),
    0x8036711C: table.sym_var("__osViIntrCount",    "u32"),
    0x80367120: table.sym_var("__osTimerCounter",   "u32"),

    # ultra/src/piacs.c
    0x80367130: table.sym_var("piAccessBuf",        "OSMesg",   "[1]",  ultra.BALIGN),
    0x80367138: table.sym_var("__osPiAccessQueue",  "OSMesgQueue",  flag=ultra.BALIGN),

    # ultra/src/siacs.c
    0x80367150: table.sym_var("siAccessBuf",        "OSMesg",   "[1]",  ultra.BALIGN),
    0x80367158: table.sym_var("__osSiAccessQueue",  "OSMesgQueue",  flag=ultra.BALIGN),

    # ultra/src/conteepread.c
    0x80367170: table.sym_var("__osEepPifRam",  "u32",  "[0x40/sizeof(u32)]",   ultra.BALIGN),

    # ultra/src/kdebugserver.c
    0x803671B0: table.sym_var("kdebugserver__buffer",   "u8",   "[0x100]",  ultra.BALIGN), # static
    0x803672B0: table.sym_var("__osThreadSave", "OSThread", flag=ultra.BALIGN),
}

sym_E0_t_spboot = {
    0x8032B260: table.sym("rspbootTextStart"),
    0x8032B330: table.sym("rspbootTextEnd"),

    0x0400100C: table.sym("boot"),
    0x04001024: table.sym("@@dmabusy", table.LOCAL),
    0x04001040: table.sym("yield_check"),
    0x04001054: table.sym("@@yield", table.LOCAL),
    0x04001068: table.sym("main"),
    0x04001090: table.sym("@@nodpwait", table.LOCAL),
    0x0400109C: table.sym("@@dmafull", table.LOCAL),
    0x040010B4: table.sym("@@dmabusy", table.LOCAL),
}

imm_E0_t_spboot = {
    0x04001000: ("%d",),
    0x04001008: ("os_task",),
    0x0400100C: (ultra.fmt_struct_OSTask,),
    0x04001010: (lambda x: "0x%04X-1" % (x+1 & 0xFFFF),),
    0x04001044: (ultra.fmt_sp_sr,),
    0x04001058: (ultra.fmt_sp_sw,),
    0x04001068: (ultra.fmt_struct_OSTask,),
    0x0400106C: (ultra.fmt_OSTask_flags,),
    0x04001084: (ultra.fmt_dpc_sr,),
    0x04001090: (ultra.fmt_struct_OSTask,),
    0x04001094: (ultra.fmt_struct_OSTask,),
    0x04001098: ("%d",),
}

sym_E0_t_gF3D_0 = {
    0x8032B330: table.sym("gspFast3D_fifoTextStart"),
    0x8032C738: table.sym("gspFast3D_fifoTextEnd"),

    0x04001000: table.sym("_04001000"),
    0x04001058: table.sym("cmd_next_sync"),
    0x04001060: table.sym(".cmd_proc", table.LOCAL),
    0x0400109C: table.sym(".cmd_nodma", table.LOCAL),
    0x040010A8: table.sym("cmd_next"),
    0x040010B8: table.sym("cmd_cont"),
    0x040010C8: table.sym("task_exit"),
    0x040010CC: table.sym(".task_yield", table.LOCAL),
    0x040010D4: table.sym("cmd_load"),
    0x040010F8: table.sym("prg_load"),
    0x040010FC: table.sym("prg_jump"),
    0x0400111C: table.sym("segment_to_physical"),
    0x0400113C: table.sym("dma_start"),
    0x0400115C: table.sym("@@write", table.LOCAL),
    0x04001164: table.sym("dma_sync"),
    0x04001178: table.sym("rdp_write"),
    0x04001198: table.sym("@@syncready", table.LOCAL),
    0x040011A4: table.sym("@@syncwrap", table.LOCAL),
    0x040011B8: table.sym("@@syncfit", table.LOCAL),
    0x040011D4: table.sym("@@write", table.LOCAL),
    0x040011F4: table.sym("@@end", table.LOCAL),
    0x040011FC: table.sym("case_IMM"),
    0x0400120C: table.sym("case_G_TRI1"),
    0x04001250: table.sym("case_G_POPMTX"),
    0x04001288: table.sym("case_G_MOVEWORD"),
    0x040012A0: table.sym("case_G_TEXTURE"),
    0x040012C4: table.sym("case_G_SETOTHERMODE_H"),
    0x040012CC: table.sym("case_G_SETOTHERMODE_L"),
    0x040012D0: table.sym(".setothermode", table.LOCAL),
    0x0400130C: table.sym("case_G_CULLDL"),
    0x04001314: table.sym("@@loop", table.LOCAL),
    0x04001328: table.sym("case_G_ENDDL"),
    0x04001348: table.sym("case_G_SETGEOMETRYMODE"),
    0x04001358: table.sym("case_G_CLEARGEOMETRYMODE"),
    0x04001370: table.sym("case_G_PERSPNORM"),
    0x04001378: table.sym("case_G_RDPHALF_1"),
    0x04001380: table.sym("case_G_RDPHALF_CONT"),
    0x04001384: table.sym("case_G_RDPHALF_2"),
    0x0400138C: table.sym("case_RDP"),
    0x040013A8: table.sym("rdp_cmd"),
    0x040013C4: table.sym("case_DMA"),
    0x040013DC: table.sym("case_G_MTX"),
    0x04001420: table.sym(".L04001420", table.LOCAL),
    0x04001438: table.sym(".L04001438", table.LOCAL),
    0x04001444: table.sym("_04001444"),
    0x04001484: table.sym("_04001484"),
    0x040014E8: table.sym("_040014E8"),
    0x04001510: table.sym("_04001510"),
    0x04001524: table.sym("_04001524"),
    0x04001558: table.sym("case_G_MOVEMEM"),
    0x04001568: table.sym("case_G_VTX"),
    0x040015E4: table.sym(".light_return", table.LOCAL),
    0x040015E8: table.sym(".vtx_clip_return", table.LOCAL),
    0x04001734: table.sym("case_G_DL"),
    0x04001754: table.sym("@@nopush", table.LOCAL),

    0x04001768: table.sym("@clip"),
    0x04001774: table.sym("@light"),

    0x04001780: table.sym("init"),
    0x040017E4: table.sym("@@initfifo", table.LOCAL),
    0x04001800: table.sym("@@noinitfifo", table.LOCAL),
    0x04001870: table.sym("@@fromyield", table.LOCAL),
    0x04001998: table.sym("rdp_tri"),
    0x040019C4: table.sym(".clip_return", table.LOCAL),
    0x04001A30: table.sym(".L04001A30", table.LOCAL),
}

sym_E0_t_gF3D_2 = {
    0x040010FC: table.sym("prg_jump"),
    0x040015E8: table.sym(".vtx_clip_return", table.LOCAL),
    0x04001768: table.sym("@clip"),
    0x04001774: table.sym("@light"),

    0x04001784: table.sym("clip"),
    0x040017A0: table.sym("ProcClipNext"),
    0x040017BC: table.sym("ProcClipI"),
    0x040017C0: table.sym("ProcClipO"),
    0x040017D4: table.sym(".L040017D4", table.LOCAL),
    0x04001818: table.sym("ProcClipFI"),
    0x0400182C: table.sym("ProcClipFO"),
    0x04001964: table.sym("ProcClipDraw"),
    0x04001804: table.sym(".L04001804_2", table.LOCAL),
    0x04001980: table.sym("_04001980"),

    0x040019C4: table.sym(".clip_return", table.LOCAL),
}

sym_E0_t_gF3D_3 = {
    0x040010FC: table.sym("prg_jump"),
    0x040015E4: table.sym(".light_return", table.LOCAL),
    0x04001768: table.sym("@clip"),
    0x04001774: table.sym("light"),

    0x04001804: table.sym(".L04001804_3", table.LOCAL),
}

sym_E0_t_gF3D_4 = {
    0x04001768: table.sym("@yield"),
    0x04001770: table.sym("exit"),
    0x04001788: table.sym("yield"),
}

imm_E0_t_gF3D_4 = {
    0x040017C8: (lambda x: "0x%04X" % (x & 0xFFFF),),
}

sym_E0_d_gF3D = {
    0x80339AC0: table.sym("gspFast3D_fifoDataStart"),
    0x8033A2C0: table.sym("gspFast3D_fifoDataEnd"),

    0x04001000: table.sym("prg_main_start"),
    0x04001080: table.sym("prg_init_start"),
    0x04001768: table.sym("prg_ext_start"),

    0x04001328: table.sym("case_G_ENDDL"),
    0x0400138C: table.sym("case_RDP"),
}

sym_E0_t_aMain = {
    0x8032C740: table.sym("aspMainTextStart"),
    0x8032D560: table.sym("aspMainTextEnd"),

    0x040010D4: table.sym(".cmd_proc", table.LOCAL),
    0x04001118: table.sym("cmd_next"),
    0x04001150: table.sym("cmd_load"),
    0x04001184: table.sym("dma_read"),
    0x040011B0: table.sym("dma_write"),
    0x040011DC: table.sym("case_A_CLEARBUFF"),
    0x04001214: table.sym("case_A_LOADBUFF"),
    0x04001254: table.sym("case_A_SAVEBUFF"),
    0x04001294: table.sym("case_A_LOADADPCM"),
    0x040012D0: table.sym("case_A_SEGMENT"),
    0x040012EC: table.sym("case_A_SETBUFF"),
    0x04001328: table.sym("case_A_SETVOL"),
    0x0400138C: table.sym("case_A_INTERLEAVE"),
    0x0400140C: table.sym("case_A_DMEMMOVE"),
    0x0400144C: table.sym("case_A_SETLOOP"),
    0x04001470: table.sym("case_A_ADPCM"),
    0x0400170C: table.sym("case_A_POLEF"),
    0x0400187C: table.sym("case_A_RESAMPLE"),
    0x040018E8: table.sym(".L040018E8", table.LOCAL),
    0x040019D8: table.sym(".L040019D8", table.LOCAL),
    0x04001B38: table.sym("case_A_ENVMIXER"),
    0x04001BB0: table.sym(".L04001BB0", table.LOCAL),
    0x04001C48: table.sym(".L04001C48", table.LOCAL),
    0x04001CB8: table.sym(".L04001CB8", table.LOCAL),
    0x04001D04: table.sym(".L04001D04", table.LOCAL),
    0x04001D50: table.sym(".L04001D50", table.LOCAL),
    0x04001DBC: table.sym(".L04001DBC", table.LOCAL),
    0x04001E24: table.sym("case_A_MIXER"),
}

sym_E0_d_aMain = {
    0x8033A2C0: table.sym("aspMainDataStart"),
    0x8033A580: table.sym("aspMainDataEnd"),

    0x04001328: table.sym("case_A_SETVOL"),
    0x0400138C: table.sym("case_A_INTERLEAVE"),
}

sym_E0_t_main = {
    # ==========================================================================
    # text
    # ==========================================================================

    # src/main.c
    0x80246050: table.sym_fnc("debug_update", flag=table.GLOBL), # unused
    0x80246170: table.sym_fnc("dummy"), # unused
    0x802461CC: table.sym_fnc("debug_main"),
    0x802461DC: table.sym_fnc("debug_sc_main"),
    0x802461EC: table.sym_fnc("debug_sc_vi"),
    0x802461FC: table.sym_fnc("sc_init"),
    0x802462E0: table.sym_fnc("sc_init_mem"),
    0x80246338: table.sym_fnc("thread_create", arg=(
        "OSThread *t",
        "OSId id",
        "void (*entry)(void *)",
        "void *arg",
        "void *sp",
        "OSPri pri",
    )),
    0x8024639C: table.sym_fnc("sc_event_prenmi"),
    0x802463EC: table.sym_fnc("sc_task_flush"),
    0x8024651C: table.sym_fnc("sc_task_start", arg=(
        "int type",
    )),
    0x8024659C: table.sym_fnc("sc_task_yield"),
    0x802465EC: table.sym_fnc("sc_event_gfxtask"),
    0x80246648: table.sym_fnc("sc_audtask_skip"),
    0x8024669C: table.sym_fnc("sc_event_vi"),
    0x802467FC: table.sym_fnc("sc_event_sp"),
    0x8024694C: table.sym_fnc("sc_event_dp"),
    0x802469B8: table.sym_fnc("sc_main", arg=(
        "unused void *arg",
    )),
    0x80246A9C: table.sym_fnc("L80246A9C", flag=table.GLOBL|table.LOCAL),
    0x80246AAC: table.sym_fnc("L80246AAC", flag=table.GLOBL|table.LOCAL),
    0x80246ABC: table.sym_fnc("L80246ABC", flag=table.GLOBL|table.LOCAL),
    0x80246ACC: table.sym_fnc("L80246ACC", flag=table.GLOBL|table.LOCAL),
    0x80246ADC: table.sym_fnc("L80246ADC", flag=table.GLOBL|table.LOCAL),
    0x80246B14: table.sym_fnc("sc_client_init", arg=(
        "int i",
        "SC_CLIENT *client",
        "OSMesgQueue *mq",
        "OSMesg msg",
    ), flag=table.GLOBL),
    0x80246B74: table.sym_fnc("sc_queue_task", arg=(
        "SC_TASK *task",
    ), flag=table.GLOBL), # unused
    0x80246BB4: table.sym_fnc("sc_queue_audtask", arg=(
        "SC_TASK *task",
    ), flag=table.GLOBL),
    0x80246C10: table.sym_fnc("sc_queue_gfxtask", arg=(
        "SC_TASK *task",
    ), flag=table.GLOBL),
    0x80246C9C: table.sym_fnc("sc_audio_enable",  flag=table.GLOBL), # unused
    0x80246CB8: table.sym_fnc("sc_audio_disable", flag=table.GLOBL), # unused
    0x80246CF0: table.sym_fnc("idle_main", arg=(
        "unused void *arg",
    )),
    0x80246DF8: table.sym_fnc("main", flag=table.GLOBL),

    # src/app.c
    0x80246E70: table.sym_fnc("video_init_dp"),
    0x802471A4: table.sym_fnc("video_init_sp"),
    0x80247284: table.sym_fnc("video_init_zimg"),
    0x802473C8: table.sym_fnc("video_init_cimg"),
    0x802474B8: table.sym_fnc("video_clear", arg=(
        "u32 fill",
    ), flag=table.GLOBL),
    0x80247620: table.sym_fnc("video_vp_clear", arg=(
        "const Vp *vp",
        "u32 fill",
    ), flag=table.GLOBL),
    0x8024784C: table.sym_fnc("video_draw_border"),
    0x802479BC: table.sym_fnc("video_vp_scissor", arg=(
        "const Vp *vp",
    ), flag=table.GLOBL),
    0x80247B3C: table.sym_fnc("video_init_task"),
    0x80247CCC: table.sym_fnc("video_draw_start", flag=table.GLOBL),
    0x80247D14: table.sym_fnc("video_draw_end", flag=table.GLOBL),
    0x80247DB4: table.sym_fnc("video_draw_reset"),
    0x80247F08: table.sym_fnc("video_init"),
    0x80247FDC: table.sym_fnc("video_start"),
    0x80248090: table.sym_fnc("video_end"),
    0x802481E0: table.sym_fnc("demo_record"), # unused
    0x80248304: table.sym_fnc("input_update_stick", arg=(
        "CONTROLLER *cont",
    )),
    0x80248498: table.sym_fnc("demo_update"),
    0x80248638: table.sym_fnc("input_update"),
    0x80248824: table.sym_fnc("input_init"),
    0x80248964: table.sym_fnc("app_init"),
    0x80248AF0: table.sym_fnc("app_main", arg=(
        "unused void *arg",
    ), flag=table.GLOBL),

    # src/audio.c
    0x80248C40: table.sym_fnc("audio_mute_reset", flag=table.GLOBL),
    0x80248C58: table.sym_fnc("audio_mute_start", arg=(
        "uint flag",
    ), flag=table.GLOBL),
    0x80248CE8: table.sym_fnc("audio_mute_end", arg=(
        "uint flag",
    ), flag=table.GLOBL),
    0x80248D78: table.sym_fnc("audio_se_lock",      flag=table.GLOBL),
    0x80248DC0: table.sym_fnc("audio_se_unlock",    flag=table.GLOBL),
    0x80248E08: table.sym_fnc("audio_output", arg=(
        "u16 type",
    ), flag=table.GLOBL),
    0x80248E54: table.sym_fnc("audio_face_sfx", arg=(
        "s16 flag",
    ), flag=table.GLOBL),
    0x80248FEC: table.sym_fnc("audio_se_ripple", flag=table.GLOBL),
    0x80249070: table.sym_fnc("bgm_endless", flag=table.GLOBL),
    0x80249178: table.sym_fnc("bgm_play", arg=(
        "u16 mode",
        "u16 bgm",
        "s16 fadein",
    ), flag=table.GLOBL),
    0x8024922C: table.sym_fnc("audio_fadeout", arg=(
        "s16 fadeout",
    ), flag=table.GLOBL),
    0x8024927C: table.sym_fnc("bgm_fadeout", arg=(
        "s16 fadeout",
    ), flag=table.GLOBL),
    0x802492D0: table.sym_fnc("bgm_stage_play", arg=(
        "u16 bgm",
    ), flag=table.GLOBL),
    0x80249310: table.sym_fnc("bgm_shell_play", flag=table.GLOBL),
    0x8024934C: table.sym_fnc("bgm_shell_stop", flag=table.GLOBL),
    0x80249398: table.sym_fnc("bgm_special_play", arg=(
        "u16 bgm",
    ), flag=table.GLOBL),
    0x80249404: table.sym_fnc("bgm_special_fadeout", flag=table.GLOBL),
    0x80249448: table.sym_fnc("bgm_special_stop", flag=table.GLOBL),
    0x80249494: table.sym_fnc("audio_env_se_play", arg=(
        "int se",
        "vecf pos",
    ), flag=table.GLOBL),
    0x802494D8: table.sym_fnc("audio_update", flag=table.GLOBL),
    0x80249500: table.sym_fnc("audio_main", arg=(
        "unused void *arg",
    ), flag=table.GLOBL),

    # src/game.c
    0x802495E0: table.sym("game_timer", table.GLOBL),
    0x802496B8: table.sym("game_ispause"),
    0x80249764: table.sym("game_state_set"),
    0x8024978C: table.sym("game_exit"),
    0x802497B8: table.sym("game_exit_fadeout", table.GLOBL),
    0x8024982C: table.sym("game_8024982C"), # unused
    0x8024983C: table.sym("game_8024983C", table.GLOBL), # init message
    0x8024995C: table.sym("game_8024995C"), # init move in front of door
    0x80249A10: table.sym("game_80249A10"), # init cap
    0x80249AB4: table.sym("game_80249AB4"), # init pl state
    0x80249AF4: table.sym_fnc("L80249AF4", flag=table.GLOBL|table.LOCAL),
    0x80249B0C: table.sym_fnc("L80249B0C", flag=table.GLOBL|table.LOCAL),
    0x80249B28: table.sym_fnc("L80249B28", flag=table.GLOBL|table.LOCAL),
    0x80249B40: table.sym_fnc("L80249B40", flag=table.GLOBL|table.LOCAL),
    0x80249B58: table.sym_fnc("L80249B58", flag=table.GLOBL|table.LOCAL),
    0x80249B74: table.sym_fnc("L80249B74", flag=table.GLOBL|table.LOCAL),
    0x80249B8C: table.sym_fnc("L80249B8C", flag=table.GLOBL|table.LOCAL),
    0x80249BA8: table.sym_fnc("L80249BA8", flag=table.GLOBL|table.LOCAL),
    0x80249BC0: table.sym_fnc("L80249BC0", flag=table.GLOBL|table.LOCAL),
    0x80249BD8: table.sym_fnc("L80249BD8", flag=table.GLOBL|table.LOCAL),
    0x80249BF0: table.sym_fnc("L80249BF0", flag=table.GLOBL|table.LOCAL),
    0x80249C0C: table.sym_fnc("L80249C0C", flag=table.GLOBL|table.LOCAL),
    0x80249C28: table.sym_fnc("L80249C28", flag=table.GLOBL|table.LOCAL),
    0x80249C40: table.sym_fnc("L80249C40", flag=table.GLOBL|table.LOCAL),
    0x80249C58: table.sym_fnc("L80249C58", flag=table.GLOBL|table.LOCAL),
    0x80249C70: table.sym_fnc("L80249C70", flag=table.GLOBL|table.LOCAL),
    0x80249C88: table.sym_fnc("L80249C88", flag=table.GLOBL|table.LOCAL),
    0x80249CA0: table.sym_fnc("L80249CA0", flag=table.GLOBL|table.LOCAL),
    0x80249CB8: table.sym_fnc("L80249CB8", flag=table.GLOBL|table.LOCAL),
    0x80249CD8: table.sym("game_80249CD8"), # init player
    0x80249EA4: table.sym_fnc("L80249EA4", flag=table.GLOBL|table.LOCAL),
    0x80249EC4: table.sym_fnc("L80249EC4", flag=table.GLOBL|table.LOCAL),
    0x80249EE4: table.sym_fnc("L80249EE4", flag=table.GLOBL|table.LOCAL),
    0x80249F08: table.sym_fnc("L80249F08", flag=table.GLOBL|table.LOCAL),
    0x80249F2C: table.sym_fnc("L80249F2C", flag=table.GLOBL|table.LOCAL),
    0x80249F4C: table.sym_fnc("L80249F4C", flag=table.GLOBL|table.LOCAL),
    0x80249F6C: table.sym_fnc("L80249F6C", flag=table.GLOBL|table.LOCAL),
    0x8024A124: table.sym("game_8024A124"), # init scene
    0x8024A18C: table.sym("game_8024A18C"), # init stage
    0x8024A1D8: table.sym("game_8024A1D8"), # init staff
    0x8024A374: table.sym("game_8024A374"), # update connect
    0x8024A584: table.sym("game_8024A584"), # is same bgm
    0x8024A700: table.sym("game_8024A700"), # link
    0x8024A7B4: table.sym("game_8024A7B4"), # get bglink
    0x8024A85C: table.sym("game_8024A85C"), # update bglink
    0x8024A9CC: table.sym("game_8024A9CC", table.GLOBL), # pl start fade
    0x8024AA44: table.sym_fnc("L8024AA44", flag=table.GLOBL|table.LOCAL),
    0x8024AA88: table.sym_fnc("L8024AA88", flag=table.GLOBL|table.LOCAL),
    0x8024AACC: table.sym_fnc("L8024AACC", flag=table.GLOBL|table.LOCAL),
    0x8024AB0C: table.sym_fnc("L8024AB0C", flag=table.GLOBL|table.LOCAL),
    0x8024AB74: table.sym_fnc("L8024AB74", flag=table.GLOBL|table.LOCAL),
    0x8024ABEC: table.sym_fnc("L8024ABEC", flag=table.GLOBL|table.LOCAL),
    0x8024AC3C: table.sym_fnc("L8024AC3C", flag=table.GLOBL|table.LOCAL),
    0x8024AC8C: table.sym_fnc("L8024AC8C", flag=table.GLOBL|table.LOCAL),
    0x8024ACF0: table.sym_fnc("L8024ACF0", flag=table.GLOBL|table.LOCAL),
    0x8024AD60: table.sym_fnc("L8024AD60", flag=table.GLOBL|table.LOCAL),
    0x8024ADC0: table.sym_fnc("L8024ADC0", flag=table.GLOBL|table.LOCAL),
    0x8024ADEC: table.sym_fnc("L8024ADEC", flag=table.GLOBL|table.LOCAL),
    0x8024AE60: table.sym_fnc("L8024AE60", flag=table.GLOBL|table.LOCAL),
    0x8024AEDC: table.sym("game_8024AEDC"), # update fade
    0x8024AFC4: table.sym_fnc("L8024AFC4", flag=table.GLOBL|table.LOCAL),
    0x8024AFDC: table.sym_fnc("L8024AFDC", flag=table.GLOBL|table.LOCAL),
    0x8024AFF8: table.sym_fnc("L8024AFF8", flag=table.GLOBL|table.LOCAL),
    0x8024B008: table.sym_fnc("L8024B008", flag=table.GLOBL|table.LOCAL),
    0x8024B03C: table.sym_fnc("L8024B03C", flag=table.GLOBL|table.LOCAL),
    0x8024B13C: table.sym("game_8024B13C"), # update hud
    0x8024B390: table.sym("game_8024B390"), # fade callback
    0x8024B3E4: table.sym("game_8024B3E4"), # state: normal
    0x8024B5D4: table.sym("game_8024B5D4"), # state: pause
    0x8024B6CC: table.sym("game_8024B6CC"), # state: frame advance
    0x8024B798: table.sym("game_8024B798", table.GLOBL),
    0x8024B7C0: table.sym("game_8024B7C0"), # state: fade
    0x8024B880: table.sym("game_8024B880"), # state: exit
    0x8024B940: table.sym("game_8024B940"), # unused / state: exit old
    0x8024B9B8: table.sym_fnc("game_update", "int"),
    0x8024B9EC: table.sym_fnc("L8024B9EC", flag=table.GLOBL|table.LOCAL),
    0x8024BA00: table.sym_fnc("L8024BA00", flag=table.GLOBL|table.LOCAL),
    0x8024BA14: table.sym_fnc("L8024BA14", flag=table.GLOBL|table.LOCAL),
    0x8024BA28: table.sym_fnc("L8024BA28", flag=table.GLOBL|table.LOCAL),
    0x8024BA3C: table.sym_fnc("L8024BA3C", flag=table.GLOBL|table.LOCAL),
    0x8024BA50: table.sym_fnc("L8024BA50", flag=table.GLOBL|table.LOCAL),
    0x8024BA8C: table.sym_fnc("game_init", "int"),
    0x8024BCD8: table.sym_fnc("p_game_main", "int", (
        "s16 arg",
        "int code",
    ), table.GLOBL), # p callback
    0x8024BD5C: table.sym_fnc("p_game_init", "int", (
        "s16 arg",
        "int code",
    ), table.GLOBL), # p callback
    0x8024BE14: table.sym_fnc("p_game_select", "int", (
        "s16 arg",
        "int code",
    ), table.GLOBL), # p callback
    0x8024BFA0: table.sym_fnc("p_ending_se", "int", (
        "s16 arg",
        "int code",
    ), table.GLOBL), # p callback

    # src/pl_collision.c
    0x8024BFF0: table.sym("pl_collision_8024BFF0"),
    0x8024C0B8: table.sym("pl_collision_8024C0B8"),
    0x8024C16C: table.sym("pl_collision_8024C16C", table.GLOBL),
    0x8024C1D8: table.sym("pl_collision_8024C1D8"),
    0x8024C51C: table.sym("pl_collision_8024C51C"),
    0x8024C590: table.sym_fnc("L8024C590", flag=table.GLOBL|table.LOCAL),
    0x8024C5A0: table.sym_fnc("L8024C5A0", flag=table.GLOBL|table.LOCAL),
    0x8024C5B0: table.sym_fnc("L8024C5B0", flag=table.GLOBL|table.LOCAL),
    0x8024C5C0: table.sym_fnc("L8024C5C0", flag=table.GLOBL|table.LOCAL),
    0x8024C5F0: table.sym_fnc("L8024C5F0", flag=table.GLOBL|table.LOCAL),
    0x8024C618: table.sym("pl_collision_8024C618", table.GLOBL),
    0x8024C66C: table.sym("pl_collision_8024C66C", table.GLOBL),
    0x8024C6C0: table.sym("pl_collision_8024C6C0", table.GLOBL),
    0x8024C780: table.sym("pl_collision_8024C780", table.GLOBL),
    0x8024C894: table.sym("pl_collision_8024C894", table.GLOBL),
    0x8024C8FC: table.sym("pl_collision_8024C8FC", table.GLOBL),
    0x8024C928: table.sym("pl_collision_8024C928", table.GLOBL),
    0x8024CA68: table.sym("pl_collision_8024CA68", table.GLOBL),
    0x8024CAF8: table.sym("pl_collision_8024CAF8", table.GLOBL),
    0x8024CB58: table.sym("pl_collision_8024CB58"),
    0x8024CBFC: table.sym("pl_collision_8024CBFC", table.GLOBL),
    0x8024CC7C: table.sym("pl_collision_8024CC7C", table.GLOBL),
    0x8024CE08: table.sym("pl_collision_8024CE08"),
    0x8024D0B4: table.sym("pl_collision_8024D0B4"),
    0x8024D130: table.sym("pl_collision_8024D130"),
    0x8024D16C: table.sym("pl_collision_8024D16C"), # unused
    0x8024D2BC: table.sym("pl_collision_8024D2BC"),
    0x8024D578: table.sym("pl_collision_8024D578"),
    0x8024D72C: table.sym("pl_collision_8024D72C"),
    0x8024D804: table.sym("pl_collision_8024D804"),
    0x8024D8B0: table.sym("pl_collision_8024D8B0"),
    0x8024D998: table.sym("pl_collision_8024D998"),
    0x8024DAAC: table.sym("pl_collision_8024DAAC"),
    0x8024DB2C: table.sym_fnc("pl_collision_8024DB2C", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024DBF0: table.sym_fnc("pl_collision_8024DBF0", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024DC28: table.sym_fnc("pl_collision_8024DC28", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024DE4C: table.sym_fnc("pl_collision_8024DE4C", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024DF10: table.sym_fnc("pl_collision_8024DF10", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024E0C4: table.sym_fnc("pl_collision_8024E0C4", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024E2FC: table.sym("pl_collision_8024E2FC", table.GLOBL),
    0x8024E388: table.sym_fnc("L8024E388", flag=table.GLOBL|table.LOCAL),
    0x8024E3B0: table.sym_fnc("L8024E3B0", flag=table.GLOBL|table.LOCAL),
    0x8024E3D8: table.sym_fnc("L8024E3D8", flag=table.GLOBL|table.LOCAL),
    0x8024E3E8: table.sym_fnc("L8024E3E8", flag=table.GLOBL|table.LOCAL),
    0x8024E3F8: table.sym_fnc("L8024E3F8", flag=table.GLOBL|table.LOCAL),
    0x8024E408: table.sym_fnc("L8024E408", flag=table.GLOBL|table.LOCAL),
    0x8024E420: table.sym_fnc("pl_collision_8024E420", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024E5A4: table.sym_fnc("L8024E5A4", flag=table.GLOBL|table.LOCAL),
    0x8024E5B4: table.sym_fnc("L8024E5B4", flag=table.GLOBL|table.LOCAL),
    0x8024E5C4: table.sym_fnc("L8024E5C4", flag=table.GLOBL|table.LOCAL),
    0x8024E5D4: table.sym_fnc("L8024E5D4", flag=table.GLOBL|table.LOCAL),
    0x8024E5E4: table.sym_fnc("L8024E5E4", flag=table.GLOBL|table.LOCAL),
    0x8024E5F4: table.sym_fnc("L8024E5F4", flag=table.GLOBL|table.LOCAL),
    0x8024E604: table.sym_fnc("L8024E604", flag=table.GLOBL|table.LOCAL),
    0x8024E6EC: table.sym_fnc("pl_collision_8024E6EC", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024E778: table.sym_fnc("pl_collision_8024E778", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024E7D4: table.sym_fnc("pl_collision_8024E7D4", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024E8F0: table.sym_fnc("pl_collision_8024E8F0", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024E9D0: table.sym_fnc("pl_collision_8024E9D0", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024EAD8: table.sym_fnc("pl_collision_8024EAD8", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024EC54: table.sym_fnc("pl_collision_8024EC54", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024ED84: table.sym_fnc("pl_collision_8024ED84", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024EE44: table.sym_fnc("pl_collision_8024EE44", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024EFF8: table.sym_fnc("pl_collision_8024EFF8", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024F134: table.sym("pl_collision_8024F134"), # unused
    0x8024F170: table.sym_fnc("pl_collision_8024F170", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024F1E0: table.sym_fnc("pl_collision_8024F1E0", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024F354: table.sym_fnc("pl_collision_8024F354", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024F4AC: table.sym_fnc("pl_collision_8024F4AC", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024F55C: table.sym_fnc("pl_collision_8024F55C", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024F5CC: table.sym_fnc("pl_collision_8024F5CC", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024F6A4: table.sym_fnc("pl_collision_8024F6A4", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024F7A8: table.sym("pl_collision_8024F7A8"),
    0x8024F8BC: table.sym_fnc("pl_collision_8024F8BC", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024FA60: table.sym_fnc("pl_collision_8024FA60", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024FB30: table.sym_fnc("pl_collision_8024FB30", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024FD2C: table.sym_fnc("pl_collision_8024FD2C", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x8024FE6C: table.sym("pl_collision_8024FE6C"),
    0x8024FF04: table.sym("pl_collision_8024FF04"),
    0x80250098: table.sym("pl_collision_80250098"),
    0x80250198: table.sym_fnc("pl_collision_80250198", "int", (
        "struct player *pl",
        "u32 flag",
        "struct object *obj",
    ), table.GLOBL), # data
    0x80250230: table.sym("pl_collision_80250230"),
    0x802503F0: table.sym("pl_collision_802503F0", table.GLOBL),
    0x802505C8: table.sym("pl_collision_802505C8"),
    0x8025065C: table.sym("pl_collision_8025065C"),
    0x80250724: table.sym("pl_collision_80250724"),
    0x80250778: table.sym("pl_collision_80250778"),
    0x802507FC: table.sym("pl_collision_802507FC", table.GLOBL),

    # src/player.c
    0x80250940: table.sym("player_80250940", table.GLOBL),
    0x8025097C: table.sym("player_8025097C", table.GLOBL),
    0x802509B8: table.sym("player_802509B8", table.GLOBL),
    0x80250B04: table.sym("player_80250B04", table.GLOBL),
    0x80250C7C: table.sym("player_80250C7C", table.GLOBL),
    0x80250D38: table.sym("player_80250D38", table.GLOBL),
    0x80250E54: table.sym("player_80250E54", table.GLOBL),
    0x80251020: table.sym("player_80251020", table.GLOBL),
    0x802510DC: table.sym("player_802510DC", table.GLOBL),
    0x80251120: table.sym("player_80251120", table.GLOBL),
    0x8025118C: table.sym("player_8025118C", table.GLOBL),
    0x80251274: table.sym("player_80251274", table.GLOBL),
    0x80251310: table.sym("player_80251310", table.GLOBL),
    0x80251444: table.sym("player_80251444", table.GLOBL),
    0x802514AC: table.sym("player_802514AC", table.GLOBL),
    0x80251510: table.sym("player_80251510", table.GLOBL),
    0x80251574: table.sym("player_80251574", table.GLOBL),
    0x802515D8: table.sym("player_802515D8", table.GLOBL),
    0x8025163C: table.sym("player_8025163C", table.GLOBL),
    0x80251708: table.sym("player_80251708", table.GLOBL),
    0x8025177C: table.sym("player_8025177C", table.GLOBL),
    0x80251818: table.sym_fnc("L80251818", flag=table.GLOBL|table.LOCAL),
    0x80251828: table.sym_fnc("L80251828", flag=table.GLOBL|table.LOCAL),
    0x80251838: table.sym_fnc("L80251838", flag=table.GLOBL|table.LOCAL),
    0x80251848: table.sym_fnc("L80251848", flag=table.GLOBL|table.LOCAL),
    0x802518A8: table.sym("player_802518A8", table.GLOBL),
    0x802519A8: table.sym_fnc("L802519A8", flag=table.GLOBL|table.LOCAL),
    0x802519B4: table.sym_fnc("L802519B4", flag=table.GLOBL|table.LOCAL),
    0x802519C4: table.sym_fnc("L802519C4", flag=table.GLOBL|table.LOCAL),
    0x802519D4: table.sym_fnc("L802519D4", flag=table.GLOBL|table.LOCAL),
    0x802519E4: table.sym_fnc("L802519E4", flag=table.GLOBL|table.LOCAL),
    0x802519F4: table.sym_fnc("L802519F4", flag=table.GLOBL|table.LOCAL),
    0x80251A48: table.sym("player_80251A48", table.GLOBL),
    0x80251AFC: table.sym("player_80251AFC", table.GLOBL),
    0x80251B54: table.sym("player_80251B54", table.GLOBL),
    0x80251BD4: table.sym("player_80251BD4", table.GLOBL),
    0x80251CFC: table.sym("player_80251CFC", table.GLOBL),
    0x80251E24: table.sym("player_80251E24"),
    0x80251F24: table.sym("player_80251F24", table.GLOBL),
    0x80252000: table.sym("player_80252000", table.GLOBL),
    0x802521A0: table.sym("player_802521A0", table.GLOBL),
    0x8025229C: table.sym("player_8025229C"),
    0x802523C8: table.sym("player_802523C8"),
    0x80252460: table.sym("player_80252460"),
    0x8025260C: table.sym_fnc("L8025260C", flag=table.GLOBL|table.LOCAL),
    0x802526A4: table.sym_fnc("L802526A4", flag=table.GLOBL|table.LOCAL),
    0x80252720: table.sym_fnc("L80252720", flag=table.GLOBL|table.LOCAL),
    0x80252760: table.sym_fnc("L80252760", flag=table.GLOBL|table.LOCAL),
    0x802527E4: table.sym_fnc("L802527E4", flag=table.GLOBL|table.LOCAL),
    0x80252898: table.sym_fnc("L80252898", flag=table.GLOBL|table.LOCAL),
    0x802529A4: table.sym_fnc("L802529A4", flag=table.GLOBL|table.LOCAL),
    0x802529E4: table.sym("player_802529E4"),
    0x80252BD4: table.sym("player_80252BD4"),
    0x80252C18: table.sym("player_80252C18"),
    0x80252CF4: table.sym("player_80252CF4", table.GLOBL),
    0x80252E5C: table.sym("player_80252E5C", table.GLOBL),
    0x802530A0: table.sym("player_802530A0", table.GLOBL),
    0x80253178: table.sym("player_80253178", table.GLOBL),
    0x802531C4: table.sym("player_802531C4", table.GLOBL),
    0x80253218: table.sym("player_80253218", table.GLOBL),
    0x80253300: table.sym("player_80253300", table.GLOBL),
    0x802533E4: table.sym("player_802533E4", table.GLOBL),
    0x80253488: table.sym("player_80253488", table.GLOBL),
    0x80253588: table.sym("player_80253588"),
    0x80253720: table.sym("player_80253720"),
    0x80253838: table.sym("player_80253838"),
    0x8025395C: table.sym("player_8025395C"),
    0x80253A60: table.sym("player_80253A60"),
    0x80253D58: table.sym("player_80253D58"),
    0x80253EC0: table.sym("player_80253EC0"),
    0x80254060: table.sym("player_80254060"),
    0x802542B4: table.sym("player_802542B4"),
    0x80254338: table.sym("player_80254338"),
    0x80254390: table.sym("player_80254390"),
    0x802543E8: table.sym("player_802543E8"),
    0x80254588: table.sym("player_80254588"),
    0x80254768: table.sym("player_80254768"), # unused
    0x80254830: table.sym("player_80254830", table.GLOBL),
    0x80254B20: table.sym("player_80254B20", table.GLOBL),
    0x80254F44: table.sym("player_80254F44", table.GLOBL),

    # src/pl_physics.c
    0x80255080: table.sym("pl_physics_80255080", table.GLOBL),
    0x8025509C: table.sym("pl_physics_8025509C", table.GLOBL),
    0x802550B0: table.sym("pl_physics_802550B0", table.GLOBL),
    0x802550C0: table.sym("pl_physics_802550C0", table.GLOBL),
    0x80255238: table.sym("pl_physics_80255238", table.GLOBL),
    0x802552FC: table.sym("pl_physics_802552FC", table.GLOBL),
    0x80255414: table.sym("pl_physics_80255414", table.GLOBL),
    0x802554B0: table.sym_fnc("L802554B0", flag=table.GLOBL|table.LOCAL),
    0x802554FC: table.sym_fnc("L802554FC", flag=table.GLOBL|table.LOCAL),
    0x80255548: table.sym_fnc("L80255548", flag=table.GLOBL|table.LOCAL),
    0x80255594: table.sym_fnc("L80255594", flag=table.GLOBL|table.LOCAL),
    0x802555F4: table.sym_fnc("L802555F4", flag=table.GLOBL|table.LOCAL),
    0x80255620: table.sym_fnc("L80255620", flag=table.GLOBL|table.LOCAL),
    0x80255654: table.sym("pl_physics_80255654", table.GLOBL),
    0x8025570C: table.sym("pl_physics_8025570C", table.GLOBL),
    0x8025580C: table.sym("pl_physics_8025580C", table.GLOBL),
    0x802559B0: table.sym("pl_physics_802559B0", table.GLOBL),
    0x80255A34: table.sym("pl_physics_80255A34", table.GLOBL),
    0x80255B04: table.sym("pl_physics_80255B04"),
    0x80255D88: table.sym("pl_physics_80255D88", table.GLOBL),
    0x80255EC4: table.sym("pl_physics_80255EC4"),
    0x802560AC: table.sym("pl_physics_802560AC"),
    0x802564E0: table.sym("pl_physics_802564E0"),
    0x80256584: table.sym("pl_physics_80256584"),
    0x8025661C: table.sym("pl_physics_8025661C"),
    0x802569F8: table.sym("pl_physics_802569F8"),
    0x80256B24: table.sym("pl_physics_80256B24", table.GLOBL),
    0x80256CD8: table.sym("pl_physics_80256CD8"), # unused
    0x80256D8C: table.sym("pl_physics_80256D8C"), # unused

    # src/pl_demo.c
    0x80256E00: table.sym("pl_demo_80256E00"),
    0x80256E88: table.sym("pl_demo_80256E88", table.GLOBL),
    0x80257060: table.sym("pl_demo_80257060", table.GLOBL), # o callback
    0x802570DC: table.sym("pl_demo_802570DC", table.GLOBL), # o callback
    0x80257198: table.sym("s_pl_demo_80257198", table.GLOBL), # s callback
    0x80257270: table.sym("pl_demo_80257270"), # unused
    0x802572B0: table.sym("pl_demo_802572B0"),
    0x8025733C: table.sym("pl_demo_8025733C"),
    0x80257450: table.sym("pl_demo_80257450"),
    0x802574E8: table.sym("pl_demo_802574E8"),
    0x80257548: table.sym("pl_demo_80257548"),
    0x802575A8: table.sym("pl_demo_802575A8", table.GLOBL),
    0x80257640: table.sym("pl_demo_80257640", table.GLOBL),
    0x80257748: table.sym("pl_demo_80257748"),
    0x80257980: table.sym("pl_demo_80257980"),
    0x80257A0C: table.sym("pl_demo_80257A0C"),
    0x80257AB0: table.sym("pl_demo_80257AB0"),
    0x80257CE4: table.sym("pl_demo_80257CE4"),
    0x80257EAC: table.sym("pl_demo_80257EAC"),
    0x80258184: table.sym("pl_demo_80258184"),
    0x80258420: table.sym("pl_demo_80258420"),
    0x802584DC: table.sym("pl_demo_802584DC"),
    0x802585C0: table.sym("pl_demo_802585C0"),
    0x802586CC: table.sym("pl_demo_802586CC"),
    0x80258744: table.sym("pl_demo_80258744"),
    0x802587EC: table.sym("pl_demo_802587EC"),
    0x8025883C: table.sym("pl_demo_8025883C"),
    0x8025888C: table.sym("pl_demo_8025888C"),
    0x802588F8: table.sym("pl_demo_802588F8"),
    0x80258964: table.sym("pl_demo_80258964"),
    0x80258A7C: table.sym("pl_demo_80258A7C"),
    0x80258B24: table.sym("pl_demo_80258B24"),
    0x80258BA8: table.sym("pl_demo_80258BA8"),
    0x80258DAC: table.sym("pl_demo_80258DAC"),
    0x80258F94: table.sym("pl_demo_80258F94"),
    0x80259264: table.sym("pl_demo_80259264"),
    0x802593CC: table.sym("pl_demo_802593CC"),
    0x802594D4: table.sym("pl_demo_802594D4"),
    0x80259608: table.sym("pl_demo_80259608"),
    0x80259740: table.sym("pl_demo_80259740"),
    0x802597AC: table.sym("pl_demo_802597AC"),
    0x80259854: table.sym("pl_demo_80259854"),
    0x802598D0: table.sym("pl_demo_802598D0"),
    0x80259C30: table.sym("pl_demo_80259C30"),
    0x80259CE8: table.sym("pl_demo_80259CE8"),
    0x80259D74: table.sym("pl_demo_80259D74"),
    0x80259E00: table.sym("pl_demo_80259E00"),
    0x80259EF8: table.sym("pl_demo_80259EF8"),
    0x80259FCC: table.sym("pl_demo_80259FCC"),
    0x8025A040: table.sym("pl_demo_8025A040"),
    0x8025A0BC: table.sym("pl_demo_8025A0BC"),
    0x8025A1AC: table.sym_fnc("L8025A1AC", flag=table.GLOBL|table.LOCAL),
    0x8025A244: table.sym_fnc("L8025A244", flag=table.GLOBL|table.LOCAL),
    0x8025A2E0: table.sym_fnc("L8025A2E0", flag=table.GLOBL|table.LOCAL),
    0x8025A450: table.sym_fnc("L8025A450", flag=table.GLOBL|table.LOCAL),
    0x8025A494: table.sym("pl_demo_8025A494"),
    0x8025A610: table.sym("pl_demo_8025A610"),
    0x8025A6FC: table.sym("pl_demo_8025A6FC"),
    0x8025A858: table.sym("pl_demo_8025A858"),
    0x8025A9AC: table.sym("pl_demo_8025A9AC"),
    0x8025AE0C: table.sym("pl_demo_8025AE0C"),
    0x8025AEA8: table.sym("pl_demo_8025AEA8"),
    0x8025AFFC: table.sym("pl_demo_8025AFFC"),
    0x8025B050: table.sym("pl_demo_8025B050"),
    0x8025B0A4: table.sym("pl_demo_8025B0A4"),
    0x8025B0F8: table.sym("pl_demo_8025B0F8"),
    0x8025B11C: table.sym("pl_demo_8025B11C"),
    0x8025B178: table.sym("pl_demo_8025B178"),
    0x8025B234: table.sym("pl_demo_8025B234"),
    0x8025B2EC: table.sym("pl_demo_8025B2EC"),
    0x8025B404: table.sym("pl_demo_8025B404"),
    0x8025B454: table.sym("pl_demo_8025B454"),
    0x8025B520: table.sym("pl_demo_8025B520"),
    0x8025B58C: table.sym("pl_demo_8025B58C"),
    0x8025B5C4: table.sym_fnc("L8025B5C4", flag=table.GLOBL|table.LOCAL),
    0x8025B5D4: table.sym_fnc("L8025B5D4", flag=table.GLOBL|table.LOCAL),
    0x8025B5E4: table.sym_fnc("L8025B5E4", flag=table.GLOBL|table.LOCAL),
    0x8025B5F4: table.sym_fnc("L8025B5F4", flag=table.GLOBL|table.LOCAL),
    0x8025B604: table.sym_fnc("L8025B604", flag=table.GLOBL|table.LOCAL),
    0x8025B614: table.sym_fnc("L8025B614", flag=table.GLOBL|table.LOCAL),
    0x8025B624: table.sym_fnc("L8025B624", flag=table.GLOBL|table.LOCAL),
    0x8025B654: table.sym("pl_demo_8025B654"),
    0x8025B760: table.sym("pl_demo_8025B760"),
    0x8025B9A8: table.sym("pl_demo_8025B9A8"),
    0x8025BBEC: table.sym("pl_demo_8025BBEC"),
    0x8025BC80: table.sym("pl_demo_8025BC80"),
    0x8025BEB8: table.sym("pl_demo_8025BEB8"),
    0x8025BF64: table.sym("pl_demo_8025BF64"),
    0x8025C014: table.sym("pl_demo_8025C014"),
    0x8025C0C4: table.sym("pl_demo_8025C0C4"),
    0x8025C1C0: table.sym("pl_demo_8025C1C0"),
    0x8025C498: table.sym("pl_demo_8025C498"),
    0x8025C600: table.sym("pl_demo_8025C600"),
    0x8025C6F8: table.sym("pl_demo_8025C6F8"),
    0x8025C904: table.sym("pl_demo_8025C904"),
    0x8025CA48: table.sym("pl_demo_8025CA48"),
    0x8025CBDC: table.sym("pl_demo_8025CBDC"),
    0x8025CD6C: table.sym("pl_demo_8025CD6C"),
    0x8025CEF0: table.sym("pl_demo_8025CEF0"),
    0x8025CFE4: table.sym("pl_demo_8025CFE4"),
    0x8025D040: table.sym("pl_demo_8025D040"),
    0x8025D078: table.sym_fnc("L8025D078", flag=table.GLOBL|table.LOCAL),
    0x8025D088: table.sym_fnc("L8025D088", flag=table.GLOBL|table.LOCAL),
    0x8025D098: table.sym_fnc("L8025D098", flag=table.GLOBL|table.LOCAL),
    0x8025D0A8: table.sym_fnc("L8025D0A8", flag=table.GLOBL|table.LOCAL),
    0x8025D0B8: table.sym_fnc("L8025D0B8", flag=table.GLOBL|table.LOCAL),
    0x8025D0C8: table.sym_fnc("L8025D0C8", flag=table.GLOBL|table.LOCAL),
    0x8025D0D8: table.sym_fnc("L8025D0D8", flag=table.GLOBL|table.LOCAL),
    0x8025D0E8: table.sym_fnc("L8025D0E8", flag=table.GLOBL|table.LOCAL),
    0x8025D0F8: table.sym_fnc("L8025D0F8", flag=table.GLOBL|table.LOCAL),
    0x8025D108: table.sym_fnc("L8025D108", flag=table.GLOBL|table.LOCAL),
    0x8025D118: table.sym_fnc("L8025D118", flag=table.GLOBL|table.LOCAL),
    0x8025D128: table.sym_fnc("L8025D128", flag=table.GLOBL|table.LOCAL),
    0x8025D138: table.sym_fnc("L8025D138", flag=table.GLOBL|table.LOCAL),
    0x8025D1D4: table.sym("pl_demo_8025D1D4"),
    0x8025D4F0: table.sym("pl_demo_8025D4F0"),
    0x8025D70C: table.sym("pl_demo_8025D70C"),
    0x8025D798: table.sym("pl_demo_main", table.GLOBL),
    0x8025D92C: table.sym_fnc("L8025D92C", flag=table.GLOBL|table.LOCAL),
    0x8025D954: table.sym_fnc("L8025D954", flag=table.GLOBL|table.LOCAL),
    0x8025D968: table.sym_fnc("L8025D968", flag=table.GLOBL|table.LOCAL),
    0x8025D97C: table.sym_fnc("L8025D97C", flag=table.GLOBL|table.LOCAL),
    0x8025D990: table.sym_fnc("L8025D990", flag=table.GLOBL|table.LOCAL),
    0x8025D9CC: table.sym_fnc("L8025D9CC", flag=table.GLOBL|table.LOCAL),
    0x8025D9E0: table.sym_fnc("L8025D9E0", flag=table.GLOBL|table.LOCAL),
    0x8025D9F4: table.sym_fnc("L8025D9F4", flag=table.GLOBL|table.LOCAL),
    0x8025DA08: table.sym_fnc("L8025DA08", flag=table.GLOBL|table.LOCAL),
    0x8025DA1C: table.sym_fnc("L8025DA1C", flag=table.GLOBL|table.LOCAL),
    0x8025DA30: table.sym_fnc("L8025DA30", flag=table.GLOBL|table.LOCAL),
    0x8025DA44: table.sym_fnc("L8025DA44", flag=table.GLOBL|table.LOCAL),
    0x8025DA58: table.sym_fnc("L8025DA58", flag=table.GLOBL|table.LOCAL),
    0x8025DA6C: table.sym_fnc("L8025DA6C", flag=table.GLOBL|table.LOCAL),
    0x8025DA80: table.sym_fnc("L8025DA80", flag=table.GLOBL|table.LOCAL),
    0x8025DA94: table.sym_fnc("L8025DA94", flag=table.GLOBL|table.LOCAL),
    0x8025DAA8: table.sym_fnc("L8025DAA8", flag=table.GLOBL|table.LOCAL),
    0x8025DABC: table.sym_fnc("L8025DABC", flag=table.GLOBL|table.LOCAL),
    0x8025DAD0: table.sym_fnc("L8025DAD0", flag=table.GLOBL|table.LOCAL),
    0x8025DAE4: table.sym_fnc("L8025DAE4", flag=table.GLOBL|table.LOCAL),
    0x8025DAF8: table.sym_fnc("L8025DAF8", flag=table.GLOBL|table.LOCAL),
    0x8025DB0C: table.sym_fnc("L8025DB0C", flag=table.GLOBL|table.LOCAL),
    0x8025DB20: table.sym_fnc("L8025DB20", flag=table.GLOBL|table.LOCAL),
    0x8025DB34: table.sym_fnc("L8025DB34", flag=table.GLOBL|table.LOCAL),
    0x8025DB48: table.sym_fnc("L8025DB48", flag=table.GLOBL|table.LOCAL),
    0x8025DB5C: table.sym_fnc("L8025DB5C", flag=table.GLOBL|table.LOCAL),
    0x8025DB70: table.sym_fnc("L8025DB70", flag=table.GLOBL|table.LOCAL),
    0x8025DB84: table.sym_fnc("L8025DB84", flag=table.GLOBL|table.LOCAL),
    0x8025DB98: table.sym_fnc("L8025DB98", flag=table.GLOBL|table.LOCAL),
    0x8025DBAC: table.sym_fnc("L8025DBAC", flag=table.GLOBL|table.LOCAL),
    0x8025DBC0: table.sym_fnc("L8025DBC0", flag=table.GLOBL|table.LOCAL),
    0x8025DBD4: table.sym_fnc("L8025DBD4", flag=table.GLOBL|table.LOCAL),
    0x8025DBE8: table.sym_fnc("L8025DBE8", flag=table.GLOBL|table.LOCAL),
    0x8025DBFC: table.sym_fnc("L8025DBFC", flag=table.GLOBL|table.LOCAL),
    0x8025DC10: table.sym_fnc("L8025DC10", flag=table.GLOBL|table.LOCAL),
    0x8025DC24: table.sym_fnc("L8025DC24", flag=table.GLOBL|table.LOCAL),
    0x8025DC38: table.sym_fnc("L8025DC38", flag=table.GLOBL|table.LOCAL),
    0x8025DC4C: table.sym_fnc("L8025DC4C", flag=table.GLOBL|table.LOCAL),
    0x8025DC74: table.sym_fnc("L8025DC74", flag=table.GLOBL|table.LOCAL),
    0x8025DC88: table.sym_fnc("L8025DC88", flag=table.GLOBL|table.LOCAL),
    0x8025DC9C: table.sym_fnc("L8025DC9C", flag=table.GLOBL|table.LOCAL),
    0x8025DCB0: table.sym_fnc("L8025DCB0", flag=table.GLOBL|table.LOCAL),
    0x8025DCC4: table.sym_fnc("L8025DCC4", flag=table.GLOBL|table.LOCAL),
    0x8025DCD8: table.sym_fnc("L8025DCD8", flag=table.GLOBL|table.LOCAL),
    0x8025DCEC: table.sym_fnc("L8025DCEC", flag=table.GLOBL|table.LOCAL),
    0x8025DD00: table.sym_fnc("L8025DD00", flag=table.GLOBL|table.LOCAL),
    0x8025DD14: table.sym_fnc("L8025DD14", flag=table.GLOBL|table.LOCAL),

    # src/pl_hang.c
    0x8025DD70: table.sym("pl_hang_8025DD70"),
    0x8025DE1C: table.sym("pl_hang_8025DE1C"),
    0x8025DF04: table.sym("pl_hang_8025DF04"),
    0x8025E21C: table.sym("pl_hang_8025E21C"),
    0x8025E5A8: table.sym("pl_hang_8025E5A8"),
    0x8025E7A4: table.sym("pl_hang_8025E7A4"),
    0x8025E830: table.sym("pl_hang_8025E830"),
    0x8025E930: table.sym("pl_hang_8025E930"),
    0x8025EA30: table.sym("pl_hang_8025EA30"),
    0x8025EB50: table.sym("pl_hang_8025EB50"),
    0x8025ECFC: table.sym("pl_hang_8025ECFC"),
    0x8025EED0: table.sym("pl_hang_8025EED0"),
    0x8025EF58: table.sym("pl_hang_8025EF58"),
    0x8025F0B4: table.sym("pl_hang_8025F0B4"),
    0x8025F1E4: table.sym("pl_hang_8025F1E4"),
    0x8025F384: table.sym("pl_hang_8025F384"),
    0x8025F4B4: table.sym("pl_hang_8025F4B4"),
    0x8025F560: table.sym("pl_hang_8025F560"),
    0x8025F644: table.sym("pl_hang_8025F644"),
    0x8025F6C0: table.sym("pl_hang_8025F6C0"),
    0x8025F970: table.sym("pl_hang_8025F970"),
    0x8025FA64: table.sym("pl_hang_8025FA64"),
    0x8025FAE8: table.sym("pl_hang_8025FAE8"),
    0x8025FB90: table.sym("pl_hang_8025FB90"),
    0x8025FC6C: table.sym("pl_hang_8025FC6C"),
    0x80260154: table.sym("pl_hang_80260154"),
    0x80260568: table.sym("pl_hang_80260568"),
    0x802605D0: table.sym("pl_hang_main", table.GLOBL),
    0x80260748: table.sym_fnc("L80260748", flag=table.GLOBL|table.LOCAL),
    0x8026075C: table.sym_fnc("L8026075C", flag=table.GLOBL|table.LOCAL),
    0x80260770: table.sym_fnc("L80260770", flag=table.GLOBL|table.LOCAL),
    0x80260784: table.sym_fnc("L80260784", flag=table.GLOBL|table.LOCAL),
    0x80260798: table.sym_fnc("L80260798", flag=table.GLOBL|table.LOCAL),

    # src/pl_wait.c
    0x802608B0: table.sym("pl_wait_802608B0"),
    0x80260AAC: table.sym("pl_wait_80260AAC"),
    0x80260CB4: table.sym("pl_wait_80260CB4"),
    0x80260F94: table.sym("pl_wait_80260F94"),
    0x80261000: table.sym("pl_wait_80261000"),
    0x80261268: table.sym("pl_wait_80261268"),
    0x802614FC: table.sym("pl_wait_802614FC"),
    0x8026168C: table.sym("pl_wait_8026168C"),
    0x802618D8: table.sym("pl_wait_802618D8"),
    0x802619D0: table.sym("pl_wait_802619D0"),
    0x80261AD0: table.sym("pl_wait_80261AD0"),
    0x80261BF8: table.sym("pl_wait_80261BF8"),
    0x80261CEC: table.sym("pl_wait_80261CEC"),
    0x80261DB4: table.sym("pl_wait_80261DB4"),
    0x80261F70: table.sym("pl_wait_80261F70"),
    0x80262080: table.sym("pl_wait_80262080"),
    0x8026217C: table.sym("pl_wait_8026217C"),
    0x802621DC: table.sym("pl_wait_802621DC"),
    0x802622DC: table.sym("pl_wait_802622DC"),
    0x80262398: table.sym("pl_wait_80262398"),
    0x80262490: table.sym("pl_wait_80262490"),
    0x80262530: table.sym("pl_wait_80262530"),
    0x80262650: table.sym("pl_wait_80262650"),
    0x80262770: table.sym("pl_wait_80262770"),
    0x80262890: table.sym("pl_wait_80262890"),
    0x80262980: table.sym("pl_wait_80262980"),
    0x80262BC4: table.sym("pl_wait_80262BC4"),
    0x80262C34: table.sym("pl_wait_80262C34"),
    0x80262D68: table.sym("pl_wait_80262D68"),
    0x80262DC4: table.sym("pl_wait_80262DC4"),
    0x80262E20: table.sym("pl_wait_80262E20"),
    0x80262E94: table.sym("pl_wait_80262E94"),
    0x80262EF0: table.sym("pl_wait_80262EF0"),
    0x80262F50: table.sym("pl_wait_80262F50"),
    0x80262FEC: table.sym("pl_wait_80262FEC"),
    0x8026305C: table.sym("pl_wait_8026305C"),
    0x802630F8: table.sym("pl_wait_802630F8"),
    0x802631F0: table.sym("pl_wait_802631F0"),
    0x802632E8: table.sym("pl_wait_802632E8"),
    0x802633B4: table.sym("pl_wait_802633B4"),
    0x8026350C: table.sym("pl_wait_8026350C"),
    0x802635E8: table.sym("pl_wait_802635E8"),
    0x80263784: table.sym("pl_wait_80263784"),
    0x80263898: table.sym("pl_wait_main", table.GLOBL),
    0x80263B38: table.sym_fnc("L80263B38", flag=table.GLOBL|table.LOCAL),
    0x80263B4C: table.sym_fnc("L80263B4C", flag=table.GLOBL|table.LOCAL),
    0x80263B88: table.sym_fnc("L80263B88", flag=table.GLOBL|table.LOCAL),
    0x80263BEC: table.sym_fnc("L80263BEC", flag=table.GLOBL|table.LOCAL),
    0x80263C00: table.sym_fnc("L80263C00", flag=table.GLOBL|table.LOCAL),
    0x80263C14: table.sym_fnc("L80263C14", flag=table.GLOBL|table.LOCAL),
    0x80263C28: table.sym_fnc("L80263C28", flag=table.GLOBL|table.LOCAL),
    0x80263C3C: table.sym_fnc("L80263C3C", flag=table.GLOBL|table.LOCAL),
    0x80263C50: table.sym_fnc("L80263C50", flag=table.GLOBL|table.LOCAL),
    0x80263C64: table.sym_fnc("L80263C64", flag=table.GLOBL|table.LOCAL),
    0x80263C78: table.sym_fnc("L80263C78", flag=table.GLOBL|table.LOCAL),
    0x80263C8C: table.sym_fnc("L80263C8C", flag=table.GLOBL|table.LOCAL),
    0x80263CB4: table.sym_fnc("L80263CB4", flag=table.GLOBL|table.LOCAL),
    0x80263CC8: table.sym_fnc("L80263CC8", flag=table.GLOBL|table.LOCAL),
    0x80263CDC: table.sym_fnc("L80263CDC", flag=table.GLOBL|table.LOCAL),
    0x80263CF0: table.sym_fnc("L80263CF0", flag=table.GLOBL|table.LOCAL),
    0x80263D04: table.sym_fnc("L80263D04", flag=table.GLOBL|table.LOCAL),
    0x80263D18: table.sym_fnc("L80263D18", flag=table.GLOBL|table.LOCAL),
    0x80263D2C: table.sym_fnc("L80263D2C", flag=table.GLOBL|table.LOCAL),
    0x80263D54: table.sym_fnc("L80263D54", flag=table.GLOBL|table.LOCAL),
    0x80263D7C: table.sym_fnc("L80263D7C", flag=table.GLOBL|table.LOCAL),
    0x80263D90: table.sym_fnc("L80263D90", flag=table.GLOBL|table.LOCAL),
    0x80263DA4: table.sym_fnc("L80263DA4", flag=table.GLOBL|table.LOCAL),
    0x80263DCC: table.sym_fnc("L80263DCC", flag=table.GLOBL|table.LOCAL),
    0x80263DE0: table.sym_fnc("L80263DE0", flag=table.GLOBL|table.LOCAL),
    0x80263E08: table.sym_fnc("L80263E08", flag=table.GLOBL|table.LOCAL),

    # src/pl_walk.c
    0x80263E60: table.sym("pl_walk_80263E60"),
    0x80263EE4: table.sym("pl_walk_80263EE4", table.GLOBL),
    0x80264024: table.sym("pl_walk_80264024"),
    0x8026409C: table.sym("pl_walk_8026409C"),
    0x802640FC: table.sym("pl_walk_802640FC"),
    0x802642B4: table.sym("pl_walk_802642B4"),
    0x80264340: table.sym("pl_walk_80264340"),
    0x8026440C: table.sym("pl_walk_8026440C"),
    0x80264740: table.sym("pl_walk_80264740"),
    0x80264B54: table.sym("pl_walk_80264B54"),
    0x80264D80: table.sym("pl_walk_80264D80"),
    0x80264E18: table.sym("pl_walk_80264E18"),
    0x80265080: table.sym("pl_walk_80265080"),
    0x802651B0: table.sym("pl_walk_802651B0"),
    0x80265244: table.sym("pl_walk_80265244"),
    0x80265458: table.sym("pl_walk_80265458"),
    0x80265514: table.sym("pl_walk_80265514"),
    0x80265558: table.sym("pl_walk_80265558"),
    0x80265620: table.sym("pl_walk_80265620"),
    0x80265700: table.sym("pl_walk_80265700"),
    0x80265B1C: table.sym("pl_walk_80265B1C"),
    0x80265D90: table.sym("pl_walk_80265D90"),
    0x80265DF8: table.sym("pl_walk_80265DF8"),
    0x80266038: table.sym("pl_walk_80266038"),
    0x802661CC: table.sym("pl_walk_802661CC"),
    0x80266354: table.sym("pl_walk_80266354"),
    0x802665B4: table.sym("pl_walk_802665B4"),
    0x80266734: table.sym("pl_walk_80266734"),
    0x8026699C: table.sym("pl_walk_8026699C"),
    0x80266AF8: table.sym("pl_walk_80266AF8"),
    0x80266D4C: table.sym("pl_walk_80266D4C"),
    0x80266E48: table.sym("pl_walk_80266E48"),
    0x80266FC8: table.sym("pl_walk_80266FC8"),
    0x80267240: table.sym("pl_walk_80267240"),
    0x80267504: table.sym("pl_walk_80267504"),
    0x80267728: table.sym("pl_walk_80267728"),
    0x8026795C: table.sym("pl_walk_8026795C"),
    0x80267C24: table.sym("pl_walk_80267C24"),
    0x80267CE4: table.sym("pl_walk_80267CE4"),
    0x80267FA4: table.sym("pl_walk_80267FA4"),
    0x80268074: table.sym("pl_walk_80268074"),
    0x802680D4: table.sym("pl_walk_802680D4"),
    0x80268168: table.sym("pl_walk_80268168"),
    0x80268338: table.sym("pl_walk_80268338"),
    0x802684AC: table.sym("pl_walk_802684AC"),
    0x802685C0: table.sym("pl_walk_802685C0"),
    0x80268608: table.sym("pl_walk_80268608"),
    0x80268684: table.sym("pl_walk_80268684"),
    0x802687B8: table.sym("pl_walk_802687B8"),
    0x802689F8: table.sym("pl_walk_802689F8"),
    0x80268ADC: table.sym("pl_walk_80268ADC"),
    0x80268B64: table.sym("pl_walk_80268B64"),
    0x80268BB0: table.sym("pl_walk_80268BB0"),
    0x80268BFC: table.sym("pl_walk_80268BFC"),
    0x80268C48: table.sym("pl_walk_80268C48"),
    0x80268C94: table.sym("pl_walk_80268C94"),
    0x80268D04: table.sym("pl_walk_80268D04"),
    0x80268DCC: table.sym("pl_walk_80268DCC"),
    0x80268F78: table.sym("pl_walk_80268F78"),
    0x80269108: table.sym("pl_walk_80269108"),
    0x80269170: table.sym("pl_walk_80269170"),
    0x802691D8: table.sym("pl_walk_802691D8"),
    0x80269264: table.sym("pl_walk_80269264"),
    0x80269300: table.sym("pl_walk_80269300"),
    0x8026939C: table.sym("pl_walk_8026939C"),
    0x8026947C: table.sym("pl_walk_8026947C"),
    0x802694E4: table.sym("pl_walk_802694E4"),
    0x80269588: table.sym("pl_walk_80269588"),
    0x80269640: table.sym("pl_walk_80269640"),
    0x80269788: table.sym("pl_walk_80269788"),
    0x802697DC: table.sym("pl_walk_802697DC"),
    0x80269830: table.sym("pl_walk_80269830"),
    0x80269954: table.sym("pl_walk_main", table.GLOBL),
    0x80269BEC: table.sym_fnc("L80269BEC", flag=table.GLOBL|table.LOCAL),
    0x80269C00: table.sym_fnc("L80269C00", flag=table.GLOBL|table.LOCAL),
    0x80269C14: table.sym_fnc("L80269C14", flag=table.GLOBL|table.LOCAL),
    0x80269C28: table.sym_fnc("L80269C28", flag=table.GLOBL|table.LOCAL),
    0x80269C78: table.sym_fnc("L80269C78", flag=table.GLOBL|table.LOCAL),
    0x80269CA0: table.sym_fnc("L80269CA0", flag=table.GLOBL|table.LOCAL),
    0x80269D54: table.sym_fnc("L80269D54", flag=table.GLOBL|table.LOCAL),
    0x80269D68: table.sym_fnc("L80269D68", flag=table.GLOBL|table.LOCAL),
    0x80269D7C: table.sym_fnc("L80269D7C", flag=table.GLOBL|table.LOCAL),
    0x80269D90: table.sym_fnc("L80269D90", flag=table.GLOBL|table.LOCAL),
    0x80269DA4: table.sym_fnc("L80269DA4", flag=table.GLOBL|table.LOCAL),
    0x80269DB8: table.sym_fnc("L80269DB8", flag=table.GLOBL|table.LOCAL),
    0x80269DCC: table.sym_fnc("L80269DCC", flag=table.GLOBL|table.LOCAL),
    0x80269DE0: table.sym_fnc("L80269DE0", flag=table.GLOBL|table.LOCAL),
    0x80269DF4: table.sym_fnc("L80269DF4", flag=table.GLOBL|table.LOCAL),
    0x80269E08: table.sym_fnc("L80269E08", flag=table.GLOBL|table.LOCAL),
    0x80269E1C: table.sym_fnc("L80269E1C", flag=table.GLOBL|table.LOCAL),
    0x80269E30: table.sym_fnc("L80269E30", flag=table.GLOBL|table.LOCAL),
    0x80269E44: table.sym_fnc("L80269E44", flag=table.GLOBL|table.LOCAL),
    0x80269E58: table.sym_fnc("L80269E58", flag=table.GLOBL|table.LOCAL),
    0x80269E6C: table.sym_fnc("L80269E6C", flag=table.GLOBL|table.LOCAL),
    0x80269E80: table.sym_fnc("L80269E80", flag=table.GLOBL|table.LOCAL),
    0x80269E94: table.sym_fnc("L80269E94", flag=table.GLOBL|table.LOCAL),
    0x80269EA8: table.sym_fnc("L80269EA8", flag=table.GLOBL|table.LOCAL),
    0x80269EBC: table.sym_fnc("L80269EBC", flag=table.GLOBL|table.LOCAL),
    0x80269ED0: table.sym_fnc("L80269ED0", flag=table.GLOBL|table.LOCAL),

    # src/pl_jump.c
    0x80269F40: table.sym("pl_jump_80269F40"),
    0x80269FC0: table.sym("pl_jump_80269FC0"),
    0x8026A090: table.sym("pl_jump_8026A090"),
    0x8026A12C: table.sym("pl_jump_8026A12C"),
    0x8026A224: table.sym("pl_jump_8026A224"),
    0x8026A400: table.sym("pl_jump_8026A400"),
    0x8026A494: table.sym("pl_jump_8026A494"),
    0x8026A598: table.sym("pl_jump_8026A598"),
    0x8026A62C: table.sym("pl_jump_8026A62C"),
    0x8026A818: table.sym("pl_jump_8026A818"),
    0x8026AA48: table.sym("pl_jump_8026AA48"),
    0x8026ACD8: table.sym("pl_jump_8026ACD8"),
    0x8026AE5C: table.sym("pl_jump_8026AE5C"),
    0x8026B004: table.sym("pl_jump_8026B004"),
    0x8026B17C: table.sym("pl_jump_8026B17C"),
    0x8026B444: table.sym("pl_jump_8026B444"),
    0x8026B49C: table.sym_fnc("L8026B49C", flag=table.GLOBL|table.LOCAL),
    0x8026B4B0: table.sym_fnc("L8026B4B0", flag=table.GLOBL|table.LOCAL),
    0x8026B4E0: table.sym_fnc("L8026B4E0", flag=table.GLOBL|table.LOCAL),
    0x8026B62C: table.sym_fnc("L8026B62C", flag=table.GLOBL|table.LOCAL),
    0x8026B654: table.sym_fnc("L8026B654", flag=table.GLOBL|table.LOCAL),
    0x8026B670: table.sym_fnc("L8026B670", flag=table.GLOBL|table.LOCAL),
    0x8026B680: table.sym_fnc("L8026B680", flag=table.GLOBL|table.LOCAL),
    0x8026B6A0: table.sym("pl_jump_8026B6A0"),
    0x8026B740: table.sym("pl_jump_8026B740"),
    0x8026B814: table.sym("pl_jump_8026B814"),
    0x8026B90C: table.sym("pl_jump_8026B90C"),
    0x8026B9AC: table.sym("pl_jump_8026B9AC"),
    0x8026BAB8: table.sym("pl_jump_8026BAB8"),
    0x8026BBB4: table.sym("pl_jump_8026BBB4"),
    0x8026BCC0: table.sym("pl_jump_8026BCC0"),
    0x8026BDCC: table.sym("pl_jump_8026BDCC"),
    0x8026BE78: table.sym("pl_jump_8026BE78"),
    0x8026BF40: table.sym("pl_jump_8026BF40"),
    0x8026C034: table.sym("pl_jump_8026C034"),
    0x8026C1E0: table.sym("pl_jump_8026C1E0"),
    0x8026C4B8: table.sym("pl_jump_8026C4B8"),
    0x8026C5D0: table.sym("pl_jump_8026C5D0"),
    0x8026C738: table.sym("pl_jump_8026C738"),
    0x8026C880: table.sym("pl_jump_8026C880"),
    0x8026C9FC: table.sym("pl_jump_8026C9FC"),
    0x8026CD0C: table.sym("pl_jump_8026CD0C"),
    0x8026CE50: table.sym("pl_jump_8026CE50"),
    0x8026CF28: table.sym("pl_jump_8026CF28"),
    0x8026D1B0: table.sym("pl_jump_8026D1B0"),
    0x8026D33C: table.sym("pl_jump_8026D33C"),
    0x8026D3C8: table.sym("pl_jump_8026D3C8"),
    0x8026D43C: table.sym("pl_jump_8026D43C"),
    0x8026D4B0: table.sym("pl_jump_8026D4B0"),
    0x8026D508: table.sym("pl_jump_8026D508"),
    0x8026D560: table.sym("pl_jump_8026D560"),
    0x8026D608: table.sym("pl_jump_8026D608"),
    0x8026D6FC: table.sym("pl_jump_8026D6FC"),
    0x8026D770: table.sym("pl_jump_8026D770"),
    0x8026D988: table.sym("pl_jump_8026D988"),
    0x8026DB54: table.sym("pl_jump_8026DB54"),
    0x8026DCF4: table.sym("pl_jump_8026DCF4"),
    0x8026DE98: table.sym("pl_jump_8026DE98"),
    0x8026E088: table.sym("pl_jump_8026E088"),
    0x8026E2B4: table.sym("pl_jump_8026E2B4"),
    0x8026E59C: table.sym("pl_jump_8026E59C"),
    0x8026E810: table.sym("pl_jump_8026E810"),
    0x8026E968: table.sym("pl_jump_8026E968"),
    0x8026EC00: table.sym("pl_jump_8026EC00"),
    0x8026F158: table.sym("pl_jump_8026F158"),
    0x8026F2EC: table.sym("pl_jump_8026F2EC"),
    0x8026F614: table.sym("pl_jump_8026F614"),
    0x8026F660: table.sym("pl_jump_8026F660"),
    0x8026F840: table.sym("pl_jump_8026F840"),
    0x8026FA18: table.sym("pl_jump_8026FA18"),
    0x8026FB04: table.sym("pl_jump_main", table.GLOBL),
    0x8026FD70: table.sym_fnc("L8026FD70", flag=table.GLOBL|table.LOCAL),
    0x8026FD84: table.sym_fnc("L8026FD84", flag=table.GLOBL|table.LOCAL),
    0x8026FD98: table.sym_fnc("L8026FD98", flag=table.GLOBL|table.LOCAL),
    0x8026FDAC: table.sym_fnc("L8026FDAC", flag=table.GLOBL|table.LOCAL),
    0x8026FDC0: table.sym_fnc("L8026FDC0", flag=table.GLOBL|table.LOCAL),
    0x8026FDD4: table.sym_fnc("L8026FDD4", flag=table.GLOBL|table.LOCAL),
    0x8026FDE8: table.sym_fnc("L8026FDE8", flag=table.GLOBL|table.LOCAL),
    0x8026FE10: table.sym_fnc("L8026FE10", flag=table.GLOBL|table.LOCAL),
    0x8026FE24: table.sym_fnc("L8026FE24", flag=table.GLOBL|table.LOCAL),
    0x8026FE38: table.sym_fnc("L8026FE38", flag=table.GLOBL|table.LOCAL),
    0x8026FE4C: table.sym_fnc("L8026FE4C", flag=table.GLOBL|table.LOCAL),
    0x8026FE60: table.sym_fnc("L8026FE60", flag=table.GLOBL|table.LOCAL),
    0x8026FE74: table.sym_fnc("L8026FE74", flag=table.GLOBL|table.LOCAL),
    0x8026FE88: table.sym_fnc("L8026FE88", flag=table.GLOBL|table.LOCAL),
    0x8026FE9C: table.sym_fnc("L8026FE9C", flag=table.GLOBL|table.LOCAL),
    0x8026FEEC: table.sym_fnc("L8026FEEC", flag=table.GLOBL|table.LOCAL),
    0x8026FF00: table.sym_fnc("L8026FF00", flag=table.GLOBL|table.LOCAL),
    0x8026FF14: table.sym_fnc("L8026FF14", flag=table.GLOBL|table.LOCAL),
    0x8026FF28: table.sym_fnc("L8026FF28", flag=table.GLOBL|table.LOCAL),
    0x8026FF3C: table.sym_fnc("L8026FF3C", flag=table.GLOBL|table.LOCAL),
    0x8026FF64: table.sym_fnc("L8026FF64", flag=table.GLOBL|table.LOCAL),
    0x8026FF8C: table.sym_fnc("L8026FF8C", flag=table.GLOBL|table.LOCAL),
    0x8026FFA0: table.sym_fnc("L8026FFA0", flag=table.GLOBL|table.LOCAL),
    0x8026FFB4: table.sym_fnc("L8026FFB4", flag=table.GLOBL|table.LOCAL),
    0x8026FFC8: table.sym_fnc("L8026FFC8", flag=table.GLOBL|table.LOCAL),
    0x8026FFDC: table.sym_fnc("L8026FFDC", flag=table.GLOBL|table.LOCAL),
    0x80270004: table.sym_fnc("L80270004", flag=table.GLOBL|table.LOCAL),
    0x8027002C: table.sym_fnc("L8027002C", flag=table.GLOBL|table.LOCAL),
    0x80270040: table.sym_fnc("L80270040", flag=table.GLOBL|table.LOCAL),
    0x80270054: table.sym_fnc("L80270054", flag=table.GLOBL|table.LOCAL),
    0x802700B8: table.sym_fnc("L802700B8", flag=table.GLOBL|table.LOCAL),
    0x802700E0: table.sym_fnc("L802700E0", flag=table.GLOBL|table.LOCAL),

    # src/pl_swim.c
    0x80270110: table.sym("pl_swim_80270110"),
    0x802701CC: table.sym("pl_swim_802701CC"),
    0x80270234: table.sym("pl_swim_80270234"),
    0x80270304: table.sym("pl_swim_80270304"),
    0x80270500: table.sym("pl_swim_80270500"),
    0x80270918: table.sym("pl_swim_80270918"),
    0x80270A74: table.sym("pl_swim_80270A74"),
    0x80270B4C: table.sym("pl_swim_80270B4C"),
    0x80270C94: table.sym("pl_swim_80270C94"),
    0x80270E40: table.sym("pl_swim_80270E40"),
    0x80270FD8: table.sym("pl_swim_80270FD8"),
    0x802710C4: table.sym("pl_swim_802710C4"),
    0x802711D4: table.sym("pl_swim_802711D4"),
    0x802712C0: table.sym("pl_swim_802712C0"),
    0x802713BC: table.sym("pl_swim_802713BC"),
    0x802714A8: table.sym("pl_swim_802714A8"),
    0x802715EC: table.sym("pl_swim_802715EC"),
    0x8027163C: table.sym("pl_swim_8027163C"),
    0x80271704: table.sym("pl_swim_80271704"),
    0x80271918: table.sym("pl_swim_80271918"),
    0x8027197C: table.sym("pl_swim_8027197C"),
    0x80271AA0: table.sym("pl_swim_80271AA0"),
    0x80271D04: table.sym("pl_swim_80271D04"),
    0x80271EB4: table.sym("pl_swim_80271EB4"),
    0x8027202C: table.sym("pl_swim_8027202C"),
    0x8027226C: table.sym("pl_swim_8027226C"),
    0x802723F0: table.sym("pl_swim_802723F0"),
    0x80272548: table.sym("pl_swim_80272548"),
    0x8027267C: table.sym("pl_swim_8027267C"),
    0x80272778: table.sym("pl_swim_80272778"),
    0x80272870: table.sym("pl_swim_80272870"),
    0x80272A60: table.sym("pl_swim_80272A60"),
    0x80272B1C: table.sym("pl_swim_80272B1C"),
    0x80272B64: table.sym("pl_swim_80272B64"),
    0x80272BAC: table.sym("pl_swim_80272BAC"),
    0x80272CBC: table.sym("pl_swim_80272CBC"),
    0x80272DC0: table.sym("pl_swim_80272DC0"),
    0x80272E3C: table.sym("pl_swim_80272E3C"),
    0x80272FE8: table.sym_fnc("L80272FE8", flag=table.GLOBL|table.LOCAL),
    0x80273004: table.sym_fnc("L80273004", flag=table.GLOBL|table.LOCAL),
    0x80273020: table.sym_fnc("L80273020", flag=table.GLOBL|table.LOCAL),
    0x8027303C: table.sym_fnc("L8027303C", flag=table.GLOBL|table.LOCAL),
    0x80273058: table.sym_fnc("L80273058", flag=table.GLOBL|table.LOCAL),
    0x80273070: table.sym_fnc("L80273070", flag=table.GLOBL|table.LOCAL),
    0x802730B8: table.sym_fnc("L802730B8", flag=table.GLOBL|table.LOCAL),
    0x802730CC: table.sym_fnc("L802730CC", flag=table.GLOBL|table.LOCAL),
    0x802730E0: table.sym_fnc("L802730E0", flag=table.GLOBL|table.LOCAL),
    0x802730F4: table.sym_fnc("L802730F4", flag=table.GLOBL|table.LOCAL),
    0x80273108: table.sym_fnc("L80273108", flag=table.GLOBL|table.LOCAL),
    0x8027311C: table.sym_fnc("L8027311C", flag=table.GLOBL|table.LOCAL),
    0x80273160: table.sym("pl_swim_80273160"),
    0x80273518: table.sym("pl_swim_80273518"),
    0x802735A4: table.sym("pl_swim_802735A4"),
    0x80273618: table.sym("pl_swim_80273618"),
    0x802737F4: table.sym("pl_swim_802737F4"),
    0x80273A2C: table.sym("pl_swim_80273A2C"),
    0x80273BD4: table.sym("pl_swim_80273BD4"),
    0x80273CD0: table.sym("pl_swim_80273CD0"),
    0x80273E74: table.sym("pl_swim_80273E74"),
    0x80274030: table.sym("pl_swim_80274030"),
    0x80274134: table.sym("pl_swim_80274134"),
    0x80274268: table.sym("pl_swim_80274268"),
    0x80274384: table.sym("pl_swim_80274384"),
    0x802744AC: table.sym("pl_swim_802744AC"),
    0x80274580: table.sym("pl_swim_80274580"),
    0x80274688: table.sym("pl_swim_80274688"),
    0x8027475C: table.sym("pl_swim_8027475C"),
    0x80274864: table.sym("pl_swim_80274864"),
    0x8027499C: table.sym("pl_swim_main", table.GLOBL),
    0x80274CBC: table.sym_fnc("L80274CBC", flag=table.GLOBL|table.LOCAL),
    0x80274CD0: table.sym_fnc("L80274CD0", flag=table.GLOBL|table.LOCAL),
    0x80274CE4: table.sym_fnc("L80274CE4", flag=table.GLOBL|table.LOCAL),
    0x80274CF8: table.sym_fnc("L80274CF8", flag=table.GLOBL|table.LOCAL),
    0x80274D0C: table.sym_fnc("L80274D0C", flag=table.GLOBL|table.LOCAL),
    0x80274D20: table.sym_fnc("L80274D20", flag=table.GLOBL|table.LOCAL),
    0x80274D34: table.sym_fnc("L80274D34", flag=table.GLOBL|table.LOCAL),
    0x80274D48: table.sym_fnc("L80274D48", flag=table.GLOBL|table.LOCAL),
    0x80274D5C: table.sym_fnc("L80274D5C", flag=table.GLOBL|table.LOCAL),
    0x80274DAC: table.sym_fnc("L80274DAC", flag=table.GLOBL|table.LOCAL),
    0x80274DE8: table.sym_fnc("L80274DE8", flag=table.GLOBL|table.LOCAL),
    0x80274DFC: table.sym_fnc("L80274DFC", flag=table.GLOBL|table.LOCAL),
    0x80274E24: table.sym_fnc("L80274E24", flag=table.GLOBL|table.LOCAL),
    0x80274E60: table.sym_fnc("L80274E60", flag=table.GLOBL|table.LOCAL),
    0x80274E74: table.sym_fnc("L80274E74", flag=table.GLOBL|table.LOCAL),
    0x80274E88: table.sym_fnc("L80274E88", flag=table.GLOBL|table.LOCAL),

    # src/pl_grab.c
    0x80274EB0: table.sym("pl_grab_80274EB0"),
    0x80274F10: table.sym("pl_grab_80274F10", table.GLOBL),
    0x80274F90: table.sym_fnc("L80274F90", flag=table.GLOBL|table.LOCAL),
    0x80274FA8: table.sym_fnc("L80274FA8", flag=table.GLOBL|table.LOCAL),
    0x80275050: table.sym_fnc("L80275050", flag=table.GLOBL|table.LOCAL),
    0x802750CC: table.sym_fnc("L802750CC", flag=table.GLOBL|table.LOCAL),
    0x802750E4: table.sym_fnc("L802750E4", flag=table.GLOBL|table.LOCAL),
    0x80275170: table.sym_fnc("L80275170", flag=table.GLOBL|table.LOCAL),
    0x802751EC: table.sym_fnc("L802751EC", flag=table.GLOBL|table.LOCAL),
    0x80275280: table.sym_fnc("L80275280", flag=table.GLOBL|table.LOCAL),
    0x80275308: table.sym_fnc("L80275308", flag=table.GLOBL|table.LOCAL),
    0x80275328: table.sym("pl_grab_80275328"),
    0x8027546C: table.sym("pl_grab_8027546C"),
    0x802755FC: table.sym("pl_grab_802755FC"),
    0x802756C8: table.sym("pl_grab_802756C8"),
    0x80275794: table.sym("pl_grab_80275794"),
    0x802758C0: table.sym("pl_grab_802758C0"),
    0x802759B4: table.sym("pl_grab_802759B4"),
    0x80275A80: table.sym("pl_grab_80275A80"),
    0x80275B34: table.sym("pl_grab_80275B34"),
    0x80275E78: table.sym("pl_grab_80275E78"),
    0x80275F0C: table.sym("pl_grab_80275F0C"),
    0x80275FE0: table.sym("pl_grab_main", table.GLOBL),
    0x802760C8: table.sym_fnc("L802760C8", flag=table.GLOBL|table.LOCAL),
    0x802760DC: table.sym_fnc("L802760DC", flag=table.GLOBL|table.LOCAL),
    0x802760F0: table.sym_fnc("L802760F0", flag=table.GLOBL|table.LOCAL),
    0x80276104: table.sym_fnc("L80276104", flag=table.GLOBL|table.LOCAL),
    0x80276140: table.sym_fnc("L80276140", flag=table.GLOBL|table.LOCAL),
    0x80276154: table.sym_fnc("L80276154", flag=table.GLOBL|table.LOCAL),
    0x80276168: table.sym_fnc("L80276168", flag=table.GLOBL|table.LOCAL),
    0x8027617C: table.sym_fnc("L8027617C", flag=table.GLOBL|table.LOCAL),

    # src/pl_callback.c
    0x802761D0: table.sym("s_stage_weather", table.GLOBL), # s callback
    0x802763D4: table.sym("s_stage_background", table.GLOBL), # s callback
    0x802764B0: table.sym("s_face_main", table.GLOBL), # s callback
    0x8027657C: table.sym("pl_callback_8027657C"),
    0x802765FC: table.sym("pl_callback_802765FC"),
    0x802766B4: table.sym("pl_callback_802766B4"),
    0x802767B8: table.sym("pl_callback_802767B8"),
    0x80276804: table.sym("pl_callback_80276804"),
    0x8027684C: table.sym("pl_callback_8027684C", table.GLOBL), # o callback
    0x802768A8: table.sym_fnc("L802768A8", flag=table.GLOBL|table.LOCAL),
    0x802768B8: table.sym_fnc("L802768B8", flag=table.GLOBL|table.LOCAL),
    0x802768C8: table.sym_fnc("L802768C8", flag=table.GLOBL|table.LOCAL),
    0x802768D8: table.sym_fnc("L802768D8", flag=table.GLOBL|table.LOCAL),
    0x802768E8: table.sym_fnc("L802768E8", flag=table.GLOBL|table.LOCAL),
    0x80276910: table.sym("pl_callback_80276910", table.GLOBL), # o callback
    0x80276AA0: table.sym("pl_callback_80276AA0"),
    0x80276BB8: table.sym("pl_callback_80276BB8", table.GLOBL), # o callback
    0x80276CCC: table.sym("pl_callback_80276CCC", table.GLOBL), # o callback
    0x80276F90: table.sym("pl_callback_80276F90"),
    0x802770A4: table.sym("s_player_alpha",         table.GLOBL), # s callback
    0x80277150: table.sym("s_player_select_lod",    table.GLOBL), # s callback
    0x802771BC: table.sym("s_player_select_eye",    table.GLOBL), # s callback
    0x80277294: table.sym("s_player_rot_torso",     table.GLOBL), # s callback
    0x802773A4: table.sym("s_player_rot_head",      table.GLOBL), # s callback
    0x802774F4: table.sym("s_player_select_glove",  table.GLOBL), # s callback
    0x802775CC: table.sym("s_player_scale",         table.GLOBL), # s callback
    0x802776D8: table.sym("s_player_select_cap",    table.GLOBL), # s callback
    0x80277740: table.sym("s_player_select_head",   table.GLOBL), # s callback
    0x80277824: table.sym("s_player_rot_wing",      table.GLOBL), # s callback
    0x8027795C: table.sym("s_player_hand",          table.GLOBL), # s callback
    0x80277B14: table.sym("s_inside_mirror",        table.GLOBL), # s callback
    0x80277D6C: table.sym("s_player_mirror",        table.GLOBL), # s callback

    # src/mem.c
    0x80277EE0: table.sym_fnc("segment_set", "uintptr_t", (
        "int segment",
        "const void *addr",
    ), table.GLOBL),
    0x80277F20: table.sym_fnc("segment_get", "void *", (
        "int segment",
    ), table.GLOBL), # unused
    0x80277F50: table.sym_fnc("segment_to_virtual", "void *", (
        "const void *addr",
    ), table.GLOBL),
    0x80277FA8: table.sym_fnc("virtual_to_segment", "void *", (
        "int segment",
        "const void *addr",
    ), table.GLOBL),
    0x80277FF0: table.sym_fnc("segment_write", flag=table.GLOBL),
    0x80278074: table.sym_fnc("mem_init", arg=(
        "void *start",
        "void *end",
    ), flag=table.GLOBL),
    0x80278120: table.sym_fnc("mem_alloc", "void *", (
        "size_t size",
        "int mode",
    ), table.GLOBL),
    0x80278238: table.sym_fnc("mem_free", arg=(
        "void *addr",
    ), flag=table.GLOBL),
    0x80278358: table.sym_fnc("mem_resize", arg=(
        "void *addr",
        "size_t size",
    ), flag=table.GLOBL), # static
    0x802783C8: table.sym_fnc("mem_available", "size_t", flag=table.GLOBL),
    0x802783E8: table.sym_fnc("mem_push", "size_t", flag=table.GLOBL),
    0x80278498: table.sym_fnc("mem_pull", "size_t", flag=table.GLOBL),
    0x80278504: table.sym_fnc("mem_dma", arg=(
        "u8 *dst",
        "const u8 *start",
        "const u8 *end",
    ), flag=table.GLOBL), # static
    0x80278610: table.sym_fnc("mem_load", "void *", (
        "const u8 *start",
        "const u8 *end",
        "int mode",
    ), table.GLOBL), # static
    0x8027868C: table.sym_fnc("mem_load_data", "void *", (
        "int segment",
        "const u8 *start",
        "const u8 *end",
        "int mode",
    ), table.GLOBL),
    0x802786F0: table.sym_fnc("mem_load_code", "void *", (
        "u8 *addr",
        "const u8 *start",
        "const u8 *end",
    ), table.GLOBL),
    0x802787D8: table.sym_fnc("mem_load_szp", "void *", (
        "int segment",
        "const u8 *start",
        "const u8 *end",
    ), table.GLOBL),
    0x802788B4: table.sym_fnc("mem_load_txt", "void *", (
        "int segment",
        "const u8 *start",
        "const u8 *end",
    ), table.GLOBL),
    0x80278974: table.sym_fnc("mem_load_main2", flag=table.GLOBL),
    0x80278A14: table.sym_fnc("arena_init", "ARENA *", (
        "size_t size",
        "int mode",
    ), table.GLOBL),
    0x80278AB8: table.sym_fnc("arena_alloc", "void *", (
        "ARENA *arena",
        "size_t size",
    ), table.GLOBL),
    0x80278B28: table.sym_fnc("arena_resize", "void *", (
        "ARENA *arena",
        "size_t size",
    ), table.GLOBL),
    0x80278B98: table.sym_fnc("heap_init", "HEAP *", (
        "size_t size",
        "int mode",
    ), table.GLOBL),
    0x80278C58: table.sym_fnc("heap_alloc", "void *", (
        "HEAP *heap",
        "size_t size",
    ), table.GLOBL),
    0x80278D74: table.sym_fnc("heap_free", arg=(
        "HEAP *heap",
        "void *addr",
    ), flag=table.GLOBL),
    0x80278F2C: table.sym_fnc("gfx_alloc", "void *", (
        "size_t size",
    ), table.GLOBL),
    0x80278FA0: table.sym_fnc("file_init_table", "FILE_TABLE *", (
        "const u8 *src",
    )),
    0x80279028: table.sym_fnc("file_init", arg=(
        "FILE *file",
        "const u8 *src",
        "u8 *buf",
    ), flag=table.GLOBL),
    0x80279084: table.sym_fnc("file_update", "int", (
        "FILE *file",
        "int index",
    ), table.GLOBL),

    # src/save.c
    0x80279160: table.sym("save_80279160"),
    0x80279174: table.sym("save_80279174"),
    0x80279218: table.sym("save_80279218"),
    0x802792C0: table.sym("save_802792C0"),
    0x80279314: table.sym("save_80279314"),
    0x8027939C: table.sym("save_8027939C"),
    0x802793FC: table.sym("save_802793FC"),
    0x802794A0: table.sym("save_802794A0"),
    0x8027951C: table.sym("save_8027951C"),
    0x802795A0: table.sym("save_802795A0"),
    0x802795D4: table.sym("save_802795D4"),
    0x80279650: table.sym("save_80279650"),
    0x80279700: table.sym("save_80279700"),
    0x80279748: table.sym("save_80279748"),
    0x80279840: table.sym("save_80279840", table.GLOBL),
    0x802798FC: table.sym("save_802798FC", table.GLOBL),
    0x80279960: table.sym("save_80279960", table.GLOBL),
    0x802799DC: table.sym_fnc("save_802799DC", flag=table.GLOBL),
    0x80279BC8: table.sym("save_80279BC8", table.GLOBL),
    0x80279C44: table.sym("save_80279C44", table.GLOBL),
    0x80279E44: table.sym("save_80279E44", table.GLOBL),
    0x80279E80: table.sym("save_80279E80", table.GLOBL),
    0x80279F80: table.sym("save_80279F80", table.GLOBL),
    0x8027A010: table.sym("save_8027A010", table.GLOBL),
    0x8027A0A8: table.sym("save_8027A0A8", table.GLOBL),
    0x8027A0F4: table.sym("save_8027A0F4", table.GLOBL),
    0x8027A16C: table.sym("save_8027A16C", table.GLOBL),
    0x8027A1C8: table.sym("save_8027A1C8", table.GLOBL),
    0x8027A23C: table.sym("save_8027A23C"),
    0x8027A310: table.sym("save_8027A310", table.GLOBL),
    0x8027A340: table.sym("save_8027A340", table.GLOBL),
    0x8027A390: table.sym("save_8027A390", table.GLOBL),
    0x8027A418: table.sym("save_8027A418", table.GLOBL),
    0x8027A4AC: table.sym("save_8027A4AC", table.GLOBL),
    0x8027A564: table.sym("save_8027A564", table.GLOBL),
    0x8027A5B4: table.sym_fnc("save_8027A5B4", "u16", flag=table.GLOBL),
    0x8027A5D4: table.sym("save_8027A5D4", table.GLOBL),
    0x8027A698: table.sym("save_8027A698", table.GLOBL),
    0x8027A6B0: table.sym("save_8027A6B0", table.GLOBL),
    0x8027A718: table.sym("save_8027A718", table.GLOBL),

    # src/scene.c
    0x8027A7D0: table.sym("scene_8027A7D0", table.GLOBL),
    0x8027A83C: table.sym("scene_8027A83C"),
    0x8027A8B0: table.sym("scene_8027A8B0", table.GLOBL),
    0x8027A93C: table.sym("scene_8027A93C", table.GLOBL),
    0x8027A9C8: table.sym_fnc("scene_8027A9C8", "void *", (
        "u8",
    ), table.GLOBL),
    0x8027AA28: table.sym("scene_8027AA28"),
    0x8027AA74: table.sym("scene_8027AA74"),
    0x8027AB04: table.sym("scene_8027AB04", table.GLOBL),
    0x8027AD74: table.sym("scene_8027AD74", table.GLOBL),
    0x8027AE44: table.sym("scene_8027AE44", table.GLOBL),
    0x8027AF48: table.sym("scene_8027AF48", table.GLOBL),
    0x8027AFBC: table.sym("scene_8027AFBC", table.GLOBL),
    0x8027B038: table.sym("scene_8027B038", table.GLOBL),
    0x8027B0C0: table.sym("scene_8027B0C0", table.GLOBL),
    0x8027B164: table.sym("scene_8027B164", table.GLOBL),
    0x8027B1A0: table.sym("scene_8027B1A0", table.GLOBL),
    0x8027B35C: table.sym("scene_8027B35C", table.GLOBL),
    0x8027B3B4: table.sym("scene_draw", table.GLOBL),

    # src/shape_draw.c
    0x8027B6C0: table.sym("shape_draw_layer_draw"),
    0x8027B904: table.sym("shape_draw_layer_gfx"),
    0x8027BA00: table.sym("shape_draw_layer"),
    0x8027BA98: table.sym("shape_draw_ortho"),
    0x8027BC74: table.sym("shape_draw_perspective"),
    0x8027BDF0: table.sym("shape_draw_lod"),
    0x8027BE84: table.sym("shape_draw_select"),
    0x8027BF58: table.sym("shape_draw_camera"),
    0x8027C114: table.sym("shape_draw_posrot"),
    0x8027C238: table.sym("shape_draw_pos"),
    0x8027C35C: table.sym("shape_draw_rot"),
    0x8027C474: table.sym("shape_draw_scale"),
    0x8027C594: table.sym("shape_draw_billboard"),
    0x8027C73C: table.sym("shape_draw_gfx"),
    0x8027C7A4: table.sym("shape_draw_callback"),
    0x8027C858: table.sym("shape_draw_background"),
    0x8027CA70: table.sym("shape_draw_joint"),
    0x8027CF38: table.sym("shape_draw_object_skeleton"),
    0x8027D0B8: table.sym("shape_draw_shadow"),
    0x8027D518: table.sym("shape_draw_object_visible"),
    0x8027D6FC: table.sym("shape_draw_object"),
    0x8027DA10: table.sym("shape_draw_object_list"),
    0x8027DA84: table.sym("shape_draw_hand"),
    0x8027DE68: table.sym("shape_draw_child"),
    0x8027DEA8: table.sym("shape_draw_list"),
    0x8027DF90: table.sym_fnc("L8027DF90", flag=table.GLOBL|table.LOCAL),
    0x8027DFA0: table.sym_fnc("L8027DFA0", flag=table.GLOBL|table.LOCAL),
    0x8027DFB0: table.sym_fnc("L8027DFB0", flag=table.GLOBL|table.LOCAL),
    0x8027DFC0: table.sym_fnc("L8027DFC0", flag=table.GLOBL|table.LOCAL),
    0x8027DFD0: table.sym_fnc("L8027DFD0", flag=table.GLOBL|table.LOCAL),
    0x8027DFE0: table.sym_fnc("L8027DFE0", flag=table.GLOBL|table.LOCAL),
    0x8027DFF0: table.sym_fnc("L8027DFF0", flag=table.GLOBL|table.LOCAL),
    0x8027E000: table.sym_fnc("L8027E000", flag=table.GLOBL|table.LOCAL),
    0x8027E010: table.sym_fnc("L8027E010", flag=table.GLOBL|table.LOCAL),
    0x8027E020: table.sym_fnc("L8027E020", flag=table.GLOBL|table.LOCAL),
    0x8027E030: table.sym_fnc("L8027E030", flag=table.GLOBL|table.LOCAL),
    0x8027E040: table.sym_fnc("L8027E040", flag=table.GLOBL|table.LOCAL),
    0x8027E050: table.sym_fnc("L8027E050", flag=table.GLOBL|table.LOCAL),
    0x8027E060: table.sym_fnc("L8027E060", flag=table.GLOBL|table.LOCAL),
    0x8027E070: table.sym_fnc("L8027E070", flag=table.GLOBL|table.LOCAL),
    0x8027E080: table.sym_fnc("L8027E080", flag=table.GLOBL|table.LOCAL),
    0x8027E090: table.sym_fnc("L8027E090", flag=table.GLOBL|table.LOCAL),
    0x8027E0A0: table.sym_fnc("L8027E0A0", flag=table.GLOBL|table.LOCAL),
    0x8027E0B0: table.sym_fnc("L8027E0B0", flag=table.GLOBL|table.LOCAL),
    0x8027E0C0: table.sym_fnc("L8027E0C0", flag=table.GLOBL|table.LOCAL),
    0x8027E130: table.sym("shape_draw_scene", table.GLOBL),

    # src/time.c
    0x8027E3E0: table.sym_fnc("time_8027E3E0", arg=(
        "int",
    ), flag=table.GLOBL),
    0x8027E490: table.sym_fnc("time_8027E490", flag=table.GLOBL),
    0x8027E520: table.sym_fnc("time_8027E520", arg=(
        "int",
    ), flag=table.GLOBL),
    0x8027E5CC: table.sym_fnc("time_8027E5CC", flag=table.GLOBL),
    0x8027E65C: table.sym("time_8027E65C"),
    0x8027E958: table.sym("time_8027E958"),
    0x8027EBCC: table.sym("time_8027EBCC"),
    0x8027EEAC: table.sym("time_8027EEAC"),
    0x8027F460: table.sym_fnc("time_draw", flag=table.GLOBL),

    # src/slidec.S
    0x8027F4E0: table.sym_fnc("slidec", arg=(
        "const u8 *src",
        "u8 *dst",
    ), flag=table.GLOBL),

    # src/camera.c
    0x8027F590: table.sym("camera_8027F590", table.GLOBL),
    0x8027F5CC: table.sym_fnc("L8027F5CC", flag=table.GLOBL|table.LOCAL),
    0x8027F5EC: table.sym_fnc("L8027F5EC", flag=table.GLOBL|table.LOCAL),
    0x8027F614: table.sym_fnc("L8027F614", flag=table.GLOBL|table.LOCAL),
    0x8027F62C: table.sym_fnc("L8027F62C", flag=table.GLOBL|table.LOCAL),
    0x8027F6CC: table.sym_fnc("L8027F6CC", flag=table.GLOBL|table.LOCAL),
    0x8027F76C: table.sym_fnc("L8027F76C", flag=table.GLOBL|table.LOCAL),
    0x8027F80C: table.sym_fnc("L8027F80C", flag=table.GLOBL|table.LOCAL),
    0x8027F834: table.sym_fnc("L8027F834", flag=table.GLOBL|table.LOCAL),
    0x8027F89C: table.sym_fnc("L8027F89C", flag=table.GLOBL|table.LOCAL),
    0x8027F8B8: table.sym("camera_8027F8B8", table.GLOBL),
    0x8027F8F0: table.sym_fnc("L8027F8F0", flag=table.GLOBL|table.LOCAL),
    0x8027F908: table.sym_fnc("L8027F908", flag=table.GLOBL|table.LOCAL),
    0x8027F920: table.sym_fnc("L8027F920", flag=table.GLOBL|table.LOCAL),
    0x8027F938: table.sym_fnc("L8027F938", flag=table.GLOBL|table.LOCAL),
    0x8027F950: table.sym_fnc("L8027F950", flag=table.GLOBL|table.LOCAL),
    0x8027F968: table.sym_fnc("L8027F968", flag=table.GLOBL|table.LOCAL),
    0x8027F980: table.sym_fnc("L8027F980", flag=table.GLOBL|table.LOCAL),
    0x8027F9A8: table.sym_fnc("L8027F9A8", flag=table.GLOBL|table.LOCAL),
    0x8027F9C0: table.sym_fnc("L8027F9C0", flag=table.GLOBL|table.LOCAL),
    0x8027F9D8: table.sym_fnc("L8027F9D8", flag=table.GLOBL|table.LOCAL),
    0x8027F9F0: table.sym("camera_8027F9F0", table.GLOBL),
    0x8027FB74: table.sym("camera_8027FB74"), # unused
    0x8027FC18: table.sym("camera_8027FC18"),
    0x8027FE20: table.sym("camera_8027FE20"),
    0x8027FF00: table.sym("camera_8027FF00"), # unused
    0x8027FFF8: table.sym("camera_8027FFF8"),
    0x80280368: table.sym("camera_80280368"),
    0x802804F4: table.sym("camera_802804F4"),
    0x802806A4: table.sym("camera_802806A4"),
    0x80280810: table.sym_fnc("camera_80280810", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x80280970: table.sym_fnc("camera_80280970", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x80280B00: table.sym("camera_80280B00"),
    0x80281188: table.sym("camera_80281188"),
    0x802813BC: table.sym("camera_802813BC"),
    0x802813EC: table.sym("camera_802813EC"),
    0x8028146C: table.sym("camera_8028146C"),
    0x80281588: table.sym("camera_80281588"),
    0x802816A0: table.sym_fnc("camera_802816A0", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x802817FC: table.sym("camera_802817FC"),
    0x80281904: table.sym_fnc("camera_80281904", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x80282280: table.sym_fnc("camera_80282280", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x802826A0: table.sym_fnc("camera_802826A0", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x80282C0C: table.sym_fnc("camera_80282C0C", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x80282C28: table.sym("camera_80282C28"), # unused
    0x80282C3C: table.sym("camera_80282C3C"),
    0x80282C7C: table.sym("camera_80282C7C"),
    0x80282CE0: table.sym("camera_80282CE0"),
    0x80282D78: table.sym_fnc("camera_80282D78", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x80283340: table.sym("camera_80283340"),
    0x80283578: table.sym("camera_80283578"),
    0x802839E4: table.sym("camera_802839E4"),
    0x80283A18: table.sym_fnc("camera_80283A18", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x80283A34: table.sym("camera_80283A34"),
    0x80283A68: table.sym_fnc("camera_80283A68", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x80283AF8: table.sym("camera_80283AF8"),
    0x80284CB8: table.sym("camera_80284CB8"),
    0x80284CFC: table.sym("camera_80284CFC"),
    0x80284D38: table.sym("camera_80284D38"),
    0x80284D74: table.sym_fnc("camera_80284D74", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x802850AC: table.sym("camera_802850AC"),
    0x802850EC: table.sym_fnc("camera_802850EC", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x8028517C: table.sym("camera_8028517C"), # unused
    0x802851DC: table.sym("camera_802851DC"),
    0x8028526C: table.sym("camera_8028526C"),
    0x802852F4: table.sym("camera_802852F4"),
    0x80285370: table.sym("camera_80285370"),
    0x80285808: table.sym_fnc("camera_80285808", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x802858A4: table.sym("camera_802858A4"),
    0x80285A2C: table.sym("camera_80285A2C"),
    0x80285D20: table.sym("camera_80285D20"),
    0x80285ED8: table.sym_fnc("camera_80285ED8", "int", (
        "struct camera *cam",
        "vecf",
        "vecf",
    ), table.GLOBL), # data / tbl
    0x80285F60: table.sym("camera_80285F60"),
    0x8028603C: table.sym("camera_8028603C"),
    0x80286088: table.sym("camera_80286088"),
    0x80286188: table.sym("camera_80286188", table.GLOBL),
    0x80286420: table.sym("camera_80286420"),
    0x802868F8: table.sym("camera_802868F8", table.GLOBL),
    0x80286C84: table.sym_fnc("L80286C84", flag=table.GLOBL|table.LOCAL),
    0x80286C94: table.sym_fnc("L80286C94", flag=table.GLOBL|table.LOCAL),
    0x80286CA4: table.sym_fnc("L80286CA4", flag=table.GLOBL|table.LOCAL),
    0x80286CB4: table.sym_fnc("L80286CB4", flag=table.GLOBL|table.LOCAL),
    0x80286CC4: table.sym_fnc("L80286CC4", flag=table.GLOBL|table.LOCAL),
    0x80286CD4: table.sym_fnc("L80286CD4", flag=table.GLOBL|table.LOCAL),
    0x80286CE4: table.sym_fnc("L80286CE4", flag=table.GLOBL|table.LOCAL),
    0x80286CF4: table.sym_fnc("L80286CF4", flag=table.GLOBL|table.LOCAL),
    0x80286D04: table.sym_fnc("L80286D04", flag=table.GLOBL|table.LOCAL),
    0x80286D14: table.sym_fnc("L80286D14", flag=table.GLOBL|table.LOCAL),
    0x80286D24: table.sym_fnc("L80286D24", flag=table.GLOBL|table.LOCAL),
    0x80286D34: table.sym_fnc("L80286D34", flag=table.GLOBL|table.LOCAL),
    0x80286D44: table.sym_fnc("L80286D44", flag=table.GLOBL|table.LOCAL),
    0x80286D54: table.sym_fnc("L80286D54", flag=table.GLOBL|table.LOCAL),
    0x80286D64: table.sym_fnc("L80286D64", flag=table.GLOBL|table.LOCAL),
    0x80286F68: table.sym("camera_80286F68", table.GLOBL),
    0x8028724C: table.sym("camera_8028724C"),
    0x8028752C: table.sym_fnc("L8028752C", flag=table.GLOBL|table.LOCAL),
    0x80287578: table.sym_fnc("L80287578", flag=table.GLOBL|table.LOCAL),
    0x8028758C: table.sym_fnc("L8028758C", flag=table.GLOBL|table.LOCAL),
    0x802875A0: table.sym_fnc("L802875A0", flag=table.GLOBL|table.LOCAL),
    0x80287664: table.sym_fnc("L80287664", flag=table.GLOBL|table.LOCAL),
    0x8028767C: table.sym_fnc("L8028767C", flag=table.GLOBL|table.LOCAL),
    0x80287694: table.sym_fnc("L80287694", flag=table.GLOBL|table.LOCAL),
    0x802876B0: table.sym_fnc("L802876B0", flag=table.GLOBL|table.LOCAL),
    0x802876C8: table.sym_fnc("L802876C8", flag=table.GLOBL|table.LOCAL),
    0x802876EC: table.sym_fnc("L802876EC", flag=table.GLOBL|table.LOCAL),
    0x802879EC: table.sym("camera_802879EC"),
    0x80287BC4: table.sym("camera_80287BC4", table.GLOBL),
    0x80287BE0: table.sym("camera_80287BE0"),
    0x80287CB8: table.sym("camera_80287CB8"),
    0x80287D30: table.sym("s_stage_camera", table.GLOBL), # s callback
    0x80287DC0: table.sym("camera_80287DC0"),
    0x80287DD4: table.sym("camera_80287DD4"),
    0x80287DE8: table.sym("camera_80287DE8"),
    0x80287E28: table.sym("camera_80287E28"),
    0x80287E50: table.sym("camera_80287E50"),
    0x80287E78: table.sym("camera_80287E78"), # unused
    0x80287EA0: table.sym("camera_80287EA0"),
    0x802882E4: table.sym("camera_802882E4"),
    0x80288624: table.sym("camera_80288624", table.GLOBL),
    0x80288718: table.sym("camera_80288718"),
    0x80288888: table.sym("camera_80288888"),
    0x802888B4: table.sym_fnc("L802888B4", flag=table.GLOBL|table.LOCAL),
    0x802888D8: table.sym_fnc("L802888D8", flag=table.GLOBL|table.LOCAL),
    0x802888FC: table.sym_fnc("L802888FC", flag=table.GLOBL|table.LOCAL),
    0x80288920: table.sym_fnc("L80288920", flag=table.GLOBL|table.LOCAL),
    0x80288944: table.sym_fnc("L80288944", flag=table.GLOBL|table.LOCAL),
    0x80288968: table.sym_fnc("L80288968", flag=table.GLOBL|table.LOCAL),
    0x802889B0: table.sym("camera_802889B0"),
    0x80288CE4: table.sym("camera_80288CE4"),
    0x80288E68: table.sym("camera_80288E68"),
    0x80288F5C: table.sym("camera_80288F5C"),
    0x80289198: table.sym("camera_80289198"),
    0x80289214: table.sym("camera_80289214"),
    0x802892D8: table.sym("camera_802892D8"),
    0x8028935C: table.sym("camera_8028935C"),
    0x802893F4: table.sym("camera_802893F4"),
    0x80289488: table.sym("camera_80289488"),
    0x802894B4: table.sym("camera_802894B4"),
    0x8028956C: table.sym("camera_8028956C"),
    0x80289610: table.sym("camera_80289610"),
    0x80289684: table.sym("camera_80289684"),
    0x802896F8: table.sym("camera_802896F8"),
    0x8028976C: table.sym("camera_8028976C"),
    0x8028984C: table.sym("camera_8028984C"),
    0x8028993C: table.sym("camera_8028993C"),
    0x802899CC: table.sym("camera_802899CC"),
    0x80289B0C: table.sym("camera_80289B0C", table.GLOBL),
    0x80289C00: table.sym("camera_80289C00"),
    0x80289D20: table.sym("camera_80289D20"),
    0x80289F88: table.sym("camera_80289F88"),
    0x8028A080: table.sym("camera_8028A080"),
    0x8028A0F4: table.sym("camera_8028A0F4"),
    0x8028A4EC: table.sym("camera_8028A4EC"),
    0x8028A6BC: table.sym("camera_8028A6BC"),
    0x8028A7EC: table.sym("camera_8028A7EC"),
    0x8028A834: table.sym("camera_8028A834"),
    0x8028A8E8: table.sym("camera_8028A8E8"),
    0x8028AA28: table.sym("camera_8028AA28"),
    0x8028AAD8: table.sym("camera_8028AAD8"),
    0x8028AB60: table.sym("camera_8028AB60"),
    0x8028AC28: table.sym("camera_8028AC28"),
    0x8028ACCC: table.sym("camera_8028ACCC"),
    0x8028AD4C: table.sym("camera_8028AD4C"),
    0x8028AE1C: table.sym("camera_8028AE1C"),
    0x8028AEF0: table.sym("camera_8028AEF0"),
    0x8028AF4C: table.sym("camera_8028AF4C"),
    0x8028B00C: table.sym("camera_8028B00C"),
    0x8028B068: table.sym("camera_8028B068"),
    0x8028B11C: table.sym("camera_8028B11C"), # unused
    0x8028B1D0: table.sym("camera_8028B1D0"),
    0x8028B218: table.sym("camera_8028B218"),
    0x8028B32C: table.sym("camera_8028B32C"),
    0x8028B438: table.sym("camera_8028B438"),
    0x8028B50C: table.sym("camera_8028B50C"),
    0x8028B724: table.sym("camera_8028B724"),
    0x8028B754: table.sym("camera_8028B754"),
    0x8028B784: table.sym("camera_8028B784"),
    0x8028B7C4: table.sym("camera_8028B7C4"),
    0x8028B804: table.sym("camera_8028B804"),
    0x8028B850: table.sym("camera_8028B850"),
    0x8028B884: table.sym("camera_8028B884"),
    0x8028B8B8: table.sym("camera_8028B8B8"),
    0x8028B8EC: table.sym("camera_8028B8EC"),
    0x8028B920: table.sym("camera_8028B920"),
    0x8028B954: table.sym("camera_8028B954"),
    0x8028B9C4: table.sym("camera_8028B9C4"),
    0x8028BD34: table.sym("camera_8028BD34", table.GLOBL),
    0x8028BD98: table.sym("camera_8028BD98"),
    0x8028C038: table.sym("camera_8028C038"),
    0x8028C13C: table.sym("camera_8028C13C"),
    0x8028C18C: table.sym("camera_8028C18C"),
    0x8028C26C: table.sym("camera_8028C26C"),
    0x8028C2C8: table.sym("camera_8028C2C8"),
    0x8028C658: table.sym_fnc("L8028C658", flag=table.GLOBL|table.LOCAL),
    0x8028C668: table.sym_fnc("L8028C668", flag=table.GLOBL|table.LOCAL),
    0x8028C678: table.sym_fnc("L8028C678", flag=table.GLOBL|table.LOCAL),
    0x8028C688: table.sym_fnc("L8028C688", flag=table.GLOBL|table.LOCAL),
    0x8028C698: table.sym_fnc("L8028C698", flag=table.GLOBL|table.LOCAL),
    0x8028C6A8: table.sym_fnc("L8028C6A8", flag=table.GLOBL|table.LOCAL),
    0x8028C724: table.sym_fnc("L8028C724", flag=table.GLOBL|table.LOCAL),
    0x8028C734: table.sym_fnc("L8028C734", flag=table.GLOBL|table.LOCAL),
    0x8028C744: table.sym_fnc("L8028C744", flag=table.GLOBL|table.LOCAL),
    0x8028C754: table.sym_fnc("L8028C754", flag=table.GLOBL|table.LOCAL),
    0x8028C764: table.sym_fnc("L8028C764", flag=table.GLOBL|table.LOCAL),
    0x8028C7A0: table.sym("camera_8028C7A0", table.GLOBL),
    0x8028C8F0: table.sym("camera_8028C8F0"),
    0x8028C9AC: table.sym("camera_8028C9AC"), # unused
    0x8028C9CC: table.sym("camera_8028C9CC"),
    0x8028CB08: table.sym("camera_8028CB08"), # unused
    0x8028CBF0: table.sym("camera_8028CBF0"),
    0x8028CD94: table.sym("camera_8028CD94"),
    0x8028CDEC: table.sym("camera_8028CDEC"),
    0x8028CE24: table.sym("camera_8028CE24"),
    0x8028D41C: table.sym("camera_8028D41C"), # unused
    0x8028D44C: table.sym("camera_8028D44C"),
    0x8028D5AC: table.sym("camera_8028D5AC"),
    0x8028D5FC: table.sym("camera_8028D5FC"),
    0x8028D658: table.sym("camera_8028D658"),
    0x8028D698: table.sym("camera_8028D698"),
    0x8028D79C: table.sym("camera_8028D79C"),
    0x8028D888: table.sym("camera_8028D888"),
    0x8028D92C: table.sym("camera_8028D92C"),
    0x8028DA18: table.sym_fnc("camera_8028DA18", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DA50: table.sym_fnc("camera_8028DA50", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DAEC: table.sym_fnc("camera_8028DAEC", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DB38: table.sym_fnc("camera_8028DB38", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DBB4: table.sym_fnc("camera_8028DBB4", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DBF4: table.sym_fnc("camera_8028DBF4", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DC1C: table.sym_fnc("camera_8028DC1C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DC70: table.sym_fnc("camera_8028DC70", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DCA4: table.sym("camera_8028DCA4"),
    0x8028DD48: table.sym_fnc("camera_8028DD48", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DE2C: table.sym_fnc("camera_8028DE2C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DE5C: table.sym_fnc("camera_8028DE5C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DE90: table.sym_fnc("camera_8028DE90", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DEC4: table.sym_fnc("camera_8028DEC4", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DEF8: table.sym_fnc("camera_8028DEF8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DF24: table.sym_fnc("camera_8028DF24", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DF6C: table.sym_fnc("camera_8028DF6C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DFB4: table.sym_fnc("camera_8028DFB4", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028DFE8: table.sym_fnc("camera_8028DFE8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E01C: table.sym_fnc("camera_8028E01C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E064: table.sym_fnc("camera_8028E064", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E098: table.sym_fnc("camera_8028E098", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E0EC: table.sym_fnc("camera_8028E0EC", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E164: table.sym_fnc("camera_8028E164", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E210: table.sym_fnc("camera_8028E210", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E298: table.sym_fnc("camera_8028E298", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E300: table.sym_fnc("camera_8028E300", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E334: table.sym("camera_8028E334"), # unused
    0x8028E38C: table.sym_fnc("camera_8028E38C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E3B8: table.sym_fnc("camera_8028E3B8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E3F0: table.sym_fnc("camera_8028E3F0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E41C: table.sym_fnc("camera_8028E41C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E450: table.sym_fnc("camera_8028E450", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E47C: table.sym_fnc("camera_8028E47C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E524: table.sym_fnc("camera_8028E524", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E55C: table.sym_fnc("camera_8028E55C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E594: table.sym_fnc("camera_8028E594", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E5CC: table.sym_fnc("camera_8028E5CC", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E604: table.sym_fnc("camera_8028E604", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E63C: table.sym_fnc("camera_8028E63C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E674: table.sym_fnc("camera_8028E674", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E6C4: table.sym_fnc("camera_8028E6C4", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E714: table.sym_fnc("camera_8028E714", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E758: table.sym_fnc("camera_8028E758", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E790: table.sym_fnc("camera_8028E790", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E7C8: table.sym_fnc("camera_8028E7C8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E818: table.sym_fnc("camera_8028E818", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E868: table.sym_fnc("camera_8028E868", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E8A0: table.sym_fnc("camera_8028E8A0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E8CC: table.sym_fnc("camera_8028E8CC", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E930: table.sym_fnc("camera_8028E930", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E974: table.sym_fnc("camera_8028E974", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E9A0: table.sym_fnc("camera_8028E9A0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028E9D8: table.sym_fnc("camera_8028E9D8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028EA28: table.sym_fnc("camera_8028EA28", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028EA60: table.sym_fnc("camera_8028EA60", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028EAB0: table.sym_fnc("camera_8028EAB0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028EAE8: table.sym_fnc("camera_8028EAE8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028EB38: table.sym_fnc("camera_8028EB38", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028EB88: table.sym_fnc("camera_8028EB88", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028EBC0: table.sym_fnc("camera_8028EBC0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028EC04: table.sym_fnc("camera_8028EC04", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028EC2C: table.sym_fnc("camera_8028EC2C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / ctl
    0x8028EC58: table.sym("camera_8028EC58"),
    0x8028ED30: table.sym("camera_8028ED30"),
    0x8028ED98: table.sym("camera_8028ED98"),
    0x8028EEB0: table.sym("camera_8028EEB0"),
    0x8028F670: table.sym("camera_8028F670"),
    0x8028F914: table.sym("camera_8028F914"),
    0x8028FC9C: table.sym("camera_8028FC9C"),
    0x8028FE24: table.sym("camera_8028FE24"),
    0x8028FE58: table.sym("camera_8028FE58"),
    0x8028FE84: table.sym("camera_8028FE84"), # unused
    0x8028FF04: table.sym("camera_8028FF04", table.GLOBL),
    0x8028FFC8: table.sym("camera_8028FFC8", table.GLOBL),
    0x8029000C: table.sym("camera_8029000C", table.GLOBL),
    0x80290098: table.sym("camera_80290098"),
    0x802900E0: table.sym("camera_802900E0"),
    0x80290104: table.sym("camera_80290104"),
    0x80290168: table.sym("camera_80290168"),
    0x802901A4: table.sym("camera_802901A4"),
    0x802901FC: table.sym("camera_802901FC"),
    0x802903B8: table.sym("camera_802903B8"),
    0x8029040C: table.sym("camera_8029040C"), # unused
    0x80290440: table.sym_fnc("camera_80290440", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80290474: table.sym("camera_80290474"), # unused
    0x802904A8: table.sym("camera_802904A8"),
    0x802904E4: table.sym("camera_802904E4"),
    0x8029051C: table.sym("camera_8029051C"),
    0x8029053C: table.sym("camera_8029053C"),
    0x80290784: table.sym("camera_80290784"),
    0x802907F4: table.sym("camera_802907F4"),
    0x80290864: table.sym("camera_80290864"),
    0x802908E8: table.sym("camera_802908E8"),
    0x80290938: table.sym("camera_80290938"), # unused
    0x80290984: table.sym("camera_80290984"), # unused
    0x802909D0: table.sym("camera_802909D0"),
    0x80290A5C: table.sym("camera_80290A5C"),
    0x80290A90: table.sym("camera_80290A90"), # unused
    0x80290ABC: table.sym("camera_80290ABC"),
    0x80290B54: table.sym("camera_80290B54"),
    0x80290BA4: table.sym("camera_80290BA4"),
    0x80290BD8: table.sym("camera_80290BD8"),
    0x80290C08: table.sym("camera_80290C08"), # unused
    0x80290C1C: table.sym_fnc("camera_80290C1C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80290C30: table.sym_fnc("camera_80290C30", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80290C44: table.sym("camera_80290C44"),
    0x80290C9C: table.sym("camera_80290C9C"),
    0x80290D90: table.sym_fnc("camera_80290D90", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80290E00: table.sym_fnc("camera_80290E00", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80290E74: table.sym("camera_80290E74"),
    0x80290EB0: table.sym("camera_80290EB0"),
    0x80290F1C: table.sym_fnc("camera_80290F1C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80290F8C: table.sym_fnc("camera_80290F8C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80291074: table.sym("camera_80291074"),
    0x80291108: table.sym_fnc("camera_80291108", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802911C8: table.sym("camera_802911C8"),
    0x80291208: table.sym("camera_80291208"),
    0x8029127C: table.sym("camera_8029127C"),
    0x802912B8: table.sym("camera_802912B8"),
    0x80291354: table.sym_fnc("camera_80291354", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x8029142C: table.sym_fnc("camera_8029142C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802914CC: table.sym("camera_802914CC"),
    0x80291514: table.sym_fnc("camera_80291514", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802915D4: table.sym_fnc("camera_802915D4", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80291654: table.sym("camera_80291654"),
    0x802916B8: table.sym("camera_802916B8"),
    0x80291774: table.sym_fnc("camera_80291774", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802917E4: table.sym("camera_802917E4"),
    0x8029184C: table.sym("camera_8029184C"),
    0x80291870: table.sym_fnc("camera_80291870", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80291924: table.sym_fnc("camera_80291924", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80291964: table.sym("camera_80291964"),
    0x802919DC: table.sym("camera_802919DC"),
    0x80291AB4: table.sym("camera_80291AB4"),
    0x80291B18: table.sym("camera_80291B18"),
    0x80291B68: table.sym("camera_80291B68"),
    0x80291BF4: table.sym("camera_80291BF4"),
    0x80291C3C: table.sym("camera_80291C3C"),
    0x80291CD0: table.sym_fnc("camera_80291CD0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80291DB0: table.sym("camera_80291DB0"),
    0x80291E84: table.sym("camera_80291E84"),
    0x80291F18: table.sym("camera_80291F18"),
    0x80292038: table.sym("camera_80292038"),
    0x80292164: table.sym_fnc("camera_80292164", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802921FC: table.sym("camera_802921FC"),
    0x8029228C: table.sym("camera_8029228C"),
    0x80292324: table.sym("camera_80292324"),
    0x80292370: table.sym("camera_80292370"),
    0x802923B8: table.sym("camera_802923B8"),
    0x80292400: table.sym("camera_80292400"), # unused
    0x80292414: table.sym("camera_80292414"),
    0x8029244C: table.sym("camera_8029244C"),
    0x80292484: table.sym("camera_80292484"),
    0x802924B8: table.sym_fnc("camera_802924B8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80292628: table.sym("camera_80292628"),
    0x802926DC: table.sym("camera_802926DC"),
    0x802927D0: table.sym("camera_802927D0"),
    0x80292868: table.sym("camera_80292868"),
    0x80292974: table.sym("camera_80292974"),
    0x80292A20: table.sym("camera_80292A20"),
    0x80292A4C: table.sym("camera_80292A4C"),
    0x80292A80: table.sym_fnc("camera_80292A80", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80292C00: table.sym("camera_80292C00"),
    0x80292D80: table.sym("camera_80292D80"),
    0x80292E2C: table.sym("camera_80292E2C"),
    0x80292EC4: table.sym("camera_80292EC4"),
    0x80292F40: table.sym("camera_80292F40"),
    0x80292F98: table.sym("camera_80292F98"),
    0x80292FE4: table.sym("camera_80292FE4"),
    0x80293018: table.sym_fnc("camera_80293018", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802930F0: table.sym("camera_802930F0"),
    0x80293164: table.sym("camera_80293164"),
    0x802931C0: table.sym("camera_802931C0"),
    0x80293220: table.sym("camera_80293220"),
    0x8029328C: table.sym("camera_8029328C"),
    0x802932F4: table.sym("camera_802932F4"),
    0x80293328: table.sym("camera_80293328"),
    0x80293354: table.sym("camera_80293354"),
    0x8029338C: table.sym_fnc("camera_8029338C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80293488: table.sym("camera_80293488"),
    0x802934B4: table.sym("camera_802934B4"),
    0x802934D8: table.sym("camera_802934D8"),
    0x80293548: table.sym("camera_80293548"),
    0x802935E0: table.sym("camera_802935E0"),
    0x80293624: table.sym("camera_80293624"),
    0x8029369C: table.sym("camera_8029369C"),
    0x802936DC: table.sym("camera_802936DC"),
    0x80293708: table.sym("camera_80293708"),
    0x80293734: table.sym("camera_80293734"),
    0x802937E8: table.sym("camera_802937E8"),
    0x8029386C: table.sym_fnc("camera_8029386C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802938C8: table.sym_fnc("camera_802938C8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80293944: table.sym_fnc("camera_80293944", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80293ABC: table.sym("camera_80293ABC"),
    0x80293AE8: table.sym("camera_80293AE8"),
    0x80293B70: table.sym("camera_80293B70"),
    0x80293BF4: table.sym("camera_80293BF4"),
    0x80293C2C: table.sym_fnc("camera_80293C2C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80293CB0: table.sym_fnc("camera_80293CB0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80293D5C: table.sym_fnc("camera_80293D5C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80293D90: table.sym("camera_80293D90"),
    0x80293DD4: table.sym("camera_80293DD4"),
    0x80293E7C: table.sym_fnc("camera_80293E7C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80293ED8: table.sym_fnc("camera_80293ED8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80293F2C: table.sym("camera_80293F2C"),
    0x80293F70: table.sym_fnc("camera_80293F70", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80293FCC: table.sym("camera_80293FCC"),
    0x80294024: table.sym("camera_80294024"),
    0x80294088: table.sym("camera_80294088"),
    0x802940CC: table.sym("camera_802940CC"),
    0x8029410C: table.sym("camera_8029410C"),
    0x802942CC: table.sym("camera_802942CC"),
    0x802942F0: table.sym_fnc("camera_802942F0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802943D4: table.sym_fnc("camera_802943D4", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80294428: table.sym("camera_80294428"),
    0x80294718: table.sym("camera_80294718"),
    0x802947A4: table.sym("camera_802947A4"),
    0x8029480C: table.sym("camera_8029480C"),
    0x802948A0: table.sym("camera_802948A0"),
    0x80294A14: table.sym_fnc("camera_80294A14", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80294A94: table.sym_fnc("camera_80294A94", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80294AE8: table.sym("camera_80294AE8"),
    0x80294B78: table.sym("camera_80294B78"),
    0x80294BB4: table.sym("camera_80294BB4"),
    0x80294C28: table.sym("camera_80294C28"),
    0x80294C5C: table.sym_fnc("camera_80294C5C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80294CC4: table.sym("camera_80294CC4"),
    0x80294D48: table.sym("camera_80294D48"),
    0x80294D88: table.sym("camera_80294D88"), # unused
    0x80294DB4: table.sym_fnc("camera_80294DB4", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80294E24: table.sym("camera_80294E24"),
    0x80294EA8: table.sym("camera_80294EA8"),
    0x80294EE8: table.sym_fnc("camera_80294EE8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80294F58: table.sym("camera_80294F58"),
    0x80294F94: table.sym("camera_80294F94"),
    0x80294FEC: table.sym_fnc("camera_80294FEC", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802950B0: table.sym("camera_802950B0"),
    0x80295140: table.sym("camera_80295140"),
    0x802951F0: table.sym("camera_802951F0"),
    0x80295270: table.sym_fnc("camera_80295270", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80295310: table.sym("camera_80295310"),
    0x802953DC: table.sym("camera_802953DC"),
    0x80295418: table.sym_fnc("camera_80295418", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80295480: table.sym("camera_80295480"),
    0x802954EC: table.sym("camera_802954EC"),
    0x80295518: table.sym("camera_80295518"),
    0x80295580: table.sym("camera_80295580"),
    0x80295670: table.sym("camera_80295670"),
    0x80295740: table.sym("camera_80295740"),
    0x8029576C: table.sym("camera_8029576C"),
    0x802957C8: table.sym_fnc("camera_802957C8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80295894: table.sym_fnc("camera_80295894", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802958D4: table.sym("camera_802958D4"),
    0x80295930: table.sym_fnc("camera_80295930", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802959CC: table.sym("camera_802959CC"), # unused
    0x80295A58: table.sym("camera_80295A58"),
    0x80295BF0: table.sym("camera_80295BF0"),
    0x80295E24: table.sym("camera_80295E24"),
    0x80295E8C: table.sym_fnc("camera_80295E8C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80295FB0: table.sym_fnc("camera_80295FB0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80295FD8: table.sym_fnc("camera_80295FD8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80296020: table.sym("camera_80296020"),
    0x802960B0: table.sym("camera_802960B0"), # unused
    0x80296160: table.sym_fnc("camera_80296160", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802962C8: table.sym_fnc("camera_802962C8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802962F0: table.sym_fnc("camera_802962F0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80296318: table.sym("camera_80296318"),
    0x802963B8: table.sym("camera_802963B8"),
    0x8029652C: table.sym("camera_8029652C"),
    0x8029665C: table.sym("camera_8029665C"),
    0x8029669C: table.sym("camera_8029669C"),
    0x802966E4: table.sym("camera_802966E4"),
    0x80296710: table.sym_fnc("camera_80296710", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802967C4: table.sym_fnc("camera_802967C4", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x8029685C: table.sym("camera_8029685C"),
    0x802968A0: table.sym_fnc("camera_802968A0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x8029695C: table.sym("camera_8029695C"),
    0x802969F8: table.sym_fnc("camera_802969F8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80296A64: table.sym("camera_80296A64"),
    0x80296B30: table.sym_fnc("camera_80296B30", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80296BC8: table.sym("camera_80296BC8"),
    0x80296C4C: table.sym("camera_80296C4C"),
    0x80296D60: table.sym("camera_80296D60"),
    0x80296DA8: table.sym("camera_80296DA8"),
    0x80296EB4: table.sym("camera_80296EB4"),
    0x80296F38: table.sym("camera_80296F38"),
    0x80296F70: table.sym("camera_80296F70"), # unused
    0x80296FA8: table.sym_fnc("camera_80296FA8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80297148: table.sym("camera_80297148"),
    0x8029720C: table.sym("camera_8029720C"),
    0x80297290: table.sym("camera_80297290"),
    0x802972EC: table.sym("camera_802972EC"),
    0x80297300: table.sym("camera_80297300"),
    0x80297384: table.sym("camera_80297384"),
    0x802973B0: table.sym_fnc("camera_802973B0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80297464: table.sym("camera_80297464"),
    0x80297560: table.sym("camera_80297560"),
    0x8029758C: table.sym("camera_8029758C"),
    0x802975C4: table.sym("camera_802975C4"),
    0x8029762C: table.sym_fnc("camera_8029762C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802976BC: table.sym("camera_802976BC"),
    0x80297728: table.sym("camera_80297728"),
    0x80297748: table.sym("camera_80297748"),
    0x80297784: table.sym("camera_80297784"),
    0x802977C8: table.sym("camera_802977C8"),
    0x802977F4: table.sym("camera_802977F4"),
    0x80297820: table.sym("camera_80297820"),
    0x8029784C: table.sym_fnc("camera_8029784C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80297908: table.sym_fnc("camera_80297908", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80297A38: table.sym_fnc("camera_80297A38", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80297A64: table.sym_fnc("camera_80297A64", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80297B58: table.sym("camera_80297B58"),
    0x80297B84: table.sym_fnc("camera_80297B84", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80297C14: table.sym("camera_80297C14"),
    0x80297C40: table.sym_fnc("camera_80297C40", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80297D60: table.sym_fnc("L80297D60", flag=table.GLOBL|table.LOCAL),
    0x80297DA0: table.sym_fnc("L80297DA0", flag=table.GLOBL|table.LOCAL),
    0x80297E00: table.sym_fnc("L80297E00", flag=table.GLOBL|table.LOCAL),
    0x80297E20: table.sym_fnc("L80297E20", flag=table.GLOBL|table.LOCAL),
    0x80297E60: table.sym_fnc("L80297E60", flag=table.GLOBL|table.LOCAL),
    0x80297EA0: table.sym_fnc("L80297EA0", flag=table.GLOBL|table.LOCAL),
    0x80297EC0: table.sym_fnc("L80297EC0", flag=table.GLOBL|table.LOCAL),
    0x80297F00: table.sym_fnc("L80297F00", flag=table.GLOBL|table.LOCAL),
    0x80297F20: table.sym_fnc("L80297F20", flag=table.GLOBL|table.LOCAL),
    0x80297F40: table.sym_fnc("L80297F40", flag=table.GLOBL|table.LOCAL),
    0x80298024: table.sym_fnc("L80298024", flag=table.GLOBL|table.LOCAL),
    0x802980DC: table.sym("camera_802980DC"),
    0x8029819C: table.sym("camera_8029819C"),
    0x80298218: table.sym("camera_80298218"),
    0x80298254: table.sym("camera_80298254"),
    0x80298290: table.sym("camera_80298290"),
    0x802983B4: table.sym_fnc("camera_802983B4", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80298458: table.sym_fnc("camera_80298458", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802984A0: table.sym("camera_802984A0"),
    0x802984B4: table.sym_fnc("camera_802984B4", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802987B0: table.sym("camera_802987B0"),
    0x8029894C: table.sym("camera_8029894C"),
    0x802989E8: table.sym("camera_802989E8"),
    0x80298AF8: table.sym_fnc("camera_80298AF8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80298BA0: table.sym_fnc("camera_80298BA0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80298C2C: table.sym_fnc("camera_80298C2C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80298CCC: table.sym_fnc("camera_80298CCC", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80298D44: table.sym_fnc("camera_80298D44", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80298D9C: table.sym_fnc("camera_80298D9C", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80298FE8: table.sym_fnc("camera_80298FE8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80299100: table.sym_fnc("camera_80299100", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80299154: table.sym_fnc("camera_80299154", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802991A8: table.sym_fnc("camera_802991A8", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802991F0: table.sym_fnc("camera_802991F0", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802992CC: table.sym_fnc("camera_802992CC", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80299360: table.sym_fnc("camera_80299360", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x80299404: table.sym_fnc("camera_80299404", arg=(
        "struct camera *cam",
    ), flag=table.GLOBL), # data / demo
    0x802994E8: table.sym("camera_802994E8"),
    0x8029956C: table.sym_fnc("L8029956C", flag=table.GLOBL|table.LOCAL),
    0x802995B4: table.sym_fnc("L802995B4", flag=table.GLOBL|table.LOCAL),
    0x802995FC: table.sym_fnc("L802995FC", flag=table.GLOBL|table.LOCAL),
    0x80299644: table.sym_fnc("L80299644", flag=table.GLOBL|table.LOCAL),
    0x8029968C: table.sym_fnc("L8029968C", flag=table.GLOBL|table.LOCAL),
    0x802996D4: table.sym_fnc("L802996D4", flag=table.GLOBL|table.LOCAL),
    0x8029971C: table.sym_fnc("L8029971C", flag=table.GLOBL|table.LOCAL),
    0x80299764: table.sym_fnc("L80299764", flag=table.GLOBL|table.LOCAL),
    0x802997AC: table.sym_fnc("L802997AC", flag=table.GLOBL|table.LOCAL),
    0x802997F4: table.sym_fnc("L802997F4", flag=table.GLOBL|table.LOCAL),
    0x8029983C: table.sym_fnc("L8029983C", flag=table.GLOBL|table.LOCAL),
    0x80299884: table.sym_fnc("L80299884", flag=table.GLOBL|table.LOCAL),
    0x802998CC: table.sym_fnc("L802998CC", flag=table.GLOBL|table.LOCAL),
    0x80299914: table.sym_fnc("L80299914", flag=table.GLOBL|table.LOCAL),
    0x8029995C: table.sym_fnc("L8029995C", flag=table.GLOBL|table.LOCAL),
    0x802999A4: table.sym_fnc("L802999A4", flag=table.GLOBL|table.LOCAL),
    0x802999EC: table.sym_fnc("L802999EC", flag=table.GLOBL|table.LOCAL),
    0x80299A34: table.sym_fnc("L80299A34", flag=table.GLOBL|table.LOCAL),
    0x80299A7C: table.sym_fnc("L80299A7C", flag=table.GLOBL|table.LOCAL),
    0x80299AC4: table.sym_fnc("L80299AC4", flag=table.GLOBL|table.LOCAL),
    0x80299B0C: table.sym_fnc("L80299B0C", flag=table.GLOBL|table.LOCAL),
    0x80299B54: table.sym_fnc("L80299B54", flag=table.GLOBL|table.LOCAL),
    0x80299B9C: table.sym_fnc("L80299B9C", flag=table.GLOBL|table.LOCAL),
    0x80299BE4: table.sym_fnc("L80299BE4", flag=table.GLOBL|table.LOCAL),
    0x80299C2C: table.sym_fnc("L80299C2C", flag=table.GLOBL|table.LOCAL),
    0x80299C74: table.sym_fnc("L80299C74", flag=table.GLOBL|table.LOCAL),
    0x80299CBC: table.sym_fnc("L80299CBC", flag=table.GLOBL|table.LOCAL),
    0x80299D04: table.sym_fnc("L80299D04", flag=table.GLOBL|table.LOCAL),
    0x80299D4C: table.sym_fnc("L80299D4C", flag=table.GLOBL|table.LOCAL),
    0x80299D94: table.sym_fnc("L80299D94", flag=table.GLOBL|table.LOCAL),
    0x80299DDC: table.sym_fnc("L80299DDC", flag=table.GLOBL|table.LOCAL),
    0x80299E24: table.sym_fnc("L80299E24", flag=table.GLOBL|table.LOCAL),
    0x80299E6C: table.sym_fnc("L80299E6C", flag=table.GLOBL|table.LOCAL),
    0x80299EB4: table.sym_fnc("L80299EB4", flag=table.GLOBL|table.LOCAL),
    0x80299EFC: table.sym_fnc("L80299EFC", flag=table.GLOBL|table.LOCAL),
    0x80299F44: table.sym_fnc("L80299F44", flag=table.GLOBL|table.LOCAL),
    0x80299F8C: table.sym_fnc("L80299F8C", flag=table.GLOBL|table.LOCAL),
    0x80299FD4: table.sym_fnc("L80299FD4", flag=table.GLOBL|table.LOCAL),
    0x8029A01C: table.sym_fnc("L8029A01C", flag=table.GLOBL|table.LOCAL),
    0x8029A064: table.sym_fnc("L8029A064", flag=table.GLOBL|table.LOCAL),
    0x8029A0AC: table.sym_fnc("L8029A0AC", flag=table.GLOBL|table.LOCAL),
    0x8029A0F4: table.sym_fnc("L8029A0F4", flag=table.GLOBL|table.LOCAL),
    0x8029A13C: table.sym_fnc("L8029A13C", flag=table.GLOBL|table.LOCAL),
    0x8029A184: table.sym_fnc("L8029A184", flag=table.GLOBL|table.LOCAL),
    0x8029A1CC: table.sym_fnc("L8029A1CC", flag=table.GLOBL|table.LOCAL),
    0x8029A214: table.sym_fnc("L8029A214", flag=table.GLOBL|table.LOCAL),
    0x8029A2F8: table.sym("camera_8029A2F8"),
    0x8029A37C: table.sym("camera_8029A37C"),
    0x8029A3B4: table.sym("camera_8029A3B4"),
    0x8029A41C: table.sym("camera_8029A41C"),
    0x8029A4D0: table.sym("camera_8029A4D0"),
    0x8029A5BC: table.sym("camera_8029A5BC"), # unused
    0x8029A5E8: table.sym("camera_8029A5E8"),
    0x8029A60C: table.sym("camera_8029A60C"),
    0x8029A64C: table.sym("camera_8029A64C"),
    0x8029A670: table.sym("camera_8029A670"),
    0x8029A694: table.sym("camera_8029A694"),
    0x8029A6F4: table.sym("camera_8029A6F4"),
    0x8029A81C: table.sym("camera_8029A81C"), # unused
    0x8029A858: table.sym("camera_8029A858"),
    0x8029A894: table.sym("camera_8029A894"),
    0x8029A8D0: table.sym("camera_8029A8D0"),
    0x8029A968: table.sym("camera_8029A968"),
    0x8029A9A4: table.sym("camera_8029A9A4"),
    0x8029AA3C: table.sym("s_stage_perspective", table.GLOBL), # s callback
    0x8029AAAC: table.sym_fnc("L8029AAAC", flag=table.GLOBL|table.LOCAL),
    0x8029AABC: table.sym_fnc("L8029AABC", flag=table.GLOBL|table.LOCAL),
    0x8029AACC: table.sym_fnc("L8029AACC", flag=table.GLOBL|table.LOCAL),
    0x8029AADC: table.sym_fnc("L8029AADC", flag=table.GLOBL|table.LOCAL),
    0x8029AAEC: table.sym_fnc("L8029AAEC", flag=table.GLOBL|table.LOCAL),
    0x8029AAFC: table.sym_fnc("L8029AAFC", flag=table.GLOBL|table.LOCAL),
    0x8029AB0C: table.sym_fnc("L8029AB0C", flag=table.GLOBL|table.LOCAL),
    0x8029AB1C: table.sym_fnc("L8029AB1C", flag=table.GLOBL|table.LOCAL),
    0x8029AB2C: table.sym_fnc("L8029AB2C", flag=table.GLOBL|table.LOCAL),
    0x8029AB3C: table.sym_fnc("L8029AB3C", flag=table.GLOBL|table.LOCAL),
    0x8029AB4C: table.sym_fnc("L8029AB4C", flag=table.GLOBL|table.LOCAL),
    0x8029AB5C: table.sym_fnc("L8029AB5C", flag=table.GLOBL|table.LOCAL),
    0x8029AB94: table.sym("camera_8029AB94"),
    0x8029ABB0: table.sym("camera_8029ABB0"),
    0x8029AC30: table.sym("camera_8029AC30"),
    0x8029AD80: table.sym("camera_8029AD80"), # unused
    0x8029AE40: table.sym("camera_8029AE40"), # unused
    0x8029AEF8: table.sym("camera_8029AEF8"),
    0x8029AF98: table.sym("camera_8029AF98"),
    0x8029B08C: table.sym("camera_8029B08C", table.GLOBL), # o callback
    0x8029B28C: table.sym("camera_8029B28C"),
    0x8029B358: table.sym("camera_8029B358"),
    0x8029B3C8: table.sym("camera_8029B3C8"),
    0x8029B49C: table.sym("camera_8029B49C", table.GLOBL), # o callback
    0x8029BDE4: table.sym("camera_8029BDE4", table.GLOBL), # o callback
    0x8029BF64: table.sym("camera_8029BF64", table.GLOBL), # o callback
    0x8029C0E4: table.sym("camera_8029C0E4"),
    0x8029C254: table.sym("camera_8029C254", table.GLOBL), # o callback
    0x8029C2FC: table.sym_fnc("L8029C2FC", flag=table.GLOBL|table.LOCAL),
    0x8029C320: table.sym_fnc("L8029C320", flag=table.GLOBL|table.LOCAL),
    0x8029C344: table.sym_fnc("L8029C344", flag=table.GLOBL|table.LOCAL),
    0x8029C554: table.sym_fnc("L8029C554", flag=table.GLOBL|table.LOCAL),
    0x8029C5EC: table.sym_fnc("L8029C5EC", flag=table.GLOBL|table.LOCAL),

    # src/course.c
    0x8029C770: table.sym("course_8029C770", table.GLOBL),

    # src/object.c
    0x8029C780: table.sym("object_8029C780"),
    0x8029C9CC: table.sym("object_8029C9CC"),
    0x8029CA58: table.sym("object_8029CA58", table.GLOBL), # o callback
    0x8029CB34: table.sym("object_8029CB34"),
    0x8029CBC8: table.sym("object_8029CBC8"),
    0x8029CD28: table.sym("object_8029CD28"),
    0x8029CD98: table.sym("object_8029CD98"),
    0x8029CE58: table.sym("object_8029CE58", table.GLOBL),
    0x8029CEDC: table.sym("object_8029CEDC", table.GLOBL),
    0x8029CFB0: table.sym("object_8029CFB0", table.GLOBL),
    0x8029D1D8: table.sym("object_8029D1D8"),
    0x8029D1E8: table.sym("object_8029D1E8", table.GLOBL),
    0x8029D324: table.sym("object_8029D324"),
    0x8029D374: table.sym("object_8029D374"),
    0x8029D428: table.sym("object_8029D428"),
    0x8029D4D0: table.sym("object_8029D4D0"), # unused
    0x8029D690: table.sym("object_8029D690", table.GLOBL),

    # src/obj_lib.c
    0x8029D890: table.sym("s_obj_lib_8029D890", table.GLOBL), # s callback
    0x8029D924: table.sym("s_obj_lib_8029D924", table.GLOBL), # s callback
    0x8029DB48: table.sym("s_obj_lib_8029DB48", table.GLOBL), # s callback
    0x8029DBD4: table.sym("s_obj_lib_8029DBD4", table.GLOBL), # s callback
    0x8029DCD4: table.sym("obj_lib_8029DCD4", table.GLOBL),
    0x8029DDA8: table.sym("obj_lib_8029DDA8", table.GLOBL),
    0x8029DE80: table.sym("obj_lib_8029DE80", table.GLOBL),
    0x8029E1B0: table.sym("obj_lib_8029E1B0", table.GLOBL),
    0x8029E27C: table.sym("obj_lib_8029E27C", table.GLOBL),
    0x8029E2F8: table.sym("obj_lib_8029E2F8", table.GLOBL),
    0x8029E398: table.sym("obj_lib_8029E398", table.GLOBL),
    0x8029E3E8: table.sym("obj_lib_8029E3E8", table.GLOBL),
    0x8029E494: table.sym("obj_lib_8029E494", table.GLOBL),
    0x8029E530: table.sym("obj_lib_8029E530", table.GLOBL),
    0x8029E5EC: table.sym("obj_lib_8029E5EC", table.GLOBL),
    0x8029E694: table.sym("obj_lib_8029E694", table.GLOBL),
    0x8029E714: table.sym("obj_lib_8029E714", table.GLOBL),
    0x8029E8BC: table.sym("obj_lib_8029E8BC", table.GLOBL),
    0x8029E914: table.sym("obj_lib_8029E914", table.GLOBL),
    0x8029E96C: table.sym("obj_lib_8029E96C", table.GLOBL),
    0x8029E9AC: table.sym("obj_lib_8029E9AC", table.GLOBL),
    0x8029EA24: table.sym("obj_lib_8029EA24", table.GLOBL),
    0x8029EAAC: table.sym("obj_lib_8029EAAC"), # unused
    0x8029EB04: table.sym("obj_lib_8029EB04", table.GLOBL),
    0x8029ED20: table.sym("obj_lib_8029ED20", table.GLOBL),
    0x8029EDCC: table.sym_fnc("obj_lib_8029EDCC", "OBJECT *", (
        "OBJECT *",
        "int",
        "const O_SCRIPT *",
    ), table.GLOBL),
    0x8029EE24: table.sym("obj_lib_8029EE24", table.GLOBL),
    0x8029EEB8: table.sym("obj_lib_8029EEB8", table.GLOBL),
    0x8029EF20: table.sym("obj_lib_8029EF20"),
    0x8029EF64: table.sym("obj_lib_8029EF64", table.GLOBL),
    0x8029EFFC: table.sym("obj_lib_8029EFFC", table.GLOBL),
    0x8029F070: table.sym("obj_lib_8029F070"), # unused
    0x8029F0C8: table.sym("obj_lib_8029F0C8", table.GLOBL),
    0x8029F0E0: table.sym("obj_lib_8029F0E0", table.GLOBL),
    0x8029F120: table.sym("obj_lib_8029F120", table.GLOBL),
    0x8029F148: table.sym("obj_lib_8029F148"),
    0x8029F188: table.sym("obj_lib_8029F188", table.GLOBL),
    0x8029F1B0: table.sym("obj_lib_8029F1B0"), # unused
    0x8029F200: table.sym("obj_lib_8029F200", table.GLOBL),
    0x8029F274: table.sym("obj_lib_8029F274", table.GLOBL),
    0x8029F2EC: table.sym("obj_lib_8029F2EC"),
    0x8029F3A8: table.sym("obj_lib_8029F3A8", table.GLOBL),
    0x8029F3D0: table.sym("obj_lib_8029F3D0", table.GLOBL),
    0x8029F404: table.sym("obj_lib_8029F404", table.GLOBL),
    0x8029F430: table.sym("obj_lib_8029F430", table.GLOBL),
    0x8029F464: table.sym("obj_lib_8029F464", table.GLOBL),
    0x8029F4B4: table.sym("obj_lib_8029F4B4", table.GLOBL),
    0x8029F514: table.sym("obj_lib_8029F514", table.GLOBL),
    0x8029F59C: table.sym("obj_lib_8029F59C", table.GLOBL),
    0x8029F600: table.sym("obj_lib_8029F600"), # unused
    0x8029F620: table.sym("obj_lib_8029F620", table.GLOBL),
    0x8029F644: table.sym("obj_lib_8029F644"), # unused
    0x8029F66C: table.sym("obj_lib_8029F66C", table.GLOBL),
    0x8029F694: table.sym("obj_lib_8029F694", table.GLOBL),
    0x8029F6BC: table.sym("obj_lib_8029F6BC", table.GLOBL),
    0x8029F6E0: table.sym("obj_lib_8029F6E0", table.GLOBL),
    0x8029F7D8: table.sym("obj_lib_8029F7D8"),
    0x8029F820: table.sym("obj_lib_8029F820", table.GLOBL),
    0x8029F848: table.sym("obj_lib_8029F848"), # unused
    0x8029F8EC: table.sym("obj_lib_8029F8EC", table.GLOBL),
    0x8029F914: table.sym("obj_lib_8029F914", table.GLOBL),
    0x8029F95C: table.sym("obj_lib_8029F95C", table.GLOBL),
    0x8029F998: table.sym("obj_lib_8029F998", table.GLOBL),
    0x8029F9EC: table.sym("obj_lib_8029F9EC", table.GLOBL),
    0x8029FB1C: table.sym("obj_lib_8029FB1C", table.GLOBL),
    0x8029FB68: table.sym("obj_lib_8029FB68"), # unused
    0x8029FBDC: table.sym("obj_lib_8029FBDC", table.GLOBL),
    0x8029FC9C: table.sym("obj_lib_8029FC9C", table.GLOBL),
    0x8029FD8C: table.sym("obj_lib_8029FD8C"),
    0x8029FDB4: table.sym("obj_lib_8029FDB4", table.GLOBL),
    0x8029FE00: table.sym("obj_lib_8029FE00", table.GLOBL),
    0x8029FE6C: table.sym("obj_lib_8029FE6C", table.GLOBL),
    0x8029FEA4: table.sym("obj_lib_8029FEA4", table.GLOBL),
    0x8029FF04: table.sym("obj_lib_8029FF04", table.GLOBL),
    0x8029FFA4: table.sym("obj_lib_8029FFA4", table.GLOBL),
    0x802A0008: table.sym_fnc("obj_lib_802A0008", "int", (
        "int",
    ), table.GLOBL),
    0x802A0050: table.sym("obj_lib_802A0050", table.GLOBL),
    0x802A00AC: table.sym("obj_lib_802A00AC"), # unused
    0x802A0114: table.sym("obj_lib_802A0114", table.GLOBL),
    0x802A0154: table.sym("obj_lib_802A0154", table.GLOBL),
    0x802A0198: table.sym("obj_lib_802A0198", table.GLOBL),
    0x802A01D8: table.sym("obj_lib_802A01D8", table.GLOBL),
    0x802A0234: table.sym("obj_lib_802A0234"),
    0x802A0380: table.sym("obj_lib_802A0380", table.GLOBL),
    0x802A0474: table.sym("obj_lib_802A0474", table.GLOBL),
    0x802A04C0: table.sym("obj_lib_802A04C0", table.GLOBL),
    0x802A04F0: table.sym("obj_lib_802A04F0"), # unused
    0x802A0514: table.sym("obj_lib_802A0514", table.GLOBL),
    0x802A0568: table.sym("obj_lib_802A0568", table.GLOBL),
    0x802A057C: table.sym("obj_lib_802A057C", table.GLOBL),
    0x802A05B4: table.sym("obj_lib_802A05B4", table.GLOBL),
    0x802A05D4: table.sym("obj_lib_802A05D4", table.GLOBL),
    0x802A05F0: table.sym("obj_lib_802A05F0", table.GLOBL),
    0x802A0604: table.sym("obj_lib_802A0604", table.GLOBL),
    0x802A064C: table.sym("obj_lib_802A064C", table.GLOBL),
    0x802A069C: table.sym("obj_lib_802A069C"),
    0x802A079C: table.sym("obj_lib_802A079C", table.GLOBL),
    0x802A07E8: table.sym("obj_lib_802A07E8"),
    0x802A0AB0: table.sym("obj_lib_802A0AB0"),
    0x802A0BDC: table.sym("obj_lib_802A0BDC"),
    0x802A0D84: table.sym("obj_lib_802A0D84"),
    0x802A0E68: table.sym("obj_lib_802A0E68", table.GLOBL),
    0x802A10E0: table.sym("obj_lib_802A10E0"), # unused
    0x802A10F0: table.sym("obj_lib_802A10F0"),
    0x802A113C: table.sym("obj_lib_802A113C"), # unused
    0x802A11A8: table.sym("obj_lib_802A11A8", table.GLOBL),
    0x802A120C: table.sym("obj_lib_802A120C", table.GLOBL),
    0x802A12A4: table.sym("obj_lib_802A12A4", table.GLOBL),
    0x802A1308: table.sym("obj_lib_802A1308", table.GLOBL), # o callback
    0x802A1370: table.sym("obj_lib_802A1370", table.GLOBL),
    0x802A1424: table.sym("obj_lib_802A1424", table.GLOBL),
    0x802A148C: table.sym("obj_lib_802A148C", table.GLOBL),
    0x802A14C4: table.sym("obj_lib_802A14C4", table.GLOBL),
    0x802A14FC: table.sym("obj_lib_802A14FC", table.GLOBL),
    0x802A1554: table.sym("obj_lib_802A1554", table.GLOBL),
    0x802A15AC: table.sym("obj_lib_802A15AC", table.GLOBL),
    0x802A1634: table.sym("obj_lib_802A1634", table.GLOBL),
    0x802A16AC: table.sym("obj_lib_802A16AC"), # unused
    0x802A1774: table.sym("obj_lib_802A1774"), # unused
    0x802A184C: table.sym("obj_lib_802A184C", table.GLOBL),
    0x802A188C: table.sym("obj_lib_802A188C", table.GLOBL),
    0x802A18DC: table.sym("obj_lib_802A18DC", table.GLOBL),
    0x802A1930: table.sym("obj_lib_802A1930", table.GLOBL),
    0x802A1960: table.sym("obj_lib_802A1960"), # unused
    0x802A19AC: table.sym("obj_lib_802A19AC", table.GLOBL),
    0x802A19C8: table.sym("obj_lib_802A19C8", table.GLOBL),
    0x802A19F0: table.sym("obj_lib_802A19F0", table.GLOBL),
    0x802A1A18: table.sym("obj_lib_802A1A18"),
    0x802A1B34: table.sym("obj_lib_802A1B34"),
    0x802A1B8C: table.sym("obj_lib_802A1B8C", table.GLOBL),
    0x802A1BDC: table.sym("obj_lib_802A1BDC", table.GLOBL),
    0x802A1C68: table.sym("obj_lib_802A1C68"), # unused
    0x802A1CC4: table.sym("obj_lib_802A1CC4"), # unused
    0x802A1D7C: table.sym("obj_lib_802A1D7C"),
    0x802A1F3C: table.sym("obj_lib_802A1F3C", table.GLOBL),
    0x802A20F4: table.sym("obj_lib_802A20F4"),
    0x802A21D4: table.sym("obj_lib_802A21D4"),
    0x802A2320: table.sym("obj_lib_802A2320", table.GLOBL), # o callback
    0x802A2348: table.sym("obj_lib_802A2348", table.GLOBL),
    0x802A24D0: table.sym("obj_lib_802A24D0"),
    0x802A25B4: table.sym("obj_lib_802A25B4", table.GLOBL),
    0x802A2644: table.sym("obj_lib_802A2644", table.GLOBL), # o callback
    0x802A2674: table.sym("obj_lib_802A2674"), # unused
    0x802A2748: table.sym("obj_lib_802A2748", table.GLOBL),
    0x802A27B0: table.sym("obj_lib_802A27B0", table.GLOBL),
    0x802A2804: table.sym("obj_lib_802A2804", table.GLOBL),
    0x802A2930: table.sym("obj_lib_802A2930", table.GLOBL),
    0x802A2A18: table.sym("obj_lib_802A2A18", table.GLOBL),
    0x802A2A84: table.sym("obj_lib_802A2A84", table.GLOBL),
    0x802A2B28: table.sym("obj_lib_802A2B28"), # unused
    0x802A2B6C: table.sym("obj_lib_802A2B6C"), # unused
    0x802A2BC4: table.sym("obj_lib_802A2BC4", table.GLOBL), # o callback
    0x802A2C1C: table.sym("obj_lib_802A2C1C"), # unused
    0x802A2C5C: table.sym("obj_lib_802A2C5C", table.GLOBL),
    0x802A2ED4: table.sym("obj_lib_802A2ED4", table.GLOBL),
    0x802A2F14: table.sym("obj_lib_802A2F14", table.GLOBL),
    0x802A2F5C: table.sym("obj_lib_802A2F5C", table.GLOBL),
    0x802A2FC0: table.sym("obj_lib_802A2FC0", table.GLOBL),
    0x802A308C: table.sym("obj_lib_802A308C", table.GLOBL),
    0x802A3124: table.sym("obj_lib_802A3124"),
    0x802A31E0: table.sym("obj_lib_802A31E0", table.GLOBL),
    0x802A3268: table.sym("obj_lib_802A3268", table.GLOBL),
    0x802A32AC: table.sym("obj_lib_802A32AC", table.GLOBL),
    0x802A34A4: table.sym("obj_lib_802A34A4", table.GLOBL),
    0x802A3604: table.sym("obj_lib_802A3604", table.GLOBL),
    0x802A3634: table.sym("obj_lib_802A3634", table.GLOBL),
    0x802A3674: table.sym("obj_lib_802A3674", table.GLOBL),
    0x802A36A4: table.sym("obj_lib_802A36A4", table.GLOBL),
    0x802A3754: table.sym("obj_lib_802A3754", table.GLOBL),
    0x802A37AC: table.sym("obj_lib_802A37AC", table.GLOBL),
    0x802A37DC: table.sym("obj_lib_802A37DC", table.GLOBL),
    0x802A3818: table.sym("obj_lib_802A3818", table.GLOBL),
    0x802A390C: table.sym("obj_lib_802A390C", table.GLOBL),
    0x802A399C: table.sym("obj_lib_802A399C", table.GLOBL), # o callback
    0x802A3A3C: table.sym("obj_lib_802A3A3C"), # unused
    0x802A3A4C: table.sym("obj_lib_802A3A4C", table.GLOBL),
    0x802A3A88: table.sym("obj_lib_802A3A88", table.GLOBL),
    0x802A3B28: table.sym("obj_lib_802A3B28"), # unused
    0x802A3B40: table.sym("obj_lib_802A3B40", table.GLOBL),
    0x802A3C18: table.sym("obj_lib_802A3C18", table.GLOBL),
    0x802A3CEC: table.sym("obj_lib_802A3CEC"), # unused
    0x802A3CFC: table.sym("obj_lib_802A3CFC", table.GLOBL),
    0x802A3D40: table.sym("obj_lib_802A3D40"), # unused
    0x802A3DD4: table.sym("obj_lib_802A3DD4", table.GLOBL),
    0x802A3E30: table.sym("obj_lib_802A3E30", table.GLOBL),
    0x802A3E80: table.sym("obj_lib_802A3E80"),
    0x802A3EF8: table.sym("obj_lib_802A3EF8"), # unused
    0x802A3F24: table.sym("obj_lib_802A3F24", table.GLOBL),
    0x802A3F48: table.sym("obj_lib_802A3F48", table.GLOBL),
    0x802A404C: table.sym("obj_lib_802A404C", table.GLOBL),
    0x802A40B8: table.sym("obj_lib_802A40B8", table.GLOBL),
    0x802A4110: table.sym("obj_lib_802A4110"), # unused
    0x802A4120: table.sym("obj_lib_802A4120", table.GLOBL), # o callback
    0x802A4210: table.sym("obj_lib_802A4210", table.GLOBL),
    0x802A4360: table.sym("obj_lib_802A4360", table.GLOBL),
    0x802A4440: table.sym("obj_lib_802A4440", table.GLOBL),
    0x802A44F4: table.sym("obj_lib_802A44F4", table.GLOBL),
    0x802A452C: table.sym("obj_lib_802A452C", table.GLOBL),
    0x802A4564: table.sym("obj_lib_802A4564", table.GLOBL),
    0x802A45E4: table.sym("s_obj_lib_802A45E4", table.GLOBL), # s callback
    0x802A462C: table.sym("obj_lib_802A462C"), # unused
    0x802A46CC: table.sym("obj_lib_802A46CC", table.GLOBL),
    0x802A4704: table.sym("obj_lib_802A4704", table.GLOBL),
    0x802A4728: table.sym("obj_lib_802A4728", table.GLOBL),
    0x802A4750: table.sym("obj_lib_802A4750", table.GLOBL),
    0x802A4774: table.sym("obj_lib_802A4774", table.GLOBL),
    0x802A47A0: table.sym("obj_lib_802A47A0", table.GLOBL),
    0x802A48BC: table.sym("obj_lib_802A48BC", table.GLOBL),
    0x802A48FC: table.sym("obj_lib_802A48FC"),
    0x802A4960: table.sym("obj_lib_802A4960", table.GLOBL),
    0x802A49B4: table.sym_fnc("L802A49B4", flag=table.GLOBL|table.LOCAL),
    0x802A4A28: table.sym_fnc("L802A4A28", flag=table.GLOBL|table.LOCAL),
    0x802A4A58: table.sym_fnc("L802A4A58", flag=table.GLOBL|table.LOCAL),
    0x802A4AAC: table.sym_fnc("L802A4AAC", flag=table.GLOBL|table.LOCAL),
    0x802A4B30: table.sym_fnc("L802A4B30", flag=table.GLOBL|table.LOCAL),
    0x802A4BE4: table.sym("obj_lib_802A4BE4", table.GLOBL),
    0x802A4F04: table.sym("obj_lib_802A4F04", table.GLOBL),
    0x802A4F58: table.sym("obj_lib_802A4F58", table.GLOBL),
    0x802A5034: table.sym("obj_lib_802A5034"), # unused
    0x802A50FC: table.sym("obj_lib_802A50FC", table.GLOBL),
    0x802A513C: table.sym("obj_lib_802A513C", table.GLOBL),
    0x802A51AC: table.sym("obj_lib_802A51AC", table.GLOBL),
    0x802A5228: table.sym("obj_lib_802A5228", table.GLOBL),
    0x802A5248: table.sym("obj_lib_802A5248", table.GLOBL),
    0x802A5288: table.sym("obj_lib_802A5288", table.GLOBL),
    0x802A52C4: table.sym("obj_lib_802A52C4", table.GLOBL),
    0x802A52F8: table.sym("obj_lib_802A52F8", table.GLOBL),
    0x802A5358: table.sym("obj_lib_802A5358", table.GLOBL),
    0x802A540C: table.sym("obj_lib_802A540C"), # unused
    0x802A5460: table.sym("obj_lib_802A5460"), # unused
    0x802A5498: table.sym("obj_lib_802A5498", table.GLOBL),
    0x802A54D8: table.sym("obj_lib_802A54D8", table.GLOBL),
    0x802A5524: table.sym("obj_lib_802A5524", table.GLOBL),
    0x802A5588: table.sym("obj_lib_802A5588", table.GLOBL),

    # src/object_a.c
    0x802A5620: table.sym("object_a_802A5620"),
    0x802A56BC: table.sym("object_a_802A56BC", table.GLOBL), # o callback
    0x802A5704: table.sym_fnc("L802A5704", flag=table.GLOBL|table.LOCAL),
    0x802A5768: table.sym_fnc("L802A5768", flag=table.GLOBL|table.LOCAL),
    0x802A57F0: table.sym_fnc("L802A57F0", flag=table.GLOBL|table.LOCAL),
    0x802A5824: table.sym_fnc("L802A5824", flag=table.GLOBL|table.LOCAL),
    0x802A58A4: table.sym_fnc("L802A58A4", flag=table.GLOBL|table.LOCAL),
    0x802A58DC: table.sym("object_a_802A58DC", table.GLOBL), # o callback
    0x802A597C: table.sym_fnc("object_a_802A597C", flag=table.GLOBL), # data
    0x802A5A44: table.sym_fnc("object_a_802A5A44", flag=table.GLOBL), # data
    0x802A5AA0: table.sym("object_a_802A5AA0", table.GLOBL), # o callback
    0x802A5ACC: table.sym("object_a_802A5ACC"),
    0x802A5BD4: table.sym("object_a_802A5BD4", table.GLOBL), # o callback
    0x802A5D4C: table.sym_fnc("object_a_802A5D4C", flag=table.GLOBL), # data
    0x802A6518: table.sym_fnc("object_a_802A6518", flag=table.GLOBL), # data
    0x802A68A0: table.sym_fnc("object_a_802A68A0", flag=table.GLOBL), # data
    0x802A6AD8: table.sym_fnc("object_a_802A6AD8", flag=table.GLOBL), # data
    0x802A6B7C: table.sym("object_a_802A6B7C", table.GLOBL), # o callback
    0x802A6C20: table.sym("object_a_802A6C20", table.GLOBL), # o callback
    0x802A6C74: table.sym("object_a_802A6C74", table.GLOBL), # o callback
    0x802A6CF4: table.sym("object_a_802A6CF4", table.GLOBL), # o callback
    0x802A6D64: table.sym("object_a_802A6D64", table.GLOBL), # o callback
    0x802A6EE4: table.sym_fnc("object_a_802A6EE4", flag=table.GLOBL), # data
    0x802A7020: table.sym_fnc("object_a_802A7020", flag=table.GLOBL), # data
    0x802A708C: table.sym_fnc("object_a_802A708C", flag=table.GLOBL), # data
    0x802A7160: table.sym_fnc("object_a_802A7160", flag=table.GLOBL), # data
    0x802A7170: table.sym("object_a_802A7170", table.GLOBL), # o callback
    0x802A719C: table.sym("s_object_a_802A719C", table.GLOBL), # s callback
    0x802A7230: table.sym("object_a_802A7230", table.GLOBL), # o callback
    0x802A7264: table.sym_fnc("object_a_802A7264", flag=table.GLOBL), # data
    0x802A7384: table.sym("object_a_802A7384"),
    0x802A73D8: table.sym_fnc("object_a_802A73D8", flag=table.GLOBL), # data
    0x802A7598: table.sym_fnc("object_a_802A7598", flag=table.GLOBL), # data
    0x802A7804: table.sym_fnc("object_a_802A7804", flag=table.GLOBL), # data
    0x802A78D8: table.sym_fnc("object_a_802A78D8", flag=table.GLOBL), # data
    0x802A7A60: table.sym_fnc("object_a_802A7A60", flag=table.GLOBL), # data
    0x802A7B1C: table.sym_fnc("object_a_802A7B1C", flag=table.GLOBL), # data
    0x802A7B5C: table.sym_fnc("object_a_802A7B5C", flag=table.GLOBL), # data
    0x802A7D14: table.sym_fnc("object_a_802A7D14", flag=table.GLOBL), # data
    0x802A7D4C: table.sym_fnc("L802A7D4C", flag=table.GLOBL|table.LOCAL),
    0x802A7E08: table.sym_fnc("L802A7E08", flag=table.GLOBL|table.LOCAL),
    0x802A7EDC: table.sym_fnc("L802A7EDC", flag=table.GLOBL|table.LOCAL),
    0x802A7F08: table.sym_fnc("L802A7F08", flag=table.GLOBL|table.LOCAL),
    0x802A7F70: table.sym_fnc("L802A7F70", flag=table.GLOBL|table.LOCAL),
    0x802A7FBC: table.sym("object_a_802A7FBC"),
    0x802A8064: table.sym("object_a_802A8064", table.GLOBL), # o callback
    0x802A816C: table.sym("object_a_802A816C", table.GLOBL), # o callback
    0x802A81E8: table.sym("object_a_802A81E8", table.GLOBL), # o callback
    0x802A821C: table.sym("object_a_802A821C", table.GLOBL), # o callback
    0x802A8370: table.sym("object_a_802A8370", table.GLOBL), # o callback
    0x802A83A0: table.sym("object_a_802A83A0", table.GLOBL), # o callback
    0x802A8630: table.sym("object_a_802A8630", table.GLOBL), # o callback
    0x802A86BC: table.sym("object_a_802A86BC"), # unused
    0x802A870C: table.sym("object_a_802A870C", table.GLOBL), # o callback
    0x802A88A4: table.sym("object_a_802A88A4", table.GLOBL), # o callback
    0x802A8A38: table.sym("object_a_802A8A38"),
    0x802A8B18: table.sym("object_a_802A8B18", table.GLOBL), # o callback
    0x802A8BC0: table.sym("object_a_802A8BC0", table.GLOBL), # o callback
    0x802A8C88: table.sym("object_a_802A8C88", table.GLOBL), # o callback
    0x802A8CDC: table.sym("object_a_802A8CDC", table.GLOBL), # o callback
    0x802A8D48: table.sym("object_a_802A8D48", table.GLOBL), # o callback
    0x802A8D98: table.sym("object_a_802A8D98", table.GLOBL), # o callback
    0x802A8DC0: table.sym_fnc("object_a_802A8DC0", flag=table.GLOBL), # data
    0x802A8F40: table.sym_fnc("object_a_802A8F40", flag=table.GLOBL), # data
    0x802A9114: table.sym_fnc("object_a_802A9114", flag=table.GLOBL), # data
    0x802A92FC: table.sym_fnc("object_a_802A92FC", flag=table.GLOBL), # data
    0x802A93F8: table.sym_fnc("object_a_802A93F8", flag=table.GLOBL), # data
    0x802A9440: table.sym_fnc("object_a_802A9440", flag=table.GLOBL), # data
    0x802A9460: table.sym_fnc("object_a_802A9460", flag=table.GLOBL), # data
    0x802A9498: table.sym("object_a_802A9498", table.GLOBL), # o callback
    0x802A94F8: table.sym("object_a_802A94F8", table.GLOBL), # o callback
    0x802A958C: table.sym("object_a_802A958C"),
    0x802A9708: table.sym("object_a_802A9708", table.GLOBL), # o callback
    0x802A973C: table.sym("object_a_802A973C"), # unused
    0x802A98C4: table.sym("object_a_802A98C4"),
    0x802A9994: table.sym_fnc("object_a_802A9994", flag=table.GLOBL), # data
    0x802A9D08: table.sym_fnc("object_a_802A9D08", flag=table.GLOBL), # data
    0x802A9F54: table.sym_fnc("object_a_802A9F54", flag=table.GLOBL), # data
    0x802A9FC8: table.sym_fnc("object_a_802A9FC8", flag=table.GLOBL), # data
    0x802AA02C: table.sym("object_a_802AA02C"),
    0x802AA0AC: table.sym("object_a_802AA0AC", table.GLOBL), # o callback
    0x802AA1B8: table.sym("object_a_802AA1B8", table.GLOBL), # o callback
    0x802AA280: table.sym("object_a_802AA280"),
    0x802AA3C8: table.sym("object_a_802AA3C8"),
    0x802AA3F4: table.sym("object_a_802AA3F4", table.GLOBL), # o callback
    0x802AA700: table.sym("object_a_802AA700", table.GLOBL), # o callback
    0x802AA774: table.sym("object_a_802AA774", table.GLOBL), # o callback
    0x802AA830: table.sym("object_a_802AA830", table.GLOBL), # o callback
    0x802AA948: table.sym("object_a_802AA948"),
    0x802AA97C: table.sym("object_a_802AA97C", table.GLOBL), # o callback
    0x802AAA60: table.sym("object_a_802AAA60", table.GLOBL), # o callback
    0x802AAB54: table.sym("object_a_802AAB54", table.GLOBL), # o callback
    0x802AAC48: table.sym("object_a_802AAC48", table.GLOBL), # o callback
    0x802AAE8C: table.sym("object_a_802AAE8C", table.GLOBL),
    0x802AAF48: table.sym("object_a_802AAF48", table.GLOBL), # o callback
    0x802AAFFC: table.sym("object_a_802AAFFC"),
    0x802AB060: table.sym("object_a_802AB060"),
    0x802AB158: table.sym("object_a_802AB158"),
    0x802AB18C: table.sym("object_a_802AB18C"),
    0x802AB1C8: table.sym("object_a_802AB1C8", table.GLOBL), # o callback
    0x802AB558: table.sym("object_a_802AB558", table.GLOBL),
    0x802AB5C8: table.sym("object_a_802AB5C8"),
    0x802AB650: table.sym("object_a_802AB650", table.GLOBL), # o callback
    0x802AB70C: table.sym("object_a_802AB70C", table.GLOBL), # o callback
    0x802AB748: table.sym("object_a_802AB748", table.GLOBL), # o callback
    0x802AB7A4: table.sym("object_a_802AB7A4", table.GLOBL), # o callback
    0x802AB860: table.sym("object_a_802AB860", table.GLOBL), # o callback
    0x802ABA40: table.sym("object_a_802ABA40", table.GLOBL), # o callback
    0x802ABC04: table.sym("object_a_802ABC04"),
    0x802ABC70: table.sym_fnc("L802ABC70", flag=table.GLOBL|table.LOCAL),
    0x802ABCA8: table.sym_fnc("L802ABCA8", flag=table.GLOBL|table.LOCAL),
    0x802ABCF8: table.sym_fnc("L802ABCF8", flag=table.GLOBL|table.LOCAL),
    0x802ABD88: table.sym_fnc("L802ABD88", flag=table.GLOBL|table.LOCAL),
    0x802ABE20: table.sym_fnc("L802ABE20", flag=table.GLOBL|table.LOCAL),
    0x802ABEE4: table.sym("object_a_802ABEE4", table.GLOBL), # o callback
    0x802ABF0C: table.sym("object_a_802ABF0C", table.GLOBL), # o callback
    0x802AC068: table.sym_fnc("object_a_802AC068", flag=table.GLOBL), # data
    0x802AC15C: table.sym_fnc("object_a_802AC15C", flag=table.GLOBL), # data
    0x802AC294: table.sym("object_a_802AC294", table.GLOBL), # o callback
    0x802AC2C0: table.sym("object_a_802AC2C0", table.GLOBL), # o callback
    0x802AC2EC: table.sym("object_a_802AC2EC", table.GLOBL), # o callback
    0x802AC3A8: table.sym("object_a_802AC3A8", table.GLOBL), # o callback
    0x802AC4A0: table.sym("object_a_802AC4A0", table.GLOBL), # o callback
    0x802AC5B4: table.sym("object_a_802AC5B4", table.GLOBL), # o callback
    0x802AC678: table.sym("object_a_802AC678", table.GLOBL), # o callback
    0x802AC78C: table.sym("object_a_802AC78C", table.GLOBL), # o callback
    0x802AC864: table.sym("object_a_802AC864", table.GLOBL), # o callback
    0x802AC910: table.sym("object_a_802AC910"),
    0x802AC958: table.sym("object_a_802AC958"),
    0x802AC9D0: table.sym("object_a_802AC9D0"),
    0x802ACA6C: table.sym("object_a_802ACA6C"),
    0x802ACAC8: table.sym("object_a_802ACAC8", table.GLOBL), # o callback
    0x802ACB90: table.sym_fnc("L802ACB90", flag=table.GLOBL|table.LOCAL),
    0x802ACBA0: table.sym_fnc("L802ACBA0", flag=table.GLOBL|table.LOCAL),
    0x802ACBB8: table.sym_fnc("L802ACBB8", flag=table.GLOBL|table.LOCAL),
    0x802ACBD0: table.sym_fnc("L802ACBD0", flag=table.GLOBL|table.LOCAL),
    0x802ACBE8: table.sym_fnc("L802ACBE8", flag=table.GLOBL|table.LOCAL),
    0x802ACC3C: table.sym("object_a_802ACC3C", table.GLOBL), # o callback
    0x802ACE80: table.sym("object_a_802ACE80", table.GLOBL), # o callback
    0x802AD078: table.sym_fnc("object_a_802AD078", flag=table.GLOBL), # data
    0x802AD10C: table.sym_fnc("object_a_802AD10C", flag=table.GLOBL), # data
    0x802AD1A4: table.sym_fnc("object_a_802AD1A4", flag=table.GLOBL), # data
    0x802AD238: table.sym_fnc("object_a_802AD238", flag=table.GLOBL), # data
    0x802AD2D0: table.sym_fnc("object_a_802AD2D0", flag=table.GLOBL), # data
    0x802AD34C: table.sym("object_a_802AD34C", table.GLOBL), # o callback
    0x802AD378: table.sym("object_a_802AD378", table.GLOBL), # o callback
    0x802AD580: table.sym_fnc("object_a_802AD580", flag=table.GLOBL), # data
    0x802AD76C: table.sym_fnc("object_a_802AD76C", flag=table.GLOBL), # data
    0x802AD7F4: table.sym_fnc("object_a_802AD7F4", flag=table.GLOBL), # data
    0x802AD828: table.sym_fnc("object_a_802AD828", flag=table.GLOBL), # data
    0x802AD890: table.sym("object_a_802AD890", table.GLOBL), # o callback
    0x802AD8BC: table.sym("object_a_802AD8BC"),
    0x802AD8F0: table.sym_fnc("object_a_802AD8F0", flag=table.GLOBL), # data
    0x802ADA4C: table.sym_fnc("object_a_802ADA4C", flag=table.GLOBL), # data
    0x802ADB88: table.sym_fnc("object_a_802ADB88", flag=table.GLOBL), # data
    0x802ADCE4: table.sym_fnc("object_a_802ADCE4", flag=table.GLOBL), # data
    0x802ADD70: table.sym_fnc("object_a_802ADD70", flag=table.GLOBL), # data
    0x802ADDF8: table.sym("object_a_802ADDF8", table.GLOBL), # o callback
    0x802ADF6C: table.sym("object_a_802ADF6C", table.GLOBL), # o callback
    0x802ADF98: table.sym("object_a_802ADF98", table.GLOBL), # o callback
    0x802ADFD8: table.sym("object_a_802ADFD8", table.GLOBL), # o callback
    0x802AE0CC: table.sym("object_a_802AE0CC", table.GLOBL),
    0x802AE238: table.sym("object_a_802AE238", table.GLOBL), # o callback
    0x802AE304: table.sym("object_a_802AE304", table.GLOBL), # o callback
    0x802AE334: table.sym("object_a_802AE334", table.GLOBL),
    0x802AE360: table.sym("object_a_802AE360", table.GLOBL), # o callback
    0x802AE394: table.sym("object_a_802AE394"), # unused
    0x802AE45C: table.sym("object_a_802AE45C"),
    0x802AE48C: table.sym("object_a_802AE48C", table.GLOBL), # o callback
    0x802AE4C0: table.sym("object_a_802AE4C0", table.GLOBL),
    0x802AE534: table.sym("object_a_802AE534", table.GLOBL), # o callback
    0x802AE85C: table.sym("object_a_802AE85C", table.GLOBL), # o callback
    0x802AE908: table.sym("object_a_802AE908", table.GLOBL), # o callback
    0x802AEA6C: table.sym_fnc("object_a_802AEA6C", flag=table.GLOBL), # data
    0x802AEAB8: table.sym_fnc("object_a_802AEAB8", flag=table.GLOBL), # data
    0x802AEB1C: table.sym_fnc("object_a_802AEB1C", flag=table.GLOBL), # data
    0x802AEB74: table.sym_fnc("object_a_802AEB74", flag=table.GLOBL), # data
    0x802AEB9C: table.sym("object_a_802AEB9C", table.GLOBL), # o callback
    0x802AEBC8: table.sym("object_a_802AEBC8", table.GLOBL), # o callback
    0x802AEC40: table.sym("object_a_802AEC40", table.GLOBL), # o callback
    0x802AECA8: table.sym("object_a_802AECA8", table.GLOBL), # o callback
    0x802AECDC: table.sym("object_a_802AECDC", table.GLOBL), # o callback
    0x802AEDC0: table.sym("object_a_802AEDC0", table.GLOBL), # o callback
    0x802AEE34: table.sym_fnc("L802AEE34", flag=table.GLOBL|table.LOCAL),
    0x802AEE68: table.sym_fnc("L802AEE68", flag=table.GLOBL|table.LOCAL),
    0x802AEE70: table.sym_fnc("L802AEE70", flag=table.GLOBL|table.LOCAL),
    0x802AEEA4: table.sym("object_a_802AEEA4", table.GLOBL), # o callback
    0x802AEF1C: table.sym("object_a_802AEF1C", table.GLOBL), # o callback
    0x802AF1E8: table.sym("object_a_802AF1E8", table.GLOBL), # o callback
    0x802AF3FC: table.sym("object_a_802AF3FC", table.GLOBL), # o callback
    0x802AF448: table.sym("object_a_802AF448", table.GLOBL), # o callback
    0x802AF5F8: table.sym("object_a_802AF5F8", table.GLOBL), # o callback
    0x802AF7C4: table.sym("object_a_802AF7C4", table.GLOBL), # o callback
    0x802AF9CC: table.sym("object_a_802AF9CC", table.GLOBL), # o callback
    0x802AFA0C: table.sym("object_a_802AFA0C", table.GLOBL), # o callback
    0x802AFAE4: table.sym("object_a_802AFAE4", table.GLOBL), # o callback
    0x802AFBF8: table.sym("object_a_802AFBF8", table.GLOBL), # o callback
    0x802AFCE4: table.sym("object_a_802AFCE4", table.GLOBL), # o callback
    0x802AFD1C: table.sym("object_a_802AFD1C", table.GLOBL), # o callback
    0x802AFEE8: table.sym("object_a_802AFEE8", table.GLOBL), # o callback
    0x802AFF30: table.sym("object_a_802AFF30", table.GLOBL), # o callback
    0x802B00E4: table.sym("object_a_802B00E4", table.GLOBL), # o callback
    0x802B0244: table.sym("object_a_802B0244"),
    0x802B039C: table.sym("object_a_802B039C"),
    0x802B04B4: table.sym("object_a_802B04B4", table.GLOBL), # o callback
    0x802B0614: table.sym("object_a_802B0614", table.GLOBL), # o callback
    0x802B0974: table.sym("object_a_802B0974", table.GLOBL), # o callback
    0x802B0B9C: table.sym("object_a_802B0B9C"),
    0x802B0BEC: table.sym("object_a_802B0BEC", table.GLOBL), # o callback
    0x802B0C3C: table.sym_fnc("L802B0C3C", flag=table.GLOBL|table.LOCAL),
    0x802B0C5C: table.sym_fnc("L802B0C5C", flag=table.GLOBL|table.LOCAL),
    0x802B0C8C: table.sym_fnc("L802B0C8C", flag=table.GLOBL|table.LOCAL),
    0x802B0CBC: table.sym_fnc("L802B0CBC", flag=table.GLOBL|table.LOCAL),
    0x802B0CEC: table.sym_fnc("L802B0CEC", flag=table.GLOBL|table.LOCAL),
    0x802B0D48: table.sym("object_a_802B0D48", table.GLOBL), # o callback
    0x802B0DF0: table.sym("object_a_802B0DF0", table.GLOBL), # o callback
    0x802B1278: table.sym("object_a_802B1278", table.GLOBL), # o callback
    0x802B12B0: table.sym_fnc("L802B12B0", flag=table.GLOBL|table.LOCAL),
    0x802B1344: table.sym_fnc("L802B1344", flag=table.GLOBL|table.LOCAL),
    0x802B13A0: table.sym_fnc("L802B13A0", flag=table.GLOBL|table.LOCAL),
    0x802B1470: table.sym_fnc("L802B1470", flag=table.GLOBL|table.LOCAL),
    0x802B14B4: table.sym_fnc("L802B14B4", flag=table.GLOBL|table.LOCAL),
    0x802B14F4: table.sym("object_a_802B14F4"),
    0x802B15E8: table.sym("object_a_802B15E8", table.GLOBL), # o callback
    0x802B1714: table.sym("object_a_802B1714"),
    0x802B17F4: table.sym("object_a_802B17F4"),
    0x802B19D8: table.sym("object_a_802B19D8"),
    0x802B1AE0: table.sym("object_a_802B1AE0", table.GLOBL), # o callback
    0x802B1B2C: table.sym("object_a_802B1B2C", table.GLOBL), # o callback
    0x802B1BB0: table.sym("s_mario_pos_child", table.GLOBL), # s callback
    0x802B1C54: table.sym("object_a_802B1C54", table.GLOBL), # o callback
    0x802B1D7C: table.sym_fnc("object_a_802B1D7C", flag=table.GLOBL), # data
    0x802B1E6C: table.sym_fnc("object_a_802B1E6C", flag=table.GLOBL), # data
    0x802B1FF4: table.sym_fnc("object_a_802B1FF4", flag=table.GLOBL), # data
    0x802B20A0: table.sym_fnc("object_a_802B20A0", flag=table.GLOBL), # data
    0x802B2154: table.sym("object_a_802B2154"),
    0x802B2278: table.sym("object_a_802B2278", table.GLOBL), # o callback
    0x802B2340: table.sym("object_a_802B2340", table.GLOBL), # o callback
    0x802B23E0: table.sym("object_a_802B23E0", table.GLOBL), # o callback
    0x802B2494: table.sym("object_a_802B2494", table.GLOBL), # o callback
    0x802B25AC: table.sym("object_a_802B25AC", table.GLOBL), # o callback
    0x802B26A4: table.sym_fnc("object_a_802B26A4", flag=table.GLOBL), # data
    0x802B27D8: table.sym_fnc("object_a_802B27D8", flag=table.GLOBL), # data
    0x802B2824: table.sym("object_a_802B2824"),
    0x802B288C: table.sym("object_a_802B288C", table.GLOBL), # o callback
    0x802B29B8: table.sym("object_a_802B29B8", table.GLOBL), # o callback
    0x802B2A04: table.sym_fnc("L802B2A04", flag=table.GLOBL|table.LOCAL),
    0x802B2A8C: table.sym_fnc("L802B2A8C", flag=table.GLOBL|table.LOCAL),
    0x802B2B24: table.sym_fnc("L802B2B24", flag=table.GLOBL|table.LOCAL),
    0x802B2B74: table.sym_fnc("L802B2B74", flag=table.GLOBL|table.LOCAL),
    0x802B2BA8: table.sym_fnc("L802B2BA8", flag=table.GLOBL|table.LOCAL),
    0x802B2BC8: table.sym("object_a_802B2BC8"),
    0x802B2D10: table.sym("object_a_802B2D10", table.GLOBL), # o callback
    0x802B2DAC: table.sym_fnc("object_a_802B2DAC", flag=table.GLOBL), # data
    0x802B2F34: table.sym_fnc("object_a_802B2F34", flag=table.GLOBL), # data
    0x802B3064: table.sym_fnc("object_a_802B3064", flag=table.GLOBL), # data
    0x802B3108: table.sym("object_a_802B3108", table.GLOBL), # o callback
    0x802B3134: table.sym("object_a_802B3134"),
    0x802B3250: table.sym("object_a_802B3250"),
    0x802B329C: table.sym("object_a_802B329C", table.GLOBL), # o callback
    0x802B3600: table.sym("object_a_802B3600", table.GLOBL), # o callback
    0x802B37B8: table.sym("object_a_802B37B8", table.GLOBL), # o callback
    0x802B3810: table.sym("object_a_802B3810", table.GLOBL), # o callback
    0x802B3830: table.sym_fnc("object_a_802B3830", flag=table.GLOBL), # data
    0x802B38B8: table.sym_fnc("object_a_802B38B8", flag=table.GLOBL), # data
    0x802B394C: table.sym_fnc("object_a_802B394C", flag=table.GLOBL), # data
    0x802B3B08: table.sym_fnc("object_a_802B3B08", flag=table.GLOBL), # data
    0x802B3B24: table.sym_fnc("object_a_802B3B24", flag=table.GLOBL), # data
    0x802B3BE0: table.sym("object_a_802B3BE0", table.GLOBL), # o callback
    0x802B3C2C: table.sym_fnc("object_a_802B3C2C", flag=table.GLOBL), # data
    0x802B3CDC: table.sym_fnc("object_a_802B3CDC", flag=table.GLOBL), # data
    0x802B3D10: table.sym_fnc("object_a_802B3D10", flag=table.GLOBL), # data
    0x802B3D74: table.sym("object_a_802B3D74", table.GLOBL), # o callback
    0x802B3DF4: table.sym("object_a_802B3DF4", table.GLOBL), # o callback
    0x802B4080: table.sym("object_a_802B4080", table.GLOBL), # o callback
    0x802B4184: table.sym("object_a_802B4184"),
    0x802B41FC: table.sym("object_a_802B41FC"),
    0x802B4288: table.sym("object_a_802B4288"),
    0x802B4300: table.sym("object_a_802B4300"),
    0x802B4368: table.sym("object_a_802B4368"),
    0x802B43DC: table.sym("object_a_802B43DC"),
    0x802B4478: table.sym_fnc("object_a_802B4478", flag=table.GLOBL), # data
    0x802B44BC: table.sym_fnc("object_a_802B44BC", flag=table.GLOBL), # data
    0x802B459C: table.sym("object_a_802B459C"), # unused
    0x802B45F4: table.sym("object_a_802B45F4"),
    0x802B473C: table.sym("object_a_802B473C"),
    0x802B48D4: table.sym("object_a_802B48D4"),
    0x802B4A1C: table.sym("object_a_802B4A1C"),
    0x802B4A3C: table.sym("object_a_802B4A3C"),
    0x802B4AF4: table.sym("object_a_802B4AF4"),
    0x802B4BAC: table.sym_fnc("object_a_802B4BAC", flag=table.GLOBL), # data
    0x802B4BE8: table.sym_fnc("object_a_802B4BE8", flag=table.GLOBL), # data
    0x802B4CA4: table.sym_fnc("object_a_802B4CA4", flag=table.GLOBL), # data
    0x802B4D14: table.sym_fnc("object_a_802B4D14", flag=table.GLOBL), # data
    0x802B4F00: table.sym_fnc("object_a_802B4F00", flag=table.GLOBL), # data
    0x802B5104: table.sym_fnc("object_a_802B5104", flag=table.GLOBL), # data
    0x802B5218: table.sym_fnc("object_a_802B5218", flag=table.GLOBL), # data
    0x802B53F4: table.sym("object_a_802B53F4"),
    0x802B5444: table.sym("object_a_802B5444"),
    0x802B5554: table.sym("object_a_802B5554"),
    0x802B55CC: table.sym_fnc("object_a_802B55CC", flag=table.GLOBL), # data
    0x802B5798: table.sym_fnc("object_a_802B5798", flag=table.GLOBL), # data
    0x802B58BC: table.sym_fnc("object_a_802B58BC", flag=table.GLOBL), # data
    0x802B59CC: table.sym_fnc("object_a_802B59CC", flag=table.GLOBL), # data
    0x802B5AEC: table.sym("object_a_802B5AEC"),
    0x802B5C00: table.sym_fnc("object_a_802B5C00", flag=table.GLOBL), # data
    0x802B5C40: table.sym_fnc("object_a_802B5C40", flag=table.GLOBL), # data
    0x802B5F6C: table.sym("object_a_802B5F6C"),
    0x802B5FEC: table.sym_fnc("object_a_802B5FEC", flag=table.GLOBL), # data
    0x802B611C: table.sym("object_a_802B611C"),
    0x802B6190: table.sym_fnc("object_a_802B6190", flag=table.GLOBL), # data
    0x802B6568: table.sym_fnc("object_a_802B6568", flag=table.GLOBL), # data
    0x802B65D0: table.sym("object_a_802B65D0"),
    0x802B6670: table.sym("object_a_802B6670"),
    0x802B6730: table.sym("object_a_802B6730"),
    0x802B67D4: table.sym("object_a_802B67D4"),
    0x802B6878: table.sym("object_a_802B6878"),
    0x802B6A10: table.sym("object_a_802B6A10"),
    0x802B6A78: table.sym("object_a_802B6A78"),
    0x802B6BAC: table.sym("object_a_802B6BAC"),
    0x802B6CF0: table.sym_fnc("object_a_802B6CF0", flag=table.GLOBL), # data
    0x802B6D28: table.sym_fnc("L802B6D28", flag=table.GLOBL|table.LOCAL),
    0x802B6D38: table.sym_fnc("L802B6D38", flag=table.GLOBL|table.LOCAL),
    0x802B6D48: table.sym_fnc("L802B6D48", flag=table.GLOBL|table.LOCAL),
    0x802B6DC0: table.sym_fnc("L802B6DC0", flag=table.GLOBL|table.LOCAL),
    0x802B6DEC: table.sym_fnc("L802B6DEC", flag=table.GLOBL|table.LOCAL),
    0x802B6DF4: table.sym_fnc("L802B6DF4", flag=table.GLOBL|table.LOCAL),
    0x802B6E20: table.sym_fnc("L802B6E20", flag=table.GLOBL|table.LOCAL),
    0x802B6E28: table.sym_fnc("L802B6E28", flag=table.GLOBL|table.LOCAL),
    0x802B6E40: table.sym("object_a_802B6E40"),
    0x802B6EE0: table.sym_fnc("object_a_802B6EE0", flag=table.GLOBL), # data
    0x802B711C: table.sym("object_a_802B711C"),
    0x802B71E4: table.sym("object_a_802B71E4"),
    0x802B72D4: table.sym("object_a_802B72D4"),
    0x802B7418: table.sym("object_a_802B7418"),
    0x802B75A4: table.sym("object_a_802B75A4", table.GLOBL), # o callback
    0x802B7878: table.sym("object_a_802B7878", table.GLOBL), # o callback
    0x802B798C: table.sym("s_object_a_802B798C", table.GLOBL), # s callback
    0x802B7A20: table.sym("object_a_802B7A20"),
    0x802B7A78: table.sym_fnc("L802B7A78", flag=table.GLOBL|table.LOCAL),
    0x802B7AE8: table.sym_fnc("L802B7AE8", flag=table.GLOBL|table.LOCAL),
    0x802B7B10: table.sym_fnc("L802B7B10", flag=table.GLOBL|table.LOCAL),
    0x802B7B38: table.sym_fnc("L802B7B38", flag=table.GLOBL|table.LOCAL),
    0x802B7B5C: table.sym_fnc("L802B7B5C", flag=table.GLOBL|table.LOCAL),
    0x802B7B9C: table.sym_fnc("L802B7B9C", flag=table.GLOBL|table.LOCAL),
    0x802B7BC0: table.sym_fnc("L802B7BC0", flag=table.GLOBL|table.LOCAL),
    0x802B7C00: table.sym_fnc("L802B7C00", flag=table.GLOBL|table.LOCAL),
    0x802B7C24: table.sym_fnc("L802B7C24", flag=table.GLOBL|table.LOCAL),
    0x802B7C64: table.sym("s_object_a_802B7C64", table.GLOBL), # s callback
    0x802B7D44: table.sym("s_object_a_802B7D44", table.GLOBL), # s callback
    0x802B7E68: table.sym_fnc("object_a_802B7E68", flag=table.GLOBL), # data
    0x802B7EF0: table.sym_fnc("object_a_802B7EF0", flag=table.GLOBL), # data
    0x802B8024: table.sym_fnc("object_a_802B8024", flag=table.GLOBL), # data
    0x802B8384: table.sym("object_a_802B8384", table.GLOBL), # o callback
    0x802B83B0: table.sym("object_a_802B83B0"),
    0x802B8434: table.sym("object_a_802B8434"),
    0x802B84AC: table.sym("object_a_802B84AC", table.GLOBL), # o callback
    0x802B85B0: table.sym("object_a_802B85B0", table.GLOBL), # o callback
    0x802B8654: table.sym("object_a_802B8654"),
    0x802B8734: table.sym("object_a_802B8734", table.GLOBL), # o callback
    0x802B8960: table.sym("object_a_802B8960", table.GLOBL), # o callback
    0x802B89EC: table.sym("object_a_802B89EC", table.GLOBL), # o callback
    0x802B8B1C: table.sym("object_a_802B8B1C", table.GLOBL), # o callback
    0x802B8C38: table.sym("object_a_802B8C38", table.GLOBL), # o callback
    0x802B8D68: table.sym("object_a_802B8D68", table.GLOBL), # o callback
    0x802B8E7C: table.sym("object_a_802B8E7C", table.GLOBL), # o callback
    0x802B9034: table.sym("object_a_802B9034", table.GLOBL), # o callback
    0x802B90EC: table.sym("object_a_802B90EC", table.GLOBL), # o callback
    0x802B921C: table.sym("object_a_802B921C", table.GLOBL), # o callback
    0x802B935C: table.sym("object_a_802B935C", table.GLOBL), # o callback
    0x802B9790: table.sym("object_a_802B9790", table.GLOBL), # o callback
    0x802B98D4: table.sym("object_a_802B98D4"),
    0x802B98FC: table.sym("object_a_802B98FC", table.GLOBL), # o callback
    0x802B9A78: table.sym("object_a_802B9A78"),
    0x802B9AF8: table.sym("object_a_802B9AF8"),
    0x802B9BB4: table.sym("object_a_802B9BB4", table.GLOBL), # o callback
    0x802B9BD8: table.sym("object_a_802B9BD8", table.GLOBL), # o callback
    0x802B9C60: table.sym_fnc("L802B9C60", flag=table.GLOBL|table.LOCAL),
    0x802B9CA0: table.sym_fnc("L802B9CA0", flag=table.GLOBL|table.LOCAL),
    0x802B9CC0: table.sym_fnc("L802B9CC0", flag=table.GLOBL|table.LOCAL),
    0x802B9CD4: table.sym_fnc("L802B9CD4", flag=table.GLOBL|table.LOCAL),
    0x802B9CF4: table.sym_fnc("L802B9CF4", flag=table.GLOBL|table.LOCAL),
    0x802B9E94: table.sym("object_a_802B9E94", table.GLOBL), # o callback
    0x802B9EFC: table.sym("object_a_802B9EFC"),
    0x802B9F34: table.sym_fnc("L802B9F34", flag=table.GLOBL|table.LOCAL),
    0x802B9F68: table.sym_fnc("L802B9F68", flag=table.GLOBL|table.LOCAL),
    0x802B9FBC: table.sym_fnc("L802B9FBC", flag=table.GLOBL|table.LOCAL),
    0x802BA008: table.sym_fnc("L802BA008", flag=table.GLOBL|table.LOCAL),
    0x802BA064: table.sym_fnc("L802BA064", flag=table.GLOBL|table.LOCAL),
    0x802BA11C: table.sym_fnc("L802BA11C", flag=table.GLOBL|table.LOCAL),
    0x802BA13C: table.sym("object_a_802BA13C"),
    0x802BA19C: table.sym("object_a_802BA19C", table.GLOBL), # o callback
    0x802BA1E0: table.sym("object_a_802BA1E0", table.GLOBL), # o callback
    0x802BA25C: table.sym("object_a_802BA25C", table.GLOBL), # o callback
    0x802BA2B0: table.sym("s_object_a_802BA2B0", table.GLOBL), # s callback
    0x802BA2F8: table.sym("object_a_802BA2F8", table.GLOBL), # o callback
    0x802BA458: table.sym("object_a_802BA458", table.GLOBL), # o callback
    0x802BA5BC: table.sym("object_a_802BA5BC", table.GLOBL), # o callback
    0x802BA608: table.sym("object_a_802BA608", table.GLOBL), # o callback
    0x802BA7E0: table.sym("object_a_802BA7E0"),
    0x802BA868: table.sym("object_a_802BA868"),
    0x802BA8C4: table.sym("object_a_802BA8C4"), # unused
    0x802BA958: table.sym("object_a_802BA958"),
    0x802BAB7C: table.sym_fnc("object_a_802BAB7C", flag=table.GLOBL), # data
    0x802BAE40: table.sym_fnc("object_a_802BAE40", flag=table.GLOBL), # data
    0x802BAEC4: table.sym_fnc("object_a_802BAEC4", flag=table.GLOBL), # data
    0x802BAF10: table.sym_fnc("object_a_802BAF10", flag=table.GLOBL), # data
    0x802BAF64: table.sym_fnc("object_a_802BAF64", flag=table.GLOBL), # data
    0x802BB07C: table.sym_fnc("object_a_802BB07C", flag=table.GLOBL), # data
    0x802BB288: table.sym_fnc("object_a_802BB288", flag=table.GLOBL), # data
    0x802BB3B8: table.sym_fnc("object_a_802BB3B8", flag=table.GLOBL), # data
    0x802BB468: table.sym_fnc("L802BB468", flag=table.GLOBL|table.LOCAL),
    0x802BB508: table.sym_fnc("L802BB508", flag=table.GLOBL|table.LOCAL),
    0x802BB564: table.sym_fnc("L802BB564", flag=table.GLOBL|table.LOCAL),
    0x802BB5A4: table.sym_fnc("L802BB5A4", flag=table.GLOBL|table.LOCAL),
    0x802BB5F4: table.sym_fnc("L802BB5F4", flag=table.GLOBL|table.LOCAL),
    0x802BB638: table.sym_fnc("L802BB638", flag=table.GLOBL|table.LOCAL),
    0x802BB6E0: table.sym_fnc("L802BB6E0", flag=table.GLOBL|table.LOCAL),
    0x802BB748: table.sym_fnc("L802BB748", flag=table.GLOBL|table.LOCAL),
    0x802BB798: table.sym("object_a_802BB798"),
    0x802BB838: table.sym("object_a_802BB838"), # unused
    0x802BB888: table.sym("object_a_802BB888"),
    0x802BBA3C: table.sym("object_a_802BBA3C"),
    0x802BBA74: table.sym_fnc("L802BBA74", flag=table.GLOBL|table.LOCAL),
    0x802BBAB4: table.sym_fnc("L802BBAB4", flag=table.GLOBL|table.LOCAL),
    0x802BBAFC: table.sym_fnc("L802BBAFC", flag=table.GLOBL|table.LOCAL),
    0x802BBB04: table.sym_fnc("L802BBB04", flag=table.GLOBL|table.LOCAL),
    0x802BBB60: table.sym_fnc("L802BBB60", flag=table.GLOBL|table.LOCAL),
    0x802BBB80: table.sym_fnc("L802BBB80", flag=table.GLOBL|table.LOCAL),
    0x802BBB98: table.sym("object_a_802BBB98", table.GLOBL), # o callback
    0x802BBC0C: table.sym("object_a_802BBC0C", table.GLOBL), # o callback
    0x802BBD6C: table.sym("object_a_802BBD6C"),
    0x802BBFD8: table.sym("object_a_802BBFD8"),
    0x802BC0F0: table.sym("object_a_802BC0F0", table.GLOBL), # o callback
    0x802BC22C: table.sym("object_a_802BC22C", table.GLOBL), # o callback
    0x802BC294: table.sym("object_a_802BC294", table.GLOBL), # o callback
    0x802BC348: table.sym("object_a_802BC348"),
    0x802BC4F4: table.sym_fnc("object_a_802BC4F4", flag=table.GLOBL), # data
    0x802BC538: table.sym_fnc("object_a_802BC538", flag=table.GLOBL), # data
    0x802BC590: table.sym_fnc("object_a_802BC590", flag=table.GLOBL), # data
    0x802BC5FC: table.sym_fnc("object_a_802BC5FC", flag=table.GLOBL), # data
    0x802BC618: table.sym("object_a_802BC618", table.GLOBL), # o callback
    0x802BC660: table.sym("object_a_802BC660", table.GLOBL), # o callback
    0x802BC728: table.sym("object_a_802BC728", table.GLOBL), # o callback
    0x802BC898: table.sym("object_a_802BC898", table.GLOBL), # o callback
    0x802BC934: table.sym("object_a_802BC934"),
    0x802BCA74: table.sym("object_a_802BCA74", table.GLOBL), # o callback
    0x802BCADC: table.sym_fnc("L802BCADC", flag=table.GLOBL|table.LOCAL),
    0x802BCB24: table.sym_fnc("L802BCB24", flag=table.GLOBL|table.LOCAL),
    0x802BCBA4: table.sym_fnc("L802BCBA4", flag=table.GLOBL|table.LOCAL),
    0x802BCC1C: table.sym_fnc("L802BCC1C", flag=table.GLOBL|table.LOCAL),
    0x802BCC90: table.sym_fnc("L802BCC90", flag=table.GLOBL|table.LOCAL),
    0x802BCCE8: table.sym("object_a_802BCCE8"),
    0x802BCDA8: table.sym("object_a_802BCDA8", table.GLOBL), # o callback
    0x802BCE58: table.sym("object_a_802BCE58", table.GLOBL), # o callback
    0x802BCE9C: table.sym("object_a_802BCE9C"),
    0x802BCF40: table.sym("object_a_802BCF40", table.GLOBL), # o callback
    0x802BCFC4: table.sym("object_a_802BCFC4"),
    0x802BD058: table.sym("object_a_802BD058", table.GLOBL), # o callback
    0x802BD3E4: table.sym("object_a_802BD3E4"),
    0x802BD488: table.sym("object_a_802BD488", table.GLOBL), # o callback
    0x802BD5DC: table.sym("object_a_802BD5DC"),
    0x802BD62C: table.sym("object_a_802BD62C"),
    0x802BD680: table.sym("object_a_802BD680", table.GLOBL), # o callback
    0x802BD8D0: table.sym("object_a_802BD8D0"),
    0x802BD91C: table.sym("object_a_802BD91C"),
    0x802BDB04: table.sym_fnc("object_a_802BDB04", flag=table.GLOBL), # data
    0x802BDB3C: table.sym_fnc("object_a_802BDB3C", flag=table.GLOBL), # data
    0x802BDB74: table.sym_fnc("object_a_802BDB74", flag=table.GLOBL), # data
    0x802BDBAC: table.sym_fnc("object_a_802BDBAC", flag=table.GLOBL), # data
    0x802BDBE4: table.sym_fnc("object_a_802BDBE4", flag=table.GLOBL), # data
    0x802BDC7C: table.sym_fnc("object_a_802BDC7C", flag=table.GLOBL), # data
    0x802BDCC8: table.sym_fnc("object_a_802BDCC8", flag=table.GLOBL), # data
    0x802BDD14: table.sym_fnc("object_a_802BDD14", flag=table.GLOBL), # data
    0x802BDD68: table.sym("object_a_802BDD68", table.GLOBL), # o callback
    0x802BDD9C: table.sym_fnc("object_a_802BDD9C", flag=table.GLOBL), # data
    0x802BDE10: table.sym("object_a_802BDE10"),
    0x802BDEEC: table.sym_fnc("object_a_802BDEEC", flag=table.GLOBL), # data
    0x802BE034: table.sym_fnc("object_a_802BE034", flag=table.GLOBL), # data
    0x802BE0B8: table.sym("object_a_802BE0B8"),
    0x802BE0EC: table.sym_fnc("object_a_802BE0EC", flag=table.GLOBL), # data
    0x802BE150: table.sym_fnc("object_a_802BE150", flag=table.GLOBL), # data
    0x802BE234: table.sym_fnc("object_a_802BE234", flag=table.GLOBL), # data
    0x802BE278: table.sym_fnc("object_a_802BE278", flag=table.GLOBL), # data
    0x802BE350: table.sym_fnc("object_a_802BE350", flag=table.GLOBL), # data
    0x802BE49C: table.sym("object_a_802BE49C"),
    0x802BE50C: table.sym_fnc("object_a_802BE50C", flag=table.GLOBL), # data
    0x802BE5A0: table.sym("object_a_802BE5A0", table.GLOBL), # o callback
    0x802BE628: table.sym("object_a_802BE628"),
    0x802BE6D4: table.sym("object_a_802BE6D4"),
    0x802BE79C: table.sym("object_a_802BE79C", table.GLOBL), # o callback
    0x802BE8A8: table.sym_fnc("object_a_802BE8A8", flag=table.GLOBL), # data
    0x802BE8B8: table.sym_fnc("object_a_802BE8B8", flag=table.GLOBL), # data
    0x802BE8F4: table.sym("object_a_802BE8F4"),
    0x802BE9DC: table.sym("object_a_802BE9DC"),
    0x802BEB14: table.sym_fnc("object_a_802BEB14", flag=table.GLOBL), # data
    0x802BEB54: table.sym_fnc("object_a_802BEB54", flag=table.GLOBL), # data
    0x802BEB8C: table.sym_fnc("object_a_802BEB8C", flag=table.GLOBL), # data
    0x802BEBC4: table.sym_fnc("object_a_802BEBC4", flag=table.GLOBL), # data
    0x802BEBFC: table.sym_fnc("object_a_802BEBFC", flag=table.GLOBL), # data
    0x802BEC34: table.sym("object_a_802BEC34", table.GLOBL), # o callback
    0x802BECB0: table.sym("object_a_802BECB0"),
    0x802BED7C: table.sym("object_a_802BED7C", table.GLOBL),
    0x802BEDEC: table.sym_fnc("object_a_802BEDEC", flag=table.GLOBL), # data
    0x802BEF8C: table.sym_fnc("object_a_802BEF8C", flag=table.GLOBL), # data
    0x802BF1D8: table.sym_fnc("object_a_802BF1D8", flag=table.GLOBL), # data
    0x802BF3C0: table.sym("object_a_802BF3C0", table.GLOBL), # o callback
    0x802BF424: table.sym("object_a_802BF424"),
    0x802BF474: table.sym_fnc("object_a_802BF474", flag=table.GLOBL), # data
    0x802BF57C: table.sym_fnc("object_a_802BF57C", flag=table.GLOBL), # data
    0x802BF648: table.sym_fnc("object_a_802BF648", flag=table.GLOBL), # data
    0x802BF6E4: table.sym_fnc("object_a_802BF6E4", flag=table.GLOBL), # data
    0x802BF760: table.sym_fnc("object_a_802BF760", flag=table.GLOBL), # data
    0x802BF90C: table.sym_fnc("object_a_802BF90C", flag=table.GLOBL), # data
    0x802BFA14: table.sym("object_a_802BFA14"),
    0x802BFA88: table.sym("object_a_802BFA88", table.GLOBL), # o callback
    0x802BFBAC: table.sym("s_object_a_802BFBAC", table.GLOBL), # s callback
    0x802BFCD8: table.sym_fnc("object_a_802BFCD8", flag=table.GLOBL), # data
    0x802BFEB8: table.sym_fnc("object_a_802BFEB8", flag=table.GLOBL), # data
    0x802BFF20: table.sym_fnc("object_a_802BFF20", flag=table.GLOBL), # data
    0x802BFF3C: table.sym("object_a_802BFF3C", table.GLOBL), # o callback
    0x802BFF68: table.sym("object_a_802BFF68"),
    0x802C00B4: table.sym_fnc("object_a_802C00B4", flag=table.GLOBL), # data
    0x802C0348: table.sym_fnc("object_a_802C0348", flag=table.GLOBL), # data
    0x802C06A8: table.sym_fnc("object_a_802C06A8", flag=table.GLOBL), # data
    0x802C0768: table.sym("object_a_802C0768", table.GLOBL), # o callback
    0x802C08A8: table.sym("object_a_802C08A8", table.GLOBL), # o callback
    0x802C0AAC: table.sym_fnc("object_a_802C0AAC", flag=table.GLOBL), # data
    0x802C0B50: table.sym_fnc("object_a_802C0B50", flag=table.GLOBL), # data
    0x802C0BA4: table.sym_fnc("object_a_802C0BA4", flag=table.GLOBL), # data
    0x802C0BC4: table.sym_fnc("object_a_802C0BC4", flag=table.GLOBL), # data
    0x802C0BE0: table.sym("object_a_802C0BE0", table.GLOBL), # o callback
    0x802C0C0C: table.sym("object_a_802C0C0C"),
    0x802C0CD4: table.sym_fnc("object_a_802C0CD4", flag=table.GLOBL), # data
    0x802C0D44: table.sym_fnc("object_a_802C0D44", flag=table.GLOBL), # data
    0x802C0F90: table.sym_fnc("object_a_802C0F90", flag=table.GLOBL), # data
    0x802C1204: table.sym("object_a_802C1204", table.GLOBL), # o callback
    0x802C12C0: table.sym("object_a_802C12C0", table.GLOBL), # o callback
    0x802C1308: table.sym_fnc("object_a_802C1308", flag=table.GLOBL), # data
    0x802C13EC: table.sym_fnc("object_a_802C13EC", flag=table.GLOBL), # data
    0x802C14B0: table.sym_fnc("object_a_802C14B0", flag=table.GLOBL), # data
    0x802C15B8: table.sym_fnc("object_a_802C15B8", flag=table.GLOBL), # data
    0x802C17BC: table.sym("object_a_802C17BC"),
    0x802C18D0: table.sym_fnc("object_a_802C18D0", flag=table.GLOBL), # data
    0x802C1988: table.sym_fnc("object_a_802C1988", flag=table.GLOBL), # data
    0x802C19C0: table.sym("object_a_802C19C0", table.GLOBL), # o callback
    0x802C19FC: table.sym("object_a_802C19FC", table.GLOBL), # o callback
    0x802C1A40: table.sym("object_a_802C1A40", table.GLOBL), # o callback
    0x802C1A80: table.sym("object_a_802C1A80", table.GLOBL), # o callback
    0x802C1A90: table.sym("object_a_802C1A90", table.GLOBL), # o callback
    0x802C1C44: table.sym("object_a_802C1C44", table.GLOBL), # o callback
    0x802C1CD4: table.sym("object_a_802C1CD4", table.GLOBL), # o callback
    0x802C1E10: table.sym("object_a_802C1E10", table.GLOBL), # o callback
    0x802C2190: table.sym("object_a_802C2190", table.GLOBL), # o callback
    0x802C2274: table.sym("object_a_802C2274", table.GLOBL), # o callback
    0x802C22B8: table.sym("object_a_802C22B8", table.GLOBL), # o callback
    0x802C242C: table.sym("object_a_802C242C", table.GLOBL), # o callback
    0x802C263C: table.sym("object_a_802C263C", table.GLOBL), # o callback
    0x802C26F8: table.sym("object_a_802C26F8", table.GLOBL), # o callback
    0x802C2930: table.sym("object_a_802C2930", table.GLOBL), # o callback
    0x802C2A24: table.sym("object_a_802C2A24", table.GLOBL), # o callback
    0x802C2CE8: table.sym("object_a_802C2CE8"),
    0x802C2EBC: table.sym_fnc("object_a_802C2EBC", flag=table.GLOBL), # data
    0x802C2FBC: table.sym_fnc("object_a_802C2FBC", flag=table.GLOBL), # data
    0x802C31C4: table.sym_fnc("object_a_802C31C4", flag=table.GLOBL), # data
    0x802C329C: table.sym("object_a_802C329C", table.GLOBL), # o callback
    0x802C32E8: table.sym("object_a_802C32E8", table.GLOBL), # o callback
    0x802C33F4: table.sym("object_a_802C33F4"),
    0x802C3440: table.sym("object_a_802C3440", table.GLOBL), # o callback
    0x802C3460: table.sym("object_a_802C3460"),
    0x802C3534: table.sym("object_a_802C3534"),
    0x802C3684: table.sym("object_a_802C3684", table.GLOBL), # o callback
    0x802C3748: table.sym("object_a_802C3748"),
    0x802C3884: table.sym("object_a_802C3884"),
    0x802C39D4: table.sym("object_a_802C39D4"),
    0x802C3B08: table.sym("object_a_802C3B08"),
    0x802C3C04: table.sym("object_a_802C3C04"),
    0x802C3CD0: table.sym("object_a_802C3CD0"),
    0x802C3D50: table.sym("object_a_802C3D50"),
    0x802C3D9C: table.sym("object_a_802C3D9C"),
    0x802C3E80: table.sym("object_a_802C3E80"),
    0x802C3F8C: table.sym("object_a_802C3F8C"),
    0x802C4118: table.sym("object_a_802C4118"),
    0x802C4158: table.sym("object_a_802C4158"),
    0x802C4210: table.sym("object_a_802C4210"),
    0x802C43F4: table.sym_fnc("object_a_802C43F4", flag=table.GLOBL), # data
    0x802C4508: table.sym_fnc("object_a_802C4508", flag=table.GLOBL), # data
    0x802C45B0: table.sym_fnc("object_a_802C45B0", flag=table.GLOBL), # data
    0x802C46D8: table.sym_fnc("object_a_802C46D8", flag=table.GLOBL), # data
    0x802C4720: table.sym_fnc("object_a_802C4720", flag=table.GLOBL), # data
    0x802C4790: table.sym_fnc("object_a_802C4790", flag=table.GLOBL), # data
    0x802C4824: table.sym("object_a_802C4824", table.GLOBL), # o callback
    0x802C48C0: table.sym_fnc("object_a_802C48C0", flag=table.GLOBL), # data
    0x802C49F0: table.sym_fnc("object_a_802C49F0", flag=table.GLOBL), # data
    0x802C4B54: table.sym_fnc("object_a_802C4B54", flag=table.GLOBL), # data
    0x802C4B9C: table.sym("object_a_802C4B9C"),
    0x802C4BD4: table.sym("object_a_802C4BD4"),
    0x802C4C10: table.sym("object_a_802C4C10"),
    0x802C4C70: table.sym_fnc("object_a_802C4C70", flag=table.GLOBL), # data
    0x802C4DD4: table.sym_fnc("object_a_802C4DD4", flag=table.GLOBL), # data
    0x802C4F30: table.sym("object_a_802C4F30", table.GLOBL), # o callback
    0x802C4FB0: table.sym_fnc("object_a_802C4FB0", flag=table.GLOBL), # data
    0x802C503C: table.sym_fnc("object_a_802C503C", flag=table.GLOBL), # data
    0x802C50D8: table.sym_fnc("object_a_802C50D8", flag=table.GLOBL), # data
    0x802C5120: table.sym_fnc("object_a_802C5120", flag=table.GLOBL), # data
    0x802C515C: table.sym("object_a_802C515C", table.GLOBL), # o callback
    0x802C51D4: table.sym("object_a_802C51D4", table.GLOBL), # o callback
    0x802C5224: table.sym("object_a_802C5224", table.GLOBL), # o callback
    0x802C53CC: table.sym("object_a_802C53CC"),
    0x802C53EC: table.sym("object_a_802C53EC", table.GLOBL), # o callback
    0x802C5414: table.sym("object_a_802C5414", table.GLOBL), # o callback
    0x802C5688: table.sym("object_a_802C5688", table.GLOBL), # o callback
    0x802C5890: table.sym("object_a_802C5890", table.GLOBL), # o callback
    0x802C5A38: table.sym("object_a_802C5A38", table.GLOBL), # o callback
    0x802C5B54: table.sym("object_a_802C5B54"),
    0x802C5CA8: table.sym("object_a_802C5CA8", table.GLOBL), # o callback
    0x802C5DC0: table.sym("object_a_802C5DC0", table.GLOBL), # o callback
    0x802C5F48: table.sym("object_a_802C5F48", table.GLOBL), # o callback
    0x802C5FDC: table.sym("object_a_802C5FDC", table.GLOBL), # o callback
    0x802C6050: table.sym("object_a_802C6050", table.GLOBL), # o callback
    0x802C60AC: table.sym("object_a_802C60AC", table.GLOBL), # o callback
    0x802C6150: table.sym("object_a_802C6150"),
    0x802C61D4: table.sym("object_a_802C61D4"),
    0x802C6278: table.sym("object_a_802C6278"),
    0x802C62BC: table.sym("object_a_802C62BC"),
    0x802C6328: table.sym("object_a_802C6328"),
    0x802C6348: table.sym("object_a_802C6348", table.GLOBL), # o callback
    0x802C6380: table.sym_fnc("L802C6380", flag=table.GLOBL|table.LOCAL),
    0x802C6390: table.sym_fnc("L802C6390", flag=table.GLOBL|table.LOCAL),
    0x802C63A0: table.sym_fnc("L802C63A0", flag=table.GLOBL|table.LOCAL),
    0x802C63B0: table.sym_fnc("L802C63B0", flag=table.GLOBL|table.LOCAL),
    0x802C63C0: table.sym_fnc("L802C63C0", flag=table.GLOBL|table.LOCAL),
    0x802C63E8: table.sym("object_a_802C63E8", table.GLOBL), # o callback
    0x802C64A4: table.sym("object_a_802C64A4", table.GLOBL), # o callback
    0x802C6538: table.sym("object_a_802C6538"),
    0x802C65C0: table.sym("object_a_802C65C0", table.GLOBL), # o callback
    0x802C6668: table.sym_fnc("L802C6668", flag=table.GLOBL|table.LOCAL),
    0x802C66F0: table.sym_fnc("L802C66F0", flag=table.GLOBL|table.LOCAL),
    0x802C688C: table.sym_fnc("L802C688C", flag=table.GLOBL|table.LOCAL),
    0x802C6920: table.sym_fnc("L802C6920", flag=table.GLOBL|table.LOCAL),
    0x802C6990: table.sym_fnc("L802C6990", flag=table.GLOBL|table.LOCAL),
    0x802C6A1C: table.sym_fnc("L802C6A1C", flag=table.GLOBL|table.LOCAL),
    0x802C6B6C: table.sym("object_a_802C6B6C", table.GLOBL), # o callback
    0x802C6CA0: table.sym("object_a_802C6CA0"),
    0x802C6D6C: table.sym_fnc("object_a_802C6D6C", flag=table.GLOBL), # data
    0x802C6EC8: table.sym_fnc("object_a_802C6EC8", flag=table.GLOBL), # data
    0x802C6FB0: table.sym_fnc("object_a_802C6FB0", flag=table.GLOBL), # data
    0x802C710C: table.sym_fnc("object_a_802C710C", flag=table.GLOBL), # data
    0x802C7254: table.sym_fnc("object_a_802C7254", flag=table.GLOBL), # data
    0x802C72B4: table.sym_fnc("object_a_802C72B4", flag=table.GLOBL), # data
    0x802C7380: table.sym_fnc("object_a_802C7380", flag=table.GLOBL), # data
    0x802C7428: table.sym("object_a_802C7428"),
    0x802C75FC: table.sym("object_a_802C75FC"),
    0x802C76D4: table.sym_fnc("object_a_802C76D4", flag=table.GLOBL), # data
    0x802C7858: table.sym_fnc("object_a_802C7858", flag=table.GLOBL), # data
    0x802C7998: table.sym_fnc("object_a_802C7998", flag=table.GLOBL), # data
    0x802C79D8: table.sym("object_a_802C79D8", table.GLOBL), # o callback
    0x802C7A70: table.sym("object_a_802C7A70", table.GLOBL), # o callback
    0x802C7B14: table.sym("object_a_802C7B14", table.GLOBL), # o callback
    0x802C7CAC: table.sym("object_a_802C7CAC", table.GLOBL), # o callback
    0x802C7D40: table.sym("object_a_802C7D40", table.GLOBL), # o callback
    0x802C7D90: table.sym("object_a_802C7D90", table.GLOBL), # o callback
    0x802C7DFC: table.sym("object_a_802C7DFC", table.GLOBL), # o callback
    0x802C7E5C: table.sym("object_a_802C7E5C", table.GLOBL), # o callback
    0x802C7F98: table.sym("object_a_802C7F98", table.GLOBL), # o callback
    0x802C81B4: table.sym("object_a_802C81B4", table.GLOBL),
    0x802C834C: table.sym("object_a_802C834C", table.GLOBL), # o callback
    0x802C85A4: table.sym("object_a_802C85A4"),
    0x802C863C: table.sym("object_a_802C863C", table.GLOBL), # o callback

    # src/obj_physics.c
    0x802C89F0: table.sym("obj_physics_802C89F0", table.GLOBL),
    0x802C8B4C: table.sym("obj_physics_802C8B4C", table.GLOBL),
    0x802C8B8C: table.sym("obj_physics_802C8B8C", table.GLOBL),
    0x802C8BC8: table.sym("obj_physics_802C8BC8", table.GLOBL),
    0x802C8EC0: table.sym("obj_physics_802C8EC0", table.GLOBL),
    0x802C8F28: table.sym("obj_physics_802C8F28", table.GLOBL),

    # src/obj_collision.c
    0x802C8F40: table.sym("obj_collision_802C8F40"), # unused
    0x802C8FE4: table.sym("obj_collision_802C8FE4"),
    0x802C91EC: table.sym("obj_collision_802C91EC"),
    0x802C9388: table.sym("obj_collision_802C9388"),
    0x802C93F8: table.sym("obj_collision_802C93F8"),
    0x802C94AC: table.sym("obj_collision_802C94AC"),
    0x802C95B4: table.sym("obj_collision_802C95B4"),
    0x802C9630: table.sym("obj_collision_802C9630"),
    0x802C9724: table.sym("obj_collision_802C9724", table.GLOBL),

    # src/obj_list.c
    0x802C97D0: table.sym("obj_list_802C97D0"), # unused
    0x802C9840: table.sym("obj_list_802C9840"), # unused
    0x802C98A4: table.sym("obj_list_802C98A4"),
    0x802C9950: table.sym("obj_list_802C9950"), # unused
    0x802C9984: table.sym("obj_list_802C9984"),
    0x802C99B8: table.sym("obj_list_802C99B8", table.GLOBL),
    0x802C9A3C: table.sym("obj_list_802C9A3C", table.GLOBL),
    0x802C9AD8: table.sym("obj_list_802C9AD8"),
    0x802C9B68: table.sym("obj_list_802C9B68", table.GLOBL),
    0x802C9C00: table.sym("obj_list_802C9C00"),
    0x802C9E5C: table.sym("obj_list_802C9E5C"),
    0x802C9F04: table.sym("obj_list_802C9F04", table.GLOBL),
    0x802CA028: table.sym("obj_list_802CA028", table.GLOBL),

    # src/obj_sfx.c
    0x802CA040: table.sym_fnc("obj_sfx_802CA040", arg=(
        "OBJ_SFX *sfx",
    ), flag=table.GLOBL),
    0x802CA144: table.sym_fnc("obj_sfx_802CA144", arg=(
        "NA_SE se",
    ), flag=table.GLOBL),
    0x802CA190: table.sym_fnc("obj_sfx_802CA190", arg=(
        "NA_SE se",
    ), flag=table.GLOBL),
    0x802CA1E0: table.sym_fnc("obj_sfx_802CA1E0", arg=(
        "NA_SE se",
    ), flag=table.GLOBL),
    0x802CA230: table.sym_fnc("obj_sfx_802CA230", "int", (
        "float x",
    )), # unused
    0x802CA2D4: table.sym_fnc("obj_sfx_802CA2D4", "int", (
        "float x",
    )), # unused

    # src/obj_debug.c
    0x802CA370: table.sym("_802CA370"), # unused
    0x802CA380: table.sym("_802CA380"), # unused
    0x802CA390: table.sym("_802CA390"), # unused
    0x802CA3A0: table.sym("_802CA3A0"), # unused
    0x802CA3B0: table.sym("obj_debug_802CA3B0", table.GLOBL),
    0x802CA3E0: table.sym("obj_debug_802CA3E0", table.GLOBL),
    0x802CA418: table.sym("obj_debug_802CA418"),
    0x802CA460: table.sym("obj_debug_802CA460"),
    0x802CA51C: table.sym("obj_debug_802CA51C", table.GLOBL),
    0x802CA568: table.sym("obj_debug_802CA568", table.GLOBL),
    0x802CA5B8: table.sym("obj_debug_802CA5B8", table.GLOBL),
    0x802CA618: table.sym("obj_debug_802CA618", table.GLOBL),
    0x802CA680: table.sym("obj_debug_802CA680"),
    0x802CA6D0: table.sym("obj_debug_802CA6D0"),
    0x802CA8E8: table.sym("obj_debug_802CA8E8"),
    0x802CA918: table.sym("obj_debug_802CA918"),
    0x802CA94C: table.sym("obj_debug_802CA94C"),
    0x802CA990: table.sym("obj_debug_802CA990"),
    0x802CAA6C: table.sym("obj_debug_802CAA6C"),
    0x802CAAA8: table.sym("obj_debug_802CAAA8"),
    0x802CAAE4: table.sym("obj_debug_802CAAE4"),
    0x802CABAC: table.sym("obj_debug_802CABAC", table.GLOBL),
    0x802CAC20: table.sym("obj_debug_802CAC20", table.GLOBL),
    0x802CACC8: table.sym("obj_debug_802CACC8"), # unused
    0x802CADC8: table.sym("obj_debug_802CADC8"), # unused
    0x802CAE9C: table.sym("obj_debug_802CAE9C"), # unused
    0x802CB0B0: table.sym("obj_debug_802CB0B0", table.GLOBL),
    0x802CB0C0: table.sym("obj_debug_802CB0C0", table.GLOBL),
    0x802CB1C0: table.sym("obj_debug_802CB1C0", table.GLOBL), # o callback
    0x802CB264: table.sym("obj_debug_802CB264", table.GLOBL), # o callback
    0x802CB394: table.sym("obj_debug_802CB394"), # unused
    0x802CB564: table.sym("obj_debug_802CB564"), # unused

    # src/wipe.c
    0x802CB5C0: table.sym("wipe_802CB5C0"),
    0x802CB640: table.sym("wipe_802CB640"),
    0x802CB894: table.sym("wipe_802CB894"),
    0x802CBA18: table.sym("wipe_802CBA18"),
    0x802CBBC4: table.sym("wipe_802CBBC4"),
    0x802CBC20: table.sym("wipe_802CBC20"),
    0x802CBC7C: table.sym("wipe_802CBC7C"),
    0x802CBD54: table.sym("wipe_802CBD54"),
    0x802CBE64: table.sym("wipe_802CBE64"),
    0x802CBEE0: table.sym("wipe_802CBEE0"),
    0x802CBF64: table.sym("wipe_802CBF64"),
    0x802CBFE8: table.sym("wipe_802CBFE8"),
    0x802CC180: table.sym("wipe_802CC180"),
    0x802CC4D8: table.sym("wipe_802CC4D8"),
    0x802CCBE8: table.sym("wipe_802CCBE8", table.GLOBL),
    0x802CCC28: table.sym_fnc("L802CCC28", flag=table.GLOBL|table.LOCAL),
    0x802CCC48: table.sym_fnc("L802CCC48", flag=table.GLOBL|table.LOCAL),
    0x802CCC68: table.sym_fnc("L802CCC68", flag=table.GLOBL|table.LOCAL),
    0x802CCC90: table.sym_fnc("L802CCC90", flag=table.GLOBL|table.LOCAL),
    0x802CCCB8: table.sym_fnc("L802CCCB8", flag=table.GLOBL|table.LOCAL),
    0x802CCCE0: table.sym_fnc("L802CCCE0", flag=table.GLOBL|table.LOCAL),
    0x802CCD08: table.sym_fnc("L802CCD08", flag=table.GLOBL|table.LOCAL),
    0x802CCD34: table.sym_fnc("L802CCD34", flag=table.GLOBL|table.LOCAL),
    0x802CCD60: table.sym_fnc("L802CCD60", flag=table.GLOBL|table.LOCAL),
    0x802CCD88: table.sym_fnc("L802CCD88", flag=table.GLOBL|table.LOCAL),
    0x802CCDB0: table.sym_fnc("L802CCDB0", flag=table.GLOBL|table.LOCAL),
    0x802CCDC8: table.sym("wipe_802CCDC8"),
    0x802CD1E8: table.sym("s_wipe_802CD1E8", table.GLOBL), # s callback

    # src/shadow.c
    0x802CD280: table.sym("shadow_802CD280"),
    0x802CD328: table.sym("shadow_802CD328"),
    0x802CD388: table.sym("shadow_802CD388"),
    0x802CD444: table.sym("shadow_802CD444"),
    0x802CD48C: table.sym("shadow_802CD48C"),
    0x802CD614: table.sym("shadow_802CD614"),
    0x802CD6C4: table.sym("shadow_802CD6C4"),
    0x802CD938: table.sym("shadow_802CD938"),
    0x802CD988: table.sym("shadow_802CD988"),
    0x802CD9EC: table.sym("shadow_802CD9EC"),
    0x802CDB20: table.sym("shadow_802CDB20"),
    0x802CDB74: table.sym("shadow_802CDB74"),
    0x802CDC40: table.sym("shadow_802CDC40"),
    0x802CDE94: table.sym("shadow_802CDE94"),
    0x802CDF3C: table.sym("shadow_802CDF3C"),
    0x802CE128: table.sym("shadow_802CE128"),
    0x802CE2BC: table.sym("shadow_802CE2BC"),
    0x802CE3EC: table.sym("shadow_802CE3EC"),
    0x802CE524: table.sym("shadow_802CE524"),
    0x802CE690: table.sym("shadow_802CE690"),
    0x802CE79C: table.sym("shadow_802CE79C"),
    0x802CE9D0: table.sym("shadow_802CE9D0"),
    0x802CEAE8: table.sym("shadow_802CEAE8"),
    0x802CEC04: table.sym("shadow_802CEC04"),
    0x802CEDC0: table.sym("shadow_802CEDC0"),
    0x802CEF6C: table.sym("shadow_802CEF6C"),
    0x802CF080: table.sym("shadow_802CF080"),
    0x802CF1F0: table.sym("shadow_802CF1F0"),
    0x802CF34C: table.sym("shadow_802CF34C", table.GLOBL),
    0x802CF41C: table.sym_fnc("L802CF41C", flag=table.GLOBL|table.LOCAL),
    0x802CF444: table.sym_fnc("L802CF444", flag=table.GLOBL|table.LOCAL),
    0x802CF46C: table.sym_fnc("L802CF46C", flag=table.GLOBL|table.LOCAL),
    0x802CF494: table.sym_fnc("L802CF494", flag=table.GLOBL|table.LOCAL),
    0x802CF4C4: table.sym_fnc("L802CF4C4", flag=table.GLOBL|table.LOCAL),
    0x802CF4F4: table.sym_fnc("L802CF4F4", flag=table.GLOBL|table.LOCAL),
    0x802CF550: table.sym_fnc("L802CF550", flag=table.GLOBL|table.LOCAL),

    # src/background.c
    0x802CF5B0: table.sym("background_802CF5B0"),
    0x802CF69C: table.sym("background_802CF69C"),
    0x802CF77C: table.sym("background_802CF77C"),
    0x802CF804: table.sym("background_802CF804"),
    0x802CFA2C: table.sym("background_802CFA2C"),
    0x802CFC68: table.sym("background_802CFC68"),
    0x802CFD88: table.sym("background_802CFD88"),
    0x802CFEF4: table.sym("background_802CFEF4", table.GLOBL),

    # src/scroll.c
    0x802D0080: table.sym("s_scroll_802D0080", table.GLOBL), # s callback
    0x802D01E0: table.sym("s_scroll_802D01E0", table.GLOBL), # s callback
    0x802D0254: table.sym("scroll_802D0254"),
    0x802D0484: table.sym("scroll_802D0484"),
    0x802D0A84: table.sym("scroll_802D0A84"),
    0x802D0BB0: table.sym("scroll_802D0BB0"),
    0x802D0C84: table.sym("scroll_802D0C84"),
    0x802D0F28: table.sym("scroll_802D0F28"),
    0x802D104C: table.sym("s_scroll_802D104C", table.GLOBL), # s callback
    0x802D1330: table.sym("scroll_802D1330"),
    0x802D13CC: table.sym("scroll_802D13CC"),
    0x802D1574: table.sym("scroll_802D1574"),
    0x802D18B4: table.sym("scroll_802D18B4"),
    0x802D1B70: table.sym("s_scroll_802D1B70", table.GLOBL), # s callback
    0x802D1CDC: table.sym("s_scroll_802D1CDC", table.GLOBL), # s callback
    0x802D1E48: table.sym("s_scroll_802D1E48", table.GLOBL), # s callback
    0x802D1FA8: table.sym("s_scroll_802D1FA8", table.GLOBL), # s callback
    0x802D2108: table.sym("s_scroll_802D2108", table.GLOBL), # s callback

    # src/obj_shape.c
    0x802D2210: table.sym("obj_shape_802D2210", table.GLOBL),
    0x802D22C4: table.sym("obj_shape_802D22C4", table.GLOBL),
    0x802D2360: table.sym("s_obj_shape_802D2360", table.GLOBL), # s callback
    0x802D2470: table.sym("s_obj_shape_802D2470", table.GLOBL), # s callback
    0x802D2520: table.sym("s_obj_shape_802D2520", table.GLOBL), # s callback
    0x802D28CC: table.sym("s_obj_shape_802D28CC", table.GLOBL), # s callback

    # src/ripple.c
    0x802D29C0: table.sym("ripple_802D29C0"),
    0x802D2A74: table.sym("ripple_802D2A74"),
    0x802D2B08: table.sym("ripple_802D2B08"),
    0x802D2B84: table.sym("ripple_802D2B84"),
    0x802D2C40: table.sym("ripple_802D2C40"),
    0x802D2D80: table.sym("ripple_802D2D80"),
    0x802D2DFC: table.sym("ripple_802D2DFC"),
    0x802D2EB8: table.sym("ripple_802D2EB8"),
    0x802D2FFC: table.sym("ripple_802D2FFC"),
    0x802D319C: table.sym("ripple_802D319C"),
    0x802D327C: table.sym("ripple_802D327C"),
    0x802D341C: table.sym("ripple_802D341C"),
    0x802D34FC: table.sym("ripple_802D34FC"),
    0x802D36AC: table.sym("ripple_802D36AC"),
    0x802D379C: table.sym("ripple_802D379C"),
    0x802D393C: table.sym("ripple_802D393C"),
    0x802D3A2C: table.sym("ripple_802D3A2C"),
    0x802D3BEC: table.sym("ripple_802D3BEC"),
    0x802D3CEC: table.sym("ripple_802D3CEC"),
    0x802D3E6C: table.sym("ripple_802D3E6C"),
    0x802D3EE4: table.sym("ripple_802D3EE4"),
    0x802D404C: table.sym("ripple_802D404C"),
    0x802D43F8: table.sym("ripple_802D43F8"),
    0x802D44BC: table.sym("ripple_802D44BC"),
    0x802D47D0: table.sym("ripple_802D47D0"),
    0x802D4EDC: table.sym("ripple_802D4EDC"),
    0x802D50DC: table.sym("ripple_802D50DC"),
    0x802D5354: table.sym("ripple_802D5354"),
    0x802D556C: table.sym("ripple_802D556C"),
    0x802D568C: table.sym("ripple_802D568C"),
    0x802D5778: table.sym("ripple_802D5778"),
    0x802D57A8: table.sym("ripple_802D57A8"),
    0x802D58E4: table.sym("ripple_802D58E4"),
    0x802D593C: table.sym("ripple_802D593C"),
    0x802D59A8: table.sym("ripple_802D59A8"),
    0x802D5AA0: table.sym("ripple_802D5AA0"),
    0x802D5B98: table.sym("s_ripple_802D5B98", table.GLOBL), # s callback
    0x802D5D0C: table.sym("s_ripple_802D5D0C", table.GLOBL), # s callback

    # src/dprint.c
    0x802D5E00: table.sym_fnc("dprint_powi", "uint", (
        "int base",
        "int exponent",
    )),
    0x802D5E54: table.sym_fnc("dprintf_write", arg=(
        "int value",
        "int base",
        "char *buf",
        "int *index",
        "u8 digit",
        "s8 zero",
    )),
    0x802D6144: table.sym_fnc("dprintf_read", arg=(
        "const char *fmt",
        "int *index",
        "u8 *digit",
        "s8 *zero",
    )),
    0x802D62D8: table.sym_fnc("dprintf", arg=(
        "int x",
        "int y",
        "const char *fmt",
        "int value",
    ), flag=table.GLOBL),
    0x802D6554: table.sym_fnc("dprint", arg=(
        "int x",
        "int y",
        "const char *str",
    ), flag=table.GLOBL),
    0x802D66C0: table.sym_fnc("dprintc", arg=(
        "int x",
        "int y",
        "const char *str",
    ), flag=table.GLOBL),
    0x802D6858: table.sym_fnc("dprint_cvt", "char", (
        "char c",
    )),
    0x802D69F8: table.sym_fnc("dprint_draw_txt", arg=(
        "char c",
    )),
    0x802D6ACC: table.sym_fnc("dprint_clamp", arg=(
        "int *x",
        "int *y",
    )),
    0x802D6B3C: table.sym_fnc("dprint_draw_char", arg=(
        "int x",
        "int y",
        "int n",
    )),
    0x802D6C88: table.sym_fnc("dprint_draw", flag=table.GLOBL),

    # src/message.c
    0x802D6F20: table.sym("message_802D6F20"),
    0x802D7070: table.sym("message_802D7070", table.GLOBL),
    0x802D7174: table.sym("message_802D7174"),
    0x802D7280: table.sym("message_802D7280"),
    0x802D7384: table.sym("message_802D7384", table.GLOBL),
    0x802D7480: table.sym("message_802D7480"), # unused
    0x802D75DC: table.sym("message_802D75DC"),
    0x802D76C8: table.sym("message_802D76C8"),
    0x802D77DC: table.sym("message_802D77DC", table.GLOBL),
    0x802D7B84: table.sym("message_802D7B84", table.GLOBL),
    0x802D7E88: table.sym("message_802D7E88", table.GLOBL),
    0x802D82D4: table.sym("message_802D82D4"),
    0x802D862C: table.sym("message_802D862C", table.GLOBL),
    0x802D8844: table.sym("message_802D8844", table.GLOBL),
    0x802D8934: table.sym("message_802D8934"),
    0x802D89B8: table.sym("message_802D89B8", table.GLOBL),
    0x802D8A80: table.sym("message_802D8A80"),
    0x802D8B34: table.sym("message_802D8B34", table.GLOBL),
    0x802D8C6C: table.sym("message_802D8C6C", table.GLOBL),
    0x802D8C88: table.sym("message_802D8C88", table.GLOBL),
    0x802D8CC4: table.sym("message_802D8CC4", table.GLOBL),
    0x802D8D08: table.sym("message_802D8D08", table.GLOBL),
    0x802D8D48: table.sym("message_802D8D48", table.GLOBL),
    0x802D8D90: table.sym("message_802D8D90", table.GLOBL),
    0x802D8E2C: table.sym("message_802D8E2C"),
    0x802D9148: table.sym("message_802D9148"),
    0x802D9388: table.sym("message_802D9388"),
    0x802D944C: table.sym("message_802D944C"),
    0x802D9634: table.sym("message_802D9634"),
    0x802D9800: table.sym("message_802D9800"),
    0x802D982C: table.sym("message_802D982C"),
    0x802D99D4: table.sym_fnc("L802D99D4", flag=table.GLOBL|table.LOCAL),
    0x802D9A10: table.sym_fnc("L802D9A10", flag=table.GLOBL|table.LOCAL),
    0x802D9A40: table.sym_fnc("L802D9A40", flag=table.GLOBL|table.LOCAL),
    0x802D9A50: table.sym_fnc("L802D9A50", flag=table.GLOBL|table.LOCAL),
    0x802D9A80: table.sym_fnc("L802D9A80", flag=table.GLOBL|table.LOCAL),
    0x802D9AA0: table.sym_fnc("L802D9AA0", flag=table.GLOBL|table.LOCAL),
    0x802D9AD4: table.sym_fnc("L802D9AD4", flag=table.GLOBL|table.LOCAL),
    0x802D9B08: table.sym_fnc("L802D9B08", flag=table.GLOBL|table.LOCAL),
    0x802D9B1C: table.sym_fnc("L802D9B1C", flag=table.GLOBL|table.LOCAL),
    0x802D9CB0: table.sym("message_802D9CB0"),
    0x802D9DFC: table.sym("message_802D9DFC"),
    0x802D9F84: table.sym("message_802D9F84"),
    0x802DA1AC: table.sym("message_802DA1AC"),
    0x802DA810: table.sym("message_802DA810", table.GLOBL),
    0x802DA844: table.sym("message_802DA844", table.GLOBL),
    0x802DA85C: table.sym("message_802DA85C", table.GLOBL),
    0x802DA8E4: table.sym("message_802DA8E4", table.GLOBL),
    0x802DA964: table.sym("message_802DA964"),
    0x802DAA34: table.sym("message_802DAA34", table.GLOBL),
    0x802DAAE4: table.sym("message_802DAAE4", table.GLOBL),
    0x802DAB58: table.sym("message_802DAB58", table.GLOBL),
    0x802DAD54: table.sym("message_802DAD54"),
    0x802DB08C: table.sym("message_802DB08C", table.GLOBL),
    0x802DB350: table.sym("message_802DB350", table.GLOBL),
    0x802DB368: table.sym("message_802DB368"),
    0x802DB3B8: table.sym("message_802DB3B8"),
    0x802DB498: table.sym("message_802DB498"),
    0x802DB6E8: table.sym("message_802DB6E8"),
    0x802DB760: table.sym("message_802DB760"),
    0x802DBB24: table.sym("message_802DBB24"),
    0x802DBE68: table.sym("message_802DBE68"),
    0x802DC15C: table.sym("message_802DC15C"),
    0x802DC418: table.sym("message_802DC418"),
    0x802DC478: table.sym("message_802DC478"),
    0x802DC570: table.sym("message_802DC570"),
    0x802DC718: table.sym("message_802DC718"),
    0x802DCA88: table.sym("message_802DCA88"),
    0x802DCD04: table.sym("message_802DCD04"),
    0x802DCF30: table.sym("message_802DCF30"),
    0x802DD194: table.sym("message_802DD194"),
    0x802DD210: table.sym("message_802DD210"),
    0x802DD838: table.sym("message_802DD838"),
    0x802DDAE0: table.sym("message_802DDAE0"),
    0x802DDCA4: table.sym("message_802DDCA4", table.GLOBL),

    # src/weather_snow.c
    0x802DDDF0: table.sym("weather_snow_802DDDF0"),
    0x802DDF38: table.sym("weather_snow_802DDF38"),
    0x802DE0BC: table.sym("weather_snow_802DE0BC"),
    0x802DE114: table.sym("weather_snow_802DE114", table.GLOBL),
    0x802DE23C: table.sym("weather_snow_802DE23C"),
    0x802DE360: table.sym("weather_snow_802DE360"),
    0x802DE458: table.sym("weather_snow_802DE458"),
    0x802DE888: table.sym("weather_snow_802DE888"),
    0x802DECD4: table.sym("weather_snow_802DECD4"), # unused
    0x802DED38: table.sym("weather_snow_802DED38"),
    0x802DEF2C: table.sym("weather_snow_802DEF2C", table.GLOBL),
    0x802DF334: table.sym("weather_snow_802DF334"),
    0x802DF748: table.sym("weather_snow_802DF748"),
    0x802DFBC8: table.sym("weather_snow_802DFBC8", table.GLOBL),

    # src/weather_lava.c
    0x802DFD50: table.sym("weather_lava_802DFD50"),
    0x802DFE00: table.sym("weather_lava_802DFE00"),
    0x802DFE80: table.sym("weather_lava_802DFE80"),
    0x802E0120: table.sym("weather_lava_802E0120"),
    0x802E048C: table.sym("weather_lava_802E048C"),
    0x802E065C: table.sym("weather_lava_802E065C"),
    0x802E08A8: table.sym("weather_lava_802E08A8"),
    0x802E0934: table.sym("weather_lava_802E0934"),
    0x802E0E24: table.sym("weather_lava_802E0E24"),
    0x802E0EB8: table.sym("weather_lava_802E0EB8"),
    0x802E1238: table.sym("weather_lava_802E1238"),
    0x802E126C: table.sym_fnc("L802E126C", flag=table.GLOBL|table.LOCAL),
    0x802E1274: table.sym_fnc("L802E1274", flag=table.GLOBL|table.LOCAL),
    0x802E1294: table.sym_fnc("L802E1294", flag=table.GLOBL|table.LOCAL),
    0x802E12B4: table.sym_fnc("L802E12B4", flag=table.GLOBL|table.LOCAL),
    0x802E12C8: table.sym_fnc("L802E12C8", flag=table.GLOBL|table.LOCAL),
    0x802E12DC: table.sym_fnc("L802E12DC", flag=table.GLOBL|table.LOCAL),
    0x802E1414: table.sym("weather_lava_802E1414"),
    0x802E1618: table.sym("weather_lava_802E1618"),
    0x802E1A20: table.sym("weather_lava_802E1A20"),
    0x802E1BB8: table.sym("weather_lava_802E1BB8"),
    0x802E1ED8: table.sym("weather_lava_802E1ED8"),
    0x802E1F48: table.sym("weather_lava_802E1F48", table.GLOBL),

    # src/obj_data.c
    0x802E20A0: table.sym("obj_data_802E20A0"),
    0x802E2134: table.sym("obj_data_802E2134"),
    0x802E21DC: table.sym("obj_data_802E21DC"),
    0x802E2284: table.sym("obj_data_802E2284"),
    0x802E233C: table.sym("obj_data_802E233C"), # unused
    0x802E2414: table.sym("obj_data_802E2414", table.GLOBL),
    0x802E2690: table.sym("obj_data_802E2690", table.GLOBL),
    0x802E2758: table.sym_fnc("L802E2758", flag=table.GLOBL|table.LOCAL),
    0x802E278C: table.sym_fnc("L802E278C", flag=table.GLOBL|table.LOCAL),
    0x802E27C0: table.sym_fnc("L802E27C0", flag=table.GLOBL|table.LOCAL),
    0x802E27F4: table.sym_fnc("L802E27F4", flag=table.GLOBL|table.LOCAL),
    0x802E2828: table.sym_fnc("L802E2828", flag=table.GLOBL|table.LOCAL),
    0x802E285C: table.sym_fnc("L802E285C", flag=table.GLOBL|table.LOCAL),
    0x802E2890: table.sym_fnc("L802E2890", flag=table.GLOBL|table.LOCAL),
    0x802E28C4: table.sym_fnc("L802E28C4", flag=table.GLOBL|table.LOCAL),
    0x802E28EC: table.sym("obj_data_802E28EC", table.GLOBL),
    0x802E2AAC: table.sym_fnc("L802E2AAC", flag=table.GLOBL|table.LOCAL),
    0x802E2AD8: table.sym_fnc("L802E2AD8", flag=table.GLOBL|table.LOCAL),
    0x802E2B30: table.sym_fnc("L802E2B30", flag=table.GLOBL|table.LOCAL),
    0x802E2BB0: table.sym_fnc("L802E2BB0", flag=table.GLOBL|table.LOCAL),
    0x802E2C5C: table.sym_fnc("L802E2C5C", flag=table.GLOBL|table.LOCAL),

    # src/hud.c
    0x802E2CF0: table.sym("hud_802E2CF0"),
    0x802E2E58: table.sym("hud_802E2E58"),
    0x802E30B4: table.sym("hud_802E30B4"),
    0x802E3214: table.sym("hud_802E3214"),
    0x802E33B8: table.sym("hud_802E33B8"),
    0x802E3430: table.sym("hud_802E3430"),
    0x802E34E4: table.sym("hud_802E34E4"),
    0x802E352C: table.sym("hud_802E352C"),
    0x802E3654: table.sym("hud_802E3654"),
    0x802E3744: table.sym("hud_802E3744"),
    0x802E37A8: table.sym("hud_802E37A8"),
    0x802E380C: table.sym("hud_802E380C"),
    0x802E38E4: table.sym("hud_802E38E4"),
    0x802E395C: table.sym("hud_802E395C"),
    0x802E3B1C: table.sym("hud_802E3B1C", table.GLOBL),
    0x802E3B3C: table.sym("hud_802E3B3C"),
    0x802E3D2C: table.sym("hud_802E3D2C", table.GLOBL),

    # src/object_b.c
    0x802E3E50: table.sym("object_b_802E3E50", table.GLOBL),
    0x802E3E68: table.sym("object_b_802E3E68"), # unused
    0x802E3F68: table.sym("object_b_802E3F68"),
    0x802E3FAC: table.sym("object_b_802E3FAC"),
    0x802E405C: table.sym("object_b_802E405C"),
    0x802E41A4: table.sym("object_b_802E41A4"),
    0x802E42E0: table.sym("object_b_802E42E0"),
    0x802E43E4: table.sym("object_b_802E43E4"),
    0x802E445C: table.sym("object_b_802E445C"),
    0x802E4814: table.sym("object_b_802E4814"),
    0x802E4CEC: table.sym("object_b_802E4CEC"),
    0x802E4D88: table.sym("object_b_802E4D88"),
    0x802E4E90: table.sym("object_b_802E4E90"),
    0x802E5114: table.sym("object_b_802E5114"),
    0x802E5160: table.sym("object_b_802E5160"),
    0x802E5208: table.sym("object_b_802E5208"),
    0x802E52B8: table.sym("object_b_802E52B8"),
    0x802E5360: table.sym("object_b_802E5360"),
    0x802E53F4: table.sym("object_b_802E53F4"),
    0x802E54B0: table.sym("object_b_802E54B0"),
    0x802E55D0: table.sym("object_b_802E55D0"),
    0x802E569C: table.sym("object_b_802E569C"),
    0x802E5760: table.sym("object_b_802E5760"),
    0x802E5824: table.sym("object_b_802E5824"),
    0x802E58B4: table.sym("object_b_802E58B4"),
    0x802E5948: table.sym("object_b_802E5948"),
    0x802E5A80: table.sym("object_b_802E5A80"),
    0x802E5B18: table.sym("object_b_802E5B18"),
    0x802E5C6C: table.sym("object_b_802E5C6C"),
    0x802E5D04: table.sym("object_b_802E5D04"), # unused
    0x802E5DE8: table.sym("object_b_802E5DE8"),
    0x802E5E6C: table.sym("object_b_802E5E6C"),
    0x802E5EA4: table.sym("object_b_802E5EA4"),
    0x802E5EE8: table.sym("object_b_802E5EE8", table.GLOBL), # o callback
    0x802E5F64: table.sym("object_b_802E5F64", table.GLOBL), # o callback
    0x802E6098: table.sym("object_b_802E6098", table.GLOBL), # o callback
    0x802E6114: table.sym("object_b_802E6114", table.GLOBL), # o callback
    0x802E62A4: table.sym("object_b_802E62A4", table.GLOBL), # o callback
    0x802E631C: table.sym("object_b_802E631C"),
    0x802E63EC: table.sym("object_b_802E63EC"),
    0x802E6474: table.sym("object_b_802E6474", table.GLOBL), # o callback
    0x802E64F0: table.sym_fnc("L802E64F0", flag=table.GLOBL|table.LOCAL),
    0x802E6540: table.sym_fnc("L802E6540", flag=table.GLOBL|table.LOCAL),
    0x802E6550: table.sym_fnc("L802E6550", flag=table.GLOBL|table.LOCAL),
    0x802E6570: table.sym_fnc("L802E6570", flag=table.GLOBL|table.LOCAL),
    0x802E65A8: table.sym_fnc("L802E65A8", flag=table.GLOBL|table.LOCAL),
    0x802E6628: table.sym("object_b_802E6628", table.GLOBL), # o callback
    0x802E6660: table.sym_fnc("L802E6660", flag=table.GLOBL|table.LOCAL),
    0x802E66D4: table.sym_fnc("L802E66D4", flag=table.GLOBL|table.LOCAL),
    0x802E66E4: table.sym_fnc("L802E66E4", flag=table.GLOBL|table.LOCAL),
    0x802E6704: table.sym_fnc("L802E6704", flag=table.GLOBL|table.LOCAL),
    0x802E673C: table.sym_fnc("L802E673C", flag=table.GLOBL|table.LOCAL),
    0x802E6790: table.sym("object_b_802E6790", table.GLOBL), # o callback
    0x802E67DC: table.sym("object_b_802E67DC", table.GLOBL), # o callback
    0x802E6A2C: table.sym("object_b_802E6A2C", table.GLOBL), # o callback
    0x802E6A8C: table.sym("object_b_802E6A8C"),
    0x802E6AF8: table.sym("object_b_802E6AF8"),
    0x802E6BD4: table.sym("object_b_802E6BD4"),
    0x802E6CF0: table.sym("object_b_802E6CF0"),
    0x802E6DC8: table.sym("object_b_802E6DC8"),
    0x802E6E84: table.sym("object_b_802E6E84"),
    0x802E6ED8: table.sym("object_b_802E6ED8"),
    0x802E7020: table.sym("object_b_802E7020"),
    0x802E7134: table.sym("object_b_802E7134"),
    0x802E7180: table.sym("object_b_802E7180"),
    0x802E7220: table.sym("object_b_802E7220"),
    0x802E7280: table.sym("object_b_802E7280"),
    0x802E7324: table.sym("object_b_802E7324"),
    0x802E742C: table.sym("object_b_802E742C", table.GLOBL), # o callback
    0x802E75A0: table.sym("object_b_802E75A0", table.GLOBL), # o callback
    0x802E76AC: table.sym("object_b_802E76AC", table.GLOBL), # o callback
    0x802E770C: table.sym("object_b_802E770C"),
    0x802E7814: table.sym("object_b_802E7814"),
    0x802E79DC: table.sym("object_b_802E79DC"),
    0x802E7B00: table.sym("object_b_802E7B00"),
    0x802E7BB0: table.sym("object_b_802E7BB0"),
    0x802E7C4C: table.sym("object_b_802E7C4C", table.GLOBL), # o callback
    0x802E7C90: table.sym("object_b_802E7C90", table.GLOBL), # o callback
    0x802E7D4C: table.sym("object_b_802E7D4C"),
    0x802E7E54: table.sym("object_b_802E7E54", table.GLOBL), # o callback
    0x802E7F70: table.sym("object_b_802E7F70", table.GLOBL), # o callback
    0x802E7FB8: table.sym("object_b_802E7FB8"),
    0x802E7FEC: table.sym("object_b_802E7FEC"),
    0x802E80DC: table.sym("object_b_802E80DC", table.GLOBL), # o callback
    0x802E82B0: table.sym("object_b_802E82B0", table.GLOBL), # o callback
    0x802E8388: table.sym("object_b_802E8388", table.GLOBL), # o callback
    0x802E844C: table.sym("object_b_802E844C"),
    0x802E84CC: table.sym("object_b_802E84CC"),
    0x802E8618: table.sym("object_b_802E8618"),
    0x802E885C: table.sym("object_b_802E885C"),
    0x802E8920: table.sym("object_b_802E8920"),
    0x802E89D4: table.sym("object_b_802E89D4", table.GLOBL), # o callback
    0x802E8A0C: table.sym_fnc("L802E8A0C", flag=table.GLOBL|table.LOCAL),
    0x802E8A64: table.sym_fnc("L802E8A64", flag=table.GLOBL|table.LOCAL),
    0x802E8A74: table.sym_fnc("L802E8A74", flag=table.GLOBL|table.LOCAL),
    0x802E8A90: table.sym_fnc("L802E8A90", flag=table.GLOBL|table.LOCAL),
    0x802E8AA0: table.sym_fnc("L802E8AA0", flag=table.GLOBL|table.LOCAL),
    0x802E8AE4: table.sym("object_b_802E8AE4", table.GLOBL), # o callback
    0x802E8C18: table.sym("object_b_802E8C18"),
    0x802E8D98: table.sym("object_b_802E8D98"),
    0x802E8ECC: table.sym("object_b_802E8ECC", table.GLOBL), # o callback
    0x802E8F68: table.sym("object_b_802E8F68", table.GLOBL), # o callback
    0x802E9018: table.sym("object_b_802E9018"),
    0x802E9278: table.sym("object_b_802E9278"),
    0x802E9470: table.sym("object_b_802E9470"),
    0x802E94E4: table.sym("object_b_802E94E4"),
    0x802E9548: table.sym("object_b_802E9548"),
    0x802E96C8: table.sym("object_b_802E96C8", table.GLOBL), # o callback
    0x802E9764: table.sym("object_b_802E9764", table.GLOBL), # o callback
    0x802E97FC: table.sym("object_b_802E97FC"),
    0x802E98C0: table.sym("object_b_802E98C0"),
    0x802E9A4C: table.sym("object_b_802E9A4C"),
    0x802E9CF4: table.sym("object_b_802E9CF4"),
    0x802E9D98: table.sym("object_b_802E9D98"),
    0x802E9F60: table.sym("object_b_802E9F60"),
    0x802EA144: table.sym("object_b_802EA144"),
    0x802EA258: table.sym("object_b_802EA258"),
    0x802EA3F0: table.sym("object_b_802EA3F0"),
    0x802EA4EC: table.sym("object_b_802EA4EC"),
    0x802EA588: table.sym("object_b_802EA588", table.GLOBL), # o callback
    0x802EA6A8: table.sym("object_b_802EA6A8", table.GLOBL), # o callback
    0x802EA6F8: table.sym("object_b_802EA6F8"),
    0x802EA75C: table.sym("object_b_802EA75C"),
    0x802EA7E0: table.sym("object_b_802EA7E0", table.GLOBL), # o callback
    0x802EA888: table.sym("object_b_802EA888", table.GLOBL), # o callback
    0x802EA934: table.sym("object_b_802EA934", table.GLOBL), # o callback
    0x802EAA10: table.sym("object_b_802EAA10", table.GLOBL), # o callback
    0x802EAA50: table.sym("object_b_802EAA50", table.GLOBL), # o callback
    0x802EAA8C: table.sym("object_b_802EAA8C", table.GLOBL), # o callback
    0x802EAAD0: table.sym("object_b_802EAAD0", table.GLOBL), # o callback
    0x802EABF0: table.sym("object_b_802EABF0", table.GLOBL), # o callback
    0x802EAC3C: table.sym("object_b_802EAC3C", table.GLOBL), # o callback
    0x802EAD3C: table.sym("object_b_802EAD3C", table.GLOBL), # o callback
    0x802EAEF8: table.sym("object_b_802EAEF8", table.GLOBL), # o callback
    0x802EAF84: table.sym("object_b_802EAF84"),
    0x802EB05C: table.sym("object_b_802EB05C", table.GLOBL), # o callback
    0x802EB104: table.sym("object_b_802EB104", table.GLOBL), # o callback
    0x802EB1C0: table.sym("object_b_802EB1C0"),
    0x802EB288: table.sym("object_b_802EB288"),
    0x802EB3F0: table.sym("object_b_802EB3F0"),
    0x802EB510: table.sym("object_b_802EB510"),
    0x802EB5C4: table.sym("object_b_802EB5C4"),
    0x802EB630: table.sym("object_b_802EB630"),
    0x802EB744: table.sym("object_b_802EB744"),
    0x802EB7E0: table.sym("object_b_802EB7E0"),
    0x802EB8B0: table.sym("object_b_802EB8B0"),
    0x802EB9D0: table.sym("object_b_802EB9D0", table.GLOBL), # o callback
    0x802EBB74: table.sym("object_b_802EBB74"),
    0x802EBC00: table.sym("object_b_802EBC00", table.GLOBL), # o callback
    0x802EBC88: table.sym("object_b_802EBC88"),
    0x802EBCE0: table.sym("object_b_802EBCE0", table.GLOBL), # o callback
    0x802EBD94: table.sym_fnc("L802EBD94", flag=table.GLOBL|table.LOCAL),
    0x802EBE04: table.sym_fnc("L802EBE04", flag=table.GLOBL|table.LOCAL),
    0x802EBE1C: table.sym_fnc("L802EBE1C", flag=table.GLOBL|table.LOCAL),
    0x802EBE34: table.sym_fnc("L802EBE34", flag=table.GLOBL|table.LOCAL),
    0x802EBE4C: table.sym_fnc("L802EBE4C", flag=table.GLOBL|table.LOCAL),
    0x802EBE9C: table.sym_fnc("L802EBE9C", flag=table.GLOBL|table.LOCAL),
    0x802EBF70: table.sym("object_b_802EBF70"),
    0x802EC030: table.sym("object_b_802EC030"),
    0x802EC1B0: table.sym("object_b_802EC1B0", table.GLOBL), # o callback
    0x802EC200: table.sym("object_b_802EC200"),
    0x802EC3D0: table.sym("object_b_802EC3D0"),
    0x802EC4E0: table.sym("object_b_802EC4E0"),
    0x802EC59C: table.sym("object_b_802EC59C"),
    0x802EC75C: table.sym("object_b_802EC75C", table.GLOBL), # o callback
    0x802EC7CC: table.sym("object_b_802EC7CC"), # unused
    0x802EC818: table.sym("object_b_802EC818"),
    0x802EC908: table.sym("object_b_802EC908", table.GLOBL), # o callback
    0x802EC9B8: table.sym("object_b_802EC9B8", table.GLOBL), # o callback
    0x802EC9F0: table.sym("object_b_802EC9F0"),
    0x802ECBA4: table.sym("object_b_802ECBA4", table.GLOBL), # o callback
    0x802ECC14: table.sym("object_b_802ECC14", table.GLOBL), # o callback
    0x802ECD0C: table.sym("object_b_802ECD0C", table.GLOBL), # o callback
    0x802ECEA0: table.sym("object_b_802ECEA0", table.GLOBL), # o callback
    0x802ECFAC: table.sym("object_b_802ECFAC", table.GLOBL), # o callback
    0x802ED10C: table.sym("object_b_802ED10C"),
    0x802ED28C: table.sym("object_b_802ED28C"),
    0x802ED39C: table.sym("object_b_802ED39C", table.GLOBL), # o callback
    0x802ED40C: table.sym("object_b_802ED40C", table.GLOBL), # o callback
    0x802ED45C: table.sym("object_b_802ED45C", table.GLOBL), # o callback
    0x802ED498: table.sym("object_b_802ED498", table.GLOBL), # o callback
    0x802ED62C: table.sym("object_b_802ED62C", table.GLOBL), # o callback
    0x802ED78C: table.sym("object_b_802ED78C", table.GLOBL), # o callback
    0x802ED7FC: table.sym("object_b_802ED7FC", table.GLOBL), # o callback
    0x802EDACC: table.sym("object_b_802EDACC", table.GLOBL), # o callback
    0x802EDB2C: table.sym("object_b_802EDB2C", table.GLOBL), # o callback
    0x802EDDFC: table.sym("object_b_802EDDFC", table.GLOBL), # o callback
    0x802EDF28: table.sym("object_b_802EDF28", table.GLOBL), # o callback
    0x802EE124: table.sym("object_b_802EE124", table.GLOBL), # o callback
    0x802EE1A0: table.sym("object_b_802EE1A0"),
    0x802EE268: table.sym("object_b_802EE268"),
    0x802EE2B8: table.sym_fnc("L802EE2B8", flag=table.GLOBL|table.LOCAL),
    0x802EE338: table.sym_fnc("L802EE338", flag=table.GLOBL|table.LOCAL),
    0x802EE390: table.sym_fnc("L802EE390", flag=table.GLOBL|table.LOCAL),
    0x802EE3C0: table.sym_fnc("L802EE3C0", flag=table.GLOBL|table.LOCAL),
    0x802EE42C: table.sym_fnc("L802EE42C", flag=table.GLOBL|table.LOCAL),
    0x802EE46C: table.sym("object_b_802EE46C"),
    0x802EE598: table.sym("object_b_802EE598"),
    0x802EE728: table.sym("object_b_802EE728"),
    0x802EE778: table.sym("object_b_802EE778"),
    0x802EE7E0: table.sym("object_b_802EE7E0", table.GLOBL), # o callback
    0x802EE818: table.sym_fnc("L802EE818", flag=table.GLOBL|table.LOCAL),
    0x802EE87C: table.sym_fnc("L802EE87C", flag=table.GLOBL|table.LOCAL),
    0x802EE8AC: table.sym_fnc("L802EE8AC", flag=table.GLOBL|table.LOCAL),
    0x802EE8BC: table.sym_fnc("L802EE8BC", flag=table.GLOBL|table.LOCAL),
    0x802EE8CC: table.sym_fnc("L802EE8CC", flag=table.GLOBL|table.LOCAL),
    0x802EE8F4: table.sym("object_b_802EE8F4", table.GLOBL), # o callback
    0x802EE9CC: table.sym("object_b_802EE9CC", table.GLOBL), # o callback
    0x802EEA24: table.sym("object_b_802EEA24"),
    0x802EEA7C: table.sym("object_b_802EEA7C"),
    0x802EEAB4: table.sym_fnc("L802EEAB4", flag=table.GLOBL|table.LOCAL),
    0x802EEAD4: table.sym_fnc("L802EEAD4", flag=table.GLOBL|table.LOCAL),
    0x802EEAF4: table.sym_fnc("L802EEAF4", flag=table.GLOBL|table.LOCAL),
    0x802EEB14: table.sym_fnc("L802EEB14", flag=table.GLOBL|table.LOCAL),
    0x802EEB30: table.sym_fnc("L802EEB30", flag=table.GLOBL|table.LOCAL),
    0x802EEB64: table.sym("object_b_802EEB64"),
    0x802EECB8: table.sym("object_b_802EECB8"),
    0x802EED14: table.sym_fnc("L802EED14", flag=table.GLOBL|table.LOCAL),
    0x802EED34: table.sym_fnc("L802EED34", flag=table.GLOBL|table.LOCAL),
    0x802EED54: table.sym_fnc("L802EED54", flag=table.GLOBL|table.LOCAL),
    0x802EED74: table.sym_fnc("L802EED74", flag=table.GLOBL|table.LOCAL),
    0x802EED94: table.sym_fnc("L802EED94", flag=table.GLOBL|table.LOCAL),
    0x802EEDF0: table.sym("object_b_802EEDF0", table.GLOBL), # o callback
    0x802EEEB4: table.sym("object_b_802EEEB4", table.GLOBL), # o callback
    0x802EEF9C: table.sym("object_b_802EEF9C", table.GLOBL), # o callback
    0x802EF0E8: table.sym("object_b_802EF0E8", table.GLOBL), # o callback
    0x802EF21C: table.sym("object_b_802EF21C", table.GLOBL), # o callback
    0x802EF274: table.sym("object_b_802EF274", table.GLOBL), # o callback
    0x802EF34C: table.sym("object_b_802EF34C", table.GLOBL), # o callback
    0x802EF3F4: table.sym("object_b_802EF3F4"),
    0x802EF524: table.sym("object_b_802EF524", table.GLOBL), # o callback
    0x802EF63C: table.sym("object_b_802EF63C", table.GLOBL), # o callback
    0x802EF66C: table.sym("object_b_802EF66C", table.GLOBL), # o callback
    0x802EF820: table.sym("object_b_802EF820", table.GLOBL), # o callback
    0x802EF858: table.sym("object_b_802EF858", table.GLOBL), # o callback
    0x802EFCD0: table.sym("object_b_802EFCD0", table.GLOBL), # o callback
    0x802EFD8C: table.sym("object_b_802EFD8C", table.GLOBL), # o callback
    0x802EFE64: table.sym("object_b_802EFE64", table.GLOBL), # o callback
    0x802EFEF4: table.sym("object_b_802EFEF4", table.GLOBL), # o callback
    0x802F0104: table.sym("object_b_802F0104", table.GLOBL), # o callback
    0x802F0168: table.sym("object_b_802F0168", table.GLOBL), # o callback
    0x802F0288: table.sym("object_b_802F0288"),
    0x802F04A0: table.sym("object_b_802F04A0"),
    0x802F05B4: table.sym("object_b_802F05B4", table.GLOBL), # o callback
    0x802F06A8: table.sym("object_b_802F06A8", table.GLOBL), # o callback
    0x802F0714: table.sym("object_b_802F0714", table.GLOBL), # o callback
    0x802F0788: table.sym("object_b_802F0788", table.GLOBL), # o callback
    0x802F07F4: table.sym("object_b_802F07F4", table.GLOBL), # o callback
    0x802F0820: table.sym("object_b_802F0820", table.GLOBL), # o callback
    0x802F084C: table.sym("object_b_802F084C", table.GLOBL), # o callback
    0x802F0898: table.sym("object_b_802F0898", table.GLOBL), # o callback
    0x802F0950: table.sym("object_b_802F0950", table.GLOBL), # o callback
    0x802F09A4: table.sym("object_b_802F09A4", table.GLOBL), # o callback
    0x802F09F0: table.sym("object_b_802F09F0", table.GLOBL), # o callback
    0x802F0A40: table.sym("object_b_802F0A40", table.GLOBL), # o callback
    0x802F0B7C: table.sym("object_b_802F0B7C"),
    0x802F0BD4: table.sym("object_b_802F0BD4"),
    0x802F0C94: table.sym("object_b_802F0C94"),
    0x802F0DF0: table.sym("object_b_802F0DF0"),
    0x802F0FA8: table.sym("object_b_802F0FA8"),
    0x802F105C: table.sym("object_b_802F105C", table.GLOBL), # o callback
    0x802F1094: table.sym_fnc("L802F1094", flag=table.GLOBL|table.LOCAL),
    0x802F112C: table.sym_fnc("L802F112C", flag=table.GLOBL|table.LOCAL),
    0x802F1158: table.sym_fnc("L802F1158", flag=table.GLOBL|table.LOCAL),
    0x802F1184: table.sym_fnc("L802F1184", flag=table.GLOBL|table.LOCAL),
    0x802F1194: table.sym_fnc("L802F1194", flag=table.GLOBL|table.LOCAL),
    0x802F120C: table.sym("object_b_802F120C", table.GLOBL), # o callback
    0x802F1370: table.sym("object_b_802F1370", table.GLOBL), # o callback
    0x802F13A8: table.sym_fnc("L802F13A8", flag=table.GLOBL|table.LOCAL),
    0x802F13E4: table.sym_fnc("L802F13E4", flag=table.GLOBL|table.LOCAL),
    0x802F13EC: table.sym_fnc("L802F13EC", flag=table.GLOBL|table.LOCAL),
    0x802F1420: table.sym_fnc("L802F1420", flag=table.GLOBL|table.LOCAL),
    0x802F148C: table.sym_fnc("L802F148C", flag=table.GLOBL|table.LOCAL),
    0x802F151C: table.sym("object_b_802F151C", table.GLOBL), # o callback
    0x802F15A8: table.sym("object_b_802F15A8", table.GLOBL), # o callback
    0x802F162C: table.sym("object_b_802F162C"),
    0x802F1714: table.sym("object_b_802F1714", table.GLOBL), # o callback
    0x802F17F0: table.sym("object_b_802F17F0", table.GLOBL), # o callback
    0x802F1954: table.sym("object_b_802F1954"),
    0x802F19C8: table.sym("object_b_802F19C8"),
    0x802F1A10: table.sym("object_b_802F1A10"),
    0x802F1A5C: table.sym_fnc("L802F1A5C", flag=table.GLOBL|table.LOCAL),
    0x802F1A70: table.sym_fnc("L802F1A70", flag=table.GLOBL|table.LOCAL),
    0x802F1A9C: table.sym_fnc("L802F1A9C", flag=table.GLOBL|table.LOCAL),
    0x802F1B0C: table.sym_fnc("L802F1B0C", flag=table.GLOBL|table.LOCAL),
    0x802F1B38: table.sym_fnc("L802F1B38", flag=table.GLOBL|table.LOCAL),
    0x802F1BA8: table.sym_fnc("L802F1BA8", flag=table.GLOBL|table.LOCAL),
    0x802F1BB8: table.sym("object_b_802F1BB8"),
    0x802F1D64: table.sym("object_b_802F1D64", table.GLOBL), # o callback
    0x802F1DC0: table.sym("object_b_802F1DC0"),
    0x802F1E5C: table.sym("object_b_802F1E5C"),
    0x802F1F3C: table.sym("object_b_802F1F3C", table.GLOBL), # o callback
    0x802F1FD0: table.sym("object_b_802F1FD0", table.GLOBL), # o callback
    0x802F2030: table.sym("object_b_802F2030"),
    0x802F20AC: table.sym("object_b_802F20AC", table.GLOBL), # o callback
    0x802F2140: table.sym("object_b_802F2140", table.GLOBL), # o callback
    0x802F21E0: table.sym("object_b_802F21E0"),
    0x802F2284: table.sym("object_b_802F2284"),
    0x802F23A8: table.sym("object_b_802F23A8", table.GLOBL), # o callback
    0x802F2498: table.sym("object_b_802F2498", table.GLOBL), # o callback
    0x802F24F4: table.sym("object_b_802F24F4", table.GLOBL), # o callback
    0x802F25B0: table.sym("object_b_802F25B0", table.GLOBL), # o callback
    0x802F2614: table.sym("object_b_802F2614", table.GLOBL), # o callback
    0x802F2768: table.sym("object_b_802F2768", table.GLOBL), # o callback
    0x802F2AA0: table.sym("object_b_802F2AA0"),
    0x802F2B88: table.sym("object_b_802F2B88", table.GLOBL),
    0x802F2BD4: table.sym("object_b_802F2BD4"),
    0x802F2C24: table.sym("object_b_802F2C24"),
    0x802F2C84: table.sym("object_b_802F2C84", table.GLOBL), # o callback
    0x802F2D8C: table.sym("object_b_802F2D8C", table.GLOBL), # o callback
    0x802F2E6C: table.sym("object_b_802F2E6C", table.GLOBL), # o callback
    0x802F2F2C: table.sym("object_b_802F2F2C", table.GLOBL), # o callback
    0x802F3014: table.sym("object_b_802F3014", table.GLOBL), # o callback
    0x802F30F0: table.sym("object_b_802F30F0", table.GLOBL), # o callback
    0x802F31BC: table.sym("object_b_802F31BC", table.GLOBL), # o callback
    0x802F328C: table.sym("object_b_802F328C", table.GLOBL), # o callback
    0x802F336C: table.sym("object_b_802F336C", table.GLOBL), # o callback
    0x802F341C: table.sym("object_b_802F341C"),
    0x802F36A4: table.sym("object_b_802F36A4", table.GLOBL), # o callback
    0x802F38B0: table.sym("object_b_802F38B0"),
    0x802F39B4: table.sym("object_b_802F39B4"),
    0x802F3A30: table.sym("object_b_802F3A30", table.GLOBL), # o callback
    0x802F3B98: table.sym("object_b_802F3B98", table.GLOBL), # o callback
    0x802F3C54: table.sym("object_b_802F3C54"),
    0x802F3CC8: table.sym("object_b_802F3CC8", table.GLOBL), # o callback
    0x802F3D30: table.sym("object_b_802F3D30", table.GLOBL), # o callback
    0x802F3DD0: table.sym("object_b_802F3DD0"),
    0x802F3EA8: table.sym("object_b_802F3EA8"),
    0x802F401C: table.sym("object_b_802F401C"),
    0x802F40CC: table.sym("object_b_802F40CC", table.GLOBL), # o callback
    0x802F4248: table.sym("object_b_802F4248", table.GLOBL), # o callback
    0x802F43B8: table.sym("object_b_802F43B8"),
    0x802F44C0: table.sym("object_b_802F44C0", table.GLOBL), # o callback
    0x802F45B8: table.sym("object_b_802F45B8", table.GLOBL), # o callback
    0x802F45F0: table.sym("object_b_802F45F0", table.GLOBL), # o callback
    0x802F4710: table.sym("object_b_802F4710", table.GLOBL), # o callback
    0x802F48F4: table.sym("object_b_802F48F4", table.GLOBL), # o callback
    0x802F496C: table.sym("object_b_802F496C", table.GLOBL), # o callback
    0x802F4B00: table.sym("object_b_802F4B00", table.GLOBL), # o callback
    0x802F4B78: table.sym("object_b_802F4B78", table.GLOBL), # o callback
    0x802F4C68: table.sym("object_b_802F4C68"),
    0x802F4CE0: table.sym("object_b_802F4CE0"),
    0x802F4D78: table.sym("object_b_802F4D78", table.GLOBL), # o callback
    0x802F4EB4: table.sym("object_b_802F4EB4", table.GLOBL), # o callback
    0x802F5010: table.sym("object_b_802F5010"),
    0x802F5068: table.sym("object_b_802F5068"),
    0x802F52C0: table.sym("object_b_802F52C0"),
    0x802F547C: table.sym("object_b_802F547C"),
    0x802F55A4: table.sym("object_b_802F55A4", table.GLOBL), # o callback
    0x802F5618: table.sym_fnc("L802F5618", flag=table.GLOBL|table.LOCAL),
    0x802F56A0: table.sym_fnc("L802F56A0", flag=table.GLOBL|table.LOCAL),
    0x802F57E8: table.sym_fnc("L802F57E8", flag=table.GLOBL|table.LOCAL),
    0x802F5930: table.sym_fnc("L802F5930", flag=table.GLOBL|table.LOCAL),
    0x802F5A78: table.sym_fnc("L802F5A78", flag=table.GLOBL|table.LOCAL),
    0x802F5BC0: table.sym_fnc("L802F5BC0", flag=table.GLOBL|table.LOCAL),
    0x802F5BD8: table.sym_fnc("L802F5BD8", flag=table.GLOBL|table.LOCAL),
    0x802F5CD4: table.sym("object_b_802F5CD4", table.GLOBL), # o callback
    0x802F5D78: table.sym("object_b_802F5D78"),
    0x802F5E44: table.sym("object_b_802F5E44"),
    0x802F5F48: table.sym("object_b_802F5F48"),
    0x802F6014: table.sym("object_b_802F6014"),
    0x802F60D8: table.sym("object_b_802F60D8"),
    0x802F6150: table.sym("object_b_802F6150"),
    0x802F6228: table.sym("object_b_802F6228", table.GLOBL), # o callback
    0x802F62E4: table.sym("object_b_802F62E4", table.GLOBL), # o callback
    0x802F6448: table.sym("object_b_802F6448", table.GLOBL), # o callback
    0x802F6588: table.sym("object_b_802F6588"),
    0x802F665C: table.sym("object_b_802F665C"),
    0x802F6984: table.sym("object_b_802F6984", table.GLOBL), # o callback
    0x802F6A44: table.sym("object_b_802F6A44"),
    0x802F6B2C: table.sym("object_b_802F6B2C"),
    0x802F6C0C: table.sym("object_b_802F6C0C", table.GLOBL), # o callback
    0x802F6D20: table.sym("object_b_802F6D20", table.GLOBL), # o callback
    0x802F6D58: table.sym("object_b_802F6D58", table.GLOBL), # o callback
    0x802F6E40: table.sym("object_b_802F6E40", table.GLOBL), # o callback
    0x802F6EB0: table.sym("object_b_802F6EB0"),
    0x802F7068: table.sym("object_b_802F7068"),
    0x802F7264: table.sym("object_b_802F7264", table.GLOBL), # o callback
    0x802F7348: table.sym("object_b_802F7348", table.GLOBL), # o callback
    0x802F7398: table.sym("object_b_802F7398"),
    0x802F7418: table.sym("object_b_802F7418"),
    0x802F74DC: table.sym("object_b_802F74DC", table.GLOBL), # o callback
    0x802F7760: table.sym("object_b_802F7760", table.GLOBL), # o callback
    0x802F7924: table.sym("object_b_802F7924", table.GLOBL), # o callback
    0x802F7978: table.sym("object_b_802F7978", table.GLOBL), # o callback
    0x802F79B0: table.sym("object_b_802F79B0", table.GLOBL), # o callback
    0x802F7A58: table.sym("object_b_802F7A58", table.GLOBL), # o callback
    0x802F7C9C: table.sym("object_b_802F7C9C", table.GLOBL), # o callback
    0x802F7D04: table.sym("object_b_802F7D04", table.GLOBL), # o callback
    0x802F7F1C: table.sym("object_b_802F7F1C"),
    0x802F7FA0: table.sym("object_b_802F7FA0", table.GLOBL), # o callback
    0x802F8044: table.sym("object_b_802F8044", table.GLOBL), # o callback
    0x802F8158: table.sym("object_b_802F8158", table.GLOBL), # o callback
    0x802F8208: table.sym("object_b_802F8208", table.GLOBL), # o callback
    0x802F82F8: table.sym("object_b_802F82F8", table.GLOBL), # o callback
    0x802F83A4: table.sym("object_b_802F83A4", table.GLOBL), # o callback
    0x802F8490: table.sym("object_b_802F8490", table.GLOBL), # o callback
    0x802F85E0: table.sym("object_b_802F85E0"),
    0x802F8760: table.sym("object_b_802F8760"),
    0x802F8808: table.sym("object_b_802F8808"),
    0x802F893C: table.sym("object_b_802F893C"),
    0x802F8988: table.sym("object_b_802F8988"),
    0x802F8A34: table.sym("object_b_802F8A34"),
    0x802F8AB4: table.sym("object_b_802F8AB4"),
    0x802F8AEC: table.sym_fnc("L802F8AEC", flag=table.GLOBL|table.LOCAL),
    0x802F8AFC: table.sym_fnc("L802F8AFC", flag=table.GLOBL|table.LOCAL),
    0x802F8B0C: table.sym_fnc("L802F8B0C", flag=table.GLOBL|table.LOCAL),
    0x802F8B1C: table.sym_fnc("L802F8B1C", flag=table.GLOBL|table.LOCAL),
    0x802F8B2C: table.sym_fnc("L802F8B2C", flag=table.GLOBL|table.LOCAL),
    0x802F8B54: table.sym("object_b_802F8B54"),
    0x802F8C74: table.sym("object_b_802F8C74"),
    0x802F8CF8: table.sym("object_b_802F8CF8"),
    0x802F8DAC: table.sym("object_b_802F8DAC", table.GLOBL), # o callback
    0x802F8E54: table.sym("object_b_802F8E54", table.GLOBL), # o callback
    0x802F8F08: table.sym("object_b_802F8F08"),
    0x802F9054: table.sym("object_b_802F9054"),
    0x802F923C: table.sym("object_b_802F923C"),
    0x802F93A8: table.sym("object_b_802F93A8"),
    0x802F9500: table.sym("object_b_802F9500"),
    0x802F95AC: table.sym("object_b_802F95AC"),
    0x802F965C: table.sym("object_b_802F965C", table.GLOBL), # o callback
    0x802F9694: table.sym_fnc("L802F9694", flag=table.GLOBL|table.LOCAL),
    0x802F96A4: table.sym_fnc("L802F96A4", flag=table.GLOBL|table.LOCAL),
    0x802F96B4: table.sym_fnc("L802F96B4", flag=table.GLOBL|table.LOCAL),
    0x802F96C4: table.sym_fnc("L802F96C4", flag=table.GLOBL|table.LOCAL),
    0x802F96D4: table.sym_fnc("L802F96D4", flag=table.GLOBL|table.LOCAL),
    0x802F96E4: table.sym_fnc("L802F96E4", flag=table.GLOBL|table.LOCAL),
    0x802F96F4: table.sym_fnc("L802F96F4", flag=table.GLOBL|table.LOCAL),
    0x802F9704: table.sym_fnc("L802F9704", flag=table.GLOBL|table.LOCAL),

    # src/object_c.c
    0x802F9730: table.sym("object_c_802F9730"),
    0x802F9770: table.sym("object_c_802F9770"),
    0x802F97BC: table.sym("object_c_802F97BC"),
    0x802F9820: table.sym("object_c_802F9820"),
    0x802F9890: table.sym("object_c_802F9890"),
    0x802F9904: table.sym("object_c_802F9904"),
    0x802F9A28: table.sym("object_c_802F9A28"),
    0x802F9E28: table.sym("object_c_802F9E28"),
    0x802FA158: table.sym("object_c_802FA158"),
    0x802FA1B0: table.sym("object_c_802FA1B0"),
    0x802FA1F8: table.sym("object_c_802FA1F8"),
    0x802FA25C: table.sym("object_c_802FA25C"),
    0x802FA2BC: table.sym("object_c_802FA2BC"),
    0x802FA32C: table.sym("object_c_802FA32C"),
    0x802FA360: table.sym("object_c_802FA360"),
    0x802FA39C: table.sym("object_c_802FA39C"),
    0x802FA3DC: table.sym("object_c_802FA3DC"),
    0x802FA428: table.sym("object_c_802FA428"),
    0x802FA4C4: table.sym("object_c_802FA4C4"),
    0x802FA544: table.sym("object_c_802FA544"),
    0x802FA5D0: table.sym("object_c_802FA5D0"),
    0x802FA618: table.sym("object_c_802FA618"),
    0x802FA660: table.sym("object_c_802FA660"),
    0x802FA6D4: table.sym("object_c_802FA6D4"),
    0x802FA748: table.sym("object_c_802FA748"),
    0x802FA7BC: table.sym("object_c_802FA7BC"),
    0x802FA830: table.sym("object_c_802FA830"),
    0x802FA900: table.sym("object_c_802FA900"),
    0x802FA964: table.sym("object_c_802FA964"),
    0x802FA9D8: table.sym("object_c_802FA9D8"),
    0x802FAA64: table.sym("object_c_802FAA64"),
    0x802FAAC8: table.sym("object_c_802FAAC8"),
    0x802FAC18: table.sym("object_c_802FAC18"),
    0x802FAD34: table.sym("object_c_802FAD34"),
    0x802FADD4: table.sym("object_c_802FADD4"),
    0x802FB01C: table.sym("object_c_802FB01C"),
    0x802FB0CC: table.sym("object_c_802FB0CC"),
    0x802FB128: table.sym("object_c_802FB128"),
    0x802FB254: table.sym("object_c_802FB254"), # unused
    0x802FB288: table.sym("object_c_802FB288"),
    0x802FB3A0: table.sym("object_c_802FB3A0"),
    0x802FB3DC: table.sym("object_c_802FB3DC"),
    0x802FB518: table.sym("object_c_802FB518"),
    0x802FB610: table.sym_fnc("L802FB610", flag=table.GLOBL|table.LOCAL),
    0x802FB618: table.sym_fnc("L802FB618", flag=table.GLOBL|table.LOCAL),
    0x802FB628: table.sym_fnc("L802FB628", flag=table.GLOBL|table.LOCAL),
    0x802FB638: table.sym_fnc("L802FB638", flag=table.GLOBL|table.LOCAL),
    0x802FB648: table.sym_fnc("L802FB648", flag=table.GLOBL|table.LOCAL),
    0x802FB658: table.sym_fnc("L802FB658", flag=table.GLOBL|table.LOCAL),
    0x802FB668: table.sym_fnc("L802FB668", flag=table.GLOBL|table.LOCAL),
    0x802FB678: table.sym_fnc("L802FB678", flag=table.GLOBL|table.LOCAL),
    0x802FB688: table.sym_fnc("L802FB688", flag=table.GLOBL|table.LOCAL),
    0x802FB6E8: table.sym("object_c_802FB6E8"),
    0x802FB778: table.sym("object_c_802FB778"),
    0x802FB87C: table.sym("object_c_802FB87C"),
    0x802FB938: table.sym("object_c_802FB938"),
    0x802FBA40: table.sym("object_c_802FBA40"),
    0x802FBAB4: table.sym("object_c_802FBAB4"),
    0x802FBC4C: table.sym("object_c_802FBC4C", table.GLOBL), # o callback
    0x802FBD5C: table.sym("object_c_802FBD5C"),
    0x802FBDD4: table.sym("object_c_802FBDD4"),
    0x802FBE50: table.sym("object_c_802FBE50"),
    0x802FBECC: table.sym("object_c_802FBECC"),
    0x802FBF58: table.sym("object_c_802FBF58"),
    0x802FBFDC: table.sym("object_c_802FBFDC"),
    0x802FC03C: table.sym("object_c_802FC03C"),
    0x802FC16C: table.sym("object_c_802FC16C"),
    0x802FC288: table.sym("object_c_802FC288"),
    0x802FC338: table.sym("object_c_802FC338"),
    0x802FC414: table.sym("object_c_802FC414"),
    0x802FC510: table.sym("object_c_802FC510"),
    0x802FC670: table.sym("object_c_802FC670"),
    0x802FC914: table.sym("object_c_802FC914"),
    0x802FCAF4: table.sym("object_c_802FCAF4"),
    0x802FCB1C: table.sym("object_c_802FCB1C"),
    0x802FCC00: table.sym("object_c_802FCC00"),
    0x802FCCC8: table.sym("object_c_802FCCC8"),
    0x802FCD64: table.sym("object_c_802FCD64"),
    0x802FCE94: table.sym("object_c_802FCE94"),
    0x802FD014: table.sym("object_c_802FD014"),
    0x802FD068: table.sym("object_c_802FD068"),
    0x802FD3E4: table.sym("object_c_802FD3E4"),
    0x802FD464: table.sym("object_c_802FD464"),
    0x802FD4B0: table.sym("object_c_802FD4B0"),
    0x802FD6AC: table.sym("object_c_802FD6AC"),
    0x802FD708: table.sym_fnc("L802FD708", flag=table.GLOBL|table.LOCAL),
    0x802FD718: table.sym_fnc("L802FD718", flag=table.GLOBL|table.LOCAL),
    0x802FD728: table.sym_fnc("L802FD728", flag=table.GLOBL|table.LOCAL),
    0x802FD738: table.sym_fnc("L802FD738", flag=table.GLOBL|table.LOCAL),
    0x802FD748: table.sym_fnc("L802FD748", flag=table.GLOBL|table.LOCAL),
    0x802FD758: table.sym_fnc("L802FD758", flag=table.GLOBL|table.LOCAL),
    0x802FD7F8: table.sym("object_c_802FD7F8", table.GLOBL), # o callback
    0x802FD950: table.sym("object_c_802FD950", table.GLOBL), # o callback
    0x802FDA28: table.sym("object_c_802FDA28", table.GLOBL), # o callback
    0x802FDEA8: table.sym("object_c_802FDEA8"),
    0x802FDFC4: table.sym("object_c_802FDFC4"),
    0x802FE37C: table.sym("object_c_802FE37C"),
    0x802FE3B0: table.sym("object_c_802FE3B0", table.GLOBL), # o callback
    0x802FE450: table.sym("object_c_802FE450"),
    0x802FE520: table.sym("object_c_802FE520"),
    0x802FE8B4: table.sym("object_c_802FE8B4", table.GLOBL), # o callback
    0x802FE988: table.sym("object_c_802FE988"),
    0x802FEB00: table.sym("object_c_802FEB00"),
    0x802FED50: table.sym("object_c_802FED50"),
    0x802FEF18: table.sym("object_c_802FEF18"),
    0x802FF040: table.sym("object_c_802FF040", table.GLOBL), # o callback
    0x802FF214: table.sym("object_c_802FF214", table.GLOBL), # o callback
    0x802FF408: table.sym("object_c_802FF408", table.GLOBL), # o callback
    0x802FF518: table.sym("object_c_802FF518"),
    0x802FF584: table.sym("object_c_802FF584"),
    0x802FF600: table.sym("object_c_802FF600"),
    0x802FF868: table.sym("object_c_802FF868"),
    0x802FF8E8: table.sym("object_c_802FF8E8"),
    0x802FF94C: table.sym("object_c_802FF94C"),
    0x802FF96C: table.sym("object_c_802FF96C", table.GLOBL), # o callback
    0x802FFB38: table.sym("object_c_802FFB38", table.GLOBL), # o callback
    0x802FFC60: table.sym("object_c_802FFC60"),
    0x802FFDAC: table.sym("object_c_802FFDAC"),
    0x8030009C: table.sym("object_c_8030009C"),
    0x803000E4: table.sym("object_c_803000E4"),
    0x803002F4: table.sym("object_c_803002F4"),
    0x803004F0: table.sym("object_c_803004F0"),
    0x8030059C: table.sym("object_c_8030059C"),
    0x80300778: table.sym("object_c_80300778"),
    0x803008A8: table.sym("object_c_803008A8"),
    0x803008EC: table.sym("object_c_803008EC"),
    0x80300940: table.sym("object_c_80300940"),
    0x803009E8: table.sym_fnc("L803009E8", flag=table.GLOBL|table.LOCAL),
    0x80300A38: table.sym_fnc("L80300A38", flag=table.GLOBL|table.LOCAL),
    0x80300A48: table.sym_fnc("L80300A48", flag=table.GLOBL|table.LOCAL),
    0x80300A58: table.sym_fnc("L80300A58", flag=table.GLOBL|table.LOCAL),
    0x80300A68: table.sym_fnc("L80300A68", flag=table.GLOBL|table.LOCAL),
    0x80300A78: table.sym_fnc("L80300A78", flag=table.GLOBL|table.LOCAL),
    0x80300DD4: table.sym("object_c_80300DD4"),
    0x80300E40: table.sym("object_c_80300E40", table.GLOBL), # o callback
    0x80300ECC: table.sym("object_c_80300ECC", table.GLOBL), # o callback
    0x80301148: table.sym("object_c_80301148", table.GLOBL), # o callback
    0x80301180: table.sym("object_c_80301180", table.GLOBL), # o callback
    0x80301210: table.sym("object_c_80301210", table.GLOBL), # o callback
    0x803014CC: table.sym("object_c_803014CC"),
    0x803016E0: table.sym("object_c_803016E0"),
    0x80301940: table.sym("object_c_80301940"),
    0x80301C88: table.sym("object_c_80301C88"),
    0x80301E84: table.sym("object_c_80301E84"),
    0x80301F70: table.sym("object_c_80301F70"),
    0x80302024: table.sym("object_c_80302024"),
    0x803020E4: table.sym("object_c_803020E4"),
    0x80302154: table.sym("object_c_80302154", table.GLOBL), # o callback
    0x80302278: table.sym_fnc("L80302278", flag=table.GLOBL|table.LOCAL),
    0x80302288: table.sym_fnc("L80302288", flag=table.GLOBL|table.LOCAL),
    0x80302298: table.sym_fnc("L80302298", flag=table.GLOBL|table.LOCAL),
    0x803022A8: table.sym_fnc("L803022A8", flag=table.GLOBL|table.LOCAL),
    0x803022B8: table.sym_fnc("L803022B8", flag=table.GLOBL|table.LOCAL),
    0x80302358: table.sym("object_c_80302358"),
    0x803023E4: table.sym("object_c_803023E4"),
    0x8030267C: table.sym("object_c_8030267C"),
    0x803027AC: table.sym("object_c_803027AC"),
    0x80302910: table.sym("object_c_80302910", table.GLOBL), # o callback
    0x803029B8: table.sym("object_c_803029B8"),
    0x80302A54: table.sym("object_c_80302A54"),
    0x80302B20: table.sym("object_c_80302B20"),
    0x80302C84: table.sym("object_c_80302C84"),
    0x80302DB0: table.sym("object_c_80302DB0"),
    0x80302E84: table.sym("object_c_80302E84"),
    0x80302F04: table.sym("object_c_80302F04"),
    0x80303028: table.sym("object_c_80303028", table.GLOBL), # o callback
    0x803030A8: table.sym("object_c_803030A8"),
    0x803031B4: table.sym("object_c_803031B4"),
    0x8030320C: table.sym("object_c_8030320C"),
    0x80303498: table.sym("object_c_80303498"),
    0x80303634: table.sym("object_c_80303634"),
    0x8030369C: table.sym("object_c_8030369C", table.GLOBL), # o callback
    0x80303744: table.sym("object_c_80303744", table.GLOBL), # o callback
    0x80303984: table.sym("object_c_80303984", table.GLOBL), # o callback
    0x80303A20: table.sym("object_c_80303A20"),
    0x80303B08: table.sym("object_c_80303B08"),
    0x80303C14: table.sym("object_c_80303C14"),
    0x80303F64: table.sym("object_c_80303F64", table.GLOBL), # o callback
    0x803041A0: table.sym("object_c_803041A0"),
    0x80304274: table.sym("object_c_80304274"),
    0x803043F8: table.sym("object_c_803043F8", table.GLOBL), # o callback
    0x80304474: table.sym("object_c_80304474"),
    0x803044C0: table.sym("object_c_803044C0", table.GLOBL), # o callback
    0x803044DC: table.sym("object_c_803044DC"),
    0x80304710: table.sym("object_c_80304710"),
    0x803047AC: table.sym("object_c_803047AC"),
    0x80304864: table.sym("object_c_80304864"),
    0x803048EC: table.sym("object_c_803048EC"),
    0x80304958: table.sym("object_c_80304958"),
    0x80304A14: table.sym("object_c_80304A14"),
    0x80304A70: table.sym("object_c_80304A70"),
    0x80304AE0: table.sym("object_c_80304AE0"),
    0x80304BA8: table.sym("object_c_80304BA8", table.GLOBL), # o callback
    0x80304C14: table.sym_fnc("L80304C14", flag=table.GLOBL|table.LOCAL),
    0x80304C24: table.sym_fnc("L80304C24", flag=table.GLOBL|table.LOCAL),
    0x80304C34: table.sym_fnc("L80304C34", flag=table.GLOBL|table.LOCAL),
    0x80304C44: table.sym_fnc("L80304C44", flag=table.GLOBL|table.LOCAL),
    0x80304C54: table.sym_fnc("L80304C54", flag=table.GLOBL|table.LOCAL),
    0x80304C64: table.sym_fnc("L80304C64", flag=table.GLOBL|table.LOCAL),
    0x80304C74: table.sym_fnc("L80304C74", flag=table.GLOBL|table.LOCAL),
    0x80304C84: table.sym_fnc("L80304C84", flag=table.GLOBL|table.LOCAL),
    0x80304E28: table.sym("object_c_80304E28"),
    0x80304F74: table.sym("object_c_80304F74"),
    0x80304FD4: table.sym("object_c_80304FD4", table.GLOBL), # o callback
    0x8030505C: table.sym("object_c_8030505C"),
    0x8030508C: table.sym("object_c_8030508C"),
    0x80305100: table.sym("object_c_80305100", table.GLOBL), # o callback
    0x8030522C: table.sym("object_c_8030522C"),
    0x803053DC: table.sym("object_c_803053DC"),
    0x80305474: table.sym("object_c_80305474"),
    0x8030586C: table.sym("object_c_8030586C"),
    0x803058A4: table.sym("object_c_803058A4"),
    0x80305904: table.sym("object_c_80305904"),
    0x80305A58: table.sym("object_c_80305A58", table.GLOBL), # o callback
    0x80305A90: table.sym_fnc("L80305A90", flag=table.GLOBL|table.LOCAL),
    0x80305AA0: table.sym_fnc("L80305AA0", flag=table.GLOBL|table.LOCAL),
    0x80305AB0: table.sym_fnc("L80305AB0", flag=table.GLOBL|table.LOCAL),
    0x80305AC0: table.sym_fnc("L80305AC0", flag=table.GLOBL|table.LOCAL),
    0x80305AD0: table.sym_fnc("L80305AD0", flag=table.GLOBL|table.LOCAL),
    0x80305BB0: table.sym("object_c_80305BB0", table.GLOBL), # o callback
    0x80305C14: table.sym("object_c_80305C14", table.GLOBL), # o callback
    0x80305C90: table.sym("object_c_80305C90", table.GLOBL), # o callback
    0x80305E2C: table.sym("object_c_80305E2C", table.GLOBL), # o callback
    0x80305F24: table.sym("object_c_80305F24", table.GLOBL), # o callback
    0x80306084: table.sym("object_c_80306084", table.GLOBL), # o callback
    0x803062A8: table.sym("object_c_803062A8"),
    0x80306304: table.sym("object_c_80306304"),
    0x80306364: table.sym("object_c_80306364"),
    0x8030668C: table.sym("object_c_8030668C"),
    0x803066D8: table.sym("object_c_803066D8"),
    0x803067E8: table.sym("object_c_803067E8", table.GLOBL), # o callback
    0x803068C0: table.sym("object_c_803068C0", table.GLOBL), # o callback
    0x8030699C: table.sym("object_c_8030699C", table.GLOBL), # o callback
    0x80306A38: table.sym("object_c_80306A38", table.GLOBL), # o callback
    0x80306CC4: table.sym("object_c_80306CC4", table.GLOBL), # o callback
    0x80306D38: table.sym("object_c_80306D38", table.GLOBL), # o callback
    0x80306F48: table.sym("object_c_80306F48", table.GLOBL), # o callback
    0x80307010: table.sym("object_c_80307010", table.GLOBL), # o callback
    0x803071B8: table.sym("object_c_803071B8", table.GLOBL), # o callback
    0x80307240: table.sym("object_c_80307240"),
    0x80307348: table.sym("object_c_80307348"),
    0x803073F8: table.sym("object_c_803073F8"),
    0x80307434: table.sym("object_c_80307434"),
    0x803075F8: table.sym("object_c_803075F8"),
    0x80307670: table.sym("object_c_80307670", table.GLOBL), # o callback
    0x80307760: table.sym("object_c_80307760", table.GLOBL), # o callback
    0x803077E0: table.sym("object_c_803077E0", table.GLOBL), # o callback
    0x80307930: table.sym("object_c_80307930", table.GLOBL), # o callback
    0x803079C8: table.sym("object_c_803079C8", table.GLOBL), # o callback
    0x80307AE4: table.sym("object_c_80307AE4", table.GLOBL), # o callback
    0x80307B58: table.sym("object_c_80307B58", table.GLOBL), # o callback
    0x80307C88: table.sym("object_c_80307C88", table.GLOBL), # o callback
    0x80307CF8: table.sym("object_c_80307CF8", table.GLOBL), # o callback
    0x80307EA4: table.sym("object_c_80307EA4", table.GLOBL), # o callback
    0x80307FB8: table.sym("object_c_80307FB8"),
    0x8030803C: table.sym("object_c_8030803C", table.GLOBL), # o callback
    0x80308110: table.sym("object_c_80308110"),
    0x80308228: table.sym("object_c_80308228"),
    0x803082EC: table.sym("object_c_803082EC"),
    0x80308454: table.sym("object_c_80308454"),
    0x80308734: table.sym("object_c_80308734"),
    0x80308A74: table.sym("object_c_80308A74"),
    0x80308AF0: table.sym("object_c_80308AF0"),
    0x80308BB8: table.sym("object_c_80308BB8"),
    0x80308D6C: table.sym("object_c_80308D6C", table.GLOBL), # o callback
    0x80308DB0: table.sym_fnc("L80308DB0", flag=table.GLOBL|table.LOCAL),
    0x80308DC0: table.sym_fnc("L80308DC0", flag=table.GLOBL|table.LOCAL),
    0x80308DD0: table.sym_fnc("L80308DD0", flag=table.GLOBL|table.LOCAL),
    0x80308DE0: table.sym_fnc("L80308DE0", flag=table.GLOBL|table.LOCAL),
    0x80308DF0: table.sym_fnc("L80308DF0", flag=table.GLOBL|table.LOCAL),
    0x80308E00: table.sym_fnc("L80308E00", flag=table.GLOBL|table.LOCAL),
    0x80308E10: table.sym_fnc("L80308E10", flag=table.GLOBL|table.LOCAL),
    0x80308E20: table.sym_fnc("L80308E20", flag=table.GLOBL|table.LOCAL),
    0x80308F08: table.sym("object_c_80308F08"),
    0x80308F94: table.sym("object_c_80308F94"),
    0x803090B8: table.sym("object_c_803090B8"),
    0x80309154: table.sym("object_c_80309154", table.GLOBL), # o callback
    0x803091E0: table.sym("object_c_803091E0", table.GLOBL), # o callback
    0x80309354: table.sym("object_c_80309354", table.GLOBL), # o callback
    0x80309454: table.sym("object_c_80309454", table.GLOBL), # o callback
    0x803094D0: table.sym("object_c_803094D0", table.GLOBL), # o callback
    0x803094F8: table.sym("object_c_803094F8", table.GLOBL), # o callback
    0x80309530: table.sym("object_c_80309530", table.GLOBL), # o callback
    0x803097A4: table.sym("object_c_803097A4", table.GLOBL), # o callback
    0x803098C0: table.sym("object_c_803098C0", table.GLOBL), # o callback
    0x80309B64: table.sym("object_c_80309B64", table.GLOBL), # o callback
    0x80309CEC: table.sym("object_c_80309CEC", table.GLOBL), # o callback
    0x80309ED4: table.sym("object_c_80309ED4"),
    0x80309F68: table.sym("object_c_80309F68"),
    0x8030A0E8: table.sym("object_c_8030A0E8"),
    0x8030A11C: table.sym("object_c_8030A11C", table.GLOBL), # o callback
    0x8030A1C0: table.sym("object_c_8030A1C0", table.GLOBL), # o callback
    0x8030A2A8: table.sym("object_c_8030A2A8"),
    0x8030A390: table.sym("object_c_8030A390"),
    0x8030A514: table.sym("object_c_8030A514"),
    0x8030A614: table.sym("object_c_8030A614"),
    0x8030A93C: table.sym("object_c_8030A93C", table.GLOBL), # o callback
    0x8030AA54: table.sym_fnc("L8030AA54", flag=table.GLOBL|table.LOCAL),
    0x8030AA64: table.sym_fnc("L8030AA64", flag=table.GLOBL|table.LOCAL),
    0x8030AA7C: table.sym_fnc("L8030AA7C", flag=table.GLOBL|table.LOCAL),
    0x8030AA84: table.sym_fnc("L8030AA84", flag=table.GLOBL|table.LOCAL),
    0x8030AA94: table.sym_fnc("L8030AA94", flag=table.GLOBL|table.LOCAL),
    0x8030AABC: table.sym("object_c_8030AABC", table.GLOBL), # o callback
    0x8030AD04: table.sym("object_c_8030AD04"),
    0x8030AE9C: table.sym("object_c_8030AE9C"),
    0x8030B0B8: table.sym("object_c_8030B0B8"),
    0x8030B0F0: table.sym("object_c_8030B0F0"),
    0x8030B220: table.sym("object_c_8030B220"),
    0x8030B2F4: table.sym("object_c_8030B2F4", table.GLOBL), # o callback
    0x8030B658: table.sym("object_c_8030B658", table.GLOBL), # o callback
    0x8030B6D8: table.sym("object_c_8030B6D8"),
    0x8030BA68: table.sym("object_c_8030BA68"),
    0x8030BC90: table.sym("object_c_8030BC90", table.GLOBL), # o callback
    0x8030BD2C: table.sym("object_c_8030BD2C"),
    0x8030BDF8: table.sym("object_c_8030BDF8"),
    0x8030BFD0: table.sym("object_c_8030BFD0", table.GLOBL), # o callback
    0x8030C06C: table.sym("object_c_8030C06C"),
    0x8030C0F0: table.sym("object_c_8030C0F0"),
    0x8030C210: table.sym("object_c_8030C210"),
    0x8030C2C8: table.sym("object_c_8030C2C8"),
    0x8030C364: table.sym("object_c_8030C364", table.GLOBL), # o callback
    0x8030C4B0: table.sym("object_c_8030C4B0", table.GLOBL), # o callback
    0x8030C564: table.sym("object_c_8030C564"),
    0x8030C60C: table.sym("object_c_8030C60C"),
    0x8030C6A4: table.sym("object_c_8030C6A4"),
    0x8030C828: table.sym("object_c_8030C828"),
    0x8030C894: table.sym("object_c_8030C894"),
    0x8030C8EC: table.sym("object_c_8030C8EC", table.GLOBL), # o callback
    0x8030C924: table.sym_fnc("L8030C924", flag=table.GLOBL|table.LOCAL),
    0x8030C934: table.sym_fnc("L8030C934", flag=table.GLOBL|table.LOCAL),
    0x8030C944: table.sym_fnc("L8030C944", flag=table.GLOBL|table.LOCAL),
    0x8030C954: table.sym_fnc("L8030C954", flag=table.GLOBL|table.LOCAL),
    0x8030C964: table.sym_fnc("L8030C964", flag=table.GLOBL|table.LOCAL),
    0x8030C98C: table.sym("object_c_8030C98C", table.GLOBL), # o callback
    0x8030CD30: table.sym("object_c_8030CD30", table.GLOBL),
    0x8030CDDC: table.sym("object_c_8030CDDC", table.GLOBL), # o callback
    0x8030CEC0: table.sym("object_c_8030CEC0"),
    0x8030D140: table.sym("object_c_8030D140"),
    0x8030D2F0: table.sym("object_c_8030D2F0", table.GLOBL), # o callback
    0x8030D42C: table.sym("object_c_8030D42C"),
    0x8030D4D4: table.sym("object_c_8030D4D4"),
    0x8030D598: table.sym("object_c_8030D598", table.GLOBL), # o callback
    0x8030D640: table.sym("object_c_8030D640", table.GLOBL), # o callback
    0x8030D8D4: table.sym("object_c_8030D8D4", table.GLOBL), # o callback
    0x8030D93C: table.sym("s_object_c_8030D93C", table.GLOBL), # s callback
    0x8030D9AC: table.sym("s_object_c_8030D9AC", table.GLOBL), # s callback
    0x8030DA14: table.sym("object_c_8030DA14"),
    0x8030DB38: table.sym("object_c_8030DB38"),
    0x8030DC70: table.sym("object_c_8030DC70", table.GLOBL), # o callback
    0x8030DFC4: table.sym("object_c_8030DFC4", table.GLOBL), # o callback
    0x8030E14C: table.sym("object_c_8030E14C", table.GLOBL), # o callback
    0x8030E16C: table.sym("object_c_8030E16C", table.GLOBL), # o callback
    0x8030E384: table.sym("object_c_8030E384"),
    0x8030E3E0: table.sym("object_c_8030E3E0"),
    0x8030E488: table.sym("object_c_8030E488"),
    0x8030E52C: table.sym("object_c_8030E52C"),
    0x8030E688: table.sym("object_c_8030E688"),
    0x8030E6D4: table.sym("object_c_8030E6D4"),
    0x8030E9E0: table.sym("object_c_8030E9E0"),
    0x8030EA9C: table.sym("object_c_8030EA9C", table.GLOBL), # o callback
    0x8030EAD4: table.sym_fnc("L8030EAD4", flag=table.GLOBL|table.LOCAL),
    0x8030EAE4: table.sym_fnc("L8030EAE4", flag=table.GLOBL|table.LOCAL),
    0x8030EAF4: table.sym_fnc("L8030EAF4", flag=table.GLOBL|table.LOCAL),
    0x8030EB04: table.sym_fnc("L8030EB04", flag=table.GLOBL|table.LOCAL),
    0x8030EB14: table.sym_fnc("L8030EB14", flag=table.GLOBL|table.LOCAL),
    0x8030EB3C: table.sym("object_c_8030EB3C"),
    0x8030ECA8: table.sym("object_c_8030ECA8"),
    0x8030ECF8: table.sym("object_c_8030ECF8"),
    0x8030EF08: table.sym("object_c_8030EF08"),
    0x8030F118: table.sym("object_c_8030F118"),
    0x8030F21C: table.sym("object_c_8030F21C"),
    0x8030F440: table.sym("object_c_8030F440"),
    0x8030F508: table.sym("object_c_8030F508"),
    0x8030F58C: table.sym("object_c_8030F58C"),
    0x8030F5CC: table.sym("object_c_8030F5CC"),
    0x8030F628: table.sym("object_c_8030F628"),
    0x8030F6BC: table.sym("object_c_8030F6BC"),
    0x8030F840: table.sym("object_c_8030F840"),
    0x8030F9C0: table.sym("object_c_8030F9C0"),
    0x8030FB3C: table.sym("object_c_8030FB3C"),
    0x8030FC34: table.sym("object_c_8030FC34"),
    0x8030FCF4: table.sym("object_c_8030FCF4"),
    0x8030FE38: table.sym("object_c_8030FE38"),
    0x8030FFF8: table.sym("object_c_8030FFF8", table.GLOBL), # o callback
    0x80310078: table.sym_fnc("L80310078", flag=table.GLOBL|table.LOCAL),
    0x80310088: table.sym_fnc("L80310088", flag=table.GLOBL|table.LOCAL),
    0x80310098: table.sym_fnc("L80310098", flag=table.GLOBL|table.LOCAL),
    0x803100A8: table.sym_fnc("L803100A8", flag=table.GLOBL|table.LOCAL),
    0x803100B8: table.sym_fnc("L803100B8", flag=table.GLOBL|table.LOCAL),
    0x803100C8: table.sym_fnc("L803100C8", flag=table.GLOBL|table.LOCAL),
    0x803100D8: table.sym_fnc("L803100D8", flag=table.GLOBL|table.LOCAL),
    0x803100E8: table.sym_fnc("L803100E8", flag=table.GLOBL|table.LOCAL),
    0x803100F8: table.sym_fnc("L803100F8", flag=table.GLOBL|table.LOCAL),
    0x80310108: table.sym_fnc("L80310108", flag=table.GLOBL|table.LOCAL),
    0x80310118: table.sym_fnc("L80310118", flag=table.GLOBL|table.LOCAL),
    0x80310128: table.sym_fnc("L80310128", flag=table.GLOBL|table.LOCAL),
    0x80310138: table.sym_fnc("L80310138", flag=table.GLOBL|table.LOCAL),
    0x80310148: table.sym_fnc("L80310148", flag=table.GLOBL|table.LOCAL),
    0x80310158: table.sym_fnc("L80310158", flag=table.GLOBL|table.LOCAL),
    0x803101DC: table.sym("object_c_803101DC"),
    0x80310258: table.sym("object_c_80310258"),
    0x80310318: table.sym("object_c_80310318"),
    0x80310498: table.sym("object_c_80310498", table.GLOBL), # o callback
    0x8031054C: table.sym("object_c_8031054C"),
    0x80310774: table.sym("object_c_80310774"),
    0x8031097C: table.sym("object_c_8031097C"),
    0x80310A7C: table.sym("object_c_80310A7C"),
    0x80310B2C: table.sym("object_c_80310B2C"),
    0x80310C3C: table.sym("object_c_80310C3C"),
    0x80310F04: table.sym("object_c_80310F04"),
    0x80311018: table.sym("object_c_80311018"),
    0x8031111C: table.sym("object_c_8031111C"),
    0x8031126C: table.sym("object_c_8031126C"),
    0x8031129C: table.sym("object_c_8031129C", table.GLOBL), # o callback
    0x80311358: table.sym_fnc("L80311358", flag=table.GLOBL|table.LOCAL),
    0x80311378: table.sym_fnc("L80311378", flag=table.GLOBL|table.LOCAL),
    0x80311390: table.sym_fnc("L80311390", flag=table.GLOBL|table.LOCAL),
    0x803113A0: table.sym_fnc("L803113A0", flag=table.GLOBL|table.LOCAL),
    0x803113B0: table.sym_fnc("L803113B0", flag=table.GLOBL|table.LOCAL),
    0x803113C0: table.sym_fnc("L803113C0", flag=table.GLOBL|table.LOCAL),
    0x803113D0: table.sym_fnc("L803113D0", flag=table.GLOBL|table.LOCAL),
    0x803113E0: table.sym_fnc("L803113E0", flag=table.GLOBL|table.LOCAL),
    0x8031157C: table.sym("object_c_8031157C"),
    0x803116C0: table.sym("object_c_803116C0"),
    0x80311874: table.sym("object_c_80311874", table.GLOBL), # o callback
    0x803118E4: table.sym("object_c_803118E4", table.GLOBL), # o callback
    0x80311954: table.sym("object_c_80311954"),
    0x803119E4: table.sym("object_c_803119E4"),
    0x80311B18: table.sym("object_c_80311B18"),
    0x80311B7C: table.sym("object_c_80311B7C"),
    0x80311DD8: table.sym("object_c_80311DD8"),
    0x80311EA4: table.sym("object_c_80311EA4"),
    0x80312070: table.sym("object_c_80312070", table.GLOBL), # o callback
    0x803120B0: table.sym_fnc("L803120B0", flag=table.GLOBL|table.LOCAL),
    0x803120C0: table.sym_fnc("L803120C0", flag=table.GLOBL|table.LOCAL),
    0x803120D0: table.sym_fnc("L803120D0", flag=table.GLOBL|table.LOCAL),
    0x803120E0: table.sym_fnc("L803120E0", flag=table.GLOBL|table.LOCAL),
    0x803120F0: table.sym_fnc("L803120F0", flag=table.GLOBL|table.LOCAL),
    0x80312100: table.sym_fnc("L80312100", flag=table.GLOBL|table.LOCAL),
    0x80312168: table.sym("object_c_80312168", table.GLOBL), # o callback
    0x80312200: table.sym("object_c_80312200", table.GLOBL), # o callback
    0x80312248: table.sym("object_c_80312248", table.GLOBL), # o callback
    0x80312370: table.sym("object_c_80312370"),
    0x8031262C: table.sym("object_c_8031262C"),
    0x8031274C: table.sym("object_c_8031274C", table.GLOBL), # o callback
    0x80312804: table.sym("object_c_80312804"),
    0x80312900: table.sym("object_c_80312900"),
    0x80312A54: table.sym("object_c_80312A54", table.GLOBL), # o callback
    0x80312AF4: table.sym("object_c_80312AF4"),
    0x80312B80: table.sym("object_c_80312B80"),
    0x80312D0C: table.sym("object_c_80312D0C"),
    0x80312EA8: table.sym("object_c_80312EA8"),
    0x80313110: table.sym("object_c_80313110", table.GLOBL), # o callback
    0x803131E8: table.sym("object_c_803131E8", table.GLOBL), # o callback
    0x8031326C: table.sym("object_c_8031326C", table.GLOBL), # o callback
    0x80313294: table.sym("object_c_80313294", table.GLOBL), # o callback
    0x80313354: table.sym("object_c_80313354", table.GLOBL), # o callback
    0x80313530: table.sym("object_c_80313530", table.GLOBL), # o callback
    0x803136CC: table.sym("object_c_803136CC", table.GLOBL), # o callback
    0x80313754: table.sym("object_c_80313754", table.GLOBL), # o callback
    0x803137F4: table.sym("object_c_803137F4", table.GLOBL), # o callback
    0x8031381C: table.sym("object_c_8031381C"),
    0x803139F0: table.sym("object_c_803139F0"),
    0x80313BE4: table.sym("object_c_80313BE4"),
    0x80313E1C: table.sym("object_c_80313E1C"),
    0x80313FC0: table.sym("object_c_80313FC0", table.GLOBL), # o callback
    0x80314098: table.sym("object_c_80314098"),
    0x8031427C: table.sym("object_c_8031427C"),
    0x803145D4: table.sym("object_c_803145D4", table.GLOBL), # o callback

    # src/audio/a.c
    0x80314A30: table.sym("Na_a_80314A30"),
    0x80314CC0: table.sym("Na_a_80314CC0"),
    0x80314DE4: table.sym("Na_a_80314DE4", table.GLOBL),
    0x80314F64: table.sym("Na_a_80314F64"),
    0x80315590: table.sym("Na_a_80315590"),
    0x80316010: table.sym("Na_a_80316010"),
    0x803160DC: table.sym("Na_a_803160DC"),
    0x80316138: table.sym("Na_a_80316138"),
    0x8031619C: table.sym("Na_a_8031619C"),
    0x803166FC: table.sym("Na_a_803166FC"),
    0x80316AC8: table.sym("Na_a_80316AC8", table.GLOBL),
    0x80316AF4: table.sym("Na_a_80316AF4", table.GLOBL),
    0x80316DA8: table.sym("Na_a_80316DA8", table.GLOBL),
    0x80316DB4: table.sym("Na_a_80316DB4", table.GLOBL),
    0x80316E00: table.sym("Na_a_80316E00", table.GLOBL),

    # src/audio/b.c
    0x80316E80: table.sym("Na_b_80316E80"),
    0x80316EC4: table.sym("Na_b_80316EC4"),
    0x80316FB4: table.sym("Na_b_80316FB4"),
    0x80317040: table.sym("Na_b_80317040", table.GLOBL),
    0x803170B4: table.sym("Na_b_803170B4"),
    0x803170D4: table.sym("Na_b_803170D4"),
    0x803170E8: table.sym("Na_b_803170E8"),
    0x80317118: table.sym("Na_b_80317118"), # unused
    0x80317128: table.sym("Na_b_80317128", table.GLOBL),
    0x80317184: table.sym("Na_b_80317184"),
    0x80317200: table.sym("Na_b_80317200"),
    0x8031727C: table.sym("Na_b_8031727C"),
    0x80317338: table.sym("Na_b_80317338"),
    0x803173F4: table.sym("Na_b_803173F4"), # unused
    0x803173FC: table.sym("Na_b_803173FC", table.GLOBL),
    0x8031782C: table.sym("Na_b_8031782C", table.GLOBL),
    0x803178EC: table.sym("Na_b_803178EC"),
    0x80317914: table.sym("Na_b_80317914"),
    0x80317948: table.sym("Na_b_80317948", table.GLOBL),
    0x80317BF0: table.sym_fnc("L80317BF0", flag=table.GLOBL|table.LOCAL),
    0x80317BFC: table.sym_fnc("L80317BFC", flag=table.GLOBL|table.LOCAL),
    0x80317C0C: table.sym_fnc("L80317C0C", flag=table.GLOBL|table.LOCAL),
    0x80317C1C: table.sym_fnc("L80317C1C", flag=table.GLOBL|table.LOCAL),
    0x80317C2C: table.sym_fnc("L80317C2C", flag=table.GLOBL|table.LOCAL),
    0x80317C3C: table.sym_fnc("L80317C3C", flag=table.GLOBL|table.LOCAL),

    # src/audio/c.c
    0x80318040: table.sym("Na_c_80318040"),
    0x803180C4: table.sym("Na_c_803180C4"),
    0x80318130: table.sym("Na_c_80318130", table.GLOBL),
    0x803181EC: table.sym("Na_c_803181EC", table.GLOBL),
    0x80318300: table.sym("Na_c_80318300", table.GLOBL),
    0x80318634: table.sym("Na_c_80318634", table.GLOBL),
    0x803188EC: table.sym("Na_c_803188EC"), # unused
    0x803188F4: table.sym("Na_c_803188F4", table.GLOBL),
    0x80318B30: table.sym("Na_c_80318B30"),
    0x80318C8C: table.sym("Na_c_80318C8C"),
    0x80318DC4: table.sym("Na_c_80318DC4"),
    0x80318E70: table.sym("Na_c_80318E70"),
    0x80318FAC: table.sym("Na_c_80318FAC"),
    0x803190F4: table.sym("Na_c_803190F4"),
    0x80319220: table.sym("Na_c_80319220", table.GLOBL),
    0x80319328: table.sym("Na_c_80319328", table.GLOBL),
    0x80319388: table.sym("Na_c_80319388"),
    0x8031950C: table.sym_fnc("Na_load", flag=table.GLOBL), # ext

    # src/audio/d.c
    0x80319920: table.sym("Na_d_80319920"),
    0x80319998: table.sym("Na_d_80319998"),
    0x803199B8: table.sym("Na_d_803199B8", table.GLOBL),
    0x80319DB8: table.sym("Na_d_80319DB8"),
    0x80319F64: table.sym("Na_d_80319F64", table.GLOBL),
    0x80319F84: table.sym("Na_d_80319F84"),
    0x80319FA4: table.sym("Na_d_80319FA4"),
    0x8031A1D0: table.sym("Na_d_8031A1D0", table.GLOBL),
    0x8031A254: table.sym("Na_d_8031A254"),
    0x8031A264: table.sym("Na_d_8031A264", table.GLOBL),
    0x8031A2B4: table.sym("Na_d_8031A2B4", table.GLOBL),
    0x8031A368: table.sym("Na_d_8031A368", table.GLOBL),
    0x8031A494: table.sym("Na_d_8031A494", table.GLOBL),
    0x8031A5D0: table.sym("Na_d_8031A5D0"),
    0x8031A610: table.sym("Na_d_8031A610", table.GLOBL),
    0x8031A63C: table.sym("Na_d_8031A63C"),
    0x8031A6CC: table.sym("Na_d_8031A6CC"),
    0x8031A794: table.sym("Na_d_8031A794"),
    0x8031A7C8: table.sym("Na_d_8031A7C8"),
    0x8031A820: table.sym("Na_d_8031A820"),
    0x8031A89C: table.sym("Na_d_8031A89C"),
    0x8031A8F0: table.sym("Na_d_8031A8F0"),
    0x8031A94C: table.sym("Na_d_8031A94C", table.GLOBL),
    0x8031AC34: table.sym("Na_d_8031AC34", table.GLOBL),
    0x8031ADAC: table.sym("Na_d_8031ADAC", table.GLOBL),

    # src/audio/e.c
    0x8031AEE0: table.sym("Na_e_8031AEE0"), # unused
    0x8031AEE8: table.sym("Na_e_8031AEE8", table.GLOBL),
    0x8031B0CC: table.sym("Na_e_8031B0CC"),
    0x8031B1C0: table.sym("Na_e_8031B1C0"),
    0x8031B248: table.sym("Na_e_8031B248"),
    0x8031B440: table.sym("Na_e_8031B440", table.GLOBL),
    0x8031B4A0: table.sym("Na_e_8031B4A0", table.GLOBL),
    0x8031B58C: table.sym("Na_e_8031B58C", table.GLOBL),
    0x8031B5AC: table.sym("Na_e_8031B5AC", table.GLOBL),
    0x8031B5D8: table.sym_fnc("L8031B5D8", flag=table.GLOBL|table.LOCAL),
    0x8031B5E0: table.sym_fnc("L8031B5E0", flag=table.GLOBL|table.LOCAL),
    0x8031B604: table.sym_fnc("L8031B604", flag=table.GLOBL|table.LOCAL),
    0x8031B61C: table.sym_fnc("L8031B61C", flag=table.GLOBL|table.LOCAL),
    0x8031B700: table.sym_fnc("L8031B700", flag=table.GLOBL|table.LOCAL),
    0x8031B734: table.sym_fnc("L8031B734", flag=table.GLOBL|table.LOCAL),
    0x8031B73C: table.sym_fnc("L8031B73C", flag=table.GLOBL|table.LOCAL),
    0x8031B7BC: table.sym_fnc("L8031B7BC", flag=table.GLOBL|table.LOCAL),

    # src/audio/f.c
    0x8031B830: table.sym("Na_f_8031B830"),
    0x8031B940: table.sym("Na_f_8031B940"),
    0x8031BA30: table.sym("Na_f_8031BA30", table.GLOBL),
    0x8031BA6C: table.sym("Na_f_8031BA6C"),
    0x8031BAF0: table.sym("Na_f_8031BAF0", table.GLOBL),
    0x8031BB5C: table.sym("Na_f_8031BB5C"),
    0x8031BBA4: table.sym("Na_f_8031BBA4"),
    0x8031BCD0: table.sym("Na_f_8031BCD0"),
    0x8031BDA0: table.sym("Na_f_8031BDA0"),
    0x8031BE44: table.sym("Na_f_8031BE44", table.GLOBL),
    0x8031BF14: table.sym("Na_f_8031BF14", table.GLOBL),
    0x8031BF54: table.sym("Na_f_8031BF54", table.GLOBL),
    0x8031BF94: table.sym("Na_f_8031BF94"),
    0x8031C03C: table.sym("Na_f_8031C03C"),
    0x8031C050: table.sym("Na_f_8031C050"),
    0x8031C080: table.sym("Na_f_8031C080"),
    0x8031C0C4: table.sym("Na_f_8031C0C4"),
    0x8031C200: table.sym_fnc("L8031C200", flag=table.GLOBL|table.LOCAL),
    0x8031C23C: table.sym_fnc("L8031C23C", flag=table.GLOBL|table.LOCAL),
    0x8031C298: table.sym_fnc("L8031C298", flag=table.GLOBL|table.LOCAL),
    0x8031C2DC: table.sym_fnc("L8031C2DC", flag=table.GLOBL|table.LOCAL),
    0x8031C328: table.sym_fnc("L8031C328", flag=table.GLOBL|table.LOCAL),
    0x8031C36C: table.sym_fnc("L8031C36C", flag=table.GLOBL|table.LOCAL),
    0x8031C3BC: table.sym_fnc("L8031C3BC", flag=table.GLOBL|table.LOCAL),
    0x8031C3E8: table.sym_fnc("L8031C3E8", flag=table.GLOBL|table.LOCAL),
    0x8031C454: table.sym_fnc("L8031C454", flag=table.GLOBL|table.LOCAL),
    0x8031C4A4: table.sym_fnc("L8031C4A4", flag=table.GLOBL|table.LOCAL),
    0x8031C5C8: table.sym_fnc("L8031C5C8", flag=table.GLOBL|table.LOCAL),
    0x8031C698: table.sym_fnc("L8031C698", flag=table.GLOBL|table.LOCAL),
    0x8031C6A0: table.sym_fnc("L8031C6A0", flag=table.GLOBL|table.LOCAL),
    0x8031CBE0: table.sym_fnc("L8031CBE0", flag=table.GLOBL|table.LOCAL),
    0x8031CBEC: table.sym_fnc("L8031CBEC", flag=table.GLOBL|table.LOCAL),
    0x8031CE54: table.sym("Na_f_8031CE54"),
    0x8031CFD4: table.sym("Na_f_8031CFD4"),
    0x8031D068: table.sym("Na_f_8031D068"),
    0x8031D08C: table.sym("Na_f_8031D08C"),
    0x8031D144: table.sym_fnc("L8031D144", flag=table.GLOBL|table.LOCAL),
    0x8031D1F8: table.sym_fnc("L8031D1F8", flag=table.GLOBL|table.LOCAL),
    0x8031D234: table.sym_fnc("L8031D234", flag=table.GLOBL|table.LOCAL),
    0x8031D26C: table.sym_fnc("L8031D26C", flag=table.GLOBL|table.LOCAL),
    0x8031D2B4: table.sym_fnc("L8031D2B4", flag=table.GLOBL|table.LOCAL),
    0x8031D2C4: table.sym_fnc("L8031D2C4", flag=table.GLOBL|table.LOCAL),
    0x8031D31C: table.sym_fnc("L8031D31C", flag=table.GLOBL|table.LOCAL),
    0x8031D344: table.sym_fnc("L8031D344", flag=table.GLOBL|table.LOCAL),
    0x8031D354: table.sym_fnc("L8031D354", flag=table.GLOBL|table.LOCAL),
    0x8031D370: table.sym_fnc("L8031D370", flag=table.GLOBL|table.LOCAL),
    0x8031D3A8: table.sym_fnc("L8031D3A8", flag=table.GLOBL|table.LOCAL),
    0x8031D3C4: table.sym_fnc("L8031D3C4", flag=table.GLOBL|table.LOCAL),
    0x8031D3D4: table.sym_fnc("L8031D3D4", flag=table.GLOBL|table.LOCAL),
    0x8031D3E4: table.sym_fnc("L8031D3E4", flag=table.GLOBL|table.LOCAL),
    0x8031D400: table.sym_fnc("L8031D400", flag=table.GLOBL|table.LOCAL),
    0x8031D424: table.sym_fnc("L8031D424", flag=table.GLOBL|table.LOCAL),
    0x8031D44C: table.sym_fnc("L8031D44C", flag=table.GLOBL|table.LOCAL),
    0x8031D474: table.sym_fnc("L8031D474", flag=table.GLOBL|table.LOCAL),
    0x8031D498: table.sym_fnc("L8031D498", flag=table.GLOBL|table.LOCAL),
    0x8031D4BC: table.sym_fnc("L8031D4BC", flag=table.GLOBL|table.LOCAL),
    0x8031D4D4: table.sym_fnc("L8031D4D4", flag=table.GLOBL|table.LOCAL),
    0x8031D4F0: table.sym_fnc("L8031D4F0", flag=table.GLOBL|table.LOCAL),
    0x8031D500: table.sym_fnc("L8031D500", flag=table.GLOBL|table.LOCAL),
    0x8031D51C: table.sym_fnc("L8031D51C", flag=table.GLOBL|table.LOCAL),
    0x8031D538: table.sym_fnc("L8031D538", flag=table.GLOBL|table.LOCAL),
    0x8031D56C: table.sym_fnc("L8031D56C", flag=table.GLOBL|table.LOCAL),
    0x8031D5A0: table.sym_fnc("L8031D5A0", flag=table.GLOBL|table.LOCAL),
    0x8031D5B4: table.sym_fnc("L8031D5B4", flag=table.GLOBL|table.LOCAL),
    0x8031D5D4: table.sym_fnc("L8031D5D4", flag=table.GLOBL|table.LOCAL),
    0x8031D5E4: table.sym_fnc("L8031D5E4", flag=table.GLOBL|table.LOCAL),
    0x8031D640: table.sym_fnc("L8031D640", flag=table.GLOBL|table.LOCAL),
    0x8031D678: table.sym_fnc("L8031D678", flag=table.GLOBL|table.LOCAL),
    0x8031D6C4: table.sym_fnc("L8031D6C4", flag=table.GLOBL|table.LOCAL),
    0x8031D6D4: table.sym_fnc("L8031D6D4", flag=table.GLOBL|table.LOCAL),
    0x8031D6F4: table.sym_fnc("L8031D6F4", flag=table.GLOBL|table.LOCAL),
    0x8031D718: table.sym_fnc("L8031D718", flag=table.GLOBL|table.LOCAL),
    0x8031D728: table.sym_fnc("L8031D728", flag=table.GLOBL|table.LOCAL),
    0x8031D73C: table.sym_fnc("L8031D73C", flag=table.GLOBL|table.LOCAL),
    0x8031D7B8: table.sym_fnc("L8031D7B8", flag=table.GLOBL|table.LOCAL),
    0x8031D7E8: table.sym_fnc("L8031D7E8", flag=table.GLOBL|table.LOCAL),
    0x8031D7F8: table.sym_fnc("L8031D7F8", flag=table.GLOBL|table.LOCAL),
    0x8031D814: table.sym_fnc("L8031D814", flag=table.GLOBL|table.LOCAL),
    0x8031D830: table.sym_fnc("L8031D830", flag=table.GLOBL|table.LOCAL),
    0x8031D87C: table.sym_fnc("L8031D87C", flag=table.GLOBL|table.LOCAL),
    0x8031D898: table.sym_fnc("L8031D898", flag=table.GLOBL|table.LOCAL),
    0x8031D8F8: table.sym_fnc("L8031D8F8", flag=table.GLOBL|table.LOCAL),
    0x8031D900: table.sym_fnc("L8031D900", flag=table.GLOBL|table.LOCAL),
    0x8031D930: table.sym_fnc("L8031D930", flag=table.GLOBL|table.LOCAL),
    0x8031D94C: table.sym_fnc("L8031D94C", flag=table.GLOBL|table.LOCAL),
    0x8031D974: table.sym_fnc("L8031D974", flag=table.GLOBL|table.LOCAL),
    0x8031D9EC: table.sym("Na_f_8031D9EC"),
    0x8031DC6C: table.sym_fnc("L8031DC6C", flag=table.GLOBL|table.LOCAL),
    0x8031DD14: table.sym_fnc("L8031DD14", flag=table.GLOBL|table.LOCAL),
    0x8031DD50: table.sym_fnc("L8031DD50", flag=table.GLOBL|table.LOCAL),
    0x8031DD88: table.sym_fnc("L8031DD88", flag=table.GLOBL|table.LOCAL),
    0x8031DDD0: table.sym_fnc("L8031DDD0", flag=table.GLOBL|table.LOCAL),
    0x8031DE30: table.sym_fnc("L8031DE30", flag=table.GLOBL|table.LOCAL),
    0x8031DE58: table.sym_fnc("L8031DE58", flag=table.GLOBL|table.LOCAL),
    0x8031DE68: table.sym_fnc("L8031DE68", flag=table.GLOBL|table.LOCAL),
    0x8031DE6C: table.sym_fnc("L8031DE6C", flag=table.GLOBL|table.LOCAL),
    0x8031DE8C: table.sym_fnc("L8031DE8C", flag=table.GLOBL|table.LOCAL),
    0x8031DF14: table.sym_fnc("L8031DF14", flag=table.GLOBL|table.LOCAL),
    0x8031DFB0: table.sym_fnc("L8031DFB0", flag=table.GLOBL|table.LOCAL),
    0x8031DFDC: table.sym_fnc("L8031DFDC", flag=table.GLOBL|table.LOCAL),
    0x8031DFF8: table.sym_fnc("L8031DFF8", flag=table.GLOBL|table.LOCAL),
    0x8031E014: table.sym_fnc("L8031E014", flag=table.GLOBL|table.LOCAL),
    0x8031E03C: table.sym_fnc("L8031E03C", flag=table.GLOBL|table.LOCAL),
    0x8031E04C: table.sym_fnc("L8031E04C", flag=table.GLOBL|table.LOCAL),
    0x8031E05C: table.sym_fnc("L8031E05C", flag=table.GLOBL|table.LOCAL),
    0x8031E090: table.sym_fnc("L8031E090", flag=table.GLOBL|table.LOCAL),
    0x8031E0A0: table.sym_fnc("L8031E0A0", flag=table.GLOBL|table.LOCAL),
    0x8031E0B0: table.sym_fnc("L8031E0B0", flag=table.GLOBL|table.LOCAL),
    0x8031E0C0: table.sym_fnc("L8031E0C0", flag=table.GLOBL|table.LOCAL),
    0x8031E194: table.sym_fnc("L8031E194", flag=table.GLOBL|table.LOCAL),
    0x8031E1A0: table.sym_fnc("L8031E1A0", flag=table.GLOBL|table.LOCAL),
    0x8031E1A8: table.sym_fnc("L8031E1A8", flag=table.GLOBL|table.LOCAL),
    0x8031E1B0: table.sym_fnc("L8031E1B0", flag=table.GLOBL|table.LOCAL),
    0x8031E240: table.sym("Na_f_8031E240", table.GLOBL),
    0x8031E2E8: table.sym("Na_f_8031E2E8", table.GLOBL),
    0x8031E374: table.sym("Na_f_8031E374", table.GLOBL),

    # src/audio/g.c
    0x8031E4F0: table.sym_fnc("Na_g_8031E4F0"), # unused
    0x8031E568: table.sym_fnc("Na_g_8031E568"), # unused
    0x8031E578: table.sym_fnc("Na_g_8031E578", arg=(
        "int",
        "int", #
    )),
    0x8031E5C0: table.sym_fnc("Na_g_8031E5C0", arg=(
        "int",
        "int", #
    )),
    0x8031E60C: table.sym_fnc("Na_g_8031E60C", arg=(
        "int",
        "int", #
        "u8",
    )),
    0x8031E6A4: table.sym_fnc("Na_g_8031E6A4", arg=(
        "int",
        "int", #
    )),
    0x8031E710: table.sym_fnc("Na_g_8031E710", arg=(
        "int",
        "int", #
        "u8",
    )),
    0x8031E7B8: table.sym_fnc("Na_main", "SC_TASK *",
    flag=table.GLOBL), # ext
    0x8031EB00: table.sym_fnc("Na_SE_play", arg=(
        "NA_SE se",
        "f32 *pos",
    ), flag=table.GLOBL), # ext
    0x8031EB30: table.sym_fnc("Na_g_8031EB30", arg=(
        "NA_SE",
        "f32 *",
    )),
    0x8031EDEC: table.sym_fnc("Na_g_8031EDEC"),
    0x8031EE70: table.sym_fnc("Na_g_8031EE70", arg=(
        "u8",
        "u8",
    )),
    0x8031EF6C: table.sym_fnc("Na_g_8031EF6C", arg=(
        "u8",
        "u8",
    )),
    0x8031EFF4: table.sym_fnc("Na_g_8031EFF4", arg=(
        "u8",
    )),
    0x8031F810: table.sym_fnc("Na_g_8031F810", "float", (
        "float",
        "float",
    )),
    0x8031F96C: table.sym_fnc("Na_g_8031F96C", "float", (
        "u8",
        "u8",
        "float",
    )),
    0x8031FB20: table.sym_fnc("Na_g_8031FB20", "float", (
        "u8",
        "u8",
    )),
    0x8031FBE8: table.sym_fnc("Na_g_8031FBE8", "u8", (
        "u8",
        "u8",
        "u8",
    )),
    0x8031FD7C: table.sym_fnc("Na_g_8031FD7C"),
    0x8031FD84: table.sym_fnc("Na_update", flag=table.GLOBL), # ext
    0x8031FDAC: table.sym_fnc("Na_g_8031FDAC"),
    0x8031FF5C: table.sym_fnc("L8031FF5C", flag=table.GLOBL|table.LOCAL),
    0x803200B0: table.sym_fnc("L803200B0", flag=table.GLOBL|table.LOCAL),
    0x803200D4: table.sym_fnc("L803200D4", flag=table.GLOBL|table.LOCAL),
    0x80320138: table.sym_fnc("L80320138", flag=table.GLOBL|table.LOCAL),
    0x8032026C: table.sym_fnc("L8032026C", flag=table.GLOBL|table.LOCAL),
    0x803203BC: table.sym_fnc("L803203BC", flag=table.GLOBL|table.LOCAL),
    0x803203DC: table.sym_fnc("L803203DC", flag=table.GLOBL|table.LOCAL),
    0x80320440: table.sym_fnc("L80320440", flag=table.GLOBL|table.LOCAL),
    0x80320544: table.sym_fnc("Na_g_80320544", arg=(
        "u8",
        "u8",
        "u16",
    )),
    0x80320678: table.sym_fnc("Na_SEQ_fadeout", arg=(
        "u8",
        "u16",
    ), flag=table.GLOBL), # ext
    0x803206BC: table.sym_fnc("Na_g_803206BC", arg=(
        "u8",
        "u8",
        "u16",
    ), flag=table.GLOBL), # ext
    0x80320734: table.sym_fnc("Na_g_80320734", arg=(
        "u8",
        "u8",
        "u8",
        "u16",
    )),
    0x8032080C: table.sym_fnc("Na_g_8032080C", arg=(
        "u8",
    )),
    0x803208EC: table.sym_fnc("Na_g_803208EC"),
    0x80320A4C: table.sym_fnc("L80320A4C", flag=table.GLOBL|table.LOCAL),
    0x80320A8C: table.sym_fnc("L80320A8C", flag=table.GLOBL|table.LOCAL),
    0x80320ACC: table.sym_fnc("L80320ACC", flag=table.GLOBL|table.LOCAL),
    0x80320B0C: table.sym_fnc("L80320B0C", flag=table.GLOBL|table.LOCAL),
    0x80320B4C: table.sym_fnc("L80320B4C", flag=table.GLOBL|table.LOCAL),
    0x80320B8C: table.sym_fnc("L80320B8C", flag=table.GLOBL|table.LOCAL),
    0x80320BCC: table.sym_fnc("L80320BCC", flag=table.GLOBL|table.LOCAL),
    0x80320BF4: table.sym_fnc("L80320BF4", flag=table.GLOBL|table.LOCAL),
    0x80320D70: table.sym_fnc("Na_g_80320D70", arg=(
        "u8",
        "u32",
        "s8",
    )), # unused
    0x80320E3C: table.sym_fnc("Na_SEQ_mute", arg=(
        "u8",
        "u16",
        "u8",
    ), flag=table.GLOBL), # ext
    0x80320EC4: table.sym_fnc("Na_SEQ_unmute", arg=(
        "u8",
        "u16",
    ), flag=table.GLOBL), # ext
    0x80320F68: table.sym_fnc("Na_g_80320F68", "u8", (
        "u16",
    )),
    0x803210D4: table.sym_fnc("Na_pause", arg=(
        "u8",
    ), flag=table.GLOBL), # ext
    0x8032112C: table.sym_fnc("Na_init", flag=table.GLOBL), # ext
    0x80321398: table.sym_fnc("Na_g_80321398", arg=(
        "u8",
        "u8 *",
        "u8 *",
        "u8 *",
    )), # unused
    0x80321474: table.sym_fnc("Na_g_80321474", arg=(
        "u32",
        "f32 *",
    ), flag=table.GLOBL), # ext
    0x80321584: table.sym_fnc("Na_g_80321584", arg=(
        "f32 *",
    ), flag=table.GLOBL), # ext
    0x80321668: table.sym_fnc("Na_g_80321668", arg=(
        "u8",
    )),
    0x8032171C: table.sym_fnc("Na_SE_clear", flag=table.GLOBL), # ext
    0x8032174C: table.sym_fnc("Na_IO_lock", arg=(
        "u8",
        "u16",
    ), flag=table.GLOBL), # ext
    0x803217A8: table.sym_fnc("Na_g_803217A8"),
    0x8032180C: table.sym_fnc("Na_IO_unlock", arg=(
        "u8",
        "u16",
    ), flag=table.GLOBL), # ext
    0x80321864: table.sym_fnc("Na_g_80321864", "u8", (
        "u8",
        "u8",
        "u8",
    )), # unused
    0x803218D8: table.sym_fnc("Na_g_803218D8", arg=(
        "u8",
        "u8",
    ), flag=table.GLOBL), # ext
    0x803218F4: table.sym_fnc("Na_g_803218F4", arg=(
        "u8",
    ), flag=table.GLOBL), # ext
    0x803219AC: table.sym_fnc("Na_BGM_play", arg=(
        "u8",
        "u16",
        "u16",
    ), flag=table.GLOBL), # ext
    0x80321BAC: table.sym_fnc("Na_BGM_stop", arg=(
        "u16",
    ), flag=table.GLOBL), # ext
    0x80321CE4: table.sym_fnc("Na_BGM_fadeout", arg=(
        "u16",
        "u16",
    ), flag=table.GLOBL), # ext
    0x80321D38: table.sym_fnc("Na_g_80321D38", flag=table.GLOBL), # ext
    0x80321D5C: table.sym_fnc("Na_g_80321D5C", "u16",
    flag=table.GLOBL), # ext
    0x80321D9C: table.sym_fnc("Na_g_80321D9C"),
    0x80321E48: table.sym_fnc("Na_BGM_fadeto_start", arg=(
        "u8",
        "u8",
        "u8",
        "u16",
    ), flag=table.GLOBL), # ext
    0x80321F48: table.sym_fnc("Na_BGM_fadeto_end", arg=(
        "u16",
    ), flag=table.GLOBL), # ext
    0x80321F9C: table.sym_fnc("Na_fadeout", arg=(
        "u16",
    ), flag=table.GLOBL), # ext
    0x80322078: table.sym_fnc("Na_g_80322078", flag=table.GLOBL), # ext
    0x803220B4: table.sym_fnc("Na_g_803220B4", flag=table.GLOBL), # ext
    0x803220F0: table.sym_fnc("Na_g_803220F0", flag=table.GLOBL), # ext
    0x8032212C: table.sym_fnc("Na_g_8032212C", flag=table.GLOBL), # ext
    0x80322168: table.sym_fnc("Na_g_80322168", arg=(
        "u8",
    ), flag=table.GLOBL), # ext
    0x803221B8: table.sym_fnc("Na_g_803221B8", flag=table.GLOBL), # ext
    0x803221F4: table.sym_fnc("Na_g_803221F4", flag=table.GLOBL), # ext
    0x80322230: table.sym_fnc("Na_mode", arg=(
        "u8",
    ), flag=table.GLOBL), # ext
    0x8032231C: table.sym_fnc("Na_output", arg=(
        "int",
    ), flag=table.GLOBL), # ext
    0x80322348: table.sym_fnc("Na_g_80322348", arg=(
        "int",
        "int",
        "int",
        "int",
    )), # unused
    0x8032235C: table.sym_fnc("Na_g_8032235C", arg=(
        "int",
    )), # unused

    # ==========================================================================
    # data
    # ==========================================================================

    0x8032D5F8: table.sym("demo_record+demo__count"),
    0x8032D5F9: table.sym("demo_record+demo__stick_x"),
    0x8032D5FA: table.sym("demo_record+demo__stick_y"),
    0x8032D5FB: table.sym("demo_record+demo__button"),

    0x8032D950: table.sym("pl_collision_table+pl_collision__type"),
    0x8032D954: table.sym("pl_collision_table+pl_collision__callback"),

    0x8032DADB: table.sym("player_8032DACC+1*15"),
    0x8032DAE0: table.sym("player_8032DAE0+0"),
    0x8032DAE4: table.sym("player_8032DAE0+4"),

    0x8032DBE2: table.sym("pl_demo_8032DC3C-1*90"),
    0x8032DC36: table.sym("pl_demo_8032DC34+2"),
    0x8032DC3A: table.sym("pl_demo_8032DC38+2"),

    0x8032DD97: table.sym("save_course-1"),

    0x8032F4D4: table.sym("camdemo_8032F4D4+camdemo__callback"),
    0x8032F4D8: table.sym("camdemo_8032F4D4+camdemo__time"),
    0x8032F534: table.sym("camdemo_8032F534+camdemo__callback"),
    0x8032F538: table.sym("camdemo_8032F534+camdemo__time"),
    0x8032F544: table.sym("camdemo_8032F544+camdemo__callback"),
    0x8032F548: table.sym("camdemo_8032F544+camdemo__time"),
    0x8032F554: table.sym("camdemo_8032F554+camdemo__callback"),
    0x8032F558: table.sym("camdemo_8032F554+camdemo__time"),
    0x8032F564: table.sym("camdemo_8032F564+camdemo__callback"),
    0x8032F568: table.sym("camdemo_8032F564+camdemo__time"),
    0x8032F56C: table.sym("camdemo_8032F56C+camdemo__callback"),
    0x8032F570: table.sym("camdemo_8032F56C+camdemo__time"),
    0x8032F574: table.sym("camdemo_8032F574+camdemo__callback"),
    0x8032F578: table.sym("camdemo_8032F574+camdemo__time"),
    0x8032F59C: table.sym("camdemo_8032F59C+camdemo__callback"),
    0x8032F5A0: table.sym("camdemo_8032F59C+camdemo__time"),
    0x8032F5C4: table.sym("camdemo_8032F5C4+camdemo__callback"),
    0x8032F5C8: table.sym("camdemo_8032F5C4+camdemo__time"),
    0x8032F5DC: table.sym("camdemo_8032F5DC+camdemo__callback"),
    0x8032F5E0: table.sym("camdemo_8032F5DC+camdemo__time"),
    0x8032F5F4: table.sym("camdemo_8032F5F4+camdemo__callback"),
    0x8032F5F8: table.sym("camdemo_8032F5F4+camdemo__time"),
    0x8032F60C: table.sym("camdemo_8032F60C+camdemo__callback"),
    0x8032F610: table.sym("camdemo_8032F60C+camdemo__time"),
    0x8032F624: table.sym("camdemo_8032F624+camdemo__callback"),
    0x8032F628: table.sym("camdemo_8032F624+camdemo__time"),
    0x8032F634: table.sym("camdemo_8032F634+camdemo__callback"),
    0x8032F638: table.sym("camdemo_8032F634+camdemo__time"),
    0x8032F63C: table.sym("camdemo_8032F63C+camdemo__callback"),
    0x8032F640: table.sym("camdemo_8032F63C+camdemo__time"),
    0x8032F64C: table.sym("camdemo_8032F64C+camdemo__callback"),
    0x8032F650: table.sym("camdemo_8032F64C+camdemo__time"),
    0x8032F65C: table.sym("camdemo_8032F65C+camdemo__callback"),
    0x8032F660: table.sym("camdemo_8032F65C+camdemo__time"),
    0x8032F674: table.sym("camdemo_8032F674+camdemo__callback"),
    0x8032F678: table.sym("camdemo_8032F674+camdemo__time"),
    0x8032F69C: table.sym("camdemo_8032F69C+camdemo__callback"),
    0x8032F6A0: table.sym("camdemo_8032F69C+camdemo__time"),
    0x8032F6AC: table.sym("camdemo_8032F6AC+camdemo__callback"),
    0x8032F6B0: table.sym("camdemo_8032F6AC+camdemo__time"),
    0x8032F6BC: table.sym("camdemo_8032F6BC+camdemo__callback"),
    0x8032F6C0: table.sym("camdemo_8032F6BC+camdemo__time"),
    0x8032F6CC: table.sym("camdemo_8032F6CC+camdemo__callback"),
    0x8032F6D0: table.sym("camdemo_8032F6CC+camdemo__time"),
    0x8032F6DC: table.sym("camdemo_8032F6DC+camdemo__callback"),
    0x8032F6E0: table.sym("camdemo_8032F6DC+camdemo__time"),
    0x8032F6F4: table.sym("camdemo_8032F6F4+camdemo__callback"),
    0x8032F6F8: table.sym("camdemo_8032F6F4+camdemo__time"),
    0x8032F6FC: table.sym("camdemo_8032F6FC+camdemo__callback"),
    0x8032F700: table.sym("camdemo_8032F6FC+camdemo__time"),
    0x8032F70C: table.sym("camdemo_8032F70C+camdemo__callback"),
    0x8032F710: table.sym("camdemo_8032F70C+camdemo__time"),
    0x8032F714: table.sym("camdemo_8032F714+camdemo__callback"),
    0x8032F718: table.sym("camdemo_8032F714+camdemo__time"),
    0x8032F71C: table.sym("camdemo_8032F71C+camdemo__callback"),
    0x8032F720: table.sym("camdemo_8032F71C+camdemo__time"),
    0x8032F72C: table.sym("camdemo_8032F72C+camdemo__callback"),
    0x8032F730: table.sym("camdemo_8032F72C+camdemo__time"),
    0x8032F734: table.sym("camdemo_8032F734+camdemo__callback"),
    0x8032F738: table.sym("camdemo_8032F734+camdemo__time"),
    0x8032F74C: table.sym("camdemo_8032F74C+camdemo__callback"),
    0x8032F750: table.sym("camdemo_8032F74C+camdemo__time"),
    0x8032F754: table.sym("camdemo_8032F754+camdemo__callback"),
    0x8032F758: table.sym("camdemo_8032F754+camdemo__time"),
    0x8032F75C: table.sym("camdemo_8032F75C+camdemo__callback"),
    0x8032F760: table.sym("camdemo_8032F75C+camdemo__time"),
    0x8032F764: table.sym("camdemo_8032F764+camdemo__callback"),
    0x8032F768: table.sym("camdemo_8032F764+camdemo__time"),
    0x8032F76C: table.sym("camdemo_8032F76C+camdemo__callback"),
    0x8032F770: table.sym("camdemo_8032F76C+camdemo__time"),
    0x8032F774: table.sym("camdemo_8032F774+camdemo__callback"),
    0x8032F778: table.sym("camdemo_8032F774+camdemo__time"),
    0x8032F784: table.sym("camdemo_8032F784+camdemo__callback"),
    0x8032F788: table.sym("camdemo_8032F784+camdemo__time"),
    0x8032F794: table.sym("camdemo_8032F794+camdemo__callback"),
    0x8032F798: table.sym("camdemo_8032F794+camdemo__time"),
    0x8032F7A4: table.sym("camdemo_8032F7A4+camdemo__callback"),
    0x8032F7A8: table.sym("camdemo_8032F7A4+camdemo__time"),
    0x8032F7B4: table.sym("camdemo_8032F7B4+camdemo__callback"),
    0x8032F7B8: table.sym("camdemo_8032F7B4+camdemo__time"),
    0x8032F7C4: table.sym("camdemo_8032F7C4+camdemo__callback"),
    0x8032F7C8: table.sym("camdemo_8032F7C4+camdemo__time"),
    0x8032F7D4: table.sym("camdemo_8032F7D4+camdemo__callback"),
    0x8032F7D8: table.sym("camdemo_8032F7D4+camdemo__time"),
    0x8032F7EC: table.sym("camdemo_8032F7EC+camdemo__callback"),
    0x8032F7F0: table.sym("camdemo_8032F7EC+camdemo__time"),

    0x803301AA: table.sym("object_a_803301A8+object_a_1__scale"),
    0x803301AC: table.sym("object_a_803301A8+object_a_1__map"),
    0x803301B0: table.sym("object_a_803301A8+object_a_1__dist"),
    0x803301D0: table.sym("object_a_803301D0+obj_pcl__arg"),
    0x803301D1: table.sym("object_a_803301D0+obj_pcl__count"),
    0x803301D3: table.sym("object_a_803301D0+obj_pcl__offset"),
    0x803301DC: table.sym("object_a_803301D0+obj_pcl__s_add"),
    0x803301E0: table.sym("object_a_803301D0+obj_pcl__s_mul"),
    0x80330204: table.sym("object_a_80330204+2*0"),
    0x80330206: table.sym("object_a_80330204+2*1"),
    0x8033022C: table.sym("object_a_8033022C+2*0"),
    0x8033022E: table.sym("object_a_8033022C+2*1"),
    0x80330244: table.sym("object_a_80330244+2*0"),
    0x80330246: table.sym("object_a_80330244+2*1"),
    0x80330260: table.sym("object_a_80330260+4*0"),
    0x80330264: table.sym("object_a_80330260+4*1"),
    0x803302AC: table.sym("object_a_803302AC+object_a_2__count"),
    0x803302B2: table.sym("object_a_803302AC+object_a_2__shape"),
    0x803302B4: table.sym("object_a_803302AC+object_a_2__map"),
    0x803302EC: table.sym("object_a_803302EC+2*0"),
    0x803302EE: table.sym("object_a_803302EC+2*1"),
    0x803302F0: table.sym("object_a_803302EC+2*2"),
    0x803303C0: table.sym("object_a_803303C0+2*0"),
    0x803303C2: table.sym("object_a_803303C0+2*1"),
    0x8033047E: table.sym("object_a_80330480+2*(3*-1+2)"),
    0x80330480: table.sym("object_a_80330480+2*0"),
    0x80330482: table.sym("object_a_80330480+2*1"),
    0x80330484: table.sym("object_a_80330480+2*2"),
    0x803305F8: table.sym("object_a_803305F8+object_a_3__map"),
    0x803305FC: table.sym("object_a_803305F8+object_a_3__px"),
    0x803305FE: table.sym("object_a_803305F8+object_a_3__pz"),
    0x80330600: table.sym("object_a_803305F8+object_a_3__ry"),
    0x803306B4: table.sym("object_a_803306B4+object_a_4__offset"),
    0x803306C4: table.sym("object_a_803306B4+object_a_4__vel"),
    0x80330C48: table.sym("object_a_80330C48+object_a_7__offset"),
    0x80330C4C: table.sym("object_a_80330C48+object_a_7__map"),
    0x80330DAC: table.sym("object_a_80330DAC+object_a_8__time"),
    0x80330DB4: table.sym("object_a_80330DAC+object_a_8__vel"),

    0x80330EE0: table.sym("shadow_rect_table+shadow_rect__sx"),
    0x80330EE4: table.sym("shadow_rect_table+shadow_rect__sz"),
    0x80330EE8: table.sym("shadow_rect_table+shadow_rect__y_scale"),

    0x80330F64: table.sym("scroll_table_a+scroll__index"),
    0x80330F70: table.sym("scroll_table_a+scroll__data"),
    0x80330F84: table.sym("scroll_table_a+scroll__layer"),

    0x803311A4: table.sym("scroll_table_b+scroll__index"),
    0x803311B0: table.sym("scroll_table_b+scroll__data"),
    0x803311C4: table.sym("scroll_table_b+scroll__layer"),

    0x8033127C: table.sym("scroll_table_c+scroll__index"),
    0x80331288: table.sym("scroll_table_c+scroll__data"),
    0x8033129C: table.sym("scroll_table_c+scroll__layer"),

    0x803317E0: table.sym("prg_obj_table+prg_obj__script"),
    0x803317E4: table.sym("prg_obj_table+prg_obj__shape"),
    0x803317E6: table.sym("prg_obj_table+prg_obj__arg"),

    0x80332350: table.sym("map_obj_table+map_obj__index"),
    0x80332351: table.sym("map_obj_table+map_obj__type"),
    0x80332352: table.sym("map_obj_table+map_obj__arg"),
    0x80332353: table.sym("map_obj_table+map_obj__shape"),
    0x80332354: table.sym("map_obj_table+map_obj__script"),

    0x803325F0: table.sym("meter+meter__mode"),
    0x803325F2: table.sym("meter+meter__x"),
    0x803325F4: table.sym("meter+meter__y"),

    0x8033282C: table.sym("object_b_8033282C+2*0"),
    0x8033282E: table.sym("object_b_8033282C+2*1"),

    0x80332860: table.sym("object_c_80332860+object_c_0__msg_start"),
    0x80332862: table.sym("object_c_80332860+object_c_0__msg_win"),
    0x80332864: table.sym("object_c_80332860+object_c_0__path"),
    0x803328D0: table.sym("object_c_803328D0+object_c_1__scale"),
    0x803328D4: table.sym("object_c_803328D0+object_c_1__se"),
    0x803328D8: table.sym("object_c_803328D0+object_c_1__dist"),
    0x803328DA: table.sym("object_c_803328D0+object_c_1__damage"),
    0x80332934: table.sym("object_c_80332938+4*-1"),
    0x80332984: table.sym("object_c_80332984+obj_pcl__arg"),
    0x80332987: table.sym("object_c_80332984+obj_pcl__offset"),
    0x8033298A: table.sym("object_c_80332984+obj_pcl__vy_add"),
    0x80332A20: table.sym("object_c_80332A20+object_c_2__map"),
    0x80332A24: table.sym("object_c_80332A20+object_c_2__p_map"),
    0x80332A28: table.sym("object_c_80332A20+object_c_2__p_shape"),
    0x80332A48: table.sym("object_c_80332A48+obj_pcl__arg"),
    0x80332A4B: table.sym("object_c_80332A48+obj_pcl__offset"),
    0x80332A4D: table.sym("object_c_80332A48+obj_pcl__vf_mul"),
    0x80332A4E: table.sym("object_c_80332A48+obj_pcl__vy_add"),
    0x80332AC0: table.sym("object_c_80332AC0+2*0"),
    0x80332AC2: table.sym("object_c_80332AC0+2*1"),
    0x80332B10: table.sym("object_c_80332B10+obj_pcl__arg"),
    0x80332B11: table.sym("object_c_80332B10+obj_pcl__count"),
    0x80332B13: table.sym("object_c_80332B10+obj_pcl__offset"),
    0x80332B14: table.sym("object_c_80332B10+obj_pcl__vf_add"),
    0x80332B16: table.sym("object_c_80332B10+obj_pcl__vy_add"),
    0x80332B1C: table.sym("object_c_80332B10+obj_pcl__s_add"),
    0x80332B64: table.sym("object_c_80332B64+object_c_3__map"),
    0x80332B68: table.sym("object_c_80332B64+object_c_3__shape"),
    0x80332CCC: table.sym("object_c_80332CCC+4*0"),
    0x80332CD0: table.sym("object_c_80332CCC+4*1"),
    0x80332CD4: table.sym("object_c_80332CCC+4*2"),
    0x80332D10: table.sym("object_c_80332D10+2*0"),
    0x80332D12: table.sym("object_c_80332D10+2*1"),
    0x80332D58: table.sym("object_c_80332D58+2*0"),
    0x80332D5A: table.sym("object_c_80332D58+2*1"),
    0x80332D5C: table.sym("object_c_80332D58+2*2"),
    0x80332E24: table.sym("object_c_80332E24+object_c_5__shape"),
    0x80332E28: table.sym("object_c_80332E24+object_c_5__script"),
    0x80332E2C: table.sym("object_c_80332E24+object_c_5__scale"),

    0x80333794: table.sym("Na_data_80333598+4*0x7F"),
    0x80333DF2: table.sym("Na_data_80333DE0+2*9"),
    0x80333FF0: table.sym("Na_pan_0+4*0x7F"),
    0x803341F0: table.sym("Na_pan_1+4*0x7F"),
    0x803343F0: table.sym("Na_pan_2+4*0x7F"),

    # ==========================================================================
    # bss
    # ==========================================================================

    0x8033AFA4: table.sym("controller_table+controller__status"),
    0x8033AFA8: table.sym("controller_table+controller__pad"),

    0x8033B098: table.sym("file_demo+file__buf"),

    0x8033B1A2: table.sym("player_table+player__rot_vel+2*0"),
    0x8033B1A4: table.sym("player_table+player__rot_vel+2*1"),
    0x8033B1A6: table.sym("player_table+player__rot_vel+2*2"),
    0x8033B1AC: table.sym("player_table+player__pos+4*0"),
    0x8033B1B0: table.sym("player_table+player__pos+4*1"),
    0x8033B1B4: table.sym("player_table+player__pos+4*2"),
    0x8033B1B8: table.sym("player_table+player__vel+4*0"),
    0x8033B1BC: table.sym("player_table+player__vel+4*1"),
    0x8033B1C0: table.sym("player_table+player__vel+4*2"),

    0x8033B248: table.sym("game_8033B248+struct_8033B248___00"),
    0x8033B249: table.sym("game_8033B248+struct_8033B248___01"),
    0x8033B24A: table.sym("game_8033B248+struct_8033B248___02"),
    0x8033B24B: table.sym("game_8033B248+struct_8033B248___03"),
    0x8033B24C: table.sym("game_8033B248+struct_8033B248___04"),

    0x8033B260: table.sym("hud+hud__life"),
    0x8033B262: table.sym("hud+hud__coin"),
    0x8033B264: table.sym("hud+hud__star"),
    0x8033B266: table.sym("hud+hud__power"),
    0x8033B268: table.sym("hud+hud__key"),
    0x8033B26A: table.sym("hud+hud__flag"),
    0x8033B26C: table.sym("hud+hud__timer"),

    0x8033B364: table.sym("shape_object_mirror+shape_object__list"),
    0x8033B368: table.sym("shape_object_mirror+shape_object__scene"),

    0x8033B3B7: table.sym("pl_shape_table+pl_shape__wing"),

    0x8033B8D0: table.sym("scene_data+scene__index"),
    0x8033B8D1: table.sym("scene_data+scene___01"),
    0x8033B8D2: table.sym("scene_data+scene__env"),
    0x8033B8D4: table.sym("scene_data+scene__s"),
    0x8033B8D8: table.sym("scene_data+scene__map"),
    0x8033B8DC: table.sym("scene_data+scene__area"),
    0x8033B8E0: table.sym("scene_data+scene__obj"),
    0x8033B8E4: table.sym("scene_data+scene__link"),
    0x8033B8E8: table.sym("scene_data+scene__linkbg"),
    0x8033B8EC: table.sym("scene_data+scene__connect"),
    0x8033B8F0: table.sym("scene_data+scene__spawn"),
    0x8033B8F4: table.sym("scene_data+scene__cam"),
    0x8033B8F8: table.sym("scene_data+scene__wind"),
    0x8033B8FC: table.sym("scene_data+scene__jet+4*0"),
    0x8033B900: table.sym("scene_data+scene__jet+4*1"),
    0x8033B904: table.sym("scene_data+scene__msg+0"),
    0x8033B905: table.sym("scene_data+scene__msg+1"),
    0x8033B906: table.sym("scene_data+scene__bgm_arg"),
    0x8033B908: table.sym("scene_data+scene__bgm_index"),

    0x8033BAB0: table.sym("wipe+wipe__flag"),
    0x8033BAB1: table.sym("wipe+wipe__type"),
    0x8033BAB2: table.sym("wipe+wipe___02"),
    0x8033BAB3: table.sym("wipe+wipe___03"),
    0x8033BAB4: table.sym("wipe+wipe__r"),
    0x8033BAB5: table.sym("wipe+wipe__g"),
    0x8033BAB6: table.sym("wipe+wipe__b"),
    0x8033BAB8: table.sym("wipe+wipe___08"),
    0x8033BABA: table.sym("wipe+wipe___0A"),
    0x8033BABC: table.sym("wipe+wipe___0C"),
    0x8033BABE: table.sym("wipe+wipe___0E"),
    0x8033BAC0: table.sym("wipe+wipe___10"),
    0x8033BAC2: table.sym("wipe+wipe___12"),
    0x8033BAC4: table.sym("wipe+wipe___14"),

    0x8033BB18: table.sym("shape_mf_stack+4*(4*3+0)"),
    0x8033BB1C: table.sym("shape_mf_stack+4*(4*3+1)"),
    0x8033BB20: table.sym("shape_mf_stack+4*(4*3+2)"),

    0x8033C390: table.sym("time+time___00"),
    0x8033C392: table.sym("time+time___02"),
    0x8033C398: table.sym("time+time___08+0"),
    0x8033C39C: table.sym("time+time___08+4"),
    0x8033C3C0: table.sym("time+time___30+0"),
    0x8033C3C4: table.sym("time+time___30+4"),

    0x8033D274: table.sym("object_8033D274+struct_8033D274__ground"),
    0x8033D276: table.sym("object_8033D274+struct_8033D274__roof"),
    0x8033D278: table.sym("object_8033D274+struct_8033D274__wall"),
    0x8033D4FC: table.sym("object_data+object__flag"),
    0x80360EA0: table.sym("object_dummy+object__list+obj_list__s+shape_object__scene"),
    0x80360EA1: table.sym("object_dummy+object__list+obj_list__s+shape_object__shape"),
    0x80361150: table.sym("obj_list_free+obj_list__next"),
    0x803611D8: table.sym("object_803611D8+1*0"),
    0x803611D9: table.sym("object_803611D8+1*1"),

    0x803612C0: table.sym("background_803612C0+struct_803612C0___00"),
    0x803612C2: table.sym("background_803612C0+struct_803612C0___02"),
    0x803612C4: table.sym("background_803612C0+struct_803612C0___04"),
    0x803612C8: table.sym("background_803612C0+struct_803612C0___08"),
    0x803612CC: table.sym("background_803612C0+struct_803612C0___0C"),

    # ==========================================================================

    0x00108A40: table.sym("_main_dataSegmentRomEnd"),
    0x004EC000: table.sym("_animeSegmentRomStart"),
    0x00579C20: table.sym("_demoSegmentRomStart"),
    0x0057B720: table.sym("_audioctlSegmentRomStart"),
    0x00593560: table.sym("_audiotblSegmentRomStart"),
    0x007B0860: table.sym("_audioseqSegmentRomStart"),
    0x007CC620: table.sym("_audiobnkSegmentRomStart"),

    # ==========================================================================

    0x80220D98: table.sym("_Na_bss-0x08"), # la
    0x80220DA0: table.sym("_Na_bss+0x00"), # la
    0x80220DB0: table.sym("_Na_bss+0x10"), # la
    0x80220DB1: table.sym("_Na_bss+0x11"),
    0x80220EA0: table.sym("_Na_bss+0x100"),
    0x80220EA2: table.sym("_Na_bss+0x102"),
    0x80220EA3: table.sym("_Na_bss+0x103"),
    0x80220EA8: table.sym("_Na_bss+0x108"), # la
    0x80220EB0: table.sym("_Na_bss+0x110"),
    0x80220EB8: table.sym("_Na_bss+0x118"), # la
    0x80220EC8: table.sym("_Na_bss+0x128"), # la
    0x80220EF8: table.sym("_Na_bss+0x158"), # la
    0x80220F08: table.sym("_Na_bss+0x168"), # la
    0x80220F18: table.sym("_Na_bss+0x178"), # la
    0x80220F28: table.sym("_Na_bss+0x188"),
    0x80220F2C: table.sym("_Na_bss+0x18C"), # la
    0x802210BC: table.sym("_Na_bss+0x31C"), # la
    0x802210C0: table.sym("_Na_bss+0x320"), # la
    0x802210F8: table.sym("_Na_bss+0x358"),
    0x802210FC: table.sym("_Na_bss+0x35C"), # la
    0x8022128C: table.sym("_Na_bss+0x4EC"), # la
    0x80221290: table.sym("_Na_bss+0x4F0"), # la
    0x802212C8: table.sym("_Na_bss+0x528"), # la
    0x802212CC: table.sym("_Na_bss+0x52C"), # la
    0x8022145C: table.sym("_Na_bss+0x6BC"), # la
    0x80221460: table.sym("_Na_bss+0x6C0"), # la
    0x80221498: table.sym("_Na_bss+0x6F8"), # la
    0x802214A8: table.sym("_Na_bss+0x708"), # la
    0x802214B0: table.sym("_Na_bss+0x710"), # la
    0x802214C0: table.sym("_Na_bss+0x720"), # la
    0x802214D0: table.sym("_Na_bss+0x730"),
    0x80221510: table.sym("_Na_bss+0x770"),
    0x80221610: table.sym("_Na_bss+0x870"), # la
    0x80222610: table.sym("_Na_bss+0x1870"),
    0x80222618: table.sym("_Na_bss+0x1878"),
    0x80222619: table.sym("_Na_bss+0x1879"),
    0x8022261A: table.sym("_Na_bss+0x187A"),
    0x80222630: table.sym("_Na_bss+0x1890"),
    0x80222644: table.sym("_Na_bss+0x18A4"),
    0x802226A8: table.sym("_Na_bss+0x1908"), # la
    0x802228C4: table.sym("_Na_bss+0x1B24"),
    0x802229D8: table.sym("_Na_bss+0x1C38"), # la
    0x802241D8: table.sym("_Na_bss+0x3438"), # la
    0x80224248: table.sym("_Na_bss+0x34A8"), # la
    0x80225BD8: table.sym("_Na_bss+0x4E38"), # la
    0x80225C98: table.sym("_Na_bss+0x4EF8"),
    0x80225CA8: table.sym("_Na_bss+0x4F08"), # la
    0x80225CAC: table.sym("_Na_bss+0x4F0C"),
    0x80225CB8: table.sym("_Na_bss+0x4F18"), # la
    0x80225CC8: table.sym("_Na_bss+0x4F28"), # la
    0x80225CD8: table.sym("_Na_bss+0x4F38"), # la
    0x80225CE8: table.sym("_Na_bss+0x4F48"), # la
    0x80225D00: table.sym("_Na_bss+0x4F60"), # la
    0x80225E00: table.sym("_Na_bss+0x5060"), # la
    0x80226300: table.sym("_Na_bss+0x5560"), # la
    0x80226318: table.sym("_Na_bss+0x5578"), # la
    0x80226320: table.sym("_Na_bss+0x5580"), # la
    0x80226338: table.sym("_Na_bss+0x5598"), # la
    0x80226938: table.sym("_Na_bss+0x5B98"),
    0x8022693C: table.sym("_Na_bss+0x5B9C"),
    0x80226940: table.sym("_Na_bss+0x5BA0"),
    0x80226948: table.sym("_Na_bss+0x5BA8"), # la
    0x80226A48: table.sym("_Na_bss+0x5CA8"), # la
    0x80226B48: table.sym("_Na_bss+0x5DA8"),
    0x80226B49: table.sym("_Na_bss+0x5DA9"),
    0x80226B4A: table.sym("_Na_bss+0x5DAA"),
    0x80226B4B: table.sym("_Na_bss+0x5DAB"),
    0x80226B4C: table.sym("_Na_bss+0x5DAC"),
    0x80226B50: table.sym("_Na_bss+0x5DB0"),
    0x80226B54: table.sym("_Na_bss+0x5DB4"),
    0x80226B58: table.sym("_Na_bss+0x5DB8"),
    0x80226B5C: table.sym("_Na_bss+0x5DBC"),
    0x80226B60: table.sym("_Na_bss+0x5DC0"),
    0x80226B64: table.sym("_Na_bss+0x5DC4"),
    0x80226B68: table.sym("_Na_bss+0x5DC8"), # la
    0x80226B6C: table.sym("_Na_bss+0x5DCC"), # la
    0x80226B70: table.sym("_Na_bss+0x5DD0"),
    0x80226B74: table.sym("_Na_bss+0x5DD4"),
    0x80226B78: table.sym("_Na_bss+0x5DD8"),
    0x80226B7C: table.sym("_Na_bss+0x5DDC"),
    0x80226B7E: table.sym("_Na_bss+0x5DDE"),
    0x80226B7F: table.sym("_Na_bss+0x5DDF"),
    0x80226B80: table.sym("_Na_bss+0x5DE0"), # la
    0x80226B84: table.sym("_Na_bss+0x5DE4"), # la
    0x80226B88: table.sym("_Na_bss+0x5DE8"),
    0x80226B8C: table.sym("_Na_bss+0x5DEC"),
    0x80226B90: table.sym("_Na_bss+0x5DF0"),
    0x80226B98: table.sym("_Na_bss+0x5DF8"),
    0x80226B9C: table.sym("_Na_bss+0x5DFC"),
    0x80226BA0: table.sym("_Na_bss+0x5E00"), # la
    0x80226C40: table.sym("_Na_bss+0x5EA0"),
    0x80226C4C: table.sym("_Na_bss+0x5EAC"),
    0x80226C52: table.sym("_Na_bss+0x5EB2"), # la
    0x80226C58: table.sym("_Na_bss+0x5EB8"), # la
    0x80226C98: table.sym("_Na_bss+0x5EF8"), # la
    0x80226CB8: table.sym("_Na_bss+0x5F18"),
    0x80226CC0: table.sym("_Na_bss+0x5F20"), # la

    0x80207690: table.sym("save-0x70"),
    0x80207698: table.sym("save-0x68"),
    0x8020769C: table.sym("save-0x64"),
    0x80207708: table.sym("save+0x08"),
    0x8020770C: table.sym("save+0x0C"),
    0x80207725: table.sym("save+0x25"),
    0x802078C0: table.sym("save+0x1C0"),
}

dev_E0_t_main = {
    0x80248AA4: 0x00108A10,
    # 0x80248AA8: 0x00108A10,
    # 0x80248AAC: 0x00108A10,
    0x80248AB0: 0x00108A10,
    0x80248AC0: 0x00108A40,
    0x80248AC4: 0x00108A40,
    0x80248AC8: 0x00108A40,
    0x80248ACC: 0x00108A40,

    0x80278994: 0x000F5580,
    0x80278998: 0x000F5580,
    0x8027899C: 0x000F5580,
    0x802789A0: 0x000F5580,
    0x802789CC: 0x000F5580,
    0x802789D0: 0x000F5580,
    0x802789D4: 0x000F5580,
    0x802789D8: 0x000F5580,

    0x80247BAC: 0x000E6260,
    0x80247BB8: 0x000E6260,
    0x80247BD8: 0x000E6330,
    0x80247BDC: 0x000E6330,
    0x8031EA30: 0x000E6260,
    0x8031EA38: 0x000F52C0,
    0x8031EA40: 0x000E6260,
    0x8031EA58: 0x000F52C0,
    0x8031EA68: 0x000F52C0,
    0x8031EA70: 0x000F52C0,
}

# todo: fmt_struct_*

imm_E0_t_main = {
    # src/mem.S
    0x80278074: (fmt_mask,),
    0x80278078: (fmt_mask,),
    0x80278080: ("sizeof__mem_link",),
    0x8027808C: (fmt_mask,),
    0x80278094: ("-sizeof__mem_link",),
    0x802780C8: ("-sizeof__mem_link",),
    0x802780E8: ("mem_link__prev",),
    0x802780F4: ("mem_link__next",),
    0x80278100: ("mem_link__prev",),
    0x8027810C: ("mem_link__next",),
    0x80278128: (fmt_mask,),
    0x8027812C: (fmt_mask,),
    0x80278138: ("sizeof__mem_link",),
    0x80278190: ("mem_link__next",),
    0x802781A0: ("mem_link__prev",),
    0x802781A8: ("mem_link__next",),
    0x802781B4: ("sizeof__mem_link",),
    0x802781E8: ("mem_link__prev",),
    0x802781F8: ("mem_link__next",),
    0x80278200: ("mem_link__prev",),
    0x80278218: ("sizeof__mem_link",),
    0x8027823C: ("-sizeof__mem_link",),
    0x80278244: ("-sizeof__mem_link",),
    0x80278268: ("mem_link__next",),
    0x80278278: ("mem_link__next",),
    0x80278284: ("mem_link__next",),
    0x802782A4: ("mem_link__next",),
    0x802782D4: ("mem_link__prev",),
    0x802782E4: ("mem_link__prev",),
    0x802782F0: ("mem_link__prev",),
    0x80278304: ("mem_link__next",),
    0x80278314: ("mem_link__prev",),
    0x80278370: ("-sizeof__mem_link",),
    0x80278384: ("mem_link__next",),
    0x802783A0: (fmt_mem_alloc,),
    0x802783D4: ("-sizeof__mem_link",),
    0x80278420: ("sizeof__mem",),
    0x80278428: (fmt_mem_alloc,),
    0x80278440: ("mem__size",),
    0x80278450: ("mem__l",),
    0x80278460: ("mem__r",),
    0x80278470: ("mem__mem",),
    0x802784A4: ("mem__size",),
    0x802784B8: ("mem__l",),
    0x802784CC: ("mem__r",),
    0x802784E0: ("mem__mem",),
    0x80278520: (fmt_mask,),
    0x80278528: (fmt_mask,),
    0x8027858C: (ultra.fmt_os_mesg_pri,),
    0x80278590: (ultra.fmt_os_readwrite,),
    0x802785B8: (ultra.fmt_os_mesg_flag,),
    0x8027862C: (fmt_mask,),
    0x80278634: (fmt_mask,),
    0x80278710: (fmt_mask,),
    0x80278718: (fmt_mask,),
    0x80278730: (fmt_mask,),
    0x80278738: (fmt_mask,),
    0x80278760: (fmt_mem_alloc,),
    0x802787F8: (fmt_mask,),
    0x80278800: (fmt_mask,),
    0x80278814: (fmt_mem_alloc,),
    0x80278848: (fmt_mem_alloc,),
    0x802788D4: (fmt_mask,),
    0x802788DC: (fmt_mask,),
    0x802788F0: (fmt_mem_alloc,),
    0x80278980: ("SEGMENT_MAIN2",),
    0x8027898C: ("SEGMENT_CIMG-SEGMENT_MAIN2",),
    0x802789A8: (fmt_mask,),
    0x802789AC: (fmt_mask,),
    0x80278A2C: (fmt_mask,),
    0x80278A30: (fmt_mask,),
    0x80278A48: ("sizeof__arena",),
    0x80278A6C: ("arena__size",),
    0x80278A74: ("arena__used",),
    0x80278A80: ("sizeof__arena",),
    0x80278A84: ("arena__start",),
    0x80278A90: ("sizeof__arena",),
    0x80278A94: ("arena__free",),
    0x80278AC0: (fmt_mask,),
    0x80278AC4: (fmt_mask,),
    0x80278AD8: ("arena__used",),
    0x80278ADC: ("arena__size",),
    0x80278AF0: ("arena__free",),
    0x80278AF8: ("arena__free",),
    0x80278B00: ("arena__free",),
    0x80278B04: ("arena__used",),
    0x80278B0C: ("arena__used",),
    0x80278B3C: (fmt_mask,),
    0x80278B40: (fmt_mask,),
    0x80278B58: ("sizeof__arena",),
    0x80278B74: ("arena__size",),
    0x80278BB0: (fmt_mask,),
    0x80278BB4: (fmt_mask,),
    0x80278BCC: ("sizeof__heap",),
    0x80278BF0: ("heap__size",),
    0x80278BFC: ("sizeof__heap",),
    0x80278C00: ("heap__start",),
    0x80278C0C: ("sizeof__heap",),
    0x80278C10: ("heap__free",),
    0x80278C18: ("heap__start",),
    0x80278C24: ("heap_link__next",),
    0x80278C30: ("heap__size",),
    0x80278C34: ("heap_link__size",),
    0x80278C5C: ("heap__free",),
    0x80278C68: (fmt_mask,),
    0x80278C6C: (fmt_mask,),
    0x80278C78: ("sizeof__heap_link",),
    0x80278C94: ("heap_link__size",),
    0x80278CAC: ("sizeof__heap_link",),
    0x80278CBC: ("heap_link__size",),
    0x80278CC4: ("sizeof__heap_link+1",),
    0x80278CD8: ("heap_link__next",),
    0x80278D00: ("heap_link__size",),
    0x80278D08: ("heap_link__size",),
    0x80278D18: ("heap_link__next",),
    0x80278D1C: ("heap_link__next",),
    0x80278D28: ("heap_link__size",),
    0x80278D78: ("-sizeof__heap_link",),
    0x80278D80: ("heap__free",),
    0x80278D88: ("heap__free",),
    0x80278D98: ("heap__free",),
    0x80278DA4: ("heap_link__next",),
    0x80278DAC: ("heap__free",),
    0x80278DC0: ("heap__free",),
    0x80278DC4: ("heap_link__size",),
    0x80278DDC: ("heap_link__size",),
    0x80278DE0: ("heap_link__size",),
    0x80278DE8: ("heap_link__size",),
    0x80278DF4: ("heap_link__next",),
    0x80278DF8: ("heap_link__next",),
    0x80278E04: ("heap__free",),
    0x80278E08: ("heap__free",),
    0x80278E10: ("heap_link__next",),
    0x80278E18: ("heap__free",),
    0x80278E28: ("heap_link__next",),
    0x80278E48: ("heap_link__next",),
    0x80278E64: ("heap_link__next",),
    0x80278E70: ("heap_link__next",),
    0x80278E84: ("heap_link__size",),
    0x80278E9C: ("heap_link__size",),
    0x80278EA0: ("heap_link__size",),
    0x80278EA8: ("heap_link__size",),
    0x80278EC0: ("heap_link__next",),
    0x80278EC4: ("heap_link__next",),
    0x80278ED0: ("heap_link__next",),
    0x80278ED8: ("heap_link__next",),
    0x80278EE4: ("heap_link__size",),
    0x80278EF8: ("heap_link__next",),
    0x80278EFC: ("heap_link__size",),
    0x80278F00: ("heap_link__size",),
    0x80278F08: ("heap_link__size",),
    0x80278F10: ("heap_link__next",),
    0x80278F14: ("heap_link__next",),
    0x80278F18: ("heap_link__next",),
    0x80278F34: (fmt_mask,),
    0x80278F38: (fmt_mask,),
    0x80278FB0: (fmt_mem_alloc,),
    0x80278FC8: ("file_table__len",),
    0x80278FD0: ("sizeof__file_table",),
    0x80278FE8: (fmt_mem_alloc,),
    0x80279004: ("file_table__src",),
    0x80279054: ("file__table",),
    0x8027905C: ("file__src",),
    0x80279068: ("file__buf",),
    0x8027909C: ("file__table",),
    0x802790AC: ("file_table__len",),
    0x802790CC: ("file_table__table+file_table__table__start",),
    0x802790D0: ("file_table__src",),
    0x802790EC: ("file_table__table+file_table__table__size",),
    0x802790FC: ("file__src",),
    0x80279118: ("file__buf",),
    0x8027912C: ("file__src",),
    0x80279130: (fmt_bool,),
}

sym_E0_d_main = {
    # ==========================================================================
    # data
    # ==========================================================================

    # src/main.c
    0x8032D560: table.sym_var("sc_client_1",        "SC_CLIENT *",  flag=table.GLOBL|ultra.DALIGN),
    0x8032D564: table.sym_var("sc_client_2",        "SC_CLIENT *",  flag=table.GLOBL|ultra.DALIGN),
    0x8032D568: table.sym_var("sc_task",            "SC_TASK *",    flag=table.GLOBL|ultra.DALIGN),
    0x8032D56C: table.sym_var("sc_audtask",         "SC_TASK *",    flag=table.GLOBL|ultra.DALIGN),
    0x8032D570: table.sym_var("sc_gfxtask",         "SC_TASK *",    flag=table.GLOBL|ultra.DALIGN),
    0x8032D574: table.sym_var("sc_audtask_next",    "SC_TASK *",    flag=table.GLOBL|ultra.DALIGN),
    0x8032D578: table.sym_var("sc_gfxtask_next",    "SC_TASK *",    flag=table.GLOBL|ultra.DALIGN),
    0x8032D57C: table.sym_var("sc_audio",           "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032D580: table.sym_var("sc_vi",              "u32",  flag=table.GLOBL|ultra.DALIGN),
    0x8032D584: table.sym_var("reset_timer",        "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032D588: table.sym_var("reset_frame",        "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032D58C: table.sym_var("debug_stage",        "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032D590: table.sym_var("debug_thread",       "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032D594: table.sym_var("debug_time",         "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032D598: table.sym_var("debug_mem",          "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032D59C: table.sym_var("debug_time_table",   "u16", "[]"),
    0x8032D5AC: table.sym_var("debug_mem_table",    "u16", "[]"),
    0x8032D5BC: table.sym_var("debug_time_index",   "s16",  flag=ultra.DALIGN),
    0x8032D5C0: table.sym_var("debug_mem_index",    "s16",  flag=ultra.DALIGN),

    # src/app.c
    0x8032D5D0: table.sym_var("app_8032D5D0",       "u32",  flag=table.GLOBL|ultra.DALIGN), # unused
    0x8032D5D4: table.sym_var("video_frame",        "u32",  flag=table.GLOBL|ultra.DALIGN),
    0x8032D5D8: table.sym_var("video_vi",           "u16",  flag=table.GLOBL|ultra.DALIGN),
    0x8032D5DC: table.sym_var("video_dp",           "u16",  flag=table.GLOBL|ultra.DALIGN),
    0x8032D5E0: table.sym_var_fnc("video_callback",         flag=table.GLOBL|ultra.DALIGN),
    0x8032D5E4: table.sym_var("controller_1",       "CONTROLLER *", flag=table.GLOBL|ultra.DALIGN),
    0x8032D5E8: table.sym_var("controller_2",       "CONTROLLER *", flag=table.GLOBL|ultra.DALIGN),
    0x8032D5EC: table.sym_var("controller_menu",    "CONTROLLER *", flag=table.GLOBL|ultra.DALIGN),
    0x8032D5F0: table.sym_var("demo",               "DEMO *",       flag=table.GLOBL|ultra.DALIGN),
    0x8032D5F4: table.sym_var("demo_index",         "u16",  flag=table.GLOBL|ultra.DALIGN),
    0x8032D5F8: table.sym_var("demo_record",        "DEMO"),

    # src/audio.c
    0x8032D600: table.sym_var("audio_mute", "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032D604: table.sym_var("audio_lock", "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032D608: table.sym_var("bgm_stage",    "u16",  flag=table.GLOBL|ultra.DALIGN),
    0x8032D60C: table.sym_var("bgm_shell",    "u16",  flag=table.GLOBL|ultra.DALIGN),
    0x8032D610: table.sym_var("bgm_special",  "u16",  flag=table.GLOBL|ultra.DALIGN),
    0x8032D614: table.sym_var("audio_endless",      "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032D618: table.sym_var("audio_8032D618",     "u32",      "[4]",  table.GLOBL),
    0x8032D628: table.sym_var("audio_output_table", "s16",      "[]",   table.GLOBL),
    0x8032D630: table.sym_var("audio_env_se_table", "NA_SE",    "[]",   table.GLOBL),
    0x8032D6C0: table.sym_var("audio_ripple",       "s8",   flag=table.GLOBL|ultra.DALIGN),

    # src/pl_physics.c
    0x8032DAF0: table.sym_var("pl_physics_8032DAF0",    "s16", "[]",    table.GLOBL),
    0x8032DAF8: table.sym_var("pl_physics_8032DAF8",    "MAP_FACE",     flag=table.GLOBL),

    # src/pl_grab.c
    0x8032DD40: table.sym_var("pl_grab_8032DD40",   "s8", "[]", table.GLOBL),

    # src/game.c
    0x8032D6D0: table.sym_var("staff_01",   "static const char *", "[]"),
    0x8032D6D8: table.sym_var("staff_02",   "static const char *", "[]"),
    0x8032D6E4: table.sym_var("staff_03",   "static const char *", "[]"),
    0x8032D6F0: table.sym_var("staff_04",   "static const char *", "[]"),
    0x8032D700: table.sym_var("staff_05",   "static const char *", "[]"),
    0x8032D710: table.sym_var("staff_06",   "static const char *", "[]"),
    0x8032D71C: table.sym_var("staff_07",   "static const char *", "[]"),
    0x8032D728: table.sym_var("staff_08",   "static const char *", "[]"),
    0x8032D738: table.sym_var("staff_09",   "static const char *", "[]"),
    0x8032D740: table.sym_var("staff_10",   "static const char *", "[]"),
    0x8032D750: table.sym_var("staff_11",   "static const char *", "[]"),
    0x8032D75C: table.sym_var("staff_12",   "static const char *", "[]"),
    0x8032D764: table.sym_var("staff_13",   "static const char *", "[]"),
    0x8032D774: table.sym_var("staff_14",   "static const char *", "[]"),
    0x8032D77C: table.sym_var("staff_15",   "static const char *", "[]"),
    0x8032D788: table.sym_var("staff_16",   "static const char *", "[]"),
    0x8032D79C: table.sym_var("staff_17",   "static const char *", "[]"),
    0x8032D7AC: table.sym_var("staff_18",   "static const char *", "[]"),
    0x8032D7BC: table.sym_var("staff_19",   "static const char *", "[]"),
    0x8032D7C4: table.sym_var("staff_20",   "static const char *", "[]"),
    0x8032D7CC: table.sym_var("staff_table",    "STAFF", "[]",  table.GLOBL),
    0x8032D93C: table.sym_var("mario",          "PLAYER *",     flag=table.GLOBL|ultra.DALIGN),
    0x8032D940: table.sym_var("game_8032D940",  "s16",  flag=table.GLOBL|ultra.DALIGN), # unused
    0x8032D944: table.sym_var("game_8032D944",  "s8",   flag=table.GLOBL|ultra.DALIGN),

    # src/pl_collision.c
    0x8032D950: table.sym_var("pl_collision_table",     "PL_COLLISION", "[]", table.GLOBL),
    0x8032DA48: table.sym_var("pl_collision_8032DA48",  "u32", "[]", table.GLOBL),
    0x8032DA6C: table.sym_var("pl_collision_8032DA6C",  "u32", "[]", table.GLOBL),
    0x8032DA90: table.sym_var("pl_collision_8032DA90",  "u8", flag=table.GLOBL|ultra.DALIGN),
    0x8032DA94: table.sym_var("pl_collision_8032DA94",  "u8", flag=table.GLOBL|ultra.DALIGN),
    0x8032DA98: table.sym_var("pl_collision_8032DA98",  "u8", flag=table.GLOBL|ultra.DALIGN),

    # src/player.c
    0x8032DAA0: table.sym_var("player_8032DAA0",    "s8",   "[][6]",    table.GLOBL),
    0x8032DACC: table.sym_var("player_8032DACC",    "u8",   "[]",       table.GLOBL),
    0x8032DAE0: table.sym_var("player_8032DAE0",    "u64",              flag=table.GLOBL),

    # src/pl_demo.c
    0x8032DB30: table.sym_var("vp_pl_demo",         "Vp",               flag=table.GLOBL),
    0x8032DB40: table.sym_var("pl_demo_staff",      "STAFF *",          flag=table.GLOBL|ultra.DALIGN),
    0x8032DB44: table.sym_var("pl_demo_8032DB44",   "s8",               flag=table.GLOBL|ultra.DALIGN),
    0x8032DB48: table.sym_var("pl_demo_8032DB48",   "s8",               flag=table.GLOBL|ultra.DALIGN),
    0x8032DB4C: table.sym_var("pl_demo_8032DB4C",   "s8", "[]",         table.GLOBL),
    0x8032DB54: table.sym_var("pl_demo_8032DB54",   "u8", "[]",         table.GLOBL),
    0x8032DB5C: table.sym_var("pl_demo_8032DB5C",   "BSPLINE", "[]",    table.GLOBL),
    0x8032DC34: table.sym_var("pl_demo_8032DC34",   "s32",              flag=table.GLOBL|ultra.DALIGN),
    0x8032DC38: table.sym_var("pl_demo_8032DC38",   "s32",              flag=table.GLOBL|ultra.DALIGN),
    0x8032DC3C: table.sym_var("pl_demo_8032DC3C",   "u8", "[]",         table.GLOBL),

    # src/pl_walk.c
    0x8032DC50: table.sym_var("pl_walk_8032DC50", "PL_WALK", flag=table.GLOBL),
    0x8032DC68: table.sym_var("pl_walk_8032DC68", "PL_WALK", flag=table.GLOBL),
    0x8032DC80: table.sym_var("pl_walk_8032DC80", "PL_WALK", flag=table.GLOBL),
    0x8032DC98: table.sym_var("pl_walk_8032DC98", "PL_WALK", flag=table.GLOBL),
    0x8032DCB0: table.sym_var("pl_walk_8032DCB0", "PL_WALK", flag=table.GLOBL),
    0x8032DCC8: table.sym_var("pl_walk_8032DCC8", "PL_WALK", flag=table.GLOBL),
    0x8032DCE0: table.sym_var("pl_walk_8032DCE0", "PL_WALK", flag=table.GLOBL),
    0x8032DCF8: table.sym_var("pl_walk_8032DCF8", "PL_WALK", flag=table.GLOBL),
    0x8032DD10: table.sym_var("pl_walk_8032DD10", "PL_WALK", flag=table.GLOBL),

    # src/pl_swim.c
    0x8032DD30: table.sym_var("pl_swim_8032DD30", "s16",   flag=table.GLOBL|ultra.DALIGN),
    0x8032DD34: table.sym_var("pl_swim_8032DD34", "s16",   flag=table.GLOBL|ultra.DALIGN),
    0x8032DD38: table.sym_var("pl_swim_8032DD38", "s16", "[]", table.GLOBL),

    # src/pl_callback.c
    0x8032DD50: table.sym_var("pl_callback_8032DD50", "s8", "[]",   table.GLOBL),
    0x8032DD58: table.sym_var("pl_callback_8032DD58", "s8", "[]",   table.GLOBL),
    0x8032DD6C: table.sym_var("pl_callback_8032DD6C", "s16",    flag=table.GLOBL|ultra.DALIGN),

    # src/mem.c
    0x8032DD70: table.sym_var("mem",    "MEM *", flag=table.GLOBL|ultra.DALIGN),

    # src/save.c
    0x8032DD80: table.sym_var("save_8032DD80",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032DD84: table.sym_var("save_8032DD84",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032DD88: table.sym_var("save_8032DD88",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032DD8C: table.sym_var("save_8032DD8C",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032DD90: table.sym_var("save_8032DD90",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032DD94: table.sym_var("save_8032DD94",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032DD98: table.sym_var("save_course",    "s8", "[]", table.GLOBL),

    # src/scene.c
    0x8032DDC0: table.sym_var("spawn_mario",        "SPAWN *",  flag=table.GLOBL|ultra.DALIGN),
    0x8032DDC4: table.sym_var("shape_table",        "SHAPE **", flag=table.GLOBL|ultra.DALIGN),
    0x8032DDC8: table.sym_var("scene_table",        "SCENE *",  flag=table.GLOBL|ultra.DALIGN),
    0x8032DDCC: table.sym_var("scene",              "SCENE *",  flag=table.GLOBL|ultra.DALIGN),
    0x8032DDD0: table.sym_var("staff",              "STAFF *",  flag=table.GLOBL|ultra.DALIGN),
    0x8032DDD4: table.sym_var("scene_vp",           "Vp *", flag=table.GLOBL|ultra.DALIGN),
    0x8032DDD8: table.sym_var("scene_sc",           "Vp *", flag=table.GLOBL|ultra.DALIGN),
    0x8032DDDC: table.sym_var("scene_wipe_timer",   "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x8032DDE0: table.sym_var("scene_fill",         "u32",  flag=table.GLOBL|ultra.DALIGN),
    0x8032DDE4: table.sym_var("scene_wipe_fill",    "u32",  flag=table.GLOBL|ultra.DALIGN),
    0x8032DDE8: table.sym_var("scene_wipe_r",       "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032DDEC: table.sym_var("scene_wipe_g",       "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032DDF0: table.sym_var("scene_wipe_b",       "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8032DDF4: table.sym_var("save_index",         "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x8032DDF8: table.sym_var("stage_index",        "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x8032DDFC: table.sym_var("scene_link_o",       "O_SCRIPT *", "[]", table.GLOBL),
    0x8032DE4C: table.sym_var("scene_link_i",       "u8", "[]", table.GLOBL),
    0x8032DE60: table.sym_var("vp_default",         "Vp",   flag=table.GLOBL),

    # src/shape_draw.c
    0x8032DE70: table.sym_var("shape_rendermode_1", "u32", "[2][8]",    table.GLOBL),
    0x8032DEB0: table.sym_var("shape_rendermode_2", "u32", "[2][8]",    table.GLOBL),
    0x8032DEF0: table.sym_var("shape_scene",    "struct shape_scene *",     flag=table.GLOBL|ultra.DALIGN),
    0x8032DEF4: table.sym_var("shape_layer",    "struct shape_layer *",     flag=table.GLOBL|ultra.DALIGN),
    0x8032DEF8: table.sym_var("shape_persp",    "struct shape_persp *",     flag=table.GLOBL|ultra.DALIGN),
    0x8032DEFC: table.sym_var("shape_camera",   "struct shape_camera *",    flag=table.GLOBL|ultra.DALIGN),
    0x8032DF00: table.sym_var("shape_object",   "struct shape_object *",    flag=table.GLOBL|ultra.DALIGN),
    0x8032DF04: table.sym_var("shape_hand",     "struct shape_hand *",      flag=table.GLOBL|ultra.DALIGN),
    0x8032DF08: table.sym_var("shape_timer",    "u16",  flag=table.GLOBL|ultra.DALIGN),

    # src/time.c
    0x8032DF10: table.sym_var("time_mode",      "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x8032DF14: table.sym_var("time_index_a",   "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x8032DF18: table.sym_var("time_index_b",   "s16",  flag=table.GLOBL|ultra.DALIGN),

    # src/camera.c
    0x8032DF20: table.sym_var("camera_8032DF20",    "s32",      flag=table.GLOBL|ultra.DALIGN), # unused
    0x8032DF24: table.sym_var("camera_8032DF24",    "OBJECT *", flag=table.GLOBL|ultra.DALIGN),
    0x8032DF28: table.sym_var("camera_8032DF28",    "s32",      flag=table.GLOBL|ultra.DALIGN),
    0x8032DF2C: table.sym_var("camera_8032DF2C",    "s32",      flag=table.GLOBL|ultra.DALIGN),
    0x8032DF30: table.sym_var("camera_8032DF30",    "OBJECT *", flag=table.GLOBL|ultra.DALIGN),
    0x8032DF34: table.sym_var("camera_8032DF34",    "s16",      flag=table.GLOBL|ultra.DALIGN),
    0x8032DF38: table.sym_var("camera_stagescene",  "s32",      flag=table.GLOBL|ultra.DALIGN),
    0x8032DF3C: table.sym_var("camera_stage_prev",  "s32",      flag=table.GLOBL|ultra.DALIGN),
    0x8032DF40: table.sym_var("camera_8032DF40",    "f32",      flag=table.GLOBL|ultra.DALIGN), # unused
    0x8032DF44: table.sym_var("camera_8032DF44",    "f32",      flag=table.GLOBL|ultra.DALIGN), # unused
    0x8032DF48: table.sym_var("camera_8032DF48",    "f32",      flag=table.GLOBL|ultra.DALIGN), # unused
    0x8032DF4C: table.sym_var("camera_8032DF4C",    "f32",      flag=table.GLOBL|ultra.DALIGN),
    0x8032DF50: table.sym_var("camera_8032DF50",    "u8",       flag=table.GLOBL|ultra.DALIGN),
    0x8032DF54: table.sym_var("camera_8032DF54",    "u8",       flag=table.GLOBL|ultra.DALIGN),
    0x8032DF58: table.sym_var("camera_8032DF58",    "u8",       flag=table.GLOBL|ultra.DALIGN),
    0x8032DF5C: table.sym_var("camera_8032DF5C",    "u8",       flag=table.GLOBL|ultra.DALIGN),
    0x8032DF60: table.sym_var("camera_8032DF60",    "void *",   flag=table.GLOBL|ultra.DALIGN), # type
    0x8032DF64: table.sym_var("camera_8032DF64",    "void *",   flag=table.GLOBL|ultra.DALIGN), # type
    0x8032DF68: table.sym_var("camera_8032DF68",    "s32",      flag=table.GLOBL|ultra.DALIGN), # unused
    0x8032DF6C: table.sym_var("camera_8032DF6C",    "vecf",     flag=table.GLOBL),
    0x8032DF78: table.sym_var("camera_8032DF78",    "vecf",     flag=table.GLOBL), # unused
    0x8032DF84: table.sym_var("camera_8032DF84",    "vecf",     flag=table.GLOBL), # unused
    0x8032DF90: table.sym_var("camera_8032DF90",    "vecf",     flag=table.GLOBL), # unused
    0x8032DF9C: table.sym_var("camera_8032DF9C",    "vecf",     flag=table.GLOBL), # unused
    0x8032DFA8: table.sym_var_fnc("camera_8032DFA8", lst="[]", val="int", arg=(
        "struct camera *",
        "vecf",
        "vecf",
    ), flag=table.GLOBL),
    0x8032DFF0: table.sym_var("camera_8032DFF0",    "vecf", flag=table.GLOBL),
    0x8032DFFC: table.sym_var("camera_8032DFFC",    "vecf", flag=table.GLOBL),
    0x8032E008: table.sym_var("camera_8032E008",    "u16",  "[]",   flag=table.GLOBL), # unused
    0x8032E018: table.sym_var("camera_8032E018",    "u8",   "[]",   flag=table.GLOBL),
    0x8032E020: table.sym_var("campos_bbh_library_test",    "CAMPOS", "[]", flag=table.GLOBL), # unused
    0x8032E050: table.sym_var("campos_bbh_library",         "CAMPOS", "[]", flag=table.GLOBL),
    0x8032E080: table.sym_var("camctl_null",    "CAMCTL", "[]", flag=table.GLOBL), # unused
    0x8032E098: table.sym_var("camctl_sl",      "CAMCTL", "[]", flag=table.GLOBL),
    0x8032E0E0: table.sym_var("camctl_thi",     "CAMCTL", "[]", flag=table.GLOBL),
    0x8032E128: table.sym_var("camctl_hmc",     "CAMCTL", "[]", flag=table.GLOBL),
    0x8032E1D0: table.sym_var("camctl_ssl",     "CAMCTL", "[]", flag=table.GLOBL),
    0x8032E248: table.sym_var("camctl_rr",      "CAMCTL", "[]", flag=table.GLOBL),
    0x8032E338: table.sym_var("camctl_cotmc",   "CAMCTL", "[]", flag=table.GLOBL),
    0x8032E368: table.sym_var("camctl_ccm",     "CAMCTL", "[]", flag=table.GLOBL),
    0x8032E3B0: table.sym_var("camctl_inside",  "CAMCTL", "[]", flag=table.GLOBL),
    0x8032E6F8: table.sym_var("camctl_bbh",     "CAMCTL", "[]", flag=table.GLOBL),
    0x8032ECB0: table.sym_var("camctl_table",   "CAMCTL *", "[]", flag=table.GLOBL),
    0x8032ED50: table.sym_var("campath_8032ED50",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032EE08: table.sym_var("campath_8032EE08",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032EEC0: table.sym_var("campath_8032EEC0",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032EF30: table.sym_var("campath_8032EF30",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032EFA0: table.sym_var("campath_8032EFA0",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032EFF0: table.sym_var("campath_8032EFF0",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032F048: table.sym_var("campath_8032F048",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032F0E8: table.sym_var("campath_8032F0E8",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032F130: table.sym_var("campath_8032F130",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032F178: table.sym_var("campath_8032F178",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032F1B8: table.sym_var("campath_8032F1B8",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032F1F0: table.sym_var("camera_8032F1F0",    "vecf", flag=table.GLOBL),
    0x8032F1FC: table.sym_var("camera_8032F1FC",    "vecf", flag=table.GLOBL),
    0x8032F208: table.sym_var("camera_8032F208",    "vecf", flag=table.GLOBL),
    0x8032F214: table.sym_var("campath_8032F214",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032F32C: table.sym_var("campath_8032F32C",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032F444: table.sym_var("campath_8032F444",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032F48C: table.sym_var("campath_8032F48C",   "CAMPATH", "[]", flag=table.GLOBL),
    0x8032F4D4: table.sym_var("camdemo_8032F4D4",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F534: table.sym_var("camdemo_8032F534",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F544: table.sym_var("camdemo_8032F544",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F554: table.sym_var("camdemo_8032F554",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F564: table.sym_var("camdemo_8032F564",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F56C: table.sym_var("camdemo_8032F56C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F574: table.sym_var("camdemo_8032F574",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F59C: table.sym_var("camdemo_8032F59C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F5C4: table.sym_var("camdemo_8032F5C4",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F5DC: table.sym_var("camdemo_8032F5DC",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F5F4: table.sym_var("camdemo_8032F5F4",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F60C: table.sym_var("camdemo_8032F60C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F624: table.sym_var("camdemo_8032F624",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F634: table.sym_var("camdemo_8032F634",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F63C: table.sym_var("camdemo_8032F63C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F64C: table.sym_var("camdemo_8032F64C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F65C: table.sym_var("camdemo_8032F65C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F674: table.sym_var("camdemo_8032F674",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F69C: table.sym_var("camdemo_8032F69C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F6AC: table.sym_var("camdemo_8032F6AC",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F6BC: table.sym_var("camdemo_8032F6BC",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F6CC: table.sym_var("camdemo_8032F6CC",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F6DC: table.sym_var("camdemo_8032F6DC",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F6F4: table.sym_var("camdemo_8032F6F4",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F6FC: table.sym_var("camdemo_8032F6FC",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F70C: table.sym_var("camdemo_8032F70C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F714: table.sym_var("camdemo_8032F714",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F71C: table.sym_var("camdemo_8032F71C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F72C: table.sym_var("camdemo_8032F72C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F734: table.sym_var("camdemo_8032F734",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F74C: table.sym_var("camdemo_8032F74C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F754: table.sym_var("camdemo_8032F754",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F75C: table.sym_var("camdemo_8032F75C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F764: table.sym_var("camdemo_8032F764",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F76C: table.sym_var("camdemo_8032F76C",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F774: table.sym_var("camdemo_8032F774",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F784: table.sym_var("camdemo_8032F784",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F794: table.sym_var("camdemo_8032F794",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F7A4: table.sym_var("camdemo_8032F7A4",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F7B4: table.sym_var("camdemo_8032F7B4",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F7C4: table.sym_var("camdemo_8032F7C4",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F7D4: table.sym_var("camdemo_8032F7D4",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F7EC: table.sym_var("camdemo_8032F7EC",   "CAMDEMO", "[]", flag=table.GLOBL),
    0x8032F804: table.sym_var("camera_windemo_table",   "u8", "[][4]",  table.GLOBL),
    0x8032F870: table.sym_var("camera_pause_table",     "u8", "[]",     table.GLOBL),
    0x8032F884: table.sym_var("campath_battlefield_eye",    "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032F8AC: table.sym_var("campath_battlefield_look",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032F8D4: table.sym_var("campath_wf1_eye",    "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032F8FC: table.sym_var("campath_wf1_look",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032F924: table.sym_var("campath_jrb1_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032F94C: table.sym_var("campath_jrb1_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032F974: table.sym_var("campath_ccm2_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032F99C: table.sym_var("campath_ccm2_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032F9C4: table.sym_var("campath_bbh1_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032F9E4: table.sym_var("campath_bbh1_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FA04: table.sym_var("campath_hmc1_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FA2C: table.sym_var("campath_hmc1_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FA54: table.sym_var("campath_thi3_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FA6C: table.sym_var("campath_thi3_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FA84: table.sym_var("campath_lll2_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FAB4: table.sym_var("campath_lll2_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FAE4: table.sym_var("campath_ssl1_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FB14: table.sym_var("campath_ssl1_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FB44: table.sym_var("campath_ddd1_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FB7C: table.sym_var("campath_ddd1_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FBB4: table.sym_var("campath_sl1_eye",    "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FBD4: table.sym_var("campath_sl1_look",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FBF4: table.sym_var("campath_wdw1_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FC14: table.sym_var("campath_wdw1_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FC34: table.sym_var("campath_ttm1_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FC64: table.sym_var("campath_ttm1_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FC94: table.sym_var("campath_thi1_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FCCC: table.sym_var("campath_thi1_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FD04: table.sym_var("campath_ttc1_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FD24: table.sym_var("campath_ttc1_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FD44: table.sym_var("campath_rr1_eye",    "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FD64: table.sym_var("campath_rr1_look",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FD84: table.sym_var("campath_sa1_eye",    "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FDAC: table.sym_var("campath_sa1_look",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FDD4: table.sym_var("campath_cotmc1_eye",     "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FDFC: table.sym_var("campath_cotmc1_look",    "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FE24: table.sym_var("campath_ddd2_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FE4C: table.sym_var("campath_ddd2_look",  "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FE74: table.sym_var("campath_ccm1_eye",   "CAMPATH", "[]",   flag=table.GLOBL),
    0x8032FE94: table.sym_var("campath_ccm1_look",  "CAMPATH", "[]",   flag=table.GLOBL),

    # src/object.c
    0x8032FEC0: table.sym_var("object_8032FEC0",    "s8", "[]", table.GLOBL),
    0x8032FECC: table.sym_var("pl_pcl_table",   "PL_PCL", "[]", table.GLOBL),

    # src/obj_lib.c
    0x80330000: table.sym_var("obj_lib_80330000",   "s8",  "[]",    table.GLOBL),
    0x80330004: table.sym_var("obj_lib_80330004",   "s16", "[]",    table.GLOBL),
    0x80330014: table.sym_var("obj_lib_80330014",   "s8",  "[]",    table.GLOBL),

    # src/object_a.c
    0x80330020: table.sym_var("object_a_80330020",  "u32",  "[]",   table.GLOBL),
    0x8033002C: table.sym_var("object_a_8033002C",  "s16",  "[]",   table.GLOBL),
    0x8033006C: table.sym_var("object_a_8033006C",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330074: table.sym_var("object_a_80330074",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330084: table.sym_var("object_a_80330084",  "OBJ_COL", flag=table.GLOBL),
    0x80330094: table.sym_var("object_a_80330094",  "OBJ_PCL", flag=table.GLOBL),
    0x803300A8: table.sym_var("object_a_803300A8",  "u8",   "[]",   table.GLOBL), # unused
    0x803300AC: table.sym_var("object_a_803300AC",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x803300BC: table.sym_var("object_a_803300BC",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x803300E0: table.sym_var("object_a_803300E0",  "OBJ_SFX", "[]",   table.GLOBL),
    0x80330140: table.sym_var("object_a_80330140",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x8033015C: table.sym_var("object_a_8033015C",  "struct object_a_0",    "[]",   table.GLOBL), # unused
    0x80330198: table.sym_var("object_a_80330198",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x803301A8: table.sym_var("object_a_803301A8",  "struct object_a_1",    "[]",   table.GLOBL),
    0x803301C0: table.sym_var("object_a_803301C0",  "OBJ_COL", flag=table.GLOBL),
    0x803301D0: table.sym_var("object_a_803301D0",  "OBJ_PCL", flag=table.GLOBL),
    0x803301E4: table.sym_var("object_a_803301E4",  "OBJ_COL", flag=table.GLOBL),
    0x803301F4: table.sym_var("object_a_803301F4",  "OBJ_COL", flag=table.GLOBL),
    0x80330204: table.sym_var("object_a_80330204",  "s16",  "[][2]",    table.GLOBL),
    0x80330224: table.sym_var("object_a_80330224",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x8033022C: table.sym_var("object_a_8033022C",  "s16",  "[][2]",    table.GLOBL),
    0x80330244: table.sym_var("object_a_80330244",  "s16",  "[][2]",    table.GLOBL),
    0x80330260: table.sym_var("object_a_80330260",  "s32",  "[][2]",    table.GLOBL),
    0x80330288: table.sym_var("object_a_80330288",  "NA_SE",    "[]",   table.GLOBL),
    0x80330290: table.sym_var("object_a_80330290",  "NA_SE",    "[]",   table.GLOBL),
    0x80330298: table.sym_var("object_a_80330298",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x803302AC: table.sym_var("object_a_803302AC",  "struct object_a_2",    "[]",   table.GLOBL),
    0x803302DC: table.sym_var("object_a_803302DC",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x803302EC: table.sym_var("object_a_803302EC",  "s16",  "[][3]",    table.GLOBL),
    0x80330318: table.sym_var("object_a_80330318",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x8033032C: table.sym_var("object_a_8033032C",  "OBJ_PCL", flag=table.GLOBL),
    0x80330340: table.sym_var("object_a_80330340",  "OBJ_PCL", flag=table.GLOBL),
    0x80330354: table.sym_var("object_a_80330354",  "s16",  "[]",   table.GLOBL),
    0x8033035C: table.sym_var("object_a_8033035C",  "OBJ_PCL",   flag=table.GLOBL),
    0x80330370: table.sym_var("object_a_80330370",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330380: table.sym_var("object_a_80330380",  "f32",  "[]",   table.GLOBL),
    0x80330390: table.sym_var("object_a_80330390",  "OBJ_COL", flag=table.GLOBL),
    0x803303A0: table.sym_var("object_a_803303A0",  "OBJ_COL", flag=table.GLOBL),
    0x803303B0: table.sym_var("object_a_803303B0",  "OBJ_COL", flag=table.GLOBL),
    0x803303C0: table.sym_var("object_a_803303C0",  "s16",  "[][2]",    table.GLOBL),
    0x803303E8: table.sym_var("object_a_803303E8",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x803303F8: table.sym_var("object_a_803303F8",  "OBJ_COL",   flag=table.GLOBL),
    0x80330408: table.sym_var("object_a_80330408",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330410: table.sym_var("object_a_80330410",  "OBJ_COL",   flag=table.GLOBL),
    0x80330420: table.sym_var("object_a_80330420",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x8033042C: table.sym_var("object_a_8033042C",  "OBJ_COL",   flag=table.GLOBL),
    0x8033043C: table.sym_var("object_a_8033043C",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330450: table.sym_var("object_a_80330450",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x8033045C: table.sym_var("object_a_8033045C",  "s8",   "[]",   table.GLOBL),
    0x8033046C: table.sym_var("object_a_8033046C",  "s16",  "[]",   table.GLOBL),
    0x80330470: table.sym_var("object_a_80330470",  "s16",  "[]",   table.GLOBL),
    0x80330474: table.sym_var("object_a_80330474",  "s8",   "[]",   table.GLOBL),
    0x80330478: table.sym_var("object_a_80330478",  "s16",  "[]",   table.GLOBL),
    0x80330480: table.sym_var("object_a_80330480",  "s16",  "[][3]",    table.GLOBL),
    0x803304C8: table.sym_var("object_a_803304C8",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330518: table.sym_var("object_a_80330518",  "OBJ_SFX", "[]",   table.GLOBL),
    0x803305F0: table.sym_var("object_a_803305F0",  "s8",   "[]",   table.GLOBL),
    0x803305F4: table.sym_var("object_a_803305F4",  "s8",   "[]",   table.GLOBL),
    0x803305F8: table.sym_var("object_a_803305F8",  "struct object_a_3",    "[]",   table.GLOBL),
    0x8033067C: table.sym_var("object_a_8033067C",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330688: table.sym_var("object_a_80330688",  "OBJ_COL", flag=table.GLOBL),
    0x80330698: table.sym_var("object_a_80330698",  "OBJ_COL", flag=table.GLOBL),
    0x803306A8: table.sym_var("object_a_803306A8",  "f32",  "[]",   table.GLOBL),
    0x803306B4: table.sym_var("object_a_803306B4",  "struct object_a_4",    "[]",   table.GLOBL),
    0x803306DC: table.sym_var("object_a_803306DC",  "PATH_DATA",    "[]",   table.GLOBL),
    0x80330738: table.sym_var("object_a_80330738",  "OBJ_SFX", "[]",   table.GLOBL),
    0x803307A0: table.sym_var("object_a_803307A0",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x803307C0: table.sym_var("object_a_803307C0",  "static s16",   "[]"),
    0x803307F4: table.sym_var("object_a_803307F4",  "static s16",   "[]"),
    0x80330828: table.sym_var("object_a_80330828",  "s16 *",    "[]",   table.GLOBL),
    0x80330830: table.sym_var("object_a_80330830",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330840: table.sym_var("object_a_80330840",  "OBJ_COL", flag=table.GLOBL),
    0x80330850: table.sym_var("object_a_80330850",  "static s8",    "[]"),
    0x80330884: table.sym_var("object_a_80330884",  "static s8",    "[]"),
    0x803308A8: table.sym_var("object_a_803308A8",  "static s8",    "[]"),
    0x803308CC: table.sym_var("object_a_803308CC",  "s8 *", "[]",   table.GLOBL),
    0x803308D8: table.sym_var("object_a_803308D8",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x803308F8: table.sym_var("object_a_803308F8",  "s8",   "[]",   table.GLOBL),
    0x80330900: table.sym_var("object_a_80330900",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330924: table.sym_var("object_a_80330924",  "static s8",    "[]"),
    0x80330940: table.sym_var("object_a_80330940",  "static s8",    "[]"),
    0x8033095C: table.sym_var("object_a_8033095C",  "static s8",    "[]"),
    0x80330978: table.sym_var("object_a_80330978",  "static s8",    "[]"),
    0x80330994: table.sym_var("object_a_80330994",  "static s8",    "[]"),
    0x803309B0: table.sym_var("object_a_803309B0",  "static s8",    "[]"),
    0x803309CC: table.sym_var("object_a_803309CC",  "static s8",    "[]"),
    0x803309E8: table.sym_var("object_a_803309E8",  "static s8",    "[]"),
    0x80330A04: table.sym_var("object_a_80330A04",  "static s8",    "[]"),
    0x80330A20: table.sym_var("object_a_80330A20",  "static s8",    "[]"),
    0x80330A3C: table.sym_var("object_a_80330A3C",  "static s8",    "[]"),
    0x80330A58: table.sym_var("object_a_80330A58",  "static s8",    "[]"),
    0x80330A74: table.sym_var("object_a_80330A74",  "static s8",    "[]"),
    0x80330A90: table.sym_var("object_a_80330A90",  "static s8",    "[]"),
    0x80330AAC: table.sym_var("object_a_80330AAC",  "struct object_a_5",    "[]",   table.GLOBL),
    0x80330B1C: table.sym_var("object_a_80330B1C",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330B38: table.sym_var("object_a_80330B38",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330B44: table.sym_var("object_a_80330B44",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330B5C: table.sym_var("object_a_80330B5C",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330B68: table.sym_var("object_a_80330B68",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330B74: table.sym_var("object_a_80330B74",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330B84: table.sym_var("object_a_80330B84",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330B90: table.sym_var("object_a_80330B90",  "OBJ_COL", flag=table.GLOBL),
    0x80330BA0: table.sym_var("object_a_80330BA0",  "struct object_a_6",    "[]",   flag=table.GLOBL),
    0x80330C20: table.sym_var("object_a_80330C20",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330C38: table.sym_var("object_a_80330C38",  "OBJ_COL", flag=table.GLOBL),
    0x80330C48: table.sym_var("object_a_80330C48",  "struct object_a_7",    "[]",   flag=table.GLOBL),
    0x80330C58: table.sym_var("object_a_80330C58",  "OBJ_COL", flag=table.GLOBL),
    0x80330C68: table.sym_var("object_a_80330C68",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330C74: table.sym_var("object_a_80330C74",  "OBJ_COL", flag=table.GLOBL),
    0x80330C84: table.sym_var("object_a_80330C84",  "s16",  "[][3]",    table.GLOBL),
    0x80330C98: table.sym_var("object_a_80330C98",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330CB0: table.sym_var("object_a_80330CB0",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330CC4: table.sym_var("object_a_80330CC4",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330CD4: table.sym_var("object_a_80330CD4",  "OBJ_COL", flag=table.GLOBL),
    0x80330CE4: table.sym_var("object_a_80330CE4",  "O_CALLBACK *", "[]",   table.GLOBL),
    0x80330D0C: table.sym_var("object_a_80330D0C",  "OBJ_SPLASH", flag=table.GLOBL),
    0x80330D30: table.sym_var("object_a_80330D30",  "OBJ_SPLASH", flag=table.GLOBL),
    0x80330D54: table.sym_var("object_a_80330D54",  "OBJ_SPLASH", flag=table.GLOBL),
    0x80330D78: table.sym_var("object_a_80330D78",  "OBJ_SPLASH", flag=table.GLOBL),
    0x80330D9C: table.sym_var("object_a_80330D9C",  "OBJ_COL", flag=table.GLOBL),
    0x80330DAC: table.sym_var("object_a_80330DAC",  "struct object_a_8",    "[]",   table.GLOBL),

    # src/obj_physics.c
    0x80330E20: table.sym_var("obj_physics_80330E20",   "s16",          flag=table.GLOBL|ultra.DALIGN),
    0x80330E24: table.sym_var("obj_physics_80330E24",   "u32", "[4]",   table.GLOBL), # unused
    0x80330E34: table.sym_var("object_movebg",          "OBJECT *",     flag=table.GLOBL|ultra.DALIGN),

    # src/obj_debug.c
    0x80330E40: table.sym_var("obj_debug_80330E40", "const char *", "[]",   table.GLOBL),
    0x80330E64: table.sym_var("obj_debug_80330E64", "const char *", "[]",   table.GLOBL),
    0x80330E88: table.sym_var("obj_debug_80330E88", "s32",  flag=table.GLOBL|ultra.DALIGN),
    0x80330E8C: table.sym_var("obj_debug_80330E8C", "s32",  flag=table.GLOBL|ultra.DALIGN),
    0x80330E90: table.sym_var("obj_debug_80330E90", "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80330E94: table.sym_var("obj_debug_80330E94", "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80330E98: table.sym_var("obj_debug_80330E98", "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80330E9C: table.sym_var("obj_debug_80330E9C", "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80330EA0: table.sym_var("obj_debug_80330EA0", "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80330EA4: table.sym_var("obj_debug_80330EA4", "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80330EA8: table.sym_var("obj_debug_80330EA8", "s16", "[]",    table.GLOBL),

    # src/wipe.c
    0x80330EC0: table.sym_var("wipe_80330EC0",  "u8",  "[4]",   table.GLOBL),
    0x80330EC4: table.sym_var("wipe_80330EC4",  "u16", "[2]",   table.GLOBL),
    0x80330EC8: table.sym_var("txt_wipe",       "u8 *", "[]",   table.GLOBL),

    # src/shadow.c
    0x80330EE0: table.sym_var("shadow_rect_table",  "SHADOW_RECT", "[]", table.GLOBL),

    # src/background.c
    0x80330F00: table.sym_var("background_table",   "u16 **", "[]", table.GLOBL),
    0x80330F28: table.sym_var("background_shade",   "u8", "[][3]", table.GLOBL),

    # src/scroll.c
    0x80330F30: table.sym_var("scroll_80330F30",    "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x80330F34: table.sym_var("scroll_80330F34",    "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x80330F38: table.sym_var("scroll_80330F38",    "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80330F3C: table.sym_var("scroll_80330F3C",    "f32",  flag=table.GLOBL|ultra.DALIGN),
    0x80330F40: table.sym_var("scroll_80330F40",    "s32",  flag=table.GLOBL|ultra.DALIGN),
    0x80330F44: table.sym_var("txt_scroll",         "u16 *", "[]",    table.GLOBL),
    0x80330F64: table.sym_var("scroll_table_a",     "SCROLL", "[]",  table.GLOBL),
    0x803311A4: table.sym_var("scroll_table_b",     "SCROLL", "[]",  table.GLOBL),
    0x8033127C: table.sym_var("scroll_table_c",     "SCROLL", "[]",  table.GLOBL),
    0x803312E8: table.sym_var("scroll_803312E8",    "s8", "[]",             table.GLOBL), # unused

    # src/obj_shape.c
    0x803312F0: table.sym_var("obj_shape_803312F0", "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x803312F4: table.sym_var("obj_shape_803312F4", "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x803312F8: table.sym_var("obj_shape_803312F8", "s16",  flag=table.GLOBL|ultra.DALIGN),

    # src/ripple.c
    0x80331300: table.sym_var("ripple_80331300",    "void *", "[]",     table.GLOBL), # type
    0x80331308: table.sym_var("ripple_80331308",    "void *", "[]",     table.GLOBL), # type
    0x80331344: table.sym_var("ripple_80331344",    "void *", "[]",     table.GLOBL), # type
    0x8033134C: table.sym_var("ripple_8033134C",    "void **", "[]",    table.GLOBL), # type
    0x80331358: table.sym_var("ripple_80331358",    "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x8033135C: table.sym_var("ripple_8033135C",    "s16",  flag=table.GLOBL|ultra.DALIGN),

    # src/dprint.c
    0x80331360: table.sym_var("dprint_index",   "s16",  flag=table.GLOBL|ultra.DALIGN),

    # src/message.c
    0x80331370: table.sym_var("message_80331370",   "u8", "[0x100]",    table.GLOBL),
    0x80331470: table.sym_var("message_80331470",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80331474: table.sym_var("message_80331474",   "f32",  flag=table.GLOBL|ultra.DALIGN),
    0x80331478: table.sym_var("message_80331478",   "f32",  flag=table.GLOBL|ultra.DALIGN),
    0x8033147C: table.sym_var("message_8033147C",   "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x80331480: table.sym_var("message_80331480",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80331484: table.sym_var("message_80331484",   "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x80331488: table.sym_var("message_80331488",   "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x8033148C: table.sym_var("message_8033148C",   "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x80331490: table.sym_var("message_80331490",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80331494: table.sym_var("message_80331494",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80331498: table.sym_var("message_80331498",   "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8033149C: table.sym_var("message_8033149C",   "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x803314A0: table.sym_var("message_803314A0",   "s32",  flag=table.GLOBL|ultra.DALIGN),
    0x803314A4: table.sym_var("str_803314A4",   "u8", "[][5]",  table.GLOBL), # the / you
    0x803314B0: table.sym_var("str_803314B0",   "u8", "[]",     table.GLOBL), # [+]
    0x803314B4: table.sym_var("str_803314B4",   "u8", "[]",     table.GLOBL), # [x]
    0x803314B8: table.sym_var("str_803314B8",   "u8", "[]",     table.GLOBL), # [*]
    0x803314BC: table.sym_var("str_803314BC",   "u8", "[]",     table.GLOBL), # [x]
    0x803314C0: table.sym_var("str_803314C0",   "u8", "[][5]",  table.GLOBL), # the / you
    0x803314CC: table.sym_var("message_803314CC",   "s16", "[]",    table.GLOBL),
    0x803314D8: table.sym_var("message_803314D8",   "s16", "[]",    table.GLOBL),
    0x803314E0: table.sym_var("message_803314E0",   "s16", "[]",    table.GLOBL),
    0x803314EC: table.sym_var("message_803314EC",   "s16", "[]",    table.GLOBL),
    0x803314F8: table.sym_var("message_803314F8",   "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x803315E4: table.sym_var("str_803315E4",   "u8 *", "[]",   table.GLOBL), # ending subtitle
    0x8033160C: table.sym_var("message_8033160C",   "u16",  flag=table.GLOBL|ultra.DALIGN),
    0x80331610: table.sym_var("message_80331610",   "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x80331614: table.sym_var("message_80331614",   "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x80331618: table.sym_var("message_80331618",   "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x8033161C: table.sym_var("message_8033161C",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80331620: table.sym_var("message_80331620",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80331624: table.sym_var("str_80331624",   "u8", "[]", table.GLOBL), # COURSE
    0x8033162C: table.sym_var("str_8033162C",   "u8", "[]", table.GLOBL), # MY SCORE
    0x80331638: table.sym_var("str_80331638",   "u8", "[]", table.GLOBL), # [*]
    0x8033163C: table.sym_var("str_8033163C",   "u8", "[]", table.GLOBL), # [.]
    0x80331640: table.sym_var("str_80331640",   "u8", "[]", table.GLOBL), # LAKITU <-> MARIO
    0x80331650: table.sym_var("str_80331650",   "u8", "[]", table.GLOBL), # LAKITU <-> STOP
    0x80331660: table.sym_var("str_80331660",   "u8", "[]", table.GLOBL), # (NORMAL)(UP-CLOSE)
    0x80331674: table.sym_var("str_80331674",   "u8", "[]", table.GLOBL), # (NORMAL)(FIXED)
    0x80331684: table.sym_var("str_80331684",   "u8", "[]", table.GLOBL), # CONTINUE
    0x80331690: table.sym_var("str_80331690",   "u8", "[]", table.GLOBL), # EXIT COURSE
    0x8033169C: table.sym_var("str_8033169C",   "u8", "[]", table.GLOBL), # SET CAMERA ANGLE WITH R
    0x803316B4: table.sym_var("str_803316B4",   "u8", "[]", table.GLOBL), # PAUSE
    0x803316BC: table.sym_var("str_803316BC",   "u8", "[]", table.GLOBL), # [*]
    0x803316C0: table.sym_var("str_803316C0",   "u8", "[]", table.GLOBL), # [+][x]
    0x803316C4: table.sym_var("str_803316C4",   "u8", "[]", table.GLOBL), # [*][x]
    0x803316C8: table.sym_var("message_803316C8",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x803316CC: table.sym_var("message_803316CC",   "s32",  flag=table.GLOBL|ultra.DALIGN),
    0x803316D0: table.sym_var("message_803316D0",   "s32",  flag=table.GLOBL|ultra.DALIGN),
    0x803316D4: table.sym_var("message_803316D4",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x803316D8: table.sym_var("str_803316D8",   "u8", "[]", table.GLOBL), # HI SCORE
    0x803316E4: table.sym_var("str_803316E4",   "u8", "[]", table.GLOBL), # CONGRATULATIONS
    0x803316F4: table.sym_var("str_803316F4",   "u8", "[]", table.GLOBL), # [+]
    0x803316F8: table.sym_var("str_803316F8",   "u8", "[]", table.GLOBL), # [x]
    0x803316FC: table.sym_var("str_803316FC",   "u8", "[]", table.GLOBL), # COURSE
    0x80331704: table.sym_var("str_80331704",   "u8", "[]", table.GLOBL), # CATCH
    0x8033170C: table.sym_var("str_8033170C",   "u8", "[]", table.GLOBL), # CLEAR
    0x80331714: table.sym_var("str_80331714",   "u8", "[]", table.GLOBL), # [*]
    0x80331718: table.sym_var("str_80331718",   "u8", "[]", table.GLOBL), # SAVE & CONTINUE
    0x80331728: table.sym_var("str_80331728",   "u8", "[]", table.GLOBL), # SAVE & QUIT
    0x80331734: table.sym_var("str_80331734",   "u8", "[]", table.GLOBL), # CONTINUE, DON'T SAVE

    # src/weather_snow.c
    0x80331750: table.sym_var("weather_snow_80331750",  "s8",           flag=table.GLOBL|ultra.DALIGN),
    0x80331758: table.sym_var("vtx_weather_snow",       "Vtx", "[]",    table.GLOBL),
    0x80331788: table.sym_var("weather_snow_80331788",  "vecs", flag=table.GLOBL),
    0x80331790: table.sym_var("weather_snow_80331790",  "vecs", flag=table.GLOBL),
    0x80331798: table.sym_var("weather_snow_80331798",  "vecs", flag=table.GLOBL),

    # src/weather_lava.c
    0x803317A0: table.sym_var("weather_lava_803317A0",  "s8",           flag=table.GLOBL|ultra.DALIGN),
    0x803317A8: table.sym_var("vtx_weather_lava",       "Vtx", "[]",    table.GLOBL),

    # src/obj_data.c
    0x803317E0: table.sym_var("prg_obj_table",  "PRG_OBJ", "[]", table.GLOBL),
    0x80332350: table.sym_var("map_obj_table",  "MAP_OBJ", "[]", table.GLOBL),

    # src/hud.c
    0x803325F0: table.sym_var("meter",  "METER", flag=table.GLOBL),
    0x803325FC: table.sym_var("hud_803325FC",   "s32",  flag=table.GLOBL|ultra.DALIGN),
    0x80332600: table.sym_var("hud_80332600",   "s16",  flag=table.GLOBL|ultra.DALIGN), # unused
    0x80332604: table.sym_var("hud_80332604",   "s16",  flag=table.GLOBL|ultra.DALIGN), # unused
    0x80332608: table.sym_var("hud_80332608",   "s16",  flag=table.GLOBL|ultra.DALIGN),

    # src/object_b.c
    0x80332610: table.sym_var("object_b_80332610",  "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80332614: table.sym_var("object_b_80332614",  "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x80332618: table.sym_var("object_b_80332618",  "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x8033261C: table.sym_var("object_b_8033261C",  "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80332620: table.sym_var("object_b_80332620",  "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x80332624: table.sym_var("object_b_80332624",  "OBJ_COL", flag=table.GLOBL),
    0x80332634: table.sym_var("object_b_80332634",  "OBJ_COL", flag=table.GLOBL),
    0x80332644: table.sym_var("object_b_80332644",  "OBJ_COL", flag=table.GLOBL),
    0x80332654: table.sym_var("object_b_80332654",  "OBJ_COL", flag=table.GLOBL),
    0x80332664: table.sym_var("object_b_80332664",  "OBJ_COL", flag=table.GLOBL),
    0x80332674: table.sym_var("object_b_80332674",  "OBJ_COL", flag=table.GLOBL),
    0x80332684: table.sym_var("object_b_80332684",  "OBJ_COL", flag=table.GLOBL),
    0x80332694: table.sym_var("object_b_80332694",  "OBJ_COL", flag=table.GLOBL),
    0x803326A4: table.sym_var("object_b_803326A4",  "OBJ_COL", flag=table.GLOBL),
    0x803326B4: table.sym_var("object_b_803326B4",  "OBJ_COL", flag=table.GLOBL),
    0x803326C4: table.sym_var("object_b_803326C4",  "PATH_DATA",    "[]",   table.GLOBL),
    0x80332718: table.sym_var("object_b_80332718",  "PATH_DATA",    "[]",   table.GLOBL),
    0x80332764: table.sym_var("object_b_80332764",  "OBJ_COL", flag=table.GLOBL),
    0x80332774: table.sym_var("object_b_80332774",  "OBJ_COL", flag=table.GLOBL),
    0x80332784: table.sym_var("object_b_80332784",  "OBJ_COL", flag=table.GLOBL),
    0x80332794: table.sym_var("object_b_80332794",  "OBJ_COL", flag=table.GLOBL),
    0x803327A4: table.sym_var("object_b_803327A4",  "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x803327A8: table.sym_var("object_b_803327A8",  "OBJ_COL", flag=table.GLOBL),
    0x803327B8: table.sym_var("object_b_803327B8",  "PATH_DATA",    "[]",   table.GLOBL),
    0x803327FC: table.sym_var("object_b_803327FC",  "OBJ_COL", flag=table.GLOBL),
    0x8033280C: table.sym_var("object_b_8033280C",  "OBJ_COL", flag=table.GLOBL),
    0x8033281C: table.sym_var("object_b_8033281C",  "OBJ_COL", flag=table.GLOBL),
    0x8033282C: table.sym_var("object_b_8033282C",  "s16", "[][2]", table.GLOBL),

    # src/object_c.c
    0x80332840: table.sym_var("object_c_80332840",  "OBJ_COL", flag=table.GLOBL),
    0x80332850: table.sym_var("object_c_80332850",  "u8",   "[6]",  table.GLOBL), # template
    0x80332858: table.sym_var("object_c_80332858",  "u8",   "[6]",  table.GLOBL), # template
    0x80332860: table.sym_var("object_c_80332860",  "struct object_c_0",    "[]",   table.GLOBL),
    0x80332880: table.sym_var("object_c_80332880",  "OBJ_COL", flag=table.GLOBL),
    0x80332890: table.sym_var("object_c_80332890",  "u8",   "[6]",  table.GLOBL), # template
    0x80332898: table.sym_var("object_c_80332898",  "OBJ_COL", flag=table.GLOBL),
    0x803328A8: table.sym_var("object_c_803328A8",  "OBJ_COL", flag=table.GLOBL),
    0x803328B8: table.sym_var("object_c_803328B8",  "s16",  "[]",   table.GLOBL),
    0x803328C0: table.sym_var("object_c_803328C0",  "OBJ_COL", flag=table.GLOBL),
    0x803328D0: table.sym_var("object_c_803328D0",  "struct object_c_1",    "[]",   table.GLOBL),
    0x803328F4: table.sym_var("object_c_803328F4",  "u8",   "[][6]",    table.GLOBL), # template
    0x80332900: table.sym_var("object_c_80332900",  "OBJ_COL", flag=table.GLOBL),
    0x80332910: table.sym_var("object_c_80332910",  "OBJ_COL", flag=table.GLOBL),
    0x80332920: table.sym_var("object_c_80332920",  "OBJ_COL", flag=table.GLOBL),
    0x80332930: table.sym_var("object_c_80332930",  "u8",   "[6]",  table.GLOBL), # template
    0x80332938: table.sym_var("object_c_80332938",  "f32",  "[]",   table.GLOBL),
    0x80332948: table.sym_var("object_c_80332948",  "int",  "[]",   table.GLOBL),
    0x80332954: table.sym_var("object_c_80332954",  "OBJ_COL", flag=table.GLOBL),
    0x80332964: table.sym_var("object_c_80332964",  "u8",   "[6]",  table.GLOBL), # template
    0x8033296C: table.sym_var("object_c_8033296C",  "OBJ_COL", flag=table.GLOBL),
    0x8033297C: table.sym_var("object_c_8033297C",  "s8",   "[]",   table.GLOBL),
    0x80332984: table.sym_var("object_c_80332984",  "OBJ_PCL", flag=table.GLOBL),
    0x80332998: table.sym_var("object_c_80332998",  "OBJ_COL", flag=table.GLOBL),
    0x803329A8: table.sym_var("object_c_803329A8",  "OBJ_COL", flag=table.GLOBL),
    0x803329B8: table.sym_var("object_c_803329B8",  "OBJ_PCL", flag=table.GLOBL),
    0x803329CC: table.sym_var("object_c_803329CC",  "MAP_DATA *", "[]",   table.GLOBL),
    0x803329DC: table.sym_var("object_c_803329DC",  "PATH_DATA *",    "[]",   table.GLOBL),
    0x80332A00: table.sym_var("object_c_80332A00",  "MAP_DATA *", "[]",   table.GLOBL),
    0x80332A20: table.sym_var("object_c_80332A20",  "struct object_c_2",    "[]",   table.GLOBL),
    0x80332A38: table.sym_var("object_c_80332A38",  "OBJ_COL", flag=table.GLOBL),
    0x80332A48: table.sym_var("object_c_80332A48",  "OBJ_PCL", flag=table.GLOBL),
    0x80332A5C: table.sym_var("object_c_80332A5C",  "OBJ_PCL", flag=table.GLOBL),
    0x80332A70: table.sym_var("object_c_80332A70",  "MAP_DATA *", "[]",   table.GLOBL),
    0x80332A78: table.sym_var("object_c_80332A78",  "u8",   "[]",   table.GLOBL),
    0x80332A7C: table.sym_var("object_c_80332A7C",  "f32",  "[]",   table.GLOBL),
    0x80332A8C: table.sym_var("object_c_80332A8C",  "MAP_DATA *", "[]",   table.GLOBL),
    0x80332A94: table.sym_var("object_c_80332A94",  "s16",  "[]",   table.GLOBL),
    0x80332A9C: table.sym_var("object_c_80332A9C",  "s16",  "[]",   table.GLOBL),
    0x80332AA4: table.sym_var("object_c_80332AA4",  "s8",   "[]",   table.GLOBL),
    0x80332AA8: table.sym_var("object_c_80332AA8",  "MAP_DATA *", "[]",   table.GLOBL),
    0x80332AB0: table.sym_var("object_c_80332AB0",  "s8",   "[]",   table.GLOBL),
    0x80332AB4: table.sym_var("object_c_80332AB4",  "s16",  "[]",   table.GLOBL),
    0x80332AB8: table.sym_var("object_c_80332AB8",  "MAP_DATA *", "[]",   table.GLOBL),
    0x80332AC0: table.sym_var("object_c_80332AC0",  "s16",  "[][2][2]", table.GLOBL),
    0x80332AE0: table.sym_var("object_c_80332AE0",  "s8",   "[]",   table.GLOBL),
    0x80332AE4: table.sym_var("object_c_80332AE4",  "s16",  "[]",   table.GLOBL),
    0x80332AE8: table.sym_var("object_c_80332AE8",  "s16",  "[][4]",    table.GLOBL),
    0x80332AF8: table.sym_var("object_c_80332AF8",  "s16",  "[]",   table.GLOBL),
    0x80332B00: table.sym_var("object_c_80332B00",  "OBJ_COL", flag=table.GLOBL),
    0x80332B10: table.sym_var("object_c_80332B10",  "OBJ_PCL", flag=table.GLOBL),
    0x80332B24: table.sym_var("object_c_80332B24",  "OBJ_COL", flag=table.GLOBL),
    0x80332B34: table.sym_var("object_c_80332B34",  "MAP_DATA *", "[]",   table.GLOBL),
    0x80332B54: table.sym_var("object_c_80332B54",  "MAP_DATA *", "[]",   table.GLOBL),
    0x80332B5C: table.sym_var("object_c_80332B5C",  "s16",  "[]",   table.GLOBL),
    0x80332B64: table.sym_var("object_c_80332B64",  "struct object_c_3",    "[][5]",    table.GLOBL),
    0x80332BDC: table.sym_var("object_c_80332BDC",  "s16",  "[]",   table.GLOBL),
    0x80332BE4: table.sym_var("object_c_80332BE4",  "MAP_DATA *", "[]",   table.GLOBL),
    0x80332BF0: table.sym_var("object_c_80332BF0",  "OBJ_COL", flag=table.GLOBL),
    0x80332C00: table.sym_var("object_c_80332C00",  "OBJ_COL", flag=table.GLOBL),
    0x80332C10: table.sym_var("object_c_80332C10",  "OBJ_COL", flag=table.GLOBL),
    0x80332C20: table.sym_var("object_c_80332C20",  "OBJ_COL", flag=table.GLOBL),
    0x80332C30: table.sym_var("object_c_80332C30",  "OBJ_COL", flag=table.GLOBL),
    0x80332C40: table.sym_var("object_c_80332C40",  "s16",  "[][2]",    table.GLOBL),
    0x80332C4C: table.sym_var("object_c_80332C4C",  "OBJ_COL", flag=table.GLOBL),
    0x80332C5C: table.sym_var("object_c_80332C5C",  "OBJ_COL", flag=table.GLOBL),
    0x80332C6C: table.sym_var("object_c_80332C6C",  "f32",  "[]",   table.GLOBL),
    0x80332C74: table.sym_var("object_c_80332C74",  "OBJ_COL", flag=table.GLOBL),
    0x80332C84: table.sym_var("object_c_80332C84",  "OBJ_COL", flag=table.GLOBL),
    0x80332C94: table.sym_var("object_c_80332C94",  "OBJ_COL", flag=table.GLOBL),
    0x80332CA4: table.sym_var("object_c_80332CA4",  "OBJ_COL", flag=table.GLOBL),
    0x80332CB4: table.sym_var("object_c_80332CB4",  "s8",   "[]",   table.GLOBL),
    0x80332CBC: table.sym_var("object_c_80332CBC",  "OBJ_COL", flag=table.GLOBL),
    0x80332CCC: table.sym_var("object_c_80332CCC",  "vecf", "[]",   table.GLOBL),
    0x80332CF0: table.sym_var("object_c_80332CF0",  "u8",   "[6]",  table.GLOBL), # template
    0x80332CF8: table.sym_var("object_c_80332CF8",  "struct object_c_4",    "[]",   table.GLOBL),
    0x80332D10: table.sym_var("object_c_80332D10",  "s16",  "[][2]",    table.GLOBL),
    0x80332D28: table.sym_var("object_c_80332D28",  "OBJ_COL", flag=table.GLOBL),
    0x80332D38: table.sym_var("object_c_80332D38",  "OBJ_COL", flag=table.GLOBL),
    0x80332D48: table.sym_var("object_c_80332D48",  "s16",  "[][2]",    table.GLOBL),
    0x80332D58: table.sym_var("object_c_80332D58",  "vecs", "[]",   table.GLOBL),
    0x80332E14: table.sym_var("object_c_80332E14",  "OBJ_COL", flag=table.GLOBL),
    0x80332E24: table.sym_var("object_c_80332E24",  "struct object_c_5",    "[]",   table.GLOBL),
    0x80332E3C: table.sym_var("object_c_80332E3C",  "OBJ_COL", flag=table.GLOBL),

    # src/audio/g.c
    0x80332E50: table.sym_var("Na_g_80332E50",  "s32",  flag=table.GLOBL|ultra.DALIGN), # rng?
    0x80332E54: table.sym_var("Na_g_80332E54",  "s32",  flag=table.GLOBL|ultra.DALIGN), # tick
    0x80332E58: table.sym_var("Na_msg_se_index",    "u8",       "[]",   table.GLOBL), # (msg len)
    0x80332F04: table.sym_var("Na_msg_se_table",    "NA_SE",    "[15]", table.GLOBL),
    0x80332F40: table.sym_var("Na_g_80332F40",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x80332F44: table.sym_var("Na_g_80332F44",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x80332F48: table.sym_var("bgmctl_bbh",     "static s16", "[]"),
    0x80332F54: table.sym_var("bgmctl_ddd",     "static s16", "[]"),
    0x80332F6C: table.sym_var("bgmctl_jrb",     "static s16", "[]"),
    0x80332F84: table.sym_var("bgmctl_unused",  "unused static s16", "[]"), # unused
    0x80332F88: table.sym_var("bgmctl_wdw",     "static s16", "[]"),
    0x80332F98: table.sym_var("bgmctl_hmc",     "static s16", "[]"),
    0x80332FA8: table.sym_var("bgmctl_38",      "static s16", "[]"),
    0x80332FB8: table.sym_var("bgmctl_null",    "static s16", "[]"),
    0x80332FBC: table.sym_var("Na_g_80332FBC",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x80332FC0: table.sym_var("Na_g_80332FC0",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x80332FC4: table.sym_var("bgmctl_table",   "s16 *", "[]",  table.GLOBL), # (stage len)
    0x80333060: table.sym_var("bgmctl_data",    "BGMCTL", "[]",  flag=table.GLOBL),
    0x803330C0: table.sym_var("Na_g_803330C0",  "u8",   "[][3]",    table.GLOBL), # (stage len)
    0x80333138: table.sym_var("Na_g_80333138",  "u16",  "[]",   table.GLOBL), # (stage len)
    0x80333188: table.sym_var("Na_SEQ_vol",     "u8",   "[]",   table.GLOBL),
    0x803331AC: table.sym_var("Na_g_803331AC",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x803331B0: table.sym_var("Na_g_803331B0",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x803331B4: table.sym_var("Na_g_803331B4",  "u8",   "[]",   table.GLOBL),
    0x803331C0: table.sym_var("Na_g_803331C0",  "u8",   "[]",   table.GLOBL),
    0x803331CC: table.sym_var("Na_g_803331CC",  "u8",   "[]",   table.GLOBL),
    0x803331D8: table.sym_var("Na_g_803331D8",  "u8",   "[]",   table.GLOBL),
    0x803331E4: table.sym_var("Na_g_803331E4",  "u8",   "[]",   table.GLOBL),
    0x803331F0: table.sym_var("Na_0",           "vecf", flag=table.GLOBL),
    0x803331FC: table.sym_var("Na_1",           "vecf", flag=table.GLOBL), # unused
    0x80333208: table.sym_var("Na_g_80333208",  "u8",   "[]",   table.GLOBL),
    0x80333214: table.sym_var("Na_g_80333214",  "u8",   flag=table.GLOBL|ultra.DALIGN), # unused
    0x80333218: table.sym_var("Na_g_80333218",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8033321C: table.sym_var("Na_g_8033321C",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x80333220: table.sym_var("Na_g_80333220",  "u16",  flag=table.GLOBL|ultra.DALIGN),
    0x80333224: table.sym_var("Na_g_80333224",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x80333228: table.sym_var("Na_g_80333228",  "u16",  flag=table.GLOBL|ultra.DALIGN),
    0x8033322C: table.sym_var("Na_g_8033322C",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x80333230: table.sym_var("Na_g_80333230",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x80333234: table.sym_var("Na_g_80333234",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x80333238: table.sym_var("Na_g_80333238",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x8033323C: table.sym_var("Na_g_8033323C",  "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x80333240: table.sym_var("Na_g_80333240",  "NA_SE",    "[]",   table.GLOBL),
    0x80333280: table.sym_var("Na_g_80333280",  "u8",       "[]",   table.GLOBL),
    0x80333290: table.sym_var("Na_g_80333290",  "u8",       "[]",   table.GLOBL),

    # src/audio/data.c
    0x803332A0: table.sym_var("Na_cfg_table",    "NA_CFG", "[]",   table.GLOBL), # 18
    0x80333498: table.sym_var("Na_data_80333498",   "s16",  "[]",   table.GLOBL), # unused
    0x80333598: table.sym_var("Na_data_80333598",   "f32",  "[]",   table.GLOBL),
    0x80333994: table.sym_var("Na_freq_table",      "f32",  "[]",   table.GLOBL),
    0x80333B94: table.sym_var("Na_data_80333B94",   "u8",   "[]",   table.GLOBL),
    0x80333BA4: table.sym_var("Na_data_80333BA4",   "u8",   "[]",   table.GLOBL),
    0x80333BB4: table.sym_var("Na_data_80333BB4",   "s8",   "[]",   table.GLOBL),
    0x80333BC4: table.sym_var("adsr_default",   "s16",  "[]",   table.GLOBL),
    0x80333BD0: table.sym_var("wave_sine",      "static s16", "[]"),
    0x80333C50: table.sym_var("wave_pulse",     "static s16", "[]"),
    0x80333CD0: table.sym_var("wave_triangle",  "static s16", "[]"),
    0x80333D50: table.sym_var("wave_saw",       "static s16", "[]"),
    0x80333DD0: table.sym_var("wave_table",     "s16 *",    "[]",   table.GLOBL),
    0x80333DE0: table.sym_var("Na_data_80333DE0",    "u16",  "[]",   table.GLOBL),
    0x80333DF4: table.sym_var("Na_pan_0",    "f32",  "[]",   table.GLOBL),
    0x80333FF4: table.sym_var("Na_pan_1",    "f32",  "[]",   table.GLOBL),
    0x803341F4: table.sym_var("Na_pan_2",    "f32",  "[]",   table.GLOBL),
    0x803343F4: table.sym_var("Na_pan_3",    "f32",  "[]",   table.GLOBL),
    0x803345F4: table.sym_var("Na_pan_4",    "f32",  "[]",   table.GLOBL),
    0x803347F4: table.sym_var("Na_pan_5",    "f32",  "[]",   table.GLOBL),
    0x803349F4: table.sym_var("Na_pan_6",    "f32",  "[]",   table.GLOBL),
    0x80334BF4: table.sym_var("Na_pan_7",    "f32",  "[]",   table.GLOBL),
    0x80334DF4: table.sym_var("Na_pan_8",    "f32",  "[]",   table.GLOBL),
    0x80334FF4: table.sym_var("Na_tick_rate",        "s16",          flag=table.GLOBL|ultra.DALIGN),
    0x80334FF8: table.sym_var("Na_data_80334FF8",    "s8",           flag=table.GLOBL|ultra.DALIGN),
    0x80334FFC: table.sym_var("Na_heap_size",        "size_t",       flag=table.GLOBL|ultra.DALIGN),
    0x80335000: table.sym_var("Na_data_80335000",    "size_t",       flag=table.GLOBL|ultra.DALIGN),
    0x80335004: table.sym_var("Na_data_80335004",    "volatile s32", flag=table.GLOBL|ultra.DALIGN),
    0x80335008: table.sym_var("Na_data_80335008",    "s8",           flag=table.GLOBL|ultra.DALIGN), # unused

    # ==========================================================================
    # rodata
    # ==========================================================================

    # src/main.c
    0x80335B60: table.sym_var_fnc("main_80335B60", "const", "[]"),

    # src/app.c
    0x80335B80: table.sym_var("str_app_buf", "const char", "[]"),

    # src/audio.c
    0x80335B90: table.sym_var("audio_80335B90", "const float"),

    # src/game.c
    0x80335BA0: table.sym_var("str_01_0", "static const char", "[]"),
    0x80335BB0: table.sym_var("str_01_1", "static const char", "[]"),
    0x80335BC4: table.sym_var("str_02_0", "static const char", "[]"),
    0x80335BDC: table.sym_var("str_02_1", "static const char", "[]"),
    0x80335BF0: table.sym_var("str_02_2", "static const char", "[]"),
    0x80335C00: table.sym_var("str_03_0", "static const char", "[]"),
    0x80335C14: table.sym_var("str_03_1", "static const char", "[]"),
    0x80335C28: table.sym_var("str_03_2", "static const char", "[]"),
    0x80335C3C: table.sym_var("str_04_0", "static const char", "[]"),
    0x80335C4C: table.sym_var("str_04_1", "static const char", "[]"),
    0x80335C5C: table.sym_var("str_04_2", "static const char", "[]"),
    0x80335C6C: table.sym_var("str_04_3", "static const char", "[]"),
    0x80335C7C: table.sym_var("str_05_0", "static const char", "[]"),
    0x80335C90: table.sym_var("str_05_1", "static const char", "[]"),
    0x80335CA8: table.sym_var("str_05_2", "static const char", "[]"),
    0x80335CB8: table.sym_var("str_05_3", "static const char", "[]"),
    0x80335CC8: table.sym_var("str_06_0", "static const char", "[]"),
    0x80335CDC: table.sym_var("str_06_1", "static const char", "[]"),
    0x80335CEC: table.sym_var("str_06_2", "static const char", "[]"),
    0x80335D00: table.sym_var("str_07_0", "static const char", "[]"),
    0x80335D14: table.sym_var("str_07_1", "static const char", "[]"),
    0x80335D20: table.sym_var("str_07_2", "static const char", "[]"),
    0x80335D2C: table.sym_var("str_08_0", "static const char", "[]"),
    0x80335D40: table.sym_var("str_08_1", "static const char", "[]"),
    0x80335D54: table.sym_var("str_08_2", "static const char", "[]"),
    0x80335D64: table.sym_var("str_08_3", "static const char", "[]"),
    0x80335D74: table.sym_var("str_09_0", "static const char", "[]"),
    0x80335D84: table.sym_var("str_09_1", "static const char", "[]"),
    0x80335D90: table.sym_var("str_10_0", "static const char", "[]"),
    0x80335DA0: table.sym_var("str_10_1", "static const char", "[]"),
    0x80335DB4: table.sym_var("str_10_2", "static const char", "[]"),
    0x80335DC4: table.sym_var("str_10_3", "static const char", "[]"),
    0x80335DD4: table.sym_var("str_11_0", "static const char", "[]"),
    0x80335DE4: table.sym_var("str_11_1", "static const char", "[]"),
    0x80335DF8: table.sym_var("str_11_2", "static const char", "[]"),
    0x80335E08: table.sym_var("str_12_0", "static const char", "[]"),
    0x80335E20: table.sym_var("str_12_1", "static const char", "[]"),
    0x80335E30: table.sym_var("str_13_0", "static const char", "[]"),
    0x80335E44: table.sym_var("str_13_1", "static const char", "[]"),
    0x80335E54: table.sym_var("str_13_2", "static const char", "[]"),
    0x80335E68: table.sym_var("str_13_3", "static const char", "[]"),
    0x80335E74: table.sym_var("str_14_0", "static const char", "[]"),
    0x80335E88: table.sym_var("str_14_1", "static const char", "[]"),
    0x80335EA0: table.sym_var("str_15_0", "static const char", "[]"),
    0x80335EB8: table.sym_var("str_15_1", "static const char", "[]"),
    0x80335EC8: table.sym_var("str_15_2", "static const char", "[]"),
    0x80335ED4: table.sym_var("str_16_0", "static const char", "[]"),
    0x80335EE8: table.sym_var("str_16_1", "static const char", "[]"),
    0x80335EF4: table.sym_var("str_16_2", "static const char", "[]"),
    0x80335F00: table.sym_var("str_16_3", "static const char", "[]"),
    0x80335F0C: table.sym_var("str_16_4", "static const char", "[]"),
    0x80335F18: table.sym_var("str_17_0", "static const char", "[]"),
    0x80335F28: table.sym_var("str_17_1", "static const char", "[]"),
    0x80335F34: table.sym_var("str_17_2", "static const char", "[]"),
    0x80335F48: table.sym_var("str_17_3", "static const char", "[]"),
    0x80335F54: table.sym_var("str_18_0", "static const char", "[]"),
    0x80335F68: table.sym_var("str_18_1", "static const char", "[]"),
    0x80335F74: table.sym_var("str_18_2", "static const char", "[]"),
    0x80335F8C: table.sym_var("str_18_3", "static const char", "[]"),
    0x80335FA0: table.sym_var("str_19_0", "static const char", "[]"),
    0x80335FAC: table.sym_var("str_19_1", "static const char", "[]"),
    0x80335FC0: table.sym_var("str_20_0", "static const char", "[]"),
    0x80335FD4: table.sym_var("str_20_1", "static const char", "[]"),
    0x80335FE8: table.sym_var_fnc("game_80335FE8", "const", "[]"),
    0x8033607C: table.sym_var_fnc("game_8033607C", "const", "[]"),
    0x80336118: table.sym_var_fnc("game_80336118", "const", "[]"),
    0x8033617C: table.sym_var_fnc("game_8033617C", "const", "[]"),
    0x80336190: table.sym_var_fnc("game_80336190", "const", "[]"),

    # src/pl_collision.c
    0x803361B0: table.sym_var_fnc("pl_collision_803361B0", "const", "[]"),
    0x80336230: table.sym_var_fnc("pl_collision_80336230", "const", "[]"),
    0x803362F8: table.sym_var_fnc("pl_collision_803362F8", "const", "[]"),
    0x80336410: table.sym_var("pl_collision_80336410", "const float"),
    0x80336414: table.sym_var("pl_collision_80336414", "const float"),
    0x80336418: table.sym_var("pl_collision_80336418", "const float"),

    # src/player.c
    0x80336420: table.sym_var("str_player_ang", "const char", "[]"),
    0x80336428: table.sym_var("str_player_spd", "const char", "[]"),
    0x80336430: table.sym_var("str_player_sta", "const char", "[]"),
    0x80336438: table.sym_var_fnc("player_80336438", "const", "[]"),
    0x80336458: table.sym_var_fnc("player_80336458", "const", "[]"),
    0x803364EC: table.sym_var_fnc("player_803364EC", "const", "[]"),
    0x8033650C: table.sym_var_fnc("player_8033650C", "const", "[]"),
    0x803365A0: table.sym_var("player_803365A0", "const float"),
    0x803365A4: table.sym_var("player_803365A4", "const float"),
    0x803365A8: table.sym_var("player_803365A8", "const float"),
    0x803365AC: table.sym_var("player_803365AC", "const float"),
    0x803365B0: table.sym_var("player_803365B0", "const float"),
    0x803365B4: table.sym_var("player_803365B4", "const float"),
    0x803365B8: table.sym_var("player_803365B8", "const float"),
    0x803365BC: table.sym_var("player_803365BC", "const float"),
    0x803365C0: table.sym_var("player_803365C0", "const float"),
    0x803365C4: table.sym_var("player_803365C4", "const float"),
    0x803365C8: table.sym_var("player_803365C8", "const float"),
    0x803365CC: table.sym_var("player_803365CC", "const float"),
    0x803365D0: table.sym_var("player_803365D0", "const float"),
    0x803365D4: table.sym_var_fnc("player_803365D4", "const", "[]"),
    0x80336658: table.sym_var("player_80336658", "const float"),
    0x8033665C: table.sym_var("player_8033665C", "const float"),
    0x80336660: table.sym_var("player_80336660", "const float"),
    0x80336664: table.sym_var("player_80336664", "const float"),
    0x80336668: table.sym_var("player_80336668", "const float"),

    # src/pl_physics.c
    0x80336670: table.sym_var("pl_physics_80336670", "const float"),
    0x80336674: table.sym_var("pl_physics_80336674", "const float"),
    0x80336678: table.sym_var_fnc("pl_physics_80336678", "const", "[]"),
    0x803366AC: table.sym_var("pl_physics_803366AC", "const float"),
    0x803366B0: table.sym_var("pl_physics_803366B0", "const float"),
    0x803366B4: table.sym_var("pl_physics_803366B4", "const float"),
    0x803366B8: table.sym_var("pl_physics_803366B8", "const float"),
    0x803366BC: table.sym_var("pl_physics_803366BC", "const float"),
    0x803366C0: table.sym_var("pl_physics_803366C0", "const float"),

    # src/pl_demo.c
    0x803366D0: table.sym_var("pl_demo_803366D0", "const float"),
    0x803366D4: table.sym_var_fnc("pl_demo_803366D4", "const", "[]"),
    0x803366E8: table.sym_var("pl_demo_803366E8", "const float"),
    0x803366EC: table.sym_var_fnc("pl_demo_803366EC", "const", "[]"),
    0x80336708: table.sym_var("pl_demo_80336708", "const float"),
    0x8033670C: table.sym_var("pl_demo_8033670C", "const float"),
    0x80336710: table.sym_var("pl_demo_80336710", "const float"),
    0x80336714: table.sym_var("pl_demo_80336714", "const float"),
    0x80336718: table.sym_var("pl_demo_80336718", "const float"),
    0x8033671C: table.sym_var("pl_demo_8033671C", "const float"),
    0x80336720: table.sym_var_fnc("pl_demo_80336720", "const", "[]"),
    0x80336754: table.sym_var_fnc("pl_demo_80336754", "const", "[]"),
    0x80336770: table.sym_var_fnc("pl_demo_80336770", "const", "[]"),
    0x80336784: table.sym_var_fnc("pl_demo_80336784", "const", "[]"),
    0x80336848: table.sym_var_fnc("pl_demo_80336848", "const", "[]"),

    # src/pl_hang.c
    0x80336940: table.sym_var("pl_hang_80336940", "const float"),
    0x80336944: table.sym_var("pl_hang_80336944", "const float"),
    0x80336948: table.sym_var("pl_hang_80336948", "const float"),
    0x8033694C: table.sym_var("pl_hang_8033694C", "const float"),
    0x80336950: table.sym_var_fnc("pl_hang_80336950", "const", "[]"),

    # src/pl_wait.c
    0x80336970: table.sym_var("pl_wait_80336970", "const float"),
    0x80336974: table.sym_var("pl_wait_80336974", "const float"),
    0x80336978: table.sym_var_fnc("pl_wait_80336978", "const", "[]"),
    0x803369A4: table.sym_var_fnc("pl_wait_803369A4", "const", "[]"),
    0x803369B8: table.sym_var_fnc("pl_wait_803369B8", "const", "[]"),
    0x80336A18: table.sym_var_fnc("pl_wait_80336A18", "const", "[]"),

    # src/pl_walk.c
    0x80336A80: table.sym_var("pl_walk_80336A80", "const float"),
    0x80336A84: table.sym_var("pl_walk_80336A84", "const float"),
    0x80336A88: table.sym_var("pl_walk_80336A88", "const float"),
    0x80336A8C: table.sym_var("pl_walk_80336A8C", "const float"),
    0x80336A90: table.sym_var("pl_walk_80336A90", "const float"),
    0x80336A94: table.sym_var("pl_walk_80336A94", "const float"),
    0x80336A98: table.sym_var("pl_walk_80336A98", "const float"),
    0x80336A9C: table.sym_var("pl_walk_80336A9C", "const float"),
    0x80336AA0: table.sym_var("pl_walk_80336AA0", "const float"),
    0x80336AA4: table.sym_var("pl_walk_80336AA4", "const float"),
    0x80336AA8: table.sym_var("pl_walk_80336AA8", "const float"),
    0x80336AAC: table.sym_var("pl_walk_80336AAC", "const float"),
    0x80336AB0: table.sym_var("pl_walk_80336AB0", "const float"),
    0x80336AB4: table.sym_var("pl_walk_80336AB4", "const float"),
    0x80336AB8: table.sym_var("pl_walk_80336AB8", "const float"),
    0x80336ABC: table.sym_var("pl_walk_80336ABC", "const float"),
    0x80336AC0: table.sym_var("pl_walk_80336AC0", "const float"),
    0x80336AC4: table.sym_var("pl_walk_80336AC4", "const float"),
    0x80336AC8: table.sym_var("pl_walk_80336AC8", "const float"),
    0x80336ACC: table.sym_var("pl_walk_80336ACC", "const float"),
    0x80336AD0: table.sym_var("pl_walk_80336AD0", "const float"),
    0x80336AD4: table.sym_var("pl_walk_80336AD4", "const float"),
    0x80336AD8: table.sym_var("pl_walk_80336AD8", "const float"),
    0x80336ADC: table.sym_var("pl_walk_80336ADC", "const float"),
    0x80336AE0: table.sym_var("pl_walk_80336AE0", "const float"),
    0x80336AE4: table.sym_var("pl_walk_80336AE4", "const float"),
    0x80336AE8: table.sym_var("pl_walk_80336AE8", "const float"),
    0x80336AEC: table.sym_var("pl_walk_80336AEC", "const float"),
    0x80336AF0: table.sym_var("pl_walk_80336AF0", "const float"),
    0x80336AF8: table.sym_var("pl_walk_80336AF8", "const double"),
    0x80336B00: table.sym_var("pl_walk_80336B00", "const float"),
    0x80336B04: table.sym_var("pl_walk_80336B04", "const float"),
    0x80336B08: table.sym_var("pl_walk_80336B08", "const float"),
    0x80336B0C: table.sym_var_fnc("pl_walk_80336B0C", "const", "[]"),
    0x80336B38: table.sym_var_fnc("pl_walk_80336B38", "const", "[]"),
    0x80336BB4: table.sym_var_fnc("pl_walk_80336BB4", "const", "[]"),
    0x80336BCC: table.sym_var_fnc("pl_walk_80336BCC", "const", "[]"),

    # src/pl_jump.c
    0x80336C00: table.sym_var("pl_jump_80336C00", "const float"),
    0x80336C04: table.sym_var("pl_jump_80336C04", "const float"),
    0x80336C08: table.sym_var("pl_jump_80336C08", "const float"),
    0x80336C0C: table.sym_var("pl_jump_80336C0C", "const float"),
    0x80336C10: table.sym_var("pl_jump_80336C10", "const float"),
    0x80336C14: table.sym_var("pl_jump_80336C14", "const float"),
    0x80336C18: table.sym_var("pl_jump_80336C18", "const float"),
    0x80336C1C: table.sym_var_fnc("pl_jump_80336C1C", "const", "[]"),
    0x80336C38: table.sym_var("pl_jump_80336C38", "const float"),
    0x80336C3C: table.sym_var("pl_jump_80336C3C", "const float"),
    0x80336C40: table.sym_var("pl_jump_80336C40", "const float"),
    0x80336C44: table.sym_var("pl_jump_80336C44", "const float"),
    0x80336C48: table.sym_var("pl_jump_80336C48", "const float"),
    0x80336C4C: table.sym_var("pl_jump_80336C4C", "const float"),
    0x80336C50: table.sym_var("pl_jump_80336C50", "const float"),
    0x80336C54: table.sym_var("pl_jump_80336C54", "const float"),
    0x80336C58: table.sym_var("pl_jump_80336C58", "const double"),
    0x80336C60: table.sym_var_fnc("pl_jump_80336C60", "const", "[]"),
    0x80336D20: table.sym_var_fnc("pl_jump_80336D20", "const", "[]"),
    0x80336D5C: table.sym_var_fnc("pl_jump_80336D5C", "const", "[]"),

    # src/pl_swim.c
    0x80336E10: table.sym_var("pl_swim_80336E10", "const float"),
    0x80336E14: table.sym_var_fnc("pl_swim_80336E14", "const", "[]"),
    0x80336E2C: table.sym_var_fnc("pl_swim_80336E2C", "const", "[]"),
    0x80336E44: table.sym_var("pl_swim_80336E44", "const float"),
    0x80336E48: table.sym_var("pl_swim_80336E48", "const float"),
    0x80336E4C: table.sym_var("pl_swim_80336E4C", "const float"),
    0x80336E50: table.sym_var("pl_swim_80336E50", "const float"),
    0x80336E54: table.sym_var("pl_swim_80336E54", "const float"),
    0x80336E58: table.sym_var("pl_swim_80336E58", "const float"),
    0x80336E5C: table.sym_var_fnc("pl_swim_80336E5C", "const", "[]"),
    0x80336EA4: table.sym_var_fnc("pl_swim_80336EA4", "const", "[]"),

    # src/pl_grab.c
    0x80336ED0: table.sym_var_fnc("pl_grab_80336ED0", "const", "[]"),
    0x80336EF8: table.sym_var_fnc("pl_grab_80336EF8", "const", "[]"),

    # src/pl_callback.c
    0x80336F40: table.sym_var_fnc("pl_callback_80336F40", "const", "[]"),
    0x80336F54: table.sym_var("pl_callback_80336F54", "const float"),
    0x80336F58: table.sym_var("pl_callback_80336F58", "const float"),
    0x80336F60: table.sym_var("pl_callback_80336F60", "const double"),
    0x80336F68: table.sym_var("pl_callback_80336F68", "const double"),

    # src/scene.c
    0x80336F70: table.sym_var("str_scene_no_controller",  "const char", "[]"),
    0x80336F80: table.sym_var("str_scene_press",          "const char", "[]"),
    0x80336F88: table.sym_var("str_scene_start",          "const char", "[]"),

    # src/shape_draw.c
    0x80336F90: table.sym_var("str_shape_draw_mem", "const char", "[]"),
    0x80336F98: table.sym_var("shape_draw_80336F98", "const float"),
    0x80336F9C: table.sym_var_fnc("shape_draw_80336F9C", "const", "[]"),
    0x8033704C: table.sym_var_fnc("shape_draw_8033704C", "const", "[]"),

    # src/camera.c
    0x803370F0: table.sym_var_fnc("camera_803370F0", "const", "[]"),
    0x80337118: table.sym_var("camera_80337118", "const float"),
    0x8033711C: table.sym_var("camera_8033711C", "const float"),
    0x80337120: table.sym_var_fnc("camera_80337120", "const", "[]"),
    0x80337148: table.sym_var("camera_80337148", "const float"),
    0x8033714C: table.sym_var("camera_8033714C", "const float"),
    0x80337150: table.sym_var("camera_80337150", "const float"),
    0x80337154: table.sym_var("camera_80337154", "const float"),
    0x80337158: table.sym_var("camera_80337158", "const float"),
    0x8033715C: table.sym_var("camera_8033715C", "const float"),
    0x80337160: table.sym_var("camera_80337160", "const float"),
    0x80337164: table.sym_var("camera_80337164", "const float"),
    0x80337168: table.sym_var("camera_80337168", "const float"),
    0x8033716C: table.sym_var("camera_8033716C", "const float"),
    0x80337170: table.sym_var("camera_80337170", "const float"),
    0x80337174: table.sym_var("camera_80337174", "const float"),
    0x80337178: table.sym_var("camera_80337178", "const float"),
    0x8033717C: table.sym_var("camera_8033717C", "const float"),
    0x80337180: table.sym_var("camera_80337180", "const float"),
    0x80337184: table.sym_var("camera_80337184", "const float"),
    0x80337188: table.sym_var("camera_80337188", "const float"),
    0x8033718C: table.sym_var("camera_8033718C", "const float"),
    0x80337190: table.sym_var("camera_80337190", "const float"),
    0x80337194: table.sym_var("camera_80337194", "const float"),
    0x80337198: table.sym_var("camera_80337198", "const float"),
    0x8033719C: table.sym_var("camera_8033719C", "const float"),
    0x803371A0: table.sym_var("camera_803371A0", "const float"),
    0x803371A4: table.sym_var("camera_803371A4", "const float"),
    0x803371A8: table.sym_var("camera_803371A8", "const float"),
    0x803371AC: table.sym_var("camera_803371AC", "const float"),
    0x803371B0: table.sym_var("camera_803371B0", "const float"),
    0x803371B4: table.sym_var("camera_803371B4", "const float"),
    0x803371B8: table.sym_var("camera_803371B8", "const float"),
    0x803371BC: table.sym_var("camera_803371BC", "const float"),
    0x803371C0: table.sym_var("camera_803371C0", "const float"),
    0x803371C4: table.sym_var("camera_803371C4", "const float"),
    0x803371C8: table.sym_var("camera_803371C8", "const float"),
    0x803371CC: table.sym_var("camera_803371CC", "const float"),
    0x803371D0: table.sym_var("camera_803371D0", "const float"),
    0x803371D4: table.sym_var("camera_803371D4", "const float"),
    0x803371D8: table.sym_var("camera_803371D8", "const float"),
    0x803371DC: table.sym_var("camera_803371DC", "const float"),
    0x803371E0: table.sym_var("camera_803371E0", "const float"),
    0x803371E4: table.sym_var("camera_803371E4", "const float"),
    0x803371E8: table.sym_var("camera_803371E8", "const float"),
    0x803371EC: table.sym_var("camera_803371EC", "const float"),
    0x803371F0: table.sym_var("camera_803371F0", "const float"),
    0x803371F4: table.sym_var("camera_803371F4", "const float"),
    0x803371F8: table.sym_var("camera_803371F8", "const float"),
    0x803371FC: table.sym_var("camera_803371FC", "const float"),
    0x80337200: table.sym_var("camera_80337200", "const float"),
    0x80337204: table.sym_var("camera_80337204", "const float"),
    0x80337208: table.sym_var("camera_80337208", "const float"),
    0x8033720C: table.sym_var("camera_8033720C", "const float"),
    0x80337210: table.sym_var("camera_80337210", "const float"),
    0x80337214: table.sym_var("camera_80337214", "const float"),
    0x80337218: table.sym_var_fnc("camera_80337218", "const", "[]"),
    0x8033725C: table.sym_var("camera_8033725C", "const float"),
    0x80337260: table.sym_var("camera_80337260", "const float"),
    0x80337264: table.sym_var("camera_80337264", "const float"),
    0x80337268: table.sym_var("camera_80337268", "const float"),
    0x8033726C: table.sym_var_fnc("camera_8033726C", "const", "[]"),
    0x803372E0: table.sym_var("camera_803372E0", "const float"),
    0x803372E4: table.sym_var("camera_803372E4", "const float"),
    0x803372E8: table.sym_var("camera_803372E8", "const float"),
    0x803372EC: table.sym_var("camera_803372EC", "const float"),
    0x803372F0: table.sym_var("camera_803372F0", "const float"),
    0x803372F4: table.sym_var("camera_803372F4", "const float"),
    0x803372F8: table.sym_var("camera_803372F8", "const float"),
    0x803372FC: table.sym_var("camera_803372FC", "const float"),
    0x80337300: table.sym_var("camera_80337300", "const float"),
    0x80337304: table.sym_var_fnc("camera_80337304", "const", "[]"),
    0x8033731C: table.sym_var("camera_8033731C", "const float"),
    0x80337320: table.sym_var("camera_80337320", "const float"),
    0x80337324: table.sym_var("camera_80337324", "const float"),
    0x80337328: table.sym_var("camera_80337328", "const float"),
    0x8033732C: table.sym_var("camera_8033732C", "const float"),
    0x80337330: table.sym_var("camera_80337330", "const float"),
    0x80337334: table.sym_var("camera_80337334", "const float"),
    0x80337338: table.sym_var("camera_80337338", "const float"),
    0x8033733C: table.sym_var_fnc("camera_8033733C", "const", "[]"),
    0x80337354: table.sym_var_fnc("camera_80337354", "const", "[]"),
    0x80337368: table.sym_var("camera_80337368", "const float"),
    0x8033736C: table.sym_var("camera_8033736C", "const float"),
    0x80337370: table.sym_var("camera_80337370", "const float"),
    0x80337374: table.sym_var("camera_80337374", "const float"),
    0x80337378: table.sym_var("camera_80337378", "const float"),
    0x8033737C: table.sym_var("camera_8033737C", "const float"),
    0x80337380: table.sym_var("camera_80337380", "const float"),
    0x80337384: table.sym_var("camera_80337384", "const float"),
    0x80337388: table.sym_var("camera_80337388", "const float"),
    0x8033738C: table.sym_var("camera_8033738C", "const float"),
    0x80337390: table.sym_var("camera_80337390", "const float"),
    0x80337394: table.sym_var("camera_80337394", "const float"),
    0x80337398: table.sym_var("camera_80337398", "const float"),
    0x8033739C: table.sym_var("camera_8033739C", "const float"),
    0x803373A0: table.sym_var("camera_803373A0", "const float"),
    0x803373A4: table.sym_var("camera_803373A4", "const float"),
    0x803373A8: table.sym_var("camera_803373A8", "const float"),
    0x803373AC: table.sym_var("camera_803373AC", "const float"),
    0x803373B0: table.sym_var("camera_803373B0", "const float"),
    0x803373B4: table.sym_var("camera_803373B4", "const float"),
    0x803373B8: table.sym_var("camera_803373B8", "const float"),
    0x803373BC: table.sym_var("camera_803373BC", "const float"),
    0x803373C0: table.sym_var("camera_803373C0", "const float"),
    0x803373C4: table.sym_var("camera_803373C4", "const float"),
    0x803373C8: table.sym_var("camera_803373C8", "const float"),
    0x803373CC: table.sym_var("camera_803373CC", "const float"),
    0x803373D0: table.sym_var("camera_803373D0", "const float"),
    0x803373D4: table.sym_var("camera_803373D4", "const float"),
    0x803373D8: table.sym_var("camera_803373D8", "const float"),
    0x803373DC: table.sym_var("camera_803373DC", "const float"),
    0x803373E0: table.sym_var("camera_803373E0", "const float"),
    0x803373E4: table.sym_var("camera_803373E4", "const float"),
    0x803373E8: table.sym_var("camera_803373E8", "const float"),
    0x803373EC: table.sym_var("camera_803373EC", "const float"),
    0x803373F0: table.sym_var("camera_803373F0", "const float"),
    0x803373F4: table.sym_var("camera_803373F4", "const float"),
    0x803373F8: table.sym_var("camera_803373F8", "const float"),
    0x803373FC: table.sym_var("camera_803373FC", "const float"),
    0x80337400: table.sym_var("camera_80337400", "const float"),
    0x80337404: table.sym_var("camera_80337404", "const float"),
    0x80337408: table.sym_var("camera_80337408", "const float"),
    0x8033740C: table.sym_var("camera_8033740C", "const float"),
    0x80337410: table.sym_var("camera_80337410", "const float"),
    0x80337414: table.sym_var("camera_80337414", "const float"),
    0x80337418: table.sym_var("camera_80337418", "const float"),
    0x8033741C: table.sym_var("camera_8033741C", "const float"),
    0x80337420: table.sym_var("camera_80337420", "const float"),
    0x80337424: table.sym_var("camera_80337424", "const float"),
    0x80337428: table.sym_var("camera_80337428", "const float"),
    0x8033742C: table.sym_var("camera_8033742C", "const float"),
    0x80337430: table.sym_var("camera_80337430", "const float"),
    0x80337434: table.sym_var("camera_80337434", "const float"),
    0x80337438: table.sym_var("camera_80337438", "const float"),
    0x8033743C: table.sym_var("camera_8033743C", "const float"),
    0x80337440: table.sym_var_fnc("camera_80337440", "const", "[]"),
    0x80337644: table.sym_var("camera_80337644", "const float"),
    0x80337648: table.sym_var("camera_80337648", "const float"),
    0x8033764C: table.sym_var("camera_8033764C", "const float"),
    0x80337650: table.sym_var("camera_80337650", "const float"),
    0x80337654: table.sym_var("camera_80337654", "const float"),
    0x80337658: table.sym_var("camera_80337658", "const float"),
    0x8033765C: table.sym_var("camera_8033765C", "const float"),
    0x80337660: table.sym_var("camera_80337660", "const float"),
    0x80337664: table.sym_var("camera_80337664", "const float"),
    0x80337668: table.sym_var_fnc("camera_80337668", "const", "[]"),
    0x80337738: table.sym_var_fnc("camera_80337738", "const", "[]"),
    0x8033776C: table.sym_var("camera_8033776C", "const float"),
    0x80337770: table.sym_var("camera_80337770", "const float"),
    0x80337774: table.sym_var("camera_80337774", "const float"),
    0x80337778: table.sym_var("camera_80337778", "const float"),
    0x8033777C: table.sym_var("camera_8033777C", "const float"),
    0x80337780: table.sym_var_fnc("camera_80337780", "const", "[]"),

    # src/object.c
    0x803377A0: table.sym_var("object_803377A0", "const double"),
    0x803377A8: table.sym_var("object_803377A8", "const double"),

    # src/obj_lib.c
    0x803377B0: table.sym_var("str_obj_lib_areainfo", "const char", "[]"),
    0x803377BC: table.sym_var("obj_lib_803377BC", "const float"),
    0x803377C0: table.sym_var("obj_lib_803377C0", "const float"),
    0x803377C4: table.sym_var("obj_lib_803377C4", "const float"),
    0x803377C8: table.sym_var("obj_lib_803377C8", "const float"),
    0x803377CC: table.sym_var("obj_lib_803377CC", "const float"),
    0x803377D0: table.sym_var("obj_lib_803377D0", "const float"),
    0x803377D8: table.sym_var("obj_lib_803377D8", "const double"),
    0x803377E0: table.sym_var("obj_lib_803377E0", "const double"),
    0x803377E8: table.sym_var("obj_lib_803377E8", "const double"),
    0x803377F0: table.sym_var("obj_lib_803377F0", "const float"),
    0x803377F4: table.sym_var("obj_lib_803377F4", "const float"),
    0x803377F8: table.sym_var("obj_lib_803377F8", "const double"),
    0x80337800: table.sym_var("obj_lib_80337800", "const float"),
    0x80337808: table.sym_var("obj_lib_80337808", "const double"),
    0x80337810: table.sym_var("obj_lib_80337810", "const float"),
    0x80337814: table.sym_var("obj_lib_80337814", "const float"),
    0x80337818: table.sym_var("obj_lib_80337818", "const float"),
    0x8033781C: table.sym_var("obj_lib_8033781C", "const float"),
    0x80337820: table.sym_var("obj_lib_80337820", "const float"),
    0x80337824: table.sym_var("obj_lib_80337824", "const float"),
    0x80337828: table.sym_var("obj_lib_80337828", "const float"),
    0x8033782C: table.sym_var("obj_lib_8033782C", "const float"),
    0x80337830: table.sym_var("obj_lib_80337830", "const float"),
    0x80337834: table.sym_var_fnc("obj_lib_80337834", "const", "[]"),

    # src/object_a.c
    0x80337850: table.sym_var("str_object_a_0_fmt",      "const char", "[]"),
    0x80337854: table.sym_var("str_object_a_0_fg",       "const char", "[]"),
    0x8033785C: table.sym_var("str_object_a_0_sp",       "const char", "[]"),
    0x80337864: table.sym_var("str_object_a_1_fmt",      "const char", "[]"),
    0x80337868: table.sym_var("str_object_a_1_md",       "const char", "[]"),
    0x80337870: table.sym_var("str_object_a_1_sp",       "const char", "[]"),
    0x80337878: table.sym_var("str_object_a_mode",      "const char", "[]"),
    0x80337884: table.sym_var("str_object_a_action",    "const char", "[]"),
    0x80337890: table.sym_var("str_object_a_number",    "const char", "[]"),
    0x8033789C: table.sym_var("str_object_a_off",       "const char", "[]"),
    0x803378A4: table.sym_var("str_object_a_x",         "const char", "[]"),
    0x803378AC: table.sym_var("str_object_a_z",         "const char", "[]"),
    0x803378B4: table.sym_var_fnc("object_a_803378B4", "const", "[]"),
    0x803378C8: table.sym_var("object_a_803378C8", "const double"),
    0x803378D0: table.sym_var("object_a_803378D0", "const double"),
    0x803378D8: table.sym_var("object_a_803378D8", "const double"),
    0x803378E0: table.sym_var("object_a_803378E0", "const float"),
    0x803378E8: table.sym_var("object_a_803378E8", "const double"),
    0x803378F0: table.sym_var("object_a_803378F0", "const float"),
    0x803378F4: table.sym_var("object_a_803378F4", "const float"),
    0x803378F8: table.sym_var("object_a_803378F8", "const float"),
    0x803378FC: table.sym_var("object_a_803378FC", "const float"),
    0x80337900: table.sym_var("object_a_80337900", "const float"),
    0x80337904: table.sym_var_fnc("object_a_80337904", "const", "[]"),
    0x80337918: table.sym_var("object_a_80337918", "const float"),
    0x80337920: table.sym_var("object_a_80337920", "const double"),
    0x80337928: table.sym_var("object_a_80337928", "const double"),
    0x80337930: table.sym_var("object_a_80337930", "const double"),
    0x80337938: table.sym_var("object_a_80337938", "const double"),
    0x80337940: table.sym_var("object_a_80337940", "const float"),
    0x80337944: table.sym_var("object_a_80337944", "const float"),
    0x80337948: table.sym_var("object_a_80337948", "const float"),
    0x8033794C: table.sym_var("object_a_8033794C", "const float"),
    0x80337950: table.sym_var("object_a_80337950", "const double"),
    0x80337958: table.sym_var("object_a_80337958", "const double"),
    0x80337960: table.sym_var("object_a_80337960", "const float"),
    0x80337968: table.sym_var("object_a_80337968", "const double"),
    0x80337970: table.sym_var("object_a_80337970", "const float"),
    0x80337974: table.sym_var_fnc("object_a_80337974", "const", "[]"),
    0x80337988: table.sym_var("object_a_80337988", "const double"),
    0x80337990: table.sym_var("object_a_80337990", "const float"),
    0x80337994: table.sym_var("object_a_80337994", "const float"),
    0x80337998: table.sym_var("object_a_80337998", "const float"),
    0x8033799C: table.sym_var("object_a_8033799C", "const float"),
    0x803379A0: table.sym_var("object_a_803379A0", "const float"),
    0x803379A4: table.sym_var("object_a_803379A4", "const float"),
    0x803379A8: table.sym_var("object_a_803379A8", "const float"),
    0x803379AC: table.sym_var("object_a_803379AC", "const float"),
    0x803379B0: table.sym_var("object_a_803379B0", "const float"),
    0x803379B4: table.sym_var_fnc("object_a_803379B4", "const", "[]"),
    0x803379C8: table.sym_var("object_a_803379C8", "const float"),
    0x803379D0: table.sym_var("object_a_803379D0", "const double"),
    0x803379D8: table.sym_var("object_a_803379D8", "const float"),
    0x803379E0: table.sym_var("object_a_803379E0", "const double"),
    0x803379E8: table.sym_var("object_a_803379E8", "const double"),
    0x803379F0: table.sym_var("object_a_803379F0", "const double"),
    0x803379F8: table.sym_var_fnc("object_a_803379F8", "const", "[]"),
    0x80337A20: table.sym_var("object_a_80337A20", "const double"),
    0x80337A28: table.sym_var("object_a_80337A28", "const float"),
    0x80337A30: table.sym_var("object_a_80337A30", "const double"),
    0x80337A38: table.sym_var("object_a_80337A38", "const double"),
    0x80337A40: table.sym_var_fnc("object_a_80337A40", "const", "[]"),
    0x80337A54: table.sym_var_fnc("object_a_80337A54", "const", "[]"),
    0x80337A68: table.sym_var("object_a_80337A68", "const double"),
    0x80337A70: table.sym_var("object_a_80337A70", "const double"),
    0x80337A78: table.sym_var("object_a_80337A78", "const float"),
    0x80337A7C: table.sym_var("object_a_80337A7C", "const float"),
    0x80337A80: table.sym_var("object_a_80337A80", "const float"),
    0x80337A84: table.sym_var("object_a_80337A84", "const float"),
    0x80337A88: table.sym_var("object_a_80337A88", "const float"),
    0x80337A8C: table.sym_var("object_a_80337A8C", "const float"),
    0x80337A90: table.sym_var("object_a_80337A90", "const double"),
    0x80337A98: table.sym_var_fnc("object_a_80337A98", "const", "[]"),
    0x80337AAC: table.sym_var("object_a_80337AAC", "const float"),
    0x80337AB0: table.sym_var("object_a_80337AB0", "const float"),
    0x80337AB8: table.sym_var("object_a_80337AB8", "const double"),
    0x80337AC0: table.sym_var("object_a_80337AC0", "const float"),
    0x80337AC4: table.sym_var("object_a_80337AC4", "const float"),
    0x80337AC8: table.sym_var("object_a_80337AC8", "const double"),
    0x80337AD0: table.sym_var("object_a_80337AD0", "const double"),
    0x80337AD8: table.sym_var("object_a_80337AD8", "const float"),
    0x80337ADC: table.sym_var("object_a_80337ADC", "const float"),
    0x80337AE0: table.sym_var("object_a_80337AE0", "const double"),
    0x80337AE8: table.sym_var("object_a_80337AE8", "const double"),
    0x80337AF0: table.sym_var("object_a_80337AF0", "const double"),
    0x80337AF8: table.sym_var("object_a_80337AF8", "const double"),
    0x80337B00: table.sym_var("object_a_80337B00", "const double"),
    0x80337B08: table.sym_var_fnc("object_a_80337B08", "const", "[]"),
    0x80337B38: table.sym_var("object_a_80337B38", "const double"),
    0x80337B40: table.sym_var("object_a_80337B40", "const double"),
    0x80337B48: table.sym_var("object_a_80337B48", "const float"),
    0x80337B4C: table.sym_var_fnc("object_a_80337B4C", "const", "[]"),
    0x80337B74: table.sym_var("object_a_80337B74", "const float"),
    0x80337B78: table.sym_var("object_a_80337B78", "const double"),
    0x80337B80: table.sym_var("object_a_80337B80", "const double"),
    0x80337B88: table.sym_var("object_a_80337B88", "const double"),
    0x80337B90: table.sym_var_fnc("object_a_80337B90", "const", "[]"),
    0x80337BA4: table.sym_var_fnc("object_a_80337BA4", "const", "[]"),
    0x80337BBC: table.sym_var("object_a_80337BBC", "const float"),
    0x80337BC0: table.sym_var("object_a_80337BC0", "const float"),
    0x80337BC4: table.sym_var("object_a_80337BC4", "const float"),
    0x80337BC8: table.sym_var("object_a_80337BC8", "const float"),
    0x80337BD0: table.sym_var("object_a_80337BD0", "const double"),
    0x80337BD8: table.sym_var("object_a_80337BD8", "const float"),
    0x80337BDC: table.sym_var("object_a_80337BDC", "const float"),
    0x80337BE0: table.sym_var("object_a_80337BE0", "const float"),
    0x80337BE4: table.sym_var("object_a_80337BE4", "const float"),
    0x80337BE8: table.sym_var("object_a_80337BE8", "const double"),
    0x80337BF0: table.sym_var("object_a_80337BF0", "const float"),
    0x80337BF4: table.sym_var("object_a_80337BF4", "const float"),
    0x80337BF8: table.sym_var("object_a_80337BF8", "const double"),
    0x80337C00: table.sym_var("object_a_80337C00", "const float"),
    0x80337C04: table.sym_var("object_a_80337C04", "const float"),
    0x80337C08: table.sym_var("object_a_80337C08", "const float"),
    0x80337C0C: table.sym_var("object_a_80337C0C", "const float"),
    0x80337C10: table.sym_var_fnc("object_a_80337C10", "const", "[]"),
    0x80337C30: table.sym_var("object_a_80337C30", "const float"),
    0x80337C34: table.sym_var_fnc("object_a_80337C34", "const", "[]"),
    0x80337C54: table.sym_var("object_a_80337C54", "const float"),
    0x80337C58: table.sym_var("object_a_80337C58", "const float"),
    0x80337C5C: table.sym_var("object_a_80337C5C", "const float"),
    0x80337C60: table.sym_var("object_a_80337C60", "const float"),
    0x80337C64: table.sym_var("object_a_80337C64", "const float"),
    0x80337C68: table.sym_var("object_a_80337C68", "const double"),
    0x80337C70: table.sym_var_fnc("object_a_80337C70", "const", "[]"),
    0x80337C84: table.sym_var("object_a_80337C84", "const float"),
    0x80337C88: table.sym_var("object_a_80337C88", "const double"),
    0x80337C90: table.sym_var("object_a_80337C90", "const float"),
    0x80337C98: table.sym_var("object_a_80337C98", "const double"),
    0x80337CA0: table.sym_var("object_a_80337CA0", "const double"),
    0x80337CA8: table.sym_var("object_a_80337CA8", "const float"),
    0x80337CB0: table.sym_var("object_a_80337CB0", "const double"),
    0x80337CB8: table.sym_var("object_a_80337CB8", "const float"),
    0x80337CBC: table.sym_var("object_a_80337CBC", "const float"),
    0x80337CC0: table.sym_var("object_a_80337CC0", "const float"),
    0x80337CC4: table.sym_var("object_a_80337CC4", "const float"),
    0x80337CC8: table.sym_var("object_a_80337CC8", "const float"),
    0x80337CCC: table.sym_var("object_a_80337CCC", "const float"),
    0x80337CD0: table.sym_var("object_a_80337CD0", "const float"),
    0x80337CD4: table.sym_var("object_a_80337CD4", "const float"),
    0x80337CD8: table.sym_var("object_a_80337CD8", "const double"),
    0x80337CE0: table.sym_var("object_a_80337CE0", "const double"),
    0x80337CE8: table.sym_var("object_a_80337CE8", "const double"),
    0x80337CF0: table.sym_var("object_a_80337CF0", "const float"),
    0x80337CF4: table.sym_var("object_a_80337CF4", "const float"),
    0x80337CF8: table.sym_var("object_a_80337CF8", "const double"),
    0x80337D00: table.sym_var("object_a_80337D00", "const float"),
    0x80337D04: table.sym_var("object_a_80337D04", "const float"),
    0x80337D08: table.sym_var("object_a_80337D08", "const float"),
    0x80337D10: table.sym_var("object_a_80337D10", "const double"),
    0x80337D18: table.sym_var("object_a_80337D18", "const float"),
    0x80337D20: table.sym_var("object_a_80337D20", "const double"),
    0x80337D28: table.sym_var("object_a_80337D28", "const double"),
    0x80337D30: table.sym_var("object_a_80337D30", "const double"),
    0x80337D38: table.sym_var("object_a_80337D38", "const float"),
    0x80337D3C: table.sym_var("object_a_80337D3C", "const float"),
    0x80337D40: table.sym_var("object_a_80337D40", "const float"),
    0x80337D44: table.sym_var("object_a_80337D44", "const float"),
    0x80337D48: table.sym_var("object_a_80337D48", "const float"),
    0x80337D50: table.sym_var("object_a_80337D50", "const double"),
    0x80337D58: table.sym_var("object_a_80337D58", "const double"),
    0x80337D60: table.sym_var("object_a_80337D60", "const double"),
    0x80337D68: table.sym_var("object_a_80337D68", "const double"),
    0x80337D70: table.sym_var("object_a_80337D70", "const float"),
    0x80337D74: table.sym_var("object_a_80337D74", "const float"),
    0x80337D78: table.sym_var("object_a_80337D78", "const float"),
    0x80337D7C: table.sym_var("object_a_80337D7C", "const float"),
    0x80337D80: table.sym_var("object_a_80337D80", "const float"),
    0x80337D84: table.sym_var("object_a_80337D84", "const float"),
    0x80337D88: table.sym_var("object_a_80337D88", "const float"),
    0x80337D8C: table.sym_var("object_a_80337D8C", "const float"),
    0x80337D90: table.sym_var("object_a_80337D90", "const float"),
    0x80337D94: table.sym_var("object_a_80337D94", "const float"),
    0x80337D98: table.sym_var_fnc("object_a_80337D98", "const", "[]"),
    0x80337DAC: table.sym_var_fnc("object_a_80337DAC", "const", "[]"),
    0x80337DC4: table.sym_var("object_a_80337DC4", "const float"),
    0x80337DC8: table.sym_var("object_a_80337DC8", "const float"),
    0x80337DCC: table.sym_var("object_a_80337DCC", "const float"),
    0x80337DD0: table.sym_var("object_a_80337DD0", "const float"),
    0x80337DD4: table.sym_var("object_a_80337DD4", "const float"),
    0x80337DD8: table.sym_var("object_a_80337DD8", "const float"),
    0x80337DE0: table.sym_var("object_a_80337DE0", "const double"),
    0x80337DE8: table.sym_var("object_a_80337DE8", "const float"),
    0x80337DEC: table.sym_var("object_a_80337DEC", "const float"),

    # src/obj_collision.c
    0x80337DF0: table.sym_var("str_obj_collision_on",   "const char", "[]"),

    # src/obj_list.c
    0x80337E00: table.sym_var("obj_list_80337E00", "const float"),
    0x80337E04: table.sym_var("obj_list_80337E04", "const float"),
    0x80337E08: table.sym_var("obj_list_80337E08", "const float"),
    0x80337E0C: table.sym_var("obj_list_80337E0C", "const float"),

    # src/obj_sfx.c
    0x80337E10: table.sym_var("obj_sfx_80337E10", "const float"),
    0x80337E14: table.sym_var("obj_sfx_80337E14", "const float"),
    0x80337E18: table.sym_var("obj_sfx_80337E18", "const float"),

    # src/obj_debug.c
    0x80337E20: table.sym_var("str_obj_debug_a0",           "const char", "[]"),
    0x80337E28: table.sym_var("str_obj_debug_a1",           "const char", "[]"),
    0x80337E30: table.sym_var("str_obj_debug_a2",           "const char", "[]"),
    0x80337E38: table.sym_var("str_obj_debug_a3",           "const char", "[]"),
    0x80337E40: table.sym_var("str_obj_debug_a4",           "const char", "[]"),
    0x80337E48: table.sym_var("str_obj_debug_a5",           "const char", "[]"),
    0x80337E50: table.sym_var("str_obj_debug_a6",           "const char", "[]"),
    0x80337E58: table.sym_var("str_obj_debug_a7",           "const char", "[]"),
    0x80337E60: table.sym_var("str_obj_debug_a",            "const char", "[]"),
    0x80337E64: table.sym_var("str_obj_debug_b0",           "const char", "[]"),
    0x80337E6C: table.sym_var("str_obj_debug_b1",           "const char", "[]"),
    0x80337E74: table.sym_var("str_obj_debug_b2",           "const char", "[]"),
    0x80337E7C: table.sym_var("str_obj_debug_b3",           "const char", "[]"),
    0x80337E84: table.sym_var("str_obj_debug_b4",           "const char", "[]"),
    0x80337E8C: table.sym_var("str_obj_debug_b5",           "const char", "[]"),
    0x80337E94: table.sym_var("str_obj_debug_b6",           "const char", "[]"),
    0x80337E9C: table.sym_var("str_obj_debug_b7",           "const char", "[]"),
    0x80337EA4: table.sym_var("str_obj_debug_b",            "const char", "[]"),
    0x80337EA8: table.sym_var("str_obj_debug_dprint_over",  "const char", "[]"),
    0x80337EB4: table.sym_var("str_obj_debug_mapinfo",      "const char", "[]"),
    0x80337EBC: table.sym_var("str_obj_debug_area",         "const char", "[]"),
    0x80337EC4: table.sym_var("str_obj_debug_wx",           "const char", "[]"),
    0x80337ECC: table.sym_var("str_obj_debug_wy",           "const char", "[]"),
    0x80337ED4: table.sym_var("str_obj_debug_wz",           "const char", "[]"),
    0x80337EDC: table.sym_var("str_obj_debug_bgy",          "const char", "[]"),
    0x80337EE4: table.sym_var("str_obj_debug_angy",         "const char", "[]"),
    0x80337EEC: table.sym_var("str_obj_debug_bgcode",       "const char", "[]"),
    0x80337EF8: table.sym_var("str_obj_debug_bgstatus",     "const char", "[]"),
    0x80337F04: table.sym_var("str_obj_debug_bgarea",       "const char", "[]"),
    0x80337F10: table.sym_var("str_obj_debug_water",        "const char", "[]"),
    0x80337F1C: table.sym_var("str_obj_debug_checkinfo",    "const char", "[]"),
    0x80337F28: table.sym_var("str_obj_debug_stageinfo",    "const char", "[]"),
    0x80337F34: table.sym_var("str_obj_debug_stage_param",  "const char", "[]"),
    0x80337F44: table.sym_var("str_obj_debug_effectinfo",   "const char", "[]"),
    0x80337F50: table.sym_var("str_obj_debug_enemyinfo",    "const char", "[]"),
    0x80337F5C: table.sym_var("str_obj_debug_obj",          "const char", "[]"),
    0x80337F64: table.sym_var("str_obj_debug_nullbg",       "const char", "[]"),
    0x80337F70: table.sym_var("str_obj_debug_wall",         "const char", "[]"),
    0x80337F7C: table.sym_var("str_obj_debug_bound",        "const char", "[]"),
    0x80337F88: table.sym_var("str_obj_debug_touch",        "const char", "[]"),
    0x80337F94: table.sym_var("str_obj_debug_takeoff",      "const char", "[]"),
    0x80337FA0: table.sym_var("str_obj_debug_dive",         "const char", "[]"),
    0x80337FAC: table.sym_var("str_obj_debug_s_water",      "const char", "[]"),
    0x80337FB8: table.sym_var("str_obj_debug_u_water",      "const char", "[]"),
    0x80337FC4: table.sym_var("str_obj_debug_b_water",      "const char", "[]"),
    0x80337FD0: table.sym_var("str_obj_debug_sky",          "const char", "[]"),
    0x80337FDC: table.sym_var("str_obj_debug_out_scope",    "const char", "[]"),
    0x80337FF0: table.sym_var("obj_debug_80337FF0",         "const double"),

    # src/wipe.c
    0x80338000: table.sym_var("wipe_80338000", "const double"),
    0x80338008: table.sym_var("wipe_80338008", "const double"),
    0x80338010: table.sym_var_fnc("wipe_80338010", "const", "[]"),

    # src/shadow.c
    0x80338060: table.sym_var("shadow_80338060", "const double"),
    0x80338068: table.sym_var("shadow_80338068", "const double"),
    0x80338070: table.sym_var("shadow_80338070", "const double"),
    0x80338078: table.sym_var("shadow_80338078", "const double"),
    0x80338080: table.sym_var("shadow_80338080", "const double"),
    0x80338088: table.sym_var("shadow_80338088", "const double"),
    0x80338090: table.sym_var("shadow_80338090", "const double"),
    0x80338098: table.sym_var("shadow_80338098", "const double"),
    0x803380A0: table.sym_var("shadow_803380A0", "const double"),
    0x803380A8: table.sym_var("shadow_803380A8", "const double"),
    0x803380B0: table.sym_var("shadow_803380B0", "const double"),
    0x803380B8: table.sym_var("shadow_803380B8", "const double"),
    0x803380C0: table.sym_var("shadow_803380C0", "const double"),
    0x803380C8: table.sym_var("shadow_803380C8", "const double"),
    0x803380D0: table.sym_var("shadow_803380D0", "const double"),
    0x803380D8: table.sym_var("shadow_803380D8", "const float"),
    0x803380E0: table.sym_var("shadow_803380E0", "const double"),
    0x803380E8: table.sym_var("shadow_803380E8", "const float"),
    0x803380F0: table.sym_var("shadow_803380F0", "const double"),
    0x803380F8: table.sym_var("shadow_803380F8", "const double"),
    0x80338100: table.sym_var("shadow_80338100", "const double"),
    0x80338108: table.sym_var_fnc("shadow_80338108", "const", "[]"),

    # src/background.c
    0x80338140: table.sym_var("background_80338140", "const double"),
    0x80338148: table.sym_var("background_80338148", "const double"),
    0x80338150: table.sym_var("background_80338150", "const double"),
    0x80338158: table.sym_var("background_80338158", "const double"),

    # src/scroll.c
    0x80338160: table.sym_var("scroll_80338160", "const double"),

    # src/ripple.c
    0x80338170: table.sym_var("ripple_80338170", "const double"),
    0x80338178: table.sym_var("ripple_80338178", "const double"),
    0x80338180: table.sym_var("ripple_80338180", "const double"),
    0x80338188: table.sym_var("ripple_80338188", "const double"),
    0x80338190: table.sym_var("ripple_80338190", "const double"),

    # src/message.c
    0x803381A0: table.sym_var("message_803381A0", "const double"),
    0x803381A8: table.sym_var("message_803381A8", "const double"),
    0x803381B0: table.sym_var("message_803381B0", "const double"),
    0x803381B8: table.sym_var_fnc("message_803381B8", "const", "[]"),

    # src/weather_snow.c
    0x80338280: table.sym_var("weather_snow_80338280", "const double"),
    0x80338288: table.sym_var("weather_snow_80338288", "const double"),
    0x80338290: table.sym_var("weather_snow_80338290", "const double"),
    0x80338298: table.sym_var("weather_snow_80338298", "const double"),
    0x803382A0: table.sym_var("weather_snow_803382A0", "const double"),
    0x803382A8: table.sym_var("weather_snow_803382A8", "const double"),
    0x803382B0: table.sym_var("weather_snow_803382B0", "const double"),

    # src/weather_lava.c
    0x803382C0: table.sym_var("weather_lava_803382C0", "const float"),
    0x803382C4: table.sym_var("weather_lava_803382C4", "const float"),
    0x803382C8: table.sym_var("weather_lava_803382C8", "const float"),
    0x803382CC: table.sym_var("weather_lava_803382CC", "const float"),
    0x803382D0: table.sym_var("weather_lava_803382D0", "const float"),
    0x803382D4: table.sym_var_fnc("weather_lava_803382D4", "const", "[]"),

    # src/obj_data.c
    0x80338310: table.sym_var_fnc("obj_data_80338310", "const", "[]"),
    0x80338368: table.sym_var_fnc("obj_data_80338368", "const", "[]"),

    # src/hud.c
    0x80338380: table.sym_var("str_hud_life_icon",  "const char", "[]"),
    0x80338384: table.sym_var("str_hud_life_x",     "const char", "[]"),
    0x80338388: table.sym_var("str_hud_life_fmt",   "const char", "[]"),
    0x8033838C: table.sym_var("str_hud_coin_icon",  "const char", "[]"),
    0x80338390: table.sym_var("str_hud_coin_x",     "const char", "[]"),
    0x80338394: table.sym_var("str_hud_coin_fmt",   "const char", "[]"),
    0x80338398: table.sym_var("str_hud_star_icon",  "const char", "[]"),
    0x8033839C: table.sym_var("str_hud_star_x",     "const char", "[]"),
    0x803383A0: table.sym_var("str_hud_star_fmt",   "const char", "[]"),
    0x803383A4: table.sym_var("str_hud_key",        "const char", "[]"),
    0x803383A8: table.sym_var("str_hud_time_text",  "const char", "[]"),
    0x803383B0: table.sym_var("str_hud_time_min",   "const char", "[]"),
    0x803383B4: table.sym_var("str_hud_time_sec",   "const char", "[]"),
    0x803383BC: table.sym_var("str_hud_time_frc",   "const char", "[]"),
    0x803383C0: table.sym_var("hud_803383C0", "const double"),
    0x803383C8: table.sym_var("hud_803383C8", "const double"),

    # src/object_b.c
    0x803383D0: table.sym_var("object_b_803383D0", "const double"),
    0x803383D8: table.sym_var("object_b_803383D8", "const double"),
    0x803383E0: table.sym_var("object_b_803383E0", "const double"),
    0x803383E8: table.sym_var("object_b_803383E8", "const double"),
    0x803383F0: table.sym_var("object_b_803383F0", "const double"),
    0x803383F8: table.sym_var("object_b_803383F8", "const double"),
    0x80338400: table.sym_var("object_b_80338400", "const double"),
    0x80338408: table.sym_var("object_b_80338408", "const double"),
    0x80338410: table.sym_var("object_b_80338410", "const double"),
    0x80338418: table.sym_var("object_b_80338418", "const double"),
    0x80338420: table.sym_var("object_b_80338420", "const double"),
    0x80338428: table.sym_var("object_b_80338428", "const double"),
    0x80338430: table.sym_var("object_b_80338430", "const double"),
    0x80338438: table.sym_var("object_b_80338438", "const double"),
    0x80338440: table.sym_var("object_b_80338440", "const double"),
    0x80338448: table.sym_var("object_b_80338448", "const double"),
    0x80338450: table.sym_var("object_b_80338450", "const double"),
    0x80338458: table.sym_var("object_b_80338458", "const double"),
    0x80338460: table.sym_var("object_b_80338460", "const double"),
    0x80338468: table.sym_var("object_b_80338468", "const double"),
    0x80338470: table.sym_var("object_b_80338470", "const double"),
    0x80338478: table.sym_var("object_b_80338478", "const float"),
    0x80338480: table.sym_var("object_b_80338480", "const double"),
    0x80338488: table.sym_var("object_b_80338488", "const double"),
    0x80338490: table.sym_var("object_b_80338490", "const float"),
    0x80338494: table.sym_var_fnc("object_b_80338494", "const", "[]"),
    0x803384A8: table.sym_var_fnc("object_b_803384A8", "const", "[]"),
    0x803384BC: table.sym_var("object_b_803384BC", "const float"),
    0x803384C0: table.sym_var("object_b_803384C0", "const float"),
    0x803384C4: table.sym_var("object_b_803384C4", "const float"),
    0x803384C8: table.sym_var("object_b_803384C8", "const float"),
    0x803384CC: table.sym_var("object_b_803384CC", "const float"),
    0x803384D0: table.sym_var("object_b_803384D0", "const float"),
    0x803384D4: table.sym_var("object_b_803384D4", "const float"),
    0x803384D8: table.sym_var("object_b_803384D8", "const float"),
    0x803384DC: table.sym_var("object_b_803384DC", "const float"),
    0x803384E0: table.sym_var("object_b_803384E0", "const float"),
    0x803384E4: table.sym_var("object_b_803384E4", "const float"),
    0x803384E8: table.sym_var("object_b_803384E8", "const float"),
    0x803384EC: table.sym_var("object_b_803384EC", "const float"),
    0x803384F0: table.sym_var("object_b_803384F0", "const float"),
    0x803384F4: table.sym_var("object_b_803384F4", "const float"),
    0x803384F8: table.sym_var("object_b_803384F8", "const float"),
    0x803384FC: table.sym_var("object_b_803384FC", "const float"),
    0x80338500: table.sym_var("object_b_80338500", "const float"),
    0x80338508: table.sym_var("object_b_80338508", "const double"),
    0x80338510: table.sym_var("object_b_80338510", "const double"),
    0x80338518: table.sym_var_fnc("object_b_80338518", "const", "[]"),
    0x80338530: table.sym_var("object_b_80338530", "const double"),
    0x80338538: table.sym_var("object_b_80338538", "const float"),
    0x80338540: table.sym_var("object_b_80338540", "const double"),
    0x80338548: table.sym_var("object_b_80338548", "const double"),
    0x80338550: table.sym_var("object_b_80338550", "const double"),
    0x80338558: table.sym_var("object_b_80338558", "const double"),
    0x80338560: table.sym_var("object_b_80338560", "const double"),
    0x80338568: table.sym_var("object_b_80338568", "const double"),
    0x80338570: table.sym_var("object_b_80338570", "const float"),
    0x80338574: table.sym_var("object_b_80338574", "const float"),
    0x80338578: table.sym_var("object_b_80338578", "const float"),
    0x8033857C: table.sym_var("object_b_8033857C", "const float"),
    0x80338580: table.sym_var("object_b_80338580", "const float"),
    0x80338584: table.sym_var("object_b_80338584", "const float"),
    0x80338588: table.sym_var("object_b_80338588", "const float"),
    0x8033858C: table.sym_var("object_b_8033858C", "const float"),
    0x80338590: table.sym_var("object_b_80338590", "const float"),
    0x80338594: table.sym_var("object_b_80338594", "const float"),
    0x80338598: table.sym_var("object_b_80338598", "const float"),
    0x8033859C: table.sym_var_fnc("object_b_8033859C", "const", "[]"),
    0x803385B8: table.sym_var("object_b_803385B8", "const double"),
    0x803385C0: table.sym_var("object_b_803385C0", "const double"),
    0x803385C8: table.sym_var("object_b_803385C8", "const double"),
    0x803385D0: table.sym_var("object_b_803385D0", "const double"),
    0x803385D8: table.sym_var("object_b_803385D8", "const double"),
    0x803385E0: table.sym_var("object_b_803385E0", "const float"),
    0x803385E8: table.sym_var("object_b_803385E8", "const double"),
    0x803385F0: table.sym_var("object_b_803385F0", "const double"),
    0x803385F8: table.sym_var("object_b_803385F8", "const double"),
    0x80338600: table.sym_var("object_b_80338600", "const float"),
    0x80338604: table.sym_var("object_b_80338604", "const float"),
    0x80338608: table.sym_var("object_b_80338608", "const float"),
    0x8033860C: table.sym_var("object_b_8033860C", "const float"),
    0x80338610: table.sym_var("object_b_80338610", "const float"),
    0x80338614: table.sym_var("object_b_80338614", "const float"),
    0x80338618: table.sym_var("object_b_80338618", "const float"),
    0x8033861C: table.sym_var("object_b_8033861C", "const float"),
    0x80338620: table.sym_var("object_b_80338620", "const float"),
    0x80338624: table.sym_var("object_b_80338624", "const float"),
    0x80338628: table.sym_var("object_b_80338628", "const float"),
    0x8033862C: table.sym_var("object_b_8033862C", "const float"),
    0x80338630: table.sym_var("object_b_80338630", "const float"),
    0x80338634: table.sym_var("object_b_80338634", "const float"),
    0x80338638: table.sym_var("object_b_80338638", "const float"),
    0x8033863C: table.sym_var_fnc("object_b_8033863C", "const", "[]"),
    0x80338650: table.sym_var_fnc("object_b_80338650", "const", "[]"),
    0x80338668: table.sym_var_fnc("object_b_80338668", "const", "[]"),
    0x80338680: table.sym_var("object_b_80338680", "const double"),
    0x80338688: table.sym_var_fnc("object_b_80338688", "const", "[]"),
    0x8033869C: table.sym_var("object_b_8033869C", "const float"),
    0x803386A0: table.sym_var("object_b_803386A0", "const float"),
    0x803386A4: table.sym_var("object_b_803386A4", "const float"),
    0x803386A8: table.sym_var("object_b_803386A8", "const float"),
    0x803386AC: table.sym_var("object_b_803386AC", "const float"),
    0x803386B0: table.sym_var("object_b_803386B0", "const float"),
    0x803386B4: table.sym_var("object_b_803386B4", "const float"),
    0x803386B8: table.sym_var("object_b_803386B8", "const float"),
    0x803386BC: table.sym_var("object_b_803386BC", "const float"),
    0x803386C0: table.sym_var("object_b_803386C0", "const float"),
    0x803386C8: table.sym_var("object_b_803386C8", "const double"),
    0x803386D0: table.sym_var("object_b_803386D0", "const double"),
    0x803386D8: table.sym_var("object_b_803386D8", "const double"),
    0x803386E0: table.sym_var("object_b_803386E0", "const float"),
    0x803386E4: table.sym_var("object_b_803386E4", "const float"),
    0x803386E8: table.sym_var("object_b_803386E8", "const float"),
    0x803386EC: table.sym_var("object_b_803386EC", "const float"),
    0x803386F0: table.sym_var_fnc("object_b_803386F0", "const", "[]"),
    0x80338704: table.sym_var("object_b_80338704", "const float"),
    0x80338708: table.sym_var("object_b_80338708", "const float"),
    0x8033870C: table.sym_var("object_b_8033870C", "const float"),
    0x80338710: table.sym_var("object_b_80338710", "const float"),
    0x80338714: table.sym_var("object_b_80338714", "const float"),
    0x80338718: table.sym_var("object_b_80338718", "const float"),
    0x8033871C: table.sym_var_fnc("object_b_8033871C", "const", "[]"),
    0x80338730: table.sym_var("object_b_80338730", "const float"),
    0x80338734: table.sym_var("object_b_80338734", "const float"),
    0x80338738: table.sym_var("object_b_80338738", "const float"),
    0x8033873C: table.sym_var("object_b_8033873C", "const float"),
    0x80338740: table.sym_var("object_b_80338740", "const double"),
    0x80338748: table.sym_var_fnc("object_b_80338748", "const", "[]"),
    0x803387D8: table.sym_var("object_b_803387D8", "const float"),
    0x803387DC: table.sym_var("object_b_803387DC", "const float"),
    0x803387E0: table.sym_var("object_b_803387E0", "const float"),
    0x803387E8: table.sym_var("object_b_803387E8", "const double"),
    0x803387F0: table.sym_var("object_b_803387F0", "const double"),
    0x803387F8: table.sym_var("object_b_803387F8", "const float"),
    0x803387FC: table.sym_var("object_b_803387FC", "const float"),
    0x80338800: table.sym_var("object_b_80338800", "const float"),
    0x80338804: table.sym_var("object_b_80338804", "const float"),
    0x80338808: table.sym_var("object_b_80338808", "const float"),
    0x8033880C: table.sym_var("object_b_8033880C", "const float"),
    0x80338810: table.sym_var("object_b_80338810", "const float"),
    0x80338814: table.sym_var("object_b_80338814", "const float"),
    0x80338818: table.sym_var("object_b_80338818", "const float"),
    0x8033881C: table.sym_var("object_b_8033881C", "const float"),
    0x80338820: table.sym_var("object_b_80338820", "const float"),
    0x80338828: table.sym_var("object_b_80338828", "const double"),
    0x80338830: table.sym_var("object_b_80338830", "const double"),
    0x80338838: table.sym_var("object_b_80338838", "const double"),
    0x80338840: table.sym_var_fnc("object_b_80338840", "const", "[]"),
    0x80338860: table.sym_var("object_b_80338860", "const double"),
    0x80338868: table.sym_var("object_b_80338868", "const double"),
    0x80338870: table.sym_var("object_b_80338870", "const double"),
    0x80338878: table.sym_var("object_b_80338878", "const double"),
    0x80338880: table.sym_var("object_b_80338880", "const double"),
    0x80338888: table.sym_var("object_b_80338888", "const double"),
    0x80338890: table.sym_var("object_b_80338890", "const double"),
    0x80338898: table.sym_var("object_b_80338898", "const double"),
    0x803388A0: table.sym_var("object_b_803388A0", "const double"),
    0x803388A8: table.sym_var("object_b_803388A8", "const double"),
    0x803388B0: table.sym_var("object_b_803388B0", "const double"),
    0x803388B8: table.sym_var("object_b_803388B8", "const double"),
    0x803388C0: table.sym_var("object_b_803388C0", "const double"),
    0x803388C8: table.sym_var("object_b_803388C8", "const double"),
    0x803388D0: table.sym_var("object_b_803388D0", "const double"),
    0x803388D8: table.sym_var("object_b_803388D8", "const double"),
    0x803388E0: table.sym_var("object_b_803388E0", "const double"),
    0x803388E8: table.sym_var("object_b_803388E8", "const double"),
    0x803388F0: table.sym_var("object_b_803388F0", "const double"),
    0x803388F8: table.sym_var("object_b_803388F8", "const double"),
    0x80338900: table.sym_var("object_b_80338900", "const float"),
    0x80338904: table.sym_var("object_b_80338904", "const float"),
    0x80338908: table.sym_var("object_b_80338908", "const float"),
    0x80338910: table.sym_var("object_b_80338910", "const double"),
    0x80338918: table.sym_var("object_b_80338918", "const double"),
    0x80338920: table.sym_var("object_b_80338920", "const float"),
    0x80338924: table.sym_var("object_b_80338924", "const float"),
    0x80338928: table.sym_var("object_b_80338928", "const float"),
    0x8033892C: table.sym_var("object_b_8033892C", "const float"),
    0x80338930: table.sym_var("object_b_80338930", "const float"),
    0x80338934: table.sym_var("object_b_80338934", "const float"),
    0x80338938: table.sym_var("object_b_80338938", "const float"),
    0x8033893C: table.sym_var("object_b_8033893C", "const float"),
    0x80338940: table.sym_var_fnc("object_b_80338940", "const", "[]"),
    0x80338954: table.sym_var("object_b_80338954", "const float"),
    0x80338958: table.sym_var("object_b_80338958", "const float"),
    0x8033895C: table.sym_var("object_b_8033895C", "const float"),
    0x80338960: table.sym_var("object_b_80338960", "const double"),
    0x80338968: table.sym_var("object_b_80338968", "const float"),
    0x8033896C: table.sym_var("object_b_8033896C", "const float"),
    0x80338970: table.sym_var("object_b_80338970", "const float"),
    0x80338974: table.sym_var("object_b_80338974", "const float"),
    0x80338978: table.sym_var_fnc("object_b_80338978", "const", "[]"),

    # src/object_c.c
    0x803389B0: table.sym_var("object_c_803389B0", "const float"),
    0x803389B4: table.sym_var("object_c_803389B4", "const float"),
    0x803389B8: table.sym_var_fnc("object_c_803389B8", "const", "[]"),
    0x803389DC: table.sym_var("object_c_803389DC", "const float"),
    0x803389E0: table.sym_var("object_c_803389E0", "const float"),
    0x803389E4: table.sym_var("object_c_803389E4", "const float"),
    0x803389E8: table.sym_var("object_c_803389E8", "const float"),
    0x803389EC: table.sym_var("object_c_803389EC", "const float"),
    0x803389F0: table.sym_var("object_c_803389F0", "const float"),
    0x803389F4: table.sym_var("object_c_803389F4", "const float"),
    0x803389F8: table.sym_var("object_c_803389F8", "const float"),
    0x803389FC: table.sym_var("object_c_803389FC", "const float"),
    0x80338A00: table.sym_var("object_c_80338A00", "const float"),
    0x80338A04: table.sym_var("object_c_80338A04", "const float"),
    0x80338A08: table.sym_var("object_c_80338A08", "const float"),
    0x80338A0C: table.sym_var("object_c_80338A0C", "const float"),
    0x80338A10: table.sym_var("object_c_80338A10", "const float"),
    0x80338A14: table.sym_var("object_c_80338A14", "const float"),
    0x80338A18: table.sym_var("object_c_80338A18", "const float"),
    0x80338A1C: table.sym_var("object_c_80338A1C", "const float"),
    0x80338A20: table.sym_var("object_c_80338A20", "const float"),
    0x80338A24: table.sym_var("object_c_80338A24", "const float"),
    0x80338A28: table.sym_var("object_c_80338A28", "const float"),
    0x80338A2C: table.sym_var("object_c_80338A2C", "const float"),
    0x80338A30: table.sym_var_fnc("object_c_80338A30", "const", "[]"),
    0x80338A4C: table.sym_var("object_c_80338A4C", "const float"),
    0x80338A50: table.sym_var("object_c_80338A50", "const float"),
    0x80338A54: table.sym_var("object_c_80338A54", "const float"),
    0x80338A58: table.sym_var("object_c_80338A58", "const float"),
    0x80338A5C: table.sym_var("object_c_80338A5C", "const float"),
    0x80338A60: table.sym_var("object_c_80338A60", "const float"),
    0x80338A64: table.sym_var("object_c_80338A64", "const float"),
    0x80338A68: table.sym_var("object_c_80338A68", "const float"),
    0x80338A6C: table.sym_var("object_c_80338A6C", "const float"),
    0x80338A70: table.sym_var("object_c_80338A70", "const float"),
    0x80338A74: table.sym_var("object_c_80338A74", "const float"),
    0x80338A78: table.sym_var("object_c_80338A78", "const float"),
    0x80338A7C: table.sym_var("object_c_80338A7C", "const float"),
    0x80338A80: table.sym_var("object_c_80338A80", "const float"),
    0x80338A84: table.sym_var("object_c_80338A84", "const float"),
    0x80338A88: table.sym_var("object_c_80338A88", "const float"),
    0x80338A8C: table.sym_var("object_c_80338A8C", "const float"),
    0x80338A90: table.sym_var("object_c_80338A90", "const float"),
    0x80338A94: table.sym_var("object_c_80338A94", "const float"),
    0x80338A98: table.sym_var("object_c_80338A98", "const float"),
    0x80338A9C: table.sym_var("object_c_80338A9C", "const float"),
    0x80338AA0: table.sym_var("object_c_80338AA0", "const float"),
    0x80338AA4: table.sym_var_fnc("object_c_80338AA4", "const", "[]"),
    0x80338ABC: table.sym_var("object_c_80338ABC", "const float"),
    0x80338AC0: table.sym_var("object_c_80338AC0", "const float"),
    0x80338AC4: table.sym_var("object_c_80338AC4", "const float"),
    0x80338AC8: table.sym_var("object_c_80338AC8", "const float"),
    0x80338ACC: table.sym_var_fnc("object_c_80338ACC", "const", "[]"),
    0x80338AE0: table.sym_var("object_c_80338AE0", "const float"),
    0x80338AE4: table.sym_var("object_c_80338AE4", "const float"),
    0x80338AE8: table.sym_var("object_c_80338AE8", "const float"),
    0x80338AEC: table.sym_var("object_c_80338AEC", "const float"),
    0x80338AF0: table.sym_var("object_c_80338AF0", "const float"),
    0x80338AF4: table.sym_var("object_c_80338AF4", "const float"),
    0x80338AF8: table.sym_var("object_c_80338AF8", "const float"),
    0x80338AFC: table.sym_var("object_c_80338AFC", "const float"),
    0x80338B00: table.sym_var("object_c_80338B00", "const float"),
    0x80338B04: table.sym_var("object_c_80338B04", "const float"),
    0x80338B08: table.sym_var("object_c_80338B08", "const float"),
    0x80338B0C: table.sym_var("object_c_80338B0C", "const float"),
    0x80338B10: table.sym_var("object_c_80338B10", "const float"),
    0x80338B14: table.sym_var("object_c_80338B14", "const float"),
    0x80338B18: table.sym_var("object_c_80338B18", "const float"),
    0x80338B1C: table.sym_var("object_c_80338B1C", "const float"),
    0x80338B20: table.sym_var("object_c_80338B20", "const float"),
    0x80338B24: table.sym_var("object_c_80338B24", "const float"),
    0x80338B28: table.sym_var("object_c_80338B28", "const float"),
    0x80338B2C: table.sym_var("object_c_80338B2C", "const float"),
    0x80338B30: table.sym_var("object_c_80338B30", "const float"),
    0x80338B34: table.sym_var("object_c_80338B34", "const float"),
    0x80338B38: table.sym_var("object_c_80338B38", "const float"),
    0x80338B3C: table.sym_var_fnc("object_c_80338B3C", "const", "[]"),
    0x80338B5C: table.sym_var("object_c_80338B5C", "const float"),
    0x80338B60: table.sym_var("object_c_80338B60", "const float"),
    0x80338B64: table.sym_var("object_c_80338B64", "const float"),
    0x80338B68: table.sym_var("object_c_80338B68", "const float"),
    0x80338B6C: table.sym_var_fnc("object_c_80338B6C", "const", "[]"),
    0x80338B80: table.sym_var("object_c_80338B80", "const float"),
    0x80338B84: table.sym_var("object_c_80338B84", "const float"),
    0x80338B88: table.sym_var("object_c_80338B88", "const float"),
    0x80338B8C: table.sym_var("object_c_80338B8C", "const float"),
    0x80338B90: table.sym_var("object_c_80338B90", "const float"),
    0x80338B94: table.sym_var("object_c_80338B94", "const float"),
    0x80338B98: table.sym_var("object_c_80338B98", "const float"),
    0x80338B9C: table.sym_var("object_c_80338B9C", "const float"),
    0x80338BA0: table.sym_var("object_c_80338BA0", "const float"),
    0x80338BA4: table.sym_var("object_c_80338BA4", "const float"),
    0x80338BA8: table.sym_var("object_c_80338BA8", "const float"),
    0x80338BAC: table.sym_var("object_c_80338BAC", "const float"),
    0x80338BB0: table.sym_var("object_c_80338BB0", "const float"),
    0x80338BB4: table.sym_var("object_c_80338BB4", "const float"),
    0x80338BB8: table.sym_var("object_c_80338BB8", "const float"),
    0x80338BBC: table.sym_var("object_c_80338BBC", "const float"),
    0x80338BC0: table.sym_var("object_c_80338BC0", "const float"),
    0x80338BC4: table.sym_var("object_c_80338BC4", "const float"),
    0x80338BC8: table.sym_var_fnc("object_c_80338BC8", "const", "[]"),
    0x80338BE8: table.sym_var("object_c_80338BE8", "const float"),
    0x80338BEC: table.sym_var("object_c_80338BEC", "const float"),
    0x80338BF0: table.sym_var("object_c_80338BF0", "const float"),
    0x80338BF4: table.sym_var("object_c_80338BF4", "const float"),
    0x80338BF8: table.sym_var("object_c_80338BF8", "const float"),
    0x80338BFC: table.sym_var("object_c_80338BFC", "const float"),
    0x80338C00: table.sym_var("object_c_80338C00", "const float"),
    0x80338C04: table.sym_var("object_c_80338C04", "const float"),
    0x80338C08: table.sym_var_fnc("object_c_80338C08", "const", "[]"),
    0x80338C1C: table.sym_var("object_c_80338C1C", "const float"),
    0x80338C20: table.sym_var("object_c_80338C20", "const float"),
    0x80338C24: table.sym_var("object_c_80338C24", "const float"),
    0x80338C28: table.sym_var("object_c_80338C28", "const float"),
    0x80338C2C: table.sym_var("object_c_80338C2C", "const float"),
    0x80338C30: table.sym_var("object_c_80338C30", "const float"),
    0x80338C34: table.sym_var("object_c_80338C34", "const float"),
    0x80338C38: table.sym_var_fnc("object_c_80338C38", "const", "[]"),
    0x80338C4C: table.sym_var("object_c_80338C4C", "const float"),
    0x80338C50: table.sym_var("object_c_80338C50", "const float"),
    0x80338C54: table.sym_var("object_c_80338C54", "const float"),
    0x80338C58: table.sym_var("object_c_80338C58", "const float"),
    0x80338C5C: table.sym_var("object_c_80338C5C", "const float"),
    0x80338C60: table.sym_var("object_c_80338C60", "const float"),
    0x80338C64: table.sym_var("object_c_80338C64", "const float"),
    0x80338C68: table.sym_var("object_c_80338C68", "const float"),
    0x80338C6C: table.sym_var("object_c_80338C6C", "const float"),
    0x80338C70: table.sym_var("object_c_80338C70", "const float"),
    0x80338C74: table.sym_var("object_c_80338C74", "const float"),
    0x80338C78: table.sym_var("object_c_80338C78", "const float"),
    0x80338C7C: table.sym_var_fnc("object_c_80338C7C", "const", "[]"),
    0x80338C90: table.sym_var("object_c_80338C90", "const float"),
    0x80338C94: table.sym_var("object_c_80338C94", "const float"),
    0x80338C98: table.sym_var("object_c_80338C98", "const float"),
    0x80338C9C: table.sym_var("object_c_80338C9C", "const float"),
    0x80338CA0: table.sym_var_fnc("object_c_80338CA0", "const", "[]"),
    0x80338CDC: table.sym_var("object_c_80338CDC", "const float"),
    0x80338CE0: table.sym_var("object_c_80338CE0", "const float"),
    0x80338CE4: table.sym_var("object_c_80338CE4", "const float"),
    0x80338CE8: table.sym_var("object_c_80338CE8", "const float"),
    0x80338CEC: table.sym_var("object_c_80338CEC", "const float"),
    0x80338CF0: table.sym_var("object_c_80338CF0", "const float"),
    0x80338CF4: table.sym_var_fnc("object_c_80338CF4", "const", "[]"),
    0x80338D14: table.sym_var("object_c_80338D14", "const float"),
    0x80338D18: table.sym_var("object_c_80338D18", "const float"),
    0x80338D1C: table.sym_var("object_c_80338D1C", "const float"),
    0x80338D20: table.sym_var("object_c_80338D20", "const float"),
    0x80338D24: table.sym_var("object_c_80338D24", "const float"),
    0x80338D28: table.sym_var("object_c_80338D28", "const float"),
    0x80338D2C: table.sym_var("object_c_80338D2C", "const float"),
    0x80338D30: table.sym_var("object_c_80338D30", "const float"),
    0x80338D34: table.sym_var_fnc("object_c_80338D34", "const", "[]"),
    0x80338D4C: table.sym_var("object_c_80338D4C", "const float"),
    0x80338D50: table.sym_var("object_c_80338D50", "const float"),
    0x80338D54: table.sym_var("object_c_80338D54", "const float"),
    0x80338D58: table.sym_var("object_c_80338D58", "const float"),
    0x80338D5C: table.sym_var("object_c_80338D5C", "const float"),
    0x80338D60: table.sym_var("object_c_80338D60", "const float"),
    0x80338D64: table.sym_var("object_c_80338D64", "const float"),
    0x80338D68: table.sym_var("object_c_80338D68", "const float"),
    0x80338D6C: table.sym_var("object_c_80338D6C", "const float"),
    0x80338D70: table.sym_var("object_c_80338D70", "const float"),
    0x80338D74: table.sym_var("object_c_80338D74", "const float"),
    0x80338D78: table.sym_var("object_c_80338D78", "const float"),
    0x80338D7C: table.sym_var("object_c_80338D7C", "const float"),
    0x80338D80: table.sym_var("object_c_80338D80", "const float"),
    0x80338D84: table.sym_var("object_c_80338D84", "const float"),
    0x80338D88: table.sym_var("object_c_80338D88", "const float"),
    0x80338D8C: table.sym_var("object_c_80338D8C", "const float"),
    0x80338D90: table.sym_var("object_c_80338D90", "const float"),

    # src/audio/a.c
    0x80338DA0: table.sym_var("Na_a_80338DA0", "const float"),
    0x80338DA4: table.sym_var("Na_a_80338DA4", "const float"),
    0x80338DA8: table.sym_var("Na_a_80338DA8", "const float"),
    0x80338DAC: table.sym_var("Na_a_80338DAC", "const float"),
    0x80338DB0: table.sym_var("Na_a_80338DB0", "const float"),

    # src/audio/b.c
    0x80338DC0: table.sym_var_fnc("Na_b_80338DC0", "const", "[]"),
    0x80338E00: table.sym_var("Na_b_80338E00", "const float"),
    0x80338E04: table.sym_var("Na_b_80338E04", "const float"),

    # src/audio/d.c
    0x80338E10: table.sym_var("Na_d_80338E10", "const float"),
    0x80338E14: table.sym_var("Na_d_80338E14", "const float"),
    0x80338E18: table.sym_var("Na_d_80338E18", "const float"),
    0x80338E1C: table.sym_var("Na_d_80338E1C", "const float"),
    0x80338E20: table.sym_var("Na_d_80338E20", "const float"),
    0x80338E24: table.sym_var("Na_d_80338E24", "const float"),

    # src/audio/e.c
    0x80338E30: table.sym_var_fnc("Na_e_80338E30", "const", "[]"),

    # src/audio/f.c
    0x80338E60: table.sym_var_fnc("Na_f_80338E60", "const", "[]"),
    0x80338E84: table.sym_var_fnc("Na_f_80338E84", "const", "[]"),
    0x80338EAC: table.sym_var_fnc("Na_f_80338EAC", "const", "[]"),
    0x80338EC0: table.sym_var_fnc("Na_f_80338EC0", "const", "[]"),
    0x80338FBC: table.sym_var_fnc("Na_f_80338FBC", "const", "[]"),
    0x80339280: table.sym_var_fnc("Na_f_80339280", "const", "[]"),
    0x80339360: table.sym_var_fnc("Na_f_80339360", "const", "[]"),

    # src/audio/g.c
    0x803394F0: table.sym_var("str_Na_g_803394F0", "const char", "[]"),
    0x803394FC: table.sym_var("str_Na_g_803394FC", "const char", "[]"),
    0x80339518: table.sym_var("str_Na_g_80339518", "const char", "[]"),
    0x80339524: table.sym_var("str_Na_g_80339524", "const char", "[]"),
    0x80339540: table.sym_var("str_Na_g_80339540", "const char", "[]"),
    0x8033954C: table.sym_var("str_Na_g_8033954C", "const char", "[]"),
    0x80339560: table.sym_var("str_Na_g_80339560", "const char", "[]"),
    0x80339568: table.sym_var("str_Na_g_80339568", "const char", "[]"),
    0x8033956C: table.sym_var("str_Na_g_8033956C", "const char", "[]"),
    0x80339578: table.sym_var("str_Na_g_80339578", "const char", "[]"),
    0x8033958C: table.sym_var("str_Na_g_8033958C", "const char", "[]"),
    0x80339594: table.sym_var("str_Na_g_80339594", "const char", "[]"),
    0x80339598: table.sym_var("str_Na_g_80339598", "const char", "[]"),
    0x803395C8: table.sym_var("str_Na_g_803395C8", "const char", "[]"),
    0x803395F8: table.sym_var("str_Na_g_803395F8", "const char", "[]"),
    0x80339600: table.sym_var("str_Na_g_80339600", "const char", "[]"),
    0x80339604: table.sym_var("str_Na_g_80339604", "const char", "[]"),
    0x80339608: table.sym_var("str_Na_g_80339608", "const char", "[]"),
    0x80339610: table.sym_var("str_Na_g_80339610", "const char", "[]"),
    0x80339614: table.sym_var("str_Na_g_80339614", "const char", "[]"),
    0x80339618: table.sym_var("str_Na_g_80339618", "const char", "[]"),
    0x80339624: table.sym_var("str_Na_g_80339624", "const char", "[]"),
    0x80339630: table.sym_var("str_Na_g_80339630", "const char", "[]"),
    0x8033963C: table.sym_var("str_Na_g_8033963C", "const char", "[]"),
    0x80339648: table.sym_var("str_Na_g_80339648", "const char", "[]"),
    0x80339660: table.sym_var("str_Na_g_80339660", "const char", "[]"),
    0x8033967C: table.sym_var("str_Na_g_8033967C", "const char", "[]"),
    0x8033968C: table.sym_var("str_Na_g_8033968C", "const char", "[]"),
    0x8033969C: table.sym_var("str_Na_g_8033969C", "const char", "[]"),
    0x803396AC: table.sym_var("str_Na_g_803396AC", "const char", "[]"),
    0x803396BC: table.sym_var("str_Na_g_803396BC", "const char", "[]"),
    0x803396CC: table.sym_var("str_Na_g_803396CC", "const char", "[]"),
    0x803396D8: table.sym_var("str_Na_g_803396D8", "const char", "[]"),
    0x803396EC: table.sym_var("str_Na_g_803396EC", "const char", "[]"),
    0x80339710: table.sym_var("Na_g_80339710", "const double"),
    0x80339718: table.sym_var("Na_g_80339718", "const double"),
    0x80339720: table.sym_var("Na_g_80339720", "const float"),
    0x80339724: table.sym_var("Na_g_80339724", "const float"),
    0x80339728: table.sym_var("Na_g_80339728", "const float"),
    0x8033972C: table.sym_var("Na_g_8033972C", "const float"),
    0x80339730: table.sym_var("Na_g_80339730", "const float"),
    0x80339734: table.sym_var("Na_g_80339734", "const float"),
    0x80339738: table.sym_var("Na_g_80339738", "const float"),
    0x8033973C: table.sym_var_fnc("Na_g_8033973C", "const", "[]"),
    0x80339764: table.sym_var_fnc("Na_g_80339764", "const", "[]"),
    0x8033978C: table.sym_var_fnc("Na_g_8033978C", "const", "[]"),

    # ==========================================================================
    # bss
    # ==========================================================================

    # src/main.c
    0x8033A580: table.sym_var("thread_fault",   "OSThread",         flag=table.GLOBL|ultra.BALIGN),
    0x8033A730: table.sym_var("thread_idle",    "OSThread",         flag=table.GLOBL|ultra.BALIGN),
    0x8033A8E0: table.sym_var("thread_sc",      "OSThread",         flag=table.GLOBL|ultra.BALIGN),
    0x8033AA90: table.sym_var("thread_app",     "OSThread",         flag=table.GLOBL|ultra.BALIGN),
    0x8033AC40: table.sym_var("thread_audio",   "OSThread",         flag=table.GLOBL|ultra.BALIGN),
    0x8033ADF0: table.sym_var("mq_pi",          "OSMesgQueue",      flag=table.GLOBL|ultra.BALIGN),
    0x8033AE08: table.sym_var("mq_sc",          "OSMesgQueue",      flag=table.GLOBL|ultra.BALIGN),
    0x8033AE20: table.sym_var("mq_sc_task",     "OSMesgQueue",      flag=table.GLOBL|ultra.BALIGN),
    0x8033AE38: table.sym_var("msg_app",        "OSMesg",           flag=table.GLOBL),
    0x8033AE40: table.sym_var("msg_pi",         "OSMesg", "[32]",   table.GLOBL|ultra.BALIGN),
    0x8033AEC0: table.sym_var("msg_si",         "OSMesg",           flag=table.GLOBL),
    0x8033AEC8: table.sym_var("msg_sc",         "OSMesg", "[16]",   table.GLOBL|ultra.BALIGN),
    0x8033AF08: table.sym_var("msg_sc_task",    "OSMesg", "[16]",   table.GLOBL|ultra.BALIGN),
    0x8033AF48: table.sym_var("iomesg_app",     "OSIoMesg",         flag=table.GLOBL|ultra.BALIGN),
    0x8033AF5C: table.sym_var("msg_null",       "OSMesg",           flag=table.GLOBL),
    0x8033AF60: table.sym_var("mq_app",         "OSMesgQueue",      flag=table.GLOBL|ultra.BALIGN),
    0x8033AF78: table.sym_var("mq_si",          "OSMesgQueue",      flag=table.GLOBL|ultra.BALIGN),

    # src/app.c
    0x8033AF90: table.sym_var("controller_table",   "CONTROLLER",   "[3]",  table.GLOBL|ultra.BALIGN),
    0x8033AFE8: table.sym_var("contstatus_table",   "OSContStatus", "[4]",  table.GLOBL|ultra.BALIGN),
    0x8033AFF8: table.sym_var("contpad_table",      "OSContPad",    "[4]",  table.GLOBL|ultra.BALIGN),
    0x8033B010: table.sym_var("mq_video_vi",        "OSMesgQueue",  flag=table.GLOBL|ultra.BALIGN),
    0x8033B028: table.sym_var("mq_video_dp",        "OSMesgQueue",  flag=table.GLOBL|ultra.BALIGN),
    0x8033B040: table.sym_var("msg_video_vi",       "OSMesg",       flag=table.GLOBL),
    0x8033B044: table.sym_var("msg_video_dp",       "OSMesg",       flag=table.GLOBL),
    0x8033B048: table.sym_var("sc_client_video",    "SC_CLIENT",    flag=table.GLOBL|ultra.BALIGN),
    0x8033B050: table.sym_var("video_cimg",         "uintptr_t", "[3]", table.GLOBL|ultra.BALIGN),
    0x8033B05C: table.sym_var("video_zimg",         "uintptr_t",        flag=table.GLOBL),
    0x8033B060: table.sym_var("anime_mario_buffer", "u8 *",         flag=table.GLOBL),
    0x8033B064: table.sym_var("demo_buffer",        "u8 *",         flag=table.GLOBL),
    0x8033B068: table.sym_var("video_task",         "SC_TASK *",    flag=table.GLOBL),
    0x8033B06C: table.sym_var("video_gfx",          "Gfx *",        flag=table.GLOBL),
    0x8033B070: table.sym_var("video_mem",          "u8 *",         flag=table.GLOBL),
    0x8033B074: table.sym_var("video",              "VIDEO *",      flag=table.GLOBL),
    0x8033B078: table.sym_var("input_flag",         "u8",   flag=table.GLOBL),
    0x8033B079: table.sym_var("eeprom_status",      "s8",   flag=table.GLOBL),
    0x8033B080: table.sym_var("file_anime_mario",   "FILE", flag=table.GLOBL|ultra.BALIGN),
    0x8033B090: table.sym_var("file_demo",          "FILE", flag=table.GLOBL|ultra.BALIGN),

    # src/audio.c
    0x8033B0A0: table.sym_var("audio_env_se_8033B0A0",  "u32", "[]",    table.GLOBL|ultra.BALIGN), # unused
    0x8033B130: table.sym_var("audio_0",            "vecf",             flag=table.GLOBL|ultra.BALIGN),
    0x8033B140: table.sym_var("mq_audio",           "OSMesgQueue",      flag=table.GLOBL|ultra.BALIGN),
    0x8033B158: table.sym_var("msg_audio",          "OSMesg",           flag=table.GLOBL),
    0x8033B160: table.sym_var("sc_client_audio",    "SC_CLIENT",        flag=table.GLOBL|ultra.BALIGN),

    # src/game.c
    0x8033B170: table.sym_var("player_table",   "PLAYER", "[1]",  table.GLOBL|ultra.BALIGN),
    0x8033B238: table.sym_var("game_8033B238",  "s16",  flag=table.GLOBL),
    0x8033B23A: table.sym_var("game_8033B23A",  "s16",  flag=table.GLOBL),
    0x8033B23C: table.sym_var("game_8033B23C",  "s16",  flag=table.GLOBL),
    0x8033B240: table.sym_var_fnc("game_8033B240", arg=("s16 *",), flag=table.GLOBL),
    0x8033B248: table.sym_var("game_8033B248",  "struct struct_8033B248",   flag=table.GLOBL|ultra.BALIGN),
    0x8033B250: table.sym_var("game_8033B250",  "s16",  flag=table.GLOBL),
    0x8033B252: table.sym_var("game_8033B252",  "s16",  flag=table.GLOBL),
    0x8033B254: table.sym_var("game_8033B254",  "s16",  flag=table.GLOBL),
    0x8033B256: table.sym_var("game_8033B256",  "s16",  flag=table.GLOBL),
    0x8033B258: table.sym_var("game_8033B258",  "u32",  flag=table.GLOBL),
    0x8033B25C: table.sym_var("game_8033B25C",  "s16",  flag=table.GLOBL), # unused
    0x8033B25E: table.sym_var("game_8033B25E",  "s8",   flag=table.GLOBL),
    0x8033B260: table.sym_var("hud",            "HUD",  flag=table.GLOBL|ultra.BALIGN),
    0x8033B26E: table.sym_var("game_8033B26E",  "s8",   flag=table.GLOBL),

    # src/pl_collision.c
    0x8033B270: table.sym_var("pl_collision_8033B270",  "u8",   flag=table.GLOBL),
    0x8033B272: table.sym_var("pl_collision_8033B272",  "s16",  flag=table.GLOBL),

    # src/player.c
    0x8033B280: table.sym_var("player_8033B280",    "s32", flag=table.GLOBL),

    # src/pl_physics.c
    0x8033B290: table.sym_var("pl_physics_8033B290",    "s32", flag=table.GLOBL), # unused

    # src/pl_demo.c
    0x8033B2A0: table.sym_var("pl_demo_8033B2A0",   "OBJECT *", flag=table.GLOBL),
    0x8033B2A4: table.sym_var("pl_demo_8033B2A4",   "OBJECT *", flag=table.GLOBL),
    0x8033B2A8: table.sym_var("pl_demo_8033B2A8",   "OBJECT *", flag=table.GLOBL),
    0x8033B2AC: table.sym_var("pl_demo_8033B2AC",   "OBJECT *", flag=table.GLOBL),
    0x8033B2B0: table.sym_var("pl_demo_8033B2B0",   "OBJECT *", flag=table.GLOBL),
    0x8033B2B4: table.sym_var("pl_demo_8033B2B4",   "OBJECT *", flag=table.GLOBL), # unused
    0x8033B2B8: table.sym_var("pl_demo_8033B2B8",   "s16",  flag=table.GLOBL),
    0x8033B2BC: table.sym_var("pl_demo_8033B2BC",   "s16", "[2]",   table.GLOBL),

    # src/pl_walk.c
    0x8033B2C0: table.sym_var("pl_walk_8033B2C0", "mtxf", "[2]",  table.GLOBL),

    # src/pl_swim.c
    0x8033B340: table.sym_var("pl_swim_8033B340",   "s16",  flag=table.GLOBL),
    0x8033B342: table.sym_var("pl_swim_8033B342",   "s16",  flag=table.GLOBL),
    0x8033B344: table.sym_var("pl_swim_8033B344",   "f32",  flag=table.GLOBL),

    # src/pl_callback.c
    0x8033B350: table.sym_var("shape_object_mirror",    "SHAPE_OBJECT", flag=table.GLOBL|ultra.BALIGN),
    0x8033B3B0: table.sym_var("pl_shape_table", "PL_SHAPE", "[2]", table.GLOBL|ultra.BALIGN),

    # src/mem.c
    0x8033B400: table.sym_var("segment_table",  "uintptr_t", "[0x20]",  table.GLOBL|ultra.BALIGN),
    0x8033B480: table.sym_var("mem_size",       "size_t",   flag=table.GLOBL),
    0x8033B484: table.sym_var("mem_start",      "u8 *",     flag=table.GLOBL),
    0x8033B488: table.sym_var("mem_end",        "u8 *",     flag=table.GLOBL),
    0x8033B48C: table.sym_var("mem_l",          "MEM_LINK *",    flag=table.GLOBL),
    0x8033B490: table.sym_var("mem_r",          "MEM_LINK *",    flag=table.GLOBL),
    0x8033B494: table.sym_var("mem_heap",       "HEAP *",        flag=table.GLOBL),

    # src/save.c
    0x8033B4A0: table.sym_var("save_8033B4A0",  "u8",   flag=table.GLOBL),
    0x8033B4A1: table.sym_var("save_8033B4A1",  "u8",   flag=table.GLOBL),
    0x8033B4A2: table.sym_var("save_8033B4A2",  "u8",   flag=table.GLOBL),
    0x8033B4A3: table.sym_var("save_8033B4A3",  "u8",   flag=table.GLOBL),
    0x8033B4A4: table.sym_var("save_8033B4A4",  "u8",   flag=table.GLOBL),
    0x8033B4A5: table.sym_var("save_8033B4A5",  "s8",   flag=table.GLOBL),
    0x8033B4A6: table.sym_var("save_8033B4A6",  "s8",   flag=table.GLOBL),

    # src/scene.c
    0x8033B4B0: table.sym_var("spawn_player",       "SPAWN",    "[1]",     table.GLOBL|ultra.BALIGN),
    0x8033B4D0: table.sym_var("shape_data",         "SHAPE *",  "[0x100]", table.GLOBL|ultra.BALIGN),
    0x8033B8D0: table.sym_var("scene_data",         "SCENE",    "[8]",     table.GLOBL|ultra.BALIGN),
    0x8033BAB0: table.sym_var("wipe",               "WIPE", flag=table.GLOBL|ultra.BALIGN),
    0x8033BAC6: table.sym_var("course_index",       "s16",  flag=table.GLOBL),
    0x8033BAC8: table.sym_var("level_index",        "s16",  flag=table.GLOBL),
    0x8033BACA: table.sym_var("scene_index",        "s16",  flag=table.GLOBL),
    0x8033BACC: table.sym_var("course_prev",        "s16",  flag=table.GLOBL),
    0x8033BACE: table.sym_var("scene_msg_code",     "s16",  flag=table.GLOBL),
    0x8033BAD0: table.sym_var("scene_msg_prev",     "s16",  flag=table.GLOBL),

    # src/shape_draw.c
    0x8033BAE0: table.sym_var("shape_mtx_index",            "s16",  flag=table.GLOBL),
    0x8033BAE8: table.sym_var("shape_mf_stack",             "mtxf",  "[32]",    table.GLOBL|ultra.BALIGN),
    0x8033C2E8: table.sym_var("shape_mtx_stack",            "Mtx *", "[32]",    table.GLOBL|ultra.BALIGN),
    0x8033C368: table.sym_var("shape_joint_type_prev",      "u8",   flag=table.GLOBL),
    0x8033C369: table.sym_var("shape_joint_shadow_prev",    "u8",   flag=table.GLOBL),
    0x8033C36A: table.sym_var("shape_joint_frame_prev",     "s16",  flag=table.GLOBL),
    0x8033C36C: table.sym_var("shape_joint_scale_prev",     "f32",  flag=table.GLOBL),
    0x8033C370: table.sym_var("shape_joint_tbl_prev",       "u16 *",    flag=table.GLOBL),
    0x8033C374: table.sym_var("shape_joint_val_prev",       "s16 *",    flag=table.GLOBL),
    0x8033C378: table.sym_var("shape_joint_type",           "u8",   flag=table.GLOBL),
    0x8033C379: table.sym_var("shape_joint_shadow",         "u8",   flag=table.GLOBL),
    0x8033C37A: table.sym_var("shape_joint_frame",          "s16",  flag=table.GLOBL),
    0x8033C37C: table.sym_var("shape_joint_scale",          "f32",  flag=table.GLOBL),
    0x8033C380: table.sym_var("shape_joint_tbl",            "u16 *",    flag=table.GLOBL),
    0x8033C384: table.sym_var("shape_joint_val",            "s16 *",    flag=table.GLOBL),
    0x8033C388: table.sym_var("shape_draw_arena",           "ARENA *",  flag=table.GLOBL),

    # src/time.c
    0x8033C390: table.sym_var("time",   "TIME", "[2]",   table.GLOBL|ultra.BALIGN),

    # 0x8033C520 camera
    0x8033C520: table.sym("_camera_bss+0x00"), # la
    0x8033C544: table.sym("_camera_bss+0x24"), # data
    0x8033C568: table.sym("_camera_bss+0x48"), # la
    0x8033C578: table.sym("_camera_bss+0x58"), # la
    0x8033C588: table.sym("_camera_bss+0x68"), # la
    0x8033C594: table.sym("_camera_bss+0x74"),
    0x8033C596: table.sym("_camera_bss+0x76"),
    0x8033C598: table.sym("_camera_bss+0x78"),
    0x8033C5A0: table.sym("_camera_bss+0x80"),
    0x8033C5A4: table.sym("_camera_bss+0x84"),
    0x8033C5A8: table.sym("_camera_bss+0x88"),
    0x8033C5AC: table.sym("_camera_bss+0x8C"),
    0x8033C5B0: table.sym("_camera_bss+0x90"),
    0x8033C5B4: table.sym("_camera_bss+0x94"),
    0x8033C5B6: table.sym("_camera_bss+0x96"),
    0x8033C5B8: table.sym("_camera_bss+0x98"),
    0x8033C5C0: table.sym("_camera_bss+0xA0"),
    0x8033C5C2: table.sym("_camera_bss+0xA2"),
    0x8033C5C4: table.sym("_camera_bss+0xA4"),
    0x8033C5C8: table.sym("_camera_bss+0xA8"),
    0x8033C5CA: table.sym("_camera_bss+0xAA"),
    0x8033C5CC: table.sym("_camera_bss+0xAC"),
    0x8033C5D0: table.sym("_camera_bss+0xB0"),
    0x8033C5D2: table.sym("_camera_bss+0xB2"),
    0x8033C5D4: table.sym("_camera_bss+0xB4"),
    0x8033C5E8: table.sym("_camera_bss+0xC8"),
    0x8033C5EC: table.sym("_camera_bss+0xCC"),
    0x8033C5F0: table.sym("_camera_bss+0xD0"),
    0x8033C5F4: table.sym("_camera_bss+0xD4"),
    0x8033C5F8: table.sym("_camera_bss+0xD8"),
    0x8033C5FC: table.sym("_camera_bss+0xDC"),
    0x8033C600: table.sym("_camera_bss+0xE0"),
    0x8033C604: table.sym("_camera_bss+0xE4"),
    0x8033C608: table.sym("_camera_bss+0xE8"),
    0x8033C60C: table.sym("_camera_bss+0xEC"),
    0x8033C610: table.sym("_camera_bss+0xF0"),
    0x8033C614: table.sym("_camera_bss+0xF4"),
    0x8033C61C: table.sym("_camera_bss+0xFC"),
    0x8033C61E: table.sym("_camera_bss+0xFE"),
    0x8033C620: table.sym("_camera_bss+0x100"),
    0x8033C622: table.sym("_camera_bss+0x102"),
    0x8033C624: table.sym("_camera_bss+0x104"),
    0x8033C628: table.sym("_camera_bss+0x108"),
    0x8033C630: table.sym("_camera_bss+0x110"),
    0x8033C632: table.sym("_camera_bss+0x112"),
    0x8033C634: table.sym("_camera_bss+0x114"),
    0x8033C668: table.sym("_camera_bss+0x148"),
    0x8033C66C: table.sym("_camera_bss+0x14C"),
    0x8033C670: table.sym("_camera_bss+0x150"),
    0x8033C674: table.sym("_camera_bss+0x154"),
    0x8033C676: table.sym("_camera_bss+0x156"),
    0x8033C678: table.sym("_camera_bss+0x158"),
    0x8033C67C: table.sym("_camera_bss+0x15C"),
    0x8033C680: table.sym("_camera_bss+0x160"),
    0x8033C684: table.sym("_camera_bss+0x164"),
    0x8033C686: table.sym("_camera_bss+0x166"),
    0x8033C688: table.sym("_camera_bss+0x168"),
    0x8033C68A: table.sym("_camera_bss+0x16A"),
    0x8033C68C: table.sym("_camera_bss+0x16C"),
    0x8033C68E: table.sym("_camera_bss+0x16E"),
    0x8033C690: table.sym("_camera_bss+0x170"),
    0x8033C698: table.sym("_camera_bss+0x178"), # la
    0x8033C6D4: table.sym("_camera_bss+0x1B4"),
    0x8033C6D5: table.sym("_camera_bss+0x1B5"),
    0x8033C6F0: table.sym("_camera_bss+0x1D0"),
    0x8033C6F2: table.sym("_camera_bss+0x1D2"),
    0x8033C6F4: table.sym("_camera_bss+0x1D4"),
    0x8033C712: table.sym("_camera_bss+0x1F2"),
    0x8033C714: table.sym("_camera_bss+0x1F4"),
    0x8033C716: table.sym("_camera_bss+0x1F6"),
    0x8033C730: table.sym("_camera_bss+0x210"),
    0x8033C732: table.sym("_camera_bss+0x212"),
    0x8033C734: table.sym("_camera_bss+0x214"),
    0x8033C736: table.sym("_camera_bss+0x216"),
    0x8033C738: table.sym("_camera_bss+0x218"),
    0x8033C73A: table.sym("_camera_bss+0x21A"),
    0x8033C73C: table.sym("_camera_bss+0x21C"),
    0x8033C740: table.sym("_camera_bss+0x220"),
    0x8033C744: table.sym("_camera_bss+0x224"),
    0x8033C748: table.sym("_camera_bss+0x228"),
    0x8033C74C: table.sym("_camera_bss+0x22C"),
    0x8033C750: table.sym("_camera_bss+0x230"),
    0x8033C754: table.sym("_camera_bss+0x234"),
    0x8033C75A: table.sym("_camera_bss+0x23A"),
    0x8033C75C: table.sym("_camera_bss+0x23C"),
    0x8033C75E: table.sym("_camera_bss+0x23E"),
    0x8033C760: table.sym("_camera_bss+0x240"),
    0x8033C764: table.sym("_camera_bss+0x244"),
    0x8033C768: table.sym("_camera_bss+0x248"),
    0x8033C76A: table.sym("_camera_bss+0x24A"),
    0x8033C76C: table.sym("_camera_bss+0x24C"),
    0x8033C770: table.sym("_camera_bss+0x250"),
    0x8033C772: table.sym("_camera_bss+0x252"),
    0x8033C774: table.sym("_camera_bss+0x254"),
    0x8033C776: table.sym("_camera_bss+0x256"),
    0x8033C778: table.sym("_camera_bss+0x258"),
    0x8033C77C: table.sym("_camera_bss+0x25C"),
    0x8033C780: table.sym("_camera_bss+0x260"),
    0x8033C788: table.sym("_camera_bss+0x268"),
    0x8033C78A: table.sym("_camera_bss+0x26A"),
    0x8033C78C: table.sym("_camera_bss+0x26C"),
    0x8033C78E: table.sym("_camera_bss+0x26E"),
    0x8033C7A8: table.sym("_camera_bss+0x288"),
    0x8033C7AE: table.sym("_camera_bss+0x28E"),
    0x8033C7D0: table.sym("_camera_bss+0x2B0"), # la
    0x8033C7DC: table.sym("_camera_bss+0x2BC"),
    0x8033C7E0: table.sym("_camera_bss+0x2C0"),
    0x8033C7E8: table.sym("_camera_bss+0x2C8"), # la
    0x8033C808: table.sym("_camera_bss+0x2E8"), # la
    0x8033C828: table.sym("_camera_bss+0x308"), # la
    0x8033C840: table.sym("_camera_bss+0x320"),
    0x8033C844: table.sym("_camera_bss+0x324"),
    0x8033C848: table.sym("_camera_bss+0x328"),
    0x8033C84A: table.sym("_camera_bss+0x32A"),
    0x8033C850: table.sym("_camera_bss+0x330"),
    0x8033C950: table.sym("_camera_bss+0x430"),
    0x8033CA50: table.sym("_camera_bss+0x530"),
    0x8033CA54: table.sym("_camera_bss+0x534"),
    0x8033CA58: table.sym("_camera_bss+0x538"),
    0x8033CA5A: table.sym("_camera_bss+0x53A"),
    0x8033CA5C: table.sym("_camera_bss+0x53C"),
    0x8033CA60: table.sym("_camera_bss+0x540"),
    0x8033CA82: table.sym("_camera_bss+0x562"),
    0x8033CBC8: table.sym("_camera_bss+0x6A8"),
    0x8033CBCC: table.sym("_camera_bss+0x6AC"),
    0x8033CBD0: table.sym("_camera_bss+0x6B0"),

    # src/object.c
    0x8033CBE0: table.sym_var("obj_list_data",      "OBJ_LIST", "[16]",  table.GLOBL|ultra.BALIGN),
    0x8033D260: table.sym_var("object_debug_flag",  "u32",  flag=table.GLOBL),
    0x8033D264: table.sym_var("object_8033D264",    "int",  flag=table.GLOBL), # "NULLBG"
    0x8033D268: table.sym_var("object_8033D268",    "int",  flag=table.GLOBL), # unused
    0x8033D26C: table.sym_var("object_8033D26C",    "int",  flag=table.GLOBL), # "WALL"
    0x8033D270: table.sym_var("object_8033D270",    "int",  flag=table.GLOBL), # "obj"
    0x8033D274: table.sym_var("object_8033D274",    "struct struct_8033D274",   flag=table.GLOBL), # no balign?
    0x8033D280: table.sym_var("object_8033D280",    "s16", "[16][8]", table.GLOBL|ultra.BALIGN),
    0x8033D380: table.sym_var("object_8033D380",    "s16", "[16][8]", table.GLOBL|ultra.BALIGN),
    0x8033D480: table.sym_var("object_8033D480",    "int",  flag=table.GLOBL), # obj freeze
    0x8033D488: table.sym_var("object_data",        "OBJECT", "[240]",   table.GLOBL|ultra.BALIGN),
    0x80360E88: table.sym_var("object_dummy",       "OBJECT",            flag=table.GLOBL|ultra.BALIGN),
    0x803610E8: table.sym_var("obj_list",           "OBJ_LIST *",    flag=table.GLOBL),
    0x803610F0: table.sym_var("obj_list_free",      "OBJ_LIST",      flag=table.GLOBL|ultra.BALIGN),
    0x80361158: table.sym_var("object_mario",       "OBJECT *",  flag=table.GLOBL),
    0x8036115C: table.sym_var("object_luigi",       "OBJECT *",  flag=table.GLOBL),
    0x80361160: table.sym_var("object",             "OBJECT *",  flag=table.GLOBL),
    0x80361164: table.sym_var("object_pc",          "O_SCRIPT *",   flag=table.GLOBL),
    0x80361168: table.sym_var("object_80361168",    "s16",  flag=table.GLOBL), # prev "obj"
    0x8036116C: table.sym_var("object_8036116C",    "int",  flag=table.GLOBL), # movebg alloc
    0x80361170: table.sym_var("object_80361170",    "int",  flag=table.GLOBL), # movebg alloc
    0x80361174: table.sym_var("object_80361174",    "int",  flag=table.GLOBL), # statbg alloc
    0x80361178: table.sym_var("object_80361178",    "int",  flag=table.GLOBL), # statbg alloc
    0x8036117C: table.sym_var("object_heap",        "HEAP *",   flag=table.GLOBL),
    0x80361180: table.sym_var("object_80361180",    "s16",  flag=table.GLOBL),
    0x80361182: table.sym_var("object_80361182",    "s16",  flag=table.GLOBL),
    0x80361184: table.sym_var("object_80361184",    "void *",   flag=table.GLOBL), # type
    0x80361188: table.sym_var("object_80361188",    "int", "[20]",      table.GLOBL|ultra.BALIGN),
    0x803611D8: table.sym_var("object_803611D8",    "s8", "[60][2]",    table.GLOBL|ultra.BALIGN),
    0x80361250: table.sym_var("object_80361250",    "s16",  flag=table.GLOBL),
    0x80361252: table.sym_var("object_80361252",    "s16",  flag=table.GLOBL),
    0x80361254: table.sym_var("object_80361254",    "s16",  flag=table.GLOBL),
    0x80361256: table.sym_var("object_80361256",    "s16",  flag=table.GLOBL),
    0x80361258: table.sym_var("object_80361258",    "s16",  flag=table.GLOBL),
    0x8036125A: table.sym_var("object_8036125A",    "s16",  flag=table.GLOBL),
    0x8036125C: table.sym_var("object_8036125C",    "s16",  flag=table.GLOBL),
    0x8036125E: table.sym_var("object_8036125E",    "s16",  flag=table.GLOBL),
    0x80361260: table.sym_var("object_80361260",    "s16",  flag=table.GLOBL),
    0x80361262: table.sym_var("object_80361262",    "s16",  flag=table.GLOBL),
    0x80361264: table.sym_var("object_80361264",    "s16",  flag=table.GLOBL),

    # src/obj_lib.c
    0x80361270: table.sym_var("obj_lib_80361270",   "s32",  flag=table.GLOBL),

    # src/object_a.c
    0x80361280: table.sym_var("object_a_80361280",  "s16",  flag=table.GLOBL),

    # src/obj_debug.c
    0x80361290: table.sym_var("obj_debug_80361290", "OBJ_DEBUG",  flag=table.GLOBL|ultra.BALIGN),
    0x803612A0: table.sym_var("obj_debug_803612A0", "OBJ_DEBUG",  flag=table.GLOBL|ultra.BALIGN),

    # src/shadow.c
    0x803612B0: table.sym_var("shadow_803612B0",    "s8",   flag=table.GLOBL),
    0x803612B2: table.sym_var("shadow_803612B2",    "s16",  flag=table.GLOBL),
    0x803612B4: table.sym_var("shadow_803612B4",    "s8",   flag=table.GLOBL),
    0x803612B5: table.sym_var("shadow_803612B5",    "s8",   flag=table.GLOBL),

    # src/background.c
    0x803612C0: table.sym_var("background_803612C0",    "struct struct_803612C0", "[2]",    table.GLOBL),

    # src/scroll.c
    0x803612E0: table.sym_var("scroll_803612E0",    "s16",  flag=table.GLOBL),

    # src/obj_shape.c
    0x803612F0: table.sym_var("obj_shape_803612F0", "s8", flag=table.GLOBL),

    # src/ripple.c
    0x80361300: table.sym_var("ripple_80361300",    "s16",      flag=table.GLOBL),
    0x80361304: table.sym_var("ripple_80361304",    "f32",      flag=table.GLOBL),
    0x80361308: table.sym_var("ripple_80361308",    "f32",      flag=table.GLOBL),
    0x8036130C: table.sym_var("ripple_8036130C",    "f32",      flag=table.GLOBL),
    0x80361310: table.sym_var("ripple_80361310",    "s16 *",    flag=table.GLOBL),
    0x80361314: table.sym_var("ripple_80361314",    "f32 *",    flag=table.GLOBL),
    0x80361318: table.sym_var("ripple_80361318",    "RIPPLE *", flag=table.GLOBL),
    0x8036131C: table.sym_var("ripple_8036131C",    "s8",       flag=table.GLOBL),

    # src/dprint.c
    0x80361320: table.sym_var("dprint_table",   "DPRINT *", "[50]",   table.GLOBL|ultra.BALIGN),

    # src/message.c
    0x803613F0: table.sym_var("message_803613F0",   "s16",  flag=table.GLOBL),
    0x803613F2: table.sym_var("message_803613F2",   "s8",   flag=table.GLOBL),
    0x803613F4: table.sym_var("message_803613F4",   "s32",  flag=table.GLOBL),
    0x803613F8: table.sym_var("message_803613F8",   "u16",  flag=table.GLOBL),
    0x803613FA: table.sym_var("message_803613FA",   "s16",  flag=table.GLOBL),
    0x803613FC: table.sym_var("message_803613FC",   "s16",  flag=table.GLOBL),
    0x803613FE: table.sym_var("message_803613FE",   "s8",   flag=table.GLOBL),

    # src/weather_snow.c
    0x80361400: table.sym_var("weather_snow",          "struct weather *",  flag=table.GLOBL),
    0x80361408: table.sym_var("weather_snow_80361408", "s32", "[3]",   table.GLOBL|ultra.BALIGN),
    0x80361414: table.sym_var("weather_snow_80361414", "s16",          flag=table.GLOBL),
    0x80361416: table.sym_var("weather_snow_80361416", "s16",          flag=table.GLOBL),

    # src/weather_lava.c
    0x80361420: table.sym_var("weather_lava_80361420", "s16", "[10]",  table.GLOBL|ultra.BALIGN),
    0x80361434: table.sym_var("gfx_weather_lava",      "Gfx *",        flag=table.GLOBL),
    0x80361438: table.sym_var("weather_lava_80361438", "s32",          flag=table.GLOBL),
    0x8036143C: table.sym_var("weather_lava_8036143C", "s32",          flag=table.GLOBL),

    # src/hud.c
    0x80361440: table.sym_var("hud_80361440",   "s16",  flag=table.GLOBL),

    # src/object_b.c
    0x80361450: table.sym_var("object_b_80361450",  "MAP_FACE *",   flag=table.GLOBL),

    # src/object_c.c
    0x80361460: table.sym_var("object_c_80361460",  "s32", flag=table.GLOBL),
    0x80361464: table.sym_var("object_c_80361464",  "s32", flag=table.GLOBL),
    0x80361468: table.sym_var("object_c_80361468",  "f32", flag=table.GLOBL),
    0x8036146C: table.sym_var("object_c_8036146C",  "f32", flag=table.GLOBL),
    0x80361470: table.sym_var("object_c_80361470",  "f32", flag=table.GLOBL),
    0x80361474: table.sym_var("object_c_80361474",  "OBJECT *", flag=table.GLOBL),
    0x80361478: table.sym_var("object_c_80361478",  "s32", flag=table.GLOBL),
    0x8036147C: table.sym_var("object_c_8036147C",  "f32", flag=table.GLOBL),
    0x80361480: table.sym_var("object_c_80361480",  "f32", flag=table.GLOBL),
    0x80361484: table.sym_var("object_c_80361484",  "f32", flag=table.GLOBL),
    0x80361488: table.sym_var("object_c_80361488",  "OBJECT *", flag=table.GLOBL),

    # 0x80361490 audio/g
    0x80361490: table.sym("_Na_g_bss+0x00"),
    0x80361498: table.sym("_Na_g_bss+0x08"), # la
    0x80361C98: table.sym("_Na_g_bss+0x808"), # la
    0x80361F98: table.sym("_Na_g_bss+0xB08"),
    0x80361FA8: table.sym("_Na_g_bss+0xB18"),
    0x80361FB8: table.sym("_Na_g_bss+0xB28"), # la
    0x80361FCC: table.sym("_Na_g_bss+0xB3C"),
    0x80364B78: table.sym("_Na_g_bss+0x36E8"),
    0x80364B82: table.sym("_Na_g_bss+0x36F2"),
    0x80364B83: table.sym("_Na_g_bss+0x36F3"),
    0x80364B88: table.sym("_Na_g_bss+0x36F8"),

    # 0x80364BA0

    # ==========================================================================
    # buffer
    # ==========================================================================

    # src/zimg.c
    0x80000400: table.sym_var("depth_buffer",   "u16", "[SCREEN_HT][SCREEN_WD]",    table.GLOBL|ultra.BALIGN),

    # src/timg.c
    0x801C1000: table.sym_var("texture_buffer", "u16", "[13][2048]",    table.GLOBL|ultra.BALIGN),

    # src/audio/heap.c
    0x801CE000: table.sym_var("Na_heap",        "u64", "[0x32200/sizeof(u64)]", table.GLOBL|ultra.BALIGN),

    # src/buffer.c
    0x80200200: table.sym_var("stack_main",     "u64", "[0x400/sizeof(u64)]",               table.GLOBL|ultra.BALIGN),
    0x80200600: table.sym_var("stack_idle",     "u64", "[0x800/sizeof(u64)]",               table.GLOBL|ultra.BALIGN),
    0x80200E00: table.sym_var("stack_sc",       "u64", "[0x2000/sizeof(u64)]",              table.GLOBL|ultra.BALIGN),
    0x80202E00: table.sym_var("stack_audio",    "u64", "[0x2000/sizeof(u64)]",              table.GLOBL|ultra.BALIGN),
    0x80204E00: table.sym_var("stack_app",      "u64", "[0x2000/sizeof(u64)]",              table.GLOBL|ultra.BALIGN),
    0x80206E00: table.sym_var("video_yield",    "u64", "[OS_YIELD_DATA_SIZE/sizeof(u64)]",  table.GLOBL|ultra.BALIGN),
    0x80207700: table.sym_var("save",           "u64", "[0x200/sizeof(u64)]",               table.GLOBL|ultra.BALIGN),
    0x80207900: table.sym_var("video_stack",    "u64", "[SP_DRAM_STACK_SIZE64]",            table.GLOBL|ultra.BALIGN),
    0x80207D00: table.sym_var("video_table",    "VIDEO", "[2]",                             table.GLOBL|ultra.BALIGN),

    # src/audio/bss.c
    # 0x80220DA0 (max 0x6260)

    # src/fifo.c
    0x80227000: table.sym_var("fifo_buffer",    "u64", "[FIFO_SIZE/sizeof(u64)]", table.GLOBL|ultra.BALIGN),

    # src/cimg.c
    0x8038F800: table.sym_var("colour_buffer_a",    "u16", "[SCREEN_HT][SCREEN_WD]",    table.GLOBL|ultra.BALIGN),
    0x803B5000: table.sym_var("colour_buffer_b",    "u16", "[SCREEN_HT][SCREEN_WD]",    table.GLOBL|ultra.BALIGN),
    0x803DA800: table.sym_var("colour_buffer_c",    "u16", "[SCREEN_HT][SCREEN_WD]",    table.GLOBL|ultra.BALIGN),

    # scroll fix
    0x07001000: table.sym("(void *)0x07001000"),
}

dev_E0_d_main = {
    0x80330F00: 0x002AC6B0,
    0x80330F04: 0x002D0040,
    0x80330F08: 0x002D64F0,
    0x80330F0C: 0x002E7880,
    0x80330F10: 0x002B8F10,
    0x80330F14: 0x002F14E0,
    0x80330F18: 0x002FB1B0,
    0x80330F1C: 0x00301CD0,
    0x80330F20: 0x002C73D0,
    0x80330F24: 0x0030CEC0,
}

sym_E0_t_main2 = {
    0x000F5580: table.sym("_main2SegmentRomStart"),
    0x00108A10: table.sym("_main2SegmentRomEnd"),

    # ==========================================================================
    # text
    # ==========================================================================

    # src/math.c
    0x80378800: table.sym_fnc("vecf_cpy", "vecf *", (
        "vecf dst",
        "const vecf src",
    ), table.GLOBL),
    0x80378840: table.sym_fnc("vecf_set", "vecf *", (
        "vecf vf",
        "f32 x",
        "f32 y",
        "f32 z",
    ), table.GLOBL),
    0x8037888C: table.sym_fnc("vecf_add", "vecf *", (
        "vecf vf",
        "const vecf a",
    ), table.GLOBL),
    0x803788E4: table.sym_fnc("vecf_addto", "vecf *", (
        "vecf vf",
        "const vecf a",
        "const vecf b",
    ), table.GLOBL), # unused
    0x8037893C: table.sym_fnc("vecs_cpy", "vecs *", (
        "vecs dst",
        "const vecs src",
    ), table.GLOBL),
    0x8037897C: table.sym_fnc("vecs_set", "vecs *", (
        "vecs vs",
        "s16 x",
        "s16 y",
        "s16 z",
    ), table.GLOBL),
    0x803789C8: table.sym_fnc("vecs_add", "vecs *", (
        "vecs vs",
        "const vecs a",
    ), table.GLOBL), # unused
    0x80378A20: table.sym_fnc("vecs_addto", "vecs *", (
        "vecs vs",
        "const vecs a",
        "const vecs b",
    ), table.GLOBL), # unused
    0x80378A78: table.sym_fnc("vecs_sub", "vecs *", (
        "vecs vs",
        "const vecs a",
    ), table.GLOBL), # unused
    0x80378AD0: table.sym_fnc("vecf_vecs", "vecf *", (
        "vecf dst",
        "const vecs src",
    ), table.GLOBL),
    0x80378B34: table.sym_fnc("vecs_vecf", "vecs *", (
        "vecs dst",
        "const vecf src",
    ), table.GLOBL),
    0x80378C50: table.sym_fnc("vecf_normal", "vecf *", (
        "vecf vf",
        "const vecf v0",
        "const vecf v1",
        "const vecf v2",
    ), table.GLOBL), # static
    0x80378D38: table.sym_fnc("vecf_cross", "vecf *", (
        "vecf vf",
        "const vecf a",
        "const vecf b",
    ), table.GLOBL), # static
    0x80378DC0: table.sym_fnc("vecf_normalise", "vecf *", (
        "vecf vf",
    ), table.GLOBL), # static
    0x80378E68: table.sym_fnc("mtxf_cpy", arg=(
        "mtxf dst",
        "const mtxf src",
    ), flag=table.GLOBL),
    0x80378EB4: table.sym_fnc("mtxf_identity", arg=(
        "mtxf mf",
    ), flag=table.GLOBL),
    0x80378F24: table.sym_fnc("mtxf_pos", arg=(
        "mtxf mf",
        "const vecf pos",
    ), flag=table.GLOBL),
    0x80378F84: table.sym_fnc("mtxf_lookat", arg=(
        "mtxf mf",
        "const vecf eye",
        "const vecf look",
        "s16 rz",
    ), flag=table.GLOBL),
    0x80379440: table.sym_fnc("mtxf_posrot", arg=(
        "mtxf mf",
        "const vecf pos",
        "const vecs rot",
    ), flag=table.GLOBL),
    0x803795F0: table.sym_fnc("mtxf_joint", arg=(
        "mtxf mf",
        "const vecf pos",
        "const vecs rot",
    ), flag=table.GLOBL),
    0x80379798: table.sym_fnc("mtxf_billboard", arg=(
        "mtxf mf",
        "const mtxf view",
        "const vecf pos",
        "s16 rz",
    ), flag=table.GLOBL),
    0x80379918: table.sym_fnc("mtxf_stand", arg=(
        "mtxf mf",
        "const vecf normal",
        "const vecf pos",
        "s16 ry",
    ), flag=table.GLOBL),
    0x80379AA4: table.sym_fnc("mtxf_ground", arg=(
        "mtxf mf",
        "const vecf pos",
        "s16 ry",
        "f32 radius",
    ), flag=table.GLOBL),
    0x80379F60: table.sym_fnc("mtxf_af_mul", arg=(
        "mtxf mf",
        "const mtxf a",
        "const mtxf b",
    ), flag=table.GLOBL),
    0x8037A29C: table.sym_fnc("mtxf_scale", arg=(
        "mtxf dst",
        "const mtxf src",
        "const vecf scale",
    ), flag=table.GLOBL),
    0x8037A348: table.sym_fnc("mtxf_transform", arg=(
        "const mtxf mf",
        "vecs vs",
    ), flag=table.GLOBL), # unused
    0x8037A434: table.sym_fnc("mtx_mtxf", arg=(
        "Mtx *m",
        "const mtxf mf",
    ), flag=table.GLOBL),
    0x8037A4B8: table.sym_fnc("mtx_r_z", arg=(
        "Mtx *m",
        "s16 rz",
    ), flag=table.GLOBL),
    0x8037A550: table.sym_fnc("vecf_untransform", arg=(
        "vecf vf",
        "const mtxf mf",
        "const mtxf cam",
    ), flag=table.GLOBL),
    0x8037A69C: table.sym_fnc("cartesian_to_polar", arg=(
        "const vecf a",
        "const vecf b",
        "f32 *dist",
        "s16 *rx",
        "s16 *ry",
    ), flag=table.GLOBL),
    0x8037A788: table.sym_fnc("polar_to_cartesian", arg=(
        "vecf a",
        "vecf b",
        "f32 dist",
        "s16 rx",
        "s16 ry",
    ), flag=table.GLOBL),
    0x8037A860: table.sym_fnc("converge_i", "int", (
        "int x",
        "int dst",
        "int inc",
        "int dec",
    ), table.GLOBL),
    0x8037A8B4: table.sym_fnc("converge_f", "float", (
        "float x",
        "float dst",
        "float inc",
        "float dec",
    ), table.GLOBL),
    0x8037A924: table.sym_fnc("atan_yx", "u16", (
        "f32 x",
        "f32 y",
    )),
    0x8037A9A8: table.sym_fnc("atan2", "s16", (
        "f32 x",
        "f32 y",
    ), table.GLOBL),
    0x8037AB88: table.sym_fnc("atan2f", "f32", (
        "f32 x",
        "f32 y",
    ), table.GLOBL), # unused
    0x8037ABEC: table.sym_fnc("bspline_curve", arg=(
        "f32 dst[4]",
        "f32 phase",
        "unused int mode",
    )),
    0x8037AC74: table.sym_fnc("L8037AC74", flag=table.GLOBL|table.LOCAL),
    0x8037AD04: table.sym_fnc("L8037AD04", flag=table.GLOBL|table.LOCAL),
    0x8037ADC0: table.sym_fnc("L8037ADC0", flag=table.GLOBL|table.LOCAL),
    0x8037AE5C: table.sym_fnc("L8037AE5C", flag=table.GLOBL|table.LOCAL),
    0x8037AF18: table.sym_fnc("L8037AF18", flag=table.GLOBL|table.LOCAL),
    0x8037AFB8: table.sym_fnc("bspline_init", arg=(
        "const BSPLINE *b",
    ), flag=table.GLOBL),
    0x8037AFE8: table.sym_fnc("bspline_update", "int", (
        "vecf dst",
    ), table.GLOBL),

    # src/shape.c
    0x8037B220: table.sym("shape_8037B220"),
    0x8037B24C: table.sym("shape_8037B24C", table.GLOBL),
    0x8037B30C: table.sym("shape_8037B30C", table.GLOBL),
    0x8037B380: table.sym("shape_8037B380", table.GLOBL),
    0x8037B448: table.sym("shape_8037B448", table.GLOBL),
    0x8037B4AC: table.sym("shape_8037B4AC", table.GLOBL),
    0x8037B530: table.sym("shape_8037B530", table.GLOBL),
    0x8037B5B4: table.sym("shape_8037B5B4", table.GLOBL),
    0x8037B670: table.sym("shape_8037B670", table.GLOBL),
    0x8037B744: table.sym("shape_8037B744", table.GLOBL),
    0x8037B7F8: table.sym("shape_8037B7F8", table.GLOBL),
    0x8037B89C: table.sym("shape_8037B89C", table.GLOBL),
    0x8037B940: table.sym("shape_8037B940", table.GLOBL),
    0x8037B9E0: table.sym("shape_8037B9E0", table.GLOBL),
    0x8037BAD4: table.sym("shape_8037BAD4", table.GLOBL),
    0x8037BB48: table.sym("shape_8037BB48", table.GLOBL),
    0x8037BBEC: table.sym("shape_8037BBEC", table.GLOBL),
    0x8037BC90: table.sym("shape_8037BC90", table.GLOBL),
    0x8037BD24: table.sym("shape_8037BD24", table.GLOBL),
    0x8037BDB4: table.sym("shape_8037BDB4", table.GLOBL),
    0x8037BE28: table.sym("shape_8037BE28", table.GLOBL),
    0x8037BECC: table.sym("shape_8037BECC", table.GLOBL),
    0x8037BF84: table.sym("shape_8037BF84", table.GLOBL),
    0x8037C044: table.sym("shape_8037C044", table.GLOBL),
    0x8037C0BC: table.sym("shape_8037C0BC", table.GLOBL),
    0x8037C138: table.sym("shape_8037C138", table.GLOBL),
    0x8037C1E4: table.sym("shape_8037C1E4"),
    0x8037C360: table.sym("shape_8037C360", table.GLOBL),
    0x8037C3D0: table.sym("shape_8037C3D0", table.GLOBL),
    0x8037C448: table.sym("shape_8037C448", table.GLOBL),
    0x8037C51C: table.sym("shape_8037C51C", table.GLOBL),
    0x8037C658: table.sym("shape_8037C658", table.GLOBL),
    0x8037C708: table.sym("shape_8037C708", table.GLOBL),
    0x8037C7D8: table.sym("shape_8037C7D8", table.GLOBL),
    0x8037C844: table.sym("shape_8037C844", table.GLOBL),
    0x8037C9E8: table.sym("shape_8037C9E8"), # unused
    0x8037CB10: table.sym("shape_8037CB10"), # unused
    0x8037CB60: table.sym("shape_8037CB60", table.GLOBL),
    0x8037CBC0: table.sym("shape_8037CBC0", table.GLOBL),
    0x8037CBFC: table.sym("shape_8037CBFC", table.GLOBL),
    0x8037CC74: table.sym("shape_8037CC74", table.GLOBL),

    # src/s_script.c
    0x8037CD60: table.sym_fnc("s_cmd_script",       flag=table.GLOBL), # data
    0x8037CE24: table.sym_fnc("s_cmd_end",          flag=table.GLOBL), # data
    0x8037CEE8: table.sym_fnc("s_cmd_jump",         flag=table.GLOBL), # data
    0x8037CF70: table.sym_fnc("s_cmd_return",       flag=table.GLOBL), # data
    0x8037CFC0: table.sym_fnc("s_cmd_push",         flag=table.GLOBL), # data
    0x8037D018: table.sym_fnc("s_cmd_pull",         flag=table.GLOBL), # data
    0x8037D050: table.sym_fnc("s_cmd_store",        flag=table.GLOBL), # data
    0x8037D0D0: table.sym_fnc("s_cmd_flag",         flag=table.GLOBL), # data
    0x8037D1D0: table.sym_fnc("s_cmd_scene",        flag=table.GLOBL), # data
    0x8037D328: table.sym_fnc("s_cmd_ortho",        flag=table.GLOBL), # data
    0x8037D3A4: table.sym_fnc("s_cmd_persp",        flag=table.GLOBL), # data
    0x8037D48C: table.sym_fnc("s_cmd_empty",        flag=table.GLOBL), # data
    0x8037D4DC: table.sym_fnc("s_cmd_1F",           flag=table.GLOBL), # data
    0x8037D500: table.sym_fnc("s_cmd_layer",        flag=table.GLOBL), # data
    0x8037D55C: table.sym_fnc("s_cmd_lod",          flag=table.GLOBL), # data
    0x8037D5D4: table.sym_fnc("s_cmd_select",       flag=table.GLOBL), # data
    0x8037D640: table.sym_fnc("s_cmd_camera",       flag=table.GLOBL), # data
    0x8037D6F0: table.sym_fnc("s_cmd_posrot",       flag=table.GLOBL), # data
    0x8037D8D4: table.sym_fnc("s_cmd_pos",          flag=table.GLOBL), # data
    0x8037D998: table.sym_fnc("s_cmd_rot",          flag=table.GLOBL), # data
    0x8037DA5C: table.sym_fnc("s_cmd_scale",        flag=table.GLOBL), # data
    0x8037DB50: table.sym_fnc("s_cmd_1E",           flag=table.GLOBL), # data
    0x8037DB74: table.sym_fnc("s_cmd_joint",        flag=table.GLOBL), # data
    0x8037DC10: table.sym_fnc("s_cmd_billboard",    flag=table.GLOBL), # data
    0x8037DCD4: table.sym_fnc("s_cmd_gfx",          flag=table.GLOBL), # data
    0x8037DD4C: table.sym_fnc("s_cmd_shadow",       flag=table.GLOBL), # data
    0x8037DDDC: table.sym_fnc("s_cmd_object",       flag=table.GLOBL), # data
    0x8037DE34: table.sym_fnc("s_cmd_callback",     flag=table.GLOBL), # data
    0x8037DE94: table.sym_fnc("s_cmd_background",   flag=table.GLOBL), # data
    0x8037DEF8: table.sym_fnc("s_cmd_1A",           flag=table.GLOBL), # data
    0x8037DF1C: table.sym_fnc("s_cmd_load",         flag=table.GLOBL), # data
    0x8037DFD4: table.sym_fnc("s_cmd_hand",         flag=table.GLOBL), # data
    0x8037E058: table.sym_fnc("s_cmd_cull",         flag=table.GLOBL), # data
    0x8037E0B4: table.sym("s_script_main", table.GLOBL),

    # src/p_script.c
    0x8037E1A0: table.sym_fnc("p_script_cmp", "int", (
        "s8 cmp",
        "int x",
    )),
    0x8037E1D4: table.sym_fnc("L8037E1D4", flag=table.GLOBL|table.LOCAL),
    0x8037E1EC: table.sym_fnc("L8037E1EC", flag=table.GLOBL|table.LOCAL),
    0x8037E20C: table.sym_fnc("L8037E20C", flag=table.GLOBL|table.LOCAL),
    0x8037E228: table.sym_fnc("L8037E228", flag=table.GLOBL|table.LOCAL),
    0x8037E244: table.sym_fnc("L8037E244", flag=table.GLOBL|table.LOCAL),
    0x8037E25C: table.sym_fnc("L8037E25C", flag=table.GLOBL|table.LOCAL),
    0x8037E278: table.sym_fnc("L8037E278", flag=table.GLOBL|table.LOCAL),
    0x8037E290: table.sym_fnc("L8037E290", flag=table.GLOBL|table.LOCAL),
    0x8037E2C4: table.sym_fnc("p_cmd_push_call",    flag=table.GLOBL), # data
    0x8037E388: table.sym_fnc("p_cmd_push_jump",    flag=table.GLOBL), # data
    0x8037E404: table.sym_fnc("p_cmd_pull_return",  flag=table.GLOBL), # data
    0x8037E47C: table.sym_fnc("p_cmd_sleep",        flag=table.GLOBL), # data
    0x8037E4FC: table.sym_fnc("p_cmd_freeze",       flag=table.GLOBL), # data
    0x8037E580: table.sym_fnc("p_cmd_jump",         flag=table.GLOBL), # data
    0x8037E5B8: table.sym_fnc("p_cmd_call",         flag=table.GLOBL), # data
    0x8037E620: table.sym_fnc("p_cmd_return",       flag=table.GLOBL), # data
    0x8037E650: table.sym_fnc("p_cmd_for",          flag=table.GLOBL), # data
    0x8037E6D4: table.sym_fnc("p_cmd_done",         flag=table.GLOBL), # data
    0x8037E780: table.sym_fnc("p_cmd_do",           flag=table.GLOBL), # data
    0x8037E7F8: table.sym_fnc("p_cmd_while",        flag=table.GLOBL), # data
    0x8037E878: table.sym_fnc("p_cmd_if_jump",      flag=table.GLOBL), # data
    0x8037E8E8: table.sym_fnc("p_cmd_if_call",      flag=table.GLOBL), # data
    0x8037E988: table.sym_fnc("p_cmd_if",           flag=table.GLOBL), # data
    0x8037EA18: table.sym_fnc("p_cmd_else",         flag=table.GLOBL), # data
    0x8037EA70: table.sym_fnc("p_cmd_endif",        flag=table.GLOBL), # data
    0x8037EA98: table.sym_fnc("p_cmd_callback",     flag=table.GLOBL), # data
    0x8037EB04: table.sym_fnc("p_cmd_process",      flag=table.GLOBL), # data
    0x8037EB98: table.sym_fnc("p_cmd_set",          flag=table.GLOBL), # data
    0x8037EBD4: table.sym_fnc("p_cmd_push",         flag=table.GLOBL), # data
    0x8037EC14: table.sym_fnc("p_cmd_pull",         flag=table.GLOBL), # data
    0x8037EC54: table.sym_fnc("p_cmd_load_code",    flag=table.GLOBL), # data
    0x8037ECA4: table.sym_fnc("p_cmd_load_data",    flag=table.GLOBL), # data
    0x8037ECF8: table.sym_fnc("p_cmd_load_szp",     flag=table.GLOBL), # data
    0x8037ED48: table.sym_fnc("p_cmd_load_face",    flag=table.GLOBL), # data
    0x8037EDF8: table.sym_fnc("p_cmd_load_txt",     flag=table.GLOBL), # data
    0x8037EE48: table.sym_fnc("p_cmd_stage_init",   flag=table.GLOBL), # data
    0x8037EEA8: table.sym_fnc("p_cmd_stage_exit",   flag=table.GLOBL), # data
    0x8037EF00: table.sym_fnc("p_cmd_stage_start",  flag=table.GLOBL), # data
    0x8037EF70: table.sym_fnc("p_cmd_stage_end",    flag=table.GLOBL), # data
    0x8037F010: table.sym_fnc("p_cmd_scene_start",  flag=table.GLOBL), # data
    0x8037F130: table.sym_fnc("p_cmd_scene_end",    flag=table.GLOBL), # data
    0x8037F164: table.sym_fnc("p_cmd_shape_gfx",    flag=table.GLOBL), # data
    0x8037F214: table.sym_fnc("p_cmd_shape_script", flag=table.GLOBL), # data
    0x8037F2A4: table.sym_fnc("p_cmd_shape_scale",  flag=table.GLOBL), # data
    0x8037F36C: table.sym_fnc("p_cmd_player",       flag=table.GLOBL), # data
    0x8037F45C: table.sym_fnc("p_cmd_object",       flag=table.GLOBL), # data
    0x8037F67C: table.sym_fnc("p_cmd_link",         flag=table.GLOBL), # data
    0x8037F790: table.sym_fnc("p_cmd_connect",      flag=table.GLOBL), # data
    0x8037F920: table.sym_fnc("p_cmd_env",          flag=table.GLOBL), # data
    0x8037F994: table.sym_fnc("p_cmd_linkbg",       flag=table.GLOBL), # data
    0x8037FB18: table.sym_fnc("p_cmd_wind",         flag=table.GLOBL), # data
    0x8037FC38: table.sym_fnc("p_cmd_jet",          flag=table.GLOBL), # data
    0x8037FDE4: table.sym_fnc("p_cmd_vi_black",     flag=table.GLOBL), # data
    0x8037FE2C: table.sym_fnc("p_cmd_vi_gamma",     flag=table.GLOBL), # data
    0x8037FE94: table.sym_fnc("p_cmd_map",          flag=table.GLOBL), # data
    0x8037FF14: table.sym_fnc("p_cmd_area",         flag=table.GLOBL), # data
    0x8037FF94: table.sym_fnc("p_cmd_obj",          flag=table.GLOBL), # data
    0x80380014: table.sym_fnc("p_cmd_scene_open",   flag=table.GLOBL), # data
    0x8038007C: table.sym_fnc("p_cmd_scene_close",  flag=table.GLOBL), # data
    0x803800BC: table.sym_fnc("p_cmd_player_open",  flag=table.GLOBL), # data
    0x80380160: table.sym_fnc("p_cmd_player_close", flag=table.GLOBL), # data
    0x803801A0: table.sym_fnc("p_cmd_scene_update", flag=table.GLOBL), # data
    0x803801E0: table.sym_fnc("p_cmd_wipe",         flag=table.GLOBL), # data
    0x8038024C: table.sym_fnc("p_cmd_32",           flag=table.GLOBL), # data
    0x80380274: table.sym_fnc("p_cmd_msg",          flag=table.GLOBL), # data
    0x80380300: table.sym_fnc("p_cmd_bgm",          flag=table.GLOBL), # data
    0x8038039C: table.sym_fnc("p_cmd_bgm_play",     flag=table.GLOBL), # data
    0x803803EC: table.sym_fnc("p_cmd_bgm_stop",     flag=table.GLOBL), # data
    0x80380434: table.sym_fnc("p_cmd_var",          flag=table.GLOBL), # data
    0x80380478: table.sym_fnc("L80380478", flag=table.GLOBL|table.LOCAL),
    0x80380490: table.sym_fnc("L80380490", flag=table.GLOBL|table.LOCAL),
    0x803804A8: table.sym_fnc("L803804A8", flag=table.GLOBL|table.LOCAL),
    0x803804C0: table.sym_fnc("L803804C0", flag=table.GLOBL|table.LOCAL),
    0x803804D8: table.sym_fnc("L803804D8", flag=table.GLOBL|table.LOCAL),
    0x80380528: table.sym_fnc("L80380528", flag=table.GLOBL|table.LOCAL),
    0x80380540: table.sym_fnc("L80380540", flag=table.GLOBL|table.LOCAL),
    0x80380558: table.sym_fnc("L80380558", flag=table.GLOBL|table.LOCAL),
    0x80380570: table.sym_fnc("L80380570", flag=table.GLOBL|table.LOCAL),
    0x80380588: table.sym_fnc("L80380588", flag=table.GLOBL|table.LOCAL),
    0x803805C8: table.sym_fnc("p_script_main", "P_SCRIPT *", (
        "P_SCRIPT *pc",
    ), table.GLOBL),

    # src/map.c
    0x80380690: table.sym("map_80380690"),
    0x80380DE8: table.sym("map_80380DE8", table.GLOBL),
    0x80380E8C: table.sym("map_80380E8C", table.GLOBL),
    0x80381038: table.sym("map_80381038"),
    0x80381264: table.sym("map_80381264", table.GLOBL),
    0x80381470: table.sym("map_80381470"), # unused
    0x803814B8: table.sym("map_803814B8", table.GLOBL),
    0x8038156C: table.sym("map_8038156C"),
    0x80381794: table.sym("map_80381794", table.GLOBL),
    0x803817E0: table.sym("map_803817E0"), # unused
    0x80381900: table.sym("map_80381900", table.GLOBL),
    0x80381BA0: table.sym("map_80381BA0", table.GLOBL),
    0x80381D3C: table.sym("map_80381D3C", table.GLOBL),
    0x80381EC8: table.sym("map_80381EC8"),
    0x80381F08: table.sym("map_80381F08", table.GLOBL),
    0x80382294: table.sym("map_80382294"), # unused

    # src/map_data.c
    0x80382490: table.sym("map_data_80382490"),
    0x803824F8: table.sym("map_data_803824F8"),
    0x80382590: table.sym("map_data_80382590"),
    0x803825D0: table.sym("map_data_803825D0"),
    0x803825FC: table.sym("map_data_803825FC"),
    0x8038283C: table.sym("map_data_8038283C"),
    0x8038289C: table.sym("map_data_8038289C"),
    0x803828FC: table.sym("map_data_803828FC"),
    0x80382990: table.sym("map_data_80382990"),
    0x80382A2C: table.sym("map_data_80382A2C"),
    0x80382B6C: table.sym("map_data_80382B6C"), # unused
    0x80382B7C: table.sym("map_data_80382B7C"),
    0x80382F84: table.sym("map_data_80382F84"),
    0x80382FBC: table.sym_fnc("L80382FBC", flag=table.GLOBL|table.LOCAL),
    0x80382FCC: table.sym_fnc("L80382FCC", flag=table.GLOBL|table.LOCAL),
    0x80382FEC: table.sym("map_data_80382FEC"),
    0x80383068: table.sym("map_data_80383068"),
    0x803831D0: table.sym("map_data_803831D0"),
    0x80383228: table.sym("map_data_80383228"),
    0x80383340: table.sym("map_data_80383340", table.GLOBL),
    0x803833B8: table.sym("map_data_803833B8", table.GLOBL),
    0x803835A4: table.sym("map_data_803835A4", table.GLOBL),
    0x80383604: table.sym("map_data_80383604"), # unused
    0x80383614: table.sym("map_data_80383614"),
    0x80383828: table.sym("map_data_80383828"),
    0x803839CC: table.sym("map_data_803839CC", table.GLOBL), # o callback

    # src/o_script.c
    0x80383B70: table.sym("o_script_80383B70"), # unused
    0x80383BB0: table.sym("o_script_80383BB0", table.GLOBL),
    0x80383CB4: table.sym("o_script_80383CB4", table.GLOBL),
    0x80383D1C: table.sym("o_script_80383D1C", table.GLOBL),
    0x80383D68: table.sym("o_script_80383D68"),
    0x80383DBC: table.sym("o_script_80383DBC"),
    0x80383DF8: table.sym("o_script_80383DF8"),
    0x80383E44: table.sym("o_script_80383E44"), # unused
    0x80383E5C: table.sym_fnc("o_script_22", "int", flag=table.GLOBL), # data
    0x80383EA0: table.sym_fnc("o_script_35", "int", flag=table.GLOBL), # data
    0x80383EE4: table.sym_fnc("o_script_21", "int", flag=table.GLOBL), # data
    0x80383F24: table.sym_fnc("o_script_1B", "int", flag=table.GLOBL), # data
    0x80383F94: table.sym_fnc("o_script_1C", "int", flag=table.GLOBL), # data
    0x8038401C: table.sym_fnc("o_script_2C", "int", flag=table.GLOBL), # data
    0x803840B4: table.sym_fnc("o_script_29", "int", flag=table.GLOBL), # data
    0x80384164: table.sym_fnc("o_script_1D", "int", flag=table.GLOBL), # data
    0x80384188: table.sym_fnc("o_script_0A", "int", flag=table.GLOBL), # data
    0x803841A0: table.sym_fnc("o_script_0B", "int", flag=table.GLOBL), # data
    0x803841B8: table.sym_fnc("o_script_02", "int", flag=table.GLOBL), # data
    0x80384224: table.sym_fnc("o_script_03", "int", flag=table.GLOBL), # data
    0x8038425C: table.sym_fnc("o_script_01", "int", flag=table.GLOBL), # data
    0x803842E4: table.sym_fnc("o_script_25", "int", flag=table.GLOBL), # data
    0x8038438C: table.sym_fnc("o_script_04", "int", flag=table.GLOBL), # data
    0x803843E0: table.sym_fnc("o_script_26", "int", flag=table.GLOBL), # data
    0x80384450: table.sym_fnc("o_script_05", "int", flag=table.GLOBL), # data
    0x803844C0: table.sym_fnc("o_script_06", "int", flag=table.GLOBL), # data
    0x80384554: table.sym_fnc("o_script_07", "int", flag=table.GLOBL), # data
    0x803845E8: table.sym_fnc("o_script_08", "int", flag=table.GLOBL), # data
    0x80384634: table.sym_fnc("o_script_09", "int", flag=table.GLOBL), # data
    0x80384678: table.sym_fnc("o_script_0C", "int", flag=table.GLOBL), # data
    0x803846D0: table.sym_fnc("o_script_0E", "int", flag=table.GLOBL), # data
    0x8038475C: table.sym_fnc("o_script_10", "int", flag=table.GLOBL), # data
    0x803847D4: table.sym_fnc("o_script_36", "int", flag=table.GLOBL), # data
    0x80384854: table.sym_fnc("o_script_14", "int", flag=table.GLOBL), # data
    0x80384928: table.sym_fnc("o_script_15", "int", flag=table.GLOBL), # data
    0x803849F8: table.sym_fnc("o_script_13", "int", flag=table.GLOBL), # data
    0x80384AB4: table.sym_fnc("o_script_16", "int", flag=table.GLOBL), # data
    0x80384B90: table.sym_fnc("o_script_17", "int", flag=table.GLOBL), # data
    0x80384C5C: table.sym_fnc("o_script_0D", "int", flag=table.GLOBL), # data
    0x80384CF0: table.sym_fnc("o_script_0F", "int", flag=table.GLOBL), # data
    0x80384D70: table.sym_fnc("o_script_11", "int", flag=table.GLOBL), # data
    0x80384E04: table.sym_fnc("o_script_12", "int", flag=table.GLOBL), # data
    0x80384E9C: table.sym_fnc("o_script_27", "int", flag=table.GLOBL), # data
    0x80384F08: table.sym_fnc("o_script_28", "int", flag=table.GLOBL), # data
    0x80384F8C: table.sym_fnc("o_script_1E", "int", flag=table.GLOBL), # data
    0x8038503C: table.sym_fnc("o_script_18", "int", flag=table.GLOBL), # data
    0x80385084: table.sym_fnc("o_script_1A", "int", flag=table.GLOBL), # data
    0x803850CC: table.sym_fnc("o_script_19", "int", flag=table.GLOBL), # data
    0x80385114: table.sym_fnc("o_script_1F", "int", flag=table.GLOBL), # data
    0x803851D0: table.sym_fnc("o_script_20", "int", flag=table.GLOBL), # data
    0x8038528C: table.sym_fnc("o_script_23", "int", flag=table.GLOBL), # data
    0x8038531C: table.sym_fnc("o_script_2E", "int", flag=table.GLOBL), # data
    0x803853AC: table.sym_fnc("o_script_2B", "int", flag=table.GLOBL), # data
    0x8038546C: table.sym_fnc("o_script_24", "int", flag=table.GLOBL), # data
    0x803854CC: table.sym_fnc("o_script_00", "int", flag=table.GLOBL), # data
    0x8038556C: table.sym("o_script_8038556C"), # unused
    0x803856A0: table.sym_fnc("o_script_2A", "int", flag=table.GLOBL), # data
    0x80385700: table.sym_fnc("o_script_2D", "int", flag=table.GLOBL), # data
    0x8038575C: table.sym_fnc("o_script_2F", "int", flag=table.GLOBL), # data
    0x803857A0: table.sym_fnc("o_script_31", "int", flag=table.GLOBL), # data
    0x803857E4: table.sym_fnc("o_script_32", "int", flag=table.GLOBL), # data
    0x8038586C: table.sym_fnc("o_script_30", "int", flag=table.GLOBL), # data
    0x80385A60: table.sym_fnc("o_script_33", "int", flag=table.GLOBL), # data
    0x80385AF0: table.sym_fnc("o_script_37", "int", flag=table.GLOBL), # data
    0x80385B4C: table.sym_fnc("o_script_34", "int", flag=table.GLOBL), # data
    0x80385BF0: table.sym("o_script_80385BF0", table.GLOBL),
    0x80385C00: table.sym("o_script_main", table.GLOBL),

    0x8038BCF4: table.sym("s_script_8038BCF8-4"),

    0x8038BD98: table.sym("s_script_8038BD88+shape__child"),

    0x8038BE40: table.sym("map_8038BE30+0x10"),
    0x8038BE44: table.sym("map_8038BE30+0x14"),
    0x8038BE48: table.sym("map_8038BE30+0x18"),
    0x8038BE4C: table.sym("map_8038BE30+0x1C"),

    0x8038BEA0: table.sym("map_data_8038BE98+0x08"),
    0x8038BEA8: table.sym("map_data_8038BE98+0x10"),

    0x8038D6A0: table.sym("map_data_8038D698+0x08"),
    0x8038D6A8: table.sym("map_data_8038D698+0x10"),

    0x80400000: table.sym("_zimgSegmentBssStart"),
    0x8038F800: table.sym("_cimgSegmentBssStart"),
}

sym_E0_d_main2 = {
    # ==========================================================================
    # data
    # ==========================================================================

    # src/math.c
    0x80385F90: table.sym_var("mtx_1",  "Mtx",  flag=table.GLOBL), # unused
    0x80385FD0: table.sym_var("vecf_0", "vecf", flag=table.GLOBL),
    0x80385FDC: table.sym_var("vecs_0", "vecs", flag=table.GLOBL),
    0x80385FE4: table.sym_var("vecf_1", "vecf", flag=table.GLOBL),
    0x80385FF0: table.sym_var("vecs_1", "vecs", flag=table.GLOBL), # unused

    # src/math_table.c
    0x80386000: table.sym_var("math_sin",   "f32", "[]",    table.GLOBL),
    0x80387000: table.sym_var("math_cos",   "f32", "[]",    table.GLOBL),
    0x8038B000: table.sym_var("math_atan",  "s16", "[]",    table.GLOBL),

    # src/s_script.c
    0x8038B810: table.sym_var_fnc("s_script_table", lst="[]", flag=table.GLOBL),

    # src/p_script.c
    0x8038B8A0: table.sym_var("p_script_arena",     "ARENA *",  flag=table.GLOBL|ultra.DALIGN),
    0x8038B8A4: table.sym_var("p_script_sleep",     "u16",  flag=table.GLOBL|ultra.DALIGN),
    0x8038B8A8: table.sym_var("p_script_freeze",    "u16",  flag=table.GLOBL|ultra.DALIGN),
    0x8038B8AC: table.sym_var("p_script_scene",     "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x8038B8B0: table.sym_var("p_script_sp",        "void **",  flag=table.GLOBL|ultra.DALIGN),
    0x8038B8B4: table.sym_var("p_script_fp",        "void **",  flag=table.GLOBL|ultra.DALIGN),
    0x8038B8B8: table.sym_var_fnc("p_script_table", lst="[]", flag=table.GLOBL),

    # src/o_script.c
    0x8038B9B0: table.sym_var_fnc("o_script_table", lst="[]", val="int", flag=table.GLOBL),

    # ==========================================================================
    # rodata
    # ==========================================================================

    # src/math.c
    0x8038BA90: table.sym_var("math_8038BA90", "const f64"),
    0x8038BA98: table.sym_var_fnc("math_8038BA98", "const", "[]"),
    0x8038BAAC: table.sym_var("math_8038BAAC", "const f32"),
    0x8038BAB0: table.sym_var("math_8038BAB0", "const f32"),
    0x8038BAB4: table.sym_var("math_8038BAB4", "const f32"),
    0x8038BAB8: table.sym_var("math_8038BAB8", "const f32"),
    0x8038BABC: table.sym_var("math_8038BABC", "const f32"),
    0x8038BAC0: table.sym_var("math_8038BAC0", "const f32"),
    0x8038BAC4: table.sym_var("math_8038BAC4", "const f32"),
    0x8038BAC8: table.sym_var("math_8038BAC8", "const f32"),
    0x8038BACC: table.sym_var("math_8038BACC", "const f32"),
    0x8038BAD0: table.sym_var("math_8038BAD0", "const f32"),
    0x8038BAD4: table.sym_var("math_8038BAD4", "const f32"),
    0x8038BAD8: table.sym_var("math_8038BAD8", "const f32"),
    0x8038BADC: table.sym_var("math_8038BADC", "const f32"),
    0x8038BAE0: table.sym_var("math_8038BAE0", "const f32"),
    0x8038BAE4: table.sym_var("math_8038BAE4", "const f32"),
    0x8038BAE8: table.sym_var("math_8038BAE8", "const f32"),

    # src/p_script.c
    0x8038BAF0: table.sym_var_fnc("p_script_8038BAF0", "const", "[]"),
    0x8038BB10: table.sym_var_fnc("p_script_8038BB10", "const", "[]"),
    0x8038BB24: table.sym_var_fnc("p_script_8038BB24", "const", "[]"),

    # src/map.c
    0x8038BB40: table.sym_var("str_map_area",   "const char", "[]"),
    0x8038BB4C: table.sym_var("str_map_dg",     "const char", "[]"),
    0x8038BB54: table.sym_var("str_map_dw",     "const char", "[]"),
    0x8038BB5C: table.sym_var("str_map_dr",     "const char", "[]"),
    0x8038BB64: table.sym_var("str_map_x",      "const char", "[]"), # %d
    0x8038BB68: table.sym_var("str_map_y",      "const char", "[]"), # %d
    0x8038BB6C: table.sym_var("str_map_z",      "const char", "[]"), # %d
    0x8038BB70: table.sym_var("str_map_listal", "const char", "[]"),
    0x8038BB7C: table.sym_var("str_map_statbg", "const char", "[]"),
    0x8038BB88: table.sym_var("str_map_movebg", "const char", "[]"),
    0x8038BB94: table.sym_var("map_8038BB94", "const f32"),
    0x8038BB98: table.sym_var("map_8038BB98", "const f32"),
    0x8038BB9C: table.sym_var("map_8038BB9C", "const f32"),
    0x8038BBA0: table.sym_var("map_8038BBA0", "const f32"),
    0x8038BBA4: table.sym_var("map_8038BBA4", "const f32"),
    0x8038BBA8: table.sym_var("map_8038BBA8", "const f32"),
    0x8038BBAC: table.sym_var("map_8038BBAC", "const f32"),

    # src/map_data.c
    0x8038BBB0: table.sym_var("map_data_8038BBB0", "const f64"),
    0x8038BBB8: table.sym_var("map_data_8038BBB8", "const f64"),
    0x8038BBC0: table.sym_var("map_data_8038BBC0", "const f64"),
    0x8038BBC8: table.sym_var("map_data_8038BBC8", "const f64"),
    0x8038BBD0: table.sym_var("map_data_8038BBD0", "const f64"),
    0x8038BBD8: table.sym_var_fnc("map_data_8038BBD8", "const", "[]"),
    0x8038BC80: table.sym_var("map_data_8038BC80", "const f32"),

    # ==========================================================================
    # bss
    # ==========================================================================

    # src/math.c
    0x8038BC90: table.sym_var("bspline",        "const BSPLINE *",  flag=table.GLOBL),
    0x8038BC94: table.sym_var("bspline_phase",  "f32",  flag=table.GLOBL),
    0x8038BC98: table.sym_var("bspline_mode",   "s32",  flag=table.GLOBL),

    # src/s_script.c
    0x8038BCA0: table.sym_var("s_script_arena",     "ARENA *",   flag=table.GLOBL),
    0x8038BCA4: table.sym_var("s_script_8038BCA4",  "SHAPE *",   flag=table.GLOBL),
    0x8038BCA8: table.sym_var("s_script_8038BCA8",  "SHAPE *",   flag=table.GLOBL),
    0x8038BCAC: table.sym_var("s_script_8038BCAC",  "SHAPE **",  flag=table.GLOBL),
    0x8038BCB0: table.sym_var("s_script_8038BCB0",  "u16",  flag=table.GLOBL),
    0x8038BCB8: table.sym_var("s_script_8038BCB8",  "void *",  "[16]", table.GLOBL|ultra.BALIGN),
    0x8038BCF8: table.sym_var("s_script_8038BCF8",  "SHAPE *", "[32]", table.GLOBL|ultra.BALIGN),
    0x8038BD78: table.sym_var("s_script_8038BD78",  "s16",  flag=table.GLOBL),
    0x8038BD7A: table.sym_var("s_script_8038BD7A",  "s16",  flag=table.GLOBL),
    0x8038BD7C: table.sym_var("s_script_8038BD7C",  "s16",  flag=table.GLOBL), # unused
    0x8038BD7E: table.sym_var("s_script_8038BD7E",  "s16",  flag=table.GLOBL),
    0x8038BD80: table.sym_var("s_script_8038BD80",  "u8 *", flag=table.GLOBL),
    0x8038BD88: table.sym_var("s_script_8038BD88",  "SHAPE", flag=table.GLOBL|ultra.BALIGN),

    # src/p_script.c
    0x8038BDA0: table.sym_var("p_script_stack", "void *", "[32]", table.GLOBL|ultra.BALIGN),
    0x8038BE20: table.sym_var("p_script_state", "s16",  flag=table.GLOBL),
    0x8038BE24: table.sym_var("p_script_code",  "int",  flag=table.GLOBL),
    0x8038BE28: table.sym_var("p_script_pc",    "u8 *", flag=table.GLOBL),

    # src/map.c
    0x8038BE30: table.sym_var("map_8038BE30",   "u8", "[0x60]", table.GLOBL),

    # src/map_data.c
    0x8038BE90: table.sym_var("map_data_8038BE90",  "u32",  flag=table.GLOBL),
    0x8038BE98: table.sym_var("map_data_8038BE98",  "u32", "[16][16][6]",   table.GLOBL|ultra.BALIGN), # type
    0x8038D698: table.sym_var("map_data_8038D698",  "u32", "[16][16][6]",   table.GLOBL|ultra.BALIGN), # type
    0x8038EE98: table.sym_var("map_data_8038EE98",  "void *",   flag=table.GLOBL),
    0x8038EE9C: table.sym_var("map_data_8038EE9C",  "void *",   flag=table.GLOBL),
    0x8038EEA0: table.sym_var("map_data_8038EEA0",  "s16",  flag=table.GLOBL),
    0x8038EEA4: table.sym_var("map_data_8038EEA4",  "u32",  "[12]", table.GLOBL), # unused

    # src/o_script.c
    0x8038EEE0: table.sym_var("rng_seed",   "u16",  flag=table.GLOBL),
}

sym_E0_t_menu = {
    0x0021F4C0: table.sym("_menuSegmentRomStart"),

    # ==========================================================================
    # text
    # ==========================================================================

    # src/title.c
    0x8016F000: table.sym("title_8016F000"),
    0x8016F128: table.sym("title_8016F128"),
    0x8016F3CC: table.sym("title_8016F3CC"),
    0x8016F4B0: table.sym("title_8016F4B0"),
    0x8016F564: table.sym("title_8016F564"),
    0x8016F5B0: table.sym("p_title_main", table.GLOBL), # p callback

    # src/title_bg.c
    0x8016F670: table.sym("s_logo_shape", table.GLOBL), # s callback
    0x8016F984: table.sym("s_logo_text", table.GLOBL), # s callback
    0x8016FBB0: table.sym("title_bg_8016FBB0"),
    0x8016FE70: table.sym("s_title_bg", table.GLOBL), # s callback
    0x8016FFFC: table.sym("s_gameover_bg", table.GLOBL), # s callback

    # src/file_select.c
    0x80170280: table.sym("file_select_80170280", table.GLOBL), # o callback
    0x801702B8: table.sym("file_select_801702B8", table.GLOBL), # o callback
    0x801702E8: table.sym("file_select_801702E8"),
    0x80170488: table.sym("file_select_80170488"),
    0x801705DC: table.sym("file_select_801705DC"),
    0x80170710: table.sym("file_select_80170710"),
    0x80170838: table.sym("file_select_80170838"),
    0x8017096C: table.sym("file_select_8017096C"),
    0x80170A4C: table.sym("file_select_80170A4C"),
    0x80170A9C: table.sym("file_select_80170A9C"),
    0x80170AEC: table.sym("file_select_80170AEC", table.GLOBL), # o callback
    0x80170B1C: table.sym("file_select_80170B1C", table.GLOBL), # o callback
    0x80170B54: table.sym_fnc("L80170B54", flag=table.GLOBL|table.LOCAL),
    0x80170B6C: table.sym_fnc("L80170B6C", flag=table.GLOBL|table.LOCAL),
    0x80170BC8: table.sym_fnc("L80170BC8", flag=table.GLOBL|table.LOCAL),
    0x80170BD0: table.sym_fnc("L80170BD0", flag=table.GLOBL|table.LOCAL),
    0x80170C2C: table.sym_fnc("L80170C2C", flag=table.GLOBL|table.LOCAL),
    0x80170C4C: table.sym_fnc("L80170C4C", flag=table.GLOBL|table.LOCAL),
    0x80170C6C: table.sym_fnc("L80170C6C", flag=table.GLOBL|table.LOCAL),
    0x80170CB4: table.sym("file_select_80170CB4"),
    0x80170D60: table.sym("file_select_80170D60"),
    0x80171168: table.sym("file_select_80171168"),
    0x8017137C: table.sym("file_select_8017137C"),
    0x80171784: table.sym("file_select_80171784"),
    0x80171A2C: table.sym("file_select_80171A2C"),
    0x80171C0C: table.sym("file_select_80171C0C"),
    0x80172014: table.sym("file_select_80172014"),
    0x801721AC: table.sym("file_select_801721AC"),
    0x8017236C: table.sym("file_select_8017236C"),
    0x801724B8: table.sym("file_select_801724B8"),
    0x8017261C: table.sym("file_select_8017261C"),
    0x80172644: table.sym("file_select_80172644"),
    0x80172818: table.sym("file_select_80172818"),
    0x801729E0: table.sym("file_select_801729E0"),
    0x80172BA8: table.sym("file_select_80172BA8"),
    0x80172D70: table.sym("file_select_80172D70", table.GLOBL), # o callback
    0x801731A8: table.sym("file_select_801731A8"),
    0x801732F8: table.sym_fnc("L801732F8", flag=table.GLOBL|table.LOCAL),
    0x80173314: table.sym_fnc("L80173314", flag=table.GLOBL|table.LOCAL),
    0x80173330: table.sym_fnc("L80173330", flag=table.GLOBL|table.LOCAL),
    0x8017334C: table.sym_fnc("L8017334C", flag=table.GLOBL|table.LOCAL),
    0x80173368: table.sym_fnc("L80173368", flag=table.GLOBL|table.LOCAL),
    0x80173394: table.sym_fnc("L80173394", flag=table.GLOBL|table.LOCAL),
    0x801733C0: table.sym_fnc("L801733C0", flag=table.GLOBL|table.LOCAL),
    0x801733EC: table.sym_fnc("L801733EC", flag=table.GLOBL|table.LOCAL),
    0x80173418: table.sym_fnc("L80173418", flag=table.GLOBL|table.LOCAL),
    0x80173430: table.sym("file_select_80173430", table.GLOBL), # o callback
    0x80173468: table.sym_fnc("L80173468", flag=table.GLOBL|table.LOCAL),
    0x80173478: table.sym_fnc("L80173478", flag=table.GLOBL|table.LOCAL),
    0x80173494: table.sym_fnc("L80173494", flag=table.GLOBL|table.LOCAL),
    0x801734B0: table.sym_fnc("L801734B0", flag=table.GLOBL|table.LOCAL),
    0x801734CC: table.sym_fnc("L801734CC", flag=table.GLOBL|table.LOCAL),
    0x801734E8: table.sym_fnc("L801734E8", flag=table.GLOBL|table.LOCAL),
    0x80173500: table.sym_fnc("L80173500", flag=table.GLOBL|table.LOCAL),
    0x80173518: table.sym_fnc("L80173518", flag=table.GLOBL|table.LOCAL),
    0x80173530: table.sym_fnc("L80173530", flag=table.GLOBL|table.LOCAL),
    0x8017354C: table.sym_fnc("L8017354C", flag=table.GLOBL|table.LOCAL),
    0x80173568: table.sym_fnc("L80173568", flag=table.GLOBL|table.LOCAL),
    0x80173584: table.sym_fnc("L80173584", flag=table.GLOBL|table.LOCAL),
    0x801735A0: table.sym_fnc("L801735A0", flag=table.GLOBL|table.LOCAL),
    0x801735BC: table.sym_fnc("L801735BC", flag=table.GLOBL|table.LOCAL),
    0x801735D8: table.sym_fnc("L801735D8", flag=table.GLOBL|table.LOCAL),
    0x801735F4: table.sym_fnc("L801735F4", flag=table.GLOBL|table.LOCAL),
    0x801735FC: table.sym_fnc("L801735FC", flag=table.GLOBL|table.LOCAL),
    0x80173604: table.sym_fnc("L80173604", flag=table.GLOBL|table.LOCAL),
    0x8017360C: table.sym_fnc("L8017360C", flag=table.GLOBL|table.LOCAL),
    0x80173614: table.sym_fnc("L80173614", flag=table.GLOBL|table.LOCAL),
    0x80173630: table.sym_fnc("L80173630", flag=table.GLOBL|table.LOCAL),
    0x8017364C: table.sym_fnc("L8017364C", flag=table.GLOBL|table.LOCAL),
    0x80173668: table.sym_fnc("L80173668", flag=table.GLOBL|table.LOCAL),
    0x80173670: table.sym_fnc("L80173670", flag=table.GLOBL|table.LOCAL),
    0x80173678: table.sym_fnc("L80173678", flag=table.GLOBL|table.LOCAL),
    0x80173680: table.sym_fnc("L80173680", flag=table.GLOBL|table.LOCAL),
    0x80173688: table.sym_fnc("L80173688", flag=table.GLOBL|table.LOCAL),
    0x801736A4: table.sym_fnc("L801736A4", flag=table.GLOBL|table.LOCAL),
    0x801736C0: table.sym_fnc("L801736C0", flag=table.GLOBL|table.LOCAL),
    0x801736DC: table.sym_fnc("L801736DC", flag=table.GLOBL|table.LOCAL),
    0x801736F4: table.sym_fnc("L801736F4", flag=table.GLOBL|table.LOCAL),
    0x80173710: table.sym_fnc("L80173710", flag=table.GLOBL|table.LOCAL),
    0x8017372C: table.sym_fnc("L8017372C", flag=table.GLOBL|table.LOCAL),
    0x80173780: table.sym("file_select_80173780"),
    0x80173900: table.sym("file_select_80173900"),
    0x80173AE0: table.sym("file_select_80173AE0"),
    0x80173C6C: table.sym("file_select_80173C6C"),
    0x80173D64: table.sym("file_select_80173D64"),
    0x80173E54: table.sym("file_select_80173E54"),
    0x80173EE4: table.sym("file_select_80173EE4"),
    0x80173FD4: table.sym("file_select_80173FD4"),
    0x80174324: table.sym("file_select_80174324"),
    0x801743AC: table.sym("file_select_801743AC"),
    0x801746F8: table.sym("file_select_801746F8"),
    0x8017472C: table.sym_fnc("L8017472C", flag=table.GLOBL|table.LOCAL),
    0x8017477C: table.sym_fnc("L8017477C", flag=table.GLOBL|table.LOCAL),
    0x80174798: table.sym_fnc("L80174798", flag=table.GLOBL|table.LOCAL),
    0x801747B4: table.sym_fnc("L801747B4", flag=table.GLOBL|table.LOCAL),
    0x801747D0: table.sym_fnc("L801747D0", flag=table.GLOBL|table.LOCAL),
    0x80174804: table.sym("file_select_80174804"),
    0x801749B0: table.sym("file_select_801749B0"),
    0x80174CA8: table.sym("file_select_80174CA8"),
    0x80175238: table.sym("file_select_80175238"),
    0x80175350: table.sym_fnc("L80175350", flag=table.GLOBL|table.LOCAL),
    0x8017536C: table.sym_fnc("L8017536C", flag=table.GLOBL|table.LOCAL),
    0x80175390: table.sym_fnc("L80175390", flag=table.GLOBL|table.LOCAL),
    0x801753A8: table.sym_fnc("L801753A8", flag=table.GLOBL|table.LOCAL),
    0x801753D4: table.sym_fnc("L801753D4", flag=table.GLOBL|table.LOCAL),
    0x80175404: table.sym("file_select_80175404"),
    0x801755A8: table.sym("file_select_801755A8"),
    0x801758A0: table.sym("file_select_801758A0"),
    0x80175B14: table.sym("file_select_80175B14"),
    0x80175B90: table.sym("file_select_80175B90"),
    0x80175D2C: table.sym("file_select_80175D2C"),
    0x80175DFC: table.sym("file_select_80175DFC"),
    0x801764E0: table.sym("file_select_801764E0"),
    0x80176520: table.sym_fnc("L80176520", flag=table.GLOBL|table.LOCAL),
    0x80176530: table.sym_fnc("L80176530", flag=table.GLOBL|table.LOCAL),
    0x80176548: table.sym_fnc("L80176548", flag=table.GLOBL|table.LOCAL),
    0x80176558: table.sym_fnc("L80176558", flag=table.GLOBL|table.LOCAL),
    0x80176568: table.sym_fnc("L80176568", flag=table.GLOBL|table.LOCAL),
    0x80176578: table.sym_fnc("L80176578", flag=table.GLOBL|table.LOCAL),
    0x80176588: table.sym_fnc("L80176588", flag=table.GLOBL|table.LOCAL),
    0x80176598: table.sym_fnc("L80176598", flag=table.GLOBL|table.LOCAL),
    0x801765A8: table.sym_fnc("L801765A8", flag=table.GLOBL|table.LOCAL),
    0x801765B8: table.sym_fnc("L801765B8", flag=table.GLOBL|table.LOCAL),
    0x80176688: table.sym("s_file_select_main", table.GLOBL), # s callback
    0x801766DC: table.sym("p_file_select_init", table.GLOBL), # p callback
    0x801768A0: table.sym("p_file_select_update", table.GLOBL), # p callback

    # src/star_select.c
    0x801768E0: table.sym("star_select_801768E0", table.GLOBL), # o callback
    0x80176A74: table.sym("star_select_80176A74"),
    0x80176B20: table.sym("star_select_80176B20", table.GLOBL), # o callback
    0x80176DF0: table.sym("star_select_80176DF0", table.GLOBL), # o callback
    0x80176FC4: table.sym("star_select_80176FC4"),
    0x80177144: table.sym("star_select_80177144"),
    0x80177518: table.sym("s_star_select_main", table.GLOBL), # s callback
    0x80177560: table.sym("p_star_select_init", table.GLOBL), # p callback
    0x80177610: table.sym("p_star_select_update", table.GLOBL), # p callback

    # src/face/main.c
    0x80177710: table.sym("face_main"), # unused

    # src/face/mem.c
    0x80177820: table.sym("face_mem_80177820"),
    0x80177924: table.sym("face_mem_80177924"),
    0x801779DC: table.sym("MakeMemBlock"),
    0x80177BB8: table.sym("Free", table.GLOBL),
    0x80177C58: table.sym("face_mem_80177C58", table.GLOBL),
    0x80177E7C: table.sym("face_mem_80177E7C", table.GLOBL),
    0x80177F0C: table.sym("face_mem_80177F0C", table.GLOBL),
    0x80177F34: table.sym("face_mem_80177F34"),
    0x801780B0: table.sym("face_mem_801780B0", table.GLOBL),

    # src/face/sfx.c
    0x801781E0: table.sym("face_sfx_801781E0", table.GLOBL),
    0x80178200: table.sym("face_sfx_80178200", table.GLOBL),
    0x8017822C: table.sym("face_sfx_8017822C", table.GLOBL),
    0x80178254: table.sym("face_sfx_80178254", table.GLOBL),

    # src/face/draw.c
    0x80178280: table.sym("face_draw_80178280"),
    0x8017831C: table.sym("face_draw_8017831C"), # unused
    0x801785DC: table.sym("Draw_Shape"),
    0x8017894C: table.sym("Draw_Shape2D"),
    0x80178A40: table.sym("face_draw_80178A40", table.GLOBL),
    0x80178C5C: table.sym("Draw_Material", table.GLOBL),
    0x80178D90: table.sym("face_draw_80178D90"),
    0x80178DEC: table.sym("face_draw_80178DEC"), # unused
    0x80178ED8: table.sym("face_draw_80178ED8", table.GLOBL),
    0x80178F04: table.sym_fnc("L80178F04", flag=table.GLOBL|table.LOCAL),
    0x80178F18: table.sym_fnc("L80178F18", flag=table.GLOBL|table.LOCAL),
    0x80178F2C: table.sym_fnc("L80178F2C", flag=table.GLOBL|table.LOCAL),
    0x80178F40: table.sym_fnc("L80178F40", flag=table.GLOBL|table.LOCAL),
    0x80178F54: table.sym_fnc("L80178F54", flag=table.GLOBL|table.LOCAL),
    0x80178F68: table.sym_fnc("L80178F68", flag=table.GLOBL|table.LOCAL),
    0x80178F7C: table.sym_fnc("L80178F7C", flag=table.GLOBL|table.LOCAL),
    0x80178F90: table.sym_fnc("L80178F90", flag=table.GLOBL|table.LOCAL),
    0x80178FA4: table.sym_fnc("L80178FA4", flag=table.GLOBL|table.LOCAL),
    0x80178FB8: table.sym_fnc("L80178FB8", flag=table.GLOBL|table.LOCAL),
    0x80178FCC: table.sym_fnc("L80178FCC", flag=table.GLOBL|table.LOCAL),
    0x80178FE0: table.sym_fnc("L80178FE0", flag=table.GLOBL|table.LOCAL),
    0x8017900C: table.sym("face_draw_8017900C"), # unused
    0x80179120: table.sym("Draw_Face", table.GLOBL),
    0x80179368: table.sym("face_draw_80179368"),
    0x801793CC: table.sym("face_draw_801793CC"),
    0x80179430: table.sym("face_draw_80179430"), # unused
    0x80179490: table.sym("face_draw_80179490", table.GLOBL),
    0x80179768: table.sym("face_draw_80179768", table.GLOBL),
    0x801798AC: table.sym("face_draw_801798AC", table.GLOBL),
    0x801799AC: table.sym("Draw_Camera", table.GLOBL),
    0x80179C0C: table.sym("face_draw_80179C0C"),
    0x80179CA4: table.sym("face_draw_80179CA4"),
    0x80179CDC: table.sym("face_draw_80179CDC", table.GLOBL),
    0x80179E08: table.sym("face_draw_80179E08"),
    0x8017A010: table.sym("draw_scene"),
    0x8017A344: table.sym("face_draw_8017A344", table.GLOBL),
    0x8017A358: table.sym("face_draw_8017A358"),
    0x8017A44C: table.sym("face_draw_8017A44C", table.GLOBL),
    0x8017A690: table.sym("face_draw_8017A690", table.GLOBL),
    0x8017A7E4: table.sym("face_draw_8017A7E4", table.GLOBL),
    0x8017A900: table.sym("Draw_Group", table.GLOBL),
    0x8017A958: table.sym("face_draw_8017A958", table.GLOBL),
    0x8017A9E0: table.sym("face_draw_8017A9E0", table.GLOBL),
    0x8017AA5C: table.sym("face_draw_8017AA5C"),
    0x8017AAF0: table.sym("face_draw_8017AAF0"),
    0x8017AED8: table.sym("updateshaders"),
    0x8017AFC8: table.sym("face_draw_8017AFC8"),
    0x8017B01C: table.sym("face_draw_8017B01C"), # unused
    0x8017B088: table.sym("face_draw_8017B088"),
    0x8017B168: table.sym("face_draw_8017B168", table.GLOBL),
    0x8017B1A4: table.sym("face_draw_8017B1A4", table.GLOBL),
    0x8017B258: table.sym("face_draw_8017B258"),
    0x8017B3DC: table.sym("find_thisface_verts"),
    0x8017B538: table.sym("map_vertices", table.GLOBL),
    0x8017B608: table.sym("face_draw_8017B608"), # unused
    0x8017B654: table.sym("face_draw_8017B654"),
    0x8017B730: table.sym("face_draw_8017B730"),
    0x8017B764: table.sym("UpdateView", table.GLOBL),
    0x8017BDD4: table.sym("face_draw_8017BDD4"), # unused

    # src/face/object.c
    0x8017BDF0: table.sym("face_object_8017BDF0", table.GLOBL),
    0x8017BE60: table.sym("face_object_8017BE60", table.GLOBL),
    0x8017BFA0: table.sym("face_object_8017BFA0", table.GLOBL),
    0x8017C010: table.sym("face_object_8017C010", table.GLOBL),
    0x8017C034: table.sym("face_object_8017C034"),
    0x8017C154: table.sym_fnc("L8017C154", flag=table.GLOBL|table.LOCAL),
    0x8017C168: table.sym_fnc("L8017C168", flag=table.GLOBL|table.LOCAL),
    0x8017C17C: table.sym_fnc("L8017C17C", flag=table.GLOBL|table.LOCAL),
    0x8017C190: table.sym_fnc("L8017C190", flag=table.GLOBL|table.LOCAL),
    0x8017C1A4: table.sym_fnc("L8017C1A4", flag=table.GLOBL|table.LOCAL),
    0x8017C1B8: table.sym_fnc("L8017C1B8", flag=table.GLOBL|table.LOCAL),
    0x8017C2D0: table.sym_fnc("L8017C2D0", flag=table.GLOBL|table.LOCAL),
    0x8017C300: table.sym("make_object", table.GLOBL),
    0x8017C450: table.sym_fnc("L8017C450", flag=table.GLOBL|table.LOCAL),
    0x8017C46C: table.sym_fnc("L8017C46C", flag=table.GLOBL|table.LOCAL),
    0x8017C488: table.sym_fnc("L8017C488", flag=table.GLOBL|table.LOCAL),
    0x8017C4A4: table.sym_fnc("L8017C4A4", flag=table.GLOBL|table.LOCAL),
    0x8017C4C0: table.sym_fnc("L8017C4C0", flag=table.GLOBL|table.LOCAL),
    0x8017C4F8: table.sym_fnc("L8017C4F8", flag=table.GLOBL|table.LOCAL),
    0x8017C688: table.sym_fnc("L8017C688", flag=table.GLOBL|table.LOCAL),
    0x8017C810: table.sym("face_object_8017C810", table.GLOBL),
    0x8017C8E0: table.sym("face_object_8017C8E0"), # unused
    0x8017C940: table.sym("face_object_8017C940", table.GLOBL),
    0x8017CA00: table.sym("face_object_8017CA00", table.GLOBL),
    0x8017CAC4: table.sym("face_object_8017CAC4", table.GLOBL),
    0x8017CB4C: table.sym("reset_plane", table.GLOBL),
    0x8017CF7C: table.sym("face_object_8017CF7C", table.GLOBL),
    0x8017D010: table.sym("face_object_8017D010", table.GLOBL),
    0x8017D22C: table.sym("face_object_8017D22C", table.GLOBL),
    0x8017D2D4: table.sym("face_object_8017D2D4", table.GLOBL),
    0x8017D3E8: table.sym("face_object_8017D3E8", table.GLOBL),
    0x8017D67C: table.sym("face_object_8017D67C", table.GLOBL),
    0x8017D6F4: table.sym("face_object_8017D6F4", table.GLOBL),
    0x8017D76C: table.sym("face_object_8017D76C", table.GLOBL),
    0x8017D838: table.sym("face_object_8017D838", table.GLOBL),
    0x8017D8E0: table.sym_fnc("L8017D8E0", flag=table.GLOBL|table.LOCAL),
    0x8017D900: table.sym_fnc("L8017D900", flag=table.GLOBL|table.LOCAL),
    0x8017D920: table.sym_fnc("L8017D920", flag=table.GLOBL|table.LOCAL),
    0x8017D940: table.sym_fnc("L8017D940", flag=table.GLOBL|table.LOCAL),
    0x8017D960: table.sym_fnc("L8017D960", flag=table.GLOBL|table.LOCAL),
    0x8017D9D0: table.sym_fnc("L8017D9D0", flag=table.GLOBL|table.LOCAL),
    0x8017DA04: table.sym("make_group", table.GLOBL),
    0x8017DC14: table.sym("addto_group", table.GLOBL),
    0x8017DD00: table.sym("addto_groupfirst", table.GLOBL),
    0x8017DDFC: table.sym("face_object_8017DDFC", table.GLOBL),
    0x8017DE80: table.sym("face_object_8017DE80"), # unused
    0x8017E328: table.sym("face_object_8017E328"), # unused
    0x8017E34C: table.sym("make_scene", table.GLOBL),
    0x8017E370: table.sym("face_object_8017E370"),
    0x8017E3F8: table.sym("face_object_8017E3F8", table.GLOBL),
    0x8017E430: table.sym("face_object_8017E430"),
    0x8017E520: table.sym("face_object_8017E520", table.GLOBL),
    0x8017E6C4: table.sym("face_object_8017E6C4", table.GLOBL),
    0x8017E978: table.sym("face_object_8017E978", table.GLOBL),
    0x8017EB2C: table.sym("face_object_8017EB2C", table.GLOBL),
    0x8017EBD4: table.sym("face_object_8017EBD4"), # unused
    0x8017EC64: table.sym("face_object_8017EC64"), # unused
    0x8017EE40: table.sym("face_object_8017EE40"), # unused
    0x8017EF0C: table.sym("face_object_8017EF0C"), # unused
    0x8017EF9C: table.sym("face_object_8017EF9C", table.GLOBL),
    0x8017F194: table.sym("face_object_8017F194", table.GLOBL),
    0x8017F350: table.sym("face_object_8017F350"),
    0x8017F50C: table.sym("face_object_8017F50C"), # unused
    0x8017F544: table.sym("face_object_8017F544"),
    0x8017F564: table.sym("face_object_8017F564"),
    0x8017F704: table.sym("move_animator"),
    0x8017F9EC: table.sym_fnc("L8017F9EC", flag=table.GLOBL|table.LOCAL),
    0x8017FA3C: table.sym_fnc("L8017FA3C", flag=table.GLOBL|table.LOCAL),
    0x8017FBFC: table.sym_fnc("L8017FBFC", flag=table.GLOBL|table.LOCAL),
    0x8017FDA4: table.sym_fnc("L8017FDA4", flag=table.GLOBL|table.LOCAL),
    0x80180054: table.sym_fnc("L80180054", flag=table.GLOBL|table.LOCAL),
    0x80180410: table.sym_fnc("L80180410", flag=table.GLOBL|table.LOCAL),
    0x801805C4: table.sym_fnc("L801805C4", flag=table.GLOBL|table.LOCAL),
    0x80180614: table.sym_fnc("L80180614", flag=table.GLOBL|table.LOCAL),
    0x8018066C: table.sym_fnc("L8018066C", flag=table.GLOBL|table.LOCAL),
    0x801806C4: table.sym_fnc("L801806C4", flag=table.GLOBL|table.LOCAL),
    0x80180730: table.sym_fnc("L80180730", flag=table.GLOBL|table.LOCAL),
    0x80180764: table.sym("face_object_80180764"),
    0x80180A64: table.sym("move_animators"),
    0x80180AB4: table.sym("face_object_80180AB4", table.GLOBL),
    0x80180AF0: table.sym("face_object_80180AF0"),
    0x80181114: table.sym("face_object_80181114"),
    0x8018114C: table.sym("face_object_8018114C"),
    0x801814B8: table.sym("face_object_801814B8"),
    0x801814F0: table.sym("face_object_801814F0"),
    0x8018159C: table.sym("face_object_8018159C", table.GLOBL),
    0x80181634: table.sym("face_object_80181634", table.GLOBL),
    0x80181678: table.sym("face_object_80181678", table.GLOBL),

    # src/face/skin.c
    0x80181720: table.sym("face_skin_80181720"), # unused
    0x801818A0: table.sym("face_skin_801818A0", table.GLOBL),
    0x8018197C: table.sym("move_skinnet", table.GLOBL),
    0x801819D4: table.sym("face_skin_801819D4", table.GLOBL),
    0x80181B10: table.sym("face_skin_80181B10"),
    0x80181C20: table.sym("reset_weight"),
    0x80181CC8: table.sym("face_skin_80181CC8", table.GLOBL),

    # src/face/particle.c
    0x80181D40: table.sym("face_particle_80181D40"),
    0x80181E54: table.sym("face_particle_80181E54"),
    0x80181FF0: table.sym("face_particle_80181FF0"),
    0x801821C8: table.sym("face_particle_801821C8"),
    0x801824E0: table.sym("face_particle_801824E0", table.GLOBL),
    0x80182630: table.sym("face_particle_80182630", table.GLOBL),
    0x8018273C: table.sym("face_particle_8018273C"),
    0x801828B8: table.sym("face_particle_801828B8"),
    0x80182B48: table.sym("face_particle_80182B48"),
    0x80182DC4: table.sym("face_particle_80182DC4"),
    0x801836B0: table.sym("face_particle_801836B0", table.GLOBL),
    0x80183708: table.sym("face_particle_80183708"), # unused
    0x801839B0: table.sym("face_particle_801839B0"), # unused
    0x801839C4: table.sym("face_particle_801839C4"), # unused
    0x801839D8: table.sym("face_particle_801839D8"), # unused
    0x801839F4: table.sym("face_particle_801839F4"), # unused
    0x80183A10: table.sym("face_particle_80183A10"),

    # src/face/dynlist.c
    0x80183A50: table.sym("face_dynlist_80183A50", table.GLOBL),
    0x80183A80: table.sym("face_dynlist_80183A80", table.GLOBL),
    0x80183AB0: table.sym("face_dynlist_80183AB0", table.GLOBL),
    0x80183B20: table.sym("proc_dynlist", table.GLOBL),
    0x80183BB0: table.sym_fnc("L80183BB0", flag=table.GLOBL|table.LOCAL),
    0x80183BCC: table.sym_fnc("L80183BCC", flag=table.GLOBL|table.LOCAL),
    0x80183BEC: table.sym_fnc("L80183BEC", flag=table.GLOBL|table.LOCAL),
    0x80183C0C: table.sym_fnc("L80183C0C", flag=table.GLOBL|table.LOCAL),
    0x80183C28: table.sym_fnc("L80183C28", flag=table.GLOBL|table.LOCAL),
    0x80183C48: table.sym_fnc("L80183C48", flag=table.GLOBL|table.LOCAL),
    0x80183C64: table.sym_fnc("L80183C64", flag=table.GLOBL|table.LOCAL),
    0x80183C80: table.sym_fnc("L80183C80", flag=table.GLOBL|table.LOCAL),
    0x80183C9C: table.sym_fnc("L80183C9C", flag=table.GLOBL|table.LOCAL),
    0x80183CB8: table.sym_fnc("L80183CB8", flag=table.GLOBL|table.LOCAL),
    0x80183CD4: table.sym_fnc("L80183CD4", flag=table.GLOBL|table.LOCAL),
    0x80183E08: table.sym_fnc("L80183E08", flag=table.GLOBL|table.LOCAL),
    0x80183E24: table.sym_fnc("L80183E24", flag=table.GLOBL|table.LOCAL),
    0x80183E40: table.sym_fnc("L80183E40", flag=table.GLOBL|table.LOCAL),
    0x80183E5C: table.sym_fnc("L80183E5C", flag=table.GLOBL|table.LOCAL),
    0x80183E80: table.sym_fnc("L80183E80", flag=table.GLOBL|table.LOCAL),
    0x80183EA4: table.sym_fnc("L80183EA4", flag=table.GLOBL|table.LOCAL),
    0x80183EC8: table.sym_fnc("L80183EC8", flag=table.GLOBL|table.LOCAL),
    0x80183EEC: table.sym_fnc("L80183EEC", flag=table.GLOBL|table.LOCAL),
    0x80183F10: table.sym_fnc("L80183F10", flag=table.GLOBL|table.LOCAL),
    0x80183F24: table.sym_fnc("L80183F24", flag=table.GLOBL|table.LOCAL),
    0x80183F48: table.sym_fnc("L80183F48", flag=table.GLOBL|table.LOCAL),
    0x80183F6C: table.sym_fnc("L80183F6C", flag=table.GLOBL|table.LOCAL),
    0x80183F90: table.sym_fnc("L80183F90", flag=table.GLOBL|table.LOCAL),
    0x80183FB0: table.sym_fnc("L80183FB0", flag=table.GLOBL|table.LOCAL),
    0x80183FD0: table.sym_fnc("L80183FD0", flag=table.GLOBL|table.LOCAL),
    0x80183FEC: table.sym_fnc("L80183FEC", flag=table.GLOBL|table.LOCAL),
    0x80184008: table.sym_fnc("L80184008", flag=table.GLOBL|table.LOCAL),
    0x80184024: table.sym_fnc("L80184024", flag=table.GLOBL|table.LOCAL),
    0x80184040: table.sym_fnc("L80184040", flag=table.GLOBL|table.LOCAL),
    0x80184060: table.sym_fnc("L80184060", flag=table.GLOBL|table.LOCAL),
    0x80184074: table.sym_fnc("L80184074", flag=table.GLOBL|table.LOCAL),
    0x80184090: table.sym_fnc("L80184090", flag=table.GLOBL|table.LOCAL),
    0x801840AC: table.sym_fnc("L801840AC", flag=table.GLOBL|table.LOCAL),
    0x801840C8: table.sym_fnc("L801840C8", flag=table.GLOBL|table.LOCAL),
    0x801840E4: table.sym_fnc("L801840E4", flag=table.GLOBL|table.LOCAL),
    0x80184100: table.sym_fnc("L80184100", flag=table.GLOBL|table.LOCAL),
    0x8018411C: table.sym_fnc("L8018411C", flag=table.GLOBL|table.LOCAL),
    0x80184138: table.sym_fnc("L80184138", flag=table.GLOBL|table.LOCAL),
    0x80184154: table.sym_fnc("L80184154", flag=table.GLOBL|table.LOCAL),
    0x80184178: table.sym_fnc("L80184178", flag=table.GLOBL|table.LOCAL),
    0x80184194: table.sym_fnc("L80184194", flag=table.GLOBL|table.LOCAL),
    0x801841B8: table.sym_fnc("L801841B8", flag=table.GLOBL|table.LOCAL),
    0x801841DC: table.sym_fnc("L801841DC", flag=table.GLOBL|table.LOCAL),
    0x801841F8: table.sym_fnc("L801841F8", flag=table.GLOBL|table.LOCAL),
    0x80184218: table.sym_fnc("L80184218", flag=table.GLOBL|table.LOCAL),
    0x80184234: table.sym_fnc("L80184234", flag=table.GLOBL|table.LOCAL),
    0x80184254: table.sym_fnc("L80184254", flag=table.GLOBL|table.LOCAL),
    0x80184270: table.sym_fnc("L80184270", flag=table.GLOBL|table.LOCAL),
    0x8018428C: table.sym_fnc("L8018428C", flag=table.GLOBL|table.LOCAL),
    0x801842AC: table.sym_fnc("L801842AC", flag=table.GLOBL|table.LOCAL),
    0x801842C8: table.sym_fnc("L801842C8", flag=table.GLOBL|table.LOCAL),
    0x801842E4: table.sym_fnc("L801842E4", flag=table.GLOBL|table.LOCAL),
    0x80184300: table.sym_fnc("L80184300", flag=table.GLOBL|table.LOCAL),
    0x8018435C: table.sym("face_dynlist_8018435C", table.GLOBL),
    0x80184400: table.sym("face_dynlist_80184400"), # unused
    0x801844A8: table.sym("face_dynlist_801844A8"),
    0x801844DC: table.sym("face_dynlist_801844DC"),
    0x80184510: table.sym("face_dynlist_80184510"),
    0x80184630: table.sym("face_dynlist_80184630"), # unused
    0x8018468C: table.sym("face_dynlist_8018468C"),
    0x80184740: table.sym("face_dynlist_80184740"),
    0x801847AC: table.sym("face_dynlist_801847AC"),
    0x80184828: table.sym("dMakeNetFromShape"),
    0x801848A0: table.sym("dMakeNetFromShapePtrPtr"),
    0x801848E8: table.sym("face_dynlist_801848E8"),
    0x80184B84: table.sym("face_dynlist_80184B84"),
    0x80184BF8: table.sym("dMakeObj", table.GLOBL),
    0x80184C3C: table.sym_fnc("L80184C3C", flag=table.GLOBL|table.LOCAL),
    0x80184C50: table.sym_fnc("L80184C50", flag=table.GLOBL|table.LOCAL),
    0x80184C70: table.sym_fnc("L80184C70", flag=table.GLOBL|table.LOCAL),
    0x80184C90: table.sym_fnc("L80184C90", flag=table.GLOBL|table.LOCAL),
    0x80184CB4: table.sym_fnc("L80184CB4", flag=table.GLOBL|table.LOCAL),
    0x80184CD4: table.sym_fnc("L80184CD4", flag=table.GLOBL|table.LOCAL),
    0x80184CF8: table.sym_fnc("L80184CF8", flag=table.GLOBL|table.LOCAL),
    0x80184D10: table.sym_fnc("L80184D10", flag=table.GLOBL|table.LOCAL),
    0x80184D30: table.sym_fnc("L80184D30", flag=table.GLOBL|table.LOCAL),
    0x80184D58: table.sym_fnc("L80184D58", flag=table.GLOBL|table.LOCAL),
    0x80184D74: table.sym_fnc("L80184D74", flag=table.GLOBL|table.LOCAL),
    0x80184DA8: table.sym_fnc("L80184DA8", flag=table.GLOBL|table.LOCAL),
    0x80184DC0: table.sym_fnc("L80184DC0", flag=table.GLOBL|table.LOCAL),
    0x80184DDC: table.sym_fnc("L80184DDC", flag=table.GLOBL|table.LOCAL),
    0x80184E04: table.sym_fnc("L80184E04", flag=table.GLOBL|table.LOCAL),
    0x80184E1C: table.sym_fnc("L80184E1C", flag=table.GLOBL|table.LOCAL),
    0x80184E44: table.sym_fnc("L80184E44", flag=table.GLOBL|table.LOCAL),
    0x80184E78: table.sym_fnc("L80184E78", flag=table.GLOBL|table.LOCAL),
    0x80184E8C: table.sym_fnc("L80184E8C", flag=table.GLOBL|table.LOCAL),
    0x80184EFC: table.sym("dAttach"),
    0x80184FC4: table.sym("face_dynlist_80184FC4"),
    0x8018536C: table.sym("dAttachTo"),
    0x80185410: table.sym("face_dynlist_80185410"),
    0x8018545C: table.sym("animdata"),
    0x801855E4: table.sym_fnc("L801855E4", flag=table.GLOBL|table.LOCAL),
    0x801855F4: table.sym_fnc("L801855F4", flag=table.GLOBL|table.LOCAL),
    0x80185604: table.sym_fnc("L80185604", flag=table.GLOBL|table.LOCAL),
    0x80185614: table.sym_fnc("L80185614", flag=table.GLOBL|table.LOCAL),
    0x80185624: table.sym_fnc("L80185624", flag=table.GLOBL|table.LOCAL),
    0x80185634: table.sym_fnc("L80185634", flag=table.GLOBL|table.LOCAL),
    0x80185644: table.sym_fnc("L80185644", flag=table.GLOBL|table.LOCAL),
    0x80185654: table.sym_fnc("L80185654", flag=table.GLOBL|table.LOCAL),
    0x80185A18: table.sym("chk_shapegen"),
    0x801861B0: table.sym("dSetNodeGroup"),
    0x80186350: table.sym("dSetMatGroup"),
    0x80186440: table.sym("dSetTextureST"),
    0x801864DC: table.sym("dUseTexture"),
    0x80186588: table.sym("dSetSkinShape"),
    0x8018666C: table.sym("dMapMaterials"),
    0x801866F8: table.sym("dMapVertices"),
    0x80186784: table.sym("dSetPlaneGroup"),
    0x801868A4: table.sym("dSetShapePtrPtr", table.GLOBL),
    0x80186A60: table.sym("dSetShapePtr"),
    0x80186BFC: table.sym("dUseObj", table.GLOBL),
    0x80186C84: table.sym("face_dynlist_80186C84", table.GLOBL),
    0x80186CAC: table.sym("face_dynlist_80186CAC", table.GLOBL),
    0x80186CDC: table.sym("dEndGroup", table.GLOBL),
    0x80186DE0: table.sym("dAddToGroup"),
    0x80186E5C: table.sym("face_dynlist_80186E5C", table.GLOBL),
    0x80186E74: table.sym("dSetInitPos", table.GLOBL),
    0x8018710C: table.sym("dSetVelocity"), # unused
    0x80187244: table.sym("face_dynlist_80187244"), # unused
    0x8018739C: table.sym("dSetTorque"), # unused
    0x80187480: table.sym("dGetInitPos", table.GLOBL),
    0x80187608: table.sym("dGetInitRot", table.GLOBL),
    0x80187794: table.sym("dSetRelPos", table.GLOBL),
    0x80187AB0: table.sym("dAddToRelPos"), # unused
    0x80187C80: table.sym("dGetRelPos", table.GLOBL),
    0x80187E78: table.sym("dGetAttObjGroup", table.GLOBL),
    0x80187F54: table.sym("dGetAttToObj"), # unused
    0x80188030: table.sym("dGetScale", table.GLOBL),
    0x801881B8: table.sym("dSetAttOffset"),
    0x8018837C: table.sym("dSetAttToOffset"),
    0x801884D0: table.sym("dGetAttOffset"), # unused
    0x80188624: table.sym("dGetAttFlags"), # unused
    0x80188738: table.sym("dSetWorldPos", table.GLOBL),
    0x801889A8: table.sym("dSetNormal"),
    0x80188AB0: table.sym("dGetWorldPosPtr"), # unused
    0x80188B7C: table.sym("dGetWorldPos", table.GLOBL),
    0x80188CD4: table.sym_fnc("L80188CD4", flag=table.GLOBL|table.LOCAL),
    0x80188D24: table.sym_fnc("L80188D24", flag=table.GLOBL|table.LOCAL),
    0x80188D74: table.sym_fnc("L80188D74", flag=table.GLOBL|table.LOCAL),
    0x80188E14: table.sym_fnc("L80188E14", flag=table.GLOBL|table.LOCAL),
    0x80188E64: table.sym_fnc("L80188E64", flag=table.GLOBL|table.LOCAL),
    0x801891AC: table.sym_fnc("L801891AC", flag=table.GLOBL|table.LOCAL),
    0x801891F4: table.sym("face_dynlist_801891F4"),
    0x80189240: table.sym("dSetScale", table.GLOBL),
    0x8018945C: table.sym("dSetRotation"),
    0x80189584: table.sym("dCofG"),
    0x80189660: table.sym("dShapeOffset"),
    0x8018973C: table.sym("dAddValPtr", table.GLOBL),
    0x801898D8: table.sym("dAddValProc", table.GLOBL),
    0x80189990: table.sym("dLinkWithPtr"),
    0x80189CD8: table.sym("dLinkWith"),
    0x80189DA8: table.sym("dSetFlags", table.GLOBL),
    0x80189E74: table.sym_fnc("L80189E74", flag=table.GLOBL|table.LOCAL),
    0x80189E94: table.sym_fnc("L80189E94", flag=table.GLOBL|table.LOCAL),
    0x80189EB4: table.sym_fnc("L80189EB4", flag=table.GLOBL|table.LOCAL),
    0x80189F14: table.sym_fnc("L80189F14", flag=table.GLOBL|table.LOCAL),
    0x80189F34: table.sym_fnc("L80189F34", flag=table.GLOBL|table.LOCAL),
    0x80189F74: table.sym_fnc("L80189F74", flag=table.GLOBL|table.LOCAL),
    0x80189FB4: table.sym("dClrFlags"),
    0x8018A12C: table.sym("dSetParmf", table.GLOBL),
    0x8018A358: table.sym("dSetParmp", table.GLOBL),
    0x8018A530: table.sym("face_dynlist_8018A530", table.GLOBL),
    0x8018A590: table.sym("dSetType", table.GLOBL),
    0x8018A700: table.sym("dSetID"),
    0x8018A828: table.sym("dSetColNum", table.GLOBL),
    0x8018A9EC: table.sym("dSetMaterial"),
    0x8018AA9C: table.sym("dFriction"),
    0x8018AB78: table.sym("dSetSpring"),
    0x8018AC24: table.sym("dSetAmbient"),
    0x8018AD00: table.sym("dSetDiffuse", table.GLOBL),
    0x8018AE30: table.sym("dControlType"),
    0x8018AEDC: table.sym("face_dynlist_8018AEDC", table.GLOBL),
    0x8018AFB0: table.sym("dGetMatrix", table.GLOBL),
    0x8018B0FC: table.sym("dSetMatrix"), # unused
    0x8018B210: table.sym("face_dynlist_8018B210"), # unused
    0x8018B2E8: table.sym("dGetRMatrixPtr", table.GLOBL),
    0x8018B3A4: table.sym("dSetIMatrix", table.GLOBL),
    0x8018B4D4: table.sym("dGetMatrixPtr", table.GLOBL),
    0x8018B5E8: table.sym("dGetIMatrixPtr", table.GLOBL),
    0x8018B6BC: table.sym("face_dynlist_8018B6BC", table.GLOBL),
    0x8018B758: table.sym("dSetSkinWeight"),

    # src/face/gadget.c
    0x8018B830: table.sym("get_objvalue", table.GLOBL),
    0x8018B8E8: table.sym("face_gadget_8018B8E8"), # unused
    0x8018B97C: table.sym("face_gadget_8018B97C"),
    0x8018B9D8: table.sym("face_gadget_8018B9D8"),
    0x8018BA40: table.sym("face_gadget_8018BA40"), # unused
    0x8018BB00: table.sym("face_gadget_8018BB00", table.GLOBL),
    0x8018BBC0: table.sym("face_gadget_8018BBC0", table.GLOBL),
    0x8018BC9C: table.sym("set_objvalue"),
    0x8018BD54: table.sym("face_gadget_8018BD54"),
    0x8018BDF8: table.sym("face_gadget_8018BDF8"),
    0x8018BE40: table.sym("adjust_gadget"), # unused
    0x8018C0F4: table.sym("reset_gadget", table.GLOBL),
    0x8018C2B0: table.sym("face_gadget_8018C2B0", table.GLOBL),

    # src/face/stdio.c
    0x8018C2F0: table.sym("face_stdio_8018C2F0"),
    0x8018C3A4: table.sym("face_stdio_8018C3A4"),
    0x8018C44C: table.sym("face_stdio_8018C44C", table.GLOBL),
    0x8018C550: table.sym("face_stdio_8018C550"), # unused
    0x8018C598: table.sym("face_stdio_8018C598", table.GLOBL),
    0x8018C704: table.sym("face_stdio_8018C704", table.GLOBL),
    0x8018C790: table.sym("face_stdio_8018C790", table.GLOBL),
    0x8018C7B4: table.sym("face_stdio_8018C7B4", table.GLOBL),
    0x8018C86C: table.sym("face_stdio_8018C86C", table.GLOBL),
    0x8018C920: table.sym("face_stdio_8018C920", table.GLOBL),
    0x8018C938: table.sym("face_stdio_8018C938", table.GLOBL),
    0x8018C954: table.sym("face_stdio_8018C954", table.GLOBL),
    0x8018CA88: table.sym("face_stdio_8018CA88"),
    0x8018CB34: table.sym("face_stdio_8018CB34"),
    0x8018CBF4: table.sym("face_stdio_8018CBF4"),
    0x8018CC54: table.sym("get_timernum", table.GLOBL),
    0x8018CCC0: table.sym("face_stdio_8018CCC0"),
    0x8018CD9C: table.sym("face_stdio_8018CD9C"), # unused
    0x8018CE0C: table.sym("face_stdio_8018CE0C"), # unused
    0x8018CEA0: table.sym("start_timer", table.GLOBL),
    0x8018CF70: table.sym("restart_timer", table.GLOBL),
    0x8018D02C: table.sym("face_stdio_8018D02C", table.GLOBL),
    0x8018D088: table.sym("face_stdio_8018D088", table.GLOBL),
    0x8018D160: table.sym("face_stdio_8018D160", table.GLOBL),
    0x8018D1A8: table.sym("face_stdio_8018D1A8"), # unused
    0x8018D1F8: table.sym("face_stdio_8018D1F8", table.GLOBL),
    0x8018D228: table.sym("face_stdio_8018D228"),
    0x8018D298: table.sym("face_stdio_8018D298", table.GLOBL),
    0x8018D358: table.sym_fnc("L8018D358", flag=table.GLOBL|table.LOCAL),
    0x8018D38C: table.sym_fnc("L8018D38C", flag=table.GLOBL|table.LOCAL),
    0x8018D410: table.sym_fnc("L8018D410", flag=table.GLOBL|table.LOCAL),
    0x8018D444: table.sym_fnc("L8018D444", flag=table.GLOBL|table.LOCAL),
    0x8018D478: table.sym_fnc("L8018D478", flag=table.GLOBL|table.LOCAL),
    0x8018D4AC: table.sym_fnc("L8018D4AC", flag=table.GLOBL|table.LOCAL),
    0x8018D560: table.sym("face_stdio_8018D560", table.GLOBL),
    0x8018D5F0: table.sym("imout", table.GLOBL),
    0x8018D6A0: table.sym("face_stdio_8018D6A0", table.GLOBL),
    0x8018D7E8: table.sym("gd_atoi", table.GLOBL),
    0x8018D948: table.sym("face_stdio_8018D948", table.GLOBL),
    0x8018D988: table.sym("face_stdio_8018D988"),
    0x8018D9E8: table.sym("face_stdio_8018D9E8"),
    0x8018DAE4: table.sym("face_stdio_8018DAE4"),
    0x8018DB38: table.sym("face_stdio_8018DB38", table.GLOBL),
    0x8018DDD8: table.sym("face_stdio_8018DDD8", table.GLOBL),
    0x8018DE1C: table.sym("face_stdio_8018DE1C"), # unused
    0x8018DE9C: table.sym("gd_strdup", table.GLOBL),
    0x8018DF18: table.sym("face_stdio_8018DF18", table.GLOBL),
    0x8018DF6C: table.sym("face_stdio_8018DF6C", table.GLOBL),
    0x8018DFF0: table.sym("face_stdio_8018DFF0", table.GLOBL),
    0x8018E098: table.sym("face_stdio_8018E098", table.GLOBL),
    0x8018E128: table.sym("face_stdio_8018E128", table.GLOBL),
    0x8018E14C: table.sym("face_stdio_8018E14C"),
    0x8018E16C: table.sym("gd_fopen", table.GLOBL),
    0x8018E37C: table.sym("face_stdio_8018E37C", table.GLOBL),
    0x8018E4A8: table.sym("face_stdio_8018E4A8", table.GLOBL),
    0x8018E4C4: table.sym("face_stdio_8018E4C4", table.GLOBL),
    0x8018E4E0: table.sym("face_stdio_8018E4E0"),
    0x8018E518: table.sym("face_stdio_8018E518", table.GLOBL),

    # src/face/joint.c
    0x8018E660: table.sym("face_joint_8018E660"),
    0x8018ED28: table.sym("face_joint_8018ED28", table.GLOBL),
    0x8018EF9C: table.sym("face_joint_8018EF9C"), # unused
    0x8018F0B8: table.sym("face_joint_8018F0B8"),
    0x8018F188: table.sym("face_joint_8018F188", table.GLOBL),
    0x8018F388: table.sym("face_joint_8018F388", table.GLOBL),
    0x8018F468: table.sym("face_joint_8018F468", table.GLOBL),
    0x8018F60C: table.sym("face_joint_8018F60C"),
    0x8018F660: table.sym("face_joint_8018F660"),
    0x8018F9DC: table.sym("face_joint_8018F9DC"),
    0x8018FBA8: table.sym("face_joint_8018FBA8", table.GLOBL),
    0x8018FC08: table.sym("face_joint_8018FC08", table.GLOBL),
    0x8018FC98: table.sym("face_joint_8018FC98", table.GLOBL),
    0x8018FDE4: table.sym("add_joint2bone", table.GLOBL),
    0x8018FEDC: table.sym("face_joint_8018FEDC", table.GLOBL),
    0x80190054: table.sym("face_joint_80190054"), # unused
    0x80190068: table.sym("face_joint_80190068"), # unused
    0x801900C8: table.sym("face_joint_801900C8"), # unused
    0x80190128: table.sym("face_joint_80190128"),
    0x801902A8: table.sym("face_joint_801902A8"),
    0x80190528: table.sym("face_joint_80190528"),
    0x801906B4: table.sym("face_joint_801906B4"),
    0x80190AF4: table.sym("face_joint_80190AF4"),
    0x80190B60: table.sym("face_joint_80190B60"), # unused
    0x80190C94: table.sym("face_joint_80190C94"),
    0x80190FA8: table.sym("face_joint_80190FA8"), # unused
    0x8019107C: table.sym("face_joint_8019107C"),
    0x801912E8: table.sym("face_joint_801912E8", table.GLOBL),
    0x80191360: table.sym("face_joint_80191360", table.GLOBL),
    0x80191500: table.sym("face_joint_80191500", table.GLOBL),
    0x80191530: table.sym("face_joint_80191530", table.GLOBL),
    0x80191638: table.sym("face_joint_80191638", table.GLOBL),
    0x8019164C: table.sym("face_joint_8019164C"), # unused
    0x80191744: table.sym("face_joint_80191744", table.GLOBL),
    0x80191964: table.sym("face_joint_80191964", table.GLOBL),
    0x80191A34: table.sym("face_joint_80191A34"), # unused
    0x80191B5C: table.sym("face_joint_80191B5C"), # unused
    0x80191D38: table.sym("face_joint_80191D38"),
    0x80191EA0: table.sym("face_joint_80191EA0"),
    0x80191F94: table.sym("face_joint_80191F94"),
    0x80191FC8: table.sym("face_joint_80191FC8", table.GLOBL),
    0x80192028: table.sym("face_joint_80192028", table.GLOBL),

    # src/face/net.c
    0x80192050: table.sym("face_net_80192050"),
    0x80192204: table.sym("reset_net", table.GLOBL),
    0x801923D4: table.sym("face_net_801923D4"),
    0x8019243C: table.sym("face_net_8019243C"),
    0x801924F4: table.sym("face_net_801924F4", table.GLOBL),
    0x80192668: table.sym("face_net_80192668"),
    0x801927E4: table.sym("face_net_801927E4"),
    0x80192C10: table.sym("face_net_80192C10"), # unused
    0x80192D9C: table.sym("move_bonesnet"),
    0x80192E0C: table.sym("face_net_80192E0C"),
    0x801930D8: table.sym("face_net_801930D8"),
    0x80193424: table.sym("face_net_80193424"),
    0x8019353C: table.sym("face_net_8019353C", table.GLOBL),
    0x80193610: table.sym("face_net_80193610"),
    0x801936DC: table.sym("move_net"),
    0x80193730: table.sym_fnc("L80193730", flag=table.GLOBL|table.LOCAL),
    0x80193738: table.sym_fnc("L80193738", flag=table.GLOBL|table.LOCAL),
    0x8019374C: table.sym_fnc("L8019374C", flag=table.GLOBL|table.LOCAL),
    0x80193778: table.sym_fnc("L80193778", flag=table.GLOBL|table.LOCAL),
    0x801937A4: table.sym_fnc("L801937A4", flag=table.GLOBL|table.LOCAL),
    0x801937B8: table.sym_fnc("L801937B8", flag=table.GLOBL|table.LOCAL),
    0x801937CC: table.sym_fnc("L801937CC", flag=table.GLOBL|table.LOCAL),
    0x80193804: table.sym("move_nets", table.GLOBL),
    0x8019387C: table.sym("face_net_8019387C"),
    0x80193988: table.sym("face_net_80193988", table.GLOBL),
    0x801939FC: table.sym("face_net_801939FC"), # unused
    0x80193C50: table.sym("face_net_80193C50", table.GLOBL),

    # src/face/math.c
    0x80193C70: table.sym("face_math_80193C70"),
    0x80193CA8: table.sym("face_math_80193CA8", table.GLOBL),
    0x8019429C: table.sym("face_math_8019429C", table.GLOBL),
    0x80194360: table.sym("face_math_80194360", table.GLOBL),
    0x80194424: table.sym("face_math_80194424", table.GLOBL),
    0x80194498: table.sym("face_math_80194498", table.GLOBL),
    0x80194868: table.sym("face_math_80194868", table.GLOBL),
    0x801948B0: table.sym("face_math_801948B0", table.GLOBL),
    0x801949C0: table.sym("face_math_801949C0", table.GLOBL),
    0x80194ACC: table.sym("face_math_80194ACC"), # unused
    0x80194B94: table.sym("absrot_matrix4", table.GLOBL),
    0x80194CD8: table.sym("face_math_80194CD8", table.GLOBL),
    0x80194D34: table.sym("face_math_80194D34", table.GLOBL),
    0x80194E54: table.sym("face_math_80194E54", table.GLOBL),
    0x80194EF8: table.sym("face_math_80194EF8", table.GLOBL),
    0x80194F3C: table.sym("face_math_80194F3C"), # unused
    0x80194FBC: table.sym("face_math_80194FBC", table.GLOBL),
    0x801950D0: table.sym("face_math_801950D0"),
    0x801956B8: table.sym("face_math_801956B8"),
    0x80195984: table.sym("face_math_80195984"),
    0x80195A4C: table.sym("face_math_80195A4C"),
    0x80195A90: table.sym("face_math_80195A90"), # unused
    0x80195B20: table.sym("face_math_80195B20"), # unused
    0x80195C44: table.sym("face_math_80195C44"), # unused
    0x80195DB8: table.sym("face_math_80195DB8"),
    0x80195ED8: table.sym("face_math_80195ED8"), # unused
    0x80196114: table.sym("face_math_80196114"),
    0x80196334: table.sym("face_math_80196334", table.GLOBL),
    0x801963C0: table.sym("face_math_801963C0", table.GLOBL),
    0x801964A0: table.sym("face_math_801964A0", table.GLOBL),
    0x80196570: table.sym("face_math_80196570", table.GLOBL),
    0x80196680: table.sym("face_math_80196680", table.GLOBL),
    0x80196754: table.sym("face_math_80196754", table.GLOBL),
    0x801970CC: table.sym("face_math_801970CC", table.GLOBL),
    0x801970E8: table.sym("face_math_801970E8", table.GLOBL),
    0x80197104: table.sym("face_math_80197104", table.GLOBL),
    0x801971A8: table.sym("face_math_801971A8"), # unused
    0x80197230: table.sym("face_math_80197230"), # unused

    # src/face/shape.c
    0x801973C0: table.sym("face_shape_801973C0"),
    0x80197400: table.sym("calc_facenormal", table.GLOBL),
    0x8019764C: table.sym("face_shape_8019764C", table.GLOBL),
    0x80197764: table.sym("make_face", table.GLOBL),
    0x80197810: table.sym("face_shape_80197810"),
    0x8019787C: table.sym("face_shape_8019787C"), # unused
    0x80197904: table.sym("face_shape_80197904", table.GLOBL),
    0x8019797C: table.sym("face_shape_8019797C", table.GLOBL),
    0x80197B14: table.sym("face_shape_80197B14"),
    0x80197B44: table.sym("face_shape_80197B44"),
    0x80197B70: table.sym("face_shape_80197B70"),
    0x80197BD4: table.sym("face_shape_80197BD4"),
    0x80197C54: table.sym("face_shape_80197C54"),
    0x80197C8C: table.sym("face_shape_80197C8C"),
    0x80197CC4: table.sym("face_shape_80197CC4"),
    0x80197DB0: table.sym("face_shape_80197DB0"),
    0x80197E90: table.sym("getfloat"),
    0x80198028: table.sym("getint"),
    0x801981A8: table.sym("face_shape_801981A8"), # unused
    0x801981BC: table.sym("face_shape_801981BC"),
    0x80198228: table.sym("face_shape_80198228"),
    0x80198294: table.sym("face_shape_80198294"), # unused
    0x801982C4: table.sym("face_shape_801982C4"), # unused
    0x80198330: table.sym("face_shape_80198330"),
    0x801983F8: table.sym("face_shape_801983F8"),
    0x8019848C: table.sym("face_shape_8019848C", table.GLOBL),
    0x80198514: table.sym("face_shape_80198514"), # unused
    0x80198584: table.sym("face_shape_80198584"),
    0x80198664: table.sym("face_shape_80198664"),
    0x80198728: table.sym("face_shape_80198728"), # unused
    0x80198844: table.sym("get_3DG1_shape"),
    0x80198D40: table.sym("face_shape_80198D40"),
    0x801990D0: table.sym("face_shape_801990D0"),
    0x801991F4: table.sym("face_shape_801991F4"),
    0x80199330: table.sym("face_shape_80199330"),
    0x801997A0: table.sym("face_shape_801997A0"), # unused
    0x801998E8: table.sym("face_shape_801998E8"), # unused
    0x80199F84: table.sym("face_shape_80199F84"), # unused
    0x80199FC8: table.sym("face_shape_80199FC8"),
    0x8019A024: table.sym("make_netfromshape", table.GLOBL),
    0x8019A0E0: table.sym("face_shape_8019A0E0", table.GLOBL),
    0x8019A1A8: table.sym("face_shape_8019A1A8", table.GLOBL),
    0x8019A4B8: table.sym("face_shape_8019A4B8", table.GLOBL),
    0x8019ABF8: table.sym("load_shapes2", table.GLOBL),
    0x8019ACD8: table.sym("face_shape_8019ACD8"), # unused
    0x8019AF04: table.sym("face_shape_8019AF04"), # unused
    0x8019A1F4: table.sym_fnc("L8019A1F4", flag=table.GLOBL|table.LOCAL),
    0x8019A220: table.sym_fnc("L8019A220", flag=table.GLOBL|table.LOCAL),
    0x8019A2B0: table.sym_fnc("L8019A2B0", flag=table.GLOBL|table.LOCAL),
    0x8019A308: table.sym_fnc("L8019A308", flag=table.GLOBL|table.LOCAL),
    0x8019A368: table.sym_fnc("L8019A368", flag=table.GLOBL|table.LOCAL),
    0x8019A418: table.sym_fnc("L8019A418", flag=table.GLOBL|table.LOCAL),
    0x8019A474: table.sym_fnc("L8019A474", flag=table.GLOBL|table.LOCAL),
    0x8019A48C: table.sym_fnc("L8019A48C", flag=table.GLOBL|table.LOCAL),
    0x8019B004: table.sym("face_shape_8019B004"), # unused

    # src/face/gfx.c
    0x8019B060: table.sym("face_gfx_8019B060", table.GLOBL),
    0x8019B080: table.sym("face_gfx_8019B080", table.GLOBL),
    0x8019B0B0: table.sym("face_gfx_8019B0B0", table.GLOBL),
    0x8019B0D0: table.sym("face_gfx_8019B0D0"),
    0x8019B158: table.sym("face_gfx_8019B158"),
    0x8019B1E4: table.sym("face_gfx_8019B1E4"),
    0x8019B278: table.sym("face_gfx_8019B278"),
    0x8019B304: table.sym("face_gfx_8019B304"),
    0x8019B390: table.sym("face_gfx_8019B390"),
    0x8019B41C: table.sym("face_gfx_8019B41C", table.GLOBL),
    0x8019B45C: table.sym("face_gfx_8019B45C", table.GLOBL),
    0x8019B49C: table.sym("face_gfx_8019B49C", table.GLOBL),
    0x8019B514: table.sym("face_gfx_8019B514"), # unused
    0x8019B53C: table.sym("gd_printf", table.GLOBL),
    0x8019B714: table.sym_fnc("L8019B714", flag=table.GLOBL|table.LOCAL),
    0x8019B770: table.sym_fnc("L8019B770", flag=table.GLOBL|table.LOCAL),
    0x8019B804: table.sym_fnc("L8019B804", flag=table.GLOBL|table.LOCAL),
    0x8019B8B8: table.sym_fnc("L8019B8B8", flag=table.GLOBL|table.LOCAL),
    0x8019B8F0: table.sym_fnc("L8019B8F0", flag=table.GLOBL|table.LOCAL),
    0x8019B93C: table.sym_fnc("L8019B93C", flag=table.GLOBL|table.LOCAL),
    0x8019BB0C: table.sym("gd_exit", table.GLOBL),
    0x8019BB44: table.sym("gd_free", table.GLOBL),
    0x8019BB90: table.sym("gd_allocblock", table.GLOBL),
    0x8019BC88: table.sym("face_gfx_8019BC88", table.GLOBL),
    0x8019BD58: table.sym("gd_malloc", table.GLOBL),
    0x8019BD90: table.sym("face_gfx_8019BD90", table.GLOBL),
    0x8019BDC8: table.sym("face_gfx_8019BDC8"), # unused
    0x8019BE14: table.sym("face_gfx_8019BE14"), # unused
    0x8019BE4C: table.sym("face_gfx_8019BE4C", table.GLOBL),
    0x8019BF08: table.sym("face_gfx_8019BF08"),
    0x8019BF80: table.sym("face_gfx_8019BF80"), # unused
    0x8019BFB0: table.sym("face_gfx_8019BFB0"),
    0x8019C240: table.sym("face_gfx_8019C240"),
    0x8019C3B0: table.sym("face_gfx_8019C3B0"), # unused
    0x8019C3C8: table.sym("face_gfx_8019C3C8"), # unused
    0x8019C418: table.sym("face_gfx_8019C418", table.GLOBL), # ext
    0x8019C450: table.sym("gdm_init", table.GLOBL), # ext
    0x8019C4EC: table.sym("gdm_setup", table.GLOBL), # ext
    0x8019C588: table.sym("face_gfx_8019C588"), # unused
    0x8019C59C: table.sym("face_gfx_8019C59C"), # unused
    0x8019C5F0: table.sym("face_gfx_8019C5F0"),
    0x8019C684: table.sym("gdm_maketestdl", table.GLOBL), # ext
    0x8019C6CC: table.sym_fnc("L8019C6CC", flag=table.GLOBL|table.LOCAL),
    0x8019C6F0: table.sym_fnc("L8019C6F0", flag=table.GLOBL|table.LOCAL),
    0x8019C708: table.sym_fnc("L8019C708", flag=table.GLOBL|table.LOCAL),
    0x8019C764: table.sym_fnc("L8019C764", flag=table.GLOBL|table.LOCAL),
    0x8019C7C0: table.sym_fnc("L8019C7C0", flag=table.GLOBL|table.LOCAL),
    0x8019C7E4: table.sym_fnc("L8019C7E4", flag=table.GLOBL|table.LOCAL),
    0x8019C828: table.sym("face_gfx_8019C828"), # unused
    0x8019C840: table.sym("face_gfx_8019C840"), # unused
    0x8019C874: table.sym("face_gfx_8019C874", table.GLOBL), # ext
    0x8019C930: table.sym("face_gfx_8019C930", table.GLOBL), # ext
    0x8019C9C8: table.sym("face_gfx_8019C9C8", table.GLOBL), # ext
    0x8019C9F8: table.sym("gdm_gettestdl", table.GLOBL), # ext
    0x8019CA58: table.sym_fnc("L8019CA58", flag=table.GLOBL|table.LOCAL),
    0x8019CADC: table.sym_fnc("L8019CADC", flag=table.GLOBL|table.LOCAL),
    0x8019CB54: table.sym_fnc("L8019CB54", flag=table.GLOBL|table.LOCAL),
    0x8019CBF8: table.sym_fnc("L8019CBF8", flag=table.GLOBL|table.LOCAL),
    0x8019CC7C: table.sym_fnc("L8019CC7C", flag=table.GLOBL|table.LOCAL),
    0x8019CD88: table.sym("gdm_getpos"), # unused
    0x8019CE3C: table.sym("face_gfx_8019CE3C"),
    0x8019CF18: table.sym("face_gfx_8019CF18"),
    0x8019CF44: table.sym("alloc_displaylist"),
    0x8019D01C: table.sym("face_gfx_8019D01C"),
    0x8019D110: table.sym("face_gfx_8019D110"),
    0x8019D168: table.sym("face_gfx_8019D168"),
    0x8019D3B8: table.sym("face_gfx_8019D3B8"), # unused
    0x8019D42C: table.sym("face_gfx_8019D42C"), # unused
    0x8019D4A0: table.sym("face_gfx_8019D4A0", table.GLOBL),
    0x8019D848: table.sym("face_gfx_8019D848", table.GLOBL),
    0x8019E438: table.sym("face_gfx_8019E438", table.GLOBL),
    0x8019E724: table.sym("face_gfx_8019E724"),
    0x8019E780: table.sym("face_gfx_8019E780"),
    0x8019E89C: table.sym("face_gfx_8019E89C"),
    0x8019E93C: table.sym("face_gfx_8019E93C"),
    0x8019E9B4: table.sym("face_gfx_8019E9B4", table.GLOBL),
    0x8019E9D4: table.sym("face_gfx_8019E9D4", table.GLOBL),
    0x8019E9F4: table.sym("gd_startdisplist", table.GLOBL),
    0x8019EB44: table.sym("face_gfx_8019EB44"),
    0x8019EBAC: table.sym("face_gfx_8019EBAC", table.GLOBL),
    0x8019ED0C: table.sym("face_gfx_8019ED0C"), # unused
    0x8019ED48: table.sym("face_gfx_8019ED48"),
    0x8019EDC8: table.sym("face_gfx_8019EDC8"), # unused
    0x8019EE34: table.sym("face_gfx_8019EE34"),
    0x8019EFAC: table.sym("face_gfx_8019EFAC"),
    0x8019F054: table.sym("face_gfx_8019F054", table.GLOBL),
    0x8019F100: table.sym("face_gfx_8019F100"), # unused
    0x8019F16C: table.sym("face_gfx_8019F16C", table.GLOBL),
    0x8019F1D8: table.sym("face_gfx_8019F1D8", table.GLOBL),
    0x8019F224: table.sym("face_gfx_8019F224", table.GLOBL),
    0x8019F2DC: table.sym("face_gfx_8019F2DC", table.GLOBL),
    0x8019F398: table.sym("face_gfx_8019F398", table.GLOBL),
    0x8019F404: table.sym("face_gfx_8019F404", table.GLOBL),
    0x8019F458: table.sym("face_gfx_8019F458", table.GLOBL),
    0x8019FB18: table.sym("face_gfx_8019FB18", table.GLOBL),
    0x8019FBA0: table.sym("face_gfx_8019FBA0", table.GLOBL),
    0x801A0030: table.sym("face_gfx_801A0030", table.GLOBL),
    0x801A0094: table.sym("face_gfx_801A0094", table.GLOBL),
    0x801A0178: table.sym("face_gfx_801A0178", table.GLOBL),
    0x801A01B0: table.sym("face_gfx_801A01B0", table.GLOBL),
    0x801A032C: table.sym("face_gfx_801A032C"),
    0x801A039C: table.sym("face_gfx_801A039C"),
    0x801A03F8: table.sym("face_gfx_801A03F8", table.GLOBL),
    0x801A0464: table.sym("face_gfx_801A0464", table.GLOBL),
    0x801A047C: table.sym("face_gfx_801A047C", table.GLOBL),
    0x801A0494: table.sym("face_gfx_801A0494", table.GLOBL),
    0x801A0588: table.sym("face_gfx_801A0588", table.GLOBL),
    0x801A05B8: table.sym("face_gfx_801A05B8", table.GLOBL),
    0x801A09AC: table.sym("face_gfx_801A09AC", table.GLOBL),
    0x801A1728: table.sym("face_gfx_801A1728", table.GLOBL),
    0x801A1804: table.sym("face_gfx_801A1804", table.GLOBL),
    0x801A18F0: table.sym("face_gfx_801A18F0", table.GLOBL),
    0x801A194C: table.sym("face_gfx_801A194C"),
    0x801A1B40: table.sym("face_gfx_801A1B40"),
    0x801A1C70: table.sym("face_gfx_801A1C70"), # unused
    0x801A1FB0: table.sym("face_gfx_801A1FB0"), # unused
    0x801A2450: table.sym("face_gfx_801A2450", table.GLOBL),
    0x801A24A0: table.sym("face_gfx_801A24A0"), # unused
    0x801A24B4: table.sym("face_gfx_801A24B4", table.GLOBL),
    0x801A24C8: table.sym("face_gfx_801A24C8"),
    0x801A2588: table.sym("face_gfx_801A2588", table.GLOBL),
    0x801A2984: table.sym("face_gfx_801A2984"),
    0x801A338C: table.sym("face_gfx_801A338C"), # unused
    0x801A3434: table.sym("face_gfx_801A3434"), # unused
    0x801A3464: table.sym("face_gfx_801A3464"),
    0x801A34B0: table.sym("face_gfx_801A34B0"),
    0x801A3538: table.sym("face_gfx_801A3538"), # unused
    0x801A35BC: table.sym("face_gfx_801A35BC"), # unused
    0x801A3620: table.sym("face_gfx_801A3620", table.GLOBL),
    0x801A36B4: table.sym("gd_shading", table.GLOBL),
    0x801A371C: table.sym("gd_getproperty", table.GLOBL),
    0x801A3788: table.sym("gd_setproperty", table.GLOBL),
    0x801A37E8: table.sym_fnc("L801A37E8", flag=table.GLOBL|table.LOCAL),
    0x801A3898: table.sym_fnc("L801A3898", flag=table.GLOBL|table.LOCAL),
    0x801A38C4: table.sym_fnc("L801A38C4", flag=table.GLOBL|table.LOCAL),
    0x801A39BC: table.sym_fnc("L801A39BC", flag=table.GLOBL|table.LOCAL),
    0x801A3A30: table.sym_fnc("L801A3A30", flag=table.GLOBL|table.LOCAL),
    0x801A3AE0: table.sym_fnc("L801A3AE0", flag=table.GLOBL|table.LOCAL),
    0x801A3B54: table.sym_fnc("L801A3B54", flag=table.GLOBL|table.LOCAL),
    0x801A3BD4: table.sym_fnc("L801A3BD4", flag=table.GLOBL|table.LOCAL),
    0x801A3BDC: table.sym_fnc("L801A3BDC", flag=table.GLOBL|table.LOCAL),
    0x801A3BE4: table.sym_fnc("L801A3BE4", flag=table.GLOBL|table.LOCAL),
    0x801A3BEC: table.sym_fnc("L801A3BEC", flag=table.GLOBL|table.LOCAL),
    0x801A3BF4: table.sym_fnc("L801A3BF4", flag=table.GLOBL|table.LOCAL),
    0x801A3BFC: table.sym_fnc("L801A3BFC", flag=table.GLOBL|table.LOCAL),
    0x801A3C20: table.sym("face_gfx_801A3C20"), # unused
    0x801A3C30: table.sym("face_gfx_801A3C30", table.GLOBL),
    0x801A3DCC: table.sym("face_gfx_801A3DCC", table.GLOBL),
    0x801A3F9C: table.sym("face_gfx_801A3F9C", table.GLOBL),
    0x801A4468: table.sym("face_gfx_801A4468", table.GLOBL),
    0x801A451C: table.sym("face_gfx_801A451C", table.GLOBL),
    0x801A4530: table.sym("face_gfx_801A4530", table.GLOBL),
    0x801A4550: table.sym("face_gfx_801A4550", table.GLOBL),
    0x801A4564: table.sym("face_gfx_801A4564", table.GLOBL),
    0x801A4578: table.sym("face_gfx_801A4578", table.GLOBL),
    0x801A45E0: table.sym("gd_gentexture"),
    0x801A4724: table.sym("face_gfx_801A4724"), # unused
    0x801A48F8: table.sym("face_gfx_801A48F8"), # unused
    0x801A4924: table.sym("face_gfx_801A4924"), # unused
    0x801A4934: table.sym("face_gfx_801A4934"), # unused
    0x801A4948: table.sym("face_gfx_801A4948"),
    0x801A4988: table.sym("face_gfx_801A4988"),
    0x801A49F4: table.sym("face_gfx_801A49F4"),
    0x801A4A04: table.sym("face_gfx_801A4A04", table.GLOBL),
    0x801A4A18: table.sym("face_gfx_801A4A18", table.GLOBL),
    0x801A4A30: table.sym("face_gfx_801A4A30", table.GLOBL),
    0x801A4A48: table.sym("face_gfx_801A4A48"), # unused
    0x801A4A58: table.sym("face_gfx_801A4A58"),
    0x801A4C44: table.sym("face_gfx_801A4C44"), # unused
    0x801A4D4C: table.sym("face_gfx_801A4D4C"),
    0x801A5098: table.sym("face_gfx_801A5098"), # unused
    0x801A5250: table.sym("face_gfx_801A5250"),
    0x801A52A8: table.sym("face_gfx_801A52A8"),
    0x801A534C: table.sym("face_gfx_801A534C", table.GLOBL),
    0x801A5484: table.sym("face_gfx_801A5484"), # unused
    0x801A5538: table.sym("gd_init", table.GLOBL),
    0x801A5A50: table.sym("face_gfx_801A5A50"), # unused
    0x801A5AD8: table.sym("face_gfx_801A5AD8", table.GLOBL),
    0x801A5AEC: table.sym("face_gfx_801A5AEC", table.GLOBL),
    0x801A5B00: table.sym("face_gfx_801A5B00", table.GLOBL),
    0x801A5B14: table.sym("face_gfx_801A5B14", table.GLOBL),
    0x801A5B44: table.sym("face_gfx_801A5B44", table.GLOBL),
    0x801A5B8C: table.sym("face_gfx_801A5B8C", table.GLOBL),
    0x801A5BC0: table.sym("face_gfx_801A5BC0"), # unused
    0x801A5BD4: table.sym("face_gfx_801A5BD4"), # unused
    0x801A5BE8: table.sym("face_gfx_801A5BE8"), # unused
    0x801A5BF8: table.sym("face_gfx_801A5BF8"), # unused
    0x801A5C20: table.sym("face_gfx_801A5C20"), # unused
    0x801A5C98: table.sym("face_gfx_801A5C98", table.GLOBL),
    0x801A5D28: table.sym("face_gfx_801A5D28"),
    0x801A5D64: table.sym("face_gfx_801A5D64"),
    0x801A5DC0: table.sym("face_gfx_801A5DC0"), # unused
    0x801A5ED0: table.sym("face_gfx_801A5ED0"), # unused
    0x801A6138: table.sym("face_gfx_801A6138"), # unused
    0x801A6430: table.sym("face_gfx_801A6430"),
    0x801A676C: table.sym("face_gfx_801A676C"),
    0x801A6904: table.sym("face_gfx_801A6904"),
    0x801A6954: table.sym("face_gfx_801A6954"), # unused
    0x801A6F70: table.sym("face_gfx_801A6F70"), # unused
    0x801A6F84: table.sym("face_gfx_801A6F84"), # unused
    0x801A6F98: table.sym("face_gfx_801A6F98"),
    0x801A7074: table.sym("load_dynlist", table.GLOBL),
    0x801A72F8: table.sym("face_gfx_801A72F8"), # unused
    0x801A730C: table.sym("face_gfx_801A730C"), # unused
    0x801A7820: table.sym("face_gfx_801A7820"), # unused

    # ==========================================================================

    0x801B58B0: table.sym("face_draw_801B58B0+0"),
    0x801B58B4: table.sym("face_draw_801B58B0+4"),
    0x801B58B8: table.sym("face_draw_801B58B8+0"),
    0x801B58BC: table.sym("face_draw_801B58B8+4"),
    0x801B58F0: table.sym("face_draw_801B58F0+0"),
    0x801B58F4: table.sym("face_draw_801B58F0+4"),
    0x801B58F8: table.sym("face_draw_801B58F8+0"),
    0x801B58FC: table.sym("face_draw_801B58F8+4"),
    0x801B5900: table.sym("face_draw_801B5900+0"),
    0x801B5904: table.sym("face_draw_801B5900+4"),
    0x801B5908: table.sym("face_draw_801B5908+0"),
    0x801B590C: table.sym("face_draw_801B5908+4"),

    0x801B5DE0: table.sym("face_object_801B5DE0+0"),
    0x801B5DE4: table.sym("face_object_801B5DE0+4"),
    0x801B5E70: table.sym("face_object_801B5E70+0"),
    0x801B5E74: table.sym("face_object_801B5E70+4"),
    0x801B5E78: table.sym("face_object_801B5E78+0"),
    0x801B5E7C: table.sym("face_object_801B5E78+4"),
    0x801B5E80: table.sym("face_object_801B5E80+0"),
    0x801B5E84: table.sym("face_object_801B5E80+4"),
    0x801B5E88: table.sym("face_object_801B5E88+0"),
    0x801B5E8C: table.sym("face_object_801B5E88+4"),
    0x801B5E90: table.sym("face_object_801B5E90+0"),
    0x801B5E94: table.sym("face_object_801B5E90+4"),
    0x801B5EC8: table.sym("face_object_801B5EC8+0"),
    0x801B5ECC: table.sym("face_object_801B5EC8+4"),
    0x801B5ED0: table.sym("face_object_801B5ED0+0"),
    0x801B5ED4: table.sym("face_object_801B5ED0+4"),

    0x801B5F90: table.sym("face_particle_801B5F90+0"),
    0x801B5F94: table.sym("face_particle_801B5F90+4"),
    0x801B5F98: table.sym("face_particle_801B5F98+0"),
    0x801B5F9C: table.sym("face_particle_801B5F98+4"),
    0x801B5FA0: table.sym("face_particle_801B5FA0+0"),
    0x801B5FA4: table.sym("face_particle_801B5FA0+4"),
    0x801B5FA8: table.sym("face_particle_801B5FA8+0"),
    0x801B5FAC: table.sym("face_particle_801B5FA8+4"),
    0x801B5FB8: table.sym("face_particle_801B5FB8+0"),
    0x801B5FBC: table.sym("face_particle_801B5FB8+4"),
    0x801B5FC0: table.sym("face_particle_801B5FC0+0"),
    0x801B5FC4: table.sym("face_particle_801B5FC0+4"),
    0x801B5FC8: table.sym("face_particle_801B5FC8+0"),
    0x801B5FCC: table.sym("face_particle_801B5FC8+4"),
    0x801B5FD0: table.sym("face_particle_801B5FD0+0"),
    0x801B5FD4: table.sym("face_particle_801B5FD0+4"),

    0x801B82E0: table.sym("face_gadget_801B82E0+0"),
    0x801B82E4: table.sym("face_gadget_801B82E0+4"),
    0x801B82E8: table.sym("face_gadget_801B82E8+0"),
    0x801B82EC: table.sym("face_gadget_801B82E8+4"),

    0x801B85A8: table.sym("face_stdio_801B85A8+0"),
    0x801B85AC: table.sym("face_stdio_801B85A8+4"),

    0x801B86B8: table.sym("face_joint_801B86B8+0"),
    0x801B86BC: table.sym("face_joint_801B86B8+4"),
    0x801B86C0: table.sym("face_joint_801B86C0+0"),
    0x801B86C4: table.sym("face_joint_801B86C0+4"),
    0x801B86C8: table.sym("face_joint_801B86C8+0"),
    0x801B86CC: table.sym("face_joint_801B86C8+4"),
    0x801B86D0: table.sym("face_joint_801B86D0+0"),
    0x801B86D4: table.sym("face_joint_801B86D0+4"),
    0x801B86D8: table.sym("face_joint_801B86D8+0"),
    0x801B86DC: table.sym("face_joint_801B86D8+4"),
    0x801B86E0: table.sym("face_joint_801B86E0+0"),
    0x801B86E4: table.sym("face_joint_801B86E0+4"),
    0x801B86F0: table.sym("face_joint_801B86F0+0"),
    0x801B86F4: table.sym("face_joint_801B86F0+4"),
    0x801B86F8: table.sym("face_joint_801B86F8+0"),
    0x801B86FC: table.sym("face_joint_801B86F8+4"),
    0x801B8700: table.sym("face_joint_801B8700+0"),
    0x801B8704: table.sym("face_joint_801B8700+4"),
    0x801B8708: table.sym("face_joint_801B8708+0"),
    0x801B870C: table.sym("face_joint_801B8708+4"),
    0x801B8710: table.sym("face_joint_801B8710+0"),
    0x801B8714: table.sym("face_joint_801B8710+4"),
    0x801B8718: table.sym("face_joint_801B8718+0"),
    0x801B871C: table.sym("face_joint_801B8718+4"),
    0x801B8720: table.sym("face_joint_801B8720+0"),
    0x801B8724: table.sym("face_joint_801B8720+4"),
    0x801B8728: table.sym("face_joint_801B8728+0"),
    0x801B872C: table.sym("face_joint_801B8728+4"),

    0x801B8930: table.sym("face_net_801B8930+0"),
    0x801B8934: table.sym("face_net_801B8930+4"),
    0x801B8938: table.sym("face_net_801B8938+0"),
    0x801B893C: table.sym("face_net_801B8938+4"),
    0x801B8940: table.sym("face_net_801B8940+0"),
    0x801B8944: table.sym("face_net_801B8940+4"),

    0x801B8A40: table.sym("face_math_801B8A40+0"),
    0x801B8A44: table.sym("face_math_801B8A40+4"),
    0x801B8A48: table.sym("face_math_801B8A48+0"),
    0x801B8A4C: table.sym("face_math_801B8A48+4"),
    0x801B8A50: table.sym("face_math_801B8A50+0"),
    0x801B8A54: table.sym("face_math_801B8A50+4"),
    0x801B8A58: table.sym("face_math_801B8A58+0"),
    0x801B8A5C: table.sym("face_math_801B8A58+4"),

    0x801B9878: table.sym("face_gfx_801B9878+0"),
    0x801B987C: table.sym("face_gfx_801B9878+4"),
    0x801B9908: table.sym("face_gfx_801B9908+0"),
    0x801B990C: table.sym("face_gfx_801B9908+4"),
    0x801B9910: table.sym("face_gfx_801B9910+0"),
    0x801B9914: table.sym("face_gfx_801B9910+4"),
    0x801B9918: table.sym("face_gfx_801B9918+0"),
    0x801B991C: table.sym("face_gfx_801B9918+4"),
    0x801B9920: table.sym("face_gfx_801B9920+0"),
    0x801B9924: table.sym("face_gfx_801B9920+4"),
    0x801B9928: table.sym("face_gfx_801B9928+0"),
    0x801B992C: table.sym("face_gfx_801B9928+4"),
    0x801B9930: table.sym("face_gfx_801B9930+0"),
    0x801B9934: table.sym("face_gfx_801B9930+4"),
    0x801B9938: table.sym("face_gfx_801B9938+0"),
    0x801B993C: table.sym("face_gfx_801B9938+4"),
    0x801B9940: table.sym("face_gfx_801B9940+0"),
    0x801B9944: table.sym("face_gfx_801B9940+4"),
    0x801B9948: table.sym("face_gfx_801B9948+0"),
    0x801B994C: table.sym("face_gfx_801B9948+4"),
    0x801B9950: table.sym("face_gfx_801B9950+0"),
    0x801B9954: table.sym("face_gfx_801B9950+4"),
    0x801B9958: table.sym("face_gfx_801B9958+0"),
    0x801B995C: table.sym("face_gfx_801B9958+4"),
    0x801B9960: table.sym("face_gfx_801B9960+0"),
    0x801B9964: table.sym("face_gfx_801B9960+4"),
    0x801B9968: table.sym("face_gfx_801B9968+0"),
    0x801B996C: table.sym("face_gfx_801B9968+4"),
    0x801B9970: table.sym("face_gfx_801B9970+0"),
    0x801B9974: table.sym("face_gfx_801B9970+4"),
    0x801B9978: table.sym("face_gfx_801B9978+0"),
    0x801B997C: table.sym("face_gfx_801B9978+4"),
    0x801B9980: table.sym("face_gfx_801B9980+0"),
    0x801B9984: table.sym("face_gfx_801B9980+4"),
    0x801B99D8: table.sym("face_gfx_801B99D8+0"),
    0x801B99DC: table.sym("face_gfx_801B99D8+4"),

    0x801B99C0: table.sym("file_select_801B99F8-4*14"),
    0x801B9A30: table.sym("file_select_801B99F8+4*14"),
    0x801B9A4C: table.sym("file_select_801B99F8+4*21"),
    0x801B9A6C: table.sym("file_select_801B99F8+4*29"),

    0x002739A0: table.sym("_face_dataSegmentRomStart"),
    0x002A6120: table.sym("_face_dataSegmentRomEnd"),
    0x04000000: table.sym("0x04000000"),
    0x04000650: table.sym("0x04000650"),
    0x04004F90: table.sym("0x04004F90"),

    # ==========================================================================

    # addr
    # src/face/draw.c
    0x801A8200: table.sym("_face_draw_data+0x00"), # la   draw
    0x801A820C: table.sym("_face_draw_data+0x0C"), # la   draw
    0x801A8218: table.sym("_face_draw_data+0x18"), # la   draw
    0x801A8224: table.sym("_face_draw_data+0x24"), # la   draw
    0x801A8230: table.sym("_face_draw_data+0x30"), # la   draw
    0x801A823C: table.sym("_face_draw_data+0x3C"), # la   draw
    0x801A8248: table.sym("_face_draw_data+0x48"), # la   draw
    0x801A8254: table.sym("_face_draw_data+0x54"), # la   draw
    0x801A8260: table.sym("_face_draw_data+0x60"), # la   draw
    0x801A826C: table.sym("_face_draw_data+0x6C"), # la   draw
    0x801A8278: table.sym("_face_draw_data+0x78"), # la   draw
    0x801A8284: table.sym("_face_draw_data+0x84"), #      draw
    0x801A8288: table.sym("_face_draw_data+0x88"), #      draw / object / particle
    0x801A8290: table.sym("_face_draw_data+0x90"), #      draw
    0x801A8294: table.sym("_face_draw_data+0x94"), # la   draw
    0x801A82A8: table.sym("_face_draw_data+0xA8"), # la   draw
    0x801A8330: table.sym("_face_draw_data+0x130"), #     draw

    # src/face/object.c
    0x801A8350: table.sym("_face_object_data+0x10"), #     object
    0x801A8354: table.sym("_face_object_data+0x14"), #     object

    # src/face/particle.c
    0x801A8364: table.sym("_face_particle_data+0x04"), #     particle
    0x801A8368: table.sym("_face_particle_data+0x08"), #     particle
    0x801A836C: table.sym("_face_particle_data+0x0C"), #     particle
    0x801A8370: table.sym("_face_particle_data+0x10"), #     particle
    0x801A83C8: table.sym("_face_particle_data+0x68"), #     particle
    0x801A83CC: table.sym("_face_particle_data+0x6C"), #     particle
    0x801A83D0: table.sym("_face_particle_data+0x70"), #     particle
    0x801A83D4: table.sym("_face_particle_data+0x74"), #     particle

    # src/face/dynlist.c
    0x801A83E0: table.sym("_face_dynlist_data+0x00"), #     dynlist
    0x801A83E4: table.sym("_face_dynlist_data+0x04"), #     dynlist
    0x801A83E8: table.sym("_face_dynlist_data+0x08"), # la  dynlist
    0x801A8400: table.sym("_face_dynlist_data+0x20"), #     dynlist

    # src/face/stdio.c
    0x801A8410: table.sym("_face_stdio_data+0x00"), #     stdio
    0x801A8414: table.sym("_face_stdio_data+0x04"), #     stdio
    0x801A8430: table.sym("_face_stdio_data+0x20"), #     stdio
    0x801A8434: table.sym("_face_stdio_data+0x24"), #     stdio
    0x801A8438: table.sym("_face_stdio_data+0x28"), #     stdio
    0x801A843C: table.sym("_face_stdio_data+0x2C"), #     stdio
    0x801A8450: table.sym("_face_stdio_data+0x40"), #     stdio

    # src/face/joint.c
    0x801A8460: table.sym("_face_joint_data+0x00"), #     joint
    0x801A8464: table.sym("_face_joint_data+0x04"), #     joint

    # addr
    # src/face/shape.c
    0x801A8470: table.sym("_face_shape_data+0x00"), #     shape / gfx
    0x801A8474: table.sym("_face_shape_data+0x04"), #     shape / draw
    0x801A8478: table.sym("_face_shape_data+0x08"), #     shape
    0x801A847C: table.sym("_face_shape_data+0x0C"), #     shape / gfx
    0x801A8480: table.sym("_face_shape_data+0x10"), #     shape / gfx
    0x801A8484: table.sym("_face_shape_data+0x14"), #     gfx
    0x801A8488: table.sym("_face_shape_data+0x18"), #     gfx
    0x801A87F8: table.sym("_face_shape_data+0x388+0"), #   shape
    0x801A87FC: table.sym("_face_shape_data+0x388+4"), #   shape

    # src/face/gfx.c
    # 00
    0x801A8804: table.sym("_face_gfx_data+0x04"), #     gfx
    # 08
    0x801A880C: table.sym("_face_gfx_data+0x0C"), #     gfx
    0x801A8810: table.sym("_face_gfx_data+0x10"),
    0x801A8814: table.sym("_face_gfx_data+0x14"),
    0x801A8818: table.sym("_face_gfx_data+0x18"),
    0x801A881C: table.sym("_face_gfx_data+0x1C"),
    0x801A8820: table.sym("_face_gfx_data+0x20"),
    0x801A8824: table.sym("_face_gfx_data+0x24"),
    0x801A8828: table.sym("_face_gfx_data+0x28"),
    0x801A882C: table.sym("_face_gfx_data+0x2C"),
    0x801A8830: table.sym("_face_gfx_data+0x30"),
    0x801A8834: table.sym("_face_gfx_data+0x34"),
    0x801A8838: table.sym("_face_gfx_data+0x38"),
    0x801A883C: table.sym("_face_gfx_data+0x3C"),
    0x801A8840: table.sym("_face_gfx_data+0x40"), # gfx / draw
    # 44
    0x801A8848: table.sym("_face_gfx_data+0x48"),
    0x801A884C: table.sym("_face_gfx_data+0x4C"),
    0x801A8850: table.sym("_face_gfx_data+0x50"),
    # 54
    0x801A8858: table.sym("_face_gfx_data+0x58"),
    0x801A885C: table.sym("_face_gfx_data+0x5C"),
    0x801A8860: table.sym("_face_gfx_data+0x60"),
    0x801A8864: table.sym("_face_gfx_data+0x64"),
    0x801A8868: table.sym("_face_gfx_data+0x68"),
    0x801A886C: table.sym("_face_gfx_data+0x6C"),
    0x801A8870: table.sym("_face_gfx_data+0x70"),
    0x801A8874: table.sym("_face_gfx_data+0x74"),
    0x801A8878: table.sym("_face_gfx_data+0x78"),
    0x801A887C: table.sym("_face_gfx_data+0x7C"),
    0x801A8880: table.sym("_face_gfx_data+0x80"),
    0x801A8884: table.sym("_face_gfx_data+0x84"),
    # 88
    0x801A888C: table.sym("_face_gfx_data+0x8C"),
    0x801A8890: table.sym("_face_gfx_data+0x90"),
    0x801A8894: table.sym("_face_gfx_data+0x94"),
    0x801A8898: table.sym("_face_gfx_data+0x98"),
    # 9C ... B8

    # addr
    # 0x801A88B8: # unused
    0x801A88C0: table.sym("_face_gfx_data+0xC0"), # la
    0x801A90C8: table.sym("_face_gfx_data+0x8C8"), # la
    0x801B1B48: table.sym("_face_gfx_data+0x9348"), # la
    0x801B1B88: table.sym("_face_gfx_data+0x9388"), # la
    0x801B4E28: table.sym("_face_gfx_data+0xC628"), # la
    0x801B4E58: table.sym("_face_gfx_data+0xC658"), # la
    0x801B5290: table.sym("_face_gfx_data+0xCA90"), # la
    0x801B5300: table.sym("_face_gfx_data+0xCB00"), # la
    0x801B5318: table.sym("_face_gfx_data+0xCB18"), # la
    0x801B539C: table.sym("_face_gfx_data+0xCB9C"),
    0x801B5468: table.sym("_face_gfx_data+0xCC68"), # la

    0x801B9AB0: table.sym("_face_bss+0x00"),
    0x801B9AD8: table.sym("_face_bss+0x28"),
    0x801B9ADC: table.sym("_face_bss+0x2C"),
    0x801B9AE0: table.sym("_face_bss+0x30"),
    0x801B9AF8: table.sym("_face_bss+0x48"),
    0x801B9B04: table.sym("_face_bss+0x54"),
    0x801B9B38: table.sym("_face_bss+0x88"),
    0x801B9B50: table.sym("_face_bss+0xA0"),
    0x801B9B5C: table.sym("_face_bss+0xAC"),
    0x801B9B68: table.sym("_face_bss+0xB8"),
    0x801B9B6C: table.sym("_face_bss+0xBC"),
    0x801B9B80: table.sym("_face_bss+0xD0"),
    0x801B9B84: table.sym("_face_bss+0xD4"),
    0x801B9B88: table.sym("_face_bss+0xD8"),
    0x801B9B8C: table.sym("_face_bss+0xDC"),
    0x801B9B98: table.sym("_face_bss+0xE8"),
    0x801B9BA0: table.sym("_face_bss+0xF0"),
    0x801B9BA8: table.sym("_face_bss+0xF8"), # la
    0x801B9CA0: table.sym("_face_bss+0x1F0"),
    0x801B9CA4: table.sym("_face_bss+0x1F4"),
    0x801B9CA8: table.sym("_face_bss+0x1F8"),
    0x801B9CB0: table.sym("_face_bss+0x200"),
    0x801B9CB4: table.sym("_face_bss+0x204"),
    0x801B9D48: table.sym("_face_bss+0x298"),
    0x801B9D90: table.sym("_face_bss+0x2E0"),
    0x801B9D94: table.sym("_face_bss+0x2E4"),
    0x801B9D98: table.sym("_face_bss+0x2E8"),
    0x801B9E60: table.sym("_face_bss+0x3B0"),
    0x801B9E64: table.sym("_face_bss+0x3B4"),
    0x801B9E68: table.sym("_face_bss+0x3B8"),
    0x801B9E74: table.sym("_face_bss+0x3C4"),
    0x801B9E78: table.sym("_face_bss+0x3C8"),
    0x801B9E7C: table.sym("_face_bss+0x3CC"),
    0x801B9E80: table.sym("_face_bss+0x3D0"),
    0x801B9E84: table.sym("_face_bss+0x3D4"),
    0x801B9E88: table.sym("_face_bss+0x3D8"),
    0x801B9E90: table.sym("_face_bss+0x3E0"),
    0x801B9E94: table.sym("_face_bss+0x3E4"),
    0x801B9E98: table.sym("_face_bss+0x3E8"),
    0x801B9EA0: table.sym("_face_bss+0x3F0"),
    0x801B9EA4: table.sym("_face_bss+0x3F4"),
    0x801B9EA8: table.sym("_face_bss+0x3F8"),
    0x801B9EB0: table.sym("_face_bss+0x400"),
    0x801B9EB4: table.sym("_face_bss+0x404"),
    0x801B9EB8: table.sym("_face_bss+0x408"),
    0x801B9F10: table.sym("_face_bss+0x460"),
    0x801B9F18: table.sym("_face_bss+0x468"),
    0x801B9F1C: table.sym("_face_bss+0x46C"),
    0x801B9F30: table.sym("_face_bss+0x480"),
    0x801B9F34: table.sym("_face_bss+0x484"),
    0x801B9F38: table.sym("_face_bss+0x488"),
    0x801B9F3C: table.sym("_face_bss+0x48C"),
    0x801B9F40: table.sym("_face_bss+0x490"),
    0x801B9F44: table.sym("_face_bss+0x494"),
    0x801B9F48: table.sym("_face_bss+0x498"),
    0x801B9F4C: table.sym("_face_bss+0x49C"),
    0x801B9F50: table.sym("_face_bss+0x4A0"),
    0x801B9F54: table.sym("_face_bss+0x4A4"),
    0x801B9F58: table.sym("_face_bss+0x4A8"), # la
    0x801B9F98: table.sym("_face_bss+0x4E8"),
    0x801B9F9C: table.sym("_face_bss+0x4EC"),
    0x801B9FA0: table.sym("_face_bss+0x4F0"),
    0x801B9FA4: table.sym("_face_bss+0x4F4"),
    0x801B9FA8: table.sym("_face_bss+0x4F8"),
    0x801B9FAC: table.sym("_face_bss+0x4FC"),
    0x801B9FB0: table.sym("_face_bss+0x500"),
    0x801B9FB8: table.sym("_face_bss+0x508"),
    0x801B9FBC: table.sym("_face_bss+0x50C"),
    0x801B9FC0: table.sym("_face_bss+0x510"),
    0x801B9FC4: table.sym("_face_bss+0x514"),
    0x801B9FC8: table.sym("_face_bss+0x518"),
    0x801B9FCC: table.sym("_face_bss+0x51C"),
    0x801B9FD0: table.sym("_face_bss+0x520"),
    0x801B9FD4: table.sym("_face_bss+0x524"),
    0x801B9FD8: table.sym("_face_bss+0x528"),
    0x801B9FDC: table.sym("_face_bss+0x52C"),
    0x801B9FE0: table.sym("_face_bss+0x530"),
    0x801B9FE4: table.sym("_face_bss+0x534"),
    0x801B9FE8: table.sym("_face_bss+0x538"),
    0x801B9FEC: table.sym("_face_bss+0x53C"),
    0x801B9FF0: table.sym("_face_bss+0x540"),
    0x801B9FF4: table.sym("_face_bss+0x544"),
    0x801B9FF8: table.sym("_face_bss+0x548"),
    0x801BA010: table.sym("_face_bss+0x560"),
    0x801BA014: table.sym("_face_bss+0x564"),
    0x801BA018: table.sym("_face_bss+0x568"),
    0x801BA01C: table.sym("_face_bss+0x56C"),
    0x801BA020: table.sym("_face_bss+0x570"),
    0x801BA030: table.sym("_face_bss+0x580"),
    0x801BA038: table.sym("_face_bss+0x588"), # la
    0x801BA078: table.sym("_face_bss+0x5C8"),
    0x801BA080: table.sym("_face_bss+0x5D0"),
    0x801BA090: table.sym("_face_bss+0x5E0"), # la
    0x801BA098: table.sym("_face_bss+0x5E8"), # la
    0x801BA0B0: table.sym("_face_bss+0x600"), # la
    0x801BA0B8: table.sym("_face_bss+0x608"),
    0x801BA0BC: table.sym("_face_bss+0x60C"),
    0x801BA0C0: table.sym("_face_bss+0x610"),
    0x801BA0C4: table.sym("_face_bss+0x614"),
    0x801BA0C8: table.sym("_face_bss+0x618"),
    0x801BA0CC: table.sym("_face_bss+0x61C"),
    0x801BA0D0: table.sym("_face_bss+0x620"),
    0x801BA0D8: table.sym("_face_bss+0x628"), # la
    0x801BA0F8: table.sym("_face_bss+0x648"), # la
    0x801BA200: table.sym("_face_bss+0x750"), # la
    0x801BA300: table.sym("_face_bss+0x850"),
    0x801BA304: table.sym("_face_bss+0x854"),
    0x801BA308: table.sym("_face_bss+0x858"),
    0x801BA31C: table.sym("_face_bss+0x86C"),
    0x801BA320: table.sym("_face_bss+0x870"),
    0x801BA328: table.sym("_face_bss+0x878"),
    0x801BA428: table.sym("_face_bss+0x978"),
    0x801BA430: table.sym("_face_bss+0x980"), # la
    0x801BA438: table.sym("_face_bss+0x988"),
    0x801BA43C: table.sym("_face_bss+0x98C"),
    0x801BA440: table.sym("_face_bss+0x990"),
    0x801BA444: table.sym("_face_bss+0x994"),
    0x801BA448: table.sym("_face_bss+0x998"),
    0x801BA44C: table.sym("_face_bss+0x99C"),
    0x801BA450: table.sym("_face_bss+0x9A0"),
    0x801BA8B0: table.sym("_face_bss+0xE00"),
    0x801BA8B4: table.sym("_face_bss+0xE04"),
    0x801BA8B8: table.sym("_face_bss+0xE08"),
    0x801BA8BC: table.sym("_face_bss+0xE0C"),
    0x801BAAAC: table.sym("_face_bss+0xFFC"),
    0x801BAAB0: table.sym("_face_bss+0x1000"),
    0x801BAAF0: table.sym("_face_bss+0x1040"),
    0x801BAAF4: table.sym("_face_bss+0x1044"),
    0x801BAAF8: table.sym("_face_bss+0x1048"),
    0x801BAAFC: table.sym("_face_bss+0x104C"),
    0x801BAB00: table.sym("_face_bss+0x1050"),
    0x801BAB04: table.sym("_face_bss+0x1054"),
    0x801BAB08: table.sym("_face_bss+0x1058"),
    0x801BAB0C: table.sym("_face_bss+0x105C"),
    0x801BAB10: table.sym("_face_bss+0x1060"),
    0x801BAB18: table.sym("_face_bss+0x1068"),
    0x801BAB40: table.sym("_face_bss+0x1090"),
    0x801BAB44: table.sym("_face_bss+0x1094"),
    0x801BAB48: table.sym("_face_bss+0x1098"),
    0x801BABB8: table.sym("_face_bss+0x1108"),
    0x801BABC0: table.sym("_face_bss+0x1110"),
    0x801BABE8: table.sym("_face_bss+0x1138"),
    0x801BABEC: table.sym("_face_bss+0x113C"),
    0x801BABF0: table.sym("_face_bss+0x1140"),
    0x801BAC60: table.sym("_face_bss+0x11B0"),
    0x801BAC64: table.sym("_face_bss+0x11B4"),
    0x801BAC68: table.sym("_face_bss+0x11B8"),
    0x801BAC70: table.sym("_face_bss+0x11C0"),
    0x801BAC74: table.sym("_face_bss+0x11C4"),
    0x801BAC78: table.sym("_face_bss+0x11C8"),
    0x801BAC80: table.sym("_face_bss+0x11D0"),
    0x801BAC84: table.sym("_face_bss+0x11D4"),
    0x801BAC88: table.sym("_face_bss+0x11D8"),
    0x801BACBC: table.sym("_face_bss+0x120C"),
    0x801BACCC: table.sym("_face_bss+0x121C"),
    0x801BACD8: table.sym("_face_bss+0x1228"),
    0x801BADD8: table.sym("_face_bss+0x1328"),
    0x801BADDC: table.sym("_face_bss+0x132C"),
    0x801BADE0: table.sym("_face_bss+0x1330"),
    0x801BADE4: table.sym("_face_bss+0x1334"),
    0x801BADF0: table.sym("_face_bss+0x1340"),
    0x801BADF4: table.sym("_face_bss+0x1344"),
    0x801BADF8: table.sym("_face_bss+0x1348"),
    0x801BAE04: table.sym("_face_bss+0x1354"),
    0x801BAE08: table.sym("_face_bss+0x1358"),
    0x801BAE2C: table.sym("_face_bss+0x137C"),
    0x801BAE30: table.sym("_face_bss+0x1380"),
    0x801BAE48: table.sym("_face_bss+0x1398"),
    0x801BAE4C: table.sym("_face_bss+0x139C"),
    0x801BAE50: table.sym("_face_bss+0x13A0"),
    0x801BAE58: table.sym("_face_bss+0x13A8"),
    0x801BAE5C: table.sym("_face_bss+0x13AC"),
    0x801BAE60: table.sym("_face_bss+0x13B0"),
    0x801BAE98: table.sym("_face_bss+0x13E8"),
    0x801BAEC0: table.sym("_face_bss+0x1410"),
    0x801BAEC4: table.sym("_face_bss+0x1414"),
    0x801BAEC8: table.sym("_face_bss+0x1418"),
    0x801BAFF0: table.sym("_face_bss+0x1540"), # la
    0x801BB000: table.sym("_face_bss+0x1550"), # la
    0x801BB018: table.sym("_face_bss+0x1568"), # la
    0x801BB030: table.sym("_face_bss+0x1580"), # la
    0x801BB038: table.sym("_face_bss+0x1588"),
    0x801BB0B8: table.sym("_face_bss+0x1608"),
    0x801BB0C0: table.sym("_face_bss+0x1610"),
    0x801BB19C: table.sym("_face_bss+0x16EC"),
    0x801BB1A0: table.sym("_face_bss+0x16F0"),
    0x801BB1A8: table.sym("_face_bss+0x16F8"),
    0x801BB1AC: table.sym("_face_bss+0x16FC"),
    0x801BB1B0: table.sym("_face_bss+0x1700"),
    0x801BB1F0: table.sym("_face_bss+0x1740"),
    0x801BB230: table.sym("_face_bss+0x1780"), # la
    0x801BB234: table.sym("_face_bss+0x1784"),
    0x801BB238: table.sym("_face_bss+0x1788"),
    0x801BB23C: table.sym("_face_bss+0x178C"),
    0x801BB240: table.sym("_face_bss+0x1790"),
    0x801BB244: table.sym("_face_bss+0x1794"),
    0x801BB248: table.sym("_face_bss+0x1798"),
    0x801BB24C: table.sym("_face_bss+0x179C"),
    0x801BB250: table.sym("_face_bss+0x17A0"),
    0x801BB254: table.sym("_face_bss+0x17A4"),
    0x801BB258: table.sym("_face_bss+0x17A8"),
    0x801BB25C: table.sym("_face_bss+0x17AC"),
    0x801BB260: table.sym("_face_bss+0x17B0"),
    0x801BB264: table.sym("_face_bss+0x17B4"),
    0x801BB268: table.sym("_face_bss+0x17B8"),
    0x801BB270: table.sym("_face_bss+0x17C0"),
    0x801BB278: table.sym("_face_bss+0x17C8"),
    0x801BB27C: table.sym("_face_bss+0x17CC"),
    0x801BB280: table.sym("_face_bss+0x17D0"),
    0x801BB290: table.sym("_face_bss+0x17E0"), # la
    0x801BB2D0: table.sym("_face_bss+0x1820"), # la
    0x801BB310: table.sym("_face_bss+0x1860"), # la
    0x801BB314: table.sym("_face_bss+0x1864"),
    0x801BB318: table.sym("_face_bss+0x1868"),
    0x801BB320: table.sym("_face_bss+0x1870"),
    0x801BB324: table.sym("_face_bss+0x1874"),
    0x801BB328: table.sym("_face_bss+0x1878"),
    0x801BB330: table.sym("_face_bss+0x1880"),
    0x801BB334: table.sym("_face_bss+0x1884"),
    0x801BB338: table.sym("_face_bss+0x1888"),
    0x801BB348: table.sym("_face_bss+0x1898"),
    0x801BB34B: table.sym("_face_bss+0x189B"),
    0x801BB34C: table.sym("_face_bss+0x189C"),
    0x801BB34F: table.sym("_face_bss+0x189F"),
    0x801BB350: table.sym("_face_bss+0x18A0"),
    0x801BB353: table.sym("_face_bss+0x18A3"),
    0x801BB360: table.sym("_face_bss+0x18B0"),
    0x801BB368: table.sym("_face_bss+0x18B8"), # la
    0x801BD8E8: table.sym("_face_bss+0x3E38"),
    0x801BD8EC: table.sym("_face_bss+0x3E3C"),
    0x801BD8F0: table.sym("_face_bss+0x3E40"),
    0x801BD8F8: table.sym("_face_bss+0x3E48"),
    0x801BD8FC: table.sym("_face_bss+0x3E4C"),
    0x801BD900: table.sym("_face_bss+0x3E50"),
    0x801BD904: table.sym("_face_bss+0x3E54"),
    0x801BD908: table.sym("_face_bss+0x3E58"),
    0x801BD92C: table.sym("_face_bss+0x3E7C"),
    0x801BD930: table.sym("_face_bss+0x3E80"),
    0x801BD938: table.sym("_face_bss+0x3E88"),
    0x801BD940: table.sym("_face_bss+0x3E90"),
    0x801BD948: table.sym("_face_bss+0x3E98"),
    0x801BD950: table.sym("_face_bss+0x3EA0"),
    0x801BD958: table.sym("_face_bss+0x3EA8"),
    0x801BD95C: table.sym("_face_bss+0x3EAC"),
    0x801BD970: table.sym("_face_bss+0x3EC0"),
    0x801BE910: table.sym("_face_bss+0x4E60"),
    0x801BE914: table.sym("_face_bss+0x4E64"),
    0x801BE918: table.sym("_face_bss+0x4E68"),
    0x801BE920: table.sym("_face_bss+0x4E70"), # la
    0x801BE960: table.sym("_face_bss+0x4EB0"), # la
    0x801BE9C0: table.sym("_face_bss+0x4F10"), # la
    0x801BE9D8: table.sym("_face_bss+0x4F28"), # la
    0x801BEA40: table.sym("_face_bss+0x4F90"), # la
    0x801BEA48: table.sym("_face_bss+0x4F98"),
    0x801BEA50: table.sym("_face_bss+0x4FA0"),
    0x801BEA58: table.sym("_face_bss+0x4FA8"), # la
    0x801BEAD4: table.sym("_face_bss+0x5024"), # la
    0x801BEB0C: table.sym("_face_bss+0x505C"), # la
    0x801BEB10: table.sym("_face_bss+0x5060"), # la
    0x801BEB24: table.sym("_face_bss+0x5074"),
}

sym_E0_d_menu = {
    # data
    # src/title.c
    0x801A7830: table.sym_var("str_stage",  "char", "[64][16]", table.GLOBL),
    0x801A7C30: table.sym_var("title_801A7C30", "u16",  flag=table.GLOBL|ultra.DALIGN),
    0x801A7C34: table.sym_var("title_801A7C34", "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x801A7C38: table.sym_var("title_801A7C38", "s16",  flag=table.GLOBL|ultra.DALIGN),

    # rodata
    # src/title.c
    0x801A7C40: table.sym_var("str_title_select_stage",         "const char", "[]"),
    0x801A7C50: table.sym_var("str_title_press_start_button",   "const char", "[]"),
    0x801A7C64: table.sym_var("str_title_stage_fmt",            "const char", "[]"),

    # data
    # src/title_bg.c
    0x801A7C70: table.sym_var("gfx_title_bg",       "Gfx *", "[]",  table.GLOBL),
    0x801A7C80: table.sym_var("title_bg_x",         "f32", "[]",    table.GLOBL),
    0x801A7CB0: table.sym_var("title_bg_y",         "f32", "[]",    table.GLOBL),
    0x801A7CE0: table.sym_var("txt_title_bg",       "u16 **", "[]", table.GLOBL),
    0x801A7CE8: table.sym_var("title_bg_mario",     "static s8", "[]"),
    0x801A7CF4: table.sym_var("title_bg_table",     "s8 *", "[]",   table.GLOBL),
    0x801A7CF8: table.sym_var("title_bg_gameover",  "s8", "[]", table.GLOBL),
    0x801A7D04: table.sym_var("title_bg_flip",      "s8", "[]", table.GLOBL),

    # data
    # src/file_select.c
    0x801A7D10: table.sym_var("file_select_801A7D10",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A7D14: table.sym_var("file_select_801A7D14",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A7D18: table.sym_var("file_select_801A7D18",   "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A7D1C: table.sym_var("file_select_801A7D1C",   "f32", "[2]",   table.GLOBL),
    0x801A7D24: table.sym_var("file_select_801A7D24",   "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x801A7D28: table.sym_var("file_select_801A7D28",   "s16", "[2]",   table.GLOBL),
    0x801A7D2C: table.sym_var("file_select_801A7D2C",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A7D30: table.sym_var("file_select_801A7D30",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A7D34: table.sym_var("file_select_801A7D34",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A7D38: table.sym_var("file_select_801A7D38",   "u8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A7D3C: table.sym_var("file_select_801A7D3C",   "s16",  flag=table.GLOBL|ultra.DALIGN),
    0x801A7D40: table.sym_var("file_select_801A7D40",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A7D44: table.sym_var("file_select_801A7D44",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A7D48: table.sym_var("file_select_801A7D48",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A7D4C: table.sym_var("file_select_801A7D4C",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A7D50: table.sym_var("file_select_801A7D50",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A7D54: table.sym_var("str_801A7D54",   "u8", "[]", table.GLOBL), # RETURN
    0x801A7D5C: table.sym_var("str_801A7D5C",   "u8", "[]", table.GLOBL), # CHECK SCORE
    0x801A7D68: table.sym_var("str_801A7D68",   "u8", "[]", table.GLOBL), # COPY FILE
    0x801A7D74: table.sym_var("str_801A7D74",   "u8", "[]", table.GLOBL), # ERASE FILE
    0x801A7D80: table.sym_var("str_801A7D80",   "u8", "[][8]",  table.GLOBL), # STEREO;MONO;HEADSET
    0x801A7D98: table.sym_var("str_801A7D98",   "u8", "[]", table.GLOBL), # MARIO A
    0x801A7DA0: table.sym_var("str_801A7DA0",   "u8", "[]", table.GLOBL), # MARIO B
    0x801A7DA8: table.sym_var("str_801A7DA8",   "u8", "[]", table.GLOBL), # MARIO C
    0x801A7DB0: table.sym_var("str_801A7DB0",   "u8", "[]", table.GLOBL), # MARIO D
    0x801A7DB8: table.sym_var("str_801A7DB8",   "u8", "[]", table.GLOBL), # NEW
    0x801A7DBC: table.sym_var("str_801A7DBC",   "u8", "[]", table.GLOBL), # [*]
    0x801A7DC0: table.sym_var("str_801A7DC0",   "u8", "[]", table.GLOBL), # [x]
    0x801A7DC4: table.sym_var("str_801A7DC4",   "u8", "[]", table.GLOBL), # SELECT FILE
    0x801A7DD0: table.sym_var("str_801A7DD0",   "u8", "[]", table.GLOBL), # SCORE
    0x801A7DD8: table.sym_var("str_801A7DD8",   "u8", "[]", table.GLOBL), # COPY
    0x801A7DE0: table.sym_var("str_801A7DE0",   "u8", "[]", table.GLOBL), # ERASE
    0x801A7DE8: table.sym_var("str_801A7DE8",   "u8", "[]", table.GLOBL), # CHECK FILE
    0x801A7DF4: table.sym_var("str_801A7DF4",   "u8", "[]", table.GLOBL), # NO SAVED DATA EXISTS
    0x801A7E0C: table.sym_var("str_801A7E0C",   "u8", "[]", table.GLOBL), # COPY FILE
    0x801A7E18: table.sym_var("str_801A7E18",   "u8", "[]", table.GLOBL), # COPY IT TO WHERE?
    0x801A7E2C: table.sym_var("str_801A7E2C",   "u8", "[]", table.GLOBL), # NO SAVED DATA EXISTS
    0x801A7E44: table.sym_var("str_801A7E44",   "u8", "[]", table.GLOBL), # COPYING COMPLETED
    0x801A7E58: table.sym_var("str_801A7E58",   "u8", "[]", table.GLOBL), # SAVED DATA EXITS
    0x801A7E6C: table.sym_var("str_801A7E6C",   "u8", "[]", table.GLOBL), # NO EMPTY FILE
    0x801A7E7C: table.sym_var("str_801A7E7C",   "u8", "[]", table.GLOBL), # YES
    0x801A7E80: table.sym_var("str_801A7E80",   "u8", "[]", table.GLOBL), # NO
    0x801A7E84: table.sym_var("str_801A7E84",   "u8", "[]", table.GLOBL), # ERASE FILE
    0x801A7E90: table.sym_var("str_801A7E90",   "u8", "[]", table.GLOBL), # SURE?
    0x801A7E98: table.sym_var("str_801A7E98",   "u8", "[]", table.GLOBL), # NO SAVED DATA EXISTS
    0x801A7EB0: table.sym_var("str_801A7EB0",   "u8", "[]", table.GLOBL), # MARIO A JUST ERASED
    0x801A7EC4: table.sym_var("str_801A7EC4",   "u8", "[]", table.GLOBL), # SAVED DATA EXITS
    0x801A7ED8: table.sym_var("str_801A7ED8",   "u8", "[]", table.GLOBL), # SOUND SELECT
    0x801A7EE8: table.sym_var("str_801A7EE8",   "u8", "[]", table.GLOBL), # [*][x]
    0x801A7EEC: table.sym_var("str_801A7EEC",   "u8", "[]", table.GLOBL), # [+][x]
    0x801A7EF0: table.sym_var("str_801A7EF0",   "u8", "[]", table.GLOBL), # [*]
    0x801A7EF4: table.sym_var("str_801A7EF4",   "u8", "[][8]",  table.GLOBL), # ----;[M]A;[M]B;[M]C;[M]D
    0x801A7F1C: table.sym_var("str_801A7F1C",   "u8", "[]", table.GLOBL), # MARIO
    0x801A7F24: table.sym_var("str_801A7F24",   "u8", "[]", table.GLOBL), # HI SCORE
    0x801A7F30: table.sym_var("str_801A7F30",   "u8", "[]", table.GLOBL), # MY SCORE
    0x801A7F3C: table.sym_var("file_select_801A7F3C",   "s16",  flag=table.GLOBL|ultra.DALIGN),

    # rodata
    # src/file_select.c
    0x801A7F40: table.sym_var("file_select_801A7F40", "const float"),
    0x801A7F48: table.sym_var("file_select_801A7F48", "const double"),
    0x801A7F50: table.sym_var("file_select_801A7F50", "const double"),
    0x801A7F58: table.sym_var("file_select_801A7F58", "const double"),
    0x801A7F60: table.sym_var("file_select_801A7F60", "const double"),
    0x801A7F68: table.sym_var("file_select_801A7F68", "const double"),
    0x801A7F70: table.sym_var("file_select_801A7F70", "const double"),
    0x801A7F78: table.sym_var("file_select_801A7F78", "const double"),
    0x801A7F80: table.sym_var_fnc("file_select_801A7F80", "const", "[]"),
    0x801A7F9C: table.sym_var("file_select_801A7F9C", "const float"),
    0x801A7FA0: table.sym_var("file_select_801A7FA0", "const float"),
    0x801A7FA4: table.sym_var("file_select_801A7FA4", "const float"),
    0x801A7FA8: table.sym_var("file_select_801A7FA8", "const float"),
    0x801A7FAC: table.sym_var("file_select_801A7FAC", "const float"),
    0x801A7FB0: table.sym_var("file_select_801A7FB0", "const float"),
    0x801A7FB4: table.sym_var("file_select_801A7FB4", "const float"),
    0x801A7FB8: table.sym_var("file_select_801A7FB8", "const float"),
    0x801A7FBC: table.sym_var("file_select_801A7FBC", "const float"),
    0x801A7FC0: table.sym_var("file_select_801A7FC0", "const float"),
    0x801A7FC4: table.sym_var("file_select_801A7FC4", "const float"),
    0x801A7FC8: table.sym_var("file_select_801A7FC8", "const float"),
    0x801A7FCC: table.sym_var("file_select_801A7FCC", "const float"),
    0x801A7FD0: table.sym_var("file_select_801A7FD0", "const float"),
    0x801A7FD4: table.sym_var("file_select_801A7FD4", "const float"),
    0x801A7FD8: table.sym_var("file_select_801A7FD8", "const float"),
    0x801A7FDC: table.sym_var("file_select_801A7FDC", "const float"),
    0x801A7FE0: table.sym_var("file_select_801A7FE0", "const float"),
    0x801A7FE4: table.sym_var("file_select_801A7FE4", "const float"),
    0x801A7FE8: table.sym_var("file_select_801A7FE8", "const float"),
    0x801A7FEC: table.sym_var("file_select_801A7FEC", "const float"),
    0x801A7FF0: table.sym_var("file_select_801A7FF0", "const float"),
    0x801A7FF4: table.sym_var("file_select_801A7FF4", "const float"),
    0x801A7FF8: table.sym_var("file_select_801A7FF8", "const float"),
    0x801A7FFC: table.sym_var_fnc("file_select_801A7FFC", "const", "[]"),
    0x801A8070: table.sym_var_fnc("file_select_801A8070", "const", "[]"),
    0x801A80F4: table.sym_var_fnc("file_select_801A80F4", "const", "[]"),
    0x801A8108: table.sym_var_fnc("file_select_801A8108", "const", "[]"),
    0x801A811C: table.sym_var_fnc("file_select_801A811C", "const", "[]"),

    # data
    # src/star_select.c
    0x801A81A0: table.sym_var("star_select_801A81A0",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A81A4: table.sym_var("star_select_801A81A4",   "s8",   flag=table.GLOBL|ultra.DALIGN),
    0x801A81A8: table.sym_var("star_select_801A81A8",   "s32",  flag=table.GLOBL|ultra.DALIGN),
    0x801A81AC: table.sym_var("str_801A81AC",   "u8", "[]", table.GLOBL), # MYSCORE
    0x801A81B4: table.sym_var("star_select_801A81B4",   "u16",  flag=table.GLOBL|ultra.DALIGN),

    # rodata
    # src/star_select.c
    0x801A81C0: table.sym_var("star_select_801A81C0", "const double"),
    0x801A81C8: table.sym_var("star_select_801A81C8", "const double"),
    0x801A81D0: table.sym_var("star_select_801A81D0", "const double"),
    0x801A81D8: table.sym_var("star_select_801A81D8", "const float"),
    0x801A81DC: table.sym_var("star_select_801A81DC", "const float"),

    # ==========================================================================
    # bss
    # ==========================================================================

    # src/title_bg.c
    0x801B99E0: table.sym_var("title_bg_801B99E0",  "u32",   flag=table.GLOBL),
    0x801B99E4: table.sym_var("title_bg_801B99E4",  "s32",   flag=table.GLOBL),
    0x801B99E8: table.sym_var("title_bg_801B99E8",  "s16",   flag=table.GLOBL),
    0x801B99EC: table.sym_var("title_bg_801B99EC",  "s32",   flag=table.GLOBL),

    # src/file_select.c
    0x801B99F0: table.sym_var("file_select_801B99F0",   "s16",  flag=table.GLOBL),
    0x801B99F8: table.sym_var("file_select_801B99F8",   "OBJECT *", "[32]",  table.GLOBL|ultra.BALIGN),
    0x801B9A78: table.sym_var("file_select_801B9A78",   "u8", "[2]",    table.GLOBL|ultra.BALIGN),

    # src/star_select.c
    0x801B9A80: table.sym_var("star_select_801B9A80",   "OBJECT *", "[8]",   table.GLOBL|ultra.BALIGN),
    0x801B9AA0: table.sym_var("star_select_801B9AA0",   "s8",   flag=table.GLOBL),
    0x801B9AA1: table.sym_var("star_select_801B9AA1",   "u8",   flag=table.GLOBL),
    0x801B9AA2: table.sym_var("star_select_801B9AA2",   "s8",   flag=table.GLOBL),
    0x801B9AA3: table.sym_var("star_select_801B9AA3",   "u8",   flag=table.GLOBL),

    # ==========================================================================
    # data
    # ==========================================================================

    # src/face/main.c
    0x801A81E0: table.sym_var("face_movement",      "int",  flag=table.GLOBL|ultra.DALIGN),
    0x801A81E4: table.sym_var("face_config_1",      "int",  flag=table.GLOBL|ultra.DALIGN), # unused
    0x801A81E8: table.sym_var("face_config_2",      "f32",  flag=table.GLOBL|ultra.DALIGN),
    0x801A81EC: table.sym_var("face_shade_smooth",  "int",  flag=table.GLOBL|ultra.DALIGN),
    0x801A81F0: table.sym_var("face_window_w",      "int",  flag=table.GLOBL|ultra.DALIGN), # unused
    0x801A81F4: table.sym_var("face_window_h",      "int",  flag=table.GLOBL|ultra.DALIGN), # unused

    # ==========================================================================
    # rodata
    # ==========================================================================

    # src/face/main.c
    0x801B54C0: table.sym_var("str_face_main_801B54C0", "const char", "[]"),
    0x801B54C8: table.sym_var("str_face_main_801B54C8", "const char", "[]"),
    0x801B54D0: table.sym_var("str_face_main_801B54D0", "const char", "[]"),
    0x801B54E4: table.sym_var("str_face_main_801B54E4", "const char", "[]"),
    0x801B54EC: table.sym_var("str_face_main_801B54EC", "const char", "[]"),
    0x801B54F4: table.sym_var("face_main_801B54F4", "const float"),

    # src/face/mem.c
    0x801B5500: table.sym_var("str_face_mem_801B5500", "const char", "[]"),
    0x801B5524: table.sym_var("str_face_mem_801B5524", "const char", "[]"),
    0x801B553C: table.sym_var("str_face_mem_801B553C", "const char", "[]"),
    0x801B555C: table.sym_var("str_face_mem_801B555C", "const char", "[]"),
    0x801B5574: table.sym_var("str_face_mem_801B5574", "const char", "[]"),
    0x801B559C: table.sym_var("str_face_mem_801B559C", "const char", "[]"),
    0x801B55B0: table.sym_var("str_face_mem_801B55B0", "const char", "[]"),
    0x801B55B4: table.sym_var("str_face_mem_801B55B4", "const char", "[]"),
    0x801B55C8: table.sym_var("str_face_mem_801B55C8", "const char", "[]"),
    0x801B55CC: table.sym_var("str_face_mem_801B55CC", "const char", "[]"),
    0x801B55E0: table.sym_var("str_face_mem_801B55E0", "const char", "[]"),
    0x801B55E4: table.sym_var("str_face_mem_801B55E4", "const char", "[]"),
    0x801B55F8: table.sym_var("str_face_mem_801B55F8", "const char", "[]"),
    0x801B55FC: table.sym_var("str_face_mem_801B55FC", "const char", "[]"),

    # src/face/draw.c
    0x801B5610: table.sym_var("str_face_draw_801B5610", "const char", "[]"),
    0x801B561C: table.sym_var("str_face_draw_801B561C", "const char", "[]"),
    0x801B5638: table.sym_var("str_face_draw_801B5638", "const char", "[]"),
    0x801B5644: table.sym_var("str_face_draw_801B5644", "const char", "[]"),
    0x801B5650: table.sym_var("str_face_draw_801B5650", "const char", "[]"),
    0x801B565C: table.sym_var("str_face_draw_801B565C", "const char", "[]"),
    0x801B5688: table.sym_var("str_face_draw_801B5688", "const char", "[]"),
    0x801B5690: table.sym_var("str_face_draw_801B5690", "const char", "[]"),
    0x801B56A4: table.sym_var("str_face_draw_801B56A4", "const char", "[]"),
    0x801B56B0: table.sym_var("str_face_draw_801B56B0", "const char", "[]"),
    0x801B56B8: table.sym_var("str_face_draw_801B56B8", "const char", "[]"),
    0x801B56C0: table.sym_var("str_face_draw_801B56C0", "const char", "[]"),
    0x801B56CC: table.sym_var("str_face_draw_801B56CC", "const char", "[]"),
    0x801B56F0: table.sym_var("str_face_draw_801B56F0", "const char", "[]"),
    0x801B56FC: table.sym_var("str_face_draw_801B56FC", "const char", "[]"),
    0x801B570C: table.sym_var("str_face_draw_801B570C", "const char", "[]"),
    0x801B5714: table.sym_var("str_face_draw_801B5714", "const char", "[]"),
    0x801B571C: table.sym_var("str_face_draw_801B571C", "const char", "[]"),
    0x801B5724: table.sym_var("str_face_draw_801B5724", "const char", "[]"),
    0x801B5734: table.sym_var("str_face_draw_801B5734", "const char", "[]"),
    0x801B573C: table.sym_var("str_face_draw_801B573C", "const char", "[]"),
    0x801B5748: table.sym_var("str_face_draw_801B5748", "const char", "[]"),
    0x801B576C: table.sym_var("str_face_draw_801B576C", "const char", "[]"),
    0x801B5778: table.sym_var("str_face_draw_801B5778", "const char", "[]"),
    0x801B5788: table.sym_var("str_face_draw_801B5788", "const char", "[]"),
    0x801B5798: table.sym_var("str_face_draw_801B5798", "const char", "[]"),
    0x801B57C4: table.sym_var("str_face_draw_801B57C4", "const char", "[]"),
    0x801B57F4: table.sym_var("str_face_draw_801B57F4", "const char", "[]"),
    0x801B580C: table.sym_var("str_face_draw_801B580C", "const char", "[]"),
    0x801B5834: table.sym_var("str_face_draw_801B5834", "const char", "[]"),
    0x801B5844: table.sym_var("str_face_draw_801B5844", "const char", "[]"),
    0x801B5854: table.sym_var("str_face_draw_801B5854", "const char", "[]"),
    0x801B585C: table.sym_var("str_face_draw_801B585C", "const char", "[]"),
    0x801B5868: table.sym_var("str_face_draw_801B5868", "const char", "[]"),
    0x801B5874: table.sym_var("str_face_draw_801B5874", "const char", "[]"),
    0x801B587C: table.sym_var("str_face_draw_801B587C", "const char", "[]"),
    0x801B58A0: table.sym_var("str_face_draw_801B58A0", "const char", "[]"),
    0x801B58A4: table.sym_var("str_face_draw_801B58A4", "const char", "[]"),
    0x801B58A8: table.sym_var("str_face_draw_801B58A8", "const char", "[]"),
    0x801B58AC: table.sym_var("str_face_draw_801B58AC", "const char", "[]"),
    0x801B58B0: table.sym_var("face_draw_801B58B0", "const double"),
    0x801B58B8: table.sym_var("face_draw_801B58B8", "const double"),
    0x801B58C0: table.sym_var_fnc("face_draw_801B58C0", "const", "[]"),
    0x801B58F0: table.sym_var("face_draw_801B58F0", "const double"),
    0x801B58F8: table.sym_var("face_draw_801B58F8", "const double"),
    0x801B5900: table.sym_var("face_draw_801B5900", "const double"),
    0x801B5908: table.sym_var("face_draw_801B5908", "const double"),
    0x801B5910: table.sym_var("face_draw_801B5910", "const float"),

    # src/face/object.c
    0x801B5920: table.sym_var("str_face_object_801B5920", "const char", "[]"),
    0x801B5928: table.sym_var("str_face_object_801B5928", "const char", "[]"),
    0x801B5930: table.sym_var("str_face_object_801B5930", "const char", "[]"),
    0x801B5938: table.sym_var("str_face_object_801B5938", "const char", "[]"),
    0x801B5944: table.sym_var("str_face_object_801B5944", "const char", "[]"),
    0x801B594C: table.sym_var("str_face_object_801B594C", "const char", "[]"),
    0x801B5954: table.sym_var("str_face_object_801B5954", "const char", "[]"),
    0x801B595C: table.sym_var("str_face_object_801B595C", "const char", "[]"),
    0x801B5968: table.sym_var("str_face_object_801B5968", "const char", "[]"),
    0x801B5970: table.sym_var("str_face_object_801B5970", "const char", "[]"),
    0x801B5978: table.sym_var("str_face_object_801B5978", "const char", "[]"),
    0x801B5984: table.sym_var("str_face_object_801B5984", "const char", "[]"),
    0x801B598C: table.sym_var("str_face_object_801B598C", "const char", "[]"),
    0x801B5994: table.sym_var("str_face_object_801B5994", "const char", "[]"),
    0x801B599C: table.sym_var("str_face_object_801B599C", "const char", "[]"),
    0x801B59A4: table.sym_var("str_face_object_801B59A4", "const char", "[]"),
    0x801B59AC: table.sym_var("str_face_object_801B59AC", "const char", "[]"),
    0x801B59B8: table.sym_var("str_face_object_801B59B8", "const char", "[]"),
    0x801B59C0: table.sym_var("str_face_object_801B59C0", "const char", "[]"),
    0x801B59C8: table.sym_var("str_face_object_801B59C8", "const char", "[]"),
    0x801B59D0: table.sym_var("str_face_object_801B59D0", "const char", "[]"),
    0x801B59DC: table.sym_var("str_face_object_801B59DC", "const char", "[]"),
    0x801B59FC: table.sym_var("str_face_object_801B59FC", "const char", "[]"),
    0x801B5A20: table.sym_var("str_face_object_801B5A20", "const char", "[]"),
    0x801B5A28: table.sym_var("str_face_object_801B5A28", "const char", "[]"),
    0x801B5A44: table.sym_var("str_face_object_801B5A44", "const char", "[]"),
    0x801B5A4C: table.sym_var("str_face_object_801B5A4C", "const char", "[]"),
    0x801B5A68: table.sym_var("str_face_object_801B5A68", "const char", "[]"),
    0x801B5A70: table.sym_var("str_face_object_801B5A70", "const char", "[]"),
    0x801B5A7C: table.sym_var("str_face_object_801B5A7C", "const char", "[]"),
    0x801B5A84: table.sym_var("str_face_object_801B5A84", "const char", "[]"),
    0x801B5A8C: table.sym_var("str_face_object_801B5A8C", "const char", "[]"),
    0x801B5A94: table.sym_var("str_face_object_801B5A94", "const char", "[]"),
    0x801B5A9C: table.sym_var("str_face_object_801B5A9C", "const char", "[]"),
    0x801B5AA4: table.sym_var("str_face_object_801B5AA4", "const char", "[]"),
    0x801B5AAC: table.sym_var("str_face_object_801B5AAC", "const char", "[]"),
    0x801B5AB8: table.sym_var("str_face_object_801B5AB8", "const char", "[]"),
    0x801B5AC0: table.sym_var("str_face_object_801B5AC0", "const char", "[]"),
    0x801B5ACC: table.sym_var("str_face_object_801B5ACC", "const char", "[]"),
    0x801B5AD4: table.sym_var("str_face_object_801B5AD4", "const char", "[]"),
    0x801B5ADC: table.sym_var("str_face_object_801B5ADC", "const char", "[]"),
    0x801B5AF0: table.sym_var("str_face_object_801B5AF0", "const char", "[]"),
    0x801B5B0C: table.sym_var("str_face_object_801B5B0C", "const char", "[]"),
    0x801B5B24: table.sym_var("str_face_object_801B5B24", "const char", "[]"),
    0x801B5B28: table.sym_var("str_face_object_801B5B28", "const char", "[]"),
    0x801B5B2C: table.sym_var("str_face_object_801B5B2C", "const char", "[]"),
    0x801B5B38: table.sym_var("str_face_object_801B5B38", "const char", "[]"),
    0x801B5B40: table.sym_var("str_face_object_801B5B40", "const char", "[]"),
    0x801B5B44: table.sym_var("str_face_object_801B5B44", "const char", "[]"),
    0x801B5B4C: table.sym_var("str_face_object_801B5B4C", "const char", "[]"),
    0x801B5B50: table.sym_var("str_face_object_801B5B50", "const char", "[]"),
    0x801B5B54: table.sym_var("str_face_object_801B5B54", "const char", "[]"),
    0x801B5B68: table.sym_var("str_face_object_801B5B68", "const char", "[]"),
    0x801B5B7C: table.sym_var("str_face_object_801B5B7C", "const char", "[]"),
    0x801B5B84: table.sym_var("str_face_object_801B5B84", "const char", "[]"),
    0x801B5B8C: table.sym_var("str_face_object_801B5B8C", "const char", "[]"),
    0x801B5B94: table.sym_var("str_face_object_801B5B94", "const char", "[]"),
    0x801B5BA0: table.sym_var("str_face_object_801B5BA0", "const char", "[]"),
    0x801B5BB0: table.sym_var("str_face_object_801B5BB0", "const char", "[]"),
    0x801B5BBC: table.sym_var("str_face_object_801B5BBC", "const char", "[]"),
    0x801B5BC4: table.sym_var("str_face_object_801B5BC4", "const char", "[]"),
    0x801B5BCC: table.sym_var("str_face_object_801B5BCC", "const char", "[]"),
    0x801B5BD4: table.sym_var("str_face_object_801B5BD4", "const char", "[]"),
    0x801B5BE0: table.sym_var("str_face_object_801B5BE0", "const char", "[]"),
    0x801B5BEC: table.sym_var("str_face_object_801B5BEC", "const char", "[]"),
    0x801B5BF4: table.sym_var("str_face_object_801B5BF4", "const char", "[]"),
    0x801B5C00: table.sym_var("str_face_object_801B5C00", "const char", "[]"),
    0x801B5C08: table.sym_var("str_face_object_801B5C08", "const char", "[]"),
    0x801B5C10: table.sym_var("str_face_object_801B5C10", "const char", "[]"),
    0x801B5C18: table.sym_var("str_face_object_801B5C18", "const char", "[]"),
    0x801B5C1C: table.sym_var("str_face_object_801B5C1C", "const char", "[]"),
    0x801B5C20: table.sym_var("str_face_object_801B5C20", "const char", "[]"),
    0x801B5C2C: table.sym_var("str_face_object_801B5C2C", "const char", "[]"),
    0x801B5C30: table.sym_var("str_face_object_801B5C30", "const char", "[]"),
    0x801B5C34: table.sym_var("str_face_object_801B5C34", "const char", "[]"),
    0x801B5C40: table.sym_var("str_face_object_801B5C40", "const char", "[]"),
    0x801B5C44: table.sym_var("str_face_object_801B5C44", "const char", "[]"),
    0x801B5C48: table.sym_var("str_face_object_801B5C48", "const char", "[]"),
    0x801B5C64: table.sym_var("str_face_object_801B5C64", "const char", "[]"),
    0x801B5C90: table.sym_var("str_face_object_801B5C90", "const char", "[]"),
    0x801B5CA0: table.sym_var("str_face_object_801B5CA0", "const char", "[]"),
    0x801B5CB0: table.sym_var("str_face_object_801B5CB0", "const char", "[]"),
    0x801B5CBC: table.sym_var("face_object_801B5CBC", "const float"),
    0x801B5CC0: table.sym_var("face_object_801B5CC0", "const float"),
    0x801B5CC4: table.sym_var("face_object_801B5CC4", "const float"),
    0x801B5CC8: table.sym_var("face_object_801B5CC8", "const float"),
    0x801B5CCC: table.sym_var("face_object_801B5CCC", "const float"),
    0x801B5CD0: table.sym_var("face_object_801B5CD0", "const float"),
    0x801B5CD4: table.sym_var_fnc("face_object_801B5CD4", "const", "[]"),
    0x801B5D54: table.sym_var_fnc("face_object_801B5D54", "const", "[]"),
    0x801B5DD4: table.sym_var("face_object_801B5DD4", "const float"),
    0x801B5DD8: table.sym_var("face_object_801B5DD8", "const float"),
    0x801B5DE0: table.sym_var("face_object_801B5DE0", "const double"),
    0x801B5DE8: table.sym_var("face_object_801B5DE8", "const float"),
    0x801B5DEC: table.sym_var_fnc("face_object_801B5DEC", "const", "[]"),
    0x801B5E70: table.sym_var("face_object_801B5E70", "const double"),
    0x801B5E78: table.sym_var("face_object_801B5E78", "const double"),
    0x801B5E80: table.sym_var("face_object_801B5E80", "const double"),
    0x801B5E88: table.sym_var("face_object_801B5E88", "const double"),
    0x801B5E90: table.sym_var("face_object_801B5E90", "const double"),
    0x801B5E98: table.sym_var("face_object_801B5E98", "const float"),
    0x801B5E9C: table.sym_var_fnc("face_object_801B5E9C", "const", "[]"),
    0x801B5EC8: table.sym_var("face_object_801B5EC8", "const double"),
    0x801B5ED0: table.sym_var("face_object_801B5ED0", "const double"),

    # src/face/skin.c
    0x801B5EE0: table.sym_var("str_face_skin_801B5EE0", "const char", "[]"),
    0x801B5F0C: table.sym_var("str_face_skin_801B5F0C", "const char", "[]"),

    # src/face/particle.c
    0x801B5F40: table.sym_var("str_face_particle_801B5F40", "const char", "[]"),
    0x801B5F64: table.sym_var("str_face_particle_801B5F64", "const char", "[]"),
    0x801B5F70: table.sym_var("str_face_particle_801B5F70", "const char", "[]"),
    0x801B5F7C: table.sym_var("str_face_particle_801B5F7C", "const char", "[]"),
    0x801B5F84: table.sym_var("str_face_particle_801B5F84", "const char", "[]"),
    0x801B5F8C: table.sym_var("str_face_particle_801B5F8C", "const char", "[]"),
    0x801B5F90: table.sym_var("face_particle_801B5F90", "const double"),
    0x801B5F98: table.sym_var("face_particle_801B5F98", "const double"),
    0x801B5FA0: table.sym_var("face_particle_801B5FA0", "const double"),
    0x801B5FA8: table.sym_var("face_particle_801B5FA8", "const double"),
    0x801B5FB0: table.sym_var("face_particle_801B5FB0", "const float"),
    0x801B5FB8: table.sym_var("face_particle_801B5FB8", "const double"),
    0x801B5FC0: table.sym_var("face_particle_801B5FC0", "const double"),
    0x801B5FC8: table.sym_var("face_particle_801B5FC8", "const double"),
    0x801B5FD0: table.sym_var("face_particle_801B5FD0", "const double"),

    # src/face/dynlist.c
    0x801B5FE0: table.sym_var("str_face_dynlist_801B5FE0", "const char", "[]"),
    0x801B5FE8: table.sym_var("str_face_dynlist_801B5FE8", "const char", "[]"),
    0x801B600C: table.sym_var("str_face_dynlist_801B600C", "const char", "[]"),
    0x801B602C: table.sym_var("str_face_dynlist_801B602C", "const char", "[]"),
    0x801B6034: table.sym_var("str_face_dynlist_801B6034", "const char", "[]"),
    0x801B603C: table.sym_var("str_face_dynlist_801B603C", "const char", "[]"),
    0x801B6040: table.sym_var("str_face_dynlist_801B6040", "const char", "[]"),
    0x801B6044: table.sym_var("str_face_dynlist_801B6044", "const char", "[]"),
    0x801B6070: table.sym_var("str_face_dynlist_801B6070", "const char", "[]"),
    0x801B608C: table.sym_var("str_face_dynlist_801B608C", "const char", "[]"),
    0x801B6094: table.sym_var("str_face_dynlist_801B6094", "const char", "[]"),
    0x801B60C0: table.sym_var("str_face_dynlist_801B60C0", "const char", "[]"),
    0x801B60C8: table.sym_var("str_face_dynlist_801B60C8", "const char", "[]"),
    0x801B60CC: table.sym_var("str_face_dynlist_801B60CC", "const char", "[]"),
    0x801B60D0: table.sym_var("str_face_dynlist_801B60D0", "const char", "[]"),
    0x801B6108: table.sym_var("str_face_dynlist_801B6108", "const char", "[]"),
    0x801B6128: table.sym_var("str_face_dynlist_801B6128", "const char", "[]"),
    0x801B6150: table.sym_var("str_face_dynlist_801B6150", "const char", "[]"),
    0x801B6154: table.sym_var("str_face_dynlist_801B6154", "const char", "[]"),
    0x801B617C: table.sym_var("str_face_dynlist_801B617C", "const char", "[]"),
    0x801B619C: table.sym_var("str_face_dynlist_801B619C", "const char", "[]"),
    0x801B61C0: table.sym_var("str_face_dynlist_801B61C0", "const char", "[]"),
    0x801B61E0: table.sym_var("str_face_dynlist_801B61E0", "const char", "[]"),
    0x801B6214: table.sym_var("str_face_dynlist_801B6214", "const char", "[]"),
    0x801B6220: table.sym_var("str_face_dynlist_801B6220", "const char", "[]"),
    0x801B6244: table.sym_var("str_face_dynlist_801B6244", "const char", "[]"),
    0x801B6278: table.sym_var("str_face_dynlist_801B6278", "const char", "[]"),
    0x801B6284: table.sym_var("str_face_dynlist_801B6284", "const char", "[]"),
    0x801B62B8: table.sym_var("str_face_dynlist_801B62B8", "const char", "[]"),
    0x801B62C4: table.sym_var("str_face_dynlist_801B62C4", "const char", "[]"),
    0x801B62E8: table.sym_var("str_face_dynlist_801B62E8", "const char", "[]"),
    0x801B630C: table.sym_var("str_face_dynlist_801B630C", "const char", "[]"),
    0x801B6318: table.sym_var("str_face_dynlist_801B6318", "const char", "[]"),
    0x801B6328: table.sym_var("str_face_dynlist_801B6328", "const char", "[]"),
    0x801B633C: table.sym_var("str_face_dynlist_801B633C", "const char", "[]"),
    0x801B635C: table.sym_var("str_face_dynlist_801B635C", "const char", "[]"),
    0x801B6380: table.sym_var("str_face_dynlist_801B6380", "const char", "[]"),
    0x801B63A0: table.sym_var("str_face_dynlist_801B63A0", "const char", "[]"),
    0x801B63AC: table.sym_var("str_face_dynlist_801B63AC", "const char", "[]"),
    0x801B63BC: table.sym_var("str_face_dynlist_801B63BC", "const char", "[]"),
    0x801B63CC: table.sym_var("str_face_dynlist_801B63CC", "const char", "[]"),
    0x801B63E4: table.sym_var("str_face_dynlist_801B63E4", "const char", "[]"),
    0x801B63FC: table.sym_var("str_face_dynlist_801B63FC", "const char", "[]"),
    0x801B641C: table.sym_var("str_face_dynlist_801B641C", "const char", "[]"),
    0x801B6450: table.sym_var("str_face_dynlist_801B6450", "const char", "[]"),
    0x801B6460: table.sym_var("str_face_dynlist_801B6460", "const char", "[]"),
    0x801B6484: table.sym_var("str_face_dynlist_801B6484", "const char", "[]"),
    0x801B64AC: table.sym_var("str_face_dynlist_801B64AC", "const char", "[]"),
    0x801B64E0: table.sym_var("str_face_dynlist_801B64E0", "const char", "[]"),
    0x801B64F0: table.sym_var("str_face_dynlist_801B64F0", "const char", "[]"),
    0x801B6514: table.sym_var("str_face_dynlist_801B6514", "const char", "[]"),
    0x801B6538: table.sym_var("str_face_dynlist_801B6538", "const char", "[]"),
    0x801B656C: table.sym_var("str_face_dynlist_801B656C", "const char", "[]"),
    0x801B657C: table.sym_var("str_face_dynlist_801B657C", "const char", "[]"),
    0x801B65A0: table.sym_var("str_face_dynlist_801B65A0", "const char", "[]"),
    0x801B65D4: table.sym_var("str_face_dynlist_801B65D4", "const char", "[]"),
    0x801B65E4: table.sym_var("str_face_dynlist_801B65E4", "const char", "[]"),
    0x801B6608: table.sym_var("str_face_dynlist_801B6608", "const char", "[]"),
    0x801B663C: table.sym_var("str_face_dynlist_801B663C", "const char", "[]"),
    0x801B664C: table.sym_var("str_face_dynlist_801B664C", "const char", "[]"),
    0x801B6670: table.sym_var("str_face_dynlist_801B6670", "const char", "[]"),
    0x801B6698: table.sym_var("str_face_dynlist_801B6698", "const char", "[]"),
    0x801B66CC: table.sym_var("str_face_dynlist_801B66CC", "const char", "[]"),
    0x801B66DC: table.sym_var("str_face_dynlist_801B66DC", "const char", "[]"),
    0x801B6700: table.sym_var("str_face_dynlist_801B6700", "const char", "[]"),
    0x801B6728: table.sym_var("str_face_dynlist_801B6728", "const char", "[]"),
    0x801B674C: table.sym_var("str_face_dynlist_801B674C", "const char", "[]"),
    0x801B6770: table.sym_var("str_face_dynlist_801B6770", "const char", "[]"),
    0x801B6794: table.sym_var("str_face_dynlist_801B6794", "const char", "[]"),
    0x801B67BC: table.sym_var("str_face_dynlist_801B67BC", "const char", "[]"),
    0x801B67F0: table.sym_var("str_face_dynlist_801B67F0", "const char", "[]"),
    0x801B6804: table.sym_var("str_face_dynlist_801B6804", "const char", "[]"),
    0x801B6828: table.sym_var("str_face_dynlist_801B6828", "const char", "[]"),
    0x801B685C: table.sym_var("str_face_dynlist_801B685C", "const char", "[]"),
    0x801B6870: table.sym_var("str_face_dynlist_801B6870", "const char", "[]"),
    0x801B6898: table.sym_var("str_face_dynlist_801B6898", "const char", "[]"),
    0x801B68CC: table.sym_var("str_face_dynlist_801B68CC", "const char", "[]"),
    0x801B68DC: table.sym_var("str_face_dynlist_801B68DC", "const char", "[]"),
    0x801B68FC: table.sym_var("str_face_dynlist_801B68FC", "const char", "[]"),
    0x801B6920: table.sym_var("str_face_dynlist_801B6920", "const char", "[]"),
    0x801B6944: table.sym_var("str_face_dynlist_801B6944", "const char", "[]"),
    0x801B6968: table.sym_var("str_face_dynlist_801B6968", "const char", "[]"),
    0x801B699C: table.sym_var("str_face_dynlist_801B699C", "const char", "[]"),
    0x801B69AC: table.sym_var("str_face_dynlist_801B69AC", "const char", "[]"),
    0x801B69D0: table.sym_var("str_face_dynlist_801B69D0", "const char", "[]"),
    0x801B6A04: table.sym_var("str_face_dynlist_801B6A04", "const char", "[]"),
    0x801B6A14: table.sym_var("str_face_dynlist_801B6A14", "const char", "[]"),
    0x801B6A38: table.sym_var("str_face_dynlist_801B6A38", "const char", "[]"),
    0x801B6A5C: table.sym_var("str_face_dynlist_801B6A5C", "const char", "[]"),
    0x801B6A90: table.sym_var("str_face_dynlist_801B6A90", "const char", "[]"),
    0x801B6AA0: table.sym_var("str_face_dynlist_801B6AA0", "const char", "[]"),
    0x801B6AC4: table.sym_var("str_face_dynlist_801B6AC4", "const char", "[]"),
    0x801B6AF8: table.sym_var("str_face_dynlist_801B6AF8", "const char", "[]"),
    0x801B6B08: table.sym_var("str_face_dynlist_801B6B08", "const char", "[]"),
    0x801B6B2C: table.sym_var("str_face_dynlist_801B6B2C", "const char", "[]"),
    0x801B6B60: table.sym_var("str_face_dynlist_801B6B60", "const char", "[]"),
    0x801B6B70: table.sym_var("str_face_dynlist_801B6B70", "const char", "[]"),
    0x801B6B94: table.sym_var("str_face_dynlist_801B6B94", "const char", "[]"),
    0x801B6BC8: table.sym_var("str_face_dynlist_801B6BC8", "const char", "[]"),
    0x801B6BD8: table.sym_var("str_face_dynlist_801B6BD8", "const char", "[]"),
    0x801B6BFC: table.sym_var("str_face_dynlist_801B6BFC", "const char", "[]"),
    0x801B6C30: table.sym_var("str_face_dynlist_801B6C30", "const char", "[]"),
    0x801B6C40: table.sym_var("str_face_dynlist_801B6C40", "const char", "[]"),
    0x801B6C64: table.sym_var("str_face_dynlist_801B6C64", "const char", "[]"),
    0x801B6C98: table.sym_var("str_face_dynlist_801B6C98", "const char", "[]"),
    0x801B6CA8: table.sym_var("str_face_dynlist_801B6CA8", "const char", "[]"),
    0x801B6CCC: table.sym_var("str_face_dynlist_801B6CCC", "const char", "[]"),
    0x801B6D00: table.sym_var("str_face_dynlist_801B6D00", "const char", "[]"),
    0x801B6D14: table.sym_var("str_face_dynlist_801B6D14", "const char", "[]"),
    0x801B6D38: table.sym_var("str_face_dynlist_801B6D38", "const char", "[]"),
    0x801B6D6C: table.sym_var("str_face_dynlist_801B6D6C", "const char", "[]"),
    0x801B6D7C: table.sym_var("str_face_dynlist_801B6D7C", "const char", "[]"),
    0x801B6DA0: table.sym_var("str_face_dynlist_801B6DA0", "const char", "[]"),
    0x801B6DD4: table.sym_var("str_face_dynlist_801B6DD4", "const char", "[]"),
    0x801B6DE0: table.sym_var("str_face_dynlist_801B6DE0", "const char", "[]"),
    0x801B6E04: table.sym_var("str_face_dynlist_801B6E04", "const char", "[]"),
    0x801B6E38: table.sym_var("str_face_dynlist_801B6E38", "const char", "[]"),
    0x801B6E48: table.sym_var("str_face_dynlist_801B6E48", "const char", "[]"),
    0x801B6E6C: table.sym_var("str_face_dynlist_801B6E6C", "const char", "[]"),
    0x801B6EA0: table.sym_var("str_face_dynlist_801B6EA0", "const char", "[]"),
    0x801B6EB4: table.sym_var("str_face_dynlist_801B6EB4", "const char", "[]"),
    0x801B6EEC: table.sym_var("str_face_dynlist_801B6EEC", "const char", "[]"),
    0x801B6F10: table.sym_var("str_face_dynlist_801B6F10", "const char", "[]"),
    0x801B6F44: table.sym_var("str_face_dynlist_801B6F44", "const char", "[]"),
    0x801B6F54: table.sym_var("str_face_dynlist_801B6F54", "const char", "[]"),
    0x801B6F78: table.sym_var("str_face_dynlist_801B6F78", "const char", "[]"),
    0x801B6FAC: table.sym_var("str_face_dynlist_801B6FAC", "const char", "[]"),
    0x801B6FBC: table.sym_var("str_face_dynlist_801B6FBC", "const char", "[]"),
    0x801B6FE0: table.sym_var("str_face_dynlist_801B6FE0", "const char", "[]"),
    0x801B7014: table.sym_var("str_face_dynlist_801B7014", "const char", "[]"),
    0x801B7024: table.sym_var("str_face_dynlist_801B7024", "const char", "[]"),
    0x801B7048: table.sym_var("str_face_dynlist_801B7048", "const char", "[]"),
    0x801B707C: table.sym_var("str_face_dynlist_801B707C", "const char", "[]"),
    0x801B708C: table.sym_var("str_face_dynlist_801B708C", "const char", "[]"),
    0x801B70B0: table.sym_var("str_face_dynlist_801B70B0", "const char", "[]"),
    0x801B70E4: table.sym_var("str_face_dynlist_801B70E4", "const char", "[]"),
    0x801B70F8: table.sym_var("str_face_dynlist_801B70F8", "const char", "[]"),
    0x801B711C: table.sym_var("str_face_dynlist_801B711C", "const char", "[]"),
    0x801B7150: table.sym_var("str_face_dynlist_801B7150", "const char", "[]"),
    0x801B7160: table.sym_var("str_face_dynlist_801B7160", "const char", "[]"),
    0x801B7184: table.sym_var("str_face_dynlist_801B7184", "const char", "[]"),
    0x801B71B8: table.sym_var("str_face_dynlist_801B71B8", "const char", "[]"),
    0x801B71C4: table.sym_var("str_face_dynlist_801B71C4", "const char", "[]"),
    0x801B71E8: table.sym_var("str_face_dynlist_801B71E8", "const char", "[]"),
    0x801B721C: table.sym_var("str_face_dynlist_801B721C", "const char", "[]"),
    0x801B722C: table.sym_var("str_face_dynlist_801B722C", "const char", "[]"),
    0x801B7250: table.sym_var("str_face_dynlist_801B7250", "const char", "[]"),
    0x801B7284: table.sym_var("str_face_dynlist_801B7284", "const char", "[]"),
    0x801B728C: table.sym_var("str_face_dynlist_801B728C", "const char", "[]"),
    0x801B72B0: table.sym_var("str_face_dynlist_801B72B0", "const char", "[]"),
    0x801B72E4: table.sym_var("str_face_dynlist_801B72E4", "const char", "[]"),
    0x801B72F4: table.sym_var("str_face_dynlist_801B72F4", "const char", "[]"),
    0x801B7318: table.sym_var("str_face_dynlist_801B7318", "const char", "[]"),
    0x801B733C: table.sym_var("str_face_dynlist_801B733C", "const char", "[]"),
    0x801B7370: table.sym_var("str_face_dynlist_801B7370", "const char", "[]"),
    0x801B7380: table.sym_var("str_face_dynlist_801B7380", "const char", "[]"),
    0x801B73A4: table.sym_var("str_face_dynlist_801B73A4", "const char", "[]"),
    0x801B73D8: table.sym_var("str_face_dynlist_801B73D8", "const char", "[]"),
    0x801B73E8: table.sym_var("str_face_dynlist_801B73E8", "const char", "[]"),
    0x801B740C: table.sym_var("str_face_dynlist_801B740C", "const char", "[]"),
    0x801B741C: table.sym_var("str_face_dynlist_801B741C", "const char", "[]"),
    0x801B742C: table.sym_var("str_face_dynlist_801B742C", "const char", "[]"),
    0x801B7460: table.sym_var("str_face_dynlist_801B7460", "const char", "[]"),
    0x801B7470: table.sym_var("str_face_dynlist_801B7470", "const char", "[]"),
    0x801B7494: table.sym_var("str_face_dynlist_801B7494", "const char", "[]"),
    0x801B74B8: table.sym_var("str_face_dynlist_801B74B8", "const char", "[]"),
    0x801B74DC: table.sym_var("str_face_dynlist_801B74DC", "const char", "[]"),
    0x801B7510: table.sym_var("str_face_dynlist_801B7510", "const char", "[]"),
    0x801B751C: table.sym_var("str_face_dynlist_801B751C", "const char", "[]"),
    0x801B7540: table.sym_var("str_face_dynlist_801B7540", "const char", "[]"),
    0x801B7574: table.sym_var("str_face_dynlist_801B7574", "const char", "[]"),
    0x801B7580: table.sym_var("str_face_dynlist_801B7580", "const char", "[]"),
    0x801B75A4: table.sym_var("str_face_dynlist_801B75A4", "const char", "[]"),
    0x801B75D8: table.sym_var("str_face_dynlist_801B75D8", "const char", "[]"),
    0x801B75F8: table.sym_var("str_face_dynlist_801B75F8", "const char", "[]"),
    0x801B762C: table.sym_var("str_face_dynlist_801B762C", "const char", "[]"),
    0x801B764C: table.sym_var("str_face_dynlist_801B764C", "const char", "[]"),
    0x801B7680: table.sym_var("str_face_dynlist_801B7680", "const char", "[]"),
    0x801B76A0: table.sym_var("str_face_dynlist_801B76A0", "const char", "[]"),
    0x801B76D4: table.sym_var("str_face_dynlist_801B76D4", "const char", "[]"),
    0x801B76E0: table.sym_var("str_face_dynlist_801B76E0", "const char", "[]"),
    0x801B7704: table.sym_var("str_face_dynlist_801B7704", "const char", "[]"),
    0x801B7710: table.sym_var("str_face_dynlist_801B7710", "const char", "[]"),
    0x801B771C: table.sym_var("str_face_dynlist_801B771C", "const char", "[]"),
    0x801B7738: table.sym_var("str_face_dynlist_801B7738", "const char", "[]"),
    0x801B7744: table.sym_var("str_face_dynlist_801B7744", "const char", "[]"),
    0x801B7778: table.sym_var("str_face_dynlist_801B7778", "const char", "[]"),
    0x801B7784: table.sym_var("str_face_dynlist_801B7784", "const char", "[]"),
    0x801B77A8: table.sym_var("str_face_dynlist_801B77A8", "const char", "[]"),
    0x801B77CC: table.sym_var("str_face_dynlist_801B77CC", "const char", "[]"),
    0x801B7800: table.sym_var("str_face_dynlist_801B7800", "const char", "[]"),
    0x801B780C: table.sym_var("str_face_dynlist_801B780C", "const char", "[]"),
    0x801B7830: table.sym_var("str_face_dynlist_801B7830", "const char", "[]"),
    0x801B7864: table.sym_var("str_face_dynlist_801B7864", "const char", "[]"),
    0x801B7870: table.sym_var("str_face_dynlist_801B7870", "const char", "[]"),
    0x801B7894: table.sym_var("str_face_dynlist_801B7894", "const char", "[]"),
    0x801B78B8: table.sym_var("str_face_dynlist_801B78B8", "const char", "[]"),
    0x801B78EC: table.sym_var("str_face_dynlist_801B78EC", "const char", "[]"),
    0x801B78FC: table.sym_var("str_face_dynlist_801B78FC", "const char", "[]"),
    0x801B7920: table.sym_var("str_face_dynlist_801B7920", "const char", "[]"),
    0x801B7954: table.sym_var("str_face_dynlist_801B7954", "const char", "[]"),
    0x801B7964: table.sym_var("str_face_dynlist_801B7964", "const char", "[]"),
    0x801B7988: table.sym_var("str_face_dynlist_801B7988", "const char", "[]"),
    0x801B79BC: table.sym_var("str_face_dynlist_801B79BC", "const char", "[]"),
    0x801B79C8: table.sym_var("str_face_dynlist_801B79C8", "const char", "[]"),
    0x801B79EC: table.sym_var("str_face_dynlist_801B79EC", "const char", "[]"),
    0x801B7A20: table.sym_var("str_face_dynlist_801B7A20", "const char", "[]"),
    0x801B7A30: table.sym_var("str_face_dynlist_801B7A30", "const char", "[]"),
    0x801B7A54: table.sym_var("str_face_dynlist_801B7A54", "const char", "[]"),
    0x801B7A88: table.sym_var("str_face_dynlist_801B7A88", "const char", "[]"),
    0x801B7A98: table.sym_var("str_face_dynlist_801B7A98", "const char", "[]"),
    0x801B7ABC: table.sym_var("str_face_dynlist_801B7ABC", "const char", "[]"),
    0x801B7AF0: table.sym_var("str_face_dynlist_801B7AF0", "const char", "[]"),
    0x801B7B00: table.sym_var("str_face_dynlist_801B7B00", "const char", "[]"),
    0x801B7B24: table.sym_var("str_face_dynlist_801B7B24", "const char", "[]"),
    0x801B7B58: table.sym_var("str_face_dynlist_801B7B58", "const char", "[]"),
    0x801B7B68: table.sym_var("str_face_dynlist_801B7B68", "const char", "[]"),
    0x801B7B8C: table.sym_var("str_face_dynlist_801B7B8C", "const char", "[]"),
    0x801B7BB0: table.sym_var("str_face_dynlist_801B7BB0", "const char", "[]"),
    0x801B7BE4: table.sym_var("str_face_dynlist_801B7BE4", "const char", "[]"),
    0x801B7BF4: table.sym_var("str_face_dynlist_801B7BF4", "const char", "[]"),
    0x801B7C18: table.sym_var("str_face_dynlist_801B7C18", "const char", "[]"),
    0x801B7C4C: table.sym_var("str_face_dynlist_801B7C4C", "const char", "[]"),
    0x801B7C5C: table.sym_var("str_face_dynlist_801B7C5C", "const char", "[]"),
    0x801B7C80: table.sym_var("str_face_dynlist_801B7C80", "const char", "[]"),
    0x801B7CB4: table.sym_var("str_face_dynlist_801B7CB4", "const char", "[]"),
    0x801B7CC4: table.sym_var("str_face_dynlist_801B7CC4", "const char", "[]"),
    0x801B7CE8: table.sym_var("str_face_dynlist_801B7CE8", "const char", "[]"),
    0x801B7D1C: table.sym_var("str_face_dynlist_801B7D1C", "const char", "[]"),
    0x801B7D30: table.sym_var("str_face_dynlist_801B7D30", "const char", "[]"),
    0x801B7D54: table.sym_var("str_face_dynlist_801B7D54", "const char", "[]"),
    0x801B7D88: table.sym_var("str_face_dynlist_801B7D88", "const char", "[]"),
    0x801B7D98: table.sym_var("str_face_dynlist_801B7D98", "const char", "[]"),
    0x801B7DBC: table.sym_var("str_face_dynlist_801B7DBC", "const char", "[]"),
    0x801B7DF0: table.sym_var("str_face_dynlist_801B7DF0", "const char", "[]"),
    0x801B7E00: table.sym_var("str_face_dynlist_801B7E00", "const char", "[]"),
    0x801B7E24: table.sym_var("str_face_dynlist_801B7E24", "const char", "[]"),
    0x801B7E58: table.sym_var("str_face_dynlist_801B7E58", "const char", "[]"),
    0x801B7E6C: table.sym_var("str_face_dynlist_801B7E6C", "const char", "[]"),
    0x801B7E90: table.sym_var("str_face_dynlist_801B7E90", "const char", "[]"),
    0x801B7EC4: table.sym_var("str_face_dynlist_801B7EC4", "const char", "[]"),
    0x801B7ED8: table.sym_var_fnc("face_dynlist_801B7ED8", "const", "[]"),
    0x801B7FB8: table.sym_var_fnc("face_dynlist_801B7FB8", "const", "[]"),
    0x801B8004: table.sym_var("face_dynlist_801B8004", "const float"),
    0x801B8008: table.sym_var_fnc("face_dynlist_801B8008", "const", "[]"),
    0x801B8034: table.sym_var_fnc("face_dynlist_801B8034", "const", "[]"),
    0x801B80B0: table.sym_var_fnc("face_dynlist_801B80B0", "const", "[]"),

    # src/face/gadget.c
    0x801B8130: table.sym_var("str_face_gadget_801B8130", "const char", "[]"),
    0x801B8148: table.sym_var("str_face_gadget_801B8148", "const char", "[]"),
    0x801B8158: table.sym_var("str_face_gadget_801B8158", "const char", "[]"),
    0x801B8164: table.sym_var("str_face_gadget_801B8164", "const char", "[]"),
    0x801B817C: table.sym_var("str_face_gadget_801B817C", "const char", "[]"),
    0x801B81C8: table.sym_var("str_face_gadget_801B81C8", "const char", "[]"),
    0x801B8240: table.sym_var("str_face_gadget_801B8240", "const char", "[]"),
    0x801B8258: table.sym_var("str_face_gadget_801B8258", "const char", "[]"),
    0x801B8268: table.sym_var("str_face_gadget_801B8268", "const char", "[]"),
    0x801B8280: table.sym_var("str_face_gadget_801B8280", "const char", "[]"),
    0x801B8290: table.sym_var("str_face_gadget_801B8290", "const char", "[]"),
    0x801B82B4: table.sym_var("str_face_gadget_801B82B4", "const char", "[]"),
    0x801B82CC: table.sym_var("str_face_gadget_801B82CC", "const char", "[]"),
    0x801B82E0: table.sym_var("face_gadget_801B82E0", "const double"),
    0x801B82E8: table.sym_var("face_gadget_801B82E8", "const double"),

    # src/face/stdio.c
    0x801B82F0: table.sym_var("str_face_stdio_801B82F0", "const char", "[]"),
    0x801B8310: table.sym_var("str_face_stdio_801B8310", "const char", "[]"),
    0x801B832C: table.sym_var("str_face_stdio_801B832C", "const char", "[]"),
    0x801B8330: table.sym_var("str_face_stdio_801B8330", "const char", "[]"),
    0x801B8348: table.sym_var("str_face_stdio_801B8348", "const char", "[]"),
    0x801B8364: table.sym_var("str_face_stdio_801B8364", "const char", "[]"),
    0x801B8370: table.sym_var("str_face_stdio_801B8370", "const char", "[]"),
    0x801B837C: table.sym_var("str_face_stdio_801B837C", "const char", "[]"),
    0x801B838C: table.sym_var("str_face_stdio_801B838C", "const char", "[]"),
    0x801B83A4: table.sym_var("str_face_stdio_801B83A4", "const char", "[]"),
    0x801B83DC: table.sym_var("str_face_stdio_801B83DC", "const char", "[]"),
    0x801B8408: table.sym_var("str_face_stdio_801B8408", "const char", "[]"),
    0x801B8434: table.sym_var("str_face_stdio_801B8434", "const char", "[]"),
    0x801B8440: table.sym_var("str_face_stdio_801B8440", "const char", "[]"),
    0x801B8444: table.sym_var("str_face_stdio_801B8444", "const char", "[]"),
    0x801B8448: table.sym_var("str_face_stdio_801B8448", "const char", "[]"),
    0x801B844C: table.sym_var("str_face_stdio_801B844C", "const char", "[]"),
    0x801B8450: table.sym_var("str_face_stdio_801B8450", "const char", "[]"),
    0x801B8454: table.sym_var("str_face_stdio_801B8454", "const char", "[]"),
    0x801B8458: table.sym_var("str_face_stdio_801B8458", "const char", "[]"),
    0x801B845C: table.sym_var("str_face_stdio_801B845C", "const char", "[]"),
    0x801B8460: table.sym_var("str_face_stdio_801B8460", "const char", "[]"),
    0x801B8464: table.sym_var("str_face_stdio_801B8464", "const char", "[]"),
    0x801B8468: table.sym_var("str_face_stdio_801B8468", "const char", "[]"),
    0x801B846C: table.sym_var("str_face_stdio_801B846C", "const char", "[]"),
    0x801B8488: table.sym_var("str_face_stdio_801B8488", "const char", "[]"),
    0x801B8490: table.sym_var("str_face_stdio_801B8490", "const char", "[]"),
    0x801B84B8: table.sym_var("str_face_stdio_801B84B8", "const char", "[]"),
    0x801B84D4: table.sym_var("str_face_stdio_801B84D4", "const char", "[]"),
    0x801B84E0: table.sym_var("str_face_stdio_801B84E0", "const char", "[]"),
    0x801B84FC: table.sym_var("str_face_stdio_801B84FC", "const char", "[]"),
    0x801B851C: table.sym_var("str_face_stdio_801B851C", "const char", "[]"),
    0x801B8544: table.sym_var("str_face_stdio_801B8544", "const char", "[]"),
    0x801B8548: table.sym_var("str_face_stdio_801B8548", "const char", "[]"),
    0x801B854C: table.sym_var_fnc("face_stdio_801B854C", "const", "[]"),
    0x801B85A8: table.sym_var("face_stdio_801B85A8", "const double"),

    # src/face/joint.c
    0x801B85B0: table.sym_var("str_face_joint_801B85B0", "const char", "[]"),
    0x801B85E0: table.sym_var("str_face_joint_801B85E0", "const char", "[]"),
    0x801B85F0: table.sym_var("str_face_joint_801B85F0", "const char", "[]"),
    0x801B85F4: table.sym_var("str_face_joint_801B85F4", "const char", "[]"),
    0x801B8608: table.sym_var("str_face_joint_801B8608", "const char", "[]"),
    0x801B860C: table.sym_var("str_face_joint_801B860C", "const char", "[]"),
    0x801B861C: table.sym_var("str_face_joint_801B861C", "const char", "[]"),
    0x801B863C: table.sym_var("str_face_joint_801B863C", "const char", "[]"),
    0x801B8658: table.sym_var("str_face_joint_801B8658", "const char", "[]"),
    0x801B8660: table.sym_var("str_face_joint_801B8660", "const char", "[]"),
    0x801B8668: table.sym_var("str_face_joint_801B8668", "const char", "[]"),
    0x801B866C: table.sym_var("str_face_joint_801B866C", "const char", "[]"),
    0x801B8670: table.sym_var("str_face_joint_801B8670", "const char", "[]"),
    0x801B8674: table.sym_var("str_face_joint_801B8674", "const char", "[]"),
    0x801B8694: table.sym_var("str_face_joint_801B8694", "const char", "[]"),
    0x801B86B8: table.sym_var("face_joint_801B86B8", "const double"),
    0x801B86C0: table.sym_var("face_joint_801B86C0", "const double"),
    0x801B86C8: table.sym_var("face_joint_801B86C8", "const double"),
    0x801B86D0: table.sym_var("face_joint_801B86D0", "const double"),
    0x801B86D8: table.sym_var("face_joint_801B86D8", "const double"),
    0x801B86E0: table.sym_var("face_joint_801B86E0", "const double"),
    0x801B86E8: table.sym_var("face_joint_801B86E8", "const float"),
    0x801B86EC: table.sym_var("face_joint_801B86EC", "const float"),
    0x801B86F0: table.sym_var("face_joint_801B86F0", "const double"),
    0x801B86F8: table.sym_var("face_joint_801B86F8", "const double"),
    0x801B8700: table.sym_var("face_joint_801B8700", "const double"),
    0x801B8708: table.sym_var("face_joint_801B8708", "const double"),
    0x801B8710: table.sym_var("face_joint_801B8710", "const double"),
    0x801B8718: table.sym_var("face_joint_801B8718", "const double"),
    0x801B8720: table.sym_var("face_joint_801B8720", "const double"),
    0x801B8728: table.sym_var("face_joint_801B8728", "const double"),

    # src/face/net.c
    0x801B8730: table.sym_var("str_face_net_801B8730", "const char", "[]"),
    0x801B8740: table.sym_var("str_face_net_801B8740", "const char", "[]"),
    0x801B874C: table.sym_var("str_face_net_801B874C", "const char", "[]"),
    0x801B8758: table.sym_var("str_face_net_801B8758", "const char", "[]"),
    0x801B8764: table.sym_var("str_face_net_801B8764", "const char", "[]"),
    0x801B8770: table.sym_var("str_face_net_801B8770", "const char", "[]"),
    0x801B8780: table.sym_var("str_face_net_801B8780", "const char", "[]"),
    0x801B878C: table.sym_var("str_face_net_801B878C", "const char", "[]"),
    0x801B8798: table.sym_var("str_face_net_801B8798", "const char", "[]"),
    0x801B87A4: table.sym_var("str_face_net_801B87A4", "const char", "[]"),
    0x801B87B0: table.sym_var("str_face_net_801B87B0", "const char", "[]"),
    0x801B87D8: table.sym_var("str_face_net_801B87D8", "const char", "[]"),
    0x801B87E4: table.sym_var("str_face_net_801B87E4", "const char", "[]"),
    0x801B87F0: table.sym_var("str_face_net_801B87F0", "const char", "[]"),
    0x801B87FC: table.sym_var("str_face_net_801B87FC", "const char", "[]"),
    0x801B8808: table.sym_var("str_face_net_801B8808", "const char", "[]"),
    0x801B8810: table.sym_var("str_face_net_801B8810", "const char", "[]"),
    0x801B8818: table.sym_var("str_face_net_801B8818", "const char", "[]"),
    0x801B8820: table.sym_var("str_face_net_801B8820", "const char", "[]"),
    0x801B8828: table.sym_var("str_face_net_801B8828", "const char", "[]"),
    0x801B8834: table.sym_var("str_face_net_801B8834", "const char", "[]"),
    0x801B8840: table.sym_var("str_face_net_801B8840", "const char", "[]"),
    0x801B8850: table.sym_var("str_face_net_801B8850", "const char", "[]"),
    0x801B8860: table.sym_var("str_face_net_801B8860", "const char", "[]"),
    0x801B8868: table.sym_var("str_face_net_801B8868", "const char", "[]"),
    0x801B8870: table.sym_var("str_face_net_801B8870", "const char", "[]"),
    0x801B887C: table.sym_var("str_face_net_801B887C", "const char", "[]"),
    0x801B888C: table.sym_var("str_face_net_801B888C", "const char", "[]"),
    0x801B889C: table.sym_var("str_face_net_801B889C", "const char", "[]"),
    0x801B88AC: table.sym_var("str_face_net_801B88AC", "const char", "[]"),
    0x801B88B4: table.sym_var("str_face_net_801B88B4", "const char", "[]"),
    0x801B88C8: table.sym_var("str_face_net_801B88C8", "const char", "[]"),
    0x801B88D8: table.sym_var("str_face_net_801B88D8", "const char", "[]"),
    0x801B88E0: table.sym_var("str_face_net_801B88E0", "const char", "[]"),
    0x801B88EC: table.sym_var("str_face_net_801B88EC", "const char", "[]"),
    0x801B88FC: table.sym_var("str_face_net_801B88FC", "const char", "[]"),
    0x801B890C: table.sym_var("str_face_net_801B890C", "const char", "[]"),
    0x801B891C: table.sym_var("str_face_net_801B891C", "const char", "[]"),
    0x801B8930: table.sym_var("face_net_801B8930", "const double"),
    0x801B8938: table.sym_var("face_net_801B8938", "const double"),
    0x801B8940: table.sym_var("face_net_801B8940", "const double"),
    0x801B8948: table.sym_var_fnc("face_net_801B8948", "const", "[]"),

    # src/face/math.c
    0x801B8970: table.sym_var("str_face_math_801B8970", "const char", "[]"),
    0x801B8990: table.sym_var("str_face_math_801B8990", "const char", "[]"),
    0x801B89B4: table.sym_var("str_face_math_801B89B4", "const char", "[]"),
    0x801B89C0: table.sym_var("str_face_math_801B89C0", "const char", "[]"),
    0x801B89C4: table.sym_var("str_face_math_801B89C4", "const char", "[]"),
    0x801B89E0: table.sym_var("str_face_math_801B89E0", "const char", "[]"),
    0x801B89FC: table.sym_var("str_face_math_801B89FC", "const char", "[]"),
    0x801B8A18: table.sym_var("str_face_math_801B8A18", "const char", "[]"),
    0x801B8A1C: table.sym_var("str_face_math_801B8A1C", "const char", "[]"),
    0x801B8A20: table.sym_var("str_face_math_801B8A20", "const char", "[]"),
    0x801B8A24: table.sym_var("str_face_math_801B8A24", "const char", "[]"),
    0x801B8A28: table.sym_var("str_face_math_801B8A28", "const char", "[]"),
    0x801B8A2C: table.sym_var("face_math_801B8A2C", "const float"),
    0x801B8A30: table.sym_var("face_math_801B8A30", "const float"),
    0x801B8A34: table.sym_var("face_math_801B8A34", "const float"),
    0x801B8A38: table.sym_var("face_math_801B8A38", "const float"),
    0x801B8A3C: table.sym_var("face_math_801B8A3C", "const float"),
    0x801B8A40: table.sym_var("face_math_801B8A40", "const double"),
    0x801B8A48: table.sym_var("face_math_801B8A48", "const double"),
    0x801B8A50: table.sym_var("face_math_801B8A50", "const double"),
    0x801B8A58: table.sym_var("face_math_801B8A58", "const double"),

    # src/face/shape.c
    0x801B8A60: table.sym_var("str_face_shape_801B8A60", "const char", "[]"),
    0x801B8A68: table.sym_var("str_face_shape_801B8A68", "const char", "[]"),
    0x801B8A70: table.sym_var("str_face_shape_801B8A70", "const char", "[]"),
    0x801B8A78: table.sym_var("str_face_shape_801B8A78", "const char", "[]"),
    0x801B8A80: table.sym_var("str_face_shape_801B8A80", "const char", "[]"),
    0x801B8A90: table.sym_var("str_face_shape_801B8A90", "const char", "[]"),
    0x801B8A9C: table.sym_var("str_face_shape_801B8A9C", "const char", "[]"),
    0x801B8AA4: table.sym_var("str_face_shape_801B8AA4", "const char", "[]"),
    0x801B8AB0: table.sym_var("str_face_shape_801B8AB0", "const char", "[]"),
    0x801B8ACC: table.sym_var("str_face_shape_801B8ACC", "const char", "[]"),
    0x801B8AD4: table.sym_var("str_face_shape_801B8AD4", "const char", "[]"),
    0x801B8AF0: table.sym_var("str_face_shape_801B8AF0", "const char", "[]"),
    0x801B8AF8: table.sym_var("str_face_shape_801B8AF8", "const char", "[]"),
    0x801B8AFC: table.sym_var("str_face_shape_801B8AFC", "const char", "[]"),
    0x801B8B0C: table.sym_var("str_face_shape_801B8B0C", "const char", "[]"),
    0x801B8B28: table.sym_var("str_face_shape_801B8B28", "const char", "[]"),
    0x801B8B48: table.sym_var("str_face_shape_801B8B48", "const char", "[]"),
    0x801B8B6C: table.sym_var("str_face_shape_801B8B6C", "const char", "[]"),
    0x801B8B8C: table.sym_var("str_face_shape_801B8B8C", "const char", "[]"),
    0x801B8BAC: table.sym_var("str_face_shape_801B8BAC", "const char", "[]"),
    0x801B8BCC: table.sym_var("str_face_shape_801B8BCC", "const char", "[]"),
    0x801B8BEC: table.sym_var("str_face_shape_801B8BEC", "const char", "[]"),
    0x801B8C0C: table.sym_var("str_face_shape_801B8C0C", "const char", "[]"),
    0x801B8C2C: table.sym_var("str_face_shape_801B8C2C", "const char", "[]"),
    0x801B8C4C: table.sym_var("str_face_shape_801B8C4C", "const char", "[]"),
    0x801B8C50: table.sym_var("str_face_shape_801B8C50", "const char", "[]"),
    0x801B8C68: table.sym_var("str_face_shape_801B8C68", "const char", "[]"),
    0x801B8C88: table.sym_var("str_face_shape_801B8C88", "const char", "[]"),
    0x801B8C98: table.sym_var("str_face_shape_801B8C98", "const char", "[]"),
    0x801B8CA0: table.sym_var("str_face_shape_801B8CA0", "const char", "[]"),
    0x801B8CA4: table.sym_var("str_face_shape_801B8CA4", "const char", "[]"),
    0x801B8CBC: table.sym_var("str_face_shape_801B8CBC", "const char", "[]"),
    0x801B8CC4: table.sym_var("str_face_shape_801B8CC4", "const char", "[]"),
    0x801B8CD8: table.sym_var("str_face_shape_801B8CD8", "const char", "[]"),
    0x801B8CE8: table.sym_var("str_face_shape_801B8CE8", "const char", "[]"),
    0x801B8CEC: table.sym_var("str_face_shape_801B8CEC", "const char", "[]"),
    0x801B8CF4: table.sym_var("str_face_shape_801B8CF4", "const char", "[]"),
    0x801B8D10: table.sym_var("str_face_shape_801B8D10", "const char", "[]"),
    0x801B8D34: table.sym_var("str_face_shape_801B8D34", "const char", "[]"),
    0x801B8D40: table.sym_var("str_face_shape_801B8D40", "const char", "[]"),
    0x801B8D44: table.sym_var("str_face_shape_801B8D44", "const char", "[]"),
    0x801B8D50: table.sym_var("str_face_shape_801B8D50", "const char", "[]"),
    0x801B8D58: table.sym_var("str_face_shape_801B8D58", "const char", "[]"),
    0x801B8D60: table.sym_var("str_face_shape_801B8D60", "const char", "[]"),
    0x801B8D68: table.sym_var("str_face_shape_801B8D68", "const char", "[]"),
    0x801B8D70: table.sym_var("str_face_shape_801B8D70", "const char", "[]"),
    0x801B8D78: table.sym_var("str_face_shape_801B8D78", "const char", "[]"),
    0x801B8D80: table.sym_var("str_face_shape_801B8D80", "const char", "[]"),
    0x801B8D88: table.sym_var("str_face_shape_801B8D88", "const char", "[]"),
    0x801B8D90: table.sym_var("str_face_shape_801B8D90", "const char", "[]"),
    0x801B8D98: table.sym_var("str_face_shape_801B8D98", "const char", "[]"),
    0x801B8DA0: table.sym_var("str_face_shape_801B8DA0", "const char", "[]"),
    0x801B8DA8: table.sym_var("str_face_shape_801B8DA8", "const char", "[]"),
    0x801B8DB0: table.sym_var("str_face_shape_801B8DB0", "const char", "[]"),
    0x801B8DB8: table.sym_var("str_face_shape_801B8DB8", "const char", "[]"),
    0x801B8DC0: table.sym_var("str_face_shape_801B8DC0", "const char", "[]"),
    0x801B8DC8: table.sym_var("str_face_shape_801B8DC8", "const char", "[]"),
    0x801B8DCC: table.sym_var("str_face_shape_801B8DCC", "const char", "[]"),
    0x801B8DD4: table.sym_var("str_face_shape_801B8DD4", "const char", "[]"),
    0x801B8DDC: table.sym_var("str_face_shape_801B8DDC", "const char", "[]"),
    0x801B8DEC: table.sym_var("str_face_shape_801B8DEC", "const char", "[]"),
    0x801B8DF4: table.sym_var_fnc("face_shape_801B8DF4", "const", "[]"),
    0x801B8E14: table.sym_var("face_shape_801B8E14", "const float"),
    0x801B8E18: table.sym_var("face_shape_801B8E18", "const float"),
    0x801B8E1C: table.sym_var("face_shape_801B8E1C", "const float"),
    0x801B8E20: table.sym_var("face_shape_801B8E20", "const float"),
    0x801B8E24: table.sym_var("face_shape_801B8E24", "const float"),

    # src/face/gfx.c
    0x801B8E30: table.sym_var("str_face_gfx_801B8E30", "const char", "[]"),
    0x801B8E34: table.sym_var("str_face_gfx_801B8E34", "const char", "[]"),
    0x801B8E64: table.sym_var("str_face_gfx_801B8E64", "const char", "[]"),
    0x801B8E78: table.sym_var("str_face_gfx_801B8E78", "const char", "[]"),
    0x801B8E8C: table.sym_var("str_face_gfx_801B8E8C", "const char", "[]"),
    0x801B8EA0: table.sym_var("str_face_gfx_801B8EA0", "const char", "[]"),
    0x801B8EB4: table.sym_var("str_face_gfx_801B8EB4", "const char", "[]"),
    0x801B8EC8: table.sym_var("str_face_gfx_801B8EC8", "const char", "[]"),
    0x801B8ED8: table.sym_var("str_face_gfx_801B8ED8", "const char", "[]"),
    0x801B8EE0: table.sym_var("str_face_gfx_801B8EE0", "const char", "[]"),
    0x801B8F14: table.sym_var("str_face_gfx_801B8F14", "const char", "[]"),
    0x801B8F44: table.sym_var("str_face_gfx_801B8F44", "const char", "[]"),
    0x801B8F4C: table.sym_var("str_face_gfx_801B8F4C", "const char", "[]"),
    0x801B8F7C: table.sym_var("str_face_gfx_801B8F7C", "const char", "[]"),
    0x801B8FA8: table.sym_var("str_face_gfx_801B8FA8", "const char", "[]"),
    0x801B8FB0: table.sym_var("str_face_gfx_801B8FB0", "const char", "[]"),
    0x801B8FBC: table.sym_var("str_face_gfx_801B8FBC", "const char", "[]"),
    0x801B8FC4: table.sym_var("str_face_gfx_801B8FC4", "const char", "[]"),
    0x801B8FCC: table.sym_var("str_face_gfx_801B8FCC", "const char", "[]"),
    0x801B8FDC: table.sym_var("str_face_gfx_801B8FDC", "const char", "[]"),
    0x801B8FEC: table.sym_var("str_face_gfx_801B8FEC", "const char", "[]"),
    0x801B8FF8: table.sym_var("str_face_gfx_801B8FF8", "const char", "[]"),
    0x801B9004: table.sym_var("str_face_gfx_801B9004", "const char", "[]"),
    0x801B900C: table.sym_var("str_face_gfx_801B900C", "const char", "[]"),
    0x801B9014: table.sym_var("str_face_gfx_801B9014", "const char", "[]"),
    0x801B9020: table.sym_var("str_face_gfx_801B9020", "const char", "[]"),
    0x801B902C: table.sym_var("str_face_gfx_801B902C", "const char", "[]"),
    0x801B9038: table.sym_var("str_face_gfx_801B9038", "const char", "[]"),
    0x801B9040: table.sym_var("str_face_gfx_801B9040", "const char", "[]"),
    0x801B904C: table.sym_var("str_face_gfx_801B904C", "const char", "[]"),
    0x801B9058: table.sym_var("str_face_gfx_801B9058", "const char", "[]"),
    0x801B9068: table.sym_var("str_face_gfx_801B9068", "const char", "[]"),
    0x801B9074: table.sym_var("str_face_gfx_801B9074", "const char", "[]"),
    0x801B9084: table.sym_var("str_face_gfx_801B9084", "const char", "[]"),
    0x801B9090: table.sym_var("str_face_gfx_801B9090", "const char", "[]"),
    0x801B909C: table.sym_var("str_face_gfx_801B909C", "const char", "[]"),
    0x801B90A4: table.sym_var("str_face_gfx_801B90A4", "const char", "[]"),
    0x801B90B0: table.sym_var("str_face_gfx_801B90B0", "const char", "[]"),
    0x801B90BC: table.sym_var("str_face_gfx_801B90BC", "const char", "[]"),
    0x801B90C8: table.sym_var("str_face_gfx_801B90C8", "const char", "[]"),
    0x801B90D4: table.sym_var("str_face_gfx_801B90D4", "const char", "[]"),
    0x801B90E0: table.sym_var("str_face_gfx_801B90E0", "const char", "[]"),
    0x801B90EC: table.sym_var("str_face_gfx_801B90EC", "const char", "[]"),
    0x801B90F4: table.sym_var("str_face_gfx_801B90F4", "const char", "[]"),
    0x801B90FC: table.sym_var("str_face_gfx_801B90FC", "const char", "[]"),
    0x801B9108: table.sym_var("str_face_gfx_801B9108", "const char", "[]"),
    0x801B9114: table.sym_var("str_face_gfx_801B9114", "const char", "[]"),
    0x801B9120: table.sym_var("str_face_gfx_801B9120", "const char", "[]"),
    0x801B912C: table.sym_var("str_face_gfx_801B912C", "const char", "[]"),
    0x801B9134: table.sym_var("str_face_gfx_801B9134", "const char", "[]"),
    0x801B9144: table.sym_var("str_face_gfx_801B9144", "const char", "[]"),
    0x801B914C: table.sym_var("str_face_gfx_801B914C", "const char", "[]"),
    0x801B915C: table.sym_var("str_face_gfx_801B915C", "const char", "[]"),
    0x801B9168: table.sym_var("str_face_gfx_801B9168", "const char", "[]"),
    0x801B9170: table.sym_var("str_face_gfx_801B9170", "const char", "[]"),
    0x801B9178: table.sym_var("str_face_gfx_801B9178", "const char", "[]"),
    0x801B9184: table.sym_var("str_face_gfx_801B9184", "const char", "[]"),
    0x801B91A4: table.sym_var("str_face_gfx_801B91A4", "const char", "[]"),
    0x801B91A8: table.sym_var("str_face_gfx_801B91A8", "const char", "[]"),
    0x801B91B0: table.sym_var("str_face_gfx_801B91B0", "const char", "[]"),
    0x801B91D8: table.sym_var("str_face_gfx_801B91D8", "const char", "[]"),
    0x801B91E4: table.sym_var("str_face_gfx_801B91E4", "const char", "[]"),
    0x801B920C: table.sym_var("str_face_gfx_801B920C", "const char", "[]"),
    0x801B9218: table.sym_var("str_face_gfx_801B9218", "const char", "[]"),
    0x801B9240: table.sym_var("str_face_gfx_801B9240", "const char", "[]"),
    0x801B924C: table.sym_var("str_face_gfx_801B924C", "const char", "[]"),
    0x801B9258: table.sym_var("str_face_gfx_801B9258", "const char", "[]"),
    0x801B9270: table.sym_var("str_face_gfx_801B9270", "const char", "[]"),
    0x801B9294: table.sym_var("str_face_gfx_801B9294", "const char", "[]"),
    0x801B92A4: table.sym_var("str_face_gfx_801B92A4", "const char", "[]"),
    0x801B92AC: table.sym_var("str_face_gfx_801B92AC", "const char", "[]"),
    0x801B92B8: table.sym_var("str_face_gfx_801B92B8", "const char", "[]"),
    0x801B92D8: table.sym_var("str_face_gfx_801B92D8", "const char", "[]"),
    0x801B92E8: table.sym_var("str_face_gfx_801B92E8", "const char", "[]"),
    0x801B9320: table.sym_var("str_face_gfx_801B9320", "const char", "[]"),
    0x801B9350: table.sym_var("str_face_gfx_801B9350", "const char", "[]"),
    0x801B9378: table.sym_var("str_face_gfx_801B9378", "const char", "[]"),
    0x801B9390: table.sym_var("str_face_gfx_801B9390", "const char", "[]"),
    0x801B93A4: table.sym_var("str_face_gfx_801B93A4", "const char", "[]"),
    0x801B93B8: table.sym_var("str_face_gfx_801B93B8", "const char", "[]"),
    0x801B93DC: table.sym_var("str_face_gfx_801B93DC", "const char", "[]"),
    0x801B9400: table.sym_var("str_face_gfx_801B9400", "const char", "[]"),
    0x801B9414: table.sym_var("str_face_gfx_801B9414", "const char", "[]"),
    0x801B9428: table.sym_var("str_face_gfx_801B9428", "const char", "[]"),
    0x801B944C: table.sym_var("str_face_gfx_801B944C", "const char", "[]"),
    0x801B9454: table.sym_var("str_face_gfx_801B9454", "const char", "[]"),
    0x801B9478: table.sym_var("str_face_gfx_801B9478", "const char", "[]"),
    0x801B9480: table.sym_var("str_face_gfx_801B9480", "const char", "[]"),
    0x801B94A0: table.sym_var("str_face_gfx_801B94A0", "const char", "[]"),
    0x801B94BC: table.sym_var("str_face_gfx_801B94BC", "const char", "[]"),
    0x801B94D8: table.sym_var("str_face_gfx_801B94D8", "const char", "[]"),
    0x801B94F8: table.sym_var("str_face_gfx_801B94F8", "const char", "[]"),
    0x801B94FC: table.sym_var("str_face_gfx_801B94FC", "const char", "[]"),
    0x801B9510: table.sym_var("str_face_gfx_801B9510", "const char", "[]"),
    0x801B9534: table.sym_var("str_face_gfx_801B9534", "const char", "[]"),
    0x801B9554: table.sym_var("str_face_gfx_801B9554", "const char", "[]"),
    0x801B957C: table.sym_var("str_face_gfx_801B957C", "const char", "[]"),
    0x801B9584: table.sym_var("str_face_gfx_801B9584", "const char", "[]"),
    0x801B9588: table.sym_var("str_face_gfx_801B9588", "const char", "[]"),
    0x801B9594: table.sym_var("str_face_gfx_801B9594", "const char", "[]"),
    0x801B959C: table.sym_var("str_face_gfx_801B959C", "const char", "[]"),
    0x801B95A0: table.sym_var("str_face_gfx_801B95A0", "const char", "[]"),
    0x801B95A8: table.sym_var("str_face_gfx_801B95A8", "const char", "[]"),
    0x801B95B0: table.sym_var("str_face_gfx_801B95B0", "const char", "[]"),
    0x801B95B8: table.sym_var("str_face_gfx_801B95B8", "const char", "[]"),
    0x801B95C0: table.sym_var("str_face_gfx_801B95C0", "const char", "[]"),
    0x801B95C4: table.sym_var("str_face_gfx_801B95C4", "const char", "[]"),
    0x801B95C8: table.sym_var("str_face_gfx_801B95C8", "const char", "[]"),
    0x801B95D0: table.sym_var("str_face_gfx_801B95D0", "const char", "[]"),
    0x801B95D8: table.sym_var("str_face_gfx_801B95D8", "const char", "[]"),
    0x801B95DC: table.sym_var("str_face_gfx_801B95DC", "const char", "[]"),
    0x801B95E4: table.sym_var("str_face_gfx_801B95E4", "const char", "[]"),
    0x801B95EC: table.sym_var("str_face_gfx_801B95EC", "const char", "[]"),
    0x801B95F8: table.sym_var("str_face_gfx_801B95F8", "const char", "[]"),
    0x801B9604: table.sym_var("str_face_gfx_801B9604", "const char", "[]"),
    0x801B9610: table.sym_var("str_face_gfx_801B9610", "const char", "[]"),
    0x801B961C: table.sym_var("str_face_gfx_801B961C", "const char", "[]"),
    0x801B9628: table.sym_var("str_face_gfx_801B9628", "const char", "[]"),
    0x801B9630: table.sym_var("str_face_gfx_801B9630", "const char", "[]"),
    0x801B963C: table.sym_var("str_face_gfx_801B963C", "const char", "[]"),
    0x801B9644: table.sym_var("str_face_gfx_801B9644", "const char", "[]"),
    0x801B964C: table.sym_var("str_face_gfx_801B964C", "const char", "[]"),
    0x801B9658: table.sym_var("str_face_gfx_801B9658", "const char", "[]"),
    0x801B9660: table.sym_var("str_face_gfx_801B9660", "const char", "[]"),
    0x801B966C: table.sym_var("str_face_gfx_801B966C", "const char", "[]"),
    0x801B9674: table.sym_var("str_face_gfx_801B9674", "const char", "[]"),
    0x801B967C: table.sym_var("str_face_gfx_801B967C", "const char", "[]"),
    0x801B9684: table.sym_var("str_face_gfx_801B9684", "const char", "[]"),
    0x801B968C: table.sym_var("str_face_gfx_801B968C", "const char", "[]"),
    0x801B9694: table.sym_var("str_face_gfx_801B9694", "const char", "[]"),
    0x801B969C: table.sym_var("str_face_gfx_801B969C", "const char", "[]"),
    0x801B96A4: table.sym_var("str_face_gfx_801B96A4", "const char", "[]"),
    0x801B96AC: table.sym_var("str_face_gfx_801B96AC", "const char", "[]"),
    0x801B96B4: table.sym_var("str_face_gfx_801B96B4", "const char", "[]"),
    0x801B96BC: table.sym_var("str_face_gfx_801B96BC", "const char", "[]"),
    0x801B96C4: table.sym_var("str_face_gfx_801B96C4", "const char", "[]"),
    0x801B96CC: table.sym_var("str_face_gfx_801B96CC", "const char", "[]"),
    0x801B96D4: table.sym_var("str_face_gfx_801B96D4", "const char", "[]"),
    0x801B96E0: table.sym_var("str_face_gfx_801B96E0", "const char", "[]"),
    0x801B96E8: table.sym_var("str_face_gfx_801B96E8", "const char", "[]"),
    0x801B96F0: table.sym_var("str_face_gfx_801B96F0", "const char", "[]"),
    0x801B96F8: table.sym_var("str_face_gfx_801B96F8", "const char", "[]"),
    0x801B9700: table.sym_var("str_face_gfx_801B9700", "const char", "[]"),
    0x801B970C: table.sym_var("str_face_gfx_801B970C", "const char", "[]"),
    0x801B9714: table.sym_var("str_face_gfx_801B9714", "const char", "[]"),
    0x801B971C: table.sym_var("str_face_gfx_801B971C", "const char", "[]"),
    0x801B9724: table.sym_var("str_face_gfx_801B9724", "const char", "[]"),
    0x801B972C: table.sym_var("str_face_gfx_801B972C", "const char", "[]"),
    0x801B9734: table.sym_var("str_face_gfx_801B9734", "const char", "[]"),
    0x801B973C: table.sym_var("str_face_gfx_801B973C", "const char", "[]"),
    0x801B9744: table.sym_var("str_face_gfx_801B9744", "const char", "[]"),
    0x801B974C: table.sym_var("str_face_gfx_801B974C", "const char", "[]"),
    0x801B9754: table.sym_var("str_face_gfx_801B9754", "const char", "[]"),
    0x801B975C: table.sym_var("str_face_gfx_801B975C", "const char", "[]"),
    0x801B9764: table.sym_var("str_face_gfx_801B9764", "const char", "[]"),
    0x801B976C: table.sym_var("str_face_gfx_801B976C", "const char", "[]"),
    0x801B9774: table.sym_var("str_face_gfx_801B9774", "const char", "[]"),
    0x801B977C: table.sym_var("str_face_gfx_801B977C", "const char", "[]"),
    0x801B9784: table.sym_var("str_face_gfx_801B9784", "const char", "[]"),
    0x801B978C: table.sym_var("str_face_gfx_801B978C", "const char", "[]"),
    0x801B9798: table.sym_var("str_face_gfx_801B9798", "const char", "[]"),
    0x801B97C4: table.sym_var("str_face_gfx_801B97C4", "const char", "[]"),
    0x801B97E0: table.sym_var("str_face_gfx_801B97E0", "const char", "[]"),
    0x801B9804: table.sym_var("str_face_gfx_801B9804", "const char", "[]"),
    0x801B9824: table.sym_var("str_face_gfx_801B9824", "const char", "[]"),
    0x801B983C: table.sym_var("str_face_gfx_801B983C", "const char", "[]"),
    0x801B9858: table.sym_var("str_face_gfx_801B9858", "const char", "[]"),
    0x801B9860: table.sym_var("str_face_gfx_801B9860", "const char", "[]"),
    0x801B9878: table.sym_var("face_gfx_801B9878", "const double"),
    0x801B9880: table.sym_var_fnc("face_gfx_801B9880", "const", "[]"),
    0x801B98D8: table.sym_var_fnc("face_gfx_801B98D8", "const", "[]"),
    0x801B98F0: table.sym_var_fnc("face_gfx_801B98F0", "const", "[]"),
    0x801B9908: table.sym_var("face_gfx_801B9908", "const double"),
    0x801B9910: table.sym_var("face_gfx_801B9910", "const double"),
    0x801B9918: table.sym_var("face_gfx_801B9918", "const double"),
    0x801B9920: table.sym_var("face_gfx_801B9920", "const double"),
    0x801B9928: table.sym_var("face_gfx_801B9928", "const double"),
    0x801B9930: table.sym_var("face_gfx_801B9930", "const double"),
    0x801B9938: table.sym_var("face_gfx_801B9938", "const double"),
    0x801B9940: table.sym_var("face_gfx_801B9940", "const double"),
    0x801B9948: table.sym_var("face_gfx_801B9948", "const double"),
    0x801B9950: table.sym_var("face_gfx_801B9950", "const double"),
    0x801B9958: table.sym_var("face_gfx_801B9958", "const double"),
    0x801B9960: table.sym_var("face_gfx_801B9960", "const double"),
    0x801B9968: table.sym_var("face_gfx_801B9968", "const double"),
    0x801B9970: table.sym_var("face_gfx_801B9970", "const double"),
    0x801B9978: table.sym_var("face_gfx_801B9978", "const double"),
    0x801B9980: table.sym_var("face_gfx_801B9980", "const double"),
    0x801B9988: table.sym_var_fnc("face_gfx_801B9988", "const", "[]"),
    0x801B99D8: table.sym_var("face_gfx_801B99D8", "const double"),

    # ==========================================================================
    # bss
    # ==========================================================================
}

sym_E0_main = {
    0x00108A10: table.sym("_main_dataSegmentRomStart"),
    0x00108A40: table.sym("_main_szpSegmentRomStart"),
    0x00114750: table.sym("_main_szpSegmentRomEnd"),
    0x10000000: table.sym("p_main", table.GLOBL),

    0x02000000: table.sym_var("txt_dprint_0", "static u16", "[]"),
    0x02000200: table.sym_var("txt_dprint_1", "static u16", "[]"),
    0x02000400: table.sym_var("txt_dprint_2", "static u16", "[]"),
    0x02000600: table.sym_var("txt_dprint_3", "static u16", "[]"),
    0x02000800: table.sym_var("txt_dprint_4", "static u16", "[]"),
    0x02000A00: table.sym_var("txt_dprint_5", "static u16", "[]"),
    0x02000C00: table.sym_var("txt_dprint_6", "static u16", "[]"),
    0x02000E00: table.sym_var("txt_dprint_7", "static u16", "[]"),
    0x02001000: table.sym_var("txt_dprint_8", "static u16", "[]"),
    0x02001200: table.sym_var("txt_dprint_9", "static u16", "[]"),
    0x02001400: table.sym_var("txt_dprint_a", "static u16", "[]"),
    0x02001600: table.sym_var("txt_dprint_b", "static u16", "[]"),
    0x02001800: table.sym_var("txt_dprint_c", "static u16", "[]"),
    0x02001A00: table.sym_var("txt_dprint_d", "static u16", "[]"),
    0x02001C00: table.sym_var("txt_dprint_e", "static u16", "[]"),
    0x02001E00: table.sym_var("txt_dprint_f", "static u16", "[]"),
    0x02002000: table.sym_var("txt_dprint_g", "static u16", "[]"),
    0x02002200: table.sym_var("txt_dprint_h", "static u16", "[]"),
    0x02002400: table.sym_var("txt_dprint_i", "static u16", "[]"),
    0x02002600: table.sym_var("txt_dprint_k", "static u16", "[]"),
    0x02002800: table.sym_var("txt_dprint_l", "static u16", "[]"),
    0x02002A00: table.sym_var("txt_dprint_m", "static u16", "[]"),
    0x02002C00: table.sym_var("txt_dprint_n", "static u16", "[]"),
    0x02002E00: table.sym_var("txt_dprint_o", "static u16", "[]"),
    0x02003000: table.sym_var("txt_dprint_p", "static u16", "[]"),
    0x02003200: table.sym_var("txt_dprint_r", "static u16", "[]"),
    0x02003400: table.sym_var("txt_dprint_s", "static u16", "[]"),
    0x02003600: table.sym_var("txt_dprint_t", "static u16", "[]"),
    0x02003800: table.sym_var("txt_dprint_u", "static u16", "[]"),
    0x02003A00: table.sym_var("txt_dprint_w", "static u16", "[]"),
    0x02003C00: table.sym_var("txt_dprint_y", "static u16", "[]"),
    0x02003E00: table.sym_var("txt_dprint_squote",   "static u16", "[]"),
    0x02004000: table.sym_var("txt_dprint_dquote",   "static u16", "[]"),
    0x02004200: table.sym_var("txt_dprint_multiply", "static u16", "[]"),
    0x02004400: table.sym_var("txt_dprint_coin",     "static u16", "[]"),
    0x02004600: table.sym_var("txt_dprint_mario",    "static u16", "[]"),
    0x02004800: table.sym_var("txt_dprint_star",     "static u16", "[]"),
    0x02004A00: table.sym_var("txt_staff_3", "static u16", "[]"),
    0x02004A80: table.sym_var("txt_staff_4", "static u16", "[]"),
    0x02004B00: table.sym_var("txt_staff_6", "static u16", "[]"),
    0x02004B80: table.sym_var("txt_staff_a", "static u16", "[]"),
    0x02004C00: table.sym_var("txt_staff_b", "static u16", "[]"),
    0x02004C80: table.sym_var("txt_staff_c", "static u16", "[]"),
    0x02004D00: table.sym_var("txt_staff_d", "static u16", "[]"),
    0x02004D80: table.sym_var("txt_staff_e", "static u16", "[]"),
    0x02004E00: table.sym_var("txt_staff_f", "static u16", "[]"),
    0x02004E80: table.sym_var("txt_staff_g", "static u16", "[]"),
    0x02004F00: table.sym_var("txt_staff_h", "static u16", "[]"),
    0x02004F80: table.sym_var("txt_staff_i", "static u16", "[]"),
    0x02005000: table.sym_var("txt_staff_j", "static u16", "[]"),
    0x02005080: table.sym_var("txt_staff_k", "static u16", "[]"),
    0x02005100: table.sym_var("txt_staff_l", "static u16", "[]"),
    0x02005180: table.sym_var("txt_staff_m", "static u16", "[]"),
    0x02005200: table.sym_var("txt_staff_n", "static u16", "[]"),
    0x02005280: table.sym_var("txt_staff_o", "static u16", "[]"),
    0x02005300: table.sym_var("txt_staff_p", "static u16", "[]"),
    0x02005380: table.sym_var("txt_staff_q", "static u16", "[]"),
    0x02005400: table.sym_var("txt_staff_r", "static u16", "[]"),
    0x02005480: table.sym_var("txt_staff_s", "static u16", "[]"),
    0x02005500: table.sym_var("txt_staff_t", "static u16", "[]"),
    0x02005580: table.sym_var("txt_staff_u", "static u16", "[]"),
    0x02005600: table.sym_var("txt_staff_v", "static u16", "[]"),
    0x02005680: table.sym_var("txt_staff_w", "static u16", "[]"),
    0x02005700: table.sym_var("txt_staff_x", "static u16", "[]"),
    0x02005780: table.sym_var("txt_staff_y", "static u16", "[]"),
    0x02005800: table.sym_var("txt_staff_z", "static u16", "[]"),
    0x02005880: table.sym_var("txt_staff_period", "static u16", "[]"),
    0x02005900: table.sym_var("txt_message_0", "static u8", "[]"),
    0x02005940: table.sym_var("txt_message_1", "static u8", "[]"),
    0x02005980: table.sym_var("txt_message_2", "static u8", "[]"),
    0x020059C0: table.sym_var("txt_message_3", "static u8", "[]"),
    0x02005A00: table.sym_var("txt_message_4", "static u8", "[]"),
    0x02005A40: table.sym_var("txt_message_5", "static u8", "[]"),
    0x02005A80: table.sym_var("txt_message_6", "static u8", "[]"),
    0x02005AC0: table.sym_var("txt_message_7", "static u8", "[]"),
    0x02005B00: table.sym_var("txt_message_8", "static u8", "[]"),
    0x02005B40: table.sym_var("txt_message_9", "static u8", "[]"),
    0x02005B80: table.sym_var("txt_message_u_a", "static u8", "[]"),
    0x02005BC0: table.sym_var("txt_message_u_b", "static u8", "[]"),
    0x02005C00: table.sym_var("txt_message_u_c", "static u8", "[]"),
    0x02005C40: table.sym_var("txt_message_u_d", "static u8", "[]"),
    0x02005C80: table.sym_var("txt_message_u_e", "static u8", "[]"),
    0x02005CC0: table.sym_var("txt_message_u_f", "static u8", "[]"),
    0x02005D00: table.sym_var("txt_message_u_g", "static u8", "[]"),
    0x02005D40: table.sym_var("txt_message_u_h", "static u8", "[]"),
    0x02005D80: table.sym_var("txt_message_u_i", "static u8", "[]"),
    0x02005DC0: table.sym_var("txt_message_u_j", "static u8", "[]"),
    0x02005E00: table.sym_var("txt_message_u_k", "static u8", "[]"),
    0x02005E40: table.sym_var("txt_message_u_l", "static u8", "[]"),
    0x02005E80: table.sym_var("txt_message_u_m", "static u8", "[]"),
    0x02005EC0: table.sym_var("txt_message_u_n", "static u8", "[]"),
    0x02005F00: table.sym_var("txt_message_u_o", "static u8", "[]"),
    0x02005F40: table.sym_var("txt_message_u_p", "static u8", "[]"),
    0x02005F80: table.sym_var("txt_message_u_q", "static u8", "[]"),
    0x02005FC0: table.sym_var("txt_message_u_r", "static u8", "[]"),
    0x02006000: table.sym_var("txt_message_u_s", "static u8", "[]"),
    0x02006040: table.sym_var("txt_message_u_t", "static u8", "[]"),
    0x02006080: table.sym_var("txt_message_u_u", "static u8", "[]"),
    0x020060C0: table.sym_var("txt_message_u_v", "static u8", "[]"),
    0x02006100: table.sym_var("txt_message_u_w", "static u8", "[]"),
    0x02006140: table.sym_var("txt_message_u_x", "static u8", "[]"),
    0x02006180: table.sym_var("txt_message_u_y", "static u8", "[]"),
    0x020061C0: table.sym_var("txt_message_u_z", "static u8", "[]"),
    0x02006200: table.sym_var("txt_message_l_a", "static u8", "[]"),
    0x02006240: table.sym_var("txt_message_l_b", "static u8", "[]"),
    0x02006280: table.sym_var("txt_message_l_c", "static u8", "[]"),
    0x020062C0: table.sym_var("txt_message_l_d", "static u8", "[]"),
    0x02006300: table.sym_var("txt_message_l_e", "static u8", "[]"),
    0x02006340: table.sym_var("txt_message_l_f", "static u8", "[]"),
    0x02006380: table.sym_var("txt_message_l_g", "static u8", "[]"),
    0x020063C0: table.sym_var("txt_message_l_h", "static u8", "[]"),
    0x02006400: table.sym_var("txt_message_l_i", "static u8", "[]"),
    0x02006440: table.sym_var("txt_message_l_j", "static u8", "[]"),
    0x02006480: table.sym_var("txt_message_l_k", "static u8", "[]"),
    0x020064C0: table.sym_var("txt_message_l_l", "static u8", "[]"),
    0x02006500: table.sym_var("txt_message_l_m", "static u8", "[]"),
    0x02006540: table.sym_var("txt_message_l_n", "static u8", "[]"),
    0x02006580: table.sym_var("txt_message_l_o", "static u8", "[]"),
    0x020065C0: table.sym_var("txt_message_l_p", "static u8", "[]"),
    0x02006600: table.sym_var("txt_message_l_q", "static u8", "[]"),
    0x02006640: table.sym_var("txt_message_l_r", "static u8", "[]"),
    0x02006680: table.sym_var("txt_message_l_s", "static u8", "[]"),
    0x020066C0: table.sym_var("txt_message_l_t", "static u8", "[]"),
    0x02006700: table.sym_var("txt_message_l_u", "static u8", "[]"),
    0x02006740: table.sym_var("txt_message_l_v", "static u8", "[]"),
    0x02006780: table.sym_var("txt_message_l_w", "static u8", "[]"),
    0x020067C0: table.sym_var("txt_message_l_x", "static u8", "[]"),
    0x02006800: table.sym_var("txt_message_l_y", "static u8", "[]"),
    0x02006840: table.sym_var("txt_message_l_z", "static u8", "[]"),
    0x02006880: table.sym_var("txt_message_arrow",      "static u8", "[]"),
    0x020068C0: table.sym_var("txt_message_exclaim",    "static u8", "[]"),
    0x02006900: table.sym_var("txt_message_coin",       "static u8", "[]"),
    0x02006940: table.sym_var("txt_message_multiply",   "static u8", "[]"),
    0x02006980: table.sym_var("txt_message_paren_l",    "static u8", "[]"),
    0x020069C0: table.sym_var("txt_message_paren_rl",   "static u8", "[]"),
    0x02006A00: table.sym_var("txt_message_paren_r",    "static u8", "[]"),
    0x02006A40: table.sym_var("txt_message_tilde",      "static u8", "[]"),
    0x02006A80: table.sym_var("txt_message_period",     "static u8", "[]"),
    0x02006AC0: table.sym_var("txt_message_percent",    "static u8", "[]"),
    0x02006B00: table.sym_var("txt_message_bullet",     "static u8", "[]"),
    0x02006B40: table.sym_var("txt_message_comma",      "static u8", "[]"),
    0x02006B80: table.sym_var("txt_message_apostrophe", "static u8", "[]"),
    0x02006BC0: table.sym_var("txt_message_question",   "static u8", "[]"),
    0x02006C00: table.sym_var("txt_message_star",       "static u8", "[]"),
    0x02006C40: table.sym_var("txt_message_star_outline", "static u8", "[]"),
    0x02006C80: table.sym_var("txt_message_quote_l",    "static u8", "[]"),
    0x02006CC0: table.sym_var("txt_message_quote_r",    "static u8", "[]"),
    0x02006D00: table.sym_var("txt_message_colon",      "static u8", "[]"),
    0x02006D40: table.sym_var("txt_message_hyphen",     "static u8", "[]"),
    0x02006D80: table.sym_var("txt_message_ampersand",  "static u8", "[]"),
    0x02006DC0: table.sym_var("txt_message_button_a",   "static u8", "[]"),
    0x02006E00: table.sym_var("txt_message_button_b",   "static u8", "[]"),
    0x02006E40: table.sym_var("txt_message_button_c",   "static u8", "[]"),
    0x02006E80: table.sym_var("txt_message_button_z",   "static u8", "[]"),
    0x02006EC0: table.sym_var("txt_message_button_r",   "static u8", "[]"),
    0x02006F00: table.sym_var("txt_message_button_cu",  "static u8", "[]"),
    0x02006F40: table.sym_var("txt_message_button_cd",  "static u8", "[]"),
    0x02006F80: table.sym_var("txt_message_button_cl",  "static u8", "[]"),
    0x02006FC0: table.sym_var("txt_message_button_cr",  "static u8", "[]"),
    0x02007000: table.sym_var("txt_camera_camera",  "static u16", "[]"),
    0x02007200: table.sym_var("txt_camera_lakitu",  "static u16", "[]"),
    0x02007400: table.sym_var("txt_camera_cross",   "static u16", "[]"),
    0x02007600: table.sym_var("txt_camera_up",      "static u16", "[]"),
    0x02007680: table.sym_var("txt_camera_down",    "static u16", "[]"),
    0x02007700: table.sym_var("txt_dprint",     "u16 *", "[]"),
    0x020077E8: table.sym_var("txt_message",    "u8 *", "[]"),
    0x02007BE8: table.sym_var("txt_staff",      "u16 *", "[]"),
    0x02007C7C: table.sym_var("txt_camera",     "u16 *", "[]"),
    0x02007D28: table.sym_var("msg_select", "MSG *", "[]"),
    0x02010A68: table.sym_var("msg_en_us",  "MSG *", "[]"),
    0x02010F68: table.sym_var("str_course", "u8 *", "[]"),
    0x0201192C: table.sym_var("str_level", "u8 *", "[]"),
    0x02011AB8: table.sym_var("align_main",     "unused static u64"),
    0x02011AC0: table.sym_var("gfx_dprint_copy_start",  "Gfx", "[]"),
    0x02011AF8: table.sym_var("gfx_dprint_copy_char",   "Gfx", "[]"),
    0x02011B28: table.sym_var("gfx_dprint_copy_end",    "Gfx", "[]"),
    0x02011B60: table.sym_var("gfx_dprint_1cyc_start",  "Gfx", "[]"),
    0x02011B98: table.sym_var("gfx_dprint_1cyc_char",   "Gfx", "[]"),
    0x02011BC8: table.sym_var("gfx_dprint_1cyc_end",    "Gfx", "[]"),
    0x02011C08: table.sym_var("vtx_message_box",    "static Vtx", "[]"),
    0x02011C48: table.sym_var("gfx_message_box",    "Gfx", "[]"),
    0x02011C88: table.sym_var("vtx_message_char",   "static Vtx", "[]"),
    0x02011CC8: table.sym_var("gfx_message_start",  "Gfx", "[]"),
    0x02011D08: table.sym_var("gfx_message_char",   "Gfx", "[]"),
    0x02011D50: table.sym_var("gfx_message_end",    "Gfx", "[]"),
    0x02011D90: table.sym_var("vtx_message_cursor", "static Vtx", "[]"),
    0x02011DC0: table.sym_var("gfx_message_cursor", "Gfx", "[]"),
    0x02011E50: table.sym_var("gfx_number_start",   "static Gfx", "[]"),
    0x02011E98: table.sym_var("gfx_number_end",     "static Gfx", "[]"),
    0x02011ED8: table.sym_var("gfx_number_0",       "Gfx", "[]"),
    0x02011F08: table.sym_var("gfx_number_1",       "Gfx", "[]"),
    0x02011F38: table.sym_var("gfx_number_2",       "Gfx", "[]"),
    0x02011F68: table.sym_var("gfx_number_3",       "Gfx", "[]"),
    0x02011F98: table.sym_var("gfx_number_4",       "Gfx", "[]"),
    0x02011FC8: table.sym_var("gfx_number_5",       "Gfx", "[]"),
    0x02011FF8: table.sym_var("gfx_number_6",       "Gfx", "[]"),
    0x02012028: table.sym_var("gfx_number_7",       "Gfx", "[]"),
    0x02012058: table.sym_var("gfx_number_8",       "Gfx", "[]"),
    0x02012088: table.sym_var("gfx_number_9",       "Gfx", "[]"),
    0x020120B8: table.sym_var("txt_shadow_circle",  "static u8", "[]"),
    0x020121B8: table.sym_var("txt_shadow_square",  "static u8", "[]"),
    0x020122B8: table.sym_var("txt_wipe_star",      "u8", "[]"),
    0x02012AB8: table.sym_var("txt_wipe_circle",    "u8", "[]"),
    0x020132B8: table.sym_var("txt_wipe_mario",     "u8", "[]"),
    0x020142B8: table.sym_var("txt_wipe_bowser",    "u8", "[]"),
    0x02014AB8: table.sym_var("txt_scroll_water_0", "u16", "[]"),
    0x020152B8: table.sym_var("txt_scroll_water_1", "u16", "[]"),
    0x02015AB8: table.sym_var("txt_scroll_water_2", "u16", "[]"),
    0x020162B8: table.sym_var("txt_scroll_mist", "u16", "[]"),
    0x02016AB8: table.sym_var("txt_scroll_lava", "u16", "[]"),
    0x020172B8: table.sym_var("light_unused", "unused static Lights1"), # unused
    0x020172D0: table.sym_var("mtx_identity",   "static Mtx"),
    0x02017310: table.sym_var("mtx_ortho",      "static Mtx"),
    0x02017350: table.sym_var("gfx_quad0", "Gfx", "[]"),
    0x02017368: table.sym_var("gfx_quad1", "Gfx", "[]"), # unused
    0x02017380: table.sym_var("gfx_shadow_start",   "static Gfx", "[]"),
    0x020173A8: table.sym_var("gfx_shadow_circle",  "Gfx", "[]"),
    0x020173F0: table.sym_var("gfx_shadow_square",  "Gfx", "[]"),
    0x02017438: table.sym_var("gfx_shadow_9",   "Gfx", "[]"),
    0x02017480: table.sym_var("gfx_shadow_4",   "Gfx", "[]"),
    0x02017498: table.sym_var("gfx_shadow_end", "Gfx", "[]"),
    0x020174C0: table.sym_var("gfx_wipe_start", "Gfx", "[]"),
    0x020174F8: table.sym_var("gfx_wipe_end",   "Gfx", "[]"),
    0x02017520: table.sym_var("gfx_wipe_draw",  "Gfx", "[]"),
    0x02017568: table.sym_var("gfx_background_start",   "Gfx", "[]"),
    0x02017598: table.sym_var("gfx_background_tile",    "Gfx", "[]"),
    0x020175C8: table.sym_var("gfx_background_end",     "Gfx", "[]"),
    0x020175F0: table.sym_var("gfx_scroll_rgba", "Gfx", "[]"),
    0x02017630: table.sym_var("gfx_scroll_ia", "Gfx", "[]"),
    0x02017670: table.sym_var("gfx_scroll_end", "Gfx", "[]"),
    0x02017698: table.sym_var("txt_minimap_arrow", "static u8", "[]"),
    0x020176D8: table.sym_var("gfx_minimap_start",  "unused static Gfx", "[]"), # unused
    0x02017710: table.sym_var("gfx_minimap_tile",   "unused static Gfx", "[]"), # unused
    0x02017740: table.sym_var("gfx_minimap_arrow",  "unused static Gfx", "[]"), # unused
    0x02017798: table.sym_var("gfx_minimap_end",    "unused static Gfx", "[]"), # unused
    0x020177B8: table.sym_var("light_ripple", "static Lights1"),
    0x020177D0: table.sym_var("gfx_ripple_s_start", "Gfx", "[]"),
    0x02017808: table.sym_var("gfx_ripple_s_end",   "Gfx", "[]"),
    0x02017828: table.sym_var("gfx_ripple_e_start", "Gfx", "[]"),
    0x02017860: table.sym_var("gfx_ripple_e_end",   "Gfx", "[]"),
    0x02017890: table.sym_var("gfx_ripple_draw",    "Gfx", "[]"),
    0x020178C0: table.sym_var("ripple_shape",   "s16", "[]"),
    0x020182A4: table.sym_var("ripple_shade",   "s16", "[]"),
}

sym_E0_shp_pl = {
    0x00114750: table.sym("_shape_player_szpSegmentRomStart"),
    0x001279B0: table.sym("_shape_player_dataSegmentRomStart"),

    # mario
    0x04000000: table.sym_var("light_mario_blue",       "static Lights1"),
    0x04000018: table.sym_var("light_mario_red",        "static Lights1"),
    0x04000030: table.sym_var("light_mario_white",      "static Lights1"),
    0x04000048: table.sym_var("light_mario_shoe",       "static Lights1"),
    0x04000060: table.sym_var("light_mario_skin",       "static Lights1"),
    0x04000078: table.sym_var("light_mario_hair",       "static Lights1"),
    0x04000090: table.sym_var("txt_mario_metal",        "static u16", "[]"),
    0x04001090: table.sym_var("txt_mario_button",       "static u16", "[]"),
    0x04001890: table.sym_var("txt_mario_logo",         "static u16", "[]"),
    0x04002090: table.sym_var("txt_mario_sideburn",     "static u16", "[]"),
    0x04002890: table.sym_var("txt_mario_moustache",    "static u16", "[]"),
    0x04003090: table.sym_var("txt_mario_eye_open",     "static u16", "[]"),
    0x04003890: table.sym_var("txt_mario_eye_half",     "static u16", "[]"),
    0x04004090: table.sym_var("txt_mario_eye_closed",   "static u16", "[]"),
    0x04005890: table.sym_var("txt_mario_eye_left",     "static u16", "[]"),
    0x04006090: table.sym_var("txt_mario_eye_right",    "static u16", "[]"),
    0x04006890: table.sym_var("txt_mario_eye_up",       "static u16", "[]"),
    0x04007090: table.sym_var("txt_mario_eye_down",     "static u16", "[]"),
    0x04007890: table.sym_var("txt_mario_eye_dead",     "static u16", "[]"),
    0x04008090: table.sym_var("txt_mario_wing_l",       "static u16", "[]"),
    0x04009090: table.sym_var("txt_mario_wing_r",       "static u16", "[]"),
    0x0400A090: table.sym_var("txt_mario_metal_wing_l", "static u16", "[]"),
    0x0400B090: table.sym_var("txt_mario_metal_wing_r", "static u16", "[]"),
    0x0400CA00: table.sym_var("gfx_mario_h_waist",      "static Gfx", "[]"),
    0x0400CC98: table.sym_var("gfx_mario_h_waist_s",    "Gfx", "[]"),
    0x0400CCC8: table.sym_var("gfx_mario_h_waist_e",    "Gfx", "[]"),
    0x0400D090: table.sym_var("gfx_mario_h_uarmL",      "Gfx", "[]"),
    0x0400D1D8: table.sym_var("gfx_mario_h_uarmL_s",    "Gfx", "[]"),
    0x0400D2F8: table.sym_var("gfx_mario_h_larmL",      "Gfx", "[]"),
    0x0400D758: table.sym_var("gfx_mario_h_fistL",      "Gfx", "[]"),
    0x0400D8F0: table.sym_var("gfx_mario_h_fistL_s",    "Gfx", "[]"),
    0x0400DCA0: table.sym_var("gfx_mario_h_uarmR",      "Gfx", "[]"),
    0x0400DDE8: table.sym_var("gfx_mario_h_uarmR_s",    "Gfx", "[]"),
    0x0400DF08: table.sym_var("gfx_mario_h_larmR",      "Gfx", "[]"),
    0x0400E2C8: table.sym_var("gfx_mario_h_fistR",      "static Gfx", "[]"),
    0x0400E458: table.sym_var("gfx_mario_h_fistR_s",    "Gfx", "[]"),
    0x0400E478: table.sym_var("gfx_mario_h_fistR_e",    "Gfx", "[]"),
    0x0400E6A8: table.sym_var("gfx_mario_h_thighL",     "static Gfx", "[]"),
    0x0400E7B0: table.sym_var("gfx_mario_h_thighL_s",   "Gfx", "[]"),
    0x0400E7E0: table.sym_var("gfx_mario_h_thighL_e",   "Gfx", "[]"),
    0x0400E918: table.sym_var("gfx_mario_h_shinL",      "Gfx", "[]"),
    0x0400EBB8: table.sym_var("gfx_mario_h_shoeL",      "Gfx", "[]"),
    0x0400ECA0: table.sym_var("gfx_mario_h_shoeL_s",    "Gfx", "[]"),
    0x0400EEB0: table.sym_var("gfx_mario_h_thighR",     "Gfx", "[]"),
    0x0400EFB8: table.sym_var("gfx_mario_h_thighR_s",   "Gfx", "[]"),
    0x0400F1D8: table.sym_var("gfx_mario_h_shinR",      "Gfx", "[]"),
    0x0400F400: table.sym_var("gfx_mario_h_shoeR",      "static Gfx", "[]"),
    0x0400F4E8: table.sym_var("gfx_mario_h_shoeR_s",    "Gfx", "[]"),
    0x0400F528: table.sym_var("gfx_mario_h_shoeR_e",    "Gfx", "[]"),
    0x0400FF28: table.sym_var("gfx_mario_h_torso0",     "static Gfx", "[]"),
    0x0400FF88: table.sym_var("gfx_mario_h_torso1",     "static Gfx", "[]"),
    0x04010260: table.sym_var("gfx_mario_h_torso2",     "static Gfx", "[]"),
    0x04010348: table.sym_var("gfx_mario_h_torso12_s",  "static Gfx", "[]"),
    0x04010370: table.sym_var("gfx_mario_h_torso_s",    "Gfx", "[]"),
    0x040103F0: table.sym_var("gfx_mario_h_torso",      "Gfx", "[]"),
    0x040112B0: table.sym_var("gfx_mario_h_cap0",       "static Gfx", "[]"),
    0x040112E8: table.sym_var("gfx_mario_h_cap1",       "static Gfx", "[]"),
    0x04011350: table.sym_var("gfx_mario_h_cap2",       "static Gfx", "[]"),
    0x040113A0: table.sym_var("gfx_mario_h_cap3",       "static Gfx", "[]"),
    0x04011438: table.sym_var("gfx_mario_h_cap4",       "static Gfx", "[]"),
    0x040116F8: table.sym_var("gfx_mario_h_cap5",       "static Gfx", "[]"),
    0x04011870: table.sym_var("gfx_mario_h_cap6",       "static Gfx", "[]"),
    0x04011960: table.sym_var("gfx_mario_h_cap456_s",   "static Gfx", "[]"),
    0x040119A0: table.sym_var("gfx_mario_h_cap_open",   "Gfx", "[]"),
    0x04011A90: table.sym_var("gfx_mario_h_cap_half",   "Gfx", "[]"),
    0x04011B80: table.sym_var("gfx_mario_h_cap_closed", "Gfx", "[]"),
    0x04011C70: table.sym_var("gfx_mario_h_cap_left",   "Gfx", "[]"),
    0x04011D60: table.sym_var("gfx_mario_h_cap_right",  "Gfx", "[]"),
    0x04011E50: table.sym_var("gfx_mario_h_cap_up",     "Gfx", "[]"),
    0x04011F40: table.sym_var("gfx_mario_h_cap_down",   "Gfx", "[]"),
    0x04012030: table.sym_var("gfx_mario_h_cap_dead",   "Gfx", "[]"),
    0x04012120: table.sym_var("gfx_mario_h_cap",        "Gfx", "[]"),
    0x04012160: table.sym_var("light_mario_skin_old",   "unused static Lights1"),
    0x04012178: table.sym_var("light_mario_hair_old",   "unused static Lights1"),
    0x040132B0: table.sym_var("gfx_mario_h_hair0",      "static Gfx", "[]"),
    0x04013318: table.sym_var("gfx_mario_h_hair1",      "static Gfx", "[]"),
    0x040133A8: table.sym_var("gfx_mario_h_hair2",      "static Gfx", "[]"),
    0x040133F8: table.sym_var("gfx_mario_h_hair3",      "static Gfx", "[]"),
    0x040136D0: table.sym_var("gfx_mario_h_hair4",      "static Gfx", "[]"),
    0x040139C0: table.sym_var("gfx_mario_h_hair34_s",   "static Gfx", "[]"),
    0x040139E8: table.sym_var("gfx_mario_h_hair_open",      "Gfx", "[]"),
    0x04013AB8: table.sym_var("gfx_mario_h_hair_half",      "Gfx", "[]"),
    0x04013B88: table.sym_var("gfx_mario_h_hair_closed",    "Gfx", "[]"),
    0x04013C58: table.sym_var("gfx_mario_h_hair_left",      "Gfx", "[]"),
    0x04013D28: table.sym_var("gfx_mario_h_hair_right",     "Gfx", "[]"),
    0x04013DF8: table.sym_var("gfx_mario_h_hair_up",        "Gfx", "[]"),
    0x04013EC8: table.sym_var("gfx_mario_h_hair_down",      "Gfx", "[]"),
    0x04013F98: table.sym_var("gfx_mario_h_hair_dead",      "Gfx", "[]"),
    0x04014068: table.sym_var("gfx_mario_h_hair",           "Gfx", "[]"),
    0x040144D8: table.sym_var("gfx_mario_m_waist",      "static Gfx", "[]"),
    0x04014638: table.sym_var("gfx_mario_m_waist_s",    "Gfx", "[]"),
    0x04014668: table.sym_var("gfx_mario_m_waist_e",    "Gfx", "[]"),
    0x040147D0: table.sym_var("gfx_mario_m_uarmL",      "Gfx", "[]"),
    0x04014840: table.sym_var("gfx_mario_m_uarmL_s",    "Gfx", "[]"),
    0x04014950: table.sym_var("gfx_mario_m_larmL",      "Gfx", "[]"),
    0x04014C90: table.sym_var("gfx_mario_m_fistL",      "Gfx", "[]"),
    0x04014DC0: table.sym_var("gfx_mario_m_fistL_s",    "Gfx", "[]"),
    0x04014ED0: table.sym_var("gfx_mario_m_uarmR",      "Gfx", "[]"),
    0x04014F40: table.sym_var("gfx_mario_m_uarmR_s",    "Gfx", "[]"),
    0x04015050: table.sym_var("gfx_mario_m_larmR",      "Gfx", "[]"),
    0x040153B0: table.sym_var("gfx_mario_m_fistR",      "Gfx", "[]"),
    0x040154E0: table.sym_var("gfx_mario_m_fistR_s",    "Gfx", "[]"),
    0x04015500: table.sym_var("gfx_mario_m_fistR_e",    "Gfx", "[]"),
    0x04015620: table.sym_var("gfx_mario_m_thighL",     "static Gfx", "[]"),
    0x040156B0: table.sym_var("gfx_mario_m_thighL_s",   "Gfx", "[]"),
    0x040156E0: table.sym_var("gfx_mario_m_thighL_e",   "Gfx", "[]"),
    0x04015848: table.sym_var("gfx_mario_m_shinL",      "Gfx", "[]"),
    0x04015A98: table.sym_var("gfx_mario_m_shoeL",      "Gfx", "[]"),
    0x04015B60: table.sym_var("gfx_mario_m_shoeL_s",    "Gfx", "[]"),
    0x04015C70: table.sym_var("gfx_mario_m_thighR",     "Gfx", "[]"),
    0x04015D00: table.sym_var("gfx_mario_m_thighR_s",   "Gfx", "[]"),
    0x04015E10: table.sym_var("gfx_mario_m_shinR",      "Gfx", "[]"),
    0x04016000: table.sym_var("gfx_mario_m_shoeR",      "static Gfx", "[]"),
    0x040160C8: table.sym_var("gfx_mario_m_shoeR_s",    "Gfx", "[]"),
    0x04016108: table.sym_var("gfx_mario_m_shoeR_e",    "Gfx", "[]"),
    0x04016668: table.sym_var("gfx_mario_m_torso0",     "static Gfx", "[]"),
    0x040166B8: table.sym_var("gfx_mario_m_torso1",     "static Gfx", "[]"),
    0x04016800: table.sym_var("gfx_mario_m_torso2",     "static Gfx", "[]"),
    0x040168A0: table.sym_var("gfx_mario_m_torso12_s",  "static Gfx", "[]"),
    0x040168C8: table.sym_var("gfx_mario_m_torso_s",    "Gfx", "[]"),
    0x04016948: table.sym_var("gfx_mario_m_torso_e",    "Gfx", "[]"),
    0x04016A18: table.sym_var("gfx_mario_l_waist",      "static Gfx", "[]"),
    0x04016AB8: table.sym_var("gfx_mario_l_waist_s",    "Gfx", "[]"),
    0x04016AE8: table.sym_var("gfx_mario_l_waist_e",    "Gfx", "[]"),
    0x04016C20: table.sym_var("gfx_mario_l_uarmL",      "Gfx", "[]"),
    0x04016C70: table.sym_var("gfx_mario_l_uarmL_s",    "Gfx", "[]"),
    0x04016D50: table.sym_var("gfx_mario_l_larmL",      "Gfx", "[]"),
    0x04016E20: table.sym_var("gfx_mario_l_fistL",      "Gfx", "[]"),
    0x04016E80: table.sym_var("gfx_mario_l_fistL_s",    "Gfx", "[]"),
    0x04016F60: table.sym_var("gfx_mario_l_uarmR",      "Gfx", "[]"),
    0x04016FB0: table.sym_var("gfx_mario_l_uarmR_s",    "Gfx", "[]"),
    0x04017090: table.sym_var("gfx_mario_l_larmR",      "Gfx", "[]"),
    0x04017160: table.sym_var("gfx_mario_l_fistR",      "static Gfx", "[]"),
    0x040171C0: table.sym_var("gfx_mario_l_fistR_s",    "Gfx", "[]"),
    0x040171E0: table.sym_var("gfx_mario_l_fistR_e",    "Gfx", "[]"),
    0x040172F0: table.sym_var("gfx_mario_l_thighL",     "static Gfx", "[]"),
    0x04017360: table.sym_var("gfx_mario_l_thighL_s",   "Gfx", "[]"),
    0x04017390: table.sym_var("gfx_mario_l_thighL_e",   "Gfx", "[]"),
    0x040174E8: table.sym_var("gfx_mario_l_shinL",      "Gfx", "[]"),
    0x04017638: table.sym_var("gfx_mario_l_shoeL",      "Gfx", "[]"),
    0x040176A8: table.sym_var("gfx_mario_l_shoeL_s",    "Gfx", "[]"),
    0x040177A8: table.sym_var("gfx_mario_l_thighR",     "Gfx", "[]"),
    0x04017818: table.sym_var("gfx_mario_l_thighR_s",   "Gfx", "[]"),
    0x04017918: table.sym_var("gfx_mario_l_shinR",      "Gfx", "[]"),
    0x04017A68: table.sym_var("gfx_mario_l_shoeR",      "static Gfx", "[]"),
    0x04017AD8: table.sym_var("gfx_mario_l_shoeR_s",    "Gfx", "[]"),
    0x04017B18: table.sym_var("gfx_mario_l_shoeR_e",    "Gfx", "[]"),
    0x04017D68: table.sym_var("gfx_mario_l_torso0",     "static Gfx", "[]"),
    0x04017D98: table.sym_var("gfx_mario_l_torso1",     "static Gfx", "[]"),
    0x04017E20: table.sym_var("gfx_mario_l_torso2",     "static Gfx", "[]"),
    0x04017E78: table.sym_var("gfx_mario_l_torso12_s",  "static Gfx", "[]"),
    0x04017EA0: table.sym_var("gfx_mario_l_torso_s",    "Gfx", "[]"),
    0x04017F20: table.sym_var("gfx_mario_l_torso_e",    "Gfx", "[]"),
    0x04018270: table.sym_var("gfx_mario_l_cap0",       "static Gfx", "[]"),
    0x04018298: table.sym_var("gfx_mario_l_cap1",       "static Gfx", "[]"),
    0x040182C0: table.sym_var("gfx_mario_l_cap2",       "static Gfx", "[]"),
    0x04018300: table.sym_var("gfx_mario_l_cap3",       "static Gfx", "[]"),
    0x04018370: table.sym_var("gfx_mario_l_cap4",       "static Gfx", "[]"),
    0x040183F0: table.sym_var("gfx_mario_l_cap5",       "static Gfx", "[]"),
    0x04018420: table.sym_var("gfx_mario_l_cap345_s",   "static Gfx", "[]"),
    0x04018460: table.sym_var("gfx_mario_l_cap_open",   "Gfx", "[]"),
    0x04018530: table.sym_var("gfx_mario_l_cap_half",   "Gfx", "[]"),
    0x04018600: table.sym_var("gfx_mario_l_cap_closed", "Gfx", "[]"),
    0x040186D0: table.sym_var("gfx_mario_l_cap_left",   "Gfx", "[]"),
    0x040187A0: table.sym_var("gfx_mario_l_cap_right",  "Gfx", "[]"),
    0x04018870: table.sym_var("gfx_mario_l_cap_up",     "Gfx", "[]"),
    0x04018940: table.sym_var("gfx_mario_l_cap_down",   "Gfx", "[]"),
    0x04018A10: table.sym_var("gfx_mario_l_cap_dead",   "Gfx", "[]"),
    0x04018AE0: table.sym_var("gfx_mario_l_cap",        "Gfx", "[]"),
    0x04018DC8: table.sym_var("gfx_mario_l_hair0",      "static Gfx", "[]"),
    0x04018DF0: table.sym_var("gfx_mario_l_hair1",      "static Gfx", "[]"),
    0x04018E30: table.sym_var("gfx_mario_l_hair2",      "static Gfx", "[]"),
    0x04018EA0: table.sym_var("gfx_mario_l_hair3",      "static Gfx", "[]"),
    0x04018F68: table.sym_var("gfx_mario_l_hair23_s",   "static Gfx", "[]"),
    0x04018F90: table.sym_var("gfx_mario_l_hair_open",      "Gfx", "[]"),
    0x04019040: table.sym_var("gfx_mario_l_hair_half",      "Gfx", "[]"),
    0x040190F0: table.sym_var("gfx_mario_l_hair_closed",    "Gfx", "[]"),
    0x040191A0: table.sym_var("gfx_mario_l_hair_left",      "Gfx", "[]"),
    0x04019250: table.sym_var("gfx_mario_l_hair_right",     "Gfx", "[]"),
    0x04019300: table.sym_var("gfx_mario_l_hair_up",        "Gfx", "[]"),
    0x040193B0: table.sym_var("gfx_mario_l_hair_down",      "Gfx", "[]"),
    0x04019460: table.sym_var("gfx_mario_l_hair_dead",      "Gfx", "[]"),
    0x04019510: table.sym_var("gfx_mario_l_hair",           "Gfx", "[]"),
    0x04019A68: table.sym_var("gfx_mario_handL",        "Gfx", "[]"),
    0x04019CA0: table.sym_var("gfx_mario_handL_s",      "Gfx", "[]"),
    0x0401A1F0: table.sym_var("gfx_mario_handR",        "static Gfx", "[]"),
    0x0401A428: table.sym_var("gfx_mario_handR_s",      "Gfx", "[]"),
    0x0401A448: table.sym_var("gfx_mario_handR_e",      "Gfx", "[]"),
    0x0401ABA8: table.sym_var("gfx_mario_capR0",        "static Gfx", "[]"),
    0x0401ABD0: table.sym_var("gfx_mario_capR1",        "static Gfx", "[]"),
    0x0401AD40: table.sym_var("gfx_mario_capR2",        "static Gfx", "[]"),
    0x0401AED0: table.sym_var("gfx_mario_capR3",        "static Gfx", "[]"),
    0x0401AF20: table.sym_var("gfx_mario_capR123_s",    "static Gfx", "[]"),
    0x0401B080: table.sym_var("gfx_mario_wingsR_l",     "static Gfx", "[]"),
    0x0401B0B0: table.sym_var("gfx_mario_wingsR_r",     "static Gfx", "[]"),
    0x0401B0E0: table.sym_var("gfx_mario_wingsR_start", "static Gfx", "[]"),
    0x0401B138: table.sym_var("gfx_mario_wingsR_end",   "static Gfx", "[]"),
    0x0401B158: table.sym_var("gfx_mario_capR_s",       "Gfx", "[]"),
    0x0401B1D8: table.sym_var("gfx_mario_wingsR_s",     "Gfx", "[]"),
    0x0401B230: table.sym_var("gfx_mario_capR_e",       "Gfx", "[]"),
    0x0401B278: table.sym_var("gfx_mario_wingsR_e",     "Gfx", "[]"),
    0x0401BC80: table.sym_var("gfx_mario_peaceR",       "Gfx", "[]"),
    0x0401BF30: table.sym_var("gfx_mario_peaceR_s",     "Gfx", "[]"),
    0x0401C330: table.sym_var("gfx_mario_cap0",         "static Gfx", "[]"),
    0x0401C368: table.sym_var("gfx_mario_cap1",         "static Gfx", "[]"),
    0x0401C4C8: table.sym_var("gfx_mario_cap2",         "static Gfx", "[]"),
    0x0401C510: table.sym_var("gfx_mario_cap12_s",      "static Gfx", "[]"),
    0x0401C678: table.sym_var("gfx_mario_wings_l",      "static Gfx", "[]"),
    0x0401C6A8: table.sym_var("gfx_mario_wings_r",      "static Gfx", "[]"),
    0x0401C6D8: table.sym_var("gfx_mario_wings_start",  "static Gfx", "[]"),
    0x0401C730: table.sym_var("gfx_mario_wings_end",    "static Gfx", "[]"),
    0x0401C758: table.sym_var("gfx_mario_cap_s",        "Gfx", "[]"), # unused
    0x0401C7E8: table.sym_var("gfx_mario_wings_s",      "Gfx", "[]"), # unused
    0x0401C890: table.sym_var("gfx_mario_cap_e",        "Gfx", "[]"), # unused
    0x0401C8E8: table.sym_var("gfx_mario_wings_e",      "Gfx", "[]"), # unused
    0x0401C9C0: table.sym_var("gfx_mario_wing_l",       "static Gfx", "[]"),
    0x0401C9E0: table.sym_var("gfx_mario_wing_r",       "static Gfx", "[]"),
    0x0401CA00: table.sym_var("gfx_mario_wing_so",      "Gfx", "[]"),
    0x0401CAB8: table.sym_var("gfx_mario_wing_sx",      "Gfx", "[]"),
    0x0401CB70: table.sym_var("gfx_mario_wing_eo",      "Gfx", "[]"),
    0x0401CC28: table.sym_var("gfx_mario_wing_ex",      "Gfx", "[]"),

    # bubble
    0x0401CD60: table.sym_var("txt_bubble_a",   "static u16", "[]"),
    0x0401D560: table.sym_var("txt_bubble_b",   "static u16", "[]"),
    0x0401DD60: table.sym_var("gfx_bubble_a",   "Gfx", "[]"),
    0x0401DDE0: table.sym_var("gfx_bubble_b",   "Gfx", "[]"),

    # dust
    0x0401DEA0: table.sym_var("txt_dust_0", "static u16", "[]"),
    0x0401E6A0: table.sym_var("txt_dust_1", "static u16", "[]"),
    0x0401EEA0: table.sym_var("txt_dust_2", "static u16", "[]"),
    0x0401F6A0: table.sym_var("txt_dust_3", "static u16", "[]"),
    0x0401FEA0: table.sym_var("txt_dust_4", "static u16", "[]"),
    0x040206A0: table.sym_var("txt_dust_5", "static u16", "[]"),
    0x04020EA0: table.sym_var("txt_dust_6", "static u16", "[]"),
    0x040216A0: table.sym_var("gfx_dust",   "static Gfx", "[]"),
    0x04021718: table.sym_var("gfx_dust_0", "Gfx", "[]"),
    0x04021730: table.sym_var("gfx_dust_1", "Gfx", "[]"),
    0x04021748: table.sym_var("gfx_dust_2", "Gfx", "[]"),
    0x04021760: table.sym_var("gfx_dust_3", "Gfx", "[]"),
    0x04021778: table.sym_var("gfx_dust_4", "Gfx", "[]"),
    0x04021790: table.sym_var("gfx_dust_5", "Gfx", "[]"),
    0x040217A8: table.sym_var("gfx_dust_6", "Gfx", "[]"),

    # smoke
    0x04021800: table.sym_var("txt_smoke",          "static u16", "[]"),
    0x04022000: table.sym_var("gfx_smoke_start",    "static Gfx", "[]"),
    0x04022028: table.sym_var("gfx_smoke",          "static Gfx", "[]"),
    0x04022048: table.sym_var("gfx_smoke_end",      "static Gfx", "[]"),
    0x04022070: table.sym_var("gfx_smoke_s",        "Gfx", "[]"),

    # wave
    0x040220C8: table.sym_var("vtx_wave",       "static Vtx", "[]"),
    0x04022108: table.sym_var("vtx_wave_red",   "static Vtx", "[]"),
    0x04022148: table.sym_var("txt_wave_0",     "static u16", "[]"),
    0x04022948: table.sym_var("txt_wave_1",     "static u16", "[]"),
    0x04023148: table.sym_var("txt_wave_2",     "static u16", "[]"),
    0x04023948: table.sym_var("txt_wave_3",     "static u16", "[]"),
    0x04024148: table.sym_var("txt_wave_4",     "static u16", "[]"),
    0x04024948: table.sym_var("txt_wave_5",     "static u16", "[]"),
    0x04025148: table.sym_var("gfx_wave_start", "static Gfx", "[]"),
    0x04025190: table.sym_var("gfx_wave_end",   "static Gfx", "[]"),
    0x040251C8: table.sym_var("gfx_wave",       "static Gfx", "[]"),
    0x040251E0: table.sym_var("gfx_wave_red",   "static Gfx", "[]"),
    0x040251F8: table.sym_var("gfx_wave_0",     "Gfx", "[]"),
    0x04025210: table.sym_var("gfx_wave_1",     "Gfx", "[]"),
    0x04025228: table.sym_var("gfx_wave_2",     "Gfx", "[]"),
    0x04025240: table.sym_var("gfx_wave_3",     "Gfx", "[]"),
    0x04025258: table.sym_var("gfx_wave_4",     "Gfx", "[]"),
    0x04025270: table.sym_var("gfx_wave_5",     "Gfx", "[]"),
    0x04025288: table.sym_var("gfx_wave_red_0", "Gfx", "[]"),
    0x040252A0: table.sym_var("gfx_wave_red_1", "Gfx", "[]"),
    0x040252B8: table.sym_var("gfx_wave_red_2", "Gfx", "[]"),
    0x040252D0: table.sym_var("gfx_wave_red_3", "Gfx", "[]"),
    0x040252E8: table.sym_var("gfx_wave_red_4", "Gfx", "[]"),
    0x04025300: table.sym_var("gfx_wave_red_5", "Gfx", "[]"),

    # ripple
    0x04025318: table.sym_var("vtx_ripple",         "static Vtx", "[]"),
    0x04025358: table.sym_var("txt_ripple_0",       "static u16", "[]"),
    0x04025B58: table.sym_var("txt_ripple_1",       "static u16", "[]"),
    0x04026358: table.sym_var("txt_ripple_2",       "static u16", "[]"),
    0x04026B58: table.sym_var("txt_ripple_3",       "static u16", "[]"),
    0x04027358: table.sym_var("gfx_ripple_start",   "static Gfx", "[]"),
    0x040273A0: table.sym_var("gfx_ripple_end",     "static Gfx", "[]"),
    0x040273D8: table.sym_var("gfx_ripple",         "static Gfx", "[]"),
    0x040273F0: table.sym_var("gfx_ripple_0",       "Gfx", "[]"),
    0x04027408: table.sym_var("gfx_ripple_1",       "Gfx", "[]"),
    0x04027420: table.sym_var("gfx_ripple_2",       "Gfx", "[]"),
    0x04027438: table.sym_var("gfx_ripple_3",       "Gfx", "[]"),

    # sparkle
    0x04027490: table.sym_var("txt_sparkle_5",  "static u16", "[]"),
    0x04027C90: table.sym_var("txt_sparkle_4",  "static u16", "[]"),
    0x04028490: table.sym_var("txt_sparkle_3",  "static u16", "[]"),
    0x04028C90: table.sym_var("txt_sparkle_2",  "static u16", "[]"),
    0x04029490: table.sym_var("txt_sparkle_1",  "static u16", "[]"),
    0x04029C90: table.sym_var("txt_sparkle_0",  "static u16", "[]"),
    0x0402A490: table.sym_var("gfx_sparkle",    "static Gfx", "[]"),
    0x0402A4F8: table.sym_var("gfx_sparkle_5",  "Gfx", "[]"),
    0x0402A510: table.sym_var("gfx_sparkle_4",  "Gfx", "[]"),
    0x0402A528: table.sym_var("gfx_sparkle_3",  "Gfx", "[]"),
    0x0402A540: table.sym_var("gfx_sparkle_2",  "Gfx", "[]"),
    0x0402A558: table.sym_var("gfx_sparkle_1",  "Gfx", "[]"),
    0x0402A570: table.sym_var("gfx_sparkle_0",  "Gfx", "[]"),

    # splash
    0x0402A5C8: table.sym_var("txt_splash_0",   "static u16", "[]"),
    0x0402B5C8: table.sym_var("txt_splash_1",   "static u16", "[]"),
    0x0402C5C8: table.sym_var("txt_splash_2",   "static u16", "[]"),
    0x0402D5C8: table.sym_var("txt_splash_3",   "static u16", "[]"),
    0x0402E5C8: table.sym_var("txt_splash_4",   "static u16", "[]"),
    0x0402F5C8: table.sym_var("txt_splash_5",   "static u16", "[]"),
    0x040305C8: table.sym_var("txt_splash_6",   "static u16", "[]"),
    0x040315C8: table.sym_var("txt_splash_7",   "static u16", "[]"),
    0x040325C8: table.sym_var("gfx_splash",     "static Gfx", "[]"),
    0x04032640: table.sym_var("gfx_splash_0",   "Gfx", "[]"),
    0x04032658: table.sym_var("gfx_splash_1",   "Gfx", "[]"),
    0x04032670: table.sym_var("gfx_splash_2",   "Gfx", "[]"),
    0x04032688: table.sym_var("gfx_splash_3",   "Gfx", "[]"),
    0x040326A0: table.sym_var("gfx_splash_4",   "Gfx", "[]"),
    0x040326B8: table.sym_var("gfx_splash_5",   "Gfx", "[]"),
    0x040326D0: table.sym_var("gfx_splash_6",   "Gfx", "[]"),
    0x040326E8: table.sym_var("gfx_splash_7",   "Gfx", "[]"),

    # droplet
    0x04032700: table.sym_var("vtx_droplet",        "static Vtx", "[]"),
    0x04032740: table.sym_var("vtx_droplet_red",    "static Vtx", "[]"),
    0x04032780: table.sym_var("txt_droplet",        "static u16", "[]"),
    0x04032980: table.sym_var("gfx_droplet_start",  "static Gfx", "[]"),
    0x040329E0: table.sym_var("gfx_droplet_end",    "static Gfx", "[]"),
    0x04032A18: table.sym_var("gfx_droplet",        "Gfx", "[]"), # 164
    0x04032A30: table.sym_var("gfx_droplet_red",    "Gfx", "[]"), # unused

    # glow
    0x04032A88: table.sym_var("txt_glow_0", "static u16", "[]"),
    0x04033288: table.sym_var("txt_glow_1", "static u16", "[]"),
    0x04033A88: table.sym_var("txt_glow_2", "static u16", "[]"),
    0x04034288: table.sym_var("txt_glow_3", "static u16", "[]"),
    0x04034A88: table.sym_var("txt_glow_4", "static u16", "[]"),
    0x04035288: table.sym_var("gfx_glow",   "static Gfx", "[]"),
    0x04035300: table.sym_var("gfx_glow_0", "Gfx", "[]"),
    0x04035318: table.sym_var("gfx_glow_1", "Gfx", "[]"),
    0x04035330: table.sym_var("gfx_glow_2", "Gfx", "[]"),
    0x04035348: table.sym_var("gfx_glow_3", "Gfx", "[]"),
    0x04035360: table.sym_var("gfx_glow_4", "Gfx", "[]"),

    # bubble
    0x17000000: table.sym_var("s_bubble_a", "S_SCRIPT", "[]", table.GLOBL), # 168
    0x1700001C: table.sym_var("s_bubble_b", "S_SCRIPT", "[]", table.GLOBL), # 170

    # dust
    0x17000038: table.sym_var("s_dust", "S_SCRIPT", "[]", table.GLOBL), # 150

    # smoke
    0x17000084: table.sym_var("s_smoke", "S_SCRIPT", "[]", table.GLOBL), # 148, 156

    # wave
    0x1700009C: table.sym_var("s_wave", "S_SCRIPT", "[]", table.GLOBL), # 165
    0x170000E0: table.sym_var("s_wave_red", "S_SCRIPT", "[]"), # unused

    # ripple
    0x17000124: table.sym_var("s_ripple_stop", "S_SCRIPT", "[]", table.GLOBL), # 166
    0x17000168: table.sym_var("s_ripple_move", "S_SCRIPT", "[]", table.GLOBL), # 163

    # sparkle
    0x170001BC: table.sym_var("s_sparkle", "S_SCRIPT", "[]", table.GLOBL), # 149

    # splash
    0x17000230: table.sym_var("s_splash", "S_SCRIPT", "[]", table.GLOBL), # 167

    # glow
    0x17000284: table.sym_var("s_glow", "S_SCRIPT", "[]", table.GLOBL), # 143

    # mario
    0x170002E0: table.sym_var("s_mario_hso_head",   "static S_SCRIPT", "[]"),
    0x1700041C: table.sym_var("s_mario_hso_gloveL", "static S_SCRIPT", "[]"),
    0x17000494: table.sym_var("s_mario_hso_gloveR", "static S_SCRIPT", "[]"),
    0x1700053C: table.sym_var("s_mario_hso",        "static S_SCRIPT", "[]"),
    0x170006F8: table.sym_var("s_mario_mso_gloveL", "static S_SCRIPT", "[]"),
    0x17000770: table.sym_var("s_mario_mso_gloveR", "static S_SCRIPT", "[]"),
    0x17000818: table.sym_var("s_mario_mso",        "static S_SCRIPT", "[]"),
    0x170009D4: table.sym_var("s_mario_lso_head",   "static S_SCRIPT", "[]"),
    0x17000B10: table.sym_var("s_mario_lso_gloveL", "static S_SCRIPT", "[]"),
    0x17000B88: table.sym_var("s_mario_lso_gloveR", "static S_SCRIPT", "[]"),
    0x17000C30: table.sym_var("s_mario_lso",        "static S_SCRIPT", "[]"),
    0x17000DEC: table.sym_var("s_mario_hsx_head",   "static S_SCRIPT", "[]"),
    0x17000F28: table.sym_var("s_mario_hsx_gloveL", "static S_SCRIPT", "[]"),
    0x17000FA0: table.sym_var("s_mario_hsx_gloveR", "static S_SCRIPT", "[]"),
    0x17001048: table.sym_var("s_mario_hsx",        "static S_SCRIPT", "[]"),
    0x17001204: table.sym_var("s_mario_msx_gloveL", "static S_SCRIPT", "[]"),
    0x1700127C: table.sym_var("s_mario_msx_gloveR", "static S_SCRIPT", "[]"),
    0x17001324: table.sym_var("s_mario_msx",        "static S_SCRIPT", "[]"),
    0x170014E0: table.sym_var("s_mario_lsx_head",   "static S_SCRIPT", "[]"),
    0x1700161C: table.sym_var("s_mario_lsx_gloveL", "static S_SCRIPT", "[]"),
    0x17001694: table.sym_var("s_mario_lsx_gloveR", "static S_SCRIPT", "[]"),
    0x1700173C: table.sym_var("s_mario_lsx",        "static S_SCRIPT", "[]"),
    0x170018F8: table.sym_var("s_mario_heo_head",   "static S_SCRIPT", "[]"),
    0x170019A4: table.sym_var("s_mario_heo_gloveL", "static S_SCRIPT", "[]"),
    0x17001A1C: table.sym_var("s_mario_heo_gloveR", "static S_SCRIPT", "[]"),
    0x17001AC4: table.sym_var("s_mario_heo",        "static S_SCRIPT", "[]"),
    0x17001C80: table.sym_var("s_mario_meo_gloveL", "static S_SCRIPT", "[]"),
    0x17001CF8: table.sym_var("s_mario_meo_gloveR", "static S_SCRIPT", "[]"),
    0x17001DA0: table.sym_var("s_mario_meo",        "static S_SCRIPT", "[]"),
    0x17001F5C: table.sym_var("s_mario_leo_head",   "static S_SCRIPT", "[]"),
    0x17002008: table.sym_var("s_mario_leo_gloveL", "static S_SCRIPT", "[]"),
    0x17002080: table.sym_var("s_mario_leo_gloveR", "static S_SCRIPT", "[]"),
    0x17002128: table.sym_var("s_mario_leo",        "static S_SCRIPT", "[]"),
    0x170022E4: table.sym_var("s_mario_hex_head",   "static S_SCRIPT", "[]"),
    0x17002390: table.sym_var("s_mario_hex_gloveL", "static S_SCRIPT", "[]"),
    0x17002408: table.sym_var("s_mario_hex_gloveR", "static S_SCRIPT", "[]"),
    0x170024B0: table.sym_var("s_mario_hex",        "static S_SCRIPT", "[]"),
    0x1700266C: table.sym_var("s_mario_mex_gloveL", "static S_SCRIPT", "[]"),
    0x170026E4: table.sym_var("s_mario_mex_gloveR", "static S_SCRIPT", "[]"),
    0x1700278C: table.sym_var("s_mario_mex",        "static S_SCRIPT", "[]"),
    0x17002958: table.sym_var("s_mario_lex_head",   "static S_SCRIPT", "[]"),
    0x17002A04: table.sym_var("s_mario_lex_gloveL", "static S_SCRIPT", "[]"),
    0x17002A7C: table.sym_var("s_mario_lex_gloveR", "static S_SCRIPT", "[]"),
    0x17002B24: table.sym_var("s_mario_lex",        "static S_SCRIPT", "[]"),
    0x17002CE0: table.sym_var("s_mario_h",          "static S_SCRIPT", "[]"),
    0x17002D14: table.sym_var("s_mario_m",          "static S_SCRIPT", "[]"),
    0x17002D48: table.sym_var("s_mario_l",          "static S_SCRIPT", "[]"),
    0x17002D7C: table.sym_var("s_mario_lod",        "static S_SCRIPT", "[]"),
    0x17002DD4: table.sym_var("s_mario", "S_SCRIPT", "[]", table.GLOBL), # 1
}

sym_E0_shp_1a = {
    0x0012A7E0: table.sym("_shape_1a_szpSegmentRomStart"),
    0x00132850: table.sym("_shape_1a_dataSegmentRomStart"),
    0x0C000000: table.sym_var("s_1a_85", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000018: table.sym_var("s_1a_86", "S_SCRIPT", "[]", table.GLOBL),
    0x0C0001E4: table.sym_var("s_1a_87", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000248: table.sym_var("s_1a_88", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000264: table.sym_var("s_1a_84", "S_SCRIPT", "[]", table.GLOBL),
    0x0C00028C: table.sym_var("s_1a_89", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_1b = {
    0x00132C60: table.sym("_shape_1b_szpSegmentRomStart"),
    0x00134A70: table.sym("_shape_1b_dataSegmentRomStart"),

    # bully
    0x050000E0: table.sym_var("txt_bully_horn",     "static u16", "[]"),
    0x050002E0: table.sym_var("gfx_bully_horn",     "static Gfx", "[]"),
    0x05000398: table.sym_var("gfx_bully_horn_s",   "Gfx", "[]"),
    0x05000408: table.sym_var("light_bully",        "static Lights1", "[]"),
    0x05000468: table.sym_var("txt_bully_body_l",   "static u16", "[]"),
    0x05001468: table.sym_var("txt_bully_body_r",   "static u16", "[]"),
    0x05002468: table.sym_var("txt_bully_eye",      "static u16", "[]"),
    0x05003708: table.sym_var("gfx_bully_shoeL",    "Gfx", "[]"),
    0x050037A0: table.sym_var("gfx_bully_shoeR",    "Gfx", "[]"),
    0x05003838: table.sym_var("gfx_bully_eye_old",  "Gfx", "[]"), # unused
    0x05003878: table.sym_var("gfx_bully_body_old", "Gfx", "[]"), # unused
    0x05003CD0: table.sym_var("gfx_bully_body_l",   "static Gfx", "[]"),
    0x05003D08: table.sym_var("gfx_bully_body_r",   "static Gfx", "[]"),
    0x05003D40: table.sym_var("gfx_bully_body_s",   "Gfx", "[]"),
    0x05003E38: table.sym_var("gfx_bully_body_big_l",   "static Gfx", "[]"),
    0x05003E70: table.sym_var("gfx_bully_body_big_r",   "static Gfx", "[]"),
    0x05003EA8: table.sym_var("gfx_bully_body_big_s",   "Gfx", "[]"),
    0x05003F80: table.sym_var("gfx_bully_eye",      "static Gfx", "[]"),
    0x05003FC8: table.sym_var("gfx_bully_eye_s",    "Gfx", "[]"),
    0x050042A4: table.sym_var("anime_bully_2",  "static ANIME"),
    0x050043D8: table.sym_var("anime_bully_1",  "static ANIME"),
    0x05004598: table.sym_var("anime_bully_0",  "static ANIME"),
    0x050046F4: table.sym_var("anime_bully_3",  "static ANIME"),
    0x0500470C: table.sym_var("anime_bully",    "ANIME *",  "[]"),
    0x05004720: table.sym_var("align_0", "unused static u64"),

    # blargg
    0x05004728: table.sym_var("light_blargg",   "static Lights1", "[]"),
    0x050058D0: table.sym_var("gfx_blargg_upper_jaw",   "Gfx", "[]"),
    0x05005A60: table.sym_var("gfx_blargg_lower_jaw",   "Gfx", "[]"),
    0x05005D00: table.sym_var("gfx_blargg_body",    "Gfx", "[]"),
    0x05006070: table.sym_var("anime_blargg_1", "static ANIME"),
    0x05006154: table.sym_var("anime_blargg_0", "static ANIME"),
    0x0500616C: table.sym_var("anime_blargg",   "ANIME *",  "[]"), # unused
    0x05006178: table.sym_var("align_1", "unused static u64"),

    # bully
    0x0C000000: table.sym_var("s_bully",    "S_SCRIPT", "[]", table.GLOBL), # 86
    0x0C000120: table.sym_var("s_bigbully", "S_SCRIPT", "[]", table.GLOBL), # 87

    # blargg
    0x0C000240: table.sym_var("s_blargg",   "S_SCRIPT", "[]", table.GLOBL), # 84
}

imm_E0_shp_1b = {
    0x05003708: 0x05000408,
    0x050037A0: 0x05000408,
    0x05003838: 0x05000408,
    0x05003878: 0x05000408,
    0x050058D0: 0x05004728,
    0x05005998: 0x05004728,
    0x05005A60: 0x05004728,
    0x05005B28: 0x05004728,
    0x05005D00: 0x05004728,
}

sym_E0_shp_1c = {
    0x00134D20: table.sym("_shape_1c_szpSegmentRomStart"),
    0x0013B5D0: table.sym("_shape_1c_dataSegmentRomStart"),
    0x0C000000: table.sym_var("s_1c_86", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000308: table.sym_var("s_1c_84", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000328: table.sym_var("s_1c_85", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_1d = {
    0x0013B910: table.sym("_shape_1d_szpSegmentRomStart"),
    0x00145C10: table.sym("_shape_1d_dataSegmentRomStart"),
    0x0C000000: table.sym_var("s_1d_88", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000068: table.sym_var("s_1d_86", "S_SCRIPT", "[]", table.GLOBL),
    0x0C00010C: table.sym_var("s_1d_85", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_1e = {
    0x00145E90: table.sym("_shape_1e_szpSegmentRomStart"),
    0x00151B70: table.sym("_shape_1e_dataSegmentRomStart"),
    0x05003F20: table.sym("0x05003F20"),
    0x0C000000: table.sym_var("s_1e_87", "S_SCRIPT", "[]", table.GLOBL),
    0x0C0002AC: table.sym_var("s_1e_0C0002AC", "static S_SCRIPT", "[]"),
    0x0C0005E4: table.sym_var("s_1e_89", "S_SCRIPT", "[]", table.GLOBL),
    0x0C0005A8: table.sym_var("s_1e_88", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000610: table.sym_var("s_1e_84", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000644: table.sym_var("s_1e_85", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_1f = {
    0x001521D0: table.sym("_shape_1f_szpSegmentRomStart"),
    0x001602E0: table.sym("_shape_1f_dataSegmentRomStart"),
    0x0C000000: table.sym_var("s_1f_85", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000110: table.sym_var("s_1f_86", "S_SCRIPT", "[]", table.GLOBL),
    0x0C00036C: table.sym_var("s_1f_87", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_1g = {
    0x00160670: table.sym("_shape_1g_szpSegmentRomStart"),
    0x001656E0: table.sym("_shape_1g_dataSegmentRomStart"),
    0x0C000000: table.sym_var("s_1g_84", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000104: table.sym_var("s_1g_87", "S_SCRIPT", "[]", table.GLOBL),
    0x0C00021C: table.sym_var("s_1g_85", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000348: table.sym_var("s_1g_86", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_1h = {
    0x00165A50: table.sym("_shape_1h_szpSegmentRomStart"),
    0x00166BD0: table.sym("_shape_1h_dataSegmentRomStart"),
    0x0C000000: table.sym_var("s_1h_0C000000", "S_SCRIPT", "[]"), # unused
    0x0C000018: table.sym_var("s_1h_0C000018", "S_SCRIPT", "[]"), # unused
    0x0C000030: table.sym_var("s_1h_0C000030", "S_SCRIPT", "[]"), # unused
    0x0C000048: table.sym_var("s_1h_85", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_1i = {
    0x00166C60: table.sym("_shape_1i_szpSegmentRomStart"),
    0x0016D5C0: table.sym("_shape_1i_dataSegmentRomStart"),
    0x0C000000: table.sym_var("s_1i_88", "S_SCRIPT", "[]", table.GLOBL),
    0x0C0000C0: table.sym_var("s_1i_89", "S_SCRIPT", "[]", table.GLOBL),
    0x0C0000D8: table.sym_var("s_1i_86", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000188: table.sym_var("s_1i_85", "S_SCRIPT", "[]", table.GLOBL),
    0x0C0001B4: table.sym_var("s_1i_87", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000224: table.sym_var("s_1i_84", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000274: table.sym_var("s_1i_90", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_1j = {
    0x0016D870: table.sym("_shape_1j_szpSegmentRomStart"),
    0x00180540: table.sym("_shape_1j_dataSegmentRomStart"),
    0x0C000000: table.sym_var("s_1j_84", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000098: table.sym_var("s_1j_0C000098", "static S_SCRIPT", "[]"),
    0x0C000254: table.sym_var("s_1j_0C000254", "static S_SCRIPT", "[]"),
    0x0C000410: table.sym_var("s_1j_222", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000460: table.sym_var("_0C000460", "unused static u64"),
    0x0C000468: table.sym_var("s_1j_85", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_1k = {
    0x00180BB0: table.sym("_shape_1k_szpSegmentRomStart"),
    0x00187FA0: table.sym("_shape_1k_dataSegmentRomStart"),
    0x0C000000: table.sym_var("s_1k_89", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000030: table.sym_var("s_1k_87", "S_SCRIPT", "[]", table.GLOBL),
    0x0C0001BC: table.sym_var("s_1k_84", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000290: table.sym_var("s_1k_85", "S_SCRIPT", "[]", table.GLOBL),
    0x0C000328: table.sym_var("s_1k_86", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_2a = {
    0x00188440: table.sym("_shape_2a_szpSegmentRomStart"),
    0x001B9070: table.sym("_shape_2a_dataSegmentRomStart"),
    0x0D000000: table.sym_var("s_2a_103", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000090: table.sym_var("s_2a_104", "S_SCRIPT", "[]", table.GLOBL),
    0x0D0000B0: table.sym_var("s_2a_3", "S_SCRIPT", "[]", table.GLOBL), # local
    0x0D0000D8: table.sym_var("s_2a_0D0000D8", "static S_SCRIPT", "[]"),
    0x0D000424: table.sym_var("s_2a_0D000424", "static S_SCRIPT", "[]"),
    0x0D000770: table.sym_var("s_2a_0D000770", "static S_SCRIPT", "[]"),
    0x0D000AB8: table.sym_var("s_2a_0D000AB8", "static S_SCRIPT", "[]"),
    0x0D000AC4: table.sym_var("s_2a_100", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000B40: table.sym_var("s_2a_105", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000BBC: table.sym_var("s_2a_101_179", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000BFC: table.sym_var("s_2a_102", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_2b = {
    0x001B9CC0: table.sym("_shape_2b_szpSegmentRomStart"),
    0x001C3DB0: table.sym("_shape_2b_dataSegmentRomStart"),
    0x0D000000: table.sym_var("s_2b_105", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000284: table.sym_var("s_2b_193", "S_SCRIPT", "[]", table.GLOBL),
    0x0D0002F4: table.sym_var("s_2b_179", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000324: table.sym_var("s_2b_103", "S_SCRIPT", "[]", table.GLOBL),
    0x0D00038C: table.sym_var("s_2b_100", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000414: table.sym_var("s_2b_104", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000450: table.sym_var("s_2b_101", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000468: table.sym_var("s_2b_102", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_2c = {
    0x001C4230: table.sym("_shape_2c_szpSegmentRomStart"),
    0x001D7C90: table.sym("_shape_2c_dataSegmentRomStart"),
    0x0D000000: table.sym_var("s_2c_106", "S_SCRIPT", "[]", table.GLOBL),
    0x0D0000B8: table.sym_var("s_2c_107", "S_SCRIPT", "[]", table.GLOBL),
    0x0D0000D0: table.sym_var("s_2c_191", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000214: table.sym_var("s_2c_104", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000358: table.sym_var("s_2c_100", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000480: table.sym_var("s_2c_103", "S_SCRIPT", "[]", table.GLOBL),
    0x0D0005D0: table.sym_var("s_2c_101", "S_SCRIPT", "[]", table.GLOBL),
    0x0D0005EC: table.sym_var("s_2c_102", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_2d = {
    0x001D8310: table.sym("_shape_2d_szpSegmentRomStart"),
    0x001E4BF0: table.sym("_shape_2d_dataSegmentRomStart"),
    0x0D000000: table.sym_var("s_2d_102", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000114: table.sym_var("s_2d_0D000114", "static S_SCRIPT", "[]"),
    0x0D00027C: table.sym_var("s_2d_0D00027C", "static S_SCRIPT", "[]"),
    0x0D0003E4: table.sym_var("s_2d_221", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000440: table.sym_var("_0D000440", "unused static u64"),
    0x0D000448: table.sym_var("s_2d_100", "S_SCRIPT", "[]", table.GLOBL),
    0x0D0005A8: table.sym_var("_0D0005A8", "unused static u64"),
    0x0D0005B0: table.sym_var("s_2d_101", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_2e = {
    0x001E51F0: table.sym("_shape_2e_szpSegmentRomStart"),
    0x001E7D90: table.sym("_shape_2e_dataSegmentRomStart"),
    0x0D000000: table.sym_var("s_2e_0D000000", "static S_SCRIPT", "[]"),
    0x0D000078: table.sym_var("s_2e_0D000078", "static S_SCRIPT", "[]"),
    0x0D0000F0: table.sym_var("s_2e_102", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_2f = {
    0x001E7EE0: table.sym("_shape_2f_szpSegmentRomStart"),
    0x001F1B30: table.sym("_shape_2f_dataSegmentRomStart"),
    0x0D000000: table.sym_var("s_2f_103", "S_SCRIPT", "[]", table.GLOBL),
    0x0D00001C: table.sym_var("s_2f_102", "S_SCRIPT", "[]", table.GLOBL),
    0x0D0000DC: table.sym_var("s_2f_100", "S_SCRIPT", "[]", table.GLOBL),
    0x0D0001A0: table.sym_var("s_2f_206", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000230: table.sym_var("s_2f_104", "S_SCRIPT", "[]", table.GLOBL),
    0x0D000394: table.sym_var("s_2f_101", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_shp_3a = {
    0x001F2200: table.sym("_shape_3common_szpSegmentRomStart"),
    0x002008D0: table.sym("_shape_3common_dataSegmentRomStart"),
    0x0F000000: table.sym_var("s_3a_140", "S_SCRIPT", "[]", table.GLOBL),
    0x0F000020: table.sym_var("_0F000020", "unused static u64"),
    0x0F000028: table.sym_var("s_3a_194", "S_SCRIPT", "[]", table.GLOBL),
    0x0F0001A0: table.sym_var("_0F0001A0", "unused static u64"),
    0x0F0001A8: table.sym_var("s_3a_128", "S_SCRIPT", "[]", table.GLOBL),
    0x0F0001C0: table.sym_var("s_3a_127", "S_SCRIPT", "[]", table.GLOBL),
    0x0F0001D8: table.sym_var("s_3a_223", "S_SCRIPT", "[]", table.GLOBL),
    0x0F0004CC: table.sym_var("s_3a_207", "S_SCRIPT", "[]", table.GLOBL),
    0x0F0004E4: table.sym_var("s_3a_202", "S_SCRIPT", "[]", table.GLOBL),
    0x0F0004FC: table.sym_var("s_3a_120", "S_SCRIPT", "[]", table.GLOBL),
    0x0F000518: table.sym_var("s_3a_220", "S_SCRIPT", "[]", table.GLOBL),
    0x0F0005D0: table.sym_var("s_3a_129", "S_SCRIPT", "[]", table.GLOBL),
    0x0F000610: table.sym_var("s_3a_130", "S_SCRIPT", "[]", table.GLOBL),
    0x0F000640: table.sym_var("s_3a_180", "S_SCRIPT", "[]", table.GLOBL),
    0x0F00066C: table.sym_var("s_3a_225", "S_SCRIPT", "[]", table.GLOBL),
    0x0F000694: table.sym_var("s_3a_137", "S_SCRIPT", "[]", table.GLOBL),
    0x0F0006E4: table.sym_var("s_3a_192", "S_SCRIPT", "[]", table.GLOBL),
    0x0F0007B8: table.sym_var("s_3a_188", "S_SCRIPT", "[]", table.GLOBL),
    0x0F0008F4: table.sym_var("s_3a_195", "S_SCRIPT", "[]", table.GLOBL),
    0x0F000A30: table.sym_var("s_3a_217", "S_SCRIPT", "[]", table.GLOBL),
    0x0F000A58: table.sym_var("s_3a_131", "S_SCRIPT", "[]", table.GLOBL),
    0x0F000AB0: table.sym_var("s_3a_190", "S_SCRIPT", "[]", table.GLOBL),
    0x0F000ADC: table.sym_var("s_3a_0F000ADC", "S_SCRIPT", "[]"), # unused
    0x0F000B08: table.sym_var("s_3a_0F000B08", "S_SCRIPT", "[]"), # unused
}

sym_E0_shp_gl = {
    0x00201410: table.sym("_shape_global_szpSegmentRomStart"),
    0x00218DA0: table.sym("_shape_global_dataSegmentRomStart"),

    # puff
    0x03000080: table.sym_var("txt_puff",       "static u16", "[]"),
    0x03000880: table.sym_var("gfx_whitepuff",  "Gfx", "[]"),
    0x03000920: table.sym_var("gfx_blackpuff",  "Gfx", "[]"),
    0x030009C0: table.sym_var("align_0", "unused static u64"),

    # explosion
    0x03000A08: table.sym_var("txt_explosion_0",    "static u16", "[]"),
    0x03001208: table.sym_var("txt_explosion_1",    "static u16", "[]"),
    0x03001A08: table.sym_var("txt_explosion_2",    "static u16", "[]"),
    0x03002208: table.sym_var("txt_explosion_3",    "static u16", "[]"),
    0x03002A08: table.sym_var("txt_explosion_4",    "static u16", "[]"),
    0x03003208: table.sym_var("txt_explosion_5",    "static u16", "[]"),
    0x03003A08: table.sym_var("txt_explosion_6",    "static u16", "[]"),
    0x03004208: table.sym_var("gfx_explosion",      "static Gfx", "[]"),
    0x03004298: table.sym_var("gfx_explosion_0",    "Gfx", "[]"),
    0x030042B0: table.sym_var("gfx_explosion_1",    "Gfx", "[]"),
    0x030042C8: table.sym_var("gfx_explosion_2",    "Gfx", "[]"),
    0x030042E0: table.sym_var("gfx_explosion_3",    "Gfx", "[]"),
    0x030042F8: table.sym_var("gfx_explosion_4",    "Gfx", "[]"),
    0x03004310: table.sym_var("gfx_explosion_5",    "Gfx", "[]"),
    0x03004328: table.sym_var("gfx_explosion_6",    "Gfx", "[]"),
    0x03004340: table.sym_var("align_1", "unused static u64"),

    # butterfly
    0x030043A8: table.sym_var("txt_butterfly_wing", "static u16", "[]"),
    0x03005408: table.sym_var("gfx_butterfly_l",    "Gfx", "[]"),
    0x030054A0: table.sym_var("gfx_butterfly_r",    "Gfx", "[]"),
    0x030055B0: table.sym_var("anime_butterfly_0",  "static ANIME"),
    0x03005698: table.sym_var("anime_butterfly_1",  "static ANIME"),
    0x030056B0: table.sym_var("anime_butterfly",    "ANIME *",  "[]"),
    0x030056B8: table.sym_var("align_2", "unused static u64"),

    # coin
    0x030056C0: table.sym_var("vtx_coin_yellow",    "static Vtx", "[]"),
    0x03005700: table.sym_var("vtx_coin_blue",      "static Vtx", "[]"),
    0x03005740: table.sym_var("vtx_coin_red",       "static Vtx", "[]"),
    0x03005780: table.sym_var("txt_coin_0",         "static u16", "[]"),
    0x03005F80: table.sym_var("txt_coin_1",         "static u16", "[]"),
    0x03006780: table.sym_var("txt_coin_2",         "static u16", "[]"),
    0x03006F80: table.sym_var("txt_coin_3",         "static u16", "[]"),
    0x03007780: table.sym_var("gfx_coin_start",     "static Gfx", "[]"),
    0x030077D0: table.sym_var("gfx_coin_end",       "static Gfx", "[]"),
    0x03007800: table.sym_var("gfx_coin_yellow_0",  "Gfx", "[]"),
    0x03007828: table.sym_var("gfx_coin_yellow_1",  "Gfx", "[]"),
    0x03007850: table.sym_var("gfx_coin_yellow_2",  "Gfx", "[]"),
    0x03007878: table.sym_var("gfx_coin_yellow_3",  "Gfx", "[]"),
    0x030078A0: table.sym_var("gfx_coin_blue_0",    "Gfx", "[]"),
    0x030078C8: table.sym_var("gfx_coin_blue_1",    "Gfx", "[]"),
    0x030078F0: table.sym_var("gfx_coin_blue_2",    "Gfx", "[]"),
    0x03007918: table.sym_var("gfx_coin_blue_3",    "Gfx", "[]"),
    0x03007940: table.sym_var("gfx_coin_red_0",     "Gfx", "[]"),
    0x03007968: table.sym_var("gfx_coin_red_1",     "Gfx", "[]"),
    0x03007990: table.sym_var("gfx_coin_red_2",     "Gfx", "[]"),
    0x030079B8: table.sym_var("gfx_coin_red_3",     "Gfx", "[]"),
    0x030079E0: table.sym_var("align_3", "unused static u64"),

    # pipe
    0x030079E8: table.sym_var("light_pipe_side",    "static Lights1"),
    0x03007E40: table.sym_var("txt_pipe_side",      "static u16", "[]"),
    0x03008E40: table.sym_var("gfx_pipe_side",      "static Gfx", "[]"),
    0x03008F98: table.sym_var("gfx_pipe_side_s",    "Gfx", "[]"),
    0x03008FF8: table.sym_var("light_pipe_top",     "static Lights1"),
    0x03009010: table.sym_var("light_pipe_bottom",  "static Lights1"),
    0x03009168: table.sym_var("txt_pipe_top",       "static u16", "[]"),
    0x03009968: table.sym_var("gfx_pipe_top",       "static Gfx", "[]"),
    0x03009A20: table.sym_var("gfx_pipe_bottom",    "static Gfx", "[]"),
    0x03009A50: table.sym_var("gfx_pipe_end_s",     "Gfx", "[]"),
    0x03009AC8: table.sym_var("map_pipe",           "MAP_DATA", "[]"),
    0x03009CD8: table.sym_var("align_4", "unused static u64"),

    # door
    0x03009CE0: table.sym_var("light_door_panel",   "static Lights1"),
    0x03009CF8: table.sym_var("light_door_knob",    "static Lights1"),
    0x03009D10: table.sym_var("txt_door_a_face",    "static u16", "[]"),
    0x0300AD10: table.sym_var("txt_door_a_side",    "static u16", "[]"),
    0x0300BD10: table.sym_var("txt_door_b_face",    "static u16", "[]"),
    0x0300CD10: table.sym_var("txt_door_b_side",    "static u16", "[]"),
    0x0300D510: table.sym_var("txt_door_d_face",    "static u16", "[]"),
    0x0300E510: table.sym_var("txt_door_d_side",    "static u16", "[]"),
    0x0300ED10: table.sym_var("txt_door_e_face",    "static u16", "[]"),
    0x0300FD10: table.sym_var("txt_door_e_side",    "static u16", "[]"),
    0x03010510: table.sym_var("txt_door_f_face",    "static u16", "[]"),
    0x03011510: table.sym_var("txt_door_f_side",    "static u16", "[]"),
    0x03011D10: table.sym_var("txt_door_star",      "static u16", "[]"),
    0x03012510: table.sym_var("txt_door_star1",     "static u16", "[]"),
    0x03012D10: table.sym_var("txt_door_star3",     "static u16", "[]"),
    0x03013510: table.sym_var("txt_door_keyhole",   "static u16", "[]"),
    0x03013C10: table.sym_var("gfx_door_a_h_panel",     "static Gfx", "[]"),
    0x03013CC8: table.sym_var("gfx_door_a_h_knob_f",    "static Gfx", "[]"),
    0x03013D78: table.sym_var("gfx_door_a_h_knob_b",    "static Gfx", "[]"),
    0x03013E28: table.sym_var("gfx_door_a_h",       "Gfx", "[]"),
    0x03013EA8: table.sym_var("gfx_door_a_h_x",     "Gfx", "[]"),
    0x03013FA0: table.sym_var("vtx_door_a_l_knob",  "static Vtx", "[]"),
    0x03014020: table.sym_var("gfx_door_a_l_panel", "static Gfx", "[]"),
    0x03014100: table.sym_var("gfx_door_a_l",       "Gfx", "[]"),
    0x03014128: table.sym_var("gfx_door_a_l_x",     "Gfx", "[]"),
    0x03014140: table.sym_var("vtx_door_star_h",    "static Vtx", "[]"),
    0x03014180: table.sym_var("vtx_door_star_l",    "static Vtx", "[]"),
    0x030141C0: table.sym_var("gfx_door_star_start",    "static Gfx", "[]"),
    0x03014218: table.sym_var("gfx_door_star_end",      "static Gfx", "[]"),
    0x03014250: table.sym_var("gfx_door_star_h",    "Gfx", "[]"),
    0x03014280: table.sym_var("gfx_door_star_l",    "Gfx", "[]"),
    0x030142B0: table.sym_var("gfx_door_star1_h",   "Gfx", "[]"),
    0x030142E0: table.sym_var("gfx_door_star1_l",   "Gfx", "[]"),
    0x03014310: table.sym_var("gfx_door_star3_h",   "Gfx", "[]"),
    0x03014340: table.sym_var("gfx_door_star3_l",   "Gfx", "[]"),
    0x03014370: table.sym_var("vtx_door_keyhole_h",     "static Vtx", "[]"),
    0x030143F0: table.sym_var("vtx_door_keyhole_l",     "static Vtx", "[]"),
    0x03014470: table.sym_var("gfx_door_keyhole_start", "static Gfx", "[]"),
    0x030144E0: table.sym_var("gfx_door_keyhole_end",   "static Gfx", "[]"),
    0x03014528: table.sym_var("gfx_door_keyhole_h",     "Gfx", "[]"),
    0x03014540: table.sym_var("gfx_door_keyhole_l",     "Gfx", "[]"),
    0x03014888: table.sym_var("gfx_door_h_knob",    "static Gfx", "[]"),
    0x030149C0: table.sym_var("gfx_door_h_side",    "static Gfx", "[]"),
    0x03014A20: table.sym_var("gfx_door_h_face",    "static Gfx", "[]"),
    0x03014A50: table.sym_var("gfx_door_h_start",   "static Gfx", "[]"),
    0x03014A80: table.sym_var("gfx_door_b_h",       "Gfx", "[]"),
    0x03014B30: table.sym_var("gfx_door_c_h",       "Gfx", "[]"),
    0x03014BE0: table.sym_var("gfx_door_d_h",       "Gfx", "[]"),
    0x03014C90: table.sym_var("gfx_door_e_h",       "Gfx", "[]"),
    0x03014D40: table.sym_var("gfx_door_f_h",       "Gfx", "[]"),
    0x03014EF0: table.sym_var("gfx_door_l_panel",   "static Gfx", "[]"),
    0x03014F30: table.sym_var("gfx_door_l_knob",    "static Gfx", "[]"),
    0x03014F68: table.sym_var("gfx_door_l_start",   "static Gfx", "[]"),
    0x03014F98: table.sym_var("gfx_door_b_l",       "Gfx", "[]"),
    0x03015008: table.sym_var("gfx_door_c_l",       "Gfx", "[]"),
    0x03015078: table.sym_var("gfx_door_d_l",       "Gfx", "[]"),
    0x030150E8: table.sym_var("gfx_door_e_l",       "Gfx", "[]"),
    0x03015158: table.sym_var("gfx_door_f_l",       "Gfx", "[]"),
    0x03015208: table.sym_var("anime_door_0",       "static ANIME"),
    0x03015220: table.sym_var("anime_door_1_val",   "static s16",   "[]"),
    0x03015404: table.sym_var("anime_door_1_tbl",   "static u16",   "[]"),
    0x03015440: table.sym_var("anime_door_1",       "static ANIME"),
    0x03015458: table.sym_var("anime_door_3",       "static ANIME"),
    0x03015470: table.sym_var("anime_door_2_val",   "static s16",   "[]"),
    0x03015654: table.sym_var("anime_door_2_tbl",   "static u16",   "[]"),
    0x03015690: table.sym_var("anime_door_2",       "static ANIME"),
    0x030156A8: table.sym_var("anime_door_4",       "static ANIME"),
    0x030156C0: table.sym_var("anime_door",         "ANIME *",  "[]"),
    0x030156D8: table.sym_var("align_5", "unused static u64"),

    # doorkey
    0x030156E0: table.sym_var("light_doorkey",    "static Lights1"),
    0x030161F8: table.sym_var("gfx_doorkey",      "Gfx", "[]"),
    0x03016BE8: table.sym_var("anime_doorkey_1",  "static ANIME"),
    0x030172B8: table.sym_var("anime_doorkey_0",  "static ANIME"),
    0x030172D0: table.sym_var("anime_doorkey",    "ANIME *",  "[]"),
    0x030172D8: table.sym_var("align_6", "unused static u64"),

    # flame
    0x03017320: table.sym_var("txt_flame_0",    "static u16", "[]"),
    0x03017B20: table.sym_var("txt_flame_1",    "static u16", "[]"),
    0x03018320: table.sym_var("txt_flame_2",    "static u16", "[]"),
    0x03018B20: table.sym_var("txt_flame_3",    "static u16", "[]"),
    0x03019320: table.sym_var("txt_flame_4",    "static u16", "[]"),
    0x03019B20: table.sym_var("txt_flame_5",    "static u16", "[]"),
    0x0301A320: table.sym_var("txt_flame_6",    "static u16", "[]"),
    0x0301AB20: table.sym_var("txt_flame_7",    "static u16", "[]"),
    0x0301B320: table.sym_var("gfx_flame",      "static Gfx", "[]"),
    0x0301B3B0: table.sym_var("gfx_flame_0",    "Gfx", "[]"),
    0x0301B3C8: table.sym_var("gfx_flame_1",    "Gfx", "[]"),
    0x0301B3E0: table.sym_var("gfx_flame_2",    "Gfx", "[]"),
    0x0301B3F8: table.sym_var("gfx_flame_3",    "Gfx", "[]"),
    0x0301B410: table.sym_var("gfx_flame_4",    "Gfx", "[]"),
    0x0301B428: table.sym_var("gfx_flame_5",    "Gfx", "[]"),
    0x0301B440: table.sym_var("gfx_flame_6",    "Gfx", "[]"),
    0x0301B458: table.sym_var("gfx_flame_7",    "Gfx", "[]"),
    0x0301B470: table.sym_var("gfx_blueflame",  "static Gfx", "[]"),
    0x0301B500: table.sym_var("gfx_blueflame_0",    "Gfx", "[]"),
    0x0301B518: table.sym_var("gfx_blueflame_1",    "Gfx", "[]"),
    0x0301B530: table.sym_var("gfx_blueflame_2",    "Gfx", "[]"),
    0x0301B548: table.sym_var("gfx_blueflame_3",    "Gfx", "[]"),
    0x0301B560: table.sym_var("gfx_blueflame_4",    "Gfx", "[]"),
    0x0301B578: table.sym_var("gfx_blueflame_5",    "Gfx", "[]"),
    0x0301B590: table.sym_var("gfx_blueflame_6",    "Gfx", "[]"),
    0x0301B5A8: table.sym_var("gfx_blueflame_7",    "Gfx", "[]"),
    0x0301B5C0: table.sym_var("align_7", "unused static u64"),

    # fish
    0x0301B5C8: table.sym_var("light_fish",         "static Lights1"),
    0x0301B5E0: table.sym_var("txt_fish",           "static u16", "[]"),
    0x0301BEC0: table.sym_var("gfx_fish_body",      "static Gfx", "[]"),
    0x0301BFB8: table.sym_var("gfx_fish_body_s",    "Gfx", "[]"),
    0x0301C0A8: table.sym_var("gfx_fish_tail",      "static Gfx", "[]"),
    0x0301C150: table.sym_var("gfx_fish_tail_s",    "Gfx", "[]"),
    0x0301C298: table.sym_var("anime_fish_0",       "static ANIME"),
    0x0301C2B0: table.sym_var("anime_fish",         "ANIME *",  "[]"),
    0x0301C2B8: table.sym_var("align_8", "unused static u64"),

    # stone
    0x0301C300: table.sym_var("txt_stone",  "static u16", "[]"),
    0x0301CB00: table.sym_var("gfx_stone",  "Gfx", "[]"), # 161
    0x0301CB98: table.sym_var("align_9", "unused static u64"),

    # leaf
    0x0301CBE0: table.sym_var("txt_leaf",   "static u16", "[]"),
    0x0301CDE0: table.sym_var("gfx_leaf",   "Gfx", "[]"),
    0x0301CE70: table.sym_var("align_10", "unused static u64"),

    # map
    0x0301CE78: table.sym_var("map_door",       "MAP_DATA", "[]"),
    0x0301CECC: table.sym_var("map_13002018",   "MAP_DATA", "[]"), # this is for some platform in LLL
    0x0301CF00: table.sym_var("align_11", "unused static u64"),

    # cap
    0x0301CF08: table.sym_var("light_cap_hair",     "static Lights1"),
    0x0301CF20: table.sym_var("light_cap_white",    "static Lights1"),
    0x0301CF38: table.sym_var("light_cap_red",      "static Lights1"),
    0x0301CF50: table.sym_var("txt_cap_metal",          "static u16", "[]"),
    0x0301DF50: table.sym_var("txt_cap_logo",           "static u16", "[]"),
    0x0301E750: table.sym_var("txt_cap_wing_l",         "static u16", "[]"),
    0x0301F750: table.sym_var("txt_cap_wing_r",         "static u16", "[]"),
    0x03020750: table.sym_var("txt_cap_metal_wing_l",   "static u16", "[]"),
    0x03021750: table.sym_var("txt_cap_metal_wing_r",   "static u16", "[]"),
    0x03022B30: table.sym_var("gfx_cap0",           "static Gfx", "[]"),
    0x03022B68: table.sym_var("gfx_cap1",           "static Gfx", "[]"),
    0x03022CC8: table.sym_var("gfx_cap2",           "static Gfx", "[]"),
    0x03022D10: table.sym_var("gfx_cap12_s",        "static Gfx", "[]"),
    0x03022E78: table.sym_var("gfx_wings_l",        "static Gfx", "[]"),
    0x03022EA8: table.sym_var("gfx_wings_r",        "static Gfx", "[]"),
    0x03022ED8: table.sym_var("gfx_wings_start",    "static Gfx", "[]"),
    0x03022F20: table.sym_var("gfx_wings_end",      "static Gfx", "[]"),
    0x03022F48: table.sym_var("gfx_cap_s",          "Gfx", "[]"),
    0x03022FF8: table.sym_var("gfx_cap_e",          "Gfx", "[]"),
    0x030230B0: table.sym_var("gfx_cap_wings_s",    "Gfx", "[]"),
    0x03023108: table.sym_var("gfx_cap_wings_e",    "Gfx", "[]"),
    0x03023160: table.sym_var("gfx_wingcap_s",      "Gfx", "[]"),
    0x03023298: table.sym_var("gfx_wingcap_e",      "Gfx", "[]"),
    0x030233D0: table.sym_var("align_12", "unused static u64"),

    # meter
    0x030233D8: table.sym_var("align_meter",    "unused static u64"),
    0x030233E0: table.sym_var("txt_meter_0_l",  "static u16", "[]"),
    0x030243E0: table.sym_var("txt_meter_0_r",  "static u16", "[]"),
    0x030253E0: table.sym_var("txt_meter_8",    "static u16", "[]"),
    0x03025BE0: table.sym_var("txt_meter_7",    "static u16", "[]"),
    0x030263E0: table.sym_var("txt_meter_6",    "static u16", "[]"),
    0x03026BE0: table.sym_var("txt_meter_5",    "static u16", "[]"),
    0x030273E0: table.sym_var("txt_meter_4",    "static u16", "[]"),
    0x03027BE0: table.sym_var("txt_meter_3",    "static u16", "[]"),
    0x030283E0: table.sym_var("txt_meter_2",    "static u16", "[]"),
    0x03028BE0: table.sym_var("txt_meter_1",    "static u16", "[]"),
    0x030293E0: table.sym_var("txt_meter_n",    "u16 *", "[]"),
    0x03029400: table.sym_var("vtx_meter_0",    "static Vtx", "[]"),
    0x03029480: table.sym_var("gfx_meter_0",    "Gfx", "[]"),
    0x03029530: table.sym_var("vtx_meter_n",    "static Vtx", "[]"),
    0x03029570: table.sym_var("gfx_meter_n",    "Gfx", "[]"),
    0x030295A0: table.sym_var("gfx_meter_end",  "Gfx", "[]"),
    0x030295D8: table.sym_var("align_13", "unused static u64"),

    # number
    0x030295E0: table.sym_var("align_14", "unused static u64"),

    # 1up
    0x030295E8: table.sym_var("vtx_1up",    "static Vtx", "[]"),
    0x03029628: table.sym_var("txt_1up",    "static u16", "[]"),
    0x0302A628: table.sym_var("gfx_1up",    "static Gfx", "[]"),
    0x0302A660: table.sym_var("gfx_1up_s",  "Gfx", "[]"),
    0x0302A6D0: table.sym_var("align_15", "unused static u64"),

    # powerstar
    0x0302A6D8: table.sym_var("light_powerstar_star",   "static Lights1"),
    0x0302A6F0: table.sym_var("txt_powerstar_star",     "static u16", "[]"),
    0x0302AEF0: table.sym_var("txt_powerstar_eye",      "static u16", "[]"),
    0x0302B7B0: table.sym_var("gfx_powerstar_star",     "static Gfx", "[]"),
    0x0302B870: table.sym_var("gfx_powerstar_star_s",   "Gfx", "[]"),
    0x0302B908: table.sym_var("light_powerstar_eyes",   "static Lights1"),
    0x0302B9C0: table.sym_var("gfx_powerstar_eyes",     "static Gfx", "[]"),
    0x0302BA18: table.sym_var("gfx_powerstar_eyes_s",   "Gfx", "[]"),
    0x0302BA88: table.sym_var("align_16", "unused static u64"),

    # sand
    0x0302BAD0: table.sym_var("txt_sand",   "static u16", "[]"),
    0x0302BCD0: table.sym_var("gfx_sand",   "Gfx", "[]"), # 159
    0x0302BD60: table.sym_var("align_17", "unused static u64"),

    # shard
    0x0302BD68: table.sym_var("light_shard_r",  "static Lights1"),
    0x0302BD80: table.sym_var("light_shard_g",  "static Lights1"),
    0x0302BD98: table.sym_var("light_shard_b",  "static Lights1"),
    0x0302BDB0: table.sym_var("light_shard_y",  "static Lights1"),
    0x0302BDF8: table.sym_var("txt_shard_cork", "static u16", "[]"),
    0x0302BFF8: table.sym_var("gfx_shard_cork", "static Gfx", "[]"),
    0x0302C028: table.sym_var("gfx_shard_cork_s",   "Gfx", "[]"),
    0x0302C238: table.sym_var("gfx_star_s",     "static Gfx", "[]"),
    0x0302C298: table.sym_var("gfx_star_sr",    "Gfx", "[]"),
    0x0302C2B8: table.sym_var("gfx_star_sg",    "Gfx", "[]"),
    0x0302C2D8: table.sym_var("gfx_star_sb",    "Gfx", "[]"),
    0x0302C2F8: table.sym_var("gfx_star_sy",    "Gfx", "[]"),
    0x0302C318: table.sym_var("gfx_star_y",     "Gfx", "[]"),
    0x0302C378: table.sym_var("gfx_shard_sr",   "Gfx", "[]"),
    0x0302C3B0: table.sym_var("gfx_shard_sg",   "Gfx", "[]"),
    0x0302C3E8: table.sym_var("gfx_shard_sb",   "Gfx", "[]"),
    0x0302C420: table.sym_var("gfx_shard_sy",   "Gfx", "[]"),
    0x0302C458: table.sym_var("gfx_shard_y",    "Gfx", "[]"),
    0x0302C480: table.sym_var("align_18", "unused static u64"),

    # shadowstar
    0x0302C488: table.sym_var("light_shadowstar",   "static Lights1"),
    0x0302C560: table.sym_var("gfx_shadowstar",     "static Gfx", "[]"),
    0x0302C620: table.sym_var("gfx_shadowstar_s",   "Gfx", "[]"),
    0x0302C658: table.sym_var("align_19", "unused static u64"),

    # snow
    0x0302C6A0: table.sym_var("txt_snow",   "static u16", "[]"),
    0x0302C8A0: table.sym_var("gfx_snow",   "Gfx", "[]"), # 158
    0x0302C938: table.sym_var("align_20", "unused static u64"),

    # signpost
    0x0302C940: table.sym_var("light_signpost_post",    "static Lights1"),
    0x0302C9C8: table.sym_var("txt_signpost_wood",      "static u16", "[]"),
    0x0302D1C8: table.sym_var("txt_signpost_face",      "static u16", "[]"),
    0x0302D9C8: table.sym_var("gfx_signpost_post",      "static Gfx", "[]"),
    0x0302DA48: table.sym_var("gfx_signpost_post_s",    "Gfx", "[]"),
    0x0302DAA8: table.sym_var("light_signpost_sign",    "static Lights1"),
    0x0302DC40: table.sym_var("gfx_signpost_sign",      "static Gfx", "[]"),
    0x0302DCD0: table.sym_var("gfx_signpost_face",      "static Gfx", "[]"),
    0x0302DD08: table.sym_var("gfx_signpost_sign_s",    "Gfx", "[]"),
    0x0302DD80: table.sym_var("map_signpost",           "MAP_DATA", "[]"),
    0x0302DE08: table.sym_var("align_21", "unused static u64"),

    # tree
    0x0302DE10: table.sym_var("light_tree",     "static Lights1"),
    0x0302DE28: table.sym_var("txt_tree_a_l",   "static u16", "[]"),
    0x0302EE28: table.sym_var("txt_tree_a_r",   "static u16", "[]"),
    0x0302FE88: table.sym_var("gfx_tree_a_l",   "static Gfx", "[]"),
    0x0302FEB8: table.sym_var("gfx_tree_a_r",   "static Gfx", "[]"),
    0x0302FEE8: table.sym_var("gfx_tree_a",     "Gfx", "[]"),
    0x0302FF60: table.sym_var("txt_tree_b",     "static u16", "[]"),
    0x03030FA0: table.sym_var("gfx_tree_b",     "Gfx", "[]"),
    0x03031048: table.sym_var("txt_tree_c",     "static u16", "[]"),
    0x03032088: table.sym_var("gfx_tree_c",     "Gfx", "[]"),
    0x03032170: table.sym_var("gfx_tree_d",     "Gfx", "[]"),
    0x03032218: table.sym_var("txt_tree_e",     "static u16", "[]"),
    0x03033258: table.sym_var("gfx_tree_e",     "Gfx", "[]"),
    0x03033300: table.sym_var("align_22", "unused static u64"),

    # puff
    0x16000000: table.sym_var("s_whitepuff", "S_SCRIPT", "[]", table.GLOBL), # 142
    0x16000020: table.sym_var("s_blackpuff", "S_SCRIPT", "[]", table.GLOBL), # 224

    # explosion
    0x16000040: table.sym_var("s_explosion", "S_SCRIPT", "[]", table.GLOBL), # 205

    # butterfly
    0x160000A8: table.sym_var("s_butterfly", "S_SCRIPT", "[]", table.GLOBL), # 187

    # coin
    0x1600013C: table.sym_var("s_coin",                 "S_SCRIPT", "[]", table.GLOBL), # 116
    0x160001A0: table.sym_var("s_coin_noshadow",        "S_SCRIPT", "[]", table.GLOBL), # 117
    0x16000200: table.sym_var("s_bluecoin",             "S_SCRIPT", "[]", table.GLOBL), # 118
    0x16000264: table.sym_var("s_bluecoin_noshadow",    "S_SCRIPT", "[]", table.GLOBL), # 119
    0x160002C4: table.sym_var("s_redcoin",              "S_SCRIPT", "[]", table.GLOBL), # 215
    0x16000328: table.sym_var("s_redcoin_noshadow",     "S_SCRIPT", "[]", table.GLOBL), # 216

    # pipe
    0x16000388: table.sym_var("s_pipe", "S_SCRIPT", "[]", table.GLOBL), # 18, 22, 73, local

    # door
    0x160003A8: table.sym_var("s_door_a",           "S_SCRIPT", "[]", table.GLOBL), # 28, 38, local
    0x1600043C: table.sym_var("s_door_a_noback",    "S_SCRIPT", "[]", table.GLOBL), #     39, local
    0x160004D0: table.sym_var("s_door_b",           "S_SCRIPT", "[]", table.GLOBL), # 29, 39, local
    0x16000564: table.sym_var("s_door_c",           "S_SCRIPT", "[]", table.GLOBL), # 30, 40? unused
    0x160005F8: table.sym_var("s_door_d",           "S_SCRIPT", "[]", table.GLOBL), # 31, 41, local
    0x1600068C: table.sym_var("s_door_e",           "S_SCRIPT", "[]", table.GLOBL), # 32, local
    0x16000720: table.sym_var("s_door_f",           "S_SCRIPT", "[]", table.GLOBL), # 29, local
    0x160007B4: table.sym_var("s_stardoor",         "S_SCRIPT", "[]", table.GLOBL), # 34, local
    0x16000868: table.sym_var("s_stardoor1",        "S_SCRIPT", "[]", table.GLOBL), # 35, local
    0x1600091C: table.sym_var("s_stardoor3",        "S_SCRIPT", "[]", table.GLOBL), # 36, local
    0x160009D0: table.sym_var("s_keydoor",          "S_SCRIPT", "[]", table.GLOBL), # 37, local

    # doorkey
    0x16000A84: table.sym_var("s_bowserkey",    "S_SCRIPT", "[]", table.GLOBL), # 204
    0x16000AB0: table.sym_var("s_doorkey",      "S_SCRIPT", "[]", table.GLOBL), # 200

    # flame
    0x16000B10: table.sym_var("s_flame_shadow", "S_SCRIPT", "[]", table.GLOBL), # 203
    0x16000B2C: table.sym_var("s_flame",        "S_SCRIPT", "[]", table.GLOBL), # 144
    0x16000B8C: table.sym_var("s_blueflame",    "S_SCRIPT", "[]", table.GLOBL), # 145

    # fish
    0x16000BEC: table.sym_var("s_fish_shadow",  "S_SCRIPT", "[]", table.GLOBL), # 186
    0x16000C44: table.sym_var("s_fish",         "S_SCRIPT", "[]", table.GLOBL), # 185

    # leaf
    0x16000C8C: table.sym_var("s_leaf", "S_SCRIPT", "[]", table.GLOBL), # 162

    # cap
    0x16000CA4: table.sym_var("s_cap_s", "S_SCRIPT", "[]", table.GLOBL), # 136
    0x16000CF0: table.sym_var("s_cap_e", "S_SCRIPT", "[]", table.GLOBL), # 134
    0x16000D3C: table.sym_var("s_wingcap_s", "S_SCRIPT", "[]", table.GLOBL), # 135
    0x16000DA8: table.sym_var("s_wingcap_e", "S_SCRIPT", "[]", table.GLOBL), # 133

    # number
    0x16000E14: table.sym_var("s_number", "S_SCRIPT", "[]", table.GLOBL), # 219

    # 1up
    0x16000E84: table.sym_var("s_1up", "S_SCRIPT", "[]", table.GLOBL), # 212

    # powerstar
    0x16000EA0: table.sym_var("s_powerstar", "S_SCRIPT", "[]", table.GLOBL), # 122

    # shard
    0x16000ED4: table.sym_var("s_shard", "S_SCRIPT", "[]", table.GLOBL), # 138
    0x16000F24: table.sym_var("s_star", "S_SCRIPT", "[]", table.GLOBL), # 139

    # shadowstar
    0x16000F6C: table.sym_var("s_shadowstar", "S_SCRIPT", "[]", table.GLOBL), # 121

    # snow
    0x16000F98: table.sym_var("s_snowball", "S_SCRIPT", "[]", table.GLOBL), # 160

    # signpost
    0x16000FB4: table.sym_var("s_signpost", "S_SCRIPT", "[]", table.GLOBL), # 124

    # tree
    0x16000FE8: table.sym_var("s_tree_a", "S_SCRIPT", "[]", table.GLOBL), # 23, local
    0x16001000: table.sym_var("s_tree_b", "S_SCRIPT", "[]", table.GLOBL), # 24, local
    0x16001018: table.sym_var("s_tree_c", "S_SCRIPT", "[]", table.GLOBL), # 25, local
    0x16001030: table.sym_var("s_tree_d", "S_SCRIPT", "[]", table.GLOBL), # 26, unused
    0x16001048: table.sym_var("s_tree_e", "S_SCRIPT", "[]", table.GLOBL), # 27, local
}

imm_E0_shp_gl = {
}

sym_E0_object = {
    0x00219E00: table.sym("_object_dataSegmentRomStart"),

    # object_a.S
    0x13000000: table.sym_var("o_13000000", "O_SCRIPT", "[]", table.GLOBL),
    0x13000054: table.sym_var("o_13000054", "O_SCRIPT", "[]", table.GLOBL), # mr. i
    0x1300008C: table.sym_var("o_1300008C", "O_SCRIPT", "[]", table.GLOBL),
    0x130000AC: table.sym_var("o_130000AC", "O_SCRIPT", "[]", table.GLOBL),
    0x130000F8: table.sym_var("o_130000F8", "O_SCRIPT", "[]", table.GLOBL),
    0x13000118: table.sym_var("o_13000118", "O_SCRIPT", "[]", table.GLOBL),
    0x13000144: table.sym_var("o_13000144", "O_SCRIPT", "[]", table.GLOBL),
    0x13000174: table.sym_var("o_13000174", "O_SCRIPT", "[]", table.GLOBL),
    0x13000194: table.sym_var("o_13000194", "O_SCRIPT", "[]", table.GLOBL),
    0x130001AC: table.sym_var("o_130001AC", "O_SCRIPT", "[]", table.GLOBL),
    0x130001CC: table.sym_var("o_130001CC", "O_SCRIPT", "[]", table.GLOBL), # cap switch
    0x130001F4: table.sym_var("o_130001F4", "O_SCRIPT", "[]", table.GLOBL),
    0x13000254: table.sym_var("o_13000254", "O_SCRIPT", "[]", table.GLOBL),
    0x13000278: table.sym_var("o_13000278", "O_SCRIPT", "[]", table.GLOBL), # chest
    0x1300029C: table.sym_var("o_1300029C", "O_SCRIPT", "[]", table.GLOBL),
    0x130002B8: table.sym_var("o_130002B8", "O_SCRIPT", "[]", table.GLOBL),
    0x130002E4: table.sym_var("o_130002E4", "O_SCRIPT", "[]", table.GLOBL),
    0x13000338: table.sym_var("o_13000338", "O_SCRIPT", "[]", table.GLOBL),
    0x13000398: table.sym_var("o_13000398", "O_SCRIPT", "[]", table.GLOBL),
    0x130003BC: table.sym_var("o_130003BC", "O_SCRIPT", "[]", table.GLOBL),
    0x13000400: table.sym_var("o_13000400", "O_SCRIPT", "[]", table.GLOBL),
    0x13000428: table.sym_var("o_13000428", "O_SCRIPT", "[]", table.GLOBL),
    0x13000444: table.sym_var("o_13000444", "O_SCRIPT", "[]", table.GLOBL),
    0x1300046C: table.sym_var("o_1300046C", "O_SCRIPT", "[]", table.GLOBL),
    0x13000494: table.sym_var("o_13000494", "O_SCRIPT", "[]", table.GLOBL),
    0x130004A8: table.sym_var("o_130004A8", "O_SCRIPT", "[]", table.GLOBL), # cannon
    0x130004E4: table.sym_var("o_130004E4", "O_SCRIPT", "[]", table.GLOBL),
    0x13000528: table.sym_var("o_13000528", "O_SCRIPT", "[]", table.GLOBL), # chuckya
    0x13000584: table.sym_var("o_13000584", "O_SCRIPT", "[]", table.GLOBL),
    0x130005B4: table.sym_var("o_130005B4", "O_SCRIPT", "[]", table.GLOBL),
    0x130005D8: table.sym_var("o_130005D8", "O_SCRIPT", "[]", table.GLOBL),
    0x13000600: table.sym_var("o_13000600", "O_SCRIPT", "[]", table.GLOBL),
    0x13000624: table.sym_var("o_13000624", "O_SCRIPT", "[]", table.GLOBL),
    0x13000638: table.sym_var("o_13000638", "O_SCRIPT", "[]", table.GLOBL),
    0x1300066C: table.sym_var("o_1300066C", "O_SCRIPT", "[]", table.GLOBL),
    0x130006A4: table.sym_var("o_130006A4", "O_SCRIPT", "[]", table.GLOBL),
    0x130006D8: table.sym_var("o_130006D8", "O_SCRIPT", "[]", table.GLOBL),
    0x130006E0: table.sym_var("o_130006E0", "O_SCRIPT", "[]", table.GLOBL),
    0x13000708: table.sym_var("o_13000708", "O_SCRIPT", "[]", table.GLOBL), # water shell
    0x13000720: table.sym_var("o_13000720", "O_SCRIPT", "[]", table.GLOBL),
    0x1300075C: table.sym_var("o_1300075C", "O_SCRIPT", "[]", table.GLOBL),
    0x13000780: table.sym_var("o_13000780", "O_SCRIPT", "[]", table.GLOBL),
    0x130007A0: table.sym_var("o_130007A0", "O_SCRIPT", "[]", table.GLOBL),
    0x130007DC: table.sym_var("o_130007DC", "O_SCRIPT", "[]", table.GLOBL),
    0x130007F8: table.sym_var("o_130007F8", "O_SCRIPT", "[]", table.GLOBL),
    0x1300080C: table.sym_var("o_1300080C", "O_SCRIPT", "[]", table.GLOBL),
    0x13000830: table.sym_var("o_13000830", "O_SCRIPT", "[]", table.GLOBL),
    0x13000888: table.sym_var("o_13000888", "O_SCRIPT", "[]", table.GLOBL),
    0x130008D0: table.sym_var("o_130008D0", "O_SCRIPT", "[]", table.GLOBL),
    0x130008EC: table.sym_var("o_130008EC", "O_SCRIPT", "[]", table.GLOBL), # coin group
    0x1300090C: table.sym_var("o_1300090C", "O_SCRIPT", "[]", table.GLOBL), # alt. coin
    0x1300091C: table.sym_var("o_1300091C", "O_SCRIPT", "[]", table.GLOBL), # coin
    0x13000940: table.sym_var("o_13000940", "O_SCRIPT", "[]", table.GLOBL),
    0x13000964: table.sym_var("o_13000964", "O_SCRIPT", "[]", table.GLOBL),
    0x13000984: table.sym_var("o_13000984", "O_SCRIPT", "[]", table.GLOBL),
    0x130009A4: table.sym_var("o_130009A4", "O_SCRIPT", "[]", table.GLOBL),
    0x130009E0: table.sym_var("o_130009E0", "O_SCRIPT", "[]", table.GLOBL),
    0x13000A14: table.sym_var("o_13000A14", "O_SCRIPT", "[]", table.GLOBL),
    0x13000A34: table.sym_var("o_13000A34", "O_SCRIPT", "[]", table.GLOBL),
    0x13000A54: table.sym_var("o_13000A54", "O_SCRIPT", "[]", table.GLOBL),
    0x13000A78: table.sym_var("o_13000A78", "O_SCRIPT", "[]", table.GLOBL),
    0x13000A98: table.sym_var("o_13000A98", "O_SCRIPT", "[]", table.GLOBL),
    0x13000ABC: table.sym_var("o_13000ABC", "O_SCRIPT", "[]", table.GLOBL),
    0x13000AD8: table.sym_var("o_13000AD8", "O_SCRIPT", "[]", table.GLOBL),
    0x13000AFC: table.sym_var("o_linkdoor", "O_SCRIPT", "[]", table.GLOBL),
    0x13000B14: table.sym(".door", table.LOCAL),
    0x13000B0C: table.sym_var("o_door",     "O_SCRIPT", "[]", table.GLOBL),
    0x13000B58: table.sym_var("o_13000B58", "O_SCRIPT", "[]", table.GLOBL),
    0x13000B8C: table.sym_var("o_13000B8C", "O_SCRIPT", "[]", table.GLOBL), # thwomp
    0x13000BC8: table.sym_var("o_13000BC8", "O_SCRIPT", "[]", table.GLOBL),
    0x13000C04: table.sym_var("o_13000C04", "O_SCRIPT", "[]", table.GLOBL),
    0x13000C28: table.sym_var("o_13000C28", "O_SCRIPT", "[]", table.GLOBL),
    0x13000C44: table.sym_var("o_13000C44", "O_SCRIPT", "[]", table.GLOBL),
    0x13000C64: table.sym_var("o_13000C64", "O_SCRIPT", "[]", table.GLOBL),
    0x13000C84: table.sym_var("o_13000C84", "O_SCRIPT", "[]", table.GLOBL),
    0x13000CFC: table.sym_var("o_13000CFC", "O_SCRIPT", "[]", table.GLOBL),
    0x13000D30: table.sym_var("o_13000D30", "O_SCRIPT", "[]", table.GLOBL),
    0x13000D6C: table.sym_var("o_13000D6C", "O_SCRIPT", "[]", table.GLOBL),
    0x13000D98: table.sym_var("o_13000D98", "O_SCRIPT", "[]", table.GLOBL),
    0x13000DB4: table.sym_var("o_13000DB4", "O_SCRIPT", "[]", table.GLOBL),
    0x13000DD8: table.sym_var("o_13000DD8", "O_SCRIPT", "[]", table.GLOBL),
    0x13000E24: table.sym_var("o_13000E24", "O_SCRIPT", "[]", table.GLOBL),
    0x13000E3C: table.sym_var("o_13000E3C", "O_SCRIPT", "[]", table.GLOBL),
    0x13000E58: table.sym_var("o_13000E58", "O_SCRIPT", "[]", table.GLOBL),
    0x13000E70: table.sym_var("o_13000E70", "O_SCRIPT", "[]", table.GLOBL),
    0x13000E88: table.sym_var("o_13000E88", "O_SCRIPT", "[]", table.GLOBL),
    0x13000EAC: table.sym_var("o_13000EAC", "O_SCRIPT", "[]", table.GLOBL),
    0x13000F08: table.sym_var("o_13000F08", "O_SCRIPT", "[]", table.GLOBL),
    0x13000F14: table.sym_var("o_13000F14", "O_SCRIPT", "[]", table.GLOBL),
    0x13000F2C: table.sym_var("o_13000F2C", "O_SCRIPT", "[]", table.GLOBL),
    0x13000F48: table.sym_var("o_13000F48", "O_SCRIPT", "[]", table.GLOBL),
    0x13000F9C: table.sym_var("o_13000F9C", "O_SCRIPT", "[]", table.GLOBL),
    0x13000FC8: table.sym_var("o_13000FC8", "O_SCRIPT", "[]", table.GLOBL),
    0x13001000: table.sym_var("o_13001000", "O_SCRIPT", "[]", table.GLOBL),
    0x13001030: table.sym_var("o_13001030", "O_SCRIPT", "[]", table.GLOBL),
    0x13001064: table.sym_var("o_13001064", "O_SCRIPT", "[]", table.GLOBL),
    0x130010B8: table.sym_var("o_130010B8", "O_SCRIPT", "[]", table.GLOBL),
    0x130010D8: table.sym_var("o_130010D8", "O_SCRIPT", "[]", table.GLOBL),
    0x13001108: table.sym_var("o_13001108", "O_SCRIPT", "[]", table.GLOBL), # v flamethrower
    0x13001124: table.sym_var("o_13001124", "O_SCRIPT", "[]", table.GLOBL),
    0x13001168: table.sym_var("o_13001168", "O_SCRIPT", "[]", table.GLOBL), # jumping fire
    0x13001184: table.sym_var("o_13001184", "O_SCRIPT", "[]", table.GLOBL),
    0x130011D0: table.sym_var("o_130011D0", "O_SCRIPT", "[]", table.GLOBL),
    0x130011EC: table.sym_var("o_130011EC", "O_SCRIPT", "[]", table.GLOBL),
    0x13001214: table.sym_var("o_13001214", "O_SCRIPT", "[]", table.GLOBL),
    0x13001254: table.sym_var("o_13001254", "O_SCRIPT", "[]", table.GLOBL),
    0x1300127C: table.sym_var("o_1300127C", "O_SCRIPT", "[]", table.GLOBL),
    0x13001298: table.sym_var("o_13001298", "O_SCRIPT", "[]", table.GLOBL),
    0x130012B4: table.sym_var("o_130012B4", "O_SCRIPT", "[]", table.GLOBL), # spindrift
    0x130012F4: table.sym_var("o_130012F4", "O_SCRIPT", "[]", table.GLOBL),
    0x13001318: table.sym_var("o_13001318", "O_SCRIPT", "[]", table.GLOBL),
    0x13001340: table.sym_var("o_13001340", "O_SCRIPT", "[]", table.GLOBL),
    0x13001368: table.sym_var("o_13001368", "O_SCRIPT", "[]", table.GLOBL),
    0x13001390: table.sym_var("o_13001390", "O_SCRIPT", "[]", table.GLOBL),
    0x130013A8: table.sym_var("o_130013A8", "O_SCRIPT", "[]", table.GLOBL),
    0x130013C4: table.sym_var("o_130013C4", "O_SCRIPT", "[]", table.GLOBL),
    0x130013DC: table.sym_var("o_130013DC", "O_SCRIPT", "[]", table.GLOBL),
    0x13001408: table.sym_var("o_13001408", "O_SCRIPT", "[]", table.GLOBL),
    0x1300142C: table.sym_var("o_1300142C", "O_SCRIPT", "[]", table.GLOBL),
    0x13001448: table.sym_var("o_13001448", "O_SCRIPT", "[]", table.GLOBL),
    0x13001468: table.sym_var("o_13001468", "O_SCRIPT", "[]", table.GLOBL),
    0x13001478: table.sym_var("o_13001478", "O_SCRIPT", "[]", table.GLOBL),
    0x130014AC: table.sym_var("o_130014AC", "O_SCRIPT", "[]", table.GLOBL), # corkbox switch
    0x130014BC: table.sym_var("o_130014BC", "O_SCRIPT", "[]", table.GLOBL), # hidden corkbox
    0x130014E0: table.sym_var("o_130014E0", "O_SCRIPT", "[]", table.GLOBL), # corkbox
    0x13001518: table.sym_var("o_13001518", "O_SCRIPT", "[]", table.GLOBL), # metal box
    0x13001548: table.sym_var("o_13001548", "O_SCRIPT", "[]", table.GLOBL), # heave ho
    0x130015A4: table.sym_var("o_130015A4", "O_SCRIPT", "[]", table.GLOBL),
    0x130015C0: table.sym_var("o_130015C0", "O_SCRIPT", "[]", table.GLOBL),
    0x13001608: table.sym_var("o_13001608", "O_SCRIPT", "[]", table.GLOBL), # springboard
    0x13001634: table.sym_var("o_13001634", "O_SCRIPT", "[]", table.GLOBL),
    0x13001650: table.sym_var("o_13001650", "O_SCRIPT", "[]", table.GLOBL), # crazy box
    0x1300167C: table.sym_var("o_1300167C", "O_SCRIPT", "[]", table.GLOBL),
    0x130016B8: table.sym_var("o_130016B8", "O_SCRIPT", "[]", table.GLOBL),
    0x130016E4: table.sym_var("o_130016E4", "O_SCRIPT", "[]", table.GLOBL),
    0x13001714: table.sym_var("o_13001714", "O_SCRIPT", "[]", table.GLOBL),
    0x13001778: table.sym_var("o_13001778", "O_SCRIPT", "[]", table.GLOBL), # ghost key
    0x1300179C: table.sym_var("o_1300179C", "O_SCRIPT", "[]", table.GLOBL), # bullet bill
    0x130017F4: table.sym_var("o_130017F4", "O_SCRIPT", "[]", table.GLOBL),
    0x13001828: table.sym_var("o_13001828", "O_SCRIPT", "[]", table.GLOBL),
    0x13001850: table.sym_var("o_13001850", "O_SCRIPT", "[]", table.GLOBL), # bowser
    0x130018CC: table.sym_var("o_130018CC", "O_SCRIPT", "[]", table.GLOBL),
    0x13001904: table.sym_var("o_13001904", "O_SCRIPT", "[]", table.GLOBL),
    0x13001920: table.sym_var("o_13001920", "O_SCRIPT", "[]", table.GLOBL),
    0x13001958: table.sym_var("o_13001958", "O_SCRIPT", "[]", table.GLOBL),
    0x13001984: table.sym_var("o_13001984", "O_SCRIPT", "[]", table.GLOBL),
    0x130019C8: table.sym_var("o_130019C8", "O_SCRIPT", "[]", table.GLOBL),
    0x13001A0C: table.sym_var("o_13001A0C", "O_SCRIPT", "[]", table.GLOBL),
    0x13001A30: table.sym_var("o_13001A30", "O_SCRIPT", "[]", table.GLOBL),
    0x13001A74: table.sym_var("o_13001A74", "O_SCRIPT", "[]", table.GLOBL),
    0x13001AA4: table.sym_var("o_13001AA4", "O_SCRIPT", "[]", table.GLOBL),
    0x13001AE8: table.sym_var("o_13001AE8", "O_SCRIPT", "[]", table.GLOBL),
    0x13001B2C: table.sym_var("o_13001B2C", "O_SCRIPT", "[]", table.GLOBL),
    0x13001B54: table.sym_var("o_13001B54", "O_SCRIPT", "[]", table.GLOBL),
    0x13001B70: table.sym_var("o_13001B70", "O_SCRIPT", "[]", table.GLOBL),
    0x13001B88: table.sym_var("o_13001B88", "O_SCRIPT", "[]", table.GLOBL),
    0x13001BB4: table.sym_var("o_13001BB4", "O_SCRIPT", "[]", table.GLOBL),
    0x13001BD4: table.sym_var("o_13001BD4", "O_SCRIPT", "[]", table.GLOBL),
    0x13001BF4: table.sym_var("o_13001BF4", "O_SCRIPT", "[]", table.GLOBL),
    0x13001C04: table.sym_var("o_13001C04", "O_SCRIPT", "[]", table.GLOBL),
    0x13001C34: table.sym_var("o_13001C34", "O_SCRIPT", "[]", table.GLOBL),
    0x13001C58: table.sym_var("o_13001C58", "O_SCRIPT", "[]", table.GLOBL),
    0x13001C7C: table.sym_var("o_13001C7C", "O_SCRIPT", "[]", table.GLOBL),
    0x13001C8C: table.sym_var("o_13001C8C", "O_SCRIPT", "[]", table.GLOBL),
    0x13001CB0: table.sym_var("o_13001CB0", "O_SCRIPT", "[]", table.GLOBL), # ukkiki
    0x13001D0C: table.sym_var("o_13001D0C", "O_SCRIPT", "[]", table.GLOBL),
    0x13001D14: table.sym_var("o_13001D14", "O_SCRIPT", "[]", table.GLOBL),
    0x13001D40: table.sym_var("o_13001D40", "O_SCRIPT", "[]", table.GLOBL),
    0x13001D78: table.sym_var("o_13001D78", "O_SCRIPT", "[]", table.GLOBL),
    0x13001DA4: table.sym_var("o_13001DA4", "O_SCRIPT", "[]", table.GLOBL),
    0x13001DA8: table.sym_var("o_13001DA8", "O_SCRIPT", "[]", table.GLOBL),
    0x13001DCC: table.sym_var("o_13001DCC", "O_SCRIPT", "[]", table.GLOBL),
    0x13001E04: table.sym_var("o_13001E04", "O_SCRIPT", "[]", table.GLOBL),
    0x13001E30: table.sym_var("o_13001E30", "O_SCRIPT", "[]", table.GLOBL),
    0x13001E4C: table.sym_var("o_13001E4C", "O_SCRIPT", "[]", table.GLOBL),
    0x13001E6C: table.sym_var("o_13001E6C", "O_SCRIPT", "[]", table.GLOBL),
    0x13001E94: table.sym_var("o_13001E94", "O_SCRIPT", "[]", table.GLOBL),
    0x13001EC4: table.sym_var("o_13001EC4", "O_SCRIPT", "[]", table.GLOBL),
    0x13001EF8: table.sym_var("o_13001EF8", "O_SCRIPT", "[]", table.GLOBL),
    0x13001F3C: table.sym_var("o_13001F3C", "O_SCRIPT", "[]", table.GLOBL),
    0x13001F68: table.sym_var("o_13001F68", "O_SCRIPT", "[]", table.GLOBL),
    0x13001F90: table.sym_var("o_13001F90", "O_SCRIPT", "[]", table.GLOBL), # tox box
    0x13001FBC: table.sym_var("o_13001FBC", "O_SCRIPT", "[]", table.GLOBL), # piranha flower (chomp)
    0x13002018: table.sym_var("o_13002018", "O_SCRIPT", "[]", table.GLOBL),
    0x13002038: table.sym_var("o_13002038", "O_SCRIPT", "[]", table.GLOBL),
    0x13002068: table.sym_var("o_13002068", "O_SCRIPT", "[]", table.GLOBL),
    0x13002088: table.sym_var("o_13002088", "O_SCRIPT", "[]", table.GLOBL), # mother penguin
    0x130020D8: table.sym_var("o_130020D8", "O_SCRIPT", "[]", table.GLOBL),
    0x130020E0: table.sym_var("o_130020E0", "O_SCRIPT", "[]", table.GLOBL),
    0x130020E8: table.sym_var("o_130020E8", "O_SCRIPT", "[]", table.GLOBL), # baby penguin
    0x1300213C: table.sym_var("o_1300213C", "O_SCRIPT", "[]", table.GLOBL),
    0x1300214C: table.sym_var("o_1300214C", "O_SCRIPT", "[]", table.GLOBL),
    0x1300215C: table.sym_var("o_1300215C", "O_SCRIPT", "[]", table.GLOBL), # fish group
    0x13002178: table.sym_var("o_13002178", "O_SCRIPT", "[]", table.GLOBL),
    0x13002194: table.sym_var("o_13002194", "O_SCRIPT", "[]", table.GLOBL),
    0x130021C0: table.sym_var("o_130021C0", "O_SCRIPT", "[]", table.GLOBL),
    0x130021E4: table.sym_var("o_130021E4", "O_SCRIPT", "[]", table.GLOBL), # cheep cheep
    0x1300220C: table.sym_var("o_1300220C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002250: table.sym_var("o_13002250", "O_SCRIPT", "[]", table.GLOBL), # itembox
    0x1300227C: table.sym_var("o_1300227C", "O_SCRIPT", "[]", table.GLOBL),
    0x1300229C: table.sym_var("o_1300229C", "O_SCRIPT", "[]", table.GLOBL),
    0x130022B8: table.sym_var("o_130022B8", "O_SCRIPT", "[]", table.GLOBL),
    0x130022D8: table.sym_var("o_130022D8", "O_SCRIPT", "[]", table.GLOBL),
    0x13002308: table.sym_var("o_13002308", "O_SCRIPT", "[]", table.GLOBL),
    0x13002338: table.sym_var("o_13002338", "O_SCRIPT", "[]", table.GLOBL), # shark
    0x13002388: table.sym_var("o_13002388", "O_SCRIPT", "[]", table.GLOBL),
    0x130023A4: table.sym_var("o_130023A4", "O_SCRIPT", "[]", table.GLOBL),
    0x130023D0: table.sym_var("o_130023D0", "O_SCRIPT", "[]", table.GLOBL),
    0x130023EC: table.sym_var("o_130023EC", "O_SCRIPT", "[]", table.GLOBL),
    0x1300241C: table.sym_var("o_1300241C", "O_SCRIPT", "[]", table.GLOBL),
    0x1300243C: table.sym_var("o_1300243C", "O_SCRIPT", "[]", table.GLOBL),
    0x1300244C: table.sym_var("o_1300244C", "O_SCRIPT", "[]", table.GLOBL),
    0x1300246C: table.sym_var("o_1300246C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002480: table.sym_var("o_13002480", "O_SCRIPT", "[]", table.GLOBL),
    0x130024AC: table.sym_var("o_130024AC", "O_SCRIPT", "[]", table.GLOBL),
    0x130024DC: table.sym_var("o_130024DC", "O_SCRIPT", "[]", table.GLOBL),
    0x13002500: table.sym_var("o_13002500", "O_SCRIPT", "[]", table.GLOBL),
    0x13002528: table.sym_var("o_13002528", "O_SCRIPT", "[]", table.GLOBL),
    0x13002568: table.sym_var("o_13002568", "O_SCRIPT", "[]", table.GLOBL), # bluecoin switch
    0x13002588: table.sym_var("o_13002588", "O_SCRIPT", "[]", table.GLOBL), # hidden bluecoin
    0x130025C0: table.sym_var("o_130025C0", "O_SCRIPT", "[]", table.GLOBL),
    0x130025E0: table.sym_var("o_130025E0", "O_SCRIPT", "[]", table.GLOBL),
    0x130025F8: table.sym_var("o_130025F8", "O_SCRIPT", "[]", table.GLOBL),
    0x13002620: table.sym_var("o_13002620", "O_SCRIPT", "[]", table.GLOBL),
    0x13002634: table.sym_var("o_13002634", "O_SCRIPT", "[]", table.GLOBL),
    0x13002650: table.sym_var("o_13002650", "O_SCRIPT", "[]", table.GLOBL), # tornado
    0x13002684: table.sym_var("o_13002684", "O_SCRIPT", "[]", table.GLOBL),
    0x130026D4: table.sym_var("o_130026D4", "O_SCRIPT", "[]", table.GLOBL),
    0x13002710: table.sym_var("o_13002710", "O_SCRIPT", "[]", table.GLOBL),
    0x13002768: table.sym_var("o_13002768", "O_SCRIPT", "[]", table.GLOBL),
    0x1300277C: table.sym_var("o_1300277C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002790: table.sym_var("o_13002790", "O_SCRIPT", "[]", table.GLOBL),
    0x130027D0: table.sym_var("o_130027D0", "O_SCRIPT", "[]", table.GLOBL),
    0x130027E4: table.sym_var("o_130027E4", "O_SCRIPT", "[]", table.GLOBL),
    0x130027F4: table.sym_var("o_130027F4", "O_SCRIPT", "[]", table.GLOBL),
    0x13002804: table.sym_var("o_13002804", "O_SCRIPT", "[]", table.GLOBL), # ghost (coin)
    0x1300286C: table.sym_var("o_1300286C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002898: table.sym_var("o_13002898", "O_SCRIPT", "[]", table.GLOBL),
    0x130028CC: table.sym_var("o_130028CC", "O_SCRIPT", "[]", table.GLOBL),
    0x130028FC: table.sym_var("o_130028FC", "O_SCRIPT", "[]", table.GLOBL),
    0x1300292C: table.sym_var("o_1300292C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002968: table.sym_var("o_13002968", "O_SCRIPT", "[]", table.GLOBL),
    0x13002998: table.sym_var("o_13002998", "O_SCRIPT", "[]", table.GLOBL),
    0x130029B0: table.sym_var("o_130029B0", "O_SCRIPT", "[]", table.GLOBL),
    0x13002A20: table.sym_var("o_13002A20", "O_SCRIPT", "[]", table.GLOBL), # dummy (rotate)
    0x13002A48: table.sym_var("o_13002A48", "O_SCRIPT", "[]", table.GLOBL), # dummy
    0x13002A5C: table.sym_var("o_13002A5C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002A7C: table.sym_var("o_13002A7C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002AA4: table.sym_var("o_tree",     "O_SCRIPT", "[]", table.GLOBL),
    0x13002AD0: table.sym_var("o_13002AD0", "O_SCRIPT", "[]", table.GLOBL),
    0x13002AF0: table.sym_var("o_13002AF0", "O_SCRIPT", "[]", table.GLOBL),
    0x13002B08: table.sym_var("o_13002B08", "O_SCRIPT", "[]", table.GLOBL),
    0x13002B5C: table.sym_var("o_13002B5C", "O_SCRIPT", "[]", table.GLOBL), # scuttlebug
    0x13002BA0: table.sym_var("o_13002BA0", "O_SCRIPT", "[]", table.GLOBL), # scuttlebug (jump out)
    0x13002BB8: table.sym_var("o_13002BB8", "O_SCRIPT", "[]", table.GLOBL),
    0x13002BCC: table.sym_var("o_13002BCC", "O_SCRIPT", "[]", table.GLOBL), # whomp
    0x13002C14: table.sym_var("o_13002C14", "O_SCRIPT", "[]", table.GLOBL),
    0x13002C60: table.sym_var("o_13002C60", "O_SCRIPT", "[]", table.GLOBL),
    0x13002C7C: table.sym_var("o_13002C7C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002CB0: table.sym_var("o_13002CB0", "O_SCRIPT", "[]", table.GLOBL),
    0x13002CE0: table.sym_var("o_13002CE0", "O_SCRIPT", "[]", table.GLOBL),
    0x13002D28: table.sym_var("o_13002D28", "O_SCRIPT", "[]", table.GLOBL),
    0x13002D50: table.sym_var("o_13002D50", "O_SCRIPT", "[]", table.GLOBL),
    0x13002D7C: table.sym_var("o_13002D7C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002DB0: table.sym_var("o_13002DB0", "O_SCRIPT", "[]", table.GLOBL),
    0x13002DC0: table.sym_var("o_13002DC0", "O_SCRIPT", "[]", table.GLOBL),
    0x13002E04: table.sym_var("o_13002E04", "O_SCRIPT", "[]", table.GLOBL),
    0x13002E20: table.sym_var("o_13002E20", "O_SCRIPT", "[]", table.GLOBL),
    0x13002E3C: table.sym_var("o_13002E3C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002E58: table.sym_var("o_13002E58", "O_SCRIPT", "[]", table.GLOBL),
    0x13002EA8: table.sym_var("o_13002EA8", "O_SCRIPT", "[]", table.GLOBL),

    # player.S
    0x13002EC0: table.sym_var("o_mario", "O_SCRIPT", "[]", table.GLOBL),
    0x13002EF8: table.sym_var("o_13002EF8", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F40: table.sym_var("o_13002F40", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F60: table.sym_var("o_13002F60", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F64: table.sym_var("o_13002F64", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F68: table.sym_var("o_13002F68", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F6C: table.sym_var("o_13002F6C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F70: table.sym_var("o_13002F70", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F74: table.sym_var("o_13002F74", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F78: table.sym_var("o_13002F78", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F7C: table.sym_var("o_13002F7C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F80: table.sym_var("o_13002F80", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F84: table.sym_var("o_13002F84", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F88: table.sym_var("o_13002F88", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F8C: table.sym_var("o_13002F8C", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F90: table.sym_var("o_13002F90", "O_SCRIPT", "[]", table.GLOBL),
    0x13002F94: table.sym_var("o_13002F94", "O_SCRIPT", "[]", table.GLOBL),

    # object_b.S
    # 0x13002FA0
    0x13002FC0: table.sym_var("o_13002FC0", "O_SCRIPT", "[]", table.GLOBL),
    0x13002FE4: table.sym_var("o_13002FE4", "O_SCRIPT", "[]", table.GLOBL),
    0x13003008: table.sym_var("o_13003008", "O_SCRIPT", "[]", table.GLOBL),
    0x1300302C: table.sym_var("o_1300302C", "O_SCRIPT", "[]", table.GLOBL),
    0x13003048: table.sym_var("o_13003048", "O_SCRIPT", "[]", table.GLOBL),
    0x13003068: table.sym_var("o_13003068", "O_SCRIPT", "[]", table.GLOBL),
    0x130030A4: table.sym_var("o_130030A4", "O_SCRIPT", "[]", table.GLOBL), # bluecoin (slider)
    0x130030D4: table.sym_var("o_130030D4", "O_SCRIPT", "[]", table.GLOBL), # bluecoin (running)
    0x13003104: table.sym_var("o_13003104", "O_SCRIPT", "[]", table.GLOBL),
    0x13003134: table.sym_var("o_13003134", "O_SCRIPT", "[]", table.GLOBL),
    0x13003158: table.sym_var("o_13003158", "O_SCRIPT", "[]", table.GLOBL), # seaweed
    0x13003174: table.sym_var("o_13003174", "O_SCRIPT", "[]", table.GLOBL), # bob-omb (walk)
    0x130031AC: table.sym_var("o_130031AC", "O_SCRIPT", "[]", table.GLOBL),
    0x130031DC: table.sym_var("o_130031DC", "O_SCRIPT", "[]", table.GLOBL),
    0x13003228: table.sym_var("o_13003228", "O_SCRIPT", "[]", table.GLOBL), # bob-omb buddy
    0x13003274: table.sym_var("o_13003274", "O_SCRIPT", "[]", table.GLOBL), # bob-omb cannon
    0x130032A8: table.sym_var("o_130032A8", "O_SCRIPT", "[]", table.GLOBL),
    0x130032C8: table.sym_var("o_130032C8", "O_SCRIPT", "[]", table.GLOBL),
    0x130032E0: table.sym_var("o_signpost", "O_SCRIPT", "[]", table.GLOBL),
    0x13003324: table.sym_var("o_13003324", "O_SCRIPT", "[]", table.GLOBL), # wall sign
    0x13003354: table.sym_var("o_13003354", "O_SCRIPT", "[]", table.GLOBL), # amp (large path)
    0x13003388: table.sym_var("o_13003388", "O_SCRIPT", "[]", table.GLOBL), # amp (circular path)
    0x130033BC: table.sym_var("o_130033BC", "O_SCRIPT", "[]", table.GLOBL), # butterfly
    0x130033EC: table.sym_var("o_130033EC", "O_SCRIPT", "[]", table.GLOBL),
    0x13003454: table.sym_var("o_13003454", "O_SCRIPT", "[]", table.GLOBL),
    0x13003464: table.sym_var("o_13003464", "O_SCRIPT", "[]", table.GLOBL),
    0x1300346C: table.sym_var("o_1300346C", "O_SCRIPT", "[]", table.GLOBL),
    0x13003474: table.sym_var("o_13003474", "O_SCRIPT", "[]", table.GLOBL),
    0x13003484: table.sym_var("o_13003484", "O_SCRIPT", "[]", table.GLOBL),
    0x130034C4: table.sym_var("o_130034C4", "O_SCRIPT", "[]", table.GLOBL),
    0x13003510: table.sym_var("o_13003510", "O_SCRIPT", "[]", table.GLOBL),
    0x13003558: table.sym_var("o_13003558", "O_SCRIPT", "[]", table.GLOBL),
    0x13003588: table.sym_var("o_13003588", "O_SCRIPT", "[]", table.GLOBL),
    0x130035B0: table.sym_var("o_130035B0", "O_SCRIPT", "[]", table.GLOBL),
    0x13003600: table.sym_var("o_13003600", "O_SCRIPT", "[]", table.GLOBL),
    0x13003614: table.sym_var("o_13003614", "O_SCRIPT", "[]", table.GLOBL),
    0x1300362C: table.sym_var("o_1300362C", "O_SCRIPT", "[]", table.GLOBL), # bully
    0x13003660: table.sym_var("o_13003660", "O_SCRIPT", "[]", table.GLOBL), # big bully?
    0x13003694: table.sym_var("o_13003694", "O_SCRIPT", "[]", table.GLOBL),
    0x13003700: table.sym_var("o_13003700", "O_SCRIPT", "[]", table.GLOBL),
    0x13003738: table.sym_var("o_13003738", "O_SCRIPT", "[]", table.GLOBL), # water ring
    0x13003750: table.sym_var("o_13003750", "O_SCRIPT", "[]", table.GLOBL),
    0x13003798: table.sym_var("o_13003798", "O_SCRIPT", "[]", table.GLOBL),
    0x130037E0: table.sym_var("o_130037E0", "O_SCRIPT", "[]", table.GLOBL),
    0x130037EC: table.sym_var("o_130037EC", "O_SCRIPT", "[]", table.GLOBL), # mine
    0x1300381C: table.sym_var("o_1300381C", "O_SCRIPT", "[]", table.GLOBL),
    0x13003840: table.sym_var("o_13003840", "O_SCRIPT", "[]", table.GLOBL),
    0x13003868: table.sym_var("o_13003868", "O_SCRIPT", "[]", table.GLOBL),
    0x13003888: table.sym_var("o_13003888", "O_SCRIPT", "[]", table.GLOBL),
    0x130038B0: table.sym_var("o_130038B0", "O_SCRIPT", "[]", table.GLOBL),
    0x130038D0: table.sym_var("o_130038D0", "O_SCRIPT", "[]", table.GLOBL),
    0x130038E8: table.sym_var("o_130038E8", "O_SCRIPT", "[]", table.GLOBL),
    0x13003910: table.sym_var("o_13003910", "O_SCRIPT", "[]", table.GLOBL),
    0x13003940: table.sym_var("o_13003940", "O_SCRIPT", "[]", table.GLOBL),
    0x13003970: table.sym_var("o_13003970", "O_SCRIPT", "[]", table.GLOBL),
    0x130039A0: table.sym_var("o_130039A0", "O_SCRIPT", "[]", table.GLOBL),
    0x130039D4: table.sym_var("o_130039D4", "O_SCRIPT", "[]", table.GLOBL), # moneybag
    0x13003A08: table.sym_var("o_13003A08", "O_SCRIPT", "[]", table.GLOBL),
    0x13003A30: table.sym_var("o_13003A30", "O_SCRIPT", "[]", table.GLOBL), # ball
    0x13003A58: table.sym_var("o_13003A58", "O_SCRIPT", "[]", table.GLOBL),
    0x13003A80: table.sym_var("o_13003A80", "O_SCRIPT", "[]", table.GLOBL),
    0x13003AA4: table.sym_var("o_13003AA4", "O_SCRIPT", "[]", table.GLOBL),
    0x13003AC8: table.sym_var("o_13003AC8", "O_SCRIPT", "[]", table.GLOBL),
    0x13003AE0: table.sym_var("o_13003AE0", "O_SCRIPT", "[]", table.GLOBL),
    0x13003B00: table.sym_var("o_13003B00", "O_SCRIPT", "[]", table.GLOBL),
    0x13003B30: table.sym_var("o_13003B30", "O_SCRIPT", "[]", table.GLOBL),
    0x13003B60: table.sym_var("o_13003B60", "O_SCRIPT", "[]", table.GLOBL),
    0x13003B98: table.sym_var("o_13003B98", "O_SCRIPT", "[]", table.GLOBL),
    0x13003BB4: table.sym_var("o_13003BB4", "O_SCRIPT", "[]", table.GLOBL),
    0x13003BEC: table.sym_var("o_13003BEC", "O_SCRIPT", "[]", table.GLOBL),
    0x13003C0C: table.sym_var("o_13003C0C", "O_SCRIPT", "[]", table.GLOBL),
    0x13003C30: table.sym_var("o_13003C30", "O_SCRIPT", "[]", table.GLOBL),
    0x13003C44: table.sym_var("o_13003C44", "O_SCRIPT", "[]", table.GLOBL),
    0x13003C58: table.sym_var("o_13003C58", "O_SCRIPT", "[]", table.GLOBL),
    0x13003C7C: table.sym_var("o_13003C7C", "O_SCRIPT", "[]", table.GLOBL),
    0x13003C90: table.sym_var("o_13003C90", "O_SCRIPT", "[]", table.GLOBL),
    0x13003CA4: table.sym_var("o_13003CA4", "O_SCRIPT", "[]", table.GLOBL),
    0x13003CB8: table.sym_var("o_13003CB8", "O_SCRIPT", "[]", table.GLOBL),
    0x13003CE4: table.sym_var("o_13003CE4", "O_SCRIPT", "[]", table.GLOBL),
    0x13003D0C: table.sym_var("o_13003D0C", "O_SCRIPT", "[]", table.GLOBL),
    0x13003D34: table.sym_var("o_13003D34", "O_SCRIPT", "[]", table.GLOBL),
    0x13003D4C: table.sym_var("o_13003D4C", "O_SCRIPT", "[]", table.GLOBL),
    0x13003D74: table.sym_var("o_13003D74", "O_SCRIPT", "[]", table.GLOBL),
    0x13003DA0: table.sym_var("o_13003DA0", "O_SCRIPT", "[]", table.GLOBL),
    0x13003DB8: table.sym_var("o_13003DB8", "O_SCRIPT", "[]", table.GLOBL),
    0x13003DD8: table.sym_var("o_13003DD8", "O_SCRIPT", "[]", table.GLOBL),
    0x13003DF8: table.sym_var("o_13003DF8", "O_SCRIPT", "[]", table.GLOBL),
    0x13003E1C: table.sym_var("o_13003E1C", "O_SCRIPT", "[]", table.GLOBL),
    0x13003E3C: table.sym_var("o_13003E3C", "O_SCRIPT", "[]", table.GLOBL),
    0x13003E64: table.sym_var("o_13003E64", "O_SCRIPT", "[]", table.GLOBL),
    0x13003E8C: table.sym_var("o_13003E8C", "O_SCRIPT", "[]", table.GLOBL),
    0x13003EAC: table.sym_var("o_redcoin",  "O_SCRIPT", "[]", table.GLOBL),
    0x13003EE4: table.sym_var("o_13003EE4", "O_SCRIPT", "[]", table.GLOBL),
    0x13003EFC: table.sym_var("o_13003EFC", "O_SCRIPT", "[]", table.GLOBL),
    0x13003F1C: table.sym_var("o_13003F1C", "O_SCRIPT", "[]", table.GLOBL), # secret
    0x13003F40: table.sym_var("o_13003F40", "O_SCRIPT", "[]", table.GLOBL),
    0x13003F78: table.sym_var("o_13003F78", "O_SCRIPT", "[]", table.GLOBL),
    0x13003FA4: table.sym_var("o_13003FA4", "O_SCRIPT", "[]", table.GLOBL),
    0x13003FDC: table.sym_var("o_13003FDC", "O_SCRIPT", "[]", table.GLOBL),
    0x13004010: table.sym_var("o_13004010", "O_SCRIPT", "[]", table.GLOBL),
    0x13004044: table.sym_var("o_13004044", "O_SCRIPT", "[]", table.GLOBL), # 1up (slider)
    0x1300407C: table.sym_var("o_1300407C", "O_SCRIPT", "[]", table.GLOBL), # 1up (still)
    0x130040B4: table.sym_var("o_130040B4", "O_SCRIPT", "[]", table.GLOBL), # 1up (jumps, then walks away)
    0x130040EC: table.sym_var("o_130040EC", "O_SCRIPT", "[]", table.GLOBL), # 1up (reveals, then walks away)
    0x13004124: table.sym_var("o_13004124", "O_SCRIPT", "[]", table.GLOBL),
    0x13004148: table.sym_var("o_13004148", "O_SCRIPT", "[]", table.GLOBL),
    0x13004180: table.sym_var("o_13004180", "O_SCRIPT", "[]", table.GLOBL),
    0x130041A4: table.sym_var("o_130041A4", "O_SCRIPT", "[]", table.GLOBL), # secret 1up (chasing)
    0x130041BC: table.sym_var("o_130041BC", "O_SCRIPT", "[]", table.GLOBL),
    0x130041F0: table.sym_var("o_130041F0", "O_SCRIPT", "[]", table.GLOBL),
    0x13004218: table.sym_var("o_13004218", "O_SCRIPT", "[]", table.GLOBL), # bridge snowman
    0x13004244: table.sym_var("o_13004244", "O_SCRIPT", "[]", table.GLOBL),
    0x13004270: table.sym_var("o_13004270", "O_SCRIPT", "[]", table.GLOBL),
    0x13004284: table.sym_var("o_13004284", "O_SCRIPT", "[]", table.GLOBL),
    0x130042B4: table.sym_var("o_130042B4", "O_SCRIPT", "[]", table.GLOBL),
    0x130042E4: table.sym_var("o_130042E4", "O_SCRIPT", "[]", table.GLOBL),
    0x13004314: table.sym_var("o_13004314", "O_SCRIPT", "[]", table.GLOBL),
    0x13004348: table.sym_var("o_13004348", "O_SCRIPT", "[]", table.GLOBL),
    0x13004370: table.sym_var("o_13004370", "O_SCRIPT", "[]", table.GLOBL),
    0x130043A0: table.sym_var("o_130043A0", "O_SCRIPT", "[]", table.GLOBL),
    0x130043C4: table.sym_var("o_130043C4", "O_SCRIPT", "[]", table.GLOBL),
    0x130043E0: table.sym_var("o_130043E0", "O_SCRIPT", "[]", table.GLOBL),
    0x1300442C: table.sym_var("o_1300442C", "O_SCRIPT", "[]", table.GLOBL),
    0x1300444C: table.sym_var("o_1300444C", "O_SCRIPT", "[]", table.GLOBL),
    0x13004470: table.sym_var("o_13004470", "O_SCRIPT", "[]", table.GLOBL),
    0x13004494: table.sym_var("o_13004494", "O_SCRIPT", "[]", table.GLOBL),
    0x130044B8: table.sym_var("o_130044B8", "O_SCRIPT", "[]", table.GLOBL),
    0x130044E0: table.sym_var("o_130044E0", "O_SCRIPT", "[]", table.GLOBL),
    0x130044FC: table.sym_var("o_130044FC", "O_SCRIPT", "[]", table.GLOBL),
    0x13004538: table.sym_var("o_13004538", "O_SCRIPT", "[]", table.GLOBL),

    # object_c.S
    0x13004580: table.sym_var("o_13004580", "O_SCRIPT", "[]", table.GLOBL), # koopa
    0x130045D0: table.sym_var("o_130045D0", "O_SCRIPT", "[]", table.GLOBL), # koopa flag
    0x130045F8: table.sym_var("o_130045F8", "O_SCRIPT", "[]", table.GLOBL),
    0x13004634: table.sym_var("o_13004634", "O_SCRIPT", "[]", table.GLOBL), # pokey
    0x13004668: table.sym_var("o_13004668", "O_SCRIPT", "[]", table.GLOBL),
    0x13004698: table.sym_var("o_13004698", "O_SCRIPT", "[]", table.GLOBL), # bat
    0x130046DC: table.sym_var("o_130046DC", "O_SCRIPT", "[]", table.GLOBL), # flyguy
    0x1300472C: table.sym_var("o_1300472C", "O_SCRIPT", "[]", table.GLOBL), # goomba
    0x13004770: table.sym_var("o_13004770", "O_SCRIPT", "[]", table.GLOBL), # goomba group
    0x1300478C: table.sym_var("o_1300478C", "O_SCRIPT", "[]", table.GLOBL), # chain chomp
    0x130047E4: table.sym_var("o_130047E4", "O_SCRIPT", "[]", table.GLOBL),
    0x1300481C: table.sym_var("o_1300481C", "O_SCRIPT", "[]", table.GLOBL), # wooden stake
    0x13004868: table.sym_var("o_13004868", "O_SCRIPT", "[]", table.GLOBL),
    0x13004898: table.sym_var("o_13004898", "O_SCRIPT", "[]", table.GLOBL), # wiggler
    0x130048E0: table.sym_var("o_130048E0", "O_SCRIPT", "[]", table.GLOBL),
    0x13004918: table.sym_var("o_13004918", "O_SCRIPT", "[]", table.GLOBL), # lakitu
    0x13004954: table.sym_var("o_13004954", "O_SCRIPT", "[]", table.GLOBL),
    0x13004988: table.sym_var("o_13004988", "O_SCRIPT", "[]", table.GLOBL),
    0x130049AC: table.sym_var("o_130049AC", "O_SCRIPT", "[]", table.GLOBL),
    0x130049C8: table.sym_var("o_130049C8", "O_SCRIPT", "[]", table.GLOBL),
    0x13004A00: table.sym_var("o_13004A00", "O_SCRIPT", "[]", table.GLOBL), # monty mole
    0x13004A58: table.sym_var("o_13004A58", "O_SCRIPT", "[]", table.GLOBL), # monty mole hole
    0x13004A78: table.sym_var("o_13004A78", "O_SCRIPT", "[]", table.GLOBL),
    0x13004AB0: table.sym_var("o_13004AB0", "O_SCRIPT", "[]", table.GLOBL),
    0x13004AF4: table.sym_var("o_13004AF4", "O_SCRIPT", "[]", table.GLOBL),
    0x13004B1C: table.sym_var("o_13004B1C", "O_SCRIPT", "[]", table.GLOBL),
    0x13004B44: table.sym_var("o_13004B44", "O_SCRIPT", "[]", table.GLOBL),
    0x13004B6C: table.sym_var("o_13004B6C", "O_SCRIPT", "[]", table.GLOBL),
    0x13004B8C: table.sym_var("o_13004B8C", "O_SCRIPT", "[]", table.GLOBL), # bubble bomb
    0x13004BA8: table.sym_var("o_13004BA8", "O_SCRIPT", "[]", table.GLOBL),
    0x13004BD4: table.sym_var("o_13004BD4", "O_SCRIPT", "[]", table.GLOBL),
    0x13004BF0: table.sym_var("o_13004BF0", "O_SCRIPT", "[]", table.GLOBL),
    0x13004C24: table.sym_var("o_13004C24", "O_SCRIPT", "[]", table.GLOBL),
    0x13004C5C: table.sym_var("o_13004C5C", "O_SCRIPT", "[]", table.GLOBL),
    0x13004C94: table.sym_var("o_13004C94", "O_SCRIPT", "[]", table.GLOBL),
    0x13004CCC: table.sym_var("o_13004CCC", "O_SCRIPT", "[]", table.GLOBL),
    0x13004CF8: table.sym_var("o_13004CF8", "O_SCRIPT", "[]", table.GLOBL),
    0x13004D28: table.sym_var("o_13004D28", "O_SCRIPT", "[]", table.GLOBL),
    0x13004D64: table.sym_var("o_13004D64", "O_SCRIPT", "[]", table.GLOBL),
    0x13004D90: table.sym_var("o_13004D90", "O_SCRIPT", "[]", table.GLOBL),
    0x13004DBC: table.sym_var("o_13004DBC", "O_SCRIPT", "[]", table.GLOBL), # snowman
    0x13004E08: table.sym_var("o_13004E08", "O_SCRIPT", "[]", table.GLOBL),
    0x13004E4C: table.sym_var("o_13004E4C", "O_SCRIPT", "[]", table.GLOBL),
    0x13004E78: table.sym_var("o_13004E78", "O_SCRIPT", "[]", table.GLOBL),
    0x13004EA0: table.sym_var("o_13004EA0", "O_SCRIPT", "[]", table.GLOBL),
    0x13004ECC: table.sym_var("o_13004ECC", "O_SCRIPT", "[]", table.GLOBL),
    0x13004EF8: table.sym_var("o_13004EF8", "O_SCRIPT", "[]", table.GLOBL), # heart
    0x13004F10: table.sym_var("o_13004F10", "O_SCRIPT", "[]", table.GLOBL), # auto cannon
    0x13004F28: table.sym_var("o_13004F28", "O_SCRIPT", "[]", table.GLOBL),
    0x13004F40: table.sym_var("o_13004F40", "O_SCRIPT", "[]", table.GLOBL), # unagi
    0x13004F78: table.sym_var("o_13004F78", "O_SCRIPT", "[]", table.GLOBL),
    0x13004F90: table.sym_var("o_13004F90", "O_SCRIPT", "[]", table.GLOBL),
    0x13004FD4: table.sym_var("o_13004FD4", "O_SCRIPT", "[]", table.GLOBL), # ghost chair
    0x13005024: table.sym_var("o_13005024", "O_SCRIPT", "[]", table.GLOBL),
    0x1300506C: table.sym_var("o_1300506C", "O_SCRIPT", "[]", table.GLOBL),
    0x130050B4: table.sym_var("o_130050B4", "O_SCRIPT", "[]", table.GLOBL),
    0x130050D4: table.sym_var("o_130050D4", "O_SCRIPT", "[]", table.GLOBL),
    0x130050F4: table.sym_var("o_130050F4", "O_SCRIPT", "[]", table.GLOBL),
    0x13005120: table.sym_var("o_13005120", "O_SCRIPT", "[]", table.GLOBL), # piranha flower (fire)
    0x13005158: table.sym_var("o_13005158", "O_SCRIPT", "[]", table.GLOBL),
    0x1300518C: table.sym_var("o_1300518C", "O_SCRIPT", "[]", table.GLOBL), # fire spit
    0x130051AC: table.sym_var("o_130051AC", "O_SCRIPT", "[]", table.GLOBL),
    0x130051E0: table.sym_var("o_130051E0", "O_SCRIPT", "[]", table.GLOBL), # snufit
    0x1300521C: table.sym_var("o_1300521C", "O_SCRIPT", "[]", table.GLOBL),
    0x1300525C: table.sym_var("o_1300525C", "O_SCRIPT", "[]", table.GLOBL),
    0x130052B4: table.sym_var("o_130052B4", "O_SCRIPT", "[]", table.GLOBL),
    0x130052D0: table.sym_var("o_130052D0", "O_SCRIPT", "[]", table.GLOBL),
    0x13005310: table.sym_var("o_13005310", "O_SCRIPT", "[]", table.GLOBL),
    0x13005354: table.sym_var("o_13005354", "O_SCRIPT", "[]", table.GLOBL),
    0x13005380: table.sym_var("o_13005380", "O_SCRIPT", "[]", table.GLOBL),
    0x130053C4: table.sym_var("o_130053C4", "O_SCRIPT", "[]", table.GLOBL),
    0x130053DC: table.sym_var("o_130053DC", "O_SCRIPT", "[]", table.GLOBL),
    0x130053F4: table.sym_var("o_130053F4", "O_SCRIPT", "[]", table.GLOBL),
    0x13005414: table.sym_var("o_13005414", "O_SCRIPT", "[]", table.GLOBL),
    0x13005440: table.sym_var("o_13005440", "O_SCRIPT", "[]", table.GLOBL), # clam
    0x13005468: table.sym_var("o_13005468", "O_SCRIPT", "[]", table.GLOBL), # skeeter
    0x130054A0: table.sym_var("o_130054A0", "O_SCRIPT", "[]", table.GLOBL),
    0x130054B8: table.sym_var("o_130054B8", "O_SCRIPT", "[]", table.GLOBL),
    0x130054EC: table.sym_var("o_130054EC", "O_SCRIPT", "[]", table.GLOBL),
    0x13005504: table.sym_var("o_13005504", "O_SCRIPT", "[]", table.GLOBL),
    0x13005528: table.sym_var("o_13005528", "O_SCRIPT", "[]", table.GLOBL),
    0x1300556C: table.sym_var("o_1300556C", "O_SCRIPT", "[]", table.GLOBL),
    0x13005598: table.sym_var("o_13005598", "O_SCRIPT", "[]", table.GLOBL), # butterfly?
    0x130055DC: table.sym_var("o_130055DC", "O_SCRIPT", "[]", table.GLOBL),

    # camera.S
    0x13005610: table.sym_var("o_13005610", "O_SCRIPT", "[]", table.GLOBL),
    0x13005638: table.sym_var("o_13005638", "O_SCRIPT", "[]", table.GLOBL),
    0x1300565C: table.sym_var("o_1300565C", "O_SCRIPT", "[]", table.GLOBL),
    0x13005680: table.sym_var("o_13005680", "O_SCRIPT", "[]", table.GLOBL),
    0x130056A4: table.sym_var("o_130056A4", "O_SCRIPT", "[]", table.GLOBL),
}

sym_E0_m_title = {
    0x8016F000: table.sym("_menuSegmentStart"),
    0x00269EA0: table.sym("_menu_title_dataSegmentRomStart"),
    0x0026A3A0: table.sym("_menu_title_szpSegmentRomStart"),
    0x14000000: table.sym("p_logo", table.GLOBL),
    0x14000078: table.sym("p_title", table.GLOBL),
    0x14000104: table.sym("p_gameover", table.GLOBL),
    0x14000190: table.sym("p_debug", table.GLOBL),
    0x1400020C: table.sym("goto_file_select"),
    0x14000238: table.sym("goto_debug"),
    0x1400025C: table.sym("goto_game"),
    0x14000284: table.sym("goto_demo"),
    0x140002A8: table.sym("goto_logo"),
    0x140002D0: table.sym_var("s_logo",     "S_SCRIPT", "[]", table.GLOBL),
    0x1400035C: table.sym_var("s_title",    "S_SCRIPT", "[]", table.GLOBL),
    0x140003B8: table.sym_var("s_gameover", "S_SCRIPT", "[]", table.GLOBL),
    0x14000414: table.sym_var("s_debug",    "S_SCRIPT", "[]", table.GLOBL),
    0x07007EA0: table.sym_var("txt_logo_wood",      "static u16", "[]"),
    0x070086A0: table.sym_var("txt_logo_marble",    "static u16", "[]"),
    0x07008EA0: table.sym_var("gfx_logo_marble",    "static Gfx", "[]"),
    0x07009E38: table.sym_var("gfx_logo_wood",      "static Gfx", "[]"),
    0x0700ADC0: table.sym_var("gfx_logo_shade",     "static Gfx", "[]"),
    0x0700B3A0: table.sym_var("gfx_logo_s",         "Gfx", "[]"),
    0x0700B4A0: table.sym_var("txt_logo_copyright", "static u16", "[]"),
    0x0700C4A0: table.sym_var("txt_logo_trademark", "static u16", "[]"),
    0x0700C6A0: table.sym_var("gfx_logo_symbol",    "Gfx", "[]"),
    0x0700C790: table.sym_var("vecf_logo_a",        "vecf", "[]"),
    0x0700C880: table.sym_var("vecf_logo_b",        "vecf", "[]"),
}

sym_E0_m_debug = {
    0x0026F420: table.sym("_menu_debug_szpSegmentRomStart"),
    0x07000000: table.sym_var("light_debug_super_s",    "static Lights1"),
    0x07000858: table.sym_var("gfx_debug_super_s",      "Gfx",  "[]"),
    0x07000A28: table.sym_var("light_debug_super_u",    "static Lights1"),
    0x07001100: table.sym_var("gfx_debug_super_u",      "Gfx",  "[]"),
    0x07001288: table.sym_var("light_debug_super_p",    "static Lights1"),
    0x07001BA0: table.sym_var("gfx_debug_super_p",      "Gfx",  "[]"),
    0x07001D98: table.sym_var("light_debug_super_e",    "static Lights1"),
    0x070025F0: table.sym_var("gfx_debug_super_e",      "Gfx",  "[]"),
    0x070027C0: table.sym_var("light_debug_super_r",    "static Lights1"),
    0x07003258: table.sym_var("gfx_debug_super_r",      "Gfx",  "[]"),
    0x070034A0: table.sym_var("light_debug_mario_m",    "static Lights1"),
    0x07003DB8: table.sym_var("gfx_debug_mario_m",      "Gfx",  "[]"),
    0x07003FB0: table.sym_var("light_debug_mario_a",    "static Lights1"),
    0x070048C8: table.sym_var("gfx_debug_mario_a",      "Gfx",  "[]"),
    0x07004AC0: table.sym_var("light_debug_mario_r",    "static Lights1"),
    0x07005558: table.sym_var("gfx_debug_mario_r",      "Gfx",  "[]"),
    0x070057A0: table.sym_var("light_debug_mario_i",    "static Lights1"),
    0x070059F8: table.sym_var("gfx_debug_mario_i",      "Gfx",  "[]"),
    0x07005A98: table.sym_var("light_debug_mario_o",    "static Lights1"),
    0x070063B0: table.sym_var("gfx_debug_mario_o",      "Gfx",  "[]"),
}

imm_E0_m_debug = {
    0x07000878: 0x07000018,
    0x070008A8: 0x07000018,
    0x070008D8: 0x07000018,
    0x07000908: 0x07000018,
    0x07000938: 0x07000018,
    0x07000968: 0x07000018,
    0x07000998: 0x07000018,
    0x070009C8: 0x07000018,
    0x070009F8: 0x07000018,
    0x07001120: 0x07000A40,
    0x07001150: 0x07000A40,
    0x07001180: 0x07000A40,
    0x070011B0: 0x07000A40,
    0x070011E0: 0x07000A40,
    0x07001210: 0x07000A40,
    0x07001240: 0x07000A40,
    0x07001270: 0x07000A40,
    0x07001BC0: 0x070012A0,
    0x07001BF0: 0x070012A0,
    0x07001C20: 0x070012A0,
    0x07001C50: 0x070012A0,
    0x07001C80: 0x070012A0,
    0x07001CB0: 0x070012A0,
    0x07001CE0: 0x070012A0,
    0x07001D10: 0x070012A0,
    0x07001D40: 0x070012A0,
    0x07001D70: 0x070012A0,
    0x07002610: 0x07001DB0,
    0x07002640: 0x07001DB0,
    0x07002670: 0x07001DB0,
    0x070026A0: 0x07001DB0,
    0x070026D0: 0x07001DB0,
    0x07002700: 0x07001DB0,
    0x07002730: 0x07001DB0,
    0x07002760: 0x07001DB0,
    0x07002790: 0x07001DB0,
    0x07003278: 0x070027D8,
    0x070032A8: 0x070027D8,
    0x070032D8: 0x070027D8,
    0x07003308: 0x070027D8,
    0x07003338: 0x070027D8,
    0x07003368: 0x070027D8,
    0x07003398: 0x070027D8,
    0x070033C8: 0x070027D8,
    0x070033F8: 0x070027D8,
    0x07003428: 0x070027D8,
    0x07003458: 0x070027D8,
    0x07003488: 0x070027D8,
    0x07003DD8: 0x070034B8,
    0x07003E08: 0x070034B8,
    0x07003E38: 0x070034B8,
    0x07003E68: 0x070034B8,
    0x07003E98: 0x070034B8,
    0x07003EC8: 0x070034B8,
    0x07003EF8: 0x070034B8,
    0x07003F28: 0x070034B8,
    0x07003F58: 0x070034B8,
    0x07003F88: 0x070034B8,
    0x070048E8: 0x07003FC8,
    0x07004918: 0x07003FC8,
    0x07004948: 0x07003FC8,
    0x07004978: 0x07003FC8,
    0x070049A8: 0x07003FC8,
    0x070049D8: 0x07003FC8,
    0x07004A08: 0x07003FC8,
    0x07004A38: 0x07003FC8,
    0x07004A68: 0x07003FC8,
    0x07004A98: 0x07003FC8,
    0x07005578: 0x07004AD8,
    0x070055A8: 0x07004AD8,
    0x070055D8: 0x07004AD8,
    0x07005608: 0x07004AD8,
    0x07005638: 0x07004AD8,
    0x07005668: 0x07004AD8,
    0x07005698: 0x07004AD8,
    0x070056C8: 0x07004AD8,
    0x070056F8: 0x07004AD8,
    0x07005728: 0x07004AD8,
    0x07005758: 0x07004AD8,
    0x07005788: 0x07004AD8,
    0x07005A18: 0x070057B8,
    0x07005A48: 0x070057B8,
    0x07005A78: 0x070057B8,
    0x070063D0: 0x07005AB0,
    0x07006400: 0x07005AB0,
    0x07006430: 0x07005AB0,
    0x07006460: 0x07005AB0,
    0x07006490: 0x07005AB0,
    0x070064C0: 0x07005AB0,
    0x070064F0: 0x07005AB0,
    0x07006520: 0x07005AB0,
    0x07006550: 0x07005AB0,
    0x07006580: 0x07005AB0,
}

sym_E0_bg_title = {
    0x002708C0: table.sym("_background_title_szpSegmentRomStart"),
    0x0A000000: table.sym_var("vtx_title_bg", "static Vtx", "[]"),
    0x0A000100: table.sym_var("gfx_title_bg_start", "Gfx", "[]"),
    0x0A000118: table.sym_var("gfx_title_bg_vtx", "Gfx", "[]"),
    0x0A000130: table.sym_var("gfx_title_bg_0", "Gfx", "[]"),
    0x0A000148: table.sym_var("gfx_title_bg_1", "Gfx", "[]"),
    0x0A000160: table.sym_var("gfx_title_bg_2", "Gfx", "[]"),
    0x0A000178: table.sym_var("gfx_title_bg_3", "Gfx", "[]"),
    0x0A000190: table.sym_var("gfx_title_bg_end", "Gfx", "[]"),
    0x0A0001C0: table.sym_var("txt_title_bg_mario_0", "static u16", "[]"),
    0x0A000E40: table.sym_var("txt_title_bg_mario_1", "static u16", "[]"),
    0x0A001AC0: table.sym_var("txt_title_bg_mario_2", "static u16", "[]"),
    0x0A002740: table.sym_var("txt_title_bg_mario_3", "static u16", "[]"),
    0x0A0033C0: table.sym_var("txt_title_bg_gameover_0", "static u16", "[]"),
    0x0A004040: table.sym_var("txt_title_bg_gameover_1", "static u16", "[]"),
    0x0A004CC0: table.sym_var("txt_title_bg_gameover_2", "static u16", "[]"),
    0x0A005940: table.sym_var("txt_title_bg_gameover_3", "static u16", "[]"),
    0x0A0065C0: table.sym_var("txt_title_bg_mario", "u16 *", "[]"),
    0x0A0065D0: table.sym_var("txt_title_bg_gameover", "u16 *", "[]"),
    0x0A0065E0: table.sym_var("align_0", "unused static u64"),
}

sym_E0_d_face = {
}

sym_E0_m_select = {
    0x002A6120: table.sym("_menu_select_dataSegmentRomStart"),
    0x002A65B0: table.sym("_menu_select_szpSegmentRomStart"),
    0x0700DE30: table.sym("0x0700DE30"),
    0x14000000: table.sym("p_file_select", table.GLOBL),
    0x14000118: table.sym("p_star_select", table.GLOBL),
    0x140001C0: table.sym(".return", table.LOCAL),
    0x140001D0: table.sym_var("s_select_3", "S_SCRIPT", "[]", table.GLOBL),
    0x14000200: table.sym_var("s_select_8", "S_SCRIPT", "[]", table.GLOBL),
    0x14000230: table.sym_var("s_select_9", "S_SCRIPT", "[]", table.GLOBL),
    0x14000260: table.sym_var("s_select_10", "S_SCRIPT", "[]", table.GLOBL),
    0x14000290: table.sym_var("s_select_4", "S_SCRIPT", "[]", table.GLOBL),
    0x140002B8: table.sym_var("s_select_5", "S_SCRIPT", "[]", table.GLOBL),
    0x140002E0: table.sym_var("s_select_6", "S_SCRIPT", "[]", table.GLOBL),
    0x14000308: table.sym_var("s_select_7", "S_SCRIPT", "[]", table.GLOBL),
    0x14000330: table.sym_var("s_select_11", "S_SCRIPT", "[]", table.GLOBL),
    0x14000358: table.sym_var("s_select_12", "S_SCRIPT", "[]", table.GLOBL),
    0x14000380: table.sym_var("s_file_select", "S_SCRIPT", "[]", table.GLOBL),
    0x14000408: table.sym_var("s_star_select", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_game = {
    0x002ABCA0: table.sym("_game_dataSegmentRomStart"),
    0x15000000: table.sym("p_game", table.GLOBL),
    0x15000228: table.sym(".case_m8", table.LOCAL),
    0x15000238: table.sym(".case_m1", table.LOCAL),
    0x15000248: table.sym(".case_m2", table.LOCAL),
    0x15000258: table.sym(".case_m3", table.LOCAL),
    0x15000268: table.sym(".case_m9", table.LOCAL),
    0x15000278: table.sym("p_game_stage"),
    0x150003F4: table.sym(".case_4", table.LOCAL),
    0x15000408: table.sym(".case_5", table.LOCAL),
    0x1500041C: table.sym(".case_6", table.LOCAL),
    0x15000430: table.sym(".case_7", table.LOCAL),
    0x15000444: table.sym(".case_8", table.LOCAL),
    0x15000458: table.sym(".case_9", table.LOCAL),
    0x1500046C: table.sym(".case_10", table.LOCAL),
    0x15000480: table.sym(".case_11", table.LOCAL),
    0x15000494: table.sym(".case_12", table.LOCAL),
    0x150004A8: table.sym(".case_13", table.LOCAL),
    0x150004BC: table.sym(".case_14", table.LOCAL),
    0x150004D0: table.sym(".case_15", table.LOCAL),
    0x150004E4: table.sym(".case_16", table.LOCAL),
    0x150004F8: table.sym(".case_17", table.LOCAL),
    0x1500050C: table.sym(".case_18", table.LOCAL),
    0x15000520: table.sym(".case_19", table.LOCAL),
    0x15000534: table.sym(".case_20", table.LOCAL),
    0x15000548: table.sym(".case_21", table.LOCAL),
    0x1500055C: table.sym(".case_22", table.LOCAL),
    0x15000570: table.sym(".case_23", table.LOCAL),
    0x15000584: table.sym(".case_24", table.LOCAL),
    0x15000598: table.sym(".case_25", table.LOCAL),
    0x150005AC: table.sym(".case_26", table.LOCAL),
    0x150005C0: table.sym(".case_27", table.LOCAL),
    0x150005D4: table.sym(".case_28", table.LOCAL),
    0x150005E8: table.sym(".case_29", table.LOCAL),
    0x150005FC: table.sym(".case_30", table.LOCAL),
    0x15000610: table.sym(".case_31", table.LOCAL),
    0x15000624: table.sym(".case_33", table.LOCAL),
    0x15000638: table.sym(".case_34", table.LOCAL),
    0x1500064C: table.sym(".case_36", table.LOCAL),
    0x15000660: table.sym("p_shape_3common", table.GLOBL),
    0x1500071C: table.sym("p_shape_1a", table.GLOBL),
    0x15000750: table.sym("p_shape_1b", table.GLOBL),
    0x1500076C: table.sym("p_shape_1c", table.GLOBL),
    0x15000788: table.sym("p_shape_1d", table.GLOBL),
    0x150007B4: table.sym("p_shape_1e", table.GLOBL),
    0x150007E8: table.sym("p_shape_1f", table.GLOBL),
    0x1500080C: table.sym("p_shape_1g", table.GLOBL),
    0x15000830: table.sym("p_shape_1h", table.GLOBL),
    0x1500084C: table.sym("p_shape_1i", table.GLOBL),
    0x15000888: table.sym("p_shape_1j", table.GLOBL),
    0x150008A4: table.sym("p_shape_1k", table.GLOBL),
    0x150008D8: table.sym("p_shape_2a", table.GLOBL),
    0x15000914: table.sym("p_shape_2b", table.GLOBL),
    0x15000958: table.sym("p_shape_2c", table.GLOBL),
    0x1500099C: table.sym("p_shape_2d", table.GLOBL),
    0x150009C0: table.sym("p_shape_2e", table.GLOBL),
    0x150009DC: table.sym("p_shape_2f", table.GLOBL),
}

dev_E0_game = {
    0x15000724: 0x0012A7E0,
    0x1500072C: 0x0012A7E0,
    0x15000758: 0x00132C60,
    0x15000774: 0x00134D20,
    0x1500077C: 0x00134D20,
    0x150007A8: 0x0013B910,
    0x150007CC: 0x00145E90,
    0x150007F0: 0x001521D0,
    0x1500080C: 0x00160670,
    0x1500086C: 0x00166C60,
    0x15000888: 0x0016D870,
    0x150008F8: 0x00188440,
    0x1500094C: 0x001B9CC0,
    0x15000988: 0x001C4230,
    0x150009A4: 0x001D8310,
    0x150009AC: 0x001D8310,
}

sym_E0_bg_a = {
    0x002AC6B0: table.sym("_background_a_szpSegmentRomStart"),
    0x0A000000: table.sym_var("background_a_0", "static u16", "[]"),
    0x0A000800: table.sym_var("background_a_1", "static u16", "[]"),
    0x0A001000: table.sym_var("background_a_2", "static u16", "[]"),
    0x0A001800: table.sym_var("background_a_3", "static u16", "[]"),
    0x0A002000: table.sym_var("background_a_4", "static u16", "[]"),
    0x0A002800: table.sym_var("background_a_5", "static u16", "[]"),
    0x0A003000: table.sym_var("background_a_6", "static u16", "[]"),
    0x0A003800: table.sym_var("background_a_7", "static u16", "[]"),
    0x0A004000: table.sym_var("background_a_8", "static u16", "[]"),
    0x0A004800: table.sym_var("background_a_9", "static u16", "[]"),
    0x0A005000: table.sym_var("background_a_10", "static u16", "[]"),
    0x0A005800: table.sym_var("background_a_11", "static u16", "[]"),
    0x0A006000: table.sym_var("background_a_12", "static u16", "[]"),
    0x0A006800: table.sym_var("background_a_13", "static u16", "[]"),
    0x0A007000: table.sym_var("background_a_14", "static u16", "[]"),
    0x0A007800: table.sym_var("background_a_15", "static u16", "[]"),
    0x0A008000: table.sym_var("background_a_16", "static u16", "[]"),
    0x0A008800: table.sym_var("background_a_17", "static u16", "[]"),
    0x0A009000: table.sym_var("background_a_18", "static u16", "[]"),
    0x0A009800: table.sym_var("background_a_19", "static u16", "[]"),
    0x0A00A000: table.sym_var("background_a_20", "static u16", "[]"),
    0x0A00A800: table.sym_var("background_a_21", "static u16", "[]"),
    0x0A00B000: table.sym_var("background_a_22", "static u16", "[]"),
    0x0A00B800: table.sym_var("background_a_23", "static u16", "[]"),
    0x0A00C000: table.sym_var("background_a_24", "static u16", "[]"),
    0x0A00C800: table.sym_var("background_a_25", "static u16", "[]"),
    0x0A00D000: table.sym_var("background_a_26", "static u16", "[]"),
    0x0A00D800: table.sym_var("background_a_27", "static u16", "[]"),
    0x0A00E000: table.sym_var("background_a_28", "static u16", "[]"),
    0x0A00E800: table.sym_var("background_a_29", "static u16", "[]"),
    0x0A00F000: table.sym_var("background_a_30", "static u16", "[]"),
    0x0A00F800: table.sym_var("background_a_31", "static u16", "[]"),
    0x0A010000: table.sym_var("background_a_32", "static u16", "[]"),
    0x0A010800: table.sym_var("background_a_33", "static u16", "[]"),
    0x0A011000: table.sym_var("background_a_34", "static u16", "[]"),
    0x0A011800: table.sym_var("background_a_35", "static u16", "[]"),
    0x0A012000: table.sym_var("background_a_36", "static u16", "[]"),
    0x0A012800: table.sym_var("background_a_37", "static u16", "[]"),
    0x0A013000: table.sym_var("background_a_38", "static u16", "[]"),
    0x0A013800: table.sym_var("background_a_39", "static u16", "[]"),
    0x0A014000: table.sym_var("background_a_40", "static u16", "[]"),
    0x0A014800: table.sym_var("background_a_41", "static u16", "[]"),
    0x0A015000: table.sym_var("background_a_42", "static u16", "[]"),
    0x0A015800: table.sym_var("background_a_43", "static u16", "[]"),
    0x0A016000: table.sym_var("background_a_44", "static u16", "[]"),
    0x0A016800: table.sym_var("background_a_45", "static u16", "[]"),
    0x0A017000: table.sym_var("background_a_46", "static u16", "[]"),
    0x0A017800: table.sym_var("background_a_47", "static u16", "[]"),
    0x0A018000: table.sym_var("background_a_48", "static u16", "[]"),
    0x0A018800: table.sym_var("background_a_49", "static u16", "[]"),
    0x0A019000: table.sym_var("background_a_50", "static u16", "[]"),
    0x0A019800: table.sym_var("background_a_51", "static u16", "[]"),
    0x0A01A000: table.sym_var("background_a_52", "static u16", "[]"),
    0x0A01A800: table.sym_var("background_a_53", "static u16", "[]"),
    0x0A01B000: table.sym_var("background_a_54", "static u16", "[]"),
    0x0A01B800: table.sym_var("background_a_55", "static u16", "[]"),
    0x0A01C000: table.sym_var("background_a_56", "static u16", "[]"),
    0x0A01C800: table.sym_var("background_a_57", "static u16", "[]"),
    0x0A01D000: table.sym_var("background_a_58", "static u16", "[]"),
    0x0A01D800: table.sym_var("background_a_59", "static u16", "[]"),
    0x0A01E000: table.sym_var("background_a_60", "static u16", "[]"),
    0x0A01E800: table.sym_var("background_a_61", "static u16", "[]"),
    0x0A01F000: table.sym_var("background_a_62", "static u16", "[]"),
    0x0A01F800: table.sym_var("background_a_63", "static u16", "[]"),
    0x0A020000: table.sym_var("background_a", "u16 *", "[]", table.GLOBL),
}

sym_E0_bg_b = {
    0x002B8F10: table.sym("_background_b_szpSegmentRomStart"),
    0x0A000000: table.sym_var("background_b_0", "static u16", "[]"),
    0x0A000800: table.sym_var("background_b_1", "static u16", "[]"),
    0x0A001000: table.sym_var("background_b_2", "static u16", "[]"),
    0x0A001800: table.sym_var("background_b_3", "static u16", "[]"),
    0x0A002000: table.sym_var("background_b_4", "static u16", "[]"),
    0x0A002800: table.sym_var("background_b_5", "static u16", "[]"),
    0x0A003000: table.sym_var("background_b_6", "static u16", "[]"),
    0x0A003800: table.sym_var("background_b_7", "static u16", "[]"),
    0x0A004000: table.sym_var("background_b_8", "static u16", "[]"),
    0x0A004800: table.sym_var("background_b_9", "static u16", "[]"),
    0x0A005000: table.sym_var("background_b_10", "static u16", "[]"),
    0x0A005800: table.sym_var("background_b_11", "static u16", "[]"),
    0x0A006000: table.sym_var("background_b_12", "static u16", "[]"),
    0x0A006800: table.sym_var("background_b_13", "static u16", "[]"),
    0x0A007000: table.sym_var("background_b_14", "static u16", "[]"),
    0x0A007800: table.sym_var("background_b_15", "static u16", "[]"),
    0x0A008000: table.sym_var("background_b_16", "static u16", "[]"),
    0x0A008800: table.sym_var("background_b_17", "static u16", "[]"),
    0x0A009000: table.sym_var("background_b_18", "static u16", "[]"),
    0x0A009800: table.sym_var("background_b_19", "static u16", "[]"),
    0x0A00A000: table.sym_var("background_b_20", "static u16", "[]"),
    0x0A00A800: table.sym_var("background_b_21", "static u16", "[]"),
    0x0A00B000: table.sym_var("background_b_22", "static u16", "[]"),
    0x0A00B800: table.sym_var("background_b_23", "static u16", "[]"),
    0x0A00C000: table.sym_var("background_b_24", "static u16", "[]"),
    0x0A00C800: table.sym_var("background_b_25", "static u16", "[]"),
    0x0A00D000: table.sym_var("background_b_26", "static u16", "[]"),
    0x0A00D800: table.sym_var("background_b_27", "static u16", "[]"),
    0x0A00E000: table.sym_var("background_b_28", "static u16", "[]"),
    0x0A00E800: table.sym_var("background_b_29", "static u16", "[]"),
    0x0A00F000: table.sym_var("background_b_30", "static u16", "[]"),
    0x0A00F800: table.sym_var("background_b_31", "static u16", "[]"),
    0x0A010000: table.sym_var("background_b_32", "static u16", "[]"),
    0x0A010800: table.sym_var("background_b_33", "static u16", "[]"),
    0x0A011000: table.sym_var("background_b_34", "static u16", "[]"),
    0x0A011800: table.sym_var("background_b_35", "static u16", "[]"),
    0x0A012000: table.sym_var("background_b_36", "static u16", "[]"),
    0x0A012800: table.sym_var("background_b_37", "static u16", "[]"),
    0x0A013000: table.sym_var("background_b_38", "static u16", "[]"),
    0x0A013800: table.sym_var("background_b_39", "static u16", "[]"),
    0x0A014000: table.sym_var("background_b_40", "static u16", "[]"),
    0x0A014800: table.sym_var("background_b_41", "static u16", "[]"),
    0x0A015000: table.sym_var("background_b_42", "static u16", "[]"),
    0x0A015800: table.sym_var("background_b_43", "static u16", "[]"),
    0x0A016000: table.sym_var("background_b_44", "static u16", "[]"),
    0x0A016800: table.sym_var("background_b_45", "static u16", "[]"),
    0x0A017000: table.sym_var("background_b_46", "static u16", "[]"),
    0x0A017800: table.sym_var("background_b_47", "static u16", "[]"),
    0x0A018000: table.sym_var("background_b_48", "static u16", "[]"),
    0x0A018800: table.sym_var("background_b_49", "static u16", "[]"),
    0x0A019000: table.sym_var("background_b_50", "static u16", "[]"),
    0x0A019800: table.sym_var("background_b_51", "static u16", "[]"),
    0x0A01A000: table.sym_var("background_b_52", "static u16", "[]"),
    0x0A01A800: table.sym_var("background_b_53", "static u16", "[]"),
    0x0A01B000: table.sym_var("background_b_54", "static u16", "[]"),
    0x0A01B800: table.sym_var("background_b_55", "static u16", "[]"),
    0x0A01C000: table.sym_var("background_b_56", "static u16", "[]"),
    0x0A01C800: table.sym_var("background_b_57", "static u16", "[]"),
    0x0A01D000: table.sym_var("background_b_58", "static u16", "[]"),
    0x0A01D800: table.sym_var("background_b_59", "static u16", "[]"),
    0x0A01E000: table.sym_var("background_b_60", "static u16", "[]"),
    0x0A01E800: table.sym_var("background_b_61", "static u16", "[]"),
    0x0A01F000: table.sym_var("background_b_62", "static u16", "[]"),
    0x0A01F800: table.sym_var("background_b_63", "static u16", "[]"),
    0x0A020000: table.sym_var("background_b", "u16 *", "[]", table.GLOBL),
}

sym_E0_bg_c = {
    0x002C73D0: table.sym("_background_c_szpSegmentRomStart"),
    0x0A000000: table.sym_var("background_c_0", "static u16", "[]"),
    0x0A000800: table.sym_var("background_c_1", "static u16", "[]"),
    0x0A001000: table.sym_var("background_c_2", "static u16", "[]"),
    0x0A001800: table.sym_var("background_c_3", "static u16", "[]"),
    0x0A002000: table.sym_var("background_c_4", "static u16", "[]"),
    0x0A002800: table.sym_var("background_c_5", "static u16", "[]"),
    0x0A003000: table.sym_var("background_c_6", "static u16", "[]"),
    0x0A003800: table.sym_var("background_c_7", "static u16", "[]"),
    0x0A004000: table.sym_var("background_c_8", "static u16", "[]"),
    0x0A004800: table.sym_var("background_c_9", "static u16", "[]"),
    0x0A005000: table.sym_var("background_c_10", "static u16", "[]"),
    0x0A005800: table.sym_var("background_c_11", "static u16", "[]"),
    0x0A006000: table.sym_var("background_c_12", "static u16", "[]"),
    0x0A006800: table.sym_var("background_c_13", "static u16", "[]"),
    0x0A007000: table.sym_var("background_c_14", "static u16", "[]"),
    0x0A007800: table.sym_var("background_c_15", "static u16", "[]"),
    0x0A008000: table.sym_var("background_c_16", "static u16", "[]"),
    0x0A008800: table.sym_var("background_c_17", "static u16", "[]"),
    0x0A009000: table.sym_var("background_c_18", "static u16", "[]"),
    0x0A009800: table.sym_var("background_c_19", "static u16", "[]"),
    0x0A00A000: table.sym_var("background_c_20", "static u16", "[]"),
    0x0A00A800: table.sym_var("background_c_21", "static u16", "[]"),
    0x0A00B000: table.sym_var("background_c_22", "static u16", "[]"),
    0x0A00B800: table.sym_var("background_c_23", "static u16", "[]"),
    0x0A00C000: table.sym_var("background_c_24", "static u16", "[]"),
    0x0A00C800: table.sym_var("background_c_25", "static u16", "[]"),
    0x0A00D000: table.sym_var("background_c_26", "static u16", "[]"),
    0x0A00D800: table.sym_var("background_c_27", "static u16", "[]"),
    0x0A00E000: table.sym_var("background_c_28", "static u16", "[]"),
    0x0A00E800: table.sym_var("background_c_29", "static u16", "[]"),
    0x0A00F000: table.sym_var("background_c_30", "static u16", "[]"),
    0x0A00F800: table.sym_var("background_c_31", "static u16", "[]"),
    0x0A010000: table.sym_var("background_c_32", "static u16", "[]"),
    0x0A010800: table.sym_var("background_c_33", "static u16", "[]"),
    0x0A011000: table.sym_var("background_c_34", "static u16", "[]"),
    0x0A011800: table.sym_var("background_c_35", "static u16", "[]"),
    0x0A012000: table.sym_var("background_c_36", "static u16", "[]"),
    0x0A012800: table.sym_var("background_c_37", "static u16", "[]"),
    0x0A013000: table.sym_var("background_c_38", "static u16", "[]"),
    0x0A013800: table.sym_var("background_c_39", "static u16", "[]"),
    0x0A014000: table.sym_var("background_c_40", "static u16", "[]"),
    0x0A014800: table.sym_var("background_c", "u16 *", "[]", table.GLOBL),
}

sym_E0_bg_d = {
    0x002D0040: table.sym("_background_d_szpSegmentRomStart"),
    0x0A000000: table.sym_var("background_d_0", "static u16", "[]"),
    0x0A000800: table.sym_var("background_d_1", "static u16", "[]"),
    0x0A001000: table.sym_var("background_d_2", "static u16", "[]"),
    0x0A001800: table.sym_var("background_d_3", "static u16", "[]"),
    0x0A002000: table.sym_var("background_d_4", "static u16", "[]"),
    0x0A002800: table.sym_var("background_d_5", "static u16", "[]"),
    0x0A003000: table.sym_var("background_d_6", "static u16", "[]"),
    0x0A003800: table.sym_var("background_d_7", "static u16", "[]"),
    0x0A004000: table.sym_var("background_d_8", "static u16", "[]"),
    0x0A004800: table.sym_var("background_d_9", "static u16", "[]"),
    0x0A005000: table.sym_var("background_d_10", "static u16", "[]"),
    0x0A005800: table.sym_var("background_d_11", "static u16", "[]"),
    0x0A006000: table.sym_var("background_d_12", "static u16", "[]"),
    0x0A006800: table.sym_var("background_d_13", "static u16", "[]"),
    0x0A007000: table.sym_var("background_d_14", "static u16", "[]"),
    0x0A007800: table.sym_var("background_d_15", "static u16", "[]"),
    0x0A008000: table.sym_var("background_d_16", "static u16", "[]"),
    0x0A008800: table.sym_var("background_d_17", "static u16", "[]"),
    0x0A009000: table.sym_var("background_d_18", "static u16", "[]"),
    0x0A009800: table.sym_var("background_d_19", "static u16", "[]"),
    0x0A00A000: table.sym_var("background_d_20", "static u16", "[]"),
    0x0A00A800: table.sym_var("background_d_21", "static u16", "[]"),
    0x0A00B000: table.sym_var("background_d_22", "static u16", "[]"),
    0x0A00B800: table.sym_var("background_d_23", "static u16", "[]"),
    0x0A00C000: table.sym_var("background_d_24", "static u16", "[]"),
    0x0A00C800: table.sym_var("background_d_25", "static u16", "[]"),
    0x0A00D000: table.sym_var("background_d_26", "static u16", "[]"),
    0x0A00D800: table.sym_var("background_d_27", "static u16", "[]"),
    0x0A00E000: table.sym_var("background_d_28", "static u16", "[]"),
    0x0A00E800: table.sym_var("background_d_29", "static u16", "[]"),
    0x0A00F000: table.sym_var("background_d_30", "static u16", "[]"),
    0x0A00F800: table.sym_var("background_d_31", "static u16", "[]"),
    0x0A010000: table.sym_var("background_d_32", "static u16", "[]"),
    0x0A010800: table.sym_var("background_d_33", "static u16", "[]"),
    0x0A011000: table.sym_var("background_d_34", "static u16", "[]"),
    0x0A011800: table.sym_var("background_d_35", "static u16", "[]"),
    0x0A012000: table.sym_var("background_d_36", "static u16", "[]"),
    0x0A012800: table.sym_var("background_d_37", "static u16", "[]"),
    0x0A013000: table.sym_var("background_d_38", "static u16", "[]"),
    0x0A013800: table.sym_var("background_d_39", "static u16", "[]"),
    0x0A014000: table.sym_var("background_d_40", "static u16", "[]"),
    0x0A014800: table.sym_var("background_d_41", "static u16", "[]"),
    0x0A015000: table.sym_var("background_d_42", "static u16", "[]"),
    0x0A015800: table.sym_var("background_d_43", "static u16", "[]"),
    0x0A016000: table.sym_var("background_d_44", "static u16", "[]"),
    0x0A016800: table.sym_var("background_d_45", "static u16", "[]"),
    0x0A017000: table.sym_var("background_d_46", "static u16", "[]"),
    0x0A017800: table.sym_var("background_d_47", "static u16", "[]"),
    0x0A018000: table.sym_var("background_d_48", "static u16", "[]"),
    0x0A018800: table.sym_var("background_d", "u16 *", "[]", table.GLOBL),
}

sym_E0_bg_e = {
    0x002D64F0: table.sym("_background_e_szpSegmentRomStart"),
    0x0A000000: table.sym_var("background_e_0", "static u16", "[]"),
    0x0A000800: table.sym_var("background_e_1", "static u16", "[]"),
    0x0A001000: table.sym_var("background_e_2", "static u16", "[]"),
    0x0A001800: table.sym_var("background_e_3", "static u16", "[]"),
    0x0A002000: table.sym_var("background_e_4", "static u16", "[]"),
    0x0A002800: table.sym_var("background_e_5", "static u16", "[]"),
    0x0A003000: table.sym_var("background_e_6", "static u16", "[]"),
    0x0A003800: table.sym_var("background_e_7", "static u16", "[]"),
    0x0A004000: table.sym_var("background_e_8", "static u16", "[]"),
    0x0A004800: table.sym_var("background_e_9", "static u16", "[]"),
    0x0A005000: table.sym_var("background_e_10", "static u16", "[]"),
    0x0A005800: table.sym_var("background_e_11", "static u16", "[]"),
    0x0A006000: table.sym_var("background_e_12", "static u16", "[]"),
    0x0A006800: table.sym_var("background_e_13", "static u16", "[]"),
    0x0A007000: table.sym_var("background_e_14", "static u16", "[]"),
    0x0A007800: table.sym_var("background_e_15", "static u16", "[]"),
    0x0A008000: table.sym_var("background_e_16", "static u16", "[]"),
    0x0A008800: table.sym_var("background_e_17", "static u16", "[]"),
    0x0A009000: table.sym_var("background_e_18", "static u16", "[]"),
    0x0A009800: table.sym_var("background_e_19", "static u16", "[]"),
    0x0A00A000: table.sym_var("background_e_20", "static u16", "[]"),
    0x0A00A800: table.sym_var("background_e_21", "static u16", "[]"),
    0x0A00B000: table.sym_var("background_e_22", "static u16", "[]"),
    0x0A00B800: table.sym_var("background_e_23", "static u16", "[]"),
    0x0A00C000: table.sym_var("background_e_24", "static u16", "[]"),
    0x0A00C800: table.sym_var("background_e_25", "static u16", "[]"),
    0x0A00D000: table.sym_var("background_e_26", "static u16", "[]"),
    0x0A00D800: table.sym_var("background_e_27", "static u16", "[]"),
    0x0A00E000: table.sym_var("background_e_28", "static u16", "[]"),
    0x0A00E800: table.sym_var("background_e_29", "static u16", "[]"),
    0x0A00F000: table.sym_var("background_e_30", "static u16", "[]"),
    0x0A00F800: table.sym_var("background_e_31", "static u16", "[]"),
    0x0A010000: table.sym_var("background_e_32", "static u16", "[]"),
    0x0A010800: table.sym_var("background_e_33", "static u16", "[]"),
    0x0A011000: table.sym_var("background_e_34", "static u16", "[]"),
    0x0A011800: table.sym_var("background_e_35", "static u16", "[]"),
    0x0A012000: table.sym_var("background_e_36", "static u16", "[]"),
    0x0A012800: table.sym_var("background_e_37", "static u16", "[]"),
    0x0A013000: table.sym_var("background_e_38", "static u16", "[]"),
    0x0A013800: table.sym_var("background_e_39", "static u16", "[]"),
    0x0A014000: table.sym_var("background_e_40", "static u16", "[]"),
    0x0A014800: table.sym_var("background_e_41", "static u16", "[]"),
    0x0A015000: table.sym_var("background_e_42", "static u16", "[]"),
    0x0A015800: table.sym_var("background_e_43", "static u16", "[]"),
    0x0A016000: table.sym_var("background_e_44", "static u16", "[]"),
    0x0A016800: table.sym_var("background_e_45", "static u16", "[]"),
    0x0A017000: table.sym_var("background_e_46", "static u16", "[]"),
    0x0A017800: table.sym_var("background_e_47", "static u16", "[]"),
    0x0A018000: table.sym_var("background_e_48", "static u16", "[]"),
    0x0A018800: table.sym_var("background_e_49", "static u16", "[]"),
    0x0A019000: table.sym_var("background_e_50", "static u16", "[]"),
    0x0A019800: table.sym_var("background_e_51", "static u16", "[]"),
    0x0A01A000: table.sym_var("background_e_52", "static u16", "[]"),
    0x0A01A800: table.sym_var("background_e_53", "static u16", "[]"),
    0x0A01B000: table.sym_var("background_e_54", "static u16", "[]"),
    0x0A01B800: table.sym_var("background_e_55", "static u16", "[]"),
    0x0A01C000: table.sym_var("background_e_56", "static u16", "[]"),
    0x0A01C800: table.sym_var("background_e_57", "static u16", "[]"),
    0x0A01D000: table.sym_var("background_e_58", "static u16", "[]"),
    0x0A01D800: table.sym_var("background_e_59", "static u16", "[]"),
    0x0A01E000: table.sym_var("background_e_60", "static u16", "[]"),
    0x0A01E800: table.sym_var("background_e_61", "static u16", "[]"),
    0x0A01F000: table.sym_var("background_e_62", "static u16", "[]"),
    0x0A01F800: table.sym_var("background_e_63", "static u16", "[]"),
    0x0A020000: table.sym_var("background_e", "u16 *", "[]", table.GLOBL),
}

sym_E0_bg_f = {
    0x002E7880: table.sym("_background_f_szpSegmentRomStart"),
    0x0A000000: table.sym_var("background_f_0", "static u16", "[]"),
    0x0A000800: table.sym_var("background_f_1", "static u16", "[]"),
    0x0A001000: table.sym_var("background_f_2", "static u16", "[]"),
    0x0A001800: table.sym_var("background_f_3", "static u16", "[]"),
    0x0A002000: table.sym_var("background_f_4", "static u16", "[]"),
    0x0A002800: table.sym_var("background_f_5", "static u16", "[]"),
    0x0A003000: table.sym_var("background_f_6", "static u16", "[]"),
    0x0A003800: table.sym_var("background_f_7", "static u16", "[]"),
    0x0A004000: table.sym_var("background_f_8", "static u16", "[]"),
    0x0A004800: table.sym_var("background_f_9", "static u16", "[]"),
    0x0A005000: table.sym_var("background_f_10", "static u16", "[]"),
    0x0A005800: table.sym_var("background_f_11", "static u16", "[]"),
    0x0A006000: table.sym_var("background_f_12", "static u16", "[]"),
    0x0A006800: table.sym_var("background_f_13", "static u16", "[]"),
    0x0A007000: table.sym_var("background_f_14", "static u16", "[]"),
    0x0A007800: table.sym_var("background_f_15", "static u16", "[]"),
    0x0A008000: table.sym_var("background_f_16", "static u16", "[]"),
    0x0A008800: table.sym_var("background_f_17", "static u16", "[]"),
    0x0A009000: table.sym_var("background_f_18", "static u16", "[]"),
    0x0A009800: table.sym_var("background_f_19", "static u16", "[]"),
    0x0A00A000: table.sym_var("background_f_20", "static u16", "[]"),
    0x0A00A800: table.sym_var("background_f_21", "static u16", "[]"),
    0x0A00B000: table.sym_var("background_f_22", "static u16", "[]"),
    0x0A00B800: table.sym_var("background_f_23", "static u16", "[]"),
    0x0A00C000: table.sym_var("background_f_24", "static u16", "[]"),
    0x0A00C800: table.sym_var("background_f_25", "static u16", "[]"),
    0x0A00D000: table.sym_var("background_f_26", "static u16", "[]"),
    0x0A00D800: table.sym_var("background_f_27", "static u16", "[]"),
    0x0A00E000: table.sym_var("background_f_28", "static u16", "[]"),
    0x0A00E800: table.sym_var("background_f_29", "static u16", "[]"),
    0x0A00F000: table.sym_var("background_f_30", "static u16", "[]"),
    0x0A00F800: table.sym_var("background_f_31", "static u16", "[]"),
    0x0A010000: table.sym_var("background_f_32", "static u16", "[]"),
    0x0A010800: table.sym_var("background_f_33", "static u16", "[]"),
    0x0A011000: table.sym_var("background_f_34", "static u16", "[]"),
    0x0A011800: table.sym_var("background_f_35", "static u16", "[]"),
    0x0A012000: table.sym_var("background_f_36", "static u16", "[]"),
    0x0A012800: table.sym_var("background_f_37", "static u16", "[]"),
    0x0A013000: table.sym_var("background_f_38", "static u16", "[]"),
    0x0A013800: table.sym_var("background_f_39", "static u16", "[]"),
    0x0A014000: table.sym_var("background_f_40", "static u16", "[]"),
    0x0A014800: table.sym_var("background_f_41", "static u16", "[]"),
    0x0A015000: table.sym_var("background_f_42", "static u16", "[]"),
    0x0A015800: table.sym_var("background_f_43", "static u16", "[]"),
    0x0A016000: table.sym_var("background_f_44", "static u16", "[]"),
    0x0A016800: table.sym_var("background_f_45", "static u16", "[]"),
    0x0A017000: table.sym_var("background_f_46", "static u16", "[]"),
    0x0A017800: table.sym_var("background_f_47", "static u16", "[]"),
    0x0A018000: table.sym_var("background_f_48", "static u16", "[]"),
    0x0A018800: table.sym_var("background_f_49", "static u16", "[]"),
    0x0A019000: table.sym_var("background_f_50", "static u16", "[]"),
    0x0A019800: table.sym_var("background_f_51", "static u16", "[]"),
    0x0A01A000: table.sym_var("background_f_52", "static u16", "[]"),
    0x0A01A800: table.sym_var("background_f_53", "static u16", "[]"),
    0x0A01B000: table.sym_var("background_f_54", "static u16", "[]"),
    0x0A01B800: table.sym_var("background_f_55", "static u16", "[]"),
    0x0A01C000: table.sym_var("background_f_56", "static u16", "[]"),
    0x0A01C800: table.sym_var("background_f_57", "static u16", "[]"),
    0x0A01D000: table.sym_var("background_f_58", "static u16", "[]"),
    0x0A01D800: table.sym_var("background_f_59", "static u16", "[]"),
    0x0A01E000: table.sym_var("background_f_60", "static u16", "[]"),
    0x0A01E800: table.sym_var("background_f_61", "static u16", "[]"),
    0x0A01F000: table.sym_var("background_f_62", "static u16", "[]"),
    0x0A01F800: table.sym_var("background_f_63", "static u16", "[]"),
    0x0A020000: table.sym_var("background_f", "u16 *", "[]", table.GLOBL),
}

sym_E0_bg_g = {
    0x002F14E0: table.sym("_background_g_szpSegmentRomStart"),
    0x0A000000: table.sym_var("background_g_0", "static u16", "[]"),
    0x0A000800: table.sym_var("background_g_1", "static u16", "[]"),
    0x0A001000: table.sym_var("background_g_2", "static u16", "[]"),
    0x0A001800: table.sym_var("background_g_3", "static u16", "[]"),
    0x0A002000: table.sym_var("background_g_4", "static u16", "[]"),
    0x0A002800: table.sym_var("background_g_5", "static u16", "[]"),
    0x0A003000: table.sym_var("background_g_6", "static u16", "[]"),
    0x0A003800: table.sym_var("background_g_7", "static u16", "[]"),
    0x0A004000: table.sym_var("background_g_8", "static u16", "[]"),
    0x0A004800: table.sym_var("background_g_9", "static u16", "[]"),
    0x0A005000: table.sym_var("background_g_10", "static u16", "[]"),
    0x0A005800: table.sym_var("background_g_11", "static u16", "[]"),
    0x0A006000: table.sym_var("background_g_12", "static u16", "[]"),
    0x0A006800: table.sym_var("background_g_13", "static u16", "[]"),
    0x0A007000: table.sym_var("background_g_14", "static u16", "[]"),
    0x0A007800: table.sym_var("background_g_15", "static u16", "[]"),
    0x0A008000: table.sym_var("background_g_16", "static u16", "[]"),
    0x0A008800: table.sym_var("background_g_17", "static u16", "[]"),
    0x0A009000: table.sym_var("background_g_18", "static u16", "[]"),
    0x0A009800: table.sym_var("background_g_19", "static u16", "[]"),
    0x0A00A000: table.sym_var("background_g_20", "static u16", "[]"),
    0x0A00A800: table.sym_var("background_g_21", "static u16", "[]"),
    0x0A00B000: table.sym_var("background_g_22", "static u16", "[]"),
    0x0A00B800: table.sym_var("background_g_23", "static u16", "[]"),
    0x0A00C000: table.sym_var("background_g_24", "static u16", "[]"),
    0x0A00C800: table.sym_var("background_g_25", "static u16", "[]"),
    0x0A00D000: table.sym_var("background_g_26", "static u16", "[]"),
    0x0A00D800: table.sym_var("background_g_27", "static u16", "[]"),
    0x0A00E000: table.sym_var("background_g_28", "static u16", "[]"),
    0x0A00E800: table.sym_var("background_g_29", "static u16", "[]"),
    0x0A00F000: table.sym_var("background_g_30", "static u16", "[]"),
    0x0A00F800: table.sym_var("background_g_31", "static u16", "[]"),
    0x0A010000: table.sym_var("background_g_32", "static u16", "[]"),
    0x0A010800: table.sym_var("background_g_33", "static u16", "[]"),
    0x0A011000: table.sym_var("background_g_34", "static u16", "[]"),
    0x0A011800: table.sym_var("background_g_35", "static u16", "[]"),
    0x0A012000: table.sym_var("background_g_36", "static u16", "[]"),
    0x0A012800: table.sym_var("background_g_37", "static u16", "[]"),
    0x0A013000: table.sym_var("background_g_38", "static u16", "[]"),
    0x0A013800: table.sym_var("background_g_39", "static u16", "[]"),
    0x0A014000: table.sym_var("background_g_40", "static u16", "[]"),
    0x0A014800: table.sym_var("background_g_41", "static u16", "[]"),
    0x0A015000: table.sym_var("background_g_42", "static u16", "[]"),
    0x0A015800: table.sym_var("background_g_43", "static u16", "[]"),
    0x0A016000: table.sym_var("background_g_44", "static u16", "[]"),
    0x0A016800: table.sym_var("background_g_45", "static u16", "[]"),
    0x0A017000: table.sym_var("background_g_46", "static u16", "[]"),
    0x0A017800: table.sym_var("background_g_47", "static u16", "[]"),
    0x0A018000: table.sym_var("background_g_48", "static u16", "[]"),
    0x0A018800: table.sym_var("background_g_49", "static u16", "[]"),
    0x0A019000: table.sym_var("background_g_50", "static u16", "[]"),
    0x0A019800: table.sym_var("background_g_51", "static u16", "[]"),
    0x0A01A000: table.sym_var("background_g_52", "static u16", "[]"),
    0x0A01A800: table.sym_var("background_g_53", "static u16", "[]"),
    0x0A01B000: table.sym_var("background_g_54", "static u16", "[]"),
    0x0A01B800: table.sym_var("background_g_55", "static u16", "[]"),
    0x0A01C000: table.sym_var("background_g_56", "static u16", "[]"),
    0x0A01C800: table.sym_var("background_g_57", "static u16", "[]"),
    0x0A01D000: table.sym_var("background_g_58", "static u16", "[]"),
    0x0A01D800: table.sym_var("background_g_59", "static u16", "[]"),
    0x0A01E000: table.sym_var("background_g_60", "static u16", "[]"),
    0x0A01E800: table.sym_var("background_g_61", "static u16", "[]"),
    0x0A01F000: table.sym_var("background_g_62", "static u16", "[]"),
    0x0A01F800: table.sym_var("background_g_63", "static u16", "[]"),
    0x0A020000: table.sym_var("background_g", "u16 *", "[]", table.GLOBL),
}

sym_E0_bg_h = {
    0x002FB1B0: table.sym("_background_h_szpSegmentRomStart"),
    0x0A000000: table.sym_var("background_h_0", "static u16", "[]"),
    0x0A000800: table.sym_var("background_h_1", "static u16", "[]"),
    0x0A001000: table.sym_var("background_h_2", "static u16", "[]"),
    0x0A001800: table.sym_var("background_h_3", "static u16", "[]"),
    0x0A002000: table.sym_var("background_h_4", "static u16", "[]"),
    0x0A002800: table.sym_var("background_h_5", "static u16", "[]"),
    0x0A003000: table.sym_var("background_h_6", "static u16", "[]"),
    0x0A003800: table.sym_var("background_h_7", "static u16", "[]"),
    0x0A004000: table.sym_var("background_h_8", "static u16", "[]"),
    0x0A004800: table.sym_var("background_h_9", "static u16", "[]"),
    0x0A005000: table.sym_var("background_h_10", "static u16", "[]"),
    0x0A005800: table.sym_var("background_h_11", "static u16", "[]"),
    0x0A006000: table.sym_var("background_h_12", "static u16", "[]"),
    0x0A006800: table.sym_var("background_h_13", "static u16", "[]"),
    0x0A007000: table.sym_var("background_h_14", "static u16", "[]"),
    0x0A007800: table.sym_var("background_h_15", "static u16", "[]"),
    0x0A008000: table.sym_var("background_h_16", "static u16", "[]"),
    0x0A008800: table.sym_var("background_h_17", "static u16", "[]"),
    0x0A009000: table.sym_var("background_h_18", "static u16", "[]"),
    0x0A009800: table.sym_var("background_h_19", "static u16", "[]"),
    0x0A00A000: table.sym_var("background_h_20", "static u16", "[]"),
    0x0A00A800: table.sym_var("background_h_21", "static u16", "[]"),
    0x0A00B000: table.sym_var("background_h_22", "static u16", "[]"),
    0x0A00B800: table.sym_var("background_h_23", "static u16", "[]"),
    0x0A00C000: table.sym_var("background_h_24", "static u16", "[]"),
    0x0A00C800: table.sym_var("background_h_25", "static u16", "[]"),
    0x0A00D000: table.sym_var("background_h_26", "static u16", "[]"),
    0x0A00D800: table.sym_var("background_h_27", "static u16", "[]"),
    0x0A00E000: table.sym_var("background_h_28", "static u16", "[]"),
    0x0A00E800: table.sym_var("background_h_29", "static u16", "[]"),
    0x0A00F000: table.sym_var("background_h_30", "static u16", "[]"),
    0x0A00F800: table.sym_var("background_h_31", "static u16", "[]"),
    0x0A010000: table.sym_var("background_h_32", "static u16", "[]"),
    0x0A010800: table.sym_var("background_h_33", "static u16", "[]"),
    0x0A011000: table.sym_var("background_h_34", "static u16", "[]"),
    0x0A011800: table.sym_var("background_h_35", "static u16", "[]"),
    0x0A012000: table.sym_var("background_h_36", "static u16", "[]"),
    0x0A012800: table.sym_var("background_h_37", "static u16", "[]"),
    0x0A013000: table.sym_var("background_h_38", "static u16", "[]"),
    0x0A013800: table.sym_var("background_h_39", "static u16", "[]"),
    0x0A014000: table.sym_var("background_h_40", "static u16", "[]"),
    0x0A014800: table.sym_var("background_h", "u16 *", "[]", table.GLOBL),
}

sym_E0_bg_i = {
    0x00301CD0: table.sym("_background_i_szpSegmentRomStart"),
    0x0A000000: table.sym_var("background_i_0", "static u16", "[]"),
    0x0A000800: table.sym_var("background_i_1", "static u16", "[]"),
    0x0A001000: table.sym_var("background_i_2", "static u16", "[]"),
    0x0A001800: table.sym_var("background_i_3", "static u16", "[]"),
    0x0A002000: table.sym_var("background_i_4", "static u16", "[]"),
    0x0A002800: table.sym_var("background_i_5", "static u16", "[]"),
    0x0A003000: table.sym_var("background_i_6", "static u16", "[]"),
    0x0A003800: table.sym_var("background_i_7", "static u16", "[]"),
    0x0A004000: table.sym_var("background_i_8", "static u16", "[]"),
    0x0A004800: table.sym_var("background_i_9", "static u16", "[]"),
    0x0A005000: table.sym_var("background_i_10", "static u16", "[]"),
    0x0A005800: table.sym_var("background_i_11", "static u16", "[]"),
    0x0A006000: table.sym_var("background_i_12", "static u16", "[]"),
    0x0A006800: table.sym_var("background_i_13", "static u16", "[]"),
    0x0A007000: table.sym_var("background_i_14", "static u16", "[]"),
    0x0A007800: table.sym_var("background_i_15", "static u16", "[]"),
    0x0A008000: table.sym_var("background_i_16", "static u16", "[]"),
    0x0A008800: table.sym_var("background_i_17", "static u16", "[]"),
    0x0A009000: table.sym_var("background_i_18", "static u16", "[]"),
    0x0A009800: table.sym_var("background_i_19", "static u16", "[]"),
    0x0A00A000: table.sym_var("background_i_20", "static u16", "[]"),
    0x0A00A800: table.sym_var("background_i_21", "static u16", "[]"),
    0x0A00B000: table.sym_var("background_i_22", "static u16", "[]"),
    0x0A00B800: table.sym_var("background_i_23", "static u16", "[]"),
    0x0A00C000: table.sym_var("background_i_24", "static u16", "[]"),
    0x0A00C800: table.sym_var("background_i_25", "static u16", "[]"),
    0x0A00D000: table.sym_var("background_i_26", "static u16", "[]"),
    0x0A00D800: table.sym_var("background_i_27", "static u16", "[]"),
    0x0A00E000: table.sym_var("background_i_28", "static u16", "[]"),
    0x0A00E800: table.sym_var("background_i_29", "static u16", "[]"),
    0x0A00F000: table.sym_var("background_i_30", "static u16", "[]"),
    0x0A00F800: table.sym_var("background_i_31", "static u16", "[]"),
    0x0A010000: table.sym_var("background_i_32", "static u16", "[]"),
    0x0A010800: table.sym_var("background_i_33", "static u16", "[]"),
    0x0A011000: table.sym_var("background_i_34", "static u16", "[]"),
    0x0A011800: table.sym_var("background_i_35", "static u16", "[]"),
    0x0A012000: table.sym_var("background_i_36", "static u16", "[]"),
    0x0A012800: table.sym_var("background_i_37", "static u16", "[]"),
    0x0A013000: table.sym_var("background_i_38", "static u16", "[]"),
    0x0A013800: table.sym_var("background_i_39", "static u16", "[]"),
    0x0A014000: table.sym_var("background_i_40", "static u16", "[]"),
    0x0A014800: table.sym_var("background_i_41", "static u16", "[]"),
    0x0A015000: table.sym_var("background_i_42", "static u16", "[]"),
    0x0A015800: table.sym_var("background_i_43", "static u16", "[]"),
    0x0A016000: table.sym_var("background_i_44", "static u16", "[]"),
    0x0A016800: table.sym_var("background_i_45", "static u16", "[]"),
    0x0A017000: table.sym_var("background_i_46", "static u16", "[]"),
    0x0A017800: table.sym_var("background_i_47", "static u16", "[]"),
    0x0A018000: table.sym_var("background_i_48", "static u16", "[]"),
    0x0A018800: table.sym_var("background_i_49", "static u16", "[]"),
    0x0A019000: table.sym_var("background_i_50", "static u16", "[]"),
    0x0A019800: table.sym_var("background_i_51", "static u16", "[]"),
    0x0A01A000: table.sym_var("background_i_52", "static u16", "[]"),
    0x0A01A800: table.sym_var("background_i_53", "static u16", "[]"),
    0x0A01B000: table.sym_var("background_i_54", "static u16", "[]"),
    0x0A01B800: table.sym_var("background_i_55", "static u16", "[]"),
    0x0A01C000: table.sym_var("background_i_56", "static u16", "[]"),
    0x0A01C800: table.sym_var("background_i_57", "static u16", "[]"),
    0x0A01D000: table.sym_var("background_i_58", "static u16", "[]"),
    0x0A01D800: table.sym_var("background_i_59", "static u16", "[]"),
    0x0A01E000: table.sym_var("background_i_60", "static u16", "[]"),
    0x0A01E800: table.sym_var("background_i_61", "static u16", "[]"),
    0x0A01F000: table.sym_var("background_i_62", "static u16", "[]"),
    0x0A01F800: table.sym_var("background_i_63", "static u16", "[]"),
    0x0A020000: table.sym_var("background_i", "u16 *", "[]", table.GLOBL),
}

sym_E0_bg_j = {
    0x0030CEC0: table.sym("_background_j_szpSegmentRomStart"),
    0x0A000000: table.sym_var("background_j_0", "static u16", "[]"),
    0x0A000800: table.sym_var("background_j_1", "static u16", "[]"),
    0x0A001000: table.sym_var("background_j_2", "static u16", "[]"),
    0x0A001800: table.sym_var("background_j_3", "static u16", "[]"),
    0x0A002000: table.sym_var("background_j_4", "static u16", "[]"),
    0x0A002800: table.sym_var("background_j_5", "static u16", "[]"),
    0x0A003000: table.sym_var("background_j_6", "static u16", "[]"),
    0x0A003800: table.sym_var("background_j_7", "static u16", "[]"),
    0x0A004000: table.sym_var("background_j_8", "static u16", "[]"),
    0x0A004800: table.sym_var("background_j_9", "static u16", "[]"),
    0x0A005000: table.sym_var("background_j_10", "static u16", "[]"),
    0x0A005800: table.sym_var("background_j_11", "static u16", "[]"),
    0x0A006000: table.sym_var("background_j_12", "static u16", "[]"),
    0x0A006800: table.sym_var("background_j_13", "static u16", "[]"),
    0x0A007000: table.sym_var("background_j_14", "static u16", "[]"),
    0x0A007800: table.sym_var("background_j_15", "static u16", "[]"),
    0x0A008000: table.sym_var("background_j_16", "static u16", "[]"),
    0x0A008800: table.sym_var("background_j_17", "static u16", "[]"),
    0x0A009000: table.sym_var("background_j_18", "static u16", "[]"),
    0x0A009800: table.sym_var("background_j_19", "static u16", "[]"),
    0x0A00A000: table.sym_var("background_j_20", "static u16", "[]"),
    0x0A00A800: table.sym_var("background_j_21", "static u16", "[]"),
    0x0A00B000: table.sym_var("background_j_22", "static u16", "[]"),
    0x0A00B800: table.sym_var("background_j_23", "static u16", "[]"),
    0x0A00C000: table.sym_var("background_j_24", "static u16", "[]"),
    0x0A00C800: table.sym_var("background_j_25", "static u16", "[]"),
    0x0A00D000: table.sym_var("background_j_26", "static u16", "[]"),
    0x0A00D800: table.sym_var("background_j_27", "static u16", "[]"),
    0x0A00E000: table.sym_var("background_j_28", "static u16", "[]"),
    0x0A00E800: table.sym_var("background_j_29", "static u16", "[]"),
    0x0A00F000: table.sym_var("background_j_30", "static u16", "[]"),
    0x0A00F800: table.sym_var("background_j_31", "static u16", "[]"),
    0x0A010000: table.sym_var("background_j_32", "static u16", "[]"),
    0x0A010800: table.sym_var("background_j_33", "static u16", "[]"),
    0x0A011000: table.sym_var("background_j_34", "static u16", "[]"),
    0x0A011800: table.sym_var("background_j_35", "static u16", "[]"),
    0x0A012000: table.sym_var("background_j_36", "static u16", "[]"),
    0x0A012800: table.sym_var("background_j_37", "static u16", "[]"),
    0x0A013000: table.sym_var("background_j_38", "static u16", "[]"),
    0x0A013800: table.sym_var("background_j_39", "static u16", "[]"),
    0x0A014000: table.sym_var("background_j_40", "static u16", "[]"),
    0x0A014800: table.sym_var("background_j_41", "static u16", "[]"),
    0x0A015000: table.sym_var("background_j_42", "static u16", "[]"),
    0x0A015800: table.sym_var("background_j_43", "static u16", "[]"),
    0x0A016000: table.sym_var("background_j_44", "static u16", "[]"),
    0x0A016800: table.sym_var("background_j_45", "static u16", "[]"),
    0x0A017000: table.sym_var("background_j_46", "static u16", "[]"),
    0x0A017800: table.sym_var("background_j_47", "static u16", "[]"),
    0x0A018000: table.sym_var("background_j_48", "static u16", "[]"),
    0x0A018800: table.sym_var("background_j_49", "static u16", "[]"),
    0x0A019000: table.sym_var("background_j_50", "static u16", "[]"),
    0x0A019800: table.sym_var("background_j_51", "static u16", "[]"),
    0x0A01A000: table.sym_var("background_j_52", "static u16", "[]"),
    0x0A01A800: table.sym_var("background_j_53", "static u16", "[]"),
    0x0A01B000: table.sym_var("background_j_54", "static u16", "[]"),
    0x0A01B800: table.sym_var("background_j_55", "static u16", "[]"),
    0x0A01C000: table.sym_var("background_j_56", "static u16", "[]"),
    0x0A01C800: table.sym_var("background_j_57", "static u16", "[]"),
    0x0A01D000: table.sym_var("background_j_58", "static u16", "[]"),
    0x0A01D800: table.sym_var("background_j_59", "static u16", "[]"),
    0x0A01E000: table.sym_var("background_j_60", "static u16", "[]"),
    0x0A01E800: table.sym_var("background_j_61", "static u16", "[]"),
    0x0A01F000: table.sym_var("background_j_62", "static u16", "[]"),
    0x0A01F800: table.sym_var("background_j_63", "static u16", "[]"),
    0x0A020000: table.sym_var("background_j", "u16 *", "[]", table.GLOBL),
}

sym_E0_txt_a = {
    0x0031E1D0: table.sym("_texture_a_szpSegmentRomStart"),
    0x09000000: table.sym_var("txt_a_0",    "u16", "[]"),
    0x09000800: table.sym_var("txt_a_1",    "u16", "[]"),
    0x09001000: table.sym_var("txt_a_2",    "u16", "[]"),
    0x09001800: table.sym_var("txt_a_3",    "u16", "[]"),
    0x09002000: table.sym_var("txt_a_4",    "u16", "[]"),
    0x09002800: table.sym_var("txt_a_5",    "u16", "[]"),
    0x09003000: table.sym_var("txt_a_6",    "u16", "[]"),
    0x09003800: table.sym_var("txt_a_7",    "u16", "[]"),
    0x09004000: table.sym_var("txt_a_8",    "u16", "[]"),
    0x09004800: table.sym_var("txt_a_9",    "u16", "[]"),
    0x09005000: table.sym_var("txt_a_10",   "u16", "[]"),
    0x09005800: table.sym_var("txt_a_11",   "u16", "[]"),
    0x09006000: table.sym_var("txt_a_12",   "u16", "[]"),
    0x09006800: table.sym_var("txt_a_13",   "u16", "[]"),
    0x09007000: table.sym_var("txt_a_14",   "u16", "[]"),
    0x09007800: table.sym_var("txt_a_15",   "u16", "[]"),
    0x09008000: table.sym_var("txt_a_16",   "u16", "[]"),
    0x09008800: table.sym_var("txt_a_17",   "u16", "[]"),
    0x09009000: table.sym_var("txt_a_18",   "u16", "[]"),
    0x09009800: table.sym_var("txt_a_19",   "u16", "[]"),
    0x0900A000: table.sym_var("txt_a_20",   "u16", "[]"),
    0x0900A800: table.sym_var("txt_a_21",   "u16", "[]"),
    0x0900B000: table.sym_var("txt_a_22",   "u16", "[]"),
    0x0900B800: table.sym_var("txt_a_23",   "u16", "[]"),
}

sym_E0_txt_b = {
    0x00326E40: table.sym("_texture_b_szpSegmentRomStart"),
    0x09000000: table.sym_var("txt_b_0",    "u16", "[]"),
    0x09000800: table.sym_var("txt_b_1",    "u16", "[]"),
    0x09001000: table.sym_var("txt_b_2",    "u16", "[]"),
    0x09001800: table.sym_var("txt_b_3",    "u16", "[]"),
    0x09002800: table.sym_var("txt_b_4",    "u16", "[]"),
    0x09003800: table.sym_var("txt_b_5",    "u16", "[]"),
    0x09004800: table.sym_var("txt_b_6",    "u16", "[]"),
    0x09005000: table.sym_var("txt_b_7",    "u16", "[]"),
    0x09006000: table.sym_var("txt_b_8",    "u16", "[]"),
    0x09006800: table.sym_var("txt_b_9",    "u16", "[]"),
    0x09007000: table.sym_var("txt_b_10",   "u16", "[]"),
    0x09008000: table.sym_var("txt_b_11",   "u16", "[]"),
    0x09008800: table.sym_var("txt_b_12",   "u16", "[]"),
    0x09009000: table.sym_var("txt_b_13",   "u16", "[]"),
    0x0900A000: table.sym_var("txt_b_14",   "u16", "[]"),
    0x0900A800: table.sym_var("txt_b_15",   "u16", "[]"),
    0x0900B000: table.sym_var("txt_b_16",   "u16", "[]"),
    0x0900B800: table.sym_var("txt_b_17",   "u16", "[]"),
}

sym_E0_txt_c = {
    0x0032D070: table.sym("_texture_c_szpSegmentRomStart"),
    0x09000000: table.sym_var("txt_c_0",    "u16", "[]"),
    0x09000800: table.sym_var("txt_c_1",    "u16", "[]"),
    0x09001000: table.sym_var("txt_c_2",    "u16", "[]"),
    0x09001800: table.sym_var("txt_c_3",    "u16", "[]"),
    0x09002000: table.sym_var("txt_c_4",    "u16", "[]"),
    0x09002800: table.sym_var("txt_c_5",    "u16", "[]"),
    0x09003000: table.sym_var("txt_c_6",    "u16", "[]"),
    0x09003800: table.sym_var("txt_c_7",    "u16", "[]"),
    0x09004000: table.sym_var("txt_c_8",    "u16", "[]"),
    0x09004800: table.sym_var("txt_c_9",    "u16", "[]"),
    0x09005000: table.sym_var("txt_c_10",   "u16", "[]"),
    0x09005800: table.sym_var("txt_c_11",   "u16", "[]"),
    0x09006000: table.sym_var("txt_c_12",   "u16", "[]"),
    0x09007000: table.sym_var("txt_c_13",   "u16", "[]"),
    0x09007800: table.sym_var("txt_c_14",   "u16", "[]"),
    0x09008000: table.sym_var("txt_c_15",   "u16", "[]"),
    0x09008800: table.sym_var("txt_c_16",   "u16", "[]"),
    0x09009000: table.sym_var("txt_c_17",   "u16", "[]"),
    0x09009800: table.sym_var("txt_c_18",   "u16", "[]"),
    0x0900A000: table.sym_var("txt_c_19",   "u16", "[]"),
    0x0900A800: table.sym_var("txt_c_20",   "u16", "[]"),
    0x0900B000: table.sym_var("txt_c_21",   "u16", "[]"),
}

sym_E0_txt_d = {
    0x00334B30: table.sym("_texture_d_szpSegmentRomStart"),
    0x09000000: table.sym_var("txt_d_0",    "u16", "[]"),
    0x09000800: table.sym_var("txt_d_1",    "u16", "[]"),
    0x09001800: table.sym_var("txt_d_2",    "u16", "[]"),
    0x09002800: table.sym_var("txt_d_3",    "u16", "[]"),
    0x09003800: table.sym_var("txt_d_4",    "u16", "[]"),
    0x09004800: table.sym_var("txt_d_5",    "u16", "[]"),
    0x09005800: table.sym_var("txt_d_6",    "u16", "[]"),
    0x09006000: table.sym_var("txt_d_7",    "u16", "[]"),
    0x09006800: table.sym_var("txt_d_8",    "u16", "[]"),
    0x09007800: table.sym_var("txt_d_9",    "u16", "[]"),
    0x09008800: table.sym_var("txt_d_10",   "u16", "[]"),
    0x09009000: table.sym_var("txt_d_11",   "u16", "[]"),
    0x0900A000: table.sym_var("txt_d_12",   "u16", "[]"),
    0x0900A800: table.sym_var("txt_d_13",   "u16", "[]"),
    0x0900B800: table.sym_var("txt_d_14",   "u16", "[]"),
}

sym_E0_txt_e = {
    0x0033D710: table.sym("_texture_e_szpSegmentRomStart"),
    0x09000000: table.sym_var("txt_e_0",    "u16", "[]"),
    0x09000800: table.sym_var("txt_e_1",    "u16", "[]"),
    0x09001000: table.sym_var("txt_e_2",    "u16", "[]"),
    0x09001800: table.sym_var("txt_e_3",    "u16", "[]"),
    0x09002000: table.sym_var("txt_e_4",    "u16", "[]"),
    0x09003000: table.sym_var("txt_e_5",    "u16", "[]"),
    0x09003800: table.sym_var("txt_e_6",    "u16", "[]"),
    0x09004800: table.sym_var("txt_e_7",    "u16", "[]"),
    0x09005000: table.sym_var("txt_e_8",    "u16", "[]"),
    0x09005800: table.sym_var("txt_e_9",    "u16", "[]"),
    0x09006000: table.sym_var("txt_e_10",   "u16", "[]"),
    0x09006800: table.sym_var("txt_e_11",   "u16", "[]"),
    0x09007000: table.sym_var("txt_e_12",   "u16", "[]"),
    0x09007800: table.sym_var("txt_e_13",   "u16", "[]"),
    0x09008000: table.sym_var("txt_e_14",   "u16", "[]"),
}

sym_E0_txt_f = {
    0x00341140: table.sym("_texture_f_szpSegmentRomStart"),
    0x09000000: table.sym_var("txt_f_0",    "u16", "[]"),
    0x09000800: table.sym_var("txt_f_1",    "u16", "[]"),
    0x09001000: table.sym_var("txt_f_2",    "u16", "[]"),
    0x09002000: table.sym_var("txt_f_3",    "u16", "[]"),
    0x09002800: table.sym_var("txt_f_4",    "u16", "[]"),
    0x09003000: table.sym_var("txt_f_5",    "u16", "[]"),
    0x09003800: table.sym_var("txt_f_6",    "u16", "[]"),
    0x09004000: table.sym_var("txt_f_7",    "u16", "[]"),
    0x09004800: table.sym_var("txt_f_8",    "u16", "[]"),
    0x09005000: table.sym_var("txt_f_9",    "u16", "[]"),
    0x09005800: table.sym_var("txt_f_10",   "u16", "[]"),
    0x09006000: table.sym_var("txt_f_11",   "u16", "[]"),
    0x09006800: table.sym_var("txt_f_12",   "u16", "[]"),
    0x09007000: table.sym_var("txt_f_13",   "u16", "[]"),
    0x09008000: table.sym_var("txt_f_14",   "u16", "[]"),
    0x09008800: table.sym_var("txt_f_15",   "u16", "[]"),
    0x09009000: table.sym_var("txt_f_16",   "u16", "[]"),
    0x09009800: table.sym_var("txt_f_17",   "u16", "[]"),
}

sym_E0_txt_g = {
    0x00347A50: table.sym("_texture_g_szpSegmentRomStart"),
    0x09000000: table.sym_var("txt_g_0",    "u16", "[]"),
    0x09001000: table.sym_var("txt_g_1",    "u16", "[]"),
    0x09001800: table.sym_var("txt_g_2",    "u16", "[]"),
    0x09002000: table.sym_var("txt_g_3",    "u16", "[]"),
    0x09002800: table.sym_var("txt_g_4",    "u16", "[]"),
    0x09003000: table.sym_var("txt_g_5",    "u16", "[]"),
    0x09003800: table.sym_var("txt_g_6",    "u16", "[]"),
    0x09004800: table.sym_var("txt_g_7",    "u16", "[]"),
    0x09005800: table.sym_var("txt_g_8",    "u16", "[]"),
    0x09006800: table.sym_var("txt_g_9",    "u16", "[]"),
    0x09007000: table.sym_var("txt_g_10",   "u16", "[]"),
    0x09007800: table.sym_var("txt_g_11",   "u16", "[]"),
    0x09008800: table.sym_var("txt_g_12",   "u16", "[]"),
    0x09009800: table.sym_var("txt_g_13",   "u16", "[]"),
    0x0900A000: table.sym_var("txt_g_14",   "u16", "[]"),
    0x0900A800: table.sym_var("txt_g_15",   "u16", "[]"),
    0x0900B800: table.sym_var("txt_g_16",   "u16", "[]"),
    0x0900C000: table.sym_var("txt_g_17",   "u16", "[]"),
}

sym_E0_txt_h = {
    0x0034E760: table.sym("_texture_h_szpSegmentRomStart"),
    0x09000000: table.sym_var("txt_h_0",    "u16", "[]"),
    0x09000800: table.sym_var("txt_h_1",    "u16", "[]"),
    0x09001000: table.sym_var("txt_h_2",    "u16", "[]"),
    0x09001800: table.sym_var("txt_h_3",    "u16", "[]"),
    0x09002000: table.sym_var("txt_h_4",    "u16", "[]"),
    0x09002800: table.sym_var("txt_h_5",    "u16", "[]"),
    0x09003000: table.sym_var("txt_h_6",    "u16", "[]"),
    0x09003800: table.sym_var("txt_h_7",    "u16", "[]"),
    0x09004000: table.sym_var("txt_h_8",    "u16", "[]"),
    0x09005000: table.sym_var("txt_h_9",    "u16", "[]"),
    0x09005800: table.sym_var("txt_h_10",   "u16", "[]"),
    0x09006000: table.sym_var("txt_h_11",   "u16", "[]"),
    0x09006800: table.sym_var("txt_h_12",   "u16", "[]"),
    0x09007000: table.sym_var("txt_h_13",   "u16", "[]"),
    0x09007800: table.sym_var("txt_h_14",   "u16", "[]"),
    0x09008000: table.sym_var("txt_h_15",   "u16", "[]"),
    0x09008400: table.sym_var("txt_h_16",   "u16", "[]"),
}

sym_E0_txt_i = {
    0x00351960: table.sym("_texture_i_szpSegmentRomStart"),
    0x09000000: table.sym_var("txt_i_0",    "u16", "[]"),
    0x09000800: table.sym_var("txt_i_1",    "u16", "[]"),
    0x09001800: table.sym_var("txt_i_2",    "u16", "[]"),
    0x09002000: table.sym_var("txt_i_3",    "u16", "[]"),
    0x09002800: table.sym_var("txt_i_4",    "u16", "[]"),
    0x09003000: table.sym_var("txt_i_5",    "u16", "[]"),
    0x09003800: table.sym_var("txt_i_6",    "u16", "[]"),
    0x09004000: table.sym_var("txt_i_7",    "u16", "[]"),
    0x09004800: table.sym_var("txt_i_8",    "u16", "[]"),
    0x09005000: table.sym_var("txt_i_9",    "u16", "[]"),
    0x09005800: table.sym_var("txt_i_10",   "u16", "[]"),
    0x09006000: table.sym_var("txt_i_11",   "u16", "[]"),
    0x09006800: table.sym_var("txt_i_12",   "u16", "[]"),
    0x09007000: table.sym_var("txt_i_13",   "u16", "[]"),
    0x09007800: table.sym_var("txt_i_14",   "u16", "[]"),
    0x09008000: table.sym_var("txt_i_15",   "u16", "[]"),
    0x09008800: table.sym_var("txt_i_16",   "u16", "[]"),
    0x09009800: table.sym_var("txt_i_17",   "u16", "[]"),
    0x0900A000: table.sym_var("txt_i_18",   "u16", "[]"),
    0x0900A800: table.sym_var("txt_i_19",   "u16", "[]"),
    0x0900B000: table.sym_var("txt_i_20",   "u16", "[]"),
    0x0900B800: table.sym_var("txt_i_21",   "u16", "[]"),
    0x0900C000: table.sym_var("txt_i_22",   "u16", "[]"),
}

sym_E0_txt_j = {
    0x00357350: table.sym("_texture_j_szpSegmentRomStart"),
    0x09000000: table.sym_var("txt_j_0",    "u16", "[]"),
    0x09000800: table.sym_var("txt_j_1",    "u16", "[]"),
    0x09001000: table.sym_var("txt_j_2",    "u16", "[]"),
    0x09001800: table.sym_var("txt_j_3",    "u16", "[]"),
    0x09002000: table.sym_var("txt_j_4",    "u16", "[]"),
    0x09002800: table.sym_var("txt_j_5",    "u16", "[]"),
    0x09003000: table.sym_var("txt_j_6",    "u16", "[]"),
    0x09003800: table.sym_var("txt_j_7",    "u16", "[]"),
    0x09004000: table.sym_var("txt_j_8",    "u16", "[]"),
    0x09004800: table.sym_var("txt_j_9",    "u16", "[]"),
    0x09005000: table.sym_var("txt_j_10",   "u16", "[]"),
    0x09005800: table.sym_var("txt_j_11",   "u16", "[]"),
    0x09006000: table.sym_var("txt_j_12",   "u16", "[]"),
    0x09006800: table.sym_var("txt_j_13",   "u16", "[]"),
    0x09007000: table.sym_var("txt_j_14",   "u16", "[]"),
    0x09007800: table.sym_var("txt_j_15",   "u16", "[]"),
    0x09008000: table.sym_var("txt_j_16",   "u16", "[]"),
    0x09008800: table.sym_var("txt_j_17",   "u16", "[]"),
    0x09009000: table.sym_var("txt_j_18",   "u16", "[]"),
    0x09009800: table.sym_var("txt_j_19",   "u16", "[]"),
    0x0900A000: table.sym_var("txt_j_20",   "u16", "[]"),
    0x0900A800: table.sym_var("txt_j_21",   "u16", "[]"),
    0x0900B000: table.sym_var("txt_j_22",   "u16", "[]"),
    0x0900B800: table.sym_var("txt_j_23",   "u16", "[]"),
}

sym_E0_txt_k = {
    0x0035ED10: table.sym("_texture_k_szpSegmentRomStart"),
    0x09000000: table.sym_var("txt_k_0",    "u16", "[]"),
    0x09000800: table.sym_var("txt_k_1",    "u16", "[]"),
    0x09001000: table.sym_var("txt_k_2",    "u16", "[]"),
    0x09002000: table.sym_var("txt_k_3",    "u16", "[]"),
    0x09002800: table.sym_var("txt_k_4",    "u16", "[]"),
    0x09003000: table.sym_var("txt_k_5",    "u16", "[]"),
    0x09003800: table.sym_var("txt_k_6",    "u16", "[]"),
    0x09004000: table.sym_var("txt_k_7",    "u16", "[]"),
    0x09004800: table.sym_var("txt_k_8",    "u16", "[]"),
    0x09005000: table.sym_var("txt_k_9",    "u16", "[]"),
    0x09005800: table.sym_var("txt_k_10",   "u16", "[]"),
    0x09006000: table.sym_var("txt_k_11",   "u16", "[]"),
    0x09006800: table.sym_var("txt_k_12",   "u16", "[]"),
    0x09007800: table.sym_var("txt_k_13",   "u16", "[]"),
    0x09008000: table.sym_var("txt_k_14",   "u16", "[]"),
    0x09008800: table.sym_var("txt_k_15",   "u16", "[]"),
    0x09009000: table.sym_var("txt_k_16",   "u16", "[]"),
    0x09009800: table.sym_var("txt_k_17",   "u16", "[]"),
    0x0900A000: table.sym_var("txt_k_18",   "u16", "[]"),
    0x0900A800: table.sym_var("txt_k_19",   "u16", "[]"),
    0x0900B000: table.sym_var("txt_k_20",   "u16", "[]"),
    0x0900B400: table.sym_var("txt_k_21",   "u16", "[]"),
    0x0900BC00: table.sym_var("txt_k_22",   "u16", "[]"),
}

sym_E0_txt_l = {
    0x00365980: table.sym("_texture_l_szpSegmentRomStart"),
    0x09000000: table.sym_var("txt_l_0",    "u16", "[]"),
    0x09001000: table.sym_var("txt_l_1",    "u16", "[]"),
    0x09002000: table.sym_var("txt_l_2",    "u16", "[]"),
    0x09003000: table.sym_var("txt_l_3",    "u16", "[]"),
    0x09003800: table.sym_var("txt_l_4",    "u16", "[]"),
    0x09004000: table.sym_var("txt_l_5",    "u16", "[]"),
    0x09004800: table.sym_var("txt_l_6",    "u16", "[]"),
    0x09005000: table.sym_var("txt_l_7",    "u16", "[]"),
    0x09005800: table.sym_var("txt_l_8",    "u16", "[]"),
    0x09006000: table.sym_var("txt_l_9",    "u16", "[]"),
    0x09007000: table.sym_var("txt_l_10",   "u16", "[]"),
    0x09008000: table.sym_var("txt_l_11",   "u16", "[]"),
    0x09008800: table.sym_var("txt_l_12",   "u16", "[]"),
    0x09009000: table.sym_var("txt_l_13",   "u16", "[]"),
    0x09009800: table.sym_var("txt_l_14",   "u16", "[]"),
    0x0900A000: table.sym_var("txt_l_15",   "u16", "[]"),
    0x0900B000: table.sym_var("txt_l_16",   "u16", "[]"),
    0x0900B800: table.sym_var("txt_l_17",   "u16", "[]"),
}

sym_E0_weather = {
    0x0036F530: table.sym("_weather_szpSegmentRomStart"),
    0x0B000000: table.sym_var("align_weather",          "unused static u64"),
    0x0B000008: table.sym_var("txt_weather_flower_0",   "static u16", "[]"),
    0x0B000808: table.sym_var("txt_weather_flower_1",   "static u16", "[]"),
    0x0B001008: table.sym_var("txt_weather_flower_2",   "static u16", "[]"),
    0x0B001808: table.sym_var("txt_weather_flower_3",   "static u16", "[]"),
    0x0B002008: table.sym_var("txt_weather_flower",     "u16 *", "[]"),
    0x0B002020: table.sym_var("txt_weather_lava_0",     "static u16", "[]"),
    0x0B002820: table.sym_var("txt_weather_lava_1",     "static u16", "[]"),
    0x0B003020: table.sym_var("txt_weather_lava_2",     "static u16", "[]"),
    0x0B003820: table.sym_var("txt_weather_lava_3",     "static u16", "[]"),
    0x0B004020: table.sym_var("txt_weather_lava_4",     "static u16", "[]"),
    0x0B004820: table.sym_var("txt_weather_lava_5",     "static u16", "[]"),
    0x0B005020: table.sym_var("txt_weather_lava_6",     "static u16", "[]"),
    0x0B005820: table.sym_var("txt_weather_lava_7",     "static u16", "[]"),
    0x0B006020: table.sym_var("txt_weather_lava",       "u16 *", "[]"),
    0x0B006048: table.sym_var("txt_weather_bubble_0",   "static u16", "[]"),
    0x0B006848: table.sym_var("txt_weather_bubble",     "u16 *", "[]"),
    0x0B00684C: table.sym_var("txt_weather_snow_a",     "static u16", "[]"),
    0x0B006A50: table.sym_var("gfx_weather_snow_a",     "Gfx", "[]"),
    0x0B006AB0: table.sym_var("gfx_weather_end",        "Gfx", "[]"),
    0x0B006AD8: table.sym_var("txt_weather_snow_b",     "static u16", "[]"),
    0x0B006CD8: table.sym_var("gfx_weather_snow_b",     "Gfx", "[]"),
    0x0B006D38: table.sym_var("gfx_weather_lava_start", "Gfx", "[]"),
    0x0B006D68: table.sym_var("gfx_weather_lava_txt",   "Gfx", "[]"),
}

sym_E0_s_bbh = {
    0x00371C40: table.sym("_stage_bbh_szpSegmentRomStart"),
    0x003828C0: table.sym("_stage_bbh_dataSegmentRomStart"),
    0x0E000000: table.sym("p_bbh_0E000000"),
    0x0E000094: table.sym("p_bbh_0E000094"),
    0x0E000128: table.sym("p_bbh_0E000128"),
    0x0E0003CC: table.sym("p_bbh_0E0003CC"),
    0x0E000418: table.sym("p_bbh", table.GLOBL),
    0x0E0005B0: table.sym_var("s_bbh_53", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005C8: table.sym_var("s_bbh_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005E0: table.sym_var("s_bbh_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005F8: table.sym_var("s_bbh_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000610: table.sym_var("s_bbh_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000628: table.sym_var("s_bbh_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000640: table.sym_var("s_bbh_59", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000658: table.sym_var("s_bbh_60", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000670: table.sym_var("s_bbh1_1", "static S_SCRIPT", "[]"),
    0x0E0006B0: table.sym_var("s_bbh1_2", "static S_SCRIPT", "[]"),
    0x0E0006E8: table.sym_var("s_bbh1_3", "static S_SCRIPT", "[]"),
    0x0E000730: table.sym_var("s_bbh1_4", "static S_SCRIPT", "[]"),
    0x0E000750: table.sym_var("s_bbh1_5", "static S_SCRIPT", "[]"),
    0x0E000768: table.sym_var("s_bbh1_6", "static S_SCRIPT", "[]"),
    0x0E0007B0: table.sym_var("s_bbh1_7", "static S_SCRIPT", "[]"),
    0x0E0007D0: table.sym_var("s_bbh1_8", "static S_SCRIPT", "[]"),
    0x0E000800: table.sym_var("s_bbh1_9", "static S_SCRIPT", "[]"),
    0x0E000828: table.sym_var("s_bbh1_10", "static S_SCRIPT", "[]"),
    0x0E000860: table.sym_var("s_bbh1_11", "static S_SCRIPT", "[]"),
    0x0E000888: table.sym_var("s_bbh1_12", "static S_SCRIPT", "[]"),
    0x0E0008B0: table.sym_var("s_bbh1_13", "static S_SCRIPT", "[]"),
    0x0E0008E8: table.sym_var("s_bbh1_14", "static S_SCRIPT", "[]"),
    0x0E000950: table.sym_var("s_bbh1_15", "static S_SCRIPT", "[]"),
    0x0E0009C8: table.sym_var("s_bbh1_16", "static S_SCRIPT", "[]"),
    0x0E000A18: table.sym_var("s_bbh1_17", "static S_SCRIPT", "[]"),
    0x0E000A60: table.sym_var("s_bbh1_18", "static S_SCRIPT", "[]"),
    0x0E000AD8: table.sym_var("s_bbh1_19", "static S_SCRIPT", "[]"),
    0x0E000B28: table.sym_var("s_bbh1_20", "static S_SCRIPT", "[]"),
    0x0E000B88: table.sym_var("s_bbh1_21", "static S_SCRIPT", "[]"),
    0x0E000BF0: table.sym_var("s_bbh1_22", "static S_SCRIPT", "[]"),
    0x0E000C38: table.sym_var("s_bbh1_23", "static S_SCRIPT", "[]"),
    0x0E000C88: table.sym_var("s_bbh1_24", "static S_SCRIPT", "[]"),
    0x0E000CE8: table.sym_var("s_bbh1_25", "static S_SCRIPT", "[]"),
    0x0E000D20: table.sym_var("s_bbh1_26", "static S_SCRIPT", "[]"),
    0x0E000D68: table.sym_var("s_bbh1_27", "static S_SCRIPT", "[]"),
    0x0E000DB0: table.sym_var("s_bbh1_28", "static S_SCRIPT", "[]"),
    0x0E000DF0: table.sym_var("s_bbh1_29", "static S_SCRIPT", "[]"),
    0x0E000E40: table.sym_var("s_bbh1_30", "static S_SCRIPT", "[]"),
    0x0E000E80: table.sym_var("s_bbh1_31", "static S_SCRIPT", "[]"),
    0x0E000EB0: table.sym_var("s_bbh1_32", "static S_SCRIPT", "[]"),
    0x0E000F00: table.sym_var("s_bbh1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_ccm = {
    0x00383950: table.sym("_stage_ccm_szpSegmentRomStart"),
    0x00395C90: table.sym("_stage_ccm_dataSegmentRomStart"),
    0x0E000000: table.sym("p_ccm_0E000000"),
    0x0E00001C: table.sym("p_ccm_0E00001C"),
    0x0E000098: table.sym("p_ccm_0E000098"),
    0x0E000114: table.sym("p_ccm_0E000114"),
    0x0E000178: table.sym("p_ccm", table.GLOBL),
    0x0E0003E0: table.sym_var("s_ccm_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000400: table.sym_var("s_ccm_210", "S_SCRIPT", "[]", table.GLOBL),
    0x0E00041C: table.sym_var("s_ccm_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E00043C: table.sym_var("s_ccm_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E00046C: table.sym_var("s_ccm_4", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004A4: table.sym_var("s_ccm_5", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004CC: table.sym_var("s_ccm_6", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004F4: table.sym_var("s_ccm_7", "S_SCRIPT", "[]", table.GLOBL),
    0x0E00052C: table.sym_var("s_ccm1", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005F8: table.sym_var("s_ccm2", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_inside = {
    0x00396340: table.sym("_stage_inside_szpSegmentRomStart"),
    0x003CF0D0: table.sym("_stage_inside_dataSegmentRomStart"),
    0x0E000000: table.sym("p_inside_0E000000"),
    0x0E0003F4: table.sym("p_inside_0E0003F4"),
    0x0E000790: table.sym("p_inside_0E000790"),
    0x0E0009BC: table.sym("p_inside_0E0009BC"),
    0x0E000AF8: table.sym("p_inside", table.GLOBL),
    0x0E000F00: table.sym_var("s_inside_208_209_213_214", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000F18: table.sym_var("s_inside_53", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000F30: table.sym_var("s_inside1_1", "static S_SCRIPT", "[]"),
    0x0E000F70: table.sym_var("s_inside1_2", "static S_SCRIPT", "[]"),
    0x0E000F88: table.sym_var("s_inside1_3", "static S_SCRIPT", "[]"),
    0x0E000FA8: table.sym_var("s_inside1_4", "static S_SCRIPT", "[]"),
    0x0E000FD0: table.sym_var("s_inside1_5", "static S_SCRIPT", "[]"),
    0x0E001000: table.sym_var("s_inside1_6", "static S_SCRIPT", "[]"),
    0x0E001038: table.sym_var("s_inside1_7", "static S_SCRIPT", "[]"),
    0x0E001088: table.sym_var("s_inside1_8", "static S_SCRIPT", "[]"),
    0x0E0010C8: table.sym_var("s_inside1_9", "static S_SCRIPT", "[]"),
    0x0E001110: table.sym_var("s_inside1_10", "static S_SCRIPT", "[]"),
    0x0E001158: table.sym_var("s_inside1_11", "static S_SCRIPT", "[]"),
    0x0E0011A8: table.sym_var("s_inside1_12", "static S_SCRIPT", "[]"),
    0x0E001200: table.sym_var("s_inside1_13", "static S_SCRIPT", "[]"),
    0x0E001260: table.sym_var("s_inside1_14", "static S_SCRIPT", "[]"),
    0x0E0012C8: table.sym_var("s_inside1_15", "static S_SCRIPT", "[]"),
    0x0E001348: table.sym_var("s_inside1_16", "static S_SCRIPT", "[]"),
    0x0E0013B8: table.sym_var("s_inside1_17", "static S_SCRIPT", "[]"),
    0x0E001400: table.sym_var("s_inside1", "S_SCRIPT", "[]", table.GLOBL),
    0x0E001518: table.sym_var("s_inside_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E001530: table.sym_var("s_inside_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E001548: table.sym_var("s_inside_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E001560: table.sym_var("s_inside2_1", "static S_SCRIPT", "[]"),
    0x0E001578: table.sym_var("s_inside2_2", "static S_SCRIPT", "[]"),
    0x0E0015B8: table.sym_var("s_inside2_3", "static S_SCRIPT", "[]"),
    0x0E0015F8: table.sym_var("s_inside2_4", "static S_SCRIPT", "[]"),
    0x0E001628: table.sym_var("s_inside2_5", "static S_SCRIPT", "[]"),
    0x0E001668: table.sym_var("s_inside2_6", "static S_SCRIPT", "[]"),
    0x0E001690: table.sym_var("s_inside2_7", "static S_SCRIPT", "[]"),
    0x0E0016D8: table.sym_var("s_inside2_8", "static S_SCRIPT", "[]"),
    0x0E001740: table.sym_var("s_inside2_9", "static S_SCRIPT", "[]"),
    0x0E001798: table.sym_var("s_inside2_10", "static S_SCRIPT", "[]"),
    0x0E001800: table.sym_var("s_inside2_11", "static S_SCRIPT", "[]"),
    0x0E001858: table.sym_var("s_inside2", "S_SCRIPT", "[]", table.GLOBL),
    0x0E001940: table.sym_var("s_inside_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E001958: table.sym_var("s_inside3_1", "static S_SCRIPT", "[]"),
    0x0E001980: table.sym_var("s_inside3_2", "static S_SCRIPT", "[]"),
    0x0E0019C8: table.sym_var("s_inside3_3", "static S_SCRIPT", "[]"),
    0x0E0019F8: table.sym_var("s_inside3_4", "static S_SCRIPT", "[]"),
    0x0E001A30: table.sym_var("s_inside3_5", "static S_SCRIPT", "[]"),
    0x0E001A58: table.sym_var("s_inside3_6", "static S_SCRIPT", "[]"),
    0x0E001AB8: table.sym_var("s_inside3_7", "static S_SCRIPT", "[]"),
    0x0E001AF8: table.sym_var("s_inside3_8", "static S_SCRIPT", "[]"),
    0x0E001B48: table.sym_var("s_inside3_9", "static S_SCRIPT", "[]"),
    0x0E001BB0: table.sym_var("s_inside3_10", "static S_SCRIPT", "[]"),
    0x0E001C10: table.sym_var("s_inside3", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_hmc = {
    0x003D0DC0: table.sym("_stage_hmc_szpSegmentRomStart"),
    0x003E6A00: table.sym("_stage_hmc_dataSegmentRomStart"),
    0x0E000000: table.sym("p_hmc_0E000000"),
    0x0E0001CC: table.sym("p_hmc_0E0001CC"),
    0x0E000290: table.sym("p_hmc_0E000290"),
    0x0E0002F4: table.sym("p_hmc_0E0002F4"),
    0x0E000388: table.sym("p_hmc", table.GLOBL),
    0x0E000530: table.sym_var("s_hmc_60", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000548: table.sym_var("s_hmc_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000570: table.sym_var("s_hmc_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000588: table.sym_var("s_hmc_59", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005A0: table.sym_var("s_hmc_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005B8: table.sym_var("s_hmc_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005D0: table.sym_var("s_hmc_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005E8: table.sym_var("s_hmc1_1", "static S_SCRIPT", "[]"),
    0x0E000618: table.sym_var("s_hmc1_2", "static S_SCRIPT", "[]"),
    0x0E000658: table.sym_var("s_hmc1_3", "static S_SCRIPT", "[]"),
    0x0E0006A8: table.sym_var("s_hmc1_4", "static S_SCRIPT", "[]"),
    0x0E0006E0: table.sym_var("s_hmc1_5", "static S_SCRIPT", "[]"),
    0x0E000700: table.sym_var("s_hmc1_6", "static S_SCRIPT", "[]"),
    0x0E000748: table.sym_var("s_hmc1_7", "static S_SCRIPT", "[]"),
    0x0E000770: table.sym_var("s_hmc1_8", "static S_SCRIPT", "[]"),
    0x0E000798: table.sym_var("s_hmc1_9", "static S_SCRIPT", "[]"),
    0x0E0007F8: table.sym_var("s_hmc1_10", "static S_SCRIPT", "[]"),
    0x0E000850: table.sym_var("s_hmc1_11", "static S_SCRIPT", "[]"),
    0x0E0008D0: table.sym_var("s_hmc1_12", "static S_SCRIPT", "[]"),
    0x0E000938: table.sym_var("s_hmc1_13", "static S_SCRIPT", "[]"),
    0x0E000998: table.sym_var("s_hmc1_14", "static S_SCRIPT", "[]"),
    0x0E000A18: table.sym_var("s_hmc1_15", "static S_SCRIPT", "[]"),
    0x0E000A88: table.sym_var("s_hmc1_16", "static S_SCRIPT", "[]"),
    0x0E000AE8: table.sym_var("s_hmc1_17", "static S_SCRIPT", "[]"),
    0x0E000B48: table.sym_var("s_hmc1_18", "static S_SCRIPT", "[]"),
    0x0E000B90: table.sym_var("s_hmc1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_ssl = {
    0x003E76B0: table.sym("_stage_ssl_szpSegmentRomStart"),
    0x003FB990: table.sym("_stage_ssl_dataSegmentRomStart"),
    0x0E000000: table.sym("p_ssl_0E000000"),
    0x0E00001C: table.sym("p_ssl_0E00001C"),
    0x0E0000E0: table.sym("p_ssl_0E0000E0"),
    0x0E000114: table.sym("p_ssl_0E000114"),
    0x0E000268: table.sym("p_ssl_0E000268"),
    0x0E00029C: table.sym("p_ssl_0E00029C"),
    0x0E0002B8: table.sym("p_ssl", table.GLOBL),
    0x0E0005C0: table.sym_var("s_ssl_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005D8: table.sym_var("s_ssl_4", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000618: table.sym_var("s_ssl_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000630: table.sym_var("s_ssl_199", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000648: table.sym_var("s_ssl1", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000734: table.sym_var("s_ssl_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000764: table.sym_var("s_ssl_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000794: table.sym_var("s_ssl_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0007AC: table.sym_var("s_ssl_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0007CC: table.sym_var("s_ssl2", "S_SCRIPT", "[]", table.GLOBL),
    0x0E00088C: table.sym_var("s_ssl3", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_bob = {
    0x003FC2B0: table.sym("_stage_bob_szpSegmentRomStart"),
    0x00405A60: table.sym("_stage_bob_dataSegmentRomStart"),
    0x07000000: table.sym_var("txt_bob_0", "static u16", "[]"),
    0x07000800: table.sym_var("txt_bob_1", "static u16", "[]"),
    0x07001000: table.sym_var("txt_bob_2", "static u16", "[]"),
    0x07001800: table.sym_var("txt_bob_3", "static u16", "[]"),
    0x07002000: table.sym_var("txt_bob_4", "static u16", "[]"),

    0x07002800: table.sym_var("light_battlefield_smooth", "static Lights1"),
    0x07003CA8: table.sym_var("gfx_battlefield_0", "static Gfx", "[]"),
    0x070041E0: table.sym_var("gfx_battlefield_1", "static Gfx", "[]"),
    0x070042B8: table.sym_var("gfx_battlefield_2", "static Gfx", "[]"),
    0x07004390: table.sym_var("gfx_battlefield_smooth", "Gfx", "[]"),

    0x07004478: table.sym_var("light_battlefield_flat", "static Lights1"),
    0x07008AF0: table.sym_var("gfx_battlefield_3", "static Gfx", "[]"),
    0x07008C28: table.sym_var("gfx_battlefield_4", "static Gfx", "[]"),
    0x07009050: table.sym_var("gfx_battlefield_5", "static Gfx", "[]"),
    0x07009370: table.sym_var("gfx_battlefield_6", "static Gfx", "[]"),
    0x07009490: table.sym_var("gfx_battlefield_7", "static Gfx", "[]"),
    0x070095B8: table.sym_var("gfx_battlefield_8", "static Gfx", "[]"),
    0x07009768: table.sym_var("gfx_battlefield_9", "static Gfx", "[]"),
    0x070097F8: table.sym_var("gfx_battlefield_10", "static Gfx", "[]"),
    0x07009960: table.sym_var("gfx_battlefield_11", "static Gfx", "[]"),
    0x070099E0: table.sym_var("gfx_battlefield_12", "static Gfx", "[]"),
    0x07009D80: table.sym_var("gfx_battlefield_flat", "Gfx", "[]"),

    0x0700A318: table.sym_var("gfx_battlefield_13", "static Gfx", "[]"),
    0x0700A470: table.sym_var("gfx_battlefield_xlu_decal", "Gfx", "[]"),

    0x0700A800: table.sym_var("gfx_battlefield_14", "static Gfx", "[]"),
    0x0700A848: table.sym_var("gfx_battlefield_15", "static Gfx", "[]"),
    0x0700A920: table.sym_var("gfx_battlefield_tex_edge", "Gfx", "[]"),

    0x0700A9E0: table.sym_var("light_battlefield_shade_h", "static Lights1"),
    0x0700A9F8: table.sym_var("light_battlefield_shade_l", "static Lights1"),
    0x0700CFC0: table.sym_var("gfx_battlefield_16_17", "static Gfx", "[]"),
    0x0700D7D8: table.sym_var("gfx_battlefield_18", "static Gfx", "[]"),
    0x0700D910: table.sym_var("gfx_battlefield_19", "static Gfx", "[]"),
    0x0700DC40: table.sym_var("gfx_battlefield_20", "static Gfx", "[]"),
    0x0700DC88: table.sym_var("gfx_battlefield_21", "static Gfx", "[]"),
    0x0700DCE0: table.sym_var("gfx_battlefield_22", "static Gfx", "[]"),
    0x0700DD18: table.sym_var("gfx_battlefield_shade", "Gfx", "[]"),

    0x0700DE30: table.sym_var("light_battlefield_23", "static Lights1"),
    0x0700E1E8: table.sym_var("gfx_battlefield_23", "static Gfx", "[]"),
    0x0700E338: table.sym_var("gfx_battlefield_23_s", "Gfx", "[]"),

    0x0700E420: table.sym_var("gfx_bob_54", "static Gfx", "[]"),
    0x0700E458: table.sym_var("gfx_bob_54_s", "Gfx", "[]"),

    0x0700E510: table.sym_var("light_bob_55", "static Lights1"),
    0x0700E6C8: table.sym_var("gfx_bob_55", "static Gfx", "[]"),
    0x0700E768: table.sym_var("gfx_bob_55_s", "Gfx", "[]"),

    0x0700E860: table.sym_var("gfx_bob_56", "static Gfx", "[]"),
    0x0700E8A0: table.sym_var("gfx_bob_56_s", "Gfx", "[]"),

    0x0700E958: table.sym_var("map_battlefield", "MAP_DATA", "[]"),
    0x0701104C: table.sym_var("obj_battlefield", "OBJ_DATA", "[]"),
    0x070113C0: table.sym_var("map_bob_54", "MAP_DATA", "[]", table.GLOBL),
    0x070113F0: table.sym_var("map_bob_55", "MAP_DATA", "[]", table.GLOBL),
    0x07011474: table.sym_var("map_bob_56", "MAP_DATA", "[]", table.GLOBL),
    0x07011530: table.sym_var("path_07011530", "PATH_DATA", "[]", table.GLOBL),
    0x070115C4: table.sym_var("path_070115C4", "PATH_DATA", "[]", table.GLOBL),
    0x070116A0: table.sym_var("path_070116A0", "PATH_DATA", "[]", table.GLOBL),

    0x0E000000: table.sym("p_bob_0E000000"),
    0x0E00007C: table.sym("p_bob_0E00007C"),
    0x0E0001E8: table.sym("p_bob_0E0001E8"),
    0x0E000264: table.sym("p_bob", table.GLOBL),
    0x0E000440: table.sym_var("s_bob_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000458: table.sym_var("s_bob_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000470: table.sym_var("s_bob_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000488: table.sym_var("s_battlefield", "S_SCRIPT", "[]", table.GLOBL),
}

dev_E0_s_bob = {
    0x07003CA8: 0x0032D070,
    0x070041E0: 0x0032D070,
    0x070042B8: 0x0032D070,
    0x07008AF0: 0x0032D070,
    0x07008C28: 0x0032D070,
    0x07009050: 0x0032D070,
    0x07009370: 0x0032D070,
    0x07009490: 0x0032D070,
    0x070095B8: 0x0032D070,
    0x070099E0: 0x0032D070,
    0x0700A318: 0x0032D070,
    0x0700A800: 0x0032D070,
    0x0700CFC0: 0x0032D070,
    0x0700D7D8: 0x0032D070,
    0x0700D910: 0x0032D070,
    0x0700DC88: 0x0032D070,
    0x0700DCE0: 0x0032D070,
    0x0700E1E8: 0x0032D070,
    0x0700E420: 0x0032D070,
    0x0700E6C8: 0x0032D070,
    0x0700E860: 0x0032D070,
}

sym_E0_s_sl = {
    0x00405FB0: table.sym("_stage_sl_szpSegmentRomStart"),
    0x0040E840: table.sym("_stage_sl_dataSegmentRomStart"),
    0x0E000000: table.sym("p_sl_0E000000"),
    0x0E00004C: table.sym("p_sl_0E00004C"),
    0x0E000068: table.sym("p_sl_0E000068"),
    0x0E0000E4: table.sym("p_sl_0E0000E4"),
    0x0E000100: table.sym("p_sl", table.GLOBL),
    0x0E000360: table.sym_var("s_sl_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000378: table.sym_var("s_sl_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000390: table.sym_var("s_sl_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0003A8: table.sym_var("s_sl1", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000484: table.sym_var("s_sl2", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_wdw = {
    0x0040ED70: table.sym("_stage_wdw_szpSegmentRomStart"),
    0x00419F90: table.sym("_stage_wdw_dataSegmentRomStart"),
    0x0E000000: table.sym("p_wdw_0E000000"),
    0x0E0002A4: table.sym("p_wdw_0E0002A4"),
    0x0E000308: table.sym("p_wdw_0E000308"),
    0x0E00033C: table.sym("p_wdw_0E00033C"),
    0x0E000370: table.sym("p_wdw", table.GLOBL),
    0x0E000580: table.sym_var("s_wdw_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000598: table.sym_var("s_wdw_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005C0: table.sym_var("s_wdw_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005E8: table.sym_var("s_wdw_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000610: table.sym_var("s_wdw_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000628: table.sym_var("s_wdw_59", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000640: table.sym_var("s_wdw_60", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000658: table.sym_var("s_wdw1", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000724: table.sym_var("s_wdw2", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_jrb = {
    0x0041A760: table.sym("_stage_jrb_szpSegmentRomStart"),
    0x00423B20: table.sym("_stage_jrb_dataSegmentRomStart"),
    0x0E000000: table.sym("p_jrb_0E000000"),
    0x0E0001B4: table.sym("p_jrb_0E0001B4"),
    0x0E000680: table.sym("p_jrb_0E000680"),
    0x0E0006CC: table.sym("p_jrb_0E0006CC"),
    0x0E0006E8: table.sym("p_jrb_0E0006E8"),
    0x0E0006EC: table.sym("p_jrb", table.GLOBL),
    0x0E000900: table.sym_var("s_jrb_61", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000918: table.sym_var("s_jrb_62", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000930: table.sym_var("s_jrb_59", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000948: table.sym_var("s_jrb_63", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000960: table.sym_var("s_jrb_60", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000978: table.sym_var("s_jrb_53", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000990: table.sym_var("s_jrb_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009C8: table.sym_var("s_jrb_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009B0: table.sym_var("s_jrb_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009E8: table.sym_var("s_jrb_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A00: table.sym_var("s_jrb_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A18: table.sym_var("s_jrb1", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000AFC: table.sym_var("s_jrb2", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_thi = {
    0x004246D0: table.sym("_stage_thi_szpSegmentRomStart"),
    0x0042C6E0: table.sym("_stage_thi_dataSegmentRomStart"),
    0x0E000000: table.sym("p_thi_0E000000"),
    0x0E000004: table.sym("p_thi_0E000004"),
    0x0E000020: table.sym("p_thi_0E000020"),
    0x0E000054: table.sym("p_thi_0E000054"),
    0x0E000178: table.sym("p_thi_0E000178"),
    0x0E000194: table.sym("p_thi_0E000194"),
    0x0E0001C8: table.sym("p_thi_0E0001C8"),
    0x0E00022C: table.sym("p_thi_0E00022C"),
    0x0E000290: table.sym("p_thi", table.GLOBL),
    0x0E0005B0: table.sym_var("s_thi_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005C8: table.sym_var("s_thi_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005F0: table.sym_var("s_thi_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000608: table.sym_var("s_thi1", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006D4: table.sym_var("s_thi2", "S_SCRIPT", "[]", table.GLOBL),
    0x0E00079C: table.sym_var("s_thi3", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_ttc = {
    0x0042CF20: table.sym("_stage_ttc_szpSegmentRomStart"),
    0x00437400: table.sym("_stage_ttc_dataSegmentRomStart"),
    0x0E000000: table.sym("p_ttc_0E000000"),
    0x0E000034: table.sym("p_ttc_0E000034"),
    0x0E0000C8: table.sym("p_ttc", table.GLOBL),
    0x0E000240: table.sym_var("s_ttc_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000258: table.sym_var("s_ttc_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000270: table.sym_var("s_ttc_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000288: table.sym_var("s_ttc_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0002A8: table.sym_var("s_ttc_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0002C8: table.sym_var("s_ttc_59", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0002E0: table.sym_var("s_ttc_60", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0002F8: table.sym_var("s_ttc_61", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000310: table.sym_var("s_ttc_62", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000328: table.sym_var("s_ttc_63", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000340: table.sym_var("s_ttc_64", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000358: table.sym_var("s_ttc_65", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000370: table.sym_var("s_ttc_66", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000388: table.sym_var("s_ttc_67", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0003A0: table.sym_var("s_ttc_68", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0003B8: table.sym_var("s_ttc1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_rr = {
    0x00437870: table.sym("_stage_rr_szpSegmentRomStart"),
    0x0044A140: table.sym("_stage_rr_dataSegmentRomStart"),
    0x0E000000: table.sym("p_rr_0E000000"),
    0x0E0002EC: table.sym("p_rr_0E0002EC"),
    0x0E000368: table.sym("p_rr_0E000368"),
    0x0E0003E4: table.sym("p_rr", table.GLOBL),
    0x0E000660: table.sym_var("s_rr_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000678: table.sym_var("s_rr_4", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000690: table.sym_var("s_rr_5", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006A8: table.sym_var("s_rr_6", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006C0: table.sym_var("s_rr_7", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006D8: table.sym_var("s_rr_8", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006F0: table.sym_var("s_rr_9", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000708: table.sym_var("s_rr_10", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000720: table.sym_var("s_rr_11", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000738: table.sym_var("s_rr_12", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000758: table.sym_var("s_rr_13", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000770: table.sym_var("s_rr_14", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000788: table.sym_var("s_rr_15", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0007A0: table.sym_var("s_rr_16", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0007B8: table.sym_var("s_rr_17", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0007D0: table.sym_var("s_rr_18", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0007E8: table.sym_var("s_rr_19", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000800: table.sym_var("s_rr_20", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000818: table.sym_var("s_rr_21", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000830: table.sym_var("s_rr_22", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000848: table.sym_var("s_rr_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000860: table.sym_var("s_rr_62", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000878: table.sym_var("s_rr_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000890: table.sym_var("s_rr_59", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0008A8: table.sym_var("s_rr_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0008C0: table.sym_var("s_rr_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0008D8: table.sym_var("s_rr_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0008F0: table.sym_var("s_rr_64", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000908: table.sym_var("s_rr_60", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000920: table.sym_var("s_rr_63", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000940: table.sym_var("s_rr_61", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000958: table.sym_var("s_rr_65", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000970: table.sym_var("s_rr_66", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000988: table.sym_var("s_rr_67", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009A0: table.sym_var("s_rr_68", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009B8: table.sym_var("s_rr_69", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009D0: table.sym_var("s_rr1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_ground = {
    0x0044ABC0: table.sym("_stage_grounds_szpSegmentRomStart"),
    0x004545E0: table.sym("_stage_grounds_dataSegmentRomStart"),
    0x0E000000: table.sym("p_grounds_0E000000"),
    0x0E00013C: table.sym("p_grounds_0E00013C"),
    0x0E000368: table.sym("p_grounds_0E000368"),
    0x0E0003CC: table.sym("p_grounds_0E0003CC", table.GLOBL),
    0x0E000508: table.sym("p_grounds", table.GLOBL),
    0x0E000660: table.sym_var("s_grounds_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006F4: table.sym_var("s_grounds_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E00070C: table.sym_var("s_grounds_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000724: table.sym_var("s_grounds_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E00073C: table.sym_var("s_grounds1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_bitdw = {
    0x00454E00: table.sym("_stage_bitdw_szpSegmentRomStart"),
    0x0045BF60: table.sym("_stage_bitdw_dataSegmentRomStart"),
    0x0E000000: table.sym("p_bitdw_0E000000"),
    0x0E000124: table.sym("p_bitdw_0E000124"),
    0x0E000158: table.sym("p_bitdw_0E000158"),
    0x0E000174: table.sym("p_bitdw", table.GLOBL),
    0x0E0003C0: table.sym_var("s_bitdw_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0003D8: table.sym_var("s_bitdw_4", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0003F0: table.sym_var("s_bitdw_5", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000408: table.sym_var("s_bitdw_6", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000420: table.sym_var("s_bitdw_7", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000438: table.sym_var("s_bitdw_8", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000450: table.sym_var("s_bitdw_9", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000468: table.sym_var("s_bitdw_10", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000480: table.sym_var("s_bitdw_11", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000498: table.sym_var("s_bitdw_12", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004B0: table.sym_var("s_bitdw_13", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004C8: table.sym_var("s_bitdw_14", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004E0: table.sym_var("s_bitdw_15", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004F8: table.sym_var("s_bitdw_16", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000510: table.sym_var("s_bitdw_17", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000528: table.sym_var("s_bitdw_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000540: table.sym_var("s_bitdw_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000558: table.sym_var("s_bitdw_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000570: table.sym_var("s_bitdw_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000588: table.sym_var("s_bitdw_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005A0: table.sym_var("s_bitdw_59", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005B8: table.sym_var("s_bitdw_60", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005D0: table.sym_var("s_bitdw_61", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005E8: table.sym_var("s_bitdw_62", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000600: table.sym_var("s_bitdw_63", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000618: table.sym_var("s_bitdw1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_vcutm = {
    0x0045C600: table.sym("_stage_vcutm_szpSegmentRomStart"),
    0x00461220: table.sym("_stage_vcutm_dataSegmentRomStart"),
    0x0E0000B0: table.sym("p_vcutm_0E0000B0"),
    0x0E000000: table.sym("p_vcutm_0E000000"),
    0x0E000094: table.sym("p_vcutm_0E000094"),
    0x0E0000CC: table.sym("p_vcutm", table.GLOBL),
    0x0E0001F0: table.sym_var("s_vcutm_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000208: table.sym_var("s_vcutm1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_bitfs = {
    0x004614D0: table.sym("_stage_bitfs_szpSegmentRomStart"),
    0x0046A840: table.sym("_stage_bitfs_dataSegmentRomStart"),
    0x0E000000: table.sym("p_bitfs_0E000000"),
    0x0E0001CC: table.sym("p_bitfs_0E0001CC"),
    0x0E000218: table.sym("p_bitfs_0E000218"),
    0x0E000234: table.sym("p_bitfs", table.GLOBL),
    0x0E0004B0: table.sym_var("s_bitfs_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004C8: table.sym_var("s_bitfs_4", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004E0: table.sym_var("s_bitfs_5", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004F8: table.sym_var("s_bitfs_6", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000510: table.sym_var("s_bitfs_7", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000528: table.sym_var("s_bitfs_8", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000540: table.sym_var("s_bitfs_9", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000558: table.sym_var("s_bitfs_10", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000570: table.sym_var("s_bitfs_11", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000588: table.sym_var("s_bitfs_12", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005A0: table.sym_var("s_bitfs_13", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005B8: table.sym_var("s_bitfs_14", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005D0: table.sym_var("s_bitfs_15", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005E8: table.sym_var("s_bitfs_16", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000600: table.sym_var("s_bitfs_17", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000618: table.sym_var("s_bitfs_18", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000630: table.sym_var("s_bitfs_19", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000648: table.sym_var("s_bitfs_20", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000660: table.sym_var("s_bitfs_21", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000678: table.sym_var("s_bitfs_59", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000690: table.sym_var("s_bitfs_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006A8: table.sym_var("s_bitfs_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006C0: table.sym_var("s_bitfs_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006D8: table.sym_var("s_bitfs_64", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006F0: table.sym_var("s_bitfs_65", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000708: table.sym_var("s_bitfs_60", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000728: table.sym_var("s_bitfs_62", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000740: table.sym_var("s_bitfs_63", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000758: table.sym_var("s_bitfs_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000770: table.sym_var("s_bitfs_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000788: table.sym_var("s_bitfs_61", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0007A0: table.sym_var("s_bitfs1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_sa = {
    0x0046B090: table.sym("_stage_sa_szpSegmentRomStart"),
    0x0046C1A0: table.sym("_stage_sa_dataSegmentRomStart"),
    0x0E000000: table.sym("p_sa_0E000000"),
    0x0E000034: table.sym("p_sa_0E000034"),
    0x0E000050: table.sym("p_sa", table.GLOBL),
    0x0E000170: table.sym_var("s_sa1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_bits = {
    0x0046C3A0: table.sym("_stage_bits_szpSegmentRomStart"),
    0x00477D00: table.sym("_stage_bits_dataSegmentRomStart"),
    0x0700B4A0: table.sym("0x0700B4A0"),
    0x0E000000: table.sym("p_bits_0E000000"),
    0x0E0001CC: table.sym("p_bits_0E0001CC"),
    0x0E0001E8: table.sym("p_bits", table.GLOBL),
    0x0E000430: table.sym_var("s_bits_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000448: table.sym_var("s_bits_4", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000460: table.sym_var("s_bits_5", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000478: table.sym_var("s_bits_6", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000490: table.sym_var("s_bits_7", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004A8: table.sym_var("s_bits_8", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004C0: table.sym_var("s_bits_9", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004D8: table.sym_var("s_bits_10", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004F0: table.sym_var("s_bits_11", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000508: table.sym_var("s_bits_12", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000520: table.sym_var("s_bits_13", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000538: table.sym_var("s_bits_14", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000550: table.sym_var("s_bits_15", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000568: table.sym_var("s_bits_16", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000580: table.sym_var("s_bits_17", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000598: table.sym_var("s_bits_18", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005B0: table.sym_var("s_bits_19", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005C8: table.sym_var("s_bits_20", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005E0: table.sym_var("s_bits_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0005F8: table.sym_var("s_bits_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000610: table.sym_var("s_bits_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000628: table.sym_var("s_bits_60", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000640: table.sym_var("s_bits_61", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000658: table.sym_var("s_bits_62", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000670: table.sym_var("s_bits_63", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000688: table.sym_var("s_bits_64", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006A0: table.sym_var("s_bits_65", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006B8: table.sym_var("s_bits_66", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006D0: table.sym_var("s_bits_67", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0006E8: table.sym_var("s_bits_68", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000700: table.sym_var("s_bits_69", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000718: table.sym_var("s_bits1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_lll = {
    0x004784A0: table.sym("_stage_lll_szpSegmentRomStart"),
    0x0048C9B0: table.sym("_stage_lll_dataSegmentRomStart"),
    0x0E000000: table.sym("p_lll_0E000000"),
    0x0E000154: table.sym("p_lll_0E000154"),
    0x0E000290: table.sym("p_lll_0E000290"),
    0x0E000324: table.sym("p_lll_0E000324"),
    0x0E0004C0: table.sym("p_lll_0E0004C0"),
    0x0E0004F4: table.sym("p_lll_0E0004F4"),
    0x0E000648: table.sym("p_lll_0E000648"),
    0x0E00067C: table.sym("p_lll", table.GLOBL),
    0x0E0009E0: table.sym_var("s_lll_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009F8: table.sym_var("s_lll_4", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A10: table.sym_var("s_lll_5", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A28: table.sym_var("s_lll_6", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A40: table.sym_var("s_lll_7", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A60: table.sym_var("s_lll_8", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A78: table.sym_var("s_lll_9", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A90: table.sym_var("s_lll_10", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000AA8: table.sym_var("s_lll_11", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000AC0: table.sym_var("s_lll_12", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000AD8: table.sym_var("s_lll_13", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000AF0: table.sym_var("s_lll_14", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B08: table.sym_var("s_lll_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B20: table.sym_var("s_lll_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B38: table.sym_var("s_lll_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B50: table.sym_var("s_lll_53", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B68: table.sym_var("s_lll_59", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B80: table.sym_var("s_lll_60", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B98: table.sym_var("s_lll_61", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000BB0: table.sym_var("s_lll_62", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000BC8: table.sym_var("s_lll_63", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000BE0: table.sym_var("s_lll_64", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000BF8: table.sym_var("s_lll_65", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000C10: table.sym_var("s_lll_67", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000C30: table.sym_var("s_lll_68", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000C50: table.sym_var("s_lll_69", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000C70: table.sym_var("s_lll_70", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000C90: table.sym_var("s_lll_71", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000CB0: table.sym_var("s_lll_72", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000CD0: table.sym_var("s_lll_73", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000CF0: table.sym_var("s_lll_74", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000D10: table.sym_var("s_lll_75", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000D30: table.sym_var("s_lll_76", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000D50: table.sym_var("s_lll_77", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000D70: table.sym_var("s_lll_78", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000D90: table.sym_var("s_lll_79", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000DB0: table.sym_var("s_lll_80", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000DD0: table.sym_var("s_lll_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000DE8: table.sym_var("s_lll_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000E00: table.sym_var("s_lll1", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000EA8: table.sym_var("s_lll_83", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000EC0: table.sym_var("s_lll2", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_ddd = {
    0x0048D930: table.sym("_stage_ddd_szpSegmentRomStart"),
    0x00495A60: table.sym("_stage_ddd_dataSegmentRomStart"),
    0x0E000000: table.sym("p_ddd_0E000000"),
    0x0E0000AC: table.sym("p_ddd_0E0000AC"),
    0x0E0000E0: table.sym("p_ddd_0E0000E0"),
    0x0E0001EC: table.sym("p_ddd_0E0001EC"),
    0x0E000208: table.sym("p_ddd_0E000208"),
    0x0E00026C: table.sym("p_ddd", table.GLOBL),
    0x0E000450: table.sym_var("s_ddd_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000478: table.sym_var("s_ddd_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004A0: table.sym_var("s_ddd_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0004C0: table.sym_var("s_ddd1", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000570: table.sym_var("s_ddd2", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_wf = {
    0x00496090: table.sym("_stage_wf_szpSegmentRomStart"),
    0x0049DA50: table.sym("_stage_wf_dataSegmentRomStart"),
    0x0E000000: table.sym("p_wf_0E000000"),
    0x0E0000DC: table.sym("p_wf_0E0000DC"),
    0x0E000260: table.sym("p_wf_0E000260"),
    0x0E0004D4: table.sym("p_wf_0E0004D4"),
    0x0E000568: table.sym("p_wf", table.GLOBL),
    0x0E0007E0: table.sym_var("s_wf_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000820: table.sym_var("s_wf_4", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000860: table.sym_var("s_wf_5", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000878: table.sym_var("s_wf_6", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000890: table.sym_var("s_wf_7", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0008A8: table.sym_var("s_wf_8", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0008E8: table.sym_var("s_wf_9", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000900: table.sym_var("s_wf_10", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000940: table.sym_var("s_wf_12", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000958: table.sym_var("s_wf_14", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009A0: table.sym_var("s_wf_15", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009B8: table.sym_var("s_wf_16", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009D0: table.sym_var("s_wf_17", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009E8: table.sym_var("s_wf_18", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A00: table.sym_var("s_wf_174", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A40: table.sym_var("s_wf_177", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A58: table.sym_var("s_wf_175", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A98: table.sym_var("s_wf_173", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000AB0: table.sym_var("s_wf_176", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000AC8: table.sym_var("s_wf_178", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000AE0: table.sym_var("s_wf_13", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000AF8: table.sym_var("s_wf_44", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B10: table.sym_var("s_wf_45", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B38: table.sym_var("s_wf_46", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B60: table.sym_var("s_wf_47", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B78: table.sym_var("s_wf_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B90: table.sym_var("s_wf_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000BA8: table.sym_var("s_wf_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000BC8: table.sym_var("s_wf_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000BE0: table.sym_var("s_wf_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000BF8: table.sym_var("s_wf1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_ending = {
    0x0049E710: table.sym("_stage_ending_szpSegmentRomStart"),
    0x004AC4B0: table.sym("_stage_ending_dataSegmentRomStart"),
    0x0E000000: table.sym("p_ending", table.GLOBL),
    0x0E000044: table.sym(".loop", table.LOCAL),
    0x0E000050: table.sym_var("s_ending1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_courty = {
    0x004AC570: table.sym("_stage_courtyard_szpSegmentRomStart"),
    0x004AF670: table.sym("_stage_courtyard_dataSegmentRomStart"),
    0x0E000000: table.sym("p_courtyard_0E000000"),
    0x0E00004C: table.sym("p_courtyard_0E00004C"),
    0x0E000098: table.sym("p_courtyard", table.GLOBL),
    0x0E000200: table.sym_var("s_courtyard_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000218: table.sym_var("s_courtyard1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_pss = {
    0x004AF930: table.sym("_stage_pss_szpSegmentRomStart"),
    0x004B7F10: table.sym("_stage_pss_dataSegmentRomStart"),
    0x0E000000: table.sym("p_pss", table.GLOBL),
    0x0E000100: table.sym_var("s_pss1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_cotmc = {
    0x004B80D0: table.sym("_stage_cotmc_szpSegmentRomStart"),
    0x004BE9E0: table.sym("_stage_cotmc_dataSegmentRomStart"),
    0x0E000000: table.sym("p_cotmc_0E000000"),
    0x0E00004C: table.sym("p_cotmc_0E00004C"),
    0x0E000068: table.sym("p_cotmc", table.GLOBL),
    0x0E0001A0: table.sym_var("s_cotmc1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_totwc = {
    0x004BEC30: table.sym("_stage_totwc_szpSegmentRomStart"),
    0x004C2700: table.sym("_stage_totwc_dataSegmentRomStart"),
    0x0E000000: table.sym("p_totwc_0E000000"),
    0x0E00001C: table.sym("p_totwc_0E00001C"),
    0x0E000038: table.sym("p_totwc", table.GLOBL),
    0x0E000160: table.sym_var("s_totwc_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000188: table.sym_var("s_totwc1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_bitdwa = {
    0x004C2920: table.sym("_stage_bitdwa_szpSegmentRomStart"),
    0x004C41C0: table.sym("_stage_bitdwa_dataSegmentRomStart"),
    0x0E000000: table.sym("p_bitdwa", table.GLOBL),
    0x0E0000D0: table.sym_var("s_bitdwa1", "S_SCRIPT", "[]", table.GLOBL),
}

dev_E0_s_bitdwa = {
    0x004C420C: 0x00188440,
}

sym_E0_s_wmotr = {
    0x004C4320: table.sym("_stage_wmotr_szpSegmentRomStart"),
    0x004CD930: table.sym("_stage_wmotr_dataSegmentRomStart"),
    0x0E000000: table.sym("p_wmotr_0E000000"),
    0x0E000094: table.sym("p_wmotr_0E000094"),
    0x0E0000B0: table.sym("p_wmotr", table.GLOBL),
    0x0E0001F0: table.sym_var("s_wmotr1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_bitfsa = {
    0x004CDBD0: table.sym("_stage_bitfsa_szpSegmentRomStart"),
    0x004CE9F0: table.sym("_stage_bitfsa_dataSegmentRomStart"),
    0x0E000000: table.sym("p_bitfsa_0E000000"),
    0x0E00007C: table.sym("p_bitfsa", table.GLOBL),
    0x0E000170: table.sym_var("s_bitfsa_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000188: table.sym_var("s_bitfsa1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_bitsa = {
    0x004CEC00: table.sym("_stage_bitsa_szpSegmentRomStart"),
    0x004D14F0: table.sym("_stage_bitsa_dataSegmentRomStart"),
    0x0E000000: table.sym("p_bitsa_0E000000"),
    0x0E00016C: table.sym("p_bitsa", table.GLOBL),
    0x0E000290: table.sym_var("s_bitsa_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0002A8: table.sym_var("s_bitsa_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0002C0: table.sym_var("s_bitsa_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0002D8: table.sym_var("s_bitsa_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0002F0: table.sym_var("s_bitsa_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000308: table.sym_var("s_bitsa_59", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000320: table.sym_var("s_bitsa_60", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000338: table.sym_var("s_bitsa_61", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000350: table.sym_var("s_bitsa_62", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000368: table.sym_var("s_bitsa_63", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000380: table.sym_var("s_bitsa_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000398: table.sym_var("s_bitsa1", "S_SCRIPT", "[]", table.GLOBL),
}

sym_E0_s_ttm = {
    0x004D1910: table.sym("_stage_ttm_szpSegmentRomStart"),
    0x004EB1F0: table.sym("_stage_ttm_dataSegmentRomStart"),
    0x0E000000: table.sym("p_ttm_0E000000"),
    0x0E00001C: table.sym("p_ttm_0E00001C"),
    0x0E0001B8: table.sym("p_ttm_0E0001B8"),
    0x0E00024C: table.sym("p_ttm_0E00024C"),
    0x0E0002B0: table.sym("p_ttm_0E0002B0"),
    0x0E000344: table.sym("p_ttm_0E000344"),
    0x0E000390: table.sym("p_ttm_0E000390"),
    0x0E000394: table.sym("p_ttm", table.GLOBL),
    0x0E000710: table.sym_var("s_ttm_54", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000730: table.sym_var("s_ttm_53", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000748: table.sym_var("s_ttm_3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000778: table.sym_var("s_ttm_4", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0007A8: table.sym_var("s_ttm_5", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0007D8: table.sym_var("s_ttm_6", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000808: table.sym_var("s_ttm_7", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000830: table.sym_var("s_ttm_8", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000858: table.sym_var("s_ttm_9", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000880: table.sym_var("s_ttm_10", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0008A8: table.sym_var("s_ttm_11", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0008D0: table.sym_var("s_ttm_12", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0008F8: table.sym_var("s_ttm_13", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000920: table.sym_var("s_ttm_15", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000948: table.sym_var("s_ttm_16", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000970: table.sym_var("s_ttm_17", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000990: table.sym_var("s_ttm_18", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009C0: table.sym_var("s_ttm_19", "S_SCRIPT", "[]", table.GLOBL),
    0x0E0009F0: table.sym_var("s_ttm_20", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A18: table.sym_var("s_ttm_21", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A40: table.sym_var("s_ttm_22", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000A70: table.sym_var("s_ttm1", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000B5C: table.sym_var("s_ttm2", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000BEC: table.sym_var("s_ttm3", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000C84: table.sym_var("s_ttm4", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000D14: table.sym_var("s_ttm_55", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000D4C: table.sym_var("s_ttm_56", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000D84: table.sym_var("s_ttm_57", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000DBC: table.sym_var("s_ttm_58", "S_SCRIPT", "[]", table.GLOBL),
    0x0E000DF4: table.sym_var("s_ttm_123", "S_SCRIPT", "[]", table.GLOBL),
}

tbl = [
    (0x00000040, 0x00001000, "E0", sym_E0_t_ipl3,   {}, {}),
    (0x00001000, 0x00001050, "E0", sym_E0_t_crt0,   {}, imm_E0_t_crt0),
    (0x00001050, 0x000DD370, "E0", sym_E0_t_main, dev_E0_t_main, imm_E0_t_main),
    (0x000DD370, 0x000E6260, "E0", sym_E0_t_ultra,  {}, {}),
    (0x000E6260, 0x000E6330, "E0", sym_E0_t_spboot, {}, imm_E0_t_spboot),
    (0x000E6330, 0x000E7318, "E0", sym_E0_t_gF3D_0, {}, {}),
    (0x000E7318, 0x000E7538, "E0", sym_E0_t_gF3D_2, {}, {}),
    (0x000E7538, 0x000E76D0, "E0", sym_E0_t_gF3D_3, {}, {}),
    (0x000E76D0, 0x000E7740, "E0", sym_E0_t_gF3D_4, {}, imm_E0_t_gF3D_4),
    (0x000E7740, 0x000E8560, "E0", sym_E0_t_aMain,  {}, {}),
    (0x000E8560, 0x000F0010, "E0", sym_E0_d_main,   dev_E0_d_main, {}),
    (0x000F0010, 0x000F0B60, "E0", sym_E0_d_ultra,  {}, {}),
    (0x000F0B60, 0x000F47B0, "E0", sym_E0_d_main,   {}, {}),
    (0x000F47B0, 0x000F4AC0, "E0", sym_E0_d_ultra,  {}, {}),
    (0x000F4AC0, 0x000F52C0, "E0", sym_E0_d_gF3D,   {}, {}),
    (0x000F52C0, 0x000F5580, "E0", sym_E0_d_aMain,  {}, {}),
    (0x000F5580, 0x00102D10, "E0", sym_E0_t_main2,  {}, {}),
    (0x00102D10, 0x00108A10, "E0", sym_E0_d_main2,  {}, {}),
    (0x00108A10, 0x00114750, "E0", sym_E0_main,     {}, {}),
    (0x00114750, 0x0012A7E0, "E0", sym_E0_shp_pl,   {}, {}),
    (0x0012A7E0, 0x00132C60, "E0", sym_E0_shp_1a,   {}, {}),
    (0x00132C60, 0x00134D20, "E0", sym_E0_shp_1b,   {}, imm_E0_shp_1b),
    (0x00134D20, 0x0013B910, "E0", sym_E0_shp_1c,   {}, {}),
    (0x0013B910, 0x00145E90, "E0", sym_E0_shp_1d,   {}, {}),
    (0x00145E90, 0x001521D0, "E0", sym_E0_shp_1e,   {}, {}),
    (0x001521D0, 0x00160670, "E0", sym_E0_shp_1f,   {}, {}),
    (0x00160670, 0x00165A50, "E0", sym_E0_shp_1g,   {}, {}),
    (0x00165A50, 0x00166C60, "E0", sym_E0_shp_1h,   {}, {}),
    (0x00166C60, 0x0016D870, "E0", sym_E0_shp_1i,   {}, {}),
    (0x0016D870, 0x00180BB0, "E0", sym_E0_shp_1j,   {}, {}),
    (0x00180BB0, 0x00188440, "E0", sym_E0_shp_1k,   {}, {}),
    (0x00188440, 0x001B9CC0, "E0", sym_E0_shp_2a,   {}, {}),
    (0x001B9CC0, 0x001C4230, "E0", sym_E0_shp_2b,   {}, {}),
    (0x001C4230, 0x001D8310, "E0", sym_E0_shp_2c,   {}, {}),
    (0x001D8310, 0x001E51F0, "E0", sym_E0_shp_2d,   {}, {}),
    (0x001E51F0, 0x001E7EE0, "E0", sym_E0_shp_2e,   {}, {}),
    (0x001E7EE0, 0x001F2200, "E0", sym_E0_shp_2f,   {}, {}),
    (0x001F2200, 0x00201410, "E0", sym_E0_shp_3a,   {}, {}),
    (0x00201410, 0x00219E00, "E0", sym_E0_shp_gl,   {}, imm_E0_shp_gl),
    (0x00219E00, 0x0021F4C0, "E0", sym_E0_object,   {}, {}),
    (0x0021F4C0, 0x00257CF0, "E0", sym_E0_t_menu,   {}, {}),
    (0x00257CF0, 0x00269EA0, "E0", sym_E0_d_menu,   {}, {}),
    (0x00269EA0, 0x0026F420, "E0", sym_E0_m_title,  {}, {}),
    (0x0026F420, 0x002708C0, "E0", sym_E0_m_debug,  {}, imm_E0_m_debug),
    (0x002708C0, 0x002739A0, "E0", sym_E0_bg_title, {}, {}),
    (0x002739A0, 0x002A6120, "E0", sym_E0_d_face,   {}, {}),
    (0x002A6120, 0x002ABCA0, "E0", sym_E0_m_select, {}, {}),
    (0x002ABCA0, 0x002AC6B0, "E0", sym_E0_game,     dev_E0_game, {}),
    (0x002AC6B0, 0x002B8F10, "E0", sym_E0_bg_a,     {}, {}),
    (0x002B8F10, 0x002C73D0, "E0", sym_E0_bg_b,     {}, {}),
    (0x002C73D0, 0x002D0040, "E0", sym_E0_bg_c,     {}, {}),
    (0x002D0040, 0x002D64F0, "E0", sym_E0_bg_d,     {}, {}),
    (0x002D64F0, 0x002E7880, "E0", sym_E0_bg_e,     {}, {}),
    (0x002E7880, 0x002F14E0, "E0", sym_E0_bg_f,     {}, {}),
    (0x002F14E0, 0x002FB1B0, "E0", sym_E0_bg_g,     {}, {}),
    (0x002FB1B0, 0x00301CD0, "E0", sym_E0_bg_h,     {}, {}),
    (0x00301CD0, 0x0030CEC0, "E0", sym_E0_bg_i,     {}, {}),
    (0x0030CEC0, 0x0031E1D0, "E0", sym_E0_bg_j,     {}, {}),
    (0x0031E1D0, 0x00326E40, "E0", sym_E0_txt_a,    {}, {}),
    (0x00326E40, 0x0032D070, "E0", sym_E0_txt_b,    {}, {}),
    (0x0032D070, 0x00334B30, "E0", sym_E0_txt_c,    {}, {}),
    (0x00334B30, 0x0033D710, "E0", sym_E0_txt_d,    {}, {}),
    (0x0033D710, 0x00341140, "E0", sym_E0_txt_e,    {}, {}),
    (0x00341140, 0x00347A50, "E0", sym_E0_txt_f,    {}, {}),
    (0x00347A50, 0x0034E760, "E0", sym_E0_txt_g,    {}, {}),
    (0x0034E760, 0x00351960, "E0", sym_E0_txt_h,    {}, {}),
    (0x00351960, 0x00357350, "E0", sym_E0_txt_i,    {}, {}),
    (0x00357350, 0x0035ED10, "E0", sym_E0_txt_j,    {}, {}),
    (0x0035ED10, 0x00365980, "E0", sym_E0_txt_k,    {}, {}),
    (0x00365980, 0x0036F530, "E0", sym_E0_txt_l,    {}, {}),
    (0x0036F530, 0x00371C40, "E0", sym_E0_weather,  {}, {}),
    (0x00371C40, 0x00383950, "E0", sym_E0_s_bbh,    {}, {}),
    (0x00383950, 0x00396340, "E0", sym_E0_s_ccm,    {}, {}),
    (0x00396340, 0x003D0DC0, "E0", sym_E0_s_inside, {}, {}),
    (0x003D0DC0, 0x003E76B0, "E0", sym_E0_s_hmc,    {}, {}),
    (0x003E76B0, 0x003FC2B0, "E0", sym_E0_s_ssl,    {}, {}),
    (0x003FC2B0, 0x00405FB0, "E0", sym_E0_s_bob,    dev_E0_s_bob, {}),
    (0x00405FB0, 0x0040ED70, "E0", sym_E0_s_sl,     {}, {}),
    (0x0040ED70, 0x0041A760, "E0", sym_E0_s_wdw,    {}, {}),
    (0x0041A760, 0x004246D0, "E0", sym_E0_s_jrb,    {}, {}),
    (0x004246D0, 0x0042CF20, "E0", sym_E0_s_thi,    {}, {}),
    (0x0042CF20, 0x00437870, "E0", sym_E0_s_ttc,    {}, {}),
    (0x00437870, 0x0044ABC0, "E0", sym_E0_s_rr,     {}, {}),
    (0x0044ABC0, 0x00454E00, "E0", sym_E0_s_ground, {}, {}),
    (0x00454E00, 0x0045C600, "E0", sym_E0_s_bitdw,  {}, {}),
    (0x0045C600, 0x004614D0, "E0", sym_E0_s_vcutm,  {}, {}),
    (0x004614D0, 0x0046B090, "E0", sym_E0_s_bitfs,  {}, {}),
    (0x0046B090, 0x0046C3A0, "E0", sym_E0_s_sa,     {}, {}),
    (0x0046C3A0, 0x004784A0, "E0", sym_E0_s_bits,   {}, {}),
    (0x004784A0, 0x0048D930, "E0", sym_E0_s_lll,    {}, {}),
    (0x0048D930, 0x00496090, "E0", sym_E0_s_ddd,    {}, {}),
    (0x00496090, 0x0049E710, "E0", sym_E0_s_wf,     {}, {}),
    (0x0049E710, 0x004AC570, "E0", sym_E0_s_ending, {}, {}),
    (0x004AC570, 0x004AF930, "E0", sym_E0_s_courty, {}, {}),
    (0x004AF930, 0x004B80D0, "E0", sym_E0_s_pss,    {}, {}),
    (0x004B80D0, 0x004BEC30, "E0", sym_E0_s_cotmc,  {}, {}),
    (0x004BEC30, 0x004C2920, "E0", sym_E0_s_totwc,  {}, {}),
    (0x004C2920, 0x004C4320, "E0", sym_E0_s_bitdwa, dev_E0_s_bitdwa, {}),
    (0x004C4320, 0x004CDBD0, "E0", sym_E0_s_wmotr,  {}, {}),
    (0x004CDBD0, 0x004CEC00, "E0", sym_E0_s_bitfsa, {}, {}),
    (0x004CEC00, 0x004D1910, "E0", sym_E0_s_bitsa,  {}, {}),
    (0x004D1910, 0x004EC000, "E0", sym_E0_s_ttm,    {}, {}),
]
