all: test_gdb

test_gdb:	test_gdb.o
	ld -o test_gdb test_gdb.o

test_gdb.o:	test_gdb.s
	as -gstabs -o test_gdb.o test_gdb.s

clean:
	rm *~ *o test_gdb
