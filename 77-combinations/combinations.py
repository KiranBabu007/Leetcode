class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def findComb(ind,path):
            if len(path)==k:
                ans.append(path[:])
            for i in range(ind,n+1):
                path.append(i)
                findComb(i+1,path)
                path.pop()
        ans=[]
        findComb(1,[])
       
        return ans
        