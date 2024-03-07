class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        rows = len(A)
        cols = len(A[0])
        low = 0
        high = rows * cols - 1
        
        # Binary search
        while low <= high:
            mid = (low + high) // 2
            mid_val = A[mid // cols][mid % cols]
            if mid_val == B:
                return 1
            elif mid_val < B:
                low = mid + 1
            else:
                high = mid - 1
        return 0
