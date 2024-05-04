#include <iostream>
using namespace std;
int main()
{
    int x, n, p, a, b = 0, i;
    cin >> x;
    cin >> n;
    for (i = 0; i < n; i++)
    {
        cin >> p;
        a = x - p;
        b = b + a; 
    }
    cout << (b+x);
    return 0;
}
