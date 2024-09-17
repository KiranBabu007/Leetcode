class Solution(object):
    def canJump(self, nums):
        ans=nums[0]
        for i in range(len(nums)):
            if i>ans:
                return False
            ans=max(ans,i+nums[i])
        return True
            
            

        