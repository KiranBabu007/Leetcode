# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.l=[]
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            self.l.append(node.val)
            inorder(node.right)
            
        inorder(root)
        return self.l==sorted(self.l) and len(self.l)==len(list(set(self.l)))
        

        
        