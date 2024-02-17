class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)
        n = len(A[0])
        
        # Check if the first row needs to be set to zero
        first_row_zero = any(A[0][j] == 0 for j in range(n))
        
        # Check if the first column needs to be set to zero
        first_col_zero = any(A[i][0] == 0 for i in range(m))
        
        # Mark rows and columns based on the values in the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                if A[i][j] == 0:
                    A[i][0] = 0
                    A[0][j] = 0
        
        # Set rows to zero based on the first column
        for i in range(1, m):
            if A[i][0] == 0:
                for j in range(1, n):
                    A[i][j] = 0
        
        # Set columns to zero based on the first row
        for j in range(1, n):
            if A[0][j] == 0:
                for i in range(1, m):
                    A[i][j] = 0
        
        # Set the first row and first column to zero if necessary
        if first_row_zero:
            for j in range(n):
                A[0][j] = 0
        
        if first_col_zero:
            for i in range(m):
                A[i][0] = 0
        
        return A
