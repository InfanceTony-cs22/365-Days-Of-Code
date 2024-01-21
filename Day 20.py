# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        if A is None or A.next is None:
            return A

        # Split the linked list into two halves
        mid = self.find_middle(A)
        left_half = A
        right_half = mid.next
        mid.next = None

        # Recursively sort the two halves
        left_sorted = self.sortList(left_half)
        right_sorted = self.sortList(right_half)

        # Merge the sorted halves
        sorted_list = self.merge(left_sorted, right_sorted)
        
        return sorted_list

    def find_middle(self, head):
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        dummy = ListNode(0)
        current = dummy

        while left is not None and right is not None:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # Append the remaining nodes of either left or right
        if left is not None:
            current.next = left
        elif right is not None:
            current.next = right

        return dummy.next
