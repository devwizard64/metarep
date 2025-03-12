#include <sm64.h>

ACTOR player_actor[1];
SHAPE *shape_data[SHAPE_MAX];
SCENE scene_data[SCENE_MAX];
ACTOR *mario_actor = &player_actor[0];
SHAPE **shape_table = shape_data;
SCENE *scene_table = scene_data;
SCENE *scenep = NULL;
STAFF *staffp = NULL;
WIPE wipe;

static Vp *sn_viewport = NULL;
static Vp *sn_scissor = NULL;
static short wipe_delay = 0;
static u32 scene_fill = 0;
static u32 blank_fill = 0;
static u8 blank_r = 0;
static u8 blank_g = 0;
static u8 blank_b = 0;

short file_index = 1;
short course_index;
short level_index;
short stage_index = 1;
short scene_index;
short prev_course;

short msg_status;
short msg_result;

#define RGBA16(r, g, b, a) \
	(((r) >> 3) << 11 | ((g) >> 3) << 6 | ((b) >> 3) << 1 | ((a) >> 7))

void SnSetVp(Vp *viewport, Vp *scissor, UCHAR r, UCHAR g, UCHAR b)
{
	USHORT fill = RGBA16(r, g, b, 0xFF);
	scene_fill = fill << 16 | fill;
	sn_viewport = viewport;
	sn_scissor  = scissor;
}

static void SnSetBlank(UCHAR r, UCHAR g, UCHAR b)
{
	USHORT fill = RGBA16(r, g, b, 0xFF);
	blank_fill = fill << 16 | fill;
	blank_r = r;
	blank_g = g;
	blank_b = b;
}

#ifdef MULTILANG
static const char *no_controller[] =
{
	"NO CONTROLLER",
	"MANETTE DEBRANCHEE",
	"CONTROLLER FEHLT",
};

void SceneDemo(void)
{
	int lang = BuGetLang();
	if ((gfx_frame & 31) < 20)
	{
		if (!cont_bitpattern) dprintc(SCREEN_WD/2, 20, no_controller[lang]);
		else dprint(20, 20, "START");
	}
}
#else
void SceneDemo(void)
{
	if ((gfx_frame & 31) < 20)
	{
		if (!cont_bitpattern)
		{
			dprintc(SCREEN_WD/2, 20, "NO CONTROLLER");
		}
		else
		{
#if REVISION == 199605
			dprintc(SCREEN_WD/2, 20, "PRESS START");
#else
			dprintc(60, 20+18*1, "PRESS");
			dprintc(60, 20+18*0, "START");
#endif
		}
	}
}
#endif

#define PORT_MAX    20

extern OBJLANG obj_13000720[];
extern OBJLANG obj_1300075C[];
extern OBJLANG obj_13000780[];
extern OBJLANG obj_130007A0[];
extern OBJLANG obj_portdoor[];
extern OBJLANG obj_13002F60[];
extern OBJLANG obj_13002F64[];
extern OBJLANG obj_13002F68[];
extern OBJLANG obj_13002F6C[];
extern OBJLANG obj_13002F70[];
extern OBJLANG obj_13002F74[];
extern OBJLANG obj_13002F78[];
extern OBJLANG obj_13002F7C[];
extern OBJLANG obj_13002F80[];
extern OBJLANG obj_13002F84[];
extern OBJLANG obj_13002F88[];
extern OBJLANG obj_13002F8C[];
extern OBJLANG obj_13002F90[];
extern OBJLANG obj_13002F94[];
extern OBJLANG obj_13003E3C[];

static OBJLANG *port_script[PORT_MAX] =
{
	obj_portdoor,
	obj_13003E3C,
	obj_13000720,
	obj_13000780,
	obj_130007A0,
	obj_1300075C,
	obj_13002F60,
	obj_13002F64,
	obj_13002F68,
	obj_13002F6C,
	obj_13002F70,
	obj_13002F74,
	obj_13002F78,
	obj_13002F94,
	obj_13002F7C,
	obj_13002F80,
	obj_13002F88,
	obj_13002F84,
	obj_13002F8C,
	obj_13002F90,
};

static u8 port_type[PORT_MAX] =
{
	ENTER_DOOR,
	ENTER_02,
	ENTER_03,
	ENTER_03,
	ENTER_03,
	ENTER_04,
	ENTER_10,
	ENTER_12,
	ENTER_13,
	ENTER_14,
	ENTER_15,
	ENTER_16,
	ENTER_17,
	ENTER_11,
	ENTER_20,
	ENTER_21,
	ENTER_22,
	ENTER_23,
	ENTER_24,
	ENTER_25,
};

int SnGetPortType(OBJECT *obj)
{
	int i;
	OBJLANG *script = VirtualToSegment(SEG_OBJECT, obj->script);
	for (i = 0; i < PORT_MAX; i++)
	{
		if (port_script[i] == script) return port_type[i];
	}
	return 0;
}

PORT *SnGetPort(UCHAR index)
{
	PORT *port = NULL;
	for (port = scenep->port; port; port = port->next)
	{
		if (port->p.attr == index) break;
	}
	return port;
}

static PORT *ObjGetPort(OBJECT *obj)
{
	UCHAR index = ObjGetCode(obj);
	return SnGetPort(index);
}

static void SnInitPort(void)
{
	PORT *port;
	SHAPE *shape = sobj_list.child;
	do
	{
		OBJECT *obj = (OBJECT *)shape;
		if (obj->flag && SnGetPortType(obj))
		{
			if ((port = ObjGetPort(obj))) port->obj = obj;
		}
	}
	while ((shape = shape->next) != sobj_list.child);
}

void SceneInit(void)
{
	int i;
	scenep = NULL;
	wipe.active = FALSE;
	wipe.blank = FALSE;
	mario_actor->scene = -1;
	for (i = 0; i < SCENE_MAX; i++)
	{
		scene_data[i].index     = i;
		scene_data[i].flag      = 0;
		scene_data[i].env       = 0;
		scene_data[i].shp       = NULL;
		scene_data[i].map       = NULL;
		scene_data[i].area      = NULL;
		scene_data[i].tag       = NULL;
		scene_data[i].port      = NULL;
		scene_data[i].bgport    = NULL;
		scene_data[i].connect   = NULL;
		scene_data[i].actor     = NULL;
		scene_data[i].cam       = NULL;
		scene_data[i]._28       = NULL;
		scene_data[i].jet[0]    = NULL;
		scene_data[i].jet[1]    = NULL;
		scene_data[i].msg[0]    = 0xFF;
		scene_data[i].msg[1]    = 0xFF;
		scene_data[i].bgm_mode  = NA_MODE_DEFAULT;
		scene_data[i].bgm       = NA_BGM_NULL;
	}
}

void SceneExit(void)
{
	int i;
	if (scenep)
	{
		SSceneNotify(scenep->shp, SC_CLOSE);
		scenep = NULL;
		wipe.active = FALSE;
	}
	for (i = 0; i < SCENE_MAX; i++)
	{
		if (scene_data[i].shp)
		{
			SSceneNotify(scene_data[i].shp, SC_EXIT);
			scene_data[i].shp = NULL;
		}
	}
}

void SceneOpen(int index)
{
	if (!scenep && scene_data[index].shp)
	{
		scenep = &scene_data[index];
		scene_index = scenep->index;
		if (scenep->map)
		{
			MapLoad(index, scenep->map, scenep->area, scenep->tag);
		}
		if (scenep->actor) ObjectOpen(0, scenep->actor);
		SnInitPort();
		SSceneNotify(scenep->shp, SC_OPEN);
	}
}

void SceneClose(void)
{
	if (scenep)
	{
		ObjectClose(0, scenep->index);
		SSceneNotify(scenep->shp, SC_CLOSE);
		scenep->flag = 0;
		scenep = NULL;
		wipe.active = FALSE;
	}
}

void SnOpenPlayer(void)
{
	Na_SeClear();
	SceneOpen(mario_actor->scene);
	if (scenep->index == mario_actor->scene)
	{
		scenep->flag |= SN_ACTIVE;
		ObjectOpen(0, mario_actor);
	}
}

void SnClosePlayer(void)
{
	if (scenep && scenep->flag & SN_ACTIVE)
	{
		ObjectClose(0, mario_actor->group);
		scenep->flag &= ~SN_ACTIVE;
		if (!scenep->flag) SceneClose();
	}
}

void SceneSet(int index)
{
	int flag = scenep->flag;
	if (scene_index != index)
	{
		SceneClose();
		SceneOpen(index);
		scenep->flag = flag;
		mario_obj->o_effect = 0;
	}
	if (flag & SN_ACTIVE)
	{
		mario_obj->s.scene = index, mario_actor->scene = index;
	}
}

void SceneProc(void)
{
	draw_timer++;
	ObjectProc(0);
}

void SnWipe(SHORT type, SHORT frame, UCHAR r, UCHAR g, UCHAR b)
{
	wipe.active = TRUE;
	wipe.type   = type;
	wipe.frame  = frame;
	wipe.blank  = FALSE;
	if (WIPE_ISOUT(type))   SnSetBlank(r, g, b);
	else                    r = blank_r, g = blank_g, b = blank_b;
	if (type < WIPE_FADE_MAX)
	{
		wipe.data.fade.r = r;
		wipe.data.fade.g = g;
		wipe.data.fade.b = b;
	}
	else
	{
		wipe.data.window.r = r;
		wipe.data.window.g = g;
		wipe.data.window.b = b;
		wipe.data.window.sx = SCREEN_WD/2;
		wipe.data.window.sy = SCREEN_HT/2;
		wipe.data.window.ex = SCREEN_WD/2;
		wipe.data.window.ey = SCREEN_HT/2;
		wipe.data.window.rot = 0;
		if (WIPE_ISOUT(type))
		{
			wipe.data.window.ssize = SCREEN_WD;
			wipe.data.window.esize = type >= WIPE_UNKNOWN_OUT ? 16 : 0;
		}
		else
		{
			wipe.data.window.ssize = type >= WIPE_UNKNOWN_IN ? 16 : 0;
			wipe.data.window.esize = SCREEN_WD;
		}
	}
}

void SnWipeDelay(
	SHORT type, SHORT frame, UCHAR r, UCHAR g, UCHAR b, SHORT delay
)
{
	wipe_delay = delay;
	SnWipe(type, frame, r, g, b);
}

void SceneDraw(void)
{
	if (scenep && !wipe.blank)
	{
		static Vp vp =
		{{
			{4*(SCREEN_WD/2), 4*(SCREEN_HT/2), G_MAXZ/2, 0},
			{4*(SCREEN_WD/2), 4*(SCREEN_HT/2), G_MAXZ/2, 0},
		}};
		DrawScene(scenep->shp, sn_viewport, sn_scissor, scene_fill);
		gSPViewport(glistp++, K0_TO_PHYS(&vp));
		gDPSetScissor(
			glistp++, G_SC_NON_INTERLACE,
			0, BORDER_HT, SCREEN_WD, SCREEN_HT-BORDER_HT
		);
		HUD_Draw();
#if BORDER_HT > 0
		gDPSetScissor(glistp++, G_SC_NON_INTERLACE, 0, 0, SCREEN_WD, SCREEN_HT);
#endif
		dprintDraw();
		CaptionDraw();
		StaffDraw();
#if BORDER_HT > 0
		gDPSetScissor(
			glistp++, G_SC_NON_INTERLACE,
			0, BORDER_HT, SCREEN_WD, SCREEN_HT-BORDER_HT
		);
#endif
		if ((msg_status = MessageProc())) msg_result = msg_status;
		if (sn_scissor) GfxVpScissor(sn_scissor);
		else gDPSetScissor(
			glistp++, G_SC_NON_INTERLACE,
			0, BORDER_HT, SCREEN_WD, SCREEN_HT-BORDER_HT
		);
		if (wipe.active)
		{
			if (wipe_delay == 0)
			{
				wipe.active = !WipeDraw(0, wipe.type, wipe.frame, &wipe.data);
				if (!wipe.active)
				{
					if (WIPE_ISOUT(wipe.type))  wipe.blank = TRUE;
					else                        SnSetBlank(0, 0, 0);
				}
			}
			else
			{
				wipe_delay--;
			}
		}
	}
	else
	{
		dprintDraw();
		if (sn_scissor) GfxVpClear(sn_scissor, blank_fill);
		else            GfxClear(blank_fill);
	}
	sn_viewport = NULL;
	sn_scissor  = NULL;
}
