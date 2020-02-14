# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:       
        nums_len = len(nums)
        if nums_len == 0:
            return None
        
        def recursion(nums, tree):
            l = len(nums)
            if l < 2:
                return
            m = l // 2

            low = nums[0:m]
            high = nums[m+1:]

            low_len = len(low)
            high_len = len(high)
            if low_len > 0:
                tree.insert(low[low_len//2])
            if high_len > 0:
                tree.insert(high[high_len//2])
            
            recursion(low, tree)
            recursion(high, tree)
            
            return tree
        
        tree = BST()
        tree.insert(nums[nums_len//2])
        
        recursion(nums, tree)
        
        return tree.root
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)
    
    def _insert(self, node, val):
        if node == None:
            return
        
        if val < node.val:
            if node.left == None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        elif val >= node.val:
            if node.right == None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)
