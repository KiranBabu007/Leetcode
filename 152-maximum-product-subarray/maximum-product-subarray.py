class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curmin,curmax=1,1
        res=max(nums)
        for n in nums:
            t=n*curmin
            curmin=min(n*curmin,n*curmax,n)
            curmax=max(t,n*curmax,n)
            
            res=max(res,curmax)
        return res