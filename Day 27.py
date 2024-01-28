class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        char_freq = {}
        
        # Count the frequency of each character in the string
        for char in A:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        odd_count = 0
        
        # Count the number of characters with odd frequency
        for freq in char_freq.values():
            if freq % 2 == 1:
                odd_count += 1
        
        # If there is at most one character with odd frequency, it can be rearranged into a palindrome
        return 1 if odd_count <= 1 else 0
