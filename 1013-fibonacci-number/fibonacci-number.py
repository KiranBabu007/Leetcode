class Solution(object):
    def fib(self, n):
        if n<=1:
            return n
        f=[0,1]
        for i in range(2,n+1):
            f.append(f[i-1]+f[i-2])
        return f[n]
        