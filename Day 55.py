class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        if not A:
            return 0
        
        n = len(A)
        
        # Starting from the second last row and moving upwards
        for i in range(n - 2, -1, -1):
            for j in range(len(A[i])):
                # For each element, update it with the minimum sum path from the two adjacent elements in the row below
                A[i][j] += min(A[i + 1][j], A[i + 1][j + 1])
        
        # The top element of the triangle will have the minimum sum path
        return A[0][0]
