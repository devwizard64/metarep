#include <sm64.h>

CONTROLLER   controller_data[CONTROLLER_LEN+1];
OSContStatus cont_status[MAXCONTROLLERS];
OSContPad    cont_pad[MAXCONTROLLERS];

OSMesgQueue gfx_vi_mq;
OSMesgQueue gfx_dp_mq;
OSMesg gfx_vi_mbox;
OSMesg gfx_dp_mbox;
SC_CLIENT sc_client_gfx;

uintptr_t gfx_cimg[3];
uintptr_t gfx_zimg;
void    *anime_mario_buf;
void    *demo_buf;
SC_TASK *gfx_task;
Gfx     *gfx_ptr;
char    *gfx_mem;
FRAME   *frame;

u8 cont_bitpattern;
s8 eeprom_status;

BANK anime_mario_bank;
BANK demo_bank;

u32 gfx_8032D5D0 = 0;
u32 gfx_frame = 0;
u16 gfx_vi = 0;
u16 gfx_dp = 0;
void (*gfx_callback)(void) = NULL;

CONTROLLER *cont1 = &controller_data[0];
CONTROLLER *cont2 = &controller_data[1];
CONTROLLER *controller = &controller_data[2];

DEMO *demo = NULL;
u16   demo_index = 0;

static void gfx_init_dp(void)
{
	gDPPipeSync(gfx_ptr++);
	gDPPipelineMode(gfx_ptr++, G_PM_1PRIMITIVE);
	gDPSetScissor(gfx_ptr++, G_SC_NON_INTERLACE, 0, 0, SCREEN_WD, SCREEN_HT);
	gDPSetCombineMode(gfx_ptr++, G_CC_SHADE, G_CC_SHADE);
	gDPSetTextureLOD(gfx_ptr++, G_TL_TILE);
	gDPSetTextureLUT(gfx_ptr++, G_TT_NONE);
	gDPSetTextureDetail(gfx_ptr++, G_TD_CLAMP);
	gDPSetTexturePersp(gfx_ptr++, G_TP_PERSP);
	gDPSetTextureFilter(gfx_ptr++, G_TF_BILERP);
	gDPSetTextureConvert(gfx_ptr++, G_TC_FILT);
	gDPSetCombineKey(gfx_ptr++, G_CK_NONE);
	gDPSetAlphaCompare(gfx_ptr++, G_AC_NONE);
	gDPSetRenderMode(gfx_ptr++, G_RM_OPA_SURF, G_RM_OPA_SURF2);
	gDPSetColorDither(gfx_ptr++, G_CD_MAGICSQ);
	gDPSetCycleType(gfx_ptr++, G_CYC_FILL);
	gDPPipeSync(gfx_ptr++);
}

static void gfx_init_sp(void)
{
	gSPClearGeometryMode(
		gfx_ptr++,
		G_SHADE | G_SHADING_SMOOTH | G_CULL_BOTH | G_FOG | G_LIGHTING |
		G_TEXTURE_GEN | G_TEXTURE_GEN_LINEAR | G_LOD
	);
	gSPSetGeometryMode(
		gfx_ptr++, G_SHADE | G_SHADING_SMOOTH | G_CULL_BACK | G_LIGHTING
	);
	gSPNumLights(gfx_ptr++, NUMLIGHTS_1);
	gSPTexture(gfx_ptr++, 0x0000, 0x0000, G_TX_NOLOD, G_TX_RENDERTILE, G_OFF);
}

static void gfx_init_zimg(void)
{
	gDPPipeSync(gfx_ptr++);
	gDPSetDepthSource(gfx_ptr++, G_ZS_PIXEL);
	gDPSetDepthImage(gfx_ptr++, gfx_zimg);
	gDPSetColorImage(
		gfx_ptr++, G_IM_FMT_RGBA, G_IM_SIZ_16b, SCREEN_WD, gfx_zimg
	);
	gDPSetFillColor(gfx_ptr++, 0x00010001U*GPACK_ZDZ(G_MAXFBZ, 0));
	gDPFillRectangle(
		gfx_ptr++, 0, BORDER_HT, SCREEN_WD-1, SCREEN_HT-BORDER_HT-1
	);
}

static void gfx_init_cimg(void)
{
	gDPPipeSync(gfx_ptr++);
	gDPSetCycleType(gfx_ptr++, G_CYC_1CYCLE);
	gDPSetColorImage(
		gfx_ptr++, G_IM_FMT_RGBA, G_IM_SIZ_16b, SCREEN_WD, gfx_cimg[gfx_dp]
	);
#if BORDER_HT > 0
	gDPSetScissor(
		gfx_ptr++, G_SC_NON_INTERLACE,
		0, BORDER_HT, SCREEN_WD, SCREEN_HT-BORDER_HT
	);
#endif
}

void gfx_clear(u32 fill)
{
	gDPPipeSync(gfx_ptr++);
	gDPSetRenderMode(gfx_ptr++, G_RM_OPA_SURF, G_RM_OPA_SURF2);
	gDPSetCycleType(gfx_ptr++, G_CYC_FILL);
	gDPSetFillColor(gfx_ptr++, fill);
	gDPFillRectangle(
		gfx_ptr++, 0, BORDER_HT, SCREEN_WD-1, SCREEN_HT-BORDER_HT-1
	);
	gDPPipeSync(gfx_ptr++);
	gDPSetCycleType(gfx_ptr++, G_CYC_1CYCLE);
}

void gfx_vp_clear(Vp *vp, u32 fill)
{
	SHORT ulx = (vp->vp.vtrans[0]-vp->vp.vscale[0])/4 + 1;
	SHORT uly = (vp->vp.vtrans[1]-vp->vp.vscale[1])/4 + 1;
	SHORT lrx = (vp->vp.vtrans[0]+vp->vp.vscale[0])/4 - 1 - 1;
	SHORT lry = (vp->vp.vtrans[1]+vp->vp.vscale[1])/4 - 1 - 1;
	gDPPipeSync(gfx_ptr++);
	gDPSetRenderMode(gfx_ptr++, G_RM_OPA_SURF, G_RM_OPA_SURF2);
	gDPSetCycleType(gfx_ptr++, G_CYC_FILL);
	gDPSetFillColor(gfx_ptr++, fill);
	gDPFillRectangle(gfx_ptr++, ulx, uly, lrx, lry);
	gDPPipeSync(gfx_ptr++);
	gDPSetCycleType(gfx_ptr++, G_CYC_1CYCLE);
}

static void gfx_draw_border(void)
{
	gDPPipeSync(gfx_ptr++);
	gDPSetScissor(gfx_ptr++, G_SC_NON_INTERLACE, 0, 0, SCREEN_WD, SCREEN_HT);
	gDPSetRenderMode(gfx_ptr++, G_RM_OPA_SURF, G_RM_OPA_SURF2);
	gDPSetCycleType(gfx_ptr++, G_CYC_FILL);
#if BORDER_HT > 0
	gDPSetFillColor(gfx_ptr++, 0x00000000);
	gDPFillRectangle(gfx_ptr++, 0, 0, SCREEN_WD-1, BORDER_HT-1);
	gDPFillRectangle(
		gfx_ptr++, 0, SCREEN_HT-BORDER_HT, SCREEN_WD-1, SCREEN_HT-1
	);
#endif
}

void gfx_vp_scissor(Vp *vp)
{
	SHORT ulx = (vp->vp.vtrans[0]-vp->vp.vscale[0])/4 + 1;
	SHORT uly = (vp->vp.vtrans[1]-vp->vp.vscale[1])/4 + 1;
	SHORT lrx = (vp->vp.vtrans[0]+vp->vp.vscale[0])/4 - 1;
	SHORT lry = (vp->vp.vtrans[1]+vp->vp.vscale[1])/4 - 1;
	gDPSetScissor(gfx_ptr++, G_SC_NON_INTERLACE, ulx, uly, lrx, lry);
}

static void gfx_make_task(void)
{
	size_t len = gfx_ptr - frame->gfx;
	gfx_task->mq = &gfx_dp_mq;
	gfx_task->msg = (OSMesg)2;
	gfx_task->task.t.type = M_GFXTASK;
	gfx_task->task.t.ucode_boot = rspbootTextStart;
	gfx_task->task.t.ucode_boot_size =
		(char *)rspbootTextEnd - (char *)rspbootTextStart;
	gfx_task->task.t.flags = 0;
	gfx_task->task.t.ucode = gspFast3D_fifoTextStart;
	gfx_task->task.t.ucode_data = gspFast3D_fifoDataStart;
	gfx_task->task.t.ucode_size = SP_UCODE_SIZE;
	gfx_task->task.t.ucode_data_size = SP_UCODE_DATA_SIZE;
	gfx_task->task.t.dram_stack = gfx_sp_stack;
	gfx_task->task.t.dram_stack_size = SP_DRAM_STACK_SIZE8;
	gfx_task->task.t.output_buff = gfx_fifo;
	gfx_task->task.t.output_buff_size = gfx_fifo + FIFO_LEN;
	gfx_task->task.t.data_ptr = (u64 *)frame->gfx;
	gfx_task->task.t.data_size = sizeof(Gfx)*len;
	gfx_task->task.t.yield_data_ptr = gfx_sp_yield;
	gfx_task->task.t.yield_data_size = OS_YIELD_DATA_SIZE;
}

void gfx_start(void)
{
	segment_write();
	gfx_init_dp();
	gfx_init_sp();
	gfx_init_zimg();
	gfx_init_cimg();
}

void gfx_end(void)
{
	gfx_draw_border();
	if (debug_time) time_draw();
	gDPFullSync(gfx_ptr++);
	gSPEndDisplayList(gfx_ptr++);
	gfx_make_task();
}

static void gfx_reset(void)
{
	if (reset_timer != 0 && reset_frame < 15)
	{
		int y;
		int x;
		int vi = gfx_vi == 0 ? 2 : gfx_vi-1;
		u64 *cimg = (void *)PHYS_TO_K0(gfx_cimg[vi]);
		cimg += SCREEN_WD/4 * reset_frame++;
		for (y = 0; y < SCREEN_HT/15; y++)
		{
			for (x = 0; x < SCREEN_WD/4; x++) *cimg++ = 0;
			cimg += SCREEN_WD/4 * (15-1);
		}
	}
	osWritebackDCacheAll();
	osRecvMesg(&gfx_vi_mq, &null_msg, OS_MESG_BLOCK);
	osRecvMesg(&gfx_vi_mq, &null_msg, OS_MESG_BLOCK);
}

static void frame_init(void)
{
	frame = &frame_data[0];
	segment_set(SEG_FRAME, frame);
	gfx_task = &frame->task;
	gfx_ptr = frame->gfx;
	gfx_mem = (char *)frame->gfx + sizeof(frame->gfx);
	gfx_start();
	gfx_clear(0x00000000);
	gfx_end();
	sc_queue_gfxtask(&frame->task);
	gfx_dp++;
	gfx_frame++;
}

static void frame_start(void)
{
	frame = &frame_data[gfx_frame & 1];
	segment_set(SEG_FRAME, frame);
	gfx_task = &frame->task;
	gfx_ptr = frame->gfx;
	gfx_mem = (char *)frame->gfx + sizeof(frame->gfx);
}

static void frame_end(void)
{
	time_gfxcpu(TIME_GFXCPU_ENDFRM);
	osRecvMesg(&gfx_dp_mq, &null_msg, OS_MESG_BLOCK);
	if (gfx_callback)
	{
		gfx_callback();
		gfx_callback = NULL;
	}
	sc_queue_gfxtask(&frame->task);
	time_gfxcpu(TIME_GFXCPU_ENDRDP);
	osRecvMesg(&gfx_vi_mq, &null_msg, OS_MESG_BLOCK);
	osViSwapBuffer((void *)PHYS_TO_K0(gfx_cimg[gfx_vi]));
	time_gfxcpu(TIME_GFXCPU_END);
	osRecvMesg(&gfx_vi_mq, &null_msg, OS_MESG_BLOCK);
	if (++gfx_vi == 3) gfx_vi = 0;
	if (++gfx_dp == 3) gfx_dp = 0;
	gfx_frame++;
}

UNUSED static void demo_record(void)
{
	static DEMO record = {0};
	u8 button = (cont1->held & 0xF000) >> 8 | (cont1->held & 0x000F);
	s8 stick_x = cont1->stick_x;
	s8 stick_y = cont1->stick_y;
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
		/*printf(
			"\t.byte %3d, %3d, %3d, 0x%02X\n",
			record.count, record.stick_x, record.stick_y, record.button
		);*/
		record.count   = 0;
		record.button  = button;
		record.stick_x = stick_x;
		record.stick_y = stick_y;
	}
	record.count++;
}

static void cont_update_stick(CONTROLLER *cont)
{
	UNUSED int i;
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
	controller_data[0].pad->button &= 0xFF3F;
	if (demo)
	{
		if (controller_data[1].pad)
		{
			controller_data[1].pad->stick_x = 0;
			controller_data[1].pad->stick_y = 0;
			controller_data[1].pad->button  = 0;
		}
		if (demo->count == 0)
		{
			controller_data[0].pad->stick_x = 0;
			controller_data[0].pad->stick_y = 0;
			controller_data[0].pad->button  = 0x0080;
		}
		else
		{
			u16 start = controller_data[0].pad->button & START_BUTTON;
			controller_data[0].pad->stick_x = demo->stick_x;
			controller_data[0].pad->stick_y = demo->stick_y;
			controller_data[0].pad->button =
				((demo->button & 0xF0) << 8) + (demo->button & 0x0F);
			controller_data[0].pad->button |= start;
			if (--demo->count == 0) demo++;
		}
	}
}

static void cont_update(void)
{
	int i;
	if (cont_bitpattern != 0)
	{
		osRecvMesg(&si_mq, &null_msg, OS_MESG_BLOCK);
		osContGetReadData(cont_pad);
	}
	demo_update();
	for (i = 0; i < CONTROLLER_LEN; i++)
	{
		CONTROLLER *cont = &controller_data[i];
		if (cont->pad)
		{
			cont->stick_x = cont->pad->stick_x;
			cont->stick_y = cont->pad->stick_y;
			cont->down    = cont->pad->button & (cont->pad->button^cont->held);
			cont->held    = cont->pad->button;
			cont_update_stick(cont);
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
	controller->stick_x = cont1->stick_x;
	controller->stick_y = cont1->stick_y;
	controller->x       = cont1->x;
	controller->y       = cont1->y;
	controller->d       = cont1->d;
	controller->down    = cont1->down;
	controller->held    = cont1->held;
}

static void cont_init(void)
{
	SHORT i;
	SHORT c;
	controller_data[0].status = &cont_status[0];
	controller_data[0].pad    = &cont_pad[0];
	osContInit(&si_mq, &cont_bitpattern, cont_status);
	eeprom_status = osEepromProbe(&si_mq);
	for (c = 0, i = 0; i < MAXCONTROLLERS && c < CONTROLLER_LEN; i++)
	{
		if (cont_bitpattern & (1 << i))
		{
			controller_data[c  ].status = &cont_status[i];
			controller_data[c++].pad    = &cont_pad[i];
		}
	}
}

extern const char _MainSegmentRomStart[];
extern const char _MainSegmentRomEnd[];
extern const char _GfxSegmentRomStart[];
extern const char _GfxSegmentRomEnd[];
extern const char _AnimeSegmentRomStart[];
extern const char _DemoSegmentRomStart[];

static void gfx_init(void)
{
	UNUSED int i;
	segment_set(0x00, (void *)0x80000000);
	osCreateMesgQueue(&gfx_dp_mq, &gfx_dp_mbox, 1);
	osCreateMesgQueue(&gfx_vi_mq, &gfx_vi_mbox, 1);
	gfx_zimg    = K0_TO_PHYS(z_image);
	gfx_cimg[0] = K0_TO_PHYS(c_image_a);
	gfx_cimg[1] = K0_TO_PHYS(c_image_b);
	gfx_cimg[2] = K0_TO_PHYS(c_image_c);
	anime_mario_buf = mem_alloc(16384, MEM_ALLOC_L);
	segment_set(SEG_ANIME_MARIO, anime_mario_buf);
	bank_init(&anime_mario_bank, _AnimeSegmentRomStart, anime_mario_buf);
	demo_buf = mem_alloc(2048, MEM_ALLOC_L);
	segment_set(SEG_DEMO, demo_buf);
	bank_init(&demo_bank, _DemoSegmentRomStart, demo_buf);
	mem_load_data(
		SEG_MAIN, _MainSegmentRomStart, _MainSegmentRomEnd, MEM_ALLOC_L
	);
	mem_load_szp(SEG_GFX, _GfxSegmentRomStart, _GfxSegmentRomEnd);
}

extern P_SCRIPT p_main[];

void gfx_main(UNUSED void *arg)
{
	P_SCRIPT *pc;
	gfx_init();
	cont_init();
	save_init();
	sc_client_init(2, &sc_client_gfx, &gfx_vi_mq, (OSMesg)1);
	pc = segment_to_virtual(p_main);
	Na_BGM_play(2, NA_SEQ_SE, 0);
	aud_output(save_output_get());
	frame_init();
	for (;;)
	{
		if (reset_timer != 0)
		{
			gfx_reset();
			continue;
		}
		time_gfxcpu(TIME_GFXCPU_START);
		if (cont_bitpattern != 0) osContStartReadData(&si_mq);
		aud_update();
		frame_start();
		cont_update();
		pc = p_script_main(pc);
		frame_end();
		if (debug_mem) dprintf(180, 20, "BUF %d", gfx_mem-(char *)gfx_ptr);
	}
}