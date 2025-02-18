class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 
        rows=len(grid)
        cols=len(grid[0])
        visited=set()

        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    if 0<=dr+row<rows and 0<=dc+col<cols and grid[dr+row][dc+col]=="1":
                        q.append((dr+row,dc+col))
                        grid[dr+row][dc+col]=0
     
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    bfs(i,j)
                    count+=1
        return count

            
                    


        