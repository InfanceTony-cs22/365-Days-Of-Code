/*
#include<iostream>
#include<sstream>
using namespace std;
*/

int main()  {
    string A;
    cin>>A;
    // YOUR CODE GOES HERE
     stringstream ss(A);
    
    char ch; // Storage area for the discarded commas
    int num; // Variable to store each integer
    
    // Extract integers separated by commas and print them
    while (ss >> num >> ch) {
        cout << num << endl;
    }
    
    // After the loop, print the last integer
    cout << num << endl;
    
    return 0;
    
    return 0;
}
