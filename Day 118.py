#include <iostream>
using namespace std;

int main() {
    int x, y;
    cin >> x >> y;
    
    string result = (x <= y) ? "Robin" : "Rahul";
    cout << result << endl;

    return 0;
}
