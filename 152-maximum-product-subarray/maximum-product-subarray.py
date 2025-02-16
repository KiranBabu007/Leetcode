class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=max(nums)
        pre,suf=1,1

        for i in range(len(nums)):
            if not pre:
                pre=1
            if not suf:
                suf=1
            pre*=nums[i]
            suf*=nums[len(nums)-i-1]
            res=max(res,pre,suf)
        return res