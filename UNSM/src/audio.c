#include <sm64.h>

#define BGM_NULL                ((u16)-1)

u8 aud_mute = 0;
u8 aud_lock = FALSE;

u16 bgm_stage   = BGM_NULL;
u16 bgm_shell   = BGM_NULL;
u16 bgm_special = BGM_NULL;

unsigned char aud_endless = FALSE;

u32 aud_8032D618[4] = {0};
s16 aud_output_table[] = {0, 3, 1};

NA_SE aud_env_se_data[36] =
{
	NA_SE1_00 + (0 << 16),
	NA_SE1_00 + (1 << 16),
	NA_SE1_00 + (2 << 16),
	NA_SE1_00 + (3 << 16),
	NA_SE1_00 + (4 << 16),
	NA_SE1_00 + (5 << 16),
	NA_SE1_00 + (6 << 16),
	NA_SE1_10,
	NA_SE1_12,
	NA_SE1_11,
	NA_SE1_14,
	NA_SE1_20,
	NA_SE_NULL,
	NA_SE4_0B,
	NA_SE4_0C,
	NA_SE4_0A,
	NA_SE4_00,
	NA_SE4_01,
	NA_SE4_02,
	NA_SE4_03,
	NA_SE4_04,
	NA_SE4_08,
	NA_SE4_05,
	NA_SE4_09,
	NA_SE6_00,
	NA_SE1_19,
	NA_SE6_02_80,
	NA_SE6_03,
	NA_SE6_10,
	NA_SE9_52,
	NA_SE8_50,
	NA_SE5_51,
	NA_SE4_08,
	NA_SE6_04_40,
	NA_SE6_04_80,
	NA_SE4_0D_0,
};
u32 aud_env_se_8033B0A0[36];

void aud_mute_reset(void)
{
	aud_mute = 0;
}

void aud_mute_start(int flag)
{
	switch (flag)
	{
	case 1: Na_pause(TRUE);         break;
	case 2: Na_SEQ_mute(0, 60, 40); break;
	}
	aud_mute |= flag;
}

void aud_mute_end(int flag)
{
	switch (flag)
	{
	case 1: Na_pause(FALSE);        break;
	case 2: Na_SEQ_unmute(0, 60);   break;
	}
	aud_mute &= ~flag;
}

void aud_se_lock(void)
{
	if (aud_lock == FALSE)
	{
		aud_lock = TRUE;
		Na_SE_lock();
	}
}

void aud_se_unlock(void)
{
	if (aud_lock == TRUE)
	{
		aud_lock = FALSE;
		Na_SE_unlock();
	}
}

void aud_output(USHORT type)
{
	if (type < 3) Na_output(aud_output_table[type]);
}

void aud_face_sfx(SHORT flag)
{
	if      (flag & (1 << 0)) Na_SE_fixed(NA_SE7_0A);
	else if (flag & (1 << 1)) Na_SE_fixed(NA_SE7_0B);
	else if (flag & (1 << 2)) Na_SE_fixed(NA_SE7_0C);
	else if (flag & (1 << 3)) Na_SE_fixed(NA_SE7_08);
	else if (flag & (1 << 4)) Na_SE_fixed(NA_SE7_08);
	else if (flag & (1 << 5)) Na_SE_fixed(NA_SE7_09);
	else if (flag & (1 << 6)) Na_SE_fixed(NA_SE7_06);
	else if (flag & (1 << 7)) Na_SE_fixed(NA_SE7_07);
	if      (flag & (1 << 8)) aud_env_se_play(20, NULL);
}

void aud_se_wave(void)
{
	static char flag = FALSE;
	if (wave_80361318 && wave_80361318->_07 == 2)
	{
		if (!flag) Na_SE_obj(NA_SE3_28, player_data[0].obj);
		flag = TRUE;
	}
	else
	{
		flag = FALSE;
	}
}

void bgm_endless(void)
{
	unsigned char flag = FALSE;
	if (stage_index == STAGE_INSIDE && scene_index == 2)
	{
		if (mario->star < 70)
		{
			if (mario->ground && mario->ground->area == 6)
			{
				if (mario->pos[2] < 2540) flag = TRUE;
			}
		}
	}
	if (aud_endless ^ flag)
	{
		aud_endless = flag;
		if (flag)   Na_BGM_push(NA_BGM_ENDLESS, 0x00, 0xFF, 1000);
		else        Na_BGM_pull(500);
	}
}

void bgm_play(USHORT mode, USHORT bgm, SHORT fadein)
{
	if (reset_timer == 0)
	{
		if (bgm != bgm_stage)
		{
			if (staff)  Na_mode(NA_MODE_STAFF);
			else        Na_mode(mode);
			if (game_8033B26E == 0 || bgm != NA_BGM_CASTLE)
			{
				Na_BGM_play(0, bgm, fadein);
				bgm_stage = bgm;
			}
		}
	}
}

void aud_fadeout(SHORT fadeout)
{
	Na_fadeout(fadeout);
	bgm_stage   = BGM_NULL;
	bgm_shell   = BGM_NULL;
	bgm_special = BGM_NULL;
}

void bgm_fadeout(SHORT fadeout)
{
	Na_SEQ_fadeout(0, fadeout);
	bgm_stage   = BGM_NULL;
	bgm_shell   = BGM_NULL;
	bgm_special = BGM_NULL;
}

void bgm_stage_play(USHORT bgm)
{
	Na_BGM_play(0, bgm, 0);
	bgm_stage = bgm;
}

void bgm_shell_play(void)
{
	Na_BGM_play(0, NA_BGM_SHELL, 0);
	bgm_shell = NA_BGM_SHELL;
}

void bgm_shell_stop(void)
{
	if (bgm_shell != BGM_NULL)
	{
		Na_BGM_stop(bgm_shell);
		bgm_shell = BGM_NULL;
	}
}

void bgm_special_play(USHORT bgm)
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

void aud_env_se_play(int se, VECF pos)
{
	Na_SE_play(aud_env_se_data[se], pos);
}

void aud_update(void)
{
	Na_update();
}

VECF aud_0;
OSMesgQueue aud_vi_mq;
OSMesg aud_vi_mbox;
SC_CLIENT sc_client_aud;

void aud_main(UNUSED void *arg)
{
	Na_load();
	Na_init();
	vecf_cpy(aud_0, vecf_0);
	osCreateMesgQueue(&aud_vi_mq, &aud_vi_mbox, 1);
	sc_client_init(1, &sc_client_aud, &aud_vi_mq, (OSMesg)0x200);
	for (;;)
	{
		OSMesg msg;
		osRecvMesg(&aud_vi_mq, &msg, OS_MESG_BLOCK);
		if (reset_timer < 25)
		{
			SC_TASK *task;
			time_audcpu();
			if ((task = Na_main())) sc_queue_audtask(task);
			time_audcpu();
		}
	}
}
