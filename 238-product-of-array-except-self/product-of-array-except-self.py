
class Solution(object):
    
    def productExceptSelf(self, nums):
        n=len(nums)
        ans=[1]*n

        left=1
        for i in range(len(nums)):
           ans[i]=left
           left*=nums[i]

        right=1
        for i in range(len(nums)-1,-1,-1):
           ans[i]*=right
           right*=nums[i]
        return ans
    
        