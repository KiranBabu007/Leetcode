class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        ans=0
        for r in range(len(nums)):
            if nums[r]==0:   
                l=r+1
                
            ans=max(ans,r-l+1)
        return ans
            