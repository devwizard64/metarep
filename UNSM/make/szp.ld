OUTPUT_ARCH(mips)
SECTIONS
{
   .text : {*(.text*); *(.data*); *(.rodata*)}
    /DISCARD/ : {*(*)}
}
