class Solution(object):
    def orangesRotting(self, grid):
        rows,cols=len(grid),len(grid[0])
        queue=deque()
        fresh=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append([i,j,0])
                if grid[i][j]==1:
                    fresh+=1
        
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        res=0
        while queue:
            r,c,t=queue.popleft()
            for dr,dc in directions:
                x,y=dr+r,dc+c
                if 0 <= x < rows and 0 <= y < cols and grid[x][y]==1:
                    grid[x][y]=2
                    fresh-=1
                    queue.append([x,y,t+1])
            res=t
        return res if not fresh else -1
        
        
                


        