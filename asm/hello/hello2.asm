section .data
msg: db "Hello World", 10
len: equ $ - msg

section .text
global _start

_start:
	mov rax, 1		; sys_write
	mov rdi, 1		; stdout
	mov rsi, msg
	mov rdx, len
	syscall

	mov rax, 60		; sys_exit
	mov rdi, 0		; return code
	syscall

