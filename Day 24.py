class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        # Base case
        if B == 0:
            return A
        # Recursive case
        return self.gcd(B, A % B)
