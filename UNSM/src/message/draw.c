static void GfxLoadIdent(void)
{
	Mtx *mtx = GfxAlloc(sizeof(Mtx));
	if (!mtx) return;
	mtx->m[0][0] = 1 << 16;
	mtx->m[1][0] = 0;
	mtx->m[2][0] = 0;
	mtx->m[3][0] = 0;
	mtx->m[0][1] = 0;
	mtx->m[1][1] = 1 << 16;
	mtx->m[2][1] = 0;
	mtx->m[3][1] = 0;
	mtx->m[0][2] = 1;
	mtx->m[1][2] = 0;
	mtx->m[2][2] = 0;
	mtx->m[3][2] = 0;
	mtx->m[0][3] = 0;
	mtx->m[1][3] = 1;
	mtx->m[2][3] = 0;
	mtx->m[3][3] = 0;
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

extern Gfx gfx_print_1cyc_start[];
extern Gfx gfx_print_1cyc_char[];
extern Gfx gfx_print_1cyc_end[];
extern Gfx gfx_print_1cyc_char[];
extern Gfx gfx_lgfont_start[];
extern Gfx gfx_lgfont_char[];
extern Gfx gfx_lgfont_end[];

#ifdef JAPANESE
#include "japanese/draw.c"
#endif
#ifdef ENGLISH
#include "english/draw.c"
#endif

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
