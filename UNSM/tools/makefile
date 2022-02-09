OBJ     := mask texture slienc

CC      := cc
CCFLAG  := -O2 -Wall -Wextra -Wpedantic

.PHONY: default
default: $(OBJ)

.PHONY: clean
clean:
	rm -f -r $(OBJ) __pycache__ *.pyc

%: %.c
	$(CC) $(CCFLAG) -o $@ $<
