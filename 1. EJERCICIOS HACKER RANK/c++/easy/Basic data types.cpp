#include <iostream>

using namespace std;

int main()
{
	int a;
	long b;
	char c;
	float d;
	double e;
	
	scanf("%d %ld %c %f %lf", &a, &b, &c, &d, &e);
	printf("%d \n%ld \n%c \n%1.3f \n%1.5lf", a, b, c, d, e);
	
	return 0;
}
