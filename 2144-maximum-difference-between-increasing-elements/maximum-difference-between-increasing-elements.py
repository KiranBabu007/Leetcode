class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=1
        maxdif=-1
        while r<len(nums):
            if nums[l]<nums[r]:
                maxdif=max(maxdif,nums[r]-nums[l])
            else:
                l=r
            r+=1
        return maxdif
        