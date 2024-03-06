class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        # Create a dictionary to store the mapping of original nodes to their copies
        node_map = {}
        
        # First pass: create copies of all nodes and store them in the dictionary
        curr = head
        while curr:
            node_map[curr] = RandomListNode(curr.label)
            curr = curr.next
        
        # Second pass: assign next and random pointers for the copies
        curr = head
        while curr:
            copy_node = node_map[curr]
            copy_node.next = node_map.get(curr.next)
            copy_node.random = node_map.get(curr.random)
            curr = curr.next
        
        return node_map[head]
