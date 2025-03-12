#include <asm.h>
#include <regdef.h>

.set noreorder

LEAF(__assertBreak)
	break 0
	j ra
END(__assertBreak)
