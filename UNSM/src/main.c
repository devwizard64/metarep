#include <sm64.h>

#define SC_EVENT_SP             100
#define SC_EVENT_DP             101
#define SC_EVENT_VI             102
#define SC_EVENT_GFXTASK        103
#define SC_EVENT_PRENMI         104

#define SC_WAITING              0
#define SC_RUNNING              1
#define SC_YIELDED              2
#define SC_RSPDONE              3
#define SC_RDPDONE              4

extern long long entry_stack[BOOT_STACK_LEN];
extern long long idle_stack[IDLE_STACK_LEN];
extern long long sched_stack[MAIN_STACK_LEN];
extern long long aud_stack[MAIN_STACK_LEN];
extern long long gfx_stack[MAIN_STACK_LEN];

UNUSED static OSThread rmon_thread;
static OSThread idle_thread;
static OSThread sched_thread;
static OSThread gfx_thread;
static OSThread aud_thread;

static OSMesgQueue pi_mq;
static OSMesgQueue sched_mq;
static OSMesgQueue sctask_mq;

static OSMesg dma_mbox;
static OSMesg pi_mbox[32];
static OSMesg si_mbox;
static OSMesg sched_mbox[16];
static OSMesg sctask_mbox[16];

static SCCLIENT *sc_audclient = NULL;
static SCCLIENT *sc_gfxclient = NULL;
static SCTASK *sc_task    = NULL;
static SCTASK *sc_audtask = NULL;
static SCTASK *sc_gfxtask = NULL;
static SCTASK *sc_audtask_next = NULL;
static SCTASK *sc_gfxtask_next = NULL;
static char sc_aud = TRUE;

OSIoMesg dma_mb;
OSMesg null_msg;
OSMesgQueue dma_mq;
OSMesgQueue si_mq;

u32 vi_count = 0;

char reset_timer = 0;
char reset_frame = 0;

#ifdef GATEWAY
char sys_halt = FALSE;
#endif

char debug_stage  = FALSE;
char debug_thread = FALSE;
char debug_time   = FALSE;
char debug_info   = FALSE;

void DebugCheck(void)
{
	static u16 timeseq[] =
		{U_JPAD, U_JPAD, D_JPAD, D_JPAD, L_JPAD, R_JPAD, L_JPAD, R_JPAD};
	static u16 infoseq[] =
		{D_JPAD, D_JPAD, U_JPAD, U_JPAD, L_JPAD, R_JPAD, L_JPAD, R_JPAD};
	static short timeidx = 0;
	static short infoidx = 0;
	if (contp->down != 0)
	{
		if (timeseq[timeidx++] == contp->down)
		{
			if (timeidx == 8) timeidx = 0, debug_time ^= TRUE;
		}
		else
		{
			timeidx = 0;
		}
		if (infoseq[infoidx++] == contp->down)
		{
			if (infoidx == 8) infoidx = 0, debug_info ^= TRUE;
		}
		else
		{
			infoidx = 0;
		}
	}
}

void dummy(void)
{
#ifdef __GNUC__
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wuninitialized"
#pragma GCC diagnostic ignored "-Wnonnull"
#pragma GCC diagnostic ignored "-Wformat-overflow"
#endif
	OSTime time;
	OSPageMask pm;
	osSetTime(time);
	osMapTLB(0, pm, NULL, 0, 0, 0);
	osUnmapTLBAll();
	sprintf(NULL, NULL);
#ifdef __GNUC__
#pragma GCC diagnostic pop
#endif
}

static void DebugEntry(void)
{
}

static void DebugSchedProc(void)
{
}

static void DebugSchedVI(void)
{
}

static void ScInit(void)
{
	osCreateMesgQueue(&dma_mq, &dma_mbox, 1);
	osCreateMesgQueue(&si_mq, &si_mbox, 1);
	osSetEventMesg(OS_EVENT_SI, &si_mq, (OSMesg)0);
	osCreateMesgQueue(&sctask_mq, sctask_mbox, 16);
	osCreateMesgQueue(&sched_mq, sched_mbox, 16);
	osViSetEvent(&sched_mq, (OSMesg)SC_EVENT_VI, 1);
	osSetEventMesg(OS_EVENT_SP, &sched_mq, (OSMesg)SC_EVENT_SP);
	osSetEventMesg(OS_EVENT_DP, &sched_mq, (OSMesg)SC_EVENT_DP);
	osSetEventMesg(OS_EVENT_PRENMI, &sched_mq, (OSMesg)SC_EVENT_PRENMI);
}

static void ScInitMem(void)
{
	void *start = (void *)ADDRESS_MEM_START;
	void *end   = (void *)ADDRESS_MEM_END;
	MemInit(start, end);
	mem_heap = HeapCreate(16384, MEM_ALLOC_L);
}

static void CreateThread(
	OSThread *t, OSId id, void (*entry)(void *), void *arg, void *sp, OSPri pri
)
{
	t->next  = NULL;
	t->queue = NULL;
	osCreateThread(t, id, entry, arg, sp, pri);
}

static void ScEventPreNMI(void)
{
	reset_timer = 1;
	reset_frame = 0;
	Na_SeClear();
	Na_LockSe();
	AudFadeout(90);
#if REVISION >= 199707
	Na_J3_802F69CC();
#endif
}

static void ScTaskFlush(void)
{
	SCTASK *task;
	while (osRecvMesg(&sctask_mq, (OSMesg *)&task, OS_MESG_NOBLOCK) != -1)
	{
		task->status = SC_WAITING;
		switch (task->task.t.type)
		{
		case M_AUDTASK: sc_audtask_next = task; break;
		case M_GFXTASK: sc_gfxtask_next = task; break;
		}
	}
	if (!sc_audtask && sc_audtask_next)
	{
		sc_audtask = sc_audtask_next;
		sc_audtask_next = NULL;
	}
	if (!sc_gfxtask && sc_gfxtask_next)
	{
		sc_gfxtask = sc_gfxtask_next;
		sc_gfxtask_next = NULL;
	}
}

static void ScTaskStart(int type)
{
	UNUSED int i;
	if (type == M_AUDTASK)  sc_task = sc_audtask;
	else                    sc_task = sc_gfxtask;
	osSpTaskStart(&sc_task->task);
	sc_task->status = SC_RUNNING;
}

static void ScTaskYield(void)
{
	if (sc_task->task.t.type == M_GFXTASK)
	{
		sc_task->status = SC_YIELDED;
		osSpTaskYield();
	}
}

static void ScEventGfxTask(void)
{
	if (!sc_task)
	{
		if (sc_gfxtask && sc_gfxtask->status == SC_WAITING)
		{
			TimeGfxRCP(TIME_GFXRCP_START);
			ScTaskStart(M_GFXTASK);
		}
	}
}

static void ScSkipAudTask(void)
{
	sc_task = sc_audtask;
	sc_task->status = SC_RUNNING;
	osSendMesg(&sched_mq, (OSMesg)SC_EVENT_SP, OS_MESG_NOBLOCK);
}

static void ScEventVI(void)
{
	UNUSED int i;
	DebugSchedVI();
	vi_count++;
#if REVISION >= 199707
	if (reset_timer > 0 && reset_timer < 100) reset_timer++;
#else
	if (reset_timer > 0) reset_timer++;
#endif
	ScTaskFlush();
	if (sc_audtask)
	{
		if (sc_task)
		{
			ScTaskYield();
		}
		else
		{
			TimeAudRCP();
			if (sc_aud) ScTaskStart(M_AUDTASK);
			else        ScSkipAudTask();
		}
	}
	else if (!sc_task)
	{
		if (sc_gfxtask && sc_gfxtask->status != SC_RSPDONE)
		{
			TimeGfxRCP(TIME_GFXRCP_START);
			ScTaskStart(M_GFXTASK);
		}
	}
#ifdef MOTOR
	motor_8024CC7C();
#endif
#ifdef GATEWAY
	if (sc_audclient && !sys_halt)
#else
	if (sc_audclient)
#endif
	{
		osSendMesg(sc_audclient->mq, sc_audclient->msg, OS_MESG_NOBLOCK);
	}
	if (sc_gfxclient)
	{
		osSendMesg(sc_gfxclient->mq, sc_gfxclient->msg, OS_MESG_NOBLOCK);
	}
}

static void ScEventSP(void)
{
	SCTASK *task = sc_task;
	sc_task = NULL;
	if (task->status == SC_YIELDED)
	{
		if (!osSpTaskYielded(&task->task))
		{
			task->status = SC_RSPDONE;
			TimeGfxRCP(TIME_GFXRCP_ENDRSP);
		}
		TimeAudRCP();
		if (sc_aud) ScTaskStart(M_AUDTASK);
		else        ScSkipAudTask();
	}
	else
	{
		task->status = SC_RSPDONE;
		if (task->task.t.type == M_AUDTASK)
		{
			TimeAudRCP();
			if (sc_gfxtask && sc_gfxtask->status != SC_RSPDONE)
			{
				if (sc_gfxtask->status != SC_YIELDED)
				{
					TimeGfxRCP(TIME_GFXRCP_START);
				}
				ScTaskStart(M_GFXTASK);
			}
			sc_audtask = NULL;
			if (task->mq) osSendMesg(task->mq, task->msg, OS_MESG_NOBLOCK);
		}
		else
		{
			TimeGfxRCP(TIME_GFXRCP_ENDRSP);
		}
	}
}

static void ScEventDP(void)
{
	if (sc_gfxtask->mq)
	{
		osSendMesg(sc_gfxtask->mq, sc_gfxtask->msg, OS_MESG_NOBLOCK);
	}
	TimeGfxRCP(TIME_GFXRCP_ENDRDP);
	sc_gfxtask->status = SC_RDPDONE;
	sc_gfxtask = NULL;
}

static void SchedProc(UNUSED void *arg)
{
	ScInit();
	ScInitMem();
	MemLoadULib();
	CreateThread(&aud_thread, 4, AudProc, NULL, aud_stack+MAIN_STACK_LEN, 20);
	osStartThread(&aud_thread);
	CreateThread(&gfx_thread, 5, GfxProc, NULL, gfx_stack+MAIN_STACK_LEN, 10);
	osStartThread(&gfx_thread);
	for (;;)
	{
		OSMesg msg;
		osRecvMesg(&sched_mq, &msg, OS_MESG_BLOCK);
		switch ((int)msg)
		{
		case SC_EVENT_VI:       ScEventVI();        break;
		case SC_EVENT_SP:       ScEventSP();        break;
		case SC_EVENT_DP:       ScEventDP();        break;
		case SC_EVENT_GFXTASK:  ScEventGfxTask();   break;
		case SC_EVENT_PRENMI:   ScEventPreNMI();    break;
		}
		DebugSchedProc();
	}
}

void ScSetClient(int i, SCCLIENT *client, OSMesgQueue *mq, OSMesg msg)
{
	client->mq  = mq;
	client->msg = msg;
	switch (i)
	{
	case SC_AUDCLIENT: sc_audclient = client; break;
	case SC_GFXCLIENT: sc_gfxclient = client; break;
	}
}

void ScQueueTask(SCTASK *task)
{
	osWritebackDCacheAll();
	osSendMesg(&sctask_mq, task, OS_MESG_NOBLOCK);
}

void ScQueueAudTask(SCTASK *task)
{
	if (sc_aud)
	{
		if (task)
		{
			osWritebackDCacheAll();
			osSendMesg(&sctask_mq, task, OS_MESG_NOBLOCK);
		}
	}
}

void ScQueueGfxTask(SCTASK *task)
{
	if (task)
	{
		osWritebackDCacheAll();
		task->status = SC_WAITING;
		if (!sc_gfxtask)
		{
			sc_gfxtask = task;
			sc_gfxtask_next = NULL;
			osSendMesg(&sched_mq, (OSMesg)SC_EVENT_GFXTASK, OS_MESG_NOBLOCK);
		}
		else
		{
			sc_gfxtask_next = task;
		}
	}
}

void ScAudEnable(void)
{
	sc_aud = TRUE;
}

void ScAudDisable(void)
{
	sc_aud = FALSE;
	while (sc_audtask);
}

static void IdleProc(UNUSED void *arg)
{
#if REVISION >= 199609 && REVISION != 199703
	int tv_type = osTvType;
#endif
	osCreateViManager(OS_PRIORITY_VIMGR);
#ifdef PAL
	osViSetMode(&osViModeTable[OS_VI_PAL_LAN1]);
#elif REVISION >= 199609
	if (tv_type == OS_TV_NTSC)  osViSetMode(&osViModeTable[OS_VI_NTSC_LAN1]);
	else                        osViSetMode(&osViModeTable[OS_VI_PAL_LAN1]);
#else
	osViSetMode(&osViModeTable[OS_VI_NTSC_LAN1]);
#endif
	osViBlack(TRUE);
	osViSetSpecialFeatures(OS_VI_DITHER_FILTER_ON);
	osViSetSpecialFeatures(OS_VI_GAMMA_OFF);
	osCreatePiManager(OS_PRIORITY_PIMGR, &pi_mq, pi_mbox, 32);
#ifdef DISK
	DiskInit();
#endif
	CreateThread(
		&sched_thread, 3, SchedProc, NULL, sched_stack+MAIN_STACK_LEN, 100
	);
	if (!debug_thread) osStartThread(&sched_thread);
	osSetThreadPri(NULL, OS_PRIORITY_IDLE);
	for (;;);
}

void entry(void)
{
	UNUSED char buf[64];
	osInitialize();
	DebugEntry();
	CreateThread(
		&idle_thread, 1, IdleProc, NULL, idle_stack+IDLE_STACK_LEN, 100
	);
	osStartThread(&idle_thread);
}
