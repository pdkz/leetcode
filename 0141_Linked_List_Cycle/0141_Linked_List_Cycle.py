# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
    
        slow = head
        fast = head
        while(slow is not None):
            if fast.next is None or fast.next.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
        
        """
        node = head
        if node is None:
            return False
        nodelist = []
        while(1):
            node = node.next
            if node in nodelist:
                return True
            if node is None:
                return False
            
            nodelist.append(node)
        """
