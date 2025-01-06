class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        s=lsum=sum(cardPoints[:k])
        rsum=0
        r=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[r]
            r-=1
            s=max(s,lsum+rsum)
        return s
        