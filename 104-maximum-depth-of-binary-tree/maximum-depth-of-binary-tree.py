# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        h=0
        m=0
        def height(h,root):
            if not root:
                return h
            right=height(h+1,root.right)
            left=height(h+1,root.left)
            return max(left,right)
        return height(0,root)
        