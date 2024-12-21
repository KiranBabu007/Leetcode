class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r=len(grid)
        c=len(grid[0])
        visit=set()
        def dfs(row,col):
            if (0>row or 0>col or row>=r or col>=c or grid[row][col]==0):
                return 1
            if (row,col) in visit:
                return 0
            visit.add((row,col))
            p=dfs(row,col+1)
            p+=dfs(row,col-1)
            p+=dfs(row+1,col)
            p+=dfs(row-1,col)
            return p

        for i in range(r):
            for j in range(c):  
                if(grid[i][j]==1):
                    return dfs(i,j)
        return p


        