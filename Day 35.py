class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A <= 1:
            return 1

        # Initialize an array to store the number of ways to reach each step
        dp = [0] * (A + 1)

        # There's 1 way to reach the 0th step (base case)
        dp[0] = 1

        # There's 1 way to reach the 1st step (base case)
        dp[1] = 1

        # Calculate the number of ways for each step starting from step 2
        for i in range(2, A + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # The final result is the number of ways to reach the top step
        return dp[A]
