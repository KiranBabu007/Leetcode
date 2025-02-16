class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=float('-inf')
        pre,suf=1,1

        for i in range(len(nums)):
            if pre==0:
                pre=1
            if suf==0:
                suf=1
            pre*=nums[i]
            suf*=nums[len(nums)-i-1]
            res=max(res,pre,suf)
        return res