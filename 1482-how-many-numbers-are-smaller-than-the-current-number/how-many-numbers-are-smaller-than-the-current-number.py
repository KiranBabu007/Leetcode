class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in nums:
            c=0
            for r in nums:
                if r<i:
                    c+=1
            res.append(c)
        return res
                

        