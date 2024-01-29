class Solution:
    # @param A : string
    # @return a string
    def solve(self, A):
        result = ""
        for char in A:
            # Toggle case for each character
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        return result
