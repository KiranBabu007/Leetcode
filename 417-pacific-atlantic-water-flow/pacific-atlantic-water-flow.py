class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        r=len(heights)
        c=len(heights[0])
        pac=set()
        atl=set()

        def dfs(row,col,_set):
            _set.add((row,col))
            for dr,dc in [(row+1,col),(row,col+1),(row-1,col),(row,col-1)]:
                if 0<=dr<r and 0<=dc<c and (dr,dc) not in _set and heights[dr][dc]>=heights[row][col]:
                    dfs(dr,dc,_set)
        
        for i in range(r):
            dfs(i,0,pac)
            dfs(i,c-1,atl)
        for j in range(c):
            dfs(0,j,pac)
            dfs(r-1,j,atl)

        return list(pac.intersection(atl))
            
        

        
        