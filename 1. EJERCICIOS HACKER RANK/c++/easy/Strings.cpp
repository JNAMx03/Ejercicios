#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string word1, word2;
    char aux;

    cin >> word1;
    cin >> word2;

    cout << word1.size() << " " << word2.size() << endl;
    cout << word1 + word2 << endl;

    aux = word1[0];
    word1[0] = word2[0];
    word2[0] = aux;

    cout << word1 << " " << word2;
  
    return 0;
}