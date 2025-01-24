#include <sm64.h>

#define PRG_UCHAR       ((unsigned char *)prg_pc)
#define PRG_SHORT       ((short *)prg_pc)
#define PRG_USHORT      ((unsigned short *)prg_pc)
#define PRG_INT         ((int *)prg_pc)
#define PRG_LONG        ((long *)prg_pc)
#define PRG_PTR         ((void **)prg_pc)
#define PRG_CALL        ((PRGCALL **)prg_pc)

#define PRG_CMD         PRG_UCHAR[0]
#define PRG_SIZE        PRG_UCHAR[1]

#define PrgStep()       (prg_pc += PRG_SIZE)
#define PrgPush(x)      (*prg_sp++ = (unsigned long)(x))
#define PrgPull()       ((void *)*--prg_sp)

static unsigned long prg_stack[32];
static s16 prg_state;
static long prg_status;
static PRGLANG *prg_pc;

static ARENA *prg_arena = NULL;
static u16 prg_sleep = 0;
static u16 prg_freeze = 0;
static s16 prg_scene = -1;
static unsigned long *prg_sp = prg_stack;
static unsigned long *prg_fp = NULL;

static int PrgCmp(CHAR cmp, long x)
{
	int result = 0;
	switch (cmp)
	{
	case PRG_CMP_AND:   result =  (prg_status & x); break;
	case PRG_CMP_NAND:  result = !(prg_status & x); break;
	case PRG_CMP_EQ:    result = prg_status == x;   break;
	case PRG_CMP_NE:    result = prg_status != x;   break;
	case PRG_CMP_LT:    result = prg_status <  x;   break;
	case PRG_CMP_LE:    result = prg_status <= x;   break;
	case PRG_CMP_GT:    result = prg_status >  x;   break;
	case PRG_CMP_GE:    result = prg_status >= x;   break;
	}
	return result;
}

static void PrgCmdExecute(void)
{
	MemPush();
	MemLoadData(PRG_SHORT[1], PRG_PTR[1], PRG_PTR[2], MEM_ALLOC_L);
	PrgPush(prg_pc + PRG_SIZE);
	PrgPush(prg_fp);
	prg_fp = prg_sp;
	prg_pc = SegmentToVirtual(PRG_PTR[3]);
}

static void PrgCmdChain(void)
{
	void *pc = PRG_PTR[3];
	MemPull();
	MemPush();
	MemLoadData(PRG_SHORT[1], PRG_PTR[1], PRG_PTR[2], MEM_ALLOC_L);
	prg_sp = prg_fp;
	prg_pc = SegmentToVirtual(pc);
}

static void PrgCmdExit(void)
{
	MemPull();
	prg_sp = prg_fp;
	prg_fp = PrgPull();
	prg_pc = PrgPull();
}

static void PrgCmdSleep(void)
{
	prg_state = 0;
	if (prg_sleep == 0)
	{
		prg_sleep = PRG_SHORT[1];
	}
	else if (--prg_sleep == 0)
	{
		PrgStep();
		prg_state = 1;
	}
}

static void PrgCmdFreeze(void)
{
	prg_state = -1;
	if (prg_freeze == 0)
	{
		prg_freeze = PRG_SHORT[1];
	}
	else if (--prg_freeze == 0)
	{
		PrgStep();
		prg_state = 1;
	}
}

static void PrgCmdJump(void)
{
	prg_pc = SegmentToVirtual(PRG_PTR[1]);
}

static void PrgCmdCall(void)
{
	PrgPush(prg_pc + PRG_SIZE);
	prg_pc = SegmentToVirtual(PRG_PTR[1]);
}

static void PrgCmdReturn(void)
{
	prg_pc = PrgPull();
}

static void PrgCmdFor(void)
{
	PrgPush(prg_pc + PRG_SIZE);
	PrgPush(PRG_SHORT[1]);
	PrgStep();
}

static void PrgCmdDone(void)
{
	unsigned long count = prg_sp[-1];
	if (count == 0)
	{
		prg_pc = (void *)prg_sp[-2];
	}
	else if (--count > 0)
	{
		prg_sp[-1] = count;
		prg_pc = (void *)prg_sp[-2];
	}
	else
	{
		PrgStep();
		prg_sp -= 2;
	}
}

static void PrgCmdRepeat(void)
{
	PrgPush(prg_pc + PRG_SIZE);
	PrgPush(0);
	PrgStep();
}

static void PrgCmdUntil(void)
{
	if (PrgCmp(PRG_UCHAR[2], PRG_LONG[1]))
	{
		PrgStep();
		prg_sp -= 2;
	}
	else
	{
		prg_pc = (void *)prg_sp[-2];
	}
}

static void PrgCmdJumpIf(void)
{
	if (PrgCmp(PRG_UCHAR[2], PRG_LONG[1]))
	{
		prg_pc = SegmentToVirtual(PRG_PTR[2]);
	}
	else
	{
		PrgStep();
	}
}

static void PrgCmdCallIf(void)
{
	if (PrgCmp(PRG_UCHAR[2], PRG_LONG[1]))
	{
		PrgPush(prg_pc + PRG_SIZE);
		prg_pc = SegmentToVirtual(PRG_PTR[2]);
	}
	else
	{
		PrgStep();
	}
}

static void PrgCmdIf(void)
{
	if (!PrgCmp(PRG_UCHAR[2], PRG_LONG[1]))
	{
		do
		{
			PrgStep();
		}
		while (PRG_CMD == PRG_CMD_ELSE || PRG_CMD == PRG_CMD_ENDIF);
	}
	PrgStep();
}

static void PrgCmdElse(void)
{
	do
	{
		PrgStep();
	}
	while (PRG_CMD == PRG_CMD_ENDIF);
	PrgStep();
}

static void PrgCmdEndif(void)
{
	PrgStep();
}

static void PrgCmdCallback(void)
{
	PRGCALL *callback = PRG_CALL[1];
	prg_status = callback(PRG_SHORT[1], prg_status);
	PrgStep();
}

static void PrgCmdProcess(void)
{
	PRGCALL *callback = PRG_CALL[1];
	prg_status = callback(PRG_SHORT[1], prg_status);
	if (!prg_status)
	{
		prg_state = 0;
	}
	else
	{
		prg_state = 1;
		PrgStep();
	}
}

static void PrgCmdSet(void)
{
	prg_status = PRG_SHORT[1];
	PrgStep();
}

static void PrgCmdPush(void)
{
	MemPush();
	PrgStep();
}

static void PrgCmdPull(void)
{
	MemPull();
	PrgStep();
}

static void PrgCmdLoadCode(void)
{
	MemLoadCode(PRG_PTR[1], PRG_PTR[2], PRG_PTR[3]);
	PrgStep();
}

static void PrgCmdLoadData(void)
{
	MemLoadData(PRG_SHORT[1], PRG_PTR[1], PRG_PTR[2], MEM_ALLOC_L);
	PrgStep();
}

static void PrgCmdLoadPres(void)
{
	MemLoadPres(PRG_SHORT[1], PRG_PTR[1], PRG_PTR[2]);
	PrgStep();
}

#define FACE_ALLOC 0xE1000

extern char _zimgSegmentStart[];
extern char _cimgSegmentStart[];

static void PrgCmdLoadFace(void)
{
	void *ptr;
	if ((ptr = MemAlloc(FACE_ALLOC, MEM_ALLOC_L)))
	{
		gdm_init(ptr, FACE_ALLOC);
		face_gfx_8019C418(_zimgSegmentStart, 2*SCREEN_WD*SCREEN_HT);
		face_gfx_8019C418(_cimgSegmentStart, 2*SCREEN_WD*SCREEN_HT*3);
		gdm_setup();
		gdm_maketestdl(PRG_SHORT[1]);
	}
	else
	{
	}
	PrgStep();
}

static void PrgCmdLoadText(void)
{
	MemLoadText(PRG_SHORT[1], PRG_PTR[1], PRG_PTR[2]);
	PrgStep();
}

static void PrgCmdStageInit(void)
{
	ShpCreateEmpty(NULL, &sobj_list);
	ObjectInit();
	SceneInit();
	MemPush();
	PrgStep();
}

static void PrgCmdStageExit(void)
{
	ObjectInit();
	SceneExit();
	SceneInit();
	MemPull();
	PrgStep();
}

static void PrgCmdStageStart(void)
{
	if (!prg_arena)
	{
		prg_arena = ArenaCreate(MemAvailable()-sizeof(ARENA), MEM_ALLOC_L);
	}
	PrgStep();
}

static void PrgCmdStageEnd(void)
{
	int i;
	ArenaResize(prg_arena, prg_arena->used);
	prg_arena = NULL;
	for (i = 0; i < SCENE_MAX; i++)
	{
		if (scene_data[i].map)
		{
			MapInit();
			break;
		}
	}
	PrgStep();
}

static void PrgCmdSceneStart(void)
{
	UCHAR i = PRG_UCHAR[2];
	SHPLANG *script = PRG_PTR[1];
	if (i < SCENE_MAX)
	{
		SSCENE *shp = (SSCENE *)ShpLangCompile(prg_arena, script);
		SCAMERA *cam = (SCAMERA *)shp->reftab[0];
		prg_scene = i;
		shp->index = i;
		scene_table[i].shp = shp;
		if (cam)    scene_table[i].cam = (CAMERA *)cam->s.arg;
		else        scene_table[i].cam = NULL;
	}
	PrgStep();
}

static void PrgCmdSceneEnd(void)
{
	prg_scene = -1;
	PrgStep();
}

static void PrgCmdShapeGfx(void)
{
	SHORT shape = PRG_SHORT[1] & 0xFFF;
	SHORT layer = PRG_USHORT[1] >> 12;
	Gfx *gfx = PRG_PTR[1];
	if (shape < SHAPE_MAX)
	{
		shape_table[shape] = &ShpCreateGfx(prg_arena, NULL, layer, gfx)->s;
	}
	PrgStep();
}

static void PrgCmdShape(void)
{
	SHORT shape = PRG_SHORT[1];
	SHPLANG *script = PRG_PTR[1];
	if (shape < SHAPE_MAX)
	{
		shape_table[shape] = ShpLangCompile(prg_arena, script);
	}
	PrgStep();
}

static void PrgCmdShapeScale(void)
{
	union {int i; float f;} scale;
	SHORT shape = PRG_SHORT[1] & 0xFFF;
	SHORT layer = PRG_USHORT[1] >> 12;
	Gfx *gfx = PRG_PTR[1];
	scale.i = PRG_INT[2];
	if (shape < SHAPE_MAX)
	{
		shape_table[shape] =
			&ShpCreateScale(prg_arena, NULL, layer, gfx, scale.f)->s.s;
	}
	PrgStep();
}

static void PrgCmdPlayer(void)
{
	SVecSet(mario_actor->pos, 0, 0, 0);
	SVecSet(mario_actor->ang, 0, 0, 0);
	mario_actor->group = -1;
	mario_actor->scene = 0;
	mario_actor->info = PRG_INT[1];
	mario_actor->script = PRG_PTR[2];
	mario_actor->shape = shape_table[PRG_UCHAR[3]];
	mario_actor->next = NULL;
	PrgStep();
}

static void PrgCmdObject(void)
{
	UCHAR mask = 1 << (level_index-1);
	if (prg_scene != -1)
	{
		if ((PRG_UCHAR[2] & mask) || PRG_UCHAR[2] == 037)
		{
			USHORT shape = PRG_UCHAR[3];
			ACTOR *actor = ArenaAlloc(prg_arena, sizeof(ACTOR));
			actor->pos[0] = PRG_SHORT[2];
			actor->pos[1] = PRG_SHORT[3];
			actor->pos[2] = PRG_SHORT[4];
			actor->ang[0] = PRG_SHORT[5] * 0x8000/180;
			actor->ang[1] = PRG_SHORT[6] * 0x8000/180;
			actor->ang[2] = PRG_SHORT[7] * 0x8000/180;
			actor->scene = prg_scene;
			actor->group = prg_scene;
			actor->info = PRG_INT[4];
			actor->script = PRG_PTR[5];
			actor->shape = shape_table[shape];
			actor->next = scene_table[prg_scene].actor;
			scene_table[prg_scene].actor = actor;
		}
	}
	PrgStep();
}

static void PrgCmdPort(void)
{
	if (prg_scene != -1)
	{
		PORT *port = ArenaAlloc(prg_arena, sizeof(PORT));
		port->p.attr = PRG_UCHAR[2];
		port->p.stage = PRG_UCHAR[3] + PRG_UCHAR[6];
		port->p.scene = PRG_UCHAR[4];
		port->p.port = PRG_UCHAR[5];
		port->obj = NULL;
		port->next = scene_table[prg_scene].port;
		scene_table[prg_scene].port = port;
	}
	PrgStep();
}

static void PrgCmdConnect(void)
{
	int i;
	CONNECT *connect;
	if (prg_scene != -1)
	{
		if (!scene_table[prg_scene].connect)
		{
			scene_table[prg_scene].connect =
				ArenaAlloc(prg_arena, sizeof(CONNECT)*CONNECT_MAX);
			for (i = 0; i < CONNECT_MAX; i++)
			{
				scene_table[prg_scene].connect[i].flag = FALSE;
			}
		}
		connect = &scene_table[prg_scene].connect[PRG_UCHAR[2]];
		connect->flag = TRUE;
		connect->scene = PRG_UCHAR[3];
		connect->offset[0] = PRG_SHORT[2];
		connect->offset[1] = PRG_SHORT[3];
		connect->offset[2] = PRG_SHORT[4];
	}
	PrgStep();
}

static void PrgCmdEnv(void)
{
	if (prg_scene != -1)
	{
		scene_table[prg_scene].env |= PRG_SHORT[1];
	}
	PrgStep();
}

static void PrgCmdBGPort(void)
{
	int i;
	BGPORT *bgport;
	if (prg_scene != -1)
	{
		if (!scene_table[prg_scene].bgport)
		{
			scene_table[prg_scene].bgport =
				ArenaAlloc(prg_arena, sizeof(BGPORT)*BGPORT_MAX);
			for (i = 0; i < BGPORT_MAX; i++)
			{
				scene_table[prg_scene].bgport[i].p.attr = FALSE;
			}
		}
		bgport = &scene_table[prg_scene].bgport[PRG_UCHAR[2]];
		bgport->p.attr = TRUE;
		bgport->p.stage = PRG_UCHAR[3] + PRG_UCHAR[6];
		bgport->p.scene = PRG_UCHAR[4];
		bgport->p.port = PRG_UCHAR[5];
	}
	PrgStep();
}

static void PrgCmd58(void)
{
	SCENE28 *_28;
	if (prg_scene != -1)
	{
		if (!(_28 = scene_table[prg_scene]._28))
		{
			_28 = scene_table[prg_scene]._28 =
				ArenaAlloc(prg_arena, sizeof(SCENE28));
		}
		_28->_00 = PRG_SHORT[1];
		_28->_02 = PRG_SHORT[2];
		_28->_04 = PRG_SHORT[3];
		_28->_06 = PRG_SHORT[4];
		_28->_08 = PRG_SHORT[5];
	}
	PrgStep();
}

static void PrgCmdJet(void)
{
	JET *jet;
	int index = PRG_UCHAR[2];
	int flag = (BuGetFlag() & (BU_KEY2|BU_KEYDOOR2)) != 0;
	if (
		(PRG_UCHAR[3] == 0) ||
		(PRG_UCHAR[3] == 1 && !flag) ||
		(PRG_UCHAR[3] == 2 && flag) ||
		(PRG_UCHAR[3] == 3 && level_index > 1)
	)
	{
		if (prg_scene != -1)
		{
			if (index < 2)
			{
				if (!(jet = scene_table[prg_scene].jet[index]))
				{
					jet = ArenaAlloc(prg_arena, sizeof(JET));
					scene_table[prg_scene].jet[index] = jet;
				}
				SVecSet(jet->pos, PRG_SHORT[2], PRG_SHORT[3], PRG_SHORT[4]);
				jet->attr = PRG_SHORT[5];
			}
		}
	}
	PrgStep();
}

static void PrgCmdViBlack(void)
{
	osViBlack(PRG_UCHAR[2]);
	PrgStep();
}

static void PrgCmdViGamma(void)
{
	osViSetSpecialFeatures(!PRG_UCHAR[2] ? OS_VI_GAMMA_OFF : OS_VI_GAMMA_ON);
	PrgStep();
}

static void PrgCmdMap(void)
{
	if (prg_scene != -1)
	{
		scene_table[prg_scene].map = SegmentToVirtual(PRG_PTR[1]);
	}
	PrgStep();
}

static void PrgCmdArea(void)
{
	if (prg_scene != -1)
	{
		scene_table[prg_scene].area = SegmentToVirtual(PRG_PTR[1]);
	}
	PrgStep();
}

static void PrgCmdTag(void)
{
	if (prg_scene != -1)
	{
		scene_table[prg_scene].tag = SegmentToVirtual(PRG_PTR[1]);
	}
	PrgStep();
}

static void PrgCmdSceneOpen(void)
{
	SHORT index = PRG_UCHAR[2];
	UNUSED void *sp18 = prg_pc + 4;
	Na_SeClear();
	SceneOpen(index);
	PrgStep();
}

static void PrgCmdSceneClose(void)
{
	SceneClose();
	PrgStep();
}

static void PrgCmdPlayerOpen(void)
{
	mario_actor->scene = PRG_UCHAR[2];
	SVecCpy(mario_actor->pos, PRG_SHORT+3);
	SVecSet(mario_actor->ang, 0, PRG_SHORT[2] * 0x8000/180, 0);
	PrgStep();
}

static void PrgCmdPlayerClose(void)
{
	SnClosePlayer();
	PrgStep();
}

static void PrgCmdSceneProc(void)
{
	SceneProc();
	PrgStep();
}

static void PrgCmdWipe(void)
{
	if (scenep) SnWipe(
		PRG_UCHAR[2], PRG_UCHAR[3], PRG_UCHAR[4], PRG_UCHAR[5], PRG_UCHAR[6]
	);
	PrgStep();
}

static void PrgCmd50(void)
{
	PrgStep();
}

static void PrgCmdMessage(void)
{
	if (prg_scene != -1)
	{
		if (PRG_UCHAR[2] < 2)
		{
			scene_table[prg_scene].msg[PRG_UCHAR[2]] = PRG_UCHAR[3];
		}
	}
	PrgStep();
}

static void PrgCmdBGM(void)
{
	if (prg_scene != -1)
	{
		scene_table[prg_scene].bgm_mode = PRG_SHORT[1];
		scene_table[prg_scene].bgm = PRG_SHORT[2];
	}
	PrgStep();
}

static void PrgCmdPlayBGM(void)
{
	AudPlayBGM(0, PRG_SHORT[1], 0);
	PrgStep();
}

static void PrgCmdAudFadeout(void)
{
	AudFadeout(PRG_SHORT[1]);
	PrgStep();
}

static void PrgCmdVar(void)
{
	if (PRG_UCHAR[2] == 0)
	{
		switch (PRG_UCHAR[3])
		{
		case PRG_VAR_FILE:    file_index      = prg_status; break;
		case PRG_VAR_COURSE:  course_index    = prg_status; break;
		case PRG_VAR_LEVEL:   level_index     = prg_status; break;
		case PRG_VAR_STAGE:   stage_index     = prg_status; break;
		case PRG_VAR_SCENE:   scene_index     = prg_status; break;
		}
	}
	else
	{
		switch (PRG_UCHAR[3])
		{
		case PRG_VAR_FILE:    prg_status = file_index;      break;
		case PRG_VAR_COURSE:  prg_status = course_index;    break;
		case PRG_VAR_LEVEL:   prg_status = level_index;     break;
		case PRG_VAR_STAGE:   prg_status = stage_index;     break;
		case PRG_VAR_SCENE:   prg_status = scene_index;     break;
		}
	}
	PrgStep();
}

static void (*prg_cmdtab[])(void) =
{
	PrgCmdExecute,
	PrgCmdChain,
	PrgCmdExit,
	PrgCmdSleep,
	PrgCmdFreeze,
	PrgCmdJump,
	PrgCmdCall,
	PrgCmdReturn,
	PrgCmdFor,
	PrgCmdDone,
	PrgCmdRepeat,
	PrgCmdUntil,
	PrgCmdJumpIf,
	PrgCmdCallIf,
	PrgCmdIf,
	PrgCmdElse,
	PrgCmdEndif,
	PrgCmdCallback,
	PrgCmdProcess,
	PrgCmdSet,
	PrgCmdPush,
	PrgCmdPull,
	PrgCmdLoadCode,
	PrgCmdLoadData,
	PrgCmdLoadPres,
	PrgCmdLoadFace,
	PrgCmdLoadText,
	PrgCmdStageInit,
	PrgCmdStageExit,
	PrgCmdStageStart,
	PrgCmdStageEnd,
	PrgCmdSceneStart,
	PrgCmdSceneEnd,
	PrgCmdShapeGfx,
	PrgCmdShape,
	PrgCmdShapeScale,
	PrgCmdObject,
	PrgCmdPlayer,
	PrgCmdPort,
	PrgCmdBGPort,
	PrgCmdConnect,
	PrgCmdSceneOpen,
	PrgCmdSceneClose,
	PrgCmdPlayerOpen,
	PrgCmdPlayerClose,
	PrgCmdSceneProc,
	PrgCmdMap,
	PrgCmdArea,
	PrgCmdMessage,
	PrgCmdEnv,
	PrgCmd50,
	PrgCmdWipe,
	PrgCmdViBlack,
	PrgCmdViGamma,
	PrgCmdBGM,
	PrgCmdPlayBGM,
	PrgCmdAudFadeout,
	PrgCmdTag,
	PrgCmd58,
	PrgCmdJet,
	PrgCmdVar,
};

PRGLANG *PrgLangExec(PRGLANG *pc)
{
	prg_state = 1;
	prg_pc = pc;
	while (prg_state == 1) prg_cmdtab[PRG_CMD]();
	TimeGfxCPU(TIME_GFXCPU_ENDPRC);
	GfxStart();
	SceneDraw();
	GfxEnd();
	GfxAlloc(0);
	return prg_pc;
}
