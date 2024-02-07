class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        # Initialize a dummy node
        dummy = ListNode(0)
        dummy.next = A
        prev = dummy
        
        # Traverse the linked list in pairs
        while A and A.next:
            # Nodes to be swapped
            first = A
            second = A.next
            
            # Swap the nodes
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move pointers forward
            prev = first
            A = first.next
        
        return dummy.next
