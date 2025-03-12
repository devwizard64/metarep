#ifndef __SM64_DEFMAP_H__
#define __SM64_DEFMAP_H__

#define MAP_VTX                 64
#define MAP_BGEND               65
#define MAP_END                 66
#define MAP_OBJECT              67
#define MAP_WATER               68
#define MAP_FACE                100

#define BG_1                    1
#define BG_4                    4   /* attr */
#define BG_5                    5
#define BG_9                    9
#define BG_10                   10
#define BG_14                   14  /* attr */
#define BG_18                   18
#define BG_19                   19
#define BG_20                   20
#define BG_21                   21
#define BG_26                   26
#define BG_CONNECT              27  /* 27..30 */
#define BG_33                   33
#define BG_34                   34
#define BG_35                   35
#define BG_36                   36  /* attr */
#define BG_37                   37  /* attr */
#define BG_38                   38
#define BG_39                   39  /* attr */
#define BG_41                   41
#define BG_42                   42
#define BG_44                   44  /* attr */
#define BG_45                   45  /* attr */
#define BG_46                   46
#define BG_47                   47
#define BG_48                   48
#define BG_50                   50
#define BG_51                   51
#define BG_52                   52
#define BG_53                   53
#define BG_54                   54
#define BG_55                   55
#define BG_56                   56
#define BG_114                  114
#define BG_115                  115
#define BG_116                  116
#define BG_117                  117
#define BG_118                  118
#define BG_119                  119
#define BG_120                  120
#define BG_121                  121
#define BG_122                  122
#define BG_123                  123

#define BGPORT_MAX              (3*15)

#define BG_WAVE                 (BG_PORT-BGPORT_MAX)    /* 166..210 */
#define BG_PORT                 (256-BGPORT_MAX)        /* 211..255 */
#define BG_WAVEL(i)             (BG_WAVE + 3*(i) + 0)
#define BG_WAVEM(i)             (BG_WAVE + 3*(i) + 1)
#define BG_WAVER(i)             (BG_WAVE + 3*(i) + 2)
#define BG_PORTL(i)             (BG_PORT + 3*(i) + 0)
#define BG_PORTM(i)             (BG_PORT + 3*(i) + 1)
#define BG_PORTR(i)             (BG_PORT + 3*(i) + 2)

#endif /* __SM64_DEFMAP_H__ */
