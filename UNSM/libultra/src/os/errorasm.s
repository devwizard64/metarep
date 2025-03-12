#include <asm.h>
#include <regdef.h>

LEAF(__osError)
	lw t0,__osCommonHandler
	beqz t0,1f
	j t0
1:
	j ra
END(__osError)
