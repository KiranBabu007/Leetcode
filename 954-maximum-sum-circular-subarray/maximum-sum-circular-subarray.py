class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curmax=0
        minSum=nums[0]
        maxSum=nums[0]
        curmin=0
        
        for i in nums:
            curmax=max(curmax+i,i)
            curmin=min(curmin+i,i)
            if curmax>maxSum:
                maxSum=curmax
            if curmin<minSum:
                minSum=curmin

        if maxSum<0:
            return maxSum
        return max(maxSum,sum(nums)-minSum)
        