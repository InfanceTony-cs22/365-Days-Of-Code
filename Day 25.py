class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        count_A = sum(1 for num in A if num > C)
        count_B = sum(1 for num in B if num < C)
        return max(count_A, count_B)
