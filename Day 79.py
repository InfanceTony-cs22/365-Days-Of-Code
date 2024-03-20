class Solution:
    def numDistinct(self, A, B):
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Empty string can form an empty subsequence
        dp[0][0] = 1

        # Initialize the first row (for empty string A)
        for j in range(1, n + 1):
            dp[0][j] = 0

        # Initialize the first column (for non-empty string A)
        for i in range(1, m + 1):
            dp[i][0] = 1

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]

