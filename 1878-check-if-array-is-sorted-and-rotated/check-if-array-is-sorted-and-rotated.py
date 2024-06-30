class Solution(object):
    def check(self, nums):
        
        
        for i in range(len(nums)):
            
            if nums[i:] + nums[:i]==sorted(nums):
                return True
        return False
            


        