#include <ultra64.h>
#include <PR/leoappli.h>

const char LEOfirmware_rev[] = "B014A17";

const u8 leo_rodata_804B21A8[9] = {2,2,2,2,2,2,2,2,2};
const u8 leo_rodata_804B21B4[9] = {3,3,3,3,3,3,3,3,3};
const u8 leo_rodata_804B21C0[9] = {0,0,0,0,0,0,0,0,0};
const u8 leo_rodata_804B21CC[9] = {0,0,0,0,0,0,0,0,0};

const u8 LEOBYTE_TBL1[9] = {232,216,208,192,176,160,144,128,112};
const u16 LEOBYTE_TBL2[9] =
	{232*85,216*85,208*85,192*85,176*85,160*85,144*85,128*85,112*85};

const u16 LEOVZONE_TBL[7][16] =
{
{292,584,858,1150,1442,1716,1990,2264,2538,2742,2946,3220,3494,3768,4042,4316},
{292,584,858,1132,1406,1698,1990,2264,2538,2812,3016,3220,3494,3768,4042,4316},
{292,584,858,1132,1406,1680,1954,2246,2538,2812,3086,3290,3494,3768,4042,4316},
{292,584,858,1132,1406,1680,1954,2228,2502,2794,3086,3360,3564,3768,4042,4316},
{292,584,858,1132,1406,1680,1954,2228,2502,2776,3050,3342,3634,3838,4042,4316},
{292,584,858,1132,1406,1680,1954,2158,2432,2706,2980,3254,3528,3820,4112,4316},
{292,584,858,1132,1406,1680,1954,2158,2362,2636,2910,3184,3458,3732,4024,4316},
};

const u16 LEOZONE_SCYL_TBL[16] =
	{0,158,316,465,614,763,912,1061,145,303,452,601,750,899,1048,1162};

const u8 LEOVZONE_PZONEHD_TBL[7][16] =
{
	{0,1,2,9,8,3,4,5,6,7,15,14,13,12,11,10},
	{0,1,2,3,10,9,8,4,5,6,7,15,14,13,12,11},
	{0,1,2,3,4,11,10,9,8,5,6,7,15,14,13,12},
	{0,1,2,3,4,5,12,11,10,9,8,6,7,15,14,13},
	{0,1,2,3,4,5,6,13,12,11,10,9,8,7,15,14},
	{0,1,2,3,4,5,6,7,14,13,12,11,10,9,8,15},
	{0,1,2,3,4,5,6,7,15,14,13,12,11,10,9,8},
};

const u16 LEOZONE_OUTERCYL_TBL[9-1] = {0,158,316,465,614,763,912,1061};

const u16 LEORAM_START_LBA[7] = {1442,1990,2538,3086,3634,4112,4316};

const u32 LEORAM_BYTE[7] =
	{0x24A9DC0,0x1C226C0,0x1450F00,0xD35680,0x6CFD40,0x1DA240,0};

const u8 leo_rodata_804B23A4[] =
{
	sizeof(LEOCmdClearQue)      - sizeof(OSMesgQueue *),
	sizeof(LEOCmdClearQue)      - sizeof(OSMesgQueue *),
	sizeof(LEOCmdInquiry)       - sizeof(OSMesgQueue *),
	sizeof(LEOCmdTestUnitReady) - sizeof(OSMesgQueue *),
	sizeof(LEOCmdRezero)        - sizeof(OSMesgQueue *),
	sizeof(LEOCmdRead)          - sizeof(OSMesgQueue *),
	sizeof(LEOCmdWrite)         - sizeof(OSMesgQueue *),
	sizeof(LEOCmdSeek)          - sizeof(OSMesgQueue *),
	sizeof(LEOCmdStartStop)     - sizeof(OSMesgQueue *),
	sizeof(LEOCmdReadCapacity)  - sizeof(OSMesgQueue *),
	sizeof(LEOCmdTranslate)     - sizeof(OSMesgQueue *),
	sizeof(LEOCmdModeSelect)    - sizeof(OSMesgQueue *),
	sizeof(LEOCmdReadDiskId)    - sizeof(OSMesgQueue *),
};
