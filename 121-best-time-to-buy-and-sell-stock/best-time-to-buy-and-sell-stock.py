class Solution(object):
    def maxProfit(self, prices):
        buy=0
        sell=1
        maxP=0
        
        while(sell<len(prices)):
           
            if(prices[buy]<prices[sell]):
                maxP=max(maxP,prices[sell]-prices[buy])
            else:
                buy=sell
            sell+=1
        return maxP

        return maxP


            

        