OBJ     := mask slienc texture

CC      := cc
CCFLAG  := -Wall -Wextra -Wpedantic -O2

.PHONY: default
default: $(OBJ)

%: %.c
	$(CC) $(CCFLAG) -o $@ $^

.PHONY: clean
clean:
	rm -rf $(OBJ) __pycache__ *.pyc
