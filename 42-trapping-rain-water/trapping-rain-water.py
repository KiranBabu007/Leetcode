class Solution(object):
    def trap(self, height):
        
        left=[]
        right=[]
        m=0

        for i in range(len(height)):
            m=max(height[i],m)
            left.append(m)
        m=0
        for i in range(len(height)-1,-1,-1):
            m=max(height[i],m)
            right.append(m)
        right.reverse() 
        l=[min(left[i],right[i])-height[i] for i in range(len(height))]

        return sum(l)

        