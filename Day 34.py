class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, word):
        # Helper function to check if a word is a palindrome
        return word == word[::-1]

    def solve(self, A):
        # Tokenize the sentence into words
        words = A.split()

        # Initialize a counter for palindromic words
        count = 0

        # Check each word for palindromicity
        for word in words:
            if self.isPalindrome(word.lower()):  # Convert to lowercase for case-insensitivity
                count += 1

        return count
