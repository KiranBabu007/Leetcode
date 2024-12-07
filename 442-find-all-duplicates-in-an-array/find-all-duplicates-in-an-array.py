class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=Counter(nums)
        print(c,len(c))
        l=[i for i in c if c[i]>1]

        return l