class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first,second=1,1

        for i in range(n-1):
            t=first
            first=first+second
            second=t
        return first
            

        return second
        
        