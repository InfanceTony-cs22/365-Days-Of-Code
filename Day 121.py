/*
#include<iostream>
#include<string>
using namespace std;
*/

int main()  {
    string A, B;
    cin>>A>>B;
    // YOUR CODE GOES HERE
cout << A.size() << " " << B.size() << endl;

    // Second line: Concatenate A and B
    cout << A + B << endl;

    // Third line: Swap the first characters of A and B
    swap(A[0], B[0]);
    cout << A << " " << B << endl;

    return 0;
}
  
