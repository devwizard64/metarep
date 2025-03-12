void GfxLoadIdent(void)
{
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	if (!mtx) return;
	mtx->m[0][0] = 1<<16; mtx->m[1][0] = 0; mtx->m[2][0] = 0; mtx->m[3][0] = 0;
	mtx->m[0][1] = 0; mtx->m[1][1] = 1<<16; mtx->m[2][1] = 0; mtx->m[3][1] = 0;
	mtx->m[0][2] = 1; mtx->m[1][2] = 0; mtx->m[2][2] = 0; mtx->m[3][2] = 0;
	mtx->m[0][3] = 0; mtx->m[1][3] = 1; mtx->m[2][3] = 0; mtx->m[3][3] = 0;
	gSPMatrix(
		glistp++, K0_TO_PHYS(mtx), G_MTX_MODELVIEW|G_MTX_LOAD|G_MTX_NOPUSH
	);
	gSPMatrix(
		glistp++, K0_TO_PHYS(mtx), G_MTX_PROJECTION|G_MTX_LOAD|G_MTX_NOPUSH
	);
}

void GfxTranslate(CHAR flag, float x, float y, float z)
{
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	if (!mtx) return;
	guTranslate(mtx, x, y, z);
	if (flag == GFX_PUSH) gSPMatrix(
		glistp++, K0_TO_PHYS(mtx), G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_PUSH
	);
	if (flag == GFX_NOPUSH) gSPMatrix(
		glistp++, K0_TO_PHYS(mtx), G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_NOPUSH
	);
}

void GfxRotate(CHAR flag, float a, float x, float y, float z)
{
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	if (!mtx) return;
	guRotate(mtx, a, x, y, z);
	if (flag == GFX_PUSH) gSPMatrix(
		glistp++, K0_TO_PHYS(mtx), G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_PUSH
	);
	if (flag == GFX_NOPUSH) gSPMatrix(
		glistp++, K0_TO_PHYS(mtx), G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_NOPUSH
	);
}

void GfxScale(CHAR flag, float x, float y, float z)
{
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	if (!mtx) return;
	guScale(mtx, x, y, z);
	if (flag == GFX_PUSH) gSPMatrix(
		glistp++, K0_TO_PHYS(mtx), G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_PUSH
	);
	if (flag == GFX_NOPUSH) gSPMatrix(
		glistp++, K0_TO_PHYS(mtx), G_MTX_MODELVIEW|G_MTX_MUL|G_MTX_NOPUSH
	);
}

void GfxScreenProj(void)
{
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	if (!mtx) return;
	GfxLoadIdent();
	guOrtho(mtx, 0, SCREEN_WD, 0, SCREEN_HT, -10, 10, 1);
	gSPPerspNormalize(glistp++, 0xFFFF);
	gSPMatrix(
		glistp++, K0_TO_PHYS(mtx), G_MTX_PROJECTION|G_MTX_MUL|G_MTX_NOPUSH
	);
}

extern u16 *txt_glbfont[];
extern u8 *txt_lgfont[];
extern u16 *txt_staff[];
extern u16 *txt_selfont[];
extern u8 *txt_smfont[];

extern Gfx gfx_print_1cyc_begin[];
extern Gfx gfx_print_1cyc_char[];
extern Gfx gfx_print_1cyc_end[];
extern Gfx gfx_print_1cyc_char[];
extern Gfx gfx_lgfont_begin[];
extern Gfx gfx_lgfont_char[];
extern Gfx gfx_lgfont_end[];

#ifndef JAPANESE
UNUSED
#endif
static u8 *UnpackI1(u16 *src, SHORT w, SHORT h)
{
	int i;
	u16 bit;
	u8 *dst;
	SHORT n = 0;
	if (!(dst = GfxAlloc(sizeof(u8)*w*h))) return NULL;
	for (i = 0; i < w*h/16; i++)
	{
		bit = 0x8000;
		while (bit != 0)
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
#ifdef JAPANESE
	u8 *txt8 = UnpackI1(txt, 8, 16);
	gDPPipeSync(glistp++);
	gDPSetTextureImage(glistp++, G_IM_FMT_IA, G_IM_SIZ_8b, 1, K0_TO_PHYS(txt8));
#else
	gDPPipeSync(glistp++);
	gDPSetTextureImage(glistp++, G_IM_FMT_IA, G_IM_SIZ_16b, 1, K0_TO_PHYS(txt));
#endif
	gSPDisplayList(glistp++, gfx_lgfont_char);
}

#ifdef JAPANESE
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
#endif

#ifdef ENGLISH
static void PrintLgMulti(CHAR code)
{
	CHAR i;
	STATIC unsigned char str_multi[][5] =
	{
		{3, CH_t,CH_h,CH_e},
		{3, CH_y,CH_o,CH_u},
	};
	for (i = 0; i < str_multi[code][0]; i++)
	{
		PrintLgChar(str_multi[code][1+i]);
		GfxTranslate(GFX_NOPUSH, kerningtab[str_multi[code][1+i]], 0, 0);
	}
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
			GfxTranslate(GFX_PUSH, x, y - 16*line, 0);
			line++;
			break;
		case CH_KUTEN:
			GfxTranslate(GFX_PUSH, -2, -5, 0);
			PrintLgChar(CH_HANDAKUTEN);
			gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
			break;
		case CH_TAB:
			GfxTranslate(GFX_NOPUSH, kerningtab[CH_SPACE]*2, 0, 0);
			break;
		case CH_the:
			PrintLgMulti(0);
			break;
		case CH_you:
			PrintLgMulti(1);
			break;
		case CH_SPACE:
			GfxTranslate(GFX_NOPUSH, kerningtab[CH_SPACE], 0, 0);
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
			GfxTranslate(GFX_NOPUSH, kerningtab[str[i]], 0, 0);
			break;
		}
		i++;
	}
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
}
#endif

#if REVISION >= 199609
void Print16(CHAR font, SHORT x, SHORT y, const unsigned char *str)
{
	int i = 0;
	u16 **selfont = SegmentToVirtual(txt_selfont);
	u16 **glbfont = SegmentToVirtual(txt_glbfont);
	unsigned int ux = x;
	unsigned int uy = y;
	int width;
	if (font == FONT_SEL)   width = 16;
	else                    width = 12;
	while (str[i] != CH_NUL)
	{
		switch (str[i])
		{
		case CH_SPACE:
			ux += 8;
			break;
		default:
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
		}
		i++;
	}
}
#else
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
#endif

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
#ifdef ENGLISH
			ux += kerningtab[str[i]];
#else
			ux += 9;
#endif
		}
		i++;
	}
}

void Print8(SHORT x, SHORT y, const unsigned char *str)
{
	int i = 0;
	u16 **font = SegmentToVirtual(txt_staff);
	unsigned int ux = x;
	unsigned int uy = y;
	gDPSetLoadTile(glistp++, G_IM_FMT_RGBA, G_IM_SIZ_16b);
	gDPSetImageBlock(
		glistp++, G_IM_FMT_RGBA, G_IM_SIZ_16b, 8, 8, 0,
		G_TX_CLAMP, G_TX_CLAMP, 3, 3, 0, 0
	);
	while (str[i] != CH_NUL)
	{
		switch (str[i])
		{
		case CH_SPACE:
			ux += 4;
			break;
		default:
			gDPPipeSync(glistp++);
			gDPLoadImageBlock(
				glistp++, font[str[i]], G_IM_FMT_RGBA, G_IM_SIZ_16b, 8, 8
			);
			gSPTextureRectangle(
				glistp++, ux << 2, uy << 2, (ux+8) << 2, (uy+8) << 2,
				G_TX_RENDERTILE, 0, 0, 0x400, 0x400
			);
			ux += 7;
			break;
		}
		i++;
	}
}
