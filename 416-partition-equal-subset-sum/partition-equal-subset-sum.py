class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total=sum(nums)
        if total%2!=0:
            return False

        target=total/2

        dp=set([0])

        for n in nums:
            l=set()
            for i in dp:
                if i+n==target:
                    return True
                l.add(i+n)
            dp.update(l)
        return False
                

        