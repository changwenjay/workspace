#include <stdio.h>
#include <math.h>

int main()
{
	long N = 35;
	long e = 2, d = 13;
	long message = 11;
	long long coded, decoded;

	printf("message: %ld\n", message);
	coded = (long long)pow(message, e) % N;
	printf("coded: %lf\n", coded);
	decoded = (long long)pow(coded, d) % N;
	printf("decoded: %lf\n", decoded);

	return 0;
}

