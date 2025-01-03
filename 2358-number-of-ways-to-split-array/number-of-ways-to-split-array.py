class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        n=len(nums)-1
        prefix=sum(nums)
        l=0
        for i in range(n):
            l+=nums[i]
            r=prefix-l
            if l>=r:
                c+=1
        return c
    
        