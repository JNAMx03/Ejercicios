#include <iostream>
#include <ctype.h>

using namespace std;

int main()
{
    string date;
    char split[] = " ";
    cin >> date;
    for (int i = 0; i < date.length; i++)
    {
        date[i] = toupper(date[i]);
    }
    char *token = strtok(date, split);
    if()
    {

    }
    return 0;
}
