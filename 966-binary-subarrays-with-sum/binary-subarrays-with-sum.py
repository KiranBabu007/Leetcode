class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def lessthan(g):
            if g<0:
                return 0
            s=0
            l=0
            ans=0
            for r in range(len(nums)):
                s+=nums[r]
                while(s>g):
                    s-=nums[l]
                    l+=1
                ans+=r-l+1
            return ans

        return lessthan(goal)-lessthan(goal-1)





