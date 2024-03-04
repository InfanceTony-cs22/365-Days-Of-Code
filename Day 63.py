class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        result = 0
        # Iterate through each bit of A
        for _ in range(32):
            # Extract the least significant bit of A
            bit = A & 1
            # Shift A to the right by 1 bit
            A >>= 1
            # Shift result to the left by 1 bit
            result <<= 1
            # If bit is 1, set the corresponding bit in result to 1
            if bit:
                result |= 1
        return result
