class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n ==1:
            return 1
        a=0
        b=1
        c=0
        for i in range(n-1):
            c=a+b
            a=b
            b=c
        return c
        