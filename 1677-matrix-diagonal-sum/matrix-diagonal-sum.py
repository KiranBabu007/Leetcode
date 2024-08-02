class Solution(object):
    def diagonalSum(self, mat):
        n=len(mat)
        lsum,rsum=0,0

        for i in range(len(mat)):
            lsum+=mat[i][i]
            rsum+=mat[i][n-1-i]

        if n % 2 != 0:
            mid=n//2
            lsum-=mat[mid][mid]

        return lsum+rsum
        