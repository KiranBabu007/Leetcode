class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum=0
        maxSum=nums[0]
        
        for i in nums:
            curSum=max(curSum+i,i)
            maxSum=max(curSum,maxSum)
        return maxSum