class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp=[[0 for j in range(len(text1)+1)] for i in range(len(text2)+1)]

        for i in range(len(text2)-1,-1,-1):
            for j in range(len(text1)-1,-1,-1):
                if text2[i]==text1[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1]) 
        return dp[0][0]

        