.data;  .globl camera_data;     camera_data:    .incbin "src/camera.data.bin"
.bss;   .globl camera_bss;      camera_bss:     .space 0x6C0
.text
