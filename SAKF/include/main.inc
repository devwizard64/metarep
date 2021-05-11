.macro ldf faraddr
    lda #.loword(faraddr)
    ldx #.hiword(faraddr)
.endmacro

.macro ldl faraddr
    ldx #.hiword(faraddr)
    lda #.loword(faraddr)
.endmacro

.macro jss addr
    ldf addr
    jsl code_008C3F
.endmacro

.macro jms addr
    ldf addr
    jml code_008C3F
.endmacro

.macro jsc addr
    ldf addr
    jsl code_008C6D
.endmacro

.macro jmc addr
    ldf addr
    jml code_008C6D
.endmacro

.macro mem_t arg, size, src, dst
    .byte arg
    .word size
    .faraddr src
    .word dst
.endmacro

.macro _00841C_t arg0, arg1
    .byte arg0
    .word arg1
.endmacro

.ifdef _J0
code_0397F4 = $0397F4
code_03A02A = $03A02A
code_03A103 = $03A103
code_03A18A = $03A18A
code_03A25E = $03A25E
code_03A2B4 = $03A2B4
code_03AC02 = $03AC02
code_03D644 = $03D644
code_03EC3A = $03EC3A
code_048184 = $048184
code_05813A = $05813A
code_05971A = $05971A
code_059A15 = $059A15
code_059A1B = $059A1B
code_059A39 = $059A39
code_059A4C = $059A4C
code_059AD7 = $059AD7
code_059AF3 = $059AF3
code_059B01 = $059B01
code_059CC1 = $059CC1
code_059D1F = $059D1F
code_05A26C = $05A26C
code_05EBC4 = $05EBC4
code_C905FC = $C905FC
code_CF2E10 = $CF2E10
code_CF63B6 = $CF63B6
code_CF63F8 = $CF63F8
code_CF98A9 = $CF98A9
code_CFB350 = $CFB350
code_CFB35D = $CFB35D
code_D00623 = $D00623
code_D00771 = $D00771
code_D01566 = $D01566
code_D02337 = $D02337
code_D0234E = $D0234E
code_D3E1DA = $D3E1DA
code_D59992 = $D59992

bss_760D = $760D
bss_7659 = $7659
bss_765D = $765D
bss_7661 = $7661
bss_7665 = $7665
bss_7691 = $7691
bss_7695 = $7695
bss_7699 = $7699
bss_769D = $769D
bss_7934 = $7934
.endif

.ifdef _E0
code_01DFC6_E0 = $01DFC6
code_0397F4 = $0397F4 ;
code_03A02A = $03A02A ;
code_03A103 = $03A103 ;
code_03A18A = $03A18A ;
code_03A25E = $03A25E ;
code_03A2B4 = $03A2B4 ;
code_03AC02 = $03AC02 ;
code_03D644 = $03D6B9
code_03EC3A = $03EC3A ;
code_048184 = $048184 ;
code_05813A = $05813A ;
code_05971A = $05971A ;
code_059A15 = $059A15 ;
code_059A1B = $059A1B ;
code_059A39 = $059A39 ;
code_059A4C = $059A4C ;
code_059AD7 = $059AD7 ;
code_059AF3 = $059AF3 ;
code_059B01 = $059B01 ;
code_059CC1 = $059CC1 ;
code_059D1F = $059D1F ;
code_05A26C = $05A26C ;
code_05EBC4 = $05EBC9
code_C905FC = $C905FC ;
code_CF2E10 = $CF2E10 ;
code_CF63B6 = $CF63B6 ;
code_CF63F8 = $CF63F8 ;
code_CF98A9 = $CF98A9 ;
code_CFB350 = $CFB350 ;
code_CFB35D = $CFB35D ;
code_D00623 = $D00623 ;
code_D00771 = $D00771 ;
code_D01566 = $D01566 ;
code_D02337 = $D02337 ;
code_D0234E = $D0234E ;
code_D3E1DA = $D3E1DA ;
code_D4FB90_E0 = $D4FB90
code_D59992 = $D59992 ;

bss_760D = $760F
bss_7659 = $765B
bss_765D = $765F
bss_7661 = $7663
bss_7665 = $7667
bss_7691 = $7693
bss_7695 = $7697
bss_7699 = $769B
bss_769D = $769F
bss_7934 = $7936
.endif

.ifdef _P0
code_01DFC6_E0 = $01DFC6 ;
code_0397F4 = $0397F4 ;
code_03A02A = $03A02A ;
code_03A103 = $03A103 ;
code_03A18A = $03A18A ;
code_03A25E = $03A25E ;
code_03A2B4 = $03A2B4 ;
code_03AC02 = $03AC02 ;
code_03D644 = $03D644 ;
code_03EC3A = $03EC3A ;
code_048184 = $048184 ;
code_05813A = $05813A ;
code_05971A = $05971A ;
code_059A15 = $059A15 ;
code_059A1B = $059A1B ;
code_059A39 = $059A39 ;
code_059A4C = $059A4C ;
code_059AD7 = $059AD7 ;
code_059AF3 = $059AF3 ;
code_059B01 = $059B01 ;
code_059CC1 = $059CC1 ;
code_059D1F = $059D1F ;
code_05A26C = $05A26C ;
code_05EBC4 = $05EBC4 ;
code_C905FC = $C905FC ;
code_CF2E10 = $CF2E10 ;
code_CF63B6 = $CF63B6 ;
code_CF63F8 = $CF63F8 ;
code_CF98A9 = $CF98A9 ;
code_CFB350 = $CFB350 ;
code_CFB35D = $CFB35D ;
code_D00623 = $D00623 ;
code_D00771 = $D00771 ;
code_D01566 = $D01566 ;
code_D02337 = $D02337 ;
code_D0234E = $D0234E ;
code_D3E1DA = $D3E1DA ;
code_D4FB90_E0 = $D4FB90 ;
code_D59992 = $D59992 ;

bss_760D = $760F ;
bss_7659 = $765B ;
bss_765D = $765F ;
bss_7661 = $7663 ;
bss_7665 = $7667 ;
bss_7691 = $7693 ;
bss_7695 = $7697 ;
bss_7699 = $769B ;
bss_769D = $769F ;
bss_7934 = $7936 ;
.endif
