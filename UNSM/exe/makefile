OBJ     := mask slienc texture

CC      := cc -Wall -Wextra -Wpedantic -O2

.PHONY: default
default: $(OBJ)

%: %.c
	$(CC) -o $@ $^

texture: texture.c lodepng/lodepng.c
	$(CC) -I lodepng -o $@ $^

.PHONY: clean
clean:
	rm -rf $(OBJ) __pycache__ *.pyc
