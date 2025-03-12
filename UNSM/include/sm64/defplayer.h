#ifndef __SM64_DEFPLAYER_H__
#define __SM64_DEFPLAYER_H__

#define PL_DEFCAP               0x00000001
#define PL_VANISHCAP            0x00000002
#define PL_METALCAP             0x00000004
#define PL_WINGCAP              0x00000008
#define PL_SPECIALCAP           (PL_VANISHCAP|PL_METALCAP|PL_WINGCAP)
#define PL_ANYCAP               (PL_DEFCAP|PL_VANISHCAP|PL_METALCAP|PL_WINGCAP)
#define PL_HEADCAP              0x00000010
#define PL_HANDCAP              0x00000020
#define PL_00000040             0x00000040  /* env effect */
#define PL_00000080             0x00000080  /* xlu effect */
#define PL_00000100             0x00000100  /* jump status */
#define PL_SOUND                0x00010000
#define PL_VOICE                0x00020000
#define PL_00040000             0x00040000  /* jump voice */
#define PL_PUNCH                0x00100000
#define PL_KICK                 0x00200000
#define PL_SWEEPKICK            0x00400000
#define PL_02000000             0x02000000  /* camera */
#define PL_40000000             0x40000000
#define PL_80000000             0x80000000

#define PA_WALKREQ              0x0001
#define PA_JUMPREQ              0x0002
#define PA_LANDREQ              0x0004
#define PA_SLIPREQ              0x0008
#define PA_MOTION               (PA_WALKREQ|PA_JUMPREQ|PA_LANDREQ|PA_SLIPREQ)
#define PA_VIEWREQ              0x0010
#define PA_WAITREQ              0x0020
#define PA_PRESREQ              0x0040
#define PA_JUMPSTA              0x0080
#define PA_GAS                  0x0100
#define PA_WADING               0x0200
#define PA_HIT                  0x0400
#define PA_TAKEREQ              0x0800
#define PA_ATCKREQ              0x2000
#define PA_TRIGSTA              0x4000
#define PA_TRIGREQ              0x8000
#define PA_ACTION               \
	(PA_MOTION|PA_VIEWREQ|PA_HIT|PA_ATCKREQ|PA_TRIGREQ)
#if REVISION >= 199609
#define PA_READREQ              (PA_JUMPREQ|PA_ATCKREQ)
#else
#define PA_READREQ              PA_ATCKREQ
#endif

#define PE_00000001             0x00000001
#define PE_00000002             0x00000002
#define PE_00000008             0x00000008
#define PE_00000010             0x00000010
#define PE_00000020             0x00000020
#define PE_00000040             0x00000040
#define PE_00000080             0x00000080
#define PE_00000100             0x00000100
#define PE_00000200             0x00000200
#define PE_00000400             0x00000400
#define PE_00000800             0x00000800
#define PE_00001000             0x00001000
#define PE_00002000             0x00002000
#define PE_00004000             0x00004000
#define PE_00008000             0x00008000
#define PE_00010000             0x00010000
#define PE_00020000             0x00020000
#define PE_00040000             0x00040000

#define PF_WAIT                 0x00000200
#define PF_WALK                 0x00000400
#define PF_JUMP                 0x00000800
#define PF_DEMO                 0x00001000
#define PF_SWIM                 0x00002000
#define PF_SINK                 0x00004000
#define PF_SHRT                 0x00008000
#define PF_RIDE                 0x00010000
#define PF_DMGE                 0x00020000
#define PF_SLIP                 0x00040000
#define PF_DIVE                 0x00080000
#define PF_POLE                 0x00100000
#define PF_ROOF                 0x00200000
#define PF_READ                 0x00400000
#define PF_ATCK                 0x00800000
#define PF_WIND                 0x01000000
#define PF_JPCN                 0x02000000
#define PF_VIEW                 0x04000000
#define PF_QUIT                 0x08000000
#define PF_HAND                 0x10000000
#define PF_HEAD                 0x20000000
#define PF_THRW                 0x80000000

#define PC_MASK                 0x1C0
#define PC_WAIT                 0x000
#define PC_WALK                 0x040
#define PC_JUMP                 0x080
#define PC_SWIM                 0x0C0
#define PC_DEMO                 0x100
#define PC_SPEC                 0x140
#define PC_ATCK                 0x180

#define PS_MASK                 0x1FF

#define PS_NULL                 0

#define PS_WAIT_01              /* 0x0C400201 */ (PC_WAIT|0x01|PF_WAIT|PF_READ|PF_VIEW|PF_QUIT)
#define PS_WAIT_02              /* 0x0C400202 */ (PC_WAIT|0x02|PF_WAIT|PF_READ|PF_VIEW|PF_QUIT)
#define PS_WAIT_03              /* 0x0C000203 */ (PC_WAIT|0x03|PF_WAIT|PF_VIEW|PF_QUIT)
#define PS_WAIT_04              /* 0x0C000204 */ (PC_WAIT|0x04|PF_WAIT|PF_VIEW|PF_QUIT)
#define PS_WAIT_05              /* 0x0C400205 */ (PC_WAIT|0x05|PF_WAIT|PF_READ|PF_VIEW|PF_QUIT)
#define PS_WAIT_06              /* 0x08000206 */ (PC_WAIT|0x06|PF_WAIT|PF_QUIT)
#define PS_WAIT_07              /* 0x08000207 */ (PC_WAIT|0x07|PF_WAIT|PF_QUIT)
#define PS_WAIT_08              /* 0x08000208 */ (PC_WAIT|0x08|PF_WAIT|PF_QUIT)
#define PS_WAIT_09              /* 0x0C400209 */ (PC_WAIT|0x09|PF_WAIT|PF_READ|PF_VIEW|PF_QUIT)
#define PS_WAIT_0A              /* 0x0C40020A */ (PC_WAIT|0x0A|PF_WAIT|PF_READ|PF_VIEW|PF_QUIT)
#define PS_WAIT_0B              /* 0x0C40020B */ (PC_WAIT|0x0B|PF_WAIT|PF_READ|PF_VIEW|PF_QUIT)
#define PS_WAIT_0D              /* 0x0002020D */ (PC_WAIT|0x0D|PF_WAIT|PF_DMGE)
#define PS_WAIT_0E              /* 0x0002020E */ (PC_WAIT|0x0E|PF_WAIT|PF_DMGE)
#define PS_WAIT_20              /* 0x0C008220 */ (PC_WAIT|0x20|PF_WAIT|PF_SHRT|PF_VIEW|PF_QUIT)
#define PS_WAIT_21              /* 0x0C008221 */ (PC_WAIT|0x21|PF_WAIT|PF_SHRT|PF_VIEW|PF_QUIT)
#define PS_WAIT_22              /* 0x0C008222 */ (PC_WAIT|0x22|PF_WAIT|PF_SHRT|PF_VIEW|PF_QUIT)
#define PS_WAIT_23              /* 0x0C008223 */ (PC_WAIT|0x23|PF_WAIT|PF_SHRT|PF_VIEW|PF_QUIT)
#define PS_WAIT_24              /* 0x0C008224 */ (PC_WAIT|0x24|PF_WAIT|PF_SHRT|PF_VIEW|PF_QUIT)
#define PS_WAIT_25              /* 0x08000225 */ (PC_WAIT|0x25|PF_WAIT|PF_QUIT)
#define PS_WAIT_26              /* 0x00020226 */ (PC_WAIT|0x26|PF_WAIT|PF_DMGE)
#define PS_WAIT_27              /* 0x0C000227 */ (PC_WAIT|0x27|PF_WAIT|PF_VIEW|PF_QUIT)
#define PS_WAIT_2F              /* 0x0800022F */ (PC_WAIT|0x2F|PF_WAIT|PF_QUIT)
#define PS_WAIT_30              /* 0x0C000230 */ (PC_WAIT|0x30|PF_WAIT|PF_VIEW|PF_QUIT)
#define PS_WAIT_31              /* 0x0C000231 */ (PC_WAIT|0x31|PF_WAIT|PF_VIEW|PF_QUIT)
#define PS_WAIT_32              /* 0x0C000232 */ (PC_WAIT|0x32|PF_WAIT|PF_VIEW|PF_QUIT)
#define PS_WAIT_33              /* 0x0C000233 */ (PC_WAIT|0x33|PF_WAIT|PF_VIEW|PF_QUIT)
#define PS_WAIT_34              /* 0x08000234 */ (PC_WAIT|0x34|PF_WAIT|PF_QUIT)
#define PS_WAIT_35              /* 0x08000235 */ (PC_WAIT|0x35|PF_WAIT|PF_QUIT)
#define PS_WAIT_36              /* 0x80000A36 */ (PC_WAIT|0x36|PF_WAIT|PF_JUMP|PF_THRW)
#define PS_WAIT_38              /* 0x18800238 */ (PC_WAIT|0x38|PF_WAIT|PF_ATCK|PF_QUIT|PF_HAND)
#define PS_WAIT_39              /* 0x08000239 */ (PC_WAIT|0x39|PF_WAIT|PF_QUIT)
#define PS_WAIT_3A              /* 0x0800023A */ (PC_WAIT|0x3A|PF_WAIT|PF_QUIT)
#define PS_WAIT_3B              /* 0x0800023B */ (PC_WAIT|0x3B|PF_WAIT|PF_QUIT)
#define PS_WAIT_3C              /* 0x0080023C */ (PC_WAIT|0x3C|PF_WAIT|PF_ATCK)
#define PS_WAIT_3D              /* 0x0C00023D */ (PC_WAIT|0x3D|PF_WAIT|PF_VIEW|PF_QUIT)
#define PS_WAIT_3E              /* 0x0C00023E */ (PC_WAIT|0x3E|PF_WAIT|PF_VIEW|PF_QUIT)
#define PS_WAIT_3F              /* 0x0800043F */ (PC_WAIT|0x3F|PF_WALK|PF_QUIT)

#define PS_WALK_00              /* 0x04000440 */ (PC_WALK|0x00|PF_WALK|PF_VIEW)
#define PS_WALK_02              /* 0x00000442 */ (PC_WALK|0x02|PF_WALK)
#define PS_WALK_03              /* 0x00000443 */ (PC_WALK|0x03|PF_WALK)
#define PS_WALK_04              /* 0x00000444 */ (PC_WALK|0x04|PF_WALK)
#define PS_WALK_05              /* 0x04000445 */ (PC_WALK|0x05|PF_WALK|PF_VIEW)
#define PS_WALK_06              /* 0x20810446 */ (PC_WALK|0x06|PF_WALK|PF_RIDE|PF_ATCK|PF_HEAD)
#define PS_WALK_07              /* 0x00000447 */ (PC_WALK|0x07|PF_WALK)
#define PS_WALK_08              /* 0x04008448 */ (PC_WALK|0x08|PF_WALK|PF_SHRT|PF_VIEW)
#define PS_WALK_09              /* 0x00020449 */ (PC_WALK|0x09|PF_WALK|PF_DMGE)
#define PS_WALK_0A              /* 0x0400044A */ (PC_WALK|0x0A|PF_WALK|PF_VIEW)
#define PS_WALK_0B              /* 0x0000044B */ (PC_WALK|0x0B|PF_WALK)
#define PS_WALK_10              /* 0x00000050 */ (PC_WALK|0x10)
#define PS_WALK_11              /* 0x00000051 */ (PC_WALK|0x11)
#define PS_WALK_12              /* 0x00840452 */ (PC_WALK|0x12|PF_WALK|PF_SLIP|PF_ATCK)
#define PS_WALK_13              /* 0x008C0453 */ (PC_WALK|0x13|PF_WALK|PF_SLIP|PF_DIVE|PF_ATCK)
#define PS_WALK_14              /* 0x00840454 */ (PC_WALK|0x14|PF_WALK|PF_SLIP|PF_ATCK)
#define PS_WALK_15              /* 0x008C0455 */ (PC_WALK|0x15|PF_WALK|PF_SLIP|PF_DIVE|PF_ATCK)
#define PS_WALK_16              /* 0x00880456 */ (PC_WALK|0x16|PF_WALK|PF_DIVE|PF_ATCK)
#define PS_WALK_17              /* 0x00800457 */ (PC_WALK|0x17|PF_WALK|PF_ATCK)
#define PS_WALK_19              /* 0x04808459 */ (PC_WALK|0x19|PF_WALK|PF_SHRT|PF_ATCK|PF_VIEW)
#define PS_WALK_1A              /* 0x0080045A */ (PC_WALK|0x1A|PF_WALK|PF_ATCK)
#define PS_WALK_20              /* 0x00020460 */ (PC_WALK|0x20|PF_WALK|PF_DMGE)
#define PS_WALK_21              /* 0x00020461 */ (PC_WALK|0x21|PF_WALK|PF_DMGE)
#define PS_WALK_22              /* 0x00020462 */ (PC_WALK|0x22|PF_WALK|PF_DMGE)
#define PS_WALK_23              /* 0x00020463 */ (PC_WALK|0x23|PF_WALK|PF_DMGE)
#define PS_WALK_24              /* 0x00020464 */ (PC_WALK|0x24|PF_WALK|PF_DMGE)
#define PS_WALK_25              /* 0x00020465 */ (PC_WALK|0x25|PF_WALK|PF_DMGE)
#define PS_WALK_26              /* 0x00020466 */ (PC_WALK|0x26|PF_WALK|PF_DMGE)
#define PS_WALK_27              /* 0x00020467 */ (PC_WALK|0x27|PF_WALK|PF_DMGE)
#define PS_WALK_30              /* 0x04000470 */ (PC_WALK|0x30|PF_WALK|PF_VIEW)
#define PS_WALK_31              /* 0x04000471 */ (PC_WALK|0x31|PF_WALK|PF_VIEW)
#define PS_WALK_32              /* 0x04000472 */ (PC_WALK|0x32|PF_WALK|PF_VIEW)
#define PS_WALK_33              /* 0x04000473 */ (PC_WALK|0x33|PF_WALK|PF_VIEW)
#define PS_WALK_34              /* 0x00000474 */ (PC_WALK|0x34|PF_WALK)
#define PS_WALK_35              /* 0x00000475 */ (PC_WALK|0x35|PF_WALK)
#define PS_WALK_36              /* 0x00000476 */ (PC_WALK|0x36|PF_WALK)
#define PS_WALK_37              /* 0x00000477 */ (PC_WALK|0x37|PF_WALK)
#define PS_WALK_38              /* 0x04000478 */ (PC_WALK|0x38|PF_WALK|PF_VIEW)
#define PS_WALK_39              /* 0x00000479 */ (PC_WALK|0x39|PF_WALK)
#define PS_WALK_3A              /* 0x0400047A */ (PC_WALK|0x3A|PF_WALK|PF_VIEW)

#define PS_JUMP_00              /* 0x03000880 */ (PC_JUMP|0x00|PF_JUMP|PF_WIND|PF_JPCN)
#define PS_JUMP_01              /* 0x03000881 */ (PC_JUMP|0x01|PF_JUMP|PF_WIND|PF_JPCN)
#define PS_JUMP_02              /* 0x01000882 */ (PC_JUMP|0x02|PF_JUMP|PF_WIND)
#define PS_JUMP_03              /* 0x01000883 */ (PC_JUMP|0x03|PF_JUMP|PF_WIND)
#define PS_JUMP_14              /* 0x03000894 */ (PC_JUMP|0x14|PF_JUMP|PF_WIND|PF_JPCN)
#define PS_JUMP_05              /* 0x03000885 */ (PC_JUMP|0x05|PF_JUMP|PF_WIND|PF_JPCN)
#define PS_JUMP_06              /* 0x03000886 */ (PC_JUMP|0x06|PF_JUMP|PF_WIND|PF_JPCN)
#define PS_JUMP_07              /* 0x01000887 */ (PC_JUMP|0x07|PF_JUMP|PF_WIND)
#define PS_JUMP_08              /* 0x03000888 */ (PC_JUMP|0x08|PF_JUMP|PF_WIND|PF_JPCN)
#define PS_JUMP_09              /* 0x01000889 */ (PC_JUMP|0x09|PF_JUMP|PF_WIND)
#define PS_JUMP_0A              /* 0x0188088A */ (PC_JUMP|0x0A|PF_JUMP|PF_DIVE|PF_ATCK|PF_WIND)
#define PS_JUMP_0C              /* 0x0100088C */ (PC_JUMP|0x0C|PF_JUMP|PF_WIND)
#define PS_JUMP_0D              /* 0x0300088D */ (PC_JUMP|0x0D|PF_JUMP|PF_WIND|PF_JPCN)
#define PS_JUMP_0E              /* 0x0300088E */ (PC_JUMP|0x0E|PF_JUMP|PF_WIND|PF_JPCN)
#define PS_JUMP_18              /* 0x00880898 */ (PC_JUMP|0x18|PF_JUMP|PF_DIVE|PF_ATCK)
#define PS_JUMP_19              /* 0x10880899 */ (PC_JUMP|0x19|PF_JUMP|PF_DIVE|PF_ATCK|PF_HAND)
#define PS_JUMP_1A              /* 0x0281089A */ (PC_JUMP|0x1A|PF_JUMP|PF_RIDE|PF_ATCK|PF_JPCN)
#define PS_JUMP_1B              /* 0x0081089B */ (PC_JUMP|0x1B|PF_JUMP|PF_RIDE|PF_ATCK)
#define PS_JUMP_1C              /* 0x1008089C */ (PC_JUMP|0x1C|PF_JUMP|PF_DIVE|PF_HAND)
#define PS_JUMP_20              /* 0x030008A0 */ (PC_JUMP|0x20|PF_JUMP|PF_WIND|PF_JPCN)
#define PS_JUMP_21              /* 0x010008A1 */ (PC_JUMP|0x21|PF_JUMP|PF_WIND)
#define PS_JUMP_22              /* 0x010008A2 */ (PC_JUMP|0x22|PF_JUMP|PF_WIND)
#define PS_JUMP_23              /* 0x010008A3 */ (PC_JUMP|0x23|PF_JUMP|PF_WIND)
#define PS_JUMP_24              /* 0x108008A4 */ (PC_JUMP|0x24|PF_JUMP|PF_ATCK|PF_HAND)
#define PS_JUMP_26              /* 0x010008A6 */ (PC_JUMP|0x26|PF_JUMP|PF_WIND)
#define PS_JUMP_27              /* 0x000008A7 */ (PC_JUMP|0x27|PF_JUMP)
#define PS_JUMP_28              /* 0x000004A8 */ (PC_JUMP|0x28|PF_WALK)
#define PS_JUMP_29              /* 0x008008A9 */ (PC_JUMP|0x29|PF_JUMP|PF_ATCK)
#define PS_JUMP_2A              /* 0x018008AA */ (PC_JUMP|0x2A|PF_JUMP|PF_ATCK|PF_WIND)
#define PS_JUMP_2B              /* 0x830008AB */ (PC_JUMP|0x2B|PF_JUMP|PF_WIND|PF_JPCN|PF_THRW)
#define PS_JUMP_2C              /* 0x018008AC */ (PC_JUMP|0x2C|PF_JUMP|PF_ATCK|PF_WIND)
#define PS_JUMP_2D              /* 0x010008AD */ (PC_JUMP|0x2D|PF_JUMP|PF_WIND)
#define PS_JUMP_2E              /* 0x000008AE */ (PC_JUMP|0x2E|PF_JUMP)
#define PS_JUMP_2F              /* 0x030008AF */ (PC_JUMP|0x2F|PF_JUMP|PF_WIND|PF_JPCN)
#define PS_JUMP_30              /* 0x010208B0 */ (PC_JUMP|0x30|PF_JUMP|PF_DMGE|PF_WIND)
#define PS_JUMP_31              /* 0x010208B1 */ (PC_JUMP|0x31|PF_JUMP|PF_DMGE|PF_WIND)
#define PS_JUMP_32              /* 0x010208B2 */ (PC_JUMP|0x32|PF_JUMP|PF_DMGE|PF_WIND)
#define PS_JUMP_33              /* 0x010208B3 */ (PC_JUMP|0x33|PF_JUMP|PF_DMGE|PF_WIND)
#define PS_JUMP_34              /* 0x010208B4 */ (PC_JUMP|0x34|PF_JUMP|PF_DMGE|PF_WIND)
#define PS_JUMP_35              /* 0x010208B5 */ (PC_JUMP|0x35|PF_JUMP|PF_DMGE|PF_WIND)
#define PS_JUMP_36              /* 0x010208B6 */ (PC_JUMP|0x36|PF_JUMP|PF_DMGE|PF_WIND)
#define PS_JUMP_37              /* 0x010208B7 */ (PC_JUMP|0x37|PF_JUMP|PF_DMGE|PF_WIND)
#define PS_JUMP_38              /* 0x010208B8 */ (PC_JUMP|0x38|PF_JUMP|PF_DMGE|PF_WIND)
#define PS_JUMP_3D              /* 0x010208BD */ (PC_JUMP|0x3D|PF_JUMP|PF_DMGE|PF_WIND)
#define PS_JUMP_3E              /* 0x010208BE */ (PC_JUMP|0x3E|PF_JUMP|PF_DMGE|PF_WIND)

#define PS_SWIM_00              /* 0x380022C0 */ (PC_SWIM|0x00|PF_WAIT|PF_SWIM|PF_QUIT|PF_HAND|PF_HEAD)
#define PS_SWIM_01              /* 0x380022C1 */ (PC_SWIM|0x01|PF_WAIT|PF_SWIM|PF_QUIT|PF_HAND|PF_HEAD)
#define PS_SWIM_02              /* 0x300022C2 */ (PC_SWIM|0x02|PF_WAIT|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_03              /* 0x300022C3 */ (PC_SWIM|0x03|PF_WAIT|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_04              /* 0x300032C4 */ (PC_SWIM|0x04|PF_WAIT|PF_DEMO|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_05              /* 0x300222C5 */ (PC_SWIM|0x05|PF_WAIT|PF_SWIM|PF_DMGE|PF_HAND|PF_HEAD)
#define PS_SWIM_06              /* 0x300222C6 */ (PC_SWIM|0x06|PF_WAIT|PF_SWIM|PF_DMGE|PF_HAND|PF_HEAD)
#define PS_SWIM_07              /* 0x300032C7 */ (PC_SWIM|0x07|PF_WAIT|PF_DEMO|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_08              /* 0x300222C8 */ (PC_SWIM|0x08|PF_WAIT|PF_SWIM|PF_DMGE|PF_HAND|PF_HEAD)
#define PS_SWIM_10              /* 0x300024D0 */ (PC_SWIM|0x10|PF_WALK|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_11              /* 0x300024D1 */ (PC_SWIM|0x11|PF_WALK|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_12              /* 0x300024D2 */ (PC_SWIM|0x12|PF_WALK|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_13              /* 0x300024D3 */ (PC_SWIM|0x13|PF_WALK|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_14              /* 0x300024D4 */ (PC_SWIM|0x14|PF_WALK|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_15              /* 0x300024D5 */ (PC_SWIM|0x15|PF_WALK|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_16              /* 0x300024D6 */ (PC_SWIM|0x16|PF_WALK|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_20              /* 0x300024E0 */ (PC_SWIM|0x20|PF_WALK|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_21              /* 0x300024E1 */ (PC_SWIM|0x21|PF_WALK|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_22              /* 0x300022E2 */ (PC_SWIM|0x22|PF_WAIT|PF_SWIM|PF_HAND|PF_HEAD)
#define PS_SWIM_23              /* 0x300222E3 */ (PC_SWIM|0x23|PF_WAIT|PF_SWIM|PF_DMGE|PF_HAND|PF_HEAD)
#define PS_SWIM_30              /* 0x080042F0 */ (PC_SWIM|0x30|PF_WAIT|PF_SINK|PF_QUIT)
#define PS_SWIM_31              /* 0x080042F1 */ (PC_SWIM|0x31|PF_WAIT|PF_SINK|PF_QUIT)
#define PS_SWIM_32              /* 0x000044F2 */ (PC_SWIM|0x32|PF_WALK|PF_SINK)
#define PS_SWIM_33              /* 0x000044F3 */ (PC_SWIM|0x33|PF_WALK|PF_SINK)
#define PS_SWIM_34              /* 0x000042F4 */ (PC_SWIM|0x34|PF_WAIT|PF_SINK)
#define PS_SWIM_35              /* 0x000042F5 */ (PC_SWIM|0x35|PF_WAIT|PF_SINK)
#define PS_SWIM_36              /* 0x000042F6 */ (PC_SWIM|0x36|PF_WAIT|PF_SINK)
#define PS_SWIM_37              /* 0x000042F7 */ (PC_SWIM|0x37|PF_WAIT|PF_SINK)
#define PS_SWIM_38              /* 0x000044F8 */ (PC_SWIM|0x38|PF_WALK|PF_SINK)
#define PS_SWIM_39              /* 0x000044F9 */ (PC_SWIM|0x39|PF_WALK|PF_SINK)
#define PS_SWIM_3A              /* 0x000044FA */ (PC_SWIM|0x3A|PF_WALK|PF_SINK)
#define PS_SWIM_3B              /* 0x000044FB */ (PC_SWIM|0x3B|PF_WALK|PF_SINK)

#define PS_DEMO_00              /* 0x00001300 */ (PC_DEMO|0x00|PF_WAIT|PF_DEMO)
#define PS_DEMO_01              /* 0x04001301 */ (PC_DEMO|0x01|PF_WAIT|PF_DEMO|PF_VIEW)
#define PS_DEMO_02              /* 0x00001302 */ (PC_DEMO|0x02|PF_WAIT|PF_DEMO)
#define PS_DEMO_03              /* 0x00001303 */ (PC_DEMO|0x03|PF_WAIT|PF_DEMO)
#define PS_DEMO_04              /* 0x00001904 */ (PC_DEMO|0x04|PF_JUMP|PF_DEMO)
#define PS_DEMO_05              /* 0x20001305 */ (PC_DEMO|0x05|PF_WAIT|PF_DEMO|PF_HEAD)
#define PS_DEMO_06              /* 0x20001306 */ (PC_DEMO|0x06|PF_WAIT|PF_DEMO|PF_HEAD)
#define PS_DEMO_07              /* 0x00001307 */ (PC_DEMO|0x07|PF_WAIT|PF_DEMO)
#define PS_DEMO_08              /* 0x00001308 */ (PC_DEMO|0x08|PF_WAIT|PF_DEMO)
#define PS_DEMO_09              /* 0x00001909 */ (PC_DEMO|0x09|PF_JUMP|PF_DEMO)
#define PS_DEMO_0A              /* 0x0000130A */ (PC_DEMO|0x0A|PF_WAIT|PF_DEMO)
#define PS_DEMO_0F              /* 0x0000130F */ (PC_DEMO|0x0F|PF_WAIT|PF_DEMO)
#define PS_DEMO_11              /* 0x00021311 */ (PC_DEMO|0x11|PF_WAIT|PF_DEMO|PF_DMGE)
#define PS_DEMO_12              /* 0x00021312 */ (PC_DEMO|0x12|PF_WAIT|PF_DEMO|PF_DMGE)
#define PS_DEMO_13              /* 0x00021313 */ (PC_DEMO|0x13|PF_WAIT|PF_DEMO|PF_DMGE)
#define PS_DEMO_14              /* 0x00021314 */ (PC_DEMO|0x14|PF_WAIT|PF_DEMO|PF_DMGE)
#define PS_DEMO_15              /* 0x00021315 */ (PC_DEMO|0x15|PF_WAIT|PF_DEMO|PF_DMGE)
#define PS_DEMO_16              /* 0x00021316 */ (PC_DEMO|0x16|PF_WAIT|PF_DEMO|PF_DMGE)
#define PS_DEMO_17              /* 0x00021317 */ (PC_DEMO|0x17|PF_WAIT|PF_DEMO|PF_DMGE)
#define PS_DEMO_18              /* 0x00001918 */ (PC_DEMO|0x18|PF_JUMP|PF_DEMO)
#define PS_DEMO_19              /* 0x00001319 */ (PC_DEMO|0x19|PF_WAIT|PF_DEMO)
#define PS_DEMO_1A              /* 0x0000131A */ (PC_DEMO|0x1A|PF_WAIT|PF_DEMO)
#define PS_DEMO_20              /* 0x00001320 */ (PC_DEMO|0x20|PF_WAIT|PF_DEMO)
#define PS_DEMO_21              /* 0x00001321 */ (PC_DEMO|0x21|PF_WAIT|PF_DEMO)
#define PS_DEMO_22              /* 0x00001322 */ (PC_DEMO|0x22|PF_WAIT|PF_DEMO)
#define PS_DEMO_23              /* 0x00001923 */ (PC_DEMO|0x23|PF_JUMP|PF_DEMO)
#define PS_DEMO_24              /* 0x00001924 */ (PC_DEMO|0x24|PF_JUMP|PF_DEMO)
#define PS_DEMO_25              /* 0x00001325 */ (PC_DEMO|0x25|PF_WAIT|PF_DEMO)
#define PS_DEMO_26              /* 0x00001926 */ (PC_DEMO|0x26|PF_JUMP|PF_DEMO)
#define PS_DEMO_27              /* 0x00001327 */ (PC_DEMO|0x27|PF_WAIT|PF_DEMO)
#define PS_DEMO_28              /* 0x00001928 */ (PC_DEMO|0x28|PF_JUMP|PF_DEMO)
#define PS_DEMO_29              /* 0x00001929 */ (PC_DEMO|0x29|PF_JUMP|PF_DEMO)
#define PS_DEMO_2A              /* 0x0000192A */ (PC_DEMO|0x2A|PF_JUMP|PF_DEMO)
#define PS_DEMO_2B              /* 0x0000192B */ (PC_DEMO|0x2B|PF_JUMP|PF_DEMO)
#define PS_DEMO_2C              /* 0x0000192C */ (PC_DEMO|0x2C|PF_JUMP|PF_DEMO)
#define PS_DEMO_2D              /* 0x0000192D */ (PC_DEMO|0x2D|PF_JUMP|PF_DEMO)
#define PS_DEMO_2E              /* 0x0000132E */ (PC_DEMO|0x2E|PF_WAIT|PF_DEMO)
#define PS_DEMO_2F              /* 0x0000132F */ (PC_DEMO|0x2F|PF_WAIT|PF_DEMO)
#define PS_DEMO_31              /* 0x00001331 */ (PC_DEMO|0x31|PF_WAIT|PF_DEMO)
#define PS_DEMO_32              /* 0x00001932 */ (PC_DEMO|0x32|PF_JUMP|PF_DEMO)
#define PS_DEMO_33              /* 0x00001333 */ (PC_DEMO|0x33|PF_WAIT|PF_DEMO)
#define PS_DEMO_34              /* 0x00001934 */ (PC_DEMO|0x34|PF_JUMP|PF_DEMO)
#define PS_DEMO_35              /* 0x00001535 */ (PC_DEMO|0x35|PF_WALK|PF_DEMO)
#define PS_DEMO_36              /* 0x00001336 */ (PC_DEMO|0x36|PF_WAIT|PF_DEMO)
#define PS_DEMO_37              /* 0x00001337 */ (PC_DEMO|0x37|PF_WAIT|PF_DEMO)
#define PS_DEMO_38              /* 0x00020338 */ (PC_DEMO|0x38|PF_WAIT|PF_DMGE)
#define PS_DEMO_39              /* 0x00020339 */ (PC_DEMO|0x39|PF_WAIT|PF_DMGE)
#define PS_DEMO_3A              /* 0x0002033A */ (PC_DEMO|0x3A|PF_WAIT|PF_DMGE)
#define PS_DEMO_3B              /* 0x0002033B */ (PC_DEMO|0x3B|PF_WAIT|PF_DMGE)
#define PS_DEMO_3C              /* 0x0002033C */ (PC_DEMO|0x3C|PF_WAIT|PF_DMGE)
#define PS_DEMO_3D              /* 0x0000133D */ (PC_DEMO|0x3D|PF_WAIT|PF_DEMO)

#define PS_SPEC_00              /* 0x08100340 */ (PC_SPEC|0x00|PF_WAIT|PF_POLE|PF_QUIT)
#define PS_SPEC_01              /* 0x00100341 */ (PC_SPEC|0x01|PF_WAIT|PF_POLE)
#define PS_SPEC_02              /* 0x00100342 */ (PC_SPEC|0x02|PF_WAIT|PF_POLE)
#define PS_SPEC_03              /* 0x00100343 */ (PC_SPEC|0x03|PF_WAIT|PF_POLE)
#define PS_SPEC_04              /* 0x00100344 */ (PC_SPEC|0x04|PF_WAIT|PF_POLE)
#define PS_SPEC_05              /* 0x00100345 */ (PC_SPEC|0x05|PF_WAIT|PF_POLE)
#define PS_SPEC_08              /* 0x08200348 */ (PC_SPEC|0x08|PF_WAIT|PF_ROOF|PF_QUIT)
#define PS_SPEC_09              /* 0x00200349 */ (PC_SPEC|0x09|PF_WAIT|PF_ROOF)
#define PS_SPEC_0A              /* 0x0020054A */ (PC_SPEC|0x0A|PF_WALK|PF_ROOF)
#define PS_SPEC_0B              /* 0x0800034B */ (PC_SPEC|0x0B|PF_WAIT|PF_QUIT)
#define PS_SPEC_0C              /* 0x0000054C */ (PC_SPEC|0x0C|PF_WALK)
#define PS_SPEC_0D              /* 0x0000054D */ (PC_SPEC|0x0D|PF_WALK)
#define PS_SPEC_0E              /* 0x0000054E */ (PC_SPEC|0x0E|PF_WALK)
#define PS_SPEC_0F              /* 0x0000054F */ (PC_SPEC|0x0F|PF_WALK)
#define PS_SPEC_30              /* 0x00020370 */ (PC_SPEC|0x30|PF_WAIT|PF_DMGE)
#define PS_SPEC_31              /* 0x00001371 */ (PC_SPEC|0x31|PF_WAIT|PF_DEMO)
#define PS_SPEC_32              /* 0x10020372 */ (PC_SPEC|0x32|PF_WAIT|PF_DMGE|PF_HAND)

#define PS_ATCK_00              /* 0x00800380 */ (PC_ATCK|0x00|PF_WAIT|PF_ATCK)
#define PS_ATCK_03              /* 0x00000383 */ (PC_ATCK|0x03|PF_WAIT)
#define PS_ATCK_05              /* 0x00000385 */ (PC_ATCK|0x05|PF_WAIT)
#define PS_ATCK_06              /* 0x00000386 */ (PC_ATCK|0x06|PF_WAIT)
#define PS_ATCK_07              /* 0x00000387 */ (PC_ATCK|0x07|PF_WAIT)
#define PS_ATCK_08              /* 0x80000588 */ (PC_ATCK|0x08|PF_WALK|PF_THRW)
#define PS_ATCK_09              /* 0x80000589 */ (PC_ATCK|0x09|PF_WALK|PF_THRW)
#define PS_ATCK_10              /* 0x00000390 */ (PC_ATCK|0x10|PF_WAIT)
#define PS_ATCK_11              /* 0x00000391 */ (PC_ATCK|0x11|PF_WAIT)
#define PS_ATCK_12              /* 0x00000392 */ (PC_ATCK|0x12|PF_WAIT)

#define WALK_FALL               0
#define WALK_STAY               1
#define WALK_STOP               2
#define WALK_WALL               3

#define JUMP_STAY               0
#define JUMP_LAND               1
#define JUMP_WALL               2
#define JUMP_LEDGE              3
#define JUMP_HANG               4
#define JUMP_BURN               6

#endif /* __SM64_DEFPLAYER_H__ */
