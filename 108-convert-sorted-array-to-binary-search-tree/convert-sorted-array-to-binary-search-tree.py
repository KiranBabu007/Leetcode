# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def helper(l,r):

            if l>r:
                return
            m=(l+r)//2
            node=TreeNode(nums[m])
            node.left=helper(l,m-1)
            node.right=helper(m+1,r)

            return node
    
        return helper(0,len(nums)-1)

        