union leo_sys_form
{
	struct
	{
		u32 country;
		u8 fmt_type;
		u8 disk_type;
		u16 ipl_load_len;
		u8 defect_num[20];
		void *loadptr;
		u8 defect_data[192];
		u16 rom_end_lba;
		u16 ram_start_lba;
		u16 ram_end_lba;
	}
	param;
	u64 u64_data[232/8];
};

struct tgt_param_form
{
	u16 lba;
	u16 cylinder;
	u16 blk_bytes;
	u8 sec_bytes;
	u8 head;
	u8 zone;
	u8 rdwr_blocks;
	u8 start_block;
};

union data_trans_form
{
	u8 u8_data[4];
	u16 u16_data[2];
	u32 u32_data;
};

struct block_param_form
{
	u8 *pntr;
	u8 *c2buff_e;
	u8 err_pos[4];
	u8 err_num;
	u8 bytes;
	u16 blkbytes;
};

#define LEO_STACKSIZE 1024

#define cmd_hdr         ((LEOCmdHeader *)LEOcur_command)
#define inquiry_cmd     ((LEOCmdInquiry *)LEOcur_command)
#define test_cmd        ((LEOCmdTestUnitReady *)LEOcur_command)
#define rezero_cmd      ((LEOCmdRezero *)LEOcur_command)
#define read_cmd        ((LEOCmdRead *)LEOcur_command)
#define write_cmd       ((LEOCmdWrite *)LEOcur_command)
#define seek_cmd        ((LEOCmdSeek *)LEOcur_command)
#define motor_cmd       ((LEOCmdStartStop *)LEOcur_command)
#define capacity_cmd    ((LEOCmdReadCapacity *)LEOcur_command)
#define translate_cmd   ((LEOCmdTranslate *)LEOcur_command)
#define mode_cmd        ((LEOCmdModeSelect *)LEOcur_command)
#define diskid_cmd      ((LEOCmdReadDiskId *)LEOcur_command)

extern u8 leoChk_cur_drvmode(u32 asic_stat);
extern void leoRead_common(u32 offset);
extern u8 leoChk_asic_ready(u32 asic_cmd, u32 asic_stat);
extern u8 leoChk_done_status(u32 asic_cmd);
extern u8 leoSend_asic_cmd_w(u32 asic_cmd, u32 asic_data);
extern u8 leoDetect_index_w(void);
extern u8 leoRecal_i(void);
extern u8 leoSeek_i(u16 rwmode);
extern int leoC2_Correction(void);
extern u16 leoLba_to_phys(u32 lba);
extern u16 leoLba_to_vzone(u32 lba);
extern void leoSet_mseq(u16 rwmode);

extern const u8 leo_rodata_804B21A8[9];
extern const u8 leo_rodata_804B21B4[9];
extern const u8 leo_rodata_804B21C0[9];
extern const u8 leo_rodata_804B21CC[9];
extern const u8 LEOBYTE_TBL1[9];
extern const u16 LEOBYTE_TBL2[9];
extern const u16 LEOVZONE_TBL[7][16];
extern const u16 LEOZONE_SCYL_TBL[16];
extern const u8 LEOVZONE_PZONEHD_TBL[7][16];
extern const u16 LEOZONE_OUTERCYL_TBL[9-1];
extern const u16 LEORAM_START_LBA[7];
extern const u32 LEORAM_BYTE[7];
extern const u8 leo_rodata_804B23A4[];

extern union leo_sys_form LEO_sys_data;
extern OSThread LEOcommandThread;
extern OSThread LEOinterruptThread;
extern u64 LEOcommandThreadStack[LEO_STACKSIZE/8];
extern u64 LEOinterruptThreadStack[LEO_STACKSIZE/8];
extern OSPri leo_bss_804E21F8;
extern OSPri leo_bss_804E21FC;
extern OSMesgQueue LEOcommand_que;
extern OSMesgQueue LEOevent_que;
extern OSMesgQueue LEOcontrol_que;
extern OSMesgQueue LEOdma_que;
extern OSMesgQueue LEOblock_que;
extern OSMesg LEOcommand_que_buf[8];
extern OSMesg LEOevent_que_buf;
extern OSMesg LEOcontrol_que_buf;
extern OSMesg LEOdma_que_buf[2];
extern OSMesg LEOblock_que_buf;
extern u8 *LEOwrite_pointer;
extern OSMesg LEOcur_command;
extern u32 LEOasic_bm_ctl_shadow;
extern u32 LEOasic_seq_ctl_shadow;
extern u8 LEOdrive_flag;
extern volatile u8 LEOclr_que_flag;
extern u16 LEOrw_flags;
extern u8 LEOdisk_type;
extern struct tgt_param_form LEOtgt_param;
extern union data_trans_form LEO_country_code;
extern OSPiHandle *LEOPiInfo;
extern OSIoMesg LEOPiDmaParam;
extern OSMesgQueue LEOc2ctrl_que;
extern u8 LEO_TempBuffer[240];
extern u8 LEOC2_Syndrome[2][232][4];
extern struct block_param_form LEOc2_param;
