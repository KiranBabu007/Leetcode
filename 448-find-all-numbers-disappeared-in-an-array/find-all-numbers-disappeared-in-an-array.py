class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[i for i in range(1,len(nums)+1)]
        ans=set(l)-set(nums)

        return list(ans)
        