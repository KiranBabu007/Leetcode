# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        res=[]
        path=''
        if root==None:
            return
        path=str(root.val)

        if root.left==None and root.right==None:
            res.append(path)
            return res
        
        if root.left!=None:
            self.DFS(root.left,res,path)
        if root.right!=None:
            self.DFS(root.right,res,path)

        return res
        

    def DFS(self,root,res,path):
        path+='->'+str(root.val)

        if root.left==None and root.right==None:
            res.append(path)
            return
        
        if root.left!=None:
            self.DFS(root.left,res,path)
        if root.right!=None:
            self.DFS(root.right,res,path)


        