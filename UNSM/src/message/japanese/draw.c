static u8 *UnpackI1(u16 *src, SHORT w, SHORT h)
{
	int i;
	USHORT bit;
	u8 *dst;
	SHORT n = 0;
	if (!(dst = GfxAlloc(w*h))) return NULL;
	for (i = 0; i < w*h/16; i++)
	{
		bit = 0x8000;
		while (bit)
		{
			if (src[i] & bit)   dst[n] = 0xFF;
			else                dst[n] = 0x00;
			bit /= 2;
			n++;
		}
	}
	return dst;
}

static void PrintLgChar(UCHAR c)
{
	u16 **lgfont = SegmentToVirtual(txt_lgfont);
	u16 *txt = SegmentToVirtual(lgfont[c]);
	u8 *txt8 = UnpackI1(txt, 8, 16);
	gDPPipeSync(glistp++);
	gDPSetTextureImage(glistp++, G_IM_FMT_IA, G_IM_SIZ_8b, 1, K0_TO_PHYS(txt8));
	gSPDisplayList(glistp++, gfx_lgfont_char);
}

void PrintLg(SHORT x, SHORT y, const unsigned char *str)
{
	char mark = 0;
	int i = 0;
	UCHAR line = 1;
	GfxTranslate(GFX_PUSH, x, y, 0);
	while (str[i] != CH_NUL)
	{
		switch (str[i])
		{
		case CH_DAKUTEN:
			mark = 1;
			break;
		case CH_HANDAKUTEN:
			mark = 2;
			break;
		case CH_LF:
			gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
			GfxTranslate(GFX_PUSH, x, y - 18*line, 0);
			line++;
			break;
		case CH_KUTEN:
			GfxTranslate(GFX_PUSH, -2, -5, 0);
			PrintLgChar(CH_HANDAKUTEN);
			gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
			break;
		case CH_SPACE:
			GfxTranslate(GFX_NOPUSH, 5, 0, 0);
			break;
			break;
		default:
			PrintLgChar(str[i]);
			if (mark)
			{
				GfxTranslate(GFX_PUSH, 5, 5, 0);
				PrintLgChar(CH_DAKUTEN+mark-1);
				gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
				mark = 0;
			}
			GfxTranslate(GFX_NOPUSH, 10, 0, 0);
		}
		i++;
	}
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
}

void Print16(CHAR font, SHORT x, SHORT y, const unsigned char *str)
{
	int i = 0;
	u16 **selfont = SegmentToVirtual(txt_selfont);
	u16 **glbfont = SegmentToVirtual(txt_glbfont);
	unsigned int ux = x;
	unsigned int uy = y;
	int width;
	if (font == FONT_SEL)   width = 16;
	else                    width = 14;
	while (str[i] != CH_NUL)
	{
		gDPPipeSync(glistp++);
		if (font == FONT_SEL) gDPSetTextureImage(
			glistp++, G_IM_FMT_RGBA, G_IM_SIZ_16b, 1, selfont[str[i]]
		);
		if (font == FONT_GLB) gDPSetTextureImage(
			glistp++, G_IM_FMT_RGBA, G_IM_SIZ_16b, 1, glbfont[str[i]]
		);
		gSPDisplayList(glistp++, gfx_print_1cyc_char);
		gSPTextureRectangle(
			glistp++, ux << 2, uy << 2, (ux+16) << 2, (uy+16) << 2,
			G_TX_RENDERTILE, 0, 0, 0x400, 0x400
		);
		ux += width;
		i++;
	}
}

void PrintSm(SHORT x, SHORT y, const unsigned char *str)
{
	char mark = 0;
	int i = 0;
	unsigned int ux = x;
	unsigned int uy = y;
	u16 **smfont = SegmentToVirtual(txt_smfont);
	while (str[i] != CH_NUL)
	{
		switch (str[i])
		{
		case CH_DAKUTEN:
			mark = 1;
			break;
		case CH_HANDAKUTEN:
			mark = 2;
			break;
		case CH_SPACE:
			ux += 4;
			break;
		default:
			gDPLoadImageBlock(
				glistp++, smfont[str[i]], G_IM_FMT_IA, G_IM_SIZ_8b, 8, 8
			);
			gSPTextureRectangle(
				glistp++, ux << 2, uy << 2, (ux+8) << 2, (uy+8) << 2,
				G_TX_RENDERTILE, 0, 0, 0x400, 0x400
			);
			if (mark)
			{
				gDPLoadImageBlock(
					glistp++, smfont[CH_DAKUTEN+mark-1],
					G_IM_FMT_IA, G_IM_SIZ_8b, 8, 8
				);
				gSPTextureRectangle(
					glistp++,
					(ux+6) << 2, (uy-7) << 2, (ux+6+8) << 2, (uy-7+8) << 2,
					G_TX_RENDERTILE, 0, 0, 0x400, 0x400
				);
				mark = 0;
			}
			ux += 9;
		}
		i++;
	}
}
