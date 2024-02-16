class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        # Edge case: negative numbers are not palindromic
        if A < 0:
            return 0
        
        # Store the original number
        original = A
        reversed_num = 0
        
        # Reverse the digits of the number
        while A > 0:
            digit = A % 10
            reversed_num = reversed_num * 10 + digit
            A = A // 10
        
        # Check if the reversed number is equal to the original number
        return 1 if reversed_num == original else 0
