CC = g++
DEPS = 
CFLAGS += -Wall -Wno-unused -D_GNU_SOURCE -std=c++11
OBJS = main.o 

%.o: %.cc $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

main: $(OBJS)
	$(CC) $(OBJS) ${CFLAGS} -I. -L. -o $@

clean :
	rm -f *.o main

