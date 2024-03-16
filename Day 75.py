class Solution:
    def fourSum(self, A, B):
        A.sort()
        n = len(A)
        res = []
        
        for i in range(n):
            for j in range(i+1, n):
                target = B - A[i] - A[j]
                left, right = j + 1, n - 1
                
                while left < right:
                    total = A[left] + A[right]
                    if total == target:
                        res.append([A[i], A[j], A[left], A[right]])
                        left += 1
                        right -= 1
                        while left < right and A[left] == A[left - 1]:
                            left += 1
                        while left < right and A[right] == A[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        # Remove duplicates
        unique_res = []
        for quad in res:
            if quad not in unique_res:
                unique_res.append(quad)
        
        return unique_res
