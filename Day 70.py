class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        def backtrack(start, comb):
            if len(comb) == B:
                result.append(comb[:])
                return
            for i in range(start, A + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        result = []
        backtrack(1, [])
        return result
