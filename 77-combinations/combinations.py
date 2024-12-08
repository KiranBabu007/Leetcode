class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def findComb(ind,n,k,path,ans):
            if len(path)==k:
                ans.append(path[:])
            for i in range(ind,n+1):
                path.append(i)
                findComb(i+1,n,k,path,ans)
                path.pop()
        ans=[]
        findComb(1,n,k,[],ans)
       
        return ans
        