# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = head
        prev = None
        
        while(node != None):
            if node.val == val:
                if prev == None:
                    head = node.next
                    node = head
                else:
                    prev.next = node.next
                    node = prev.next   
            else:
                prev = node
                node = node.next
                
        return head
