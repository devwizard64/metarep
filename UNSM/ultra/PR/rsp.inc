.rsp

.macro li, rt, imm
    .if (imm) >= 0x8000
        ori     rt, $0, imm
    .else
        addi    rt, $0, imm
    .endif
.endmacro

.macro la, rt, imm
    addiu   rt, $0, lo(imm)
.endmacro

.macro move, rt, rs
    ori     rt, rs, 0
.endmacro

.macro vmov, vt, vs
    vadd    vt, vs, $v0[0]
.endmacro

.macro .base, addr
    .headersize (addr) - orga()
.endmacro

.macro .even
    .if (org() & 4) != 0
        nop
    .endif
.endmacro

.macro .odd
    .if (org() & 4) == 0
        nop
    .endif
.endmacro

.half equ .halfword

SP_SR_H         equ 0x0001  ; halt
SP_SR_B         equ 0x0002  ; break
SP_SR_DB        equ 0x0004  ; DMA busy
SP_SR_DF        equ 0x0008  ; DMA full
SP_SR_IF        equ 0x0010  ; I/O full
SP_SR_SS        equ 0x0020  ; single step
SP_SR_IB        equ 0x0040  ; interrupt on break

SP_SW_CH        equ 0x00000001  ; clear H
SP_SW_SH        equ 0x00000002  ; set H
SP_SW_CB        equ 0x00000004  ; clear B
SP_SW_CI        equ 0x00000008  ; clear interrupt
SP_SW_SI        equ 0x00000010  ; set interrupt
SP_SW_CSS       equ 0x00000020  ; clear SS
SP_SW_SSS       equ 0x00000040  ; set SS
SP_SW_CIB       equ 0x00000080  ; clear IB
SP_SW_SIB       equ 0x00000100  ; set IB

DPC_SR_X        equ 0x0001  ; XBUS DMEM or DRAM select
DPC_SR_F        equ 0x0002  ; frozen
DPC_SR_FL       equ 0x0004  ; flushed
DPC_SR_G        equ 0x0008  ; GCLK is alive
DPC_SR_TB       equ 0x0010  ; TMEM busy
DPC_SR_PB       equ 0x0020  ; PIPE busy
DPC_SR_CB       equ 0x0040  ; CMD busy
DPC_SR_CR       equ 0x0080  ; CMD ready
DPC_SR_DB       equ 0x0100  ; DMA busy
DPC_SR_EV       equ 0x0200  ; END valid
DPC_SR_SV       equ 0x0400  ; START valid

DPC_SW_CX       equ 0x0001  ; clear X
DPC_SW_SX       equ 0x0002  ; set X
DPC_SW_CF       equ 0x0004  ; clear F
DPC_SW_SF       equ 0x0008  ; set F
DPC_SW_CFL      equ 0x0010  ; clear FL
DPC_SW_SFL      equ 0x0020  ; set FL
DPC_SW_CTC      equ 0x0040  ; clear TMEM count
DPC_SW_CPC      equ 0x0080  ; clear PIPE count
DPC_SW_CCC      equ 0x0100  ; clear CMD count
DPC_SW_CGC      equ 0x0200  ; clear CLOCK count

t_type          equ 0x0FC0
t_flag          equ 0x0FC4
t_boot          equ 0x0FC8
t_boot_size     equ 0x0FCC
t_text          equ 0x0FD0
t_text_size     equ 0x0FD4
t_data          equ 0x0FD8
t_data_size     equ 0x0FDC
t_stack         equ 0x0FE0
t_stack_size    equ 0x0FE4
t_fifo_start    equ 0x0FE8
t_fifo_end      equ 0x0FEC
t_cmd           equ 0x0FF0
t_cmd_size      equ 0x0FF4
t_yield         equ 0x0FF8
t_yield_size    equ 0x0FFC
