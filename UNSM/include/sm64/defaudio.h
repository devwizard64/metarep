#ifndef __SM64_DEFAUDIO_H__
#define __SM64_DEFAUDIO_H__

#define NA_MODE_DEFAULT         0
#define NA_MODE_CASTLE          1
#define NA_MODE_ARENA           2
#define NA_MODE_WATER           3
#define NA_MODE_DUNGEON         4
#define NA_MODE_FIELD           5
#define NA_MODE_GHOST           6
#define NA_MODE_STAFF           7

#define NA_SEQ_SE               0
#define NA_SEQ_STARCATCH        1
#define NA_SEQ_TITLE            2
#define NA_SEQ_FIELD            3
#define NA_SEQ_CASTLE           4
#define NA_SEQ_WATER            5
#define NA_SEQ_FIRE             6
#define NA_SEQ_ARENA            7
#define NA_SEQ_SNOW             8
#define NA_SEQ_SLIDER           9
#define NA_SEQ_GHOST            10
#define NA_SEQ_LULLABY          11
#define NA_SEQ_DUNGEON          12
#define NA_SEQ_STARSELECT       13
#define NA_SEQ_SPECIAL          14
#define NA_SEQ_METAL            15
#define NA_SEQ_BOWSERMSG        16
#define NA_SEQ_BOWSER           17
#define NA_SEQ_HISCORE          18
#define NA_SEQ_MERRYGOROUND     19
#define NA_SEQ_FANFARE          20
#define NA_SEQ_STARAPPEAR       21
#define NA_SEQ_BATTLE           22
#define NA_SEQ_ARENACLEAR       23
#define NA_SEQ_ENDLESS          24
#define NA_SEQ_FINAL            25
#define NA_SEQ_STAFF            26
#define NA_SEQ_SOLUTION         27
#define NA_SEQ_TOADMSG          28
#define NA_SEQ_PEACHMSG         29
#define NA_SEQ_INTRO            30
#define NA_SEQ_FINALCLEAR       31
#define NA_SEQ_ENDING           32
#define NA_SEQ_FILESELECT       33
#define NA_SEQ_LAKITUMSG        34

#define NA_BGM_NULL             0
#define NA_BGM_STARCATCH        (NA_SEQ_STARCATCH | 0xF00)
#define NA_BGM_TITLE            NA_SEQ_TITLE
#define NA_BGM_GAMEOVER         (NA_SEQ_TITLE | 0x80)
#define NA_BGM_FIELD            NA_SEQ_FIELD
#define NA_BGM_CASTLE           NA_SEQ_CASTLE
#define NA_BGM_WATER            NA_SEQ_WATER
#define NA_BGM_AQUARIUM         (NA_SEQ_WATER | 0x80)
#define NA_BGM_FIRE             NA_SEQ_FIRE
#define NA_BGM_ARENA            NA_SEQ_ARENA
#define NA_BGM_SNOW             NA_SEQ_SNOW
#define NA_BGM_SLIDER           NA_SEQ_SLIDER
#define NA_BGM_RACE             (NA_SEQ_SLIDER | 0x400)
#define NA_BGM_GHOST            NA_SEQ_GHOST
#define NA_BGM_LULLABY          NA_SEQ_LULLABY
#define NA_BGM_DUNGEON          NA_SEQ_DUNGEON
#define NA_BGM_STARSELECT       NA_SEQ_STARSELECT
#define NA_BGM_SPECIAL          (NA_SEQ_SPECIAL | 0x400)
#define NA_BGM_SHELL            (NA_SEQ_SPECIAL | 0x80 | 0x400)
#define NA_BGM_METAL            (NA_SEQ_METAL | 0x400)
/* #define NA_BGM_BOWSERMSG        NA_SEQ_BOWSERMSG */
#define NA_BGM_BOWSER           NA_SEQ_BOWSER
/* #define NA_BGM_HISCORE          NA_SEQ_HISCORE */
#define NA_BGM_MERRYGOROUND     NA_SEQ_MERRYGOROUND
/* #define NA_BGM_FANFARE          NA_SEQ_FANFARE */
/* #define NA_BGM_STARAPPEAR       NA_SEQ_STARAPPEAR */
#define NA_BGM_BATTLE           (NA_SEQ_BATTLE | 0x400)
#define NA_BGM_ARENACLEAR       (NA_SEQ_ARENACLEAR | 0xF00)
#define NA_BGM_ENDLESS          NA_SEQ_ENDLESS
#define NA_BGM_FINAL            NA_SEQ_FINAL
#define NA_BGM_STAFF            (NA_SEQ_STAFF | 0xF00)
/* #define NA_BGM_SOLUTION         NA_SEQ_SOLUTION */
/* #define NA_BGM_TOADMSG          NA_SEQ_TOADMSG */
/* #define NA_BGM_PEACHMSG         NA_SEQ_PEACHMSG */
/* #define NA_BGM_INTRO            NA_SEQ_INTRO */
#define NA_BGM_FINALCLEAR       (NA_SEQ_FINALCLEAR | 0xF00)
#define NA_BGM_ENDING           NA_SEQ_ENDING
#define NA_BGM_FILESELECT       NA_SEQ_FILESELECT
/* #define NA_BGM_LAKITUMSG       NA_SEQ_LAKITUMSG */

#define NA_SE_NULL              0x00000000

#define NA_SE0_00               0x04008081
#define NA_SE0_08               0x04088081
#define NA_SE0_10               0x06108081
#define NA_SE0_18               0x04188081
#define NA_SE0_20               0x06208081
#define NA_SE0_28               0x04289081
#define NA_SE0_29               0x04299081
#define NA_SE0_2A               0x042A9081
#define NA_SE0_2B               0x042B9081
#define NA_SE0_2C               0x062C0081
#define NA_SE0_2D               0x042DA081
#define NA_SE0_2E               0x042E0081
#define NA_SE0_2F               0x042F9081
#define NA_SE0_30               0x0430C081
#define NA_SE0_31               0x04316081
#define NA_SE0_32               0x04328081
#define NA_SE0_33               0x04338081
#define NA_SE0_34               0x04348081
#define NA_SE0_35               0x04358081
#define NA_SE0_36               0x04368081
#define NA_SE0_37               0x04378081
#define NA_SE0_38               0x04388081
#define NA_SE0_3A               0x043A8081
#define NA_SE0_3D               0x043D8081
#define NA_SE0_3E               0x043E8081
#define NA_SE0_3F               0x043F8081
#define NA_SE0_40               0x04408081
#define NA_SE0_41               0x04418081
#define NA_SE0_42               0x04428081
#define NA_SE0_43               0x04438081
#define NA_SE0_44_A0            0x0444A081
#define NA_SE0_44_B0            0x0444B081
#define NA_SE0_44_C0            0x0444C081
#define NA_SE0_45               0x0445A081
#define NA_SE0_46               0x0446A081
#define NA_SE0_47               0x0447A081
#define NA_SE0_48               0x04488081
#define NA_SE0_50               0x04509081
#define NA_SE0_51               0x04519081
#define NA_SE0_52               0x04529081
#define NA_SE0_56               0x04568081
#define NA_SE0_57               0x0457C081
#define NA_SE0_58               0x0458A081
#define NA_SE0_59               0x0459B081
#define NA_SE0_5A               0x045A8081
#define NA_SE0_5B               0x045BFF81
#define NA_SE0_5C               0x045C8081
#define NA_SE0_5E               0x045E8081
#define NA_SE0_5F               0x045F8081
#define NA_SE0_60               0x04608081

#define NA_SE1_00               0x14000001
#define NA_SE1_10               0x14100001
#define NA_SE1_11               0x14110001
#define NA_SE1_12               0x14128001
#define NA_SE1_14               0x14140001
#define NA_SE1_16               0x14160001
#define NA_SE1_17               0x14170001
#define NA_SE1_18               0x1C180001
#define NA_SE1_19               0x1D192001
#define NA_SE1_20               0x14200001
#define NA_SE1_28               0x14280001

#define NA_SE2_00               0x24008081
#define NA_SE2_03               0x24038081
#define NA_SE2_04               0x24048081
#define NA_SE2_05               0x24058081
#define NA_SE2_06               0x24068081
#define NA_SE2_07               0x24078081
#define NA_SE2_08               0x2408C081
#define NA_SE2_09               0x24098081
#define NA_SE2_0A               0x240AFF81
#define NA_SE2_0B_80            0x240B8081
#if NA_REVISION >= 101
#define NA_SE2_0B_D0            0x240BD081
#else
#define NA_SE2_0B_D0            0x240B8081
#endif
#define NA_SE2_0C               0x240C8081
#define NA_SE2_0D               0x240D8081
#define NA_SE2_0E               0x240E8081
#define NA_SE2_0F               0x240F8081
#define NA_SE2_10               0x2410C081
#define NA_SE2_11_80            0x24118081
#define NA_SE2_11_F0            0x2411F081
#define NA_SE2_13_80            0x24138081
#define NA_SE2_13_D0            0x2413D081
#define NA_SE2_14               0x2414A081
#define NA_SE2_15               0x2415FF81
#define NA_SE2_16               0x24168081
#define NA_SE2_18               0x24188081
#define NA_SE2_1B               0x241B8081
#define NA_SE2_1C               0x241C8081
#define NA_SE2_1D               0x241D8081
#define NA_SE2_1E               0x241E8081
#define NA_SE2_1F               0x241F8081
#define NA_SE2_20               0x24208081
#define NA_SE2_22               0x24228081
#define NA_SE2_23               0x2423F081
#define NA_SE2_24               0x24248081
#define NA_SE2_28               0x2428FF81
#define NA_SE2_2B               0x242B8081
#define NA_SE2_30               0x24308081
#define NA_SE2_31               0x2431FF81
#define NA_SE2_32               0x2432FF81
#define NA_SE2_33               0x2433FFA1
#define NA_SE2_34               0x24348081
#define NA_SE2_35               0x2435FF81
#define NA_SE2_36               0x24368081
#define NA_SE2_37               0x24378081
#define NA_SE2_38               0x2438FF81
#define NA_SE2_39               0x2439FF81
#define NA_SE2_3A               0x243AFF81
#define NA_SE2_3B               0x243BFF81
#define NA_SE2_3C               0x243CFF81
#define NA_SE2_3D               0x243DFF81
#define NA_SE2_3E               0x243EFF81
#define NA_SE2_3F               0x243FFF81

#define NA_SE3_00               0x30008081
#define NA_SE3_03               0x30038081
#define NA_SE3_04               0x3004C081
#define NA_SE3_05               0x3005C081
#define NA_SE3_06               0x3006C081
#define NA_SE3_07               0x3007C081
#define NA_SE3_09               0x30090081
#define NA_SE3_0A               0x300A0081
#define NA_SE3_0B               0x300B0081
#define NA_SE3_0C               0x300C8081
#define NA_SE3_0D               0x300D0081
#define NA_SE3_0E               0x300E8081
#define NA_SE3_0F               0x300F0081
#define NA_SE3_11               0x38118081
#define NA_SE3_12               0x38128081
#define NA_SE3_16               0x30160091
#define NA_SE3_17               0x30170081
#define NA_SE3_20               0x31208081
#define NA_SE3_22               0x31228081
#define NA_SE3_24               0x32240081
#define NA_SE3_25               0x32250081
#define NA_SE3_26               0x30264081
#define NA_SE3_27               0x30274081
#if NA_REVISION >= 101
#define NA_SE3_28               0x39280081
#else
#define NA_SE3_28               0x38280081
#endif
#define NA_SE3_2B               0x302B0081
#define NA_SE3_2D               0x302D8081
#define NA_SE3_2E               0x302E2081
#define NA_SE3_2F               0x312F0081
#if NA_REVISION >= 201
#define NA_SE3_30               0x38302081
#elif NA_REVISION >= 101
#define NA_SE3_30               0x38300081
#else
#define NA_SE3_30               0x30300081
#endif
#define NA_SE3_34               0x30344081
#define NA_SE3_35               0x30354081
#define NA_SE3_36               0x30364081
#if NA_REVISION >= 101
#define NA_SE3_37               0x38378081
#else
#define NA_SE3_37               0x30370081
#endif
#define NA_SE3_38               0x30380081
#define NA_SE3_39               0x30390081
#define NA_SE3_3A               0x303A0081
#define NA_SE3_3B               0x303B0081
#define NA_SE3_3C               0x303C0081
#define NA_SE3_3D_00            0x303D0081
#define NA_SE3_3D_80            0x303D8081
#define NA_SE3_3E               0x303E0081
#define NA_SE3_3F               0x303FA081
#define NA_SE3_40_00            0x30400081
#define NA_SE3_40_40            0x30404081
#define NA_SE3_41               0x3041C081
#define NA_SE3_42               0x30420081
#define NA_SE3_43               0x30430081
#define NA_SE3_44               0x30440081
#define NA_SE3_45               0x30450081
#if NA_REVISION >= 101
#define NA_SE3_46               0x30468081
#else
#define NA_SE3_46               0x30460081
#endif
#define NA_SE3_47               0x30478081
#define NA_SE3_48               0x30480081
#define NA_SE3_4D               0x314D4081
#define NA_SE3_4E               0x304EC081
#define NA_SE3_4F               0x304FC081
#define NA_SE3_56               0x30560081
#define NA_SE3_57               0x3057FF91
#define NA_SE3_58               0x3058FF81
#define NA_SE3_5A_00            0x315A0081
#define NA_SE3_5A_40            0x315A4081
#define NA_SE3_5B               0x315B0081
#define NA_SE3_5C               0x315C0081
#define NA_SE3_5D               0x305D0081
#define NA_SE3_5E               0x305E0081
#define NA_SE3_5F               0x305F0081
#define NA_SE3_62               0x31628081
#define NA_SE3_64               0x3064C081
#define NA_SE3_65               0x3065C081
#define NA_SE3_66               0x30668081
#define NA_SE3_67               0x3067A081
#define NA_SE3_69               0x30690081
#define NA_SE3_6B               0x306B8081
#define NA_SE3_6C               0x306C4081
#define NA_SE3_6D_20            0x306D2081
#define NA_SE3_6D_40            0x306D4081
#define NA_SE3_6E               0x306E2081
#define NA_SE3_6F               0x306F3081
#define NA_SE3_70               0x30703081
#define NA_SE3_71               0x30713081
#define NA_SE3_73               0x30730081
#define NA_SE3_74               0x30740081
#define NA_SE3_75               0x30750081
#define NA_SE3_76               0x30762081

#define NA_SE4_00               0x40000001
#define NA_SE4_01               0x40010001
#define NA_SE4_02               0x40020001
#define NA_SE4_03               0x41030001
#define NA_SE4_04               0x40040001
#define NA_SE4_05               0x40050001
#define NA_SE4_08               0x40080001
#define NA_SE4_09               0x40090001
#define NA_SE4_0A               0x400A0001
#define NA_SE4_0B               0x400B0001
#define NA_SE4_0C               0x400C0001
#define NA_SE4_0D_00            0x400D0001
#define NA_SE4_0D_10            0x400D1001
#define NA_SE4_0D_1             0x410D0001
#define NA_SE4_0E               0x400E0001
#define NA_SE4_0F               0x400F4001
#define NA_SE4_10               0x40108001
#define NA_SE4_13               0x40130001
#define NA_SE4_14               0x40140011
#define NA_SE4_15               0x41150001
#define NA_SE4_16               0x41160001
#define NA_SE4_17               0x40178001
#define NA_SE4_18               0x40188001

#define NA_SE5_00               0x50008081
#define NA_SE5_01               0x50010081
#define NA_SE5_02               0x50020081
#define NA_SE5_03               0x50030081
#define NA_SE5_05               0x50050081
#define NA_SE5_06               0x50060081
#define NA_SE5_07               0x50070081
#define NA_SE5_08               0x50080081
#define NA_SE5_09               0x50098081
#define NA_SE5_0A               0x500A0081
#define NA_SE5_0B               0x500B0081
#define NA_SE5_0C               0x500CA081
#define NA_SE5_0D               0x500DF081
#define NA_SE5_0E               0x500EF081
#define NA_SE5_0F               0x500FF081
#define NA_SE5_13               0x50130081
#define NA_SE5_14               0x50140081
#define NA_SE5_15_50            0x50155081
#define NA_SE5_15_80            0x50158081
#define NA_SE5_16_60            0x50166081
#define NA_SE5_16_80            0x50168081
#define NA_SE5_17               0x50178081
#define NA_SE5_18               0x5118A081
#define NA_SE5_1A               0x501A5081
#define NA_SE5_1B               0x501B3081
#define NA_SE5_1D               0x501D8081
#define NA_SE5_1E               0x501EA081
#define NA_SE5_1F               0x501F4081
#define NA_SE5_21               0x50210081
#define NA_SE5_22_00            0x50220081
#define NA_SE5_22_20            0x50222081
#define NA_SE5_24               0x50244081
#define NA_SE5_25               0x50254081
#define NA_SE5_27               0x50270081
#define NA_SE5_28               0x50288081
#define NA_SE5_29               0x5029A081
#define NA_SE5_2A               0x502A0081
#define NA_SE5_2B               0x502B0081
#define NA_SE5_2C               0x502C8081
#define NA_SE5_2D               0x502D0081
#define NA_SE5_2E               0x502E8081
#define NA_SE5_2F_00            0x502F0081
#define NA_SE5_2F_60            0x502F6081
#define NA_SE5_30               0x50308081
#define NA_SE5_31               0x50310081
#define NA_SE5_32               0x50324081
#define NA_SE5_33               0x50334081
#define NA_SE5_36               0x50366081
#define NA_SE5_37               0x50376081
#define NA_SE5_38               0x50388081
#define NA_SE5_39               0x50390081
#define NA_SE5_3A               0x503A0081
#define NA_SE5_3B               0x503B0081
#define NA_SE5_3C               0x503C0081
#define NA_SE5_3D               0x503DA081
#define NA_SE5_3E               0x503EA081
#define NA_SE5_3F               0x503F4081
#define NA_SE5_40               0x50406081
#define NA_SE5_41               0x50410081
#define NA_SE5_46               0x50468081
#define NA_SE5_47               0x5147C081
#define NA_SE5_48               0x50480081
#define NA_SE5_4A               0x524A0081
#define NA_SE5_4C               0x504C0081
#define NA_SE5_4D               0x504D0081
#define NA_SE5_4F               0x504F0081
#define NA_SE5_51               0x50514001
#define NA_SE5_54               0x50542081
#define NA_SE5_55               0x50558081
#define NA_SE5_58               0x50584081
#define NA_SE5_59               0x50591081
#define NA_SE5_5D               0x505D4081
#define NA_SE5_5F               0x505F8091
#define NA_SE5_60               0x5060B081
#define NA_SE5_61               0x5061B081
#define NA_SE5_64               0x5064C081
#define NA_SE5_65               0x5065D081
#define NA_SE5_68               0x50684081
#define NA_SE5_6A               0x506A0081
#define NA_SE5_6C               0x506C0081
#define NA_SE5_6D               0x506D0081
#define NA_SE5_6E               0x516E0081
#define NA_SE5_6F               0x506F0081
#define NA_SE5_70               0x50706081
#define NA_SE5_73               0x50734081
#define NA_SE5_74               0x50744081

#define NA_SE6_00               0x60000001
#define NA_SE6_02_80            0x60028001
#define NA_SE6_02_FF            0x6002FF01
#define NA_SE6_03               0x60034001
#define NA_SE6_04_40            0x60044001
#define NA_SE6_04_80            0x60048001
#define NA_SE6_05               0x60050001
#define NA_SE6_06               0x60064001
#define NA_SE6_08               0x60086001
#define NA_SE6_09               0x60098001
#define NA_SE6_0A               0x600A4001
#define NA_SE6_0B               0x600B4001
#define NA_SE6_10               0x60104001

#define NA_SE7_00               0x7000F881
#if NA_REVISION >= 101
#define NA_SE7_02               0x7002FF81
#else
#define NA_SE7_02               0x7002F081
#endif
#define NA_SE7_03               0x7003FF81
#define NA_SE7_04               0x70040081
#define NA_SE7_05               0x70050081
#define NA_SE7_06               0x70060081
#define NA_SE7_07               0x70070081
#define NA_SE7_08               0x70080081
#define NA_SE7_09               0x70090081
#define NA_SE7_0A               0x700A0081
#define NA_SE7_0B               0x700B0081
#define NA_SE7_0C               0x700C0081
#define NA_SE7_0D               0x700D0081
#define NA_SE7_0E               0x700E0081
#define NA_SE7_0F               0x700F0081
#define NA_SE7_11               0x70110081
#define NA_SE7_13               0x70130081
#define NA_SE7_14               0x70140081
#define NA_SE7_15               0x70150081
#define NA_SE7_16               0x7016A081
#define NA_SE7_17               0x7017A081
#define NA_SE7_18               0x70188081
#define NA_SE7_19               0x71198081
#define NA_SE7_1A               0x701A8081
#define NA_SE7_1D               0x701DB081
#define NA_SE7_1E               0x701EFF81
#define NA_SE7_1F               0x701FFF81
#define NA_SE7_22               0x70222081
#define NA_SE7_23               0x7023FF81
#define NA_SE7_24               0x7024FF81

#define NA_SE8_2E               0x802E2081
#define NA_SE8_3E               0x803EC081
#define NA_SE8_40               0x80400081
#define NA_SE8_48               0x80482081
#define NA_SE8_4B               0x814BE081
#define NA_SE8_4C               0x814CF081
#define NA_SE8_50               0x80504001
#define NA_SE8_54               0x8054F011
#define NA_SE8_55               0x8055F011
#define NA_SE8_57               0x8057FF91
#define NA_SE8_59               0x80590081
#define NA_SE8_60               0x80600081
#define NA_SE8_61               0x80610081
#define NA_SE8_63               0x8063D081
#define NA_SE8_6A               0x806AA081

#define NA_SE9_04               0x90040081
#define NA_SE9_10               0x90105081
#define NA_SE9_11               0x90116081
#define NA_SE9_19               0x90192081
#define NA_SE9_1C               0x901C0081
#define NA_SE9_42               0x91424081
#define NA_SE9_43               0x90434081
#define NA_SE9_44               0x90444081
#define NA_SE9_45               0x90450081
#define NA_SE9_49               0x90490081
#define NA_SE9_52               0x90524001
#define NA_SE9_57               0x90570081
#define NA_SE9_5A_00            0x935A0081
#define NA_SE9_5A_C0            0x935AC081
#define NA_SE9_5B               0x925B0081
#define NA_SE9_66               0x90668081
#define NA_SE9_67               0x90678081
#define NA_SE9_69               0x90694081
#define NA_SE9_6B               0x906B0081

#define NA_TIME(x)              (8*(x)-2)

#endif /* __SM64_DEFAUDIO_H__ */
