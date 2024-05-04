#include <stdio.h>
#include <math.h>

int main()
{
	int a, i;
	float sum = 0;
	
	scanf("%d", &a);
	
	int b = a;
	

	int n = floor(log10(abs(a))) + 1;
	
	for(i = 1; i<=n; i++)
	{
		
		sum =  sum + pow((b%10),n);
		b = b/10;
		
	}
	
	//printf("%1.0f", sum);
	if(sum == a)
	{
		printf("%d is an Armstrong number", a);
	}
	else
	{
		printf("%d is not an Armstrong number", a);
	}
	
	return 0;
}
