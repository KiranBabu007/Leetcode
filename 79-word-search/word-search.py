class Solution(object):
    def exist(self, board, word):
        row,col=len(board),len(board[0])
        def dfs(r,c,i):
            if i==len(word):
                return True
            if(r<0 or c<0 or r>=row or c>=col or word[i]!=board[r][c]):
                return False
            t=board[r][c]
            board[r][c]="#"

            res=(dfs(r+1,c,i+1) or 
            dfs(r-1,c,i+1) or 
            dfs(r,c+1,i+1) or 
            dfs(r,c-1,i+1))
            board[r][c]=t

            return res
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False
        