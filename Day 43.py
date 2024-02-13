class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        # Step 1: Calculate the mean
        mean = sum(A) / len(A)
        
        # Step 2: Calculate the sum of squared differences
        sum_squared_diff = sum((x - mean) ** 2 for x in A)
        
        # Step 3: Calculate the variance
        variance = sum_squared_diff / len(A)
        
        # Step 4: Return the variance rounded to two decimal points
        return "{:.2f}".format(variance)
