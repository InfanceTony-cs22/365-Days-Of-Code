class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        m = len(A)
        n = len(A[0])

        # Initialize dp array
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = A[0][0]

        # Fill the first row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + A[0][j]

        # Fill the first column
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + A[i][0]

        # Fill the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + A[i][j]

        return dp[m - 1][n - 1]
