class Solution:
    # @param A : list of integers
    # @return an integer
    def majorityElement(self, A):
        # Initialize candidate and count
        candidate = A[0]
        count = 1

        # Find the candidate element
        for num in A[1:]:
            if num == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = num
                    count = 1

        # Verify if the candidate is the majority element
        count = 0
        for num in A:
            if num == candidate:
                count += 1

        if count > len(A) // 2:
            return candidate
