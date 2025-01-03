class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        n=len(nums)
        l,r=sum(nums[:1]),sum(nums[1:])
        for i in range(1,n):
            print(l,r)
            if l>=r:
                c+=1
            l+=nums[i]
            r-=nums[i]
            
        return c
    
        