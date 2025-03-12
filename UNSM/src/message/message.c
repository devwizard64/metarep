void CursorProc(CHAR code, s8 *cursor, CHAR min, CHAR max)
{
	UCHAR flag = 0;
	if (code == CURSOR_V)
	{
		if (contp->stick_y > +60) flag += 1;
		if (contp->stick_y < -60) flag += 2;
	}
	else if (code == CURSOR_H)
	{
		if (contp->stick_x > +60) flag += 2;
		if (contp->stick_x < -60) flag += 1;
	}
	if (((flag^cursor_status) & flag) == 2)
	{
		if (*cursor == max)
		{
			*cursor = max;
		}
		else
		{
			Na_FixSePlay(NA_SE7_00);
			(*cursor)++;
		}
	}
	if (((flag^cursor_status) & flag) == 1)
	{
		if (*cursor == min)
		{
		}
		else
		{
			Na_FixSePlay(NA_SE7_00);
			(*cursor)--;
		}
	}
	if (cursor_timer == 10)
	{
		cursor_timer = 8;
		cursor_status = 0;
	}
	else
	{
		cursor_timer++;
		cursor_status = flag;
	}
	if (!(flag & 3)) cursor_timer = 0;
}

#ifdef JAPANESE
SHORT StrCenterX(SHORT x, const unsigned char *str, float kerning)
{
	SHORT i = 0;
	float width = 0;
	float space = 0;
	while (str[i] != CH_NUL)
	{
		if (str[i] == CH_SPACE) space += 1.0;
		else if (str[i] != CH_DAKUTEN && str[i] != CH_HANDAKUTEN) width += 1.0;
		i++;
	}
	return (float)x - kerning*(width/2.0) - (kerning/2.0)*(space/2.0);
}
#endif

#ifdef ENGLISH
SHORT StrCenterX(SHORT x, const unsigned char *str, UNUSED float kerning)
{
	SHORT i = 0;
	float width = 0;
	while (str[i] != CH_NUL)
	{
		width += kerningtab[str[i]];
		i++;
	}
	return x - (SHORT)(width/2.0);
}

SHORT StrWidth(const unsigned char *str)
{
	SHORT i = 0;
	SHORT width = 0;
	while (str[i] != CH_NUL)
	{
		width += kerningtab[str[i]];
		i++;
	}
	return width;
}
#endif

void PrintCoin(int code, CHAR file, CHAR course, SHORT x, SHORT y)
{
	unsigned char buf[4];
	SHORT coin;
	static unsigned char str16_coin[] = {CH16_COIN,CH_NUL};
	static unsigned char str16_cross[] = {CH16_CROSS,CH_NUL};
	if (code == 0)  coin = BuGetHiScoreCoin(course);
	else            coin = BuFileGetCoin(file, course);
	if (coin)
	{
		Print16(FONT_GLB, x, y, str16_coin);
		Print16(FONT_GLB, x+16, y, str16_cross);
		IntToStr(coin, buf);
		Print16(FONT_GLB, x+32, y, buf);
	}
}

void PrintStar(CHAR file, CHAR course, SHORT x, SHORT y)
{
	unsigned char buf[4];
	SHORT star;
	STATIC unsigned char str16_star[] = {CH16_STAR,CH_NUL};
	STATIC unsigned char str16_cross[] = {CH16_CROSS,CH_NUL};
	star = BuFileStarCount(file, course);
	if (star)
	{
		Print16(FONT_GLB, x, y, str16_star);
		Print16(FONT_GLB, x+16, y, str16_cross);
		IntToStr(star, buf);
		Print16(FONT_GLB, x+32, y, buf);
	}
}

void IntToStr(int value, unsigned char *str)
{
	int c, d, u;
	CHAR i = 0;
	if (value > 999) {str[0] = CH_0; str[1] = CH_NUL; return;}
	c = value / 100;
	d = (value - 100*c) / 10;
	u = value - 100*c - 10*d;
	if (     c) str[i] = CH_0+c, i++;
	if (d || c) str[i] = CH_0+d, i++;
	str[i] = CH_0+u, i++;
	str[i] = CH_NUL;
}

SHORT MsgGet(void)
{
	return msg_code;
}

void MsgOpen(SHORT code)
{
	if (msg_code == MSG_NULL)
	{
		msg_code = code;
		msg_type = 0;
	}
}

void MsgOpenInt(SHORT code, int value)
{
	if (msg_code == MSG_NULL)
	{
		msg_code = code;
		msg_value = value;
		msg_type = 0;
	}
}

void MsgOpenSignpost(SHORT code)
{
	if (msg_code == MSG_NULL)
	{
		msg_code = code;
		msg_type = 1;
	}
}

void MsgOpenPrompt(SHORT code)
{
	if (msg_code == MSG_NULL)
	{
		msg_code = code;
		msg_type = 0;
		msg_cursor_flag = TRUE;
	}
}

void MsgClose(void)
{
	GmFreeze(0, NULL);
	if (msg_type == 1) camera_8028BD34(2);
	msg_scale = 19;
	msg_angle = 90;
	msg_state = 0;
	msg_code = MSG_NULL;
	msg_index = 0;
	msg_cursor_flag = FALSE;
	msg_next = 0;
	msg_answer = 0;
}

static void MsgDrawBack(MESSAGE *msg, CHAR line)
{
	UNUSED Mtx *mtx;
	GfxTranslate(GFX_NOPUSH, msg->x, msg->y, 0);
	switch (msg_type)
	{
	case 0:
		if (msg_state == 0 || msg_state == 3)
		{
			GfxScale(GFX_NOPUSH, 1.0/msg_scale, 1.0/msg_scale, 1);
			GfxRotate(GFX_NOPUSH, msg_angle*4, 0, 0, 1);
		}
		gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, 150);
		break;
	case 1:
		if (msg_state == 0 || msg_state == 3)
		{
			GfxTranslate(GFX_NOPUSH, 65.0-65.0/msg_scale, 40.0/msg_scale-40, 0);
			GfxScale(GFX_NOPUSH, 1.0/msg_scale, 1.0/msg_scale, 1);
		}
		gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 150);
		break;
	}
#ifdef JAPANESE
	GfxTranslate(GFX_PUSH, -5, 2, 0);
	GfxScale(GFX_NOPUSH, 1.1F, (float)line/4 + 0.1, 1);
#endif
#ifdef ENGLISH
	GfxTranslate(GFX_PUSH, -7, 5, 0);
	GfxScale(GFX_NOPUSH, 1.1F, (float)line/5 + 0.1, 1);
#endif
	gSPDisplayList(glistp++, gfx_message_box);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
}

static void MsgSetColor(CHAR flag, CHAR line)
{
	u8 color;
	if (ISTRUE(flag))
	{
		if (line == 1)
		{
			gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 0xFF);
		}
		else if (line == msg_cursor)
		{
			color = 200 + 50*SIN(msg_theta);
			gDPSetEnvColor(glistp++, color, color, color, 0xFF);
		}
		else
		{
			gDPSetEnvColor(glistp++, 200, 200, 200, 0xFF);
		}
	}
	else
	{
		switch (msg_type)
		{
			case 0: break;
			case 1: gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, 0xFF); break;
		}
	}
}

#ifdef JAPANESE
#define MsgStart(line) GfxTranslate(GFX_PUSH, 5, 2 - 20*(line), 0)
#endif
#ifdef ENGLISH
#define MsgStart(line) GfxTranslate(GFX_PUSH, 0, 2 - 16*(line), 0)
#define MsgSpace(space) \
	GfxTranslate(GFX_NOPUSH, kerningtab[CH_SPACE]*(space), 0, 0)
#endif

static void MsgLF(CHAR line, CHAR end, char *state, char *space, short *count)
{
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	if (line == end)
	{
		*state = 1;
		return;
	}
	MsgStart(line);
	*count = 0;
	*space = 1;
}

#ifdef JAPANESE
static void MsgKuten(char *space, short *count)
{
	if (*count != 0) GfxTranslate(GFX_NOPUSH, 10*(*space), 0, 0);
	GfxTranslate(GFX_PUSH, -2, -5, 0);
	PrintLgChar(CH_HANDAKUTEN);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	(*count)++;
	*space = 1;
}

static void MsgFmtInt(char *space, short *count)
{
	CHAR d = msg_value/10;
	CHAR u = msg_value - 10*d;
	if (d)
	{
		GfxTranslate(GFX_NOPUSH, 10*(*space), 0, 0);
		PrintLgChar(CH_0+d);
	}
	else
	{
		(*space)++;
	}
	GfxTranslate(GFX_NOPUSH, 10*(*space), 0, 0);
	PrintLgChar(CH_0+u);
	(*count)++;
	*space = 1;
}
#endif

#ifdef ENGLISH
static void MsgFmtInt(char *space, short *count)
{
	CHAR d = msg_value/10;
	CHAR u = msg_value - 10*d;
	if (d)
	{
		if (*space != 1) MsgSpace(*space);
		PrintLgChar(CH_0+d);
		GfxTranslate(GFX_NOPUSH, kerningtab[CH_0+d], 0, 0);
		*space = 1;
		(*count)++;
	}
	else
	{
	}
	if (*space != 1) MsgSpace(*space-1);
	PrintLgChar(CH_0+u);
	GfxTranslate(GFX_NOPUSH, kerningtab[CH_0+u], 0, 0);
	(*count)++;
	*space = 1;
}

static void MsgMulti(
	CHAR code, CHAR line, short *count, CHAR page, CHAR space, CHAR start
)
{
	CHAR i;
	STATIC unsigned char str_multi[][5] =
	{
		{3, CH_t,CH_h,CH_e},
		{3, CH_y,CH_o,CH_u},
	};
	if (line >= start && line <= start+page)
	{
		if (*count != 0 || space != 1) MsgSpace(space-1);
		for (i = 0; i < str_multi[code][0]; i++)
		{
			PrintLgChar(str_multi[code][1+i]);
			GfxTranslate(GFX_NOPUSH, kerningtab[str_multi[code][1+i]], 0, 0);
		}
	}
	count += str_multi[code][0];
}
#endif

static unsigned int MsgClamp(SHORT x)
{
	if (x < 0) x = 0;
	return x;
}

#if REVISION >= 199609
static void MsgDraw(CHAR flag, MESSAGE *msg, CHAR start)
#else
static void MsgDraw(CHAR flag, MESSAGE *msg)
#endif
{
	UNUSED int i, n;
	unsigned char c;
	const unsigned char *str = SegmentToVirtual(msg->str);
	char line = 1, end, state = 0;
#ifdef JAPANESE
	char mark = 0;
#else
	UNUSED char mark = 0;
#endif
	char space = 1, page = msg->line;
	short index, count = 0;
	if (msg_state == 2) end = 1 + 2*page;
	else                end = 1 +   page;
	gSPDisplayList(glistp++, gfx_lgfont_begin);
	index = msg_index;
	if (msg_state == 2) GfxTranslate(GFX_NOPUSH, 0, msg_scroll, 0);
	MsgStart(line);
	while (!state)
	{
		MsgSetColor(flag, line);
		c = str[index];
		switch (c)
		{
		case CH_NUL:
			state = 2;
			gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
			break;
		case CH_LF:
			line++;
			MsgLF(line, end, &state, &space, &count);
#if REVISION >= 199609
#ifdef JAPANESE
			mark = 0;
#endif
#endif
			break;
		case CH_DAKUTEN:
			mark = 1;
			break;
		case CH_HANDAKUTEN:
			mark = 2;
			break;
		case CH_SPACE:
#ifdef JAPANESE
			if (count != 0) space++;
#endif
#ifdef ENGLISH
			space++;
#endif
			count++;
			break;
#ifdef JAPANESE
		case CH_KUTEN:
			MsgKuten(&space, &count);
			break;
#endif
#ifdef ENGLISH
		case CH_TAB:
			space += 2;
			count += 2;
			break;
		case CH_the:
			MsgMulti(0, line, &count, page, space, start);
			space = 1;
			break;
		case CH_you:
			MsgMulti(1, line, &count, page, space, start);
			space = 1;
			break;
#endif
		case CH_FMTINT:
			MsgFmtInt(&space, &count);
			break;
		default:
#if REVISION >= 199609
			if (line >= start && line <= start+page)
			{
#ifdef JAPANESE
				if (count != 0) GfxTranslate(GFX_NOPUSH, 10*space, 0, 0);
				PrintLgChar(c);
				space = 1;
				count++;
				if (mark)
				{
					GfxTranslate(GFX_PUSH, 5, 7, 0);
					PrintLgChar(CH_DAKUTEN+mark-1);
					gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
					mark = 0;
				}
#endif
#ifdef ENGLISH
				if (count != 0 || space != 1) MsgSpace(space-1);
				PrintLgChar(c);
				GfxTranslate(GFX_NOPUSH, kerningtab[c], 0, 0);
				space = 1;
				count++;
#endif
			}
#else
#ifdef JAPANESE
			if (count != 0) GfxTranslate(GFX_NOPUSH, 10*space, 0, 0);
			PrintLgChar(c);
			space = 1;
			count++;
			if (mark)
			{
				GfxTranslate(GFX_PUSH, 5, 7, 0);
				PrintLgChar(CH_DAKUTEN+mark-1);
				gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
				mark = 0;
			}
#endif
#endif
		}
#if REVISION < 199609
#ifdef JAPANESE
		if (count == 12)
		{
			if (str[index+1] == CH_KUTEN)
			{
				MsgKuten(&space, &count);
				index++;
			}
			if (str[index+1] == CH_TOUTEN)
			{
				GfxTranslate(GFX_NOPUSH, 10*space, 0, 0);
				PrintLgChar(CH_TOUTEN);
				index++;
			}
			if (str[index+1] == CH_LF) index++;
			if (str[index+1] == CH_NUL)
			{
				state = 2;
				gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
				break;
			}
			else
			{
				line++;
				MsgLF(line, end, &state, &space, &count);
			}
		}
#endif
#endif
		index++;
	}
	gSPDisplayList(glistp++, gfx_lgfont_end);
	if (msg_state == 1)
	{
		if (state == 2) msg_next = -1;
		else            msg_next = index;
	}
	msg_cursor_line = line;
}

static void MsgDrawCursor(void)
{
	if (msg_state == 1) CursorProc(CURSOR_H, &msg_cursor, 1, 2);
#ifdef JAPANESE
	GfxTranslate(GFX_NOPUSH, 25 + 50*(msg_cursor-1), 1 - 20*msg_cursor_line, 0);
#endif
#ifdef ENGLISH
	GfxTranslate(GFX_NOPUSH, 9 + 56*(msg_cursor-1), 2 - 16*msg_cursor_line, 0);
#endif
	if (msg_type == 0) {gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 0xFF);}
	else               {gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, 0xFF);}
	gSPDisplayList(glistp++, gfx_message_cursor);
}

static void MsgDrawNextPage(CHAR line)
{
	unsigned int frame = gfx_frame;
	if (frame & 8) return;
#ifdef JAPANESE
	GfxTranslate(GFX_PUSH, 123, 2 + -20*line, 0);
#endif
#ifdef ENGLISH
	GfxTranslate(GFX_PUSH, 118, 5 + -16*line, 0);
#endif
	GfxScale(GFX_NOPUSH, 0.8F, 0.8F, 1);
	GfxRotate(GFX_NOPUSH, -90, 0, 0, 1);
	if (msg_type == 0) {gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 0xFF);}
	else               {gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, 0xFF);}
	gSPDisplayList(glistp++, gfx_message_cursor);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
}

static void MsgProcEndSound(SHORT msg)
{
	STATIC short battle[] = {MSG_17, MSG_114, MSG_128, MSG_117, MSG_150};
	STATIC short fanfare[] = {MSG_5, MSG_9, MSG_55, MSG_164};
	STATIC short se7_1e[] = {MSG_10, MSG_11, MSG_12, MSG_13, MSG_14};
#if REVISION >= 199609
	STATIC short bgmstop[] = {MSG_17, MSG_115, MSG_116, MSG_118, MSG_152};
#else
	STATIC short bgmstop[] = {MSG_17, MSG_115, MSG_118, MSG_152};
#endif
	SHORT i;
	for (i = 0; i < (int)lenof(battle); i++)
	{
		if (battle[i] == msg)
		{
			Na_SeqUnmute(0, 60);
			Na_BgmPlay(0, NA_BGM_BATTLE, 0);
			return;
		}
	}
	for (i = 0; i < (int)lenof(fanfare); i++)
	{
		if (fanfare[i] == msg && msg_cursor == 1)
		{
			Na_Fanfare();
			return;
		}
	}
	for (i = 0; i < (int)lenof(se7_1e); i++)
	{
		if (se7_1e[i] == msg && msg_cursor == 1)
		{
			Na_FixSePlay(NA_SE7_1E);
			return;
		}
	}
	for (i = 0; i < (int)lenof(bgmstop); i++)
	{
		if (bgmstop[i] == msg)
		{
			Na_SeqFadeout(0, 1);
			return;
		}
	}
}

#ifdef sgi
#define SetScissor(pkt, mode, ulx, uly, lrx, lry) \
	gDPSetScissor(pkt, mode, ulx, uly, lrx, lry)
#else
#define SetScissor(pkt, mode, ulx, uly, lrx, lry) \
	gDPSetScissorFrac(pkt, mode, 4*(ulx), 4*(uly), 4*(lrx), 4*(lry))
#endif

static void MsgProc(void)
{
	MESSAGE **msgtab = SegmentToVirtual(messagetab);
	MESSAGE *msg = SegmentToVirtual(msgtab[msg_code]);
#if REVISION >= 199609
	CHAR line;
#endif
	if (msg == SegmentToVirtual(NULL))
	{
		msg_code = MSG_NULL;
		return;
	}
	switch (msg_state)
	{
	case 0:
		if (msg_angle == 90)
		{
			Na_MessageSound(msg_code);
			Na_FixSePlay(NA_SE7_04);
		}
		if (msg_type == 0)
		{
			msg_angle -= 90/12.0;
			msg_scale -= 18/12.0;
		}
		else
		{
			msg_angle -= 90/9.0;
			msg_scale -= 18/9.0;
		}
		if (msg_angle == 0)
		{
			msg_state = 1;
			msg_cursor = 1;
		}
#if REVISION >= 199609
		line = 1;
#endif
		break;
	case 1:
		msg_angle = 0;
		if (contp->down & A_BUTTON || contp->down & B_BUTTON)
		{
			if (msg_next == -1)
			{
				MsgProcEndSound(msg_code);
				msg_state = 3;
			}
			else
			{
				msg_state = 2;
				Na_FixSePlay(NA_SE7_13);
			}
		}
#if REVISION >= 199609
		line = 1;
#endif
		break;
	case 2:
		msg_scroll += 2*msg->line;
#ifdef JAPANESE
		if (msg_scroll >= 20*msg->line)
#endif
#ifdef ENGLISH
		if (msg_scroll >= 16*msg->line)
#endif
		{
			msg_index = msg_next;
			msg_state = 1;
			msg_scroll = 0;
		}
#if REVISION >= 199609
#ifdef JAPANESE
		line = 1 + msg_scroll/20;
#endif
#ifdef ENGLISH
		line = 1 + msg_scroll/16;
#endif
#endif
		break;
	case 3:
		if (msg_angle == 20)
		{
			GmFreeze(0, NULL);
			Na_FixSePlay(NA_SE7_05);
			if (msg_type == 1) camera_8028BD34(2);
			msg_answer = msg_cursor;
		}
		msg_angle += 90/9;
		msg_scale += 18/9;
		if (msg_angle == 90)
		{
			msg_state = 0;
			msg_code = MSG_NULL;
			msg_index = 0;
			msg_cursor_flag = FALSE;
			msg_next = 0;
			msg_answer = 0;
		}
#if REVISION >= 199609
		line = 1;
#endif
		break;
#ifdef __GNUC__
	default: __builtin_unreachable();
#endif
	}
	MsgDrawBack(msg, msg->line);
#ifdef JAPANESE
	SetScissor(
		glistp++, G_SC_NON_INTERLACE,
		MsgClamp(msg->x),
		MsgClamp(SCREEN_HT-msg->y),
		MsgClamp(msg->x+130),
		MsgClamp(SCREEN_HT-msg->y + 80*msg->line/4)
	);
#endif
#ifdef ENGLISH
	SetScissor(
		glistp++, G_SC_NON_INTERLACE,
		MsgClamp(msg->x),
		MsgClamp(SCREEN_HT-msg->y),
		MsgClamp(msg->x+132),
		MsgClamp(SCREEN_HT-msg->y + 80*msg->line/5)
	);
#endif
#if REVISION >= 199609
	MsgDraw(FALSE, msg, line);
#else
	MsgDraw(FALSE, msg);
#endif
	if (msg_next == -1 && ISTRUE(msg_cursor_flag)) MsgDrawCursor();
	gDPSetScissor(glistp++, G_SC_NON_INTERLACE, 2, 2, SCREEN_WD-4, SCREEN_HT-4);
	if (msg_next != -1 && msg_state == 1) MsgDrawNextPage(msg->line);
}

static short menu_code = MENU_NULL;

void MenuOpen(SHORT code)
{
	if (menu_code == MENU_NULL) menu_code = code;
}
