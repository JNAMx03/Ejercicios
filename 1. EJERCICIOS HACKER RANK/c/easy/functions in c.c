#include <stdio.h>

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max(int x, int y)
{
	if(x > y)
	{
		return x;
	}
	else
	{
		return y;
	}
}

int max_of_four(int a, int b, int c, int d)
{
	int n = max(a, b);
	int m = max(c, d);
	int o = max(n, m);
	return o;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
