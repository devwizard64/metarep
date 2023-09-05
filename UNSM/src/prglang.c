#include <sm64.h>

#define P_UCHAR         ((u8 *)p_pc)
#define P_SHORT         ((s16 *)p_pc)
#define P_USHORT        ((u16 *)p_pc)
#define P_INT           ((s32 *)p_pc)
#define P_PTR           ((void **)p_pc)
#define P_CALL          ((PRGCALL **)p_pc)

#define P_CMD           P_UCHAR[0]
#define P_SIZE          P_UCHAR[1]

#define p_step()        (p_pc += P_SIZE)
#define p_push(x)       (*p_sp++ = (uintptr_t)(x))
#define p_pull()        ((void *)*--p_sp)

static uintptr_t p_stack[32];
static s16 p_state;
static int p_code;
static P_SCRIPT *p_pc;

static ARENA *p_arena = NULL;
static u16 p_sleep = 0;
static u16 p_freeze = 0;
static s16 p_scene = -1;
static uintptr_t *p_sp = p_stack;
static uintptr_t *p_fp = NULL;

static int p_cmp(CHAR cmp, int x)
{
	int result = 0;
	switch (cmp)
	{
	case P_CMP_AND:     result =  (p_code & x); break;
	case P_CMP_NAND:    result = !(p_code & x); break;
	case P_CMP_EQ:      result = p_code == x;   break;
	case P_CMP_NE:      result = p_code != x;   break;
	case P_CMP_LT:      result = p_code <  x;   break;
	case P_CMP_LE:      result = p_code <= x;   break;
	case P_CMP_GT:      result = p_code >  x;   break;
	case P_CMP_GE:      result = p_code >= x;   break;
	}
	return result;
}

static void p_cmd_execute(void)
{
	mem_push();
	mem_load_data(P_SHORT[1], P_PTR[1], P_PTR[2], MEM_ALLOC_L);
	p_push(p_pc + P_SIZE);
	p_push(p_fp);
	p_fp = p_sp;
	p_pc = segment_to_virtual(P_PTR[3]);
}

static void p_cmd_chain(void)
{
	void *pc = P_PTR[3];
	mem_pull();
	mem_push();
	mem_load_data(P_SHORT[1], P_PTR[1], P_PTR[2], MEM_ALLOC_L);
	p_sp = p_fp;
	p_pc = segment_to_virtual(pc);
}

static void p_cmd_exit(void)
{
	mem_pull();
	p_sp = p_fp;
	p_fp = p_pull();
	p_pc = p_pull();
}

static void p_cmd_sleep(void)
{
	p_state = 0;
	if (p_sleep == 0)
	{
		p_sleep = P_SHORT[1];
	}
	else if (--p_sleep == 0)
	{
		p_step();
		p_state = 1;
	}
}

static void p_cmd_freeze(void)
{
	p_state = -1;
	if (p_freeze == 0)
	{
		p_freeze = P_SHORT[1];
	}
	else if (--p_freeze == 0)
	{
		p_step();
		p_state = 1;
	}
}

static void p_cmd_jump(void)
{
	p_pc = segment_to_virtual(P_PTR[1]);
}

static void p_cmd_call(void)
{
	p_push(p_pc + P_SIZE);
	p_pc = segment_to_virtual(P_PTR[1]);
}

static void p_cmd_return(void)
{
	p_pc = p_pull();
}

static void p_cmd_for(void)
{
	p_push(p_pc + P_SIZE);
	p_push(P_SHORT[1]);
	p_step();
}

static void p_cmd_done(void)
{
	uintptr_t sp04 = p_sp[-1];
	if (sp04 == 0)
	{
		p_pc = (void *)p_sp[-2];
	}
	else if (--sp04 > 0)
	{
		p_sp[-1] = sp04;
		p_pc = (void *)p_sp[-2];
	}
	else
	{
		p_step();
		p_sp -= 2;
	}
}

static void p_cmd_repeat(void)
{
	p_push(p_pc + P_SIZE);
	p_push(0);
	p_step();
}

static void p_cmd_until(void)
{
	if (p_cmp(P_UCHAR[2], P_INT[1]))
	{
		p_step();
		p_sp -= 2;
	}
	else
	{
		p_pc = (void *)p_sp[-2];
	}
}

static void p_cmd_jump_if(void)
{
	if (p_cmp(P_UCHAR[2], P_INT[1]))
	{
		p_pc = segment_to_virtual(P_PTR[2]);
	}
	else
	{
		p_step();
	}
}

static void p_cmd_call_if(void)
{
	if (p_cmp(P_UCHAR[2], P_INT[1]))
	{
		p_push(p_pc + P_SIZE);
		p_pc = segment_to_virtual(P_PTR[2]);
	}
	else
	{
		p_step();
	}
}

static void p_cmd_if(void)
{
	if (!p_cmp(P_UCHAR[2], P_INT[1]))
	{
		do
		{
			p_step();
		}
		while (P_CMD == P_CMD_ELSE || P_CMD == P_CMD_ENDIF);
	}
	p_step();
}

static void p_cmd_else(void)
{
	do
	{
		p_step();
	}
	while (P_CMD == P_CMD_ENDIF);
	p_step();
}

static void p_cmd_endif(void)
{
	p_step();
}

static void p_cmd_callback(void)
{
	PRGCALL *callback = P_CALL[1];
	p_code = callback(P_SHORT[1], p_code);
	p_step();
}

static void p_cmd_process(void)
{
	PRGCALL *callback = P_CALL[1];
	p_code = callback(P_SHORT[1], p_code);
	if (p_code == 0)
	{
		p_state = 0;
	}
	else
	{
		p_state = 1;
		p_step();
	}
}

static void p_cmd_set(void)
{
	p_code = P_SHORT[1];
	p_step();
}

static void p_cmd_push(void)
{
	mem_push();
	p_step();
}

static void p_cmd_pull(void)
{
	mem_pull();
	p_step();
}

static void p_cmd_load_code(void)
{
	mem_load_code(P_PTR[1], P_PTR[2], P_PTR[3]);
	p_step();
}

static void p_cmd_load_data(void)
{
	mem_load_data(P_SHORT[1], P_PTR[1], P_PTR[2], MEM_ALLOC_L);
	p_step();
}

static void p_cmd_load_szp(void)
{
	mem_load_szp(P_SHORT[1], P_PTR[1], P_PTR[2]);
	p_step();
}

extern char _zimgSegmentStart[];
extern char _cimgSegmentStart[];

static void p_cmd_load_face(void)
{
	void *ptr;
	if ((ptr = mem_alloc(0xE1000, MEM_ALLOC_L)))
	{
		gdm_init(ptr, 0xE1000);
		face_gfx_8019C418(_zimgSegmentStart, 2*SCREEN_WD*SCREEN_HT);
		face_gfx_8019C418(_cimgSegmentStart, 2*SCREEN_WD*SCREEN_HT*3);
		gdm_setup();
		gdm_maketestdl(P_SHORT[1]);
	}
	else
	{
	}
	p_step();
}

static void p_cmd_load_txt(void)
{
	mem_load_txt(P_SHORT[1], P_PTR[1], P_PTR[2]);
	p_step();
}

static void p_cmd_stage_init(void)
{
	s_create_empty(NULL, &sobj_list);
	object_8029D1E8();
	scene_init();
	mem_push();
	p_step();
}

static void p_cmd_stage_exit(void)
{
	object_8029D1E8();
	scene_exit();
	scene_init();
	mem_pull();
	p_step();
}

static void p_cmd_stage_start(void)
{
	if (!p_arena)
	{
		p_arena = arena_init(mem_available()-sizeof(ARENA), MEM_ALLOC_L);
	}
	p_step();
}

static void p_cmd_stage_end(void)
{
	int i;
	arena_resize(p_arena, p_arena->used);
	p_arena = NULL;
	for (i = 0; i < 8; i++)
	{
		if (scene_data[i].map)
		{
			map_init();
			break;
		}
	}
	p_step();
}

static void p_cmd_scene_start(void)
{
	UCHAR i = P_UCHAR[2];
	S_SCRIPT *script = P_PTR[1];
	if (i < 8)
	{
		S_SCENE *shp = (S_SCENE *)s_process(p_arena, script);
		S_CAMERA *cam = (S_CAMERA *)shp->table[0];
		p_scene = i;
		shp->index = i;
		scene_table[i].shp = shp;
		if (cam)    scene_table[i].cam = (CAMERA *)cam->s.arg;
		else        scene_table[i].cam = NULL;
	}
	p_step();
}

static void p_cmd_scene_end(void)
{
	p_scene = -1;
	p_step();
}

static void p_cmd_shape_gfx(void)
{
	SHORT index = P_SHORT[1] & 0xFFF;
	SHORT layer = P_USHORT[1] >> 12;
	Gfx *gfx = P_PTR[1];
	if (index < 256)
	{
		shape_table[index] = &s_create_gfx(p_arena, NULL, layer, gfx)->s;
	}
	p_step();
}

static void p_cmd_shape_script(void)
{
	SHORT index = P_SHORT[1];
	S_SCRIPT *script = P_PTR[1];
	if (index < 256)
	{
		shape_table[index] = s_process(p_arena, script);
	}
	p_step();
}

static void p_cmd_shape_scale(void)
{
	union {int i; float f;} scale;
	SHORT index = P_SHORT[1] & 0xFFF;
	SHORT layer = P_USHORT[1] >> 12;
	Gfx *gfx = P_PTR[1];
	scale.i = P_INT[2];
	if (index < 256)
	{
		shape_table[index] =
			&s_create_scale(p_arena, NULL, layer, gfx, scale.f)->s.s;
	}
	p_step();
}

static void p_cmd_player(void)
{
	vecs_set(spawn_mario->pos, 0, 0, 0);
	vecs_set(spawn_mario->ang, 0, 0, 0);
	spawn_mario->group = -1;
	spawn_mario->scene = 0;
	spawn_mario->arg = P_INT[1];
	spawn_mario->script = P_PTR[2];
	spawn_mario->shape = shape_table[P_UCHAR[3]];
	spawn_mario->next = NULL;
	p_step();
}

static void p_cmd_object(void)
{
	UCHAR mask = 1 << (level_index-1);
	if (p_scene != -1)
	{
		if ((P_UCHAR[2] & mask) || P_UCHAR[2] == 0x1F)
		{
			USHORT shape = P_UCHAR[3];
			SPAWN *spawn = arena_alloc(p_arena, sizeof(SPAWN));
			spawn->pos[0] = P_SHORT[2];
			spawn->pos[1] = P_SHORT[3];
			spawn->pos[2] = P_SHORT[4];
			spawn->ang[0] = P_SHORT[5] * 0x8000/180;
			spawn->ang[1] = P_SHORT[6] * 0x8000/180;
			spawn->ang[2] = P_SHORT[7] * 0x8000/180;
			spawn->scene = p_scene;
			spawn->group = p_scene;
			spawn->arg = P_INT[4];
			spawn->script = P_PTR[5];
			spawn->shape = shape_table[shape];
			spawn->next = scene_table[p_scene].spawn;
			scene_table[p_scene].spawn = spawn;
		}
	}
	p_step();
}

static void p_cmd_port(void)
{
	if (p_scene != -1)
	{
		PORT *port = arena_alloc(p_arena, sizeof(PORT));
		port->index = P_UCHAR[2];
		port->stage = P_UCHAR[3] + P_UCHAR[6];
		port->scene = P_UCHAR[4];
		port->port = P_UCHAR[5];
		port->obj = NULL;
		port->next = scene_table[p_scene].port;
		scene_table[p_scene].port = port;
	}
	p_step();
}

static void p_cmd_connect(void)
{
	int i;
	CONNECT *connect;
	if (p_scene != -1)
	{
		if (!scene_table[p_scene].connect)
		{
			scene_table[p_scene].connect =
				arena_alloc(p_arena, sizeof(CONNECT)*4);
			for (i = 0; i < 4; i++)
			{
				scene_table[p_scene].connect[i].flag = FALSE;
			}
		}
		connect = &scene_table[p_scene].connect[P_UCHAR[2]];
		connect->flag = TRUE;
		connect->port = P_UCHAR[3];
		connect->offset[0] = P_SHORT[2];
		connect->offset[1] = P_SHORT[3];
		connect->offset[2] = P_SHORT[4];
	}
	p_step();
}

static void p_cmd_env(void)
{
	if (p_scene != -1)
	{
		scene_table[p_scene].env |= P_SHORT[1];
	}
	p_step();
}

static void p_cmd_bgport(void)
{
	int i;
	BGPORT *bgport;
	if (p_scene != -1)
	{
		if (!scene_table[p_scene].bgport)
		{
			scene_table[p_scene].bgport =
				arena_alloc(p_arena, sizeof(BGPORT)*45);
			for (i = 0; i < 45; i++)
			{
				scene_table[p_scene].bgport[i].flag = FALSE;
			}
		}
		bgport = &scene_table[p_scene].bgport[P_UCHAR[2]];
		bgport->flag = TRUE;
		bgport->stage = P_UCHAR[3] + P_UCHAR[6];
		bgport->scene = P_UCHAR[4];
		bgport->port = P_UCHAR[5];
	}
	p_step();
}

static void p_cmd_wind(void)
{
	WIND *wind;
	if (p_scene != -1)
	{
		if (!(wind = scene_table[p_scene].wind))
		{
			wind = scene_table[p_scene].wind =
				arena_alloc(p_arena, sizeof(WIND));
		}
		wind->_00 = P_SHORT[1];
		wind->_02 = P_SHORT[2];
		wind->_04 = P_SHORT[3];
		wind->_06 = P_SHORT[4];
		wind->_08 = P_SHORT[5];
	}
	p_step();
}

static void p_cmd_jet(void)
{
	JET *jet;
	int index = P_UCHAR[2];
	int flag = (save_flag_get() & 0xA0) != 0;
	if (
		(P_UCHAR[3] == 0) ||
		(P_UCHAR[3] == 1 && !flag) ||
		(P_UCHAR[3] == 2 && flag) ||
		(P_UCHAR[3] == 3 && level_index >= 2)
	)
	{
		if (p_scene != -1)
		{
			if (index < 2)
			{
				if (!(jet = scene_table[p_scene].jet[index]))
				{
					jet = arena_alloc(p_arena, sizeof(JET));
					scene_table[p_scene].jet[index] = jet;
				}
				vecs_set(jet->pos, P_SHORT[2], P_SHORT[3], P_SHORT[4]);
				jet->arg = P_SHORT[5];
			}
		}
	}
	p_step();
}

static void p_cmd_vi_black(void)
{
	osViBlack(P_UCHAR[2]);
	p_step();
}

static void p_cmd_vi_gamma(void)
{
	osViSetSpecialFeatures(!P_UCHAR[2] ? 2 : 1);
	p_step();
}

static void p_cmd_map(void)
{
	if (p_scene != -1)
	{
		scene_table[p_scene].map = segment_to_virtual(P_PTR[1]);
	}
	p_step();
}

static void p_cmd_area(void)
{
	if (p_scene != -1)
	{
		scene_table[p_scene].area = segment_to_virtual(P_PTR[1]);
	}
	p_step();
}

static void p_cmd_tag(void)
{
	if (p_scene != -1)
	{
		scene_table[p_scene].tag = segment_to_virtual(P_PTR[1]);
	}
	p_step();
}

static void p_cmd_scene_open(void)
{
	SHORT index = P_UCHAR[2];
	UNUSED void *sp18 = p_pc + 4;
	Na_SE_clear();
	scene_open(index);
	p_step();
}

static void p_cmd_scene_close(void)
{
	scene_close();
	p_step();
}

static void p_cmd_player_open(void)
{
	spawn_mario->scene = P_UCHAR[2];
	vecs_cpy(spawn_mario->pos, P_SHORT+3);
	vecs_set(spawn_mario->ang, 0, P_SHORT[2] * 0x8000/180, 0);
	p_step();
}

static void p_cmd_player_close(void)
{
	scene_player_close();
	p_step();
}

static void p_cmd_scene_update(void)
{
	scene_update();
	p_step();
}

static void p_cmd_wipe(void)
{
	if (scene)
	{
		scene_wipe(P_UCHAR[2], P_UCHAR[3], P_UCHAR[4], P_UCHAR[5], P_UCHAR[6]);
	}
	p_step();
}

static void p_cmd_50(void)
{
	p_step();
}

static void p_cmd_msg(void)
{
	if (p_scene != -1)
	{
		if (P_UCHAR[2] < 2) scene_table[p_scene].msg[P_UCHAR[2]] = P_UCHAR[3];
	}
	p_step();
}

static void p_cmd_bgm(void)
{
	if (p_scene != -1)
	{
		scene_table[p_scene].bgm_mode = P_SHORT[1];
		scene_table[p_scene].bgm = P_SHORT[2];
	}
	p_step();
}

static void p_cmd_bgm_play(void)
{
	bgm_play(0, P_SHORT[1], 0);
	p_step();
}

static void p_cmd_bgm_stop(void)
{
	aud_fadeout(P_SHORT[1]);
	p_step();
}

static void p_cmd_var(void)
{
	if (P_UCHAR[2] == 0)
	{
		switch (P_UCHAR[3])
		{
		case P_VAR_SAVE:    save_index = p_code; break;
		case P_VAR_COURSE:  course_index = p_code; break;
		case P_VAR_LEVEL:   level_index = p_code; break;
		case P_VAR_STAGE:   stage_index = p_code; break;
		case P_VAR_SCENE:   scene_index = p_code; break;
		}
	}
	else
	{
		switch (P_UCHAR[3])
		{
		case P_VAR_SAVE:    p_code = save_index; break;
		case P_VAR_COURSE:  p_code = course_index; break;
		case P_VAR_LEVEL:   p_code = level_index; break;
		case P_VAR_STAGE:   p_code = stage_index; break;
		case P_VAR_SCENE:   p_code = scene_index; break;
		}
	}
	p_step();
}

static void (*p_cmd_table[])(void) =
{
	p_cmd_execute,
	p_cmd_chain,
	p_cmd_exit,
	p_cmd_sleep,
	p_cmd_freeze,
	p_cmd_jump,
	p_cmd_call,
	p_cmd_return,
	p_cmd_for,
	p_cmd_done,
	p_cmd_repeat,
	p_cmd_until,
	p_cmd_jump_if,
	p_cmd_call_if,
	p_cmd_if,
	p_cmd_else,
	p_cmd_endif,
	p_cmd_callback,
	p_cmd_process,
	p_cmd_set,
	p_cmd_push,
	p_cmd_pull,
	p_cmd_load_code,
	p_cmd_load_data,
	p_cmd_load_szp,
	p_cmd_load_face,
	p_cmd_load_txt,
	p_cmd_stage_init,
	p_cmd_stage_exit,
	p_cmd_stage_start,
	p_cmd_stage_end,
	p_cmd_scene_start,
	p_cmd_scene_end,
	p_cmd_shape_gfx,
	p_cmd_shape_script,
	p_cmd_shape_scale,
	p_cmd_object,
	p_cmd_player,
	p_cmd_port,
	p_cmd_bgport,
	p_cmd_connect,
	p_cmd_scene_open,
	p_cmd_scene_close,
	p_cmd_player_open,
	p_cmd_player_close,
	p_cmd_scene_update,
	p_cmd_map,
	p_cmd_area,
	p_cmd_msg,
	p_cmd_env,
	p_cmd_50,
	p_cmd_wipe,
	p_cmd_vi_black,
	p_cmd_vi_gamma,
	p_cmd_bgm,
	p_cmd_bgm_play,
	p_cmd_bgm_stop,
	p_cmd_tag,
	p_cmd_wind,
	p_cmd_jet,
	p_cmd_var,
};

P_SCRIPT *p_execute(P_SCRIPT *pc)
{
	p_state = 1;
	p_pc = pc;
	while (p_state == 1) p_cmd_table[P_CMD]();
	time_gfxcpu(TIME_GFXCPU_ENDUPD);
	gfx_start();
	scene_draw();
	gfx_end();
	gfx_alloc(0);
	return p_pc;
}
