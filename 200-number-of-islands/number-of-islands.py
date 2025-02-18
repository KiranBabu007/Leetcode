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
                    new_row,new_col=dr+row,dc+col
                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]=="1" and (new_row,new_col) not in visited:
                        q.append((new_row,new_col))
                        visited.add((new_row,new_col))
                        
        visited=set()
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    bfs(i,j)
                    visited.add((i,j))
                    count+=1
        return count

            
                    


        