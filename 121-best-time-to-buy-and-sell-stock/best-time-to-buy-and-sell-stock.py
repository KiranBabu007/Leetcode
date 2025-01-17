class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        r=1
        maxp=0
        while r<len(prices):
            if prices[l]<prices[r]:
                maxp=max(maxp,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return maxp
            
        