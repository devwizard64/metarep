.data;  .globl object_debug_data;   object_debug_data:      .incbin "src/object_debug.data.bin"
.bss;   .globl object_debug_bss;    object_debug_bss:       .space 0x20
.text
