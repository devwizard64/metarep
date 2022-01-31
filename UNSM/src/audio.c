#include <sm64/types.h>
#include <sm64/main.h>
#include <sm64/audio.h>
#include <sm64/game.h>
#include <sm64/scene.h>
#include <sm64/time.h>
#include <sm64/ripple.h>
#include <sm64/math.h>
#include <sm64/map.h>
#include <sm64/audio/c.h>
#include <sm64/audio/g.h>

#define BGM_NULL                0xFFFF

u8 audio_mute = 0;
u8 audio_lock = false;

u16 bgm_stage   = BGM_NULL;
u16 bgm_shell   = BGM_NULL;
u16 bgm_special = BGM_NULL;

u8 audio_endless = false;

u32 audio_8032D618[4] = {0};
s16 audio_output_table[] = {0, 3, 1};

u32 audio_env_se_table[] =
{
    0x14000001, 0x14010001, 0x14020001, 0x14030001,
    0x14040001, 0x14050001, 0x14060001, 0x14100001,
    0x14128001, 0x14110001, 0x14140001, 0x14200001,
    0x00000000, 0x400B0001, 0x400C0001, 0x400A0001,
    0x40000001, 0x40010001, 0x40020001, 0x41030001,
    0x40040001, 0x40080001, 0x40050001, 0x40090001,
    0x60000001, 0x1D192001, 0x60028001, 0x60034001,
    0x60104001, 0x90524001, 0x80504001, 0x50514001,
    0x40080001, 0x60044001, 0x60048001, 0x400D0001,
};
u32 audio_env_se_8033B0A0[lenof(audio_env_se_table)];

void audio_mute_reset(void)
{
    audio_mute = 0;
}

void audio_mute_start(uint flag)
{
    switch (flag)
    {
        case 1: Na_pause(true);         break;
        case 2: Na_SEQ_mute(0, 60, 40); break;
    }
    audio_mute |= flag;
}

void audio_mute_end(uint flag)
{
    switch (flag)
    {
        case 1: Na_pause(false);        break;
        case 2: Na_SEQ_unmute(0, 60);   break;
    }
    audio_mute &= ~flag;
}

void audio_se_lock(void)
{
    if (audio_lock == false)
    {
        audio_lock = true;
        Na_IO_lock(2, 0x037A);
    }
}

void audio_se_unlock(void)
{
    if (audio_lock == true)
    {
        audio_lock = false;
        Na_IO_unlock(2, 0x37A);
    }
}

void audio_output(u16 type)
{
    if (type < 3) Na_output(audio_output_table[type]);
}

void audio_face_sfx(s16 flag)
{
    if      (flag & (1 << 0)) Na_SE_fixed(NA_SE7_0A);
    else if (flag & (1 << 1)) Na_SE_fixed(NA_SE7_0B);
    else if (flag & (1 << 2)) Na_SE_fixed(NA_SE7_0C);
    else if (flag & (1 << 3)) Na_SE_fixed(NA_SE7_08);
    else if (flag & (1 << 4)) Na_SE_fixed(NA_SE7_08);
    else if (flag & (1 << 5)) Na_SE_fixed(NA_SE7_09);
    else if (flag & (1 << 6)) Na_SE_fixed(NA_SE7_06);
    else if (flag & (1 << 7)) Na_SE_fixed(NA_SE7_07);
    if      (flag & (1 << 8)) audio_env_se_play(20, NULL);
}

void audio_se_ripple(void)
{
    static s8 flag = false;
    if (ripple_80361318 != NULL && ripple_80361318->_07 == 2)
    {
        if (!flag) Na_SE_obj(NA_SE3_28, player_table[0].obj);
        flag = true;
    }
    else
    {
        flag = false;
    }
}

void bgm_endless(void)
{
    u8 flag = false;
    if (stage_index == 6 && scene_index == 2)
    {
        if (mario->star < 70)
        {
            if (mario->ground != NULL && mario->ground->area == 6)
            {
                if (mario->pos[2] < 2540) flag = true;
            }
        }
    }
    if (audio_endless ^ flag)
    {
        audio_endless = flag;
        if (flag)   Na_BGM_fadeto_start(24, 0x00, 0xFF, 1000);
        else        Na_BGM_fadeto_end(500);
    }
}

void bgm_play(u16 mode, u16 bgm, s16 fadein)
{
    if (reset_timer == 0)
    {
        if (bgm != bgm_stage)
        {
            if (staff != NULL)  Na_mode(7);
            else                Na_mode(mode);
            if (game_8033B26E == 0 || bgm != 4)
            {
                Na_BGM_play(0, bgm, fadein);
                bgm_stage = bgm;
            }
        }
    }
}

void audio_fadeout(s16 fadeout)
{
    Na_fadeout(fadeout);
    bgm_stage   = BGM_NULL;
    bgm_shell   = BGM_NULL;
    bgm_special = BGM_NULL;
}

void bgm_fadeout(s16 fadeout)
{
    Na_SEQ_fadeout(0, fadeout);
    bgm_stage   = BGM_NULL;
    bgm_shell   = BGM_NULL;
    bgm_special = BGM_NULL;
}

void bgm_stage_play(u16 bgm)
{
    Na_BGM_play(0, bgm, 0);
    bgm_stage = bgm;
}

void bgm_shell_play(void)
{
    Na_BGM_play(0, 0x400 | 0x80 | 14, 0);
    bgm_shell = 0x400 | 0x80 | 14;
}

void bgm_shell_stop(void)
{
    if (bgm_shell != BGM_NULL)
    {
        Na_BGM_stop(bgm_shell);
        bgm_shell = BGM_NULL;
    }
}

void bgm_special_play(u16 bgm)
{
    Na_BGM_play(0, bgm, 0);
    if (bgm_special != BGM_NULL && bgm_special != bgm)
    {
        Na_BGM_stop(bgm_special);
    }
    bgm_special = bgm;
}

void bgm_special_fadeout(void)
{
    if (bgm_special != BGM_NULL)
    {
        Na_BGM_fadeout(bgm_special, 600);
    }
}

void bgm_special_stop(void)
{
    if (bgm_special != BGM_NULL)
    {
        Na_BGM_stop(bgm_special);
        bgm_special = BGM_NULL;
    }
}

void audio_env_se_play(int se, vecf pos)
{
    Na_SE_play(audio_env_se_table[se], pos);
}

void audio_update(void)
{
    Na_update();
}

vecf audio_0;
OSMesgQueue mq_audio;
OSMesg msg_audio;
SC_CLIENT sc_client_audio;

void audio_main(unused void *arg)
{
    Na_load();
    Na_init();
    vecf_cpy(audio_0, vecf_0);
    osCreateMesgQueue(&mq_audio, &msg_audio, 1);
    sc_client_init(1, &sc_client_audio, &mq_audio, (OSMesg)0x200);
    while (true)
    {
        OSMesg msg;
        osRecvMesg(&mq_audio, &msg, OS_MESG_BLOCK);
        if (reset_timer < 25)
        {
            SC_TASK *task;
            time_8027E490();
            if ((task = Na_main()) != NULL) sc_queue_audtask(task);
            time_8027E490();
        }
    }
}
