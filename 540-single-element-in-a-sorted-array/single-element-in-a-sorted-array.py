class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=Counter(nums)

        for i in c:
            if c[i]==1:
                return i
        