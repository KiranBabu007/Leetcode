class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        n=len(height)
        l,r,res=0,n-1,0

        for i in range(n):
            area=(r-l)*min(height[l],height[r])
            res=max(res,area)

            if(height[l]<=height[r]):
                l+=1
            else:
                r-=1
        return res


        