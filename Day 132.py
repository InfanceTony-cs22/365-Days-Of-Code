#include <queue>
#include <vector>
using namespace std;

int solve(vector<int> &A) {
    int minCost = 0;
    
    // Create a min heap priority queue
    priority_queue<int, vector<int>, greater<int>> pq(A.begin(), A.end());
    
    // Keep merging the two shortest ropes until there's only one rope left
    while (pq.size() > 1) {
        int rope1 = pq.top();
        pq.pop();
        int rope2 = pq.top();
        pq.pop();
        
        int mergedRope = rope1 + rope2;
        minCost += mergedRope;
        
        pq.push(mergedRope); // Push the merged rope back into the priority queue
    }
    
    return minCost;
}
