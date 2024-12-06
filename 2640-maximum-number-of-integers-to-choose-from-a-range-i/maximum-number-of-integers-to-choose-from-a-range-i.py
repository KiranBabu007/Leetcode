class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned=set(banned)
        ans=0
        s=0
        for i in range(1,n+1):
            
            if i in banned:
                continue
            if s+i<=maxSum:
                s+=i
                print(i,s)
                ans+=1

        return ans


            
        