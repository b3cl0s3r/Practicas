IDIR =../include
CC=g++
CFLAGS=-I$(IDIR) -std=c++11 -g

ODIR=../src

LIBS=-lm

_OBJ = block_t.o row_t.o wall_t.o main.o unbreakable_wall.o
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))

all: main

$(ODIR)/block_t.o: $(ODIR)/block_t.cpp $(IDIR)/block_t.hpp
	$(CC) -c -o $@ $< $(CFLAGS)

$(ODIR)/row_t.o: $(ODIR)/row_t.cpp $(IDIR)/row_t.hpp $(IDIR)/block_t.hpp
	$(CC) -c -o $@ $< $(CFLAGS)

$(ODIR)/wall_t.o: $(ODIR)/wall_t.cpp $(IDIR)/wall_t.hpp $(IDIR)/row_t.hpp $(IDIR)/block_t.hpp
	$(CC) -c -o $@ $< $(CFLAGS)

$(ODIR)/unbreakable_wall.o: $(ODIR)/unbreakable_wall.cpp $(IDIR)/unbreakable_wall.hpp $(IDIR)/wall_t.hpp $(IDIR)/row_t.hpp $(IDIR)/block_t.hpp
	$(CC) -c -o $@ $< $(CFLAGS)

$(ODIR)/main.o: $(ODIR)/main.cpp $(IDIR)/block_t.hpp $(IDIR)/row_t.hpp $(IDIR)/wall_t.hpp $(IDIR)/unbreakable_wall.hpp
	$(CC) -c -o $@ $< $(CFLAGS)

main: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ $(INCDIR)/*~
