class Solution:
    def sortColors(self, A):
        # Initialize pointers
        low = 0
        mid = 0
        high = len(A) - 1

        # Iterate through the array
        while mid <= high:
            if A[mid] == 0:
                # Swap element at mid with element at low
                A[low], A[mid] = A[mid], A[low]
                # Move low and mid pointers forward
                low += 1
                mid += 1
            elif A[mid] == 1:
                # Leave element at mid in place
                mid += 1
            else:  # A[mid] == 2
                # Swap element at mid with element at high
                A[mid], A[high] = A[high], A[mid]
                # Move high pointer backward
                high -= 1

        return A
