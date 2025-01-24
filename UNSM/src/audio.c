#include <sm64.h>

#define BGM_NULL                ((u16)-1)

static u8 aud_mute_flag = 0;
static u8 aud_lock_flag = FALSE;

static u16 bgm_stage   = BGM_NULL;
static u16 bgm_shell   = BGM_NULL;
static u16 bgm_special = BGM_NULL;

static unsigned char aud_endless = FALSE;

UNUSED static char aud_8032D618 = 0;
UNUSED static u32 aud_levelse_8033B0A0[36];
UNUSED static FVEC aud_8032D61C = {0};
static FVEC aud_0;

static OSMesgQueue aud_vi_mq;
static OSMesg aud_vi_mbox;
static SCCLIENT aud_client;

static s16 aud_modetab[] = {NA_OUTPUT_WIDE, NA_OUTPUT_MONO, NA_OUTPUT_PHONE};

static Na_Se aud_levelse_data[36] =
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

void AudResetMute(void)
{
	aud_mute_flag = 0;
}

void AudSetMute(int flag)
{
	switch (flag)
	{
	case AUD_PAUSE: Na_Pause(TRUE); break;
	case AUD_QUIET: Na_SeqMute(NA_HANDLE_BGM, 60, 40); break;
	}
	aud_mute_flag |= flag;
}

void AudClrMute(int flag)
{
	switch (flag)
	{
	case AUD_PAUSE: Na_Pause(FALSE); break;
	case AUD_QUIET: Na_SeqUnmute(NA_HANDLE_BGM, 60); break;
	}
	aud_mute_flag &= ~flag;
}

void AudLock(void)
{
	if (ISFALSE(aud_lock_flag))
	{
		aud_lock_flag = TRUE;
		Na_LockSe();
	}
}

void AudUnlock(void)
{
	if (ISTRUE(aud_lock_flag))
	{
		aud_lock_flag = FALSE;
		Na_UnlockSe();
	}
}

void AudSetMode(USHORT mode)
{
	if (mode < 3) Na_SetOutput(aud_modetab[mode]);
}

void AudPlayFaceSound(SHORT flag)
{
	if      (flag & (1 << 0)) Na_FixSePlay(NA_SE7_0A);
	else if (flag & (1 << 1)) Na_FixSePlay(NA_SE7_0B);
	else if (flag & (1 << 2)) Na_FixSePlay(NA_SE7_0C);
	else if (flag & (1 << 3)) Na_FixSePlay(NA_SE7_08);
	else if (flag & (1 << 4)) Na_FixSePlay(NA_SE7_08);
	else if (flag & (1 << 5)) Na_FixSePlay(NA_SE7_09);
	else if (flag & (1 << 6)) Na_FixSePlay(NA_SE7_06);
	else if (flag & (1 << 7)) Na_FixSePlay(NA_SE7_07);
	if      (flag & (1 << 8)) AudPlayLevelSe(20, NULL);
}

void AudProcWaveSound(void)
{
	static char flag = FALSE;
	if (wavep && wavep->state == WAVE_ENTER)
	{
		if (!flag) Na_ObjSePlay(NA_SE3_28, player_data[0].obj);
		flag = TRUE;
	}
	else
	{
		flag = FALSE;
	}
}

void AudProcEndlessMusic(void)
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
		if (flag)   Na_SeqPush(NA_BGM_ENDLESS, 0x00, 0xFF, 1000);
		else        Na_SeqPull(500);
	}
}

void AudPlayBGM(USHORT mode, USHORT bgm, SHORT fadein)
{
	if (!reset_timer)
	{
		if (bgm != bgm_stage)
		{
			if (staffp) Na_SetMode(NA_MODE_STAFF);
			else        Na_SetMode(mode);
			if (!(first_msg && bgm == NA_BGM_CASTLE))
			{
				Na_BgmPlay(NA_HANDLE_BGM, bgm, fadein);
				bgm_stage = bgm;
			}
		}
	}
}

void AudFadeout(SHORT fadeout)
{
	Na_Fadeout(fadeout);
	bgm_stage   = BGM_NULL;
	bgm_shell   = BGM_NULL;
	bgm_special = BGM_NULL;
}

void AudFadeoutBGM(SHORT fadeout)
{
	Na_SeqFadeout(NA_HANDLE_BGM, fadeout);
	bgm_stage   = BGM_NULL;
	bgm_shell   = BGM_NULL;
	bgm_special = BGM_NULL;
}

void AudPlayStageBGM(USHORT bgm)
{
	Na_BgmPlay(NA_HANDLE_BGM, bgm, 0);
	bgm_stage = bgm;
}

void AudPlayShellBGM(void)
{
	Na_BgmPlay(NA_HANDLE_BGM, NA_BGM_SHELL, 0);
	bgm_shell = NA_BGM_SHELL;
}

void AudStopShellBGM(void)
{
	if (bgm_shell != BGM_NULL)
	{
		Na_BgmStop(bgm_shell);
		bgm_shell = BGM_NULL;
	}
}

void AudPlaySpecialBGM(USHORT bgm)
{
	Na_BgmPlay(NA_HANDLE_BGM, bgm, 0);
	if (bgm_special != BGM_NULL && bgm_special != bgm)
	{
		Na_BgmStop(bgm_special);
	}
	bgm_special = bgm;
}

void AudFadeoutSpecialBGM(void)
{
	if (bgm_special != BGM_NULL)
	{
		Na_BgmFadeout(bgm_special, 600);
	}
}

void AudStopSpecialBGM(void)
{
	if (bgm_special != BGM_NULL)
	{
		Na_BgmStop(bgm_special);
		bgm_special = BGM_NULL;
	}
}

void AudPlayLevelSe(int se, FVEC pos)
{
	Na_SePlay(aud_levelse_data[se], pos);
}

void AudTick(void)
{
	Na_Tick();
}

void AudProc(UNUSED void *arg)
{
	Na_Load();
	Na_Init();
	FVecCpy(aud_0, fvec_0);
	osCreateMesgQueue(&aud_vi_mq, &aud_vi_mbox, 1);
	ScSetClient(SC_AUDCLIENT, &aud_client, &aud_vi_mq, (OSMesg)0x200);
	for (;;)
	{
		OSMesg msg;
		osRecvMesg(&aud_vi_mq, &msg, OS_MESG_BLOCK);
		if (reset_timer < 25)
		{
			SCTASK *task;
			TimeAudCPU();
			if ((task = Na_Main())) ScQueueAudTask(task);
			TimeAudCPU();
		}
	}
}
