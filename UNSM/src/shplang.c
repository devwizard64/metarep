#include <sm64.h>

#define SHP_UCHAR       ((unsigned char *)shp_pc)
#define SHP_SHORT       ((short *)shp_pc)
#define SHP_USHORT      ((unsigned short *)shp_pc)
#define SHP_INT         ((int *)shp_pc)
#define SHP_UINT        ((unsigned int *)shp_pc)
#define SHP_PTR         ((void **)shp_pc)
#define SHP_CALL        ((SHPCALL **)shp_pc)

#define SHP_CMD         SHP_UCHAR[0]

static ARENA *shp_arena;
static SHAPE *shape_root;
UNUSED static SHAPE *shape_8038BCA8;
static SHAPE **shape_reftab;
static u16 shape_reflen;
static unsigned long shp_stack[16];
static SHAPE *shape_stack[32];
static s16 shape_sp;
static s16 shp_sp;
UNUSED static s16 shape_fp;
static s16 shp_fp;
static SHPLANG *shp_pc;

SHAPE sobj_list;

static short *ShpGetFVec(FVEC dst, short *src)
{
	dst[0] = *src++;
	dst[1] = *src++;
	dst[2] = *src++;
	return src;
}

static short *ShpGetSVec(SVEC dst, short *src)
{
	dst[0] = *src++;
	dst[1] = *src++;
	dst[2] = *src++;
	return src;
}

static short *ShpGetAng(SVEC dst, short *src)
{
	dst[0] = *src++ * 0x8000/180;
	dst[1] = *src++ * 0x8000/180;
	dst[2] = *src++ * 0x8000/180;
	return src;
}

static void ShapeLink(SHAPE *shape)
{
	if (shape)
	{
		shape_stack[shape_sp] = shape;
		if (shape_sp == 0)
		{
			if (!shape_root) shape_root = shape;
		}
		else if (shape_stack[shape_sp-1]->type == ST_BRANCH)
		{
			((SBRANCH *)shape_stack[shape_sp-1])->shape = shape;
		}
		else
		{
			ShpLink(shape_stack[shape_sp-1], shape);
		}
	}
}

static void ShpCmdExecute(void)
{
	shp_stack[shp_sp++] = (unsigned long)(shp_pc+2);
	shp_stack[shp_sp++] = (shape_sp << 16) + shp_fp;
	shp_fp = shp_sp;
	shp_pc = SegmentToVirtual(SHP_PTR[1]);
}

static void ShpCmdExit(void)
{
	shp_sp = shp_fp;
	shp_fp = shp_stack[--shp_sp] & 0xFFFF;
	shape_sp = shp_stack[shp_sp] >> 16;
	shp_pc = (void *)shp_stack[--shp_sp];
}

static void ShpCmdJump(void)
{
	if (SHP_UCHAR[1] == 1) shp_stack[shp_sp++] = (unsigned long)(shp_pc+2);
	shp_pc = SegmentToVirtual(SHP_PTR[1]);
}

static void ShpCmdReturn(void)
{
	shp_pc = (void *)shp_stack[--shp_sp];
}

static void ShpCmdStart(void)
{
	shape_stack[shape_sp+1] = shape_stack[shape_sp];
	shape_sp++;
	shp_pc += 1;
}

static void ShpCmdEnd(void)
{
	shape_sp--;
	shp_pc += 1;
}

static void ShpCmdStore(void)
{
	USHORT index = SHP_SHORT[1];
	if (index < shape_reflen) shape_reftab[index] = shape_stack[shape_sp];
	shp_pc += 1;
}

static void ShpCmdFlag(void)
{
	USHORT mode = SHP_UCHAR[1];
	u16 flag = SHP_SHORT[1];
	switch (mode)
	{
	case 0: shape_stack[shape_sp]->flag = flag; break;
	case 1: shape_stack[shape_sp]->flag |= flag; break;
	case 2: shape_stack[shape_sp]->flag &= ~flag; break;
	}
	shp_pc += 1;
}

static void ShpCmdScene(void)
{
	int i;
	SSCENE *shp;
	SHORT x = SHP_SHORT[2];
	SHORT y = SHP_SHORT[3];
	SHORT w = SHP_SHORT[4];
	SHORT h = SHP_SHORT[5];
	shape_reflen = SHP_SHORT[1] + 2;
	shp = ShpCreateScene(shp_arena, NULL, 0, x, y, w, h);
	shape_reftab = ArenaAlloc(shp_arena, sizeof(SHAPE *)*shape_reflen);
	shp->reftab = shape_reftab;
	shp->reflen = shape_reflen;
	for (i = 0; i < shape_reflen; i++) shape_reftab[i] = NULL;;
	ShapeLink(&shp->s);
	shp_pc += 3;
}

static void ShpCmdOrtho(void)
{
	SORTHO *shp;
	float scale = (float)SHP_SHORT[1] / 100;
	shp = ShpCreateOrtho(shp_arena, NULL, scale);
	ShapeLink(&shp->s);
	shp_pc += 1;
}

static void ShpCmdPersp(void)
{
	SPERSP *shp;
	SHPCALL *callback = NULL;
	SHORT fovy = SHP_SHORT[1];
	SHORT near = SHP_SHORT[2];
	SHORT far = SHP_SHORT[3];
	if (SHP_UCHAR[1])
	{
		callback = SHP_CALL[2];
		shp_pc += 1;
	}
	shp = ShpCreatePersp(shp_arena, NULL, fovy, near, far, callback, 0);
	ShapeLink(&shp->s.s);
	shp_pc += 2;
}

static void ShpCmdEmpty(void)
{
	SHAPE *shape;
	shape = ShpCreateEmpty(shp_arena, NULL);
	ShapeLink(shape);
	shp_pc += 1;
}

static void ShpCmd31(void)
{
	shp_pc += 4;
}

static void ShpCmdLayer(void)
{
	SLAYER *shp;
	shp = ShpCreateLayer(shp_arena, NULL, SHP_UCHAR[1]);
	ShapeLink(&shp->s);
	shp_pc += 1;
}

static void ShpCmdLOD(void)
{
	SLOD *shp;
	SHORT min = SHP_SHORT[2];
	SHORT max = SHP_SHORT[3];
	shp = ShpCreateLOD(shp_arena, NULL, min, max);
	ShapeLink(&shp->s);
	shp_pc += 2;
}

static void ShpCmdSelect(void)
{
	SSELECT *shp;
	shp = ShpCreateSelect(shp_arena, NULL, SHP_SHORT[1], 0, SHP_CALL[1], 0);
	ShapeLink(&shp->s.s);
	shp_pc += 2;
}

static void ShpCmdCamera(void)
{
	SCAMERA *shp;
	void *pc = SHP_SHORT+2;
	FVEC eye, look;
	pc = ShpGetFVec(eye, pc);
	pc = ShpGetFVec(look, pc);
	shp = ShpCreateCamera(
		shp_arena, NULL, eye, look, SHP_CALL[4], SHP_SHORT[1]
	);
	ShapeLink(&shp->s.s);
	shape_reftab[0] = &shp->s.s;
	shp_pc += 5;
}

static void ShpCmdCoord(void)
{
	SCOORD *shp;
	SVEC pos, ang;
	Gfx *gfx = NULL;
	SHORT layer = 0;
	SHORT flag = SHP_UCHAR[1];
	void *pc = shp_pc;
	switch ((flag & 0x70) >> 4)
	{
	case 0:
		pc = ShpGetSVec(pos, (short *)pc+2);
		pc = ShpGetAng(ang, pc);
		break;
	case 1:
		pc = ShpGetSVec(pos, (short *)pc+1);
		SVecCpy(ang, svec_0);
		break;
	case 2:
		pc = ShpGetAng(ang, (short *)pc+1);
		SVecCpy(pos, svec_0);
		break;
	case 3:
		SVecCpy(pos, svec_0);
		SVecSet(ang, 0, ((short *)pc)[1] * 0x8000/180, 0);
		pc = (SHPLANG *)pc + 1;
		break;
	}
	if (flag & 0x80)
	{
		gfx = *(void **)pc;
		layer = flag & 15;
		pc = (SHPLANG *)pc + 1;
	}
	shp = ShpCreateCoord(shp_arena, NULL, layer, gfx, pos, ang);
	ShapeLink(&shp->s.s);
	shp_pc = pc;
}

static void ShpCmdPos(void)
{
	SPOS *shp;
	SVEC pos;
	SHORT layer = 0;
	SHORT flag = SHP_UCHAR[1];
	void *pc = shp_pc;
	Gfx *gfx = NULL;
	pc = ShpGetSVec(pos, (short *)pc+1);
	if (flag & 0x80)
	{
		gfx = *(void **)pc;
		layer = flag & 15;
		pc = (SHPLANG *)pc + 1;
	}
	shp = ShpCreatePos(shp_arena, NULL, layer, gfx, pos);
	ShapeLink(&shp->s.s);
	shp_pc = pc;
}

static void ShpCmdAng(void)
{
	SANG *shp;
	SVEC ang;
	SHORT layer = 0;
	SHORT flag = SHP_UCHAR[1];
	void *pc = shp_pc;
	Gfx *gfx = NULL;
	pc = ShpGetAng(ang, (short *)pc+1);
	if (flag & 0x80)
	{
		gfx = *(void **)pc;
		layer = flag & 15;
		pc = (SHPLANG *)pc + 1;
	}
	shp = ShpCreateAng(shp_arena, NULL, layer, gfx, ang);
	ShapeLink(&shp->s.s);
	shp_pc = pc;
}

static void ShpCmdScale(void)
{
	SSCALE *shp;
	SHORT layer = 0;
	SHORT flag = SHP_UCHAR[1];
	float scale = (float)SHP_UINT[1] / 0x10000;
	Gfx *gfx = NULL;
	if (flag & 0x80)
	{
		gfx = SHP_PTR[2];
		layer = flag & 15;
		shp_pc += 1;
	}
	shp = ShpCreateScale(shp_arena, NULL, layer, gfx, scale);
	ShapeLink(&shp->s.s);
	shp_pc += 2;
}

static void ShpCmd30(void)
{
	shp_pc += 2;
}

static void ShpCmdJoint(void)
{
	SJOINT *shp;
	SVEC pos;
	int layer = SHP_UCHAR[1];
	Gfx *gfx = SHP_PTR[2];
	void *pc = shp_pc;
	ShpGetSVec(pos, (short *)pc+1);
	shp = ShpCreateJoint(shp_arena, NULL, layer, gfx, pos);
	ShapeLink(&shp->s.s);
	shp_pc += 3;
}

static void ShpCmdBillboard(void)
{
	SBILLBOARD *shp;
	SVEC pos;
	SHORT layer = 0;
	SHORT flag = SHP_UCHAR[1];
	void *pc = shp_pc;
	Gfx *gfx = NULL;
	pc = ShpGetSVec(pos, (short *)pc+1);
	if (flag & 0x80)
	{
		gfx = *(void **)pc;
		layer = flag & 15;
		pc = (SHPLANG *)pc + 1;
	}
	shp = ShpCreateBillboard(shp_arena, NULL, layer, gfx, pos);
	ShapeLink(&shp->s.s);
	shp_pc = pc;
}

static void ShpCmdGfx(void)
{
	SGFX *shp;
	int layer = SHP_UCHAR[1];
	Gfx *gfx = SHP_PTR[1];
	shp = ShpCreateGfx(shp_arena, NULL, layer, gfx);
	ShapeLink(&shp->s);
	shp_pc += 2;
}

static void ShpCmdShadow(void)
{
	SSHADOW *shp;
	UCHAR type = SHP_SHORT[1];
	UCHAR alpha = SHP_SHORT[2];
	SHORT size = SHP_SHORT[3];
	shp = ShpCreateShadow(shp_arena, NULL, size, alpha, type);
	ShapeLink(&shp->s);
	shp_pc += 2;
}

static void ShpCmdObject(void)
{
	SBRANCH *shp;
	shp = ShpCreateBranch(shp_arena, NULL, &sobj_list);
	ShapeLink(&shp->s);
	shp_pc += 1;
}

static void ShpCmdCallback(void)
{
	SCALLBACK *shp;
	shp = ShpCreateCallback(shp_arena, NULL, SHP_CALL[1], SHP_SHORT[1]);
	ShapeLink(&shp->s);
	shp_pc += 2;
}

static void ShpCmdBack(void)
{
	SBACK *shp;
	shp = ShpCreateBack(shp_arena, NULL, SHP_SHORT[1], SHP_CALL[1], 0);
	ShapeLink(&shp->s.s);
	shp_pc += 2;
}

static void ShpCmd26(void)
{
	shp_pc += 2;
}

static void ShpCmdBranch(void)
{
	SBRANCH *shp;
	SHAPE *shape = NULL;
	SHORT index = SHP_SHORT[1];
	if (index >= 0)
	{
		shape = shape_reftab[index];
		if (shape->type == ST_BRANCH)   shape = ((SBRANCH *)shape)->shape;
		else                            shape = NULL;
	}
	shp = ShpCreateBranch(shp_arena, NULL, shape);
	ShapeLink(&shp->s);
	shp_pc += 1;
}

static void ShpCmdHand(void)
{
	SHAND *shp;
	SVEC pos;
	ShpGetSVec(pos, SHP_SHORT+1);
	shp = ShpCreateHand(shp_arena, NULL, NULL, pos, SHP_CALL[2], SHP_UCHAR[1]);
	ShapeLink(&shp->s.s);
	shp_pc += 3;
}

static void ShpCmdCull(void)
{
	SCULL *shp;
	shp = ShpCreateCull(shp_arena, NULL, SHP_SHORT[1]);
	ShapeLink(&shp->s);
	shp_pc += 1;
}

static void (*shp_cmdtab[])(void) =
{
	ShpCmdExecute,
	ShpCmdExit,
	ShpCmdJump,
	ShpCmdReturn,
	ShpCmdStart,
	ShpCmdEnd,
	ShpCmdStore,
	ShpCmdFlag,
	ShpCmdScene,
	ShpCmdOrtho,
	ShpCmdPersp,
	ShpCmdEmpty,
	ShpCmdLayer,
	ShpCmdLOD,
	ShpCmdSelect,
	ShpCmdCamera,
	ShpCmdCoord,
	ShpCmdPos,
	ShpCmdAng,
	ShpCmdJoint,
	ShpCmdBillboard,
	ShpCmdGfx,
	ShpCmdShadow,
	ShpCmdObject,
	ShpCmdCallback,
	ShpCmdBack,
	ShpCmd26,
	ShpCmdBranch,
	ShpCmdHand,
	ShpCmdScale,
	ShpCmd30,
	ShpCmd31,
	ShpCmdCull,
};

SHAPE *ShpLangCompile(ARENA *arena, SHPLANG *script)
{
	shape_root = NULL;
	shape_reflen = 0;
	shape_stack[0] = NULL;
	shape_sp = 0;
	shp_sp = 2;
	shp_fp = 2;
	shp_pc = SegmentToVirtual(script);
	shp_arena = arena;
	shp_stack[0] = 0;
	shp_stack[1] = 0;
	while (shp_pc) shp_cmdtab[SHP_CMD]();
	return shape_root;
}
