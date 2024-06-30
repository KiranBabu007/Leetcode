class Solution(object):
    def check(self, nums):
        l=sorted(nums)
        
        for i in range(len(nums)):
            new = nums[i:] + nums[:i]
            if new==l:
                return True
        return False
            


        