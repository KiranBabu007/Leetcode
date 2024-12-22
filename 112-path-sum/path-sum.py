# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        sum=0
        def dfs(node,s):
            
            if not node:
                return False
            s+=node.val
            if s==targetSum and not node.left and not node.right:
                return True     
            l=dfs(node.left,s)
            r=dfs(node.right,s)
            
            return l or r
        
        return dfs(root,0)

        