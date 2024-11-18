class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        res=[0]*n
        stack=[]

        for i in range(n):
            while(stack and temperatures[i]>temperatures[stack[-1]]):
                l=stack.pop()
                res[l]=i-l
            stack.append(i)
        return res
        
        