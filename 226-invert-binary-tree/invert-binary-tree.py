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
        def swap(root):
            if not root:
                return
            if not root.left and not root.right:
                return      
            swap(root.left)
            swap(root.right)
            root.left,root.right=root.right,root.left
            
        swap(root)
        return root
        