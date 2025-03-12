#include <ultra64.h>
#include "leoint.h"

union leo_sys_form LEO_sys_data;
OSThread LEOcommandThread;
OSThread LEOinterruptThread;
u64 LEOcommandThreadStack[LEO_STACKSIZE/8];
u64 LEOinterruptThreadStack[LEO_STACKSIZE/8];
OSPri leo_bss_804E21F8;
OSPri leo_bss_804E21FC;
OSMesgQueue LEOcommand_que;
OSMesgQueue LEOevent_que;
OSMesgQueue LEOcontrol_que;
OSMesgQueue LEOdma_que;
OSMesgQueue LEOblock_que;
OSMesg LEOcommand_que_buf[8];
OSMesg LEOevent_que_buf;
OSMesg LEOcontrol_que_buf;
OSMesg LEOdma_que_buf[2];
OSMesg LEOblock_que_buf;
u8 *LEOwrite_pointer;
OSMesg LEOcur_command;
u32 LEOasic_bm_ctl_shadow;
u32 LEOasic_seq_ctl_shadow;
u8 LEOdrive_flag;
volatile u8 LEOclr_que_flag;
u16 LEOrw_flags;
u8 LEOdisk_type;
struct tgt_param_form LEOtgt_param;
union data_trans_form LEO_country_code;
