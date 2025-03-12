#include <sm64.h>

#define MTR_EVENT_VRTC  0x56525443

typedef struct motor8031D998
{
	unsigned char _00;
	unsigned char _01;
	short _02;
	short _04;
}
MOTOR8031D998;

typedef struct motor8031D9B0
{
	short _00;
	short _02;
	short _04;
	short _06;
	short _08;
	short _0A;
	short _0C;
	short _0E;
}
MOTOR8031D9B0;

extern long long motor_stack[MAIN_STACK_LEN];

static OSThread motor_thread;
static OSPfs motor_pfs;
static OSMesg motor_8031D958[1];
static OSMesgQueue motor_8031D960;
static OSMesg motor_mbox[1];
static OSMesgQueue motor_mq;

static int motor_8030CE00 = FALSE;
static int motor_8030CE04 = FALSE;
static int motor_8030CE08 = 0;
static MOTOR8031D998 motor_8031D998[3];
static MOTOR8031D9B0 motor_8031D9B0;
int motor_8030CE0C = 0;

void motor_8024C4A0(void)
{
	osCreateMesgQueue(&motor_8031D960, motor_8031D958, 1);
	osSendMesg(&motor_8031D960, (OSMesg)0, OS_MESG_NOBLOCK);
}

void motor_8024C4E4(void)
{
	OSMesg msg;
	osRecvMesg(&motor_8031D960, &msg, OS_MESG_BLOCK);
}

void motor_8024C510(void)
{
	osSendMesg(&motor_8031D960, (OSMesg)0, OS_MESG_NOBLOCK);
}

static void motor_8024C53C(void)
{
	if (motor_8030CE04)
	{
		motor_8024C4E4();
		if (!osMotorStart(&motor_pfs))  motor_8030CE08 = 0;
		else                            motor_8030CE08++;
		motor_8024C510();
	}
}

static void motor_8024C5A8(void)
{
	if (motor_8030CE04)
	{
		motor_8024C4E4();
		if (!osMotorStop(&motor_pfs))   motor_8030CE08 = 0;
		else                            motor_8030CE08++;
		motor_8024C510();
	}
}

static void motor_8024C614(void)
{
	if (reset_timer > 0)
	{
		motor_8024C5A8();
		return;
	}
	if (motor_8031D9B0._08 > 0)
	{
		motor_8031D9B0._08--;
		motor_8024C53C();
	}
	else if (motor_8031D9B0._04 > 0)
	{
		motor_8031D9B0._04--;
		motor_8031D9B0._02 -= motor_8031D9B0._0E;
		if (motor_8031D9B0._02 < 0) motor_8031D9B0._02 = 0;
		if (motor_8031D9B0._00 == 1)
		{
			motor_8024C53C();
		}
		else if (motor_8031D9B0._06 >= 0x100)
		{
			motor_8031D9B0._06 -= 0x100;
			motor_8024C53C();
		}
		else
		{
			motor_8031D9B0._06 +=
				motor_8031D9B0._02*motor_8031D9B0._02*motor_8031D9B0._02/0x200
				+ 4;
			motor_8024C5A8();
		}
	}
	else
	{
		motor_8031D9B0._04 = 0;
		if (motor_8031D9B0._0A >= 5)
		{
			motor_8024C53C();
		}
		else if (motor_8031D9B0._0A >= 2 && !(vi_count % motor_8031D9B0._0C))
		{
			motor_8024C53C();
		}
		else
		{
			motor_8024C5A8();
		}
	}
	if (motor_8031D9B0._0A > 0) motor_8031D9B0._0A--;
}

static void motor_8024C7AC(void)
{
	if (motor_8031D998[0]._00)
	{
		motor_8031D9B0._06 = 0;
		motor_8031D9B0._08 = 4;
		motor_8031D9B0._00 = motor_8031D998[0]._00;
		motor_8031D9B0._04 = motor_8031D998[0]._02;
		motor_8031D9B0._02 = motor_8031D998[0]._01;
		motor_8031D9B0._0E = motor_8031D998[0]._04;
	}
	motor_8031D998[0] = motor_8031D998[1];
	motor_8031D998[1] = motor_8031D998[2];
	motor_8031D998[2]._00 = 0;
}

void motor_8024C834(SHORT a0, SHORT a1)
{
	if (!demop)
	{
		if (a1 > 70)    motor_8031D998[2]._00 = 1;
		else            motor_8031D998[2]._00 = 2;
		motor_8031D998[2]._01 = a1;
		motor_8031D998[2]._02 = a0;
		motor_8031D998[2]._04 = 0;
	}
}

void motor_8024C89C(SHORT a0)
{
	motor_8031D998[2]._04 = a0;
}

int motor_8024C8AC(void)
{
	if (motor_8031D9B0._08+motor_8031D9B0._04 > 3) return FALSE;
	if (motor_8031D998[0]._00) return FALSE;
	if (motor_8031D998[1]._00) return FALSE;
	if (motor_8031D998[2]._00) return FALSE;
	return TRUE;
}

void motor_8024C924(void)
{
	if (!demop)
	{
		if (motor_8031D9B0._0A == 0) motor_8031D9B0._0A = 7;
		if (motor_8031D9B0._0A <  4) motor_8031D9B0._0A = 4;
		motor_8031D9B0._0C = 7;
	}
}

void motor_8024C974(int a0)
{
	if (!demop)
	{
		if (motor_8031D9B0._0A == 0) motor_8031D9B0._0A = 7;
		if (motor_8031D9B0._0A <  4) motor_8031D9B0._0A = 4;
		if (a0 == 4) motor_8031D9B0._0C = 1;
		if (a0 == 3) motor_8031D9B0._0C = 2;
		if (a0 == 2) motor_8031D9B0._0C = 3;
		if (a0 == 1) motor_8031D9B0._0C = 4;
		if (a0 == 0) motor_8031D9B0._0C = 5;
	}
}

void motor_8024CA04(void)
{
	if (!demop)
	{
		motor_8031D9B0._0A = 4;
		motor_8031D9B0._0C = 4;
	}
}

static void MotorProc(UNUSED void *arg)
{
	motor_8024CB90();
	motor_8030CE00 = TRUE;
	for (;;)
	{
		OSMesg msg;
		osRecvMesg(&motor_mq, &msg, OS_MESG_BLOCK);
		motor_8024C7AC();
		motor_8024C614();
		if (motor_8030CE04)
		{
			if (motor_8030CE08 >= 30) motor_8030CE04 = FALSE;
		}
		else
		{
			if (!(vi_count % 60))
			{
				motor_8030CE04 =
					osMotorInit(&si_mq, &motor_pfs, cont1->port) == 0;
				motor_8030CE08 = 0;
			}
		}
		if (motor_8030CE0C > 0) motor_8030CE0C--;
	}
}

void motor_8024CB90(void)
{
	motor_8030CE04 = osMotorInit(&si_mq, &motor_pfs, cont1->port) == 0;
	if (motor_8030CE04) osMotorStop(&motor_pfs);
	motor_8031D998[0]._00 = 0;
	motor_8031D998[1]._00 = 0;
	motor_8031D998[2]._00 = 0;
	motor_8031D9B0._04 = 0;
	motor_8031D9B0._0A = 0;
	motor_8030CE0C = 0;
}

void motor_8024CC10(void)
{
	osCreateMesgQueue(&motor_mq, motor_mbox, 1);
	osCreateThread(
		&motor_thread, 6, MotorProc, NULL, motor_stack+MAIN_STACK_LEN, 30
	);
	osStartThread(&motor_thread);
}

void motor_8024CC7C(void)
{
	if (motor_8030CE00)
	{
		osSendMesg(&motor_mq, (OSMesg)MTR_EVENT_VRTC, OS_MESG_NOBLOCK);
	}
}
