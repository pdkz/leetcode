# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        d = collections.defaultdict(int)
        
        nodeA = headA
        nodeB = headB
        while(nodeA != None or nodeB != None):
            if nodeA != None:
                d[nodeA] += 1
                nodeA = nodeA.next
            if nodeB != None:
                d[nodeB] += 1 
                nodeB = nodeB.next

        intersection_node = [node for node, v in d.items() if v == 2]
        if len(intersection_node) > 0:
            return intersection_node[0]
        
        return None
