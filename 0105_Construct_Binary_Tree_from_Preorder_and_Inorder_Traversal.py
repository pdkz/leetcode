# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        preorder_val = preorder[0]
        node = TreeNode(preorder_val)
        
        inorder_index = inorder.index(preorder_val)

        node.left = self.buildTree(preorder[1:inorder_index+1], inorder[:inorder_index])
        node.right = self.buildTree(preorder[inorder_index+1:], inorder[inorder_index+1:])
    
        return node