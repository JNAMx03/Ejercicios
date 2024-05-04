#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    int x, n, p, a, b = 0, i;
    scanf ("%i", &x);
    scanf ("%i", &n);
    for (i = 0; i < n; i++)
    {
        scanf ("%i", &p);
        a = x - p;
        b = b + a; 
    }
    printf("%i", b+x);
    return 0;
}
