class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        # Initialize current pointer to the head of the linked list
        current = A
        
        # Traverse the linked list
        while current and current.next:
            # Check if current node's value is equal to next node's value
            if current.val == current.next.val:
                # Skip the next node by updating the next pointer
                current.next = current.next.next
            else:
                # Move the current pointer to the next node
                current = current.next
        
        # Return the head of the modified linked list
        return A
