class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # Check if the year is divisible by 4 and not divisible by 100
        # or it is divisible by 400
        if (A % 4 == 0 and A % 100 != 0) or (A % 400 == 0):
            return 1  # Leap year
        else:
            return 0  # Not a leap year
