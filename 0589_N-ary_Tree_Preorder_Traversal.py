"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.vals = []
        
    def preorder(self, root: 'Node') -> List[int]:
        self.traversal(root)
        return self.vals
    
    def traversal(self, node):
        if node == None:
            return
        
        self.vals.append(node.val)
        
        for child in node.children:
            self.traversal(child)

        
            
