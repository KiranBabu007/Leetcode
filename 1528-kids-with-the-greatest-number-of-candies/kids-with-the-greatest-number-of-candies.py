class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=max(candies)
        l=[]
        for i in candies:
            if i+extraCandies >= n:
                l.append(True)
            else:
                l.append(False)
        return l
        