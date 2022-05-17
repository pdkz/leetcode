# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = []
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        path = []
        self.traverse(root, sum, path)
        return self.result
    
    def traverse(self, node, s, path):
        if node == None:
            return
        
        path.append(node.val)
        
        self.traverse(node.left, s, path)
        self.traverse(node.right, s, path)
        
        if node.left == None and node.right == None:
            pathsum = sum(path)            
            if sum(path) == s:
                self.result.append(path.copy())

        path.pop()
