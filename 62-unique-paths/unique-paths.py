class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo={}
        def findpath(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r>=m or c>=n:
                return 0
            if r==m-1 and c==n-1:
                return 1
            memo[(r+1,c)]=findpath(r+1,c)
            memo[(r,c+1)]=findpath(r,c+1)
            return memo[(r+1,c)]+memo[(r,c+1)]

        return findpath(0,0)
        