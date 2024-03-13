class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if not A:
            return 0
        
        n = len(A)
        # Initialize dp table to store the minimum cost for each house and color
        dp = [[0] * 3 for _ in range(n)]
        
        # Base case: the cost of painting the first house is the same as the cost matrix
        dp[0] = A[0]
        
        # Iterate through the rest of the houses
        for i in range(1, n):
            # Calculate the minimum cost for painting each color of the current house
            dp[i][0] = A[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = A[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = A[i][2] + min(dp[i-1][0], dp[i-1][1])
        
        # Return the minimum cost of painting the last house
        return min(dp[n-1])
