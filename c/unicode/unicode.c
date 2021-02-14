// 宠
// 00000000  e5 ae a0 0a                                       |....|        ssasss
// 00000004
// e5         ae         a0
// 1110 0101  1010 1110  1010 0000
#include <stdio.h>

int main()
{
	// int c = 23456;
	int c = 23457;
	int b0 = 0b0101;
	int b1 = 0b101110;
	int b2 = 0b100000;
	int c0, c1, c2;

	c2 = c % 64;
	c2 |= 0b10000000;

	c1 = (c / 64 ) % 64;
	c1 |= 0b10000000;

	c0 = (c / 64 / 64) % 64;
	c0 |= 0b11100000;

	printf("%x %x %x\n", c0, c1, c2);
	printf("%c%c%c\n", c0, c1, c2);

	return 0;
}

