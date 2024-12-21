class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r=len(grid)
        c=len(grid[0])
        p=0
        d=[[0,1],[0,-1],[1,0],[-1,0]]      
        for i in range(r):
            for j in range(c):  
                if(grid[i][j]==1):
                    p+=4
                    for dr,dc in d:
                        newr,newc=i+dr,j+dc
                        if(newr in range(r) and newc in range(c) and grid[newr][newc]==1):
                            p-=1
        
        return p


        