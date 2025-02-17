class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        ans=0
        for i in logs:
            if i=="../":
                ans=max(0,ans-1)
            elif i=="./":
                continue
            else:
                ans+=1
        return ans 

        