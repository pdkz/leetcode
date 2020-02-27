# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.paths = []
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path = []
        self.traverse(root, path)
        
        return self.paths
    
    def traverse(self, node, path):
        if node == None:
            return

        path.append(node.val)
        
        self.traverse(node.left, path)
        self.traverse(node.right, path)
        
        if node.left == None and node.right == None:
            self.paths.append('->'.join([str(_) for _ in path]))
            
        path.pop()
