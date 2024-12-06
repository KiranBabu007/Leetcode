class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        def findSubsets(ind,nums,ans,path):
            if ind==len(nums):
                ans.append(path[:])
                
                return
           
            
            findSubsets(ind+1,nums,ans,path)
            path.append(nums[ind])
            
            findSubsets(ind+1,nums,ans,path)
            path.pop()
        
        findSubsets(0,nums,ans,[])
        return ans
        