class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        def backtrack(nums, path, res):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]], res)
        
        permutations = []
        backtrack(A, [], permutations)
        return permutations
