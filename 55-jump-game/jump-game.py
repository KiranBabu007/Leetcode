class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        pindex=nums[0]

        for i in range(len(nums)):
            if i <=pindex:
                pindex=max(pindex,nums[i]+i)
            if pindex>=len(nums)-1:
                return True
        return False

        
        