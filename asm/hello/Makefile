all: hello

hello: hello.o
	ld -o hello hello.o

hello.o: hello.asm
	nasm -g -felf64 -o hello.o hello.asm

clean:
	rm *~ *o hello

