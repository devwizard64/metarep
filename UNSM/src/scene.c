#include <sm64/types.h>
#include <sm64/segment.h>
#include <sm64/app.h>
#include <sm64/pl_demo.h>
#include <sm64/memory.h>
#include <sm64/scene.h>
#include <sm64/draw.h>
#include <sm64/object.h>
#include <sm64/wipe.h>
#include <sm64/dprint.h>
#include <sm64/message.h>
#include <sm64/hud.h>
#include <sm64/shape.h>
#include <sm64/s_script.h>
#include <sm64/audio/g.h>

SPAWN spawn_player[1];
SHAPE *shape_data[SHAPE_LEN];
SCENE scene_data[SCENE_LEN];
WIPE wipe;
s16 course_index;
s16 level_index;
s16 scene_index;
s16 course_prev;
s16 msg_code;
s16 msg_latch;

SPAWN *spawn_mario = &spawn_player[0];
SHAPE **shape_table = shape_data;
SCENE *scene_table = scene_data;
SCENE *scene = NULL;
STAFF *staff = NULL;
Vp *scene_viewport = NULL;
Vp *scene_scissor = NULL;
s16 wipe_delay = 0;
u32 scene_fill = 0;
u32 blank_fill = 0;
u8 blank_r = 0;
u8 blank_g = 0;
u8 blank_b = 0;
s16 save_index = 1;
s16 stage_index = 1;

#define RGBA16(r, g, b, a)  \
    (((r) >> 3) << 11 | ((g) >> 3) << 6 | ((b) >> 3) << 1 | ((a) >> 7))

void scene_vp_set(Vp *viewport, Vp *scissor, UCHAR r, UCHAR g, UCHAR b)
{
    USHORT fill = RGBA16(r, g, b, 0xFF);
    scene_fill = fill << 16 | fill;
    scene_viewport = viewport;
    scene_scissor  = scissor;
}

static void scene_blank_set(UCHAR r, UCHAR g, UCHAR b)
{
    USHORT fill = RGBA16(r, g, b, 0xFF);
    blank_fill = fill << 16 | fill;
    blank_r = r;
    blank_g = g;
    blank_b = b;
}

void scene_demo(void)
{
    if ((video_frame & 0x1F) < 20)
    {
        if (input_flag == 0)
        {
            dprintc(SCREEN_WD/2, 20, "NO CONTROLLER");
        }
        else
        {
            dprintc(60, 20+18*1, "PRESS");
            dprintc(60, 20+18*0, "START");
        }
    }
}

extern O_SCRIPT o_13000720[];
extern O_SCRIPT o_1300075C[];
extern O_SCRIPT o_13000780[];
extern O_SCRIPT o_130007A0[];
extern O_SCRIPT o_linkdoor[];
extern O_SCRIPT o_13002F60[];
extern O_SCRIPT o_13002F64[];
extern O_SCRIPT o_13002F68[];
extern O_SCRIPT o_13002F6C[];
extern O_SCRIPT o_13002F70[];
extern O_SCRIPT o_13002F74[];
extern O_SCRIPT o_13002F78[];
extern O_SCRIPT o_13002F7C[];
extern O_SCRIPT o_13002F80[];
extern O_SCRIPT o_13002F84[];
extern O_SCRIPT o_13002F88[];
extern O_SCRIPT o_13002F8C[];
extern O_SCRIPT o_13002F90[];
extern O_SCRIPT o_13002F94[];
extern O_SCRIPT o_13003E3C[];

#define LINK_LEN    20

int obj_link_code(OBJECT *obj)
{
    static const O_SCRIPT *link_script[LINK_LEN] =
    {
        o_linkdoor,
        o_13003E3C,
        o_13000720,
        o_13000780,
        o_130007A0,
        o_1300075C,
        o_13002F60,
        o_13002F64,
        o_13002F68,
        o_13002F6C,
        o_13002F70,
        o_13002F74,
        o_13002F78,
        o_13002F94,
        o_13002F7C,
        o_13002F80,
        o_13002F88,
        o_13002F84,
        o_13002F8C,
        o_13002F90,
    };
    static u8 link_code[LINK_LEN] =
    {
        1,
        2,
        3,
        3,
        3,
        4,
        16,
        18,
        19,
        20,
        21,
        22,
        23,
        17,
        32,
        33,
        34,
        35,
        36,
        37,
    };
    int i;
    const S_SCRIPT *script = virtual_to_segment(SEG_DATA_OBJECT, obj->script);
    for (i = 0; i < LINK_LEN; i++)
    {
        if (link_script[i] == script) return link_code[i];
    }
    return 0;
}

LINK *link_get(UCHAR index)
{
    LINK *link = NULL;
    for (link = scene->link; link != NULL; link = link->next)
    {
        if (link->index == index) break;
    }
    return link;
}

static LINK *obj_link_get(OBJECT *obj)
{
    UCHAR index = obj_code_get(obj);
    return link_get(index);
}

static void link_init(void)
{
    LINK *link;
    SHAPE *shape = s_script_8038BD88.child;
    do
    {
        OBJECT *obj = (OBJECT *)shape;
        if (obj->flag != 0 && obj_link_code(obj) != 0)
        {
            if ((link = obj_link_get(obj)) != NULL) link->obj = obj;
        }
    }
    while ((shape = shape->next) != s_script_8038BD88.child);
}

void scene_init(void)
{
    int i;
    scene = NULL;
    wipe.active = FALSE;
    wipe.blank = FALSE;
    spawn_mario->scene = -1;
    for (i = 0; i < SCENE_LEN; i++)
    {
        scene_data[i].index     = i;
        scene_data[i].flag      = 0;
        scene_data[i].env       = 0;
        scene_data[i].s         = NULL;
        scene_data[i].map       = NULL;
        scene_data[i].area      = NULL;
        scene_data[i].obj       = NULL;
        scene_data[i].link      = NULL;
        scene_data[i].linkbg    = NULL;
        scene_data[i].connect   = NULL;
        scene_data[i].spawn     = NULL;
        scene_data[i].cam       = NULL;
        scene_data[i].wind      = NULL;
        scene_data[i].jet[0]    = NULL;
        scene_data[i].jet[1]    = NULL;
        scene_data[i].msg[0]    = 0xFF;
        scene_data[i].msg[1]    = 0xFF;
        scene_data[i].bgm_mode  = NA_MODE_DEFAULT;
        scene_data[i].bgm       = NA_BGM_NULL;
    }
}

void scene_exit(void)
{
    int i;
    if (scene != NULL)
    {
        shape_8037C360(scene->s, S_CODE_CLOSE);
        scene = NULL;
        wipe.active = FALSE;
    }
    for (i = 0; i < SCENE_LEN; i++)
    {
        if (scene_data[i].s != NULL)
        {
            shape_8037C360(scene_data[i].s, S_CODE_EXIT);
            scene_data[i].s = NULL;
        }
    }
}

void scene_open(int index)
{
    if (scene == NULL && scene_data[index].s != NULL)
    {
        scene = &scene_data[index];
        scene_index = scene->index;
        if (scene->map != NULL) map_data_803833B8(
            index, scene->map, scene->area, scene->obj
        );
        if (scene->spawn != NULL) object_8029CFB0(0, scene->spawn);
        link_init();
        shape_8037C360(scene->s, S_CODE_OPEN);
    }
}

void scene_close(void)
{
    if (scene != NULL)
    {
        object_8029CEDC(0, scene->index);
        shape_8037C360(scene->s, S_CODE_CLOSE);
        scene->flag = 0;
        scene = NULL;
        wipe.active = FALSE;
    }
}

void scene_player_open(void)
{
    Na_SE_clear();
    scene_open(spawn_mario->scene);
    if (scene->index == spawn_mario->scene)
    {
        scene->flag |= SCENE_FLAG_01;
        object_8029CFB0(0, spawn_mario);
    }
}

void scene_player_close(void)
{
    if (scene != NULL && (scene->flag & SCENE_FLAG_01))
    {
        object_8029CEDC(0, spawn_mario->group);
        scene->flag &= ~SCENE_FLAG_01;
        if (scene->flag == 0) scene_close();
    }
}

void scene_set(int index)
{
    int flag = scene->flag;
    if (scene_index != index)
    {
        scene_close();
        scene_open(index);
        scene->flag = flag;
        obj_mario->o_particle = 0;
    }
    if (flag & SCENE_FLAG_01)
    {
        obj_mario->list.s.scene = index, spawn_mario->scene = index;
    }
}

void scene_update(void)
{
    draw_timer++;
    object_8029D690(0);
}

void scene_wipe(SHORT type, SHORT frame, UCHAR r, UCHAR g, UCHAR b)
{
    wipe.active = TRUE;
    wipe.type   = type;
    wipe.frame  = frame;
    wipe.blank  = FALSE;
    if (type & 1)   scene_blank_set(r, g, b);
    else            r = blank_r, g = blank_g, b = blank_b;
    if (type < 8)
    {
        wipe.arg.fade.r = r;
        wipe.arg.fade.g = g;
        wipe.arg.fade.b = b;
    }
    else
    {
        wipe.arg.window.r = r;
        wipe.arg.window.g = g;
        wipe.arg.window.b = b;
        wipe.arg.window.s_x = SCREEN_WD/2;
        wipe.arg.window.s_y = SCREEN_HT/2;
        wipe.arg.window.e_x = SCREEN_WD/2;
        wipe.arg.window.e_y = SCREEN_HT/2;
        wipe.arg.window.rot_vel = 0;
        if (type & 1)
        {
            wipe.arg.window.s_size = SCREEN_WD;
            wipe.arg.window.e_size = type >= 15 ? 16 : 0;
        }
        else
        {
            wipe.arg.window.s_size = type >= 14 ? 16 : 0;
            wipe.arg.window.e_size = SCREEN_WD;
        }
    }
}

void scene_wipe_delay(
    SHORT type, SHORT frame, UCHAR r, UCHAR g, UCHAR b, SHORT delay
)
{
    wipe_delay = delay;
    scene_wipe(type, frame, r, g, b);
}

void scene_draw(void)
{
    if (scene != NULL && !wipe.blank)
    {
        static Vp vp =
        {{
            {4*(SCREEN_WD/2), 4*(SCREEN_HT/2), G_MAXZ/2, 0},
            {4*(SCREEN_WD/2), 4*(SCREEN_HT/2), G_MAXZ/2, 0},
        }};
        draw_scene(scene->s, scene_viewport, scene_scissor, scene_fill);
        gSPViewport(video_gfx++, K0_TO_PHYS(&vp));
        gDPSetScissor(
            video_gfx++, G_SC_NON_INTERLACE,
            0, BORDER_HT, SCREEN_WD, SCREEN_HT-BORDER_HT
        );
        hud_draw();
#if BORDER_HT > 0
        gDPSetScissor(
            video_gfx++, G_SC_NON_INTERLACE, 0, 0, SCREEN_WD, SCREEN_HT
        );
#endif
        dprint_draw();
        message_802DAB58();
        pl_demo_80256E88();
#if BORDER_HT > 0
        gDPSetScissor(
            video_gfx++, G_SC_NON_INTERLACE,
            0, BORDER_HT, SCREEN_WD, SCREEN_HT-BORDER_HT
        );
#endif
        if ((msg_code = message_802DDCA4()) != 0) msg_latch = msg_code;
        if (scene_scissor != NULL) video_vp_scissor(scene_scissor);
        else gDPSetScissor(
            video_gfx++, G_SC_NON_INTERLACE,
            0, BORDER_HT, SCREEN_WD, SCREEN_HT-BORDER_HT
        );
        if (wipe.active)
        {
            if (wipe_delay == 0)
            {
                wipe.active =
                    !wipe_802CCBE8(0, wipe.type, wipe.frame, &wipe.arg);
                if (!wipe.active)
                {
                    if (wipe.type & 1)  wipe.blank = TRUE;
                    else                scene_blank_set(0, 0, 0);
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
        dprint_draw();
        if (scene_scissor != NULL)  video_vp_clear(scene_scissor, blank_fill);
        else                        video_clear(blank_fill);
    }
    scene_viewport = NULL;
    scene_scissor  = NULL;
}
