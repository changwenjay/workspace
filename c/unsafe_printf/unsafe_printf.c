#include <stdio.h>

void unsafe_printf(const char *s)
{
	char *t = "hello";
	printf(s, t);
}

int main()
{

	unsafe_printf("%s%s%s%s%s%s\n");

	return 0;
}

