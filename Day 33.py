class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        sock_count = {}
        pair_count = 0

        for sock in A:
            if sock in sock_count:
                sock_count[sock] += 1
                if sock_count[sock] % 2 == 0:
                    pair_count += 1
            else:
                sock_count[sock] = 1

        return pair_count
