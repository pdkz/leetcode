# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        prev_node = None
        curr_node = head
        next_node = head.next
        
        while(curr_node is not None):
            node = next_node
            duplicated = 0
            while(node is not None and node.val == curr_node.val):
                node = node.next
                duplicated += 1
            if duplicated > 0:
                if prev_node is None:
                    curr_node = node
                    head = curr_node
                    if curr_node is None: break
                    next_node = curr_node.next
                else:
                    prev_node.next = node
                    curr_node = node
                    if curr_node is None: break
                    next_node = curr_node.next
            else:
                prev_node = curr_node
                curr_node = curr_node.next
                if curr_node is None: break
                next_node = curr_node.next
            
        return head
  
