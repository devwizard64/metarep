#include <sm64/types.h>
#include <sm64/segment.h>
#include <sm64/main.h>
#include <sm64/app.h>
#include <sm64/audio.h>
#include <sm64/mem.h>
#include <sm64/save.h>
#include <sm64/time.h>
#include <sm64/dprint.h>
#include <sm64/p_script.h>
#include <sm64/zimg.h>
#include <sm64/buffer.h>
#include <sm64/fifo.h>
#include <sm64/cimg.h>
#include <sm64/audio/g.h>

#define CONTROLLER_LEN  2

CONTROLLER   controller_table[CONTROLLER_LEN+1];
OSContStatus contstatus_table[MAXCONTROLLERS];
OSContPad    contpad_table[MAXCONTROLLERS];

OSMesgQueue mq_video_vi;
OSMesgQueue mq_video_dp;
OSMesg msg_video_vi;
OSMesg msg_video_dp;
SC_CLIENT sc_client_video;

uintptr_t video_cimg[3];
uintptr_t video_zimg;
u8      *anime_mario_buffer;
u8      *demo_buffer;
SC_TASK *video_task;
Gfx     *video_gfx;
u8      *video_mem;
VIDEO   *video;

u8 input_flag;
s8 eeprom_status;

FILE file_anime_mario;
FILE file_demo;

u32 app_8032D5D0 = 0;
u32 video_frame = 0;
u16 video_vi = 0;
u16 video_dp = 0;
void (*video_callback)(void) = NULL;

CONTROLLER *controller_1    = &controller_table[0];
CONTROLLER *controller_2    = &controller_table[1];
CONTROLLER *controller_menu = &controller_table[2];

DEMO *demo = NULL;
u16   demo_index = 0;

static void video_init_dp(void)
{
    gDPPipeSync(video_gfx++);
    gDPPipelineMode(video_gfx++, G_PM_1PRIMITIVE);
    gDPSetScissor(video_gfx++, G_SC_NON_INTERLACE, 0, 0, SCREEN_WD, SCREEN_HT);
    gDPSetCombineMode(video_gfx++, G_CC_SHADE, G_CC_SHADE);
    gDPSetTextureLOD(video_gfx++, G_TL_TILE);
    gDPSetTextureLUT(video_gfx++, G_TT_NONE);
    gDPSetTextureDetail(video_gfx++, G_TD_CLAMP);
    gDPSetTexturePersp(video_gfx++, G_TP_PERSP);
    gDPSetTextureFilter(video_gfx++, G_TF_BILERP);
    gDPSetTextureConvert(video_gfx++, G_TC_FILT);
    gDPSetCombineKey(video_gfx++, G_CK_NONE);
    gDPSetAlphaCompare(video_gfx++, G_AC_NONE);
    gDPSetRenderMode(video_gfx++, G_RM_OPA_SURF, G_RM_OPA_SURF2);
    gDPSetColorDither(video_gfx++, G_CD_MAGICSQ);
    gDPSetCycleType(video_gfx++, G_CYC_FILL);
    gDPPipeSync(video_gfx++);
}

static void video_init_sp(void)
{
    gSPClearGeometryMode(
        video_gfx++,
        G_SHADE | G_SHADING_SMOOTH | G_CULL_BOTH | G_FOG | G_LIGHTING |
        G_TEXTURE_GEN | G_TEXTURE_GEN_LINEAR | G_LOD
    );
    gSPSetGeometryMode(
        video_gfx++, G_SHADE | G_SHADING_SMOOTH | G_CULL_BACK | G_LIGHTING
    );
    gSPNumLights(video_gfx++, NUMLIGHTS_1);
    gSPTexture(video_gfx++, 0x0000, 0x0000, G_TX_NOLOD, G_TX_RENDERTILE, G_OFF);
}

static void video_init_zimg(void)
{
    gDPPipeSync(video_gfx++);
    gDPSetDepthSource(video_gfx++, G_ZS_PIXEL);
    gDPSetDepthImage(video_gfx++, video_zimg);
    gDPSetColorImage(
        video_gfx++, G_IM_FMT_RGBA, G_IM_SIZ_16b, SCREEN_WD, video_zimg
    );
    gDPSetFillColor(video_gfx++, 0x00010001U*GPACK_ZDZ(G_MAXFBZ, 0));
    gDPFillRectangle(
        video_gfx++, 0, BORDER_HT, SCREEN_WD-1, SCREEN_HT-BORDER_HT-1
    );
}

static void video_init_cimg(void)
{
    gDPPipeSync(video_gfx++);
    gDPSetCycleType(video_gfx++, G_CYC_1CYCLE);
    gDPSetColorImage(
        video_gfx++, G_IM_FMT_RGBA, G_IM_SIZ_16b, SCREEN_WD,
        video_cimg[video_dp]
    );
#if BORDER_HT > 0
    gDPSetScissor(
        video_gfx++, G_SC_NON_INTERLACE,
        0, BORDER_HT, SCREEN_WD, SCREEN_HT-BORDER_HT
    );
#endif
}

void video_clear(u32 fill)
{
    gDPPipeSync(video_gfx++);
    gDPSetRenderMode(video_gfx++, G_RM_OPA_SURF, G_RM_OPA_SURF2);
    gDPSetCycleType(video_gfx++, G_CYC_FILL);
    gDPSetFillColor(video_gfx++, fill);
    gDPFillRectangle(
        video_gfx++, 0, BORDER_HT, SCREEN_WD-1, SCREEN_HT-BORDER_HT-1
    );
    gDPPipeSync(video_gfx++);
    gDPSetCycleType(video_gfx++, G_CYC_1CYCLE);
}

void video_vp_clear(const Vp *vp, u32 fill)
{
    s16 ulx = (vp->vp.vtrans[0]-vp->vp.vscale[0])/4 + 1;
    s16 uly = (vp->vp.vtrans[1]-vp->vp.vscale[1])/4 + 1;
    s16 lrx = (vp->vp.vtrans[0]+vp->vp.vscale[0])/4 - 1 - 1;
    s16 lry = (vp->vp.vtrans[1]+vp->vp.vscale[1])/4 - 1 - 1;
    gDPPipeSync(video_gfx++);
    gDPSetRenderMode(video_gfx++, G_RM_OPA_SURF, G_RM_OPA_SURF2);
    gDPSetCycleType(video_gfx++, G_CYC_FILL);
    gDPSetFillColor(video_gfx++, fill);
    gDPFillRectangle(video_gfx++, ulx, uly, lrx, lry);
    gDPPipeSync(video_gfx++);
    gDPSetCycleType(video_gfx++, G_CYC_1CYCLE);
}

static void video_draw_border(void)
{
    gDPPipeSync(video_gfx++);
    gDPSetScissor(video_gfx++, G_SC_NON_INTERLACE, 0, 0, SCREEN_WD, SCREEN_HT);
    gDPSetRenderMode(video_gfx++, G_RM_OPA_SURF, G_RM_OPA_SURF2);
    gDPSetCycleType(video_gfx++, G_CYC_FILL);
#if BORDER_HT > 0
    gDPSetFillColor(video_gfx++, 0x00000000);
    gDPFillRectangle(video_gfx++, 0, 0, SCREEN_WD-1, BORDER_HT-1);
    gDPFillRectangle(
        video_gfx++, 0, SCREEN_HT-BORDER_HT, SCREEN_WD-1, SCREEN_HT-1
    );
#endif
}

void video_vp_scissor(const Vp *vp)
{
    s16 ulx = (vp->vp.vtrans[0]-vp->vp.vscale[0])/4 + 1;
    s16 uly = (vp->vp.vtrans[1]-vp->vp.vscale[1])/4 + 1;
    s16 lrx = (vp->vp.vtrans[0]+vp->vp.vscale[0])/4 - 1;
    s16 lry = (vp->vp.vtrans[1]+vp->vp.vscale[1])/4 - 1;
    gDPSetScissor(video_gfx++, G_SC_NON_INTERLACE, ulx, uly, lrx, lry);
}

static void video_init_task(void)
{
    size_t len = video_gfx - video->gfx;
    video_task->mq = &mq_video_dp;
    video_task->msg = (OSMesg)2;
    video_task->task.t.type = M_GFXTASK;
    video_task->task.t.ucode_boot = rspbootTextStart;
    video_task->task.t.ucode_boot_size =
        (u8 *)rspbootTextEnd - (u8 *)rspbootTextStart;
    video_task->task.t.flags = 0;
    video_task->task.t.ucode = gspFast3D_fifoTextStart;
    video_task->task.t.ucode_data = gspFast3D_fifoDataStart;
    video_task->task.t.ucode_size = SP_UCODE_SIZE;
    video_task->task.t.ucode_data_size = SP_UCODE_DATA_SIZE;
    video_task->task.t.dram_stack = video_stack;
    video_task->task.t.dram_stack_size = sizeof(video_stack);
    video_task->task.t.output_buff = fifo_buffer;
    video_task->task.t.output_buff_size = fifo_buffer + lenof(fifo_buffer);
    video_task->task.t.data_ptr = (u64 *)video->gfx;
    video_task->task.t.data_size = sizeof(Gfx)*len;
    video_task->task.t.yield_data_ptr = video_yield;
    video_task->task.t.yield_data_size = sizeof(video_yield);
}

void video_draw_start(void)
{
    segment_write();
    video_init_dp();
    video_init_sp();
    video_init_zimg();
    video_init_cimg();
}

void video_draw_end(void)
{
    video_draw_border();
    if (debug_time) time_draw();
    gDPFullSync(video_gfx++);
    gSPEndDisplayList(video_gfx++);
    video_init_task();
}

static void video_draw_reset(void)
{
    if (reset_timer != 0 && reset_frame < 15)
    {
        int y;
        int x;
        int vi = video_vi == 0 ? 2 : video_vi-1;
        u64 *cimg = (void *)PHYS_TO_K0(video_cimg[vi]);
        cimg += SCREEN_WD/4 * reset_frame++;
        for (y = 0; y < 16; y++)
        {
            for (x = 0; x < SCREEN_WD/4; x++) *cimg++ = 0;
            cimg += SCREEN_WD/4 * (SCREEN_HT/16-1);
        }
    }
    osWritebackDCacheAll();
    osRecvMesg(&mq_video_vi, &msg_null, OS_MESG_BLOCK);
    osRecvMesg(&mq_video_vi, &msg_null, OS_MESG_BLOCK);
}

static void video_init(void)
{
    video = &video_table[0];
    segment_set(SEGMENT_VIDEO >> 24, video);
    video_task = &video->task;
    video_gfx = video->gfx;
    video_mem = (u8 *)video->gfx + sizeof(video->gfx);
    video_draw_start();
    video_clear(0x00000000);
    video_draw_end();
    sc_queue_gfxtask(&video->task);
    video_dp++;
    video_frame++;
}

static void video_start(void)
{
    video = &video_table[video_frame & 1];
    segment_set(SEGMENT_VIDEO >> 24, video);
    video_task = &video->task;
    video_gfx = video->gfx;
    video_mem = (u8 *)video->gfx + sizeof(video->gfx);
}

static void video_end(void)
{
    time_8027E3E0(2);
    osRecvMesg(&mq_video_dp, &msg_null, OS_MESG_BLOCK);
    if (video_callback != NULL)
    {
        video_callback();
        video_callback = NULL;
    }
    sc_queue_gfxtask(&video->task);
    time_8027E3E0(3);
    osRecvMesg(&mq_video_vi, &msg_null, OS_MESG_BLOCK);
    osViSwapBuffer((void *)PHYS_TO_K0(video_cimg[video_vi]));
    time_8027E3E0(4);
    osRecvMesg(&mq_video_vi, &msg_null, OS_MESG_BLOCK);
    if (++video_vi == 3) video_vi = 0;
    if (++video_dp == 3) video_dp = 0;
    video_frame++;
}

unused static void demo_record(void)
{
    static DEMO record = {0};
    u8 button =
        (controller_1->held & 0xF000) >> 8 | (controller_1->held & 0x000F);
    s8 stick_x = controller_1->stick_x;
    s8 stick_y = controller_1->stick_y;
    if (stick_x > -8 && stick_x < 8) stick_x = 0;
    if (stick_y > -8 && stick_y < 8) stick_y = 0;
    if
    (
        record.count == 0xFF ||
        button  != record.button  ||
        stick_x != record.stick_x ||
        stick_y != record.stick_y
    )
    {
        /*
        printf(
            "    .byte %3d, %3d, %3d, 0x%02X\n",
            record.count, record.stick_x, record.stick_y, record.button
        );
        */
        record.count   = 0;
        record.button  = button;
        record.stick_x = stick_x;
        record.stick_y = stick_y;
    }
    record.count++;
}

static void input_update_stick(CONTROLLER *cont)
{
    unused int i;
    cont->x = 0;
    cont->y = 0;
    if (cont->stick_x <= -8) cont->x = cont->stick_x + 6;
    if (cont->stick_x >=  8) cont->x = cont->stick_x - 6;
    if (cont->stick_y <= -8) cont->y = cont->stick_y + 6;
    if (cont->stick_y >=  8) cont->y = cont->stick_y - 6;
    cont->d = sqrtf(cont->x*cont->x + cont->y*cont->y);
    if (cont->d > 64)
    {
        cont->x *= 64/cont->d;
        cont->y *= 64/cont->d;
        cont->d  = 64;
    }
}

static void demo_update(void)
{
    controller_table[0].pad->button &= 0xFF3F;
    if (demo != NULL)
    {
        if (controller_table[1].pad != NULL)
        {
            controller_table[1].pad->stick_x = 0;
            controller_table[1].pad->stick_y = 0;
            controller_table[1].pad->button  = 0;
        }
        if (demo->count == 0)
        {
            controller_table[0].pad->stick_x = 0;
            controller_table[0].pad->stick_y = 0;
            controller_table[0].pad->button  = 0x0080;
        }
        else
        {
            u16 start = controller_table[0].pad->button & START_BUTTON;
            controller_table[0].pad->stick_x = demo->stick_x;
            controller_table[0].pad->stick_y = demo->stick_y;
            controller_table[0].pad->button =
                ((demo->button & 0xF0) << 8) + (demo->button & 0x0F);
            controller_table[0].pad->button |= start;
            if (--demo->count == 0) demo++;
        }
    }
}

static void input_update(void)
{
    int i;
    if (input_flag != 0)
    {
        osRecvMesg(&mq_si, &msg_null, OS_MESG_BLOCK);
        osContGetReadData(contpad_table);
    }
    demo_update();
    for (i = 0; i < CONTROLLER_LEN; i++)
    {
        CONTROLLER *cont = &controller_table[i];
        if (cont->pad != NULL)
        {
            cont->stick_x = cont->pad->stick_x;
            cont->stick_y = cont->pad->stick_y;
            cont->down    = cont->pad->button & (cont->pad->button^cont->held);
            cont->held    = cont->pad->button;
            input_update_stick(cont);
        }
        else
        {
            cont->stick_x = 0;
            cont->stick_y = 0;
            cont->down    = 0;
            cont->held    = 0;
            cont->x       = 0;
            cont->y       = 0;
            cont->d       = 0;
        }
    }
    controller_menu->stick_x = controller_1->stick_x;
    controller_menu->stick_y = controller_1->stick_y;
    controller_menu->x       = controller_1->x;
    controller_menu->y       = controller_1->y;
    controller_menu->d       = controller_1->d;
    controller_menu->down    = controller_1->down;
    controller_menu->held    = controller_1->held;
}

static void input_init(void)
{
    s16 i;
    s16 c;
    controller_table[0].status = &contstatus_table[0];
    controller_table[0].pad    = &contpad_table[0];
    osContInit(&mq_si, &input_flag, contstatus_table);
    eeprom_status = osEepromProbe(&mq_si);
    for (c = 0, i = 0; i < MAXCONTROLLERS && c < CONTROLLER_LEN; i++)
    {
        if (input_flag & (1 << i))
        {
            controller_table[c  ].status = &contstatus_table[i];
            controller_table[c++].pad    = &contpad_table[i];
        }
    }
}

extern u8 _main_dataSegmentRomStart[];
extern u8 _main_dataSegmentRomEnd[];
extern u8 _main_szpSegmentRomStart[];
extern u8 _main_szpSegmentRomEnd[];
extern u8 _animeSegmentRomStart[];
extern u8 _demoSegmentRomStart[];

static void app_init(void)
{
    unused int i;
    segment_set(0x00, (void *)0x80000000);
    osCreateMesgQueue(&mq_video_dp, &msg_video_dp, 1);
    osCreateMesgQueue(&mq_video_vi, &msg_video_vi, 1);
    video_zimg    = K0_TO_PHYS(depth_buffer);
    video_cimg[0] = K0_TO_PHYS(colour_buffer_a);
    video_cimg[1] = K0_TO_PHYS(colour_buffer_b);
    video_cimg[2] = K0_TO_PHYS(colour_buffer_c);
    anime_mario_buffer = mem_alloc(0x4000, MEM_ALLOC_L);
    segment_set(SEGMENT_ANIME_MARIO >> 24, anime_mario_buffer);
    file_init(&file_anime_mario, _animeSegmentRomStart, anime_mario_buffer);
    demo_buffer = mem_alloc(0x800, MEM_ALLOC_L);
    segment_set(SEGMENT_DEMO >> 24, demo_buffer);
    file_init(&file_demo, _demoSegmentRomStart, demo_buffer);
    mem_load_data(
        SEGMENT_DATA_MAIN >> 24,
        _main_dataSegmentRomStart,
        _main_dataSegmentRomEnd,
        MEM_ALLOC_L
    );
    mem_load_szp(
        SEGMENT_SZP_MAIN >> 24,
        _main_szpSegmentRomStart,
        _main_szpSegmentRomEnd
    );
}

extern P_SCRIPT p_main[];

void app_main(unused void *arg)
{
    P_SCRIPT *pc;
    app_init();
    input_init();
    save_802799DC();
    sc_client_init(2, &sc_client_video, &mq_video_vi, (OSMesg)1);
    pc = segment_to_virtual(p_main);
    Na_BGM_play(2, 0, 0);
    audio_output(save_8027A5B4());
    video_init();
    while (true)
    {
        if (reset_timer != 0)
        {
            video_draw_reset();
            continue;
        }
        time_8027E3E0(0);
        if (input_flag != 0) osContStartReadData(&mq_si);
        audio_update();
        video_start();
        input_update();
        pc = p_script_main(pc);
        video_end();
        if (debug_mem) dprintf(180, 20, "BUF %d", video_mem-(u8 *)video_gfx);
    }
}
