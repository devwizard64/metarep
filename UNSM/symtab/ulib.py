import main

sym_J0_E0_ulib_text = {
	# ==========================================================================
	# text
	# ==========================================================================

	# src/math.c
	0x80378800: main.sym_fnc("vecf_cpy", "float *", (
		"VECF dst",
		"VECF src",
	), flag={"GLOBL"}),
	0x80378840: main.sym_fnc("vecf_set", "float *", (
		"VECF v",
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}),
	0x8037888C: main.sym_fnc("vecf_add", "float *", (
		"VECF v",
		"VECF a",
	), flag={"GLOBL"}),
	0x803788E4: main.sym_fnc("vecf_addto", "float *", (
		"VECF v",
		"VECF a",
		"VECF b",
	), flag={"GLOBL"}), # unused
	0x8037893C: main.sym_fnc("vecs_cpy", "short *", (
		"VECS dst",
		"VECS src",
	), flag={"GLOBL"}),
	0x8037897C: main.sym_fnc("vecs_set", "short *", (
		"VECS v",
		"SHORT x",
		"SHORT y",
		"SHORT z",
	), flag={"GLOBL"}),
	0x803789C8: main.sym_fnc("vecs_add", "short *", (
		"VECS v",
		"VECS a",
	), flag={"GLOBL"}), # unused
	0x80378A20: main.sym_fnc("vecs_addto", "short *", (
		"VECS v",
		"VECS a",
		"VECS b",
	), flag={"GLOBL"}), # unused
	0x80378A78: main.sym_fnc("vecs_sub", "short *", (
		"VECS v",
		"VECS a",
	), flag={"GLOBL"}), # unused
	0x80378AD0: main.sym_fnc("vecs_to_vecf", "float *", (
		"VECF dst",
		"VECS src",
	), flag={"GLOBL"}),
	0x80378B34: main.sym_fnc("vecf_to_vecs", "short *", (
		"VECS dst",
		"VECF src",
	), flag={"GLOBL"}),
	0x80378C50: main.sym_fnc("vecf_normal", "float *", (
		"VECF v",
		"VECF v0",
		"VECF v1",
		"VECF v2",
	), flag={"GLOBL"}), # static
	0x80378D38: main.sym_fnc("vecf_cross", "float *", (
		"VECF v",
		"VECF a",
		"VECF b",
	), flag={"GLOBL"}), # static
	0x80378DC0: main.sym_fnc("vecf_normalize", "float *", (
		"VECF v",
	), flag={"GLOBL"}), # static
	0x80378E68: main.sym_fnc("mtxf_cpy", arg=(
		"MTXF dst",
		"MTXF src",
	), flag={"GLOBL"}),
	0x80378EB4: main.sym_fnc("mtxf_identity", arg=(
		"MTXF m",
	), flag={"GLOBL"}),
	0x80378F24: main.sym_fnc("mtxf_pos", arg=(
		"MTXF m",
		"VECF pos",
	), flag={"GLOBL"}),
	0x80378F84: main.sym_fnc("mtxf_lookat", arg=(
		"MTXF m",
		"VECF eye",
		"VECF look",
		"SHORT angz",
	), flag={"GLOBL"}),
	0x80379440: main.sym_fnc("mtxf_coord", arg=(
		"MTXF m",
		"VECF pos",
		"VECS ang",
	), flag={"GLOBL"}),
	0x803795F0: main.sym_fnc("mtxf_joint", arg=(
		"MTXF m",
		"VECF pos",
		"VECS ang",
	), flag={"GLOBL"}),
	0x80379798: main.sym_fnc("mtxf_billboard", arg=(
		"MTXF dst",
		"MTXF src",
		"VECF pos",
		"SHORT angz",
	), flag={"GLOBL"}),
	0x80379918: main.sym_fnc("mtxf_stand", arg=(
		"MTXF m",
		"VECF vy",
		"VECF pos",
		"SHORT angy",
	), flag={"GLOBL"}),
	0x80379AA4: main.sym_fnc("mtxf_ground", arg=(
		"MTXF m",
		"VECF pos",
		"SHORT angy",
		"float radius",
	), flag={"GLOBL"}),
	0x80379F60: main.sym_fnc("mtxf_cat", arg=(
		"MTXF m",
		"MTXF a",
		"MTXF b",
	), flag={"GLOBL"}),
	0x8037A29C: main.sym_fnc("mtxf_scale", arg=(
		"MTXF dst",
		"MTXF src",
		"VECF scale",
	), flag={"GLOBL"}),
	0x8037A348: main.sym_fnc("mtxf_transform", arg=(
		"MTXF m",
		"VECS v",
	), flag={"GLOBL"}), # unused
	0x8037A434: main.sym_fnc("mtxf_to_mtx", arg=(
		"Mtx *m",
		"MTXF mf",
	), flag={"GLOBL"}),
	0x8037A4B8: main.sym_fnc("mtx_angz", arg=(
		"Mtx *m",
		"SHORT angz",
	), flag={"GLOBL"}),
	0x8037A550: main.sym_fnc("vecf_scenepos", arg=(
		"VECF v",
		"MTXF m",
		"MTXF cam",
	), flag={"GLOBL"}),
	0x8037A69C: main.sym_fnc("cartesian_to_polar", arg=(
		"VECF a",
		"VECF b",
		"float *dist",
		"short *angx",
		"short *angy",
	), flag={"GLOBL"}),
	0x8037A788: main.sym_fnc("polar_to_cartesian", arg=(
		"VECF a",
		"VECF b",
		"float dist",
		"SHORT angx",
		"SHORT angy",
	), flag={"GLOBL"}),
	0x8037A860: main.sym_fnc("convergei", "int", (
		"int x",
		"int dst",
		"int inc",
		"int dec",
	), flag={"GLOBL"}),
	0x8037A8B4: main.sym_fnc("convergef", "float", (
		"float x",
		"float dst",
		"float inc",
		"float dec",
	), flag={"GLOBL"}),
	0x8037A924: main.sym_fnc("atan_yx", "USHORT", (
		"float y",
		"float x",
	)),
	0x8037A9A8: main.sym_fnc("ATAN2", "short", (
		"float y",
		"float x",
	), flag={"GLOBL"}),
	0x8037AB88: main.sym_fnc("atan2f", "float", (
		"float y",
		"float x",
	), flag={"GLOBL"}), # unused
	0x8037ABEC: main.sym_fnc("bspline_curve", arg=(
		"float curve[4]",
		"float phase",
		"int mode",
	)),
	0x8037AC74: main.sym_fnc("L8037AC74", flag={"GLOBL","LOCAL"}),
	0x8037AD04: main.sym_fnc("L8037AD04", flag={"GLOBL","LOCAL"}),
	0x8037ADC0: main.sym_fnc("L8037ADC0", flag={"GLOBL","LOCAL"}),
	0x8037AE5C: main.sym_fnc("L8037AE5C", flag={"GLOBL","LOCAL"}),
	0x8037AF18: main.sym_fnc("L8037AF18", flag={"GLOBL","LOCAL"}),
	0x8037AFB8: main.sym_fnc("bspline_init", arg=(
		"BSPLINE *b",
	), flag={"GLOBL"}),
	0x8037AFE8: main.sym_fnc("bspline_proc", "int", (
		"VECF dst",
	), flag={"GLOBL"}),

	# src/shape.c
	0x8037B220: main.sym_fnc("shape_init", arg=(
		"SHAPE *shape",
		"int type",
	)),
	0x8037B24C: main.sym_fnc("s_create_scene", "S_SCENE *", (
		"ARENA *arena",
		"S_SCENE *shp",
		"SHORT index",
		"SHORT x",
		"SHORT y",
		"SHORT w",
		"SHORT h",
	), flag={"GLOBL"}),
	0x8037B30C: main.sym_fnc("s_create_ortho", "S_ORTHO *", (
		"ARENA *arena",
		"S_ORTHO *shp",
		"float scale",
	), flag={"GLOBL"}),
	0x8037B380: main.sym_fnc("s_create_persp", "S_PERSP *", (
		"ARENA *arena",
		"S_PERSP *shp",
		"float fovy",
		"SHORT near",
		"SHORT far",
		"SHPCALL *callback",
		"unsigned long arg",
	), flag={"GLOBL"}),
	0x8037B448: main.sym_fnc("s_create_empty", "SHAPE *", (
		"ARENA *arena",
		"SHAPE *shp",
	), flag={"GLOBL"}),
	0x8037B4AC: main.sym_fnc("s_create_layer", "S_LAYER *", (
		"ARENA *arena",
		"S_LAYER *shp",
		"SHORT zb",
	), flag={"GLOBL"}),
	0x8037B530: main.sym_fnc("s_create_lod", "S_LOD *", (
		"ARENA *arena",
		"S_LOD *shp",
		"SHORT min",
		"SHORT max",
	), flag={"GLOBL"}),
	0x8037B5B4: main.sym_fnc("s_create_select", "S_SELECT *", (
		"ARENA *arena",
		"S_SELECT *shp",
		"SHORT code",
		"SHORT index",
		"SHPCALL *callback",
		"unsigned long arg",
	), flag={"GLOBL"}),
	0x8037B670: main.sym_fnc("s_create_camera", "S_CAMERA *", (
		"ARENA *arena",
		"S_CAMERA *shp",
		"VECF eye",
		"VECF look",
		"SHPCALL *callback",
		"unsigned long arg",
	), flag={"GLOBL"}),
	0x8037B744: main.sym_fnc("s_create_coord", "S_COORD *", (
		"ARENA *arena",
		"S_COORD *shp",
		"int layer",
		"Gfx *gfx",
		"VECS pos",
		"VECS ang",
	), flag={"GLOBL"}),
	0x8037B7F8: main.sym_fnc("s_create_pos", "S_POS *", (
		"ARENA *arena",
		"S_POS *shp",
		"int layer",
		"Gfx *gfx",
		"VECS pos",
	), flag={"GLOBL"}),
	0x8037B89C: main.sym_fnc("s_create_ang", "S_ANG *", (
		"ARENA *arena",
		"S_ANG *shp",
		"int layer",
		"Gfx *gfx",
		"VECS ang",
	), flag={"GLOBL"}),
	0x8037B940: main.sym_fnc("s_create_scale", "S_SCALE *", (
		"ARENA *arena",
		"S_SCALE *shp",
		"int layer",
		"Gfx *gfx",
		"float scale",
	), flag={"GLOBL"}),
	0x8037B9E0: main.sym_fnc("s_create_object", "S_OBJECT *", (
		"ARENA *arena",
		"S_OBJECT *shp",
		"SHAPE *shape",
		"VECF pos",
		"VECS ang",
		"VECF scale",
	), flag={"GLOBL"}),
	0x8037BAD4: main.sym_fnc("s_create_cull", "S_CULL *", (
		"ARENA *arena",
		"S_CULL *shp",
		"SHORT dist",
	), flag={"GLOBL"}),
	0x8037BB48: main.sym_fnc("s_create_joint", "S_JOINT *", (
		"ARENA *arena",
		"S_JOINT *shp",
		"int layer",
		"Gfx *gfx",
		"VECS pos",
	), flag={"GLOBL"}),
	0x8037BBEC: main.sym_fnc("s_create_billboard", "S_BILLBOARD *", (
		"ARENA *arena",
		"S_BILLBOARD *shp",
		"int layer",
		"Gfx *gfx",
		"VECS pos",
	), flag={"GLOBL"}),
	0x8037BC90: main.sym_fnc("s_create_gfx", "S_GFX *", (
		"ARENA *arena",
		"S_GFX *shp",
		"int layer",
		"Gfx *gfx",
	), flag={"GLOBL"}),
	0x8037BD24: main.sym_fnc("s_create_shadow", "S_SHADOW *", (
		"ARENA *arena",
		"S_SHADOW *shp",
		"SHORT size",
		"UCHAR alpha",
		"UCHAR type",
	), flag={"GLOBL"}),
	0x8037BDB4: main.sym_fnc("s_create_list", "S_LIST *", (
		"ARENA *arena",
		"S_LIST *shp",
		"SHAPE *shape",
	), flag={"GLOBL"}),
	0x8037BE28: main.sym_fnc("s_create_callback", "S_CALLBACK *", (
		"ARENA *arena",
		"S_CALLBACK *shp",
		"SHPCALL *callback",
		"unsigned long arg",
	), flag={"GLOBL"}),
	0x8037BECC: main.sym_fnc("s_create_back", "S_BACK *", (
		"ARENA *arena",
		"S_BACK *shp",
		"USHORT code",
		"SHPCALL *callback",
		"unsigned long arg",
	), flag={"GLOBL"}),
	0x8037BF84: main.sym_fnc("s_create_hand", "S_HAND *", (
		"ARENA *arena",
		"S_HAND *shp",
		"S_OBJECT *obj",
		"VECS pos",
		"SHPCALL *callback",
		"unsigned long arg",
	), flag={"GLOBL"}),
	0x8037C044: main.sym_fnc("shape_link", "SHAPE *", (
		"SHAPE *parent",
		"SHAPE *shape",
	), flag={"GLOBL"}),
	0x8037C0BC: main.sym_fnc("shape_unlink", "SHAPE *", (
		"SHAPE *shape",
	), flag={"GLOBL"}),
	0x8037C138: main.sym_fnc("shape_makefirst", "SHAPE *", (
		"SHAPE *shape",
	), flag={"GLOBL"}),
	0x8037C1E4: main.sym_fnc("shape_notify", arg=(
		"SHAPE *shape",
		"int code",
	)),
	0x8037C360: main.sym_fnc("s_scene_notify", arg=(
		"S_SCENE *shp",
		"int code",
	), flag={"GLOBL"}),
	0x8037C3D0: main.sym_fnc("sobj_init", arg=(
		"S_OBJECT *shp",
	), flag={"GLOBL"}),
	0x8037C448: main.sym_fnc("sobj_enter", arg=(
		"S_OBJECT *shp",
		"SHAPE *shape",
		"VECF pos",
		"VECS ang",
	), flag={"GLOBL"}),
	0x8037C51C: main.sym_fnc("sobj_actor", arg=(
		"S_OBJECT *shp",
		"ACTOR *actor",
	), flag={"GLOBL"}),
	0x8037C658: main.sym_fnc("sobj_set_anime", arg=(
		"S_OBJECT *shp",
		"ANIME **animep",
	), flag={"GLOBL"}),
	0x8037C708: main.sym_fnc("sobj_set_animev", arg=(
		"S_OBJECT *shp",
		"ANIME **animep",
		"int speed",
	), flag={"GLOBL"}),
	0x8037C7D8: main.sym_fnc("anime_index", "int", (
		"int frame",
		"u16 **tbl",
	), flag={"GLOBL"}),
	0x8037C844: main.sym_fnc("skel_step", "int", (
		"SKELETON *skel",
		"s32 *vframe",
	), flag={"GLOBL"}),
	0x8037C9E8: main.sym_fnc("sobj_get_animepos", arg=(
		"S_OBJECT *shp",
		"VECF pos",
	)), # unused
	0x8037CB10: main.sym_fnc("shape_get_scene", "S_SCENE *", (
		"SHAPE *shape",
	)), # unused

	# src/shplang.c
	0x8037CB60: main.sym_fnc("s_read_vecf", "short *", (
		"VECF dst",
		"short *src",
	)),
	0x8037CBC0: main.sym_fnc("s_read_vecs", "short *", (
		"VECS dst",
		"short *src",
	)),
	0x8037CBFC: main.sym_fnc("s_read_ang", "short *", (
		"VECS dst",
		"short *src",
	)),
	0x8037CC74: main.sym_fnc("s_link", arg=(
		"SHAPE *shape",
	)),
	0x8037CD60: main.sym_fnc("s_cmd_execute"), # data
	0x8037CE24: main.sym_fnc("s_cmd_exit"), # data
	0x8037CEE8: main.sym_fnc("s_cmd_jump"), # data
	0x8037CF70: main.sym_fnc("s_cmd_return"), # data
	0x8037CFC0: main.sym_fnc("s_cmd_start"), # data
	0x8037D018: main.sym_fnc("s_cmd_end"), # data
	0x8037D050: main.sym_fnc("s_cmd_store"), # data
	0x8037D0D0: main.sym_fnc("s_cmd_flag"), # data
	0x8037D1D0: main.sym_fnc("s_cmd_scene"), # data
	0x8037D328: main.sym_fnc("s_cmd_ortho"), # data
	0x8037D3A4: main.sym_fnc("s_cmd_persp"), # data
	0x8037D48C: main.sym_fnc("s_cmd_empty"), # data
	0x8037D4DC: main.sym_fnc("s_cmd_31"), # data
	0x8037D500: main.sym_fnc("s_cmd_layer"), # data
	0x8037D55C: main.sym_fnc("s_cmd_lod"), # data
	0x8037D5D4: main.sym_fnc("s_cmd_select"), # data
	0x8037D640: main.sym_fnc("s_cmd_camera"), # data
	0x8037D6F0: main.sym_fnc("s_cmd_coord"), # data
	0x8037D8D4: main.sym_fnc("s_cmd_pos"), # data
	0x8037D998: main.sym_fnc("s_cmd_ang"), # data
	0x8037DA5C: main.sym_fnc("s_cmd_scale"), # data
	0x8037DB50: main.sym_fnc("s_cmd_30"), # data
	0x8037DB74: main.sym_fnc("s_cmd_joint"), # data
	0x8037DC10: main.sym_fnc("s_cmd_billboard"), # data
	0x8037DCD4: main.sym_fnc("s_cmd_gfx"), # data
	0x8037DD4C: main.sym_fnc("s_cmd_shadow"), # data
	0x8037DDDC: main.sym_fnc("s_cmd_object"), # data
	0x8037DE34: main.sym_fnc("s_cmd_callback"), # data
	0x8037DE94: main.sym_fnc("s_cmd_back"), # data
	0x8037DEF8: main.sym_fnc("s_cmd_26"), # data
	0x8037DF1C: main.sym_fnc("s_cmd_load"), # data
	0x8037DFD4: main.sym_fnc("s_cmd_hand"), # data
	0x8037E058: main.sym_fnc("s_cmd_cull"), # data
	0x8037E0B4: main.sym_fnc("s_process", "SHAPE *", (
		"ARENA *arena",
		"S_SCRIPT *script",
	), flag={"GLOBL"}),

	# src/prglang.c
	0x8037E1A0: main.sym_fnc("p_cmp", "int", (
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
	0x8037E2C4: main.sym_fnc("p_cmd_execute"), # data
	0x8037E388: main.sym_fnc("p_cmd_chain"), # data
	0x8037E404: main.sym_fnc("p_cmd_exit"), # data
	0x8037E47C: main.sym_fnc("p_cmd_sleep"), # data
	0x8037E4FC: main.sym_fnc("p_cmd_freeze"), # data
	0x8037E580: main.sym_fnc("p_cmd_jump"), # data
	0x8037E5B8: main.sym_fnc("p_cmd_call"), # data
	0x8037E620: main.sym_fnc("p_cmd_return"), # data
	0x8037E650: main.sym_fnc("p_cmd_for"), # data
	0x8037E6D4: main.sym_fnc("p_cmd_done"), # data
	0x8037E780: main.sym_fnc("p_cmd_repeat"), # data
	0x8037E7F8: main.sym_fnc("p_cmd_until"), # data
	0x8037E878: main.sym_fnc("p_cmd_jump_if"), # data
	0x8037E8E8: main.sym_fnc("p_cmd_call_if"), # data
	0x8037E988: main.sym_fnc("p_cmd_if"), # data
	0x8037EA18: main.sym_fnc("p_cmd_else"), # data
	0x8037EA70: main.sym_fnc("p_cmd_endif"), # data
	0x8037EA98: main.sym_fnc("p_cmd_callback"), # data
	0x8037EB04: main.sym_fnc("p_cmd_process"), # data
	0x8037EB98: main.sym_fnc("p_cmd_set"), # data
	0x8037EBD4: main.sym_fnc("p_cmd_push"), # data
	0x8037EC14: main.sym_fnc("p_cmd_pull"), # data
	0x8037EC54: main.sym_fnc("p_cmd_load_code"), # data
	0x8037ECA4: main.sym_fnc("p_cmd_load_data"), # data
	0x8037ECF8: main.sym_fnc("p_cmd_load_pres"), # data
	0x8037ED48: main.sym_fnc("p_cmd_load_face"), # data
	0x8037EDF8: main.sym_fnc("p_cmd_load_text"), # data
	0x8037EE48: main.sym_fnc("p_cmd_stage_init"), # data
	0x8037EEA8: main.sym_fnc("p_cmd_stage_exit"), # data
	0x8037EF00: main.sym_fnc("p_cmd_stage_start"), # data
	0x8037EF70: main.sym_fnc("p_cmd_stage_end"), # data
	0x8037F010: main.sym_fnc("p_cmd_scene_start"), # data
	0x8037F130: main.sym_fnc("p_cmd_scene_end"), # data
	0x8037F164: main.sym_fnc("p_cmd_shape_gfx"), # data
	0x8037F214: main.sym_fnc("p_cmd_shape_script"), # data
	0x8037F2A4: main.sym_fnc("p_cmd_shape_scale"), # data
	0x8037F36C: main.sym_fnc("p_cmd_player"), # data
	0x8037F45C: main.sym_fnc("p_cmd_object"), # data
	0x8037F67C: main.sym_fnc("p_cmd_port"), # data
	0x8037F790: main.sym_fnc("p_cmd_connect"), # data
	0x8037F920: main.sym_fnc("p_cmd_env"), # data
	0x8037F994: main.sym_fnc("p_cmd_bgport"), # data
	0x8037FB18: main.sym_fnc("p_cmd_wind"), # data
	0x8037FC38: main.sym_fnc("p_cmd_jet"), # data
	0x8037FDE4: main.sym_fnc("p_cmd_vi_black"), # data
	0x8037FE2C: main.sym_fnc("p_cmd_vi_gamma"), # data
	0x8037FE94: main.sym_fnc("p_cmd_map"), # data
	0x8037FF14: main.sym_fnc("p_cmd_area"), # data
	0x8037FF94: main.sym_fnc("p_cmd_tag"), # data
	0x80380014: main.sym_fnc("p_cmd_scene_open"), # data
	0x8038007C: main.sym_fnc("p_cmd_scene_close"), # data
	0x803800BC: main.sym_fnc("p_cmd_player_open"), # data
	0x80380160: main.sym_fnc("p_cmd_player_close"), # data
	0x803801A0: main.sym_fnc("p_cmd_scene_proc"), # data
	0x803801E0: main.sym_fnc("p_cmd_wipe"), # data
	0x8038024C: main.sym_fnc("p_cmd_32"), # data
	0x80380274: main.sym_fnc("p_cmd_msg"), # data
	0x80380300: main.sym_fnc("p_cmd_bgm"), # data
	0x8038039C: main.sym_fnc("p_cmd_bgm_play"), # data
	0x803803EC: main.sym_fnc("p_cmd_aud_fadeout"), # data
	0x80380434: main.sym_fnc("p_cmd_var"), # data
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
	0x803805C8: main.sym_fnc("p_execute", "P_SCRIPT *", (
		"P_SCRIPT *pc",
	), flag={"GLOBL"}),

	# src/bgcheck.c
	0x80380690: main.sym_fnc("bglist_check_wall", "int", (
		"BGLIST *list",
		"WALLCHECK *check",
	)),
	0x80380DE8: main.sym_fnc("bg_hit_wall", "int", (
		"float *x",
		"float *y",
		"float *z",
		"float offset",
		"float radius",
	), flag={"GLOBL"}),
	0x80380E8C: main.sym_fnc("bg_check_wall", "int", (
		"WALLCHECK *check",
	), flag={"GLOBL"}),
	0x80381038: main.sym_fnc("bglist_check_roof", "BGFACE *", (
		"BGLIST *list",
		"int x",
		"int y",
		"int z",
		"float *roof_y",
	)),
	0x80381264: main.sym_fnc("bg_check_roof", "float", (
		"float x",
		"float y",
		"float z",
		"BGFACE **roof",
	), flag={"GLOBL"}),
	0x80381470: main.sym_fnc("obj_ground_y", "float", (
		"OBJECT *obj",
	)), # unused
	0x803814B8: main.sym_fnc("bg_check_plane", "float", (
		"float x",
		"float y",
		"float z",
		"PLANE **plane",
	), flag={"GLOBL"}),
	0x8038156C: main.sym_fnc("bglist_check_ground", "float", (
		"BGLIST *list",
		"int x",
		"int y",
		"int z",
		"float *ground_y",
	)),
	0x80381794: main.sym_fnc("bg_check_ground_y", "float", (
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}),
	0x803817E0: main.sym_fnc("bg_check_ground_movebg", "float", (
		"float x",
		"float y",
		"float z",
		"BGFACE **ground",
	)), # unused
	0x80381900: main.sym_fnc("bg_check_ground", "float", (
		"float x",
		"float y",
		"float z",
		"BGFACE **ground",
	), flag={"GLOBL"}),
	0x80381BA0: main.sym_fnc("bg_check_water", "float", (
		"float x",
		"float z",
	), flag={"GLOBL"}),
	0x80381D3C: main.sym_fnc("bg_check_gas", "float", (
		"float x",
		"float z",
	), flag={"GLOBL"}),
	0x80381EC8: main.sym_fnc("bglist_len", "int", (
		"BGLIST *list",
	)),
	0x80381F08: main.sym_fnc("bgcheck_debug", arg=(
		"float x",
		"float z",
	), flag={"GLOBL"}),
	0x80382294: main.sym_fnc("bg_hit_ground_roof", "int", (
		"int flag",
		"float *x",
		"float *y",
		"float *z",
		"float radius",
		"BGFACE **face",
		"float *face_y",
	)), # unused

	# src/bgload.c
	0x80382490: main.sym_fnc("bglist_alloc", "BGLIST *"),
	0x803824F8: main.sym_fnc("bgface_alloc", "BGFACE *"),
	0x80382590: main.sym_fnc("bgroot_clear", arg=(
		"BGROOT *root",
	)),
	0x803825D0: main.sym_fnc("statbg_clear"),
	0x803825FC: main.sym_fnc("bglist_create", arg=(
		"SHORT flag",
		"SHORT ix",
		"SHORT iz",
		"BGFACE *face",
	)),
	0x8038283C: main.sym_fnc("min3", "SHORT", (
		"SHORT x",
		"SHORT y",
		"SHORT z",
	)),
	0x8038289C: main.sym_fnc("max3", "SHORT", (
		"SHORT x",
		"SHORT y",
		"SHORT z",
	)),
	0x803828FC: main.sym_fnc("bgarea_min", "SHORT", (
		"SHORT x",
	)),
	0x80382990: main.sym_fnc("bgarea_max", "SHORT", (
		"SHORT x",
	)),
	0x80382A2C: main.sym_fnc("bgface_link", arg=(
		"BGFACE *face",
		"int flag",
	)),
	0x80382B6C: main.sym_fnc("bgload_80382B6C"), # unused
	0x80382B7C: main.sym_fnc("bgface_create", "BGFACE *", (
		"MAP *vtx",
		"MAP **map",
	)),
	0x80382F84: main.sym_fnc("bgface_hasattr", "int", (
		"SHORT code",
	)),
	0x80382FBC: main.sym_fnc("L80382FBC", flag={"GLOBL","LOCAL"}),
	0x80382FCC: main.sym_fnc("L80382FCC", flag={"GLOBL","LOCAL"}),
	0x80382FEC: main.sym_fnc("bgface_flag", "int", (
		"SHORT code",
	)),
	0x80383068: main.sym_fnc("statbg_face", arg=(
		"MAP **map",
		"MAP *vtx",
		"SHORT code",
		"AREA **area",
	)),
	0x803831D0: main.sym_fnc("statbg_vtx", "MAP *", (
		"MAP **map",
	)),
	0x80383228: main.sym_fnc("statbg_water", arg=(
		"MAP **map",
	)),
	0x80383340: main.sym_fnc("map_init", flag={"GLOBL"}),
	0x803833B8: main.sym_fnc("map_load", arg=(
		"SHORT scene",
		"MAP *map",
		"AREA *area",
		"TAG *tag",
	), flag={"GLOBL"}),
	0x803835A4: main.sym_fnc("movebg_clear", flag={"GLOBL"}),
	0x80383604: main.sym_fnc("bgload_80383604"), # unused
	0x80383614: main.sym_fnc("movebg_vtx", arg=(
		"MAP **map",
		"MAP *vtx",
	)),
	0x80383828: main.sym_fnc("movebg_face", arg=(
		"MAP **map",
		"MAP *vtx",
	)),
	0x803839CC: main.sym_fnc("object_map_load", flag={"GLOBL"}), # o callback

	# src/objlang.c
	0x80383B70: main.sym_fnc("o_jump", arg=(
		"O_SCRIPT *script",
	)), # unused
	0x80383BB0: main.sym_fnc("rand", "u16", flag={"GLOBL"}),
	0x80383CB4: main.sym_fnc("randf", "float", flag={"GLOBL"}),
	0x80383D1C: main.sym_fnc("randsign", "int", flag={"GLOBL"}),
	0x80383D68: main.sym_fnc("obj_set_shapecoord", arg=(
		"OBJECT *obj",
	)),
	0x80383DBC: main.sym_fnc("o_push", arg=(
		"unsigned long x",
	)),
	0x80383DF8: main.sym_fnc("o_pull", "unsigned long"),
	0x80383E44: main.sym_fnc("o_error"), # unused
	0x80383E5C: main.sym_fnc("o_cmd_shapehide", "int"), # data
	0x80383EA0: main.sym_fnc("o_cmd_shapedisable", "int"), # data
	0x80383EE4: main.sym_fnc("o_cmd_billboard", "int"), # data
	0x80383F24: main.sym_fnc("o_cmd_shape", "int"), # data
	0x80383F94: main.sym_fnc("o_cmd_makeobj", "int"), # data
	0x8038401C: main.sym_fnc("o_cmd_makechild", "int"), # data
	0x803840B4: main.sym_fnc("o_cmd_makeobjcode", "int"), # data
	0x80384164: main.sym_fnc("o_cmd_destroy", "int"), # data
	0x80384188: main.sym_fnc("o_cmd_exit", "int"), # data
	0x803841A0: main.sym_fnc("o_cmd_end", "int"), # data
	0x803841B8: main.sym_fnc("o_cmd_call", "int"), # data
	0x80384224: main.sym_fnc("o_cmd_return", "int"), # data
	0x8038425C: main.sym_fnc("o_cmd_sleep", "int"), # data
	0x803842E4: main.sym_fnc("o_cmd_memsleep", "int"), # data
	0x8038438C: main.sym_fnc("o_cmd_jump", "int"), # data
	0x803843E0: main.sym_fnc("o_cmd_for2", "int"), # data
	0x80384450: main.sym_fnc("o_cmd_for", "int"), # data
	0x803844C0: main.sym_fnc("o_cmd_fend", "int"), # data
	0x80384554: main.sym_fnc("o_cmd_fcontinue", "int"), # data
	0x803845E8: main.sym_fnc("o_cmd_while", "int"), # data
	0x80384634: main.sym_fnc("o_cmd_wend", "int"), # data
	0x80384678: main.sym_fnc("o_cmd_callback", "int"), # data
	0x803846D0: main.sym_fnc("o_cmd_setf", "int"), # data
	0x8038475C: main.sym_fnc("o_cmd_seti", "int"), # data
	0x803847D4: main.sym_fnc("o_cmd_sets", "int"), # data
	0x80384854: main.sym_fnc("o_cmd_setrandf", "int"), # data
	0x80384928: main.sym_fnc("o_cmd_setrandi", "int"), # data
	0x803849F8: main.sym_fnc("o_cmd_setranda", "int"), # data
	0x80384AB4: main.sym_fnc("o_cmd_addrandf", "int"), # data
	0x80384B90: main.sym_fnc("o_cmd_addranda", "int"), # data
	0x80384C5C: main.sym_fnc("o_cmd_addf", "int"), # data
	0x80384CF0: main.sym_fnc("o_cmd_addi", "int"), # data
	0x80384D70: main.sym_fnc("o_cmd_setflag", "int"), # data
	0x80384E04: main.sym_fnc("o_cmd_clrflag", "int"), # data
	0x80384E9C: main.sym_fnc("o_cmd_ptr", "int"), # data
	0x80384F08: main.sym_fnc("o_cmd_anime", "int"), # data
	0x80384F8C: main.sym_fnc("o_cmd_ground", "int"), # data
	0x8038503C: main.sym_fnc("o_cmd_24", "int"), # data
	0x80385084: main.sym_fnc("o_cmd_25", "int"), # data
	0x803850CC: main.sym_fnc("o_cmd_26", "int"), # data
	0x80385114: main.sym_fnc("o_cmd_memaddf", "int"), # data
	0x803851D0: main.sym_fnc("o_cmd_memaddi", "int"), # data
	0x8038528C: main.sym_fnc("o_cmd_hit", "int"), # data
	0x8038531C: main.sym_fnc("o_cmd_dmg", "int"), # data
	0x803853AC: main.sym_fnc("o_cmd_hitoff", "int"), # data
	0x8038546C: main.sym_fnc("o_cmd_36", "int"), # data
	0x803854CC: main.sym_fnc("o_cmd_init", "int"), # data
	0x8038556C: main.sym_fnc("o_setrandtbl", arg=(
		"int len",
	)), # unused
	0x803856A0: main.sym_fnc("o_cmd_map", "int"), # data
	0x80385700: main.sym_fnc("o_cmd_save", "int"), # data
	0x8038575C: main.sym_fnc("o_cmd_hitcode", "int"), # data
	0x803857A0: main.sym_fnc("o_cmd_hitflag", "int"), # data
	0x803857E4: main.sym_fnc("o_cmd_scale", "int"), # data
	0x8038586C: main.sym_fnc("o_cmd_physics", "int"), # data
	0x80385A60: main.sym_fnc("o_cmd_memclrparentflag", "int"), # data
	0x80385AF0: main.sym_fnc("o_cmd_splash", "int"), # data
	0x80385B4C: main.sym_fnc("o_cmd_inc", "int"), # data
	0x80385BF0: main.sym_fnc("o_init", flag={"GLOBL"}),
	0x80385C00: main.sym_fnc("o_execute", flag={"GLOBL"}),

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
	0x80385FD0: main.sym_var("vecf_0", "VECF", flag={"GLOBL"}),
	0x80385FDC: main.sym_var("vecs_0", "VECS", flag={"GLOBL"}),
	0x80385FE4: main.sym_var("vecf_1", "VECF", flag={"GLOBL"}),
	0x80385FF0: main.sym_var("vecs_1", "VECS", flag={"GLOBL"}), # unused

	# src/mathtbl.s
	0x80386000: main.sym_var("math_sin", "float", "[]", flag={"GLOBL"}),
	0x80387000: main.sym_var("math_cos", "float", "[]", flag={"GLOBL"}),
	0x8038B000: main.sym_var("math_atan", "short", "[]", flag={"GLOBL"}),

	# src/shplang.c
	0x8038B810: main.sym_var_fnc("s_cmd_table", lst="[]"),

	# src/prglang.c
	0x8038B8A0: main.sym_var("p_arena", "ARENA *", flag={"DALIGN"}),
	0x8038B8A4: main.sym_var("p_sleep", "u16", flag={"DALIGN"}),
	0x8038B8A8: main.sym_var("p_freeze", "u16", flag={"DALIGN"}),
	0x8038B8AC: main.sym_var("p_scene", "s16", flag={"DALIGN"}),
	0x8038B8B0: main.sym_var("p_sp", "unsigned long *", flag={"DALIGN"}),
	0x8038B8B4: main.sym_var("p_fp", "unsigned long *", flag={"DALIGN"}),
	0x8038B8B8: main.sym_var_fnc("p_cmd_table", lst="[]"),

	# src/objlang.c
	0x8038B9B0: main.sym_var_fnc("o_cmd_table", lst="[]", val="int"),

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
	0x8038BCA0: main.sym_var("s_arena", "ARENA *"),
	0x8038BCA4: main.sym_var("shp_root", "SHAPE *"),
	0x8038BCA8: main.sym_var("shp_8038BCA8", "SHAPE *"), # unused
	0x8038BCAC: main.sym_var("shp_table", "SHAPE **"),
	0x8038BCB0: main.sym_var("shp_count", "u16"),
	0x8038BCB8: main.sym_var("s_stack", "unsigned long", "[16]", flag={"BALIGN"}),
	0x8038BCF8: main.sym_var("shp_stack", "SHAPE *", "[32]", flag={"BALIGN"}),
	0x8038BD78: main.sym_var("shp_sp", "s16"),
	0x8038BD7A: main.sym_var("s_sp", "s16"),
	0x8038BD7C: main.sym_var("shp_fp", "s16"), # unused
	0x8038BD7E: main.sym_var("s_fp", "s16"),
	0x8038BD80: main.sym_var("s_pc", "S_SCRIPT *"),
	0x8038BD88: main.sym_var("sobj_list", "SHAPE", flag={"GLOBL","BALIGN"}),

	# src/prglang.c
	0x8038BDA0: main.sym_var("p_stack", "unsigned long", "[32]", flag={"BALIGN"}),
	0x8038BE20: main.sym_var("p_state", "s16"),
	0x8038BE24: main.sym_var("p_status", "int"),
	0x8038BE28: main.sym_var("p_pc", "P_SCRIPT *"),

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
	0x8038EEE0: main.sym_var("rand_seed", "u16", flag={"GLOBL"}),
}

sym_G0_ulib_text = {
	0x80378800: main.sym("vecf_cpy", flag={"GLOBL"}),
}

sym_DD_ulib_text = {
	0x80510000: main.sym("vecf_cpy", flag={"GLOBL"}),
}

sym_P0_ulib_text = {
	0x8036FF00: main.sym("P0_8036FF00"),
}
