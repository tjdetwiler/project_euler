CC = g++
DEPS = utils.h
CFLAGS += -Wall -Wno-unused -D_GNU_SOURCE 
OBJS = main.o utils.o

%.o: %.cc $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

test: test.o
	$(CC) test.o ${CFLAGS} -I. -L. -o $@

main: $(OBJS)
	$(CC) $(OBJS) ${CFLAGS} -I. -L. -o $@

clean :
	rm -f *.o main

