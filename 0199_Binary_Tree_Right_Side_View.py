class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        current = 0
        queue = [(1, root)]
        rsv = []
        while len(queue) > 0:
            height, node = queue.pop(0)
            if not node:
                break
            
            if height == current + 1:
                current = height
                rsv.append(node.val)
            
            if node.right:
                queue.append((current+1, node.right))
            if node.left:
                queue.append((current+1, node.left))
    
        return rsv
