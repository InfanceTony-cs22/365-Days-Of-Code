class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A <= 1:
            return 0  # Not prime
        if A == 2 or A == 3:
            return 1  # Prime
        if A % 2 == 0 or A % 3 == 0:
            return 0  # Not prime

        i = 5
        while i * i <= A:
            if A % i == 0 or A % (i + 2) == 0:
                return 0  # Not prime
            i += 6
        return 1  # Prime
