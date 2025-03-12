import main

imm_E0_Audioctl = {
	0x00000150: 5,
	0x00000570: 8,
	0x00000AD0: 2,
	0x00000D00: 9,
	0x000014D0: 10,
	0x00001ED0: 10,
	0x00002A30: 10,
	0x00003450: 10,
	0x00003E00: 10,
	0x00004F70: 6,
	0x000054A0: 10,
	0x00006390: 10,
	0x000069B0: 11,
	0x00007CB0: 10,
	0x00008EB0: 6,
	0x00009450: 3,
	0x000098A0: 6,
	0x0000A4B0: 10,
	0x0000B970: 10,
	0x0000C2B0: 10,
	0x0000D290: 4,
	0x0000D430: 8,
	0x0000E3B0: 1,
	0x0000E4B0: 10,
	0x0000F7F0: 10,
	0x00010930: 11,
	0x00011CE0: 10,
	0x000125C0: 11,
	0x000135A0: 6,
	0x000138B0: 5,
	0x00013BE0: 3,
	0x00013F50: 11,
	0x00014280: 8,
	0x000145D0: 3,
	0x000147D0: 10,
	0x000156B0: 7,
	0x00015B30: 1,
	0x000167C0: 15,
}

imm_E0_Audiotbl = {
	0x00000140: (None, "se0_0", "se/0_0.aifc"), # flip
	0x00000830: (None, "se0_1", "se/0_1.aifc"), # (continuous)
	0x00003100: (None, "se0_2", "se/0_2.aifc"), # beat
	0x00003430: (None, "yoshi", "se/yoshi.aifc"),
	0x00004600: (None, "se0_4", "se/0_4.aifc"), # pop out
	0x00005790: (None, "se0_5", "se/0_5.aifc"), # pound

	0x000072E0: (None, "se1_0", "se/1_0.aifc"), # step?
	0x00007340: (None, "se1_1", "se/1_1.aifc"), # grass step
	0x000075F0: (None, "se1_3", "se/1_3.aifc"), # floor step
	0x00007830: (None, "se1_4", "se/1_4.aifc"), # wood step
	0x00007EC0: (None, "se1_5", "se/1_5.aifc"), # sand step
	0x00008540: (None, "se1_6", "se/1_6.aifc"), # snow step
	0x000086A0: (None, "se1_7", "se/1_7.aifc"), # metal step
	0x0000A080: (None, "se1_8", "se/1_8.aifc"), # sand

	0x0000ACB0: (None, "se2_0", "se/2_0.aifc"), # dive
	0x0000E440: (None, "se2_1", "se/2_1.aifc"), # splash
	0x0000F930: (None, "se2_2", "se/2_2.aifc"), # swim

	# various sliding / continuous
	0x000114C0: (None, "se3_0", "se/3_0.aifc"),
	0x00013150: (None, "se3_1", "se/3_1.aifc"),
	0x00014320: (None, "se3_2", "se/3_2.aifc"),
	0x000153E0: (None, "se3_3", "se/3_3.aifc"),
	0x000168B0: (None, "se3_4", "se/3_4.aifc"),
	0x00017360: (None, "se3_5", "se/3_5.aifc"),
	0x00017E70: (None, "se3_6", "se/3_6.aifc"),
	0x000188C0: (None, "se3_7", "se/3_7.aifc"),
	0x00019720: (None, "se3_8", "se/3_8.aifc"),
	0x0001BFA0: (None, "se3_9", "se/3_9.aifc"),

	0x0001C770: (None, "se4_0", "se/4_0.aifc"), # warp
	0x0001DD50: (None, "se4_1", "se/4_1.aifc"), # doorknob
	0x0001ED80: (None, "se4_2__5_4", "se/4_2__5_4.aifc"), # hinge creak
	0x00021A00: (None, "se4_3", "se/4_3.aifc"), # metal creak
	0x000231C0: (None, "se4_4", "se/4_4.aifc"), # (metal) door close
	0x000243C0: (None, "se4_5", "se/4_5.aifc"), # surfacing
	0x00027B60: (None, "se4_6", "se/4_6.aifc"), # short swim
	0x00028310: (None, "se4_8", "se/4_8.aifc"),
	0x0002A680: (None, "se4_9", "se/4_9.aifc"),
	0x0002B100: (None, "se4_10", "se/4_10.aifc"),
	0x0002B810: (None, "se4_11", "se/4_11.aifc"),
	0x0002BDE0: (None, "se4_13", "se/4_13.aifc"), # eject from painting
	0x0002E9F0: (None, "se4_14", "se/4_14.aifc"), # star noise
	0x00034300: (None, "se4_15", "se/4_15.aifc"), # blast
	0x0003C150: (None, "se5_0", "se/5_0.aifc"),
	0x0003D1C0: (None, "se5_1", "se/5_1.aifc"),
	0x0003F670: (None, "se5_2", "se/5_2.aifc"), # elevator
	0x0003FAB0: (None, "se5_3", "se/5_3.aifc"),
	0x000431A0: (None, "se5_5", "se/5_5.aifc"),
	0x00043E30: (None, "se5_6", "se/5_6.aifc"), # wind
	0x00047700: (None, "se5_7", "se/5_7.aifc"), # box break
	0x0004A010: (None, "se5_8", "se/5_8.aifc"), # bird
	0x0004A7E0: (None, "se5_9", "se/5_9.aifc"), # bird
	0x0004B190: (None, "se5_10", "se/5_10.aifc"), # bird
	0x0004C0F0: (None, "se5_11", "se/5_11.aifc"),
	0x0004C910: (None, "se5_12", "se/5_12.aifc"), # bird
	0x0004CC40: (None, "se5_13", "se/5_13.aifc"),
	0x0004F470: (None, "se5_14", "se/5_14.aifc"), # spring
	0x00050E20: (None, "se5_15", "se/5_15.aifc"), # shine

	0x00051EA0: (None, "se6_0", "se/6_0.aifc"), # MIPS
	0x00052730: (None, "se6_1", "se/6_1.aifc"),
	0x000533F0: (None, "se6_2", "se/6_2.aifc"), # bowser growl
	0x00055700: (None, "se6_4", "se/6_4.aifc"), # bowser shriek
	0x000594B0: (None, "se6_5", "se/6_5.aifc"), # bowser swing
	0x00059FA0: (None, "se6_6", "se/6_6.aifc"), # bowser inhale
	0x0005B960: (None, "se6_7", "se/6_7.aifc"), # penguin step
	0x0005C020: (None, "se6_8", "se/6_8.aifc"),
	0x0005C550: (None, "se6_9", "se/6_9.aifc"), # laugh
	0x0005E1E0: (None, "se6_10", "se/6_10.aifc"), # cannon 1
	0x0005EB00: (None, "se6_11", "se/6_11.aifc"), # cannon 2
	0x0005F480: (None, "se6_12", "se/6_12.aifc"), # cannon 3
	0x0005FD10: (None, "se6_14", "se/6_14.aifc"), # piranha flower death
	0x000611C0: (None, "se6_15", "se/6_15.aifc"), # moving stone

	0x00063A40: (None, "se7_0", "se/7_0.aifc"), # ghost death
	0x00063F00: (None, "se7_1", "se/7_1.aifc"),
	0x00064D50: (None, "se7_2", "se/7_2.aifc"),
	0x00065210: (None, "se7_3", "se/7_3.aifc"), # blast
	0x00067B70: (None, "se7_5", "se/7_5.aifc"), # bowser breath
	0x0006A5B0: (None, "se7_6", "se/7_6.aifc"), # cannon turn
	0x0006B5C0: (None, "se7_7", "se/7_7.aifc"), # monkey
	0x0006C890: (None, "se7_8", "se/7_8.aifc"),
	0x0006DC70: (None, "se7_9", "se/7_9.aifc"), # klepto?
	0x0006E1E0: (None, "se7_10", "se/7_10.aifc"), # penguin cry
	0x0006F130: (None, "se7_11", "se/7_11.aifc"),
	0x00070980: (None, "se7_12", "se/7_12.aifc"), # thwomp
	0x00071F20: (None, "se7_13", "se/7_13.aifc"), # piano
	0x00074210: (None, "se7_14", "se/7_14.aifc"), # chain chomp

	0x00074930: (None, "se8_0", "se/8_0.aifc"), # Ho
	0x00075090: (None, "se8_1", "se/8_1.aifc"), # Wa
	0x000758A0: (None, "se8_2", "se/8_2.aifc"), # Ya
	0x00076330: (None, "se8_3", "se/8_3.aifc"), # Haha
	0x00077E30: (None, "se8_4", "se/8_4.aifc"), # Yahoo
	0x00079F80: (None, "se8_5", "se/8_5.aifc"), # falling grunt
	0x0007AA80: (None, "se8_6", "se/8_6.aifc"), # grab object
	0x0007BC00: (None, "se8_7", "se/8_7.aifc"), # Wa
	0x0007C690: (None, "se8_8", "se/8_8.aifc"), # Woa
	0x0007E720: (None, "se8_9", "se/8_9.aifc"), # lifting grunt
	0x00080050: (None, "se8_10", "se/8_10.aifc"), # damage
	0x00081660: (None, "se8_11", "se/8_11.aifc"), # Oof
	0x00082C10: (None, "se8_12", "se/8_12.aifc"), # Here we go
	0x00085E20: (None, "se8_13", "se/8_13.aifc"), # yawn
	0x00089720: (None, "se8_14", "se/8_14.aifc"), # snore 1
	0x0008B800: (None, "se8_15", "se/8_15.aifc"), # snore 2
	0x0008C3C0: (None, "se8_16", "se/8_16.aifc"), # Doh
	0x0008D7E0: (None, "se8_17", "se/8_17.aifc"), # Game over
	0x0008F110: (None, "se8_18", "se/8_18.aifc"), # Hello
	0x00090C30: (None, "se8_19", "se/8_19.aifc"), # Press START to play
	0x00094200: (None, "se8_20", "se/8_20.aifc"), # Boing
	0x00095340: (None, "se8_21", "se/8_21.aifc"), # dream
	0x000AD300: (None, "se8_22", "se/8_22.aifc"), # So long Bowser
	0x000B07B0: (None, "se8_23", "se/8_23.aifc"), # I'm tired
	0x000B3440: (None, "se8_24", "se/8_24.aifc"), # Waha
	0x000B5A20: (None, "se8_25", "se/8_25.aifc"), # Yippee
	0x000B7D60: (None, "se8_26", "se/8_26.aifc"), # Let's go

	0x000B9DF0: (32000, "se9_0_2", "se/9_0_2.aifc"), # piano
	0x000BB570: (16000, "se9_0h", "se/9_0h.aifc"), # piano
	0x000BC130: (32000, "se9_1", "se/9_1.aifc"), # piano + string (pause)
	0x000BEC60: (32000, "se9_3", "se/9_3.aifc"), # bell (coin)
	0x000C0D70: (None, "se9_4", "se/9_4.aifc"), # camera buzz
	0x000C1BF0: (None, "se9_5", "se/9_5.aifc"), # camera click
	0x000C2280: (None, "se9_6", "se/9_6.aifc"), # face stretch

	0x000C4940: (None, "se10_0", "se/10_0.aifc"), # falling
	0x000CAA00: (None, "se10_1", "se/10_1.aifc"), # Hoohoo
	0x000CBFE0: (None, "se10_2", "se/10_2.aifc"), # low power
	0x000CD460: (None, "se10_4", "se/10_4.aifc"), # standing death
	0x000D1210: (None, "se10_5", "se/10_5.aifc"), # burning
	0x000D58F0: (None, "se10_6", "se/10_6.aifc"), # push off grunt
	0x000D61E0: (None, "se10_7", "se/10_7.aifc"), # cough
	0x000D6BE0: (None, "se10_8", "se/10_8.aifc"), # It's me, Mario
	0x000DAE60: (None, "se10_9", "se/10_9.aifc"), # Ya
	0x000DB700: (None, "se10_10", "se/10_10.aifc"), # Hoo
	0x000DCD60: (None, "se10_11", "se/10_11.aifc"), # Mama-mia
	0x000DEDA0: (None, "se10_12", "se/10_12.aifc"), # Okey-dokey
	0x000E0DD0: (None, "se10_13", "se/10_13.aifc"), # drowning
	0x000E3D00: (None, "se10_14", "se/10_14.aifc"), # Thank you so much for playing my game
	0x000E9170: (None, "se10_15", "se/10_15.aifc"), # Dear Mario: ...
	0x000FE6A0: (None, "se10_16", "se/10_16.aifc"), # Mario!
	0x00100350: (None, "se10_17", "se/10_17.aifc"), # The power of the Stars is restored to the castle...
	0x001078C0: (None, "se10_18", "se/10_18.aifc"), # ...and it's all thanks to you!
	0x0010B550: (None, "se10_19", "se/10_19.aifc"), # Thank you, Mario!
	0x0010ECD0: (None, "se10_20", "se/10_20.aifc"), # We have to do something special for you...
	0x00114B20: (None, "se10_21", "se/10_21.aifc"), # Listen, everybody, let's bake a delicious cake...
	0x0011E5B0: (None, "se10_22", "se/10_22.aifc"), # ...for Mario...
	0x001209E0: (None, "se10_23", "se/10_23.aifc"), # Mario!

	0x001225A0: (32000, "banjoL", "inst/banjoL.aifc"),
	0x001253E0: (32000, "banjo", "inst/banjo.aifc"),
	0x00127C80: (32000, "violin", "inst/violin.aifc"),
	0x0012C050: (32000, "whistle", "inst/whistle.aifc"),
	0x00130340: (32000, "honky_tonk", "inst/honky_tonk.aifc"),
	0x00132150: (24000, "acoustic_bass", "inst/acoustic_bass.aifc"),
	0x001358E0: (16000, "kick", "inst/kick.aifc"),
	0x001360A0: (32000, "rim", "inst/rim.aifc"),
	0x00136C30: (24000, "snare", "inst/snare.aifc"),
	0x001380B0: (32000, "tom", "inst/tom.aifc"),
	0x00139B70: (32000, "tambourine", "inst/tambourine.aifc"),
	0x0013C150: (22050, "bongo_1", "inst/bongo_1.aifc"),
	0x0013DD70: (32000, "bongo_2", "inst/bongo_2.aifc"),
	0x0013EF10: (32000, "claves", "inst/claves.aifc"),
	0x00140110: (32000, "closed_hi_hat", "inst/closed_hi_hat.aifc"),
	0x00140960: (32000, "open_hi_hat", "inst/open_hi_hat.aifc"),
	0x00143900: (32000, "ride_cymbal", "inst/ride_cymbal.aifc"),
	0x00146A80: (32000, "crash_cymbal", "inst/crash_cymbal.aifc"),
	0x0014B190: (32000, "snare_2L", "inst/snare_2L.aifc"),
	0x0014CD60: (32000, "snare_2", "inst/snare_2.aifc"),
	0x0014F3D0: (32000, "strings_1L", "inst/strings_1L.aifc"),
	0x00154320: (32000, "strings_1", "inst/strings_1.aifc"),
	0x00158E70: (32000, "french_horn", "inst/french_horn.aifc"),
	0x0015C7C0: (32000, "trumpet", "inst/trumpet.aifc"),
	0x0015FFA0: (32000, "timpani", "inst/timpani.aifc"),
	0x00164D40: (32000, "brass_section", "inst/brass_section.aifc"),
	0x00169410: (32000, "slap_bass", "inst/slap_bass.aifc"),
	0x0016B770: (32000, "synth_voice", "inst/synth_voice.aifc"),
	0x0016F500: (32000, "muted_guitar_fourth", "inst/muted_guitar_fourth.aifc"),
	0x00170ED0: (32000, "melodic_tom", "inst/melodic_tom.aifc"),
	0x00176B00: (22050, "triangleL", "inst/triangleL.aifc"),
	0x00176F00: (22050, "triangle", "inst/triangle.aifc"),
	0x00178780: (32000, "cabasa", "inst/cabasa.aifc"),
	0x00179810: (12000, "bass_lead", "inst/bass_lead.aifc"),
	0x0017B500: (24000, "choir_ooh", "inst/choir_ooh.aifc"),
	0x0017EC10: (32000, "strings_2L", "inst/strings_2L.aifc"),
	0x00182A20: (32000, "strings_2", "inst/strings_2.aifc"),
	0x00187110: (32000, "strings_2H", "inst/strings_2H.aifc"),
	0x0018B570: (32000, "electric_piano", "inst/electric_piano.aifc"),
	0x00192660: (32000, "harpsichord", "inst/harpsichord.aifc"),
	0x00198CB0: (24000, "sitar_1", "inst/sitar_1.aifc"),
	0x0019CAB0: (32000, "orchestra_hit", "inst/orchestra_hit.aifc"),
	0x0019FC30: (24000, "percussion_loopL", "inst/percussion_loopL.aifc"),
	0x001A3310: (24000, "percussion_loop", "inst/percussion_loop.aifc"),
	0x001A5100: (24000, "percussion_loopH", "inst/percussion_loopH.aifc"),
	0x001A9740: (32000, "trombone", "inst/trombone.aifc"),
	0x001AD350: (16000, "accordion", "inst/accordion.aifc"),
	0x001B1A90: (32000, "snow_bells", "inst/snow_bells.aifc"),
	0x001B6C00: (32000, "charang", "inst/charang.aifc"),
	0x001BB230: (32000, "overdriven_guitar", "inst/overdriven_guitar.aifc"),
	0x001BEE70: (32000, "power_snare", "inst/power_snare.aifc"),
	0x001C3000: (24000, "power_kick", "inst/power_kick.aifc"),
	0x001C41D0: (32000, "flute", "inst/flute.aifc"),
	0x001C6670: (24000, "percussive_organ", "inst/percussive_organ.aifc"),
	0x001C9080: (32000, "synth_bass", "inst/synth_bass.aifc"),
	0x001CB110: (16000, "square_lead", "inst/square_lead.aifc"),
	0x001CCE30: (22050, "synth_kick", "inst/synth_kick.aifc"),
	0x001CD7F0: (24000, "sitar_2", "inst/sitar_2.aifc"),
	0x001D2A60: (16000, "music_box", "inst/music_box.aifc"),
	0x001D64E0: (32000, "acoustic_guitarL", "inst/acoustic_guitarL.aifc"),
	0x001DBF50: (32000, "acoustic_guitar", "inst/acoustic_guitar.aifc"),
	0x001E0A80: (11025, "acoustic_guitarH", "inst/acoustic_guitarH.aifc"),
	0x001E3B10: (32000, "ghost", "inst/ghost.aifc"),
	0x001E67F0: (27777, "ghost_bell_1", "inst/ghost_bell_1.aifc"),
	0x001EB590: (16000, "ghost_bell_2", "inst/ghost_bell_2.aifc"),
	0x001EF1F0: (32000, "pan_flute", "inst/pan_flute.aifc"),
	0x001F3830: (22050, "celesta", "inst/celesta.aifc"),
	0x001F43E0: (16000, "harmonica", "inst/harmonica.aifc"),
	0x001F7590: (32000, "piano", "inst/piano.aifc"),
	0x001FB120: (16000, "french_hornH", "inst/french_hornH.aifc"),
	0x001FCDF0: (32000, "pizzicato_strings", "inst/pizzicato_strings.aifc"),
	0x001FFA70: (16000, "pizzicato_stringsH", "inst/pizzicato_stringsH.aifc"),
	0x00202EA0: (32000, "steel_drum", "inst/steel_drum.aifc"),
	0x00206870: (16000, "music_box", "inst/music_box.aifc"),
	0x0020A2F0: (32000, "voice_pah", "inst/voice_pah.aifc"),
	0x0020BC40: (32000, "church_organ", "inst/church_organ.aifc"),
	0x00215A40: (16000, "church_organH", "inst/church_organH.aifc"),
	0x00219BE0: (24000, "choir_ooh", "inst/choir_ooh.aifc"),
}

imm_E0_Audioseq = {
	0x00000120: 0x348C, # se
	0x000035B0: 0x026B, # starcatch
	0x00003820: 0x203E, # title
	0x00005860: 0x1402, # field
	0x00006C70: 0x09BE, # castle
	0x00007630: 0x12AC, # water
	0x000088E0: 0x0993, # fire
	0x00009280: 0x0D5A, # arena
	0x00009FE0: 0x1FCF, # snow
	0x0000BFB0: 0x1D08, # slider
	0x0000DCC0: 0x162A, # ghost
	0x0000F2F0: 0x0573, # lullaby
	0x0000F870: 0x1317, # dungeon
	0x00010B90: 0x0086, # starselect
	0x00010C20: 0x0C39, # wing
	0x00011860: 0x0AD2, # metal
	0x00012340: 0x0228, # bowsermsg
	0x00012570: 0x1285, # bowser
	0x00013800: 0x010F, # hiscore
	0x00013910: 0x0679, # merrygoround
	0x00013F90: 0x00C5, # fanfare
	0x00014060: 0x0284, # starappear
	0x000142F0: 0x0D6B, # battle
	0x00015060: 0x029F, # arena_clear
	0x00015300: 0x06F1, # endless
	0x00015A00: 0x0DBB, # final
	0x000167C0: 0x37E9, # staff
	0x00019FB0: 0x00D8, # solution
	0x0001A090: 0x00D0, # toadmsg
	0x0001A160: 0x01B0, # peachmsg
	0x0001A310: 0x06E4, # intro
	0x0001AA00: 0x080A, # finalclear
	0x0001B210: 0x075A, # ending
	0x0001B970: 0x030D, # fileselect
	0x0001BC80: 0x0139, # lakitumsg
}
