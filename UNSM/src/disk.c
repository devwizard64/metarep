#include <sm64.h>
#include <sm64/defdisk.h>
#include <PR/leoappli.h>

#define BLK_SIZE_ZONE2          17680

#ifdef DISK

#define AUDBUFSIZE              0x60000
#define GFXBUFSIZE              0xA0000

static char *disk_audbuf = (char *)ADDRESS_DISK;
static char *disk_gfxbuf = (char *)ADDRESS_DISK + AUDBUFSIZE;
static u32 disk_lastlba = -1;
static u32 disk_lastxfer = -1;

void DiskInit(void)
{
	leoInitialize(LEO_PRIORITY_WRK, LEO_PRIORITY_INT);
}

void DiskRead(u32 lba, u32 xfer_blks, void *buff_ptr)
{
	volatile LEOCmdRead cmd;
	if (lba == disk_lastlba && xfer_blks <= disk_lastxfer) return;
	do
	{
		cmd.header.command = LEO_COMMAND_READ;
		cmd.header.reserve1 = 0;
		cmd.header.control = 0;
		cmd.header.reserve3 = 0;
		cmd.header.status = 0;
		cmd.lba = lba;
		cmd.xfer_blks = xfer_blks;
		cmd.buff_ptr = buff_ptr;
		disk_lastlba = lba;
		disk_lastxfer = xfer_blks;
		cmd.post = NULL;
		leoCommand((void *)&cmd);
		while (!cmd.header.status);
	}
	while (cmd.header.status != LEO_STATUS_GOOD);
}

void DiskWrite(u32 lba, u32 xfer_blks, const void *buff_ptr)
{
	volatile LEOCmdWrite cmd;
	cmd.header.command = LEO_COMMAND_WRITE;
	cmd.header.reserve1 = 0;
	cmd.header.control = 0;
	cmd.header.reserve3 = 0;
	cmd.header.status = 0;
	cmd.lba = lba;
	cmd.xfer_blks = xfer_blks;
	cmd.buff_ptr = (void *)buff_ptr;
	cmd.post = NULL;
	leoCommand((void *)&cmd);
	while (!cmd.header.status);
}

/* audio dma */
void disk_8040BAEC(char *dst, const char *start, const char *end)
{
	u32 rom = (u32)start - ROM_START;
	u32 lba = ROM_LBA + rom/BLK_SIZE_ZONE2;
	char *src = (char *)((long)disk_audbuf + rom%BLK_SIZE_ZONE2);
	unsigned int size = end - start;
	if (size == WAVE_SIZE)
	{
		DiskRead(WAVE_LBA, WAVE_LEN, dst);
		return;
	}
	if (size > AUDBUFSIZE) return;
	DiskRead(
		lba, ROM_LBA+((u32)end-ROM_START-1)/BLK_SIZE_ZONE2+1 - lba, disk_audbuf
	);
	bcopy(src, dst, size);
}

void RomRead(char *dst, const char *start, const char *end)
{
	u32 rom = (u32)start - ROM_START;
	u32 lba = ROM_LBA + rom/BLK_SIZE_ZONE2;
	char *src = (char *)((long)disk_gfxbuf + rom%BLK_SIZE_ZONE2);
	unsigned int size = end - start;
	if (size > GFXBUFSIZE) return;
	DiskRead(
		lba, ROM_LBA+((u32)end-ROM_START-1)/BLK_SIZE_ZONE2+1 - lba, disk_gfxbuf
	);
	bcopy(src, dst, size);
}

#endif
