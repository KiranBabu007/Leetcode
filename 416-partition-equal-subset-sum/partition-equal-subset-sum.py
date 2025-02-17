class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo={}
        def helper(n,i):
            if (n,i) in memo:
                return memo[(n,i)]
            if n==0:
                return True
            if n<0 or i>=len(nums): 
                return False
            memo[(n,i)]=helper(n-nums[i],i+1) or helper(n,i+1)
            return memo[(n,i)]
            
        t=sum(nums)

        if t%2!=0:
            return False

        target=t//2
    
        return helper(target,0)

        