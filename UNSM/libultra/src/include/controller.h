#define PIFRAMSIZE 16

typedef struct
{
	u32 ramarray[PIFRAMSIZE-1];
	u32 pifstatus;
}
OSPifRam;

#define CONT_REQUEST            0
#define CONT_READ               1
#define CONT_RAM_READ           2
#define CONT_RAM_WRITE          3
#define CONT_EEPROM_READ        4
#define CONT_EEPROM_WRITE       5
#define CONT_SETCH              254
#define CONT_RESET              255
#define CONT_ETC                CONT_SETCH

#define CON_ERR_MASK            0xc0

#define CONT_FORMAT             1
#define CHANNEL_RESET           0xfd
#define FORMAT_END              0xfe

typedef struct
{
	u8 dummy;
	u8 txsize;
	u8 rxsize;
	u8 cmd;
	u8 typeh;
	u8 typel;
	u8 status;
	u8 dummy1;
}
__OSContRequesFormat;

typedef struct
{
	u8 txsize;
	u8 rxsize;
	u8 cmd;
	u8 typeh;
	u8 typel;
	u8 status;
}
__OSContRequesFormatShort;

typedef struct
{
	u8 dummy;
	u8 txsize;
	u8 rxsize;
	u8 cmd;
	u16 addr;
	u8 data[BLOCKSIZE];
	u8 datacrc;
}
__OSContRamReadFormat;

extern OSPifRam __osPfsPifRam;
extern int __osPfsLastChannel;

extern s32 __osContRamRead(OSMesgQueue *, int, u16, u8 *);
extern s32 __osContRamWrite(OSMesgQueue *, int, u16, u8 *, int);

extern s32 __osPfsGetStatus(OSMesgQueue *, int);

extern void __osPfsRequestData(u8);
extern void __osPfsGetInitData(u8 *, OSContStatus *);

#define EEPROM_WAIT             12000

typedef struct
{
	u8 txsize;
	u8 rxsize;
	u8 cmd;
	u8 address;
	u8 data[EEPROM_BLOCK_SIZE];
}
__OSContEepromFormat;

extern OSPifRam __osEepPifRam;
extern OSTimer __osEepromTimer;
extern OSMesgQueue __osEepromTimerQ;
extern OSMesg __osEepromTimerMsg;

extern s32 __osEepStatus(OSMesgQueue *, OSContStatus *);

typedef struct
{
	u8 dummy;
	u8 txsize;
	u8 rxsize;
	u8 cmd;
	u16 button;
	s8 stick_x;
	s8 stick_y;
}
__OSContReadFormat;

extern OSPifRam __osContPifRam;
extern u8 __osContLastCmd;
extern u8 __osMaxControllers;

extern void __osPackRequestData(u8);
extern void __osPackResetData(void);
extern void __osContGetInitData(u8 *, OSContStatus *);

extern u8 __osContAddressCrc(u16);
extern u8 __osContDataCrc(u8 *);
