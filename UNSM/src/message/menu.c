extern unsigned char *coursename[];
extern unsigned char *levelname[];

/******************************************************************************/
/* Pause menu                                                                 */
/******************************************************************************/

#define PAUSELINE       15

#define PAUSEJMARIX     14
#define PAUSEJSTOPX     124
#define PAUSEJUGEMUY    2
#define PAUSENORMALY    -13

#ifdef JAPANESE
#define PAUSENREALX     4
#define PAUSENSTOPX     116
#define PAUSECOURSEWD   30
#define PAUSECRSX       0
#define PAUSECRSY       -4
#define PAUSECAMX       0
#define PAUSECAMY       0
#endif
#ifdef ENGLISH
#define PAUSENREALX     3
#define PAUSENSTOPX     119
#define PAUSECOURSEWD   37
#define PAUSECRSX       -4
#define PAUSECRSY       -2
#define PAUSECAMX       0
#define PAUSECAMY       2
#endif

char redcoin_count;
static s8 camera_cursor = 1;
char pausemenu_level = 1;

void PauseMenu_Init(void)
{
	redcoin_count = 0;
}

static void PauseMenu_InitCourse(void)
{
	if (camera_80288624(0) == 1)    camera_cursor = 1;
	else                            camera_cursor = 2;
}

static void MenuDrawBack(void)
{
	GfxTranslate(GFX_PUSH, 0, SCREEN_HT, 0);
	GfxScale(GFX_NOPUSH, 2.6F, 3.4F, 1);
	gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, 110);
	gSPDisplayList(glistp++, gfx_message_box);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
}

extern Gfx gfx_redcoin_0[];
extern Gfx gfx_redcoin_1[];
extern Gfx gfx_redcoin_2[];
extern Gfx gfx_redcoin_3[];

static void PauseMenu_PutRedCoin(SHORT x, SHORT y)
{
	unsigned int frame = gfx_frame;
	GfxTranslate(GFX_PUSH, x, y, 0);
	GfxScale(GFX_NOPUSH, 0.2F, 0.2F, 1);
	gDPSetRenderMode(glistp++, G_RM_TEX_EDGE, G_RM_TEX_EDGE2);
	switch (frame & 6)
	{
	case 0: gSPDisplayList(glistp++, gfx_redcoin_0); break;
	case 2: gSPDisplayList(glistp++, gfx_redcoin_1); break;
	case 4: gSPDisplayList(glistp++, gfx_redcoin_2); break;
	case 6: gSPDisplayList(glistp++, gfx_redcoin_3); break;
	}
	gDPSetRenderMode(glistp++, G_RM_AA_ZB_OPA_SURF, G_RM_AA_ZB_OPA_SURF2);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
}

static void PauseMenu_DrawRedCoin(void)
{
	CHAR i;
	for (i = 0; i < redcoin_count; i++) PauseMenu_PutRedCoin(290 - 20*i, 16);
}

static void PauseMenu_DrawCourse(void)
{
	STATIC unsigned char str_course[] = {STR_COURSE};
	STATIC unsigned char str_my_score[] = {STR_MY_SCORE};
	STATIC unsigned char str_star[] = {CH_STAR,CH_NUL};
	STATIC unsigned char str_nostar[] = {CH_NOSTAR,CH_NUL};
	unsigned char buf[4];
	unsigned char **crstab = SegmentToVirtual(coursename);
	unsigned char *crsname;
	unsigned char **lvltab = SegmentToVirtual(levelname);
	unsigned char *lvlname;
	UCHAR course = course_index-1;
	UCHAR star = BuGetStar(course_index-1);
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
	if (course < COURSE_EXT-1)
	{
		PrintCoin(1, file_index-1, course, 178, 103);
		PrintStar(file_index-1, course, 118, 103);
	}
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
	if (course < COURSE_EXT-1 && BuStarCount(course))
	{
		PrintLg(62, 121, str_my_score);
	}
	crsname = SegmentToVirtual(crstab[course]);
	if (course < COURSE_EXT-1)
	{
		PrintLg(63, 157, str_course);
		IntToStr(course_index, buf);
		PrintLg(63+PAUSECOURSEWD, 157, buf);
		lvlname = SegmentToVirtual(
			lvltab[6*(course_index-1) + (pausemenu_level-1)]
		);
		if (star & (1 << (pausemenu_level-1)))  PrintLg(98, 140, str_star);
		else                                    PrintLg(98, 140, str_nostar);
		PrintLg(116, 140, lvlname);
#if REVISION >= 199609
		PrintLg(117, 157, &crsname[3]);
	}
	else
	{
		PrintLg(94, 157, &crsname[3]);
	}
#else
	}
	PrintLg(117, 157, &crsname[3]);
#endif
	gSPDisplayList(glistp++, gfx_lgfont_end);
}

static void PauseMenu_ProcCamera(SHORT x, SHORT y, s8 *cursor, SHORT space)
{
	STATIC unsigned char str_lakitu_mario[] = {STR_LAKITU_MARIO};
	STATIC unsigned char str_lakitu_stop[] = {STR_LAKITU_STOP};
	STATIC unsigned char str_normal_up_close[] = {STR_NORMAL_UP_CLOSE};
	STATIC unsigned char str_normal_fixed[] = {STR_NORMAL_FIXED};
	CursorProc(CURSOR_H, cursor, 1, 2);
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
	PrintLg(x+PAUSEJMARIX, y+PAUSEJUGEMUY, str_lakitu_mario);
	PrintLg(x+PAUSENREALX, y+PAUSENORMALY, str_normal_up_close);
	PrintLg(x+PAUSEJSTOPX, y+PAUSEJUGEMUY, str_lakitu_stop);
	PrintLg(x+PAUSENSTOPX, y+PAUSENORMALY, str_normal_fixed);
	gSPDisplayList(glistp++, gfx_lgfont_end);
	GfxTranslate(GFX_PUSH, x+PAUSECAMX+space*(*cursor-1), y+PAUSECAMY, 0);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
	gSPDisplayList(glistp++, gfx_message_cursor);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	switch (*cursor)
	{
	case 1: camera_80288624(1); break;
	case 2: camera_80288624(2); break;
	}
}

static void PauseMenu_ProcCourse(SHORT x, SHORT y, s8 *cursor, SHORT space)
{
	STATIC unsigned char str_continue[] = {STR_CONTINUE};
	STATIC unsigned char str_exit_course[] = {STR_EXIT_COURSE};
	STATIC unsigned char str_set_camera_angle_with_r[] =
		{STR_SET_CAMERA_ANGLE_WITH_R};
	CursorProc(CURSOR_V, cursor, 1, 3);
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
	PrintLg(x+10, y-2-PAUSELINE*0, str_continue);
	PrintLg(x+10, y-2-PAUSELINE*1, str_exit_course);
#if REVISION >= 199609
	if (*cursor != 3)
	{
		PrintLg(x+10, y-2-31, str_set_camera_angle_with_r);
#else
	if (*cursor != 3) \
	{ \
		PrintLg(x+10, y-2-31, str_set_camera_angle_with_r);
#endif
		gSPDisplayList(glistp++, gfx_lgfont_end);
		GfxTranslate(GFX_PUSH, x+PAUSECRSX, y+PAUSECRSY-space*(*cursor-1), 0);
		gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
		gSPDisplayList(glistp++, gfx_message_cursor);
		gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	}
	if (*cursor == 3) PauseMenu_ProcCamera(x-42, y-42, &camera_cursor, 110);
}

static void PauseMenu_DrawScoreBox(SHORT x, SHORT y)
{
	GfxTranslate(GFX_PUSH, x-78, y-32, 0);
	GfxScale(GFX_NOPUSH, 1.2F, 0.8F, 1);
	gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, 105);
	gSPDisplayList(glistp++, gfx_message_box);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	GfxTranslate(GFX_PUSH, x+6, y-28, 0);
	GfxRotate(GFX_NOPUSH, 90, 0, 0, 1);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
	gSPDisplayList(glistp++, gfx_message_cursor);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	GfxTranslate(GFX_PUSH, x-9, y-101, 0);
	GfxRotate(GFX_NOPUSH, 270, 0, 0, 1);
	gSPDisplayList(glistp++, gfx_message_cursor);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
}

static void PauseMenu_InitSelect(void)
{
	UCHAR cursor;
	if (bu_course == COURSE_NULL)
	{
		cursor = 0;
	}
	else
	{
		cursor = bu_course-1;
		if (cursor >= 15) cursor = 15;
	}
	msg_cursor = cursor;
}

static void PauseMenu_DrawSelect(void)
{
	STATIC unsigned char str_pause[] = {STR_PAUSE};
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
	Print16(FONT_GLB, 123, 81, str_pause);
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
}

static void PauseMenu_DrawStar(SHORT x, SHORT y, SHORT file, SHORT course)
{
	SHORT n = 0;
	unsigned char buf[30];
	STATIC unsigned char str_star[] = {CH_STAR,CH_NUL};
	UCHAR star = BuFileGetStar(file, course);
	USHORT count = BuFileStarCount(file, course);
	USHORT i = 0;
	if (star & 0100)
	{
		count--;
		PrintLg(x+89, y-5, str_star);
	}
	while (n != count)
	{
		if (star & (1 << i))
		{
			buf[2*i] = CH_STAR;
			n++;
		}
		else
		{
			buf[2*i] = CH_NOSTAR;
		}
		buf[2*i+1] = CH_SPACE;
		i++;
	}
	if (count == i && count != 6)
	{
		buf[2*i+0] = CH_NOSTAR;
		buf[2*i+1] = CH_SPACE;
		i++;
	}
	buf[2*i] = CH_NUL;
	PrintLg(x+14, y+13, buf);
}

static void PauseMenu_ProcScore(SHORT x, SHORT y)
{
	unsigned char **crstab = SegmentToVirtual(coursename);
	STATIC unsigned char str_coin_x[] = {CH_COIN,CH_CROSS,CH_NUL};
	unsigned char *crsname;
	unsigned char buf[8];
	SHORT prev = msg_cursor;
	CursorProc(CURSOR_V, &msg_cursor, COURSE_MIN-1-1, COURSE_EXT-1+1);
	if (msg_cursor == COURSE_EXT-1+1) msg_cursor = COURSE_MIN-1;
	if (msg_cursor == COURSE_MIN-1-1) msg_cursor = COURSE_EXT-1;
	if (msg_cursor != COURSE_EXT-1)
	{
		while (!BuStarCount(msg_cursor))
		{
			if (msg_cursor >= prev) msg_cursor++;
			else                    msg_cursor--;
			if (msg_cursor == COURSE_EXT-1 || msg_cursor == COURSE_MIN-1-1)
			{
				msg_cursor = COURSE_EXT-1;
				break;
			}
		}
	}
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
	if (msg_cursor < COURSE_EXT-1)
	{
		crsname = SegmentToVirtual(crstab[msg_cursor]);
		PauseMenu_DrawStar(x, y, file_index-1, msg_cursor);
		PrintLg(x+34, y-5, str_coin_x);
		IntToStr(BuGetCoin(msg_cursor), buf);
		PrintLg(x+34+20, y-5, buf);
	}
	else
	{
		STATIC unsigned char str_star_x[] = {CH_STAR,CH_CROSS,CH_NUL};
		crsname = SegmentToVirtual(crstab[25]);
		PrintLg(x+40, y+13, str_star_x);
		IntToStr(BuStarRange(15, 24), buf);
		PrintLg(x+40+20, y+13, buf);
	}
	PrintLg(x-9, y+30, crsname);
	gSPDisplayList(glistp++, gfx_lgfont_end);
}

static SHORT PauseMenu_Proc(void)
{
	SHORT result;
	switch (msg_state)
	{
	case 0:
		msg_cursor = 1;
		msg_alpha = 0;
		GmFreeze(-1, NULL);
		Na_FixSePlay(NA_SE7_02);
		if (course_index >= COURSE_MIN && course_index <= COURSE_MAX)
		{
			PauseMenu_InitCourse();
			msg_state = 1;
		}
		else
		{
			PauseMenu_InitSelect();
			msg_state = 2;
		}
		break;
	case 1:
		MenuDrawBack();
		PauseMenu_DrawCourse();
		PauseMenu_DrawRedCoin();
		if (player_data[0].state & PF_QUIT)
		{
			PauseMenu_ProcCourse(99, 93, &msg_cursor, PAUSELINE);
		}
		if (contp->down & A_BUTTON || contp->down & START_BUTTON)
		{
			GmFreeze(0, NULL);
			Na_FixSePlay(NA_SE7_03);
			msg_state = 0;
			menu_code = -1;
			if (msg_cursor == 2)    result = msg_cursor;
			else                    result = 1;
			return result;
		}
		break;
	case 2:
		MenuDrawBack();
		PauseMenu_DrawSelect();
		PauseMenu_DrawScoreBox(160, 143);
		PauseMenu_ProcScore(104, 60);
		if (contp->down & A_BUTTON || contp->down & START_BUTTON)
		{
			GmFreeze(0, NULL);
			Na_FixSePlay(NA_SE7_03);
			menu_code = -1;
			msg_state = 0;
			return 1;
		}
		break;
	}
	if (msg_alpha < 250) msg_alpha += 25;
	return 0;
}

/******************************************************************************/
/* Save menu                                                                  */
/******************************************************************************/

static char savedemo_end = FALSE;
static int savedemo_timer = 0;
static int savedemo_coin = 0;
char savemenu_code = 0;

#define SAVELINE        20

#define SAVEDEMOX       118
#define SAVEDEMOY       103
#define SAVECOURSEX     63
#define SAVECOURSEY     167
#define SAVECLEARX      69
#define SAVECLEARY      132
#define SAVECATCHX      74
#define SAVECATCHY      147

#ifdef JAPANESE
#if REVISION >= 199609
#define HISCOREX        118
#define CONGRATX        70
#else
#define HISCOREX        112
#define CONGRATX        60
#endif
#define HISCOREY        48
#define CONGRATY        67
#define SAVEOPTX        10
#define SAVEOPTY        2
#define SAVECOURSEWD    30
#define CrsStrWd(str)   124
#define LvlStrWd(str)   134
#endif
#ifdef ENGLISH
#define HISCOREX        109
#define CONGRATX        70
#define HISCOREY        36
#define CONGRATY        67
#define SAVEOPTX        12
#define SAVEOPTY        0
#define SAVECOURSEWD    39
#define CrsStrWd(str)   StrWidth(str)
#define LvlStrWd(str)   StrWidth(str)
#endif

static void SaveMenu_DrawBanner(CHAR code)
{
	STATIC unsigned char str_hi_score[] = {STR_HI_SCORE};
	STATIC unsigned char str_congratulations[] = {STR_CONGRATULATIONS};
	UCHAR color = 200 + 50*SIN(msg_theta);
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, color, color, color, 0xFF);
	if (code == 0)  Print16(FONT_GLB, HISCOREX, HISCOREY, str_hi_score);
	else            Print16(FONT_GLB, CONGRATX, CONGRATY, str_congratulations);
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
}

static void SaveMenu_ProcDemo(SHORT x, SHORT y)
{
	unsigned char buf[4];
	STATIC unsigned char str16_coin[] = {CH16_COIN,CH_NUL};
	STATIC unsigned char str16_cross[] = {CH16_CROSS,CH_NUL};
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 0xFF);
	Print16(FONT_GLB, x+ 0, y, str16_coin);
	Print16(FONT_GLB, x+16, y, str16_cross);
	IntToStr(savedemo_coin, buf);
	Print16(FONT_GLB, x+32, y, buf);
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
	if (savedemo_coin >= hud.coin)
	{
		savedemo_end = TRUE;
		savedemo_coin = hud.coin;
		if (bu_myscore) SaveMenu_DrawBanner(0);
	}
	else
	{
		if (savedemo_timer & 1 || hud.coin > 70)
		{
			savedemo_coin++;
			Na_FixSePlay(NA_SE7_15);
			if (
				savedemo_coin == 50 ||
				savedemo_coin == 100 ||
				savedemo_coin == 150
			)
			{
				Na_FixSePlay(NA_SE3_58);
				mario->life++;
			}
		}
		if (savedemo_coin == hud.coin && bu_myscore) Na_FixSePlay(NA_SE7_22);
	}
}

static void SaveMenu_ProcStar(int code, UCHAR star)
{
	if (savedemo_coin == hud.coin && !(bu_star & star))
	{
		if (!savemenu_code)
		{
			Na_HiScore();
			savemenu_code = code;
		}
	}
}

static void SaveMenu_Draw(void)
{
#if REVISION < 199609
	STATIC unsigned char str16_star[] = {CH16_STAR,CH_NUL};
#endif
#ifdef JAPANESE
	STATIC unsigned char str_course[] = {STR_COURSE};
	STATIC unsigned char str_catch[] = {STR_CATCH};
	STATIC unsigned char str_clear[] = {STR_CLEAR};
#endif
#ifdef ENGLISH
	STATIC unsigned char str_course[] = {STR_COURSE};
	UNUSED STATIC unsigned char str_catch[] = {STR_CATCH};
	STATIC unsigned char str_clear[] = {STR_CLEAR};
#endif
#if REVISION >= 199609
	STATIC unsigned char str16_star[] = {CH16_STAR,CH_NUL};
#endif
	unsigned char **lvltab = SegmentToVirtual(levelname);
	unsigned char **crstab = SegmentToVirtual(coursename);
	unsigned char *name;
	unsigned char buf[4];
	if (bu_course < COURSE_EXT)
	{
		SaveMenu_ProcDemo(SAVEDEMOX, SAVEDEMOY);
		SaveMenu_ProcStar(1, 1 << (bu_level-1));
		if (bu_level == 7)  name = SegmentToVirtual(lvltab[91]);
		else                name = SegmentToVirtual(
			lvltab[6*(bu_course-1)+(bu_level-1)]
		);
		gSPDisplayList(glistp++, gfx_lgfont_begin);
		IntToStr(bu_course, buf);
		gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, msg_alpha);
		PrintLg(SAVECOURSEX+2, SAVECOURSEY-2, str_course);
		PrintLg(SAVECOURSEX+SAVECOURSEWD+2, SAVECOURSEY-2, buf);
		gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
		PrintLg(SAVECOURSEX, SAVECOURSEY, str_course);
		PrintLg(SAVECOURSEX+SAVECOURSEWD, SAVECOURSEY, buf);
		gSPDisplayList(glistp++, gfx_lgfont_end);
	}
	else if (bu_course == COURSE_BITDW || bu_course == COURSE_BITFS)
	{
		name = SegmentToVirtual(crstab[bu_course-1]);
		gSPDisplayList(glistp++, gfx_lgfont_begin);
		gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, msg_alpha);
		PrintLg(SAVECLEARX+2, SAVECLEARY-2, name);
		PrintLg(SAVECLEARX+CrsStrWd(name)+10+2, SAVECLEARY-2, str_clear);
		gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
		PrintLg(SAVECLEARX, SAVECLEARY, name);
		PrintLg(SAVECLEARX+CrsStrWd(name)+10, SAVECLEARY, str_clear);
		gSPDisplayList(glistp++, gfx_lgfont_end);
		SaveMenu_DrawBanner(1);
		SaveMenu_ProcDemo(SAVEDEMOX, SAVEDEMOY+8);
		SaveMenu_ProcStar(2, 0);
		return;
	}
	else
	{
		name = SegmentToVirtual(lvltab[90]);
		SaveMenu_ProcDemo(SAVEDEMOX, SAVEDEMOY);
		SaveMenu_ProcStar(1, 1 << (bu_level-1));
	}
	gSPDisplayList(glistp++, gfx_print_1cyc_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
	Print16(FONT_GLB, 55, 77, str16_star);
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, msg_alpha);
	PrintLg(SAVECATCHX+2, SAVECATCHY-2, name);
#ifdef JAPANESE
	PrintLg(SAVECATCHX+LvlStrWd(name)+10+2, SAVECATCHY-2, str_catch);
#endif
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
	PrintLg(SAVECATCHX, SAVECATCHY, name);
#ifdef JAPANESE
	PrintLg(SAVECATCHX+LvlStrWd(name)+10, SAVECATCHY, str_catch);
#endif
	gSPDisplayList(glistp++, gfx_lgfont_end);
}

static void SaveMenu_ProcSave(SHORT x, SHORT y, s8 *cursor, SHORT space)
{
	STATIC unsigned char str_save_and_continue[] = {STR_SAVE_AND_CONTINUE};
	STATIC unsigned char str_save_and_quit[] = {STR_SAVE_AND_QUIT};
	STATIC unsigned char str_continue_dont_save[] = {STR_CONTINUE_DONT_SAVE};
	CursorProc(CURSOR_V, cursor, 1, 3);
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
	PrintLg(x+SAVEOPTX, y+SAVEOPTY-SAVELINE*0, str_save_and_continue);
	PrintLg(x+SAVEOPTX, y+SAVEOPTY-SAVELINE*1, str_save_and_quit);
	PrintLg(x+SAVEOPTX, y+SAVEOPTY-SAVELINE*2, str_continue_dont_save);
	gSPDisplayList(glistp++, gfx_lgfont_end);
	GfxTranslate(GFX_PUSH, x, y - space*(*cursor-1), 0);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, msg_alpha);
	gSPDisplayList(glistp++, gfx_message_cursor);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
}

static SHORT SaveMenu_Proc(void)
{
	SHORT result;
	switch (msg_state)
	{
	case 0:
		SaveMenu_Draw();
		if (savedemo_timer > 100 && ISTRUE(savedemo_end))
		{
			msg_state = 1;
			GmFreeze(-1, NULL);
			msg_alpha = 0;
			msg_cursor = 1;
		}
		break;
	case 1:
		MenuDrawBack();
		SaveMenu_Draw();
		SaveMenu_ProcSave(100, 86, &msg_cursor, SAVELINE);
		if (savedemo_timer > 110 && (
			contp->down & A_BUTTON || contp->down & START_BUTTON
		))
		{
			GmFreeze(0, NULL);
			Na_FixSePlay(NA_SE7_1E);
			msg_state = 0;
			menu_code = -1;
			result = msg_cursor;
			savedemo_timer = 0;
			savedemo_coin = 0;
			savedemo_end = FALSE;
			savemenu_code = 0;
			return result;
		}
		break;
	}
	if (msg_alpha < 250) msg_alpha += 25;
	savedemo_timer++;
	return 0;
}
