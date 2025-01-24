#define MsgStart(line) GfxTranslate(GFX_PUSH, 0, 2 - 16*(line), 0)
#define MsgSpace(space) \
	GfxTranslate(GFX_NOPUSH, kerningtab[CH_SPACE]*(space), 0, 0)

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
		{3, CH_t, CH_h, CH_e},
		{3, CH_y, CH_o, CH_u},
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

static unsigned int MsgClamp(SHORT x)
{
	if (x < 0) x = 0;
	return x;
}

static void MsgDraw(CHAR flag, MESSAGE *msg, CHAR start)
{
	UNUSED int i, n;
	unsigned char c;
	const unsigned char *str = SegmentToVirtual(msg->str);
	char line = 1, end, state = 0;
	UNUSED
	char mark = 0;
	char space = 1, page = msg->line;
	short index, count = 0;
	if (msg_state == 2) end = 1 + 2*page;
	else                end = 1 +   page;
	gSPDisplayList(glistp++, gfx_lgfont_start);
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
			break;
		case CH_DAKUTEN:
			mark = 1;
			break;
		case CH_HANDAKUTEN:
			mark = 2;
			break;
		case CH_SPACE:
			space++;
			count++;
			break;
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
		case CH_FMTINT:
			MsgFmtInt(&space, &count);
			break;
		default:
			if (line >= start && line <= start+page)
			{
				if (count != 0 || space != 1) MsgSpace(space-1);
				PrintLgChar(c);
				GfxTranslate(GFX_NOPUSH, kerningtab[c], 0, 0);
				space = 1;
				count++;
			}
		}
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
	GfxTranslate(GFX_NOPUSH, 9 + 56*(msg_cursor-1), 2 - 16*msg_cursor_line, 0);
	if (msg_type == 0) {gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 0xFF);}
	else               {gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, 0xFF);}
	gSPDisplayList(glistp++, gfx_message_cursor);
}

static void MsgDrawNextPage(CHAR line)
{
	unsigned int frame = gfx_frame;
	if (frame & 8) return;
	GfxTranslate(GFX_PUSH, 118, 5 + -16*line, 0);
	GfxScale(GFX_NOPUSH, 0.8F, 0.8F, 1);
	GfxRotate(GFX_NOPUSH, -90, 0, 0, 1);
	if (msg_type == 0) {gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 0xFF);}
	else               {gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, 0xFF);}
	gSPDisplayList(glistp++, gfx_message_cursor);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
}
