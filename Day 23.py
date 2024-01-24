class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        modulo_value = 10**7
        # Directly return the sum of A and B modulo 10^7
        return (A + B) % modulo_value
