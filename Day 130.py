#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N; // Number of integers in the sorted array
    vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }

    int Q;
    cin >> Q; // Number of queries
    while (Q--) {
        int X;
        cin >> X; // Query integer
        
        // Find lower bound using lower_bound function
        auto lower = lower_bound(arr.begin(), arr.end(), X);
        int leftmost_index = lower - arr.begin();
        
        // Find upper bound using upper_bound function
        auto upper = upper_bound(arr.begin(), arr.end(), X);
        int rightmost_index = upper - arr.begin() - 1;
        
        // If X is found in the array
        if (leftmost_index <= rightmost_index && arr[leftmost_index] == X) {
            cout << leftmost_index << endl;
        } 
        // If X is not found, print the rightmost index at which X can be inserted
        else {
            cout << rightmost_index + 1 << endl;
        }
    }

    return 0;
}
