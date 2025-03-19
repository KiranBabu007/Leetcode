class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        c=sorted(c,key=lambda key:c[key],reverse=True)
        
        return c[:k]
        