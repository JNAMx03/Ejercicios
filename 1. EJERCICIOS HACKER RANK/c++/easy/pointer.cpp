#include <iostream>
#include <cmath>

using namespace std;

void update(int *a,int *b) {
	int ra = *a, rb = *b;
	*a = ra + rb;
	*b = abs(ra-rb);
    // Complete this function    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    cin >> a;
	cin >> b;
    update(pa, pb);
    cout << a << "\n" << b;

    return 0;
}
