class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        winner=0
        beaten=set()
        r=len(grid)
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1 and j not in beaten:
                    winner=i
                    beaten.add(j)
        return winner
        