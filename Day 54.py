class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        max_reachable = 0
        n = len(A)
        for i in range(n):
            if i > max_reachable:
                return 0
            max_reachable = max(max_reachable, i + A[i])
            if max_reachable >= n - 1:
                return 1
        return 1  # This line is reached when the last index is already reached
