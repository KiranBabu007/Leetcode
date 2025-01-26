class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows,cols=len(grid),len(grid[0])

        rcnt=[0] * rows
        ccnt=[0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    rcnt[r]+=1
                    ccnt[c]+=1
        res=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and max(rcnt[r],ccnt[c])>1:
                    res+=1
        return res
                    
        

        