/*
 *  F i l e N a m e  :  l e o a p p l i . h
 *
 ****************************************************************************
 *                   (C) Copyright ALPS Electric Co., Ltd. 1995-1996
 ****************************************************************************
*/

/*-----------------------------------*/
/*   DRIVE PARAMETER                 */
/*-----------------------------------*/
#define  LEO_DISK_TYPE_MIN    0
#define  LEO_DISK_TYPE_MAX    6

#define  LEO_LBA_MIN          0
#define  LEO_LBA_MAX          4291

#define  LEO_LBA_ROM_TOP      LEO_LBA_MIN
#define  LEO_LBA_ROM_END0     1417
#define  LEO_LBA_ROM_END1     1965
#define  LEO_LBA_ROM_END2     2513
#define  LEO_LBA_ROM_END3     3061
#define  LEO_LBA_ROM_END4     3609
#define  LEO_LBA_ROM_END5     4087
#define  LEO_LBA_ROM_END6     LEO_LBA_MAX
#define  LEO_LBA_RAM_TOP0     (LEO_LBA_ROM_END0+1)
#define  LEO_LBA_RAM_TOP1     (LEO_LBA_ROM_END1+1)
#define  LEO_LBA_RAM_TOP2     (LEO_LBA_ROM_END2+1)
#define  LEO_LBA_RAM_TOP3     (LEO_LBA_ROM_END3+1)
#define  LEO_LBA_RAM_TOP4     (LEO_LBA_ROM_END4+1)
#define  LEO_LBA_RAM_TOP5     (LEO_LBA_ROM_END5+1)
#define  LEO_LBA_RAM_TOP6     (LEO_LBA_ROM_END6+1)
#define  LEO_LBA_RAM_END6     LEO_LBA_MAX

/*-----------------------------------*/
/*   LEO FUNCTION DEFINITIONS        */
/*-----------------------------------*/
extern void leoInitialize(OSPri PRI_WRK, OSPri PRI_INT);
extern void leoCommand(void *CDB);
extern void leoReset(void);

/*-----------------------------------*/
/*   THREAD PRIORITY                 */
/*-----------------------------------*/
#define  LEO_PRIORITY_WRK   (OS_PRIORITY_PIMGR-1)
#define  LEO_PRIORITY_INT   OS_PRIORITY_PIMGR

/*-----------------------------------*/
/*   COMMAND CODE                    */
/*-----------------------------------*/
#define LEO_COMMAND_CLEAR_QUE         0x01
#define LEO_COMMAND_INQUIRY           0x02
#define LEO_COMMAND_TEST_UNIT_READY   0x03
#define LEO_COMMAND_REZERO            0x04
#define LEO_COMMAND_READ              0x05
#define LEO_COMMAND_WRITE             0x06
#define LEO_COMMAND_SEEK              0x07
#define LEO_COMMAND_START_STOP        0x08
#define LEO_COMMAND_READ_CAPACITY     0x09
#define LEO_COMMAND_TRANSLATE         0x0a
#define LEO_COMMAND_MODE_SELECT       0x0b
#define LEO_COMMAND_READ_DISK_ID      0x0c

/*-----------------------------------*/
/* CONTROL BIT                       */
/*-----------------------------------*/
#define LEO_CONTROL_POST              0x80   /* ENABLE POST QUEUE */
#define LEO_CONTROL_START             0x01   /* START COMMAND */
#define LEO_CONTROL_STBY              0x02   /* STAND-BY MODE(NOT SLEEP MODE) */
#define LEO_CONTROL_WRT               0x01   /* READ RE-WRITE-ABLE CAPACITY */
#define LEO_CONTROL_TBL               0x01   /* TRANSLATE BYTE TO LBA */

/*-----------------------------------*/
/* BIT FIELD PARAMETER               */
/*-----------------------------------*/
#define LEO_TEST_UNIT_MR              0x01   /* MEDIUM REMOVED */
#define LEO_TEST_UNIT_RE              0x02   /* HEAD RETRACTED */
#define LEO_TEST_UNIT_SS              0x04   /* SPINDLE STOPPED */

/*-----------------------------------*/
/* STATUS                            */
/*-----------------------------------*/
#define LEO_STATUS_GOOD               0x01
#define LEO_STATUS_CHECK_CONDITION    0x02
#define LEO_STATUS_BUSY               0x08

/*-----------------------------------*/
/* SENSE CODE                        */
/*-----------------------------------*/
#define LEO_SENSE_NO_ADDITIONAL_SENSE_INFOMATION   0
#define LEO_SENSE_NO_SEEK_COMPLETE                 2
#define LEO_SENSE_WRITE_FAULT                      3
#define LEO_SENSE_DRIVE_NOT_READY                  4
#define LEO_SENSE_NO_REFERENCE_POSITION_FOUND      6
#define LEO_SENSE_DEVICE_COMMUNICATION_FAILURE     8
#define LEO_SENSE_TRACK_FOLLOWING_ERROR            9
#define LEO_SENSE_UNRECOVERED_READ_ERROR           17
#define LEO_SENSE_INVALID_COMMAND_OPERATION_CODE   32
#define LEO_SENSE_LBA_OUT_OF_RANGE                 33
#define LEO_SENSE_WRITE_PROTECT_ERROR              39
#define LEO_SENSE_MEDIUM_MAY_HAVE_CHANGED          40
#define LEO_SENSE_POWERONRESET_DEVICERESET_OCCURED 41
#define LEO_SENSE_COMMAND_TERMINATED               47
#define LEO_SENSE_INCOMPATIBLE_MEDIUM_INSTALLED    48
#define LEO_SENSE_MEDIUM_NOT_PRESENT               58
#define LEO_SENSE_DIAGNOSTIC_FAILURE               64
#define LEO_SENSE_COMMAND_PHASE_ERROR              74
#define LEO_SENSE_DATA_PHASE_ERROR                 75

/*-----------------------------------*/
/* Command Block Header              */
/*-----------------------------------*/
typedef struct{
    u8    command;
    u8    reserve1;
    u8    control;
    u8    reserve3;
    u8    status;
    u8    sense;
    u8    reserve6;
    u8    reserve7;
} LEOCmdHeader;

/*-----------------------------------*/
/* CLEAR QUEUE(01H) command          */
/*-----------------------------------*/
typedef struct {
    LEOCmdHeader  header;
    OSMesgQueue  *post;
} LEOCmdClearQue;

/*-----------------------------------*/
/* INQUIRY(02H) command              */
/*-----------------------------------*/
typedef struct {
    LEOCmdHeader  header;
    u8            dev_type;
    u8            version;
    u8            dev_num;
    u8            leo_bios_ver;
    u32           reserve5;
    u32           reserve6;
    u32           reserve7;
    OSMesgQueue  *post;
} LEOCmdInquiry;

/*-----------------------------------*/
/* TEST UNIT READY(03H) command      */
/*-----------------------------------*/
typedef struct {
    LEOCmdHeader  header;
    u8            test;
    u8            reserve2;
    u8            reserve3;
    u8            reserve4;
    OSMesgQueue  *post;
} LEOCmdTestUnitReady;

/*-----------------------------------*/
/* REZERO(04H) command               */
/*-----------------------------------*/
typedef struct {
    LEOCmdHeader  header;
    OSMesgQueue  *post;
} LEOCmdRezero;

/*-----------------------------------*/
/* READ(05H) command                 */
/*-----------------------------------*/
typedef struct {
    LEOCmdHeader  header;
    u32           lba;
    u32           xfer_blks;
    void         *buff_ptr;
    u32           rw_bytes;
    OSMesgQueue  *post;
} LEOCmdRead;

/*-----------------------------------*/
/* WRITE(06H) command                */
/*-----------------------------------*/
typedef LEOCmdRead LEOCmdWrite;

/*-----------------------------------*/
/* SEEK(07H) command                 */
/*-----------------------------------*/
typedef struct {
    LEOCmdHeader  header;
    u32           lba;
    OSMesgQueue  *post;
} LEOCmdSeek;

/*-----------------------------------*/
/* START/STOP(08H) command           */
/*-----------------------------------*/
typedef struct {
    LEOCmdHeader  header;
    OSMesgQueue  *post;
} LEOCmdStartStop;

/*-----------------------------------*/
/* READ CAPACITY(09H) command        */
/*-----------------------------------*/
typedef struct {
    LEOCmdHeader  header;
    u32           start_lba;
    u32           end_lba;
    u32           capa_bytes;
    OSMesgQueue  *post;
} LEOCmdReadCapacity;

/*-----------------------------------*/
/* TRANSLATE(0AH) command            */
/*-----------------------------------*/
typedef struct {
    LEOCmdHeader  header;
    u32           start_lba;
    u32           in_param;
    u32           out_param;
    OSMesgQueue  *post;
} LEOCmdTranslate;

/*-----------------------------------*/
/* MODE SELECT(0BH) command          */
/*-----------------------------------*/
typedef struct {
    LEOCmdHeader  header;
    u8            page_code;
    u8            reserve1;
    u8            standby_time;
    u8            sleep_time;
    u8            led_on_time;
    u8            led_off_time;
    u8            reserve18;
    u8            reserve19;
    OSMesgQueue  *post;
} LEOCmdModeSelect;

/*-----------------------------------*/
/* READ DISK ID(0CH) command         */
/*-----------------------------------*/
typedef struct {
    LEOCmdHeader  header;
    void         *buffer_pointer;
    OSMesgQueue  *post;
} LEOCmdReadDiskId;

/*-------end of leoappli.h--------------------------*/


