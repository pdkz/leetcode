# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lnode = l1
        rnode = l2
        node = None
        head = None
        prev = None
        while(True):
            if lnode == None and rnode == None:
                break        
            if lnode == None:
                node = ListNode(rnode.val)
                if prev is not None:
                    prev.next = node
                prev = node
                rnode = rnode.next
            elif rnode == None:
                node = ListNode(lnode.val)
                if prev is not None:
                    prev.next = node
                prev = node
                lnode = lnode.next
            elif lnode.val <= rnode.val:
                node = ListNode(lnode.val)
                if prev is not None:
                    prev.next = node
                prev = node
                lnode = lnode.next
            elif lnode.val > rnode.val:
                node = ListNode(rnode.val)
                if prev is not None:
                    prev.next = node
                prev = node
                rnode = rnode.next

            if head == None:
                head = prev
        
        return head
