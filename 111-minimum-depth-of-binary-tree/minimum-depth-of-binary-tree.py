class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:  
            return 0
        c=0
        def dfs(node,c):
            if not node:
                return float('inf')
            if not node.left and not node.right:
                return c
            return min(dfs(node.left,c+1),dfs(node.right,c+1))
                
        return dfs(root,1)
        