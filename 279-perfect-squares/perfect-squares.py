class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=3:
            return n
        num=int(sqrt(n))
        p=[]
        memo={}
        for i in range(1,num+1):
            p.append(i*i)
        
        dp=[float('inf')] * (n+1)

        for i in range(1,n+1):
            if i in p:
                dp[i]=1
                continue
            for square in p:
                if i>square:
                    dp[i]=min(dp[i],1+dp[i-square])
        return dp[n]






        