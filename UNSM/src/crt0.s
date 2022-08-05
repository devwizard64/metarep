.set noreorder

.globl _start
_start:
    lui     $8, %hi(_codeSegmentBssStart)
    lui     $9, _bss_size_hi
    addiu   $8, $8, %lo(_codeSegmentBssStart)
    ori     $9, $9, _bss_size_lo
1:
    sub     $9, 8
    sw      $0, 0($8)
    sw      $0, 4($8)
    bnez    $9, 1b
    add     $8, 8
    lui     $10, %hi(entry)
    lui     $29, %hi(stack_entry+0x400)
    addiu   $10, $10, %lo(entry)
    j       $10
    addiu   $29, $29, %lo(stack_entry+0x400)
    nop
    nop
    nop
    nop
    nop
    nop
