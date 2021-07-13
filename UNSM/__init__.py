import os
import struct

import main
import table
import ultra

fmt_bool = ["false", "true"]

fmt_glayer = (
    "G_LAYER_BACKGROUND",
    "G_LAYER_OPA_SURF",
    "G_LAYER_OPA_DECAL",
    "G_LAYER_OPA_INTER",
    "G_LAYER_TEX_EDGE",
    "G_LAYER_XLU_SURF",
    "G_LAYER_XLU_DECAL",
    "G_LAYER_XLU_INTER",
)

fmt_otype = [
    "O_TYPE_PLAYER",
    "O_TYPE_1",
    "O_TYPE_PLAYERATTACK",
    "O_TYPE_3",
    "O_TYPE_OBJECTA",
    "O_TYPE_OBJECTB",
    "O_TYPE_ITEM",
    "O_TYPE_7",
    "O_TYPE_DEFAULT",
    "O_TYPE_MOVEBG",
    "O_TYPE_PLAYERUSE",
    "O_TYPE_SYSTEM",
    "O_TYPE_PARTICLE",
]

shp_game = {
    1: "MARIO",
    116: "ENTITY_116",
    117: "ENTITY_117",
    118: "ENTITY_118",
    119: "ENTITY_119",
    121: "ENTITY_121",
    122: "ENTITY_122",
    124: "ENTITY_124",
    133: "ENTITY_133",
    134: "ENTITY_134",
    135: "ENTITY_135",
    136: "ENTITY_136",
    138: "ENTITY_138",
    139: "ENTITY_139",
    142: "ENTITY_142",
    143: "GLOW",
    144: "ENTITY_144",
    145: "ENTITY_145",
    148: "SMOKE",
    149: "SPARKLE",
    150: "DUST",
    156: "SMOKE2",
    158: "ENTITY_158",
    159: "ENTITY_159",
    160: "ENTITY_160",
    161: "ENTITY_161",
    162: "ENTITY_162",
    163: "RIPPLE_MOVE",
    164: "DROPLET_WHITE",
    165: "WAVE_WHITE",
    166: "RIPPLE_STOP",
    167: "SPLASH",
    168: "BUBBLE_A",
    170: "BUBBLE_B",
    185: "ENTITY_185",
    186: "ENTITY_186",
    187: "ENTITY_187",
    200: "ENTITY_200",
    203: "ENTITY_203",
    204: "ENTITY_204",
    205: "ENTITY_205",
    212: "ENTITY_212",
    215: "ENTITY_215",
    216: "ENTITY_216",
    219: "DIGIT",
    224: "ENTITY_224",
}

shp_c0 = {
    120: "C0_120",
    127: "C0_127",
    128: "C0_128",
    129: "C0_129",
    130: "C0_130",
    131: "C0_131",
    132: "C0_132",
    137: "C0_137",
    140: "C0_140",
    180: "C0_180",
    188: "C0_188",
    190: "C0_190",
    192: "C0_192",
    194: "C0_194",
    195: "C0_195",
    201: "C0_201",
    202: "C0_202",
    207: "C0_207",
    217: "C0_217",
    218: "C0_218",
    220: "C0_220",
    223: "C0_223",
    225: "C0_225",
}

shp_a0 = {
    84: "A0_84",
    85: "A0_85",
    86: "A0_86",
    87: "A0_87",
    88: "A0_88",
    89: "A0_89",
}

shp_a1 = {
    84: "A1_84",
    86: "A1_86",
    87: "A1_87",
}

shp_a2 = {
    84: "A2_84",
    85: "A2_85",
    86: "A2_86",
}

shp_a3 = {
    84: "A3_84",
    85: "A3_85",
    86: "A3_86",
    87: "A3_87",
    88: "A3_88",
}

shp_a4 = {
    84: "A4_84",
    85: "A4_85",
    86: "A4_86",
    87: "A4_87",
    88: "A4_88",
    89: "A4_89",
}

shp_a5 = {
    84: "A5_84",
    85: "A5_85",
    86: "A5_86",
    87: "A5_87",
}

shp_a6 = {
    84: "A6_84",
    85: "A6_85",
    86: "A6_86",
    87: "A6_87",
}

shp_a7 = {
    84: "A7_84",
    85: "A7_85",
    86: "A7_86",
}

shp_a8 = {
    84: "A8_84",
    85: "A8_85",
    86: "A8_86",
    87: "A8_87",
    88: "A8_88",
    89: "A8_89",
    90: "A8_90",
}

shp_a9 = {
    84: "A9_84",
    85: "A9_85",
    222: "A9_222",
}

shp_a10 = {
    84: "A10_84",
    85: "A10_85",
    86: "A10_86",
    87: "A10_87",
    88: "A10_88",
    89: "A10_89",
}

shp_b0 = {
    100: "B0_100",
    101: "B0_101",
    102: "B0_102",
    103: "B0_103",
    104: "B0_104",
    105: "B0_105",
    179: "B0_179",
}

shp_b1 = {
    100: "B1_100",
    101: "B1_101",
    102: "B1_102",
    103: "B1_103",
    104: "B1_104",
    105: "B1_105",
    179: "B1_179",
    193: "B1_193",
}

shp_b2 = {
    100: "B2_100",
    101: "B2_101",
    102: "B2_102",
    103: "B2_103",
    104: "B2_104",
    106: "B2_106",
    107: "B2_107",
    191: "B2_191",
}

shp_b3 = {
    100: "B3_100",
    101: "B3_101",
    102: "B3_102",
    221: "B3_221",
}

shp_b4 = {
    100: "B4_100",
    101: "B4_101",
    102: "B4_102",
}

shp_b5 = {
    100: "B5_100",
    101: "B5_101",
    102: "B5_102",
    103: "B5_103",
    104: "B5_104",
    206: "B5_206",
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
    29: "ENTITY_29",
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
    25: "ENTITY_25",
    39: "ENTITY_39",
    54: "CCM_54",
    55: "CCM_55",
    210: "CCM_210",
}

shp_inside = {
    28: "ENTITY_28",
    29: "ENTITY_29",
    34: "ENTITY_34",
    35: "ENTITY_35",
    36: "ENTITY_36",
    37: "ENTITY_37",
    38: "ENTITY_38",
    39: "ENTITY_39",
    41: "ENTITY_41",
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
    29: "ENTITY_29",
    31: "ENTITY_31",
    32: "ENTITY_32",
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
    27: "ENTITY_27",
    54: "SSL_54",
    55: "SSL_55",
    56: "SSL_56",
    57: "SSL_57",
    58: "SSL_58",
    199: "SSL_199",
}

shp_bob = {
    23: "ENTITY_23",
    54: "BOB_54",
    55: "BOB_55",
    56: "BOB_56",
}

shp_sl = {
    25: "ENTITY_25",
    54: "SL_54",
    55: "SL_55",
    56: "SL_56",
}

shp_wdw = {
    23: "ENTITY_23",
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
    22: "ENTITY_22",
    23: "ENTITY_23",
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
    22: "ENTITY_22",
    23: "ENTITY_23",
    38: "ENTITY_38",
    41: "ENTITY_41",
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
    18: "ENTITY_18",
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
    22: "ENTITY_22",
    54: "VCUTM_54",
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
    73: "ENTITY_73",
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
    23: "ENTITY_23",
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

shp_end = {
}

shp_courty = {
    3: "COURTYARD_3",
    24: "ENTITY_24",
    39: "ENTITY_39",
}

shp_pss = {
}

shp_cotmc = {
}

shp_totwc = {
    3: "TOTWC_3",
}

shp_bitdwa = {
    3: "B0_3",
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
    (0x002A6120, 0x002ABCA0, shp_select),
    (0x002ABCA0, 0x002AC300, shp_game,),
    (0x002AC300, 0x002AC3BC, shp_c0,),
    (0x002AC3BC, 0x002AC3F0, shp_a0,),
    (0x002AC3F0, 0x002AC40C, shp_a1,),
    (0x002AC40C, 0x002AC428, shp_a2,),
    (0x002AC428, 0x002AC454, shp_a3,),
    (0x002AC454, 0x002AC488, shp_a4,),
    (0x002AC488, 0x002AC4AC, shp_a5,),
    (0x002AC4AC, 0x002AC4EC, shp_a6,),
    (0x002AC4D0, 0x002AC4EC, shp_a7,),
    (0x002AC4EC, 0x002AC528, shp_a8,),
    (0x002AC528, 0x002AC544, shp_a9,),
    (0x002AC544, 0x002AC578, shp_a10,),
    (0x002AC578, 0x002AC5B4, shp_b0,),
    (0x002AC5B4, 0x002AC5F8, shp_b1,),
    (0x002AC5F8, 0x002AC63C, shp_b2,),
    (0x002AC63C, 0x002AC660, shp_b3,),
    (0x002AC660, 0x002AC67C, shp_b4,),
    (0x002AC67C, 0x002AC6B0, shp_b5,),
    (0x00371C40, 0x00383950, shp_game, shp_c0, shp_a8,  shp_b5, shp_bbh),
    (0x00383950, 0x00396340, shp_game, shp_c0, shp_a6,  shp_b4, shp_ccm),
    (0x00396340, 0x003D0DC0, shp_game,                  shp_b3, shp_inside),
    (0x003D0DC0, 0x003E76B0, shp_game, shp_c0, shp_a5,  shp_b5, shp_hmc),
    (0x003E76B0, 0x003FC2B0, shp_game, shp_c0, shp_a4,          shp_ssl),
    (0x003FC2B0, 0x00405FB0, shp_game, shp_c0, shp_a2,  shp_b2, shp_bob),
    (0x00405FB0, 0x0040ED70, shp_game, shp_c0, shp_a6,  shp_b4, shp_sl),
    (0x0040ED70, 0x0041A760, shp_game, shp_c0, shp_a0,  shp_b1, shp_wdw),
    (0x0041A760, 0x004246D0, shp_game, shp_c0, shp_a3,  shp_b1, shp_jrb),
    (0x004246D0, 0x0042CF20, shp_game, shp_c0, shp_a10, shp_b2, shp_thi),
    (0x0042CF20, 0x00437870, shp_game, shp_c0, shp_a0,          shp_ttc),
    (0x00437870, 0x0044ABC0, shp_game, shp_c0, shp_a10,         shp_rr),
    (0x0044ABC0, 0x00454E00, shp_game, shp_c0, shp_a9,  shp_b3, shp_ground),
    (0x00454E00, 0x0045C600, shp_game, shp_c0, shp_a10, shp_b5, shp_bitdw),
    (0x0045C600, 0x004614D0, shp_game, shp_c0, shp_a7,          shp_vcutm),
    (0x004614D0, 0x0046B090, shp_game, shp_c0, shp_a1,  shp_b5, shp_bitfs),
    (0x0046B090, 0x0046C3A0, shp_game,         shp_a3,  shp_b1, shp_sa),
    (0x0046C3A0, 0x004784A0, shp_game, shp_c0,          shp_b2, shp_bits),
    (0x004784A0, 0x0048D930, shp_game, shp_c0, shp_a1,  shp_b5, shp_lll),
    (0x0048D930, 0x00496090, shp_game, shp_c0, shp_a3,  shp_b1, shp_ddd),
    (0x00496090, 0x0049E710, shp_game, shp_c0, shp_a0,  shp_b2, shp_wf),
    (0x0049E710, 0x004AC570, shp_game,                          shp_end),
    (0x004AC570, 0x004AF930, shp_game, shp_c0, shp_a8,          shp_courty),
    (0x004AF930, 0x004B80D0, shp_game, shp_c0, shp_a7,          shp_pss),
    (0x004B80D0, 0x004BEC30, shp_game, shp_c0, shp_a7,  shp_b5, shp_cotmc),
    (0x004BEC30, 0x004C2920, shp_game, shp_c0, shp_a7,          shp_totwc),
    (0x004C2920, 0x004C4320, shp_game,                  shp_b0, shp_bitdwa),
    (0x004C4320, 0x004CDBD0, shp_game, shp_c0, shp_a1,  shp_b5, shp_wmotr),
    (0x004CDBD0, 0x004CEC00, shp_game,                  shp_b0, shp_bitfsa),
    (0x004CEC00, 0x004D1910, shp_game,                  shp_b0, shp_bitsa),
    (0x004D1910, 0x004EC000, shp_game, shp_c0, shp_a5,          shp_ttm),
)

def fmt_time(x):
    if x >= 30:
        s = "30*%d" % (x//30)
        x %= 30
        if x != 0:
            s += "+%d" % x
        return s
    else:
        return "%d" % x

def fmt_shape(x):
    if x == 0:
        return "S_NULL"
    addr = table.dev_addr(ultra.script)
    for shp in shp_table:
        if addr >= shp[0] and addr < shp[1]:
            for s in shp[2:]:
                if x in s:
                    return "S_" + s[x]
    return "%d" % x

import UNSM.asm
import UNSM.c
import UNSM.exe.lang
import UNSM.sym
import UNSM.header

msg_table = [
    "MSG_0",
    "MSG_1",
    "MSG_2",
    "MSG_3",
    "MSG_4",
    "MSG_5",
    "MSG_6",
    "MSG_7",
    "MSG_8",
    "MSG_9",
    "MSG_10",
    "MSG_11",
    "MSG_12",
    "MSG_13",
    "MSG_14",
    "MSG_15",
    "MSG_16",
    "MSG_17",
    "MSG_18",
    "MSG_19",
    "MSG_20",
    "MSG_21",
    "MSG_22",
    "MSG_23",
    "MSG_24",
    "MSG_25",
    "MSG_26",
    "MSG_27",
    "MSG_28",
    "MSG_29",
    "MSG_30",
    "MSG_31",
    "MSG_32",
    "MSG_33",
    "MSG_34",
    "MSG_35",
    "MSG_36",
    "MSG_37",
    "MSG_38",
    "MSG_39",
    "MSG_40",
    "MSG_41",
    "MSG_42",
    "MSG_43",
    "MSG_44",
    "MSG_45",
    "MSG_46",
    "MSG_47",
    "MSG_48",
    "MSG_49",
    "MSG_50",
    "MSG_51",
    "MSG_52",
    "MSG_53",
    "MSG_54",
    "MSG_55",
    "MSG_56",
    "MSG_57",
    "MSG_58",
    "MSG_59",
    "MSG_60",
    "MSG_61",
    "MSG_62",
    "MSG_63",
    "MSG_64",
    "MSG_65",
    "MSG_66",
    "MSG_67",
    "MSG_68",
    "MSG_69",
    "MSG_70",
    "MSG_71",
    "MSG_72",
    "MSG_73",
    "MSG_74",
    "MSG_75",
    "MSG_76",
    "MSG_77",
    "MSG_78",
    "MSG_79",
    "MSG_80",
    "MSG_81",
    "MSG_82",
    "MSG_83",
    "MSG_84",
    "MSG_85",
    "MSG_86",
    "MSG_87",
    "MSG_88",
    "MSG_89",
    "MSG_90",
    "MSG_91",
    "MSG_92",
    "MSG_93",
    "MSG_94",
    "MSG_95",
    "MSG_96",
    "MSG_97",
    "MSG_98",
    "MSG_99",
    "MSG_100",
    "MSG_101",
    "MSG_102",
    "MSG_103",
    "MSG_104",
    "MSG_105",
    "MSG_106",
    "MSG_107",
    "MSG_108",
    "MSG_109",
    "MSG_110",
    "MSG_111",
    "MSG_112",
    "MSG_113",
    "MSG_114",
    "MSG_115",
    "MSG_116",
    "MSG_117",
    "MSG_118",
    "MSG_119",
    "MSG_120",
    "MSG_121",
    "MSG_122",
    "MSG_123",
    "MSG_124",
    "MSG_125",
    "MSG_126",
    "MSG_127",
    "MSG_128",
    "MSG_129",
    "MSG_130",
    "MSG_131",
    "MSG_132",
    "MSG_133",
    "MSG_134",
    "MSG_135",
    "MSG_136",
    "MSG_137",
    "MSG_138",
    "MSG_139",
    "MSG_140",
    "MSG_141",
    "MSG_142",
    "MSG_143",
    "MSG_144",
    "MSG_145",
    "MSG_146",
    "MSG_147",
    "MSG_148",
    "MSG_149",
    "MSG_150",
    "MSG_151",
    "MSG_152",
    "MSG_153",
    "MSG_154",
    "MSG_155",
    "MSG_156",
    "MSG_157",
    "MSG_158",
    "MSG_159",
    "MSG_160",
    "MSG_161",
    "MSG_162",
    "MSG_163",
    "MSG_164",
    "MSG_165",
    "MSG_166",
    "MSG_167",
    "MSG_168",
    "MSG_169",
]

msg_course = [
    "COURSE_BOB; 1",
    "COURSE_WF",
    "COURSE_JRB",
    "COURSE_CCM",
    "COURSE_BBH",
    "COURSE_HMC",
    "COURSE_LLL",
    "COURSE_SSL",
    "COURSE_DDD",
    "COURSE_SL",
    "COURSE_WDW",
    "COURSE_TTM",
    "COURSE_THI",
    "COURSE_TTC",
    "COURSE_RR",
    "COURSE_BITDW",
    "COURSE_BITFS",
    "COURSE_BITS",
    "COURSE_PSS",
    "COURSE_COTMC",
    "COURSE_TOTWC",
    "COURSE_VCUTM",
    "COURSE_WMOTR",
    "COURSE_SA",
    "COURSE_END",
    None,
]

seq_table = [
    "sfx",
    "seq01",
    "seq02",
    "seq03",
    "seq04",
    "seq05",
    "seq06",
    "seq07",
    "seq08",
    "seq09",
    "seq0A",
    "seq0B",
    "seq0C",
    "seq0D",
    "seq0E",
    "seq0F",
    "seq10",
    "seq11",
    "seq12",
    "seq13",
    "seq14",
    "seq15",
    "seq16",
    "seq17",
    "seq18",
    "seq19",
    "seq1A",
    "seq1B",
    "seq1C",
    "seq1D",
    "seq1E",
    "seq1F",
    "seq20",
    "seq21",
    "seq22",
]

str_code = """
.set noreorder
.set noat
"""

str_code_s = """
#include <sm64/types.h>
""" + str_code

str_code_u = """
#include <ultra64.h>
""" + str_code

str_code_d = str_code_u + ".set gp = 64\n"

str_data_u = """
#include <ultra64.h>

"""

str_ucode_text = """
.include "PR/rsp.inc"
.create "build/PR/%s.text.bin", 0x%08X

"""

str_ucode_base = """

.base %s
"""

str_ucode_data = """

.close

.create "build/PR/%s.data.bin", 0

"""

str_ucode_end = """

.close
"""

str_ucode_s_text = """
.globl %sTextStart
%sTextStart:
.incbin "build/PR/%s.text.bin"
.globl %sTextEnd
%sTextEnd:
"""

str_ucode_s_data = """
.data
.globl %sDataStart
%sDataStart:
.incbin "build/PR/%s.data.bin"
.globl %sDataEnd
%sDataEnd:
"""

str_data = """
#include <sm64/types.h>

"""

str_gfx = """
#include <sm64/types.h>
#include <sm64/gbi_ext.h>

"""

str_g_script = """
#include <sm64/types.h>
#include <sm64/g_script.h>

#define __SCRIPT__

"""

str_s_script = """
#include <sm64/types.h>
#include <sm64/s_script.h>

.data

"""

str_o_script = """
#include <sm64/types.h>
#include <sm64/o_script.h>

#define __SCRIPT__

.data

"""

def slidec(src):
    sig, size, ci, di = struct.unpack(">4sIII", src[:0x10])
    ti  = 0x10
    dst = B""
    bit = 0
    bi  = 0
    while len(dst) < size:
        if bi == 0:
            bit, = struct.unpack(">I", src[ti:ti+4])
            ti += 4
            bi = 32
        if bit & 0x80000000:
            dst += src[di:di+1]
            di += 1
        else:
            so, = struct.unpack(">H", src[ci:ci+2])
            ci += 2
            of = len(dst) - ((so & 0x0FFF) + 1)
            sz = (so >> 12) + 3
            dst += (sz*dst[of:of+sz])[:sz]
        bit <<= 1
        bi -= 1
    return dst

def s_szp(self, argv):
    start, end, data = argv
    self.data[data+".szp"] = self.cache(start, end, data, slidec)
    self.dev = start

def s_szpbin(start, end, size, name):
    return [main.s_call, [
        [s_szp, start, end, "E0"],
        [main.s_bin, 0, size, "E0.szp", ["%s.bin" % name]],
        [main.s_dev, None],
    ]]

def s_dirfile(path, fn):
    if path != None:
        return [main.s_call, [
            [main.s_dir, path],
            [main.s_str, "#include \"%s/%s\"\n" % (path, fn)],
            [main.s_file, fn],
        ]]
    return [main.s_call, [
        [main.s_str, "#include \"%s\"\n" % fn],
        [main.s_file, fn],
    ]]

def s_writepop():
    return [main.s_call, [
        [main.s_write],
        [main.s_pop],
    ]]

def s_ifdef(s):
    return [main.s_str, "\n\n#ifdef %s\n\n" % s]

def s_ifndef(s):
    return [main.s_str, "\n\n#ifndef %s\n\n" % s]

def s_ifndef_define(s):
    return [main.s_str, "\n\n#ifndef %s\n#define %s\n\n" % (s, s)]

def s_else(s):
    return [main.s_str, "\n\n#else /* %s */\n\n" % s]

def s_endif(s):
    return [main.s_str, "\n\n#endif /* %s */\n\n" % s]

def s_script_ifndef():
    return s_ifndef("__SCRIPT__")

def s_script_else():
    return s_else("__SCRIPT__")

def s_script_endif():
    return s_endif("__SCRIPT__")

def s_header_macro(self, argv):
    fmt, = argv
    fn = self.file[-1][0].rpartition("include" + os.path.sep)[-1]
    self.file[-1][1].append(fmt % "".join([
        x if x in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" else "_"
        for x in fn.upper()
    ]))

def s_header(name, globl=[], c=[], asm=[]):
    lst = [
        [main.s_file, "%s.h" % name],
            [s_header_macro, "\n\n#ifndef __%s__\n"],
            [s_header_macro, "#define __%s__\n\n"],
    ] + globl
    if len(c) > 0:
        lst += [
            s_ifndef("__ASSEMBLER__"),
        ] + c
        if len(asm) > 0:
            lst += [
                s_else("__ASSEMBLER__"),
            ] + asm
        lst += [
            s_endif("__ASSEMBLER__"),
        ]
    elif len(asm) > 0:
        lst += [
            s_ifdef("__ASSEMBLER__"),
        ] + asm + [
            s_endif("__ASSEMBLER__"),
        ]
    lst += [
            [s_header_macro, "\n\n#endif /* __%s__ */\n\n"],
        [main.s_write],
    ]
    return [main.s_call, lst]

def s_header_code(ts, te, ds, de, bs, be, name, lst, sg="", sc="", sa=""):
    return s_header(name, [
        [main.s_str, sg],
    ], [
        [main.s_str, sc],
        [main.s_str, "\n"],
        [ultra.c.s_struct, lst],
        [main.s_str, "\n"],
        [ultra.c.s_extern, bs, be, "E0", ds],
        [ultra.c.s_extern, ds, de, "E0", None],
        [main.s_str, "\n"],
        [ultra.c.s_extern, ts, te, "E0", None],
    ], [
        [main.s_str, sa],
        [main.s_str, "\n"],
        [ultra.asm.s_struct, lst],
    ] if sa != "" or len(lst) > 0 else [])

def s_ucode(name, addr, text, data=[]):
    label = name.replace(".", "_") # todo: proper
    lst = [
        [main.s_file, "%s.s" % name],
            [main.s_str, str_ucode_s_text % (label, label, name, label, label)],
    ]
    if len(data) > 0:
        lst += [
            [main.s_str, str_ucode_s_data % (label, label, name, label, label)],
        ]
    lst += [
        [main.s_write],
        [main.s_file, "%s.asm" % name],
            [main.s_str, str_ucode_text % (name, addr)],
    ] + text
    if len(data) > 0:
        lst += [
            [main.s_str, str_ucode_data % name],
        ] + data
    lst += [
            [main.s_str, str_ucode_end],
        [main.s_write],
    ]
    return [main.s_call, lst]

def s_code(start, end, fn, s=str_code_s, macro=True, sep=False):
    return [main.s_call, [
        [main.s_file, "%s.S" % fn],
            [main.s_str, s],
            [ultra.asm.s_code, start, end, "E0", 0, macro, sep],
        [main.s_write],
    ]]

def s_data(ds, de, rs, re, bs, be, fn, dl, rl, s=""):
    return [main.s_call, [
        [main.s_file, "%s.c" % fn],
            [main.s_str, "\n"], [main.s_str, s],
            [main.s_str, "\n"], [ultra.c.s_data, rs, re, "E0", rl],
            [main.s_str, "\n"], [ultra.c.s_bss,  bs, be, "E0", ds],
            [main.s_str, "\n"], [ultra.c.s_data, ds, de, "E0", dl],
        [main.s_write],
    ]]

def s_databin(start, end, name):
    return [main.s_bin, start, end, "E0", ["%s.bin" % name]]

def s_gfx(start, end, a, name, lst):
    return [main.s_call, [
        [main.s_dir, name],
            [s_szp, start, end, "E0"],
            [main.s_addr, a << 24],
            [main.s_file, "gfx.c"],
                [main.s_call, lst],
            [main.s_write],
            [main.s_dev, None],
            [main.s_addr, 0],
        [main.s_pop],
    ]]

def s_shapebin(start, end, size, gsize, b, name):
    return [main.s_call, [
        [main.s_dir, name],
            s_szpbin(start, end, size, "gfx"),
            [main.s_addr, (b << 24) - end],
            [main.s_file, "g.c"],
                [main.s_str, str_g_script],
                [c.s_script_g, b << 24, (b << 24) + gsize, "E0"],
            [main.s_write],
            [main.s_addr, 0],
        [main.s_pop],
    ]]

def s_shape(start, end, a, b, name, gfx, g):
    return [main.s_call, [
        [main.s_dir, name],
            [s_szp, start, end, "E0"],
            [main.s_addr, (a << 24)],
            [main.s_file, "gfx.c"],
                [main.s_str, str_gfx],
                [main.s_call, gfx],
            [main.s_write],
            [main.s_dev, None],
            [main.s_addr, (b << 24) - end],
            [main.s_file, "g.c"],
                [main.s_str, str_g_script],
                [main.s_call, g],
            [main.s_write],
            [main.s_addr, 0],
        [main.s_pop],
    ]]

def s_script(start, end, addr, size):
    s_start = addr
    s_end   = addr + size
    g_start = (s_end+0x0F) & ~0x0F
    g_end   = addr + end-start
    return [main.s_call, [
        [main.s_addr, addr-start],
        [main.s_file, "s.S"],
            [main.s_str, str_s_script],
            [asm.s_script, s_start, s_end, "E0", 0],
        [main.s_write],
        [main.s_file, "g.c"],
            [main.s_str, str_g_script],
            [c.s_script_g, g_start, g_end, "E0"],
        [main.s_write],
        [main.s_addr, 0],
    ]]

def s_shape_s(start, end, name):
    return [main.s_call, [
        s_dirfile(os.path.join("shape", name), "s.S"),
            [asm.s_script, start, end, "E0", 0],
        s_writepop(),
    ]]

def s_stagebin(a, b, c, size, g, name):
    return [main.s_call, [
        [main.s_dir, name],
            s_szpbin(a, b, size, "gfx"),
            s_script(b, c, 0x0E000000, g),
        [main.s_pop],
    ]]

def s_ply(start, gfx, end, name, light=False, scale=None):
    return [main.s_call, [
        [c.s_ply_vtx, name],
        [ultra.c.s_data, start, end, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, gfx, name, light, scale],
            [0, 1, 1, ultra.c.d_Gfx, end],
        ]],
    ]]

def d_texture_n(t, w, h, end, fmt="%d", start=0, step=1):
    return [0, 1, [
        [0, 1, 1, c.d_texture, t, w, h, fmt % i]
        for i in range(start, end, step)
    ]]

stbl_motion = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "60",
    "61",
    "62",
    "63",
    "64",
    "65",
    "66",
    "67",
    "68",
    "69",
    "70",
    "71",
    "72",
    "73",
    "74",
    "75",
    "76",
    "77",
    "78",
    "79",
    "80",
    "81",
    "82",
    "83",
    "84",
    "85",
    "86",
    "87",
    "88",
    "89",
    "90",
    "91",
    "92",
    "93",
    "94",
    "95",
    "96",
    "97",
    "98",
    "99",
    "100",
    "101",
    "102",
    "103",
    "104",
    "105",
    "106",
    "107",
    "108",
    "109",
    "110",
    "111",
    "112",
    "113",
    "114",
    "115",
    "116",
    "117",
    "118",
    "119",
    "120",
    "121",
    "122",
    "123",
    "124",
    "125",
    "126",
    "127",
    "128",
    "129",
    "130",
    "131",
    "132",
    "133",
    "134",
    "135",
    "136",
    "137",
    "138",
    "139",
    "140",
    "141",
    "142",
    "143",
    "144",
    "145",
    "146",
    "147",
    "148",
    "149",
    "150",
    "151",
    "152",
    "153",
    "154",
    "155",
    "156",
    "157",
    "158",
    "159",
    "160",
    "161",
    "162",
    "163",
    "164",
    "165",
    "166",
    "167",
    "168",
    "169",
    "170",
    "171",
    "172",
    "173",
    "174",
    "175",
    "176",
    "177",
    "178",
    "179",
    "180",
    "181",
    "182",
    "183",
    "184",
    "185",
    "186",
    "187",
    "188",
    "189",
    "190",
    "191",
    "192",
    "193",
    "194",
    "195",
    "196",
    "197",
    "198",
    "199",
    "200",
    "201",
    "202",
    "203",
    "204",
    "205",
    "206",
    "207",
    "208",
]

ctbl_motion = {
    1: "1_2",
    2: "1_2",
    7: "7_8",
    8: "7_8",
    11: "11_12",
    12: "11_12",
    15: "15_16",
    16: "15_16",
    44: "44_45",
    45: "44_45",
    60: "60_61",
    61: "60_61",
    69: "69_70",
    70: "69_70",
    77: "77_78",
    78: "77_78",
    86: "86_87",
    87: "86_87",
    111: "111_112",
    112: "111_112",
    114: "114_115",
    115: "114_115",
    136: "136_137",
    137: "136_137",
    142: "142_143",
    143: "142_143",
    181: "181_182",
    182: "181_182",
    188: "188_189",
    189: "188_189",
    203: "203_204",
    204: "203_204",
}

stbl_demo = [
    "bitdwa",
    "wf",
    "ccm",
    "bbh",
    "jrb",
    "hmc",
    "pss",
]

ultra_src = [
    [main.s_file, "parameters.S"],
        [main.s_str, header.str_ultra_parameters],
    [main.s_write],
    s_code(0x803223B0, 0x803223D4, "osSetTime",                 str_code_u, False),
    s_code(0x803223E0, 0x80322494, "osMapTLB",                  str_code_u, False),
    s_code(0x803224A0, 0x803224E4, "osUnmapTLBAll",             str_code_u, False),
    s_code(0x803224F0, 0x80322594, "sprintf",                   str_code_u, False),
    s_code(0x803225A0, 0x803225CC, "osCreateMesgQueue",         str_code_u, False),
    s_code(0x803225D0, 0x80322638, "osSetEventMesg",            str_code_u, False),
    s_code(0x80322640, 0x803226AC, "osViSetEvent",              str_code_u, False),
    s_code(0x803226B0, 0x803227F4, "osCreateThread",            str_code_u, False),
    s_code(0x80322800, 0x80322938, "osRecvMesg",                str_code_u, False),
    s_code(0x80322940, 0x80322BFC, "osSpTaskStart",             str_code_u, False),
    s_code(0x80322C00, 0x80322C20, "osSpTaskYield",             str_code_u, False),
    s_code(0x80322C20, 0x80322D6C, "osSendMesg",                str_code_u, False),
    s_code(0x80322D70, 0x80322DF0, "osSpTaskYielded",           str_code_u, False),
    s_code(0x80322DF0, 0x80322F40, "osStartThread",             str_code_u, False),
    s_code(0x80322F40, 0x80322F68, "osWritebackDCacheAll",      str_code_u, False),
    s_code(0x80322F70, 0x803232C4, "osCreateViManager",         str_code_u, False),
    s_code(0x803232D0, 0x80323338, "osViSetMode",               str_code_u, False),
    s_code(0x80323340, 0x803233B0, "osViBlack",                 str_code_u, False),
    s_code(0x803233B0, 0x80323568, "osViSetSpecialFeatures",    str_code_u, False),
    s_code(0x80323570, 0x803236EC, "osCreatePiManager",         str_code_u, False),
    s_code(0x803236F0, 0x803237D0, "osSetThreadPri",            str_code_u, False),
    s_code(0x803237D0, 0x80323A00, "osInitialize",              str_code_u, False),
    s_code(0x80323A00, 0x80323A50, "osViSwapBuffer",            str_code_u, False),
    s_code(0x80323A50, 0x80323A58, "sqrtf",                     str_code_u, False),
    s_code(0x80323A60, 0x80323CB8, "osContReadData",            str_code_u, False),
    s_code(0x80323CC0, 0x80324080, "osContInit",                str_code_u, False),
    s_code(0x80324080, 0x803240EC, "osEepromProbe",             str_code_u, False),
    s_code(0x803240F0, 0x803243B0, "ll_multdiv",                str_code_d, False),
    s_code(0x803243B0, 0x8032445C, "osInvalDCache",             str_code_u, False),
    s_code(0x80324460, 0x80324564, "osPiStartDma",              str_code_u, False),
    s_code(0x80324570, 0x8032460C, "bzero",                     str_code_u, False),
    s_code(0x80324610, 0x80324684, "osInvalICache",             str_code_u, False),
    s_code(0x80324690, 0x803247CC, "osEepromLongRead",          str_code_u, False),
    s_code(0x803247D0, 0x8032490C, "osEepromLongWrite",         str_code_u, False),
    s_code(0x80324910, 0x80324C14, "bcopy",                     str_code_u, False),
    s_code(0x80324C20, 0x80324DDC, "guOrtho",                   str_code_u, False),
    s_code(0x80324DE0, 0x80325068, "guPerspective",             str_code_u, False),
    s_code(0x80325070, 0x803250F4, "osGetTime",                 str_code_u, False),
    s_code(0x80325100, 0x80325308, "ll_cvt",                    str_code_d, False),
    s_code(0x80325310, 0x80325478, "cosf",                      str_code_u, False),
    s_code(0x80325480, 0x80325640, "sinf",                      str_code_u, False),
    s_code(0x80325640, 0x803256DC, "guTranslate",               str_code_u, False),
    s_code(0x803256E0, 0x803258C4, "guRotate",                  str_code_u, False),
    s_code(0x803258D0, 0x8032596C, "guScale",                   str_code_u, False),
    s_code(0x80325970, 0x80325AD0, "osAiSetFrequency",          str_code_u, False),
    s_code(0x80325AD0, 0x80325D18, "alBnkfNew",                 str_code_u, False),
    s_code(0x80325D20, 0x80325D94, "osWritebackDCache",         str_code_u, False),
    s_code(0x80325DA0, 0x80325DAC, "osAiGetLength",             str_code_u, False),
    s_code(0x80325DB0, 0x80325E58, "osAiSetNextBuffer",         str_code_u, False),
    s_code(0x80325E60, 0x80326260, "__osTimerService",          str_code_u, False),
    s_code(0x80326260, 0x803273E4, "printf",                    str_code_u, False),
    s_code(0x803273F0, 0x80327484, "string",                    str_code_u, False),
    s_code(0x80327490, 0x803274D0, "__osDequeueThread",         str_code_u, False),
    s_code(0x803274D0, 0x8032750C, "__osInterrupt",             str_code_u, False),
    s_code(0x80327510, 0x80327634, "__osViInit",                str_code_u, False),
    s_code(0x80327640, 0x80327EB0, "__osException",             str_code_d, False),
    s_code(0x80327EB0, 0x80327F2C, "osVirtualToPhysical",       str_code_u, False),
    s_code(0x80327F30, 0x80327F3C, "__osSpSetStatus",           str_code_u, False),
    s_code(0x80327F40, 0x80327F74, "__osSpSetPc",               str_code_u, False),
    s_code(0x80327F80, 0x8032800C, "__osSpRawStartDma",         str_code_u, False),
    s_code(0x80328010, 0x8032803C, "__osSpDeviceBusy",          str_code_u, False),
    s_code(0x80328040, 0x8032804C, "__osSpGetStatus",           str_code_u, False),
    s_code(0x80328050, 0x80328068, "osGetThreadPri",            str_code_u, False),
    s_code(0x80328070, 0x8032807C, "__osViGetCurrentContext",   str_code_u, False),
    s_code(0x80328080, 0x803283DC, "__osViSwapContext",         str_code_u, False),
    s_code(0x803283E0, 0x803283EC, "osGetCount",                str_code_u, False),
    s_code(0x803283F0, 0x803284B0, "__osPiAccess",              str_code_u, False),
    s_code(0x803284B0, 0x80328590, "osPiRawStartDma",           str_code_u, False),
    s_code(0x80328590, 0x80328704, "__osDevMgrMain",            str_code_u, False),
    s_code(0x80328710, 0x80328720, "__osSetSR",                 str_code_u, False),
    s_code(0x80328720, 0x8032872C, "__osGetSR",                 str_code_u, False),
    s_code(0x80328730, 0x80328740, "__osSetFpcCsr",             str_code_u, False),
    s_code(0x80328740, 0x80328790, "__osSiRawReadIo",           str_code_u, False),
    s_code(0x80328790, 0x803287DC, "__osSiRawWriteIo",          str_code_u, False),
    s_code(0x803287E0, 0x80328838, "osMapTLBRdb",               str_code_u, False),
    s_code(0x80328840, 0x80328894, "osPiRawReadIo",             str_code_u, False),
    s_code(0x803288A0, 0x80328960, "__osSiAccess",              str_code_u, False),
    s_code(0x80328960, 0x80328A0C, "__osSiRawStartDma",         str_code_u, False),
    s_code(0x80328A10, 0x80328AE4, "osSetTimer",                str_code_u, False),
    s_code(0x80328AF0, 0x80328FD0, "osEepromWrite",             str_code_u, False),
    s_code(0x80328FD0, 0x80329120, "osJamMesg",                 str_code_u, False),
    s_code(0x80329120, 0x80329148, "osPiGetCmdQueue",           str_code_u, False),
    s_code(0x80329150, 0x80329444, "osEepromRead",              str_code_u, False),
    s_code(0x80329450, 0x803296BC, "guMtxIdent",                str_code_u, False),
    s_code(0x803296C0, 0x80329744, "guNormalize",               str_code_u, False),
    s_code(0x80329750, 0x80329780, "__osAiDeviceBusy",          str_code_u, False),
    s_code(0x80329780, 0x8032978C, "__osSetCompare",            str_code_u, False),
    s_code(0x80329790, 0x80329A90, "_Litob",                    str_code_u, False),
    s_code(0x80329A90, 0x8032A860, "_Ldtob",                    str_code_u, False),
    s_code(0x8032A860, 0x8032ACD4, "8032A860",                  str_code_u, False),
    s_code(0x8032ACE0, 0x8032AE04, "__osSyncPutChars",          str_code_u, False),
    s_code(0x8032AE10, 0x8032AE70, "osSetIntMask",              str_code_u, False),
    s_code(0x8032AE70, 0x8032AF68, "osDestroyThread",           str_code_u, False),
    s_code(0x8032AF70, 0x8032B028, "__osProbeTLB",              str_code_u, False),
    s_code(0x8032B030, 0x8032B05C, "__osSiDeviceBusy",          str_code_u, False),
    s_code(0x8032B060, 0x8032B1E4, "ldiv",                      str_code_u, False),
    s_code(0x8032B1F0, 0x8032B1FC, "__osGetCause",              str_code_u, False),
    s_code(0x8032B200, 0x8032B258, "__osAtomicDec",             str_code_u, False),
    s_data(0x80335010, 0x803358D0, 0x803397B0, 0x803397B0, 0, 0, "osViModeTable", [
        [1, -28, ultra.c.d_OSViMode],
    ], [], str_data_u),
    s_data(0x803358D0, 0x803358E8, 0x803397B0, 0x803397B0, 0, 0, "osCreateViManager.data", [
        [1, 1, 1, ultra.c.d_str, 0x18, "0"],
    ], [], str_data_u),
    s_data(0x803358F0, 0x80335908, 0x803397B0, 0x803397B0, 0, 0, "osCreatePiManager.data", [
        [1, 1, 1, ultra.c.d_str, 0x18, "0"],
    ], [], str_data_u),
    s_data(0x80335910, 0x8033591C, 0x803397B0, 0x803397B0, 0, 0, "osInitialize.data", [
        [0, 1, 1, ultra.c.d_u64],
        [0, 1, 1, ultra.c.d_u32],
    ], [], str_data_u),
    s_data(0x80335920, 0x80335924, 0x803397B0, 0x803397B0, 0, 0, "osContInit.data", [
        [0, 1, 1, ultra.c.d_u32],
    ], [], str_data_u),
    s_data(0x80335930, 0x80335930, 0x803397B0, 0x803397B8, 0, 0, "guPerspective.data", [], [
        [0, 1, 1, ultra.c.d_f64],
    ], str_data_u),
    s_data(0x80335930, 0x80335930, 0x803397C0, 0x803397D0, 0, 0, "ll_cvt.data", [], [
        [0, 2, 1, ultra.c.d_u64, "0x%016X"],
    ], str_data_u),
    s_data(0x80335930, 0x80335930, 0x803397D0, 0x80339814, 0, 0, "cosf.data", [], [
        [0, -5, 1, ultra.c.d_f64],
        [0,  3, 1, ultra.c.d_f64],
        [0,  1, 1, ultra.c.d_f32],
    ], str_data_u),
    s_data(0x80335930, 0x80335930, 0x80339820, 0x80339864, 0, 0, "sinf.data", [], [
        [0, -5, 1, ultra.c.d_f64],
        [0,  3, 1, ultra.c.d_f64],
        [0,  1, 1, ultra.c.d_f32],
    ], str_data_u),
    s_data(0x80335930, 0x80335930, 0x80339870, 0x80339874, 0, 0, "guRotate.data", [], [
        [0, 1, 1, ultra.c.d_f32],
    ], str_data_u),
    s_data(0x80335930, 0x80335931, 0x80339880, 0x80339880, 0, 0, "osAiSetNextBuffer.data", [
        [0, 1, 1, ultra.c.d_u8],
    ], [], str_data_u),
    s_data(0x80335940, 0x80335944, 0x80339880, 0x80339880, 0, 0, "__osTimerService.data", [
        [0, 1, 1, ultra.c.d_addr, 0],
    ], [], str_data_u),
    s_data(0x80335950, 0x80335994, 0x80339880, 0x80339974, 0, 0, "printf.data", [
        [0, 2, 36, "str"],
    ], [
        [0, 1, 4, "str"],
        [0, 1, 8, "str"],
        [1, 1, 6, ultra.c.d_u32],
        [0, -52, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data_u),
    s_data(0x803359A0, 0x803359B8, 0x80339980, 0x80339980, 0, 0, "__osDequeueThread.data", [
        [0, 1, 1, ultra.c.d_OSThreadTail],
        [0, 4, 1, ultra.c.d_addr, ultra.c.A_ADDR, "OSThread *"],
    ], [], str_data_u),
    s_data(0x803359C0, 0x80335A30, 0x80339980, 0x80339980, 0, 0, "__osViInit.data", [
        [1, 2, 1, ultra.c.d_str, 0x30, "0"],
        [0, 2, 1, ultra.c.d_addr, ultra.c.A_ADDR],
        [0, 2, 1, ultra.c.d_u32],
    ], [], str_data_u),
    s_data(0x80335A30, 0x80335A4C, 0x80339980, 0x803399C4, 0, 0, "__osException.data", [
        [1, 1, 1, ultra.c.d_str, 0x14, "0"],
        [0, 2, 1, ultra.c.d_u32],
    ], [
        [0, -2, 16, ultra.c.d_u8],
        [0, -9, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data_u),
    s_data(0x80335A50, 0x80335A50, 0x803399D0, 0x803399D4, 0, 0, "__libm_qnan_f", [], [
        [0, 1, 1, ultra.c.d_u32, "0x%08X"],
    ], str_data_u),
    s_data(0x80335A50, 0x80335A54, 0x803399E0, 0x803399E0, 0, 0, "__osPiAccess.data", [
        [0, 1, 1, ultra.c.d_u32],
    ], [], str_data_u),
    s_data(0x80335A60, 0x80335A64, 0x803399E0, 0x803399E0, 0, 0, "__osSiAccess.data", [
        [0, 1, 1, ultra.c.d_u32],
    ], [], str_data_u),
    s_data(0x80335A70, 0x80335A98, 0x803399E0, 0x803399E0, 0, 0, "_Litob.data", [
        [0, 2, 20, "str"],
    ], [], str_data_u),
    s_data(0x80335AA0, 0x80335AA0, 0x803399E0, 0x80339A40, 0, 0, "_Ldtob.data", [], [
        [0, -9, 1, ultra.c.d_f64],
        [0, 4, 4, "str"],
        [0, 1, 1, ultra.c.d_f64],
    ], str_data_u),
    s_data(0x80335AA0, 0x80335AF0, 0x80339A40, 0x80339A40, 0, 0, "osViModeNtscLan1", [
        [0, 1, ultra.c.d_OSViMode],
    ], [], str_data_u),
    s_data(0x80335AF0, 0x80335B40, 0x80339A40, 0x80339A40, 0, 0, "osViModePalLan1", [
        [0, 1, ultra.c.d_OSViMode],
    ], [], str_data_u),
    s_data(0x80335B40, 0x80335B4C, 0x80339A40, 0x80339A40, 0, 0, "8032A860.data", [
        [0, 3, 1, ultra.c.d_u32],
    ], [], str_data_u),
    s_data(0x80335B50, 0x80335B58, 0x80339A40, 0x80339A40, 0, 0, "__osSyncPutChars.data", [
        [0, 2, 1, ultra.c.d_u32],
    ], [], str_data_u),
    s_data(0x80335B60, 0x80335B60, 0x80339A40, 0x80339AC0, 0, 0, "osSetIntMask.data", [], [
        [0, -8, 8, ultra.c.d_u16, "0x%04X"],
    ], str_data_u),
    [main.s_file, "data.S"],
        [main.s_str, """
.bss

.globl _ultra_bss
_ultra_bss:
    .space 0x28C0
"""],
    [main.s_write],
]

ultra_PR = [
    s_code(0x80246000, 0x80246050, "crt0", str_code_u, False),
    [main.s_addr, 0],
    [main.s_file, "header.S"],
        [ultra.asm.s_header, "E0"],
    [main.s_write],
    [main.s_addr, 0xA4000000-0x00000000],
    # s_code(0xA4000040, 0xA4000B6C, "ipl3"),
    # [main.s_bin, 0xA4000B70, 0xA4001000, "E0", ["ipl3.data.bin"]],
    [main.s_bin, 0xA4000040, 0xA4001000, "E0", ["ipl3.bin"]],
    [main.s_file, "ipl3.S"],
        [main.s_str, ".incbin \"PR/ipl3.bin\"\n"],
    [main.s_write],
    s_ucode("rspboot", 0x04001000, [
        [main.s_addr, 0x04001000 - 0x000E6260],
        [ultra.asm.s_code, 0x04001000, 0x040010D0, "E0", 1, False, False],
    ]),
    s_ucode("gspFast3D.fifo", 0x04001080, [
        [main.s_addr, 0x04001080 - 0x000E6330],
        [ultra.asm.s_code, 0x04001080, 0x04001FE0, "E0", 1, False, False],
        [main.s_str, str_ucode_base % "0x04001000"],
        [main.s_addr, 0x04001000 - 0x000E7290],
        [ultra.asm.s_code, 0x04001000, 0x04001088, "E0", 1, False, False],
        [main.s_str, str_ucode_base % "0x04001768"],
        [main.s_addr, 0x04001768 - 0x000E7318],
        [ultra.asm.s_code, 0x04001768, 0x04001988, "E0", 1, False, False],
        [main.s_str, str_ucode_base % "0x04001768"],
        [main.s_addr, 0x04001768 - 0x000E7538],
        [ultra.asm.s_code, 0x04001768, 0x04001900, "E0", 1, False, False],
        [main.s_str, str_ucode_base % "0x04001768"],
        [main.s_addr, 0x04001768 - 0x000E76D0],
        [ultra.asm.s_code, 0x04001768, 0x040017D0, "E0", 1, False, False],
    ], [
        [main.s_addr, 0x00000000 - 0x000F4AC0],
        [ultra.asm.s_data, 0x00000000, 0x00000800, "E0", [
            [ 5, 1, asm.d_prg],
            [ 1, 2, ultra.asm.d_shalf], # VCONST_SCREENCLAMP
            [ 1, 2, ultra.asm.d_half],
            [ 1, 4, ultra.asm.d_shalf], # VCONST_OFFSET
            [ 1, 4, ultra.asm.d_half],
            [ 1, 8, ultra.asm.d_half], # VCONST1_OFFSET
            [ 1, 8, ultra.asm.d_shalf], # VOPENGL_OFFSET
            [ 1, 8, ultra.asm.d_shalf], # VNEWT_OFFSET
            [12, 1, ultra.asm.d_word], # CLIP_SELECT
            [ 1, 1, ultra.asm.d_addr], # DOLIGHT
            [ 3, 1, ultra.asm.d_half], # arccos
            [ 1, 6, ultra.asm.d_half], # CLIPMASKS
            [ 1, 1, ultra.asm.d_shalf], # ANCHOR
            [ 1, 1, ultra.asm.d_addr], # TASKDONE
            [ 1, 1, ultra.asm.d_word], # SEGADDR_MASK_OFFSET
            [ 4, 1, ultra.asm.d_addr], # op type
            [10, 1, ultra.asm.d_addr], # op 00
            [15, 1, ultra.asm.d_addr], # op 80
            [ 7, 1, ultra.asm.d_addr], # clip
            [ 1, 1, ultra.asm.d_addr], # DMAWAITDL
            [(0x800-0x106), 1, ultra.asm.d_byte],
        ]],
    ]),
    s_ucode("aspMain", 0x04001080, [
        [main.s_addr, 0x04001080 - 0x000E7740],
        [ultra.asm.s_code, 0x04001080, 0x04001EA0, "E0", 1, False, False],
    ], [
        [main.s_addr, 0x00000000 - 0x000F52C0],
        [ultra.asm.s_data, 0x00000000, 0x000002C0, "E0", [
            [0x2C, 4, ultra.asm.d_word],
        ]],
    ]),
]

include_main = [
    s_header("buffer"),
    s_header_code(0x80246050, 0x80246E68, 0x8032D560, 0x8032D5C4, 0x8033A580, 0x8033AF90, "main", header.struct_main, """
#include <sm64/types.h>
"""),
    s_header_code(0x80246E70, 0x80248C3C, 0x8032D5D0, 0x8032D5FC, 0x8033AF90, 0x8033B09C, "app", header.struct_app, """
#include <sm64/types.h>
#include <sm64/main.h>
"""),
    s_header_code(0x80248C40, 0x802495DC, 0x8032D600, 0x8032D6C1, 0x8033B0A0, 0x8033B170, "audio", header.struct_audio, """
#include <sm64/types.h>
#include <sm64/main.h>
"""),
    s_header_code(0x802495E0, 0x8024BFE4, 0x8032D6D0, 0x8032D948, 0x8033B170, 0x8033B26F, "game", header.struct_game, """
#include <sm64/types.h>
#include <sm64/player.h>
"""),
    s_header_code(0x8024BFF0, 0x8025093C, 0x8032D950, 0x8032DA9C, 0x8033B270, 0x8033B274, "player_touch", header.struct_player_touch, """
#include <sm64/types.h>
#include <sm64/player.h>
#include <sm64/object.h>
"""),
    s_header_code(0x80250940, 0x8025507C, 0x8032DAA0, 0x8032DAE8, 0x8033B280, 0x8033B284, "player", header.struct_player, """
#include <sm64/types.h>
"""),
    s_header_code(0x80255080, 0x80256DFC, 0x8032DAF0, 0x8032DB28, 0x8033B290, 0x8033B294, "player_move", header.struct_player_move, """
#include <sm64/types.h>
"""),
    s_header_code(0x80256E00, 0x8025DD68, 0x8032DB30, 0x8032DC50, 0x8033B2A0, 0x8033B2C0, "player_demo", header.struct_player_demo, """
#include <sm64/types.h>
"""),
    s_header_code(0x8025DD70, 0x802608AC, 0x8032DC50, 0x8032DC50, 0, 0, "player_hang", header.struct_player_hang, """
#include <sm64/types.h>
"""),
    s_header_code(0x802608B0, 0x80263E5C, 0x8032DC50, 0x8032DC50, 0, 0, "player_stop", header.struct_player_stop, """
#include <sm64/types.h>
"""),
    s_header_code(0x80263E60, 0x80269F38, 0x8032DC50, 0x8032DD28, 0x8033B2C0, 0x8033B340, "player_ground", header.struct_player_ground, """
#include <sm64/types.h>
"""),
    s_header_code(0x80269F40, 0x80270104, 0x8032DD30, 0x8032DD30, 0, 0, "player_air", header.struct_player_air, """
#include <sm64/types.h>
"""),
    s_header_code(0x80270110, 0x80274EAC, 0x8032DD30, 0x8032DD40, 0x8033B340, 0x8033B348, "player_water", header.struct_player_water, """
#include <sm64/types.h>
"""),
    s_header_code(0x80274EB0, 0x802761D0, 0x8032DD40, 0x8032DD48, 0, 0, "player_grab", header.struct_player_grab, """
#include <sm64/types.h>
"""),
    s_header_code(0x802761D0, 0x80277ED4, 0x8032DD50, 0x8032DD6A, 0x8033B350, 0x8033B400, "player_callback", header.struct_player_callback, """
#include <sm64/types.h>
"""),
    s_header_code(0x80277EE0, 0x80279158, 0x8032DD70, 0x8032DD74, 0x8033B400, 0x8033B498, "mem", header.struct_mem, """
#include <sm64/types.h>

#define MEM_ALLOC_L 0
#define MEM_ALLOC_R 1
""", "", """
#define TABLE()     .word (table_end-table_start)/8, 0
#define FILE(file)  .word file, file##_end-file
"""),
    s_header_code(0x80279160, 0x8027A7C4, 0x8032DD80, 0x8032DDBE, 0x8033B4A0, 0x8033B4A7, "save", header.struct_save, """
#include <sm64/types.h>
"""),
    s_header_code(0x8027A7D0, 0x8027B6C0, 0x8032DDC0, 0x8032DE70, 0x8033B4B0, 0x8033BAE0, "world", header.struct_world, """
#include <sm64/types.h>
#include <sm64/o_script.h>
"""),
    s_header_code(0x8027B6C0, 0x8027E3DC, 0x8032DE70, 0x8032DF0C, 0x8033BAE0, 0x8033C38C, "g_draw", header.struct_g_draw, """
#include <sm64/types.h>
"""),
    s_header_code(0x8027E3E0, 0x8027F4D4, 0x8032DF10, 0x8032DF1C, 0x8033C390, 0x8033C520, "time", header.struct_time, """
#include <sm64/types.h>
"""),
    s_header_code(0x8027F4E0, 0x8027F584, 0x8032DF20, 0x8032DF20, 0, 0, "slidec", header.struct_slidec, """
#include <sm64/types.h>
"""),
    s_header_code(0x8027F590, 0x8029C764, 0x8032DF20, 0x8032FEB4, 0, 0, "camera", header.struct_camera, """
#include <sm64/types.h>
"""),
    s_header_code(0x8029C770, 0x8029C780, 0x8032FEC0, 0x8032FEC0, 0, 0, "course", header.struct_course, """
#include <sm64/types.h>
"""),
    s_header_code(0x8029C780, 0x8029D884, 0x8032FEC0, 0x8032FFFC, 0, 0, "object", header.struct_object, """
#include <sm64/types.h>
#include <sm64/g.h>
#include <sm64/o_script.h>
"""),
    s_header_code(0x8029D890, 0x802A5618, 0x80330000, 0x80330018, 0x80361270, 0x80361274, "object_lib", header.struct_object_lib, """
#include <sm64/types.h>
"""),
    s_header_code(0x802A5620, 0x802C89F0, 0x80330020, 0x80330E1C, 0x80361280, 0x80361282, "object_a", header.struct_object_a, """
#include <sm64/types.h>
"""),
    s_header_code(0x802C89F0, 0x802C8F40, 0x80330E20, 0x80330E38, 0, 0, "object_move", header.struct_object_move, """
#include <sm64/types.h>
"""),
    s_header_code(0x802C8F40, 0x802C97C8, 0x80330E40, 0x80330E40, 0, 0, "object_touch", header.struct_object_touch, """
#include <sm64/types.h>
"""),
    s_header_code(0x802C97D0, 0x802CA03C, 0x80330E40, 0x80330E40, 0, 0, "object_list", header.struct_object_list, """
#include <sm64/types.h>
"""),
    s_header_code(0x802CA040, 0x802CA370, 0x80330E40, 0x80330E40, 0, 0, "object_sfx", header.struct_object_sfx, """
#include <sm64/types.h>
"""),
    s_header_code(0x802CA370, 0x802CB5B4, 0x80330E40, 0x80330EB2, 0, 0, "object_debug", header.struct_object_debug, """
#include <sm64/types.h>
"""),
    s_header_code(0x802CB5C0, 0x802CD27C, 0x80330EC0, 0x80330ED8, 0, 0, "wipe", header.struct_wipe, """
#include <sm64/types.h>
"""),
    s_header_code(0x802CD280, 0x802CF5A4, 0x80330EE0, 0x80330EF8, 0x803612B0, 0x803612B6, "shadow", header.struct_shadow, """
#include <sm64/types.h>
"""),
    s_header_code(0x802CF5B0, 0x802D007C, 0x80330F00, 0x80330F2E, 0x803612C0, 0x803612E0, "background", header.struct_background, """
#include <sm64/types.h>
"""),
    s_header_code(0x802D0080, 0x802D2208, 0x80330F30, 0x803312F0, 0x803612E0, 0x803612E2, "scroll", header.struct_scroll, """
#include <sm64/types.h>
"""),
    s_header_code(0x802D2210, 0x802D29BC, 0x803312F0, 0x803312FC, 0x803612F0, 0x803612F1, "object_gfx", header.struct_object_gfx, """
#include <sm64/types.h>
"""),
    s_header_code(0x802D29C0, 0x802D5E00, 0x80331300, 0x80331360, 0x80361300, 0x8036131D, "ripple", header.struct_ripple, """
#include <sm64/types.h>
"""),
    s_header_code(0x802D5E00, 0x802D6F18, 0x80331360, 0x80331364, 0x80361320, 0x803613F0, "print", header.struct_print, """
#include <sm64/types.h>
"""),
    s_header_code(0x802D6F20, 0x802DDDEC, 0x80331370, 0x8033174C, 0x803613F0, 0x803613FF, "message", header.struct_message, """
#include <sm64/types.h>
"""),
    s_header_code(0x802DDDF0, 0x802DFD50, 0x80331750, 0x803317A0, 0, 0, "particle_snow", header.struct_particle_snow, """
#include <sm64/types.h>
"""),
    s_header_code(0x802DFD50, 0x802E2094, 0x803317A0, 0x803317D8, 0, 0, "particle_lava", header.struct_particle_lava, """
#include <sm64/types.h>
"""),
    s_header_code(0x802E20A0, 0x802E2CF0, 0x803317E0, 0x803325E8, 0, 0, "obj_data", header.struct_obj_data, """
#include <sm64/types.h>
#include <sm64/o_script.h>
""" + header.str_obj_data_globl),
    s_header_code(0x802E2CF0, 0x802E3E50, 0x803325F0, 0x8033260C, 0x80361440, 0x80361442, "hud", header.struct_hud, """
#include <sm64/types.h>
"""),
    s_header_code(0x802E3E50, 0x802F972C, 0x80332610, 0x8033283C, 0x80361450, 0x80361454, "object_b", header.struct_object_b, """
#include <sm64/types.h>
"""),
    s_header_code(0x802F9730, 0x80314A2C, 0x80332840, 0x80332E4C, 0x80361460, 0x8036148C, "object_c", header.struct_object_c, """
#include <sm64/types.h>
"""),
]

include_main2 = [
    s_header_code(0x80378800, 0x8037B21C, 0x80385F90, 0x8038B802, 0x8038BC90, 0x8038BC9C, "math", header.struct_math, """
#include <sm64/types.h>
""", """
#define sin(x)  math_sin[(u16)(x) >> 4]
#define cos(x)  math_cos[(u16)(x) >> 4]
""", ""),
    s_header_code(0x8037B220, 0x8037CD60, 0x8038B810, 0x8038B810, 0, 0, "g", header.struct_g, """
#include <sm64/types.h>
"""),
    s_header_code(0x8037CD60, 0x8037E19C, 0x8038B810, 0x8038B894, 0x8038BCA0, 0x8038BD9C, "g_script", header.struct_g_script, """
#include <sm64/types.h>
#include <sm64/script.h>
#include <sm64/g.h>
""" + header.str_g_script_globl, header.str_g_script_c, ""),
    s_header_code(0x8037E1A0, 0x80380684, 0x8038B8A0, 0x8038B9AC, 0x8038BDA0, 0x8038BE2C, "s_script", header.struct_s_script, """
#include <sm64/types.h>
#include <sm64/segment.h>
#include <sm64/script.h>
#include <sm64/g_script.h>
""" + header.str_s_script_globl, header.str_s_script_c, header.str_s_script_asm),
    s_header_code(0x80380690, 0x8038248C, 0x8038B9B0, 0x8038B9B0, 0x8038BE30, 0x8038BE90, "map", header.struct_map, """
#include <sm64/types.h>
"""),
    s_header_code(0x80382490, 0x80383B6C, 0x8038B9B0, 0x8038B9B0, 0x8038BE90, 0x8038EED4, "map_data", header.struct_map_data, """
#include <sm64/types.h>
""" + header.str_map_data_globl),
    s_header_code(0x80383B70, 0x80385F88, 0x8038B9B0, 0x8038BA90, 0x8038EEE0, 0x8038EEE2, "o_script", header.struct_o_script, """
#include <sm64/types.h>
#include <sm64/script.h>
#include <sm64/g_script.h>
""" + header.str_o_script_globl, header.str_o_script_c, header.str_o_script_asm),
]

include_menu = [
    s_header_code(0x8016F000, 0x8016F670, 0x801A7830, 0x801A7C3C, 0, 0, "title", header.struct_title, """
#include <sm64/types.h>
"""),
    s_header_code(0x8016F670, 0x80170280, 0x801A7C70, 0x801A7D10, 0x801B99E0, 0x801B99F0, "title_bg", header.struct_title_bg, """
#include <sm64/types.h>
"""),
    s_header_code(0x80170280, 0x801768E0, 0x801A7D10, 0x801A7F3E, 0x801B99F0, 0x801B9A7A, "file_select", header.struct_file_select, """
#include <sm64/types.h>
"""),
    s_header_code(0x801768E0, 0x80177710, 0x801A81A0, 0x801A81B6, 0x801B9A80, 0x801B9AA4, "star_select", header.struct_star_select, """
#include <sm64/types.h>
"""),
]

include_audio = [
    s_header_code(0x80314A30, 0x80316E78, 0x80332E50, 0x80332E50, 0, 0, "a", header.struct_audio_a, """
#include <sm64/types.h>
"""),
    s_header_code(0x80316E80, 0x80318034, 0x80332E50, 0x80332E50, 0, 0, "b", header.struct_audio_b, """
#include <sm64/types.h>
"""),
    s_header_code(0x80318040, 0x80319914, 0x00000000, 0x00000000, 0, 0, "c", header.struct_audio_c, """
#include <sm64/types.h>
"""),
    s_header_code(0x80319920, 0x8031AEDC, 0x80332E50, 0x80332E50, 0, 0, "d", header.struct_audio_d, """
#include <sm64/types.h>
"""),
    s_header_code(0x8031AEE0, 0x8031B82C, 0x80332E50, 0x80332E50, 0, 0, "e", header.struct_audio_e, """
#include <sm64/types.h>
"""),
    s_header_code(0x8031B830, 0x8031E4E4, 0x80332E50, 0x80332E50, 0, 0, "f", header.struct_audio_f, """
#include <sm64/types.h>
"""),
    s_header_code(0x8031E4F0, 0x80322364, 0x80332E50, 0x80332E50, 0, 0, "g", header.struct_audio_g, """
#include <sm64/types.h>
"""),
    s_header_code(0x80246050, 0x80246050, 0x80332E50, 0x80335010, 0, 0, "data", header.struct_audio_data, """
#include <sm64/types.h>
"""),
    s_header_code(0x80246050, 0x80246050, 0x8032D560, 0x8032D560, 0x80220DA0, 0x80226CBC, "bss", header.struct_audio_bss, """
#include <sm64/types.h>
"""),
    s_header_code(0x80246050, 0x80246050, 0x8032D560, 0x8032D560, 0x801CE000, 0x801FF200, "heap", [], """
#include <sm64/types.h>
"""),
]

include_face = [
    s_header_code(0x80177710, 0x80177820, 0x801A81E0, 0x801A81E0, 0, 0, "main", header.struct_face_main, """
#include <sm64/types.h>
"""),
    s_header_code(0x80177820, 0x801781DC, 0x801A81E0, 0x801A81E0, 0, 0, "mem", header.struct_face_mem, """
#include <sm64/types.h>
"""),
    s_header_code(0x801781E0, 0x80178278, 0x00000000, 0x00000000, 0, 0, "sfx", header.struct_face_sfx, """
#include <sm64/types.h>
"""),
    s_header_code(0x80178280, 0x8017BDE4, 0x801A81E0, 0x801A81E0, 0, 0, "draw", header.struct_face_draw, """
#include <sm64/types.h>
"""),
    s_header_code(0x8017BDF0, 0x80181718, 0x801A81E0, 0x801A81E0, 0, 0, "object", header.struct_face_object, """
#include <sm64/types.h>
"""),
    s_header_code(0x80181720, 0x80181D38, 0x801A81E0, 0x801A81E0, 0, 0, "skin", header.struct_face_skin, """
#include <sm64/types.h>
"""),
    s_header_code(0x80181D40, 0x80183A48, 0x801A81E0, 0x801A81E0, 0, 0, "particle", header.struct_face_particle, """
#include <sm64/types.h>
"""),
    s_header_code(0x80183A50, 0x8018B830, 0x801A81E0, 0x801A81E0, 0, 0, "dynlist", header.struct_face_dynlist, """
#include <sm64/types.h>
"""),
    s_header_code(0x8018B830, 0x8018C2F0, 0x801A81E0, 0x801A81E0, 0, 0, "gadget", header.struct_face_gadget, """
#include <sm64/types.h>
"""),
    s_header_code(0x8018C2F0, 0x8018E660, 0x801A81E0, 0x801A81E0, 0, 0, "stdio", header.struct_face_stdio, """
#include <sm64/types.h>
"""),
    s_header_code(0x8018E660, 0x80192050, 0x801A81E0, 0x801A81E0, 0, 0, "joint", header.struct_face_joint, """
#include <sm64/types.h>
"""),
    s_header_code(0x80192050, 0x80193C70, 0x801A81E0, 0x801A81E0, 0, 0, "net", header.struct_face_net, """
#include <sm64/types.h>
"""),
    s_header_code(0x80193C70, 0x801973C0, 0x801A81E0, 0x801A81E0, 0, 0, "math", header.struct_face_math, """
#include <sm64/types.h>
"""),
    s_header_code(0x801973C0, 0x8019B060, 0x801A81E0, 0x801A81E0, 0, 0, "shape", header.struct_face_shape, """
#include <sm64/types.h>
"""),
    s_header_code(0x8019B060, 0x801A7830, 0x801A81E0, 0x801A81E0, 0, 0, "gfx", header.struct_face_gfx, """
#include <sm64/types.h>
"""),
]

src_buffer = [
    [main.s_file, "zimg.c"],
        [main.s_str, str_data],
        [ultra.c.s_bss, 0x80000400, 0x80025C00, "E0", 0x8032D560],
    [main.s_write],
    [main.s_file, "timg.c"],
        [main.s_str, str_data],
        [ultra.c.s_bss, 0x801C1000, 0x801CE000, "E0", 0x8032D560],
    [main.s_write],
    [main.s_file, "buffer.c"],
        [main.s_str, """
#include <sm64/types.h>
#include <sm64/app.h>

"""],
        [ultra.c.s_bss, 0x80200200, 0x80220DA0, "E0", 0x8032D560],
    [main.s_write],
    [main.s_file, "fifo.c"],
        [main.s_str, str_data],
        [ultra.c.s_bss, 0x80227000, 0x80246000, "E0", 0x8032D560],
    [main.s_write],
    [main.s_file, "cimg.c"],
        [main.s_str, str_data],
        [ultra.c.s_bss, 0x8038F800, 0x80400000, "E0", 0x8032D560],
    [main.s_write],
]

src_main = [
    s_code(0x80246050, 0x80246E68, "main", """
#include <sm64/types.h>
#include <sm64/segment.h>
""" + str_code),
    s_code(0x80246E70, 0x80248C3C, "app", """
#include <sm64/types.h>
#include <sm64/app.h>
""" + str_code),
    s_code(0x80248C40, 0x802495DC, "audio"),
    s_code(0x802495E0, 0x8024BFE4, "game", """
#include <sm64/types.h>
#include <sm64/game.h>
#include <sm64/wipe.h>
#include <sm64/hud.h>
""" + str_code),
    s_code(0x8024BFF0, 0x8025093C, "player_touch", """
#include <sm64/types.h>
#include <sm64/player_touch.h>
#include <sm64/hud.h>
""" + str_code),
    s_code(0x80250940, 0x8025507C, "player", """
#include <sm64/types.h>
#include <sm64/hud.h>
""" + str_code),
    s_code(0x80255080, 0x80256DFC, "player_move"),
    s_code(0x80256E00, 0x8025DD68, "player_demo", """
#include <sm64/types.h>
#include <sm64/hud.h>
""" + str_code),
    s_code(0x8025DD70, 0x802608AC, "player_hang"),
    s_code(0x802608B0, 0x80263E5C, "player_stop"),
    s_code(0x80263E60, 0x80269F38, "player_ground"),
    s_code(0x80269F40, 0x80270104, "player_air"),
    s_code(0x80270110, 0x80274EAC, "player_water"),
    s_code(0x80274EB0, 0x802761D0, "player_grab"),
    s_code(0x802761D0, 0x80277ED4, "player_callback", """
#include <sm64/types.h>
#include <sm64/player_callback.h>
#include <sm64/object.h>
#include <sm64/wipe.h>
""" + str_code),
    s_code(0x80277EE0, 0x80279158, "mem", """
#include <sm64/types.h>
#include <sm64/segment.h>
#include <sm64/mem.h>
""" + str_code),
    s_code(0x80279160, 0x8027A7C4, "save"),
    s_code(0x8027A7D0, 0x8027B6C0, "world", """
#include <sm64/types.h>
#include <sm64/world.h>
#include <sm64/wipe.h>
#include <sm64/g.h>
""" + str_code),
    s_code(0x8027B6C0, 0x8027E3DC, "g_draw"),
    s_code(0x8027E3E0, 0x8027F4D4, "time", """
#include <sm64/types.h>
#include <sm64/time.h>
""" + str_code),
    s_code(0x8027F4E0, 0x8027F584, "slidec"),

    s_code(0x8027F590, 0x8029C764, "camera"),

    s_code(0x8029C770, 0x8029C780, "course"),
    s_code(0x8029C780, 0x8029D884, "object", """
#include <sm64/types.h>
#include <sm64/player.h>
#include <sm64/object.h>
""" + str_code),
    s_code(0x8029D890, 0x802A5618, "object_lib", """
#include <sm64/types.h>
#include <sm64/object.h>
""" + str_code),
    s_code(0x802A5620, 0x802C89F0, "object_a", """
#include <sm64/types.h>
#include <sm64/hud.h>
#include <sm64/object.h>
""" + str_code),
    s_code(0x802C89F0, 0x802C8F40, "object_move"),
    s_code(0x802C8F40, 0x802C97C8, "object_touch"),
    s_code(0x802C97D0, 0x802CA03C, "object_list", """
#include <sm64/types.h>
#include <sm64/object.h>
""" + str_code),
    s_code(0x802CA040, 0x802CA370, "object_sfx"),
    s_code(0x802CA370, 0x802CB5B4, "object_debug"),

    s_code(0x802CB5C0, 0x802CD27C, "wipe"),
    s_code(0x802CD280, 0x802CF5A4, "shadow", """
#include <sm64/types.h>
#include <sm64/shadow.h>
""" + str_code),
    s_code(0x802CF5B0, 0x802D007C, "background", """
#include <sm64/types.h>
#include <sm64/background.h>
""" + str_code),
    s_code(0x802D0080, 0x802D2208, "scroll", """
#include <sm64/types.h>
#include <sm64/scroll.h>
""" + str_code),
    s_code(0x802D2210, 0x802D29BC, "object_gfx", """
#include <sm64/types.h>
#include <sm64/hud.h>
""" + str_code),
    s_code(0x802D29C0, 0x802D5E00, "ripple"),

    s_code(0x802D5E00, 0x802D6F18, "print"),
    s_code(0x802D6F20, 0x802DDDEC, "message", """
#include <sm64/types.h>
#include <sm64/hud.h>
""" + str_code),
    s_code(0x802DDDF0, 0x802DFD50, "particle_snow"),
    s_code(0x802DFD50, 0x802E2094, "particle_lava"),
    s_code(0x802E20A0, 0x802E2CF0, "obj_data", """
#include <sm64/types.h>
#include <sm64/object.h>
#include <sm64/obj_data.h>
""" + str_code),
    s_code(0x802E2CF0, 0x802E3E50, "hud", """
#include <sm64/types.h>
#include <sm64/hud.h>
""" + str_code),
    s_code(0x802E3E50, 0x802F972C, "object_b", """
#include <sm64/types.h>
#include <sm64/object.h>
#include <sm64/hud.h>
""" + str_code),

    s_code(0x802F9730, 0x80314A2C, "object_c"),

    s_data(0x8032D560, 0x8032D5C4, 0x80335B60, 0x80335B74, 0x8033A580, 0x8033AF90, "main.data", [
        [0,   7, 1, ultra.c.d_addr, 0],
        [0,   1, c.d_bool_s8],
        [0,   1, 1, ultra.c.d_u32],
        [0,   2, ultra.c.d_align_s8],
        [0,   4, c.d_bool_s8],
        [0, -16, 1, ultra.c.d_flag16, ultra.c.flag_button],
        [0,   2, ultra.c.d_align_s16],
    ], [
        [0, -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], """
#include <sm64/types.h>
#include <sm64/main.h>
"""),
    s_data(0x8032D5D0, 0x8032D5FC, 0x80335B80, 0x80335B88, 0x8033AF90, 0x8033B09C, "app.data", [
        [0, 2, 1, ultra.c.d_u32],
        [0, 2, ultra.c.d_align_u16],
        [0, 1, 1, ultra.c.d_addr, 0],
        [0, 1, 1, ultra.c.d_str, 4, "&controller_table[0]"],
        [0, 1, 1, ultra.c.d_str, 4, "&controller_table[1]"],
        [0, 1, 1, ultra.c.d_str, 4, "&controller_table[2]"],
        [0, 1, 1, ultra.c.d_addr, 0],
        [0, 1, ultra.c.d_align_u16],
        [1, 1, 1, ultra.c.d_str, 4, "0"],
    ], [
        [0, 1, 8, "str"],
    ], """
#include <sm64/types.h>
#include <sm64/main.h>
#include <sm64/app.h>
#include <sm64/mem.h>
"""),
    s_data(0x8032D600, 0x8032D6C1, 0x80335B90, 0x80335B94, 0x8033B0A0, 0x8033B170, "audio.data", [
        [0,  2, ultra.c.d_align_u8],
        [0,  3, [[0, 1, 1, ultra.c.d_u16, "0x%04X"], [0, 1, 2, None]]],
        [0,  1, ultra.c.d_align_u8],
        [1,  1, 1, ultra.c.d_str, 0x10, "0"],
        [1,  1, 4, ultra.c.d_s16],
        [0, -9, 4, ultra.c.d_u32, "0x%08X"],
        [0,  1, 1, ultra.c.d_s8],
    ], [
        [0, 1, 1, ultra.c.d_f32],
    ], """
#include <sm64/types.h>
#include <sm64/main.h>
"""),
    s_data(0x8032D6D0, 0x8032D948, 0x80335BA0, 0x803361A8, 0x8033B170, 0x8033B26F, "game.data", [
        [1, 1, 2, ultra.c.d_addr, 0],
        [1, 1, 3, ultra.c.d_addr, 0],
        [1, 1, 3, ultra.c.d_addr, 0],
        [1, 1, 4, ultra.c.d_addr, 0],
        [1, 1, 4, ultra.c.d_addr, 0],
        [1, 1, 3, ultra.c.d_addr, 0],
        [1, 1, 3, ultra.c.d_addr, 0],
        [1, 1, 4, ultra.c.d_addr, 0],
        [1, 1, 2, ultra.c.d_addr, 0],
        [1, 1, 4, ultra.c.d_addr, 0],
        [1, 1, 3, ultra.c.d_addr, 0],
        [1, 1, 2, ultra.c.d_addr, 0],
        [1, 1, 4, ultra.c.d_addr, 0],
        [1, 1, 2, ultra.c.d_addr, 0],
        [1, 1, 3, ultra.c.d_addr, 0],
        [1, 1, 5, ultra.c.d_addr, 0],
        [1, 1, 4, ultra.c.d_addr, 0],
        [1, 1, 4, ultra.c.d_addr, 0],
        [1, 1, 2, ultra.c.d_addr, 0],
        [1, 1, 2, ultra.c.d_addr, 0],
        [0, -23, 1, c.d_staff],
        [0, 1, 1, ultra.c.d_str, 4, "&player_table[0]"],
        [0, 1, ultra.c.d_align_s16],
        [0, 1, ultra.c.d_align_s8],
    ], [
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0, 1, 24, "str"],
        [0, 1, 20, "str"],
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0, 1, 24, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0, 1, 16, "str"],
        [0, 1, 24, "str"],
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0, 1, 12, "str"],
        [0, 1, 20, "str"],
        [0, 1, 24, "str"],
        [0, 1, 24, "str"],
        [0, 1, 16, "str"],
        [0, 1, 12, "str"],
        [0, 1, 20, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 12, "str"],
        [0, 1, 20, "str"],
        [0, 1, 12, "str"],
        [0, 1, 20, "str"],
        [0, 1, 12, "str"],
        [0, 1, 24, "str"],
        [0, 1, 20, "str"],
        [0, 1, 12, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, -112, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], """
#include <sm64/types.h>
#include <sm64/game.h>
#include <sm64/player.h>
#include <sm64/object.h>
#include <sm64/hud.h>
"""),
    s_data(0x8032D950, 0x8032DA9C, 0x803361B0, 0x8033641C, 0x8033B270, 0x8033B274, "player_touch.data", [
        [0, -31, 1, c.d_player_touch],
        [0, -18, 1, ultra.c.d_u32, "0x%08X"],
        [0, 3, c.d_bool_u8],
    ], [
        [0, -152, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0, 3, 1, ultra.c.d_f32],
    ], """
#include <sm64/types.h>
#include <sm64/player_touch.h>
"""),
    s_data(0x8032DAA0, 0x8032DAE8, 0x80336420, 0x8033666C, 0x8033B280, 0x8033B284, "player.data", [
        [1, -7, 6, ultra.c.d_s8],
        [0, 1, 2, None],
        [0, -4, 4, ultra.c.d_u8],
        [0, 1, 4, None],
        [0, 1, 1, ultra.c.d_u64, "0x%016X"], # bin
    ], [
        [0,   1, 8, "str"],
        [0,   1, 8, "str"],
        [0,   1, 8, "str"],
        [0, -90, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  13, 1, ultra.c.d_f32],
        [0, -33, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   5, 1, ultra.c.d_f32],
    ], str_data),
    s_data(0x8032DAF0, 0x8032DB28, 0x80336670, 0x803366C4, 0x8033B290, 0x8033B294, "player_move.data", [
        [1, 1, 3, ultra.c.d_s16], [0, 1, 2, None],
        [0, 1, c.d_map_face],
    ], [
        [0,   2, 1, ultra.c.d_f32],
        [0, -13, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   6, 1, ultra.c.d_f32],
    ], """
#include <sm64/types.h>
#include <sm64/map.h>
"""),
    s_data(0x8032DB30, 0x8032DC50, 0x803366D0, 0x80336940, 0x8033B2A0, 0x8033B2C0, "player_demo.data", [
        [0,   1, 1, c.d_vp],
        [0,   1, 1, ultra.c.d_addr, 0],
        [0,   2, ultra.c.d_align_s8],
        [1,   1, 7, ultra.c.d_s8],
        [0,   1, 1, None],
        [1,   1, 6, ultra.c.d_u8],
        [0,   1, 2, None],
        [0, -27, 1, c.d_bspline],
        [0,   2, 1, ultra.c.d_s32],
        [0, -10, 2, ultra.c.d_u8],
    ], [
        [0,    1, 1, ultra.c.d_f32],
        [0,   -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,    1, 1, ultra.c.d_f32],
        [0,   -7, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,    6, 1, ultra.c.d_f32],
        [0, -136, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], """
#include <sm64/types.h>
#include <sm64/gbi_ext.h>
#include <sm64/math.h>
"""),
    s_data(0x8032DC50, 0x8032DC50, 0x80336940, 0x80336964, 0, 0, "player_hang.data", [], [
        [0,  4, 1, ultra.c.d_f32],
        [0, -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data),
    s_data(0x8032DC50, 0x8032DC50, 0x80336970, 0x80336A74, 0, 0, "player_stop.data", [], [
        [0,   2, 1, ultra.c.d_f32],
        [0, -63, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data),
    s_data(0x8032DC50, 0x8032DD28, 0x80336A80, 0x80336BF4, 0x8033B2C0, 0x8033B340, "player_ground.data", [
        [0, 9, c.d_player_ground],
    ], [
        [0,  29, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,   3, 1, ultra.c.d_f32],
        [0, -58, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], """
#include <sm64/types.h>
#include <sm64/player_ground.h>
"""),
    s_data(0x8032DD30, 0x8032DD30, 0x80336C00, 0x80336E0C, 0, 0, "player_air.data", [], [
        [0,    7, 1, ultra.c.d_f32],
        [0,   -7, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,    8, 1, ultra.c.d_f32],
        [0,    1, 1, ultra.c.d_f64],
        [0, -107, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data),
    s_data(0x8032DD30, 0x8032DD40, 0x80336E10, 0x80336ECC, 0x8033B340, 0x8033B348, "player_water.data", [
        [0, 2, ultra.c.d_align_s16],
        [1, 1, 4, ultra.c.d_s16],
    ], [
        [0,   1, 1, ultra.c.d_f32],
        [0, -12, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   6, 1, ultra.c.d_f32],
        [0, -28, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data),
    s_data(0x8032DD40, 0x8032DD48, 0x80336ED0, 0x80336F38, 0, 0, "player_grab.data", [
        [1, 1, 8, ultra.c.d_s8],
    ], [
        [0, -26, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data),
    s_data(0x8032DD50, 0x8032DD6A, 0x80336F40, 0x80336F70, 0x8033B350, 0x8033B400, "player_callback.data", [
        [1,  1, 8, ultra.c.d_s8],
        [0, -3, 6, ultra.c.d_s8], [0, 1, 2, None],
        [0,  1, ultra.c.d_align_s16],
    ], [
        [0, -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  2, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,  2, 1, ultra.c.d_f64],
    ], """
#include <sm64/types.h>
#include <sm64/player_callback.h>
#include <sm64/object.h>
"""),
    s_data(0x8032DD70, 0x8032DD74, 0x80336F70, 0x80336F70, 0x8033B400, 0x8033B498, "mem.data", [
        [0, 1, 1, ultra.c.d_addr, 0],
    ], [], """
#include <sm64/types.h>
#include <sm64/mem.h>
"""),
    s_data(0x8032DD80, 0x8032DDBE, 0x80336F70, 0x80336F70, 0x8033B4A0, 0x8033B4A7, "save.data", [
        [0, 6, ultra.c.d_align_u8],
        [0, -38, 1, ultra.c.d_u8],
    ], [], """
#include <sm64/types.h>
"""),
    s_data(0x8032DDC0, 0x8032DE70, 0x80336F70, 0x80336F90, 0x8033B4B0, 0x8033BAE0, "world.data", [
        [0, 7, 1, ultra.c.d_addr, 0],
        [0, 1, ultra.c.d_align_s16],
        [0, 1, 1, ultra.c.d_u32],
        [0, 1, 1, ultra.c.d_u32],
        [0, 3, ultra.c.d_align_u8],
        [0, 2, ultra.c.d_align_s16],
        [0, -20, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0, -20, 1, ultra.c.d_u8],
        [0, 1, 1, c.d_vp],
    ], [
        [0, 1, 16, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
    ], """
#include <sm64/types.h>
#include <sm64/gbi_ext.h>
#include <sm64/world.h>
#include <sm64/wipe.h>
#include <sm64/o_script.h>
"""),
    s_data(0x8032DE70, 0x8032DF0C, 0x80336F90, 0x803370EC, 0x8033BAE0, 0x8033C38C, "g_draw.data", [
        [1, -4, [[0, -8, 1, c.d_rendermode]]],
        [0, 6, 1, ultra.c.d_addr, 0],
        [0, 1, ultra.c.d_align_u16],
    ], [
        [0, 1, 8, "str"],
        [0, 1, 1, ultra.c.d_f32],
        [0, -84, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], """
#include <sm64/types.h>
"""),
    s_data(0x8032DF10, 0x8032DF1C, 0x803370F0, 0x803370F0, 0x8033C390, 0x8033C520, "time.data", [
        [0, 3, ultra.c.d_align_s16],
    ], [], """
#include <sm64/types.h>
#include <sm64/time.h>
"""),
    s_databin(0x8032DF20, 0x8032FEB4, "camera.data"),
    [main.s_file, "camera.S"],
        [main.s_str, """
.data

.globl _camera_data
_camera_data:
    .incbin "src/camera.data.bin"

.bss

.globl _camera_bss
_camera_bss:
    .space 0x6C0
"""],
    [main.s_write],
    s_data(0x8032DF20, 0x8032FEB4, 0x803370F0, 0x80337794, 0, 0, "camera.data", [
    ], [
        [0,  -10, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,    2, 1, ultra.c.d_f32],
        [0,  -10, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   52, 1, ultra.c.d_f32],
        [0,  -17, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,    4, 1, ultra.c.d_f32],
        [0,  -29, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,    9, 1, ultra.c.d_f32],
        [0,   -6, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,    8, 1, ultra.c.d_f32],
        [0,  -11, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   54, 1, ultra.c.d_f32],
        [0, -129, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,    9, 1, ultra.c.d_f32],
        [0,  -65, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,    5, 1, ultra.c.d_f32],
        [0,   -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data),
    s_data(0x8032FEC0, 0x8032FFFC, 0x803377A0, 0x803377B0, 0x8033CBE0, 0x80361266, "object.data", [
        [0, -10, 1, ultra.c.d_s8, fmt_otype],
        [0,  -1, 1, ultra.c.d_s8],
        [0,   1, 1, None],
        [0, -19, 1, c.d_particle],
    ], [
        [0, 2, 1, ultra.c.d_f64],
    ], """
#include <sm64/types.h>
#include <sm64/object.h>
"""),
    s_data(0x80330000, 0x80330018, 0x803377B0, 0x80337848, 0x80361270, 0x80361274, "object_lib.data", [
        [1, 1, 4, ultra.c.d_s8],
        [1, 1, 8, ultra.c.d_s16, "0x%02X"],
        [1, 1, 4, ultra.c.d_s8],
    ], [
        [0,  1, 12, "str"],
        [0,  6, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,  3, 1, ultra.c.d_f64],
        [0,  2, 1, ultra.c.d_f32],
        [0,  1, 1, ultra.c.d_f64],
        [0,  1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,  1, 1, ultra.c.d_f64],
        [0,  9, 1, ultra.c.d_f32],
        [0, -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data),
    s_databin(0x80330020, 0x80330E1C, "object_a.data"),
    [main.s_file, "object_a.S"],
        [main.s_str, """
.data

.globl _object_a_data
_object_a_data:
    .incbin "src/object_a.data.bin"
"""],
    [main.s_write],
    s_data(0x80330020, 0x80330E1C, 0x80337850, 0x80337DF0, 0x80361280, 0x80361282, "object_a.data", [
    ], [
        [0,   1,  4, "str"],
        [0,   2,  8, "str"],
        [0,   1,  4, "str"],
        [0,   2,  8, "str"],
        [0,   3, 12, "str"],
        [0,   3,  8, "str"],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   3, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,   5, 1, ultra.c.d_f32],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   4, 1, ultra.c.d_f64],
        [0,   4, 1, ultra.c.d_f32],
        [0,   2, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   1, 1, ultra.c.d_f64],
        [0,   9, 1, ultra.c.d_f32],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   3, 1, ultra.c.d_f64],
        [0, -10, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   1, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   2, 1, ultra.c.d_f64],
        [0, -10, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   2, 1, ultra.c.d_f64],
        [0,   6, 1, ultra.c.d_f32],
        [0,   1, 1, ultra.c.d_f64],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   2, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,   2, 1, ultra.c.d_f32],
        [0,   2, 1, ultra.c.d_f64],
        [0,   2, 1, ultra.c.d_f32],
        [0,   5, 1, ultra.c.d_f64],
        [0, -12, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   2, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32],
        [0, -10, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   1, 1, ultra.c.d_f32],
        [0,   3, 1, ultra.c.d_f64],
        [0, -11, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   4, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,   4, 1, ultra.c.d_f32],
        [0,   1, 1, ultra.c.d_f64],
        [0,   2, 1, ultra.c.d_f32],
        [0,   1, 1, ultra.c.d_f64],
        [0,   4, 1, ultra.c.d_f32],
        [0,  -8, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   1, 1, ultra.c.d_f32],
        [0,  -8, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   5, 1, ultra.c.d_f32],
        [0,   1, 1, ultra.c.d_f64],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   1, 1, ultra.c.d_f32],
        [0,   1, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   2, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,   8, 1, ultra.c.d_f32],
        [0,   3, 1, ultra.c.d_f64],
        [0,   2, 1, ultra.c.d_f32],
        [0,   1, 1, ultra.c.d_f64],
        [0,   3, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   3, 1, ultra.c.d_f64],
        [0,   5, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   4, 1, ultra.c.d_f64],
        [0,  10, 1, ultra.c.d_f32],
        [0, -11, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   6, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,   2, 1, ultra.c.d_f32],
    ], str_data),
    s_data(0x80330E20, 0x80330E38, 0x80337DF0, 0x80337DF0, 0, 0, "object_move.data", [
        [0, 1, ultra.c.d_align_s16],
        [1, 1, 1, ultra.c.d_str, 0x10, "0"],
        [0, 1, 1, ultra.c.d_addr, 0],
    ], [], str_data),
    s_data(0x80330E40, 0x80330E40, 0x80337DF0, 0x80337DF4, 0, 0, "object_touch.data", [], [
        [0, 1, 4, "str"],
    ]),
    s_data(0x80330E40, 0x80330E40, 0x80337E00, 0x80337E10, 0, 0, "object_list.data", [], [
        [0, 4, 1, ultra.c.d_f32],
    ], str_data),
    s_data(0x80330E40, 0x80330E40, 0x80337E10, 0x80337E1C, 0, 0, "object_sfx.data", [], [
        [0, 3, 1, ultra.c.d_f32],
    ], str_data),
    s_databin(0x80330E40, 0x80330EB2, "object_debug.data"),
    [main.s_file, "object_debug.S"],
        [main.s_str, """
.data

.globl _object_debug_data
_object_debug_data:
    .incbin "src/object_debug.data.bin"

.bss

.globl _object_debug_bss
_object_debug_bss:
    .space 0x20

"""],
    [main.s_write],
    s_data(0x80330E40, 0x80330EB2, 0x80337E20, 0x80337FF8, 0, 0, "object_debug.data", [
    ], [
        [0,  8,  8, "str"],
        [0,  1,  4, "str"],
        [0,  8,  8, "str"],
        [0,  1,  4, "str"],
        [0,  1, 12, "str"],
        [0,  7,  8, "str"],
        [0,  6, 12, "str"],
        [0,  1, 16, "str"],
        [0,  2, 12, "str"],
        [0,  1,  8, "str"],
        [0, 10, 12, "str"],
        [0,  1, 16, "str"],
        [0, 1, 4, None],
        [0, 1, 1, ultra.c.d_f64],
    ], str_data),
    s_data(0x80330EC0, 0x80330ED8, 0x80338000, 0x80338060, 0, 0, "wipe.data", [
        [1, 2, 1, ultra.c.d_str, 4, "0"],
        [0, -4, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], [
        [0,   2, 1, ultra.c.d_f64],
        [0, -20, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data),
    s_data(0x80330EE0, 0x80330EF8, 0x80338060, 0x8033813C, 0x803612B0, 0x803612B6, "shadow.data", [
        [0, -2, 1, c.d_shadow_rect],
    ], [
        [0,  15, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   3, 1, ultra.c.d_f64],
        [0, -13, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], """
#include <sm64/types.h>
#include <sm64/shadow.h>
"""),
    s_data(0x80330F00, 0x80330F2E, 0x80338140, 0x80338160, 0x803612C0, 0x803612E0, "background.data", [
        [0, -10, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [1, -2, 3, ultra.c.d_u8, "0x%02X"],
    ], [
        [0, 4, 1, ultra.c.d_f64],
    ], """
#include <sm64/types.h>
#include <sm64/background.h>
"""),
    s_data(0x80330F30, 0x803312F0, 0x80338160, 0x80338168, 0x803612E0, 0x803612E2, "scroll.data", [
        [0,   2, ultra.c.d_align_s16],
        [0,   1, ultra.c.d_align_s8],
        [0,   1, 1, ultra.c.d_f32],
        [0,   1, 1, ultra.c.d_s32],
        [0,  -8, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0, -25, 1, c.d_scroll],
        [1,   1, 8, ultra.c.d_s8],
    ], [
        [0, 1, 1, ultra.c.d_f64],
    ], """
#include <sm64/types.h>
#include <sm64/scroll.h>
#include <sm64/g_script.h>
"""),
    s_data(0x803312F0, 0x803312FC, 0x80338170, 0x80338170, 0x803612F0, 0x803612F1, "object_gfx.data", [
        [0, 3, ultra.c.d_align_s16],
    ], [], str_data),
    s_data(0x80331300, 0x80331360, 0x80338170, 0x80338198, 0x80361300, 0x8036131D, "ripple.data", [
        [0, -19, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  -3, 1, ultra.c.d_addr, 0],
        [0,   2, ultra.c.d_align_s16],
    ], [
        [0, 5, 1, ultra.c.d_f64],
    ], str_data),
    s_data(0x80331360, 0x80331364, 0x803381A0, 0x803381A0, 0x80361320, 0x803613F0, "print.data", [
        [0, 1, ultra.c.d_align_s16],
    ], [], str_data),
    [main.s_file, "message.data.c"],
        [main.s_str, str_data],
        [main.s_str, "\n"],
        [ultra.c.s_data, 0x803381A0, 0x80338278, "E0", [
            [0,   3, 1, ultra.c.d_f64],
            [0, -48, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        ]],
        [main.s_str, "\n"],
        [ultra.c.s_bss, 0x803613F0, 0x803613FF, "E0", 0x803381A0],
        [main.s_str, "\n"],
        [ultra.c.s_data, 0x80331370, 0x803314A4, "E0", [
            [0, -16, 16, ultra.c.d_u8],
            [0, 1, ultra.c.d_align_s8],
            [0, 2, 1, ultra.c.d_f32],
            [0, 1, ultra.c.d_align_s16],
            [0, 1, ultra.c.d_align_s8],
            [0, 3, ultra.c.d_align_s16],
            [0, 2, ultra.c.d_align_s8],
            [0, 2, ultra.c.d_align_u8],
            [0, 1, 1, ultra.c.d_s32],
            [1, -1, 4, ultra.c.d_u8, "0x%02X"], [0, 1, 1, None],
            [1, -1, 4, ultra.c.d_u8, "0x%02X"], [0, 1, 3, None],
        ]],
        [c.s_msg, 0x803314B0, 0x803314C0, "E0", 0, "message_a", None, [
            (0, "en_p", "803314B0"),
            (0, "en_p", "803314B4"),
            (0, "en_p", "803314B8"),
            (0, "en_p", "803314BC"),
        ]],
        [ultra.c.s_data, 0x803314C0, 0x803314FC, "E0", [
            [1, -1, 4, ultra.c.d_u8, "0x%02X"], [0, 1, 1, None],
            [1, -1, 4, ultra.c.d_u8, "0x%02X"], [0, 1, 3, None],
            [1, 1, 5, ultra.c.d_s16], [0, 1, 2, None],
            [1, 1, 4, ultra.c.d_s16],
            [1, 1, 5, ultra.c.d_s16], [0, 1, 2, None],
            [1, 1, 5, ultra.c.d_s16], [0, 1, 2, None],
            [0, 1, ultra.c.d_align_s16],
        ]],
        [c.s_msg, 0x803315E4, 0x8033160C, "E0", 1, "803315E4", "en", None],
        [ultra.c.s_data, 0x8033160C, 0x80331624, "E0", [
            [0, 1, ultra.c.d_align_u16],
            [0, 3, ultra.c.d_align_s16],
            [0, 2, ultra.c.d_align_s8],
        ]],
        [c.s_msg, 0x80331624, 0x803316C8, "E0", 0, "message_c", None, [
            (0, "en", "80331624"),
            (0, "en", "8033162C"),
            (0, "en", "80331638"),
            (0, "en", "8033163C"),
            (0, "en", "80331640"),
            (0, "en", "80331650"),
            (0, "en", "80331660"),
            (0, "en", "80331674"),
            (0, "en", "80331684"),
            (0, "en", "80331690"),
            (0, "en", "8033169C"),
            (0, "en", "803316B4"),
            (0, "en", "803316BC"),
            (0, "en", "803316C0"),
            (0, "en", "803316C4"),
        ]],
        [ultra.c.s_data, 0x803316C8, 0x803316D8, "E0", [
            [0, 1, ultra.c.d_align_s8],
            [0, 2, 1, ultra.c.d_s32],
            [0, 1, ultra.c.d_align_s8],
        ]],
        [c.s_msg, 0x803316D8, 0x8033174C, "E0", 0, "message_d", None, [
            (0, "en",   "803316D8"),
            (0, "en",   "803316E4"),
            (0, "en_p", "803316F4"),
            (0, "en_p", "803316F8"),
            (0, "en",   "803316FC"),
            (0, "en",   "80331704"),
            (0, "en",   "8033170C"),
            (0, "en_p", "80331714"),
            (0, "en",   "80331718"),
            (0, "en",   "80331728"),
            (0, "en",   "80331734"),
        ]],
    [main.s_write],
    s_databin(0x80331750, 0x803317A0, "particle_snow.data"),
    [main.s_file, "particle_snow.S"],
        [main.s_str, """
.data

.globl _particle_snow_data
_particle_snow_data:
    .incbin "src/particle_snow.data.bin"

.bss

.globl _particle_snow_bss
_particle_snow_bss:
    .space 0x20
"""],
    [main.s_write],
    s_data(0x80331750, 0x803317A0, 0x80338280, 0x803382B8, 0, 0, "particle_snow.data", [
    ], [
        [0, 7, 1, ultra.c.d_f64],
    ], str_data),
    s_databin(0x803317A0, 0x803317D8, "particle_lava.data"),
    [main.s_file, "particle_lava.S"],
        [main.s_str, """
.data

.globl _particle_lava_data
_particle_lava_data:
    .incbin "src/particle_lava.data.bin"

.bss

.globl _particle_lava_bss
_particle_lava_bss:
    .space 0x20
"""],
    [main.s_write],
    s_data(0x803317A0, 0x803317D8, 0x803382C0, 0x80338310, 0, 0, "particle_lava.data", [
    ], [
        [0,   5, 1, ultra.c.d_f32],
        [0, -15, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data),
    s_data(0x803317E0, 0x803325E8, 0x80338310, 0x8033837C, 0, 0, "obj_data.data", [
        [0, -366, 1, c.d_obj_data],
        [0,  -83, 1, c.d_map_obj],
    ], [
        [0, -27, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], """
#include <sm64/types.h>
#include <sm64/obj_data.h>
#include <sm64/g_script.h>
"""),
    s_data(0x803325F0, 0x8033260C, 0x80338380, 0x803383D0, 0x80361440, 0x80361442, "hud.data", [
        [0, 1, 1, c.d_power],
        [0, 1, 1, ultra.c.d_s32],
        [0, 3, ultra.c.d_align_s16],
    ], [
        [0, 10, 4, "str"],
        [0,  1, 8, "str"],
        [0,  1, 4, "str"],
        [0,  1, 8, "str"],
        [0,  1, 4, "str"],
        [0,  2, 1, ultra.c.d_f64],
    ], """
#include <sm64/types.h>
#include <sm64/hud.h>
"""),
    s_databin(0x80332610, 0x8033283C, "object_b.data"),
    [main.s_file, "object_b.S"],
        [main.s_str, """
.data

.globl _object_b_data
_object_b_data:
    .incbin "src/object_b.data.bin"
"""],
    [main.s_write],
    s_data(0x80332610, 0x8033283C, 0x803383D0, 0x803389A4, 0x80361450, 0x80361454, "object_b.data", [
    ], [
        [0,  21, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   2, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32],
        [0, -10, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  18, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   2, 1, ultra.c.d_f64],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN], [0, 1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   6, 1, ultra.c.d_f64],
        [0,  11, 1, ultra.c.d_f32],
        [0,  -6, 1, ultra.c.d_addr, ultra.c.A_EXTERN], [0, 1, 4, None],
        [0,   5, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   3, 1, ultra.c.d_f64],
        [0,  15, 1, ultra.c.d_f32],
        [0, -16, 1, ultra.c.d_addr, ultra.c.A_EXTERN], [0, 1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  10, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   3, 1, ultra.c.d_f64],
        [0,   4, 1, ultra.c.d_f32],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   6, 1, ultra.c.d_f32],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   4, 1, ultra.c.d_f32],
        [0,   1, 1, ultra.c.d_f64],
        [0, -36, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   3, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   2, 1, ultra.c.d_f64],
        [0,  11, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   3, 1, ultra.c.d_f64],
        [0,  -7, 1, ultra.c.d_addr, ultra.c.A_EXTERN], [0, 1, 4, None],
        [0,  20, 1, ultra.c.d_f64],
        [0,   3, 1, ultra.c.d_f32], [0, 1, 4, None],
        [0,   2, 1, ultra.c.d_f64],
        [0,   8, 1, ultra.c.d_f32],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   3, 1, ultra.c.d_f32],
        [0,   1, 1, ultra.c.d_f64],
        [0,   4, 1, ultra.c.d_f32],
        [0, -11, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data),
    s_databin(0x80332840, 0x80332E4C, "object_c.data"),
    [main.s_file, "object_c.S"],
        [main.s_str, """
.data

.globl _object_c_data
_object_c_data:
    .incbin "src/object_c.data.bin"
"""],
    [main.s_write],
    s_data(0x80332840, 0x80332E4C, 0x803389B0, 0x80338D94, 0x80361460, 0x8036148C, "object_c.data", [
    ], [
        [0,   2, 1, ultra.c.d_f32],
        [0,  -9, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  21, 1, ultra.c.d_f32],
        [0,  -7, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  22, 1, ultra.c.d_f32],
        [0,  -6, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   4, 1, ultra.c.d_f32],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  23, 1, ultra.c.d_f32],
        [0,  -8, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   4, 1, ultra.c.d_f32],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  18, 1, ultra.c.d_f32],
        [0,  -8, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   8, 1, ultra.c.d_f32],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   7, 1, ultra.c.d_f32],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  12, 1, ultra.c.d_f32],
        [0,  -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   4, 1, ultra.c.d_f32],
        [0, -15, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   6, 1, ultra.c.d_f32],
        [0,  -8, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   8, 1, ultra.c.d_f32],
        [0,  -6, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  18, 1, ultra.c.d_f32],
    ], str_data),
]

src_main2 = [
    s_code(0x80378800, 0x8037B21C, "math"),
    s_code(0x8037B220, 0x8037CD60, "g"),
    s_code(0x8037CD60, 0x8037E19C, "g_script"),
    s_code(0x8037E1A0, 0x80380684, "s_script", """
#include <sm64/types.h>
#include <sm64/world.h>
""" + str_code),
    s_code(0x80380690, 0x8038248C, "map"),
    s_code(0x80382490, 0x80383B6C, "map_data"),
    s_code(0x80383B70, 0x80385F88, "o_script"),

    s_data(0x80385F90, 0x80385FF8, 0x8038BA90, 0x8038BAEC, 0x8038BC90, 0x8038BC9C, "math.data", [
        [0, 1, 1, c.d_matrix],
        [1, 1, 3, ultra.c.d_f32],
        [1, 1, 3, ultra.c.d_s16], [0, 1, 2, None],
        [1, 1, 3, ultra.c.d_f32],
        [1, 1, 3, ultra.c.d_s16], [0, 1, 2, None],
    ], [
        [0, 1, 1, ultra.c.d_f64],
        [0, -5, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0, 16, 1, ultra.c.d_f32],
    ], str_gfx),
    [main.s_file, "math_table.S"],
        [main.s_str, """
.data

"""],
        [ultra.asm.s_data, 0x80386000, 0x8038B802, "E0", [
            [0x1400, 1, ultra.asm.d_float],
            [  0x80, 8, ultra.asm.d_half],
            [     1, 1, ultra.asm.d_half],
        ]],
    [main.s_write],
    s_data(0x8038B810, 0x8038B894, 0x8038BAF0, 0x8038BAF0, 0x8038BCA0, 0x8038BD9C, "g_script.data", [
        [0, -0x21, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], [], """
#include <sm64/types.h>
#include <sm64/g.h>
"""),
    s_data(0x8038B8A0, 0x8038B9AC, 0x8038BAF0, 0x8038BB38, 0x8038BDA0, 0x8038BE2C, "s_script.data", [
        [0, 1, 1, ultra.c.d_addr, 0],
        [0, 2, ultra.c.d_align_u16],
        [0, 1, ultra.c.d_align_s16],
        [0, 2, 1, ultra.c.d_addr, 0],
        [0, -0x3D, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], [
        [0, -18, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], str_data),
    s_data(0x8038B9B0, 0x8038B9B0, 0x8038BB40, 0x8038BBB0, 0x8038BE30, 0x8038BE90, "map.data", [], [
        [0, 1, 12, "str"],
        [0, 3,  8, "str"],
        [0, 3,  4, "str"],
        [0, 3, 12, "str"],
        [0, 7, 1, ultra.c.d_f32],
    ], str_data),
    s_data(0x8038B9B0, 0x8038B9B0, 0x8038BBB0, 0x8038BC84, 0x8038BE90, 0x8038EED4, "map_data.data", [], [
        [0, 5, 1, ultra.c.d_f64],
        [0, -42, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0, 1, 1, ultra.c.d_f32],
    ], str_data),
    s_data(0x8038B9B0, 0x8038BA90, 0x8038BC90, 0x8038BC90, 0x8038EEE0, 0x8038EEE2, "o_script.data", [
        [0, -0x38, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ], [], str_data),
]

src_menu = [
    s_code(0x8016F000, 0x8016F670, "title", """
#include <sm64/types.h>
#include <sm64/mem.h>
""" + str_code),
    s_code(0x8016F670, 0x80170280, "title_bg"),
    s_code(0x80170280, 0x801768E0, "file_select"),
    s_code(0x801768E0, 0x80177710, "star_select"),

    s_data(0x801A7830, 0x801A7C3C, 0x801A7C40, 0x801A7C68, 0, 0, "title.data", [
        [0, -38, 16, "str"],
        [0, 26, 16, None],
        [0, 1, ultra.c.d_align_u16],
        [0, 2, ultra.c.d_align_s16],
    ], [
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0, 1,  4, "str"],
    ], str_data),
    s_data(0x801A7C70, 0x801A7D10, 0x801A7D10, 0x801A7D10, 0x801B99E0, 0x801B99F0, "title_bg.data", [
        [0, -4, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0, -6, 4, ultra.c.d_f32],
        [0, -2, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0, -3, 4, ultra.c.d_s8],
        [0, -1, 1, ultra.c.d_addr, 0],
        [0, -3, 4, ultra.c.d_s8],
        [0, -1, 4, ultra.c.d_s8],
        [0, -1, 1, ultra.c.d_s8],
        [0, -1, 4, ultra.c.d_s8],
        [0, -1, 3, ultra.c.d_s8],
    ], [], str_data),
    [main.s_file, "file_select.data.c"],
        [main.s_str, str_data],
        [main.s_str, "\n"],
        [ultra.c.s_data, 0x801A7F40, 0x801A8194, "E0", [
            [0,    1, 1, ultra.c.d_f32], [0, 1, 4, None],
            [0,    7, 1, ultra.c.d_f64],
            [0,   -7, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
            [0,   24, 1, ultra.c.d_f32],
            [0, -102, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        ]],
        [main.s_str, "\n"],
        [ultra.c.s_bss, 0x801B99F0, 0x801B9A7A, "E0", 0x801A7D10],
        [main.s_str, "\n"],
        [ultra.c.s_data, 0x801A7D10, 0x801A7D54, "E0", [
            [0, 2, ultra.c.d_align_s8],
            [0, 1, ultra.c.d_align_u8],
            [1, 1, 2, ultra.c.d_f32],
            [0, 1, ultra.c.d_align_s16],
            [1, 1, 2, ultra.c.d_s16],
            [0, 3, ultra.c.d_align_s8],
            [0, 1, ultra.c.d_align_u8],
            [0, 1, ultra.c.d_align_s16],
            [0, 5, ultra.c.d_align_s8],
        ]],
        [c.s_msg, 0x801A7D54, 0x801A7F3C, "E0", 0, "file_select", None, [
            (0, "en",   "801A7D54"),
            (0, "en",   "801A7D5C"),
            (0, "en",   "801A7D68"),
            (0, "en",   "801A7D74"),
            (1, "en",   "801A7D80", 8, 3),
            (0, "en",   "801A7D98"),
            (0, "en",   "801A7DA0"),
            (0, "en",   "801A7DA8"),
            (0, "en",   "801A7DB0"),
            (0, "en",   "801A7DB8"),
            (0, "en_p", "801A7DBC"),
            (0, "en_p", "801A7DC0"),
            (0, "en",   "801A7DC4"),
            (0, "en",   "801A7DD0"),
            (0, "en",   "801A7DD8"),
            (0, "en",   "801A7DE0"),
            (0, "en",   "801A7DE8"),
            (0, "en",   "801A7DF4"),
            (0, "en",   "801A7E0C"),
            (0, "en",   "801A7E18"),
            (0, "en",   "801A7E2C"),
            (0, "en",   "801A7E44"),
            (0, "en",   "801A7E58"),
            (0, "en",   "801A7E6C"),
            (0, "en",   "801A7E7C"),
            (0, "en",   "801A7E80"),
            (0, "en",   "801A7E84"),
            (0, "en",   "801A7E90"),
            (0, "en",   "801A7E98"),
            (0, "en",   "801A7EB0"),
            (0, "en",   "801A7EC4"),
            (0, "en",   "801A7ED8"),
            (0, "en",   "801A7EE8"),
            (0, "en",   "801A7EEC"),
            (0, "en",   "801A7EF0"),
            (1, "en_s", "801A7EF4", 8, 5),
            (0, "en",   "801A7F1C"),
            (0, "en",   "801A7F24"),
            (0, "en",   "801A7F30"),
        ]],
        [ultra.c.s_data, 0x801A7F3C, 0x801A7F3E, "E0", [
            [0, 1, 1, ultra.c.d_s16, "0x%02X"],
        ]],
    [main.s_write],
    [main.s_file, "star_select.data.c"],
        [main.s_str, str_data],
        [main.s_str, "\n"],
        [ultra.c.s_data, 0x801A81C0, 0x801A81E0, "E0", [
            [0, 3, 1, ultra.c.d_f64],
            [0, 2, 1, ultra.c.d_f32],
        ]],
        [main.s_str, "\n"],
        [ultra.c.s_bss, 0x801B9A80, 0x801B9AA4, "E0", 0x801A81A0],
        [main.s_str, "\n"],
        [ultra.c.s_data, 0x801A81A0, 0x801A81AC, "E0", [
            [0, 2, ultra.c.d_align_s8],
            [0, 1, 1, ultra.c.d_s32],
        ]],
        [c.s_msg, 0x801A81AC, 0x801A81B4, "E0", 0, "star_select", None, [
            (0, "en", "801A81AC"),
        ]],
        [ultra.c.s_data, 0x801A81B4, 0x801A81B6, "E0", [
            [0, 1, 1, ultra.c.d_u16, "0x%02X"],
        ]],
    [main.s_write],
]

src_audio = [
    s_code(0x80314A30, 0x80316E78, "a"),
    s_code(0x80316E80, 0x80318034, "b"),
    s_code(0x80318040, 0x80319914, "c"),
    s_code(0x80319920, 0x8031AEDC, "d"),
    s_code(0x8031AEE0, 0x8031B82C, "e"),
    s_code(0x8031B830, 0x8031E4E4, "f"),
    s_code(0x8031E4F0, 0x80322364, "g"),

    s_data(0x80332E50, 0x80332E50, 0x80338DA0, 0x80338DB4, 0, 0, "a.data", [], [
        [0, 5, 1, ultra.c.d_f32],
    ]),
    s_data(0x80332E50, 0x80332E50, 0x80338DC0, 0x80338E08, 0, 0, "b.data", [], [
        [0, -16, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   2, 1, ultra.c.d_f32],
    ]),
    s_data(0x80332E50, 0x80332E50, 0x80338E10, 0x80338E28, 0, 0, "d.data", [], [
        [0, 6, 1, ultra.c.d_f32],
    ]),
    s_data(0x80332E50, 0x80332E50, 0x80338E30, 0x80338E54, 0, 0, "e.data", [], [
        [0, -9, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ]),
    s_data(0x80332E50, 0x80332E50, 0x80338E60, 0x803394E4, 0, 0, "f.data", [], [
        [0, -417, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ]),
    [main.s_file, "g.S"],
        [main.s_str, """
.bss

.globl _audio_g_bss
_audio_g_bss:
    .space 0x3710
"""],
    [main.s_write],
    s_data(0x80332E50, 0x80332E50, 0x803394F0, 0x803397AC, 0, 0, "g.data", [], [
        [0, 1, 12, "str"],
        [0, 1, 28, "str"],
        [0, 1, 12, "str"],
        [0, 1, 28, "str"],
        [0, 1, 12, "str"],
        [0, 1, 20, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1, 12, "str"],
        [0, 1, 20, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 2, 48, "str"],
        [0, 1,  8, "str"],
        [0, 2,  4, "str"],
        [0, 1,  8, "str"],
        [0, 2,  4, "str"],
        [0, 4, 12, "str"],
        [0, 1, 24, "str"],
        [0, 1, 28, "str"],
        [0, 5, 16, "str"],
        [0, 1, 12, "str"],
        [0, 1, 20, "str"],
        [0, 1, 32, "str"],
        [0, 1,  4, None],
        [0,   2, 1, ultra.c.d_f64],
        [0,   7, 1, ultra.c.d_f32],
        [0, -28, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ]),
    s_databin(0x80332E50, 0x80335010, "data"),
    [main.s_file, "data.S"],
        [main.s_str, """
.data

.globl _audio_data
_audio_data:
    .incbin "src/audio/data.bin"
"""],
    [main.s_write],
    [main.s_file, "bss.S"],
        [main.s_str, """
.bss

.globl _audio_bss
_audio_bss:
    .space 0x5F1C
"""],
    [main.s_write],
    [main.s_file, "heap.c"],
        [main.s_str, str_data],
        [ultra.c.s_bss, 0x801CE000, 0x80200200, "E0", 0x8032D560],
    [main.s_write],
]

src_face = [
    s_code(0x80177710, 0x80177820, "main"),
    s_code(0x80177820, 0x801781DC, "mem"),
    s_code(0x801781E0, 0x80178278, "sfx"),
    s_code(0x80178280, 0x8017BDE4, "draw"),
    s_code(0x8017BDF0, 0x80181718, "object"),
    s_code(0x80181720, 0x80181D38, "skin"),
    s_code(0x80181D40, 0x80183A48, "particle"),
    s_code(0x80183A50, 0x8018B830, "dynlist"),
    s_code(0x8018B830, 0x8018C2F0, "gadget"),
    s_code(0x8018C2F0, 0x8018E660, "stdio"),
    s_code(0x8018E660, 0x80192050, "joint"),
    s_code(0x80192050, 0x80193C70, "net"),
    s_code(0x80193C70, 0x801973C0, "math"),
    s_code(0x801973C0, 0x8019B060, "shape"),
    s_code(0x8019B060, 0x801A7830, "gfx"),

    s_databin(0x801A81E0, 0x801B54C0, "data"),
    [main.s_file, "data.S"],
        [main.s_str, """
.data

.globl _face_data
_face_data:
    .incbin "src/face/data.bin"

.bss

.globl _face_bss
_face_bss:
    .space 0x5080
"""],
    [main.s_write],

    s_data(0x801A81E0, 0x801A81E0, 0x801B54C0, 0x801B54FC, 0, 0, "main.data", [], [
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 20, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 1, ultra.c.d_f32],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B5500, 0x801B560C, 0, 0, "mem.data", [], [
        [0, 1, 36, "str"],
        [0, 1, 24, "str"],
        [0, 1, 32, "str"],
        [0, 1, 24, "str"],
        [0, 1, 40, "str"],
        [0, 1, 20, "str"],
        [0, 1,  4, "str"],
        [0, 1, 20, "str"],
        [0, 1,  4, "str"],
        [0, 1, 20, "str"],
        [0, 1,  4, "str"],
        [0, 1, 20, "str"],
        [0, 1,  4, "str"],
        [0, 1, 16, "str"],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B5610, 0x801B5914, 0, 0, "draw.data", [], [
        [0, 1, 12, "str"],
        [0, 1, 28, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 44, "str"],
        [0, 1,  8, "str"],
        [0, 1, 20, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 16, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 44, "str"],
        [0, 1, 48, "str"],
        [0, 1, 24, "str"],
        [0, 1, 40, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1, 36, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0,   2, 1, ultra.c.d_f64],
        [0, -12, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   4, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B5920, 0x801B5ED8, 0, 0, "object.data", [], [
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 32, "str"],
        [0, 1, 36, "str"],
        [0, 1,  8, "str"],
        [0, 1, 28, "str"],
        [0, 1,  8, "str"],
        [0, 1, 28, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 20, "str"],
        [0, 1, 28, "str"],
        [0, 1, 24, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1, 12, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1, 12, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1, 28, "str"],
        [0, 1, 44, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 12, "str"],
        [0,   6, 1, ultra.c.d_f32],
        [0, -64, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   2, 1, ultra.c.d_f32],
        [0,   1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32],
        [0, -32, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   1, 4, None],
        [0,   5, 1, ultra.c.d_f64],
        [0,   1, 1, ultra.c.d_f32],
        [0, -11, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   2, 1, ultra.c.d_f64],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B5EE0, 0x801B5F38, 0, 0, "skin.data", [], [
        [0, 1, 44, "str"],
        [0, 1, 44, "str"],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B5F40, 0x801B5FD8, 0, 0, "particle.data", [], [
        [0, 1, 36, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 4, 1, ultra.c.d_f64],
        [0, 1, 1, ultra.c.d_f32],
        [0, 1, 4, None],
        [0, 4, 1, ultra.c.d_f64],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B5FE0, 0x801B812C, 0, 0, "dynlist.data", [], [
        [0, 1,  8, "str"],
        [0, 1, 36, "str"],
        [0, 1, 32, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1, 44, "str"],
        [0, 1, 28, "str"],
        [0, 1,  8, "str"],
        [0, 1, 44, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1, 56, "str"],
        [0, 1, 32, "str"],
        [0, 1, 40, "str"],
        [0, 1,  4, "str"],
        [0, 1, 40, "str"],
        [0, 1, 32, "str"],
        [0, 1, 36, "str"],
        [0, 1, 32, "str"],
        [0, 1, 52, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 12, "str"],
        [0, 1, 52, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0, 1, 32, "str"],
        [0, 1, 36, "str"],
        [0, 1, 32, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 24, "str"],
        [0, 1, 24, "str"],
        [0, 1, 32, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 40, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 40, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 40, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 40, "str"],
        [0, 1, 52, "str"],
        [0, 1, 20, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 20, "str"],
        [0, 1, 40, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 32, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 20, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 20, "str"],
        [0, 1, 56, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 20, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1,  8, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 32, "str"],
        [0, 1, 52, "str"],
        [0, 1, 32, "str"],
        [0, 1, 52, "str"],
        [0, 1, 32, "str"],
        [0, 1, 52, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 28, "str"],
        [0, 1, 12, "str"],
        [0, 1, 52, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 12, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 20, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 16, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 20, "str"],
        [0, 1, 36, "str"],
        [0, 1, 52, "str"],
        [0, 1, 20, "str"],
        [0, -75, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   1, 1, ultra.c.d_f32],
        [0, -73, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B8130, 0x801B82F0, 0, 0, "gadget.data", [], [
        [0, 1,  24, "str"],
        [0, 1,  16, "str"],
        [0, 1,  12, "str"],
        [0, 1,  24, "str"],
        [0, 1,  76, "str"],
        [0, 1, 120, "str"],
        [0, 1,  24, "str"],
        [0, 1,  16, "str"],
        [0, 1,  24, "str"],
        [0, 1,  16, "str"],
        [0, 1,  36, "str"],
        [0, 1,  24, "str"],
        [0, 1,  16, "str"],
        [0, 1, 4, None],
        [0, 2, 1, ultra.c.d_f64],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B82F0, 0x801B85B0, 0, 0, "stdio.data", [], [
        [0, 1, 32, "str"],
        [0, 1, 28, "str"],
        [0, 1,  4, "str"],
        [0, 1, 24, "str"],
        [0, 1, 28, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 24, "str"],
        [0, 1, 56, "str"],
        [0, 1, 44, "str"],
        [0, 1, 44, "str"],
        [0, 1, 12, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1, 28, "str"],
        [0, 1,  8, "str"],
        [0, 1, 40, "str"],
        [0, 1, 28, "str"],
        [0, 1, 12, "str"],
        [0, 1, 28, "str"],
        [0, 1, 32, "str"],
        [0, 1, 40, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, -22, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B85B0, 0x801B8730, 0, 0, "joint.data", [], [
        [0, 1, 48, "str"],
        [0, 1, 16, "str"],
        [0, 1,  4, "str"],
        [0, 1, 20, "str"],
        [0, 1,  4, "str"],
        [0, 1, 16, "str"],
        [0, 1, 32, "str"],
        [0, 1, 28, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1, 32, "str"],
        [0, 1, 32, "str"],
        [0, 1, 4, None],
        [0, 6, 1, ultra.c.d_f64],
        [0, 2, 1, ultra.c.d_f32],
        [0, 8, 1, ultra.c.d_f64],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B8730, 0x801B8964, 0, 0, "net.data", [], [
        [0, 1, 16, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 40, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1,  8, "str"],
        [0, 1, 20, "str"],
        [0, 1, 16, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 20, "str"],
        [0,  3, 1, ultra.c.d_f64],
        [0, -7, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B8970, 0x801B8A60, 0, 0, "math.data", [], [
        [0, 1, 32, "str"],
        [0, 1, 36, "str"],
        [0, 1, 12, "str"],
        [0, 1,  4, "str"],
        [0, 1, 28, "str"],
        [0, 1, 28, "str"],
        [0, 1, 28, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 5, 1, ultra.c.d_f32],
        [0, 4, 1, ultra.c.d_f64],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B8A60, 0x801B8E28, 0, 0, "shape.data", [], [
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 16, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 28, "str"],
        [0, 1,  8, "str"],
        [0, 1, 28, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1, 16, "str"],
        [0, 1, 28, "str"],
        [0, 1, 32, "str"],
        [0, 1, 36, "str"],
        [0, 1, 32, "str"],
        [0, 1, 32, "str"],
        [0, 1, 32, "str"],
        [0, 1, 32, "str"],
        [0, 1, 32, "str"],
        [0, 1, 32, "str"],
        [0, 1, 32, "str"],
        [0, 1,  4, "str"],
        [0, 1, 24, "str"],
        [0, 1, 32, "str"],
        [0, 1, 16, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1, 24, "str"],
        [0, 1,  8, "str"],
        [0, 1, 20, "str"],
        [0, 1, 16, "str"],
        [0, 1,  4, "str"],
        [0, 1,  8, "str"],
        [0, 1, 28, "str"],
        [0, 1, 36, "str"],
        [0, 1, 12, "str"],
        [0, 1,  4, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 16, "str"],
        [0, 1,  8, "str"],
        [0, -8, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  5, 1, ultra.c.d_f32],
    ]),
    s_data(0x801A81E0, 0x801A81E0, 0x801B8E30, 0x801B99E0, 0, 0, "gfx.data", [], [
        [0, 1,  4, "str"],
        [0, 1, 48, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, 1, 16, "str"],
        [0, 1,  8, "str"],
        [0, 1, 52, "str"],
        [0, 1, 48, "str"],
        [0, 1,  8, "str"],
        [0, 1, 48, "str"],
        [0, 1, 44, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 16, "str"],
        [0, 1, 16, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 12, "str"],
        [0, 1, 16, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1, 16, "str"],
        [0, 1,  8, "str"],
        [0, 1, 16, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 32, "str"],
        [0, 1,  4, "str"],
        [0, 1,  8, "str"],
        [0, 1, 40, "str"],
        [0, 1, 12, "str"],
        [0, 1, 40, "str"],
        [0, 1, 12, "str"],
        [0, 1, 40, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 24, "str"],
        [0, 1, 36, "str"],
        [0, 1, 16, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 32, "str"],
        [0, 1, 16, "str"],
        [0, 1, 56, "str"],
        [0, 1, 48, "str"],
        [0, 1, 40, "str"],
        [0, 1, 24, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, 1, 36, "str"],
        [0, 1, 36, "str"],
        [0, 1, 20, "str"],
        [0, 1, 20, "str"],
        [0, 1, 36, "str"],
        [0, 1,  8, "str"],
        [0, 1, 36, "str"],
        [0, 1,  8, "str"],
        [0, 1, 32, "str"],
        [0, 1, 28, "str"],
        [0, 1, 28, "str"],
        [0, 1, 32, "str"],
        [0, 1,  4, "str"],
        [0, 1, 20, "str"],
        [0, 1, 36, "str"],
        [0, 1, 32, "str"],
        [0, 1, 40, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1,  4, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  4, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1,  8, "str"],
        [0, 1, 12, "str"],
        [0, 1, 44, "str"],
        [0, 1, 28, "str"],
        [0, 1, 36, "str"],
        [0, 1, 32, "str"],
        [0, 1, 24, "str"],
        [0, 1, 28, "str"],
        [0, 1,  8, "str"],
        [0, 1, 24, "str"],
        [0,   1, 1, ultra.c.d_f64],
        [0, -34, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,  16, 1, ultra.c.d_f64],
        [0, -19, 1, ultra.c.d_addr, ultra.c.A_EXTERN],
        [0,   1, 4, None],
        [0,   1, 1, ultra.c.d_f64],
    ]),
]

data_main_gfx = [
    [main.s_str, """
#include <sm64/types.h>
#include <sm64/gbi_ext.h>
#include <sm64/message.h>

"""],
    s_dirfile("print", "texture.c"),
        [ultra.c.s_data, 0x02000000, 0x02004A00, "E0.szp", [
            [0, 1, 1, c.d_texture, "rgba16", 16, 16, name]
            for name in list("0123456789abcdefghiklmnoprstuwy") + [
                "squote",
                "dquote",
                "multiply",
                "coin",
                "mario",
                "star",
            ]
        ]],
    s_writepop(),
    s_dirfile("credit", "texture.c"),
        [ultra.c.s_data, 0x02004A00, 0x02005900, "E0.szp", [
            [0, 1, 1, c.d_texture, "rgba16", 8, 8, name]
            for name in list("346abcdefghijklmnopqrstuvwxyz") + ["period"]
        ]],
    s_writepop(),
    s_dirfile("message", "texture.c"),
        [ultra.c.s_data, 0x02005900, 0x02007000, "E0.szp", [
            [0, 1, 1, c.d_texture, "ia4", 16, 8, name]
            for name in list("0123456789") + [
                "u_"+x for x in "abcdefghijklmnopqrstuvwxyz"
            ] + [
                "l_"+x for x in "abcdefghijklmnopqrstuvwxyz"
            ] + [
                "arrow",
                "exclaim",
                "coin",
                "multiply",
                "paren_l",
                "paren_rl",
                "paren_r",
                "tilde",
                "period",
                "percent",
                "bullet",
                "comma",
                "apostrophe",
                "question",
                "star",
                "star_outline",
                "quote_l",
                "quote_r",
                "colon",
                "hyphen",
                "ampersand",
                "button_a",
                "button_b",
                "button_c",
                "button_z",
                "button_r",
                "button_cu",
                "button_cd",
                "button_cl",
                "button_cr",
            ]
        ]],
    s_writepop(),
    s_dirfile("camera", "texture.c"),
        [ultra.c.s_data, 0x02007000, 0x02007700, "E0.szp", [
            [0, 1, 1, c.d_texture, "rgba16", 16, 16, "camera"],
            [0, 1, 1, c.d_texture, "rgba16", 16, 16, "lakitu"],
            [0, 1, 1, c.d_texture, "rgba16", 16, 16, "cross"],
            [0, 1, 1, c.d_texture, "rgba16",  8,  8, "up"],
            [0, 1, 1, c.d_texture, "rgba16",  8,  8, "down"],
        ]],
    s_writepop(),
    s_dirfile("print", "table.c"),
        [ultra.c.s_data, 0x02007700, 0x020077E8, "E0.szp", [
            [0, -58, 1, ultra.c.d_addr, 0],
        ]],
    s_writepop(),
    s_dirfile("message", "table.c"),
        [ultra.c.s_data, 0x020077E8, 0x02007BE8, "E0.szp", [
            [0, -0x100, 1, ultra.c.d_addr, 0],
        ]],
    s_writepop(),
    s_dirfile("credit", "table.c"),
        [ultra.c.s_data, 0x02007BE8, 0x02007C7C, "E0.szp", [
            [0, -37, 1, ultra.c.d_addr, 0],
        ]],
    s_writepop(),
    s_dirfile("camera", "table.c"),
        [ultra.c.s_data, 0x02007C7C, 0x02007C94, "E0.szp", [
            [0, -6, 1, ultra.c.d_addr, 0],
        ]],
    s_writepop(),
    [main.s_str, "\n"],
    [c.s_msg, 0x02007D28, 0x02007D34, "E0.szp", 2, "select", "jp",   None],
    [c.s_msg, 0x02010A68, 0x02010D14, "E0.szp", 2, "en_us",  "en_m", msg_table],
    [c.s_msg, 0x02010F68, 0x02010FD4, "E0.szp", 1, "course", "en_m", msg_course],
    [c.s_msg, 0x0201192C, 0x02011AB4, "E0.szp", 1, "level",  "en_m", None],
    [main.s_str, "\n"],
    [ultra.c.s_data, 0x02011AB8, 0x02011AC0, "E0.szp", [
        [0, 1, 1, ultra.c.d_u64],
    ]],
    [main.s_str, "\n"],
    s_dirfile("print", "gfx.c"),
        [ultra.c.s_data, 0x02011AC0, 0x02011C08, "E0.szp", [
            [0, 1, 1, ultra.c.d_Gfx, 0x02011C08],
        ]],
    s_writepop(),
    s_dirfile("message", "gfx.c"),
        [ultra.c.s_data, 0x02011C08, 0x02011E10, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            [0,  1, 1, ultra.c.d_Gfx, 0x02011C88],
            [0, -4, 1, ultra.c.d_Vtx, False],
            [0,  1, 1, ultra.c.d_Gfx, 0x02011D90],
            [0, -3, 1, ultra.c.d_Vtx, False],
            [0,  1, 1, ultra.c.d_Gfx, 0x02011E10],
        ]],
    s_writepop(),
    s_dirfile("print", "digit.c"),
        [ultra.c.s_data, 0x02011E10, 0x020120B8, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            [0,  1, 1, ultra.c.d_Gfx, 0x020120B8],
        ]],
    s_writepop(),
    s_dirfile("shadow", "texture.c"),
        [ultra.c.s_data, 0x020120B8, 0x020122B8, "E0.szp", [
            [0, 1, 1, c.d_texture, "ia8", 16, 16, "circle"],
            [0, 1, 1, c.d_texture, "ia8", 16, 16, "square"],
        ]],
    s_writepop(),
    s_dirfile("wipe", "texture.c"),
        [ultra.c.s_data, 0x020122B8, 0x02014AB8, "E0.szp", [
            [0, 1, 1, c.d_texture, "ia8", 32, 64, "star"],
            [0, 1, 1, c.d_texture, "ia8", 32, 64, "circle"],
            [0, 1, 1, c.d_texture, "ia8", 64, 64, "mario"],
            [0, 1, 1, c.d_texture, "ia8", 32, 64, "bowser"],
        ]],
    s_writepop(),
    s_dirfile("scroll", "texture.c"),
        [ultra.c.s_data, 0x02014AB8, 0x020172B8, "E0.szp", [
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "water_0"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "water_1"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "water_2"],
            [0, 1, 1, c.d_texture, "ia16",   32, 32, "mist"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "lava"],
        ]],
    s_writepop(),
    [ultra.c.s_data, 0x020172B8, 0x02017380, "E0.szp", [
        [0, 1, 1, ultra.c.d_Lights1],
        [0, 2, 1, c.d_matrix],
        [0, 1, 1, ultra.c.d_Gfx, 0x02017380],
    ]],
    s_dirfile("shadow", "gfx.c"),
        [ultra.c.s_data, 0x02017380, 0x020174C0, "E0.szp", [
            [0, 1, 1, ultra.c.d_Gfx, 0x020174C0],
        ]],
    s_writepop(),
    s_dirfile("wipe", "gfx.c"),
        [ultra.c.s_data, 0x020174C0, 0x02017568, "E0.szp", [
            [0, 1, 1, ultra.c.d_Gfx, 0x02017568],
        ]],
    s_writepop(),
    s_dirfile("background", "gfx.c"),
        [ultra.c.s_data, 0x02017568, 0x020175F0, "E0.szp", [
            [0, 1, 1, ultra.c.d_Gfx, 0x020175F0],
        ]],
    s_writepop(),
    s_dirfile("scroll", "gfx.c"),
        [ultra.c.s_data, 0x020175F0, 0x02017698, "E0.szp", [
            [0, 1, 1, ultra.c.d_Gfx, 0x02017698],
        ]],
    s_writepop(),
    s_dirfile("minimap", "gfx.c"),
        [ultra.c.s_data, 0x02017698, 0x020177B8, "E0.szp", [
            [0, 1, 1, c.d_texture, "ia8", 8, 8, "arrow"],
            [0, 1, 1, ultra.c.d_Gfx, 0x020177B8],
        ]],
    s_writepop(),
    s_dirfile("ripple", "gfx.c"),
        [ultra.c.s_data, 0x020177B8, 0x02018A0E, "E0.szp", [
            [0, 1, 1, ultra.c.d_Lights1],
            [0, 1, 1, ultra.c.d_Gfx, 0x020178C0],
            [0, 2, 1, c.d_ripple_0],
            [0, 1, 2, None],
            [0, 1, 1, c.d_ripple_1, 0x02018A0E],
        ]],
    s_writepop(),
]

data_player_gfx = [
    s_dirfile("mario", "gfx.c"),
        s_script_ifndef(),
        [ultra.c.s_data, 0x04000000, 0x0400C090, "E0.szp", [
            [0, 6, 1, c.d_light, 0.5],
            [0, 1, 1, c.d_texture, "rgba16", 64, 32, "metal"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "button"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "logo"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "sideburn"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "moustache"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "eye_open"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "eye_half"],
            [0, 3, 1, c.d_texture, "rgba16", 32, 32, "eye_closed"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "eye_left"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "eye_right"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "eye_up"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "eye_down"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "eye_dead"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 64, "wing_l"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 64, "wing_r"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 64, "metal_wing_l"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 64, "metal_wing_r"],
        ]],
        s_ply(0x0400CA00, 0x0400CC90, 0x0400CD40, "h_waist",  True),
        s_ply(0x0400D090, 0x0400D1D0, 0x0400D1F8, "h_uarmL",  True),
        s_ply(0x0400D2F8, 0x0400D3E0, 0x0400D3E8, "h_larmL",  True),
        s_ply(0x0400D758, 0x0400D8E8, 0x0400D910, "h_fistL",  True),
        s_ply(0x0400DCA0, 0x0400DDE0, 0x0400DE08, "h_uarmR",  True),
        s_ply(0x0400DF08, 0x0400DFF0, 0x0400DFF8, "h_larmR",  True),
        s_ply(0x0400E2C8, 0x0400E450, 0x0400E4A8, "h_fistR",  True),
        s_ply(0x0400E6A8, 0x0400E7A8, 0x0400E858, "h_thighL", True),
        s_ply(0x0400E918, 0x0400E9C0, 0x0400E9C8, "h_shinL",  True),
        s_ply(0x0400EBB8, 0x0400EC98, 0x0400ECC0, "h_shoeL",  True),
        s_ply(0x0400EEB0, 0x0400EFB0, 0x0400EFD8, "h_thighR", True),
        s_ply(0x0400F1D8, 0x0400F288, 0x0400F290, "h_shinR",  True),
        s_ply(0x0400F400, 0x0400F4E0, 0x0400F568, "h_shoeR",  True),
        [c.s_ply_vtx, "h_torso0"],
        [c.s_ply_vtx, "h_torso2"],
        [c.s_ply_vtx, "h_torso1"],
        [ultra.c.s_data, 0x0400FF28, 0x04010410, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, 0x0400FF80, "h_torso0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0400FF88],
            [0, 1, 1, c.d_ply_gfx, 0x04010258, "h_torso1", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04010260],
            [0, 1, 1, c.d_ply_gfx, 0x04010340, "h_torso2", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04010410],
        ]],
        [c.s_ply_vtx, "h_cap0"],
        [c.s_ply_vtx, "h_cap1"],
        [c.s_ply_vtx, "h_cap2"],
        [c.s_ply_vtx, "h_cap3"],
        [c.s_ply_vtx, "h_cap5"],
        [c.s_ply_vtx, "h_cap4"],
        [c.s_ply_vtx, "h_cap6"],
        [ultra.c.s_data, 0x040112B0, 0x04012190, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, 0x040112E0, "h_cap0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040112E8],
            [0, 1, 1, c.d_ply_gfx, 0x04011348, "h_cap1", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04011350],
            [0, 1, 1, c.d_ply_gfx, 0x04011398, "h_cap2", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040113A0],
            [0, 1, 1, c.d_ply_gfx, 0x04011430, "h_cap3", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04011438],
            [0, 1, 1, c.d_ply_gfx, 0x040116F0, "h_cap4", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040116F8],
            [0, 1, 1, c.d_ply_gfx, 0x04011868, "h_cap5", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04011870],
            [0, 1, 1, c.d_ply_gfx, 0x04011958, "h_cap6", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04012160],
            [0, 2, 1, c.d_light, 0.25],
        ]],
        [c.s_ply_vtx, "h_hair0"],
        [c.s_ply_vtx, "h_hair2"],
        [c.s_ply_vtx, "h_hair1"],
        [c.s_ply_vtx, "h_hair3a"],
        [c.s_ply_vtx, "h_hair4"],
        [c.s_ply_vtx, "h_hair3b"],
        [ultra.c.s_data, 0x040132B0, 0x04014098, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, 0x04013310, "h_hair0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04013318],
            [0, 1, 1, c.d_ply_gfx, 0x040133A0, "h_hair1", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040133A8],
            [0, 1, 1, c.d_ply_gfx, 0x040133F0, "h_hair2", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040133F8],
            [0, 1, 1, c.d_ply_gfx, 0x040136B8, "h_hair3a", True, None],
            [0, 1, 1, c.d_ply_gfx, 0x040136C8, "h_hair3b", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x040136D0],
            [0, 1, 1, c.d_ply_gfx, 0x040139B8, "h_hair4", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04014098],
        ]],
        s_ply(0x040144D8, 0x04014630, 0x040146E0, "m_waist",  True),
        s_ply(0x040147D0, 0x04014838, 0x04014860, "m_uarmL",  True),
        s_ply(0x04014950, 0x040149B8, 0x040149C0, "m_larmL",  True),
        s_ply(0x04014C90, 0x04014DB8, 0x04014DE0, "m_fistL",  True),
        s_ply(0x04014ED0, 0x04014F38, 0x04014F60, "m_uarmR",  True),
        s_ply(0x04015050, 0x040150B8, 0x040150C0, "m_larmR",  True),
        s_ply(0x040153B0, 0x040154D8, 0x04015530, "m_fistR",  True),
        s_ply(0x04015620, 0x040156A8, 0x04015758, "m_thighL", True),
        s_ply(0x04015848, 0x040158D0, 0x040158D8, "m_shinL",  True),
        s_ply(0x04015A98, 0x04015B58, 0x04015B80, "m_shoeL",  True),
        s_ply(0x04015C70, 0x04015CF8, 0x04015D20, "m_thighR", True),
        s_ply(0x04015E10, 0x04015E98, 0x04015EA0, "m_shinR",  True),
        s_ply(0x04016000, 0x040160C0, 0x04016148, "m_shoeR",  True),
        [c.s_ply_vtx, "m_torso0"],
        [c.s_ply_vtx, "m_torso2"],
        [c.s_ply_vtx, "m_torso1"],
        [ultra.c.s_data, 0x04016668, 0x04016968, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, 0x040166B0, "m_torso0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040166B8],
            [0, 1, 1, c.d_ply_gfx, 0x040167F8, "m_torso1", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04016800],
            [0, 1, 1, c.d_ply_gfx, 0x04016898, "m_torso2", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04016968],
        ]],
        s_ply(0x04016A18, 0x04016AB0, 0x04016B60, "l_waist",  True),
        s_ply(0x04016C20, 0x04016C68, 0x04016C90, "l_uarmL",  True),
        s_ply(0x04016D50, 0x04016D98, 0x04016DA0, "l_larmL",  True),
        s_ply(0x04016E20, 0x04016E78, 0x04016EA0, "l_fistL",  True),
        s_ply(0x04016F60, 0x04016FA8, 0x04016FD0, "l_uarmR",  True),
        s_ply(0x04017090, 0x040170D8, 0x040170E0, "l_larmR",  True),
        s_ply(0x04017160, 0x040171B8, 0x04017210, "l_fistR",  True),
        s_ply(0x040172F0, 0x04017358, 0x04017408, "l_thighL", True),
        s_ply(0x040174E8, 0x04017550, 0x04017558, "l_shinL",  True),
        s_ply(0x04017638, 0x040176A0, 0x040176C8, "l_shoeL",  True),
        s_ply(0x040177A8, 0x04017810, 0x04017838, "l_thighR", True),
        s_ply(0x04017918, 0x04017980, 0x04017988, "l_shinR",  True),
        s_ply(0x04017A68, 0x04017AD0, 0x04017B58, "l_shoeR",  True),
        [c.s_ply_vtx, "l_torso0"],
        [c.s_ply_vtx, "l_torso1"],
        [c.s_ply_vtx, "l_torso2"],
        [ultra.c.s_data, 0x04017D68, 0x04017F40, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, 0x04017D90, "l_torso0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04017D98],
            [0, 1, 1, c.d_ply_gfx, 0x04017E18, "l_torso1", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04017E20],
            [0, 1, 1, c.d_ply_gfx, 0x04017E70, "l_torso2", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04017F40],
        ]],
        [c.s_ply_vtx, "l_cap0"],
        [c.s_ply_vtx, "l_cap1"],
        [c.s_ply_vtx, "l_cap2"],
        [c.s_ply_vtx, "l_cap4"],
        [c.s_ply_vtx, "l_cap3"],
        [c.s_ply_vtx, "l_cap5"],
        [ultra.c.s_data, 0x04018270, 0x04018B18, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, 0x04018290, "l_cap0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018298],
            [0, 1, 1, c.d_ply_gfx, 0x040182B8, "l_cap1", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x040182C0],
            [0, 1, 1, c.d_ply_gfx, 0x040182F8, "l_cap2", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018300],
            [0, 1, 1, c.d_ply_gfx, 0x04018368, "l_cap3", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018370],
            [0, 1, 1, c.d_ply_gfx, 0x040183E8, "l_cap4", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x040183F0],
            [0, 1, 1, c.d_ply_gfx, 0x04018418, "l_cap5", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018B18],
        ]],
        [c.s_ply_vtx, "l_hair0"],
        [c.s_ply_vtx, "l_hair1"],
        [c.s_ply_vtx, "l_hair2"],
        [c.s_ply_vtx, "l_hair3"],
        [ultra.c.s_data, 0x04018DC8, 0x04019538, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, 0x04018DE8, "l_hair0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018DF0],
            [0, 1, 1, c.d_ply_gfx, 0x04018E28, "l_hair1", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018E30],
            [0, 1, 1, c.d_ply_gfx, 0x04018E98, "l_hair2", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04018EA0],
            [0, 1, 1, c.d_ply_gfx, 0x04018F60, "l_hair3", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x04019538],
        ]],
        s_ply(0x04019A68, 0x04019C98, 0x04019CC0, "handL", True),
        s_ply(0x0401A1F0, 0x0401A420, 0x0401A478, "handR", True),
        [c.s_ply_vtx, "capR0"],
        [c.s_ply_vtx, "capR2"],
        [c.s_ply_vtx, "capR1"],
        [c.s_ply_vtx, "capR3"],
        [ultra.c.s_data, 0x0401ABA8, 0x0401AF60, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, 0x0401ABC8, "capR0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401ABD0],
            [0, 1, 1, c.d_ply_gfx, 0x0401AD38, "capR1", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401AD40],
            [0, 1, 1, c.d_ply_gfx, 0x0401AEC8, "capR2", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401AED0],
            [0, 1, 1, c.d_ply_gfx, 0x0401AF18, "capR3", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401AF60],
        ]],
        [c.s_ply_vtx, "wingsR_l"],
        [c.s_ply_vtx, "wingsR_r"],
        [ultra.c.s_data, 0x0401B080, 0x0401B2D0, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, 0x0401B0A8, "wingsR_l", True, (32, 64)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401B0B0],
            [0, 1, 1, c.d_ply_gfx, 0x0401B0D8, "wingsR_r", True, (32, 64)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401B2D0],
        ]],
        s_ply(0x0401BC80, 0x0401BF28, 0x0401BF50, "peaceR", True),
        [c.s_ply_vtx, "cap0"],
        [c.s_ply_vtx, "cap1"],
        [c.s_ply_vtx, "cap2"],
        [ultra.c.s_data, 0x0401C330, 0x0401C538, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, 0x0401C360, "cap0", True, (32, 32)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401C368],
            [0, 1, 1, c.d_ply_gfx, 0x0401C4C0, "cap1", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401C4C8],
            [0, 1, 1, c.d_ply_gfx, 0x0401C508, "cap2", True, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401C538],
        ]],
        [c.s_ply_vtx, "wings_l"],
        [c.s_ply_vtx, "wings_r"],
        [ultra.c.s_data, 0x0401C678, 0x0401C940, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, 0x0401C6A0, "wings_l", True, (32, 64)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401C6A8],
            [0, 1, 1, c.d_ply_gfx, 0x0401C6D0, "wings_r", True, (32, 64)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401C940],
        ]],
        [c.s_ply_vtx, "wing_l"],
        [c.s_ply_vtx, "wing_r"],
        [ultra.c.s_data, 0x0401C9C0, 0x04019538, "E0.szp", [
            [0, 1, 1, c.d_ply_gfx, 0x0401C9D8, "wing_l", True, (32, 64)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401C9E0],
            [0, 1, 1, c.d_ply_gfx, 0x0401C9F8, "wing_r", True, (32, 64)],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401CD20],
        ]],
        s_script_else(),
    s_writepop(),
    s_dirfile("bubble", "gfx.c"),
        s_script_ifndef(),
        [ultra.c.s_data, 0x0401CD20, 0x0401DE60, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "a"],
            [0, 1, 1, c.d_texture, "rgba16", 32, 32, "b"],
            [0, 1, 1, ultra.c.d_Gfx, 0x0401DE60],
        ]],
        s_script_else(),
    s_writepop(),
    s_dirfile("dust", "gfx.c"),
        s_script_ifndef(),
        [ultra.c.s_data, 0x0401DE60, 0x040217C0, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            d_texture_n("ia16", 32, 32, 7),
            [0, 1, 1, ultra.c.d_Gfx, 0x040217C0],
        ]],
        s_script_else(),
    s_writepop(),
    s_dirfile("smoke", "gfx.c"),
        s_script_ifndef(),
        [ultra.c.s_data, 0x040217C0, 0x040220C8, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            [0, 1, 1, c.d_texture, "ia16", 32, 32, "texture"],
            [0, 1, 1, ultra.c.d_Gfx, 0x040220C8],
        ]],
        s_script_else(),
    s_writepop(),
    s_dirfile("wave", "gfx.c"),
        s_script_ifndef(),
        [ultra.c.s_data, 0x040220C8, 0x04025318, "E0.szp", [
            [0, -8, 1, ultra.c.d_Vtx, False],
            d_texture_n("ia16", 32, 32, 6),
            [0, 1, 1, ultra.c.d_Gfx, 0x04025318],
        ]],
        s_script_else(),
    s_writepop(),
    s_dirfile("ripple", "gfx.c"),
        s_script_ifndef(),
        [ultra.c.s_data, 0x04025318, 0x04027450, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            d_texture_n("ia16", 32, 32, 4),
            [0, 1, 1, ultra.c.d_Gfx, 0x04027450],
        ]],
        s_script_else(),
    s_writepop(),
    s_dirfile("sparkle", "gfx.c"),
        s_script_ifndef(),
        [ultra.c.s_data, 0x04027450, 0x0402A588, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            d_texture_n("rgba16", 32, 32, -1, start=5, step=-1),
            [0, 1, 1, ultra.c.d_Gfx, 0x0402A588],
        ]],
        s_script_else(),
    s_writepop(),
    s_dirfile("splash", "gfx.c"),
        s_script_ifndef(),
        [ultra.c.s_data, 0x0402A588, 0x04032700, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            d_texture_n("rgba16", 32, 64, 8),
            [0, 1, 1, ultra.c.d_Gfx, 0x04032700],
        ]],
        s_script_else(),
    s_writepop(),
    s_dirfile("droplet", "gfx.c"),
        s_script_ifndef(),
        [ultra.c.s_data, 0x04032700, 0x04032A48, "E0.szp", [
            [0, -8, 1, ultra.c.d_Vtx, False],
            [0, 1, 1, c.d_texture, "rgba16", 16, 16, "texture"],
            [0, 1, 1, ultra.c.d_Gfx, 0x04032A48],
        ]],
    s_writepop(),
    s_dirfile("glow", "gfx.c"),
        s_script_ifndef(),
        [ultra.c.s_data, 0x04032A48, 0x04035378, "E0.szp", [
            [0, -4, 1, ultra.c.d_Vtx, False],
            d_texture_n("ia16", 32, 32, 5),
            [0, 1, 1, ultra.c.d_Gfx, 0x04035378],
        ]],
        s_script_else(),
    s_writepop(),
]

data_player_g = [
    s_dirfile("bubble", "gfx.c"),
        [c.s_script_g, 0x17000000, 0x17000038, "E0"],
        s_script_endif(),
    s_writepop(),
    s_dirfile("dust", "gfx.c"),
        [c.s_script_g, 0x17000038, 0x17000084, "E0"],
        s_script_endif(),
    s_writepop(),
    s_dirfile("smoke", "gfx.c"),
        [c.s_script_g, 0x17000084, 0x1700009C, "E0"],
        s_script_endif(),
    s_writepop(),
    s_dirfile("wave", "gfx.c"),
        [c.s_script_g, 0x1700009C, 0x17000124, "E0"],
        s_script_endif(),
    s_writepop(),
    s_dirfile("ripple", "gfx.c"),
        [c.s_script_g, 0x17000124, 0x170001BC, "E0"],
        s_script_endif(),
    s_writepop(),
    s_dirfile("sparkle", "gfx.c"),
        [c.s_script_g, 0x170001BC, 0x17000230, "E0"],
        s_script_endif(),
    s_writepop(),
    s_dirfile("splash", "gfx.c"),
        [c.s_script_g, 0x17000230, 0x17000284, "E0"],
        s_script_endif(),
    s_writepop(),
    s_dirfile("droplet", "gfx.c"),
        s_script_endif(),
    s_writepop(),
    s_dirfile("glow", "gfx.c"),
        [c.s_script_g, 0x17000284, 0x170002E0, "E0"],
        s_script_endif(),
    s_writepop(),
    s_dirfile("mario", "gfx.c"),
        [c.s_script_g, 0x170002E0, 0x17002E30, "E0"],
        s_script_endif(),
    s_writepop(),
]

data_a1_gfx = [
    s_dirfile("bully", "gfx.c"),
        s_script_ifndef(),
        [c.s_ply_vtx, "horn"],
        [ultra.c.s_data, 0x050000E0, 0x05004720, "E0.szp", [
            [0, 1, 1, c.d_texture, "rgba16", 16, 16, "horn"],
            [0, 1, 1, ultra.c.d_Gfx, 0x050002F8],
            [0, 1, 1, c.d_ply_gfx, 0x05000390, "horn", False, (16, 16)],
            [0, 1, 1, ultra.c.d_Gfx, 0x05000408],
            [0, (0x05000408-0x05004720)//8, 8, ultra.c.d_u8, "0x%02X"],
        ]],
        s_script_else(),
    s_writepop(),
    [ultra.c.s_data, 0x05004720, 0x05004728, "E0.szp", [
        [0, 1, 1, ultra.c.d_u64],
    ]],
    s_dirfile("blargg", "gfx.c"),
        s_script_ifndef(),
        [ultra.c.s_data, 0x05004728, 0x05006178, "E0.szp", [
            [0, (0x05004728-0x05006178)//8, 8, ultra.c.d_u8, "0x%02X"],
        ]],
        s_script_else(),
    s_writepop(),
    [ultra.c.s_data, 0x05006178, 0x05006180, "E0.szp", [
        [0, 1, 1, ultra.c.d_u64],
    ]],
]

data_a1_g = [
    s_dirfile("bully", "gfx.c"),
        [c.s_script_g, 0x0C000000, 0x0C000240, "E0"],
        s_script_endif(),
    s_writepop(),
    s_dirfile("blargg", "gfx.c"),
        [c.s_script_g, 0x0C000240, 0x0C0002B0, "E0"],
        s_script_endif(),
    s_writepop(),
]

data_object = [
    [main.s_file, "object_a.S"],
        [main.s_str, str_o_script],
        [asm.s_script, 0x13000000, 0x13002EB8, "E0", 1],
    [main.s_write],
    [main.s_file, "player.S"],
        [main.s_str, str_o_script],
        [asm.s_script, 0x13002EC0, 0x13002F98, "E0", 1],
    [main.s_write],
    [main.s_file, "object_b.S"],
        [main.s_str, str_o_script],
        [asm.s_script, 0x13002FA0, 0x13004580, "E0", 1],
    [main.s_write],
    [main.s_file, "object_c.S"],
        [main.s_str, str_o_script],
        [asm.s_script, 0x13004580, 0x13005610, "E0", 1],
    [main.s_write],
    [main.s_file, "camera.S"],
        [main.s_str, str_o_script],
        [asm.s_script, 0x13005610, 0x130056BC, "E0", 1],
    [main.s_write],
]

data_game = [
    [asm.s_script, 0x15000000, 0x15000660, "E0", 0],
    [main.s_str, "\n"],
    s_shape_s(0x15000660, 0x1500071C, "c0"),
    s_shape_s(0x1500071C, 0x15000750, "a0"),
    s_shape_s(0x15000750, 0x1500076C, "a1"),
    s_shape_s(0x1500076C, 0x15000788, "a2"),
    s_shape_s(0x15000788, 0x150007B4, "a3"),
    s_shape_s(0x150007B4, 0x150007E8, "a4"),
    s_shape_s(0x150007E8, 0x1500080C, "a5"),
    s_shape_s(0x1500080C, 0x15000830, "a6"),
    s_shape_s(0x15000830, 0x1500084C, "a7"),
    s_shape_s(0x1500084C, 0x15000888, "a8"),
    s_shape_s(0x15000888, 0x150008A4, "a9"),
    s_shape_s(0x150008A4, 0x150008D8, "a10"),
    s_shape_s(0x150008D8, 0x15000914, "b0"),
    s_shape_s(0x15000914, 0x15000958, "b1"),
    s_shape_s(0x15000958, 0x1500099C, "b2"),
    s_shape_s(0x1500099C, 0x150009C0, "b3"),
    s_shape_s(0x150009C0, 0x150009DC, "b4"),
    s_shape_s(0x150009DC, 0x15000A10, "b5"),
]

data_particle_a = [
    [main.s_str, """
#include <sm64/types.h>
#include <sm64/gbi_ext.h>

"""],
    [ultra.c.s_data, 0x0B000000, 0x0B000008, "E0.szp", [
        [0, 1, 1, ultra.c.d_u64],
    ]],
    [main.s_str, "\n"],
    s_dirfile("flower", "texture.c"),
        [ultra.c.s_data, 0x0B000008, 0x0B002020, "E0.szp", [
            d_texture_n("rgba16", 32, 32, 4),
            [0, -6, 1, ultra.c.d_addr, 0],
        ]],
    s_writepop(),
    s_dirfile("lava", "texture.c"),
        [ultra.c.s_data, 0x0B002020, 0x0B006048, "E0.szp", [
            d_texture_n("rgba16", 32, 32, 8),
            [0, -10, 1, ultra.c.d_addr, 0],
        ]],
    s_writepop(),
    s_dirfile("bubble", "texture.c"),
        [ultra.c.s_data, 0x0B006048, 0x0B00684C, "E0.szp", [
            d_texture_n("rgba16", 32, 32, 1),
            [0, -1, 1, ultra.c.d_addr, 0],
        ]],
    s_writepop(),
    s_dirfile("snow", "gfx.c"),
        [ultra.c.s_data, 0x0B00684C, 0x0B006D98, "E0.szp", [
            [0, 1, 1, c.d_texture, "rgba16", 16, 16, "a"],
            [0, 1, 4, None],
            [0, 1, 1, ultra.c.d_Gfx, 0x0B006AD8],
            [0, 1, 1, c.d_texture, "rgba16", 16, 16, "b"],
            [0, 1, 1, ultra.c.d_Gfx, 0x0B006D98],
        ]],
    s_writepop(),
]

lst = [
    [main.s_data, "E0", ["donor", "UNSME0.z64"]],
    [main.s_dir, "include"],
        [main.s_file, "sm64.inc"],
            [ultra.asm.s_definelabel, "E0"],
        [main.s_write],
        s_header(
            "sm64",
            [[main.s_str, header.str_sm64_globl]]
        ),
        [main.s_dir, "sm64"],
            s_header(
                "types",
                [[main.s_str, header.str_types_globl]],
                [[main.s_str, header.str_types_c]],
                [[main.s_str, header.str_types_asm]]
            ),
            s_header(
                "gbi_ext",
                [[main.s_str, str_data]],
                [[main.s_str, header.str_gbi_ext_c]]
            ),
            s_header(
                "segment",
                [[main.s_str, header.str_segment_globl]]
            ),
            s_header(
                "script",
                [[main.s_str, str_data]],
                [[main.s_str, header.str_script_c]],
                [[main.s_str, header.str_script_asm]]
            ),
            [main.s_addr, 0x80246000-0x00001000],
            [main.s_call, include_main],
            [main.s_dir, "audio"],
                [main.s_call, include_audio],
                s_header(
                    "file",
                    asm=[[main.s_str, header.str_audio_file_asm]]
                ),
            [main.s_pop],
            [main.s_addr, 0x80378800-0x000F5580],
            [main.s_call, include_main2],
            [main.s_addr, 0x8016F000-0x0021F4C0],
            [main.s_call, include_menu],
            [main.s_dir, "face"],
                [main.s_call, include_face],
            [main.s_pop],
        [main.s_pop],
    [main.s_pop],
    [main.s_dir, "ultra"],
        [main.s_addr, 0x80246000-0x00001000],
        [main.s_dir, "src"],
            [main.s_call, ultra_src],
        [main.s_pop],
        [main.s_dir, "PR"],
            [main.s_call, ultra_PR],
        [main.s_pop],
        [main.s_addr, 0],
    [main.s_pop],
    [main.s_dir, "src"],
        [main.s_addr, 0x80246000-0x00001000],
        [main.s_call, src_buffer],
        [main.s_call, src_main],
        [main.s_dir, "audio"],
            [main.s_call, src_audio],
        [main.s_pop],
        [main.s_addr, 0x80378800-0x000F5580],
        [main.s_call, src_main2],
        [main.s_addr, 0x8016F000-0x0021F4C0],
        [main.s_call, src_menu],
        [main.s_dir, "face"],
            [main.s_call, src_face],
        [main.s_pop],
        [main.s_addr, 0],
    [main.s_pop],
    [main.s_dir, "data"],
        [main.s_addr, 0x10000000-0x00108A10],
        [main.s_file, "main.S"],
            [main.s_str, str_s_script],
            [asm.s_script, 0x10000000, 0x10000028, "E0", 0],
        [main.s_write],
        s_gfx(0x00108A40, 0x00114750, 0x02, "main", data_main_gfx),
        [main.s_dir, "shape"],
            s_shape(
                0x00114750, 0x001279B0, 0x04, 0x17, "player",
                data_player_gfx, data_player_g
            ),
            s_shapebin(0x0012A7E0, 0x00132850, 0x00015360, 0x0410, 0x0C, "a0"),
            s_shape(
                0x00132C60, 0x00134A70, 0x05, 0x0C, "a1",
                data_a1_gfx, data_a1_g
            ),
            s_shapebin(0x00134D20, 0x0013B5D0, 0x000110A0, 0x0340, 0x0C, "a2"),
            s_shapebin(0x0013B910, 0x00145C10, 0x00013D30, 0x0280, 0x0C, "a3"),
            s_shapebin(0x00145E90, 0x00151B70, 0x00014650, 0x0660, 0x0C, "a4"),
            s_shapebin(0x001521D0, 0x001602E0, 0x000160B8, 0x0384, 0x0C, "a5"),
            s_shapebin(0x00160670, 0x001656E0, 0x0000D130, 0x0364, 0x0C, "a6"),
            s_shapebin(0x00165A50, 0x00166BD0, 0x000034C8, 0x0090, 0x0C, "a7"),
            s_shapebin(0x00166C60, 0x0016D5C0, 0x00010178, 0x02AC, 0x0C, "a8"),
            [main.s_dir, "a9"],
                s_szpbin(0x0016D870, 0x00180540, 0x00024200, "gfx"),
                [main.s_addr, 0x0C000000-0x00180540],
                [main.s_file, "g.c"],
                    [main.s_str, str_g_script],
                    [c.s_script_g, 0x0C000000, 0x0C00045C, "E0"],
                    [main.s_str, "\n\nunused static u64 _0C000460 = 0;\n\n"],
                    [c.s_script_g, 0x0C000468, 0x0C000664, "E0"],
                [main.s_write],
                [main.s_addr, 0],
            [main.s_pop],
            s_shapebin(0x00180BB0, 0x00187FA0, 0x00016EC0, 0x04A0, 0x0C, "a10"),
            s_shapebin(0x00188440, 0x001B9070, 0x00062F10, 0x0C4C, 0x0D, "b0"),
            s_shapebin(0x001B9CC0, 0x001C3DB0, 0x00017960, 0x0480, 0x0D, "b1"),
            s_shapebin(0x001C4230, 0x001D7C90, 0x00025188, 0x0678, 0x0D, "b2"),
            [main.s_dir, "b3"],
                s_szpbin(0x001D8310, 0x001E4BF0, 0x00017E78, "gfx"),
                [main.s_addr, 0x0D000000-0x001E4BF0],
                [main.s_file, "g.c"],
                    [main.s_str, str_g_script],
                    [c.s_script_g, 0x0D000000, 0x0D00043C, "E0"],
                    [main.s_str, "\n\nunused static u64 _0D000440 = 0;\n\n"],
                    [c.s_script_g, 0x0D000448, 0x0D0005A4, "E0"],
                    [main.s_str, "\n\nunused static u64 _0D0005A8 = 0;\n\n"],
                    [c.s_script_g, 0x0D0005B0, 0x0D000600, "E0"],
                [main.s_write],
                [main.s_addr, 0],
            [main.s_pop],
            [main.s_dir, "b4"],
                s_szpbin(0x001E51F0, 0x001E7D90, 0x00005E78, "gfx"),
                [main.s_addr, 0x0D000000-0x001E7D90],
                [main.s_file, "g.c"],
                    [main.s_str, str_g_script],
                    [c.s_script_g, 0x0D000000, 0x0D000140, "E0"],
                    [main.s_str, "\n\nunused static u64 _0D000140 = 0;\n\n"],
                [main.s_write],
                [main.s_addr, 0],
            [main.s_pop],
            s_shapebin(0x001E7EE0, 0x001F1B30, 0x00015070, 0x000006D0, 0x0D, "b5"),
            [main.s_dir, "c0"],
                s_szpbin(0x001F2200, 0x002008D0, 0x00028BF0, "gfx"),
                [main.s_addr, 0x0F000000-0x002008D0],
                [main.s_file, "g.c"],
                    [main.s_str, str_g_script],
                    [c.s_script_g, 0x0F000000, 0x0F000020, "E0"],
                    [main.s_str, "\n\nunused static u64 _0F000020 = 0;\n\n"],
                    [c.s_script_g, 0x0F000028, 0x0F00019C, "E0"],
                    [main.s_str, "\n\nunused static u64 _0F0001A0 = 0;\n\n"],
                    [c.s_script_g, 0x0F0001A8, 0x0F000B34, "E0"],
                [main.s_write],
                [main.s_addr, 0],
            [main.s_pop],
            [main.s_dir, "entity"],
                s_szpbin(0x00201410, 0x00218DA0, 0x00033308, "gfx"),
                [main.s_addr, 0x16000000-0x00218DA0],
                [main.s_file, "g.c"],
                    [main.s_str, str_g_script],
                    [main.s_str, "\n\nextern G_SCRIPT g_entity_144[];\n\n"],
                    [c.s_script_g, 0x16000000, 0x16001060, "E0"],
                [main.s_write],
                [main.s_addr, 0],
            [main.s_pop],
        [main.s_pop],
        [main.s_dir, "object"],
            [main.s_addr, 0x13000000-0x00219E00],
            [main.s_call, data_object],
            [main.s_addr, 0],
        [main.s_pop],
        [main.s_dir, "menu"],
            [main.s_dir, "title"],
                s_script(0x00269EA0, 0x0026A39C, 0x14000000, 0x2D0),
                s_szpbin(0x0026A3A0, 0x0026F420, 0x0000C940, "logo"),
                s_szpbin(0x0026F420, 0x002708C0, 0x000065A8, "selectstage"),
            [main.s_pop],
            [main.s_dir, "select"],
                s_script(0x002A6120, 0x002A65B0, 0x14000000, 0x1C4),
                s_szpbin(0x002A65B0, 0x002ABCA0, 0x0000DE60, "gfx"),
            [main.s_pop],
        [main.s_pop],
        [main.s_dir, "face"],
            [main.s_bin, 0x002739A0, 0x002A6120, "E0", ["data.bin"]],
            [main.s_file, "data.S"],
                [main.s_str, ".data\n.incbin \"data/face/data.bin\"\n"],
            [main.s_write],
        [main.s_pop],
        [main.s_addr, 0x15000000-0x002ABCA0],
        [main.s_file, "game.S"],
            [main.s_str, str_s_script],
            [main.s_call, data_game],
        [main.s_write],
        [main.s_addr, 0],
        [main.s_dir, "background"],
            # s_gfx(0x002708C0, 0x002739A0, "title", data_background_title),
            s_szpbin(0x002708C0, 0x002739A0, 0x000065E8, "title/gfx"),
            s_szpbin(0x002AC6B0, 0x002B8F10, 0x00020140, "a/gfx"), # 20000 + 140
            s_szpbin(0x002B8F10, 0x002C73D0, 0x00020140, "b/gfx"), # 20000 + 140
            s_szpbin(0x002C73D0, 0x002D0040, 0x00014940, "c/gfx"), # 14800 + 140
            s_szpbin(0x002D0040, 0x002D64F0, 0x00018940, "d/gfx"), # 18800 + 140
            s_szpbin(0x002D64F0, 0x002E7880, 0x00020140, "e/gfx"), # 20000 + 140
            s_szpbin(0x002E7880, 0x002F14E0, 0x00020140, "f/gfx"), # 20000 + 140
            s_szpbin(0x002F14E0, 0x002FB1B0, 0x00020140, "g/gfx"), # 20000 + 140
            s_szpbin(0x002FB1B0, 0x00301CD0, 0x00014940, "h/gfx"), # 14800 + 140
            s_szpbin(0x00301CD0, 0x0030CEC0, 0x00020140, "i/gfx"), # 20000 + 140
            s_szpbin(0x0030CEC0, 0x0031E1D0, 0x00020140, "j/gfx"), # 20000 + 140
        [main.s_pop],
        [main.s_dir, "texture"],
            # s_gfx(0x0031E1D0, 0x00326E40, 0x09, "a", [
            #     d_texture_n("rgba16", 32, 32, 24),
            # ]),
            s_szpbin(0x0031E1D0, 0x00326E40, 0x0000C000, "a/gfx"),
            s_szpbin(0x00326E40, 0x0032D070, 0x0000C800, "b/gfx"),
            s_szpbin(0x0032D070, 0x00334B30, 0x0000B800, "c/gfx"),
            s_szpbin(0x00334B30, 0x0033D710, 0x0000C800, "d/gfx"),
            s_szpbin(0x0033D710, 0x00341140, 0x00008800, "e/gfx"),
            s_szpbin(0x00341140, 0x00347A50, 0x0000A000, "f/gfx"),
            s_szpbin(0x00347A50, 0x0034E760, 0x0000C800, "g/gfx"),
            s_szpbin(0x0034E760, 0x00351960, 0x00008C00, "h/gfx"),
            s_szpbin(0x00351960, 0x00357350, 0x0000C800, "i/gfx"),
            s_szpbin(0x00357350, 0x0035ED10, 0x0000C000, "j/gfx"),
            s_szpbin(0x0035ED10, 0x00365980, 0x0000C400, "k/gfx"),
            s_szpbin(0x00365980, 0x0036F530, 0x0000C800, "l/gfx"),
        [main.s_pop],
        [main.s_dir, "particle"],
            s_gfx(0x0036F530, 0x00371C40, 0x0B, "a", data_particle_a),
        [main.s_pop],
        [main.s_dir, "stage"],
            s_stagebin(0x00371C40, 0x003828C0, 0x00383950, 0x00026E44, 0x5A8, "bbh"),
            s_stagebin(0x00383950, 0x00395C90, 0x00396340, 0x000237A6, 0x3DC, "ccm"),
            s_stagebin(0x00396340, 0x003CF0D0, 0x003D0DC0, 0x00079118, 0xEFC, "inside"),
            s_stagebin(0x003D0DC0, 0x003E6A00, 0x003E76B0, 0x0002B968, 0x530, "hmc"),
            s_stagebin(0x003E76B0, 0x003FB990, 0x003FC2AC, 0x000288B0, 0x5B4, "ssl"),
            s_stagebin(0x003FC2B0, 0x00405A60, 0x00405FAC, 0x000117C2, 0x43C, "bob"),
            s_stagebin(0x00405FB0, 0x0040E840, 0x0040ED64, 0x0000FA88, 0x360, "sl"),
            s_stagebin(0x0040ED70, 0x00419F90, 0x0041A75C, 0x00018788, 0x57C, "wdw"),
            s_stagebin(0x0041A760, 0x00423B20, 0x004246C4, 0x000113AC, 0x900, "jrb"),
            s_stagebin(0x004246D0, 0x0042C6E0, 0x0042CF1C, 0x0000E3BC, 0x5A4, "thi"),
            s_stagebin(0x0042CF20, 0x00437400, 0x00437868, 0x00016A20, 0x240, "ttc"),
            s_stagebin(0x00437870, 0x0044A140, 0x0044ABB4, 0x0002EE76, 0x658, "rr"),
            s_stagebin(0x0044ABC0, 0x004545E0, 0x00454E00, 0x00011878, 0x65C, "grounds"),
            s_stagebin(0x00454E00, 0x0045BF60, 0x0045C600, 0x0000FE30, 0x3B4, "bitdw"),
            s_stagebin(0x0045C600, 0x00461220, 0x004614C8, 0x0000ACC8, 0x1F0, "vcutm"),
            s_stagebin(0x004614D0, 0x0046A840, 0x0046B088, 0x00015C08, 0x4A4, "bitfs"),
            s_stagebin(0x0046B090, 0x0046C1A0, 0x0046C3A0, 0x00003330, 0x168, "sa"),
            s_stagebin(0x0046C3A0, 0x00477D00, 0x004784A0, 0x0001B7F4, 0x42C, "bits"),
            s_stagebin(0x004784A0, 0x0048C9B0, 0x0048D930, 0x000288D0, 0x9D8, "lll"),
            s_stagebin(0x0048D930, 0x00495A60, 0x00496090, 0x0000FD10, 0x450, "ddd"),
            s_stagebin(0x00496090, 0x0049DA50, 0x0049E70C, 0x00011E18, 0x7E0, "wf"),
            s_stagebin(0x0049E710, 0x004AC4B0, 0x004AC56C, 0x00027350, 0x050, "end"),
            s_stagebin(0x004AC570, 0x004AF670, 0x004AF930, 0x00006E7C, 0x1FC, "courtyard"),
            s_stagebin(0x004AF930, 0x004B7F10, 0x004B80C8, 0x0001109C, 0x0F8, "pss"),
            s_stagebin(0x004B80D0, 0x004BE9E0, 0x004BEC28, 0x0000BFA8, 0x194, "cotmc"),
            s_stagebin(0x004BEC30, 0x004C2700, 0x004C2920, 0x000089C6, 0x158, "totwc"),
            s_stagebin(0x004C2920, 0x004C41C0, 0x004C4318, 0x00002AC8, 0x0D0, "bitdwa"),
            s_stagebin(0x004C4320, 0x004CD930, 0x004CDBCC, 0x000137AE, 0x1E4, "wmotr"),
            s_stagebin(0x004CDBD0, 0x004CE9F0, 0x004CEC00, 0x00001BA0, 0x16C, "bitfsa"),
            s_stagebin(0x004CEC00, 0x004D14F0, 0x004D1910, 0x000050BC, 0x28C, "bitsa"),
            s_stagebin(0x004D1910, 0x004EB1F0, 0x004EBFFC, 0x00030474, 0x710, "ttm"),
        [main.s_pop],
        [main.s_dir, "file"],
            [main.s_addr, 0-0x004EC000],
            [main.s_file, "motion.S"],
                [main.s_str, header.str_motion],
                [asm.s_motion, 0x0008DC18, "E0", "motion", (
                    stbl_motion, ctbl_motion
                )],
            [main.s_write],
            [main.s_addr, 0-0x00579C20],
            [main.s_file, "demo.S"],
                [main.s_str, header.str_demo],
                [asm.s_demo, 0x00001B00, "E0", "demo", (stbl_demo, {})],
            [main.s_write],
            [main.s_addr, 0],
        [main.s_pop],
        [main.s_dir, "audio"],
            # 0x00017E40, 0x0021D300
            [main.s_bin, 0x0057B720, 0x00593560, "E0", ["ctl.bin"]],
            [main.s_bin, 0x00593560, 0x007B0860, "E0", ["tbl.bin"]],
            [main.s_file, "ctl.S"],
                [main.s_str, header.str_audio_ctl],
            [main.s_write],
            [main.s_file, "tbl.S"],
                [main.s_str, header.str_audio_tbl],
            [main.s_write],
            [asm.s_audio_seqbnk, 0x007B0860, 0x007CC620, "E0", seq_table],
            [main.s_file, "seq.S"],
                [main.s_str, header.str_audio_seq],
            [main.s_write],
            [main.s_file, "bnk.S"],
                [main.s_str, header.str_audio_bnk],
            [main.s_write],
        [main.s_pop],
    [main.s_pop],
]
