MEMORY
{
	HDR: start = $0000, size = $0010, fill = yes, fillval = $00;
	PRG: start = $C000, size = $4000, fill = yes, fillval = $FF;
	CHR: start = $0000, size = $2000, fill = yes, fillval = $FF;
}
SEGMENTS
{
	HEADER: load = HDR, type = ro;
	CODE:   load = PRG, type = ro, start = $C000;
	AUDIO:  load = PRG, type = ro, start = $F8A7;
	VECTOR: load = PRG, type = ro, start = $FFFA;
	CHR:    load = CHR, type = ro;
}
