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
        
        def findComb(t):
            if t in memo:
                return memo[t]
            if t<0:
                return float('inf')
            if t==0:
                return 0
            ans=float('inf')
            for prime in p:
                ans=min(ans,1+findComb(t-prime,))
            memo[t]=ans
            return memo[t]
        return findComb(n)


        