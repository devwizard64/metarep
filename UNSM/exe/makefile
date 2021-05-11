CC      := cc -Wall -Wextra -Wpedantic -O2

default: build/crc build/szp build/texture

build/texture: texture.c ../lodepng/lodepng.c | build
	$(CC) -I ../lodepng -o $@ $^

build/%: %.c | build
	$(CC) -o $@ $^

build:
	mkdir -p $@

clean:
	rm -rf build __pycache__ *.pyc

.PHONY: default clean
