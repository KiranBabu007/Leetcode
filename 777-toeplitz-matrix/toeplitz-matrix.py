class Solution(object):
    def isToeplitzMatrix(self, matrix):
        r=len(matrix)
        c=len(matrix[0])
        if not matrix or not matrix[0]:
            return True
        for i in range(r-1):
            for j in range(c-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True

        