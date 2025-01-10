class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=r=maxlen=0
        zero=0
        while(r<len(nums)):
            if nums[r]==0:
                zero+=1
            if(zero>k):
                if nums[l]==0:
                    zero-=1
                l+=1
            else:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
            

