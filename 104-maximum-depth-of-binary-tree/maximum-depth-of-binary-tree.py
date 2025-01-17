# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node,n):
            if not node:
                return n
            
            return max(dfs(node.left,n+1),
            dfs(node.right,n+1))

            
        return dfs(root,0)
        