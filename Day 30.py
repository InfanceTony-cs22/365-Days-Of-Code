class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        # Initialize an array to store the frequency of characters
        frequency = [0] * 26

        # Iterate through the string and count the frequency of each character
        for char in A:
            # Check if the character is a lowercase alphabet
            if 'a' <= char <= 'z':
                frequency[ord(char) - ord('a')] += 1

        return frequency
