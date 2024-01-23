class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        # Split the input string into a list of words
        words = A.split()

        # Reverse the list of words
        reversed_words = words[::-1]

        # Join the reversed list of words into a single string
        reversed_string = ' '.join(reversed_words)

        return reversed_string
