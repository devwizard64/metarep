/* void slidec(const char *src, char *dst) */
.globl slidec
slidec:
    lw      $t8, 0x04($a0)
    lw      $a3, 0x08($a0)
    lw      $t9, 0x0C($a0)
    move    $a2, $0
    add     $t8, $a1
    add     $a3, $a0
    add     $t9, $a0
    add     $a0, 0x10
1:
    bnez    $a2, 2f
    lw      $t0, ($a0)
    li      $a2, 32
    add     $a0, 4
2:
    slt     $t1, $t0, $0
    beqz    $t1, 2f
    lb      $t2, ($t9)
    add     $t9, 1
    sb      $t2, ($a1)
    add     $a1, 1
    b       3f
2:
    lhu     $t2, ($a3)
    add     $a3, 2
    srl     $t3, $t2, 12
    and     $t2, 0xFFF
    sub     $t1, $a1, $t2
    add     $t3, 3
2:
    lb      $t2, -1($t1)
    sub     $t3, 1
    add     $t1, 1
    sb      $t2, ($a1)
    add     $a1, 1
    bnez    $t3, 2b
3:
    sll     $t0, 1
    sub     $a2, 1
    bne     $a1, $t8, 1b
    j       $ra
