#include <sm64/types.h>
#include <sm64/segment.h>
#include <sm64/main.h>
#include <sm64/app.h>
#include <sm64/audio.h>
#include <sm64/memory.h>
#include <sm64/time.h>
#include <sm64/buffer.h>
#include <sm64/audio/g.h>

#define SC_EVENT_SP             100
#define SC_EVENT_DP             101
#define SC_EVENT_VI             102
#define SC_EVENT_GFXTASK        103
#define SC_EVENT_PRENMI         104

OSThread thread_rmon;
OSThread thread_idle;
OSThread thread_sc;
OSThread thread_app;
OSThread thread_audio;

OSMesgQueue pi_mq;
OSMesgQueue sc_mq;
OSMesgQueue sc_task_mq;
OSMesg dma_msg;
OSMesg pi_msg[32];
OSMesg si_msg;
OSMesg sc_msg[16];
OSMesg sc_task_msg[16];

OSIoMesg dma_mb;
OSMesg null_msg;
OSMesgQueue dma_mq;
OSMesgQueue si_mq;

SC_CLIENT *sc_client_1 = NULL;
SC_CLIENT *sc_client_2 = NULL;
SC_TASK *sc_task    = NULL;
SC_TASK *sc_audtask = NULL;
SC_TASK *sc_gfxtask = NULL;
SC_TASK *sc_audtask_next = NULL;
SC_TASK *sc_gfxtask_next = NULL;
s8 sc_audio = TRUE;
u32 sc_vi = 0;

s8 reset_timer = 0;
s8 reset_frame = 0;

s8 debug_stage  = FALSE;
s8 debug_thread = FALSE;
s8 debug_time   = FALSE;
s8 debug_mem    = FALSE;

void debug_update(void)
{
    static u16 button_t[] =
    {
        U_JPAD,
        U_JPAD,
        D_JPAD,
        D_JPAD,
        L_JPAD,
        R_JPAD,
        L_JPAD,
        R_JPAD,
    };
    static u16 button_m[] =
    {
        D_JPAD,
        D_JPAD,
        U_JPAD,
        U_JPAD,
        L_JPAD,
        R_JPAD,
        L_JPAD,
        R_JPAD,
    };
    static s16 t = 0;
    static s16 m = 0;
    if (cont_menu->down != 0)
    {
        if (button_t[t++] == cont_menu->down)
        {
            if (t == lenof(button_t)) t = 0, debug_time ^= FALSE^TRUE;
        }
        else
        {
            t = 0;
        }
        if (button_m[m++] == cont_menu->down)
        {
            if (m == lenof(button_m)) m = 0, debug_mem ^= FALSE^TRUE;
        }
        else
        {
            m = 0;
        }
    }
}

void dummy(void)
{
#ifdef __GNUC__
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wuninitialized"
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

static void debug_entry(void)
{
}

static void debug_sc_main(void)
{
}

static void debug_sc_vi(void)
{
}

static void sc_init(void)
{
    osCreateMesgQueue(&dma_mq, &dma_msg, 1);
    osCreateMesgQueue(&si_mq, &si_msg, 1);
    osSetEventMesg(OS_EVENT_SI, &si_mq, (OSMesg)0);
    osCreateMesgQueue(&sc_task_mq, sc_task_msg, lenof(sc_task_msg));
    osCreateMesgQueue(&sc_mq, sc_msg, lenof(sc_msg));
    osViSetEvent(&sc_mq, (OSMesg)SC_EVENT_VI, 1);
    osSetEventMesg(OS_EVENT_SP, &sc_mq, (OSMesg)SC_EVENT_SP);
    osSetEventMesg(OS_EVENT_DP, &sc_mq, (OSMesg)SC_EVENT_DP);
    osSetEventMesg(OS_EVENT_PRENMI, &sc_mq, (OSMesg)SC_EVENT_PRENMI);
}

static void sc_init_mem(void)
{
    void *start = (void *)SEGMENT_MEM_START;
    void *end   = (void *)SEGMENT_MEM_END;
    mem_init(start, end);
    mem_heap = heap_init(0x4000, MEM_ALLOC_L);
}

static void thread_create(
    OSThread *t, OSId id, void (*entry)(void *), void *arg, void *sp, OSPri pri
)
{
    t->next  = NULL;
    t->queue = NULL;
    osCreateThread(t, id, entry, arg, sp, pri);
}

static void sc_event_prenmi(void)
{
    reset_timer = 1;
    reset_frame = 0;
    Na_SE_clear();
    Na_SE_lock();
    audio_fadeout(90);
}

static void sc_task_flush(void)
{
    SC_TASK *task;
    while (osRecvMesg(&sc_task_mq, (OSMesg *)&task, OS_MESG_NOBLOCK) != -1)
    {
        task->state = 0;
        switch (task->task.t.type)
        {
            case M_AUDTASK: sc_audtask_next = task; break;
            case M_GFXTASK: sc_gfxtask_next = task; break;
        }
    }
    if (sc_audtask == NULL && sc_audtask_next != NULL)
    {
        sc_audtask = sc_audtask_next;
        sc_audtask_next = NULL;
    }
    if (sc_gfxtask == NULL && sc_gfxtask_next != NULL)
    {
        sc_gfxtask = sc_gfxtask_next;
        sc_gfxtask_next = NULL;
    }
}

static void sc_task_start(int type)
{
    UNUSED int i;
    if (type == M_AUDTASK)  sc_task = sc_audtask;
    else                    sc_task = sc_gfxtask;
    osSpTaskStart(&sc_task->task);
    sc_task->state = 1;
}

static void sc_task_yield(void)
{
    if (sc_task->task.t.type == M_GFXTASK)
    {
        sc_task->state = 2;
        osSpTaskYield();
    }
}

static void sc_event_gfxtask(void)
{
    if (sc_task == NULL)
    {
        if (sc_gfxtask != NULL && sc_gfxtask->state == 0)
        {
            time_gfxrcp(TIME_GFXRCP_START);
            sc_task_start(M_GFXTASK);
        }
    }
}

static void sc_audtask_skip(void)
{
    sc_task = sc_audtask;
    sc_task->state = 1;
    osSendMesg(&sc_mq, (OSMesg)SC_EVENT_SP, OS_MESG_NOBLOCK);
}

static void sc_event_vi(void)
{
    UNUSED int i;
    debug_sc_vi();
    sc_vi++;
    if (reset_timer > 0) reset_timer++;
    sc_task_flush();
    if (sc_audtask != NULL)
    {
        if (sc_task != NULL)
        {
            sc_task_yield();
        }
        else
        {
            time_audrcp();
            if (sc_audio)   sc_task_start(M_AUDTASK);
            else            sc_audtask_skip();
        }
    }
    else if (sc_task == NULL)
    {
        if (sc_gfxtask != NULL && sc_gfxtask->state != 3)
        {
            time_gfxrcp(TIME_GFXRCP_START);
            sc_task_start(M_GFXTASK);
        }
    }
    if (sc_client_1 != NULL)
    {
        osSendMesg(sc_client_1->mq, sc_client_1->msg, OS_MESG_NOBLOCK);
    }
    if (sc_client_2 != NULL)
    {
        osSendMesg(sc_client_2->mq, sc_client_2->msg, OS_MESG_NOBLOCK);
    }
}

static void sc_event_sp(void)
{
    SC_TASK *task = sc_task;
    sc_task = NULL;
    if (task->state == 2)
    {
        if (!osSpTaskYielded(&task->task))
        {
            task->state = 3;
            time_gfxrcp(TIME_GFXRCP_ENDRSP);
        }
        time_audrcp();
        if (sc_audio)   sc_task_start(M_AUDTASK);
        else            sc_audtask_skip();
    }
    else
    {
        task->state = 3;
        if (task->task.t.type == M_AUDTASK)
        {
            time_audrcp();
            if (sc_gfxtask != NULL && sc_gfxtask->state != 3)
            {
                if (sc_gfxtask->state != 2) time_gfxrcp(TIME_GFXRCP_START);
                sc_task_start(M_GFXTASK);
            }
            sc_audtask = NULL;
            if (task->mq != NULL)
            {
                osSendMesg(task->mq, task->msg, OS_MESG_NOBLOCK);
            }
        }
        else
        {
            time_gfxrcp(TIME_GFXRCP_ENDRSP);
        }
    }
}

static void sc_event_dp(void)
{
    if (sc_gfxtask->mq != NULL)
    {
        osSendMesg(sc_gfxtask->mq, sc_gfxtask->msg, OS_MESG_NOBLOCK);
    }
    time_gfxrcp(TIME_GFXRCP_ENDRDP);
    sc_gfxtask->state = 4;
    sc_gfxtask = NULL;
}

static void sc_main(UNUSED void *arg)
{
    sc_init();
    sc_init_mem();
    mem_load_lib();
    thread_create(
        &thread_audio, 4, audio_main, NULL, stack_audio+lenof(stack_audio), 20
    );
    osStartThread(&thread_audio);
    thread_create(
        &thread_app, 5, app_main, NULL, stack_app+lenof(stack_app), 10
    );
    osStartThread(&thread_app);
    for (;;)
    {
        OSMesg msg;
        osRecvMesg(&sc_mq, &msg, OS_MESG_BLOCK);
        switch ((int)msg)
        {
            case SC_EVENT_VI:       sc_event_vi();      break;
            case SC_EVENT_SP:       sc_event_sp();      break;
            case SC_EVENT_DP:       sc_event_dp();      break;
            case SC_EVENT_GFXTASK:  sc_event_gfxtask(); break;
            case SC_EVENT_PRENMI:   sc_event_prenmi();  break;
        }
        debug_sc_main();
    }
}

void sc_client_init(int i, SC_CLIENT *client, OSMesgQueue *mq, OSMesg msg)
{
    client->mq  = mq;
    client->msg = msg;
    switch (i)
    {
        case 1: sc_client_1 = client; break;
        case 2: sc_client_2 = client; break;
    }
}

void sc_queue_task(SC_TASK *task)
{
    osWritebackDCacheAll();
    osSendMesg(&sc_task_mq, task, OS_MESG_NOBLOCK);
}

void sc_queue_audtask(SC_TASK *task)
{
    if (sc_audio)
    {
        if (task != NULL)
        {
            osWritebackDCacheAll();
            osSendMesg(&sc_task_mq, task, OS_MESG_NOBLOCK);
        }
    }
}

void sc_queue_gfxtask(SC_TASK *task)
{
    if (task != NULL)
    {
        osWritebackDCacheAll();
        task->state = 0;
        if (sc_gfxtask == NULL)
        {
            sc_gfxtask = task;
            sc_gfxtask_next = NULL;
            osSendMesg(&sc_mq, (OSMesg)SC_EVENT_GFXTASK, OS_MESG_NOBLOCK);
        }
        else
        {
            sc_gfxtask_next = task;
        }
    }
}

void sc_audio_enable(void)
{
    sc_audio = TRUE;
}

void sc_audio_disable(void)
{
    sc_audio = FALSE;
    while (sc_audtask != NULL);
}

static void idle_main(UNUSED void *arg)
{
#ifndef VERSION_J00
    int tv_type = osTvType;
#endif
    osCreateViManager(OS_PRIORITY_VIMGR);
#ifndef VERSION_J00
    if (tv_type == OS_TV_NTSC)  osViSetMode(&osViModeTable[OS_VI_NTSC_LAN1]);
    else                        osViSetMode(&osViModeTable[OS_VI_PAL_LAN1]);
#else
    osViSetMode(&osViModeTable[OS_VI_NTSC_LAN1]);
#endif
    osViBlack(TRUE);
    osViSetSpecialFeatures(OS_VI_DITHER_FILTER_ON);
    osViSetSpecialFeatures(OS_VI_GAMMA_OFF);
    osCreatePiManager(OS_PRIORITY_PIMGR, &pi_mq, pi_msg, lenof(pi_msg));
    thread_create(&thread_sc, 3, sc_main, NULL, stack_sc+lenof(stack_sc), 100);
    if (!debug_thread) osStartThread(&thread_sc);
    osSetThreadPri(NULL, OS_PRIORITY_IDLE);
    for (;;);
}

void entry(void)
{
    UNUSED char buf[64];
    osInitialize();
    debug_entry();
    thread_create(
        &thread_idle, 1, idle_main, NULL, stack_idle+lenof(stack_idle), 100
    );
    osStartThread(&thread_idle);
}
