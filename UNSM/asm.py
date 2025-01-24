import struct
import math

import main
import ultra
import UNSM

def d_prg_prc(self, argv):
	self.addr += 6
	dst = ultra.ah(self, self.save)
	return "0, 0, 0, %s" % dst
d_prg = [".half", d_prg_prc]

seg_table = {
	0x02: "SEG_GFX",
	0x03: "SEG_GLOBAL_GFX",
	0x04: "SEG_PLAYER_GFX",
	0x05: "SEG_SHAPE1_GFX",
	0x06: "SEG_SHAPE2_GFX",
	0x07: "SEG_STAGE_GFX",
	0x08: "SEG_SHAPE3_GFX",
	0x09: "SEG_TEXTURE",
	0x0A: "SEG_BACKGROUND",
	0x0B: "SEG_WEATHER",
	0x0C: "SEG_SHAPE1_SHP",
	0x0D: "SEG_SHAPE2_SHP",
	0x0E: "SEG_STAGE_DATA",
	0x0F: "SEG_SHAPE3_SHP",
	0x13: "SEG_OBJECT",
	0x14: "SEG_MENU_DATA",
	0x15: "SEG_GAME",
	0x16: "SEG_GLOBAL_SHP",
	0x17: "SEG_PLAYER_SHP",
}

# 00 01
def prg_execute(self, argv):
	number = self.s16()
	start  = self.u32()
	end    = self.u32()
	script = self.u32()
	seg    = self.segtab[start]
	start  = self.meta.sym[seg][start].label
	if not start.endswith("SegmentRomStart"):
		raise RuntimeError("prg_execute(): bad segment")
	end    = start[:-5] + "End"
	script = self.meta.sym[seg][script].label
	number = seg_table[number]
	return (None, number, start, end, script)

# 02 07 0A 1B 1C 1D 1E 20
def prg_null(self, argv):
	self.addr += 2
	return (None,)

# 03 04
def prg_time(self, argv):
	time = UNSM.fmt.fmt_time(self.s16())
	return (None, time)

# 05 06 2E 2F 39
def prg_script(self, argv):
	g, = argv
	self.addr += 2
	script = ultra.aw(self, self.save) if g else ultra.asm.aw(self)
	return (None, script)

# (08) (09)

# 0B 0C
def prg_cmp(self, argv):
	s, = argv
	cmp_ = ("AND", "NAND", "EQ", "NE", "LT", "LE", "GT", "GE")[self.u8()]
	self.addr += 1
	val = self.s32()
	if self.seg.endswith(".Game"):
		if val < 0: val = UNSM.fmt.fmt_exit[val]
		else: val = UNSM.fmt.fmt_stage[val]
	elif self.seg.endswith(".Title"):
		val = {
			-1: "-1",
			100: "100+FALSE",
			101: "100+TRUE",
		}[val]
	elif self.seg.endswith(".Select"):
		val = {
			0: "FALSE",
		}[val]
	else:
		val = "%d" % val
	if s:
		script = ultra.asm.aw(self)
		return (None, cmp_, val, script)
	return (None, cmp_, val)

# (0D) (0E) (0F) (10)

# 11 12
def prg_callback(self, argv):
	arg = "%d" % self.u16()
	callback = ultra.aw(self, self.save)
	return (None, callback, arg)

# 13 19
def prg_arg(self, argv):
	x = "%d" % self.s16()
	return (None, x)

# (14) (15)

# 16 17 18 1A
def prg_load(self, argv):
	flag, = argv
	number = self.s16()
	if flag: addr = self.u32()
	start = self.u32()
	end   = self.u32()
	seg = self.segtab[start]
	start = self.meta.sym[seg][start].label
	if not start.endswith("SegmentRomStart"):
		raise RuntimeError("prg_load(): bad segment")
	if flag: addr = start[:-8] + "Start"
	end = start[:-5] + "End"
	if flag: return (None, addr, start, end)
	number = seg_table[number]
	return (None, number, start, end)

# 1F
def prg_scenestart(self, argv):
	scene = "%d" % self.u8()
	self.addr += 1
	script = ultra.aw(self, self.save)
	return (None, scene, script)

# 21
def prg_shapegfx(self, argv):
	x = self.u16()
	layer = UNSM.fmt.fmt_layer(self, x >> 12)
	shape = UNSM.fmt.fmt_shape(self, x & 0x0FFF)
	gfx = ultra.aw(self, self.save)
	return (None, shape, gfx, layer)

# 22
def prg_shape(self, argv):
	shape = UNSM.fmt.fmt_shape(self, self.u16())
	script = ultra.aw(self, self.save)
	return (None, shape, script)

# (23)

# 24
def prg_object(self, argv):
	mask = self.u8()
	shape = UNSM.fmt.fmt_shape(self, self.u8())
	posx = "%d" % self.s16()
	posy = "%d" % self.s16()
	posz = "%d" % self.s16()
	angx = "%d" % self.s16()
	angy = "%d" % self.s16()
	angz = "%d" % self.s16()
	a0 = "%d" % self.u8()
	a1 = "%d" % self.u8()
	flag = UNSM.fmt.fmt_actor_flag(self, self.u16())
	script = ultra.aw(self, self.save)
	if mask == 0x1F: return (
		"Object", shape, posx, posy, posz, angx, angy, angz,
		a0, a1, flag, script
	)
	mask = "0%02o" % mask
	return (
		None, mask, shape, posx, posy, posz, angx, angy, angz,
		a0, a1, flag, script
	)

# 25
def prg_player(self, argv):
	shape = UNSM.fmt.fmt_shape(self, self.u16())
	arg0 = self.u8()
	arg1 = self.u8()
	flag = self.u16()
	script = ultra.aw(self, self.save)
	if (shape, arg0, arg1, flag, script) == ("S_MARIO", 0, 0, 1, "o_mario"):
		return ("Mario",)
	arg0 = "%d" % arg0
	arg1 = "%d" % arg1
	flag = UNSM.fmt.fmt_actor_flag(self, flag)
	return (None, shape, arg0, arg1, flag, script)

# 26 27
def prg_port(self, argv):
	mid, bg = argv
	if bg:
		index = "%d" % self.u8()
	else:
		index = UNSM.fmt.fmt_port(self, self.u8())
	stage = UNSM.fmt.fmt_stage[self.u8()]
	scene = "%d" % self.u8()
	port  = UNSM.fmt.fmt_port(self, self.u8())
	flag  = self.u8()
	self.addr += 1
	return (mid if flag else None, index, stage, scene, port)

# 28
def prg_connect(self, argv):
	index = "%d" % self.u8()
	scene = "%d" % self.u8()
	offx = "%d" % self.s16()
	offy = "%d" % self.s16()
	offz = "%d" % self.s16()
	self.addr += 2
	return (None, index, scene, offx, offy, offz)

# 29 2A
def prg_scene(self, argv):
	scene = "%d" % self.u8()
	self.addr += 1
	return (None, scene)

# 2B
def prg_playeropen(self, argv):
	scene = "%d" % self.u8()
	self.addr += 1
	angy = "%d" % self.s16()
	posx = "%d" % self.s16()
	posy = "%d" % self.s16()
	posz = "%d" % self.s16()
	return (None, scene, angy, posx, posy, posz)

# (2C) (2D)

# 30
def prg_message(self, argv):
	index = "%d" % self.u8()
	msg   = UNSM.fmt.fmt_msg(self, self.u8())
	return (None, index, msg)

# 31
def prg_env(self, argv):
	env = (
		"ENV_GRASS",
		"ENV_ROCK",
		"ENV_SNOW",
		"ENV_SAND",
		"ENV_GHOST",
		"ENV_WATER",
		"ENV_SLIDER",
	)[self.s16()]
	return (None, env)

# 33
def prg_wipe(self, argv):
	type_ = {
		0: "WIPE_FADE_IN",
		1: "WIPE_FADE_OUT",
		8: "WIPE_STAR_IN",
		9: "WIPE_STAR_OUT",
		10: "WIPE_CIRCLE_IN",
		11: "WIPE_CIRCLE_OUT",
		16: "WIPE_MARIO_IN",
		17: "WIPE_MARIO_OUT",
		18: "WIPE_BOWSER_IN",
		19: "WIPE_BOWSER_OUT",
	}[self.u8()]
	time  = UNSM.fmt.fmt_time(self.u8())
	r = "0x%02X" % self.u8()
	g = "0x%02X" % self.u8()
	b = "0x%02X" % self.u8()
	self.addr += 1
	return (None, type_, time, r, g, b)

# 34
def prg_bool(self, argv):
	x = ultra.fmt_bool[self.u8()]
	self.addr += 1
	return (None, x)

# (35)

# 36
def prg_bgm(self, argv):
	mode = UNSM.fmt.fmt_na_mode[self.u16()]
	bgm  = UNSM.fmt.fmt_na_bgm[self.u16()]
	self.addr += 2
	return (None, mode, bgm)

# 37
def prg_playbgm(self, argv):
	bgm = UNSM.fmt.fmt_na_bgm[self.u16()]
	return (None, bgm)

# 38
def prg_audfadeout(self, argv):
	fadeout = "NA_TIME(%d)" % ((self.s16()+2)//8)
	return (None, fadeout)

# (3A)

# 3B
def prg_jet(self, argv):
	index = "%d" % self.u8()
	mode  = "%d" % self.u8()
	posx  = "%d" % self.s16()
	posy  = "%d" % self.s16()
	posz  = "%d" % self.s16()
	arg   = "%d" % self.s16()
	return (None, index, mode, posx, posy, posz, arg)

# 3C
def prg_var(self, argv):
	cmd = (
		"Store",
		"Load",
	)[self.u8()]
	var = (
		"FILE",
		"COURSE",
		"LEVEL",
		"STAGE",
		"SCENE",
	)[self.u8()]
	return (cmd, var)

prg_name = [
	"Execute",      # 0x00
	"Chain",        # 0x01
	"Exit",         # 0x02
	"Sleep",        # 0x03
	"Freeze",       # 0x04
	"Jump",         # 0x05
	"Call",         # 0x06
	"Return",       # 0x07
	"For",          # 0x08
	"Done",         # 0x09
	"Repeat",       # 0x0A
	"Until",        # 0x0B
	"JumpIf",       # 0x0C
	"CallIf",       # 0x0D
	"If",           # 0x0E
	"Else",         # 0x0F
	"Endif",        # 0x10
	"Callback",     # 0x11
	"Process",      # 0x12
	"Set",          # 0x13
	"Push",         # 0x14
	"Pull",         # 0x15
	"LoadCode",     # 0x16
	"LoadData",     # 0x17
	"LoadPres",     # 0x18
	"LoadFace",     # 0x19
	"LoadText",     # 0x1A
	"StageInit",    # 0x1B
	"StageExit",    # 0x1C
	"StageStart",   # 0x1D
	"StageEnd",     # 0x1E
	"SceneStart",   # 0x1F
	"SceneEnd",     # 0x20
	"ShapeGfx",     # 0x21
	"Shape",        # 0x22
	"ShapeScale",   # 0x23
	"Obj",          # 0x24
	"Player",       # 0x25
	"Port",         # 0x26
	"BGPort",       # 0x27
	"Connect",      # 0x28
	"SceneOpen",    # 0x29
	"SceneClose",   # 0x2A
	"PlayerOpen",   # 0x2B
	"PlayerClose",  # 0x2C
	"SceneProc",    # 0x2D
	"Map",          # 0x2E
	"Area",         # 0x2F
	"Message",      # 0x30
	"Env",          # 0x31
	None,           # 0x32
	"Wipe",         # 0x33
	"ViBlack",      # 0x34
	"ViGamma",      # 0x35
	"BGM",          # 0x36
	"PlayBGM",      # 0x37
	"AudFadeout",   # 0x38
	"Tag",          # 0x39
	None,           # 0x3A
	"Jet",          # 0x3B
	None,           # 0x3C
]

prg_func = [
	(prg_execute,), # 0x00
	(prg_execute,), # 0x01
	(prg_null,), # 0x02
	(prg_time,), # 0x03
	(prg_time,), # 0x04
	(prg_script, False), # 0x05
	(prg_script, True), # 0x06
	(prg_null,), # 0x07
	None, # 0x08
	None, # 0x09
	(prg_null,), # 0x0A
	(prg_cmp, False), # 0x0B
	(prg_cmp, True), # 0x0C
	None, # 0x0D
	None, # 0x0E
	None, # 0x0F
	None, # 0x10
	(prg_callback,), # 0x11
	(prg_callback,), # 0x12
	(prg_arg,), # 0x13
	None, # 0x14
	None, # 0x15
	(prg_load, True), # 0x16
	(prg_load, False), # 0x17
	(prg_load, False), # 0x18
	(prg_arg,), # 0x19 T:enum(face)
	(prg_load, False), # 0x1A
	(prg_null,), # 0x1B
	(prg_null,), # 0x1C
	(prg_null,), # 0x1D
	(prg_null,), # 0x1E
	(prg_scenestart,), # 0x1F
	(prg_null,), # 0x20
	(prg_shapegfx,), # 0x21
	(prg_shape,), # 0x22
	None, # 0x23
	(prg_object,), # 0x24
	(prg_player,), # 0x25
	(prg_port, "PortMid", False), # 0x26
	(prg_port, "BGPortMid", True), # 0x27
	(prg_connect,), # 0x28
	(prg_scene,), # 0x29
	(prg_scene,), # 0x2A
	(prg_playeropen,), # 0x2B
	None, # 0x2C
	None, # 0x2D
	(prg_script, True), # 0x2E
	(prg_script, True), # 0x2F
	(prg_message,), # 0x30
	(prg_env,), # 0x31
	None, # 0x32
	(prg_wipe,), # 0x33
	(prg_bool,), # 0x34
	None, # 0x35
	(prg_bgm,), # 0x36
	(prg_playbgm,), # 0x37
	(prg_audfadeout,), # 0x38
	(prg_script, True), # 0x39
	None, # 0x3A
	(prg_jet,), # 0x3B
	(prg_var,), # 0x3C
]

prg_inc = {0x08, 0x0A, 0x0E, 0x0F, 0x1D, 0x1F}
prg_dec = {0x09, 0x0B, 0x0F, 0x10, 0x1E, 0x20}

# 00
def obj_init(self, argv):
	type_ = UNSM.fmt.fmt_ot[self.u8()]
	self.addr += 2
	return (None, type_)

# 01
def obj_time(self, argv):
	self.addr += 1
	time = UNSM.fmt.fmt_time(self.s16())
	return (None, time)

# 02 04 0C 2A 37
def obj_script(self, argv):
	g, = argv
	self.addr += 3
	script = ultra.aw(self, self.save) if g else ultra.asm.aw(self)
	return (None, script)

# 03 06 07 08 09 0A (0B) 1D 1E 21 22 2D 35
def obj_null(self, argv):
	self.addr += 3
	return (None,)

# 05 32
def obj_arg(self, argv):
	self.addr += 1
	x = "%d" % self.s16()
	return (None, x)

# 0D 0E 0F 10
def obj_md(self, argv):
	mem = self.u8()
	val = self.s16()
	if mem == 42: val = UNSM.fmt.fmt_hittype(self, val)
	else: val = "%d" % val
	mem = UNSM.fmt.fmt_o[mem]
	return (None, mem, val)

# 11 (12)
def obj_mh(self, argv):
	mem = UNSM.fmt.fmt_o[self.u8()]
	flag = self.u16()
	if mem == "O_FLAG":
		flag = UNSM.fmt.fmt_oflag(self, flag)
	else:
		flag = "0x%04X" % flag
	return (None, mem, flag)

# 13 14 15 16 (17)
def obj_mdd(self, argv):
	mem = UNSM.fmt.fmt_o[self.u8()]
	val = "%d" % self.s16()
	mul = "%d" % self.s16()
	self.addr += 2
	return (None, mem, val, mul)

# 1B
def obj_shape(self, argv):
	self.addr += 1
	shape = UNSM.fmt.fmt_shape(self, self.u16())
	return (None, shape)

# 1C 29 2C
def obj_makeobj(self, argv):
	m, = argv
	self.addr += 1
	code = "%d" % self.s16()
	shape = UNSM.fmt.fmt_shape(self, self.u32())
	script = ultra.aw(self, self.save)
	if m: return (None, shape, script, code)
	return (None, shape, script)

# 1F (20)
def obj_mmm(self, argv):
	mem = UNSM.fmt.fmt_o[self.u8()]
	a   = UNSM.fmt.fmt_o[self.u8()]
	b   = UNSM.fmt.fmt_o[self.u8()]
	return (None, mem, a, b)

# 23 2B 2E
def obj_hitbox(self, argv):
	m, = argv
	self.addr += 3
	radius = "%d" % self.s16()
	height = "%d" % self.s16()
	if m:
		offset = "%d" % self.s16()
		self.addr += 2
		return (None, radius, height, offset)
	return (None, radius, height)

# 25 (26)
def obj_m(self, argv):
	mem = UNSM.fmt.fmt_o[self.u8()]
	self.addr += 2
	return (None, mem)

# 27
def obj_mp(self, argv):
	mem = UNSM.fmt.fmt_o[self.u8()]
	self.addr += 2
	script = ultra.aw(self, self.save)
	return (None, mem, script)

# 28
def obj_anime(self, argv):
	anime = "%d" % self.u8() # T:enum(anime)
	self.addr += 2
	return (None, anime)

# 2F
def obj_hittype(self, argv):
	self.addr += 3
	x = UNSM.fmt.fmt_hittype(self, self.u32())
	return (None, x)

# 30
def obj_physics(self, argv):
	self.addr += 3
	radius      = "%d" % self.s16()
	gravity     = "%d" % self.s16()
	density     = "%d" % self.s16()
	drag        = "%d" % self.s16()
	friction    = "%d" % self.s16()
	bounce      = "%d" % self.s16()
	self.addr += 4
	return (None, radius, gravity, density, drag, friction, bounce)

# 33
def obj_memclrparentflag(self, argv):
	mem = UNSM.fmt.fmt_o[self.u8()]
	self.addr += 2
	flag = "0x%08X" % self.u32() # T:flag(effect)
	return (None, mem, flag)

# 34
def obj_mt(self, argv):
	mem = UNSM.fmt.fmt_o[self.u8()]
	time = UNSM.fmt.fmt_time(self.s16())
	return (None, mem, time)

obj_name = [
	"Init",         # 0x00
	"Sleep",        # 0x01
	"Call",         # 0x02
	"Return",       # 0x03
	"Jump",         # 0x04
	"For",          # 0x05
	"Fend",         # 0x06
	"Fcontinue",    # 0x07
	"While",        # 0x08
	"Wend",         # 0x09
	"Exit",         # 0x0A
	"End",          # 0x0B
	"Callback",     # 0x0C
	"AddF",         # 0x0D
	"SetF",         # 0x0E
	"AddI",         # 0x0F
	"SetI",         # 0x10
	"SetFlag",      # 0x11
	"ClrFlag",      # 0x12
	"SetRandA",     # 0x13
	"SetRandF",     # 0x14
	"SetRandI",     # 0x15
	"AddRandF",     # 0x16
	"AddRandA",     # 0x17
	None,           # 0x18
	None,           # 0x19
	None,           # 0x1A
	"Shape",        # 0x1B
	"MakeObj",      # 0x1C
	"Destroy",      # 0x1D
	"Ground",       # 0x1E
	"MemAddF",      # 0x1F
	"MemAddI",      # 0x20
	"Billboard",    # 0x21
	"Hide",         # 0x22
	"HitBox",       # 0x23
	None,           # 0x24
	"MemSleep",     # 0x25
	"For2",         # 0x26
	"Ptr",          # 0x27
	"Anime",        # 0x28
	"MakeObjCode",  # 0x29
	"Map",          # 0x2A
	"HitBoxOff",    # 0x2B
	"MakeChild",    # 0x2C
	"SavePos",      # 0x2D
	"DmgBox",       # 0x2E
	"HitType",      # 0x2F
	"Physics",      # 0x30
	"HitFlag",      # 0x31
	"Scale",        # 0x32
	"MemClrParentFlag", # 0x33
	"Inc",          # 0x34
	"ClrActive",    # 0x35
	"SetS",         # 0x36
	"Splash",       # 0x37
]

obj_func = [
	(obj_init,), # 0x00
	(obj_time,), # 0x01
	(obj_script, True), # 0x02
	(obj_null,), # 0x03
	(obj_script, False), # 0x04
	(obj_arg,), # 0x05
	(obj_null,), # 0x06
	(obj_null,), # 0x07
	(obj_null,), # 0x08
	(obj_null,), # 0x09
	(obj_null,), # 0x0A
	None, # 0x0B
	(obj_script, True), # 0x0C
	(obj_md,), # 0x0D
	(obj_md,), # 0x0E
	(obj_md,), # 0x0F
	(obj_md,), # 0x10
	(obj_mh,), # 0x11
	None, # 0x12
	(obj_mdd,), # 0x13
	(obj_mdd,), # 0x14
	(obj_mdd,), # 0x15
	(obj_mdd,), # 0x16
	None, # 0x17
	None, # 0x18
	None, # 0x19
	None, # 0x1A
	(obj_shape,), # 0x1B
	(obj_makeobj, False), # 0x1C
	(obj_null,), # 0x1D
	(obj_null,), # 0x1E
	(obj_mmm,), # 0x1F
	None, # 0x20
	(obj_null,), # 0x21
	(obj_null,), # 0x22
	(obj_hitbox, False), # 0x23
	None, # 0x24
	(obj_m,), # 0x25
	None, # 0x26
	(obj_mp,), # 0x27
	(obj_anime,), # 0x28
	(obj_makeobj, True), # 0x29
	(obj_script, True), # 0x2A
	(obj_hitbox, True), # 0x2B
	(obj_makeobj, False), # 0x2C
	(obj_null,), # 0x2D
	(obj_hitbox, False), # 0x2E
	(obj_hittype,), # 0x2F
	(obj_physics,), # 0x30
	None, # 0x31
	(obj_arg,), # 0x32
	(obj_memclrparentflag,), # 0x33
	(obj_mt,), # 0x34
	(obj_null,), # 0x35
	None, # 0x36
	(obj_script, True), # 0x37
]

obj_inc = {0x05, 0x08, 0x26}
obj_dec = {0x06, 0x07, 0x09}

def lang(self, argv, name, func, inc, dec, prefix):
	seg, start, end = argv
	ultra.asm.init(self, seg, start)
	line = []
	tab = 0
	while self.addr < end:
		self.save = self.addr
		c = self.u8()
		if prefix == "p": self.addr += 1
		f = func[c]
		argv = f[0](self, f[1:])
		s = argv[0] if argv[0] is not None else name[c]
		if c in dec: tab -= 1
		ln = "%s%s%s(%s)" % ("\t"*tab, prefix, s, ", ".join(argv[1:]))
		if c in inc: tab += 1
		line.append((self.save, ln))
	ultra.asm.fmt(self, line)

def s_prglang(self, argv):
	lang(self, argv, prg_name, prg_func, prg_inc, prg_dec, "p")

def s_objlang(self, argv):
	lang(self, argv, obj_name, obj_func, obj_inc, obj_dec, "o")

def stbl_add(stbl, i, t, s):
	if i not in stbl: stbl[i] = [t]
	stbl[i].append(s)

def etbl_add(etbl, i, s):
	if i not in etbl: etbl[i] = []
	etbl[i].append(s)

def bank_init(self, argv):
	seg, end, name, tbl = argv
	ultra.asm.init(self, seg, 0)
	cnt = self.u32()
	self.addr += 4
	line = self.file[-1][1]
	stbl = {}
	etbl = {}
	line.append("TABLE()\ntable:\n")
	for i in range(cnt):
		s = "%s_%s" % (name, tbl[0][i])
		line.append("\tBANK(%s)\n" % s)
		start = self.u32()
		size  = self.u32()
		stbl_add(stbl, start, 0, s)
		etbl_add(etbl, start+size, s)
	line.append("table_end:\n\n")
	return end, name, tbl, cnt, line, stbl, etbl

def bank_s(self, line, stbl):
	self.save = self.addr
	if self.addr in stbl:
		label = stbl[self.addr]
		line.append("\n")
		for s in label[1:]: line.append("%s:\n" % s)
		return label
	return None

def bank_e(self, line, etbl):
	if self.addr in etbl:
		for s in etbl[self.addr]: line.append("%s_end:\n" % s)
		return True
	return False

def s_anime(self, argv):
	end, name, tbl, cnt, line, stbl, etbl = bank_init(self, argv)
	init = True
	i = 0
	while self.addr < end:
		if init:
			fn = (tbl[1][i] if i in tbl[1] else tbl[0][i]) + ".sx"
			line.append("#include \"%s/%s\"\n" % (name, fn))
			c = [".balign 4\n"]
		label = bank_s(self, c, stbl)
		if label is not None:
			t = label[0]
			if t == 0: s = label[-1]
		init = False
		# anime
		if t == 0:
			a_flag  = UNSM.fmt.fmt_anime_flag(self, self.s16())
			a_waist = self.s16()
			a_start = self.s16()
			a_loop  = self.s16()
			a_frame = self.s16()
			a_joint = self.s16()
			a_val   = self.save + self.u32()
			a_tbl   = self.save + self.u32()
			a_siz   = self.save + self.u32()
			stbl_add(stbl, a_val, 1, s + "_val")
			stbl_add(stbl, a_tbl, 2, s + "_tbl")
			c.append((
				"\tANIME(%s, %s, %d, %d, %d, %d, %d)\n"
			) % (s, a_flag, a_waist, a_start, a_loop, a_frame, a_joint))
			i += 1
		# val
		elif t == 1:
			c.append("\t.short %s\n" % ", ".join([
				# "0x%04X" % self.u16()
				"%6d" % self.s16()
				for _ in range(min(8, (a_siz-self.save)//2))
			]))
			if self.addr == a_siz: c.append("\n")
		# tbl
		elif t == 2:
			c.append("\t.short %s\n" % ", ".join([
				"%5d" % self.u16()
				for _ in range(6)
			]))
		else:
			raise RuntimeError("bad mode")
		if bank_e(self, c, etbl):
			data = main.line_prc(c)
			fn = self.path_join([name, fn])
			main.mkdir(fn)
			with open(fn, "w") as f: f.write(data)
			self.addr = (self.addr+3) & ~3
			init = True

def s_demo(self, argv):
	end, name, tbl, cnt, line, stbl, etbl = bank_init(self, argv)
	while self.addr < end:
		if bank_s(self, line, stbl) is not None:
			stage = UNSM.fmt.fmt_stage[self.u8()]
			self.addr += 3
			line.append("\tDEMO(%s)\n" % stage)
		else:
			count   = self.u8()
			stick_x = self.s8()
			stick_y = self.s8()
			button  = self.u8()
			line.append("\t.byte %3d, %3d, %3d, 0x%02X\n" % (
				count, stick_x, stick_y, button
			))
		bank_e(self, line, etbl)

def pstr(s):
	if not len(s) & 1: s += B"\0"
	return struct.pack(">B", len(s)) + s

def iff_chunk(code, data):
	return struct.pack(">4sI", code, len(data)) + data

def aifc_pack(rate, wave, book=None, loop=None):
	x, = struct.unpack(">Q", struct.pack(">d", rate))
	e = 0x3FFF + (x >> 52)-0x3FF
	f = 1 << 63 | (x & 0xFFFFFFFFFFFFF) << 11
	data = B"AIFC"
	data += iff_chunk(
		B"COMM", struct.pack(">HIHHQ", 1, 16*len(wave)//9, 16, e, f) +
		B"VAPC" + pstr(B"VADPCM ~4-1")
	)
	if book: data += iff_chunk(
		B"APPL", B"stoc" + pstr(B"VADPCMCODES") +
		struct.pack(">HHH", 1, book[0], book[1]) + book[2]
	)
	if loop: data += iff_chunk(
		B"APPL", B"stoc" + pstr(B"VADPCMLOOPS") +
		struct.pack(">HHIII", 1, 1, loop[0], loop[1], loop[2]) +
		(loop[3] if loop[2] > 0 else struct.pack(">32x"))
	)
	data += iff_chunk(B"SSND", struct.pack(">II", 0, 0) + wave)
	if len(data) & 1: data += B"\0"
	return iff_chunk(B"FORM", data)

def al_book(self, ctl, book):
	if not book: return None
	self.addr = ctl+book
	order       = self.u32()
	npredictors = self.u32()
	book = self.c_next(16 << npredictors)
	return (order, npredictors, book)

def al_loop(self, ctl, loop):
	if not loop: return None
	self.addr = ctl+loop
	start = self.u32()
	end   = self.u32()
	count = self.u32()
	if count > 0:
		self.addr += 4
		state = self.c_next(32)
		return (start, end, count, state)
	return (start, end, count)

def al_sound(self, ctlseg, tblseg, bankdata, wavedata, ctl, tbl, snd, key):
	if not snd: return None
	self.addr = ctl+snd
	self.addr += 4
	wave = self.u32()
	loop = self.u32()
	book = self.u32()
	size = self.u32()
	x = key
	key *= 32000
	wave += tbl
	self.seg = tblseg
	imm = self.get_imm(wave)
	self.seg = ctlseg
	rate = imm[0] if imm[0] is not None else int(round(key))
	name = imm[1]
	if wave not in wavedata:
		path = imm[2]
		book = al_book(self, ctl, book)
		loop = al_loop(self, ctl, loop)
		wavedata[wave] = [size, book, loop, rate, path, name]
	return (name, int(round(12*math.log2(round(key/rate, 6)))))

def al_envelope(self, bankdata, ctl, env):
	self.addr = ctl+env
	if env not in bankdata[1]:
		envelope = []
		while True:
			envelope.append((self.s16(), self.s16()))
			if envelope[-1][0] in {-1, -2, -3}: break
		name = "env%d" % bankdata[0]
		bankdata[0] += 1
		bankdata[1][env] = (name, ", ".join("%d, %d" % x for x in envelope))

def al_note(x):
	return (
		"C", "Cs", "D", "Eb", "E",
		"F", "Fs", "G", "Ab", "A", "Bb", "B",
	)[(x+9) % 12] + "%d" % ((x+9) // 12)

def al_instrument(self, ctlseg, tblseg, bankdata, wavedata, ctl, tbl, inst, i):
	if not inst: return
	self.save = self.addr
	self.addr = ctl+inst
	self.addr += 1
	min_ = self.u8()
	max_ = self.u8()
	rel = self.u8()
	env = self.u32()
	sound = [(self.u32(), self.f()) for i in range(3)]
	al_envelope(self, bankdata, ctl, env)
	self.addr = (self.addr+15) & ~15
	if self.addr in {0x1C30, 0x1CA0}:
		al_envelope(self, bankdata, ctl, self.addr-ctl)
	sound = [
		al_sound(self, ctlseg, tblseg, bankdata, wavedata, ctl, tbl, snd, key)
		for snd, key in sound
	]
	bankdata[2].append((
		"\tinstrument[%d] =\n"
		"\t{\n"
		"\t\trelease = %d;\n"
		"\t\tenvelope = %s;\n"
	) % (i, rel, bankdata[1][env][0]))
	if sound[0] is not None: bankdata[2].append((
		"\t\tsoundL = {%s, %s, %s};\n"
	) % (al_note(min_), sound[0][0], al_note(39-sound[0][1])))
	bankdata[2].append((
		"\t\tsound = {%s, %s};\n"
	) % (               sound[1][0], al_note(39-sound[1][1])))
	if sound[2] is not None: bankdata[2].append((
		"\t\tsoundH = {%s, %s, %s};\n"
	) % (al_note(max_), sound[2][0], al_note(39-sound[2][1])))
	bankdata[2].append("\t};\n")
	self.addr = self.save

def al_percussion(self, ctlseg, tblseg, bankdata, wavedata, ctl, tbl, perc, i):
	if not perc: return
	self.save = self.addr
	self.addr = ctl+perc
	rel = self.u8()
	pan = self.u8()
	self.addr += 2
	snd, key = self.u32(), self.f()
	env = self.u32()
	al_envelope(self, bankdata, ctl, env)
	snd, note = al_sound(
		self, ctlseg, tblseg, bankdata, wavedata, ctl, tbl, snd, key
	)
	bankdata[2].append((
		"\tpercussion[%d] =\n"
		"\t{\n"
		"\t\trelease = %d;\n"
		"\t\tpan = %d;\n"
		"\t\tenvelope = %s;\n"
		"\t\tsound = {%s, %s};\n"
		"\t};\n"
	) % (i, rel, pan, bankdata[1][env][0], snd, al_note(39+note)))
	self.addr = self.save

def s_audio_ctltbl(self, argv):
	ctlseg, tblseg, ctlname, tblname = argv
	line = self.file[-1][1]
	wavetbl = {i: {} for i in tblname}
	banktbl = {}
	ultra.asm.init(self, tblseg, 0)
	self.addr += 2
	cnt = self.u16()
	for i in range(cnt):
		start = self.u32()
		self.addr += 4
		if i not in ctlname: continue
		banktbl[i] = [[0, {}, []], wavetbl[start], 0, start]
	ultra.asm.init(self, ctlseg, 0)
	self.addr += 2
	cnt = self.u16()
	for i in range(cnt):
		start = self.u32()
		self.addr += 4
		if i not in ctlname: continue
		self.save = self.addr
		self.addr = start
		icnt = self.u32()
		pcnt = self.u32()
		flag = self.u32()
		date = self.u32()
		banktbl[i][2] = self.addr
		banktbl[i].extend([icnt, pcnt, flag, date])
		self.addr = self.save
	for i in banktbl:
		bankdata, wavedata, ctl, tbl, icnt, pcnt, flag, date = banktbl[i]
		ultra.asm.init(self, ctlseg, ctl)
		imm = self.get_imm(ctl)
		perc = self.u32()
		itbl = [self.u32() for i in range(icnt)]
		self.addr = ctl+perc
		ptbl = [self.u32() for i in range(pcnt)]
		for inst in sorted(itbl):
			i = itbl.index(inst)
			if i == imm:
				for perc in sorted(ptbl):
					p = ptbl.index(perc)
					al_percussion(
						self, ctlseg, tblseg, bankdata, wavedata, ctl, tbl,
						perc, p
					)
			al_instrument(
				self, ctlseg, tblseg, bankdata, wavedata, ctl, tbl, inst, i
			)
	for tbl in sorted(wavetbl.keys()):
		wavedata = wavetbl[tbl]
		line.append("wave %s\n{\n" % tblname[tbl])
		for wave in sorted(wavedata.keys()):
			size, book, loop, rate, path, name = wavedata[wave]
			wave = self.segment[tblseg][wave:wave+size]
			data = aifc_pack(rate, wave, book, loop)
			fn = self.path_join(path)
			main.mkdir(fn)
			with open(fn, "wb") as f: f.write(data)
			line.append("\tsound %s \"%s\";\n" % (name, "/".join(path)))
		line.append("};\n\n")
	for i in sorted(banktbl.keys()):
		bankdata, wavedata, ctl, tbl, icnt, pcnt, flag, date = banktbl[i]
		line.append("bank %s\n{\n" % ctlname[i])
		line.append("\tdate = {%X, %X, %X};\n" % (
			date >> 16, date >> 8 & 0xFF, date >> 0 & 0xFF
		))
		line.append("\twave %s;\n" % tblname[tbl])
		for env in sorted(bankdata[1].keys()):
			line.append("\tenvelope %s {%s};\n" % bankdata[1][env])
		line += bankdata[2]
		line.append("};\n\n")

def s_audio_seqbnk(self, argv):
	seq, bnk, path = argv
	line = self.file[-1][1]
	ultra.asm.init(self, seq, 0)
	self.addr += 2
	cnt = self.u16()
	for i in range(cnt):
		start = self.u32()
		size  = self.u32()
		imm = self.get_imm(start)
		if imm is not None: size = imm
		data = self.segment[seq][start:start+size]
		fn = self.path_join(path[i])
		main.mkdir(fn)
		with open(fn, "wb") as f: f.write(data)
	ultra.asm.init(self, bnk, 0)
	for i in range(cnt):
		start = self.u16()
		self.save = self.addr
		self.addr = start
		line.append("%s\n" % " ".join([
			"%d" % self.u8() for _ in range(self.u8())
		]))
		self.addr = self.save
