/*
#include<iostream>
using namespace std;
*/

void solve(int *A, int *B){
if (A && B) {
        
        int sum = *A + *B;
        int diff = abs(*A - *B);
        
        // Update values in memory
        *A = sum;
        *B = diff;
    }
}



/*
int main()  {
    int A, B;
    int *pA = &A, *pB = &B;
    cin>>A>>B;
    solve(pA, pB);
    cout<<A<<endl;
    cout<<B<<endl;
    return 0;
}
*/
