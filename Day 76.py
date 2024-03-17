class Solution:
    def isPower(self, A):
        if A == 1:
            return 1
        for i in range(2, int(A ** 0.5) + 1):
            p = 2
            while i ** p <= A:
                if i ** p == A:
                    return 1
                p += 1
        return 0
