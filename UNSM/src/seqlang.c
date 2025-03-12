#include <sm64.h>

#define SEQ_UCHAR       ((unsigned char *)seq_pc)
#define SEQ_SHORT       ((short *)seq_pc)
#define SEQ_INT         ((int *)seq_pc)
#define SEQ_LONG        ((long *)seq_pc)
#define SEQ_PTR         ((void **)seq_pc)
#define SEQ_CALL        ((SEQCALL **)seq_pc)

#define SEQ_CMD         SEQ_UCHAR[0]
#define SEQ_SIZE        SEQ_UCHAR[1]

#define SeqStep()       (seq_pc += SEQ_SIZE)
#define SeqPush(x)      (*seq_sp++ = (unsigned long)(x))
#define SeqPull()       ((void *)*--seq_sp)

static unsigned long seq_stack[32];
static short seq_state;
static long seq_status;
static SEQLANG *seq_pc;

static ARENA *seq_arena = NULL;
static u16 seq_sleep = 0;
static u16 seq_freeze = 0;
static short seq_scene = -1;
static unsigned long *seq_sp = seq_stack;
static unsigned long *seq_fp = NULL;

static int SeqCmp(CHAR cmp, long x)
{
	int result = 0;
	switch (cmp)
	{
	case SEQ_CMP_AND:   result =  (seq_status & x); break;
	case SEQ_CMP_NAND:  result = !(seq_status & x); break;
	case SEQ_CMP_EQ:    result = seq_status == x;   break;
	case SEQ_CMP_NE:    result = seq_status != x;   break;
	case SEQ_CMP_LT:    result = seq_status <  x;   break;
	case SEQ_CMP_LE:    result = seq_status <= x;   break;
	case SEQ_CMP_GT:    result = seq_status >  x;   break;
	case SEQ_CMP_GE:    result = seq_status >= x;   break;
	}
	return result;
}

static void SeqCmdExecute(void)
{
	MemPush();
	MemLoadData(SEQ_SHORT[1], SEQ_PTR[1], SEQ_PTR[2], MEM_ALLOC_L);
	SeqPush(seq_pc + SEQ_SIZE);
	SeqPush(seq_fp);
	seq_fp = seq_sp;
	seq_pc = SegmentToVirtual(SEQ_PTR[3]);
}

static void SeqCmdChain(void)
{
	void *pc = SEQ_PTR[3];
	MemPull();
	MemPush();
	MemLoadData(SEQ_SHORT[1], SEQ_PTR[1], SEQ_PTR[2], MEM_ALLOC_L);
	seq_sp = seq_fp;
	seq_pc = SegmentToVirtual(pc);
}

static void SeqCmdExit(void)
{
	MemPull();
	seq_sp = seq_fp;
	seq_fp = SeqPull();
	seq_pc = SeqPull();
}

static void SeqCmdSleep(void)
{
	seq_state = 0;
	if (seq_sleep == 0)
	{
		seq_sleep = SEQ_SHORT[1];
	}
	else if (--seq_sleep == 0)
	{
		SeqStep();
		seq_state = 1;
	}
}

static void SeqCmdFreeze(void)
{
	seq_state = -1;
	if (seq_freeze == 0)
	{
		seq_freeze = SEQ_SHORT[1];
	}
	else if (--seq_freeze == 0)
	{
		SeqStep();
		seq_state = 1;
	}
}

static void SeqCmdJump(void)
{
	seq_pc = SegmentToVirtual(SEQ_PTR[1]);
}

static void SeqCmdCall(void)
{
	SeqPush(seq_pc + SEQ_SIZE);
	seq_pc = SegmentToVirtual(SEQ_PTR[1]);
}

static void SeqCmdReturn(void)
{
	seq_pc = SeqPull();
}

static void SeqCmdFor(void)
{
	SeqPush(seq_pc + SEQ_SIZE);
	SeqPush(SEQ_SHORT[1]);
	SeqStep();
}

static void SeqCmdDone(void)
{
	unsigned long count = seq_sp[-1];
	if (count == 0)
	{
		seq_pc = (void *)seq_sp[-2];
	}
	else if (--count > 0)
	{
		seq_sp[-1] = count;
		seq_pc = (void *)seq_sp[-2];
	}
	else
	{
		SeqStep();
		seq_sp -= 2;
	}
}

static void SeqCmdRepeat(void)
{
	SeqPush(seq_pc + SEQ_SIZE);
	SeqPush(0);
	SeqStep();
}

static void SeqCmdUntil(void)
{
	if (SeqCmp(SEQ_UCHAR[2], SEQ_LONG[1]))
	{
		SeqStep();
		seq_sp -= 2;
	}
	else
	{
		seq_pc = (void *)seq_sp[-2];
	}
}

static void SeqCmdJumpIf(void)
{
	if (SeqCmp(SEQ_UCHAR[2], SEQ_LONG[1]))
	{
		seq_pc = SegmentToVirtual(SEQ_PTR[2]);
	}
	else
	{
		SeqStep();
	}
}

static void SeqCmdCallIf(void)
{
	if (SeqCmp(SEQ_UCHAR[2], SEQ_LONG[1]))
	{
		SeqPush(seq_pc + SEQ_SIZE);
		seq_pc = SegmentToVirtual(SEQ_PTR[2]);
	}
	else
	{
		SeqStep();
	}
}

static void SeqCmdIf(void)
{
	if (!SeqCmp(SEQ_UCHAR[2], SEQ_LONG[1]))
	{
		do
		{
			SeqStep();
		}
		while (SEQ_CMD == SEQ_CMD_ELSE || SEQ_CMD == SEQ_CMD_ENDIF);
	}
	SeqStep();
}

static void SeqCmdElse(void)
{
	do
	{
		SeqStep();
	}
	while (SEQ_CMD == SEQ_CMD_ENDIF);
	SeqStep();
}

static void SeqCmdEndif(void)
{
	SeqStep();
}

static void SeqCmdCallback(void)
{
	SEQCALL *callback = SEQ_CALL[1];
	seq_status = callback(SEQ_SHORT[1], seq_status);
	SeqStep();
}

static void SeqCmdProcess(void)
{
	SEQCALL *callback = SEQ_CALL[1];
	seq_status = callback(SEQ_SHORT[1], seq_status);
	if (!seq_status)
	{
		seq_state = 0;
	}
	else
	{
		seq_state = 1;
		SeqStep();
	}
}

static void SeqCmdSet(void)
{
	seq_status = SEQ_SHORT[1];
	SeqStep();
}

static void SeqCmdPush(void)
{
	MemPush();
	SeqStep();
}

static void SeqCmdPull(void)
{
	MemPull();
	SeqStep();
}

static void SeqCmdLoadCode(void)
{
	MemLoadCode(SEQ_PTR[1], SEQ_PTR[2], SEQ_PTR[3]);
	SeqStep();
}

static void SeqCmdLoadData(void)
{
	MemLoadData(SEQ_SHORT[1], SEQ_PTR[1], SEQ_PTR[2], MEM_ALLOC_L);
	SeqStep();
}

static void SeqCmdLoadPres(void)
{
	MemLoadPres(SEQ_SHORT[1], SEQ_PTR[1], SEQ_PTR[2]);
	SeqStep();
}

#define FACE_ALLOC 0xE1000

extern char _zimgSegmentStart[];
extern char _cimgSegmentStart[];

static void SeqCmdLoadFace(void)
{
#if REVISION != 199605
	void *ptr;
	if ((ptr = MemAlloc(FACE_ALLOC, MEM_ALLOC_L)))
	{
		gdm_init(ptr, FACE_ALLOC);
		face_gfx_8019C418(_zimgSegmentStart, 2*SCREEN_WD*SCREEN_HT);
		face_gfx_8019C418(_cimgSegmentStart, 2*SCREEN_WD*SCREEN_HT*3);
		gdm_setup();
		gdm_maketestdl(SEQ_SHORT[1]);
	}
	else
	{
		debugf(("face anime memory overflow\n"));
	}
#endif
	SeqStep();
}

static void SeqCmdLoadText(void)
{
	MemLoadText(SEQ_SHORT[1], SEQ_PTR[1], SEQ_PTR[2]);
	SeqStep();
}

static void SeqCmdStageInit(void)
{
	ShpCreateEmpty(NULL, &sobj_list);
	ObjectInit();
	SceneInit();
	MemPush();
	SeqStep();
}

static void SeqCmdStageExit(void)
{
	ObjectInit();
	SceneExit();
	SceneInit();
	MemPull();
	SeqStep();
}

static void SeqCmdCompileBegin(void)
{
	if (!seq_arena) seq_arena = ArenaCreateFull();
	SeqStep();
}

static void SeqCmdCompileEnd(void)
{
	int i;
	ArenaShrink(seq_arena);
	seq_arena = NULL;
	for (i = 0; i < SCENE_MAX; i++)
	{
		if (scene_data[i].map)
		{
			MapInit();
			break;
		}
	}
	SeqStep();
}

static void SeqCmdSceneBegin(void)
{
	UCHAR i = SEQ_UCHAR[2];
	SHPLANG *script = SEQ_PTR[1];
	if (i < SCENE_MAX)
	{
		SSCENE *shp = (SSCENE *)ShpLangCompile(seq_arena, script);
		SCAMERA *cam = (SCAMERA *)shp->reftab[0];
		seq_scene = i;
		shp->index = i;
		scene_table[i].shp = shp;
		if (cam)    scene_table[i].cam = (CAMERA *)cam->s.arg;
		else        scene_table[i].cam = NULL;
	}
	SeqStep();
}

static void SeqCmdSceneEnd(void)
{
	seq_scene = -1;
	SeqStep();
}

static void SeqCmdShapeGfx(void)
{
	SHORT shape = SEQ_SHORT[1] & 0xFFF;
	SHORT layer = (unsigned short)SEQ_SHORT[1] >> 12;
	Gfx *gfx = SEQ_PTR[1];
	if (shape < SHAPE_MAX)
	{
		shape_table[shape] = &ShpCreateGfx(seq_arena, NULL, layer, gfx)->s;
	}
	SeqStep();
}

static void SeqCmdShape(void)
{
	SHORT shape = SEQ_SHORT[1];
	SHPLANG *script = SEQ_PTR[1];
	if (shape < SHAPE_MAX)
	{
		shape_table[shape] = ShpLangCompile(seq_arena, script);
	}
	SeqStep();
}

static void SeqCmdShapeScale(void)
{
	union {int i; float f;} scale;
	SHORT shape = SEQ_SHORT[1] & 0xFFF;
	SHORT layer = (unsigned short)SEQ_SHORT[1] >> 12;
	Gfx *gfx = SEQ_PTR[1];
	scale.i = SEQ_INT[2];
	if (shape < SHAPE_MAX)
	{
		shape_table[shape] =
			&ShpCreateScale(seq_arena, NULL, layer, gfx, scale.f)->s.s;
	}
	SeqStep();
}

static void SeqCmdPlayer(void)
{
	SVecSet(mario_actor->pos, 0, 0, 0);
	SVecSet(mario_actor->ang, 0, 0, 0);
	mario_actor->group = -1;
	mario_actor->scene = 0;
	mario_actor->info = SEQ_INT[1];
	mario_actor->script = SEQ_PTR[2];
	mario_actor->shape = shape_table[SEQ_UCHAR[3]];
	mario_actor->next = NULL;
	SeqStep();
}

static void SeqCmdObject(void)
{
	UCHAR mask = 1 << (level_index-1);
	if (seq_scene != -1)
	{
		if (SEQ_UCHAR[2] & mask || SEQ_UCHAR[2] == 037)
		{
			USHORT shape = SEQ_UCHAR[3];
			ACTOR *actor = ArenaAlloc(seq_arena, sizeof(ACTOR));
			actor->pos[0] = SEQ_SHORT[2];
			actor->pos[1] = SEQ_SHORT[3];
			actor->pos[2] = SEQ_SHORT[4];
			actor->ang[0] = DEG(SEQ_SHORT[5]);
			actor->ang[1] = DEG(SEQ_SHORT[6]);
			actor->ang[2] = DEG(SEQ_SHORT[7]);
			actor->scene = seq_scene;
			actor->group = seq_scene;
			actor->info = SEQ_INT[4];
			actor->script = SEQ_PTR[5];
			actor->shape = shape_table[shape];
			actor->next = scene_table[seq_scene].actor;
			scene_table[seq_scene].actor = actor;
		}
	}
	SeqStep();
}

static void SeqCmdPort(void)
{
	if (seq_scene != -1)
	{
		PORT *port = ArenaAlloc(seq_arena, sizeof(PORT));
		port->p.attr = SEQ_UCHAR[2];
		port->p.stage = SEQ_UCHAR[3] + SEQ_UCHAR[6];
		port->p.scene = SEQ_UCHAR[4];
		port->p.port = SEQ_UCHAR[5];
		port->obj = NULL;
		port->next = scene_table[seq_scene].port;
		scene_table[seq_scene].port = port;
	}
	SeqStep();
}

static void SeqCmdConnect(void)
{
	int i;
	CONNECT *connect;
	if (seq_scene != -1)
	{
		if (!scene_table[seq_scene].connect)
		{
			scene_table[seq_scene].connect =
				ArenaAlloc(seq_arena, sizeof(CONNECT)*CONNECT_MAX);
			for (i = 0; i < CONNECT_MAX; i++)
			{
				scene_table[seq_scene].connect[i].flag = FALSE;
			}
		}
		connect = &scene_table[seq_scene].connect[SEQ_UCHAR[2]];
		connect->flag = TRUE;
		connect->scene = SEQ_UCHAR[3];
		connect->offset[0] = SEQ_SHORT[2];
		connect->offset[1] = SEQ_SHORT[3];
		connect->offset[2] = SEQ_SHORT[4];
	}
	SeqStep();
}

static void SeqCmdEnv(void)
{
	if (seq_scene != -1)
	{
		scene_table[seq_scene].env |= SEQ_SHORT[1];
	}
	SeqStep();
}

static void SeqCmdBGPort(void)
{
	int i;
	BGPORT *bgport;
	if (seq_scene != -1)
	{
		if (!scene_table[seq_scene].bgport)
		{
			scene_table[seq_scene].bgport =
				ArenaAlloc(seq_arena, sizeof(BGPORT)*BGPORT_MAX);
			for (i = 0; i < BGPORT_MAX; i++)
			{
				scene_table[seq_scene].bgport[i].p.attr = FALSE;
			}
		}
		bgport = &scene_table[seq_scene].bgport[SEQ_UCHAR[2]];
		bgport->p.attr = TRUE;
		bgport->p.stage = SEQ_UCHAR[3] + SEQ_UCHAR[6];
		bgport->p.scene = SEQ_UCHAR[4];
		bgport->p.port = SEQ_UCHAR[5];
	}
	SeqStep();
}

static void SeqCmd58(void)
{
	SCENE28 *_28;
	if (seq_scene != -1)
	{
		if (!(_28 = scene_table[seq_scene]._28))
		{
			_28 = scene_table[seq_scene]._28 =
				ArenaAlloc(seq_arena, sizeof(SCENE28));
		}
		_28->_00 = SEQ_SHORT[1];
		_28->_02 = SEQ_SHORT[2];
		_28->_04 = SEQ_SHORT[3];
		_28->_06 = SEQ_SHORT[4];
		_28->_08 = SEQ_SHORT[5];
	}
	SeqStep();
}

static void SeqCmdJet(void)
{
	JET *jet;
	int index = SEQ_UCHAR[2];
	int flag = (BuGetFlag() & (BU_KEY2|BU_KEYDOOR2)) != 0;
	if (
		(SEQ_UCHAR[3] == 0) ||
		(SEQ_UCHAR[3] == 1 && !flag) ||
		(SEQ_UCHAR[3] == 2 && flag) ||
		(SEQ_UCHAR[3] == 3 && level_index > 1)
	)
	{
		if (seq_scene != -1)
		{
			if (index < 2)
			{
				if (!(jet = scene_table[seq_scene].jet[index]))
				{
					jet = ArenaAlloc(seq_arena, sizeof(JET));
					scene_table[seq_scene].jet[index] = jet;
				}
				SVecSet(jet->pos, SEQ_SHORT[2], SEQ_SHORT[3], SEQ_SHORT[4]);
				jet->attr = SEQ_SHORT[5];
			}
		}
	}
	SeqStep();
}

static void SeqCmdViBlack(void)
{
	osViBlack(SEQ_UCHAR[2]);
	SeqStep();
}

static void SeqCmdViGamma(void)
{
	osViSetSpecialFeatures(!SEQ_UCHAR[2] ? OS_VI_GAMMA_OFF : OS_VI_GAMMA_ON);
	SeqStep();
}

static void SeqCmdMap(void)
{
	if (seq_scene != -1)
	{
		scene_table[seq_scene].map = SegmentToVirtual(SEQ_PTR[1]);
	}
	SeqStep();
}

static void SeqCmdArea(void)
{
	if (seq_scene != -1)
	{
		scene_table[seq_scene].area = SegmentToVirtual(SEQ_PTR[1]);
	}
	SeqStep();
}

static void SeqCmdTag(void)
{
	if (seq_scene != -1)
	{
		scene_table[seq_scene].tag = SegmentToVirtual(SEQ_PTR[1]);
	}
	SeqStep();
}

static void SeqCmdSceneOpen(void)
{
	SHORT index = SEQ_UCHAR[2];
	UNUSED void *sp18 = seq_pc + 4;
	Na_SeClear();
	SceneOpen(index);
	SeqStep();
}

static void SeqCmdSceneClose(void)
{
	SceneClose();
	SeqStep();
}

static void SeqCmdPlayerOpen(void)
{
	mario_actor->scene = SEQ_UCHAR[2];
	SVecCpy(mario_actor->pos, SEQ_SHORT+3);
	SVecSet(mario_actor->ang, 0, DEG(SEQ_SHORT[2]), 0);
	SeqStep();
}

static void SeqCmdPlayerClose(void)
{
	SnClosePlayer();
	SeqStep();
}

static void SeqCmdSceneProc(void)
{
	SceneProc();
	SeqStep();
}

static void SeqCmdWipe(void)
{
	if (scenep) SnWipe(
		SEQ_UCHAR[2], SEQ_UCHAR[3], SEQ_UCHAR[4], SEQ_UCHAR[5], SEQ_UCHAR[6]
	);
	SeqStep();
}

static void SeqCmd50(void)
{
	debugf(("BAD: seqBlankColor\n"));
	SeqStep();
}

static void SeqCmdMessage(void)
{
	if (seq_scene != -1)
	{
		if (SEQ_UCHAR[2] < 2)
		{
			scene_table[seq_scene].msg[SEQ_UCHAR[2]] = SEQ_UCHAR[3];
		}
	}
	SeqStep();
}

static void SeqCmdBGM(void)
{
	if (seq_scene != -1)
	{
		scene_table[seq_scene].bgm_mode = SEQ_SHORT[1];
		scene_table[seq_scene].bgm = SEQ_SHORT[2];
	}
	SeqStep();
}

static void SeqCmdPlayBGM(void)
{
	AudPlayBGM(0, SEQ_SHORT[1], 0);
	SeqStep();
}

static void SeqCmdAudFadeout(void)
{
	AudFadeout(SEQ_SHORT[1]);
	SeqStep();
}

static void SeqCmdVar(void)
{
	if (SEQ_UCHAR[2] == 0)
	{
		switch (SEQ_UCHAR[3])
		{
		case SEQ_VAR_FILE:    file_index      = seq_status; break;
		case SEQ_VAR_COURSE:  course_index    = seq_status; break;
		case SEQ_VAR_LEVEL:   level_index     = seq_status; break;
		case SEQ_VAR_STAGE:   stage_index     = seq_status; break;
		case SEQ_VAR_SCENE:   scene_index     = seq_status; break;
		}
	}
	else
	{
		switch (SEQ_UCHAR[3])
		{
		case SEQ_VAR_FILE:    seq_status = file_index;      break;
		case SEQ_VAR_COURSE:  seq_status = course_index;    break;
		case SEQ_VAR_LEVEL:   seq_status = level_index;     break;
		case SEQ_VAR_STAGE:   seq_status = stage_index;     break;
		case SEQ_VAR_SCENE:   seq_status = scene_index;     break;
		}
	}
	SeqStep();
}

static void (*seq_cmdtab[])(void) =
{
	SeqCmdExecute,
	SeqCmdChain,
	SeqCmdExit,
	SeqCmdSleep,
	SeqCmdFreeze,
	SeqCmdJump,
	SeqCmdCall,
	SeqCmdReturn,
	SeqCmdFor,
	SeqCmdDone,
	SeqCmdRepeat,
	SeqCmdUntil,
	SeqCmdJumpIf,
	SeqCmdCallIf,
	SeqCmdIf,
	SeqCmdElse,
	SeqCmdEndif,
	SeqCmdCallback,
	SeqCmdProcess,
	SeqCmdSet,
	SeqCmdPush,
	SeqCmdPull,
	SeqCmdLoadCode,
	SeqCmdLoadData,
	SeqCmdLoadPres,
	SeqCmdLoadFace,
	SeqCmdLoadText,
	SeqCmdStageInit,
	SeqCmdStageExit,
	SeqCmdCompileBegin,
	SeqCmdCompileEnd,
	SeqCmdSceneBegin,
	SeqCmdSceneEnd,
	SeqCmdShapeGfx,
	SeqCmdShape,
	SeqCmdShapeScale,
	SeqCmdObject,
	SeqCmdPlayer,
	SeqCmdPort,
	SeqCmdBGPort,
	SeqCmdConnect,
	SeqCmdSceneOpen,
	SeqCmdSceneClose,
	SeqCmdPlayerOpen,
	SeqCmdPlayerClose,
	SeqCmdSceneProc,
	SeqCmdMap,
	SeqCmdArea,
	SeqCmdMessage,
	SeqCmdEnv,
	SeqCmd50,
	SeqCmdWipe,
	SeqCmdViBlack,
	SeqCmdViGamma,
	SeqCmdBGM,
	SeqCmdPlayBGM,
	SeqCmdAudFadeout,
	SeqCmdTag,
	SeqCmd58,
	SeqCmdJet,
	SeqCmdVar,
};

SEQLANG *SeqExec(SEQLANG *pc)
{
	seq_state = 1;
	seq_pc = pc;
	while (seq_state == 1)
	{
		debugf(("%08X: ", seq_pc));
		debugf(("%02d\n", SEQ_CMD));
		seq_cmdtab[SEQ_CMD]();
	}
	TimeGfxCPU(TIME_GFXCPU_ENDPRC);
	GfxBegin();
	SceneDraw();
	GfxEnd();
	GfxAlloc(0);
	return seq_pc;
}
