class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        def findSubsets(ind,nums,ans,path):
            
            ans.append(path[:])
            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]:
                    continue   
                path.append(nums[i])
                findSubsets(i+1,nums,ans,path)
                path.pop()
        nums.sort()
        findSubsets(0,nums,ans,[])
        return ans
        