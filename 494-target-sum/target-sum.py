class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo={}
        n=len(nums)
        ans=0
        def ways(i,s):
            if (i,s) in memo:
                return memo[(i,s)]
            if i==n and target==s:
                return 1
            if i>=n:
                return 0
            
            ans=ways(i+1,s+nums[i])+ways(i+1,s-nums[i])
            memo[(i,s)]=ans

            return ans
            
        return ways(0,0)
