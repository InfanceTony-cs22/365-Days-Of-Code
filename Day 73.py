class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        # Transpose the matrix
        for i in range(n):
            for j in range(i+1, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        # Reverse each row of the transposed matrix
        for i in range(n):
            A[i].reverse()
        return A
