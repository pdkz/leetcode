# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        postorder_val = postorder[-1]
        node = TreeNode(val=postorder_val)
        inorder_index = inorder.index(postorder_val)

        node.left = self.buildTree(inorder[:inorder_index], postorder[:inorder_index])
        node.right = self.buildTree(inorder[inorder_index+1:], postorder[inorder_index:len(postorder)-1])
        
        return node