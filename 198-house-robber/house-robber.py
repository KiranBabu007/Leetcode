class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        rob1,rob2=0,0

        for i in nums:
            temp=max(i+rob1,rob2)
            rob1=rob2
            rob2=temp
        return max(rob1,rob2)
        