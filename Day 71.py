class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        def dfs(i, j):
            if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] != 'X':
                return
            A[i] = A[i][:j] + 'O' + A[i][j + 1:]
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 'X':
                    dfs(i, j)
                    count += 1
        return count
