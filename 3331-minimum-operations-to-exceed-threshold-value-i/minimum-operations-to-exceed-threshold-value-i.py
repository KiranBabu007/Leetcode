class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans=0
        while(nums[ans]<k):
            ans+=1
        else:
            return ans
        