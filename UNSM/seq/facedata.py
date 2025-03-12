import main
import ultra

import UNSM.c

ico1 = [
	[main.f_str, "#include \"../face.h\"\n\n"],
	[ultra.c.f_data, "E0.menu.face", 0x04000000, 0x04000648, [
		[0, -67, 1, UNSM.c.d_face_dynlist, 0],
	]],
]

spot = [
	[main.f_str, "#include \"../face.h\"\n\n"],
	[ultra.c.f_data, "E0.menu.face", 0x04000650, 0x04000C20, [
		[0, -62, 1, UNSM.c.d_face_dynlist, 0],
	]],
]

mario = [
	[main.f_str, "#include \"../face.h\"\n\n"],
	[ultra.c.f_data, "E0.menu.face", 0x04000C20, 0x0400AFC0, [
		[0, -440, 3, ultra.c.d_s16], [0, 1, 1, UNSM.c.d_face_dyndata],
		[0, -877, 4, ultra.c.d_s16], [0, 1, 1, UNSM.c.d_face_dyndata],
		[0,  -44, 1, UNSM.c.d_face_dynlist, 1],
		[0,  -48, 3, ultra.c.d_s16], [0, 1, 1, UNSM.c.d_face_dyndata],
		[0,  -82, 4, ultra.c.d_s16], [0, 1, 1, UNSM.c.d_face_dyndata],
		[0,  -28, 1, UNSM.c.d_face_dynlist, 1],
		[0,  -48, 3, ultra.c.d_s16], [0, 1, 1, UNSM.c.d_face_dyndata],
		[0,  -82, 4, ultra.c.d_s16], [0, 1, 1, UNSM.c.d_face_dyndata],
		[0,  -28, 1, UNSM.c.d_face_dynlist, 1],
		[0,  -26, 3, ultra.c.d_s16], [0, 1, 1, UNSM.c.d_face_dyndata],
		[0,  -36, 4, ultra.c.d_s16], [0, 1, 1, UNSM.c.d_face_dyndata],
		[0,  -16, 1, UNSM.c.d_face_dynlist, 1],
		[0,  -26, 3, ultra.c.d_s16], [0, 1, 1, UNSM.c.d_face_dyndata],
		[0,  -36, 4, ultra.c.d_s16], [0, 1, 1, UNSM.c.d_face_dyndata],
		[0,  -16, 1, UNSM.c.d_face_dynlist, 1],
		[0,  -56, 3, ultra.c.d_s16], [0, 1, 1, UNSM.c.d_face_dyndata],
		[0, -100, 4, ultra.c.d_s16], [0, 1, 1, UNSM.c.d_face_dyndata],
		[0, -1042, 1, UNSM.c.d_face_dynlist, 1],
	]],
]

mario_anim = [
	[main.f_str, "#include \"../face.h\"\n\n"],
	[ultra.c.f_data, "E0.menu.face", 0x0400AFC0, 0x040326E0, [
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -820, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -820, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -820, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -820, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -820, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 3, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 6, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 6, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
		[0, -986, 6, ultra.c.d_s16], [0, -3, 1, UNSM.c.d_face_dyndata],
	]],
]

seq = [
	[main.s_file, "src/face/data/ico1.c", ico1],
	[main.s_file, "src/face/data/spot.c", spot],
	[main.s_file, "src/face/data/mario.c", mario],
	[main.s_file, "src/face/data/mario_anim.c", mario_anim],
]
