class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        if not A or not B:
            return None
        
        # Pointers for both lists
        ptr1 = A
        ptr2 = B
        
        # Traverse both lists until they intersect or reach the end
        while ptr1 != ptr2:
            # Move ptr1 to the next node
            ptr1 = ptr1.next if ptr1 else B
            # Move ptr2 to the next node
            ptr2 = ptr2.next if ptr2 else A
        
        # Return the intersection node (or None if no intersection)
        return ptr1
