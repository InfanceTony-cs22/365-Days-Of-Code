class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        # Helper function to find the intersection point of two pointers
        def findIntersection(head):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return None
        
        if not A or not A.next:
            return None
        
        # Find the intersection point using Floyd's Tortoise and Hare algorithm
        intersection = findIntersection(A)
        
        # If there's no intersection point, there's no cycle
        if not intersection:
            return None
        
        # Move one pointer to the head and keep the other at the intersection point
        # Then, move both pointers one step at a time until they meet; the meeting point will be the start of the cycle
        ptr1 = A
        ptr2 = intersection
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
