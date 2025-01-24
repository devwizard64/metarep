#include <sm64.h>

#ifdef JAPANESE
#include "ja_jp.h"
#endif
#ifdef ENGLISH
#include "en_us.h"
#endif

#ifdef ENGLISH
static u8 kerningtab[256] =
{
	7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6,
	6, 6, 5, 6, 6, 5, 8, 8, 6, 6, 6, 6, 6, 5, 6, 6,
	8, 7, 6, 6, 6, 5, 5, 6, 5, 5, 6, 5, 4, 5, 5, 3,
	7, 5, 5, 5, 6, 5, 5, 5, 5, 5, 7, 7, 5, 5, 4, 4,
	8, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	8, 8, 8, 8, 7, 7, 6, 7, 7, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	7, 5, 10, 5, 9, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 5, 7, 7, 6, 6, 8, 0, 8, 10, 6, 4, 10, 0, 0,
};
#endif

static s8 msg_state = 0;
static float msg_angle = 90;
static short msg_theta;
static float msg_scale = 19;
static short msg_scroll = 0;
static s8 msg_type = 0;
static s16 msg_code = -1;
static s16 msg_next = 0;
static s16 msg_index = 0;
static s8 msg_cursor = 1;
static s8 msg_cursor_line;
static char msg_cursor_flag = FALSE;
static int msg_value;
static u16 msg_alpha;

static u8 cursor_status = 0;
static u8 cursor_timer = 0;

int msg_answer = 0;

extern Gfx gfx_message_box[];
extern Gfx gfx_message_cursor[];

extern MESSAGE *selecttab[];
extern MESSAGE *messagetab[];

#include "message/draw.c"
#include "message/message.c"
#include "message/demo.c"
#include "message/menu.c"

SHORT MessageProc(void)
{
	SHORT result = 0;
	GfxScreenProj();
	if (menu_code != -1)
	{
		switch (menu_code)
		{
		case 0: result = PauseMenu_Proc();  break;
		case 1: result = PauseMenu_Proc();  break;
		case 2: result = SaveMenu_Proc();   break;
		case 3: result = SaveMenu_Proc();   break;
		}
		msg_theta += 0x1000;
	}
	else if (msg_code != -1)
	{
		if (msg_code == 20)
		{
			OpeningDraw();
			return result;
		}
		MsgProc();
		msg_theta += 0x1000;
	}
	return result;
}
