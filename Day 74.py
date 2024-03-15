class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        # Base case: if A is None or A is the last node
        if A is None or A.next is None:
            return A
        # Reverse the rest of the linked list
        rest = self.reverseList(A.next)
        # Set A's next node's next to A itself
        A.next.next = A
        # Set A's next to None to break the original connection
        A.next = None
        return rest
