class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curSum=0
        res=0
        hashmap={0:1}
        for i in range(len(nums)):
            curSum+=nums[i]
            diff=curSum-k

            res+=hashmap.get(diff,0)
            hashmap[curSum]=1+hashmap.get(curSum,0)
        return res


            
        