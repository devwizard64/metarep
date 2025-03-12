#include <sm64.h>

extern BACKUP backup;

#define BU_INFO_KEY 0x4849  /* HI */
#define BU_FILE_KEY 0x4441  /* DA */

typedef struct backupmid
{
	u8 level;
	u8 course;
	u8 stage;
	u8 scene;
	u8 port;
}
BACKUPMID;

static BACKUPMID bu_mid;

static char bu_info_dirty;
static char bu_file_dirty;

u8 bu_course = 0;
u8 bu_level = 0;
u8 bu_hiscore = FALSE;
u8 bu_myscore = FALSE;
u8 bu_star = 0;
u8 bu_jump = FALSE;

char coursetab[] =
{
	COURSE_NULL,
	COURSE_NULL,
	COURSE_NULL,
	COURSE_BBH,
	COURSE_CCM,
	COURSE_NULL,
	COURSE_HMC,
	COURSE_SSL,
	COURSE_BOB,
	COURSE_SL,
	COURSE_WDW,
	COURSE_JRB,
	COURSE_THI,
	COURSE_TTC,
	COURSE_RR,
	COURSE_NULL,
	COURSE_BITDW,
	COURSE_VCUTM,
	COURSE_BITFS,
	COURSE_SA,
	COURSE_BITS,
	COURSE_LLL,
	COURSE_DDD,
	COURSE_WF,
	COURSE_ENDING,
	COURSE_NULL,
	COURSE_PSS,
	COURSE_COTMC,
	COURSE_TOTWC,
	COURSE_BITDW,
	COURSE_WMOTR,
	COURSE_NULL,
	COURSE_BITFS,
	COURSE_BITS,
	COURSE_NULL,
	COURSE_TTM,
	COURSE_NULL,
	COURSE_NULL,
};

static void BuInitDebug(void)
{
	UNUSED int i;
}

#define BU_ADDR(addr)   ((unsigned long)(addr)-(unsigned long)&backup)

#ifdef DISK

#include <PR/leoappli.h>

static int BackupRead(void *data, int size)
{
	char *ptr = (char *)ADDRESS_BACKUP;
	DiskRead(LEO_LBA_RAM_TOP0, 1, ptr);
	bcopy(ptr + BU_ADDR(data), data, size);
	return 1;
}

static int BackupWrite(const void *data, int size)
{
	char *ptr = (char *)ADDRESS_BACKUP;
	bcopy(data, ptr + BU_ADDR(data), size);
	DiskWrite(LEO_LBA_RAM_TOP0, 1, ptr);
	return 1;
}

#else

static int BackupRead(void *data, int size)
{
	int ret = 0;
	if (eeprom_status)
	{
		int n = 4;
		int address = BU_ADDR(data) / 8;
		do
		{
#ifdef MOTOR
			motor_8024C4E4();
#endif
			n--;
			ret = osEepromLongRead(&si_mq, address, data, size);
#ifdef MOTOR
			motor_8024C510();
#endif
		}
		while (n > 0 && ret);
	}
	return ret;
}

static int BackupWrite(const void *data, int size)
{
	int ret = 1;
	if (eeprom_status)
	{
		int n = 4;
		int address = BU_ADDR(data) / 8;
		do
		{
#ifdef MOTOR
			motor_8024C4E4();
#endif
			n--;
			ret = osEepromLongWrite(&si_mq, address, (void *)data, size);
#ifdef MOTOR
			motor_8024C510();
#endif
		}
		while (n > 0 && ret);
	}
	return ret;
}

#endif

static u16 BuCheckSum(unsigned char *data, int size)
{
	USHORT sum = 0;
	while (size-- > 2) sum += *data++;
	return sum;
}

static int BuCheck(void *data, int size, USHORT key)
{
	BUCHECK *check = (BUCHECK *)(size-(int)sizeof(BUCHECK)+(char *)data);
	if (check->key != key) return FALSE;
	if (BuCheckSum(data, size) != check->sum) return FALSE;
	return TRUE;
}

static void BuCheckSet(void *data, int size, USHORT key)
{
	BUCHECK *check = (BUCHECK *)(size-(int)sizeof(BUCHECK)+(char *)data);
	check->key = key;
	check->sum = BuCheckSum(data, size);
}

static void BuInfoRecover(int src)
{
	int dst = src ^ 1;
	BuCheckSet(&backup.info[src], sizeof(BACKUPINFO), BU_INFO_KEY);
	bcopy(&backup.info[src], &backup.info[dst], sizeof(BACKUPINFO));
	BackupWrite(&backup.info[dst], sizeof(BACKUPINFO));
}

static void BuInfoWrite(void)
{
	if (bu_info_dirty)
	{
		BuCheckSet(&backup.info[0], sizeof(BACKUPINFO), BU_INFO_KEY);
		bcopy(&backup.info[0], &backup.info[1], sizeof(BACKUPINFO));
		BackupWrite(&backup.info, sizeof(BACKUPINFO)*2);
		bu_info_dirty = FALSE;
	}
}

static void BuInfoErase(void)
{
	bzero(&backup.info[0], sizeof(BACKUPINFO));
	backup.info[0].time[0] = 0x15555555*3;
	backup.info[0].time[1] = 0x15555555*2;
	backup.info[0].time[2] = 0x15555555*1;
	bu_info_dirty = TRUE;
	BuInfoWrite();
}

static int BuGetTime(int file, int course)
{
	return backup.info[0].time[file] >> 2*course & 3;
}

static void BuSetTime(int file, int course, int time)
{
	unsigned int mask = 3 << (2*course);
	backup.info[0].time[file] &= ~mask;
	backup.info[0].time[file] |= time << (2*course);
}

static void BuUpdateTime(int file, int course)
{
	int i;
	unsigned int t;
	unsigned int time = BuGetTime(file, course);
	if (time > 0)
	{
		for (i = 0; i < 4; i++)
		{
			t = BuGetTime(i, course);
			if (t < time) BuSetTime(i, course, t+1);
		}
		BuSetTime(file, course, 0);
		bu_info_dirty = TRUE;
	}
}

static void BuUpdateTimeAll(int file)
{
	int i;
	for (i = 0; i < 15; i++) BuUpdateTime(file, i);
}

static void BuFileRecover(int file, int src)
{
	int dst = src ^ 1;
	BuCheckSet(&backup.file[file][src], sizeof(BACKUPFILE), BU_FILE_KEY);
	bcopy(&backup.file[file][src], &backup.file[file][dst], sizeof(BACKUPFILE));
	BackupWrite(&backup.file[file][dst], sizeof(BACKUPFILE));
}

void BuFileWrite(int file)
{
	if (bu_file_dirty)
	{
		BuCheckSet(&backup.file[file][0], sizeof(BACKUPFILE), BU_FILE_KEY);
		bcopy(&backup.file[file][0], &backup.file[file][1], sizeof(BACKUPFILE));
		BackupWrite(&backup.file[file], sizeof(BACKUPFILE)*2);
		bu_file_dirty = FALSE;
	}
	BuInfoWrite();
}

void BuFileErase(int file)
{
	BuUpdateTimeAll(file);
	bzero(&backup.file[file][0], sizeof(BACKUPFILE));
	bu_file_dirty = TRUE;
	BuFileWrite(file);
}

VOID BuFileCopy(int src, int dst)
{
	UNUSED int result;
	BuUpdateTimeAll(dst);
	bcopy(&backup.file[src][0], &backup.file[dst][0], sizeof(BACKUPFILE));
	bu_file_dirty = TRUE;
	BuFileWrite(dst);
}

void BackupInit(void)
{
	int i, x;
	bu_info_dirty = FALSE;
	bu_file_dirty = FALSE;
	bzero(&backup, sizeof(BACKUP));
	BackupRead(&backup, sizeof(BACKUP));
	x  = BuCheck(&backup.info[0], sizeof(BACKUPINFO), BU_INFO_KEY)<<0;
	x |= BuCheck(&backup.info[1], sizeof(BACKUPINFO), BU_INFO_KEY)<<1;
	switch (x)
	{
	case FALSE<<0|FALSE<<1: BuInfoErase();    break;
	case TRUE <<0|FALSE<<1: BuInfoRecover(0); break;
	case FALSE<<0|TRUE <<1: BuInfoRecover(1); break;
	}
	for (i = 0; i < 4; i++)
	{
		x  = BuCheck(&backup.file[i][0], sizeof(BACKUPFILE), BU_FILE_KEY)<<0;
		x |= BuCheck(&backup.file[i][1], sizeof(BACKUPFILE), BU_FILE_KEY)<<1;
		switch (x)
		{
		case FALSE<<0|FALSE<<1: BuFileErase(i);       break;
		case TRUE <<0|FALSE<<1: BuFileRecover(i, 0);  break;
		case FALSE<<0|TRUE <<1: BuFileRecover(i, 1);  break;
		}
	}
	BuInitDebug();
}

void BuReset(void)
{
	bcopy(
		&backup.file[file_index-1][1], &backup.file[file_index-1][0],
		sizeof(BACKUPFILE)
	);
	bcopy(&backup.info[1], &backup.info[0], sizeof(BACKUPINFO));
	bu_info_dirty = FALSE;
	bu_file_dirty = FALSE;
}

void BuSet(SHORT coin, SHORT level)
{
	int file = file_index-1;
	int course = course_index-1;
	int mask = 1 << level;
	UNUSED unsigned int flag = BuGetFlag();
	bu_course = course+1;
	bu_level  = level+1;
	bu_hiscore = FALSE;
	bu_myscore = FALSE;
	if (course >= 0 && course < 15)
	{
		if (coin > BuGetHiScoreCoin(course))
		{
			bu_hiscore = TRUE;
		}
		if (BuFileGetCoin(file, course) < coin)
		{
			backup.file[file][0].coin[course] = coin;
			BuUpdateTime(file, course);
			bu_myscore = TRUE;
			bu_file_dirty = TRUE;
		}
	}
	switch (stage_index)
	{
	case STAGE_BITDWA:
		if (!(BuGetFlag() & (BU_KEY1|BU_KEYDOOR1)))
		{
			BuSetFlag(BU_KEY1);
		}
		break;
	case STAGE_BITFSA:
		if (!(BuGetFlag() & (BU_KEY2|BU_KEYDOOR2)))
		{
			BuSetFlag(BU_KEY2);
		}
		break;
	case STAGE_BITSA:
		break;
	default:
		if (!(BuFileGetStar(file, course) & mask))
		{
			BuFileSetStar(file, course, mask);
		}
		break;
	}
}

int BuFileIsActive(int file)
{
	return (backup.file[file][0].flag & BU_ACTIVE) != 0;
}

u32 BuGetHiScore(int course)
{
	int i;
	int max_coin = -1;
	int max_time = -1;
	int file = 0;
	for (i = 0; i < 4; i++)
	{
		if (BuFileGetStar(i, course))
		{
			int coin = BuFileGetCoin(i, course);
			int time = BuGetTime(i, course);
			if (coin > max_coin || (coin == max_coin && time > max_time))
			{
				max_coin = coin;
				max_time = time;
				file = i+1;
			}
		}
	}
	return (file << 16) + MAX(max_coin, 0);
}

int BuFileStarCount(int file, int course)
{
	int i;
	int n = 0;
	UCHAR mask = 1;
	UCHAR star = BuFileGetStar(file, course);
	for (i = 0; i < 7; i++, mask <<= 1) if (star & mask) n++;
	return n;
}

int BuFileStarRange(int file, int min, int max)
{
	int n = 0;
	for (; min <= max; min++) n += BuFileStarCount(file, min);
	return n + BuFileStarCount(file, -1);
}

void BuSetFlag(unsigned int flag)
{
	backup.file[file_index-1][0].flag |= flag|BU_ACTIVE;
	bu_file_dirty = TRUE;
}

void BuClrFlag(unsigned int flag)
{
	backup.file[file_index-1][0].flag &= ~flag;
	backup.file[file_index-1][0].flag |= BU_ACTIVE;
	bu_file_dirty = TRUE;
}

unsigned int BuGetFlag(void)
{
	if (staffp || demop) return 0;
	return backup.file[file_index-1][0].flag;
}

int BuFileGetStar(int file, int course)
{
	int flag;
	if (course == -1)   flag = backup.file[file][0].flag >> 24 & 0x7F;
	else                flag = backup.file[file][0].star[course] & 0x7F;
	return flag;
}

void BuFileSetStar(int file, int course, int flag)
{
	if (course == -1)   backup.file[file][0].flag |= flag << 24;
	else                backup.file[file][0].star[course] |= flag;
	backup.file[file][0].flag |= BU_ACTIVE;
	bu_file_dirty = TRUE;
}

int BuFileGetCoin(int file, int course)
{
	return backup.file[file][0].coin[course];
}

int BuGetCannon(void)
{
	return (backup.file[file_index-1][0].star[course_index] & 0x80) != 0;
}

void BuSetCannon(void)
{
	backup.file[file_index-1][0].star[course_index] |= 0x80;
	backup.file[file_index-1][0].flag |= BU_ACTIVE;
	bu_file_dirty = TRUE;
}

void BuSetCap(SHORT x, SHORT y, SHORT z)
{
	BACKUPFILE *file = &backup.file[file_index-1][0];
	file->stage = stage_index;
	file->scene = scene_index;
	SVecSet(file->pos, x, y, z);
	BuSetFlag(BU_LOSTCAP);
}

int BuGetCap(SVEC pos)
{
	BACKUPFILE *file = &backup.file[file_index-1][0];
	unsigned int flag = BuGetFlag();
	if (
		file->stage == stage_index &&
		file->scene == scene_index &&
		(flag & BU_LOSTCAP)
	)
	{
		SVecCpy(pos, file->pos);
		return TRUE;
	}
	return FALSE;
}

void BuSetSound(USHORT sound)
{
	AudSetMode(sound);
	backup.info[0].sound = sound;
	bu_info_dirty = TRUE;
	BuInfoWrite();
}

USHORT BuGetSound(void)
{
	return backup.info[0].sound;
}

void BuInitCap(void)
{
	if (BuGetFlag() & BU_LOSTCAP)
	{
		switch (backup.file[file_index-1][0].stage)
		{
		case STAGE_SSL: BuSetFlag(BU_CONDORCAP);    break;
		case STAGE_SL:  BuSetFlag(BU_SNOWMANCAP);   break;
		case STAGE_TTM: BuSetFlag(BU_MONKEYCAP);    break;
		}
		BuClrFlag(BU_LOSTCAP);
	}
}

#ifdef MULTILANG
void BuSetLang(USHORT lang)
{
	backup.info[0].lang = lang;
	bu_info_dirty = TRUE;
	BuInfoWrite();
}

USHORT BuGetLang(void)
{
	return backup.info[0].lang;
}
#endif

void BuClrMid(void)
{
	bu_mid.course = COURSE_NULL;
}

void BuSetMid(PORTINFO *p)
{
	if (p->stage & 0x80)
	{
		bu_mid.level  = level_index;
		bu_mid.course = course_index;
		bu_mid.stage  = p->stage & 0x7F;
		bu_mid.scene  = p->scene;
		bu_mid.port   = p->port;
	}
}

int BuGetMid(PORTINFO *p)
{
	short result = FALSE;
	SHORT course = StageToCourse(p->stage & 0x7F);
	if (
		bu_mid.course != COURSE_NULL &&
		prev_course == course &&
		bu_mid.level == level_index
	)
	{
		p->stage = bu_mid.stage;
		p->scene = bu_mid.scene;
		p->port  = bu_mid.port;
		result = TRUE;
	}
	else
	{
		bu_mid.course = COURSE_NULL;
	}
	return result;
}
