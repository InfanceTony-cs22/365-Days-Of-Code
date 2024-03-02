class Solution:
    def subsetsWithDup(self, A):
        # Sort the input list
        A.sort()

        # Define a recursive function to generate subsets
        def generate_subsets(index, subset, result):
            # Append the current subset to the result list
            result.append(subset[:])

            # Iterate through the elements starting from the current index
            for i in range(index, len(A)):
                # Skip duplicates
                if i > index and A[i] == A[i - 1]:
                    continue
                # Recursively call the function with the next index
                generate_subsets(i + 1, subset + [A[i]], result)

        # Initialize an empty result list
        result = []

        # Call the recursive function to generate subsets
        generate_subsets(0, [], result)

        # Return the result list
        return result
