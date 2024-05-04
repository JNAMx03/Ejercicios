#include <stdio.h>

int main()
{
	int a, b;
	float c, d;
	
	scanf("%d %d", &a, &b);
	printf("%d\n%d", a, b);
	printf("\n%d %d\n", a+b, a-b);
	
	scanf("%f %f", &c, &d);
	printf("%f\n%f", c, d);
	printf("\n%1.1f %1.1f\n", c+d, c-d);
	
	return 0;
}
