#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(){
    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
    int limit = n + n - 1;

    for (int i = 0; i < limit; i++){
      for (int j = 0; j < limit; j++){
        int min = i < j ? i : j;
        min = min < limit-i ? min : limit-i-1;
        min = min < limit-j-1 ? min : limit-j-1;
        printf("%d ", n-min);
      }
      printf("\n");
      
    }
    
    return 0;
}