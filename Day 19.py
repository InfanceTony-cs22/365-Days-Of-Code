# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        # Initialize a dummy node as the starting point of the merged list
        dummy = ListNode(0)
        # Create a pointer to the current node in the merged list
        current = dummy

        # Iterate until either A or B becomes None
        while A is not None and B is not None:
            if A.val < B.val:
                current.next = A
                A = A.next
            else:
                current.next = B
                B = B.next
            # Move the current pointer to the last added node
            current = current.next

        # If there are remaining nodes in A, append them to the merged list
        while A is not None:
            current.next = A
            A = A.next
            current = current.next

        # If there are remaining nodes in B, append them to the merged list
        while B is not None:
            current.next = B
            B = B.next
            current = current.next

        # The merged list starts from the next of the dummy node
        return dummy.next
