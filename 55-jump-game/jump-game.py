class Solution(object):
    def canJump(self, nums):
        ans=0
        n=len(nums)
        for i in range(n):
            if i>ans:
                return False
            ans=max(ans,i+nums[i])
            if ans>=n-1:
                return True
        return True
            
            

        