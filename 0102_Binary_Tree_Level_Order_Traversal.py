# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        queue = [(0, root)]
        ht = collections.defaultdict(list)
        
        while(len(queue) != 0):
            lv, node = queue.pop(0)
            
            left = node.left
            right = node.right
            
            ht[lv].append(node.val)
            
            if left != None:
                queue.append((lv+1, left))
            if right != None:
                queue.append((lv+1, right))

        return list(ht.values())
