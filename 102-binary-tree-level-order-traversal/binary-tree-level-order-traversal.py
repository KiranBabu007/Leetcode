# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        q=deque([root])
        ans=[]
        ans.append([root.val])
        while q:
            l=[]
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                    l.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    l.append(node.right.val)
            ans.append(l)
        return ans[:-1]
                
        