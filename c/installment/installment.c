#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char **argv)
{
	double intr_before;
	int period;
	int payment_before;

	double intr_after;
	double payment_after_each;
	double payment_after_total;

	if (argc != 4) {
		printf("3 arguments needed!\n");
		printf("example: $ install 0.1347 12 30000\n");
		exit(0);
	}
	
	intr_before = atof(argv[1]);
	period = atoi(argv[2]);
	payment_before = atoi(argv[3]);
	printf("intr: %g, period: %d, original payment: %d\n", 
			intr_before, period, payment_before);
	
	intr_after = pow(10.0, log10(1 + intr_before) / 12.0) - 1;
	printf("intr_after: %g\n", intr_after);
	
	payment_after_total = payment_before * pow(1 + intr_after, period);
	payment_after_each = payment_after_total / period;
	
	printf("after, each: %g, total: %g\n", 
			payment_after_each, payment_after_total);

	return 0;
}

