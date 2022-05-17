class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]

        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)        

        dfs(root, None)
        
        ans = []
        seen = set()
        queue = deque([[target, 0]])
        
        while queue:
            node, level = queue.popleft()
            
            if level == k and target != node:
                ans.append(node.val)
            
            if not node in seen:
                if node.left and not node.left in seen:
                    queue.append([node.left, level+1])
                if node.right and not node.right in seen:
                    queue.append([node.right, level+1])
                if node.parent and not node.parent in seen:
                    queue.append([node.parent, level+1])

                seen.add(node)
            
        return ans