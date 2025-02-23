class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l=0
        r=len(nums)-1
        c=0
        while l<r:
            if nums[l]+nums[r]>k:
                r-=1
            elif nums[l]+nums[r]<k:
                l+=1
            else:
                c+=1
                l+=1
                r-=1
        return c
        