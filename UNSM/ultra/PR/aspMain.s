.globl aspMainTextStart
aspMainTextStart:
.incbin "build/PR/aspMain.text.bin"
.globl aspMainTextEnd
aspMainTextEnd:
.data
.globl aspMainDataStart
aspMainDataStart:
.incbin "build/PR/aspMain.data.bin"
.globl aspMainDataEnd
aspMainDataEnd:
