# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def dfs(node,maxValue):
            if not node:
                return 0
            r=1 if node.val >= maxValue else 0
            maxValue=max(node.val,maxValue)
            r+=dfs(node.left,maxValue)
            r+=dfs(node.right,maxValue)

            return r

        return dfs(root,root.val)
        