class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        ans=high
        while(low<high):
            mid=(low+high)//2
            k = sum(math.ceil(pile / mid) for pile in piles)
            if k<=h:
                ans=min(ans,mid)
                high=mid
            else:
                low=mid+1
        return ans
        