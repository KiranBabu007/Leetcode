class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp=sorted(nums)
        
        hashmap={}
        for i in range(len(nums)):
            hashmap[temp[i]]=min(hashmap.get(temp[i],float('inf')),i)
        res=[]
        for i in nums:
            res.append(hashmap[i])
        return res

                

        