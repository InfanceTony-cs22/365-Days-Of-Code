#include<iostream>

using namespace std;

int main()  {
    char ch;
    cin >> ch;
    
    int ascii_value = static_cast<int>(ch);
    cout << ascii_value << endl;
    
    return 0;
}
