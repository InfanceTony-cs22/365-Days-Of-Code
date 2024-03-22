# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        # Edge case: If B and C are same, no need to reverse
        if B == C:
            return A
        
        # Create a dummy node to avoid handling special cases
        dummy = ListNode(0)
        dummy.next = A
        prev = dummy
        
        # Move prev to the (B-1)th node
        for _ in range(B - 1):
            prev = prev.next
        
        # Initialize pointers for reversing the sublist
        curr = prev.next
        next_node = curr.next
        
        # Reverse the sublist from B to C
        for _ in range(C - B):
            next_next = next_node.next
            next_node.next = curr
            curr = next_node
            next_node = next_next
        
        # Connect the reversed sublist with the rest of the list
        prev.next.next = next_node
        prev.next = curr
        
        return dummy.next
