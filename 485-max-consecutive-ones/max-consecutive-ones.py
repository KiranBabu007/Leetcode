class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        maxcount=0
        for num in nums:
            if num:
                count+=1
            else:
                maxcount=max(maxcount,count)
                count=0
        maxcount=max(maxcount,count)
        return maxcount
            
            