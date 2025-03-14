class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])

        memo={}

        def findPaths(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r>=row or c>=col:
                return 0
            if obstacleGrid[r][c]==1:
                return 0
            if r==row-1 and c==col-1:
                return 1
            memo[(r+1,c)]=findPaths(r+1,c)
            memo[(r,c+1)]=findPaths(r,c+1)
            return memo[(r+1,c)]+memo[(r,c+1)]           
        return findPaths(0,0)




        

        