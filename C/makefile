TARGET := test
C_FILES := $(wildcard source/*.c)
LIB_TYPE := $(shell if [ `uname` = Linux ] ; then echo .so ; else echo .dll ; fi)
OBJ_FILES := $(addprefix objects/,$(notdir $(C_FILES:.c=.o)))
SO_FILES := $(addprefix shared/,$(notdir $(C_FILES:.c=$(LIB_TYPE))))

CFLAGS = -pedantic -fPIC -Wall -std=c99
CSHAREFLAGS = -std=c99 -fPIC -shared -Wl,-soname,

all: $(TARGET) $(SO_FILES) test testAlgorithm

$(TARGET): main.c $(OBJ_FILES)
	gcc -std=c99 -o $@ $< $(OBJ_FILES)
	
objects/%.o: source/%.c
	gcc -c $(CFLAGS) -o $@ $<

shared/%$(LIB_TYPE): source/%.c
	gcc $(CSHAREFLAGS)$@.1 -o $@ $<

.PHONY: testAlgorithm
testAlgorithm:
	./test --iterations 4

clean:
	rm -f objects/*.o
	rm -f shared/*.so
	rm -f shared/*.dll
