#include <asm.h>
#include <regdef.h>
#include <sys/fpu.h>
#include <PR/R4300.h>
#include <PR/rcp.h>
#include <PR/os.h>
#include <PR/rdb.h>

#include "exceptasm.h"
#include "threadasm.h"

#define RCP_INTMASK (RCP_IMASK >> RCP_IMASKSHIFT)

.rdata

__osIntOffTable:
	.byte 4*0,4*5,4*6,4*6,4*7,4*7,4*7,4*7
	.byte 4*8,4*8,4*8,4*8,4*8,4*8,4*8,4*8
	.byte 4*0,4*1,4*2,4*2,4*3,4*3,4*3,4*3
	.byte 4*4,4*4,4*4,4*4,4*4,4*4,4*4,4*4

__osIntTable:
	.word redispatch
	.word sw1
	.word sw2
	.word rcp
	.word cart
	.word prenmi
#if REVISION >= 199611
	.word IP6_Hdlr
	.word IP7_Hdlr
#else
	.word panic
	.word panic
#endif
	.word counter

.data

.globl __osHwIntTable
__osHwIntTable:
	.word 0
	.word 0
	.word 0
	.word 0
	.word 0

#if REVISION >= 199611

#ifndef _FINALROM

__osRdb_DbgRead_Ct:
	.word 0

__osRdb_Mesg:
	.word 0

__os_Kdebug_Pkt:
	.word 0

#endif

#else

__osIsRdbWrite:
	.word 0

__osIsRdbRead:
	.word 0

#endif

.text

.set noreorder
.set noat

LEAF(__osExceptionPreamble)
	la k0,__osException
	j k0
	nop
END(__osExceptionPreamble)

LEAF(__osException)
	la k0,__osThreadSave

	sd AT,T_CONTEXT_AT(k0)
.set at

	mfc0 k1,C0_SR
	sw k1,T_CONTEXT_SR(k0)
	and k1,~(SR_EXL|SR_IE)
	mtc0 k1,C0_SR

	sd t0,T_CONTEXT_T0(k0)
	sd t1,T_CONTEXT_T1(k0)
	sd t2,T_CONTEXT_T2(k0)
	sw zero,T_FP(k0)
	mfc0 t0,C0_CAUSE

.set reorder

#if REVISION >= 199611

#ifndef _FINALROM
	and t1,t0,CAUSE_EXCMASK
	li t2,EXC_INT
	bne t1,t2,savecontext

	and t1,k1,t0
	and t2,t1,CAUSE_IP7
	beqz t2,notIP7

	la t1,RDB_WRITE_INTR_REG
	sw zero,(t1)

IP7check:
.set noreorder
	mfc0 t0,C0_CAUSE
.set reorder
	and t0,CAUSE_IP7
	bne zero,t0,IP7check

	la t2,RDB_BASE_REG
	lw t0,(t2)
	srl t1,t0,26
	and t1,0x3F
	li t2,RDB_TYPE_HtoG_DATA
	beq t1,t2,HandData
	li t2,RDB_TYPE_HtoG_DEBUG
	beq t1,t2,HandDbg
	li t2,RDB_TYPE_HtoG_KDEBUG
	beq t1,t2,HandKDebug
	li t2,RDB_TYPE_HtoG_DEBUG_CT
	beq t1,t2,DbgCnt
	li t2,RDB_TYPE_HtoG_DATA_DONE
	beq t1,t2,DataRead
	li t2,RDB_TYPE_HtoG_LOG_DONE
	beq t1,t2,LogRead
	li t2,RDB_TYPE_HtoG_REQ_RAMROM
	beq t1,t2,ReqRamrom
	li t2,RDB_TYPE_HtoG_FREE_RAMROM
	beq t1,t2,FreeRamrom
	li t2,RDB_TYPE_HtoG_PROF_SIGNAL
	beq t1,t2,SignalProf
	b rdbout

SignalProf:
	li t2,RDB_PROF_ACK_SIG
	srl t1,t0,16
	and t1,0xFF
	beq t1,t2,AckProf
	li t2,ES_SIZE*OS_EVENT_RDB_FLUSH_PROF
	sw t2,__osRdb_Mesg
	b savecontext
AckProf:
	li t2,ES_SIZE*OS_EVENT_RDB_ACK_PROF
	sw t2,__osRdb_Mesg
	b savecontext

HandKDebug:
	sw t0,__os_Kdebug_Pkt
	b savecontext

DbgCnt:
	li t2,0xFFFFFF
	and t1,t0,t2
	sw t1,__osRdb_DbgRead_Ct
	b rdbout

DataRead:
	li t2,ES_SIZE*OS_EVENT_RDB_DATA_DONE
	sw t2,__osRdb_Mesg
	b savecontext

LogRead:
	li t2,ES_SIZE*OS_EVENT_RDB_LOG_DONE
	sw t2,__osRdb_Mesg
	b savecontext

ReqRamrom:
	li t2,ES_SIZE*OS_EVENT_RDB_REQ_RAMROM
	sw t2,__osRdb_Mesg
	b savecontext

FreeRamrom:
	li t2,ES_SIZE*OS_EVENT_RDB_FREE_RAMROM
	sw t2,__osRdb_Mesg
	b savecontext

HandData:
	srl t1,t0,24
	and t1,0x3
	beq zero,t1,rdbout
	lw t2,__osRdb_Read_Data_Ct
	subu t2,t1
	sw t2,__osRdb_Read_Data_Ct
	sd t3,T_CONTEXT_T3(k0)
	lw t3,__osRdb_Read_Data_Buf
	srl t2,t0,16
	and t2,0xFF
	sb t2,(t3)
	add t3,1
	sub t1,1
	beq zero,t1,doneData
	srl t2,t0,8
	and t2,0xFF
	sb t2,(t3)
	add t3,1
	sub t1,1
	beq zero,t1,doneData
	and t0,0xFF
	sb t0,(t3)
	add t3,1
doneData:
	sw t3,__osRdb_Read_Data_Buf
	ld t3,T_CONTEXT_T3(k0)
	lw t2,__osRdb_Read_Data_Ct
	bne zero,t2,rdbout
	li t2,ES_SIZE*OS_EVENT_RDB_READ_DONE
	sw t2,__osRdb_Mesg
	b savecontext

HandDbg:
	srl t1,t0,24
	and t1,0x3
	beq zero,t1,rdbout
	lw t2,__osRdb_DbgRead_Ct
	subu t2,t1
	sw t2,__osRdb_DbgRead_Ct
	sd t3,T_CONTEXT_T3(k0)
	lw t3,__osRdb_DbgRead_Buf
	bne zero,t3,1f
	ld t3,T_CONTEXT_T3(k0)
	b rdbout
1:
	srl t2,t0,16
	and t2,0xFF
	sb t2,(t3)
	add t3,1
	sub t1,1
	beq zero,t1,doneDbg
	srl t2,t0,8
	and t2,0xFF
	sb t2,(t3)
	add t3,1
	sub t1,1
	beq zero,t1,doneDbg
	and t0,0xFF
	sb t0,(t3)
	add t3,1
doneDbg:
	sw t3,__osRdb_DbgRead_Buf
	ld t3,T_CONTEXT_T3(k0) 
	lw t2,__osRdb_DbgRead_Ct
	bne zero,t2,rdbout
	li t2,ES_SIZE*OS_EVENT_RDB_DBG_DONE
	sw t2,__osRdb_Mesg
	b savecontext

notIP7:
	and t2,t1,CAUSE_IP6
	beqz t2,savecontext
	la t1,RDB_READ_INTR_REG
	sw zero,(t1)
	lw t2,__osRdb_IP6_Ct
	bnez t2,2f
	li t2,1
	sw t2,__osRdb_IP6_Empty
	b rdbout
2:
	sub t2,1
	sw t2,__osRdb_IP6_Ct
	lw t0,__osRdb_IP6_Data
	lw t1,__osRdb_IP6_CurSend
	sll t2,t1,2
	add t0,t2,t0
	lw t2,(t0)
	add t1,1
	lw t0,__osRdb_IP6_Size
	sub t0,t1
	bgtz t0,5f
	li t1,0
5:
	sw t1,__osRdb_IP6_CurSend

checkIP6:
.set noreorder
	mfc0 t0,C0_CAUSE
.set reorder
	and t0,CAUSE_IP6
	bne zero,t0,checkIP6
	la t0,RDB_BASE_REG
	sw t2,(t0)

rdbout:
.set noreorder
	ld t0,T_CONTEXT_T0(k0)
	ld t1,T_CONTEXT_T1(k0)
	ld t2,T_CONTEXT_T2(k0)
.set noat
	ld AT,T_CONTEXT_AT(k0)
.set at
	lw k1,T_CONTEXT_SR(k0)
	mtc0 k1,C0_SR
	nop
	nop
	nop
	nop
	eret
.set reorder

#endif

#else

	and t1,t0,CAUSE_EXCMASK
	li t2,EXC_INT
	bne t1,t2,savecontext

	and t1,k1,t0
	and t2,t1,CAUSE_IP7
	beqz t2,notIP7

	li t1,1
	sw t1,__osIsRdbWrite
	b 3f

notIP7:
	and t2,t1,CAUSE_IP6
	beqz t2,savecontext

	li t1,1
	sw t1,__osIsRdbRead
	b 3f

#endif

savecontext:

#if REVISION < 199611
	sw zero,__osIsRdbWrite
	sw zero,__osIsRdbRead
#endif

	move t0,k0
	lw k0,__osRunningThread

	ld t1,T_CONTEXT_AT(t0)
	sd t1,T_CONTEXT_AT(k0)
	ld t1,T_CONTEXT_SR(t0)
	sd t1,T_CONTEXT_SR(k0)
	ld t1,T_CONTEXT_T0(t0)
	sd t1,T_CONTEXT_T0(k0)
	ld t1,T_CONTEXT_T1(t0)
	sd t1,T_CONTEXT_T1(k0)
	ld t1,T_CONTEXT_T2(t0)
	sd t1,T_CONTEXT_T2(k0)
3:

	sd v0,T_CONTEXT_V0(k0)
	sd v1,T_CONTEXT_V1(k0)
	sd a0,T_CONTEXT_A0(k0)
	sd a1,T_CONTEXT_A1(k0)
	sd a2,T_CONTEXT_A2(k0)
	sd a3,T_CONTEXT_A3(k0)
	sd t3,T_CONTEXT_T3(k0)
	sd t4,T_CONTEXT_T4(k0)
	sd t5,T_CONTEXT_T5(k0)
	sd t6,T_CONTEXT_T6(k0)
	sd t7,T_CONTEXT_T7(k0)
	sd s0,T_CONTEXT_S0(k0)
	sd s1,T_CONTEXT_S1(k0)
	sd s2,T_CONTEXT_S2(k0)
	sd s3,T_CONTEXT_S3(k0)
	sd s4,T_CONTEXT_S4(k0)
	sd s5,T_CONTEXT_S5(k0)
	sd s6,T_CONTEXT_S6(k0)
	sd s7,T_CONTEXT_S7(k0)
	sd t8,T_CONTEXT_T8(k0)
	sd t9,T_CONTEXT_T9(k0)
	sd gp,T_CONTEXT_GP(k0)
	sd sp,T_CONTEXT_SP(k0)
	sd s8,T_CONTEXT_S8(k0)
	sd ra,T_CONTEXT_RA(k0)
	mflo t0
	sd t0,T_CONTEXT_LO(k0)
	mfhi t0
	sd t0,T_CONTEXT_HI(k0)

#if REVISION >= 199611
	lw k1,T_CONTEXT_SR(k0)
	and t1,k1,SR_IMASK
	beqz t1,savercp
	la t0,__OSGlobalIntMask
	lw t0,(t0)
#if REVISION >= 199707
	xor t2,t0,~0
	and t2,SR_IMASK
	or t4,t1,t2
	and t3,k1,~SR_IMASK
	and t0,SR_IMASK
	or t3,t4
	and t1,t0
	and k1,~SR_IMASK
	sw t3,T_CONTEXT_SR(k0)
	or k1,t1
#else
	xor t0,~0
	and t0,SR_IMASK
	or t1,t0
	and k1,~SR_IMASK
	or k1,t1
	sw k1,T_CONTEXT_SR(k0)
#endif

savercp:
	lw t1,PHYS_TO_K1(MI_INTR_MASK_REG)
	beqz t1,endrcp
	la t0,__OSGlobalIntMask
	lw t0,(t0)
	srl t0,RCP_IMASKSHIFT
	xor t0,~0
	and t0,RCP_INTMASK
	lw t4,T_CONTEXT_RCP(k0)
	and t0,t4
	or t1,t0
endrcp:
	sw t1,T_CONTEXT_RCP(k0)
#endif

.set noreorder

	mfc0 t0,C0_EPC
	sw t0,T_CONTEXT_PC(k0)

	lw t0,T_FP(k0)
	beqz t0,1f
	nop

	cfc1 t0,fpc_csr
	nop
	sw t0,T_CONTEXT_FPCSR(k0)
	s.d $f0,T_CONTEXT_FP0(k0)
	s.d $f2,T_CONTEXT_FP2(k0)
	s.d $f4,T_CONTEXT_FP4(k0)
	s.d $f6,T_CONTEXT_FP6(k0)
	s.d $f8,T_CONTEXT_FP8(k0)
	s.d $f10,T_CONTEXT_FP10(k0)
	s.d $f12,T_CONTEXT_FP12(k0)
	s.d $f14,T_CONTEXT_FP14(k0)
	s.d $f16,T_CONTEXT_FP16(k0)
	s.d $f18,T_CONTEXT_FP18(k0)
	s.d $f20,T_CONTEXT_FP20(k0)
	s.d $f22,T_CONTEXT_FP22(k0)
	s.d $f24,T_CONTEXT_FP24(k0)
	s.d $f26,T_CONTEXT_FP26(k0)
	s.d $f28,T_CONTEXT_FP28(k0)
	s.d $f30,T_CONTEXT_FP30(k0)
1:

	mfc0 t0,C0_CAUSE
	sw t0,T_CONTEXT_CAUSE(k0)

.set reorder

#if REVISION < 199611
	lw t1,PHYS_TO_K1(MI_INTR_MASK_REG)
	sw t1,T_CONTEXT_RCP(k0)
#endif

	li t1,OS_STATE_RUNNABLE
	sh t1,T_STATE(k0)

#if REVISION >= 199611

#ifndef _FINALROM
	lw a0,__os_Kdebug_Pkt
	beqz a0,no_kdebug
	sw zero,__os_Kdebug_Pkt
	jal kdebugserver
	b __osDispatchThreadSave
no_kdebug:
	lw a0,__osRdb_Mesg
	beqz a0,no_rdb_mesg
	sw zero,__osRdb_Mesg
	jal send_mesg
	lw t0,T_CONTEXT_CAUSE(k0)
no_rdb_mesg:
#endif

#else

	lw t1,__osIsRdbWrite
	beqz t1,no_kdebug
	la t2,RDB_WRITE_INTR_REG
	sw zero,(t2)
	lw a0,RDB_BASE_REG
	jal kdebugserver
	b __osDispatchThreadSave
no_kdebug:
	lw t1,__osIsRdbRead
	beqz t1,no_rdb_mesg
	la t2,RDB_READ_INTR_REG
	sw zero,(t2)
	lw t1,__osRdbSendMessage
	beqz t1,1f
	li a0,ES_SIZE*OS_EVENT_RDB_READ_OK
	jal send_mesg
1:
	lw t1,__osRdbWriteOK
	add t1,1
	sw t1,__osRdbWriteOK
	b __osDispatchThreadSave
no_rdb_mesg:

#endif

	and t1,t0,CAUSE_EXCMASK
	li t2,EXC_BREAK
	beq t1,t2,handle_break
	li t2,EXC_CPU
	beq t1,t2,handle_CpU
	li t2,EXC_INT
	bne t1,t2,panic

handle_interrupt:
	and s0,k1,t0

next_interrupt:
	and t1,s0,CAUSE_IPMASK
	srl t2,t1,CAUSE_IPSHIFT+4
	bnez t2,1f
	srl t2,t1,CAUSE_IPSHIFT
	add t2,16
1:
	lbu t2,__osIntOffTable(t2)
	lw t2,__osIntTable(t2)
	j t2

#if REVISION >= 199611
IP6_Hdlr:
	and s0,~SR_IBIT6
	b next_interrupt

IP7_Hdlr:
	and s0,~SR_IBIT7
	b next_interrupt
#endif

counter:
.set noreorder
	mfc0 t1,C0_COMPARE
	mtc0 t1,C0_COMPARE
.set reorder
	li a0,ES_SIZE*OS_EVENT_COUNTER
	jal send_mesg
	and s0,~SR_IBIT8
	b next_interrupt

cart:
#if REVISION >= 199611
	li a0,ES_SIZE*OS_EVENT_CART
	and s0,~SR_IBIT4
	la sp,leoDiskStack
	addu sp,4096-16
#endif
	li t2,IR_SIZE*1
	lw t2,__osHwIntTable(t2)
	beqz t2,1f
	jal t2
#if REVISION >= 199611
#if REVISION >= 199707
	li a0,ES_SIZE*OS_EVENT_CART
#endif
	beqz v0,1f
	b redispatch
1:
	jal send_mesg
#else
1:
	li a0,ES_SIZE*OS_EVENT_CART
	jal send_mesg
	and s0,~SR_IBIT4
#endif
	b next_interrupt

rcp:
	lw s1,PHYS_TO_K1(MI_INTR_REG)
#if REVISION >= 199611
	la t0,__OSGlobalIntMask
	lw t0,(t0)
	srl t0,RCP_IMASKSHIFT
	and s1,t0
#else
	and s1,RCP_INTMASK
#endif
	and t1,s1,MI_INTR_SP
	beqz t1,vi

	and s1,~MI_INTR_SP & RCP_INTMASK
	lw t4,PHYS_TO_K1(SP_STATUS_REG)
	li t1,SP_CLR_INTR
	sw t1,PHYS_TO_K1(SP_STATUS_REG)
	and t4,SP_STATUS_TASKDONE|SP_STATUS_YIELDED
	beqz t4,sp_other_break
	li a0,ES_SIZE*OS_EVENT_SP
	jal send_mesg
	beqz s1,NoMoreRcpInts
	b vi

sp_other_break:
	li a0,ES_SIZE*OS_EVENT_SP_BREAK
	jal send_mesg
	beqz s1,NoMoreRcpInts

vi:
	and t1,s1,MI_INTR_VI
	beqz t1,ai

	and s1,~MI_INTR_VI & RCP_INTMASK
	sw zero,PHYS_TO_K1(VI_CURRENT_REG)
	li a0,ES_SIZE*OS_EVENT_VI
	jal send_mesg
	beqz s1,NoMoreRcpInts

ai:
	and t1,s1,MI_INTR_AI
	beqz t1,si

	and s1,~MI_INTR_AI & RCP_INTMASK
	li t1,1
	sw t1,PHYS_TO_K1(AI_STATUS_REG)
	li a0,ES_SIZE*OS_EVENT_AI
	jal send_mesg
	beqz s1,NoMoreRcpInts

si:
	and t1,s1,MI_INTR_SI
	beqz t1,pi

	and s1,~MI_INTR_SI & RCP_INTMASK
	sw zero,PHYS_TO_K1(SI_STATUS_REG)
	li a0,ES_SIZE*OS_EVENT_SI
	jal send_mesg
	beqz s1,NoMoreRcpInts

pi:
	and t1,s1,MI_INTR_PI
	beqz t1,dp

	and s1,~MI_INTR_PI & RCP_INTMASK
	li t1,PI_CLR_INTR
	sw t1,PHYS_TO_K1(PI_STATUS_REG)
	li a0,ES_SIZE*OS_EVENT_PI
	jal send_mesg
	beqz s1,NoMoreRcpInts

dp:
	and t1,s1,MI_INTR_DP
	beqz t1,NoMoreRcpInts

	and s1,~MI_INTR_DP & RCP_INTMASK
	li t1,MI_CLR_DP_INTR
	sw t1,PHYS_TO_K1(MI_BASE_REG)
	li a0,ES_SIZE*OS_EVENT_DP
	jal send_mesg

NoMoreRcpInts:
	and s0,~SR_IBIT3
	b next_interrupt

prenmi:
	lw k1,T_CONTEXT_SR(k0)
	and k1,~SR_IBIT5
	sw k1,T_CONTEXT_SR(k0)

	la t1,__osShutdown
	lw t2,(t1)
	beqz t2,firstnmi
	and s0,~SR_IBIT5
	b redispatch

firstnmi:
	li t2,1
	sw t2,(t1)
	li a0,ES_SIZE*OS_EVENT_PRENMI
	jal send_mesg
	and s0,~SR_IBIT5
	lw t2,__osRunQueue
	lw k1,T_CONTEXT_SR(t2)
	and k1,~SR_IBIT5
	sw k1,T_CONTEXT_SR(t2)
	b redispatch

sw2:
	and t0,~CAUSE_SW2
.set noreorder
	mtc0 t0,C0_CAUSE
.set reorder
	li a0,ES_SIZE*OS_EVENT_SW2
	jal send_mesg
	and s0,~SR_IBIT2
	b next_interrupt

sw1:
	and t0,~CAUSE_SW1
.set noreorder
	mtc0 t0,C0_CAUSE
.set reorder
	li a0,ES_SIZE*OS_EVENT_SW1
	jal send_mesg
	and s0,~SR_IBIT1
	b next_interrupt

handle_break:
	li t1,OS_FLAG_CPU_BREAK
	sh t1,T_FLAGS(k0)
	li a0,ES_SIZE*OS_EVENT_CPU_BREAK
	jal send_mesg
	b redispatch

redispatch:
	lw t1,T_PRIORITY(k0)
	lw t2,__osRunQueue
	lw t3,T_PRIORITY(t2)
	bge t1,t3,enqueueRunning
	move a1,k0
	la a0,__osRunQueue
	jal __osEnqueueThread
	j __osDispatchThread

enqueueRunning:
	la t1,__osRunQueue
	lw t2,T_NEXT(t1)
	sw t2,T_NEXT(k0)
	sw k0,T_NEXT(t1)
	j __osDispatchThread

panic:
	sw k0,__osFaultedThread
	li t1,OS_STATE_STOPPED
	sh t1,T_STATE(k0)
	li t1,OS_FLAG_FAULT
	sh t1,T_FLAGS(k0)
.set noreorder
	mfc0 t2,C0_BADVADDR
.set reorder
	sw t2,T_CONTEXT_BADVADDR(k0)
	li a0,ES_SIZE*OS_EVENT_FAULT
	jal send_mesg
	j __osDispatchThread
END(__osException)

LEAF(send_mesg)
	move s2,ra
	la t2,__osEventStateTab
	addu t2,a0

	lw t1,ES_QUEUE(t2)
	beqz t1,send_done

	lw t3,MQ_VALIDCOUNT(t1)
	lw t4,MQ_MSGCOUNT(t1)
	bge t3,t4,send_done

	lw t5,MQ_FIRST(t1)
	addu t5,t3
	rem t5,t4

	lw t4,MQ_MSG(t1)
	mul t5,4
	addu t4,t5
	lw t5,ES_MESSAGE(t2)
	sw t5,(t4)

	addu t2,t3,1
	sw t2,MQ_VALIDCOUNT(t1)

	lw t2,MQ_MTQUEUE(t1)
	lw t3,(t2)
	beqz t3,send_done

	move a0,t1
	jal __osPopThread
	move t2,v0

	move a1,t2
	la a0,__osRunQueue
	jal __osEnqueueThread

send_done:
	j s2
END(send_mesg)

LEAF(handle_CpU)
	and t1,t0,CAUSE_CEMASK
	srl t1,CAUSE_CESHIFT
	li t2,1
	bne t1,t2,panic

	li t1,1
	sw t1,T_FP(k0)

	lw k1,T_CONTEXT_SR(k0)
	or k1,SR_CU1
	sw k1,T_CONTEXT_SR(k0)

	b enqueueRunning
END(handle_CpU)

LEAF(__osEnqueueAndYield)
	lw a1,__osRunningThread
.set noreorder
	mfc0 t0,C0_SR
.set reorder
	or t0,SR_EXL
	sw t0,T_CONTEXT_SR(a1)
	sd s0,T_CONTEXT_S0(a1)
	sd s1,T_CONTEXT_S1(a1)
	sd s2,T_CONTEXT_S2(a1)
	sd s3,T_CONTEXT_S3(a1)
	sd s4,T_CONTEXT_S4(a1)
	sd s5,T_CONTEXT_S5(a1)
	sd s6,T_CONTEXT_S6(a1)
	sd s7,T_CONTEXT_S7(a1)
	sd gp,T_CONTEXT_GP(a1)
	sd sp,T_CONTEXT_SP(a1)
	sd s8,T_CONTEXT_S8(a1)
	sd ra,T_CONTEXT_RA(a1)
	sw ra,T_CONTEXT_PC(a1)

	lw k1,T_FP(a1)
	beqz k1,1f

	cfc1 k1,fpc_csr
	sw k1,T_CONTEXT_FPCSR(a1)
	s.d $f20,T_CONTEXT_FP20(a1)
	s.d $f22,T_CONTEXT_FP22(a1)
	s.d $f24,T_CONTEXT_FP24(a1)
	s.d $f26,T_CONTEXT_FP26(a1)
	s.d $f28,T_CONTEXT_FP28(a1)
	s.d $f30,T_CONTEXT_FP30(a1)
1:

#if REVISION >= 199611
	lw k1,T_CONTEXT_SR(a1)
	and t1,k1,SR_IMASK
	beqz t1,2f
	la t0,__OSGlobalIntMask
	lw t0,(t0)
	xor t0,~0
	and t0,SR_IMASK
	or t1,t0
	and k1,~SR_IMASK
	or k1,t1
	sw k1,T_CONTEXT_SR(a1)
2:
#endif
	lw k1,PHYS_TO_K1(MI_INTR_MASK_REG)
#if REVISION >= 199611
	beqz k1,3f
	la k0,__OSGlobalIntMask
	lw k0,(k0)
	srl k0,RCP_IMASKSHIFT
	xor k0,~0
	and k0,RCP_INTMASK
	lw t0,T_CONTEXT_RCP(a1)
	and k0,t0
	or k1,k0
3:
#endif
	sw k1,T_CONTEXT_RCP(a1)

	beqz a0,noEnqueue
	jal __osEnqueueThread
noEnqueue:
	j __osDispatchThread
END(__osEnqueueAndYield)

LEAF(__osEnqueueThread)
	move t9,a0
	lw t8,T_NEXT(a0)
	lw t7,T_PRIORITY(a1)
	lw t6,T_PRIORITY(t8)
	blt t6,t7,2f
1:
	move t9,t8
	lw t8,T_NEXT(t8)
	lw t6,T_PRIORITY(t8)
	bge t6,t7,1b
2:
	lw t8,T_NEXT(t9)
	sw t8,T_NEXT(a1)
	sw a1,T_NEXT(t9)
	sw a0,T_QUEUE(a1)
	j ra
END(__osEnqueueThread)

LEAF(__osPopThread)
	lw v0,(a0)
	lw t9,T_NEXT(v0)
	sw t9,(a0)
#ifdef _DEBUG
	sw zero,T_NEXT(v0)
#endif
	j ra
END(__osPopThread)

LEAF(__osDispatchThread)
	la a0,__osRunQueue
	jal __osPopThread
	sw v0,__osRunningThread
	li t0,OS_STATE_RUNNING
	sh t0,T_STATE(v0)
	move k0,v0

__osDispatchThreadSave:
#if REVISION >= 199611
	lw k1,T_CONTEXT_SR(k0)
	la t0,__OSGlobalIntMask
	lw t0,(t0)
	and t0,SR_IMASK
	and t1,k1,SR_IMASK
	and t1,t0
	and k1,~SR_IMASK
	or k1,t1
.set noreorder
	mtc0 k1,C0_SR
.set reorder
#endif
.set noat
	ld AT,T_CONTEXT_AT(k0)
.set at
	ld v0,T_CONTEXT_V0(k0)
	ld v1,T_CONTEXT_V1(k0)
	ld a0,T_CONTEXT_A0(k0)
	ld a1,T_CONTEXT_A1(k0)
	ld a2,T_CONTEXT_A2(k0)
	ld a3,T_CONTEXT_A3(k0)
	ld t0,T_CONTEXT_T0(k0)
	ld t1,T_CONTEXT_T1(k0)
	ld t2,T_CONTEXT_T2(k0)
	ld t3,T_CONTEXT_T3(k0)
	ld t4,T_CONTEXT_T4(k0)
	ld t5,T_CONTEXT_T5(k0)
	ld t6,T_CONTEXT_T6(k0)
	ld t7,T_CONTEXT_T7(k0)
	ld s0,T_CONTEXT_S0(k0)
	ld s1,T_CONTEXT_S1(k0)
	ld s2,T_CONTEXT_S2(k0)
	ld s3,T_CONTEXT_S3(k0)
	ld s4,T_CONTEXT_S4(k0)
	ld s5,T_CONTEXT_S5(k0)
	ld s6,T_CONTEXT_S6(k0)
	ld s7,T_CONTEXT_S7(k0)
	ld t8,T_CONTEXT_T8(k0)
	ld t9,T_CONTEXT_T9(k0)
	ld gp,T_CONTEXT_GP(k0)
	ld sp,T_CONTEXT_SP(k0)
	ld s8,T_CONTEXT_S8(k0)
	ld ra,T_CONTEXT_RA(k0)
	ld k1,T_CONTEXT_LO(k0)
	mtlo k1
	ld k1,T_CONTEXT_HI(k0)
	mthi k1
	lw k1,T_CONTEXT_PC(k0)
.set noreorder
	mtc0 k1,C0_EPC

#if REVISION < 199611
	lw k1,T_CONTEXT_SR(k0)
	mtc0 k1,C0_SR
#endif

	lw k1,T_FP(k0)
	beqz k1,1f
	nop
	lw k1,T_CONTEXT_FPCSR(k0)
	ctc1 k1,fpc_csr
	l.d $f0,T_CONTEXT_FP0(k0)
	l.d $f2,T_CONTEXT_FP2(k0)
	l.d $f4,T_CONTEXT_FP4(k0)
	l.d $f6,T_CONTEXT_FP6(k0)
	l.d $f8,T_CONTEXT_FP8(k0)
	l.d $f10,T_CONTEXT_FP10(k0)
	l.d $f12,T_CONTEXT_FP12(k0)
	l.d $f14,T_CONTEXT_FP14(k0)
	l.d $f16,T_CONTEXT_FP16(k0)
	l.d $f18,T_CONTEXT_FP18(k0)
	l.d $f20,T_CONTEXT_FP20(k0)
	l.d $f22,T_CONTEXT_FP22(k0)
	l.d $f24,T_CONTEXT_FP24(k0)
	l.d $f26,T_CONTEXT_FP26(k0)
	l.d $f28,T_CONTEXT_FP28(k0)
	l.d $f30,T_CONTEXT_FP30(k0)
1:
	lw k1,T_CONTEXT_RCP(k0)
#if REVISION >= 199611
	la k0,__OSGlobalIntMask
	lw k0,(k0)
	srl k0,RCP_IMASKSHIFT
	and k1,k0
#endif
	sll k1,1
	la k0,__osRcpImTable
	addu k1,k0
	lhu k1,(k1)
	la k0,PHYS_TO_K1(MI_INTR_MASK_REG)
	sw k1,(k0)
	nop
	nop
	nop
	nop
	eret
.set reorder
END(__osDispatchThread)

LEAF(__osCleanupThread)
	move a0,zero
	jal osDestroyThread
END(__osCleanupThread)
