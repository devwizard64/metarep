import struct
import math

import main
import table
import ultra
import UNSM

def d_prg_prc(argv):
	ultra.script.c_addr += 6
	dst = ultra.ah()
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
	0x0A: "SEG_BACK",
	0x0B: "SEG_WEATHER",
	0x0C: "SEG_SHAPE1_DATA",
	0x0D: "SEG_SHAPE2_DATA",
	0x0E: "SEG_STAGE_DATA",
	0x0F: "SEG_SHAPE3_DATA",
	0x13: "SEG_OBJECT",
	0x14: "SEG_MENU_DATA",
	0x15: "SEG_GAME",
	0x16: "SEG_GLOBAL_DATA",
	0x17: "SEG_PLAYER_DATA",
}

# 00 01
def prg_execute(argv):
	seg    = ultra.uh()
	start  = ultra.uw()
	end    = ultra.uw()
	script = ultra.uw()
	dev = ultra.script.addr + start
	start  = ultra.sym(start,  dev)
	# end    = ultra.sym(end,    dev)
	if not start.endswith("SegmentRomStart"):
		raise RuntimeError("prg_execute(): bad segment")
	end    = start[:-5] + "End"
	script = ultra.sym(script, dev)
	seg = seg_table[seg]
	return (None, seg, start, end, script)

# 02 07 0A 1B 1C 1D 1E 20
def prg_null(argv):
	ultra.script.c_addr += 2
	return (None,)

# 03 04
def prg_time(argv):
	time = UNSM.table.fmt_time(ultra.sh())
	return (None, time)

# 05 06 2E 2F 39
def prg_script(argv):
	g, = argv
	ultra.script.c_addr += 2
	script = ultra.aw() if g else ultra.asm.aw()
	return (None, script)

# (08) (09)

# 0B 0C
def prg_cmp(argv):
	s, = argv
	cmp_ = ("AND", "NAND", "EQ", "NE", "LT", "LE", "GT", "GE")[ultra.ub()]
	ultra.script.c_addr += 1
	val = "%d" % ultra.sw()
	if s:
		script = ultra.asm.aw()
		return (None, cmp_, val, script)
	return (None, cmp_, val)

# (0D) (0E) (0F) (10)

# 11 12
def prg_callback(argv):
	arg = "%d" % ultra.uh()
	callback = ultra.aw()
	return (None, callback, arg)

# 13 19
def prg_arg(argv):
	x = "%d" % ultra.sh()
	return (None, x)

# (14) (15)

# 16 17 18 1A
def prg_load(argv):
	flag, = argv
	seg   = ultra.uh()
	if flag: addr = ultra.uw()
	start = ultra.uw()
	end   = ultra.uw()
	dev   = ultra.script.addr + start
	# if flag: addr = ultra.sym(addr, dev)
	start = ultra.sym(start, dev)
	# end   = ultra.sym(end,   dev)
	if not start.endswith("SegmentRomStart"):
		raise RuntimeError("p_load(): bad segment")
	if flag: addr = start[:-8] + "Start"
	end = start[:-5] + "End"
	if flag: return (None, addr, start, end)
	seg = seg_table[seg]
	return (None, seg, start, end)

# 1F
def prg_scene_start(argv):
	scene = "%d" % ultra.ub()
	ultra.script.c_addr += 1
	script = ultra.aw()
	return (None, scene, script)

# 21
def prg_shape_gfx(argv):
	x = ultra.uh()
	layer = UNSM.table.fmt_layer(x >> 12)
	shape = UNSM.table.fmt_shape(x & 0x0FFF)
	ultra.tag = "gfx"
	gfx = ultra.aw()
	return (None, shape, gfx, layer)

# 22
def prg_shape_script(argv):
	shape = UNSM.table.fmt_shape(ultra.uh())
	script = ultra.aw()
	return (None, shape, script)

# (23)

# 24
def prg_object(argv):
	mask = ultra.ub()
	shape = UNSM.table.fmt_shape(ultra.ub())
	px = "%d" % ultra.sh()
	py = "%d" % ultra.sh()
	pz = "%d" % ultra.sh()
	ax = "%d" % ultra.sh()
	ay = "%d" % ultra.sh()
	az = "%d" % ultra.sh()
	arg0 = "%d" % ultra.ub()
	arg1 = "%d" % ultra.ub()
	flag = "%d" % ultra.uh()
	script = ultra.aw()
	if mask != 0x1F:
		mask = "0%02o" % mask
		return (
			"Obj", mask, shape, px, py, pz, ax, ay, az,
			arg0, arg1, flag, script
		)
	return (None, shape, px, py, pz, ax, ay, az, arg0, arg1, flag, script)

# 25
def prg_player(argv):
	shape = UNSM.table.fmt_shape(ultra.uh())
	arg0 = ultra.ub()
	arg1 = ultra.ub()
	flag = ultra.uh()
	script = ultra.aw()
	if (shape, arg0, arg1, flag, script) == ("S_MARIO", 0, 0, 1, "o_mario"):
		return ("Mario",)
	arg0 = "%d" % arg0
	arg1 = "%d" % arg1
	flag = "%d" % flag # T:flag
	return (None, shape, arg0, arg1, flag, script)

# 26 27
def prg_port(argv):
	m, = argv
	index = "%d" % ultra.ub()
	stage = UNSM.table.fmt_stage(ultra.ub())
	scene = "%d" % ultra.ub()
	port  = "%d" % ultra.ub()
	flag  = ultra.ub()
	ultra.script.c_addr += 1
	return (m if flag == 0x80 else None, index, stage, scene, port)

# 28
def prg_connect(argv):
	index = "%d" % ultra.ub()
	scene = "%d" % ultra.ub()
	px = "%d" % ultra.sh()
	py = "%d" % ultra.sh()
	pz = "%d" % ultra.sh()
	ultra.script.c_addr += 2
	return (None, index, scene, px, py, pz)

# 29 2A
def prg_scene(argv):
	scene = "%d" % ultra.ub()
	ultra.script.c_addr += 1
	return (None, scene)

# 2B
def prg_player_open(argv):
	scene = "%d" % ultra.ub()
	ultra.script.c_addr += 1
	ay = "%d" % ultra.sh()
	px = "%d" % ultra.sh()
	py = "%d" % ultra.sh()
	pz = "%d" % ultra.sh()
	return (None, scene, ay, px, py, pz)

# (2C) (2D)

# 30
def prg_msg(argv):
	type_ = "%d" % ultra.ub() # T:enum(msgtype)
	msg   = UNSM.table.fmt_msg(ultra.ub())
	return (None, type_, msg)

# 31
def prg_env(argv):
	env = (
		"ENV_GRASS",
		"ENV_ROCK",
		"ENV_SNOW",
		"ENV_SAND",
		"ENV_GHOST",
		"ENV_WATER",
		"ENV_SLIDER",
	)[ultra.sh()]
	return (None, env)

# 33
def prg_wipe(argv):
	type_ = "0x%02X" % ultra.ub() # T:enum(wipe)
	time  = UNSM.table.fmt_time(ultra.ub())
	r     = "0x%02X" % ultra.ub()
	g     = "0x%02X" % ultra.ub()
	b     = "0x%02X" % ultra.ub()
	ultra.script.c_addr += 1
	return (None, type_, time, r, g, b)

# 34
def prg_bool(argv):
	x = ultra.fmt_bool[ultra.ub()]
	ultra.script.c_addr += 1
	return (None, x)

# (35)

# 36
def prg_bgm(argv):
	mode = UNSM.table.fmt_na_mode(ultra.uh())
	bgm  = UNSM.table.fmt_na_bgm(ultra.uh())
	ultra.script.c_addr += 2
	return (None, mode, bgm)

# 37
def prg_bgm_play(argv):
	bgm = UNSM.table.fmt_na_bgm(ultra.uh())
	return (None, bgm)

# 38
def prg_bgm_stop(argv):
	time = "%d" % (ultra.sh()+2) # T:audtime
	return (None, time)

# (3A)

# 3B
def prg_jet(argv):
	index = "%d" % ultra.ub()
	mode  = "%d" % ultra.ub()
	px    = "%d" % ultra.sh()
	py    = "%d" % ultra.sh()
	pz    = "%d" % ultra.sh()
	arg   = "%d" % ultra.sh()
	return (None, index, mode, px, py, pz, arg)

# 3C
def prg_var(argv):
	cmd = (
		"Store",
		"Load",
	)[ultra.ub()]
	var = (
		"SAVE",
		"COURSE",
		"LEVEL",
		"STAGE",
		"SCENE",
	)[ultra.ub()]
	return (cmd, var)

prg_str = [
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
	"LoadSzp",      # 0x18
	"LoadFace",     # 0x19
	"LoadTxt",      # 0x1A
	"StageInit",    # 0x1B
	"StageExit",    # 0x1C
	"StageStart",   # 0x1D
	"StageEnd",     # 0x1E
	"SceneStart",   # 0x1F
	"SceneEnd",     # 0x20
	"ShapeGfx",     # 0x21
	"ShapeScript",  # 0x22
	"ShapeScale",   # 0x23
	"Object",       # 0x24
	"Player",       # 0x25
	"Port",         # 0x26
	"BGPort",       # 0x27
	"Connect",      # 0x28
	"SceneOpen",    # 0x29
	"SceneClose",   # 0x2A
	"PlayerOpen",   # 0x2B
	"PlayerClose",  # 0x2C
	"SceneUpdate",  # 0x2D
	"Map",          # 0x2E
	"Area",         # 0x2F
	"Msg",          # 0x30
	"Env",          # 0x31
	None,           # 0x32
	"Wipe",         # 0x33
	"ViBlack",      # 0x34
	"ViGamma",      # 0x35
	"Bgm",          # 0x36
	"BgmPlay",      # 0x37
	"BgmStop",      # 0x38
	"Tag",          # 0x39
	"Wind",         # 0x3A
	"Jet",          # 0x3B
	None,           # 0x3C
]

prg_fnc = [
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
	(prg_scene_start,), # 0x1F
	(prg_null,), # 0x20
	(prg_shape_gfx,), # 0x21
	(prg_shape_script,), # 0x22
	None, # 0x23
	(prg_object,), # 0x24
	(prg_player,), # 0x25
	(prg_port, "PortMid"), # 0x26
	(prg_port, "BGPortMid"), # 0x27
	(prg_connect,), # 0x28
	(prg_scene,), # 0x29
	(prg_scene,), # 0x2A
	(prg_player_open,), # 0x2B
	None, # 0x2C
	None, # 0x2D
	(prg_script, True), # 0x2E
	(prg_script, True), # 0x2F
	(prg_msg,), # 0x30
	(prg_env,), # 0x31
	None, # 0x32
	(prg_wipe,), # 0x33
	(prg_bool,), # 0x34
	None, # 0x35
	(prg_bgm,), # 0x36
	(prg_bgm_play,), # 0x37
	(prg_bgm_stop,), # 0x38
	(prg_script, True), # 0x39
	None, # 0x3A
	(prg_jet,), # 0x3B
	(prg_var,), # 0x3C
]

prg_inc = {0x08, 0x0A, 0x0E, 0x0F, 0x1D, 0x1F}
prg_dec = {0x09, 0x0B, 0x0F, 0x10, 0x1E, 0x20}

# 00
def obj_init(argv):
	type_ = UNSM.table.fmt_o_type(ultra.ub())
	ultra.script.c_addr += 2
	return (None, type_)

# 01
def obj_time(argv):
	ultra.script.c_addr += 1
	time = UNSM.table.fmt_time(ultra.sh())
	return (None, time)

# 02 04 0C 2A 37
def obj_script(argv):
	g, = argv
	ultra.script.c_addr += 3
	script = ultra.aw() if g else ultra.asm.aw()
	return (None, script)

# 03 06 07 08 09 0A (0B) 1D 1E 21 22 2D 35
def obj_null(argv):
	ultra.script.c_addr += 3
	return (None,)

# 05 32
def obj_arg(argv):
	ultra.script.c_addr += 1
	x = "%d" % ultra.sh()
	return (None, x)

# 0D 0E 0F 10
def obj_md(argv):
	mem = UNSM.table.fmt_o_mem[ultra.ub()]
	val = "%d" % ultra.sh()
	return (None, mem, val)

# 11 (12)
def obj_mh(argv):
	mem = UNSM.table.fmt_o_mem[ultra.ub()]
	val = "0x%04X" % ultra.uh()
	return (None, mem, val)

# 13 14 15 16 (17)
def obj_mdd(argv):
	mem = UNSM.table.fmt_o_mem[ultra.ub()]
	val = "%d" % ultra.sh()
	mul = "%d" % ultra.sh()
	ultra.script.c_addr += 2
	return (None, mem, val, mul)

# 1B
def obj_shape(argv):
	ultra.script.c_addr += 1
	shape = UNSM.table.fmt_shape(ultra.uh())
	return (None, shape)

# 1C 29 2C
def obj_object(argv):
	m, = argv
	ultra.script.c_addr += 1
	arg = "%d" % ultra.sh()
	shape = UNSM.table.fmt_shape(ultra.uw())
	script = ultra.aw()
	if m: return (None, shape, script, arg)
	return (None, shape, script)

# 1F (20)
def obj_mmm(argv):
	mem = UNSM.table.fmt_o_mem[ultra.ub()]
	a   = UNSM.table.fmt_o_mem[ultra.ub()]
	b   = UNSM.table.fmt_o_mem[ultra.ub()]
	return (None, mem, a, b)

# 23 2B 2E
def obj_collision(argv):
	m, = argv
	ultra.script.c_addr += 3
	radius = "%d" % ultra.sh()
	height = "%d" % ultra.sh()
	if m:
		offset = "%d" % ultra.sh()
		ultra.script.c_addr += 2
		return (None, radius, height, offset)
	return (None, radius, height)

# 25 (26)
def obj_m(argv):
	mem = UNSM.table.fmt_o_mem[ultra.ub()]
	ultra.script.c_addr += 2
	return (None, mem)

# 27
def obj_mp(argv):
	mem = UNSM.table.fmt_o_mem[ultra.ub()]
	ultra.script.c_addr += 2
	script = ultra.aw()
	return (None, mem, script)

# 28
def obj_anime(argv):
	anime = "0x%02X" % ultra.ub() # T:enum(anime)
	ultra.script.c_addr += 2
	return (None, anime)

# 2F (31) (36)
def obj_w(argv):
	ultra.script.c_addr += 3
	x = "0x%08X" % ultra.uw()
	return (None, x)

# 30
def obj_physics(argv):
	ultra.script.c_addr += 3
	a = "%d" % ultra.sh()
	b = "%d" % ultra.sh()
	c = "%d" % ultra.sh()
	d = "%d" % ultra.sh()
	e = "%d" % ultra.sh()
	f = "%d" % ultra.sh()
	g = "%d" % ultra.sh()
	h = "%d" % ultra.sh()
	return (None, a, b, c, d, e, f, g, h)

# 33
def obj_memclrflag(argv):
	mem = UNSM.table.fmt_o_mem[ultra.ub()]
	ultra.script.c_addr += 2
	flag = "0x%08X" % ultra.uw() # T:flag
	return (None, mem, flag)

# 34
def obj_mt(argv):
	mem = UNSM.table.fmt_o_mem[ultra.ub()]
	time = UNSM.table.fmt_time(ultra.sh())
	return (None, mem, time)

obj_str = [
	"Init",     # 0x00
	"Sleep",    # 0x01
	"Call",     # 0x02
	"Return",   # 0x03
	"Jump",     # 0x04
	"For",      # 0x05
	"Fend",     # 0x06
	"Fcontinue",    # 0x07
	"While",    # 0x08
	"Wend",     # 0x09
	"Exit",     # 0x0A
	"End",      # 0x0B
	"Callback", # 0x0C
	"AddF",     # 0x0D
	"SetF",     # 0x0E
	"AddI",     # 0x0F
	"SetI",     # 0x10
	"SetFlag",  # 0x11
	"ClrFlag",  # 0x12
	"SetRandA", # 0x13
	"SetRandF", # 0x14
	"SetRandI", # 0x15
	"AddRandF", # 0x16
	"AddRandA", # 0x17
	None,       # 0x18
	None,       # 0x19
	None,       # 0x1A
	"Shape",    # 0x1B
	"Object",   # 0x1C
	"Destroy",  # 0x1D
	"Ground",   # 0x1E
	"MemAddF",  # 0x1F
	"MemAddI",  # 0x20
	"Billboard",    # 0x21
	"ShapeHide",    # 0x22
	"ColHit",   # 0x23
	None,       # 0x24
	"MemSleep", # 0x25
	"For2",     # 0x26
	"Ptr",      # 0x27
	"Anime",    # 0x28
	"ObjectArg",    # 0x29
	"Map",      # 0x2A
	"ColOff",   # 0x2B
	"Child",    # 0x2C
	"Origin",   # 0x2D
	"ColDmg",   # 0x2E
	"ColType",  # 0x2F
	"Physics",  # 0x30
	"ColArg",   # 0x31
	"Scale",    # 0x32
	"MemClrFlag",   # 0x33
	"Inc",      # 0x34
	"ShapeDisable", # 0x35
	"SetS",     # 0x36
	"Splash",   # 0x37
]

obj_fnc = [
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
	(obj_mh,), # 0x11 T:flag
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
	(obj_object, False), # 0x1C
	(obj_null,), # 0x1D
	(obj_null,), # 0x1E
	(obj_mmm,), # 0x1F
	None, # 0x20
	(obj_null,), # 0x21
	(obj_null,), # 0x22
	(obj_collision, False), # 0x23
	None, # 0x24
	(obj_m,), # 0x25
	None, # 0x26
	(obj_mp,), # 0x27
	(obj_anime,), # 0x28
	(obj_object, True), # 0x29
	(obj_script, True), # 0x2A
	(obj_collision, True), # 0x2B
	(obj_object, False), # 0x2C
	(obj_null,), # 0x2D
	(obj_collision, False), # 0x2E
	(obj_w,), # 0x2F T:flag
	(obj_physics,), # 0x30
	None, # 0x31
	(obj_arg,), # 0x32
	(obj_memclrflag,), # 0x33
	(obj_mt,), # 0x34
	(obj_null,), # 0x35
	None, # 0x36
	(obj_script, True), # 0x37
]

obj_inc = {0x05, 0x08, 0x26}
obj_dec = {0x06, 0x07, 0x09}

scr_table = [
	(prg_str, prg_fnc, prg_inc, prg_dec, "p"),
	(obj_str, obj_fnc, obj_inc, obj_dec, "o"),
]

def s_script(self, argv):
	start, end, data, i = argv
	ultra.asm.init(self, start, data)
	s_str, s_fnc, s_inc, s_dec, s_t = scr_table[i]
	line = []
	tab = 0
	while self.c_addr < end:
		self.c_push()
		c = ultra.ub()
		if i == 0: self.c_addr += 1
		f = s_fnc[c]
		scrtbl = {
			0x22: "s_script",
			0x2E: "map",
			0x2F: "area",
			0x39: "tag",
		}
		objtbl = {
			0x27: "anime",
			0x2A: "map",
			0x37: "splash",
		}
		if i == 0 and c in scrtbl: ultra.tag = scrtbl[c]
		if i == 1 and c in objtbl: ultra.tag = objtbl[c]
		argv = f[0](f[1:])
		s = argv[0] if argv[0] != None else s_str[c]
		if c in s_dec: tab -= 1
		ln = "%s%s%s(%s)" % ("\t"*tab, s_t, s, ", ".join(argv[1:]))
		if c in s_inc: tab += 1
		line.append((self.c_dst, ln))
	ultra.asm.fmt(self, line)

def stbl_add(stbl, i, t, s):
	if i not in stbl: stbl[i] = [t]
	stbl[i].append(s)

def etbl_add(etbl, i, s):
	if i not in etbl: etbl[i] = []
	etbl[i].append(s)

def bank_init(self, argv):
	end, data, name, tbl = argv
	ultra.asm.init(self, 0, data)
	cnt = ultra.uw()
	self.c_addr += 4
	line = self.file[-1][1]
	stbl = {}
	etbl = {}
	line.append("TABLE()\ntable:\n")
	for i in range(cnt):
		s = "%s_%s" % (name, tbl[0][i])
		line.append("\tBANK(%s)\n" % s)
		start = ultra.uw()
		size  = ultra.uw()
		stbl_add(stbl, start, 0, s)
		etbl_add(etbl, start+size, s)
	line.append("table_end:\n\n")
	return end, name, tbl, cnt, line, stbl, etbl

def bank_s(self, line, stbl):
	self.c_push()
	if self.c_addr in stbl:
		label = stbl[self.c_addr]
		line.append("\n")
		for s in label[1:]: line.append("%s:\n" % s)
		return label
	return None

def bank_e(self, line, etbl):
	if self.c_addr in etbl:
		for s in etbl[self.c_addr]: line.append("%s_end:\n" % s)
		return True
	return False

def s_anime(self, argv):
	end, name, tbl, cnt, line, stbl, etbl = bank_init(self, argv)
	init = True
	i = 0
	while self.c_addr < end:
		if init:
			fn = (tbl[1][i] if i in tbl[1] else tbl[0][i]) + ".sx"
			line.append("#include \"%s/%s\"\n" % (name, fn))
			c = [".balign 4\n"]
		label = bank_s(self, c, stbl)
		if label != None:
			t = label[0]
			if t == 0: s = label[-1]
		init = False
		# anime
		if t == 0:
			a_flag  = UNSM.table.fmt_anime_flag(ultra.sh())
			a_waist = ultra.sh()
			a_start = ultra.sh()
			a_loop  = ultra.sh()
			a_frame = ultra.sh()
			a_joint = ultra.sh()
			a_val   = self.c_dst + ultra.uw()
			a_tbl   = self.c_dst + ultra.uw()
			a_siz   = self.c_dst + ultra.uw()
			stbl_add(stbl, a_val, 1, s + "_val")
			stbl_add(stbl, a_tbl, 2, s + "_tbl")
			c.append((
				"\tANIME(%s, %s, %d, %d, %d, %d, %d)\n"
			) % (s, a_flag, a_waist, a_start, a_loop, a_frame, a_joint))
			i += 1
		# val
		elif t == 1:
			c.append("\t.short %s\n" % ", ".join([
				# "0x%04X" % ultra.uh()
				"%6d" % ultra.sh()
				for _ in range(min(8, (a_siz-self.c_dst)//2))
			]))
			if self.c_addr == a_siz: c.append("\n")
		# tbl
		elif t == 2:
			c.append("\t.short %s\n" % ", ".join([
				"%5d" % ultra.uh()
				for _ in range(6)
			]))
		else:
			raise RuntimeError("bad mode")
		if bank_e(self, c, etbl):
			data = main.line_prc(c)
			fn = self.path_join([name, fn])
			main.mkdir(fn)
			with open(fn, "w") as f: f.write(data)
			self.c_addr = (self.c_addr+3) & ~3
			init = True

def s_demo(self, argv):
	end, name, tbl, cnt, line, stbl, etbl = bank_init(self, argv)
	while self.c_addr < end:
		if bank_s(self, line, stbl) != None:
			stage = UNSM.table.fmt_stage(ultra.ub())
			self.c_addr += 3
			line.append("\tDEMO(%s)\n" % stage)
		else:
			count   = ultra.ub()
			stick_x = ultra.sb()
			stick_y = ultra.sb()
			button  = ultra.ub()
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

def al_book(self, book):
	if book == 0: return None
	self.c_addr = book
	order       = ultra.uw()
	npredictors = ultra.uw()
	book = self.c_next(16 << npredictors)
	return (order, npredictors, book)

def al_loop(self, loop):
	if loop == 0: return None
	self.c_addr = loop
	start = ultra.uw()
	end   = ultra.uw()
	count = ultra.uw()
	if count > 0:
		self.c_addr += 4
		state = self.c_next(32)
		return (start, end, count, state)
	return (start, end, count)

def al_sound(self, bankdata, wavedata, tbl, snd, key):
	if snd == 0: return None
	self.c_addr = snd
	self.c_addr += 4
	wave = ultra.uw()
	loop = ultra.uw()
	book = ultra.uw()
	size = ultra.uw()
	x = key
	key *= 32000
	wave = tbl+wave
	imm = table.imm_addr(self, wave)
	rate = imm[0] if imm[0] != None else int(round(key))
	name = imm[1]
	if wave not in wavedata:
		path = imm[2]
		book = al_book(self, book)
		loop = al_loop(self, loop)
		wavedata[wave] = [size, book, loop, rate, path, name]
	return (name, int(round(12*math.log2(round(key/rate, 6)))))

def al_envelope(self, bankdata, env):
	self.c_addr = env
	if env not in bankdata[1]:
		envelope = []
		while True:
			envelope.append((ultra.sh(), ultra.sh()))
			if envelope[-1][0] in {-1, -2, -3}: break
		name = "env%d" % bankdata[0]
		bankdata[0] += 1
		bankdata[1][env] = (name, ", ".join("%d, %d" % x for x in envelope))

def al_note(x):
	return (
		"C", "Cs", "D", "Eb", "E",
		"F", "Fs", "G", "Ab", "A", "Bb", "B",
	)[(x+9) % 12] + "%d" % ((x+9) // 12)

def al_instrument(self, bankdata, wavedata, tbl, inst, i):
	if inst == 0: return
	self.c_push()
	self.c_addr = inst
	self.c_addr += 1
	min_ = ultra.ub()
	max_ = ultra.ub()
	rel = ultra.ub()
	env = ultra.uw()
	sound = [(ultra.uw(), ultra.f()) for i in range(3)]
	al_envelope(self, bankdata, env)
	if self.c_addr-self.addr in {0x57D350, 0x57D3C0}:
		al_envelope(self, bankdata, (self.c_addr+15) & ~15)
	sound = [
		al_sound(self, bankdata, wavedata, tbl, snd, key)
		for snd, key in sound
	]
	bankdata[2].append((
		"\tinstrument[%d] =\n"
		"\t{\n"
		"\t\trelease = %d;\n"
		"\t\tenvelope = %s;\n"
	) % (i, rel, bankdata[1][env][0]))
	if sound[0] != None: bankdata[2].append((
		"\t\tsoundL = {%s, %s, %s};\n"
	) % (al_note(min_), sound[0][0], al_note(39-sound[0][1])))
	bankdata[2].append((
		"\t\tsound = {%s, %s};\n"
	) % (               sound[1][0], al_note(39-sound[1][1])))
	if sound[2] != None: bankdata[2].append((
		"\t\tsoundH = {%s, %s, %s};\n"
	) % (al_note(max_), sound[2][0], al_note(39-sound[2][1])))
	bankdata[2].append("\t};\n")
	self.c_pull()

def al_percussion(self, bankdata, wavedata, tbl, perc, i):
	if perc == 0: return
	self.c_push()
	self.c_addr = perc
	rel = ultra.ub()
	pan = ultra.ub()
	self.c_addr += 2
	snd, key = ultra.uw(), ultra.f()
	env = ultra.uw()
	al_envelope(self, bankdata, env)
	snd, note = al_sound(self, bankdata, wavedata, tbl, snd, key)
	bankdata[2].append((
		"\tpercussion[%d] =\n"
		"\t{\n"
		"\t\trelease = %d;\n"
		"\t\tpan = %d;\n"
		"\t\tenvelope = %s;\n"
		"\t\tsound = {%s, %s};\n"
		"\t};\n"
	) % (i, rel, pan, bankdata[1][env][0], snd, al_note(39+note)))
	self.c_pull()

def s_audio_ctltbl(self, argv):
	ctl, tbl, data, ctlname, tblname = argv
	line = self.file[-1][1]
	wavetbl = {i: {} for i in tblname}
	banktbl = {}
	self.addr = 0-tbl
	ultra.asm.init(self, 0, data)
	self.c_addr += 2
	cnt = ultra.uh()
	for i in range(cnt):
		start = ultra.uw()
		self.c_addr += 4
		if i not in ctlname: continue
		banktbl[i] = [[0, {}, []], wavetbl[tbl+start], ctl, tbl+start]
	self.addr = 0-ctl
	ultra.asm.init(self, 0, self.c_data)
	self.c_addr += 2
	cnt = ultra.uh()
	for i in range(cnt):
		start = ultra.uw()
		self.c_addr += 4
		if i not in ctlname: continue
		self.c_push()
		self.c_addr = start
		icnt = ultra.uw()
		pcnt = ultra.uw()
		flag = ultra.uw()
		date = ultra.uw()
		banktbl[i][2] += self.c_addr
		banktbl[i] += [icnt, pcnt, flag, date]
		self.c_pull()
	for i in banktbl:
		bankdata, wavedata, ctl, tbl, icnt, pcnt, flag, date = banktbl[i]
		self.addr = 0-ctl
		ultra.asm.init(self, 0, self.c_data)
		imm = table.imm_addr(self, ctl)
		perc = ultra.uw()
		itbl = [ultra.uw() for i in range(icnt)]
		self.c_addr = perc
		ptbl = [ultra.uw() for i in range(pcnt)]
		for inst in sorted(itbl):
			i = itbl.index(inst)
			if i == imm:
				for perc in sorted(ptbl):
					p = ptbl.index(perc)
					al_percussion(self, bankdata, wavedata, tbl, perc, p)
			al_instrument(self, bankdata, wavedata, tbl, inst, i)
	for tbl in sorted(wavetbl.keys()):
		wavedata = wavetbl[tbl]
		line.append("wave %s\n{\n" % tblname[tbl])
		for wave in sorted(wavedata.keys()):
			size, book, loop, rate, path, name = wavedata[wave]
			wave = self.data[self.c_data][wave:wave+size]
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
	seq, bnk, data, path = argv
	line = self.file[-1][1]
	self.addr = 0-seq
	ultra.asm.init(self, 0, data)
	self.c_addr += 2
	cnt = ultra.uh()
	for i in range(cnt):
		start = ultra.uw()
		size  = ultra.uw()
		start = seq+start
		imm = table.imm_addr(self, start)
		if imm != None: size = imm
		data = self.data[self.c_data][start:start+size]
		fn = self.path_join(path[i])
		main.mkdir(fn)
		with open(fn, "wb") as f: f.write(data)
	self.addr = 0-bnk
	ultra.asm.init(self, 0, self.c_data)
	for i in range(cnt):
		start = ultra.uh()
		self.c_push()
		self.c_addr = start
		line.append("%s\n" % " ".join([
			"%d" % ultra.ub() for _ in range(ultra.ub())
		]))
		self.c_pull()
