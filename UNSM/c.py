import struct
import json

import png

import main
import table
import ultra
import UNSM
import UNSM.table

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
	fn = ultra.script.path_join([gltf_name + ".glb"])
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
	start = self.c_addr
	while self.c_addr < end:
		w0 = ultra.uw()
		w1 = ultra.uw()
		cmd = w0 >> 24
		if cmd == 0x04:
			addr = self.c_addr
			self.c_addr = w1
			e = w1 + (w0 & 0xFFFF)
			i = w0 >> 16 & 0x0F
			while self.c_addr < e:
				imm = table.imm_addr(self, self.c_addr)
				x = ultra.sh()
				y = ultra.sh()
				z = ultra.sh()
				self.c_addr += 2
				s = ultra.sh()
				t = ultra.sh()
				if light:
					nx = ultra.sb()
					ny = ultra.sb()
					nz = ultra.sb()
					r, g, b = imm if imm is not None else (0, 0, 0)
				else:
					nx, ny, nz = imm if imm is not None else (0, 0, 0)
					r = ultra.ub()
					g = ultra.ub()
					b = ultra.ub()
				a = ultra.ub()
				buf[i] = (x, y, z, s, t, nx, ny, nz, r, g, b, a)
				i += 1
			self.c_addr = addr
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
			self.c_addr -= 8
			break
	if start == self.c_addr: return 0
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
	fn = ultra.script.path_join([obj_name + ".obj"])
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

# todo: macro
def d_staff_prc(argv):
	stage   = UNSM.table.fmt_stage(ultra.ub())
	scene   = ultra.ub()
	flag    = ultra.ub()
	ang     = ultra.ub()
	x       = ultra.sh()
	y       = ultra.sh()
	z       = ultra.sh()
	ultra.script.c_addr += 2
	str_    = ultra.c.aw()
	return ["{%s, %d, 0x%02X, 0x%02X, {%d, %d, %d}, %s}" % (
		stage, scene, flag, ang, x, y, z, str_
	)]
d_staff = [False, d_staff_prc]

# collision.c

def d_collision_prc(argv):
	flag     = ultra.uw() # T:flag(collision)
	callback = ultra.c.aw()
	return ["{0x%08X, %s}" % (flag, callback)]
d_collision = [False, d_collision_prc]

# player.c
# plphysics.c
# pldemo.c
# plhang.c
# plwait.c

# plwalk.c

d_pl_walk = [
	[0, -2, 1, ultra.c.d_s16],
	[0, -5, 1, ultra.c.d_u32, "0x%08X"],
]

# pljump.c
# plswim.c
# plgrab.c
# plcallback.c
# memory.c
# save.c
# scene.c
# draw.c
# time.c
# slidec.c

# camera.c

def d_campos_prc(argv):
	code = ultra.sh()
	ultra.script.c_addr += 2
	x    = ultra.fmt_float(ultra.f())
	y    = ultra.fmt_float(ultra.f())
	z    = ultra.fmt_float(ultra.f())
	_10  = ultra.fmt_float(ultra.f())
	_14  = ultra.fmt_float(ultra.f())
	return ["{%d, {%s, %s, %s}, %s, %s}" % (code, x, y, z, _10, _14)]
d_campos = [False, d_campos_prc]

def d_camctl_prc(argv):
	_00 = ultra.sb()
	ultra.script.c_addr += 3
	callback = ultra.c.aw()
	x   = ultra.sh()
	y   = ultra.sh()
	z   = ultra.sh()
	w   = ultra.sh()
	h   = ultra.sh()
	d   = ultra.sh()
	ang = ultra.fmt_s16(ultra.sh())
	ultra.script.c_addr += 2
	arg = (_00, callback, x, y, z, w, h, d, ang)
	if arg == (0, "NULL", 0, 0, 0, 0, 0, 0, "0x0000"):
		return ["{0}"]
	return ["{%d, %s, {%d, %d, %d}, {%d, %d, %d}, %s}" % arg]
d_camctl = [False, d_camctl_prc]

def d_campath_prc(argv):
	flag    = ultra.sb()
	time    = ultra.ub()
	x       = ultra.sh()
	y       = ultra.sh()
	z       = ultra.sh()
	return ["{%2d, %3d, {%5d, %5d, %5d}}" % (flag, time, x, y, z)]
d_campath = [False, d_campath_prc]

def d_camdemo_prc(argv):
	callback = ultra.c.aw()
	time = ultra.sh()
	ultra.script.c_addr += 2
	time = ultra.fmt_s16(time) if time in {0x7FFF} else "%d" % time
	return ["{%s, %s}" % (callback, time)]
d_camdemo = [False, d_camdemo_prc]

# tmp
def d_camera_windemo_prc(argv):
	b0 = ultra.ub()
	b1 = ultra.ub()
	b2 = ultra.ub()
	b3 = ultra.ub()
	return ["CAM_WINDEMO(%d, %d, %d, %d, %d, %d, %d)" % (
		b0 & 0x0F, b0 >> 4,
		b1 & 0x0F, b1 >> 4,
		b2 & 0x0F, b2 >> 4,
		b3 & 0x0F,
	)]
d_camera_windemo = [False, d_camera_windemo_prc]

# tmp
def d_camera_pause_prc(argv):
	x = ultra.ub()
	return ["CAM_PAUSE(%s)" % ", ".join([
		"%d" % (x >> i & 1) for i in range(8)
	])]
d_camera_pause = [False, d_camera_pause_prc]

# course.c

# object.c

def d_pl_pcl_prc(argv):
	code    = ultra.uw() # T:flag
	flag    = ultra.uw() # T:flag
	shape   = UNSM.table.fmt_shape(ultra.ub())
	ultra.script.c_addr += 3
	script  = ultra.aw(extern=True)
	if (code, flag, shape, script) == (0, 0, "S_NULL", "NULL"):
		return ["{0}"]
	return ["{0x%08X, 0x%08X, %s, %s}" % (code, flag, shape, script)]
d_pl_pcl = [False, d_pl_pcl_prc]

# objlib.c

def d_obj_splash_prc(argv):
	flag    = ultra.fmt_s16(ultra.sh())
	shape   = UNSM.table.fmt_shape(ultra.sh())
	script  = ultra.c.aw(True)
	ay_mul  = ultra.sh()
	p_mul   = ultra.sh()
	vf_add  = ultra.fmt_float(ultra.f())
	vf_mul  = ultra.fmt_float(ultra.f())
	vy_add  = ultra.fmt_float(ultra.f())
	vy_mul  = ultra.fmt_float(ultra.f())
	s_add   = ultra.fmt_float(ultra.f())
	s_mul   = ultra.fmt_float(ultra.f())
	return [
		"%s, %s, %s," % (flag, shape, script),
		"/* ang y    */  %d," % ay_mul,
		"/* pos      */  %d," % p_mul,
		"/* vel f    */  %s, %s," % (vf_add, vf_mul),
		"/* vel y    */  %s, %s," % (vy_add, vy_mul),
		"/* scale    */  %s, %s," % (s_add, s_mul),
	]
d_obj_splash = [False, d_obj_splash_prc]

def d_obj_pcl_prc(argv):
	arg     = ultra.sb()
	count   = ultra.sb()
	shape   = UNSM.table.fmt_shape(ultra.ub())
	offset  = ultra.sb()
	vf_add  = ultra.sb()
	vf_mul  = ultra.sb()
	vy_add  = ultra.sb()
	vy_mul  = ultra.sb()
	gravity = ultra.sb()
	drag    = ultra.sb()
	ultra.script.c_addr += 2
	s_add   = ultra.fmt_float(ultra.f())
	s_mul   = ultra.fmt_float(ultra.f())
	return [
		"/* arg      */  %d," % arg,
		"/* count    */  %d," % count,
		"/* shape    */  %s," % shape,
		"/* offset   */  %d," % offset,
		"/* vel f    */  %d, %d," % (vf_add, vf_mul),
		"/* vel y    */  %d, %d," % (vy_add, vy_mul),
		"/* gravity  */  %d," % gravity,
		"/* drag     */  %d," % drag,
		"/* scale    */  %s, %s," % (s_add, s_mul),
	]
d_obj_pcl = [False, d_obj_pcl_prc]

def d_obj_col_prc(argv):
	type_   = ultra.uw() # T:flag
	offset  = ultra.ub()
	ap      = ultra.sb()
	hp      = ultra.sb()
	coin    = ultra.sb()
	hit_r   = ultra.sh()
	hit_h   = ultra.sh()
	dmg_r   = ultra.sh()
	dmg_h   = ultra.sh()
	return [
		"/* type     */  0x%08X," % type_,
		"/* offset   */  %d,"     % offset,
		"/* ap       */  %d,"     % ap,
		"/* hp       */  %d,"     % hp,
		"/* coin     */  %d,"     % coin,
		"/* hit r, h */  %d, %d," % (hit_r, hit_h),
		"/* dmg r, h */  %d, %d," % (dmg_r, dmg_h),
	]
d_obj_col = [False, d_obj_col_prc]

# object_a.c

def d_object_a_0_prc(argv):
	_00 = ultra.fmt_s16(ultra.sh())
	ultra.script.c_addr += 2
	_04 = ultra.fmt_float(ultra.f())
	_08 = ultra.fmt_float(ultra.f())
	return ["{%s, %s, %s}" % (_00, _04, _08)]
d_object_a_0 = [False, d_object_a_0_prc]

def d_object_a_1_prc(argv):
	flag    = ultra.sh()
	scale   = ultra.sh()
	map_    = ultra.c.aw(True)
	dist    = ultra.sh()
	ultra.script.c_addr += 2
	return ["{%d, %d, %s, %d}" % (flag, scale, map_, dist)]
d_object_a_1 = [False, d_object_a_1_prc]

def d_80330260_prc(argv):
	a = ultra.sw()
	b = ultra.sw()
	a = ("%d" if a == -1 else "0x%08X") % a
	return ["{%s, %d}" % (a, b)]
d_80330260 = [False, d_80330260_prc]

def d_object_a_2_prc(argv):
	count   = ultra.sh()
	add     = ultra.sh()
	mul     = ultra.sh()
	shape   = UNSM.table.fmt_shape(ultra.sh())
	map_    = ultra.c.aw(True)
	return ["{%d, %d, %d, %s, %s}" % (count, add, mul, shape, map_)]
d_object_a_2 = [False, d_object_a_2_prc]

def d_object_a_3_prc(argv):
	map_    = ultra.c.aw(True)
	px      = ultra.sh()
	pz      = ultra.sh()
	ay      = ultra.fmt_s16(ultra.sh())
	ultra.script.c_addr += 2
	return ["{%s, %d, %d, %s}" % (map_, px, pz, ay)]
d_object_a_3 = [False, d_object_a_3_prc]

def d_object_a_4_prc(argv):
	offset  = ultra.sw()
	sx      = ultra.fmt_float(ultra.f())
	sy      = ultra.fmt_float(ultra.f())
	sz      = ultra.fmt_float(ultra.f())
	vel     = ultra.fmt_float(ultra.f())
	return ["{%d, {%s, %s, %s}, %s}" % (offset, sx, sy, sz, vel)]
d_object_a_4 = [False, d_object_a_4_prc]

def d_object_a_5_prc(argv):
	shape   = UNSM.table.fmt_shape(ultra.ub())
	px      = ultra.sb()
	pz      = ultra.sb()
	state   = ultra.sb()
	data    = ultra.c.aw()
	return ["{%s, %d, %d, %d, %s}" % (shape, px, pz, state, data)]
d_object_a_5 = [False, d_object_a_5_prc]

def d_object_a_6_prc(argv):
	index   = ultra.ub()
	flag    = ultra.ub()
	arg     = ultra.ub()
	shape   = UNSM.table.fmt_shape(ultra.ub())
	script  = ultra.c.aw(True)
	return ["{%d, %d, %d, %s, %s}" % (index, flag, arg, shape, script)]
d_object_a_6 = [False, d_object_a_6_prc]

def d_object_a_7_prc(argv):
	offset  = ultra.sh()
	shape   = UNSM.table.fmt_shape(ultra.sh())
	map_    = ultra.c.aw(True)
	return ["{%d, %s, %s}" % (offset, shape, map_)]
d_object_a_7 = [False, d_object_a_7_prc]

def d_object_a_8_prc(argv):
	time        = ultra.sw()
	anime       = ultra.sw() # T:enum(anime)
	vel         = ultra.fmt_float(ultra.f())
	anime_vel   = ultra.fmt_float(ultra.f())
	return ["{%d, %d, %s, %s}" % (time, anime, vel, anime_vel)]
d_object_a_8 = [False, d_object_a_8_prc]

# objphysics.c
# objcollision.c
# objlist.c

# objsfx.c

def d_obj_sfx_prc(argv):
	flag    = ultra.sh()
	l       = ultra.sb()
	r       = ultra.sb()
	se      = UNSM.table.fmt_na_se(ultra.uw())
	if (flag, l, r, se) == (0, 0, 0, 0):
		return ["{0}"]
	return ["{%d, %d, %d, %s}" % (flag, l, r, se)]
d_obj_sfx = [False, d_obj_sfx_prc]

# objdebug.c
# wipe.c

# shadow.c

def d_shadow_rect_prc(argv):
	sx = ultra.fmt_float(ultra.f())
	sz = ultra.fmt_float(ultra.f())
	y_scale = ultra.fmt_bool[ultra.sb()]
	ultra.script.c_addr += 3
	return ["{%s, %s, %s}" % (sx, sz, y_scale)]
d_shadow_rect = [False, d_shadow_rect_prc]

# back.c

# scroll.c

def d_scroll_prc(argv):
	index   = ultra.sw()
	texture = ultra.sw()
	len_    = ultra.sw()
	data    = ultra.c.aw(True)
	start   = ultra.c.aw(True)
	end     = ultra.c.aw(True)
	draw    = ultra.c.aw(True)
	r       = ultra.ub()
	g       = ultra.ub()
	b       = ultra.ub()
	a       = ultra.ub()
	layer   = ultra.sw()
	arg0    = (index, texture, len_, data)
	arg1    = (start, end, draw)
	arg2    = (r, g, b, a, UNSM.table.fmt_layer(layer))
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
d_scroll = [False, d_scroll_prc]

# objshape.c

# wave.c

def d_wave_shape_prc(argv):
	n = ultra.sh()
	lst = ["%d," % n]
	for _ in range(n):
		x = ultra.sh()
		y = ultra.sh()
		z = ultra.sh()
		lst.append("%d, %d, %d," % (x, y, z))
	return lst
d_wave_shape = [False, d_wave_shape_prc]

def d_wave_shade_prc(argv):
	end, = argv
	lst = []
	while ultra.script.c_addr < end:
		n = ultra.sh()
		f = [n] + [ultra.sh() for _ in range(n)]
		lst.append(" ".join(["%d," % x for x in f]))
	return lst
d_wave_shade = [False, d_wave_shade_prc]

# dprint.c
# message.c
# snow.c
# lava.c

# tag.c

def d_tag_obj_prc(argv):
	start, = argv
	i       = (ultra.script.c_dst-start) // 8
	script  = ultra.aw(extern=True)
	shape   = UNSM.table.fmt_shape(ultra.sh())
	arg     = ultra.sh()
	return ["/* %3d */   {%s, %s, %d}" % (i, script, shape, arg)]
d_tag_obj = [False, d_tag_obj_prc]

map_obj_ext = {}

def d_map_obj_prc(argv):
	index  = ultra.ub()
	ext    = ultra.ub()
	code   = ultra.ub()
	shape  = UNSM.table.fmt_shape(ultra.ub())
	script = ultra.aw(extern=True)
	map_obj_ext[index] = ext
	index = UNSM.table.fmt_map_obj(index)
	ext   = "MAP_EXT_" + (
		"NULL",
		"AY",
		"AY_ARG",
		"XYZ",
		"AY_CODE",
	)[ext]
	return ["{%s, %s, %d, %s, %s}" % (index, ext, code, shape, script)]
d_map_obj = [False, d_map_obj_prc]

def d_tag_prc(argv):
	lst = []
	while True:
		x = ultra.uh()
		o = (x & 0x1FF) - 31
		ay = x >> 9
		if o == -1:
			lst.append("TAG_END,")
			break
		elif o < 0:
			lst.append("%d," % x)
			break
		else:
			px  = ultra.sh()
			py  = ultra.sh()
			pz  = ultra.sh()
			arg = ultra.sh()
			lst.append("TAG(%s, %d, %d, %d, %d, %d)," % (
				UNSM.table.fmt_tag_x[o], ay, px, py, pz, arg,
			))
	ultra.script.c_addr = (ultra.script.c_addr+3) & ~3
	return lst
d_tag = [False, d_tag_prc]

# hud.c

def d_meter_prc(argv):
	mode    = ultra.sb()
	ultra.script.c_addr += 1
	x       = ultra.sh()
	y       = ultra.sh()
	ultra.script.c_addr += 2
	scale   = ultra.fmt_float(ultra.f())
	return ["{%d, %d, %d, %s}" % (mode, x, y, scale)]
d_meter = [False, d_meter_prc]

# object_b.c

# object_c.c

def d_object_c_0_prc(argv):
	msg_start   = UNSM.table.fmt_msg(ultra.sh())
	msg_win     = UNSM.table.fmt_msg(ultra.sh())
	path        = ultra.c.aw(True)
	star_x      = ultra.sh()
	star_y      = ultra.sh()
	star_z      = ultra.sh()
	ultra.script.c_addr += 2
	return ["{%s, %s, %s, {%d, %d, %d}}" % (
		msg_start, msg_win, path, star_x, star_y, star_z
	)]
d_object_c_0 = [False, d_object_c_0_prc]

def d_object_c_1_prc(argv):
	scale   = ultra.fmt_float(ultra.f())
	se      = UNSM.table.fmt_na_se(ultra.uw())
	dist    = ultra.sh()
	damage  = ultra.sb()
	ultra.script.c_addr += 1
	return ["{%s, %s, %d, %d}" % (scale, se, dist, damage)]
d_object_c_1 = [False, d_object_c_1_prc]

def d_object_c_2_prc(argv):
	map_    = ultra.c.aw(True)
	p_map   = ultra.c.aw(True)
	p_shape = UNSM.table.fmt_shape(ultra.sh())
	ultra.script.c_addr += 2
	return ["{%s, %s, %s}" % (map_, p_map, p_shape)]
d_object_c_2 = [False, d_object_c_2_prc]

def d_80332AC0_prc(argv):
	a = ultra.sh()
	b = ultra.sh()
	return ["{%d, %d}" % (a, b)]
d_80332AC0 = [False, d_80332AC0_prc]

def d_object_c_3_prc(argv):
	map_    = ultra.c.aw(True)
	shape   = UNSM.table.fmt_shape(ultra.sh())
	ultra.script.c_addr += 2
	return ["{%s, %s}" % (map_, shape)]
d_object_c_3 = [False, d_object_c_3_prc]

def d_object_c_4_prc(argv):
	msg     = ultra.sh()
	ultra.script.c_addr += 2
	radius  = ultra.fmt_float(ultra.f())
	height  = ultra.fmt_float(ultra.f())
	return ["{%d, %s, %s}" % (msg, radius, height)]
d_object_c_4 = [False, d_object_c_4_prc]

def d_object_c_5_prc(argv):
	shape   = UNSM.table.fmt_shape(ultra.sw())
	script  = ultra.c.aw(True)
	scale   = ultra.fmt_float(ultra.f())
	return ["{%s, %s, %s}" % (shape, script, scale)]
d_object_c_5 = [False, d_object_c_5_prc]

# math.c

def d_bspline_prc(argv):
	time = ultra.sh()
	x    = ultra.sh()
	y    = ultra.sh()
	z    = ultra.sh()
	return ["{%2d, {%5d, %5d, %5d}}" % (time, x, y, z)]
d_bspline = [False, d_bspline_prc]

# shape.c

def d_anime_prc(self, line, tab, argv):
	anime, = argv
	shared = self.c_addr == anime
	self.c_addr = anime
	flag    = UNSM.table.fmt_anime_flag(ultra.sh())
	waist   = ultra.sh()
	start   = ultra.sh()
	loop    = ultra.sh()
	frame   = ultra.sh()
	joint   = ultra.sh()
	val     = ultra.uw()
	tbl     = ultra.uw()
	size    = ultra.uw()
	sym_anime = table.sym_addr(self, anime, rej=True)
	if shared:
		sym_val = table.sym_addr(self, val, rej=True)
		sym_tbl = table.sym_addr(self, tbl, rej=True)
	else:
		self.c_push()
		self.c_addr = tbl
		tbl_data = [(ultra.uh(), ultra.uh()) for _ in range(3*(1+joint))]
		self.c_addr = val
		val_data = [ultra.sh() for _ in range(max([f+i for f, i in tbl_data]))]
		sym_val = table.sym_var(sym_anime.label+"_val", "static short", "[]")
		sym_tbl = table.sym_var(sym_anime.label+"_tbl", "static u16", "[]")
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
		self.c_pull()
	line.append((anime, sym_anime, set(), [
		"/* flag     */  %s," % flag,
		"/* waist    */  %d," % waist,
		"/* start    */  %d," % start,
		"/* loop     */  %d," % loop,
		"/* frame    */  %d," % frame,
		"/* joint    */  %d," % joint,
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

def d_map_prc(argv):
	global obj_vtx
	global obj_tri
	name, = argv
	lst = []
	while True:
		x = ultra.sh()
		if x == 64:
			obj_vtx = [
				(ultra.sh(), ultra.sh(), ultra.sh())
				for _ in range(ultra.sh())
			]
		elif x == 65:
			lst.append("#include \"%s.h\"" % ultra.script.path_rel([name]))
		elif x == 66:
			lst.append("MAP_END,")
			break
		elif x == 67:
			n = ultra.sh()
			lst.append("MAP_OBJECT, %d," % n)
			for _ in range(n):
				o = ultra.sh()
				n = (3, 4, 5, 6, 4)[map_obj_ext[o]]
				o = UNSM.table.fmt_map_obj(o)
				lst.append(" ".join(
					[o + ","] + ["%d," % ultra.sh() for _ in range(n)]
				))
		elif x == 68:
			n = ultra.sh()
			lst.append("MAP_WATER, %d," % n)
			for _ in range(n):
				lst.append(" ".join(["%d," % ultra.sh() for _ in range(6)]))
		else:
			n = 4 if x in {4, 14, 36, 37, 39, 44, 45} else 3
			x = "%d" % x # T:enum(bg)
			obj_tri.extend([
				[x] + [ultra.sh() for _ in range(n)]
				for _ in range(ultra.sh())
			])
	ultra.script.c_addr = (ultra.script.c_addr+3) & ~3
	return lst
d_map = [False, d_map_prc]

def d_area_prc(argv):
	global obj_area
	name, n = argv
	obj_area = [ultra.sb() for _ in range(n)]
	ultra.script.c_addr = (ultra.script.c_addr+3) & ~3
	return ["#include \"%s.h\"" % ultra.script.path_rel([name])]
d_area = [False, d_area_prc]

# objlang.c

# audio/g.c

def d_Na_bgmctl_prc(argv):
	n, = argv
	lst = ["%s," % UNSM.table.fmt_na_bgm(ultra.sh())]
	n -= 1
	while n > 0:
		x = ultra.sh()
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
				v.append(" %d," % ultra.sh())
				n -= 1
			bit >>= 1
		lst.append("".join(c) + ")," + "".join(v))
	ultra.script.c_addr = (ultra.script.c_addr+3) & ~3
	return lst
d_Na_bgmctl = [False, d_Na_bgmctl_prc]

def d_Na_bgmctl_data_prc(argv):
	a_voice = ultra.uh()
	a_vol   = ultra.uh()
	a_time  = ultra.sh()
	b_voice = ultra.uh()
	b_vol   = ultra.uh()
	b_time  = ultra.sh()
	return ["{(s16)0x%04X, 0x%02X, %3d, (s16)0x%04X, 0x%02X, %3d}" % (
		a_voice, a_vol, a_time,
		b_voice, b_vol, b_time,
	)]
d_Na_bgmctl_data = [False, d_Na_bgmctl_data_prc]

# audio/data.c

def d_Na_cfg_prc(argv):
	freq    = ultra.uw()
	voice   = ultra.ub()
	e_filt  = ultra.ub()
	e_size  = ultra.uh()
	e_vol   = ultra.uh()
	vol     = ultra.uh()
	_0C     = ultra.uw()
	_10     = ultra.uw()
	_14     = ultra.uw()
	_18     = ultra.uw()
	arg = (freq, voice, e_filt, e_size, e_vol, vol, _0C, _10, _14, _18)
	if arg == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0):
		return ["{0}"]
	return [(
		"{%5d, %2d, %d, 0x%04X, 0x%04X, 0x%04X, "
		"0x%04X, 0x%04X, 0x%04X, 0x%04X}"
	) % arg]
d_Na_cfg = [False, d_Na_cfg_prc]

# ?

def d_path_data_prc(argv):
	lst = []
	while True:
		x = ultra.sh()
		if x < 0:
			lst.append("%d," % x)
			break
		else:
			lst.append("%d, %d, %d, %d," % (
				x, ultra.sh(), ultra.sh(), ultra.sh(),
			))
	ultra.script.c_addr = (ultra.script.c_addr+3) & ~3
	return lst
d_path_data = [False, d_path_data_prc]

# ========

def d_rendermode_prc(argv):
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
	}[ultra.uw()]]
d_rendermode = [False, d_rendermode_prc]

def d_light_prc(argv):
	a, = argv
	a = ultra.fmt_float(a)
	ultra.script.c_addr += 8
	r = ultra.ub()
	g = ultra.ub()
	b = ultra.ub()
	ultra.script.c_addr += 13
	return ["gdSPDefLight(%s, 0x%02X, 0x%02X, 0x%02X)" % (a, r, g, b)]
d_light = [False, d_light_prc]

def d_matrix_prc(argv):
	h = [ultra.sh() for i in range(16)]
	l = [ultra.uh() for i in range(16)]
	return ["gdSPDefMatrix("] + ["\t" + " ".join([
		ultra.fmt_float(
			float(h[i] << 16 | l[i]) / 0x10000, "", len(argv) == 0
		) + ("," if i != 15 else "") for i in range(i, i+4)
	]) for i in range(0, 16, 4)] + [")"]
d_matrix = [False, d_matrix_prc]

texture_cvt_rgba16 = [False, True, 1, ultra.uh, lambda x: (
	(x >> 11       ) * 0xFF//0x1F,
	(x >>  6 & 0x1F) * 0xFF//0x1F,
	(x >>  1 & 0x1F) * 0xFF//0x1F,
	(x       & 0x01) * 0xFF,
)]
texture_cvt_ia4 = [True, True, 2, ultra.ub, lambda x: (
	(x >> 5       ) * 0xFF//0x07,
	(x >> 4 & 0x01) * 0xFF,
	(x >> 1 & 0x07) * 0xFF//0x07,
	(x      & 0x01) * 0xFF,
)]
texture_cvt_ia8 = [True, True, 1, ultra.ub, lambda x: (
	(x >> 4       ) * 0x11,
	(x      & 0x0F) * 0x11,
)]
texture_cvt_ia16 = [True, True, 1, ultra.uh, lambda x: (
	(x >> 8       ),
	(x      & 0xFF),
)]

def d_texture_prc(argv):
	fmt, w, h, name = argv
	g, a, n, f, c = {
		"rgba16":   texture_cvt_rgba16,
		"ia4":      texture_cvt_ia4,
		"ia8":      texture_cvt_ia8,
		"ia16":     texture_cvt_ia16,
	}[fmt]
	data = [
		[x for x in [c(f()) for _ in range(w//n)] for x in x]
		for _ in range(h)
	]
	writer = png.Writer(w, h, greyscale=g, alpha=a)
	fn = "%s.%s.png" % (ultra.script.path_join([name]), fmt)
	main.mkdir(fn)
	with open(fn, "wb") as f: writer.write(f, data)
	return ["#include \"%s.%s.h\"" % (ultra.script.path_rel([name]), fmt)]
d_texture = [False, d_texture_prc]

def d_gfx_prc(self, line, tab, argv):
	end = argv[0]
	lst = argv[1:]
	i = 0
	name = None
	while self.c_addr < end:
		ultra.c.lst_push(self, line)
		if type(lst[i]) == str:
			name = lst[i]
			i += 1
		i += gfx_prc(self, line, tab, end, name, lst[i])
		ultra.c.lst_push(self, line)
		start = self.c_addr
		while self.c_addr < end:
			w0 = ultra.uw()
			w1 = ultra.uw()
			cmd = w0 >> 24
			if cmd == 0x04:
				self.c_addr -= 8
				break
		if start != self.c_addr:
			argv = [self.c_addr]
			self.c_pull()
			ultra.c.d_Gfx_prc(self, line, tab, argv)
d_gfx = [True, d_gfx_prc]

def g_movemem(argv):
	a_0  = ultra.uw()
	a_1  = ultra.uw()
	d0_0 = ultra.uw()
	d0_1 = ultra.uw()
	if a_0 == 0x03860010 and d0_0 == 0x03880010 and a_1-d0_1 == 8:
		imm = table.imm_addr(ultra.script, ultra.script.c_dst)
		if imm is not None:
			light = ultra.fmt_addr(d0_1, array=(imm, 0x18))
		else:
			light = ultra.fmt_addr(d0_1)
		return ("SPSetLights1N", light)
	return None

def g_tri1(argv):
	w0_0 = ultra.uw()
	w1_0 = ultra.uw()
	w0_1 = ultra.uw()
	w1_1 = ultra.uw()
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

def g_texture(argv):
	w0 = ultra.uw()
	w1 = ultra.uw()
	s = (w1 >> 16) // 62
	t = (w1 & 0xFFFF) // 62
	for x in (s, t):
		if x == 0 or (x & ~(1 << x.bit_length()-1)) != 0:
			return None
	s = "62*%d" % s
	t = "62*%d" % t
	return ultra.c.g_texture_prc(s, t, w0)

def g_loadimageblock(cmd, timg, fmt, siz, width, w):
	tile, uls, ult, lrs, dxt = ultra.c.gx_tile(w[0], w[1])
	if (width, tile, uls, ult) != (1, 7, 0, 0):
		return None
	width  = max(16 >> siz, (0x800 << siz) // dxt)
	height = (lrs+1) // width
	ultra.c.timgproc(timg)
	timg   = ultra.sym(timg)
	fmt    = ultra.c.g_im_fmt[fmt]
	siz    = ultra.c.g_im_siz(siz)
	width  = "%d" % width
	height = "%d" % height
	return (cmd, timg, fmt, siz, width, height)

def g_settimg(argv):
	w = [(ultra.uw(), ultra.uw()) for _ in range(3)]
	fmt, siz, width, timg = ultra.c.gx_settimg(w[0][0], w[0][1])
	if tuple([x[0] >> 24 for x in w]) == (0xFD, 0xE6, 0xF3):
		return g_loadimageblock("DPLoadImageBlock", timg, fmt, siz, width, w[2])
	w += [(ultra.uw(), ultra.uw()) for _ in range(2)]
	c = tuple([x[0] >> 24 for x in w])
	if tuple([x[0] >> 24 for x in w]) == (0xFD, 0xE8, 0xF5, 0xE6, 0xF3):
		if ultra.c.gx_settile(w[2][0], w[2][1]) == (
			fmt, siz, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0
		):
			return g_loadimageblock(
				"DPLoadImageBlockT", timg, fmt, siz, width, w[4]
			)
	return None

def g_rdptilesync(argv):
	w = [(ultra.uw(), ultra.uw()) for _ in range(3)]
	if tuple([x[0] >> 24 for x in w]) == (0xE8, 0xF5, 0xF2):
		fmt, siz, line, tmem, c1_tile, pal, cmt, maskt, shiftt, cms, masks, \
			shifts = ultra.c.gx_settile(w[1][0], w[1][1])
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

def g_setcombine(argv):
	x = ultra.c.g_setcombine_prc(g_setcombine_mode)
	if len(x) == 3:
		return x
	return None

def g_settile(argv):
	w = [(ultra.uw(), ultra.uw()) for _ in range(5)]
	c = tuple([x[0] >> 24 for x in w])
	if c == (0xF5, 0xE6, 0xF3, 0xF5, 0xF2):
		c0_fmt, c0_siz, c0_line, c0_tmem, c0_tile, c0_palette, c0_cmt, \
			c0_maskt, c0_shiftt, c0_cms, c0_masks, c0_shifts = \
			ultra.c.gx_settile(w[0][0], w[0][1])
		c2_tile, c2_uls, c2_ult, c2_lrs, c2_dxt = \
			ultra.c.gx_tile(w[2][0], w[2][1])
		c3_fmt, c3_siz, c3_line, c3_tmem, c3_tile, c3_palette, c3_cmt, \
			c3_maskt, c3_shiftt, c3_cms, c3_masks, c3_shifts = \
			ultra.c.gx_settile(w[3][0], w[3][1])
		c4_t, c4_uls, c4_ult, c4_lrs, c4_lrt = ultra.c.gx_tile(w[4][0], w[4][1])
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
			if siz == 0:
				return ("DPLoadTextureBlock_4bN", fmt) + arg
			siz = ultra.c.g_im_siz(siz)
			return ("DPLoadTextureBlockN", fmt, siz) + arg
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
		x = ultra.ub()
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
	self.c_addr = (self.c_addr+3) & ~3

def s_message(self, argv):
	start, end, data, cmd, path, name, lang = argv
	ultra.init(self, start, data)
	line = ["$name: %s\n$lang: %s\n\n" % (name, lang)]
	lang = UNSM.tools.lang.table[lang]
	while self.c_addr < end:
		x = ultra.uw()
		if x == 0: break
		addr = self.c_addr
		self.c_addr = x
		arg = []
		if cmd == "msg":
			arg = ultra.sw()
			ln  = ultra.sb()
			self.c_addr += 1
			x   = ultra.sh()
			y   = ultra.sh()
			self.c_addr += 2
			self.c_addr = ultra.uw()
			arg = ["%d, %d, %d, %d" % (arg, ln, x, y)]
		line.append("$%s:" % cmd)
		if arg: line.append(" " + "; ".join(arg))
		line.append("\n")
		s_message_str(self, lang, line)
		line.append("\n")
		self.c_addr = addr
	data = "".join(line).rstrip("\n") + "\n"
	fn = self.path_join([path + ".txt"])
	main.mkdir(fn)
	with open(fn, "w") as f: f.write(data)
	self.file[-1][1].append("#include \"%s.h\"\n" % self.path_rel([path]))

# 00 02
def shp_call(argv):
	arg = ultra.ub()
	ultra.script.c_addr += 2
	script = ultra.c.aw(extern=ultra.script.c_dst == 0x16000B1C)
	if arg == 1:
		return ("Call", script)
	return (None, script)

# 01 03 04 05 0B 17
def shp_null(argv):
	ultra.script.c_addr += 3
	return (None,)

# 08
def shp_scene(argv):
	ultra.script.c_addr += 1
	n = "%d" % ultra.sh()
	x = "%d" % ultra.sh()
	y = "%d" % ultra.sh()
	w = "%d" % ultra.sh()
	h = "%d" % ultra.sh()
	return (None, x, y, w, h, n)

# 09 20
def shp_arg(argv):
	ultra.script.c_addr += 1
	arg = "%d" % ultra.sh()
	return (None, arg)

# 0A
def shp_persp(argv):
	c    = ultra.ub()
	fovy = "%d" % ultra.sh()
	n    = "%d" % ultra.sh()
	f    = "%d" % ultra.sh()
	if c:
		callback = ultra.c.aw()
		return ("Perspective", fovy, n, f, callback)
	return (None, fovy, n, f)

# 0C
def shp_layer(argv):
	depth = ultra.fmt_bool[ultra.ub()]
	ultra.script.c_addr += 2
	return (None, depth)

# 0D
def shp_lod(argv):
	ultra.script.c_addr += 3
	min_ = "%d" % ultra.sh()
	max_ = "%d" % ultra.sh()
	return (None, min_, max_)

# 0E 18
def shp_callback(argv):
	ultra.script.c_addr += 1
	arg = ultra.sh()
	callback = ultra.c.aw()
	# s_stage_weather
	# s_face_main
	# s_obj_lib_8029D924
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
		"s_scroll_802D104C",
		"s_scroll_802D1B70",
		"s_scroll_802D1CDC",
		"s_scroll_802D1E48",
		"s_scroll_802D1FA8",
		"s_scroll_802D2108",
	}:
		arg = "0x%04X" % arg
	else:
		arg = "%d" % arg # T:enum(*)
	return (None, arg, callback)

# 0F
def shp_camera(argv):
	ultra.script.c_addr += 1
	arg = "%d" % ultra.sh() # T:enum(camera)
	px  = "%d" % ultra.sh()
	py  = "%d" % ultra.sh()
	pz  = "%d" % ultra.sh()
	lx  = "%d" % ultra.sh()
	ly  = "%d" % ultra.sh()
	lz  = "%d" % ultra.sh()
	callback = ultra.c.aw()
	return (None, arg, px, py, pz, lx, ly, lz, callback)

# 10
def shp_gfx_coord(argv):
	arg = ultra.ub()
	x = arg >> 4 & 7
	if x == 0:
		ultra.script.c_addr += 2
		px = "%d" % ultra.sh()
		py = "%d" % ultra.sh()
		pz = "%d" % ultra.sh()
		ax = "%d" % ultra.sh()
		ay = "%d" % ultra.sh()
		az = "%d" % ultra.sh()
		s = "Coord"
		a = (px, py, pz, ax, ay, az)
	if x == 1:
		px = "%d" % ultra.sh()
		py = "%d" % ultra.sh()
		pz = "%d" % ultra.sh()
		s = "CoordPos"
		a = (px, py, pz)
	if x == 2:
		ax = "%d" % ultra.sh()
		ay = "%d" % ultra.sh()
		az = "%d" % ultra.sh()
		s = "CoordAng"
		a = (ax, ay, az)
	if x == 3:
		ay = "%d" % ultra.sh()
		s = "CoordAY"
		a = (ay,)
	if arg & 0x80:
		layer = UNSM.table.fmt_layer(arg & 15)
		ultra.tag = "gfx"
		gfx = ultra.aw(extern=True)
		return ("Gfx"+s, layer, gfx) + a
	return (s,) + a

# 11 12 14 1D
def shp_gfx_arg(argv):
	c, m = argv
	arg = ultra.ub()
	if m == 0:
		x = "%d" % ultra.sh()
		y = "%d" % ultra.sh()
		z = "%d" % ultra.sh()
		a = (x, y, z)
	else:
		ultra.script.c_addr += 2
		s = ultra.fmt_float(ultra.round_cvt(
			lambda x: float(x)/0x10000,
			lambda x: int(0x10000*x),
			ultra.sw()
		))
		a = (s,)
	if arg & 0x80:
		layer = UNSM.table.fmt_layer(arg & 0x0F)
		ultra.tag = "gfx"
		gfx = ultra.aw(extern=True)
		return (c, layer, gfx) + a
	return (None,) + a

# 13
def shp_gfx_pos(argv):
	layer = UNSM.table.fmt_layer(ultra.ub())
	x = "%d" % ultra.sh()
	y = "%d" % ultra.sh()
	z = "%d" % ultra.sh()
	ultra.tag = "gfx"
	gfx = ultra.aw(extern=True)
	return (None, layer, gfx, x, y, z)

# 15
def shp_gfx(argv):
	layer = UNSM.table.fmt_layer(ultra.ub())
	ultra.script.c_addr += 2
	ultra.tag = "gfx"
	gfx = ultra.aw(extern=True)
	return (None, layer, gfx)

# 16
def shp_shadow(argv):
	ultra.script.c_addr += 1
	type_ = "%d" % ultra.uh() # T:enum(shadow)
	alpha = "%d" % ultra.uh()
	size  = "%d" % ultra.uh()
	return (None, size, alpha, type_)

# 19
def shp_back(argv):
	ultra.script.c_addr += 1
	arg = ultra.sh()
	callback = ultra.c.aw()
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
def shp_hand(argv):
	arg = "%d" % ultra.ub()
	x = "%d" % ultra.sh()
	y = "%d" % ultra.sh()
	z = "%d" % ultra.sh()
	callback = ultra.c.aw()
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
	while self.c_addr < end:
		if ultra.c.lst_push(self, line):
			t = 0
		c = ultra.ub()
		f = shp_fnc[c]
		argv = f[0](f[1:])
		s = argv[0] if argv[0] is not None else shp_str[c]
		if self.addr == 0x0E000000-0x004EB1F0 and self.c_dst == 0x0E00093C:
			c = 0x05
		if c in {0x05} and t > 0: t -= 1
		if c in {0x01}: t = 0
		line[-1][-1].append(
			tab + "\t"*t + "s" + s + "(" + ", ".join(argv[1:]) + "),"
		)
		if c in {0x04}: t += 1
d_s_script = [True, d_s_script_prc]
