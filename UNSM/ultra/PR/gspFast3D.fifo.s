.globl gspFast3D_fifoTextStart
gspFast3D_fifoTextStart:
.incbin "build/PR/gspFast3D.fifo.text.bin"
.globl gspFast3D_fifoTextEnd
gspFast3D_fifoTextEnd:
.data
.globl gspFast3D_fifoDataStart
gspFast3D_fifoDataStart:
.incbin "build/PR/gspFast3D.fifo.data.bin"
.globl gspFast3D_fifoDataEnd
gspFast3D_fifoDataEnd:
