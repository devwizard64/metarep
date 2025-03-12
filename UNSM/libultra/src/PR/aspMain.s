.globl aspMainTextStart
aspMainTextStart:
.incbin "aspMain.text.bin"
.globl aspMainTextEnd
aspMainTextEnd:

.data

.globl aspMainDataStart
aspMainDataStart:
.incbin "aspMain.data.bin"
.globl aspMainDataEnd
aspMainDataEnd:
