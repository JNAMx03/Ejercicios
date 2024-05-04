#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

int find_nth_term(int n, int a, int b, int c) {
  //Write your code here.
  	int aux = 0;
	
	switch(n)
	{
		case 1:
			return a;
		break;
		case 2:
			return b;
		break;
		case 3:
			return c;
		break;
		default:
			
			aux = a + b + c;
			a = b;
			b = c;
			c = aux;
			/*if(n == 4)
			{
				return aux;
			}*/
			n--;
			return find_nth_term(n, a, b, c);
			
		
	}
  
  
}

int main() {
    int n, a, b, c;
  
    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);
 
    printf("%d", ans); 
    return 0;
}
