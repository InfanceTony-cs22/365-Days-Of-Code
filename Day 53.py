class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        left = 0
        right = 1
        n = len(A)
        
        # Traverse the array with two pointers
        while right < n:
            diff = A[right] - A[left]
            if diff == B:
                return 1
            elif diff < B:
                right += 1
            else:
                left += 1
                if left == right:
                    right += 1
        
        return 0
