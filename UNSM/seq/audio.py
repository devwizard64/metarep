import main

import UNSM.asm

ctlname = [
	"se0",
	"se1",
	"se2",
	"se3",
	"se4",
	"se5",
	"se6",
	"se7",
	"se8",
	"se9",
	"se10",
	"music11",
	"music12",
	"music13",
	"music14",
	"music15",
	"music16",
	"music17",
	"music18",
	"music19",
	"music20",
	"music21",
	"music22",
	"music23",
	"music24",
	"music25",
	"music26",
	"music27",
	"music28",
	"music29",
	"music30",
	"music31",
	"music32",
	"music33",
	"music34",
	"music35",
	"music36",
	"music37",
]

tblname = {
	0x00000140: "se0",
	0x000072E0: "se1",
	0x0000ACB0: "se2",
	0x000114C0: "se3",
	0x0001C770: "se4_5",
	0x00051EA0: "se6",
	0x00063A40: "se7",
	0x00074930: "se8",
	0x000B9DF0: "se9",
	0x000C4940: "se10",
	0x001225A0: "music",
	0x00206870: "music20",
	0x0020A2F0: "music22",
	0x0020BC40: "music29",
}

E0_inst = [
	[UNSM.asm.f_audio_ctltbl, "E0.Audioctl", "E0.Audiotbl", ctlname, tblname],
]

seq_inst = [
	[main.s_file, "audio/E0/inst.ins", E0_inst],
]

seqname = [
	"se",
	"starcatch",
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
	"starselect",
	"special",
	"metal",
	"bowsermsg",
	"bowser",
	"hiscore",
	"merrygoround",
	"fanfare",
	"starappear",
	"battle",
	"arenaclear",
	"endless",
	"final",
	"staff",
	"solution",
	"toadmsg",
	"peachmsg",
	"intro",
	"finalclear",
	"ending",
	"fileselect",
	"lakitumsg",
]

E0_seq = [
	[UNSM.asm.f_audio_seqbnk, "E0.Audioseq", "E0.Audiobnk", seqname],
]

seq_seq = [
	[main.s_file, "audio/E0/bnk.txt", E0_seq],
]
