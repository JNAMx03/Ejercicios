#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
	int i, j, max_and = 0, max_not = 0, max_xor = 0, aux;
	for(i = 1; i <= (n-1); i++)
	{
		
		for(j = (i+1); j <= n; j++)
		{
			aux = i & j;
			if(max_and < aux && aux < k )
			{
				max_and = i & j;
			}
			
			aux = i | j;
			if(max_not < aux && aux < k )
			{
				max_not = i | j;
			}
			
			aux = i ^ j;
			if(max_xor < aux && aux < k )
			{
				max_xor = i ^ j;
			}
			
		}
		
	}
	printf("%d\n%d\n%d", max_and, max_not, max_xor);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}

