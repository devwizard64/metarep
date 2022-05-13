#include <sm64/types.h>
#include <sm64/app.h>
#include <sm64/audio.h>
#include <sm64/mem.h>
#include <sm64/save.h>
#include <sm64/scene.h>
#include <sm64/dprint.h>
#include <sm64/audio/g.h>

char str_stage[64][16] =
{
    "",
    "",
    "",
    "TERESA OBAKE",
    "YYAMA1 % YSLD1",
    "SELECT ROOM",
    "HORROR DUNGEON",
    "SABAKU % PYRMD",
    "BATTLE FIELD",
    "YUKIYAMA2",
    "POOL KAI",
    "WTDG % TINBOTU",
    "BIG WORLD",
    "CLOCK TOWER",
    "RAINBOW CRUISE",
    "MAIN MAP",
    "EXT1 YOKO SCRL",
    "EXT7 HORI MINI",
    "EXT2 TIKA LAVA",
    "EXT9 SUISOU",
    "EXT3 HEAVEN",
    "FIREB1 % INVLC",
    "WATER LAND",
    "MOUNTAIN",
    "ENDING",
    "URANIWA",
    "EXT4 MINI SLID",
    "IN THE FALL",
    "EXT6 MARIO FLY",
    "KUPPA1",
    "EXT8 BLUE SKY",
    "",
    "KUPPA2",
    "KUPPA3",
    "",
    "DONKEY % SLID2",
    "",
    "",
};

static int title_demo(int code)
{
    static u16 timer = 0;
    demo = NULL;
    if (code == 0)
    {
        if (cont_1->held == 0 && cont_1->d == 0)
        {
            if (++timer == 800)
            {
                file_update(&file_demo, demo_index);
                if (++demo_index == file_demo.table->len) demo_index = 0;
                demo = (DEMO *)(file_demo.buf+4);
                code = file_demo.buf[0];
                save_index = 1;
                level_index = 1;
            }
        }
        else
        {
            timer = 0;
        }
    }
    return code;
}

static int title_debug(void)
{
    int flag = false;
    if (cont_1->down & A_BUTTON) stage_index +=  1, flag = true;
    if (cont_1->down & B_BUTTON) stage_index -=  1, flag = true;
    if (cont_1->down & U_JPAD)   stage_index -=  1, flag = true;
    if (cont_1->down & D_JPAD)   stage_index +=  1, flag = true;
    if (cont_1->down & L_JPAD)   stage_index -= 10, flag = true;
    if (cont_1->down & R_JPAD)   stage_index += 10, flag = true;
    if (flag) Na_SE_fixed(NA_SE3_2B);
    if (stage_index > 38) stage_index =  1;
    if (stage_index <  1) stage_index = 38;
    save_index = 4;
    level_index = 6;
    dprintc(SCREEN_WD/2, 80, "SELECT STAGE");
    dprintc(SCREEN_WD/2, 30, "PRESS START BUTTON");
    dprintf(40, 60, "%2d", stage_index);
    dprint(80, 60, str_stage[stage_index-1]);
    if (cont_1->down & START_BUTTON)
    {
        if (cont_1->held == (Z_TRIG | START_BUTTON | L_CBUTTONS | R_CBUTTONS))
        {
            debug_stage = false;
            return -1;
        }
        Na_SE_fixed(NA_SE7_1E);
        return stage_index;
    }
    return 0;
}

static int title_face(void)
{
    static s16 flag = true;
    int code = 0;
    if (flag == true)
    {
        if (video_frame <= 128) Na_SE_fixed(NA_SE2_32);
        else                    Na_SE_fixed(NA_SE2_33);
        flag = false;
    }
    scene_demo();
    if (cont_1->down & START_BUTTON)
    {
        Na_SE_fixed(NA_SE7_1E);
        code = 100 + debug_stage;
        flag = true;
    }
    return title_demo(code);
}

static int title_gameover(void)
{
    static s16 flag = true;
    int code = 0;
    if (flag == true)
    {
        Na_SE_fixed(NA_SE2_31);
        flag = false;
    }
    scene_demo();
    if (cont_1->down & START_BUTTON)
    {
        Na_SE_fixed(NA_SE7_1E);
        code = 100 + debug_stage;
        flag = true;
    }
    return title_demo(code);
}

static int title_logo(void)
{
    bgm_play(NA_MODE_DEFAULT, NA_BGM_NULL, 0);
    Na_SE_fixed(NA_SE7_14);
    return 1;
}

int p_title_main(SHORT arg, int code)
{
    int result;
    switch (arg)
    {
        case 0:     result = title_logo();      break;
        case 1:     result = title_face();      break;
        case 2:     result = title_gameover();  break;
        case 3:     result = title_debug();     break;
#ifndef sgi
        default:    result = code;              break;
#endif
    }
    return result;
}
