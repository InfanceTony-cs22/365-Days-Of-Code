class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        # Initialize pointers
        prev = None
        current = A
        next = None
        
        # Iterate through the linked list
        while current:
            # Store the next node
            next = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move pointers forward
            prev = current
            current = next
        
        # Update the head of the linked list
        A = prev
        
        # Return the new head
        return A
