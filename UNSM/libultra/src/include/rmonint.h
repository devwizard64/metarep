#define TV_ERROR_NO_ERROR 0
#define TV_ERROR_ILLEGAL_CALL -1
#define TV_ERROR_INVALID_ID -2
#define TV_ERROR_OP_PROTECTED -4
#define TV_ERROR_INVALID_ADDRESS -5
#define TV_ERROR_INVALID_CAPABILITY -8
#define TV_ERROR_NO_MORE_IDS -10

typedef int TVid;
typedef unsigned short TVushort;
typedef unsigned char TVuchar;

typedef struct __KKObjsStruct
{
	TVushort number;
	TVid objects[1];
}
KKObjs;

typedef struct __KKFaultInfoStruct
{
	unsigned int addr;
	short major;
	short minor;
}
KKFaultInfo;

typedef struct __KKThreadStatusStruct
{
	int flags;
	short why;
	short what;
	TVid tid;
	TVid pid;
	unsigned int instr;
	KKFaultInfo info;
	int priority;
	int start;
	int rv;
	unsigned args[6];
}
KKThreadStatus;

typedef struct __KKRunStruct
{
	int flags;
	unsigned int vaddr;
}
KKRun;

typedef struct __KKFaultStruct
{
	short majorMask;
	short minorMask;
}
KKFault;

typedef struct __KKRegionStruct
{
	unsigned int vaddr;
	unsigned int size;
	short flags;
	unsigned int paddr;
}
KKRegion;

typedef struct __KKGregSetStruct
{
	unsigned int gregs[37];
}
KKGregSet;

typedef struct __KKFPregSetStruct
{
	union
	{
		double dregs[16];
		float fregs[32];
		unsigned int regs[32];
	}
	fpregs;
	unsigned int fpcsr;
	unsigned int fppad;
}
KKFPregSet;

typedef struct __KKCpScalarSetStruct
{
	unsigned int sregs[40];
}
KKCpScalarRegSet;

typedef struct __KKCpVectorSetStruct
{
	unsigned int vregs[4*32];
}
KKCpVectorRegSet;

typedef struct __KKHeaderStruct
{
	int length;
	char code;
	char type;
	short error;
	char rev;
	char method;
	short notused2;
}
KKHeader;

typedef struct __KKObjectRequestStruct
{
	KKHeader header;
	TVid object;
}
KKObjectRequest;

typedef struct __KKRunThreadRequestStruct
{
	KKHeader header;
	TVid tid;
	KKRun actions;
}
KKRunThreadRequest;

typedef struct __KKFaultRequestStruct
{
	KKHeader header;
	TVid tid;
	KKFault fault;
	TVuchar stopAllThreads;
}
KKFaultRequest;

typedef struct __KKGRegsetRequestStruct
{
	KKHeader header;
	TVid tid;
	KKGregSet registers;
}
KKGRegsetRequest;

typedef struct __KKFPRegsetRequestStruct
{
	KKHeader header;
	TVid tid;
	KKFPregSet registers;
}
KKFPRegsetRequest;

typedef struct __KKCpScalarRegsetRequestStruct
{
	KKHeader header;
	TVid tid;
	KKCpScalarRegSet registers;
}
KKCpScalarRegsetRequest;

typedef struct __KKCpVectorRegsetRequestStruct
{
	KKHeader header;
	TVid tid;
	KKCpVectorRegSet registers;
}
KKCpVectorRegsetRequest;

typedef struct __KKReadRequestStruct
{
	KKHeader header;
	TVid object;
	unsigned int addr;
	unsigned int nbytes;
}
KKReadRequest;

typedef struct __KKWriteHeaderStruct
{
	KKHeader header;
	TVid object;
	unsigned int addr;
	unsigned int nbytes;
}
KKWriteHeader;

typedef struct __KKWriteRequestStruct
{
	KKWriteHeader writeHeader;
	char buffer[1];
}
KKWriteRequest;

typedef struct __KKSetBkptRequestStruct
{
	KKHeader header;
	TVid object;
	unsigned int addr;
}
KKSetBkptRequest;

typedef struct __KKClrBkptRequestStruct
{
	KKHeader header;
	TVid object;
	TVid bp;
}
KKClrBkptRequest;

typedef struct __KKObjectEventStruct
{
	KKHeader header;
	TVid object;
}
KKObjectEvent;

typedef struct __KKObjsEventStruct
{
	KKHeader header;
	TVid object;
	KKObjs objs;
}
KKObjsEvent;

typedef struct __KKBufferEventStruct
{
	KKHeader header;
	TVid object;
	char buffer[1];
}
KKBufferEvent;

typedef struct __KKStatusEventStruct
{
	KKHeader header;
	KKThreadStatus status;
}
KKStatusEvent;

typedef struct __KKNumberEventStruct
{
	KKHeader header;
	TVid object;
	unsigned int number;
}
KKNumberEvent;

typedef struct __KKRegionEventStruct
{
	KKHeader header;
	TVid object;
	unsigned int number;
	KKRegion regions[1];
}
KKRegionEvent;

typedef struct __KKGregEventStruct
{
	KKHeader header;
	TVid tid;
	KKGregSet registers;
}
KKGregEvent;

typedef struct __KKFPregEventStruct
{
	KKHeader header;
	TVid tid;
	KKFPregSet registers;
}
KKFPregEvent;

typedef struct __KKCpSregEventStruct
{
	KKHeader header;
	TVid tid;
	KKCpScalarRegSet registers;
}
KKCpSregEvent;

typedef struct __KKCpVregEventStruct
{
	KKHeader header;
	TVid tid;
	KKCpVectorRegSet registers;
}
KKCpVregEvent;

typedef struct __KKBkptEventStruct
{
	KKHeader header;
	TVid object;
	TVid bp;
	unsigned int instruction;
}
KKBkptEvent;

#define IsBreak(inst) (((inst) & 0xFC00003F) == 0xD)

extern u8 __rmonUtilityBuffer[256];

extern OSMesgQueue __rmonMQ;

extern u8 __rmonRcpAtBreak;

extern void __rmonSendFault(OSThread *);
extern void __rmonIOflush(void);
extern void __rmonIOputw(u32);

extern int __rmonExecute(KKHeader *);

extern void __rmonWriteWordTo(u32 *, u32);
extern u32 __rmonReadWordAt(u32 *);
extern void __rmonMemcpy(u8 *, u8 *, u32);
extern void __rmonCopyWords(u32 *, u32 *, u32);
extern int __rmonReadMem(KKHeader *);
extern int __rmonWriteMem(KKHeader *);
extern int __rmonListProcesses(KKHeader *);
extern int __rmonLoadProgram(KKHeader *);
extern int __rmonGetExeName(KKHeader *);
extern int __rmonGetRegionCount(KKHeader *);
extern int __rmonGetRegions(KKHeader *);

extern void __rmonMaskIdleThreadInts(void);
extern OSThread *__rmonGetTCB(int);
extern int __rmonStopUserThreads(int);
extern int __rmonListThreads(KKHeader *);
extern int __rmonGetThreadStatus(int, int, KKStatusEvent *);
extern int __rmonThreadStatus(KKHeader *);
extern int __rmonStopThread(KKHeader *);
extern int __rmonRunThread(KKHeader *);

extern int __rmonSetFault(KKHeader *);
extern void __rmonInit(void);
extern int __rmonSetComm(KKHeader *);

extern int __rmonGetGRegisters(KKHeader *);
extern int __rmonSetGRegisters(KKHeader *);
extern int __rmonGetFRegisters(KKHeader *);
extern int __rmonSetFRegisters(KKHeader *);
extern int __rmonGetSRegs(KKHeader *);
extern int __rmonSetSRegs(KKHeader *);
extern int __rmonGetVRegs(KKHeader *);
extern int __rmonSetVRegs(KKHeader *);
extern u32 __rmonGetRegisterContents(int, int, int);

extern int __rmonSetBreak(KKHeader *);
extern int __rmonListBreak(KKHeader *);
extern int __rmonClearBreak(KKHeader *);
extern u32 __rmonGetBranchTarget(int, int, char *);
extern int __rmonSetSingleStep(int, u32 *);
extern void __rmonGetExceptionStatus(KKStatusEvent *);
extern void __rmonHitBreak(void);
extern void __rmonHitSpBreak(void);
extern void __rmonHitCpuFault(void);

extern void __rmonSendHeader(KKHeader *const, u32, u32);
extern void __rmonSendReply(KKHeader *const, u32, u32);
extern void __rmonSendData(const char *, unsigned int);

extern int __rmonRCPrunning(void);
extern void __rmonIdleRCP(void);
extern void __rmonStepRCP(void);
extern void __rmonRunRCP(void);
