import main

import UNSM.asm

enemyaobj = [
	[main.f_str, "#include <sm64/objlang.h>\n\n#define SCRIPT\n\n.data\n\n"],
	[UNSM.asm.f_objlang, "E0.Object", 0x13000000, 0x13002EB8],
]

playerobj = [
	[main.f_str, "#include <sm64/objlang.h>\n\n#define SCRIPT\n\n.data\n\n"],
	[UNSM.asm.f_objlang, "E0.Object", 0x13002EC0, 0x13002F98],
]

select_obj = [
	[UNSM.asm.f_objlang, "E0.Object", 0x13002FA0, 0x13003068],
]

enemybobj = [
	[main.f_str, "#include <sm64/objlang.h>\n\n#define SCRIPT\n\n.data\n\n"],
	[main.f_str, "#include \"enemyb/select.c\"\n"],
	[UNSM.asm.f_objlang, "E0.Object", 0x13003068, 0x13004580],
]

enemycobj = [
	[main.f_str, "#include <sm64/objlang.h>\n\n#define SCRIPT\n\n.data\n\n"],
	[UNSM.asm.f_objlang, "E0.Object", 0x13004580, 0x13005610],
]

cameraobj = [
	[main.f_str, "#include <sm64/objlang.h>\n\n#define SCRIPT\n\n.data\n\n"],
	[UNSM.asm.f_objlang, "E0.Object", 0x13005610, 0x130056BC],
]

seq = [
	[main.s_file, "src/enemyaobj.sx", enemyaobj],
	[main.s_file, "src/playerobj.sx", playerobj],
	[main.s_file, "src/enemyb/select.c", select_obj],
	[main.s_file, "src/enemybobj.sx", enemybobj],
	[main.s_file, "src/enemycobj.sx", enemycobj],
	[main.s_file, "src/cameraobj.sx", cameraobj],
]
