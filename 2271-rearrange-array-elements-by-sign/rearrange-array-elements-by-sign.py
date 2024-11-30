class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p,n=0,1
        res=[0]* len(nums)
        for i in nums:
            if i>0:
                res[p]=i
                p+=2
            else:
                res[n]=i
                n+=2
        return res

        