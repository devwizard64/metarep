#include <sm64/types.h>
#include <sm64/memory.h>
#include <sm64/shape.h>

extern Gfx gfx_wipe_start[];

extern Gfx gfx_logo_s[];
extern Gfx gfx_logo_symbol[];
extern f32 logo_scale_a[];
extern f32 logo_scale_b[];

extern Gfx gfx_title_bg_start[];
extern Gfx gfx_title_bg_vtx[];
extern Gfx gfx_title_bg_0[];
extern Gfx gfx_title_bg_1[];
extern Gfx gfx_title_bg_2[];
extern Gfx gfx_title_bg_3[];
extern Gfx gfx_title_bg_end[];
extern u16 *txt_title_bg_mario[];
extern u16 *txt_title_bg_gameover[];

s32 title_bg_timer;
s32 title_bg_count;
s16 title_bg_frame;
s32 title_bg_alpha;

void *s_logo_shape(int code, SHAPE *shape, void *data)
{
    SHAPE_CALLBACK *s = (SHAPE_CALLBACK *)shape;
    Gfx *gfx = NULL;
    Gfx *g = NULL;
    Mtx *mtx;
    f32 *a = segment_to_virtual(logo_scale_a);
    f32 *b = segment_to_virtual(logo_scale_b);
    if (code != S_CODE_DRAW)
    {
        title_bg_frame = 0;
    }
    else if (code == S_CODE_DRAW)
    {
        float x;
        float y;
        float z;
        shape_layer_set(s, S_LAYER_OPA_SURF);
        mtx = gfx_alloc(sizeof(Mtx));
        g = gfx = gfx_alloc(sizeof(Gfx)*4);
        if (title_bg_frame >= 0 && title_bg_frame < 0+20)
        {
            x = a[3*(title_bg_frame-0)+0];
            y = a[3*(title_bg_frame-0)+1];
            z = a[3*(title_bg_frame-0)+2];
        }
        else if (title_bg_frame >= 0+20 && title_bg_frame < 75)
        {
            x = 1;
            y = 1;
            z = 1;
        }
        else if (title_bg_frame >= 75 && title_bg_frame < 75+16)
        {
            x = b[3*(title_bg_frame-75)+0];
            y = b[3*(title_bg_frame-75)+1];
            z = b[3*(title_bg_frame-75)+2];
        }
        else
        {
            x = 0;
            y = 0;
            z = 0;
        }
        guScale(mtx, x, y, z);
        gSPMatrix(g++, mtx, G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_PUSH);
        gSPDisplayList(g++, gfx_logo_s);
        gSPPopMatrix(g++, G_MTX_MODELVIEW);
        gSPEndDisplayList(g);
        title_bg_frame++;
    }
    return gfx;
}

void *s_logo_symbol(int code, SHAPE *shape, void *data)
{
    SHAPE_CALLBACK *s = (SHAPE_CALLBACK *)shape;
    Gfx *gfx = NULL;
    Gfx *g = NULL;
    if (code != S_CODE_DRAW)
    {
        title_bg_alpha = 0;
    }
    else if (code == S_CODE_DRAW)
    {
        g = gfx = gfx_alloc(sizeof(Gfx)*5);
        gSPDisplayList(g++, gfx_wipe_start);
        gDPSetEnvColor(g++, 0xFF, 0xFF, 0xFF, title_bg_alpha);
        if (title_bg_alpha == 0xFF)
        {
            if (0) {}
            shape_layer_set(s, S_LAYER_OPA_SURF);
            gDPSetRenderMode(g++, G_RM_AA_OPA_SURF, G_RM_AA_OPA_SURF2);
        }
        else
        {
            shape_layer_set(s, S_LAYER_XLU_SURF);
            gDPSetRenderMode(g++, G_RM_AA_XLU_SURF, G_RM_AA_XLU_SURF2);
            if (0) {}
        }
        gSPDisplayList(g++, gfx_logo_symbol);
        gSPEndDisplayList(g);
        if (title_bg_frame > 18)
        {
            title_bg_alpha += 26;
            if (title_bg_alpha > 0xFF) title_bg_alpha = 0xFF;
        }
    }
    return gfx;
}

static Gfx *title_bg_tile(int index, s8 *bg)
{
    static Gfx *gfx_title_bg[] =
    {
        gfx_title_bg_0,
        gfx_title_bg_1,
        gfx_title_bg_2,
        gfx_title_bg_3,
    };
    static f32 x[] = {0, 80, 160, 240, 0, 80, 160, 240, 0, 80, 160, 240};
    static f32 y[] = {160, 160, 160, 160, 80, 80, 80, 80, 0, 0, 0, 0};
    static u16 **txt_title_bg[] =
    {
        txt_title_bg_mario,
        txt_title_bg_gameover,
    };
    Mtx *mtx = gfx_alloc(sizeof(Mtx));
    Gfx *gfx = gfx_alloc(sizeof(Gfx)*(2 + 4*(7+1) + 2));
    Gfx *g = gfx;
    u16 **txt = segment_to_virtual(txt_title_bg[bg[index]]);
    int i;
    guTranslate(mtx, x[index], y[index], 0);
    gSPMatrix(g++, mtx, G_MTX_MODELVIEW|G_MTX_LOAD|G_MTX_PUSH);
    gSPDisplayList(g++, gfx_title_bg_vtx);
    for (i = 0; i < 4; i++)
    {
        gDPLoadTextureBlock(
            g++, txt[i], G_IM_FMT_RGBA, G_IM_SIZ_16b, 80, 20, 0,
            G_TX_CLAMP, G_TX_CLAMP, 7, 6, G_TX_NOLOD, G_TX_NOLOD
        );
        gSPDisplayList(g++, gfx_title_bg[i]);
    }
    gSPPopMatrix(g++, G_MTX_MODELVIEW);
    gSPEndDisplayList(g);
    return gfx;
}

void *s_title_bg(int code, SHAPE *shape, void *data)
{
    static s8 bg_mario[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    static s8 *bg_table[] = {bg_mario};
    SHAPE_CALLBACK *s = (SHAPE_CALLBACK *)shape;
    int index = s->arg & 0xFF;
    s8 *bg = bg_table[index];
    Gfx *gfx = NULL;
    Gfx *g = NULL;
    int i;
    if (code == S_CODE_DRAW)
    {
        g = gfx = gfx_alloc(sizeof(Gfx)*(2 + 4*3 + 2));
        shape_layer_set(s, S_LAYER_OPA_SURF);
        gSPDisplayList(g++, gfx_wipe_start);
        gSPDisplayList(g++, gfx_title_bg_start);
        for (i = 0; i < 4*3; i++)
        {
            gSPDisplayList(g++, title_bg_tile(i, bg));
        }
        gSPDisplayList(g++, gfx_title_bg_end);
        gSPEndDisplayList(g);
    }
    return gfx;
}

void *s_gameover_bg(int code, SHAPE *shape, void *data)
{
    static s8 bg[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
    static s8 flip[] = {0, 1, 2, 3, 7, 11, 10, 9, 8, 4, 5, 6};
    SHAPE_CALLBACK *s = (SHAPE_CALLBACK *)shape;
    Gfx *gfx = NULL;
    Gfx *g = NULL;
    int i;
    if (code != S_CODE_DRAW)
    {
        int i;
        title_bg_timer = 0;
        title_bg_count = -2;
        for (i = 0; i < 4*3; i++) bg[i] = 1;
    }
    else
    {
        g = gfx = gfx_alloc(sizeof(Gfx)*(2 + 4*3 + 2));
        if (title_bg_count == -2)
        {
            if (title_bg_timer == 180)
            {
                title_bg_count++;
                title_bg_timer = 0;
            }
        }
        else if (title_bg_count != lenof(flip)-1 && !(title_bg_timer & 1))
        {
            title_bg_count++;
            bg[flip[title_bg_count]] = 0;
        }
        if (title_bg_count != lenof(flip)-1) title_bg_timer++;
        shape_layer_set(s, S_LAYER_OPA_SURF);
        gSPDisplayList(g++, gfx_wipe_start);
        gSPDisplayList(g++, gfx_title_bg_start);
        for (i = 0; i < 4*3; i++)
        {
            gSPDisplayList(g++, title_bg_tile(i, bg));
        }
        gSPDisplayList(g++, gfx_title_bg_end);
        gSPEndDisplayList(g);
    }
    return gfx;
}
