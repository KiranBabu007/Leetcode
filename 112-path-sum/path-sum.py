# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        
        def dfs(node,s):
            if not node:
                return False
            s+=node.val
            if not node.left and not node.right:
                return s==targetSum
            return dfs(node.left,s) or dfs(node.right,s)

        return dfs(root,0)

        