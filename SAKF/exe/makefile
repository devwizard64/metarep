OBJ     := crc

CC      := cc -Wall -Wextra -Wpedantic -O2

.PHONY: default
default: $(OBJ)

%: %.c
	$(CC) -o $@ $^

.PHONY: clean
clean:
	rm -rf $(OBJ)
