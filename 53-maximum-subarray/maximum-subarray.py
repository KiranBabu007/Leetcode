class Solution(object):
    def maxSubArray(self, nums):

        if not nums:
            return
        curr=0
        sum=nums[0]
        for i in nums:
            if curr<0:
                curr=0
            curr+=i
            sum=max(sum,curr)

        return sum
        