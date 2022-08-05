#include <sm64/types.h>
#include <sm64/main.h>
#include <sm64/app.h>
#include <sm64/audio.h>
#include <sm64/save.h>
#include <sm64/scene.h>
#include <sm64/math.h>
#include <sm64/buffer.h>

#include ASSET(data/main/course.inc.h)

#define SAVE_DATA_KEY   0x4849  /* HI */
#define SAVE_FILE_KEY   0x4441  /* DA */

u8 save_mid_level;
u8 save_mid_course;
u8 save_mid_stage;
u8 save_mid_scene;
u8 save_mid_link;
s8 save_data_dirty;
s8 save_file_dirty;

u8 save_course  = 0;
u8 save_level   = 0;
u8 save_hiscore = FALSE;
u8 save_myscore = FALSE;
u8 save_star    = 0;
u8 save_jump    = FALSE;

s8 course_table[] =
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

static void save_init_debug(void)
{
    UNUSED int i;
}

static int save_rd(void *data, int size)
{
    int code = 0;
    if (eeprom_status != 0)
    {
        int n = 4;
        int address = ((uintptr_t)data-(uintptr_t)&save) / 8;
        do
        {
            n--;
            code = osEepromLongRead(&si_mq, address, data, size);
        }
        while (n > 0 && code != 0);
    }
    return code;
}

static int save_wr(const void *data, int size)
{
    int code = 1;
    if (eeprom_status != 0)
    {
        int n = 4;
        int address = ((uintptr_t)data-(uintptr_t)&save) / 8;
        do
        {
            n--;
            code = osEepromLongWrite(&si_mq, address, (void *)data, size);
        }
        while (n > 0 && code != 0);
    }
    return code;
}

static USHORT save_check_sum(const u8 *data, int size)
{
    USHORT sum = 0;
    while (size-- > 2) sum += *data++;
    return (u16)sum;
}

static int save_check(const void *data, int size, USHORT key)
{
    SAVE_CHECK *check = (SAVE_CHECK *)((size-sizeof(SAVE_CHECK))+(char *)data);
    if (check->key != key) return FALSE;
    if (save_check_sum(data, size) != check->sum) return FALSE;
    return TRUE;
}

static void save_check_set(void *data, int size, USHORT key)
{
    SAVE_CHECK *check = (SAVE_CHECK *)((size-sizeof(SAVE_CHECK))+(char *)data);
    check->key = key;
    check->sum = save_check_sum(data, size);
}

static void save_data_recover(int src)
{
    int dst = src ^ 1;
    save_check_set(&save.data[src], sizeof(SAVE_DATA), SAVE_DATA_KEY);
    bcopy(&save.data[src], &save.data[dst], sizeof(SAVE_DATA));
    save_wr(&save.data[dst], sizeof(SAVE_DATA));
}

static void save_data_write(void)
{
    if (save_data_dirty)
    {
        save_check_set(&save.data[0], sizeof(SAVE_DATA), SAVE_DATA_KEY);
        bcopy(&save.data[0], &save.data[1], sizeof(SAVE_DATA));
        save_wr(&save.data, sizeof(SAVE_DATA)*2);
        save_data_dirty = FALSE;
    }
}

static void save_data_erase(void)
{
    bzero(&save.data[0], sizeof(SAVE_DATA));
    save.data[0].time[0] = 0x15555555*3;
    save.data[0].time[1] = 0x15555555*2;
    save.data[0].time[2] = 0x15555555*1;
    save_data_dirty = TRUE;
    save_data_write();
}

static uint save_time_get(int file, int course)
{
    return save.data[0].time[file] >> (2*course) & 3;
}

static void save_time_set(int file, int course, uint time)
{
    uint mask = 3 << (2*course);
    save.data[0].time[file] &= ~mask;
    save.data[0].time[file] |= time << (2*course);
}

static void save_time_update(int file, int course)
{
    int i;
    uint t;
    uint time = save_time_get(file, course);
    if (time > 0)
    {
        for (i = 0; i < 4; i++)
        {
            t = save_time_get(i, course);
            if (t < time) save_time_set(i, course, t+1);
        }
        save_time_set(file, course, 0);
        save_data_dirty = TRUE;
    }
}

static void save_time_update_all(int file)
{
    int i;
    for (i = 0; i < 15; i++) save_time_update(file, i);
}

static void save_file_recover(int file, int src)
{
    int dst = src ^ 1;
    save_check_set(&save.file[file][src], sizeof(SAVE_FILE), SAVE_FILE_KEY);
    bcopy(&save.file[file][src], &save.file[file][dst], sizeof(SAVE_FILE));
    save_wr(&save.file[file][dst], sizeof(SAVE_FILE));
}

void save_file_write(int file)
{
    if (save_file_dirty)
    {
        save_check_set(&save.file[file][0], sizeof(SAVE_FILE), SAVE_FILE_KEY);
        bcopy(&save.file[file][0], &save.file[file][1], sizeof(SAVE_FILE));
        save_wr(&save.file[file], sizeof(SAVE_FILE)*2);
        save_file_dirty = FALSE;
    }
    save_data_write();
}

void save_file_erase(int file)
{
    save_time_update_all(file);
    bzero(&save.file[file][0], sizeof(SAVE_FILE));
    save_file_dirty = TRUE;
    save_file_write(file);
}

void save_file_copy(int src, int dst)
{
    UNUSED int i;
    save_time_update_all(dst);
    bcopy(&save.file[src][0], &save.file[dst][0], sizeof(SAVE_FILE));
    save_file_dirty = TRUE;
    save_file_write(dst);
}

void save_init(void)
{
    int i;
    int x;
    save_data_dirty = FALSE;
    save_file_dirty = FALSE;
    bzero(&save, sizeof(SAVE));
    save_rd(&save, sizeof(SAVE));
    x  = save_check(&save.data[0], sizeof(SAVE_DATA), SAVE_DATA_KEY)<<0;
    x |= save_check(&save.data[1], sizeof(SAVE_DATA), SAVE_DATA_KEY)<<1;
    switch (x)
    {
        case FALSE<<0 | FALSE<<1: save_data_erase();       break;
        case TRUE <<0 | FALSE<<1: save_data_recover(0);    break;
        case FALSE<<0 | TRUE <<1: save_data_recover(1);    break;
    }
    for (i = 0; i < 4; i++)
    {
        x  = save_check(&save.file[i][0], sizeof(SAVE_FILE), SAVE_FILE_KEY)<<0;
        x |= save_check(&save.file[i][1], sizeof(SAVE_FILE), SAVE_FILE_KEY)<<1;
        switch (x)
        {
            case FALSE<<0 | FALSE<<1: save_file_erase(i);       break;
            case TRUE <<0 | FALSE<<1: save_file_recover(i, 0);  break;
            case FALSE<<0 | TRUE <<1: save_file_recover(i, 1);  break;
        }
    }
    save_init_debug();
}

void save_reset(void)
{
    bcopy(
        &save.file[save_index-1][1], &save.file[save_index-1][0],
        sizeof(SAVE_FILE)
    );
    bcopy(&save.data[1], &save.data[0], sizeof(SAVE_DATA));
    save_data_dirty = FALSE;
    save_file_dirty = FALSE;
}

void save_set(SHORT coin, SHORT level)
{
    int file = save_index-1;
    int course = course_index-1;
    uint mask = 1 << level;
    UNUSED uint flag = save_flag_get();
    save_course = course+1;
    save_level  = level+1;
    save_hiscore = FALSE;
    save_myscore = FALSE;
    if (course >= 0 && course < 15)
    {
        if (coin > (u16)(save_hiscore_get(course) & 0xFFFF))
        {
            save_hiscore = TRUE;
        }
        if (save_file_coin_get(file, course) < coin)
        {
            save.file[file][0].coin[course] = coin;
            save_time_update(file, course);
            save_myscore = TRUE;
            save_file_dirty = TRUE;
        }
    }
    switch (stage_index)
    {
        case STAGE_BITDWA:
            if (!(save_flag_get() & (SAVE_000010|SAVE_000040)))
            {
                save_flag_set(SAVE_000010);
            }
            break;
        case STAGE_BITFSA:
            if (!(save_flag_get() & (SAVE_000020|SAVE_000080)))
            {
                save_flag_set(SAVE_000020);
            }
            break;
        case STAGE_BITSA:
            break;
        default:
            if (!(save_file_star_get(file, course) & mask))
            {
                save_file_star_set(file, course, mask);
            }
            break;
    }
}

int save_file_isactive(int file)
{
    return (save.file[file][0].flag & SAVE_ACTIVE) != 0;
}

int save_hiscore_get(int course)
{
    int i;
    int max_coin = -1;
    int max_time = -1;
    int file = 0;
    for (i = 0; i < 4; i++)
    {
        if (save_file_star_get(i, course) != 0)
        {
            int coin = save_file_coin_get(i, course);
            int time = save_time_get(i, course);
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

int save_file_star_count(int file, int course)
{
    int i;
    int n = 0;
    u8 mask = 1;
    u8 star = save_file_star_get(file, course);
    for (i = 0; i < 7; i++, mask <<= 1) if (star & mask) n++;
    return n;
}

int save_file_star_range(int file, int min, int max)
{
    int n = 0;
    for (; min <= max; min++) n += save_file_star_count(file, min);
    return n + save_file_star_count(file, -1);
}

void save_flag_set(uint flag)
{
    save.file[save_index-1][0].flag |= SAVE_ACTIVE | flag;
    save_file_dirty = TRUE;
}

void save_flag_clr(uint flag)
{
    save.file[save_index-1][0].flag &= ~flag;
    save.file[save_index-1][0].flag |= SAVE_ACTIVE;
    save_file_dirty = TRUE;
}

uint save_flag_get(void)
{
    if (staff != NULL || demo != NULL) return 0;
    return save.file[save_index-1][0].flag;
}

uint save_file_star_get(int file, int course)
{
    uint flag;
    if (course == -1)   flag = save.file[file][0].flag >> 24 & 0x7F;
    else                flag = save.file[file][0].star[course] & 0x7F;
    return flag;
}

void save_file_star_set(int file, int course, uint flag)
{
    if (course == -1)   save.file[file][0].flag |= flag << 24;
    else                save.file[file][0].star[course] |= flag;
    save.file[file][0].flag |= SAVE_ACTIVE;
    save_file_dirty = TRUE;
}

int save_file_coin_get(int file, int course)
{
    return save.file[file][0].coin[course];
}

int save_cannon_get(void)
{
    return (save.file[save_index-1][0].star[course_index] & 0x80) != 0;
}

void save_cannon_set(void)
{
    save.file[save_index-1][0].star[course_index] |= 0x80;
    save.file[save_index-1][0].flag |= SAVE_ACTIVE;
    save_file_dirty = TRUE;
}

void save_cap_set(SHORT x, SHORT y, SHORT z)
{
    SAVE_FILE *file = &save.file[save_index-1][0];
    file->stage = stage_index;
    file->scene = scene_index;
    vecs_set(file->pos, x, y, z);
    save_flag_set(SAVE_010000);
}

int save_cap_get(VECS pos)
{
    SAVE_FILE *file = &save.file[save_index-1][0];
    uint flag = save_flag_get();
    if (
        file->stage == stage_index &&
        file->scene == scene_index &&
        (flag & SAVE_010000)
    )
    {
        vecs_cpy(pos, file->pos);
        return TRUE;
    }
    return FALSE;
}

void save_output_set(USHORT output)
{
    audio_output(output);
    save.data[0].output = output;
    save_data_dirty = TRUE;
    save_data_write();
}

USHORT save_output_get(void)
{
    return save.data[0].output;
}

void save_cap_init(void)
{
    if (save_flag_get() & SAVE_010000)
    {
        switch (save.file[save_index-1][0].stage)
        {
            case STAGE_SSL: save_flag_set(SAVE_020000); break;
            case STAGE_SL:  save_flag_set(SAVE_080000); break;
            case STAGE_TTM: save_flag_set(SAVE_040000); break;
        }
        save_flag_clr(SAVE_010000);
    }
}

void save_mid_clear(void)
{
    save_mid_course = 0;
}

void save_mid_set(const LINK *link)
{
    if (link->stage & 0x80)
    {
        save_mid_level  = level_index;
        save_mid_course = course_index;
        save_mid_stage  = link->stage & 0x7F;
        save_mid_scene  = link->scene;
        save_mid_link   = link->link;
    }
}

int save_mid_get(LINK *link)
{
    SHORT flag = FALSE;
    SHORT course = stage_to_course(link->stage & 0x7F);
    if (
        save_mid_course != 0 &&
        course_prev == course &&
        save_mid_level == level_index
    )
    {
        link->stage = save_mid_stage;
        link->scene = save_mid_scene;
        link->link  = save_mid_link;
        flag = TRUE;
    }
    else
    {
        save_mid_course = 0;
    }
    return flag;
}
