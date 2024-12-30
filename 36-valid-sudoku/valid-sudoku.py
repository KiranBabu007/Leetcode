class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowset=defaultdict(set)
        colset=defaultdict(set)
        squareset=defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if ( board[i][j] in rowset[i] or board[i][j] in colset[j] or board[i][j] in squareset[(i//3,j//3)] ):
                    return False
                rowset[i].add(board[i][j])
                colset[j].add(board[i][j])
                squareset[(i//3,j//3)].add(board[i][j])
        return True
        