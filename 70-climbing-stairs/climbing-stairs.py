class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1 for _ in range(n+1)]
        print(dp)
        def Climb(n):
            if n<0:
                return 0
            if n==0:
                return 1
            if(dp[n]!=-1):
                return dp[n]
            dp[n]=Climb(n-1)+Climb(n-2)
            return Climb(n-1)+Climb(n-2)
        return Climb(n)
        