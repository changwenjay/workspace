#include <stdio.h>

int fab(int k)
{
	int i, sum, k_1, k_2;

	if (k == 0) {
		sum = 0;
	} else if (k == 1) {
		sum = 1;
	} else {
		k_1 = 1;
		k_2 = 0;
		for (i = 2; i < k + 1; i++) {
			sum = k_1 + k_2;
			// printf("sum 0, 1, 2: %d, %d, %d\n", sum, k_1, k_2);
			k_2 = k_1;
			k_1 = sum;
		}
	}

	return sum;
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

