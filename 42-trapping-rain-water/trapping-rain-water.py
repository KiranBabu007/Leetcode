class Solution(object):
    def trap(self, height):
        n=len(height)
        left=[0]*n
        right=[0]*n
        m=0

        for i in range(n):
            m=max(height[i],m)
            left[i]=m
        m=0
        for i in range(n-1,-1,-1):
            m=max(height[i],m)
            right[i]=m
        l=[min(left[i],right[i])-height[i] for i in range(n)]

        return sum(l)

        