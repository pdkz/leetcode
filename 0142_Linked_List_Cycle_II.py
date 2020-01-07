# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        nodes = set()
        while(head is not None):
            if head in nodes:
                print(head.val)
                return head
            nodes.add(head)
            head = head.next
            
        return None
