import main

sym_J0_E0_ulib_text = {
	# ==========================================================================
	# text
	# ==========================================================================

	# src/math.c
	0x80378800: main.sym_fnc("FVecCpy", "float *", (
		"FVEC dst",
		"FVEC src",
	), flag={"GLOBL"}),
	0x80378840: main.sym_fnc("FVecSet", "float *", (
		"FVEC v",
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}),
	0x8037888C: main.sym_fnc("FVecAdd", "float *", (
		"FVEC v",
		"FVEC a",
	), flag={"GLOBL"}),
	0x803788E4: main.sym_fnc("FVecAddTo", "float *", (
		"FVEC v",
		"FVEC a",
		"FVEC b",
	), flag={"GLOBL"}), # unused
	0x8037893C: main.sym_fnc("SVecCpy", "short *", (
		"SVEC dst",
		"SVEC src",
	), flag={"GLOBL"}),
	0x8037897C: main.sym_fnc("SVecSet", "short *", (
		"SVEC v",
		"SHORT x",
		"SHORT y",
		"SHORT z",
	), flag={"GLOBL"}),
	0x803789C8: main.sym_fnc("SVecAdd", "short *", (
		"SVEC v",
		"SVEC a",
	), flag={"GLOBL"}), # unused
	0x80378A20: main.sym_fnc("SVecAddTo", "short *", (
		"SVEC v",
		"SVEC a",
		"SVEC b",
	), flag={"GLOBL"}), # unused
	0x80378A78: main.sym_fnc("SVecSub", "short *", (
		"SVEC v",
		"SVEC a",
	), flag={"GLOBL"}), # unused
	0x80378AD0: main.sym_fnc("SVecToFVec", "float *", (
		"FVEC dst",
		"SVEC src",
	), flag={"GLOBL"}),
	0x80378B34: main.sym_fnc("FVecToSVec", "short *", (
		"SVEC dst",
		"FVEC src",
	), flag={"GLOBL"}),
	0x80378C50: main.sym_fnc("CalcNormal", "float *", (
		"FVEC v",
		"FVEC v0",
		"FVEC v1",
		"FVEC v2",
	), flag={"GLOBL"}), # static
	0x80378D38: main.sym_fnc("CrossProduct", "float *", (
		"FVEC v",
		"FVEC a",
		"FVEC b",
	), flag={"GLOBL"}), # static
	0x80378DC0: main.sym_fnc("Normalize", "float *", (
		"FVEC v",
	), flag={"GLOBL"}), # static
	0x80378E68: main.sym_fnc("FMtxCpy", arg=(
		"FMTX dst",
		"FMTX src",
	), flag={"GLOBL"}),
	0x80378EB4: main.sym_fnc("FMtxIdent", arg=(
		"FMTX m",
	), flag={"GLOBL"}),
	0x80378F24: main.sym_fnc("FMtxPos", arg=(
		"FMTX m",
		"FVEC pos",
	), flag={"GLOBL"}),
	0x80378F84: main.sym_fnc("FMtxLookAt", arg=(
		"FMTX m",
		"FVEC eye",
		"FVEC look",
		"SHORT angz",
	), flag={"GLOBL"}),
	0x80379440: main.sym_fnc("FMtxCoord", arg=(
		"FMTX m",
		"FVEC pos",
		"SVEC ang",
	), flag={"GLOBL"}),
	0x803795F0: main.sym_fnc("FMtxJoint", arg=(
		"FMTX m",
		"FVEC pos",
		"SVEC ang",
	), flag={"GLOBL"}),
	0x80379798: main.sym_fnc("FMtxBillboard", arg=(
		"FMTX dst",
		"FMTX src",
		"FVEC pos",
		"SHORT angz",
	), flag={"GLOBL"}),
	0x80379918: main.sym_fnc("FMtxStand", arg=(
		"FMTX m",
		"FVEC vy",
		"FVEC pos",
		"SHORT angy",
	), flag={"GLOBL"}),
	0x80379AA4: main.sym_fnc("FMtxGround", arg=(
		"FMTX m",
		"FVEC pos",
		"SHORT angy",
		"float radius",
	), flag={"GLOBL"}),
	0x80379F60: main.sym_fnc("FMtxCatAffine", arg=(
		"FMTX m",
		"FMTX a",
		"FMTX b",
	), flag={"GLOBL"}),
	0x8037A29C: main.sym_fnc("FMtxScale", arg=(
		"FMTX dst",
		"FMTX src",
		"FVEC scale",
	), flag={"GLOBL"}),
	0x8037A348: main.sym_fnc("Transform", arg=(
		"FMTX m",
		"SVEC v",
	), flag={"GLOBL"}), # unused
	0x8037A434: main.sym_fnc("FMtxToMtx", arg=(
		"Mtx *m",
		"FMTX mf",
	), flag={"GLOBL"}),
	0x8037A4B8: main.sym_fnc("MtxAngZ", arg=(
		"Mtx *m",
		"SHORT angz",
	), flag={"GLOBL"}),
	0x8037A550: main.sym_fnc("CalcScenePos", arg=(
		"FVEC v",
		"FMTX m",
		"FMTX cam",
	), flag={"GLOBL"}),
	0x8037A69C: main.sym_fnc("CartesianToPolar", arg=(
		"FVEC a",
		"FVEC b",
		"float *dist",
		"short *angx",
		"short *angy",
	), flag={"GLOBL"}),
	0x8037A788: main.sym_fnc("PolarToCartesian", arg=(
		"FVEC a",
		"FVEC b",
		"float dist",
		"SHORT angx",
		"SHORT angy",
	), flag={"GLOBL"}),
	0x8037A860: main.sym_fnc("ConvergeI", "int", (
		"int x",
		"int dst",
		"int inc",
		"int dec",
	), flag={"GLOBL"}),
	0x8037A8B4: main.sym_fnc("ConvergeF", "float", (
		"float x",
		"float dst",
		"float inc",
		"float dec",
	), flag={"GLOBL"}),
	0x8037A924: main.sym_fnc("AtanRef", "USHORT", (
		"float y",
		"float x",
	)),
	0x8037A9A8: main.sym_fnc("ATAN2", "short", (
		"float y",
		"float x",
	), flag={"GLOBL"}),
	0x8037AB88: main.sym_fnc("ATAN2F", "float", (
		"float y",
		"float x",
	), flag={"GLOBL"}), # unused
	0x8037ABEC: main.sym_fnc("BSplineCurve", arg=(
		"float curve[4]",
		"float phase",
		"int mode",
	)),
	0x8037AC74: main.sym_fnc("L8037AC74", flag={"GLOBL","LOCAL"}),
	0x8037AD04: main.sym_fnc("L8037AD04", flag={"GLOBL","LOCAL"}),
	0x8037ADC0: main.sym_fnc("L8037ADC0", flag={"GLOBL","LOCAL"}),
	0x8037AE5C: main.sym_fnc("L8037AE5C", flag={"GLOBL","LOCAL"}),
	0x8037AF18: main.sym_fnc("L8037AF18", flag={"GLOBL","LOCAL"}),
	0x8037AFB8: main.sym_fnc("BSplineInit", arg=(
		"BSPLINE *b",
	), flag={"GLOBL"}),
	0x8037AFE8: main.sym_fnc("BSplineProc", "int", (
		"FVEC dst",
	), flag={"GLOBL"}),

	# src/shape.c
	0x8037B220: main.sym_fnc("ShpInit", arg=(
		"SHAPE *shape",
		"int type",
	)),
	0x8037B24C: main.sym_fnc("ShpCreateScene", "SSCENE *", (
		"ARENA *arena",
		"SSCENE *shp",
		"SHORT index",
		"SHORT x",
		"SHORT y",
		"SHORT w",
		"SHORT h",
	), flag={"GLOBL"}),
	0x8037B30C: main.sym_fnc("ShpCreateOrtho", "SORTHO *", (
		"ARENA *arena",
		"SORTHO *shp",
		"float scale",
	), flag={"GLOBL"}),
	0x8037B380: main.sym_fnc("ShpCreatePersp", "SPERSP *", (
		"ARENA *arena",
		"SPERSP *shp",
		"float fovy",
		"SHORT near",
		"SHORT far",
		"SHPCALL *callback",
		"unsigned long arg",
	), flag={"GLOBL"}),
	0x8037B448: main.sym_fnc("ShpCreateEmpty", "SHAPE *", (
		"ARENA *arena",
		"SHAPE *shp",
	), flag={"GLOBL"}),
	0x8037B4AC: main.sym_fnc("ShpCreateLayer", "SLAYER *", (
		"ARENA *arena",
		"SLAYER *shp",
		"SHORT zb",
	), flag={"GLOBL"}),
	0x8037B530: main.sym_fnc("ShpCreateLOD", "SLOD *", (
		"ARENA *arena",
		"SLOD *shp",
		"SHORT min",
		"SHORT max",
	), flag={"GLOBL"}),
	0x8037B5B4: main.sym_fnc("ShpCreateSelect", "SSELECT *", (
		"ARENA *arena",
		"SSELECT *shp",
		"SHORT code",
		"SHORT index",
		"SHPCALL *callback",
		"unsigned long arg",
	), flag={"GLOBL"}),
	0x8037B670: main.sym_fnc("ShpCreateCamera", "SCAMERA *", (
		"ARENA *arena",
		"SCAMERA *shp",
		"FVEC eye",
		"FVEC look",
		"SHPCALL *callback",
		"unsigned long arg",
	), flag={"GLOBL"}),
	0x8037B744: main.sym_fnc("ShpCreateCoord", "SCOORD *", (
		"ARENA *arena",
		"SCOORD *shp",
		"int layer",
		"Gfx *gfx",
		"SVEC pos",
		"SVEC ang",
	), flag={"GLOBL"}),
	0x8037B7F8: main.sym_fnc("ShpCreatePos", "SPOS *", (
		"ARENA *arena",
		"SPOS *shp",
		"int layer",
		"Gfx *gfx",
		"SVEC pos",
	), flag={"GLOBL"}),
	0x8037B89C: main.sym_fnc("ShpCreateAng", "SANG *", (
		"ARENA *arena",
		"SANG *shp",
		"int layer",
		"Gfx *gfx",
		"SVEC ang",
	), flag={"GLOBL"}),
	0x8037B940: main.sym_fnc("ShpCreateScale", "SSCALE *", (
		"ARENA *arena",
		"SSCALE *shp",
		"int layer",
		"Gfx *gfx",
		"float scale",
	), flag={"GLOBL"}),
	0x8037B9E0: main.sym_fnc("ShpCreateObject", "SOBJECT *", (
		"ARENA *arena",
		"SOBJECT *shp",
		"SHAPE *shape",
		"FVEC pos",
		"SVEC ang",
		"FVEC scale",
	), flag={"GLOBL"}),
	0x8037BAD4: main.sym_fnc("ShpCreateCull", "SCULL *", (
		"ARENA *arena",
		"SCULL *shp",
		"SHORT dist",
	), flag={"GLOBL"}),
	0x8037BB48: main.sym_fnc("ShpCreateJoint", "SJOINT *", (
		"ARENA *arena",
		"SJOINT *shp",
		"int layer",
		"Gfx *gfx",
		"SVEC pos",
	), flag={"GLOBL"}),
	0x8037BBEC: main.sym_fnc("ShpCreateBillboard", "SBILLBOARD *", (
		"ARENA *arena",
		"SBILLBOARD *shp",
		"int layer",
		"Gfx *gfx",
		"SVEC pos",
	), flag={"GLOBL"}),
	0x8037BC90: main.sym_fnc("ShpCreateGfx", "SGFX *", (
		"ARENA *arena",
		"SGFX *shp",
		"int layer",
		"Gfx *gfx",
	), flag={"GLOBL"}),
	0x8037BD24: main.sym_fnc("ShpCreateShadow", "SSHADOW *", (
		"ARENA *arena",
		"SSHADOW *shp",
		"SHORT size",
		"UCHAR alpha",
		"UCHAR type",
	), flag={"GLOBL"}),
	0x8037BDB4: main.sym_fnc("ShpCreateBranch", "SBRANCH *", (
		"ARENA *arena",
		"SBRANCH *shp",
		"SHAPE *shape",
	), flag={"GLOBL"}),
	0x8037BE28: main.sym_fnc("ShpCreateCallback", "SCALLBACK *", (
		"ARENA *arena",
		"SCALLBACK *shp",
		"SHPCALL *callback",
		"unsigned long arg",
	), flag={"GLOBL"}),
	0x8037BECC: main.sym_fnc("ShpCreateBack", "SBACK *", (
		"ARENA *arena",
		"SBACK *shp",
		"USHORT code",
		"SHPCALL *callback",
		"unsigned long arg",
	), flag={"GLOBL"}),
	0x8037BF84: main.sym_fnc("ShpCreateHand", "SHAND *", (
		"ARENA *arena",
		"SHAND *shp",
		"SOBJECT *obj",
		"SVEC pos",
		"SHPCALL *callback",
		"unsigned long arg",
	), flag={"GLOBL"}),
	0x8037C044: main.sym_fnc("ShpLink", "SHAPE *", (
		"SHAPE *parent",
		"SHAPE *shape",
	), flag={"GLOBL"}),
	0x8037C0BC: main.sym_fnc("ShpUnlink", "SHAPE *", (
		"SHAPE *shape",
	), flag={"GLOBL"}),
	0x8037C138: main.sym_fnc("ShpMakeFirst", "SHAPE *", (
		"SHAPE *shape",
	), flag={"GLOBL"}),
	0x8037C1E4: main.sym_fnc("ShpNotify", arg=(
		"SHAPE *shape",
		"int code",
	)),
	0x8037C360: main.sym_fnc("SSceneNotify", arg=(
		"SSCENE *shp",
		"int code",
	), flag={"GLOBL"}),
	0x8037C3D0: main.sym_fnc("SObjInit", arg=(
		"SOBJECT *shp",
	), flag={"GLOBL"}),
	0x8037C448: main.sym_fnc("SObjEnter", arg=(
		"SOBJECT *shp",
		"SHAPE *shape",
		"FVEC pos",
		"SVEC ang",
	), flag={"GLOBL"}),
	0x8037C51C: main.sym_fnc("SObjActor", arg=(
		"SOBJECT *shp",
		"ACTOR *actor",
	), flag={"GLOBL"}),
	0x8037C658: main.sym_fnc("SObjSetAnime", arg=(
		"SOBJECT *shp",
		"ANIME **animep",
	), flag={"GLOBL"}),
	0x8037C708: main.sym_fnc("SObjSetAnimeV", arg=(
		"SOBJECT *shp",
		"ANIME **animep",
		"int speed",
	), flag={"GLOBL"}),
	0x8037C7D8: main.sym_fnc("AnimeIndex", "int", (
		"int frame",
		"u16 **tbl",
	), flag={"GLOBL"}),
	0x8037C844: main.sym_fnc("SkelStep", "int", (
		"SKELETON *skel",
		"s32 *vframe",
	), flag={"GLOBL"}),
	0x8037C9E8: main.sym_fnc("SObjGetAnimePos", arg=(
		"SOBJECT *shp",
		"FVEC pos",
	)), # unused
	0x8037CB10: main.sym_fnc("ShpGetScene", "SSCENE *", (
		"SHAPE *shape",
	)), # unused

	# src/shplang.c
	0x8037CB60: main.sym_fnc("ShpLangReadFVec", "short *", (
		"FVEC dst",
		"short *src",
	)),
	0x8037CBC0: main.sym_fnc("ShpLangReadSVec", "short *", (
		"SVEC dst",
		"short *src",
	)),
	0x8037CBFC: main.sym_fnc("ShpLangReadAng", "short *", (
		"SVEC dst",
		"short *src",
	)),
	0x8037CC74: main.sym_fnc("ShpLangLink", arg=(
		"SHAPE *shape",
	)),
	0x8037CD60: main.sym_fnc("ShpCmdExecute"), # data
	0x8037CE24: main.sym_fnc("ShpCmdExit"), # data
	0x8037CEE8: main.sym_fnc("ShpCmdJump"), # data
	0x8037CF70: main.sym_fnc("ShpCmdReturn"), # data
	0x8037CFC0: main.sym_fnc("ShpCmdStart"), # data
	0x8037D018: main.sym_fnc("ShpCmdEnd"), # data
	0x8037D050: main.sym_fnc("ShpCmdStore"), # data
	0x8037D0D0: main.sym_fnc("ShpCmdFlag"), # data
	0x8037D1D0: main.sym_fnc("ShpCmdScene"), # data
	0x8037D328: main.sym_fnc("ShpCmdOrtho"), # data
	0x8037D3A4: main.sym_fnc("ShpCmdPersp"), # data
	0x8037D48C: main.sym_fnc("ShpCmdEmpty"), # data
	0x8037D4DC: main.sym_fnc("ShpCmd31"), # data
	0x8037D500: main.sym_fnc("ShpCmdLayer"), # data
	0x8037D55C: main.sym_fnc("ShpCmdLOD"), # data
	0x8037D5D4: main.sym_fnc("ShpCmdSelect"), # data
	0x8037D640: main.sym_fnc("ShpCmdCamera"), # data
	0x8037D6F0: main.sym_fnc("ShpCmdCoord"), # data
	0x8037D8D4: main.sym_fnc("ShpCmdPos"), # data
	0x8037D998: main.sym_fnc("ShpCmdAng"), # data
	0x8037DA5C: main.sym_fnc("ShpCmdScale"), # data
	0x8037DB50: main.sym_fnc("ShpCmd30"), # data
	0x8037DB74: main.sym_fnc("ShpCmdJoint"), # data
	0x8037DC10: main.sym_fnc("ShpCmdBillboard"), # data
	0x8037DCD4: main.sym_fnc("ShpCmdGfx"), # data
	0x8037DD4C: main.sym_fnc("ShpCmdShadow"), # data
	0x8037DDDC: main.sym_fnc("ShpCmdObject"), # data
	0x8037DE34: main.sym_fnc("ShpCmdCallback"), # data
	0x8037DE94: main.sym_fnc("ShpCmdBack"), # data
	0x8037DEF8: main.sym_fnc("ShpCmd26"), # data
	0x8037DF1C: main.sym_fnc("ShpCmdLoad"), # data
	0x8037DFD4: main.sym_fnc("ShpCmdHand"), # data
	0x8037E058: main.sym_fnc("ShpCmdCull"), # data
	0x8037E0B4: main.sym_fnc("ShpLangCompile", "SHAPE *", (
		"ARENA *arena",
		"SHPLANG *script",
	), flag={"GLOBL"}),

	# src/prglang.c
	0x8037E1A0: main.sym_fnc("PrgCmp", "int", (
		"CHAR cmp",
		"int x",
	)),
	0x8037E1D4: main.sym_fnc("L8037E1D4", flag={"GLOBL","LOCAL"}),
	0x8037E1EC: main.sym_fnc("L8037E1EC", flag={"GLOBL","LOCAL"}),
	0x8037E20C: main.sym_fnc("L8037E20C", flag={"GLOBL","LOCAL"}),
	0x8037E228: main.sym_fnc("L8037E228", flag={"GLOBL","LOCAL"}),
	0x8037E244: main.sym_fnc("L8037E244", flag={"GLOBL","LOCAL"}),
	0x8037E25C: main.sym_fnc("L8037E25C", flag={"GLOBL","LOCAL"}),
	0x8037E278: main.sym_fnc("L8037E278", flag={"GLOBL","LOCAL"}),
	0x8037E290: main.sym_fnc("L8037E290", flag={"GLOBL","LOCAL"}),
	0x8037E2C4: main.sym_fnc("PrgCmdExecute"), # data
	0x8037E388: main.sym_fnc("PrgCmdChain"), # data
	0x8037E404: main.sym_fnc("PrgCmdExit"), # data
	0x8037E47C: main.sym_fnc("PrgCmdSleep"), # data
	0x8037E4FC: main.sym_fnc("PrgCmdFreeze"), # data
	0x8037E580: main.sym_fnc("PrgCmdJump"), # data
	0x8037E5B8: main.sym_fnc("PrgCmdCall"), # data
	0x8037E620: main.sym_fnc("PrgCmdReturn"), # data
	0x8037E650: main.sym_fnc("PrgCmdFor"), # data
	0x8037E6D4: main.sym_fnc("PrgCmdDone"), # data
	0x8037E780: main.sym_fnc("PrgCmdRepeat"), # data
	0x8037E7F8: main.sym_fnc("PrgCmdUntil"), # data
	0x8037E878: main.sym_fnc("PrgCmdJumpIf"), # data
	0x8037E8E8: main.sym_fnc("PrgCmdCallIf"), # data
	0x8037E988: main.sym_fnc("PrgCmdIf"), # data
	0x8037EA18: main.sym_fnc("PrgCmdElse"), # data
	0x8037EA70: main.sym_fnc("PrgCmdEndif"), # data
	0x8037EA98: main.sym_fnc("PrgCmdCallback"), # data
	0x8037EB04: main.sym_fnc("PrgCmdProcess"), # data
	0x8037EB98: main.sym_fnc("PrgCmdSet"), # data
	0x8037EBD4: main.sym_fnc("PrgCmdPush"), # data
	0x8037EC14: main.sym_fnc("PrgCmdPull"), # data
	0x8037EC54: main.sym_fnc("PrgCmdLoadCode"), # data
	0x8037ECA4: main.sym_fnc("PrgCmdLoadData"), # data
	0x8037ECF8: main.sym_fnc("PrgCmdLoadPres"), # data
	0x8037ED48: main.sym_fnc("PrgCmdLoadFace"), # data
	0x8037EDF8: main.sym_fnc("PrgCmdLoadText"), # data
	0x8037EE48: main.sym_fnc("PrgCmdStageInit"), # data
	0x8037EEA8: main.sym_fnc("PrgCmdStageExit"), # data
	0x8037EF00: main.sym_fnc("PrgCmdStageStart"), # data
	0x8037EF70: main.sym_fnc("PrgCmdStageEnd"), # data
	0x8037F010: main.sym_fnc("PrgCmdSceneStart"), # data
	0x8037F130: main.sym_fnc("PrgCmdSceneEnd"), # data
	0x8037F164: main.sym_fnc("PrgCmdShapeGfx"), # data
	0x8037F214: main.sym_fnc("PrgCmdShape"), # data
	0x8037F2A4: main.sym_fnc("PrgCmdShapeScale"), # data
	0x8037F36C: main.sym_fnc("PrgCmdPlayer"), # data
	0x8037F45C: main.sym_fnc("PrgCmdObject"), # data
	0x8037F67C: main.sym_fnc("PrgCmdPort"), # data
	0x8037F790: main.sym_fnc("PrgCmdConnect"), # data
	0x8037F920: main.sym_fnc("PrgCmdEnv"), # data
	0x8037F994: main.sym_fnc("PrgCmdBGPort"), # data
	0x8037FB18: main.sym_fnc("PrgCmdWind"), # data
	0x8037FC38: main.sym_fnc("PrgCmdJet"), # data
	0x8037FDE4: main.sym_fnc("PrgCmdViBlack"), # data
	0x8037FE2C: main.sym_fnc("PrgCmdViGamma"), # data
	0x8037FE94: main.sym_fnc("PrgCmdMap"), # data
	0x8037FF14: main.sym_fnc("PrgCmdArea"), # data
	0x8037FF94: main.sym_fnc("PrgCmdTag"), # data
	0x80380014: main.sym_fnc("PrgCmdSceneOpen"), # data
	0x8038007C: main.sym_fnc("PrgCmdSceneClose"), # data
	0x803800BC: main.sym_fnc("PrgCmdPlayerOpen"), # data
	0x80380160: main.sym_fnc("PrgCmdPlayerClose"), # data
	0x803801A0: main.sym_fnc("PrgCmdSceneProc"), # data
	0x803801E0: main.sym_fnc("PrgCmdWipe"), # data
	0x8038024C: main.sym_fnc("PrgCmd32"), # data
	0x80380274: main.sym_fnc("PrgCmdMessage"), # data
	0x80380300: main.sym_fnc("PrgCmdBGM"), # data
	0x8038039C: main.sym_fnc("PrgCmdPlayBGM"), # data
	0x803803EC: main.sym_fnc("PrgCmdAudFadeout"), # data
	0x80380434: main.sym_fnc("PrgCmdVar"), # data
	0x80380478: main.sym_fnc("L80380478", flag={"GLOBL","LOCAL"}),
	0x80380490: main.sym_fnc("L80380490", flag={"GLOBL","LOCAL"}),
	0x803804A8: main.sym_fnc("L803804A8", flag={"GLOBL","LOCAL"}),
	0x803804C0: main.sym_fnc("L803804C0", flag={"GLOBL","LOCAL"}),
	0x803804D8: main.sym_fnc("L803804D8", flag={"GLOBL","LOCAL"}),
	0x80380528: main.sym_fnc("L80380528", flag={"GLOBL","LOCAL"}),
	0x80380540: main.sym_fnc("L80380540", flag={"GLOBL","LOCAL"}),
	0x80380558: main.sym_fnc("L80380558", flag={"GLOBL","LOCAL"}),
	0x80380570: main.sym_fnc("L80380570", flag={"GLOBL","LOCAL"}),
	0x80380588: main.sym_fnc("L80380588", flag={"GLOBL","LOCAL"}),
	0x803805C8: main.sym_fnc("PrgLangExec", "PRGLANG *", (
		"PRGLANG *pc",
	), flag={"GLOBL"}),

	# src/bgcheck.c
	0x80380690: main.sym_fnc("BGListCheckWall", "int", (
		"BGLIST *list",
		"WALLCHECK *check",
	)),
	0x80380DE8: main.sym_fnc("BGHitWall", "int", (
		"float *x",
		"float *y",
		"float *z",
		"float offset",
		"float radius",
	), flag={"GLOBL"}),
	0x80380E8C: main.sym_fnc("BGCheckWall", "int", (
		"WALLCHECK *check",
	), flag={"GLOBL"}),
	0x80381038: main.sym_fnc("BGListCheckRoof", "BGFACE *", (
		"BGLIST *list",
		"int x",
		"int y",
		"int z",
		"float *roof_y",
	)),
	0x80381264: main.sym_fnc("BGCheckRoof", "float", (
		"float x",
		"float y",
		"float z",
		"BGFACE **roof",
	), flag={"GLOBL"}),
	0x80381470: main.sym_fnc("ObjCheckGroundY", "float", (
		"OBJECT *obj",
	)), # unused
	0x803814B8: main.sym_fnc("BGCheckPlane", "float", (
		"float x",
		"float y",
		"float z",
		"PLANE **plane",
	), flag={"GLOBL"}),
	0x8038156C: main.sym_fnc("BGListCheckGround", "float", (
		"BGLIST *list",
		"int x",
		"int y",
		"int z",
		"float *ground_y",
	)),
	0x80381794: main.sym_fnc("BGCheckGroundY", "float", (
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}),
	0x803817E0: main.sym_fnc("BGCheckGroundMoveBG", "float", (
		"float x",
		"float y",
		"float z",
		"BGFACE **ground",
	)), # unused
	0x80381900: main.sym_fnc("BGCheckGround", "float", (
		"float x",
		"float y",
		"float z",
		"BGFACE **ground",
	), flag={"GLOBL"}),
	0x80381BA0: main.sym_fnc("BGCheckWater", "float", (
		"float x",
		"float z",
	), flag={"GLOBL"}),
	0x80381D3C: main.sym_fnc("BGCheckGas", "float", (
		"float x",
		"float z",
	), flag={"GLOBL"}),
	0x80381EC8: main.sym_fnc("BGListLen", "int", (
		"BGLIST *list",
	)),
	0x80381F08: main.sym_fnc("BGCheckDebug", arg=(
		"float x",
		"float z",
	), flag={"GLOBL"}),
	0x80382294: main.sym_fnc("BGHitGroundRoof", "int", (
		"int flag",
		"float *x",
		"float *y",
		"float *z",
		"float radius",
		"BGFACE **face",
		"float *face_y",
	)), # unused

	# src/bgload.c
	0x80382490: main.sym_fnc("BGListAlloc", "BGLIST *"),
	0x803824F8: main.sym_fnc("BGFaceAlloc", "BGFACE *"),
	0x80382590: main.sym_fnc("BGRootClear", arg=(
		"BGROOT *root",
	)),
	0x803825D0: main.sym_fnc("StatBGClear"),
	0x803825FC: main.sym_fnc("BGListCreate", arg=(
		"SHORT flag",
		"SHORT ix",
		"SHORT iz",
		"BGFACE *face",
	)),
	0x8038283C: main.sym_fnc("Min3", "SHORT", (
		"SHORT x",
		"SHORT y",
		"SHORT z",
	)),
	0x8038289C: main.sym_fnc("Max3", "SHORT", (
		"SHORT x",
		"SHORT y",
		"SHORT z",
	)),
	0x803828FC: main.sym_fnc("BGAreaMin", "SHORT", (
		"SHORT x",
	)),
	0x80382990: main.sym_fnc("BGAreaMax", "SHORT", (
		"SHORT x",
	)),
	0x80382A2C: main.sym_fnc("BGFaceLink", arg=(
		"BGFACE *face",
		"int flag",
	)),
	0x80382B6C: main.sym_fnc("bgload_80382B6C"), # unused
	0x80382B7C: main.sym_fnc("BGFaceCreate", "BGFACE *", (
		"MAP *vtx",
		"MAP **map",
	)),
	0x80382F84: main.sym_fnc("BGFaceHasAttr", "int", (
		"SHORT code",
	)),
	0x80382FBC: main.sym_fnc("L80382FBC", flag={"GLOBL","LOCAL"}),
	0x80382FCC: main.sym_fnc("L80382FCC", flag={"GLOBL","LOCAL"}),
	0x80382FEC: main.sym_fnc("BGFaceFlag", "int", (
		"SHORT code",
	)),
	0x80383068: main.sym_fnc("StatBGFace", arg=(
		"MAP **map",
		"MAP *vtx",
		"SHORT code",
		"AREA **area",
	)),
	0x803831D0: main.sym_fnc("StatBGVtx", "MAP *", (
		"MAP **map",
	)),
	0x80383228: main.sym_fnc("StatBGWater", arg=(
		"MAP **map",
	)),
	0x80383340: main.sym_fnc("MapInit", flag={"GLOBL"}),
	0x803833B8: main.sym_fnc("MapLoad", arg=(
		"SHORT scene",
		"MAP *map",
		"AREA *area",
		"TAG *tag",
	), flag={"GLOBL"}),
	0x803835A4: main.sym_fnc("MoveBGClear", flag={"GLOBL"}),
	0x80383604: main.sym_fnc("bgload_80383604"), # unused
	0x80383614: main.sym_fnc("MoveBGVtx", arg=(
		"MAP **map",
		"MAP *vtx",
	)),
	0x80383828: main.sym_fnc("MoveBGFace", arg=(
		"MAP **map",
		"MAP *vtx",
	)),
	0x803839CC: main.sym_fnc("ObjectMapLoad", flag={"GLOBL"}), # objcall

	# src/objlang.c
	0x80383B70: main.sym_fnc("ObjectScriptEntry", arg=(
		"OBJLANG *script",
	)), # unused
	0x80383BB0: main.sym_fnc("Rand", "u16", flag={"GLOBL"}),
	0x80383CB4: main.sym_fnc("RandF", "float", flag={"GLOBL"}),
	0x80383D1C: main.sym_fnc("RandSign", "int", flag={"GLOBL"}),
	0x80383D68: main.sym_fnc("ObjSetShapeCoord", arg=(
		"OBJECT *obj",
	)),
	0x80383DBC: main.sym_fnc("ObjectPush", arg=(
		"unsigned long x",
	)),
	0x80383DF8: main.sym_fnc("ObjectPull", "unsigned long"),
	0x80383E44: main.sym_fnc("ObjectError"), # unused
	0x80383E5C: main.sym_fnc("ObjCmdShapeHide", "int"), # data
	0x80383EA0: main.sym_fnc("ObjCmdShapeDisable", "int"), # data
	0x80383EE4: main.sym_fnc("ObjCmdBillboard", "int"), # data
	0x80383F24: main.sym_fnc("ObjCmdShape", "int"), # data
	0x80383F94: main.sym_fnc("ObjCmdMakeObj", "int"), # data
	0x8038401C: main.sym_fnc("ObjCmdMakeChild", "int"), # data
	0x803840B4: main.sym_fnc("ObjCmdMakeObjCode", "int"), # data
	0x80384164: main.sym_fnc("ObjCmdDestroy", "int"), # data
	0x80384188: main.sym_fnc("ObjCmdExit", "int"), # data
	0x803841A0: main.sym_fnc("ObjCmdEnd", "int"), # data
	0x803841B8: main.sym_fnc("ObjCmdCall", "int"), # data
	0x80384224: main.sym_fnc("ObjCmdReturn", "int"), # data
	0x8038425C: main.sym_fnc("ObjCmdSleep", "int"), # data
	0x803842E4: main.sym_fnc("ObjCmdMemSleep", "int"), # data
	0x8038438C: main.sym_fnc("ObjCmdJump", "int"), # data
	0x803843E0: main.sym_fnc("ObjCmdFor2", "int"), # data
	0x80384450: main.sym_fnc("ObjCmdFor", "int"), # data
	0x803844C0: main.sym_fnc("ObjCmdFend", "int"), # data
	0x80384554: main.sym_fnc("ObjCmdFcontinue", "int"), # data
	0x803845E8: main.sym_fnc("ObjCmdWhile", "int"), # data
	0x80384634: main.sym_fnc("ObjCmdWend", "int"), # data
	0x80384678: main.sym_fnc("ObjCmdCallback", "int"), # data
	0x803846D0: main.sym_fnc("ObjCmdSetF", "int"), # data
	0x8038475C: main.sym_fnc("ObjCmdSetI", "int"), # data
	0x803847D4: main.sym_fnc("ObjCmdSetS", "int"), # data
	0x80384854: main.sym_fnc("ObjCmdSetRandF", "int"), # data
	0x80384928: main.sym_fnc("ObjCmdSetRandI", "int"), # data
	0x803849F8: main.sym_fnc("ObjCmdSetRandA", "int"), # data
	0x80384AB4: main.sym_fnc("ObjCmdAddRandF", "int"), # data
	0x80384B90: main.sym_fnc("ObjCmdAddRandA", "int"), # data
	0x80384C5C: main.sym_fnc("ObjCmdAddF", "int"), # data
	0x80384CF0: main.sym_fnc("ObjCmdAddI", "int"), # data
	0x80384D70: main.sym_fnc("ObjCmdSetFlag", "int"), # data
	0x80384E04: main.sym_fnc("ObjCmdClrFlag", "int"), # data
	0x80384E9C: main.sym_fnc("ObjCmdPtr", "int"), # data
	0x80384F08: main.sym_fnc("ObjCmdAnime", "int"), # data
	0x80384F8C: main.sym_fnc("ObjCmdGround", "int"), # data
	0x8038503C: main.sym_fnc("ObjCmd24", "int"), # data
	0x80385084: main.sym_fnc("ObjCmd25", "int"), # data
	0x803850CC: main.sym_fnc("ObjCmd26", "int"), # data
	0x80385114: main.sym_fnc("ObjCmdMemAddF", "int"), # data
	0x803851D0: main.sym_fnc("ObjCmdMemAddI", "int"), # data
	0x8038528C: main.sym_fnc("ObjCmdHit", "int"), # data
	0x8038531C: main.sym_fnc("ObjCmdDmg", "int"), # data
	0x803853AC: main.sym_fnc("ObjCmdHitOff", "int"), # data
	0x8038546C: main.sym_fnc("ObjCmd36", "int"), # data
	0x803854CC: main.sym_fnc("ObjCmdInit", "int"), # data
	0x8038556C: main.sym_fnc("ObjLangSetRandTbl", arg=(
		"int len",
	)), # unused
	0x803856A0: main.sym_fnc("ObjCmdMap", "int"), # data
	0x80385700: main.sym_fnc("ObjCmdSave", "int"), # data
	0x8038575C: main.sym_fnc("ObjCmdHitType", "int"), # data
	0x803857A0: main.sym_fnc("ObjCmdHitFlag", "int"), # data
	0x803857E4: main.sym_fnc("ObjCmdScale", "int"), # data
	0x8038586C: main.sym_fnc("ObjCmdPhysics", "int"), # data
	0x80385A60: main.sym_fnc("ObjCmdMemClrParentFlag", "int"), # data
	0x80385AF0: main.sym_fnc("ObjCmdSplash", "int"), # data
	0x80385B4C: main.sym_fnc("ObjCmdInc", "int"), # data
	0x80385BF0: main.sym_fnc("ObjLangInit", flag={"GLOBL"}),
	0x80385C00: main.sym_fnc("ObjLangExec", flag={"GLOBL"}),

	0x8038BCF4: main.sym("shp_stack-4"),

	0x8038BD98: main.sym("sobj_list+0x10"), # child

	0x8038BE40: main.sym("ground_plane+0x10"), # nx
	0x8038BE44: main.sym("ground_plane+0x14"), # ny
	0x8038BE48: main.sym("ground_plane+0x18"), # nz
	0x8038BE4C: main.sym("ground_plane+0x1C"), # nw

	0x8038BEA0: main.sym("statbg_root+0x08"), # roof
	0x8038BEA8: main.sym("statbg_root+0x10"), # wall

	0x8038D6A0: main.sym("movebg_root+0x08"), # roof
	0x8038D6A8: main.sym("movebg_root+0x10"), # wall

	0x80400000: main.sym("_zimgSegmentBssStart"),
	0x8038F800: main.sym("_cimgSegmentBssStart"),
}

sym_J0_E0_ulib_data = {
	# ==========================================================================
	# data
	# ==========================================================================

	# src/math.c
	0x80385F90: main.sym_var("mtx_1", "Mtx", flag={"GLOBL"}), # unused
	0x80385FD0: main.sym_var("fvec_0", "FVEC", flag={"GLOBL"}),
	0x80385FDC: main.sym_var("svec_0", "SVEC", flag={"GLOBL"}),
	0x80385FE4: main.sym_var("fvec_1", "FVEC", flag={"GLOBL"}),
	0x80385FF0: main.sym_var("svec_1", "SVEC", flag={"GLOBL"}), # unused

	# src/mathtbl.s
	0x80386000: main.sym_var("sintable", "float", "[]", flag={"GLOBL"}),
	0x80387000: main.sym_var("costable", "float", "[]", flag={"GLOBL"}),
	0x8038B000: main.sym_var("atantable", "short", "[]", flag={"GLOBL"}),

	# src/shplang.c
	0x8038B810: main.sym_var_fnc("shp_cmdtab", lst="[]"),

	# src/prglang.c
	0x8038B8A0: main.sym_var("prg_arena", "ARENA *", flag={"DALIGN"}),
	0x8038B8A4: main.sym_var("prg_sleep", "u16", flag={"DALIGN"}),
	0x8038B8A8: main.sym_var("prg_freeze", "u16", flag={"DALIGN"}),
	0x8038B8AC: main.sym_var("prg_scene", "s16", flag={"DALIGN"}),
	0x8038B8B0: main.sym_var("prg_sp", "unsigned long *", flag={"DALIGN"}),
	0x8038B8B4: main.sym_var("prg_fp", "unsigned long *", flag={"DALIGN"}),
	0x8038B8B8: main.sym_var_fnc("prg_cmdtab", lst="[]"),

	# src/objlang.c
	0x8038B9B0: main.sym_var_fnc("obj_cmdtab", lst="[]", val="int"),

	# ==========================================================================
	# rodata
	# ==========================================================================

	# src/math.c
	0x8038BA90: main.sym_var("math_8038BA90", "const double"),
	0x8038BA98: main.sym_var_fnc("math_8038BA98", "const", "[]"),
	0x8038BAAC: main.sym_var("math_8038BAAC", "const float"),
	0x8038BAB0: main.sym_var("math_8038BAB0", "const float"),
	0x8038BAB4: main.sym_var("math_8038BAB4", "const float"),
	0x8038BAB8: main.sym_var("math_8038BAB8", "const float"),
	0x8038BABC: main.sym_var("math_8038BABC", "const float"),
	0x8038BAC0: main.sym_var("math_8038BAC0", "const float"),
	0x8038BAC4: main.sym_var("math_8038BAC4", "const float"),
	0x8038BAC8: main.sym_var("math_8038BAC8", "const float"),
	0x8038BACC: main.sym_var("math_8038BACC", "const float"),
	0x8038BAD0: main.sym_var("math_8038BAD0", "const float"),
	0x8038BAD4: main.sym_var("math_8038BAD4", "const float"),
	0x8038BAD8: main.sym_var("math_8038BAD8", "const float"),
	0x8038BADC: main.sym_var("math_8038BADC", "const float"),
	0x8038BAE0: main.sym_var("math_8038BAE0", "const float"),
	0x8038BAE4: main.sym_var("math_8038BAE4", "const float"),
	0x8038BAE8: main.sym_var("math_8038BAE8", "const float"),

	# src/prglang.c
	0x8038BAF0: main.sym_var_fnc("prglang_8038BAF0", "const", "[]"),
	0x8038BB10: main.sym_var_fnc("prglang_8038BB10", "const", "[]"),
	0x8038BB24: main.sym_var_fnc("prglang_8038BB24", "const", "[]"),

	# src/bgcheck.c
	0x8038BB40: main.sym_var("str_bgcheck_area", "const char", "[]"),
	0x8038BB4C: main.sym_var("str_bgcheck_dg", "const char", "[]"),
	0x8038BB54: main.sym_var("str_bgcheck_dw", "const char", "[]"),
	0x8038BB5C: main.sym_var("str_bgcheck_dr", "const char", "[]"),
	0x8038BB64: main.sym_var("str_bgcheck_ground", "const char", "[]"), # %d
	0x8038BB68: main.sym_var("str_bgcheck_wall", "const char", "[]"), # %d
	0x8038BB6C: main.sym_var("str_bgcheck_roof", "const char", "[]"), # %d
	0x8038BB70: main.sym_var("str_bgcheck_listal", "const char", "[]"),
	0x8038BB7C: main.sym_var("str_bgcheck_statbg", "const char", "[]"),
	0x8038BB88: main.sym_var("str_bgcheck_movebg", "const char", "[]"),
	0x8038BB94: main.sym_var("bgcheck_8038BB94", "const float"),
	0x8038BB98: main.sym_var("bgcheck_8038BB98", "const float"),
	0x8038BB9C: main.sym_var("bgcheck_8038BB9C", "const float"),
	0x8038BBA0: main.sym_var("bgcheck_8038BBA0", "const float"),
	0x8038BBA4: main.sym_var("bgcheck_8038BBA4", "const float"),
	0x8038BBA8: main.sym_var("bgcheck_8038BBA8", "const float"),
	0x8038BBAC: main.sym_var("bgcheck_8038BBAC", "const float"),

	# src/bgload.c
	0x8038BBB0: main.sym_var("bgload_8038BBB0", "const double"),
	0x8038BBB8: main.sym_var("bgload_8038BBB8", "const double"),
	0x8038BBC0: main.sym_var("bgload_8038BBC0", "const double"),
	0x8038BBC8: main.sym_var("bgload_8038BBC8", "const double"),
	0x8038BBD0: main.sym_var("bgload_8038BBD0", "const double"),
	0x8038BBD8: main.sym_var_fnc("bgload_8038BBD8", "const", "[]"),
	0x8038BC80: main.sym_var("bgload_8038BC80", "const float"),

	# ==========================================================================
	# bss
	# ==========================================================================

	# src/math.c
	0x8038BC90: main.sym_var("bspline", "BSPLINE *"),
	0x8038BC94: main.sym_var("bspline_phase", "float"),
	0x8038BC98: main.sym_var("bspline_mode", "int"),

	# src/shplang.c
	0x8038BCA0: main.sym_var("shp_arena", "ARENA *"),
	0x8038BCA4: main.sym_var("shape_root", "SHAPE *"),
	0x8038BCA8: main.sym_var("shape_8038BCA8", "SHAPE *"), # unused
	0x8038BCAC: main.sym_var("shape_storetab", "SHAPE **"),
	0x8038BCB0: main.sym_var("shape_storelen", "u16"),
	0x8038BCB8: main.sym_var("shp_stack", "unsigned long", "[16]", flag={"BALIGN"}),
	0x8038BCF8: main.sym_var("shape_stack", "SHAPE *", "[32]", flag={"BALIGN"}),
	0x8038BD78: main.sym_var("shape_sp", "s16"),
	0x8038BD7A: main.sym_var("shp_sp", "s16"),
	0x8038BD7C: main.sym_var("shape_fp", "s16"), # unused
	0x8038BD7E: main.sym_var("shp_fp", "s16"),
	0x8038BD80: main.sym_var("shp_pc", "SHPLANG *"),
	0x8038BD88: main.sym_var("sobj_list", "SHAPE", flag={"GLOBL","BALIGN"}),

	# src/prglang.c
	0x8038BDA0: main.sym_var("prg_stack", "unsigned long", "[32]", flag={"BALIGN"}),
	0x8038BE20: main.sym_var("prg_state", "s16"),
	0x8038BE24: main.sym_var("prg_status", "int"),
	0x8038BE28: main.sym_var("prg_pc", "PRGLANG *"),

	# src/bgcheck.c
	0x8038BE30: main.sym_var("ground_plane", "PLANE"),
	0x8038BE58: main.sym_var("bgcheck_8038BE58", "char", "[56]"),

	# src/bgload.c
	0x8038BE90: main.sym_var("bgload_8038BE90", "int", flag={"GLOBL"}),
	0x8038BE98: main.sym_var("statbg_root", "BGROOT", "[16][16]", flag={"GLOBL","BALIGN"}),
	0x8038D698: main.sym_var("movebg_root", "BGROOT", "[16][16]", flag={"GLOBL","BALIGN"}),
	0x8038EE98: main.sym_var("bglist_data", "BGLIST *", flag={"GLOBL"}),
	0x8038EE9C: main.sym_var("bgface_data", "BGFACE *", flag={"GLOBL"}),
	0x8038EEA0: main.sym_var("bgface_max", "s16", flag={"GLOBL"}),
	0x8038EEA4: main.sym_var("bgload_8038EEA4", "int", "[12]", flag={"GLOBL"}), # unused

	# src/objlang.c
	0x8038EEE0: main.sym_var("rand_seed", "u16"),
}

sym_G0_ulib_text = {
	0x80378800: main.sym("FVecCpy", flag={"GLOBL"}),
}

sym_DD_ulib_text = {
	0x80510000: main.sym("FVecCpy", flag={"GLOBL"}),
}

sym_P0_ulib_text = {
	0x8036FF00: main.sym("P0_8036FF00"),
}
