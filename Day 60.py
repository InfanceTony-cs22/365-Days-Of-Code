class Solution:
    def addTwoNumbers(self, A, B):
        # Initialize dummy node for result list
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Traverse both linked lists simultaneously
        while A is not None or B is not None:
            # Get the values of current nodes or 0 if node is None
            val1 = A.val if A else 0
            val2 = B.val if B else 0

            # Calculate sum with carry
            total = val1 + val2 + carry

            # Update carry and digit for next iteration
            carry = total // 10
            digit = total % 10

            # Create a new node with the digit and attach it to the result list
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes in both linked lists if they exist
            if A:
                A = A.next
            if B:
                B = B.next

        # Add any remaining carry to the result list
        if carry > 0:
            current.next = ListNode(carry)

        # Return the head of the result list
        return dummy.next
