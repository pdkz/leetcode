# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
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
