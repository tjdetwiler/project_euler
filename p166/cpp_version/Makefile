CC = g++
DEPS = utils.h bigraph.h hopcroft_karp.h hungarian.h
CFLAGS += -Wall -Wno-unused -D_GNU_SOURCE
OBJS = main.o utils.o bigraph.o hopcroft_karp.o hungarian.o

%.o: %.cc $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)


main: $(OBJS)
	$(CC) $(OBJS) ${CFLAGS} -I. -L. -o $@

clean :
	rm -f *.o main

