#include <stdio.h>

int fab(int k)
{
	if (k == 0) {
		return 0;
	} else if (k == 1) {
		return 1;
	} else {
		return fab(k - 1) + fab(k -2);
	}
}

int main()
{
	int k = 8;
	int i;

	for (i = 0; i < k; i++) {
		printf("fab(%d): %d\n", i, fab(i));
	}

	return 0;
}

