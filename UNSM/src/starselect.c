#include <sm64.h>

#ifdef ENGLISH
#include "en_us.h"
#endif

extern Gfx gfx_print_1cyc_start[];
extern Gfx gfx_print_1cyc_end[];
extern Gfx gfx_lgfont_start[];
extern Gfx gfx_lgfont_end[];
extern unsigned char *coursename[];
extern unsigned char *levelname[];

extern Gfx gfx_smfont_start[];
extern Gfx gfx_smfont_end[];
extern Gfx gfx_course[];

static OBJECT *ss_obj[8];
static s8 ss_result;
static u8 ss_have;
static s8 ss_count;
static u8 ss_next;
static s8 ss_option = 0;
static s8 ss_cursor = 0;
static int ss_timer = 0;

extern OBJLANG o_selectstar[];

void SelectStar_Proc(void)
{
	switch (object->o_v0)
	{
	case 0:
		object->o_f5 -= 0.1;
		if (object->o_f5 < 1.0) object->o_f5 = 1.0;
		object->o_shapeangy = 0;
		break;
	case 1:
		object->o_f5 += 0.1;
		if (object->o_f5 > 1.3) object->o_f5 = 1.3;
		object->o_shapeangy += 0x800;
		break;
	case 2:
		object->o_shapeangy += 0x800;
		break;
	}
	ObjectSetScale(object->o_f5);
	object->o_v1++;
}

static void StarMenu_Init100(UCHAR star)
{
	if (star & 0100)
	{
		ss_obj[6] = ObjMakeAt(
			object, 0, S_POWERSTAR, o_selectstar, 370, 24, -300, 0, 0, 0
		);
		ss_obj[6]->o_f5 = 0.8;
		ss_obj[6]->o_v0 = 2;
	}
}

void StarMenu_Init(void)
{
	SHORT i = 0;
	int shape[10];
	UCHAR star = BuGetStar(course_index-1);
	ss_count = 0;
	while (i != ss_have)
	{
		if (star & (1 << ss_count))
		{
			shape[ss_count] = S_POWERSTAR;
			i++;
		}
		else
		{
			shape[ss_count] = S_SHADESTAR;
			if (ss_next == 0)
			{
				ss_next = ss_count+1;
				ss_cursor = ss_count;
			}
		}
		ss_count++;
	}
	if (ss_count == ss_have && ss_count != 6)
	{
		shape[ss_count] = S_SHADESTAR;
		ss_next = ss_count+1;
		ss_cursor = ss_count;
		ss_count++;
	}
	if (ss_have == 6) ss_next = ss_count;
	if (ss_have == 0) ss_next = 1;
	for (i = 0; i < ss_count; i++)
	{
		ss_obj[i] = ObjMakeAt(
			object, 0, shape[i], o_selectstar,
			-75*(ss_count-1) + 152*i, 248, -300, 0, 0, 0
		);
		ss_obj[i]->o_f5 = 1;
	}
	StarMenu_Init100(star);
}

void StarMenu_Proc(void)
{
	CHAR i;
	UCHAR count;
	UCHAR star = BuGetStar(course_index-1);
	if (ss_have != 6)
	{
		ss_option = 0;
		CursorProc(CURSOR_H, &ss_cursor, 0, ss_have);
		count = ss_cursor;
		for (i = 0; i < ss_count; i++)
		{
			if ((star & (1 << i)) || i == ss_next-1)
			{
				if (count == 0)
				{
					ss_option = i;
					break;
				}
				count--;
			}
		}
	}
	else
	{
		CursorProc(CURSOR_H, &ss_cursor, 0, ss_count-1);
		ss_option = ss_cursor;
	}
	for (i = 0; i < ss_count; i++)
	{
		if (ss_option == i) ss_obj[i]->o_v0 = 1;
		else                ss_obj[i]->o_v0 = 0;
	}
}

#define COURSE_X    (SCREEN_WD/2-2)
#define COURSE_Y    159

static void SsDrawCourse(void)
{
	unsigned char buf[4];
	GfxTranslate(GFX_PUSH, COURSE_X, SCREEN_HT-COURSE_Y, 0);
	gSPDisplayList(glistp++, gfx_course);
	gSPPopMatrix(glistp++, G_MTX_MODELVIEW);
	gSPDisplayList(glistp++, gfx_print_1cyc_start);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 0xFF);
	itostr(course_index, buf);
	if (course_index < 10) Print16(FONT_GLB, COURSE_X-12/2, COURSE_Y-1, buf);
	else                   Print16(FONT_GLB, COURSE_X-30/2, COURSE_Y-1, buf);
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
}

static void SsDraw(void)
{
	STATIC unsigned char str_myscore[] = {STR_MYSCORE};
	unsigned char str_number[] = {0, CH_NUL};
	unsigned char **crstab = SegmentToVirtual(coursename);
	unsigned char *crsname = SegmentToVirtual(crstab[course_index-1]);
	unsigned char **lvltab = SegmentToVirtual(levelname);
	unsigned char *lvlname;
	SHORT course_x, level_x;
	CHAR i;
	GfxScreenProj();
	gSPDisplayList(glistp++, gfx_print_1cyc_start);
	gDPSetEnvColor(glistp++, 0xFF, 0xFF, 0xFF, 0xFF);
	PrintCoin(1, file_index-1, course_index-1, SCREEN_WD/2-5, 106);
	gSPDisplayList(glistp++, gfx_print_1cyc_end);
	gSPDisplayList(glistp++, gfx_lgfont_start);
	gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, 0xFF);
	if (BuGetCoin(course_index-1))
	{
		PrintLg(SCREEN_WD/2-58, SCREEN_HT-122, str_myscore);
	}
	course_x = StrCenterX(SCREEN_WD/2, &crsname[3], 10);
	PrintLg(course_x, SCREEN_HT-16-(COURSE_Y+32), &crsname[3]);
	gSPDisplayList(glistp++, gfx_lgfont_end);
	SsDrawCourse();
	gSPDisplayList(glistp++, gfx_smfont_start);
	gDPSetEnvColor(glistp++, 0x00, 0x00, 0x00, 0xFF);
	if (ss_count)
	{
		lvlname = SegmentToVirtual(lvltab[6*(course_index-1)+ss_option]);
		level_x = StrCenterX(SCREEN_WD/2+3, lvlname, 8);
		PrintSm(level_x, 81, lvlname);
	}
	for (i = 1; i <= ss_count; i++)
	{
		str_number[0] = CH_0 + i;
		PrintSm(SCREEN_WD/2-4 - 17*(ss_count-1) + 34*(i-1), 38, str_number);
	}
	gSPDisplayList(glistp++, gfx_smfont_end);
}

long StarSelectDraw(SHORT code, UNUSED long status)
{
	if (code == SC_DRAW) SsDraw();
	return 0;
}

long StarSelectInit(UNUSED SHORT code, UNUSED long status)
{
	UCHAR star = BuGetStar(course_index-1);
	ss_result = 0;
	ss_next = 0;
	ss_count = 0;
	ss_timer = 0;
	ss_have = BuStarCount(course_index-1);
	if (star & 0100) ss_have--;
#ifndef sgi
	return 1;
#endif
}

long StarSelectProc(UNUSED SHORT code, UNUSED long status)
{
	if (ss_timer > 10 && (
		(contp->down & A_BUTTON) ||
		(contp->down & START_BUTTON) ||
		(contp->down & B_BUTTON)
	))
	{
#ifdef NEWVOICE
		Na_FixSePlay(NA_SE7_24);
#else
		Na_FixSePlay(NA_SE7_1E);
#endif
		if (ss_next >= ss_option+1) ss_result = ss_option+1;
		else                        ss_result = ss_next;
		pausemenu_level = ss_option+1;
	}
	SceneProc();
	ss_timer++;
	return ss_result;
}
