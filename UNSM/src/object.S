.data;  .globl object_data;     object_data:    .incbin "src/object.data.bin"
.bss;   .globl object_bss;      object_bss:     .space 0x24690
.text
