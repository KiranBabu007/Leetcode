class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    for row in range(r):
                        if matrix[row][j]==0:
                            continue
                        matrix[row][j]='#'
                    for col in range(c):
                        if matrix[i][col]==0:
                            continue
                        matrix[i][col]='#'
        for i in range(r):
            for j in range(c):
                if matrix[i][j]=='#':
                    matrix[i][j]=0

        
        