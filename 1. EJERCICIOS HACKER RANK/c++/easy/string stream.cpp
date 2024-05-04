#include <sstream>
#include <vector>
#include <iostream>
#include <sstream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
	vector<int> nums;
	int i=0, nn;
	string t = "";
	while(str[i] != NULL)
	{
		t += str[i];
		if(str[i] == ',' || str[i+1] == NULL)
		{
			stringstream ss;
			ss << t;
			ss >> nn;
			nums.push_back(nn);
			t = "";
		}
		i++;
	}
	return nums;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
