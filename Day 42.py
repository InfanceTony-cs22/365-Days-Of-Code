# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        # Handle edge case where the list is empty
        if not A:
            return None
        
        # Initialize two pointers
        fast = A
        slow = A
        
        # Move fast pointer forward by B steps
        for _ in range(B):
            if fast.next:
                fast = fast.next
            else:
                # If B is greater than the size of the list, remove the first node
                return A.next
        
        # Move both pointers simultaneously until fast reaches the end of the list
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        # Remove the B-th node by updating the next pointer of the previous node
        prev.next = slow.next
        
        return A
