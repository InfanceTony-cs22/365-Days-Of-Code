# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        # Find the length of the linked list
        length = 0
        current = A
        while current:
            length += 1
            current = current.next
        
        # Effective rotation
        k = B % length
        
        # If no rotation needed or linked list is empty
        if k == 0 or length == 0:
            return A
        
        # Find the (length - k)th node from the beginning
        slow = A
        fast = A
        for _ in range(k):
            fast = fast.next
        
        # Move both pointers simultaneously
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Update pointers to rotate the list
        new_head = slow.next
        slow.next = None
        current = new_head
        while current.next:
            current = current.next
        current.next = A
        
        return new_head
