str_digit   = "0123456789"
str_upper   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_lower   = "abcdefghijklmnopqrstuvwxyz"
str_hira_0  = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん。、"
str_hira_1  = "がぎぐげござじずぜぞだぢづでど" # dakuten
str_hira_2  = "ばびぶべぼ" # dakuten
str_hira_3  = "ぱぴぷぺぽ" # handakuten
str_hira_4  = "ぇっゃゅょぁぃぅぉ" # small
str_kata_0  = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン ー"
str_kata_1  = "ガギグゲゴザジズゼゾダヂヅデド" # dakuten
str_kata_2  = "バビブベボ" # dakuten
str_kata_3  = "パピプペポ" # handakuten
str_kata_4  = "ェッャュョァィゥォ" # small

def str_range(i, s, c=[]):
    return [(s, c + [i+n]) for n, s in enumerate(s)]

global3 = [
    ("[+]", [0xF9]),
    ("[*]", [0xFA]),
    ("[x]", [0xFB]),
]

common3 = global3 + [
    ("<->", [0xE4]),
    ("[-]", [0xFC]),
    ("[.]", [0xFD]),
]

global2 = [
]

common2 = global2 + [
    ("%d",  [0xE0]),
]

global1 = str_range(0x00, str_digit + str_upper) + [
    ("&",   [0xE5]),
    ("!",   [0xF2]),
    ("?",   [0xF4]),
    ("\n",  [0xFE]),
]

common1 = global1 + [
    ("(",   [0xE1]),
    (")",   [0xE3]),
    (":",   [0xE6]),
    ("%",   [0xF3]),
    ("…",   [0xF8]),
]

jp = common3 + common2 + common1 + (
    str_range(0x40 + 5*1, str_hira_1, [0xF0]) +
    str_range(0x40 + 5*5, str_hira_2, [0xF0]) +
    str_range(0x40 + 5*5, str_hira_3, [0xF1]) +
    str_range(0x70 + 5*1, str_kata_1, [0xF0]) +
    str_range(0x70 + 5*5, str_kata_2, [0xF0]) +
    str_range(0x70 + 5*5, str_kata_3, [0xF1]) +
    str_range(0x40, str_hira_0) +
    str_range(0x70, str_kata_0) +
    str_range(0xA0, str_hira_4) +
    str_range(0xD0, str_kata_4)
) + [
    ("『",   [0xF5]),
    ("』",   [0xF6]),
    ("〜",   [0xF7]),
]

jp_p = str_range(0x00, "ファイルセレクトをコピーするけマリオスアみどの?サウンド")

en1 = [
    ("'",   [0x3E]),
    (".",   [0x3F]),
    (",",   [0x6F]),
    (" ",   [0x9E]),
    ("-",   [0x9F]),
    ("\t",  [0xD0]),
]

en = [
    ("[^]", [0x50]),
    ("[v]", [0x51]),
    ("[<]", [0x52]),
    ("[>]", [0x53]),
    ("[A]", [0x54]),
    ("[B]", [0x55]),
    ("[C]", [0x56]),
    ("[Z]", [0x57]),
    ("[R]", [0x58]),
] + common3 + common2 + common1 + en1 + str_range(0x24, str_lower) + [
    ("{",   [0xF5]),
    ("}",   [0xF6]),
    ("~",   [0xF7]),
]

en_m = [
    ("the", [0xD1]),
    ("you", [0xD2]),
    (")(",  [0xE2]),
] + en

en_s = [
    ("[M]", [0x40, 0x41]),
] + global3 + global1 + en1

en_p = [
    ("[x]", [0x32]),
    ("[+]", [0x33]),
    ("[*]", [0x35]),
    ("\n",  [0xFE]),
]

table = {
    "jp":   jp,
    "jp_p": jp_p,
    "en":   en,
    "en_m": en_m,
    "en_s": en_s,
    "en_p": en_p,
}
