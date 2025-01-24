#define MsgStartLine(line) GfxTranslate(GFX_PUSH, 5, 2 - 20*(line), 0)

static void MsgNewline(
	CHAR line, CHAR end, char *state, char *space, short *count
)
{
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	if (line == end)
	{
		*state = 1;
		return;
	}
	MsgStartLine(line);
	*count = 0;
	*space = 1;
}

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


static unsigned int MsgClamp(SHORT x)
{
	if (x < 0) x = 0;
	return x;
}

static void MsgDraw(CHAR flag, MESSAGE *msg)
{
	UNUSED int i, n;
	unsigned char c;
	const unsigned char *str = SegmentToVirtual(msg->str);
	char line = 1, end, state = 0, mark = 0, space = 1, page = msg->line;
	short index, count = 0;
	if (msg_state == 2) end = 1 + 2*page;
	else                end = 1 +   page;
	gSPDisplayList(glistp++, gfx_lgfont_start);
	index = msg_index;
	if (msg_state == 2) GfxTranslate(GFX_NOPUSH, 0, msg_scroll, 0);
	MsgStartLine(line);
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
			MsgNewline(line, end, &state, &space, &count);
			break;
		case CH_DAKUTEN:
			mark = 1;
			break;
		case CH_HANDAKUTEN:
			mark = 2;
			break;
		case CH_SPACE:
			if (count != 0) space++;
			count++;
			break;
		case CH_KUTEN:
			MsgKuten(&space, &count);
			break;
		case CH_FMTINT:
			MsgFmtInt(&space, &count);
			break;
		default:
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
		}
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
				MsgNewline(line, end, &state, &space, &count);
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
	GfxTranslate(GFX_NOPUSH, 25 + 50*(msg_cursor-1), 1 - 20*msg_cursor_line, 0);
	if (msg_type == 0) {gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 0xFF);}
	else               {gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, 0xFF);}
	gSPDisplayList(glistp++, gfx_message_cursor);
}

static void MsgDrawNextPage(CHAR line)
{
	unsigned int frame = gfx_frame;
	if (frame & 8) return;
	GfxTranslate(GFX_PUSH, 123, 2 + -20*line, 0);
	GfxScale(GFX_NOPUSH, 0.8F, 0.8F, 1);
	GfxRotate(GFX_NOPUSH, -90, 0, 0, 1);
	if (msg_type == 0) {gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 0xFF);}
	else               {gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, 0xFF);}
	gSPDisplayList(glistp++, gfx_message_cursor);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
}
