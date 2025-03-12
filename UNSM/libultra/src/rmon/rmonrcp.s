#include <asm.h>
#include <regdef.h>
#include <PR/rcp.h>

LEAF(__rmonRCPrunning)
	move v0,zero
	lw t0,PHYS_TO_K1(SP_STATUS_REG)
	and t0,SP_STATUS_HALT|SP_STATUS_BROKE
	bnez t0,isHalted
	or v0,1
isHalted:
	j ra
END(__rmonRCPrunning)

LEAF(__rmonIdleRCP)
	li a0,PHYS_TO_K1(SP_DMA_BUSY_REG)
wait4dma:
	lw v0,(a0)
	bnez v0,wait4dma
	li a1,SP_SET_HALT|SP_CLR_INTR_BREAK
	li a0,PHYS_TO_K1(SP_STATUS_REG)
	sw a1,(a0)
awaitIdle:
	li a0,PHYS_TO_K1(SP_STATUS_REG)
	lw v0,(a0)
	and v0,SP_STATUS_HALT|SP_STATUS_BROKE
	beqz v0,awaitIdle
	j ra
END(__rmonIdleRCP)

LEAF(__rmonStepRCP)
	li a0,PHYS_TO_K1(SP_STATUS_REG)
	li a1,SP_CLR_HALT|SP_CLR_BROKE|SP_SET_SSTEP|SP_CLR_INTR_BREAK
	sw a1,(a0)
	b awaitIdle
END(__rmonStepRCP)

LEAF(__rmonRunRCP)
	li a0,PHYS_TO_K1(MI_INTR_MASK_REG)
	li a1,MI_INTR_MASK_SET_SP
	sw a1,(a0)
	li a0,PHYS_TO_K1(SP_STATUS_REG)
	li a1,SP_CLR_HALT|SP_CLR_BROKE|SP_CLR_SSTEP|SP_SET_INTR_BREAK
	sw a1,(a0)
	j ra
END(__rmonRunRCP)
