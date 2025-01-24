#include <sm64.h>
#include <PR/leoappli.h>

#define BLK_SIZE_ZONE2          17680

#ifdef DISK

#define ROM_LBA                 560
#define ROM_START               0x40000

#define AUDBUFSIZE              0x60000
#define GFXBUFSIZE              0xA0000

static char *disk_audbuf = (char *)0x80246000;
static char *disk_gfxbuf = (char *)0x80246000 + AUDBUFSIZE;
static u32 disk_lastlba = -1;
static u32 disk_lastxfer = -1;

void DiskInit(void)
{
	leoInitialize(149, 150);
}

static void DiskRead(u32 lba, u32 xfer_blks, void *buff_ptr)
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
		cmd.size = 0;
		leoCommand((void *)&cmd);
		while (cmd.header.status == 0);
	}
	while (cmd.header.status != 1);
}

void DiskWrite(u32 lba, u32 xfer_blks, void *buff_ptr)
{
	volatile LEOCmdWrite cmd;
	cmd.header.command = LEO_COMMAND_WRITE;
	cmd.header.reserve1 = 0;
	cmd.header.control = 0;
	cmd.header.reserve3 = 0;
	cmd.header.status = 0;
	cmd.lba = lba;
	cmd.xfer_blks = xfer_blks;
	cmd.buff_ptr = buff_ptr;
	cmd.size = 0;
	leoCommand((void *)&cmd);
	while (cmd.header.status == 0);
}

/* audio dma */
void disk_8040BAEC(char *dst, const char *start, const char *end)
{
	u32 rom_start = (u32)start - ROM_START;
	u32 lba_start = ROM_LBA + rom_start/BLK_SIZE_ZONE2;
	char *ptr = (char *)((long)disk_audbuf + rom_start%BLK_SIZE_ZONE2);
	unsigned int size = end - start;
	if (size == 0xDE230)
	{
		DiskRead(268, 66, dst);
		return;
	}
	if (size > AUDBUFSIZE) return;
	DiskRead(
		lba_start,
		ROM_LBA + ((u32)end-ROM_START-1)/BLK_SIZE_ZONE2+1 - lba_start,
		disk_audbuf
	);
	bcopy(ptr, dst, size);
}

void MemRead(char *dst, const char *start, const char *end)
{
	u32 rom_start = (u32)start - ROM_START;
	u32 lba_start = ROM_LBA + rom_start/BLK_SIZE_ZONE2;
	char *ptr = (char *)((long)disk_gfxbuf + rom_start%BLK_SIZE_ZONE2);
	unsigned int size = end - start;
	if (size > GFXBUFSIZE) return;
	DiskRead(
		lba_start,
		ROM_LBA + ((u32)end-ROM_START-1)/BLK_SIZE_ZONE2+1 - lba_start,
		disk_gfxbuf
	);
	bcopy(ptr, dst, size);
}

#endif
