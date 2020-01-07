# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h1 = l1
        h2 = l2
        n = 0
        s = 0
        while(h1 is not None or h2 is not None):
            v1 = 0
            v2 = 0
            
            digit = 10 ** n
            
            if h1 is not None:
                v1 = h1.val
                h1 = h1.next
            if h2 is not None:
                v2 = h2.val
                h2 = h2.next
            
            s = s + (v1 + v2) * digit
            n += 1

        s = str(s)
        head = None
        prev = None
        for i, d in enumerate(s[::-1]):
            l = ListNode(int(d))
            if prev is not None:
                prev.next = l
            if i == 0:
                head = l
            prev = l
            
        return head
