class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # Convert the integer to a string to iterate through its digits
        digits = str(A)
        product = 1

        # Multiply each digit to calculate the product
        for digit in digits:
            product *= int(digit)

        return product
