class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res=float("-inf")
        wsum=sum(nums[:k])
        res=wsum
        for i in range(k,len(nums)):
            wsum+=nums[i]-nums[i-k]
            res=max(res,wsum)

        return res/k

            
        