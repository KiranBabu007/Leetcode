class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo=[-1] *( n+1)
        def climb(n):
            if n<=2:
                memo[n]=n
                return n
            if memo[n]==-1:
                memo[n]=climb(n-1)+climb(n-2)
            return memo[n]
        return climb(n)

        