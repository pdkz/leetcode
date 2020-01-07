# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        prev_node = None
        while(node != None):
            if prev_node is not None and node.val == prev_node.val:
                prev_node.next = node.next
                node = prev_node
            else:
                prev_node = node
            
            node = node.next
        
        return head
