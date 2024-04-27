#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    for (int i = 0; i < N; ++i) {
        if (i % 2 == 0) {
            // Skip even numbers
            continue;
        }
        cout << i << endl;
    }
    
    return 0;
}
