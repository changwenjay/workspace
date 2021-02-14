.section .data
	.int 19

.section .text
.global _start

_start:
	nop
	movl $19, %eax
	addl $19, %eax
	nop
	nop
	movl $60, %eax
	xor %edi, %edi
	syscall

