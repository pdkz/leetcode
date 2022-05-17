# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        n = node
        p = None
        while(n != None):
            if n.next == None:
                p.next = None
                break
                
            tmp = n.val
            n.val = n.next.val
            n.next.val = tmp
            
            p = n
            n = n.next
