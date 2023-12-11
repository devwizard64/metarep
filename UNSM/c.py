import struct
import json

import png

import main
import ultra
import UNSM

GLTF_BYTE   = 5120
GLTF_UBYTE  = 5121
GLTF_SHORT  = 5122
GLTF_USHORT = 5123
GLTF_INT    = 5124
GLTF_UINT   = 5125
GLTF_FLOAT  = 5126

def gltf_bufferView(gltf, buf, data):
	index = len(gltf["bufferViews"])
	gltf["bufferViews"].append({
		"buffer": 0,
		"byteLength": len(data),
		"byteOffset": gltf["buffers"][0]["byteLength"],
	})
	gltf["buffers"][0]["byteLength"] += len(data)
	buf.append(data)
	return index

def gltf_array(gltf, buf, data, t, n, normalized=False, box=False):
	accessor = {
		"bufferView": gltf_bufferView(gltf, buf, B"".join([
			struct.pack("<"+"bBhHiIf"[t-5120], x)
			for x in ([x for x in data for x in x] if n > 0 else data)
		])),
		"count": len(data),
		"componentType": t,
		"type": "VEC%d" % n if n > 0 else "SCALAR",
	}
	if normalized: accessor["normalized"] = True
	if box:
		accessor["min"] = [min([x[i] for x in data]) for i in range(n)]
		accessor["max"] = [max([x[i] for x in data]) for i in range(n)]
	index = len(gltf["accessors"])
	gltf["accessors"].append(accessor)
	return index

def gltf_primitive(gltf, buf, attrib, tri, mtl):
	primitive = {
		"attributes": {
			i: gltf_array(gltf, buf, data, t, n, normalized, box)
			for i, data, t, n, normalized, box in attrib
		},
		"indices": gltf_array(gltf, buf, tri, GLTF_USHORT, 0)
	}
	if mtl: primitive["material"] = gltf_mtltab[mtl]
	return primitive

def s_gltf(self, argv):
	global gltf_name
	global gltf_mtl
	global gltf_mtltab
	global gltf_mesh
	global gltf_meshinfo
	global gltf_meshdata
	gltf_name, gltf_mtl = argv
	gltf_mtltab = {mtl[0]: i for i, mtl in enumerate(gltf_mtl)}
	gltf_mesh = []
	gltf_meshinfo = {}
	gltf_meshdata = {}
	# print("\n%s_DEP := \\" % gltf_name.upper())

def s_gltf_mesh(self, argv):
	name, mesh = argv
	gltf_mesh.append((name, mesh))
	gltf_meshinfo[name] = mesh
	gltf_meshdata[name] = [False, [None]*len(mesh)]
	self.file[-1][1].append("#include \"%s.h\"\n" % self.path_rel([name]))
	# print("\t%s.h \\" % self.path_join([name], 1))
	# for light, mtl in mesh:
	# 	print("\t%s.h \\" % self.path_join(["%s.%s" % (name, mtl)], 1))

def s_gltf_write(self, argv):
	gltf = {
		"asset": {
			"generator": "metarep",
			"version": "2.0",
		},
		"scene": 0,
		"scenes": [],
		"nodes": [],
		"materials": [],
		"meshes": [],
		"textures": [],
		"images": [],
		"accessors": [],
		"bufferViews": [],
		"buffers": [{"byteLength": 0}],
	}
	buf = []
	for mtl in gltf_mtl:
		material = {"name": mtl[0]}
		if len(mtl) > 1:
			pbr = {}
			if mtl[1]:
				# mtl[1][0]
				pbr["baseColorFactor"] = [
					mtl[1][1+i]/255.0 for i in range(3)
				] + [1]
			if len(mtl) > 2:
				pbr["baseColorTexture"] = {"index": len(gltf["textures"])}
				gltf["textures"].append({"source": len(gltf["images"])})
				gltf["images"].append({"uri": mtl[2][0]})
				if len(mtl) > 3: material["extras"] = mtl[3]
			pbr["metallicFactor"] = 0
			material["pbrMetallicRoughness"] = pbr
		gltf["materials"].append(material)
	for i in ("materials", "textures", "images"):
		if not gltf[i]: gltf.pop(i)
	for i, mesh in enumerate(gltf_mesh):
		name, mesh = mesh
		flag, prim = gltf_meshdata[name]
		mesh = {"name": name, "primitives": [
			gltf_primitive(gltf, buf, attrib, tri, mtl)
			for attrib, tri, mtl in prim
		]}
		if flag: mesh["extras"] = {"r": 0, "g": 1, "b": 2}
		gltf["meshes"].append(mesh)
		gltf["nodes"].append({"name": name, "mesh": i})
	gltf["scenes"].append({
		"name": "Scene",
		"nodes": list(range(len(gltf["nodes"]))),
	})
	chunk = [
		[B"JSON", B" ", json.dumps(gltf, separators=(",", ":")).encode()],
		[B"BIN", B"\0", B"".join(buf)],
	]
	fn = self.path_join([gltf_name + ".glb"])
	main.mkdir(fn)
	with open(fn, "wb") as f:
		size = 12 + sum([8+((len(data)+3) & ~3) for code, pad, data in chunk])
		f.write(struct.pack("<4sII", B"glTF", 2, size))
		for code, pad, data in chunk:
			f.write(struct.pack("<I4s", (len(data)+3) & ~3, code))
			f.write(data)
			f.write(pad * (-len(data) & 3))

def gfx_prc(self, line, tab, end, name, index):
	light, mtl = gltf_meshinfo[name][index]
	txt = False
	normal = False
	color = False
	alpha = False
	if mtl:
		m = gltf_mtl[gltf_mtltab[mtl]]
		if len(m) > 2:
			txt = True
			w, h = m[2][1:]
			ss = st = 1
			ts = tt = -0.5
			if len(m) > 3:
				if "ss" in m[3]: ss = m[3]["ss"]
				if "st" in m[3]: st = m[3]["st"]
				if "ts" in m[3]: ts = m[3]["ts"]
				if "tt" in m[3]: tt = m[3]["tt"]
	vtx = []
	tri = []
	buf = 16*[None]
	start = self.addr
	while self.addr < end:
		w0 = self.u32()
		w1 = self.u32()
		cmd = w0 >> 24
		if cmd == 0x04:
			addr = self.addr
			self.addr = w1
			e = w1 + (w0 & 0xFFFF)
			i = w0 >> 16 & 0x0F
			while self.addr < e:
				imm = self.get_imm(self.addr)
				x = self.s16()
				y = self.s16()
				z = self.s16()
				self.addr += 2
				s = self.s16()
				t = self.s16()
				if light:
					nx = self.s8()
					ny = self.s8()
					nz = self.s8()
					r, g, b = imm if imm is not None else (0, 0, 0)
				else:
					nx, ny, nz = imm if imm is not None else (0, 0, 0)
					r = self.u8()
					g = self.u8()
					b = self.u8()
				a = self.u8()
				buf[i] = (x, y, z, s, t, nx, ny, nz, r, g, b, a)
				i += 1
			self.addr = addr
		elif cmd == 0xBF:
			t = (
				(w1 >> 16 & 0xFF) // 10,
				(w1 >>  8 & 0xFF) // 10,
				(w1       & 0xFF) // 10,
			)
			for v in t:
				if buf[v] in vtx:
					tri.append(vtx.index(buf[v]))
				else:
					tri.append(len(vtx))
					vtx.append(buf[v])
					if buf[v][5:8] != (0, 0, 0): normal = True
					if buf[v][8:10] != (0, 0, 0): color = True
					if buf[v][11] != 0: alpha = True
		else:
			self.addr -= 8
			break
	if start == self.addr: return 0
	attrib = [("POSITION", [v[0:3] for v in vtx], GLTF_FLOAT, 3, False, True)]
	if txt: attrib.append(("TEXCOORD_0", [(
		(v[3]*ss/32.0 - ts)/w,
		(v[4]*st/32.0 - tt)/h,
	) for v in vtx], GLTF_FLOAT, 2, False, False))
	if normal: attrib.append(("NORMAL", [
		(v[5]/128.0, v[6]/128.0, v[7]/128.0) for v in vtx
	], GLTF_FLOAT, 3, False, False))
	if color: attrib.append(("COLOR_0", [
		v[8:11+alpha] for v in vtx
	], GLTF_UBYTE, 3+alpha, True, False))
	elif alpha: attrib.append(("COLOR_0", [
		(0xFF, 0xFF, 0xFF, v[11]) for v in vtx
	], GLTF_UBYTE, 4, True, False))
	if not light and normal: gltf_meshdata[name][0] = True
	gltf_meshdata[name][1][index] = (attrib, tri, mtl)
	name = "%s.%s" % (name, mtl)
	line[-1][-1].append("#include \"%s.h\"" % self.path_rel([name]))
	return 1

def s_obj(self, argv):
	global obj_name
	global obj_vtx
	global obj_tri
	global obj_area
	obj_name, = argv
	obj_vtx = None
	obj_tri = []
	obj_area = None

def s_obj_write(self, argv):
	fn = self.path_join([obj_name + ".obj"])
	main.mkdir(fn)
	with open(fn, "w") as f:
		f.write("# metarep\n")
		for v in obj_vtx: f.write("v %d %d %d\n" % v)
		f.write("o %s\n" % obj_name)
		mtl = None
		for i, t in enumerate(obj_tri):
			m = t[0]
			if len(t) > 4: m += ",%d" % t[4]
			if obj_area: m += ";%d" % obj_area[i]
			if mtl != m:
				mtl = m
				f.write("usemtl %s\n" % mtl)
			f.write("f %d %d %d\n" % (1+t[1], 1+t[2], 1+t[3]))

# main.c
# graphics.c
# audio.c

# game.c

def d_staff_str_prc(self, argv):
	s = []
	n = 1
	while len(s) < n:
		x = self.u32()
		addr = self.addr
		self.addr = x
		x = "".join(self.asciz(4))
		self.addr = addr
		if n == 1: n = {
			"1": 2,
			"2": 3,
			"3": 4,
			"4": 4,
			"5": 5,
			"6": 5,
			"7": 6,
		}[x[0]]
		s.append(self.fmt_str(x))
	return ["{" + ", ".join(s) + "}"]
d_staff_str = [False, d_staff_str_prc]

def d_staff_prc(self, argv):
	stage   = self.u8()
	scene   = self.u8()
	flag    = self.u8()
	level = flag & 7
	pos = flag & 0x30
	off = flag & 0xC0
	angy    = self.u8()
	posx    = self.s16()
	posy    = self.s16()
	posz    = self.s16()
	self.addr += 2
	str_    = ultra.c.aw(self)
	stage = (UNSM.fmt.fmt_stage[stage]+",").ljust(14)
	flag = "%d" % level
	if str_ != "NULL":
		flag += "|STAFF_%s|0x%02X" % (("TL", "TR", "BL", "BR")[pos >> 4], off)
	flag = (flag+",").ljust(16)
	angy = "-0x%02X" % -angy if angy < 0 else " 0x%02X" % angy
	return ["{%s %d, %s %s, %5d, %5d, %5d, %s}" % (
		stage, scene, flag, angy, posx, posy, posz, str_
	)]
d_staff = [False, d_staff_prc]

# collision.c

def d_collision_prc(self, argv):
	flag     = self.u32() # T:flag(collision)
	callback = ultra.c.aw(self)
	return ["{0x%08X, %s}" % (flag, callback)]
d_collision = [False, d_collision_prc]

# player.c
# physics.c
# pldemo.c
# plhang.c
# plwait.c

# plmove.c

d_pl_move = [
	[0, -2, 1, ultra.c.d_s16],
	[0, -5, 1, ultra.c.d_u32, "0x%08X"],
]

# pljump.c
# plswim.c
# plhold.c
# callback.c
# memory.c
# save.c
# scene.c
# draw.c
# time.c
# slidec.c

# camera.c

def d_campos_prc(self, argv):
	code = self.s16()
	self.addr += 2
	x    = self.fmt_float(self.f())
	y    = self.fmt_float(self.f())
	z    = self.fmt_float(self.f())
	_10  = self.fmt_float(self.f())
	_14  = self.fmt_float(self.f())
	return ["{%d, {%s, %s, %s}, %s, %s}" % (code, x, y, z, _10, _14)]
d_campos = [False, d_campos_prc]

def d_camctl_prc(self, argv):
	_00 = self.s8()
	self.addr += 3
	callback = ultra.c.aw(self)
	x   = self.s16()
	y   = self.s16()
	z   = self.s16()
	w   = self.s16()
	h   = self.s16()
	d   = self.s16()
	ang = ultra.fmt_s16(self, self.s16())
	self.addr += 2
	arg = (_00, callback, x, y, z, w, h, d, ang)
	if arg == (0, "NULL", 0, 0, 0, 0, 0, 0, "0x0000"): return ["{0}"]
	return ["{%d, %s, {%d, %d, %d}, {%d, %d, %d}, %s}" % arg]
d_camctl = [False, d_camctl_prc]

def d_campath_prc(self, argv):
	flag    = self.s8()
	time    = self.u8()
	x       = self.s16()
	y       = self.s16()
	z       = self.s16()
	return ["{%2d, %3d, {%5d, %5d, %5d}}" % (flag, time, x, y, z)]
d_campath = [False, d_campath_prc]

def d_camdemo_prc(self, argv):
	callback = ultra.c.aw(self)
	time = self.s16()
	self.addr += 2
	time = ultra.fmt_s16(self, time) if time in {0x7FFF} else "%d" % time
	return ["{%s, %s}" % (callback, time)]
d_camdemo = [False, d_camdemo_prc]

# tmp
def d_camera_windemo_prc(self, argv):
	b0 = self.u8()
	b1 = self.u8()
	b2 = self.u8()
	b3 = self.u8()
	return ["CAM_WINDEMO(%d, %d, %d, %d, %d, %d, %d)" % (
		b0 & 0x0F, b0 >> 4,
		b1 & 0x0F, b1 >> 4,
		b2 & 0x0F, b2 >> 4,
		b3 & 0x0F,
	)]
d_camera_windemo = [False, d_camera_windemo_prc]

# tmp
def d_camera_pause_prc(self, argv):
	x = self.u8()
	return ["CAM_PAUSE(%s)" % ", ".join([
		"%d" % (x >> i & 1) for i in range(8)
	])]
d_camera_pause = [False, d_camera_pause_prc]

# course.c

# object.c

def d_pl_effect_prc(self, argv):
	code    = self.u32() # T:flag
	flag    = self.u32() # T:flag
	shape   = UNSM.fmt.fmt_shape(self, self.u8())
	self.addr += 3
	script  = ultra.c.aw(self, extern=True)
	if (code, flag, shape, script) == (0, 0, "S_NULL", "NULL"):
		return ["{0}"]
	return ["{0x%08X, 0x%08X, %s, %s}" % (code, flag, shape, script)]
d_pl_effect = [False, d_pl_effect_prc]

# objlib.c

def d_obj_splash_prc(self, argv):
	flag    = ultra.fmt_s16(self, self.s16())
	shape   = UNSM.fmt.fmt_shape(self, self.s16())
	script  = ultra.c.aw(self, extern=True)
	ay_mul  = self.s16()
	p_mul   = self.s16()
	vf_add  = self.fmt_float(self.f())
	vf_mul  = self.fmt_float(self.f())
	vy_add  = self.fmt_float(self.f())
	vy_mul  = self.fmt_float(self.f())
	s_add   = self.fmt_float(self.f())
	s_mul   = self.fmt_float(self.f())
	return [
		"%s, %s, %s," % (flag, shape, script),
		"/*ang y*/\t%d," % ay_mul,
		"/*pos  */\t%d," % p_mul,
		"/*vel f*/\t%s, %s," % (vf_add, vf_mul),
		"/*vel y*/\t%s, %s," % (vy_add, vy_mul),
		"/*scale*/\t%s, %s," % (s_add, s_mul),
	]
d_obj_splash = [False, d_obj_splash_prc]

def d_obj_effect_prc(self, argv):
	arg     = self.s8()
	count   = self.s8()
	shape   = UNSM.fmt.fmt_shape(self, self.u8())
	offset  = self.s8()
	vf_add  = self.s8()
	vf_mul  = self.s8()
	vy_add  = self.s8()
	vy_mul  = self.s8()
	gravity = self.s8()
	drag    = self.s8()
	self.addr += 2
	s_add   = self.fmt_float(self.f())
	s_mul   = self.fmt_float(self.f())
	return [
		"/*arg    */\t%d," % arg,
		"/*count  */\t%d," % count,
		"/*shape  */\t%s," % shape,
		"/*offset */\t%d," % offset,
		"/*vel f  */\t%d, %d," % (vf_add, vf_mul),
		"/*vel y  */\t%d, %d," % (vy_add, vy_mul),
		"/*gravity*/\t%d," % gravity,
		"/*drag   */\t%d," % drag,
		"/*scale  */\t%s, %s," % (s_add, s_mul),
	]
d_obj_effect = [False, d_obj_effect_prc]

def d_obj_hit_prc(self, argv):
	code    = self.u32() # T:flag
	offset  = self.u8()
	ap      = self.s8()
	hp      = self.s8()
	coin    = self.s8()
	hit_r   = self.s16()
	hit_h   = self.s16()
	dmg_r   = self.s16()
	dmg_h   = self.s16()
	return [
		"/*code   */\t0x%08X," % code,
		"/*offset */\t%d,"     % offset,
		"/*ap     */\t%d,"     % ap,
		"/*hp     */\t%d,"     % hp,
		"/*coin   */\t%d,"     % coin,
		"/*hit r,h*/\t%d, %d," % (hit_r, hit_h),
		"/*dmg r,h*/\t%d, %d," % (dmg_r, dmg_h),
	]
d_obj_hit = [False, d_obj_hit_prc]

# object_a.c

def d_object_a_0_prc(self, argv):
	_00 = ultra.fmt_s16(self, self.s16())
	self.addr += 2
	_04 = self.fmt_float(self.f())
	_08 = self.fmt_float(self.f())
	return ["{%s, %s, %s}" % (_00, _04, _08)]
d_object_a_0 = [False, d_object_a_0_prc]

def d_object_a_1_prc(self, argv):
	flag    = self.s16()
	scale   = self.s16()
	map_    = ultra.c.aw(self, extern=True)
	dist    = self.s16()
	self.addr += 2
	return ["{%d, %d, %s, %d}" % (flag, scale, map_, dist)]
d_object_a_1 = [False, d_object_a_1_prc]

def d_80330260_prc(self, argv):
	a = self.s32()
	b = self.s32()
	a = ("%d" if a == -1 else "0x%08X") % a
	return ["{%s, %d}" % (a, b)]
d_80330260 = [False, d_80330260_prc]

def d_object_a_2_prc(self, argv):
	count   = self.s16()
	add     = self.s16()
	mul     = self.s16()
	shape   = UNSM.fmt.fmt_shape(self, self.s16())
	map_    = ultra.c.aw(self, extern=True)
	return ["{%d, %d, %d, %s, %s}" % (count, add, mul, shape, map_)]
d_object_a_2 = [False, d_object_a_2_prc]

def d_object_a_3_prc(self, argv):
	map_    = ultra.c.aw(self, extern=True)
	posx    = self.s16()
	posz    = self.s16()
	angy    = ultra.fmt_s16(self, self.s16())
	self.addr += 2
	return ["{%s, %d, %d, %s}" % (map_, posx, posz, angy)]
d_object_a_3 = [False, d_object_a_3_prc]

def d_object_a_4_prc(self, argv):
	offset  = self.s32()
	scalex  = self.fmt_float(self.f())
	scaley  = self.fmt_float(self.f())
	scalez  = self.fmt_float(self.f())
	vel     = self.fmt_float(self.f())
	return ["{%d, {%s, %s, %s}, %s}" % (offset, scalex, scaley, scalez, vel)]
d_object_a_4 = [False, d_object_a_4_prc]

def d_object_a_5_prc(self, argv):
	shape   = UNSM.fmt.fmt_shape(self, self.u8())
	posx    = self.s8()
	posz    = self.s8()
	state   = self.s8()
	data    = ultra.c.aw(self)
	return ["{%s, %d, %d, %d, %s}" % (shape, posx, posz, state, data)]
d_object_a_5 = [False, d_object_a_5_prc]

def d_object_a_6_prc(self, argv):
	index   = self.u8()
	flag    = self.u8()
	arg     = self.u8()
	shape   = UNSM.fmt.fmt_shape(self, self.u8())
	script  = ultra.c.aw(self, extern=True)
	return ["{%d, %d, %d, %s, %s}" % (index, flag, arg, shape, script)]
d_object_a_6 = [False, d_object_a_6_prc]

def d_object_a_7_prc(self, argv):
	offset  = self.s16()
	shape   = UNSM.fmt.fmt_shape(self, self.s16())
	map_    = ultra.c.aw(self, extern=True)
	return ["{%d, %s, %s}" % (offset, shape, map_)]
d_object_a_7 = [False, d_object_a_7_prc]

def d_object_a_8_prc(self, argv):
	time        = self.s32()
	anime       = self.s32() # T:enum(anime)
	vel         = self.fmt_float(self.f())
	anime_vel   = self.fmt_float(self.f())
	return ["{%d, %d, %s, %s}" % (time, anime, vel, anime_vel)]
d_object_a_8 = [False, d_object_a_8_prc]

# ride.c
# hitcheck.c
# objlist.c

# objsound.c

def d_stepsound_prc(self, argv):
	flag    = self.s16()
	l       = self.s8()
	r       = self.s8()
	se      = UNSM.fmt.fmt_na_se(self, self.u32())
	if (flag, l, r, se) == (0, 0, 0, 0): return ["{0}"]
	return ["{%d, %d, %d, %s}" % (flag, l, r, se)]
d_stepsound = [False, d_stepsound_prc]

# debug.c
# wipe.c

# shadow.c

def d_shadow_rect_prc(self, argv):
	sizex = self.fmt_float(self.f())
	sizez = self.fmt_float(self.f())
	flag = ultra.fmt_bool[self.s8()]
	self.addr += 3
	return ["{%s, %s, %s}" % (sizex, sizez, flag)]
d_shadow_rect = [False, d_shadow_rect_prc]

# back.c

# water.c

def d_water_prc(self, argv):
	index   = self.s32()
	texture = self.s32()
	len_    = self.s32()
	data    = ultra.c.aw(self, extern=True)
	start   = ultra.c.aw(self, extern=True)
	end     = ultra.c.aw(self, extern=True)
	draw    = ultra.c.aw(self, extern=True)
	r       = self.u8()
	g       = self.u8()
	b       = self.u8()
	a       = self.u8()
	layer   = self.s32()
	arg0    = (index, texture, len_, data)
	arg1    = (start, end, draw)
	arg2    = (r, g, b, a, UNSM.fmt.fmt_layer(self, layer))
	if arg0+arg1+arg2 == (
		0, 0, 0, "NULL",
		"NULL", "NULL", "NULL",
		0, 0, 0, 0, "LAYER_BACK"
	):
		return ["{0}"]
	return [
		"{",
			"\t0x%04X, %d, %2d, %s," % arg0,
			"\t%s, %s, %s," % arg1,
			"\t0x%02X, 0x%02X, 0x%02X, 0x%02X, %s," % arg2,
		"}",
	]
d_water = [False, d_water_prc]

# objshape.c

# wave.c

def d_wave_shape_prc(self, argv):
	n = self.s16()
	lst = ["%d," % n]
	for _ in range(n):
		x = self.s16()
		y = self.s16()
		z = self.s16()
		lst.append("%d, %d, %d," % (x, y, z))
	return lst
d_wave_shape = [False, d_wave_shape_prc]

def d_wave_shade_prc(self, argv):
	end, = argv
	lst = []
	while self.addr < end:
		n = self.s16()
		f = [n] + [self.s16() for _ in range(n)]
		lst.append(" ".join(["%d," % x for x in f]))
	return lst
d_wave_shade = [False, d_wave_shade_prc]

# dprint.c
# message.c
# weather.c
# lava.c

# tag.c

def d_tag_obj_prc(self, argv):
	start, = argv
	i       = (self.save-start) // 8
	script  = ultra.c.aw(self, extern=True)
	shape   = UNSM.fmt.fmt_shape(self, self.s16())
	code    = self.s16()
	if i != 0 and (script, shape, code) == ("o_coin", "S_COIN", 0):
		return ["/*%3d*/\tTAGOBJ_NULL" % i]
	return ["/*%3d*/\t{%s, %s, %d}" % (i, script, shape, code)]
d_tag_obj = [False, d_tag_obj_prc]

map_obj_ext = {}

def d_map_obj_prc(self, argv):
	index  = self.u8()
	ext    = self.u8()
	arg    = self.u8()
	shape  = UNSM.fmt.fmt_shape(self, self.u8())
	script = ultra.c.aw(self, extern=True)
	map_obj_ext[index] = ext
	index = UNSM.fmt.fmt_map_obj(index)
	ext   = "MAP_EXT_" + (
		"NULL",
		"ANG",
		"ANG_CODE",
		"XYZ",
		"ANG_ARG",
	)[ext]
	return ["{%s, %s, %d, %s, %s}" % (index, ext, arg, shape, script)]
d_map_obj = [False, d_map_obj_prc]

def d_tag_prc(self, argv):
	lst = []
	while True:
		x = self.u16()
		o = (x & 0x1FF) - 31
		angy = x >> 9
		if o == -1:
			lst.append("TAG_END,")
			break
		elif o < 0:
			lst.append("%d," % x)
			break
		else:
			posx = self.s16()
			posy = self.s16()
			posz = self.s16()
			code = self.s16()
			lst.append("TAG(%s, %d, %d, %d, %d, %d)," % (
				UNSM.fmt.fmt_tag_x[o], angy, posx, posy, posz, code,
			))
	self.addr = (self.addr+3) & ~3
	return lst
d_tag = [False, d_tag_prc]

# hud.c

def d_meter_prc(self, argv):
	mode    = self.s8()
	self.addr += 1
	x       = self.s16()
	y       = self.s16()
	self.addr += 2
	scale   = self.fmt_float(self.f())
	return ["{%d, %d, %d, %s}" % (mode, x, y, scale)]
d_meter = [False, d_meter_prc]

# object_b.c

# object_c.c

def d_object_c_0_prc(self, argv):
	msg_start   = UNSM.fmt.fmt_msg(self, self.s16())
	msg_win     = UNSM.fmt.fmt_msg(self, self.s16())
	path        = ultra.c.aw(self, extern=True)
	star_x      = self.s16()
	star_y      = self.s16()
	star_z      = self.s16()
	self.addr += 2
	return ["{%s, %s, %s, {%d, %d, %d}}" % (
		msg_start, msg_win, path, star_x, star_y, star_z
	)]
d_object_c_0 = [False, d_object_c_0_prc]

def d_object_c_1_prc(self, argv):
	scale   = self.fmt_float(self.f())
	se      = UNSM.fmt.fmt_na_se(self, self.u32())
	dist    = self.s16()
	damage  = self.s8()
	self.addr += 1
	return ["{%s, %s, %d, %d}" % (scale, se, dist, damage)]
d_object_c_1 = [False, d_object_c_1_prc]

def d_object_c_2_prc(self, argv):
	map_    = ultra.c.aw(self, extern=True)
	p_map   = ultra.c.aw(self, extern=True)
	p_shape = UNSM.fmt.fmt_shape(self, self.s16())
	self.addr += 2
	return ["{%s, %s, %s}" % (map_, p_map, p_shape)]
d_object_c_2 = [False, d_object_c_2_prc]

def d_80332AC0_prc(self, argv):
	a = self.s16()
	b = self.s16()
	return ["{%d, %d}" % (a, b)]
d_80332AC0 = [False, d_80332AC0_prc]

def d_object_c_3_prc(self, argv):
	map_    = ultra.c.aw(self, extern=True)
	shape   = UNSM.fmt.fmt_shape(self, self.s16())
	self.addr += 2
	return ["{%s, %s}" % (map_, shape)]
d_object_c_3 = [False, d_object_c_3_prc]

def d_object_c_4_prc(self, argv):
	msg     = self.s16()
	self.addr += 2
	radius  = self.fmt_float(self.f())
	height  = self.fmt_float(self.f())
	return ["{%d, %s, %s}" % (msg, radius, height)]
d_object_c_4 = [False, d_object_c_4_prc]

def d_object_c_5_prc(self, argv):
	shape   = UNSM.fmt.fmt_shape(self, self.s32())
	script  = ultra.c.aw(self, extern=True)
	scale   = self.fmt_float(self.f())
	return ["{%s, %s, %s}" % (shape, script, scale)]
d_object_c_5 = [False, d_object_c_5_prc]

# math.c

def d_bspline_prc(self, argv):
	time = self.s16()
	x    = self.s16()
	y    = self.s16()
	z    = self.s16()
	return ["{%2d, {%5d, %5d, %5d}}" % (time, x, y, z)]
d_bspline = [False, d_bspline_prc]

# shape.c

def d_anime_prc(self, line, tab, argv):
	anime, = argv
	shared = self.addr == anime
	self.addr = anime
	flag    = UNSM.fmt.fmt_anime_flag(self, self.s16())
	waist   = self.s16()
	start   = self.s16()
	loop    = self.s16()
	frame   = self.s16()
	joint   = self.s16()
	val     = self.u32()
	tbl     = self.u32()
	size    = self.u32()
	sym_anime = self.get_sym(anime)
	if shared:
		sym_val = self.get_sym(val)
		sym_tbl = self.get_sym(tbl)
	else:
		self.save = self.addr
		self.addr = tbl
		tbl_data = [(self.u16(), self.u16()) for _ in range(3*(1+joint))]
		self.addr = val
		val_data = [self.s16() for _ in range(max([f+i for f, i in tbl_data]))]
		sym_val = main.sym_var(sym_anime.label+"_val", "static short", "[]")
		sym_tbl = main.sym_var(sym_anime.label+"_tbl", "static u16", "[]")
		line.append((val, sym_val, set(), [
			" ".join([
				# "-0x%04X," % -x if x < 0 else " 0x%04X," % x
				"%6d," % x
				for x in val_data[i:i+8]
			])
			for i in range(0, len(val_data), 8)
		]))
		line.append((tbl, sym_tbl, set(), [
			" ".join([
				"%5d, %5d," % x
				for x in tbl_data[i:i+3]
			])
			for i in range(0, len(tbl_data), 3)
		]))
		self.addr = self.save
	line.append((anime, sym_anime, set(), [
		"/*flag */\t%s," % flag,
		"/*waist*/\t%d," % waist,
		"/*start*/\t%d," % start,
		"/*loop */\t%d," % loop,
		"/*frame*/\t%d," % frame,
		"/*joint*/\t%d," % joint,
		"%s," % sym_val.label,
		"%s," % sym_tbl.label,
		("0x%X," if size > 0 else "%d,") % size,
	]))
d_anime = [True, d_anime_prc]

# shplang.c
# prglang.c

# bgcheck.c

d_bgface = [
	[0, -1, 2, ultra.c.d_s16],
	[0, -2, 1, ultra.c.d_s8],
	[0, -1, 2, ultra.c.d_s16],
	[1, -3, 3, ultra.c.d_s16],
	[0, -1, 4, ultra.c.d_f32],
	[0, -1, 1, ultra.c.d_addr, 0],
]

# bgload.c

def d_map_prc(self, argv):
	global obj_vtx
	global obj_tri
	name, = argv
	lst = []
	while True:
		x = self.s16()
		if x == 64:
			obj_vtx = [
				(self.s16(), self.s16(), self.s16())
				for _ in range(self.s16())
			]
		elif x == 65:
			lst.append("#include \"%s.h\"" % self.path_rel([name]))
		elif x == 66:
			lst.append("MAP_END,")
			break
		elif x == 67:
			n = self.s16()
			lst.append("MAP_OBJECT, %d," % n)
			for _ in range(n):
				o = self.s16()
				n = (3, 4, 5, 6, 4)[map_obj_ext[o]]
				o = UNSM.fmt.fmt_map_obj(o)
				lst.append(" ".join(
					[o + ","] + ["%d," % self.s16() for _ in range(n)]
				))
		elif x == 68:
			n = self.s16()
			lst.append("MAP_WATER, %d," % n)
			for _ in range(n):
				lst.append(" ".join(["%d," % self.s16() for _ in range(6)]))
		else:
			n = 4 if x in {4, 14, 36, 37, 39, 44, 45} else 3
			x = "%d" % x # T:enum(bg)
			obj_tri.extend([
				[x] + [self.s16() for _ in range(n)]
				for _ in range(self.s16())
			])
	self.addr = (self.addr+3) & ~3
	return lst
d_map = [False, d_map_prc]

def d_area_prc(self, argv):
	global obj_area
	name, n = argv
	obj_area = [self.s8() for _ in range(n)]
	self.addr = (self.addr+3) & ~3
	return ["#include \"%s.h\"" % self.path_rel([name])]
d_area = [False, d_area_prc]

# objlang.c

# audio/g.c

def d_Na_bgmctl_prc(self, argv):
	n, = argv
	lst = ["%s," % UNSM.fmt.fmt_na_bgm[self.s16()]]
	n -= 1
	while n > 0:
		x = self.s16()
		n -= 1
		c = ["(s16)(%d" % (x & 0xFF)]
		v = []
		bit = 1 << 15
		for ctl in (
			"GE_X",
			"GE_Y",
			"GE_Z",
			"LT_X",
			"LT_Y",
			"LT_Z",
			"SCENE",
			"AREA",
		):
			if x & bit:
				c.append(" | BGMCTL(%s)" % ctl)
				v.append(" %d," % self.s16())
				n -= 1
			bit >>= 1
		lst.append("".join(c) + ")," + "".join(v))
	self.addr = (self.addr+3) & ~3
	return lst
d_Na_bgmctl = [False, d_Na_bgmctl_prc]

def d_Na_bgmctl_data_prc(self, argv):
	a_voice = self.u16()
	a_vol   = self.u16()
	a_time  = self.s16()
	b_voice = self.u16()
	b_vol   = self.u16()
	b_time  = self.s16()
	return ["{(s16)0x%04X, 0x%02X, %3d, (s16)0x%04X, 0x%02X, %3d}" % (
		a_voice, a_vol, a_time,
		b_voice, b_vol, b_time,
	)]
d_Na_bgmctl_data = [False, d_Na_bgmctl_data_prc]

# audio/data.c

def d_Na_cfg_prc(self, argv):
	freq    = self.u32()
	voice   = self.u8()
	e_filt  = self.u8()
	e_size  = self.u16()
	e_vol   = self.u16()
	vol     = self.u16()
	_0C     = self.u32()
	_10     = self.u32()
	_14     = self.u32()
	_18     = self.u32()
	arg = (freq, voice, e_filt, e_size, e_vol, vol, _0C, _10, _14, _18)
	if arg == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0):
		return ["{0}"]
	return [(
		"{%5d, %2d, %d, 0x%04X, 0x%04X, 0x%04X, "
		"0x%04X, 0x%04X, 0x%04X, 0x%04X}"
	) % arg]
d_Na_cfg = [False, d_Na_cfg_prc]

# ?

def d_path_data_prc(self, argv):
	lst = []
	while True:
		x = self.s16()
		if x < 0:
			lst.append("%d," % x)
			break
		else:
			lst.append("%d, %d, %d, %d," % (
				x, self.s16(), self.s16(), self.s16(),
			))
	self.addr = (self.addr+3) & ~3
	return lst
d_path_data = [False, d_path_data_prc]

# face

def d_face_srt_prc(self, argv):
	sx = self.fmt_float(self.f())
	sy = self.fmt_float(self.f())
	sz = self.fmt_float(self.f())
	rx = self.fmt_float(self.f())
	ry = self.fmt_float(self.f())
	rz = self.fmt_float(self.f())
	tx = self.fmt_float(self.f())
	ty = self.fmt_float(self.f())
	tz = self.fmt_float(self.f())
	return ["{{%s, %s, %s}, {%s, %s, %s}, {%s, %s, %s}}" % (
		sx, sy, sz, rx, ry, rz, tx, ty, tz,
	)]
d_face_srt = [False, d_face_srt_prc]

def d_face_dyndata_prc(self, argv):
	count = self.s32()
	type_ = self.s32()
	data = ultra.c.aw(self)
	return ["{%d, %d, %s}" % (count, type_, data)]
d_face_dyndata = [False, d_face_dyndata_prc]

dyn_cmd = {
	0xD1D4: "dStart",
	0: "dSetNamesType",
	1: "dSetInitPos",
	2: "dSetRelPos",
	3: "dSetWorldPos",
	4: "dSetNormal",
	5: "dSetScale",
	6: "dSetRotation",
	7: "dSetObjFlags",
	8: "dSetFlags",
	9: "dClrFlags",
	10: "dSetFriction",
	11: "dSetSpring",
	12: "dCall",
	13: "dSetColNum",
	15: "dMakeObj",
	16: "dStartGroup",
	17: "dEndGroup",
	18: "dAddToGroup",
	19: "dSetType",
	20: "dSetMatGroup",
	21: "dSetNodeGroup",
	22: "dSetSkinShape",
	23: "dSetPlaneGroup",
	24: "dSetShapePtrPtr",
	25: "dSetShapePtr",
	26: "dSetShapeOffset",
	27: "dSetCofG",
	28: "dLinkWith",
	29: "dLinkWithPtr",
	30: "dUseObj",
	31: "dSetControlType",
	32: "dSetSkinWeight",
	33: "dSetAmbient",
	34: "dSetDiffuse",
	35: "dSetID",
	36: "dSetMaterial",
	37: "dMapMaterials",
	38: "dMapVertices",
	39: "dAttach",
	40: "dAttachTo",
	41: "dSetAttOffset",
	43: "dSetSuffix",
	44: "dSetParmf",
	45: "dSetParmp",
	46: "dStartChain",
	47: "dAddLink",
	48: "dEndChain",
	49: "dMakeVertex",
	50: "dAddValPtr",
	52: "dUseTexture",
	53: "dSetTextureST",
	54: "dMakeNetFromShape",
	55: "dMakeNetFromShapePtrPtr",
	58: "dEnd",
}

def dyn_fmt_name(self, p, flag):
	if flag: return "%d" % p
	if p >= 0x8016F000: return ultra.fmt_addr(self, p)
	if p == 0: return "NULL"
	self.save = self.addr
	self.addr = p
	x = "".join(self.asciz(4))
	self.addr = self.save
	return self.fmt_str(x)

def dyn_null(self, argv, c, p, i, x, y, z):
	return "%s()" % dyn_cmd[c]

def dyn_p(self, argv, c, p, i, x, y, z):
	s = ultra.sym(self, p, self.save, "(void *)0x%08X")
	sym = self.find_sym(p, self.save)
	if sym is not None:
		s = sym.label
		if not sym.lst: s = "&" + s
	else:
		s = "(void *)0x%08X" % p
	return "%s(%s)" % (dyn_cmd[c], s)

def dyn_name(self, argv, c, p, i, x, y, z):
	flag, = argv
	return "%s(%s)" % (dyn_cmd[c], dyn_fmt_name(self, p, flag))

def dyn_pi(self, argv, c, p, i, x, y, z):
	return "%s(%s, %d)" % (dyn_cmd[c], ultra.fmt_addr(self, p), i)

def dyn_i(self, argv, c, p, i, x, y, z):
	return "%s(%d)" % (dyn_cmd[c], i)

def dyn_ip(self, argv, c, p, i, x, y, z):
	return "%s(%d, %s)" % (dyn_cmd[c], i, ultra.fmt_addr(self, p))

def dyn_ix(self, argv, c, p, i, x, y, z):
	return "%s(%d, %s)" % (dyn_cmd[c], i, x)

def dyn_x(self, argv, c, p, i, x, y, z):
	return "%s(%s)" % (dyn_cmd[c], x)

def dyn_xy(self, argv, c, p, i, x, y, z):
	return "%s(%s, %s)" % (dyn_cmd[c], x, y)

def dyn_xyz(self, argv, c, p, i, x, y, z):
	return "%s(%s, %s, %s)" % (dyn_cmd[c], x, y, z)

def dyn_iname(self, argv, c, p, i, x, y, z):
	flag, = argv
	return "%s(%d, %s)" % (dyn_cmd[c], i, dyn_fmt_name(self, p, flag))

def dyn_setparmp(self, argv, c, p, i, x, y, z):
	if p < 0x04000000: return "dSetParmi(%d, %d)" % (i, p)
	return "dSetParmp(%d, %s)" % (i, ultra.fmt_addr(self, p))

def dyn_addvalptr(self, argv, c, p, i, x, y, z):
	flag, = argv
	return "%s(%s, %s, %d, %s)" % (
		dyn_cmd[c], dyn_fmt_name(self, p, flag), y, i, x
	)

def d_face_dynlist_prc(self, argv):
	c = self.s32()
	p = self.u32()
	i = self.s32()
	x = self.fmt_float(self.f())
	y = self.fmt_float(self.f())
	z = self.fmt_float(self.f())
	return [{
		0xD1D4: dyn_null,
		0: dyn_i,
		1: dyn_xyz,
		2: dyn_xyz,
		3: dyn_xyz,
		4: dyn_xyz,
		5: dyn_xyz,
		6: dyn_xyz,
		7: dyn_i,
		8: dyn_i,
		9: dyn_i,
		10: dyn_xyz,
		11: dyn_x,
		12: dyn_p,
		13: dyn_i,
		15: dyn_iname,
		16: dyn_name,
		17: dyn_name,
		18: dyn_name,
		19: dyn_i,
		20: dyn_name,
		21: dyn_name,
		22: dyn_name,
		23: dyn_name,
		24: dyn_p,
		25: dyn_name,
		26: dyn_xyz,
		27: dyn_xyz,
		28: dyn_name,
		29: dyn_p,
		30: dyn_name,
		31: dyn_i,
		32: dyn_ix,
		33: dyn_xyz,
		34: dyn_xyz,
		35: dyn_i,
		36: dyn_pi,
		37: dyn_name,
		38: dyn_name,
		39: dyn_name,
		40: dyn_iname,
		41: dyn_xyz,
		43: dyn_name,
		44: dyn_ix,
		45: dyn_setparmp,
		46: dyn_name,
		47: dyn_name,
		48: dyn_name,
		49: dyn_xyz,
		50: dyn_addvalptr,
		52: dyn_i,
		53: dyn_xy,
		54: dyn_name,
		55: dyn_p,
		58: dyn_null,
	}[c](self, argv, c, p, i, x, y, z)]
d_face_dynlist = [False, d_face_dynlist_prc]

def d_face_bank_prc(self, argv):
	index = self.s32()
	dynlist = ultra.c.aw(self, extern=True)
	return ["{%d, %s}" % (index, dynlist)]
d_face_bank = [False, d_face_bank_prc]

# ========

def d_rendermode_prc(self, argv):
	return [{
		0x00442078: "G_RM_AA_ZB_OPA_SURF",
		0x00112078: "G_RM_AA_ZB_OPA_SURF2",
		0x004049D8: "G_RM_AA_ZB_XLU_SURF",
		0x001049D8: "G_RM_AA_ZB_XLU_SURF2",
		0x00442D58: "G_RM_AA_ZB_OPA_DECAL",
		0x00112D58: "G_RM_AA_ZB_OPA_DECAL2",
		0x00404DD8: "G_RM_AA_ZB_XLU_DECAL",
		0x00104DD8: "G_RM_AA_ZB_XLU_DECAL2",
		0x00442478: "G_RM_AA_ZB_OPA_INTER",
		0x00112478: "G_RM_AA_ZB_OPA_INTER2",
		0x004045D8: "G_RM_AA_ZB_XLU_INTER",
		0x001045D8: "G_RM_AA_ZB_XLU_INTER2",
		0x00443078: "G_RM_AA_ZB_TEX_EDGE",
		0x00113078: "G_RM_AA_ZB_TEX_EDGE2",
		0x00442048: "G_RM_AA_OPA_SURF",
		0x00112048: "G_RM_AA_OPA_SURF2",
		0x004041C8: "G_RM_AA_XLU_SURF",
		0x001041C8: "G_RM_AA_XLU_SURF2",
		0x00443048: "G_RM_AA_TEX_EDGE",
		0x00113048: "G_RM_AA_TEX_EDGE2",
		0x00442230: "G_RM_ZB_OPA_SURF",
		0x00112230: "G_RM_ZB_OPA_SURF2",
		0x0C084000: "G_RM_OPA_SURF",
		0x03024000: "G_RM_OPA_SURF2",
	}[self.u32()]]
d_rendermode = [False, d_rendermode_prc]

def d_light_prc(self, argv):
	a, = argv
	a = self.fmt_float(a)
	self.addr += 8
	r = self.u8()
	g = self.u8()
	b = self.u8()
	self.addr += 13
	return ["gdSPDefLight(%s, 0x%02X, 0x%02X, 0x%02X)" % (a, r, g, b)]
d_light = [False, d_light_prc]

def d_Mtx_prc(self, argv):
	h = [self.s16() for i in range(16)]
	l = [self.u16() for i in range(16)]
	return ["gdSPDefMatrix("] + ["\t" + " ".join([
		self.fmt_float(
			float(h[i] << 16 | l[i]) / 0x10000, "", len(argv) == 0
		) + ("," if i != 15 else "") for i in range(i, i+4)
	]) for i in range(0, 16, 4)] + [")"]
d_Mtx = [False, d_Mtx_prc]

texture_cvt_rgba16 = [False, True, 1, lambda self: self.u16(), lambda x: (
	(x >> 11       ) * 0xFF//0x1F,
	(x >>  6 & 0x1F) * 0xFF//0x1F,
	(x >>  1 & 0x1F) * 0xFF//0x1F,
	(x       & 0x01) * 0xFF,
)]
texture_cvt_ia4 = [True, True, 2, lambda self: self.u8(), lambda x: (
	(x >> 5       ) * 0xFF//0x07,
	(x >> 4 & 0x01) * 0xFF,
	(x >> 1 & 0x07) * 0xFF//0x07,
	(x      & 0x01) * 0xFF,
)]
texture_cvt_ia8 = [True, True, 1, lambda self: self.u8(), lambda x: (
	(x >> 4       ) * 0x11,
	(x      & 0x0F) * 0x11,
)]
texture_cvt_ia16 = [True, True, 1, lambda self: self.u16(), lambda x: (
	(x >> 8       ),
	(x      & 0xFF),
)]

def d_texture_prc(self, argv):
	fmt, w, h, name = argv
	g, a, n, f, c = {
		"rgba16":   texture_cvt_rgba16,
		"ia4":      texture_cvt_ia4,
		"ia8":      texture_cvt_ia8,
		"ia16":     texture_cvt_ia16,
	}[fmt]
	data = [
		[x for x in [c(f(self)) for _ in range(w//n)] for x in x]
		for _ in range(h)
	]
	writer = png.Writer(w, h, greyscale=g, alpha=a)
	fn = "%s.%s.png" % (self.path_join([name]), fmt)
	main.mkdir(fn)
	with open(fn, "wb") as f: writer.write(f, data)
	return ["#include \"%s.%s.h\"" % (self.path_rel([name]), fmt)]
d_texture = [False, d_texture_prc]

def d_gfx_prc(self, line, tab, argv):
	end = argv[0]
	lst = argv[1:]
	i = 0
	name = None
	while self.addr < end:
		ultra.c.lst_push(self, line)
		if type(lst[i]) == str:
			name = lst[i]
			i += 1
		i += gfx_prc(self, line, tab, end, name, lst[i])
		ultra.c.lst_push(self, line)
		start = self.addr
		while self.addr < end:
			w0 = self.u32()
			w1 = self.u32()
			cmd = w0 >> 24
			if cmd == 0x04:
				self.addr -= 8
				break
		if start != self.addr:
			argv = [self.addr]
			self.addr = self.save
			ultra.c.d_Gfx_prc(self, line, tab, argv)
d_gfx = [True, d_gfx_prc]

def g_movemem(self, argv):
	a_0  = self.u32()
	a_1  = self.u32()
	d0_0 = self.u32()
	d0_1 = self.u32()
	if a_0 == 0x03860010 and d0_0 == 0x03880010 and a_1-d0_1 == 8:
		imm = self.get_imm(self.save)
		if imm is not None:
			light = ultra.fmt_addr(self, d0_1, array=(imm, 0x18))
		else:
			light = ultra.fmt_addr(self, d0_1)
		return ("SPSetLights1N", light)
	return None

def g_tri1(self, argv):
	w0_0 = self.u32()
	w1_0 = self.u32()
	w0_1 = self.u32()
	w1_1 = self.u32()
	if w0_0 == 0xBF000000 and w0_1 == 0xBF000000:
		v00 = "%2d" % ((w1_0 >> 16 & 0xFF) // 10)
		v01 = "%2d" % ((w1_0 >>  8 & 0xFF) // 10)
		v02 = "%2d" % ((w1_0 >>  0 & 0xFF) // 10)
		flag0 = "%d" % (w1_0 >> 24)
		v10 = "%2d" % ((w1_1 >> 16 & 0xFF) // 10)
		v11 = "%2d" % ((w1_1 >>  8 & 0xFF) // 10)
		v12 = "%2d" % ((w1_1 >>  0 & 0xFF) // 10)
		flag1 = "%d" % (w1_1 >> 24)
		return ("SP2Triangles", v00, v01, v02, flag0, v10, v11, v12, flag1)
	return None

def g_texture(self, argv):
	w0 = self.u32()
	w1 = self.u32()
	s = (w1 >> 16) // 62
	t = (w1 & 0xFFFF) // 62
	for x in (s, t):
		if x == 0 or (x & ~(1 << x.bit_length()-1)) != 0: return None
	s = "62*%d" % s
	t = "62*%d" % t
	return ultra.c.g_texture_prc(s, t, w0)

def g_loadimageblock(self, cmd, timg, fmt, siz, width, w):
	tile, uls, ult, lrs, dxt = ultra.c.gx_tile(w[0], w[1])
	if (width, tile, uls, ult) != (1, 7, 0, 0): return None
	width  = max(16 >> siz, (0x800 << siz) // dxt)
	height = (lrs+1) // width
	ultra.c.timgproc(self, timg)
	timg   = ultra.sym(self, timg, self.save)
	fmt    = ultra.c.g_im_fmt[fmt]
	siz    = ultra.c.g_im_siz(siz)
	width  = "%d" % width
	height = "%d" % height
	return (cmd, timg, fmt, siz, width, height)

def g_settimg(self, argv):
	w = []
	if ultra.c.g_words(self, w, 3):
		fmt, siz, width, timg = ultra.c.gx_settimg(w[0][0], w[0][1])
		if tuple([x[0] >> 24 for x in w]) == (0xFD, 0xE6, 0xF3):
			return g_loadimageblock(
				self, "DPLoadImageBlock", timg, fmt, siz, width, w[2]
			)
		if ultra.c.g_words(self, w, 2):
			c = tuple([x[0] >> 24 for x in w])
			if tuple([x[0] >> 24 for x in w]) == (0xFD, 0xE8, 0xF5, 0xE6, 0xF3):
				if ultra.c.gx_settile(w[2][0], w[2][1]) == (
					fmt, siz, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0
				):
					return g_loadimageblock(
						self, "DPLoadImageBlockT", timg, fmt, siz, width, w[4]
					)
	return None

def g_rdptilesync(self, argv):
	w = []
	if ultra.c.g_words(self, w, 3):
		if tuple([x[0] >> 24 for x in w]) == (0xE8, 0xF5, 0xF2):
			fmt, siz, line, tmem, c1_tile, pal, cmt, maskt, shiftt, cms, \
				masks, shifts = ultra.c.gx_settile(w[1][0], w[1][1])
			c2_tile, uls, ult, lrs, lrt = ultra.c.gx_tile(w[2][0], w[2][1])
			width  = (lrs >> 2) + 1
			height = (lrt >> 2) + 1
			if (line, tmem, c1_tile, c2_tile, uls, ult, lrs, lrt) == (
				ultra.c.g_calc_line(width, siz), 0, 0,
				0, 0, 0, (width-1) << 2, (height-1) << 2
			):
				fmt     = ultra.c.g_im_fmt[fmt]
				siz     = ultra.c.g_im_siz(siz)
				width   = "%d" % width
				height  = "%d" % height
				pal     = "%d" % pal
				cms     = ultra.c.g_tx_cm(cms)
				cmt     = ultra.c.g_tx_cm(cmt)
				masks   = ultra.c.g_tx_mask(masks)
				maskt   = ultra.c.g_tx_mask(maskt)
				shifts  = "%d" % shifts
				shiftt  = "%d" % shiftt
				return ("DPSetImageBlock",
					fmt, siz, width, height, pal,
					cms, cmt, masks, maskt, shifts, shiftt
				)
	return None

g_cc_env        = ("0", "0", "0", "ENVIRONMENT")
g_cc_t0_en      = ("TEXEL0", "0", "ENVIRONMENT", "0")
g_cc_sh_en      = ("SHADE", "0", "ENVIRONMENT", "0")

g_setcombine_mode = {
	ultra.c.g_cc_shade      + g_cc_env:     "G_CC_SHADE_ENV",
	ultra.c.g_cc_texel0     + g_cc_env:     "G_CC_DECALRGB_ENV",
	ultra.c.g_cc_texel0     + g_cc_t0_en:   "G_CC_DECALRGBA_ENV",
	ultra.c.g_cc_t0_sh_t0a  + g_cc_env:     "G_CC_BLENDRGB_ENVA",
	ultra.c.g_cc_t0_sh      + g_cc_env:     "G_CC_MODULATERGB_ENVA",
	ultra.c.g_cc_t0_sh      + g_cc_t0_en:   "G_CC_MODULATERGBA_ENVA",
	g_cc_t0_en  + g_cc_t0_en:   "G_CC_MODULATERGBA_ENV",
	g_cc_sh_en  + g_cc_sh_en:   "G_CC_MODULATESE",
}

def g_setcombine(self, argv):
	x = ultra.c.g_setcombine_prc(self, g_setcombine_mode)
	if len(x) == 3: return x
	return None

def g_settile(self, argv):
	w = []
	if ultra.c.g_words(self, w, 5):
		c = tuple([x[0] >> 24 for x in w])
		c0_fmt, c0_siz, c0_line, c0_tmem, c0_tile, c0_palette, c0_cmt, \
			c0_maskt, c0_shiftt, c0_cms, c0_masks, c0_shifts = \
			ultra.c.gx_settile(w[0][0], w[0][1])
		if c == (0xF5, 0xE6, 0xF3, 0xF5, 0xF2):
			c2_tile, c2_uls, c2_ult, c2_lrs, c2_dxt = \
				ultra.c.gx_tile(w[2][0], w[2][1])
			c3_fmt, c3_siz, c3_line, c3_tmem, c3_tile, c3_palette, c3_cmt, \
				c3_maskt, c3_shiftt, c3_cms, c3_masks, c3_shifts = \
				ultra.c.gx_settile(w[3][0], w[3][1])
			c4_t, c4_uls, c4_ult, c4_lrs, c4_lrt = \
				ultra.c.gx_tile(w[4][0], w[4][1])
			fmt     = c3_fmt
			siz     = c3_siz
			width   = (c4_lrs >> 2) + 1
			height  = (c4_lrt >> 2) + 1
			pal     = c3_palette
			cms     = c3_cms
			cmt     = c3_cmt
			masks   = c3_masks
			maskt   = c3_maskt
			shifts  = c3_shifts
			shiftt  = c3_shiftt
			if (
				c0_fmt, c0_siz, c0_line, c0_tmem, c0_tile, c0_palette,
				c0_cmt, c0_maskt, c0_shiftt, c0_cms, c0_masks, c0_shifts,
				c2_tile, c2_uls, c2_ult, c2_lrs, c2_dxt,
				c3_fmt, c3_siz, c3_line, c3_tmem, c3_tile, c3_palette,
				c3_cmt, c3_maskt, c3_shiftt, c3_cms, c3_masks, c3_shifts,
				c4_t, c4_uls, c4_ult, c4_lrs, c4_lrt,
			) == (
				fmt, (2,2,2,3)[siz], 0, 0, 7, 0,
				cmt, maskt, shiftt, cms, masks, shifts,
				7, 0, 0, ultra.c.g_calc_lrs(width, height, siz),
				ultra.c.g_calc_dxt(width, siz),
				fmt, siz, ultra.c.g_calc_line(width, siz), 0, 0, pal,
				cmt, maskt, shiftt, cms, masks, shifts,
				0, 0, 0, (width-1) << 2, (height-1) << 2,
			):
				fmt     = ultra.c.g_im_fmt[fmt]
				width   = "%d" % width
				height  = "%d" % height
				pal     = "%d" % pal
				cms     = ultra.c.g_tx_cm(cms)
				cmt     = ultra.c.g_tx_cm(cmt)
				masks   = ultra.c.g_tx_mask(masks)
				maskt   = ultra.c.g_tx_mask(maskt)
				shifts  = "%d" % shifts
				shiftt  = "%d" % shiftt
				arg = (
					width, height, pal,
					cms, cmt,
					masks, maskt, shifts, shiftt,
				)
				if siz == 0: return ("DPLoadTextureBlock_4bN", fmt) + arg
				siz = ultra.c.g_im_siz(siz)
				return ("DPLoadTextureBlockN", fmt, siz) + arg
	self.addr = self.save
	w0 = self.u32()
	w1 = self.u32()
	fmt, siz, line, tmem, tile, palette, cmt, maskt, shiftt, cms, masks, \
		shifts = ultra.c.gx_settile(w0, w1)
	if (line, tmem, tile, palette, cmt, maskt, shiftt, cms, masks, shifts) == \
		(0, 0, 7, 0, 0, 0, 0, 0, 0, 0):
		fmt = ultra.c.g_im_fmt[fmt]
		siz = ultra.c.g_im_siz(siz)
		return ("DPSetLoadTile", fmt, siz)
	return None

gfx_table = {
	0x03: (g_movemem,),
	0xBF: (g_tri1,),
	0xBB: (g_texture,),
	0xFD: (g_settimg,),
	0xFC: (g_setcombine,),
	0xF5: (g_settile,),
	0xE8: (g_rdptilesync,),
}

def s_message_str(self, lang, line):
	lst = []
	while True:
		x = self.u8()
		if x == 0xFF: break
		lst.append(x)
	i = 0
	while i < len(lst):
		for s, c in lang:
			n = len(c)
			if lst[i:i+n] == c:
				line.append(s)
				i += n
				break
		else:
			raise RuntimeError("illegal character 0x%02X" % lst[i])
	if not line[-1].endswith("\n"): line.append("\n")
	self.addr = (self.addr+3) & ~3

def s_message(self, argv):
	seg, start, end, cmd, path, name, lang = argv[:7]
	ultra.init(self, seg, start)
	line = ["$name: %s\n$lang: %s\n\n" % (name, lang)]
	lang = UNSM.tools.lang.table[lang]
	count = 0
	while self.addr < end:
		x = self.u32()
		if x == 0: break
		addr = self.addr
		self.addr = x
		arg = []
		if cmd == "msg":
			arg = self.s32()
			ln  = self.s8()
			self.addr += 1
			x   = self.s16()
			y   = self.s16()
			self.addr += 2
			self.addr = self.u32()
			arg = ["%d, %d, %d, %d" % (arg, ln, x, y)]
		if len(argv) > 7: line.append("$$ %s\n" % self.fmt(argv[7], count))
		line.append("$%s:" % cmd)
		if arg: line.append(" " + "; ".join(arg))
		line.append("\n")
		s_message_str(self, lang, line)
		line.append("\n")
		self.addr = addr
		count += 1
	data = "".join(line).rstrip("\n") + "\n"
	fn = self.path_join([path + ".txt"])
	main.mkdir(fn)
	with open(fn, "w") as f: f.write(data)
	self.file[-1][1].append("#include \"%s.h\"\n" % self.path_rel([path]))

def s_back(self, argv):
	seg, start = argv
	ultra.c.init(self, seg, start)
	self.file[-1][1].append("\nBACK %s =\n{{\n%s}};\n" % (
		self.meta.sym[seg][start].label, "".join([
			"\t%s\n" % " ".join([
				self.meta.sym[seg][self.u32()].label + ","
				for _ in range(10)
			])
			for _ in range(8)
		])
	))

# 00 02
def shp_call(self, argv):
	arg = self.u8()
	self.addr += 2
	script = ultra.c.aw(self)
	if arg == 1:
		return ("Call", script)
	return (None, script)

# 01 03 04 05 0B 17
def shp_null(self, argv):
	self.addr += 3
	return (None,)

# 08
def shp_scene(self, argv):
	self.addr += 1
	n = "%d" % self.s16()
	x = "%d" % self.s16()
	y = "%d" % self.s16()
	w = "%d" % self.s16()
	h = "%d" % self.s16()
	return (None, x, y, w, h, n)

# 09 20
def shp_arg(self, argv):
	self.addr += 1
	arg = "%d" % self.s16()
	return (None, arg)

# 0A
def shp_persp(self, argv):
	c    = self.u8()
	fovy = "%d" % self.s16()
	n    = "%d" % self.s16()
	f    = "%d" % self.s16()
	if c:
		callback = ultra.c.aw(self)
		return ("Perspective", fovy, n, f, callback)
	return (None, fovy, n, f)

# 0C
def shp_layer(self, argv):
	depth = ultra.fmt_bool[self.u8()]
	self.addr += 2
	return (None, depth)

# 0D
def shp_lod(self, argv):
	self.addr += 3
	min_ = "%d" % self.s16()
	max_ = "%d" % self.s16()
	return (None, min_, max_)

# 0E 18
def shp_callback(self, argv):
	self.addr += 1
	arg = self.s16()
	callback = ultra.c.aw(self)
	# s_stage_weather
	# s_face_proc
	# s_objlib_8029D924
	# s_wave_802D5B98
	if callback == "s_stage_weather":
		arg = "WEATHER_" + {
			0: "NULL",
			1: "SNOW",
			2: "BUBBLE",
			12: "LAVA",
			13: "WHIRLPOOL",
			14: "JET",
		}[arg]
	elif callback in {
		"s_water_802D104C",
		"s_water_802D1B70",
		"s_water_802D1CDC",
		"s_water_802D1E48",
		"s_water_802D1FA8",
		"s_water_802D2108",
	}:
		arg = "0x%04X" % arg
	else:
		arg = "%d" % arg # T:enum(*)
	return (None, arg, callback)

# 0F
def shp_camera(self, argv):
	self.addr += 1
	arg     = "%d" % self.s16() # T:enum(camera)
	eye_x   = "%d" % self.s16()
	eye_y   = "%d" % self.s16()
	eye_z   = "%d" % self.s16()
	look_x  = "%d" % self.s16()
	look_y  = "%d" % self.s16()
	look_z  = "%d" % self.s16()
	callback = ultra.c.aw(self)
	return (None, arg, eye_x, eye_y, eye_z, look_x, look_y, look_z, callback)

# 10
def shp_gfx_coord(self, argv):
	arg = self.u8()
	x = arg >> 4 & 7
	if x == 0:
		self.addr += 2
		posx = "%d" % self.s16()
		posy = "%d" % self.s16()
		posz = "%d" % self.s16()
		angx = "%d" % self.s16()
		angy = "%d" % self.s16()
		angz = "%d" % self.s16()
		s = "Coord"
		a = (posx, posy, posz, angx, angy, angz)
	if x == 1:
		posx = "%d" % self.s16()
		posy = "%d" % self.s16()
		posz = "%d" % self.s16()
		s = "CoordPos"
		a = (posx, posy, posz)
	if x == 2:
		angx = "%d" % self.s16()
		angy = "%d" % self.s16()
		angz = "%d" % self.s16()
		s = "CoordAng"
		a = (angx, angy, angz)
	if x == 3:
		angy = "%d" % self.s16()
		s = "CoordAngY"
		a = (angy,)
	if arg & 0x80:
		layer = UNSM.fmt.fmt_layer(self, arg & 15)
		gfx = ultra.c.aw(self)
		return ("Gfx"+s, layer, gfx) + a
	return (s,) + a

# 11 12 14 1D
def shp_gfx_arg(self, argv):
	c, m = argv
	arg = self.u8()
	if m == 0:
		x = "%d" % self.s16()
		y = "%d" % self.s16()
		z = "%d" % self.s16()
		a = (x, y, z)
	else:
		self.addr += 2
		s = self.fmt_float(main.round_cvt(
			lambda x: float(x)/0x10000,
			lambda x: int(0x10000*x),
			self.s32()
		))
		a = (s,)
	if arg & 0x80:
		layer = UNSM.fmt.fmt_layer(self, arg & 15)
		gfx = ultra.c.aw(self)
		return (c, layer, gfx) + a
	return (None,) + a

# 13
def shp_gfx_pos(self, argv):
	layer = UNSM.fmt.fmt_layer(self, self.u8())
	x = "%d" % self.s16()
	y = "%d" % self.s16()
	z = "%d" % self.s16()
	gfx = ultra.c.aw(self)
	return (None, layer, gfx, x, y, z)

# 15
def shp_gfx(self, argv):
	layer = UNSM.fmt.fmt_layer(self, self.u8())
	self.addr += 2
	gfx = ultra.c.aw(self)
	return (None, layer, gfx)

# 16
def shp_shadow(self, argv):
	self.addr += 1
	type_ = "SHADOW_" + {
		0: "CIRCLE9",
		1: "CIRCLE4",
		10: "SQUAREFIX",
		11: "SQUARE",
		12: "SQUARECUT",
		50: "50",
		51: "51",
		99: "MARIO",
	}[self.s16()]
	alpha = "%d" % self.s16()
	size  = "%d" % self.s16()
	return (None, size, alpha, type_)

# 19
def shp_back(self, argv):
	self.addr += 1
	arg = self.s16()
	callback = ultra.c.aw(self)
	if callback == "NULL":
		r = (arg >> 11 & 0x1F) * 0xFF//0x1F
		g = (arg >>  6 & 0x1F) * 0xFF//0x1F
		b = (arg >>  1 & 0x1F) * 0xFF//0x1F
		a = arg & 1
		arg = "GPACK_RGBA5551(0x%02X, 0x%02X, 0x%02X, %d)" % (r, g, b, a)
	else:
		arg = "BACK_" + "ADEFBGHICJ"[arg]
	return (None, arg, callback)

# 1C
def shp_hand(self, argv):
	arg = "%d" % self.u8()
	x = "%d" % self.s16()
	y = "%d" % self.s16()
	z = "%d" % self.s16()
	callback = ultra.c.aw(self)
	return (None, x, y, z, arg, callback)

shp_str = (
	"Execute", # 0x00
	"Exit", # 0x01
	"Jump", # 0x02
	"Return", # 0x03
	"Start", # 0x04
	"End", # 0x05
	"Store", # 0x06
	"Flag", # 0x07
	"Scene", # 0x08
	"Ortho", # 0x09
	"Persp", # 0x0A
	"Empty", # 0x0B
	"Layer", # 0x0C
	"LOD", # 0x0D
	"Select", # 0x0E
	"Camera", # 0x0F
	"Coord", # 0x10
	"Pos", # 0x11
	"Ang", # 0x12
	"Joint", # 0x13
	"Billboard", # 0x14
	"Gfx", # 0x15
	"Shadow", # 0x16
	"Object", # 0x17
	"Callback", # 0x18
	"Background", # 0x19
	None, # 0x1A
	"Load", # 0x1B
	"Hand", # 0x1C
	"Scale", # 0x1D
	None, # 0x1E
	None, # 0x1F
	"Cull", # 0x20
)

shp_fnc = (
	(shp_call,), # 0x00
	(shp_null,), # 0x01
	(shp_call,), # 0x02
	(shp_null,), # 0x03
	(shp_null,), # 0x04
	(shp_null,), # 0x05
	None, # 0x06
	None, # 0x07
	(shp_scene,), # 0x08
	(shp_arg,), # 0x09
	(shp_persp,), # 0x0A
	(shp_null,), # 0x0B
	(shp_layer,), # 0x0C
	(shp_lod,), # 0x0D
	(shp_callback,), # 0x0E
	(shp_camera,), # 0x0F
	(shp_gfx_coord,), # 0x10
	(shp_gfx_arg, "GfxPos", 0), # 0x11
	(shp_gfx_arg, "GfxAng", 0), # 0x12
	(shp_gfx_pos,), # 0x13
	(shp_gfx_arg, "GfxBillboard", 0), # 0x14
	(shp_gfx,), # 0x15
	(shp_shadow,), # 0x16
	(shp_null,), # 0x17
	(shp_callback,), # 0x18
	(shp_back,), # 0x19
	None, # 0x1A
	None, # 0x1B
	(shp_hand,), # 0x1C
	(shp_gfx_arg, "GfxScale", 1), # 0x1D
	None, # 0x1E
	None, # 0x1F
	(shp_arg,), # 0x20
)

def d_s_script_prc(self, line, tab, argv):
	end, = argv
	t = 0
	while self.addr < end:
		if ultra.c.lst_push(self, line): t = 0
		c = self.u8()
		f = shp_fnc[c]
		argv = f[0](self, f[1:])
		s = argv[0] if argv[0] is not None else shp_str[c]
		if self.seg == "E0.TTM.data" and self.save == 0x0E00093C: c = 0x05
		if c in {0x05} and t > 0: t -= 1
		if c in {0x01}: t = 0
		line[-1][-1].append(
			tab + "\t"*t + "s" + s + "(" + ", ".join(argv[1:]) + "),"
		)
		if c in {0x04}: t += 1
d_s_script = [True, d_s_script_prc]
