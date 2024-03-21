class Solution:
    # Function to find the middle of the linked list
    def findMiddle(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Function to reverse a linked list
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    # Function to merge two linked lists alternatively
    def mergeLists(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy
        while head1 and head2:
            tail.next = head1
            head1 = head1.next
            tail = tail.next
            tail.next = head2
            head2 = head2.next
            tail = tail.next
        if head1:
            tail.next = head1
        return dummy.next

    # Main function to reorder the linked list
    def reorderList(self, head):
        if not head or not head.next:
            return head

        # Find the middle of the linked list
        middle = self.findMiddle(head)

        # Reverse the second half of the linked list
        second_half = self.reverseList(middle.next)
        middle.next = None  # Break the linked list into two halves

        # Merge the first half with the reversed second half
        return self.mergeLists(head, second_half)
