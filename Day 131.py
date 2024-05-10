#include<iostream>
#include<map>
using namespace std;

int main() {
    int Q;
    cin >> Q;
    map<int, int> boxes; // Map to store the number of balls in each box
    
    while(Q--) {
        int type, X, Y;
        cin >> type >> X;
        
        if(type == 1) {
            cin >> Y;
            boxes[X] += Y; // Add Y balls to box X
        } else if(type == 2) {
            boxes.erase(X); // Remove all balls from box X
        } else if(type == 3) {
            cout << boxes[X] << endl; // Print the number of balls in box X
        }
    }
    
    return 0;
}
