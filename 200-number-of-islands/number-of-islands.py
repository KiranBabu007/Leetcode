class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 

        rows=len(grid)
        cols=len(grid[0])
        islands=0
        visited=set()

        def bfs(r,c):
            q=collections.deque()
            directions=[[0,-1],[0,1],[1,0],[-1,0]]
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c]=='1' and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
     
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and (i,j) not in visited:
                    bfs(i,j)
                    islands+=1
        return islands

        