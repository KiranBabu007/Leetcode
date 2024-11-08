class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return
        island=0
        vis=set()
        rows,cols=len(grid),len(grid[0])

        def bfs(r,c):
            q=collections.deque()
            vis.add((r,c))
            q.append((r,c))
            while(q):
                row,col=q.popleft()
                directions=[[0,-1],[0,1],[1,0],[-1,0]]
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if r in range(rows) and c in range(cols) and (r,c) not in vis and grid[r][c]=="1":
                        vis.add((r,c))
                        q.append((r,c))


                


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in vis:
                    bfs(i,j)
                    island+=1
        return island

        