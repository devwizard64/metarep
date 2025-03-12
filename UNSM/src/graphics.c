#include <sm64.h>

UNUSED static char gfx_8032D5D0 = 0;

static OSContStatus cont_status[MAXCONTROLLERS];
static OSContPad cont_pad[MAXCONTROLLERS];

static OSMesgQueue gfx_vi_mq;
static OSMesgQueue gfx_dp_mq;
static OSMesg gfx_vi_mbox;
static OSMesg gfx_dp_mbox;
static SCCLIENT gfx_client;

static unsigned long gfx_cimg[3];
static unsigned long gfx_zimg;
static void *mario_anime_buf;
static void *demo_buf;

u32 gfx_frame = 0;
u16 gfx_vi = 0;
u16 gfx_dp = 0;
SCTASK *gfx_task;
Gfx *glistp;
char *gfx_mem;
FRAME *framep;
void (*gfx_callback)(void) = NULL;

CONTROLLER controller_data[CONTROLLER_MAX+1];
CONTROLLER *cont1 = &controller_data[0];
CONTROLLER *cont2 = &controller_data[1];
CONTROLLER *contp = &controller_data[2];
DEMO *demop = NULL;
u16 demo_index = 0;
u8 cont_bitpattern;
s8 eeprom_status;

BANK mario_anime_bank;
BANK demo_bank;

#ifdef GATEWAY

#define HALT_REG_START_ADDR 0x0ff70000
#define HALT_REG_latency 0x5
#define HALT_REG_pulse 0x0c
#define HALT_REG_pageSize 0xd
#define HALT_REG_relDuration 0x2

extern void __osPiGetAccess(void);
extern void __osPiRelAccess(void);

static void WriteGatewayRegister(int active)
{
	register u32 stat;
	IO_WRITE(PI_BSD_DOM2_LAT_REG, HALT_REG_latency);
	IO_WRITE(PI_BSD_DOM2_PWD_REG, HALT_REG_pulse);
	IO_WRITE(PI_BSD_DOM2_PGS_REG, HALT_REG_pageSize);
	IO_WRITE(PI_BSD_DOM2_RLS_REG, HALT_REG_relDuration);
	__osPiGetAccess();
	stat = IO_READ(PI_STATUS_REG);
	while (stat & (PI_STATUS_IO_BUSY|PI_STATUS_DMA_BUSY))
	{
		stat = IO_READ(PI_STATUS_REG);
	}
	if (active) IO_WRITE(HALT_REG_START_ADDR, 0x01010101);
	else        IO_WRITE(HALT_REG_START_ADDR, 0x00000000);
	__osPiRelAccess();
}

static void ContRead(void)
{
	osRecvMesg(&si_mq, &null_msg, OS_MESG_BLOCK);
	osContGetReadData(cont_pad);
#ifdef MOTOR
	motor_8024C510();
#endif
	if ((cont1->pad->button & (U_JPAD|D_JPAD)) == (U_JPAD|D_JPAD))
	{
		sys_halt = TRUE;
		WriteGatewayRegister(1);
		do
		{
			osContStartReadData(&si_mq);
			osRecvMesg(&si_mq, &null_msg, OS_MESG_BLOCK);
			osContGetReadData(cont_pad);
		}
		while ((cont1->pad->button & (L_JPAD|R_JPAD)) != (L_JPAD|R_JPAD));
		WriteGatewayRegister(0);
		sys_halt = FALSE;
	}
}

#else

#ifdef MOTOR
#define ContRead() \
{ \
	osRecvMesg(&si_mq, &null_msg, OS_MESG_BLOCK); \
	osContGetReadData(cont_pad); \
	motor_8024C510(); \
}
#else
#define ContRead() \
{ \
	osRecvMesg(&si_mq, &null_msg, OS_MESG_BLOCK); \
	osContGetReadData(cont_pad); \
}
#endif

#endif

static void GfxInitDP(void)
{
	gDPPipeSync(glistp++);
	gDPPipelineMode(glistp++, G_PM_1PRIMITIVE);
	gDPSetScissor(glistp++, G_SC_NON_INTERLACE, 0, 0, SCREEN_WD, SCREEN_HT);
	gDPSetCombineMode(glistp++, G_CC_SHADE, G_CC_SHADE);
	gDPSetTextureLOD(glistp++, G_TL_TILE);
	gDPSetTextureLUT(glistp++, G_TT_NONE);
	gDPSetTextureDetail(glistp++, G_TD_CLAMP);
	gDPSetTexturePersp(glistp++, G_TP_PERSP);
	gDPSetTextureFilter(glistp++, G_TF_BILERP);
	gDPSetTextureConvert(glistp++, G_TC_FILT);
	gDPSetCombineKey(glistp++, G_CK_NONE);
	gDPSetAlphaCompare(glistp++, G_AC_NONE);
	gDPSetRenderMode(glistp++, G_RM_OPA_SURF, G_RM_OPA_SURF2);
	gDPSetColorDither(glistp++, G_CD_MAGICSQ);
	gDPSetCycleType(glistp++, G_CYC_FILL);
#if REVISION >= 199707
	gDPSetAlphaDither(glistp++, G_AD_PATTERN);
#endif
	gDPPipeSync(glistp++);
}

static void GfxInitSP(void)
{
	gSPClearGeometryMode(
		glistp++,
		G_SHADE | G_SHADING_SMOOTH | G_CULL_BOTH | G_FOG | G_LIGHTING |
		G_TEXTURE_GEN | G_TEXTURE_GEN_LINEAR | G_LOD
	);
	gSPSetGeometryMode(
		glistp++, G_SHADE | G_SHADING_SMOOTH | G_CULL_BACK | G_LIGHTING
	);
	gSPNumLights(glistp++, NUMLIGHTS_1);
	gSPTexture(glistp++, 0x0000, 0x0000, G_TX_NOLOD, G_TX_RENDERTILE, G_OFF);
}

static void GfxInitZB(void)
{
	gDPPipeSync(glistp++);
	gDPSetDepthSource(glistp++, G_ZS_PIXEL);
	gDPSetDepthImage(glistp++, gfx_zimg);
	gDPSetColorImage(
		glistp++, G_IM_FMT_RGBA, G_IM_SIZ_16b, SCREEN_WD, gfx_zimg
	);
	gDPSetFillColor(glistp++, 0x00010001U*GPACK_ZDZ(G_MAXFBZ, 0));
	gDPFillRectangle(
		glistp++, 0, BORDER_HT, SCREEN_WD-1, SCREEN_HT-BORDER_HT-1
	);
}

static void GfxInitCB(void)
{
	gDPPipeSync(glistp++);
	gDPSetCycleType(glistp++, G_CYC_1CYCLE);
	gDPSetColorImage(
		glistp++, G_IM_FMT_RGBA, G_IM_SIZ_16b, SCREEN_WD, gfx_cimg[gfx_dp]
	);
#if BORDER_HT > 0
	gDPSetScissor(
		glistp++, G_SC_NON_INTERLACE,
		0, BORDER_HT, SCREEN_WD, SCREEN_HT-BORDER_HT
	);
#endif
}

void GfxClear(u32 fill)
{
	gDPPipeSync(glistp++);
	gDPSetRenderMode(glistp++, G_RM_OPA_SURF, G_RM_OPA_SURF2);
	gDPSetCycleType(glistp++, G_CYC_FILL);
	gDPSetFillColor(glistp++, fill);
	gDPFillRectangle(
		glistp++, 0, BORDER_HT, SCREEN_WD-1, SCREEN_HT-BORDER_HT-1
	);
	gDPPipeSync(glistp++);
	gDPSetCycleType(glistp++, G_CYC_1CYCLE);
}

void GfxVpClear(Vp *vp, u32 fill)
{
	SHORT ulx = (vp->vp.vtrans[0]-vp->vp.vscale[0])/4 + 1;
	SHORT uly = (vp->vp.vtrans[1]-vp->vp.vscale[1])/4 + 1;
	SHORT lrx = (vp->vp.vtrans[0]+vp->vp.vscale[0])/4 - 1 - 1;
	SHORT lry = (vp->vp.vtrans[1]+vp->vp.vscale[1])/4 - 1 - 1;
	gDPPipeSync(glistp++);
	gDPSetRenderMode(glistp++, G_RM_OPA_SURF, G_RM_OPA_SURF2);
	gDPSetCycleType(glistp++, G_CYC_FILL);
	gDPSetFillColor(glistp++, fill);
	gDPFillRectangle(glistp++, ulx, uly, lrx, lry);
	gDPPipeSync(glistp++);
	gDPSetCycleType(glistp++, G_CYC_1CYCLE);
}

static void GfxDrawBorder(void)
{
	gDPPipeSync(glistp++);
	gDPSetScissor(glistp++, G_SC_NON_INTERLACE, 0, 0, SCREEN_WD, SCREEN_HT);
	gDPSetRenderMode(glistp++, G_RM_OPA_SURF, G_RM_OPA_SURF2);
	gDPSetCycleType(glistp++, G_CYC_FILL);
#if BORDER_HT > 0
	gDPSetFillColor(glistp++, 0x00000000);
	gDPFillRectangle(glistp++, 0, 0, SCREEN_WD-1, BORDER_HT-1);
	gDPFillRectangle(
		glistp++, 0, SCREEN_HT-BORDER_HT, SCREEN_WD-1, SCREEN_HT-1
	);
#endif
}

void GfxVpScissor(Vp *vp)
{
	SHORT ulx = (vp->vp.vtrans[0]-vp->vp.vscale[0])/4 + 1;
	SHORT uly = (vp->vp.vtrans[1]-vp->vp.vscale[1])/4 + 1;
	SHORT lrx = (vp->vp.vtrans[0]+vp->vp.vscale[0])/4 - 1;
	SHORT lry = (vp->vp.vtrans[1]+vp->vp.vscale[1])/4 - 1;
	gDPSetScissor(glistp++, G_SC_NON_INTERLACE, ulx, uly, lrx, lry);
}

static void GfxMakeTask(void)
{
	int len = glistp - framep->gfx;
	gfx_task->mq = &gfx_dp_mq;
	gfx_task->msg = (OSMesg)2;
	gfx_task->task.t.type = M_GFXTASK;
	gfx_task->task.t.ucode_boot = (void *)rspbootTextStart;
	gfx_task->task.t.ucode_boot_size =
		(char *)rspbootTextEnd - (char *)rspbootTextStart;
	gfx_task->task.t.flags = 0;
	gfx_task->task.t.ucode = (void *)gspFast3D_fifoTextStart;
	gfx_task->task.t.ucode_data = (void *)gspFast3D_fifoDataStart;
	gfx_task->task.t.ucode_size = SP_UCODE_SIZE;
	gfx_task->task.t.ucode_data_size = SP_UCODE_DATA_SIZE;
	gfx_task->task.t.dram_stack = gfx_sp_stack;
	gfx_task->task.t.dram_stack_size = SP_DRAM_STACK_SIZE8;
	gfx_task->task.t.output_buff = gfx_fifo;
	gfx_task->task.t.output_buff_size = gfx_fifo + FIFO_LEN;
	gfx_task->task.t.data_ptr = (u64 *)framep->gfx;
	gfx_task->task.t.data_size = sizeof(Gfx)*len;
	gfx_task->task.t.yield_data_ptr = gfx_sp_yield;
#if REVISION == 199605 /* ? */
	gfx_task->task.t.yield_data_size = 0xBA0;
#else
	gfx_task->task.t.yield_data_size = OS_YIELD_DATA_SIZE;
#endif
}

void GfxBegin(void)
{
	SegmentWrite();
	GfxInitDP();
	GfxInitSP();
	GfxInitZB();
	GfxInitCB();
}

void GfxEnd(void)
{
	GfxDrawBorder();
	if (debug_time) TimeDraw();
	gDPFullSync(glistp++);
	gSPEndDisplayList(glistp++);
	GfxMakeTask();
}

static void GfxReset(void)
{
	if (reset_timer && reset_frame < 15)
	{
		int y, x;
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

static void FrameInit(void)
{
	framep = &frame_data[0];
	SegmentSet(SEG_FRAME, framep);
	gfx_task = &framep->task;
	glistp = framep->gfx;
	gfx_mem = (char *)framep->gfx + sizeof(framep->gfx);
	GfxBegin();
	GfxClear(0x00000000);
	GfxEnd();
	ScQueueGfxTask(&framep->task);
	gfx_dp++;
	gfx_frame++;
}

static void FrameBegin(void)
{
	framep = &frame_data[gfx_frame & 1];
	SegmentSet(SEG_FRAME, framep);
	gfx_task = &framep->task;
	glistp = framep->gfx;
	gfx_mem = (char *)framep->gfx + sizeof(framep->gfx);
}

static void FrameEnd(void)
{
	TimeGfxCPU(TIME_GFXCPU_ENDFRM);
	osRecvMesg(&gfx_dp_mq, &null_msg, OS_MESG_BLOCK);
	if (gfx_callback)
	{
		gfx_callback();
		gfx_callback = NULL;
	}
	ScQueueGfxTask(&framep->task);
	TimeGfxCPU(TIME_GFXCPU_ENDRDP);
	osRecvMesg(&gfx_vi_mq, &null_msg, OS_MESG_BLOCK);
	osViSwapBuffer((void *)PHYS_TO_K0(gfx_cimg[gfx_vi]));
	TimeGfxCPU(TIME_GFXCPU_END);
	osRecvMesg(&gfx_vi_mq, &null_msg, OS_MESG_BLOCK);
	if (++gfx_vi == 3) gfx_vi = 0;
	if (++gfx_dp == 3) gfx_dp = 0;
	gfx_frame++;
}

UNUSED
static void DemoRecord(void)
{
	static DEMO record = {0};
	u8 button = (cont1->held & 0xF000) >> 8 | (cont1->held & 0x000F);
	s8 stick_x = cont1->stick_x;
	s8 stick_y = cont1->stick_y;
	if (stick_x > -8 && stick_x < 8) stick_x = 0;
	if (stick_y > -8 && stick_y < 8) stick_y = 0;
	if (
		record.count == 255 ||
		button != record.button  ||
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

static void ContProcStick(CONTROLLER *cont)
{
	UNUSED int i;
	cont->x = 0;
	cont->y = 0;
	if (cont->stick_x <= -8) cont->x = cont->stick_x + 6;
	if (cont->stick_x >=  8) cont->x = cont->stick_x - 6;
	if (cont->stick_y <= -8) cont->y = cont->stick_y + 6;
	if (cont->stick_y >=  8) cont->y = cont->stick_y - 6;
	cont->dist = DIST2(cont->x, cont->y);
	if (cont->dist > 64)
	{
		cont->x *= 64/cont->dist;
		cont->y *= 64/cont->dist;
		cont->dist = 64;
	}
}

static void DemoProc(void)
{
	controller_data[0].pad->button &= 0xFF3F;
	if (demop)
	{
		if (controller_data[1].pad)
		{
			controller_data[1].pad->stick_x = 0;
			controller_data[1].pad->stick_y = 0;
			controller_data[1].pad->button  = 0;
		}
		if (demop->count == 0)
		{
			controller_data[0].pad->stick_x = 0;
			controller_data[0].pad->stick_y = 0;
			controller_data[0].pad->button  = CONT_EXIT;
		}
		else
		{
			u16 start = controller_data[0].pad->button & START_BUTTON;
			controller_data[0].pad->stick_x = demop->stick_x;
			controller_data[0].pad->stick_y = demop->stick_y;
			controller_data[0].pad->button =
				((demop->button & 0xF0) << 8) + (demop->button & 0x0F);
			controller_data[0].pad->button |= start;
			if (--demop->count == 0) demop++;
		}
	}
}

static void ContProc(void)
{
	int i;
	if (cont_bitpattern) ContRead();
	DemoProc();
	for (i = 0; i < CONTROLLER_MAX; i++)
	{
		CONTROLLER *cont = &controller_data[i];
		if (cont->pad)
		{
			cont->stick_x = cont->pad->stick_x;
			cont->stick_y = cont->pad->stick_y;
			cont->down    = cont->pad->button & (cont->pad->button^cont->held);
			cont->held    = cont->pad->button;
			ContProcStick(cont);
		}
		else
		{
			cont->stick_x = 0;
			cont->stick_y = 0;
			cont->down    = 0;
			cont->held    = 0;
			cont->x       = 0;
			cont->y       = 0;
			cont->dist    = 0;
		}
	}
	contp->stick_x = cont1->stick_x;
	contp->stick_y = cont1->stick_y;
	contp->x       = cont1->x;
	contp->y       = cont1->y;
	contp->dist    = cont1->dist;
	contp->down    = cont1->down;
	contp->held    = cont1->held;
}

static void ContInit(void)
{
	SHORT i, c;
	controller_data[0].status = &cont_status[0];
	controller_data[0].pad    = &cont_pad[0];
	osContInit(&si_mq, &cont_bitpattern, cont_status);
#ifdef DISK
	eeprom_status = 1;
#else
	eeprom_status = osEepromProbe(&si_mq);
#endif
	for (c = 0, i = 0; i < MAXCONTROLLERS && c < CONTROLLER_MAX; i++)
	{
		if (cont_bitpattern & (1 << i))
		{
#ifdef MOTOR
			controller_data[c  ].port = i;
#endif
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
extern const char _AnimeSegmentRomEnd[];
extern const char _DemoSegmentRomStart[];

static void GfxInit(void)
{
	UNUSED int i;
	SegmentSet(0x00, (void *)0x80000000);
	osCreateMesgQueue(&gfx_dp_mq, &gfx_dp_mbox, 1);
	osCreateMesgQueue(&gfx_vi_mq, &gfx_vi_mbox, 1);
	gfx_zimg    = K0_TO_PHYS(z_image);
	gfx_cimg[0] = K0_TO_PHYS(c_image_a);
	gfx_cimg[1] = K0_TO_PHYS(c_image_b);
	gfx_cimg[2] = K0_TO_PHYS(c_image_c);
	mario_anime_buf = MemAlloc(16384, MEM_ALLOC_L);
	SegmentSet(SEG_MARIO_ANIME, mario_anime_buf);
#ifdef DISK
	BankInitAnime(
		&mario_anime_bank, _AnimeSegmentRomStart, _AnimeSegmentRomEnd,
		mario_anime_buf
	);
#else
	BankInit(&mario_anime_bank, _AnimeSegmentRomStart, mario_anime_buf);
#endif
	demo_buf = MemAlloc(2048, MEM_ALLOC_L);
	SegmentSet(SEG_DEMO, demo_buf);
	BankInit(&demo_bank, _DemoSegmentRomStart, demo_buf);
	MemLoadData(
		SEG_MAIN, _MainSegmentRomStart, _MainSegmentRomEnd, MEM_ALLOC_L
	);
	MemLoadPres(SEG_GFX, _GfxSegmentRomStart, _GfxSegmentRomEnd);
}

extern SEQLANG seq_main[];

void GfxProc(UNUSED void *arg)
{
	SEQLANG *pc;
	debugf(("start gfx thread\n"));
	GfxInit();
#ifdef MOTOR
	motor_8024C4A0();
#endif
	debugf(("init ctrl\n"));
	ContInit();
	debugf(("done ctrl\n"));
#ifdef MOTOR
	motor_8024CC10();
#endif
	BackupInit();
	ScSetClient(SC_GFXCLIENT, &gfx_client, &gfx_vi_mq, (OSMesg)1);
	pc = SegmentToVirtual(seq_main);
#if REVISION != 199605
	Na_BgmPlay(NA_HANDLE_SE, NA_SEQ_SE, 0);
#endif
	AudSetMode(BuGetSound());
	FrameInit();
	for (;;)
	{
		if (reset_timer)
		{
			GfxReset();
			continue;
		}
		TimeGfxCPU(TIME_GFXCPU_START);
		if (cont_bitpattern)
		{
#ifdef MOTOR
			motor_8024C4E4();
#endif
			osContStartReadData(&si_mq);
		}
		AudTick();
		FrameBegin();
		ContProc();
		pc = SeqExec(pc);
		FrameEnd();
		if (debug_info) dprintf(180, 20, "BUF %d", gfx_mem-(char *)glistp);
	}
}
