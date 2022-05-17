# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        prev = None
        curr = head
        
        while curr:
            if curr.next and (curr.val == curr.next.val):
                node = curr
                while node and (curr.val == node.val):
                    node = node.next
                
                if prev:
                    prev.next = node
                else:
                    # for example, in case [1,1,1,2,3]
                    head = node
                
                curr = node
            else:
                prev = curr
                curr = curr.next
        return head
