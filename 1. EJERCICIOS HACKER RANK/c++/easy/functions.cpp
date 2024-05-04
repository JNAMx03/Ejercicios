#include <iostream>
#include <cstdio>
using namespace std;

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
	int m = max(a, b);
	int n = max(c, d);
	int o = max(m, n);
	return o;
}

int main() {
    int a, b, c, d;
    cin >> a;
	cin >> b;
	cin >> c;
	cin >> d;
    int ans = max_of_four(a, b, c, d);
    cout << ans;
    
    return 0;
}
