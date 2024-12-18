class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        answer=[]
        for i in range(len(prices)):
            flag=0
            for j in range(i+1,len(prices)):
                if j>i and prices[j]<=prices[i]:
                    answer.append(prices[i]-prices[j])
                    flag=1
                    break
            if flag==0:
                answer.append(prices[i])
        return answer