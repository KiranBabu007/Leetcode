# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def invert(node):
            if not node:
                return 
            invert(node.left)
            invert(node.right)
            node.left,node.right=node.right,node.left

            return node
        return invert(root)

        