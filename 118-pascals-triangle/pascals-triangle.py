class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        for i in range(numRows):
            l=[]
            for j in range(i+1):
                if j==0:
                    ans=1
                    l.append(ans)
                    continue
                ans=ans*(i+1-j)
                ans=ans/j
                l.append(ans)
            res.append(l)
        return res
        

        