# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        curr = head
        prev = None
        while curr:
            if prev and (prev.val == curr.val):
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return head
