#include<iostream>
#include <vector>
#include<algorithm>
using namespace std;

int main()  {
    int N;
    cin >> N;
    vector<int> v(N);
    for (int i = 0; i < N; ++i) {
        cin >> v[i];
    }
    int X;
    cin >> X;
    v.erase(v.begin() + X);
    sort(v.begin(), v.end());
    for (int i = 0; i < v.size(); ++i) {
        cout << v[i] << endl;
    }
    return 0;
}
